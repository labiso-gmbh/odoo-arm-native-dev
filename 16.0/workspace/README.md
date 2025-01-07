# Odoo 16.0 Workspace

This directory contains your Odoo 16.0 development environment. Here's what you need to know:

## Structure

- `odoo/`: Clone the Odoo 16.0 community repository here
  ```bash
  git clone -b 16.0 https://github.com/odoo/odoo.git
  ```

- `enterprise/`: Clone the Odoo 16.0 enterprise repository here (if you have access)
  ```bash
  git clone -b 16.0 https://github.com/odoo/enterprise.git
  ```

- Custom modules should be placed in their own directories at this level

## Configuration

The `.vscode` directory will be created automatically when you first open the workspace in VSCode. It will contain:
- `odoo.conf`: Odoo server configuration
- VSCode workspace settings

## Ports

This workspace uses the following ports:
- Odoo web: `8016`
- Odoo longpolling: `8046`
- PostgreSQL: `5436`
- Mailpit SMTP: `1026`
- Mailpit UI: `8026`
