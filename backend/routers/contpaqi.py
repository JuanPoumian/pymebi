from fastapi import APIRouter, HTTPException
from backend.connectors.contpaqi_connector import ContpaqiConnector
from backend.schemas.contpaqi import ContpaqiConnection, ContpaqiQueryRequest

router = APIRouter(
    prefix="/contpaqi",
    tags=["contpaqi"],
)

@router.post("/test-connection/")
def test_contpaqi_connection(conn: ContpaqiConnection):
    connector = ContpaqiConnector(conn.host, conn.username, conn.password, conn.database)
    if connector.test_connection():
        return {"status": "success", "message": "Conexión exitosa con Contpaqi"}
    else:
        raise HTTPException(status_code=400, detail="No se pudo conectar con Contpaqi")

@router.post("/execute/")
def execute_contpaqi_query(request: ContpaqiQueryRequest):
    connector = ContpaqiConnector(request.host, request.username, request.password, request.database)
    data = connector.execute_query(request.query, request.params)
    return {"data": data}
