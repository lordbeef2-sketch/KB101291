# NOMAGIC ATTACHMENT: ha-proxy-SAMPLE.zip

- attachment_id: `304002676`
- space_key: `MCS`
- parent_page_id: `304002672`
- parent_page_title: (2026x Refresh1) Downloadable scripts
- media_type: `application/zip`
- reported_bytes: 4682
- download_url: https://docs.nomagic.com/download/attachments/304002672/ha-proxy-SAMPLE.zip?version=2&modificationDate=1782458171830&api=v2
- payload_kind: `archive-expanded`
- downloaded_sha256: `8c5e5fadd9206f319ac75d9a5164d34e199869411b5b592bc86762186e9eaf8f`

## ARCHIVE CONTENTS

### ENTRY: ha-proxy-SAMPLE/configure_haproxy18_layer4_tcp.sh

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

### ENTRY: ha-proxy-SAMPLE/configure_haproxy18_layer7_https.sh

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

### ENTRY: ha-proxy-SAMPLE/example_install_haproxy.sh

- bytes: 769
- crc32: `b06bfb03`
- decoded_as: `utf-8`

````text
# #!/bin/bash
# Detect OS
if [ -f /etc/os-release ]; then
    . /etc/os-release
    case "$ID" in
        rhel)
            echo "Detected supported OS: $NAME $VERSION"
            ;;
        *)
            echo "Error: $NAME is not supported. This script supports only RHEL Linux."
            exit 1
            ;;
    esac
else
    echo "Error: Cannot detect OS. Exiting."
    exit 1
fi

# Check if haproxy package is available
if ! yum list available haproxy &>/dev/null; then
    echo "Error: 'haproxy' package not available in your enabled repos."
    exit 1
fi

# Install HAProxy
echo "Installing HAProxy..."
yum -y install haproxy
if [ $? -eq 0 ]; then
    echo "HAProxy installed successfully."
else
    echo "Error: Failed to install HAProxy."
    exit 1
fi


````

### ENTRY: ha-proxy-SAMPLE/haproxy.cfg.layer4.tcp.tmpl

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

### ENTRY: ha-proxy-SAMPLE/haproxy.cfg.layer7.https.tmpl

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
  "id": "304002676",
  "type": "attachment",
  "status": "current",
  "title": "ha-proxy-SAMPLE.zip",
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
    "when": "2026-06-26T09:16:11.830+02:00",
    "message": "",
    "number": 2,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/304002676/version/2"
    },
    "_expandable": {
      "content": "/rest/api/content/304002676"
    }
  },
  "position": -1,
  "container": {
    "id": "304002672",
    "type": "page",
    "status": "current",
    "title": "(2026x Refresh1) Downloadable scripts",
    "position": 3,
    "extensions": {
      "position": 3
    },
    "_links": {
      "webui": "/spaces/MCS/pages/304002672/2026x+Refresh1+Downloadable+scripts",
      "edit": "/pages/resumedraft.action?draftId=304002672",
      "tinyui": "/x/cLYeEg",
      "self": "https://docs.nomagic.com/rest/api/content/304002672"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/304002672/child",
      "restrictions": "/rest/api/content/304002672/restriction/byOperation",
      "history": "/rest/api/content/304002672/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/304002672/descendant",
      "space": "/rest/api/space/MCS",
      "relevantViewRestrictions": "/rest/api/content/304002672/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/zip"
  },
  "extensions": {
    "mediaType": "application/zip",
    "fileSize": 4682,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/304002672/ha-proxy-SAMPLE.zip?version=2&modificationDate=1782458171830&api=v2",
    "webui": "/spaces/MCS/pages/304002672/2026x+Refresh1+Downloadable+scripts?preview=%2F304002672%2F304002676%2Fha-proxy-SAMPLE.zip",
    "self": "https://docs.nomagic.com/rest/api/content/304002676"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/304002676/child",
    "restrictions": "/rest/api/content/304002676/restriction/byOperation",
    "history": "/rest/api/content/304002676/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/304002676/descendant",
    "space": "/rest/api/space/MCS",
    "relevantViewRestrictions": "/rest/api/content/304002676/restriction/relevantViewRestrictions"
  }
}
````
