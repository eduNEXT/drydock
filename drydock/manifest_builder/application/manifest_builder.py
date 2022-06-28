
from drydock.manifest_builder.domain.config import DrydockConfig
from drydock.manifest_builder.domain.manifest_repository import ManifestRepository


class ManifestBuilder:

    def __init__(self, repository: ManifestRepository, options: dict):
        self.repository = repository
        self.options = options

    def __call__(self, config: DrydockConfig):
        self.repository.save(config=config)
