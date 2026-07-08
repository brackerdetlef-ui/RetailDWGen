import random
import yaml

from generator.base import BaseGenerator
from generator.infrastructure.csv_writer import CSVWriter


class MarkenGenerator(BaseGenerator):

    def __init__(self, config, logger):

        super().__init__(config, logger)

        self.writer = CSVWriter(
            "output/stammdaten/marken.csv"
        )

    def generate(self):

        random.seed(
            self.config.get(
                "general",
                "seed"
            )
        )

        with open(
            "config/marken.yaml",
            "r",
            encoding="utf-8"
        ) as file:

            daten = yaml.safe_load(file)

        marken = daten["marken"]

        anzahl = min(
            self.config.get(
                "generator",
                "marken"
            ),
            len(marken)
        )

        anzahl_hersteller = self.config.get(
            "generator",
            "hersteller"
        )

        rows = []

        for nummer, name in enumerate(
            marken[:anzahl],
            start=1
        ):

            rows.append([
                nummer,
                f"M{nummer:04d}",
                name,
                random.randint(
                    1,
                    anzahl_hersteller
                ),
                True
            ])

        self.writer.write(
            [
                "marke_id",
                "marke_code",
                "bezeichnung",
                "hersteller_id",
                "aktiv"
            ],
            rows
        )

        self.logger.info(
            "%d Marken erzeugt.",
            len(rows)
        )
