# NOMAGIC ATTACHMENT: TWC container examples 2026x.zip

- attachment_id: `306283081`
- space_key: `MCS`
- parent_page_id: `306283079`
- parent_page_title: Copy of incorrect documentation of Building Teamwork Cloud container
- media_type: `application/zip`
- reported_bytes: 6703
- download_url: https://docs.nomagic.com/download/attachments/306283079/TWC%20container%20examples%202026x.zip?version=1&modificationDate=1778489860587&api=v2
- payload_kind: `archive-expanded`
- downloaded_sha256: `a22b852bb44ddfe331d5b5e8f2bc9e9beb515f8e544fafb0d01ef56f4e740be8`

## ARCHIVE CONTENTS

### ENTRY: cassandra/Dockerfile

- bytes: 964
- crc32: `a71bc663`
- decoded_as: `utf-8`

````text
FROM cassandra:5.0.4

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

### ENTRY: cleanup.sh

- bytes: 85
- crc32: `dee67ae7`
- decoded_as: `utf-8`

````text
#!/usr/bin/env bash
rm -r CATIANoMagicServices
rm -r data
rm -r twcloud/TeamworkCloud
````

### ENTRY: config.twc-compose.sh

- bytes: 512
- crc32: `517f2418`
- decoded_as: `utf-8`

````text
#!/usr/bin/env bash

echo "Unpacking and staging Teamwork Cloud files"
echo "..."

unzip -q twcloudsuite.zip
mv TeamworkCloudSuite twcloud/TeamworkCloudSuite

echo "Generating self-signed certificates"
echo "..."

bash generateCerts.sh

mkdir -p data/twcloud/certs/trust
cp data/certs/twcloud.p12 data/twcloud/certs
cp data/certs/*.crt data/twcloud/certs/trust
cp -r data/twcloud data/twcloud2
cp -r data/twcloud data/twcloud3

mkdir -p data/cassandra
mkdir -p data/zookeeper

echo "..."
echo "Staging Complete"

````

### ENTRY: docker-compose.3-3.yaml

- bytes: 5808
- crc32: `8a40f84f`
- decoded_as: `utf-8`

````yaml
version: '2.4'
services:
  zookeeper:
    image: zookeeper:3.9.4
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
    image: elasticsearch:8.19.0
    mem_limit: 2g
    ports:
      - "9200:9200"
    environment:
      - discovery.type=single-node
      - cluster.routing.allocation.disk.threshold_enabled=false
      - xpack.security.enabled=false
      - xpack.security.http.ssl.enabled=false
      - xpack.security.transport.ssl.enabled=false
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
    mem_limit: 2g
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
    mem_limit: 2g
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

````

### ENTRY: docker-compose.yml

- bytes: 2705
- crc32: `a8a7cce1`
- decoded_as: `utf-8`

````yaml
version: '2.4'
services:
  zookeeper:
    image: zookeeper:3.9.4
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
    image: elasticsearch:8.19.0
    mem_limit: 2g
    ports:
      - "9200:9200"
    environment:
      - discovery.type=single-node
      - cluster.routing.allocation.disk.threshold_enabled=false
      - xpack.security.enabled=false
      - xpack.security.http.ssl.enabled=false
      - xpack.security.transport.ssl.enabled=false
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

````

### ENTRY: generateCerts.sh

- bytes: 587
- crc32: `92b6871c`
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
popd || exit

````

### ENTRY: README.md

- bytes: 3230
- crc32: `933c8802`
- decoded_as: `utf-8`

````markdown
# Example with docker-compose

* Works with release 2026x
* Using cassandra 5.0.4

## Purpose

The purpose - to provide example of TeamworkCloud Suite containerization with docker.

Using docker compose as launch configuration for suite.

Two solutions provided:
1. Single cassandra and single teamworkcloud [here](#running-1-1-setup)
2. 3x cassandra cluster and 3x teamworkcloud cluster [here](#running-3-3-setup)

## Requirements

- Docker and Docker Compose
- Java JDK 21 or newer (for key generating certificates)
- Linux, WSL 2.0, or Cygwin for Windows (to execute scripts)
- Free RAM for 1-1 solution `28G+`:
  - zookeeper - `2G`
  - zoonavigator - `1G`
  - elasticsearch - `2G`
  - cassandra - `1G`
  - twcloud - `3G`
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
- have license key in license server available.

## Steps

### Running 1-1 setup

1. Download twcloud no-install Linux64 zip file to example working directory and rename to `twcloudsuite.zip`
   * name of file is important here.
2. Run command `config.twc-compose.sh` to download Artemis package, unzip TWC files, and generate certificate.
3. Run command `docker compose build` to initial Docker Compose container configurations.
4. Run command `docker compose up -d` to build container images, if needed, and launch containers.

To access webapp: `https://host.docker.internal:8443/webapp`

Apply license key via REST API: `https://host.docker.internal:8111`

To connect from MagicDraw: `host.docker.internal:3579`

* Command to stop containers: `docker compose stop` (ephermeral storage still active)
* To stop and remove Docker containers: `docker compose down` (all ephermeral storage deleted)

### Running 3-3 setup

1. Download twcloud no-install Linux64 zip file to example working directory and rename to `twcloudsuite.zip`
   * name of file is important here.
2. Run command `config.twc-compose.sh` to download Artemis package, unzip TWC files, and generate certificate.
3. Run command `docker compose -f docker-compose.3-3.yaml build` to initial Docker Compose container configurations.
4. Run command `docker compose -f docker-compose.3-3.yaml up -d` to build container images, if needed, and launch containers.


Eg. `docker compose -f docker-compose.3-3.yaml build`


Note: You have to have valid apropriate license in order to start in cluster mode.

## Persistence

Some containers have data directories mapped to host for persistence between restarts. This directory is `data/{service_name}`.

Container that use `data` directory for persisting new data:
- cassandra
- cassandra2
- cassandra3
- elasticsearch
- zookeeper

For clean retry you may want to clear all of those directory contents except for `webapp/certs` - do not delete this.

## Advanced usage

### Existing cassandra database

It is possible to copy existing database contents to `data/cassandra` and running all systems.
Not yet tested. Might need some more properties changes for cassandra to start.

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

- bytes: 344
- crc32: `bc0d9028`
- decoded_as: `utf-8`

````text
FROM eclipse-temurin:21.0.6_7-jdk
RUN apt-get -y update && apt-get -y upgrade && apt-get -y install apt-utils sudo wget netcat-traditional && rm -rf /var/lib/apt/lists/*
COPY docker.scripts /scripts
RUN sh /scripts/init.sh
COPY TeamworkCloudSuite /twcloud
WORKDIR /twcloud
EXPOSE 8111 3579
VOLUME /certs
CMD ["/scripts/entrypoint.sh"]

````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "306283081",
  "type": "attachment",
  "status": "current",
  "title": "TWC container examples 2026x.zip",
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
    "when": "2026-05-11T10:57:40.587+02:00",
    "message": "",
    "number": 1,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/306283081/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/306283081"
    }
  },
  "position": -1,
  "container": {
    "id": "306283079",
    "type": "page",
    "status": "current",
    "title": "Copy of incorrect documentation of Building Teamwork Cloud container",
    "position": 1,
    "extensions": {
      "position": 1
    },
    "_links": {
      "webui": "/spaces/MCS/pages/306283079/Copy+of+incorrect+documentation+of+Building+Teamwork+Cloud+container",
      "edit": "/pages/resumedraft.action?draftId=306283079",
      "tinyui": "/x/R4JBEg",
      "self": "https://docs.nomagic.com/rest/api/content/306283079"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/306283079/child",
      "restrictions": "/rest/api/content/306283079/restriction/byOperation",
      "history": "/rest/api/content/306283079/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/306283079/descendant",
      "space": "/rest/api/space/MCS",
      "relevantViewRestrictions": "/rest/api/content/306283079/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/zip"
  },
  "extensions": {
    "mediaType": "application/zip",
    "fileSize": 6703,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/306283079/TWC%20container%20examples%202026x.zip?version=1&modificationDate=1778489860587&api=v2",
    "webui": "/spaces/MCS/pages/306283079/Copy+of+incorrect+documentation+of+Building+Teamwork+Cloud+container?preview=%2F306283079%2F306283081%2FTWC+container+examples+2026x.zip",
    "self": "https://docs.nomagic.com/rest/api/content/306283081"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/306283081/child",
    "restrictions": "/rest/api/content/306283081/restriction/byOperation",
    "history": "/rest/api/content/306283081/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/306283081/descendant",
    "space": "/rest/api/space/MCS",
    "relevantViewRestrictions": "/rest/api/content/306283081/restriction/relevantViewRestrictions"
  }
}
````
