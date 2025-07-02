from backend.db import engine
from backend.models.client import Base

Base.metadata.create_all(bind=engine)
