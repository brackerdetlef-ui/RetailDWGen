import random
import yaml

from generator.base import BaseGenerator
from generator.csv_writer import CSVWriter


class HerstellerGenerator(BaseGenerator):

    def __init__(self, config, logger):

        super().__init__(config, logger)

        self.writer = CSVWriter(
            "output/stammdaten/hersteller.csv"
        )

    def generate(self):

        random.seed(
            self.config.get("general", "seed")
        )

        with open(
            "config/hersteller.yaml",
            "r",
            encoding="utf-8"
        ) as file:

            daten = yaml.safe_load(file)

        laender = [
            "DE",
            "AT",
            "CH",
            "NL",
            "FR",
            "SE",
            "US",
            "JP",
            "KR",
            "TW"
        ]

        rows = []

        for nummer, name in enumerate(
                daten["hersteller"],
                start=1):

            rows.append([
                nummer,
                f"H{nummer:04d}",
                name,
                random.choice(laender),
                True
            ])

        self.writer.write(
            [
                "hersteller_id",
                "hersteller_code",
                "name",
                "land",
                "aktiv"
            ],
            rows
        )

        self.logger.info(
            "%d Hersteller erzeugt.",
            len(rows)
        )
