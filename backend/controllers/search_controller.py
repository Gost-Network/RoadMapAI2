from flask import jsonify
from backend.services.search_service import get_location


def search_location(data):

    place = data.get("place")

    if not place:
        return jsonify({
            "success": False,
            "message": "Place is required"
        }), 400

    result = get_location(place)

    return jsonify(result)