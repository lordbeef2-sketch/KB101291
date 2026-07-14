# NOMAGIC ATTACHMENT: upgrade_jdk_webapp.sh

- attachment_id: `137991455`
- space_key: `MCS2024x`
- parent_page_id: `137991451`
- parent_page_title: Hardening Magic Collaboration Studio
- media_type: `text/x-sh`
- reported_bytes: 2118
- download_url: https://docs.nomagic.com/download/attachments/137991451/upgrade_jdk_webapp.sh?version=1&modificationDate=1695977444459&api=v2
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
  "id": "137991455",
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
    "when": "2023-09-29T10:50:44.459+02:00",
    "message": "",
    "number": 1,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/137991455/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/137991455"
    }
  },
  "position": -1,
  "container": {
    "id": "137991451",
    "type": "page",
    "status": "current",
    "title": "Hardening Magic Collaboration Studio",
    "position": 2,
    "extensions": {
      "position": 2
    },
    "_links": {
      "webui": "/spaces/MCS2024x/pages/137991451/Hardening+Magic+Collaboration+Studio",
      "edit": "/pages/resumedraft.action?draftId=137991451",
      "tinyui": "/x/G5U5C",
      "self": "https://docs.nomagic.com/rest/api/content/137991451"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS2024x",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/137991451/child",
      "restrictions": "/rest/api/content/137991451/restriction/byOperation",
      "history": "/rest/api/content/137991451/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/137991451/descendant",
      "space": "/rest/api/space/MCS2024x",
      "relevantViewRestrictions": "/rest/api/content/137991451/restriction/relevantViewRestrictions"
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
    "download": "/download/attachments/137991451/upgrade_jdk_webapp.sh?version=1&modificationDate=1695977444459&api=v2",
    "webui": "/spaces/MCS2024x/pages/137991451/Hardening+Magic+Collaboration+Studio?preview=%2F137991451%2F137991455%2Fupgrade_jdk_webapp.sh",
    "self": "https://docs.nomagic.com/rest/api/content/137991455"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/137991455/child",
    "restrictions": "/rest/api/content/137991455/restriction/byOperation",
    "history": "/rest/api/content/137991455/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/137991455/descendant",
    "space": "/rest/api/space/MCS2024x",
    "relevantViewRestrictions": "/rest/api/content/137991455/restriction/relevantViewRestrictions"
  }
}
````
