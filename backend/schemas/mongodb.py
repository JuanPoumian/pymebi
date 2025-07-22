from pydantic import BaseModel

class MongoDBConnection(BaseModel):
    uri: str
    database: str

class MongoDBFetchRequest(MongoDBConnection):
    collection: str
    filter: dict = {}
