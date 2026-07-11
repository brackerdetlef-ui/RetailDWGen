#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : base.py
Version : 2.0.1

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

from abc import ABC, abstractmethod

import random
from pathlib import Path


class BaseGenerator(ABC):
    """
    Gemeinsame Basisklasse aller Generatoren.

    Version 1.7
    """

    depends_on = []

    def __init__(self, config, logger):

        self.config = config
        self.logger = logger

        # Wird vom GeneratorManager gesetzt
        self.context = None

        # Eigener Zufallsgenerator
        self.random = random.Random()

        # Statistik
        self.records_created = 0

    # ---------------------------------------------------------

    @property
    def name(self):

        return self.__class__.__name__

    # ---------------------------------------------------------

    def log(self, message):

        self.logger.info("[%s] %s", self.name, message)

    # ---------------------------------------------------------

    @property
    def output_directory(self):

        if hasattr(self.config, "output_directory"):
            return Path(self.config.output_directory)

        return Path("output")

    # ---------------------------------------------------------

    def run(self):

        self.log("Starte")

        self.initialize()
        self.load_reference_data()
        self.before_generate()

        self.generate()

        self.validate()
        self.after_generate()

        self.log(
            f"{self.records_created} Datensätze erzeugt."
        )

    # ---------------------------------------------------------

    def initialize(self):
        pass

    # ---------------------------------------------------------

    def load_reference_data(self):
        pass

    # ---------------------------------------------------------

    def before_generate(self):
        pass

    # ---------------------------------------------------------

    @abstractmethod
    def generate(self):
        pass

    # ---------------------------------------------------------

    def validate(self):
        return True

    # ---------------------------------------------------------

    def after_generate(self):
        pass

    # ---------------------------------------------------------

    def record_created(self, amount=1):

        self.records_created += amount
