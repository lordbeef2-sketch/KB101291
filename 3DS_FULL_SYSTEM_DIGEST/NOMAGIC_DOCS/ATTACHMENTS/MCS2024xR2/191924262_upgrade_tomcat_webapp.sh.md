# NOMAGIC ATTACHMENT: upgrade_tomcat_webapp.sh

- attachment_id: `191924262`
- space_key: `MCS2024xR2`
- parent_page_id: `191924260`
- parent_page_title: Installing Web Application Platform on Linux with GUI
- media_type: `application/x-sh`
- reported_bytes: 1484
- download_url: https://docs.nomagic.com/download/attachments/191924260/upgrade_tomcat_webapp.sh?version=1&modificationDate=1728049792258&api=v2
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
  "id": "191924262",
  "type": "attachment",
  "status": "current",
  "title": "upgrade_tomcat_webapp.sh",
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
    "when": "2024-10-04T15:49:52.258+02:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/191924262/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/191924262"
    }
  },
  "position": -1,
  "container": {
    "id": "191924260",
    "type": "page",
    "status": "current",
    "title": "Installing Web Application Platform on Linux with GUI",
    "position": 2,
    "extensions": {
      "position": 2
    },
    "_links": {
      "webui": "/spaces/MCS2024xR2/pages/191924260/Installing+Web+Application+Platform+on+Linux+with+GUI",
      "edit": "/pages/resumedraft.action?draftId=191924260",
      "tinyui": "/x/JIhwCw",
      "self": "https://docs.nomagic.com/rest/api/content/191924260"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS2024xR2",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/191924260/child",
      "restrictions": "/rest/api/content/191924260/restriction/byOperation",
      "history": "/rest/api/content/191924260/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/191924260/descendant",
      "space": "/rest/api/space/MCS2024xR2",
      "relevantViewRestrictions": "/rest/api/content/191924260/restriction/relevantViewRestrictions"
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
    "download": "/download/attachments/191924260/upgrade_tomcat_webapp.sh?version=1&modificationDate=1728049792258&api=v2",
    "webui": "/spaces/MCS2024xR2/pages/191924260/Installing+Web+Application+Platform+on+Linux+with+GUI?preview=%2F191924260%2F191924262%2Fupgrade_tomcat_webapp.sh",
    "self": "https://docs.nomagic.com/rest/api/content/191924262"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/191924262/child",
    "restrictions": "/rest/api/content/191924262/restriction/byOperation",
    "history": "/rest/api/content/191924262/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/191924262/descendant",
    "space": "/rest/api/space/MCS2024xR2",
    "relevantViewRestrictions": "/rest/api/content/191924262/restriction/relevantViewRestrictions"
  }
}
````
