"""
RetailDWGen
Generator Registry

Version 1.7
"""

from __future__ import annotations

from typing import Dict
from typing import List
from typing import Type

# ----------------------------------------------------------------------
# Zentrale Registry
# ----------------------------------------------------------------------

_GENERATORS: Dict[str, Type] = {}


# ----------------------------------------------------------------------
# Registrierung
# ----------------------------------------------------------------------

def register_generator(cls):
    """
    Registriert einen Generator.

    Verwendung:

        @register_generator
        class ArtikelGenerator(BaseGenerator):
            ...
    """

    _GENERATORS[cls.__name__] = cls
    return cls


# ----------------------------------------------------------------------
# Zugriff
# ----------------------------------------------------------------------

def registered_generators() -> List[Type]:
    """
    Liefert alle registrierten Generator-Klassen.
    """

    return list(_GENERATORS.values())


def create_generators(config, logger):
    """
    Erzeugt Generator-Instanzen.
    """

    return [
        generator(config, logger)
        for generator in registered_generators()
    ]


# ----------------------------------------------------------------------
# Sortierung nach Abhängigkeiten
# ----------------------------------------------------------------------

def sort_generators(generators):
    """
    Sortiert Generatoren anhand ihrer depends_on-Liste.

    Beispiel:

        depends_on = [
            "HerstellerGenerator",
            "MarkenGenerator"
        ]
    """

    result = []
    finished = set()

    remaining = list(generators)

    while remaining:

        progress = False

        for generator in remaining[:]:

            deps = getattr(generator, "depends_on", [])

            if all(dep in finished for dep in deps):

                result.append(generator)
                finished.add(generator.__class__.__name__)

                remaining.remove(generator)
                progress = True

        if not progress:

            unresolved = []

            for generator in remaining:

                unresolved.append(
                    f"{generator.__class__.__name__}: "
                    f"{getattr(generator, 'depends_on', [])}"
                )

            raise RuntimeError(
                "Nicht auflösbare Generator-Abhängigkeiten:\n"
                + "\n".join(unresolved)
            )

    return result


# ----------------------------------------------------------------------
# Hilfsfunktionen
# ----------------------------------------------------------------------

def clear_registry():
    """
    Nur für Tests.
    """

    _GENERATORS.clear()


def generator_names():
    """
    Liefert die Namen aller registrierten Generatoren.
    """

    return sorted(_GENERATORS.keys())
