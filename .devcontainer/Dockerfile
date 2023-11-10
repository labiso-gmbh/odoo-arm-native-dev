# Using debian:bookworm-slim as base image for a smaller footprint
FROM debian:bookworm-slim as base-odoo-17

# Ensuring failure on any error and logging all commands
SHELL ["/bin/bash", "-xeo", "pipefail", "-c"]

# Setting up environment variables for localization
ENV LANG C.UTF-8

# Define TARGETARCH for architecture-specific operations
ARG TARGETARCH

# Install essential packages and dependencies for Odoo and PostgreSQL
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    dirmngr \
    fonts-noto-cjk \
    gnupg \
    libssl-dev \
    node-less \
    npm \
    python3-num2words \
    python3-pdfminer \
    python3-pip \
    python3-phonenumbers \
    python3-pyldap \
    python3-qrcode \
    python3-renderpm \
    python3-setuptools \
    python3-slugify \
    python3-vobject \
    python3-watchdog \
    python3-xlrd \
    python3-xlwt \
    python3-geoip2 \
    python3-rjsmin \
    xz-utils \
    postgresql-client \
    && curl -o wkhtmltox.deb -sSL https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.buster_amd64.deb \
    && curl -o libssl1.1.deb -sSL ftp.us.debian.org/debian/pool/main/o/openssl/libssl1.1_1.1.1w-0+deb11u1_amd64.deb \
    && echo 'ea8277df4297afc507c61122f3c349af142f31e5 wkhtmltox.deb' | sha1sum -c - \
    && echo '975578b8e6cb8a0eb0734f34f3fa59e5507d9053 libssl1.1.deb' | sha1sum -c - \
    && apt-get install -y --no-install-recommends ./wkhtmltox.deb ./libssl1.1.deb \
    && rm -f /etc/apt/sources.list.d/pgdg.list \
    && rm -rf /var/lib/apt/lists/* ./wkhtmltox.deb ./libssl1.1.deb

# Installing rtlcss using npm for RTL language support
RUN npm install -g rtlcss

# Specifying Odoo version as environment variable for better maintainability
ENV ODOO_VERSION 17.0
ARG ODOO_RELEASE=latest

# Install Odoo from the official source
RUN curl -o odoo.deb -sSL http://nightly.odoo.com/${ODOO_VERSION}/nightly/deb/odoo_${ODOO_VERSION}.${ODOO_RELEASE}_all.deb \
    && apt-get update \
    && apt-get -y install --no-install-recommends ./odoo.deb \
    && rm -rf /var/lib/apt/lists/* odoo.deb

# Copying essential scripts and configuration files into the container
COPY ./entrypoint.sh /

# Setting permissions and creating directories for Odoo
RUN mkdir -p /mnt/extra-addons \
    && chown -R odoo /mnt/extra-addons

# Defining volumes for persistence
VOLUME ["/var/lib/odoo", "/mnt/extra-addons"]

# Exposing ports for Odoo services
EXPOSE 8069 8071 8072

# Setting the default config file path
ENV ODOO_RC /etc/odoo/odoo.conf

# Adding utility script for PostgreSQL readiness
COPY wait-for-psql.py /usr/local/bin/wait-for-psql.py

# Switching to non-root user for security
USER odoo

# Default entrypoint and command
ENTRYPOINT ["/entrypoint.sh"]
CMD ["odoo"]

# Creating a secondary stage for additional configurations
FROM base-odoo-17

# Switching back to root user for installation purposes
USER root

# Setting shell options and environment variables
SHELL ["/bin/bash", "-xeo", "pipefail", "-c"]
ARG DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8 ODOO_RC=/etc/odoo/odoo.conf ODOO_VERSION=16 PGHOST=postgres PGPASSWORD=odoo SHELL=/bin/bash

# Installing additional dependencies
RUN echo 'Acquire::https::apt.postgresql.org::Verify-Peer "false";' > /etc/apt/apt.conf.d/99postgresql-cert \
    && mkdir /odoo_files \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
    cups \
    default-jdk \
    gcc \
    git \
    libcups2-dev \
    libwebp-dev \
    python3-dev

# Copying required files and scripts into the container
COPY requirements.txt /odoo_files/requirements.txt
COPY bashrc /odoo_files/.bashrc
COPY odoo-dev-bin /usr/bin/
COPY entrypoint.sh /entrypoint.sh

# Setting permissions and user configurations
RUN chown odoo:odoo /entrypoint.sh \
    && chmod +x /entrypoint.sh \
    && chmod 777 /usr/bin/* \
    && chown -R odoo:odoo /odoo_files \
    && mkdir -p /home/odoo \
    && chown odoo:odoo /home/odoo \
    && usermod -d /home/odoo odoo

# Installing Python dependencies
RUN pip install --break-system-packages --no-cache-dir -r /odoo_files/requirements.txt

# Setting the final entrypoint and user
ENTRYPOINT ["/entrypoint.sh"]
USER odoo

# Setting default shell
ENV SHELL=/bin/bash
