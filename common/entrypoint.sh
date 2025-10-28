#!/usr/bin/env bash

# Copy bashrc template if it doesn't exist in the home directory (due to volume mount)
if [ ! -f "/home/odoo/.bashrc" ]; then
  cp /usr/local/etc/bashrc_template /home/odoo/.bashrc
  chown odoo:odoo /home/odoo/.bashrc
fi

find /workspace -name "requirements.txt" -exec pip3 install --break-system-packages -r {} \;

sleep infinity