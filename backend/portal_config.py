from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.db import get_db_connection

router = APIRouter()

class PortalConfig(BaseModel):
    client_id: str
    client_secret1: str
    client_secret2: str
    taxpayer_name: str
    taxpayer_registration: str
    taxpayer_address: str

@router.post("/portal-config")
async def save_portal_config(config: PortalConfig):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM portal_config")
    cursor.execute(
        "INSERT INTO portal_config (client_id, client_secret1, client_secret2, taxpayer_name, taxpayer_registration, taxpayer_address) VALUES (?, ?, ?, ?, ?, ?)",
        (config.client_id, config.client_secret1, config.client_secret2, config.taxpayer_name, config.taxpayer_registration, config.taxpayer_address)
    )
    conn.commit()
    conn.close()
    return {"message": "Portal configuration saved"}

@router.get("/portal-config")
async def get_portal_config():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM portal_config LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Portal configuration not found")
    return {
        "client_id": row["client_id"],
        "client_secret1": row["client_secret1"],
        "client_secret2": row["client_secret2"],
        "taxpayer_name": row["taxpayer_name"],
        "taxpayer_registration": row["taxpayer_registration"],
        "taxpayer_address": row["taxpayer_address"],
    }
