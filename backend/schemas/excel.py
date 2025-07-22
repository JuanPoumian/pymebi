from pydantic import BaseModel
from typing import Optional, List

class ExcelConnection(BaseModel):
    file_path: str

class ExcelFetchRequest(ExcelConnection):
    sheet_name: Optional[str] = None
    fields: Optional[List[str]] = None
