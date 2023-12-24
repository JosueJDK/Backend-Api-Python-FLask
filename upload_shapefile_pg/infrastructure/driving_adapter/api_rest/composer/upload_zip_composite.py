from upload_shapefile_pg.infrastructure.driving_adapter.api_rest.controllers import UploadZipController

def create_upload_zip_controller() -> UploadZipController:
    """
    Creates an instance of UploadZipController.

    Returns:
    - UploadZipController: Instance of UploadZipController for handling zip file uploads.
    """
    upload_zip_controller = UploadZipController()
    return upload_zip_controller