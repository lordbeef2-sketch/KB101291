# NOMAGIC ATTACHMENT: TWC_MCS_install_scripts_2024xRefresh3.zip

- attachment_id: `239798886`
- space_key: `MCS2024xR3`
- parent_page_id: `227173072`
- parent_page_title: Installation on Linux
- media_type: `application/zip`
- reported_bytes: 11366
- download_url: https://docs.nomagic.com/download/attachments/227173072/TWC_MCS_install_scripts_2024xRefresh3.zip?version=2&modificationDate=1761043675474&api=v2
- payload_kind: `archive-expanded`
- downloaded_sha256: `43a12302c5bdc630ea11cea5c81c6acabfab74fa248b32441f6ac813569c4e60`

## ARCHIVE CONTENTS

### ENTRY: fixcassandraservice.sh

- bytes: 662
- crc32: `c539584e`
- decoded_as: `utf-8`

````text
#!/bin/bash
################################
#   fixcassandraservice.sh
#
#   Fixes inability for systemd to control cassandra as a result of a vulnerability fix in systemd
#
################################
cat << EOF > /etc/systemd/system/cassandra.service
[Unit]
Description=Apache Cassandra
After=network.target

[Service]
PIDFile=/var/run/cassandra/cassandra.pid
User=cassandra
Group=cassandra
ExecStart=/usr/sbin/cassandra -f -p /var/run/cassandra/cassandra.pid
Restart=always
LimitNOFILE=100000
LimitMEMLOCK=infinity
LimitNPROC=32768

[Install]
WantedBy=multi-user.target
EOF

chkconfig --del cassandra
systemctl daemon-reload
systemctl enable cassandra


````

### ENTRY: install_cassandra4x_ol_rhel.sh

- bytes: 19694
- crc32: `8311d499`
- decoded_as: `utf-8`

````text
#!/bin/bash
CASSANDRA_VER=4.1.8  #Specify Cassandra version to install.

# Java Package Option
CASSANDRA_JAVA_PKG=java-11-openjdk  #Set package name or RPM file of Java

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
Usage: install_cassandra4x_ol_rhel.sh [option]

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
			echo "Installing Java 11 and Setting System Default"
			echo "============================================="
			$PKG_EXE install -q $CASSANDRA_JAVA_PKG
			alternatives --set java $(grep "java-11" /var/lib/alternatives/java | grep -o -P '(?<=@).*(?=@)')
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
	C8_CONF_FILES="cassandra.yaml jvm11-server.options jvm8-server.options logback.xml"
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
		sed -i "s/- seeds: \"127.0.0.1/- seeds: \"$IP_ADDRESS/g" $file.$twc_mod_ext
		sed -i "s/listen_address:.*/listen_address: $IP_ADDRESS/g" $file.$twc_mod_ext
		sed -i "s/# broadcast_rpc_address:.*/broadcast_rpc_address: $IP_ADDRESS/g" $file.$twc_mod_ext
		sed -i "s/broadcast_rpc_address:.*/broadcast_rpc_address: $IP_ADDRESS/g" $file.$twc_mod_ext
		sed -i "s/# commitlog_total_space:.*/commitlog_total_space: 8192MiB/g" $file.$twc_mod_ext
		sed -i "s/commitlog_total_space:.*/commitlog_total_space: 8192MiB/g" $file.$twc_mod_ext
		sed -i "s/^rpc_address:.*/rpc_address: 0.0.0.0/g" $file.$twc_mod_ext
		sed -i "s/commitlog_segment_size:.*/commitlog_segment_size: 192MiB/g" $file.$twc_mod_ext
		sed -i "s/read_request_timeout:.*/read_request_timeout: 1800000ms/g" $file.$twc_mod_ext
		sed -i "s/range_request_timeout:.*/range_request_timeout: 1800000ms/g" $file.$twc_mod_ext
		sed -i "s/^write_request_timeout:.*/write_request_timeout: 1800000ms/g" $file.$twc_mod_ext
		sed -i "s/cas_contention_timeout:.*/cas_contention_timeout: 1000ms/g" $file.$twc_mod_ext
		sed -i "s/truncate_request_timeout:.*/truncate_request_timeout: 1800000ms/g" $file.$twc_mod_ext
		sed -i "s/request_timeout:.*/request_timeout: 1800000ms/g" $file.$twc_mod_ext
		sed -i "s/batch_size_warn_threshold:.*/batch_size_warn_threshold: 3000KiB/g" $file.$twc_mod_ext
		sed -i "s/batch_size_fail_threshold:.*/batch_size_fail_threshold: 5000KiB/g" $file.$twc_mod_ext
		sed -i "s/# data_file_directories:.*/data_file_directories:/g" $file.$twc_mod_ext
		sed -i '/data_file_directories:.*/!b;n;c\ \ \ \ - '"$C8_DATA_FILE_DIR"'\/data' $file.$twc_mod_ext
		sed -i "s+# hints_directory:.*+hints_directory: $C8_DATA_FILE_DIR\/hints+g" $file.$twc_mod_ext
		sed -i "s+hints_directory:.*+hints_directory: $C8_DATA_FILE_DIR\/hints+g" $file.$twc_mod_ext
		sed -i "s+# commitlog_directory:.*+commitlog_directory: $C8_COMMITLOG_DIR\/commitlog+g" $file.$twc_mod_ext
		sed -i "s+commitlog_directory:.*+commitlog_directory: $C8_COMMITLOG_DIR\/commitlog+g" $file.$twc_mod_ext
		sed -i "s+# saved_caches_directory:.*+saved_caches_directory: $C8_DATA_FILE_DIR\/saved_caches+g" $file.$twc_mod_ext
		sed -i "s+saved_caches_directory:.*+saved_caches_directory: $C8_DATA_FILE_DIR\/saved_caches+g" $file.$twc_mod_ext
	elif [ "$file" == "jvm11-server.options" ]; then
		sed -i "s/-XX:+UseConcMarkSweepGC/#-XX:+UseConcMarkSweepGC/g" $file.$twc_mod_ext
		sed -i "s/-XX:+CMSParallelRemarkEnabled/#-XX:+CMSParallelRemarkEnabled/g" $file.$twc_mod_ext
		sed -i "s/-XX:SurvivorRatio=8/#-XX:SurvivorRatio=8/g" $file.$twc_mod_ext
		sed -i "s/-XX:MaxTenuringThreshold=1/#-XX:MaxTenuringThreshold=1/g" $file.$twc_mod_ext
		sed -i "s/-XX:CMSInitiatingOccupancyFraction=75/#-XX:CMSInitiatingOccupancyFraction=75/g" $file.$twc_mod_ext
		sed -i "s/-XX:+UseCMSInitiatingOccupancyOnly/#-XX:+UseCMSInitiatingOccupancyOnly/g" $file.$twc_mod_ext
		sed -i "s/-XX:CMSWaitDuration=10000/#-XX:CMSWaitDuration=10000/g" $file.$twc_mod_ext
		sed -i "s/-XX:+CMSParallelInitialMarkEnabled/#-XX:+CMSParallelInitialMarkEnabled/g" $file.$twc_mod_ext
		sed -i "s/-XX:+CMSEdenChunksRecordAlways/#-XX:+CMSEdenChunksRecordAlways/g" $file.$twc_mod_ext
		sed -i "s/-XX:+CMSClassUnloadingEnabled/#-XX:+CMSClassUnloadingEnabled/g" $file.$twc_mod_ext
		sed -i "s/#-XX:+UseG1GC/-XX:+UseG1GC/g" $file.$twc_mod_ext
		sed -i "s/#-XX:MaxGCPauseMillis=300/-XX:MaxGCPauseMillis=300/g" $file.$twc_mod_ext
		sed -i "s/#-XX:ParallelGCThreads=16/-XX:ParallelGCThreads=$NPROCS/g" $file.$twc_mod_ext
		sed -i "s/#-XX:ConcGCThreads=16/-XX:ConcGCThreads=$NPROCS/g" $file.$twc_mod_ext
	elif [ "$file" == "jvm8-server.options" ]; then
		sed -i "s/-XX:+UseParNewGC/#-XX:+UseParNewGC/g" $file.$twc_mod_ext
		sed -i "s/-XX:+UseConcMarkSweepGC/#-XX:+UseConcMarkSweepGC/g" $file.$twc_mod_ext
		sed -i "s/-XX:+CMSParallelRemarkEnabled/#-XX:+CMSParallelRemarkEnabled/g" $file.$twc_mod_ext
		sed -i "s/-XX:SurvivorRatio=8/#-XX:SurvivorRatio=8/g" $file.$twc_mod_ext
		sed -i "s/-XX:MaxTenuringThreshold=1/#-XX:MaxTenuringThreshold=1/g" $file.$twc_mod_ext
		sed -i "s/-XX:CMSInitiatingOccupancyFraction=75/#-XX:CMSInitiatingOccupancyFraction=75/g" $file.$twc_mod_ext
		sed -i "s/-XX:+UseCMSInitiatingOccupancyOnly/#-XX:+UseCMSInitiatingOccupancyOnly/g" $file.$twc_mod_ext
		sed -i "s/-XX:CMSWaitDuration=10000/#-XX:CMSWaitDuration=10000/g" $file.$twc_mod_ext
		sed -i "s/-XX:+CMSParallelInitialMarkEnabled/#-XX:+CMSParallelInitialMarkEnabled/g" $file.$twc_mod_ext
		sed -i "s/-XX:+CMSEdenChunksRecordAlways/#-XX:+CMSEdenChunksRecordAlways/g" $file.$twc_mod_ext
		sed -i "s/-XX:+CMSClassUnloadingEnabled/#-XX:+CMSClassUnloadingEnabled/g" $file.$twc_mod_ext
		sed -i "s/#-XX:+UseG1GC/-XX:+UseG1GC/g" $file.$twc_mod_ext
		sed -i "s/#-XX:MaxGCPauseMillis=300/-XX:MaxGCPauseMillis=300/g" $file.$twc_mod_ext
		sed -i "s/#-XX:ParallelGCThreads=16/-XX:ParallelGCThreads=$NPROCS/g" $file.$twc_mod_ext
		sed -i "s/#-XX:ConcGCThreads=16/-XX:ConcGCThreads=$NPROCS/g" $file.$twc_mod_ext
		sed -i "s/-XX:+PrintGCDetails/#-XX:+PrintGCDetails/g" $file.$twc_mod_ext
		sed -i "s/-XX:+PrintGCDateStamps/#-XX:+PrintGCDateStamps/g" $file.$twc_mod_ext
		sed -i "s/-XX:+PrintHeapAtGC/#-XX:+PrintHeapAtGC/g" $file.$twc_mod_ext
		sed -i "s/-XX:+PrintTenuringDistribution/#-XX:+PrintTenuringDistribution/g" $file.$twc_mod_ext
		sed -i "s/-XX:+PrintGCApplicationStoppedTime/#-XX:+PrintGCApplicationStoppedTime/g" $file.$twc_mod_ext
		sed -i "s/-XX:+PrintPromotionFailure/#-XX:+PrintPromotionFailure/g" $file.$twc_mod_ext
		sed -i "s/-XX:+UseGCLogFileRotation/#-XX:+UseGCLogFileRotation/g" $file.$twc_mod_ext
		sed -i "s/-XX:NumberOfGCLogFiles=10/#-XX:NumberOfGCLogFiles=10/g" $file.$twc_mod_ext
		sed -i "s/-XX:GCLogFileSize=10M/#-XX:GCLogFileSize=10M/g" $file.$twc_mod_ext
	elif [ "$file" == "logback.xml" ]; then
		sed -i '/ref="ASYNCDEBUGLOG"/c\\    <!-- <appender-ref ref="ASYNCDEBUGLOG" /> -->' $file.$twc_mod_ext
	fi
	#Copy modified file to Cassandra configuration path. Delete temporary file.
	\cp -fR ./$file.$twc_mod_ext $C8_CONF_PATH/$file && rm -f $file.$twc_mod_ext
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
PIDFile=/var/run/cassandra/cassandra.pid
User=cassandra
Group=cassandra
ExecStart=/usr/sbin/cassandra -f -p /var/run/cassandra/cassandra.pid
Restart=always
LimitNOFILE=100000
LimitMEMLOCK=infinity
LimitNPROC=32768

[Install]
WantedBy=multi-user.target
EOF
	sleep 5
	systemctl daemon-reload
	if type -p chkconfig > /dev/null; then systemctl enable cassandra; fi
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
	# Configure tunedisk config to run during boot. Replace previous rc.local config.
	TWC_TUNE_PATH=/etc/cassandra
	if ! [ -f $TWC_TUNE_PATH/tunedisk.sh ]; then
		mkdir -p $TWC_TUNE_PATH
		echo "  ... Creating disk, CPU, and memory tuning parameters in:"
		echo "        $TWC_TUNE_PATH/tunedisk.sh"

		cat << EOF > $TWC_TUNE_PATH/tunedisk.sh
#!/bin/bash
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

### ENTRY: install_flex_ol_rhel.sh

- bytes: 6196
- crc32: `500b889f`
- decoded_as: `utf-8`

````text
#!/bin/bash
FN_INSTALL_PATH=/opt/local/FNPLicenseServerManager
CAMEO_URL=https://d1g91r27pzl568.cloudfront.net/Cameo_daemon/FlexNet_11_19_6/linux64/cameo.zip
LMGRD_URL=https://d1oqhepk9od1tu.cloudfront.net/Flex_License_Server_Utilities/v11.19.6/linux64/lmgrd.zip
LMADMIN_URL=https://d1oqhepk9od1tu.cloudfront.net/Flex_License_Server_Utilities/v11.19.6/linux64/lmadmin-x64_linux-11_19_6_0.bin
CAMEO_FILE=$(basename $CAMEO_URL)
LMGRD_FILE=$(basename $LMGRD_URL)
LMADMIN_FILE=$(basename $LMADMIN_URL)
LMADMIN_VER=11.9.6
echo
if [ "$EUID" -ne 0 ];then
	echo "Please run as root or sudo."
	exit 1
fi
echo "============================="
echo "Installing Auxiliary Packages"
echo "============================="
yum install -y wget
yum install -y unzip
yum install -y java-11-openjdk
yum install -y ld-linux.so.2
bash -c "if [ ! -e /lib64/ld-lsb-x86-64.so.3 ]; then ln -s ld-linux-x86-64.so.2 /lib64/ld-lsb-x86-64.so.3; fi"

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
echo "============================================="
echo "Getting Linux 64-bit Cameo Daemon for FlexNet"
echo "============================================="
if [[ -f $CAMEO_FILE || -f ${CAMEO_FILE%.*} ]]; then 
    echo "Local copy of Cameo daemon found."
else
    wget $CAMEO_URL
fi
if [ -f $CAMEO_FILE ]; then unzip $CAMEO_FILE; fi
echo "=========================================="
echo "Getting Linux 64-bit lmgrd version $LMADMIN_VER"
echo "=========================================="
if [[ -f $LMGRD_FILE || -f ${LMGRD_FILE%.*} ]]; then 
    echo "Local copy of lmgrd found."
else
    wget $LMGRD_URL
fi
if [ -f $LMGRD_FILE ]; then unzip lmgrd.zip; fi
echo "======================================"
echo "Making flex log file named FlexLog.log"
echo "======================================"
touch FlexLog.log
chmod 664 FlexLog.log
echo "============================================"
echo "Getting Linux 64-bit lmadmin version $LMADMIN_VER"
echo "============================================"
if [ -f $LMADMIN_FILE ]; then
    echo "Local copy of $LMADMIN_FILE found."
else
    wget $LMADMIN_URL
fi
# Check if all required files exist in current path. Terminate if any of the files are not found.
file_list="$LMADMIN_FILE ${LMGRD_FILE%.*} ${CAMEO_FILE%.*}"
for file in $file_list
do
    if ! [ -f $file ]; then
        echo "$file not found. Installation terminated." && exit 1
    else
        chmod +x $file
    fi
done
echo "========================================="
echo "Executing lmadmin version 11.19 installer"
echo "IMPORTANT: Install into directory $FN_INSTALL_PATH"
echo ""
echo " Note:  Accept all defaults for script to work properly!!!"
echo ""
read -p -"Press any key to continue ...: " -n1 -s
echo "=========================================="
JAVA_TOOL_OPTIONS="-Djdk.util.zip.disableZip64ExtraFieldValidation=true" ./$LMADMIN_FILE -i console -DUSER_INSTALL_DIR=$FN_INSTALL_PATH
if [ -f "$FN_INSTALL_PATH/lmadmin" ]; then
    mkdir -p $FN_INSTALL_PATH/licenses/cameo/
    cp cameo $FN_INSTALL_PATH/cameo
    mv cameo $FN_INSTALL_PATH/licenses/cameo/cameo
    mv lmgrd $FN_INSTALL_PATH/lmgrd
    mv FlexLog.log $FN_INSTALL_PATH/FlexLog.log
    chown -R lmadmin:lmadmin $FN_INSTALL_PATH/
else
    echo "Installation terminated. Either installation failed or a different path was specified."
    echo "Please make sure FN_INSTALL_PATH in the script matches what is specified during installation."
    exit 1
fi

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
firewall-cmd --zone=$FWZONE --add-service=lmadmin --permanent
firewall-cmd --reload
#This firewalld service will overwrite previous configurations. Use examples below to remove custom settings.
#firewall-cmd --zone=public --remove-port=27000-27009/tcp --permanent &> /dev/null 
#firewall-cmd --zone=internal --remove-port=27000-27009/tcp --permanent &> /dev/null 
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
sleep 5
chown root:root /etc/systemd/system/lmadmin.service
chmod 755 /etc/systemd/system/lmadmin.service
systemctl daemon-reload
systemctl enable lmadmin.service
echo "Removing installanywhere temporary directory"
rm -fr $IATEMPDIR
echo "=========================================="
echo "  lmadmin service installation complete"
echo "  usage: systemctl start|stop lmadmin"
echo "  GUI: http://<servername>:8090"
echo "  username/password: admin/admin"
echo "=========================================="

````

### ENTRY: install_twc_mcs_ol_rhel.sh

- bytes: 5443
- crc32: `2b24a9a8`
- decoded_as: `utf-8`

````text
#!/bin/bash
NM_VERSION='2024x Refresh 3'

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
if [[ $INSTALLER =~ "magic" ]]; then
	PRODUCT="Magic Collaboration Studio ${NM_VERSION}"
elif [[ $INSTALLER =~ "twcloud" ]]; then
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
#echo "Creating twcloud group and user"
#getent group twcloud >/dev/null || groupadd -r twcloud
#getent passwd twcloud >/dev/null || useradd -d /home/twcloud -g twcloud -m -r twcloud
echo "Creating temporary directory for install anywhere"
IATEMPDIR=$(pwd)/_tmp
export IATEMPDIR
mkdir $IATEMPDIR
echo ""
echo "IMPORTANT: "
echo "           When prompted for user to run service, use twcloud"
echo "           When prompted for Java Home location, use Java 17 location, e.g., /etc/alternatives/jre_17"
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

# Archive initial set of configuration files and self-signed keystore from installation
TWC_BACKUP_UTIL=${TWCLOUD_HOME%/*}/Utilities/AdminTools/backup-twc-configs.sh
if [ -f $TWC_BACKUP_UTIL ]; then $TWC_BACKUP_UTIL; fi

echo "Post-install configuration completed."
echo "Additional shortcuts and utilities available at:"
echo "   ${TWCLOUD_HOME%/*}/Utilities/AdminTools"
echo
````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "239798886",
  "type": "attachment",
  "status": "current",
  "title": "TWC_MCS_install_scripts_2024xRefresh3.zip",
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
    "when": "2025-10-21T12:47:55.474+02:00",
    "message": "",
    "number": 2,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/239798886/version/2"
    },
    "_expandable": {
      "content": "/rest/api/content/239798886"
    }
  },
  "position": -1,
  "container": {
    "id": "227173072",
    "type": "page",
    "status": "current",
    "title": "Installation on Linux",
    "position": 0,
    "extensions": {
      "position": 0
    },
    "_links": {
      "webui": "/spaces/MCS2024xR3/pages/227173072/Installation+on+Linux",
      "edit": "/pages/resumedraft.action?draftId=227173072",
      "tinyui": "/x/0GKKDQ",
      "self": "https://docs.nomagic.com/rest/api/content/227173072"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS2024xR3",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/227173072/child",
      "restrictions": "/rest/api/content/227173072/restriction/byOperation",
      "history": "/rest/api/content/227173072/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/227173072/descendant",
      "space": "/rest/api/space/MCS2024xR3",
      "relevantViewRestrictions": "/rest/api/content/227173072/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/zip"
  },
  "extensions": {
    "mediaType": "application/zip",
    "fileSize": 11366,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/227173072/TWC_MCS_install_scripts_2024xRefresh3.zip?version=2&modificationDate=1761043675474&api=v2",
    "webui": "/spaces/MCS2024xR3/pages/227173072/Installation+on+Linux?preview=%2F227173072%2F239798886%2FTWC_MCS_install_scripts_2024xRefresh3.zip",
    "self": "https://docs.nomagic.com/rest/api/content/239798886"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/239798886/child",
    "restrictions": "/rest/api/content/239798886/restriction/byOperation",
    "history": "/rest/api/content/239798886/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/239798886/descendant",
    "space": "/rest/api/space/MCS2024xR3",
    "relevantViewRestrictions": "/rest/api/content/239798886/restriction/relevantViewRestrictions"
  }
}
````
