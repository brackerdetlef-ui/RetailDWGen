import random

from faker import Faker

from generator.base import BaseGenerator
from generator.infrastructure.csv_writer import CSVWriter


class FilialenGenerator(BaseGenerator):

    def __init__(self, config, logger):

        super().__init__(config, logger)

        self.writer = CSVWriter(
            "output/stammdaten/filialen.csv"
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
            "filialen"
        )

        rows = []

        for nummer in range(
            1,
            anzahl + 1
        ):

            rows.append([

                nummer,

                f"F{nummer:04d}",

                f"Filiale {nummer}",

                self.fake.street_address(),

                self.fake.postcode(),

                self.fake.city(),

                "Deutschland",

                self.fake.phone_number(),

                round(
                    random.uniform(
                        300,
                        8000
                    ),
                    0
                ),

                self.fake.date_between(
                    start_date="-25y",
                    end_date="today"
                ),

                True

            ])

        self.writer.write(

            [

                "filiale_id",
                "filiale_code",
                "bezeichnung",
                "strasse",
                "plz",
                "ort",
                "land",
                "telefon",
                "verkaufsflaeche_qm",
                "eroeffnungsdatum",
                "aktiv"

            ],

            rows

        )

        self.logger.info(
            "%d Filialen erzeugt.",
            len(rows)
        )
