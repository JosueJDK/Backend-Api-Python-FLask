from typing import Type

from shared.errors import HttpErrors
from shared.interfaces import RouteInterface as Route
from httpx import Request, Response

async def flask_adapter(request: Type[Request], api_route: Type[Route]) -> any:
    try:
        response = await api_route.route(request)
    except:
        https_error = HttpErrors.error_500()
        return Response(
            status_code=https_error["status_code"], json=https_error["body"]
        )
    return response
