# NOMAGIC ATTACHMENT: HAProxy-Pkg.zip

- attachment_id: `170491402`
- space_key: `TWCloud2024xR1`
- parent_page_id: `170491401`
- parent_page_title: Layer 4 and Layer 7 proxy setup
- media_type: `application/zip`
- reported_bytes: 4709
- download_url: https://docs.nomagic.com/download/attachments/170491401/HAProxy-Pkg.zip?version=2&modificationDate=1734446968699&api=v2
- payload_kind: `archive-expanded`
- downloaded_sha256: `10fce141e848586f77bff89564278816a5fe6ae738e82685e83d543a68c419da`

## ARCHIVE CONTENTS

### ENTRY: HAProxy-Pkg/configure_haproxy18_layer4_tcp.sh

- bytes: 1938
- crc32: `947b066f`
- decoded_as: `utf-8`

````text
#!/bin/bash
#
# HAProxy Proxy/LB depoyment and configuration script
#
HAPROXY_CONF=/etc/opt/rh/rh-haproxy18/haproxy/haproxy.cfg

echo "This script will configure HAProxy as a local proxy where all services are bound to port 443"
echo ""
echo "----------------------------------------------------------------------------"
echo ""
read -e -p "Please enter the port number for Client->TWCserver Communications (Settings/Secured Connection in TWC Admin):  "  -i "10002"  SSL_PORT
echo ""
read -e -p "Please enter the IP Address for the Webapp Proxy:  "  -i ""  WEBAPP_IP
echo ""
read -e -p "Please enter the IP Address for the REST API Proxy:  "  -i ""  REST_IP  
echo ""
read -e -p "Please enter the IP Address for the Client->TWCserver Proxy:  "  -i ""  MD_IP  
echo ""
read -e -p "Please enter the IP Address for the FlexNET Proxy:  "  -i ""  FLEX_IP  
echo ""
echo "----------------------------------------------------------------------------"

echo "Reconfiguring SELinux for http connections"
echo ""
setsebool -P haproxy_connect_any 1 -P
echo "Copying HAProxy configuration template"
\cp -f haproxy.cfg.layer4.tcp.tmpl $HAPROXY_CONF
echo ""
echo "Applying configuration changes"
echo ""

sed -i "s/:SSL_PORT/:$SSL_PORT/g" $HAPROXY_CONF
sed -i "s/WEBAPP_IP:/$WEBAPP_IP:/g" $HAPROXY_CONF
sed -i "s/REST_IP:/$REST_IP:/g" $HAPROXY_CONF
sed -i "s/MD_IP:/$MD_IP:/g" $HAPROXY_CONF
sed -i "s/FLEX_IP:/$FLEX_IP:/g" $HAPROXY_CONF
echo ""
echo "Configuring firewall rule to allow port 443"
FWZONE=$(firewall-cmd --get-default-zone)
echo "Discovered firewall zone $FWZONE"
cat <<EOF | tee /etc/firewalld/services/haproxy.xml
<?xml version="1.0" encoding="utf-8"?>
<service version="1.0">
    <short>haproxy</short>
    <description>haproxy</description>
    <port port="443" protocol="tcp"/>
</service>
EOF
sleep 5
firewall-cmd --zone=$FWZONE --add-service=haproxy --permanent
firewall-cmd --reload 
echo "HAProxy Local Proxy Deployment Complete"

````

### ENTRY: HAProxy-Pkg/configure_haproxy18_layer7_https.sh

- bytes: 2184
- crc32: `4dee587f`
- decoded_as: `utf-8`

````text
#!/bin/bash
#
# HAProxy 1.8 configuration script - SSL Termination
#
HAPROXY_CONF=/etc/opt/rh/rh-haproxy18/haproxy/haproxy.cfg

echo "This script will deploy and configure HAProxy as a local proxy with TLS termination where all services are bound to port 443"
echo ""
echo "----------------------------------------------------------------------------"
echo ""
read -e -p "Please enter the port number for Client->TWCserver Communications (Settings/Secured Connection in TWC Admin):  "  -i "10002"  SSL_PORT
echo ""
read -e -p "Please enter the IP Address for the https proxy (Webapp/Authserver/REST):  "  -i ""  WEBAPP_IP
echo ""
read -e -p "Please enter the IP Address for the Client->TWCserver Proxy:  "  -i ""  MD_IP  
echo ""
read -e -p "Please enter the IP Address for the FlexNET Proxy:  "  -i ""  FLEX_IP  
echo ""
read -e -p "Please enter the full path to your server certificate (PEM which includes certs and key):  "  -i ""  CERT_PATH
echo ""
echo "----------------------------------------------------------------------------"
echo ""
echo "Reconfiguring SELinux for http connections"
echo ""
setsebool -P haproxy_connect_any 1 -P
echo "Copying HAProxy configuration template"
echo "Reconfiguring SELinux for tcp connections"
echo ""
setsebool -P haproxy_connect_any 1 -P
echo "Copying HAProxy configuration template"
\cp -f haproxy.cfg.layer7.https.tmpl $HAPROXY_CONF
echo ""
echo "Applying configuration changes"
echo ""

sed -i "s/:SSL_PORT/:$SSL_PORT/g" $HAPROXY_CONF
sed -i "s/WEBAPP_IP:/$WEBAPP_IP:/g" $HAPROXY_CONF
sed -i "s/MD_IP:/$MD_IP:/g" $HAPROXY_CONF
sed -i "s/FLEX_IP:/$FLEX_IP:/g" $HAPROXY_CONF
sed -i "s#CERT_PATH#$CERT_PATH#g" $HAPROXY_CONF

echo ""
echo "Configuring firewall rule to allow port 443"
FWZONE=$(firewall-cmd --get-default-zone)
echo "Discovered firewall zone $FWZONE"
cat <<EOF | tee /etc/firewalld/services/haproxy.xml
<?xml version="1.0" encoding="utf-8"?>
<service version="1.0">
    <short>haproxy</short>
    <description>haproxy</description>
    <port port="443" protocol="tcp"/>
</service>
EOF
sleep 5
firewall-cmd --zone=$FWZONE --add-service=haproxy --permanent
firewall-cmd --reload 
echo "HAProxy Local Proxy Deployment Complete"

````

### ENTRY: HAProxy-Pkg/example_install_haproxy.sh

- bytes: 253
- crc32: `33d84e88`
- decoded_as: `utf-8`

````text
#!/bin/bash
#
# Example of HA-Proxy installation on CentOS 7
#
echo "Installing Software Collections (SCL)"
yum install centos-release-scl
echo ""
echo "Installing HAProxy 1.8"
yum -y -q install rh-haproxy18-haproxy rh-haproxy18-haproxy-syspaths
echo ""
````

### ENTRY: HAProxy-Pkg/haproxy.cfg.layer4.tcp.tmpl

- bytes: 2453
- crc32: `33015a43`
- decoded_as: `utf-8`

````text
#---------------------------------------------------------------------
# HAProxy Layer 4 (TCP) Example Configuration 
#---------------------------------------------------------------------

#---------------------------------------------------------------------
# Global settings
#---------------------------------------------------------------------
global

    log 127.0.0.1 local2

    chroot      /var/lib/haproxy
    pidfile     /var/run/haproxy.pid
    maxconn     4000
    user        haproxy
    group       haproxy
    daemon

    # turn on stats unix socket
    stats socket /var/lib/haproxy/stats

#---------------------------------------------------------------------
# common defaults that all the 'listen' and 'backend' sections will
# use if not designated in their block
#---------------------------------------------------------------------
defaults
    mode                    tcp
    balance                 source
    log                     global
    option                  tcplog
    option                  dontlognull
    option http-server-close
    option                  redispatch
    retries                 3
    timeout http-request    10s
    timeout queue           1m
    timeout connect         10s
    timeout client          1m
    timeout server          1m
    timeout http-keep-alive 10s
    timeout check           10s
    maxconn                 3000

#---------------------------------------------------------------------
# frontends  which proxy to the backends
#---------------------------------------------------------------------


frontend            webapp
    bind            WEBAPP_IP:443
    mode            tcp
    default_backend webapp


frontend            rest
    bind            REST_IP:443
    mode            tcp
    default_backend rest


frontend            md
    bind            MD_IP:443
    mode            tcp
    default_backend md


frontend            flex
    bind            FLEX_IP:443
    mode            tcp
    default_backend flex


#---------------------------------------------------------------------
#  backends for proxying services
#---------------------------------------------------------------------
backend webapp
    mode tcp
    server      static 127.0.0.1:8443

backend rest
    mode tcp
    server      static 127.0.0.1:8111

backend md
    mode tcp
    server      static 127.0.0.1:SSL_PORT

backend flex
    mode tcp
    server      static 127.0.0.1:1101


````

### ENTRY: HAProxy-Pkg/haproxy.cfg.layer7.https.tmpl

- bytes: 3659
- crc32: `7f2b88c2`
- decoded_as: `utf-8`

````text
#---------------------------------------------------------------------
# HAProxy Hybrid Configuration Example (HTTPS/TCP) For TWC
#---------------------------------------------------------------------

#---------------------------------------------------------------------
# Global settings
#---------------------------------------------------------------------
global

    log 127.0.0.1 local2

    chroot      /var/lib/haproxy
    pidfile     /var/run/haproxy.pid
    maxconn     4000
    user        haproxy
    group       haproxy
    daemon

    # turn on stats unix socket
    stats socket /var/lib/haproxy/stats

    #enforce TLS >= 1.2 and strong ciphers
    ssl-default-bind-options ssl-min-ver TLSv1.2

    # Mozilla SSL Configuration Generator: https://ssl-config.mozilla.org/
    ssl-default-bind-ciphers ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256
    ssl-server-verify none
#---------------------------------------------------------------------
# common defaults that all the 'listen' and 'backend' sections will
# use if not designated in their block
#---------------------------------------------------------------------
defaults
    mode                    http
    balance                 source
    log                     global
    option                  httplog
    option                  dontlognull
    option http-server-close
    option                  redispatch
    retries                 3
    timeout http-request    10s
    timeout queue           1m
    timeout connect         10s
    timeout client          1m
    timeout server          1m
    timeout http-keep-alive 10s
    timeout check           10s
    maxconn                 3000

#---------------------------------------------------------------------
# frontends  which proxy to the backends
#---------------------------------------------------------------------


frontend            https_services
    mode            http
    bind            WEBAPP_IP:443 ssl crt CERT_PATH

    acl             webapp-acl            path_beg /webapp
    acl             webapp-acl            path_beg /authentication
    acl             webapp-acl            path_beg /admin
    acl             webapp-acl            path_beg /collaborator
    acl             webapp-acl            path_beg /document-exporter
    acl             webapp-acl            path_beg /oslc
    acl             webapp-acl            path_beg /reports
    acl             webapp-acl            path_beg /resources
    acl             webapp-acl            path_beg /resource-usage-map
    acl             webapp-acl            path_beg /simulation
    use_backend     webapp if webapp-acl
 
    acl             rest-acl              path_beg  /osmc
    use_backend     rest if rest-acl

frontend            md
    bind            MD_IP:443
    mode            tcp
    option          tcplog
    default_backend md

frontend            flex
    bind            FLEX_IP:443
    mode            tcp
    option          tcplog
    default_backend flex

#---------------------------------------------------------------------
#  backends for proxying services
#---------------------------------------------------------------------
backend webapp
    server      static 127.0.0.1:8443 ssl

backend rest
    server      static 127.0.0.1:8111 ssl

backend md
    mode tcp
    server      static 127.0.0.1:3579

backend flex
    mode tcp
    server      static 127.0.0.1:1101

	

````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "170491402",
  "type": "attachment",
  "status": "current",
  "title": "HAProxy-Pkg.zip",
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
    "when": "2024-12-17T15:49:28.699+01:00",
    "message": "",
    "number": 2,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/170491402/version/2"
    },
    "_expandable": {
      "content": "/rest/api/content/170491402"
    }
  },
  "position": -1,
  "container": {
    "id": "170491401",
    "type": "page",
    "status": "current",
    "title": "Layer 4 and Layer 7 proxy setup",
    "position": 5,
    "extensions": {
      "position": 5
    },
    "_links": {
      "webui": "/spaces/TWCloud2024xR1/pages/170491401/Layer+4+and+Layer+7+proxy+setup",
      "edit": "/pages/resumedraft.action?draftId=170491401",
      "tinyui": "/x/CX4pCg",
      "self": "https://docs.nomagic.com/rest/api/content/170491401"
    },
    "_expandable": {
      "container": "/rest/api/space/TWCloud2024xR1",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/170491401/child",
      "restrictions": "/rest/api/content/170491401/restriction/byOperation",
      "history": "/rest/api/content/170491401/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/170491401/descendant",
      "space": "/rest/api/space/TWCloud2024xR1",
      "relevantViewRestrictions": "/rest/api/content/170491401/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/zip"
  },
  "extensions": {
    "mediaType": "application/zip",
    "fileSize": 4709,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/170491401/HAProxy-Pkg.zip?version=2&modificationDate=1734446968699&api=v2",
    "webui": "/spaces/TWCloud2024xR1/pages/170491401/Layer+4+and+Layer+7+proxy+setup?preview=%2F170491401%2F170491402%2FHAProxy-Pkg.zip",
    "self": "https://docs.nomagic.com/rest/api/content/170491402"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/170491402/child",
    "restrictions": "/rest/api/content/170491402/restriction/byOperation",
    "history": "/rest/api/content/170491402/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/170491402/descendant",
    "space": "/rest/api/space/TWCloud2024xR1",
    "relevantViewRestrictions": "/rest/api/content/170491402/restriction/relevantViewRestrictions"
  }
}
````
