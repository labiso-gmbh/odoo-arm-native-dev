#!/usr/bin/env bash

# Copy bashrc template if it doesn't exist in the home directory (due to volume mount)
if [ ! -f "/home/odoo/.bashrc" ]; then
  cp /usr/local/etc/bashrc_template /home/odoo/.bashrc
  chown odoo:odoo /home/odoo/.bashrc
fi

# Copy AI agent instruction files to workspace if they don't exist
for file in AGENTS.md CLAUDE.md GEMINI.md; do
  if [ -f "/odoo_files/$file" ] && [ ! -f "/workspace/$file" ]; then
    cp "/odoo_files/$file" "/workspace/$file"
    chown odoo:odoo "/workspace/$file"
  fi
done

find /workspace -name "requirements.txt" -exec pip3 install --break-system-packages -r {} \;

# Update CLI tools on every start via Homebrew
export PATH="/home/linuxbrew/.linuxbrew/bin:/home/linuxbrew/.linuxbrew/sbin:$PATH"
echo "Updating Claude Code CLI and Gemini CLI via Homebrew..."
brew upgrade claude-code gemini-cli 2>/dev/null || true

sleep infinity