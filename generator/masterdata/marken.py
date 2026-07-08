import csv
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

        with open(
            "config/marken.yaml",
            "r",
            encoding="utf-8"
        ) as file:

            daten = yaml.safe_load(file)

        hersteller = {}

        with open(
            "output/stammdaten/hersteller.csv",
            "r",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(
                file,
                delimiter=self.config.get(
                    "general",
                    "delimiter"
                )
            )

            for row in reader:

                hersteller[
                    row["name"]
                ] = int(
                    row["hersteller_id"]
                )

        anzahl = min(
            self.config.get(
                "generator",
                "marken"
            ),
            len(daten["marken"])
        )

        rows = []

        for nummer, marke in enumerate(
            daten["marken"][:anzahl],
            start=1
        ):

            hersteller_name = marke["hersteller"]

            if hersteller_name not in hersteller:

                self.logger.warning(
                    "Hersteller '%s' nicht gefunden.",
                    hersteller_name
                )

                continue

            rows.append([

                nummer,

                f"M{nummer:04d}",

                marke["name"],

                hersteller[
                    hersteller_name
                ],

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
