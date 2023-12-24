class ShapefileNotFoundErrorException(Exception):
    def __init__(self, message="Shapefile not found in the specified directory."):
        self.message = message
        super().__init__(self.message)
