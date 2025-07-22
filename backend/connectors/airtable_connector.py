from pyairtable import Table

class AirtableConnector:
    def __init__(self, api_key, base_id):
        self.api_key = api_key
        self.base_id = base_id

    def test_connection(self):
        try:
            # Listar todas las tablas (primera tabla por default)
            table = Table(self.api_key, self.base_id, "Table 1")
            records = table.all(max_records=1)
            return True
        except Exception as e:
            print(f"Airtable Error: {e}")
            return False

    def fetch_data(self, table_name, fields=None, filters=None):
        try:
            table = Table(self.api_key, self.base_id, table_name)
            records = table.all(fields=fields, formula=filters)
            # Limpieza de los registros
            data = [r["fields"] for r in records]
            return data
        except Exception as e:
            print(f"Airtable Fetch Error: {e}")
            return []
