from glob import glob
import os
import pkg_resources

import typing as t

import functools
from tutor import hooks as tutor_hooks
from .hooks import SYNC_WAVES_ORDER_ATTRS_TYPE, SYNC_WAVES_ORDER

from .__about__ import __version__


CORE_SYNC_WAVES_ORDER: t.Dict[str, SYNC_WAVES_ORDER_ATTRS_TYPE] = {
    "jobs": {
        'drydock-mysql-job': 1,
        'drydock-mongodb-job': 1,
        'drydock-lms-job': 2,
        'drydock-cms-job': 3,
        'drydock-notes-job-mysql': 4,
        'drydock-minio-job': 4,
        'drydock-mfe-lms-job': 4,
        'drydock-forum-job': 4
    },
    "deployments": {
        'lms': 1,
        'cms': 1,
        'lms-worker': 1,
        'cms-worker': 1,
        'forum': 1,
        'cms-debug': 1,
        'lms-debug': 1,
    },
    "ingresses": {
        'ingress-debug': 1,
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


@tutor_hooks.Actions.PLUGIN_LOADED.add()
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
    return get_sync_waves_order()[kind][resource_name]

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

tutor_hooks.Filters.ENV_TEMPLATE_VARIABLES.add_items(
    [
        ('iter_sync_waves_order', iter_sync_waves_order),
        ('get_sync_waves_for_resource', get_sync_waves_for_resource),
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
