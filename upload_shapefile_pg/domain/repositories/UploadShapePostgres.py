from abc import ABC, abstractmethod

class UploadShapePostgresRepository(ABC):
    @abstractmethod
    def upload_shp_postgres(self, shapefile_path: str, table_name: str) -> str:
        """
        Uploads a shapefile to a PostgreSQL database table.

        Args:
        - shapefile_path (str): Path to the shapefile to be uploaded.
        - table_name (str): Name of the table in the PostgreSQL database.

        Returns:
        - bool: True if the upload was successful, False otherwise.
        """
        raise NotImplementedError()
