async function getSafetyScore(routeData) {

    try {

        const response = await fetch("/safety", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                route: routeData
            })

        });

        const data = await response.json();

        if (data.success) {

            document.getElementById("score").innerText =
                data.safety_score;

            document.getElementById("risk").innerText =
                data.risk_level;

        }

        return data;

    }

    catch (error) {

        console.error(error);

    }

}