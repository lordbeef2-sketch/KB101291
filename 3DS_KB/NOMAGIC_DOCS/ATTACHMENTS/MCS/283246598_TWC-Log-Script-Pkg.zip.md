# NOMAGIC ATTACHMENT: TWC-Log-Script-Pkg.zip

- attachment_id: `283246598`
- space_key: `MCS`
- parent_page_id: `282460195`
- parent_page_title: Downloadable scripts
- media_type: `application/zip`
- reported_bytes: 4671
- download_url: https://docs.nomagic.com/download/attachments/282460195/TWC-Log-Script-Pkg.zip?version=1&modificationDate=1767618666491&api=v2
- payload_kind: `archive-expanded`
- downloaded_sha256: `17e61ebfaeaaf9afadc82794e898284238e5041a4c7c16c6ab31ef44a0199160`

## ARCHIVE CONTENTS

### ENTRY: clearlogfiles.sh

- bytes: 5537
- crc32: `2f06d96b`
- decoded_as: `utf-8`

````text
#!/bin/bash

# This script renames Teamwork Cloud log files so that fresh logs can be created.
# Execute the script in Linux Bash or Windows Cygwin

TWC_ENV_PATH="/etc/twcloud/twcloud-env"
WAP_SVC_PATH="/etc/systemd/system/webapp.service"
CASSANDRA_LOG_PATH="/var/log/cassandra"
TWCLOUD_HOME="/cygdrive/c/Program Files/TeamworkCloud"
echo

# Obtain TWC environment settings for either Linux or Windows Cygwin
if [ -f "$TWC_ENV_PATH" ]; then   #Linux
	source "$TWC_ENV_PATH"
	USER_HOME_PATH=$(eval echo ~"$TWCLOUD_OWNR")
  # Detect WebApp Platform installation path (compatible with 2024x and 2026x)
  if [ -f "$WAP_SVC_PATH" ]; then
    if grep -q "CATALINA_HOME_WEBAPP" "$WAP_SVC_PATH"; then
      WAP_PATH=$(grep "CATALINA_HOME_WEBAPP" "$WAP_SVC_PATH" | cut -f3 -d=)
    elif grep -q "CATALINA_HOME=" "$WAP_SVC_PATH"; then
      WAP_PATH=$(grep "CATALINA_HOME=" "$WAP_SVC_PATH" | cut -f3 -d=)
    else
      echo "Warning: Could not determine WebApp Platform path from '$WAP_SVC_PATH'"
    fi
  fi
	# Check if script is run as root
	if [ "$EUID" -ne 0 ]; then
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
	USER_HOME_PATH="/cygdrive/c/Users/$USER"
	CASSANDRA_LOG_PATH="/cygdrive/c/apache-cassandra-3.11.10/logs"
	WIN_INSTALL_PATH="/cygdrive/c/Program Files"
	if [ -d "$WIN_INSTALL_PATH/CATIANoMagicServices" ]; then
		TWCLOUD_HOME="$WIN_INSTALL_PATH/CATIANoMagicServices/TeamworkCloud"
	elif [ -d "$WIN_INSTALL_PATH/MagicCollaborationStudio" ]; then
		TWCLOUD_HOME="$WIN_INSTALL_PATH/MagicCollaborationStudio/TeamworkCloud"
	fi
	if [ -d "$TWCLOUD_HOME/../WebAppPlatform" ]; then WAP_PATH="$TWCLOUD_HOME/../WebAppPlatform"; fi
else
	echo "Unable to determine installation status."
	exit 1
fi

# Verify TWC environment paths
echo "Teamwork Cloud Installation Path: '$TWCLOUD_HOME'"
echo "Teamwork Cloud User Home Path: '$USER_HOME_PATH'"
echo

# Determine the latest TWC version installed and rename log files.
if grep -Eq "2024x|2026x" "$TWCLOUD_HOME/osmc/twc-rest-swagger.json"; then
	echo "Clearing 2024x/2026x server.log"
	[ -f "$TWCLOUD_HOME/logs/server.log" ] && mv -f "$TWCLOUD_HOME/logs/server.log" "$TWCLOUD_HOME/logs/backup.server.log"
	echo "Clearing 2024x/2026x authentication.log"
	[ -f "$WAP_PATH/logs/webappplatform/authentication.log" ] && mv -f "$WAP_PATH/logs/webappplatform/authentication.log" "$WAP_PATH/logs/webappplatform/backup.authentication.log"
elif [ -d "$USER_HOME_PATH/.twcloud/2022x" ]; then
	echo "Clearing 22x server.log"
	[ -f "$USER_HOME_PATH/.twcloud/2022x/server.log" ] && mv -f "$USER_HOME_PATH/.twcloud/2022x/server.log" "$USER_HOME_PATH/.twcloud/2022x/backup.server.log"
	echo "Clearing 22x authentication.log"
	[ -f "$WAP_PATH/logs/webappplatform/authentication.log" ] && mv -f "$WAP_PATH/logs/webappplatform/authentication.log" "$WAP_PATH/logs/webappplatform/backup.authentication.log"
elif [ -d "$USER_HOME_PATH/.twcloud/2021x" ]; then
	echo "Clearing 21x server.log"
	[ -f "$USER_HOME_PATH/.twcloud/2021x/server.log" ] && mv -f "$USER_HOME_PATH/.twcloud/2021x/server.log" "$USER_HOME_PATH/.twcloud/2021x/backup.server.log"
	if (systemctl is-active -q authserver); then
		echo "Please stop authserver service to clear authserver.log"
	else
		echo "Clearing 21x authserver.log"
		[ -f "$USER_HOME_PATH/.authserver/2021x/authserver.log" ] && mv -f "$USER_HOME_PATH/.authserver/2021x/authserver.log" "$USER_HOME_PATH/.authserver/2021x/backup.authserver.log"
	fi
elif [ -d "$USER_HOME_PATH/.twcloud/19.0" ]; then
	echo "Clearing v19 server.log"
	mv -f "$USER_HOME_PATH/.twcloud/19.0/server.log" "$USER_HOME_PATH/.twcloud/19.0/backup.server.log"
	if (systemctl is-active -q authserver); then
		echo "Please stop authserver service to clear authserver.log"
	else
		echo "Clearing v19 authserver.log"
		[ -f "$USER_HOME_PATH/.authserver/19.0/authserver.log" ] && mv -f "$USER_HOME_PATH/.authserver/19.0/authserver.log" "$USER_HOME_PATH/.authserver/19.0/backup.authserver.log"
	fi
else
	echo "Teamwork Cloud log files not found."
	exit 1
fi
echo "Clearing Web App log"
[ -f "$WAP_PATH/logs/webappplatform/web-app.log" ] && mv -f "$WAP_PATH/logs/webappplatform/web-app.log" "$WAP_PATH/logs/webappplatform/backup.web-app.log"
[ -f "$WAP_PATH/logs/webappplatform/admin.log" ] && mv -f "$WAP_PATH/logs/webappplatform/admin.log" "$WAP_PATH/logs/webappplatform/backup.admin.log"
[ -f "$WAP_PATH/logs/webappplatform/webapp.log" ] && mv -f "$WAP_PATH/logs/webappplatform/webapp.log" "$WAP_PATH/logs/webappplatform/backup.webapp.log"
echo "Clearing catalina.out"
[ -f "$WAP_PATH/logs/catalina.out" ] && mv -f "$WAP_PATH/logs/catalina.out" "$WAP_PATH/logs/backup.catalina.out"
# Rename the Cassandra log file if it exists on the system.
if [ -d "$CASSANDRA_LOG_PATH" ]; then
	echo "Clearing Cassandra log file."
	[ -f "$CASSANDRA_LOG_PATH/system.log" ] && mv -f "$CASSANDRA_LOG_PATH/system.log" "$CASSANDRA_LOG_PATH/backup.system.log"
fi

echo
echo "Teamwork Cloud log files have been cleared."
echo

````

### ENTRY: getlogfiles.sh

- bytes: 5011
- crc32: `d493d920`
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
TWC_LOG_PKG=$TWC_LOG_PKG_PREFIX-$TWC_LOG_EXE_TIME.tar.gz

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

  # Detect WebApp Platform installation path (compatible with 2024x and 2026x)
	if [ -f $WAP_SVC_PATH ]; then
		if grep -q "CATALINA_HOME_WEBAPP" "$WAP_SVC_PATH"; then
			WAP_PATH=$(grep "CATALINA_HOME_WEBAPP" "$WAP_SVC_PATH" | cut -f3 -d=)
		elif grep -q "CATALINA_HOME=" "$WAP_SVC_PATH"; then
			WAP_PATH=$(grep "CATALINA_HOME=" "$WAP_SVC_PATH" | cut -f3 -d=)
		else
			echo "Could not determine Web App Platform installation path from $WAP_SVC_PATH"
		fi

  elif [ -d /cygdrive ]; then
    echo "--- Windows Cygwin Mode ---"
    CASSANDRA_LOG_PATH=/cygdrive/c/apache-cassandra-3.11.10/logs/system.log
    WIN_INSTALL_PATH="/cygdrive/c/Program Files"
    # Update paths for 22xR2 and newer releases
    if [ -d "$WIN_INSTALL_PATH"/CATIANoMagicServices ]; then
      TWCLOUD_HOME="$WIN_INSTALL_PATH"/CATIANoMagicServices/TeamworkCloud
    elif [ -d "$WIN_INSTALL_PATH"/MagicCollaborationStudio ]; then
      TWCLOUD_HOME="$WIN_INSTALL_PATH"/MagicCollaborationStudio/TeamworkCloud
    fi
    if [ -d "$TWCLOUD_HOME"/../WebAppPlatform ]; then WAP_PATH="$TWCLOUD_HOME"/../WebAppPlatform; fi
  else
    echo "Unable to determine installation status."
  fi
fi

# Determine the latest TWC version installed and copy log files.
if grep -Eq "2024x|2026x" "$TWCLOUD_HOME"/osmc/twc-rest-swagger.json; then
	echo "Copying Teamwork Cloud 24x/26x log file."
	echo "TWC 24x/26x Found" >> $IATEMPDIR/$TWC_SYS_LOG
	cp "$TWCLOUD_HOME"/logs/server.log $IATEMPDIR/$TWC_LOG
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

# Copy webapp logs generated within past 24 hours
if [ -d "$WAP_PATH" ]; then
	cd "$WAP_PATH"/logs
	echo "Copying Web App Platform log files."
	cp webappplatform/*.log $IATEMPDIR/
	if [ -f $IATEMPDIR/web-app.log ]; then mv $IATEMPDIR/web-app.log $IATEMPDIR/$WAP_LOG; fi
	if [ -f $IATEMPDIR/admin.log ]; then mv $IATEMPDIR/admin.log $IATEMPDIR/$WAP_LOG; fi
	if [ -f $IATEMPDIR/authentication.log ]; then mv $IATEMPDIR/authentication.log $IATEMPDIR/$AUTH_LOG; fi
	for file in $(find * -newermt "-24 hours" -prune -type f)
	do
		cp $file $IATEMPDIR/
	done
fi
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
cd $IATEMPDIR && tar cvzf $TWC_LOG_PKG * && mv $TWC_LOG_PKG ../ && cd ..

# Remove temporary directory
rm -fr $IATEMPDIR
echo
echo "Log package created: $TWC_LOG_PKG"
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
  "id": "283246598",
  "type": "attachment",
  "status": "current",
  "title": "TWC-Log-Script-Pkg.zip",
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
    "when": "2026-01-05T14:11:06.491+01:00",
    "message": "",
    "number": 1,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/283246598/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/283246598"
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
    "mediaType": "application/zip"
  },
  "extensions": {
    "mediaType": "application/zip",
    "fileSize": 4671,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/282460195/TWC-Log-Script-Pkg.zip?version=1&modificationDate=1767618666491&api=v2",
    "webui": "/spaces/MCS/pages/282460195/Downloadable+scripts?preview=%2F282460195%2F283246598%2FTWC-Log-Script-Pkg.zip",
    "self": "https://docs.nomagic.com/rest/api/content/283246598"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/283246598/child",
    "restrictions": "/rest/api/content/283246598/restriction/byOperation",
    "history": "/rest/api/content/283246598/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/283246598/descendant",
    "space": "/rest/api/space/MCS",
    "relevantViewRestrictions": "/rest/api/content/283246598/restriction/relevantViewRestrictions"
  }
}
````
