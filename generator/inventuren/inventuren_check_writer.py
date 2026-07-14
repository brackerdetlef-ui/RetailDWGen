#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : inventuren_check_writer.py
Version : 2.2.0

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

"""
Writer fuer die technische Kontroll-Datei eines
Inventur-Exports.

Die Check-Datei dokumentiert den vom
Warenwirtschaftssystem erzeugten Export.

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


class InventurenCheckWriter:
    """
    Schreibt technische Kontroll-Dateien
    fuer Inventurimporte.
    """

    def __init__(
        self,
        output_directory: str = "output/inventuren"
    ):
        self.output_directory = Path(output_directory)

    def write_check_file(
        self,
        warehouse_id: str,
        export_timestamp: datetime,
        inventory_date: str,
        first_inventory_id: int | None,
        last_inventory_id: int | None,
        record_count: int,
        export_start: datetime,
        export_end: datetime,
        inventory_filename: str
    ) -> str:
        """
        Schreibt die Check-Datei.

        Beispiel:

        inventuren_2026-07-10_23:58_check.csv
        """

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        timestamp = export_timestamp.strftime(
            "%Y-%m-%d_%H:%M"
        )

        filename = (
            f"inventuren_{timestamp}_check.csv"
        )

        filepath = (
            self.output_directory / filename
        )

        check_data = [

            (
                "lager_nummer",
                warehouse_id
            ),

            (
                "inventurdatum",
                inventory_date
            ),

            (
                "inventur_datei",
                inventory_filename
            ),

            (
                "erzeugt_am",
                export_timestamp.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            ),

            (
                "erste_inventur_id",
                first_inventory_id
            ),

            (
                "letzte_inventur_id",
                last_inventory_id
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
