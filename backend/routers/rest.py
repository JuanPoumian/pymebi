from fastapi import APIRouter, HTTPException
from backend.connectors.rest_connector import RESTConnector
from backend.schemas.rest import RESTConnection, RESTFetchRequest

router = APIRouter(
    prefix="/rest",
    tags=["rest"],
)

@router.post("/test-connection/")
def test_rest_connection(conn: RESTConnection):
    connector = RESTConnector(conn.url, conn.headers)
    if connector.test_connection():
        return {"status": "success", "message": "Conexión exitosa con REST API"}
    else:
        raise HTTPException(status_code=400, detail="No se pudo conectar con REST API")

@router.post("/fetch-data/")
def fetch_rest_data(request: RESTFetchRequest):
    connector = RESTConnector(request.url, request.headers)
    data = connector.fetch_data(request.endpoint, request.method, request.params, request.body)
    return {"data": data}
