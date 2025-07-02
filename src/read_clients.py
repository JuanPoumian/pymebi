from sqlalchemy import create_engine, MetaData, select
import os
from dotenv import load_dotenv

load_dotenv()
DB_URL = os.getenv('DATABASE_URL')
engine = create_engine(DB_URL)
meta = MetaData()
meta.reflect(bind=engine)

clients = meta.tables['clients']
connectors = meta.tables['connectors']

with engine.connect() as conn:
    print("Clientes:")
    for row in conn.execute(select(clients)):
        print(dict(row._mapping))
    print("\nConectores:")
    for row in conn.execute(select(connectors)):
        print(dict(row._mapping))
