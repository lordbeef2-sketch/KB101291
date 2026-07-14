# NOMAGIC ATTACHMENT: clearlogfiles.sh

- attachment_id: `111218191`
- space_key: `FAQ`
- parent_page_id: `70395805`
- parent_page_title: Where can I find log files of a modeling tool, Cameo Collaborator, and Teamwork Cloud
- media_type: `application/x-sh`
- reported_bytes: 3282
- download_url: https://docs.nomagic.com/download/attachments/70395805/clearlogfiles.sh?version=1&modificationDate=1670397521410&api=v2
- payload_kind: `text-exact`
- downloaded_sha256: `1e96d71c5b621f0bf38f25aefaf93c0426ee6df197e265b0683ca11c18b43c8d`

## EXACT ATTACHMENT SOURCE

````text
#!/bin/bash

# This script renames Teamwork Cloud log files so that fresh logs can be created.
# Execute the script in Linux Bash or Windows Cygwin

echo
TWC_ENV_PATH=/etc/twcloud/twcloud-env
CASSANDRA_LOG_PATH=/var/log/cassandra

# Obtain TWC environment settings for either Linux or Windows Cygwin
if [ -f $TWC_ENV_PATH ]; then   #Linux
	source $TWC_ENV_PATH
	USER_HOME_PATH=$(eval echo ~$TWCLOUD_OWNR)
	# Check if script is run as root
	if [ "$EUID" -ne 0 ];then
		echo "Please run as root or sudo."
		exit 1
	fi
	# Check if twcloud and webapp services are running
	if (systemctl is-active -q twcloud) && (systemctl is-active -q webapp); then
		echo "Please stop all Teamwork Cloud services before proceeding."
		exit 1
	fi
else   #Windows Cygwin
	echo "Please make sure all Teamwork Cloud services have been stopped before proceeding."
	read -p "Press any key to continue..."
	USER_HOME_PATH=/cygdrive/c/Users/$USER
	TWCLOUD_HOME="/cygdrive/c/Program Files/TeamworkCloud"
fi

TWC_ENV_PATH=/etc/twcloud/twcloud-env
CASSANDRA_LOG_PATH=/var/log/cassandra

# Verify TWC environment paths
echo "Teamwork Cloud Installation Path: $TWCLOUD_HOME"
echo "Teamwork Cloud User Home Path: $USER_HOME_PATH"

# Determine the latest TWC version installed and copy log files.
if [ -d $USER_HOME_PATH/.twcloud/2022x ]; then
	echo "Clearing 22x server.log"
	mv -f $USER_HOME_PATH/.twcloud/2022x/server.log $USER_HOME_PATH/.twcloud/2022x/backup.server.log
	echo "Clearing 22x authentication.log"
	mv -f "$TWCLOUD_HOME"/WebAppPlatform/logs/webappplatform/authentication.log "$TWCLOUD_HOME"/WebAppPlatform/logs/webappplatform/backup.authentication.log
elif [ -d $USER_HOME_PATH/.twcloud/2021x ]; then
	echo "Clearing 21x server.log"
	mv -f $USER_HOME_PATH/.twcloud/2021x/server.log $USER_HOME_PATH/.twcloud/2021x/backup.server.log
	if (systemctl is-active -q authserver); then
		echo "Please stop authserver service to clear authserver.log"
	else
		echo "Clearing 21x authserver.log"
		mv -f $USER_HOME_PATH/.authserver/2021x/authserver.log $USER_HOME_PATH/.authserver/2021x/backup.authserver.log
	fi
elif [ -d $USER_HOME_PATH/.twcloud/19.0 ]; then
	echo "Clearing v19 server.log"
	mv -f $USER_HOME_PATH/.twcloud/19.0/server.log $USER_HOME_PATH/.twcloud/19.0/backup.server.log
	if (systemctl is-active -q authserver); then
		echo "Please stop authserver service to clear authserver.log"
	else
		echo "Clearing v19 authserver.log"
		mv -f $USER_HOME_PATH/.authserver/19.0/authserver.log $USER_HOME_PATH/.authserver/19.0/backup.authserver.log
	fi
else
	echo "Teamwork Cloud log files not found."
	exit 1
fi
echo "Clearing web-app.log"
mv -f "$TWCLOUD_HOME"/WebAppPlatform/logs/webappplatform/web-app.log "$TWCLOUD_HOME"/WebAppPlatform/logs/webappplatform/backup.web-app.log
echo "Clearing catalina.out"
mv -f "$TWCLOUD_HOME"/WebAppPlatform/logs/catalina.out "$TWCLOUD_HOME"/WebAppPlatform/logs/backup.catalina.out
# Copy the Cassandra log file if it exists on the system.
if [ -d $CASSANDRA_LOG_PATH ]; then
	if (systemctl is-active -q cassandra); then
		echo "Please stop cassandra service to clear system.log"
	else
		echo "Clearing Cassandra log file."
		mv -f $CASSANDRA_LOG_PATH/system.log $CASSANDRA_LOG_PATH/backup.system.log
	fi
fi

echo
echo "Teamwork Cloud log files have been cleared."
echo

````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "111218191",
  "type": "attachment",
  "status": "current",
  "title": "clearlogfiles.sh",
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
    "when": "2022-12-07T08:18:41.410+01:00",
    "message": "",
    "number": 1,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/111218191/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/111218191"
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
    "fileSize": 3282,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/70395805/clearlogfiles.sh?version=1&modificationDate=1670397521410&api=v2",
    "webui": "/spaces/FAQ/pages/70395805/Where+can+I+find+log+files+of+a+modeling+tool+Cameo+Collaborator+and+Teamwork+Cloud?preview=%2F70395805%2F111218191%2Fclearlogfiles.sh",
    "self": "https://docs.nomagic.com/rest/api/content/111218191"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/111218191/child",
    "restrictions": "/rest/api/content/111218191/restriction/byOperation",
    "history": "/rest/api/content/111218191/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/111218191/descendant",
    "space": "/rest/api/space/FAQ",
    "relevantViewRestrictions": "/rest/api/content/111218191/restriction/relevantViewRestrictions"
  }
}
````
