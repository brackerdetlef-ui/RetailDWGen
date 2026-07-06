from generator.masterdata.warengruppen import WarengruppenGenerator
from generator.masterdata.hersteller import HerstellerGenerator
from generator.masterdata.lieferanten import LieferantenGenerator
from generator.infrastructure.project_paths import ProjectPaths


class GeneratorManager:

    def __init__(self, config, logger):

        self.config = config
        self.logger = logger

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
            )

        ]

        for generator in generatoren:

            self.logger.info(
                "Starte %s",
                generator.__class__.__name__
            )

            generator.generate()

            self.logger.info(
                "%s beendet",
                generator.__class__.__name__
            )
