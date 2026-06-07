import pandas as pd


def load_dataset(file_path):

    df = pd.read_csv(file_path)

    return df


def clean_dataset(df):

    df = df.dropna()

    df = df.drop_duplicates()

    return df