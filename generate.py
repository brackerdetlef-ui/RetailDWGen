from generator.config import Config
from generator.logger import setup_logger
from generator.warengruppen import WarengruppenGenerator


def main():

    config = Config()

    logger = setup_logger()

    logger.info("RetailDWGen gestartet.")

    print("=" * 50)
    print(config.get("project", "name"))
    print("Version", config.get("project", "version"))
    print("=" * 50)

    generator = WarengruppenGenerator(
        config,
        logger
    )

    generator.generate()

    print("Warengruppen erfolgreich erzeugt.")


if __name__ == "__main__":
    main()
