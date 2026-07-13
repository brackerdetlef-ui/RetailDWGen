#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : marken.py
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
class MarkenGenerator(CSVGenerator):
    """
    Generator für Marken.

    """

    yaml_file = "config/marken.yaml"

    _timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    output_file = f"output/stammdaten/marken_{_timestamp}.csv"

    header = [
        "marke_id",
        "marke_code",
        "bezeichnung",
        "hersteller_id",
        "aktiv"
    ]

    depends_on = [
        "HerstellerGenerator"
    ]

    # ------------------------------------------------------------

    def build_rows(self):

        daten = self.section("marken")

        anzahl = min(
            self.config.get(
                "generator",
                "marken"
            ),
            len(daten)
        )

        #
        # Hersteller aus dem Context lesen
        #
        hersteller = {}

        if self.context is not None:

            for row in self.context.hersteller:

                hersteller[
                    row["name"]
                ] = row["hersteller_id"]

        rows = []
        context_rows = []

        for nummer, marke in enumerate(
                daten[:anzahl],
                start=1):

            hersteller_name = marke["hersteller"]

            if hersteller_name not in hersteller:

                self.logger.warning(
                    "Hersteller '%s' nicht gefunden.",
                    hersteller_name
                )

                continue

            code = f"M{nummer:04d}"

            rows.append([

                nummer,

                code,

                marke["name"],

                hersteller[
                    hersteller_name
                ],

                True

            ])

            context_rows.append({

                "marke_id": nummer,
                "marke_code": code,
                "bezeichnung": marke["name"],
                "hersteller_id": hersteller[
                    hersteller_name
                ],
                "aktiv": True

            })

        return rows, context_rows

    # ------------------------------------------------------------

    def update_context(self, context_rows):

        if self.context is not None:
            self.context.marken = context_rows
