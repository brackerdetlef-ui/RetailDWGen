#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : lieferanten.py
Version : 2.0.1

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

from faker import Faker

from generator.csv_generator import CSVGenerator
from generator.registry import register_generator
from generator.utils import create_email
from generator.utils import create_website


@register_generator
class LieferantenGenerator(CSVGenerator):
    """
    Generator für Lieferanten.

    Version 1.7
    """

    output_file = "output/stammdaten/lieferanten.csv"

    header = [
        "lieferant_id",
        "lieferant_code",
        "firmenname",
        "strasse",
        "plz",
        "ort",
        "land",
        "telefon",
        "email",
        "webseite",
        "zahlungsziel",
        "aktiv"
    ]

    depends_on = []

    # YAML wird hier nicht benötigt
    yaml_file = None

    # ------------------------------------------------------------------

    def __init__(self, config, logger):

        super().__init__(config, logger)

        self.faker = Faker("de_DE")

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
            "lieferanten"
        )

        laender = [
            "DE",
            "AT",
            "CH",
            "NL",
            "FR",
            "IT",
            "PL",
            "CZ"
        ]

        zahlungsziele = [
            14,
            30,
            60
        ]

        rows = []
        context_rows = []

        for nummer in range(1, anzahl + 1):

            firma = self.faker.company()

            email = create_email(firma)
            webseite = create_website(firma)

            land = self.random.choice(laender)
            zahlungsziel = self.random.choice(zahlungsziele)

            code = f"L{nummer:06d}"

            row = [
                nummer,
                code,
                firma,
                self.faker.street_address(),
                self.faker.postcode(),
                self.faker.city(),
                land,
                self.faker.phone_number(),
                email,
                webseite,
                zahlungsziel,
                True
            ]

            rows.append(row)

            context_rows.append({
                "lieferant_id": nummer,
                "lieferant_code": code,
                "firmenname": firma,
                "strasse": row[3],
                "plz": row[4],
                "ort": row[5],
                "land": land,
                "telefon": row[7],
                "email": email,
                "webseite": webseite,
                "zahlungsziel": zahlungsziel,
                "aktiv": True
            })

        return rows, context_rows

    # ------------------------------------------------------------------

    def update_context(self, context_rows):

        if self.context is not None:
            self.context.lieferanten = context_rows
