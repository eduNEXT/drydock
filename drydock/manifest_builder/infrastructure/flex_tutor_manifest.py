import os

from abc import abstractmethod
from drydock.manifest_builder.domain.config import DrydockConfig
from drydock.manifest_builder.domain.manifest_repository import ManifestRepository

from tutor import env as tutor_env
from tutor import hooks


class FlexibleTutorManifest(ManifestRepository):

    def save(config: DrydockConfig) -> None:

        # import pudb; pu.db
        env = config.get_data()

        # Render the manifest by reusing the code that tutor uses for the env
        fixed_root = "test-manifest"
        # tutor_env.save(context.obj.root, config)

        def my_base_dir(root):
            """Return the environment base directory."""
            return os.path.join(fixed_root, "")

        tutor_env.base_dir = my_base_dir
        tutor_env.save(None, env)


        hooks.filters.clear("env:templates:targets")
        name = "drydock"
        hooks.filters.add_items(
            "env:templates:targets",
            [
                (
                    os.path.join(name, "manifest_001"),
                    "",
                ),
            ],
        )
        tutor_env.save(None, env)
