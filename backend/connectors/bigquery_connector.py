from google.cloud import bigquery
from google.oauth2 import service_account
import json

class BigQueryConnector:
    def __init__(self, credentials_json, project_id):
        if isinstance(credentials_json, str):
            if credentials_json.strip().startswith("{"):
                info = json.loads(credentials_json)
            else:
                # Asume que es la ruta al archivo JSON
                with open(credentials_json) as f:
                    info = json.load(f)
        else:
            info = credentials_json
        credentials = service_account.Credentials.from_service_account_info(info)
        self.client = bigquery.Client(credentials=credentials, project=project_id)

    def test_connection(self):
        try:
            datasets = list(self.client.list_datasets())
            return True
        except Exception as e:
            print(f"Error BigQuery: {e}")
            return False

    def execute_query(self, query, params=None):
        job_config = bigquery.QueryJobConfig()
        if params:
            job_config.query_parameters = [
                bigquery.ScalarQueryParameter(name, "STRING", value)
                for name, value in params.items()
            ]
        query_job = self.client.query(query, job_config=job_config)
        results = query_job.result()
        columns = [field.name for field in results.schema]
        data = [dict(zip(columns, row)) for row in results]
        return data
