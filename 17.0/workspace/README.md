# Odoo 17.0 Workspace

This directory contains your Odoo 17.0 development environment. Here's what you need to know:

## Structure

- `odoo/`: Clone the Odoo 17.0 community repository here
  ```bash
  git clone -b 17.0 https://github.com/odoo/odoo.git
  ```

- `enterprise/`: Clone the Odoo 17.0 enterprise repository here (if you have access)
  ```bash
  git clone -b 17.0 https://github.com/odoo/enterprise.git
  ```

- Custom modules should be placed in their own directories at this level

## Configuration

The `.vscode` directory will be created automatically when you first open the workspace in VSCode. It will contain:
- `odoo.conf`: Odoo server configuration
- VSCode workspace settings

## Ports

This workspace uses the following ports:
- Odoo web: `8017`
- Odoo longpolling: `8047`
- PostgreSQL: `5437`
- Mailpit SMTP: `1025`
- Mailpit UI: `8025`
