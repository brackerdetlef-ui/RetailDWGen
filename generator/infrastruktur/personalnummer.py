#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : personalnummer.py
Version : 2.0.1

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

class PersonalnummerGenerator:

    def __init__(self, start=1000, increment=10):

        self.nummer = start
        self.increment = increment

    def _pruefziffer(self, code):

        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        wert = 0

        for zeichen in code:

            if zeichen.isdigit():

                wert += int(zeichen)

            else:

                wert += ord(zeichen.upper()) - ord("A") + 1

        return alphabet[wert % 36]

    def generate(self, vorname, nachname):

        erster = (
            nachname[0]
            if nachname
            else "X"
        ).upper()

        zweiter = (
            vorname[0]
            if vorname
            else "X"
        ).upper()

        basis = (
            f"{erster}"
            f"{zweiter}"
            f"{self.nummer:04d}"
        )

        pruefziffer = self._pruefziffer(
            basis
        )

        personalnummer = (
            basis +
            pruefziffer
        )

        self.nummer += self.increment

        return personalnummer
