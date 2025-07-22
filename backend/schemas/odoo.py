from pydantic import BaseModel, HttpUrl
from typing import List

class OdooConnection(BaseModel):
    url: HttpUrl
    db: str
    username: str
    password: str

class OdooFetchRequest(OdooConnection):
    model: str
    fields: List[str]
