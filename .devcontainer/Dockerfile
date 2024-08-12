# Stage 1: Base Odoo Installation

FROM debian:bookworm-slim as base-odoo-17

# Set environment variables for localization and non-interactive installations
ENV LANG=C.UTF-8 DEBIAN_FRONTEND=noninteractive

# Install essential packages and dependencies
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
    && echo '975578b8e6cb8a0eb0734f3fa59e5507d9053 libssl1.1.deb' | sha1sum -c - \
    && apt-get install -y --no-install-recommends ./wkhtmltox.deb ./libssl1.1.deb \
    && rm -f /etc/apt/sources.list.d/pgdg.list \
    && rm -rf /var/lib/apt/lists/* ./wkhtmltox.deb ./libssl1.1.deb

# Install rtlcss for RTL language support
RUN npm install -g rtlcss

# Define Odoo version and release
ENV ODOO_VERSION 17.0
ARG ODOO_RELEASE=latest

# Install Odoo
RUN curl -o odoo.deb -sSL http://nightly.odoo.com/${ODOO_VERSION}/nightly/deb/odoo_${ODOO_VERSION}.${ODOO_RELEASE}_all.deb \
    && apt-get update \
    && apt-get -y install --no-install-recommends ./odoo.deb \
    && rm -rf /var/lib/apt/lists/* odoo.deb

# Create directories and set permissions
RUN mkdir -p /mnt/extra-addons \
    && chown -R odoo:odoo /mnt/extra-addons

# Define volumes for persistence
VOLUME ["/var/lib/odoo", "/mnt/extra-addons"]

# Expose ports for Odoo services
EXPOSE 8069 8071 8072

# Set the default Odoo config file path
ENV ODOO_RC /etc/odoo/odoo.conf

# Stage 2: Development Environment

FROM base-odoo-17

# Install additional development dependencies
RUN echo 'Acquire::https::apt.postgresql.org::Verify-Peer "false";' > /etc/apt/apt.conf.d/99postgresql-cert \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
    cups \
    default-jdk \
    gcc \
    git \
    libcups2-dev \
    libwebp-dev \
    python3-dev

# Install the odoo command line upgrade tool
RUN curl -s https://upgrade.odoo.com/upgrade -o /usr/local/bin/odoo-upgrade \
    && chmod +x /usr/local/bin/odoo-upgrade

# Copy project files and scripts
COPY requirements.txt /odoo_files/requirements.txt
COPY bashrc /odoo_files/.bashrc
COPY odoo-dev-bin /usr/bin/
COPY entrypoint.sh /entrypoint.sh
COPY wait-for-psql.py /usr/local/bin/wait-for-psql.py

# Set permissions and user configurations
RUN chown odoo:odoo /entrypoint.sh \
    && chmod +x /entrypoint.sh \
    && chmod 777 /usr/bin/* \
    && chown -R odoo:odoo /odoo_files \
    && mkdir -p /home/odoo \
    && chown odoo:odoo /home/odoo \
    && usermod -d /home/odoo odoo

# Install Python dependencies
RUN pip install --break-system-packages --no-cache-dir -r /odoo_files/requirements.txt

# Set the entrypoint and user
USER odoo
ENTRYPOINT ["/entrypoint.sh"]

# Set default shell
ENV SHELL=/bin/bash
