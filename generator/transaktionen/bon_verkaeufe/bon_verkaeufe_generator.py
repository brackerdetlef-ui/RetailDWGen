#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : bon_verkaeufe_generator.py
Version : 2.0.1

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

"""
Generator fuer Bon-Verkaeufe.

Erzeugt Testdaten fuer Bon-Verkaeufe.

In Version 2.0 werden die Bon-Verkaeufe
noch unabhaengig von den aggregierten
Verkaeufen erzeugt.
"""

from datetime import datetime
from random import randint, uniform

from generator.bon_verkaeufe.bon_verkaeufe_sequence import (
    BonVerkaeufeSequence
)
from generator.bon_verkaeufe.bon_verkaeufe_writer import (
    BonVerkaeufeWriter
)
from generator.bon_verkaeufe.bon_verkaeufe_check_writer import (
    BonVerkaeufeCheckWriter
)


class BonVerkaeufeGenerator:
    """
    Generator fuer Bon-Verkaeufe.
    """

    def __init__(
        self,
        config,
        logger
    ):
        self.config = config
        self.logger = logger

        self.sequence = BonVerkaeufeSequence()
        self.writer = BonVerkaeufeWriter()
        self.check_writer = BonVerkaeufeCheckWriter()

    def generate(self):

        self.logger.info(
            "Starte Generator: Bon-Verkaeufe"
        )

        export_start = datetime.now()

        store_id = "001"

        sales_date = export_start.strftime(
            "%Y-%m-%d"
        )

        export_timestamp = export_start

        self.sequence.initialize_store(
            store_id,
            97000001
        )

        sales_records = []

        first_sequence_id = None
        last_sequence_id = None

        #
        # Anzahl der zu erzeugenden Bons
        #

        number_of_receipts = 150

        #
        # Start-Bonnummer
        #

        receipt_number = 1000

        for _ in range(number_of_receipts):

            current_receipt = receipt_number

            receipt_number += 1

            #
            # 1 bis 20 Positionen pro Bon
            #

            number_of_positions = randint(
                1,
                20
            )

            cash_register = randint(
                1,
                12
            )

            sales_time = (
                f"{randint(8,21):02d}:"
                f"{randint(0,59):02d}:"
                f"{randint(0,59):02d}"
            )

            for position in range(
                1,
                number_of_positions + 1
            ):

                sequence_id = (
                    self.sequence.get_next_id(
                        store_id
                    )
                )

                if first_sequence_id is None:
                    first_sequence_id = sequence_id

                last_sequence_id = sequence_id

                quantity = randint(
                    1,
                    5
                )

                sales_price = round(
                    uniform(
                        0.49,
                        149.99
                    ),
                    2
                )

                sales_value = round(
                    quantity
                    * sales_price,
                    2
                )

                record = {

                    "bon_sequence_id":
                        sequence_id,

                    "bon_nummer":
                        current_receipt,

                    "filial_nummer":
                        store_id,

                    "verkaufsdatum":
                        sales_date,

                    "verkaufszeit":
                        sales_time,

                    "kasse_nummer":
                        cash_register,

                    "position_nummer":
                        position,

                    "artikel_nummer":
                        str(
                            randint(
                                100000,
                                199999
                            )
                        ),

                    "verkaufsmenge":
                        quantity,

                    "verkaufspreis":
                        sales_price,

                    "verkaufswert":
                        sales_value

                }

                sales_records.append(
                    record
                )

        sales_filename = (
            self.writer.write_sales_file(

                store_id=store_id,

                export_timestamp=export_timestamp,

                sales_records=sales_records

            )
        )

        export_end = datetime.now()

        self.check_writer.write_check_file(

            store_id=store_id,

            export_timestamp=export_timestamp,

            sales_date=sales_date,

            first_sequence_id=first_sequence_id,

            last_sequence_id=last_sequence_id,

            receipt_count=number_of_receipts,

            record_count=len(
                sales_records
            ),

            export_start=export_start,

            export_end=export_end,

            sales_filename=sales_filename

        )

        self.logger.info(
            f"{number_of_receipts} Bons erzeugt."
        )

        self.logger.info(
            f"{len(sales_records)} "
            "Bonpositionen erzeugt."
        )

        self.logger.info(
            "Generator Bon-Verkaeufe beendet."
        )
