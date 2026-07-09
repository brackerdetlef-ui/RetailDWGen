"""
RetailDWGen

Basisklasse aller Generatoren.

Version 1.7
"""

from __future__ import annotations

import random
from pathlib import Path
from typing import Any


class BaseGenerator:
    """
    Gemeinsame Basisklasse aller Generatoren.

    Jeder Generator besitzt den identischen Ablauf:

        initialize()
            ↓
        load_reference_data()
            ↓
        before_generate()
            ↓
        generate()
            ↓
        validate()
            ↓
        after_generate()
    """

    name = "BaseGenerator"

    # Generatoren können hier ihre Abhängigkeiten definieren.
    depends_on: list[str] = []

    def __init__(
        self,
        config: Any,
        logger: Any,
        context: Any,
    ) -> None:

        self.config = config
        self.logger = logger
        self.context = context

        # Eigener Zufallsgenerator
        self.random = random.Random()

        # Statistik
        self.records_created = 0

    @property
    def output_path(self) -> Path:
        return Path(self.config.output_directory)

    # ------------------------------------------------------------------
    # Logging
    # ------------------------------------------------------------------

    def log(self, message: str) -> None:
        if self.logger:
            self.logger.info(f"[{self.name}] {message}")

    # ------------------------------------------------------------------
    # Lebenszyklus
    # ------------------------------------------------------------------

    def run(self) -> None:
        """
        Führt den kompletten Generator-Lebenszyklus aus.
        """

        self.log("Starte Generator")

        self.initialize()
        self.load_reference_data()
        self.before_generate()

        self.generate()

        self.validate()
        self.after_generate()

        self.log(
            f"Generator beendet ({self.records_created} Datensätze erzeugt)"
        )

    # ------------------------------------------------------------------
    # Erweiterungspunkte
    # ------------------------------------------------------------------

    def initialize(self) -> None:
        """
        Einmalige Initialisierung.
        """
        pass

    def load_reference_data(self) -> None:
        """
        Stammdaten laden.
        """
        pass

    def before_generate(self) -> None:
        """
        Hook unmittelbar vor generate().
        """
        pass

    def generate(self) -> None:
        """
        Muss vom Generator implementiert werden.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__}.generate() ist nicht implementiert."
        )

    def validate(self) -> bool:
        """
        Optionale Validierung.
        """
        return True

    def after_generate(self) -> None:
        """
        Hook nach erfolgreicher Generierung.
        """
        pass

    # ------------------------------------------------------------------
    # Statistik
    # ------------------------------------------------------------------

    def record_created(self, amount: int = 1) -> None:
        """
        Erhöht den Datensatzzähler.
        """
        self.records_created += amount
