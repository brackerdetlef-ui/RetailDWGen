#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : inventuren_writer.py
Version : 2.0.1

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

"""
Writer fuer Inventuren.

Erzeugt die CSV-Datei einer Inventur
eines Lagers.

Der Writer erzeugt keine Datensaetze und
keine IDs.
Er schreibt ausschliesslich bereits erzeugte
Inventurdaten.
"""

from pathlib import Path
import csv
from datetime import datetime


class InventurenWriter:
    """
    Schreibt Inventurdateien.
    """

    def __init__(
        self,
        output_directory: str = "output/inventuren"
    ):
        self.output_directory = Path(output_directory)

    def write_inventory_file(
        self,
        warehouse_id: str,
        export_timestamp: datetime,
        inventory_records: list[dict]
    ) -> str:
        """
        Schreibt eine Inventurdatei.

        Beispiel:

        inventuren_210_2026-07-10_23:58.csv

        Rueckgabe:
        Dateiname der erzeugten Inventurdatei.
        """

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        timestamp = export_timestamp.strftime(
            "%Y-%m-%d_%H:%M"
        )

        filename = (
            f"inventuren_{warehouse_id}_{timestamp}.csv"
        )

        filepath = (
            self.output_directory / filename
        )

        fieldnames = [

            "inventur_id",

            "lager_nummer",

            "inventurdatum",

            "inventurart",

            "inventurgrund",

            "artikel_nummer",

            "gezählte_menge",

            "systemmenge",

            "differenz"

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
                inventory_records
            )

        return filename
