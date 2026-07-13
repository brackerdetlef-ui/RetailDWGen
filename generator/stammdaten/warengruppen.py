#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : warengruppen.py
Version : 2.1.0

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

import yaml

from generator.csv_generator import CSVGenerator
from generator.registry import register_generator
from datetime import datetime


@register_generator
class WarengruppenGenerator(CSVGenerator):
    """
    Generator für Warengruppen.

    """

    _timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    output_file = f"output/stammdaten/warengruppen_{_timestamp}.csv"

    yaml_file = "config/warengruppen.yaml"

    header = [
        "wg_id",
        "wg_code",
        "wg_kurzcode",
        "bezeichnung",
        "parent_id",
        "aktiv"
    ]

    depends_on = []

    # ------------------------------------------------------------------

    def build_rows(self):

        warengruppen = self.section("warengruppen")

        rows = []
        context_rows = []

        for nummer, eintrag in enumerate(
                warengruppen,
                start=1):

            code = f"WG{nummer:03d}"

            rows.append([
                nummer,
                code,
                eintrag["code"],
                eintrag["name"],
                "",
                True
            ])

            context_rows.append({
                "wg_id": nummer,
                "wg_code": code,
                "wg_kurzcode": eintrag["code"],
                "bezeichnung": eintrag["name"],
                "parent_id": "",
                "aktiv": True
            })

        return rows, context_rows

    # ------------------------------------------------------------------

    def update_context(self, context_rows):

        if self.context is not None:
            self.context.warengruppen = context_rows
