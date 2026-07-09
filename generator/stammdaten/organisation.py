import yaml

from generator.csv_generator import CSVGenerator
from generator.registry import register_generator


@register_generator
class OrganisationGenerator(CSVGenerator):
    """
    Generator für Organisationseinheiten.

    Version 1.7
    """

    yaml_file = "config/organisation.yaml"

    output_file = "output/stammdaten/organisation.csv"

    header = [
        "org_id",
        "org_code",
        "org_kuerzel",
        "bezeichnung",
        "parent_code",
        "typ",
        "aktiv"
    ]

    depends_on = [
        "WarengruppenGenerator"
    ]

    # ------------------------------------------------------------------

    def build_rows(self):

        organisation = self.section("organisation")

        rows = []
        context_rows = []

        nummer = 1

        # ----------------------------------------------------
        # Feste Organisationseinheiten
        # ----------------------------------------------------

        for eintrag in organisation:

            row = [
                nummer,
                eintrag["code"],
                eintrag["kuerzel"],
                eintrag["bezeichnung"],
                eintrag["parent"] or "",
                eintrag["typ"],
                True
            ]

            rows.append(row)

            context_rows.append({
                "org_id": nummer,
                "org_code": eintrag["code"],
                "org_kuerzel": eintrag["kuerzel"],
                "bezeichnung": eintrag["bezeichnung"],
                "parent_code": eintrag["parent"] or "",
                "typ": eintrag["typ"],
                "aktiv": True
            })

            nummer += 1

        # ----------------------------------------------------
        # Warengruppen aus dem Context
        # ----------------------------------------------------

        warengruppen = self.context.warengruppen

        # ----------------------------------------------------
        # Verkaufsgruppen
        # ----------------------------------------------------

        org_code = 510

        for wg in warengruppen:

            row = [
                nummer,
                str(org_code),
                "VG" + wg["wg_kurzcode"],
                f"Verkaufsgruppe {wg['bezeichnung']}",
                "010",
                "verkaufsgruppe",
                True
            ]

            rows.append(row)

            context_rows.append({
                "org_id": nummer,
                "org_code": str(org_code),
                "org_kuerzel": "VG" + wg["wg_kurzcode"],
                "bezeichnung": f"Verkaufsgruppe {wg['bezeichnung']}",
                "parent_code": "010",
                "typ": "verkaufsgruppe",
                "aktiv": True
            })

            nummer += 1
            org_code += 1

        # ----------------------------------------------------
        # Einkaufsgruppen
        # ----------------------------------------------------

        org_code = 610

        for wg in warengruppen:

            row = [
                nummer,
                str(org_code),
                "EG" + wg["wg_kurzcode"],
                f"Einkaufsgruppe {wg['bezeichnung']}",
                "020",
                "einkaufsgruppe",
                True
            ]

            rows.append(row)

            context_rows.append({
                "org_id": nummer,
                "org_code": str(org_code),
                "org_kuerzel": "EG" + wg["wg_kurzcode"],
                "bezeichnung": f"Einkaufsgruppe {wg['bezeichnung']}",
                "parent_code": "020",
                "typ": "einkaufsgruppe",
                "aktiv": True
            })

            nummer += 1
            org_code += 1

        return rows, context_rows

    # ------------------------------------------------------------------

    def update_context(self, context_rows):

        if self.context is not None:
            self.context.organisation = context_rows
