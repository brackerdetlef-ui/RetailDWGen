#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : verloren_vernichtet_generator.py
Version : 2.0.1

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

"""
Generator fuer Verlust- und Vernichtungsdaten.

Erzeugt Testdaten fuer verlorene bzw.
vernichtete Artikel.
"""

from datetime import datetime
from random import randint, uniform, choice

from generator.transaktionen.verloren_vernichtet.verloren_vernichtet_sequence import (
    VerlorenVernichtetSequence
)
from generator.transaktionen.verloren_vernichtet.verloren_vernichtet_writer import (
    VerlorenVernichtetWriter
)
from generator.transaktionen.verloren_vernichtet.verloren_vernichtet_check_writer import (
    VerlorenVernichtetCheckWriter
)


class VerlorenVernichtetGenerator:
    """
    Generator fuer Verlust- und Vernichtungsdaten.
    """

    def __init__(
        self,
        config,
        logger
    ):
        self.config = config
        self.logger = logger

        self.sequence = VerlorenVernichtetSequence()
        self.writer = VerlorenVernichtetWriter()
        self.check_writer = VerlorenVernichtetCheckWriter()

    def generate(self):
        """
        Einstiegspunkt.
        """

        self.logger.info(
            "Starte Generator: Verloren/Vernichtet"
        )

        export_start = datetime.now()

        store_id = "001"

        #
        # Vernichtungslager
        #
        warehouse_id = "129"

        loss_date = export_start.strftime(
            "%Y-%m-%d"
        )

        export_timestamp = export_start

        #
        # Sequenz initialisieren
        #

        try:

            self.sequence.initialize_store(
                store_id,
                65000001
            )

        except Exception:
            pass

        #
        # Moegliche Verlustgruende
        #

        loss_reasons = [

            "VERDORBEN",

            "BESCHAEDIGT",

            "DIEBSTAHL",

            "SCHWUND",

            "INVENTURDIFFERENZ",

            "RUECKRUF",

            "SONSTIGES"

        ]

        #
        # Anzahl Testdatensaetze
        #

        number_of_records = 75

        loss_records = []

        first_loss_id = None
        last_loss_id = None

        for _ in range(number_of_records):

            loss_id = self.sequence.get_next_id(
                store_id
            )

            if first_loss_id is None:
                first_loss_id = loss_id

            last_loss_id = loss_id

            quantity = randint(
                1,
                10
            )

            purchase_price = round(
                uniform(
                    0.49,
                    99.99
                ),
                2
            )

            record = {

                "verlust_id": loss_id,

                "filial_nummer": store_id,

                "lager_nummer": warehouse_id,

                "verlustdatum": loss_date,

                "artikel_nummer": str(
                    randint(
                        100000,
                        199999
                    )
                ),

                "verlustmenge": quantity,

                "einkaufspreis": purchase_price,

                "verlustwert": round(
                    quantity * purchase_price,
                    2
                ),

                "verlustgrund": choice(
                    loss_reasons
                )

            }

            loss_records.append(
                record
            )

        #
        # Verlustdatei schreiben
        #

        loss_filename = self.writer.write_loss_file(
            store_id=store_id,
            export_timestamp=export_timestamp,
            loss_records=loss_records
        )

        export_end = datetime.now()

        #
        # Checkdatei schreiben
        #

        self.check_writer.write_check_file(

            store_id=store_id,

            export_timestamp=export_timestamp,

            loss_date=loss_date,

            first_loss_id=first_loss_id,

            last_loss_id=last_loss_id,

            record_count=len(
                loss_records
            ),

            export_start=export_start,

            export_end=export_end,

            loss_filename=loss_filename

        )

        self.logger.info(
            f"{len(loss_records)} Verlustdatensaetze erzeugt."
        )

        self.logger.info(
            "Generator Verloren/Vernichtet beendet."
        )
