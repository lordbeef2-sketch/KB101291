# NOMAGIC ATTACHMENT: install_flex_ol_rhel.sh

- attachment_id: `247046463`
- space_key: `MCS`
- parent_page_id: `247046462`
- parent_page_title: Installing the FlexNet server
- media_type: `text/x-sh`
- reported_bytes: 5157
- download_url: https://docs.nomagic.com/download/attachments/247046462/install_flex_ol_rhel.sh?version=1&modificationDate=1754923591721&api=v2
- payload_kind: `text-exact`
- downloaded_sha256: `815c662d39927f2d31acc6e5fed022511fc24736df7e7e4a85d5a58452b345bb`

## EXACT ATTACHMENT SOURCE

````text
#!/bin/bash
FN_INSTALL_PATH=/opt/local/FNPLicenseServerManager
CAMEO_URL=https://d1g91r27pzl568.cloudfront.net/Cameo_daemon/FlexNet_11_19/linux64/cameo.zip
LMGRD_URL=https://d1oqhepk9od1tu.cloudfront.net/Flex_License_Server_Utilities/v11.19.0/linux64/lmgrd.zip
LMADMIN_URL=https://d1oqhepk9od1tu.cloudfront.net/Flex_License_Server_Utilities/v11.19.0/linux64/lmadmin-x64_lsb-11_19_0_0.bin
echo "============================="
echo "Installing Auxiliary Packages"
echo "============================="
yum install -y wget
yum install -y unzip
yum install -y java-11-openjdk
#Install redhat-lsb-core 64-bit
yum install -y redhat-lsb-core.x86_64
echo "=================="
echo "Installing lmadmin"
echo "=================="
echo "Creating temporary directory for install anywhere"
IATEMPDIR=$(pwd)/_tmp
export IAEMPDIR
mkdir $IATEMPDIR
getent group lmadmin >/dev/null || groupadd -r lmadmin
getent passwd lmadmin >/dev/null || useradd -g lmadmin -r lmadmin
echo "lmadmin ALL=(ALL) NOPASSWD:ALL " >> /etc/sudoers
# If Web GUI to Flex licensing is not a must - lmgrd can be used, can be placed in rc.local to startup on boot
# usage - ./lmgrd -c PATH_TO_KEY_FILE -l PATH_TO_LOG_FILE
# RW rights needed to both files
echo "==========================================================="
echo "Getting Linux 64-bit IPv6 version 11.19 "
echo "==========================================================="
wget $CAMEO_URL
unzip cameo.zip
chmod +x cameo
echo "========================================"
echo "Getting Linux 64-bit lmgrd version 11.19"
echo "========================================"
wget $LMGRD_URL
unzip lmgrd.zip
chmod +x lmgrd
echo "======================================"
echo "Making flex log file named FlexLog.log"
echo "======================================"
touch FlexLog.log
chmod 664 FlexLog.log
echo "=========================================="
echo "Getting Linux 64-bit lmadmin version 11.19"
echo "=========================================="
wget $LMADMIN_URL
INSTALLER=$(find lmadmin*.bin)
echo "Installer file: $INSTALLER"
chmod +x $INSTALLER
echo "========================================="
echo "Executing lmadmin version 11.19 installer"
echo "IMPORTANT: Install into directory $FN_INSTALL_PATH"
echo ""
echo " Note:  Accept all defaults for script to work properly!!!"
echo ""
read -p -"Press any key to continue ...: " -n1 -s
echo "=========================================="
JAVA_TOOL_OPTIONS="-Djdk.util.zip.disableZip64ExtraFieldValidation=true" ./$INSTALLER -i console -DUSER_INSTALL_DIR=$FN_INSTALL_PATH
mkdir -p $FN_INSTALL_PATH/licenses/cameo/
cp cameo $FN_INSTALL_PATH/cameo
mv cameo $FN_INSTALL_PATH/licenses/cameo/cameo
mv lmgrd $FN_INSTALL_PATH/lmgrd
mv FlexLog.log $FN_INSTALL_PATH/FlexLog.log
chown -R lmadmin:lmadmin $FN_INSTALL_PATH/

FWSTATUS="$(systemctl is-active firewalld.service)"
if [ "${FWSTATUS}" = "active" ]; then
echo "======================="
echo "Configuring firewall"
echo "======================="
FWZONE=$(firewall-cmd --get-default-zone)
cat <<EOF > /etc/firewalld/services/lmadmin.xml
<?xml version="1.0" encoding="utf-8"?>
<service version="1.0">
    <short>lmadmin</short>
    <description>lmadmin</description>
    <port port="8090" protocol="tcp"/>
    <port port="1101" protocol="tcp"/>
</service>
EOF
sleep 10
firewall-cmd --zone=public --remove-port=8090/tcp --permanent &> /dev/null 
firewall-cmd --zone=public --remove-port=1101/tcp --permanent &> /dev/null 
firewall-cmd --zone=public --remove-port=27000-27009/tcp --permanent &> /dev/null 
firewall-cmd --zone=internal --remove-port=8090/tcp --permanent &> /dev/null 
firewall-cmd --zone=internal --remove-port=1101/tcp --permanent &> /dev/null 
firewall-cmd --zone=internal --remove-port=27000-27009/tcp --permanent &> /dev/null 
firewall-cmd --zone=$FWZONE --add-service=lmadmin --permanent
firewall-cmd --reload
else
echo "========================================================="
echo "Firewall is not running - skipping firewall configuration"
echo "========================================================="
fi

# If IP and host are not resolved properly, uncomment the next 3 lines to associate IP with host.
#IP_ADDRESS=$(ip route get 1 | sed 's/^.*src \([^ ]*\).*$/\1/;q')
#HOSTNAME=$(hostname)
#echo "$IP_ADDRESS     $HOSTNAME" >> /etc/hosts  
echo "=========================================="
echo "Creating systemd service - lmadmin"
echo "=========================================="
cat <<EOF > /etc/systemd/system/lmadmin.service
[Unit]
Description=Flexnet License Daemon
After=network.target network.service

[Service]
User=lmadmin
WorkingDirectory=$FN_INSTALL_PATH/
ExecStart=$FN_INSTALL_PATH/lmadmin -allowStopServer yes
Restart=always
RestartSec=30
Type=forking

[Install]
WantedBy=multi-user.target

EOF
chown root:root /etc/systemd/system/lmadmin.service
chmod 755 /etc/systemd/system/lmadmin.service
systemctl daemon-reload
systemctl enable lmadmin.service
echo "Removing installanywhere temporary directory"
rm -fr $IATEMPDIR
echo "=========================================="
echo "lmadmin service installation complete"
echo "  usage: systemctl start|stop lmadmin"
echo "=========================================="

````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "247046463",
  "type": "attachment",
  "status": "current",
  "title": "install_flex_ol_rhel.sh",
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
    "when": "2025-08-11T16:46:31.721+02:00",
    "message": "",
    "number": 1,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/247046463/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/247046463"
    }
  },
  "position": -1,
  "container": {
    "id": "247046462",
    "type": "page",
    "status": "current",
    "title": "Installing the FlexNet server",
    "position": 2,
    "extensions": {
      "position": 2
    },
    "_links": {
      "webui": "/spaces/MCS/pages/247046462/Installing+the+FlexNet+server",
      "edit": "/pages/resumedraft.action?draftId=247046462",
      "tinyui": "/x/PqG5Dg",
      "self": "https://docs.nomagic.com/rest/api/content/247046462"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/247046462/child",
      "restrictions": "/rest/api/content/247046462/restriction/byOperation",
      "history": "/rest/api/content/247046462/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/247046462/descendant",
      "space": "/rest/api/space/MCS",
      "relevantViewRestrictions": "/rest/api/content/247046462/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "text/x-sh"
  },
  "extensions": {
    "mediaType": "text/x-sh",
    "fileSize": 5157,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/247046462/install_flex_ol_rhel.sh?version=1&modificationDate=1754923591721&api=v2",
    "webui": "/spaces/MCS/pages/247046462/Installing+the+FlexNet+server?preview=%2F247046462%2F247046463%2Finstall_flex_ol_rhel.sh",
    "self": "https://docs.nomagic.com/rest/api/content/247046463"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/247046463/child",
    "restrictions": "/rest/api/content/247046463/restriction/byOperation",
    "history": "/rest/api/content/247046463/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/247046463/descendant",
    "space": "/rest/api/space/MCS",
    "relevantViewRestrictions": "/rest/api/content/247046463/restriction/relevantViewRestrictions"
  }
}
````
