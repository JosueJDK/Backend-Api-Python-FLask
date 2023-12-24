from flask import Flask
from flask_cors import CORS
from upload_shapefile_pg.infrastructure.driving_adapter.api_rest.routes import api_routes_bp
from dotenv import load_dotenv
import os

load_dotenv()

if not os.path.exists(os.getenv("UPLOAD_FOLDER")):
    os.makedirs(os.getenv("UPLOAD_FOLDER"))  # Crea el directorio si no existe


app = Flask(__name__)
CORS(app)

app.register_blueprint(api_routes_bp)

if '__main__' == __name__:
    app.run(host="0.0.0.0", port=5480, debug=False)
