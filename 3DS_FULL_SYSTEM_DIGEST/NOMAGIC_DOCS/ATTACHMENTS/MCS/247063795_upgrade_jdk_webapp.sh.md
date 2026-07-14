# NOMAGIC ATTACHMENT: upgrade_jdk_webapp.sh

- attachment_id: `247063795`
- space_key: `MCS`
- parent_page_id: `247063790`
- parent_page_title: (2026x) Hardening the deployment and its services
- media_type: `text/x-sh`
- reported_bytes: 2118
- download_url: https://docs.nomagic.com/download/attachments/247063790/upgrade_jdk_webapp.sh?version=1&modificationDate=1755163542089&api=v2
- payload_kind: `text-exact`
- downloaded_sha256: `4ece4842037fdfe93c0407fa92b76dc3017e4859df82e9b3fa8fdc4adfcd0c34`

## EXACT ATTACHMENT SOURCE

````text
#!/bin/bash
##################################################################
#  Upgrade JDK in CATIA NoMagic Webapp Platform to a newer OpenJDK
#  CATIA No Magic DevOps Team
##################################################################

###  JRE_DOWNLOAD contains the download URL to the target OpenJDK tar archive
###  The example below upgrades the JDK to OpenJDK 17.0.5+8

# Edit default version if you can't input it during upgrade
DEFAULT_VERSION=17.0.5+8

###########################################
#
#  DO NOT MODIFY ANYTHING BELOW THIS POINT
#
###########################################

echo ""
echo "-------------------------------------------------------------------------------------------------------------------------------------"
read -e -p "Please enter OpenJDK version of JRE you would like to use in the same style as it is in example [default is: $DEFAULT_VERSION] : " JRE_VERSION
echo "--------------------------------------------------------------------------------------------------------------------------------------"
echo ""
JRE_VERSION="${JRE_VERSION:-$DEFAULT_VERSION}"

echo "OpenJDK will be upgraded to: "$JRE_VERSION "version."

MAJOR_VERSION=$(echo $JRE_VERSION | cut -d . -f 1)
DOWNLOAD_VERSION=${JRE_VERSION/+/_}
echo $DOWNLOAD_VERSION

###  JRE_DOWNLOAD contains the download URL to the target OpenJDK tar archive
JRE_DOWNLOAD=https://github.com/adoptium/temurin$MAJOR_VERSION-binaries/releases/download/jdk-$JRE_VERSION/OpenJDK17U-jre_x64_linux_hotspot_$DOWNLOAD_VERSION.tar.gz

#####################################
#  Install wget
yum install wget -y -q

JRE_HOME=$(cat /etc/systemd/system/webapp.service | grep JRE_HOME | cut -f 3 -d '=')
JRE_OWNER=$(stat -c "%U:%G" $JRE_HOME)
JRE_TAR=$(basename $JRE_DOWNLOAD)
mkdir _tmp
cd _tmp

##   Download OpenJDK
wget $JRE_DOWNLOAD

##  Remove current JRE_HOME
rm -fr $JRE_HOME

##  Extract OpenJDK
mkdir -p $JRE_HOME
tar -xf $JRE_TAR -C $JRE_HOME --strip-components=1
chown -R $JRE_OWNER $JRE_HOME

####################################
# Remove foder with extracted files
cd ..
rm -fr _tmp
echo "Upgrade completed successfully."

````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "247063795",
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
    "when": "2025-08-14T11:25:42.089+02:00",
    "message": "",
    "number": 1,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/247063795/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/247063795"
    }
  },
  "position": -1,
  "container": {
    "id": "247063790",
    "type": "page",
    "status": "current",
    "title": "(2026x) Hardening the deployment and its services",
    "position": 3,
    "extensions": {
      "position": 3
    },
    "_links": {
      "webui": "/spaces/MCS/pages/247063790/2026x+Hardening+the+deployment+and+its+services",
      "edit": "/pages/resumedraft.action?draftId=247063790",
      "tinyui": "/x/7uS5Dg",
      "self": "https://docs.nomagic.com/rest/api/content/247063790"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/247063790/child",
      "restrictions": "/rest/api/content/247063790/restriction/byOperation",
      "history": "/rest/api/content/247063790/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/247063790/descendant",
      "space": "/rest/api/space/MCS",
      "relevantViewRestrictions": "/rest/api/content/247063790/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "text/x-sh"
  },
  "extensions": {
    "mediaType": "text/x-sh",
    "fileSize": 2118,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/247063790/upgrade_jdk_webapp.sh?version=1&modificationDate=1755163542089&api=v2",
    "webui": "/spaces/MCS/pages/247063790/2026x+Hardening+the+deployment+and+its+services?preview=%2F247063790%2F247063795%2Fupgrade_jdk_webapp.sh",
    "self": "https://docs.nomagic.com/rest/api/content/247063795"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/247063795/child",
    "restrictions": "/rest/api/content/247063795/restriction/byOperation",
    "history": "/rest/api/content/247063795/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/247063795/descendant",
    "space": "/rest/api/space/MCS",
    "relevantViewRestrictions": "/rest/api/content/247063795/restriction/relevantViewRestrictions"
  }
}
````
