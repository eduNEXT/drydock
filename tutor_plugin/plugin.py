from glob import glob
import os
import pkg_resources
import yaml

from importlib import import_module

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


def import_string(dotted_path):
    """
    Import a dotted module path and return the attribute/class designated by the
    last name in the path. Raise ImportError if the import failed.
    """
    try:
        module_path, class_name = dotted_path.rsplit(".", 1)
        module = import_module(module_path)
        return getattr(module, class_name)
    except ValueError as err:
        raise ImportError("%s doesn't look like a module path" % dotted_path) from err
    except AttributeError as err:
        raise ImportError(
            'Module "%s" does not define a "%s" attribute/class'
            % (module_path, class_name)
        ) from err


@click.group(name="drydock", short_help="Manage drydock")
@click.pass_context
def drydock_command(context):
    pass


@click.command(name="save")
@click.option(
    "-r",
    "--ref",
    envvar="DRYDOCK_REF",
    type=click.Path(resolve_path=True),
    help="Path to the yml file that holds the builder class configuration.",
)
@click.pass_context
def save(context, ref: str):

    with open(ref, encoding="utf-8") as f:
        reference = yaml.load(f, Loader=yaml.SafeLoader)
    app = reference.get('drydock', {})

    Config = import_string(app.get('config_class'))
    Manifest = import_string(app.get('manifest_class'))
    Builder = import_string(app.get('builder_class'))

    build = Builder(
        repository=Manifest(options=app.get('manifest_options', {})),
        options=app.get('builder_options', {}),
    )
    config=Config(context=context, options=app.get('config_options', {}))
    build(config=config)


drydock_command.add_command(save)

hooks.Filters.CLI_COMMANDS.add_item(drydock_command)

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
