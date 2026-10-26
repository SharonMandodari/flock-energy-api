from fastapi import FastAPI, HTTPException
from app.client import UrjaPortalClient

app = FastAPI(
    title="Flock Energy - Urja Meter Ops API",
    version="1.0.0"
)

client = UrjaPortalClient("https://urja-ops.flockenergy.tech")

@app.get("/api/v1/meters/{meter_id}")
def get_meter(meter_id: str):
    try:
        return client.get_meter_details(meter_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/v1/meters/{meter_id}/consumption")
def get_meter_consumption(meter_id: str):
    try:
        return client.get_meter_consumption(meter_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))