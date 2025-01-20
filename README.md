# data-warehouse-cloud
Proyecto para crear un Data Warehouse en la nube usando AWS Redshift/PostgreSQL y transformaciones de datos

# Data Warehouse en la Nube

## Descripción
Este proyecto tiene como objetivo diseñar y crear un **Data Warehouse** utilizando **AWS Redshift**, **PostgreSQL**, o **Snowflake**. Se extraen grandes volúmenes de datos de diversas fuentes, se aplican transformaciones usando **Python** y **dbt**, y se organiza el modelo de datos en **estrella** o **3NF (tercera forma normal)**.

## Tecnologías Utilizadas
- **Base de Datos**: PostgreSQL o AWS Redshift
- **Transformación de Datos**: Python, dbt
- **Automatización de Procesos**: Airflow (opcional)
- **Modelado de Datos**: Modelo en estrella o 3NF

## Estructura del Proyecto

### `data/`
Contiene los archivos de datos de ejemplo.

### `scripts/`
Contiene los scripts de Python para cargar y transformar los datos.

### `dbt_project/`
Contiene las configuraciones y modelos de **dbt** para realizar transformaciones SQL en el Data Warehouse.

## Requisitos

1. PostgreSQL o AWS Redshift configurado.
2. Instalar las dependencias del proyecto con:

    ```bash
    pip install -r requirements.txt
    ```

## Cómo Ejecutar

1. Configura tu conexión a la base de datos en el script `scripts/load_data.py`.
2. Carga los datos en la base de datos ejecutando:

    ```bash
    python scripts/load_data.py
    ```

3. Realiza las transformaciones de datos con:

    ```bash
    python scripts/transform_data.py
    ```

4. Configura y ejecuta los modelos en **dbt** siguiendo las instrucciones en la carpeta `dbt_project`.

## Licencia
Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.
