# NOMAGIC ATTACHMENT: install_telemetry_node.sh

- attachment_id: `218759538`
- space_key: `TWCloud2024xR2`
- parent_page_id: `218759532`
- parent_page_title: Installation using scripts
- media_type: `application/x-sh`
- reported_bytes: 2260
- download_url: https://docs.nomagic.com/download/attachments/218759532/install_telemetry_node.sh?version=1&modificationDate=1742303293311&api=v2
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
  "id": "218759538",
  "type": "attachment",
  "status": "current",
  "title": "install_telemetry_node.sh",
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
    "when": "2025-03-18T14:08:13.311+01:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/218759538/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/218759538"
    }
  },
  "position": -1,
  "container": {
    "id": "218759532",
    "type": "page",
    "status": "current",
    "title": "Installation using scripts",
    "position": 0,
    "extensions": {
      "position": 0
    },
    "_links": {
      "webui": "/spaces/TWCloud2024xR2/pages/218759532/Installation+using+scripts",
      "edit": "/pages/resumedraft.action?draftId=218759532",
      "tinyui": "/x/bAEKDQ",
      "self": "https://docs.nomagic.com/rest/api/content/218759532"
    },
    "_expandable": {
      "container": "/rest/api/space/TWCloud2024xR2",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/218759532/child",
      "restrictions": "/rest/api/content/218759532/restriction/byOperation",
      "history": "/rest/api/content/218759532/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/218759532/descendant",
      "space": "/rest/api/space/TWCloud2024xR2",
      "relevantViewRestrictions": "/rest/api/content/218759532/restriction/relevantViewRestrictions"
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
    "download": "/download/attachments/218759532/install_telemetry_node.sh?version=1&modificationDate=1742303293311&api=v2",
    "webui": "/spaces/TWCloud2024xR2/pages/218759532/Installation+using+scripts?preview=%2F218759532%2F218759538%2Finstall_telemetry_node.sh",
    "self": "https://docs.nomagic.com/rest/api/content/218759538"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/218759538/child",
    "restrictions": "/rest/api/content/218759538/restriction/byOperation",
    "history": "/rest/api/content/218759538/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/218759538/descendant",
    "space": "/rest/api/space/TWCloud2024xR2",
    "relevantViewRestrictions": "/rest/api/content/218759538/restriction/relevantViewRestrictions"
  }
}
````
