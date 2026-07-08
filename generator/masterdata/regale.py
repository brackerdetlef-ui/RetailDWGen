import json
import yaml

from generator.base import BaseGenerator
from generator.infrastructure.csv_writer import CSVWriter


class RegaleGenerator(BaseGenerator):

    def __init__(self, config, logger):

        super().__init__(config, logger)

        self.writer = CSVWriter(
            "output/stammdaten/regale.csv"
        )

    def generate(self):

        with open(
            "config/regale.yaml",
            "r",
            encoding="utf-8"
        ) as file:

            daten = yaml.safe_load(file)

        regale = daten["regale"]

        rows = []

        for nummer, eintrag in enumerate(
                regale,
                start=1):

            rows.append(
                [
                    nummer,
                    eintrag["code"],
                    eintrag["bezeichnung"],
                    eintrag["typ"],
                    eintrag["temperatur"],
                    eintrag["gang"],
                    eintrag["seite"],
                    eintrag["meter_von"],
                    eintrag["meter_bis"],
                    eintrag["regalebenen"],
                    json.dumps(
                        eintrag.get(
                            "eigenschaften",
                            {}
                        ),
                        ensure_ascii=False,
                        separators=(",", ":")
                    ),
                    True
                ]
            )

        self.writer.write(
            [
                "regal_id",
                "regal_code",
                "bezeichnung",
                "regal_typ",
                "temperatur_zone",
                "gang",
                "seite",
                "meter_von",
                "meter_bis",
                "regalebenen",
                "eigenschaften",
                "aktiv"
            ],
            rows
        )

        self.logger.info(
            "%d Regale erzeugt.",
            len(rows)
        )
