class FileUploadServiceException(Exception):
    def __init__(self, message="Error saving the file"):
        self.message = message
        super().__init__(self.message)
