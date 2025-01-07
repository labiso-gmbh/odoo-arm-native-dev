# Odoo Multi-Version Development Environment

Welcome to the Odoo Multi-Version Development Environment! This repository provides development containers for Odoo versions 16.0, 17.0, and 18.0, optimized for Apple Silicon (ARM64) architecture.

## Overview

This repository contains separate development environments for different Odoo versions, each configured with:
- Docker containers optimized for ARM64 architecture
- VSCode development container configuration
- PostgreSQL database
- Mailpit for email testing
- Development tools and extensions

## Prerequisites

Before you begin, ensure you have installed:
- [Docker Desktop](https://docs.docker.com/get-docker/)
- [Visual Studio Code](https://code.visualstudio.com/download)
- [VSCode Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

## Repository Structure

```
.
├── 16.0/                   # Odoo 16.0 environment
│   ├── .devcontainer/     # Container configuration
│   └── workspace/         # Development workspace
├── 17.0/                   # Odoo 17.0 environment
│   ├── .devcontainer/     # Container configuration
│   └── workspace/         # Development workspace
└── 18.0/                   # Odoo 18.0 environment
    ├── .devcontainer/     # Container configuration
    └── workspace/         # Development workspace
```

## Port Configuration

Each Odoo version uses different ports to avoid conflicts:

### Odoo 16.0
- Odoo web: `8016`
- Odoo longpolling: `8046`
- PostgreSQL: `5436`
- Mailpit SMTP: `1026`
- Mailpit UI: `8026`

### Odoo 17.0
- Odoo web: `8017`
- Odoo longpolling: `8047`
- PostgreSQL: `5437`
- Mailpit SMTP: `1025`
- Mailpit UI: `8025`

### Odoo 18.0
- Odoo web: `8018`
- Odoo longpolling: `8048`
- PostgreSQL: `5438`
- Mailpit SMTP: `1027`
- Mailpit UI: `8027`

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/labiso-gmbh/odoo-development
   ```

2. Choose the Odoo version you want to work with by opening its directory in VSCode:
   ```bash
   code 16.0  # For Odoo 16
   code 17.0  # For Odoo 17
   code 18.0  # For Odoo 18
   ```

3. When prompted to "Reopen in Container", click "Reopen in Container". Alternatively, open the Command Palette (F1 or Cmd+Shift+P) and select "Remote-Containers: Reopen in Container".

4. Wait for the container to build and start. This may take a few minutes the first time.

5. Once the container is ready, you can access:
   - Odoo web interface at `http://localhost:80xx` (where xx is 16, 17, or 18)
   - Mailpit interface at `http://localhost:80xx` (where xx is 26, 25, or 27)

## Development Workflow

1. Each version's workspace directory contains:
   - `odoo/`: The Odoo source code
   - `enterprise/`: Odoo Enterprise modules (if available)
   - Custom module directories

2. The development container includes:
   - Python with required dependencies
   - PostgreSQL database
   - Development tools (git, black formatter, etc.)
   - VSCode extensions for Odoo development

3. Changes made in the workspace directory persist on your host machine.

## Contributing

We welcome contributions! Please feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) file for details.

---

For support or questions, please open an issue in this repository.
