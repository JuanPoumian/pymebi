from sqlalchemy import create_engine, MetaData
import os
from dotenv import load_dotenv

load_dotenv()
DB_URL = os.getenv('DATABASE_URL')
engine = create_engine(DB_URL)
meta = MetaData()
meta.reflect(bind=engine)

clients = meta.tables['clients']
connectors = meta.tables['connectors']

def add_client_and_connector(name, email, connector_type, config):
    with engine.begin() as conn:  # begin() crea una transacción real
        # 1. Inserta cliente
        result = conn.execute(
            clients.insert().values(name=name, email=email)
        )
        client_id = result.inserted_primary_key[0]
        print(f"[DEBUG] Cliente insertado, id: {client_id}")

        # 2. Inserta conector
        result2 = conn.execute(
            connectors.insert().values(
                client_id=client_id,
                connector_type=connector_type,
                config=config  # dict, se serializa a JSON
            )
        )
        connector_id = result2.inserted_primary_key[0]
        print(f"[DEBUG] Conector insertado, id: {connector_id}")

        return client_id, connector_id

if __name__ == "__main__":
    odoo_config = {
        "host": "odoo.demo.com",
        "db": "odoo_db",
        "user": "admin",
        "password": "admin123"
    }
    client_id, connector_id = add_client_and_connector(
        "Empresa Demo", "demo@pymebi.com", "odoo", odoo_config
    )
    print(f"Cliente registrado con id: {client_id}")
    print(f"Conector Odoo registrado con id: {connector_id}")
