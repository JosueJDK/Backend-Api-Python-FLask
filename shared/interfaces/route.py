from typing import Type
from abc import ABC, abstractmethod
from httpx import Request, Response

class RouteInterface(ABC):
    @abstractmethod
    def route(self, http_request: Type[Request]) -> Response:
        raise Exception("Should implement method: route")