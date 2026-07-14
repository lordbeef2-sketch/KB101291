# NOMAGIC ATTACHMENT: hardening_scripts_2024xRefresh3.zip

- attachment_id: `264929399`
- space_key: `MCS2024xR3`
- parent_page_id: `227173225`
- parent_page_title: Hardening Cassandra
- media_type: `application/zip`
- reported_bytes: 3682
- download_url: https://docs.nomagic.com/download/attachments/227173225/hardening_scripts_2024xRefresh3.zip?version=1&modificationDate=1761048805217&api=v2
- payload_kind: `archive-expanded`
- downloaded_sha256: `d3fc86bc22beb240e641939886107e98fe149777ab8fc69b352a4ba110f4802f`

## ARCHIVE CONTENTS

### ENTRY: harden_cassandra_ports.sh

- bytes: 1472
- crc32: `86529da2`
- decoded_as: `utf-8`

````text
#!/bin/bash
echo "Hardening Cassandra Ports"
echo "Creating Cassandra firewall service profile"
cat <<EOF |  tee /etc/firewalld/services/cassandra.xml  &> /dev/null
<?xml version="1.0" encoding="utf-8"?>
<service version="1.0">
    <short>cassandra</short>
    <description>cassandra</description>
	<port port="7000" protocol="tcp"/>
	<port port="7001" protocol="tcp"/>
	<port port="9042" protocol="tcp"/>
	<port port="9142" protocol="tcp"/>
</service>
EOF
echo "Removing existing firewall rules on the cassandra ports or service profile"
sleep 5
zone=$(firewall-cmd --get-default) &> /dev/null
firewall-cmd --zone=$zone --remove-port=7000/tcp --permanent  &> /dev/null
firewall-cmd --zone=$zone --remove-port=7001/tcp --permanent  &> /dev/null
firewall-cmd --zone=$zone --remove-port=7199/tcp --permanent  &> /dev/null
firewall-cmd --zone=$zone --remove-port=9042/tcp --permanent  &> /dev/null
firewall-cmd --zone=$zone --remove-port=9142/tcp --permanent  &> /dev/null
firewall-cmd --zone=$zone --remove-service=cassandra --permanent  &> /dev/null
echo "Creating rich rules for Cassandra nodes discovered via nodetool gossipinfo"
set -f
local_list=($(nodetool gossipinfo | grep '/' | cut -f 2 -d /))
set +f
for i in "${local_list[@]}" ; do
        cmd=" firewall-cmd --zone=$zone --add-rich-rule='rule family=\"ipv4\" source address=\"$i\" service name=\"cassandra\" accept' --permanent  &> /dev/null"
    echo $cmd
    eval $cmd
done
firewall-cmd --reload  &> /dev/null

````

### ENTRY: upgrade_jdk_webapp.sh

- bytes: 2780
- crc32: `53385e7b`
- decoded_as: `utf-8`

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

### ENTRY: upgrade_tomcat_webapp.sh

- bytes: 3766
- crc32: `4ba61e6f`
- decoded_as: `utf-8`

````text
#!/bin/bash
##########################################################
#  Upgrade Tomcat Version used by WebApp Platform
#  CATIA No Magic DevOps Team
# ################################

# This script utilizes rsync, so we will install it via yum
# If you are offline you need to put required installer file in the same location with this script

# Edit default version if you can't input it during upgrade
DEFAULT_VERSION=10.1.18

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
	WEBAPP_ROOT=$(cat /etc/systemd/system/webapp.service | grep CATALINA_HOME_WEBAPP | cut -f 3 -d '=')
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
  "id": "264929399",
  "type": "attachment",
  "status": "current",
  "title": "hardening_scripts_2024xRefresh3.zip",
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
    "when": "2025-10-21T14:13:25.217+02:00",
    "message": "",
    "number": 1,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/264929399/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/264929399"
    }
  },
  "position": -1,
  "container": {
    "id": "227173225",
    "type": "page",
    "status": "current",
    "title": "Hardening Cassandra",
    "position": 0,
    "extensions": {
      "position": 0
    },
    "_links": {
      "webui": "/spaces/MCS2024xR3/pages/227173225/Hardening+Cassandra",
      "edit": "/pages/resumedraft.action?draftId=227173225",
      "tinyui": "/x/aWOKDQ",
      "self": "https://docs.nomagic.com/rest/api/content/227173225"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS2024xR3",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/227173225/child",
      "restrictions": "/rest/api/content/227173225/restriction/byOperation",
      "history": "/rest/api/content/227173225/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/227173225/descendant",
      "space": "/rest/api/space/MCS2024xR3",
      "relevantViewRestrictions": "/rest/api/content/227173225/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/zip"
  },
  "extensions": {
    "mediaType": "application/zip",
    "fileSize": 3682,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/227173225/hardening_scripts_2024xRefresh3.zip?version=1&modificationDate=1761048805217&api=v2",
    "webui": "/spaces/MCS2024xR3/pages/227173225/Hardening+Cassandra?preview=%2F227173225%2F264929399%2Fhardening_scripts_2024xRefresh3.zip",
    "self": "https://docs.nomagic.com/rest/api/content/264929399"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/264929399/child",
    "restrictions": "/rest/api/content/264929399/restriction/byOperation",
    "history": "/rest/api/content/264929399/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/264929399/descendant",
    "space": "/rest/api/space/MCS2024xR3",
    "relevantViewRestrictions": "/rest/api/content/264929399/restriction/relevantViewRestrictions"
  }
}
````
