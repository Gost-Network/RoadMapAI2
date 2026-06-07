from flask import Blueprint, request
from backend.controllers.route_controller import get_route

route_bp = Blueprint(
    "route_bp",
    __name__
)

@route_bp.route(
    "/route",
    methods=["POST"]
)
def route():

    data = request.get_json()

    return get_route(data)