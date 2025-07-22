# connectors/base_connector.py

class BaseConnector:
    """
    Base para todos los conectores.
    Si creas un nuevo conector, debes heredar de esta clase.
    """
    def __init__(self, config):
        self.config = config

    def test_connection(self):
        """
        Prueba la conexión con la fuente de datos.
        """
        raise NotImplementedError("Implementa este método en tu conector específico.")

    def fetch_sales(self):
        """
        Regresa la lista de ventas como lista de diccionarios.
        """
        raise NotImplementedError("Implementa este método en tu conector específico.")

    def get_schema(self):
        """
        Devuelve los nombres de los campos de las ventas.
        """
        raise NotImplementedError("Implementa este método en tu conector específico.")
