from datetime import date, timedelta
import random

from faker import Faker

from generator.base import BaseGenerator
from generator.infrastructure.csv_writer import CSVWriter
from generator.utils import slugify


class KundenGenerator(BaseGenerator):

    def __init__(self, config, logger):

        super().__init__(config, logger)

        self.writer = CSVWriter(
            "output/stammdaten/kunden.csv"
        )

        self.faker = Faker("de_DE")

    def generate(self):

        seed = self.config.get(
            "general",
            "seed"
        )

        random.seed(seed)
        Faker.seed(seed)

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

        rows = []

        heute = date.today()

        for nummer in range(1, anzahl + 1):

            geschlecht = random.choice(
                ["m", "w"]
            )

            if geschlecht == "m":

                anrede = "Herr"

                vorname = self.faker.first_name_male()

            else:

                anrede = "Frau"

                vorname = self.faker.first_name_female()

            nachname = self.faker.last_name()

            if random.random() < 0.10:

                firma = self.faker.company()

                kundengruppe = "GESCHAEFT"

            else:

                firma = ""

                kundengruppe = "PRIVAT"

            email = (
                slugify(
                    vorname
                    + "."
                    + nachname
                )
                + "@example.com"
            )

            alter = random.randint(
                18,
                85
            )

            geburtsdatum = heute - timedelta(
                days=alter * 365
            )

            kunde_seit = heute - timedelta(
                days=random.randint(
                    0,
                    3650
                )
            )

            rows.append([

                nummer,

                f"K{nummer:07d}",

                anrede,

                vorname,

                nachname,

                firma,

                self.faker.street_address(),

                self.faker.postcode(),

                self.faker.city(),

                random.choice(laender),

                self.faker.phone_number(),

                self.faker.phone_number(),

                email,

                geburtsdatum.isoformat(),

                kunde_seit.isoformat(),

                kundengruppe,

                random.randint(0, 10000),

                True

            ])

        self.writer.write(

            header,

            rows

        )

        self.logger.info(

            "%d Kunden erzeugt.",

            anzahl

        )  
