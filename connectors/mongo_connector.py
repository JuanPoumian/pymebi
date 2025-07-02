from .base_connector import BaseConnector

class MongoConnector(BaseConnector):
    def __init__(self, config):
        super().__init__(config)
        self.uri = config.get("uri")
        self.database = config.get("database")
        self.collection = config.get("collection")

    def test_connection(self):
        try:
            from pymongo import MongoClient
            client = MongoClient(self.uri, serverSelectionTimeoutMS=3000)
            client.admin.command("ping")
            return True
        except Exception as e:
            print(f"Mongo Error: {e}")
            return False

    def fetch_sales(self):
        try:
            from pymongo import MongoClient
            client = MongoClient(self.uri)
            db = client[self.database]
            coll = db[self.collection]
            docs = list(coll.find().limit(10))
            # Quita el _id si quieres
            for doc in docs:
                doc.pop('_id', None)
            return docs
        except Exception as e:
            print(f"Mongo Fetch Error: {e}")
            return []

    def get_schema(self):
        ventas = self.fetch_sales()
        return list(ventas[0].keys()) if ventas else []
