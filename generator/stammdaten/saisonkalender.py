#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : saisonkalender.py
Version : 2.1.0

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

from generator.csv_generator import CSVGenerator
from generator.registry import register_generator
from datetime import datetime


@register_generator
class SaisonkalenderGenerator(CSVGenerator):
    """
    Generator für Saisonkalender.

    """


    yaml_file = "config/saisonkalender.yaml"

    _timestamp = datetime.now().strftime(
         "%Y-%m-%d_%H-%M-%S"
    )

    output_file = f"output/stammdaten/saisonkalender_{_timestamp}.csv"

    header = [
        "saison_id",
        "saison_code",
        "bezeichnung",
        "beginn",
        "ende",
        "aktiv"
    ]

    depends_on = []

    # ------------------------------------------------------------------

    def build_rows(self):

        saisons = self.section("saisons")

        rows = []
        context_rows = []

        for nummer, eintrag in enumerate(
                saisons,
                start=1):

            row = [
                nummer,
                eintrag["code"],
                eintrag["bezeichnung"],
                eintrag["beginn"],
                eintrag["ende"],
                True
            ]

            rows.append(row)

            context_rows.append({
                "saison_id": nummer,
                "saison_code": eintrag["code"],
                "bezeichnung": eintrag["bezeichnung"],
                "beginn": eintrag["beginn"],
                "ende": eintrag["ende"],
                "aktiv": True
            })

        return rows, context_rows

    # ------------------------------------------------------------------

    def update_context(self, context_rows):

        if self.context is not None:
            self.context.saisonkalender = context_rows
