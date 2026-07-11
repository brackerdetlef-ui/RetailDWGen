#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : kostenarten.py
Version : 2.0.1

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

from generator.csv_generator import CSVGenerator
from generator.registry import register_generator


@register_generator
class KostenartenGenerator(CSVGenerator):
    """
    Generator für Kostenarten.

    Version 1.7
    """

    yaml_file = "config/kostenarten.yaml"

    output_file = "output/stammdaten/kostenarten.csv"

    header = [
        "ka_id",
        "ka_nr",
        "bezeichnung",
        "gruppe",
        "aktiv"
    ]

    depends_on = []

    # ------------------------------------------------------------------

    def build_rows(self):

        kostenarten = self.section("kostenarten")

        rows = []
        context_rows = []

        for nummer, eintrag in enumerate(
                kostenarten,
                start=1):

            row = [
                nummer,
                eintrag["nummer"],
                eintrag["bezeichnung"],
                eintrag["gruppe"],
                True
            ]

            rows.append(row)

            context_rows.append({
                "ka_id": nummer,
                "ka_nr": eintrag["nummer"],
                "bezeichnung": eintrag["bezeichnung"],
                "gruppe": eintrag["gruppe"],
                "aktiv": True
            })

        return rows, context_rows

    # ------------------------------------------------------------------

    def update_context(self, context_rows):

        if self.context is not None:
            self.context.kostenarten = context_rows
