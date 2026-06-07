from flask import jsonify
from backend.services.route_service import generate_route


def get_route(data):

    source = data.get("source")
    destination = data.get("destination")

    if not source or not destination:

        return jsonify({
            "success": False,
            "message": "Source and Destination are required"
        }), 400

    result = generate_route(
        source,
        destination
    )

    return jsonify(result)