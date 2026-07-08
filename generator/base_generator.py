"""
RetailDWGen

Basisklasse aller Generatoren.
"""

from __future__ import annotations

import random
from pathlib import Path


class BaseGenerator:

    name = "BaseGenerator"

    depends_on = []

    def __init__(
        self,
        config,
        logger,
        context,
    ):

        self.config = config
        self.logger = logger
        self.context = context

        self.random = random.Random()

    @property
    def output_path(self) -> Path:
        return Path(self.config.output_directory)

    def log(self, message: str):

        if self.logger:
            self.logger.info(f"[{self.name}] {message}")

    def generate(self):

        raise NotImplementedError()

    def validate(self):

        return True
