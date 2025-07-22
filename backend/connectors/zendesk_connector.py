from .base_connector import BaseConnector
import requests

class ZendeskConnector(BaseConnector):
    def __init__(self, config):
        super().__init__(config)
        self.subdomain = config.get("subdomain")
        self.email = config.get("email")
        self.token = config.get("token")

    def test_connection(self):
        url = f"https://{self.subdomain}.zendesk.com/api/v2/tickets.json"
        try:
            resp = requests.get(
                url,
                auth=(f"{self.email}/token", self.token),
                timeout=5
            )
            return resp.status_code == 200
        except Exception as e:
            print(f"Zendesk Error: {e}")
            return False

    def fetch_sales(self):
        url = f"https://{self.subdomain}.zendesk.com/api/v2/tickets.json"
        try:
            resp = requests.get(
                url,
                auth=(f"{self.email}/token", self.token),
                timeout=10
            )
            data = resp.json().get("tickets", [])
            return data
        except Exception as e:
            print(f"Zendesk Fetch Error: {e}")
            return []

    def get_schema(self):
        ventas = self.fetch_sales()
        return list(ventas[0].keys()) if ventas else []
