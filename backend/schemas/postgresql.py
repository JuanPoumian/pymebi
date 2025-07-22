from pydantic import BaseModel

class PostgreSQLConnection(BaseModel):
    host: str
    port: int
    database: str
    username: str
    password: str

class PostgreSQLQueryRequest(PostgreSQLConnection):
    query: str
    params: dict = {}
