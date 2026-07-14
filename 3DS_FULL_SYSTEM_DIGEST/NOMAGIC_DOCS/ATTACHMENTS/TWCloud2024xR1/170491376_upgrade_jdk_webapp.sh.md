# NOMAGIC ATTACHMENT: upgrade_jdk_webapp.sh

- attachment_id: `170491376`
- space_key: `TWCloud2024xR1`
- parent_page_id: `170491374`
- parent_page_title: Hardening Web Application Platform
- media_type: `text/x-sh`
- reported_bytes: 2780
- download_url: https://docs.nomagic.com/download/attachments/170491374/upgrade_jdk_webapp.sh?version=1&modificationDate=1715246041818&api=v2
- payload_kind: `text-exact`
- downloaded_sha256: `164068682f4df45b9c99fe44d665a871879303a54deb59534eb48b8d24d88c4d`

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
DEFAULT_VERSION=17.0.8.1+1

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
	JRE_DOWNLOAD=https://github.com/adoptium/temurin$MAJOR_VERSION-binaries/releases/download/jdk-$JRE_VERSION/OpenJDK17U-jre_x64_linux_hotspot_$DOWNLOAD_VERSION.tar.gz
	#  Install wget
	yum install wget -y -q
	##   Download OpenJDK
	wget $JRE_DOWNLOAD
	JRE_TAR=$(basename $JRE_DOWNLOAD)
	[ ! -e "${JRE_TAR}" ] && echo "Download failed! Check the version or internet connection and try again." && exit|| echo "$JRE_TAR download successful."
fi

echo "OpenJDK will be upgraded to: "$JRE_VERSION "version."

if [ -f $WAP_SVC_PATH ]; then
	JRE_HOME=$(cat /etc/systemd/system/webapp.service | grep JRE_HOME | cut -f 3 -d '=')
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
  "id": "170491376",
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
    "when": "2024-05-09T11:14:01.818+02:00",
    "message": "",
    "number": 1,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/170491376/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/170491376"
    }
  },
  "position": -1,
  "container": {
    "id": "170491374",
    "type": "page",
    "status": "current",
    "title": "Hardening Web Application Platform",
    "position": 3,
    "extensions": {
      "position": 3
    },
    "_links": {
      "webui": "/spaces/TWCloud2024xR1/pages/170491374/Hardening+Web+Application+Platform",
      "edit": "/pages/resumedraft.action?draftId=170491374",
      "tinyui": "/x/7n0pCg",
      "self": "https://docs.nomagic.com/rest/api/content/170491374"
    },
    "_expandable": {
      "container": "/rest/api/space/TWCloud2024xR1",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/170491374/child",
      "restrictions": "/rest/api/content/170491374/restriction/byOperation",
      "history": "/rest/api/content/170491374/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/170491374/descendant",
      "space": "/rest/api/space/TWCloud2024xR1",
      "relevantViewRestrictions": "/rest/api/content/170491374/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "text/x-sh"
  },
  "extensions": {
    "mediaType": "text/x-sh",
    "fileSize": 2780,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/170491374/upgrade_jdk_webapp.sh?version=1&modificationDate=1715246041818&api=v2",
    "webui": "/spaces/TWCloud2024xR1/pages/170491374/Hardening+Web+Application+Platform?preview=%2F170491374%2F170491376%2Fupgrade_jdk_webapp.sh",
    "self": "https://docs.nomagic.com/rest/api/content/170491376"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/170491376/child",
    "restrictions": "/rest/api/content/170491376/restriction/byOperation",
    "history": "/rest/api/content/170491376/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/170491376/descendant",
    "space": "/rest/api/space/TWCloud2024xR1",
    "relevantViewRestrictions": "/rest/api/content/170491376/restriction/relevantViewRestrictions"
  }
}
````
