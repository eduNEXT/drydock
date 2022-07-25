"""
Collection of tutor based renderers for Kubernetes manifests.
"""
import os
import shutil
import tempfile
from os.path import join as path_join

import pkg_resources
from tutor import env as tutor_env
from tutor import fmt, hooks

from drydock.manifest_builder.domain.config import DrydockConfig
from drydock.manifest_builder.domain.manifest_repository import ManifestRepository


class BaseManifests(ManifestRepository):
    """Baseline of Kubernetes configuration repository.

    Generates an environment based on Tutor with the relevant Kubernetes configuration
    to be tracked by version control.
    """
    TEMPLATE_ROOT = "kustomized/tutor13"
    TEMPLATE_TARGETS = [
        f"{TEMPLATE_ROOT}/base",
        f"{TEMPLATE_ROOT}/extensions",
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
        self.output_dir = options.get("output", "drydock-env")

    def render(self, root: str, config: DrydockConfig) -> None:
        """Register drydock custom templates and render a tutor env."""
        with hooks.Contexts.APP("drydock-base").enter():
            hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(pkg_resources.resource_filename("drydock", "templates"))
            hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
                [
                    (target, "drydock") for target in self.TEMPLATE_TARGETS
                ],
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
        base_dir = path_join(src, "env/drydock", f"{self.TEMPLATE_ROOT}")
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
