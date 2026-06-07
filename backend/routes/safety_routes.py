from flask import Blueprint, request
from backend.controllers.safety_controller import get_safety_score

safety_bp = Blueprint(
    "safety_bp",
    __name__
)

@safety_bp.route(
    "/safety",
    methods=["POST"]
)
def safety():

    data = request.get_json()

    return get_safety_score(data)