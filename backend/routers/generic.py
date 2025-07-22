from fastapi import APIRouter, HTTPException
from backend.connectors.generic_connector import GenericConnector
from backend.schemas.generic import GenericConnection, GenericFetchRequest

router = APIRouter(
    prefix="/generic",
    tags=["generic"],
)

@router.post("/test-connection/")
def test_generic_connection(conn: GenericConnection):
    connector = GenericConnector(conn.url, conn.username, conn.password, conn.api_key)
    if connector.test_connection():
        return {"status": "success", "message": "Conexión exitosa con el sistema genérico"}
    else:
        raise HTTPException(status_code=400, detail="No se pudo conectar")

@router.post("/fetch-data/")
def fetch_generic_data(request: GenericFetchRequest):
    connector = GenericConnector(request.url, request.username, request.password, request.api_key)
    data = connector.fetch_data(request.resource, request.method, request.params, request.body)
    return {"data": data}
