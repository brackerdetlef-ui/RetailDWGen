"""
Hilfsklasse zur Ermittlung der Lagernummern
einer Filiale.

Die Lagernummern werden aus der Filialnummer
und einem Lager-Suffix gebildet.
Hunderter und Tausender = Lagernummer 1-99
Zehner 1 Kundenseitig 2 Lieferantenseitig

Beispiele:

Filiale 001:
110 Verkauf
118 Pfand
119 Kunden-Retouren
121 Lieferanten-Retouren
129 Verloren/Vernichtet

Filiale 002:
210 Verkauf
218 Pfand
219 Kunden-Retouren
221 Lieferanten-Retouren
229 Verloren/Vernichtet

Filiale 099:
9910 Verkauf
9918 Pfand
9919 Kunden-Retouren
9921 Lieferanten-Retouren
9929 Verloren/Vernichtet
"""


class LagerNummern:

    @staticmethod
    def get_lager_nummer(
        store_id: str,
        suffix: str
    ) -> str:
        """
        Ermittelt eine Lagernummer.

        Beispiel:

        store_id = "001"
        suffix   = "19"

        Ergebnis:

        119
        """

        return f"{int(store_id)}{suffix}"

    @staticmethod
    def verkauf(store_id: str) -> str:
        return LagerNummern.get_lager_nummer(
            store_id,
            "10"
        )

    @staticmethod
    def pfand(store_id: str) -> str:
        return LagerNummern.get_lager_nummer(
            store_id,
            "18"
        )

    @staticmethod
    def kunden_retouren(store_id: str) -> str:
        return LagerNummern.get_lager_nummer(
            store_id,
            "19"
        )

    @staticmethod
    def lieferanten_retouren(store_id: str) -> str:
        return LagerNummern.get_lager_nummer(
            store_id,
            "21"
        )

    @staticmethod
    def verloren_vernichtet(store_id: str) -> str:
        return LagerNummern.get_lager_nummer(
            store_id,
            "29"
        )

    @staticmethod
    def sperrlager(store_id: str) -> str:
        return LagerNummern.get_lager_nummer(
            store_id,
            "40"
        )
