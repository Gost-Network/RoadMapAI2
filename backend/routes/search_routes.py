from flask import Blueprint, request
from backend.controllers.search_controller import search_location

search_bp = Blueprint(
    "search_bp",
    __name__
)

@search_bp.route(
    "/search",
    methods=["POST"]
)
def search():

    data = request.get_json()

    return search_location(data)