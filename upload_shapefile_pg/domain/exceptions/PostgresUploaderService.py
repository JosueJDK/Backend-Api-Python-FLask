class PostgresUploaderServiceException(Exception):
    def __init__(self, message="Error uploading shapefile to PostgreSQL."):
        self.message = message
        super().__init__(self.message)
