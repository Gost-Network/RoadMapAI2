console.log("Road Map AI Loaded");

let currentLat = null;
let currentLon = null;

let map = L.map("map").setView([19.0760, 72.8777], 11);

L.tileLayer(
    "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    {
        maxZoom: 19,
        attribution: "© OpenStreetMap"
    }
).addTo(map);

let currentMarker = null;
let destinationMarker = null;
let routeLine = null;

if (navigator.geolocation) {

    navigator.geolocation.getCurrentPosition(

        function (position) {

            currentLat = position.coords.latitude;
            currentLon = position.coords.longitude;

            console.log(
                "Location:",
                currentLat,
                currentLon
            );

            map.setView(
                [currentLat, currentLon],
                15
            );

            currentMarker = L.marker(
                [currentLat, currentLon]
            )
            .addTo(map)
            .bindPopup("📍 Current Location")
            .openPopup();

        },

        function (error) {

            console.log(error);

            alert(
                "Location Permission Required"
            );

        }

    );

}

document
.getElementById("routeBtn")
.addEventListener(
    "click",
    findRoute
);

async function findRoute() {

    const destination =
        document
        .getElementById("destination")
        .value
        .trim();

    if (destination === "") {

        alert(
            "Please Enter Destination"
        );

        return;
    }

    if (currentLat === null) {

        alert(
            "Waiting For GPS Location"
        );

        return;
    }

    try {

        const response = await fetch(
            "/search",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    place: destination
                })
            }
        );

        const data =
            await response.json();

        if (!data.success) {

            alert(
                "Location Not Found"
            );

            return;
        }

        const destLat =
            data.latitude;

        const destLon =
            data.longitude;

        if (destinationMarker) {

            map.removeLayer(
                destinationMarker
            );

        }

        destinationMarker =
            L.marker(
                [destLat, destLon]
            )
            .addTo(map)
            .bindPopup(destination);

        if (routeLine) {

            map.removeLayer(
                routeLine
            );

        }

        routeLine =
            L.polyline(
                [
                    [currentLat, currentLon],
                    [destLat, destLon]
                ],
                {
                    weight: 5
                }
            )
            .addTo(map);

        map.fitBounds(
            routeLine.getBounds()
        );

    }

    catch (error) {

        console.log(error);

        alert(
            "Route Generation Failed"
        );

    }

}