#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : regalplaetze.py
Version : 2.1.0

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

import json
import yaml

from generator.base import BaseGenerator
from generator.infrastruktur.csv_writer import CSVWriter
from datetime import datetime


class RegalplaetzeGenerator(BaseGenerator):

    def __init__(self, config, logger):

        super().__init__(config, logger)

        _timestamp = datetime.now().strftime(
             "%Y-%m-%d_%H-%M-%S"
        )


        self.writer = CSVWriter(
            f"output/stammdaten/regalplaetze_{_timestamp}.csv"
        )

    def generate(self):

        with open(
            "config/regale.yaml",
            "r",
            encoding="utf-8"
        ) as file:

            regale = yaml.safe_load(file)["regale"]

        with open(
            "config/regalplaetze.yaml",
            "r",
            encoding="utf-8"
        ) as file:

            regaltypen = yaml.safe_load(file)["regaltypen"]

        rows = []

        regalplatz_id = 1

        for regal in regale:

            typ = regal["typ"]

            ebenen = regaltypen[typ]["ebenen"]

            for meter in range(
                regal["meter_von"],
                regal["meter_bis"] + 1
            ):

                for ebene in ebenen:

                    regalplatz_code = (
                        f'{regal["code"]}'
                        f'-M{meter:03d}'
                        f'-E{ebene["nummer"]}'
                    )

                    eigenschaften = {

                        "regaltyp": typ,

                        "ebene_name": ebene["name"],

                        "temperaturzone":
                            regal["temperatur"]

                    }

                    rows.append(

                        [

                            regalplatz_id,

                            regalplatz_code,

                            regal["code"],

                            regal["gang"],

                            regal["seite"],

                            meter,

                            ebene["nummer"],

                            json.dumps(
                                eigenschaften,
                                ensure_ascii=False
                            ),

                            True

                        ]

                    )

                    regalplatz_id += 1

        self.writer.write(

            [

                "regalplatz_id",

                "regalplatz_code",

                "regal_code",

                "gang",

                "seite",

                "regalmeter",

                "regalebene",

                "eigenschaften",

                "aktiv"

            ],

            rows

        )

        self.logger.info(

            "%d Regalplätze erzeugt.",

            len(rows)

        )
