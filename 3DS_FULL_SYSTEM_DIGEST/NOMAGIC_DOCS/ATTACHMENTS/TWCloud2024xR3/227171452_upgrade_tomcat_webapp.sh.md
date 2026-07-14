# NOMAGIC ATTACHMENT: upgrade_tomcat_webapp.sh

- attachment_id: `227171452`
- space_key: `TWCloud2024xR3`
- parent_page_id: `227171450`
- parent_page_title: Installing Web Application Platform on Linux
- media_type: `application/x-sh`
- reported_bytes: 1484
- download_url: https://docs.nomagic.com/download/attachments/227171450/upgrade_tomcat_webapp.sh?version=1&modificationDate=1746450327699&api=v2
- payload_kind: `text-exact`
- downloaded_sha256: `9016ed62c52e0e74cdb99f4bdfb3757acfa877ccc664ea8c13ebb07b7cfa6a0f`

## EXACT ATTACHMENT SOURCE

````text
#!/bin/bash
##########################################################
#  Upgrade Tomcat Version used by WebApp Platform
#  Benjamin Krajmalnik (benjamin.krajmalnik@3ds.com)
# ################################
# This script utilizes rsync, so we will install it via yum
# Please set the tomcat version you would like to use

TOMCAT_VERSION=10.1.11

#####################################
# 
#  DO NOT MODIFY ANYTHING BEYOND THIS POINT
#
#####################################

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
mkdir _tmp
cd _tmp/
wget $TOMCAT_DOWNLOAD
tar -xf $TOMCAT_TAR
cd $TOMCAT_DIR
rsync -av bin/*.jar $WEBAPP_ROOT/bin/
rsync -av lib/*.jar $WEBAPP_ROOT/lib/
####################################
# Ensure proper ownership of files
chown -R $WEBAPP_OWNER $WEBAPP_ROOT
####################################
# Remove downloaded files
cd ../..
rm -fr _tmp
````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "227171452",
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
    "when": "2025-05-05T15:05:27.699+02:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/227171452/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/227171452"
    }
  },
  "position": -1,
  "container": {
    "id": "227171450",
    "type": "page",
    "status": "current",
    "title": "Installing Web Application Platform on Linux",
    "position": 1,
    "extensions": {
      "position": 1
    },
    "_links": {
      "webui": "/spaces/TWCloud2024xR3/pages/227171450/Installing+Web+Application+Platform+on+Linux",
      "edit": "/pages/resumedraft.action?draftId=227171450",
      "tinyui": "/x/elyKDQ",
      "self": "https://docs.nomagic.com/rest/api/content/227171450"
    },
    "_expandable": {
      "container": "/rest/api/space/TWCloud2024xR3",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/227171450/child",
      "restrictions": "/rest/api/content/227171450/restriction/byOperation",
      "history": "/rest/api/content/227171450/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/227171450/descendant",
      "space": "/rest/api/space/TWCloud2024xR3",
      "relevantViewRestrictions": "/rest/api/content/227171450/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/x-sh"
  },
  "extensions": {
    "mediaType": "application/x-sh",
    "fileSize": 1484,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/227171450/upgrade_tomcat_webapp.sh?version=1&modificationDate=1746450327699&api=v2",
    "webui": "/spaces/TWCloud2024xR3/pages/227171450/Installing+Web+Application+Platform+on+Linux?preview=%2F227171450%2F227171452%2Fupgrade_tomcat_webapp.sh",
    "self": "https://docs.nomagic.com/rest/api/content/227171452"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/227171452/child",
    "restrictions": "/rest/api/content/227171452/restriction/byOperation",
    "history": "/rest/api/content/227171452/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/227171452/descendant",
    "space": "/rest/api/space/TWCloud2024xR3",
    "relevantViewRestrictions": "/rest/api/content/227171452/restriction/relevantViewRestrictions"
  }
}
````
