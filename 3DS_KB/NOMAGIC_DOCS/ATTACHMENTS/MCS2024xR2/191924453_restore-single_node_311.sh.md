# NOMAGIC ATTACHMENT: restore-single_node_311.sh

- attachment_id: `191924453`
- space_key: `MCS2024xR2`
- parent_page_id: `191924449`
- parent_page_title: Backup and restore data procedures
- media_type: `application/x-sh`
- reported_bytes: 9696
- download_url: https://docs.nomagic.com/download/attachments/191924449/restore-single_node_311.sh?version=1&modificationDate=1728049802368&api=v2
- payload_kind: `text-exact`
- downloaded_sha256: `e881e36551d374861731e5a7fa97bd771c8e0002321e07c64f50c177bc63f0fd`

## EXACT ATTACHMENT SOURCE

````text
#!/bin/bash

die() {
  local _ret=$1
  test -n "$_ret" || _ret=1
  test "$_PRINT_HELP" = yes && print_help >&2
  echo "$1" >&2
  exit ${_ret}
}

begins_with_short_option() {
  local first_option all_short_options
  all_short_options='h'
  first_option="${1:0:1}"
  test "$all_short_options" = "${all_short_options/$first_option/}" && return 1 || return 0
}

# THE DEFAULTS INITIALIZATION - OPTIONALS
COMMITLOG_DIR=$commitlog_path
DATABASE_DIR=$cassandra_database
CASSANDRA_PATH=$cassandra
CASSANDRA_AS_SERVICE=$service
RECOVERY_FILE=$rf

_arg_dir=$DATABASE_DIR
_arg_commitlog=$COMMITLOG_DIR
_arg_rf=$RECOVERY_FILE
_arg_cassandra=$CASSANDRA_PATH

print_help() {
  printf '%s\n' ""
  printf 'Usage: %s [--dir <arg>] [--commitlog <arg>] [--rf <arg>] [--cassandra <arg>] [-h|--help]\n' "$0"
  printf '\t%s\n' "--dir: cassandra database path (default: DATABASE_DIR)"
  printf '\t%s\n' "--commitlog: commitlog path (default: COMMITLOG_DIR)"
  printf '\t%s\n' "--rf: full path to snapshot archive (default: RECOVERY_FILE)"
  printf '\t%s\n' "--cassandra: cassandra installation path when cassandra is not executed as a service (default: CASSANDRA_PATH)"
  printf '\t%s\n' "-h,--help: Prints help"
}

parse_commandline() {
  while test $# -gt 0; do
    _key="$1"
    case "$_key" in
    --dir)
      test $# -lt 2 && die "Missing value for the optional argument '$_key'." 1
      _arg_dir="$2"
      DATABASE_DIR=$_arg_dir
      shift
      ;;
    --dir=*)
      _arg_dir="${_key##--dir=}"
      DATABASE_DIR=$_arg_dir
      ;;
    --commitlog)
      test $# -lt 2 && die "Missing value for the optional argument '$_key'." 1
      _arg_commitlog="$2"
      COMMITLOG_DIR=$_arg_commitlog
      shift
      ;;
    --commitlog=*)
      _arg_commitlog="${_key##--commitlog=}"
      COMMITLOG_DIR=$_arg_commitlog
      ;;
    --rf)
      test $# -lt 2 && die "Missing value for the optional argument '$_key'." 1
      _arg_rf="$2"
      RECOVERY_FILE=$_arg_rf
      shift
      ;;
    --rf=*)
      _arg_rf="${_key##--rf=}"
      RECOVERY_FILE=$_arg_rf
      ;;
    --cassandra)
      test $# -lt 2 && die "Missing value for the optional argument '$_key'." 1
      _arg_cassandra="$2"
      CASSANDRA_PATH=$_arg_cassandra
      shift
      ;;
    --cassandra=*)
      _arg_cassandra="${_key##--cassandra=}"
      CASSANDRA_PATH=$_arg_cassandra
      ;;
    -h | --help)
      print_help
      exit 0
      ;;
    -h*)
      print_help
      exit 0
      ;;
    *)
      _PRINT_HELP=yes die "FATAL ERROR: Got an unexpected argument '$1'" 1
      ;;
    esac
    shift
  done
}

parse_commandline "$@"

osname=$(uname -o)

wait_s=30

user_name=cassandra
password=cassandra

init() {
  init_database_dir
  init_commitlog_dir
  init_cassandra_home
  init_recovery_file
}

init_database_dir() {
  if [ ! -d "$DATABASE_DIR" ]; then
    request_db_dir
  fi
}

init_commitlog_dir() {
  if [ ! -d "$COMMITLOG_DIR" ]; then
    request_commitlog_dir
  fi
}

init_recovery_file() {
  if [ ! -f "$RECOVERY_FILE" ]; then
    request_recovery_file
  fi
}

init_cassandra_home() {
  if [ "$CASSANDRA_AS_SERVICE" = false ]; then
    if [ ! -d "$CASSANDRA_PATH" ]; then
      request_cassandra_home
    fi
  fi
}

remove_old_data() {
  echo "Removing current data *** DESTRUCTIVE ***"
  (
    cd "$DATABASE_DIR/data/"
    #remove the db files from keyspaces
    find . -name "*.db" -delete
    #remove subfolders under snapshots
    find . -type d -path "*/snapshots/*" | xargs rm -fr
    #find . -type f ! -path "*/snapshots/*" -exec rm -f {} \;
    check_for_errors
    #find . -type d ! -path "*/snapshots/*" -iname "*_Idx" -exec rm -rf {} \;
    #check_for_errors
  )
}

stop_cassandra() {
  if [ "$CASSANDRA_AS_SERVICE" = '' ] || [ "$CASSANDRA_AS_SERVICE" = true ]; then
    echo "Stoping Cassandra service"
    if [ "$osname" = "Cygwin" ]; then
      net stop cassandra
    else
      systemctl stop cassandra
      echo "Waiting $wait_s seconds for Cassandra to stop"
      sleep $wait_s
      nohup ps aux | grep Cassandra | awk {'print $2'} | xargs kill >/dev/null 2>&1 &
      check_for_errors
    fi
  else
    echo "Stoping Cassandra process"
    if [ "$osname" = "Cygwin" ]; then
      wmic PROCESS where "CommandLine like '%cassandra%'" Call Terminate
    else
      nohup ps aux | grep Cassandra | awk {'print $2'} | xargs kill >/dev/null 2>&1 &
      check_for_errors
    fi
  fi
  sleep 5
}

start_cassandra() {
  if [ "$CASSANDRA_AS_SERVICE" = '' ] || [ "$CASSANDRA_AS_SERVICE" = true ]; then
    echo "Starting Cassandra service"
    if [ "$osname" = "Cygwin" ]; then
      net start cassandra
    else
      systemctl start cassandra
    fi
  else
    if [ -d $CASSANDRA_PATH ]; then
      echo "Starting Cassandra process"
      if [ "$osname" = "Cygwin" ]; then
        (
          cd "$CASSANDRA_PATH/bin/"
          cassandra -f &
          disown
          check_for_errors
        )
      else
        (
          cd "$CASSANDRA_PATH/bin/"
          ./cassandra
          check_for_errors
        )
      fi
    else
      echo "Cassandra home set to: $CASSANDRA_PATH"
      echo "Cassandra home is not set correctly. Example usage: $ cassandra=/opt/cassandra-2.2.5 ./restore_single_node.sh"
      echo "Or you can start Cassandra manually"
    fi
  fi
  echo "Waiting $wait_s seconds for Cassandra"
  sleep $wait_s
}

restore_data() {
  echo "Restoring snapshot data"
  (
    cd "$DATABASE_DIR/data/"
    for keyspace in $(find . -mindepth 2 -maxdepth 2 -type d); do
      echo "Restoring: $keyspace"
      for snapshot in $(find $keyspace -mindepth 2 -maxdepth 2 -type d | sort -nr | head -1); do
        echo "Copying contents from: $snapshot to: $keyspace"
        for ext in db json txt crc32 cql
        do
          file=$snapshot/*.$ext
          cp $file $keyspace 2>/dev/null || :
        done
        # check_for_errors
      done
    done
  )

  if [ "$CASSANDRA_AS_SERVICE" = '' ] || [ "$CASSANDRA_AS_SERVICE" = true ]; then
    (
      cd "$DATABASE_DIR"
      if [ ! "$osname" = "Cygwin" ]; then
        chown -R cassandra:cassandra data/
      else
        chown -R Administrators:SYSTEM data/
      fi
    )
  fi
}

clear_commitlog() {
  (
    cd "$COMMITLOG_DIR"
    find . -name "*.log" -delete
  )
}

commitlog_not_found() {
  echo "Commitlog dir not cleared, please clear it manually"
}

commitlog_found() {
  echo "Removing old commit logs"
}

repair_keyspaces_linux() {
  NODETOOL=nodetool

  for keyspace in $(nodetool tablestats | grep "Keyspace :" | awk -F ":" '{print $2}'); do
    echo $keyspace
    $NODETOOL -h localhost -u $user_name -pw $password -p 7199 repair $keyspace
  done
  check_for_errors
}

repair_keyspaces_cygwin() {
  echo "Repairing Cassandra keyspaces"
  NODETOOL=nodetool.bat

  for keyspace in $(nodetool tablestats | grep "Keyspace :" | awk -F ":" '{print $2}'); do
    echo $keyspace
    $NODETOOL -h localhost -u $user_name -pw $password -p 7199 repair $keyspace
  done
  check_for_errors
}

remove_recovery() {
  echo "Removing old snapshots"
  (
    cd "$DATABASE_DIR/data"
    nohup find . -path "*/snapshots/*" -exec rm -rf {} \; >/dev/null 2>&1 &
    check_for_errors
  )
}

request_recovery_file() {
  need_file=true
  while $need_file; do
    read -p "Please enter full backup file path. I.e. /home/user/backups/cassandra_backup_2016.07.29.12.23.24.tar: " RECOVERY_FILE
    if [ ! -f "$RECOVERY_FILE" ]; then
      echo "No backup file found $RECOVERY_FILE"
      echo "Wrong file entered."
    else
      need_file=false
    fi
  done
}

request_cassandra_home() {
  need_dir=true
  while $need_dir; do
    read -p "Please enter Cassandra home directory. I.e. /opt/cassandra-2.2.5: " CASSANDRA_PATH
    if [ ! -d "$CASSANDRA_PATH/bin/" ]; then
      echo "No directory $CASSANDRA_PATH/bin/"
      echo "Wrong directory entered."
    else
      need_dir=false
    fi
  done
}

request_commitlog_dir() {
  need_dir=true
  while $need_dir; do
    read -p "Please enter Cassandra commitlog directory. I.e. /var/lib/cassandra/commitlog: " COMMITLOG_DIR
    if [ ! -d "$COMMITLOG_DIR" ]; then
      echo "No directory $COMMITLOG_DIR"
      echo "Wrong directory entered."
    else
      need_dir=false
    fi
  done
}

request_db_dir() {
  need_dir=true
  while $need_dir; do
    read -p "Please enter Cassandra database directory. I.e. /var/lib/cassandra: " DATABASE_DIR
    if [ ! -d "$DATABASE_DIR/data/" ]; then
      echo "No directory $DATABASE_DIR/data/"
      echo "Wrong directory entered."
    else
      need_dir=false
    fi
  done
}

recover_snapshot_from_backup() {
  echo "Restoring snapshot from backup"
  (
    cd "$DATABASE_DIR/data"
    remove_old_data
    clear_commitlog
    tar --same-owner -C "$DATABASE_DIR/data/" -xvf "$RECOVERY_FILE"
    check_for_errors
    echo "Finished Restoring snapshot from backup"
  )
}

check_for_errors() {
  rc=$?
  if [[ $rc != 0 ]]; then
    echo "Error $rc"
    exit $rc
  fi
}

repair_keyspaces() {
  if [ "$osname" = "Cygwin" ]; then
    repair_keyspaces_cygwin
  else
    repair_keyspaces_linux
  fi
}

fail() {
  echo "Database recovery failed, please check console output for more details"
}

finish() {
  echo "Finished snapshot recovery"
}

{
  init && stop_cassandra && recover_snapshot_from_backup && restore_data && remove_recovery && start_cassandra && repair_keyspaces && finish
} || {
  fail
}

````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "191924453",
  "type": "attachment",
  "status": "current",
  "title": "restore-single_node_311.sh",
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
    "when": "2024-10-04T15:50:02.368+02:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/191924453/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/191924453"
    }
  },
  "position": -1,
  "container": {
    "id": "191924449",
    "type": "page",
    "status": "current",
    "title": "Backup and restore data procedures",
    "position": 0,
    "extensions": {
      "position": 0
    },
    "_links": {
      "webui": "/spaces/MCS2024xR2/pages/191924449/Backup+and+restore+data+procedures",
      "edit": "/pages/resumedraft.action?draftId=191924449",
      "tinyui": "/x/4YhwCw",
      "self": "https://docs.nomagic.com/rest/api/content/191924449"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS2024xR2",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/191924449/child",
      "restrictions": "/rest/api/content/191924449/restriction/byOperation",
      "history": "/rest/api/content/191924449/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/191924449/descendant",
      "space": "/rest/api/space/MCS2024xR2",
      "relevantViewRestrictions": "/rest/api/content/191924449/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/x-sh"
  },
  "extensions": {
    "mediaType": "application/x-sh",
    "fileSize": 9696,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/191924449/restore-single_node_311.sh?version=1&modificationDate=1728049802368&api=v2",
    "webui": "/spaces/MCS2024xR2/pages/191924449/Backup+and+restore+data+procedures?preview=%2F191924449%2F191924453%2Frestore-single_node_311.sh",
    "self": "https://docs.nomagic.com/rest/api/content/191924453"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/191924453/child",
    "restrictions": "/rest/api/content/191924453/restriction/byOperation",
    "history": "/rest/api/content/191924453/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/191924453/descendant",
    "space": "/rest/api/space/MCS2024xR2",
    "relevantViewRestrictions": "/rest/api/content/191924453/restriction/relevantViewRestrictions"
  }
}
````
