# NOMAGIC ATTACHMENT: add_twc_monitor.sh

- attachment_id: `303988788`
- space_key: `MCS`
- parent_page_id: `303988766`
- parent_page_title: (2026x) Automated installation using scripts
- media_type: `text/x-sh`
- reported_bytes: 631
- download_url: https://docs.nomagic.com/download/attachments/303988766/add_twc_monitor.sh?version=1&modificationDate=1777300154163&api=v2
- payload_kind: `text-exact`
- downloaded_sha256: `349ea6c78f712e1cffb15c25186febe9e0755cbc6a32000dd672ee9059e60d12`

## EXACT ATTACHMENT SOURCE

````text
#!/bin/bash
echo "=========================================="
echo "Monitor additional TWC node     "
echo "=========================================="
read -e -p "Please enter the hostname of the Teamwork Cloud Node (as obtained via the hostname command):  "  -i ""  HOSTNAME
echo "" 
read -e -p "Please enter the IP Address of the Teamwork Cloud Node:  "  -i ""  IPADDRESS
echo "" 
JMXFILE=twcloud-$HOSTNAME.json
sudo sed -e "s/HOST_NAME/$HOSTNAME/g" twcloud.json.template > $JMXFILE
sudo sed -i "s/IP_ADDRESS/$IPADDRESS/g" $JMXFILE
sudo chmod 755 $JMXFILE
sudo \cp -fR $JMXFILE /var/lib/jmxtrans/
sudo systemctl restart jmxtrans
````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "303988788",
  "type": "attachment",
  "status": "current",
  "title": "add_twc_monitor.sh",
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
    "when": "2026-04-27T16:29:14.163+02:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/303988788/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/303988788"
    }
  },
  "position": -1,
  "container": {
    "id": "303988766",
    "type": "page",
    "status": "current",
    "title": "(2026x) Automated installation using scripts",
    "position": 0,
    "extensions": {
      "position": 0
    },
    "_links": {
      "webui": "/spaces/MCS/pages/303988766/2026x+Automated+installation+using+scripts",
      "edit": "/pages/resumedraft.action?draftId=303988766",
      "tinyui": "/x/HoAeEg",
      "self": "https://docs.nomagic.com/rest/api/content/303988766"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/303988766/child",
      "restrictions": "/rest/api/content/303988766/restriction/byOperation",
      "history": "/rest/api/content/303988766/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/303988766/descendant",
      "space": "/rest/api/space/MCS",
      "relevantViewRestrictions": "/rest/api/content/303988766/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "text/x-sh"
  },
  "extensions": {
    "mediaType": "text/x-sh",
    "fileSize": 631,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/303988766/add_twc_monitor.sh?version=1&modificationDate=1777300154163&api=v2",
    "webui": "/spaces/MCS/pages/303988766/2026x+Automated+installation+using+scripts?preview=%2F303988766%2F303988788%2Fadd_twc_monitor.sh",
    "self": "https://docs.nomagic.com/rest/api/content/303988788"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/303988788/child",
    "restrictions": "/rest/api/content/303988788/restriction/byOperation",
    "history": "/rest/api/content/303988788/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/303988788/descendant",
    "space": "/rest/api/space/MCS",
    "relevantViewRestrictions": "/rest/api/content/303988788/restriction/relevantViewRestrictions"
  }
}
````
