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

        # Neu für Version 1.6
        self.context = DataContext()

    def run(self):

        generatoren = [

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

        for generator in generatoren:

            #
            # Vorbereitung auf Version 1.6
            #
            if hasattr(generator, "context"):
                generator.context = self.context

            self.logger.info(
                "Starte %s",
                generator.__class__.__name__
            )

            generator.generate()

            self.logger.info(
                "%s beendet",
                generator.__class__.__name__
            )
