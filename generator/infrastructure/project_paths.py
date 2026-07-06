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
