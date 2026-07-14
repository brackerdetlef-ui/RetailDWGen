#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : bon_verkaeufe_writer.py
Version : 2.2.0

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

"""
Writer fuer Bon-Verkaeufe.

Erzeugt die CSV-Datei fuer Bon-Verkaeufe.

Der Writer erzeugt keine Datensaetze und
keine IDs.
Er schreibt ausschliesslich bereits erzeugte
Bon-Verkaufsdaten.
"""

from pathlib import Path
import csv
from datetime import datetime


class BonVerkaeufeWriter:
    """
    Schreibt Bon-Verkaufsdateien.
    """

    def __init__(
        self,
        output_directory: str = "output/bon_verkaeufe"
    ):
        self.output_directory = Path(output_directory)

    def write_sales_file(
        self,
        store_id: str,
        export_timestamp: datetime,
        sales_records: list[dict]
    ) -> str:
        """
        Schreibt eine Bon-Verkaufsdatei.

        Beispiel:

        bon_verkaeufe_2026-07-10_23:58.csv

        Rueckgabe:
        Dateiname der erzeugten Bon-Verkaufsdatei.
        """

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        timestamp = export_timestamp.strftime(
            "%Y-%m-%d_%H:%M"
        )

        filename = (
            f"bon_verkaeufe_{timestamp}.csv"
        )

        filepath = (
            self.output_directory / filename
        )

        fieldnames = [

            "bon_sequence_id",

            "bon_nummer",

            "filial_nummer",

            "verkaufsdatum",

            "verkaufszeit",

            "kasse_nummer",

            "position_nummer",

            "artikel_nummer",

            "verkaufsmenge",

            "verkaufspreis",

            "verkaufswert"

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

        return filename
