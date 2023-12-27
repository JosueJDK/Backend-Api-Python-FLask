from flask import Flask
from flask_cors import CORS
from upload_shapefile_pg.infrastructure.driving_adapter.api_rest.routes import api_routes_bp as upload_shapefile_pg
from search_address.infrastructure.driving_adapter.api_rest.routes import api_routes_bp as search_address

app = Flask(__name__)
CORS(app)

app.register_blueprint(upload_shapefile_pg)
app.register_blueprint(search_address)

if '__main__' == __name__:
    app.run(host="0.0.0.0", port=5400, debug=False)
