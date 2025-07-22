from pydantic import BaseModel, HttpUrl
from typing import Optional, Dict, Any

class GenericConnection(BaseModel):
    url: HttpUrl
    username: Optional[str] = None
    password: Optional[str] = None
    api_key: Optional[str] = None

class GenericFetchRequest(GenericConnection):
    resource: str
    params: Optional[Dict[str, Any]] = None
    method: str = "GET"
    body: Optional[dict] = None
