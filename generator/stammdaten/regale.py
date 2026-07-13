#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : regale.py
Version : 2.1.0

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

import json

from generator.csv_generator import CSVGenerator
from generator.registry import register_generator
from datetime import datetime


@register_generator
class RegaleGenerator(CSVGenerator):
    """
    Generator für Regale.

    """

    yaml_file = "config/regale.yaml"

    _timestamp = datetime.now().strftime(
         "%Y-%m-%d_%H-%M-%S"
    )

    output_file = f"output/stammdaten/regale_{_timestamp}.csv"

    header = [
        "regal_id",
        "regal_code",
        "bezeichnung",
        "regal_typ",
        "temperatur_zone",
        "gang",
        "seite",
        "meter_von",
        "meter_bis",
        "regalebenen",
        "eigenschaften",
        "aktiv"
    ]

    depends_on = []

    # ------------------------------------------------------------------

    def build_rows(self):

        regale = self.section("regale")

        rows = []
        context_rows = []

        for nummer, eintrag in enumerate(
                regale,
                start=1):

            eigenschaften = json.dumps(
                eintrag.get(
                    "eigenschaften",
                    {}
                ),
                ensure_ascii=False,
                separators=(",", ":")
            )

            row = [
                nummer,
                eintrag["code"],
                eintrag["bezeichnung"],
                eintrag["typ"],
                eintrag["temperatur"],
                eintrag["gang"],
                eintrag["seite"],
                eintrag["meter_von"],
                eintrag["meter_bis"],
                eintrag["regalebenen"],
                eigenschaften,
                True
            ]

            rows.append(row)

            context_rows.append({
                "regal_id": nummer,
                "regal_code": eintrag["code"],
                "bezeichnung": eintrag["bezeichnung"],
                "regal_typ": eintrag["typ"],
                "temperatur_zone": eintrag["temperatur"],
                "gang": eintrag["gang"],
                "seite": eintrag["seite"],
                "meter_von": eintrag["meter_von"],
                "meter_bis": eintrag["meter_bis"],
                "regalebenen": eintrag["regalebenen"],
                "eigenschaften": eigenschaften,
                "aktiv": True
            })

        return rows, context_rows

    # ------------------------------------------------------------------

    def update_context(self, context_rows):

        if self.context is not None:
            self.context.regale = context_rows
