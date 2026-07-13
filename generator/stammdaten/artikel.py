#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : artikel.py
Version : 2.1.0

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

from faker import Faker

from generator.csv_generator import CSVGenerator
from generator.registry import register_generator
from datetime import datetime


@register_generator
class ArtikelGenerator(CSVGenerator):
    """
    Generator für Artikel.

    Version 2.1
    """

    _timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    output_file = (
        f"output/stammdaten/artikel_{_timestamp}.csv"
    )

    yaml_file = None

    header = [
        "artikel_id",
        "artikel_code",
        "ean",
        "bezeichnung",
        "hersteller_id",
        "marke_id",
        "warengruppe_id",
        "uvp",
        "einkaufspreis",
        "verkaufspreis",
        "aktiv"
    ]

    depends_on = [
        "WarengruppenGenerator",
        "HerstellerGenerator",
        "MarkenGenerator"
    ]

    # ------------------------------------------------------------------

    def __init__(self, config, logger):

        super().__init__(config, logger)

        self.fake = Faker("de_DE")

    # ------------------------------------------------------------------

    def initialize(self):

        seed = self.config.get(
            "general",
            "seed"
        )

        self.random.seed(seed)
        Faker.seed(seed)

    # ------------------------------------------------------------------

    def build_rows(self):

        anzahl = self.config.get(
            "generator",
            "artikel"
        )

        hersteller = self.context.hersteller
        marken = self.context.marken
        warengruppen = self.context.warengruppen

        adjektive = [
            "Premium",
            "Classic",
            "Comfort",
            "Eco",
            "Smart",
            "Professional",
            "Ultra"
        ]

        produkte = [
            "Kaffeemaschine",
            "Notebook",
            "Fernseher",
            "Staubsauger",
            "Bohrmaschine",
            "Monitor",
            "Maus",
            "Tastatur",
            "Drucker",
            "Wasserkocher",
            "Mixer",
            "Rucksack",
            "Kopfhörer",
            "Smartphone",
            "Tablet"
        ]

        varianten = [
            "",
            "XL",
            "Mini",
            "Plus",
            "Pro",
            "Max"
        ]

        rows = []
        context_rows = []

        for nummer in range(1, anzahl + 1):

            einkauf = round(
                self.random.uniform(5.00, 500.00),
                2
            )

            uvp = round(
                einkauf * self.random.uniform(1.20, 2.20),
                2
            )

            verkauf = round(
                self.random.uniform(einkauf, uvp),
                2
            )

            bezeichnung = (
                f"{self.random.choice(adjektive)} "
                f"{self.random.choice(produkte)} "
                f"{self.random.choice(varianten)}"
            ).strip()

            hersteller_id = self.random.choice(
                hersteller
            )["hersteller_id"]

            marke_id = self.random.choice(
                marken
            )["marke_id"]

            warengruppe_id = self.random.choice(
                warengruppen
            )["wg_id"]

            row = [

                nummer,

                f"A{nummer:08d}",

                self.fake.ean13(),

                bezeichnung,

                hersteller_id,

                marke_id,

                warengruppe_id,

                uvp,

                einkauf,

                verkauf,

                True

            ]

            rows.append(row)

            context_rows.append({

                "artikel_id": nummer,
                "artikel_code": row[1],
                "ean": row[2],
                "bezeichnung": bezeichnung,
                "hersteller_id": hersteller_id,
                "marke_id": marke_id,
                "warengruppe_id": warengruppe_id,
                "uvp": uvp,
                "einkaufspreis": einkauf,
                "verkaufspreis": verkauf,
                "aktiv": True

            })

        return rows, context_rows

    # ------------------------------------------------------------------

    def update_context(self, context_rows):

        if self.context is not None:
            self.context.artikel = context_rows
