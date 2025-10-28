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
    # Your Google Cloud Project ID for Vertex AI access (optional, if using Vertex AI)
    GCP_PROJECT_ID="your-google-cloud-project-id"

    # Your Google Cloud location/region for Vertex AI (e.g., us-central1) (optional, if using Vertex AI)
    GOOGLE_CLOUD_LOCATION="your-google-cloud-location"

    # Your Google API Key for direct Gemini API access (optional, if not using Vertex AI)
    GOOGLE_API_KEY="your-google-api-key"
    ```
    *   **`GCP_PROJECT_ID`** and **`GOOGLE_CLOUD_LOCATION`** are needed if you plan to use Vertex AI.
    *   **`GOOGLE_API_KEY`** is needed if you plan to use direct Gemini API access. You should typically use one method or the other.

### Authentication Methods

You can choose between two primary methods for Gemini CLI authentication:

#### 1. Using a Google API Key (Direct Gemini API Access)

This method is simpler if you only need direct access to the Gemini API without the full Vertex AI platform features.

1.  **Obtain an API Key**: Generate a Google API Key from the Google Cloud Console. Ensure it has the necessary permissions to access the Gemini API.
2.  **Set `GOOGLE_API_KEY`**: Add your API key to the `GOOGLE_API_KEY` variable in your `.env` file.
3.  **Usage**: Gemini CLI will automatically pick up this API key.

#### 2. Using Vertex AI (Recommended for Production/Advanced Features)

This method leverages Google Cloud's Vertex AI platform, offering enhanced security, management, and features.

1.  **Configure `.env`**: Ensure `GCP_PROJECT_ID` and `GOOGLE_CLOUD_LOCATION` are set in your `.env` file.
2.  **Authenticate `gcloud` on Host**: To allow the Gemini CLI to access Vertex AI, you need to authenticate with Google Cloud on your host machine. This can be done once, and the credentials will be persisted and available inside your dev containers.
    *   **Install Google Cloud CLI (if not already installed)**: Follow the official Google Cloud documentation to install `gcloud` CLI on your host machine.
    *   **Authenticate**: Open a terminal on your host machine and run the following command:
        ```bash
        gcloud auth application-default login
        ```
        This command will open a browser window for you to log in with your Google account. Once authenticated, the credentials will be stored in `~/.config/gcloud` on your host machine. This directory is mounted into your dev containers, making the authentication available within the container.
3.  **Configure Gemini CLI (Inside Container)**: After authenticating `gcloud` on your host and rebuilding your container, open a terminal *inside your dev container* and start Gemini CLI. Then, use the `/auth` command:
    ```bash
    gemini
    /auth
    ```
    Follow the prompts to select **Google Vertex AI**. Gemini CLI should automatically pick up the `GCP_PROJECT_ID` and `GOOGLE_CLOUD_LOCATION` from your environment variables.

With these steps, the Gemini CLI inside your Odoo development containers will be able to interact with Gemini models using your chosen authentication method.

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
