import pandas as pd

files = [
    "data/Accident_data_india.csv",
    "data/accident_prediction_india.csv",
    "data/indian_roads_dataset.csv"
]

for file in files:

    print("\n" + "="*50)
    print(file)
    print("="*50)

    df = pd.read_csv(file)

    print(df.columns.tolist())
   