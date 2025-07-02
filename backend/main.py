# backend/main.py

from fastapi import FastAPI

# Importa TODOS los routers de tus conectores
from backend.routers import (
    odoo,
    hubspot,
    rest,
    sqlserver,
    mysql,
    postgresql,
    mongodb,
    oracle,
    sap,
    bigquery,
    google_sheets,
    airtable,
    contpaqi,
    excel,
    # Agrega aquí otros conectores personalizados si necesitas
)

app = FastAPI(
    title="PymeBI API",
    description="API profesional para gestionar múltiples conectores",
    version="1.0.0"
)

# Incluye cada router
app.include_router(odoo.router)
app.include_router(hubspot.router)
app.include_router(rest.router)
app.include_router(sqlserver.router)
app.include_router(mysql.router)
app.include_router(postgresql.router)
app.include_router(mongodb.router)
app.include_router(oracle.router)
app.include_router(sap.router)
app.include_router(bigquery.router)
app.include_router(google_sheets.router)
app.include_router(airtable.router)
app.include_router(contpaqi.router)
app.include_router(excel.router)

# Ruta raíz opcional
@app.get("/")
async def root():
    return {"mensaje": "Bienvenido a PymeBI API. Consulta la documentación en /docs"}
