#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : csv_writer.py
Version : 2.0.1

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

import csv
from pathlib import Path


class CSVWriter:

    def __init__(self, filename):

        self.filename = filename

        Path(filename).parent.mkdir(parents=True, exist_ok=True)

    def write(self, header, rows):

        with open(
            self.filename,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(
                file,
                delimiter=";"
            )

            writer.writerow(header)

            writer.writerows(rows)
