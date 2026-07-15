# NOMAGIC ATTACHMENT: install_twc_mcs_ol_rhel.sh

- attachment_id: `275415183`
- space_key: `MCS`
- parent_page_id: `247046464`
- parent_page_title: Installing services
- media_type: `text/x-sh`
- reported_bytes: 5129
- download_url: https://docs.nomagic.com/download/attachments/247046464/install_twc_mcs_ol_rhel.sh?version=2&modificationDate=1764594971735&api=v2
- payload_kind: `text-exact`
- downloaded_sha256: `803dd6bbd66192769d15171778f2ce735a37f81c98b41d5c53e76a3cccf8610f`

## EXACT ATTACHMENT SOURCE

````text
#!/bin/bash
NM_VERSION='2026x'

#Document exporter font package. Specify local RPM file if installing locally.
DOC_EXPORT_FONT_PKG=dejavu-serif-fonts
echo
if [ "$EUID" -ne 0 ];then
	echo "Please run as root or sudo."
	exit 1
fi
#Obtain OS information using either lsb_release or /etc/os-release
if ( type lsb_release &> /dev/null ); then
	OS=$(lsb_release -is)
	if [[ $OS =~ "RedHat" ]]; then OS="rhel"; fi
	if [[ $OS =~ "Oracle" ]]; then OS="ol"; fi
	OS_V=$(lsb_release -rs | cut -f1 -d.)
elif [ -f /etc/os-release ]; then
	source /etc/os-release
	OS=$ID
	OS_V=$(echo $VERSION_ID | cut -f1 -d.)
else
	echo "Installation Exited: Unable to obtain OS information."
	exit 1
fi
#Set package manager
if type -p dnf  > /dev/null; then
	PKG_EXE="dnf -y"
elif type -p yum > /dev/null; then
	PKG_EXE="yum -y"
else
	echo "Package manager dnf/yum not found. Consider using rpm command for manual installation."
fi

#Look for .bin installer file. Ask user to select one if multiple files are found.
BIN_FOUND=$(find *.bin 2>/dev/null | wc -l)
if [[ $BIN_FOUND == '1' ]]; then
	INSTALLER=$(find *.bin)
elif [[ $BIN_FOUND == '0' ]]; then
	echo "No installer (.bin) file found. Please place installer in current path and try again."
	exit 1
else
	echo
	echo "Multiple installer files found. Please select file for installation."
	BIN_FILES=($(ls *.bin))
	select file in "${BIN_FILES[@]}"; do
		if [[ -n $file ]]; then
			INSTALLER=$file
			break
		else
			echo "Invalid selection"
		fi
	done
fi

if [[ $INSTALLER =~ "magic" || $INSTALLER =~ "Magic" ]]; then
  PRODUCT="Magic Collaboration Studio ${NM_VERSION}"
elif [[ $INSTALLER =~ "twcloud" || $INSTALLER =~ "TeamworkCloud" ]]; then
  PRODUCT="Teamwork Cloud ${NM_VERSION}"
else
  echo "Unrecognized installer file. Exiting."
  exit 1
fi

echo "======================================================"
echo "Installing $PRODUCT"
echo "======================================================"

#Check if font package is installed. Try to install from repository or local RPM.
if ! rpm -q $DOC_EXPORT_FONT_PKG; then
	echo "Attempting to install fonts package for Document Exporter"
	$PKG_EXE install $DOC_EXPORT_FONT_PKG
fi

echo "Creating temporary directory for install anywhere"
IATEMPDIR=$(pwd)/_tmp
export IATEMPDIR
mkdir $IATEMPDIR
echo ""
echo "IMPORTANT: "
echo "           When prompted for user to run service, use twcloud"
echo "           When prompted for Java Home location, use Java 21 location, e.g., /etc/alternatives/jre_21"
echo ""
read -p -"Press any key to continue ...: " -n1 -s
echo
echo "Main installer starting ..."
chmod +x $INSTALLER
./$INSTALLER

FWSTATUS="$(systemctl is-active firewalld.service)"
if [ "${FWSTATUS}" = "active" ]; then
echo "======================="
echo "Configuring firewall"
echo "======================="
FWZONE=$(firewall-cmd --get-default-zone)
echo "Discovered firewall zone $FWZONE"
cat <<EOF > /etc/firewalld/services/twcloud.xml
<?xml version="1.0" encoding="utf-8"?>
<service version="1.0">
    <short>twcloud</short>
    <description>twcloud</description>
    <port port="8111" protocol="tcp"/>
    <port port="3579" protocol="tcp"/>
    <port port="10002" protocol="tcp"/>
    <port port="2552" protocol="tcp"/>
    <port port="2468" protocol="tcp"/>
    <port port="8443" protocol="tcp"/>
  	<port port="2181" protocol="tcp"/>
</service>
EOF
sleep 10
firewall-cmd --zone=$FWZONE --add-service=twcloud --permanent
firewall-cmd --reload
#This firewalld service will overwrite previous configurations. Use example below to remove custom settings.
#firewall-cmd --zone=$FWZONE --remove-port=8555/tcp --permanent &> /dev/null
else
echo "======================="
echo "Firewall is not running - skipping firewall configuration"
echo "======================="
fi

echo "Increase file limits for twcloud user"
echo "twcloud - nofile 50000" > /etc/security/limits.d/twcloud.conf

#Check if tuning was applied from previous installation. Skip if applied from before.
if ! ( grep -q "tunings for Teamwork Cloud" /etc/sysctl.conf ); then
echo "Applying post-install performance tuning"
echo "  /etc/sysctl.conf tuning"
cat <<EOF >> /etc/sysctl.conf
 
#  Preliminary tunings for Teamwork Cloud
net.core.rmem_max=16777216
net.core.wmem_max=16777216
net.core.optmem_max=40960
net.core.default_qdisc=fq
net.core.somaxconn=4096
net.ipv4.conf.all.arp_notify = 1
net.ipv4.tcp_keepalive_time=60
net.ipv4.tcp_keepalive_probes=3
net.ipv4.tcp_keepalive_intvl=10
net.ipv4.tcp_mtu_probing=1
net.ipv4.tcp_rmem=4096 12582912 16777216
net.ipv4.tcp_wmem=4096 12582912 16777216
net.ipv4.tcp_max_syn_backlog=8096
net.ipv4.tcp_slow_start_after_idle = 0
net.ipv4.tcp_tw_reuse = 1
vm.max_map_count = 1048575
vm.swappiness = 0
vm.dirty_background_ratio=5
vm.dirty_ratio=80
vm.dirty_expire_centisecs = 12000
EOF
sleep 10
sysctl -p -q
else
echo "Skipping post-install performance tuning. Already configured."
fi

echo "Removing installanywhere temporary directory"
rm -fr $IATEMPDIR

echo "Post-install configuration completed."
echo "Additional shortcuts and utilities available at:"
echo
( . /etc/twcloud/twcloud-env; echo "${TWCLOUD_HOME%/*}/Utilities/AdminTools" )
echo
````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "275415183",
  "type": "attachment",
  "status": "current",
  "title": "install_twc_mcs_ol_rhel.sh",
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
    "when": "2025-12-01T14:16:11.735+01:00",
    "message": "",
    "number": 2,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/275415183/version/2"
    },
    "_expandable": {
      "content": "/rest/api/content/275415183"
    }
  },
  "position": -1,
  "container": {
    "id": "247046464",
    "type": "page",
    "status": "current",
    "title": "Installing services",
    "position": 3,
    "extensions": {
      "position": 3
    },
    "_links": {
      "webui": "/spaces/MCS/pages/247046464/Installing+services",
      "edit": "/pages/resumedraft.action?draftId=247046464",
      "tinyui": "/x/QKG5Dg",
      "self": "https://docs.nomagic.com/rest/api/content/247046464"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/247046464/child",
      "restrictions": "/rest/api/content/247046464/restriction/byOperation",
      "history": "/rest/api/content/247046464/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/247046464/descendant",
      "space": "/rest/api/space/MCS",
      "relevantViewRestrictions": "/rest/api/content/247046464/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "text/x-sh"
  },
  "extensions": {
    "mediaType": "text/x-sh",
    "fileSize": 5129,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/247046464/install_twc_mcs_ol_rhel.sh?version=2&modificationDate=1764594971735&api=v2",
    "webui": "/spaces/MCS/pages/247046464/Installing+services?preview=%2F247046464%2F275415183%2Finstall_twc_mcs_ol_rhel.sh",
    "self": "https://docs.nomagic.com/rest/api/content/275415183"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/275415183/child",
    "restrictions": "/rest/api/content/275415183/restriction/byOperation",
    "history": "/rest/api/content/275415183/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/275415183/descendant",
    "space": "/rest/api/space/MCS",
    "relevantViewRestrictions": "/rest/api/content/275415183/restriction/relevantViewRestrictions"
  }
}
````
