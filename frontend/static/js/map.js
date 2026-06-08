console.log("Road Map AI Loaded");

let currentLat = null;
let currentLon = null;

let map = L.map("map").setView(
    [19.0760, 72.8777],
    11
);

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

        function(position) {

            currentLat = position.coords.latitude;
            currentLon = position.coords.longitude;

            console.log(
                "GPS SUCCESS:",
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
            .bindPopup(
                "📍 Current Location"
            )
            .openPopup();

        },

        function(error) {

            console.log(
                "GPS ERROR:",
                error
            );

            alert(
                "GPS Error: " +
                error.message
            );

        },

        {
            enableHighAccuracy: true,
            timeout: 10000,
            maximumAge: 0
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

    if (
        currentLat === null ||
        currentLon === null
    ) {

        alert(
            "GPS Location Not Ready"
        );

        return;
    }

    try {

        const response =
            await fetch(
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
            .bindPopup(
                destination
            );

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

        const distance =
            (
                Math.sqrt(
                    Math.pow(
                        destLat -
                        currentLat,
                        2
                    ) +
                    Math.pow(
                        destLon -
                        currentLon,
                        2
                    )
                ) * 111
            ).toFixed(2);

        const eta =
            Math.round(
                (
                    parseFloat(
                        distance
                    ) / 40
                ) * 60
            );

        document.getElementById(
            "distance"
        ).innerText =
            distance + " KM";

        document.getElementById(
            "eta"
        ).innerText =
            eta + " Min";

        try {

            const safetyResponse =
                await fetch(
                    "/safety",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                            "application/json"
                        },

                        body: JSON.stringify({
                            route: {
                                source_lat:
                                currentLat,

                                source_lon:
                                currentLon,

                                destination_lat:
                                destLat,

                                destination_lon:
                                destLon
                            }
                        })
                    }
                );

            const safetyData =
                await safetyResponse.json();

            if (
                safetyData.success
            ) {

                document.getElementById(
                    "score"
                ).innerText =
                    safetyData.safety_score;

                document.getElementById(
                    "risk"
                ).innerText =
                    safetyData.risk_level;

            }

        }

        catch(error) {

            console.log(
                "Safety Error:",
                error
            );

        }

        alert(
            "Route Generated Successfully"
        );

    }

    catch(error) {

        console.log(
            "Route Error:",
            error
        );

        alert(
            "Route Generation Failed"
        );

    }

}