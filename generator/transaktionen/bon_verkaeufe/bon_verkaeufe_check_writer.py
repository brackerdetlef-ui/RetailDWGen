#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : bon_verkaeufe_check_writer.py
Version : 2.0.1

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

"""
Writer fuer die technische Kontroll-Datei eines
Bon-Verkaufs-Exports.

Die Check-Datei dokumentiert den vom
Kassensystem erzeugten Export.

Sie dient zur:

- Vollstaendigkeitskontrolle
- Nachverfolgung von Exporten
- Analyse technischer Probleme

Die Datei ist nicht Bestandteil des
fachlichen DWH-Modells.
"""

from pathlib import Path
import csv
from datetime import datetime


class BonVerkaeufeCheckWriter:
    """
    Schreibt technische Kontroll-Dateien
    fuer Bon-Verkaufsimporte.
    """

    def __init__(
        self,
        output_directory: str = "output/bon_verkaeufe"
    ):
        self.output_directory = Path(output_directory)

    def write_check_file(
        self,
        store_id: str,
        export_timestamp: datetime,
        sales_date: str,
        first_sequence_id: int | None,
        last_sequence_id: int | None,
        receipt_count: int,
        record_count: int,
        export_start: datetime,
        export_end: datetime,
        sales_filename: str
    ) -> str:
        """
        Schreibt die Check-Datei.

        Beispiel:

        bon_verkaeufe_001_2026-07-10_23:58_check.csv
        """

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        timestamp = export_timestamp.strftime(
            "%Y-%m-%d_%H:%M"
        )

        filename = (
            f"bon_verkaeufe_{store_id}_{timestamp}_check.csv"
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
                "bon_verkaeufe_datei",
                sales_filename
            ),

            (
                "erzeugt_am",
                export_timestamp.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            ),

            (
                "erste_sequence_id",
                first_sequence_id
            ),

            (
                "letzte_sequence_id",
                last_sequence_id
            ),

            (
                "anzahl_bons",
                receipt_count
            ),

            (
                "anzahl_positionen",
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
