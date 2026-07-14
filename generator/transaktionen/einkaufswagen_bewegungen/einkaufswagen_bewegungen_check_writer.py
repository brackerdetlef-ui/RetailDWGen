#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : einkaufswagen_bewegungen_check_writer.py
Version : 2.2.0

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

"""
Writer fuer die technische Kontroll-Datei eines
Einkaufswagen-Bewegungs-Exports.

Die Check-Datei dokumentiert den vom
Einkaufswagen-Ortungssystem erzeugten Export.

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


class EinkaufswagenBewegungenCheckWriter:
    """
    Schreibt technische Kontroll-Dateien fuer
    Einkaufswagen-Bewegungen.
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

    def write_check_file(
        self,
        store_id: str,
        export_timestamp: datetime,
        movement_date: str,
        first_sequence_id: int | None,
        last_sequence_id: int | None,
        record_count: int,
        export_start: datetime,
        export_end: datetime,
        movements_filename: str
    ) -> str:
        """
        Schreibt die Check-Datei.

        Beispiel:

        einkaufswagen_bewegungen_2026-07-09_23:58_check.csv
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
            f"{timestamp}_check.csv"
        )

        filepath = (
            self.output_directory
            / filename
        )

        check_data = [

            (
                "filial_nummer",
                store_id
            ),

            (
                "bewegungsdatum",
                movement_date
            ),

            (
                "bewegungs_datei",
                movements_filename
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
