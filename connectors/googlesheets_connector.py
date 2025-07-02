from .base_connector import BaseConnector

class GoogleSheetsConnector(BaseConnector):
    def __init__(self, config):
        super().__init__(config)
        self.sheet_id = config.get("sheet_id")
        # Aquí iría la inicialización real de la API

    def test_connection(self):
        # Simulación, luego pon la lógica real con la API de Google
        return True

    def fetch_sales(self):
        # Devuelve lista de dicts (igual que los otros conectores)
        # Ejemplo simulado
        return [
            {'id': 1, 'name': 'SO101', 'date_order': '2024-07-01', 'amount_total': 3200, 'partner_id': [2, 'Cliente Google']}
        ]

    def get_schema(self):
        return ["id", "name", "date_order", "amount_total", "partner_id"]