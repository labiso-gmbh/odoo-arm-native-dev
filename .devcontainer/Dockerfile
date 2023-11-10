FROM odoo:17.0

USER root

SHELL ["/bin/bash", "-xo", "pipefail", "-c"]

ARG DEBIAN_FRONTEND=noninteractive ODOO_UID=1000 ODOO_GID=1000
ENV LANG=C.UTF-8 ODOO_RC=/etc/odoo/odoo.conf ODOO_VERSION=16 PGHOST=postgres PGPASSWORD=odoo SHELL=/bin/bash

# PPA of Postgres has a certificate problem, so disable the check
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

COPY requirements.txt /odoo_files/requirements.txt
COPY bashrc /odoo_files/.bashrc
COPY odoo-dev-bin /usr/bin/
COPY entrypoint.sh /entrypoint.sh

RUN chown odoo:odoo /entrypoint.sh \
    && chmod +x /entrypoint.sh \
    && chmod 777 /usr/bin/* \
    && chown -R odoo:odoo /odoo_files \
    && mkdir -p /home/odoo \
    && chown odoo:odoo /home/odoo \
    && usermod -d /home/odoo odoo

RUN pip install --no-cache-dir -r /odoo_files/requirements.txt

ENTRYPOINT ["/entrypoint.sh"]

USER odoo

ENV SHELL=/bin/bash