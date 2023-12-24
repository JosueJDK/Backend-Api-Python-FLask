class ZipExtractionErrorException(Exception):
    def __init__(self, message="Error extracting zip file."):
        self.message = message
        super().__init__(self.message)
