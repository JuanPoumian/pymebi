from .base_connector import BaseConnector
import requests

class HubSpotConnector(BaseConnector):
    def __init__(self, config):
        super().__init__(config)
        self.api_key = config.get("api_key")

    def test_connection(self):
        url = f"https://api.hubapi.com/crm/v3/objects/contacts?hapikey={self.api_key}&limit=1"
        try:
            resp = requests.get(url, timeout=5)
            return resp.status_code == 200
        except Exception as e:
            print(f"HubSpot Error: {e}")
            return False

    def fetch_sales(self):
        url = f"https://api.hubapi.com/crm/v3/objects/deals?hapikey={self.api_key}&limit=5"
        try:
            resp = requests.get(url, timeout=10)
            data = resp.json().get("results", [])
            return data
        except Exception as e:
            print(f"HubSpot Fetch Error: {e}")
            return []

    def get_schema(self):
        sales = self.fetch_sales()
        return list(sales[0].keys()) if sales else []
