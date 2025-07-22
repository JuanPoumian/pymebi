from pydantic import BaseModel

class OracleConnection(BaseModel):
    host: str
    port: int
    service_name: str
    username: str
    password: str

class OracleQueryRequest(OracleConnection):
    query: str
    params: dict = {}
