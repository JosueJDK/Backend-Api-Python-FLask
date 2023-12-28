import requests
import os

def publish_layer_in_geoserver(layer_name):
    workspace = os.getenv('WORKSPACE_GEOSERVER')
    data_store_name = os.getenv('DATASTORE_GEOSERVER')
    native_name = layer_name
    
    geoserver_url = os.getenv('GEOSERVER_URL')
    rest_url = f'{geoserver_url}/rest/workspaces/{workspace}/datastores/{data_store_name}/featuretypes'

    xml_data = f'''
        <featureType>
            <name>{layer_name}</name>
            <nativeName>{native_name}</nativeName>
            <srs>EPSG:4326</srs>
        </featureType>
    '''

    headers = {
        'Content-Type': 'application/xml',
    }
    
    auth = ('admin', 'geoserver')

    try:
        response = requests.post(rest_url, data=xml_data, headers=headers, auth=auth)
        if response.status_code == 201:
            print(f"Capa '{layer_name}' publicada en GeoServer.")
            return f"Capa '{layer_name}' publicada en GeoServer."
        else:
            return f"Error al publicar la capa en GeoServer. Código de estado: {response.status_code}"
    except requests.RequestException as e:
        return f"Error al realizar la solicitud: {str(e)}"