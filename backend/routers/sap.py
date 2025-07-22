from fastapi import APIRouter, HTTPException
from backend.connectors.sap_connector import SAPConnector
from backend.schemas.sap import SAPConnection, SAPFetchRequest

router = APIRouter(
    prefix="/sap",
    tags=["sap"],
)

@router.post("/test-connection/")
def test_sap_connection(conn: SAPConnection):
    connector = SAPConnector(conn.host, conn.username, conn.password, conn.client, conn.lang)
    if connector.test_connection():
        return {"status": "success", "message": "Conexión exitosa con SAP"}
    else:
        raise HTTPException(status_code=400, detail="No se pudo conectar con SAP")

@router.post("/fetch-data/")
def fetch_sap_data(request: SAPFetchRequest):
    connector = SAPConnector(request.host, request.username, request.password, request.client, request.lang)
    data = connector.fetch_data(request.table, request.fields, request.filters)
    return {"data": data}
