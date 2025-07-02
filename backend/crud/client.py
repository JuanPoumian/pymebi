from sqlalchemy.orm import Session
from backend.models.client import Client
from backend.schemas.client import ClientCreate

def create_client(db: Session, client: ClientCreate):
    db_client = Client(name=client.name, email=client.email)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_clients(db: Session):
    return db.query(Client).all()
