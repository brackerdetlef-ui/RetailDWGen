#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : csv_generator.py
Version : 2.0.1

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

from abc import abstractmethod

from generator.infrastruktur.csv_writer import CSVWriter
from generator.yaml_generator import YAMLGenerator


class CSVGenerator(YAMLGenerator):
    """
    Basisklasse aller CSV-basierten Generatoren.
    """

    output_file = None
    header = []

    def __init__(self, config, logger):

        super().__init__(config, logger)

        if self.output_file is None:
            raise ValueError(
                f"{self.__class__.__name__}: output_file wurde nicht definiert."
            )

        self.writer = CSVWriter(self.output_file)

    # ------------------------------------------------------------

    @abstractmethod
    def build_rows(self):
        pass

    # ------------------------------------------------------------

    def update_context(self, context_rows):
        pass

    # ------------------------------------------------------------

    def generate(self):

        rows, context_rows = self.build_rows()

        self.writer.write(
            self.header,
            rows
        )

        self.records_created = len(rows)

        if self.context is not None:
            self.update_context(context_rows)

        self.log(
            f"{self.records_created} Datensätze geschrieben."
        )
