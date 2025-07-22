from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base
import datetime

Base = declarative_base()

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    # Si quieres, puedes agregar: users = relationship("User", back_populates="client")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)  # <-- AGREGA ESTA LÍNEA
    password = Column(String)  # <-- Aquí se guarda el HASH de la contraseña
    client_id = Column(Integer, ForeignKey("clients.id"))
    client = relationship("Client")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
