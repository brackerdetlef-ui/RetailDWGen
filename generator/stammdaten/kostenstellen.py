#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : kostenstellen.py
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
class KostenstellenGenerator(CSVGenerator):
    """
    Generator für Kostenstellen.

    """

    yaml_file = "config/kostenstellen.yaml"

    _timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    output_file = f"output/stammdaten/kostenstellen_{_timestamp}.csv"

    header = [
        "kst_id",
        "kst_nr",
        "bezeichnung",
        "bereich",
        "aktiv"
    ]

    depends_on = []

    # ------------------------------------------------------------------

    def build_rows(self):

        kostenstellen = self.section("kostenstellen")

        rows = []
        context_rows = []

        for nummer, eintrag in enumerate(
                kostenstellen,
                start=1):

            row = [
                nummer,
                eintrag["nummer"],
                eintrag["bezeichnung"],
                eintrag["bereich"],
                True
            ]

            rows.append(row)

            context_rows.append({
                "kst_id": nummer,
                "kst_nr": eintrag["nummer"],
                "bezeichnung": eintrag["bezeichnung"],
                "bereich": eintrag["bereich"],
                "aktiv": True
            })

        return rows, context_rows

    # ------------------------------------------------------------------

    def update_context(self, context_rows):

        if self.context is not None:
            self.context.kostenstellen = context_rows
