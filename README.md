# Odoo Development Environment for Apple Silicon

A development environment optimized for Odoo on Apple Silicon (M-Chips) and ARM64 architectures. This project provides native ARM64 support for Odoo development, offering improved performance by eliminating the need for Rosetta 2 emulation.

## 🚀 Key Features

- Native ARM64 support optimized for Apple Silicon
- Development environments for Odoo 16.0, 17.0, 18.0, and 19.0
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

| Service          | 16.0  | 17.0  | 18.0  | 19.0  |
|-----------------|-------|-------|-------|-------|
| Odoo Web        | 8016  | 8017  | 8018  | 8019  |
| Odoo Longpolling| 8046  | 8047  | 8048  | 8049  |
| PostgreSQL      | 5436  | 5437  | 5438  | 5439  |
| Mailpit SMTP    | 1016  | 1017  | 1018  | 1019  |
| Mailpit UI      | 8116  | 8117  | 8118  | 8119  |

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
   code 19.0  # For Odoo 19
   ```

3. When prompted, select "Reopen in Container" or use the Command Palette (F1):
   - Choose "Remote-Containers: Reopen in Container"

4. After the initial container build:
   - Access Odoo: http://localhost:80xx (xx = version number)
   - Access Mailpit: http://localhost:81xx (xx = 16/17/18/19)

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

## ☁️ Gemini CLI Authentication

This development environment supports flexible authentication for the Gemini CLI, allowing you to use either a Google API Key for direct access or integrate with Google Cloud's Vertex AI.

### Environment Variables (.env file)

To manage your authentication credentials and Google Cloud project details, a `.env` file is used. This file is ignored by Git (`.gitignore`) to prevent sensitive information from being committed.

1.  **Create your `.env` file**: Copy the provided `.env.example` file to `.env` in the root of this project:
    ```bash
    cp .env.example .env
    ```

2.  **Configure your `.env` file**: Open the newly created `.env` file and fill in the relevant details:
    ```ini
    # .env
    # Your Google Cloud Project ID for Vertex AI access
    GCP_PROJECT_ID="your-google-cloud-project-id"

    # Your Google Cloud location/region for Vertex AI (e.g., us-central1)
    GOOGLE_CLOUD_LOCATION="your-google-cloud-location"

    # Path to your Google Cloud Service Account JSON key file on the host machine
    GCP_SERVICE_ACCOUNT_KEY_FILE="/path/to/your/service-account-file.json"

    # Your Google API Key for direct Gemini API access (optional)
    GOOGLE_API_KEY="your-google-api-key"
    ```
    *   **`GCP_PROJECT_ID`**, **`GOOGLE_CLOUD_LOCATION`**, and **`GCP_SERVICE_ACCOUNT_KEY_FILE`** are needed if you plan to use Vertex AI.
    *   **`GOOGLE_API_KEY`** is an alternative if you prefer direct Gemini API access.

### Authentication Methods

You can choose between two primary methods for Gemini CLI authentication:

#### 1. Using a Service Account (Recommended for Vertex AI)

This method uses a Google Cloud Service Account JSON key file for robust and persistent authentication. It is the **recommended** approach for using Vertex AI.

1.  **Create and Download a Service Account Key**:
    *   In the Google Cloud Console, navigate to "IAM & Admin" > "Service Accounts".
    *   Create a new service account or select an existing one.
    *   Grant it the necessary roles (e.g., "Vertex AI User").
    *   Create a new JSON key and download it to a secure location on your host machine.

2.  **Configure `.env`**:
    *   Set `GCP_PROJECT_ID` and `GOOGLE_CLOUD_LOCATION` in your `.env` file.
    *   Set `GCP_SERVICE_ACCOUNT_KEY_FILE` to the absolute path of the downloaded JSON key file on your host machine.

3.  **Rebuild Your Container**: If the container is already running, you'll need to rebuild it for the changes to take effect. In VSCode, you can use the command "Remote-Containers: Rebuild Container".

4.  **Configure Gemini CLI (Inside Container)**:
    *   Open a terminal *inside your dev container* and start Gemini CLI: `gemini`
    *   Use the `/auth` command and select **Google Vertex AI**. Gemini CLI will automatically use the service account credentials mounted into the container.

#### 2. Using a Google API Key (Direct Gemini API Access)

This method is simpler if you only need direct access to the Gemini API without the full Vertex AI platform features.

1.  **Obtain an API Key**: Generate a Google API Key from the Google Cloud Console.
2.  **Set `GOOGLE_API_KEY`**: Add your API key to the `GOOGLE_API_KEY` variable in your `.env` file.
3.  **Usage**: Gemini CLI will automatically pick up this API key.

#### 3. Using `gcloud auth application-default login` (Legacy Method)

This method is now considered **outdated** but remains available for users who prefer not to use service accounts. It relies on credentials generated on the host machine.

1.  **Authenticate `gcloud` on Host**:
    *   Install the Google Cloud CLI (`gcloud`) on your host machine.
    *   Run `gcloud auth application-default login`. This stores credentials in `~/.config/gcloud`.
2.  **Limitation**: This method can lead to sessions that expire, requiring you to re-authenticate periodically. The service account method is more stable for long-term development.

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
