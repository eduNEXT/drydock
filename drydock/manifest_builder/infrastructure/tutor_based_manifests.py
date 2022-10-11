"""
Collection of tutor based renderers for Kubernetes manifests.
"""
import glob
import os
import shutil
import tempfile
from os.path import join as path_join

import pkg_resources
from tutor import env as tutor_env
from tutor import fmt, hooks
from tutor.exceptions import TutorError

from drydock.manifest_builder.domain.config import DrydockConfig
from drydock.manifest_builder.domain.manifest_repository import ManifestRepository


class BaseManifests(ManifestRepository):
    """Baseline of Kubernetes configuration repository.

    Generates an environment based on Tutor with the relevant Kubernetes configuration
    to be tracked by version control.
    """
    DEFAULT_TEMPLATE_ROOT = "kustomized/tutor13"

    def __init__(self, options: dict) -> None:
        """Initialize the class based on the `manifest_options` from the reference.

        Parameters
        ----------
        options: dict
            Defines additional configuration options for the generations of the
            configuration repository.

            - ["output"]: Name of the directory to store the manifests.
        """
        self.output_dir = options.get("output", "drydock-env")
        self.template_root = options.get("template_root", self.DEFAULT_TEMPLATE_ROOT)
        self.template_targets = [
            f"{self.template_root}/base",
            f"{self.template_root}/extensions",
            f"{self.template_root}/kustomization.yml",
    ]

    def render(self, root: str, config: DrydockConfig) -> None:
        """Register drydock custom templates and render a tutor env."""
        with hooks.Contexts.APP("drydock-base").enter():
            hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(pkg_resources.resource_filename("drydock", "templates"))
            hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
                [(target, "drydock") for target in self.template_targets],
            )
        tutor_env.save(root, config.get_data())
        hooks.Filters.ENV_TEMPLATE_ROOTS.clear(context=hooks.Contexts.APP("drydock-base").name)
        hooks.Filters.ENV_TEMPLATE_TARGETS.clear(context=hooks.Contexts.APP("drydock-base").name)

    def relocate_env(self, src: str, dst: str) -> None:
        """Moves the drydock rendered templates and tutor plugins to src.

        At the moment we render a full tutor env with our templates under
        'env/drydock/default'. The final drydock env is the one in 'env/drydock'
        **plus** the plugin directory that has to be manually relocated to
        'env/drydock/base/plugins'.

        Parameters
        ----------
        src: str
            The inital path where the full tutor env was rendered.
        dst: str
            The path to save the final drydock env.
        """
        base_dir = path_join(src, "env/drydock", f"{self.template_root}")
        plugins_dir = path_join(src, "env/plugins")
        shutil.move(base_dir, dst)
        if os.path.exists(plugins_dir):
            shutil.move(plugins_dir, path_join(dst, "base"))

    def save(self, config: DrydockConfig) -> None:
        """Creates an alternative tutor env with the base openedx installation.

        The generated env consists of a Kustomize application that uses the original
        tutor env as a base in addition to an `extensions` overlay to include additional
        resources.

        Parameters
        ----------
        config: DrydockConfig
            A Tutor configuration extension.
        """
        tutor_root = config.get_root()
        dst = path_join(tutor_root, self.output_dir)
        with tempfile.TemporaryDirectory() as tmpdir:
            src = path_join(tmpdir)
            self.render(src, config)
            shutil.rmtree(path=dst, ignore_errors=True)
            self.relocate_env(src, dst)

        fmt.echo_info(f"Drydock environment generated in {dst}")


class ExtendedManifests(ManifestRepository):
    """Include additional extension points"""

    EXTENSIONS_DIRECTORY = "extra-extensions"

    def __init__(self, options: dict) -> None:
        """Initializes both an ExtendedManifest and a BaseManifests with `options`.

        ExtendedManifest takes an aribitrary Tutor template root provided in the
        options and renders it in the extra-extensions directory from BaseManifests

        Parameters
        ----------
        options: dict
            A superset of options from BaseManifests. In addition to the values expected
            by BaseManifests, include the template root.
        """
        self.options = options
        self.base_manifests = BaseManifests(options=options)

    def save(self, config: DrydockConfig):
        """Create a BaseManifests environment and add arbitrary templates.

        Uses the BaseManifests environment and adds an extra directory `extra-extensions`
        with arbitrary templates taken from extra_templates.

        Parameters
        ----------
        config: DrydockConfig
            A Tutor configuration extension.
        """
        tutor_root = config.get_root()
        dst = path_join(tutor_root, self.options.get("output", "drydock-env"))

        if not self.options.get("extra_templates"):
            self.base_manifests.save(config)
            return

        hooks.Filters.ENV_PATCH("drydock-kustomization-resources").add_item(f"- {self.EXTENSIONS_DIRECTORY}")

        self.base_manifests.save(config)

        with tempfile.TemporaryDirectory() as tmpdir:
            src = path_join(tmpdir)
            self.render(src, config)
            self.relocate_env(src, dst)

    def render(self, root: str, config: DrydockConfig) -> None:
        """Register the arbitrary templates and render them.

        This will add all the files and folders in EXTENSIONS_DIRECTORY
        akin to "EXTENSIONS_DIRECTORY/*".
        Parameters
        ----------
        root: str
            path to use as a Tutor root
        config: DrydockConfig
            Tutor compatible configuration values.
        """
        template_root = self.options.get("extra_templates")
        extensions_path = os.path.abspath(path_join(template_root, "extra-extensions"))

        with hooks.Contexts.APP("drydock-extended").enter():
            hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(template_root)
            hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
                [
                    (f"{self.EXTENSIONS_DIRECTORY}/{os.path.basename(path)}", "drydock/")
                    for path in glob.glob(path_join(extensions_path, "*"))
                ]
            )

        tutor_env.save(root, config.get_data())
        hooks.Filters.ENV_TEMPLATE_ROOTS.clear(context=hooks.Contexts.APP("drydock-extended").name)
        hooks.Filters.ENV_TEMPLATE_TARGETS.clear(context=hooks.Contexts.APP("drydock-extended").name)
        hooks.Filters.ENV_PATCHES.clear(context=hooks.Contexts.APP("drydock-extended").name)

    def relocate_env(self, src: str, dst: str) -> None:
        """Move the templates rendered in extra-extension to the drydock-env.

        Parameters
        ----------
        src: str
            root where the environment was generated
        dst: str
            destination of the final environment
        """
        base_dir = path_join(src, "env/drydock/", f"{self.EXTENSIONS_DIRECTORY}")
        if not os.path.exists(base_dir):
            raise TutorError("[DRYDOCK] Missing extra-extensions folder")
        shutil.move(base_dir, dst)


class GlobalManifests(BaseManifests):
    """Generate environment not bound to tutor env manifests."""

    TEMPLATE_ROOT = "kustomized/global-stack"
    TEMPLATE_TARGETS = [
        f"{TEMPLATE_ROOT}/kustomization.yml",
    ]

    def __init__(self, options: dict) -> None:
        """Initialize the class based on the `manifest_options` from the reference.

        Parameters
        ----------
        options: dict
            Defines additional configuration options for the generations of the
            configuration repository.

            - ["output"]: Name of the directory to store the manifests.
        """
        self.output_dir = options.get("output", "drydock-global-env")

    def relocate_env(self, src: str, dst: str) -> None:
        """Moves the drydock rendered templates a global destination.

        Parameters
        ----------
        src: str
            The initial path where the full tutor env was rendered.
        dst: str
            The path to save the final environment with the global manifests..
        """
        base_dir = path_join(src, "env/drydock", f"{self.TEMPLATE_ROOT}")
        shutil.move(base_dir, dst)
