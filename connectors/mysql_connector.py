from .base_connector import BaseConnector
import pandas as pd

class MySQLConnector(BaseConnector):
    def __init__(self, config):
        super().__init__(config)
        self.host = config.get("host")
        self.port = config.get("port", 3306)
        self.database = config.get("database")
        self.user = config.get("user")
        self.password = config.get("password")
        self.query = config.get("query", "SELECT * FROM ventas LIMIT 10")

    def test_connection(self):
        try:
            import pymysql
            conn = pymysql.connect(
                host=self.host, port=self.port,
                user=self.user, password=self.password, database=self.database,
                connect_timeout=3
            )
            conn.close()
            return True
        except Exception as e:
            print(f"MySQL Error: {e}")
            return False

    def fetch_sales(self):
        try:
            import pymysql
            conn = pymysql.connect(
                host=self.host, port=self.port,
                user=self.user, password=self.password, database=self.database
            )
            df = pd.read_sql(self.query, conn)
            conn.close()
            return df.to_dict(orient="records")
        except Exception as e:
            print(f"MySQL Fetch Error: {e}")
            return []

    def get_schema(self):
        ventas = self.fetch_sales()
        return list(ventas[0].keys()) if ventas else []
