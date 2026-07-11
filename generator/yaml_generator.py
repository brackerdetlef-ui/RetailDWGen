#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : yaml_generator.py
Version : 2.0.1

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

from abc import abstractmethod
import yaml

from generator.base import BaseGenerator


class YAMLGenerator(BaseGenerator):
    """
    Basisklasse für Generatoren, die ihre Stammdaten aus YAML beziehen.
    """

    # Vom Generator zu überschreiben
    yaml_file = None

    def initialize(self):

        super().initialize()

        if self.yaml_file is None:
            raise ValueError(
                f"{self.__class__.__name__}: yaml_file wurde nicht definiert."
            )

        with open(
            self.yaml_file,
            "r",
            encoding="utf-8"
        ) as file:

            self.data = yaml.safe_load(file)

    # ------------------------------------------------------------

    def yaml(self):
        """
        Liefert die geladenen YAML-Daten.
        """
        return self.data

    # ------------------------------------------------------------

    def section(self, name):
        """
        Liefert einen Abschnitt der YAML-Datei.
        """
        return self.data[name]
