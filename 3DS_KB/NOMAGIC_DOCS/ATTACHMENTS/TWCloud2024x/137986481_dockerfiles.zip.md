# NOMAGIC ATTACHMENT: dockerfiles.zip

- attachment_id: `137986481`
- space_key: `TWCloud2024x`
- parent_page_id: `137986474`
- parent_page_title: Deployment example for Web Application Platform on Kubernetes
- media_type: `application/zip`
- reported_bytes: 7382
- download_url: https://docs.nomagic.com/download/attachments/137986474/dockerfiles.zip?version=1&modificationDate=1695376244365&api=v2
- payload_kind: `archive-expanded`
- downloaded_sha256: `afd95bb790a65fd733b1c2821ee764dc23f8c4a43128c47b70f9347b1617fdf7`

## ARCHIVE CONTENTS

### ENTRY: dockerfiles/Dockerfile_admin-console

- bytes: 1052
- crc32: `8e6467ff`
- decoded_as: `utf-8`

````text
FROM tomcat:9.0.73-jre17-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY admin.war ${TOMCAT_DIR}/webapps/
COPY logback.xml ${TOMCAT_DIR}/shared/conf/
COPY webappplatform.properties ${TOMCAT_DIR}/shared/conf/
COPY server.xml ${TOMCAT_DIR}/conf/
COPY keystore.p12 ${TOMCAT_DIR}/shared/conf/

RUN sed -i "s|shared\.loader=*$|shared\.loader=\"\${catalina.base}/shared/conf\"|" ${TOMCAT_DIR}/conf/catalina.properties && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' >> ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    chmod o+x ${SET_ENV_FILE} && \	
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \    
    rm -rf webapps.dist && \
    apt-get clean 

USER tomcat

EXPOSE 8443

CMD ["catalina.sh", "run"]

````

### ENTRY: dockerfiles/Dockerfile_auth-server

- bytes: 1398
- crc32: `feed7008`
- decoded_as: `utf-8`

````text
FROM tomcat:9.0.73-jre17-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY logback.xml ${TOMCAT_DIR}/shared/conf/
COPY webappplatform.properties ${TOMCAT_DIR}/shared/conf/
COPY authserver.properties ${TOMCAT_DIR}/shared/conf/
COPY keystore.p12 ${TOMCAT_DIR}/shared/conf/
COPY teamworkcloud.crt ${TOMCAT_DIR}/shared/conf/
COPY authentication.war ${TOMCAT_DIR}/webapps/
COPY server.xml ${TOMCAT_DIR}/conf/

RUN sed -i "s|shared\.loader=*$|shared\.loader=\"\${catalina.base}/shared/conf\"|" ${TOMCAT_DIR}/conf/catalina.properties && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' >> ${SET_ENV_FILE} && \
    echo 'export JAVA_OPTS="$JAVA_OPTS -Dspring.config.additional-location=$CATALINA_HOME/shared/conf/authserver.properties,$CATALINA_HOME/shared/conf/webappplatform.properties"' >> ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install net-tools && \
    chmod o+x ${SET_ENV_FILE} && \
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist && \
    apt-get clean

USER tomcat

EXPOSE 8443

CMD ["catalina.sh", "run"]


````

### ENTRY: dockerfiles/Dockerfile_collaborator

- bytes: 1054
- crc32: `d5ca732e`
- decoded_as: `utf-8`

````text
FROM tomcat:9.0.73-jre17-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY collaborator.war ${TOMCAT_DIR}/webapps/
COPY logback.xml ${TOMCAT_DIR}/shared/conf/
COPY webappplatform.properties ${TOMCAT_DIR}/shared/conf/
COPY server.xml ${TOMCAT_DIR}/conf/
COPY keystore.p12 ${TOMCAT_DIR}/shared/conf/

RUN sed -i "s|shared\.loader=*$|shared\.loader=\"\${catalina.base}/shared/conf\"|" ${TOMCAT_DIR}/conf/catalina.properties && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' >> ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    chmod o+x ${SET_ENV_FILE} && \	
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist && \
    apt-get clean

USER tomcat

EXPOSE 8443

CMD ["catalina.sh", "run"]

````

### ENTRY: dockerfiles/Dockerfile_doc-export

- bytes: 1277
- crc32: `094d3fe6`
- decoded_as: `utf-8`

````text
FROM tomcat:9.0.73-jre17-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY document-exporter.war ${TOMCAT_DIR}/webapps/
COPY logback.xml ${TOMCAT_DIR}/shared/conf/
COPY webappplatform.properties ${TOMCAT_DIR}/shared/conf/
COPY server.xml ${TOMCAT_DIR}/conf/
COPY keystore.p12 ${TOMCAT_DIR}/shared/conf/

RUN sed -i "s|shared\.loader=*$|shared\.loader=\"\${catalina.base}/shared/conf\"|" ${TOMCAT_DIR}/conf/catalina.properties && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' >> ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    chmod o+x ${SET_ENV_FILE} && \
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \   
    apt install dialog apt-utils -y && \    
    echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | debconf-set-selections && \
    apt-get install ttf-mscorefonts-installer -y && \
    rm -rf webapps.dist && \
    apt-get clean

USER tomcat

EXPOSE 8443

CMD ["catalina.sh", "run"]

````

### ENTRY: dockerfiles/Dockerfile_oslc

- bytes: 1047
- crc32: `de06e3fe`
- decoded_as: `utf-8`

````text
FROM tomcat:9.0.73-jre17-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY oslc.war ${TOMCAT_DIR}/webapps/
COPY logback.xml ${TOMCAT_DIR}/shared/conf/
COPY webappplatform.properties ${TOMCAT_DIR}/shared/conf/
COPY server.xml ${TOMCAT_DIR}/conf/
COPY keystore.p12 ${TOMCAT_DIR}/shared/conf/

RUN sed -i "s|shared\.loader=*$|shared\.loader=\"\${catalina.base}/shared/conf\"|" ${TOMCAT_DIR}/conf/catalina.properties && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' >> ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    chmod o+x ${SET_ENV_FILE} && \	
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist && \
    apt-get clean 

USER tomcat

EXPOSE 8443

CMD ["catalina.sh", "run"]

````

### ENTRY: dockerfiles/Dockerfile_reports

- bytes: 1051
- crc32: `1881806b`
- decoded_as: `utf-8`

````text
FROM tomcat:9.0.73-jre17-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY reports.war ${TOMCAT_DIR}/webapps/
COPY logback.xml ${TOMCAT_DIR}/shared/conf/
COPY webappplatform.properties ${TOMCAT_DIR}/shared/conf/
COPY server.xml ${TOMCAT_DIR}/conf/
COPY keystore.p12 ${TOMCAT_DIR}/shared/conf/

RUN sed -i "s|shared\.loader=*$|shared\.loader=\"\${catalina.base}/shared/conf\"|" ${TOMCAT_DIR}/conf/catalina.properties && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' >> ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    chmod o+x ${SET_ENV_FILE} && \	
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist  && \
    apt-get clean 

USER tomcat

EXPOSE 8443

CMD ["catalina.sh", "run"]

````

### ENTRY: dockerfiles/Dockerfile_resources

- bytes: 1028
- crc32: `63064c5c`
- decoded_as: `utf-8`

````text
FROM tomcat:9.0.73-jre17-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY resources.war ${TOMCAT_DIR}/webapps/
COPY logback.xml ${TOMCAT_DIR}/shared/conf/
COPY webappplatform.properties ${TOMCAT_DIR}/shared/conf/
COPY server.xml ${TOMCAT_DIR}/conf/
COPY keystore.p12 ${TOMCAT_DIR}/shared/conf/

RUN sed -i "s|shared\.loader=*$|shared\.loader=\"\${catalina.base}/shared/conf\"|" ${TOMCAT_DIR}/conf/catalina.properties && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' >> ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    chmod o+x ${SET_ENV_FILE} && \	
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist

USER tomcat

EXPOSE 8443

CMD ["catalina.sh", "run"]

````

### ENTRY: dockerfiles/Dockerfile_resource-usage-map

- bytes: 1061
- crc32: `a850fcec`
- decoded_as: `utf-8`

````text
FROM tomcat:9.0.73-jre17-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY resource-usage-map.war ${TOMCAT_DIR}/webapps/
COPY logback.xml ${TOMCAT_DIR}/shared/conf/
COPY webappplatform.properties ${TOMCAT_DIR}/shared/conf/
COPY server.xml ${TOMCAT_DIR}/conf/
COPY keystore.p12 ${TOMCAT_DIR}/shared/conf/

RUN sed -i "s|shared\.loader=*$|shared\.loader=\"\${catalina.base}/shared/conf\"|" ${TOMCAT_DIR}/conf/catalina.properties && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' >> ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    chmod o+x ${SET_ENV_FILE} && \	
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist && \
    apt-get clean 

USER tomcat

EXPOSE 8443

CMD ["catalina.sh", "run"]

````

### ENTRY: dockerfiles/Dockerfile_simulation

- bytes: 1053
- crc32: `f3d6aa6e`
- decoded_as: `utf-8`

````text
FROM tomcat:9.0.73-jre17-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY simulation.war ${TOMCAT_DIR}/webapps/
COPY logback.xml ${TOMCAT_DIR}/shared/conf/
COPY webappplatform.properties ${TOMCAT_DIR}/shared/conf/
COPY server.xml ${TOMCAT_DIR}/conf/
COPY keystore.p12 ${TOMCAT_DIR}/shared/conf/

RUN sed -i "s|shared\.loader=*$|shared\.loader=\"\${catalina.base}/shared/conf\"|" ${TOMCAT_DIR}/conf/catalina.properties && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' >> ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    chmod o+x ${SET_ENV_FILE} && \	
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist && \
    apt-get clean 

USER tomcat

EXPOSE 8443

CMD ["catalina.sh", "run"]

````

### ENTRY: dockerfiles/Dockerfile_webapp

- bytes: 1049
- crc32: `0f6962d1`
- decoded_as: `utf-8`

````text
FROM tomcat:9.0.73-jre17-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY webapp.war ${TOMCAT_DIR}/webapps/
COPY logback.xml ${TOMCAT_DIR}/shared/conf/
COPY webappplatform.properties ${TOMCAT_DIR}/shared/conf/
COPY server.xml ${TOMCAT_DIR}/conf/
COPY keystore.p12 ${TOMCAT_DIR}/shared/conf/

RUN sed -i "s|shared\.loader=*$|shared\.loader=\"\${catalina.base}/shared/conf\"|" ${TOMCAT_DIR}/conf/catalina.properties && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' >> ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    chmod o+x ${SET_ENV_FILE} && \	
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist && \
    apt-get clean 

USER tomcat

EXPOSE 8443

CMD ["catalina.sh", "run"]

````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "137986481",
  "type": "attachment",
  "status": "current",
  "title": "dockerfiles.zip",
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
    "when": "2023-09-22T11:50:44.365+02:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/137986481/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/137986481"
    }
  },
  "position": -1,
  "container": {
    "id": "137986474",
    "type": "page",
    "status": "current",
    "title": "Deployment example for Web Application Platform on Kubernetes",
    "position": 5,
    "extensions": {
      "position": 5
    },
    "_links": {
      "webui": "/spaces/TWCloud2024x/pages/137986474/Deployment+example+for+Web+Application+Platform+on+Kubernetes",
      "edit": "/pages/resumedraft.action?draftId=137986474",
      "tinyui": "/x/qoE5C",
      "self": "https://docs.nomagic.com/rest/api/content/137986474"
    },
    "_expandable": {
      "container": "/rest/api/space/TWCloud2024x",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/137986474/child",
      "restrictions": "/rest/api/content/137986474/restriction/byOperation",
      "history": "/rest/api/content/137986474/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/137986474/descendant",
      "space": "/rest/api/space/TWCloud2024x",
      "relevantViewRestrictions": "/rest/api/content/137986474/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/zip"
  },
  "extensions": {
    "mediaType": "application/zip",
    "fileSize": 7382,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/137986474/dockerfiles.zip?version=1&modificationDate=1695376244365&api=v2",
    "webui": "/spaces/TWCloud2024x/pages/137986474/Deployment+example+for+Web+Application+Platform+on+Kubernetes?preview=%2F137986474%2F137986481%2Fdockerfiles.zip",
    "self": "https://docs.nomagic.com/rest/api/content/137986481"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/137986481/child",
    "restrictions": "/rest/api/content/137986481/restriction/byOperation",
    "history": "/rest/api/content/137986481/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/137986481/descendant",
    "space": "/rest/api/space/TWCloud2024x",
    "relevantViewRestrictions": "/rest/api/content/137986481/restriction/relevantViewRestrictions"
  }
}
````
