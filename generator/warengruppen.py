from generator.base import BaseGenerator
from generator.csv_writer import CSVWriter


class WarengruppenGenerator(BaseGenerator):

    def __init__(self, config, logger):

        super().__init__(config, logger)

        self.writer = CSVWriter(
            "output/stammdaten/warengruppen.csv"
        )

    def generate(self):

        warengruppen = [
            "Notebooks",
            "Desktop-PCs",
            "Monitore",
            "Drucker",
            "Scanner",
            "Tablets",
            "Smartphones",
            "Server",
            "NAS",
            "Router",
            "Switches",
            "Access Points",
            "USV",
            "SSD",
            "Festplatten",
            "RAM",
            "Grafikkarten",
            "Mainboards",
            "CPUs",
            "Netzteile",
            "Gehäuse",
            "Mäuse",
            "Tastaturen",
            "Headsets",
            "Lautsprecher",
            "Webcams",
            "Mikrofone",
            "Beamer",
            "Displays",
            "HDMI-Kabel",
            "USB-Kabel",
            "Adapter",
            "Dockingstations",
            "Druckerzubehör",
            "Papier",
            "Ordner",
            "Schreibwaren",
            "Bürostühle",
            "Schreibtische",
            "Aktenschränke",
            "Software",
            "Antivirus",
            "Backup",
            "Smart Home",
            "Überwachung",
            "Werkzeug",
            "Reinigung",
            "Verpackung",
            "Batterien",
            "Sonstiges"
        ]

        rows = []

        for nummer, name in enumerate(warengruppen, start=1):

            rows.append(
                [
                    nummer,
                    f"WG{nummer:03d}",
                    name,
                    "",
                    True
                ]
            )

        self.writer.write(
            [
                "wg_id",
                "wg_code",
                "bezeichnung",
                "parent_id",
                "aktiv"
            ],
            rows
        )

        self.logger.info(
            "%d Warengruppen erzeugt.",
            len(rows)
        )
