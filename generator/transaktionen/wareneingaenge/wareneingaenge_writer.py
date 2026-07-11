#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : wareneingaenge_writer.py
Version : 2.0.1

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

"""
Writer fuer Wareneingangs-Dateien.

Erzeugt die CSV-Datei, die den Wareneingang
einer Filiale beschreibt.

Der Writer erzeugt keine Wareneingaenge und
keine IDs.
Er schreibt ausschliesslich bereits erzeugte
Wareneingangsdaten.
"""

from pathlib import Path
import csv
from datetime import datetime


class WareneingaengeWriter:
    """
    Schreibt Wareneingangsdateien.
    """

    def __init__(
        self,
        output_directory: str = "output/bewegungsdaten"
    ):
        self.output_directory = Path(output_directory)

    def write_goods_receipt_file(
        self,
        store_id: str,
        export_timestamp: datetime,
        goods_receipt_records: list[dict]
    ) -> str:
        """
        Schreibt eine Wareneingangsdatei.

        Beispiel:
        wareneingaenge_003_2026-07-09_23:58.csv

        Rueckgabe:
        Dateiname der erzeugten Wareneingangsdatei.
        """

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        timestamp = export_timestamp.strftime(
            "%Y-%m-%d_%H:%M"
        )

        filename = (
            f"wareneingaenge_{store_id}_{timestamp}.csv"
        )

        filepath = (
            self.output_directory / filename
        )

        fieldnames = [

            "wareneingangs_id",

            "filial_nummer",

            "lager_nummer",

            "wareneingangsdatum",

            "lieferant_nummer",

            "artikel_nummer",

            "eingangsmenge",

            "einkaufspreis",

            "wareneingangswert"

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
                goods_receipt_records
            )

        return filename
