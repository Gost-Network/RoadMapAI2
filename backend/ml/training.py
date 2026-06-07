import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import joblib

df = pd.read_csv(
    "data/indian_roads_dataset.csv"
)

categorical_columns = [

    "road_type",
    "weather",
    "traffic_density"

]

encoders = {}

for column in categorical_columns:

    encoder = LabelEncoder()

    df[column] = encoder.fit_transform(
        df[column].astype(str)
    )

    encoders[column] = encoder

features = [

    "road_type",
    "weather",
    "traffic_density",
    "hour",
    "is_weekend",
    "is_peak_hour"

]

target = "risk_score"

X = df[features]

y = df[target]

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,
    test_size=0.2,
    random_state=42

)

model = RandomForestRegressor(

    n_estimators=100,
    random_state=42

)

model.fit(
    X_train,
    y_train
)

joblib.dump(
    model,
    "models/risk_model.pkl"
)

joblib.dump(
    encoders,
    "models/encoders.pkl"
)

print(
    "Model Trained Successfully"
)