# connectors/excel_connector.py

from .base_connector import BaseConnector
import pandas as pd

class ExcelConnector(BaseConnector):
    """
    Conector para archivos Excel (XLSX).
    """
    def test_connection(self):
        try:
            pd.read_excel(self.config["file_path"], nrows=1)
            return True
        except Exception:
            return False

    def fetch_sales(self):
        df = pd.read_excel(self.config["file_path"])
        return df.to_dict(orient="records")

    def get_schema(self):
        df = pd.read_excel(self.config["file_path"], nrows=1)
        return df.columns.tolist()
