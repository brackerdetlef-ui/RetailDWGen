#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : utils.py
Version : 2.0.1

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

import re
import unicodedata


def slugify(text: str) -> str:
    """
    Wandelt einen Text in einen URL-/E-Mail-tauglichen Slug um.
    """

    text = text.strip().lower()

    ersetzungen = {
        "ä": "ae",
        "ö": "oe",
        "ü": "ue",
        "ß": "ss"
    }

    for alt, neu in ersetzungen.items():
        text = text.replace(alt, neu)

    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")

    text = re.sub(r"&", " ", text)

    text = re.sub(r"[^a-z0-9]+", "-", text)

    text = text.strip("-")

    return text


def create_email(company: str) -> str:
    """
    Erzeugt eine E-Mail-Adresse aus dem Firmennamen.
    """

    return f"{slugify(company)}@example.com"


def create_website(company: str) -> str:
    """
    Erzeugt eine Webseite aus dem Firmennamen.
    """

    return f"www.{slugify(company)}.de"
