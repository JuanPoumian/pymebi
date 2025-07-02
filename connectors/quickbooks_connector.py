from .base_connector import BaseConnector

class QuickBooksConnector(BaseConnector):
    def __init__(self, config):
        super().__init__(config)
        self.token = config.get("token")
        self.realm_id = config.get("realm_id")

    def test_connection(self):
        # Demo: simulado. En real usar QuickBooks Online API con requests y OAuth2.
        return all([self.token, self.realm_id])

    def fetch_sales(self):
        # Demo: datos simulados
        return [
            {"id": 1, "customer": "QBooks-Cliente1", "total": 8000},
            {"id": 2, "customer": "QBooks-Cliente2", "total": 2550}
        ]

    def get_schema(self):
        return ["id", "customer", "total"]
