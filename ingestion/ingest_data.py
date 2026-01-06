import pandas as pd
from pathlib import Path

def load_data():
    data_path = Path("data/sample_flights.csv")
    df = pd.read_csv(data_path)
    print("Data loaded successfully!")
    print(df.head())
    return df

if __name__ == "__main__":
    load_data()
