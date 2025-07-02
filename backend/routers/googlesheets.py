from fastapi import APIRouter

router = APIRouter(
    prefix="/conectores/googlesheets",
    tags=["googlesheets"]
)

@router.post("/test_connection")
async def test_connection(data: dict):
    return {"ok": True, "mensaje": "Conexión a Google Sheets exitosa."}

@router.post("/fetch_data")
async def fetch_data(data: dict):
    return [{"id": 1, "dato": "Dato Google Sheets"}]

@router.post("/get_schema")
async def get_schema(data: dict):
    return ["id", "dato"]
