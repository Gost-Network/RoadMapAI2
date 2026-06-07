import joblib
import pandas as pd

model = joblib.load(
    "models/risk_model.pkl"
)

encoders = joblib.load(
    "models/encoders.pkl"
)

def calculate_safety(route_data):

    try:

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

        prediction = float(
            model.predict(df)[0]
        )

        safety_score = round(
            (1 - prediction) * 100,
            2
        )

        if safety_score >= 70:

            risk = "Low"

        elif safety_score >= 40:

            risk = "Medium"

        else:

            risk = "High"

        return {

            "success": True,

            "safety_score":
            safety_score,

            "risk_level":
            risk

        }

    except Exception as e:

        return {

            "success": False,

            "message": str(e)

        }