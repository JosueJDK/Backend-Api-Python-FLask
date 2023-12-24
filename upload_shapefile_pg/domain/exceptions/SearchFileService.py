class SearchFileServiceException(Exception):
    def __init__(self, message="An error occurred while searching for shapefiles."):
        self.message = message
        super().__init__(self.message)
