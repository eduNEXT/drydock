import os
import pkg_resources

from abc import abstractmethod
from drydock.manifest_builder.domain.config import DrydockConfig
from drydock.manifest_builder.domain.manifest_repository import ManifestRepository

from tutor import env as tutor_env
from tutor import hooks


class FlexibleTutorManifest(ManifestRepository):

    def save(self, config: DrydockConfig) -> None:

        env = config.get_data()

        # Render the manifest by reusing the code that tutor uses for the env
        fixed_root = "test-manifest"

        def my_base_dir(root):
            """Return the environment base directory."""
            return os.path.join(fixed_root, "")

        tutor_env.base_dir = my_base_dir
        tutor_env.save(None, env)


        hooks.filters.clear("env:templates:targets")
        hooks.filters.add_items(
            "env:templates:targets",
            [
                (
                    os.path.join("manifest_builder", "manifest_001"),
                    "",
                ),
            ],
        )

        hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(
            pkg_resources.resource_filename("drydock", "templates")
        )

        tutor_env.save(None, env)
