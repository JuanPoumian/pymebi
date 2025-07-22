from connectors.factory import get_connector

print("=== Odoo ===")
config_odoo = {"host": "odoo.demo.com", "db": "odoo_db", "user": "admin", "password": "admin123"}
odoo = get_connector("odoo", config_odoo)
print("Test conexión:", odoo.test_connection())
print("Ventas:", odoo.fetch_sales())
print("Schema:", odoo.get_schema())

print("\n=== Excel ===")
config_excel = {"filepath": "ruta/a/archivo.xlsx"}
excel = get_connector("excel", config_excel)
print("Test conexión:", excel.test_connection())
print("Ventas:", excel.fetch_sales())
print("Schema:", excel.get_schema())

print("\n=== Google Sheets ===")
config_sheets = {"spreadsheet_id": "tu_id", "sheet_name": "Sheet1", "credentials_json": "credenciales.json"}
gs = get_connector("googlesheets", config_sheets)
print("Test conexión:", gs.test_connection())
print("Ventas:", gs.fetch_sales())
print("Schema:", gs.get_schema())

print("\n=== HubSpot ===")
config_hubspot = {"api_key": "tu_api_key"}
hubspot = get_connector("hubspot", config_hubspot)
print("Test conexión:", hubspot.test_connection())
print("Ventas:", hubspot.fetch_sales())
print("Schema:", hubspot.get_schema())

print("\n=== REST ===")
config_rest = {"url": "https://jsonplaceholder.typicode.com/posts"}
rest = get_connector("rest", config_rest)
print("Test conexión:", rest.test_connection())
print("Ventas:", rest.fetch_sales())
print("Schema:", rest.get_schema())

print("\n=== SQL Server ===")
config_sqlserver = {
    "host": "localhost", "port": 1433, "database": "mi_db", "user": "usuario", "password": "pass",
    "query": "SELECT TOP 10 * FROM ventas"
}
sqlserver = get_connector("sqlserver", config_sqlserver)
print("Test conexión:", sqlserver.test_connection())
print("Ventas:", sqlserver.fetch_sales())
print("Schema:", sqlserver.get_schema())

print("\n=== MySQL ===")
config_mysql = {
    "host": "localhost", "port": 3306, "database": "mi_db", "user": "usuario", "password": "pass",
    "query": "SELECT * FROM ventas LIMIT 10"
}
mysql = get_connector("mysql", config_mysql)
print("Test conexión:", mysql.test_connection())
print("Ventas:", mysql.fetch_sales())
print("Schema:", mysql.get_schema())

print("\n=== MongoDB ===")
config_mongo = {"uri": "mongodb://localhost:27017/", "database": "mi_db", "collection": "ventas"}
mongo = get_connector("mongo", config_mongo)
print("Test conexión:", mongo.test_connection())
print("Ventas:", mongo.fetch_sales())
print("Schema:", mongo.get_schema())

print("\n=== PostgreSQL ===")
config_postgres = {
    "url": "postgresql://usuario:pass@localhost:5432/mi_db",
    "query": "SELECT * FROM ventas LIMIT 10"
}
postgres = get_connector("postgresql", config_postgres)
print("Test conexión:", postgres.test_connection())
print("Ventas:", postgres.fetch_sales())
print("Schema:", postgres.get_schema())

print("\n=== SAP ===")
config_sap = {"url": "https://sap.ejemplo.com/api", "user": "usuario", "password": "pass"}
sap = get_connector("sap", config_sap)
print("Test conexión:", sap.test_connection())
print("Ventas:", sap.fetch_sales())
print("Schema:", sap.get_schema())

print("\n=== Contpaqi ===")
config_contpaqi = {"conn_str": "Driver={SQL Server};Server=localhost;Database=mi_db;UID=usuario;PWD=pass;", "query": "SELECT * FROM ventas"}
contpaqi = get_connector("contpaqi", config_contpaqi)
print("Test conexión:", contpaqi.test_connection())
print("Ventas:", contpaqi.fetch_sales())
print("Schema:", contpaqi.get_schema())

print("\n=== Zoho CRM ===")
config_zoho = {"token": "zoho_token", "org_id": "zoho_org"}
zoho = get_connector("zoho", config_zoho)
print("Test conexión:", zoho.test_connection())
print("Ventas:", zoho.fetch_sales())
print("Schema:", zoho.get_schema())

print("\n=== QuickBooks ===")
config_quickbooks = {"token": "quickbooks_token", "realm_id": "quickbooks_realm"}
qb = get_connector("quickbooks", config_quickbooks)
print("Test conexión:", qb.test_connection())
print("Ventas:", qb.fetch_sales())
print("Schema:", qb.get_schema())

print("\n=== Salesforce ===")
config_sf = {"token": "sf_token", "instance_url": "https://mi_instance.salesforce.com"}
sf = get_connector("salesforce", config_sf)
print("Test conexión:", sf.test_connection())
print("Ventas:", sf.fetch_sales())
print("Schema:", sf.get_schema())

print("\n=== Zendesk ===")
config_zendesk = {"subdomain": "mi_subdominio", "email": "usuario@empresa.com", "token": "api_token"}
zendesk = get_connector("zendesk", config_zendesk)
print("Test conexión:", zendesk.test_connection())
print("Ventas:", zendesk.fetch_sales())
print("Schema:", zendesk.get_schema())
