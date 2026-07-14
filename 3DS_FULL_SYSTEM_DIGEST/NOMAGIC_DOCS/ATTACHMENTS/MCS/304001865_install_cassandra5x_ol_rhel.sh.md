# NOMAGIC ATTACHMENT: install_cassandra5x_ol_rhel.sh

- attachment_id: `304001865`
- space_key: `MCS`
- parent_page_id: `304001863`
- parent_page_title: (2026x Refresh1) Installing Apache Cassandra
- media_type: `text/x-sh`
- reported_bytes: 18331
- download_url: https://docs.nomagic.com/download/attachments/304001863/install_cassandra5x_ol_rhel.sh?version=1&modificationDate=1777452421779&api=v2
- payload_kind: `text-exact`
- downloaded_sha256: `63743e44d10195a66a2b2e7842d28e5ca4b8efff53b46126ba4a4391a1df982a`

## EXACT ATTACHMENT SOURCE

````text
#!/bin/bash
CASSANDRA_VER=5.0.5  #Specify Cassandra version to install.

# Java Package Option
CASSANDRA_JAVA_PKG=java-17-openjdk  #Set package name or RPM file of Java

# Install dependency packages. Set to false if network access to package manager is not available. 
#  Check prerequisites in documentation to manually install dependencies.
PKG_INSTALL=true

# Cassandra Configuration Environment
C8_DATA_FILE_DIR=/data
C8_COMMITLOG_DIR=/logs
C8_CONF_PATH=/etc/cassandra/default.conf

INSTALL_C8=true

function print_help {
	cat <<HELP
Usage: install_cassandra5x_ol_rhel.sh [option]

Automated Cassandra installation script. For standard installation, execute script with no options.

Options:
	dryrun			Perform preliminary system checks without actual installation.
	showconf		Show key Cassandra configuration parameters.
	version <version>	Specify a different Cassandra version to install. 
	conf <dir>		Modify configuration for current installation. Specify full path to Cassandra configuration directory.

HELP
	exit 1
}

# Check if Cassandra packages exist locally. Install from local source if found.
function locate_c8pkg {
	#Configure Cassandra package download URLs based on version specified.
	C8_RPM_URL="https://apache.jfrog.io/artifactory/cassandra-rpm"
	C8_PKG_NAME="cassandra-$CASSANDRA_VER-1.noarch.rpm"
	C8_TOOLS_NAME="cassandra-tools-$CASSANDRA_VER-1.noarch.rpm"
	C8_VERX="$(echo $CASSANDRA_VER | cut -c 1,3)x"
	echo && echo "Requested Cassandra Version: $CASSANDRA_VER"
	if [ -f $C8_PKG_NAME ]; then
		CASSANDRA_PKG_URL=$C8_PKG_NAME
		echo "Cassandra will be installed from local $CASSANDRA_PKG_URL"
	else
		CASSANDRA_PKG_URL=$C8_RPM_URL/$C8_VERX/$C8_PKG_NAME
		echo "Cassandra core package download: $CASSANDRA_PKG_URL"
	fi
	if [ -f $C8_TOOLS_NAME ]; then
		CASSANDRA_TOOLS_URL=$C8_TOOLS_NAME
		echo "Cassandra will be installed from local $CASSANDRA_TOOLS_URL"
	else
		CASSANDRA_TOOLS_URL=$C8_RPM_URL/$C8_VERX/$C8_TOOLS_NAME
		echo "Cassandra Tools download: $CASSANDRA_TOOLS_URL"
	fi
}

# Perform preliminary system checks before installation.
function preinstall_checks {
	#If downloading RPM package remotely, confirm remote connection is possible.
	if [[ $CASSANDRA_PKG_URL =~ "https" ]]; then
		if type curl > /dev/null; then 
			echo "Checking remote connection ..."
			if curl --head --silent $CASSANDRA_PKG_URL > /dev/null 2>&1; then
				http_response=$(curl -s -o /dev/null -w "%{response_code}" $CASSANDRA_PKG_URL)
				if [ $http_response != "404" ]; then
					echo "  Success"
				else
					echo "  Cassandra package not found. Please check version specified ($CASSANDRA_VER)."
					unset CASSANDRA_PKG_URL
				fi
			else
				echo "  Remote access to download site failed. Please check network connection or try local installation instead."
				unset CASSANDRA_PKG_URL
			fi
		fi
	fi
	echo
	if [ "$EUID" -ne 0 ];then
		echo "Please run as root or sudo."
		exit 1
	fi
	#Check if current installation exists. Terminate install if Cassandra exists on the system.
	if type -p cassandra > /dev/null; then
		echo "Cassandra $(cassandra -v) installation found. Please uninstall before proceeding with new installation."
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
		OS="Unknown OS"
	fi
	#Set package manager
	if type -p dnf  > /dev/null; then
		PKG_EXE="dnf -y"
	elif type -p yum > /dev/null; then
		PKG_EXE="yum -y"
	else
		echo "Package manager dnf/yum not found. Consider using rpm command for manual installation."
	fi
}

function install_cassandra {
	if [[ $CASSANDRA_PKG_URL =~ "rpm" ]]; then
		echo "========================================================"
		echo "Installing Apache Cassandra $CASSANDRA_VER for $OS $OS_V"
		echo "========================================================"
		echo "Removing old Cassandra repos"
		rm -f /etc/yum.repos.d/cassandra.repo &> /dev/null
		#Install Java for Cassandra and set installed version as default system Java.
		if [ "$PKG_INSTALL" == true ]; then
			echo "============================================="
			echo "Installing Java 17 and Setting System Default"
			echo "============================================="
			$PKG_EXE install -q $CASSANDRA_JAVA_PKG
			alternatives --set java $(grep "java-17" /var/lib/alternatives/java | grep -o -P '(?<=@).*(?=@)')
			$PKG_EXE install -q chkconfig   #Install SysV package for service auto-start.
		fi
		#Install Cassandra RPM packages.
		$PKG_EXE --nogpgcheck install $CASSANDRA_PKG_URL
		$PKG_EXE --nogpgcheck install $CASSANDRA_TOOLS_URL
	fi
	#Verify installation. Exit if Cassandra installation is not found.
	if type -p cassandra > /dev/null; then
		echo "Cassandra $(cassandra -v) base installation verified."
	else
		echo && echo "Installation was not successful. Please look for issues in output above."
		exit 1
	fi
}

function create_firewall_rules {
	FWSTATUS="$(systemctl is-active firewalld.service)"
	if [ "${FWSTATUS}" = "active" ]; then
		echo "======================="
		echo "Configuring firewall"
		echo "======================="
		FWZONE=$(firewall-cmd --get-default-zone)
		echo "Discovered firewall zone $FWZONE"
		cat <<EOF > /etc/firewalld/services/cassandra.xml
<?xml version="1.0" encoding="utf-8"?>
<service version="1.0">
<short>cassandra</short>
	<description>cassandra</description>
	<port port="7000" protocol="tcp"/>
	<port port="9042" protocol="tcp"/>
</service>
EOF
		sleep 10
		firewall-cmd --zone=$FWZONE --add-service=cassandra --permanent
		firewall-cmd --reload
	#This firewalld service will overwrite previous configurations. Use example below to remove custom settings.
	#firewall-cmd --zone=$FWZONE --remove-port=9160/tcp --permanent  &> /dev/null
	else
		echo "======================="
		echo "Firewall is not running - skipping firewall configuration"
		echo "======================="
	fi
}

function create_data_paths {
	echo "====================================================="
	echo "Changing ownership of data and commit log directories"
	echo "====================================================="
	mkdir -p $C8_DATA_FILE_DIR
	mkdir -p $C8_COMMITLOG_DIR
	chown cassandra:cassandra $C8_DATA_FILE_DIR &> /dev/null
	chown cassandra:cassandra $C8_COMMITLOG_DIR &> /dev/null
}

# Make configuration changes to optimize performance.
function configure_c8 {
	C8_CONF_FILES="cassandra.yaml jvm17-server.options jvm11-server.options logback.xml"
	twc_mod_ext=twc-mod
	echo "====================================================="
	echo "Making configuration file changes"
	echo "====================================================="
	#Obtain machine IP address. Revert to localhost if IP not found.
	IP_ADDRESS=$(ip route get 1 | sed 's/^.*src \([^ ]*\).*$/\1/;q')
	if [ -z "$IP_ADDRESS" ]; then IP_ADDRESS=localhost; fi
	#Obtain server CPU count
	NPROCS=$(nproc)
	#Go through configuration file list and make changes.
	for file in $C8_CONF_FILES
	do
	#Create a backup of Cassandra configuration file before modification
	\cp -f $C8_CONF_PATH/$file $C8_CONF_PATH/$file.backup
	#Create a temporary file for modification.
	\cp -f $C8_CONF_PATH/$file ./$file.$twc_mod_ext
	echo "Processing $file ..."
	if [ "$file" == "cassandra.yaml" ]; then
	  # Networking and Topology
		sed -i "s/- seeds: \"127.0.0.1/- seeds: \"$IP_ADDRESS/g" $file.$twc_mod_ext
		sed -i "s/listen_address:.*/listen_address: $IP_ADDRESS/g" $file.$twc_mod_ext
		sed -i "s/# broadcast_rpc_address:.*/broadcast_rpc_address: $IP_ADDRESS/g" $file.$twc_mod_ext
		sed -i "s/broadcast_rpc_address:.*/broadcast_rpc_address: $IP_ADDRESS/g" $file.$twc_mod_ext
		sed -i "s/^rpc_address:.*/rpc_address: 0.0.0.0/g" $file.$twc_mod_ext

		# Storage Path Customization
		sed -i "s/# data_file_directories:.*/data_file_directories:/g" $file.$twc_mod_ext
		sed -i '/data_file_directories:.*/!b;n;c\ \ \ \ - '"$C8_DATA_FILE_DIR"'\/data' $file.$twc_mod_ext
		sed -i "s+# hints_directory:.*+hints_directory: $C8_DATA_FILE_DIR\/hints+g" $file.$twc_mod_ext
		sed -i "s+hints_directory:.*+hints_directory: $C8_DATA_FILE_DIR\/hints+g" $file.$twc_mod_ext
		sed -i "s+# commitlog_directory:.*+commitlog_directory: $C8_COMMITLOG_DIR\/commitlog+g" $file.$twc_mod_ext
		sed -i "s+commitlog_directory:.*+commitlog_directory: $C8_COMMITLOG_DIR\/commitlog+g" $file.$twc_mod_ext
		sed -i "s+# saved_caches_directory:.*+saved_caches_directory: $C8_DATA_FILE_DIR\/saved_caches+g" $file.$twc_mod_ext
		sed -i "s+saved_caches_directory:.*+saved_caches_directory: $C8_DATA_FILE_DIR\/saved_caches+g" $file.$twc_mod_ext

		# Memory and Caches
		sed -i "s/memtable_heap_space:.*/memtable_heap_space: 4092MiB/g" $file.$twc_mod_ext
		sed -i "s/key_cache_size:.*/key_cache_size: 200MiB/g" $file.$twc_mod_ext
		sed -i "s/# file_cache_size: 512MiB/file_cache_size: 3072MiB/g" $file.$twc_mod_ext

    # Commitlog
		sed -i "s/# commitlog_total_space:.*/commitlog_total_space: 8192MiB/g" $file.$twc_mod_ext
		sed -i "s/commitlog_total_space:.*/commitlog_total_space: 8192MiB/g" $file.$twc_mod_ext
		sed -i "s/commitlog_segment_size:.*/commitlog_segment_size: 192MiB/g" $file.$twc_mod_ext

    # Request Timeouts
    sed -i "s/read_request_timeout:.*/read_request_timeout: 1800000ms/g" $file.$twc_mod_ext
		sed -i "s/range_request_timeout:.*/range_request_timeout: 1800000ms/g" $file.$twc_mod_ext
		sed -i "s/^write_request_timeout:.*/write_request_timeout: 1800000ms/g" $file.$twc_mod_ext
		sed -i "s/cas_contention_timeout:.*/cas_contention_timeout: 1000ms/g" $file.$twc_mod_ext
		sed -i "s/truncate_request_timeout:.*/truncate_request_timeout: 1800000ms/g" $file.$twc_mod_ext
		sed -i "s/request_timeout:.*/request_timeout: 1800000ms/g" $file.$twc_mod_ext

		# Concurrent Tasks
		sed -i "s/concurrent_reads: 32/concurrent_reads: 64/g" $file.$twc_mod_ext
    sed -i "s/concurrent_writes: 32/concurrent_writes: 64/g" $file.$twc_mod_ext
    sed -i "s/concurrent_counter_writes: 32/concurrent_counter_writes: 64/g" $file.$twc_mod_ext

    # Throttling and Compaction
		sed -i "s/batch_size_warn_threshold:.*/batch_size_warn_threshold: 3000KiB/g" $file.$twc_mod_ext
		sed -i "s/batch_size_fail_threshold:.*/batch_size_fail_threshold: 5000KiB/g" $file.$twc_mod_ext
		sed -i "s|compaction_throughput:.*|compaction_throughput: 512MiB/s|g" $file.$twc_mod_ext
		sed -i "s|# stream_throughput_outbound: 24MiB/s|stream_throughput_outbound: 4096MiB/s|g" $file.$twc_mod_ext
		sed -i "s/#concurrent_compactors: 1/concurrent_compactors: 1/g" $file.$twc_mod_ext

		# Other Settings
		sed -i "s/internode_compression: dc/internode_compression: all/g" $file.$twc_mod_ext

	elif [ "$file" == "jvm17-server.options" ]; then
		sed -i "s/#-XX:ParallelGCThreads=16/-XX:ParallelGCThreads=$NPROCS/g" $file.$twc_mod_ext
    sed -i "s/#-XX:ConcGCThreads=16/-XX:ConcGCThreads=$NPROCS/g" $file.$twc_mod_ext
    if grep -q MaxDirectMemorySize "$file.$twc_mod_ext"; then
      sed -i 's|^\s*#\?\s*-XX:MaxDirectMemorySize.*|-XX:MaxDirectMemorySize=10G|' "$file.$twc_mod_ext"
    else
      echo "-XX:MaxDirectMemorySize=10G" | sudo tee -a "$file.$twc_mod_ext"
    fi

	elif [ "$file" == "jvm11-server.options" ]; then
		sed -i "s/#-XX:ParallelGCThreads=16/-XX:ParallelGCThreads=$NPROCS/g" $file.$twc_mod_ext
    sed -i "s/#-XX:ConcGCThreads=16/-XX:ConcGCThreads=$NPROCS/g" $file.$twc_mod_ext
    if grep -q MaxDirectMemorySize "$file.$twc_mod_ext"; then
          sed -i 's|^\s*#\?\s*-XX:MaxDirectMemorySize.*|-XX:MaxDirectMemorySize=10G|' "$file.$twc_mod_ext"
        else
          echo "-XX:MaxDirectMemorySize=10G" | tee -a "$file.$twc_mod_ext"
    fi

	elif [ "$file" == "logback.xml" ]; then
		sed -i '/ref="ASYNCDEBUGLOG"/c\\    <!-- <appender-ref ref="ASYNCDEBUGLOG" /> -->' $file.$twc_mod_ext
  fi
  	#Copy modified file to Cassandra configuration path. Delete temporary file.
	#\cp -fR ./$file.$twc_mod_ext $C8_CONF_PATH/$file && rm -f $file.$twc_mod_ext
	\cp -fR ./$file.$twc_mod_ext $C8_CONF_PATH/$file
	done
}

# Output key Cassandra configuration parameters
function check_c8conf {
	file=$C8_CONF_PATH/cassandra.yaml
	if [ -f $file ]; then
		echo "Checking $file"
		echo "====================="
		echo "Configuration Summary"
		echo "====================="
		grep -E "^(cluster_name:|num_tokens:|\\s*- seeds:|listen_address:|rpc_address:|broadcast_rpc_address:|broadcast_address:|endpoint_snitch:)" $file
		grep -A1 "data_file_directories:" $file
		grep -E "^(commitlog_directory:)" $file
		echo
	fi
}

# Create service file for Cassandra and enable
function create_service {
	cat << EOF > /etc/systemd/system/cassandra.service
[Unit]
Description=Apache Cassandra
After=network.target

[Service]
User=cassandra
Group=cassandra
LimitNOFILE=100000
LimitNPROC=32768
LimitMEMLOCK=infinity
EnvironmentFile=/etc/default/cassandra
ExecStart=/usr/sbin/cassandra -f
TimeoutStopSec=600
Restart=on-failure
RestartSec=10
PIDFile=/var/run/cassandra/cassandra.pid

[Install]
WantedBy=multi-user.target
EOF
	sleep 5
	systemctl daemon-reload
	systemctl enable cassandra
}

# Apply system tuning for performance
function tune_system {
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
vm.swappiness = 1
vm.dirty_background_ratio=5
vm.dirty_ratio=80
vm.dirty_expire_centisecs = 12000
EOF
		sleep 10
		sysctl -p -q
	else
		echo "Skipping post-install performance tuning. Already configured."
	fi
	# Configure tunedisk config to run during boot. Replace previous rc.local config.
	TWC_TUNE_PATH=/etc/cassandra
	if ! [ -f $TWC_TUNE_PATH/tunedisk.sh ]; then
		mkdir -p $TWC_TUNE_PATH
		echo "  ... Creating disk, CPU, and memory tuning parameters in:"
		echo "        $TWC_TUNE_PATH/tunedisk.sh"

		cat << EOF > $TWC_TUNE_PATH/tunedisk.sh
#!/bin/bash
set -e
## Added for disk tuning this read-heavy interactive system
sleep 10
#for DISK in sda sdb sdc sdd
for DISK in \$(ls -all /sys/block | egrep 'sd|xvd' | awk '{for(i=1;i<=NF;i++){if(\$i == "->"){print \$(i-1) OFS}}}')
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
		chmod +x $TWC_TUNE_PATH/tunedisk.sh
		echo "  ... Setting parameters to be executed on server restart"
		# Delete previous tunedisk.sh path and set new path.
		sed --in-place /"tuning for TeamworkCloud"/d /etc/rc.local
		sed --in-place /tunedisk.sh/d /etc/rc.local
		cat <<EOF >> /etc/rc.local
#  Perform additional tuning for TeamworkCloud
$TWC_TUNE_PATH/tunedisk.sh
EOF
		chmod +x /etc/rc.d/rc.local
		echo "  ... Applying tuning changes"
		$TWC_TUNE_PATH/tunedisk.sh > $TWC_TUNE_PATH/tunedisk.log
	fi
}

# Check system environment for potential startup and performance issues.
function check_system {
	if [[ ! $(lsblk -l | grep /data) ]]; then
		echo "Cassandra storage requirement exception: /data is not mounted on separate disk."
	fi
	if [[ ! $(lsblk -l | grep /logs) ]]; then
		echo "Cassandra storage requirement exception: /logs is not mounted on separate disk."
	fi
	if [[ $(swapon -s) ]]; then
		echo "Cassandra storage requirement exception: Swap is active. Turn off for better performance."
	fi
	if [[ $(findmnt /tmp | grep noexec) ]]; then
		echo "Potential system exception: /tmp is mounted with noexec. Cassandra service may not be able to start. See FAQ documentation for solution."
	fi
	if type selinuxenabled > /dev/null; then
		selinuxenabled
		if [ $? -eq 0 ]; then
			if [[ $(findmnt /dev/shm | grep noexec) ]]; then
				echo "Potential system exception: /dev/shm is mounted with noexec. Cassandra service may not start when SELinux is enabled. Remount with exec."
			fi
		fi
	fi
	echo "All system checks completed."
}
###############
# Main Script #
###############
if [[ $# -ne 0 ]]; then
	#Process commandline options.
	if [ "$1" == "dryrun" ]; then
		INSTALL_C8=false
	elif [ "$1" == "version" ]; then
		CASSANDRA_VER=$2
	elif [ "$1" == "showconf" ]; then
		check_c8conf && exit 1
	elif [ "$1" == "conf" ]; then
		C8_CONF_PATH=$2
		if [ -f $C8_CONF_PATH/cassandra.yaml ]; then
			configure_c8
		else
			echo "Invalid path specified."
		fi
		exit 1
	else   #Print help if option is not recognized
		print_help
	fi
fi
# Standard installation
locate_c8pkg
preinstall_checks
if [ "$INSTALL_C8" == true ]; then
	install_cassandra
	create_firewall_rules
	create_data_paths
	configure_c8
	create_service
	tune_system
	check_c8conf
	echo "Cassandra installation completed." &&	echo
fi
check_system

````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "304001865",
  "type": "attachment",
  "status": "current",
  "title": "install_cassandra5x_ol_rhel.sh",
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
    "when": "2026-04-29T10:47:01.779+02:00",
    "message": "",
    "number": 1,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/304001865/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/304001865"
    }
  },
  "position": -1,
  "container": {
    "id": "304001863",
    "type": "page",
    "status": "current",
    "title": "(2026x Refresh1) Installing Apache Cassandra",
    "position": 1,
    "extensions": {
      "position": 1
    },
    "_links": {
      "webui": "/spaces/MCS/pages/304001863/2026x+Refresh1+Installing+Apache+Cassandra",
      "edit": "/pages/resumedraft.action?draftId=304001863",
      "tinyui": "/x/R7MeEg",
      "self": "https://docs.nomagic.com/rest/api/content/304001863"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/304001863/child",
      "restrictions": "/rest/api/content/304001863/restriction/byOperation",
      "history": "/rest/api/content/304001863/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/304001863/descendant",
      "space": "/rest/api/space/MCS",
      "relevantViewRestrictions": "/rest/api/content/304001863/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "text/x-sh"
  },
  "extensions": {
    "mediaType": "text/x-sh",
    "fileSize": 18331,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/304001863/install_cassandra5x_ol_rhel.sh?version=1&modificationDate=1777452421779&api=v2",
    "webui": "/spaces/MCS/pages/304001863/2026x+Refresh1+Installing+Apache+Cassandra?preview=%2F304001863%2F304001865%2Finstall_cassandra5x_ol_rhel.sh",
    "self": "https://docs.nomagic.com/rest/api/content/304001865"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/304001865/child",
    "restrictions": "/rest/api/content/304001865/restriction/byOperation",
    "history": "/rest/api/content/304001865/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/304001865/descendant",
    "space": "/rest/api/space/MCS",
    "relevantViewRestrictions": "/rest/api/content/304001865/restriction/relevantViewRestrictions"
  }
}
````
