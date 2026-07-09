# RetailDWGen

RetailDWGen es un proyecto de código abierto desarrollado en Python para generar datos de prueba realistas de una empresa del sector comercial.

Los archivos CSV generados pueden importarse en prácticamente cualquier sistema de bases de datos relacional, plataforma de datos o entorno de análisis. El objetivo del proyecto es proporcionar datos reproducibles y de alta calidad para desarrollo, formación, demostraciones y pruebas de rendimiento.

## Características

* Generación de datos maestros realistas para empresas comerciales
* Salida en formato CSV codificado en UTF-8
* Archivos separados por punto y coma (;)
* Número de registros configurable
* Generación reproducible mediante una semilla aleatoria configurable
* Arquitectura modular basada en generadores
* Desarrollado para Python 3.10.12

## Generadores disponibles

La versión actual permite generar:

* Grupos de productos
* Fabricantes
* Proveedores
* Clientes

## Requisitos

* Python 3.10.12
* pip
* Se recomienda utilizar un entorno virtual

## Instalación

Clonar el repositorio:

```bash
git clone <repository-url>
cd RetailDWGen
```

Crear un entorno virtual:

```bash
python3 -m venv .venv
```

Activar el entorno:

```bash
source .venv/bin/activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Uso

Ejecutar el generador:

```bash
python generate.py
```

Los archivos CSV se crearán en el directorio:

```text
output/stammdaten/
```

## Configuración

La cantidad de datos generados y otros parámetros se configuran mediante los archivos incluidos en el directorio `config`.

## Estructura del proyecto

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

## Principios del proyecto

RetailDWGen se desarrolla siguiendo unos principios sencillos:

* Código claro y fácil de comprender
* Arquitectura modular
* Datos reproducibles
* Estructura del proyecto bien organizada
* Independencia del sistema de base de datos

El objetivo principal es generar archivos CSV realistas que puedan utilizarse posteriormente en distintos entornos de datos, sin depender de una tecnología específica.

## Licencia

RetailDWGen se distribuye bajo la licencia MIT.

Consulta el archivo `LICENSE` para obtener más información.

