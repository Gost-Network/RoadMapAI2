import requests

response = requests.post(
    "http://127.0.0.1:5000/safety",
    json={
        "route": {
            "source": "Dahanu",
            "destination": "Boisar"
        }
    }
)

print(response.status_code)
print(response.json())