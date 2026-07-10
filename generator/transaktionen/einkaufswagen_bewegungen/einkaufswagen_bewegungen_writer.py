"""
Writer fuer Einkaufswagen-Bewegungen.

Erzeugt die CSV-Datei fuer Einkaufswagen-
Bewegungen.

Der Writer erzeugt keine Datensaetze und
keine IDs.
Er schreibt ausschliesslich bereits erzeugte
Bewegungsdaten.
"""

from pathlib import Path
import csv
from datetime import datetime


class EinkaufswagenBewegungenWriter:
    """
    Schreibt Einkaufswagen-Bewegungsdateien.
    """

    def __init__(
        self,
        output_directory: str = (
            "output/einkaufswagen_bewegungen"
        )
    ):
        self.output_directory = Path(
            output_directory
        )

    def write_movements_file(
        self,
        store_id: str,
        export_timestamp: datetime,
        movement_records: list[dict]
    ) -> str:
        """
        Schreibt eine Einkaufswagen-
        Bewegungsdatei.

        Beispiel:

        einkaufswagen_bewegungen_001_2026-07-10_23:58.csv

        Rueckgabe:
        Dateiname der erzeugten CSV-Datei.
        """

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        timestamp = export_timestamp.strftime(
            "%Y-%m-%d_%H:%M"
        )

        filename = (
            f"einkaufswagen_bewegungen_"
            f"{store_id}_{timestamp}.csv"
        )

        filepath = (
            self.output_directory
            / filename
        )

        fieldnames = [

            "sequence_id",

            "filial_nummer",

            "einkaufswagen_id",

            "einkauf_id",

            "zeitpunkt",

            "gang_nummer",

            "meter",

            "seite"

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
                movement_records
            )

        return filename
