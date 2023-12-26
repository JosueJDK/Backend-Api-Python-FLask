# Backend-Api-Python-FLask

## Características

- Desarrollado en Python con el framework Flask.
- Implementa la arquitectura limpia (Clean Architecture).
- Permite la carga y procesamiento de archivos zip para buscar archivos .shp y cargar datos utilizando GeoPandas.
- Permite buscar direcciones por similtud usando el algoritmo de fuzzywuzzy
- Lectura de archivos con mas de 10 millones de registros en formato (parte, hdf5) usandop VAEX

## Funcionalidad

El proyecto ofrece una API REST con el siguiente endpoint:

### Ruta de la API:

```
POST http://192.168.1.35:5480/api/upload
```

#### Request

Recibe un archivo file en formato zip como dato de request para ser procesado.

#### Response

```json
{
    "code": 200,
    "data": {
        "table_name": "pruebashape"
    },
    "message": "Carga de datos exitosa",
    "status": "success"
}
```

## Características principales

- **Carga de Archivos Zip**: El proyecto permite la subida de archivos zip.
- **Descompresión y Búsqueda de Archivos .shp**: Se encarga de descomprimir los archivos zip y buscar archivos con extensión .shp.
- **Procesamiento de Datos Geoespaciales**: Utiliza la librería GeoPandas para cargar y procesar datos geoespaciales.

### Descripción de la Ruta de la API

La ruta de la API proporciona funcionalidades para buscar direcciones basadas en ciertos parámetros proporcionados. A continuación, se detallan los aspectos clave de esta funcionalidad:

#### URL y Método HTTP
- Método: `POST`
- URL: `http://192.168.1.35:5480/api/search/address/street`

#### Solicitud (Request)

La solicitud requiere los siguientes parámetros en formato JSON:
```json
{
	"departamento": "Lima",
	"provincia": "lima",
	"distrito": "san isidro",
	"direccion": "palmeras",
	"numpuerta": "166"
}
```

#### Respuesta (Response)

La respuesta devolverá datos en formato JSON, incluyendo:
```json
{
	"code": 200,
	"data": {
		"data_search": [
			{
				"departamento": "LIMA",
				"direcc": "PS PALMIRAS 166",
				"distrito": "SAN ISIDRO",
				"lat_y": -12.0945806487,
				"lon_x": -77.0430101964,
				"provincia": "LIMA",
				"similarity_direccion": 1.81
			},
            ...
		]
	},
	"message": "data",
	"status": "success"
}
```

### Características Clave de la Funcionalidad de Búsqueda de Direcciones

La funcionalidad de búsqueda de direcciones ofrece las siguientes características esenciales:

- **Búsqueda de Direcciones Precisas**: Permite buscar direcciones detalladas mediante parámetros como departamento, provincia, distrito, dirección y número de puerta.
- **Geocodificación de Direcciones**: Convierte las direcciones ingresadas en coordenadas geográficas (latitud y longitud) para su ubicación precisa en un mapa.
- **Normalización y Similaridad de Direcciones**: Normaliza las direcciones y encuentra similitudes cercanas para mejorar la precisión de la búsqueda.


## Uso

1. Clona este repositorio.
2. Instala las dependencias necesarias.
3. Ejecuta la aplicación.

## Ejecución

Para iniciar la aplicación:

```bash
# Instala las dependencias
pip install -r requirements.txt

# Ejecuta la aplicación en modo desarrollador
python app.py

# Ejecuta la aplicación en modo produccion
gunicorn --worker-class gevent --workers 8 --bind 0.0.0.0:5480 app:app --max-requests 10000 --timeout 300 --keep-alive 5 --log-level info
```