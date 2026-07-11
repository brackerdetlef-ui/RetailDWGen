#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : kunden.py
Version : 2.0.1

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

from datetime import date, timedelta

from faker import Faker

from generator.base import BaseGenerator
from generator.csv_generator import CSVGenerator
from generator.registry import register_generator
from generator.utils import slugify


@register_generator
class KundenGenerator(CSVGenerator):
    """
    Generator für Kunden.

    Version 1.7
    """

    output_file = "output/stammdaten/kunden.csv"

    yaml_file = None

    header = [
        "kunde_id",
        "kunden_nr",
        "anrede",
        "vorname",
        "nachname",
        "firma",
        "strasse",
        "plz",
        "ort",
        "land",
        "telefon",
        "mobil",
        "email",
        "geburtsdatum",
        "kunde_seit",
        "kundengruppe",
        "bonuspunkte",
        "aktiv"
    ]

    depends_on = []

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
            "kunden"
        )

        laender = [
            "DE",
            "AT",
            "CH",
            "NL",
            "FR"
        ]

        heute = date.today()

        rows = []
        context_rows = []

        for nummer in range(1, anzahl + 1):

            geschlecht = self.random.choice(["m", "w"])

            if geschlecht == "m":

                anrede = "Herr"
                vorname = self.faker.first_name_male()

            else:

                anrede = "Frau"
                vorname = self.faker.first_name_female()

            nachname = self.faker.last_name()

            if self.random.random() < 0.10:

                firma = self.faker.company()
                kundengruppe = "GESCHAEFT"

            else:

                firma = ""
                kundengruppe = "PRIVAT"

            email = (
                slugify(
                    vorname + "." + nachname
                )
                + "@example.com"
            )

            alter = self.random.randint(
                18,
                85
            )

            geburtsdatum = heute - timedelta(
                days=alter * 365
            )

            kunde_seit = heute - timedelta(
                days=self.random.randint(
                    0,
                    3650
                )
            )

            land = self.random.choice(laender)
            bonuspunkte = self.random.randint(
                0,
                10000
            )

            row = [

                nummer,

                f"K{nummer:07d}",

                anrede,

                vorname,

                nachname,

                firma,

                self.faker.street_address(),

                self.faker.postcode(),

                self.faker.city(),

                land,

                self.faker.phone_number(),

                self.faker.phone_number(),

                email,

                geburtsdatum.isoformat(),

                kunde_seit.isoformat(),

                kundengruppe,

                bonuspunkte,

                True

            ]

            rows.append(row)

            context_rows.append({

                "kunde_id": nummer,
                "kunden_nr": row[1],
                "anrede": anrede,
                "vorname": vorname,
                "nachname": nachname,
                "firma": firma,
                "strasse": row[6],
                "plz": row[7],
                "ort": row[8],
                "land": land,
                "telefon": row[10],
                "mobil": row[11],
                "email": email,
                "geburtsdatum": geburtsdatum.isoformat(),
                "kunde_seit": kunde_seit.isoformat(),
                "kundengruppe": kundengruppe,
                "bonuspunkte": bonuspunkte,
                "aktiv": True

            })

        return rows, context_rows

    # ------------------------------------------------------------------

    def update_context(self, context_rows):

        if self.context is not None:
            self.context.kunden = context_rows
