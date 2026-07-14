# NOMAGIC ATTACHMENT: upgrade_jdk_webapp.sh

- attachment_id: `189149944`
- space_key: `TWCloud2024xR2`
- parent_page_id: `189149943`
- parent_page_title: Installing Web Application Platform on Linux with GUI
- media_type: `application/x-sh`
- reported_bytes: 777
- download_url: https://docs.nomagic.com/download/attachments/189149943/upgrade_jdk_webapp.sh?version=1&modificationDate=1728044291158&api=v2
- payload_kind: `text-exact`
- downloaded_sha256: `aebb60db86c452bc7452ffcc6da022ebb8196fdec1b4f6a1fe6e1cd6b1913682`

## EXACT ATTACHMENT SOURCE

````text
#!/bin/bash
###  JRE_DOWNLOAD contains the download URL to the target OpenJDK tar archive
###  The example below upgrades the JRE to OpenJDK JRE 17.0.8+7

JRE_DOWNLOAD=https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.8%2B7/OpenJDK17U-jre_x64_linux_hotspot_17.0.8_7.tar.gz

#####  Do not modify below this point  ######

JRE_HOME=$(cat /etc/systemd/system/webapp.service | grep JRE_HOME | cut -f 3 -d '=')
JRE_OWNER=$(stat -c "%U:%G" $JRE_HOME)
JRE_TAR=$(basename $JRE_DOWNLOAD)
mkdir _tmp
cd _tmp
##   Download OpenJDK JRE
wget $JRE_DOWNLOAD

##  Remove current JRE_HOME
rm -fr $JRE_HOME

##  Extract OpenJDK
mkdir -p $JRE_HOME
tar -xf $JRE_TAR -C $JRE_HOME --strip-components=1
chown -R $JRE_OWNER $JRE_HOME

cd ..
rm -fr _tmp
````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "189149944",
  "type": "attachment",
  "status": "current",
  "title": "upgrade_jdk_webapp.sh",
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
    "when": "2024-10-04T14:18:11.158+02:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/189149944/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/189149944"
    }
  },
  "position": -1,
  "container": {
    "id": "189149943",
    "type": "page",
    "status": "current",
    "title": "Installing Web Application Platform on Linux with GUI",
    "position": 2,
    "extensions": {
      "position": 2
    },
    "_links": {
      "webui": "/spaces/TWCloud2024xR2/pages/189149943/Installing+Web+Application+Platform+on+Linux+with+GUI",
      "edit": "/pages/resumedraft.action?draftId=189149943",
      "tinyui": "/x/9zJGCw",
      "self": "https://docs.nomagic.com/rest/api/content/189149943"
    },
    "_expandable": {
      "container": "/rest/api/space/TWCloud2024xR2",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/189149943/child",
      "restrictions": "/rest/api/content/189149943/restriction/byOperation",
      "history": "/rest/api/content/189149943/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/189149943/descendant",
      "space": "/rest/api/space/TWCloud2024xR2",
      "relevantViewRestrictions": "/rest/api/content/189149943/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/x-sh"
  },
  "extensions": {
    "mediaType": "application/x-sh",
    "fileSize": 777,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/189149943/upgrade_jdk_webapp.sh?version=1&modificationDate=1728044291158&api=v2",
    "webui": "/spaces/TWCloud2024xR2/pages/189149943/Installing+Web+Application+Platform+on+Linux+with+GUI?preview=%2F189149943%2F189149944%2Fupgrade_jdk_webapp.sh",
    "self": "https://docs.nomagic.com/rest/api/content/189149944"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/189149944/child",
    "restrictions": "/rest/api/content/189149944/restriction/byOperation",
    "history": "/rest/api/content/189149944/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/189149944/descendant",
    "space": "/rest/api/space/TWCloud2024xR2",
    "relevantViewRestrictions": "/rest/api/content/189149944/restriction/relevantViewRestrictions"
  }
}
````
