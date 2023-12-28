import requests
import os

def get_layer_bbox(layer_name):
    workspace = os.getenv('WORKSPACE_GEOSERVER')
    data_store_name = os.getenv('DATASTORE_GEOSERVER')
    native_name = layer_name
    
    geoserver_url = os.getenv('GEOSERVER_URL')
    rest_url = f'{geoserver_url}/rest/workspaces/{workspace}/datastores/{data_store_name}/featuretypes/{native_name}.json'

    auth = ('admin', 'geoserver')

    try:
        response = requests.get(rest_url, auth=auth)
        if response.status_code == 200:
            layer_info = response.json()
            bbox = layer_info['featureType']['nativeBoundingBox']
            return bbox
        else:
            return f"Error al obtener la bbox de la capa. Código de estado: {response.status_code}"
    except requests.RequestException as e:
        return f"Error al realizar la solicitud: {str(e)}"