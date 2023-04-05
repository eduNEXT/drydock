FROM mysql:5.7-debian as base

RUN apt-get update && apt-get install -y wget gnupg2

RUN wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | apt-key add -

RUN echo "deb http://repo.mongodb.org/apt/debian buster/mongodb-org/6.0 main" | tee /etc/apt/sources.list.d/mongodb-org-6.0.list

RUN apt-get update && apt-get install -y \
    mongodb-org \
    awscli \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m backupuser
RUN echo "backupuser ALL=(ALL) NOPASSWD: /usr/bin/mysql, /usr/bin/mongodump" >> /etc/sudoers

USER backupuser

WORKDIR /home/backupuser

RUN echo
