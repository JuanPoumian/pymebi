from pydantic import BaseModel

class SAPConnection(BaseModel):
    host: str
    username: str
    password: str
    client: str
    lang: str

class SAPFetchRequest(SAPConnection):
    table: str
    fields: list[str]
    filters: dict = {}
