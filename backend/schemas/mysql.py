from pydantic import BaseModel

class MySQLConnection(BaseModel):
    host: str
    port: int
    database: str
    username: str
    password: str

class MySQLQueryRequest(MySQLConnection):
    query: str
    params: dict = {}
