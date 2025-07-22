from sqlalchemy.orm import Session
from backend.models.client import Client
from sqlalchemy.exc import IntegrityError

def get_client(db: Session, client_id: int) -> Client | None:
    return db.query(Client).filter(Client.id == client_id).first()

def get_client_by_email(db: Session, email: str) -> Client | None:
    return db.query(Client).filter(Client.email == email).first()

def get_clients(db: Session, skip: int = 0, limit: int = 100) -> list[Client]:
    return db.query(Client).offset(skip).limit(limit).all()

def create_client(db: Session, name: str, email: str) -> Client:
    db_client = Client(name=name, email=email)
    db.add(db_client)
    try:
        db.commit()
        db.refresh(db_client)
        return db_client
    except IntegrityError:
        db.rollback()
        raise ValueError("Ya existe un cliente con ese nombre o correo")
