import requests

API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6ImUyMjRhYzJjZDAxZTQzYWU5N2NlOTIyNmRmM2ExNzgwIiwiaCI6Im11cm11cjY0In0="


def generate_route(
    source_lat,
    source_lon,
    destination_lat,
    destination_lon
):

    try:

        headers = {

            "Authorization":
            API_KEY,

            "Content-Type":
            "application/json"

        }

        body = {

            "coordinates": [

                [
                    float(source_lon),
                    float(source_lat)
                ],

                [
                    float(destination_lon),
                    float(destination_lat)
                ]

            ]

        }

        response = requests.post(

            "https://api.openrouteservice.org/v2/directions/driving-car/geojson",

            json=body,

            headers=headers,

            timeout=20

        )

        data = response.json()

        print(
            "ROUTE RESPONSE:",
            data
        )

        if "features" not in data:

            return {

                "success": False,

                "message":
                str(data)

            }

        steps = data[
            "features"
        ][0][
            "properties"
        ][
            "segments"
        ][0][
            "steps"
        ]

        instructions = []

        for step in steps:

            instructions.append({

                "instruction":
                step["instruction"],

                "distance":
                round(
                    step["distance"],
                    0
                )

            })

        geometry = data[
            "features"
        ][0][
            "geometry"
        ][
            "coordinates"
        ]

        route_coordinates = []

        for point in geometry:

            route_coordinates.append({

                "lat":
                point[1],

                "lon":
                point[0]

            })

        summary = data[
            "features"
        ][0][
            "properties"
        ][
            "summary"
        ]

        distance_km = round(

            summary[
                "distance"
            ] / 1000,

            2

        )

        eta_minutes = round(

            summary[
                "duration"
            ] / 60,

            0

        )

        return {

            "success": True,

            "distance_km":
            distance_km,

            "eta_minutes":
            eta_minutes,

            "route":
            route_coordinates,

            "instructions":
            instructions

        }

    except Exception as e:

        print(
            "ROUTE ERROR:",
            e
        )

        return {

            "success": False,

            "message":
            str(e)

        }