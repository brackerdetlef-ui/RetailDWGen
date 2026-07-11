#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : wareneingaenge_generator.py
Version : 2.0.1

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

"""
Generator fuer Wareneingaenge.

Erzeugt Testdaten fuer Wareneingangsimporte.
"""

from datetime import datetime
from random import randint, uniform

from generator.transaktionen.wareneingaenge.wareneingaenge_sequence import (
    WareneingaengeSequence
)
from generator.transaktionen.wareneingaenge.wareneingaenge_writer import (
    WareneingaengeWriter
)
from generator.transaktionen.wareneingaenge.wareneingaenge_check_writer import (
    WareneingaengeCheckWriter
)


class WareneingaengeGenerator:
    """
    Generator fuer Wareneingaenge.
    """

    def __init__(
        self,
        config,
        logger
    ):
        self.config = config
        self.logger = logger

        self.sequence = WareneingaengeSequence()
        self.writer = WareneingaengeWriter()
        self.check_writer = WareneingaengeCheckWriter()

    def generate(self):
        """
        Einstiegspunkt.
        """

        self.logger.info(
            "Starte Generator: Wareneingaenge"
        )

        export_start = datetime.now()

        store_id = "001"

        warehouse_id = "110"

        goods_receipt_date = export_start.strftime(
            "%Y-%m-%d"
        )

        export_timestamp = export_start

        #
        # Sequenz initialisieren
        #

        try:

            self.sequence.initialize_store(
                store_id,
                55000001
            )

        except Exception:
            pass

        #
        # Anzahl Testdatensaetze
        #

        number_of_records = 250

        goods_receipt_records = []

        first_goods_receipt_id = None
        last_goods_receipt_id = None

        for _ in range(number_of_records):

            goods_receipt_id = self.sequence.get_next_id(
                store_id
            )

            if first_goods_receipt_id is None:
                first_goods_receipt_id = goods_receipt_id

            last_goods_receipt_id = goods_receipt_id

            quantity = randint(
                1,
                48
            )

            purchase_price = round(
                uniform(
                    0.49,
                    99.99
                ),
                2
            )

            record = {

                "wareneingangs_id": goods_receipt_id,

                "filial_nummer": store_id,

                "lager_nummer": warehouse_id,

                "wareneingangsdatum": goods_receipt_date,

                "lieferant_nummer": str(
                    randint(
                        10000,
                        19999
                    )
                ),

                "artikel_nummer": str(
                    randint(
                        100000,
                        199999
                    )
                ),

                "eingangsmenge": quantity,

                "einkaufspreis": purchase_price,

                "wareneingangswert": round(
                    quantity * purchase_price,
                    2
                )

            }

            goods_receipt_records.append(
                record
            )

        #
        # Wareneingangsdatei schreiben
        #

        goods_receipt_filename = self.writer.write_goods_receipt_file(
            store_id=store_id,
            export_timestamp=export_timestamp,
            goods_receipt_records=goods_receipt_records
        )

        export_end = datetime.now()

        #
        # Checkdatei schreiben
        #

        self.check_writer.write_check_file(

            store_id=store_id,

            export_timestamp=export_timestamp,

            goods_receipt_date=goods_receipt_date,

            first_goods_receipt_id=first_goods_receipt_id,

            last_goods_receipt_id=last_goods_receipt_id,

            record_count=len(
                goods_receipt_records
            ),

            export_start=export_start,

            export_end=export_end,

            goods_receipt_filename=goods_receipt_filename

        )

        self.logger.info(
            f"{len(goods_receipt_records)} Wareneingaenge erzeugt."
        )

        self.logger.info(
            "Generator Wareneingaenge beendet."
        )
