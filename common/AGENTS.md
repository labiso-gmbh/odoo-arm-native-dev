

## Environment Overview

This is an **Odoo 19.0 development environment** with three main components:

1. **Odoo Core** - Located at `/usr/lib/python3/dist-packages/odoo` (system-wide installation)
2. **Odoo Enterprise** - Located at `/workspace/enterprise` (proprietary modules)
3. **Labidoo Product Suite** - Located at `/workspace/labidoo` (custom proprietary modules by Labiso GmbH)
4. **Additional custom module repositories** - Located at `/workspace/`

The workspace uses a custom development launcher script (`odoo-dev-bin`) that automatically discovers and configures addon paths from all directories in `/workspace`.

## Key Configuration Files

- **`.vscode/launch.json`** - VS Code debug configurations for running Odoo EE and CE
- **`.vscode/odoo.conf`** - Odoo server configuration (database connection, ports, SMTP)
- **Ports used:**
  - Odoo web: `8019` (internally `8069`, mapped via container)
  - Odoo longpolling: `8049`
  - PostgreSQL: `5439` (internally via `postgres` host)
  - Mailpit SMTP: `1019`
  - Mailpit UI: `8119`

## Running Odoo

### Start the Server

Use the custom launcher script that automatically configures addon paths:

```bash
# Run with Enterprise modules (default database: dev_ee)
odoo-dev-bin --database=dev_ee --config=/workspace/.vscode/odoo.conf

# Run Community Edition only (exclude enterprise)
odoo-dev-bin --exclude-addon-dirs=*enterprise* --database=dev_ce --config=/workspace/.vscode/odoo.conf

# Include only specific addon directories
odoo-dev-bin --include-addon-dirs="labidoo,enterprise" --database=dev_ee --config=/workspace/.vscode/odoo.conf
```

The `odoo-dev-bin` script:
- Automatically discovers all addon directories in `/workspace`
- Supports `--include-addon-dirs` and `--exclude-addon-dirs` glob patterns
- Configures the `--addons-path` automatically
- Passes remaining arguments to Odoo

### Common Development Commands

```bash
# Install/upgrade modules
odoo-dev-bin -d dev_ee -i module_name --stop-after-init

# Update existing modules
odoo-dev-bin -d dev_ee -u module_name --stop-after-init

# Enable development mode with auto-reload
odoo-dev-bin -d dev_ee --dev=all

# Enable QWeb and XML development mode
odoo-dev-bin -d dev_ee --dev=qweb,xml

# Load specific language
odoo-dev-bin -d dev_ee --load-language=de_DE

# Export translations
odoo-dev-bin -d dev_ee --language=de_DE --i18n-export=/workspace/translations.po --modules=module_name

# Open Odoo shell
odoo-dev-bin -d dev_ee shell

# Start without loading specific modules
odoo-dev-bin -d dev_ee --load=base,web
```

## Testing

### Run Tests

```bash
# Enable tests for all modules
odoo-dev-bin -d dev_ee --test-enable --stop-after-init

# Run tests for specific module
odoo-dev-bin -d dev_ee --test-enable --test-tags=/module_name --stop-after-init

# Run specific test class
odoo-dev-bin -d dev_ee --test-enable --test-tags=/module_name:TestClassName --stop-after-init

# Run specific test method
odoo-dev-bin -d dev_ee --test-enable --test-tags=/module_name:TestClassName.test_method_name --stop-after-init

# Run tests tagged with specific tag
odoo-dev-bin -d dev_ee --test-enable --test-tags=post_install --stop-after-init

# Exclude tests
odoo-dev-bin -d dev_ee --test-enable --test-tags=-standard --stop-after-init

# Set log level for tests
odoo-dev-bin -d dev_ee --test-enable --test-tags=/module_name --log-level=test --stop-after-init
```

### Test Organization

Tests are located in `tests/` directories within modules and follow standard Odoo patterns:
- Inherit from common base classes like `odoo.tests.common.TransactionCase` or `odoo.addons.sale.tests.common.SaleCommon`
- Use `@tagged("post_install", "-at_install")` decorators to control when tests run
- Tests run twice: at module installation (`at_install`) and after all modules load (`post_install`)

Example test structure:
```python
from odoo.tests import tagged
from odoo.addons.sale.tests.common import SaleCommon

@tagged("post_install", "-at_install")
class TestSaleOrder(SaleCommon):
    def test_something(self):
        # Test implementation
        pass
```

## Labidoo Product Suite Architecture

The **labidoo** directory contains 50+ custom modules organized by functional area:

### Core Modules
- `labidoo_base` - Foundation module with centralized configuration interface for all Labidoo modules
- `labidoo_server` - Server-level customizations
- `labidoo_web` - Web interface customizations

### Domain-Specific Modules
Each module follows Odoo's standard structure:
```
module_name/
├── __init__.py
├── __manifest__.py
├── models/
├── views/
├── tests/
├── static/
│   ├── src/
│   └── description/
├── data/
├── i18n/
└── README.md
```

### Key Module Categories
- **Authentication & Access**: `auth_admin_passkey`, `labidoo_smart_login`, `base_user_role`
- **Sales**: `labidoo_sale`, `labidoo_sale_agents`, `labidoo_sale_subscription`, `labidoo_sale_rental`
- **Accounting**: `labidoo_account`, `labidoo_account_sdd`, `labidoo_dunning`, `labidoo_l10n_de_reports`
- **Mail & Communication**: `labidoo_mail`, `labidoo_mass_mail`, `mail_multicompany`, `mail_outbound_static`
- **Project Management**: `labidoo_project`, `labidoo_sale_project`, `labidoo_industry_fsm`
- **Website & E-commerce**: `labidoo_website_sale_*`, `labidoo_theme_common`
- **Document Management**: `labidoo_dms`, `labidoo_knowledge`
- **AI Features**: `labidoo_ai` (leverages Odoo 19's pgvector extension for RAG capabilities)
- **German Localization**: `labidoo_din5008`, `labidoo_din5008_sale`, `labidoo_din5008_purchase`

All Labidoo modules are proprietary software by Labiso GmbH.

## Module Manifest Structure

Odoo modules are defined by `__manifest__.py` files containing:
```python
{
    "name": "Module Name",
    "category": "Category",
    "summary": "Short description",
    "description": """Long description""",
    "author": "Labiso GmbH",
    "license": "Other proprietary",
    "website": "https://www.labidoo.de",
    "version": "19.0.x.y",  # Format: ODOO_VERSION.MAJOR.MINOR
    "depends": ["base", "other_module"],
    "data": [
        "security/ir.model.access.csv",
        "views/view_file.xml",
    ],
    "assets": {
        "web.assets_backend": ["module/static/src/js/file.js"],
    },
    "demo": [],
    "auto_install": False,  # or ["dependency"] for bridge modules
    "installable": True,
    "application": False,  # True for top-level apps
}
```

## Database Configuration

PostgreSQL database connection is configured in `.vscode/odoo.conf`:
- Host: `postgres` (container hostname)
- User: `odoo`
- Password: `odoo`
- Port: `5432` (internal container port)

The database includes the **pgvector** extension for AI/RAG features in Odoo 19.0.

## Development Workflows

### Creating a New Module

```bash
# Use Odoo scaffold command
odoo scaffold module_name /workspace/labidoo

# Follow the naming convention: labidoo_feature_name
```

### Debugging

Use VS Code launch configurations in `.vscode/launch.json`:
- **"Odoo EE"** - Run Enterprise edition with dev_ee database
- **"Odoo CE"** - Run Community edition with dev_ce database (excludes enterprise addons)

Both configs set `justMyCode: false` for full debugging including Odoo core.

### Module Dependencies

When adding dependencies:
1. Add to `depends` list in `__manifest__.py`
2. Ensure dependency modules are available in addon paths
3. Update/reinstall module: `odoo-dev-bin -d dev_ee -u module_name --stop-after-init`

### Working with Translations

German (`de_DE`) is a primary language for this environment:
```bash
# Load German language data
odoo-dev-bin -d dev_ee --load-language=de_DE

# Export translations for a module
odoo-dev-bin -d dev_ee --language=de_DE --i18n-export=/workspace/module.po --modules=module_name

# Import translations
odoo-dev-bin -d dev_ee --i18n-import=/workspace/module.po --language=de_DE
```

## Common Odoo Patterns in This Codebase

### Model Inheritance
Models extend existing Odoo models using `_inherit`:
```python
from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    custom_field = fields.Char(string="Custom Field")
```

### View Inheritance
Views extend existing views using XPath expressions:
```xml
<record id="view_partner_form_custom" model="ir.ui.view">
    <field name="name">res.partner.form.custom</field>
    <field name="model">res.partner</field>
    <field name="inherit_id" ref="base.view_partner_form"/>
    <field name="arch" type="xml">
        <xpath expr="//field[@name='phone']" position="after">
            <field name="custom_field"/>
        </xpath>
    </field>
</record>
```

### Security Access Rights
Access rights are defined in CSV files under `security/`:
```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_model_user,model.user,model_model,base.group_user,1,0,0,0
```

## AI and RAG Capabilities

Odoo 19.0 includes native AI features:
- PostgreSQL **pgvector** extension is pre-installed
- Enables semantic search and similarity operations
- Supports AI agent capabilities
- Used by `labidoo_ai` module

## Important Notes

1. **Proprietary Modules**: Both `enterprise/` and `labidoo/` contain proprietary code. Do not redistribute.
2. **Python Version**: Uses Python 3.14+ from Homebrew (`/home/linuxbrew/.linuxbrew/opt/python@3.14`)
3. **Time Zone**: Development script sets `TZ=UTC` automatically
4. **Workers**: Configuration uses `workers=0` for development (single-threaded for easier debugging)
5. **Email**: Uses Mailpit for local email testing (no external SMTP needed)
6. **Module Naming**: Follow convention `labidoo_<functional_area>` for consistency

## Useful Odoo CLI Commands

```bash
# List available commands
odoo --help

# Database management
odoo db list
odoo db create -d new_database
odoo db drop -d old_database
odoo db dump -d database_name -f backup.zip

# Module operations
odoo module list -d dev_ee  # List installed modules
odoo module install -d dev_ee -m module_name
odoo module uninstall -d dev_ee -m module_name

# Count lines of code
odoo cloc -d dev_ee -m module_name

# Neutralize production database for testing
odoo neutralize -d dev_ee

# Generate module scaffold
odoo scaffold module_name /workspace/labidoo
```

## Logging Configuration

Control logging verbosity:
```bash
# Set global log level
odoo-dev-bin -d dev_ee --log-level=debug

# Set module-specific log level
odoo-dev-bin -d dev_ee --log-handler=odoo.http:DEBUG

# Log SQL queries
odoo-dev-bin -d dev_ee --log-sql

# Log HTTP requests
odoo-dev-bin -d dev_ee --log-web

# Combined logging
odoo-dev-bin -d dev_ee --log-level=test --log-handler=odoo.tools.convert:DEBUG
```
