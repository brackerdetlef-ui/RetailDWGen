import yaml

from generator.base import BaseGenerator
from generator.infrastructure.csv_writer import CSVWriter


class KostenstellenGenerator(BaseGenerator):

    def __init__(self, config, logger):

        super().__init__(config, logger)

        self.writer = CSVWriter(
            "output/stammdaten/kostenstellen.csv"
        )

    def generate(self):

        with open(
            "config/kostenstellen.yaml",
            "r",
            encoding="utf-8"
        ) as file:

            daten = yaml.safe_load(file)

        kostenstellen = daten["kostenstellen"]

        rows = []

        for nummer, eintrag in enumerate(
                kostenstellen,
                start=1):

            rows.append(
                [
                    nummer,
                    eintrag["nummer"],
                    eintrag["bezeichnung"],
                    eintrag["bereich"],
                    True
                ]
            )

        self.writer.write(
            [
                "kst_id",
                "kst_nr",
                "bezeichnung",
                "bereich",
                "aktiv"
            ],
            rows
        )

        self.logger.info(
            "%d Kostenstellen erzeugt.",
            len(rows)
        )
