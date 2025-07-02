from .base_connector import BaseConnector
import requests

class SalesforceConnector(BaseConnector):
    def __init__(self, config):
        super().__init__(config)
        self.token = config.get("token")
        self.instance_url = config.get("instance_url")

    def test_connection(self):
        url = f"{self.instance_url}/services/data/v59.0/"
        headers = {"Authorization": f"Bearer {self.token}"}
        try:
            resp = requests.get(url, headers=headers, timeout=5)
            return resp.status_code == 200
        except Exception as e:
            print(f"Salesforce Error: {e}")
            return False

    def fetch_sales(self):
        url = f"{self.instance_url}/services/data/v59.0/query"
        headers = {"Authorization": f"Bearer {self.token}"}
        params = {"q": "SELECT Id, Name, Amount FROM Opportunity LIMIT 5"}
        try:
            resp = requests.get(url, headers=headers, params=params, timeout=10)
            data = resp.json().get("records", [])
            return data
        except Exception as e:
            print(f"Salesforce Fetch Error: {e}")
            return []

    def get_schema(self):
        ventas = self.fetch_sales()
        return list(ventas[0].keys()) if ventas else []
