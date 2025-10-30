#!/bin/bash

# This script is executed before the dev container is started.
# It checks if the GCP service account key file exists and creates
# a docker-compose.override.yml file accordingly.

set -e

GCP_KEY_FILE=~/.config/gcp/vertex-ai-service-account.json
OVERRIDE_FILE=$(dirname "$0")/docker-compose.override.yml

if [ -f "$GCP_KEY_FILE" ]; then
  echo "GCP key file found. Creating override file with mount."
  cat > "$OVERRIDE_FILE" <<EOL
version: "3.9"
services:
  odoo:
    volumes:
      - "$GCP_KEY_FILE:/home/odoo/.gcp/service-account.json:ro"
EOL
else
  echo "GCP key file not found. Creating empty override file."
  echo "version: \"3.9\"" > "$OVERRIDE_FILE"
fi
