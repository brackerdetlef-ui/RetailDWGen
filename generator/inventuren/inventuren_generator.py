"""
Generator fuer Inventuren.

Erzeugt Testdaten fuer Inventuren eines Lagers.

In Version 2.0 werden die Inventurdaten
noch zufaellig erzeugt.
"""

from datetime import datetime
from random import choice, randint

from generator.inventuren.inventuren_sequence import (
    InventurenSequence
)
from generator.inventuren.inventuren_writer import (
    InventurenWriter
)
from generator.inventuren.inventuren_check_writer import (
    InventurenCheckWriter
)


class InventurenGenerator:
    """
    Generator fuer Inventuren.
    """

    def __init__(
        self,
        config,
        logger
    ):
        self.config = config
        self.logger = logger

        self.sequence = InventurenSequence()
        self.writer = InventurenWriter()
        self.check_writer = InventurenCheckWriter()

    def generate(self):
        """
        Einstiegspunkt.
        """

        self.logger.info(
            "Starte Generator: Inventuren"
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

        self.sequence.initialize_store(
            warehouse_id,
            95000001
        )

        #
        # Inventurart
        #

        inventory_type = choice(
            [
                "STICHTAG",
                "STICHPROBE",
                "PERMANENT"
            ]
        )

        #
        # Inventurgrund
        #

        inventory_reason = choice(
            [
                "Regulaere Inventur",
                "Vom System angeordnet",
                "Auffaellige Bestandsabweichung",
                "Stichprobenkontrolle",
                "Revision",
                "Interne Kontrolle"
            ]
        )

        #
        # Anzahl Datensaetze
        #

        number_of_records = 500

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

            system_quantity = randint(
                0,
                500
            )

            counted_quantity = max(
                0,
                system_quantity
                + randint(-5, 5)
            )

            difference = (
                counted_quantity
                - system_quantity
            )

            record = {

                "inventur_id":
                    inventory_id,

                "lager_nummer":
                    warehouse_id,

                "inventurdatum":
                    inventory_date,

                "inventurart":
                    inventory_type,

                "inventurgrund":
                    inventory_reason,

                "artikel_nummer":
                    str(
                        randint(
                            100000,
                            199999
                        )
                    ),

                "gezählte_menge":
                    counted_quantity,

                "systemmenge":
                    system_quantity,

                "differenz":
                    difference

            }

            inventory_records.append(
                record
            )

        #
        # Inventurdatei schreiben
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
            "Inventurdatensaetze erzeugt."
        )

        self.logger.info(
            "Generator Inventuren beendet."
        )
