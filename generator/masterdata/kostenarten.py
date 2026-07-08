import yaml

from generator.base import BaseGenerator
from generator.infrastructure.csv_writer import CSVWriter


class KostenartenGenerator(BaseGenerator):

    def __init__(self, config, logger):

        super().__init__(config, logger)

        self.writer = CSVWriter(
            "output/stammdaten/kostenarten.csv"
        )

    def generate(self):

        with open(
            "config/kostenarten.yaml",
            "r",
            encoding="utf-8"
        ) as file:

            daten = yaml.safe_load(file)

        kostenarten = daten["kostenarten"]

        rows = []

        for nummer, eintrag in enumerate(
                kostenarten,
                start=1):

            rows.append(
                [
                    nummer,
                    eintrag["nummer"],
                    eintrag["bezeichnung"],
                    eintrag["gruppe"],
                    True
                ]
            )

        self.writer.write(
            [
                "ka_id",
                "ka_nr",
                "bezeichnung",
                "gruppe",
                "aktiv"
            ],
            rows
        )

        self.logger.info(
            "%d Kostenarten erzeugt.",
            len(rows)
        )
