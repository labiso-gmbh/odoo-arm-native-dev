#!/bin/bash
# PostgreSQL initialization script for Odoo 19.0
# This script ensures the vector extension is available for RAG support

set -e

# Function to create vector extension in a database
create_vector_extension() {
    local db_name="$1"
    echo "Creating vector extension in database: $db_name"
    
    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$db_name" <<-EOSQL
        CREATE EXTENSION IF NOT EXISTS vector;
        \echo 'Vector extension created in database: $db_name'
EOSQL
}

# Create extension in default postgres database
create_vector_extension "postgres"

# Create extension in template1 so all new databases inherit it
create_vector_extension "template1"

echo "PostgreSQL vector extension setup completed for Odoo 19.0 RAG support"