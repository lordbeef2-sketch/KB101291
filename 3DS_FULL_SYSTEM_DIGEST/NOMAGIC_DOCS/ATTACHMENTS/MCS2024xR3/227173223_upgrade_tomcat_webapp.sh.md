# NOMAGIC ATTACHMENT: upgrade_tomcat_webapp.sh

- attachment_id: `227173223`
- space_key: `MCS2024xR3`
- parent_page_id: `227173220`
- parent_page_title: Hardening Magic Collaboration Studio
- media_type: `text/x-sh`
- reported_bytes: 2430
- download_url: https://docs.nomagic.com/download/attachments/227173220/upgrade_tomcat_webapp.sh?version=1&modificationDate=1746452088941&api=v2
- payload_kind: `text-exact`
- downloaded_sha256: `4467b0f1e456b5f6b2f78927b17723c1ff2fd0467372fe4d39b9162dbb52d6b7`

## EXACT ATTACHMENT SOURCE

````text
#!/bin/bash
##########################################################
#  Upgrade Tomcat Version used by WebApp Platform
#  CATIA No Magic DevOps Team
# ################################

# This script utilizes rsync, so we will install it via yum
# If you are offline you need to put required installer file in the same location with this script

# Edit default version if you can't input it during upgrade
DEFAULT_VERSION=9.0.63

###########################################
#
#  DO NOT MODIFY ANYTHING BEYOND THIS POINT
#
###########################################

echo ""
echo "----------------------------------------------------------------------------"
echo "This script utilizes rsync, so we will install it via yum."
echo "Please ensure rsync is on the system if thes are no posibility to use yum package manager"
echo ""
echo "----------------------------------------------------------------------------"
read -e -p "Please enter the tomcat version you would like to use. [default is: $DEFAULT_VERSION] : " TOMCAT_VERSION
echo "----------------------------------------------------------------------------"
echo ""
TOMCAT_VERSION="${TOMCAT_VERSION:-$DEFAULT_VERSION}"

echo "Tomcat will be upgraded to: "$TOMCAT_VERSION "version."

WEBAPP_ROOT=$(cat /etc/systemd/system/webapp.service | grep CATALINA_HOME_WEBAPP | cut -f 3 -d '=')
WEBAPP_OWNER=$(stat -c "%U:%G" $WEBAPP_ROOT)

#####################################
#  Install rsync
yum install rsync -y -q
####################################
# Setting up script variables
MAJOR_VERSION=$(echo $TOMCAT_VERSION | cut -d . -f 1)
TOMCAT_DOWNLOAD=https://archive.apache.org/dist/tomcat/tomcat-$MAJOR_VERSION/v$TOMCAT_VERSION/bin/apache-tomcat-$TOMCAT_VERSION.tar.gz
TOMCAT_TAR=$(basename $TOMCAT_DOWNLOAD)
TOMCAT_DIR=$(basename $TOMCAT_TAR .tar.gz)

#####################################
# Begin deployment
wget $TOMCAT_DOWNLOAD
[ ! -e "${TOMCAT_TAR}" ] && echo "File does not exist ! Check the file name or internet connection and try again." && exit|| echo "File $TOMCAT_TAR exists"
tar -xf $TOMCAT_TAR
rsync -av $TOMCAT_DIR/bin/*.jar $WEBAPP_ROOT/bin/
rsync -av $TOMCAT_DIR/lib/*.jar $WEBAPP_ROOT/lib/
####################################
# Ensure proper ownership of files
chown -R $WEBAPP_OWNER $WEBAPP_ROOT/bin $WEBAPP_ROOT/lib
####################################
# Remove foder with extracted files
rm -fr $TOMCAT_DIR
echo ""
echo "Upgrade completed successfully."


````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "227173223",
  "type": "attachment",
  "status": "current",
  "title": "upgrade_tomcat_webapp.sh",
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
    "when": "2025-05-05T15:34:48.941+02:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/227173223/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/227173223"
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
    "fileSize": 2430,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/227173220/upgrade_tomcat_webapp.sh?version=1&modificationDate=1746452088941&api=v2",
    "webui": "/spaces/MCS2024xR3/pages/227173220/Hardening+Magic+Collaboration+Studio?preview=%2F227173220%2F227173223%2Fupgrade_tomcat_webapp.sh",
    "self": "https://docs.nomagic.com/rest/api/content/227173223"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/227173223/child",
    "restrictions": "/rest/api/content/227173223/restriction/byOperation",
    "history": "/rest/api/content/227173223/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/227173223/descendant",
    "space": "/rest/api/space/MCS2024xR3",
    "relevantViewRestrictions": "/rest/api/content/227173223/restriction/relevantViewRestrictions"
  }
}
````
