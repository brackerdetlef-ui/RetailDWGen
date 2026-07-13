#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : kostenarten.py
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
class KostenartenGenerator(CSVGenerator):
    """
    Generator für Kostenarten.

    """

    yaml_file = "config/kostenarten.yaml"

    _timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    output_file = f"output/stammdaten/kostenarten_{_timestamp}.csv"

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
