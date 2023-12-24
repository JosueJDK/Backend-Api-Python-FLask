import os
from typing import Type
from httpx import Request, Response
from shared.errors import HttpErrors
from upload_shapefile_pg.domain.services import FileUploadService, DirectoryFileDeleterService
from upload_shapefile_pg.application.use_cases import ShapefileUploadUseCase
from upload_shapefile_pg.infrastructure.implementation import ShapefileToPostgresUploaderRepository

class UploadZipController:
    """ Class to handle the route for uploading a zip file """

    def __init__(self):
        # Accessing the environment variables
        self.allowed_extensions = set(os.getenv("ALLOWED_EXTENSIONS", "").split(","))
        self.upload_folder = os.getenv("UPLOAD_FOLDER")

    async def route(self, http_request: Type[Request]) -> Response:
        """
        Handles the HTTP route for uploading a zip file.

        Args:
        - http_request: The HTTP request object.

        Returns:
        - Response: HTTP response object.
        """
        try:
            # Check if the file is provided
            if 'file' not in http_request.files or not http_request.files['file'].filename:
                return self.bad_request("Archivo no proporcionado o no válido")

            file_upload_service = FileUploadService(http_request.files['file'], self.allowed_extensions, self.upload_folder)
            zip_file_name = file_upload_service.save_file()
            
            if not zip_file_name:
                return self.bad_request("Formato de archivo no válido")
            
            shapefile_upload_use_case = ShapefileUploadUseCase(ShapefileToPostgresUploaderRepository())
            data = await shapefile_upload_use_case.run(self.upload_folder, zip_file_name)

            return self.success_response("Carga de datos exitosa", {"table_name":data})
        except Exception as e:
            return self.server_error(str(e))
        
        finally:
            directoryFileDeleterService = DirectoryFileDeleterService(self.upload_folder)
            directoryFileDeleterService.delete_files()

    @staticmethod
    def bad_request(message):
        """
        Returns a 400 Bad Request response.

        Args:
        - message: Error message.

        Returns:
        - Response: HTTP 400 Bad Request response object.
        """
        return Response(status_code=400, json={"status" : "error", "message": message, "data": None})

    @staticmethod
    def success_response(message, data=None):
        """
        Returns a successful response.

        Args:
        - message: Success message.
        - data: Additional data (optional).

        Returns:
        - Response: HTTP 200 OK response object.
        """
        return Response(status_code=200, json={"status" : "success", "message": message, "data": data})

    @staticmethod
    def server_error(message):
        """
        Returns a 500 Internal Server Error response.

        Args:
        - message: Error message.

        Returns:
        - Response: HTTP 500 Internal Server Error response object.
        """
        return Response(status_code=500, json={"status" : "error", "message": message, "data": None})
