"""
Generator fuer Kundenretouren.

Erzeugt Testdaten fuer Kundenretouren.
"""

from datetime import datetime
from random import randint, uniform, choice

from generator.transaktionen.kunden_retouren.kunden_retouren_sequence import (
    KundenRetourenSequence
)
from generator.transaktionen.kunden_retouren.kunden_retouren_writer import (
    KundenRetourenWriter
)
from generator.transaktionen.kunden_retouren.kunden_retouren_check_writer import (
    KundenRetourenCheckWriter
)


class KundenRetourenGenerator:
    """
    Generator fuer Kundenretouren.
    """

    def __init__(
        self,
        config,
        logger
    ):
        self.config = config
        self.logger = logger

        self.sequence = KundenRetourenSequence()
        self.writer = KundenRetourenWriter()
        self.check_writer = KundenRetourenCheckWriter()

    def generate(self):
        """
        Einstiegspunkt.
        """

        self.logger.info(
            "Starte Generator: KundenRetouren"
        )

        export_start = datetime.now()

        store_id = "001"

        #
        # Kundenretourenlager
        #
        warehouse_id = "219"

        return_date = export_start.strftime(
            "%Y-%m-%d"
        )

        export_timestamp = export_start

        #
        # Sequenz initialisieren
        #

        try:

            self.sequence.initialize_store(
                store_id,
                75000001
            )

        except Exception:
            pass

        #
        # Moegliche Retourengruende
        #

        return_reasons = [

            "GEFAELLT_NICHT",

            "FALSCHER_ARTIKEL",

            "DEFEKT",

            "BESCHAEDIGT",

            "GARANTIE",

            "UMTAUSCH",

            "SONSTIGES"

        ]

        #
        # Anzahl Testdatensaetze
        #

        number_of_records = 50

        customer_return_records = []

        first_return_id = None
        last_return_id = None

        for _ in range(number_of_records):

            return_id = self.sequence.get_next_id(
                store_id
            )

            if first_return_id is None:
                first_return_id = return_id

            last_return_id = return_id

            quantity = randint(
                1,
                5
            )

            sales_price = round(
                uniform(
                    0.99,
                    199.99
                ),
                2
            )

            record = {

                "retoure_id": return_id,

                "filial_nummer": store_id,

                "lager_nummer": warehouse_id,

                "retourendatum": return_date,

                #
                # Referenz auf den
                # urspruenglichen Verkauf
                #

                "verkaufs_id": randint(
                    10000001,
                    10999999
                ),

                "artikel_nummer": str(
                    randint(
                        100000,
                        199999
                    )
                ),

                "retourenmenge": quantity,

                "verkaufspreis": sales_price,

                "retourenwert": round(
                    quantity * sales_price,
                    2
                ),

                "retourengrund": choice(
                    return_reasons
                )

            }

            customer_return_records.append(
                record
            )

        #
        # Retourendatei schreiben
        #

        return_filename = self.writer.write_customer_returns_file(
            store_id=store_id,
            export_timestamp=export_timestamp,
            customer_return_records=customer_return_records
        )

        export_end = datetime.now()

        #
        # Checkdatei schreiben
        #

        self.check_writer.write_check_file(

            store_id=store_id,

            export_timestamp=export_timestamp,

            return_date=return_date,

            first_return_id=first_return_id,

            last_return_id=last_return_id,

            record_count=len(
                customer_return_records
            ),

            export_start=export_start,

            export_end=export_end,

            return_filename=return_filename

        )

        self.logger.info(
            f"{len(customer_return_records)} Kundenretouren erzeugt."
        )

        self.logger.info(
            "Generator KundenRetouren beendet."
        )
