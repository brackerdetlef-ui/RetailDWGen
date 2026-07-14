#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : bestaende_writer.py
Version : 2.2.0

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

"""
Writer fuer Artikelbestaende.

Erzeugt die CSV-Datei fuer den Bestand
eines Lagers.

Der Writer erzeugt keine Datensaetze und
keine IDs.
Er schreibt ausschliesslich bereits erzeugte
Bestandsdaten.
"""

from pathlib import Path
import csv
from datetime import datetime


class BestaendeWriter:
    """
    Schreibt Bestandsdateien.
    """

    def __init__(
        self,
        output_directory: str = "output/bestaende"
    ):
        self.output_directory = Path(output_directory)

    def write_inventory_file(
        self,
        warehouse_id: str,
        export_timestamp: datetime,
        inventory_records: list[dict]
    ) -> str:
        """
        Schreibt eine Bestandsdatei.

        Beispiel:

        artikelbestaende_2026-07-10_23:58.csv

        Rueckgabe:
        Dateiname der erzeugten Bestandsdatei.
        """

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        timestamp = export_timestamp.strftime(
            "%Y-%m-%d_%H:%M"
        )

        filename = (
            f"artikelbestaende_{timestamp}.csv"
        )

        filepath = (
            self.output_directory / filename
        )

        fieldnames = [

            "bestands_id",

            "lager_nummer",

            "bestandsdatum",

            "artikel_nummer",

            "bestandsmenge",

            "durchschnittlicher_ek_preis",

            "bestandswert"

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
