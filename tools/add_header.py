#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
Projekt : RetailDWGen
Datei   : add_header.py
Version : 2.0.1

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : Detlef Bracker
Lizenz  : MIT License
============================================================
"""

from pathlib import Path
import re

PROJECT = "RetailDWGen"
VERSION = "2.0.1"
AUTHOR = "Detlef Bracker"
LICENSE = "MIT License"

HEADER = """#!/usr/bin/env python3
# -*- coding: utf-8 -*-

\"\"\"
============================================================
Projekt : {project}
Datei   : {filename}
Version : {version}

Beschreibung:
TODO: Beschreibung ergänzen.

Autor   : {author}
Lizenz  : {license}
============================================================
\"\"\"

"""

SKIP_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".idea",
    ".vscode",
    "build",
    "dist",
}


def has_project_header(text: str) -> bool:
    """Prüft, ob bereits ein Projektheader vorhanden ist."""
    return (
        "Projekt :" in text[:800]
        or "RetailDWGen" in text[:800]
        or "RetailDWHPostgres" in text[:800]
    )


def strip_existing_header(text: str) -> str:
    """
    Entfernt Shebang, Encoding und ersten Modul-Docstring.
    Der eigentliche Python-Code bleibt erhalten.
    """

    text = re.sub(r"^#!/.*?\n", "", text)
    text = re.sub(r"^# -\*-[^\n]*-\*-\n", "", text)
    text = text.lstrip()

    if text.startswith('"""'):
        end = text.find('"""', 3)
        if end != -1:
            text = text[end + 3 :]

    return text.lstrip()


def process_file(file: Path):

    original = file.read_text(encoding="utf-8")

    if has_project_header(original):
        body = strip_existing_header(original)
    else:
        body = original

    header = HEADER.format(
        project=PROJECT,
        filename=file.name,
        version=VERSION,
        author=AUTHOR,
        license=LICENSE,
    )

    file.write_text(header + body, encoding="utf-8")

    print(f"[OK] {file}")


def main():

    root = Path.cwd()

    count = 0

    for pyfile in root.rglob("*.py"):

        if any(part in SKIP_DIRS for part in pyfile.parts):
            continue

        process_file(pyfile)
        count += 1

    print()
    print("=" * 60)
    print(f"{count} Python-Dateien aktualisiert.")
    print("=" * 60)


if __name__ == "__main__":
    main()
