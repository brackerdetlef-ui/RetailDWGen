"""
Writer fuer die technische Kontroll-Datei eines Wareneingangs-Exports.

Die Check-Datei dokumentiert den vom Warenwirtschaftssystem
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


class WareneingaengeCheckWriter:
    """
    Schreibt technische Kontroll-Dateien
    fuer Wareneingangsimporte.
    """

    def __init__(
        self,
        output_directory: str = "output/bewegungsdaten"
    ):
        self.output_directory = Path(output_directory)

    def write_check_file(
        self,
        store_id: str,
        export_timestamp: datetime,
        goods_receipt_date: str,
        first_goods_receipt_id: int | None,
        last_goods_receipt_id: int | None,
        record_count: int,
        export_start: datetime,
        export_end: datetime,
        goods_receipt_filename: str
    ) -> str:
        """
        Schreibt die Check-Datei.

        Beispiel:
        wareneingaenge_003_2026-07-09_23:58_check.csv
        """

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        timestamp = export_timestamp.strftime(
            "%Y-%m-%d_%H:%M"
        )

        filename = (
            f"wareneingaenge_{store_id}_{timestamp}_check.csv"
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
                "wareneingangsdatum",
                goods_receipt_date
            ),

            (
                "wareneingangs_datei",
                goods_receipt_filename
            ),

            (
                "erzeugt_am",
                export_timestamp.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            ),

            (
                "erste_wareneingangs_id",
                first_goods_receipt_id
            ),

            (
                "letzte_wareneingangs_id",
                last_goods_receipt_id
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

        return filename
