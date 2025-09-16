-- Initialize PostgreSQL with required extensions for Odoo 19.0
-- This script is executed when the database is first created

-- Create the vector extension for RAG (Retrieval-Augmented Generation) support
-- Required for AI agents in Odoo 19.0
CREATE EXTENSION IF NOT EXISTS vector;

-- Log the extension creation
\echo 'PostgreSQL vector extension has been created for Odoo 19.0 RAG support'