from generator.config import Config
from generator.logger import setup_logger
from generator.manager import GeneratorManager


def main():

    config = Config()

    logger = setup_logger()

    print("=" * 50)
    print(config.get("project", "name"))
    print("Version", config.get("project", "version"))
    print("=" * 50)

    manager = GeneratorManager(
        config,
        logger
    )

    manager.run()

    print("Fertig.")


if __name__ == "__main__":
   main()
