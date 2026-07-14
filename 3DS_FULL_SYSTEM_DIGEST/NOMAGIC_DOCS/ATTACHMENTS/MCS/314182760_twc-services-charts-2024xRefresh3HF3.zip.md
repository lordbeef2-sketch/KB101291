# NOMAGIC ATTACHMENT: twc-services-charts-2024xRefresh3HF3.zip

- attachment_id: `314182760`
- space_key: `MCS`
- parent_page_id: `314182206`
- parent_page_title: Copy of Deployment example on Kubernetes
- media_type: `application/zip`
- reported_bytes: 191250
- download_url: https://docs.nomagic.com/download/attachments/314182206/twc-services-charts-2024xRefresh3HF3.zip?version=1&modificationDate=1783514666460&api=v2
- payload_kind: `archive-expanded`
- downloaded_sha256: `9c5145e13bb0cf39917dc30e032ca896a0329c146ccdf093ca54e990abf222d9`

## ARCHIVE CONTENTS

### ENTRY: dockerfiles/admin-console/Dockerfile

- bytes: 948
- crc32: `56a6e871`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.55-jre21-temurin-jammy

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

- bytes: 954
- crc32: `bf008af0`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.55-jre21-temurin-jammy

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

- bytes: 996
- crc32: `09be1701`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.55-jre21-temurin-jammy

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

- bytes: 1672
- crc32: `e031153a`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.55-jre21-temurin-jammy

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

- bytes: 947
- crc32: `ead81195`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.55-jre21-temurin-jammy

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

- bytes: 947
- crc32: `5c56c85e`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.55-jre21-temurin-jammy

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

- bytes: 1081
- crc32: `4098acb2`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.55-jre21-temurin-jammy

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

- bytes: 952
- crc32: `0b8808e2`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.55-jre21-temurin-jammy

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

- bytes: 953
- crc32: `61942bd8`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.55-jre21-temurin-jammy

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

- bytes: 945
- crc32: `74ea5eb1`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.55-jre21-temurin-jammy

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

### ENTRY: dockerfiles/sgi-crawler/Dockerfile

- bytes: 950
- crc32: `98601556`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.55-jre21-temurin-jammy

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

- bytes: 950
- crc32: `f9490bb7`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.55-jre21-temurin-jammy

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

### ENTRY: helm-charts/charts/adminconsole/Chart.yaml

- bytes: 144
- crc32: `a7337bae`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: adminconsole
description: A Helm chart for admin-console
type: application
version: 0.1.3.2
appVersion: "2024xrefresh3HF3"

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

- bytes: 1168
- crc32: `2496d1b6`
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
version: 0.1.3.2

# This is the version number of the application being deployed. This version number should be
# incremented each time you make changes to the application. Versions are not expected to
# follow Semantic Versioning. They should reflect the version the application is using.
# It is recommended to use it with quotes.
appVersion: "2024xrefresh3HF3"

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

- bytes: 147
- crc32: `14f49366`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: authentication
description: A Helm chart for authentication
type: application
version: 0.1.3.2
appVersion: "2024xrefresh3HF3"

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

- bytes: 143
- crc32: `6b258a35`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: collaborator
description: A Helm chart for collaborator
type: application
version: 0.1.3.2
appVersion: "2024xrefresh3HF3"

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

- bytes: 141
- crc32: `877041fc`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: docexporter
description: A Helm chart for docexporter
type: application
version: 0.1.3.2
appVersion: "2024xrefresh3HF3"

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

### ENTRY: helm-charts/charts/oslc/Chart.yaml

- bytes: 127
- crc32: `be420095`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: oslc
description: A Helm chart for oslc
type: application
version: 0.1.3.2
appVersion: "2024xrefresh3HF3"

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

- bytes: 133
- crc32: `42db824b`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: reports
description: A Helm chart for reports
type: application
version: 0.1.3.2
appVersion: "2024xrefresh3HF3"

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

- bytes: 137
- crc32: `06f99bb5`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: resources
description: A Helm chart for resources
type: application
version: 0.1.3.2
appVersion: "2024xrefresh3HF3"

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

- bytes: 140
- crc32: `9bb0f70a`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: rum
description: A Helm chart for resource usage map
type: application
version: 0.1.3.2
appVersion: "2024xrefresh3HF3"

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

- bytes: 139
- crc32: `53c66786`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: simulation
description: A Helm chart for simulation
type: application
version: 0.1.3.2
appVersion: "2024xrefresh3HF3"

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

- bytes: 133
- crc32: `6d1e52a6`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: twcloud
description: A Helm chart for twcloud
type: application
version: 0.1.3.2
appVersion: "2024xrefresh3HF3"

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

### ENTRY: helm-charts/charts/webapp/Chart.yaml

- bytes: 131
- crc32: `4f19e486`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: webapp
description: A Helm chart for webapp
type: application
version: 0.1.3.2
appVersion: "2024xrefresh3HF3"

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

### ENTRY: helm-charts/charts/cassandra/Chart.yaml

- bytes: 165
- crc32: `c540afad`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: cassandra
description: A Helm chart for Apache Cassandra using the official Docker image
type: application
version: 0.1.3.2
appVersion: "5.0.5"

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

### ENTRY: helm-charts/charts/cassandra/templates/statefulset.yaml

- bytes: 11248
- crc32: `bbb30f9f`
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
            ## MAX_HEAP_SIZE and HEAP_NEWSIZE must be set or unset *in pairs*.
            ## cassandra-env.sh aborts startup if exactly one is set. Leave both
            ## empty to let Cassandra auto-calculate from detected memory/cores.
            - name: MAX_HEAP_SIZE
              value: {{ .Values.jvm.maxHeapSize | quote }}
            - name: HEAP_NEWSIZE
              value: {{ .Values.jvm.newHeapSize | quote }}
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

### ENTRY: helm-charts/charts/cassandra/values.yaml

- bytes: 6359
- crc32: `0ab94a06`
- decoded_as: `utf-8`

````yaml
## Enable/disable this chart
enabled: true

## Official Cassandra image
image:
  repository: cassandra
  tag: "4.1.8"
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
  ## HEAP_NEWSIZE (young generation). Must be set together with maxHeapSize —
  ## cassandra-env.sh refuses to start if only one of the two is set. Set both
  ## to a value, or leave both empty ("") to auto-calculate. For CMS, ~100M per
  ## CPU core is a reasonable starting point, capped near 1/4 of the heap.
  newHeapSize: "800M"
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

### ENTRY: helm-charts/charts/elementchooser/Chart.yaml

- bytes: 147
- crc32: `4f4c20a5`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: elementchooser
description: A Helm chart for elementchooser
type: application
version: 0.1.3.2
appVersion: "2024xrefresh3HF3"

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

### ENTRY: helm-charts/charts/sgicrawler/Chart.yaml

- bytes: 139
- crc32: `e8e62b3f`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: sgicrawler
description: A Helm chart for sgicrawler
type: application
version: 0.1.3.2
appVersion: "2024xrefresh3HF3"

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

- bytes: 138
- crc32: `d642856a`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: sysml2api
description: A Helm chart for sysmlv2api
type: application
version: 0.1.3.2
appVersion: "2024xrefresh3HF3"

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

### ENTRY: helm-charts/charts/zookeeper/Chart.yaml

- bytes: 294
- crc32: `a4266ead`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: zookeeper
description: A Helm chart for Apache ZooKeeper using the official image
type: application
version: 0.1.3.2
appVersion: "3.9"
keywords:
  - zookeeper
  - coordination
  - distributed
sources:
  - https://hub.docker.com/_/zookeeper
  - https://zookeeper.apache.org

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

### ENTRY: helm-charts/charts/kubernetes-ingress-1.49.0.tgz

- bytes: 38845
- crc32: `eb64c69e`
- sha256: `236bcd86e4af6ab6e126a3ad4c270ca8f7706a8087deb8391e39507c72b5acd0`
- payload_status: binary metadata only

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

- bytes: 2832
- crc32: `816842c1`
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

- bytes: 6287
- crc32: `78cbbe5d`
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
  maxReplicaCount: {{ .Values.maxreplicas | default 50 }}
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

- bytes: 5708
- crc32: `b168b57b`
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

- bytes: 1495
- crc32: `5205dba6`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: tcas
description: A Helm chart to deploy Teamwork cloud and services

type: application

version: 0.1.3.2

appVersion: "2024xrefresh3HF3"

dependencies:
- name: kubernetes-ingress
  version: 1.49.0
  repository: https://haproxytech.github.io/helm-charts
  alias: ingress
  condition: ingress.enabled

- name: zookeeper
  version: 0.1.3.2
  condition: zookeeper.enabled

- name: cassandra
  version: 0.1.3.2  
  condition: cassandra.enabled

- name: twcloud
  version: 0.1.3.2
  condition: twcloud.enabled

- name: adminconsole
  version: 0.1.3.2
  condition: adminconsole.enabled

- name: authentication
  version: 0.1.3.2
  condition: authentication.enabled

- name: artemis
  version: 0.1.3.2
  condition: artemis.enabled

- name: collaborator
  version: 0.1.3.2
  condition: collaborator.enabled

- name: docexporter
  version: 0.1.3.2
  condition: docexporter.enabled

- name: oslc
  version: 0.1.3.2
  condition: oslc.enabled

- name: reports
  version: 0.1.3.2
  condition: reports.enabled

- name: resources
  version: 0.1.3.2
  condition: resources.enabled

- name: rum
  version: 0.1.3.2
  condition: rum.enabled

- name: simulation
  version: 0.1.3.2
  condition: simulation.enabled

- name: webapp
  version: 0.1.3.2
  condition: webapp.enabled

- name: sysml2api
  version: 0.1.3.2
  condition: sysml2api.enabled

- name: sgicrawler
  version: 0.1.3.2
  condition: sgicrawler.enabled

- name: elementchooser
  version: 0.1.3.2
  condition: elementchooser.enabled
````

### ENTRY: helm-charts/values.yaml

- bytes: 19635
- crc32: `a84df2b7`
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
    tag: "4.1.8"
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
    tag: "2.54.0"

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

### ENTRY: helm-charts/configs/auth/authserver.properties

- bytes: 8701
- crc32: `59a1fc52`
- decoded_as: `utf-8`

````text
#---------------------------------------------------
# List of allowed redirect URIs. Authentication server
# client should pass valid redirect URI to /authorize endpoint.
#---------------------------------------------------
authentication.redirect.uri.whitelist=https://127.0.0.1:8443/,https://127.0.0.1:8111/,https://md_redirect

#-------------------------------------------------------------------------------
# Authentication ID token expiration time in seconds.
#-------------------------------------------------------------------------------
#authentication.token.expirity=604800

#-------------------------------------------------------------------------------
# Authentication code expiration time in seconds.
#-------------------------------------------------------------------------------
#authentication.code.token.expirity=15

#-------------------------------------------------------------------------------
# Authentication refresh token expiration time in seconds.
#-------------------------------------------------------------------------------
#authentication.refresh.token.expirity=1209600

#-------------------------------------------------------------------------------
# Authentication ID token expiration time in seconds
# for the implicit authentication flow (for ex., used
# for MagicDraw UML).
#-------------------------------------------------------------------------------
#authentication.implicit.token.expirity=86400

#-------------------------------------------------------------------------------
# Authentication ID token that has extremely long
# expiration time and should only be used in
# server-server requests when there is a need to
# perform regular batch jobs.
#-------------------------------------------------------------------------------
#authentication.unlimited.token.expirity=630720000

#-------------------------------------------------------------------------------
# Properties used for keystore reading:
#
# - Path to keystore file (absolute or relative)
# - Keystore type (JKS or PKCS12)
# - Keystore password
# - Private key password
# - Private key alias in the keystore
#
# If service is deployed on a cluster, all instances should use the same keystore.
#-------------------------------------------------------------------------------
authentication.server.key-store=../TeamworkCloud/configuration/keystore.p12
authentication.server.key-store-type=PKCS12
authentication.server.key-store-password=nomagic
authentication.server.key-password=nomagic
authentication.server.key-alias=teamworkcloud

#-------------------------------------------------------------------------------
# Valid client IDs (separated by commas).
#-------------------------------------------------------------------------------
#authentication.client.ids=MAGICDRAW,webApplicationPlatform,twcSynchronizationManager

#-------------------------------------------------------------------------------
# Implicit authentication flow client IDs (separated by commas).
#-------------------------------------------------------------------------------
#authentication.client.implicit=MAGICDRAW

#-------------------------------------------------------------------------------
# Client IDs that use token ID of unlimited expiration (separated by commas).
#-------------------------------------------------------------------------------
#authentication.client.unlimited=twcSynchronizationManager

#-------------------------------------------------------------------------------
# IDs of clients that do not see Remember Me flag (separated by commas).
#-------------------------------------------------------------------------------
#authentication.remember.me.hidden.client.ids=MAGICDRAW

#---------------------------------------------------
# SAML integration is no longer configured via properties file.
# Instead, SAML can be configured in Settings application under SAML menu section.
#---------------------------------------------------

#-------------------------------------------------------------------------------
# Indicates if authentication by certificate is available.
#-------------------------------------------------------------------------------
authentication.certificate.enabled=false

#-------------------------------------------------------------------------------
# Indicates if authentication by certificate information in HTTP headers is
# available. This option should only be used when Authentication Server can only
# be accessed through load balancer or proxy server that checks validity of the
# client certificate and sets appropriate HTTP headers:
# * X-Issuer-Dn
# * X-Subject-Dn
# * X-Serial-Number (hex format)
#-------------------------------------------------------------------------------
#authentication.certificate.headers.enabled=false

#-------------------------------------------------------------------------------
# If certificate authentication is enabled, following parameters are used for
# username extraction from the certificate subject DN (distinguished name) or
# SAN (subject alternative name) field. User name is stored in the TWCloud
# server.
# * Source of the user name. Available values: dn (distinguished name), san 
#   (subject alternative name)
# * SAN type. Available values: 0 (other name), 1 (RFC 822 name), 2 (DNS name),
#   4 (directory name).
# * SAN identifier to use if SAN type is 0.
# * Template to use if user name source is DN or SAN type is 4.
#-------------------------------------------------------------------------------
#authentication.certificate.username.source=dn
#authentication.certificate.username.san.type=4
#authentication.certificate.username.san.id=
#authentication.certificate.username.template=(CN)

#-------------------------------------------------------------------------------
# If certificate authentication is enabled, following parameters are used for
# user display name extraction from the certificate subject DN (distinguished
# name) or SAN (subject alternative name) field. Display name is used for
# display purposes only, and describes the text that is shown on authentication
# button.
# * Source of the display name. Available values: dn (distinguished name), san 
#   (subject alternative name)
# * SAN type. Available values: 0 (other name), 1 (RFC 822 name), 2 (DNS name),
#   4 (directory name).
# * SAN identifier to use if SAN type is 0.
# * Template to use if display name source is DN or SAN type is 4.
#-------------------------------------------------------------------------------
#authentication.certificate.displayname.source=dn
#authentication.certificate.displayname.san.type=4
#authentication.certificate.displayname.san.id=
#authentication.certificate.displayname.template=(CN)

#-------------------------------------------------------------------------------
# URL or absolute filesystem path to the CRL file that
# contains the list of the certificates revoked by the
# certificate authority.
#-------------------------------------------------------------------------------
#authentication.certificate.revocation.list.url=
#authentication.certificate.revocation.list.file=

#-------------------------------------------------------------------------------
# Properties for GUI transformation:
# 1. Path to the banner logo if such used, for ex., ./banner.png.
# File types JPEG, GIF and PNG are supported.
# 2. Banner text. Only new line (\n) special symbol is supported.
# 3. Color for login page background. Different formats allowed,
# for ex., #FFFFFF, rgb(220,220,220), etc. Default color is rgb(250,250,250).
#-------------------------------------------------------------------------------
#classification.loginbannerlogo=
#classification.loginbannertext=
#classification.loginbackground=

#-------------------------------------------------------------------------------
# Ability to disable username/password authentication
# if external user authentication (CAC, SAML) is used.
#-------------------------------------------------------------------------------
#authentication.disable.credentials=false

#-------------------------------------------------------------------------------
# Defines the delay (in seconds) between retry attempts when a connection to
# TWC Cassandra client is refused (Cassandra may be not started yet).
#-------------------------------------------------------------------------------
cassandra.client.connection.delay = 30

#-------------------------------------------------------------------------------
# Specifies how many times the application should retry a failed
# TWC Cassandra client connection.
#-------------------------------------------------------------------------------
cassandra.client.connection.retries = 12
````

### ENTRY: helm-charts/configs/cassandra/cassandra.yaml

- bytes: 91491
- crc32: `14d8a849`
- decoded_as: `utf-8`

````yaml

# Cassandra storage config YAML

# NOTE:
#   See https://cassandra.apache.org/doc/latest/configuration/ for
#   full explanations of configuration directives
# /NOTE

# The name of the cluster. This is mainly used to prevent machines in
# one logical cluster from joining another.
cluster_name: 'Test Cluster'

# This defines the number of tokens randomly assigned to this node on the ring
# The more tokens, relative to other nodes, the larger the proportion of data
# that this node will store. You probably want all nodes to have the same number
# of tokens assuming they have equal hardware capability.
#
# If you leave this unspecified, Cassandra will use the default of 1 token for legacy compatibility,
# and will use the initial_token as described below.
#
# Specifying initial_token will override this setting on the node's initial start,
# on subsequent starts, this setting will apply even if initial token is set.
#
# See https://cassandra.apache.org/doc/latest/getting_started/production.html#tokens for
# best practice information about num_tokens.
#
num_tokens: 16

# Triggers automatic allocation of num_tokens tokens for this node. The allocation
# algorithm attempts to choose tokens in a way that optimizes replicated load over
# the nodes in the datacenter for the replica factor.
#
# The load assigned to each node will be close to proportional to its number of
# vnodes.
#
# Only supported with the Murmur3Partitioner.

# Replica factor is determined via the replication strategy used by the specified
# keyspace.
# allocate_tokens_for_keyspace: KEYSPACE

# Replica factor is explicitly set, regardless of keyspace or datacenter.
# This is the replica factor within the datacenter, like NTS.
allocate_tokens_for_local_replication_factor: 3

# initial_token allows you to specify tokens manually.  While you can use it with
# vnodes (num_tokens > 1, above) -- in which case you should provide a 
# comma-separated list -- it's primarily used when adding nodes to legacy clusters 
# that do not have vnodes enabled.
# initial_token:

# May either be "true" or "false" to enable globally
hinted_handoff_enabled: true

# When hinted_handoff_enabled is true, a black list of data centers that will not
# perform hinted handoff
# hinted_handoff_disabled_datacenters:
#    - DC1
#    - DC2

# this defines the maximum amount of time a dead host will have hints
# generated.  After it has been dead this long, new hints for it will not be
# created until it has been seen alive and gone down again.
# Min unit: ms
max_hint_window: 3h

# Maximum throttle in KiBs per second, per delivery thread.  This will be
# reduced proportionally to the number of nodes in the cluster.  (If there
# are two nodes in the cluster, each delivery thread will use the maximum
# rate; if there are three, each will throttle to half of the maximum,
# since we expect two nodes to be delivering hints simultaneously.)
# Min unit: KiB
hinted_handoff_throttle: 1024KiB

# Number of threads with which to deliver hints;
# Consider increasing this number when you have multi-dc deployments, since
# cross-dc handoff tends to be slower
max_hints_delivery_threads: 2

# Directory where Cassandra should store hints.
# If not set, the default directory is $CASSANDRA_HOME/data/hints.
# hints_directory: /var/lib/cassandra/hints

# How often hints should be flushed from the internal buffers to disk.
# Will *not* trigger fsync.
# Min unit: ms
hints_flush_period: 10000ms

# Maximum size for a single hints file, in mebibytes.
# Min unit: MiB
max_hints_file_size: 128MiB

# The file size limit to store hints for an unreachable host, in mebibytes.
# Once the local hints files have reached the limit, no more new hints will be created.
# Set a non-positive value will disable the size limit.
# max_hints_size_per_host: 0MiB

# Enable / disable automatic cleanup for the expired and orphaned hints file.
# Disable the option in order to preserve those hints on the disk.
auto_hints_cleanup_enabled: false

# Enable/disable transfering hints to a peer during decommission. Even when enabled, this does not guarantee
# consistency for logged batches, and it may delay decommission when coupled with a strict hinted_handoff_throttle.
# Default: true
# transfer_hints_on_decommission: true

# Compression to apply to the hint files. If omitted, hints files
# will be written uncompressed. LZ4, Snappy, and Deflate compressors
# are supported.
#hints_compression:
#   - class_name: LZ4Compressor
#     parameters:
#         -

# Enable / disable persistent hint windows.
#
# If set to false, a hint will be stored only in case a respective node
# that hint is for is down less than or equal to max_hint_window.
#
# If set to true, a hint will be stored in case there is not any
# hint which was stored earlier than max_hint_window. This is for cases
# when a node keeps to restart and hints are not delivered yet, we would be saving
# hints for that node indefinitely.
#
# Defaults to true.
#
# hint_window_persistent_enabled: true

# Maximum throttle in KiBs per second, total. This will be
# reduced proportionally to the number of nodes in the cluster.
# Min unit: KiB
batchlog_replay_throttle: 1024KiB

# Strategy to choose the batchlog storage endpoints.
#
# Available options:
#
# - random_remote
#   Default, purely random, prevents the local rack, if possible.
#
# - prefer_local
#   Similar to random_remote. Random, except that one of the replications will go to the local rack,
#   which mean it offers lower availability guarantee than random_remote or dynamic_remote.
#
# - dynamic_remote
#   Using DynamicEndpointSnitch to select batchlog storage endpoints, prevents the
#   local rack, if possible. This strategy offers the same availability guarantees
#   as random_remote but selects the fastest endpoints according to the DynamicEndpointSnitch.
#   (DynamicEndpointSnitch currently only tracks reads and not writes - i.e. write-only
#   (or mostly-write) workloads might not benefit from this strategy.)
#   Note: this strategy will fall back to random_remote, if dynamic_snitch is not enabled.
#
# - dynamic
#   Mostly the same as dynamic_remote, except that local rack is not excluded, which mean it offers lower
#   availability guarantee than random_remote or dynamic_remote.
#   Note: this strategy will fall back to random_remote, if dynamic_snitch is not enabled.
#
# batchlog_endpoint_strategy: random_remote

# Authentication backend, implementing IAuthenticator; used to identify users
# Out of the box, Cassandra provides org.apache.cassandra.auth.{AllowAllAuthenticator,
# PasswordAuthenticator}.
#
# - AllowAllAuthenticator performs no checks - set it to disable authentication.
# - PasswordAuthenticator relies on username/password pairs to authenticate
#   users. It keeps usernames and hashed passwords in system_auth.roles table.
#   Please increase system_auth keyspace replication factor if you use this authenticator.
#   If using PasswordAuthenticator, CassandraRoleManager must also be used (see below)
authenticator: AllowAllAuthenticator

# Authorization backend, implementing IAuthorizer; used to limit access/provide permissions
# Out of the box, Cassandra provides org.apache.cassandra.auth.{AllowAllAuthorizer,
# CassandraAuthorizer}.
#
# - AllowAllAuthorizer allows any action to any user - set it to disable authorization.
# - CassandraAuthorizer stores permissions in system_auth.role_permissions table. Please
#   increase system_auth keyspace replication factor if you use this authorizer.
authorizer: AllowAllAuthorizer

# Part of the Authentication & Authorization backend, implementing IRoleManager; used
# to maintain grants and memberships between roles.
# Out of the box, Cassandra provides org.apache.cassandra.auth.CassandraRoleManager,
# which stores role information in the system_auth keyspace. Most functions of the
# IRoleManager require an authenticated login, so unless the configured IAuthenticator
# actually implements authentication, most of this functionality will be unavailable.
#
# - CassandraRoleManager stores role data in the system_auth keyspace. Please
#   increase system_auth keyspace replication factor if you use this role manager.
role_manager: CassandraRoleManager

# Network authorization backend, implementing INetworkAuthorizer; used to restrict user
# access to certain DCs
# Out of the box, Cassandra provides org.apache.cassandra.auth.{AllowAllNetworkAuthorizer,
# CassandraNetworkAuthorizer}.
#
# - AllowAllNetworkAuthorizer allows access to any DC to any user - set it to disable authorization.
# - CassandraNetworkAuthorizer stores permissions in system_auth.network_permissions table. Please
#   increase system_auth keyspace replication factor if you use this authorizer.
network_authorizer: AllowAllNetworkAuthorizer

# Depending on the auth strategy of the cluster, it can be beneficial to iterate
# from root to table (root -> ks -> table) instead of table to root (table -> ks -> root).
# As the auth entries are whitelisting, once a permission is found you know it to be
# valid. We default to false as the legacy behavior is to query at the table level then
# move back up to the root. See CASSANDRA-17016 for details.
# traverse_auth_from_root: false

# Validity period for roles cache (fetching granted roles can be an expensive
# operation depending on the role manager, CassandraRoleManager is one example)
# Granted roles are cached for authenticated sessions in AuthenticatedUser and
# after the period specified here, become eligible for (async) reload.
# Defaults to 2000, set to 0 to disable caching entirely.
# Will be disabled automatically for AllowAllAuthenticator.
# For a long-running cache using roles_cache_active_update, consider
# setting to something longer such as a daily validation: 86400000
# Min unit: ms
roles_validity: 2000ms

# Refresh interval for roles cache (if enabled).
# After this interval, cache entries become eligible for refresh. Upon next
# access, an async reload is scheduled and the old value returned until it
# completes. If roles_validity is non-zero, then this must be
# also.
# This setting is also used to inform the interval of auto-updating if
# using roles_cache_active_update.
# Defaults to the same value as roles_validity.
# For a long-running cache, consider setting this to 60000 (1 hour) etc.
# Min unit: ms
# roles_update_interval: 2000ms

# If true, cache contents are actively updated by a background task at the
# interval set by roles_update_interval. If false, cache entries
# become eligible for refresh after their update interval. Upon next access,
# an async reload is scheduled and the old value returned until it completes.
# roles_cache_active_update: false

# Validity period for permissions cache (fetching permissions can be an
# expensive operation depending on the authorizer, CassandraAuthorizer is
# one example). Defaults to 2000, set to 0 to disable.
# Will be disabled automatically for AllowAllAuthorizer.
# For a long-running cache using permissions_cache_active_update, consider
# setting to something longer such as a daily validation: 86400000ms
# Min unit: ms
permissions_validity: 2000ms

# Refresh interval for permissions cache (if enabled).
# After this interval, cache entries become eligible for refresh. Upon next
# access, an async reload is scheduled and the old value returned until it
# completes. If permissions_validity is non-zero, then this must be
# also.
# This setting is also used to inform the interval of auto-updating if
# using permissions_cache_active_update.
# Defaults to the same value as permissions_validity.
# For a longer-running permissions cache, consider setting to update hourly (60000)
# Min unit: ms
# permissions_update_interval: 2000ms

# If true, cache contents are actively updated by a background task at the
# interval set by permissions_update_interval. If false, cache entries
# become eligible for refresh after their update interval. Upon next access,
# an async reload is scheduled and the old value returned until it completes.
# permissions_cache_active_update: false

# Validity period for credentials cache. This cache is tightly coupled to
# the provided PasswordAuthenticator implementation of IAuthenticator. If
# another IAuthenticator implementation is configured, this cache will not
# be automatically used and so the following settings will have no effect.
# Please note, credentials are cached in their encrypted form, so while
# activating this cache may reduce the number of queries made to the
# underlying table, it may not  bring a significant reduction in the
# latency of individual authentication attempts.
# Defaults to 2000, set to 0 to disable credentials caching.
# For a long-running cache using credentials_cache_active_update, consider
# setting to something longer such as a daily validation: 86400000
# Min unit: ms
credentials_validity: 2000ms

# Refresh interval for credentials cache (if enabled).
# After this interval, cache entries become eligible for refresh. Upon next
# access, an async reload is scheduled and the old value returned until it
# completes. If credentials_validity is non-zero, then this must be
# also.
# This setting is also used to inform the interval of auto-updating if
# using credentials_cache_active_update.
# Defaults to the same value as credentials_validity.
# For a longer-running permissions cache, consider setting to update hourly (60000)
# Min unit: ms
# credentials_update_interval: 2000ms

# If true, cache contents are actively updated by a background task at the
# interval set by credentials_update_interval. If false (default), cache entries
# become eligible for refresh after their update interval. Upon next access,
# an async reload is scheduled and the old value returned until it completes.
# credentials_cache_active_update: false

# The partitioner is responsible for distributing groups of rows (by
# partition key) across nodes in the cluster. The partitioner can NOT be
# changed without reloading all data.  If you are adding nodes or upgrading,
# you should set this to the same partitioner that you are currently using.
#
# The default partitioner is the Murmur3Partitioner. Older partitioners
# such as the RandomPartitioner, ByteOrderedPartitioner, and
# OrderPreservingPartitioner have been included for backward compatibility only.
# For new clusters, you should NOT change this value.
#
partitioner: org.apache.cassandra.dht.Murmur3Partitioner

# Directories where Cassandra should store data on disk. If multiple
# directories are specified, Cassandra will spread data evenly across 
# them by partitioning the token ranges.
# If not set, the default directory is $CASSANDRA_HOME/data/data.
# data_file_directories:
#     - /var/lib/cassandra/data

# Directory were Cassandra should store the data of the local system keyspaces.
# By default Cassandra will store the data of the local system keyspaces in the first of the data directories specified
# by data_file_directories.
# This approach ensures that if one of the other disks is lost Cassandra can continue to operate. For extra security
# this setting allows to store those data on a different directory that provides redundancy.
# local_system_data_file_directory:

# commit log.  when running on magnetic HDD, this should be a
# separate spindle than the data directories.
# If not set, the default directory is $CASSANDRA_HOME/data/commitlog.
# commitlog_directory: /var/lib/cassandra/commitlog

# Enable / disable CDC functionality on a per-node basis. This modifies the logic used
# for write path allocation rejection (standard: never reject. cdc: reject Mutation
# containing a CDC-enabled table if at space limit in cdc_raw_directory).
cdc_enabled: false

# CommitLogSegments are moved to this directory on flush if cdc_enabled: true and the
# segment contains mutations for a CDC-enabled table. This should be placed on a
# separate spindle than the data directories. If not set, the default directory is
# $CASSANDRA_HOME/data/cdc_raw.
# cdc_raw_directory: /var/lib/cassandra/cdc_raw

# Policy for data disk failures:
#
# die
#   shut down gossip and client transports and kill the JVM for any fs errors or
#   single-sstable errors, so the node can be replaced.
#
# stop_paranoid
#   shut down gossip and client transports even for single-sstable errors,
#   kill the JVM for errors during startup.
#
# stop
#   shut down gossip and client transports, leaving the node effectively dead, but
#   can still be inspected via JMX, kill the JVM for errors during startup.
#
# best_effort
#    stop using the failed disk and respond to requests based on
#    remaining available sstables.  This means you WILL see obsolete
#    data at CL.ONE!
#
# ignore
#    ignore fatal errors and let requests fail, as in pre-1.2 Cassandra
disk_failure_policy: stop

# Policy for commit disk failures:
#
# die
#   shut down the node and kill the JVM, so the node can be replaced.
#
# stop
#   shut down the node, leaving the node effectively dead, but
#   can still be inspected via JMX.
#
# stop_commit
#   shutdown the commit log, letting writes collect but
#   continuing to service reads, as in pre-2.0.5 Cassandra
#
# ignore
#   ignore fatal errors and let the batches fail
commit_failure_policy: stop

# Maximum size of the native protocol prepared statement cache
#
# Valid values are either "auto" (omitting the value) or a value greater 0.
#
# Note that specifying a too large value will result in long running GCs and possbily
# out-of-memory errors. Keep the value at a small fraction of the heap.
#
# If you constantly see "prepared statements discarded in the last minute because
# cache limit reached" messages, the first step is to investigate the root cause
# of these messages and check whether prepared statements are used correctly -
# i.e. use bind markers for variable parts.
#
# Do only change the default value, if you really have more prepared statements than
# fit in the cache. In most cases it is not neccessary to change this value.
# Constantly re-preparing statements is a performance penalty.
#
# Default value ("auto") is 1/256th of the heap or 10MiB, whichever is greater
# Min unit: MiB
prepared_statements_cache_size:

# Maximum size of the key cache in memory.
#
# Each key cache hit saves 1 seek and each row cache hit saves 2 seeks at the
# minimum, sometimes more. The key cache is fairly tiny for the amount of
# time it saves, so it's worthwhile to use it at large numbers.
# The row cache saves even more time, but must contain the entire row,
# so it is extremely space-intensive. It's best to only use the
# row cache if you have hot rows or static rows.
#
# NOTE: if you reduce the size, you may not get you hottest keys loaded on startup.
#
# Default value is empty to make it "auto" (min(5% of Heap (in MiB), 100MiB)). Set to 0 to disable key cache.
# Min unit: MiB
key_cache_size:

# Duration in seconds after which Cassandra should
# save the key cache. Caches are saved to saved_caches_directory as
# specified in this configuration file.
#
# Saved caches greatly improve cold-start speeds, and is relatively cheap in
# terms of I/O for the key cache. Row cache saving is much more expensive and
# has limited use.
#
# Default is 14400 or 4 hours.
# Min unit: s
key_cache_save_period: 4h

# Number of keys from the key cache to save
# Disabled by default, meaning all keys are going to be saved
# key_cache_keys_to_save: 100

# Row cache implementation class name. Available implementations:
#
# org.apache.cassandra.cache.OHCProvider
#   Fully off-heap row cache implementation (default).
#
# org.apache.cassandra.cache.SerializingCacheProvider
#   This is the row cache implementation availabile
#   in previous releases of Cassandra.
# row_cache_class_name: org.apache.cassandra.cache.OHCProvider

# Maximum size of the row cache in memory.
# Please note that OHC cache implementation requires some additional off-heap memory to manage
# the map structures and some in-flight memory during operations before/after cache entries can be
# accounted against the cache capacity. This overhead is usually small compared to the whole capacity.
# Do not specify more memory that the system can afford in the worst usual situation and leave some
# headroom for OS block level cache. Do never allow your system to swap.
#
# Default value is 0, to disable row caching.
# Min unit: MiB
row_cache_size: 0MiB

# Duration in seconds after which Cassandra should save the row cache.
# Caches are saved to saved_caches_directory as specified in this configuration file.
#
# Saved caches greatly improve cold-start speeds, and is relatively cheap in
# terms of I/O for the key cache. Row cache saving is much more expensive and
# has limited use.
#
# Default is 0 to disable saving the row cache.
# Min unit: s
row_cache_save_period: 0s

# Number of keys from the row cache to save.
# Specify 0 (which is the default), meaning all keys are going to be saved
# row_cache_keys_to_save: 100

# Maximum size of the counter cache in memory.
#
# Counter cache helps to reduce counter locks' contention for hot counter cells.
# In case of RF = 1 a counter cache hit will cause Cassandra to skip the read before
# write entirely. With RF > 1 a counter cache hit will still help to reduce the duration
# of the lock hold, helping with hot counter cell updates, but will not allow skipping
# the read entirely. Only the local (clock, count) tuple of a counter cell is kept
# in memory, not the whole counter, so it's relatively cheap.
#
# NOTE: if you reduce the size, you may not get you hottest keys loaded on startup.
#
# Default value is empty to make it "auto" (min(2.5% of Heap (in MiB), 50MiB)). Set to 0 to disable counter cache.
# NOTE: if you perform counter deletes and rely on low gcgs, you should disable the counter cache.
# Min unit: MiB
counter_cache_size:

# Duration in seconds after which Cassandra should
# save the counter cache (keys only). Caches are saved to saved_caches_directory as
# specified in this configuration file.
#
# Default is 7200 or 2 hours.
# Min unit: s
counter_cache_save_period: 7200s

# Number of keys from the counter cache to save
# Disabled by default, meaning all keys are going to be saved
# counter_cache_keys_to_save: 100

# saved caches
# If not set, the default directory is $CASSANDRA_HOME/data/saved_caches.
# saved_caches_directory: /var/lib/cassandra/saved_caches

# Number of seconds the server will wait for each cache (row, key, etc ...) to load while starting
# the Cassandra process. Setting this to zero is equivalent to disabling all cache loading on startup
# while still having the cache during runtime.
# Min unit: s
# cache_load_timeout: 30s

# commitlog_sync may be either "periodic", "group", or "batch." 
# 
# When in batch mode, Cassandra won't ack writes until the commit log
# has been flushed to disk.  Each incoming write will trigger the flush task.
# commitlog_sync_batch_window_in_ms is a deprecated value. Previously it had
# almost no value, and is being removed.
#
# commitlog_sync_batch_window_in_ms: 2
#
# group mode is similar to batch mode, where Cassandra will not ack writes
# until the commit log has been flushed to disk. The difference is group
# mode will wait up to commitlog_sync_group_window between flushes.
#
# Min unit: ms
# commitlog_sync_group_window: 1000ms
#
# the default option is "periodic" where writes may be acked immediately
# and the CommitLog is simply synced every commitlog_sync_period
# milliseconds.
commitlog_sync: periodic
# Min unit: ms
commitlog_sync_period: 10000ms

# When in periodic commitlog mode, the number of milliseconds to block writes
# while waiting for a slow disk flush to complete.
# Min unit: ms
# periodic_commitlog_sync_lag_block:

# The size of the individual commitlog file segments.  A commitlog
# segment may be archived, deleted, or recycled once all the data
# in it (potentially from each columnfamily in the system) has been
# flushed to sstables.
#
# The default size is 32, which is almost always fine, but if you are
# archiving commitlog segments (see commitlog_archiving.properties),
# then you probably want a finer granularity of archiving; 8 or 16 MB
# is reasonable.
# Max mutation size is also configurable via max_mutation_size setting in
# cassandra.yaml. The default is half the size commitlog_segment_size in bytes.
# This should be positive and less than 2048.
#
# NOTE: If max_mutation_size is set explicitly then commitlog_segment_size must
# be set to at least twice the size of max_mutation_size
#
# Min unit: MiB
commitlog_segment_size: 192MiB

# Compression to apply to the commit log. If omitted, the commit log
# will be written uncompressed.  LZ4, Snappy, and Deflate compressors
# are supported.
# commitlog_compression:
#   - class_name: LZ4Compressor
#     parameters:
#         -

# Compression to apply to SSTables as they flush for compressed tables.
# Note that tables without compression enabled do not respect this flag.
#
# As high ratio compressors like LZ4HC, Zstd, and Deflate can potentially
# block flushes for too long, the default is to flush with a known fast
# compressor in those cases. Options are:
#
# none : Flush without compressing blocks but while still doing checksums.
# fast : Flush with a fast compressor. If the table is already using a
#        fast compressor that compressor is used.
# table: Always flush with the same compressor that the table uses. This
#        was the pre 4.0 behavior.
#
# flush_compression: fast

# any class that implements the SeedProvider interface and has a
# constructor that takes a Map<String, String> of parameters will do.
seed_provider:
  # Addresses of hosts that are deemed contact points.
  # Cassandra nodes use this list of hosts to find each other and learn
  # the topology of the ring.  You must change this if you are running
  # multiple nodes!
  - class_name: org.apache.cassandra.locator.SimpleSeedProvider
    parameters:
      # seeds is actually a comma-delimited list of addresses.
      # Ex: "<ip1>,<ip2>,<ip3>"
      - seeds: "127.0.0.1:7000"

# For workloads with more data than can fit in memory, Cassandra's
# bottleneck will be reads that need to fetch data from
# disk. "concurrent_reads" should be set to (16 * number_of_drives) in
# order to allow the operations to enqueue low enough in the stack
# that the OS and drives can reorder them. Same applies to
# "concurrent_counter_writes", since counter writes read the current
# values before incrementing and writing them back.
#
# On the other hand, since writes are almost never IO bound, the ideal
# number of "concurrent_writes" is dependent on the number of cores in
# your system; (8 * number_of_cores) is a good rule of thumb.
concurrent_reads: 32
concurrent_writes: 32
concurrent_counter_writes: 32

# For materialized view writes, as there is a read involved, so this should
# be limited by the less of concurrent reads or concurrent writes.
concurrent_materialized_view_writes: 32

# Maximum memory to use for inter-node and client-server networking buffers.
#
# Defaults to the smaller of 1/16 of heap or 128MB. This pool is allocated off-heap,
# so is in addition to the memory allocated for heap. The cache also has on-heap
# overhead which is roughly 128 bytes per chunk (i.e. 0.2% of the reserved size
# if the default 64k chunk size is used).
# Memory is only allocated when needed.
# Min unit: MiB
# networking_cache_size: 128MiB

# Enable the sstable chunk cache.  The chunk cache will store recently accessed
# sections of the sstable in-memory as uncompressed buffers.
# file_cache_enabled: false

# Maximum memory to use for sstable chunk cache and buffer pooling.
# 32MB of this are reserved for pooling buffers, the rest is used for chunk cache
# that holds uncompressed sstable chunks.
# Defaults to the smaller of 1/4 of heap or 512MB. This pool is allocated off-heap,
# so is in addition to the memory allocated for heap. The cache also has on-heap
# overhead which is roughly 128 bytes per chunk (i.e. 0.2% of the reserved size
# if the default 64k chunk size is used).
# Memory is only allocated when needed.
# Min unit: MiB
# file_cache_size: 512MiB

# Flag indicating whether to allocate on or off heap when the sstable buffer
# pool is exhausted, that is when it has exceeded the maximum memory
# file_cache_size, beyond which it will not cache buffers but allocate on request.

# buffer_pool_use_heap_if_exhausted: true

# The strategy for optimizing disk read
# Possible values are:
# ssd (for solid state disks, the default)
# spinning (for spinning disks)
# disk_optimization_strategy: ssd

# Total permitted memory to use for memtables. Cassandra will stop
# accepting writes when the limit is exceeded until a flush completes,
# and will trigger a flush based on memtable_cleanup_threshold
# If omitted, Cassandra will set both to 1/4 the size of the heap.
# Min unit: MiB
# memtable_heap_space: 2048MiB
# Min unit: MiB
# memtable_offheap_space: 2048MiB

# memtable_cleanup_threshold is deprecated. The default calculation
# is the only reasonable choice. See the comments on  memtable_flush_writers
# for more information.
#
# Ratio of occupied non-flushing memtable size to total permitted size
# that will trigger a flush of the largest memtable. Larger mct will
# mean larger flushes and hence less compaction, but also less concurrent
# flush activity which can make it difficult to keep your disks fed
# under heavy write load.
#
# memtable_cleanup_threshold defaults to 1 / (memtable_flush_writers + 1)
# memtable_cleanup_threshold: 0.11

# Specify the way Cassandra allocates and manages memtable memory.
# Options are:
#
# heap_buffers
#   on heap nio buffers
#
# offheap_buffers
#   off heap (direct) nio buffers
#
# offheap_objects
#    off heap objects
memtable_allocation_type: heap_buffers

# Limit memory usage for Merkle tree calculations during repairs of a certain
# table and common token range. Repair commands targetting multiple tables or
# virtual nodes can exceed this limit depending on concurrent_merkle_tree_requests.
#
# The default is 1/16th of the available heap. The main tradeoff is that
# smaller trees have less resolution, which can lead to over-streaming data.
# If you see heap pressure during repairs, consider lowering this, but you
# cannot go below one mebibyte. If you see lots of over-streaming, consider
# raising this or using subrange repair.
#
# For more details see https://issues.apache.org/jira/browse/CASSANDRA-14096.
#
# Min unit: MiB
# repair_session_space:

# The number of simultaneous Merkle tree requests during repairs that can
# be performed by a repair command. The size of each validation request is
# limited by the repair_session_space property, so setting this to 1 will make
# sure that a repair command doesn't exceed that limit, even if the repair
# command is repairing multiple tables or multiple virtual nodes.
#
# There isn't a limit by default for backwards compatibility, but this can
# produce OOM for  commands repairing multiple tables or multiple virtual nodes.
# A limit of just 1 simultaneous Merkle tree request is generally recommended
# with no virtual nodes so repair_session_space, and thereof the Merkle tree
# resolution, can be high. For virtual nodes a value of 1 with the default
# repair_session_space value will produce higher resolution Merkle trees
# at the expense of speed. Alternatively, when working with virtual nodes it
# can make sense to reduce the repair_session_space and increase the value of
# concurrent_merkle_tree_requests because each range will contain fewer data.
#
# For more details see https://issues.apache.org/jira/browse/CASSANDRA-19336.
#
# A zero value means no limit.
# concurrent_merkle_tree_requests: 0

# Total space to use for commit logs on disk.
#
# If space gets above this value, Cassandra will flush every dirty CF
# in the oldest segment and remove it.  So a small total commitlog space
# will tend to cause more flush activity on less-active columnfamilies.
#
# The default value is the smaller of 8192, and 1/4 of the total space
# of the commitlog volume.
#
commitlog_total_space: 8192MiB

# This sets the number of memtable flush writer threads per disk
# as well as the total number of memtables that can be flushed concurrently.
# These are generally a combination of compute and IO bound.
#
# Memtable flushing is more CPU efficient than memtable ingest and a single thread
# can keep up with the ingest rate of a whole server on a single fast disk
# until it temporarily becomes IO bound under contention typically with compaction.
# At that point you need multiple flush threads. At some point in the future
# it may become CPU bound all the time.
#
# You can tell if flushing is falling behind using the MemtablePool.BlockedOnAllocation
# metric which should be 0, but will be non-zero if threads are blocked waiting on flushing
# to free memory.
#
# memtable_flush_writers defaults to two for a single data directory.
# This means that two  memtables can be flushed concurrently to the single data directory.
# If you have multiple data directories the default is one memtable flushing at a time
# but the flush will use a thread per data directory so you will get two or more writers.
#
# Two is generally enough to flush on a fast disk [array] mounted as a single data directory.
# Adding more flush writers will result in smaller more frequent flushes that introduce more
# compaction overhead.
#
# There is a direct tradeoff between number of memtables that can be flushed concurrently
# and flush size and frequency. More is not better you just need enough flush writers
# to never stall waiting for flushing to free memory.
#
# memtable_flush_writers: 2

# Total space to use for change-data-capture logs on disk.
#
# If space gets above this value, Cassandra will throw WriteTimeoutException
# on Mutations including tables with CDC enabled. A CDCCompactor is responsible
# for parsing the raw CDC logs and deleting them when parsing is completed.
#
# The default value is the min of 4096 MiB and 1/8th of the total space
# of the drive where cdc_raw_directory resides.
# Min unit: MiB
# cdc_total_space: 4096MiB

# When we hit our cdc_raw limit and the CDCCompactor is either running behind
# or experiencing backpressure, we check at the following interval to see if any
# new space for cdc-tracked tables has been made available. Default to 250ms
# Min unit: ms
# cdc_free_space_check_interval: 250ms

# A fixed memory pool size in MB for for SSTable index summaries. If left
# empty, this will default to 5% of the heap size. If the memory usage of
# all index summaries exceeds this limit, SSTables with low read rates will
# shrink their index summaries in order to meet this limit.  However, this
# is a best-effort process. In extreme conditions Cassandra may need to use
# more than this amount of memory.
# Min unit: KiB
index_summary_capacity:

# How frequently index summaries should be resampled.  This is done
# periodically to redistribute memory from the fixed-size pool to sstables
# proportional their recent read rates.  Setting to null value will disable this
# process, leaving existing index summaries at their current sampling level.
# Min unit: m
index_summary_resize_interval: 60m

# Whether to, when doing sequential writing, fsync() at intervals in
# order to force the operating system to flush the dirty
# buffers. Enable this to avoid sudden dirty buffer flushing from
# impacting read latencies. Almost always a good idea on SSDs; not
# necessarily on platters.
trickle_fsync: false
# Min unit: KiB
trickle_fsync_interval: 10240KiB

# TCP port, for commands and data
# For security reasons, you should not expose this port to the internet.  Firewall it if needed.
storage_port: 7000

# SSL port, for legacy encrypted communication. This property is unused unless enabled in
# server_encryption_options (see below). As of cassandra 4.0, this property is deprecated
# as a single port can be used for either/both secure and insecure connections.
# For security reasons, you should not expose this port to the internet. Firewall it if needed.
ssl_storage_port: 7001

# Address or interface to bind to and tell other Cassandra nodes to connect to.
# You _must_ change this if you want multiple nodes to be able to communicate!
#
# Set listen_address OR listen_interface, not both.
#
# Leaving it blank leaves it up to InetAddress.getLocalHost(). This
# will always do the Right Thing _if_ the node is properly configured
# (hostname, name resolution, etc), and the Right Thing is to use the
# address associated with the hostname (it might not be). If unresolvable
# it will fall back to InetAddress.getLoopbackAddress(), which is wrong for production systems.
#
# Setting listen_address to 0.0.0.0 is always wrong.
#
listen_address: localhost

# Set listen_address OR listen_interface, not both. Interfaces must correspond
# to a single address, IP aliasing is not supported.
# listen_interface: eth0

# If you choose to specify the interface by name and the interface has an ipv4 and an ipv6 address
# you can specify which should be chosen using listen_interface_prefer_ipv6. If false the first ipv4
# address will be used. If true the first ipv6 address will be used. Defaults to false preferring
# ipv4. If there is only one address it will be selected regardless of ipv4/ipv6.
# listen_interface_prefer_ipv6: false

# Address to broadcast to other Cassandra nodes
# Leaving this blank will set it to the same value as listen_address
# broadcast_address: 1.2.3.4

# When using multiple physical network interfaces, set this
# to true to listen on broadcast_address in addition to
# the listen_address, allowing nodes to communicate in both
# interfaces.
# Ignore this property if the network configuration automatically
# routes  between the public and private networks such as EC2.
# listen_on_broadcast_address: false

# Internode authentication backend, implementing IInternodeAuthenticator;
# used to allow/disallow connections from peer nodes.
# internode_authenticator: org.apache.cassandra.auth.AllowAllInternodeAuthenticator

# Whether to start the native transport server.
# The address on which the native transport is bound is defined by rpc_address.
start_native_transport: true
# port for the CQL native transport to listen for clients on
# For security reasons, you should not expose this port to the internet.  Firewall it if needed.
native_transport_port: 9042
# Enabling native transport encryption in client_encryption_options allows you to either use
# encryption for the standard port or to use a dedicated, additional port along with the unencrypted
# standard native_transport_port.
# Enabling client encryption and keeping native_transport_port_ssl disabled will use encryption
# for native_transport_port. Setting native_transport_port_ssl to a different value
# from native_transport_port will use encryption for native_transport_port_ssl while
# keeping native_transport_port unencrypted.
# native_transport_port_ssl: 9142
# The maximum threads for handling requests (note that idle threads are stopped
# after 30 seconds so there is not corresponding minimum setting).
# native_transport_max_threads: 128
# The maximum threads for handling auth requests in a separate executor from main request executor.
# When set to 0, main executor for requests is used.
# native_transport_max_auth_threads: 0
#
# The maximum size of allowed frame. Frame (requests) larger than this will
# be rejected as invalid. The default is 16MiB. If you're changing this parameter,
# you may want to adjust max_value_size accordingly. This should be positive and less than 2048.
# Min unit: MiB
# native_transport_max_frame_size: 16MiB

# The maximum number of concurrent client connections.
# The default is -1, which means unlimited.
# native_transport_max_concurrent_connections: -1

# The maximum number of concurrent client connections per source ip.
# The default is -1, which means unlimited.
# native_transport_max_concurrent_connections_per_ip: -1

# Controls whether Cassandra honors older, yet currently supported, protocol versions.
# The default is true, which means all supported protocols will be honored.
native_transport_allow_older_protocols: true

# Controls when idle client connections are closed. Idle connections are ones that had neither reads
# nor writes for a time period.
#
# Clients may implement heartbeats by sending OPTIONS native protocol message after a timeout, which
# will reset idle timeout timer on the server side. To close idle client connections, corresponding
# values for heartbeat intervals have to be set on the client side.
#
# Idle connection timeouts are disabled by default.
# Min unit: ms
# native_transport_idle_timeout: 60000ms

# When enabled, limits the number of native transport requests dispatched for processing per second.
# Behavior once the limit has been breached depends on the value of THROW_ON_OVERLOAD specified in
# the STARTUP message sent by the client during connection establishment. (See section "4.1.1. STARTUP"
# in "CQL BINARY PROTOCOL v5".) With the THROW_ON_OVERLOAD flag enabled, messages that breach the limit
# are dropped, and an OverloadedException is thrown for the client to handle. When the flag is not
# enabled, the server will stop consuming messages from the channel/socket, putting backpressure on
# the client while already dispatched messages are processed.
# native_transport_rate_limiting_enabled: false
# native_transport_max_requests_per_second: 1000000

# The address or interface to bind the native transport server to.
#
# Set rpc_address OR rpc_interface, not both.
#
# Leaving rpc_address blank has the same effect as on listen_address
# (i.e. it will be based on the configured hostname of the node).
#
# Note that unlike listen_address, you can specify 0.0.0.0, but you must also
# set broadcast_rpc_address to a value other than 0.0.0.0.
#
# For security reasons, you should not expose this port to the internet.  Firewall it if needed.
rpc_address: localhost

# Set rpc_address OR rpc_interface, not both. Interfaces must correspond
# to a single address, IP aliasing is not supported.
# rpc_interface: eth1

# If you choose to specify the interface by name and the interface has an ipv4 and an ipv6 address
# you can specify which should be chosen using rpc_interface_prefer_ipv6. If false the first ipv4
# address will be used. If true the first ipv6 address will be used. Defaults to false preferring
# ipv4. If there is only one address it will be selected regardless of ipv4/ipv6.
# rpc_interface_prefer_ipv6: false

# RPC address to broadcast to drivers and other Cassandra nodes. This cannot
# be set to 0.0.0.0. If left blank, this will be set to the value of
# rpc_address. If rpc_address is set to 0.0.0.0, broadcast_rpc_address must
# be set.
# broadcast_rpc_address: 1.2.3.4

# enable or disable keepalive on rpc/native connections
rpc_keepalive: true

# Uncomment to set socket buffer size for internode communication
# Note that when setting this, the buffer size is limited by net.core.wmem_max
# and when not setting it it is defined by net.ipv4.tcp_wmem
# See also:
# /proc/sys/net/core/wmem_max
# /proc/sys/net/core/rmem_max
# /proc/sys/net/ipv4/tcp_wmem
# /proc/sys/net/ipv4/tcp_wmem
# and 'man tcp'
# Min unit: B
# internode_socket_send_buffer_size:

# Uncomment to set socket buffer size for internode communication
# Note that when setting this, the buffer size is limited by net.core.wmem_max
# and when not setting it it is defined by net.ipv4.tcp_wmem
# Min unit: B
# internode_socket_receive_buffer_size:

# Set to true to have Cassandra create a hard link to each sstable
# flushed or streamed locally in a backups/ subdirectory of the
# keyspace data.  Removing these links is the operator's
# responsibility.
incremental_backups: false

# Whether or not to take a snapshot before each compaction.  Be
# careful using this option, since Cassandra won't clean up the
# snapshots for you.  Mostly useful if you're paranoid when there
# is a data format change.
snapshot_before_compaction: false

# Whether or not a snapshot is taken of the data before keyspace truncation
# or dropping of column families. The STRONGLY advised default of true 
# should be used to provide data safety. If you set this flag to false, you will
# lose data on truncation or drop.
auto_snapshot: true

# Adds a time-to-live (TTL) to auto snapshots generated by table
# truncation or drop (when enabled).
# After the TTL is elapsed, the snapshot is automatically cleared.
# By default, auto snapshots *do not* have TTL, uncomment the property below
# to enable TTL on auto snapshots.
# Accepted units: d (days), h (hours) or m (minutes)
# auto_snapshot_ttl: 30d

# The act of creating or clearing a snapshot involves creating or removing
# potentially tens of thousands of links, which can cause significant performance
# impact, especially on consumer grade SSDs. A non-zero value here can
# be used to throttle these links to avoid negative performance impact of
# taking and clearing snapshots
snapshot_links_per_second: 0

# Granularity of the collation index of rows within a partition.
# Increase if your rows are large, or if you have a very large
# number of rows per partition.  The competing goals are these:
#
# - a smaller granularity means more index entries are generated
#   and looking up rows withing the partition by collation column
#   is faster
# - but, Cassandra will keep the collation index in memory for hot
#   rows (as part of the key cache), so a larger granularity means
#   you can cache more hot rows
# Min unit: KiB
column_index_size: 64KiB

# Per sstable indexed key cache entries (the collation index in memory
# mentioned above) exceeding this size will not be held on heap.
# This means that only partition information is held on heap and the
# index entries are read from disk.
#
# Note that this size refers to the size of the
# serialized index information and not the size of the partition.
# Min unit: KiB
column_index_cache_size: 2KiB

# Number of simultaneous compactions to allow, NOT including
# validation "compactions" for anti-entropy repair.  Simultaneous
# compactions can help preserve read performance in a mixed read/write
# workload, by mitigating the tendency of small sstables to accumulate
# during a single long running compactions. The default is usually
# fine and if you experience problems with compaction running too
# slowly or too fast, you should look at
# compaction_throughput first.
#
# concurrent_compactors defaults to the smaller of (number of disks,
# number of cores), with a minimum of 2 and a maximum of 8.
# 
# If your data directories are backed by SSD, you should increase this
# to the number of cores.
# concurrent_compactors: 1

# Number of simultaneous repair validations to allow. If not set or set to
# a value less than 1, it defaults to the value of concurrent_compactors.
# To set a value greeater than concurrent_compactors at startup, the system
# property cassandra.allow_unlimited_concurrent_validations must be set to
# true. To dynamically resize to a value > concurrent_compactors on a running
# node, first call the bypassConcurrentValidatorsLimit method on the
# org.apache.cassandra.db:type=StorageService mbean
# concurrent_validations: 0

# Number of simultaneous materialized view builder tasks to allow.
concurrent_materialized_view_builders: 1

# Throttles compaction to the given total throughput across the entire
# system. The faster you insert data, the faster you need to compact in
# order to keep the sstable count down, but in general, setting this to
# 16 to 32 times the rate you are inserting data is more than sufficient.
# Setting this to 0 disables throttling. Note that this accounts for all types
# of compaction, including validation compaction (building Merkle trees
# for repairs).
compaction_throughput: 64MiB/s

# When compacting, the replacement sstable(s) can be opened before they
# are completely written, and used in place of the prior sstables for
# any range that has been written. This helps to smoothly transfer reads 
# between the sstables, reducing page cache churn and keeping hot rows hot
# Set sstable_preemptive_open_interval to null for disabled which is equivalent to
# sstable_preemptive_open_interval_in_mb being negative
# Min unit: MiB
sstable_preemptive_open_interval: 50MiB

# Starting from 4.1 sstables support UUID based generation identifiers. They are disabled by default
# because once enabled, there is no easy way to downgrade. When the node is restarted with this option
# set to true, each newly created sstable will have a UUID based generation identifier and such files are
# not readable by previous Cassandra versions. At some point, this option will become true by default
# and eventually get removed from the configuration.
uuid_sstable_identifiers_enabled: false

# When enabled, permits Cassandra to zero-copy stream entire eligible
# SSTables between nodes, including every component.
# This speeds up the network transfer significantly subject to
# throttling specified by entire_sstable_stream_throughput_outbound,
# and entire_sstable_inter_dc_stream_throughput_outbound
# for inter-DC transfers.
# Enabling this will reduce the GC pressure on sending and receiving node.
# When unset, the default is enabled. While this feature tries to keep the
# disks balanced, it cannot guarantee it. This feature will be automatically
# disabled if internode encryption is enabled.
# stream_entire_sstables: true

# Throttles entire SSTable outbound streaming file transfers on
# this node to the given total throughput in Mbps.
# Setting this value to 0 it disables throttling.
# When unset, the default is 200 Mbps or 24 MiB/s.
# entire_sstable_stream_throughput_outbound: 24MiB/s

# Throttles entire SSTable file streaming between datacenters.
# Setting this value to 0 disables throttling for entire SSTable inter-DC file streaming.
# When unset, the default is 200 Mbps or 24 MiB/s.
# entire_sstable_inter_dc_stream_throughput_outbound: 24MiB/s

# Throttles all outbound streaming file transfers on this node to the
# given total throughput in Mbps. This is necessary because Cassandra does
# mostly sequential IO when streaming data during bootstrap or repair, which
# can lead to saturating the network connection and degrading rpc performance.
# When unset, the default is 200 Mbps or 24 MiB/s.
# stream_throughput_outbound: 24MiB/s

# Throttles all streaming file transfer between the datacenters,
# this setting allows users to throttle inter dc stream throughput in addition
# to throttling all network stream traffic as configured with
# stream_throughput_outbound_megabits_per_sec
# When unset, the default is 200 Mbps or 24 MiB/s.
# inter_dc_stream_throughput_outbound: 24MiB/s

# Server side timeouts for requests. The server will return a timeout exception
# to the client if it can't complete an operation within the corresponding
# timeout. Those settings are a protection against:
#   1) having client wait on an operation that might never terminate due to some
#      failures.
#   2) operations that use too much CPU/read too much data (leading to memory build
#      up) by putting a limit to how long an operation will execute.
# For this reason, you should avoid putting these settings too high. In other words,
# if you are timing out requests because of underlying resource constraints then
# increasing the timeout will just cause more problems. Of course putting them too
# low is equally ill-advised since clients could get timeouts even for successful
# operations just because the timeout setting is too tight.

# How long the coordinator should wait for read operations to complete.
# Lowest acceptable value is 10 ms.
# Min unit: ms
read_request_timeout: 1800000ms
# How long the coordinator should wait for seq or index scans to complete.
# Lowest acceptable value is 10 ms.
# Min unit: ms
range_request_timeout: 1800000ms
# How long the coordinator should wait for writes to complete.
# Lowest acceptable value is 10 ms.
# Min unit: ms
write_request_timeout: 1800000ms
# How long the coordinator should wait for counter writes to complete.
# Lowest acceptable value is 10 ms.
# Min unit: ms
counter_write_request_timeout: 1800000ms
# How long a coordinator should continue to retry a CAS operation
# that contends with other proposals for the same row.
# Lowest acceptable value is 10 ms.
# Min unit: ms
cas_contention_timeout: 1000ms
# How long the coordinator should wait for truncates to complete
# (This can be much longer, because unless auto_snapshot is disabled
# we need to flush first so we can snapshot before removing the data.)
# Lowest acceptable value is 10 ms.
# Min unit: ms
truncate_request_timeout: 1800000ms
# The default timeout for other, miscellaneous operations.
# Lowest acceptable value is 10 ms.
# Min unit: ms
request_timeout: 1800000ms

# Defensive settings for protecting Cassandra from true network partitions.
# See (CASSANDRA-14358) for details.
#
# The amount of time to wait for internode tcp connections to establish.
# Min unit: ms
# internode_tcp_connect_timeout: 2000ms
#
# The amount of time unacknowledged data is allowed on a connection before we throw out the connection
# Note this is only supported on Linux + epoll, and it appears to behave oddly above a setting of 30000
# (it takes much longer than 30s) as of Linux 4.12. If you want something that high set this to 0
# which picks up the OS default and configure the net.ipv4.tcp_retries2 sysctl to be ~8.
# Min unit: ms
# internode_tcp_user_timeout: 30000ms

# The amount of time unacknowledged data is allowed on a streaming connection.
# The default is 5 minutes. Increase it or set it to 0 in order to increase the timeout.
# Min unit: ms
# internode_streaming_tcp_user_timeout: 300000ms

# Global, per-endpoint and per-connection limits imposed on messages queued for delivery to other nodes
# and waiting to be processed on arrival from other nodes in the cluster.  These limits are applied to the on-wire
# size of the message being sent or received.
#
# The basic per-link limit is consumed in isolation before any endpoint or global limit is imposed.
# Each node-pair has three links: urgent, small and large.  So any given node may have a maximum of
# N*3*(internode_application_send_queue_capacity+internode_application_receive_queue_capacity)
# messages queued without any coordination between them although in practice, with token-aware routing, only RF*tokens
# nodes should need to communicate with significant bandwidth.
#
# The per-endpoint limit is imposed on all messages exceeding the per-link limit, simultaneously with the global limit,
# on all links to or from a single node in the cluster.
# The global limit is imposed on all messages exceeding the per-link limit, simultaneously with the per-endpoint limit,
# on all links to or from any node in the cluster.
#
# Min unit: B
# internode_application_send_queue_capacity: 4MiB
internode_application_send_queue_reserve_endpoint_capacity: 512MiB
# internode_application_send_queue_reserve_global_capacity: 512MiB
# internode_application_receive_queue_capacity: 4MiB
internode_application_receive_queue_reserve_endpoint_capacity: 512MiB
# internode_application_receive_queue_reserve_global_capacity: 512MiB


# How long before a node logs slow queries. Select queries that take longer than
# this timeout to execute, will generate an aggregated log message, so that slow queries
# can be identified. Set this value to zero to disable slow query logging.
# Min unit: ms
slow_query_log_timeout: 500ms

# Enable operation timeout information exchange between nodes to accurately
# measure request timeouts.  If disabled, replicas will assume that requests
# were forwarded to them instantly by the coordinator, which means that
# under overload conditions we will waste that much extra time processing 
# already-timed-out requests.
#
# Warning: It is generally assumed that users have setup NTP on their clusters, and that clocks are modestly in sync, 
# since this is a requirement for general correctness of last write wins.
# internode_timeout: true

# Set period for idle state control messages for earlier detection of failed streams
# This node will send a keep-alive message periodically on the streaming's control channel.
# This ensures that any eventual SocketTimeoutException will occur within 2 keep-alive cycles
# If the node cannot send, or timeouts sending, the keep-alive message on the netty control channel
# the stream session is closed.
# Default value is 300s (5 minutes), which means stalled streams
# are detected within 10 minutes
# Specify 0 to disable.
# Min unit: s
# streaming_keep_alive_period: 300s

# Limit number of connections per host for streaming
# Increase this when you notice that joins are CPU-bound rather that network
# bound (for example a few nodes with big files).
# streaming_connections_per_host: 1

# Settings for stream stats tracking; used by system_views.streaming table
# How long before a stream is evicted from tracking; this impacts both historic and currently running
# streams.
# streaming_state_expires: 3d
# How much memory may be used for tracking before evicting session from tracking; once crossed
# historic and currently running streams maybe impacted.
# streaming_state_size: 40MiB
# Enable/Disable tracking of streaming stats
# streaming_stats_enabled: true

# Allows denying configurable access (rw/rr) to operations on configured ks, table, and partitions, intended for use by
# operators to manage cluster health vs application access. See CASSANDRA-12106 and CEP-13 for more details.
# partition_denylist_enabled: false

# denylist_writes_enabled: true
# denylist_reads_enabled: true
# denylist_range_reads_enabled: true

# The interval at which keys in the cache for denylisting will "expire" and async refresh from the backing DB.
# Note: this serves only as a fail-safe, as the usage pattern is expected to be "mutate state, refresh cache" on any
# changes to the underlying denylist entries. See documentation for details.
# Min unit: s
# denylist_refresh: 600s

# In the event of errors on attempting to load the denylist cache, retry on this interval.
# Min unit: s
# denylist_initial_load_retry: 5s

# We cap the number of denylisted keys allowed per table to keep things from growing unbounded. Nodes will warn above
# this limit while allowing new denylisted keys to be inserted. Denied keys are loaded in natural query / clustering
# ordering by partition key in case of overflow.
# denylist_max_keys_per_table: 1000

# We cap the total number of denylisted keys allowed in the cluster to keep things from growing unbounded.
# Nodes will warn on initial cache load that there are too many keys and be direct the operator to trim down excess
# entries to within the configured limits.
# denylist_max_keys_total: 10000

# Since the denylist in many ways serves to protect the health of the cluster from partitions operators have identified
# as being in a bad state, we usually want more robustness than just CL.ONE on operations to/from these tables to
# ensure that these safeguards are in place. That said, we allow users to configure this if they're so inclined.
# denylist_consistency_level: QUORUM

# phi value that must be reached for a host to be marked down.
# most users should never need to adjust this.
# phi_convict_threshold: 8

# endpoint_snitch -- Set this to a class that implements
# IEndpointSnitch.  The snitch has two functions:
#
# - it teaches Cassandra enough about your network topology to route
#   requests efficiently
# - it allows Cassandra to spread replicas around your cluster to avoid
#   correlated failures. It does this by grouping machines into
#   "datacenters" and "racks."  Cassandra will do its best not to have
#   more than one replica on the same "rack" (which may not actually
#   be a physical location)
#
# CASSANDRA WILL NOT ALLOW YOU TO SWITCH TO AN INCOMPATIBLE SNITCH
# ONCE DATA IS INSERTED INTO THE CLUSTER.  This would cause data loss.
# This means that if you start with the default SimpleSnitch, which
# locates every node on "rack1" in "datacenter1", your only options
# if you need to add another datacenter are GossipingPropertyFileSnitch
# (and the older PFS).  From there, if you want to migrate to an
# incompatible snitch like Ec2Snitch you can do it by adding new nodes
# under Ec2Snitch (which will locate them in a new "datacenter") and
# decommissioning the old ones.
#
# Out of the box, Cassandra provides:
#
# SimpleSnitch:
#    Treats Strategy order as proximity. This can improve cache
#    locality when disabling read repair.  Only appropriate for
#    single-datacenter deployments.
#
# GossipingPropertyFileSnitch
#    This should be your go-to snitch for production use.  The rack
#    and datacenter for the local node are defined in
#    cassandra-rackdc.properties and propagated to other nodes via
#    gossip.  If cassandra-topology.properties exists, it is used as a
#    fallback, allowing migration from the PropertyFileSnitch.
#
# PropertyFileSnitch:
#    Proximity is determined by rack and data center, which are
#    explicitly configured in cassandra-topology.properties.
#
# Ec2Snitch:
#    Appropriate for EC2 deployments in a single Region. Loads Region
#    and Availability Zone information from the EC2 API. The Region is
#    treated as the datacenter, and the Availability Zone as the rack.
#    Only private IPs are used, so this will not work across multiple
#    Regions.
#
# Ec2MultiRegionSnitch:
#    Uses public IPs as broadcast_address to allow cross-region
#    connectivity.  (Thus, you should set seed addresses to the public
#    IP as well.) You will need to open the storage_port or
#    ssl_storage_port on the public IP firewall.  (For intra-Region
#    traffic, Cassandra will switch to the private IP after
#    establishing a connection.)
#
# RackInferringSnitch:
#    Proximity is determined by rack and data center, which are
#    assumed to correspond to the 3rd and 2nd octet of each node's IP
#    address, respectively.  Unless this happens to match your
#    deployment conventions, this is best used as an example of
#    writing a custom Snitch class and is provided in that spirit.
#
# You can use a custom Snitch by setting this to the full class name
# of the snitch, which will be assumed to be on your classpath.
endpoint_snitch: SimpleSnitch

# controls how often to perform the more expensive part of host score
# calculation
# Min unit: ms
dynamic_snitch_update_interval: 100ms
# controls how often to reset all host scores, allowing a bad host to
# possibly recover
# Min unit: ms
dynamic_snitch_reset_interval: 600000ms
# if set greater than zero, this will allow
# 'pinning' of replicas to hosts in order to increase cache capacity.
# The badness threshold will control how much worse the pinned host has to be
# before the dynamic snitch will prefer other replicas over it.  This is
# expressed as a double which represents a percentage.  Thus, a value of
# 0.2 means Cassandra would continue to prefer the static snitch values
# until the pinned host was 20% worse than the fastest.
dynamic_snitch_badness_threshold: 1.0

# Configure server-to-server internode encryption
#
# JVM and netty defaults for supported SSL socket protocols and cipher suites can
# be replaced using custom encryption options. This is not recommended
# unless you have policies in place that dictate certain settings, or
# need to disable vulnerable ciphers or protocols in case the JVM cannot
# be updated.
#
# FIPS compliant settings can be configured at JVM level and should not
# involve changing encryption settings here:
# https://docs.oracle.com/javase/8/docs/technotes/guides/security/jsse/FIPS.html
#
# **NOTE** this default configuration is an insecure configuration. If you need to
# enable server-to-server encryption generate server keystores (and truststores for mutual
# authentication) per:
# http://download.oracle.com/javase/8/docs/technotes/guides/security/jsse/JSSERefGuide.html#CreateKeystore
# Then perform the following configuration changes:
#
# Step 1: Set internode_encryption=<dc|rack|all> and explicitly set optional=true. Restart all nodes
#
# Step 2: Set optional=false (or remove it) and if you generated truststores and want to use mutual
# auth set require_client_auth=true. Restart all nodes
server_encryption_options:
  # On outbound connections, determine which type of peers to securely connect to.
  #   The available options are :
  #     none : Do not encrypt outgoing connections
  #     dc   : Encrypt connections to peers in other datacenters but not within datacenters
  #     rack : Encrypt connections to peers in other racks but not within racks
  #     all  : Always use encrypted connections
  internode_encryption: none
  # When set to true, encrypted and unencrypted connections are allowed on the storage_port
  # This should _only be true_ while in unencrypted or transitional operation
  # optional defaults to true if internode_encryption is none
  # optional: true
  # If enabled, will open up an encrypted listening socket on ssl_storage_port. Should only be used
  # during upgrade to 4.0; otherwise, set to false.
  legacy_ssl_storage_port_enabled: false
  # Set to a valid keystore if internode_encryption is dc, rack or all
  keystore: conf/.keystore
  keystore_password: cassandra
  # Configure the way Cassandra creates SSL contexts.
  # To use PEM-based key material, see org.apache.cassandra.security.PEMBasedSslContextFactory
  # ssl_context_factory:
  #     # Must be an instance of org.apache.cassandra.security.ISslContextFactory
  #     class_name: org.apache.cassandra.security.DefaultSslContextFactory
  # Verify peer server certificates
  require_client_auth: false
  # Set to a valid trustore if require_client_auth is true
  truststore: conf/.truststore
  truststore_password: cassandra
  # Verify that the host name in the certificate matches the connected host
  require_endpoint_verification: false
  # More advanced defaults:
  # protocol: TLS
  # store_type: JKS
  # cipher_suites: [
  #   TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,
  #   TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA,
  #   TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_AES_128_GCM_SHA256, TLS_RSA_WITH_AES_128_CBC_SHA,
  #   TLS_RSA_WITH_AES_256_CBC_SHA
  # ]

# Configure client-to-server encryption.
#
# **NOTE** this default configuration is an insecure configuration. If you need to
# enable client-to-server encryption generate server keystores (and truststores for mutual
# authentication) per:
# http://download.oracle.com/javase/8/docs/technotes/guides/security/jsse/JSSERefGuide.html#CreateKeystore
# Then perform the following configuration changes:
#
# Step 1: Set enabled=true and explicitly set optional=true. Restart all nodes
#
# Step 2: Set optional=false (or remove it) and if you generated truststores and want to use mutual
# auth set require_client_auth=true. Restart all nodes
client_encryption_options:
  # Enable client-to-server encryption
  enabled: false
  # When set to true, encrypted and unencrypted connections are allowed on the native_transport_port
  # This should _only be true_ while in unencrypted or transitional operation
  # optional defaults to true when enabled is false, and false when enabled is true.
  # optional: true
  # Set keystore and keystore_password to valid keystores if enabled is true
  keystore: conf/.keystore
  keystore_password: cassandra
  # Configure the way Cassandra creates SSL contexts.
  # To use PEM-based key material, see org.apache.cassandra.security.PEMBasedSslContextFactory
  # ssl_context_factory:
  #     # Must be an instance of org.apache.cassandra.security.ISslContextFactory
  #     class_name: org.apache.cassandra.security.DefaultSslContextFactory
  # Verify client certificates
  require_client_auth: false
  # Set trustore and truststore_password if require_client_auth is true
  # truststore: conf/.truststore
  # truststore_password: cassandra
  # More advanced defaults:
  # protocol: TLS
  # store_type: JKS
  # cipher_suites: [
  #   TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,
  #   TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA,
  #   TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_AES_128_GCM_SHA256, TLS_RSA_WITH_AES_128_CBC_SHA,
  #   TLS_RSA_WITH_AES_256_CBC_SHA
  # ]

# internode_compression controls whether traffic between nodes is
# compressed.
# Can be:
#
# all
#   all traffic is compressed
#
# dc
#   traffic between different datacenters is compressed
#
# none
#   nothing is compressed.
internode_compression: dc

# Enable or disable tcp_nodelay for inter-dc communication.
# Disabling it will result in larger (but fewer) network packets being sent,
# reducing overhead from the TCP protocol itself, at the cost of increasing
# latency if you block for cross-datacenter responses.
inter_dc_tcp_nodelay: false

# TTL for different trace types used during logging of the repair process.
# Min unit: s
trace_type_query_ttl: 1d
# Min unit: s
trace_type_repair_ttl: 7d

# If unset, all GC Pauses greater than gc_log_threshold will log at
# INFO level
# UDFs (user defined functions) are disabled by default.
# As of Cassandra 3.0 there is a sandbox in place that should prevent execution of evil code.
user_defined_functions_enabled: false

# Enables scripted UDFs (JavaScript UDFs).
# Java UDFs are always enabled, if user_defined_functions_enabled is true.
# Enable this option to be able to use UDFs with "language javascript" or any custom JSR-223 provider.
# This option has no effect, if user_defined_functions_enabled is false.
scripted_user_defined_functions_enabled: false

# Enables encrypting data at-rest (on disk). Different key providers can be plugged in, but the default reads from
# a JCE-style keystore. A single keystore can hold multiple keys, but the one referenced by
# the "key_alias" is the only key that will be used for encrypt opertaions; previously used keys
# can still (and should!) be in the keystore and will be used on decrypt operations
# (to handle the case of key rotation).
#
# It is strongly recommended to download and install Java Cryptography Extension (JCE)
# Unlimited Strength Jurisdiction Policy Files for your version of the JDK.
# (current link: http://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html)
#
# Currently, only the following file types are supported for transparent data encryption, although
# more are coming in future cassandra releases: commitlog, hints
transparent_data_encryption_options:
  enabled: false
  chunk_length_kb: 64
  cipher: AES/CBC/PKCS5Padding
  key_alias: testing:1
  # CBC IV length for AES needs to be 16 bytes (which is also the default size)
  # iv_length: 16
  key_provider:
    - class_name: org.apache.cassandra.security.JKSKeyProvider
      parameters:
        - keystore: conf/.keystore
          keystore_password: cassandra
          store_type: JCEKS
          key_password: cassandra


#####################
# SAFETY THRESHOLDS #
#####################

# When executing a scan, within or across a partition, we need to keep the
# tombstones seen in memory so we can return them to the coordinator, which
# will use them to make sure other replicas also know about the deleted rows.
# With workloads that generate a lot of tombstones, this can cause performance
# problems and even exaust the server heap.
# (http://www.datastax.com/dev/blog/cassandra-anti-patterns-queues-and-queue-like-datasets)
# Adjust the thresholds here if you understand the dangers and want to
# scan more tombstones anyway.  These thresholds may also be adjusted at runtime
# using the StorageService mbean.
tombstone_warn_threshold: 1000
tombstone_failure_threshold: 100000

# Filtering and secondary index queries at read consistency levels above ONE/LOCAL_ONE use a
# mechanism called replica filtering protection to ensure that results from stale replicas do
# not violate consistency. (See CASSANDRA-8272 and CASSANDRA-15907 for more details.) This
# mechanism materializes replica results by partition on-heap at the coordinator. The more possibly
# stale results returned by the replicas, the more rows materialized during the query.
replica_filtering_protection:
    # These thresholds exist to limit the damage severely out-of-date replicas can cause during these
    # queries. They limit the number of rows from all replicas individual index and filtering queries
    # can materialize on-heap to return correct results at the desired read consistency level.
    #
    # "cached_replica_rows_warn_threshold" is the per-query threshold at which a warning will be logged.
    # "cached_replica_rows_fail_threshold" is the per-query threshold at which the query will fail.
    #
    # These thresholds may also be adjusted at runtime using the StorageService mbean.
    #
    # If the failure threshold is breached, it is likely that either the current page/fetch size
    # is too large or one or more replicas is severely out-of-sync and in need of repair.
    cached_rows_warn_threshold: 2000
    cached_rows_fail_threshold: 32000

# Log WARN on any multiple-partition batch size exceeding this value. 5KiB per batch by default.
# Caution should be taken on increasing the size of this threshold as it can lead to node instability.
# Min unit: KiB
batch_size_warn_threshold: 3000KiB

# Fail any multiple-partition batch exceeding this value. 50KiB (10x warn threshold) by default.
# Min unit: KiB
batch_size_fail_threshold: 5000KiB

# Log WARN on any batches not of type LOGGED than span across more partitions than this limit
unlogged_batch_across_partitions_warn_threshold: 10

# Log a warning when compacting partitions larger than this value
compaction_large_partition_warning_threshold: 100MiB

# Log a warning when writing more tombstones than this value to a partition
compaction_tombstone_warning_threshold: 100000

# GC Pauses greater than 200 ms will be logged at INFO level
# This threshold can be adjusted to minimize logging if necessary
# Min unit: ms
# gc_log_threshold: 200ms

# GC Pauses greater than gc_warn_threshold will be logged at WARN level
# Adjust the threshold based on your application throughput requirement. Setting to 0
# will deactivate the feature.
# Min unit: ms
# gc_warn_threshold: 1000ms

# Maximum size of any value in SSTables. Safety measure to detect SSTable corruption
# early. Any value size larger than this threshold will result into marking an SSTable
# as corrupted. This should be positive and less than 2GiB.
# Min unit: MiB
# max_value_size: 256MiB

# ** Impact on keyspace creation **
# If replication factor is not mentioned as part of keyspace creation, default_keyspace_rf would apply.
# Changing this configuration would only take effect for keyspaces created after the change, but does not impact
# existing keyspaces created prior to the change.
# ** Impact on keyspace alter **
# When altering a keyspace from NetworkTopologyStrategy to SimpleStrategy, default_keyspace_rf is applied if rf is not
# explicitly mentioned.
# ** Impact on system keyspaces **
# This would also apply for any system keyspaces that need replication factor.
# A further note about system keyspaces - system_traces and system_distributed keyspaces take RF of 2 or default,
# whichever is higher, and system_auth keyspace takes RF of 1 or default, whichever is higher.
# Suggested value for use in production: 3
# default_keyspace_rf: 1

# Track a metric per keyspace indicating whether replication achieved the ideal consistency
# level for writes without timing out. This is different from the consistency level requested by
# each write which may be lower in order to facilitate availability.
# ideal_consistency_level: EACH_QUORUM

# Automatically upgrade sstables after upgrade - if there is no ordinary compaction to do, the
# oldest non-upgraded sstable will get upgraded to the latest version
# automatic_sstable_upgrade: false
# Limit the number of concurrent sstable upgrades
# max_concurrent_automatic_sstable_upgrades: 1

# Audit logging - Logs every incoming CQL command request, authentication to a node. See the docs
# on audit_logging for full details about the various configuration options.
audit_logging_options:
  enabled: false
  logger:
    - class_name: BinAuditLogger
  # audit_logs_dir:
  # included_keyspaces:
  # excluded_keyspaces: system, system_schema, system_virtual_schema
  # included_categories:
  # excluded_categories:
  # included_users:
  # excluded_users:
  # roll_cycle: HOURLY
  # block: true
  # max_queue_weight: 268435456 # 256 MiB
  # max_log_size: 17179869184 # 16 GiB
  ## archive command is "/path/to/script.sh %path" where %path is replaced with the file being rolled:
  # archive_command:
  # max_archive_retries: 10


# default options for full query logging - these can be overridden from command line when executing
# nodetool enablefullquerylog
# full_query_logging_options:
  # log_dir:
  # roll_cycle: HOURLY
  # block: true
  # max_queue_weight: 268435456 # 256 MiB
  # max_log_size: 17179869184 # 16 GiB
  ## archive command is "/path/to/script.sh %path" where %path is replaced with the file being rolled:
  # archive_command:
  ## note that enabling this allows anyone with JMX/nodetool access to run local shell commands as the user running cassandra
  # allow_nodetool_archive_command: false
  # max_archive_retries: 10

# validate tombstones on reads and compaction
# can be either "disabled", "warn" or "exception"
# corrupted_tombstone_strategy: disabled

# Diagnostic Events #
# If enabled, diagnostic events can be helpful for troubleshooting operational issues. Emitted events contain details
# on internal state and temporal relationships across events, accessible by clients via JMX.
diagnostic_events_enabled: false

# Use native transport TCP message coalescing. If on upgrade to 4.0 you found your throughput decreasing, and in
# particular you run an old kernel or have very fewer client connections, this option might be worth evaluating.
#native_transport_flush_in_batches_legacy: false

# Enable tracking of repaired state of data during reads and comparison between replicas
# Mismatches between the repaired sets of replicas can be characterized as either confirmed
# or unconfirmed. In this context, unconfirmed indicates that the presence of pending repair
# sessions, unrepaired partition tombstones, or some other condition means that the disparity
# cannot be considered conclusive. Confirmed mismatches should be a trigger for investigation
# as they may be indicative of corruption or data loss.
# There are separate flags for range vs partition reads as single partition reads are only tracked
# when CL > 1 and a digest mismatch occurs. Currently, range queries don't use digests so if
# enabled for range reads, all range reads will include repaired data tracking. As this adds
# some overhead, operators may wish to disable it whilst still enabling it for partition reads
repaired_data_tracking_for_range_reads_enabled: false
repaired_data_tracking_for_partition_reads_enabled: false
# If false, only confirmed mismatches will be reported. If true, a separate metric for unconfirmed
# mismatches will also be recorded. This is to avoid potential signal:noise issues are unconfirmed
# mismatches are less actionable than confirmed ones.
report_unconfirmed_repaired_data_mismatches: false

# Having many tables and/or keyspaces negatively affects performance of many operations in the
# cluster. When the number of tables/keyspaces in the cluster exceeds the following thresholds
# a client warning will be sent back to the user when creating a table or keyspace.
# As of cassandra 4.1, these properties are deprecated in favor of keyspaces_warn_threshold and tables_warn_threshold
# table_count_warn_threshold: 150
# keyspace_count_warn_threshold: 40

# configure the read and write consistency levels for modifications to auth tables
# auth_read_consistency_level: LOCAL_QUORUM
# auth_write_consistency_level: EACH_QUORUM

# Delays on auth resolution can lead to a thundering herd problem on reconnects; this option will enable
# warming of auth caches prior to node completing startup. See CASSANDRA-16958
# auth_cache_warming_enabled: false

#########################
# EXPERIMENTAL FEATURES #
#########################

# Enables materialized view creation on this node.
# Materialized views are considered experimental and are not recommended for production use.
materialized_views_enabled: false

# Enables SASI index creation on this node.
# SASI indexes are considered experimental and are not recommended for production use.
sasi_indexes_enabled: false

# Enables creation of transiently replicated keyspaces on this node.
# Transient replication is experimental and is not recommended for production use.
transient_replication_enabled: false

# Enables the used of 'ALTER ... DROP COMPACT STORAGE' statements on this node.
# 'ALTER ... DROP COMPACT STORAGE' is considered experimental and is not recommended for production use.
drop_compact_storage_enabled: false

# Whether or not USE <keyspace> is allowed. This is enabled by default to avoid failure on upgrade.
#use_statements_enabled: true

# When the client triggers a protocol exception or unknown issue (Cassandra bug) we increment
# a client metric showing this; this logic will exclude specific subnets from updating these
# metrics
#client_error_reporting_exclusions:
#  subnets:
#    - 127.0.0.1
#    - 127.0.0.0/31

# Enables read thresholds (warn/fail) across all replicas for reporting back to the client.
# See: CASSANDRA-16850
# read_thresholds_enabled: false # scheduled to be set true in 4.2
# When read_thresholds_enabled: true, this tracks the materialized size of a query on the
# coordinator. If coordinator_read_size_warn_threshold is defined, this will emit a warning
# to clients with details on what query triggered this as well as the size of the result set; if
# coordinator_read_size_fail_threshold is defined, this will fail the query after it
# has exceeded this threshold, returning a read error to the user.
# coordinator_read_size_warn_threshold:
# coordinator_read_size_fail_threshold:
# When read_thresholds_enabled: true, this tracks the size of the local read (as defined by
# heap size), and will warn/fail based off these thresholds; undefined disables these checks.
# local_read_size_warn_threshold:
# local_read_size_fail_threshold:
# When read_thresholds_enabled: true, this tracks the expected memory size of the RowIndexEntry
# and will warn/fail based off these thresholds; undefined disables these checks
# row_index_read_size_warn_threshold:
# row_index_read_size_fail_threshold:

# Guardrail to warn or fail when creating more user keyspaces than threshold.
# The two thresholds default to -1 to disable.
# keyspaces_warn_threshold: -1
# keyspaces_fail_threshold: -1
# Guardrail to warn or fail when creating more user tables than threshold.
# The two thresholds default to -1 to disable.
# tables_warn_threshold: -1
# tables_fail_threshold: -1
# Guardrail to enable or disable the ability to create uncompressed tables
# uncompressed_tables_enabled: true
# Guardrail to warn or fail when creating/altering a table with more columns per table than threshold.
# The two thresholds default to -1 to disable.
# columns_per_table_warn_threshold: -1
# columns_per_table_fail_threshold: -1
# Guardrail to warn or fail when creating more secondary indexes per table than threshold.
# The two thresholds default to -1 to disable.
# secondary_indexes_per_table_warn_threshold: -1
# secondary_indexes_per_table_fail_threshold: -1
# Guardrail to enable or disable the creation of secondary indexes
# secondary_indexes_enabled: true
# Guardrail to warn or fail when creating more materialized views per table than threshold.
# The two thresholds default to -1 to disable.
# materialized_views_per_table_warn_threshold: -1
# materialized_views_per_table_fail_threshold: -1
# Guardrail to warn about, ignore or reject properties when creating tables. By default all properties are allowed.
# table_properties_warned: []
# table_properties_ignored: []
# table_properties_disallowed: []
# Guardrail to allow/disallow user-provided timestamps. Defaults to true.
# user_timestamps_enabled: true
# Guardrail to allow/disallow GROUP BY functionality.
# group_by_enabled: true
# Guardrail to allow/disallow TRUNCATE and DROP TABLE statements
# drop_truncate_table_enabled: true
# Guardrail to warn or fail when using a page size greater than threshold.
# The two thresholds default to -1 to disable.
# page_size_warn_threshold: -1
# page_size_fail_threshold: -1
# Guardrail to allow/disallow list operations that require read before write, i.e. setting list element by index and
# removing list elements by either index or value. Defaults to true.
# read_before_write_list_operations_enabled: true
# Guardrail to warn or fail when querying with an IN restriction selecting more partition keys than threshold.
# The two thresholds default to -1 to disable.
# partition_keys_in_select_warn_threshold: -1
# partition_keys_in_select_fail_threshold: -1
# Guardrail to warn or fail when an IN query creates a cartesian product with a size exceeding threshold,
# eg. "a in (1,2,...10) and b in (1,2...10)" results in cartesian product of 100.
# The two thresholds default to -1 to disable.
# in_select_cartesian_product_warn_threshold: -1
# in_select_cartesian_product_fail_threshold: -1
# Guardrail to warn about or reject read consistency levels. By default, all consistency levels are allowed.
# read_consistency_levels_warned: []
# read_consistency_levels_disallowed: []
# Guardrail to warn about or reject write consistency levels. By default, all consistency levels are allowed.
# write_consistency_levels_warned: []
# write_consistency_levels_disallowed: []
# Guardrail to warn or fail when encountering larger size of collection data than threshold.
# At query time this guardrail is applied only to the collection fragment that is being writen, even though in the case
# of non-frozen collections there could be unaccounted parts of the collection on the sstables. This is done this way to
# prevent read-before-write. The guardrail is also checked at sstable write time to detect large non-frozen collections,
# although in that case exceeding the fail threshold will only log an error message, without interrupting the operation.
# The two thresholds default to null to disable.
# Min unit: B
# collection_size_warn_threshold:
# Min unit: B
# collection_size_fail_threshold:
# Guardrail to warn or fail when encountering more elements in collection than threshold.
# At query time this guardrail is applied only to the collection fragment that is being writen, even though in the case
# of non-frozen collections there could be unaccounted parts of the collection on the sstables. This is done this way to
# prevent read-before-write. The guardrail is also checked at sstable write time to detect large non-frozen collections,
# although in that case exceeding the fail threshold will only log an error message, without interrupting the operation.
# The two thresholds default to -1 to disable.
# items_per_collection_warn_threshold: -1
# items_per_collection_fail_threshold: -1
# Guardrail to allow/disallow querying with ALLOW FILTERING. Defaults to true.
# allow_filtering_enabled: true
# Guardrail to warn or fail when creating a user-defined-type with more fields in than threshold.
# Default -1 to disable.
# fields_per_udt_warn_threshold: -1
# fields_per_udt_fail_threshold: -1
# Guardrail to warn or fail when local data disk usage percentage exceeds threshold. Valid values are in [1, 100].
# This is only used for the disks storing data directories, so it won't count any separate disks used for storing
# the commitlog, hints nor saved caches. The disk usage is the ratio between the amount of space used by the data
# directories and the addition of that same space and the remaining free space on disk. The main purpose of this
# guardrail is rejecting user writes when the disks are over the defined usage percentage, so the writes done by
# background processes such as compaction and streaming don't fail due to a full disk. The limits should be defined
# accordingly to the expected data growth due to those background processes, so for example a compaction strategy
# doubling the size of the data would require to keep the disk usage under 50%.
# The two thresholds default to -1 to disable.
# data_disk_usage_percentage_warn_threshold: -1
# data_disk_usage_percentage_fail_threshold: -1
# Allows defining the max disk size of the data directories when calculating thresholds for
# disk_usage_percentage_warn_threshold and disk_usage_percentage_fail_threshold, so if this is greater than zero they
# become percentages of a fixed size on disk instead of percentages of the physically available disk size. This should
# be useful when we have a large disk and we only want to use a part of it for Cassandra's data directories.
# Valid values are in [1, max available disk size of all data directories].
# Defaults to null to disable and use the physically available disk size of data directories during calculations.
# Min unit: B
# data_disk_usage_max_disk_size:
# Guardrail to warn or fail when the minimum replication factor is lesser than threshold.
# This would also apply to system keyspaces.
# Suggested value for use in production: 2 or higher
# minimum_replication_factor_warn_threshold: -1
# minimum_replication_factor_fail_threshold: -1

# Startup Checks are executed as part of Cassandra startup process, not all of them
# are configurable (so you can disable them) but these which are enumerated bellow.
# Uncomment the startup checks and configure them appropriately to cover your needs.
#
#startup_checks:
# Verifies correct ownership of attached locations on disk at startup. See CASSANDRA-16879 for more details.
#  check_filesystem_ownership:
#    enabled: false
#    ownership_token: "sometoken" # (overriden by "CassandraOwnershipToken" system property)
#    ownership_filename: ".cassandra_fs_ownership" # (overriden by "cassandra.fs_ownership_filename")
# Prevents a node from starting if snitch's data center differs from previous data center.
#  check_dc:
#    enabled: true # (overriden by cassandra.ignore_dc system property)
# Prevents a node from starting if snitch's rack differs from previous rack.
#  check_rack:
#    enabled: true # (overriden by cassandra.ignore_rack system property)
# Enable this property to fail startup if the node is down for longer than gc_grace_seconds, to potentially
# prevent data resurrection on tables with deletes. By default, this will run against all keyspaces and tables
# except the ones specified on excluded_keyspaces and excluded_tables.
#  check_data_resurrection:
#    enabled: false
# file where Cassandra periodically writes the last time it was known to run
#    heartbeat_file: /var/lib/cassandra/data/cassandra-heartbeat
#    excluded_keyspaces: # comma separated list of keyspaces to exclude from the check
#    excluded_tables: # comma separated list of keyspace.table pairs to exclude from the check

````

### ENTRY: helm-charts/configs/cassandra/logback.xml

- bytes: 5098
- crc32: `e9deb2d5`
- decoded_as: `utf-8`

````xml
<!--
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache License, Version 2.0 (the
 "License"); you may not use this file except in compliance
 with the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the License is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the License for the
 specific language governing permissions and limitations
 under the License.
-->

<!--
In order to disable debug.log, comment-out the ASYNCDEBUGLOG
appender reference in the root level section below.
-->

<configuration scan="true" scanPeriod="60 seconds">
  <jmxConfigurator />

  <!-- No shutdown hook; we run it ourselves in StorageService after shutdown -->

  <!-- SYSTEMLOG rolling file appender to system.log (INFO level) -->

  <appender name="SYSTEMLOG" class="ch.qos.logback.core.rolling.RollingFileAppender">
    <filter class="ch.qos.logback.classic.filter.ThresholdFilter">
      <level>INFO</level>
    </filter>
    <file>${cassandra.logdir}/system.log</file>
    <rollingPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy">
      <!-- rollover daily -->
      <fileNamePattern>${cassandra.logdir}/system.log.%d{yyyy-MM-dd}.%i.zip</fileNamePattern>
      <!-- each file should be at most 50MB, keep 7 days worth of history, but at most 5GB -->
      <maxFileSize>50MB</maxFileSize>
      <maxHistory>7</maxHistory>
      <totalSizeCap>5GB</totalSizeCap>
    </rollingPolicy>
    <encoder>
      <pattern>%-5level [%thread] %date{ISO8601} %F:%L - %msg%n</pattern>
    </encoder>
  </appender>

  <!-- DEBUGLOG rolling file appender to debug.log (all levels) -->

  <appender name="DEBUGLOG" class="ch.qos.logback.core.rolling.RollingFileAppender">
    <file>${cassandra.logdir}/debug.log</file>
    <rollingPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy">
      <!-- rollover daily -->
      <fileNamePattern>${cassandra.logdir}/debug.log.%d{yyyy-MM-dd}.%i.zip</fileNamePattern>
      <!-- each file should be at most 50MB, keep 7 days worth of history, but at most 5GB -->
      <maxFileSize>50MB</maxFileSize>
      <maxHistory>7</maxHistory>
      <totalSizeCap>5GB</totalSizeCap>
    </rollingPolicy>
    <encoder>
      <pattern>%-5level [%thread] %date{ISO8601} %F:%L - %msg%n</pattern>
    </encoder>
  </appender>

  <!-- ASYNCLOG assynchronous appender to debug.log (all levels) -->

  <appender name="ASYNCDEBUGLOG" class="ch.qos.logback.classic.AsyncAppender">
    <queueSize>1024</queueSize>
    <discardingThreshold>0</discardingThreshold>
    <includeCallerData>true</includeCallerData>
    <appender-ref ref="DEBUGLOG" />
  </appender>

  <!-- STDOUT console appender to stdout (INFO level) -->

  <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
    <filter class="ch.qos.logback.classic.filter.ThresholdFilter">
      <level>INFO</level>
    </filter>
    <encoder>
      <pattern>%-5level [%thread] %date{ISO8601} %F:%L - %msg%n</pattern>
    </encoder>
  </appender>

  <!-- Uncomment below configuration (Audit Logging (FileAuditLogger) rolling file appender and Audit Logging
  additivity) in order to have the log events flow through separate log file instead of system.log.
  Audit Logging (FileAuditLogger) rolling file appender to audit.log -->
  <!-- <appender name="AUDIT" class="ch.qos.logback.core.rolling.RollingFileAppender">
    <file>${cassandra.logdir}/audit/audit.log</file>
    <rollingPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy"> -->
      <!-- rollover daily -->
      <!-- <fileNamePattern>${cassandra.logdir}/audit/audit.log.%d{yyyy-MM-dd}.%i.zip</fileNamePattern> -->
      <!-- each file should be at most 50MB, keep 30 days worth of history, but at most 5GB -->
      <!-- <maxFileSize>50MB</maxFileSize>
      <maxHistory>30</maxHistory>
      <totalSizeCap>5GB</totalSizeCap>
    </rollingPolicy>
    <encoder>
      <pattern>%-5level [%thread] %date{ISO8601} %F:%L - %msg%n</pattern>
    </encoder>
  </appender> -->

  <!-- Audit Logging additivity to redirect audit logging events to audit/audit.log -->
  <!-- <logger name="org.apache.cassandra.audit" additivity="false" level="INFO">
    <appender-ref ref="AUDIT"/>
  </logger> -->

  <!-- Uncomment bellow and corresponding appender-ref to activate logback metrics
  <appender name="LogbackMetrics" class="com.codahale.metrics.logback.InstrumentedAppender" />
   -->

  <root level="INFO">
    <appender-ref ref="SYSTEMLOG" />
    <appender-ref ref="STDOUT" />
    <appender-ref ref="ASYNCDEBUGLOG" /> <!-- Comment this line to disable debug.log -->
    <!--
    <appender-ref ref="LogbackMetrics" />
    -->
  </root>

  <logger name="org.apache.cassandra" level="DEBUG"/>
</configuration>

````

### ENTRY: helm-charts/configs/ssl/tls.crt

- bytes: 1395
- crc32: `c0109a00`
- decoded_as: `utf-8`

````text
-----BEGIN CERTIFICATE-----
MIID2TCCAsGgAwIBAgIUdB9giFRNKvWO6c2Ob5SksModr5wwDQYJKoZIhvcNAQEL
BQAwfDELMAkGA1UEBhMCTFQxDjAMBgNVBAgMBVN0YXRlMQ0wCwYDVQQHDARDaXR5
MRUwEwYDVQQKDAxPcmdhbml6YXRpb24xEzARBgNVBAsMCkRlcGFydG1lbnQxIjAg
BgNVBAMMGW5tLXdhcDEwNjM5LmRzb25lLjNkcy5jb20wHhcNMjYwNjMwMTAxNjAw
WhcNMjcwNjMwMTAxNjAwWjB8MQswCQYDVQQGEwJMVDEOMAwGA1UECAwFU3RhdGUx
DTALBgNVBAcMBENpdHkxFTATBgNVBAoMDE9yZ2FuaXphdGlvbjETMBEGA1UECwwK
RGVwYXJ0bWVudDEiMCAGA1UEAwwZbm0td2FwMTA2MzkuZHNvbmUuM2RzLmNvbTCC
ASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALhtcAYbV1Rl3pB5zXWge+IY
mVQH6VJs0FWBQqen9M5QcQ9w+Bs9cPcNUsfGxlwMVbDuQVOAis0sgxw13S6Lvb1k
6umm2s559Jl9KC1GcZdmlu90CgsWg14r5M6KgZk+ncHufrMQzDunE8VMA8KOkd5G
L3/8gRsv7DzyEsqB748rThVuz1yN0YbhJsPjxoGSdG3U75P91quvVwUCFj3GxtHG
cvdpjACMAngMGDZ0hzt74kAR9qE1Sr9efYtyvJXvIY0XliAJOfWdC2fI/TVqE466
BuO1d06nBgDac+mpHSAxc5MlSzSoMj7eWBN3WYggk1zneSanMJbUen9OxcfHyWMC
AwEAAaNTMFEwHQYDVR0OBBYEFLW6JYo7fQcdqG23QLTLQNyU36+hMB8GA1UdIwQY
MBaAFLW6JYo7fQcdqG23QLTLQNyU36+hMA8GA1UdEwEB/wQFMAMBAf8wDQYJKoZI
hvcNAQELBQADggEBACZtePBhBjYzBmv8w040oafcqUbkn91pErm40b09FO7W8P1F
T/6dxtvVZ4T0WBJ/KDlBUXWqJJ5htNkclJbT+1Yg6nBRJzvCK8wQvnn3H3CHhkEE
v8JKEF+i9m2zEJ771oXIkW/WnOIon4ln/WqDNwlG83YFwk7zmsSS3mr8rHQOMLjQ
se0LIz4C7VUB2UDYdQNs/16ua+Askf9h1GNmREve9OgBUQ2plFA5TfBUTD3IypxO
cJMO1L3/ZXDHjds1FHqOJds6sPpzhig6EAaIH2vUsAvOnOWW7kAzDrm0919jBSaq
IfBaSlxcwSQnD8PSU4ZQqh4k1mDdDRaEOkzyyoo=
-----END CERTIFICATE-----

````

### ENTRY: helm-charts/configs/ssl/tls.key

- bytes: 1700
- crc32: `9c88cdeb`
- decoded_as: `utf-8`

````text
-----BEGIN PRIVATE KEY-----
MIIEuwIBADANBgkqhkiG9w0BAQEFAASCBKUwggShAgEAAoIBAQC4bXAGG1dUZd6Q
ec11oHviGJlUB+lSbNBVgUKnp/TOUHEPcPgbPXD3DVLHxsZcDFWw7kFTgIrNLIMc
Nd0ui729ZOrpptrOefSZfSgtRnGXZpbvdAoLFoNeK+TOioGZPp3B7n6zEMw7pxPF
TAPCjpHeRi9//IEbL+w88hLKge+PK04Vbs9cjdGG4SbD48aBknRt1O+T/darr1cF
AhY9xsbRxnL3aYwAjAJ4DBg2dIc7e+JAEfahNUq/Xn2LcryV7yGNF5YgCTn1nQtn
yP01ahOOugbjtXdOpwYA2nPpqR0gMXOTJUs0qDI+3lgTd1mIIJNc53kmpzCW1Hp/
TsXHx8ljAgMBAAECgf8SXtRJx29reLoyqe9NSC8O1mRvelpDW5Nk8PsyuAgqhNi+
MQKFtBkMgsc8HxCjGpduiEz5hFRPG5/zr2nYuRKtSuAbZgNljcBPiaf22o12B0IB
mA1oDVYIi1a/PAystw//wUHdlE7DomDVxjyZpJnjChqxJPW3P47Ig1Rb15WFLR/N
puVq9w5s3dXeEPYdThXGdvD7nxRHqtOV1PTGhomeaAYfuOIj/EXWOWxU41Naylrv
DrbzogQo+d3gC/G7HtE7q0pYvuVrP57A8aCORvQ5YcgzUqyHdNmN76lWkDXMAN73
rHsLofFdpwRTTQCBllmI3sExjcifJSMyhBmHvX0CgYEA3i1wALak5DXuB+RyBDvB
UmyejfpudaArCY+xc9VvwviNggGM0I5asz8mCSyrnTmRr/e5B6cD5fBGvaoW8IZL
/ydQ6Z2Y5zS5hjE1Oy8ogOFzFKnjCpm0D5jwkhmdovE3yJBMJfmhT2I0RKlVWvmu
fgJ+t/edTTpGneyQLTTFV40CgYEA1IDUpcpwtzObK5UjKd7AEiPZ2pjuIMfJgiNp
UQQhrREASwJzP1VkYBDFVMBi8ZxbimJSbGAdox97333WFJF/gz3BaxiqHueX1YE6
md8PR16cN6w4E9bHAFX7yvr26gSssFK2h2wWEA3nfQyXLauqvsunGuWqvnZeFV8B
42dwsK8CgYEApPnoaR82YZ8KGSIw56PXcXTmZ1bGHuHIE1l30yNx0bzultK/1T1f
bCo//CAHbsAIxjmUU3JZGqzIWp2qWv/d/qEbG93CZCxqdpKjjEcANHM0GOvtgzmO
0uYl/Na4jv2/BlbftHMgrOmnFjUHBH7Saw8/OSvMykOznCDFDkxZHSECgYAx5GmI
32XlbYViDyrpWrYnzCkLDNrj8WRbXKsObXTmqFY0Rkf+t7LQZz+dbWoNphNMA1es
wEhVE0BHMclAnQSeMLKnzWurw94/L48tr1RsAkeVPqcP6V5hss5iUtgEC8Lrxw+5
7eOkM0+FaZ5ZB7QYBcKfKwsSmsHuLJdJ5/BqWwKBgGOyQdRVVeVaj9isUp2zAbOV
RPue0UNyE5xUY0XRE5IryKJTwlBPTnilsB/5PXJbzCb4SourRaIkT/KdyoFPOqxH
CylTZhV12qSPLXvOPIZrUhILiuzjyOIYBONyakUcIRa9QHEdgaod+WoYo0uuC6VY
TM8sUq5Y7u9NcziXNbDJ
-----END PRIVATE KEY-----

````

### ENTRY: helm-charts/configs/tomcat/catalina.properties

- bytes: 7263
- crc32: `a6e2fded`
- decoded_as: `utf-8`

````text
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#
# List of comma-separated packages that start with or equal this string
# will cause a security exception to be thrown when
# passed to checkPackageAccess unless the
# corresponding RuntimePermission ("accessClassInPackage."+package) has
# been granted.
package.access=sun.,org.apache.catalina.,org.apache.coyote.,org.apache.jasper.,org.apache.tomcat.
#
# List of comma-separated packages that start with or equal this string
# will cause a security exception to be thrown when
# passed to checkPackageDefinition unless the
# corresponding RuntimePermission ("defineClassInPackage."+package) has
# been granted.
#
# by default, no packages are restricted for definition, and none of
# the class loaders supplied with the JDK call checkPackageDefinition.
#
package.definition=sun.,java.,org.apache.catalina.,org.apache.coyote.,\
org.apache.jasper.,org.apache.naming.,org.apache.tomcat.

#
#
# List of comma-separated paths defining the contents of the "common"
# classloader. Prefixes should be used to define what is the repository type.
# Path may be relative to the CATALINA_HOME or CATALINA_BASE path or absolute.
# If left as blank,the JVM system loader will be used as Catalina's "common"
# loader.
# Examples:
#     "foo": Add this folder as a class repository
#     "foo/*.jar": Add all the JARs of the specified folder as class
#                  repositories
#     "foo/bar.jar": Add bar.jar as a class repository
#
# Note: Values are enclosed in double quotes ("...") in case either the
#       ${catalina.base} path or the ${catalina.home} path contains a comma.
#       Because double quotes are used for quoting, the double quote character
#       may not appear in a path.
common.loader="${catalina.base}/lib","${catalina.base}/lib/*.jar","${catalina.home}/lib","${catalina.home}/lib/*.jar"

#
# List of comma-separated paths defining the contents of the "server"
# classloader. Prefixes should be used to define what is the repository type.
# Path may be relative to the CATALINA_HOME or CATALINA_BASE path or absolute.
# If left as blank, the "common" loader will be used as Catalina's "server"
# loader.
# Examples:
#     "foo": Add this folder as a class repository
#     "foo/*.jar": Add all the JARs of the specified folder as class
#                  repositories
#     "foo/bar.jar": Add bar.jar as a class repository
#
# Note: Values may be enclosed in double quotes ("...") in case either the
#       ${catalina.base} path or the ${catalina.home} path contains a comma.
#       Because double quotes are used for quoting, the double quote character
#       may not appear in a path.
server.loader=

#
# List of comma-separated paths defining the contents of the "shared"
# classloader. Prefixes should be used to define what is the repository type.
# Path may be relative to the CATALINA_BASE path or absolute. If left as blank,
# the "common" loader will be used as Catalina's "shared" loader.
# Examples:
#     "foo": Add this folder as a class repository
#     "foo/*.jar": Add all the JARs of the specified folder as class
#                  repositories
#     "foo/bar.jar": Add bar.jar as a class repository
# Please note that for single jars, e.g. bar.jar, you need the URL form
# starting with file:.
#
# Note: Values may be enclosed in double quotes ("...") in case either the
#       ${catalina.base} path or the ${catalina.home} path contains a comma.
#       Because double quotes are used for quoting, the double quote character
#       may not appear in a path.
shared.loader=${catalina.base}/shared/conf

# Default list of JAR files that should not be scanned using the JarScanner
# functionality. This is typically used to scan JARs for configuration
# information. JARs that do not contain such information may be excluded from
# the scan to speed up the scanning process. This is the default list. JARs on
# this list are excluded from all scans. The list must be a comma separated list
# of JAR file names.
# The list of JARs to skip may be over-ridden at a Context level for individual
# scan types by configuring a JarScanner with a nested JarScanFilter.
# The JARs listed below include:
# - Tomcat Bootstrap JARs
# - Tomcat API JARs
# - Catalina JARs
# - Jasper JARs
# - Tomcat JARs
# - Common non-Tomcat JARs
# - Test JARs (JUnit, Cobertura and dependencies)
tomcat.util.scan.StandardJarScanFilter.jarsToSkip=\
bootstrap.jar,commons-daemon.jar,tomcat-juli.jar,\
annotations-api.jar,el-api.jar,jsp-api.jar,servlet-api.jar,websocket-api.jar,\
jaspic-api.jar,\
catalina.jar,catalina-ant.jar,catalina-ha.jar,catalina-storeconfig.jar,\
catalina-tribes.jar,\
jasper.jar,jasper-el.jar,ecj-*.jar,\
tomcat-api.jar,tomcat-util.jar,tomcat-util-scan.jar,tomcat-coyote.jar,\
tomcat-dbcp.jar,tomcat-jni.jar,tomcat-websocket.jar,\
tomcat-i18n-en.jar,tomcat-i18n-es.jar,tomcat-i18n-fr.jar,tomcat-i18n-ja.jar,\
tomcat-juli-adapters.jar,catalina-jmx-remote.jar,catalina-ws.jar,\
tomcat-jdbc.jar,\
tools.jar,\
commons-beanutils*.jar,commons-codec*.jar,commons-collections*.jar,\
commons-dbcp*.jar,commons-digester*.jar,commons-fileupload*.jar,\
commons-httpclient*.jar,commons-io*.jar,commons-lang*.jar,commons-logging*.jar,\
commons-math*.jar,commons-pool*.jar,\
jstl.jar,taglibs-standard-spec-*.jar,\
geronimo-spec-jaxrpc*.jar,wsdl4j*.jar,\
ant.jar,ant-junit*.jar,aspectj*.jar,jmx.jar,h2*.jar,hibernate*.jar,httpclient*.jar,\
jmx-tools.jar,jta*.jar,log4j*.jar,mail*.jar,slf4j*.jar,\
xercesImpl.jar,xmlParserAPIs.jar,xml-apis.jar,\
junit.jar,junit-*.jar,hamcrest-*.jar,easymock-*.jar,cglib-*.jar,\
objenesis-*.jar,ant-launcher.jar,\
cobertura-*.jar,asm-*.jar,dom4j-*.jar,icu4j-*.jar,jaxen-*.jar,jdom-*.jar,\
jetty-*.jar,oro-*.jar,servlet-api-*.jar,tagsoup-*.jar,xmlParserAPIs-*.jar,\
xom-*.jar,\
"${catalina.base}/shared/conf"

# Default list of JAR files that should be scanned that overrides the default
# jarsToSkip list above. This is typically used to include a specific JAR that
# has been excluded by a broad file name pattern in the jarsToSkip list.
# The list of JARs to scan may be over-ridden at a Context level for individual
# scan types by configuring a JarScanner with a nested JarScanFilter.
tomcat.util.scan.StandardJarScanFilter.jarsToScan=\
log4j-web*.jar,log4j-taglib*.jar,log4javascript*.jar,slf4j-taglib*.jar

# String cache configuration.
tomcat.util.buf.StringCache.byte.enabled=true
#tomcat.util.buf.StringCache.char.enabled=true
#tomcat.util.buf.StringCache.trainThreshold=500000
#tomcat.util.buf.StringCache.cacheSize=5000

````

### ENTRY: helm-charts/configs/tomcat/server.xml

- bytes: 9641
- crc32: `c9ad492d`
- decoded_as: `utf-8`

````xml
<?xml version="1.0" encoding="UTF-8"?>
<!--
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
<!-- Note:  A "Server" is not itself a "Container", so you may not
     define subcomponents such as "Valves" at this level.
     Documentation at /docs/config/server.html
 -->
<Server port="-1" shutdown="SHUTDOWN">
    <Listener className="org.apache.catalina.startup.VersionLoggerListener" />
    <!-- Security listener. Documentation at /docs/config/listeners.html
    <Listener className="org.apache.catalina.security.SecurityListener" />
    -->
    <!--APR library loader. Documentation at /docs/apr.html -->
    <Listener className="org.apache.catalina.core.AprLifecycleListener" SSLEngine="on" />
    <!-- Prevent memory leaks due to use of particular java/jakarta APIs-->
    <Listener className="org.apache.catalina.core.JreMemoryLeakPreventionListener" />
    <Listener className="org.apache.catalina.mbeans.GlobalResourcesLifecycleListener" />
    <Listener className="org.apache.catalina.core.ThreadLocalLeakPreventionListener" />

    <!-- Global JNDI resources
         Documentation at /docs/jndi-resources-howto.html
    -->
    <GlobalNamingResources>
        <!-- Editable user database that can also be used by
             UserDatabaseRealm to authenticate users
        -->
        <Resource name="UserDatabase" auth="Container"
                  type="org.apache.catalina.UserDatabase"
                  description="User database that can be updated and saved"
                  factory="org.apache.catalina.users.MemoryUserDatabaseFactory"
                  pathname="conf/tomcat-users.xml" />
    </GlobalNamingResources>

    <!-- A "Service" is a collection of one or more "Connectors" that share
         a single "Container" Note:  A "Service" is not itself a "Container",
         so you may not define subcomponents such as "Valves" at this level.
         Documentation at /docs/config/service.html
     -->
    <Service name="Catalina">

        <!--The connectors can use a shared executor, you can define one or more named thread pools-->
        <!--
        <Executor name="tomcatThreadPool" namePrefix="catalina-exec-"
            maxThreads="150" minSpareThreads="4"/>
        -->


        <!-- A "Connector" represents an endpoint by which requests are received
             and responses are returned. Documentation at :
             Java HTTP Connector: /docs/config/http.html
             Java AJP  Connector: /docs/config/ajp.html
             APR (HTTP/AJP) Connector: /docs/apr.html
             Define a non-SSL/TLS HTTP/1.1 Connector on port 8080
        -->
        <!--Connector  port=""
                       protocol="HTTP/1.1"
                       address=""
                       connectionTimeout="20000"
                       redirectPort="8443"/-->
        <!-- A "Connector" using the shared thread pool-->

        <!--<Connector executor="tomcatThreadPool"
                   port="8080" protocol="HTTP/1.1"
                   connectionTimeout="20000"
                   redirectPort="8443" />-->

        <!-- Define a SSL/TLS HTTP/1.1 Connector on port 8443
             This connector uses the NIO implementation with the JSSE engine. When
             using the JSSE engine, the JSSE configuration attributes must be used.
        -->

        <Connector port="8443" protocol="org.apache.coyote.http11.Http11NioProtocol"
                   sslImplementationName="org.apache.tomcat.util.net.jsse.JSSEImplementation"
                   maxThreads="150" SSLEnabled="true">
            <SSLHostConfig sslProtocol="TLS"
                           protocols="TLSv1.2"
                           honorCipherOrder="true"
                           certificateVerification="none"
                           ciphers="TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384,
                          TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384,
                          TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384,
                          TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384,
                          TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,
                          TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,
                          TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256,
                          TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256,
                          TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384,
                          TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384,
                          TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384,
                          TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384,
                          TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256,
                          TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256,
                          TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256,
                          TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256" >
                <Certificate certificateKeystoreFile="./shared/conf/keystore.p12"
                             certificateKeystorePassword="nomagic"
                             type="RSA" />
            </SSLHostConfig>
        </Connector>

        <!--
        <Connector port="8443" protocol="org.apache.coyote.http11.Http11NioProtocol"
                   maxThreads="150" SSLEnabled="true">
            <SSLHostConfig>
                <Certificate certificateKeystoreFile="conf/localhost-rsa.jks"
                             type="RSA" />
            </SSLHostConfig>
        </Connector>
        -->
        <!-- Define a SSL/TLS HTTP/1.1 Connector on port 8443 with HTTP/2
             This connector uses the APR/native implementation. When using the
             APR/native implementation or the OpenSSL engine with NIO or NIO2 then
             the OpenSSL configuration attributes must be used.
        -->
        <!--
        <Connector port="8443" protocol="org.apache.coyote.http11.Http11AprProtocol"
                   maxThreads="150" SSLEnabled="true" >
            <UpgradeProtocol className="org.apache.coyote.http2.Http2Protocol" />
            <SSLHostConfig>
                <Certificate certificateKeyFile="conf/localhost-rsa-key.pem"
                             certificateFile="conf/localhost-rsa-cert.pem"
                             certificateChainFile="conf/localhost-rsa-chain.pem"
                             type="RSA" />
            </SSLHostConfig>
        </Connector>
        -->

        <!-- Define an AJP 1.3 Connector on port 8009 -->
        <Connector port="8009" protocol="AJP/1.3" secretRequired="false" redirectPort="8443" />


        <!-- An Engine represents the entry point (within Catalina) that processes
             every request.  The Engine implementation for Tomcat stand alone
             analyzes the HTTP headers included with the request, and passes them
             on to the appropriate Host (virtual host).
             Documentation at /docs/config/engine.html -->

        <!-- You should set jvmRoute to support load-balancing via AJP ie :
        <Engine name="Catalina" defaultHost="localhost" jvmRoute="jvm1">
        -->
        <Engine name="Catalina" defaultHost="localhost">

            <!--For clustering, please take a look at documentation at:
                /docs/cluster-howto.html  (simple how to)
                /docs/config/cluster.html (reference documentation) -->
            <!--
            <Cluster className="org.apache.catalina.ha.tcp.SimpleTcpCluster"/>
            -->

            <!-- Use the LockOutRealm to prevent attempts to guess user passwords
                 via a brute-force attack -->
            <Realm className="org.apache.catalina.realm.LockOutRealm">
                <!-- This Realm uses the UserDatabase configured in the global JNDI
                     resources under the key "UserDatabase".  Any edits
                     that are performed against this UserDatabase are immediately
                     available for use by the Realm.  -->
                <Realm className="org.apache.catalina.realm.UserDatabaseRealm"
                       resourceName="UserDatabase"/>
            </Realm>

            <Host name="localhost"  appBase="webapps"
                  unpackWARs="true" autoDeploy="true">

                <!-- SingleSignOn valve, share authentication between web applications
                     Documentation at: /docs/config/valve.html -->
                <!--
                <Valve className="org.apache.catalina.authenticator.SingleSignOn" />
                -->

                <!-- Access log processes all example.
                     Documentation at: /docs/config/valve.html
                     Note: The pattern used is equivalent to using pattern="common" -->
                <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs"
                       prefix="localhost_access_log" suffix=".txt"
                       pattern="%h %l %u %t &quot;%r&quot; %s %b" />

            </Host>
        </Engine>
    </Service>
</Server>

````

### ENTRY: helm-charts/configs/twcloud/ssl/keystore.p12

- bytes: 2830
- crc32: `f986073d`
- sha256: `3972002ce8193668687c1bb28848fc6721a988e9a444d71ff8069205bfe64924`
- payload_status: binary metadata only

### ENTRY: helm-charts/configs/twcloud/application.conf

- bytes: 22614
- crc32: `e2e1706c`
- decoded_as: `utf-8`

````text
akka {

	remote {

		# List of the transport drivers that will be loaded by the remoting.
	    # A list of fully qualified config paths must be provided where
	    # the given configuration path contains a transport-class key
	    # pointing to an implementation class of the Transport interface.
	    # If multiple transports are provided, the address of the first
	    # one will be used as a default address.
	    enabled-transports = ["akka.remote.artery.canonical"]

		# Settings for the failure detector to monitor connections.
	    # For TCP it is not important to have fast failure detection, since
	    # most connection failures are captured by TCP itself.
	    # The default DeadlineFailureDetector will trigger if there are no heartbeats within
	    # the duration heartbeat-interval + acceptable-heartbeat-pause.
		transport-failure-detector {
			# How often keep-alive heartbeat messages should be sent to each connection.
     		heartbeat-interval = 5 s

      		# Number of potentially lost/delayed heartbeats that will be
			# accepted before considering it to be an anomaly.
		    # A margin to the `heartbeat-interval` is important to be able to survive sudden,
		    # occasional, pauses in heartbeat arrivals, due to for example garbage collect or
		    # network drop.
		    acceptable-heartbeat-pause = 55 s
		}

		watch-failure-detector {
			# Defines the failure detector threshold.
		    # A low threshold is prone to generate many wrong suspicions but ensures
		    # a quick detection in the event of a real crash. Conversely, a high
		    # threshold generates fewer mistakes but needs more time to detect
		    # actual crashes.
		    threshold = 12.0
		}

		### Configuration for the Netty based transport drivers
		artery {
			canonical {
 			# The hostname or ip clients should connect to.
 			# If it is not set, it will be set automatically to the IP that can connect to the seed node.
			# hostname = ""

 			# The default remote server port clients should connect to.
      		# Default is 2552 (AKKA), use 0 if you want a random available port
      		# This port needs to be unique for each actor system on the same machine.
			port = 2552
			}

			advanced {
				# Maximum serialized message size, including header data.	
				maximum-frame-size = 25000000b
			}
		}
	}


	cluster {
		# Initial contact points of the cluster.
    	# The nodes to join automatically at startup.
    	# Comma separated full URIs defined by a string on the form of
    	# "akka://system@hostname:port"
		# Can set by system property.
		# e.g. ["akka://twcloud@10.1.1.123:2552","akka://twcloud@10.1.1.124:2552"]
		# The default value depends on the operation mode. In cluster mode, the seed node is mandatory in all nodes.
		# In single server mode, the seed node configuration is optional. It is set to 127.0.0.1 by default at runtime.
		# seed-nodes = ["akka://twcloud@${seed-node.ip}:2552"]

		# how long to wait for one of the seed nodes to reply to initial join request
    	seed-node-timeout = 5s

    	# If a join request fails it will be retried after this period.
    	# Disable join retry by specifying "off".
    	retry-unsuccessful-join-after = 10s

    	# Should the 'leader' in the cluster be allowed to automatically mark
    	# unreachable nodes as DOWN after a configured time of unreachability?
    	# Using auto-down implies that two separate clusters will automatically be
    	# formed in case of network partition.
    	# Disable with "off" or specify a duration to enable auto-down.
    	# If a downing-provider-class is configured this setting is ignored.
    	auto-down-unreachable-after = 10s

    	allow-weakly-up-members = off

		failure-detector {
			# Defines the failure detector threshold.
			# A low threshold is prone to generate many wrong suspicions but ensures
			# a quick detection in the event of a real crash. Conversely, a high
			# threshold generates fewer mistakes but needs more time to detect
			# actual crashes.
			threshold = 8.0

			# How often keep-alive heartbeat messages should be sent to each connection.
      		heartbeat-interval = 5 s

      		# Number of potentially lost/delayed heartbeats that will be
		    # accepted before considering it to be an anomaly.
		    # This margin is important to be able to survive sudden, occasional,
		    # pauses in heartbeat arrivals, due to for example garbage collect or
		    # network drop.
		    acceptable-heartbeat-pause = 60 s

		    # After the heartbeat request has been sent the first failure detection
		    # will start after this period, even though no heartbeat message has
		    # been received.
		    expected-response-after = 2 s
		}
	}
}

esi {

	# Core/max threads to server requests from client in parallel when using multiple-executor
	actor {
		clienthandler-dispatcher {
			multiple-executor {
				pool-size-max = 96
				pool-size-core = 64
			}
		}

        queuecommit-handler-dispatcher {
            multiple-executor {
                pool-size-max = 512
                pool-size-core = 64
            }
         }
	}
	
	config {
		# A decrypt key file
		# Change the file location according your needs
		# decrypt_key_file = "<root_path>/keys/propertiesEncryptionKey"
		
		# An example value printed when start TWC.
		# Put the value from an encryptor here.
		# encrypt_example = "ENC(Deh5EdmaDGWgU0N+2MEtyaJfm1f9QuRcEg==)"
	}

	emf {
		dynamic-load-epackages = true
	}

	net
	{
	    client-socket-worker-pool = 128

		connectors = [
			{
				# The ip address to bind to (for client connection).
				# the default value is bind to all IPs.
				host = "0.0.0.0"

				# Port for client application to connect to. The default value is 3579
				# This is corresponding to the port specified when connecting from client such as MagicDraw
				port = 3579

				protocol = "raw"
			}
		]

		# To support deploy TWCloud in private network but client connect from public network,
		# Specify IP address that will be used by client to connect to this TWCloud from public network
		# This value will be default to esi.net.host if it is empty.
		# server-broadcast-host is not recommended to use.
		# server-broadcast-host = ""
	}
	# Socket read/write timeout
	astyanax.socket-timeout = 60000

	serializer.max-buffersize =  -1

	server {
		# session timeout in milliseconds
		session.timeout = 1800000
		session.maximum-number = 10000
		session.reconnect.timeout = 3600000

		# Delay to kill ClientHandler when the connection lost (is ms).
		# The value of terminate.delay-ms comes from ${esi.server.session.timeout} + 300000
		actor.clienthandler.terminate.delay-ms = 2100000

		# Time in ms that server will retain multi-part responses in memory
		multipart-reply.retention = 100000

		core {
			# Internal TWC load balancer. Set to false to use with an external load balancer or a tunnel environment.
			# load_balancer = true
			
			# The default domain for login.
			# default_domain = "twc"

			licensing.connect {
				# Enabled connection retry
				wait.enabled = true

				# Waiting time in ms before retrying to connect to flex license server
				wait=30000

				# Number of reconnection attempts before resetting license status
				max=20
			}
		}
	}

	# What the server will do for the incoming references to the removed objects when commit
	#
	# 'fix' ->    Server will remove all references automatically from objects
	#             that have references to any removed objects when commit
	#
	# 'reject' -> The commit will be rejected if there have references from objects
	#             to any removed objects but those references are not included in the commit
	#
	# The default is 'fix'.
	#
	# persistence.emf.incoming-ref-behavior = "fix"

	persistence {
		cassandra {
			keyspace {
				replication-factor = 3
			}

			columnfamily {
				# store metadata by eobject id
				metadata.cache-size = 200000

				# store parent of each eobject
				branch.hierarchy.cache-size = 40000

				branch.revisions.cache-size = 40000

				# store eobject instance by eobject id and revision, size is in Megabytes
				data.cache-size = 2000

				# store eobject reference instance by eobject id and revision
				reference.cache-size = 500000

				# store user session, recommended to have session cache size same as max sessions size
				session.cache-size = 10000

				# epackage id and  uri
				epackage-uri.cache-size = 2000

				# store role by role id
				role.cache-size = 1000

				# store commit information of each revision
				commit.cache-size = 2000
			}
		}
		cache {
			# this setting is never use
			uuid = 1000000

			# store ReferenceSlotColumn by byteBuffer of itself
			reference-slot-column = 4000

			# Store username <-> id
			user-id.cache-size=30000

			# store list of resource id and revision by eobject id [with time to live]
			eobject-id-for-revision.cache-size = 30
			eobject-id-for-revision.expire-after-access-time-ms = 9000000

			# store IdAndRev for prevent OutOfMemory [with time to live]
			eobject-id-and-revision-for-revision.cache-size = 5000000
			eobject-id-and-revision-for-revision.expire-after-access-time-ms = 9000000
		}

		threadpool {
			shared-worker {
				pool.size = 128

				# If not specify, default to pool.size
				#queue.size = 128
			}
		}
		cachemanager {
			# Percentage of remaining heap space that will trigger cache eviction
			freeheapspace = 10

			# Interval time for checking available heap
			memory-check-period-ms = 30000

			# The cache with highest used percentage will be selected by cache manager to be cleared.
			# However, if the used percentage of the selected cache is less than this minimum-evict-percent number,
			# cache eviction will be skipped.
			minimum-evict-percent = 3
		}
        branch {
            # How many revisions is contained per branch entry in Branch table. Do not change this after branch is created!
            revision-slot-size = 4096
        }

        announcement {
            seconds-to-keep-expired-announcements = 604800
            check_resource_announcements = true
        }

        queuecommit {
            enable = true

            # How often the tracker should scan for timeout-ed clients. Scans all queues, shouldn't be set low value.
            service-scan-interval-ms = 15000

            # Expected maximum time to wait for heartbeat update from the client.
            client-refresh-heartbeat-ms = 60000

            # Maximum time server will wait for client for this queue when it's waiting to start committing.
            # Time starts when servers starts to process this queue.
            max-client-wait-timeout-ms = 600000

            # Maximum timeout that server will wait for queue to update before sending results back to the client.
            queue-status-update-result-timeout-ms = 10000

            # The minimum time must pass before checking if the client still exists
            client-existence-timeout-ms = 120000

            event-notifier {
                thread-name-prefix = "queueCommitEventListener"

                # maximum unique resource + branch combination able to serve without any wait.
                pool-size-max = 256
            }
        }
	}

	zookeeper {
        # Enable Apache ZooKeeper support for TWCloud service discovery.
        twc {
            enabled = true
            seed.path = "/twc/seeds"
        }

        # Enable Apache ZooKeeper support for TWCloud akka cluster seed management.
        # This helps when running multiple TWCloud instances and when TWCloud IP address changes frequently
        akka {
            # Enable ZooKeeper for TWCloud akka cluster
            enabled = false
            seed.path = "/akka/cluster/seed"
        }

        # Enable ZooKeeper for TWCloud Cassandra seed cluster
        cassandra {
            # Enable Apache ZooKeeper support for TWCloud cassandra seed retrieval.
            enabled = false
            # Should be same as cassandra.yaml config property 'zk_cassandra_seeds_path'
            seed.path = "/cassandra/seeds"
            # Native port on which Cassandra is listening
            native-port = 9042
        }

        # Path to Webapp services discovery on Zookeeper
        webapp.services.path = "/services"

        # Specify Zookeeper contact host:port.
        url = "127.0.0.1:2181"

        # ZooKeeper session timeout
        session-timeout-ms = 15000
        # ZooKeeper connect timeout
        connection-timeout-ms = 10000
        # How many times TWCloud will try to retrieve cassandra seeds from ZooKeeper
        operation-retries = -1

        # Backoff between failed connect attempts
        backoff = 1000
        # retry attempts
        backoff_retries = 3
    }
}

# Specify how many write object commands(except locking) per batch that will be sent to C* at a time.
# Furthermore, server will use thread pool to send batches to C*.
# For single node if the value is more than 1, this may be result in performance improvement.
# But this is 'not always' true for cluster environment and sometime the result is opposite
# which lead to many problems related to timeout. So, we recommend to use value 1 for cluster.
#
# For single C* node, you may use the below configuration to gain some performance.
# esi.persistence.write-batch-size=10000
#
# Default write batch size to 1 to avoid timeout problem in cluster environment
esi.persistence.write-batch-size=1

esi.dm {
	# Enable cross-site request for use with Swagger UI from another host.
	# allow-origin = ["*"]

	# Enable to turn on CSRF protection. This will block all incoming REST API requests, except those, coming from specified
	# IP addresses. List of strings, allowed IP must begin with specified string.
	# csrf.allowed-addresses = ["127.0.0.1", "0.0.0"]
}

# Secure connection with SSL between Cassandra and TWCloud
esi.security {
    cassandra {
        enabled = false
    	keystorePath = "configuration/keystore.p12"
    	keystoreType = "pkcs12"
    	keystorePassword = "nomagic"
    	truststorePath = "configuration/keystore.p12"
        truststoreType = "pkcs12"
        truststorePassword = "nomagic"
        protocol = "TLSv1.2"
    }
}

esi.console {

	## The locations which are used to look up for the web resources.
	## The current look up process will return the first location which is accessible.
	## The default is resources/.
	#template-paths = [
	#	"resources/"
	#	]

	## Space indent in the json response message.
	json-indent = 2

	#
	# Restlet parameters
	restlet {

		# allow listing the Local file reference ("/resources")
		allowListDirectory = false

		## cookie setting maximum age (in second)
		maxCookieAge = 900

		## cleanup expired session. (in second)
		cleanup.interval = 1800

		license {
			# Waiting interval  (millisecond) before retry to connect again
			retry.interval = 5000

			maxRetry = 30
		}

        # Custom response headers which will be returned from the http/https requests
        response-headers = [
                "Strict-Transport-Security: max-age=31536000; includeSubDomains; preload",
                "Content-Security-Policy: default-src=none",
                "X-XSS-Protection: 1; mode=block",
                "X-Content-Type-Options: nosniff",
                "X-Frame-Options: SAMEORIGIN"
        ]
	}



	# proxy server used in reporting issue.
	proxy {
		# Use proxy server or not. Default is false.
		enable = false

		# Proxy server address. Ex. "127.0.0.1"
		address = ""

		# Proxy server port.
		port = 0

		# User for authentication
		authentication-user = ""

		# Password for authentication.
		authentication-password = ""
	}
}

esi.httpd {

	host = "0.0.0.0"

	# REST API port
	port = 8111

	# SSL configuration
	ssl {
		enabled = true
		keystorePath = "configuration/keystore.p12"
		keystoreType = "pkcs12"
		keystorePassword = "nomagic"
		keyPassword = "nomagic"
	}

	socketSendBufferSize = 131072
	socketReceiveBufferSize = 131072
}


esi.persistence.startup {

	# Waiting time in ms before retrying to connect to Cassandra
	cassandra-reconnection-delay = 30000

	# Number of reconnection attempts before shutting down the server
	cassandra-reconnection-attempt = 12
}

esi.persistence.um.allow-external-user-creation-on-successfully-authen = false


# Authentication Server address
esi.auth {
	#
	# Example #1
	# url = "https://127.0.0.1:8443"
	# server-type = "authenserver"

	# Example #2
	# url = "https://3dsx.3ds.com
	# server-type = "direct"

	# Authentication Server base URL.
	url = ""

	# A server type of the authentication URL. It can be "authenserver" or "direct".
	# If server-type is "authenserver", the URL points to a configuration JSON.
	# If server-type is "direct", the URL points to a authorization page. No need to resolve it again.
	server-type = "authenserver"

	# If https is enabled in Authentication server, path to a certificate or a key store is needed
	# The key store format must be JKS or PKCS12.
	https {

	}

	# Authentication server password. Should be the same as authentication.client.secret in webappplatform.properties
	secret = "CHANGE_ME"
}

esi.persistence.reject-write-fail-safe {

	enable = false

	# This option should be used when you set up
	# commit log and data directory for cassandra on the different drive.
	# Furthermore, this option will be ignored if commitlog-and-data-max-used-bytes config is enabled.
	commitlog-max-used-bytes = 0
	data-max-used-bytes = 0

	# This option should be used when you set up
	# commit log and data directory for cassandra on the same drive.
	# Specify value > 0 to enable this option
	# If this option is enabled then commitlog-max-used-bytes and data-max-used-bytes will be ignored.
	commitlog-and-data-max-used-bytes = 0

	# Endpoints to retrieve commit log and data usage information
	endpoint {

		default-jmx-port = 7199
		fetch-interval-ms = 60000

		# Uncomment lines below in case JMX connection to cassandra require authentication
		# username = "admin"
		# password = "password"
	}
}

esi.oslc {
	protocol = "https"
	server = "cc.nomagic.com"
	port = 8443
	path.elements = "/oslc/api/oslc"
	path.rootservices = "/oslc/api"
}

esi.metrics{
	enabled = true
}

esi.ldap {
		# This value will be used for query ldap user account. If it is empty, the default [posixAccount,person,account] will be used.
		userObjectClasses = [posixAccount,person,account]

		# This value will be used for query ldap group account. If it is empty, the default [group,posixGroup,groupOfNames,groupOfUniqueNames] will be used.
		groupObjectClasses =  [group,posixGroup,groupOfNames,groupOfUniqueNames]

		# This value will be used for mapping the TWC attributes (fullname, phone, email, department, description) with Ldap attributes.
		attribute {
				fullname = "cn"

				phone = "mobile"

				email = "mail"

				department = "o"

				description = "description"
		}

		# Used for LDAP servers which end their usernames with "\" character.
		# If LDAP server doesn't allow backslash character usage then leave it as false, otherwise set to true
		allowBackSlashChar = false

		# This value will be used to limit filter size of ldap search. Depend on LDAP server MaxReceiveBuffer size value.
		search-filter-size = 8000000

		# This value should be corresponding to maxSizeLimit of LDAP server configuration and never higher
		search-batch-limit = 250

		# Page size for search results, this configuration keeps responses to ldap server manageable size. Should be not more
		# that configured "search-batch-limit" to make any effect. 0 for turning pagination off in case of the LDAP server does
		# not support pagination.
		search-page-size = 100

        # Reuse LDAP connections via internal connection pool.
        # When enabled:
        #  - Connections are reused per (host, protocol, port, username)
        #  - close() returns the connection to the pool (does not close the socket)
        #  - Reduces TLS handshakes and improves performance
		use-connection-pool = true


        # Follow LDAP referrals returned by the server.
        # Required for:
        #  - Active Directory forests
        #  - Cross-domain searches
        #  - DNS partitions (ForestDnsZones, DomainDnsZones)
        # When disabled, referrals are not resolved automatically and
        # searches may return incomplete results in multi-domain setups.
        # Recommended: true for AD environments
		follow-referrals = true
}

esi.log {
    webhooks {
        # Maximum number of WebhookFiredEvent that can be stored in the event log for each webhook
        max-count-fired-event = 10
    }
}

esi.persistence.datastax-java-driver {
	basic {
		contact-points = [${?CASSANDRA_SEED0}][${?CASSANDRA_SEED1}][${?CASSANDRA_SEED2}]

        request.timeout = 10 minutes
		timeout = 10 minutes

		load-balancing-policy {
			class = DefaultLoadBalancingPolicy
			#class = DcInferringLoadBalancingPolicy
			local-datacenter = datacenter1
			slow-replica-avoidance = true
		}

	}

	advanced {
		reconnect-on-init = true
		reconnection-policy {
			class = ExponentialReconnectionPolicy
			# Waiting time in ms before retrying to connect to Cassandra
			base-delay = 30 seconds
			max-delay = 2 minutes
		}

		retry-policy {
			class = com.nomagic.esi.server.persistence.cassandra.retrypolicy.CQLNativeRetryPolicy
			CQLNativeRetryPolicy {
				max-backoff-time-ms = 180000

				query {
					attempt-times = 3
					backoff-time-ms = 1000
					backoff-mode = "constant"
				}

				request {
					attempt-times = 3
					backoff-time-ms = 1000
					backoff-mode = "constant"
				}

				write {
					backoff-mode = "constant"
					attempt-times = 3
					backoff-time-ms = 1000
				}
			}
		}

		protocol {
			version = V5
		}

		connection {
			connect-timeout = 60 seconds
            init-query-timeout = 60 seconds
            set-keyspace-timeout = 60 seconds
			pool {
				local.size = 3
				remote.size = 3
			}
		}

		auth-provider {
			# Enable this section to enable the cassandra authentication.
			# class = PlainTextAuthProvider
			# username = cassandra
			# password = cassandra
		}
	}
}

# Number of threads use to serve requests from client in parallel
#
akka {
  actor {
    default-dispatcher {
        fork-join-executor {
           parallelism-min = 64
        }
    }
  }
  java-flight-recorder {
    enabled = false
  }
}

# Custom suffix for Elasticsearch index names. Allows for separating indexes of separate TWCloud instances/clusters
# if they are using same Elasticsearch instance. Uncomment and enter a non-empty alphanumeric value to enable.
# NOTE: make sure to set the same suffix for all nodes of the same TWCloud cluster!
#
# esi.query.es.index-name-suffix = "CHANGE_ME"
````

### ENTRY: helm-charts/configs/twcloud/logback.xml

- bytes: 4470
- crc32: `8b0a1e5c`
- decoded_as: `utf-8`

````xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration debug="false" scan="true" scanPeriod="15 seconds">
	<contextName>Teamwork Cloud</contextName>
	<contextListener class="ch.qos.logback.classic.jul.LevelChangePropagator"/>
	
	<appender name="SERVER-CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
		<encoder>
			<pattern>%-5.5level %date{YYYY-MM-dd HH:mm:ss.SSSXXX} %message [%logger{200}, %thread{10}]%n</pattern>
		</encoder>
	</appender>

	<appender name="WEBSERVER-CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
		<encoder>
			<pattern>%-5.5level %date{YYYY-MM-dd HH:mm:ss.SSSXXX} [WEBSERVER] %message [%logger{200}, %thread{10}]%n</pattern>
		</encoder>
	</appender>

	<appender name="SERVER-FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
	    <filter class="com.nomagic.esi.sync.server.logging.InvertedSyncLogFilter"/>
		<file>logs/server.log</file>
		<rollingPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy">
			<fileNamePattern>logs/server.%d{yyyy-MM-dd}.%i.log.zip</fileNamePattern>
			<maxFileSize>50MB</maxFileSize>
			<totalSizeCap>1024MB</totalSizeCap>
		</rollingPolicy>
		<encoder>
		  <pattern>%-5.5level %date{YYYY-MM-dd HH:mm:ss.SSSXXX} %message [%logger{200}, %thread{10}]%n</pattern>
		</encoder>
	</appender>

	<appender name="WEBHOOK-FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>logs/webhook.log</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy">
            <fileNamePattern>logs/webhook.%d{yyyy-MM-dd}.%i.log.zip</fileNamePattern>
            <maxFileSize>50MB</maxFileSize>
            <totalSizeCap>1024MB</totalSizeCap>
        </rollingPolicy>
        <encoder>
            <pattern>%-5.5level %date{YYYY-MM-dd HH:mm:ss.SSSXXX} %X{webhook:-} %X{event:-} %message [%logger{200}, %thread{10}]%n</pattern>
        </encoder>
    </appender>

    <appender name="PROJECT-SYNC-FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <filter class="com.nomagic.esi.sync.server.logging.SyncLogFilter"/>
        <file>logs/project-sync.log</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy">
            <fileNamePattern>logs/project-sync.%d{yyyy-MM-dd}.%i.log.zip</fileNamePattern>
            <maxFileSize>50MB</maxFileSize>
            <totalSizeCap>1024MB</totalSizeCap>
        </rollingPolicy>
        <encoder>
        <pattern>%-5.5level %date{YYYY-MM-dd HH:mm:ss.SSSXXX} %message [%logger{200}, %thread{10}]%n</pattern>
        </encoder>
    </appender>

	<appender name="SERVER-STARTUP-CONFIG-FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
		<file>logs/startup-config.log</file>
		<rollingPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy">
			<fileNamePattern>logs/startup-config.%d{yyyy-MM-dd}.%i.log.zip</fileNamePattern>
			<maxFileSize>50MB</maxFileSize>
			<totalSizeCap>1024MB</totalSizeCap>
		</rollingPolicy>
		<encoder>
		  <pattern>%-5.5level %date{YYYY-MM-dd HH:mm:ss.SSSXXX} %message %n</pattern>
		</encoder>
	</appender>
	
	<appender name="SECURITY-FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
		<file>logs/security.log</file>
		<rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
		<!-- daily rollover -->
			<fileNamePattern>logs/security.%d{yyyy-MM-dd}.log</fileNamePattern>
		</rollingPolicy>
		<encoder>
		  <pattern>%-5.5level %date{YYYY-MM-dd HH:mm:ss.SSSXXX} %message [%logger{200}, %thread{10}]%n</pattern>
		</encoder>
	</appender>

	<root level="WARN">
		<!-- Enable the next line to see the server log output on the console -->
		<!-- <appender-ref ref="SERVER-CONSOLE"/> -->
		<appender-ref ref="SERVER-FILE" />
	</root>

	<logger name="com.nomagic.authentication.client" level="WARN" additivity="false">
    	    <appender-ref ref="SERVER-FILE" />
    </logger>

	<logger name="com.nomagic.esi" level="INFO" additivity="false">
	    <appender-ref ref="SERVER-FILE" />
	    <appender-ref ref="PROJECT-SYNC-FILE"/>
		<!-- Enable the next line to see the server log output on the console -->
		<!-- <appender-ref ref="SERVER-CONSOLE"/> -->
	</logger>

	<logger name="com.nomagic.esi.config.StartupConfigLogger" level="INFO" additivity="false">
		<appender-ref ref="SERVER-STARTUP-CONFIG-FILE" />
	</logger>

	<logger name="WEBHOOKS" level="INFO" additivity="false">
        <appender-ref ref="WEBHOOK-FILE"/>
    </logger>

</configuration>

````

### ENTRY: helm-charts/configs/twcloud/jvm.options

- bytes: 790
- crc32: `64c90d73`
- decoded_as: `utf-8`

````text
-Xmx${TWC_XMX}
-Desi.system.config=configuration/application.conf
-Djavax.xml.parsers.SAXParserFactory=com.sun.org.apache.xerces.internal.jaxp.SAXParserFactoryImpl
-Djavax.xml.parsers.DocumentBuilderFactory=com.sun.org.apache.xerces.internal.jaxp.DocumentBuilderFactoryImpl
-Dlogback.configurationFile=configuration/logback.xml
-Desi.shiro.config=configuration/shiro.ini
-Dfile.encoding=utf-8
-Dcom.sun.management.jmxremote
-Dcom.sun.management.jmxremote.port=2468
-Dcom.sun.management.jmxremote.rmi.port=2468
-Dcom.sun.management.jmxremote.local.only=false
-Dcom.sun.management.jmxremote.authenticate=false
-Dcom.sun.management.jmxremote.ssl=false
-Djdk.util.zip.disableZip64ExtraFieldValidation=true
--add-opens java.base/java.lang=ALL-UNNAMED --add-opens java.base/java.util=ALL-UNNAMED

````

### ENTRY: helm-charts/configs/wap/revision.txt

- bytes: 559
- crc32: `e1573dcf`
- decoded_as: `utf-8`

````text
authentication: 2024xRefresh3HF3-f2d57c04
collaborator: 2024xRefresh3HF3-e60d5859
admin_console: 2024xRefresh3HF3-4e39fcc9
document_exporter: 2024xRefresh3HF3-cf84ac55
element-chooser: 2024xRefresh3HF3-cd55406e
oslc: 2024xRefresh3HF3-35f82843
reports: 2024xRefresh3HF3-c4743cee
resources: 2024xRefresh3HF3-2043a6d5
resource_usage_map: 2024xRefresh3HF3-250908f7
sgi-crawler: 2024xRefresh3HF3-027eadfe
simulation-toolkit-web: 2024xRefresh3HF3-7d83aff2
sysmlv2-api: 2024xRefresh3HF3-4208035c
TWC_client: 2024.3.3.v20260612-1302
webapp: 2024xRefresh3HF3-e0d4a90a

````

### ENTRY: helm-charts/configs/wap/log4j2.properties

- bytes: 2809
- crc32: `4d025206`
- decoded_as: `utf-8`

````text
status = info
name = WebappLog4jProperties

#properties
property.contextName=${serviceNameLookup:defaultApp}
property.logBaseDir=${sys:catalina.base}/logs/webappplatform

#console appender
appender.console.type = Console
appender.console.name = console
appender.console.layout.type = PatternLayout
appender.console.layout.pattern = [%-5level] %d{yyyy-MM-dd HH:mm:ss.SSS} [%t] %c{1} - %msg%n

#file appender
appender.file.type = RollingFile
appender.file.name = file
appender.file.fileName = ${logBaseDir}/${contextName}.log
appender.file.filePattern = ${logBaseDir}/${contextName}-%i.log.gz
appender.file.layout.type = PatternLayout
appender.file.layout.pattern = %d{yyyy-MM-dd HH:mm:ss.SSS} [%-5level] [%t] %c{3} %C{3}.%M(%F:%L) - %m%n
appender.file.policies.type = Policies
appender.file.policies.startup.type = OnStartupTriggeringPolicy
appender.file.policies.size.type = SizeBasedTriggeringPolicy
appender.file.policies.size.size = 100MB
appender.file.strategy.type = DefaultRolloverStrategy
appender.file.strategy.max = 3

#loggers
logger.springframework.name = org.springframework
logger.springframework.level = error
logger.springframework.additivity = false
logger.springframework.appenderRef.file.ref = file

logger.springframeworkJms.name = org.springframework.jms
logger.springframeworkJms.level = off
logger.springframeworkJms.additivity = false
logger.springframeworkJms.appenderRef.file.ref = file

logger.webappplatform.name = com.nomagic.webappplatform
logger.webappplatform.level = error
logger.webappplatform.additivity = false
logger.webappplatform.appenderRef.file.ref = file

logger.opensaml.name = org.opensaml
logger.opensaml.level = off
logger.opensaml.additivity = false
logger.opensaml.appenderRef.file.ref = file

logger.activemq.name = org.apache.activemq.artemis
logger.activemq.level = off
logger.activemq.additivity = false
logger.activemq.appenderRef.file.ref = file

logger.twcRest.name = TWC_REST_LOGGER
logger.twcRest.level = off
logger.twcRest.additivity = false
logger.twcRest.appenderRef.file.ref = file

logger.esi.name = com.nomagic.esi
logger.esi.level = error
logger.esi.additivity = false
logger.esi.appenderRef.file.ref = file

logger.apache.name = org.apache
logger.apache.level = error
logger.apache.additivity = false
logger.apache.appenderRef.file.ref = file

logger.floating.name = FLOATING
logger.floating.level = info
logger.floating.additivity = false
logger.floating.appenderRef.file.ref = file

logger.license.name = LICENSE
logger.license.level = info
logger.license.additivity = false
logger.license.appenderRef.file.ref = file

logger.zookeeper.name = org.apache.zookeeper
logger.zookeeper.level = off
logger.zookeeper.additivity = false
logger.zookeeper.appenderRef.file.ref = file

rootLogger.level = warn
rootLogger.appenderRef.stdout.ref = console

````

### ENTRY: helm-charts/configs/wap/webappplatform.properties

- bytes: 9145
- crc32: `609d480a`
- decoded_as: `utf-8`

````text
#
# General properties
#

install.root=.

#
# Specify the environment where the service is running.
# Possible values are 'standard' or 'cloud'. The default value is 'standard'.
# Specifying the environment will change how services interact with each other.
#
#environment=standard

#
# Web application platform properties
#

# Specify the guest username and password.
# If the guest user comes from a domain, specify it as domain\\user.name
wap.guest.username=Guest
wap.guest.password=Guest

#
# Authentication server properties
#

# Specify the Authentication server location.
# IP address or domain name.
authentication.server.ip=127.0.0.1

# Specify the Authentication server port.
authentication.server.port=8443

# Specify rest protocol (http or https) depending on the Authentication server setup.
authentication.server.protocol=https

# Specify an optional redirect uri if the incoming request does not provide one.
# By default, redirect uri is the authentication server location. Remove # for the property to work.
#authentication.redirect.uri=http://127.0.0.1/webapp/

# Optional value.
# Specify a unique platform ID. The default value is webApplicationPlatform
authentication.client.id=webApplicationPlatform

# Optional value.
# Specify a unique ID that will be used in the remote repository management functionality
authentication.remote.client.id=twcSynchronizationManager

# Optional value.
# Specify the authentication client password that platform will use to secure communication with the Authentication server.
# The default value is CHANGE_ME
authentication.client.secret=CHANGE_ME

# Set to true to ignore Authentication server certificate validation. Otherwise, set to false.
# The value depends on the Authentication server setup.
authentication.server.ignore.certificate=true

#
# Teamwork Cloud server properties
#

# Specify the Teamwork Cloud administrator username and password.
# If the Administrator user comes from a domain, specify it as domain\\user.name
twc.admin.username=Administrator
twc.admin.password=Administrator

# Specify the Teamwork Cloud IP address or domain name.
twc.ip=127.0.0.1

# Specify rest protocol (http or https) depending on the Teamwork Cloud server setup.
twc.rest.protocol=https

# Specify the Teamwork Cloud rest API port.
twc.rest.port=8111

# Specify the Teamwork Cloud client API port.
twc.client.port=3579

# Specify the maximum total number of connections.
twc.client.max.total.connections=20

# Specify the maximum number of connections allowed for a route
twc.client.max.connections.per.route=20

# Specify how many milliseconds to wait for establishing connection
# with the remote server before a timeout exception occurs.
twc.client.connect.timeout.ms=30000

# Specify how many milliseconds to wait for the server to respond
# to various calls before a timeout exception occurs.
twc.client.socket.timeout.ms=120000

# Specify how many milliseconds to wait for checking out a connection
# from the connection pool before an exception occurs.
twc.client.connection.request.timeout.ms=120000

# Set to true to ignore Teamwork Cloud certificate validation. Otherwise, set to false.
twc.client.ignore.certificate=true

# Set to true to enable TLS. Otherwise, set to false.
twc.client.tls=false

# Specify the keystore type, for example, JKS.
#twc.client.keystore.type=JKS

# Specify the full path to the keystore file.
#twc.client.keystore.path=<full.path>

# If the keystore is password-protected, specify the password of the keystore.
#twc.client.keystore.password=<password>

#
# FlexNet/DSLS server properties for Web Application Platform services
#

# Specify if you want to use the FlexNet or DSLS framework (the default value is FlexNet).
#license.framework=FlexNet

# Specify the FlexNet/DSLS license server IP:Port address.
# If the value of the 'license.dsls.server.mode' property is ORGANIZATION_DEFINED, address will be read from the DSLicSrv.txt file.
#license.server=

# If the DSLS framework is used, specifiy the DSLS server mode (ORGANIZATION_DEFINED/CUSTOM).
#license.dsls.server.mode=ORGANIZATION_DEFINED

#
# Platform mailing engine properties used to send notifications via e-mail
#

# Specify the e-mail server host name.
mail.host=gate.company.com

# Specify the e-mail server port. Common ports are: 25, 465, 587.
mail.port=25

#Specify the username and password.
mail.username=anonymous
mail.password=

# Specify the e-mail protocol and encoding.
mail.protocol=smtp
mail.encoding=UTF-8

# Specify the sender's e-mail address.
mail.from.default=info@company.com

#
# Mailing engine TLS secure properties
#

# Set to true if the authentication for SSL/TLS is enabled. If this property is set to true, the 'mail.username' and 'mail.password' properties must be specified as well.
#mail.smtp.auth=true

# Specify the server whose certificate is not trustworthy to bypass it. The value of this property should be the same as the 'mail.host' property, or "*" to bypass all certificates.
#mail.smtp.ssl.trust=gate.company.com

# Set to true if the SSL mailing server is used. A common port is 465.
#mail.smtp.ssl.enable=true

# Set to true if the TLS mailing server is used. Common ports are: 25, 587.
#mail.smtp.starttls.enable=true

#
# Platform service discovery related properties
#

# Specify the Zookeeper server IP address.
zookeeper.server.ip=127.0.0.1
# Specify the Zookeeper server port.
zookeeper.server.port=2181
# Specify zk node where ZooKeeper registers applications
zookeeper.base.service.path=/services
# Enable or disable service discovery. Enabled if the property does not exist
service.discovery.enabled=true
#

# Specify the public URL of service(s),
# for example, http(s)://my.domain:8443/
service.url=/
#
# The service for internal communication can be accessed via service.url or via service.internal.name if environment is set to 'cloud'.
#
# Specify a unique service name.
# NOTE: The default value is <service.name>-service, e.g., webapp-service.
#service.internal.name=
#
# Specify the internal service port, e.g., 8080.
#service.internal.port=
#
# Specify the internal service protocol.
# Possible values are `http` or `https`.
#service.internal.protocol=

# Enables or disables ACLs of ZooKeeper nodes under zookeeper.base.service.path. To use this functionality,
# skipACL must be set to no in the ZooKeeper configuration file, which is <zookeeper-home>/conf/zoo.cfg by default
#zookeeper.acl.enable=false
#zookeeper.acl.username=zkuser
#zookeeper.acl.password=zkpassword
# One of: all, read, write, create, delete, admin. If not set, the all permission will be used
#zookeeper.acl.user.permissions=all

#
# HTTP Client properties
#

# Set to true to ignore certificate validation when one WAP service calls another service. Otherwise, set to false.
http.client.ignore.certificate=true

#
# Messaging related properties.
#

# Set to true if the embedded broker needs to be started when starting the web application platform
messaging.server.start=true
# Specify tcp connection data for messaging
messaging.server.ip=127.0.0.1
messaging.server.port=61616
# If the following property is set to true, then ssl will be used for transmitting data, and
# keystore path and password must be specified.
messaging.server.ssl.enabled=false
# Uncomment and specify path to the server keystore and its password. The keystore can be put to the classpath
# and referenced by the name, or its path can be specified, e.g. file:///E:/keys/keystore.jks or /opt/keys/keystore.jks
# messaging.server.ssl.keystore.path=keystore.jks
# messaging.server.ssl.keystore.password=some_password
#
# If self-signed certificates are used, uncomment and specify a path to the truststore and its password that will be used
# by applications that send and receive messages to and from messaging server.
# messaging.client.ssl.truststore.path=truststore.jks
# messaging.client.ssl.truststore.password=some_password
#
# Defines whether users that can communicate with message server are restricted. If set to true,
# a user for communication needs to be set as shown in the commented line that follows the setting.
messaging.server.security.enabled=false
# messaging.user.name=wap
# messaging.user.password=wap

#
# Export related properties.
#

# Specify how long (in minutes) generated PDF/HTML files will be stored in the Task Manager.
document.exporter.file.storing.time=1440

# Specify path to the Prince executable. May be left empty or commented if the document exporter is not installed
# The path may be absolute or relative to the Web application platform home folder
document.exporter.prince.path=../Prince/lib/prince/bin/prince

# Specify additional conversion using Prince options if needed. The options can be of the form key=value or just a key, separated by a comma,
# e. g. verbose logging can be enabled by providing 'log' and 'verbose' options: document.exporter.prince.options=log=<absolute path to the conversion log>,verbose
# document.exporter.prince.options=

#
# Simulation related properties.
#

# Set to true to enable license checkout for the server-side simulation web application. Otherwise, set to false.
sim.license.checkout=false

````

### ENTRY: helm-charts/configs/wap/log4j2simulation.properties

- bytes: 2250
- crc32: `84a628ec`
- decoded_as: `utf-8`

````text
status = info
name = SimulationWebappLog4jProperties

#properties
property.contextName=${serviceNameLookup:defaultApp}
property.logBaseDir=${sys:catalina.base}/logs/webappplatform

#console appender
appender.console.type = Console
appender.console.name = console
appender.console.layout.type = PatternLayout
appender.console.layout.pattern = [%-5level] %d{yyyy-MM-dd HH:mm:ss.SSS} [%t] %c{1} - %msg%n

#file appender
appender.file.type = RollingFile
appender.file.name = file
appender.file.fileName = ${logBaseDir}/${contextName}.log
appender.file.filePattern = ${logBaseDir}/${contextName}-%i.log.gz
appender.file.layout.type = PatternLayout
appender.file.layout.pattern = %d{yyyy-MM-dd HH:mm:ss.SSS} [%-5level] [%t] %c{3} %C{3}.%M(%F:%L) - %m%n
appender.file.policies.type = Policies
appender.file.policies.startup.type = OnStartupTriggeringPolicy
appender.file.policies.size.type = SizeBasedTriggeringPolicy
appender.file.policies.size.size = 100MB
appender.file.strategy.type = DefaultRolloverStrategy
appender.file.strategy.max = 3

#loggers
logger.springframework.name = org.springframework
logger.springframework.level = warn
logger.springframework.additivity = false
logger.springframework.appenderRef.file.ref = file

logger.webappplatform.name = com.nomagic.webappplatform
logger.webappplatform.level = off
logger.webappplatform.additivity = false
logger.webappplatform.appenderRef.file.ref = file

logger.activemq.name = org.apache.activemq.artemis
logger.activemq.level = error
logger.activemq.additivity = false
logger.activemq.appenderRef.file.ref = file

logger.apache.name = org.apache
logger.apache.level = error
logger.apache.additivity = false
logger.apache.appenderRef.file.ref = file

rootLogger.level = warn
rootLogger.appenderRef.stdout.ref = console

appender.sim.type = SimulationWebLogAppender
appender.sim.name = simulationWebLogAppender
appender.sim.layout.type = PatternLayout
appender.sim.layout.pattern = %d{yyyy-MM-dd HH:mm:ss.SSS} [%-5level] [%t] %c{3} %C{3}.%M(%F:%L) - %m%n

logger.simulation.name = com.dassault_systemes.simulation.log
logger.simulation.level = warn
logger.simulation.additivity = false
logger.simulation.appenderRef.file.ref = file
logger.simulation.appenderRef.sim.ref = simulationWebLogAppender
````

### ENTRY: helm-charts/Chart.lock

- bytes: 1162
- crc32: `e8e62344`
- decoded_as: `utf-8`

````text
dependencies:
- name: kubernetes-ingress
  repository: https://haproxytech.github.io/helm-charts
  version: 1.49.0
- name: zookeeper
  repository: ""
  version: 0.1.3.2
- name: cassandra
  repository: ""
  version: 0.1.3.2
- name: twcloud
  repository: ""
  version: 0.1.3.2
- name: adminconsole
  repository: ""
  version: 0.1.3.2
- name: authentication
  repository: ""
  version: 0.1.3.2
- name: artemis
  repository: ""
  version: 0.1.3.2
- name: collaborator
  repository: ""
  version: 0.1.3.2
- name: docexporter
  repository: ""
  version: 0.1.3.2
- name: oslc
  repository: ""
  version: 0.1.3.2
- name: reports
  repository: ""
  version: 0.1.3.2
- name: resources
  repository: ""
  version: 0.1.3.2
- name: rum
  repository: ""
  version: 0.1.3.2
- name: simulation
  repository: ""
  version: 0.1.3.2
- name: webapp
  repository: ""
  version: 0.1.3.2
- name: sysml2api
  repository: ""
  version: 0.1.3.2
- name: sgicrawler
  repository: ""
  version: 0.1.3.2
- name: elementchooser
  repository: ""
  version: 0.1.3.2
digest: sha256:2141494f30a9fe3eaf58e1001bb0fd4dc00fc67bba75faaa36f48cc866069202
generated: "2026-06-30T14:14:40.862473446+02:00"

````

### ENTRY: helm-charts/wip_ingress.yaml

- bytes: 20098
- crc32: `2dcadd1c`
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
  repoURL: kns-harbor.dsone.3ds.com/

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
  serviceUrl: https://nm-wap10639.dsone.3ds.com/

  # Specify the Authentication server ip address or domain name.
  # Ingress external ip or domain name bind to external ip.
  # MANDATORY !
  # authenticationServerIp: ingress.example.com
  authenticationServerIp: nm-wap10639.dsone.3ds.com
  
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
  licenseServer: kns-dev-nm.dsone.3ds.com:1101

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
    tag: "4.1.8"
  commonLabels: {app: cassandra}
  podLabels: {app: cassandra}
  volumePermissions:
    enabled: false
  persistence:
    enabled: true
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
  enabled: true

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
      enabled: true
      storage: 20Gi
      storageClassName: cassandra-local
      ## Local path that must exist on each node before deploying.
      ## The Cassandra process must have write access to this directory.
      localPath: /pv/multi-cass-cluster
      ## One entry per Cassandra node — PVs will be named cass-vol-cluster-0, -1, -2
      ## Example: - host: host.example.com (keep - host: lines depending on your deployment stragety)
      nodes:
        - host: nm-k8sw1.dsone.3ds.com
        - host: nm-k8sw2.dsone.3ds.com
        - host: nm-k8sw3.dsone.3ds.com

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
    repository: twc/twcloud
    # Specifies image tag name
    tag: 2024xRefresh3HF3-release
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
    repository: webapp/admin-console
    # Specifies image tag name
    tag: 2024xRefresh3HF3-release

# Authentication application settings
authentication:
  # Specifies whether a authentication application should be deployed (Optional)
  enabled: true
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: webapp/authentication
    # Specifies image tag name
    tag: 2024xRefresh3HF3-release
# Sgicrawler application settings
sgicrawler:
  # Specifies whether a Sgicrawler application should be deployed (Mandatory)
  enabled: false
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: webapp/sgi-crawler
    # Specifies image tag name
    tag: 2024xRefresh3HF3-release

# Sysml2-api application settings
sysml2api:
  # Specifies whether a Sysml2-api application should be deployed (Mandatory)
  enabled: false
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: webapp/sysml2-api
    # Specifies image tag name
    tag: 2024xRefresh3HF3-release
# Artemis service settings
artemis:
  # Specifies whether a artemis service should be deployed (Optional)
  # Required for WAP applications: resources, collaborator, document-exporter, simulation.
  enabled: true
  image:
    # Specifies image repository name
    repository: apache/artemis
    # Specifies image tag name (if tag is floating int, then be in quotation marks)
    tag: "2.54.0"

# Collaborator application settings
collaborator:
  # Specifies whether a collaborator application should be deployed
  enabled: true
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: webapp/collaborator
    # Specifies image tag name
    tag: 2024xRefresh3HF3-release

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
    repository: webapp/document-exporter
    # Specifies image tag name
    tag: 2024xRefresh3HF3-release

elementchooser:
  # Specifies whether a element-chooser application should be deployed (Optional)
  enabled: false
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: webapp/element-chooser
    # Specifies image tag name
    tag: 2024xRefresh3HF3-release

# Oslc application settings
oslc:
  # Specifies whether a oslc application should be deployed (Optional)
  enabled: false
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: webapp/oslc
    # Specifies image tag name
    tag: 2024xRefresh3HF3-release

# Reports application settings
reports:
  # Specifies whether a reports application should be deployed (Optional)
  enabled: true
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: webapp/reports
    # Specifies image tag name
    tag: 2024xRefresh3HF3-release

# Resources application settings
resources:
  # Specifies whether a resources application should be deployed (Optional)
  enabled: true
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: webapp/resources
    # Specifies image tag name
    tag: 2024xRefresh3HF3-release

# Resource-usage-map application settings
rum:
  # Specifies whether a resource-usage-map application should be deployed (Optional)
  enabled: true
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: webapp/resource-usage-map
    # Specifies image tag name
    tag: 2024xRefresh3HF3-release

# Simulation application settings
simulation:
  # Specifies whether a simulation application should be deployed (Optional)
  enabled: true
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: webapp/simulation
    # Specifies image tag name
    tag: 2024xRefresh3HF3-release
  startupProbe:
    httpGet:
      # Specifies startup probe protocol, setting depends on your image configuration
      scheme: HTTPS
      # Specifies startup probe port, setting depends on your image configuration
      port: 8443

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
    tag: 2024xRefresh3HF3-release

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
      - host: nm-wap10639.dsone.3ds.com
````

### ENTRY: releaseNotes.txt

- bytes: 252
- crc32: `9d9202d9`
- decoded_as: `utf-8`

````text
TCAS_V: 2024xRefresh3HF3

Changes:
    Replaced Bitnami Zookeeper chart.
    Replaced Bitnami Cassandra chart.
    Replaced retiring ingress-nginx to haproxy ingress.
    Zookeeper version updated to 3.9.5
    Artemis ActiveMQ version updated to 2.54.0
````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "314182760",
  "type": "attachment",
  "status": "current",
  "title": "twc-services-charts-2024xRefresh3HF3.zip",
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
    "when": "2026-07-08T14:44:26.460+02:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/314182760/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/314182760"
    }
  },
  "position": -1,
  "container": {
    "id": "314182206",
    "type": "page",
    "status": "current",
    "title": "Copy of Deployment example on Kubernetes",
    "position": 7,
    "extensions": {
      "position": 7
    },
    "_links": {
      "webui": "/spaces/MCS/pages/314182206/Copy+of+Deployment+example+on+Kubernetes",
      "edit": "/pages/resumedraft.action?draftId=314182206&draftShareId=73e5001b-f32b-4d89-93a3-03a2e641800c",
      "tinyui": "/x/Pgq6Eg",
      "self": "https://docs.nomagic.com/rest/api/content/314182206"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/314182206/child",
      "restrictions": "/rest/api/content/314182206/restriction/byOperation",
      "history": "/rest/api/content/314182206/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/314182206/descendant",
      "space": "/rest/api/space/MCS",
      "relevantViewRestrictions": "/rest/api/content/314182206/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/zip"
  },
  "extensions": {
    "mediaType": "application/zip",
    "fileSize": 191250,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/314182206/twc-services-charts-2024xRefresh3HF3.zip?version=1&modificationDate=1783514666460&api=v2",
    "webui": "/spaces/MCS/pages/314182206/Copy+of+Deployment+example+on+Kubernetes?preview=%2F314182206%2F314182760%2Ftwc-services-charts-2024xRefresh3HF3.zip",
    "self": "https://docs.nomagic.com/rest/api/content/314182760"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/314182760/child",
    "restrictions": "/rest/api/content/314182760/restriction/byOperation",
    "history": "/rest/api/content/314182760/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/314182760/descendant",
    "space": "/rest/api/space/MCS",
    "relevantViewRestrictions": "/rest/api/content/314182760/restriction/relevantViewRestrictions"
  }
}
````
