import random

from faker import Faker

from generator.base import BaseGenerator
from generator.infrastructure.csv_writer import CSVWriter


class LagerGenerator(BaseGenerator):

    def __init__(self, config, logger):

        super().__init__(config, logger)

        self.writer = CSVWriter(
            "output/stammdaten/lager.csv"
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
            "lager"
        )

        anzahl_filialen = self.config.get(
            "generator",
            "filialen"
        )

        lagerarten = [

            "Hauptlager",
            "Regionallager",
            "Filiallager",
            "Außenlager"

        ]

        rows = []

        for nummer in range(
            1,
            anzahl + 1
        ):

            rows.append([

                nummer,

                f"L{nummer:04d}",

                f"Lager {nummer}",

                random.choice(
                    lagerarten
                ),

                random.randint(
                    1,
                    anzahl_filialen
                ),

                self.fake.street_address(),

                self.fake.postcode(),

                self.fake.city(),

                random.randint(
                    500,
                    50000
                ),

                True

            ])

        self.writer.write(

            [

                "lager_id",
                "lager_code",
                "bezeichnung",
                "lagerart",
                "filiale_id",
                "strasse",
                "plz",
                "ort",
                "kapazitaet",
                "aktiv"

            ],

            rows

        )

        self.logger.info(
            "%d Lager erzeugt.",
            len(rows)
        )
