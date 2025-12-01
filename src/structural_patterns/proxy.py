from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Request:
    ip: str
    headers: dict
    body: dict


class Controller(ABC):
    @abstractmethod
    def get(self, request: Request) -> dict:
        pass

class MovieController(Controller):
    def get(self, request: Request) -> dict:
        print(f"Making a request with the following headers and body. HEADERS: {request.headers}; BODY: {request.body}")
        return {"status_code": 200, "message": "Retrieving movie ..."}

class ProxyMovieController(Controller):
    __ALLOWED_IPS = ["217.111.217.82"]
    def __init__(self, movie_controller: MovieController):
        self.__movie_controller = movie_controller

    def get(self, request: Request) -> dict:
        if self.__ip_is_allowed(request.ip):
            return self.__movie_controller.get(request)

        return {"status_code": 401, "message": "IP not allowed"}

    def __ip_is_allowed(self, ip: str) -> bool:
        return ip in self.__ALLOWED_IPS

def client_code(controller: Controller) -> dict:
    print("\n--- AUTHORIZED REQUEST ---")
    authorized_request = Request(ip="217.111.217.82", headers={"test": True}, body={"movie_id": 297})
    print(controller.get(authorized_request))

    print("\n--- UNAUTHORIZED REQUEST ---")
    unauthorized_request = Request(ip="647.349.038.86", headers={"test": True}, body={"movie_id": 297})
    print(controller.get(unauthorized_request))

if __name__ == "__main__":
    print("\n==============================")
    print("CLIENT USING REAL CONTROLLER")
    print("==============================")
    real_controller = MovieController()
    client_code(real_controller)

    print("\n==============================")
    print("CLIENT USING PROXY CONTROLLER")
    print("==============================")
    proxy_controller = ProxyMovieController(real_controller)
    client_code(proxy_controller)
