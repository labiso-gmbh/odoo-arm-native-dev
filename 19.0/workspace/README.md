# Odoo 19.0 Workspace

This directory contains your Odoo 19.0 development environment. Here's what you need to know:

## Structure

- `odoo/`: Clone the Odoo 19.0 community repository here
  ```bash
  git clone -b 19.0 https://github.com/odoo/odoo.git
  ```

- `enterprise/`: Clone the Odoo 19.0 enterprise repository here (if you have access)
  ```bash
  git clone -b 19.0 https://github.com/odoo/enterprise.git
  ```

- Custom modules should be placed in their own directories at this level

## Configuration

The `.vscode` directory will be created automatically when you first open the workspace in VSCode. It will contain:
- `odoo.conf`: Odoo server configuration
- VSCode workspace settings

## Features

### AI & RAG Support
This development environment includes support for Odoo 19.0's new AI features:
- **PostgreSQL Vector Extension**: Pre-installed `pgvector` extension for RAG (Retrieval-Augmented Generation)
- **AI Agents**: Ready for Odoo's new AI agent capabilities
- **Vector Search**: Support for semantic search and similarity operations

The PostgreSQL database is automatically configured with the `vector` extension when the container starts.

## Ports

This workspace uses the following ports:
- Odoo web: `8019`
- Odoo longpolling: `8049`
- PostgreSQL: `5439`
- Mailpit SMTP: `1019`
- Mailpit UI: `8119`
