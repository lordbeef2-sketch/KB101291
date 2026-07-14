# NOMAGIC ATTACHMENT: harden_cassandra_ports.sh

- attachment_id: `137986524`
- space_key: `TWCloud2024x`
- parent_page_id: `137986520`
- parent_page_title: Hardening Teamwork Cloud and services
- media_type: `text/x-sh`
- reported_bytes: 1599
- download_url: https://docs.nomagic.com/download/attachments/137986520/harden_cassandra_ports.sh?version=1&modificationDate=1695376248434&api=v2
- payload_kind: `text-exact`
- downloaded_sha256: `20aeebb1a0b0a6308bb6770e0ffa3d7c06b1436dd5d9e35825b1ee9cc080d01c`

## EXACT ATTACHMENT SOURCE

````text
#!/bin/bash
echo "Hardening Cassandra Ports"
echo "Creating Cassandra firewall service profile"
cat <<EOF |  tee /etc/firewalld/services/cassandra.xml  &> /dev/null
<?xml version="1.0" encoding="utf-8"?>
<service version="1.0">
    <short>cassandra</short>
    <description>cassandra</description>
    <port port="7000" protocol="tcp"/>
    <port port="7001" protocol="tcp"/>
	<port port="9042" protocol="tcp"/>
	<port port="9160" protocol="tcp"/>
	<port port="9142" protocol="tcp"/>
</service>
EOF
echo "Removing existing firewall rules on the cassandra ports or service profile"
sleep 5 
zone=$(firewall-cmd --get-default) &> /dev/null
firewall-cmd --zone=$zone --remove-port=7000/tcp --permanent  &> /dev/null
firewall-cmd --zone=$zone --remove-port=7001/tcp --permanent  &> /dev/null
firewall-cmd --zone=$zone --remove-port=7199/tcp --permanent  &> /dev/null
firewall-cmd --zone=$zone --remove-port=9042/tcp --permanent  &> /dev/null
firewall-cmd --zone=$zone --remove-port=9160/tcp --permanent  &> /dev/null
firewall-cmd --zone=$zone --remove-port=9142/tcp --permanent  &> /dev/null
firewall-cmd --zone=$zone --remove-service=cassandra --permanent  &> /dev/null
echo "Creating ruch rules for Cassandra nodes discovered via nodetool gossipinfo"
set -f
local_list=($(nodetool gossipinfo | grep '/' | cut -f 2 -d /)) 
set +f
for i in "${local_list[@]}" ; do
        cmd=" firewall-cmd --zone=$zone --add-rich-rule='rule family=\"ipv4\" source address=\"$i\" service name=\"cassandra\" accept' --permanent  &> /dev/null"
        echo $cmd
        eval $cmd
done
firewall-cmd --reload  &> /dev/null

````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "137986524",
  "type": "attachment",
  "status": "current",
  "title": "harden_cassandra_ports.sh",
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
    "when": "2023-09-22T11:50:48.434+02:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/137986524/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/137986524"
    }
  },
  "position": -1,
  "container": {
    "id": "137986520",
    "type": "page",
    "status": "current",
    "title": "Hardening Teamwork Cloud and services",
    "position": 3,
    "extensions": {
      "position": 3
    },
    "_links": {
      "webui": "/spaces/TWCloud2024x/pages/137986520/Hardening+Teamwork+Cloud+and+services",
      "edit": "/pages/resumedraft.action?draftId=137986520",
      "tinyui": "/x/2IE5C",
      "self": "https://docs.nomagic.com/rest/api/content/137986520"
    },
    "_expandable": {
      "container": "/rest/api/space/TWCloud2024x",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/137986520/child",
      "restrictions": "/rest/api/content/137986520/restriction/byOperation",
      "history": "/rest/api/content/137986520/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/137986520/descendant",
      "space": "/rest/api/space/TWCloud2024x",
      "relevantViewRestrictions": "/rest/api/content/137986520/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "text/x-sh"
  },
  "extensions": {
    "mediaType": "text/x-sh",
    "fileSize": 1599,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/137986520/harden_cassandra_ports.sh?version=1&modificationDate=1695376248434&api=v2",
    "webui": "/spaces/TWCloud2024x/pages/137986520/Hardening+Teamwork+Cloud+and+services?preview=%2F137986520%2F137986524%2Fharden_cassandra_ports.sh",
    "self": "https://docs.nomagic.com/rest/api/content/137986524"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/137986524/child",
    "restrictions": "/rest/api/content/137986524/restriction/byOperation",
    "history": "/rest/api/content/137986524/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/137986524/descendant",
    "space": "/rest/api/space/TWCloud2024x",
    "relevantViewRestrictions": "/rest/api/content/137986524/restriction/relevantViewRestrictions"
  }
}
````
