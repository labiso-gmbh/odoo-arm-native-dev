# Odoo Development Environment for Apple Silicon

A development environment optimized for Odoo on Apple Silicon (M-Chips) and ARM64 architectures. This project provides native ARM64 support for Odoo development, offering improved performance by eliminating the need for Rosetta 2 emulation.

## 🚀 Key Features

- Native ARM64 support optimized for Apple Silicon
- Development environments for Odoo 16.0, 17.0, and 18.0
- VSCode devcontainer with ARM64 support
- Integrated development tools and debugging capabilities
- Isolated container environments for each Odoo version

## 💡 Technical Background

Common challenges in Odoo development on Apple Silicon include:
- AMD64 Docker images requiring Rosetta 2 emulation
- Performance impact on build times and development
- Compatibility issues with development tools under emulation

This environment addresses these challenges through:
- Native ARM64 base images and dependencies
- Optimized container configuration
- Integrated development toolchain

## 🏗 Technical Architecture

### Container Stack
- Base Image: `arm64v8/debian:bookworm-slim`
- Native ARM64 PostgreSQL
- Mailpit for email testing
- Development tools and utilities

### Development Features
- VSCode integration with extensions
- Black code formatting
- Git integration
- Debugging tools
- Python package management
- Automated addons path configuration

## 📋 Prerequisites

- Apple Silicon Mac (M-Chips) or ARM64-based system
- [Docker Desktop](https://docs.docker.com/get-docker/)
- [Visual Studio Code](https://code.visualstudio.com/download)
- [VSCode Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

## 🔌 Port Configuration

Service ports for each Odoo version:

| Service          | 16.0  | 17.0  | 18.0  |
|-----------------|-------|-------|-------|
| Odoo Web        | 8016  | 8017  | 8018  |
| Odoo Longpolling| 8046  | 8047  | 8048  |
| PostgreSQL      | 5436  | 5437  | 5438  |
| Mailpit SMTP    | 1016  | 1017  | 1018  |
| Mailpit UI      | 8116  | 8117  | 8118  |

## 🚀 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/labiso-gmbh/odoo-development
   cd odoo-development
   ```

2. Open your preferred Odoo version in VSCode:
   ```bash
   code 16.0  # For Odoo 16
   code 17.0  # For Odoo 17
   code 18.0  # For Odoo 18
   ```

3. When prompted, select "Reopen in Container" or use the Command Palette (F1):
   - Choose "Remote-Containers: Reopen in Container"

4. After the initial container build:
   - Access Odoo: http://localhost:80xx (xx = version number)
   - Access Mailpit: http://localhost:81xx (xx = 16/17/18)

## 📁 Workspace Structure

Standard workspace organization:
```
workspace/
├── enterprise/     # Odoo Enterprise modules (optional)
└── custom_repo_1/         # Custom modules
└── custom_repo_2/         # Custom modules
└── custom_repo_.../         # Custom modules
```

## 🛠 Development Tools

- **Python Environment**
  - Black formatter
  - Pylance
  - Debugging configurations

- **VSCode Integration**
  - Odoo snippets
  - Git support
  - XML/Python support
  - Thunder Client

- **Container Tools**
  - ARM64 wkhtmltopdf
  - PostgreSQL utilities
  - Development dependencies

## 🔄 Development Workflow

1. **Module Development**
   - Module creation in workspace directory
   - Configured addons path
   - Python hot-reload support

2. **Database Management**
   - PostgreSQL access via dedicated ports
   - Database initialization tools

3. **Email Testing**
   - Mailpit email capture
   - Web interface for email review

## 🤝 Contributing

Contributions are welcome through:
- Issue reports for bugs or feature requests
- Pull requests for improvements
- Usage feedback and suggestions

## ⚖️ License

This project is available under the MIT License. See [LICENSE](LICENSE) file for details.

## 🏢 About LABISO

Developed and maintained by [LABISO GmbH](https://www.labiso.de), specializing in Odoo development and consulting services. We contribute to the Odoo community through open-source projects and professional services.

---

For inquiries:
- Submit an issue in this repository
- Visit our [website](https://www.labiso.de)
- Connect on [LinkedIn](https://www.linkedin.com/company/labiso-gmbh)
