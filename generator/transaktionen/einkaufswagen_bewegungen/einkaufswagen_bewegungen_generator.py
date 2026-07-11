#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : einkaufswagen_bewegungen_generator.py
Version : 2.0.1

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

"""
Generator fuer Einkaufswagen-Bewegungen.

Erzeugt Testdaten fuer Einkaufswagen-
Bewegungsimporte.
"""

from datetime import datetime, timedelta
from random import randint, choice

from generator.transaktionen.einkaufswagen_bewegungen.einkaufswagen_bewegungen_sequence import (
    EinkaufswagenBewegungenSequence
)
from generator.transaktionen.einkaufswagen_bewegungen.einkaufswagen_bewegungen_writer import (
    EinkaufswagenBewegungenWriter
)
from generator.transaktionen.einkaufswagen_bewegungen.einkaufswagen_bewegungen_check_writer import (
    EinkaufswagenBewegungenCheckWriter
)


class EinkaufswagenBewegungenGenerator:
    """
    Generator fuer Einkaufswagen-Bewegungen.
    """

    def __init__(
        self,
        config,
        logger
    ):
        self.config = config
        self.logger = logger

        self.sequence = (
            EinkaufswagenBewegungenSequence()
        )

        self.writer = (
            EinkaufswagenBewegungenWriter()
        )

        self.check_writer = (
            EinkaufswagenBewegungenCheckWriter()
        )

    def generate(self):
        """
        Einstiegspunkt.
        """

        self.logger.info(
            "Starte Generator: Einkaufswagen-Bewegungen"
        )

        export_start = datetime.now()

        store_id = "001"

        movement_date = export_start.strftime(
            "%Y-%m-%d"
        )

        export_timestamp = export_start

        #
        # Sequenz initialisieren
        #

        try:
            self.sequence.initialize_store(
                store_id,
                90000001
            )
        except Exception:
            pass

        #
        # Anzahl Testdatensaetze
        #

        number_of_records = 500

        movement_records = []

        first_sequence_id = None
        last_sequence_id = None

        start_time = export_start

        for _ in range(number_of_records):

            sequence_id = (
                self.sequence.get_next_id(
                    store_id
                )
            )

            if first_sequence_id is None:
                first_sequence_id = sequence_id

            last_sequence_id = sequence_id

            einkaufswagen_id = randint(
                1,
                150
            )

            einkauf_id = (
                f"{movement_date.replace('-', '')}_"
                f"{einkaufswagen_id:04d}"
            )

            zeitpunkt = start_time.strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            start_time += timedelta(
                seconds=15
            )

            record = {

                "sequence_id": sequence_id,

                "filial_nummer": store_id,

                "einkaufswagen_id": (
                    einkaufswagen_id
                ),

                "einkauf_id": einkauf_id,

                "zeitpunkt": zeitpunkt,

                "gang_nummer": randint(
                    -9,
                    5
                ),

                "meter": round(
                    randint(0, 750) / 10,
                    1
                ),

                "seite": choice(
                    [
                        "links",
                        "mitte",
                        "rechts"
                    ]
                )

            }

            movement_records.append(
                record
            )

        #
        # Bewegungsdatei schreiben
        #

        movements_filepath = (
            self.writer.write_movements_file(

                store_id=store_id,

                export_timestamp=export_timestamp,

                movement_records=movement_records

            )
        )

        export_end = datetime.now()

        #
        # Checkdatei schreiben
        #

        self.check_writer.write_check_file(

            store_id=store_id,

            export_timestamp=export_timestamp,

            movement_date=movement_date,

            first_sequence_id=first_sequence_id,

            last_sequence_id=last_sequence_id,

            record_count=len(
                movement_records
            ),

            export_start=export_start,

            export_end=export_end,

            movements_filename=movements_filepath

        )

        self.logger.info(
            f"{len(movement_records)} "
            "Einkaufswagen-Bewegungen erzeugt."
        )

        self.logger.info(
            "Generator Einkaufswagen-Bewegungen beendet."
        )
