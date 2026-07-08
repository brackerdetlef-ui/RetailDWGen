import random

from faker import Faker

from generator.base import BaseGenerator
from generator.infrastructure.csv_writer import CSVWriter


class MitarbeiterGenerator(BaseGenerator):

    def __init__(self, config, logger):

        super().__init__(config, logger)

        self.writer = CSVWriter(
            "output/stammdaten/mitarbeiter.csv"
        )

        self.fake = Faker("de_DE")

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

        abteilungen = [

            "Verkauf",
            "Kasse",
            "Einkauf",
            "Lager",
            "Logistik",
            "Verwaltung",
            "IT",
            "Marketing",
            "Personal"

        ]

        rows = []

        for nummer in range(
            1,
            anzahl + 1
        ):

            vorname = self.fake.first_name()
            nachname = self.fake.last_name()

            rows.append([

                nummer,

                f"M{nummer:06d}",

                vorname,

                nachname,

                f"{vorname}.{nachname}".lower().replace(" ", "") + "@retaildwgen.local",

                random.choice(
                    abteilungen
                ),

                random.randint(
                    1,
                    anzahl_filialen
                ),

                self.fake.date_between(
                    start_date="-20y",
                    end_date="today"
                ),

                self.fake.phone_number(),

                True

            ])

        self.writer.write(

            [

                "mitarbeiter_id",
                "mitarbeiter_code",
                "vorname",
                "nachname",
                "email",
                "abteilung",
                "filiale_id",
                "eintrittsdatum",
                "telefon",
                "aktiv"

            ],

            rows

        )

        self.logger.info(
            "%d Mitarbeiter erzeugt.",
            len(rows)
        )
