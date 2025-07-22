from fastapi import APIRouter, HTTPException
from backend.connectors.mysql_connector import MySQLConnector
from backend.schemas.mysql import MySQLConnection, MySQLQueryRequest

router = APIRouter(
    prefix="/mysql",
    tags=["mysql"],
)

@router.post("/test-connection/")
def test_mysql_connection(conn: MySQLConnection):
    connector = MySQLConnector(conn.host, conn.port, conn.database, conn.username, conn.password)
    if connector.test_connection():
        return {"status": "success", "message": "Conexión exitosa con MySQL"}
    else:
        raise HTTPException(status_code=400, detail="No se pudo conectar con MySQL")

@router.post("/execute/")
def execute_mysql_query(request: MySQLQueryRequest):
    connector = MySQLConnector(request.host, request.port, request.database, request.username, request.password)
    data = connector.execute_query(request.query, request.params)
    return {"data": data}
