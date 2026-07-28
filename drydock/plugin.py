import base64
import functools
import hashlib
import importlib.resources
import os
import typing as t
from glob import glob

import click
from tutor import env as tutor_env
from tutor import hooks as tutor_hooks
from tutor import serialize, types
from tutor.exceptions import TutorError
from tutor.commands.jobs import do_callback
from tutor.commands.k8s import k8s

from drydock.__about__ import __version__
from drydock.hooks import SYNC_WAVES_ORDER, SYNC_WAVES_ORDER_ATTRS_TYPE

INIT_JOBS_SYNC_WAVE = 1

TUTOR_CONFIG: types.Config = {}

tutor_hooks.Filters.CONFIG_DEFAULTS.add_items(
    [
        ("DRYDOCK_VERSION", __version__),
        ("DRYDOCK_INIT_JOBS", False),
        ("DRYDOCK_INIT_JOBS_EXCLUDED", []),
        ("DRYDOCK_CMS_SSO_USER", "cms"),
        ("DRYDOCK_AUTO_TLS", True),
        ("DRYDOCK_MIGRATE_FROM", 0),
        ("DRYDOCK_INGRESS", True),
        ("DRYDOCK_INGRESS_CLASS", "traefik"),
        ("DRYDOCK_INGRESS_EXTRA_HOSTS", []),
        ("DRYDOCK_INGRESS_LMS_EXTRA_HOSTS", []),
        ("DRYDOCK_NEWRELIC_LICENSE_KEY", ""),
        ("DRYDOCK_CUSTOM_CERTS", {}),
        ("DRYDOCK_LETSENCRYPT_EMAIL", "{{ CONTACT_EMAIL }}"),
        ("DRYDOCK_ENABLE_MULTITENANCY", True),
        ("DRYDOCK_ENABLE_SCORM", True),
        ("DRYDOCK_POD_LIFECYCLE", True),
        ("DRYDOCK_PDB_MINAVAILABLE_PERCENTAGE_LMS", 0),
        ("DRYDOCK_PDB_MINAVAILABLE_PERCENTAGE_LMS_WORKER", 0),
        ("DRYDOCK_PDB_MINAVAILABLE_PERCENTAGE_CMS", 0),
        ("DRYDOCK_PDB_MINAVAILABLE_PERCENTAGE_CMS_WORKER", 0),
        ("DRYDOCK_PDB_MINAVAILABLE_PERCENTAGE_MFE", 0),
        ("DRYDOCK_PDB_MINAVAILABLE_PERCENTAGE_FORUM", 0),
        ("DRYDOCK_PDB_MINAVAILABLE_PERCENTAGE_CADDY", 0),
        (
            "DRYDOCK_POST_INIT_DEPLOYMENTS",
            ["lms", "cms", "forum", "lms-worker", "cms-worker", "superset", "superset-worker", "superset-celery-beat"],
        ),
        ("DRYDOCK_REGISTRY_CREDENTIALS", ""),
        ("DRYDOCK_MAINTENANCE_ENABLED", False),
        ("DRYDOCK_MAINTENANCE_ALLOWED_IPS", []),
        ("DRYDOCK_MAINTENANCE_PAGE_DIR", ""),
    ]
)

tutor_hooks.Filters.CONFIG_OVERRIDES.add_items(
    [
        ("FORUM_MONGODB_DATABASE", "cs_comments_service"),
        ("MONGODB_ROOT_USERNAME", ""),
        ("MONGODB_ROOT_PASSWORD", ""),
    ]
)


@tutor_hooks.Actions.CONFIG_LOADED.add()
def _capture_config(config: types.Config) -> None:
    global TUTOR_CONFIG
    TUTOR_CONFIG = config


# This function is taken from
# https://github.com/overhangio/tutor/blob/v16.1.8/tutor/commands/k8s.py#L182
def _load_jobs(tutor_conf: types.Config) -> t.Iterable[t.Any]:
    jobs = str(tutor_env.render_file(tutor_conf, "k8s", "jobs.yml").strip())
    for manifest in serialize.load_all(jobs):
        if manifest["kind"] == "Job":
            yield manifest


# The definition of the init tasks is taken and adapted from
# https://github.com/overhangio/tutor/blob/v16.1.8/tutor/commands/jobs.py#L65
# and https://github.com/overhangio/tutor/blob/v16.1.8/tutor/commands/k8s.py#L82
def get_init_tasks():
    """Return the list of init tasks to run."""
    if not TUTOR_CONFIG:
        return []
    init_tasks = list(tutor_hooks.Filters.CLI_DO_INIT_TASKS.iterate())
    jobs = TUTOR_CONFIG.get("DRYDOCK_INIT_JOBS_EXCLUDED", [])
    if not isinstance(jobs, list):
        click.secho("'DRYDOCK_INIT_JOBS_EXCLUDED' must be a list. Ignoring.", fg="yellow")
        jobs = []
    excluded_init_jobs = set(jobs)

    for i, (service, command) in enumerate(init_tasks):
        for template in _load_jobs(TUTOR_CONFIG):
            if template["metadata"]["name"] != service + "-job" or template["metadata"]["name"] in excluded_init_jobs:
                continue

            render_command = tutor_env.render_str(TUTOR_CONFIG, command)

            template["metadata"]["name"] = "drydock-" + template["metadata"]["name"] + "-" + str(i)
            template["metadata"]["labels"].update(
                {
                    "app.kubernetes.io/component": "drydock-job",
                    "drydock.io/target-service": template["metadata"]["name"],
                    "drydock.io/runner-service": template["metadata"]["name"],
                }
            )
            template["metadata"]["annotations"] = {
                "argocd.argoproj.io/sync-wave": INIT_JOBS_SYNC_WAVE + i * 2,
                "argocd.argoproj.io/hook": "Sync",
                "argocd.argoproj.io/hook-delete-policy": "HookSucceeded,BeforeHookCreation",
            }

            shell_command = ["sh", "-e", "-c"]
            if template["spec"]["template"]["spec"]["containers"][0].get("command") == []:
                # In some cases, we need to bypass the container entrypoint.
                # Unfortunately, AFAIK, there is no way to do so in K8s manifests. So we mark
                # some jobs with "command: []". For these jobs, the entrypoint becomes "sh -e -c".
                # We do not do this for every job, because some (most) entrypoints are actually useful.
                template["spec"]["template"]["spec"]["containers"][0]["command"] = shell_command
                container_args = [render_command]
            else:
                container_args = shell_command + [render_command]

            template["spec"]["template"]["spec"]["containers"][0]["args"] = container_args
            template["spec"]["backoffLimit"] = 1
            template["spec"]["ttlSecondsAfterFinished"] = 3600

            yield serialize.dumps(template)


CORE_SYNC_WAVES_ORDER: SYNC_WAVES_ORDER_ATTRS_TYPE = {
    "drydock-upgrade-lms-job": 50,
    "drydock-upgrade-cms-job": 51,
    "deployments:post-init-apps": 100,
    "horizontalpodautoscalers:all": 150,
}


@SYNC_WAVES_ORDER.add()
def _add_core_sync_waves_order(sync_waves_config: SYNC_WAVES_ORDER_ATTRS_TYPE) -> SYNC_WAVES_ORDER_ATTRS_TYPE:
    sync_waves_config.update(CORE_SYNC_WAVES_ORDER)
    return sync_waves_config


@functools.cache
def get_sync_waves_order() -> SYNC_WAVES_ORDER_ATTRS_TYPE:
    """
    This function is cached for performance.
    """
    return SYNC_WAVES_ORDER.apply({})


@tutor_hooks.Actions.PLUGIN_LOADED.add()
def _clear_sync_waves_order_cache(_name: str) -> None:
    """
    Don't forget to clear cache, or we'll have some strange surprises...
    """
    get_sync_waves_order.cache_clear()


def iter_sync_waves_order() -> t.Iterable[SYNC_WAVES_ORDER_ATTRS_TYPE]:
    """
    Yield:
        (name, dict)
    """
    yield from get_sync_waves_order().items()


def get_sync_waves_for_resource(resource_name: str) -> int:
    """
    Args:
        resource_name: the name of the resource
    Returns:
        int
    """
    return get_sync_waves_order().get(resource_name, 0)


DEFAULT_MAINTENANCE_PAGE_DIR = str(
    importlib.resources.files("drydock") / "templates" / "drydock" / "maintenance-default"
)


def _resolve_maintenance_dir(page_dir: str) -> str:
    """
    Resolve the directory holding the maintenance page assets.

    An empty ``page_dir`` falls back to the plugin's built-in default page.
    Relative paths are resolved against the Tutor root when it is available.
    """
    if not page_dir:
        return DEFAULT_MAINTENANCE_PAGE_DIR
    if os.path.isabs(page_dir):
        return page_dir
    try:
        root = click.get_current_context().obj.root
        return os.path.join(root, page_dir)
    except (RuntimeError, AttributeError):
        return os.path.abspath(page_dir)


def get_maintenance_files(page_dir: str = "") -> list[dict[str, t.Any]]:
    """
    Return the top-level files of the maintenance page directory.

    Only top-level files are returned because ConfigMap keys cannot contain
    ``/``. Text files go into ``data``; binary files are base64-encoded into
    ``binaryData``. The maintenance page should reference its assets relatively
    (e.g. ``./style.css``), since they all land in the same served directory.
    """
    base = _resolve_maintenance_dir(page_dir)
    if not os.path.isdir(base):
        raise TutorError(f"DRYDOCK_MAINTENANCE_PAGE_DIR: directory does not exist: {base}")
    files: list[dict[str, t.Any]] = []
    for name in sorted(os.listdir(base)):
        full_path = os.path.join(base, name)
        if not os.path.isfile(full_path):
            continue
        with open(full_path, "rb") as asset:
            raw = asset.read()
        try:
            files.append({"name": name, "binary": False, "data": raw.decode("utf-8")})
        except UnicodeDecodeError:
            files.append({"name": name, "binary": True, "data": base64.b64encode(raw).decode("ascii")})
    if not any(asset["name"] == "index.html" for asset in files):
        raise TutorError(
            f"DRYDOCK_MAINTENANCE_PAGE_DIR: no index.html found in {base}. "
            "The maintenance page entry point must be named index.html."
        )
    return files


def maintenance_assets_checksum(page_dir: str = "") -> str:
    """
    Short content hash of the maintenance assets.

    Used to suffix the ConfigMap name and annotate the Caddy pod template, so
    that updating the page triggers a rollout.
    """
    digest = hashlib.sha256()
    for asset in get_maintenance_files(page_dir):
        digest.update(asset["name"].encode("utf-8"))
        digest.update(b"\0")
        digest.update(asset["data"].encode("utf-8"))
        digest.update(b"\0")
    return digest.hexdigest()[:12]


################# You don't really have to bother about what's below this line,
################# except maybe for educational purposes :)

# Plugin templates
tutor_hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(str(importlib.resources.files("drydock") / "templates"))
tutor_hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    [
        ("drydock/build", "plugins"),
        ("drydock/apps", "plugins"),
        ("drydock/k8s", "plugins"),
    ],
)
# Load all patches from the "patches" folder
for path in glob(str(importlib.resources.files("drydock") / "patches" / "*")):
    with open(path, encoding="utf-8") as patch_file:
        tutor_hooks.Filters.ENV_PATCHES.add_item(
            (os.path.basename(path), patch_file.read()),
            tutor_hooks.priorities.LOW,  # Apply our changes last to correctly override defaults.
        )


tutor_hooks.Filters.ENV_TEMPLATE_VARIABLES.add_items(
    [
        ("get_init_tasks", get_init_tasks),
        ("iter_sync_waves_order", iter_sync_waves_order),
        ("get_sync_waves_for_resource", get_sync_waves_for_resource),
        ("get_maintenance_files", get_maintenance_files),
        ("maintenance_assets_checksum", maintenance_assets_checksum),
    ]
)

# # init script
with open(
    str(importlib.resources.files("drydock") / "templates" / "drydock" / "task" / "mongodb" / "init"),
    encoding="utf-8",
) as fi:
    tutor_hooks.Filters.CLI_DO_INIT_TASKS.add_item(("mongodb", fi.read()), priority=tutor_hooks.priorities.HIGH)


@click.command(name="delete-dbs", help="Drop all databases")
def delete_dbs_command():
    """
    Utility command to delete the main databases/users created on init.

    We have to manually use `do_callback` instead of relying on the more
    standard `CLI_DO_COMMANDS` filter because we want to skip the initial
    hardcoded checks (deployments for caddy and meillisearch up).
    """

    MONGO_DROP_COMMAND = """
    mongosh \
        --host {% if MONGODB_REPLICA_SET %}{{ MONGODB_REPLICA_SET }}/{% endif %}{{ MONGODB_HOST }} \
        --port {{ MONGODB_PORT }} \
        {% if MONGODB_ROOT_USERNAME %} \
        --username {{ MONGODB_ROOT_USERNAME }} \
        {% endif  %} \
        {% if MONGODB_ROOT_PASSWORD %} \
        --password {{ MONGODB_ROOT_PASSWORD }} \
        {% endif  %} \
        --authenticationDatabase {{ MONGODB_AUTH_SOURCE }} \
        {% if MONGODB_USE_SSL %} --tls true {% endif %} \
        {{ MONGODB_DATABASE }} \
        --eval 'db.dropDatabase()'

    {% if 'forum' in PLUGINS %}
    mongosh \
        --host {% if MONGODB_REPLICA_SET %}{{ MONGODB_REPLICA_SET }}/{% endif %}{{ MONGODB_HOST }} \
        --port {{ MONGODB_PORT }} \
        {% if MONGODB_ROOT_USERNAME %} \
        --username {{ MONGODB_ROOT_USERNAME }} \
        {% endif %} \
        {% if MONGODB_ROOT_PASSWORD %} \
        --password {{ MONGODB_ROOT_PASSWORD }} \
        {% endif %} \
        --authenticationDatabase {{ MONGODB_AUTH_SOURCE }} \
        {% if MONGODB_USE_SSL %} --tls true {% endif %} \
        {{ FORUM_MONGODB_DATABASE }} \
        --eval 'db.dropDatabase()'
    {% endif  %}
    """
    MYSQL_DROP_COMMAND = """
    mysql \
        --user {{ MYSQL_ROOT_USERNAME }} \
        --password="{{ MYSQL_ROOT_PASSWORD }}" \
        --host "{{ MYSQL_HOST }}" \
        --port {{ MYSQL_PORT }} \
        --execute "DROP DATABASE IF EXISTS {{ OPENEDX_MYSQL_DATABASE }};"
    mysql \
        --user {{ MYSQL_ROOT_USERNAME }} \
        --password="{{ MYSQL_ROOT_PASSWORD }}" \
        --host "{{ MYSQL_HOST }}" \
        --port {{ MYSQL_PORT }} \
        --execute "DROP USER IF EXISTS '{{ OPENEDX_MYSQL_USERNAME }}';" \
    {% if 'notes' in PLUGINS %}
    mysql \
        --user {{ MYSQL_ROOT_USERNAME }} \
        --password="{{ MYSQL_ROOT_PASSWORD }}" \
        --host "{{ MYSQL_HOST }}" \
        --port {{ MYSQL_PORT }} \
        --execute 'DROP DATABASE IF EXISTS {{ NOTES_MYSQL_DATABASE }};' \
    mysql \
        --user {{ MYSQL_ROOT_USERNAME }} \
        --password="{{ MYSQL_ROOT_PASSWORD }}" \
        --host "{{ MYSQL_HOST }}" \
        --port {{ MYSQL_PORT }} \
        --execute 'DROP USER IF EXISTS {{ NOTES_MYSQL_USERNAME }};' \
    {% endif %}
    """
    do_callback(
        service_commands=[
            ("mongodb", MONGO_DROP_COMMAND),
            ("mysql", MYSQL_DROP_COMMAND),
        ]
    )


k8s.add_command(delete_dbs_command)
