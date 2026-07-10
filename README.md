# RetailDWGen

🇩🇪 [Deutsch](README.de.md) | 🇬🇧 **English** | 🇪🇸 [Español](README.es.md) | 🇫🇷 [Français](README.fr.md)

---

## Realistic Test Data for Retail, Data Warehousing and Business Intelligence

RetailDWGen is a Python-based generator for realistic retail test data.

The project generates structured CSV files suitable for software testing, training, demonstrations, and the development and validation of Data Warehouse (DWH), Business Intelligence (BI), and analytics solutions.

The generated datasets are based on common retail business processes and can be imported into virtually any database system for further processing and analysis.

---

# Version 2.0

Version **2.0** transforms RetailDWGen into a comprehensive platform for generating realistic retail datasets.

In addition to master data, the project now generates transaction data, inventory data, and technical control files. This makes RetailDWGen particularly suitable for Data Warehouse projects, ETL development, software testing, analytics, and demonstrations.

The datasets generated in version 2.0 intentionally focus on establishing a complete retail data landscape. Functional consistency between the different data domains will be enhanced step by step in future releases.

---

# Features

* Realistic master data generation
* Realistic transaction data generation
* Inventory data generation
* Technical control (check) files
* Continuous technical sequence numbers
* Reproducible datasets using configurable random seeds
* UTF-8 CSV output with semicolon separators
* Modular generator architecture
* Consistent generator design
* Developed with Python 3.10

---

# Supported Data Domains

## Master Data

* Product groups
* Products
* Manufacturers
* Suppliers
* Customers
* Stores
* Warehouses
* Employees
* Cash registers
* Shopping carts
* Additional master data

---

## Transaction Data

* Sales
* Goods receipts
* Customer returns
* Lost / damaged goods
* Receipt (basket) sales
* Shopping cart movements

---

## Inventory Data

* Warehouse inventory
* Inventory counts

---

## Technical Components

Each generator follows the same structure and produces:

* CSV data file
* Technical check file
* Continuous technical sequence numbers

---

# Typical Use Cases

RetailDWGen is suitable for:

* Data Warehouse projects
* Business Intelligence
* ETL development
* Software testing
* Performance testing
* Data migration
* Demonstrations
* Training
* Prototyping
* Analytical applications

---

# Requirements

* Python 3.10
* Python virtual environment (recommended)

---

# Installation

Clone the repository

```bash
git clone <repository-url>
cd RetailDWGen
```

Create a virtual environment

```bash
python3 -m venv .venv
```

Activate the virtual environment

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Usage

Start the data generation process

```bash
python generate.py
```

Generated CSV files are written to:

```text
output/
```

---

# Project Structure

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

The number of generated records and additional settings are centrally managed through configuration files.

---

# Roadmap

## Version 2.x

* Additional data domains
* Improved business consistency
* Extended warehouse and inventory logic
* More simulation data

## Version 3.x

* Cross-domain business consistency
* Complete retail process simulation
* Enhanced shopping cart movement simulation
* Consistent receipt and sales data
* Realistic inventory management

## Long-Term Vision

RetailDWGen aims to become a comprehensive simulation platform for retail businesses.

Future plans include:

* Complete Data Warehouse test datasets
* End-to-end retail process simulation
* Shopping cart movement analytics
* Shelf and store simulations
* AI-ready analytical datasets
* Visualization of customer movements within stores

---

# Author

**Detlef Bracker**

RetailDWGen is an open-source project created by Detlef Bracker to demonstrate modern software engineering, data modeling, and Data Warehouse architectures for retail environments.

---

# Feedback and Discussions

Questions, ideas, suggestions, and professional discussions are always welcome.

Please use **GitHub Discussions** for general topics or create an **Issue** if you discover a bug or would like to suggest an improvement.

Your feedback is greatly appreciated and helps improve RetailDWGen.

---

# License

This project is licensed under the MIT License.

Copyright © Detlef Bracker

For more information, please refer to the `LICENSE` file.

