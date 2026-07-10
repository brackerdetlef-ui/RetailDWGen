"""
Generator fuer Verkaufsdaten.

Erzeugt Testdaten fuer Verkaufsimporte.
"""

from datetime import datetime
from random import randint, uniform

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
        Einstiegspunkt.
        """

        self.logger.info(
            "Starte Generator: Verkaeufe"
        )

        export_start = datetime.now()

        store_id = "001"

        sales_date = export_start.strftime(
            "%Y-%m-%d"
        )

        export_timestamp = export_start

        #
        # Sequenz initialisieren
        #

        try:
            self.sequence.initialize_store(
                store_id,
                10000001
            )
        except Exception:
            pass

        #
        # Anzahl Testdatensaetze
        #

        number_of_records = 250

        sales_records = []

        first_sales_id = None
        last_sales_id = None

        for _ in range(number_of_records):

            sales_id = self.sequence.get_next_id(
                store_id
            )

            if first_sales_id is None:
                first_sales_id = sales_id

            last_sales_id = sales_id

            record = {

                "verkaufs_id": sales_id,

                "filial_nummer": store_id,

                "verkaufsdatum": sales_date,

                "artikel_nummer": str(
                    randint(
                        100000,
                        199999
                    )
                ),

                "verkaufs_menge": randint(
                    1,
                    5
                ),

                "netto_umsatz": round(
                    uniform(
                        0.99,
                        99.99
                    ),
                    2
                )

            }

            sales_records.append(
                record
            )

        #
        # Verkaufsdatei schreiben
        #

        sales_filepath = self.writer.write_sales_file(
            store_id=store_id,
            export_timestamp=export_timestamp,
            sales_records=sales_records
        )

        export_end = datetime.now()

        #
        # Checkdatei schreiben
        #

        self.check_writer.write_check_file(

            store_id=store_id,

            export_timestamp=export_timestamp,

            sales_date=sales_date,

            first_sales_id=first_sales_id,

            last_sales_id=last_sales_id,

            record_count=len(
                sales_records
            ),

            export_start=export_start,

            export_end=export_end,

            sales_filename=sales_filepath

        )

        self.logger.info(
            f"{len(sales_records)} Verkaufsdatensaetze erzeugt."
        )

        self.logger.info(
            "Generator Verkaeufe beendet."
        )
