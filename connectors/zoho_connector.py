from .base_connector import BaseConnector
import requests

class ZohoCRMConnector(BaseConnector):
    def __init__(self, config):
        super().__init__(config)
        self.token = config.get("token")
        self.org_id = config.get("org_id")

    def test_connection(self):
        url = "https://www.zohoapis.com/crm/v2/Leads"
        headers = {
            "Authorization": f"Zoho-oauthtoken {self.token}",
            "orgId": self.org_id
        }
        try:
            resp = requests.get(url, headers=headers, timeout=5)
            return resp.status_code == 200
        except Exception as e:
            print(f"Zoho Error: {e}")
            return False

    def fetch_sales(self):
        url = "https://www.zohoapis.com/crm/v2/Deals"
        headers = {
            "Authorization": f"Zoho-oauthtoken {self.token}",
            "orgId": self.org_id
        }
        try:
            resp = requests.get(url, headers=headers, timeout=10)
            data = resp.json().get("data", [])
            return data
        except Exception as e:
            print(f"Zoho Fetch Error: {e}")
            return []

    def get_schema(self):
        ventas = self.fetch_sales()
        return list(ventas[0].keys()) if ventas else []
