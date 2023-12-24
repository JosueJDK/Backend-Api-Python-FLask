import zipfile
from upload_shapefile_pg.domain.exceptions import ZipFileExtractorServiceException, ZipExtractionErrorException

class ZipFileExtractorService:
    """
    A service class for extracting zip files.

    This class provides functionality to extract a zip file to a specified directory.
    """

    def __init__(self):
        pass

    async def unzip_file(self, path_zipfile_path: str) -> str:
        """
        Unzips the provided zip file to a directory with the same name as the zip file.

        Args:
        - path_zipfile_path (str): Path to the zip file.

        Returns:
        - str: Path to the directory where the file was extracted.
        """
        try:
            extract_folder = path_zipfile_path.rstrip('.zip')
            with zipfile.ZipFile(path_zipfile_path, 'r') as zip_ref:
                zip_ref.extractall(extract_folder)
            return extract_folder

        except zipfile.BadZipFile as bzfe:
            raise ZipExtractionErrorException(f"Error extracting zip file: {str(bzfe)}")
            
        except Exception as e:
            raise ZipFileExtractorServiceException(f"An error occurred during zip extraction: {str(e)}")
