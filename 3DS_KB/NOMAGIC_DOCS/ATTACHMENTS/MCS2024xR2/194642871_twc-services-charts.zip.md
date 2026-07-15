# NOMAGIC ATTACHMENT: twc-services-charts.zip

- attachment_id: `194642871`
- space_key: `MCS2024xR2`
- parent_page_id: `191924296`
- parent_page_title: Deployment example for Teamwork Cloud with services on Kubernetes
- media_type: `application/zip`
- reported_bytes: 63739
- download_url: https://docs.nomagic.com/download/attachments/191924296/twc-services-charts.zip?version=1&modificationDate=1730800055651&api=v2
- payload_kind: `archive-expanded`
- downloaded_sha256: `6c287d195737153da59051b3d89c9c5c29f7243910a9e1d1dca402b4a1703613`

## ARCHIVE CONTENTS

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

- bytes: 1547
- crc32: `4dec4933`
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

- bytes: 130
- crc32: `f19f3e38`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: adminconsole
description: A Helm chart for admin-console
type: application
version: 0.1.2
appVersion: 1.16.0

````

### ENTRY: helm-charts/charts/artemis/templates/deployment.yaml

- bytes: 393
- crc32: `7957d483`
- decoded_as: `utf-8`

````yaml
{{ if .Values.enabled }}
{{- include "main-template.deployment" . }}
          ports:
          {{- range .Values.containers.ports }}
            - containerPort: {{ .containerPort }}
          {{- end }}
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

- bytes: 1156
- crc32: `523fa921`
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
version: 0.1.2

# This is the version number of the application being deployed. This version number should be
# incremented each time you make changes to the application. Versions are not expected to
# follow Semantic Versioning. They should reflect the version the application is using.
# It is recommended to use it with quotes.
appVersion: "1.16.0"

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

### ENTRY: helm-charts/charts/authentication/values.yaml

- bytes: 1179
- crc32: `e79a6ee5`
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

service:
  type: ClusterIP
  port: 8443
  targetPort: 8443


````

### ENTRY: helm-charts/charts/authentication/Chart.yaml

- bytes: 1150
- crc32: `2b703336`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: authentication
description: A Helm chart for Kubernetes

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
version: 0.1.2

# This is the version number of the application being deployed. This version number should be
# incremented each time you make changes to the application. Versions are not expected to
# follow Semantic Versioning. They should reflect the version the application is using.
# It is recommended to use it with quotes.
appVersion: "1.16.0"

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

### ENTRY: helm-charts/charts/collaborator/values.yaml

- bytes: 1704
- crc32: `391d7a28`
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
    -Dlicense.server={{ .Values.global.licenseServer }}
    -Dlicense.framework={{ .Values.global.licenseFramework }}

service:
  type: ClusterIP
  port: 8443
  targetPort: 8443


````

### ENTRY: helm-charts/charts/collaborator/Chart.yaml

- bytes: 1148
- crc32: `889f5086`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: collaborator
description: A Helm chart for Kubernetes

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
version: 0.1.2

# This is the version number of the application being deployed. This version number should be
# incremented each time you make changes to the application. Versions are not expected to
# follow Semantic Versioning. They should reflect the version the application is using.
# It is recommended to use it with quotes.
appVersion: "1.16.0"

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

- bytes: 1147
- crc32: `8a1c5f51`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: docexporter
description: A Helm chart for Kubernetes

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
version: 0.1.2

# This is the version number of the application being deployed. This version number should be
# incremented each time you make changes to the application. Versions are not expected to
# follow Semantic Versioning. They should reflect the version the application is using.
# It is recommended to use it with quotes.
appVersion: "1.16.0"

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

- bytes: 1578
- crc32: `da0a4f1a`
- decoded_as: `utf-8`

````yaml
appName: oslc-deployment
appLabel: oslc
svcName: oslc-service
ident: wap

replicaCount: 1

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

- bytes: 1140
- crc32: `8431a56d`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: oslc
description: A Helm chart for Kubernetes

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
version: 0.1.2

# This is the version number of the application being deployed. This version number should be
# incremented each time you make changes to the application. Versions are not expected to
# follow Semantic Versioning. They should reflect the version the application is using.
# It is recommended to use it with quotes.
appVersion: "1.16.0"

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

- bytes: 1143
- crc32: `9295549e`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: reports
description: A Helm chart for Kubernetes

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
version: 0.1.2

# This is the version number of the application being deployed. This version number should be
# incremented each time you make changes to the application. Versions are not expected to
# follow Semantic Versioning. They should reflect the version the application is using.
# It is recommended to use it with quotes.
appVersion: "1.16.0"

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

- bytes: 1145
- crc32: `c6a43602`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: resources
description: A Helm chart for Kubernetes

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
version: 0.1.2

# This is the version number of the application being deployed. This version number should be
# incremented each time you make changes to the application. Versions are not expected to
# follow Semantic Versioning. They should reflect the version the application is using.
# It is recommended to use it with quotes.
appVersion: "1.16.0"

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

- bytes: 1139
- crc32: `e97ce6ea`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: rum
description: A Helm chart for Kubernetes

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
version: 0.1.2

# This is the version number of the application being deployed. This version number should be
# incremented each time you make changes to the application. Versions are not expected to
# follow Semantic Versioning. They should reflect the version the application is using.
# It is recommended to use it with quotes.
appVersion: "1.16.0"

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

### ENTRY: helm-charts/charts/simulation/values.yaml

- bytes: 1792
- crc32: `9954df60`
- decoded_as: `utf-8`

````yaml
appName: simulation-deployment
appJobName: simulation-job
appLabel: simulation
svcName: simulation-service
ident: wap

# Specifies that local TWCloud is used (default true).
twcBuiltIn: true

maxReplicaCount: 100
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
    -Dlicense.server={{ .Values.global.licenseServer }}
    -Dlicense.framework={{ .Values.global.licenseFramework }}
    -Dsim.license.checkout=true

service:
  type: ClusterIP
  port: 8443
  targetPort: 8443

````

### ENTRY: helm-charts/charts/simulation/Chart.yaml

- bytes: 1146
- crc32: `dceb82ae`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: simulation
description: A Helm chart for Kubernetes

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
version: 0.1.2

# This is the version number of the application being deployed. This version number should be
# incremented each time you make changes to the application. Versions are not expected to
# follow Semantic Versioning. They should reflect the version the application is using.
# It is recommended to use it with quotes.
appVersion: "1.16.0"

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

- bytes: 4361
- crc32: `26a1a58d`
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

### ENTRY: helm-charts/charts/twcloud/values.yaml

- bytes: 600
- crc32: `3b90e3c9`
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
    -Desi.zookeeper.server.ip={{ .Release.Name }}-zookeeper    
    -Desi.net.connectors.0.host=$(POD_IP)
    -Desi.net.connectors.0.port=3579
    -Desi.net.connectors.0.protocol=raw
    -Desi.persistence.cassandra-access-lock.skip-lock-validation=true
    -Desi.zookeeper.akka.enabled=true
    -Desi.server.env.kubernetes=true

````

### ENTRY: helm-charts/charts/twcloud/Chart.yaml

- bytes: 1143
- crc32: `a656c8f9`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: twcloud
description: A Helm chart for Kubernetes

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
version: 0.1.2

# This is the version number of the application being deployed. This version number should be
# incremented each time you make changes to the application. Versions are not expected to
# follow Semantic Versioning. They should reflect the version the application is using.
# It is recommended to use it with quotes.
appVersion: "1.16.0"

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

- bytes: 1288
- crc32: `c36fde8d`
- decoded_as: `utf-8`

````yaml
appName: webapp-deployment
appLabel: webapp
svcName: webapp-service
ident: wap
fullnameOverride: webapp

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

- bytes: 1142
- crc32: `017c1909`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: webapp
description: A Helm chart for Kubernetes

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
version: 0.1.2

# This is the version number of the application being deployed. This version number should be
# incremented each time you make changes to the application. Versions are not expected to
# follow Semantic Versioning. They should reflect the version the application is using.
# It is recommended to use it with quotes.
appVersion: "1.16.0"

````

### ENTRY: helm-charts/charts/sgicrawler/Chart.yaml

- bytes: 1146
- crc32: `b282f640`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: sgicrawler
description: A Helm chart for Kubernetes

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
version: 0.1.2

# This is the version number of the application being deployed. This version number should be
# incremented each time you make changes to the application. Versions are not expected to
# follow Semantic Versioning. They should reflect the version the application is using.
# It is recommended to use it with quotes.
appVersion: "1.16.0"

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

- bytes: 1145
- crc32: `4fe5b032`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: sysml2api
description: A Helm chart for Kubernetes

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
version: 0.1.2

# This is the version number of the application being deployed. This version number should be
# incremented each time you make changes to the application. Versions are not expected to
# follow Semantic Versioning. They should reflect the version the application is using.
# It is recommended to use it with quotes.
appVersion: "1.16.0"

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

- bytes: 4567
- crc32: `9e93e30d`
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
      {{- with .Values.podAnnotations }}
      annotations:
        {{- toYaml . | nindent 8 }}
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
      {{- if .Values.global.twcBuiltIn }}
      {{- include "main-template.init-container" . }}
          {{- end }}
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

- bytes: 3880
- crc32: `ac9541d3`
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
{{- define "main-template.fullname" -}}
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
          image: bitnami/kubectl          
          command: ['bash', '-c', "kubectl get -n {{ .Release.Namespace }} configmap {{ .Release.Name }}-cassandra-seeds >/dev/null 2>&1 && kubectl delete -n {{ .Release.Namespace }} configmap {{ .Release.Name }}-cassandra-seeds; seeds=$(kubectl get pod {{ .Release.Name }}-cassandra-0 -o jsonpath='{.spec.containers[0].env[?(@.name==\"CASSANDRA_SEEDS\")].value}' | awk -F, '{for(i=1;i<=NF;i++) printf \"%s:9042%s\", $i, (i==NF ? ORS : FS)}'); IFS=','; read -ra entries <<< \"$seeds\"; for ((i=0; i<${#entries[@]}; i++)); do varname=\"CASSANDRA_SEED$i\"; declare \"$varname\"=\"${entries[$i]}\"; echo \"$varname=${!varname}\"; done >/tmp/seeds; kubectl create -n {{ .Release.Namespace }} configmap {{ .Release.Name }}-cassandra-seeds --from-env-file=/tmp/seeds"]
        {{- end }}
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

- bytes: 742
- crc32: `cea3cc29`
- decoded_as: `utf-8`

````text
{{ define "main-initcontainer" }}
{{ if .Values.twcloud.enabled }}
      initContainers:
      - name: init-twcloud
        image: busybox:1.28
        command: ['sh', '-c', "until nslookup {{ include "main-template.fullname" . }}-service.$(cat /var/run/secrets/kubernetes.io/serviceaccount/namespace).svc.cluster.local; do echo waiting for {{ include "main-template.fullname" . }}-service; sleep 2; done"]
      - name: init-twcloud-configmap
        image: bitnami/kubectl
        command: ['sh', '-c', 'kubectl create cm webapp-cassandra-seeds --from-literal CASSANDRA_SEEDS=$(kubectl get pod webapp-cassandra-0 -o json | jq '.spec.containers[0].env[] | select(.name == "CASSANDRA_SEEDS").value' | tr -d '"')']
      {{- end }}
{{- end  }}
````

### ENTRY: helm-charts/templates/_job.tpl

- bytes: 3161
- crc32: `88362b3c`
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
  maxReplicaCount: {{ .Values.maxReplicaCount | default 50 }}
  pollingInterval: {{ .Values.pollingInterval | default 1 }}
  jobTargetRef:
    completions: 1
    template:
      metadata:
        labels:
          jobgroup: {{ .Values.appLabel }}
      spec:
        containers:
          - name: {{ .Chart.Name }}
            image: "{{ .Values.global.repoURL }}{{ .Values.image.repository }}:{{ .Values.image.tag }}"
            imagePullPolicy: {{ .Values.global.pullPolicy }}
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
                          -Dtwc.ip={{ .Values.global.twcIp }}
                          -Dtwc.rest.port={{ .Values.global.twcRestPort }}
                          -Dzookeeper.server.ip={{ .Values.global.zookeeperServerIp }}
                          -Dservice.uri={{ .Values.global.serviceUri }}
                          -Dauthentication.server.ip={{ .Values.global.authenticationServerIp }}
                          -Dauthentication.server.port={{ .Values.global.authenticationServerPort }}
                          -Dauthentication.server.protocol={{ .Values.global.authenticationServerProtocol }}
                          -Dauthentication.client.secret={{ .Values.global.authenticationClientSecret }}                        
                          -Dlicense.server.name={{ .Values.global.licenseServerName }}
                          -Dlicense.server.port={{ .Values.global.licenseServerPort }}
                          -Dmessaging.server.ip={{ .Release.Name }}-artemis
                          -Dmessaging.server.port={{ .Values.global.messagingServerPort }}
                          -Dmessaging.server.security.enabled={{ .Values.global.messagingServerSecurityEnabled }}
                          -Dmessaging.user.name={{ .Values.global.activeMqUserName }}
                          -Dmessaging.user.password={{ .Values.global.activeMqPassword }}
                          -Dsim.license.checkout=true"
            ports:
              - name: {{ include "main-template.name" . }}
                containerPort: {{ .Values.service.port }}
                protocol: TCP
  triggers:
    - type: artemis-queue
      metadata:
        managementEndpoint: "{{ .Release.Name }}-artemis:8161"
        queueName: "jms!/sim!/QueueRun"
        brokerName: "0.0.0.0"
        brokerAddress: "jms!/sim!/QueueRun"
        username: {{ .Values.global.activeMqUserName }}
        password: {{ .Values.global.activeMqPassword }}
        queueLength: '1'
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

- bytes: 932
- crc32: `b8b7bf5b`
- decoded_as: `utf-8`

````yaml
{{ if .Values.persistentVolumes.enabled }}
{{ range .Values.persistentVolumes.workers }}
apiVersion: v1
kind: PersistentVolume
metadata:
  name: {{ $.Values.persistentVolumes.name }}-{{ .host }}
spec:
  capacity:
    storage: {{ $.Values.persistentVolumes.storage }}
  volumeMode: {{ $.Values.persistentVolumes.volumeMode }}
  accessModes:
    - {{ $.Values.persistentVolumes.accessModes }}
  persistentVolumeReclaimPolicy: {{ $.Values.persistentVolumes.persistentVolumeReclaimPolicy }}
  storageClassName: {{ $.Values.persistentVolumes.storageClassName }}
  local:
    path: {{ $.Values.persistentVolumes.localPath }}
  nodeAffinity:
    required:
      nodeSelectorTerms:
        - matchExpressions:
            - key: {{ $.Values.persistentVolumes.matchExpressionsKey }}
              operator: {{ $.Values.persistentVolumes.matchExpressionsOperator }}
              values:
                - {{ .host }}
---
{{- end }}
{{ end }}
````

### ENTRY: helm-charts/templates/rbac.yaml

- bytes: 1822
- crc32: `6a00d80a`
- decoded_as: `utf-8`

````yaml
---
apiVersion: v1
kind: ServiceAccount
metadata:
  annotations:
    kubernetes.io/enforce-mountable-secrets: "true"
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

- bytes: 235
- crc32: `54330789`
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

- bytes: 2648
- crc32: `0e151344`
- decoded_as: `utf-8`

````text
Thank you for installing Teamwork cloud and services.
Your release is named {{ .Release.Name }}.

CHART NAME: {{ .Chart.Name }}
CHART VERSION: {{ .Chart.Version }}
APP VERSION: {{ .Chart.AppVersion }}

To learn more about the release, try:
-------------------------------------
  $ helm status {{ .Release.Name }}
  $ helm get all {{ .Release.Name }}
-------------------------------------
Deployed applications and services:
-------------------------------------
{{- if .Values.twcloud.enabled }}
Teamwork cloud server - Replicas: {{ .Values.twcloud.replicas }}
{{- end }}
{{- if .Values.cassandra.enabled }}
Cassandra DB - Replicas: {{ .Values.cassandra.replicaCount }}
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
{{- if .Values.zookeeper.enabled }}
Zookeeper server
{{- end }}
-------------------------------------

{{ if .Values.ingress.enabled }}
ingress-nginx is enabled.
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

### ENTRY: helm-charts/templates/ingress-resource.yaml

- bytes: 5395
- crc32: `f4ace1d9`
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
  {{/*name: {{ $fullName-ing.resource }}*/}}
  name: ingress.resource
  labels:
    {{- include "main-template.labels" . | nindent 4 }}
  {{- with .Values.ingress.controller.annotations }}
  annotations:
    {{- toYaml . | nindent 4 }}    
  {{- end }}
spec:
  {{- if and .Values.ingress.controller.className (semverCompare ">=1.18-0" .Capabilities.KubeVersion.GitVersion) }}
  ingressClassName: {{ .Values.ingress.controller.className }}
  {{- end }}
  {{- if .Values.ingress.controller.tls }}
  tls:
    {{- range .Values.ingress.controller.tls }}
    - hosts:
        {{- range .hosts }}
        - {{ . | quote }}
        {{- end }}
      secretName: {{ .secretName }}
    {{- end }}
  {{- end }}
  rules:
  {{- range .Values.ingress.controller.hosts }}
  - host: {{ .host | quote }}
  {{- end }}      
    http:      
      paths:  
        {{- if .Values.adminconsole.enabled }}
        - path: /admin
          pathType: Prefix
          backend:
            service:
              name: {{ .Release.Name }}-{{ .Values.adminconsole.appLabel | replace "-" "" }}
              port:
                number: {{ $.Values.adminconsole.service.port }}
        {{- end }}
        {{- if .Values.authentication.enabled }}
        - path: /authentication
          pathType: Prefix
          backend:
            service:
              name: {{ .Release.Name }}-{{ .Values.authentication.appLabel }}
              port:
                number: {{ $.Values.authentication.service.port }}
        {{- end }}
        {{- if .Values.collaborator.enabled }}
        - path: /collaborator
          pathType: Prefix
          backend:
            service:
              name: {{ .Release.Name }}-{{ .Values.collaborator.appLabel }}
              port:
                number: {{ $.Values.collaborator.service.port }}
        {{- end }}
        {{- if .Values.docexporter.enabled }}
        - path: /document-exporter
          pathType: Prefix
          backend:
            service:
              name: {{ .Release.Name }}-{{ .Values.docexporter.appLabel }}
              port: 
                number: {{ $.Values.docexporter.service.port }}
        {{- end }}        
        {{- if .Values.oslc.enabled }}
        - path: /oslc
          pathType: Prefix
          backend:
            service:
              name: {{ .Release.Name }}-{{ .Values.oslc.appLabel }}
              port:
                number: {{ $.Values.oslc.service.port }}
        {{- end }}
        {{- if .Values.reports.enabled }}
        - path: /reports
          pathType: Prefix
          backend:
            service:
              name: {{ .Release.Name }}-{{ .Values.reports.appLabel }}
              port:
                number: {{ $.Values.reports.service.port }}
        {{- end }}
        {{- if .Values.resources.enabled }}
        - path: /resources
          pathType: Prefix
          backend:
            service:
              name: {{ .Release.Name }}-{{ .Values.resources.appLabel }}
              port:
                number: {{ $.Values.resources.service.port }}
        {{- end }}
        {{- if .Values.rum.enabled }}
        - path: /resource-usage-map
          pathType: Prefix
          backend:
            service:
              name: {{ .Release.Name }}-{{ .Values.rum.appLabel }}
              port:
                number: {{ $.Values.rum.service.port }}
        {{- end }}
        {{- if .Values.simulation.enabled }}        
        - path: /simulation
          pathType: Prefix
          backend:
            service:
              name: {{ .Release.Name }}-{{ .Values.simulation.appLabel }}
              port:
                number: {{ $.Values.simulation.service.port }}
        {{- end }}
        {{- if .Values.webapp.enabled }}
        - path: /webapp
          pathType: Prefix
          backend:
            service:
              name: {{ .Release.Name }}-{{ .Values.webapp.appLabel }}
              port:
                number: {{ $.Values.webapp.service.port }}
        {{- end }}
        {{- if .Values.sysml2api.enabled }}
        - path: /sysmlv2-api
          pathType: Prefix
          backend:
            service:
              name: {{ .Release.Name }}-{{ .Values.sysml2api.appLabel }}
              port:
                number: {{ $.Values.sysml2api.service.port }}
        {{- end }}
        {{- if .Values.sgicrawler.enabled }}
        - path: /sgi-crawler
          pathType: Prefix
          backend:
            service:
              name: {{ .Release.Name }}-{{ .Values.sgicrawler.appLabel }}
              port:
                number: {{ $.Values.sgicrawler.service.port }}
        {{- end }}
{{- end }}


````

### ENTRY: helm-charts/Chart.yaml

- bytes: 1461
- crc32: `fd41e64a`
- decoded_as: `utf-8`

````yaml
apiVersion: v2
name: tcas
description: A Helm chart to deploy Teamwork cloud and services

type: application

version: 0.1.2

appVersion: "2024xR2"

dependencies:
- name: ingress-nginx
  version: 4.11.2
  repository: https://kubernetes.github.io/ingress-nginx
  alias: ingress
  condition: ingress.enabled

- name: zookeeper
  version: 13.4.0
  repository: https://charts.bitnami.com/bitnami
  condition: zookeeper.enabled

- name: cassandra
  version: 11.1.7
  repository: https://charts.bitnami.com/bitnami
  condition: cassandra.enabled

- name: twcloud
  version: 0.1.2
  condition: twcloud.enabled

- name: adminconsole
  version: 0.1.2
  condition: adminconsole.enabled

- name: authentication
  version: 0.1.2
  condition: authentication.enabled

- name: artemis
  version: 0.1.2
  condition: artemis.enabled

- name: collaborator
  version: 0.1.2
  condition: collaborator.enabled

- name: docexporter
  version: 0.1.2
  condition: docexporter.enabled

- name: oslc
  version: 0.1.2
  condition: oslc.enabled

- name: reports
  version: 0.1.2
  condition: reports.enabled

- name: resources
  version: 0.1.2
  condition: resources.enabled

- name: rum
  version: 0.1.2
  condition: rum.enabled

- name: simulation
  version: 0.1.2
  condition: simulation.enabled

- name: webapp
  version: 0.1.2
  condition: webapp.

- name: sysml2api
  version: 0.1.2
  condition: sysml2api.enabled

- name: sgicrawler
  version: 0.1.2
  condition: sgicrawler.enabled

````

### ENTRY: helm-charts/values.yaml

- bytes: 15417
- crc32: `65df40b1`
- decoded_as: `utf-8`

````yaml
# Global values for all applications and sevices
global:
  # Specify the image repository url (should end with /).
  # MANDATORY !
  # repoURL: admin.example.com:5000/
  repoURL: 

  # Docker hub repository for 
  dockerHub: registry.hub.docker.com/

  # Specify the image pull policy
  pullPolicy: Always

  # Property for sidecar container
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

  # Specify the url reserved for Ingress to access WebAppPlatform
  # MANDATORY !
  # serviceUri: https://example.com/
  serviceUrl: 

  # Specify the Authentication server domain name (FQDN) reserved for Ingress
  # MANDATORY !
  # authenticationServerIp: example.com
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

  # Specify the licensing framework.  
  # licenseFramework: FlexNet
  # Do not change (works only with FlexNet)
  licenseFramework: FlexNet

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

# Applications and Services settings

##### TeamworkCloud and components #####

cassandra:
  enabled: true
  image:
    registry:
    pullPolicy: Always
    repository:
    tag:
  extraVolumes:
  - name: config-volume
    configMap:
      name: "{{ .Release.Name }}-cassandra-cm"
  commonLabels: {app: cassandra}
  podLabels: {app: cassandra}
  volumePermissions:
    enabled: true
  persistence:
    enabled: true
    storageClass: cassandra-local
    size: 10Gi
    accessModes: ["ReadWriteOnce"]
  readinessProbe:
    enabled: true
    initialDelaySeconds: 60
    periodSeconds: 60
    timeoutSeconds: 60
    failureThreshold: 30
  livenessProbe:
    enabled: true
    initialDelaySeconds: 60
    periodSeconds: 60
    timeoutSeconds: 60
    successThreshold: 1
    failureThreshold: 30
  # cluster.seedCount sets how many cassandra nodes will have info about cassandra.
  # If you run single cassandra, value should be 1, if you run cassandra cluster 
  # value shoud be 2 or more depending on your needs.
  cluster:
    seedCount: 2
  # ReplicaCount should match with twcloud
  replicaCount: 3
  updateStrategy:
    type: RollingUpdate
  # Intra Port on the Host and Container (Default: 7000)
  # containerPorts.intra: 7000
  # Intra Port on the Host (Default: 7000)
  # hostPorts.intra: 7000
  jvm:
    maxHeapSize: "12G"
    newHeapSize: "2G"
  # Extra environment variables
  extraEnvVars:
    - name: CASSANDRA_AUTHENTICATOR
      value: AllowAllAuthenticator
    - name: CASSANDRA_AUTHORIZER
      value: AllowAllAuthorizer
  extraVolumeMounts:
    - name: config-volume
      mountPath: /opt/bitnami/cassandra/conf.default/cassandra.yaml
      subPath: cassandra.yaml
      readOnly: true
    - name: config-volume
      mountPath: /opt/bitnami/cassandra/conf.default/logback.xml
      subPath: logback.xml
      readOnly: true
  # Resource limits
  resources:
    requests:
      cpu: 4000m
      memory: 16G
    limits:
      cpu: 4000m
      memory: 16G
  # Pod anti-affinity preset. Ignored if affinity is set. Allowed values: soft or hard
  podAntiAffinityPreset: hard

# Persistent Volumes used by Cassandra
persistentVolumes:
  # Enable Persistent Volumes
  enabled: true
  # Cassandra persistent volume name
  name: cass-vol-cluster
  # Persistent volume storage size
  storage: 20Gi
  # Persistent volume mode
  volumeMode: Filesystem
  # Persistent volume access mode
  accessModes: ReadWriteOnce
  # Persistent volume reclaim policy
  persistentVolumeReclaimPolicy: Retain
  # Storage class name
  storageClassName: cassandra-local
  # Persistent volume local path (mount location on workers !!! Path is not created automatically !!!)
  # Provide path of precreated directory for Cassandra data base on all worker nodes
  # Example: localPath: /cassandra
  # MANDATORY !
  localPath: 
  # Persistent volume node secector terms match expressions
  matchExpressionsKey: kubernetes.io/hostname
  matchExpressionsOperator: In
  # List worker hosts (fqdn) on which persistent volumes should be created.
  # Local storage doesn't supports dynamic persistent volume provisioning
  # so you have to provide list of worker nodes on which persistent volumes
  # should be provisioned.
  # MANDATORY !
  # Example:
  #   workers:
  #   - host: worker1.example.com
  #   - host: worker2.example.com
  #   - host: worker3.example.com
  workers:
  - host:

# IMPORTANT !!!
# Configure repositories and tags for each service based on images previously stored in local repository

twcloud:
  enabled: true
  # Set svcLB to true if you want expose service as LoadBalancer type.
  # By default Teamwork Cloud ports are exposed through Ingress-nginx
  svcLB: false
  # Default Cassandra port
  cassandraPort: 9042
  image:
    # Specifies image repository name
    repository: 
    # Specifies image tag name
    tag:
  replicas: 3
  env:
    twcxmx: 8g
  resources:
    requests:
      memory: '10G'
      cpu: '2000m'
    limits:
      memory: '10G'
      cpu: '2000m'  

##### WebApplicationPlatform #####

# IMPORTANT !!!
# Configure repositories and tags for each service based on images previously stored in local repository

# Admin-console application settings
adminconsole:
  # Specifies whether a admin-console application should be deployed (Mandatory)
  enabled: true
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: 
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
    repository: 
    # Specifies image tag name
    tag: 

# Artemis service settings
artemis:
  # Specifies whether a artemis service should be deployed (Optional)
  # Required for WAP applications: resources, collaborator, document-exporter, simulation.
  enabled: true
  image:
    # Specifies image repository name
    repository: apache/activemq-artemis
    # Specifies image tag name (if tag is floating int, then be in quotation marks)
    tag: "2.32.0"

# Collaborator application settings
collaborator:
  # Specifies whether a collaborator application should be deployed
  enabled: true
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: 
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
    repository: 
    # Specifies image tag name
    tag: 

# Oslc application settings
oslc:
  # Specifies whether a oslc application should be deployed (Optional)
  enabled: true
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: 
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
    repository: 
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
    repository: 
    # Specifies image tag name
    tag: 

# Resource-usage-map application settings
rum:
  # Specifies whether a resource-usage-map application should be deployed (Optional)
  enabled: true
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: 
    # Specifies image tag name
    tag: 

# Simulation application settings
simulation:
  # Specifies whether a simulation application should be deployed (Optional)
  enabled: true
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: 
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
    repository: 
    # Specifies image tag name
    tag:

# Sgicrawler application settings
sgicrawler:
  # Specifies whether a Sgicrawler application should be deployed (Mandatory)
  enabled: true
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: 
    # Specifies image tag name
    tag:

# Sysml2-api application settings
sysml2api:
  # Specifies whether a Sysml2-api application should be deployed (Mandatory)
  enabled: true
  # Specifies replica count
  replicas: 1
  image:
    # Specifies image repository name
    repository: 
    # Specifies image tag name
    tag:

# Zookeeper service settings
zookeeper:
  # Specifies whether a zookeeper service should be deployed (Mandatory)
  enabled: true
  containerPorts:
    # Specifies zookeeper service port
    client: 2181
  persistence:
   # Specifies enables/disables persistance (by default disabled for testing purpose)
   enabled: false
  volumePermissions:
   enabled: false

# Ingress-nginx settings
ingress:
  enabled: true
  # Exposes TWCloud server and rest api ports through ingress controller
  tcp:
    3579: "{{ .Release.Namespace }}/{{ .Release.Name }}-twcloud:3579"
    8111: "{{ .Release.Namespace }}/{{ .Release.Name }}-twcloud:8111"
  controller:    
    className: "nginx"
    allowSnippetAnnotations: true
    # Specifies annotations      
    annotations: 
      nginx.ingress.kubernetes.io/backend-protocol: https
      nginx.ingress.kubernetes.io/proxy-body-size: 100m
      nginx.ingress.kubernetes.io/session-cookie-name: "COOKIE"
      nginx.ingress.kubernetes.io/affinity-canary-behavior: "sticky"
      nginx.ingress.kubernetes.io/affinity-mode: "persistent"
      nginx.ingress.kubernetes.io/affinity: "cookie"
      nginx.ingress.kubernetes.io/proxy-connect-timeout: "600"
      nginx.ingress.kubernetes.io/proxy-read-timeout: "3600"
      nginx.ingress.kubernetes.io/proxy-send-timeout: "3600"
      nginx.ingress.kubernetes.io/proxy-buffering: "on"
      nginx.ingress.kubernetes.io/proxy-buffers-number: "4"
      nginx.ingress.kubernetes.io/proxy-buffer-size: "16k"
      nginx.ingress.kubernetes.io/send-timeout: "600"
        
    # Additional custom Nginx configuration
    config:
      log-format-escape-json: '"true"'
      log-format-stream: '{"time":"$time_iso8601","remote_addr":"$remote_addr","protocol":"$protocol","status":"$status","upstream_addr":"$upstream_addr","upstream_connect_time":"$upstream_connect_time","upstream_first_byte_time":"$upstream_first_byte_time","upstream_session_time":"$upstream_session_time"}'
      log-format-upstream: '{"time":"$time_iso8601","remote_addr":"$remote_addr","proxy_protocol_addr":"$proxy_protocol_addr","proxy_protocol_port":"$proxy_protocol_port","x_forward_for":"$proxy_add_x_forwarded_for","remote_user":"$remote_user","host":"$host","request_method":"$request_method","request_uri":"$request_uri","server_protocol":"$server_protocol","status":"$status","request_time":"$request_time","request_length":"$request_length","bytes_sent":"$bytes_sent","upstream_name":"$proxy_upstream_name","upstream_addr":"$upstream_addr","upstream_uri":"$uri","upstream_response_length":"$upstream_response_length","upstream_response_time":"$upstream_response_time","upstream_status":"$upstream_status","http_referrer":"$http_referer","http_user_agent":"$http_user_agent","http_cookie":"$http_cookie"}'    
    # Extra environment variables
    extraEnvs:
      - name: RELEASE_NAME
        valueFrom:
            fieldRef:
              fieldPath: metadata.labels['app.kubernetes.io/instance']
    # Extra pod arguments
    extraArgs:
      tcp-services-configmap: $(POD_NAMESPACE)/$(RELEASE_NAME)-ingress-tcp    
    service:
      enabled: true
      externalTrafficPolicy: "Local"
      ports:
        http: 80
        https: 443
      targetPorts:
        http: http
        https: https

    hosts:
    # Specify domain name (fqdn) which is bind to exposed ip LoadBalancer address.
    # MANDATORY !
    # - host: example.com
    - host: 
      paths:
    tls:
    # Specify tls secret name that you createad earlier.
    # - secretName: secretName
    - secretName: tls-secret
      # Specify domain names for which tls is enabled (every domain name in new line and starts with -).
      # MANDATORY !
      hosts:
      # - example.com
      

````

### ENTRY: dockerfiles/admin-console/Dockerfile

- bytes: 1005
- crc32: `1802e8cd`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.28-jre17-temurin-jammy

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
- crc32: `6b3cbcb5`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.28-jre17-temurin-jammy

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
- crc32: `ad8c3cb5`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.28-jre17-temurin-jammy

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
- crc32: `24454d67`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.28-jre17-temurin-jammy

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
- crc32: `3f3ff40f`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.28-jre17-temurin-jammy

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
- crc32: `65ff1e06`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.28-jre17-temurin-jammy

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
- crc32: `cdd2fdf6`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.28-jre17-temurin-jammy

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
- crc32: `d996901f`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.28-jre17-temurin-jammy

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
- crc32: `7e1eb69d`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.28-jre17-temurin-jammy

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
- crc32: `e0d0792d`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.28-jre17-temurin-jammy

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

### ENTRY: dockerfiles/sgi-crawler/Dockerfile

- bytes: 1011
- crc32: `b849f34b`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.28-jre17-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY sgi-crawler.war ${TOMCAT_DIR}/webapps/
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

### ENTRY: dockerfiles/sysml2-api/Dockerfile

- bytes: 1011
- crc32: `06c11a79`
- decoded_as: `utf-8`

````text
FROM tomcat:10.1.28-jre17-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY sysmlv2-api.war ${TOMCAT_DIR}/webapps/
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

### ENTRY: releaseNotes.txt

- bytes: 104
- crc32: `90de4c9d`
- decoded_as: `utf-8`

````text
New services:
    sgi-crawler
    sysml2-api

Changes:
    ingress-nginx chart version changed to 4.11.2
````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "194642871",
  "type": "attachment",
  "status": "current",
  "title": "twc-services-charts.zip",
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
    "when": "2024-11-05T10:47:35.651+01:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/194642871/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/194642871"
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
    "fileSize": 63739,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/191924296/twc-services-charts.zip?version=1&modificationDate=1730800055651&api=v2",
    "webui": "/spaces/MCS2024xR2/pages/191924296/Deployment+example+for+Teamwork+Cloud+with+services+on+Kubernetes?preview=%2F191924296%2F194642871%2Ftwc-services-charts.zip",
    "self": "https://docs.nomagic.com/rest/api/content/194642871"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/194642871/child",
    "restrictions": "/rest/api/content/194642871/restriction/byOperation",
    "history": "/rest/api/content/194642871/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/194642871/descendant",
    "space": "/rest/api/space/MCS2024xR2",
    "relevantViewRestrictions": "/rest/api/content/194642871/restriction/relevantViewRestrictions"
  }
}
````
