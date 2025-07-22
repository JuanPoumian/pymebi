from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.crud import client as crud_client
from backend.db import get_db
from backend.schemas.client import ClientCreate, ClientRead

router = APIRouter(
    prefix="/clients",
    tags=["clients"],
)

@router.post("/", response_model=ClientRead)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    db_client = crud_client.get_client_by_email(db, email=client.email)
    if db_client:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_client = crud_client.create_client(db=db, name=client.name, email=client.email)
    return new_client

@router.get("/", response_model=list[ClientRead])
def read_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clients = crud_client.get_clients(db, skip=skip, limit=limit)
    return clients

@router.get("/{client_id}", response_model=ClientRead)
def read_client(client_id: int, db: Session = Depends(get_db)):
    db_client = crud_client.get_client(db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client
