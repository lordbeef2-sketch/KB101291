# NOMAGIC ATTACHMENT: dockerfiles.zip

- attachment_id: `191924298`
- space_key: `MCS2024xR2`
- parent_page_id: `191924296`
- parent_page_title: Deployment example for Teamwork Cloud with services on Kubernetes
- media_type: `application/zip`
- reported_bytes: 9756
- download_url: https://docs.nomagic.com/download/attachments/191924296/dockerfiles.zip?version=1&modificationDate=1728049793970&api=v2
- payload_kind: `archive-expanded`
- downloaded_sha256: `a428fcd9ed03d7c7cf0b5771f335f1367000bbb49501d86d6415ec2db396a7c2`

## ARCHIVE CONTENTS

### ENTRY: dockerfiles/admin-console/Dockerfile

- bytes: 1005
- crc32: `9769a957`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.20-jre17-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY admin.war ${TOMCAT_DIR}/webapps/
COPY ROOT ${TOMCAT_DIR}/webapps/ROOT

RUN echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' > ${SET_ENV_FILE} && \
    chmod o+x ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y netcat curl && \
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist && \
    apt-get clean && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES} -DLOG4J_ENABLE_JNDI_LOOKUP=true -DLOG4J_CONFIGURATION_FILE=${CATALINA_HOME}/shared/conf/log4j2.properties"' >> ${SET_ENV_FILE}

USER tomcat

EXPOSE 8080

CMD ["catalina.sh", "run"]

````

### ENTRY: dockerfiles/authentication/Dockerfile

- bytes: 1015
- crc32: `87839527`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.20-jre17-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY authentication.war ${TOMCAT_DIR}/webapps/
COPY ROOT ${TOMCAT_DIR}/webapps/ROOT

RUN echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' > ${SET_ENV_FILE} && \
    chmod o+x ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y netcat curl && \
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist && \
    apt-get clean && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES} -DLOG4J_ENABLE_JNDI_LOOKUP=true -DLOG4J_CONFIGURATION_FILE=${CATALINA_HOME}/shared/conf/log4j2.properties"' >> ${SET_ENV_FILE}

USER tomcat

EXPOSE 8080

CMD ["catalina.sh", "run"]


````

### ENTRY: dockerfiles/collaborator/Dockerfile

- bytes: 1053
- crc32: `752fc528`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.20-jre17-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY collaborator.war ${TOMCAT_DIR}/webapps/
COPY data ${TOMCAT_DIR}/shared/conf/data
COPY ROOT ${TOMCAT_DIR}/webapps/ROOT

RUN echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' > ${SET_ENV_FILE} && \
    chmod o+x ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y netcat curl && \
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist && \
    apt-get clean && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES} -DLOG4J_ENABLE_JNDI_LOOKUP=true -DLOG4J_CONFIGURATION_FILE=${CATALINA_HOME}/shared/conf/log4j2.properties"' >> ${SET_ENV_FILE}

USER tomcat

EXPOSE 8080

CMD ["catalina.sh", "run"]

````

### ENTRY: dockerfiles/document-exporter/Dockerfile

- bytes: 1737
- crc32: `c74e37fd`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.20-jre17-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}
ARG PRINCE_V=15.3
ARG PRINCE_F=prince-${PRINCE_V}-linux-generic-x86_64.tar.gz
ARG LINK=https://www.princexml.com/download/prince-${PRINCE_V}-linux-generic-x86_64.tar.gz

COPY document-exporter.war ${TOMCAT_DIR}/webapps/
COPY data ${TOMCAT_DIR}/shared/conf/data
COPY ROOT ${TOMCAT_DIR}/webapps/ROOT

SHELL ["/bin/bash", "-c"]
RUN curl -OL --output-dir /tmp ${LINK} && \
    tar -xzf /tmp/${PRINCE_F} -C /tmp && \
    mv /tmp/${PRINCE_F::-7} /usr/local/prince && \
    cd /usr/local/prince && ln -s lib/prince/bin/ ./ && cd - && \
    rm -rf webapps.dist && \
    rm -f /tmp/${PRINCE_F}

RUN echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' > ${SET_ENV_FILE} && \
    chmod o+x ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y netcat curl && \
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \   
    apt install dialog apt-utils -y && \    
    echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | debconf-set-selections && \
    apt-get install ttf-mscorefonts-installer -y && \
    rm -rf webapps.dist && \
    apt-get clean && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES} -DLOG4J_ENABLE_JNDI_LOOKUP=true -DLOG4J_CONFIGURATION_FILE=${CATALINA_HOME}/shared/conf/log4j2.properties"' >> ${SET_ENV_FILE}
    
USER tomcat

EXPOSE 8080

CMD ["catalina.sh", "run"]

````

### ENTRY: dockerfiles/oslc/Dockerfile

- bytes: 1004
- crc32: `31e091d3`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.20-jre17-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY oslc.war ${TOMCAT_DIR}/webapps/
COPY ROOT ${TOMCAT_DIR}/webapps/ROOT

RUN echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' > ${SET_ENV_FILE} && \
    chmod o+x ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y netcat curl && \
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist && \
    apt-get clean && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES} -DLOG4J_ENABLE_JNDI_LOOKUP=true -DLOG4J_CONFIGURATION_FILE=${CATALINA_HOME}/shared/conf/log4j2.properties"' >> ${SET_ENV_FILE}

USER tomcat

EXPOSE 8080

CMD ["catalina.sh", "run"]

````

### ENTRY: dockerfiles/reports/Dockerfile

- bytes: 1008
- crc32: `a679e53b`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.20-jre17-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY reports.war ${TOMCAT_DIR}/webapps/
COPY ROOT ${TOMCAT_DIR}/webapps/ROOT

RUN echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' > ${SET_ENV_FILE} && \
    chmod o+x ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y netcat curl && \
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist  && \
    apt-get clean && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES} -DLOG4J_ENABLE_JNDI_LOOKUP=true -DLOG4J_CONFIGURATION_FILE=${CATALINA_HOME}/shared/conf/log4j2.properties"' >> ${SET_ENV_FILE}

USER tomcat

EXPOSE 8080

CMD ["catalina.sh", "run"]

````

### ENTRY: dockerfiles/resource-usage-map/Dockerfile

- bytes: 1394
- crc32: `d3881e5d`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.20-jre17-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY resource-usage-map.war ${TOMCAT_DIR}/webapps/
COPY ROOT ${TOMCAT_DIR}/webapps/ROOT

RUN echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES} -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=2468 -Dcom.sun.management.jmxremote.rmi.port=2468 -Dcom.sun.management.jmxremote.local.only=false -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false"' > ${SET_ENV_FILE} && \
    chmod o+x ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y netcat curl && \
    groupadd --gid ${USER_GID} tomcat && \
    apt-get install -y curl apt-utils netcat mc lsof net-tools vim telnet tcpdump dnsutils iperf iputils-ping && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist && \
    apt-get clean && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES} -DLOG4J_ENABLE_JNDI_LOOKUP=true -DLOG4J_CONFIGURATION_FILE=${CATALINA_HOME}/shared/conf/log4j2.properties"' >> ${SET_ENV_FILE}

USER tomcat

EXPOSE 8080 2468

CMD ["catalina.sh", "run"]

````

### ENTRY: dockerfiles/resources/Dockerfile

- bytes: 986
- crc32: `a93b3ee6`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.20-jre17-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY resources.war ${TOMCAT_DIR}/webapps/
COPY ROOT ${TOMCAT_DIR}/webapps/ROOT

RUN echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' > ${SET_ENV_FILE} && \
    chmod o+x ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y netcat curl && \
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES} -DLOG4J_ENABLE_JNDI_LOOKUP=true -DLOG4J_CONFIGURATION_FILE=${CATALINA_HOME}/shared/conf/log4j2.properties"' >> ${SET_ENV_FILE}

USER tomcat

EXPOSE 8080

CMD ["catalina.sh", "run"]

````

### ENTRY: dockerfiles/simulation/Dockerfile

- bytes: 1010
- crc32: `3e991631`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.20-jre17-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY simulation.war ${TOMCAT_DIR}/webapps/
COPY ROOT ${TOMCAT_DIR}/webapps/ROOT

RUN echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' > ${SET_ENV_FILE} && \
    chmod o+x ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y netcat curl && \
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist && \
    apt-get clean && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES} -DLOG4J_ENABLE_JNDI_LOOKUP=true -DLOG4J_CONFIGURATION_FILE=${CATALINA_HOME}/shared/conf/log4j2.properties"' >> ${SET_ENV_FILE}

USER tomcat

EXPOSE 8080

CMD ["catalina.sh", "run"]

````

### ENTRY: dockerfiles/twc/Dockerfile

- bytes: 703
- crc32: `e965aeea`
- decoded_as: `utf-8`

````text
FROM eclipse-temurin:17.0.11_9-jre-jammy

ARG twcdir=TeamworkCloud
ARG USER_UID=5001
ARG USER_GID=${USER_UID}

COPY $twcdir /twcloud
WORKDIR /twcloud
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install netcat && \
    rm -rf /var/lib/apt/lists/* && \
    groupadd --gid ${USER_GID} twcloud && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d /twcloud -c "TeamworkCloud user" twcloud && \
    cd /twcloud && \
    curl -OL https://downloads.datastax.com/enterprise/cqlsh-5.1.tar.gz && \
    tar -xzf cqlsh-5.1.tar.gz && \
    rm -f cqlsh-5.1.tar.gz && \
    chown -R twcloud:twcloud ../twcloud

USER twcloud
EXPOSE 8111 3579

CMD ["/bin/bash", "twcloud"]
````

### ENTRY: dockerfiles/webapp/Dockerfile

- bytes: 1006
- crc32: `f0856836`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.20-jre17-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY webapp.war ${TOMCAT_DIR}/webapps/
COPY ROOT ${TOMCAT_DIR}/webapps/ROOT

RUN echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' > ${SET_ENV_FILE} && \
    chmod o+x ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y netcat curl && \
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist && \
    apt-get clean && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES} -DLOG4J_ENABLE_JNDI_LOOKUP=true -DLOG4J_CONFIGURATION_FILE=${CATALINA_HOME}/shared/conf/log4j2.properties"' >> ${SET_ENV_FILE}

USER tomcat

EXPOSE 8080

CMD ["catalina.sh", "run"]

````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "191924298",
  "type": "attachment",
  "status": "current",
  "title": "dockerfiles.zip",
  "version": {
    "by": {
      "type": "known",
      "username": "rre6",
      "userKey": "2c90b2828dee4d35018defef1f8f0005",
      "profilePicture": {
        "path": "/images/icons/profilepics/default.svg",
        "width": 48,
        "height": 48,
        "isDefault": true
      },
      "displayName": "Rytis RŪKŠTELĖ",
      "_links": {
        "self": "https://docs.nomagic.com/rest/api/user?key=2c90b2828dee4d35018defef1f8f0005"
      },
      "_expandable": {
        "status": ""
      }
    },
    "when": "2024-10-04T15:49:53.970+02:00",
    "message": "",
    "number": 1,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/191924298/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/191924298"
    }
  },
  "position": -1,
  "container": {
    "id": "191924296",
    "type": "page",
    "status": "current",
    "title": "Deployment example for Teamwork Cloud with services on Kubernetes",
    "position": 5,
    "extensions": {
      "position": 5
    },
    "_links": {
      "webui": "/spaces/MCS2024xR2/pages/191924296/Deployment+example+for+Teamwork+Cloud+with+services+on+Kubernetes",
      "edit": "/pages/resumedraft.action?draftId=191924296",
      "tinyui": "/x/SIhwCw",
      "self": "https://docs.nomagic.com/rest/api/content/191924296"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS2024xR2",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/191924296/child",
      "restrictions": "/rest/api/content/191924296/restriction/byOperation",
      "history": "/rest/api/content/191924296/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/191924296/descendant",
      "space": "/rest/api/space/MCS2024xR2",
      "relevantViewRestrictions": "/rest/api/content/191924296/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/zip"
  },
  "extensions": {
    "mediaType": "application/zip",
    "fileSize": 9756,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/191924296/dockerfiles.zip?version=1&modificationDate=1728049793970&api=v2",
    "webui": "/spaces/MCS2024xR2/pages/191924296/Deployment+example+for+Teamwork+Cloud+with+services+on+Kubernetes?preview=%2F191924296%2F191924298%2Fdockerfiles.zip",
    "self": "https://docs.nomagic.com/rest/api/content/191924298"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/191924298/child",
    "restrictions": "/rest/api/content/191924298/restriction/byOperation",
    "history": "/rest/api/content/191924298/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/191924298/descendant",
    "space": "/rest/api/space/MCS2024xR2",
    "relevantViewRestrictions": "/rest/api/content/191924298/restriction/relevantViewRestrictions"
  }
}
````
