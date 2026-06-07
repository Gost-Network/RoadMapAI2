import joblib
import pandas as pd

# Load Model
model = joblib.load(
    "models/risk_model.pkl"
)

# Load Encoders
encoders = joblib.load(
    "models/encoders.pkl"
)

def predict_risk():

    sample = {

        "road_type": "highway",
        "weather": "clear",
        "traffic_density": "low",
        "hour": 14,
        "is_weekend": 0,
        "is_peak_hour": 0

    }

    sample["road_type"] = (
        encoders["road_type"]
        .transform(
            [sample["road_type"]]
        )[0]
    )

    sample["weather"] = (
        encoders["weather"]
        .transform(
            [sample["weather"]]
        )[0]
    )

    sample["traffic_density"] = (
        encoders["traffic_density"]
        .transform(
            [sample["traffic_density"]]
        )[0]
    )

    df = pd.DataFrame(
        [sample]
    )

    prediction = model.predict(
        df
    )[0]

    print(
        "\nRisk Score:",
        round(prediction, 2)
    )

    if prediction < 35:

        print(
            "Risk Level: Low"
        )

    elif prediction < 70:

        print(
            "Risk Level: Medium"
        )

    else:

        print(
            "Risk Level: High"
        )

predict_risk()