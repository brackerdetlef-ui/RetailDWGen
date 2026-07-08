import yaml

from generator.base import BaseGenerator
from generator.infrastructure.csv_writer import CSVWriter


class SaisonkalenderGenerator(BaseGenerator):

    def __init__(self, config, logger):

        super().__init__(config, logger)

        self.writer = CSVWriter(
            "output/stammdaten/saisonkalender.csv"
        )

    def generate(self):

        with open(
            "config/saisonkalender.yaml",
            "r",
            encoding="utf-8"
        ) as file:

            daten = yaml.safe_load(file)

        saisons = daten["saisons"]

        rows = []

        for nummer, eintrag in enumerate(
                saisons,
                start=1):

            rows.append(
                [
                    nummer,
                    eintrag["code"],
                    eintrag["bezeichnung"],
                    eintrag["beginn"],
                    eintrag["ende"],
                    True
                ]
            )

        self.writer.write(
            [
                "saison_id",
                "saison_code",
                "bezeichnung",
                "beginn",
                "ende",
                "aktiv"
            ],
            rows
        )

        self.logger.info(
            "%d Saisons erzeugt.",
            len(rows)
        )
