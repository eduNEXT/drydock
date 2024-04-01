from glob import glob
import os
import pkg_resources

from tutor import hooks

from .__about__ import __version__


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

        "CMS_LIMIT_CPU": 1,
        "CMS_LIMIT_MEMORY": "2Gi",
        "CMS_MAX_REPLICAS": 3,
        "CMS_MIN_REPLICAS": 3,
        "CMS_REQUEST_CPU": "600m",
        "CMS_REQUEST_MEMORY": "1Gi",
        "CMS_TARGET_CPU": 90,
        "CMS_WORKERS_MAX_REPLICAS": 3,
        "CMS_WORKERS_MIN_REPLICAS": 1,
        "CMS_WORKERS_TARGET_CPU": 90,
        "CMS_WORKER_LIMIT_CPU": 1,
        "CMS_WORKER_LIMIT_MEMORY": "2Gi",
        "CMS_WORKER_REQUEST_CPU": "600m",
        "CMS_WORKER_REQUEST_MEMORY": "1Gi",
        "HPA": False,
        "LMS_LIMIT_CPU": 1,
        "LMS_LIMIT_MEMORY": "2Gi",
        "LMS_MAX_REPLICAS": 1,
        "LMS_MIN_REPLICAS": 1,
        "LMS_REQUEST_CPU": "600m",
        "LMS_REQUEST_MEMORY": "1Gi",
        "LMS_TARGET_CPU": 90,
        "LMS_WORKERS_MAX_REPLICAS": 3,
        "LMS_WORKERS_MIN_REPLICAS": 1,
        "LMS_WORKERS_TARGET_CPU": 90,
        "LMS_WORKER_LIMIT_CPU": 1,
        "LMS_WORKER_LIMIT_MEMORY": "2Gi",
        "LMS_WORKER_REQUEST_CPU": "600m",
        "LMS_WORKER_REQUEST_MEMORY": "1Gi",
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
