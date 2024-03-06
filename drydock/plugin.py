from glob import glob
import os
import yaml
import pkg_resources

from tutor import hooks as tutor_hooks

from .__about__ import __version__

INSTALLATION_PATH = f'{os.getcwd()}/env'

@tutor_hooks.Actions.PLUGINS_LOADED.add()
def get_init_tasks():
    """Return the list of init tasks to run."""
    init_tasks = list(tutor_hooks.Filters.CLI_DO_INIT_TASKS.iterate())

    templates_path = f'{INSTALLATION_PATH}/k8s/jobs.yml'

    jobs = yaml.load_all(open(templates_path, 'r', encoding='utf-8'), Loader=yaml.FullLoader)

    response = []
    for job in jobs:
        for service, definition in init_tasks:
            if job['metadata']['name'] == service + '-job':
                k8s_data = dict()
                k8s_data['container'] = job['spec']['template']['spec']['containers'][0]
                k8s_data['volumes'] = job['spec']['template']['spec']['volumes'] if 'volumes' in job['spec']['template']['spec'] else []
                k8s_data['name'] = service
                k8s_data['command'] = definition
                k8s_data['image'] = job['spec']['template']['spec']['containers'][0]['image']
                k8s_data['env'] = k8s_data['container']['env'] if 'env' in k8s_data['container'] else []
                k8s_data['volumeMounts'] = k8s_data['container']['volumeMounts'] if 'volumeMounts' in k8s_data['container']  else []


                response.append(k8s_data)
                break

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
