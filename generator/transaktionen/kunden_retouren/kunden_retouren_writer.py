"""
Writer fuer Kundenretouren.

Erzeugt die CSV-Datei fuer Kundenretouren
einer Filiale.

Der Writer erzeugt keine Datensaetze und
keine IDs.
Er schreibt ausschliesslich bereits erzeugte
Retourendaten.
"""

from pathlib import Path
import csv
from datetime import datetime


class KundenRetourenWriter:
    """
    Schreibt Kundenretourendateien.
    """

    def __init__(
        self,
        output_directory: str = "output/bewegungsdaten"
    ):
        self.output_directory = Path(output_directory)

    def write_customer_returns_file(
        self,
        store_id: str,
        export_timestamp: datetime,
        customer_return_records: list[dict]
    ) -> str:
        """
        Schreibt eine Kundenretourendatei.

        Beispiel:

        kunden_retouren_003_2026-07-09_23:58.csv

        Rueckgabe:
        Dateiname der erzeugten Kundenretourendatei.
        """

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        timestamp = export_timestamp.strftime(
            "%Y-%m-%d_%H:%M"
        )

        filename = (
            f"kunden_retouren_{store_id}_{timestamp}.csv"
        )

        filepath = (
            self.output_directory / filename
        )

        fieldnames = [

            "retoure_id",

            "filial_nummer",

            "lager_nummer",

            "retourendatum",

            "verkaufs_id",

            "artikel_nummer",

            "retourenmenge",

            "verkaufspreis",

            "retourenwert",

            "retourengrund"

        ]

        with open(
            filepath,
            "w",
            encoding="utf-8",
            newline=""
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames,
                delimiter=";"
            )

            writer.writeheader()

            writer.writerows(
                customer_return_records
            )

        return filename
