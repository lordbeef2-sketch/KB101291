# NOMAGIC ATTACHMENT: getlogfiles.sh

- attachment_id: `111218192`
- space_key: `FAQ`
- parent_page_id: `70395805`
- parent_page_title: Where can I find log files of a modeling tool, Cameo Collaborator, and Teamwork Cloud
- media_type: `application/x-sh`
- reported_bytes: 2909
- download_url: https://docs.nomagic.com/download/attachments/70395805/getlogfiles.sh?version=1&modificationDate=1670397521775&api=v2
- payload_kind: `text-exact`
- downloaded_sha256: `13c10e7753fd0a82d97d740b813e0371d2b41b4e56ec8fbc9ac068c4981cd0bb`

## EXACT ATTACHMENT SOURCE

````text
#!/bin/bash

# This script creates a tar package of log files for Teamwork Cloud services.
# Execute the script in Linux Bash or Windows Cygwin

TWC_LOG_PKG=TWC-logs.tar
TWC_ENV_PATH=/etc/twcloud/twcloud-env
CASSANDRA_LOG_PATH=/var/log/cassandra/system.log
echo

# Create temporary directory to stage log files.
IATEMPDIR=$(pwd)/_tmp
mkdir $IATEMPDIR

# Obtain TWC environment settings for either Linux or Windows Cygwin
if [ -f $TWC_ENV_PATH ]; then
	source $TWC_ENV_PATH
	USER_HOME_PATH=$(eval echo ~$TWCLOUD_OWNR)
	cat $TWC_ENV_PATH >> $IATEMPDIR/sys-info.txt
	# Obtain server CPU and MEM info
	echo -e "\n### CPU INFO ###\n" >> $IATEMPDIR/sys-info.txt
	lscpu | grep CPU >> $IATEMPDIR/sys-info.txt
	echo -e "################\n" >> $IATEMPDIR/sys-info.txt
	echo -e "### MEM INFO ###" >> $IATEMPDIR/sys-info.txt
	free -h >> $IATEMPDIR/sys-info.txt
	echo -e "\n################" >> $IATEMPDIR/sys-info.txt
else
	echo "--- Windows Cygwin Mode ---"
	USER_HOME_PATH=/cygdrive/c/Users/$USER
	TWCLOUD_HOME="/cygdrive/c/Program Files/TeamworkCloud"
fi

# Verify TWC environment paths
echo "Teamwork Cloud Installation Path: $TWCLOUD_HOME"
echo "Teamwork Cloud User Home Path: $USER_HOME_PATH"

# Determine the latest TWC version installed and copy log files.
if [ -d $USER_HOME_PATH/.twcloud/2022x ]; then
	echo "Copying Teamwork Cloud 22x log file."
	echo "TWC 22x" >> $IATEMPDIR/sys-info.txt
	cp $USER_HOME_PATH/.twcloud/2022x/server.log $IATEMPDIR/twc-server.log
	cp "$TWCLOUD_HOME"/WebAppPlatform/logs/webappplatform/authentication.log $IATEMPDIR/
elif [ -d $USER_HOME_PATH/.twcloud/2021x ]; then
	echo "Copying Teamwork Cloud 21x log file."
	echo "TWC 21x" >> $IATEMPDIR/sys-info.txt
	cp $USER_HOME_PATH/.twcloud/2021x/server.log $IATEMPDIR/twc-server.log
	cp $USER_HOME_PATH/.authserver/2021x/authserver.log $IATEMPDIR/
elif [ -d $USER_HOME_PATH/.twcloud/19.0 ]; then
	echo "Copying Teamwork Cloud v19 log file."
	echo "TWC v19" >> $IATEMPDIR/sys-info.txt
	cp $USER_HOME_PATH/.twcloud/19.0/server.log $IATEMPDIR/twc-server.log
	cp $USER_HOME_PATH/.authserver/19.0/authserver.log $IATEMPDIR/
else
	echo "Teamwork Cloud log files not found."
	exit 1
fi
cp "$TWCLOUD_HOME"/WebAppPlatform/logs/webappplatform/web-app.log $IATEMPDIR/
cp "$TWCLOUD_HOME"/WebAppPlatform/logs/catalina.out $IATEMPDIR/
# Copy the Cassandra log file if it exists on the system.
if [ -f $CASSANDRA_LOG_PATH ]; then
	echo "Copying Cassandra log file."
	cp $CASSANDRA_LOG_PATH $IATEMPDIR/cassandra-system.log
fi
# Gather system information
if [ -f /etc/os-release ]; then cat /etc/os-release >> $IATEMPDIR/sys-info.txt; fi
if command -v systeminfo; then systeminfo >> $IATEMPDIR/sys-info.txt; fi

# Tar up log package
echo
echo "Creating tar package ..."
cd $IATEMPDIR && tar cvf $TWC_LOG_PKG * && mv $TWC_LOG_PKG ../ && cd ..

# Remove temporary directory
rm -fr $IATEMPDIR
echo
echo "Teamwork Cloud log package ready: $TWC_LOG_PKG"
echo

````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "111218192",
  "type": "attachment",
  "status": "current",
  "title": "getlogfiles.sh",
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
    "when": "2022-12-07T08:18:41.775+01:00",
    "message": "",
    "number": 1,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/111218192/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/111218192"
    }
  },
  "position": -1,
  "container": {
    "id": "70395805",
    "type": "page",
    "status": "current",
    "title": "Where can I find log files of a modeling tool, Cameo Collaborator, and Teamwork Cloud",
    "position": 0,
    "extensions": {
      "position": 0
    },
    "_links": {
      "webui": "/spaces/FAQ/pages/70395805/Where+can+I+find+log+files+of+a+modeling+tool+Cameo+Collaborator+and+Teamwork+Cloud",
      "edit": "/pages/resumedraft.action?draftId=70395805&draftShareId=a494b7c9-4896-4340-9187-5f9a7d250b0f",
      "tinyui": "/x/nScyB",
      "self": "https://docs.nomagic.com/rest/api/content/70395805"
    },
    "_expandable": {
      "container": "/rest/api/space/FAQ",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/70395805/child",
      "restrictions": "/rest/api/content/70395805/restriction/byOperation",
      "history": "/rest/api/content/70395805/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/70395805/descendant",
      "space": "/rest/api/space/FAQ",
      "relevantViewRestrictions": "/rest/api/content/70395805/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/x-sh"
  },
  "extensions": {
    "mediaType": "application/x-sh",
    "fileSize": 2909,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/70395805/getlogfiles.sh?version=1&modificationDate=1670397521775&api=v2",
    "webui": "/spaces/FAQ/pages/70395805/Where+can+I+find+log+files+of+a+modeling+tool+Cameo+Collaborator+and+Teamwork+Cloud?preview=%2F70395805%2F111218192%2Fgetlogfiles.sh",
    "self": "https://docs.nomagic.com/rest/api/content/111218192"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/111218192/child",
    "restrictions": "/rest/api/content/111218192/restriction/byOperation",
    "history": "/rest/api/content/111218192/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/111218192/descendant",
    "space": "/rest/api/space/FAQ",
    "relevantViewRestrictions": "/rest/api/content/111218192/restriction/relevantViewRestrictions"
  }
}
````
