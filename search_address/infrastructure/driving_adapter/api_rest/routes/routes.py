from flask import jsonify, Blueprint, request
from search_address.infrastructure.driving_adapter.api_rest.composer import create_search_address_street_controller
from shared.adapter import flask_adapter
import os
from dotenv import load_dotenv
from search_address.infrastructure.driven_adapter.vaex_core import vaex

load_dotenv()
df = vaex.open(str(os.getenv("ROUTE_FILE_DATA_ADDRESS_STREET_HDF5")))

api_routes_bp = Blueprint("api_routes_search_address", __name__)

@api_routes_bp.route("/api/search/address/street", methods=["POST"])
async def search_address_street():
    
    response = await flask_adapter(request=request, api_route=create_search_address_street_controller(df))

    return jsonify({
                "status" : response.json().get("status"),
                "code" : response.status_code,
                "message" : response.json().get('message'),
                "data" : response.json().get("data")
            }), response.status_code