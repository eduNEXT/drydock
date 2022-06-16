from abc import ABC, abstractmethod


class DrydockConfig(ABC):

    @abstractmethod
    def get_data() -> dict:
        pass
