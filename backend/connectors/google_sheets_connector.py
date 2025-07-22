import gspread
from google.oauth2.service_account import Credentials
import json

class GoogleSheetsConnector:
    def __init__(self, credentials_json):
        if isinstance(credentials_json, str):
            if credentials_json.strip().startswith("{"):
                info = json.loads(credentials_json)
            else:
                # Si mandas ruta al archivo (no recomendado para SaaS)
                with open(credentials_json) as f:
                    info = json.load(f)
        else:
            info = credentials_json
        self.scopes = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
        self.credentials = Credentials.from_service_account_info(info, scopes=self.scopes)
        self.client = gspread.authorize(self.credentials)

    def test_connection(self):
        try:
            # Lista 1 hoja como prueba
            spreadsheets = self.client.openall()
            return True if spreadsheets else True  # Levanta aunque no haya hojas
        except Exception as e:
            print(f"Google Sheets Error: {e}")
            return False

    def fetch_data(self, spreadsheet_id, worksheet_name=None, range_name=None):
        try:
            sh = self.client.open_by_key(spreadsheet_id)
            if worksheet_name:
                worksheet = sh.worksheet(worksheet_name)
            else:
                worksheet = sh.get_worksheet(0)
            # Si pasas un rango específico, úsalo
            if range_name:
                data = worksheet.get(range_name)
            else:
                data = worksheet.get_all_values()
            # Opcional: convierte a lista de dicts si la primera fila son headers
            if data and len(data) > 1:
                headers = data[0]
                records = [dict(zip(headers, row)) for row in data[1:]]
                return records
            return data
        except Exception as e:
            print(f"Fetch Data Error: {e}")
            return []
