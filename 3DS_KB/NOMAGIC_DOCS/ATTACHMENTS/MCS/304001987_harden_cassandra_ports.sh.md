# NOMAGIC ATTACHMENT: harden_cassandra_ports.sh

- attachment_id: `304001987`
- space_key: `MCS`
- parent_page_id: `304001985`
- parent_page_title: (2026x Refresh1) Hardening the deployment and its services
- media_type: `text/x-sh`
- reported_bytes: 1599
- download_url: https://docs.nomagic.com/download/attachments/304001985/harden_cassandra_ports.sh?version=1&modificationDate=1777452435317&api=v2
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
  "id": "304001987",
  "type": "attachment",
  "status": "current",
  "title": "harden_cassandra_ports.sh",
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
    "when": "2026-04-29T10:47:15.317+02:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/304001987/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/304001987"
    }
  },
  "position": -1,
  "container": {
    "id": "304001985",
    "type": "page",
    "status": "current",
    "title": "(2026x Refresh1) Hardening the deployment and its services",
    "position": 3,
    "extensions": {
      "position": 3
    },
    "_links": {
      "webui": "/spaces/MCS/pages/304001985/2026x+Refresh1+Hardening+the+deployment+and+its+services",
      "edit": "/pages/resumedraft.action?draftId=304001985",
      "tinyui": "/x/wbMeEg",
      "self": "https://docs.nomagic.com/rest/api/content/304001985"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/304001985/child",
      "restrictions": "/rest/api/content/304001985/restriction/byOperation",
      "history": "/rest/api/content/304001985/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/304001985/descendant",
      "space": "/rest/api/space/MCS",
      "relevantViewRestrictions": "/rest/api/content/304001985/restriction/relevantViewRestrictions"
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
    "download": "/download/attachments/304001985/harden_cassandra_ports.sh?version=1&modificationDate=1777452435317&api=v2",
    "webui": "/spaces/MCS/pages/304001985/2026x+Refresh1+Hardening+the+deployment+and+its+services?preview=%2F304001985%2F304001987%2Fharden_cassandra_ports.sh",
    "self": "https://docs.nomagic.com/rest/api/content/304001987"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/304001987/child",
    "restrictions": "/rest/api/content/304001987/restriction/byOperation",
    "history": "/rest/api/content/304001987/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/304001987/descendant",
    "space": "/rest/api/space/MCS",
    "relevantViewRestrictions": "/rest/api/content/304001987/restriction/relevantViewRestrictions"
  }
}
````
