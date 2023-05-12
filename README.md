# Odoo-Development Repository for Labiso GmbH

Welcome to the Odoo-Development repository for Labiso GmbH! This repository serves as the common development environment for Odoo, using Visual Studio Code's (VSCode) devcontainers.

## Overview

Odoo is a comprehensive open-source suite of business applications including Sales, CRM, Project management, Warehouse management, Manufacturing, Financial management, and Human Resources just to name a few. Our aim is to simplify and standardize the Odoo development process across our team.

VSCode devcontainers provide a fully configured development environment that can be shared across the team. This ensures consistency across development setups and eliminates the "works on my machine" problem.

## Getting Started

Before you start, you will need to install:

- [Docker](https://docs.docker.com/get-docker/)
- [VSCode](https://code.visualstudio.com/download)
- [VSCode Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

## Usage

To start developing with the Labiso GmbH Odoo development environment, follow these steps:

1. Clone this repository:

    ```bash
    git clone https://github.com/labiso-gmbh/odoo-development
    ```

2. Open the project folder in VSCode.

3. When prompted to "Reopen in Container", select "Reopen in Container". If not prompted, open the Command Palette (`F1` or `Ctrl+Shift+P`), and type "Reopen in Container".

The development environment is now ready to use!

## Structure

The repository is structured as follows:

- `.devcontainer/`: This directory contains the configuration for the devcontainer. It includes the Dockerfile which specifies the image used for the container and a devcontainer.json file which configures the VSCode settings for the environment.
- `workspace/odoo_addons`: This directory contains the Odoo repositories you will actually work on.

## Contributing

We encourage team members to contribute and improve our development environment. Please feel free to make a pull request or open an issue if you encounter any problems or think of any improvements.

## Support

If you encounter any problems or have any questions, please open an issue on this repository.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) file for details.

## Acknowledgements

We'd like to thank the wider community for their contributions to Odoo and VSCode devcontainers, upon which this project is built.

---

Happy coding!
