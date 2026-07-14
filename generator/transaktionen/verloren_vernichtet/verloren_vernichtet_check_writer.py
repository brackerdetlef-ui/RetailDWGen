#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : verloren_vernichtet_check_writer.py
Version : 2.2.0

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

"""
Writer fuer die technische Kontroll-Datei eines
Verlust-/Vernichtungs-Exports.

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


class VerlorenVernichtetCheckWriter:
    """
    Schreibt technische Kontroll-Dateien
    fuer Verlustimporte.
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
        loss_date: str,
        first_loss_id: int | None,
        last_loss_id: int | None,
        record_count: int,
        export_start: datetime,
        export_end: datetime,
        loss_filename: str
    ) -> str:
        """
        Schreibt die Check-Datei.

        Beispiel:

        verloren_vernichtet_2026-07-09_23:58_check.csv
        """

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        timestamp = export_timestamp.strftime(
            "%Y-%m-%d_%H:%M"
        )

        filename = (
            f"verloren_vernichtet_{timestamp}_check.csv"
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
                "verlustdatum",
                loss_date
            ),

            (
                "verlust_datei",
                loss_filename
            ),

            (
                "erzeugt_am",
                export_timestamp.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            ),

            (
                "erste_verlust_id",
                first_loss_id
            ),

            (
                "letzte_verlust_id",
                last_loss_id
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

