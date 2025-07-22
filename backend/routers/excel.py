from fastapi import APIRouter, HTTPException
from backend.connectors.excel_connector import ExcelConnector
from backend.schemas.excel import ExcelConnection, ExcelFetchRequest

router = APIRouter(
    prefix="/excel",
    tags=["excel"],
)

@router.post("/fetch-data/")
def fetch_excel_data(request: ExcelFetchRequest):
    connector = ExcelConnector(request.file_path, request.sheet_name)
    data = connector.fetch_data(request.fields)
    return {"data": data}
