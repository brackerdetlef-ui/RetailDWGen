# RetailDWGen

🇩🇪 [Deutsch](README.de.md) | 🇬🇧 [English](README.md) | 🇪🇸 [Español](README.es.md) | 🇫🇷 **Français**

---

## Génération de données de test réalistes pour le commerce, les Data Warehouses et la Business Intelligence

RetailDWGen est un générateur de données de test réalistes pour le commerce de détail, développé en Python.

Le projet produit des fichiers CSV structurés destinés aux tests logiciels, à la formation, aux démonstrations ainsi qu'au développement et à la validation de solutions de Data Warehouse (DWH), de Business Intelligence (BI) et d'analyse de données.

Les jeux de données générés s'appuient sur les processus courants du commerce de détail et peuvent être importés dans pratiquement n'importe quel système de gestion de bases de données pour être exploités et analysés.

---

# Version 2.0

Avec la version **2.0**, RetailDWGen devient une plateforme complète de génération de données réalistes pour le commerce.

En plus des données de référence, le projet génère désormais des données transactionnelles, des données de stock et des fichiers techniques de contrôle. RetailDWGen convient ainsi parfaitement aux projets de Data Warehouse, aux développements ETL, aux tests logiciels, aux analyses de données et aux démonstrations.

Les données produites dans la version 2.0 ont pour objectif de constituer une base complète de données commerciales. Les relations fonctionnelles entre les différents domaines de données seront progressivement enrichies dans les versions futures.

---

# Fonctionnalités

* Génération de données de référence réalistes
* Génération de données transactionnelles
* Génération de données de stock
* Génération de fichiers techniques de contrôle
* Numéros de séquence techniques continus
* Jeux de données reproductibles grâce à une graine aléatoire configurable
* Fichiers CSV encodés en UTF-8 avec point-virgule comme séparateur
* Architecture modulaire des générateurs
* Structure homogène pour tous les générateurs
* Développé avec Python 3.10

---

# Domaines de données pris en charge

## Données de référence

* Familles de produits
* Articles
* Fabricants
* Fournisseurs
* Clients
* Magasins
* Entrepôts
* Employés
* Caisses
* Chariots de courses
* Autres données de référence

---

## Données transactionnelles

* Ventes
* Réceptions de marchandises
* Retours clients
* Produits perdus ou détruits
* Ventes par ticket de caisse
* Déplacements des chariots de courses

---

## Données de stock

* Stocks d'entrepôt
* Inventaires

---

## Composants techniques

Chaque générateur suit une structure identique et produit :

* un fichier CSV de données
* un fichier technique de contrôle (Check)
* des numéros de séquence techniques continus

---

# Cas d'utilisation

RetailDWGen est particulièrement adapté à :

* projets Data Warehouse
* Business Intelligence
* développement ETL
* tests logiciels
* tests de performance
* migration de données
* démonstrations
* formations
* prototypage
* applications analytiques

---

# Prérequis

* Python 3.10
* Environnement virtuel Python (recommandé)

---

# Installation

Cloner le dépôt

```bash
git clone <repository-url>
cd RetailDWGen
```

Créer un environnement virtuel

```bash
python3 -m venv .venv
```

Activer l'environnement virtuel

```bash
source .venv/bin/activate
```

Installer les dépendances

```bash
pip install -r requirements.txt
```

---

# Utilisation

Lancer la génération des données

```bash
python generate.py
```

Les fichiers CSV générés sont enregistrés dans le répertoire :

```text
output/
```

---

# Structure du projet

```text
RetailDWGen/
│
├── config/
├── generator/
│   ├── infrastructure/
│   ├── master_data/
│   ├── transactions/
│   └── inventory/
│
├── configuration/
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

# Configuration

Le nombre d'enregistrements générés ainsi que les autres paramètres sont définis de manière centralisée dans les fichiers de configuration.

---

# Feuille de route

## Version 2.x

* Extension des domaines de données
* Amélioration de la cohérence fonctionnelle
* Enrichissement de la logique des entrepôts et des stocks
* Nouveaux scénarios de simulation

## Version 3.x

* Intégration fonctionnelle entre tous les domaines de données
* Simulation complète des processus du commerce
* Simulation avancée des déplacements des chariots
* Cohérence entre tickets de caisse et ventes
* Gestion réaliste des stocks

## Vision à long terme

RetailDWGen a pour ambition de devenir une plateforme complète de simulation pour le commerce de détail.

Les évolutions prévues comprennent notamment :

* jeux de données complets pour les Data Warehouses
* simulation de l'ensemble des processus commerciaux
* analyse des déplacements des chariots de courses
* simulation des magasins et des rayons
* jeux de données adaptés à l'intelligence artificielle
* visualisation des parcours clients à l'intérieur des magasins

---

# Auteur

**Detlef Bracker**

RetailDWGen est un projet open source développé par Detlef Bracker afin de démontrer des techniques modernes de développement logiciel, de modélisation des données et d'architectures Data Warehouse appliquées au commerce de détail.

---

# Commentaires et discussions

Les questions, suggestions, idées et discussions techniques sont les bienvenues.

N'hésitez pas à utiliser **GitHub Discussions** pour les échanges généraux ou à créer une **Issue** si vous découvrez un problème ou souhaitez proposer une amélioration.

Toutes les contributions participent à l'amélioration continue de RetailDWGen.

---

# Licence

Ce projet est distribué sous licence MIT.

Copyright © Detlef Bracker

Pour plus d'informations, veuillez consulter le fichier `LICENSE`.

