#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : planogramme.py
Version : 2.0.1

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

import yaml

from generator.base import BaseGenerator
from generator.infrastruktur.csv_writer import CSVWriter


class PlanogrammeGenerator(BaseGenerator):

    def __init__(self, config, logger):

        super().__init__(config, logger)

        self.writer = CSVWriter(
            "output/stammdaten/planogramme.csv"
        )

    def generate(self):

        with open(
            "config/planogramme.yaml",
            "r",
            encoding="utf-8"
        ) as file:

            daten = yaml.safe_load(file)

        planogramme = daten["planogramme"]

        rows = []

        for nummer, eintrag in enumerate(
                planogramme,
                start=1):

            rows.append(
                [
                    nummer,
                    eintrag["code"],
                    eintrag["bezeichnung"],
                    eintrag["gaenge"],
                    eintrag["regalmeter"],
                    eintrag["regalebenen"],
                    True
                ]
            )

        self.writer.write(
            [
                "planogramm_id",
                "planogramm_code",
                "bezeichnung",
                "anzahl_gaenge",
                "regalmeter",
                "regalebenen",
                "aktiv"
            ],
            rows
        )

        self.logger.info(
            "%d Planogramme erzeugt.",
            len(rows)
        )
