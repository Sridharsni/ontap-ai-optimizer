from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # ✅ ADD THIS
from pydantic import BaseModel

app = FastAPI()

# ✅ CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # or ["*"] to allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dummy in-memory volume DB
db = {
    "volumes": [
        {"uuid": "vol-1", "name": "volume1", "size": 1000000000},
        {"uuid": "vol-2", "name": "volume2", "size": 2000000000}
    ]
}

class VolumeUpdate(BaseModel):
    size: int

@app.get("/api/storage/volumes")
def get_volumes():
    return {"records": db["volumes"]}

@app.patch("/api/storage/volumes/{volume_uuid}")
def update_volume(volume_uuid: str, body: VolumeUpdate):
    for vol in db["volumes"]:
        if vol["uuid"] == volume_uuid:
            vol["size"] = body.size
            return {"status": "updated", "volume": vol}
    raise HTTPException(status_code=404, detail="Volume not found")
