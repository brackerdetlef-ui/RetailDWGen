import yaml

from generator.base import BaseGenerator
from generator.infrastructure.csv_writer import CSVWriter


class OrganisationGenerator(BaseGenerator):

    def __init__(self, config, logger):

        super().__init__(config, logger)

        self.writer = CSVWriter(
            "output/stammdaten/organisation.csv"
        )

    def generate(self):

        # ----------------------------------------------------
        # Organisation laden
        # ----------------------------------------------------

        with open(
            "config/organisation.yaml",
            "r",
            encoding="utf-8"
        ) as file:

            daten = yaml.safe_load(file)

        organisation = daten["organisation"]

        rows = []

        nummer = 1

        # ----------------------------------------------------
        # Feste Organisationseinheiten
        # ----------------------------------------------------

        for eintrag in organisation:

            rows.append(
                [
                    nummer,
                    eintrag["code"],
                    eintrag["kuerzel"],
                    eintrag["bezeichnung"],
                    eintrag["parent"] or "",
                    eintrag["typ"],
                    True
                ]
            )

            nummer += 1

        # ----------------------------------------------------
        # Warengruppen laden
        # ----------------------------------------------------

        with open(
            "config/warengruppen.yaml",
            "r",
            encoding="utf-8"
        ) as file:

            daten = yaml.safe_load(file)

        warengruppen = daten["warengruppen"]

        # ----------------------------------------------------
        # Verkaufsgruppen erzeugen
        # ----------------------------------------------------

        org_code = 510

        for wg in warengruppen:

            kuerzel = "VG" + wg["code"]

            rows.append(
                [
                    nummer,
                    f"{org_code}",
                    kuerzel,
                    f"Verkaufsgruppe {wg['name']}",
                    "010",
                    "verkaufsgruppe",
                    True
                ]
            )

            nummer += 1
            org_code += 1

        # ----------------------------------------------------
        # Einkaufsgruppen erzeugen
        # ----------------------------------------------------

        org_code = 610

        for wg in warengruppen:

            kuerzel = "EG" + wg["code"]

            rows.append(
                [
                   nummer,
                   f"{org_code}",
                   kuerzel,
                   f"Einkaufsgruppe {wg['name']}",
                   "020",
                   "einkaufsgruppe",
                   True
                ]
            )

            nummer += 1
            org_code += 1

        # ----------------------------------------------------
        # CSV schreiben
        # ----------------------------------------------------

        self.writer.write(
            [
                "org_id",
                "org_code",
                "org_kuerzel",
                "bezeichnung",
                "parent_code",
                "typ",
                "aktiv"
            ],
            rows
        )

        self.logger.info(
            "%d Organisationseinheiten erzeugt.",
            len(rows)
        )
