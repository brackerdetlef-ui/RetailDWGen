"""
Writer fuer die technische Kontroll-Datei eines Verkaufs-Exports.

Die Check-Datei dokumentiert den vom Filial-Kassensystem
erzeugten Export.

Sie dient zur:
- Vollstaendigkeitskontrolle
- Nachverfolgung von Exporten
- Analyse technischer Probleme

Die Datei ist nicht Bestandteil des fachlichen DWH-Modells.
"""

from pathlib import Path
import csv
from datetime import datetime


class VerkaeufeCheckWriter:
    """
    Schreibt technische Kontroll-Dateien fuer Verkaufsimporte.
    """

    def __init__(
        self,
        output_directory: str = "ausgabe/verkaeufe"
    ):
        self.output_directory = Path(output_directory)

    def write_check_file(
        self,
        store_id: str,
        export_timestamp: datetime,
        sales_date: str,
        first_sales_id: int | None,
        last_sales_id: int | None,
        record_count: int,
        export_start: datetime,
        export_end: datetime,
        sales_filename: str
    ) -> str:
        """
        Schreibt die Check-Datei.

        Beispiel:
        verkaeufe_003_2026-07-09_23:58_check.csv
        """

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        timestamp = export_timestamp.strftime(
            "%Y-%m-%d_%H:%M"
        )

        filename = (
            f"verkaeufe_{store_id}_{timestamp}_check.csv"
        )

        filepath = (
            self.output_directory / filename
        )

        check_data = [
            (
                "filial_nummer",
                store_id
            ),
            (
                "verkaufsdatum",
                sales_date
            ),
            (
                "verkaufs_datei",
                sales_filename
            ),
            (
                "erzeugt_am",
                export_timestamp.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            ),
            (
                "erste_verkaufs_id",
                first_sales_id
            ),
            (
                "letzte_verkaufs_id",
                last_sales_id
            ),
            (
                "anzahl_saetze",
                record_count
            ),
            (
                "export_start",
                export_start.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            ),
            (
                "export_ende",
                export_end.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            )
        ]

        with open(
            filepath,
            "w",
            encoding="utf-8",
            newline=""
        ) as file:

            writer = csv.writer(
                file,
                delimiter=";"
            )

            writer.writerow(
                [
                    "parameter",
                    "wert"
                ]
            )

            writer.writerows(
                check_data
            )

        return str(filepath)
