# Stage 1: Base Odoo Installation
FROM arm64v8/ubuntu:noble AS base-odoo-18

# Set environment variables
ENV LANG=C.UTF-8 \
    DEBIAN_FRONTEND=noninteractive \
    ODOO_VERSION=18.0 \
    ODOO_RELEASE=latest \
    ODOO_RC=/workspace/.vscode/odoo.conf

# Install dependencies and Odoo
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates curl dirmngr fonts-noto-cjk gnupg libssl-dev \
    node-less npm python3-num2words python3-pdfminer python3-pip \
    python3-phonenumbers python3-pyldap python3-qrcode python3-renderpm \
    python3-setuptools python3-slugify python3-vobject python3-watchdog \
    python3-xlrd python3-xlwt python3-geoip2 python3-rjsmin xz-utils \
    openssh-client rsync tesseract-ocr tesseract-ocr-eng tesseract-ocr-deu \
    postgresql-client wget \
    && wget -O wkhtmltox.deb https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-3/wkhtmltox_0.12.6.1-3.jammy_arm64.deb \
    && apt-get install -y --no-install-recommends ./wkhtmltox.deb \
    && npm install -g rtlcss \
    && curl -o odoo.deb -sSL http://nightly.odoo.com/${ODOO_VERSION}/nightly/deb/odoo_${ODOO_VERSION}.${ODOO_RELEASE}_all.deb \
    && apt-get install -y --no-install-recommends ./odoo.deb \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && rm -f /etc/apt/sources.list.d/pgdg.list ./wkhtmltox.deb ./odoo.deb

# Create directories and set permissions
RUN mkdir -p /mnt/extra-addons \
    && chown -R odoo:odoo /mnt/extra-addons

# Define volumes and expose ports
VOLUME ["/var/lib/odoo", "/mnt/extra-addons"]
EXPOSE 8069 8071 8072

# Stage 2: Development Environment
FROM base-odoo-18

# Install development dependencies
# Install ARM64 development dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cups \
    default-jdk \
    gcc \
    git \
    libcups2-dev \
    libwebp-dev \
    python3-dev \
    python3-venv \
    software-properties-common \
    wget \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install odoo-upgrade tool
RUN curl -s https://upgrade.odoo.com/upgrade -o /usr/local/bin/odoo-upgrade \
    && chmod +x /usr/local/bin/odoo-upgrade \
    && ln -s /usr/bin/python3 /usr/bin/python

# Copy project files and scripts
COPY requirements.txt /odoo_files/
COPY bashrc /odoo_files/.bashrc
COPY odoo-dev-bin /usr/bin/
COPY entrypoint.sh /
COPY wait-for-psql.py /usr/local/bin/

# Set permissions and user configurations
RUN chown odoo:odoo /entrypoint.sh && chmod +x /entrypoint.sh \
    && chmod 755 /usr/bin/* \
    && chown -R odoo:odoo /odoo_files \
    && mkdir -p /home/odoo && chown odoo:odoo /home/odoo \
    && usermod -d /home/odoo odoo

# Install Python dependencies with ARM64 optimizations
RUN pip install --break-system-packages --no-cache-dir -r /odoo_files/requirements.txt

# Set user, entrypoint, and default shell
USER odoo
ENV SHELL=/bin/bash
ENTRYPOINT ["/entrypoint.sh"]
