# connectors/odoo_connector.py

from .base_connector import BaseConnector

class OdooConnector(BaseConnector):
    """
    Conector de ejemplo para Odoo.
    """
    def __init__(self, config):
        super().__init__(config)
        # Aquí puedes guardar los detalles del config si los necesitas

    def test_connection(self):
        # Aquí pondrías la conexión real a Odoo, por ahora siempre responde True si config tiene lo necesario.
        required_keys = ['host', 'db', 'user', 'password']
        return all(k in self.config for k in required_keys)

    def fetch_sales(self):
        # Simulado. Aquí debería ir tu integración real.
        return [
            {'id': 1, 'name': 'SO001', 'date_order': '2024-06-01', 'amount_total': 1200, 'partner_id': [7, 'Cliente XYZ']},
            {'id': 2, 'name': 'SO002', 'date_order': '2024-06-03', 'amount_total': 2100, 'partner_id': [9, 'Cliente ABC']}
        ]

    def get_schema(self):
        return ["id", "name", "date_order", "amount_total", "partner_id"]
