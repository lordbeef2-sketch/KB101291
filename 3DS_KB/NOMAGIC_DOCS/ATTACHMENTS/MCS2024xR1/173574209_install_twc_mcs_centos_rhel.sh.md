# NOMAGIC ATTACHMENT: install_twc_mcs_centos_rhel.sh

- attachment_id: `173574209`
- space_key: `MCS2024xR1`
- parent_page_id: `173574208`
- parent_page_title: Installing Magic Collaboration Studio services
- media_type: `text/x-sh`
- reported_bytes: 7500
- download_url: https://docs.nomagic.com/download/attachments/173574208/install_twc_mcs_centos_rhel.sh?version=1&modificationDate=1717672808350&api=v2
- payload_kind: `text-exact`
- downloaded_sha256: `0d9df3f6e8c1b75fc4297ce60ff6ff667613aa64d8e99a9571ab8de67646aef3`

## EXACT ATTACHMENT SOURCE

````text
#!/bin/bash
NM_VERSION='2022x Refresh 2'

if [ "$EUID" -ne 0 ];then
	echo
	echo "Please run as root or sudo."
	exit 1
fi
#Obtain OS information using either lsb_release or /etc/os-release
if ( type lsb_release &> /dev/null ); then
	OS=$(lsb_release -is)
	if [[ $OS =~ "RedHat" ]]; then OS="rhel"; fi
	if [[ $OS =~ "CentOS" ]]; then OS="centos"; fi
	OS_V=$(lsb_release -rs | cut -f1 -d.)
elif [ -f /etc/os-release ]; then
	source /etc/os-release
	OS=$ID
	OS_V=$(echo $VERSION_ID | cut -f1 -d.)
else
	echo "Installation Exited: Unable to obtain OS information."
	exit 1
fi
#Check for compatibility
unset PKG_EXE
if [[ $OS  =~ "rhel" ]] || [[ $OS  =~ "centos" ]]; then
	if [[ $OS_V  == "7" ]]; then
		PKG_EXE=yum
	elif [[ $OS_V  == "8" ]]; then
		PKG_EXE=dnf
	fi
fi
if [[ -z "${PKG_EXE}" ]]; then
	echo "Installation Exited: $OS $OS_V is not supported."
	exit 1
fi

#Look for .bin installer file. Ask user to select one if multiple files are found.
BIN_FOUND=$(find *.bin | wc -l)
if [[ $BIN_FOUND == '1' ]]; then
	INSTALLER=$(find *.bin)
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
if [[ $INSTALLER =~ "magic" ]]; then
	PRODUCT="Magic Collaboration Studio ${NM_VERSION}"
elif [[ $INSTALLER =~ "twcloud" ]]; then
	PRODUCT="Teamwork Cloud ${NM_VERSION}"
else
	echo "Unrecognized installer file. Exiting."
	echo exit 1
fi

#Determine OS and set install command for EPEL package
if rpm -q epel-release > /dev/null; then
	EPEL_RELEASE=$(rpm -q epel-release)
	INSTALL_CMDS="echo Package $EPEL_RELEASE already installed, skipping."
else
	if [[ $OS  =~ "rhel" ]]; then
		echo "Installing epel-release for RHEL"
		INSTALL_CMDS="rpm -ivh https://dl.fedoraproject.org/pub/epel/epel-release-latest-$OS_V.noarch.rpm"
	elif [[ $OS  =~ "centos" ]]; then
		echo "Installing epel-release for CentOS 7"
		INSTALL_CMDS="yum -y -q install epel-release"
	fi
fi
#Install EPEL Package
eval $INSTALL_CMDS
$PKG_EXE -y -q update

echo "======================================================"
echo "Installing $PRODUCT"
echo "======================================================"
echo "Installing unzip"
$PKG_EXE install -y unzip
echo "Installing fonts"
$PKG_EXE install -y dejavu-serif-fonts
echo "Installing Tomcat Native Libraries"
$PKG_EXE install -y tomcat-native
echo "Creating twcloud group and user"
getent group twcloud >/dev/null || groupadd -r twcloud
getent passwd twcloud >/dev/null || useradd -d /home/twcloud -g twcloud -m -r twcloud
echo "Creating temporary directory for install anywhere"
IATEMPDIR=$(pwd)/_tmp
export IATEMPDIR
mkdir $IATEMPDIR
echo ""
echo "IMPORTANT: "
echo "           When prompted for user to run service, use twcloud"
echo "           When prompted for Java Home location, use Java 11 location, e.g., /etc/alternatives/jre_11"
echo ""
read -p -"Press any key to continue ...: " -n1 -s
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
</service>
EOF
sleep 10
firewall-cmd --zone=$FWZONE --remove-port=8111/tcp --permanent &> /dev/null
firewall-cmd --zone=$FWZONE --remove-port=3579/tcp --permanent &> /dev/null
firewall-cmd --zone=$FWZONE --remove-port=8555/tcp --permanent &> /dev/null
firewall-cmd --zone=$FWZONE --remove-port=2552/tcp --permanent &> /dev/null
firewall-cmd --zone=$FWZONE --remove-port=2468/tcp --permanent &> /dev/null
firewall-cmd --zone=$FWZONE --add-service=twcloud --permanent
firewall-cmd --reload
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
sysctl -p
else
echo "Skipping post-install performance tuning. Already configured."
fi

echo "  ... Creating disk, CPU, and memory tuning parameters in /home/twcloud/tunedisk.sh"
cat << EOF > /home/twcloud/tunedisk.sh
#!/bin/bash
## Added for disk tuning this read-heavy interactive system
sleep 10
#for DISK in sda sdb sdc sdd
for DISK in \$(ls -all /sys/block | egrep 'sd|xvd|dm' | awk '{for(i=1;i<=NF;i++){if(\$i == "->"){print \$(i-1) OFS}}}')
do
    echo \$DISK
    # Select none scheduler first
    echo none > /sys/block/\${DISK}/queue/scheduler
    echo scheduler: \$(cat /sys/block/\${DISK}/queue/scheduler)
    echo 1 > /sys/block/\${DISK}/queue/nomerges
    echo nomerges: \$(cat /sys/block/\${DISK}/queue/nomerges)
    echo 256 > /sys/block/\${DISK}/queue/read_ahead_kb
    echo read_ahead_kb: \$(cat /sys/block/\${DISK}/queue/read_ahead_kb)
    echo 0 > /sys/block/\${DISK}/queue/rotational
    echo rotational: \$(cat /sys/block/\${DISK}/queue/rotational)
    echo 256 > /sys/block/\${DISK}/queue/nr_requests
    echo nr_requests: \$(cat /sys/block/\${DISK}/queue/nr_requests)
     
    echo 2 > /sys/block/\${DISK}/queue/rq_affinity
    echo rq_affinity: \$(cat /sys/block/\${DISK}/queue/rq_affinity)
done
# Disable huge page defrag
echo never | tee /sys/kernel/mm/transparent_hugepage/defrag
 
#Disable CPU Freq scaling
 
for CPUFREQ in /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
do
    [ -f \$CPUFREQ ] || continue
    echo -n performance > \$CPUFREQ
done
 
#Disable zone-reclaim
 
echo 0 > /proc/sys/vm/zone_reclaim_mode
EOF
sleep 10
chmod +x /home/twcloud/tunedisk.sh
echo "  ... Setting parameters to be executed on server restart"
#Check if rc.local was set to run tunedisk.sh from previous installation. Skip if found.
if ! ( grep -q "tuning for TeamworkCloud" /etc/rc.local ); then
cat <<EOF >> /etc/rc.local
 
#  Perform additional tuning for TeamworkCloud
/home/twcloud/tunedisk.sh
EOF
chmod +x /etc/rc.d/rc.local
fi

echo "  ... Applying tuning changes - there is a 30 second delay before execution"
/home/twcloud/tunedisk.sh
echo "Removing installanywhere temporary directory"
rm -fr $IATEMPDIR
````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "173574209",
  "type": "attachment",
  "status": "current",
  "title": "install_twc_mcs_centos_rhel.sh",
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
    "when": "2024-06-06T13:20:08.350+02:00",
    "message": "",
    "number": 1,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/173574209/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/173574209"
    }
  },
  "position": -1,
  "container": {
    "id": "173574208",
    "type": "page",
    "status": "current",
    "title": "Installing Magic Collaboration Studio services",
    "position": 3,
    "extensions": {
      "position": 3
    },
    "_links": {
      "webui": "/spaces/MCS2024xR1/pages/173574208/Installing+Magic+Collaboration+Studio+services",
      "edit": "/pages/resumedraft.action?draftId=173574208",
      "tinyui": "/x/QIhYCg",
      "self": "https://docs.nomagic.com/rest/api/content/173574208"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS2024xR1",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/173574208/child",
      "restrictions": "/rest/api/content/173574208/restriction/byOperation",
      "history": "/rest/api/content/173574208/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/173574208/descendant",
      "space": "/rest/api/space/MCS2024xR1",
      "relevantViewRestrictions": "/rest/api/content/173574208/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "text/x-sh"
  },
  "extensions": {
    "mediaType": "text/x-sh",
    "fileSize": 7500,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/173574208/install_twc_mcs_centos_rhel.sh?version=1&modificationDate=1717672808350&api=v2",
    "webui": "/spaces/MCS2024xR1/pages/173574208/Installing+Magic+Collaboration+Studio+services?preview=%2F173574208%2F173574209%2Finstall_twc_mcs_centos_rhel.sh",
    "self": "https://docs.nomagic.com/rest/api/content/173574209"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/173574209/child",
    "restrictions": "/rest/api/content/173574209/restriction/byOperation",
    "history": "/rest/api/content/173574209/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/173574209/descendant",
    "space": "/rest/api/space/MCS2024xR1",
    "relevantViewRestrictions": "/rest/api/content/173574209/restriction/relevantViewRestrictions"
  }
}
````
