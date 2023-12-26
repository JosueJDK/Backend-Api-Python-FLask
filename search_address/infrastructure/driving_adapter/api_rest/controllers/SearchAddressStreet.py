from typing import Type
from httpx import Request, Response
from shared.errors import HttpErrors
import json

class SearchAddressStreetController:

    def __init__(self, dataframe):
        self.df = dataframe

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

            if (
                "departamento" in body_params
                and "provincia" in body_params
                and "distrito" in body_params
                and "direccion" in body_params
                and "numpuerta" in body_params
            ):
                data_search =  {
                    "departamento" : http_request.json['departamento'].upper(),
                    "provincia" : http_request.json["provincia"].upper(),
                    "distrito" : http_request.json["distrito"].upper(),
                    "direccion" : http_request.json["direccion"].upper(),
                    "numpuerta" : http_request.json["numpuerta"]
                }
                                
                result_data = self.df.search.address_street(http_request.json['departamento'].upper(), http_request.json["provincia"].upper(), http_request.json["distrito"].upper(), http_request.json["direccion"].upper(), http_request.json["numpuerta"]).to_pandas_df()
                json_data = result_data.to_json(orient='records')

                return self.success_response("data", {"data_search":json.loads(json_data)})
            else:
                return self.bad_request("Todos los campos son requeridos.")
                
            
        except Exception as e:
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
