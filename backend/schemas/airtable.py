from pydantic import BaseModel

class AirtableConnection(BaseModel):
    api_key: str
    base_id: str

class AirtableFetchRequest(AirtableConnection):
    table: str
    fields: list[str]
    filters: dict = {}
