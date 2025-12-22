# Odoo Development Environments (Apple Silicon Optimized)

This project provides a specialized development environment for Odoo (versions 16.0, 17.0, 18.0, 19.0) optimized for Apple Silicon (M-Chips) and ARM64 architectures. It utilizes Docker and VS Code Devcontainers to ensure a consistent, performant, and isolated development experience.

## Project Overview

-   **Goal:** Enable native ARM64 Odoo development, avoiding Rosetta 2 emulation overhead.
-   **Stack:** Docker Compose, VS Code Devcontainers, Debian (bookworm-slim), PostgreSQL, Mailpit.
-   **Versions:** Supports Odoo 16.0, 17.0, 18.0, and 19.0.

## Architecture & Components

The environment is structured to isolate each Odoo version while sharing common configuration patterns.

*   **Docker Container:** Runs the Odoo server and development tools.
*   **PostgreSQL:** Dedicated database container for each version.
    *   **Odoo 19.0+:** Uses `pgvector/pgvector:pg15` to support RAG (Retrieval-Augmented Generation) and vector search capabilities.
*   **Mailpit:** Catches outgoing emails for testing purposes.
*   **Workspace:** A local directory (`workspace/`) mounted into the container, ensuring code persistence and easy access from the host.

## Directory Structure

*   **`[Version]/`** (e.g., `18.0/`, `16.0/`): Contains version-specific configurations.
    *   **`.devcontainer/`**: VS Code Devcontainer configuration (`devcontainer.json`, `docker-compose.yml`, `Dockerfile`).
    *   **`workspace/`**: The main working directory for Odoo modules. This is where you should clone or create your custom addons.
*   **`common/`**: Shared scripts and configuration files used across different versions (e.g., `entrypoint.sh`, `bashrc`).
*   **`.env`**: (Git-ignored) Stores environment variables and secrets, particularly for Gemini CLI and Google Cloud authentication.

## Getting Started

### Prerequisites

*   Apple Silicon Mac or ARM64 system.
*   Docker Desktop.
*   Visual Studio Code with the "Remote - Containers" extension.

### Setup

1.  **Clone the Repository:**
    ```bash
    git clone <repository-url>
    cd odoo-development
    ```

2.  **Configure Environment:**
    Copy `.env.example` to `.env` and configure your Google Cloud credentials (see Gemini CLI section below).
    ```bash
    cp .env.example .env
    ```

3.  **Launch in VS Code:**
    Open the specific version folder you want to work on (e.g., `18.0`) in VS Code.
    ```bash
    code 18.0
    ```

4.  **Start Container:**
    When prompted by VS Code, select **"Reopen in Container"**. Alternatively, use the Command Palette (`F1` or `Cmd+Shift+P`) and search for "Remote-Containers: Reopen in Container".

## Usage & Workflow

### Service Access

Each version runs on specific ports to allow simultaneous execution (though typically you run one at a time).

| Service | 16.0 | 17.0 | 18.0 | 19.0 |
| :--- | :--- | :--- | :--- | :--- |
| **Odoo Web** | `localhost:8016` | `localhost:8017` | `localhost:8018` | `localhost:8019` |
| **Mailpit UI** | `localhost:8116` | `localhost:8117` | `localhost:8118` | `localhost:8119` |
| **PostgreSQL** | `localhost:5436` | `localhost:5437` | `localhost:5438` | `localhost:5439` |

### Development

*   **Source Code:** Place your custom Odoo modules in the `workspace/` directory of the respective version.
*   **Requirements:** The `entrypoint.sh` script automatically installs Python packages from any `requirements.txt` found in the `workspace/` directory on startup.
*   **Odoo 19.0+ Preparation:** Run `19.0/.devcontainer/prepare-devcontainer.sh` on your host before starting the container to set up the GCP key mount.
*   **Tools:** The container comes pre-configured with:
    *   `black` (Python formatter)
    *   VS Code extensions (Python, Odoo Snippets, XML, etc.)
    *   `gemini` CLI

## Gemini CLI Integration

This environment is pre-configured for the Gemini CLI. You can authenticate using one of two methods:

### Method 1: Service Account (Recommended for Vertex AI)

The environment is designed to mount a service account key from your host machine.

1.  **Key Location:** Place your Google Cloud service account JSON key at:
    `~/.config/gcp/vertex-ai-service-account.json` (on your host machine).
2.  **Preparation (Odoo 19.0):** Run the `prepare-devcontainer.sh` script. It creates a `docker-compose.override.yml` that mounts this key to `/home/odoo/.gcp/service-account.json` inside the container.
3.  **Configure `.env`:** Set `GOOGLE_CLOUD_LOCATION` (e.g., `us-central1`) in your `.env` file in the project root.
4.  **Authenticate:** Inside the container, run `gemini` -> `/auth` -> **Google Vertex AI**. The `GOOGLE_APPLICATION_CREDENTIALS` environment variable is automatically set.

### Method 2: API Key

1.  **Get Key:** Obtain a Google API Key.
2.  **Configure `.env`:** Set `GOOGLE_API_KEY="your-key"` in your `.env` file.
3.  **Authenticate:** The CLI will automatically detect the key.
