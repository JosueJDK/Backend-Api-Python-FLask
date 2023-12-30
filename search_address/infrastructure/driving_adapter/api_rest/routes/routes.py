from flask import jsonify, Blueprint, request
from search_address.infrastructure.driving_adapter.api_rest.composer import (
    create_search_address_street_controller, 
    search_addres_departamento_controller,
    search_addres_provincia_controller,
    search_addres_distrito_controller,
    search_addres_manzana_controller,
    search_addres_urbanizacion_controller,
    search_addres_centropoblado_controller)
from shared.adapter import flask_adapter
import os
from dotenv import load_dotenv
from search_address.infrastructure.driven_adapter.vaex_core import vaex

load_dotenv()

api_routes_bp = Blueprint("api_routes_search_address", __name__)

df_departamento = vaex.open("/home/ubuntu/clean_architecture/public/data/PERU_DEPARTAMENTOS.hdf5")
@api_routes_bp.route("/api/search/address/departamento", methods=["GET"])
async def search_address_departamento():
    
    response = await flask_adapter(request=request, api_route=search_addres_departamento_controller(df_departamento))

    return jsonify({
                "status" : response.json().get("status"),
                "code" : response.status_code,
                "message" : response.json().get('message'),
                "data" : response.json().get("data")
            }), response.status_code

df_provincia = vaex.open("/home/ubuntu/clean_architecture/public/data/PERU_PROVINCIAS.hdf5")
@api_routes_bp.route("/api/search/address/provincia", methods=["POST"])
async def search_address_provincia():
    
    response = await flask_adapter(request=request, api_route=search_addres_provincia_controller(df_provincia))

    return jsonify({
                "status" : response.json().get("status"),
                "code" : response.status_code,
                "message" : response.json().get('message'),
                "data" : response.json().get("data")
            }), response.status_code

df_distrito = vaex.open("/home/ubuntu/clean_architecture/public/data/PERU_DISTRITOS.hdf5")
@api_routes_bp.route("/api/search/address/distrito", methods=["POST"])
async def search_address_distrito():
    
    response = await flask_adapter(request=request, api_route=search_addres_distrito_controller(df_distrito))

    return jsonify({
                "status" : response.json().get("status"),
                "code" : response.status_code,
                "message" : response.json().get('message'),
                "data" : response.json().get("data")
            }), response.status_code

df_street = vaex.open("/home/ubuntu/clean_architecture/public/data/PERU_CALLES.hdf5")
df_vias = vaex.open("public/data/PERU_VIAS_UNICAS.hdf5")
@api_routes_bp.route("/api/search/address/street", methods=["POST"])
async def search_address_street():
    
    response = await flask_adapter(request=request, api_route=create_search_address_street_controller(df_street, df_vias))

    return jsonify({
                "status" : response.json().get("status"),
                "code" : response.status_code,
                "message" : response.json().get('message'),
                "data" : response.json().get("data")
            }), response.status_code


df_urbanizacion = vaex.open("/home/ubuntu/clean_architecture/public/data/PERU_MANZANAS_UNICAS.hdf5")
@api_routes_bp.route("/api/search/address/urbanizacion", methods=["POST"])
async def search_address_urbanizacion():
    
    response = await flask_adapter(request=request, api_route=search_addres_urbanizacion_controller(df_urbanizacion))

    return jsonify({
                "status" : response.json().get("status"),
                "code" : response.status_code,
                "message" : response.json().get('message'),
                "data" : response.json().get("data")
            }), response.status_code

df_manzanas = vaex.open("/home/ubuntu/clean_architecture/public/data/PERU_MANZANAS.hdf5")
@api_routes_bp.route("/api/search/address/manzana", methods=["POST"])
async def search_address_manzana():
    
    response = await flask_adapter(request=request, api_route=search_addres_manzana_controller(df_manzanas))

    return jsonify({
                "status" : response.json().get("status"),
                "code" : response.status_code,
                "message" : response.json().get('message'),
                "data" : response.json().get("data")
            }), response.status_code

df_centro_poblado = vaex.open("/home/ubuntu/clean_architecture/public/data/PERU_CENTROS_POBLADOS.hdf5")
@api_routes_bp.route("/api/search/address/centro_poblado", methods=["POST"])
async def search_address_centropoblado():
    
    response = await flask_adapter(request=request, api_route=search_addres_centropoblado_controller(df_centro_poblado))

    return jsonify({
                "status" : response.json().get("status"),
                "code" : response.status_code,
                "message" : response.json().get('message'),
                "data" : response.json().get("data")
            }), response.status_code