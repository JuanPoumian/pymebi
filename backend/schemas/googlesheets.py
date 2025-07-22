from pydantic import BaseModel
from typing import Optional, List

class GoogleSheetsConnection(BaseModel):
    credentials_json: str
    spreadsheet_id: str

class GoogleSheetsFetchRequest(GoogleSheetsConnection):
    range: str
    major_dimension: Optional[str] = "ROWS"
