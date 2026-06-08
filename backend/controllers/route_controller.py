from flask import jsonify
from backend.services.route_service import generate_route


def get_route(data):

    source_lat = data.get(
        "source_lat"
    )

    source_lon = data.get(
        "source_lon"
    )

    destination_lat = data.get(
        "destination_lat"
    )

    destination_lon = data.get(
        "destination_lon"
    )

    if (
        source_lat is None or
        source_lon is None or
        destination_lat is None or
        destination_lon is None
    ):

        return jsonify({

            "success": False,

            "message":
            "Coordinates are required"

        }), 400

    result = generate_route(

        source_lat,
        source_lon,

        destination_lat,
        destination_lon

    )

    return jsonify(result)