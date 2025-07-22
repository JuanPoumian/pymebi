import pyodbc

class SQLServerConnector:
    def __init__(self, host, port, database, username, password):
        self.host = host
        self.port = port
        self.database = database
        self.username = username
        self.password = password
        self.connection = None

    def connect(self):
        if self.connection is None:
            conn_str = (
                f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                f'SERVER={self.host},{self.port};'
                f'DATABASE={self.database};'
                f'UID={self.username};'
                f'PWD={self.password}'
            )
            self.connection = pyodbc.connect(conn_str)
        return self.connection

    def test_connection(self):
        try:
            conn = self.connect()
            conn.close()
            self.connection = None
            return True
        except Exception as e:
            print("Error al conectar SQL Server:", e)
            return False

    def execute_query(self, query, params=None):
        conn = self.connect()
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        results = [dict(zip(columns, row)) for row in rows]
        cursor.close()
        return results
