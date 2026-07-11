#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : wareneingaenge_sequence.py
Version : 2.0.1

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

"""
Verwaltung der fortlaufenden Wareneingangs-IDs.

Die ID stammt aus dem Warenwirtschaftssystem der Filiale.

Sie dient ausschliesslich:

- Vollstaendigkeitspruefung
- Erkennung fehlender Datensaetze
- technische Nachverfolgung

Die ID ist kein fachlicher Schluessel im DWH.
"""

from pathlib import Path
import json


class WareneingaengeSequence:
    """
    Verwaltet fortlaufende IDs je Filiale.
    """

    def __init__(
        self,
        storage_file: str = "konfiguration/wareneingaenge_sequences.json"
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
        store_id: str,
        start_id: int
    ):
        """
        Initialisiert eine neue Filial-Sequenz.

        Beispiel:
        Filiale 003 startet mit 55000001.
        """

        if store_id not in self.sequences:
            self.sequences[store_id] = start_id - 1
            self._save()

    def get_next_id(
        self,
        store_id: str
    ) -> int:
        """
        Liefert die naechste Wareneingangs-ID.
        """

        if store_id not in self.sequences:
            raise ValueError(
                f"No sequence initialized for store {store_id}"
            )

        self.sequences[store_id] += 1

        self._save()

        return self.sequences[store_id]

    def get_id_range(
        self,
        store_id: str,
        number_of_records: int
    ) -> tuple[int, int]:
        """
        Reserviert einen zusammenhaengenden ID-Bereich.

        Beispiel:
        250 Datensaetze

        Ergebnis:
        55000001 - 55000250
        """

        if store_id not in self.sequences:
            raise ValueError(
                f"No sequence initialized for store {store_id}"
            )

        first_id = self.sequences[store_id] + 1

        last_id = (
            self.sequences[store_id]
            + number_of_records
        )

        self.sequences[store_id] = last_id

        self._save()

        return first_id, last_id

    def get_current_id(
        self,
        store_id: str
    ) -> int:
        """
        Liefert die zuletzt vergebene Wareneingangs-ID.
        """

        if store_id not in self.sequences:
            raise ValueError(
                f"No sequence initialized for store {store_id}"
            )

        return self.sequences[store_id]
