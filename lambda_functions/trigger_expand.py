# monitor_trigger.py
import pandas as pd
import numpy as np
import requests
from datetime import datetime
from sklearn.linear_model import LinearRegression

CSV_PATH = "usage_log.csv"
TOTAL_CAPACITY = 150
EXPANSION_SIZE = 50
LAST_EXPANSION_DAY = None
CURRENT_DAY = datetime(2024, 6, 4).date()

def should_expand_volume(df, total_capacity, last_expansion_day, current_day):
    if last_expansion_day == current_day:
        return False

    X = df["day_count"].values.reshape(-1, 1)
    y = df["used_gb"].values

    model = LinearRegression()
    model.fit(X, y)

    last_day = df["day_count"].max()
    future_days = np.array([last_day + i for i in range(1, 4)]).reshape(-1, 1)
    predictions = model.predict(future_days)

    if np.max(predictions) > 0.8 * total_capacity:
        return True
    return False

def run_monitor():
    global LAST_EXPANSION_DAY
    df = pd.read_csv(CSV_PATH)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    if should_expand_volume(df, TOTAL_CAPACITY, LAST_EXPANSION_DAY, CURRENT_DAY):
        response = requests.post("http://localhost:8000/expand_volume", json={
            "volume_id": "vol-001",
            "size_to_add": EXPANSION_SIZE
        })
        print("Expansion triggered:", response.json())
        LAST_EXPANSION_DAY = CURRENT_DAY
    else:
        print("No expansion needed today.")

if __name__ == "__main__":
    run_monitor()
