# RetailDWGen

RetailDWGen est un projet Open Source développé en Python permettant de générer des données de test réalistes pour une entreprise du secteur du commerce.

Les fichiers CSV générés peuvent être importés dans pratiquement tout système de gestion de bases de données relationnelles, plateforme de données ou environnement d'analyse. L'objectif du projet est de fournir des jeux de données fiables et reproductibles pour le développement, la formation, les démonstrations et les tests de performance.

## Fonctionnalités

* Génération de données de référence réalistes pour une entreprise commerciale
* Export au format CSV encodé en UTF-8
* Fichiers séparés par un point-virgule (;)
* Nombre d'enregistrements configurable
* Génération reproductible grâce à une graine aléatoire configurable
* Architecture modulaire basée sur des générateurs
* Développé pour Python 3.10.12

## Générateurs actuellement disponibles

La version actuelle permet de générer :

* Groupes de produits
* Fabricants
* Fournisseurs
* Clients

## Prérequis

* Python 3.10.12
* pip
* Un environnement virtuel est recommandé

## Installation

Cloner le dépôt :

```bash
git clone <repository-url>
cd RetailDWGen
```

Créer un environnement virtuel :

```bash
python3 -m venv .venv
```

Activer l'environnement :

```bash
source .venv/bin/activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

## Utilisation

Lancer la génération des données :

```bash
python generate.py
```

Les fichiers CSV seront créés dans le répertoire :

```text
output/stammdaten/
```

## Configuration

Le nombre de données générées ainsi que les différents paramètres sont définis dans les fichiers de configuration situés dans le répertoire `config`.

## Structure du projet

```text
RetailDWGen/

config/
generator/
generator/masterdata/
generator/infrastructure/
output/

generate.py
requirements.txt
VERSION
README.md
```

## Principes du projet

RetailDWGen repose sur quelques principes simples :

* Un code clair et facile à comprendre
* Une architecture modulaire
* Une génération de données reproductible
* Une structure de projet bien organisée
* Une indépendance vis-à-vis du système de base de données

L'objectif principal est de produire des fichiers CSV réalistes pouvant être utilisés dans différents environnements de données, sans dépendre d'une technologie particulière.

## Licence

RetailDWGen est distribué sous licence MIT.

Consultez le fichier `LICENSE` pour plus d'informations.

