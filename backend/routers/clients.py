from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.schemas.client import ClientCreate, ClientOut
from backend.crud.client import create_client, get_clients
from backend.db import get_db

router = APIRouter(
    prefix="/clientes",
    tags=["clientes"]
)

@router.post("/", response_model=ClientOut)
def create(client: ClientCreate, db: Session = Depends(get_db)):
    return create_client(db, client)

@router.get("/", response_model=list[ClientOut])
def read_clients(db: Session = Depends(get_db)):
    return get_clients(db)
