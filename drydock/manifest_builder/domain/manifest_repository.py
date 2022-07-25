from abc import ABC, abstractmethod
from drydock.manifest_builder.domain.config import DrydockConfig


class ManifestRepository(ABC):

    @abstractmethod
    def save(self, config: DrydockConfig) -> None:
        pass
