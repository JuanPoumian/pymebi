from fastapi import APIRouter, HTTPException
from backend.connectors.airtable_connector import AirtableConnector
from backend.schemas.airtable import AirtableConnection, AirtableFetchRequest

router = APIRouter(
    prefix="/airtable",
    tags=["airtable"],
)

@router.post("/test-connection/")
def test_airtable_connection(conn: AirtableConnection):
    connector = AirtableConnector(conn.api_key, conn.base_id)
    if connector.test_connection():
        return {"status": "success", "message": "Conexión exitosa con Airtable"}
    else:
        raise HTTPException(status_code=400, detail="No se pudo conectar con Airtable")

@router.post("/fetch-data/")
def fetch_airtable_data(request: AirtableFetchRequest):
    connector = AirtableConnector(request.api_key, request.base_id)
    data = connector.fetch_data(request.table, request.fields, request.filters)
    return {"data": data}
