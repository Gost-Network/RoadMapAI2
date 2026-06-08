from geopy.geocoders import Nominatim

geolocator = Nominatim(
    user_agent="road_map_ai"
)

def get_location(place):

    try:

        location = geolocator.geocode(
            place
        )

        print(
            "SEARCH:",
            place
        )

        print(
            "RESULT:",
            location
        )

        if location:

            return {

                "success": True,

                "place":
                place,

                "latitude":
                location.latitude,

                "longitude":
                location.longitude,

                "address":
                location.address

            }

        return {

            "success": False,

            "message":
            "Location Not Found"

        }

    except Exception as e:

        return {

            "success": False,

            "message":
            str(e)

        }