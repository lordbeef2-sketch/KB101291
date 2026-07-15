# NOMAGIC ATTACHMENT: nGinx-Proxy-Pkg.zip

- attachment_id: `144638001`
- space_key: `MCS2024x`
- parent_page_id: `144637999`
- parent_page_title: Layer 4 and Layer 7 proxy setup
- media_type: `application/zip`
- reported_bytes: 7065
- download_url: https://docs.nomagic.com/download/attachments/144637999/nGinx-Proxy-Pkg.zip?version=1&modificationDate=1700236506675&api=v2
- payload_kind: `archive-expanded`
- downloaded_sha256: `88f02581368c953a2218e0809f4ce1a335342f6a05a60a112bcb6290013da942`

## ARCHIVE CONTENTS

### ENTRY: nGinx-Proxy-Pkg/configure_nginx_layer4_tcp.sh

- bytes: 1992
- crc32: `c341169c`
- decoded_as: `utf-8`

````text
#!/bin/bash
#
# nGinx Proxy/LB depoyment and configuration script
#
NGINX_CONF=/etc/nginx/nginx.conf
STREAM_CONF=/etc/nginx/conf.d/stream.conf

echo "This script will configure nGinx as a local proxy where all services are bound to port 443"
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
echo ""
echo "Reconfiguring SELinux for http connections"
echo ""
setsebool httpd_can_network_connect on -P 
echo "Copying nGinx configuration templates"
\cp -f nginx.conf.layer4.tcp.tmpl $NGINX_CONF
\cp -f stream.conf.layer4.tcp.tmpl $STREAM_CONF
echo ""
echo "Applying configuration changes"
echo ""

sed -i "s/:SSL_PORT/:$SSL_PORT/g" $STREAM_CONF
sed -i "s/WEBAPP_IP:/$WEBAPP_IP:/g" $STREAM_CONF
sed -i "s/REST_IP:/$REST_IP:/g" $STREAM_CONF
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

### ENTRY: nGinx-Proxy-Pkg/configure_nginx_layer7_https.sh

- bytes: 2146
- crc32: `97bdadec`
- decoded_as: `utf-8`

````text
#!/bin/bash
#
# nGinx Proxy/LB depoyment and configuration script
#
NGINX_CONF=/etc/nginx/nginx.conf
STREAM_CONF=/etc/nginx/conf.d/stream.conf
HTTPS_CONF=/etc/nginx/conf.d/https.conf

echo "This script will configure nGinx as a local proxy where all services are bound to port 443"
echo ""
echo "----------------------------------------------------------------------------"
echo ""
read -e -p "Please enter the port number for Client->TWCserver Communications (Settings/Secured Connection in TWC Admin):  "  -i "10002"  SSL_PORT
echo ""
read -e -p "Please enter the IP Address for the https proxy (Webapp/AUthserver/REST):  "  -i ""  WEBAPP_IP
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
setsebool httpd_can_network_connect on -P 
echo "Copying nGinx configuration templates"
\cp -f nginx.conf.layer7.https.tmpl $NGINX_CONF
\cp -f stream.conf.layer7.https.tmpl $STREAM_CONF
\cp -f https.conf.layer7.https.tmpl $HTTPS_CONF
echo ""
echo "Applying configuration changes"
echo ""

sed -i "s/:SSL_PORT/:$SSL_PORT/g" $STREAM_CONF
sed -i "s/WEBAPP_IP:/$WEBAPP_IP:/g" $HTTPS_CONF
sed -i "s/MD_IP:/$MD_IP:/g" $STREAM_CONF
sed -i "s/FLEX_IP:/$FLEX_IP:/g" $STREAM_CONF
sed -i "s#CERT_PATH#$CERT_PATH#g" $HTTPS_CONF
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

### ENTRY: nGinx-Proxy-Pkg/example_install_nginx.sh

- bytes: 432
- crc32: `45f90767`
- decoded_as: `utf-8`

````text
#!/bin/bash
#
# Example of nGinx Proxy/LB installation on CentOS 7
#
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
````

### ENTRY: nGinx-Proxy-Pkg/https.conf.layer7.https.tmpl

- bytes: 2096
- crc32: `88737974`
- decoded_as: `utf-8`

````text
#---------------------------------------------------------------------
# nGinx Layer 7 Configuration Example (HTTPS) For TWC
#---------------------------------------------------------------------

http {

    ssl_certificate                 CERT_PATH;
    ssl_certificate_key             CERT_PATH;
    ssl_session_timeout             1d;
    ssl_session_cache               shared:TWCSSL:10m;

    #enforce TLS >= 1.2 and strong ciphers
    ssl_protocols                   TLSv1.2 TLSv1.3;

    # Mozilla SSL Configuration Generator: https://ssl-config.mozilla.org/
    ssl_ciphers                     ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers       off;
    proxy_set_header                Host $host;


    upstream webapp {
        ip_hash;
        server 127.0.0.1:8443;
    }

    upstream rest {
            ip_hash;
            server 127.0.0.1:8111;
    }

    server {
        listen WEBAPP_IP:443 ssl;
        location /webapp {
            proxy_pass https://webapp;
        }
        location /authentication {
            proxy_pass https://webapp;
        }
        location /admin {
            proxy_pass https://webapp;
        }
        location /collaborator {
            proxy_pass https://webapp;
        }
        location /document-exporter {
            proxy_pass https://webapp;
        }
        location /oslc-selection-dialog {
            proxy_pass https://webapp;
        }
        location /reports {
            proxy_pass https://webapp;
        }
        location /resources {
            proxy_pass https://webapp;
        }
        location /resource-usage-map {
            proxy_pass https://webapp;
        }
        location /simulation {
            proxy_pass https://webapp;
        }
        location /osmc {
            proxy_pass https://rest;
        }
    }
}


````

### ENTRY: nGinx-Proxy-Pkg/nginx.conf.layer4.tcp.tmpl

- bytes: 535
- crc32: `28576cd3`
- decoded_as: `utf-8`

````text
# For more information on configuration, see:
#   * Official English Documentation: http://nginx.org/en/docs/
#   * Official Russian Documentation: http://nginx.org/ru/docs/

user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

# Load dynamic modules. See /usr/share/nginx/README.dynamic.
include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024;
}

#  stream.conf contains the configuration for our TWC Proxy/Load balancer

include conf.d/stream.conf;


````

### ENTRY: nGinx-Proxy-Pkg/nginx.conf.layer7.https.tmpl

- bytes: 565
- crc32: `6a43cf5c`
- decoded_as: `utf-8`

````text
# For more information on configuration, see:
#   * Official English Documentation: http://nginx.org/en/docs/
#   * Official Russian Documentation: http://nginx.org/ru/docs/

user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

# Load dynamic modules. See /usr/share/nginx/README.dynamic.
include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024;
}

#  stream.conf contains the configuration for our TWC Proxy/Load balancer

include conf.d/stream.conf;

include conf.d/https.conf;


````

### ENTRY: nGinx-Proxy-Pkg/stream.conf.layer4.tcp.tmpl

- bytes: 3396
- crc32: `046602e3`
- decoded_as: `utf-8`

````text
# stream core module provides TCP/UDP proxying and load balancing

stream {
	
	#
	# By default, SELinux only allows the http process access to the following ports (semanage ports -l | grep http)
	#	http_port_t                    tcp      80, 81, 443, 488, 8008, 8009, 8443, 9000
	# In order for the proxy to connect to other ports, they need to either be added, or a simpler solution is to allow
	#	http to connect to all ports, by issuing the following command
	#		sudo setsebool httpd_can_network_connect on -P 
	#    
	# application.conf in TWC needs to be configured to turn off the internal load balancing in TWC on all nodes
	#     setting:  load_balancer = false (default is true) - make sure setting is uncommented
	# 
	#
	# Additional configuration in TWC
	#
	#	Create a separate keystore for webapp, authserver, and twc, based on the common names for each server
	#	i.e.  twcadmin.domain (webapp - 8443), twc.domain (twc - 8111), twcauth.domain (authserver - 8555)
	#
	#	These keystores are used an all nodes, since we will be proxying and end user systems will not see the individual nodes
	#
	# Notation in template
	#
	# 127.0.0.1 is the private (local) IP addresses for this node
	# SSL_PORT is the user defined port to which TWC will bind for TLS communications between the MD clients and TWC
	#	If you do not want to use SSL, then you can use the default of 3579
	#
	# WEBAPP_IP is the local IP address on this machine to which we will bind access to TWC Admin (8443)
	# REST_IP is the local IP address on this machine to which we will bind access to the REST API (8111)
	# AUTH_IP is the local IP address on this machine to which we will bind access to the Authserver(8555)
	# MD_IP is the local IP address on this machine to which we will bind access to the MD->TWC data stream (SSL_PORT)
	# FLEX_IP is the local IP address on this machine to which we will bind access to the cameo daemon on the FLEX server (1101)
	#
	# Each of these IP's would be resolvable to the service FQDN (and common name of TWC Admin, REST, and Authserver).
	#
	#

	# define our proxied server groups
	# hash directive is a mechanism for traffic from a given client to go to a given server
	# For a single node proxy it is not necessary, but is in the configuration for consistency when the server group consists of a load balanced group
	# the upstream servers are the nodes running TWC


	upstream webapp_servers {
		hash $remote_addr consistent;
		server 127.0.0.1:8443;
	}

	upstream rest_servers {
		hash $remote_addr consistent;
		server 127.0.0.1:8111;
	}

	upstream md_servers {
		hash $remote_addr consistent;
		server 127.0.0.1:SSL_PORT;
	}

	# define the proxy listeners

	server {
		listen WEBAPP_IP:443;
		proxy_buffer_size 16k;
		proxy_pass webapp_servers;
	}

	server {
		listen REST_IP:443;
		proxy_buffer_size 16k;
		proxy_pass rest_servers;
	}

	server {
		listen MD_IP:443;
		proxy_buffer_size 16k;
		proxy_pass md_servers;
	}

	# in this particular configuration, the FLEXNet server is running on the same server as the proxy
	# therefore, proxy_pass is pointing to localhost, since the cameo daemon binds to all ports
	# If Flex is running on a seprate instance, specify that instance's IP address

	server {
		listen FLEX_IP:443;
		proxy_buffer_size 16k;
		proxy_pass 127.0.0.1:1101;
	}
}


````

### ENTRY: nGinx-Proxy-Pkg/stream.conf.layer7.https.tmpl

- bytes: 2056
- crc32: `0b2e9146`
- decoded_as: `utf-8`

````text
# stream core module provides TCP/UDP proxying and load balancing

stream {
	
	#
	# By default, SELinux only allows the http process access to the following ports (semanage ports -l | grep http)
	#	http_port_t                    tcp      80, 81, 443, 488, 8008, 8009, 8443, 9000
	# In order for the proxy to connect to other ports, they need to either be added, or a simpler solution is to allow
	#	http to connect to all ports, by issuing the following command
	#		sudo setsebool httpd_can_network_connect on -P 
	#    
	# application.conf in TWC needs to be configured to turn off the internal load balancing in TWC on all nodes
	#     setting:  load_balancer = false (default is true) - make sure setting is uncommented
	# 
	#
	#
	# Notation in template
	#
	# 127.0.0.1 is the private (local) IP addresses for this node
	# SSL_PORT is the user defined port to which TWC will bind for TLS communications between the MD clients and TWC
	#	If you do not want to use SSL, then you can use the default of 3579
	#
	# MD_IP is the local IP address on this machine to which we will bind access to the MD->TWC data stream (SSL_PORT)
	# FLEX_IP is the local IP address on this machine to which we will bind access to the cameo daemon on the FLEX server (1101)
	#
	# Each of these IP's would be resolvable to the service FQDN (and common name of TWC Admin, REST, and Authserver).
	#
	#

	# define our proxied server groups
	# hash directive is a mechanism for traffic from a given client to go to a given server
	# For a single node proxy it is not necessary, but is in the configuration for consistency when the server group consists of a load balanced group
	# the upstream servers are the nodes running TWC


	upstream md_servers {
		hash $remote_addr consistent;
		server 127.0.0.1:SSL_PORT;
	}

	# define the proxy listeners

	server {
		listen MD_IP:443;
		proxy_buffer_size 16k;
		proxy_pass md_servers;
	}


	server {
		listen FLEX_IP:443;
		proxy_buffer_size 16k;
		proxy_pass 127.0.0.1:1101;
	}
}


````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "144638001",
  "type": "attachment",
  "status": "current",
  "title": "nGinx-Proxy-Pkg.zip",
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
    "when": "2023-11-17T16:55:06.675+01:00",
    "message": "",
    "number": 1,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/144638001/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/144638001"
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
    "mediaType": "application/zip"
  },
  "extensions": {
    "mediaType": "application/zip",
    "fileSize": 7065,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/144637999/nGinx-Proxy-Pkg.zip?version=1&modificationDate=1700236506675&api=v2",
    "webui": "/spaces/MCS2024x/pages/144637999/Layer+4+and+Layer+7+proxy+setup?preview=%2F144637999%2F144638001%2FnGinx-Proxy-Pkg.zip",
    "self": "https://docs.nomagic.com/rest/api/content/144638001"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/144638001/child",
    "restrictions": "/rest/api/content/144638001/restriction/byOperation",
    "history": "/rest/api/content/144638001/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/144638001/descendant",
    "space": "/rest/api/space/MCS2024x",
    "relevantViewRestrictions": "/rest/api/content/144638001/restriction/relevantViewRestrictions"
  }
}
````
