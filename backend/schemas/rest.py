from pydantic import BaseModel, HttpUrl
from typing import Optional, Dict

class RESTConnection(BaseModel):
    url: HttpUrl
    headers: Optional[Dict[str, str]] = None

class RESTFetchRequest(RESTConnection):
    endpoint: str
    params: Optional[Dict[str, str]] = None
    method: str = "GET"
    body: Optional[dict] = None
