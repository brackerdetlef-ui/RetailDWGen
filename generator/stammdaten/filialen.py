from faker import Faker

from generator.csv_generator import CSVGenerator
from generator.registry import register_generator


@register_generator
class FilialenGenerator(CSVGenerator):
    """
    Generator für Filialen.

    Version 1.7
    """

    output_file = "output/stammdaten/filialen.csv"

    yaml_file = None

    header = [
        "filiale_id",
        "filiale_code",
        "bezeichnung",
        "strasse",
        "plz",
        "ort",
        "land",
        "telefon",
        "verkaufsflaeche_qm",
        "eroeffnungsdatum",
        "aktiv"
    ]

    depends_on = []

    # ------------------------------------------------------------------

    def __init__(self, config, logger):

        super().__init__(config, logger)

        self.fake = Faker("de_DE")

    # ------------------------------------------------------------------

    def initialize(self):

        seed = self.config.get(
            "general",
            "seed"
        )

        self.random.seed(seed)
        Faker.seed(seed)

    # ------------------------------------------------------------------

    def build_rows(self):

        anzahl = self.config.get(
            "generator",
            "filialen"
        )

        rows = []
        context_rows = []

        for nummer in range(
            1,
            anzahl + 1
        ):

            code = f"F{nummer:04d}"

            verkaufsflaeche = round(
                self.random.uniform(
                    300,
                    8000
                ),
                0
            )

            eroeffnungsdatum = self.fake.date_between(
                start_date="-25y",
                end_date="today"
            )

            row = [

                nummer,

                code,

                f"Filiale {nummer}",

                self.fake.street_address(),

                self.fake.postcode(),

                self.fake.city(),

                "Deutschland",

                self.fake.phone_number(),

                verkaufsflaeche,

                eroeffnungsdatum,

                True

            ]

            rows.append(row)

            context_rows.append({

                "filiale_id": nummer,
                "filiale_code": code,
                "bezeichnung": f"Filiale {nummer}",
                "strasse": row[3],
                "plz": row[4],
                "ort": row[5],
                "land": "Deutschland",
                "telefon": row[7],
                "verkaufsflaeche_qm": verkaufsflaeche,
                "eroeffnungsdatum": eroeffnungsdatum,
                "aktiv": True

            })

        return rows, context_rows

    # ------------------------------------------------------------------

    def update_context(self, context_rows):

        if self.context is not None:
            self.context.filialen = context_rows
