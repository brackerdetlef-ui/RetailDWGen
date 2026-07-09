# RetailDWGen

RetailDWGen is an open-source Python project for generating realistic retail business data.

The generated CSV files can be imported into virtually any relational database, cloud data platform or analytics environment. The project focuses on providing realistic and reproducible test data for development, education, demonstrations and performance testing.

## Features

* Generate realistic retail master data
* UTF-8 encoded CSV output
* Semicolon separated files
* Configurable number of generated records
* Reproducible datasets using configurable random seeds
* Modular generator architecture
* Written for Python 3.10.12

## Current Data Generators

The current release supports generation of:

* Product Categories
* Manufacturers
* Suppliers
* Customers

Additional generators will be introduced in future releases.

## Requirements

* Python 3.10.12
* pip
* Virtual Environment (recommended)

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd RetailDWGen
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Generate the CSV files by running:

```bash
python generate.py
```

Generated files are written to

```text
output/stammdaten/
```

## Configuration

The amount of generated data and additional settings are controlled through the configuration files located in the `config` directory.

## Project Structure

```text
RetailDWGen/

config/
generator/
generator/stammdaten/
generator/infrastruktur/
output/

generate.py
requirements.txt
VERSION
README.md
```

## Design Principles

RetailDWGen follows a few simple principles:

* Easy to understand
* Easy to extend
* Reproducible data generation
* Clear project structure
* Database independent

The project intentionally focuses on generating high-quality CSV data without being tied to any specific database system.

## License

RetailDWGen is released under the MIT License.

See the LICENSE file for details.

