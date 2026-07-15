# NOMAGIC ATTACHMENT: TWC_MCS_install_scripts_2024xRefresh1.zip

- attachment_id: `247063418`
- space_key: `MCS`
- parent_page_id: `247063416`
- parent_page_title: (2026x) Installation on Linux
- media_type: `application/zip`
- reported_bytes: 9334
- download_url: https://docs.nomagic.com/download/attachments/247063416/TWC_MCS_install_scripts_2024xRefresh1.zip?version=1&modificationDate=1755163516557&api=v2
- payload_kind: `archive-expanded`
- downloaded_sha256: `b5f6dbc2a96b6ea2b6aa5909257505efe75786601263f178993e4e53a8c15f52`

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

- bytes: 12728
- crc32: `e9dffdd4`
- decoded_as: `utf-8`

````text
#!/bin/bash
CASSANDRA_VER=4.1.4  #Specify Cassandra version to install.

# Package Downloads
CASSANDRA_JAVA_PKG=java-11-openjdk  #Default Java required by Cassandra
CASSANDRA_JAVA17_PKG=java-17-openjdk  #Installs tzdata needed by Cassandra 4.1

# Configure Cassandra package download URLs based on version specified.
C8_RPM_URL="https://apache.jfrog.io/artifactory/cassandra-rpm"
C8_PKG_NAME="cassandra-$CASSANDRA_VER-1.noarch.rpm"
C8_TOOLS_NAME="cassandra-tools-$CASSANDRA_VER-1.noarch.rpm"
C8_VERX="$(echo $CASSANDRA_VER | cut -c 1,3)x"

# If Cassandra packages exist locally, then installation will install from local source.
if [ -f $C8_PKG_NAME ]; then
	CASSANDRA_PKG_URL=$C8_PKG_NAME
	echo "Cassandra will be installed from local $CASSANDRA_PKG_URL"
else
	CASSANDRA_PKG_URL=$C8_RPM_URL/$C8_VERX/$C8_PKG_NAME
	echo "Cassandra will retrieved from: $CASSANDRA_PKG_URL"
fi
if [ -f $C8_TOOLS_NAME ]; then
	CASSANDRA_TOOLS_URL=$C8_TOOLS_NAME
	echo "Cassandra will be installed from local $CASSANDRA_TOOLS_URL"
else
	CASSANDRA_TOOLS_URL=$C8_RPM_URL/$C8_VERX/$C8_TOOLS_NAME
	echo "Cassandra will retrieved from: $CASSANDRA_TOOLS_URL"
fi
echo
if [ "$EUID" -ne 0 ];then
	echo "Please run as root or sudo."
	exit 1
fi
#Check if current installation exists.
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

echo "========================================================"
echo "Installing Apache Cassandra $CASSANDRA_VER for $OS $OS_V"
echo "========================================================"
echo "Removing Datastax Community Edition"
$PKG_EXE remove datastax-agent  &> /dev/null
$PKG_EXE remove opscenter  &> /dev/null
rm -f /etc/yum.repos.d/datastax.repo  &> /dev/null
echo "Removing old Cassandra repos"
rm -f /etc/yum.repos.d/cassandra.repo &> /dev/null

#Install Java for Cassandra and set installed version as default system Java.
$PKG_EXE install $CASSANDRA_JAVA_PKG
echo "========================================"
echo "Setting Java 11 as default on the system"
echo "========================================"
alternatives --set java $(grep "java-11" /var/lib/alternatives/java | grep -o -P '(?<=@).*(?=@)')

#Install Cassandra RPM packages, verify installation.
$PKG_EXE --nogpgcheck install $CASSANDRA_PKG_URL
$PKG_EXE --nogpgcheck install $CASSANDRA_TOOLS_URL
if type -p cassandra > /dev/null; then
	echo "Cassandra $(cassandra -v) base installation verified."
else
	echo && echo "Installation was not successful. Please look for issues in output above."
	exit 1
fi

#Install Java 17
$PKG_EXE install $CASSANDRA_JAVA17_PKG

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
    <port port="7001" protocol="tcp"/>
    <port port="9042" protocol="tcp"/>
    <port port="9142" protocol="tcp"/>
</service>
EOF
sleep 5
firewall-cmd --zone=$FWZONE --add-service=cassandra --permanent
firewall-cmd --reload
#This firewalld service will overwrite previous configurations. Use example below to remove custom settings.
#firewall-cmd --zone=$FWZONE --remove-port=9160/tcp --permanent  &> /dev/null
else
echo "======================="
echo "Firewall is not running - skipping firewall configuration"
echo "======================="
fi
echo "====================================================="
echo "Changing ownership of data and commit log directories"
echo "====================================================="
mkdir /data &> /dev/null
mkdir /logs &> /dev/null
chown cassandra:cassandra /data &> /dev/null
chown cassandra:cassandra /logs &> /dev/null
echo "====================================================="
echo "Making configuration file changes"
echo "====================================================="
IP_ADDRESS=$(ip route get 1 | sed 's/^.*src \([^ ]*\).*$/\1/;q')
if [ -z "$IP_ADDRESS" ]; then IP_ADDRESS=localhost; fi   # Revert to localhost if IP address is not found.
cp /etc/cassandra/default.conf/cassandra.yaml /etc/cassandra/default.conf/cassandra.yaml.backup
cp /etc/cassandra/default.conf/cassandra.yaml ./cassandra.yaml.template
sed -i "s/- seeds: \"127.0.0.1/- seeds: \"$IP_ADDRESS/g" cassandra.yaml.template
sed -i "s/listen_address:.*/listen_address: $IP_ADDRESS/g" cassandra.yaml.template
sed -i "s/# broadcast_rpc_address:.*/broadcast_rpc_address: $IP_ADDRESS/g" cassandra.yaml.template
sed -i "s/broadcast_rpc_address:.*/broadcast_rpc_address: $IP_ADDRESS/g" cassandra.yaml.template
sed -i "s/# commitlog_total_space:.*/commitlog_total_space: 8192MiB/g" cassandra.yaml.template
sed -i "s/commitlog_total_space:.*/commitlog_total_space: 8192MiB/g" cassandra.yaml.template
sed -i "s/^rpc_address:.*/rpc_address: 0.0.0.0/g" cassandra.yaml.template
sed -i "s/commitlog_segment_size:.*/commitlog_segment_size: 192MiB/g" cassandra.yaml.template
sed -i "s/read_request_timeout:.*/read_request_timeout: 1800000ms/g" cassandra.yaml.template
sed -i "s/range_request_timeout:.*/range_request_timeout: 1800000ms/g" cassandra.yaml.template
sed -i "s/^write_request_timeout:.*/write_request_timeout: 1800000ms/g" cassandra.yaml.template
sed -i "s/cas_contention_timeout:.*/cas_contention_timeout: 1000ms/g" cassandra.yaml.template
sed -i "s/truncate_request_timeout:.*/truncate_request_timeout: 1800000ms/g" cassandra.yaml.template
sed -i "s/request_timeout:.*/request_timeout: 1800000ms/g" cassandra.yaml.template
sed -i "s/batch_size_warn_threshold:.*/batch_size_warn_threshold: 3000KiB/g" cassandra.yaml.template
sed -i "s/batch_size_fail_threshold:.*/batch_size_fail_threshold: 5000KiB/g" cassandra.yaml.template
sed -i '/data_file_directories:.*/!b;n;c\ \ \ \ - \/data\/data' cassandra.yaml.template
sed -i "s/hints_directory:.*/hints_directory: \/data\/hints/g" cassandra.yaml.template
sed -i "s/commitlog_directory:.*/commitlog_directory: \/logs\/commitlog/g" cassandra.yaml.template
sed -i "s/saved_caches_directory:.*/saved_caches_directory: \/data\/saved_caches/g" cassandra.yaml.template
cp -fR ./cassandra.yaml.template /etc/cassandra/default.conf/cassandra.yaml
#Obtain server CPU count
NPROCS=$(nproc)
#Modify jvm11-server.options for Cassandra 4
cp /etc/cassandra/default.conf/jvm11-server.options /etc/cassandra/default.conf/jvm11-server.options.backup
cp /etc/cassandra/default.conf/jvm11-server.options ./jvm11-server.options.template
sed -i "s/-XX:+UseConcMarkSweepGC/#-XX:+UseConcMarkSweepGC/g" jvm11-server.options.template
sed -i "s/-XX:+CMSParallelRemarkEnabled/#-XX:+CMSParallelRemarkEnabled/g" jvm11-server.options.template
sed -i "s/-XX:SurvivorRatio=8/#-XX:SurvivorRatio=8/g" jvm11-server.options.template
sed -i "s/-XX:MaxTenuringThreshold=1/#-XX:MaxTenuringThreshold=1/g" jvm11-server.options.template
sed -i "s/-XX:CMSInitiatingOccupancyFraction=75/#-XX:CMSInitiatingOccupancyFraction=75/g" jvm11-server.options.template
sed -i "s/-XX:+UseCMSInitiatingOccupancyOnly/#-XX:+UseCMSInitiatingOccupancyOnly/g" jvm11-server.options.template
sed -i "s/-XX:CMSWaitDuration=10000/#-XX:CMSWaitDuration=10000/g" jvm11-server.options.template
sed -i "s/-XX:+CMSParallelInitialMarkEnabled/#-XX:+CMSParallelInitialMarkEnabled/g" jvm11-server.options.template
sed -i "s/-XX:+CMSEdenChunksRecordAlways/#-XX:+CMSEdenChunksRecordAlways/g" jvm11-server.options.template
sed -i "s/-XX:+CMSClassUnloadingEnabled/#-XX:+CMSClassUnloadingEnabled/g" jvm11-server.options.template
sed -i "s/#-XX:+UseG1GC/-XX:+UseG1GC/g" jvm11-server.options.template
sed -i "s/#-XX:MaxGCPauseMillis=300/-XX:MaxGCPauseMillis=300/g" jvm11-server.options.template
sed -i "s/#-XX:ParallelGCThreads=16/-XX:ParallelGCThreads=$NPROCS/g" jvm11-server.options.template
sed -i "s/#-XX:ConcGCThreads=16/-XX:ConcGCThreads=$NPROCS/g" jvm11-server.options.template
cp -fR ./jvm11-server.options.template /etc/cassandra/default.conf/jvm11-server.options
#Modify jvm8-server.options for Cassandra 4
cp /etc/cassandra/default.conf/jvm8-server.options /etc/cassandra/default.conf/jvm8-server.options.backup
cp /etc/cassandra/default.conf/jvm8-server.options ./jvm8-server.options.template
sed -i "s/-XX:+UseParNewGC/#-XX:+UseParNewGC/g" jvm8-server.options.template
sed -i "s/-XX:+UseConcMarkSweepGC/#-XX:+UseConcMarkSweepGC/g" jvm8-server.options.template
sed -i "s/-XX:+CMSParallelRemarkEnabled/#-XX:+CMSParallelRemarkEnabled/g" jvm8-server.options.template
sed -i "s/-XX:SurvivorRatio=8/#-XX:SurvivorRatio=8/g" jvm8-server.options.template
sed -i "s/-XX:MaxTenuringThreshold=1/#-XX:MaxTenuringThreshold=1/g" jvm8-server.options.template
sed -i "s/-XX:CMSInitiatingOccupancyFraction=75/#-XX:CMSInitiatingOccupancyFraction=75/g" jvm8-server.options.template
sed -i "s/-XX:+UseCMSInitiatingOccupancyOnly/#-XX:+UseCMSInitiatingOccupancyOnly/g" jvm8-server.options.template
sed -i "s/-XX:CMSWaitDuration=10000/#-XX:CMSWaitDuration=10000/g" jvm8-server.options.template
sed -i "s/-XX:+CMSParallelInitialMarkEnabled/#-XX:+CMSParallelInitialMarkEnabled/g" jvm8-server.options.template
sed -i "s/-XX:+CMSEdenChunksRecordAlways/#-XX:+CMSEdenChunksRecordAlways/g" jvm8-server.options.template
sed -i "s/-XX:+CMSClassUnloadingEnabled/#-XX:+CMSClassUnloadingEnabled/g" jvm8-server.options.template
sed -i "s/#-XX:+UseG1GC/-XX:+UseG1GC/g" jvm8-server.options.template
sed -i "s/#-XX:MaxGCPauseMillis=300/-XX:MaxGCPauseMillis=300/g" jvm8-server.options.template
sed -i "s/#-XX:ParallelGCThreads=16/-XX:ParallelGCThreads=$NPROCS/g" jvm8-server.options.template
sed -i "s/#-XX:ConcGCThreads=16/-XX:ConcGCThreads=$NPROCS/g" jvm8-server.options.template
sed -i "s/-XX:+PrintGCDetails/#-XX:+PrintGCDetails/g" jvm8-server.options.template
sed -i "s/-XX:+PrintGCDateStamps/#-XX:+PrintGCDateStamps/g" jvm8-server.options.template
sed -i "s/-XX:+PrintHeapAtGC/#-XX:+PrintHeapAtGC/g" jvm8-server.options.template
sed -i "s/-XX:+PrintTenuringDistribution/#-XX:+PrintTenuringDistribution/g" jvm8-server.options.template
sed -i "s/-XX:+PrintGCApplicationStoppedTime/#-XX:+PrintGCApplicationStoppedTime/g" jvm8-server.options.template
sed -i "s/-XX:+PrintPromotionFailure/#-XX:+PrintPromotionFailure/g" jvm8-server.options.template
sed -i "s/-XX:+UseGCLogFileRotation/#-XX:+UseGCLogFileRotation/g" jvm8-server.options.template
sed -i "s/-XX:NumberOfGCLogFiles=10/#-XX:NumberOfGCLogFiles=10/g" jvm8-server.options.template
sed -i "s/-XX:GCLogFileSize=10M/#-XX:GCLogFileSize=10M/g" jvm8-server.options.template
cp -fR ./jvm8-server.options.template /etc/cassandra/default.conf/jvm8-server.options
#Modify logback.xml
cp /etc/cassandra/default.conf/logback.xml /etc/cassandra/default.conf/logback.xml.backup
cp /etc/cassandra/default.conf/logback.xml ./logback.xml.template
sed -i '/ref="ASYNCDEBUGLOG"/c\\    <!-- <appender-ref ref="ASYNCDEBUGLOG" /> -->' logback.xml.template
cp -fR logback.xml.template /etc/cassandra/default.conf/logback.xml

# Create service file for Cassandra and enable
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
chkconfig --del cassandra
systemctl daemon-reload
systemctl enable cassandra
echo
echo "Cassandra installation completed."
echo
# Check if /tmp is mounted with noexec
if [[ $(findmnt /tmp | grep noexec) ]]; then
    echo "/tmp is mounted with noexec. Cassandra will not start. See documentation for more details."
fi
if [[ $(findmnt /dev/shm | grep noexec) ]]; then
    echo "/dev/shm is mounted with noexec. Cassandra will not start. Remount with exec."
fi
echo


````

### ENTRY: install_flex_ol_rhel.sh

- bytes: 5754
- crc32: `78d97bbe`
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
echo "========================================="
echo "Getting Linux 64-bit IPv6 version 11.19.6"
echo "========================================="
if [ -f $CAMEO_FILE ]; then 
    echo "Local copy of $CAMEO_FILE found."
else
    wget $CAMEO_URL
fi
unzip cameo.zip
chmod +x cameo
echo "=========================================="
echo "Getting Linux 64-bit lmgrd version 11.19.6"
echo "=========================================="
if [ -f $LMGRD_FILE ]; then 
    echo "Local copy of $LMGRD_FILE found."
else
    wget $LMGRD_URL
fi
unzip lmgrd.zip
chmod +x lmgrd
echo "======================================"
echo "Making flex log file named FlexLog.log"
echo "======================================"
touch FlexLog.log
chmod 664 FlexLog.log
echo "============================================"
echo "Getting Linux 64-bit lmadmin version 11.19.6"
echo "============================================"
if [ -f $LMADMIN_FILE ]; then
    echo "Local copy of $LMADMIN_FILE found."
else
    wget $LMADMIN_URL
fi
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
sleep 5
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

- bytes: 7563
- crc32: `8b30be8d`
- decoded_as: `utf-8`

````text
#!/bin/bash
NM_VERSION='2024x Refresh 1'
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
	exit 1
fi

echo "======================================================"
echo "Installing $PRODUCT"
echo "======================================================"

echo "Installing unzip"
$PKG_EXE install unzip
echo "Installing fonts for Document Exporter"
$PKG_EXE install dejavu-serif-fonts
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
sleep 5
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
sysctl -p
else
echo "Skipping post-install performance tuning. Already configured."
fi

# Configure tunedisk config to run during boot. Only configures if TWCLOUD_HOME is found.
TWC_ENV_PATH=/etc/twcloud/twcloud-env
if [ -f $TWC_ENV_PATH ]; then
	source $TWC_ENV_PATH
	TWC_TUNE_PATH=$TWCLOUD_HOME/scripts/linux
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
# Check if rc.local was set to run tunedisk.sh from previous installation.
# Replace tunedisk.sh path if found. Ignore if tunedisk was set previously.
if ( grep -q "/home/twcloud/tunedisk.sh" /etc/rc.local ); then
	sed -i "s+/home/twcloud/tunedisk.sh.*+$TWC_TUNE_PATH/tunedisk.sh+g" /etc/rc.local
fi
if ! ( grep -q "tuning for TeamworkCloud" /etc/rc.local ); then
cat <<EOF >> /etc/rc.local
 
#  Perform additional tuning for TeamworkCloud
$TWC_TUNE_PATH/tunedisk.sh
EOF
chmod +x /etc/rc.d/rc.local
fi

echo "  ... Applying tuning changes - there is a 30 second delay before execution"
$TWC_TUNE_PATH/tunedisk.sh > $TWC_TUNE_PATH/tunedisk.log
fi  # TWC_ENV_PATH check close

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
  "id": "247063418",
  "type": "attachment",
  "status": "current",
  "title": "TWC_MCS_install_scripts_2024xRefresh1.zip",
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
    "when": "2025-08-14T11:25:16.557+02:00",
    "message": "",
    "number": 1,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/247063418/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/247063418"
    }
  },
  "position": -1,
  "container": {
    "id": "247063416",
    "type": "page",
    "status": "current",
    "title": "(2026x) Installation on Linux",
    "position": 1,
    "extensions": {
      "position": 1
    },
    "_links": {
      "webui": "/spaces/MCS/pages/247063416/2026x+Installation+on+Linux",
      "edit": "/pages/resumedraft.action?draftId=247063416",
      "tinyui": "/x/eOO5Dg",
      "self": "https://docs.nomagic.com/rest/api/content/247063416"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/247063416/child",
      "restrictions": "/rest/api/content/247063416/restriction/byOperation",
      "history": "/rest/api/content/247063416/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/247063416/descendant",
      "space": "/rest/api/space/MCS",
      "relevantViewRestrictions": "/rest/api/content/247063416/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/zip"
  },
  "extensions": {
    "mediaType": "application/zip",
    "fileSize": 9334,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/247063416/TWC_MCS_install_scripts_2024xRefresh1.zip?version=1&modificationDate=1755163516557&api=v2",
    "webui": "/spaces/MCS/pages/247063416/2026x+Installation+on+Linux?preview=%2F247063416%2F247063418%2FTWC_MCS_install_scripts_2024xRefresh1.zip",
    "self": "https://docs.nomagic.com/rest/api/content/247063418"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/247063418/child",
    "restrictions": "/rest/api/content/247063418/restriction/byOperation",
    "history": "/rest/api/content/247063418/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/247063418/descendant",
    "space": "/rest/api/space/MCS",
    "relevantViewRestrictions": "/rest/api/content/247063418/restriction/relevantViewRestrictions"
  }
}
````
