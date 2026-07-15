# NOMAGIC ATTACHMENT: add_twc_monitor.sh

- attachment_id: `218759722`
- space_key: `MCS2024xR1`
- parent_page_id: `218759712`
- parent_page_title: Installation using scripts
- media_type: `text/x-sh`
- reported_bytes: 631
- download_url: https://docs.nomagic.com/download/attachments/218759712/add_twc_monitor.sh?version=1&modificationDate=1742303709932&api=v2
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
  "id": "218759722",
  "type": "attachment",
  "status": "current",
  "title": "add_twc_monitor.sh",
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
    "when": "2025-03-18T14:15:09.932+01:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/218759722/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/218759722"
    }
  },
  "position": -1,
  "container": {
    "id": "218759712",
    "type": "page",
    "status": "current",
    "title": "Installation using scripts",
    "position": 0,
    "extensions": {
      "position": 0
    },
    "_links": {
      "webui": "/spaces/MCS2024xR1/pages/218759712/Installation+using+scripts",
      "edit": "/pages/resumedraft.action?draftId=218759712",
      "tinyui": "/x/IAIKDQ",
      "self": "https://docs.nomagic.com/rest/api/content/218759712"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS2024xR1",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/218759712/child",
      "restrictions": "/rest/api/content/218759712/restriction/byOperation",
      "history": "/rest/api/content/218759712/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/218759712/descendant",
      "space": "/rest/api/space/MCS2024xR1",
      "relevantViewRestrictions": "/rest/api/content/218759712/restriction/relevantViewRestrictions"
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
    "download": "/download/attachments/218759712/add_twc_monitor.sh?version=1&modificationDate=1742303709932&api=v2",
    "webui": "/spaces/MCS2024xR1/pages/218759712/Installation+using+scripts?preview=%2F218759712%2F218759722%2Fadd_twc_monitor.sh",
    "self": "https://docs.nomagic.com/rest/api/content/218759722"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/218759722/child",
    "restrictions": "/rest/api/content/218759722/restriction/byOperation",
    "history": "/rest/api/content/218759722/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/218759722/descendant",
    "space": "/rest/api/space/MCS2024xR1",
    "relevantViewRestrictions": "/rest/api/content/218759722/restriction/relevantViewRestrictions"
  }
}
````
