#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : config.py
Version : 2.0.1

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

import yaml


class Config:

    def __init__(self, filename: str = "config/config.yaml"):

        with open(filename, "r", encoding="utf-8") as f:
            self.data = yaml.safe_load(f)

    def get(self, *keys):

        value = self.data

        for key in keys:

            if key not in value:
                raise KeyError(
                    f"Konfigurationsschlüssel '{'.'.join(keys)}' nicht gefunden."
                )

            value = value[key]

        return value
