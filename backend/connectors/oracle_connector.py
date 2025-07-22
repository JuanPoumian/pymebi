import cx_Oracle

class OracleConnector:
    def __init__(self, host, port, service_name, username, password):
        self.host = host
        self.port = port
        self.service_name = service_name
        self.username = username
        self.password = password
        self.connection = None

    def connect(self):
        if self.connection is None:
            dsn = cx_Oracle.makedsn(self.host, self.port, service_name=self.service_name)
            self.connection = cx_Oracle.connect(
                user=self.username,
                password=self.password,
                dsn=dsn
            )
        return self.connection

    def test_connection(self):
        try:
            conn = self.connect()
            conn.close()
            self.connection = None
            return True
        except Exception as e:
            print(f"Error al conectar a Oracle: {e}")
            return False

    def execute_query(self, query, params=None):
        conn = self.connect()
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        cursor.close()
        return [dict(zip(columns, row)) for row in rows]
