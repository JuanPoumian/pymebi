from fastapi import APIRouter, HTTPException
from backend.connectors.hubspot_connector import HubSpotConnector
from backend.schemas.hubspot import HubSpotConnection, HubSpotFetchRequest

router = APIRouter(
    prefix="/hubspot",
    tags=["hubspot"],
)

@router.post("/test-connection/")
def test_hubspot_connection(conn: HubSpotConnection):
    connector = HubSpotConnector(conn.api_key)
    if connector.test_connection():
        return {"status": "success", "message": "Conexión exitosa con HubSpot"}
    else:
        raise HTTPException(status_code=400, detail="No se pudo conectar con HubSpot")

@router.post("/fetch-data/")
def fetch_hubspot_data(request: HubSpotFetchRequest):
    connector = HubSpotConnector(request.api_key)
    data = connector.fetch_data(request.endpoint, request.params)
    return {"data": data}
