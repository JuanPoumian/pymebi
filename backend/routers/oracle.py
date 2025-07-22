from fastapi import APIRouter, HTTPException
from backend.connectors.oracle_connector import OracleConnector
from backend.schemas.oracle import OracleConnection, OracleQueryRequest

router = APIRouter(
    prefix="/oracle",
    tags=["oracle"],
)

@router.post("/test-connection/")
def test_oracle_connection(conn: OracleConnection):
    connector = OracleConnector(conn.host, conn.port, conn.service_name, conn.username, conn.password)
    if connector.test_connection():
        return {"status": "success", "message": "Conexión exitosa con Oracle"}
    else:
        raise HTTPException(status_code=400, detail="No se pudo conectar con Oracle")

@router.post("/execute/")
def execute_oracle_query(request: OracleQueryRequest):
    connector = OracleConnector(request.host, request.port, request.service_name, request.username, request.password)
    data = connector.execute_query(request.query, request.params)
    return {"data": data}
