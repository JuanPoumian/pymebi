from .base_connector import BaseConnector
import requests

class RESTConnector(BaseConnector):
    def __init__(self, config):
        super().__init__(config)
        self.url = config.get("url")
        self.headers = config.get("headers", {})

    def test_connection(self):
        try:
            resp = requests.get(self.url, headers=self.headers, timeout=5)
            return resp.status_code == 200
        except Exception as e:
            print(f"REST Test Error: {e}")
            return False

    def fetch_sales(self):
        try:
            resp = requests.get(self.url, headers=self.headers, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                if isinstance(data, dict) and "results" in data:
                    return data["results"]
                return data if isinstance(data, list) else [data]
            return []
        except Exception as e:
            print(f"REST Fetch Error: {e}")
            return []

    def get_schema(self):
        sales = self.fetch_sales()
        return list(sales[0].keys()) if sales else []
