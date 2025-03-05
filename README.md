# Car Scraper API

Este proyecto es una API construida con **FastAPI** que permite obtener datos de vehículos (coches) desde múltiples fuentes en línea. Los datos se obtienen mediante web scraping y se pueden filtrar por marca, modelo y año. La API está diseñada para ser rápida y eficiente, utilizando un sistema de caché para almacenar los datos después de la primera solicitud. (La primera vez que se corre el sistema dura aproximadamente unos 20 segundos)

## Características principales

- **Extracción de datos**: Obtiene datos de vehículos desde tres fuentes diferentes.
- **Filtros**: Permite filtrar los resultados por marca, modelo y año.
- **Caché**: Almacena los datos en caché después de la primera solicitud para mejorar el rendimiento.
- **Endpoint único**: Proporciona un único endpoint para acceder a los datos filtrados.

## Requisitos previos

Antes de ejecutar este proyecto, asegúrate de tener instalado lo siguiente:

- Python 3.8 o superior.
- `pip` (gestor de paquetes de Python).

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu-usuario/car-scraper-api.git
   cd car-scraper-api
   ````
2. Crea un entorno virtual (opcional pero recomendado):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
3. Instala las dependencias:

   ```bash
   pip install fastapi uvicorn requests beautifulsoup4

## Dependencias

El proyecto utiliza las siguientes dependencias:
    `FastAPI`: Framework para construir la API.
    `uvicorn`: Servidor ASGI para ejecutar la API.
    `requests`: Para realizar solicitudes HTTP.
    `beautifulsoup4`: Para analizar el HTML y extraer datos.
### Ejecución
Para ejecutar la API, sigue estos pasos:
Asegúrate de estar en el directorio raíz del proyecto.
Ejecuta el siguiente comando:

   ```bash
    uvicorn api:app --reload --host 0.0.0.0 --port 8000
        Esto iniciará el servidor en http://0.0.0.0:8000.
   ````
   
Uso de la API
La API proporciona un único endpoint para obtener los datos de los vehículos:

Endpoint
```bash
URL: http://0.0.0.0:8000/cars
````

Método: GET
Parámetros de consulta
Puedes filtrar los resultados utilizando los siguientes parámetros:
`brand`: Filtra por marca del vehículo (ejemplo: volvo).
`model`: Filtra por modelo del vehículo (ejemplo: xc).
`year`: Filtra por año del vehículo (ejemplo: 2018).

Ejemplos de solicitudes
1. Obtener todos los vehículos:
    ```bash
    curl -X GET "http://0.0.0.0:8000/cars"
    ````
2. Filtrar por marca (brand):
    ```bash
    curl -X GET "http://0.0.0.0:8000/cars?brand=volvo"
    ````
3. Filtrar por modelo (model):
    ```bash
    curl -X GET "http://0.0.0.0:8000/cars?model=xc"
    ````
4. Filtrar por año (year):
    ```bash
    curl -X GET "http://0.0.0.0:8000/cars?year=2018"
    ````
Respuesta
La API devuelve un objeto JSON con la siguiente estructura:
 ```bash
    {
        {
    "total": 10,
    "cars": [
                {
                "brand": "Volvo",
                "model": "XC90",
                "year": "2018",
                "price": "$45,000",
                "source": "montao.do",
                "page": 1
                },
        ]
        }
    }
 ````



        