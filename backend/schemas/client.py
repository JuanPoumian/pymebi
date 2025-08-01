from pydantic import BaseModel, EmailStr

class ClientBase(BaseModel):
    name: str
    email: EmailStr

class ClientCreate(ClientBase):
    pass

class ClientRead(ClientBase):
    id: int

    class Config:
        orm_mode = True
