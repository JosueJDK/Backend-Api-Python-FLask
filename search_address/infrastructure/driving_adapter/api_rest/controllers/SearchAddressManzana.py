from typing import Type
from httpx import Request, Response
from shared.errors import HttpErrors
import json

class SearchAddressManzanaController:

    def __init__(self, dataframe):
        self.df = dataframe

    async def route(self, http_request: Type[Request]) -> Response:
        try:
            body_params = http_request.json.keys()

            _departamento = http_request.json['departamento'] if 'departamento' in body_params else False
            _provincia = http_request.json['provincia'] if 'provincia' in body_params else False
            _distrito = http_request.json['distrito'] if 'distrito' in body_params else False
            _urbanizacion = http_request.json['urbanizacion'] if 'urbanizacion' in body_params else False
            _manzana = http_request.json['manzana'] if 'manzana' in body_params else False
            _lote = http_request.json['lote'] if 'lote' in body_params else False
            
            # if (_manzana and
            #     len(_manzana) != 0 and
            #     _lote and
            #     len(str(_lote)) != 0
            # ):                                
            #     result_data = self.df.search.address_street(
            #         _departamento if len(str(_departamento)) != 0 else False,
            #         _provincia if len(str(_provincia)) != 0 else False,
            #         _distrito if len(str(_distrito)) != 0 else False,
            #         _manzana,
            #         _lote,
            #     ).to_pandas_df()

            #     json_data = result_data.to_json(orient='records')

            #     return self.success_response("data", {"data_search":json.loads(json_data)})
            if (_urbanizacion and
                len(_urbanizacion) != 0  and
                _manzana and
                len(_manzana) != 0
            ):                                
                result_data = self.df.search.address_manzana(
                    _departamento if len(str(_departamento)) != 0 else False,
                    _provincia if len(str(_provincia)) != 0 else False,
                    _distrito if len(str(_distrito)) != 0 else False,
                    _urbanizacion,
                    _manzana,
                    False
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
