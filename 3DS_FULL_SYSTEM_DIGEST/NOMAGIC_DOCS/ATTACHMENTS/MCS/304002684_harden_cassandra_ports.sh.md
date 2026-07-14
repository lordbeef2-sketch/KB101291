# NOMAGIC ATTACHMENT: harden_cassandra_ports.sh

- attachment_id: `304002684`
- space_key: `MCS`
- parent_page_id: `304002672`
- parent_page_title: (2026x Refresh1) Downloadable scripts
- media_type: `text/x-sh`
- reported_bytes: 1472
- download_url: https://docs.nomagic.com/download/attachments/304002672/harden_cassandra_ports.sh?version=2&modificationDate=1782458090181&api=v2
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
  "id": "304002684",
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
    "when": "2026-06-26T09:14:50.181+02:00",
    "message": "",
    "number": 2,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/304002684/version/2"
    },
    "_expandable": {
      "content": "/rest/api/content/304002684"
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
    "mediaType": "text/x-sh"
  },
  "extensions": {
    "mediaType": "text/x-sh",
    "fileSize": 1472,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/304002672/harden_cassandra_ports.sh?version=2&modificationDate=1782458090181&api=v2",
    "webui": "/spaces/MCS/pages/304002672/2026x+Refresh1+Downloadable+scripts?preview=%2F304002672%2F304002684%2Fharden_cassandra_ports.sh",
    "self": "https://docs.nomagic.com/rest/api/content/304002684"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/304002684/child",
    "restrictions": "/rest/api/content/304002684/restriction/byOperation",
    "history": "/rest/api/content/304002684/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/304002684/descendant",
    "space": "/rest/api/space/MCS",
    "relevantViewRestrictions": "/rest/api/content/304002684/restriction/relevantViewRestrictions"
  }
}
````
