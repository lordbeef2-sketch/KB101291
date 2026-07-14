# NOMAGIC ATTACHMENT: install_monitoring_node.sh

- attachment_id: `218759801`
- space_key: `MCS2024xR2`
- parent_page_id: `218759799`
- parent_page_title: Installation using scripts
- media_type: `text/x-sh`
- reported_bytes: 5018
- download_url: https://docs.nomagic.com/download/attachments/218759799/install_monitoring_node.sh?version=1&modificationDate=1742303747776&api=v2
- payload_kind: `text-exact`
- downloaded_sha256: `43fd824c182fb2afe2fb6617aa4bc9b25f645a8b7c2fe8c1c29419ab8d094573`

## EXACT ATTACHMENT SOURCE

````text
#!/bin/bash
echo "=========================================="
echo "Installing Monitoring Node Components     "
echo "=========================================="
HOSTNAME=$(hostname)
FWZONE=$(sudo firewall-cmd --get-default-zone)
echo "Installing InfluxDB"
echo "============================="
sudo yum install -y wget
sudo yum install -y curl
cat <<EOF | sudo tee /etc/yum.repos.d/influxdata.repo
[influxdata]
name = InfluxData Repository - Stable
baseurl = https://repos.influxdata.com/stable/\$basearch/main
enabled = 1
gpgcheck = 1
gpgkey = https://repos.influxdata.com/influxdata-archive_compat.key
EOF
sudo yum -y install influxdb
echo "============================="
echo "Opening firewall for InfluxDB"
echo "============================="
cat <<EOF | sudo tee /etc/firewalld/services/influxdb.xml
<?xml version="1.0" encoding="utf-8"?>
<service version="1.0">
    <short>influxdb</short>
    <description>InfluxDB</description>
    <port port="8086" protocol="tcp"/>
    <port port="2003" protocol="tcp"/>
</service>
EOF
sleep 10
sudo firewall-cmd --permanent --zone=$FWZONE --add-service=influxdb
sudo systemctl enable influxdb.service
echo "============================="
echo "Installing Grafana"
echo "============================="
sudo yum install -y https://s3-us-west-2.amazonaws.com/grafana-releases/release/grafana-5.2.1-1.x86_64.rpm 

cat <<EOF | sudo tee /etc/firewalld/services/grafana.xml
<?xml version="1.0" encoding="utf-8"?>
<service version="1.0">
    <short>grafana</short>
    <description>Grafana</description>
    <port port="3000" protocol="tcp"/>
</service>
EOF
sleep 5
echo ""
sudo firewall-cmd --permanent --zone=$FWZONE --add-service=grafana
sudo firewall-cmd --reload
sudo systemctl enable grafana-server.service
echo "============================"
echo "Installing jmxtrans"
echo "============================"
sudo yum -y install  https://repo1.maven.org/maven2/org/jmxtrans/jmxtrans/272/jmxtrans-272.rpm
sudo chkconfig --del jmxtrans
read -e -p "Please enter the hostname of the Teamwork Cloud Node (as obtained via the hostname command):  "  -i ""  HOSTNAME
echo "" 
read -e -p "Please enter the IP Address of the Teamwork Cloud Node:  "  -i ""  IPADDRESS
echo "" 
JMXFILE=twcloud-$HOSTNAME.json
sudo sed -e "s/HOST_NAME/$HOSTNAME/g" twcloud.json.template > $JMXFILE
sudo sed -i "s/IP_ADDRESS/$IPADDRESS/g" $JMXFILE

sudo chmod 755 $JMXFILE
sudo \cp -fR $JMXFILE /var/lib/jmxtrans/

cat <<EOF | sudo tee /etc/systemd/system/jmxtrans.service
[Unit]
Description=JMX Transformer - more than meets the eye
After=syslog.target network.target

[Service]
Type=forking
User=jmxtrans
Group=jmxtrans
# Run ExecStartPre with root-permissions
PermissionsStartOnly=true
ExecStartPre=-/usr/bin/mkdir /run/jmxtrans/
ExecStartPre=/usr/bin/chown -R jmxtrans:jmxtrans /run/jmxtrans/
PIDFile=/var/run/jmxtrans/jmxtrans.pid
ExecStart=/usr/share/jmxtrans/bin/jmxtrans start

[Install]
WantedBy=multi-user.target
 

EOF
sleep 5
sudo chmod +x /etc/systemd/system/jmxtrans.service
sudo sed -i '/wrapper.app.parameter.3/a wrapper.app.parameter.4=-s\nwrapper.app.parameter.5=30\n' /etc/jmxtrans/wrapper.conf 
sudo systemctl enable jmxtrans
echo "==========================="
echo "Initializing influxdb databases with 35 day retention"
echo "==========================="
sudo cp influxdb.conf /etc/influxdb/influxdb.conf
sudo systemctl daemon-reload
sudo systemctl enable influxdb

sudo systemctl start influxdb
sleep 5
sudo influx -execute "CREATE DATABASE graphite with duration 35d"
sudo influx -execute "CREATE DATABASE telegraf with duration 35d"
sudo influx -execute "CREATE DATABASE twcloud with duration 35d"  
sudo influx -execute "CREATE DATABASE webapp with duration 35d"  
sudo systemctl daemon-reload
echo "==========================="
echo "Starting Grafana Server"
echo "==========================="
sudo systemctl enable grafana-server
sudo systemctl start grafana-server
echo "==========================="
echo "Starting jmxtrans"
echo "==========================="
sudo systemctl enable jmxtrans
sudo systemctl start jmxtrans
echo "=========================="
echo "Reloading firewall rules"
echo "=========================="
sudo firewall-cmd --reload
echo "=========================="
echo "Create Grafana Datasources"
echo "=========================="
sudo curl -X POST -H "Content-Type: application/json" -d @datasource1.json http://admin:admin@localhost:3000/api/datasources
sudo curl -X POST -H "Content-Type: application/json" -d @datasource2.json http://admin:admin@localhost:3000/api/datasources
sudo curl -X POST -H "Content-Type: application/json" -d @datasource3.json http://admin:admin@localhost:3000/api/datasources 
sudo curl -X POST -H "Content-Type: application/json" -d @datasource4.json http://admin:admin@localhost:3000/api/datasources 
echo "=========================="
echo "Create Grafana Guest User" 
echo "=========================="
sudo curl -X POST -H "Content-Type: application/json" -d @createguest.json http://admin:admin@localhost:3000/api/admin/users/

````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "218759801",
  "type": "attachment",
  "status": "current",
  "title": "install_monitoring_node.sh",
  "version": {
    "by": {
      "type": "known",
      "username": "agnpal",
      "userKey": "ff80808151426f0e0151af8b0d360002",
      "profilePicture": {
        "path": "/download/attachments/6598412/user-avatar",
        "width": 48,
        "height": 48,
        "isDefault": false
      },
      "displayName": "Agne P.",
      "_links": {
        "self": "https://docs.nomagic.com/rest/api/user?key=ff80808151426f0e0151af8b0d360002"
      },
      "_expandable": {
        "status": ""
      }
    },
    "when": "2025-03-18T14:15:47.776+01:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/218759801/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/218759801"
    }
  },
  "position": -1,
  "container": {
    "id": "218759799",
    "type": "page",
    "status": "current",
    "title": "Installation using scripts",
    "position": 0,
    "extensions": {
      "position": 0
    },
    "_links": {
      "webui": "/spaces/MCS2024xR2/pages/218759799/Installation+using+scripts",
      "edit": "/pages/resumedraft.action?draftId=218759799",
      "tinyui": "/x/dwIKDQ",
      "self": "https://docs.nomagic.com/rest/api/content/218759799"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS2024xR2",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/218759799/child",
      "restrictions": "/rest/api/content/218759799/restriction/byOperation",
      "history": "/rest/api/content/218759799/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/218759799/descendant",
      "space": "/rest/api/space/MCS2024xR2",
      "relevantViewRestrictions": "/rest/api/content/218759799/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "text/x-sh"
  },
  "extensions": {
    "mediaType": "text/x-sh",
    "fileSize": 5018,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/218759799/install_monitoring_node.sh?version=1&modificationDate=1742303747776&api=v2",
    "webui": "/spaces/MCS2024xR2/pages/218759799/Installation+using+scripts?preview=%2F218759799%2F218759801%2Finstall_monitoring_node.sh",
    "self": "https://docs.nomagic.com/rest/api/content/218759801"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/218759801/child",
    "restrictions": "/rest/api/content/218759801/restriction/byOperation",
    "history": "/rest/api/content/218759801/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/218759801/descendant",
    "space": "/rest/api/space/MCS2024xR2",
    "relevantViewRestrictions": "/rest/api/content/218759801/restriction/relevantViewRestrictions"
  }
}
````
