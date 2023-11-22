FROM mysql:5.7-debian as base

RUN apt-get update && apt-get install -y wget gnupg2

RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add -

RUN echo "deb http://repo.mongodb.org/apt/debian buster/mongodb-org/4.4 main" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list

RUN apt-get update && apt-get install -y \
    mongodb-org \
    awscli \
    && rm -rf /var/lib/apt/lists/*

RUN wget -O /tmp/azcopy.tar.gz https://aka.ms/downloadazcopy-v10-linux \
    && tar -xvf /tmp/azcopy.tar.gz -C /tmp \
    && cp /tmp/azcopy_linux_amd64*/azcopy /usr/bin/ \
    && chmod +x /usr/bin/azcopy \
    && rm -rf /tmp/azcopy*

RUN useradd -m backupuser
RUN echo "backupuser ALL=(ALL) NOPASSWD: /usr/bin/mysql, /usr/bin/mongodump" >> /etc/sudoers

USER backupuser

WORKDIR /data

COPY docker-entrypoint.sh /usr/local/bin/

ENTRYPOINT ["docker-entrypoint.sh"]
