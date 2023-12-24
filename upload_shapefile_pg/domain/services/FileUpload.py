import os
from upload_shapefile_pg.domain.exceptions import FileUploadServiceException, InvalidFileExtensionException
class FileUploadService:
    """
    A service class to handle file uploads.

    Args:
    - uploaded_file: Uploaded file object.
    - allowed_extensions: Set of allowed file extensions.
    - path_upload_folder: Path to the folder where files will be uploaded.
    """

    def __init__(self, uploaded_file, allowed_extensions, path_upload_folder):
        self.allowed_extensions = allowed_extensions
        self.path_upload_folder = path_upload_folder
        self.uploaded_file = uploaded_file

    def _is_allowed_file(self, filename):
        """
        Checks if the file extension is allowed.

        Args:
        - filename: Name of the file.

        Returns:
        - bool: True if the file extension is allowed, False otherwise.
        """
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.allowed_extensions

    def save_file(self):
        """
        Saves the uploaded file to the specified folder if it meets the criteria.

        Returns:
        - str or None: Returns the filename if successful, None otherwise.
        """
        try:
            if self.uploaded_file:
                if not self._is_allowed_file(self.uploaded_file.filename):
                    raise InvalidFileExtensionException()
                file_path = os.path.join(self.path_upload_folder, self.uploaded_file.filename)
                self.uploaded_file.save(file_path)
                return self.uploaded_file.filename
            else:
                return None
        except InvalidFileExtensionException as e:
            raise e
        except Exception as e:
            raise FileUploadServiceException(f"Error saving the file: {str(e)}")
