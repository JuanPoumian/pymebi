from backend.db import engine
from backend.models.user import Base as UserBase
from backend.models.client import Base as ClientBase

# Esto asegura que ambas tablas se creen si no existen
UserBase.metadata.create_all(bind=engine)
ClientBase.metadata.create_all(bind=engine)
