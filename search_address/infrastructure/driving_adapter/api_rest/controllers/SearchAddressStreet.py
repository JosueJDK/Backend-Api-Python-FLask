from typing import Type
from httpx import Request, Response
from shared.errors import HttpErrors
import json

class SearchAddressStreetController:

    def __init__(self, dataframe, dataframe2):
        self.df = dataframe
        self.df2 = dataframe2

    async def route(self, http_request: Type[Request]) -> Response:
        """
        Handles the HTTP route for uploading a zip file.

        Args:
        - http_request: The HTTP request object.

        Returns:
        - Response: HTTP response object.
        """
        try:
            body_params = http_request.json.keys()

            _departamento = http_request.json['departamento'] if 'departamento' in body_params else False
            _provincia = http_request.json['provincia'] if 'provincia' in body_params else False
            _distrito = http_request.json['distrito'] if 'distrito' in body_params else False
            _direccion = http_request.json['direccion'] if 'direccion' in body_params else False
            _numpuerta = http_request.json['numpuerta'] if 'numpuerta' in body_params else False
            
            if (_direccion and
                len(_direccion) != 0 and
                _numpuerta and
                len(str(_numpuerta)) != 0
            ):                                
                result_data = self.df.search.address_street(
                    _departamento if len(str(_departamento)) != 0 else False,
                    _provincia if len(str(_provincia)) != 0 else False,
                    _distrito if len(str(_distrito)) != 0 else False,
                    _direccion,
                    _numpuerta,
                ).to_pandas_df()

                json_data = result_data.to_json(orient='records')

                return self.success_response("data", {"data_search":json.loads(json_data)})
            elif (_direccion and
                len(_direccion) != 0
            ):                                
                result_data = self.df2.search.address_street(
                    _departamento if len(str(_departamento)) != 0 else False,
                    _provincia if len(str(_provincia)) != 0 else False,
                    _distrito if len(str(_distrito)) != 0 else False,
                    _direccion,
                    False
                ).to_pandas_df()

                json_data = result_data.to_json(orient='records')

                return self.success_response("data", {"data_search":json.loads(json_data)})
            else:
                return self.bad_request("Todos los campos son requeridos.")
                
            
        except Exception as e:
            print(e)
            return self.server_error(str(e))

    @staticmethod
    def bad_request(message):
        """
        Returns a 400 Bad Request response.

        Args:
        - message: Error message.

        Returns:
        - Response: HTTP 400 Bad Request response object.
        """
        return Response(status_code=400, json={"status" : "error", "message": message, "data": None})

    @staticmethod
    def success_response(message, data=None):
        """
        Returns a successful response.

        Args:
        - message: Success message.
        - data: Additional data (optional).

        Returns:
        - Response: HTTP 200 OK response object.
        """
        return Response(status_code=200, json={"status" : "success", "message": message, "data": data})

    @staticmethod
    def server_error(message):
        """
        Returns a 500 Internal Server Error response.

        Args:
        - message: Error message.

        Returns:
        - Response: HTTP 500 Internal Server Error response object.
        """
        return Response(status_code=500, json={"status" : "error", "message": message, "data": None})
