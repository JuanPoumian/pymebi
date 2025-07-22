from fastapi import APIRouter, HTTPException
from backend.connectors.google_sheets_connector import GoogleSheetsConnector
from backend.schemas.googlesheets import GoogleSheetsConnection, GoogleSheetsFetchRequest

router = APIRouter(
    prefix="/google-sheets",
    tags=["google-sheets"],
)

@router.post("/test-connection/")
def test_google_sheets_connection(conn: GoogleSheetsConnection):
    connector = GoogleSheetsConnector(conn.credentials_json, conn.spreadsheet_id)
    if connector.test_connection():
        return {"status": "success", "message": "Conexión exitosa con Google Sheets"}
    else:
        raise HTTPException(status_code=400, detail="No se pudo conectar con Google Sheets")

@router.post("/fetch-data/")
def fetch_google_sheets_data(request: GoogleSheetsFetchRequest):
    connector = GoogleSheetsConnector(request.credentials_json, request.spreadsheet_id)
    data = connector.fetch_data(request.range, request.major_dimension)
    return {"data": data}
