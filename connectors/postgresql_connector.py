from .base_connector import BaseConnector
import pandas as pd

class PostgreSQLConnector(BaseConnector):
    def __init__(self, config):
        super().__init__(config)
        self.url = config.get("url")
        self.query = config.get("query", "SELECT * FROM ventas LIMIT 10")

    def test_connection(self):
        try:
            import sqlalchemy
            engine = sqlalchemy.create_engine(self.url)
            with engine.connect() as conn:
                return True
        except Exception as e:
            print(f"PostgreSQL Error: {e}")
            return False

    def fetch_sales(self):
        try:
            import sqlalchemy
            engine = sqlalchemy.create_engine(self.url)
            df = pd.read_sql(self.query, engine)
            return df.to_dict(orient="records")
        except Exception as e:
            print(f"PostgreSQL Fetch Error: {e}")
            return []

    def get_schema(self):
        ventas = self.fetch_sales()
        return list(ventas[0].keys()) if ventas else []
