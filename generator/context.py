#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : context.py
Version : 2.0.1

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class DataContext:
    """
    Zentrale Ablage aller erzeugten Daten.

    Der Context ersetzt keine Datenbank und keine CSV-Dateien.
    Er dient ausschließlich dazu, dass nachfolgende Generatoren
    bereits erzeugte Objekte direkt verwenden können.
    """

    warengruppen: list[Any] = field(default_factory=list)
    hersteller: list[Any] = field(default_factory=list)
    marken: list[Any] = field(default_factory=list)

    artikel: list[Any] = field(default_factory=list)

    kunden: list[Any] = field(default_factory=list)

    filialen: list[Any] = field(default_factory=list)
    lager: list[Any] = field(default_factory=list)

    lieferanten: list[Any] = field(default_factory=list)

    mitarbeiter: list[Any] = field(default_factory=list)

    organisation: dict[str, Any] = field(default_factory=dict)

    def clear(self) -> None:
        """Setzt den Context zurück."""

        self.__dict__.update(DataContext().__dict__)
