from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.schemas.user import UserCreate, UserOut
from backend.crud.user import create_user, get_users
from backend.db import get_db

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"]
)

@router.post("/", response_model=UserOut)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/", response_model=list[UserOut])
def read_users(db: Session = Depends(get_db)):
    return get_users(db)
