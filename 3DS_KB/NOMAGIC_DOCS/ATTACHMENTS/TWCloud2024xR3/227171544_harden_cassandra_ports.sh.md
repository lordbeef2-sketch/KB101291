# NOMAGIC ATTACHMENT: harden_cassandra_ports.sh

- attachment_id: `227171544`
- space_key: `TWCloud2024xR3`
- parent_page_id: `227171543`
- parent_page_title: Hardening Cassandra
- media_type: `text/x-sh`
- reported_bytes: 1472
- download_url: https://docs.nomagic.com/download/attachments/227171543/harden_cassandra_ports.sh?version=3&modificationDate=1761048889778&api=v2
- payload_kind: `text-exact`
- downloaded_sha256: `e7eb4dd96d89c72998bbc30d7b84238842e29748b0e62a6f2cfcc4060fc7e819`

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
firewall-cmd --zone=$zone --remove-port=9142/tcp --permanent  &> /dev/null
firewall-cmd --zone=$zone --remove-service=cassandra --permanent  &> /dev/null
echo "Creating rich rules for Cassandra nodes discovered via nodetool gossipinfo"
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
  "id": "227171544",
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
    "when": "2025-10-21T14:14:49.778+02:00",
    "message": "",
    "number": 3,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/227171544/version/3"
    },
    "_expandable": {
      "content": "/rest/api/content/227171544"
    }
  },
  "position": -1,
  "container": {
    "id": "227171543",
    "type": "page",
    "status": "current",
    "title": "Hardening Cassandra",
    "position": 0,
    "extensions": {
      "position": 0
    },
    "_links": {
      "webui": "/spaces/TWCloud2024xR3/pages/227171543/Hardening+Cassandra",
      "edit": "/pages/resumedraft.action?draftId=227171543",
      "tinyui": "/x/11yKDQ",
      "self": "https://docs.nomagic.com/rest/api/content/227171543"
    },
    "_expandable": {
      "container": "/rest/api/space/TWCloud2024xR3",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/227171543/child",
      "restrictions": "/rest/api/content/227171543/restriction/byOperation",
      "history": "/rest/api/content/227171543/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/227171543/descendant",
      "space": "/rest/api/space/TWCloud2024xR3",
      "relevantViewRestrictions": "/rest/api/content/227171543/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "text/x-sh"
  },
  "extensions": {
    "mediaType": "text/x-sh",
    "fileSize": 1472,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/227171543/harden_cassandra_ports.sh?version=3&modificationDate=1761048889778&api=v2",
    "webui": "/spaces/TWCloud2024xR3/pages/227171543/Hardening+Cassandra?preview=%2F227171543%2F227171544%2Fharden_cassandra_ports.sh",
    "self": "https://docs.nomagic.com/rest/api/content/227171544"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/227171544/child",
    "restrictions": "/rest/api/content/227171544/restriction/byOperation",
    "history": "/rest/api/content/227171544/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/227171544/descendant",
    "space": "/rest/api/space/TWCloud2024xR3",
    "relevantViewRestrictions": "/rest/api/content/227171544/restriction/relevantViewRestrictions"
  }
}
````
