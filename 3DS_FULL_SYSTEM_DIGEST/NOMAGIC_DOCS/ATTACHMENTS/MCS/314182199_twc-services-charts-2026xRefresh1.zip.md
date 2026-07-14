# NOMAGIC ATTACHMENT: twc-services-charts-2026xRefresh1.zip

- attachment_id: `314182199`
- space_key: `MCS`
- parent_page_id: `247046576`
- parent_page_title: Deployment example on Kubernetes
- media_type: `application/zip`
- reported_bytes: 92560
- download_url: https://docs.nomagic.com/download/attachments/247046576/twc-services-charts-2026xRefresh1.zip?version=1&modificationDate=1782731926702&api=v2
- payload_kind: `archive-expanded`
- downloaded_sha256: `3058f176d9234f9faa4df5f849e33958ad63119a101843b27ff4e69a900085b8`

## ARCHIVE CONTENTS

### ENTRY: dockerfiles/admin-console/Dockerfile

- bytes: 947
- crc32: `468a60b3`
- decoded_as: `utf-8`

````text
FROM tomcat:11.0.8-jre21-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY admin.war ${TOMCAT_DIR}/webapps/
COPY ROOT ${TOMCAT_DIR}/webapps/ROOT

RUN sed -i "s|shared\.loader=*$|shared\.loader=\"\${catalina.base}/shared/conf\"|" ${CATALINA_HOME}/conf/catalina.properties && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' >> ${SET_ENV_FILE} && \
    chmod o+x ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y netcat curl && \
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist && \
    apt-get clean
    
USER tomcat

EXPOSE 8080

CMD ["catalina.sh", "run"]

````

### ENTRY: dockerfiles/authentication/Dockerfile

- bytes: 953
- crc32: `94747dea`
- decoded_as: `utf-8`

````text
FROM tomcat:11.0.8-jre21-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY authentication.war ${TOMCAT_DIR}/webapps/
COPY ROOT ${TOMCAT_DIR}/webapps/ROOT

RUN sed -i "s|shared\.loader=*$|shared\.loader=\"\${catalina.base}/shared/conf\"|" ${CATALINA_HOME}/conf/catalina.properties && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' >> ${SET_ENV_FILE} && \
    chmod o+x ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y netcat curl && \
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist && \
    apt-get clean

USER tomcat

EXPOSE 8080

CMD ["catalina.sh", "run"]


````

### ENTRY: dockerfiles/collaborator/Dockerfile

- bytes: 995
- crc32: `44d28f51`
- decoded_as: `utf-8`

````text
FROM tomcat:11.0.8-jre21-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY collaborator.war ${TOMCAT_DIR}/webapps/
COPY data ${TOMCAT_DIR}/shared/conf/data
COPY ROOT ${TOMCAT_DIR}/webapps/ROOT

RUN sed -i "s|shared\.loader=*$|shared\.loader=\"\${catalina.base}/shared/conf\"|" ${CATALINA_HOME}/conf/catalina.properties && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' >> ${SET_ENV_FILE} && \
    chmod o+x ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y netcat curl && \
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist && \
    apt-get clean
    
USER tomcat

EXPOSE 8080

CMD ["catalina.sh", "run"]

````

### ENTRY: dockerfiles/document-exporter/Dockerfile

- bytes: 1671
- crc32: `d6ef73d2`
- decoded_as: `utf-8`

````text
FROM tomcat:11.0.8-jre21-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}
ARG PRINCE_V=16.1
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

RUN sed -i "s|shared\.loader=*$|shared\.loader=\"\${catalina.base}/shared/conf\"|" ${CATALINA_HOME}/conf/catalina.properties && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' >> ${SET_ENV_FILE} && \
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
    apt-get clean

USER tomcat

EXPOSE 8080

CMD ["catalina.sh", "run"]

````

### ENTRY: dockerfiles/oslc/Dockerfile

- bytes: 946
- crc32: `1c2a890f`
- decoded_as: `utf-8`

````text
FROM tomcat:11.0.8-jre21-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY oslc.war ${TOMCAT_DIR}/webapps/
COPY ROOT ${TOMCAT_DIR}/webapps/ROOT

RUN sed -i "s|shared\.loader=*$|shared\.loader=\"\${catalina.base}/shared/conf\"|" ${CATALINA_HOME}/conf/catalina.properties && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' >> ${SET_ENV_FILE} && \
    chmod o+x ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y netcat curl && \
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist && \
    apt-get clean
    
USER tomcat

EXPOSE 8080

CMD ["catalina.sh", "run"]

````

### ENTRY: dockerfiles/reports/Dockerfile

- bytes: 946
- crc32: `aaa450c4`
- decoded_as: `utf-8`

````text
FROM tomcat:11.0.8-jre21-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY reports.war ${TOMCAT_DIR}/webapps/
COPY ROOT ${TOMCAT_DIR}/webapps/ROOT

RUN sed -i "s|shared\.loader=*$|shared\.loader=\"\${catalina.base}/shared/conf\"|" ${CATALINA_HOME}/conf/catalina.properties && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' >> ${SET_ENV_FILE} && \
    chmod o+x ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y netcat curl && \
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist  && \
    apt-get clean

USER tomcat

EXPOSE 8080

CMD ["catalina.sh", "run"]

````

### ENTRY: dockerfiles/resource-usage-map/Dockerfile

- bytes: 1080
- crc32: `ed682a09`
- decoded_as: `utf-8`

````text
FROM tomcat:11.0.8-jre21-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY resource-usage-map.war ${TOMCAT_DIR}/webapps/
COPY ROOT ${TOMCAT_DIR}/webapps/ROOT

RUN sed -i "s|shared\.loader=*$|shared\.loader=\"\${catalina.base}/shared/conf\"|" ${CATALINA_HOME}/conf/catalina.properties && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' >> ${SET_ENV_FILE} && \
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
    apt-get clean
    
USER tomcat

EXPOSE 8080 2468

CMD ["catalina.sh", "run"]

````

### ENTRY: dockerfiles/resources/Dockerfile

- bytes: 951
- crc32: `1c6c1f9d`
- decoded_as: `utf-8`

````text
FROM tomcat:11.0.8-jre21-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY resources.war ${TOMCAT_DIR}/webapps/
COPY ROOT ${TOMCAT_DIR}/webapps/ROOT

RUN sed -i "s|shared\.loader=*$|shared\.loader=\"\${catalina.base}/shared/conf\"|" ${CATALINA_HOME}/conf/catalina.properties && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' >> ${SET_ENV_FILE} && \
    chmod o+x ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y netcat curl && \
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist && \
    apt-get clean
    
USER tomcat

EXPOSE 8080

CMD ["catalina.sh", "run"]

````

### ENTRY: dockerfiles/simulation/Dockerfile

- bytes: 952
- crc32: `a139a362`
- decoded_as: `utf-8`

````text
FROM tomcat:11.0.8-jre21-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY simulation.war ${TOMCAT_DIR}/webapps/
COPY ROOT ${TOMCAT_DIR}/webapps/ROOT

RUN sed -i "s|shared\.loader=*$|shared\.loader=\"\${catalina.base}/shared/conf\"|" ${CATALINA_HOME}/conf/catalina.properties && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' >> ${SET_ENV_FILE} && \
    chmod o+x ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y netcat curl && \
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist && \
    apt-get clean
    
USER tomcat

EXPOSE 8080

CMD ["catalina.sh", "run"]

````

### ENTRY: dockerfiles/webapp/Dockerfile

- bytes: 944
- crc32: `ceffcc94`
- decoded_as: `utf-8`

````text
FROM tomcat:11.0.8-jre21-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY webapp.war ${TOMCAT_DIR}/webapps/
COPY ROOT ${TOMCAT_DIR}/webapps/ROOT

RUN sed -i "s|shared\.loader=*$|shared\.loader=\"\${catalina.base}/shared/conf\"|" ${CATALINA_HOME}/conf/catalina.properties && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' >> ${SET_ENV_FILE} && \
    chmod o+x ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y netcat curl && \
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist && \
    apt-get clean

USER tomcat

EXPOSE 8080

CMD ["catalina.sh", "run"]

````

### ENTRY: dockerfiles/magiclab/Dockerfile

- bytes: 1275
- crc32: `9ceefc60`
- decoded_as: `utf-8`

````text
FROM tomcat:11.0.8-jre21-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}
ARG CATALINA_HOME=${TOMCAT_DIR}

COPY magiclab.war ${TOMCAT_DIR}/webapps/
COPY ROOT ${TOMCAT_DIR}/webapps/ROOT

RUN sed -i "s|shared\.loader=*$|shared\.loader=\"\${catalina.base}/shared/conf\"|" ${CATALINA_HOME}/conf/catalina.properties && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' >> ${SET_ENV_FILE} && \
    echo 'export CATALINA_OPTS="$CATALINA_OPTS --add-opens=java.desktop/javax.swing.text=ALL-UNNAMED"' >> ${SET_ENV_FILE} && \
    chmod o+x ${SET_ENV_FILE} && \
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist && \
    apt-get update -y && \
    apt-get upgrade -y && \
    apt install dialog apt-utils -y && \
    echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | debconf-set-selections && \
    apt-get install ttf-mscorefonts-installer -y && \
	apt-get clean

USER tomcat

EXPOSE 8080

CMD ["catalina.sh", "run"]


````

### ENTRY: dockerfiles/sgi-crawler/Dockerfile

- bytes: 949
- crc32: `82cfbba4`
- decoded_as: `utf-8`

````text
FROM tomcat:11.0.8-jre21-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY sgi-crawler.war ${TOMCAT_DIR}/webapps/
COPY ROOT ${TOMCAT_DIR}/webapps/ROOT

RUN sed -i "s|shared\.loader=*$|shared\.loader=\"\${catalina.base}/shared/conf\"|" ${CATALINA_HOME}/conf/catalina.properties && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' >> ${SET_ENV_FILE} && \
    chmod o+x ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y netcat curl && \
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist && \
    apt-get clean

USER tomcat

EXPOSE 8080

CMD ["catalina.sh", "run"]

````

### ENTRY: dockerfiles/sysml2-api/Dockerfile

- bytes: 949
- crc32: `e3e6a545`
- decoded_as: `utf-8`

````text
FROM tomcat:11.0.8-jre21-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY sysmlv2-api.war ${TOMCAT_DIR}/webapps/
COPY ROOT ${TOMCAT_DIR}/webapps/ROOT

RUN sed -i "s|shared\.loader=*$|shared\.loader=\"\${catalina.base}/shared/conf\"|" ${CATALINA_HOME}/conf/catalina.properties && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' >> ${SET_ENV_FILE} && \
    chmod o+x ${SET_ENV_FILE} && \
    apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y netcat curl && \
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist && \
    apt-get clean

USER tomcat

EXPOSE 8080

CMD ["catalina.sh", "run"]

````

### ENTRY: dockerfiles/magiclabcollab/Dockerfile

- bytes: 1282
- crc32: `5e312826`
- decoded_as: `utf-8`

````text
FROM tomcat:11.0.8-jre21-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}
ARG CATALINA_HOME=${TOMCAT_DIR}

COPY magiclab-collaborator.war ${TOMCAT_DIR}/webapps/
COPY ROOT ${TOMCAT_DIR}/webapps/ROOT

RUN sed -i "s|shared\.loader=*$|shared\.loader=\"\${catalina.base}/shared/conf\"|" ${CATALINA_HOME}/conf/catalina.properties && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' >> ${SET_ENV_FILE} && \
    echo 'export CATALINA_OPTS="$CATALINA_OPTS --add-opens=java.desktop/javax.swing.text=ALL-UNNAMED"' >> ${SET_ENV_FILE} && \
    chmod o+x ${SET_ENV_FILE} && \
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist && \
	apt-get update -y && \
	apt-get upgrade -y && \
    apt install dialog apt-utils -y && \
    echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | debconf-set-selections && \
    apt-get install ttf-mscorefonts-installer -y && \
	apt-get clean

USER tomcat

EXPOSE 8080

CMD ["catalina.sh", "run"]


````

### ENTRY: dockerfiles/twcloud/Dockerfile

- bytes: 627
- crc32: `03b4f0f8`
- decoded_as: `utf-8`

````text
FROM eclipse-temurin:21.0.8_9-jre-jammy

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
    sed -i 's|\.\./Certs|configuration|g' /twcloud/configuration/application.conf && \
    chown -R twcloud:twcloud /twcloud
    

USER twcloud
EXPOSE 8111 3579

CMD ["/bin/bash", "twcloud"]
````

### ENTRY: helm-charts/charts/adminconsole/templates/deployment.yaml

- bytes: 80
- crc32: `0cba172d`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.deployment" . }}
{{- end }}

````

### ENTRY: helm-charts/charts/adminconsole/templates/service.yaml

- bytes: 78
- crc32: `1ceed9a4`
- decoded_as: `utf-8`

````yaml
{{- if .Values.enabled }}
{{- include "main-template.service" . }}
{{- end }}

````

### ENTRY: helm-charts/charts/adminconsole/values.yaml

- bytes: 1539
- crc32: `2ba22ec7`
- decoded_as: `utf-8`

````yaml
appName: admin-console-deployment
appLabel: admin-console
svcName: admin-console-service
ident: wap

# Specifies that local TWCloud is used (default true).
twcBuiltIn: true

env:
  value: >-
    -Denvironment=cloud
    -Dservice.internal.protocol=https
    -Dservice.internal.name={{ include "main-template.fullname" . }}
    -Dservice.internal.port=8443
    -Dtwc.ip={{ .Release.Name }}-twcloud
    -Dtwc.admin.username={{ .Values.global.twcAdminUsername }}
    -Dtwc.admin.password={{ .Values.global.twcAdminPassword }}
    -Dtwc.rest.port={{ .Values.global.twcRestPort }}
    -Dtwc.client.port={{ .Values.global.twcClientPort }}
    -Dzookeeper.server.ip={{ .Release.Name }}-zookeeper
    -Dzookeeper.server.port={{ .Values.global.zookeeperServerPort }}
    -Dservice.url={{ .Values.global.serviceUrl }}
    -Dauthentication.server.ip={{ .Values.global.authenticationServerIp }}
    -Dauthentication.server.port={{ .Values.global.authenticationServerPort }}
    -Dauthentication.server.protocol={{ .Values.global.authenticationServerProtocol }}
    -Dauthentication.client.secret={{ .Values.global.authenticationClientSecret }}
    -Dmessaging.server.ip={{ .Release.Name }}-artemis
    -Dmessaging.server.port={{ .Values.global.messagingServerPort }}
    -Dmessaging.server.security.enabled={{ .Values.global.messagingServerSecurityEnabled }}
    -Dmessaging.user.name={{ .Values.global.activeMqUserName }}
    -Dmessaging.user.password={{ .Values.global.activeMqPassword }}

service:
  type: ClusterIP
  port: 8443
  targetPort: 8443


````

### ENTRY: helm-charts/charts/adminconsole/Chart.yaml

- bytes: 139
- crc32: `cfc9971f`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: adminconsole
description: A Helm chart for admin-console
type: application
version: 0.1.5
appVersion: "2026xRefresh1"

````

### ENTRY: helm-charts/charts/artemis/templates/deployment.yaml

- bytes: 256
- crc32: `037b924d`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.deployment" . }}
{{- end }}
{{/*
{{ if .Values.admin_console.enabled }}
{{- include "main-template.deployment" . }}
{{- else }}
{{- printf "Values.admin_console.enabled is set to false" }}
{{- end }}
*/}}
````

### ENTRY: helm-charts/charts/artemis/templates/service.yaml

- bytes: 354
- crc32: `412df15b`
- decoded_as: `utf-8`

````yaml
{{- if .Values.enabled }}
{{- include "main-template.service" . }}
spec:
  type: {{ .Values.service.type }}
  selector:
    app: {{ .Values.appLabel }}
  ports:
    {{- range .Values.service.ports }}
      - name: {{ .name }}                
        port: {{ .port }}
        targetPort: {{ .targetPort }}
        protocol: TCP
    {{- end }}
{{- end }}

````

### ENTRY: helm-charts/charts/artemis/values.yaml

- bytes: 953
- crc32: `fd8352f3`
- decoded_as: `utf-8`

````yaml
# Default values for artemis.
# This is a YAML-formatted file.
# Declare variables to be passed into your templates.

appName: artemis-deployment
appLabel: artemis
svcName: artemis-service

containers:
  ports:
  - containerPort: 61616
  - containerPort: 8161
  - containerPort: 9404
  - containerPort: 5672
  - containerPort: 61613
  - containerPort: 5445
  - containerPort: 1883

service:
  type: ClusterIP
  ports:
  - name: service
    port: 61616
    targetPort: 61616
    protocol: TCP
  - name: console
    port: 8161
    targetPort: 8161
    protocol: UDP
  - name: broadcast
    port: 9404
    targetPort: 9404
    protocol: UDP
  - name: acceptor-amqp
    port: 5672
    targetPort: 5672
    protocol: TCP
  - name: acceptor-stomp
    port: 61613
    targetPort: 61613
    protocol: TCP
  - name: accep-hornetq
    port: 5445
    targetPort: 5445
    protocol: TCP
  - name: acceptor-mqt
    port: 1883
    targetPort: 1883
    protocol: TCP


````

### ENTRY: helm-charts/charts/artemis/Chart.yaml

- bytes: 1163
- crc32: `02710770`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: artemis
description: A Helm chart for Apache ActiveMQ artemis

# A chart can be either an 'application' or a 'library' chart.
#
# Application charts are a collection of templates that can be packaged into versioned archives
# to be deployed.
#
# Library charts provide useful utilities or functions for the chart developer. They're included as
# a dependency of application charts to inject those utilities and functions into the rendering
# pipeline. Library charts do not define any templates and therefore cannot be deployed.
type: application

# This is the chart version. This version number should be incremented each time you make changes
# to the chart and its templates, including the app version.
# Versions are expected to follow Semantic Versioning (https://semver.org/)
version: 0.1.5

# This is the version number of the application being deployed. This version number should be
# incremented each time you make changes to the application. Versions are not expected to
# follow Semantic Versioning. They should reflect the version the application is using.
# It is recommended to use it with quotes.
appVersion: "2026xRefresh1"

````

### ENTRY: helm-charts/charts/authentication/templates/deployment.yaml

- bytes: 80
- crc32: `0cba172d`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.deployment" . }}
{{- end }}

````

### ENTRY: helm-charts/charts/authentication/templates/service.yaml

- bytes: 77
- crc32: `60462dd0`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.service" . }}
{{- end }}

````

### ENTRY: helm-charts/charts/authentication/Chart.yaml

- bytes: 142
- crc32: `d321ca9d`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: authentication
description: A Helm chart for authentication
type: application
version: 0.1.5
appVersion: "2026xRefresh1"

````

### ENTRY: helm-charts/charts/authentication/values.yaml

- bytes: 1698
- crc32: `46b33bd7`
- decoded_as: `utf-8`

````yaml
appName: authentication-deployment
appLabel: authentication
svcName: authentication-service
ident: auth

# Specifies that local TWCloud is used (default true).
twcBuiltIn: true

env:
  value: >-
    -Denvironment=cloud
    -Dservice.internal.protocol=https
    -Dservice.internal.name={{ include "main-template.fullname" . }}
    -Dservice.internal.port=8443
    -Dtwc.ip={{ .Release.Name }}-twcloud
    -Dtwc.admin.username={{ .Values.global.twcAdminUsername }}
    -Dtwc.admin.password={{ .Values.global.twcAdminPassword }}
    -Dtwc.client.port={{ .Values.global.twcClientPort | default 3579 }}
    -Dtwc.rest.port={{ .Values.global.twcRestPort }}
    -Dtwc.client.port={{ .Values.global.twcClientPort }}
    -Dzookeeper.server.ip={{ .Release.Name }}-zookeeper
    -Dzookeeper.server.port={{ .Values.global.zookeeperServerPort }}
    -Dauthentication.server.ip={{ .Values.global.authenticationServerIp }}
    -Dauthentication.server.port={{ .Values.global.authenticationServerPort }}
    -Dservice.url={{ .Values.global.serviceUrl }}
    -Dauthentication.redirect.uri=https://{{ .Values.global.authenticationServerIp }}/webapp
    -Dauthentication.redirect.uri.whitelist=http
    -Dauthentication.server.key-store=./shared/conf/keystore.p12
    -Dmessaging.server.ip={{ .Release.Name }}-artemis
    -Dmessaging.server.port={{ .Values.global.messagingServerPort }}
    -Dmessaging.server.security.enabled={{ .Values.global.messagingServerSecurityEnabled }}
    -Dmessaging.user.name={{ .Values.global.activeMqUserName }}
    -Dmessaging.user.password={{ .Values.global.activeMqPassword }}
    -Dmessage.server.persistence.enabled=true

service:
  type: ClusterIP
  port: 8443
  targetPort: 8443


````

### ENTRY: helm-charts/charts/collaborator/templates/deployment.yaml

- bytes: 80
- crc32: `0cba172d`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.deployment" . }}
{{- end }}

````

### ENTRY: helm-charts/charts/collaborator/templates/service.yaml

- bytes: 77
- crc32: `60462dd0`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.service" . }}
{{- end }}

````

### ENTRY: helm-charts/charts/collaborator/Chart.yaml

- bytes: 138
- crc32: `17396f38`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: collaborator
description: A Helm chart for collaborator
type: application
version: 0.1.5
appVersion: "2026xRefresh1"

````

### ENTRY: helm-charts/charts/collaborator/values.yaml

- bytes: 1586
- crc32: `2fcf5270`
- decoded_as: `utf-8`

````yaml
appName: collaborator-deployment
appLabel: collaborator
svcName: collaborator-service
ident: wap

# Specifies that local TWCloud is used (default true).
twcBuiltIn: true

env:
  value: >-
    -Denvironment=cloud
    -Dservice.internal.protocol=https
    -Dservice.internal.name={{ include "main-template.fullname" . }}
    -Dservice.internal.port=8443
    -Dtwc.ip={{ .Release.Name }}-twcloud    
    -Dtwc.admin.username={{ .Values.global.twcAdminUsername }}
    -Dtwc.admin.password={{ .Values.global.twcAdminPassword }}
    -Dtwc.rest.port={{ .Values.global.twcRestPort }}
    -Dtwc.client.port={{ .Values.global.twcClientPort }}
    -Dzookeeper.server.ip={{ .Release.Name }}-zookeeper
    -Dzookeeper.server.port={{ .Values.global.zookeeperServerPort }}
    -Dservice.url={{ .Values.global.serviceUrl }}
    -Dauthentication.server.ip={{ .Values.global.authenticationServerIp }}
    -Dauthentication.server.port={{ .Values.global.authenticationServerPort }}
    -Dauthentication.server.protocol={{ .Values.global.authenticationServerProtocol }}
    -Dauthentication.client.secret={{ .Values.global.authenticationClientSecret }}
    -Dmessaging.server.ip={{ .Release.Name }}-artemis
    -Dmessaging.server.port={{ .Values.global.messagingServerPort }}
    -Dmessaging.server.security.enabled={{ .Values.global.messagingServerSecurityEnabled }}
    -Dmessaging.user.name={{ .Values.global.activeMqUserName }}
    -Dmessaging.user.password={{ .Values.global.activeMqPassword }}
    -Dmessage.server.persistence.enabled=true

service:
  type: ClusterIP
  port: 8443
  targetPort: 8443


````

### ENTRY: helm-charts/charts/docexporter/templates/deployment.yaml

- bytes: 80
- crc32: `0cba172d`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.deployment" . }}
{{- end }}

````

### ENTRY: helm-charts/charts/docexporter/templates/service.yaml

- bytes: 77
- crc32: `60462dd0`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.service" . }}
{{- end }}

````

### ENTRY: helm-charts/charts/docexporter/values.yaml

- bytes: 2129
- crc32: `34c2503b`
- decoded_as: `utf-8`

````yaml
appName: document-exporter-deployment
appLabel: docexporter
svcName: document-exporter-service
ident: wap

# Specifies that local TWCloud is used (default true).
twcBuiltIn: true

env:
  value: >-
    -Denvironment=cloud
    -Dservice.internal.protocol=https
    -Dservice.internal.name={{ include "main-template.fullname" . }}
    -Dservice.internal.port=8443
    -Dtwc.ip={{ .Release.Name }}-twcloud    
    -Dtwc.admin.username={{ .Values.global.twcAdminUsername }}
    -Dtwc.admin.password={{ .Values.global.twcAdminPassword }}
    -Dtwc.rest.port={{ .Values.global.twcRestPort }}
    -Dtwc.client.port={{ .Values.global.twcClientPort }}
    -Dzookeeper.server.ip={{ .Release.Name }}-zookeeper
    -Dzookeeper.server.port={{ .Values.global.zookeeperServerPort }}
    -Dservice.url={{ .Values.global.serviceUrl }}
    -Dauthentication.server.ip={{ .Values.global.authenticationServerIp }}
    -Dauthentication.server.port={{ .Values.global.authenticationServerPort }}
    -Dauthentication.server.protocol={{ .Values.global.authenticationServerProtocol }}
    -Dauthentication.client.secret={{ .Values.global.authenticationClientSecret }}
    -Dmessaging.server.ip={{ .Release.Name }}-artemis
    -Dmessaging.server.port={{ .Values.global.messagingServerPort }}
    -Dmessaging.server.security.enabled={{ .Values.global.messagingServerSecurityEnabled }}
    -Dmessaging.user.name={{ .Values.global.activeMqUserName }}
    -Dmessaging.user.password={{ .Values.global.activeMqPassword }}
    -Dmessage.server.persistence.enabled=true
    -Dlicense.server={{ .Values.global.licenseServer }}
    -Dlicense.framework={{ .Values.global.licenseFramework }}
    -Dignore.wap.twc.compatibility={{ .Values.global.ignoreWapTwcCompatibility }}	
    -Dmessaging.consumer.window.size=0
    -Dignore.wap.twc.compatibility=true
    -Ddocument.exporter.file.storing.time={{ .Values.global.docexporterFileStoring }}
    -Ddocument.exporter.prince.path={{ .Values.documentExporterPrincePath }}
    -Ddocument.exporter.prince.options=log=/usr/local/tomcat/logs/webappplatform/prince.log

service:
  type: ClusterIP
  port: 8443
  targetPort: 8443

````

### ENTRY: helm-charts/charts/docexporter/Chart.yaml

- bytes: 136
- crc32: `6f81ef89`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: docexporter
description: A Helm chart for docexporter
type: application
version: 0.1.5
appVersion: "2026xRefresh1"

````

### ENTRY: helm-charts/charts/oslc/templates/deployment.yaml

- bytes: 80
- crc32: `0cba172d`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.deployment" . }}
{{- end }}

````

### ENTRY: helm-charts/charts/oslc/templates/service.yaml

- bytes: 77
- crc32: `60462dd0`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.service" . }}
{{- end }}

````

### ENTRY: helm-charts/charts/oslc/values.yaml

- bytes: 1574
- crc32: `553f92ad`
- decoded_as: `utf-8`

````yaml
appName: oslc-deployment
appLabel: oslc
svcName: oslc-service
ident: wap

replicas: 1

# Specifies that local TWCloud is used (default true).
twcBuiltIn: true

env:
  value: >-
    -Denvironment=cloud
    -Dservice.internal.protocol=https
    -Dservice.internal.name={{ include "main-template.fullname" . }}
    -Dservice.internal.port=8443
    -Dtwc.ip={{ .Release.Name }}-twcloud    
    -Dtwc.admin.username={{ .Values.global.twcAdminUsername }}
    -Dtwc.admin.password={{ .Values.global.twcAdminPassword }}
    -Dtwc.rest.port={{ .Values.global.twcRestPort }}
    -Dtwc.client.port={{ .Values.global.twcClientPort }}
    -Dzookeeper.server.ip={{ .Release.Name }}-zookeeper
    -Dzookeeper.server.port={{ .Values.global.zookeeperServerPort }}
    -Dservice.url={{ .Values.global.serviceUrl }}
    -Dauthentication.server.ip={{ .Values.global.authenticationServerIp }}
    -Dauthentication.server.port={{ .Values.global.authenticationServerPort }}
    -Dauthentication.server.protocol={{ .Values.global.authenticationServerProtocol }}
    -Dauthentication.client.secret={{ .Values.global.authenticationClientSecret }}
    -Dmessaging.server.ip={{ .Release.Name }}-artemis
    -Dmessaging.server.port={{ .Values.global.messagingServerPort }}
    -Dmessaging.server.security.enabled={{ .Values.global.messagingServerSecurityEnabled }}
    -Dmessaging.user.name={{ .Values.global.activeMqUserName }}
    -Dmessaging.user.password={{ .Values.global.activeMqPassword }}
    -Dmessage.server.persistence.enabled=true

service:
  type: ClusterIP
  port: 8443
  targetPort: 8443

````

### ENTRY: helm-charts/charts/oslc/Chart.yaml

- bytes: 122
- crc32: `203aaaee`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: oslc
description: A Helm chart for oslc
type: application
version: 0.1.5
appVersion: "2026xRefresh1"

````

### ENTRY: helm-charts/charts/reports/templates/deployment.yaml

- bytes: 79
- crc32: `036665e7`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.deployment" . }}
{{- end }}
````

### ENTRY: helm-charts/charts/reports/templates/service.yaml

- bytes: 76
- crc32: `f9c975b3`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.service" . }}
{{- end }}
````

### ENTRY: helm-charts/charts/reports/values.yaml

- bytes: 1566
- crc32: `ceaea34b`
- decoded_as: `utf-8`

````yaml
appName: reports-deployment
appLabel: reports
svcName: reports-service
ident: wap

# Specifies that local TWCloud is used (default true).
twcBuiltIn: true

env:
  value: >-
    -Denvironment=cloud
    -Dservice.internal.protocol=https
    -Dservice.internal.name={{ include "main-template.fullname" . }}
    -Dservice.internal.port=8443
    -Dtwc.ip={{ .Release.Name }}-twcloud
    -Dtwc.admin.username={{ .Values.global.twcAdminUsername }}
    -Dtwc.admin.password={{ .Values.global.twcAdminPassword }}
    -Dtwc.rest.port={{ .Values.global.twcRestPort }}
    -Dtwc.client.port={{ .Values.global.twcClientPort }}
    -Dzookeeper.server.ip={{ .Release.Name }}-zookeeper
    -Dzookeeper.server.port={{ .Values.global.zookeeperServerPort }}
    -Dservice.url={{ .Values.global.serviceUrl }}
    -Dmessaging.server.ip={{ .Release.Name }}-artemis
    -Dmessaging.server.port={{ .Values.global.messagingServerPort }}
    -Dmessaging.server.security.enabled={{ .Values.global.messagingServerSecurityEnabled }}
    -Dmessaging.user.name={{ .Values.global.activeMqUserName }}
    -Dmessaging.user.password={{ .Values.global.activeMqPassword }}
    -Dmessage.server.persistence.enabled=true
    -Dauthentication.server.ip={{ .Values.global.authenticationServerIp }}
    -Dauthentication.server.port={{ .Values.global.authenticationServerPort }}
    -Dauthentication.server.protocol={{ .Values.global.authenticationServerProtocol }}
    -Dauthentication.client.secret={{ .Values.global.authenticationClientSecret }}

service:
  type: ClusterIP
  port: 8443
  targetPort: 8443

````

### ENTRY: helm-charts/charts/reports/Chart.yaml

- bytes: 128
- crc32: `29e1b366`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: reports
description: A Helm chart for reports
type: application
version: 0.1.5
appVersion: "2026xRefresh1"

````

### ENTRY: helm-charts/charts/resources/templates/deployment.yaml

- bytes: 80
- crc32: `0cba172d`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.deployment" . }}
{{- end }}

````

### ENTRY: helm-charts/charts/resources/templates/service.yaml

- bytes: 77
- crc32: `60462dd0`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.service" . }}
{{- end }}

````

### ENTRY: helm-charts/charts/resources/values.yaml

- bytes: 1572
- crc32: `9a1e27ec`
- decoded_as: `utf-8`

````yaml
appName: resources-deployment
appLabel: resources
svcName: resources-service
ident: wap

# Specifies that local TWCloud is used (default true).
twcBuiltIn: true

env:
  value: >-
    -Denvironment=cloud
    -Dservice.internal.protocol=https
    -Dservice.internal.name={{ include "main-template.fullname" . }}
    -Dservice.internal.port=8443
    -Dtwc.ip={{ .Release.Name }}-twcloud
    -Dtwc.admin.username={{ .Values.global.twcAdminUsername }}
    -Dtwc.admin.password={{ .Values.global.twcAdminPassword }}
    -Dtwc.rest.port={{ .Values.global.twcRestPort }}
    -Dtwc.client.port={{ .Values.global.twcClientPort }}
    -Dzookeeper.server.ip={{ .Release.Name }}-zookeeper
    -Dzookeeper.server.port={{ .Values.global.zookeeperServerPort }}
    -Dservice.url={{ .Values.global.serviceUrl }}
    -Dauthentication.server.ip={{ .Values.global.authenticationServerIp }}
    -Dauthentication.server.port={{ .Values.global.authenticationServerPort }}
    -Dauthentication.server.protocol={{ .Values.global.authenticationServerProtocol }}
    -Dauthentication.client.secret={{ .Values.global.authenticationClientSecret }}
    -Dmessaging.server.ip={{ .Release.Name }}-artemis
    -Dmessaging.server.port={{ .Values.global.messagingServerPort }}
    -Dmessaging.server.security.enabled={{ .Values.global.messagingServerSecurityEnabled }}
    -Dmessaging.user.name={{ .Values.global.activeMqUserName }}
    -Dmessaging.user.password={{ .Values.global.activeMqPassword }}
    -Dmessage.server.persistence.enabled=true

service:
  type: ClusterIP
  port: 8443
  targetPort: 8443

````

### ENTRY: helm-charts/charts/resources/Chart.yaml

- bytes: 132
- crc32: `079b1e0e`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: resources
description: A Helm chart for resources
type: application
version: 0.1.5
appVersion: "2026xRefresh1"

````

### ENTRY: helm-charts/charts/rum/templates/deployment.yaml

- bytes: 80
- crc32: `0cba172d`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.deployment" . }}
{{- end }}

````

### ENTRY: helm-charts/charts/rum/templates/service.yaml

- bytes: 77
- crc32: `60462dd0`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.service" . }}
{{- end }}

````

### ENTRY: helm-charts/charts/rum/values.yaml

- bytes: 1538
- crc32: `6534dd4e`
- decoded_as: `utf-8`

````yaml
appName: resource-usage-map-deployment
appLabel: rum
svcName: resource-usage-map-service
ident: wap

# Specifies that local TWCloud is used (default true).
twcBuiltIn: true

env:
  value: >-
    -Denvironment=cloud
    -Dservice.internal.protocol=https
    -Dservice.internal.name={{ include "main-template.fullname" . }}
    -Dservice.internal.port=8443
    -Dtwc.ip={{ .Release.Name }}-twcloud
    -Dtwc.admin.username={{ .Values.global.twcAdminUsername }}
    -Dtwc.admin.password={{ .Values.global.twcAdminPassword }}
    -Dtwc.rest.port={{ .Values.global.twcRestPort }}
    -Dtwc.client.port={{ .Values.global.twcClientPort }}
    -Dzookeeper.server.ip={{ .Release.Name }}-zookeeper
    -Dzookeeper.server.port={{ .Values.global.zookeeperServerPort }}
    -Dservice.url={{ .Values.global.serviceUrl }}
    -Dmessaging.server.ip={{ .Release.Name }}-artemis
    -Dmessaging.server.port={{ .Values.global.messagingServerPort }}
    -Dmessaging.server.security.enabled={{ .Values.global.messagingServerSecurityEnabled }}
    -Dmessaging.user.name={{ .Values.global.activeMqUserName }}
    -Dmessaging.user.password={{ .Values.global.activeMqPassword }}
    -Dauthentication.server.ip={{ .Values.global.authenticationServerIp }}
    -Dauthentication.server.port={{ .Values.global.authenticationServerPort }}
    -Dauthentication.server.protocol={{ .Values.global.authenticationServerProtocol }}
    -Dauthentication.client.secret={{ .Values.global.authenticationClientSecret }}

service:
  type: ClusterIP
  port: 8443
  targetPort: 8443

````

### ENTRY: helm-charts/charts/rum/Chart.yaml

- bytes: 135
- crc32: `bce8f15c`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: rum
description: A Helm chart for resource usage map
type: application
version: 0.1.5
appVersion: "2026xRefresh1"

````

### ENTRY: helm-charts/charts/simulation/templates/deployment.yaml

- bytes: 80
- crc32: `0cba172d`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.deployment" . }}
{{- end }}

````

### ENTRY: helm-charts/charts/simulation/templates/job.yaml

- bytes: 73
- crc32: `86d408b9`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.job" . }}
{{- end }}

````

### ENTRY: helm-charts/charts/simulation/templates/service.yaml

- bytes: 77
- crc32: `60462dd0`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.service" . }}
{{- end }}

````

### ENTRY: helm-charts/charts/simulation/Chart.yaml

- bytes: 134
- crc32: `78a2e95a`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: simulation
description: A Helm chart for simulation
type: application
version: 0.1.5
appVersion: "2026xRefresh1"

````

### ENTRY: helm-charts/charts/simulation/values.yaml

- bytes: 1638
- crc32: `99a89b46`
- decoded_as: `utf-8`

````yaml
appName: simulation-deployment
appJobName: simulation-job
appLabel: simulation
svcName: simulation-service
ident: wap

# Specifies that local TWCloud is used (default true).
twcBuiltIn: true

maxreplicas: 100
pollingInterval: 1
env:
  value: >-
    -Denvironment=cloud
    -Dservice.internal.protocol=https
    -Dservice.internal.name={{ include "main-template.fullname" . }}
    -Dservice.internal.port=8443
    -Dtwc.ip={{ .Release.Name }}-twcloud
    -Dtwc.admin.username={{ .Values.global.twcAdminUsername }}
    -Dtwc.admin.password={{ .Values.global.twcAdminPassword }}
    -Dtwc.rest.port={{ .Values.global.twcRestPort }}
    -Dtwc.client.port={{ .Values.global.twcClientPort }}
    -Dzookeeper.server.ip={{ .Release.Name }}-zookeeper
    -Dzookeeper.server.port={{ .Values.global.zookeeperServerPort }}
    -Dservice.url={{ .Values.global.serviceUrl }}
    -Dauthentication.server.ip={{ .Values.global.authenticationServerIp }}
    -Dauthentication.server.port={{ .Values.global.authenticationServerPort }}
    -Dauthentication.server.protocol={{ .Values.global.authenticationServerProtocol }}
    -Dauthentication.client.secret={{ .Values.global.authenticationClientSecret }}
    -Dmessaging.server.ip={{ .Release.Name }}-artemis
    -Dmessaging.server.port={{ .Values.global.messagingServerPort }}
    -Dmessaging.server.security.enabled={{ .Values.global.messagingServerSecurityEnabled }}
    -Dmessaging.user.name={{ .Values.global.activeMqUserName }}
    -Dmessaging.user.password={{ .Values.global.activeMqPassword }}
    -Dmessage.server.persistence.enabled=true

service:
  type: ClusterIP
  port: 8443
  targetPort: 8443

````

### ENTRY: helm-charts/charts/twcloud/templates/service.yaml

- bytes: 1456
- crc32: `4c79ab1f`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
apiVersion: v1
kind: Service
metadata:
  name: {{ include "main-template.fullname" . }}
  labels:
    app: {{ .Values.labels.app }}
spec:
  type: ClusterIP
  selector:
    app: twcloud
  ports:
    - port: 3579
      name: main
      protocol: TCP
    - port: 8111
      name: admin-port
      protocol: TCP
    - port: 2552
      name: twc-remote
      protocol: TCP
    - port: 2468
      name: jmx
      protocol: TCP
  sessionAffinity: ClientIP
  sessionAffinityConfig:
    clientIP:
      timeoutSeconds: 600
---
apiVersion: v1
kind: Service
metadata:
  name: {{ include "main-template.fullname" . }}-headless
spec:
  clusterIP: None 
  selector:
    app: {{ .Values.labels.app }}
  ports:
    - port: 3579
      name: main
      protocol: TCP
    - port: 8111
      name: admin-port
      protocol: TCP
    - port: 2552
      name: twc-remote
      protocol: TCP
    - port: 2468
      name: jmx
      protocol: TCP
---
{{- if .Values.svcLB }}
apiVersion: v1
kind: Service
metadata:
  name: {{ include "main-template.fullname" . }}-lb
  labels:
    app: {{ .Values.labels.app }}
spec:
  type: LoadBalancer
  selector:
    app: twcloud
  ports:
    - port: 3579
      name: main
      protocol: TCP
    - port: 8111
      name: admin-port
      protocol: TCP
    - port: 2468
      name: jmx
      protocol: TCP
  sessionAffinity: ClientIP
  sessionAffinityConfig:
    clientIP:
      timeoutSeconds: 600
{{- end }}
{{- end }}
````

### ENTRY: helm-charts/charts/twcloud/templates/statefulset.yaml

- bytes: 4481
- crc32: `2d5bb10f`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: {{ include "main-template.fullname" . }}
  labels:
    app: {{ .Values.labels.app }}
spec:
  updateStrategy:
    type: RollingUpdate
  selector:
    matchLabels:
      app: {{ .Values.labels.app }}
  replicas: {{ .Values.replicas }}
  serviceName: {{ include "main-template.fullname" . }}-headless
  template:
    metadata:
      namespace: {{ .Release.Namespace }}
      name: {{ .Values.labels.app }}
      annotations:
        checksum/twcloud-config: {{ $.Files.Glob "configs/twcloud/*" | toYaml | sha256sum | quote }}
      labels:
        app: {{ .Values.labels.app }}
    spec:
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            - labelSelector:
                matchExpressions:
                  - key: app
                    operator: In
                    values:
                      - twcloud
              topologyKey: "kubernetes.io/hostname"
        podAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            - labelSelector:
                matchExpressions:
                  - key: app
                    operator: In
                    values:
                      - cassandra
              namespaces:
              - {{ .Release.Namespace }}
              topologyKey: "kubernetes.io/hostname"
      volumes:
        - name: config-volume          
          configMap:
            name: {{ .Release.Name }}-twcloud-cm
        - name: certs
          secret:
            secretName: {{ .Release.Name }}-certificates
      serviceAccountName: {{ .Release.Name }}-tcas
      containers:
      - name: twcloud
        image: {{ .Values.global.repoURL }}{{ .Values.image.repository }}:{{ .Values.image.tag }}
        imagePullPolicy: {{ .Values.global.pullPolicy }}
        ports:
          - containerPort: 8111
            name: admin-port
          - containerPort: 3579
            name: main
          - containerPort: 2552
            name: twc-remote
          - containerPort: 2468
            name: jmx
        env:
          - name: TWC_ZOOKEEPER_URL
            value: '{{ .Values.global.zookeeperServerIp }}:{{ .Values.global.zookeeperServerPort }}'
          - name: TWC_ZOOKEEPER_PATH
            value: '/akka/cluster/seed'
          - name: TWC_XMX
            value: '{{ .Values.env.twcxmx }}'
          - name: POD_IP
            valueFrom:
              fieldRef:
                fieldPath: status.podIP
          - name: POD_NAME
            valueFrom:
              fieldRef:
                fieldPath: metadata.name
          - name: STS_INDEX
            valueFrom:
              fieldRef:
                fieldPath: metadata.labels['apps.kubernetes.io/pod-index']     
          - name: TWCLOUD_OPTS
            value: {{ tpl .Values.env.value . | quote }}
        envFrom:
        - configMapRef:
            name: {{ .Release.Name }}-cassandra-seeds
        volumeMounts:
        - mountPath: /twcloud/configuration/application.conf
          name: config-volume
          subPath: application.conf
          readOnly: true
        - mountPath: /twcloud/jvm.options
          name: config-volume
          subPath: jvm.options
          readOnly: true
        - mountPath: /twcloud/configuration/logback.xml
          name: config-volume
          subPath: logback.xml
          readOnly: true
        - mountPath: /twcloud/configuration/teamworkcloud.crt
          name: certs
          subPath: teamworkcloud.crt
          readOnly: true
        - mountPath: /twcloud/configuration/keystore.p12
          name: certs
          subPath: keystore.p12
          readOnly: true
        resources:
          requests:
            memory: '{{ .Values.resources.requests.memory }}'
            cpu: '{{ .Values.resources.requests.cpu }}'
          limits:
            memory: '{{ .Values.resources.requests.memory }}'
            cpu: '{{ .Values.resources.requests.cpu }}'
        readinessProbe:
          tcpSocket:
            port: 3579
          initialDelaySeconds: 30
          periodSeconds: 5
          timeoutSeconds: 5
          failureThreshold: 60
          successThreshold: 1
        livenessProbe:
          tcpSocket:
            port: 3579
          initialDelaySeconds: 5
          timeoutSeconds: 5
          periodSeconds: 5
          failureThreshold: 60
          successThreshold: 1
      {{- include "main-template.init-container" . }}
{{ end }}
````

### ENTRY: helm-charts/charts/twcloud/Chart.yaml

- bytes: 128
- crc32: `2d4ad83c`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: twcloud
description: A Helm chart for twcloud
type: application
version: 0.1.5
appVersion: "2026xRefresh1"

````

### ENTRY: helm-charts/charts/twcloud/values.yaml

- bytes: 631
- crc32: `8e4e2796`
- decoded_as: `utf-8`

````yaml
labels:
  app: twcloud

env:
  value: >-
    -Desi.auth.url=https://{{ .Values.global.authenticationServerIp }}:{{ .Values.global.authenticationServerPort }}
    -Desi.httpd.ssl.enabled=true
    -Desi.zookeeper.cassandra.enabled=false
    -Desi.zookeeper.twc.enabled=true
    -Desi.zookeeper.url={{ .Release.Name }}-zookeeper:{{ .Values.global.zookeeperServerPort }}
    -Desi.net.connectors.0.host=$(POD_IP)
    -Desi.net.connectors.0.port=3579
    -Desi.net.connectors.0.protocol=raw
    -Desi.persistence.cassandra-access-lock.skip-lock-validation=true
    -Desi.zookeeper.akka.enabled=true
    -Desi.server.env.kubernetes=true

````

### ENTRY: helm-charts/charts/webapp/templates/deployment.yaml

- bytes: 82
- crc32: `17e55806`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.deployment" . }}   
{{- end }}
````

### ENTRY: helm-charts/charts/webapp/templates/service.yaml

- bytes: 77
- crc32: `60462dd0`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.service" . }}
{{- end }}

````

### ENTRY: helm-charts/charts/webapp/values.yaml

- bytes: 1289
- crc32: `49f7af68`
- decoded_as: `utf-8`

````yaml
appName: webapp-deployment
appLabel: webapp
svcName: webapp-service
ident: wap
#fullnameOverride: webapp

# Specifies that local TWCloud is used (default true).
twcBuiltIn: true

env:
  value: >-
    -Denvironment=cloud
    -Dservice.internal.protocol=https
    -Dservice.internal.name={{ include "main-template.fullname" . }}
    -Dservice.internal.port=8443
    -Dtwc.ip={{ .Release.Name }}-twcloud
    -Dtwc.admin.username={{ .Values.global.twcAdminUsername }}
    -Dtwc.admin.password={{ .Values.global.twcAdminPassword }}
    -Dtwc.rest.port={{ .Values.global.twcRestPort }}
    -Dtwc.client.port={{ .Values.global.twcClientPort }}
    -Dzookeeper.server.ip={{ .Release.Name }}-zookeeper
    -Dzookeeper.server.port={{ .Values.global.zookeeperServerPort }}
    -Dservice.url={{ .Values.global.serviceUrl }}
    -Dauthentication.server.ip={{ .Values.global.authenticationServerIp }}
    -Dauthentication.server.port={{ .Values.global.authenticationServerPort }}
    -Dauthentication.server.protocol={{ .Values.global.authenticationServerProtocol }}
    -Dauthentication.client.secret={{ .Values.global.authenticationClientSecret }}
    -Dauthentication.redirect.uri=https://{{ .Values.global.authenticationServerIp }}/webapp

service:
  type: ClusterIP
  port: 8443
  targetPort: 8443

````

### ENTRY: helm-charts/charts/webapp/Chart.yaml

- bytes: 126
- crc32: `01228d0c`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: webapp
description: A Helm chart for webapp
type: application
version: 0.1.5
appVersion: "2026xRefresh1"

````

### ENTRY: helm-charts/charts/elementchooser/Chart.yaml

- bytes: 142
- crc32: `06e18370`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: elementchooser
description: A Helm chart for elementchooser
type: application
version: 0.1.5
appVersion: "2026xRefresh1"

````

### ENTRY: helm-charts/charts/elementchooser/templates/deployment.yaml

- bytes: 79
- crc32: `036665e7`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.deployment" . }}
{{- end }}
````

### ENTRY: helm-charts/charts/elementchooser/templates/service.yaml

- bytes: 76
- crc32: `f9c975b3`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.service" . }}
{{- end }}
````

### ENTRY: helm-charts/charts/elementchooser/values.yaml

- bytes: 1083
- crc32: `e33a2187`
- decoded_as: `utf-8`

````yaml
appLabel: elementchooser
ident: wap

replicas: 1

# Specifies that local TWCloud is used (default true).
twcBuiltIn: true

env:
  value: >-
    -Denvironment=cloud
    -Dservice.internal.protocol=https
    -Dservice.internal.name={{ include "main-template.fullname" . }}
    -Dservice.internal.port=8443
    -Dtwc.ip={{ .Release.Name }}-twcloud
    -Dtwc.admin.username={{ .Values.global.twcAdminUsername }}
    -Dtwc.admin.password={{ .Values.global.twcAdminPassword }}
    -Dtwc.rest.port={{ .Values.global.twcRestPort }}
    -Dzookeeper.server.ip={{ .Release.Name }}-zookeeper
    -Dzookeeper.server.port={{ .Values.global.zookeeperServerPort }}
    -Dservice.url={{ .Values.global.serviceUrl }}
    -Dauthentication.server.ip={{ .Values.global.authenticationServerIp }}
    -Dauthentication.server.port={{ .Values.global.authenticationServerPort }}
    -Dauthentication.server.protocol={{ .Values.global.authenticationServerProtocol }}
    -Dauthentication.client.secret={{ .Values.global.authenticationClientSecret }}

service:
  type: ClusterIP
  port: 8443
  targetPort: 8443

````

### ENTRY: helm-charts/charts/magiclab/Chart.yaml

- bytes: 129
- crc32: `942a1d28`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: magiclab
description: A Helm chart for MagicLab
type: application
version: 0.1.5
appVersion: "2026xRefresh1"
````

### ENTRY: helm-charts/charts/magiclab/templates/deployment.yaml

- bytes: 80
- crc32: `0cba172d`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.deployment" . }}
{{- end }}

````

### ENTRY: helm-charts/charts/magiclab/templates/service.yaml

- bytes: 78
- crc32: `1ceed9a4`
- decoded_as: `utf-8`

````yaml
{{- if .Values.enabled }}
{{- include "main-template.service" . }}
{{- end }}

````

### ENTRY: helm-charts/charts/magiclab/values.yaml

- bytes: 1586
- crc32: `a1a5f0ce`
- decoded_as: `utf-8`

````yaml
appName: magiclab-deployment
appLabel: magiclab
svcName: magiclab-service
ident: wap

replicas: 1

# Specifies that local TWCloud is used (default true).
twcBuiltIn: true

env:
  value: >-
    -Denvironment=cloud
    -Dservice.internal.protocol=https
    -Dservice.internal.name={{ include "main-template.fullname" . }}
    -Dservice.internal.port=8443
    -Dtwc.ip={{ .Release.Name }}-twcloud    
    -Dtwc.admin.username={{ .Values.global.twcAdminUsername }}
    -Dtwc.admin.password={{ .Values.global.twcAdminPassword }}
    -Dtwc.rest.port={{ .Values.global.twcRestPort }}
    -Dtwc.client.port={{ .Values.global.twcClientPort }}
    -Dzookeeper.server.ip={{ .Release.Name }}-zookeeper
    -Dzookeeper.server.port={{ .Values.global.zookeeperServerPort }}
    -Dservice.url={{ .Values.global.serviceUrl }}
    -Dauthentication.server.ip={{ .Values.global.authenticationServerIp }}
    -Dauthentication.server.port={{ .Values.global.authenticationServerPort }}
    -Dauthentication.server.protocol={{ .Values.global.authenticationServerProtocol }}
    -Dauthentication.client.secret={{ .Values.global.authenticationClientSecret }}
    -Dmessaging.server.ip={{ .Release.Name }}-artemis
    -Dmessaging.server.port={{ .Values.global.messagingServerPort }}
    -Dmessaging.server.security.enabled={{ .Values.global.messagingServerSecurityEnabled }}
    -Dmessaging.user.name={{ .Values.global.activeMqUserName }}
    -Dmessaging.user.password={{ .Values.global.activeMqPassword }}
    -Dmessage.server.persistence.enabled=true

service:
  type: ClusterIP
  port: 8443
  targetPort: 8443

````

### ENTRY: helm-charts/charts/sgicrawler/Chart.yaml

- bytes: 134
- crc32: `92094e48`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: sgicrawler
description: A Helm chart for sgicrawler
type: application
version: 0.1.5
appVersion: "2026xRefresh1"

````

### ENTRY: helm-charts/charts/sgicrawler/templates/deployment.yaml

- bytes: 80
- crc32: `0cba172d`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.deployment" . }}
{{- end }}

````

### ENTRY: helm-charts/charts/sgicrawler/templates/service.yaml

- bytes: 77
- crc32: `60462dd0`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.service" . }}
{{- end }}

````

### ENTRY: helm-charts/charts/sgicrawler/values.yaml

- bytes: 1531
- crc32: `e35d5876`
- decoded_as: `utf-8`

````yaml
appName: sgi-crawler-deployment
appLabel: sgicrawler
svcName: sgi-crawler-service
ident: wap

# Specifies that local TWCloud is used (default true).
twcBuiltIn: true

env:
  value: >-
    -Denvironment=cloud
    -Dservice.internal.protocol=https
    -Dservice.internal.name={{ include "main-template.fullname" . }}
    -Dservice.internal.port=8443
    -Dtwc.ip={{ .Release.Name }}-twcloud
    -Dtwc.admin.username={{ .Values.global.twcAdminUsername }}
    -Dtwc.admin.password={{ .Values.global.twcAdminPassword }}
    -Dtwc.rest.port={{ .Values.global.twcRestPort }}
    -Dtwc.client.port={{ .Values.global.twcClientPort }}
    -Dzookeeper.server.ip={{ .Release.Name }}-zookeeper
    -Dzookeeper.server.port={{ .Values.global.zookeeperServerPort }}
    -Dservice.url={{ .Values.global.serviceUrl }}
    -Dmessaging.server.ip={{ .Release.Name }}-artemis
    -Dmessaging.server.port={{ .Values.global.messagingServerPort }}
    -Dmessaging.server.security.enabled={{ .Values.global.messagingServerSecurityEnabled }}
    -Dmessaging.user.name={{ .Values.global.activeMqUserName }}
    -Dmessaging.user.password={{ .Values.global.activeMqPassword }}
    -Dauthentication.server.ip={{ .Values.global.authenticationServerIp }}
    -Dauthentication.server.port={{ .Values.global.authenticationServerPort }}
    -Dauthentication.server.protocol={{ .Values.global.authenticationServerProtocol }}
    -Dauthentication.client.secret={{ .Values.global.authenticationClientSecret }}

service:
  type: ClusterIP
  port: 8443
  targetPort: 8443

````

### ENTRY: helm-charts/charts/sysml2api/Chart.yaml

- bytes: 133
- crc32: `a4cbefa5`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: sysml2api
description: A Helm chart for sysmlv2api
type: application
version: 0.1.5
appVersion: "2026xRefresh1"

````

### ENTRY: helm-charts/charts/sysml2api/templates/deployment.yaml

- bytes: 80
- crc32: `0cba172d`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.deployment" . }}
{{- end }}

````

### ENTRY: helm-charts/charts/sysml2api/templates/service.yaml

- bytes: 77
- crc32: `60462dd0`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.service" . }}
{{- end }}

````

### ENTRY: helm-charts/charts/sysml2api/values.yaml

- bytes: 1528
- crc32: `8d7db49a`
- decoded_as: `utf-8`

````yaml
appName: sysml2-api-deployment
appLabel: sysml2api
svcName: sysml2-api-service
ident: wap

# Specifies that local TWCloud is used (default true).
twcBuiltIn: true

env:
  value: >-
    -Denvironment=cloud
    -Dservice.internal.protocol=https
    -Dservice.internal.name={{ include "main-template.fullname" . }}
    -Dservice.internal.port=8443
    -Dtwc.ip={{ .Release.Name }}-twcloud
    -Dtwc.admin.username={{ .Values.global.twcAdminUsername }}
    -Dtwc.admin.password={{ .Values.global.twcAdminPassword }}
    -Dtwc.rest.port={{ .Values.global.twcRestPort }}
    -Dtwc.client.port={{ .Values.global.twcClientPort }}
    -Dzookeeper.server.ip={{ .Release.Name }}-zookeeper
    -Dzookeeper.server.port={{ .Values.global.zookeeperServerPort }}
    -Dservice.url={{ .Values.global.serviceUrl }}
    -Dmessaging.server.ip={{ .Release.Name }}-artemis
    -Dmessaging.server.port={{ .Values.global.messagingServerPort }}
    -Dmessaging.server.security.enabled={{ .Values.global.messagingServerSecurityEnabled }}
    -Dmessaging.user.name={{ .Values.global.activeMqUserName }}
    -Dmessaging.user.password={{ .Values.global.activeMqPassword }}
    -Dauthentication.server.ip={{ .Values.global.authenticationServerIp }}
    -Dauthentication.server.port={{ .Values.global.authenticationServerPort }}
    -Dauthentication.server.protocol={{ .Values.global.authenticationServerProtocol }}
    -Dauthentication.client.secret={{ .Values.global.authenticationClientSecret }}

service:
  type: ClusterIP
  port: 8443
  targetPort: 8443

````

### ENTRY: helm-charts/charts/magiclabcollab/Chart.yaml

- bytes: 148
- crc32: `32363605`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: magiclabcollab
description: A Helm chart for MagicLab-Collaborator
type: application
version: 0.1.5
appVersion: "2026xRefresh1"
````

### ENTRY: helm-charts/charts/magiclabcollab/templates/deployment.yaml

- bytes: 80
- crc32: `0cba172d`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.deployment" . }}
{{- end }}

````

### ENTRY: helm-charts/charts/magiclabcollab/templates/service.yaml

- bytes: 78
- crc32: `1ceed9a4`
- decoded_as: `utf-8`

````yaml
{{- if .Values.enabled }}
{{- include "main-template.service" . }}
{{- end }}

````

### ENTRY: helm-charts/charts/magiclabcollab/values.yaml

- bytes: 1604
- crc32: `715c394f`
- decoded_as: `utf-8`

````yaml
appName: magiclabcollab-deployment
appLabel: magiclabcollab
svcName: magiclabcollab-service
ident: wap

replicas: 1

# Specifies that local TWCloud is used (default true).
twcBuiltIn: true

env:
  value: >-
    -Denvironment=cloud
    -Dservice.internal.protocol=https
    -Dservice.internal.name={{ include "main-template.fullname" . }}
    -Dservice.internal.port=8443
    -Dtwc.ip={{ .Release.Name }}-twcloud    
    -Dtwc.admin.username={{ .Values.global.twcAdminUsername }}
    -Dtwc.admin.password={{ .Values.global.twcAdminPassword }}
    -Dtwc.rest.port={{ .Values.global.twcRestPort }}
    -Dtwc.client.port={{ .Values.global.twcClientPort }}
    -Dzookeeper.server.ip={{ .Release.Name }}-zookeeper
    -Dzookeeper.server.port={{ .Values.global.zookeeperServerPort }}
    -Dservice.url={{ .Values.global.serviceUrl }}
    -Dauthentication.server.ip={{ .Values.global.authenticationServerIp }}
    -Dauthentication.server.port={{ .Values.global.authenticationServerPort }}
    -Dauthentication.server.protocol={{ .Values.global.authenticationServerProtocol }}
    -Dauthentication.client.secret={{ .Values.global.authenticationClientSecret }}
    -Dmessaging.server.ip={{ .Release.Name }}-artemis
    -Dmessaging.server.port={{ .Values.global.messagingServerPort }}
    -Dmessaging.server.security.enabled={{ .Values.global.messagingServerSecurityEnabled }}
    -Dmessaging.user.name={{ .Values.global.activeMqUserName }}
    -Dmessaging.user.password={{ .Values.global.activeMqPassword }}
    -Dmessage.server.persistence.enabled=true

service:
  type: ClusterIP
  port: 8443
  targetPort: 8443

````

### ENTRY: helm-charts/charts/zookeeper/templates/NOTES.txt

- bytes: 1943
- crc32: `c7922ce2`
- decoded_as: `utf-8`

````text
ZooKeeper has been deployed!

Release name : {{ .Release.Name }}
Namespace    : {{ .Release.Namespace }}
Replicas     : {{ .Values.replicas }}
Image        : {{ .Values.image.repository }}:{{ .Values.image.tag | default .Chart.AppVersion }}

=== Connect to ZooKeeper ===

Client endpoint (within cluster):
  {{ include "zookeeper.fullname" . }}.{{ .Release.Namespace }}.svc.cluster.local:{{ .Values.zookeeper.clientPort }}

Individual pod DNS (headless service):
{{- $fullname := include "zookeeper.fullname" . }}
{{- $headless := include "zookeeper.headlessServiceName" . }}
{{- range $i := until (int .Values.replicas) }}
  {{ $fullname }}-{{ $i }}.{{ $headless }}.{{ $.Release.Namespace }}.svc.cluster.local
{{- end }}

=== Quick Test ===

Run a ZooKeeper client pod to test connectivity:

  kubectl run zk-client --rm -it \
    --image zookeeper:{{ .Values.image.tag | default .Chart.AppVersion }} \
    --restart=Never \
    -- zkCli.sh -server {{ include "zookeeper.fullname" . }}.{{ .Release.Namespace }}.svc.cluster.local:{{ .Values.zookeeper.clientPort }}

Or test with ruok (4-letter word command):

  kubectl exec -n {{ .Release.Namespace }} {{ include "zookeeper.fullname" . }}-0 -- \
    bash -c "echo ruok | nc localhost {{ .Values.zookeeper.clientPort }}"

Expected output: imok

{{- if .Values.zookeeper.adminServer.enabled }}
=== Admin Server ===

Access the ZooKeeper Admin HTTP server:

  kubectl port-forward svc/{{ include "zookeeper.fullname" . }} {{ .Values.zookeeper.adminServer.port }}:{{ .Values.zookeeper.adminServer.port }} -n {{ .Release.Namespace }}
  curl http://localhost:{{ .Values.zookeeper.adminServer.port }}/commands
  curl http://localhost:{{ .Values.zookeeper.adminServer.port }}/commands/stats
  curl http://localhost:{{ .Values.zookeeper.adminServer.port }}/commands/leader
{{- else }}
=== Admin Server ===

Admin server is disabled. To enable it, set:
  zookeeper.adminServer.enabled: true
{{- end }}

````

### ENTRY: helm-charts/charts/zookeeper/templates/pdb.yaml

- bytes: 409
- crc32: `3e53a2b2`
- decoded_as: `utf-8`

````yaml
{{- if .Values.podDisruptionBudget.enabled }}
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: {{ include "zookeeper.fullname" . }}
  namespace: {{ .Release.Namespace }}
  labels:
    {{- include "zookeeper.labels" . | nindent 4 }}
spec:
  minAvailable: {{ max 0 (sub .Values.replicas 1) }}
  selector:
    matchLabels:
      {{- include "zookeeper.selectorLabels" . | nindent 6 }}
{{- end }}
````

### ENTRY: helm-charts/charts/zookeeper/templates/service.yaml

- bytes: 1953
- crc32: `95eac654`
- decoded_as: `utf-8`

````yaml
---
## Client-facing ClusterIP service
apiVersion: v1
kind: Service
metadata:
  name: {{ include "zookeeper.fullname" . }}
  namespace: {{ .Release.Namespace }}
  labels:
    {{- include "zookeeper.labels" . | nindent 4 }}
  {{- with .Values.service.client.annotations }}
  annotations:
    {{- toYaml . | nindent 4 }}
  {{- end }}
spec:
  type: {{ .Values.service.client.type }}
  ports:
    - name: client
      port: {{ .Values.service.client.port }}
      targetPort: client
      protocol: TCP
    {{- if .Values.zookeeper.adminServer.enabled }}
    - name: admin
      port: {{ .Values.zookeeper.adminServer.port }}
      targetPort: admin
      protocol: TCP
    {{- end }}
  selector:
    {{- include "zookeeper.selectorLabels" . | nindent 4 }}

---
## Headless service for StatefulSet pod DNS resolution
## Each pod will be reachable at: <pod-name>.<headless-svc>.<namespace>.svc.cluster.local
apiVersion: v1
kind: Service
metadata:
  name: {{ include "zookeeper.headlessServiceName" . }}
  namespace: {{ .Release.Namespace }}
  labels:
    {{- include "zookeeper.labels" . | nindent 4 }}
  {{- with .Values.service.headless.annotations }}
  annotations:
    {{- toYaml . | nindent 4 }}
  {{- end }}
spec:
  type: ClusterIP
  clusterIP: None
  publishNotReadyAddresses: true
  ports:
    - name: client
      port: {{ .Values.zookeeper.clientPort }}
      targetPort: client
      protocol: TCP
    {{- if gt (int .Values.replicas) 1 }}
    - name: follower
      port: {{ .Values.zookeeper.serverPort }}
      targetPort: follower
      protocol: TCP
    - name: election
      port: {{ .Values.zookeeper.leaderElectionPort }}
      targetPort: election
      protocol: TCP
    {{- end }}
    {{- if .Values.zookeeper.adminServer.enabled }}
    - name: admin
      port: {{ .Values.zookeeper.adminServer.port }}
      targetPort: admin
      protocol: TCP
    {{- end }}
  selector:
    {{- include "zookeeper.selectorLabels" . | nindent 4 }}

````

### ENTRY: helm-charts/charts/zookeeper/templates/serviceaccount.yaml

- bytes: 362
- crc32: `111af29e`
- decoded_as: `utf-8`

````yaml
{{- if .Values.serviceAccount.create -}}
apiVersion: v1
kind: ServiceAccount
metadata:
  name: {{ include "zookeeper.serviceAccountName" . }}
  namespace: {{ .Release.Namespace }}
  labels:
    {{- include "zookeeper.labels" . | nindent 4 }}
  {{- with .Values.serviceAccount.annotations }}
  annotations:
    {{- toYaml . | nindent 4 }}
  {{- end }}
{{- end }}

````

### ENTRY: helm-charts/charts/zookeeper/templates/statefulset.yaml

- bytes: 12334
- crc32: `f16efd24`
- decoded_as: `utf-8`

````yaml
{{- $dataEnabled := and .Values.persistence.enabled .Values.persistence.data.enabled }}
{{- $logEnabled := and .Values.persistence.enabled .Values.persistence.log.enabled }}
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: {{ include "zookeeper.fullname" . }}
  namespace: {{ .Release.Namespace }}
  labels:
    {{- include "zookeeper.labels" . | nindent 4 }}
spec:
  serviceName: {{ include "zookeeper.headlessServiceName" . }}
  replicas: {{ .Values.replicas }}
  selector:
    matchLabels:
      {{- include "zookeeper.selectorLabels" . | nindent 6 }}
  ##
  ## OrderedReady ensures pods start and stop one at a time in order (0, 1, 2...).
  ## This is important for ZooKeeper so the ensemble forms quorum correctly on startup
  ## and doesn't lose quorum during rolling updates or restarts.
  ## (Parallel would start all pods simultaneously which can cause split-brain on first boot)
  ##
  podManagementPolicy: OrderedReady
  updateStrategy:
    type: {{ .Values.updateStrategy.type }}
    {{- if eq .Values.updateStrategy.type "RollingUpdate" }}
    rollingUpdate:
      partition: {{ .Values.updateStrategy.rollingUpdate.partition }}
    {{- end }}
  template:
    metadata:
      labels:
        {{- include "zookeeper.selectorLabels" . | nindent 8 }}
      annotations:
        {{- toYaml .Values.podAnnotations | nindent 8 }}
    spec:
      {{- with .Values.imagePullSecrets }}
      imagePullSecrets:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      serviceAccountName: {{ include "zookeeper.serviceAccountName" . }}
      securityContext:
        {{- toYaml .Values.podSecurityContext | nindent 8 }}
      terminationGracePeriodSeconds: {{ .Values.terminationGracePeriodSeconds }}
      {{- with .Values.priorityClassName }}
      priorityClassName: {{ . }}
      {{- end }}
      ##
      ## Volumes are declared here when persistence is disabled for that volume.
      ## When persistence is enabled, the volume comes from volumeClaimTemplates below.
      ##
      ## persistence.enabled is the master switch — when false both volumes use emptyDir
      ## regardless of data.enabled / log.enabled.
      {{- $needVolumesBlock := or (not $dataEnabled) (not $logEnabled) .Values.extraVolumes }}
      {{- if $needVolumesBlock }}
      volumes:
        {{- if not $dataEnabled }}
        - name: data
          emptyDir: {}
        {{- end }}
        {{- if not $logEnabled }}
        - name: log
          emptyDir: {}
        {{- end }}
        {{- with .Values.extraVolumes }}
        {{- toYaml . | nindent 8 }}
        {{- end }}
      {{- else }}
      {{- with .Values.extraVolumes }}
      volumes:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- end }}
      initContainers:
        - name: zookeeper-init
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag | default .Chart.AppVersion }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          command:
            - /bin/bash
            - -ec
            - |
              # Extract ordinal index from pod name (e.g. zookeeper-0 → myid=1)
              ORDINAL="${HOSTNAME##*-}"
              MY_ID=$((ORDINAL + 1))
              echo "Setting ZooKeeper myid to: ${MY_ID}"
              mkdir -p /data/data
              echo "${MY_ID}" > /data/data/myid
              echo "myid set to $(cat /data/data/myid)"
          volumeMounts:
            - name: data
              mountPath: /data
          securityContext:
            {{- toYaml .Values.securityContext | nindent 12 }}
      containers:
        - name: zookeeper
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag | default .Chart.AppVersion }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          securityContext:
            {{- toYaml .Values.securityContext | nindent 12 }}
          ports:
            - name: client
              containerPort: {{ .Values.zookeeper.clientPort }}
              protocol: TCP
            {{- if gt (int .Values.replicas) 1 }}
            - name: follower
              containerPort: {{ .Values.zookeeper.serverPort }}
              protocol: TCP
            - name: election
              containerPort: {{ .Values.zookeeper.leaderElectionPort }}
              protocol: TCP
            {{- end }}
            {{- if .Values.zookeeper.adminServer.enabled }}
            - name: admin
              containerPort: {{ .Values.zookeeper.adminServer.port }}
              protocol: TCP
            {{- end }}
          env:
            - name: ZOO_SERVERS
              value: {{ include "zookeeper.serverList" . | quote }}
            {{- range $key, $value := .Values.zookeeper.env }}
            - name: {{ $key }}
              value: {{ $value | quote }}
            {{- end }}
            - name: ZOO_DATA_DIR
              value: /data/data
            - name: ZOO_DATA_LOG_DIR
              value: /datalog
            ## Admin server — explicitly enable or disable based on values
            - name: ZOO_ADMINSERVER_ENABLED
              value: {{ .Values.zookeeper.adminServer.enabled | quote }}
            {{- if .Values.zookeeper.adminServer.enabled }}
            - name: ZOO_ADMIN_SERVER_PORT
              value: {{ .Values.zookeeper.adminServer.port | quote }}
            {{- end }}
          ##
          ## startupProbe runs first and gives ZooKeeper time to fully initialize
          ## before liveness/readiness probes take over. Prevents premature restarts
          ## on slow nodes or large datasets.
          ## Max startup time = failureThreshold * periodSeconds (default: 20 * 10 = 200s)
          ##
          {{- if .Values.startupProbe.enabled }}
          startupProbe:
            {{- if .Values.zookeeper.adminServer.enabled }}
            httpGet:
              path: /commands/ruok
              port: admin
            {{- else }}
            exec:
              command:
                - /bin/bash
                - -ec
                - |
                  OK=$(echo ruok | nc -w 2 localhost {{ .Values.zookeeper.clientPort }})
                  if [ "$OK" = "imok" ]; then exit 0; else exit 1; fi
            {{- end }}
            initialDelaySeconds: {{ .Values.startupProbe.initialDelaySeconds }}
            periodSeconds: {{ .Values.startupProbe.periodSeconds }}
            timeoutSeconds: {{ .Values.startupProbe.timeoutSeconds }}
            failureThreshold: {{ .Values.startupProbe.failureThreshold }}
            successThreshold: {{ .Values.startupProbe.successThreshold }}
          {{- end }}
          {{- if .Values.livenessProbe.enabled }}
          livenessProbe:
            {{- if .Values.zookeeper.adminServer.enabled }}
            ## Admin server enabled → use clean httpGet probe (no nc required)
            httpGet:
              path: /commands/ruok
              port: admin
            {{- else }}
            ## Admin server disabled → fall back to ruok via nc on client port
            exec:
              command:
                - /bin/bash
                - -ec
                - |
                  OK=$(echo ruok | nc -w 2 localhost {{ .Values.zookeeper.clientPort }})
                  if [ "$OK" = "imok" ]; then exit 0; else exit 1; fi
            {{- end }}
            initialDelaySeconds: {{ .Values.livenessProbe.initialDelaySeconds }}
            periodSeconds: {{ .Values.livenessProbe.periodSeconds }}
            timeoutSeconds: {{ .Values.livenessProbe.timeoutSeconds }}
            failureThreshold: {{ .Values.livenessProbe.failureThreshold }}
            successThreshold: {{ .Values.livenessProbe.successThreshold }}
          {{- end }}
          {{- if .Values.readinessProbe.enabled }}
          readinessProbe:
            {{- if .Values.zookeeper.adminServer.enabled }}
            ## Admin server enabled → use clean httpGet probe (no nc required)
            httpGet:
              path: /commands/ruok
              port: admin
            {{- else }}
            ## Admin server disabled → fall back to ruok via nc on client port
            exec:
              command:
                - /bin/bash
                - -ec
                - |
                  OK=$(echo ruok | nc -w 2 localhost {{ .Values.zookeeper.clientPort }})
                  if [ "$OK" = "imok" ]; then exit 0; else exit 1; fi
            {{- end }}
            initialDelaySeconds: {{ .Values.readinessProbe.initialDelaySeconds }}
            periodSeconds: {{ .Values.readinessProbe.periodSeconds }}
            timeoutSeconds: {{ .Values.readinessProbe.timeoutSeconds }}
            failureThreshold: {{ .Values.readinessProbe.failureThreshold }}
            successThreshold: {{ .Values.readinessProbe.successThreshold }}
          {{- end }}
          ##
          ## preStop hook: sleep before shutdown to allow the load balancer / service
          ## endpoints to be updated and in-flight client connections to drain gracefully.
          ## Without this, clients may get connection errors during rolling updates.
          ##
          lifecycle:
            preStop:
              exec:
                command:
                  - /bin/bash
                  - -ec
                  - sleep {{ .Values.lifecycle.preStopSleepSeconds }}
          resources:
            {{- toYaml .Values.resources | nindent 12 }}
          volumeMounts:
            - name: data
              mountPath: /data
            - name: log
              mountPath: /datalog
            {{- with .Values.extraVolumeMounts }}
            {{- toYaml . | nindent 12 }}
            {{- end }}
      {{- with .Values.nodeSelector }}
      nodeSelector:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      ##
      ## topologySpreadConstraints spreads pods evenly across nodes/zones.
      ## More reliable than podAntiAffinity preferred — this gives a hard guarantee
      ## that pods won't stack on the same node (maxSkew: 1).
      ## Falls back gracefully via whenUnsatisfiable: ScheduleAnyway if not enough nodes.
      ##
      {{- with .Values.topologySpreadConstraints }}
      topologySpreadConstraints:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- with .Values.affinity }}
      affinity:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- with .Values.tolerations }}
      tolerations:
        {{- toYaml . | nindent 8 }}
      {{- end }}
  ##
  ## Only create PVCs when persistence is enabled.
  ## When disabled, emptyDir volumes are declared above in the pod spec instead.
  ##
  {{- if or $dataEnabled $logEnabled }}
  volumeClaimTemplates:
    ##
    ## Data volume (ZooKeeper snapshots -> /data)
    ##
    {{- if $dataEnabled }}
    - metadata:
        name: data
        {{- with .Values.persistence.annotations }}
        annotations:
          {{- toYaml . | nindent 10 }}
        {{- end }}
      spec:
        volumeMode: {{ .Values.persistence.volumeMode | default "Filesystem" }}
        accessModes:
          {{- toYaml .Values.persistence.accessModes | nindent 10 }}
        {{- if .Values.persistence.storageClass }}
        storageClassName: {{ if eq "-" .Values.persistence.storageClass }}""{{ else }}{{ .Values.persistence.storageClass }}{{ end }}
        {{- end }}
        {{- if .Values.persistence.data.volumeName }}
        volumeName: {{ .Values.persistence.data.volumeName }}
        {{- end }}
        resources:
          requests:
            storage: {{ .Values.persistence.dataSize }}
    {{- end }}
    ##
    ## Log volume (ZooKeeper transaction logs -> /datalog)
    ##
    {{- if $logEnabled }}
    - metadata:
        name: log
        {{- with .Values.persistence.annotations }}
        annotations:
          {{- toYaml . | nindent 10 }}
        {{- end }}
      spec:
        volumeMode: {{ .Values.persistence.volumeMode | default "Filesystem" }}
        accessModes:
          {{- toYaml .Values.persistence.accessModes | nindent 10 }}
        {{- if .Values.persistence.storageClass }}
        storageClassName: {{ if eq "-" .Values.persistence.storageClass }}""{{ else }}{{ .Values.persistence.storageClass }}{{ end }}
        {{- end }}
        {{- if .Values.persistence.log.volumeName }}
        volumeName: {{ .Values.persistence.log.volumeName }}
        {{- end }}
        resources:
          requests:
            storage: {{ .Values.persistence.logSize }}
    {{- end }}
  {{- end }}
````

### ENTRY: helm-charts/charts/zookeeper/templates/_helpers.tpl

- bytes: 2463
- crc32: `d7cbe6a9`
- decoded_as: `utf-8`

````text
{{/*
Expand the name of the chart.
*/}}
{{- define "zookeeper.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
*/}}
{{- define "zookeeper.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create chart label.
*/}}
{{- define "zookeeper.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "zookeeper.labels" -}}
helm.sh/chart: {{ include "zookeeper.chart" . }}
{{ include "zookeeper.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "zookeeper.selectorLabels" -}}
app.kubernetes.io/name: {{ include "zookeeper.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Service account name
*/}}
{{- define "zookeeper.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{- default (include "zookeeper.fullname" .) .Values.serviceAccount.name }}
{{- else }}
{{- default "default" .Values.serviceAccount.name }}
{{- end }}
{{- end }}

{{/*
Headless service name
*/}}
{{- define "zookeeper.headlessServiceName" -}}
{{- printf "%s-headless" (include "zookeeper.fullname" .) }}
{{- end }}

{{/*
Generate ZooKeeper server list for ZOO_SERVERS env var
Format: server.1=<host>:2888:3888;2181 server.2=...
*/}}
{{- define "zookeeper.serverList" -}}
{{- $fullname := include "zookeeper.fullname" . -}}
{{- $headless := include "zookeeper.headlessServiceName" . -}}
{{- $replicas := int .Values.replicas -}}
{{- $serverPort := int .Values.zookeeper.serverPort -}}
{{- $electionPort := int .Values.zookeeper.leaderElectionPort -}}
{{- $clientPort := int .Values.zookeeper.clientPort -}}
{{- $servers := list -}}
{{- range $i := until $replicas -}}
{{- $servers = append $servers (printf "server.%d=%s-%d.%s:%d:%d;%d" (add $i 1) $fullname $i $headless $serverPort $electionPort $clientPort) -}}
{{- end -}}
{{- join " " $servers }}
{{- end }}

````

### ENTRY: helm-charts/charts/zookeeper/Chart.yaml

- bytes: 292
- crc32: `67c6ac2f`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: zookeeper
description: A Helm chart for Apache ZooKeeper using the official image
type: application
version: 0.1.5
appVersion: "3.9"
keywords:
  - zookeeper
  - coordination
  - distributed
sources:
  - https://hub.docker.com/_/zookeeper
  - https://zookeeper.apache.org

````

### ENTRY: helm-charts/charts/zookeeper/values.yaml

- bytes: 7044
- crc32: `fd22d2b9`
- decoded_as: `utf-8`

````yaml
# Default values for zookeeper chart

replicas: 1

image:
  repository: zookeeper
  pullPolicy: IfNotPresent
  # Overrides the image tag whose default is the chart appVersion
  tag: "3.9"

imagePullSecrets: []
nameOverride: ""
fullnameOverride: ""

## ZooKeeper configuration
## ref: https://zookeeper.apache.org/doc/current/zookeeperAdmin.html
zookeeper:
  ## Client port
  clientPort: 2181
  ## Peer/follower port
  serverPort: 2888
  ## Leader election port
  leaderElectionPort: 3888

  ## Admin HTTP server
  ## When enabled: exposes a REST API for diagnostics on adminServer.port
  ##   and probes will use httpGet against /commands/ruok (no nc required)
  ## When disabled: admin server is turned off and probes fall back to
  ##   the ruok 4-letter word via nc on the client port
  adminServer:
    enabled: true
    port: 8080

  ## ZooKeeper environment variables
  ## ref: https://hub.docker.com/_/zookeeper (Environment Variables section)
  env:
    ZOO_TICK_TIME: "2000"
    ZOO_INIT_LIMIT: "5"
    ZOO_SYNC_LIMIT: "2"
    ZOO_MAX_CLIENT_CNXNS: "60"
    ZOO_AUTOPURGE_PURGEINTERVAL: "1"
    ZOO_AUTOPURGE_SNAPRETAINCOUNT: "3"
    ZOO_4LW_COMMANDS_WHITELIST: "mntr,conf,ruok"
    # ZOO_LOG4J_PROP: "INFO,ROLLINGFILE"

## Service account
serviceAccount:
  create: true
  annotations: {}
  name: ""

## Pod annotations
podAnnotations: {}

## Pod security context
podSecurityContext:
  fsGroup: 1000
  runAsUser: 1000

## Container security context
securityContext:
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: false
  runAsNonRoot: true
  runAsUser: 1000

## Services
service:
  ## Client service (ClusterIP by default)
  client:
    type: ClusterIP
    port: 2181
    annotations: {}

  ## Headless service for StatefulSet DNS
  headless:
    annotations: {}

## Resources
resources:
  requests:
    cpu: 250m
    memory: 512Mi
  limits:
    cpu: 1
    memory: 1Gi

## Update strategy
## RollingUpdate: rolls pods one at a time (safe, default)
## OnDelete: only updates a pod when you manually delete it (full manual control)
updateStrategy:
  type: RollingUpdate
  rollingUpdate:
    ## partition: only pods with ordinal >= partition are updated.
    ## Useful for canary upgrades — e.g. set to 2 to only update pod-2 first.
    partition: 0

## Termination grace period in seconds.
## Should be long enough for ZooKeeper to finish serving in-flight requests
## and for preStop sleep to complete before SIGKILL is sent.
## Must be > lifecycle.preStopSleepSeconds
terminationGracePeriodSeconds: 60

## Priority class name — protects ZooKeeper pods from eviction under node pressure.
## Requires a PriorityClass resource to exist in the cluster.
## Example: priorityClassName: "high-priority"
priorityClassName: ""

## Lifecycle hooks
lifecycle:
  ## Seconds to sleep in preStop hook before shutdown.
  ## Gives the kube-proxy / load balancer time to remove the pod from
  ## service endpoints so in-flight client connections drain cleanly.
  ## Must be < terminationGracePeriodSeconds
  preStopSleepSeconds: 10

## Startup probe — runs before liveness/readiness, gives ZooKeeper time to initialize.
## Kubernetes will not start liveness/readiness until startupProbe succeeds.
## Max allowed startup time = failureThreshold * periodSeconds (default: 20 * 10s = 200s)
startupProbe:
  enabled: true
  initialDelaySeconds: 10
  periodSeconds: 10
  timeoutSeconds: 5
  failureThreshold: 20
  successThreshold: 1

## Liveness probe
livenessProbe:
  enabled: true
  initialDelaySeconds: 30
  periodSeconds: 10
  timeoutSeconds: 5
  failureThreshold: 6
  successThreshold: 1

## Readiness probe
readinessProbe:
  enabled: true
  initialDelaySeconds: 10
  periodSeconds: 10
  timeoutSeconds: 5
  failureThreshold: 6
  successThreshold: 1

## Persistent storage
## persistence.enabled is the master switch — false disables both volumes regardless
## of data.enabled / log.enabled. When true, data and log can be toggled independently.
persistence:
  ## Master switch — false forces emptyDir for both volumes (ephemeral, data lost on pod restart)
  enabled: false

  ## Volume mode: Filesystem (default) or Block
  volumeMode: Filesystem

  ## Storage class for dynamic provisioning.
  ## Use "" for cluster default, "-" to disable dynamic provisioning
  storageClass: ""

  accessModes:
    - ReadWriteOnce

  annotations: {}

  ## Data volume (ZooKeeper snapshots -> /data)
  data:
    ## Set to false to use emptyDir instead of a PVC for the data volume
    enabled: false
    ## volumeName: bind to a specific pre-provisioned PV by name.
    ## Leave empty to use dynamic provisioning via storageClass.
    volumeName: ""

  ## Log volume (ZooKeeper transaction logs -> /datalog)
  ## Keeping logs on a separate volume improves I/O isolation.
  log:
    ## Set to false to use emptyDir instead of a PVC for the log volume
    enabled: false
    ## volumeName: bind to a specific pre-provisioned PV by name.
    volumeName: ""

  ## Data volume size (ZooKeeper snapshots)
  dataSize: 8Gi

  ## Log volume size (ZooKeeper transaction logs)
  logSize: 4Gi

## Extra volumes to add to the pod spec.
## Useful for mounting ConfigMaps, Secrets, or hostPath directories into the container.
##
## Example — mount a custom log4j config from a ConfigMap:
##   extraVolumes:
##     - name: zookeeper-config
##       configMap:
##         name: my-zookeeper-config
##
## Example — mount a Secret:
##   extraVolumes:
##     - name: zookeeper-secret
##       secret:
##         secretName: my-zookeeper-secret
##
extraVolumes: []

## Extra volume mounts to add to the ZooKeeper container.
## Each entry must reference a volume name defined in extraVolumes above.
##
## Example — mount log4j.properties from a ConfigMap:
##   extraVolumeMounts:
##     - name: zookeeper-config
##       mountPath: /conf/log4j.properties
##       subPath: log4j.properties
##       readOnly: true
##
## Example — mount an entire directory:
##   extraVolumeMounts:
##     - name: zookeeper-config
##       mountPath: /conf
##       readOnly: true
##
extraVolumeMounts: []

## Node selector
nodeSelector: {}

## Tolerations
tolerations: []

## topologySpreadConstraints — spreads pods evenly across nodes/zones.
## More reliable than podAntiAffinity because it gives a hard guarantee (maxSkew: 1)
## that pods won't stack on the same node.
## whenUnsatisfiable: ScheduleAnyway falls back gracefully if not enough nodes exist
## (e.g. single-node dev cluster).
topologySpreadConstraints:
  - maxSkew: 1
    topologyKey: kubernetes.io/hostname
    whenUnsatisfiable: ScheduleAnyway
    labelSelector:
      matchLabels:
        app.kubernetes.io/name: zookeeper

## Affinity — optional, set if you need more advanced scheduling rules.
## topologySpreadConstraints above already handles node spreading.
affinity: {}

## Pod disruption budget
podDisruptionBudget:
  enabled: true
  minAvailable: 2

## Network policy
networkPolicy:
  enabled: false
  ## Ingress rules for ZooKeeper ports
  ingressRules: []
  ## Egress rules
  egressRules: []
````

### ENTRY: helm-charts/charts/cassandra/Chart.yaml

- bytes: 163
- crc32: `3d98db97`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: cassandra
description: A Helm chart for Apache Cassandra using the official Docker image
type: application
version: 0.1.5
appVersion: "5.0.5"

````

### ENTRY: helm-charts/charts/cassandra/values.yaml

- bytes: 6023
- crc32: `88666c84`
- decoded_as: `utf-8`

````yaml
## Enable/disable this chart
enabled: true

## Official Cassandra image
image:
  repository: cassandra
  tag: "5.0.5"
  pullPolicy: IfNotPresent

## Image pull secrets for private registries
imagePullSecrets: []
# - name: my-registry-secret

## Number of Cassandra nodes
replicaCount: 3

## How many of the first N pods are seed nodes
## Should be 1 for single node, 2+ for clusters
cluster:
  name: "cassandra"
  seedCount: 2
  domain: cluster.local
  ## Datacenter and rack — only used when endpointSnitch is GossipingPropertyFileSnitch
  dc: "dc1"
  rack: "rack1"
  ## Set to GossipingPropertyFileSnitch to enable dc/rack awareness
  endpointSnitch: "SimpleSnitch"

## Graceful shutdown period — must be longer than nodetool drain takes.
## nodetool drain typically completes within 60-90s, 180s gives safe margin.
terminationGracePeriodSeconds: 180

## Update strategy
updateStrategy:
  type: RollingUpdate

## Start all pods simultaneously instead of one by one
## Cassandra handles parallel startup gracefully via seed retry
podManagementPolicy: Parallel

## JVM heap settings
jvm:
  maxHeapSize: "12288M"
  extraOpts: "-Djava.rmi.server.hostname=localhost -Dcom.sun.management.jmxremote.port=7199 -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.local.only=false"

## Set to false to prevent new nodes from streaming data automatically on join.
## Useful for manual data migrations.
autoBootstrap: true

## Authentication
##
## Three independent knobs:
##   - authenticator: Cassandra authenticator class name (always set on the pod)
##   - authorizer:    Cassandra authorizer class name (always set on the pod)
##   - enabled:       When true, additionally injects CASSANDRA_USER and CASSANDRA_PASSWORD
##                    from the Secret. Set this to true when using PasswordAuthenticator.
##
## Common configurations:
##   No auth (default):
##     authenticator: AllowAllAuthenticator
##     authorizer:    AllowAllAuthorizer
##     enabled:       false
##
##   Password auth:
##     authenticator: PasswordAuthenticator
##     authorizer:    CassandraAuthorizer
##     enabled:       true
##
##   Custom authenticator (mTLS, plugin, etc.):
##     authenticator: <fully.qualified.ClassName>
##     authorizer:    <fully.qualified.ClassName>
##     enabled:       false   # set true only if your authenticator needs USER/PASSWORD env vars
##
auth:
  authenticator: AllowAllAuthenticator
  authorizer: AllowAllAuthorizer
  enabled: false
  username: cassandra
  ## Leave empty to auto-generate a random password on first install
  password: ""
  ## Name of existing Secret with key 'cassandra-password'
  ## If set, password field above is ignored
  existingSecret: ""

## Extra environment variables passed to the container.
## Do NOT set CASSANDRA_AUTHENTICATOR or CASSANDRA_AUTHORIZER here —
## use the auth.authenticator / auth.authorizer fields above instead.
extraEnvVars:
  - name: CASSANDRA_ENABLE_REMOTE_JMX
    value: "true"
  - name: MAX_DIRECT_MEMORY_SIZE
    value: "8G"

## Additional volumeMounts for the cassandra container.
## Pair each entry with a matching volume in extraVolumes below.
## Example — mount a JMX password file from a Secret:
#  extraVolumeMounts:
#    - name: jmx-password
#      mountPath: /etc/cassandra/jmxremote.password
#      subPath: jmxremote.password
#      readOnly: true
extraVolumeMounts: []

## Additional volumes for the cassandra pod.
## Pair each entry with a matching mount in extraVolumeMounts above.
## Example — load a JMX password from a pre-existing Secret:
#  extraVolumes:
#    - name: jmx-password
#      secret:
#        secretName: cassandra-jmx-credentials
#        defaultMode: 0400
extraVolumes: []

## Persistence
persistence:
  enabled: true
  storageClass: cassandra-local
  size: 10Gi
  accessModes:
    - ReadWriteOnce

## Service ports
service:
  cql: 9042
  intra: 7000
  tls: 7001
  jmx: 7199

## Resource limits
resources:
  requests:
    cpu: 1000m
    memory: 16Gi
  limits:
    cpu: 2000m
    memory: 24Gi

## Pod anti-affinity — hard prevents two Cassandra pods on the same node
podAntiAffinity: hard

## Priority class — prevents Cassandra pods from being evicted on resource-constrained nodes
priorityClassName: ""

## Timezone config — mounts a host timezone file into the container.
## If hostPath is empty, the volume is skipped and the pod uses the container default (UTC).
timezone:
  enabled: false
  hostPath: 

## Security context — disabled to run as root (required for some configurations)
## Security context — cassandra user UID/GID is 999 in the official image
containerSecurityContext:
  enabled: false
  runAsUser: 999
  runAsGroup: 999
  runAsNonRoot: true

## Startup probe — used instead of high initialDelaySeconds on liveness/readiness.
## Allows up to failureThreshold * periodSeconds for Cassandra to start.
startupProbe:
  enabled: true
  periodSeconds: 10
  failureThreshold: 60
  timeoutSeconds: 10

## Readiness probe
readinessProbe:
  enabled: true
  periodSeconds: 30
  timeoutSeconds: 10
  failureThreshold: 10

## Liveness probe
livenessProbe:
  enabled: true
  periodSeconds: 30
  timeoutSeconds: 10
  successThreshold: 1
  failureThreshold: 10

## NetworkPolicy — leave ports empty to allow all traffic by default
## Add port entries to restrict access to specific sources
networkPolicy:
  enabled: false
  ## Example:
  # ingress:
  #   - ports:
  #       - port: 9042
  #     from:
  #       - podSelector:
  #           matchLabels:
  #             app: twcloud

## PodDisruptionBudget — ensures at least 2 nodes stay up during maintenance
podDisruptionBudget:
  enabled: true
  minAvailable: 2

## Common labels applied to all resources
commonLabels:
  app: cassandra

## Additional pod labels
podLabels:
  app: cassandra

## Pod annotations — useful for Prometheus scraping, Vault injection, etc.
podAnnotations: {}

## ServiceAccount
serviceAccount:
  create: true
  name: ""
  annotations: {}
````

### ENTRY: helm-charts/charts/cassandra/.helmignore

- bytes: 349
- crc32: `2732ec16`
- decoded_as: `utf-8`

````text
# Patterns to ignore when building packages.
# This supports shell glob matching, relative path matching, and
# negation (prefixed with !). Only one pattern per line.
.DS_Store
# Common VCS dirs
.git/
.gitignore
.bzr/
.bzrignore
.hg/
.hgignore
.svn/
# Common backup files
*.swp
*.bak
*.tmp
*.orig
*~
# Various IDEs
.project
.idea/
*.tmproj
.vscode/

````

### ENTRY: helm-charts/charts/cassandra/templates/_helpers.tpl

- bytes: 1823
- crc32: `6dd7b870`
- decoded_as: `utf-8`

````text
{{/*
Expand the name of the chart.
*/}}
{{- define "cassandra.name" -}}
{{- .Chart.Name }}
{{- end }}

{{/*
Full name: release-chart
*/}}
{{- define "cassandra.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name }}
{{- end }}

{{/*
Headless service name
*/}}
{{- define "cassandra.headlessServiceName" -}}
{{- printf "%s-%s-headless" .Release.Name .Chart.Name }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "cassandra.labels" -}}
helm.sh/chart: {{ .Chart.Name }}-{{ .Chart.Version }}
app.kubernetes.io/name: {{ include "cassandra.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "cassandra.selectorLabels" -}}
app.kubernetes.io/name: {{ include "cassandra.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
ServiceAccount name
*/}}
{{- define "cassandra.serviceAccountName" -}}
{{- if .Values.serviceAccount.name }}
{{- .Values.serviceAccount.name }}
{{- else }}
{{- include "cassandra.fullname" . }}
{{- end }}
{{- end }}

{{/*
Build comma-separated seed list from the first .Values.cluster.seedCount pods.
Example result: webapp-cassandra-0.webapp-cassandra-headless.wap.svc.cluster.local,webapp-cassandra-1.webapp-cassandra-headless.wap.svc.cluster.local
*/}}
{{- define "cassandra.seeds" -}}
{{- $seeds := list -}}
{{- $fullname := include "cassandra.fullname" . -}}
{{- $headless := include "cassandra.headlessServiceName" . -}}
{{- $ns := .Release.Namespace -}}
{{- $domain := .Values.cluster.domain -}}
{{- range $i, $e := until (int .Values.cluster.seedCount) -}}
  {{- $seeds = append $seeds (printf "%s-%d.%s.%s.svc.%s" $fullname $i $headless $ns $domain) -}}
{{- end -}}
{{- join "," $seeds -}}
{{- end }}

````

### ENTRY: helm-charts/charts/cassandra/templates/service.yaml

- bytes: 1693
- crc32: `5f0aab3c`
- decoded_as: `utf-8`

````yaml
{{- if .Values.enabled }}
## ClusterIP service — used by TWCloud to connect on CQL port 9042
apiVersion: v1
kind: Service
metadata:
  name: {{ include "cassandra.fullname" . }}
  labels:
    {{- include "cassandra.labels" . | nindent 4 }}
    {{- with .Values.commonLabels }}
    {{- toYaml . | nindent 4 }}
    {{- end }}
spec:
  type: ClusterIP
  ports:
    - name: cql
      port: {{ .Values.service.cql }}
      targetPort: cql
      protocol: TCP
    - name: intra
      port: {{ .Values.service.intra }}
      targetPort: intra
      protocol: TCP
    - name: tls
      port: {{ .Values.service.tls }}
      targetPort: tls
      protocol: TCP
    - name: jmx
      port: {{ .Values.service.jmx }}
      targetPort: jmx
      protocol: TCP
  selector:
    {{- include "cassandra.selectorLabels" . | nindent 4 }}
---
## Headless service — used for pod DNS resolution and seed discovery
apiVersion: v1
kind: Service
metadata:
  name: {{ include "cassandra.headlessServiceName" . }}
  labels:
    {{- include "cassandra.labels" . | nindent 4 }}
    {{- with .Values.commonLabels }}
    {{- toYaml . | nindent 4 }}
    {{- end }}
spec:
  type: ClusterIP
  clusterIP: None
  publishNotReadyAddresses: true
  ports:
    - name: cql
      port: {{ .Values.service.cql }}
      targetPort: cql
      protocol: TCP
    - name: intra
      port: {{ .Values.service.intra }}
      targetPort: intra
      protocol: TCP
    - name: tls
      port: {{ .Values.service.tls }}
      targetPort: tls
      protocol: TCP
    - name: jmx
      port: {{ .Values.service.jmx }}
      targetPort: jmx
      protocol: TCP
  selector:
    {{- include "cassandra.selectorLabels" . | nindent 4 }}
{{- end }}

````

### ENTRY: helm-charts/charts/cassandra/templates/statefulset.yaml

- bytes: 10915
- crc32: `9b12d84c`
- decoded_as: `utf-8`

````yaml
{{- if .Values.enabled }}
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: {{ include "cassandra.fullname" . }}
  labels:
    {{- include "cassandra.labels" . | nindent 4 }}
    {{- with .Values.commonLabels }}
    {{- toYaml . | nindent 4 }}
    {{- end }}
spec:
  serviceName: {{ include "cassandra.headlessServiceName" . }}
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      {{- include "cassandra.selectorLabels" . | nindent 6 }}
  podManagementPolicy: {{ .Values.podManagementPolicy }}
  updateStrategy:
    type: {{ .Values.updateStrategy.type }}
  template:
    metadata:
      labels:
        {{- include "cassandra.selectorLabels" . | nindent 8 }}
        {{- with .Values.podLabels }}
        {{- toYaml . | nindent 8 }}
        {{- end }}
      annotations:
        {{- with .Values.podAnnotations }}
        {{- toYaml . | nindent 8 }}
        {{- end }}
        ## Auto-computed checksum — triggers pod restart when cassandra config files change
        checksum/cassandra-config: {{ $.Files.Glob "configs/cassandra/*" | toYaml | sha256sum | quote }}
    spec:
      serviceAccountName: {{ include "cassandra.serviceAccountName" . }}
      {{- with .Values.imagePullSecrets }}
      imagePullSecrets:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- if .Values.priorityClassName }}
      priorityClassName: {{ .Values.priorityClassName | quote }}
      {{- end }}
      ##
      ## Anti-affinity — prevents two Cassandra pods landing on the same node
      ##
      {{- if eq .Values.podAntiAffinity "hard" }}
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            - labelSelector:
                matchLabels:
                  {{- include "cassandra.selectorLabels" . | nindent 18 }}
              topologyKey: kubernetes.io/hostname
      {{- else if eq .Values.podAntiAffinity "soft" }}
      affinity:
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 1
              podAffinityTerm:
                labelSelector:
                  matchLabels:
                    {{- include "cassandra.selectorLabels" . | nindent 20 }}
                topologyKey: kubernetes.io/hostname
      {{- end }}
      ##
      ## Security context
      ##
      {{- if .Values.containerSecurityContext.enabled }}
      securityContext:
        runAsUser: {{ .Values.containerSecurityContext.runAsUser }}
        runAsGroup: {{ .Values.containerSecurityContext.runAsGroup }}
        runAsNonRoot: {{ .Values.containerSecurityContext.runAsNonRoot }}
      {{- end }}
      terminationGracePeriodSeconds: {{ .Values.terminationGracePeriodSeconds }}
      initContainers:
        - name: copy-configs
          image: busybox:1.28
          command:
            - sh
            - -c
            - |
              cp /config-ro/cassandra.yaml /config-rw/cassandra.yaml
              cp /config-ro/logback.xml /config-rw/logback.xml
          volumeMounts:
            - name: config-volume
              mountPath: /config-ro
            - name: config-writable
              mountPath: /config-rw
      containers:
        - name: cassandra
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          lifecycle:
            preStop:
              exec:
                ## Drain the node before shutdown — flushes memtables and hands off hints
                command:
                  - /bin/bash
                  - -c
                  - nodetool drain
          ports:
            - name: cql
              containerPort: {{ .Values.service.cql }}
              protocol: TCP
            - name: intra
              containerPort: {{ .Values.service.intra }}
              protocol: TCP
            - name: tls
              containerPort: {{ .Values.service.tls }}
              protocol: TCP
            - name: jmx
              containerPort: {{ .Values.service.jmx }}
              protocol: TCP
          env:
            ##
            ## Seed nodes — built from the first .cluster.seedCount pod DNS names
            ##
            - name: CASSANDRA_SEEDS
              value: {{ include "cassandra.seeds" . | quote }}
            ##
            ## Pod IP — used by Cassandra for listen_address and broadcast_rpc_address
            ##
            - name: POD_IP
              valueFrom:
                fieldRef:
                  fieldPath: status.podIP
            ##
            ## Cluster name
            ##
            - name: CASSANDRA_CLUSTER_NAME
              value: {{ .Values.cluster.name | quote }}
            - name: CASSANDRA_ENDPOINT_SNITCH
              value: {{ .Values.cluster.endpointSnitch | quote }}
            {{- if eq .Values.cluster.endpointSnitch "GossipingPropertyFileSnitch" }}
            - name: CASSANDRA_DC
              value: {{ .Values.cluster.dc | quote }}
            - name: CASSANDRA_RACK
              value: {{ .Values.cluster.rack | quote }}
            {{- end }}
            ##
            ## Auto bootstrap — set to false for manual data migrations
            ##
            - name: CASSANDRA_AUTO_BOOTSTRAP
              value: {{ .Values.autoBootstrap | quote }}
            ##
            ## JVM heap settings
            ##
            - name: MAX_HEAP_SIZE
              value: {{ .Values.jvm.maxHeapSize | quote }}
            - name: JVM_EXTRA_OPTS
              value: {{ .Values.jvm.extraOpts | quote }}
            ##
            ## Authentication — authenticator and authorizer are always set explicitly.
            ## Defaults (AllowAll*) disable auth. Set auth.enabled=true and switch the
            ## class names to PasswordAuthenticator/CassandraAuthorizer to enable auth.
            ## See values.yaml for details and custom-authenticator usage.
            ##
            - name: CASSANDRA_AUTHENTICATOR
              value: {{ .Values.auth.authenticator | quote }}
            - name: CASSANDRA_AUTHORIZER
              value: {{ .Values.auth.authorizer | quote }}
            {{- if .Values.auth.enabled }}
            - name: CASSANDRA_USER
              value: {{ .Values.auth.username | quote }}
            - name: CASSANDRA_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: {{ .Values.auth.existingSecret | default (printf "%s-cassandra-auth" .Release.Name) }}
                  key: cassandra-password
            {{- end }}
            ##
            ## Extra user-defined env vars (CASSANDRA_ENABLE_REMOTE_JMX, MAX_DIRECT_MEMORY_SIZE, etc.)
            ##
            {{- with .Values.extraEnvVars }}
            {{- toYaml . | nindent 12 }}
            {{- end }}
          volumeMounts:
            {{- if .Values.persistence.enabled }}
            - name: data
              mountPath: /var/lib/cassandra
            {{- else }}
            - name: cassandra-data-emptydir
              mountPath: /var/lib/cassandra
            {{- end }}
            - name: config-writable
              mountPath: /etc/cassandra/cassandra.yaml
              subPath: cassandra.yaml
            - name: config-writable
              mountPath: /etc/cassandra/logback.xml
              subPath: logback.xml
            {{- if and .Values.timezone.enabled .Values.timezone.hostPath }}
            - name: tz-config
              mountPath: /etc/localtime
            {{- end }}
            ##
            ## User-defined additional mounts — pair with extraVolumes below.
            ## Use to mount additional config files, secrets, or volumes into /etc/cassandra/
            ## or anywhere else in the container. See values.yaml for example syntax.
            ##
            {{- with .Values.extraVolumeMounts }}
            {{- toYaml . | nindent 12 }}
            {{- end }}
          {{- with .Values.resources }}
          resources:
            {{- toYaml . | nindent 12 }}
          {{- end }}
          ##
          ## Readiness probe
          ##
          {{- if .Values.readinessProbe.enabled }}
          readinessProbe:
            exec:
              command:
                - /bin/bash
                - -c
                - nodetool status | grep -E "^UN\s+$(hostname -i)"
            periodSeconds: {{ .Values.readinessProbe.periodSeconds }}
            timeoutSeconds: {{ .Values.readinessProbe.timeoutSeconds }}
            failureThreshold: {{ .Values.readinessProbe.failureThreshold }}
          {{- end }}
          ##
          ## Liveness probe
          ##
          {{- if .Values.livenessProbe.enabled }}
          livenessProbe:
            exec:
              command:
                - /bin/bash
                - -c
                - nodetool status
            periodSeconds: {{ .Values.livenessProbe.periodSeconds }}
            timeoutSeconds: {{ .Values.livenessProbe.timeoutSeconds }}
            successThreshold: {{ .Values.livenessProbe.successThreshold }}
            failureThreshold: {{ .Values.livenessProbe.failureThreshold }}
          {{- end }}
          ##
          ## Startup probe — gives Cassandra time to start before liveness kicks in
          ##
          {{- if .Values.startupProbe.enabled }}
          startupProbe:
            tcpSocket:
              port: {{ .Values.service.cql }}
            periodSeconds: {{ .Values.startupProbe.periodSeconds }}
            failureThreshold: {{ .Values.startupProbe.failureThreshold }}
            timeoutSeconds: {{ .Values.startupProbe.timeoutSeconds }}
          {{- end }}
      volumes:
        {{- if not .Values.persistence.enabled }}
        ## Named distinctly from "data" to avoid matching existing PVCs
        ## (StatefulSet auto-binds PVCs named data-<pod-name> if they exist)
        - name: cassandra-data-emptydir
          emptyDir: {}
        {{- end }}
        - name: config-volume
          configMap:
            name: {{ .Release.Name }}-cassandra-cm
        - name: config-writable
          emptyDir: {}
        {{- if and .Values.timezone.enabled .Values.timezone.hostPath }}
        - name: tz-config
          hostPath:
            path: {{ .Values.timezone.hostPath }}
            type: File
        {{- end }}
        ##
        ## User-defined additional volumes — pair with extraVolumeMounts above.
        ## See values.yaml for example syntax.
        ##
        {{- with .Values.extraVolumes }}
        {{- toYaml . | nindent 8 }}
        {{- end }}
  ##
  ## PVC template — creates a PVC per pod for Cassandra data
  ##
  {{- if .Values.persistence.enabled }}
  volumeClaimTemplates:
    - metadata:
        name: data
      spec:
        accessModes:
          {{- toYaml .Values.persistence.accessModes | nindent 10 }}
        storageClassName: {{ .Values.persistence.storageClass }}
        resources:
          requests:
            storage: {{ .Values.persistence.size }}
  {{- end }}
{{- end }}
````

### ENTRY: helm-charts/charts/cassandra/templates/configmap-seeds.yaml

- bytes: 846
- crc32: `806005cb`
- decoded_as: `utf-8`

````yaml
{{- if .Values.enabled }}
## Pre-computed seed addresses for consumption by TWCloud.
## Replaces the dynamic kubectl-based init container approach.
## Variables CASSANDRA_SEED0..N are read by TWCloud's application.conf.
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-cassandra-seeds
  labels:
    {{- include "cassandra.labels" . | nindent 4 }}
    {{- with .Values.commonLabels }}
    {{- toYaml . | nindent 4 }}
    {{- end }}
data:
  {{- $fullname := include "cassandra.fullname" . }}
  {{- $headless := include "cassandra.headlessServiceName" . }}
  {{- $ns := .Release.Namespace }}
  {{- $domain := .Values.cluster.domain }}
  {{- range $i, $e := until (int .Values.cluster.seedCount) }}
  CASSANDRA_SEED{{ $i }}: {{ printf "%s-%d.%s.%s.svc.%s:9042" $fullname $i $headless $ns $domain | quote }}
  {{- end }}
{{- end }}
````

### ENTRY: helm-charts/charts/cassandra/templates/poddisruptionbudget.yaml

- bytes: 485
- crc32: `066e9fe5`
- decoded_as: `utf-8`

````yaml
{{- if and .Values.enabled .Values.podDisruptionBudget.enabled }}
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: {{ include "cassandra.fullname" . }}
  labels:
    {{- include "cassandra.labels" . | nindent 4 }}
    {{- with .Values.commonLabels }}
    {{- toYaml . | nindent 4 }}
    {{- end }}
spec:
  minAvailable: {{ .Values.podDisruptionBudget.minAvailable }}
  selector:
    matchLabels:
      {{- include "cassandra.selectorLabels" . | nindent 6 }}
{{- end }}
````

### ENTRY: helm-charts/charts/cassandra/templates/networkpolicy.yaml

- bytes: 678
- crc32: `03b7236b`
- decoded_as: `utf-8`

````yaml
{{- if and .Values.enabled .Values.networkPolicy.enabled }}
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: {{ include "cassandra.fullname" . }}
  labels:
    {{- include "cassandra.labels" . | nindent 4 }}
    {{- with .Values.commonLabels }}
    {{- toYaml . | nindent 4 }}
    {{- end }}
spec:
  podSelector:
    matchLabels:
      {{- include "cassandra.selectorLabels" . | nindent 6 }}
  policyTypes:
    - Ingress
  {{- if .Values.networkPolicy.ingress }}
  ingress:
    {{- toYaml .Values.networkPolicy.ingress | nindent 4 }}
  {{- else }}
  ## No ingress rules defined — all inbound traffic is allowed
  ingress:
    - {}
  {{- end }}
{{- end }}
````

### ENTRY: helm-charts/charts/cassandra/templates/serviceAccount.yaml

- bytes: 426
- crc32: `b30ec91b`
- decoded_as: `utf-8`

````yaml
{{- if and .Values.enabled .Values.serviceAccount.create }}
apiVersion: v1
kind: ServiceAccount
metadata:
  name: {{ include "cassandra.serviceAccountName" . }}
  labels:
    {{- include "cassandra.labels" . | nindent 4 }}
    {{- with .Values.commonLabels }}
    {{- toYaml . | nindent 4 }}
    {{- end }}
  {{- with .Values.serviceAccount.annotations }}
  annotations:
    {{- toYaml . | nindent 4 }}
  {{- end }}
{{- end }}
````

### ENTRY: helm-charts/charts/cassandra/templates/secret.yaml

- bytes: 854
- crc32: `1823b741`
- decoded_as: `utf-8`

````yaml
{{- if and .Values.enabled .Values.auth.enabled (not .Values.auth.existingSecret) }}
{{- $secretName := printf "%s-cassandra-auth" .Release.Name }}
{{- $existingSecret := lookup "v1" "Secret" .Release.Namespace $secretName }}
{{- $password := "" }}
{{- if $existingSecret }}
  {{- $password = index $existingSecret.data "cassandra-password" | b64dec }}
{{- else if .Values.auth.password }}
  {{- $password = .Values.auth.password }}
{{- else }}
  {{- $password = randAlphaNum 16 }}
{{- end }}
apiVersion: v1
kind: Secret
metadata:
  name: {{ $secretName }}
  labels:
    {{- include "cassandra.labels" . | nindent 4 }}
    {{- with .Values.commonLabels }}
    {{- toYaml . | nindent 4 }}
    {{- end }}
type: Opaque
data:
  cassandra-password: {{ $password | b64enc | quote }}
  cassandra-username: {{ .Values.auth.username | b64enc | quote }}
{{- end }}
````

### ENTRY: helm-charts/charts/cassandra/templates/NOTES.txt

- bytes: 1007
- crc32: `085ca420`
- decoded_as: `utf-8`

````text
Apache Cassandra is starting up.

Release:   {{ .Release.Name }}
Namespace: {{ .Release.Namespace }}
Cluster:   {{ .Values.cluster.name }}
Replicas:  {{ .Values.replicaCount }}
Image:     {{ .Values.image.repository }}:{{ .Values.image.tag }}

## Check cluster status
kubectl exec -n {{ .Release.Namespace }} {{ include "cassandra.fullname" . }}-0 -- nodetool status

## Connect with cqlsh
{{- if .Values.auth.enabled }}
kubectl exec -n {{ .Release.Namespace }} {{ include "cassandra.fullname" . }}-0 -- \
  cqlsh -u {{ .Values.auth.username }} -p <password-from-secret>

## Get the generated password
kubectl get secret -n {{ .Release.Namespace }} {{ .Release.Name }}-cassandra-auth \
  -o jsonpath='{.data.cassandra-password}' | base64 -d
{{- else }}
kubectl exec -n {{ .Release.Namespace }} {{ include "cassandra.fullname" . }}-0 -- cqlsh
{{- end }}

## Watch pod startup
kubectl get pods -n {{ .Release.Namespace }} -l app.kubernetes.io/name=cassandra -w

## Seed nodes
{{ include "cassandra.seeds" . }}
````

### ENTRY: helm-charts/crd/metalLB/l2advertisement.yaml

- bytes: 146
- crc32: `375ca82b`
- decoded_as: `utf-8`

````yaml
apiVersion: metallb.io/v1beta1
kind: L2Advertisement
metadata:
  name: example
  namespace: metallb-system
spec:
  ipAddressPools:
  - first-pool

````

### ENTRY: helm-charts/crd/metalLB/metallb_ipaddresspool.yaml

- bytes: 207
- crc32: `3bc4b977`
- decoded_as: `utf-8`

````yaml
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: first-pool
  namespace: metallb-system
spec:
  addresses:
  #- 192.168.1.1/24
  #- 192.168.9.1-192.168.9.5
  #- fc00:f853:0ccd:e799::/124

````

### ENTRY: helm-charts/templates/_deployment.tpl

- bytes: 5148
- crc32: `67908f78`
- decoded_as: `utf-8`

````text
{{ define "main-template.deployment" }}
apiVersion: apps/v1
kind: Deployment
metadata:
#  name: {{ include "main-template.fullname" . }}
  name: {{ .Release.Name }}-{{ .Chart.Name }}
  labels:
    {{- include "main-template.labels" . | nindent 4 }}
    date: "{{ now | unixEpoch }}"
spec:
  replicas: {{ .Values.replicas | default 1 }}
  selector:
    matchLabels:
      {{- include "main-template.selectorLabels" . | trim | nindent 6 }}
  template:
    metadata:
      annotations:
        {{- with .Values.podAnnotations }}
        {{- toYaml . | nindent 8 }}
        {{- end }}
        ## Auto-computed checksums — trigger pod restart when config files change
        checksum/wap-config: {{ $.Files.Glob "configs/wap/*" | toYaml | sha256sum | quote }}
        checksum/tomcat-config: {{ $.Files.Glob "configs/tomcat/*" | toYaml | sha256sum | quote }}
        {{- if or (eq .Values.ident "auth") }}
        checksum/auth-config: {{ $.Files.Glob "configs/auth/*" | toYaml | sha256sum | quote }}
        {{- end }}
      labels:
        {{- include "main-template.selectorLabels" . | trim | nindent 8 }}
    spec:      
      {{- with .Values.imagePullSecrets }}
      imagePullSecrets:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      serviceAccountName: {{ .Release.Name }}-tcas
      containers:
        - name: {{ .Chart.Name }}
          {{- if or (eq .Values.ident "wap") (eq .Values.ident "auth") }}
          image: "{{ .Values.global.repoURL }}{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          imagePullPolicy: {{ .Values.global.pullPolicy }}
          volumeMounts:
          - name: config-volume
            mountPath: /usr/local/tomcat/shared/conf/revision.txt
            subPath: revision.txt
            readOnly: true
          - name: config-volume
            mountPath: /usr/local/tomcat/shared/conf/webappplatform.properties
            subPath: webappplatform.properties
            readOnly: true
          - name: config-volume
            mountPath: /usr/local/tomcat/shared/conf/log4j2.properties
            subPath: log4j2.properties
            readOnly: true
          - name: config-volume
            mountPath: /usr/local/tomcat/shared/conf/authserver.properties
            subPath: authserver.properties
            readOnly: true
          - name: config-volume
            mountPath: /usr/local/tomcat/conf/server.xml
            subPath: server.xml
            readOnly: true
          - name: config-volume
            mountPath: /usr/local/tomcat/conf/catalina.properties
            subPath: catalina.properties
            readOnly: true
          - name: certs
            mountPath: /usr/local/tomcat/shared/conf/keystore.p12
            subPath: keystore.p12
            readOnly: true
          - name: certs
            mountPath: /usr/local/tomcat/shared/conf/teamworkcloud.crt
            subPath: teamworkcloud.crt
            readOnly: true
          {{ else }}
          image: "{{ .Values.global.dockerHub }}{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          imagePullPolicy: {{ .Values.global.pullPolicy }}
          {{- end }}
          {{- if or (eq .Values.ident "wap") (eq .Values.ident "auth") }}
          env:
            - name: WEBAPP_PROPERTIES
              value: {{ tpl .Values.env.value . | quote }}
          ports:
            - name: {{ include "main-template.name" . }}
              containerPort: {{ .Values.service.port }}
              protocol: TCP
          {{- else if .Values.containers.ports }}
          ports:
            {{- range .Values.containers.ports }}
            - containerPort: {{ .containerPort }}
            {{- end }}
          {{- end }}
      {{- if .Values.global.twcBuiltIn }}
      {{- include "main-template.init-container" . }}
      {{- end }}
      volumes:
        - name: certs
          secret:
            secretName: {{ .Release.Name }}-certificates
        {{- if (eq .Values.global.licenseDslsServerMode "CUSTOM") }}
        - name: dsls-cm
          configMap:
            name: {{ .Release.Name }}-dsls-cm
        {{- end }}
        - name: config-volume
          projected:
            sources:
            - configMap:
              # Provide the name of the ConfigMap containing the files you want
              # to add to the container
                name: {{ .Release.Name }}-wap-cm
            {{- if eq .Values.ident "auth" }}
            - configMap:
              # Provide the name of the ConfigMap containing the files you want
              # to add to the container
                name: {{ .Release.Name }}-auth-cm
            {{- end }}
            - configMap:
              # Provide the name of the ConfigMap containing the files you want
              # to add to the container
                name: {{ .Release.Name }}-tomcat-cm
      {{- with .Values.nodeSelector }}
      nodeSelector:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- with .Values.affinity }}
      affinity:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- with .Values.tolerations }}
      tolerations:
        {{- toYaml . | nindent 8 }}
      {{- end }}
{{- end }}
````

### ENTRY: helm-charts/templates/_namespace.tpl

- bytes: 103
- crc32: `f34abb81`
- decoded_as: `utf-8`

````text
{{ define "main-template.namespace" }}
apiVersion: v1
kind: Namespace
metadata:
  name: dev
{{- end }}

````

### ENTRY: helm-charts/templates/_service.tpl

- bytes: 602
- crc32: `bb78abd5`
- decoded_as: `utf-8`

````text
{{ define "main-template.service" }}
apiVersion: v1
kind: Service
metadata:
#  name: {{ include "main-template.fullname" . }}
  name: {{ .Release.Name }}-{{ .Chart.Name }}
  labels:
    {{- include "main-template.labels" . | nindent 4 }}
spec:
  {{- if or .Values.ident "wap" .Values.ident "auth" }}
  type: {{ .Values.service.type }}
  ports:
    - name: {{ include "main-template.name" . }}
      port: {{ .Values.service.port }}
      targetPort: {{ .Values.service.targetPort }}
      protocol: TCP
  selector:
    {{- include "main-template.selectorLabels" . | nindent 4 }}
  {{- end }}
{{- end }}
````

### ENTRY: helm-charts/templates/configmap.yaml

- bytes: 1390
- crc32: `87b69b5a`
- decoded_as: `utf-8`

````yaml
{{- if or .Values.adminconsole.enabled .Values.collaborator.enabled .Values.docexporter.enabled .Values.oslc.enabled 
.Values.reports.enabled .Values.resources.enabled .Values.rum.enabled .Values.simulation.enabled .Values.webapp.enabled }}
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-wap-cm
data:
{{ (.Files.Glob "configs/wap/*").AsConfig | indent 4 }}
{{- end }}
---
{{- if or .Values.authentication.enabled }}
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-auth-cm
data:
{{ (.Files.Glob "configs/auth/*").AsConfig | indent 4 }}
{{- end }}
---
{{- if or .Values.adminconsole.enabled .Values.collaborator.enabled .Values.docexporter.enabled .Values.oslc.enabled 
.Values.reports.enabled .Values.resources.enabled .Values.rum.enabled .Values.simulation.enabled .Values.webapp.enabled }}
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-tomcat-cm
data:
{{ (.Files.Glob "configs/tomcat/*").AsConfig | indent 4 }}
{{- end }}
---
{{- if or .Values.twcloud.enabled }}
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-twcloud-cm
data:
{{ (.Files.Glob "configs/twcloud/*").AsConfig | indent 4 }}
{{- end }}
---
{{- if or .Values.cassandra.enabled }}
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-cassandra-cm
data:
{{ (.Files.Glob "configs/cassandra/*").AsConfig | indent 4 }}
{{- end }}
````

### ENTRY: helm-charts/templates/pv.yaml

- bytes: 1670
- crc32: `de212ca2`
- decoded_as: `utf-8`

````yaml
{{- /*
  Creates one PV per node per volume group defined in persistentVolumes.volumes[].
  Sub-charts create their own PVCs independently via their own persistence.enabled flag.

  PV naming convention: <volume.name>-<host>
    e.g. zookeeper-data-pv-nm-k8sw1.dsone.3ds.com

  To enable persistence for a sub-chart:
    1. Set persistentVolumes.volumes[<name>].enabled: true  (creates PVs here)
    2. Set <subchart>.persistence.enabled: true             (creates PVCs in sub-chart)
    Both must be true for persistence to work with local static storage.
*/ -}}
{{- if .Values.persistentVolumes.enabled }}
{{- range .Values.persistentVolumes.volumes }}
{{- if .enabled }}
{{- $volume := . }}
{{- range $index, $node := $volume.nodes }}
---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: {{ $volume.name }}-{{ $node.host }}
  labels:
    app.kubernetes.io/managed-by: {{ $.Release.Service }}
    volume-group: {{ $volume.name }}
    node: {{ $node.host }}
spec:
  capacity:
    storage: {{ $volume.storage }}
  volumeMode: {{ $.Values.persistentVolumes.volumeMode }}
  accessModes:
    - {{ $.Values.persistentVolumes.accessModes }}
  persistentVolumeReclaimPolicy: {{ $.Values.persistentVolumes.persistentVolumeReclaimPolicy }}
  storageClassName: {{ $volume.storageClassName }}
  local:
    path: {{ $volume.localPath }}
  nodeAffinity:
    required:
      nodeSelectorTerms:
        - matchExpressions:
            - key: {{ $.Values.persistentVolumes.matchExpressionsKey }}
              operator: {{ $.Values.persistentVolumes.matchExpressionsOperator }}
              values:
                - {{ $node.host }}
{{- end }}
{{- end }}
{{- end }}
{{- end }}
````

### ENTRY: helm-charts/templates/rbac.yaml

- bytes: 1826
- crc32: `931222c5`
- decoded_as: `utf-8`

````yaml
---
apiVersion: v1
kind: ServiceAccount
metadata:
  # annotations:
  #   kubernetes.io/enforce-mountable-secrets: "true"
  name: {{ .Release.Name }}-tcas
  namespace: {{ .Release.Namespace }}
automountServiceAccountToken: true
secrets:
- name: {{ .Release.Name }}-certificates
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: {{ .Release.Name }}-tcas-pod-reader
  namespace: {{ .Release.Namespace }}
rules:
- apiGroups:
  - ""
  resources:
  - pods
  - secrets
  - endpoints
  verbs:
  - get
  - list
  - watch
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: {{ .Release.Name }}-tcas-configmap
  namespace: {{ .Release.Namespace }}
rules:
- apiGroups:
  - ""
  resources:
  - configmaps
  verbs:
  - create
  - update
  - get
  - patch
  - delete
  - get
  - list
  - watch
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: {{ .Release.Name }}-tcas-binding
  namespace: {{ .Release.Namespace }}
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: {{ .Release.Name }}-tcas-pod-reader
subjects:
- kind: ServiceAccount
  name: {{ .Release.Name }}-tcas
  namespace: {{ .Release.Namespace }}
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: {{ .Release.Name }}-tcas-configmap-binding
  namespace: {{ .Release.Namespace }}
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: {{ .Release.Name }}-tcas-configmap
subjects:
- kind: ServiceAccount
  name: {{ .Release.Name }}-tcas
  namespace: {{ .Release.Namespace }}
---
apiVersion: v1
kind: Secret
metadata:
  name: {{ .Release.Name }}-tcas-secret
  namespace: {{ .Release.Namespace }}
  annotations:
    kubernetes.io/service-account.name: {{ .Release.Name }}-tcas
  labels:
    component: tcas 
type: kubernetes.io/service-account-token
````

### ENTRY: helm-charts/templates/required.yaml

- bytes: 590
- crc32: `deb5ccdc`
- decoded_as: `utf-8`

````yaml
{{- $_ := required "**** .Values.global.repoURL is a required value ****" .Values.global.repoURL }}
{{- $_ := required "**** .Values.global.twcAdminUsername is a required value ****" .Values.global.twcAdminUsername }}
{{- $_ := required "**** .Values.global.twcAdminPassword is a required value ****" .Values.global.twcAdminPassword }}
{{- $_ := required "**** .Values.global.authenticationServerProtocol is a required value ****" .Values.global.authenticationServerProtocol }}
{{- $_ := required "**** .Values.global.licenseServer is a required value ****" .Values.global.licenseServer }}

````

### ENTRY: helm-charts/templates/storageClass.yaml

- bytes: 621
- crc32: `e29a5e42`
- decoded_as: `utf-8`

````yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
  name: cassandra-local
provisioner: kubernetes.io/no-provisioner
volumeBindingMode: WaitForFirstConsumer
---
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: zookeeper-local
provisioner: kubernetes.io/no-provisioner
## Same WaitForFirstConsumer binding mode as cassandra-local.
## Without this, the PVC binds immediately to any available PV regardless
## of which node the pod gets scheduled on, causing the pod to be stuck pending.
volumeBindingMode: WaitForFirstConsumer
````

### ENTRY: helm-charts/templates/tls.yaml

- bytes: 633
- crc32: `9508dccd`
- decoded_as: `utf-8`

````yaml
{{- if or .Values.twcloud.enabled .Values.adminconsole.enabled .Values.collaborator.enabled .Values.docexporter.enabled 
.Values.oslc.enabled .Values.reports.enabled .Values.resources.enabled .Values.rum.enabled .Values.simulation.enabled 
.Values.webapp.enabled }}
apiVersion: v1
kind: Secret
metadata:
  name: {{ .Release.Name }}-certificates
type: Opaque
data:
{{ (.Files.Glob "configs/twcloud/ssl/*").AsSecrets | indent 2 }}
{{- end }}
---
{{- if .Values.ingress.enabled -}}
apiVersion: v1
kind: Secret
metadata:
  name: tls-secret
type: kubernetes.io/tls
data:
{{ (.Files.Glob "configs/ssl/*").AsSecrets | indent 2 }}
{{- end }}
````

### ENTRY: helm-charts/templates/NOTES.txt

- bytes: 3081
- crc32: `d22911ef`
- decoded_as: `utf-8`

````text
Thank you for installing Teamwork cloud and services.
Your release is named {{ .Release.Name }}.

CHART NAME: {{ .Chart.Name }}
CHART VERSION: {{ .Chart.Version }}
APP VERSION: {{ .Chart.AppVersion }}

To learn more about the release, try:
-------------------------------------
  $ helm status {{ .Release.Name }} -n {{ .Release.Namespace }}
  $ helm get all {{ .Release.Name }} -n {{ .Release.Namespace }}
-------------------------------------
Deployed applications and services:
-------------------------------------
{{- if .Values.twcloud.enabled }}
Teamwork cloud server - Replicas: {{ .Values.twcloud.replicas }}
{{- end }}
{{- if .Values.cassandra.enabled }}
Cassandra DB - Replicas: {{ .Values.cassandra.replicas }}
{{- end }}
{{- if .Values.adminconsole.enabled }}
Admin console application - Replicas: {{ .Values.adminconsole.replicas }}
{{- end }}
{{- if .Values.artemis.enabled }}
Active MQ artemis server
{{- end }}
{{- if .Values.authentication.enabled }}
Authentication application - Replicas: {{ .Values.authentication.replicas }}
{{- end }}
{{- if .Values.collaborator.enabled }}
Collaborator application - Replicas: {{ .Values.collaborator.replicas }}
{{- end }}
{{- if .Values.docexporter.enabled }}
Document exporter application - Replicas: {{ .Values.docexporter.replicas }}
{{- end }}
{{- if .Values.oslc.enabled }}
Oslc application - Replicas: {{ .Values.oslc.replicas }}
{{- end }}
{{- if .Values.reports.enabled }}
Reports application - Replicas: {{ .Values.reports.replicas }}
{{- end }}
{{- if .Values.resources.enabled }}
Resources application - Replicas: {{ .Values.resources.replicas }}
{{- end }}
{{- if .Values.rum.enabled }}
Resource-usage-map application - Replicas: {{ .Values.rum.replicas }}
{{- end }}
{{- if .Values.simulation.enabled }}
Simulation application - Replicas: {{ .Values.simulation.replicas }}
{{- end }}
{{- if .Values.magiclab.enabled }}
Magic-lab application - Replicas: {{ .Values.magiclab.replicas }}
{{- end }}
{{- if .Values.magiclabcollab.enabled }}
Magic-lab-collaborator application - Replicas: {{ .Values.magiclabcollab.replicas }}
{{- end }}
{{- if .Values.webapp.enabled }}
Webapp application - Replicas: {{ .Values.webapp.replicas }}
{{- end }}
{{- if .Values.sysml2api.enabled }}
Sysml2api application - Replicas: {{ .Values.sysml2api.replicas }}
{{- end }}
{{- if .Values.sgicrawler.enabled }}
Sgicrawler application - Replicas: {{ .Values.sgicrawler.replicas }}
{{- end }}
{{- if .Values.elementchooser.enabled }}
Element chooser application - Replicas: {{ .Values.elementchooser.replicas }}
{{- end }}
{{- if .Values.zookeeper.enabled }}
Zookeeper server
{{- end }}
-------------------------------------

{{ if .Values.ingress.enabled }}
haproxy-ingress is enabled.
-------------------------------------
{{- range .Values.ingress.controller.hosts }}
url exposed by LoadBalancer: https://{{.host}}/webapp{{- end }}
{{- if .Values.ingress.tcp }}
{{ range .Values.ingress.controller.hosts }}
Twcloud TCP Ports exposed through nginx
url: {{.host}}{{- end }}
{{- end }}
-------------------------------------
{{- end }}
````

### ENTRY: helm-charts/templates/_helpers.tpl

- bytes: 4524
- crc32: `2b6ec827`
- decoded_as: `utf-8`

````text
{{/*
Expand the name of the chart.
*/}}
{{- define "main-template.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Release name.
*/}}
{{- define "main-release.name" -}}
{{- default .Release.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{/*
{{- define "main-template.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if eq $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}
*/}}
{{- define "main-template.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "main-template.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "main-template.labels" -}}
helm.sh/chart: {{ include "main-template.chart" . }}
{{ include "main-template.selectorLabels" . }}
{{- if .Chart.AppVersion -}}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Init Containers
*/}}

{{- define "main-template.init-container" }}
      initContainers:
        {{- if eq .Values.ident "wap" }}
        - name: init-twcloud
          image: busybox:1.28          
          command: ['sh', '-c', "until nc -vz {{ .Release.Name }}-twcloud.$(cat /var/run/secrets/kubernetes.io/serviceaccount/namespace).svc.cluster.local 8111; do echo waiting for {{ include "main-template.fullname" . }}-service; sleep 2; done"]
        {{- else }}
        - name: init-twcloud
          image: busybox:1.28          
          command: ['sh', '-c', "until nc -vz {{ .Release.Name }}-cassandra.$(cat /var/run/secrets/kubernetes.io/serviceaccount/namespace).svc.cluster.local 9042; do echo waiting for {{ include "main-template.fullname" . }}-service; sleep 2; done"]
        - name: init-twcloud-configmap
          image: bitnamilegacy/kubectl:1.33.4-debian-12-r0
          command: ['bash', '-c', "kubectl get -n {{ .Release.Namespace }} configmap {{ .Release.Name }}-cassandra-seeds >/dev/null 2>&1 && kubectl delete -n {{ .Release.Namespace }} configmap {{ .Release.Name }}-cassandra-seeds; seeds=$(kubectl get pod {{ .Release.Name }}-cassandra-0 -o jsonpath='{.spec.containers[0].env[?(@.name==\"CASSANDRA_SEEDS\")].value}' | awk -F, '{for(i=1;i<=NF;i++) printf \"%s:9042%s\", $i, (i==NF ? ORS : FS)}'); IFS=','; read -ra entries <<< \"$seeds\"; for ((i=0; i<${#entries[@]}; i++)); do varname=\"CASSANDRA_SEED$i\"; declare \"$varname\"=\"${entries[$i]}\"; echo \"$varname=${!varname}\"; done >/tmp/seeds; kubectl create -n {{ .Release.Namespace }} configmap {{ .Release.Name }}-cassandra-seeds --from-env-file=/tmp/seeds"]
        {{- end }}
{{- end -}}

{{/*
Returns the concatenated content of all cassandra config files.
Called from the cassandra subchart to compute a restart-triggering hash.
*/}}
{{- define "main-template.cassandraConfigChecksum" -}}
{{- range $path, $bytes := .Files.Glob "configs/cassandra/*" -}}
{{- $path }}:
{{ $bytes | toString }}
{{ end }}
{{- end -}}

{{/*
Selector labels
*/}}
{{- define "main-template.selectorLabels" -}}
app: {{ include "main-template.name" . }}
project: {{ include "main-template.name" . }}
{{/* app.kubernetes.io/name: {{ include "main-template.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }} */}}
{{- end -}}

{{/*
Java system properties
*/}}

{{- define "java-system-props" -}}
{{ join "," .Values.java.system.props }}
{{- end -}}

{{/*
Create the name of the service account to use

{{- define "main-template.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{- default (include "main-template.fullname" .) .Values.serviceAccount.name }}
{{- else }}
{{- default "default" .Values.serviceAccount.name }}
{{- end }}
{{- end }}
*/}}
````

### ENTRY: helm-charts/templates/_initcontainer.tpl

- bytes: 768
- crc32: `ac291952`
- decoded_as: `utf-8`

````text
{{ define "main-initcontainer" }}
{{ if .Values.twcloud.enabled }}
      initContainers:
      - name: init-twcloud
        image: busybox:1.28
        command: ['sh', '-c', "until nslookup {{ include "main-template.fullname" . }}-service.$(cat /var/run/secrets/kubernetes.io/serviceaccount/namespace).svc.cluster.local; do echo waiting for {{ include "main-template.fullname" . }}-service; sleep 2; done"]
      - name: init-twcloud-configmap
        image: bitnamilegacy/kubectl:1.33.4-debian-12-r0
        command: ['sh', '-c', 'kubectl create cm webapp-cassandra-seeds --from-literal CASSANDRA_SEEDS=$(kubectl get pod webapp-cassandra-0 -o json | jq '.spec.containers[0].env[] | select(.name == "CASSANDRA_SEEDS").value' | tr -d '"')']
      {{- end }}
{{- end  }}
````

### ENTRY: helm-charts/templates/_job.tpl

- bytes: 6283
- crc32: `8d7d3b6d`
- decoded_as: `utf-8`

````text
{{ define "main-template.job" }}
apiVersion: keda.sh/v1alpha1
kind: ScaledJob
metadata:
  name: {{ include "main-template.fullname" . }}-job
  labels:
    {{- include "main-template.labels" . | nindent 4 }}
spec:
  scalingStrategy:
    strategy: "accurate"
    pendingPodConditions:
      - "Ready"
  maxreplicas: {{ .Values.maxreplicas | default 50 }}
  pollingInterval: {{ .Values.pollingInterval | default 1 }}
  jobTargetRef:
    completions: 1
    template:
      metadata:
        annotations:
          checksum/wap-config: {{ $.Files.Glob "configs/wap/*" | toYaml | sha256sum | quote }}
          checksum/tomcat-config: {{ $.Files.Glob "configs/tomcat/*" | toYaml | sha256sum | quote }}
        labels:
          jobgroup: {{ .Values.appLabel }}
      spec:
        containers:
          - name: {{ .Chart.Name }}
            image: "{{ .Values.global.repoURL }}{{ .Values.image.repository }}:{{ .Values.image.tag }}"
            imagePullPolicy: {{ .Values.global.pullPolicy }}
            volumeMounts:
              - name: config-volume
                mountPath: /usr/local/tomcat/shared/conf/revision.txt
                subPath: revision.txt
                readOnly: true
              - name: config-volume
                mountPath: /usr/local/tomcat/shared/conf/webappplatform.properties
                subPath: webappplatform.properties
                readOnly: true
              - name: config-volume
                mountPath: /usr/local/tomcat/shared/conf/log4j2.properties
                subPath: log4j2.properties
                readOnly: true
              - name: config-volume
                mountPath: /usr/local/tomcat/shared/conf/authserver.properties
                subPath: authserver.properties
                readOnly: true
              - name: config-volume
                mountPath: /usr/local/tomcat/conf/server.xml
                subPath: server.xml
                readOnly: true
              - name: config-volume
                mountPath: /usr/local/tomcat/conf/catalina.properties
                subPath: catalina.properties
                readOnly: true
              - name: certs
                mountPath: /usr/local/tomcat/shared/conf/keystore.p12
                subPath: keystore.p12
                readOnly: true
              - name: certs
                mountPath: /usr/local/tomcat/shared/conf/teamworkcloud.crt
                subPath: teamworkcloud.crt
                readOnly: true
            startupProbe:
                httpGet:
                  scheme: {{ .Values.startupProbe.httpGet.scheme }}
                  path: /simulation/api/ready
                  port: {{ .Values.startupProbe.httpGet.port }}
                failureThreshold: 120
                periodSeconds: 5
            env:
              - name: WEBAPP_PROPERTIES
                value: "-Dsim.shutdown.on.empty.run.queue=true
                        -Denvironment=cloud
                        -Dservice.internal.protocol=https
                        -Dservice.internal.name={{ include "main-template.fullname" . }}
                        -Dservice.internal.port=8443
                        -Dtwc.ip={{ .Release.Name }}-twcloud
                        -Dtwc.admin.username={{ .Values.global.twcAdminUsername }}
                        -Dtwc.admin.password={{ .Values.global.twcAdminPassword }}
                        -Dtwc.rest.port={{ .Values.global.twcRestPort }}
                        -Dtwc.client.port={{ .Values.global.twcClientPort }}
                        -Dzookeeper.server.ip={{ .Release.Name }}-zookeeper
                        -Dzookeeper.server.port={{ .Values.global.zookeeperServerPort }}
                        -Dservice.url={{ .Values.global.serviceUrl }}
                        -Dauthentication.server.ip={{ .Values.global.authenticationServerIp }}
                        -Dauthentication.server.port={{ .Values.global.authenticationServerPort }}
                        -Dauthentication.server.protocol={{ .Values.global.authenticationServerProtocol }}
                        -Dauthentication.client.secret={{ .Values.global.authenticationClientSecret }}
                        -Dmessaging.server.ip={{ .Release.Name }}-artemis.{{ .Release.Namespace }}.svc.cluster.local
                        -Dmessaging.server.port={{ .Values.global.messagingServerPort }}
                        -Dmessaging.server.security.enabled={{ .Values.global.messagingServerSecurityEnabled }}
                        -Dmessaging.user.name={{ .Values.global.activeMqUserName }}
                        -Dmessaging.user.password={{ .Values.global.activeMqPassword }}
                        -Dmessage.server.persistence.enabled=true"
            ports:
              - name: {{ include "main-template.name" . }}
                containerPort: {{ .Values.service.port }}
                protocol: TCP
        volumes:
          - name: certs
            secret:
              secretName: {{ .Release.Name }}-certificates
          {{- if (eq .Values.global.licenseDslsServerMode "CUSTOM") }}
          - name: dsls-cm    
            configMap:
              name: {{ .Release.Name }}-dsls-cm
          {{- end }}
          - name: config-volume
            projected:
              sources:
              - configMap:
                # Provide the name of the ConfigMap containing the files you want
                # to add to the container
                  name: {{ .Release.Name }}-wap-cm
              - configMap:
                # Provide the name of the ConfigMap containing the files you want
                # to add to the container
                  name: {{ .Release.Name }}-auth-cm
              - configMap:
                # Provide the name of the ConfigMap containing the files you want
                # to add to the container
                  name: {{ .Release.Name }}-tomcat-cm
  triggers:
    - type: artemis-queue
      metadata:
        managementEndpoint: "{{ .Release.Name }}-artemis.{{ .Release.Namespace }}.svc.cluster.local:8161"
        queueName: "jms!/sim!/QueueRun"
        brokerName: "0.0.0.0"
        brokerAddress: "jms!/sim!/QueueRun"
        username: {{ .Values.global.activeMqUserName }}
        password: {{ .Values.global.activeMqPassword }}
        queueLength: '1'
{{- end }}
````

### ENTRY: helm-charts/templates/ingress-resource.yaml

- bytes: 6353
- crc32: `b02777dc`
- decoded_as: `utf-8`

````yaml
{{- if .Values.ingress.enabled -}}
{{- $fullName := include "main-template.fullname" . -}}
{{- if and .Values.ingress.controller.className (not (semverCompare ">=1.18-0" .Capabilities.KubeVersion.GitVersion)) }}
  {{- if not (hasKey .Values.ingress.controller.annotations "kubernetes.io/ingress.class") }}
  {{- $_ := set .Values.ingress.controller.annotations "kubernetes.io/ingress.class" .Values.ingress.controller.className}}
  {{- end }}
{{- end }}
{{- if semverCompare ">=1.19-0" .Capabilities.KubeVersion.GitVersion -}}
apiVersion: networking.k8s.io/v1
{{- else if semverCompare ">=1.14-0" .Capabilities.KubeVersion.GitVersion -}}
apiVersion: networking.k8s.io/v1beta1
{{- else -}}
apiVersion: extensions/v1beta1
{{- end }}
kind: Ingress
metadata:
  name: {{ $fullName }}-ingress
  labels:
    {{- include "main-template.labels" . | nindent 4 }}
  {{- with .Values.ingress.controller.annotations }}
  annotations:
    {{- toYaml . | nindent 4 }}
  {{- end }}
spec:
  {{- if and .Values.ingress.controller.className (semverCompare ">=1.18-0" .Capabilities.KubeVersion.GitVersion) }}
  ingressClassName: haproxy
  {{- end }}
  {{- if .Values.ingress.controller.defaultTLSSecret.enabled }}
  tls:
    {{- range .Values.ingress.controller.hosts }}
    - hosts:
        - {{ .host | quote }}
      secretName: {{ $.Values.ingress.controller.defaultTLSSecret.secret | default "tls-secret" }}
    {{- end }}
  {{- end }}
  rules:
  {{- range .Values.ingress.controller.hosts }}
  - host: {{ .host | quote }}
    http:
      paths:
        {{- if $.Values.adminconsole.enabled }}
        - path: /admin
          pathType: Prefix
          backend:
            service:
              name: {{ $.Release.Name }}-{{ $.Values.adminconsole.appLabel | replace "-" "" }}
              port:
                number: {{ $.Values.adminconsole.service.port }}
        {{- end }}
        {{- if $.Values.authentication.enabled }}
        - path: /authentication
          pathType: Prefix
          backend:
            service:
              name: {{ $.Release.Name }}-{{ $.Values.authentication.appLabel }}
              port:
                number: {{ $.Values.authentication.service.port }}
        {{- end }}
        {{- if $.Values.collaborator.enabled }}
        - path: /collaborator
          pathType: Prefix
          backend:
            service:
              name: {{ $.Release.Name }}-{{ $.Values.collaborator.appLabel }}
              port:
                number: {{ $.Values.collaborator.service.port }}
        {{- end }}
        {{- if $.Values.docexporter.enabled }}
        - path: /document-exporter
          pathType: Prefix
          backend:
            service:
              name: {{ $.Release.Name }}-{{ $.Values.docexporter.appLabel }}
              port:
                number: {{ $.Values.docexporter.service.port }}
        {{- end }}
        {{- if $.Values.elementchooser.enabled }}
        - path: /element-chooser
          pathType: Prefix
          backend:
            service:
              name: {{ $.Release.Name }}-{{ $.Values.elementchooser.appLabel }}
              port:
                number: {{ $.Values.elementchooser.service.port }}
        {{- end }}
        {{- if $.Values.oslc.enabled }}
        - path: /oslc
          pathType: Prefix
          backend:
            service:
              name: {{ $.Release.Name }}-{{ $.Values.oslc.appLabel }}
              port:
                number: {{ $.Values.oslc.service.port }}
        {{- end }}
        {{- if $.Values.reports.enabled }}
        - path: /reports
          pathType: Prefix
          backend:
            service:
              name: {{ $.Release.Name }}-{{ $.Values.reports.appLabel }}
              port:
                number: {{ $.Values.reports.service.port }}
        {{- end }}
        {{- if $.Values.resources.enabled }}
        - path: /resources
          pathType: Prefix
          backend:
            service:
              name: {{ $.Release.Name }}-{{ $.Values.resources.appLabel }}
              port:
                number: {{ $.Values.resources.service.port }}
        {{- end }}
        {{- if $.Values.rum.enabled }}
        - path: /resource-usage-map
          pathType: Prefix
          backend:
            service:
              name: {{ $.Release.Name }}-{{ $.Values.rum.appLabel }}
              port:
                number: {{ $.Values.rum.service.port }}
        {{- end }}
        {{- if $.Values.magiclab.enabled }}
        - path: /magiclab
          pathType: Prefix
          backend:
            service:
              name: {{ $.Release.Name }}-{{ $.Values.magiclab.appLabel }}
              port:
                number: {{ $.Values.magiclab.service.port }}
        {{- end }}
        {{- if $.Values.magiclabcollab.enabled }}
        - path: /magiclab-collaborator
          pathType: Prefix
          backend:
            service:
              name: {{ $.Release.Name }}-{{ $.Values.magiclabcollab.appLabel }}
              port:
                number: {{ $.Values.magiclabcollab.service.port }}
        {{- end }}
        {{- if $.Values.simulation.enabled }}
        - path: /simulation
          pathType: Prefix
          backend:
            service:
              name: {{ $.Release.Name }}-{{ $.Values.simulation.appLabel }}
              port:
                number: {{ $.Values.simulation.service.port }}
        {{- end }}
        {{- if $.Values.webapp.enabled }}
        - path: /webapp
          pathType: Prefix
          backend:
            service:
              name: {{ $.Release.Name }}-{{ $.Values.webapp.appLabel }}
              port:
                number: {{ $.Values.webapp.service.port }}
        {{- end }}
        {{- if $.Values.sysml2api.enabled }}
        - path: /sysmlv2-api
          pathType: Prefix
          backend:
            service:
              name: {{ $.Release.Name }}-{{ $.Values.sysml2api.appLabel }}
              port:
                number: {{ $.Values.sysml2api.service.port }}
        {{- end }}
        {{- if $.Values.sgicrawler.enabled }}
        - path: /sgi-crawler
          pathType: Prefix
          backend:
            service:
              name: {{ $.Release.Name }}-{{ $.Values.sgicrawler.appLabel }}
              port:
                number: {{ $.Values.sgicrawler.service.port }}
        {{- end }}
  {{- end }}
{{- end }}
````

### ENTRY: helm-charts/templates/tcp-services.yaml

- bytes: 1966
- crc32: `4e6af14b`
- decoded_as: `utf-8`

````yaml
{{- if and .Values.ingress.enabled .Values.twcloud.enabled }}
## HAProxy TCP CRD — exposes TWCloud raw TCP ports through the ingress controller.
## These ports bypass HTTP/HTTPS routing and are proxied directly at TCP level.
##
## Requires the TCP CRD (tcps.ingress.v3.haproxy.org) to be installed.
## The haproxytech kubernetes-ingress chart installs this automatically via a
## post-install Helm hook job — but that runs AFTER manifests are validated,
## so on the very first install the CRD must be pre-applied with kubectl.
## See chart README for the bootstrap step.
##
## Since haproxy-ingress v3.1 the ingress.class annotation is mandatory.
## In v3, `binds` is a map keyed by bind name (not an array as in v1).
---
apiVersion: ingress.v3.haproxy.org/v3
kind: TCP
metadata:
  name: {{ .Release.Name }}-twcloud-client-api
  namespace: {{ .Release.Namespace }}
  annotations:
    ingress.class: haproxy
spec:
  - name: twcloud-client-api
    frontend:
      name: twcloud-client-api
      binds:
        bind-3579:
          name: bind-3579
          port: 3579
    service:
      name: {{ .Release.Name }}-twcloud
      port: 3579
---
apiVersion: ingress.v3.haproxy.org/v3
kind: TCP
metadata:
  name: {{ .Release.Name }}-twcloud-rest-api
  namespace: {{ .Release.Namespace }}
  annotations:
    ingress.class: haproxy
spec:
  - name: twcloud-rest-api
    frontend:
      name: twcloud-rest-api
      binds:
        bind-8111:
          name: bind-8111
          port: 8111
    service:
      name: {{ .Release.Name }}-twcloud
      port: 8111
---
apiVersion: ingress.v3.haproxy.org/v3
kind: TCP
metadata:
  name: {{ .Release.Name }}-twcloud-admin
  namespace: {{ .Release.Namespace }}
  annotations:
    ingress.class: haproxy
spec:
  - name: twcloud-admin
    frontend:
      name: twcloud-admin
      binds:
        bind-2468:
          name: bind-2468
          port: 2468
    service:
      name: {{ .Release.Name }}-twcloud
      port: 2468
{{- end }}
````

### ENTRY: helm-charts/Chart.yaml

- bytes: 1598
- crc32: `a9bb4aca`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: tcas
description: A Helm chart to deploy Teamwork cloud and services

type: application

version: 0.1.5

appVersion: "2026xRefresh1"

dependencies:
- name: kubernetes-ingress
  version: 1.49.0
  repository: https://haproxytech.github.io/helm-charts
  alias: ingress
  condition: ingress.enabled

- name: zookeeper
  version: 0.1.5
  condition: zookeeper.enabled

- name: cassandra
  version: 0.1.5  
  condition: cassandra.enabled

- name: twcloud
  version: 0.1.5
  condition: twcloud.enabled

- name: adminconsole
  version: 0.1.5
  condition: adminconsole.enabled

- name: authentication
  version: 0.1.5
  condition: authentication.enabled

- name: artemis
  version: 0.1.5
  condition: artemis.enabled

- name: collaborator
  version: 0.1.5
  condition: collaborator.enabled

- name: docexporter
  version: 0.1.5
  condition: docexporter.enabled

- name: oslc
  version: 0.1.5
  condition: oslc.enabled

- name: reports
  version: 0.1.5
  condition: reports.enabled

- name: resources
  version: 0.1.5
  condition: resources.enabled

- name: rum
  version: 0.1.5
  condition: rum.enabled

- name: magiclab
  version: 0.1.5
  condition: magiclab.enabled

- name: magiclabcollab
  version: 0.1.5
  condition: magiclabcollab.enabled

- name: simulation
  version: 0.1.5
  condition: simulation.enabled

- name: webapp
  version: 0.1.5
  condition: webapp.enabled

- name: sysml2api
  version: 0.1.5
  condition: sysml2api.enabled

- name: sgicrawler
  version: 0.1.5
  condition: sgicrawler.enabled

- name: elementchooser
  version: 0.1.5
  condition: elementchooser.enabled
````

### ENTRY: helm-charts/values.yaml

- bytes: 20262
- crc32: `a63ede11`
- decoded_as: `utf-8`

````yaml
# Global values for all applications and sevices
global:
  #Allow to use bitnami legacy images.
  security:
    allowInsecureImages: true
  # Specify the image repository url (should end with /).
  # MANDATORY !
  # repoURL: admin.example.com:5000/
  repoURL: 

  # Docker hub repository for 
  dockerHub: registry.hub.docker.com/

  # Specify the image pull policy
  pullPolicy: Always

  # Defines that TWC will be deployed by this helm chart
  # Do not change.
  twcBuiltIn: true

  # Specify the Teamwork Cloud rest API port (Default: 8111).
  twcRestPort: 8111

  # Specify the Teamwork Cloud client API port (Default: 3579).
  twcClientPort: 3579

  # Specify the Teamwork Cloud administrator user name (Default: Administrator).
  # MANDATORY !
  twcAdminUsername: Administrator

  # Specify the Teamwork Cloud administrator password (Default: Administrator).
  # MANDATORY !
  twcAdminPassword: Administrator

  # Specify the url to access WebAppPlatform
  # MANDATORY !
  # serviceUri: https://ingress.example.com/
  serviceUrl: 

  # Specify the Authentication server ip address or domain name.
  # Ingress external ip or domain name bind to external ip.
  # MANDATORY !
  # authenticationServerIp: ingress.example.com
  authenticationServerIp: 
  
  # Specify the Authentication server port (depends on your ingress configuration. Default: 443).
  authenticationServerPort: 443

  # Specify rest protocol (http or https) depending on the Authentication server setup (Default: https).
  authenticationServerProtocol: https

  # Optional value.
  # Specify the authentication client password that platform will use to secure communication with the Authentication server.
  # (Default: CHANGE_ME)
  authenticationClientSecret: CHANGE_ME

  # Specify the Zookeeper server IP address or service name (Default: {{ .Release.Name }}-zookeeper ).
  zookeeperServerIp: "{{ .Release.Name }}-zookeeper"
  
  # Specify the Zookeeper server port (Default: 2181 ).
  zookeeperServerPort: 2181

  # Specify the FlexNet licence server IP address (licensing server).
  # MANDATORY !
  # licenseServerName: example.com:port
  licenseServer: 

  # Specify the license framework FlexNet or DSLS.
  # MANDATORY !
  # licenseFramework: FlexNet
  licenseFramework: FlexNet

  # If license framework is DSLS then you should enabel this property (default is CUSTOM).
  #licenseDslsServerMode: CUSTOM

  # messagingServerIp is Apache ActiveMQ Artemis service ip or service name (Default: {{ .Release.Name }}-artemis ).
  # messagingServerIp: {{ .Release.Name }}-artemis

  # messagingServerPort is Apache ActiveMQ Artemis service port (Default: 61616)
  messagingServerPort: 61616

  # messagingServerSecurityEnabled defines whether users that can communicate with message server are
  # restricted. If set to true, a user for communication needs to be set as shown in the commented
  # line that follows the setting.
  messagingServerSecurityEnabled: true

  # Specify username for ActiveMQ Artemis service (Default: artemis)
  # MANDATORY !
  activeMqUserName: artemis

  # Specify password for ActiveMQ Artemis service (Default: artemis)
  # MANDATORY !
  activeMqPassword: artemis

  # ignoreWapTwcCompatibility is to enable/disable twcloud version compatibility
  # checking (for testing purpose ONLY)
  # ignoreWapTwcCompatibility: true

  # docexporterFileStoring specifies how long (in minutes) generated PDF/HTML files will be stored
  # in the Task Manager.
  docexporterFileStoring: 1440

  # Zookeeper cassandra path
  cassandraContactPointsZookeeperPath: /cassandra/seeds

# Applications and Services settings

##### TeamworkCloud and components #####

cassandra:
  enabled: true
  image:
    repository: cassandra
    tag: "5.0.5"
  commonLabels: {app: cassandra}
  podLabels: {app: cassandra}
  volumePermissions:
    enabled: false
  persistence:
    enabled: false
    storageClass: cassandra-local
    size: 20Gi
    accessModes:
      - ReadWriteOnce
  containerSecurityContext:
    enabled: false
    runAsUser: 999
    runAsGroup: 999
    runAsNonRoot: true

  ## Startup probe — used instead of high initialDelaySeconds on liveness/readiness.
  ## Allows up to failureThreshold * periodSeconds for Cassandra to start.
  startupProbe:
    enabled: true
    periodSeconds: 10
    failureThreshold: 60
    timeoutSeconds: 10

  ## Readiness probe
  readinessProbe:
    enabled: true
    periodSeconds: 30
    timeoutSeconds: 10
    failureThreshold: 10

  ## Liveness probe
  livenessProbe:
    enabled: true
    periodSeconds: 30
    timeoutSeconds: 10
    successThreshold: 1
    failureThreshold: 10
  # cluster.seedCount sets how many cassandra nodes will have info about cassandra.
  # If you run single cassandra, value should be 1, if you run cassandra cluster 
  # value shoud be 2 or more depending on your needs.
  cluster:
    seedCount: 2
  # ReplicaCount should match with twcloud
  replicaCount: 3
  
  updateStrategy:
    type: RollingUpdate

  ## OrderedReady ensures pods restart one at a time during upgrades.
  ## Each pod must pass readiness probe before the next one restarts,
  ## preventing gossip failures when multiple nodes restart simultaneously.
  podManagementPolicy: OrderedReady

  # Intra Port on the Host and Container (Default: 7000)
  # containerPorts.intra: 7000

  # Intra Port on the Host (Default: 7000)
  # hostPorts.intra: 7000
  # JVM properties
  jvm:
    maxHeapSize: "12288m"
    newHeapSize: "800m"
    extraOpts: "-Djava.rmi.server.hostname=localhost -Dcom.sun.management.jmxremote.port=7199 -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.local.only=false"
  # Extra environment variables
  extraEnvVars:
    - name: CASSANDRA_ENABLE_REMOTE_JMX
      value: "true"
    - name: MAX_DIRECT_MEMORY_SIZE
      value: "8G"  
  # Resource limits
  resources:
    requests:
      cpu: 1000m
      memory: 16Gi
    limits:
      cpu: 2000m
      memory: 24Gi
  # Pod anti-affinity preset. Ignored if affinity is set. Allowed values: soft or hard
  podAntiAffinityPreset: hard

# Persistent Volumes used by Cassandra and Zookeeper

## =============================================================================
## Persistent Volumes
## =============================================================================
## Controls PV *creation* sub-charts from a single place.
##
## HOW IT WORKS:
##   This section only creates PersistentVolume (PV) resources.
##   Each Cassandra and Zookeeper sub-chart controls its own PersistentVolumeClaim (PVC) independently
##   via its own `persistence.enabled` flag.
##
## COMMON SCENARIOS:
##
##   1. Static local storage (bare-metal / on-prem, no dynamic provisioner):
##        persistentVolumes.enabled: true        ← creates PVs
##        cassandra.persistence.enabled: true     ← sub-chart creates PVCs
##        cassandra.persistentVolumes.enabled: false  ← sub-chart skips its own PVs
##
##   2. Dynamic provisioner (AWS EBS, GCE PD, Longhorn, etc):
##        persistentVolumes.enabled: false        ← no PVs needed, provisioner handles it
##        cassandra.persistence.enabled: true     ← sub-chart creates PVCs
##        cassandra.persistence.storageClass: "longhorn"  ← provisioner creates PV automatically
##
##   3. Ephemeral / dev / test (no storage at all):
##        persistentVolumes.enabled: false        ← no PVs
##        cassandra.persistence.enabled: false    ← no PVCs, uses emptyDir
##
## =============================================================================
persistentVolumes:
  ## Master switch — set to false to skip ALL PV creation across all sub-charts.
  ## Useful when using a dynamic provisioner that creates PVs automatically.
  enabled: false

  ## Default reclaim policy applied to all PVs unless overridden per volume.
  ## Retain: PV and its data survive after PVC is deleted (recommended for production)
  ## Delete: PV and its data are automatically deleted when PVC is deleted
  persistentVolumeReclaimPolicy: Retain

  ## Volume mode applied to all PVs.
  ## Filesystem: standard file-based access (default, works with all ZooKeeper/Cassandra setups)
  ## Block: raw block device (advanced use cases only)
  volumeMode: Filesystem

  ## Access mode applied to all PVs.
  ## ReadWriteOnce: volume can be mounted by a single node (standard for local storage)
  accessModes: ReadWriteOnce

  ## Node affinity configuration — used to pin each PV to a specific node.
  ## This ensures a StatefulSet pod always finds its data on the same node it wrote to.
  matchExpressionsKey: kubernetes.io/hostname
  matchExpressionsOperator: In

  ## List of volume groups — one entry per logical storage purpose.
  ## Each group generates one PV per node in its `nodes` list.
  ## e.g. 3 nodes → 3 PVs named <name>-0, <name>-1, <name>-2
  volumes:

    ## -------------------------------------------------------------------------
    ## Cassandra data volumes
    ## -------------------------------------------------------------------------
    - name: cass-vol-cluster
      ## Set to false to skip PV creation for Cassandra without touching other volumes.
      ## If disabling, also set cassandra.persistence.storageClass to a dynamic provisioner
      ## or set cassandra.persistence.enabled: false to use emptyDir instead.
      enabled: false
      storage: 20Gi
      storageClassName: cassandra-local
      ## Local path that must exist on each node before deploying.
      ## The Cassandra process must have write access to this directory.
      localPath: /pv/multi-cass-cluster
      ## One entry per Cassandra node — PVs will be named cass-vol-cluster-0, -1, -2
      ## Example: - host: host.example.com (keep - host: lines depending on your deployment stragety)
      nodes:
        - host: 
        - host: 
        - host: 

    ## -------------------------------------------------------------------------
    ## ZooKeeper data volumes (snapshots → /data)
    ## -------------------------------------------------------------------------
    - name: zookeeper-data-pv
      ## Also set zookeeper.persistence.enabled: true and zookeeper.persistence.data.enabled: true
      enabled: false
      storage: 8Gi
      storageClassName: zookeeper-local
      ## Local path that must exist on each node before deploying.
      localPath: /pv/zookeeper/data
      ## Example: - host: host.example.com (keep - host: lines depending on your deployment stragety)
      nodes:
        - host: 
        - host: 
        - host: 

    ## -------------------------------------------------------------------------
    ## ZooKeeper log volumes (transaction logs → /datalog)
    ## Kept separate from data for better I/O isolation.
    ## -------------------------------------------------------------------------
    - name: zookeeper-log-pv
      ## Also set zookeeper.persistence.enabled: true and zookeeper.persistence.log.enabled: true
      enabled: false
      storage: 4Gi
      storageClassName: zookeeper-local
      localPath: /pv/zookeeper/log
      ## Example: - host: host.example.com (keep - host: lines depending on your deployment stragety)
      nodes:
        - host: 
        - host: 
        - host: 

twcloud:
  enabled: true
  svcLB: false
  cassandraPort: 9042
  image:
    # Specifies image repository name
    repository: twcloud/twcloud
    # Specifies image tag name
    tag: 
  replicas: 3
  env:
    twcxmx: 8384m
  resources:
    requests:
      memory: '8Gi'
      cpu: '1000m'
    limits:
      memory: '12Gi'
      cpu: '1000m'  

##### WebApplicationPlatform #####

# Admin-console application settings
adminconsole:
  # Specifies whether a admin-console application should be deployed (Mandatory)
  enabled: true
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: admin-console/admin-console
    # Specifies image tag name
    tag: 

# Authentication application settings
authentication:
  # Specifies whether a authentication application should be deployed (Optional)
  enabled: true
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: authentication/authentication
    # Specifies image tag name
    tag: 
# Sgicrawler application settings
sgicrawler:
  # Specifies whether a Sgicrawler application should be deployed (Mandatory)
  enabled: false
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: sgi-crawler/sgi-crawler
    # Specifies image tag name
    tag: 

# Sysml2-api application settings
sysml2api:
  # Specifies whether a Sysml2-api application should be deployed (Mandatory)
  enabled: false
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: sysml2-api/sysml2-api
    # Specifies image tag name
    tag: 
# Artemis service settings
artemis:
  # Specifies whether a artemis service should be deployed (Optional)
  # Required for WAP applications: resources, collaborator, document-exporter, simulation.
  enabled: true
  image:
    # Specifies image repository name
    repository: apache/artemis
    # Specifies image tag name (if tag is floating int, then be in quotation marks)
    tag: "2.53.0"

# Collaborator application settings
collaborator:
  # Specifies whether a collaborator application should be deployed
  enabled: true
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: collaborator/collaborator
    # Specifies image tag name
    tag: 

# Document-exporter application settings
docexporter:
  # Specifies whether a document-exporter application should be deployed (Optional)
  enabled: true
  # Specifies replica count
  replicas: 1
  # Specify path to the Prince executable. May be left empty or commented if the document exporter is not installed
  # The path may be absolute or relative to the Web application platform home folder
  documentExporterPrincePath: /usr/local/prince/lib/prince/bin/prince
  image:
    # Specifies image repository name
    repository: document-exporter/document-exporter
    # Specifies image tag name
    tag: 

elementchooser:
  # Specifies whether a element-chooser application should be deployed (Optional)
  enabled: false
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: element-chooser/element-chooser
    # Specifies image tag name
    tag: 

# Oslc application settings
oslc:
  # Specifies whether a oslc application should be deployed (Optional)
  enabled: false
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: oslc/oslc
    # Specifies image tag name
    tag: 

# Reports application settings
reports:
  # Specifies whether a reports application should be deployed (Optional)
  enabled: true
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: reports/reports
    # Specifies image tag name
    tag: 

# Resources application settings
resources:
  # Specifies whether a resources application should be deployed (Optional)
  enabled: true
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: resources/resources
    # Specifies image tag name
    tag: 

# Resource-usage-map application settings
rum:
  # Specifies whether a resource-usage-map application should be deployed (Optional)
  enabled: false
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: resource-usage-map/resource-usage-map
    # Specifies image tag name
    tag: 

# Simulation application settings
simulation:
  # Specifies whether a simulation application should be deployed (Optional)
  enabled: false
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: simulation/simulation
    # Specifies image tag name
    tag: 
  startupProbe:
    httpGet:
      # Specifies startup probe protocol, setting depends on your image configuration
      scheme: HTTPS
      # Specifies startup probe port, setting depends on your image configuration
      port: 8443

# MagicLab application settings
magiclab:
  # Specifies whether a MagicLab application should be deployed (Optional)
  enabled: true
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: magiclab/magiclab
    # Specifies image tag name
    tag: 

# MagicLab Collaborator application settings
magiclabcollab:
  # Specifies whether a MagicLab application should be deployed (Optional)
  enabled: true
  # Specifies replica count
  replicas: 3
  image:
    # Specifies image repository name
    repository: magiclabcollab/magiclabcollab
    # Specifies image tag name
    tag: 

# Webapp application settings
webapp:
  # Specifies whether a webapp application should be deployed (Mandatory)
  enabled: true
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: webapp/webapp
    # Specifies image tag name
    tag: 

# Zookeeper service settings
zookeeper:
  # Specifies whether a zookeeper service should be deployed (Mandatory)
  enabled: true
  # Must match the number of nodes in persistentVolumes.volumes[zookeeper-*].nodes
  replicas: 3
  image:
    repository: zookeeper
    pullPolicy: IfNotPresent
    tag: "3.9.5"
  # Persistence — binds to PVs created by the persistentVolumes section above.
  # storageClass must match persistentVolumes.volumes[zookeeper-*].storageClassName
  persistence:
    ## Master switch — false uses emptyDir for both volumes (ephemeral, data lost on restart)
    ## When true, data and log volumes can be enabled independently below.
    enabled: false
    storageClass: zookeeper-local
    accessModes:
      - ReadWriteOnce
    dataSize: 8Gi
    logSize: 4Gi
    data:
      ## Enable persistent storage for ZooKeeper snapshots (/data)
      ## Also set persistentVolumes.volumes[zookeeper-data-pv].enabled: true
      enabled: false
    log:
      ## Enable persistent storage for ZooKeeper transaction logs (/datalog)
      ## Also set persistentVolumes.volumes[zookeeper-log-pv].enabled: true
      enabled: false

# HAProxy Ingress Controller settings
# Replaces ingress-nginx (retired). Uses haproxytech/kubernetes-ingress helm chart.
# TCP ports (3579, 8111, 2468) are handled via TCP CRD in templates/tcp-services.yaml
ingress:
  enabled: true
  controller:
    ## ingressClassName must match the class set on the ingress controller (default: haproxy)
    className: haproxy

    ## Run as Deployment — works correctly with MetalLB providing the external IP
    kind: Deployment
    replicaCount: 2

    service:
      enabled: true
      type: LoadBalancer
      ports:
        http: 80
        https: 443
      ## Ports exposed on the controller for TCP CRD services (3579, 8111, 2468)
      ## These must match the ports defined in templates/tcp-services.yaml
      tcpPorts:
        - name: twc-client
          port: 3579
          targetPort: 3579
          protocol: TCP
        - name: twc-rest
          port: 8111
          targetPort: 8111
          protocol: TCP
        - name: twc-admin
          port: 2468
          targetPort: 2468
          protocol: TCP

    ## HAProxy ConfigMap options (equivalent to nginx controller.config)
    ## Full list: https://www.haproxy.com/documentation/kubernetes-ingress/community/configuration-reference/configmap/
    config:
      timeout-connect: "3600s"
      timeout-client: "3600s"
      timeout-server: "3600s"
      proxy-body-size: "100m"
      ssl-redirect: "true"    

    ## TLS
    defaultTLSSecret:
      enabled: true
      secretNamespace: '{{ include "kubernetes-ingress.namespace" . }}'
      secret: tls-secret

    ## Ingress resource annotations
    annotations:
      ## Backends serve HTTPS — tell HAProxy to use SSL when connecting to backends
      haproxy.org/server-ssl: "true"
      ## Keep WebSocket connections alive
      haproxy.org/timeout-tunnel: "3600s"
      haproxy.org/cookie-persistence: "rtns-cookie"

    hosts:
      # MANDATORY !
      # - host: example.com
      - host: 
````

### ENTRY: releaseNotes.txt

- bytes: 279
- crc32: `399449a9`
- decoded_as: `utf-8`

````text
TCAS_V: 2026xRefresh1

Changes:
    Replaced Bitnami Zookeeper chart.
    Replaced Bitnami Cassandra chart.
    Replaced retiring ingress-nginx to haproxy.
    Zookeeper version updated to 3.9.5
    Artemis ActiveMQ version updated to 2.53.0

Services:
    MagicLab-Collaborator

````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "314182199",
  "type": "attachment",
  "status": "current",
  "title": "twc-services-charts-2026xRefresh1.zip",
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
    "when": "2026-06-29T13:18:46.702+02:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/314182199/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/314182199"
    }
  },
  "position": -1,
  "container": {
    "id": "247046576",
    "type": "page",
    "status": "current",
    "title": "Deployment example on Kubernetes",
    "position": 1,
    "extensions": {
      "position": 1
    },
    "_links": {
      "webui": "/spaces/MCS/pages/247046576/Deployment+example+on+Kubernetes",
      "edit": "/pages/resumedraft.action?draftId=247046576",
      "tinyui": "/x/sKG5Dg",
      "self": "https://docs.nomagic.com/rest/api/content/247046576"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/247046576/child",
      "restrictions": "/rest/api/content/247046576/restriction/byOperation",
      "history": "/rest/api/content/247046576/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/247046576/descendant",
      "space": "/rest/api/space/MCS",
      "relevantViewRestrictions": "/rest/api/content/247046576/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/zip"
  },
  "extensions": {
    "mediaType": "application/zip",
    "fileSize": 92560,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/247046576/twc-services-charts-2026xRefresh1.zip?version=1&modificationDate=1782731926702&api=v2",
    "webui": "/spaces/MCS/pages/247046576/Deployment+example+on+Kubernetes?preview=%2F247046576%2F314182199%2Ftwc-services-charts-2026xRefresh1.zip",
    "self": "https://docs.nomagic.com/rest/api/content/314182199"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/314182199/child",
    "restrictions": "/rest/api/content/314182199/restriction/byOperation",
    "history": "/rest/api/content/314182199/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/314182199/descendant",
    "space": "/rest/api/space/MCS",
    "relevantViewRestrictions": "/rest/api/content/314182199/restriction/relevantViewRestrictions"
  }
}
````
