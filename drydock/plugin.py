from glob import glob
import os
import pkg_resources

from tutor import hooks

from .__about__ import __version__

VERSION_LIST = [
    ('MAPLE', '13'),
    ('NUTMEG', '14'),
    ('OLIVE', '15'),
    ('PALM', '16'),
    ('QUINCE', '17'),
]

PRIORITY_LIST = [
    ('job', 'migration-maple-lms-job'),
    ('job', 'migration-maple-cms-job'),
    ('job', 'migration-nutmeg-lms-job'),
    ('job', 'migration-olive-lms-job'),

    ('job', 'drydock-mysql-job'),
    ('job', 'drydock-notes-job-mysql'),
    ('job', 'drydock-mongodb-job'),
    ('job', 'drydock-minio-job'),
    ('job', 'drydock-mfe-lms-job'),
    ('job', 'drydock-lms-job'),
    ('job', 'drydock-forum-job'),
    ('job', 'drydock-cms-job'),

    ('deployment', 'lms'),
    ('deployment', 'cms'),
    ('deployment', 'lms-worker'),
    ('deployment', 'cms-worker'),
    ('deployment', 'forum'),

    ('deployment', 'cms-debug'),
    ('deployment', 'lms-debug'),
    ('ingress', 'ingress-debug'),

    ('deployment', 'lms-debug'),
    ('deployment', 'cms-debug'),
    ('ingress', 'ingress-debug'),
]

def get_priority(kind, name):
    """ Return the priority of a k8s object."""
    for i, (k, n) in enumerate(PRIORITY_LIST):
        if k == kind and n == name:
            return i + 1
    return len(PRIORITY_LIST)

################# Configuration
config = {
    # Add here your new settings
    "defaults": {
        "VERSION": __version__,
        "INIT_JOBS": False,
        "MIGRATE_FROM": "",
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

def get_migration_list():
    """
    Return a list of migration jobs to run based on the MIGRATE_FROM and VERSION
    settings.
    """
    migration_list = []
    migrate_from = config["defaults"]["MIGRATE_FROM"]
    migrate_to = config['defaults']['VERSION'].split('.', maxsplit=1)[0]
    for name, version in VERSION_LIST:
        if migrate_from.lower() == name.lower():
            migrate_from = version
        if migrate_from <= version <= migrate_to:
            migration_list.append(name.lower())
    return migration_list


hooks.Filters.CONFIG_DEFAULTS.add_items([("OPENEDX_DEBUG_COOKIE", "ednx_enable_debug")])
hooks.Filters.CONFIG_OVERRIDES.add_items([
        # This values are not prefixed with DRYDOCK_
        ("MONGODB_ROOT_USERNAME", ""),
        ("MONGODB_ROOT_PASSWORD", ""),
        ("MONGODB_AUTH_SOURCE", "{{ MONGODB_DATABASE }}"),
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

hooks.Filters.ENV_TEMPLATE_VARIABLES.add_items(
    [
        ('get_priority', get_priority),
        ('get_migration_list', get_migration_list),
    ]
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
