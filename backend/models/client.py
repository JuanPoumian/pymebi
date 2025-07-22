from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    users = relationship("User", back_populates="client")