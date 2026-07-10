# RetailDWGen

🇩🇪 [Deutsch](README.de.md) | 🇬🇧 [English](README.md) | 🇪🇸 **Español** | 🇫🇷 [Français](README.fr.md)

---

## Datos de prueba realistas para Comercio Minorista, Data Warehouse e Inteligencia de Negocio

RetailDWGen es un generador de datos de prueba para empresas del comercio minorista desarrollado en Python.

El proyecto genera archivos CSV estructurados que pueden utilizarse para pruebas de software, formación, demostraciones y para el desarrollo y validación de soluciones de Data Warehouse (DWH), Business Intelligence (BI) y análisis de datos.

Los conjuntos de datos generados se basan en procesos habituales del comercio minorista y pueden importarse a prácticamente cualquier sistema de bases de datos para su posterior procesamiento y análisis.

---

# Versión 2.0

Con la versión **2.0**, RetailDWGen se convierte en una plataforma integral para la generación de datos realistas del sector minorista.

Además de los datos maestros, el proyecto genera datos transaccionales, datos de inventario y archivos técnicos de control. Esto hace que RetailDWGen sea especialmente adecuado para proyectos de Data Warehouse, procesos ETL, pruebas de software, análisis de datos y demostraciones.

Los datos generados en la versión 2.0 están orientados deliberadamente a construir un ecosistema completo de datos comerciales. La coherencia funcional entre los distintos tipos de datos se ampliará progresivamente en futuras versiones.

---

# Características

* Generación de datos maestros realistas
* Generación de datos transaccionales
* Generación de datos de inventario
* Generación de archivos técnicos de control
* Números de secuencia técnicos consecutivos
* Datos reproducibles mediante una semilla aleatoria configurable
* Salida CSV en formato UTF-8 con separador de punto y coma
* Arquitectura modular de generadores
* Diseño uniforme para todos los generadores
* Desarrollado con Python 3.10

---

# Áreas de datos compatibles

## Datos maestros

* Grupos de productos
* Productos
* Fabricantes
* Proveedores
* Clientes
* Tiendas
* Almacenes
* Empleados
* Cajas registradoras
* Carritos de compra
* Otros datos maestros

---

## Datos transaccionales

* Ventas
* Entradas de mercancía
* Devoluciones de clientes
* Productos perdidos o destruidos
* Ventas por ticket
* Movimientos de carritos de compra

---

## Datos de inventario

* Inventario de almacén
* Inventarios físicos

---

## Componentes técnicos

Cada generador sigue la misma estructura y genera:

* Archivo CSV con los datos
* Archivo técnico de control (Check)
* Números de secuencia técnicos consecutivos

---

# Casos de uso

RetailDWGen resulta adecuado para:

* Proyectos de Data Warehouse
* Business Intelligence
* Desarrollo de procesos ETL
* Pruebas de software
* Pruebas de rendimiento
* Migraciones de datos
* Demostraciones
* Formación
* Prototipos
* Aplicaciones analíticas

---

# Requisitos

* Python 3.10
* Entorno virtual de Python (recomendado)

---

# Instalación

Clonar el repositorio

```bash
git clone <repository-url>
cd RetailDWGen
```

Crear un entorno virtual

```bash
python3 -m venv .venv
```

Activar el entorno virtual

```bash
source .venv/bin/activate
```

Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

# Uso

Iniciar la generación de datos

```bash
python generate.py
```

Los archivos CSV generados se almacenan en:

```text
output/
```

---

# Estructura del proyecto

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

# Configuración

La cantidad de registros generados y el resto de parámetros se gestionan de forma centralizada mediante archivos de configuración.

---

# Hoja de ruta

## Versión 2.x

* Nuevas áreas de datos
* Mejora de la coherencia funcional
* Ampliación de la lógica de almacenes e inventarios
* Nuevos escenarios de simulación

## Versión 3.x

* Integración funcional entre todas las áreas de datos
* Simulación completa de procesos comerciales
* Simulación avanzada de movimientos de carritos
* Integración coherente entre tickets y ventas
* Gestión realista de inventarios

## Visión a largo plazo

RetailDWGen tiene como objetivo convertirse en una plataforma integral de simulación para empresas del comercio minorista.

Entre los desarrollos previstos se incluyen:

* Datos completos de prueba para Data Warehouse
* Simulación integral de procesos comerciales
* Análisis de movimientos de carritos de compra
* Simulación de tiendas y estanterías
* Conjuntos de datos preparados para inteligencia artificial
* Visualización de los recorridos de los clientes dentro de la tienda

---

# Autor

**Detlef Bracker**

RetailDWGen es un proyecto de código abierto desarrollado por Detlef Bracker para demostrar técnicas modernas de desarrollo de software, modelado de datos y arquitecturas de Data Warehouse aplicadas al comercio minorista.

---

# Comentarios y debates

Las preguntas, sugerencias, ideas y debates técnicos son siempre bienvenidos.

Puede utilizar **GitHub Discussions** para cuestiones generales o crear un **Issue** si detecta un error o desea proponer una mejora.

Toda aportación ayuda a seguir mejorando RetailDWGen.

---

# Licencia

Este proyecto se distribuye bajo la licencia MIT.

Copyright © Detlef Bracker

Para más información, consulte el archivo `LICENSE`.

