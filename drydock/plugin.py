from glob import glob
from typing import Any, Iterable
import os
import click
import pkg_resources

import typing as t

import functools
from .hooks import SYNC_WAVES_ORDER_ATTRS_TYPE, SYNC_WAVES_ORDER

from tutor import hooks as tutor_hooks
from tutor import env as tutor_env
from tutor import serialize, types
from tutor import config as tutor_config

from .__about__ import __version__

INIT_JOBS_SYNC_WAVE = 1

VERSION_LIST = [
    ('MAPLE', '13'),
    ('NUTMEG', '14'),
    ('OLIVE', '15'),
    ('PALM', '16'),
    ('QUINCE', '17'),
]

def _load_jobs(tutor_conf: types.Config) -> Iterable[Any]:
    jobs = tutor_env.render_file(tutor_conf, "k8s", "jobs.yml").strip()
    for manifest in serialize.load_all(jobs):
        if manifest["kind"] == "Job":
            yield manifest

def get_init_tasks():
    """Return the list of init tasks to run."""
    init_tasks = list(tutor_hooks.Filters.CLI_DO_INIT_TASKS.iterate())
    context = click.get_current_context().obj
    tutor_conf = tutor_config.load(context.root)

    # Standarize deprecated COMMANDS_INIT and COMMANDS_PRE_INIT Filter
    pre_init_tasks = []
    for service, init_path in tutor_hooks.Filters.COMMANDS_PRE_INIT.iterate():
        pre_init_tasks.append((service, tutor_env.read_template_file(*init_path)))

    init_tasks = pre_init_tasks + init_tasks

    for service, init_path in list(tutor_hooks.Filters.COMMANDS_INIT.iterate()):
        init_tasks.append((service, tutor_env.read_template_file(*init_path)))

    response = []
    for i, (service, command) in enumerate(init_tasks):
        for template in _load_jobs(tutor_conf):
            if template['metadata']['name'] != service + '-job':
                continue

            render_command = tutor_env.render_str(tutor_conf, command)

            template['metadata']['name'] = 'drydock-' + template['metadata']['name'] + '-' + str(i)
            template['metadata']['labels'] = {
                'drydock.io/component': 'job',
                'drydock.io/target-service': template['metadata']['name'],
                'drydock.io/runner-service': template['metadata']['name']
            }
            template['metadata']['annotations'] = {
                'argocd.argoproj.io/sync-wave': INIT_JOBS_SYNC_WAVE + i,
                'argocd.argoproj.io/hook': 'Sync',
                'argocd.argoproj.io/hook-delete-policy': 'HookSucceeded'
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

    return response


def get_upgrade_list():
    """
    Return a list of upgrade target versions based on the MIGRATE_FROM setting.
    """
    context = click.get_current_context().obj
    tutor_conf = tutor_config.load(context.root)

    upgrade_list = []
    if not 'MIGRATE_FROM' in tutor_conf:
        return upgrade_list
    migrate_from = tutor_conf["MIGRATE_FROM"]
    migrate_to = config['defaults']['VERSION'].split('.', maxsplit=1)[0]
    for name, version in VERSION_LIST:
        if migrate_from.lower() == name.lower():
            migrate_from = version
        if migrate_from <= version <= migrate_to:
            upgrade_list.append(name.lower())
    return upgrade_list


CORE_SYNC_WAVES_ORDER: t.Dict[str, SYNC_WAVES_ORDER_ATTRS_TYPE] = {
    "jobs": {
        "drydock-upgrade-lms-job": 50,
        "drydock-upgrade-cms-job": 51
    },
    "deployments": {
        "lms-lifecycle-enabled": 100,
        "cms-lifecycle-enabled": 100,
        "lms-debug": 50,
        "cms-debug": 50,
    },
    "horizontalpodautoscalers": {
        "all": 150
    },
    "ingresses": {
        "ingress-debug": 200
    },
}

# The core sync-waves configs are added with a high priority, such that other users can override or
# remove them.
@SYNC_WAVES_ORDER.add(priority=tutor_hooks.priorities.HIGH)
def _add_core_sync_waves_order(sync_waves_config: t.Dict[str, SYNC_WAVES_ORDER_ATTRS_TYPE]) -> t.Dict[str, SYNC_WAVES_ORDER_ATTRS_TYPE]:
    sync_waves_config.update(CORE_SYNC_WAVES_ORDER)
    return sync_waves_config


@functools.lru_cache(maxsize=None)
def get_sync_waves_order() -> t.Dict[str, SYNC_WAVES_ORDER_ATTRS_TYPE]:
    """
    This function is cached for performance.
    """
    return SYNC_WAVES_ORDER.apply({})


@tutor_hooks.Actions.PLUGIN_LOADED
def _clear_sync_waves_order_cache(_name: str) -> None:
    """
    Don't forget to clear cache, or we'll have some strange surprises...
    """
    get_sync_waves_order.cache_clear()


def iter_sync_waves_order() -> t.Iterable[t.Tuple[str, SYNC_WAVES_ORDER_ATTRS_TYPE]]:
    """
    Yield:
        (name, dict)
    """
    yield from get_sync_waves_order().items()


def get_sync_waves_for_resource(resource_name: str, kind: str) -> SYNC_WAVES_ORDER_ATTRS_TYPE:
    """
    Args:
        resource_name: the name of the resource
        kind: the kind of the resource
    Returns:
        dict
    """
    order = get_sync_waves_order()
    if kind not in order:
        return 0
    if resource_name not in order[kind]:
        return 0
    return order[kind][resource_name]


################# Configuration
config = {
    # Add here your new settings
    "defaults": {
        "VERSION": __version__,
        "INIT_JOBS": False,
        "CMS_SSO_USER": "cms",
        "AUTO_TLS": True,
        "MIGRATE_FROM": "",
        "FLOWER": False,
        "INGRESS": False,
        "INGRESS_EXTRA_HOSTS": [],
        "INGRESS_LMS_EXTRA_HOSTS": [],
        "NEWRELIC": False,
        "NEWRELIC_LICENSE_KEY": "",
        "CUSTOM_CERTS": {},
        "DEBUG": False,
        "LETSENCRYPT_EMAIL": "{{ CONTACT_EMAIL }}",
        "ENABLE_CELERY_TUNING": True,
        "ENABLE_MULTITENANCY": True,
        "ENABLE_SCORM": True,
        "ENABLE_SENTRY": True,
        "SENTRY_DSN": "",
        "POD_LIFECYCLE": True,
        "BYPASS_CADDY": False,
    },
    # Add here settings that don't have a reasonable default for all users. For
    # instance: passwords, secret keys, etc.
    "unique": {
        # "SECRET_KEY": "\{\{ 24|random_string \}\}",
    },
    # Danger zone! Add here values to override settings from Tutor core or other plugins.
    "overrides": {
    },
}

tutor_hooks.Filters.CONFIG_DEFAULTS.add_items([("OPENEDX_DEBUG_COOKIE", "ednx_enable_debug")])
tutor_hooks.Filters.CONFIG_OVERRIDES.add_items([
        # This values are not prefixed with DRYDOCK_
        ("MONGODB_ROOT_USERNAME", ""),
        ("MONGODB_ROOT_PASSWORD", ""),
])


################# You don't really have to bother about what's below this line,
################# except maybe for educational purposes :)

# Plugin templates
tutor_hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(
    pkg_resources.resource_filename("drydock", "templates")
)

tutor_hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    [
        ("drydock/build", "plugins"),
        ("drydock/apps", "plugins"),
        ("drydock/k8s", "plugins"),
    ],
)

# Load all patches from the "patches" folder
for path in glob(
    os.path.join(
        pkg_resources.resource_filename("drydock", "patches"),
        "*",
    )
):
    with open(path, encoding="utf-8") as patch_file:
        tutor_hooks.Filters.ENV_PATCHES.add_item((os.path.basename(path), patch_file.read()))

# Load all configuration entries
tutor_hooks.Filters.CONFIG_DEFAULTS.add_items(
    [
        (f"DRYDOCK_{key}", value)
        for key, value in config["defaults"].items()
    ]
)
tutor_hooks.Filters.CONFIG_UNIQUE.add_items(
    [
        (f"DRYDOCK_{key}", value)
        for key, value in config["unique"].items()
    ]
)
tutor_hooks.Filters.CONFIG_OVERRIDES.add_items(list(config["overrides"].items()))

tutor_hooks.Filters.ENV_TEMPLATE_VARIABLES.add_items(
    [
        ('get_init_tasks', get_init_tasks),
        ('get_upgrade_list', get_upgrade_list),
        ('iter_sync_waves_order', iter_sync_waves_order),
        ('get_sync_waves_for_resource', get_sync_waves_for_resource),
    ]
)

# # init script
with open(
    pkg_resources.resource_filename("drydock", "templates/drydock/task/mongodb/init"),
    encoding="utf-8",
) as fi:
    tutor_hooks.Filters.CLI_DO_INIT_TASKS.add_item(("mongodb", fi.read()), priority=tutor_hooks.priorities.HIGH)
