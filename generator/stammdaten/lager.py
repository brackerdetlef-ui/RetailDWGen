from faker import Faker

from generator.csv_generator import CSVGenerator
from generator.registry import register_generator


@register_generator
class LagerGenerator(CSVGenerator):
    """
    Generator für Lager.

    Version 1.7
    """

    output_file = "output/stammdaten/lager.csv"

    yaml_file = None

    header = [
        "lager_id",
        "lager_code",
        "bezeichnung",
        "lagerart",
        "filiale_id",
        "strasse",
        "plz",
        "ort",
        "kapazitaet",
        "aktiv"
    ]

    depends_on = [
        "FilialenGenerator"
    ]

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
            "lager"
        )

        lagerarten = [
            "Hauptlager",
            "Regionallager",
            "Filiallager",
            "Außenlager"
        ]

        filialen = self.context.filialen
        anzahl_filialen = len(filialen)

        rows = []
        context_rows = []

        for nummer in range(
            1,
            anzahl + 1
        ):

            code = f"L{nummer:04d}"

            lagerart = self.random.choice(
                lagerarten
            )

            filiale_id = self.random.randint(
                1,
                anzahl_filialen
            )

            kapazitaet = self.random.randint(
                500,
                50000
            )

            row = [

                nummer,

                code,

                f"Lager {nummer}",

                lagerart,

                filiale_id,

                self.fake.street_address(),

                self.fake.postcode(),

                self.fake.city(),

                kapazitaet,

                True

            ]

            rows.append(row)

            context_rows.append({

                "lager_id": nummer,
                "lager_code": code,
                "bezeichnung": f"Lager {nummer}",
                "lagerart": lagerart,
                "filiale_id": filiale_id,
                "strasse": row[5],
                "plz": row[6],
                "ort": row[7],
                "kapazitaet": kapazitaet,
                "aktiv": True

            })

        return rows, context_rows

    # ------------------------------------------------------------------

    def update_context(self, context_rows):

        if self.context is not None:
            self.context.lager = context_rows
