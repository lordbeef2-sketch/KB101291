# NOMAGIC ATTACHMENT: HAProxy-Pkg.zip

- attachment_id: `144637973`
- space_key: `TWCloud2024x`
- parent_page_id: `144637972`
- parent_page_title: Layer 4 and Layer 7 proxy setup
- media_type: `application/zip`
- reported_bytes: 4462
- download_url: https://docs.nomagic.com/download/attachments/144637972/HAProxy-Pkg.zip?version=1&modificationDate=1700236336198&api=v2
- payload_kind: `archive-expanded`
- downloaded_sha256: `f304ffcfb0021c674889555985225a5f475ca365c091d81477606ccf841adc7e`

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

- bytes: 2544
- crc32: `ba2ade14`
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

- bytes: 3779
- crc32: `c33d3cd0`
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
    acl             webapp-acl            path_beg /oslc-selection-dialog
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
  "id": "144637973",
  "type": "attachment",
  "status": "current",
  "title": "HAProxy-Pkg.zip",
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
    "when": "2023-11-17T16:52:16.198+01:00",
    "message": "",
    "number": 1,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/144637973/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/144637973"
    }
  },
  "position": -1,
  "container": {
    "id": "144637972",
    "type": "page",
    "status": "current",
    "title": "Layer 4 and Layer 7 proxy setup",
    "position": 5,
    "extensions": {
      "position": 5
    },
    "_links": {
      "webui": "/spaces/TWCloud2024x/pages/144637972/Layer+4+and+Layer+7+proxy+setup",
      "edit": "/pages/resumedraft.action?draftId=144637972",
      "tinyui": "/x/FACfC",
      "self": "https://docs.nomagic.com/rest/api/content/144637972"
    },
    "_expandable": {
      "container": "/rest/api/space/TWCloud2024x",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/144637972/child",
      "restrictions": "/rest/api/content/144637972/restriction/byOperation",
      "history": "/rest/api/content/144637972/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/144637972/descendant",
      "space": "/rest/api/space/TWCloud2024x",
      "relevantViewRestrictions": "/rest/api/content/144637972/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/zip"
  },
  "extensions": {
    "mediaType": "application/zip",
    "fileSize": 4462,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/144637972/HAProxy-Pkg.zip?version=1&modificationDate=1700236336198&api=v2",
    "webui": "/spaces/TWCloud2024x/pages/144637972/Layer+4+and+Layer+7+proxy+setup?preview=%2F144637972%2F144637973%2FHAProxy-Pkg.zip",
    "self": "https://docs.nomagic.com/rest/api/content/144637973"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/144637973/child",
    "restrictions": "/rest/api/content/144637973/restriction/byOperation",
    "history": "/rest/api/content/144637973/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/144637973/descendant",
    "space": "/rest/api/space/TWCloud2024x",
    "relevantViewRestrictions": "/rest/api/content/144637973/restriction/relevantViewRestrictions"
  }
}
````
