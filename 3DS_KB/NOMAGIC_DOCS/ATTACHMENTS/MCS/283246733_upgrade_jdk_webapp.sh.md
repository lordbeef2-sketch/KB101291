# NOMAGIC ATTACHMENT: upgrade_jdk_webapp.sh

- attachment_id: `283246733`
- space_key: `MCS`
- parent_page_id: `283246728`
- parent_page_title: (2026x) Downloadable scripts
- media_type: `text/x-sh`
- reported_bytes: 2801
- download_url: https://docs.nomagic.com/download/attachments/283246728/upgrade_jdk_webapp.sh?version=2&modificationDate=1773673356065&api=v2
- payload_kind: `text-exact`
- downloaded_sha256: `70a0687438619fbda739ab466bce7a81a0cc094cf4c71512336d12d71b5e0a38`

## EXACT ATTACHMENT SOURCE

````text
#!/bin/bash
##################################################################
#  Upgrade JDK in CATIA NoMagic Webapp Platform to a newer OpenJDK
#  CATIA No Magic DevOps Team
##################################################################

###  JRE_DOWNLOAD contains the download URL to the target OpenJDK tar archive
###  The example below upgrades the JDK to selected OpenJDK

# Edit default version if you can't input it during upgrade
DEFAULT_VERSION=21.0.8+9

WAP_SVC_PATH=/etc/systemd/system/webapp.service
###########################################
#
#  DO NOT MODIFY ANYTHING BELOW THIS POINT
#
###########################################
# Check if script is run as root or sudo.
if [ "$EUID" -ne 0 ];then
	echo
	echo "Please run as root or sudo."
	exit 1
fi
unset JRE_TAR
JRE_TAR=$(find *jre_x64_linux_hotspot* 2>/dev/null | tail -n1)
if [[ -n "$JRE_TAR" ]]; then
	JRE_VERSION=$(basename $JRE_TAR .tar.gz | cut -d '_' -f 5)
	echo ""
	echo "Local upgrade package found for Java $JRE_VERSION: $JRE_TAR"
	read -p "Proceed with upgrade using this local package (y to continue)? " qinstall
	if ! [[ $qinstall =~ [yY](es)* ]]; then unset JRE_TAR; fi
fi

# Download Java upgrade package
if ! [[ -n "$JRE_TAR" ]]; then
	echo ""
	echo "----------------------------------------------------------------------------------------------------"
	read -e -p "Please enter the full Java version for upgrade [default is: $DEFAULT_VERSION] : " JRE_VERSION
	echo "----------------------------------------------------------------------------------------------------"
	echo ""
	JRE_VERSION="${JRE_VERSION:-$DEFAULT_VERSION}"
	MAJOR_VERSION=$(echo $JRE_VERSION | cut -d . -f 1)
	DOWNLOAD_VERSION=${JRE_VERSION/+/_}
	JRE_DOWNLOAD=https://github.com/adoptium/temurin$MAJOR_VERSION-binaries/releases/download/jdk-$JRE_VERSION/OpenJDK${MAJOR_VERSION}U-jre_x64_linux_hotspot_$DOWNLOAD_VERSION.tar.gz
	#  Install wget
	yum install wget -y -q
	##   Download OpenJDK
	wget $JRE_DOWNLOAD
	JRE_TAR=$(basename $JRE_DOWNLOAD)
	[ ! -e "${JRE_TAR}" ] && echo "Download failed! Check the version or internet connection and try again." && exit|| echo "$JRE_TAR download successful."
fi

echo "OpenJDK will be upgraded to: "$JRE_VERSION "version."

if [ -f $WAP_SVC_PATH ]; then
	JRE_HOME=$(cat /etc/systemd/system/webapp.service | grep CATALINA_HOME | cut -f 3 -d '=')/jre
	JRE_OWNER=$(stat -c "%U:%G" $JRE_HOME)
else
	echo "Could not find webapp service file. Exiting."
	exit 1
fi

##  Remove current JRE_HOME
rm -fr $JRE_HOME

# Create temp directory
mkdir _tmp
cd _tmp
##  Extract OpenJDK
mkdir -p $JRE_HOME
tar -xf ../$JRE_TAR -C $JRE_HOME --strip-components=1
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
  "id": "283246733",
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
    "when": "2026-03-16T16:02:36.065+01:00",
    "message": "",
    "number": 2,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/283246733/version/2"
    },
    "_expandable": {
      "content": "/rest/api/content/283246733"
    }
  },
  "position": -1,
  "container": {
    "id": "283246728",
    "type": "page",
    "status": "current",
    "title": "(2026x) Downloadable scripts",
    "position": 3,
    "extensions": {
      "position": 3
    },
    "_links": {
      "webui": "/spaces/MCS/pages/283246728/2026x+Downloadable+scripts",
      "edit": "/pages/resumedraft.action?draftId=283246728&draftShareId=a92844c2-9f09-4d2f-90dc-55dea13961e3",
      "tinyui": "/x/iADiE",
      "self": "https://docs.nomagic.com/rest/api/content/283246728"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/283246728/child",
      "restrictions": "/rest/api/content/283246728/restriction/byOperation",
      "history": "/rest/api/content/283246728/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/283246728/descendant",
      "space": "/rest/api/space/MCS",
      "relevantViewRestrictions": "/rest/api/content/283246728/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "text/x-sh"
  },
  "extensions": {
    "mediaType": "text/x-sh",
    "fileSize": 2801,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/283246728/upgrade_jdk_webapp.sh?version=2&modificationDate=1773673356065&api=v2",
    "webui": "/spaces/MCS/pages/283246728/2026x+Downloadable+scripts?preview=%2F283246728%2F283246733%2Fupgrade_jdk_webapp.sh",
    "self": "https://docs.nomagic.com/rest/api/content/283246733"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/283246733/child",
    "restrictions": "/rest/api/content/283246733/restriction/byOperation",
    "history": "/rest/api/content/283246733/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/283246733/descendant",
    "space": "/rest/api/space/MCS",
    "relevantViewRestrictions": "/rest/api/content/283246733/restriction/relevantViewRestrictions"
  }
}
````
