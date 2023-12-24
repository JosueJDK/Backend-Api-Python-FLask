class ZipFileExtractorServiceException(Exception):
    def __init__(self, message="An error occurred during zip extraction."):
        self.message = message
        super().__init__(self.message)
