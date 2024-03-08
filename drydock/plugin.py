from glob import glob
import os
import click
import pkg_resources

from tutor import env as tutor_env
from tutor import serialize
from tutor import config as tutor_config
from tutor import hooks

from .__about__ import __version__

INIT_JOBS_SYNC_WAVE = -100


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

    standarized_commands = []
    for service, init_path in list(hooks.Filters.COMMANDS_INIT.iterate()):
        standarized_commands.append((service, tutor_env.read_template_file(*init_path)))


    init_tasks.extend(standarized_commands)

    templates = tutor_env.render_file(tutor_conf, "k8s", "jobs.yml").strip()
    templates = list(serialize.load_all(templates))

    response = []
    for i, (service, definition) in enumerate(init_tasks):
        for template in templates:
            if template['metadata']['name'] != service + '-job':
                continue

            render_definition = tutor_env.render_str(tutor_conf, definition)

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
                container_args = [render_definition]
            else:
                container_args = shell_command + [render_definition]

            template["spec"]["template"]["spec"]["containers"][0]["args"] = container_args
            template["spec"]["backoffLimit"] = 1
            template["spec"]["ttlSecondsAfterFinished"] = 3600


            response.append(serialize.dumps(template))

    return response


################# Configuration
config = {
    # Add here your new settings
    "defaults": {
        "VERSION": __version__,
        "INIT_JOBS": False,
        "CMS_SSO_USER": "cms",
        "AUTO_TLS": True,
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
    ]
)

# # init script
with open(
    pkg_resources.resource_filename("drydock", "templates/drydock/task/mongodb/init"),
    encoding="utf-8",
) as fi:
    hooks.Filters.CLI_DO_INIT_TASKS.add_item(("mongodb", fi.read()), priority=hooks.priorities.HIGH)
