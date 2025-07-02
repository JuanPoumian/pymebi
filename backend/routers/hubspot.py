from fastapi import APIRouter

router = APIRouter(prefix="/conectores/hubspot", tags=["hubspot"])

@router.post("/test_connection")
async def test_connection(data: dict):
    # Aquí va la lógica real de conexión, pero ahora solo simulamos
    return {"ok": True, "mensaje": "Conexión a HubSpot exitosa."}

@router.post("/fetch_data")
async def fetch_data(data: dict):
    # Aquí va la lógica real para traer datos de HubSpot
    return [{"id": 1, "dato": "Dato HubSpot"}]

@router.post("/get_schema")
async def get_schema(data: dict):
    return ["id", "dato"]
