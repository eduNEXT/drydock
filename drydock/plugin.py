from glob import glob
from typing import Any, Iterable
import os
import click
import pkg_resources

from tutor import env as tutor_env
from tutor import serialize
from tutor import config as tutor_config
from tutor import hooks, types

from .__about__ import __version__

INIT_JOBS_SYNC_WAVE = -100

VERSION_LIST = [
    ('MAPLE', '13'),
    ('NUTMEG', '14'),
    ('OLIVE', '15'),
    ('PALM', '16'),
    ('QUINCE', '17'),
]

def _get_upgrade_jobs(tutor_conf: types.Config):
    upgrade_jobs = []
    if 'MIGRATE_FROM' in tutor_conf and tutor_conf["MIGRATE_FROM"].lower() in [name.lower() for name, _ in VERSION_LIST]:
        command_lms = tutor_env.read_template_file('drydock', 'k8s', 'upgrade-scripts', 'lms.sh')
        command_cms = tutor_env.read_template_file('drydock', 'k8s', 'upgrade-scripts', 'cms.sh')
        upgrade_jobs.append(('lms', command_lms))
        upgrade_jobs.append(('cms', command_cms))

    return upgrade_jobs

def _load_jobs(tutor_conf: types.Config) -> Iterable[Any]:
    jobs = tutor_env.render_file(tutor_conf, "k8s", "jobs.yml").strip()
    for manifest in serialize.load_all(jobs):
        if manifest["kind"] == "Job":
            yield manifest

def get_init_tasks():
    """Return the list of init tasks to run."""
    init_tasks = list(hooks.Filters.CLI_DO_INIT_TASKS.iterate())
    context = click.get_current_context().obj
    tutor_conf = tutor_config.load(context.root)

    # Standarize deprecated COMMANDS_INIT and COMMANDS_PRE_INIT Filter
    pre_init_tasks = []
    for service, init_path in hooks.Filters.COMMANDS_PRE_INIT.iterate():
        pre_init_tasks.append((service, tutor_env.read_template_file(*init_path)))

    init_tasks = pre_init_tasks + init_tasks

    for service, init_path in list(hooks.Filters.COMMANDS_INIT.iterate()):
        init_tasks.append((service, tutor_env.read_template_file(*init_path)))

    upgrade_jobs = _get_upgrade_jobs(tutor_conf)
    if upgrade_jobs:
        init_tasks.extend(upgrade_jobs)

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

hooks.Filters.CONFIG_DEFAULTS.add_items([("OPENEDX_DEBUG_COOKIE", "ednx_enable_debug")])
hooks.Filters.CONFIG_OVERRIDES.add_items([
        # This values are not prefixed with DRYDOCK_
        ("MONGODB_ROOT_USERNAME", ""),
        ("MONGODB_ROOT_PASSWORD", ""),
])


################# You don't really have to bother about what's below this line,
################# except maybe for educational purposes :)

# Plugin templates
hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(
    pkg_resources.resource_filename("drydock", "templates")
)

hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
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
        hooks.Filters.ENV_PATCHES.add_item((os.path.basename(path), patch_file.read()))

# Load all configuration entries
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [
        (f"DRYDOCK_{key}", value)
        for key, value in config["defaults"].items()
    ]
)
hooks.Filters.CONFIG_UNIQUE.add_items(
    [
        (f"DRYDOCK_{key}", value)
        for key, value in config["unique"].items()
    ]
)
hooks.Filters.CONFIG_OVERRIDES.add_items(list(config["overrides"].items()))

hooks.Filters.ENV_TEMPLATE_VARIABLES.add_items(
    [
        ('get_init_tasks', get_init_tasks),
        ('get_upgrade_list', get_upgrade_list),
    ]
)

# # init script
with open(
    pkg_resources.resource_filename("drydock", "templates/drydock/task/mongodb/init"),
    encoding="utf-8",
) as fi:
    hooks.Filters.CLI_DO_INIT_TASKS.add_item(("mongodb", fi.read()), priority=hooks.priorities.HIGH)
