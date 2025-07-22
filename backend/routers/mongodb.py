from fastapi import APIRouter, HTTPException
from backend.connectors.mongodb_connector import MongoDBConnector
from backend.schemas.mongodb import MongoDBConnection, MongoDBFetchRequest

router = APIRouter(
    prefix="/mongodb",
    tags=["mongodb"],
)

@router.post("/test-connection/")
def test_mongodb_connection(conn: MongoDBConnection):
    connector = MongoDBConnector(conn.uri, conn.database)
    if connector.test_connection():
        return {"status": "success", "message": "Conexión exitosa con MongoDB"}
    else:
        raise HTTPException(status_code=400, detail="No se pudo conectar con MongoDB")

@router.post("/fetch-data/")
def fetch_mongodb_data(request: MongoDBFetchRequest):
    connector = MongoDBConnector(request.uri, request.database)
    data = connector.fetch_data(request.collection, request.filter)
    return {"data": data}
