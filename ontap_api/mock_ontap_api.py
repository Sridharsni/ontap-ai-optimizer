# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime, date
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class VolumeExpansionRequest(BaseModel):
    volume_id: str
    size_to_add: int

volume_state = {
    "vol-001": {
        "total_gb": 150,
        "last_expansion_day": None,
        "expansion_history": []
    }
}

@app.post("/expand_volume")
def expand_volume(req: VolumeExpansionRequest):
    vol = volume_state.get(req.volume_id)
    today = datetime.now().date()

    if vol["last_expansion_day"] == today:
        return {"message": "Already expanded today."}

    vol["total_gb"] += req.size_to_add
    vol["last_expansion_day"] = today
    vol["expansion_history"].append({"timestamp": datetime.now().isoformat(), "size": req.size_to_add})

    return {"message": f"Expanded by {req.size_to_add}GB", "new_total": vol["total_gb"]}

@app.get("/monitor")
def get_monitor_data():
    df = pd.read_csv("usage_log.csv")
    return {
        "timestamps": df["timestamp"].tolist(),
        "used_gb": df["used_gb"].tolist(),
        "total_gb": volume_state["vol-001"]["total_gb"],
        "threshold": 0.8 * volume_state["vol-001"]["total_gb"],
        "expansion_events": volume_state["vol-001"]["expansion_history"],
        "last_expansion_day": str(volume_state["vol-001"]["last_expansion_day"])
    }
