"""
Generator fuer Verkaufsdaten.

Der Generator simuliert den Tagesabschluss eines Filial-Kassensystems.

Dabei entstehen:

- Verkaufsdatei
- technische Check-Datei

Die eigentliche Verkaufslogik wird schrittweise erweitert.
"""

from generator.transaktionen.verkaeufe.verkaeufe_sequence import (
    VerkaeufeSequence
)
from generator.transaktionen.verkaeufe.verkaeufe_writer import (
    VerkaeufeWriter
)
from generator.transaktionen.verkaeufe.verkaeufe_check_writer import (
    VerkaeufeCheckWriter
)


class VerkaeufeGenerator:
    """
    Generator fuer Verkaufsdaten.
    """

    def __init__(
        self,
        config,
        logger
    ):
        self.config = config
        self.logger = logger

        self.sequence = VerkaeufeSequence()
        self.writer = VerkaeufeWriter()
        self.check_writer = VerkaeufeCheckWriter()

    def generate(self):
        """
        Einstiegspunkt des Generators.

        Der Manager ruft diese Methode auf.
        """

        self.logger.info(
            "Starte Generator: Verkaeufe"
        )

        filiale = "001"

        verkaufsdatum = "2026-07-09"

        verkaufs_id = 1324 

        # -----------------------------------------------------------------
        # Die eigentliche Verkaufs-Simulation wird in den naechsten
        # Ausbaustufen implementiert.
        #
        # Geplant:
        #
        # 1. Filialen bestimmen
        # 2. Tagesabschluss simulieren
        # 3. Verkaufsdaten je Artikel aggregieren
        # 4. Verkaufs-IDs vergeben
        # 5. Verkaufsdatei schreiben
        # 6. Check-Datei schreiben
        # 7. Uebertragung simulieren
        # -----------------------------------------------------------------

        self.logger.info(
            "Generator Verkaeufe beendet."
        )
