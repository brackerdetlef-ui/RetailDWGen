from faker import Faker
import random

from generator.base import BaseGenerator
from generator.infrastructure.csv_writer import CSVWriter
from generator.utils import create_email
from generator.utils import create_website


class LieferantenGenerator(BaseGenerator):

    def __init__(self, config, logger):

        super().__init__(config, logger)

        self.writer = CSVWriter(
            "output/stammdaten/lieferanten.csv"
        )

        self.faker = Faker("de_DE")

    def generate(self):

        random.seed(
            self.config.get("general", "seed")
        )

        Faker.seed(
            self.config.get("general", "seed")
        )

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

        zahlungsziele = [14, 30, 60]

        rows = []

        for nummer in range(1, anzahl + 1):

            firma = self.faker.company()

            email = create_email(firma)

            webseite = create_website(firma)

            rows.append([

                nummer,

                f"L{nummer:06d}",

                firma,

                self.faker.street_address(),

                self.faker.postcode(),

                self.faker.city(),

                random.choice(laender),

                self.faker.phone_number(),

                email,

                webseite,

                random.choice(zahlungsziele),

                True

            ])

        self.writer.write(

            [

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

            ],

            rows

        )

        self.logger.info(
            "%d Lieferanten erzeugt.",
            anzahl
        )
