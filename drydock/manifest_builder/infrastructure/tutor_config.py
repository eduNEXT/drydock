import pkg_resources
import tutor
import yaml

from drydock.manifest_builder.domain.config import DrydockConfig


class TutorConfig(DrydockConfig):
    def __init__(self, context, options: dict):
        self.context = context
        self.options = options

    def get_data(self) -> dict:
        config = tutor.config.load_full(self.context.obj.root)
        return config

    def get_root(self) -> dict:
        return self.context.obj.root


class TutorExtendedConfig(DrydockConfig):
    """Drydock configuration based on tutor."""
    DEFAULT_TEMPLATE_SET = "kustomized/tutor13"

    def __init__(self, context, options: dict):
        """Initialize the class based on the `config_options` from the manifest.

        Parameters
        ----------
        context: clic.core.Context
            context of the current Tutor command.
        options: dict

            - ["template_set"]: template set to render default values from.
        """
        self.context = context
        self.options = options

    def get_data(self) -> dict:
        """Return tutor config values using a template set defaults as fallback.

        Retrieve the Tutor configuration values for the current TUTOR_ROOT and 
        use the the values in `defaults.yml` of the chosen template set

        Returns
        -------
        base: dict
            Tutor configuration values taken from the config.yml at the TUTOR_ROOT
            using the defaults from the template set as a fallback.
        """
        template_set = self.options.get("template_set", self.DEFAULT_TEMPLATE_SET)

        try:
            defaults_path = pkg_resources.resource_filename("drydock", f"templates/{template_set}/defaults.yml")
            with open(defaults_path, encoding="utf-8") as file:
                base = yaml.safe_load(file)
        except FileNotFoundError:
            base = {}

        config = tutor.config.load_full(self.get_root())
        base.update(config)
        return base

    def get_root(self) -> str:
        return self.context.obj.root
