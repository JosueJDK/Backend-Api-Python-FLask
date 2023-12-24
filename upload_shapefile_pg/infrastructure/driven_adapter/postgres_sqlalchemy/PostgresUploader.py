import os
import geopandas as gpd
from sqlalchemy import create_engine
from upload_shapefile_pg.domain.exceptions import PostgresUploaderServiceException

class PostgresShapefileUploader:
    """
    A class for uploading a shapefile to PostgreSQL.

    This class reads a shapefile using geopandas and uploads it to a PostgreSQL database.
    """

    def __init__(self, shapefile_path: str, table_name: str):
        """
        Initializes the PostgresShapefileUploader.

        Args:
        - shapefile_path (str): Path to the shapefile.
        - table_name (str): Name of the table in the PostgreSQL database.
        """

        self.shapefile_path = shapefile_path
        self.table_name = table_name
        self._db_connection = {
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'host': os.getenv('DB_HOST'),
            'port': os.getenv('DB_PORT'),
            'database': os.getenv('DB_DATABASE')
        }

    def upload_file_shape_postgres(self):
        """
        Uploads the shapefile to PostgreSQL.

        Reads the shapefile using geopandas and uploads it to a specified table in a PostgreSQL database.
        """
        try:
            # Load the Shapefile using geopandas
            gdf = gpd.read_file(self.shapefile_path)

            # Create a SQLAlchemy engine to perform the database upload
            engine = create_engine(self._generate_engine_url())

            # Upload the GeoDataFrame to the PostgreSQL database
            gdf.to_postgis(self.table_name, engine, if_exists='replace', index=False)

        except Exception as e:
            raise PostgresUploaderServiceException(f"Error uploading shapefile to PostgreSQL: {str(e)}")
        finally:
            if 'engine' in locals():
                engine.dispose()  # Cierra la conexión a la base de datos
                return self.table_name

    def _generate_engine_url(self) -> str:
        """
        Generates the SQLAlchemy engine URL for the PostgreSQL database.

        Returns:
        - str: SQLAlchemy engine URL.
        """
        try:
            return f"postgresql://{self._db_connection['user']}:{self._db_connection['password']}@{self._db_connection['host']}:{self._db_connection['port']}/{self._db_connection['database']}"
        except KeyError as ke:
            raise ValueError(f"Missing database configuration: {str(ke)}")
