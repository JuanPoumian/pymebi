from fastapi import APIRouter, HTTPException
from backend.connectors.postgresql_connector import PostgreSQLConnector
from backend.schemas.postgresql import PostgreSQLConnection, PostgreSQLQueryRequest

router = APIRouter(
    prefix="/postgresql",
    tags=["postgresql"],
)

@router.post("/test-connection/")
def test_postgresql_connection(conn: PostgreSQLConnection):
    connector = PostgreSQLConnector(conn.host, conn.port, conn.database, conn.username, conn.password)
    if connector.test_connection():
        return {"status": "success", "message": "Conexión exitosa con PostgreSQL"}
    else:
        raise HTTPException(status_code=400, detail="No se pudo conectar con PostgreSQL")

@router.post("/execute/")
def execute_postgresql_query(request: PostgreSQLQueryRequest):
    connector = PostgreSQLConnector(request.host, request.port, request.database, request.username, request.password)
    data = connector.execute_query(request.query, request.params)
    return {"data": data}
