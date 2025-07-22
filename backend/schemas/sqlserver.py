from pydantic import BaseModel

class SQLServerConnection(BaseModel):
    host: str
    port: int
    database: str
    username: str
    password: str

class SQLServerQueryRequest(SQLServerConnection):
    query: str
    params: dict = {}
