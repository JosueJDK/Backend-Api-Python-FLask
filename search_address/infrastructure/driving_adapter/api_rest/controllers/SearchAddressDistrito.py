from typing import Type
from httpx import Request, Response
from shared.errors import HttpErrors
import json

class SearchAddressDistritoController:

    def __init__(self, dataframe):
        self.df = dataframe

    async def route(self, http_request: Type[Request]) -> Response:
        try:
            body_params = http_request.json.keys()

            _departamento = http_request.json['departamento'] if 'departamento' in body_params else False
            _provincia = http_request.json['provincia'] if 'provincia' in body_params else False
            _distrito = http_request.json['distrito'] if 'distrito' in body_params else False

            if (_distrito and
                len(_distrito) != 0
            ):        
                result_data = self.df.search.address_distrito(
                    _departamento if len(_departamento) != 0 else False,
                    _provincia if len(_provincia) != 0 else False,
                    _distrito
                    ).to_pandas_df()
                
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
