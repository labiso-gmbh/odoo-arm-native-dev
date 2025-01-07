# Odoo Development Environment for Apple Silicon

Welcome to LABISO's Odoo Development Environment, a cutting-edge solution optimized for Apple Silicon (M1/M2/M3) and ARM64 architectures. This project revolutionizes Odoo development on Apple Silicon by eliminating the need for Rosetta 2 emulation, delivering native performance and superior development experience.

## 🚀 Key Features

- **Native ARM64 Performance**: Engineered specifically for Apple Silicon, eliminating the performance overhead of Rosetta 2 emulation
- **Multi-Version Support**: Preconfigured environments for Odoo 16.0, 17.0, and 18.0
- **Optimized Development Container**: VSCode devcontainer with full ARM64 support
- **Comprehensive Tooling**: Integrated development tools, debugging capabilities, and code formatting
- **Isolated Environments**: Each Odoo version runs in its own container with dedicated services

## 🎯 Why This Matters

Traditional Odoo development on Apple Silicon faces significant challenges:
- Most Odoo Docker images are built for AMD64, requiring Rosetta 2 emulation
- Emulation results in slower build times and reduced performance
- Development tools often run sub-optimally under emulation

Our solution addresses these challenges by:
- Using native ARM64 base images and dependencies
- Optimizing the development environment for Apple Silicon
- Providing a seamless, high-performance development experience

## 🛠 Technical Architecture

### Container Stack
- Base Image: `arm64v8/debian:bookworm-slim`
- Native ARM64 PostgreSQL
- Mailpit for email testing
- Custom development tools and scripts

### Development Features
- VSCode integration with curated extensions
- Black code formatting
- Git integration
- Debugging tools
- Custom Python package management
- Automatic addons path generation

## 📋 Prerequisites

- Apple Silicon Mac (M1/M2/M3) or ARM64-based system
- [Docker Desktop](https://docs.docker.com/get-docker/)
- [Visual Studio Code](https://code.visualstudio.com/download)
- [VSCode Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

## 🚦 Port Configuration

Each Odoo version uses dedicated ports to prevent conflicts:

| Service          | 16.0  | 17.0  | 18.0  |
|-----------------|-------|-------|-------|
| Odoo Web        | 8016  | 8017  | 8018  |
| Odoo Longpolling| 8046  | 8047  | 8048  |
| PostgreSQL      | 5436  | 5437  | 5438  |
| Mailpit SMTP    | 1016  | 1017  | 1018  |
| Mailpit UI      | 8116  | 8117  | 8118  |

## 🏃‍♂️ Getting Started

1. Clone this repository:
   \`\`\`bash
   git clone https://github.com/labiso-gmbh/odoo-development
   cd odoo-development
   \`\`\`

2. Choose your Odoo version and open it in VSCode:
   \`\`\`bash
   code 16.0  # For Odoo 16
   code 17.0  # For Odoo 17
   code 18.0  # For Odoo 18
   \`\`\`

3. When prompted, click "Reopen in Container" or use the Command Palette (F1):
   - Select "Remote-Containers: Reopen in Container"

4. Initial container build will take a few minutes. After that:
   - Odoo web interface: http://localhost:80xx (xx = version number)
   - Mailpit interface: http://localhost:81xx (xx = 16/17/18)

## 📁 Workspace Structure

Each version's workspace contains:
\`\`\`
workspace/
├── odoo/           # Odoo community source code
├── enterprise/     # Odoo Enterprise modules (optional)
└── custom/         # Your custom modules
\`\`\`

## 🛠 Development Tools

- **Python Tools**
  - Black formatter (preconfigured)
  - Pylance for advanced Python support
  - Debug configurations

- **VSCode Extensions**
  - Odoo snippets
  - Git integration
  - XML/Python language support
  - Thunder Client for API testing

- **Container Features**
  - Native ARM64 wkhtmltopdf
  - PostgreSQL client tools
  - Development dependencies

## 🔄 Development Workflow

1. **Module Development**
   - Create new modules in the workspace directory
   - Automatic addons path configuration
   - Hot-reload for Python changes

2. **Database Management**
   - Direct PostgreSQL access via configured ports
   - Automated database initialization

3. **Email Testing**
   - Mailpit for catching all outgoing emails
   - Web interface for email inspection

## 🤝 Contributing

We welcome contributions! Please feel free to:
- Submit issues for bugs or feature requests
- Create pull requests for improvements
- Share your success stories

## ⚖️ License

This project is licensed under the MIT License. See [LICENSE](LICENSE) file for details.

## 🏢 About LABISO

This development environment is maintained by [LABISO GmbH](https://www.labiso.de), a leading Odoo development and consulting company. We're committed to improving the Odoo development experience and giving back to the community through open-source contributions like this one.

---

For support, questions, or collaboration opportunities:
- Open an issue in this repository
- Contact us through our [website](https://www.labiso.de)
- Follow us on [LinkedIn](https://www.linkedin.com/company/labiso-gmbh)
