from generator.warengruppen import WarengruppenGenerator


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
