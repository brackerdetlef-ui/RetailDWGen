import yaml
from generator.base import BaseGenerator
from generator.infrastructure.csv_writer import CSVWriter


class WarengruppenGenerator(BaseGenerator):

    def __init__(self, config, logger):

        super().__init__(config, logger)

        self.writer = CSVWriter(
            "output/stammdaten/warengruppen.csv"
        )

    def generate(self):

        with open(
            "config/warengruppen.yaml",
            "r",
            encoding="utf-8"
        ) as file:

             daten = yaml.safe_load(file)

        warengruppen = daten["warengruppen"]

        rows = []

        for nummer, name in enumerate(warengruppen, start=1):

            rows.append(
                [
                    nummer,
                    f"WG{nummer:03d}",
                    name,
                    "",
                    True
                ]
            )

        self.writer.write(
            [
                "wg_id",
                "wg_code",
                "bezeichnung",
                "parent_id",
                "aktiv"
            ],
            rows
        )

        self.logger.info(
            "%d Warengruppen erzeugt.",
            len(rows)
        )
