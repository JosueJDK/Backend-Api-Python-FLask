from flask import jsonify, Blueprint, request
from upload_shapefile_pg.infrastructure.driving_adapter.api_rest.composer import create_upload_zip_controller
from shared.adapter import flask_adapter

api_routes_bp = Blueprint("api_routes", __name__)

@api_routes_bp.route("/api/upload", methods=["POST"])
async def upload_zip():
    
    response = await flask_adapter(request=request, api_route=create_upload_zip_controller())

    return jsonify({
                "status" : response.json().get("status"),
                "code" : response.status_code,
                "message" : response.json().get('message'),
                "data" : response.json().get("data")
            }), response.status_code