from fastapi import APIRouter, HTTPException
from backend.connectors.bigquery_connector import BigQueryConnector
from backend.schemas.bigquery import BigQueryConnection, BigQueryQueryRequest

router = APIRouter(
    prefix="/bigquery",
    tags=["bigquery"],
)

@router.post("/test-connection/")
def test_bigquery_connection(conn: BigQueryConnection):
    connector = BigQueryConnector(conn.credentials_json, conn.project_id)
    if connector.test_connection():
        return {"status": "success", "message": "Conexión exitosa con BigQuery"}
    else:
        raise HTTPException(status_code=400, detail="No se pudo conectar con BigQuery")

@router.post("/execute/")
def execute_bigquery_query(request: BigQueryQueryRequest):
    connector = BigQueryConnector(request.credentials_json, request.project_id)
    data = connector.execute_query(request.query, request.params)
    return {"data": data}
