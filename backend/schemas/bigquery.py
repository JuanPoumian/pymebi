from pydantic import BaseModel

class BigQueryConnection(BaseModel):
    credentials_json: str
    project_id: str

class BigQueryQueryRequest(BigQueryConnection):
    query: str
    params: dict = {}
