import requests
import pandas as pd
from datetime import datetime

def run_etl():
    print("Extracting data...")
    url = "https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&hourly=temperature_2m"
    response = requests.get(url)
    data = response.json()

    print("Transforming data...")
    df = pd.DataFrame()
    df['time'] = data['hourly']['time']
    df['temperature_c'] = data['hourly']['temperature_2m']
    df['processed_at'] = datetime.now()
    df = df.dropna()

    print("Loading data...")
    output_file = 'weather_data.csv'
    df.to_csv(output_file, index=False)
    print(f"Success! Data saved to {output_file}")

if __name__ == "__main__":
    run_etl()