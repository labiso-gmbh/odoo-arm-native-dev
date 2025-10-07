# Stage 1: Base Odoo Installation
FROM arm64v8/debian:bookworm-slim as base-odoo-17

# Set environment variables
ENV LANG=C.UTF-8 \
    DEBIAN_FRONTEND=noninteractive \
    ODOO_VERSION=17.0 \
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
    postgresql-client \
    && curl -o wkhtmltox.deb -sSL https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.bullseye_arm64.deb \
    && curl -o libssl1.1.deb -sSL ftp.us.debian.org/debian/pool/main/o/openssl/libssl1.1_1.1.1w-0+deb11u1_arm64.deb \
    && apt-get install -y --no-install-recommends ./wkhtmltox.deb ./libssl1.1.deb \
    && npm install -g rtlcss \
    && npm install -g @google/gemini-cli \
    && curl -o odoo.deb -sSL http://nightly.odoo.com/${ODOO_VERSION}/nightly/deb/odoo_${ODOO_VERSION}.${ODOO_RELEASE}_all.deb \
    && apt-get install -y --no-install-recommends ./odoo.deb \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && rm -f /etc/apt/sources.list.d/pgdg.list ./wkhtmltox.deb ./libssl1.1.deb ./odoo.deb

# Create directories and set permissions
RUN mkdir -p /mnt/extra-addons \
    && chown -R odoo:odoo /mnt/extra-addons

# Define volumes and expose ports
VOLUME ["/var/lib/odoo", "/mnt/extra-addons"]
EXPOSE 8069 8071 8072

# Stage 2: Development Environment
FROM base-odoo-17

# Install development dependencies and multi-arch support
RUN echo 'Acquire::https::apt.postgresql.org::Verify-Peer "false";' > /etc/apt/apt.conf.d/99postgresql-cert \
    && dpkg --add-architecture amd64 \
    && apt-get update && apt-get install -y --no-install-recommends \
    cups default-jdk gcc git libcups2-dev libwebp-dev python3-dev \
    libc6:amd64 libstdc++6:amd64 libgcc1:amd64 libz1:amd64 \
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

# Install Python dependencies
RUN pip install --break-system-packages --no-cache-dir -r /odoo_files/requirements.txt

# Set user, entrypoint, and default shell
USER odoo
ENV SHELL=/bin/bash
ENTRYPOINT ["/entrypoint.sh"]
