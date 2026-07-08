import random

from faker import Faker

from generator.base import BaseGenerator
from generator.infrastructure.csv_writer import CSVWriter


class ArtikelGenerator(BaseGenerator):

    def __init__(self, config, logger):

        super().__init__(config, logger)

        self.writer = CSVWriter(
            "output/stammdaten/artikel.csv"
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
            "artikel"
        )

        anzahl_warengruppen = self.config.get(
            "generator",
            "warengruppen"
        )

        anzahl_hersteller = self.config.get(
            "generator",
            "hersteller"
        )

        anzahl_marken = self.config.get(
            "generator",
            "marken"
        )

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

        for nummer in range(1, anzahl + 1):

            einkauf = round(
                random.uniform(5.00, 500.00),
                2
            )

            uvp = round(
                einkauf * random.uniform(1.20, 2.20),
                2
            )

            verkauf = round(
                random.uniform(einkauf, uvp),
                2
            )

            bezeichnung = (
                f"{random.choice(adjektive)} "
                f"{random.choice(produkte)} "
                f"{random.choice(varianten)}"
            ).strip()

            rows.append([

                nummer,

                f"A{nummer:08d}",

                self.fake.ean13(),

                bezeichnung,

                random.randint(
                    1,
                    anzahl_hersteller
                ),

                random.randint(
                    1,
                    anzahl_marken
                ),

                random.randint(
                    1,
                    anzahl_warengruppen
                ),

                uvp,

                einkauf,

                verkauf,

                True

            ])

        self.writer.write(

            [

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

            ],

            rows

        )

        self.logger.info(
            "%d Artikel erzeugt.",
            len(rows)
        )
