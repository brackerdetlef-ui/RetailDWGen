"""
Writer fuer Verlust- und Vernichtungsdateien.

Erzeugt die CSV-Datei fuer verlorene bzw.
vernichtete Artikel einer Filiale.

Der Writer erzeugt keine Datensaetze und
keine IDs.
Er schreibt ausschliesslich bereits erzeugte
Verlustdaten.
"""

from pathlib import Path
import csv
from datetime import datetime


class VerlorenVernichtetWriter:
    """
    Schreibt Verlustdateien.
    """

    def __init__(
        self,
        output_directory: str = "output/bewegungsdaten"
    ):
        self.output_directory = Path(output_directory)

    def write_loss_file(
        self,
        store_id: str,
        export_timestamp: datetime,
        loss_records: list[dict]
    ) -> str:
        """
        Schreibt eine Verlustdatei.

        Beispiel:
        verloren_vernichtet_003_2026-07-09_23:58.csv

        Rueckgabe:
        Dateiname der erzeugten Verlustdatei.
        """

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        timestamp = export_timestamp.strftime(
            "%Y-%m-%d_%H:%M"
        )

        filename = (
            f"verloren_vernichtet_{store_id}_{timestamp}.csv"
        )

        filepath = (
            self.output_directory / filename
        )

        fieldnames = [

            "verlust_id",

            "filial_nummer",

            "lager_nummer",

            "verlustdatum",

            "artikel_nummer",

            "verlustmenge",

            "einkaufspreis",

            "verlustwert",

            "verlustgrund"

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
                loss_records
            )

        return filename
