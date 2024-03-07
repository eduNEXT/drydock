from glob import glob
import os
import yaml
import pkg_resources

from tutor import env as tutor_env
from tutor import hooks as tutor_hooks

from .__about__ import __version__

INSTALLATION_PATH = f'{os.getcwd()}/env'

INIT_JOBS_SYNC_WAVE = -100


@tutor_hooks.Actions.PLUGINS_LOADED.add()
def get_init_tasks():
    """Return the list of init tasks to run."""
    init_tasks = list(tutor_hooks.Filters.CLI_DO_INIT_TASKS.iterate())

    # Standarize deprecated COMMANDS_INIT Filter, to be removed in palm or later
    standarized_commands = []
    for service, init_path in list(tutor_hooks.Filters.COMMANDS_INIT.iterate()):
        standarized_commands.append((service, tutor_env.read_template_file(*init_path)))

    init_tasks.extend(standarized_commands)

    templates_path = f'{INSTALLATION_PATH}/k8s/jobs.yml'
    templates = list(yaml.load_all(open(templates_path, 'r', encoding='utf-8'), Loader=yaml.FullLoader))

    response = []
    for i, (service, definition) in enumerate(init_tasks):
        for template in templates:
            if template['metadata']['name'] == service + '-job':
                data = dict()
                container = template['spec']['template']['spec']['containers'][0]
                data['volumes'] = template['spec']['template']['spec']['volumes'] if 'volumes' in template['spec']['template']['spec'] else []
                data['name'] = service
                data['command'] = definition
                data['image'] = template['spec']['template']['spec']['containers'][0]['image']
                data['env'] = container['env'] if 'env' in container else []
                data['volumeMounts'] = container['volumeMounts'] if 'volumeMounts' in container  else []
                data['syncwave'] = INIT_JOBS_SYNC_WAVE + i
                data['iteration'] = i

                response.append(data)

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
    ]
)
