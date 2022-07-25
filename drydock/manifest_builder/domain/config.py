from abc import ABC, abstractmethod


class DrydockConfig(ABC):

    @abstractmethod
    def get_data(self) -> dict:
        pass

    @abstractmethod
    def get_root(self) -> str:
        pass
