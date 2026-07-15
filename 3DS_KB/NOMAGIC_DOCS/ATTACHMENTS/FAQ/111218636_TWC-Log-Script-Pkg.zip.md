# NOMAGIC ATTACHMENT: TWC-Log-Script-Pkg.zip

- attachment_id: `111218636`
- space_key: `FAQ`
- parent_page_id: `70395805`
- parent_page_title: Where can I find log files of a modeling tool, Cameo Collaborator, and Teamwork Cloud
- media_type: `application/zip`
- reported_bytes: 4392
- download_url: https://docs.nomagic.com/download/attachments/70395805/TWC-Log-Script-Pkg.zip?version=6&modificationDate=1702281093383&api=v2
- payload_kind: `archive-expanded`
- downloaded_sha256: `df2839a10992d145cdac9c97f7e85625877bfaec1ad1c1ad977f0f9c8e9a81aa`

## ARCHIVE CONTENTS

### ENTRY: clearlogfiles.sh

- bytes: 4899
- crc32: `e457eeb0`
- decoded_as: `utf-8`

````text
#!/bin/bash

# This script renames Teamwork Cloud log files so that fresh logs can be created.
# Execute the script in Linux Bash or Windows Cygwin

TWC_ENV_PATH=/etc/twcloud/twcloud-env
CASSANDRA_LOG_PATH=/var/log/cassandra
TWCLOUD_HOME="/cygdrive/c/Program Files/TeamworkCloud"
echo

# Obtain TWC environment settings for either Linux or Windows Cygwin
if [ -f "$TWC_ENV_PATH" ]; then   #Linux
	source $TWC_ENV_PATH
	USER_HOME_PATH=$(eval echo ~$TWCLOUD_OWNR)
	# Obtain Web App Platform Installation path
	if [ -f /etc/systemd/system/webapp.service ]; then
		WAP_PATH=$(cat /etc/systemd/system/webapp.service | grep CATALINA_HOME_WEBAPP | cut -f3 -d\=)
	fi
	# Check if script is run as root
	if [ "$EUID" -ne 0 ];then
		echo "Please run as root or sudo."
		exit 1
	fi
	# Check if twcloud and webapp services are running
	echo "Checking services ..."
	if (systemctl is-active -q twcloud) && (systemctl is-active -q webapp); then
		echo "Please stop all Teamwork Cloud services before proceeding."
		exit 1
	fi
	# Check if cassandra service is running
	if (systemctl is-active -q cassandra); then
		unset CASSANDRA_LOG_PATH
		echo "Cassandra service is still running. Log file will not be reset."
	fi
elif [ -d "/cygdrive" ]; then   #Windows Cygwin
	echo "Please make sure all Teamwork Cloud services have been stopped before proceeding."
	read -p "Press any key to continue..."
	USER_HOME_PATH=/cygdrive/c/Users/$USER
	CASSANDRA_LOG_PATH=/cygdrive/c/apache-cassandra-3.11.10/logs
	if [ -d "/cygdrive/c/Program Files/CATIANoMagicServices" ]; then
		TWCLOUD_HOME="/cygdrive/c/Program Files/CATIANoMagicServices/TeamworkCloud"
		WAP_PATH="$TWCLOUD_HOME"/../WebAppPlatform
	fi
else
	echo "Unable to determine installation status."
	exit 1
fi

# Verify TWC environment paths
echo "Teamwork Cloud Installation Path: $TWCLOUD_HOME"
echo "Teamwork Cloud User Home Path: $USER_HOME_PATH"
echo

# Determine the latest TWC version installed and rename log files.
if grep -q 2024x $TWCLOUD_HOME/osmc/twc-rest-swagger.json; then
	echo "Clearing 24x server.log"
	[ -f "$TWCLOUD_HOME"/logs/server.log ] && mv -f "$TWCLOUD_HOME"/logs/server.log "$TWCLOUD_HOME"/logs/backup.server.log
	echo "Clearing 24x authentication.log"
	[ -f "$WAP_PATH"/logs/webappplatform/authentication.log ] && mv -f "$WAP_PATH"/logs/webappplatform/authentication.log "$WAP_PATH"/logs/webappplatform/backup.authentication.log
elif [ -d $USER_HOME_PATH/.twcloud/2022x ]; then
	echo "Clearing 22x server.log"
	[ -f $USER_HOME_PATH/.twcloud/2022x/server.log ] && mv -f $USER_HOME_PATH/.twcloud/2022x/server.log $USER_HOME_PATH/.twcloud/2022x/backup.server.log
	echo "Clearing 22x authentication.log"
	[ -f "$WAP_PATH"/logs/webappplatform/authentication.log ] && mv -f "$WAP_PATH"/logs/webappplatform/authentication.log "$WAP_PATH"/logs/webappplatform/backup.authentication.log
elif [ -d $USER_HOME_PATH/.twcloud/2021x ]; then
	echo "Clearing 21x server.log"
	[ -f $USER_HOME_PATH/.twcloud/2021x/server.log ] && mv -f $USER_HOME_PATH/.twcloud/2021x/server.log $USER_HOME_PATH/.twcloud/2021x/backup.server.log
	if (systemctl is-active -q authserver); then
		echo "Please stop authserver service to clear authserver.log"
	else
		echo "Clearing 21x authserver.log"
		[ -f $USER_HOME_PATH/.authserver/2021x/authserver.log ] && mv -f $USER_HOME_PATH/.authserver/2021x/authserver.log $USER_HOME_PATH/.authserver/2021x/backup.authserver.log
	fi
elif [ -d $USER_HOME_PATH/.twcloud/19.0 ]; then
	echo "Clearing v19 server.log"
	mv -f $USER_HOME_PATH/.twcloud/19.0/server.log $USER_HOME_PATH/.twcloud/19.0/backup.server.log
	if (systemctl is-active -q authserver); then
		echo "Please stop authserver service to clear authserver.log"
	else
		echo "Clearing v19 authserver.log"
		[ -f $USER_HOME_PATH/.authserver/19.0/authserver.log ] && mv -f $USER_HOME_PATH/.authserver/19.0/authserver.log $USER_HOME_PATH/.authserver/19.0/backup.authserver.log
	fi
else
	echo "Teamwork Cloud log files not found."
	exit 1
fi
echo "Clearing Web App log"
[ -f "$WAP_PATH"/logs/webappplatform/web-app.log ] && mv -f "$WAP_PATH"/logs/webappplatform/web-app.log "$WAP_PATH"/logs/webappplatform/backup.web-app.log
[ -f "$WAP_PATH"/logs/webappplatform/admin.log ] && mv -f "$WAP_PATH"/logs/webappplatform/admin.log "$WAP_PATH"/logs/webappplatform/backup.admin.log
[ -f "$WAP_PATH"/logs/webappplatform/webapp.log ] && mv -f "$WAP_PATH"/logs/webappplatform/webapp.log "$WAP_PATH"/logs/webappplatform/backup.webapp.log
echo "Clearing catalina.out"
[ -f "$WAP_PATH"/logs/catalina.out ] && mv -f "$WAP_PATH"/logs/catalina.out "$WAP_PATH"/logs/backup.catalina.out
# Rename the Cassandra log file if it exists on the system.
if [ -d "$CASSANDRA_LOG_PATH" ]; then
	echo "Clearing Cassandra log file."
	[ -f $CASSANDRA_LOG_PATH/system.log ] && mv -f $CASSANDRA_LOG_PATH/system.log $CASSANDRA_LOG_PATH/backup.system.log
fi

echo
echo "Teamwork Cloud log files have been cleared."
echo

````

### ENTRY: getlogfiles.sh

- bytes: 4483
- crc32: `469c8ddf`
- decoded_as: `utf-8`

````text
#!/bin/bash

# This script creates a tar package of log files for Teamwork Cloud and/or Web App Platform.
# Execute the script in Linux Bash or Windows Cygwin

# Set Paths Windows Cygwin (Default from 22xR1 and older)
TWCLOUD_HOME="/cygdrive/c/Program Files/TeamworkCloud"
USER_HOME_PATH=/cygdrive/c/Users/$USER
WAP_PATH="$TWCLOUD_HOME"/WebAppPlatform

# Set filenames
TWC_SYS_LOG=0-sys-info.txt
TWC_LOG=1-twc-server.log
WAP_LOG=4-web-app-admin.log
AUTH_LOG=3-authentication.log
CASSANDRA_LOG=2-cassandra-system.log

# Linux Environment Paths
TWC_ENV_PATH=/etc/twcloud/twcloud-env
CASSANDRA_LOG_PATH=/var/log/cassandra/system.log
WAP_SVC_PATH=/etc/systemd/system/webapp.service
echo
# Package Config
TWC_LOG_PKG_PREFIX=TWC-logs
TWC_LOG_EXE_TIME=$(date +"%Y%m%d-%H")
TWC_LOG_PKG=$TWC_LOG_PKG_PREFIX-$TWC_LOG_EXE_TIME.tar

# Create temporary directory to stage log files.
IATEMPDIR=$(pwd)/_tmp
mkdir $IATEMPDIR

# Obtain TWC or WAP environment settings for Linux system
if [ -d /etc/systemd/system ]; then 
	# Obtain server CPU and MEM info
	echo -e "\n### CPU INFO ###\n" >> $IATEMPDIR/$TWC_SYS_LOG
	lscpu | grep CPU >> $IATEMPDIR/$TWC_SYS_LOG
	echo -e "################\n" >> $IATEMPDIR/$TWC_SYS_LOG
	echo -e "### MEM INFO ###" >> $IATEMPDIR/$TWC_SYS_LOG
	free -h >> $IATEMPDIR/$TWC_SYS_LOG
	echo -e "\n################" >> $IATEMPDIR/$TWC_SYS_LOG
	# Check if Teamwork Cloud is installed
	if [ -f $TWC_ENV_PATH ]; then
		source $TWC_ENV_PATH
		USER_HOME_PATH=$(eval echo ~$TWCLOUD_OWNR)
		cat $TWC_ENV_PATH >> $IATEMPDIR/$TWC_SYS_LOG
		echo >> $IATEMPDIR/$TWC_SYS_LOG
	fi
	# Obtain Web App Platform Installation path
	if [ -f $WAP_SVC_PATH ]; then
		WAP_PATH=$(cat $WAP_SVC_PATH | grep CATALINA_HOME_WEBAPP | cut -f3 -d\=)
	else
		echo "Could not locate installation. Exiting..."
		exit 1
	fi
else
	echo "--- Windows Cygwin Mode ---"
	CASSANDRA_LOG_PATH=/cygdrive/c/apache-cassandra-3.11.10/logs/system.log
	# Update paths for 22xR2 and newer releases
	if [ -d "/cygdrive/c/Program Files/CATIANoMagicServices" ]; then
		TWCLOUD_HOME="/cygdrive/c/Program Files/CATIANoMagicServices/TeamworkCloud"
		WAP_PATH="$TWCLOUD_HOME"/../WebAppPlatform
	fi
fi

# Verify TWC environment paths
echo "Web App Platform Installation Path: $WAP_PATH"
echo "Teamwork Cloud User Home Path: $USER_HOME_PATH"

# Determine the latest TWC version installed and copy log files.
if grep -q 2024x $TWCLOUD_HOME/osmc/twc-rest-swagger.json; then
	echo "Copying Teamwork Cloud 24x log file."
	echo "TWC 24x Found" >> $IATEMPDIR/$TWC_SYS_LOG
	cp $TWCLOUD_HOME/logs/server.log $IATEMPDIR/$TWC_LOG
elif [ -d $USER_HOME_PATH/.twcloud/2022x ]; then
	echo "Copying Teamwork Cloud 22x log file."
	echo "TWC 22x Found" >> $IATEMPDIR/$TWC_SYS_LOG
	cp $USER_HOME_PATH/.twcloud/2022x/server.log $IATEMPDIR/$TWC_LOG
elif [ -d $USER_HOME_PATH/.twcloud/2021x ]; then
	echo "Copying Teamwork Cloud 21x log file."
	echo "TWC 21x Found" >> $IATEMPDIR/$TWC_SYS_LOG
	cp $USER_HOME_PATH/.twcloud/2021x/server.log $IATEMPDIR/$TWC_LOG
	cp $USER_HOME_PATH/.authserver/2021x/authserver.log $IATEMPDIR/$AUTH_LOG
elif [ -d $USER_HOME_PATH/.twcloud/19.0 ]; then
	echo "Copying Teamwork Cloud v19 log file."
	echo "TWC 19.0 Found" >> $IATEMPDIR/$TWC_SYS_LOG
	cp $USER_HOME_PATH/.twcloud/19.0/server.log $IATEMPDIR/$TWC_LOG
	cp $USER_HOME_PATH/.authserver/19.0/authserver.log $IATEMPDIR/$AUTH_LOG
else
	echo "Teamwork Cloud log files not found."
fi

# Copy webapps log and logs generated within past 24 hours
cd "$WAP_PATH"/logs
cp webappplatform/*.log $IATEMPDIR/
if [ -f $IATEMPDIR/web-app.log ]; then mv $IATEMPDIR/web-app.log $IATEMPDIR/$WAP_LOG; fi
if [ -f $IATEMPDIR/admin.log ]; then mv $IATEMPDIR/admin.log $IATEMPDIR/$WAP_LOG; fi
if [ -f $IATEMPDIR/authentication.log ]; then mv $IATEMPDIR/authentication.log $IATEMPDIR/$AUTH_LOG; fi
for file in $(find * -newermt "-24 hours" -prune -type f)
do
	cp $file $IATEMPDIR/
done

# Copy the Cassandra log file if it exists on the system.
if [ -f $CASSANDRA_LOG_PATH ]; then
	echo "Copying Cassandra log file."
	cp $CASSANDRA_LOG_PATH $IATEMPDIR/$CASSANDRA_LOG
fi
# Gather system information
if [ -f /etc/os-release ]; then cat /etc/os-release >> $IATEMPDIR/$TWC_SYS_LOG; fi
if command -v systeminfo; then systeminfo >> $IATEMPDIR/$TWC_SYS_LOG; fi

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

### ENTRY: README.md

- bytes: 2323
- crc32: `1f345310`
- decoded_as: `utf-8`

````markdown
Script package for processing Teamwork Cloud log files. These scripts can be executed on Linux and Windows Cygwin. Elevated permissions will be required to execute the scripts in order to access the log files.

## TWC Log File Packager - getlogfiles.sh

Script for gathering all the TWC-related log files and system information into a tar package. 

**Warning:** The script will access and store system information, including OS version, memory, and CPU data.

A path check of services in /etc/systemd/system/ is used to determine whether the system is Linux or Windows. The Web App Platform installation path is obtained from the webapp.service file. Another path check of _$CASSANDRA_LOG_PATH_ is used to deterine whether Cassandra is installed on the same server as TWC.

For 24x, the new $TWCLOUD_HOME/logs path is checked. Older TWC versions are determined by checking _$USER_HOME_PATH_/.twcloud. The script will assume the latest version found is the TWC currently running on the server. For example, if .twcloud/2022x and .twcloud/2021x exist, then it is assumed that 2022x is the installed version running on the server. The version will determine where the authentication logs will be retrieved. 

List of log files:
- server.log (TWC)
- system.log (Cassandra, if installed on the same server)
- webapps/*.log (including webapp.log/web-app.log and authentication.log)
- authserver.log (if 21x or older)
- Catalina and access logs from the past 24 hours

The script will also gather system information and write to a `sys-info.txt` file.

Linux:
- twcloud-env content
- CPU (lscpu)
- Memory (free)
- OS (/etc/os-release)

Windows Cygwin (systeminfo):
- OS
- Memory

All files are archived in a tar package with the filename: `TWC-logs-<YMD Date>-<Hour>.tar`

## TWC Log File Reset - clearlogfiles.sh

Script for renaming all the TWC-relevant log files so that a fresh set of log files can be generated. This is typically used to prepare a log file package for a support request.

The overall logic is similar to the `getlogfiles.sh` script. For Linux, an additional check is implemented to verify if the associated services have been stopped. If the service is not stopped, then the associated log file will not be renamed. For Windows Cygwin, a message will remind the user to stop all services before proceeding.

````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "111218636",
  "type": "attachment",
  "status": "current",
  "title": "TWC-Log-Script-Pkg.zip",
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
    "when": "2023-12-11T08:51:33.383+01:00",
    "message": "",
    "number": 6,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/111218636/version/6"
    },
    "_expandable": {
      "content": "/rest/api/content/111218636"
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
    "mediaType": "application/zip"
  },
  "extensions": {
    "mediaType": "application/zip",
    "fileSize": 4392,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/70395805/TWC-Log-Script-Pkg.zip?version=6&modificationDate=1702281093383&api=v2",
    "webui": "/spaces/FAQ/pages/70395805/Where+can+I+find+log+files+of+a+modeling+tool+Cameo+Collaborator+and+Teamwork+Cloud?preview=%2F70395805%2F111218636%2FTWC-Log-Script-Pkg.zip",
    "self": "https://docs.nomagic.com/rest/api/content/111218636"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/111218636/child",
    "restrictions": "/rest/api/content/111218636/restriction/byOperation",
    "history": "/rest/api/content/111218636/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/111218636/descendant",
    "space": "/rest/api/space/FAQ",
    "relevantViewRestrictions": "/rest/api/content/111218636/restriction/relevantViewRestrictions"
  }
}
````
