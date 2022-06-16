from glob import glob
import os
import pkg_resources

from tutor import hooks

from .__about__ import __version__


import click


################# Configuration
config = {
    # Add here your new settings
    "defaults": {
        "VERSION": __version__,
    },
    # Add here settings that don't have a reasonable default for all users. For
    # instance: passwords, secret keys, etc.
    "unique": {
        # "SECRET_KEY": "\{\{ 24|random_string \}\}",
    },
    # Danger zone! Add here values to override settings from Tutor core or other plugins.
    "overrides": {
        "PLATFORM_NAME": "My platform as defined in plugin.py",
    },
}


@click.group(name="drydock", short_help="Manage drydock")
@click.pass_context
def drydock_command(context):
    pass


@click.command(name="save")
@click.pass_context
def save(context):

    from drydock.manifest_builder.application.manifest_builder import ManifestBuilder
    from drydock.manifest_builder.infrastructure import flex_tutor_manifest, tutor_config


    builder = ManifestBuilder(flex_tutor_manifest.FlexibleTutorManifest)
    config = tutor_config.TutorConfig(context=context)
    builder(config)


drydock_command.add_command(save)

hooks.filters.add_items(
    "cli:commands",
    [
        drydock_command,
    ],
)


################# You don't really have to bother about what's below this line,
################# except maybe for educational purposes :)

# Plugin templates
hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(
    pkg_resources.resource_filename("tutor_plugin", "templates")
)
hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    [
        ("tutor_plugin/build", "plugins"),
        ("tutor_plugin/apps", "plugins"),
    ],
)
# Load all patches from the "patches" folder
for path in glob(
    os.path.join(
        pkg_resources.resource_filename("tutor_plugin", "patches"),
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
