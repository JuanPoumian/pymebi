from .base_connector import BaseConnector

class SAPConnector(BaseConnector):
    def __init__(self, config):
        super().__init__(config)
        self.url = config.get("url")
        self.user = config.get("user")
        self.password = config.get("password")

    def test_connection(self):
        # Simulación. En producción, conecta al API de SAP (usualmente REST, SOAP o pyRFC)
        return all([self.url, self.user, self.password])

    def fetch_sales(self):
        # Demo: datos simulados
        return [
            {"id": 1, "folio": "SAP-0001", "monto": 3000},
            {"id": 2, "folio": "SAP-0002", "monto": 7800}
        ]

    def get_schema(self):
        return ["id", "folio", "monto"]
