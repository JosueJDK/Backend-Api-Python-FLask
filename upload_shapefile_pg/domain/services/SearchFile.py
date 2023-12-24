import os
from upload_shapefile_pg.domain.exceptions import SearchFileServiceException, ShapefileNotFoundErrorException

class SearchFileService:
    """
    A service class for searching shapefiles.

    This class provides functionality to search for shapefiles within a directory.
    """

    def __init__(self):
        pass

    async def search_file_shape(self, dir_shapefile_path: str) -> str:
        """
        Searches for a shapefile within the provided directory path.

        Args:
        - dir_shapefile_path (str): Path to the directory containing shapefiles.

        Returns:
        - str: Path to the found shapefile or raises ShapefileNotFoundError if not found.
        """
        try:
            for root, dirs, files in os.walk(dir_shapefile_path):
                for file in files:
                    if file.endswith('.shp'):
                        return os.path.join(root, file)
            raise ShapefileNotFoundErrorException()

        except ShapefileNotFoundErrorException as e:
            raise e

        except Exception as e:
            raise SearchFileServiceException(f"An error occurred while searching for shapefiles: {str(e)}")
