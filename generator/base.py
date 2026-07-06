from abc import ABC, abstractmethod


class BaseGenerator(ABC):

    def __init__(self, config, logger):

        self.config = config
        self.logger = logger

    @abstractmethod
    def generate(self):

        pass
