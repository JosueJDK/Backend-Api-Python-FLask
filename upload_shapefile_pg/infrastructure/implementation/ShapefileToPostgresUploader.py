from upload_shapefile_pg.domain.repositories import UploadShapePostgresRepository
from upload_shapefile_pg.infrastructure.driven_adapter.postgres_sqlalchemy import PostgresShapefileUploader

class ShapefileToPostgresUploaderRepository(UploadShapePostgresRepository):
    """
    Repository implementation for uploading shapefiles to PostgreSQL.
    
    Inherits from UploadShapePostgresRepository and implements the upload_shp_postgres method.
    """

    async def upload_shp_postgres(self, shapefile_path: str, table_name: str) -> str:
        """
        Uploads a shapefile to PostgreSQL.

        Args:
        - shapefile_path (str): Path to the shapefile.
        - table_name (str): Name of the table in PostgreSQL.

        Returns:
        - bool: True if the upload is successful, otherwise False.
        """
        try:
            postgres_shapefile_uploader = PostgresShapefileUploader(shapefile_path, table_name)
            return postgres_shapefile_uploader.upload_file_shape_postgres()
        except Exception as e:
            raise e