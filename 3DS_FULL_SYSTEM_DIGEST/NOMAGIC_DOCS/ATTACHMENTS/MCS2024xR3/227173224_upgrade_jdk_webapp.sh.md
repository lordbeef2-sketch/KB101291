# NOMAGIC ATTACHMENT: upgrade_jdk_webapp.sh

- attachment_id: `227173224`
- space_key: `MCS2024xR3`
- parent_page_id: `227173220`
- parent_page_title: Hardening Magic Collaboration Studio
- media_type: `text/x-sh`
- reported_bytes: 2118
- download_url: https://docs.nomagic.com/download/attachments/227173220/upgrade_jdk_webapp.sh?version=1&modificationDate=1746452088945&api=v2
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
  "id": "227173224",
  "type": "attachment",
  "status": "current",
  "title": "upgrade_jdk_webapp.sh",
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
    "when": "2025-05-05T15:34:48.945+02:00",
    "message": "",
    "number": 1,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/227173224/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/227173224"
    }
  },
  "position": -1,
  "container": {
    "id": "227173220",
    "type": "page",
    "status": "current",
    "title": "Hardening Magic Collaboration Studio",
    "position": 3,
    "extensions": {
      "position": 3
    },
    "_links": {
      "webui": "/spaces/MCS2024xR3/pages/227173220/Hardening+Magic+Collaboration+Studio",
      "edit": "/pages/resumedraft.action?draftId=227173220",
      "tinyui": "/x/ZGOKDQ",
      "self": "https://docs.nomagic.com/rest/api/content/227173220"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS2024xR3",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/227173220/child",
      "restrictions": "/rest/api/content/227173220/restriction/byOperation",
      "history": "/rest/api/content/227173220/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/227173220/descendant",
      "space": "/rest/api/space/MCS2024xR3",
      "relevantViewRestrictions": "/rest/api/content/227173220/restriction/relevantViewRestrictions"
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
    "download": "/download/attachments/227173220/upgrade_jdk_webapp.sh?version=1&modificationDate=1746452088945&api=v2",
    "webui": "/spaces/MCS2024xR3/pages/227173220/Hardening+Magic+Collaboration+Studio?preview=%2F227173220%2F227173224%2Fupgrade_jdk_webapp.sh",
    "self": "https://docs.nomagic.com/rest/api/content/227173224"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/227173224/child",
    "restrictions": "/rest/api/content/227173224/restriction/byOperation",
    "history": "/rest/api/content/227173224/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/227173224/descendant",
    "space": "/rest/api/space/MCS2024xR3",
    "relevantViewRestrictions": "/rest/api/content/227173224/restriction/relevantViewRestrictions"
  }
}
````
