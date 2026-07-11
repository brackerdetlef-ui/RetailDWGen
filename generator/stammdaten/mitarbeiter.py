#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : mitarbeiter.py
Version : 2.0.1

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

import random

from faker import Faker

from generator.base import BaseGenerator
from generator.infrastruktur.csv_writer import CSVWriter
from generator.infrastruktur.personalnummer import PersonalnummerGenerator


class MitarbeiterGenerator(BaseGenerator):

    def __init__(self, config, logger):

        super().__init__(config, logger)

        self.writer = CSVWriter(
            "output/stammdaten/mitarbeiter.csv"
        )

        self.fake = Faker("de_DE")

        self.personalnummer = PersonalnummerGenerator()

    def generate(self):

        random.seed(
            self.config.get(
                "general",
                "seed"
            )
        )

        Faker.seed(
            self.config.get(
                "general",
                "seed"
            )
        )

        anzahl = self.config.get(
            "generator",
            "mitarbeiter"
        )

        anzahl_filialen = self.config.get(
            "generator",
            "filialen"
        )

        anzahl_lager = self.config.get(
            "generator",
            "lager"
        )

        zentrale_abteilungen = [

            "Geschäftsführung",
            "Controlling",
            "Einkauf",
            "Finanzen",
            "IT",
            "Marketing",
            "Personal"

        ]

        filial_abteilungen = [

            "Verkauf",
            "Kasse",
            "Information",
            "Service",
            "Marktleitung"

        ]

        lager_abteilungen = [

            "Wareneingang",
            "Kommissionierung",
            "Versand",
            "Inventur",
            "Logistik"

        ]

        rows = []

        for nummer in range(
            1,
            anzahl + 1
        ):

            vorname = self.fake.first_name()

            nachname = self.fake.last_name()

            personalnummer = self.personalnummer.generate(
                vorname,
                nachname
            )

            email = (
                f"{vorname}.{nachname}"
                .lower()
                .replace(" ", "")
                .replace("ä", "ae")
                .replace("ö", "oe")
                .replace("ü", "ue")
                .replace("ß", "ss")
                + "@retaildwgen.local"
            )

            zufall = random.random()

            if zufall < 0.10:

                einsatzort_typ = "ZENTRALE"

                einsatzort_id = 0

                abteilung = random.choice(
                    zentrale_abteilungen
                )

            elif zufall < 0.80:

                einsatzort_typ = "FILIALE"

                einsatzort_id = random.randint(
                    1,
                    anzahl_filialen
                )

                abteilung = random.choice(
                    filial_abteilungen
                )

            else:

                einsatzort_typ = "LAGER"

                einsatzort_id = random.randint(
                    1,
                    anzahl_lager
                )

                abteilung = random.choice(
                    lager_abteilungen
                )

            rows.append([

                nummer,

                personalnummer,

                vorname,

                nachname,

                email,

                einsatzort_typ,

                einsatzort_id,

                abteilung,

                self.fake.phone_number(),

                self.fake.date_between(
                    start_date="-20y",
                    end_date="today"
                ),

                True

            ])

        self.writer.write(

            [

                "mitarbeiter_id",
                "personalnummer",
                "vorname",
                "nachname",
                "email",
                "einsatzort_typ",
                "einsatzort_id",
                "abteilung",
                "telefon",
                "eintrittsdatum",
                "aktiv"

            ],

            rows

        )

        self.logger.info(
            "%d Mitarbeiter erzeugt.",
            len(rows)
        )
