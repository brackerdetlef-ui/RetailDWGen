#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : hersteller.py
Version : 2.1

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
class HerstellerGenerator(CSVGenerator):
    """
    Generator für Hersteller.

    Version 2.1
    """

    _timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    output_file = f"output/stammdaten/hersteller_{_timestamp}.csv"

    header = [
        "hersteller_id",
        "hersteller_code",
        "name",
        "land",
        "aktiv"
    ]

    depends_on = []

    # ------------------------------------------------------------------

    def initialize(self):

        seed = self.config.get("general", "seed")
        self.random.seed(seed)

    # ------------------------------------------------------------------

    def build_rows(self):

        with open(
            "config/hersteller.yaml",
            "r",
            encoding="utf-8"
        ) as file:

            daten = yaml.safe_load(file)

        anzahl = self.config.get(
            "generator",
            "hersteller"
        )

        laender = [
            "DE",
            "AT",
            "CH",
            "NL",
            "FR",
            "SE",
            "US",
            "JP",
            "KR",
            "TW"
        ]

        rows = []
        context_rows = []

        for nummer, name in enumerate(
                daten["hersteller"][:anzahl],
                start=1):

            code = f"H{nummer:04d}"

            land = self.random.choice(laender)

            rows.append([
                nummer,
                code,
                name,
                land,
                True
            ])

            context_rows.append({
                "hersteller_id": nummer,
                "hersteller_code": code,
                "name": name,
                "land": land,
                "aktiv": True
            })

        return rows, context_rows

    # ------------------------------------------------------------------

    def update_context(self, context_rows):

        if self.context is not None:
            self.context.hersteller = context_rows
