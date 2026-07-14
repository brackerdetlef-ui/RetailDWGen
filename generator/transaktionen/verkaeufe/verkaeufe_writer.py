#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : verkaeufe_writer.py
Version : 2.2.0

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

"""
Writer fuer Verkaufs-Tagesdateien.

Erzeugt die CSV-Datei, die vom Kassensystem einer Filiale
nach dem Tagesabschluss bereitgestellt wird.

Der Writer erzeugt keine Verkaufsdaten und keine IDs.
Er schreibt nur bereits erzeugte Verkaufsaggregation.
"""

from pathlib import Path
import csv
from datetime import datetime


class VerkaeufeWriter:
    """
    Schreibt Verkaufsdateien.
    """

    def __init__(
        self,
        output_directory: str = "output/bewegungsdaten"
    ):
        self.output_directory = Path(output_directory)

    def write_sales_file(
        self,
        store_id: str,
        export_timestamp: datetime,
        sales_records: list[dict]
    ) -> str:
        """
        Schreibt eine Verkaufsdatei.

        Beispiel:
        verkaeufe_2026-07-09_23:58.csv

        Rueckgabe:
        Dateiname der erzeugten Verkaufsdatei.
        """

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        timestamp = export_timestamp.strftime(
            "%Y-%m-%d_%H:%M"
        )

        filename = (
            f"verkaeufe_{timestamp}.csv"
        )

        filepath = (
            self.output_directory / filename
        )

        fieldnames = [
            "verkaufs_id",
            "filial_nummer",
            "verkaufsdatum",
            "artikel_nummer",
            "verkaufs_menge",
            "netto_umsatz"
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
                sales_records
            )

        #
        # Fuer die Check-Datei wird nur der Dateiname benoetigt.
        #
        return filename
