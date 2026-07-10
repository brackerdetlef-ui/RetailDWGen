"""
Generator fuer Artikelbestaende.

Erzeugt Testdaten fuer Lagerbestaende.

In Version 2.0 werden die Bestaende noch
zufaellig erzeugt und nicht aus den
Bewegungsdaten berechnet.
"""

from datetime import datetime
from random import randint, uniform

from generator.bestaende.bestaende_sequence import (
    BestaendeSequence
)
from generator.bestaende.bestaende_writer import (
    BestaendeWriter
)
from generator.bestaende.bestaende_check_writer import (
    BestaendeCheckWriter
)


class BestaendeGenerator:
    """
    Generator fuer Artikelbestaende.
    """

    def __init__(
        self,
        config,
        logger
    ):
        self.config = config
        self.logger = logger

        self.sequence = BestaendeSequence()
        self.writer = BestaendeWriter()
        self.check_writer = BestaendeCheckWriter()

    def generate(self):
        """
        Einstiegspunkt.
        """

        self.logger.info(
            "Starte Generator: Artikelbestaende"
        )

        export_start = datetime.now()

        #
        # Verkaufslager Filiale 001
        #
        warehouse_id = "110"

        inventory_date = export_start.strftime(
            "%Y-%m-%d"
        )

        export_timestamp = export_start

        #
        # Sequenz initialisieren
        #

        try:

            self.sequence.initialize_store(
                warehouse_id,
                85000001
            )

        except Exception:
            pass

        #
        # Anzahl Testdatensaetze
        #

        number_of_records = 1000

        inventory_records = []

        first_inventory_id = None
        last_inventory_id = None

        for _ in range(number_of_records):

            inventory_id = self.sequence.get_next_id(
                warehouse_id
            )

            if first_inventory_id is None:
                first_inventory_id = inventory_id

            last_inventory_id = inventory_id

            quantity = randint(
                0,
                500
            )

            average_purchase_price = round(
                uniform(
                    0.25,
                    250.00
                ),
                2
            )

            inventory_value = round(
                quantity
                * average_purchase_price,
                2
            )

            record = {

                "bestands_id": inventory_id,

                "lager_nummer": warehouse_id,

                "bestandsdatum": inventory_date,

                "artikel_nummer": str(
                    randint(
                        100000,
                        199999
                    )
                ),

                "bestandsmenge": quantity,

                "durchschnittlicher_ek_preis":
                    average_purchase_price,

                "bestandswert":
                    inventory_value

            }

            inventory_records.append(
                record
            )

        #
        # Bestandsdatei schreiben
        #

        inventory_filename = self.writer.write_inventory_file(

            warehouse_id=warehouse_id,

            export_timestamp=export_timestamp,

            inventory_records=inventory_records

        )

        export_end = datetime.now()

        #
        # Checkdatei schreiben
        #

        self.check_writer.write_check_file(

            warehouse_id=warehouse_id,

            export_timestamp=export_timestamp,

            inventory_date=inventory_date,

            first_inventory_id=first_inventory_id,

            last_inventory_id=last_inventory_id,

            record_count=len(
                inventory_records
            ),

            export_start=export_start,

            export_end=export_end,

            inventory_filename=inventory_filename

        )

        self.logger.info(
            f"{len(inventory_records)} "
            "Bestandsdatensaetze erzeugt."
        )

        self.logger.info(
            "Generator Artikelbestaende beendet."
        )
