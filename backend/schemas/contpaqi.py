from pydantic import BaseModel

class ContpaqiConnection(BaseModel):
    host: str
    username: str
    password: str
    database: str

class ContpaqiQueryRequest(ContpaqiConnection):
    query: str
    params: dict = {}
