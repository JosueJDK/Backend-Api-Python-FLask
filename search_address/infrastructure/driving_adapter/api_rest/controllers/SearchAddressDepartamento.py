from typing import Type
from httpx import Request, Response
from shared.errors import HttpErrors
import json

class SearchAddressDepartamentoController:

    def __init__(self, dataframe):
        self.df = dataframe

    async def route(self, http_request: Type[Request]) -> Response:
        try:
            result_data = self.df.to_pandas_df()
            json_data = result_data.to_json(orient='records')

            return self.success_response("data", {"data_search":json.loads(json_data)})
        
        except Exception as e:
            return self.server_error(str(e))

    @staticmethod
    def bad_request(message):
        return Response(status_code=400, json={"status" : "error", "message": message, "data": None})

    @staticmethod
    def success_response(message, data=None):
        return Response(status_code=200, json={"status" : "success", "message": message, "data": data})

    @staticmethod
    def server_error(message):
        return Response(status_code=500, json={"status" : "error", "message": message, "data": None})
