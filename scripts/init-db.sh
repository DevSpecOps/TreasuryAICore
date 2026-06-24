#!/bin/bash
set -e

# This script is automatically executed by PostgreSQL on first start.
# It creates the initial table structure for the treasury database.

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE TABLE IF NOT EXISTS transactions (
        id SERIAL PRIMARY KEY,
        amount DECIMAL(10,2) NOT NULL,
        currency VARCHAR(3) NOT NULL,
        status VARCHAR(20) NOT NULL,
        created_at TIMESTAMP DEFAULT NOW()
    );
    CREATE INDEX idx_transactions_status ON transactions(status);
EOSQL