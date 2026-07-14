# NOMAGIC ATTACHMENT: twcloud-on-docker-master.zip

- attachment_id: `189149973`
- space_key: `TWCloud2024xR2`
- parent_page_id: `189149970`
- parent_page_title: Building Teamwork Cloud containers
- media_type: `application/zip`
- reported_bytes: 3081
- download_url: https://docs.nomagic.com/download/attachments/189149970/twcloud-on-docker-master.zip?version=1&modificationDate=1728044292744&api=v2
- payload_kind: `archive-expanded`
- downloaded_sha256: `1abf3183b012f6f3a7293f6090fca04d683e0ccb16bb7dadb42e96732bfbbccd`

## ARCHIVE CONTENTS

### ENTRY: twcloud-on-docker-master/CLUSTER.md

- bytes: 741
- crc32: `60c316dd`
- decoded_as: `utf-8`

````markdown
# Cluster

## Create docker image

Docker image creation does not differ from single node [here](README.md#create-docker-image)

## Cluster configuration

On **each** host:
 * expose port 2552 by adding to `compose/docker-compose.yml#twcloud.ports` (same as 8111 port)
 * configure `compose/configuration/application.conf` key `akka.cluster.seed-nodes` as in
[TWCloud Cluster Setup](https://docs.nomagic.com/display/TWCloud2021xR1/TWCloud+Cluster+Setup) documentation.
 * modify CASSANDRA_SEEDS in `compose/docker-compose.yml` as in
   [TWCloud Cluster Setup](https://docs.nomagic.com/display/TWCloud2021xR1/TWCloud+Cluster+Setup) documentation.
 * start docker compose sample as in [example](README.md#example-with-docker-compose) step 6



````

### ENTRY: twcloud-on-docker-master/README.md

- bytes: 2024
- crc32: `fe7946a4`
- decoded_as: `utf-8`

````markdown
# TWCloud dockerization instructions

## Intro

This readme contains instruction how to build docker image from teamworkcloudsuite archive.

## Workspace

- image/ - folder that contains Dockerfile
- compose/ - folder that contains docker compose runtime instructions

## Create docker image

1. Working directory `image/`.
2. Review `Dockerfile`.
3. Extract teamworkcloudsuite archive contens to `image/` so that now you have `image/TeamworkCloudSuite/` folder.
4. Modify your configurations as needed.
   * `TeamworkCloudSuite/jvm.options`
   * `TeamworkCloudSuite/configuration/application.conf` 
   * `TeamworkCloudSuite/configuration/logback.xml`
5. run command `docker build -t twcloud .` You can name your image differently here.

## Example with docker compose

_Note: this will require free 12Gb of ram._

1. Working directory `compose/`.
2. Copy from `image/TeamworkCloudSuite/configuration` to `compose/configuration`
3. Modify configurations as needed.
   * `configuration/application.conf`
   * `configuration/logback.xml`
4. Mandatory modification of `configuration/application.conf` for this sample:
   * change key value `esi.persistence.datastax-java-driver.basic.contact-points` from `127.0.0.1:9042` to `cassandra:9042` 
5. (Optional) you can modify memory limits for cassandra and twcloud in `docker-compose.yml`
6. run command `docker compose up -d`

Helpful commands:
* `docker compose logs -f twcloud` - show output of twcloud docker container.
* `docker compose down` - stop all compose containers.
* `docker compose down -v` - stop and remove all containers.

## Extras

### Cassandra on host machine

Docker provides special hostname for the host machine named `host.docker.internal`.

How to use it:

* Modify `configuration/application.conf` key `esi.persistence.datastax-java-driver.basic.contact-points` as `host.docker.
  internal:9042`.
* Remove or comment all section of `cassandra` under `services` in `docker-compose.yml`.
* Remove or comment all section of `depends_on` under `twcloud`.


````

### ENTRY: twcloud-on-docker-master/compose/docker-compose.yml

- bytes: 925
- crc32: `e4c0412f`
- decoded_as: `utf-8`

````yaml
version: '2.4'
services:
  cassandra:
    image: cassandra:4.0.3
    mem_limit: 4g
    environment:
      - CASSANDRA_START_RPC=false
      - CASSANDRA_SEEDS=cassandra
      - CASSANDRA_LISTEN_ADDRESS=cassandra
      - MAX_HEAP_SIZE=4000M
      - HEAP_NEWSIZE=800M
    networks:
      - twcnetwork
    ports:
      - "9042:9042"
    healthcheck:
      test: [ "CMD", "cqlsh", "-e", "describe keyspaces" ]
      interval: 5s
      timeout: 5s
      retries: 60
  twcloud:
    build:
      context: ../image
    mem_limit: 8g
    networks:
      - twcnetwork
    ports:
      - "8111:8111"
      - "3579:3579"
    volumes:
      - .\configuration\application.conf:/opt/twc/TeamworkCloudSuite/configuration/application.conf
      - .\configuration\logback.xml:/opt/twc/TeamworkCloudSuite/configuration/logback.xml
    depends_on:
      cassandra:
        condition: service_healthy
networks:
  twcnetwork:
    name: mytwcnetwork
````

### ENTRY: twcloud-on-docker-master/image/Dockerfile

- bytes: 406
- crc32: `1ab9bb58`
- decoded_as: `utf-8`

````text
FROM openjdk:11.0.13
# copy directory contents to docker internal directory
COPY TeamworkCloudSuite /opt/twc/TeamworkCloudSuite
# set working directory
WORKDIR /opt/twc/TeamworkCloudSuite
# run certificate generation
RUN chmod +x scripts/linux/genkey && scripts/linux/genkey
# declare ports that can be used
EXPOSE 3579
EXPOSE 8111
EXPOSE 2552
# declare entrypoint starting this image
ENTRYPOINT ./twcloud

````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "189149973",
  "type": "attachment",
  "status": "current",
  "title": "twcloud-on-docker-master.zip",
  "version": {
    "by": {
      "type": "known",
      "username": "ingabe",
      "userKey": "ff80808151f3008c0152c05ba1a40003",
      "profilePicture": {
        "path": "/download/attachments/7415957/user-avatar",
        "width": 48,
        "height": 48,
        "isDefault": false
      },
      "displayName": "Inga A.",
      "_links": {
        "self": "https://docs.nomagic.com/rest/api/user?key=ff80808151f3008c0152c05ba1a40003"
      },
      "_expandable": {
        "status": ""
      }
    },
    "when": "2024-10-04T14:18:12.744+02:00",
    "message": "",
    "number": 1,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/189149973/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/189149973"
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
    "fileSize": 3081,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/189149970/twcloud-on-docker-master.zip?version=1&modificationDate=1728044292744&api=v2",
    "webui": "/spaces/TWCloud2024xR2/pages/189149970/Building+Teamwork+Cloud+containers?preview=%2F189149970%2F189149973%2Ftwcloud-on-docker-master.zip",
    "self": "https://docs.nomagic.com/rest/api/content/189149973"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/189149973/child",
    "restrictions": "/rest/api/content/189149973/restriction/byOperation",
    "history": "/rest/api/content/189149973/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/189149973/descendant",
    "space": "/rest/api/space/TWCloud2024xR2",
    "relevantViewRestrictions": "/rest/api/content/189149973/restriction/relevantViewRestrictions"
  }
}
````
