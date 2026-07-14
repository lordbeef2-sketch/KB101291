# NOMAGIC ATTACHMENT: upgrade_tomcat_webapp.sh

- attachment_id: `227173230`
- space_key: `MCS2024xR3`
- parent_page_id: `227173229`
- parent_page_title: Hardening Web Application Platform
- media_type: `application/x-sh`
- reported_bytes: 3759
- download_url: https://docs.nomagic.com/download/attachments/227173229/upgrade_tomcat_webapp.sh?version=3&modificationDate=1763645452330&api=v2
- payload_kind: `text-exact`
- downloaded_sha256: `3d1b81d73a96f89c2ccef720e523adc3adef0ea15e1f4de6a91d13f2295531a0`

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
DEFAULT_VERSION=10.1.40

WAP_SVC_PATH=/etc/systemd/system/webapp.service
###########################################
#
#  DO NOT MODIFY ANYTHING BEYOND THIS POINT
#
###########################################
# Check if script is run as root or sudo.
if [ "$EUID" -ne 0 ];then
	echo
	echo "Please run as root or sudo."
	exit 1
fi
unset TOMCAT_PKG
echo ""
echo "----------------------------------------------------------------------------"
echo "This script utilizes rsync, so we will install it via yum."
echo "Please ensure rsync is on the system if thes are no posibility to use yum package manager"
echo ""
echo "----------------------------------------------------------------------------"
# Check if local Tomcat upgrade package exists. 
TOMCAT_PKG=$(find apache-tomcat* 2>/dev/null | tail -n1)
if [[ -n "$TOMCAT_PKG" ]]; then
	if file $TOMCAT_PKG | grep -q "gzip compressed"; then
		TOMCAT_VERSION=$(basename $TOMCAT_PKG .tar.gz | cut -d '-' -f 3)
		TOMCAT_DIR=$(basename $TOMCAT_PKG .tar.gz)
		EXTRACT_EXE="tar -xf"
	elif file $TOMCAT_PKG | grep -q "Zip archive"; then
		TOMCAT_VERSION=$(basename $TOMCAT_PKG .zip | cut -d '-' -f 3)
		TOMCAT_DIR=$(basename $TOMCAT_PKG .zip)
		EXTRACT_EXE="unzip -q"
	else
		echo "Unknown File Type: $TOMCAT_PKG"
		unset TOMCAT_PKG
	fi
	echo ""
	echo "Local upgrade package found for Tomcat $TOMCAT_VERSION: $TOMCAT_PKG"
	read -p "Proceed with upgrade using this local package (y to continue)? " qinstall
	if ! [[ $qinstall =~ [yY](es)* ]]; then unset TOMCAT_PKG; fi
fi
# Assume Tomcat will be downloaded either local package is not found, or user does not want to use local package.
if ! [[ -n "$TOMCAT_PKG" ]]; then
	read -e -p "Please enter the tomcat upgrade version [default is: $DEFAULT_VERSION] : " TOMCAT_VERSION
	TOMCAT_VERSION="${TOMCAT_VERSION:-$DEFAULT_VERSION}"
	MAJOR_VERSION=$(echo $TOMCAT_VERSION | cut -d . -f 1)
	TOMCAT_PKG=apache-tomcat-$TOMCAT_VERSION.tar.gz
	TOMCAT_DOWNLOAD=https://archive.apache.org/dist/tomcat/tomcat-$MAJOR_VERSION/v$TOMCAT_VERSION/bin/$TOMCAT_PKG
	wget $TOMCAT_DOWNLOAD
	TOMCAT_DIR=$(basename $TOMCAT_PKG .tar.gz)
	EXTRACT_EXE="tar -xf"
	[ ! -e "${TOMCAT_PKG}" ] && echo "Download failed! Check the version or internet connection and try again." && exit|| echo "$TOMCAT_PKG download successful."
fi
echo "----------------------------------------------------------------------------"
echo ""

echo "Tomcat will be upgraded to: "$TOMCAT_VERSION "version."

if [ -f $WAP_SVC_PATH ]; then
	WEBAPP_ROOT=$(cat /etc/systemd/system/webapp.service | grep CATALINA_HOME | cut -f 3 -d '=')
	WEBAPP_OWNER=$(stat -c "%U:%G" $WEBAPP_ROOT)
else
	echo "Could not find webapp service file. Exiting."
	exit 1
fi

#####################################
#  Install rsync
yum install rsync -y -q
####################################

#####################################
# Begin deployment
$EXTRACT_EXE $TOMCAT_PKG
rsync -av $TOMCAT_DIR/bin/*.jar $WEBAPP_ROOT/bin/
rsync -av $TOMCAT_DIR/lib/*.jar $WEBAPP_ROOT/lib/
rsync -v $TOMCAT_DIR/* $WEBAPP_ROOT/
####################################
# Ensure proper ownership of files
chown -R $WEBAPP_OWNER $WEBAPP_ROOT/bin $WEBAPP_ROOT/lib
find $WEBAPP_ROOT -maxdepth 1 -type f -exec chown $WEBAPP_OWNER {} +
####################################
# Remove foder with extracted files
rm -fr $TOMCAT_DIR
echo ""
echo "Upgrade completed successfully."


````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "227173230",
  "type": "attachment",
  "status": "current",
  "title": "upgrade_tomcat_webapp.sh",
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
    "when": "2025-11-20T14:30:52.330+01:00",
    "message": "",
    "number": 3,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/227173230/version/3"
    },
    "_expandable": {
      "content": "/rest/api/content/227173230"
    }
  },
  "position": -1,
  "container": {
    "id": "227173229",
    "type": "page",
    "status": "current",
    "title": "Hardening Web Application Platform",
    "position": 2,
    "extensions": {
      "position": 2
    },
    "_links": {
      "webui": "/spaces/MCS2024xR3/pages/227173229/Hardening+Web+Application+Platform",
      "edit": "/pages/resumedraft.action?draftId=227173229",
      "tinyui": "/x/bWOKDQ",
      "self": "https://docs.nomagic.com/rest/api/content/227173229"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS2024xR3",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/227173229/child",
      "restrictions": "/rest/api/content/227173229/restriction/byOperation",
      "history": "/rest/api/content/227173229/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/227173229/descendant",
      "space": "/rest/api/space/MCS2024xR3",
      "relevantViewRestrictions": "/rest/api/content/227173229/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/x-sh"
  },
  "extensions": {
    "mediaType": "application/x-sh",
    "fileSize": 3759,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/227173229/upgrade_tomcat_webapp.sh?version=3&modificationDate=1763645452330&api=v2",
    "webui": "/spaces/MCS2024xR3/pages/227173229/Hardening+Web+Application+Platform?preview=%2F227173229%2F227173230%2Fupgrade_tomcat_webapp.sh",
    "self": "https://docs.nomagic.com/rest/api/content/227173230"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/227173230/child",
    "restrictions": "/rest/api/content/227173230/restriction/byOperation",
    "history": "/rest/api/content/227173230/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/227173230/descendant",
    "space": "/rest/api/space/MCS2024xR3",
    "relevantViewRestrictions": "/rest/api/content/227173230/restriction/relevantViewRestrictions"
  }
}
````
