from abc import abstractmethod
from tutor import config as tutor_config
from drydock.manifest_builder.domain.config import DrydockConfig


class TutorConfig(DrydockConfig):

    def __init__(self, context, options: dict):
        self.context = context
        self.options = options

    def get_data(self) -> dict:
        config = tutor_config.load_full(self.context.obj.root)
        return config
