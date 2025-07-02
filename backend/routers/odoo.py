from fastapi import APIRouter

router = APIRouter(prefix="/conectores/odoo", tags=["odoo"])

@router.post("/test_connection")
async def test_connection(data: dict):
    return {"ok": True, "mensaje": "Conexión a Odoo exitosa."}

@router.post("/fetch_data")
async def fetch_data(data: dict):
    return [{"id": 1, "dato": "Dato Odoo"}]

@router.post("/get_schema")
async def get_schema(data: dict):
    return ["id", "dato"]
