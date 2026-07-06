from pathlib import Path

from generator.infrastructure.config import Config
from generator.infrastructure.logger import setup_logger
from generator.manager import GeneratorManager


def read_version():

    return Path("VERSION").read_text(
        encoding="utf-8"
    ).strip()


def main():

    config = Config()

    logger = setup_logger()

    print()

    print("=" * 60)
    print(config.get("project", "name"))
    print("Version", read_version())
    print("=" * 60)

    manager = GeneratorManager(
        config,
        logger
    )

    manager.run()

    print()
    print("RetailDWGen erfolgreich beendet.")
    print()


if __name__ == "__main__":

    main()
