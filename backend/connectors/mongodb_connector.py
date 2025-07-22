from pymongo import MongoClient

class MongoDBConnector:
    def __init__(self, uri, database):
        self.uri = uri
        self.database = database

    def test_connection(self):
        try:
            client = MongoClient(self.uri, serverSelectionTimeoutMS=3000)
            client.admin.command("ping")
            return True
        except Exception as e:
            print(f"Mongo Error: {e}")
            return False

    def fetch_data(self, collection, filter=None):
        try:
            client = MongoClient(self.uri)
            db = client[self.database]
            coll = db[collection]
            docs = list(coll.find(filter or {}).limit(10))
            for doc in docs:
                doc.pop('_id', None)
            return docs
        except Exception as e:
            print(f"Mongo Fetch Error: {e}")
            return []
