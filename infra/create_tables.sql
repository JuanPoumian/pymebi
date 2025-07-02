-- Tabla de clientes
CREATE TABLE IF NOT EXISTS clients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Tabla de conectores
CREATE TABLE IF NOT EXISTS connectors (
    id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES clients(id),
    connector_type VARCHAR(50) NOT NULL, -- 'odoo', 'hubspot', 'googlesheets', etc.
    config JSONB NOT NULL, -- credenciales y parámetros
    created_at TIMESTAMP DEFAULT NOW()
);
