# NOMAGIC ATTACHMENT: install_telemetry_node.sh

- attachment_id: `227171594`
- space_key: `TWCloud2024xR3`
- parent_page_id: `227171588`
- parent_page_title: Installation using scripts
- media_type: `application/x-sh`
- reported_bytes: 2260
- download_url: https://docs.nomagic.com/download/attachments/227171588/install_telemetry_node.sh?version=1&modificationDate=1746450346227&api=v2
- payload_kind: `text-exact`
- downloaded_sha256: `1ee0e887b72d953087db5391792bee85ef09b72faad61e04df6347f3f1128225`

## EXACT ATTACHMENT SOURCE

````text
#!/bin/bash
HOSTNAME=$(hostname)
IP=$(ip route get 1 | awk '{print $NF;exit}')
echo "=========================================="
echo "Installing Cassandra/Teamwork Cloud Monitoring Stack"
echo "=========================================="
echo ""
read -e -p "Please enter the IP address of the server where InfuxDB will be installed :  "  -i ""  IP
echo ""
echo "============================="
echo "Installing telegraf"
echo "============================="
cat <<EOF | sudo tee /etc/yum.repos.d/influxdb.repo
[influxdb]
name = InfluxDB Repository - RHEL \$releasever
baseurl = https://repos.influxdata.com/rhel/\$releasever/\$basearch/stable
enabled = 1
gpgcheck = 1
gpgkey = https://repos.influxdata.com/influxdb.key
EOF
sudo yum -y install telegraf
sudo sed -e "s/HOST_NAME/$IP/g" telegraf.conf.template > telegraf.conf
sudo \cp -fR telegraf.conf /etc/telegraf/telegraf.conf
echo "============================="
echo "Download and deploy metrics-graphite-3.1.2 for Cassandra monitoring"
echo "============================="
sudo wget https://repo1.maven.org/maven2/io/dropwizard/metrics/metrics-graphite/3.1.5/metrics-graphite-3.1.5.jar
sudo \cp -fR metrics-graphite-3.1.5.jar /usr/share/cassandra/lib/
sudo \cp -fR /etc/cassandra/default.conf/cassandra-env.sh /etc/cassandra/default.conf/cassandra-env.sh.backup
sudo cat <<EOF >> /etc/cassandra/default.conf/cassandra-env.sh

# Enable metrics reporting to InfluxDB using the yammer library
METRICS_REPORTER_CFG="metrics-reporter-graphite.yaml"
JVM_OPTS="\$JVM_OPTS -Dcassandra.metricsReporterConfigFile=\$METRICS_REPORTER_CFG"

EOF
sudo sed -e "s/HOST_NAME/$(hostname)/g" metrics-reporter-graphite.yaml.template > metrics-reporter-graphite.yaml
sudo sed -i "s/IP/$IP/g" metrics-reporter-graphite.yaml
sudo \cp -fR metrics-reporter-graphite.yaml /etc/cassandra/default.conf/metrics-reporter-graphite.yaml
sudo chmod 755 /etc/cassandra/default.conf/metrics-reporter-graphite.yaml
sudo yum -y install net-tools
echo "=============================="
echo "Starting Telegraf Service"
echo "=============================="
sudo systemctl start telegraf
echo "=============================="
echo "Cassandra must be restarted for telemetry to be sent to the monitoring node"
echo "=============================="

````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "227171594",
  "type": "attachment",
  "status": "current",
  "title": "install_telemetry_node.sh",
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
    "when": "2025-05-05T15:05:46.227+02:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/227171594/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/227171594"
    }
  },
  "position": -1,
  "container": {
    "id": "227171588",
    "type": "page",
    "status": "current",
    "title": "Installation using scripts",
    "position": 0,
    "extensions": {
      "position": 0
    },
    "_links": {
      "webui": "/spaces/TWCloud2024xR3/pages/227171588/Installation+using+scripts",
      "edit": "/pages/resumedraft.action?draftId=227171588",
      "tinyui": "/x/BF2KDQ",
      "self": "https://docs.nomagic.com/rest/api/content/227171588"
    },
    "_expandable": {
      "container": "/rest/api/space/TWCloud2024xR3",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/227171588/child",
      "restrictions": "/rest/api/content/227171588/restriction/byOperation",
      "history": "/rest/api/content/227171588/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/227171588/descendant",
      "space": "/rest/api/space/TWCloud2024xR3",
      "relevantViewRestrictions": "/rest/api/content/227171588/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/x-sh"
  },
  "extensions": {
    "mediaType": "application/x-sh",
    "fileSize": 2260,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/227171588/install_telemetry_node.sh?version=1&modificationDate=1746450346227&api=v2",
    "webui": "/spaces/TWCloud2024xR3/pages/227171588/Installation+using+scripts?preview=%2F227171588%2F227171594%2Finstall_telemetry_node.sh",
    "self": "https://docs.nomagic.com/rest/api/content/227171594"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/227171594/child",
    "restrictions": "/rest/api/content/227171594/restriction/byOperation",
    "history": "/rest/api/content/227171594/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/227171594/descendant",
    "space": "/rest/api/space/TWCloud2024xR3",
    "relevantViewRestrictions": "/rest/api/content/227171594/restriction/relevantViewRestrictions"
  }
}
````
