#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : kostenstellen.py
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
class KostenstellenGenerator(CSVGenerator):
    """
    Generator für Kostenstellen.

    Version 1.7
    """

    yaml_file = "config/kostenstellen.yaml"

    output_file = "output/stammdaten/kostenstellen.csv"

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
