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

        with open(
            "config/organisation.yaml",
            "r",
            encoding="utf-8"
        ) as file:

            daten = yaml.safe_load(file)

        organisation = daten["organisation"]

        rows = []

        for nummer, eintrag in enumerate(
                organisation,
                start=1):

            rows.append([
                nummer,
                eintrag["code"],
                eintrag["kuerzel"],
                eintrag["bezeichnung"],
                eintrag["parent"] if eintrag["parent"] else "",
                eintrag["typ"],
                True
            ])

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
