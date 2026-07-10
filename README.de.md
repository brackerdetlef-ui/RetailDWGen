# RetailDWGen

🇩🇪 **Deutsch** | 🇬🇧 [English](README.md) | 🇪🇸 [Español](README.es.md) | 🇫🇷 [Français](README.fr.md)

---

## Realistische Testdaten für Handel, Data Warehouse und Business Intelligence

RetailDWGen ist ein Python-basierter Generator für realistische Testdaten eines Handelsunternehmens.

Das Projekt erzeugt strukturierte CSV-Dateien, die sich für Softwaretests, Schulungen, Demonstrationen sowie den Aufbau und die Validierung von Data-Warehouse-Systemen (DWH), Business-Intelligence-Lösungen und analytischen Anwendungen eignen.

Die erzeugten Daten orientieren sich an typischen Prozessen eines Handelsunternehmens und können in beliebige Datenbanksysteme importiert und dort weiterverarbeitet werden.

---

# Version 2.0

Mit Version **2.0** wurde RetailDWGen zu einer umfassenden Plattform zur Erzeugung realistischer Handelsdaten erweitert.

Neben klassischen Stammdaten werden nun auch Bewegungs-, Bestands- und technische Kontrollinformationen erzeugt. Dadurch eignet sich RetailDWGen insbesondere für Data-Warehouse-Projekte, ETL-Prozesse, Softwaretests sowie analytische Anwendungen.

Die in Version 2.0 erzeugten Daten dienen bewusst dem Aufbau einer vollständigen Datenlandschaft. Fachliche Zusammenhänge zwischen den einzelnen Datenarten werden in den folgenden Versionen schrittweise weiterentwickelt.

---

# Merkmale

* Erzeugung realistischer Stammdaten
* Erzeugung realistischer Bewegungsdaten
* Erzeugung von Bestandsdaten
* Erzeugung technischer Kontroll-Dateien
* Fortlaufende technische Sequenznummern
* Reproduzierbare Datensätze durch konfigurierbaren Zufalls-Seed
* CSV-Ausgabe im UTF-8-Format mit Semikolon als Trennzeichen
* Modulare Generatorarchitektur
* Einheitlicher Aufbau aller Generatoren
* Entwickelt mit Python 3.10

---

# Unterstützte Datenbereiche

## Stammdaten

* Warengruppen
* Artikel
* Hersteller
* Lieferanten
* Kunden
* Filialen
* Lager
* Mitarbeiter
* Kassen
* Einkaufswagen
* weitere Stammdaten

---

## Bewegungsdaten

* Verkäufe
* Wareneingänge
* Kunden-Retouren
* Verloren / Vernichtet
* Bon-Verkäufe
* Einkaufswagen-Bewegungen

---

## Bestandsdaten

* Lagerbestände
* Inventuren

---

## Technische Komponenten

Jeder Generator erzeugt nach einem einheitlichen Schema:

* CSV-Datendatei
* technische Kontroll-Datei (Check-Datei)
* fortlaufende technische Sequenznummern

---

# Einsatzgebiete

RetailDWGen eignet sich unter anderem für

* Data-Warehouse-Projekte
* Business Intelligence
* ETL-Entwicklung
* Softwaretests
* Performancetests
* Datenmigrationen
* Demonstrationen
* Schulungen
* Prototypen
* analytische Anwendungen

---

# Voraussetzungen

* Python 3.10
* Virtuelle Python-Umgebung (empfohlen)

---

# Installation

Repository klonen

```bash
git clone <repository-url>
cd RetailDWGen
```

Virtuelle Umgebung erstellen

```bash
python3 -m venv .venv
```

Virtuelle Umgebung aktivieren

```bash
source .venv/bin/activate
```

Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

---

# Verwendung

Datengenerierung starten

```bash
python generate.py
```

Die erzeugten CSV-Dateien werden im Verzeichnis

```text
output/
```

abgelegt.

---

# Projektstruktur

```text
RetailDWGen/
│
├── config/
├── generator/
│   ├── infrastruktur/
│   ├── stammdaten/
│   ├── transaktionen/
│   └── bestaende/
│
├── konfiguration/
├── output/
├── generate.py
├── requirements.txt
├── VERSION
├── LICENSE
├── README.md
├── README.de.md
├── README.es.md
└── README.fr.md
```

---

# Konfiguration

Die Anzahl der zu erzeugenden Datensätze sowie weitere Einstellungen werden zentral über Konfigurationsdateien gesteuert.

---

# Roadmap

## Version 2.x

* Ausbau weiterer Datenbereiche
* Verbesserung der fachlichen Konsistenz
* Erweiterung der Lager- und Bestandslogik
* Ausbau weiterer Simulationsdaten

## Version 3.x

* Fachliche Verknüpfung aller Datenbereiche
* Konsistente Warenwirtschaftssimulation
* Erweiterte Einkaufswagen-Simulation
* Konsistente Bon- und Verkaufsdaten
* Realistische Lagerbestände

## Langfristige Ziele

RetailDWGen soll zu einer umfassenden Simulationsplattform für Handelsunternehmen ausgebaut werden.

Geplant sind unter anderem:

* vollständige Data-Warehouse-Testdaten
* Simulation kompletter Handelsprozesse
* Einkaufswagen-Bewegungsanalysen
* Regal- und Filialsimulationen
* Unterstützung analytischer KI-Verfahren
* Visualisierung von Kundenbewegungen innerhalb einer Filiale

---

# Autor

**Detlef Bracker**

RetailDWGen ist ein Open-Source-Projekt von Detlef Bracker zur Demonstration moderner Softwareentwicklung, Datenmodellierung sowie Data-Warehouse-Architekturen im Handelsumfeld.

---

# Feedback und Diskussion

Fragen, Anregungen, Verbesserungsvorschläge und fachliche Diskussionen sind jederzeit willkommen.

Nutzen Sie hierfür gerne die **GitHub Discussions** oder erstellen Sie ein **Issue**, wenn Sie einen Fehler gefunden haben oder einen Verbesserungsvorschlag einbringen möchten.

Ich freue mich über jeden fachlichen Austausch und jedes Feedback zur Weiterentwicklung von RetailDWGen.

---

# Lizenz

Dieses Projekt steht unter der MIT License.

Copyright © Detlef Bracker

Weitere Informationen befinden sich in der Datei `LICENSE`.

