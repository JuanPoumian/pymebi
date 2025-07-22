from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    client_id: int

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    client_id: int

    class Config:
        orm_mode = True
