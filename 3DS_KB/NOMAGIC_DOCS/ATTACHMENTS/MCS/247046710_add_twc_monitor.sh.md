# NOMAGIC ATTACHMENT: add_twc_monitor.sh

- attachment_id: `247046710`
- space_key: `MCS`
- parent_page_id: `247046700`
- parent_page_title: Automated installation using scripts
- media_type: `text/x-sh`
- reported_bytes: 631
- download_url: https://docs.nomagic.com/download/attachments/247046700/add_twc_monitor.sh?version=1&modificationDate=1754923596982&api=v2
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
  "id": "247046710",
  "type": "attachment",
  "status": "current",
  "title": "add_twc_monitor.sh",
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
    "when": "2025-08-11T16:46:36.982+02:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/247046710/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/247046710"
    }
  },
  "position": -1,
  "container": {
    "id": "247046700",
    "type": "page",
    "status": "current",
    "title": "Automated installation using scripts",
    "position": 0,
    "extensions": {
      "position": 0
    },
    "_links": {
      "webui": "/spaces/MCS/pages/247046700/Automated+installation+using+scripts",
      "edit": "/pages/resumedraft.action?draftId=247046700",
      "tinyui": "/x/LKK5Dg",
      "self": "https://docs.nomagic.com/rest/api/content/247046700"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/247046700/child",
      "restrictions": "/rest/api/content/247046700/restriction/byOperation",
      "history": "/rest/api/content/247046700/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/247046700/descendant",
      "space": "/rest/api/space/MCS",
      "relevantViewRestrictions": "/rest/api/content/247046700/restriction/relevantViewRestrictions"
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
    "download": "/download/attachments/247046700/add_twc_monitor.sh?version=1&modificationDate=1754923596982&api=v2",
    "webui": "/spaces/MCS/pages/247046700/Automated+installation+using+scripts?preview=%2F247046700%2F247046710%2Fadd_twc_monitor.sh",
    "self": "https://docs.nomagic.com/rest/api/content/247046710"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/247046710/child",
    "restrictions": "/rest/api/content/247046710/restriction/byOperation",
    "history": "/rest/api/content/247046710/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/247046710/descendant",
    "space": "/rest/api/space/MCS",
    "relevantViewRestrictions": "/rest/api/content/247046710/restriction/relevantViewRestrictions"
  }
}
````
