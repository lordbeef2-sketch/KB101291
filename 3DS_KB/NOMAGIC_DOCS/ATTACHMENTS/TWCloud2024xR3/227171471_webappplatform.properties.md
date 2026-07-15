# NOMAGIC ATTACHMENT: webappplatform.properties

- attachment_id: `227171471`
- space_key: `TWCloud2024xR3`
- parent_page_id: `227171466`
- parent_page_title: Installing Web Application Platform manually
- media_type: `application/octet-stream`
- reported_bytes: 6057
- download_url: https://docs.nomagic.com/download/attachments/227171466/webappplatform.properties?version=1&modificationDate=1746450328927&api=v2
- payload_kind: `text-exact`
- downloaded_sha256: `0e950c2de9237cb30352781b51f36c956ec29f6e14033b1f5345ae2646b41213`

## EXACT ATTACHMENT SOURCE

````text
#
# General properties
#

install.root=.

#
# Web application platform properties
#

# Specify the guest user name and password.
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

# Specify the Teamwork Cloud administrator user name and password.
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

# Set to true to enable TLS. Otherwise, set to false or comment the property to disable it
#twc.client.tls=true

# Specify the keystore type, for example, JKS.
#twc.client.keystore.type=JKS

# Specify the full path to the keystore file.
#twc.client.keystore.path=<full.path>

# If the keystore is password-protected, specify the password of the keystore.
#twc.client.keystore.password=<password>

#
# FlexNet server properties
#

# Specify the FlexNet licence server IP address.
flexnet.server.name=127.0.0.1

# Specify the FlexNet license server port.
flexnet.server.port=1101

#
# Platform mailing engine properties used to send notifications via e-mail
#

# Specify the e-mail server host name.
mail.host=gate.company.com

# Specify the e-mail server port.
mail.port=25

#Specify the user name and password.
mail.username=anonymous
mail.password=

# Specify the e-mail protocol and encoding.
mail.protocol=smtp
mail.encoding=UTF-8

# Specify the sender's e-mail address.
mail.from.default=info@company.com

#
# Platform service discovery related properties
#

# Specify the ZooKeeper servers host:port values, separated by a comma. Port can be omitted if default 2181 is used
zookeeper.connect.string=localhost
# Specify zk node where ZooKeeper registers applications
zookeeper.base.service.path=/services
# Enable or disable service discovery. Enabled if the property does not exist
service.discovery.enabled=true
# Indicates path of services. Specify / if all services are deployed on the same Tomcat.
service.uri=/

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
# and referenced by the name, or its path can be specified, e. g. file:///E:/keys/keystore.jks or /opt/keys/keystore.jks
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

````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "227171471",
  "type": "attachment",
  "status": "current",
  "title": "webappplatform.properties",
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
    "when": "2025-05-05T15:05:28.927+02:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/227171471/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/227171471"
    }
  },
  "position": -1,
  "container": {
    "id": "227171466",
    "type": "page",
    "status": "current",
    "title": "Installing Web Application Platform manually",
    "position": 4,
    "extensions": {
      "position": 4
    },
    "_links": {
      "webui": "/spaces/TWCloud2024xR3/pages/227171466/Installing+Web+Application+Platform+manually",
      "edit": "/pages/resumedraft.action?draftId=227171466",
      "tinyui": "/x/ilyKDQ",
      "self": "https://docs.nomagic.com/rest/api/content/227171466"
    },
    "_expandable": {
      "container": "/rest/api/space/TWCloud2024xR3",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/227171466/child",
      "restrictions": "/rest/api/content/227171466/restriction/byOperation",
      "history": "/rest/api/content/227171466/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/227171466/descendant",
      "space": "/rest/api/space/TWCloud2024xR3",
      "relevantViewRestrictions": "/rest/api/content/227171466/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/octet-stream"
  },
  "extensions": {
    "mediaType": "application/octet-stream",
    "fileSize": 6057,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/227171466/webappplatform.properties?version=1&modificationDate=1746450328927&api=v2",
    "webui": "/spaces/TWCloud2024xR3/pages/227171466/Installing+Web+Application+Platform+manually?preview=%2F227171466%2F227171471%2Fwebappplatform.properties",
    "self": "https://docs.nomagic.com/rest/api/content/227171471"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/227171471/child",
    "restrictions": "/rest/api/content/227171471/restriction/byOperation",
    "history": "/rest/api/content/227171471/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/227171471/descendant",
    "space": "/rest/api/space/TWCloud2024xR3",
    "relevantViewRestrictions": "/rest/api/content/227171471/restriction/relevantViewRestrictions"
  }
}
````
