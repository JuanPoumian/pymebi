from .base_connector import BaseConnector
import pandas as pd

class ContpaqiConnector(BaseConnector):
    def __init__(self, config):
        super().__init__(config)
        self.conn_str = config.get("conn_str")  # Usualmente SQL Server ODBC
        self.query = config.get("query", "SELECT TOP 10 * FROM ventas")

    def test_connection(self):
        try:
            import pyodbc
            with pyodbc.connect(self.conn_str, timeout=3) as conn:
                return True
        except Exception as e:
            print(f"Contpaqi Error: {e}")
            return False

    def fetch_sales(self):
        try:
            import pyodbc
            with pyodbc.connect(self.conn_str) as conn:
                df = pd.read_sql(self.query, conn)
                return df.to_dict(orient="records")
        except Exception as e:
            print(f"Contpaqi Fetch Error: {e}")
            return []

    def get_schema(self):
        ventas = self.fetch_sales()
        return list(ventas[0].keys()) if ventas else []
