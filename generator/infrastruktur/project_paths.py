#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : project_paths.py
Version : 2.0.1

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

from pathlib import Path


class ProjectPaths:
    """Verwaltet alle Projektpfade."""

    ROOT = Path(__file__).resolve().parent.parent.parent

    CONFIG = ROOT / "config"
    OUTPUT = ROOT / "output"
    LOGS = ROOT / "logs"
    DOCS = ROOT / "docs"
    TESTS = ROOT / "tests"

    STAMMDATEN = OUTPUT / "stammdaten"
    BEWEGUNGSDATEN = OUTPUT / "bewegungsdaten"
