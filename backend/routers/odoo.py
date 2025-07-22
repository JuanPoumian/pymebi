from fastapi import APIRouter, HTTPException
from backend.connectors.odoo_connector import OdooConnector
from backend.schemas.odoo import OdooConnection, OdooFetchRequest

router = APIRouter(
    prefix="/odoo",
    tags=["odoo"],
)

@router.post("/test-connection/")
def test_odoo_connection(conn: OdooConnection):
    connector = OdooConnector(conn.url, conn.db, conn.username, conn.password)
    if connector.test_connection():
        return {"status": "success", "message": "Conexión exitosa con Odoo"}
    else:
        raise HTTPException(status_code=400, detail="No se pudo conectar con Odoo")

@router.post("/fetch-data/")
def fetch_odoo_data(request: OdooFetchRequest):
    connector = OdooConnector(request.url, request.db, request.username, request.password)
    data = connector.fetch_data(request.model, request.fields)
    return {"data": data}
