# NOMAGIC ATTACHMENT: TWC-Container-Example-Pkg.zip

- attachment_id: `189149971`
- space_key: `TWCloud2024xR2`
- parent_page_id: `189149970`
- parent_page_title: Building Teamwork Cloud containers
- media_type: `application/zip`
- reported_bytes: 11306
- download_url: https://docs.nomagic.com/download/attachments/189149970/TWC-Container-Example-Pkg.zip?version=3&modificationDate=1757080215388&api=v2
- payload_kind: `archive-expanded`
- downloaded_sha256: `2086672158fb882649102b63fbcad947fdb47a2cb6bb54c3797645b42343e32b`

## ARCHIVE CONTENTS

### ENTRY: cassandra/Dockerfile

- bytes: 951
- crc32: `ef85bc41`
- decoded_as: `utf-8`

````text
FROM cassandra:4.1.1

RUN echo "-Xlog:gc=info,heap*=info,age*=info,safepoint=info,promotion*=info:file=/var/log/cassandra/gc.log:time,uptime,pid,tid,level:filecount=10,filesize=10485760" >> /etc/cassandra/jvm11-server.options

RUN sed -i -e 's/^#commitlog_segment_size:.*/commitlog_segment_size: 192MiB/' \
       -e 's/^read_request_timeout:.*/read_request_timeout: 1800000ms/' \
       -e 's/^range_request_timeout:.*/range_request_timeout: 1800000ms/' \
       -e 's/^write_request_timeout:.*/write_request_timeout: 1800000ms/' \
       -e 's/^cas_contention_timeout:.*/cas_contention_timeout: 1000ms/' \
       -e 's/^truncate_request_timeout:.*/truncate_request_timeout: 1800000ms/' \
       -e 's/^request_timeout:.*/request_timeout: 1800000ms/' \
       -e 's/^batch_size_warn_threshold:.*/batch_size_warn_threshold: 3000KiB/' \
       -e 's/^batch_size_fail_threshold:.*/batch_size_fail_threshold: 5000KiB/' \
		/etc/cassandra/cassandra.yaml


````

### ENTRY: messaging/docker.scripts/docker-run.sh

- bytes: 1475
- crc32: `265f7f9f`
- decoded_as: `utf-8`

````text
#!/bin/bash
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.



# This is the entry point for the docker images.
# This file is executed when docker run is called.


set -e

BROKER_HOME=/var/lib/
CONFIG_PATH=$BROKER_HOME/etc
export BROKER_HOME OVERRIDE_PATH CONFIG_PATH

if [[ ${ANONYMOUS_LOGIN,,} == "true" ]]; then
  LOGIN_OPTION="--allow-anonymous"
else
  LOGIN_OPTION="--require-login"
fi

CREATE_ARGUMENTS="--user ${ARTEMIS_USER} --password ${ARTEMIS_PASSWORD} --silent ${LOGIN_OPTION} ${EXTRA_ARGS}"

echo CREATE_ARGUMENTS=${CREATE_ARGUMENTS}

if ! [ -f ./etc/broker.xml ]; then
    /opt/activemq-artemis/bin/artemis create ${CREATE_ARGUMENTS} .
else
    echo "broker already created, ignoring creation"
fi

exec ./bin/artemis "$@"


````

### ENTRY: messaging/Dockerfile

- bytes: 2164
- crc32: `a9848b81`
- decoded_as: `utf-8`

````text
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# ActiveMQ Artemis

FROM adoptopenjdk:11-jre-hotspot
LABEL maintainer="Apache ActiveMQ Team"
# Make sure pipes are considered to determine success, see: https://github.com/hadolint/hadolint/wiki/DL4006
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
WORKDIR /opt

ENV ARTEMIS_USER artemis
ENV ARTEMIS_PASSWORD artemis
ENV ANONYMOUS_LOGIN false
ENV EXTRA_ARGS --http-host 0.0.0.0 --relax-jolokia

# add user and group for artemis
RUN groupadd -g 1000 -r artemis && useradd -r -u 1000 -g artemis artemis \
 && apt-get -qq -o=Dpkg::Use-Pty=0 update && \
    apt-get -qq -o=Dpkg::Use-Pty=0 install -y libaio1 netcat && \
    rm -rf /var/lib/apt/lists/*

USER artemis

ADD ./apache-artemis/ /opt/activemq-artemis/

# Web Server
EXPOSE 8161 
# Port for CORE,MQTT,AMQP,HORNETQ,STOMP,OPENWIRE
EXPOSE 61616 
# JMX Exporter    9404 
# Port for HORNETQ,STOMP    5445 
# Port for AMQP    5672 
# Port for MQTT    1883 
# Port for STOMP    61613

USER root

RUN mkdir /var/lib/artemis-instance && chown -R artemis.artemis /var/lib/artemis-instance

#RUN cp -r /opt/activemq-artemis/* /var/lib/artemis-instance/

COPY ./docker.scripts/docker-run.sh /scripts/

USER artemis

# Expose some outstanding folders
VOLUME ["/var/lib/artemis-instance"]
WORKDIR /var/lib/artemis-instance

ENTRYPOINT ["/scripts/docker-run.sh"]
CMD ["run"]

````

### ENTRY: twcloud/docker.scripts/entrypoint.sh

- bytes: 734
- crc32: `ddec5e7f`
- decoded_as: `utf-8`

````text
#!/bin/bash

echo "JAVA_HOME=${JAVA_HOME}"
echo "TWCLOUD_OPTS=${TWCLOUD_OPTS}"

echo ======================================================
free -h
echo ======================================================
java -version
echo ======================================================

ls -la

sed -i 's/\r//g' twcloud
sed -i 's/\r//g' jvm.options
sed -i 's/\r//g' configuration/application.conf
echo ======================================================
cat configuration/application.conf
echo ======================================================
cat jvm.options
echo ======================================================
echo "Starting..."
./twcloud
echo "Exiting... $?"
echo ======================================================

````

### ENTRY: twcloud/docker.scripts/init.sh

- bytes: 176
- crc32: `597f647d`
- decoded_as: `utf-8`

````text
#!/bin/bash
echo "=== INIT ==="

apt-get -y update && apt-get -y upgrade && apt-get -y install apt-utils sudo wget netcat && rm -rf /var/lib/apt/lists/*

echo "/=== INIT ===/"

````

### ENTRY: twcloud/Dockerfile

- bytes: 320
- crc32: `b82e4b7f`
- decoded_as: `utf-8`

````text
FROM eclipse-temurin:17.0.8.1_1-jdk
RUN apt-get -y update && apt-get -y upgrade && apt-get -y install apt-utils sudo wget netcat && rm -rf /var/lib/apt/lists/*
COPY docker.scripts /scripts
RUN sh /scripts/init.sh
COPY TeamworkCloud /twcloud
WORKDIR /twcloud
EXPOSE 8111 3579
VOLUME /certs
CMD ["/scripts/entrypoint.sh"]

````

### ENTRY: webapp/docker.scripts/run.sh

- bytes: 3604
- crc32: `81c6171e`
- decoded_as: `utf-8`

````text
#!/bin/bash
echo "ZOOKEEPER_HOST=${ZOOKEEPER_HOST}"
echo "CASSANDRA_HOST=${CASSANDRA_HOST}"
echo "TWC_HOST=${TWC_HOST}"
echo "MESSAGING_EXTERNAL=${MESSAGING_EXTERNAL}"
echo "MESSAGING_HOST=${MESSAGING_HOST}"
echo "MESSAGING_PORT=${MESSAGING_PORT}"
echo "REDIRECT_WHITELIST=${REDIRECT_WHITELIST}"
echo "JAVA_HOME=${JAVA_HOME}"

# debug
pwd

if [ -n "${REDIRECT_WHITELIST}" ]; then
  sed -i "s|^authentication.redirect.uri.whitelist=.*$|authentication.redirect.uri.whitelist=${REDIRECT_WHITELIST}|" shared/conf/authserver.properties
fi
if [ -n "${CASSANDRA_HOST}" ]; then
  sed -i "s|^cassandra.contactPoints=.*$|cassandra.contactPoints=${CASSANDRA_HOST}|" shared/conf/authserver.properties
fi
sed -i "s|^#authentication.client.ids=.*$|authentication.client.ids=MAGICDRAW,webApplicationPlatform,twcSynchronizationManager,twc-rest-api|" shared/conf/authserver.properties

if [ -n "${TWC_HOST}" ]; then
  sed -i "s|^twc.ip=.*$|twc.ip=${TWC_HOST}|" shared/conf/webappplatform.properties
fi
if [ -n "${ZOOKEEPER_HOST}" ]; then
  sed -i "s|^zookeeper.server.ip=.*$|zookeeper.server.ip=${ZOOKEEPER_HOST}|" shared/conf/webappplatform.properties
fi
if [ -n "${MESSAGING_EXTERNAL}" ]; then
  if [ "${MESSAGING_EXTERNAL}" = true ]; then
    sed -i "s|^messaging.server.start=.*$|messaging.server.start=false|" shared/conf/webappplatform.properties
    sed -i "s|^messaging.server.ip=.*$|messaging.server.ip=${MESSAGING_HOST}|" shared/conf/webappplatform.properties
    sed -i "s|^messaging.server.port=.*$|messaging.server.port=${MESSAGING_PORT}|" shared/conf/webappplatform.properties
  else
    sed -i "s|^messaging.server.start=.*$|messaging.server.start=true|" shared/conf/webappplatform.properties
	sed -i "s|^messaging.server.ip=.*$|messaging.server.ip=127.0.0.1|" shared/conf/webappplatform.properties
  fi
fi
if [ -n "${MESSAGING_SECURITY_ENABLED}" ]; then
	if [ "${MESSAGING_SECURITY_ENABLED}" = true ]; then
		sed -i "s|.*messaging.server.security.enabled=.*$|messaging.server.security.enabled=true|" shared/conf/webappplatform.properties
		sed -i "s|.*messaging.user.name=.*$|messaging.user.name=${MESSAGING_SECURITY_USERNAME}|" shared/conf/webappplatform.properties
		sed -i "s|.*messaging.user.password=.*$|messaging.user.password=${MESSAGING_SECURITY_PASSWORD}|" shared/conf/webappplatform.properties
		
	else
		sed -i "s|.*messaging.server.security.enabled=.*$|messaging.server.security.enabled=false|" shared/conf/webappplatform.properties
	fi
fi

# TODO need to pass external IP/HOSTNAME
#sed -i "s|^authentication.server.ip=.*$|authentication.server.ip=kns-waptwc1.dsone.3ds.com|" shared/conf/webappplatform.properties
sed -i "s|^authentication.server.ip=.*$|authentication.server.ip=host.docker.internal|" shared/conf/webappplatform.properties

echo "" >> shared/conf/webappplatform.properties
echo "ignore.wap.twc.compatibility=true" >> shared/conf/webappplatform.properties

sed -i "s|^authentication.server.key-store=.*$|authentication.server.key-store=certs/webapp.p12|" shared/conf/authserver.properties
sed -i "s|^authentication.server.key-alias=.*$|authentication.server.key-alias=webapp|" shared/conf/authserver.properties
sed -i 's|certificateKeystoreFile="../TeamworkCloud/configuration/keystore.p12"|certificateKeystoreFile="certs/webapp.p12"|' conf/server.xml

#debug
mkdir -p logs/bak
cp shared/conf/authserver.properties logs/bak/authserver.properties
cp shared/conf/webappplatform.properties logs/bak/webappplatform.properties
cp conf/server.xml logs/bak/server.xml
echo -----------------------------------------------------------

bash ./bin/catalina.sh run >> logs/output.log 2>&1
````

### ENTRY: webapp/Dockerfile

- bytes: 425
- crc32: `86421ea8`
- decoded_as: `utf-8`

````text
FROM openjdk:17.0.2-jdk
RUN microdnf install -y sudo && microdnf install -y wget && microdnf install -y nc

ARG TOMCAT_DIR=/webapp
ARG SET_ENV_FILE=${TOMCAT_DIR}/bin/setenv.sh

COPY docker.scripts /scripts
COPY WebAppPlatform /webapp

RUN echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' >> ${SET_ENV_FILE}
RUN chmod o+x ${SET_ENV_FILE}

WORKDIR /webapp
EXPOSE 8443 8080
CMD ["sh", "/scripts/run.sh"]

````

### ENTRY: cleanup.sh

- bytes: 117
- crc32: `d4ec03a4`
- decoded_as: `utf-8`

````text
#!/usr/bin/env bash
rm -r CATIANoMagicServices
rm -r data
rm -r twcloud/TeamworkCloud
rm -r webapp/WebAppPlatform
````

### ENTRY: docker-compose.3-3.yaml

- bytes: 7112
- crc32: `180b8350`
- decoded_as: `utf-8`

````yaml
version: '2.4'
services:
  zookeeper:
    image: zookeeper:3.7.0
    restart: unless-stopped
    mem_limit: 2g
    volumes:
      - ./data/zookeeper/data:/data
      - ./data/zookeeper/datalog:/datalog
      - ./data/zookeeper/logs:/logs
    healthcheck:
      test: [ "CMD", "echo", "ruok", "|", "nc -w2 zookeeper 4444" ]
      interval: 5s
      timeout: 10s
      retries: 3
  zoonavigator:
    image: elkozmon/zoonavigator:1.1.1
    restart: unless-stopped
    mem_limit: 1g
    ports:
      - "9000:9000"
    environment:
      - "CONNECTION_MYZK_CONN=zookeeper:2181"
      - "CONNECTION_LOCAL_CONN=localhost:2181"
      - "AUTO_CONNECT_CONNECTION_ID=MYZK"
    depends_on:
      zookeeper:
        condition: service_healthy
  elasticsearch:
    image: elasticsearch:7.16.2
    restart: unless-stopped
    mem_limit: 2g
    ports:
      - "9200:9200"
    environment:
      - discovery.type=single-node
      - cluster.routing.allocation.disk.threshold_enabled=false
      - "ES_JAVA_OPTS=-Xms2000M -Xmx2000M"
    volumes:
      - ./data/elasticsearch:/usr/share/elasticsearch/data
    healthcheck:
      test: [ "CMD", "nc", "-z", "-w2", "localhost", "9200"]
      interval: 5s
      timeout: 5s
      retries: 60
  cassandra:
    build: cassandra
    restart: unless-stopped
    mem_limit: 2g
    ports:
      - "9042:9042"
      - "9160:9160"
    environment:
      - CASSANDRA_SEEDS=cassandra
      - CASSANDRA_LISTEN_ADDRESS=cassandra
      - MAX_HEAP_SIZE=1000M
      - HEAP_NEWSIZE=100M
      - CASSANDRA_REPLICATION_FACTOR=3
    volumes:
      - ./data/cassandra:/var/lib/cassandra
    healthcheck:
      test: [ "CMD", "cqlsh", "-e", "describe keyspaces" ]
      interval: 5s
      timeout: 5s
      retries: 60
  cassandra2:
    build: cassandra
    restart: unless-stopped
    mem_limit: 1g
    ports:
      - "9043:9042"
      - "9161:9160"
    environment:
      - CASSANDRA_SEEDS=cassandra
      - CASSANDRA_LISTEN_ADDRESS=cassandra2
      - MAX_HEAP_SIZE=1000M
      - HEAP_NEWSIZE=100M
    volumes:
      - ./data/cassandra2:/var/lib/cassandra
    healthcheck:
      test: [ "CMD", "cqlsh", "-e", "describe keyspaces" ]
      interval: 5s
      timeout: 5s
      retries: 60
    depends_on:
      cassandra:
        condition: service_healthy
  cassandra3:
    build: cassandra
    restart: unless-stopped
    mem_limit: 1g
    ports:
      - "9044:9042"
      - "9162:9160"
    environment:
      - CASSANDRA_SEEDS=cassandra
      - CASSANDRA_LISTEN_ADDRESS=cassandra3
      - MAX_HEAP_SIZE=1000M
      - HEAP_NEWSIZE=100M
    volumes:
      - ./data/cassandra3:/var/lib/cassandra
    healthcheck:
      test: [ "CMD", "cqlsh", "-e", "describe keyspaces" ]
      interval: 5s
      timeout: 5s
      retries: 60
    depends_on:
      cassandra:
        condition: service_healthy
  twcloud:
    build: twcloud
    restart: unless-stopped
    mem_limit: 3g
    ports:
      - "8111:8111"
      - "3579:3579"
    environment:
      - TWCLOUD_OPTS=
        -Xmx3000M
        -Desi.httpd.ssl.keystorePath=certs/twcloud.p12
        -Dakka.cluster.seed-nodes.0=akka://twcloud@twcloud:2552
        -Desi.persistence.datastax-java-driver.basic.contact-points.0=cassandra:9042
        -Desi.indexer.enabled=true
        -Desi.server.actor.query.component-enabled=true
        -Desi.auth.url=https://host.docker.internal:8443
        -Desi.auth.https.file=certs/trust/webapp.crt
        -Desi.zookeeper.url=zookeeper:2181
        -Desi.query.es.node.host=elasticsearch
    volumes:
      - ./data/twcloud/certs:/twcloud/certs
    healthcheck:
      test: [ "CMD", "nc", "-z", "-w2", "localhost", "3579" ]
      interval: 5s
      timeout: 5s
      retries: 60
    depends_on:
      cassandra:
        condition: service_healthy
      elasticsearch:
        condition: service_healthy
  twcloud2:
    build: twcloud
    restart: unless-stopped
    mem_limit: 3g
    ports:
      - "8112:8111"
      - "3580:3579"
    environment:
      - TWCLOUD_OPTS=
        -Xmx3000M
        -Desi.httpd.ssl.keystorePath=certs/twcloud.p12
        -Dakka.cluster.seed-nodes.0=akka://twcloud@twcloud:2552
        -Desi.persistence.datastax-java-driver.basic.contact-points.0=cassandra:9042
        -Desi.indexer.enabled=true
        -Desi.server.actor.query.component-enabled=true
        -Desi.auth.url=https://host.docker.internal:8443
        -Desi.auth.https.file=certs/trust/webapp.crt
        -Desi.zookeeper.url=zookeeper:2181
        -Desi.query.es.node.host=elasticsearch
    volumes:
      - ./data/twcloud2/certs:/twcloud/certs
    healthcheck:
      test: [ "CMD", "nc", "-z", "-w2", "localhost", "3579" ]
      interval: 5s
      timeout: 5s
      retries: 60
    depends_on:
      cassandra:
        condition: service_healthy
      elasticsearch:
        condition: service_healthy
      twcloud:
        condition: service_healthy
  twcloud3:
    build: twcloud
    restart: unless-stopped
    mem_limit: 3g
    ports:
      - "8113:8111"
      - "3581:3579"
    environment:
      - TWCLOUD_OPTS=
        -Xmx3000M
        -Desi.httpd.ssl.keystorePath=certs/twcloud.p12
        -Dakka.cluster.seed-nodes.0=akka://twcloud@twcloud:2552
        -Desi.persistence.datastax-java-driver.basic.contact-points.0=cassandra:9042
        -Desi.indexer.enabled=true
        -Desi.server.actor.query.component-enabled=true
        -Desi.auth.url=https://host.docker.internal:8443
        -Desi.auth.https.file=certs/trust/webapp.crt
        -Desi.zookeeper.url=zookeeper:2181
        -Desi.query.es.node.host=elasticsearch
    volumes:
      - ./data/twcloud3/certs:/twcloud/certs
    healthcheck:
      test: [ "CMD", "nc", "-z", "-w2", "localhost", "3579" ]
      interval: 5s
      timeout: 5s
      retries: 60
    depends_on:
      cassandra:
        condition: service_healthy
      elasticsearch:
        condition: service_healthy
      twcloud:
        condition: service_healthy
  messaging:
    build: messaging
    mem_limit: 2g
    ports:
      - "61616:61616"
      - "8161:8161"
    healthcheck:
      test: [ "CMD", "nc", "-z", "-w2", "localhost", "61616" ]
      interval: 5s
      timeout: 10s
      retries: 3
  webapp:
    build: webapp
    restart: unless-stopped
    mem_limit: 2g
    ports:
      - "8443:8443"
    environment:
      - ZOOKEEPER_HOST=zookeeper
      - CASSANDRA_HOST=cassandra
      - TWC_HOST=twcloud
      - MESSAGING_EXTERNAL=true
      - MESSAGING_HOST=messaging
      - MESSAGING_PORT=61616
      - REDIRECT_WHITELIST=http
    volumes:
      - ./data/webapp/certs:/webapp/certs
      - ./data/webapp/logs:/webapp/logs
    healthcheck:
      test: [ "CMD", "nc", "-z", "-w2", "localhost", "8443" ]
      interval: 5s
      timeout: 5s
      retries: 60
    depends_on:
      cassandra:
        condition: service_healthy
      twcloud:
        condition: service_healthy
      messaging:
        condition: service_healthy

````

### ENTRY: docker-compose.yml

- bytes: 3927
- crc32: `9de70a1d`
- decoded_as: `utf-8`

````yaml
version: '2.4'
services:
  zookeeper:
    image: zookeeper:3.7.0
    mem_limit: 2g
#    volumes:
#      - ./data/zookeeper/data:/data
#      - ./data/zookeeper/datalog:/datalog
#      - ./data/zookeeper/logs:/logs
    healthcheck:
      test: [ "CMD", "echo", "ruok", "|", "nc -w 2 zookeeper 4444" ]
      interval: 5s
      timeout: 10s
      retries: 3
  zoonavigator:
    image: elkozmon/zoonavigator:1.1.1
    ports:
      - "9000:9000"
    environment:
      - "CONNECTION_MYZK_CONN=zookeeper:2181"
      - "CONNECTION_LOCAL_CONN=localhost:2181"
      - "AUTO_CONNECT_CONNECTION_ID=MYZK"
    depends_on:
      zookeeper:
        condition: service_healthy
  elasticsearch:
    image: elasticsearch:7.16.2
    mem_limit: 2g
    ports:
      - "9200:9200"
    environment:
      - discovery.type=single-node
      - cluster.routing.allocation.disk.threshold_enabled=false
      - "ES_JAVA_OPTS=-Xms2000M -Xmx2000M"
#    volumes:
#      - ./data/elasticsearch:/usr/share/elasticsearch/data
    healthcheck:
      test: [ "CMD", "nc", "-z", "-w2", "localhost", "9200" ]
      interval: 5s
      timeout: 5s
      retries: 60
  cassandra:
    build: cassandra
    mem_limit: 2g
    ports:
      - "9042:9042"
      - "9160:9160"
    environment:
      - CASSANDRA_SEEDS=cassandra
      - CASSANDRA_LISTEN_ADDRESS=cassandra
      - MAX_HEAP_SIZE=1000M
      - HEAP_NEWSIZE=100M
#    volumes:
#      - ./data/cassandra:/var/lib/cassandra
    healthcheck:
      test: [ "CMD", "cqlsh", "-e", "describe keyspaces" ]
      interval: 5s
      timeout: 5s
      retries: 60
  twcloud:
    build: twcloud
    mem_limit: 3g
    ports:
      - "8111:8111"
      - "3579:3579"
    environment:
      - TWCLOUD_OPTS=
        -Xmx3000M
        -Desi.httpd.ssl.keystorePath=certs/twcloud.p12
        -Dakka.cluster.seed-nodes.0=akka://twcloud@twcloud:2552
        -Desi.persistence.datastax-java-driver.basic.contact-points.0=cassandra:9042
        -Desi.indexer.enabled=true
        -Desi.server.actor.query.component-enabled=true
        -Desi.auth.url=https://host.docker.internal:8443
        -Desi.zookeeper.url=zookeeper:2181
        -Desi.auth.https.file=certs/trust/webapp.crt
        -Desi.query.es.node.host=elasticsearch
    volumes:
      - ./data/twcloud/certs:/twcloud/certs
    healthcheck:
      test: [ "CMD", "nc", "-z", "-w2", "localhost", "3579" ]
      interval: 5s
      timeout: 5s
      retries: 60
    depends_on:
      cassandra:
        condition: service_healthy
      elasticsearch:
        condition: service_healthy
  messaging:
    build: messaging
    mem_limit: 2g
    ports:
      - "61616:61616"
      - "8161:8161"
    healthcheck:
      test: [ "CMD", "nc", "-z", "-w2", "localhost", "61616" ]
      interval: 5s
      timeout: 10s
      retries: 3
  webapp:
    build: webapp
#    mem_limit: 8200m
    ports:
      - "8443:8443"
      - "8080:8080"
    environment:
      - ZOOKEEPER_HOST=zookeeper
      - CASSANDRA_HOST=cassandra
      - TWC_HOST=twcloud
      - MESSAGING_EXTERNAL=true
      - MESSAGING_HOST=messaging
      - MESSAGING_PORT=61616
      - MESSAGING_SECURITY_ENABLED=true
      - MESSAGING_SECURITY_USERNAME=artemis
      - MESSAGING_SECURITY_PASSWORD=artemis
      - REDIRECT_WHITELIST=http
      - WEBAPP_PROPERTIES=
        -Dmessaging.server.security.enabled=true
        -Dmessaging.user.name=artemis
        -Dmessaging.user.password=artemis
    volumes:
      - ./data/webapp/certs:/webapp/certs
      - ./data/webapp/logs:/webapp/logs
    healthcheck:
      test: [ "CMD", "nc", "-z", "-w2", "localhost", "8443" ]
      interval: 5s
      timeout: 5s
      retries: 60
    depends_on:
      cassandra:
        condition: service_healthy
      twcloud:
        condition: service_healthy
      messaging:
        condition: service_started

````

### ENTRY: generateCerts.sh

- bytes: 608
- crc32: `25796f8b`
- decoded_as: `utf-8`

````text
#!/usr/bin/env bash

mkdir -p data/certs

generate() {
  local fqdn=$1

  echo Generate keypair with -dname cn=$fqdn -ext SAN=dns:$fqdn

keytool -genkeypair -keyalg RSA -sigalg SHA256withRSA -keysize 2048 -validity 3650 -keystore "${fqdn}.p12" \
 -storetype  pkcs12 -storepass nomagic -keypass nomagic -alias $fqdn -dname cn=$fqdn \
 -ext BasicConstraints:critical=ca:false -ext SAN=dns:$fqdn,dns:localhost,dns:host.docker.internal
keytool -export -keystore "${fqdn}.p12" -storepass nomagic -alias ${fqdn} -file "${fqdn}.crt"

}

pushd data/certs && \
generate twcloud && \
generate webapp && \
popd || exit

````

### ENTRY: README.md

- bytes: 3450
- crc32: `eb390036`
- decoded_as: `utf-8`

````markdown
# Example with docker-compose

* Works with release 2022x GA and Refresh 1
* Using cassandra 4.0.3

## Purpose

The purpose - to provide example of TeamworkCloud Suite containerization with docker.

Using docker compose as launch configuration for suite.

Two solutions provided:
1. Single cassandra and single teamworkcloud [here](#running-1-1-setup)
2. 3x cassandra cluster and 3x teamworkcloud cluster [here](#running-3-3-setup)

## Requirements

- Docker and Docker Compose
- Java JDK 8 or newer (for key generating certificates)
- Linux, WSL 2.0, or Cygwin for Windows (to execute scripts)
- Free RAM for 1-1 solution `28G+`:
  - zookeeper - `2G`
  - zoonavigator - `1G`
  - elasticsearch - `2G`
  - cassandra - `1G`
  - twcloud - `3G`
  - messaging - `2G`
  - webapp - `no limit set`
- Free RAM for 3-3 solution `56G+`:
  - zookeeper - `2G`
  - zoonavigator - `1G`
  - elasticsearch - `2G`
  - cassandra - `1G`
  - cassandra2 - `1G`
  - cassandra3 - `1G` 
  - twcloud - `3G`
  - twcloud2 - `3G`
  - twcloud3 - `3G`
  - messaging - `2G`
  - webapp - `no limit set`
- have license key in license server available.

## Steps

### Running 1-1 setup

1. Download twcloud no-install Linux64 zip file to example working directory and rename to `twcloudsuite.zip`
   * name of file is important here.
2. Run command `config.twc-compose.sh` to download Artemis package, unzip TWC files, and generate certificate.
3. Run command `docker compose build` to initial Docker Compose container configurations.
4. Run command `docker compose up -d` to build container images, if needed, and launch containers.

To access webapp: `https://host.docker.internal:8443/webapp`

Apply license key via web UI or REST API: `https://host.docker.internal:8111`

To connect from MagicDraw: `host.docker.internal:3579`

* Command to stop containers: `docker compose stop` (ephermeral storage still active)
* To stop and remove Docker containers: `docker compose down` (all ephermeral storage deleted)

### Running 3-3 setup

All steps as in 1-1 with one change to `docker compose` commands - need to add `-f docker compose.3-3.yaml`.

Eg. `docker compose -f docker-compose.3-3.yaml build`

## Persistence

Some containers have data directories mapped to host for persistence between restarts. This directory is `data/{service_name}`.

Container that use `data` directory for persisting new data:
- cassandra
- cassandra2
- cassandra3
- elasticsearch
- webapp (only logs)
- zookeeper

For clean retry you may want to clear all of those directory contents except for `webapp/certs` - do not delete this.

## Advanced usage

### Existing cassandra database

It is possible to copy existing database contents to `data/cassandra` and running all systems.
Not yet tested. Might need some more properties changes for cassandra to start.

### Use different Artemis version

To use a different version of ActiveMQ Artemis in messaging, do the following before executing `config.twc-compose.sh`. The configuratoin script will not download Artemis if the `apache-artemis` folder already exists.

1. Download `ActiveMQ Artemis` for linux - [download](https://activemq.apache.org/components/artemis/download/)
2. Extract to `messaging` directory and rename extracted folder to `apache-artemis`
   * expected directory is `apache-artemis`. eg. part of path `example/messaging/apache-artemis`

````

### ENTRY: config.twc-compose.sh

- bytes: 1243
- crc32: `bde0e906`
- decoded_as: `utf-8`

````text
#!/usr/bin/env bash

if ! [ -d messaging/apache-artemis ]; then
 echo "Downloading and preparing ActiveMQ Artemis"
 echo "..."
 cd messaging
 curl -O https://archive.apache.org/dist/activemq/activemq-artemis/2.26.0/apache-artemis-2.26.0-bin.zip
 unzip -q apache-artemis-2.26.0-bin.zip
 rm -f apache-artemis-2.26.0-bin.zip
 mv apache-artemis-2.26.0 apache-artemis
 cd ..
fi

echo "Unpacking and staging Teamwork Cloud files"
echo "..."
unzip -q twcloudsuite.zip
# extracted locally to 'CATIANoMagicServices'

if [ -d CATIANoMagicServices ]; then
	echo "Unpacked sucessfully"
	cp -r CATIANoMagicServices/TeamworkCloud twcloud
	cp -r CATIANoMagicServices/WebAppPlatform webapp
	mkdir -p data/twcloud

	echo "Generating self-signed certificates"
	echo "..."
	bash generateCerts.sh

	mkdir -p data/twcloud/certs/trust
	cp data/certs/twcloud.p12 data/twcloud/certs
	cp data/certs/*.crt data/twcloud/certs/trust
	cp -r data/twcloud data/twcloud2
	cp -r data/twcloud data/twcloud3

	mkdir -p data/webapp/certs/trust
	cp data/certs/webapp.p12 data/webapp/certs
	cp data/certs/*.crt data/webapp/certs/trust

	mkdir -p data/cassandra
	mkdir -p data/zookeeper

	echo "..."
	echo "Staging Complete"
else 
	echo "Staging failed. Cannot inflate archive."
fi

````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "189149971",
  "type": "attachment",
  "status": "current",
  "title": "TWC-Container-Example-Pkg.zip",
  "version": {
    "by": {
      "type": "known",
      "username": "jse21",
      "userKey": "2c9f81f87be2b373017e241b5e8b0001",
      "profilePicture": {
        "path": "/download/attachments/85767822/user-avatar",
        "width": 48,
        "height": 48,
        "isDefault": false
      },
      "displayName": "Jonė Š.",
      "_links": {
        "self": "https://docs.nomagic.com/rest/api/user?key=2c9f81f87be2b373017e241b5e8b0001"
      },
      "_expandable": {
        "status": ""
      }
    },
    "when": "2025-09-05T15:50:15.388+02:00",
    "message": "",
    "number": 3,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/189149971/version/3"
    },
    "_expandable": {
      "content": "/rest/api/content/189149971"
    }
  },
  "position": -1,
  "container": {
    "id": "189149970",
    "type": "page",
    "status": "current",
    "title": "Building Teamwork Cloud containers",
    "position": 0,
    "extensions": {
      "position": 0
    },
    "_links": {
      "webui": "/spaces/TWCloud2024xR2/pages/189149970/Building+Teamwork+Cloud+containers",
      "edit": "/pages/resumedraft.action?draftId=189149970",
      "tinyui": "/x/EjNGCw",
      "self": "https://docs.nomagic.com/rest/api/content/189149970"
    },
    "_expandable": {
      "container": "/rest/api/space/TWCloud2024xR2",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/189149970/child",
      "restrictions": "/rest/api/content/189149970/restriction/byOperation",
      "history": "/rest/api/content/189149970/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/189149970/descendant",
      "space": "/rest/api/space/TWCloud2024xR2",
      "relevantViewRestrictions": "/rest/api/content/189149970/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/zip"
  },
  "extensions": {
    "mediaType": "application/zip",
    "fileSize": 11306,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/189149970/TWC-Container-Example-Pkg.zip?version=3&modificationDate=1757080215388&api=v2",
    "webui": "/spaces/TWCloud2024xR2/pages/189149970/Building+Teamwork+Cloud+containers?preview=%2F189149970%2F189149971%2FTWC-Container-Example-Pkg.zip",
    "self": "https://docs.nomagic.com/rest/api/content/189149971"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/189149971/child",
    "restrictions": "/rest/api/content/189149971/restriction/byOperation",
    "history": "/rest/api/content/189149971/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/189149971/descendant",
    "space": "/rest/api/space/TWCloud2024xR2",
    "relevantViewRestrictions": "/rest/api/content/189149971/restriction/relevantViewRestrictions"
  }
}
````
