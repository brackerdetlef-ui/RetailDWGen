#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : inventuren_sequence.py
Version : 2.0.1

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

"""
Verwaltung der fortlaufenden Inventur-IDs.

Die ID stammt aus dem Warenwirtschaftssystem.

Sie dient ausschliesslich:

- Vollstaendigkeitspruefung
- Erkennung fehlender Datensaetze
- technische Nachverfolgung

Die ID ist kein fachlicher Schluessel im DWH.
"""

from pathlib import Path
import json


class InventurenSequence:
    """
    Verwaltet fortlaufende Inventur-IDs je Lager.
    """

    def __init__(
        self,
        storage_file: str = "konfiguration/inventuren_sequences.json"
    ):
        self.storage_file = Path(storage_file)
        self.sequences = self._load()

    def _load(self) -> dict:
        """
        Laedt gespeicherte Sequenzstaende.
        """

        if self.storage_file.exists():
            with open(
                self.storage_file,
                "r",
                encoding="utf-8"
            ) as file:
                return json.load(file)

        return {}

    def _save(self):
        """
        Speichert aktuelle Sequenzstaende.
        """

        self.storage_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            self.storage_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.sequences,
                file,
                indent=2
            )

    def initialize_store(
        self,
        warehouse_id: str,
        start_id: int
    ):
        """
        Initialisiert eine neue Lager-Sequenz.

        Beispiel:
        Lager 210 startet mit 95000001.
        """

        if warehouse_id not in self.sequences:
            self.sequences[warehouse_id] = start_id - 1
            self._save()

    def get_next_id(
        self,
        warehouse_id: str
    ) -> int:
        """
        Liefert die naechste Inventur-ID.
        """

        if warehouse_id not in self.sequences:
            raise ValueError(
                f"No sequence initialized for warehouse {warehouse_id}"
            )

        self.sequences[warehouse_id] += 1

        self._save()

        return self.sequences[warehouse_id]

    def get_id_range(
        self,
        warehouse_id: str,
        number_of_records: int
    ) -> tuple[int, int]:
        """
        Reserviert einen zusammenhaengenden ID-Bereich.
        """

        if warehouse_id not in self.sequences:
            raise ValueError(
                f"No sequence initialized for warehouse {warehouse_id}"
            )

        first_id = (
            self.sequences[warehouse_id] + 1
        )

        last_id = (
            self.sequences[warehouse_id]
            + number_of_records
        )

        self.sequences[warehouse_id] = last_id

        self._save()

        return first_id, last_id

    def get_current_id(
        self,
        warehouse_id: str
    ) -> int:
        """
        Liefert die zuletzt vergebene Inventur-ID.
        """

        if warehouse_id not in self.sequences:
            raise ValueError(
                f"No sequence initialized for warehouse {warehouse_id}"
            )

        return self.sequences[warehouse_id]
