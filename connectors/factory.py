def get_connector(connector_type, config):
    if connector_type == "odoo":
        from .odoo_connector import OdooConnector
        return OdooConnector(config)
    elif connector_type == "excel":
        from .excel_connector import ExcelConnector
        return ExcelConnector(config)
    elif connector_type == "googlesheets":
        from .googlesheets_connector import GoogleSheetsConnector
        return GoogleSheetsConnector(config)
    elif connector_type == "hubspot":
        from .hubspot_connector import HubSpotConnector
        return HubSpotConnector(config)
    elif connector_type == "rest":
        from .rest_connector import RESTConnector
        return RESTConnector(config)
    elif connector_type == "sqlserver":
        from .sqlserver_connector import SQLServerConnector
        return SQLServerConnector(config)
    elif connector_type == "mysql":
        from .mysql_connector import MySQLConnector
        return MySQLConnector(config)
    elif connector_type == "mongo":
        from .mongo_connector import MongoConnector
        return MongoConnector(config)
    elif connector_type == "postgresql":
        from .postgresql_connector import PostgreSQLConnector
        return PostgreSQLConnector(config)
    elif connector_type == "sap":
        from .sap_connector import SAPConnector
        return SAPConnector(config)
    elif connector_type == "contpaqi":
        from .contpaqi_connector import ContpaqiConnector
        return ContpaqiConnector(config)
    elif connector_type == "zoho":
        from .zoho_connector import ZohoCRMConnector
        return ZohoCRMConnector(config)
    elif connector_type == "quickbooks":
        from .quickbooks_connector import QuickBooksConnector
        return QuickBooksConnector(config)
    elif connector_type == "salesforce":
        from .salesforce_connector import SalesforceConnector
        return SalesforceConnector(config)
    elif connector_type == "zendesk":
        from .zendesk_connector import ZendeskConnector
        return ZendeskConnector(config)
    else:
        raise ValueError(f"Tipo de conector desconocido: {connector_type}")
