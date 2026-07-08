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

        #
        # Für den DataContext
        #
        context_rows = []

        for nummer, eintrag in enumerate(
                warengruppen,
                start=1):

            row = [
                nummer,
                f"WG{nummer:03d}",
                eintrag["code"],
                eintrag["name"],
                "",
                True
            ]

            rows.append(row)

            #
            # Im DataContext speichern
            #
            context_rows.append({
                "wg_id": nummer,
                "wg_code": f"WG{nummer:03d}",
                "wg_kurzcode": eintrag["code"],
                "bezeichnung": eintrag["name"],
                "parent_id": "",
                "aktiv": True
            })

        #
        # CSV schreiben
        #
        self.writer.write(
            [
                "wg_id",
                "wg_code",
                "wg_kurzcode",
                "bezeichnung",
                "parent_id",
                "aktiv"
            ],
            rows
        )

        #
        # Context befüllen (falls vorhanden)
        #
        if hasattr(self, "context"):
            self.context.warengruppen = context_rows

        self.logger.info(
            "%d Warengruppen erzeugt.",
            len(rows)
        )
