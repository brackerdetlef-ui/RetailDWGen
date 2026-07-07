# RetailDWGen

RetailDWGen ist ein Python-basierter Generator für realistische Testdaten eines Handelsunternehmens.

Das Projekt erzeugt strukturierte CSV-Dateien, die sich für Tests, Schulungen, Demonstrationen und die Entwicklung von Datenmodellen eignen. Die erzeugten Daten können in beliebige Datenbanksysteme importiert und dort weiterverarbeitet werden.

## Merkmale

* Erzeugung realistischer Stammdaten
* Reproduzierbare Datensätze durch konfigurierbaren Zufalls-Seed
* CSV-Ausgabe im UTF-8-Format mit Semikolon als Trennzeichen
* Konfigurierbare Anzahl der Datensätze
* Modulare Generatorarchitektur
* Entwickelt mit Python 3.10.12

## Aktuell unterstützte Stammdaten

* Warengruppen
* Hersteller
* Lieferanten
* Kunden

## Voraussetzungen

* Python 3.10.12
* Virtuelle Python-Umgebung (empfohlen)

## Installation

Repository klonen:

```bash
git clone <repository-url>
cd RetailDWGen
```

Virtuelle Umgebung erstellen:

```bash
python3 -m venv .venv
```

Virtuelle Umgebung aktivieren:

```bash
source .venv/bin/activate
```

Abhängigkeiten installieren:

```bash
pip install -r requirements.txt
```

## Verwendung

Datengenerierung starten:

```bash
python generate.py
```

Die erzeugten CSV-Dateien befinden sich anschließend im Verzeichnis:

```text
output/stammdaten/
```

## Projektstruktur

```text
RetailDWGen/
│
├── config/
├── generator/
│   ├── infrastructure/
│   └── masterdata/
├── output/
├── generate.py
├── requirements.txt
├── VERSION
└── README.md
```

## Konfiguration

Die Anzahl der zu erzeugenden Datensätze sowie weitere Einstellungen werden zentral über die Konfigurationsdateien gesteuert.

## Lizenz

Dieses Projekt steht unter der MIT License.

Weitere Informationen befinden sich in der Datei `LICENSE`.

