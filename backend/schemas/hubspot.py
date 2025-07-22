from pydantic import BaseModel

class HubSpotConnection(BaseModel):
    api_key: str

class HubSpotFetchRequest(HubSpotConnection):
    endpoint: str
    params: dict = {}
