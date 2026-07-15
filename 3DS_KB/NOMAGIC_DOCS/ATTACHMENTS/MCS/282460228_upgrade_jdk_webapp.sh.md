# NOMAGIC ATTACHMENT: upgrade_jdk_webapp.sh

- attachment_id: `282460228`
- space_key: `MCS`
- parent_page_id: `282460195`
- parent_page_title: Downloadable scripts
- media_type: `text/x-sh`
- reported_bytes: 2801
- download_url: https://docs.nomagic.com/download/attachments/282460195/upgrade_jdk_webapp.sh?version=1&modificationDate=1767616255168&api=v2
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
  "id": "282460228",
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
    "when": "2026-01-05T13:30:55.168+01:00",
    "message": "",
    "number": 1,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/282460228/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/282460228"
    }
  },
  "position": -1,
  "container": {
    "id": "282460195",
    "type": "page",
    "status": "current",
    "title": "Downloadable scripts",
    "position": 3,
    "extensions": {
      "position": 3
    },
    "_links": {
      "webui": "/spaces/MCS/pages/282460195/Downloadable+scripts",
      "edit": "/pages/resumedraft.action?draftId=282460195&draftShareId=3df9d0aa-3635-459f-94f6-6a0af2a0c768",
      "tinyui": "/x/IwDWE",
      "self": "https://docs.nomagic.com/rest/api/content/282460195"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/282460195/child",
      "restrictions": "/rest/api/content/282460195/restriction/byOperation",
      "history": "/rest/api/content/282460195/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/282460195/descendant",
      "space": "/rest/api/space/MCS",
      "relevantViewRestrictions": "/rest/api/content/282460195/restriction/relevantViewRestrictions"
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
    "download": "/download/attachments/282460195/upgrade_jdk_webapp.sh?version=1&modificationDate=1767616255168&api=v2",
    "webui": "/spaces/MCS/pages/282460195/Downloadable+scripts?preview=%2F282460195%2F282460228%2Fupgrade_jdk_webapp.sh",
    "self": "https://docs.nomagic.com/rest/api/content/282460228"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/282460228/child",
    "restrictions": "/rest/api/content/282460228/restriction/byOperation",
    "history": "/rest/api/content/282460228/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/282460228/descendant",
    "space": "/rest/api/space/MCS",
    "relevantViewRestrictions": "/rest/api/content/282460228/restriction/relevantViewRestrictions"
  }
}
````
