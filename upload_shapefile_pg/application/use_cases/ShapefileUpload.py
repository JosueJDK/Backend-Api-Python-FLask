import os
from abc import ABC, abstractmethod
from upload_shapefile_pg.domain.repositories import UploadShapePostgresRepository
from upload_shapefile_pg.domain.services import SearchFileService, ZipFileExtractorService
from upload_shapefile_pg.domain.exceptions import SearchFileServiceException, ShapefileNotFoundErrorException, ZipExtractionErrorException, ZipFileExtractorServiceException

class ShapefileUploadUseCase:
    """
    Use case class to handle the upload of shapefiles to a PostgreSQL database.

    Args:
    - upload_shp_postgres: An instance of UploadShapePostgresRepository.

    This class extracts and uploads shapefiles to a PostgreSQL database.
    """

    def __init__(self, upload_shp_postgres: UploadShapePostgresRepository):
        self._upload_shp_postgres = upload_shp_postgres
        self._zip_extractor = ZipFileExtractorService()
        self._file_searcher = SearchFileService()

    async def run(self, upload_folder: str, zip_file_name: str) -> str:
        """
        Runs the sequence of actions for shapefile upload.

        Args:
        - upload_folder: The path to the folder containing the uploaded zip file.
        - zip_file_name: Name of the uploaded zip file.

        Returns:
        - bool: True if the upload process is successful, False otherwise.
        """
        try:
            zip_file_path = os.path.join(upload_folder, zip_file_name)
            
            # Extract Zip File
            unzipped_files = await self._zip_extractor.unzip_file(zip_file_path)
            
            # Search for .shp file
            path_file_shp = await self._file_searcher.search_file_shape(unzipped_files)
            
            # Upload Shape File to Postgres
            return await self._upload_shp_postgres.upload_shp_postgres(path_file_shp, zip_file_name.rstrip('.zip'))
            
        except Exception as e:
            raise e