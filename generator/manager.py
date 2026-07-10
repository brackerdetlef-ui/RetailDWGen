from generator.context import DataContext

from generator.stammdaten.warengruppen import WarengruppenGenerator
from generator.stammdaten.hersteller import HerstellerGenerator
from generator.stammdaten.lieferanten import LieferantenGenerator
from generator.stammdaten.kunden import KundenGenerator
from generator.stammdaten.artikel import ArtikelGenerator
from generator.stammdaten.marken import MarkenGenerator
from generator.stammdaten.lager import LagerGenerator
from generator.stammdaten.mitarbeiter import MitarbeiterGenerator
from generator.stammdaten.filialen import FilialenGenerator
from generator.stammdaten.kostenstellen import KostenstellenGenerator
from generator.stammdaten.kostenarten import KostenartenGenerator
from generator.stammdaten.organisation import OrganisationGenerator
from generator.stammdaten.saisonkalender import SaisonkalenderGenerator
from generator.stammdaten.regale import RegaleGenerator
from generator.stammdaten.regalplaetze import RegalplaetzeGenerator
from generator.transaktionen.verkaeufe.verkaeufe_sequence import VerkaeufeSequence
from generator.transaktionen.verkaeufe.verkaeufe_writer import VerkaeufeWriter
from generator.transaktionen.verkaeufe.verkaeufe_check_writer import VerkaeufeCheckWriter
from generator.transaktionen.verkaeufe.verkaeufe_generator import VerkaeufeGenerator
from generator.transaktionen.wareneingaenge.wareneingaenge_sequence import WareneingaengeSequence
from generator.transaktionen.wareneingaenge.wareneingaenge_writer import WareneingaengeWriter
from generator.transaktionen.wareneingaenge.wareneingaenge_check_writer import WareneingaengeCheckWriter
from generator.transaktionen.wareneingaenge.wareneingaenge_generator import WareneingaengeGenerator
from generator.transaktionen.kunden_retouren.kunden_retouren_sequence import KundenRetourenSequence
from generator.transaktionen.kunden_retouren.kunden_retouren_writer import KundenRetourenWriter
from generator.transaktionen.kunden_retouren.kunden_retouren_check_writer import KundenRetourenCheckWriter
from generator.transaktionen.kunden_retouren.kunden_retouren_generator import KundenRetourenGenerator
from generator.transaktionen.verloren_vernichtet.verloren_vernichtet_sequence import VerlorenVernichtetSequence
from generator.transaktionen.verloren_vernichtet.verloren_vernichtet_writer import VerlorenVernichtetWriter
from generator.transaktionen.verloren_vernichtet.verloren_vernichtet_check_writer import VerlorenVernichtetCheckWriter
from generator.transaktionen.verloren_vernichtet.verloren_vernichtet_generator import VerlorenVernichtetGenerator
from generator.transaktionen.einkaufswagen_bewegungen.einkaufswagen_bewegungen_sequence import EinkaufswagenBewegungenSequence
from generator.transaktionen.einkaufswagen_bewegungen.einkaufswagen_bewegungen_writer import EinkaufswagenBewegungenWriter
from generator.transaktionen.einkaufswagen_bewegungen.einkaufswagen_bewegungen_check_writer import EinkaufswagenBewegungenCheckWriter
from generator.transaktionen.einkaufswagen_bewegungen.einkaufswagen_bewegungen_generator import EinkaufswagenBewegungenGenerator
from generator.bestaende.bestaende_sequence import BestaendeSequence
from generator.bestaende.bestaende_writer import BestaendeWriter
from generator.bestaende.bestaende_check_writer import BestaendeCheckWriter
from generator.bestaende.bestaende_generator import BestaendeGenerator
from generator.inventuren.inventuren_sequence import InventurenSequence
from generator.inventuren.inventuren_writer import InventurenWriter
from generator.inventuren.inventuren_check_writer import InventurenCheckWriter
from generator.inventuren.inventuren_generator import InventurenGenerator






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
            ),

            VerkaeufeGenerator(
                self.config,
                self.logger
            ),

            WareneingaengeGenerator(
                self.config,
                self.logger
            ),

            KundenRetourenGenerator(
                self.config,
                self.logger
            ),

            VerlorenVernichtetGenerator(
                self.config,
                self.logger
            ),

            BestaendeGenerator(
                self.config,
                self.logger
            ),
 
            InventurenGenerator(
                self.config,
                self.logger
            ),

            EinkaufswagenBewegungenGenerator(
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
