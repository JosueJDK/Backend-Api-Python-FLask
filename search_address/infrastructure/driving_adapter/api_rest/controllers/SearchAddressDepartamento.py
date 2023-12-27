from typing import Type
from httpx import Request, Response
from shared.errors import HttpErrors
import json

class SearchAddressDepartamentoController:

    def __init__(self, dataframe):
        self.df = dataframe

    async def route(self, http_request: Type[Request]) -> Response:
        try:
            body_params = http_request.json.keys()

            if (
                "departamento" in body_params
            ):        
                result_data = self.df.search.address_departamento(http_request.json['departamento']).to_pandas_df()
                json_data = result_data.to_json(orient='records')

                return self.success_response("data", {"data_search":json.loads(json_data)})
            else:
                return self.bad_request("Todos los campos son requeridos.")
                
            
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
