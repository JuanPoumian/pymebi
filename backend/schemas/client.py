from pydantic import BaseModel

class ClientCreate(BaseModel):
    name: str
    email: str

class ClientOut(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        orm_mode = True
