# NOMAGIC ATTACHMENT: install_proxy_nginx_tcp.sh

- attachment_id: `144638013`
- space_key: `MCS2024x`
- parent_page_id: `144637999`
- parent_page_title: Layer 4 and Layer 7 proxy setup
- media_type: `text/x-sh`
- reported_bytes: 2536
- download_url: https://docs.nomagic.com/download/attachments/144637999/install_proxy_nginx_tcp.sh?version=1&modificationDate=1700236506721&api=v2
- payload_kind: `text-exact`
- downloaded_sha256: `fcc1f459a8f02c6875502564f4ebd7d649eb6b3388f8aab663dbbcc12d75a25c`

## EXACT ATTACHMENT SOURCE

````text
#!/bin/bash
#
# nGinx Proxy/LB depoyment and configuration script
#
# Benjamin Krajmalnik (benjamin.krajmalnik@3ds.com)
# 
NGINX_CONF=/etc/nginx/nginx.conf
STREAM_CONF=/etc/nginx/conf.d/stream.conf

echo "This script will deploy and configure nGinx as a local proxy where all services are bound to port 443"
echo ""
echo "----------------------------------------------------------------------------"
echo ""
read -e -p "Please enter the port number for MD->TWC Communications (Settings/Secured Connection in TWC Admin):  "  -i "10002"  SSL_PORT
echo ""
read -e -p "Please enter the IP Address for the Webapp Proxy:  "  -i ""  WEBAPP_IP
echo ""
read -e -p "Please enter the IP Address for the REST API Proxy:  "  -i ""  REST_IP  
echo ""
read -e -p "Please enter the IP Address for the Authserver Proxy:  "  -i ""  AUTH_IP  
echo ""
read -e -p "Please enter the IP Address for the MD->TWC Proxy:  "  -i ""  MD_IP  
echo ""
read -e -p "Please enter the IP Address for the FlexNET Proxy:  "  -i ""  FLEX_IP  
echo ""
echo "----------------------------------------------------------------------------"
echo ""
OS=$(cat /etc/redhat-release | cut -f 1 -d " ");
if [ $OS = 'CentOS' ] 
then
	echo "Installing epel-release for CentOS"
	yum -y -q install epel-release
else
	echo "Installing epel-release for RHEL"
	rpm -ivh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
	yum -y -q update
fi
echo ""
echo "Installing nGinx"
yum -y -q install nginx
echo ""
echo "Reconfiguring SELinux for http connections"
echo ""
setsebool httpd_can_network_connect on -P 
echo "Copying nGinx configuration templates"
\cp -f nginx.conf.template.tcp $NGINX_CONF
\cp -f stream.conf.template.tcp $STREAM_CONF
echo ""
echo "Applying configuration changes"
echo ""

sed -i "s/:SSL_PORT/:$SSL_PORT/g" $STREAM_CONF
sed -i "s/WEBAPP_IP:/$WEBAPP_IP:/g" $STREAM_CONF
sed -i "s/REST_IP:/$REST_IP:/g" $STREAM_CONF
sed -i "s/AUTH_IP:/$AUTH_IP:/g" $STREAM_CONF
sed -i "s/MD_IP:/$MD_IP:/g" $STREAM_CONF
sed -i "s/FLEX_IP:/$FLEX_IP:/g" $STREAM_CONF
echo ""
echo "Configuring firewall rule to allow port 443"
FWZONE=$(firewall-cmd --get-default-zone)
echo "Discovered firewall zone $FWZONE"
cat <<EOF | tee /etc/firewalld/services/nginx.xml
<?xml version="1.0" encoding="utf-8"?>
<service version="1.0">
    <short>nginx</short>
    <description>nginx</description>
    <port port="443" protocol="tcp"/>
</service>
EOF
sleep 5
firewall-cmd --zone=$FWZONE --add-service=nginx --permanent
firewall-cmd --reload 
echo "nGInx Local Proxy Deployment Complete"

````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "144638013",
  "type": "attachment",
  "status": "current",
  "title": "install_proxy_nginx_tcp.sh",
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
    "when": "2023-11-17T16:55:06.721+01:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/144638013/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/144638013"
    }
  },
  "position": -1,
  "container": {
    "id": "144637999",
    "type": "page",
    "status": "current",
    "title": "Layer 4 and Layer 7 proxy setup",
    "position": 5,
    "extensions": {
      "position": 5
    },
    "_links": {
      "webui": "/spaces/MCS2024x/pages/144637999/Layer+4+and+Layer+7+proxy+setup",
      "edit": "/pages/resumedraft.action?draftId=144637999",
      "tinyui": "/x/LwCfC",
      "self": "https://docs.nomagic.com/rest/api/content/144637999"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS2024x",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/144637999/child",
      "restrictions": "/rest/api/content/144637999/restriction/byOperation",
      "history": "/rest/api/content/144637999/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/144637999/descendant",
      "space": "/rest/api/space/MCS2024x",
      "relevantViewRestrictions": "/rest/api/content/144637999/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "text/x-sh"
  },
  "extensions": {
    "mediaType": "text/x-sh",
    "fileSize": 2536,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/144637999/install_proxy_nginx_tcp.sh?version=1&modificationDate=1700236506721&api=v2",
    "webui": "/spaces/MCS2024x/pages/144637999/Layer+4+and+Layer+7+proxy+setup?preview=%2F144637999%2F144638013%2Finstall_proxy_nginx_tcp.sh",
    "self": "https://docs.nomagic.com/rest/api/content/144638013"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/144638013/child",
    "restrictions": "/rest/api/content/144638013/restriction/byOperation",
    "history": "/rest/api/content/144638013/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/144638013/descendant",
    "space": "/rest/api/space/MCS2024x",
    "relevantViewRestrictions": "/rest/api/content/144638013/restriction/relevantViewRestrictions"
  }
}
````
