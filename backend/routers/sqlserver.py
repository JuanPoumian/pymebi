from fastapi import APIRouter, HTTPException
from backend.connectors.sqlserver_connector import SQLServerConnector
from backend.schemas.sqlserver import SQLServerConnection, SQLServerQueryRequest

router = APIRouter(
    prefix="/sqlserver",
    tags=["sqlserver"],
)

@router.post("/test-connection/")
def test_sqlserver_connection(conn: SQLServerConnection):
    connector = SQLServerConnector(conn.host, conn.port, conn.database, conn.username, conn.password)
    if connector.test_connection():
        return {"status": "success", "message": "Conexión exitosa con SQL Server"}
    else:
        raise HTTPException(status_code=400, detail="No se pudo conectar con SQL Server")

@router.post("/execute/")
def execute_sqlserver_query(request: SQLServerQueryRequest):
    connector = SQLServerConnector(request.host, request.port, request.database, request.username, request.password)
    data = connector.execute_query(request.query, request.params)
    return {"data": data}
