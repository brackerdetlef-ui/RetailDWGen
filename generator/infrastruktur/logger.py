#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : logger.py
Version : 2.0.1

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

import logging
from pathlib import Path


def setup_logger():

    Path("logs").mkdir(exist_ok=True)

    logging.basicConfig(
        filename="logs/retaildwgen.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s"
    )

    return logging.getLogger("RetailDWGen")
