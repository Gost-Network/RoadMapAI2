async function searchPlace(placeName) {

    try {

        const response = await fetch("/search", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                place: placeName
            })

        });

        const data = await response.json();

        return data;

    }

    catch (error) {

        console.error(error);

        return null;

    }

}