from generator.context import DataContext

from generator.masterdata.warengruppen import WarengruppenGenerator
from generator.masterdata.hersteller import HerstellerGenerator
from generator.masterdata.lieferanten import LieferantenGenerator
from generator.masterdata.kunden import KundenGenerator
from generator.masterdata.artikel import ArtikelGenerator
from generator.masterdata.marken import MarkenGenerator
from generator.masterdata.lager import LagerGenerator
from generator.masterdata.mitarbeiter import MitarbeiterGenerator
from generator.masterdata.filialen import FilialenGenerator
from generator.masterdata.kostenstellen import KostenstellenGenerator
from generator.masterdata.kostenarten import KostenartenGenerator
from generator.masterdata.organisation import OrganisationGenerator
from generator.masterdata.saisonkalender import SaisonkalenderGenerator
from generator.masterdata.regale import RegaleGenerator
from generator.masterdata.regalplaetze import RegalplaetzeGenerator


class GeneratorManager:

    def __init__(self, config, logger):

        self.config = config
        self.logger = logger
        self.context = DataContext()

    # -----------------------------------------------------------------

    def _create_generators(self):

        return [

            WarengruppenGenerator(
                self.config,
                self.logger
            ),

            HerstellerGenerator(
                self.config,
                self.logger
            ),

            LieferantenGenerator(
                self.config,
                self.logger
            ),

            KundenGenerator(
                self.config,
                self.logger
            ),

            MarkenGenerator(
                self.config,
                self.logger
            ),

            ArtikelGenerator(
                self.config,
                self.logger
            ),

            OrganisationGenerator(
                self.config,
                self.logger
            ),

            SaisonkalenderGenerator(
                self.config,
                self.logger
            ),

            RegaleGenerator(
                self.config,
                self.logger
            ),

            RegalplaetzeGenerator(
                self.config,
                self.logger
            ),

            KostenstellenGenerator(
                self.config,
                self.logger
            ),

            KostenartenGenerator(
                self.config,
                self.logger
            )

        ]

    # -----------------------------------------------------------------

    def _sort_generators(self, generators):
        """
        Sortiert Generatoren anhand ihrer depends_on-Definition.

        Für Generatoren ohne Abhängigkeiten bleibt die ursprüngliche
        Reihenfolge erhalten.
        """

        result = []
        completed = set()

        remaining = list(generators)

        while remaining:

            progress = False

            for generator in remaining[:]:

                deps = getattr(generator, "depends_on", [])

                if all(dep in completed for dep in deps):

                    result.append(generator)
                    completed.add(generator.__class__.__name__)

                    remaining.remove(generator)
                    progress = True

            if not progress:
                raise RuntimeError(
                    "Zyklische oder nicht erfüllbare Generator-Abhängigkeit gefunden."
                )

        return result

    # -----------------------------------------------------------------

    def run(self):

        generators = self._create_generators()
        generators = self._sort_generators(generators)

        self.logger.info("")
        self.logger.info("=== RetailDWGen V1.7 gestartet ===")
        self.logger.info("")

        for generator in generators:

            generator.context = self.context

            self.logger.info("----------------------------------------")
            self.logger.info(
                "Starte %s",
                generator.__class__.__name__
            )

            try:

                if hasattr(generator, "run"):
                    generator.run()
                else:
                    generator.generate()

            except Exception:

                self.logger.exception(
                    "%s wurde mit einem Fehler beendet.",
                    generator.__class__.__name__
                )
                raise

            self.logger.info(
                "%s erfolgreich beendet.",
                generator.__class__.__name__
            )

        self.logger.info("")
        self.logger.info("=== Alle Generatoren erfolgreich beendet ===")
        self.logger.info("")
