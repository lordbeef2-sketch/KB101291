# NI DOCUMENT BUNDLE: labview-datalogging-and-supervisory-control-module

<!--NI_BUNDLE_CHUNK bundle=labview-datalogging-and-supervisory-control-module start=1 end=137 -->
<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=access-citadel-data-using-odbc-queries.html language=enus -->
## TOPIC 00001: Access Citadel Data using ODBC Queries

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `access-citadel-data-using-odbc-queries.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/access-citadel-data-using-odbc-queries.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can access Citadel data using ODBC queries from data tables. You can access Citadel data using ODBC queries from data tables. Aliases TableThe Citadel ODBC driver automatically generates alias names for traces or data sets whose names are longer than the Maximum Column Name Length value specifie

### Access Citadel Data using ODBC Queries

You can access Citadel data using ODBC queries from data tables.

You can access Citadel data using ODBC queries from data tables.

#### Aliases Table

The Citadel
 ODBC driver automatically generates alias names for traces or data sets whose
 names are longer than the Maximum Column Name Length value specified
 in the Citadel 5 ODBC Setup dialog box.

The LabVIEW Datalogging
 and Supervisory Control (DSC) Module stores generated alias names in an Aliases table. The Aliases table has two columns:
 AliasName and FullName.

Database
 tables and column names can be up 126 characters long and cannot contain some special
 characters. Some ODBC clients support only names up to 62 characters long. Note that the
 database URL is not included in the trace or data set name.

The alias name consists
 of a prefix and the original trace or data set name substring, so the total length of the
 alias string is equal to the Maximum Column Name Length value. The
 alias prefix has the following format ~XXXXXXXXXXXXXXXX_
 whereXXXXXXXXXXXXXXXX is a 64-bit trace or data set
 ID.

For example, if the original shared variable URL is
 \\computer\my_database\my_process_folder\my_process\my_folder_1\my_folder_2\pot1.valueand Maximum Column Name Length is 32, the alias name is
 ~A012ABC4045FE43A_r_2/pot1@value where A012ABC4045FE43A is
 the internal trace ID. Note that database URL (\\computer\my_database\)
 is not used for the alias and that certain special characters were mapped to supported
 characters.

Some ODBC clients do not handle certain special characters in column and
 table names. The ODBC clients replace special characters in shared variable names and data
 set names as shown in the following table:

| Special Character | Converted Character |
| --- | --- |
| . | @ |
| \\ | / |

The special characters changed in ODBC 5. If you are converting SQL queries from an
 earlier version earlier of the ODBC driver, you might have to rewrite any SQL queries you
 set up in the earlier processes.

#### IntData Table

With Citadel
 5, the IntData table replaces the
 Traces table. The ODBC driver presents Citadel data to other
 applications as an IntData table. The table contains a field or
 column for each shared variable logged to the Citadel database and three
 fields you can use to specify query criteria and to time stamp retrieved data:
 IntInterval, LocalTime, and
 UTCTime.

Because Citadel is event-driven,
 Citadel logs a value only when the value changes. Using
 IntInterval, you can query Citadel for values
 evenly spaced over a period of time. The Citadel service stores the time
 in UTCTime format and derives LocalTime from
 the stored time. You can configure the time zone per database through the Citadel 5
 ODBC Setup configuration dialog box.

The following table illustrates the
 Citadel 5
 IntData table columns:

| Column Name | Description |
| --- | --- |
| LocalTime | Time stamps that indicate local time when values are logged. Note that local time is calculated from Coordinated Universal Time (UTC) using current time zone setting. |
| UTCTime | Time stamps that indicate UTC time when values are logged. |
| IntInterval | Replaces Interval column available in the Citadel 4.x version. Default interpolation interval is one day. Note that syntax of interpolation interval string is the same and that you can continue to use special interval types (YEAR, MONTH, WEEK). |
| shared variableName | Shared variable name. |

IntInterval specifies the query value sample rate and can
 range from 1 ns to several years. The default value of IntInterval is
 1 (one day). IntInterval appears as a regular table column. Display
 format depends on the IntInterval value specified in the WHERE clause
 of the query. Fixed intervals appear as hh:mm:ss.ffffff.
 ffffff is the fractional part of a second. Special intervals WEEK,
 MONTH, YEAR appear in days.

Refer to the following examples for how to use the
 intervals:

| IntInterval | Interval length | Note |
| --- | --- | --- |
| 1 | One day (24 hours) | — |
| 1.5 | One and a half days (36 hours) | — |
| '0:2' | 2 seconds | — |
| '5:2.125' | 5 minutes, 2 seconds, and 125 milliseconds | — |
| '10:0:0.001' | 10 hours and 1 millisecond | — |
| 'WEEK' | 7 days | — |
| 'MONTH' | 1 month | Accounts for different month lengths and leap years. |
| 'YEAR' | 1 year | Accounts for different month lengths and leap years. |

#### RawData Table

With
 Citadel 5, the RawData table replaces the
 Points table of Citadel 4. Use the
 RawData table to retrieve the actual values logged for a shared
 variable and the times they were logged. Because logging to Citadel takes
 place asynchronously, there is no correlation between the time stamps for one shared
 variable and another. For this reason, when querying the RawData
 table, you can query only one shared variable at a time.

The following table
 illustrates the Citadel 5
 RawData table columns:

| Column Name | Description |
| --- | --- |
| LocalTime | Time stamps that indicate local time when values are logged. Note that local time is calculated from the logged UTC time using current time zone setting. |
| UTCTime | Time stamps that indicate UTC time when values are logged. |
| LoggingTime | Time stamps that indicate local time when values are logged regardless of local time zone setting. |
| shared variableName | Shared variable name. |
| Quality | Shared variable quality. |

The possible values for Quality are in the following
 table:

| Value | Description |
| --- | --- |
| 0x00000000 | Quality good |
| 0x00000001 | Stale |
| 0x00000002 | Sensor Failure |
| 0x00000004 | Device Failure |
| 0x00000008 | Server Failure |
| 0x00000010 | Network Failure |
| 0x00000020 | Nonexistent |
| 0x00000040 | No Known Value |
| 0x00000080 | Inactive |
| 0x00000100 | Forced |
| 0x00000200 | Low Limited |
| 0x00000400 | High Limited |
| 0x00000800 | Constant |
| 0x00001000 | Sensor Inaccurate |
| 0x00002000 | EU Limits Exceeded |
| 0x00004000 | Subnormal |
| 0x00008000 | Math Exception |
| 0x00010000 | Comm Link Failure |

The WHERE clause using LocalTime,
 UTCTime and LoggingTime is supported for the
 RawData table. However, IntInterval is not
 relevant to the RawData table. The data transforms also are not
 relevant to the RawData table and are not supported. Note that standard set functions (MAX,
 MIN, AVG, COUNT) are supported.

#### Dataset
 Tables

IntData and RawData tables
 contain all shared variables available in given Citadel database. Data set tables contain
 only shared variables available in particular data sets. There are
 DS_IntData_dataset and
 DS_RawData_dataset tables per data set. In
 addition to IntData or RawData table columns,
 data set tables have RunID and RunName
 columns.

In addition to the example queries, the WHERE clause can restrict query to
 specified data set run(s).

The following table illustrates the Citadel
 5
 DS_IntData and DS_RawData table columns:

| IntData | Description |
| --- | --- |
| LocalTime | Time stamps that indicate local time when values are logged. Note that local time is calculated from UTC time using current time zone setting. |
| UTCTime | Time stamps that indicate UTC time when values are logged. |
| IntInterval | Interpolation interval. Default interpolation interval is one day. |
| RunID | Unique 64-bit identification of data set run. |
| RunName | Name of data set run. Note that this name is not unique and can be NULL. |
| shared variableName | Shared variable name. |

| RawData | Description |
| --- | --- |
| LocalTime | Time stamps that indicate local time when values are logged. Note that local time is calculated from UTC time using current time zone setting. |
| UTCTime | Time stamps that indicate UTC time when values are logged. |
| LoggingTime | Time stamps that indicate local time when values are logged regardless of local time zone setting. |
| Quality | Shared variable quality. |
| RunID | Unique 64-bit identification of data set run. |
| RunName | Name of data set run. Note that this name is not unique and can be NULL. |
| shared variableName | Shared variable name. |

Parent topic:

Access Citadel Data with SQL

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=access-citadel-data-with-sql.html language=enus -->
## TOPIC 00002: Access Citadel Data with SQL

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `access-citadel-data-with-sql.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/access-citadel-data-with-sql.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section describes Structured Query Language (SQL), Open Database Connectivity (ODBC), and accessing Citadel data using both SQL and ODBC. SQLSQL is an industry-standard language used for retrieving, updating, and managing data. In LabVIEW with the Enterprise Connectivity toolkit and in Lookout,

### Access Citadel Data with SQL

This section describes Structured Query Language (SQL), Open Database Connectivity (ODBC),
 and accessing Citadel data using both SQL and ODBC.

#### SQL

SQL is an industry-standard
 language used for retrieving, updating, and managing data. In LabVIEW with the Enterprise
 Connectivity toolkit and in Lookout, you can use SQL to build queries to
 extract data from a Citadel database. The Citadel ODBC
 driver also includes many built-in data transforms to simplify statistical analysis of
 retrieved data.

#### ODBC

ODBC is a standard developed
 by Microsoft. ODBC defines the mechanisms for accessing data residing in Database Management
 Systems (DBMSs). Nearly all Windows-based applications that can retrieve data from a
 database support ODBC.

Parent topic:

LabVIEW Datalogging and Supervisory Control Module Features

Related concepts:

- Logging Historical Data to the Citadel Database

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=access-pv.html language=enus -->
## TOPIC 00003: Access PVs

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `access-pv.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/access-pv.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Access PVs to read, write, or subscribe to PV values. After you publish PVs to an EPICS network by using the EPICS Server I/O server, use EPICS Client I/O servers or third-party EPICS clients to access PVs.Some third-party EPICS clients do not support all these three operations on PV values. Refer t

### Access PVs

Access PVs to read, write, or
 subscribe to PV values. After you publish PVs to an EPICS network by using the EPICS
 Server I/O server, use EPICS Client I/O servers or third-party EPICS clients to
 access PVs.

Note

When you write values to a PV that corresponds to a Boolean shared variable, you must
 write True or False to this PV. Otherwise, the
 value of this PV does not change.

The following table shows the PV attributes that you can access for different PV
 categories:

| PV Category | PV Attribute | Description |
| --- | --- | --- |
| All | VAL | Displays the current value of the PV. |
| STAT | Displays the current status of the PV. |  |
| SEVR | Displays the current alarm severity of the PV. |  |
| Numeric | HIHI | Displays the HIHI alarm level of the PV. |
| HIGH | Displays the HIGH alarm level of the PV. |  |
| LOW | Displays the LOW alarm level of the PV. |  |
| LOLO | Displays the LOLO alarm level of the PV. |  |
| HHSV | Displays the severity of HIHI alarms. |  |
| HSV | Displays the severity of HIGH alarms. |  |
| LSV | Displays the severity of LOW alarms. |  |
| LLSV | Displays the severity of LOLO alarms. |  |
| Logical | OSV | Displays the severity of ONE alarms. |
| ZSV | Displays the severity of ZERO alarms. |  |
| Array | NELM | Displays the element number of the array. |

Parent topic:

Use EPICS Server I/O Servers

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=access-the-alarms-events-web-service.html language=enus -->
## TOPIC 00004: Access the Alarms & Events Web Service

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `access-the-alarms-events-web-service.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/access-the-alarms-events-web-service.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Datalogging and Supervisory Control (DSC) Module includes the built-in LabVIEW Web service, nialarm.The nialarm web service exposes the Alarms & Events VIs: Read Alarms, Read Events, Acknowledge Alarms, and Alarm Status.Specifying the URLYou use a URL and HTTP methods to interact with th

### Access the Alarms & Events Web
 Service

The LabVIEW Datalogging and Supervisory Control (DSC) Module includes the built-in
 LabVIEW Web service, nialarm.

The nialarm web service exposes the Alarms & Events
 VIs: Read Alarms, Read Events,
 Acknowledge Alarms, and Alarm Status.

#### Specifying the URL

You use
 a URL and HTTP methods to interact with the nialarm web service.
 Refer to the following table to specify the URL pattern, which consists of the web
 method and tag URL, and input parameters of the URL. Input parameters and XML tags
 in post data are case sensitive.

| Description | URL pattern | HTTP method | Input parameters |
| --- | --- | --- | --- |
| Queries alarm information. | alarms/<tag_URL> | GET | host=HOSTNAME (localhost)OUTPUT_FORMAT={XML, JSON} (XML) |
| Queries event information. | events/<tag_URL> | GET | host=HOSTNAME (localhost)OUTPUT_FORMAT={XML, JSON} (XML) |
| Queries alarm and event information. | all/<tag_URL> | GET | host=HOSTNAME (localhost)OUTPUT_FORMAT={XML, JSON} (XML) |
| Queries a summary of the alarms associated with shared variables. | alarmstatus/<tag_URL> | GET | host=HOSTNAMEminPriority=MIN_NUM (0)maxPriority=MAX_NUM (1000)showAcked=BOOL(TRUE\|FALSE) (FALSE)OUTPUT_FORMAT={XML, JSON} (XML) |
| Acknowledges alarms by shared variable. | alarms/<tag_URL> | POSTPost data:ackUser=ACKUSERcomment=TEXT | host=HOSTNAME (localhost) |
| Acknowledges alarms by alarm. | alarms | POSTPost data:AlarmUrl=ALARMURL*ackUser=ACKUSERcomment=TEXT | None |
| Acknowledges alarms by alarm area. | alarms | POSTPost data:alarmArea=AREATEXT*ackUser=ACKUSERcomment=TEXT | None |
| Acknowledges events by shared variable. | events/<tag_URL> | POSTPost data:N/A | host=HOSTNAME (localhost) |
| Acknowledges alarms and events by shared variable. | all/<tag_URL> | POSTPost data:ackUser=ACKUSERcomment=TEXT | host=HOSTNAME (localhost) |

Note

#### Specifying the Tag URL

When
 constructing a URL to interact with the nialarm web service, you
 can specify the tag URL in one of the following formats:

Relative

tag_URL

library

library/variable

host

host

Webservice

tag_URL

library

library/variable

VariableAPI

tag_URL

computer/library

computer/library/variable

The following table shows possible example URLs:

| Web method | Example URL | Description |
| --- | --- | --- |
| all | http://localhost:3580/nialarm/all/library1/variable2HTTP method: POSTPost data: ackUser=operator1&comment=test | Invokes the all Web method to acknowledge the alarms and events associated with the shared variable at \\\\localhost\\library1\\variable2. This example also specifies that the alarms and events are acknowledged by the user operator1 with a comment test. |
| alarms | http://localhost:3580/nialarm/alarms/library1/variable1?host=remote-computer | From the local computer, invokes the alarms Web method to retrieve all alarms for a variable on a computer named remote-computer. By default, information returns as an XML-formatted response because the URL does not specify the output format. |
| alarmstatus | http://localhost:3580/nialarm/alarmstatus?minPriority=100&maxPriority=1000 | Invokes the alarmstatus Web method to retrieve the summaries of alarms whose priority is between 100 and 1000. By default, information returns as an XML-formatted response because the URL does not specify the output format. |
| alarms | http://localhost:3580/nialarm/alarmsHTTP method: POSTPost data: AlarmUrl=\\\\server1\\library1\\variable1.Alarms.HiHi&AlarmUrl=\\\\server2\\library2\\variable2.Alarms.Hi&ackUser=operator1 | Invokes the alarms Web method to acknowledge alarms specified by the AlarmUrl tag in the post data. You can specify optional parameters, such as ackUser and comment, by delimiting these parameters with an ampersand (&). You can specify multiple alarms you want to acknowledge by delimiting them with an ampersand. |
| events | http://localhost:3580/nialarm/events/library1/variable1HTTP method: POSTPost data: N/A | Invokes the events Web method to acknowledge the events associated with the shared variable at \\\\localhost\\library1\\variable1. |

#### Configuring Remote
 Access

You can configure the nialarm web service to
 query alarms and events that reside on the same computer as the web service or that
 reside on other computers. By default, the web service can query alarms and events
 on other computers. To query alarms and events on the same computer as the Web
 service only, specify RemoteSupport=[FALSE] in the
 [NI_AlarmEvent_WS] section of the web service configuration
 file. The web service configuration file is located in the
 C:\ProgramData\National
 Instruments\WebServices\NI\nialarm\WebServices.ini
 directory.

Parent topic:

Interact with DSC Module Web Services

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=access-the-citadel-web-service.html language=enus -->
## TOPIC 00005: Access the Citadel Web Service

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `access-the-citadel-web-service.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/access-the-citadel-web-service.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Datalogging and Supervisory Control (DSC) Module includes the following Historical VIs and Tags VI for the nicitadel web service.The nicitadel web service exposes these VIs:Alarm & Event Query (queries alarms only)Get Computer ListGet Database ListGet Trace InfoGet Trace ListRead TraceSp

### Access the Citadel Web Service

The LabVIEW Datalogging and Supervisory Control (DSC) Module includes the following
 Historical VIs and Tags VI for the nicitadel
 web service.

The nicitadel web service exposes these VIs:

- Alarm & Event Query (queries alarms only)
- Get Computer List
- Get Database List
- Get Trace Info
- Get Trace List
- Read Trace

#### Specifying the URL

You use
 a URL and HTTP methods to interact with the nicitadel Web service. Refer to the
 following table to specify the URL pattern, which consists of the Web method and tag
 URL, and input parameters of the URL. Input parameters are case sensitive.

| Description | URL pattern | HTTP method | Input parameters |
| --- | --- | --- | --- |
| Queries a list of computers on the local network. | computerlist | GET | OUTPUT_FORMAT={XML, JSON} (XML) |
| Queries a list of databases on the computer you specify in <computer>. | databaselist/<computer> | GET | OUTPUT_FORMAT={XML, JSON} (XML) |
| Queries a list of traces. | tracelist | GET | dbpath=DB_SERVER/DB_PATH (localhost/Default_Database)OUTPUT_FORMAT={XML, JSON} (XML) |
| Queries trace information. | info/<tag_URL> | GET | dbpath=DB_SERVER/DB_PATH (localhost/Default_Database)OUTPUT_FORMAT={XML, JSON} (XML) |
| Queries trace data. | trace/<tag_URL> | GET | start=TIMESTAMP (Timestamp of the first data point) end=TIMESTAMP (Timestamp of the last data point) dbpath=DB_SERVER/DB_PATH (localhost/Default_Database)maxItems=INTEGER (–1)decimate=BOOLEAN (FALSE)OUTPUT_FORMAT={XML, JSON} (XML) |
| Queries historical alarms. | alarms/<tag_URL> | GET | start=TIMESTAMP (Timestamp of the first alarm) end=TIMESTAMP (Timestamp of the last alarm) dbpath=DB_SERVER/DB_PATH (localhost/Default_Database) OUTPUT_FORMAT={XML, JSON} (XML) |

Note

#### Specifying the Tag URL

You must specify the <tag_URL> as an absolute path in the
 following format: computer/library/variable. For example, when
 you invoke the info or trace Web methods, you must
 specify the variable name in the <tag_URL>.

When
 invoking the alarms Web method, you can define
 <tag_URL> as computer/library,
 computer, or unspecified. If you do not
 specify the <tag_URL>, the alarms Web
 method queries the historical alarms under the localhost and the
 default database.

When you specify an input parameter, use the following table to understand the values
 that the input parameter can accept:

| Input parameter | Input parameter value | Description | Example |
| --- | --- | --- | --- |
| dbpath | DB_SERVER/DB_PATH | Specifies the database path. DB_SERVER and DB_PATH are strings. The forward slash (/) is required. | dbpath=computer1/mydatabase |
| startend | TIMESTAMP | Specifies the timestamp. The format must be YYYY-MM-DDThh:mm:ss(+/-)time-offset, where T is a delimiter separating the date and time and time-offset is the hours and minutes ahead or behind UTC time. | start=2010-12-31T00:30:57+08:00 |
| maxItems | INTEGER | Specifies an integer. The default is –1, which means the trace Web method queries the maximum number of traces. Possible values are –1, 0, 1, 2,... If the value is greater than 2,147,483,647, the Web method queries only a maximum of 2,147,483,647 traces. | maxItems=1000 |
| decimate | BOOLEAN | Specifies a Boolean. Possible values are TRUE and FALSE. | decimate=TRUE |

The following table shows possible example URLs:

| Web method | Example URL | Description |
| --- | --- | --- |
| computerlist | http://localhost:3580/nicitadel/computerlist?OUTPUT_FORMAT=JSON | Invokes the computerlist Web method to retrieve computers on the local network. Information returns as a JSON-formatted response. |
| databaselist | http://localhost:3580/nicitadel/databaselist/computer1?OUTPUT_FORMAT=JSON | Invoke the databaselist Web method to retrieve the list of databases on the computer computer1. |
| trace | http://localhost:3580/nicitadel/trace/computer1/library1/variable1?OUTPUT_FORMAT=JSON&dbpath=computer1/Default_Database | Invokes the trace Web method to retrieve the trace data of the trace URL computer1/library1/variable1 and database path computer1/Default_Database. |
| alarms | http://localhost:3580/nicitadel/alarms/computer1/library1?dbpath=computer1/C__Program_Files_National_Instruments_LabVIEW_2010_data | Invokes the alarms Web method to retrieve the historical alarms of the trace URL computer1/library1/variable1 and database path computer1/C__Program_Files_National_Instruments_LabVIEW_2010_data. By default, information returns as an XML-formatted response because the URL does not specify the output format. |

Parent topic:

Interact with DSC Module Web Services

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=acknowledge-alarms.html language=enus -->
## TOPIC 00006: Acknowledging Alarms

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `acknowledge-alarms.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/acknowledge-alarms.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Datalogging and Supervisory Control (DSC) Module generates alarms when pre-defined behaviors or errors occur in DSC Module applications. Acknowledging alarms ensures that you notice the unexpected or bad values of shared variables.When you configure alarms, you can configure the DSC Modu

### Acknowledging Alarms

The LabVIEW Datalogging and Supervisory Control (DSC) Module generates alarms when
 pre-defined behaviors or errors occur in DSC Module applications. Acknowledging alarms
 ensures that you notice the unexpected or bad values of shared variables.

Note

You can acknowledge alarms by using the methods referenced in the *Related
 Concepts*.

Parent topic:

Use Alarms and Events in DSC Module Applications

Related tasks:

- Configuring Alarms

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=archive-citadel-data.html language=enus -->
## TOPIC 00007: Archive Citadel Data

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `archive-citadel-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/archive-citadel-data.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can archive historical data in the following ways: Use the Historical Data Viewer. Use the Archive Traces VI to merge two existing databases by archiving the databases into the same directory. Archive the Citadel database manually by copying or moving the database files. If you archive the datab

### Archive Citadel Data

You can archive historical data in the following ways:

- Use the Historical Data Viewer .
- Use the Archive Traces VI to merge two existing databases by archiving the
 databases into the same directory.
- Archive the Citadel database manually by copying or moving the database
 files.

If you archive the database manually, you must detach the database before you archive it
 manually. Detach the database using the Historical Data Viewer in
 MAX or the Detach Database VI. You then can
 use the Historical Data Viewer to reattach the database after you
 copy it. Copy the LabVIEW project library (.lvlib) and the
 historical files to the new location. Although you can retrieve historical data without
 the .lvlib file, you do not have the shared variable configuration
 information, such as engineering range and unit, unless you archive the
 .lvlib file. Stop the Shared Variable Engine and
 Citadel database before archiving the files manually.

When you create a .lvlib file, the default location for the data generated
 by the shared variables configured in that file is a directory called
 data located in the directory in which you saved the
 .lvlib file. Maintain the relative path between the
 .lvlib file and the historical files in the new archive
 location. For example, if the .lvlib file is in
 c:\archive, keep the historical database in
 c:\archive\data.

Copy or move all files in the database directory to the directory you have selected as the
 logging directory. However, if you copy those files into a directory with an already
 existing database, the filenames collide. You can safely merge two databases by
 archiving the databases into the same database directory with the Archive
 Traces VI and the Historical Data Viewer.

Parent topic:

Logging Historical Data to the Citadel Database

Related concepts:

- Logging Historical Data to the Citadel Database
- Pass Data between LabVIEW and the Shared Variable Engine

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=archiving-and-extracting-alarm-and-event-data.html language=enus -->
## TOPIC 00008: Archiving and Extracting Alarm and Event Data

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `archiving-and-extracting-alarm-and-event-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/archiving-and-extracting-alarm-and-event-data.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can manage alarm and event data logged to Citadel manually or programmatically.To archive and export logged alarms and events manually, use the Historical Data Viewer, available in the Measurement & Automation Explorer. To programmatically archive logged alarms and events, use the Alarm & Event

### Archiving and Extracting Alarm and Event Data

You can manage alarm and event data logged to Citadel manually or
 programmatically.

To archive and export logged alarms and events manually, use the Historical Data
 Viewer, available in the Measurement &
 Automation Explorer. To programmatically archive logged
 alarms and events, use the Alarm & Event Archive VI.
 To extract alarm and event data from a Citadel database,
 use the Alarm & Event Query VI.

Parent topic:

Use Alarms and Events in DSC Module Applications

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=bind-shared-variables-to-opc-server-data-i.html language=enus -->
## TOPIC 00009: Bind Shared Variables to OPC Server Data Items

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `bind-shared-variables-to-opc-server-data-i.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/bind-shared-variables-to-opc-server-data-i.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can bind shared variables to data items on OPC servers if you have created an OPC Client I/O server for the OPC server already.Use the data items of OPC Client I/O servers to set the active state of OPC Client I/O servers and monitor the servers to which the client instances connect. OPC Client

### Bind Shared Variables to OPC Server Data
 Items

You can bind shared variables to data items on OPC servers if you have created an OPC
 Client I/O server for the OPC server already.

Use the data items of OPC Client I/O servers to set the active state of OPC Client I/O servers
 and monitor the servers to which the client instances connect. OPC Client I/O servers
 have the following data items:

Active

Change to Write

Change to
 Read

TRUE

FALSE

Connected

TRUE

OPC Interface Version

Revised Update Rate

Server ProgID

Note

Parent topic:

Shared Variables

Related concepts:

- Creating OPC Client I/O Servers

Related tasks:

- Binding Shared Variables to Data Items on OPC Servers That Do Not Support Browsing

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=binding-shared-variables-to-data-items-on-opc.html language=enus -->
## TOPIC 00010: Binding Shared Variables to Data Items on OPC Servers That Do Not Support Browsing

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `binding-shared-variables-to-data-items-on-opc.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/binding-shared-variables-to-data-items-on-opc.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: If an OPC server does not support the Server Browse Address Space Interface, LabVIEW does not automatically display data items for that OPC server. Complete the following steps to bind a shared variable to a data item on these kinds of OPC servers. Add a shared variable to the project or right-click

### Binding Shared Variables to Data Items on OPC Servers That Do Not Support Browsing

If an OPC server does not support the Server Browse Address Space Interface, LabVIEW
 does not automatically display data items for that OPC server. Complete the
 following steps to bind a shared variable to a data item on these kinds of OPC
 servers.

1. Add a shared variable to the project or right-click an existing shared variable
 in the Project Explorer window and select
 Properties from the shortcut menu. 
 The Shared Variable Properties dialog box is
 displayed.
2. On the Variable page, place a checkmark in the
 Enable Aliasing checkbox.
3. In the Bind to pull-down menu, select PSP URL.
4. Click the Browse button to display the Browse
 for Variable dialog box. Select the OPC Client I/O server for
 the OPC server data item to which you want to bind the shared variable.
5. In the Access Type pull-down menu, select an access type.
6. Click the OK button.

Parent topic:

Interact with Data Using I/O Servers

Related concepts:

- Use OPC Client I/O Servers

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=build-front-panels-for-dsc-module-applicat.html language=enus -->
## TOPIC 00011: Build Front Panels for DSC Module Applications

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `build-front-panels-for-dsc-module-applicat.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/build-front-panels-for-dsc-module-applicat.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can build the front panel of a VI with a combination of controls and indicators representing the values of shared variables.A front panel is the user interface of a VI. Graphics, both as decorations and as controls and indicators, can make front panels easier to operate and more informative.Conn

### Build Front Panels for DSC Module
 Applications

You can build the front panel of a VI with a combination of controls and indicators
 representing the values of shared variables.

A front panel is the user interface of a VI. Graphics, both as decorations and as controls
 and indicators, can make front panels easier to operate and more informative.

#### Connecting Controls and Indicators to Shared
 Variables

You can connect front panel objects to shared variables to read and write shared variable
 data.

#### Creating a Shared Variable Control and Shared
 Variable Constant

Use the shared variable control and shared variable constant to
 select, browse to, or enter shared variables for use in VIs. You can wire the shared
 variable control and shared variable constant into Alarms & Events
 VIs, Historical VIs, DataSocket VI and functions, and
 the Shared Variables VIs. You also can configure alarms, scaling,
 security, and logging options using the SharedVariableIO properties. To access the
 SharedVariableIO properties, right-click a shared variable constant on the block diagram and
 select Create»Property from the shortcut menu.

Note

Variable
 Type

Network-Published

Variable

Shared Variable
 Properties

By default, the shared variable control and
 shared variable constant accept any name. You can configure the shared variable control or
 shared variable constant to accept only names of existing shared variables by right-clicking
 the shared variable object and removing the checkmark from Allow Undefined
 Names in the shortcut menu. Removing the checkmark from Allow
 Undefined Names means that you must enter the name of an existing shared
 variable into the shared variable object.

When you save VIs that contain a shared
 variable control or shared variable constant, each shared variable control and shared
 variable constant retains the shared variable name that you selected.

#### Adding and Customizing Graphics

The DSC Module Controls palette includes Boolean controls and indicators such as pipes,
 valves, and pumps, and numeric controls and indicators such as tanks and hoppers. These
 images change to reflect the state of the shared variables to which you connect
 them.

The LabVIEW Datalogging and Supervisory Control (DSC) Module also includes the
 Image Navigator, which is an extensive library of supervisory control images and other
 images ranging from basic geometric shapes to drawings of special equipment. You can launch
 the Image Navigator by selecting Tools»DSC Module»Image Navigator.
 Refer to the *Image Navigator Help*, available by selecting
 Help»Contents in the Image Navigator, for more information about
 editing, copying, and importing and exporting graphics with the Image
 Navigator.

#### Security Configuration

The DSC
 Module includes the Front Panel Security dialog box, available by
 selecting Tools»Security»Front Panel Security, to allow you to add
 security options to many front panel objects. You also can add security to front panel
 objects individually with the Security tab of the object properties
 dialog box, available by right-clicking the control or indicator and selecting
 Properties from the shortcut menu.

Parent topic:

Displaying and Controlling Data

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=building-a-dsc-module-application.html language=enus -->
## TOPIC 00012: Building a DSC Module Application

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `building-a-dsc-module-application.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/building-a-dsc-module-application.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the following guidelines to develop a DSC Module application. Plan the application requirements, including requirements for channel count, hardware or other I/O sources, data logging, security, and performance. Do not skip step 1. This step impacts decisions at every stage of development, includ

### Building a DSC Module Application

Use the following guidelines to develop a DSC Module
 application.

1. Plan the application requirements, including requirements for channel
 count, hardware or other I/O sources, data logging, security, and
 performance. 
 Note Do
 not skip step 1. This step impacts decisions at every stage of
 development, including setting up servers, configuring shared
 variables, and setting up network clients and
 servers.
2. Physically establish a connection to the hardware. Connect, configure,
 test, and troubleshoot the hardware.
3. Configure I/O servers to communicate with the hardware. Use the
 Distributed System Manager to verify connections to the hardware. You
 must deploy the LabVIEW project libraries in the application before
 using the System Manager to verify and troubleshoot the connections.
 In LabVIEW, select Tools»Distributed System
 Manager to launch the System Manager.
4. Use the Batch Variable Creation dialog box,
 available by right-clicking a LabVIEW project library in the
 Project Explorer window and selecting
 Create Variables from the shortcut menu,
 to create many shared variables in one batch. You also can use the
 Create Bound Variables dialog box,
 available by right-clicking a project library in the
 Project Explorer window and selecting
 Create Bound Variables from the shortcut
 menu, to bind the shared variables you create to I/O server data
 items. Repeat step 3 to verify that the shared variables communicate
 with the I/O source.
5. Add additional shared variables and configure data logging and alarming
 as necessary for your application.
6. Build the Human Machine Interface (HMI) portion of the
 application.
7. Use the LabVIEW and DSC Module VIs and functions to
 add additional functionality to the HMI application.
8. Test, deploy, and document the application. Use the System Manager to
 troubleshoot the application if you find problems while testing.

Use LabVIEW Application Builder to build
 an application. Right-click Build Specifications in
 the Project Explorer window and select
 New»Application (EXE) from the shortcut menu to
 display the Application Properties dialog
 box.

Note

Include all VIs you want to use in the
 built application, as well as external data files, as source files to create
 an executable. On theSource Files page of the
 Application Properties dialog box, you can
 specify files to include with the application. For a DSC Module application,
 you usually include the following files:

- Project libraries ( .lvlib )
- Hardware configuration files, such as MAX configuration data
- Server software for all servers the application depends on for data

When you build an application that includes custom I/O servers, place a
 checkmark in the Deploy libraries for shared variables when
 application starts checkbox on the Shared
 Variable Deployment page. Then, the LabVIEW Application
 Builder detects and copies all dependent custom I/O servers to the
 LVDSC folder inside the same directory as the
 build.

You also can add all dependent custom I/O servers to the build
 by adding the project libraries of the custom I/O servers to the
 Always Included list on the Source
 Files page. Do not modify or remove any files in the
 LVDSC folder. If you add the project libraries to
 the Always Included list without placing a checkmark
 in the Deploy libraries for shared variables when application
 startscheckbox, you must deploy these project libraries
 programmatically by using the Deploy Libraries
 VI.

If the application you want to build uses VI Server properties and
 methods to modify a project library or shared variables within a project
 library, place a checkmark in the Enable Enhanced DSC Run-Time
 support checkbox on the Advanced
 page of the Application Properties dialog
 box.

You can build an installer to install the built application on a
 target computer later. Right-click Build
 Specifications in the Project
 Explorer window and select
 New»Installer from the shortcut menu to build
 an installer for the application.

Note

Parent topic:

Design a DSC Module Application

Related concepts:

- Interact with Data Using I/O Servers
- Managing I/O with Shared Variables
- Network and Deploy Applications
- Logging Historical Data to the Citadel Database
- Set Alarms for Shared Variables

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=choose-between-modbus-i-o-servers-and-modbu.html language=enus -->
## TOPIC 00013: Choose between Modbus I/O Servers and Modbus VIs

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `choose-between-modbus-i-o-servers-and-modbu.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/choose-between-modbus-i-o-servers-and-modbu.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use both Modbus VIs and Modbus I/O servers to create Modbus masters and slaves and perform read and write operations on Modbus slaves.LabVIEW provides Modbus VIs and Modbus I/O servers for establishing Modbus communication between devices connected over different types of buses or networks.T

### Choose between Modbus I/O Servers and Modbus
 VIs

You can use both Modbus VIs and Modbus I/O servers to create Modbus
 masters and slaves and perform read and write operations on Modbus slaves.

LabVIEW provides Modbus VIs and Modbus I/O servers for establishing Modbus
 communication between devices connected over different types of buses or networks.

The following table compares the attributes of Modbus VIs and Modbus I/O
 servers:

| Attribute | Modbus VIs | Modbus I/O Servers |
| --- | --- | --- |
| Complexity | Complex | Configuration based and easy to use |
| Functionality | Full-featured | Unable to complete certain functions, such as reading exception status |
| Customization | Infinite customization | Limited customization |

Use the following table to help you decide which method to choose:

| Method | Typical Use Cases |
| --- | --- |
| Modbus VIs | Reading exception status of Modbus slaves.Using a TCP Modbus slave to listen to different ports or using a TCP Modbus master to connect to different ports.Building a control system with specific performance or rate requirements. In other words, you want to control the requests that Modbus masters generate, determine when to send these requests, and operate on the responses that Modbus slaves send. For example, you want to read and write five holding registers at 50 Hz and all the other data at 1 Hz. |
| Modbus I/O Servers | Accessing Modbus data tables as floating-point numbers.Establishing Modbus communication between a Supervisory Control And Data Acquisition (SCADA) system and devices. You do not have any specific performance requirements on this system or want any deterministic control over devices. |

Parent topic:

Modbus Communication in LabVIEW

Related concepts:

- Use Modbus I/O Servers
- Modbus Communication in LabVIEW

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=choosing-an-i-o-server.html language=enus -->
## TOPIC 00014: Choose an I/O Server

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `choosing-an-i-o-server.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/choosing-an-i-o-server.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can create the following types of I/O servers with the LabVIEW Datalogging and Supervisory Control (DSC) Module: alarm printer, custom, data set marking, EPICS client, EPICS server, Modbus, Modbus slave, or OPC client. Alarm Printer You can create Alarm Printer I/O servers to print alarms and ev

### Choose an I/O Server

You can create the following types of I/O servers with the LabVIEW Datalogging and
 Supervisory Control (DSC) Module: alarm printer, custom, data set marking, EPICS client, EPICS
 server, Modbus, Modbus slave, or OPC client.

Alarm Printer

Custom

DSC Module

Data Set Marking

EPICS Client

EPICS Server

Modbus

Modbus Slave

OPC Client

Refer to the *How LabVIEW Uses I/O Servers* article on the Developer Zone web site for
 more information about the I/O servers that you can create in LabVIEW.

Parent topic:

Interact with Data Using I/O Servers

Related concepts:

- Pass Data between LabVIEW and the Shared Variable Engine

Related tasks:

- Print Alarm and Event Data

Related information:

- How LabVIEW Uses I/O Servers

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=committing-shared-variables.html language=enus -->
## TOPIC 00015: Committing Shared Variables

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `committing-shared-variables.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/committing-shared-variables.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Committing a Single Shared Variable Complete the following steps to commit a single shared variable to the Shared Variable Engine (SVE). Wire a shared variable reference number to the Property Set Mode property of the SharedVariableIO class. Set the Property Set Mode property to buffer.If you are cr

### Committing Shared Variables

#### Committing a Single Shared
 Variable

Complete the following steps to commit a single shared variable
 to the Shared Variable Engine (SVE).

1. Wire a shared variable reference number to the Property Set Mode property of the
 SharedVariableIO class.
2. Set the Property Set Mode property to buffer . Note If you are
 creating a new shared variable, set the set mode
 input of the Create Shared Variable VI to
 buffer.
3. Wire the shared variable output of
 the Property Set Mode property or of the Create Shared
 Variable VI to the shared variable input of
 another SharedVariableIO class Property Node.
4. Use the second Property Node to enable other
 SharedVariableIO properties for the shared variable.
5. Wire the shared variable output of the second Property
 Node to the shared variable input of a Property Set Mode
 property.
6. Set the Property Set Mode property to commit .
7. Run the VI.

#### Committing Multiple Shared
 Variables

Complete the following steps to commit multiple shared variables to the SVE
 simultaneously.

1. Wire a shared variable refnum to the Property Set Mode property of the SharedVariableIO
 class.
2. Set the Property Set Mode property to buffer . Note If you are
 creating a new shared variable, set the set mode
 input of the Create Shared Variable VI to
 buffer.
3. Wire the shared variable output of the Property Set
 Mode property or of the Create Shared Variable VI to the
 shared variable input of another SharedVariableIO
 class Property Node.
4. Use the second Property Node to enable other SharedVariableIO properties
 for the shared variable.
5. Repeat steps 1-4 for each shared variable you want to commit.
6. Wire an array of the shared variable references you created or modified to the shared
 variables input of the Commit Shared
 Variables VI.
7. Run the VI.

Parent topic:

Deploying, Committing, and Monitoring Shared Variables

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=components-of-a-dsc-module-application.html language=enus -->
## TOPIC 00016: Components of a DSC Module Application

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `components-of-a-dsc-module-application.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/components-of-a-dsc-module-application.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: A LabVIEW Datalogging and Supervisory Control (DSC) Module application typically consists of three components: front panels that you use to view and interact with data, shared variables that represent I/O data, and supervisory programs that implement custom I/O logic.Some advanced DSC Module applica

### Components of a DSC Module Application

A LabVIEW Datalogging and Supervisory Control (DSC) Module application typically consists
 of three components: front panels that you use to view and interact with data, shared
 variables that represent I/O data, and supervisory programs that implement custom I/O
 logic.

Note

You can organize the components of a DSC Module application in a LabVIEW project.

The Shared Variable Engine (SVE) manages and provides access to shared variables. All DSC Module
 applications use both LabVIEW and the SVE.

Refer to the following sections for specific information on each components.

- [Front Panels](front-panels.html)
- [Shared Variables and I/O Servers](shared-variables-and-io-servers.html)
- [Supervisory Programs](supervisory-programs.html)

Parent topic:

Design a DSC Module Application

Related concepts:

- Pass Data between LabVIEW and the Shared Variable Engine
- Logging Historical Data to the Citadel Database
- Set Alarms for Shared Variables
- Configure Security

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=configure-alarms-and-events.html language=enus -->
## TOPIC 00017: Configure Alarms and Events

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `configure-alarms-and-events.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/configure-alarms-and-events.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Datalogging and Supervisory Control (DSC) Module provides multiple predefined alarms for the specified shared variable data types.Predefined alarms for the specified shared variable data types: HI_HI Valid for numeric shared variables only HI Valid for numeric shared variables only LO Va

### Configure Alarms and Events

The LabVIEW Datalogging and Supervisory Control (DSC) Module provides multiple predefined
 alarms for the specified shared variable data types.

Predefined alarms for the specified shared variable data types:

HI_HI

HI

LO

LO_LO

Bad Status

Rate of Change

Value

You can enable and configure alarms and events for shared variables by using the following
 methods:

- Shared Variable Properties dialog box — You can enable and configure
 alarms and events for shared variables in the Shared Variable
 Properties dialog box. Access this dialog box by right-clicking a
 shared variable in the Project Explorer window and selecting
 Properties from the shortcut menu.
- Multiple Variable Editor window — You can use the Multiple
 Variable Editor window to enable and configure alarms and events of
 multiple shared variables.
- Distributed System Manager — You can use the Distributed System Manager
 to configure parameters of shared variable alarms.

Before the DSC Module can log alarms and events, you must enable alarms and events logging.
 Right-click a LabVIEW project library in the Project Explorer window and select
 Properties from the shortcut menu. Select DSC
 Settings: Database from the Category list. On the
 Citadel page or Relational Database
 page, place a checkmark in the Enable Alarms and Events Logging
 checkbox.

If you configure a shared variable for data or event logging to the Citadel
 database but the Shared Variable Engine (SVE) cannot establish a connection to the
 Citadel database, the SVE triggers an alarm and logs the data to
 the default database.

You can use the DSC Module to create user-defined alarms and events. User-defined alarms and
 events are not associated with a shared variable. You can use user-defined alarms and
 events for error handling and event triggering to detect when an application runs
 abnormally. LabVIEW logs the user-defined alarm or event to the
 Citadel historical database.

Parent topic:

Use Alarms and Events in DSC Module Applications

Related concepts:

- Supported Shared Variable Types
- Pass Data between LabVIEW and the Shared Variable Engine

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=configure-scaling-for-shared-variables.html language=enus -->
## TOPIC 00018: Configure Scaling for Shared Variables

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `configure-scaling-for-shared-variables.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/configure-scaling-for-shared-variables.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Scaling is useful for converting a range of values from measured units into a calculated range. You can configure scaling for each data type of shared variables.You can configure scaling on the Scaling page of the Shared Variable Properties dialog box. You also can use the Scaling SharedVariableIO p

### Configure Scaling for Shared Variables

Scaling is useful for converting a range of values from measured units into a calculated
 range. You can configure scaling for each data type of shared variables.

You can configure scaling on the Scaling page of the Shared
 Variable Properties dialog box. You also can use the Scaling
 SharedVariableIO properties.

#### Scaling Numeric Shared
 Variables

You can use linear and square root scaling for numeric shared
 variables.

Often an application needs the LabVIEW Datalogging and Supervisory
 Control (DSC) Module to manipulate the raw data used in the device server to put the
 data in a form, called engineering units, suitable for the users of the application.
 You can define the raw range and engineering range for a shared variable to perform
 simple conversions between the two ranges on the Scaling page of the
 Shared Variable Properties dialog box. The raw range
 refers to the values used by the device server. The engineering range refers to the
 values used by the Shared Variable Engine and the Human Machine Interface (HMI)
 application.

#### Linear and Square Root
 Scaling

Linear scaling is defined by the following
 equation:

m * raw +
 b

where

- b is the Engineering Zero Scale
- m is the ( Engineering Full Scale –
 Engineering Zero Scale )/( Raw Full
 Scale – Raw Zero Scale ).

Square root scaling is defined by the following
 equation:

b + m *
 sqrt(raw – o)

where

- b is the Engineering Zero Scale
- m is the ( Engineering Full Scale –
 Engineering Zero Scale )/sqrt( Raw Full
 Scale – Raw Zero Scale )
- o is the Raw Zero Scale

The following table shows shared variable values that range from 0 to 100 scaled
 to engineering units ranging from 0 to 10:

| Raw Units | Linear Scale | Square Root Scale |
| --- | --- | --- |
| 0 | 0 | 0 |
| 4 | .4 | 2 |
| 9 | .9 | 3 |
| 10 | 1 | 3.16 |
| 16 | 1.6 | 4 |
| 20 | 2 | 4.47 |
| 25 | 2.5 | 5 |
| 30 | 3 | 5.48 |
| 36 | 3.6 | 6 |
| 40 | 4 | 6.32 |
| 49 | 4.9 | 7 |
| 50 | 5 | 7.07 |
| 60 | 6 | 7.75 |
| 64 | 6.4 | 8 |
| 70 | 7 | 8.37 |
| 80 | 8 | 8.94 |
| 81 | 8.1 | 9 |
| 90 | 9 | 9.49 |
| 100 | 10 | 10 |

The following table shows shared variable values that range from 0 to 100
 scaled to engineering units ranging from 15 to 30:

| Raw Units | Linear Scale | Square Root Scale |
| --- | --- | --- |
| 0 | 15 | 15 |
| 4 | 15.60 | 18 |
| 10 | 16.50 | 19.74 |
| 16 | 17.40 | 21 |
| 20 | 18 | 21.71 |
| 30 | 19.50 | 23.22 |
| 36 | 20.40 | 24 |
| 40 | 21 | 24.49 |
| 50 | 22.50 | 25.61 |
| 60 | 24 | 26.62 |
| 64 | 24.60 | 27 |
| 70 | 25.50 | 27.55 |
| 80 | 27 | 28.42 |
| 90 | 28.5 | 29.23 |
| 100 | 30 | 30 |

Offset scaling delivers more complicated results.

#### Linear Scaling Example

In
 this example, a device server returns a voltage from 0 to 5 V. The voltage is
 related to a position sensor, and the real-world position is measured in
 centimeters, with 0 V mapped to 50 cm and 5 V mapped to 100 cm.

The following
 table shows the values of the shared variables after scaling:

| Raw Units (V) | Linear Scale (cm) |
| --- | --- |
| 0 | 50 |
| 1 | 60 |
| 2 | 70 |
| 3 | 80 |
| 4 | 90 |
| 5 | 100 |

#### Square Root Scaling
 Example

In this example, a flow meter measures the flow rate of a liquid
 using a differential pressure reading. The device server provides 4 to 20 mA
 readings. The actual flow is measured in Gallons Per Minute (GPM), where 4 mA
 corresponds to 0 GPM and 20 mA corresponds to 100 GPM.

The following table
 shows the values of the shared variables after scaling:

| Raw Units (mA) | Square Root Scale (GPM) |
| --- | --- |
| 4 | 0 |
| 5 | 25 |
| 6 | 35.36 |
| 7 | 43.3 |
| 8 | 50 |
| 10 | 61.24 |
| 13 | 75 |
| 15 | 82.92 |
| 20 | 100 |

#### Assigning Units to a Double Shared
 Variable

Use the Scaling.Units SharedVariableIO
 property to assign units to a shared variable. In the previous example, you could
 specify gallons per minute as a constant to the Scaling.Units
 property.

#### Scaling Boolean Shared
 Variables

You can use inverted scaling for Boolean shared variables. When you enable inverted
 scaling, the DSC Module inverts the Boolean value when communicating with the
 server.

#### Scaling U32 Bit Field Shared
 Variables

You can use invert mask and select mask scaling for U32 bit
 field shared variables.

Mask scaling applies only to U32 bit fields. LabVIEW
 stores a bit field as a number, translating the number back into a 32-bit field when
 needed. The bit field holds a collection of 32 values, each value limited to 1 or 0.
 With mask scaling, you can decide which of these array members to pay attention to.
 Any bit filtered out by the mask appears as a zero. Bits not filtered out appear as
 zero or one, reflecting the actual value. A mask of
 00000000000000001111111111111111 (0x0000FFFF)
 where 0 marks a position to filter out and 1 marks
 a place to report, reads the bit array:
 10110011100011001100111000110010

as the following:
 00000000000000001100111000110010

Note

The following table shows examples of
 shared variables configured for U32 bit field scaling:

| Shared Variable Name | Raw Value | Scaling Invert Mask | Scaling Select Mask | Scaled Value |
| --- | --- | --- | --- | --- |
| Shared Variable 1 | 0x0000000F | 0x00000000 | 0x000000FF | 0x0000000F |
| Shared Variable 2 | 0x0000000F | 0x00000033 | 0x000000FF | 0x0000003C |
| Shared Variable 3 | 0x0000000F | 0x00000033 | 0x0000000F | 0x0000000C |
| Shared Variable 4 | 0x0000000F | 0x00000000 | 0x00000033 | 0x00000003 |
| Shared Variable 5 | 0x0000000F | 0x00000033 | 0x00000033 | 0x00000030 |
| Shared Variable 6 | 0x00000FF0 | 0x0000000F | 0x000000FF | 0x000000FF |

Parent topic:

Shared Variable Properties

Related tasks:

- Scaling Boolean Shared Variables
- Scaling U32 Bit Field Shared Variables

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=configure-security.html language=enus -->
## TOPIC 00019: Configure Security

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `configure-security.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/configure-security.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: To implement security in an application, you must set up user and group accounts and then configure and restrict access to the front panel controls and indicators.Add security to a LabVIEW Datalogging and Supervisory Control (DSC) Module application to restrict user access to the front panel based o

### Configure Security

To implement security in an application, you must set up user and group accounts and then
 configure and restrict access to the front panel controls and indicators.

Add security to a LabVIEW Datalogging and Supervisory Control (DSC) Module application to
 restrict user access to the front panel based on permissions attached to user account
 names. You can create a system with permission-based security in which users are allowed
 various degrees of access to tools or data depending on the permission attached to their
 account names in the access property of the tool or data involved.

- [Create and Configure User and Group Accounts](create-and-configure-user-and-group-accou.html)
- [Set Access to Front Panel Controls and Indicators](set-access-to-front-panel-controls-and-in.html)
- [Configuring Security Settings for Front Panel Controls and Indicators](configuring-security-settings-for-front-panel.html)
- [Configuring Security Settings for Shared Variables](configuring-security-settings-for-shared-vari.html)
- [Disabling Windows Special Key Capabilities](disabling-windows-special-key-capabilities.html)
- [Logging In and Out](logging-in-and-out-dsc-module.html)
- [Setting a Proxy User Account](setting-a-proxy-user-account.html)

Parent topic:

LabVIEW Datalogging and Supervisory Control Module Features

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=configure-shared-variables-dsc-module-or-re.html language=enus -->
## TOPIC 00020: Configure Shared Variables

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `configure-shared-variables-dsc-module-or-re.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/configure-shared-variables-dsc-module-or-re.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure an individual shared variable interactively, a group of shared variables interactively, or any number of shared variables programmatically. Use the following table to understand the methods of configuring a shared variable. Method Recommended Use Required Product Interactively by u

### Configure Shared Variables

You can configure an individual shared variable interactively, a group of shared variables
 interactively, or any number of shared variables programmatically. Use the following
 table to understand the methods of configuring a shared variable.

| Method | Recommended Use | Required Product |
| --- | --- | --- |
| Interactively by using the Shared Variable Properties dialog box | Configuring an individual shared variable | LabVIEW Development System, LabVIEW Datalogging and Supervisory Control (DSC) Module, or LabVIEW Real-Time Module |
| Interactively by using the Multiple Variable Editor window | Configuring multiple shared variables simultaneously | DSC Module or Real-Time Module |
| Programmatically by using the SharedVariableIO properties | Reading and writing engineering units, scales, and other information about the shared variable | DSC Module |

To delete a shared variable, right-click the shared variable in the Project
 Explorer window and select Remove from the
 shortcut menu.

Changes you make using the Shared Variable Properties dialog box, the
 Multiple Variable Editor window, or the shared variable
 properties affect the .lvlib file. Changes you make using the
 SharedVariableIO properties do not affect the LabVIEW project library
 (.lvlib). The SharedVariableIO properties affect the Shared
 Variable Engine (SVE) directly.

#### Configuring Shared Variables
 Interactively

You can configure shared variables interactively by using
 the Logging, Update Deadband, Alarming, Initial Value, Security, Scaling,
 Description, Real-Time FIFO, and Network pages of the Shared Variable
 Properties dialog box.

Note

#### Configuring Multiple Shared Variables
 Interactively

By using the Multiple Variable Editor
 window, you can configure multiple shared variables simultaneously and
 interactively. You can use the Multiple Variable Editor
 window to edit properties, such as alarming, logging, network, description, and
 scaling, for a large number of shared variables. You also can change the data type
 of multiple shared variables.

#### Configuring Shared Variables
 Programmatically

By using the SharedVariableIO properties, you can
 configure shared variables programmatically by editing many shared variable
 properties, such as alarming, logging, and scaling. You also can read shared
 variable information and read and configure network information
 programmatically.

Note

Variable Type

Network-Published

Variable

Shared Variable Properties

The following list describes the properties you can read and write. The
 shared variable properties that you can read and write depend on the data type of
 the shared variable and on your target and licensed product(s).

Shared variable information

Network information

Alarming

Logging

Scaling

You can configure SharedVariableIO properties for network-published shared
 variables only. Enable network publishing for a shared variable before you configure
 and read this shared variable.

- [Configuring Shared Variables Interactively](configuring-shared-variables-interactively.html)
- [Configuring Shared Variables Programmatically](configuring-shared-variables-programmatically.html)

Parent topic:

Shared Variable Properties

Related concepts:

- Shared Variables
- Supported Shared Variable Properties Based on Target and Products

Related tasks:

- Enabling Network Publishing for Shared Variables

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=configuring-alarms-for-boolean-shared-variabl.html language=enus -->
## TOPIC 00021: Configuring Alarms for Boolean Shared Variables

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `configuring-alarms-for-boolean-shared-variabl.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/configuring-alarms-for-boolean-shared-variabl.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: You can configure alarming for network-published shared variables only. Enable network publishing for a shared variable before you configure alarming for this shared variable.Complete the following steps to configure alarms for Boolean shared variables: Right-click a Boolean shared variable in the P

### Configuring Alarms for Boolean Shared Variables

You can configure alarming for network-published shared variables only. Enable
 network publishing for a shared variable before you configure alarming for this
 shared variable.

Complete the following steps to configure alarms for Boolean shared variables:

1. Right-click a Boolean shared variable in the Project
 Explorer window and select Properties
 from the shortcut menu to display the Shared Variable
 Properties dialog box.
2. Select Alarming to display the
 Alarming page.
3. On the Alarming page, place a checkmark in the Enable
 Alarming checkbox.
4. In the Alarms section, place a checkmark in the appropriate cell of the Enabled column for the type of alarm you want to enable.
5. Enter the name of the alarm in the appropriate cell of the Name column.
6. If you enabled the Boolean alarm, set the cell in the Alarm
 On column to Low to configure the shared
 variable to be in an alarm state when the value is FALSE. Set
 the cell to High to configure the shared variable to be
 in an alarm state when the value is TRUE.
7. In the appropriate cell of the Priority column, enter a
 priority for the alarm. The priority level can be 1–1,000,
 where 1,000 is the highest priority.
8. In the appropriate cell of the Ack Type column, select an acknowledging type.
9. In the appropriate cell of the Area column, enter a name for the area to which the alarm belongs.
10. In the appropriate cell of the Description column, enter a description of the alarm.
11. In the appropriate cell of the Log? column, place a checkmark in the
 checkbox to log alarm information to the database.
12. Click the OK button to close the Shared
 Variable Properties dialog box.

Note

Ack

Description

Set

Parent topic:

Use Alarms and Events in DSC Module Applications

Related tasks:

- Enabling Network Publishing for Shared Variables

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=configuring-alarms-for-numeric-shared-variabl.html language=enus -->
## TOPIC 00022: Configuring Alarms for Numeric Shared Variables

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `configuring-alarms-for-numeric-shared-variabl.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/configuring-alarms-for-numeric-shared-variabl.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: You can configure alarming for network-published shared variables only. Enable network publishing for a shared variable before you configure alarming for this shared variable. Complete the following steps to configure alarms for numeric shared variables: Right-click a numeric shared variable in the

### Configuring Alarms for Numeric Shared Variables

You can configure alarming for network-published shared variables only. Enable network publishing
 for a shared variable before you configure alarming for this shared variable.
 Complete the following steps to configure alarms for numeric shared variables:

1. Right-click a numeric shared variable in the Project
 Explorer window and select Properties
 from the shortcut menu to display the Shared Variable
 Properties dialog box.
2. Select Alarming to display the
 Alarming page.
3. On the Alarming page, place a checkmark in the Enable
 Alarming checkbox.
4. In the Alarms section, place a checkmark in the appropriate cell of the Enabled column for the type of alarm that you want to enable.
5. In the appropriate cell of the Name column, enter the name of the alarm.
6. If you enable a HI_HI, HI, LO, or LO_LO alarm, configure the following alarm
 properties:
  1. In the appropriate cell of the Level/Change
 column, enter the level that triggers the alarm condition. The shared
 variable alarm state remains inactive until the shared variable value
 equals or exceeds the Level/Change value.
  2. In the appropriate cell of the Deadband/Time
 column, enter the alarm deadband. Deadband/Time
 acts like a hysteresis. The Shared Variable Engine (SVE) does not clear
 an active alarm until the percentage difference between the new value
 and the previous value equals or exceeds the deadband. If you set the
 too high, the SVE might not clear the alarm.
7. If you enable a Rate of Change alarm, configure the following alarm
 properties:
  1. In the appropriate cell of the Level/Change
 column, enter the change that triggers the alarm condition.
 Level/Change specifies the value that the
 network shared variable value must change in the value of
 Deadband/Time to go into an alarm
 state.
  2. In the appropriate cell of the Deadband/Time
 column, enter the alarm time. Deadband/Time
 specifies the amount of time in which the network shared variable value
 must change at least the value of Level/Change to
 go into an alarm state.
8. In the appropriate cell of the Priority column, enter a priority for the
 alarm. The priority can be 1–1,000, where 1,000 is the highest priority.
9. In the appropriate cell of the Ack Type column, select an acknowledging type.
10. In the appropriate cell of the Area column, enter a name for the area to which the alarm belongs.
11. In the appropriate cell of the Description column, enter a description of the alarm.
12. In the appropriate cell of the Log? column, place a checkmark in the
 checkbox to log alarm information to the database.
13. Optional: 
 Place a checkmark in the Generate event on value change
 checkbox to generate events when the values of shared variables change.
14. Click the OK button to close the Shared
 Variable Properties dialog box.

Parent topic:

Use Alarms and Events in DSC Module Applications

Related concepts:

- Pass Data between LabVIEW and the Shared Variable Engine
- Supported Shared Variable Types

Related tasks:

- Enabling Network Publishing for Shared Variables

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=configuring-alarms-for-string-shared-variable.html language=enus -->
## TOPIC 00023: Configuring Alarms for String Shared Variables

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `configuring-alarms-for-string-shared-variable.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/configuring-alarms-for-string-shared-variable.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: You can configure alarming for network-published shared variables only. Enable network publishing for a shared variable before you configure alarming for this shared variable. Complete the following steps to configure alarms for string and custom shared variables: Right-click a string or custom shar

### Configuring Alarms for String Shared Variables

You can configure alarming for network-published shared variables only. Enable network publishing
 for a shared variable before you configure alarming for this shared variable.
 Complete the following steps to configure alarms for string and custom shared
 variables:

1. Right-click a string or custom shared variable in the Project
 Explorer window and select Properties
 from the shortcut menu to display the Shared Variable
 Properties dialog box.
2. Select Alarming to display the
 Alarming page.
3. Place a checkmark in the Enable Alarming checkbox.
4. In the Alarms section, place a checkmark in the appropriate cell of the Enabled column.
5. In the appropriate cell of Name column, enter the name of the alarm.
6. In the appropriate cell of the Priority column, enter a
 priority for the alarm. The priority level can be 1–1,000,
 where 1,000 is the highest priority.
7. In the appropriate cell of the Ack Type column, select an acknowledgement type.
8. In the appropriate cell of the Area column, enter a name for the area to which the alarm belongs.
9. In the appropriate cell of the Description column, enter a description of the alarm.
10. In the appropriate cell of the Log? column, place a checkmark to log
 alarm information to the database.
11. Optional: 
 Place a checkmark in the Generate event on value change
 checkbox to generate events when the values of shared variables change.
12. Click the OK button to close the Shared
 Variable Properties dialog box.

Parent topic:

Use Alarms and Events in DSC Module Applications

Related tasks:

- Enabling Network Publishing for Shared Variables

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=configuring-alarms-for-u32-bit-field-shared-v.html language=enus -->
## TOPIC 00024: Configuring Alarms for U32 Bit Field Shared Variables

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `configuring-alarms-for-u32-bit-field-shared-v.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/configuring-alarms-for-u32-bit-field-shared-v.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: You can configure alarming for network-published shared variables only. Enable network publishing for a shared variable before you configure alarming for this shared variable. Complete the following steps to configure alarms for bit array shared variables: Right-click a U32 Bit Field shared variable

### Configuring Alarms for U32 Bit Field Shared Variables

You can configure alarming for network-published shared variables only. Enable network publishing
 for a shared variable before you configure alarming for this shared variable.
 Complete the following steps to configure alarms for bit array shared variables:

1. Right-click a U32 Bit Field shared variable in the Project
 Explorer window and select Properties
 from the shortcut menu to display the Shared Variable
 Properties dialog box.
2. Select Alarming to display the Alarming page.
3. On the Alarming page, place a checkmark in the Enable
 Alarming checkbox.
4. In the Alarms section, place a checkmark in the appropriate cell of the Enabled column for the type of alarm that you want to enable for the bit array shared variable.
5. Set the appropriate cell of the Alarm On column to Any to configure the shared variable to be in an alarm state when any bit meets the alarm criteria. Set the cell to All to configure the shared variable to be in an alarm state when all bits meet the alarm criteria.
6. In the appropriate cell of the Invert column, enter 1 or
 0 for each bit to determine whether this bit meets the alarm criteria when high
 (1) or low (0). For example, if you enter 1 for a bit, this bit meets the alarm
 criteria when low. If you enter 0 for a bit, this bit meets the alarm criteria
 when high. In bit-wise terminology, the Shared Variable Engine (SVE) performs an
 XOR with the Invert value to produce the alarm state. The
 LabVIEW Datalogging and Supervisory Control (DSC) Module applies the
 Invert value to the scaled value after the DSC Module
 applies any relevant scaling masks.
7. In the appropriate cell of the Mask column, enter the bits that the DSC Module uses to calculate the alarm for the shared variable. LabVIEW uses bits that are 1 in the alarm calculation. Bits that are 0 do not cause an alarm, regardless of their value. In bit-wise terminology, the SVE performs an AND with the Mask value to produce the alarm state. The DSC Module applies the Mask value to the scaled value after applying any relevant scaling masks.
8. In the appropriate cell of the Priority column, enter a
 priority for the alarm. The priority level can be 1–1,000,
 where 1,000 is the highest priority.
9. In the appropriate cell of the Ack Type column, select an acknowledgement type.
10. In the appropriate cell of the Area column, enter a name for the area to which the alarm belongs.
11. In the appropriate cell of the Description column, enter a description of the alarm.
12. In the appropriate cell of the Log? column, place a checkmark in the
 checkbox to log alarm information to the database.
13. Click the OK button to close the Shared
 Variable Properties dialog box.

Parent topic:

Use Alarms and Events in DSC Module Applications

Related concepts:

- Pass Data between LabVIEW and the Shared Variable Engine

Related tasks:

- Enabling Network Publishing for Shared Variables

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=configuring-alarms.html language=enus -->
## TOPIC 00025: Configuring Alarms

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `configuring-alarms.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/configuring-alarms.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to configure alarms. Right-click a target or a LabVIEW project library in the Project Explorer window and select New»Variable from the shortcut menu to display the Shared Variable Properties dialog box. You also can right-click an existing shared variable in the Project

### Configuring Alarms

Complete the following steps to configure
 alarms.

1. Right-click a target or a LabVIEW project library in the Project
 Explorer window and select New»Variable
 from the shortcut menu to display the Shared Variable
 Properties dialog box. 
 You also can right-click an existing shared variable in the Project
 Explorer window and select Properties
 from the shortcut menu to display this dialog box.
2. Select Alarming from the list of this dialog box to
 display the Alarming page.
3. Place a checkmark in the Enable Alarming checkbox.
4. Place a checkmark in the cells of Enabled column for the alarms that you want to configure.
5. Set the alarm attributes in the Alarming section. The available
 attributes vary depending on the data type of the shared variable that you are
 configuring, for example, double, Boolean, bit array, and string.
6. Click the OK button to close the dialog box.

Note

Tools»Distributed System Manager

Parent topic:

Edit Shared Variable Properties

Related concepts:

- Supported Shared Variable Types

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=configuring-alarms_2.html language=enus -->
## TOPIC 00026: Configuring Alarms

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `configuring-alarms_2.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/configuring-alarms_2.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to configure alarms. Right-click a target or a LabVIEW project library in the Project Explorer window and select New»Variable from the shortcut menu to display the Shared Variable Properties dialog box. You also can right-click an existing shared variable in the Project

### Configuring Alarms

Complete the following steps to configure
 alarms.

1. Right-click a target or a LabVIEW project library in the Project
 Explorer window and select New»Variable
 from the shortcut menu to display the Shared Variable
 Properties dialog box. 
 You also can right-click an existing shared variable in the Project
 Explorer window and select Properties
 from the shortcut menu to display this dialog box.
2. Select Alarming from the list of this dialog box to
 display the Alarming page.
3. Place a checkmark in the Enable Alarming checkbox.
4. Place a checkmark in the cells of Enabled column for the alarms that you want to configure.
5. Set the alarm attributes in the Alarming section. The available
 attributes vary depending on the data type of the shared variable that you are
 configuring, for example, double, Boolean, bit array, and string.
6. Click the OK button to close the dialog box.

Note

Tools»Distributed System Manager

Parent topic:

Use Alarms and Events in DSC Module Applications

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=configuring-deployed-data-set-marking-i-o-ser.html language=enus -->
## TOPIC 00027: Configuring Deployed Data Set Marking I/O Servers

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `configuring-deployed-data-set-marking-i-o-ser.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/configuring-deployed-data-set-marking-i-o-ser.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to configure a deployed data set marking I/O server. Set the configure_start_end_condition parameter of this I/O server to TRUE. You can set this parameter by binding a shared variable to this parameter or by using the Distributed System Manager. Access the System Manage

### Configuring Deployed Data Set Marking I/O Servers

Complete the following steps to configure a
 deployed data set marking I/O server.

1. Set the configure_start_end_condition
 parameter of this I/O server to TRUE. You
 can set this parameter by binding a shared variable to this
 parameter or by using the Distributed System Manager. Access
 the System Manager by launching LabVIEW and selecting
 Tools»Distributed System
 Manager.
2. Configure the other parameters of this I/O server that you want to configure.
3. Set the configure_start_end_condition
 parameter to FALSE to apply the
 configurations for this I/O server.

Parent topic:

Interact with Data Using I/O Servers

Related concepts:

- Use Data Set Marking I/O Servers

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=configuring-local-opc-servers-to-work-with-op.html language=enus -->
## TOPIC 00028: Configuring Local OPC Servers to Work with OPC Client I/O Servers

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `configuring-local-opc-servers-to-work-with-op.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/configuring-local-opc-servers-to-work-with-op.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: You must verify the DCOM configuration for a local OPC server before you connect an OPC Client I/O server to the OPC server. The manufacturer recommends that you configure the OPC server to run with an identity of The interactive user.Complete the following steps to change and verify the identity se

### Configuring Local OPC Servers to Work with OPC Client I/O Servers

You must verify the DCOM configuration for a local OPC server before you connect an
 OPC Client I/O server to the OPC server. The manufacturer recommends that you
 configure the OPC server to run with an identity of The interactive
 user.

Complete the following steps to change and verify the identity setting for the OPC server:

1. Log in to Windows as an administrator.
2. In the Windows Control Panel, navigate to the Administrative Tools folder.
3. Double-click the Component Services shortcut to launch
 the Component Services utility. You also can launch the
 Component Services utility by selecting
 Start»Run, entering dcomcnfg
 in the command prompt, and clicking the OK button.
4. In the Component Services window, select
 Component Services»Computers»My Computer»DCOM Config
 from the Console Root tree to display the DCOM
 configurations on the computer.
5. Right-click the OPC server you installed on the computer and select
 Properties from the shortcut menu to display the
 Properties dialog box. Contact the OPC server vendor
 if you cannot find the OPC server in the DCOM Config
 list.
6. On the Identity page, click the The interactive user button.
7. Click the OK button to close the
 Properties dialog box.

You must relaunch or redeploy the OPC server before the change takes effect.

Parent topic:

Interact with Data Using I/O Servers

Related concepts:

- Use OPC Client I/O Servers

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=configuring-security-settings-for-front-panel.html language=enus -->
## TOPIC 00029: Configuring Security Settings for Front Panel Controls and Indicators

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `configuring-security-settings-for-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/configuring-security-settings-for-front-panel.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: You can configure security settings for an individual front panel object or for multiple front panel objects at one time. You can grant access to front panel objects for users and groups only. You cannot set security settings for a computer.You cannot add security to ActiveX controls. To add user or

### Configuring Security Settings for Front Panel Controls and Indicators

Note

To add user or group access for a front panel object, you must create or add the user or group to
 the Domain Account Manager.

Complete the following steps to configure security for a front panel object:

1. Right-click the control or indicator and select Properties from the shortcut menu.
2. Click the Security tab in the
 Properties dialog box.
3. Click the Add button to display the Add New
 Host/User dialog box and select a user or group for which you
 want to configure access rights.
4. Click the OK button to close the Add New
 Host/User dialog box and return to the
 Security tab of the Properties
 dialog box.
5. For each user or group, select an access level from the Access pull-down menu. You can select Full Access, Disabled (View Only), Disabled & Grayed Out, or No Access (Hidden).
6. Click the OK button to close the
 Properties dialog box.

Complete the following steps to configure security for multiple front panel objects at a
 time:

1. Select Tools»Security»Front Panel Security to open the Front
 Panel Security dialog box.
2. Select one or more objects from the Controls & Indicators list. This list contains the front panel objects and displays security status of these objects.
3. Click the Add button to open the Add New Host/User 
 dialog box and select a user or group for which you want to configure access
 rights.
4. Click the OK button to close the Add New Host/User 
 dialog box and return to the Front Panel Security dialog
 box.
5. Select an access level from the Access pull-down menu to set permissions for the currently selected user or group.
6. Click the OK button to close the Front Panel
 Security dialog box.

Note

No Access
 (Hidden)

Everyone

You also can copy and paste security settings between controls, indicators and VIs. Select an
 object and click the Copy ACL Value button. Then, select
 another object and click the Paste ACL Value button.

LabVIEW applies the most restrictive security mode for the control or indicator. For example, if
 you configure security for a control in the Security tab, and
 you also use a Property Node, such as the Disabled property, to affect the behavior
 of the same control, LabVIEW applies the most restrictive security mode. LabVIEW
 maintains both pieces of security information and applies them as necessary.

Parent topic:

Configure Security

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=configuring-security-settings-for-shared-vari.html language=enus -->
## TOPIC 00030: Configuring Security Settings for Shared Variables

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `configuring-security-settings-for-shared-vari.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/configuring-security-settings-for-shared-vari.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure security settings for an individual shared variable or for multiple shared variables at one time. You can also grant or deny access to shared variables for users, groups, and computers. By default, the access rights are unspecified. If you leave an access unspecified, that access i

### Configuring Security Settings for Shared Variables

Note

To add user or group access for a shared variable, the user or group first must be created in the
 Domain Account Manager.

Complete the following steps to configure security for a shared variable.

1. Right-click the shared variable in the Project Explorer window and select
 Properties from the shortcut menu to display the
 Shared Variable Properties dialog box.
2. Select Security to display the Security page.
3. Place a checkmark in the Enable Security checkbox.
4. Add users, groups, or hosts for the shared variable.
  - Add users or groups for the shared variable.
    1. Click the Add button and select
 User/Groups from the pull-down menu to
 display the Browse for Users/Groups dialog
 box.
    2. In this dialog box, select the user or group that you want to add.
 Press the <Ctrl> key and click additional items to select
 multiple items.
    3. Click the OK button to close this dialog box
 and add the users and/or groups to the
 Security page.
  - Add a host for the shared variable.
    1. Click the Add button and select
 Host from the pull-down menu. A new host
 appear on the Security page.
    2. Enter the computer name or IP address of the host computer in the
 User/Group/Host column.
5. Set permissions for the users, groups, and hosts. Double-click the cells in the Read
 Access and Write Access columns and select
 permissions from the pull-down menus. If you want to grant the access, select
 Grant from the pull-down menu. If you want to deny the
 access, select Deny from the pull-down menu.
6. Click the OK button to close the Shared Variable
 Properties dialog box.

Complete the following steps to configure security for multiple shared variables at a time:

1. Right-click a LabVIEW project library or the shared variables you want to configure in the
 Project Explorer window and select Multiple
 Variable Editor from the shortcut menu to display the
 Multiple Variable Editor window.
2. Select all of the cells in the Security:Enable column.
3. Click a cell in the Security:Enable column and select on from the pull-down list that appears. An additional Security:ACL option appears as a column in the table.
4. Select all of the cells in the Security:ACL column.
5. Click a cell in the Security:ACL column to display the Configure button.
6. Click the Configure button to display the ACL
 Configuration dialog box.
7. Click the Add button to display the Add New
 Host/User dialog box. You can use the dialog box to select a user,
 group, or host computer for which you want to configure access rights.
8. Select a user or group from the Users and groups list, or enter the computer or IP address of the computer in the Host text box.
9. Click the OK button to close the Add New Host/User 
 dialog box and return to the ACL Configuration dialog
 box.
10. In the Permissions list, select a permission.
11. If you want to grant the selected user this permission, place a checkmark in the Grant checkbox. If you want to deny the selected user this permission, place a checkmark in the Deny checkbox.
12. Click the OK button to close the ACL Configuration 
 dialog box and return to the Multiple Variable Editor 
 window.
13. Click the Done button to close the Multiple Variable
 Editor window.

Parent topic:

Configure Security

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=configuring-shared-variables-interactively.html language=enus -->
## TOPIC 00031: Configuring Shared Variables Interactively

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `configuring-shared-variables-interactively.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/configuring-shared-variables-interactively.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: You can configure shared variables interactively by using the Shared Variable Properties dialog box where you can edit the shared variable properties, such as logging, update deadband, alarming, scaling, initial value, description, and security, for network-published shared variables only. Complete

### Configuring Shared Variables Interactively

You can configure shared variables interactively by using the Shared
 Variable Properties dialog box where you can edit the shared
 variable properties, such as logging, update deadband, alarming, scaling, initial
 value, description, and security, for network-published shared variables only.

Complete the following steps to configure a shared variable interactively:

1. Right-click a shared variable in the Project Explorer
 window and select Properties from the shortcut menu to
 display the Shared Variable Properties dialog box.
2. Select one of the following options in the listbox of the Shared
 Variable Properties dialog box to display the properties that
 you want to edit: 
 **Logging**—Displays properties that describe logging resolution, logging
 deadband, and other logging settings for a shared variable.
 **Update Deadband**—Displays properties that describe the deadband ranges for a shared
 variable.
 **Alarming**—Displays properties that describe abnormal process conditions for a
 given shared variable.
 **Scaling**—Displays properties that describe which scaling function to apply to
 a shared variable value.
 **Initial Value**—Displays properties that describe the initial values for a shared
 variable.
 **Description**—Displays properties that describe a shared variable.
 **Security**—Displays properties that describe security settings for a shared
 variable.
3. After deploying the shared variable, use the Distributed System Manager to test
 the shared variable configuration and make sure you are reading and writing data
 properly with servers. Select Tools»Distributed System
 Manager to launch the System Manager.

You also can use the SharedVariableIO properties to configure shared variables programmatically.

Parent topic:

Configure Shared Variables

Related concepts:

- Shared Variable Properties

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=configuring-shared-variables-programmatically.html language=enus -->
## TOPIC 00032: Configuring Shared Variables Programmatically

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `configuring-shared-variables-programmatically.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/configuring-shared-variables-programmatically.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: You can configure a shared variable programmatically by using the SharedVariableIO properties which you can configure for network-published shared variables only.Enable network publishing for a shared variable before you configure this shared variable.Complete the following steps to configure a shar

### Configuring Shared Variables Programmatically

You can configure a shared variable programmatically by using the SharedVariableIO
 properties which you can configure for network-published shared variables only.

Enable network publishing for a shared variable before you configure this shared variable.

Complete the following steps to configure a shared variable programmatically:

1. Create and deploy a shared variable.
2. Add a shared variable constant on the block diagram.
3. Click the down arrow on the shared variable constant and select or browse to a shared variable
 to configure.
4. Right-click the shared variable constant and select
 Create»Property from the shortcut menu.
5. Select the property you want to configure. 
 A Property Node appears with the property you selected.Note To write data to the shared
 variable properties, right-click the Property Node and select
 Change To Write from the shortcut menu. To read
 data from shared variable properties, right-click the Property Node and
 select Change To Read from the shortcut menu. Some
 properties are read-only properties. Refer to the characteristics of each
 property to determine whether the property is read-only.
6. Wire the shared variable constant to the Property Node.

Parent topic:

Configure Shared Variables

Related tasks:

- Enabling Network Publishing for Shared Variables
- Deploying a Shared Variable

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=create-and-configure-user-and-group-accou.html language=enus -->
## TOPIC 00033: Create and Configure User and Group Accounts

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `create-and-configure-user-and-group-accou.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/create-and-configure-user-and-group-accou.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Domain Account Manager to create and configure domain users and groups, assign users to one or more groups, and manage security accounts for LabVIEW Datalogging and Supervisory Control (DSC) Module applications.Only Administrators or members of the Administrators group can create, revise, or

### Create and Configure User and Group
 Accounts

Use the Domain Account Manager to create and configure domain users and groups,
 assign users to one or more groups, and manage security accounts for
 LabVIEW Datalogging and Supervisory Control (DSC) Module
 applications.

Only Administrators or members of the Administrators group can create, revise, or delete system
 user accounts. Use the Security VIs to access user
 information programmatically.

Use the Domain Account Manager to export and import a local domain so you
 can migrate the security settings when you deploy LabVIEW applications to
 target computers.

Parent topic:

Configure Security

Related concepts:

- Deploy a DSC Module Application

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=create-epics-client-i-o-servers-dsc-module.html language=enus -->
## TOPIC 00034: Create EPICS Client I/O Servers

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `create-epics-client-i-o-servers-dsc-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/create-epics-client-i-o-servers-dsc-module.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can create EPICS Client I/O servers to monitor process variables that an EPICS server, or Input/Output Controller (IOC), publishes using the Channel Access network protocol, and to read process variables from and write process variables directly to an IOC using network-published shared variables

### Create EPICS Client I/O Servers

Note

EPICS: Input /
 Output Controller Application Developer's Guide

Argonne National Laboratory

You can create EPICS Client I/O Servers either interactively or programmatically.

- [Creating EPICS Client I/O Servers Interactively](create-epics-client-io-servers-interact.html)
- [Creating EPICS Client I/O Servers Programmatically](create-epics-client-io-servers-program.html)

Parent topic:

Interact with Data Using I/O Servers

Related concepts:

- Use EPICS Client I/O Servers

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=create-epics-client-io-servers-interact.html language=enus -->
## TOPIC 00035: Creating EPICS Client I/O Servers Interactively

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `create-epics-client-io-servers-interact.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/create-epics-client-io-servers-interact.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to create an EPICS Client I/O server interactively. In the Project Explorer window, right-click a target, such as the My Computer target, and select New»I/O Server from the shortcut menu. In the Create New I/O Server dialog box, select EPICS Client and click the Continue

### Creating EPICS Client I/O Servers
 Interactively

Complete the following steps to create an EPICS Client I/O
 server interactively.

1. In the Project Explorer window, right-click a target,
 such as the My Computer target, and select
 New»I/O Server from the shortcut menu.
2. In the Create New I/O Server dialog box, select
 EPICS Client and click the
 Continue button.
3. In the Configure EPICS Client I/O Server dialog box,
 click the Add Record button to add a process variable you
 want to monitor. The Configure EPICS Client I/O Server
 dialog box organizes process variables first by record and then by field. 
 Note The
 manufacturer recommends limiting the number of process variables in one
 EPICS Client I/O server to 2,000. Create multiple EPICS Client I/O servers
 if you want to monitor more than 2,000 process variables.
4. Optional: 
 You also can click the Import File button to load
 multiple process variables stored in a .db, or record instance,
 file. 
 You typically create a .db file when you configure an
 IOC.Note When
 you import multiple process variables, LabVIEW imports only the
 VAL field of the process variables.
5. Specify the Name of the record of the process variable
 you want to monitor. 
 Record names within the same I/O server must be unique.
6. Select the field of the process variable and specify the
 Name, Data type, and
 Access type of the field. 
 Field names under the same record must be unique.
7. Click the Add Field button if you want to add another
 field under an existing record.
8. Repeat steps 3 through 6 for as many process variables as you want to
 monitor.
9. Click the OK button.

After you create an EPICS Client I/O server, you can use the View I/O
 Items dialog box to view the process variables the I/O server
 monitors. To display the View I/O Items dialog box,
 right-click the I/O server in the Project Explorer window and
 select View I/O Items from the shortcut menu.

Parent topic:

Create EPICS Client I/O Servers

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=create-epics-client-io-servers-program.html language=enus -->
## TOPIC 00036: Creating EPICS Client I/O Servers Programmatically

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `create-epics-client-io-servers-program.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/create-epics-client-io-servers-program.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to create an EPICS Client I/O server programmatically. Add the Create EPICS Client VI to the block diagram. Right-click the EPICS Client URL in input of the Create EPICS Client VI and select Create»Constant or Create»Control from the shortcut menu. In the constant or con

### Creating EPICS Client I/O Servers
 Programmatically

Complete the following steps to create an EPICS Client I/O
 server programmatically.

1. Add the Create EPICS Client VI to the block diagram.
2. Right-click the EPICS Client URL in input of the
 Create EPICS Client VI and select
 Create»Constant or
 Create»Control from the shortcut menu. In the
 constant or control, specify the location to create the EPICS Client I/O
 server.
3. Add the Add Record VI to the block diagram.
4. Wire the EPICS Client ref output of the Create
 EPICS Client VI to the EPICS Client ref in
 input of the Add Record VI.
5. Right-click the record name input of the Add
 Record VI and select Create»Constant or
 Create»Control from the shortcut menu. In the
 constant or control, specify the name of the record you want to add to the EPICS
 Client I/O server.
6. Add the Add Field VI to the block diagram.
7. Wire the EPICS Client ref out output of the Add
 Record VI to the EPICS Client ref in input
 of the Add Field VI.
8. Wire the constant or control of the record name input of
 the Add Record VI to the record name
 input of the Add Field VI.
9. Right-click the field name input of the Add
 Field VI and select Create»Constant or
 Create»Control from the shortcut menu. In the
 constant or control, specify the name of the field you want to add to the EPICS
 Client I/O server.
10. Optional: 
 Right-click the access type input of the Add
 Field VI and select Create»Constant or
 Create»Control from the shortcut menu. In the
 constant or control, select the access type for the field.
11. Optional: 
 Right-click the data type input of the Add
 Field VI and select Create»Constant or
 Create»Control from the shortcut menu. In the
 constant or control, select the data type for the field.
12. Add the Deploy EPICS Client VI to the block diagram.
13. Wire the EPICS Client ref out output of the Add
 Field VI to the EPICS Client ref in input
 of the Deploy EPICS Client VI.
14. Run this VI to create and deploy the EPICS Client I/O server and to subscribe
 to the process variables on the EPICS network.

Parent topic:

Create EPICS Client I/O Servers

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=create-epics-server-i-o-servers-dsc-module.html language=enus -->
## TOPIC 00037: Create EPICS Server I/O Servers (DSC Module or Real-Time Module)

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `create-epics-server-i-o-servers-dsc-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/create-epics-server-i-o-servers-dsc-module.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can create EPICS Server I/O servers to publish shared variables as Process Variables (PVs) by using the Channel Access (CA) network protocol.You can create EPICS Server I/O servers to publish I/O Variables (IOVs) as PVs by using the CA network protocol.Use EPICS Client I/O servers, or third-part

### Create EPICS Server I/O Servers (DSC Module or
 Real-Time Module)

You can create EPICS Server I/O servers to publish shared variables as Process Variables
 (PVs) by using the Channel Access (CA) network protocol.

You can create EPICS Server I/O servers to publish I/O Variables (IOVs) as PVs by using the CA
 network protocol.

Use EPICS Client I/O servers, or third-party EPICS clients, to monitor and update the published
 PVs after you deploy the processes that contain the shared variables and EPICS Server
 I/O servers.

- [Creating EPICS Server I/O Servers Interactively](create-epics-server-io-servers-interact.html)
- [Creating EPICS Server I/O Servers Programmatically](create-epics-server-io-servers-program.html)

Parent topic:

Interact with Data Using I/O Servers

Related concepts:

- Use EPICS Server I/O Servers
- Use EPICS Client I/O Servers

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=create-epics-server-io-servers-interact.html language=enus -->
## TOPIC 00038: Creating EPICS Server I/O Servers Interactively

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `create-epics-server-io-servers-interact.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/create-epics-server-io-servers-interact.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to create an EPICS Server I/O server interactively. In the Project Explorer window, right-click a target, such as the My Computer target, and select New»I/O Server from the shortcut menu. In the Create New I/O Server dialog box, select EPICS Server and click the Continue

### Creating EPICS Server I/O Servers
 Interactively

Complete the following steps to create an EPICS Server I/O
 server interactively.

1. In the Project Explorer window, right-click a target,
 such as the My Computer target, and select
 New»I/O Server from the shortcut menu.
2. In the Create New I/O Server dialog box, select
 EPICS Server and click the
 Continue button.
3. In the Configure EPICS Server I/O Server dialog box,
 click the Add/Remove Variables button to display the
 Add/Remove Variables dialog box. 
 Note Use the
 Configure EPICS Server I/O Server dialog box to
 configure new and existing EPICS Server I/O servers. You can launch this
 dialog box by right-clicking an EPICS Server I/O server and selecting
 Properties from the shortcut menu.
4. In the Access type pull-down menu, specify the access
 type for the shared variables that you want to add.
5. In the Add/Remove Variables dialog box, select the
 shared variables that you want to publish and click the
 Add button to add these shared variables to the
 Added Variables list. 
 Press the Ctrl key to select multiple shared
 variables.Note Select a target and click the Add All button to add
 all supported shared variables under this target. You can select a shared
 variable from the Added variables list and click the
 Remove button to remove the shared variable from
 this list. You also can click the Remove All button
 to remove all shared variables from this list.
6. Click the OK button to add the shared variables to the
 Configure EPICS Server I/O Server dialog box.
7. Optional: 
 Triple-click a cell in the PV field to customize PV
 names for the added shared variables. 
 Note Do not use spaces in the customized PV names. Otherwise,
 LabVIEW reports these PV names as invalid PV names.
8. Optional: 
 Click a cell in the Access type fields to customize
 access types for the added shared variables.
9. Click the OK button to create the EPICS Server I/O
 server.

Parent topic:

Create EPICS Server I/O Servers (DSC Module or Real-Time Module)

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=create-epics-server-io-servers-program.html language=enus -->
## TOPIC 00039: Creating EPICS Server I/O Servers Programmatically

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `create-epics-server-io-servers-program.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/create-epics-server-io-servers-program.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to create an EPICS Server I/O server programmatically. Add the Create EPICS Server VI to the block diagram. Right-click the EPICS Server URL in input of the Create EPICS Server VI and select Create»Constant or Create»Control from the shortcut menu. In the constant or con

### Creating EPICS Server I/O Servers
 Programmatically

Complete the following steps to create an EPICS Server I/O
 server programmatically.

1. Add the Create EPICS Server VI to the block diagram.
2. Right-click the EPICS Server URL in input of the
 Create EPICS Server VI and select
 Create»Constant or
 Create»Control from the shortcut menu. In the
 constant or control, specify the location to create the EPICS Server I/O
 server.
3. Add the Create PV VI to the block diagram.
4. Wire the EPICS Server ref output of the Create
 EPICS Server VI to the EPICS Server ref in
 input of the Create PV VI.
5. Right-click the variable path input of the
 Create PV VI and select
 Create»Constant or
 Create»Control from the shortcut menu. In the
 constant or control, specify the path of the shared variable you want to publish
 to the EPICS Server I/O server.
6. Optional: 
 Right-click the PV name input of the Create
 PV VI and select Create»Constant or
 Create»Control from the shortcut menu. In the
 constant or control, specify the name of the process variable for the shared
 variable you want to publish.
7. Optional: 
 Right-click the access type input of the Create
 PV VI and select Create»Constant or
 Create»Control from the shortcut menu. In the
 constant or control, select the access type for the process variable.
8. Optional: 
 Specify the data type of the process variable by using one of the following
 methods: 
 Note If the shared
 variable exists, you do not need to wire the data
 type input.
 Wire a data type control or constant, such as a numeric constant, with a
 default value to the data type input of the
 Create PV VI. The constant or control you wire to
 the data type input specifies the data type of
 the process variable.
 Wire the shared variable reference to the Variable Property Node, select
 the Data Type property, and wire the Data Type
 output of the Variable Property Node to data type
 input of the Create PV VI.
9. Add the Deploy EPICS Server VI to the block diagram.
10. Wire the EPICS Server ref out output of the
 Create PV VI to the EPICS Server ref
 in input of the Deploy EPICS Server VI.
11. Run this VI to create and deploy the EPICS Server I/O server and to create a
 process variable for the shared variable you publish to the EPICS Server I/O
 server.

Parent topic:

Create EPICS Server I/O Servers (DSC Module or Real-Time Module)

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=create-pipe-networks-with-multi-segment-pip.html language=enus -->
## TOPIC 00040: Create Pipe Networks with Multi-Segment Pipe Controls

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `create-pipe-networks-with-multi-segment-pip.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/create-pipe-networks-with-multi-segment-pip.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Multi-Segment Pipe control to represent real-world pipe networks that you need to monitor.By default, when you add the Multi-Segment Pipe control to the front panel window, an s-shaped pipe network appears. This pipe network contains three pipe segments, two flanges, and two elbows, as shown

### Create Pipe Networks with Multi-Segment Pipe
 Controls

Use the Multi-Segment Pipe control to represent real-world pipe networks that you need to
 monitor.

By default, when you add the Multi-Segment Pipe control to the front panel window, an s-shaped
 pipe network appears. This pipe network contains
 three pipe segments, two flanges, and two elbows,
 as shown in the following figure. You can add pipe
 segments to this pipe network, remove pipe
 segments, and change the direction in which the
 flanges point.

The following figure illustrates the pipe network with three segments:

[IMAGE alt='image' src='GUID-4B3EC5EF-1E2A-4337-B1B7-D13DF6CA8CB6-a5.gif']

The Multi-Segment Pipe control is a Boolean control that uses two different colors to represent
 TRUE and FALSE values. Therefore, you also can
 change the color of a pipe network to customize what the pipe network represents. For
 example, you might use the color blue to represent cold water and the color red to
 represent hot water flowing through the pipe network.

The following list provides tips for modifying a pipe network:

- To add pipe segments to a pipe network, right-click a pipe segment and select Add
 Horizontal Pipe Segment or Add Vertical Pipe
 Segment from the shortcut menu. You also can press the
 Ctrl key and click a horizontal pipe segment to add a
 vertical pipe segment to the pipe network. Press the Ctrl key
 and click a vertical pipe segment to add a horizontal pipe segment to the pipe
 network.
- To change the direction in which a flange points, press the Ctrl key and
 click the flange. If you click the top half of a flange pointing left or right, the
 flange points up. If you click the bottom half of a flange pointing left or right,
 the flange points down. Similarly, if you click the right half of a flange pointing
 up or down, the flange points right. If you click the left half of a flange pointing
 up or down, the flange points left. Changing the direction in which a flange points
 also adds a pipe segment to the pipe network.You also can right-click a flange
 pointing right or left and select Add "Up" Pipe Segment or
 Add "Down" Pipe Segment from the shortcut menu to change
 the direction in which a flange points. Right-click a flange pointing up or down and
 select Add "Left" Pipe Segment or Add "Right" Pipe
 Segment from the shortcut menu.
- To remove pipe segments from a pipe network, right-click a pipe segment and select Delete Pipe Segment from the shortcut menu.
- To select an entire pipe network, click and drag the cursor over any portion of the pipe network.
- To change the length of a pipe segment, click and drag a flange in the direction in which you want to lengthen or shorten the adjoining pipe segment. You also can click and drag a horizontal pipe segment to change the length of the adjoining vertical pipe segments, or you can click and drag a vertical pipe segment to change the length of the adjoining horizontal pipe segments.
- To change the radius of the pipe segments in a pipe network, move the cursor over any pipe
 segment to display resizing handles. Click and
 drag a resizing handle to adjust the radius of the
 pipe segment. You also can set the pipe radius
 programmatically. The pipe radius is the distance,
 in pixels, between the center of a pipe segment to
 the edge of the pipe segment. All pipe segments in
 the pipe network have the same radius. Note The
 maximum pipe radius is one pixel less than the
 radius of the narrowest flange. The minimum pipe
 radius is five pixels.
- To change the radius or depth of a flange, move the cursor over the flange to display resizing
 handles. Click and drag a resizing handle to adjust the radius or depth of the
 flange. You also can set the flange dimensions programmatically. When you
 programmatically set the radius of the flange, you actually specify the flange
 width. The radius of the flange is equal to the pipe radius plus the flange width.
 The flange width is the distance, in pixels, from the edge of the adjoining pipe
 segment to the edge of the flange. The flange depth is the distance, in pixels, from
 the end of the adjoining pipe segment to the end of the flange. Note The maximum flange width is 500
 pixels. The minimum flange width is one pixel. The maximum flange depth is 50
 pixels. The minimum flange depth is four pixels.
- To change the color of an entire pipe network, use the Operating tool to click any part of the
 pipe network. The default colors are grey and
 blue. You can change these two colors in edit mode
 by using the Coloring tool to right-click the
 Multi-Segment Pipe control and to select a
 different color from the color picker. You also
 can specify the colors of the pipe network
 programmatically.

The following figure illustrates the pipe radius, flange width, and flange depth:

[IMAGE alt='image' src='GUID-B497CC6F-1BE8-4B4F-A7A5-B9C88889273F-a5.gif']

You also can use the 2D Pipe controls on the 2D Controls palette and the 3D Pipes controls on the
 3D Controls palette to create pipe networks. The
 advantage of using the Multi-Segment Pipe control
 is that you can reshape and resize an entire pipe
 network interactively. In addition, you need to
 use only one control to create an entire pipe
 network. If you use the 2D Pipe or 3D Pipes
 controls, you must add and resize multiple pipe
 segments, flanges, and elbows individually to
 create a pipe network. You also must ensure that
 you properly align and connect the pipe segments,
 flanges, and elbows when you add, delete, or
 resize any part of the pipe network.

The Multi-Segment Pipe control does not support tees, or branches, in the pipe network. However,
 you can use tees with the Multi-Segment Pipe
 control to join two pipe networks. Similarly, you
 can use any of the 2D Controls or 3D Controls,
 such as pumps and valves, to add functionality to
 or to extend the pipe network you created using
 the Multi-Segment Pipe control.

Parent topic:

Displaying and Controlling Data

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=create-shared-variables.html language=enus -->
## TOPIC 00041: Create Shared Variables

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `create-shared-variables.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/create-shared-variables.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Datalogging and Supervisory Control Module allows you to create shared variables in several ways. Create shared variables in the Shared Variable Properties dialog box.You can use the features the LabVIEW Datalogging and Supervisory Control (DSC) Module adds for network-published shared variables

### Create Shared Variables

The Datalogging and Supervisory Control Module allows you to create shared
 variables in several ways.

- Create shared variables in the Shared Variable Properties dialog box.

Note

- Create multiple shared variables at one time in the Batch Variable
 Creation dialog box, available by right-clicking
 a LabVIEW project library in the Project
 Explorer window and selecting Create
 Variables from the shortcut menu.
- Create shared variables dynamically using the Engine Control VIs.

Note

Create Process

Parent topic:

Shared Variables

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=creating-a-citadel-odbc-data-source.html language=enus -->
## TOPIC 00042: Creating a Citadel ODBC Data Source

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `creating-a-citadel-odbc-data-source.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/creating-a-citadel-odbc-data-source.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: When you install the LabVIEW Datalogging and Supervisory Control (DSC) Module, the DSC Module automatically creates a Citadel database, an ODBC data source, and a default System DSN with the same name as the Citadel database. If you remove a database from the ODBC connection, the DSC Module removes

### Creating a Citadel ODBC Data Source

When you install the LabVIEW Datalogging and Supervisory Control (DSC) Module, the
 DSC Module automatically creates a Citadel database, an ODBC data
 source, and a default System DSN with the same name as the
 Citadel database.

If you remove a database from the ODBC connection, the DSC Module removes the
 corresponding DSN too, unless you modified the System DSN manually in the ODBC
 setup.

Complete the following steps to create a Citadel ODBC data source
 to use with the DSC Module:

1. Shut down all ODBC applications, such as databases, spreadsheets, word processors, and Microsoft Query, before you run the ODBC applet.
2. In the Windows Control Panel, navigate to the Administrative Tools folder.
3. Double-click the Data Sources (ODBC) shortcut to launch the Microsoft ODBC Data Source Administrator.
4. Click the User DSN tab or the System DSN tab, depending on which type of data source you want to create. User DSNs are visible only to the user who created them on the current computer. System DSNs are available to all users on the current computer. Click the Add button.
5. Select Citadel 5 Database, then click the
 Finish button.
6. In the Citadel 5 ODBC Setup dialog box enter values in the
 Data Source Name, Description,
 and Database URL fields.. 
 The Data Source Name is the name that ODBC
 applications use to select the data source and must be different from
 any other ODBC data source name.
 Description is a free-form text string you can
 enter to describe the data source.
 Database URL is the computer and database name
 for the data you intend to access, such as \\computer\database.
7. Click the Test Connection button to test the connection to the database.
8. Click the OK button in the Citadel 5 ODBC
 Setup dialog box, then click OK in the
 ODBC Data Source Administrator dialog box. The DSC
 Module creates a default System DSN and a new Citadel
 database, both with the name you specified in the Data Source
 Name field.

Note

Maximum Column Name Length

Maximum Column Name Length

Some ODBC clients do not handle certain special characters in column and table names. The
 following table lists special characters in shared variable names and data set names
 and their replacements:

| Special Character | Converted Character |
| --- | --- |
| . | @ |
| \\ | / |

The special characters changed in ODBC 5. If you convert SQL queries from an earlier version of the ODBC driver, you might have to rewrite any SQL queries you set up in earlier processes.

Parent topic:

Logging Historical Data to the Citadel Database

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=creating-a-data-link-for-the-odbc-data-source.html language=enus -->
## TOPIC 00043: Creating a Data Link for the ODBC Data Source

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `creating-a-data-link-for-the-odbc-data-source.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/creating-a-data-link-for-the-odbc-data-source.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: To access Citadel data from an ADO client, you need a data link to ODBC. If you are able to create the data link from within your ADO client, you might be required to create the data link multiple times. Complete the following steps to create a data link once that can be stored anywhere on your syst

### Creating a Data Link for the ODBC Data
 Source

To access Citadel data from an ADO client, you need a data link to ODBC. If
 you are able to create the data link from within your ADO client, you might be
 required to create the data link multiple times. Complete the following steps to
 create a data link once that can be stored anywhere on your system or network:

1. Create a Citadel 5 ODBC data source if you do not have
 one.
2. Create a new text document with a .txt extension.
3. Open this text document in Notepad and select File»Save
 as to display the Save as dialog
 box.
4. In this dialog box, select All Files from the Save as type pull-down menu.
5. In the File name pull-down menu, enter a file name with
 a .udl extension, for example
 data_link.udl
6. Right-click the .udl file and select
 Properties from the shortcut menu. In the dialog box
 that appears, click the Provider tab and select
 Microsoft OLE DB Provider for ODBC Drivers.
7. Click the Next button or the
 Connection tab and select the Citadel 5
 ODBC data source name.
8. Click the OK button.

Parent topic:

Logging Historical Data to the Citadel Database

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=creating-data-sets-for-logging.html language=enus -->
## TOPIC 00044: Creating Data Sets for Logging

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `creating-data-sets-for-logging.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/creating-data-sets-for-logging.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: You must create shared variables before you can create data sets for logging. You also must enable the logging property of a shared variable before you can configure a data set marking I/O server. Use the LabVIEW Datalogging and Supervisory Control (DSC) Module to create a data set of multiple share

### Creating Data Sets for Logging

You must create shared variables before you can create data sets for logging. You also must
 enable the logging property of a shared variable before you can configure a data set
 marking I/O server. Use the LabVIEW Datalogging and Supervisory Control (DSC) Module
 to create a data set of multiple shared variables for logging.

Complete the following steps to create a data set for logging:

1. In the Project Explorer window, right-click a target,
 such as the My Computer target, and select
 New»I/O Server from the shortcut menu.
2. In the Create New I/O Server dialog box, select
 Data Set Marking and click the
 Continue button.
3. On the Definition page of the Configure Data
 Set Marking I/O Server dialog box, select a shared variable from
 the Data set ID pull-down menu. 
 The DSC Module uses this shared variable as the name of the reference for the
 data set. The Data set ID is a string or analog
 network-published shared variable from the same LabVIEW project library. When
 you start logging a data set, the value of the Data set
 ID at that time becomes the identifier of the data set run. For
 example, a Data set ID might be the serial number of a
 unit under test, and the data set for that serial number might consist of the
 traces logged during testing of that unit. Because the same unit might be tested
 more than once, the DSC Module might use that Data set ID
 more than once, so the DSC Module creates a unique internal identification value
 for every run. However, you might want to assign a unique Data set
 ID for each run. For example, you can combine a serial number
 with a timestamp.
4. Use the Start when and End when
 options to specify the type of start and end conditions and to specify a shared
 variable to monitor for the fulfillment of that condition. 
 When the start condition occurs, a new run starts, if the previous run
 has ended. When the end condition occurs, the run ends.
5. Click the Shared Variables tab.
6. Click the Add Shared Variable button to display the
 Add Shared Variables dialog box.
7. Select the shared variables you want to include in the data set.
8. Click the Add button. The shared variables you selected appear in the Currently Selected Shared Variables list on the Shared Variables page.
9. Optional: 
 Use the Advanced page to enter the name of the equipment
 and corresponding description for the equipment used in the data set.
10. Click the OK button.

Note

Parent topic:

Logging Historical Data to the Citadel Database

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=creating-modbus-i-o-servers-dsc-module-or-rea.html language=enus -->
## TOPIC 00045: Creating Modbus I/O Servers (DSC Module or Real-Time Module)

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `creating-modbus-i-o-servers-dsc-module-or-rea.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/creating-modbus-i-o-servers-dsc-module-or-rea.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: After you create a Modbus I/O server, you can create shared variables and bind the shared variables to Modbus I/O server data items.(DSC Module) You can create a Modbus or Modbus Slave I/O server interactively or programmatically. (Real-Time Module) You can create a Modbus or Modbus Slave I/O server

### Creating Modbus I/O Servers (DSC Module or
 Real-Time Module)

After you create a Modbus I/O server, you can create shared variables and bind the shared
 variables to Modbus I/O server data items.

(DSC Module) You can create a Modbus or Modbus Slave I/O server interactively or
 programmatically.

Note

Create Bound Variables

Note

CommFail

ErrorStatus

#### Creating Modbus I/O Servers
 Interactively

Complete the following steps to create a Modbus or Modbus Slave I/O server
 interactively:

1. In the Project Explorer window, right-click a target, such as the
 My Computer target, and select New»I/O
 Server from the shortcut menu.
2. In the Create New I/O Server dialog box, select
 Modbus or Modbus Slave and click the
 Continue button.
3. In the Configure Modbus I/O Server or Configure Modbus Slave
 I/O Server dialog box, select the communication protocol, or
 Model , and configure the Communication
 Settings you want to use.
4. Click the Advanced button of the
 Configure Modbus I/O Server dialog box to configure the
 Maximum Data Points Per Command .
5. Click the OK button.

#### Creating Modbus I/O Servers
 Programmatically

Complete the following steps to create a Modbus or Modbus Slave I/O server
 programmatically:

1. Place the Create and Configure IO Server Express VI on the block
 diagram.
2. In the configuration dialog box that appears, select Modbus or
 Modbus Slave from the I/O server type 
 pull-down list.
3. Click the Set Attributes button to display the Configure
 Modbus I/O Server or Configure Modbus Slave I/O
 Server dialog box. Note If you click the OK button before you set the
 attributes for this I/O server instance, LabVIEW automatically displays the
 Configure Modbus I/O Server or Configure Modbus
 Slave I/O Server dialog box.
4. In the Configure Modbus I/O Server or Configure Modbus Slave
 I/O Server dialog box, configure the settings for the new I/O server.
5. Click the Advanced button of the
 Configure Modbus I/O Server dialog box to configure the
 Maximum Data Points Per Command .
6. Click the OK button.

Parent topic:

Interact with Data Using I/O Servers

Related concepts:

- Pass Data between LabVIEW and the Shared Variable Engine
- Modbus Communication in LabVIEW
- Use Modbus I/O Servers

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=creating-on-input-change-i-o-servers.html language=enus -->
## TOPIC 00046: Creating On Input Change I/O Servers

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `creating-on-input-change-i-o-servers.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/creating-on-input-change-i-o-servers.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following guidelines to create an on input change I/O server.Create a custom I/O server in the Project Explorer window.Configure the on input change I/O server by using the Custom VI-based Server – On Input Change wizard.Set the initial values for the inputs of the on input change I/O server

### Creating On Input Change I/O Servers

Use the following guidelines to create an on input change I/O server.

1. Create a custom I/O server in the Project Explorer window.
2. Configure the on input change I/O server by using the Custom VI-based Server – On
 Input Change wizard.
3. Set the initial values for the inputs of the on input change I/O server.

To create another on input change I/O server by using the same custom I/O server, you do not need
 to create the custom I/O server again. In this situation, you can set the initial values for
 the inputs to reconfigure the I/O server.

#### Creating a New On Input Change I/O Server in
 the Project Explorer Window

Complete the following steps to create a new on input change I/O server in the
 Project Explorer window:

1. In the Project Explorer window, right-click a target, such as the
 My Computer target, and select New»I/O
 Server from the shortcut menu.
2. In the Create New I/O Server dialog box, select Custom VI - On
 Input Change and click the Continue button.
3. In the Configure Custom VI - On Input Change I/O Server dialog box, click
 the New button to display the Custom VI-based Server –
 On Input Change wizard. You also can select Tools»DSC Module»VI
 Based Server Wizard»On Input Change to display the Custom
 VI-based Server – On Input Change wizard.

#### Configuring the On Input Change I/O Server by
 Using the Custom VI-based Server – On Input Change Wizard

The Custom
 VI-based Server – On Input Change wizard converts a VI into a custom I/O
 server that performs calculations for an application and publishes the calculated results as
 NI Publish-Subscribe Protocol (NI-PSP) data items to the network. This wizard contains three
 pages that you must configure. Complete the following steps to configure the on input change
 I/O server.

1. On the Select VI page, enter the path to the VI that you want to
 convert into an on input change I/O server in the Path to VI text
 box. You also can use the Browse button to navigate to the VI.
2. If you installed the LabVIEW VI Analyzer Toolkit, place a
 checkmark in the Run VI Analyzer on VI checkbox. The VI Analyzer
 Toolkit can help you optimize the VI by running tests on the VI.
3. Click the Next button to continue.
4. On the Configure Server Distribution Component page, enter a name
 for the server configuration in the Configuration name text
 box.
5. Use the Browse button in the Support files 
 section to navigate to the support files necessary to run the server.
6. Click the Add button to add the support files to the list of
 Support files .
7. Click the Next button.
8. On the Server Distribution Component page, the wizard shows a
 summary of what the wizard is going to build. Click the Build 
 button. LabVIEW shows a Build Status dialog box. Note LabVIEW creates and places
 the I/O server dependency files in the National Instruments\Shared\DSC\Custom
 VI Input Change Server\version number\filename folder.

#### Setting the Initial Values of the On Input
 Change I/O Server

After the Custom VI-based Server – On Input
 Change wizard builds the files, the Configure Custom VI – On Input
 Change I/O Server dialog box appears again. Complete the following steps to
 use this dialog box to set the initial values for the inputs for the on input change I/O
 server.

1. Click the Next button.
2. On the Select Run Condition page, specify when you want the VI to
 run. The VI can run when any input value changes or when a specific input value changes.
 If you select the Run VI when specific input changes option, you
 also must select an input from the Input pull-down menu.
3. Click the Next button.
4. On the Set Initial Values page, you can assign initial values for
 the inputs on the VI. Select an input from the Input connectors 
 table and enter a value in the text box that appears to the right of the table.
5. Click the Finish button.

Parent topic:

Interact with Data Using I/O Servers

Related concepts:

- Use On Input Change I/O Servers
- Using Custom VI-Based I/O Servers

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=creating-opc-client-i-o-servers.html language=enus -->
## TOPIC 00047: Creating OPC Client I/O Servers

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `creating-opc-client-i-o-servers.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/creating-opc-client-i-o-servers.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can create an OPC Client I/O server to connect to a local or remote OPC server in a LabVIEW project or programmatically. After you create an OPC Client I/O server, you can configure a local OPC server to work with an OPC Client I/O server. You also can bind shared variables to the data items of

### Creating OPC Client I/O Servers

You can create an OPC Client I/O server to connect to a local or remote OPC server in a LabVIEW
 project or programmatically. After you create an OPC Client I/O server, you can
 configure a local OPC server to work with an OPC Client I/O server. You also can bind
 shared variables to the data items of the OPC Client I/O server.

#### Creating an OPC Client I/O Server in
 a LabVIEW Project

Complete the following steps to create an OPC Client I/O
 server in a LabVIEW project:

1. In the Project Explorer window, right-click a target,
 such as the My Computer target, and select
 New»I/O Server from the shortcut menu.
2. In the Create New I/O Server dialog box, select
 OPC Client and click the
 Continue button.
3. In the Configure OPC Client I/O Server dialog box,
 specify the Registered OPC servers to which you want to
 connect. The Registered OPC servers option lists all the
 OPC servers installed on a particular Machine .
4. Enter values for the Update rate (ms) ,
 Deadband (%) , and Reconnect poll rate
 (s) settings.
5. Click the Advanced tab to configure
 the Server Instance Preference , the Write
 Method Preference , and the Use Shared Variable Engine
 timestamps options.
6. Click the Diagnostics tab to
 configure the settings for logging diagnostic information about the OPC Client
 I/O server.
7. Click the OK button.

#### Creating an OPC Client I/O Server
 Programmatically

Complete the following steps to create an OPC Client I/O server
 programmatically:

1. Add the Create and Configure IO Server Express VI on the block diagram.
2. In the configuration dialog box that appears, select OPC
 Client from the I/O server type pull-down
 menu.
3. Click the Set Attributes button to display the Configure OPC
 Client I/O Server dialog box. Note If you click the
 OK button before you set the attributes for this
 OPC Client I/O server, LabVIEW automatically displays the
 Configure OPC Client I/O Server dialog
 box.
4. In the Configure OPC Client I/O Server dialog box, configure the settings
 for the new I/O server.
5. Click the OK button to close the Configure OPC Client I/O
 Server dialog box.
6. Click the OK button to close the configuration dialog box for the
 Express VI.

Parent topic:

Interact with Data Using I/O Servers

Related concepts:

- Use OPC Client I/O Servers
- Bind Shared Variables to OPC Server Data Items

Related tasks:

- Configuring Local OPC Servers to Work with OPC Client I/O Servers

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=creating-periodic-i-o-servers.html language=enus -->
## TOPIC 00048: Creating Periodic I/O Servers

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `creating-periodic-i-o-servers.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/creating-periodic-i-o-servers.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following guidelines to create a periodic I/O server.Create a custom I/O server in the Project Explorer window.Configure the periodic I/O server using the Custom VI-based Server – Periodic wizard.Set the initial values for the inputs of the periodic I/O server.After you create a new periodic

### Creating Periodic I/O Servers

Use the following guidelines to create a periodic I/O server.

1. Create a custom I/O server in the Project Explorer window.
2. Configure the periodic I/O server using the Custom VI-based Server –
 Periodic wizard.
3. Set the initial values for the inputs of the periodic I/O server.

After you create a new periodic I/O server, you do not need to create it again. You can just set the initial values for the inputs to reconfigure the I/O server.

#### Creating a New Periodic I/O Server in the
 Project Explorer Window

Complete the following steps to create a new periodic I/O
 server in the Project Explorer window:

1. In the Project Explorer window, right-click a target, such as the
 My Computer target, and select New»I/O
 Server from the shortcut menu.
2. In the Create New I/O Server dialog box, select Custom
 VI – Periodic and click the Continue button.
3. In the Configure Custom VI – Periodic I/O Server dialog box,
 click the New button to display the Custom VI-based
 Server – Periodic wizard. You also can select Tools»DSC Module»VI
 Based Server Wizard»Periodic to display the Custom VI-based
 Server – Periodic wizard.

#### Configuring the Periodic I/O Server by Using
 the Custom VI-based Server – Periodic Wizard

The Custom VI-based Server
 – Periodic wizard converts a VI into a custom I/O server that runs in the
 Shared Variable Engine and publishes NI Publish-Subscribe Protocol (NI-PSP) data items to
 the network. The Custom VI-based Server – Periodic wizard contains
 five pages that you must configure. Complete the following steps to configure the periodic
 I/O server:

1. On the Select VI page, enter the path to the VI that you want to
 convert into a periodic I/O server in the Path to VI text box. You
 also can use the Browse button to navigate to the VI.
2. If you installed the LabVIEW VI Analyzer Toolkit, place a
 checkmark in the Run VI Analyzer on VI checkbox. The VI Analyzer
 Toolkit can help you optimize the VI by running tests on the VI.
3. Click the Next button to continue.
4. On the Select Controls and Indicators To Publish page, select the
 front panel objects that you want to publish by placing checkmarks in the checkboxes next
 to the front panel object name displayed in the Controls or
 Indicators list. You must select at least one control or
 indicator to publish.
5. Click the Next button.
6. On the Select Method To Stop The Server page, select the method
 you want to use to stop the VI. You can select Abort VI or
 Stop the following While Loops . Use the Stop the
 following While Loops option to select a While Loop from the block diagram
 to use as the shutdown option.
7. In the Timeout(ms) text box, enter the amount of time, in
 milliseconds, you want the VI to wait before timing out.
8. Click the Next button.
9. On the Configure Server Distribution Component page, enter a name
 for the server configuration in the Configuration name text
 box.
10. Use the Browse button in the Support files 
 section to navigate to the support files necessary to run the server.
11. Click the Add button to add the support files to the list of
 Support files .
12. Click the Next button.
13. On the Server Distribution Component page, the wizard shows a
 summary of what the wizard is going to build. Click the Build 
 button. LabVIEW shows a Build Status dialog box. Note LabVIEW creates and places
 the I/O server dependency files in the National Instruments\Shared\DSC\Custom
 VI Periodic Server\version number\registration and National
 Instruments\Shared\DSC\Custom VI Periodic Server\version number\templates
 folders.

#### Setting the Initial Values of the Periodic
 I/O Server

After the Custom VI-based Server – Periodic Assistant builds the files,
 the Configure Custom VI – Periodic I/O Server dialog box appears
 again. Complete the following steps to use this dialog box to set the initial values for the
 inputs for the periodic I/O server:

1. Select an input from the Published controls table and enter a
 value in the control that appears to the right of the table.
2. Click the OK button to close Configure Custom VI –
 Periodic I/O Server dialog box.

Parent topic:

Interact with Data Using I/O Servers

Related concepts:

- Use Periodic I/O Servers
- Using Custom VI-Based I/O Servers
- Pass Data between LabVIEW and the Shared Variable Engine

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=creating-shared-variables-programmatically-ds.html language=enus -->
## TOPIC 00049: Creating Shared Variables Programmatically

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `creating-shared-variables-programmatically-ds.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/creating-shared-variables-programmatically-ds.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to create shared variables programmatically.Create a new LabVIEW VI. Add the Create Shared Variable VI on the block diagram. Specify a name for the process and wire it to the process name input of the Create Shared Variable VI. Use the process name input to define a logi

### Creating Shared Variables
 Programmatically

Complete the following steps to create shared variables
 programmatically.

1. Create a new LabVIEW VI.
2. Add the Create Shared Variable VI on the block diagram.
3. Specify a name for the process and wire it to the process name
 input of the Create Shared Variable VI. Use the process name input to
 define a logical grouping of shared variables.
4. Specify a name for the shared variable and wire it to the shared variable
 name input of the Create Shared Variable VI.
5. Specify a data type for the shared variable and wire it to the data
 type input of the Create Shared Variable VI.
6. Select File»Save to save the VI.
7. Run the VI. LabVIEW creates a shared variable with the shared variable name in the process name process.

Parent topic:

Create Shared Variables

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=deploy-a-dsc-module-application.html language=enus -->
## TOPIC 00050: Deploy a DSC Module Application

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `deploy-a-dsc-module-application.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/deploy-a-dsc-module-application.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: To deploy a LabVIEW Datalogging and Supervisory Control (DSC) Module application, you need a built application and any configuration information that the application and target computer require. Deployment refers to building an application and then distributing the application to a computer differen

### Deploy a DSC Module Application

Note

Before you deploy a DSC Module application, you need to determine how the application manages
 deployment and undeployment of LabVIEW project libraries. By default, project libraries
 do not deploy automatically in a built application. You can enable the automatic
 deployment and undeployment on the Shared Variable Deployment
 page. Then, the application deploys project libraries when the application starts and
 undeploys project libraries when the application exits. You also can use the
 Deploy Libraries and Undeploy Libraries VIs to deploy and
 undeploy project libraries programmatically.

Parent topic:

Network and Deploy Applications

Related tasks:

- Building a DSC Module Application
- Distributing a Built Application

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=deploying-a-shared-variable.html language=enus -->
## TOPIC 00051: Deploying a Shared Variable

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `deploying-a-shared-variable.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/deploying-a-shared-variable.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: When you deploy a shared variable, the Shared Variable Engine makes the shared variable available to other VIs and across a network.Complete the following steps to deploy a shared variable: Create a shared variable. Expand the project root to display the My Computer target. If the LabVIEW project li

### Deploying a Shared Variable

Complete the following steps to deploy a shared variable:

1. Create a shared variable.
2. Expand the project root to display the My Computer target.
3. If the LabVIEW project library is not under the My Computer
 target, in the Project Explorer window, add the project library
 that contains the shared variable you created to the My Computer
 target.
4. Right-click the project library and select Deploy All from the shortcut menu to deploy the shared variables in that project library.

Parent topic:

Deploying, Committing, and Monitoring Shared Variables

Related concepts:

- The Shared Variable Engine

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=deploying-committing-and-monitoring-shared-va.html language=enus -->
## TOPIC 00052: Deploying, Committing, and Monitoring Shared Variables

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `deploying-committing-and-monitoring-shared-va.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/deploying-committing-and-monitoring-shared-va.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section contains information about how to deploy, commit, and monitor shared variables with the LabVIEW Datalogging and Supervisory Control (DSC) Module.

### Deploying, Committing, and Monitoring Shared Variables

This section contains information about how to deploy, commit, and monitor shared
 variables with the LabVIEW Datalogging and Supervisory Control (DSC)
 Module.

- [Deploying a Shared Variable](deploying-a-shared-variable.html)
- [Committing Shared Variables](committing-shared-variables.html)
- [Monitoring Shared Variable Values](monitoring-shared-variable-values-dsc-module.html)

Parent topic:

Shared Variables

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=designing-a-dsc-module-application.html language=enus -->
## TOPIC 00053: Design a DSC Module Application

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `designing-a-dsc-module-application.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/designing-a-dsc-module-application.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DSC Module allows you to either design applications that run in the LabVIEW application development environment, or design custom Supervisory Control And Data Acquisition (SCADA) applications to deploy with the DSC Module Run-Time System.Refer to the manufacturer's web site for information about

### Design a DSC Module Application

The DSC Module allows you to either design applications that run in the LabVIEW
 application development environment, or design custom Supervisory Control
 And Data Acquisition (SCADA) applications to deploy with the DSC Module
 Run-Time System.

Note

A DSC Module application typically consists of three components: front panels, shared variables,
 and supervisory programs. You can use the Model-View-Controller design pattern to
 develop a DSC Module application using these three components.

Before you develop a DSC Module application, you might want to review the DSC Module example VIs
 or use an example VI as a starting point for building your application. You
 can access these example VIs by selecting Help»Find
 Examples from the pull-down menu and selecting
 Toolkits and Modules»Datalogging and Supervisory Control
 Module in the Example Finder window.

- [Components of a DSC Module Application](components-of-a-dsc-module-application.html)
- [Building a DSC Module Application](building-a-dsc-module-application.html)
- [Model-View-Controller Design Pattern](model-view-controller-design-pattern.html)

Parent topic:

LabVIEW Datalogging and Supervisory Control Module Features

Related concepts:

- Deploy a DSC Module Application

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=disabling-windows-special-key-capabilities.html language=enus -->
## TOPIC 00054: Disabling Windows Special Key Capabilities

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `disabling-windows-special-key-capabilities.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/disabling-windows-special-key-capabilities.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: You can prevent a user or group from using Windows special key capabilities. The following keys can be restricted: <Ctrl-Alt-Delete> <Ctrl-Esc> <Alt-Esc> <Alt-Tab> <Alt-Enter> <Ctrl-Alt-Esc> <Delete> Windows logo key arrow keys Complete the following steps to disable special key capabilities for the

### Disabling Windows Special Key Capabilities

- <Ctrl-Alt-Delete>
- <Ctrl-Esc>
- <Alt-Esc>
- <Alt-Tab>
- <Alt-Enter>
- <Ctrl-Alt-Esc>
- <Delete>
- Windows logo key
- arrow keys

Complete the following steps to disable special key capabilities for the users or
 groups that you specify:

1. Log in as an administrator by selecting Tools»User
 Name.
2. Select Tools»Options to display the
 Options dialog box.
3. Select Security from the Category
 list to display the Security Options page.
4. In the Advanced keyboard option section, specify the
 users or groups you want to disable special key capabilities for. 
 By default, LabVIEW enables special key capabilities for all users and groups
 and the Users or groups listbox is not activated. To
 activate the Users or groups listbox, click
 Add to add a user or group to this listbox. If the
 Users or groups is activated, LabVIEW then disables
 special key capabilities for all users and groups not listed in the listbox. If
 you want to remove a selected user or group from the Users or
 groups listbox, click the user or group and click
 Remove. LabVIEW then disables special key
 capabilities for the user and group that you removed.Note If the user special key
 capabilities conflict with the group capabilities, the user capabilities
 take precedence. The following examples demonstrate different use cases for
 specifying users and groups in the Users or groups
 listbox. If you want to enable special keys for a specific user in a group
 and disable special keys for the other users in this group, add the
 specific user to the Users or groups
 listbox.If you want to disable special keys for a specific user in a group
 and enable special keys for the other users in this group, add both
 the group and the specific user to the Users or
 groups listbox. Click the specific user and place a
 checkmark in the Disable special keys
 checkbox.
5. Click the OK button. 
 Note To disable Windows key
 access, you must perform a custom installation to install the Keyboard
 Filter Driver.

Parent topic:

Configure Security

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=display-trends.html language=enus -->
## TOPIC 00055: Display Trends

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `display-trends.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/display-trends.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: A trend is a graph display of shared variable values over time. With the LabVIEW Datalogging and Supervisory Control (DSC) Module, you have several options for displaying trends for real-time and historical data. Displaying Real-Time TrendsA real-time trend is a display of shared variable values as

### Display Trends

A trend is a graph display of shared variable values over time. With the LabVIEW
 Datalogging and Supervisory Control (DSC) Module, you have several options for displaying
 trends for real-time and historical data.

#### Displaying Real-Time Trends

A
 real-time trend is a display of shared variable values as they are collected in real time
 over a relatively short period of time. You can use the Distributed System Manager to
 display a real-time trend or use the Real-Time Trend Express VI to
 display a real-time trend in an application.

Because the Real-Time Trend
 Express VI waits for the specified time interval, place this
 Express VI in its own While Loop to control the
 execution rate of this Express VI. To run other VIs at the same rate that
 the real-time trend updates, place these VIs in the same While
 Loop.

The Real-Time Trend Express VI updates the value
 for each shared variable every time the Shared Variable Engine writes to the waveform chart
 indicator of this Express VI. If a VI using this indicator runs several
 times, the real-time trend continues to display previously acquired data. The manufacturer
 recommends that you configure this Express VI before the While
 Loop begins executing. You must specify the Shared Variable List to use this
 Express VI.

#### Displaying Historical Trends

A
 historical trend is a display of project values that have been logged to the
 Citadel historical database, usually over a relatively long period of
 time. If you configure an application to log values, you can display a historical trend in
 several ways.

Parent topic:

Displaying and Controlling Data

Related concepts:

- Pass Data between LabVIEW and the Shared Variable Engine
- Logging Historical Data to the Citadel Database
- Extracting and Viewing Citadel Data

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=displaying-and-controlling-data.html language=enus -->
## TOPIC 00056: Displaying and Controlling Data

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `displaying-and-controlling-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/displaying-and-controlling-data.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: A Human Machine Interface (HMI) is the interface through which an operator interacts with a system and with the outside environment that the system monitors and controls. In LabVIEW, you use VIs as the HMI for an application.The LabVIEW Datalogging and Supervisory Control (DSC) Module installs contr

### Displaying and Controlling Data

A Human Machine Interface (HMI) is the interface through which an operator interacts
 with a system and with the outside environment that the system monitors and controls.
 In LabVIEW, you use VIs as the HMI for an application.

The LabVIEW Datalogging and Supervisory Control (DSC) Module installs controls and indicators and
 VIs and functions to help you create HMIs. Use the DSC Module VIs
 and functions to control the HMI, access the Citadel historical database, perform
 calculations and logic, and change between different displays.

Before you build an HMI, make sure that you are familiar with Property Nodes and the VI
 server.

To develop an HMI application, create the front panel and then complete the block diagram.

- [Build Front Panels for DSC Module Applications](build-front-panels-for-dsc-module-applicat.html)
- [Set the Database Read Rate](set-the-database-read-rate.html)
- [Display Trends](display-trends.html)
- [Create Pipe Networks with Multi-Segment Pipe Controls](create-pipe-networks-with-multi-segment-pip.html)

Parent topic:

LabVIEW Datalogging and Supervisory Control Module Features

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=distribute-epics-server-io-servers.html language=enus -->
## TOPIC 00057: Distribute EPICS Server I/O Servers

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `distribute-epics-server-io-servers.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/distribute-epics-server-io-servers.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: By distributing an EPICS Server I/O server to a target computer, you can use the EPICS Server I/O server on multiple target computers. To distribute EPICS Server I/O servers, you must copy the whole LabVIEW project or application to the target computer. When you distribute an EPICS Server I/O server

### Distribute EPICS Server I/O Servers

By distributing an EPICS Server I/O server to a target computer, you can use the
 EPICS Server I/O server on multiple target computers.

To distribute EPICS Server I/O servers, you must copy the whole LabVIEW project or
 application to the target computer.

When you distribute an EPICS Server I/O server, the shared variables for publishing
 are source shared variables. Source shared variables have the following types:

Local source shared variables

Remote source shared variables

When you distribute an EPICS Server I/O server to a target computer, LabVIEW changes
 the URLs of local source shared variables from the development computer to the
 target computer. For example, LabVIEW changes the URL
 \\development_computer\library1\variable1 to
 \\target_computer\library1\variable1. LabVIEW does not
 change the URLs of remote source shared variables.

Parent topic:

Use EPICS Server I/O Servers

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=distributing-a-built-application.html language=enus -->
## TOPIC 00058: Distributing a Built Application

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `distributing-a-built-application.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/distributing-a-built-application.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the following guidelines to distribute a built application to a target computer.Install the LabVIEW Datalogging and Supervisory Control (DSC) Module Run-Time System on the target computer if you have not installed it already.You must have the DSC Module Run-Time System installed to run a DSC Mod

### Distributing a Built Application

Use the following guidelines to distribute a built
 application to a target computer.

1. Install the LabVIEW Datalogging and Supervisory Control (DSC) Module Run-Time
 System on the target computer if you have not installed it already. Note You must have the DSC Module
 Run-Time System installed to run a DSC Module application. Refer to the
 manufacturer's website for more information about the DSC Module Run-Time
 System.
2. Optional: 
 Right-click the application specification you want to distribute and select
 Properties from the shortcut menu to display the
 Application Properties dialog box. From
 the Preview page, click the Generate
 Preview button to review the generated files for the
 application.
3. Copy the entire built application directory to the target computer. If you
 created an installer, run the setup.exe file to install the
 application on the target computer. 
 Note The built
 application stores Citadel database in this directory.
 Ensure this directory is accessible if you enable logging for this
 application.
4. Optional: 
 Test the deployment of shared variables on the target computer before running
 the application. Use the Distributed System Manager to verify that shared
 variable deployment is successful. To launch the System Manager from LabVIEW,
 select Tools»Distributed System Manager.
5. Run the application on the target computer.

Parent topic:

Network and Deploy Applications

Related concepts:

- Logging Historical Data to the Citadel Database

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=edit-shared-variable-properties.html language=enus -->
## TOPIC 00059: Edit Shared Variable Properties

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `edit-shared-variable-properties.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/edit-shared-variable-properties.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section contains information about how to configure shared variables by editing shared variable properties, such as initial value, alarming, scaling, and update deadband, with the LabVIEW Datalogging and Supervisory Control (DSC) Module.

### Edit Shared Variable Properties

This section contains information about how to configure shared variables by
 editing shared variable properties, such as initial value, alarming,
 scaling, and update deadband, with the LabVIEW Datalogging and Supervisory
 Control (DSC) Module.

- [Enabling Network Publishing for Shared Variables](enabling-network-publishing-for-shared-variab.html)
- [Initializing Shared Variable Values](initializing-shared-variable-values.html)
- [Configuring Alarms](configuring-alarms.html)
- [Scaling Numeric Shared Variables](scaling-numeric-shared-variables.html)
- [Scaling U32 Bit Field Shared Variables](scaling-u32-bit-field-shared-variables.html)
- [Scaling Boolean Shared Variables](scaling-boolean-shared-variables.html)
- [Setting Shared Variable Deadbands](setting-shared-variable-deadbands.html)

Parent topic:

Shared Variable Properties

Related concepts:

- Shared Variables
- Shared Variable Properties

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=enable-data-and-event-logging-with-shared-v.html language=enus -->
## TOPIC 00060: Enable Data and Event Logging with Shared Variables

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `enable-data-and-event-logging-with-shared-v.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/enable-data-and-event-logging-with-shared-v.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: To enable logging, first configure logging options in the Project Library Properties dialog box then enable logging on the Logging page of the Shared Variable Properties dialog box when you create the shared variable.After you enable logging, the Shared Variable Engine (SVE) acquires data from all s

### Enable Data and Event Logging with Shared
 Variables

To enable logging, first configure logging options in the Project Library
 Properties dialog box then enable logging on the
 Logging page of the Shared Variable
 Properties dialog box when you create the shared variable.

After you enable logging, the Shared Variable Engine (SVE) acquires data from all shared
 variables for which you have enabled logging. The SVE then sends the data to the
 database, which logs the data.

To enable logging programmatically, use the Logging:Enabled, Logging:Log Alarms and Events, and
 Logging:Log Data SharedVariableIO properties.

Parent topic:

Shared Variable Properties

Related concepts:

- The Shared Variable Engine

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=enabling-network-publishing-for-shared-variab.html language=enus -->
## TOPIC 00061: Enabling Network Publishing for Shared Variables

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `enabling-network-publishing-for-shared-variab.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/enabling-network-publishing-for-shared-variab.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to enable network publishing for a shared variable. In the Project Explorer window, double-click a shared variable to display the Shared Variable Properties dialog box. On the Variable page, select Network-Published from the Variable Type pull-down menu.Click the OK butt

### Enabling Network Publishing for Shared Variables

Complete the following steps to enable network publishing for
 a shared variable.

1. In the Project Explorer window, double-click a shared variable
 to display the Shared Variable Properties dialog box.
2. On the Variable page, select
 Network-Published from the Variable Type
 pull-down menu.
3. Click the OK button.

Parent topic:

Edit Shared Variable Properties

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=extracting-and-viewing-citadel-data.html language=enus -->
## TOPIC 00062: Extracting and Viewing Citadel Data

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `extracting-and-viewing-citadel-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/extracting-and-viewing-citadel-data.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can view historical data logged to a Citadel database in the following ways: Use the Tags VIs, the Historical VIs, and the Historical Trend Express VI. You can specify the traces that the Historical Trend Express VI displays. You cannot browse to other traces, zoom in, jump to breaks, or jump to

### Extracting and Viewing Citadel Data

You can view historical data logged to a Citadel database in the following
 ways:

- Use the Tags VIs, the Historical VIs, and the
 Historical Trend Express VI. You can specify the traces that
 the Historical Trend Express VI displays. You cannot browse to
 other traces, zoom in, jump to breaks, or jump to minimums and maximums in the
 display.
- Use the Historical Data Viewer . With the Historical Data
 Viewer , you can view any number of traces and browse to traces within
 multiple databases. You can zoom out to any width, locate breaks, and jump to
 minimums and maximums of a trace.
- Use an ODBC-compliant program to query the Citadel database.

#### Accessing Historical Data Using
 Historical Data VIs

Use the Historical VIs in a Human
 Machine Interface (HMI) to retrieve and manipulate data logged in
 Citadel database files. You can use these VIs to browse
 files, extract the information in a format to display in the Historical
 Trend Express VI, or export the data to a spreadsheet file
 format.

#### Using URLs with Historical
 VIs

You can use URLs to locate data across a network with the
 Historical VIs. You can enter a URL from the front panel
 directly into a shared variable control. Right-click the shared variable control and
 select Allow Undefined Names from the shortcut
 menu.

The general form for the URL for shared variables is
 \\ComputerName\ProcessName\SharedVariableName,
 where ComputerName is the name of the computer running the
 process containing the SharedVariableName on the network,
 ProcessName is the name of the process containing the data
 item you want to connect to, and SharedVariableName is the name
 of the data item to which you want to connect.

Tip

ProcessName

SharedVariableName

You do not need to enter a path to the Citadel database. The
 LabVIEW Datalogging and Supervisory Control (DSC) Module can locate the Citadel
 database using the name of the computer on which the database resides and the
 database name. A database URL consists of the computer and database name where data
 for the source is stored, for example
 \\computer\my_database.

If you use a URL input for a variable name input in
 addition to a database URL for the database URL input with a
 Historical VI, the DSC Module checks the data directory
 specified by database URL for the shared variable part of the
 URL. If the DSC Module does not find that shared variable, it reports that it cannot
 access the shared variable. If you use a URL input for a variable
 name input while the database URL input is
 blank, the DSC Module uses the variable name URL to locate
 the shared variable data.

Parent topic:

Logging Historical Data to the Citadel Database

Related concepts:

- Access Citadel Data using ODBC Queries

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=filtering-alarms-and-events-in-the-alarm-and.html language=enus -->
## TOPIC 00063: Filtering Alarms and Events in the Alarm and Event Display Control

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `filtering-alarms-and-events-in-the-alarm-and.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/filtering-alarms-and-events-in-the-alarm-and.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to set the filter criteria to see certain alarms and events in the Alarm and Event Display control. To complete these steps, you must have a VI with an Alarm and Event Display control. Select Operate»Change to Run Mode to switch the VI to run mode. You also can press Ctr

### Filtering Alarms and Events in the Alarm and
 Event Display Control

Complete the following steps to set the filter criteria to
 see certain alarms and events in the Alarm and Event Display control. To complete these
 steps, you must have a VI with an Alarm and Event Display control.

1. Select Operate»Change to Run Mode to switch the VI to
 run mode. You also can press Ctrl-M to switch between
 edit mode and run mode. 
 Note When you set
 filters for events, the Alarm and Event Display control clears the existing
 events. When new events occur, the Alarm and Event Display control displays
 only the events that meet the filter criteria.
2. Right-click the Alarm and Event Display control and select Filter
 Options from the shortcut menu to display the
 Filter dialog box.
3. Specify filter criteria to display only alarms and events. You can select from the following
 filter criteria: Specifying Priorities — Place a checkmark in the
 Priority checkbox and enter priority values
 in the Min and Max text
 boxes.Specifying Users — Place a checkmark in the User
 Name checkbox and enter a user name in the text box to
 monitor alarms and events that occurred while that user is logged on.
 You can enter only one user name at a time. Note You can use asterisk
 (*) and question mark (?) wildcards to expand the scope of the
 filter. The asterisk represents one or more characters, and the
 question mark represents a single character. For example, a* stands
 for all user names that start with letter a. a? also stands for all
 user names start with letter a, but these user names must have only
 two characters.Specifying Acknowledging Users — Place a checkmark in the Ack.
 User Name checkbox and enter a user name in the text
 box. You can enter only one user name at a time, but you can use
 wildcards to expand the scope of the filter.Specifying Comments — Place a checkmark in the Ack.
 Comment checkbox and enter a comment in the text box.
 You can use wildcards to expand the scope of the filter.Specifying Object Names — Place a checkmark in the Object
 Name checkbox and enter an object name. You can enter
 only one object name at a time, but you can use wildcards to expand the
 scope of the filter.Note You must enter the
 full path to the system tree object, for example,
 \\computer\process\object.Specifying Descriptions — Place a checkmark in the
 Description checkbox and enter a description
 in the text box to restrict monitoring to alarms with the description.
 You can use wildcards to expand the scope of the filter.Specifying Area Names — Place a checkmark in the Area
 Name checkbox and enter an area name in the text box to
 restrict monitoring to that alarm area. You can enter only one alarm
 area at a time, but you can use wildcards to expand the scope of the
 filter.Note You can click the
 Browse button to display the
 Select Area dialog box. This dialog box
 displays alarm areas of the alarms in the Alarm and Event Display
 control. You can select an alarm area in the dialog box and click
 the OK button to apply this alarm area to the
 text box.
4. Optional: Use the Old Alarms section to display alarms that the
 user or the system has acknowledged and cleared. You can enter a number in the
 Number text box to specify the number of old alarms
 that the Alarm and Event Display control shows. You also can specify a starting
 time in the Start Time text box to display old alarms
 that occurred later than the starting time.
5. Optional: Select a display option among Show Alarms,
 Show Events, or Show
 Everything to display alarms, events, or both alarms and events
 in the Alarm and Event Display control.
6. Optional: Place a checkmark in the Audible Alarms checkbox to
 enable a sound alert when an alarm takes place. The sound depends on the system
 setting for error sounds.
7. Click the OK button. The Alarm and Event Display control displays only the alarms and events
 that meet all the filter criteria.

Parent topic:

Use Alarms and Events in DSC Module Applications

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=front-panels.html language=enus -->
## TOPIC 00064: Front Panels

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `front-panels.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/front-panels.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use front panels to interact with and display information about the state of a Supervisory Control And Data Acquisition (SCADA) system. You can use front panels as a user interface to display information about a VI. The DSC Module also extends front panel capability by enabling front panel data bind

### Front Panels

Use front panels to interact with and display information about the state of a
 Supervisory Control And Data Acquisition (SCADA) system.

You can use front panels as a user interface to display information about a VI. The DSC
 Module also extends front panel capability by enabling front panel data binding to
 reduce the amount of time you need to spend developing block diagrams.

In addition to front panel data binding, you also can use several user-interface-related
 features of the DSC Module. For example, you can use industrial automation images that
 the Image Navigator provides.

Parent topic:

Components of a DSC Module Application

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=initialize-shared-variable-values.html language=enus -->
## TOPIC 00065: Initialize Shared Variable Values

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `initialize-shared-variable-values.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/initialize-shared-variable-values.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: An initial value is a value that the shared variable is set to when you first deploy the shared variable. You can specify an initial value for each shared variable in the Initial Value page of the Shared Variable Properties dialog box.You also can use an Initial Value SharedVariableIO property to sp

### Initialize Shared Variable Values

An initial value is a value that the shared variable is set to when you first deploy the
 shared variable. You can specify an initial value for each shared variable in the
 Initial Value page of the Shared Variable
 Properties dialog box.

You also can use an Initial Value SharedVariableIO property to specify an initial value
 programmatically.

Parent topic:

Shared Variable Properties

Related tasks:

- Deploying a Shared Variable
- Initializing Shared Variable Values

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=initializing-shared-variable-values.html language=enus -->
## TOPIC 00066: Initializing Shared Variable Values

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `initializing-shared-variable-values.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/initializing-shared-variable-values.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: You can set the initial value for network-published shared variables only. Enable network publishing for a shared variable before you set an initial value for this shared variable. Complete the following steps to initialize a shared variable to a known value when the Shared Variable Engine starts: R

### Initializing Shared Variable Values

You can set the initial value for network-published shared variables only. Enable network
 publishing for a shared variable before you set an initial value for
 this shared variable. Complete the following steps to initialize a
 shared variable to a known value when the Shared Variable Engine
 starts:

1. Right-click a target or a LabVIEW project library in the
 Project Explorer window and
 select New»Variable from the shortcut
 menu to display the Shared Variable
 Properties dialog box. 
 You also can right-click an existing shared variable in the
 Project Explorer window and
 select Properties from the shortcut
 menu to display this dialog box.
2. Select Initial Value to display the
 Initial Value page.
3. Place a checkmark in the Enable Initial Value checkbox.
4. Enter the initial value you want the shared variable to have in the
 Initial Value control. 
 The information you enter in this control depends on the data type of the
 shared variable:Boolean — Click the TRUE or
 FALSE buttons in the
 Initial Value section to set the initial
 value.Double — Enter a numeric value in the Initial Value text box.Integer — Enter a numeric value in the Initial Value text box.Single — Enter a numeric value in the Initial Value text box.String — Enter a text value in the Initial Value text box.U32 Bit Field — Enter a numeric value in the Initial Value text box.
5. Click the OK button.

Parent topic:

Edit Shared Variable Properties

Related concepts:

- The Shared Variable Engine

Related tasks:

- Enabling Network Publishing for Shared Variables

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=interact-with-dsc-module-web-services.html language=enus -->
## TOPIC 00067: Interact with DSC Module Web Services

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `interact-with-dsc-module-web-services.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/interact-with-dsc-module-web-services.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Datalogging and Supervisory Control (DSC) Module includes built-in web services that expose DSC Module VIs functionality.LabVIEW web services allow web browsers and HTTP-capable clients to interact with LabVIEW applications. You use URLs and HTTP methods to transmit data to the web servi

### Interact with DSC Module Web Services

The LabVIEW Datalogging and Supervisory Control (DSC) Module includes built-in web
 services that expose DSC Module VIs functionality.

LabVIEW web services allow web browsers and HTTP-capable clients to interact with LabVIEW
 applications. You use URLs and HTTP methods to transmit data to the web service. The DSC
 Module includes the following web services:

Alarms & Events Web service

nialarm

Citadel Web service

Citadel

nicitadel

#### Accessing the DSC Module Web
 Services

In a web browser or other web client, you use URLs and HTTP
 methods to exchange information with the web service, as well as send values as post
 data using the POST HTTP method. Refer to the *World Wide Web Consortium*
 at www.w3.org for more information about HTTP method
 definitions, including the POST method.

The following figure shows an example
 URL that a web client might use to exchange data with the Alarms & Events Web
 service, nialarm:

[IMAGE alt='image' src='GUID-5804F5B5-AE09-44CF-9E62-F188D99691EA-a5.gif']

IP address or computer name

localhost

Port

3580

Web service name

Web service name

Web method

Tag URL

Input parameters

DSC Module Web services can return data as XML- or JSON-formatted responses. By
 default, the DSC Module Web services return XML-formatted responses.

#### Error Handling

After
 responding to a client request, the web service displays a response message in the
 HTTP header. The HTTP header describes whether an operation succeeds or fails. If an
 operation succeeds, the Reason-Phrase field in the HTTP header is empty. If an
 operation fails, the Reason-Phrase field in the HTTP header contains information
 about the failure, such as the LabVIEW error code and explanation of the
 error.

- [Access the Alarms & Events Web Service](access-the-alarms-events-web-service.html)
- [Access the Citadel Web Service](access-the-citadel-web-service.html)

Parent topic:

Network and Deploy Applications

Related concepts:

- Logging Historical Data to the Citadel Database

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=interacting-with-data-by-using-i-o-servers.html language=enus -->
## TOPIC 00068: Interact with Data Using I/O Servers

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `interacting-with-data-by-using-i-o-servers.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/interacting-with-data-by-using-i-o-servers.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: An I/O server is an application that communicates with and manages input/output devices such as Programmable Logic Controllers (PLCs), remote input/output devices, remote Shared Variable Engines (SVE), and Data Acquisition (DAQ) plug-in devices.I/O servers plug into the SVE to provide a list of item

### Interact with Data Using I/O Servers

An I/O server is an application that communicates with and manages input/output devices
 such as Programmable Logic Controllers (PLCs), remote input/output devices, remote
 Shared Variable Engines (SVE), and Data Acquisition (DAQ) plug-in devices.

I/O servers plug into the SVE to provide a list of items available for subscription and to source
 that data to the SVE. These I/O servers read selected input items and write to the
 selected input items on demand. With the LabVIEW Datalogging and Supervisory Control
 (DSC) Module, you can write LabVIEW I/O servers for any client. Typically, I/O servers
 expose certain configurable properties that you can configure when you add the I/O
 server to the LabVIEW project. For example, you might be able to configure the following
 options:

Poll rate

Poll items

Published items

I/O servers report error conditions reported by the hardware on abnormal conditions. The I/O
 server starts running when you deploy the LabVIEW project library that defines the
 server and stops when you stop or undeploy the project library. If you create the I/O
 server programmatically, the I/O server starts running when the VI that contains it
 executes the Create and Configure I/O Server Express VI. The I/O
 server then stops running when the VI that contains it executes the Delete I/O
 Server VI.

A server item is a channel, input/output point, or variable in a hardware device. Connect DSC
 Module applications to these server items with network-published shared variables.
 Device servers monitor the values acquired by the hardware. The SVE updates the shared
 variables when the server sends new data to the SVE. Servers also update each output
 when the Human Machine Interface (HMI) application writes that shared variable value,
 and they handle and report communications and device errors. A good device server covers
 all device- and hardware-specific details, establishing a device-independent
 input/output layer for the DSC Module. Many device servers include a configuration
 utility as well as the run-time application that communicates with the SVE.

#### OPC
 Servers

The DSC Module can connect to any OPC-compliant server and to many
 third-party device servers. You also can connect to custom I/O
 servers.

Start»All Programs»National Instruments»OPC
 Servers

x

»OPC Servers
 Configuration

x

Launcher

x

x

Note

OPC Servers
 Help

Help»Server Help

The DSC Module
 also can function as an OPC server and as a data source for the Publish-Subscribe
 Protocol networking protocol. The SVE functions as an OPC 2.x and OPC 3.0 compatible
 server. LabVIEW uses the Variable Engine OPC interface to display all numeric,
 Boolean, and string shared variables that you deploy to the SVE. Use any OPC
 2.x or OPC 3.0 client to view and modify OPC data that the
 OPC server publishes.

When you use a third-party OPC client to connect to the
 Variable Engine OPC server, the server name might appear as Variable
 Engine and Variable Engine.1. To ensure
 forward compatibility, connect to the Variable Engine
 instance when configuring an OPC connection.

Installers you build using the
 Application Builder also function as OPC servers if you include the SVE in the
 installer.

A server is not always the same as a device driver or an instrument
 driver. An instrument driver is a software component designed to control a
 programmable instrument, such as a multimeter. A device driver is a low-level
 software component that a computer needs to work with a plug-in interface. A device
 driver also can function as a server if the device driver meets certain standards,
 such as the OPC specification.

- [Choose an I/O Server](choosing-an-i-o-server.html)
- [Use Data Set Marking I/O Servers](using-data-set-marking-i-o-servers.html)
- [Use EPICS I/O Servers](using-epics-i-o-servers-dsc-module-or-real-ti.html)
- [Use Modbus I/O Servers](use-modbus-i-o-servers-dsc-module-or-real-t.html)
- [Use OPC Client I/O Servers](use-opc-client-i-o-servers.html)
- [Using Custom VI-Based I/O Servers](use-custom-vi-based-i-o-servers.html)
- [Binding Shared Variables to Data Items on OPC Servers That Do Not Support Browsing](binding-shared-variables-to-data-items-on-opc.html)
- [Create EPICS Client I/O Servers](create-epics-client-i-o-servers-dsc-module.html)
- [Create EPICS Server I/O Servers (DSC Module or Real-Time Module)](create-epics-server-i-o-servers-dsc-module.html)
- [Creating Modbus I/O Servers (DSC Module or Real-Time Module)](creating-modbus-i-o-servers-dsc-module-or-rea.html)
- [Creating On Input Change I/O Servers](creating-on-input-change-i-o-servers.html)
- [Creating OPC Client I/O Servers](creating-opc-client-i-o-servers.html)
- [Configuring Deployed Data Set Marking I/O Servers](configuring-deployed-data-set-marking-i-o-ser.html)
- [Configuring Local OPC Servers to Work with OPC Client I/O Servers](configuring-local-opc-servers-to-work-with-op.html)
- [Creating Periodic I/O Servers](creating-periodic-i-o-servers.html)

Parent topic:

LabVIEW Datalogging and Supervisory Control Module Features

Related concepts:

- Pass Data between LabVIEW and the Shared Variable Engine

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=introduction-to-modbus-masters-and-slaves-dsc.html language=enus -->
## TOPIC 00069: Introduction to Modbus Masters and Slaves

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `introduction-to-modbus-masters-and-slaves-dsc.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/introduction-to-modbus-masters-and-slaves-dsc.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: In Modbus master-slave communication, the Modbus master initiates transactions or queries, whereas the Modbus slaves respond by providing the requested data or performing the requested action.Typical Modbus master devices include host processors and programming panels. Typical Modbus slave devices i

### Introduction to Modbus Masters and
 Slaves

In Modbus master-slave communication, the Modbus master initiates transactions or
 queries, whereas the Modbus slaves respond by providing the requested data or performing
 the requested action.

Typical Modbus master devices include host processors and programming panels. Typical Modbus
 slave devices include programmable controllers. The messages that Modbus masters and
 slaves exchange are called frames. Different Modbus communications methods, such as
 Modbus Serial and Modbus Ethernet, lead to different types of Modbus master-slave
 communication.

#### Master-Slave Communication in Modbus
 Serial

In this communications method, a Modbus master and one or more
 Modbus slaves connect to the same bus simultaneously. The maximum number of Modbus
 slaves that a serial bus can connect to is 247. The Modbus master initiates
 communication with Modbus slaves using one of the following modes:

Unicast mode

Note

Broadcast mode

#### Master-Slave Communication in Modbus
 Ethernet

In this communications method, one or more Modbus masters establish a TCP connection
 to communicate with a Modbus slave. The Modbus masters connect to the Modbus slave
 with a specific address and port. The Modbus slave determines the number of Modbus
 masters that can connect to itself.

Parent topic:

Modbus Communication in LabVIEW

Related concepts:

- Modbus Transmission Mode

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=log-data-in-sets.html language=enus -->
## TOPIC 00070: Log Data in Sets

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `log-data-in-sets.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/log-data-in-sets.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: With the LabVIEW Datalogging and Supervisory Control (DSC) Module, you can organize historical data into data sets.A data set is a group of shared variable values that LabVIEW logs together during a finite time period. You can use a data set to record shared variable values for repeated tests. A dat

### Log Data in Sets

With the LabVIEW Datalogging and Supervisory Control (DSC) Module, you can organize
 historical data into data sets.

A data set is a group of shared variable values that LabVIEW logs together during a finite time
 period. You can use a data set to record shared variable values for repeated tests. A
 data set might cover a batch and contain all the values generated during a single
 execution of a batch process. The ID shared variable for each data set denotes a
 particular data set and the time during which the data set run took place. A batch
 process is defined by specific start and end conditions. The start and end conditions
 can include an analog input or digital input or time of day. You can perform batch
 logging with a data set marking I/O server.

#### Retrieving Logged Data
 Sets

You can use the Historical Data Viewer or the
 DataSets VIs to retrieve the data set values.

#### Considerations for Logging Data
 Sets

You cannot include a data set within another data set. Also, if a
 data set starts but does not properly meet its end condition, the data set is an
 open-ended run and does not appear as a complete data set when you access completed
 data sets in the Historical Data Viewer or with the
 DataSets VIs.

Parent topic:

Logging Historical Data to the Citadel Database

Related concepts:

- Use Data Set Marking I/O Servers

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=logging-data-to-relational-databases.html language=enus -->
## TOPIC 00071: Logging Data to Relational Databases

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `logging-data-to-relational-databases.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/logging-data-to-relational-databases.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can log shared variable data, alarms, and events to the following supported relational databases: Microsoft Access, MySQL, Oracle, PostgreSQL, and SQL Server.Logging data to a supported relational database enables you to work with shared variables, alarms, and events in a database other than the

### Logging Data to Relational Databases

You can log shared variable data, alarms, and events to the following supported
 relational databases: Microsoft Access, MySQL, Oracle, PostgreSQL, and SQL Server.

Logging data to a supported relational database enables you to work with shared variables,
 alarms, and events in a database other than the Citadel database. You must be familiar
 working with the supported relational database before logging data to that database.

You can log to a supported relational database by using one of the following methods:

- Log to the default relational database server. The default relational database server is the
 Microsoft SQL Server 2008 R2 Express, which installs with the LabVIEW Datalogging
 and Supervisory Control (DSC) Module. The Microsoft SQL Server 2008 R2 Express and
 the background services run automatically. You can monitor these services in the
 Services utility. The default relational database name is
 NIVariable_Default . Note The default database is located
 in the C:\ProgramData\National
 Instruments\Tagger\nivariable_database directory.
- Log to a preconfigured system Data Source Name (DSN), which you first configure on your
 machine.
- Log to a database by using a custom database connection string. You can enter the database
 connection string manually or build the database connection string by clicking the
 Build button on the Relational
 Database page.

Relational Database

DSC Settings:
 Database

Project Library Properties

Note

Use the Table Management dialog box to specify the table name for each
 data type that logs to the database. The DSC Module supports logging the following data
 types to a supported relational database: numeric, Boolean, and string. Each data type
 logs to a separate table. LabVIEW also logs alarms and events to a separate table. You
 can customize the table name for each data type that LabVIEW logs by process. For
 example, you can specify that data of the same data type from different processes logs
 to the same table or to different tables.

Parent topic:

Logging Historical Data to Databases

Related concepts:

- Logging Historical Data to the Citadel Database
- Monitoring Services

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=logging-historical-data-to-citadel-data.html language=enus -->
## TOPIC 00072: Logging Historical Data to the Citadel Database

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `logging-historical-data-to-citadel-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/logging-historical-data-to-citadel-data.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Citadel historical database is a database that the LabVIEW Datalogging and Supervisory Control (DSC) Module and other products use.This database efficiently stores data that applications acquire and process. The DSC Module uses the Citadel historical database to log shared variable data from the

### Logging Historical Data to the Citadel
 Database

The Citadel historical database is a database that the LabVIEW
 Datalogging and Supervisory Control (DSC) Module and other products use.

Citadel

Citadel
 ODBC

Note

Data processed by the SVE is contained in memory; LabVIEW does not create a file to hold the
 data. When you run an application configured to log data, LabVIEW logs data from the SVE
 to the Citadel historical database. You cannot log data when the SVE
 is stopped.

The Citadel historical database includes an ODBC driver, which enables other
 applications to directly retrieve data from a Citadel database using
 SQL queries. The Citadel 5 ODBC driver is compliant with SQL 92 and
 ODBC 2.5 standards. All clients that follow these standards can retrieve data from a
 Citadel 5 database. ADO clients can use the ODBC driver through
 the Microsoft OLE DB Provider for ODBC Drivers to access the Citadel
 5 database. MS Query wizard can be used to build-up queries. The
 Citadel database runs on Windows as a service.

Citadel

Caution

Citadel

Note

Citadel

Citadel

Citadel

Citadel

The data you log to a Citadel database resides in a set of files in the target
 directory you set for logging. This data can include shared variable values from the
 application as well as alarms and events. You determine the data that is logged to a
 specific location when you configure shared variables and alarm and event logging for
 shared variables. Shared variable data that logs to the Citadel
 database is called a trace. A trace contains the data type, data values, timestamps, and
 qualities of the shared variable. Each shared variable logs to an independent trace. You
 also can log data in sets.

Note

You can access Citadel data through the Historical Data
 Viewer, Historical VIs, SQL queries, or any other
 ODBC-compliant application such as Microsoft Query, Microsoft Access, or Microsoft
 Excel.

#### Specifying an Appropriate Database
 Location

To ensure that data logging to the Citadel
 database is successful, you must specify an appropriate database location to which
 the DSC Module has full access.

By default, the DSC Module configures
 appropriate access rights for the labview\data folder and
 stores the database in that folder. If you want to store the database in a different
 folder, ensure that the folder meets the following requirements:

- The database folder is readable by all members of the USERS group. The
 Citadel database is a shared resource and must be
 available to all users of the system. Alarm logging fails if the database folder
 is not readable to all users.
- The database folder is writable by the user who wants to log data.
- The database folder is readable and writable by the SYSTEM user. The
 Citadel service runs as a SYSTEM user and must have
 sufficient access rights to manage the database files.
- The database folder is writable by the NETWORK SERVICE user. By default, the
 folders under the C:\Users directory and the top-level
 folders that the NETWORK SERVICE user creates are writable by that user.

If you do not store the database in the labview\data
 folder, the manufacturer recommends that you place the database under the Windows
 Public user directory, located at C:\Users\Public. This folder
 always meets the requirements above. Do not use the following folders to store the
 database:

- C:\Windows —The system has highly restricted access to this
 folder.
- C:\Users\Username —This folder is visible only to the owning
 user, so the system has restricted access to this folder.

- [Log Data in Sets](log-data-in-sets.html)
- [Archive Citadel Data](archive-citadel-data.html)
- [Print Citadel Data](print-citadel-data.html)
- [Extracting and Viewing Citadel Data](extracting-and-viewing-citadel-data.html)
- [Creating a Citadel ODBC Data Source](creating-a-citadel-odbc-data-source.html)
- [Creating a Data Link for the ODBC Data Source](creating-a-data-link-for-the-odbc-data-source.html)
- [Creating Data Sets for Logging](creating-data-sets-for-logging.html)
- [Logging Historical Data](logging-historical-data.html) Complete the following steps to enable logging to the Citadel database for a process.
- [Opening a Trace for Writing Directly to Citadel](opening-a-trace-for-writing-directly-to-citad.html)
- [Writing a Data Break into a Citadel Trace](writing-a-data-break-into-a-citadel-trace.html)
- [Writing a Value to a Citadel Trace](writing-a-value-to-a-citadel-trace.html) You can use the Write Trace VI to append a data point to a Citadel trace.

Parent topic:

Logging Historical Data to Databases

Related concepts:

- Pass Data between LabVIEW and the Shared Variable Engine
- Access Citadel Data with SQL
- Use Alarms and Events in DSC Module Applications

Related tasks:

- Stopping and Starting the Shared Variable Engine

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=logging-historical-data-to-databases.html language=enus -->
## TOPIC 00073: Logging Historical Data to Databases

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `logging-historical-data-to-databases.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/logging-historical-data-to-databases.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Datalogging and Supervisory Control (DSC) Module can log data to the Citadel historical database as well as supported relational databases.When you enable data logging to a database, you can access, manipulate, and analyze the stored data. The manufacturer provides tools, such as the His

### Logging Historical Data to Databases

The LabVIEW Datalogging and Supervisory Control (DSC) Module can log data to the
 Citadel historical database as well as supported relational
 databases.

When you enable data logging to a database, you can access, manipulate, and analyze the stored
 data. The manufacturer provides tools, such as the Historical Data
 Viewer, Historical VIs, Tags VIs,
 and so on, for you to work with data you log to the Citadel database.
 Contact your database administrator for information about working with data in supported
 relational databases.

- [Logging Data to Relational Databases](logging-data-to-relational-databases.html)
- [Logging Historical Data to the Citadel Database](logging-historical-data-to-citadel-data.html)

Parent topic:

LabVIEW Datalogging and Supervisory Control Module Features

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=logging-historical-data.html language=enus -->
## TOPIC 00074: Logging Historical Data

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `logging-historical-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/logging-historical-data.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to enable logging to the Citadel database for a process. Complete the following steps to enable logging to the Citadel database for a process.You also can log data to a supported relational database for a process. Use the Relational Database page on the DSC Settings: Dat

### Logging Historical Data

Complete the following steps to enable logging to the Citadel database for a
 process.

Citadel

Note

Relational Database

DSC
 Settings: Database

Project Library
 Properties

1. Right-click a LabVIEW project library in the Project
 Explorer window and select Properties
 from the shortcut menu to display the Project Library
 Properties dialog box.
2. Select DSC Settings: Database from the Category list.
3. On the Citadel page of the DSC Settings:
 Database page, place a checkmark in the Enable Data
 Logging checkbox to enable data logging.
4. Enter the name of the computer to which you want to log data in the
 Log to computer text box. 
 The default computer is localhost, which is the local computer. If you want
 to log data to a remote computer, ensure you have the LabVIEW Datalogging and
 Supervisory Control (DSC) Module or the DSC Module Run-Time System installed on
 that computer. Note Refer to the manufacturer's web site for information about the DSC Module
 Run-Time System.
5. Enter the name of the database to which you want to log data in the Database name text box.
6. Enter the location of the database to which you want to log data in the
 Database path text box. 
 If you log data to directories created in a secure file system, such as NTFS, you must grant
 Change or Full Control permissions for the current user, the SYSTEM account, and
 the NETWORK SERVICE account to access the directory. If you do not grant these
 accounts appropriate access to the database directory, the Citadel service
 cannot create and modify the database files it uses to store historical data and
 alarms. Note (Windows 7/Vista) The Citadel service does not have
 access to a specific user folder, for example,
 C:\Users\lvadmin\. Therefore, the
 Citadel service cannot create or modify databases in
 this folder.
7. Select the length of time you want data to be available in the database in the Data Lifespan options.
8. Place a checkmark in the Enable Alarms and Events Logging checkbox to log alarms and events.
9. Place a checkmark in the Use the same database for alarms and events checkbox to use the same database you set up for data logging.
10. Click the OK button to close the dialog box.

Note

You also can use the Enable Data Logging On Process VI or the Enable
 Alarm Logging On Process to enable or disable logging to the
 Citadel database programmatically.

Parent topic:

Logging Historical Data to the Citadel Database

Related concepts:

- Logging Data to Relational Databases

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=logging-in-and-out-dsc-module.html language=enus -->
## TOPIC 00075: Logging In and Out

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `logging-in-and-out-dsc-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/logging-in-and-out-dsc-module.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to log into a LabVIEW Datalogging and Supervisory Control (DSC) Module application. To log in, select Tools»Security»Login. Type your user account name and password. If you do not know your account name, or forget your password, contact your LabVIEW administrator.To log

### Logging In and Out

Complete the following steps to log into a LabVIEW
 Datalogging and Supervisory Control (DSC) Module application.

1. To log in, select
 Tools»Security»Login.
2. Type your user account name and password. If you do not know your account name, or forget your password, contact your LabVIEW administrator.

To log out, select Tools»Security»Logout or select Tools»User
 Name and click the Logout
 button.

Parent topic:

Configure Security

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=lv-datalogging-and-supervisory-control-module.html language=enus -->
## TOPIC 00076: LabVIEW Datalogging and Supervisory Control Module Features

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `lv-datalogging-and-supervisory-control-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/lv-datalogging-and-supervisory-control-module.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Datalogging and Supervisory Control (DSC) Module extends the LabVIEW graphical development environment with additional functionality for the rapid development of distributed measurement, control, and high-channel-count monitoring applications.The DSC Module also enhances the LabVIEW shar

### LabVIEW Datalogging and Supervisory Control
 Module Features

The LabVIEW Datalogging and Supervisory Control (DSC) Module extends the LabVIEW
 graphical development environment with additional functionality for the rapid
 development of distributed measurement, control, and high-channel-count monitoring
 applications.

The DSC Module also enhances the LabVIEW shared variable. Use the shared variable to access and
 pass data among VIs and devices on the local computer and across a network. A shared
 variable can represent a value or an I/O point. With the DSC Module, you can log data
 automatically; add alarming, scaling, and security to the shared variable; and configure
 the shared variable programmatically.

The DSC Module also enhances the Distributed System Manager. You can use the System Manager to
 monitor, configure, and acknowledge alarms. You also can use the System Manager to
 monitor and acknowledge events.

To use the System Manager, launch LabVIEW and select Tools»Distributed System
 Manager.

The DSC Module also provides tools for graphing historical or real-time trends, enhancing the
 security of front panels, and writing custom I/O servers. You can read or write to OLE
 for Process Control (OPC) connections, Programmable Logic Controllers (PLCs), or custom
 I/O servers that you write. The DSC Module provides solutions for supervisory control of
 a wide variety of distributed systems using graphical LabVIEW programming.

- [Design a DSC Module Application](designing-a-dsc-module-application.html)
- [Interact with Data Using I/O Servers](interacting-with-data-by-using-i-o-servers.html)
- [Modbus Communication in LabVIEW](modbus-communication-in-labview.html)
- [Managing I/O with Shared Variables](managing-i-o-with-shared-variables.html)
- [Displaying and Controlling Data](displaying-and-controlling-data.html)
- [Use Alarms and Events in DSC Module Applications](use-alarms-and-events-in-dsc-module-applica.html)
- [Logging Historical Data to Databases](logging-historical-data-to-databases.html)
- [Configure Security](configure-security.html)
- [Network and Deploy Applications](network-and-deploy-applications.html)
- [Access Citadel Data with SQL](access-citadel-data-with-sql.html)

Related concepts:

- Using Custom VI-Based I/O Servers

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=managing-i-o-with-shared-variables.html language=enus -->
## TOPIC 00077: Managing I/O with Shared Variables

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `managing-i-o-with-shared-variables.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/managing-i-o-with-shared-variables.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: With the LabVIEW Datalogging and Supervisory Control (DSC) Module, you can configure how LabVIEW scales shared variable data, logs shared variable data to a historical database, and sets alarm levels and priorities for shared variable data.You can use shared variables to represent a real-world input

### Managing I/O with Shared Variables

With the LabVIEW Datalogging and Supervisory Control (DSC) Module, you can configure how
 LabVIEW scales shared variable data, logs shared variable data to a historical database,
 and sets alarm levels and priorities for shared variable data.

Note

You can configure a shared variable by editing shared variable properties. The shared variable
 properties that you can edit depends on the data type of the shared variable and on your
 target and licensed product(s).

Shared variables communicate between VIs, remote computers, and hardware through the Shared
 Variable Engine (SVE). The SVE is a data processing engine that manages the use and
 connectivity of shared variables. The SVE uses the NI Publish-Subscribe Protocol
 (NI-PSP) data transfer protocol to write and allow users to read live data.

The DSC Module also adds OPC functionality to LabVIEW, allowing shared variables to connect to
 OPC servers and clients. To connect shared variables to OPC server data items
 interactively, you can create an OPC Client I/O server, or use the Multiple
 Variable Editor window, available by right-clicking a project library or
 shared variable in the Project Explorer window and selecting
 Multiple Variable Editor from the shortcut menu. LabVIEW
 automatically publishes deployed shared variables to the OPC server.

- [Shared Variables](shared-variables.html)
- [The Shared Variable Engine](the-shared-variable-engine.html)
- [Shared Variable Properties](shared-variable-properties.html)

Parent topic:

LabVIEW Datalogging and Supervisory Control Module Features

Related concepts:

- Supported Shared Variable Properties Based on Target and Products
- Creating OPC Client I/O Servers
- Create Shared Variables
- Deploying, Committing, and Monitoring Shared Variables
- Pass Data between LabVIEW and the Shared Variable Engine
- Edit Shared Variable Properties
- Configure Shared Variables

Related reference:

- Supported Shared Variable Properties Based on Data Type

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=modbus-communication-in-labview.html language=enus -->
## TOPIC 00078: Modbus Communication in LabVIEW

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `modbus-communication-in-labview.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/modbus-communication-in-labview.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Modbus is a communications protocol that provides master-slave communication between devices. Modbus allows data exchange between Programmable Logic Controllers (PLCs) and computers or Human Machine Interfaces (HMIs).Supervisory Control And Data Acquisition (SCADA) systems and HMIs can integrate dev

### Modbus Communication in LabVIEW

Modbus is a communications protocol that provides master-slave communication between
 devices. Modbus allows data exchange between Programmable Logic Controllers (PLCs) and
 computers or Human Machine Interfaces (HMIs).

Supervisory Control And Data Acquisition (SCADA) systems and HMIs can integrate devices using
 Modbus. Refer to the *Modbus Organization* web site at
 *www.modbus.org* for more information about Modbus.

- [Modbus Transmission Mode](modbus-transmission-mode-dsc-module-or-real-t.html)
- [Modbus Data Representation](modbus-data-representation-dsc-module-or-real.html)
- [Introduction to Modbus Masters and Slaves](introduction-to-modbus-masters-and-slaves-dsc.html)
- [Choose between Modbus I/O Servers and Modbus VIs](choose-between-modbus-i-o-servers-and-modbu.html)

Parent topic:

LabVIEW Datalogging and Supervisory Control Module Features

Related concepts:

- Use Modbus I/O Servers
- Creating Modbus I/O Servers (DSC Module or Real-Time Module)
- Troubleshooting Modbus I/O Servers
- Choose between Modbus I/O Servers and Modbus VIs

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=modbus-data-representation-dsc-module-or-real.html language=enus -->
## TOPIC 00079: Modbus Data Representation

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `modbus-data-representation-dsc-module-or-real.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/modbus-data-representation-dsc-module-or-real.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Modbus bases its data model on data tables and in read and write operations, Modbus allows masters and slaves to select up to 65,536 data items for each data table. Modbus Data TableA data table is an array or a block of memory that stores data. Modbus bases its data model on data tables, as describ

### Modbus Data Representation

Modbus bases its data model on data tables and in read and write
 operations, Modbus allows masters and slaves to select up to 65,536
 data items for each data table.

#### Modbus Data Table

A data table is an array or a block of memory that stores data. Modbus bases its data
 model on data tables, as described in the following table:

| Data Table | Data Type | Access Type | Use Case | Comment |
| --- | --- | --- | --- | --- |
| Discrete Input | Boolean | Read-Only | Representing sensor inputs and other Boolean values to read. | Both Modbus masters and slaves can read discrete inputs. Only Modbus slaves can write discrete inputs. |
| Coil | Boolean | Read or Write | Representing outputs and internal bits to read and write. | Both Modbus masters and slaves can read and write coils. |
| Input Register | Unsigned 16-Bit Integers | Read-Only | Representing analog input values and other integer values to read. | Both Modbus masters and slaves can read input registers. Only Modbus slaves can write input registers. |
| Holding Register | Unsigned 16-Bit Integers | Read or Write | Representing analog outputs and internal numbers to read and write. | Both Modbus masters and slaves can read and write holding registers. |

#### Modbus Data Table Address

Modbus references data using data table addresses. Each data table has its own
 assigned address. However, the maximum number of contiguous data items that Modbus
 masters can select depends on the data table type and the operation to perform. For
 example, the maximum number of coils a Modbus master can write is 1,968. The maximum
 number of discrete inputs a Modbus master can read is 2,000.

Modbus data table
 addresses are integer numbers. The addresses are 0-based, meaning that the starting
 address for each data table is 0. However, some devices use 1-based addresses.
 Verify the starting address in each device to ensure that you select the appropriate
 data items.

Parent topic:

Modbus Communication in LabVIEW

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=modbus-transmission-mode-dsc-module-or-real-t.html language=enus -->
## TOPIC 00080: Modbus Transmission Mode

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `modbus-transmission-mode-dsc-module-or-real-t.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/modbus-transmission-mode-dsc-module-or-real-t.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Modbus provides Serial and Ethernet as communication methods. These communications methods use different data transmission modes: Remote Terminal Unit (RTU), American Standard Code for Information Interchange (ASCII), and Transmission Control Protocol (TCP). Modbus Serial At any time, only one Modbu

### Modbus Transmission Mode

Modbus provides Serial and Ethernet as communication methods. These
 communications methods use different data transmission modes: Remote
 Terminal Unit (RTU), American Standard Code for Information Interchange
 (ASCII), and Transmission Control Protocol (TCP).

Modbus Serial

Modbus Ethernet

The following table describes these transmission modes:

| Transmission Mode | Communications Method | Description |
| --- | --- | --- |
| RTU | Serial | Each message data byte consists of two 4-bit hexadecimal characters. Devices and applications transmit each message in a continuous stream of characters. |
| ASCII | Serial | Each message data byte consists of two ASCII characters. |
| TCP | Ethernet | The Modbus data message is encapsulated in a TCP frame. |

Parent topic:

Modbus Communication in LabVIEW

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=model-view-controller-design-pattern.html language=enus -->
## TOPIC 00081: Model-View-Controller Design Pattern

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `model-view-controller-design-pattern.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/model-view-controller-design-pattern.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Model-View-Controller (MVC) design pattern is an application design pattern that consists of three components: a model represents any data in the system, a view provides access to the model, and a controller processes events and then updates the model with new data.The following flowchart illust

### Model-View-Controller Design Pattern

The Model-View-Controller (MVC) design pattern is an application design pattern
 that consists of three components: a model represents any data in the
 system, a view provides access to the model, and a controller processes
 events and then updates the model with new data.

The following flowchart illustrates the interaction of each component in the MVC design
 pattern:

[IMAGE alt='image' src='GUID-BC711EC6-E9CB-4E9C-8B33-0208DD949C87-a5.gif']

As shown in the previous flowchart, when an event occurs in a system, the system passes the event
 to a controller that monitors the event. The controller processes the event and then
 updates the model. Views receive data changes from the model and update accordingly.

You can use the MVC design pattern for most LabVIEW Datalogging and Supervisory Control (DSC)
 Module applications. In the DSC Module, shared variables and other I/O points represent
 a model. A set of front panel windows represents a view. Front panel windows interact
 with the model through front panel data binding. Any supervisory program, such as an I/O
 server, running in the application represents a controller.

The following flowchart illustrates the interaction of the components in a DSC Module application
 according to the MVC design pattern:

[IMAGE alt='image' src='GUID-04EC3DD1-2600-40F0-8CA4-C4F1B4BC6918-a5.gif']

The DSC Module is an event-driven I/O system. Real-world sensor inputs or user inputs through a
 front panel can generate events. When an event occurs, the Shared Variable Engine
 processes and passes the event to any supervisory programs that monitor the event. Then
 the DSC Module either executes these supervisory programs and updates the shared
 variables or directly passes the event to the shared variables. Front panel windows
 interact with the shared variables through front panel data binding and update
 accordingly when data changes.

When you develop a DSC Module application, you can build a model, a view, and a controller in any
 order. However, the manufacturer recommends that you build an application in
 the following order:

1. Design a model. Define how you want to organize shared variables in the application. Create a project and use LabVIEW project libraries to organize functional groups of shared variables.
2. Design a view. Create front panel windows to interact with the shared variables.
3. Design one or more controllers. Create supervisory control VIs that process events in the application.

Parent topic:

Design a DSC Module Application

Related concepts:

- Pass Data between LabVIEW and the Shared Variable Engine

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=monitoring-services.html language=enus -->
## TOPIC 00082: Monitoring Services

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `monitoring-services.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/monitoring-services.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI Publish-Subscribe Protocol (NI-PSP) networking protocol requires three background services that run on Windows outside of any NI applications.The services include Citadel 4 Service, Citadel 5, PSP Service Locator, and Time Synchronization. In the Windows Task Manager, these services appear as

### Monitoring Services

The NI Publish-Subscribe Protocol (NI-PSP) networking protocol requires three
 background services that run on Windows outside of any NI
 applications.

Citadel 4 Service

Citadel 5

PSP Service Locator

Time
 Synchronization

lkcitdl.exe

Citadel
 4

nicitdl5.exe

Citadel 5

lkads.exe

tagsrv.exe

lktsrv.exe

Note

The DSC Module also installs the Microsoft SQL Server 2008 R2 Express, which appears as
 sqlservr.exe in the Services utility. The
 Microsoft SQL Server 2008 R2 Express and the background services run
 automatically. If you need to interact with these services, you can use
 the Services utility. On Windows operating systems, select
 Start»Run, enter
 services.msc in the Open
 text box, and click the OK button to launch the
 Services utility.

Parent topic:

Network and Deploy Applications

Related concepts:

- Pass Data between LabVIEW and the Shared Variable Engine

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=monitoring-shared-variable-values-dsc-module.html language=enus -->
## TOPIC 00083: Monitoring Shared Variable Values

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `monitoring-shared-variable-values-dsc-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/monitoring-shared-variable-values-dsc-module.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to monitor and write shared variable values. Select Tools»Distributed System Manager to display the Distributed System Manager. Navigate to the shared variables you want to monitor by using the system tree pane.Right-click the shared variable and select Watch List from t

### Monitoring Shared Variable Values

Complete the following steps to monitor and write
 shared variable values.

1. Select Tools»Distributed System Manager
 to display the Distributed System Manager.
2. Navigate to the shared variables you want to monitor by using the system tree pane.
3. Right-click the shared variable and select Watch List from the shortcut menu to open a new Watch List view.
You also can select multiple shared variables and drag them to an existing Watch List view.
4. Monitor the shared variable in the Watch List view.
5. Select Action»Refresh to refresh the
 system tree. The shared variables in the Watch
 List update continuously.

Refer to the *Distributed System Manager Help* for more information about the System
 Manager.

You also can monitor and update shared variable values programmatically by using the
 Read Tag and Write Tag
 VIs.

Parent topic:

Deploying, Committing, and Monitoring Shared Variables

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=network-and-deploy-applications.html language=enus -->
## TOPIC 00084: Network and Deploy Applications

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `network-and-deploy-applications.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/network-and-deploy-applications.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you develop a LabVIEW Datalogging and Supervisory Control Module application, multiple users might need access to that application. You can choose to either set up a networked application or deploy the application to other computers.Networking an application enables users to access the applicat

### Network and Deploy Applications

When you develop a LabVIEW Datalogging and Supervisory Control Module application,
 multiple users might need access to that application. You can choose to either set up
 a networked application or deploy the application to other computers.

Networking an application enables users to access the application, which remains on the host
 computer, from across the network as long as no communication problems occur.
 Deploying an application enables users to access copies of the application on
 computers other than the computer on which you developed the application.

- [Deploy a DSC Module Application](deploy-a-dsc-module-application.html)
- [Distributing a Built Application](distributing-a-built-application.html)
- [Monitoring Services](monitoring-services.html)
- [Interact with DSC Module Web Services](interact-with-dsc-module-web-services.html)
- [Setting Up Networked Applications](setting-up-networked-applications-dsc-module.html)
- [Registering Remote Computers](registering-remote-computers-dsc-module.html)
- [Setting Time Synchronization for Networked Computers](setting-time-synchronization-for-networked-co.html)
- [Troubleshooting Communication Problems](troubleshooting-communication-problems.html)

Parent topic:

LabVIEW Datalogging and Supervisory Control Module Features

Related tasks:

- Setting Up Networked Applications

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=new-features-and-changes.html language=enus -->
## TOPIC 00085: LabVIEW Datalogging and Supervisory Control Module New Features and Changes

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/new-features-and-changes.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of LabVIEW Datalogging and Supervisory Control Module. Discover what is new in the latest releases of LabVIEW Datalogging and Supervisory Control Module.If you cannot find new features and changes for your v

### LabVIEW Datalogging and Supervisory Control
 Module
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of LabVIEW Datalogging and Supervisory Control
 Module.

LabVIEW Datalogging and Supervisory Control
 Module

Note

Release Notes

Related information:

- Software and Driver Downloads

#### LabVIEW Datalogging and Supervisory Control
 Module 2021 Changes

Learn about new features, behavior changes, and other updates in LabVIEW Datalogging
 and Supervisory Control Module 2021.

- LabVIEW Datalogging and Supervisory Control Module 2021 no longer supports Windows
 7/8.1, Windows Server 2008/2012, or any 32-bit Windows operating system.
  - Versions of this product that ship after May 1, 2021 may not install or execute
 correctly on these operating systems. For information about operating systems that
 NI supports, visit NI Support for Windows 7, Windows 8.1, Windows Server 2008
 R2, Windows Server 2012 R2, and All 32-Bit Windows .

Related information:

- NI Support for Windows 7, Windows 8.1, Windows Server 2008 R2,
 Windows Server 2012 R2, and All 32-Bit Windows

#### LabVIEW Datalogging and Supervisory Control
 Module 2018 Changes

Learn about new features, behavior changes, and other updates in LabVIEW Datalogging
 and Supervisory Control Module 2018.

LabVIEW Datalogging and Supervisory Control Module 2018 includes only bug fixes. Refer to
 the Release Notes for a list of bug fixes.

Related information:

- Release Notes

#### LabVIEW Datalogging and Supervisory Control
 Module 2019 Changes

Learn about new features, behavior changes, and other updates in LabVIEW Datalogging
 and Supervisory Control Module 2019.

LabVIEW Datalogging and Supervisory Control Module 2019 includes only bug fixes. Refer to
 the Release Notes for a list of bug fixes.

Related information:

- Release Notes

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=opening-a-trace-for-writing-directly-to-citad.html language=enus -->
## TOPIC 00086: Opening a Trace for Writing Directly to Citadel

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `opening-a-trace-for-writing-directly-to-citad.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/opening-a-trace-for-writing-directly-to-citad.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: You can use the Open Trace VI to create a direct trace for writing to a Citadel historical database. Complete the following steps to open a trace for writing: Add the Open Trace VI on the block diagram. Wire the URL of the Citadel database to the database URL input of this VI. Choose a name for the

### Opening a Trace for Writing Directly to Citadel

You can use the Open Trace VI to create a direct trace for writing to a
 Citadel historical database. Complete the following steps to open a
 trace for writing:

1. Add the Open Trace VI on the block diagram.
2. Wire the URL of the Citadel database to the database
 URL input of this VI.
3. Choose a name for the process and wire it to the process name input of this VI. Use the process name input to define a logical grouping of traces.
4. Choose a name for the trace and wire it to the trace name input
 of this VI. 
 Use the name of an existing trace to append data to the end of that trace because the
 Open Trace VI fails if there is an open trace refnum for the trace
 already. This VI also fails if the Shared Variable Engine is writing data to the trace
 already.
5. Use the polymorphic VI selector to choose the type of the data you want to write.
6. Optional: 
 Configure the timeout and precision of the trace.

Parent topic:

Logging Historical Data to the Citadel Database

Related concepts:

- Extracting and Viewing Citadel Data
- Pass Data between LabVIEW and the Shared Variable Engine

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=overview.html language=enus -->
## TOPIC 00087: LabVIEW Datalogging and Supervisory Control Module Overview

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/overview.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Datalogging and Supervisory Control (DSC) Module is add-on software for the LabVIEW programming environment. You can use this module to develop a distributed monitoring and control system with tags ranging from a few dozen to tens of thousands. It includes tools for logging data to a net

### LabVIEW Datalogging and Supervisory Control
 Module
 Overview

The LabVIEW Datalogging and Supervisory Control (DSC) Module is add-on software for the
 LabVIEW programming environment. You can use this module to develop a distributed
 monitoring and control system with tags ranging from a few dozen to tens of thousands.
 It includes tools for logging data to a networked historical database, tracking
 real-time and historical trends, managing alarms and events, networking LabVIEW
 Real-Time targets and OPC devices into one complete system, and adding security to user
 interfaces. You can choose from a development license, a deployment license for
 distributing developing code, or a debug/deploy license, which you can use to resolve
 issues on applications that were created with a development license.

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=pass-data-between-labview-and-the-shared-v.html language=enus -->
## TOPIC 00088: Pass Data between LabVIEW and the Shared Variable Engine

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `pass-data-between-labview-and-the-shared-v.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/pass-data-between-labview-and-the-shared-v.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can pass data between LabVIEW and the Shared Variable Engine (SVE) by using different data access methods.The complexity of the application you build determines the data access method to use. For example, passing data between LabVIEW and the SVE requires significantly more resources than updatin

### Pass Data between LabVIEW and the Shared
 Variable Engine

You can pass data between LabVIEW and the Shared Variable Engine (SVE) by using different
 data access methods.

The complexity of the application you build determines the data access method to use. For
 example, passing data between LabVIEW and the SVE requires significantly more resources than
 updating a Local Variable in LabVIEW. Therefore, you must minimize the number of writes and
 reads that you make to or from shared variables in a VI. Though performance varies greatly
 depending on the system configuration, the SVE can process at least 5,000 updates per second
 for double-typed shared variables.

You can pass data between LabVIEW and the SVE by using either a static or programmatic data
 access method. The following table describes static and programmatic data access methods that
 you can use:

| Data Access Method | Recommended Use | Supported Method | Required Product |
| --- | --- | --- | --- |
| Static | Small applications that contain a small number of shared variables and do not gain in complexity over time. | Shared Variable nodesFront panel data binding | LabVIEW Development System |
| Programmatic | Applications that contain a large number of shared variables or require dynamic creation of shared variables. | Shared Variable VI and functionsShared variable Event structure supportTag VIs | LabVIEW Datalogging and Supervisory Control (DSC) Module |

#### Shared Variable Nodes (Static Data Access
 Method)

You can configure Shared Variable nodes to read data
 from or write data to the SVE. Shared Variable nodes update automatically
 if you rename or move the corresponding shared variable in a project. Thus, you also can use
 this method when you develop an entire application within one project. However, with
 Shared Variable nodes, you cannot change the source of the data at run
 time. Shared Variable nodes also are difficult to use in subVIs.
 Therefore, maintaining or reusing applications developed with this method can be difficult
 because this method has limited scalability.

#### Front Panel Binding (Static Data Access
 Method)

You can bind shared variables to a front panel object using the NI-PSP.
 Binding a front panel object enables you to create a flexible and reconfigurable user
 interface with minimal programming requirements. You can configure front panel data binding
 by using VI Server properties and methods. To set the URL of a front panel control bound
 using the NI-PSP, obtain a control reference to the control or indicator and write to the
 Data Binding:Path property of the control.

Note

#### Shared Variable VI and Functions
 (Programmatic Data Access Method)

If you want to allow for a growing application,
 you can use the Shared Variable VI and Functions with the NI
 Publish-Subscribe Protocol (NI-PSP) to read data from or write data to the SVE
 programmatically. The Shared Variable VI and functions behave similarly
 to the Shared Variable node. However, with the Shared
 Variable VI and functions, you can reconfigure the source of the data at run
 time.

#### Shared Variable Event Structure Support
 (Programmatic Data Access Method)

The DSC Module enables you to monitor shared
 variables using the Shared Variable VIs and the Event Structure.
 Shared Variable Event structure support allows you to receive raw event
 data directly from the SVE. This programming model most closely resembles the execution
 model running in the SVE. Shared variable Event structure support is read-only but allows
 you to process all events, including value changes, quality changes, instantiations, and
 deletions, that the SVE passes. This programmatic data access method is useful in
 supervisory control applications where the VI needs to take a predefined action upon
 encountering a change in the system.

#### Tags VIs (Programmatic Data Access
 Method)

Tags are data sources that contain values, traces, alarms, and events of
 multiple shared variables and I/O server data items. You can manage the following shared
 variable properties programmatically by using the Tags VIs.

- Values of shared variables
- Alarms of shared variables
- Bindings between front panel objects and shared variables
- Trends of shared variables

Parent topic:

The Shared Variable Engine

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=print-alarm-and-event-data.html language=enus -->
## TOPIC 00089: Print Alarm and Event Data

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `print-alarm-and-event-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/print-alarm-and-event-data.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Alarm Printer I/O server to print alarms and events that LabVIEW processes generate. You can print all available information about an alarm or event, or you can select the information you want to print.You can use the Alarm Printer I/O server to print alarms and events only to line printers

### Print Alarm and Event Data

Use the Alarm Printer I/O server to print alarms and events that LabVIEW processes
 generate. You can print all available information about an alarm or event, or you
 can select the information you want to print.

You can use the Alarm Printer I/O server to print alarms and events only to line printers through
 a parallel (LPT) or serial (COM) port connection. Refer to the printer documentation to
 determine if the printer supports line printing.

Right-click My Computer or a LabVIEW project library name in the
 Project Explorer window and select New»I/O
 Server from the shortcut menu to display the Create New
 I/O Server dialog box. Select Alarm Printer from
 the I/O Server Type list and click the
 Continue button to display the Configure Alarm
 Printer I/O Server dialog box. After you configure and deploy this
 I/O server, LabVIEW prints any alarms or events that LabVIEW processes generate to
 the printer you specify.

Use the View I/O Items dialog box to determine if the printing was
 successful or if a printer failure occurred. Right-click the Alarm Printer I/O
 server in the Project Explorer window and select
 View I/O Items to display the View I/O
 Items dialog box.

Parent topic:

Use Alarms and Events in DSC Module Applications

Related tasks:

- Printing Alarms and Events

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=print-citadel-data.html language=enus -->
## TOPIC 00090: Print Citadel Data

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `print-citadel-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/print-citadel-data.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can print logged historical data in the following ways: Print historical data trends from the Historical Data Viewer. You can export data to a spreadsheet or to HTML format. Print historical data from a spreadsheet. To export historical data, use the Write Traces to Spreadsheet VI or Write Trace

### Print Citadel Data

You can print logged historical data in the following ways:

- Print historical data trends from the Historical Data Viewer . You can export
 data to a spreadsheet or to HTML format.
- Print historical data from a spreadsheet. To export historical data, use the Write
 Traces to Spreadsheet VI or Write Traces
 to Spreadsheet File VI. You then can print the
 data from the resulting spreadsheet file.
- Print historical data from a text file that you create by exporting to a spreadsheet file.
- Use an ODBC-compatible application to query the Citadel historical database
 and print the results.

Parent topic:

Logging Historical Data to the Citadel Database

Related concepts:

- Access Citadel Data using ODBC Queries

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=printing-alarms-and-events.html language=enus -->
## TOPIC 00091: Printing Alarms and Events

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `printing-alarms-and-events.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/printing-alarms-and-events.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Alarm Printer I/O server to print alarms and events that LabVIEW processes generate. You can print all available information about an alarm or event, or you can select the information you want to print.You can use Alarm Printer I/O server to print alarms and events through serial ports. The

### Printing Alarms and Events

Note

Complete the following steps to create an Alarm Printer I/O server and print alarm and event
 data:

1. Configure alarms for a shared variable.
2. Deploy the shared variable. After you deploy the shared variable, LabVIEW can send the values of the shared variable to the SVE. When these values trigger alarms or events, the Alarm Printer I/O server you configure sends the alarm or event data to the printer.
3. Right-click My Computer or a LabVIEW project library
 name in the Project Explorer window and select
 New»I/O Server from the shortcut menu to display the
 Create New I/O Server dialog box.
4. Select Alarm Printer from the I/O Server
 Type list and click the Continue button
 to display the Configure Alarm Printer I/O Server dialog
 box.
5. On the Port Settings page, configure the line printer to which you want to print the alarm and event data.
6. Click the Format tab.
7. On the Format page, place checkmarks in the checkboxes for the information that you want to print. Specify the Date Format and Time Format if you want to print the Set Time, Ack Time, or Clear Time.
8. Click the OK button. The new I/O server appears under the project library you selected or, if you did not specify a project library, under a new project library.
9. Right-click the Alarm Printer I/O server in the Project Explorer window and select Deploy from the shortcut menu to deploy the I/O server. After you deploy the I/O server, the I/O server can send alarm and event data that LabVIEW processes generate to the printer that you specified.

```text
[Alarm or Event], [Object Name], [Set Time], [Set User], [Ack Time], [Ack User], [Clear Time], [Clear User], [Priority], [Area], [Value], [Setpoint], [Description], [Ack Comment].
```

Parent topic:

Use Alarms and Events in DSC Module Applications

Related concepts:

- Pass Data between LabVIEW and the Shared Variable Engine

Related tasks:

- Configuring Alarms

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=publish-shared-variables-to-epics.html language=enus -->
## TOPIC 00092: Publish Shared Variables to an EPICS Network

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `publish-shared-variables-to-epics.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/publish-shared-variables-to-epics.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you publish a shared variable, the EPICS Server I/O server creates a Process Variable (PV) for this shared variable and binds this shared variable to this PV. The type of this PV corresponds to the data type of this shared variable. For example, when you publish a shared variable with a data ty

### Publish Shared Variables to an EPICS
 Network

When you publish a shared variable, the EPICS Server I/O server creates a Process
 Variable (PV) for this shared variable and binds this shared variable to this PV.

The type of this PV corresponds to the data type of this shared variable. For example,
 when you publish a shared variable with a data type of Double, the
 EPICS Server I/O server creates a PV with a type of DBF_DOUBLE for
 this shared variable. After you deploy the processes that contain this shared variable
 and this EPICS Server I/O server, the EPICS Server I/O server publishes this PV to the
 EPICS network by using the CA network protocol.

You can publish the following types of shared variables by using EPICS Server I/O
 servers:

| Shared Variable Data Type | PV Type | Data Type Description | PV Category |
| --- | --- | --- | --- |
| Single | DBF_FLOAT | Single-precision floating-point number | Numeric |
| Double | DBF_DOUBLE | Double-precision floating-point number |  |
| Int8 | DBF_CHAR | 8-bit integer |  |
| UInt8 | DBF_UCHAR | Unsigned 8-bit integer |  |
| Int16 | DBF_SHORT | 16-bit integer |  |
| UInt16 | DBF_USHORT | Unsigned 16-bit integer |  |
| Int32 | DBF_LONG | 32-bit integer |  |
| UInt32 | DBF_ULONG | Unsigned 32-bit integer |  |
| Boolean | DBF_ENUM | True or False logical value | Logical |
| String | DBF_String | A sequence of characters representing readable text | String |
| Array of Single | DBF_FLOAT | Array of single-precision floating-point numbers | Array |
| Array of Double | DBF_DOUBLE | Array of double-precision floating-point numbers |  |
| Array of Boolean | DBF_ENUM | Array of True or False logical values |  |
| Array of Int8 | DBF_CHAR | Array of 8-bit integers |  |
| Array of UInt8 | DBF_UCHAR | Array of unsigned 8-bit integers |  |
| Array of Int16 | DBF_SHORT | Array of 16-bit integers |  |
| Array of UInt16 | DBF_USHORT | Array of unsigned 16-bit integers |  |
| Array of Int32 | DBF_LONG | Array of 32-bit integers |  |
| Array of UInt32 | DBF_ULONG | Array of unsigned 32-bit integers |  |

Note

Array of Double

DBF_Double

Parent topic:

Use EPICS Server I/O Servers

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=registering-remote-computers-dsc-module.html language=enus -->
## TOPIC 00093: Registering Remote Computers

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `registering-remote-computers-dsc-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/registering-remote-computers-dsc-module.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: You need to register remote computers before setting up networked applications. Complete the following steps to register a remote computer: In LabVIEW, select Tools»Shared Variable»Register Computer to display the Register Remote Computer dialog box. In the Machine Name or IP Address text box, speci

### Registering Remote Computers

You need to register remote computers before setting up networked applications. Complete the
 following steps to register a remote computer:

1. In LabVIEW, select Tools»Shared Variable»Register
 Computer to display the
 Register Remote Computer
 dialog box.
2. In the Machine Name or IP Address text box, specify the computer name or the IP address of the remote computer.
3. Click the OK button to register this computer.

After you register a remote computer, the Distributed System Manager displays this computer under
 the Network Items folder in the system tree
 pane. You also can register and unregister a remote computer by
 using the System Manager. In LabVIEW, select
 Tools»Distributed System Manager to
 launch the System Manager.

Parent topic:

Network and Deploy Applications

Related tasks:

- Setting Up Networked Applications

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=scaling-boolean-shared-variables.html language=enus -->
## TOPIC 00094: Scaling Boolean Shared Variables

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `scaling-boolean-shared-variables.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/scaling-boolean-shared-variables.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: You can use scaling only for network-published shared variables, I/O variables, or I/O aliases. When the shared variable you want to scale is a network-published shared variable, it must have a data source. Configure a network-published shared variable to have a data source by placing a checkmark in

### Scaling Boolean Shared Variables

Note

Enable Aliasing

Variable

Shared
 Variable Properties

Shared variables with a data type of Boolean can have inverted scaling. Complete the following
 steps to scale Boolean shared variables:

1. Right-click a target or a LabVIEW project library in the Project
 Explorer window and select New»Variable
 from the shortcut menu to display the Shared Variable
 Properties dialog box. 
 You also can right-click an existing shared variable in the Project
 Explorer window and select Properties
 from the shortcut menu to display this dialog box.
2. Select Scaling to display the Scaling page.
3. Place a checkmark in the Enable Scaling checkbox.
4. Place a checkmark in the Invert checkbox for the Shared Variable Engine
 (SVE) to invert the Boolean value when the SVE communicates with the device
 server.
5. Click the OK button to close the Shared
 Variable Properties dialog box.

Use the SharedVariableIO properties to scale Boolean shared variables programmatically.

Parent topic:

Edit Shared Variable Properties

Related concepts:

- Configure Scaling for Shared Variables
- The Shared Variable Engine

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=scaling-numeric-shared-variables.html language=enus -->
## TOPIC 00095: Scaling Numeric Shared Variables

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `scaling-numeric-shared-variables.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/scaling-numeric-shared-variables.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: You can use scaling only for network-published shared variables, I/O variables, or I/O aliases. When the shared variable you want to scale is a network-published shared variable, it must have a data source. Configure a network-published shared variable to have a data source by placing a checkmark in

### Scaling Numeric Shared Variables

Note

Enable Aliasing

Variable

Shared Variable Properties

Complete the following steps to scale shared variables:

1. Right-click a shared variable in the Project
 Explorer window and select
 Properties from the shortcut
 menu to display the Shared Variable
 Properties dialog box.
2. Select Scaling to display the
 Scaling page.
3. Place a checkmark in the Enable Scaling checkbox.
4. Select one of the following scaling options from the Scale Type
 pull-down menu. 
 Linear—Enables a linear
 (mx + b)
 conversion between raw and engineering
 ranges.
 Square Root—Enables a square root conversion between the raw (Raw Zero
 Scale and Raw Full Scale) and engineering
 (Engineering Zero Scale and Engineering Full
 Scale) ranges, which is b +
 m *
 sqrt(raw –
 o) where b =
 Engineering Zero Scale, m =
 (Engineering Full Scale – Engineering Zero
 Scale)/sqrt(Raw Full Scale – Raw Zero Scale), and
 o = Raw Zero Scale.
5. Optional: 
 In the Engineering Unit test box,
 specify the unit of data measurement, such as degrees
 Celsius, pounds, grams, and so on.
6. Specify the raw and engineering ranges in the Raw Full Scale, Raw Zero Scale, Engineering Full Scale, and Engineering Zero Scale numeric controls.
7. Optional: 
 Place a checkmark in the Coerce to Range
 checkbox to coerce the data to the specified range.
8. Click the OK button to close the
 Shared Variable Properties
 dialog box.

Use the SharedVariableIO properties to scale shared variables programmatically.

Parent topic:

Edit Shared Variable Properties

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=scaling-u32-bit-field-shared-variables.html language=enus -->
## TOPIC 00096: Scaling U32 Bit Field Shared Variables

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `scaling-u32-bit-field-shared-variables.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/scaling-u32-bit-field-shared-variables.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: You can use scaling only for network-published shared variables, I/O variables, or I/O aliases. When the shared variable you want to scale is a network-published shared variable, it must have a data source. Configure a network-published shared variable to have a data source by placing a checkmark in

### Scaling U32 Bit Field Shared Variables

Note

Enable Aliasing

Variable

Shared Variable Properties

Shared variables with a data type of U32 Bit Field can have invert-mask and/or select-mask
 scaling. Complete the following steps to scale bit array shared variables:

1. Right-click a target or a LabVIEW project library in the
 Project Explorer window and
 select New»Variable from the shortcut
 menu to display the Shared Variable
 Properties dialog box. 
 You also can right-click an existing shared variable in the
 Project Explorer window and
 select Properties from the shortcut
 menu to display this dialog box.
2. Select Scaling from the list of this dialog box to
 display the Scaling page.
3. Place a checkmark in the Enable Scaling checkbox.
4. In the Scaling Invert Mask text box, set the bits you need to scale. LabVIEW masks the bits you do not set and reports these masked bits in an array as zeros.
5. In the Scaling Select Mask text box, set which bits are inverted between
 the device server and the Shared Variable Engine. You can invert only the bits
 specified in this text box.
6. Click the OK button to close the Shared
 Variable Properties dialog box.

Use the SharedVariableIO properties to scale U32 Bit Array shared variables programmatically.

Parent topic:

Edit Shared Variable Properties

Related concepts:

- Pass Data between LabVIEW and the Shared Variable Engine

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=set-access-to-front-panel-controls-and-in.html language=enus -->
## TOPIC 00097: Set Access to Front Panel Controls and Indicators

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `set-access-to-front-panel-controls-and-in.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/set-access-to-front-panel-controls-and-in.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure security settings for front panel controls and indicators to restrict access to the objects.To control access to a front panel object, right-click the object and select Properties from the shortcut menu and select the Security tab in the Properties dialog box. Click the Add button

### Set Access to Front Panel Controls and
 Indicators

You can configure security settings for front panel controls and indicators to restrict
 access to the objects.

To control access to a front panel object, right-click the object and select
 Properties from the shortcut menu and select the
 Security tab in the Properties dialog box.
 Click the Add button to add to the list all the individual user
 accounts or groups of users you want to have access to that object and set the access level
 for each user or group. LabVIEW stores security settings with each control.

Front Panel Security

Note

#### Restricting Access within an HMI
 Application

Use the Security VIs to restrict access and enforce
 security within a Human Machine Interface (HMI).

#### Setting an Engine User Account

You
 can specify an engine user to ensure that the local Shared Variable Engine (SVE) has access
 to shared variable data no matter who is logged into the local LabVIEW Datalogging and
 Supervisory Control (DSC) Module application. If a locally-defined shared variable in the
 SVE attempts to access shared variable data across the network using the Publish-Subscribe
 Protocol networking protocol, the local SVE uses the engine user account.

If the
 remote computer recognizes the account, the computer grants the access rights defined for
 that account. If the remote computer does not recognize the account, the computer grants the
 proxy user access rights that are defined on the remote computer.

#### Prompting an Operator to Log into an
 Application

Use the Security Invoke Login Dialog VI to launch
 the Login dialog box and return the user name and access level. You
 can include the application control login as part of the HMI.

#### Logging an Operator into or out of an
 Application Programmatically

Use the Security Programmatic
 Login VI to log in an operator. To use this VI, you must enter a user name and
 password. If you use the VI correctly, the user is logged into the system, and a
 Login dialog box does not appear.

Use the Security
 Programmatic Logout VI to log the current user out of the DSC
 Module.

#### Identifying the Current Operator

Use the Security Interactive User Info VI to return the name
 and current operator name and information. Use this VI to retrieve information about any
 user account.

Parent topic:

Configure Security

Related concepts:

- Pass Data between LabVIEW and the Shared Variable Engine

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=set-alarms-for-shared-variables.html language=enus -->
## TOPIC 00098: Set Alarms for Shared Variables

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `set-alarms-for-shared-variables.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/set-alarms-for-shared-variables.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use alarms to notify users of abnormal conditions for a given shared variable.You can specify whether to enable alarms, under what circumstances a shared variable is in alarm, the priority level of an alarm, and how alarms are acknowledged. Each alarm limit has a priority ranging between 1 and 1,000

### Set Alarms for Shared Variables

Use alarms to notify users of abnormal conditions for a given shared variable.

You can specify whether to enable alarms, under what circumstances a shared variable is in alarm,
 the priority level of an alarm, and how alarms are acknowledged. Each alarm limit has a
 priority ranging between 1 and 1,000.

The LabVIEW Datalogging and Supervisory Control (DSC) Module generates alarms depending on the
 value or status of a shared variable. The alarms based on value vary with the shared
 variable data type. For any shared variable, if the status is bad, the DSC Module can
 generate a bad status alarm.

#### Defining an Alarm Area

Use
 an alarm area to define a subset of shared variables in the system. You also can use
 an alarm area to perform tasks on a set of shared variables at the same
 time.

You can specify the area to which an alarm belongs on the
 Alarming page of the Shared Variable
 Properties dialog box. You also can use the
 Alarming.AlarmName.Area SharedVariableIO property, where
 AlarmName is HI_HI, HI, LO_LO, LO, RoC, U32 Bit Field, Bad
 Status, or Boolean, to specify an alarm area programmatically.

#### Configuring Alarm Acknowledgement
 Mode

You can use one of two modes to handle shared variables that were previously in alarm
 but have returned to normal: Auto Acknowledge and User Must Acknowledge. Configure
 these modes on the Alarming page for each shared variable
 alarm. If you configure an alarm for automatic acknowledgement, the acknowledgment
 status automatically changes from unacknowledged to acknowledged when the shared
 variable returns to normal. If you configure an alarm for user acknowledgement, the
 status remains unacknowledged until the operator acknowledges the
 alarm.

#### Setting Alarms for Numeric Shared
 Variables

You can configure numeric shared variables to have the following alarms: HI_HI, HI,
 LO, LO_LO, Bad Status, and RoC (Rate of Change). The DSC Module calculates alarms
 after performing scaling. The DSC Module lists alarm levels in engineering
 units.

#### Setting Alarm Deadband on Numeric
 Shared Variables

Alarm deadband defines the percentage a shared variable
 value must change from the alarm limit before the change is considered a significant
 change. For example, if a shared variable that represents a temperature value hovers
 near an alarm limit of 40°C, the shared variable might trigger an alarm many times
 in a relatively short period of time.

The following table shows examples of
 events with alarm deadband set to 0.0%:

| Time | Value | Change | Alarm Condition |
| --- | --- | --- | --- |
| 9:15:05 | 41.1 | Yes | HI |
| 9:15:10 | 39.9 | Yes | None |
| 9:15:15 | 40.1 | Yes | HI |
| 9:15:20 | 38.5 | Yes | None |

This type of situation clogs event files with redundant information and can
 frustrate operators who have to acknowledge alarms even when the change is
 insignificant. Increase the alarm deadband to alleviate this problem.

For the
 shared variable to trigger an alarm, the shared variable value must exceed the exact
 alarm value (in the previous example, 40). However, to be considered normal again,
 it must deviate from the alarm value by an amount greater than the alarm deadband.
 For example, if the range is 0 to 40 °C, an alarm deadband of 1.0%, or one degree
 Celsius, eliminates unnecessary events.

The following table shows examples of
 events with alarm deadband set to 1.0%:

| Time | Value | Change | Alarm Condition |
| --- | --- | --- | --- |
| 9:15:05 | 41.1 | Yes | HI |
| 9:15:10 | 39.9 | No | HI |
| 9:15:15 | 40.1 | No | HI |
| 9:15:20 | 38.5 | Yes | None |

#### Setting Alarms for Boolean Shared
 Variables

You can configure Boolean shared variables to have two alarm states—either the shared
 variable is in alarm or it is not. You can determine whether a Boolean shared
 variable is in alarm when it is ON (high) or OFF (low).

You also can specify a bad status alarm.

#### Setting Alarms for U32 Bit Field
 Shared Variables

You can configure U32 bit field shared variables to have
 one of two types of alarms — either any or all of its bits are in the alarm
 state.

You also can specify a bad status alarm.

#### Setting Alarms for All Other Shared Variable Data Types

You can specify a bad status alarm for all other types of shared variables.

Parent topic:

Shared Variable Properties

Related concepts:

- Supported Shared Variable Types

Related tasks:

- Configuring Alarms for Numeric Shared Variables
- Configuring Alarms for Boolean Shared Variables
- Configuring Alarms for U32 Bit Field Shared Variables

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=set-shared-variable-deadbands.html language=enus -->
## TOPIC 00099: Set Shared Variable Deadbands

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `set-shared-variable-deadbands.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/set-shared-variable-deadbands.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: A deadband is a filter that eliminates noise from data. LabVIEW compares any changes in value from a data point to the previous value. The new value replaces the old value only if the difference between the new value and the previous value exceeds the deadband.You can set deadbands only for network-

### Set Shared Variable Deadbands

A deadband is a filter that eliminates noise from data. LabVIEW compares any changes in
 value from a data point to the previous value. The new value replaces the old value only
 if the difference between the new value and the previous value exceeds the deadband.

You can set deadbands only for network-published shared variables with a floating-point data
 type.

Note

The Shared Variable Engine (SVE) uses update deadband and logging deadband values to eliminate
 unnecessary processing on insignificant data value changes. A deadband defines what
 constitutes a significant change. The SVE ignores an operation if the change in data is
 not considered significant. By increasing the deadband size, you can reduce the strain
 on the SVE, though this might compromise data resolution.

#### Deadbanding Interaction

You
 can configure the following deadband settings when you configure individual shared
 variables: update deadband, logging deadband, and alarm deadband.

The update
 deadband affects how the SVE updates values. Logging deadband and alarm deadband
 values operate on the values that have passed through the update deadband value. If
 you set the update deadband value greater than the logging or alarm deadband values,
 the update deadband might interfere with the logging or alarm deadband settings,
 resulting in inadequate historical logging or alarm management.

The OPC server
 applies the deadband you set in the Configure OPC Client I/O
 Server dialog box before sending the data to the SVE. The SVE
 applies the logging deadband upon receiving the data. The effects of this deadband
 setting also can apply to the update deadband and alarm deadband values. Refer to
 the OPC server documentation before you change the deadband settings for an OPC
 Client I/O server. Not all OPC servers support deadbands.

#### Setting Deadbands for OPC Client I/O
 Servers

The deadband is the percent of change within a range that a value
 from the OPC server must change before the OPC server communicates the value to the
 SVE. Settings made in the OPC server determine the range for each data item. Refer
 to the OPC server documentation for more information about that server. Set the
 deadband for an OPC Client I/O server in the Configure OPC Client I/O
 Server dialog box.

#### Setting Update
 Deadbands

When you set an update deadband value, the SVE compares any new
 value acquired to the existing value. The new value replaces the old value only if
 the percentage difference between the new value and the previous value equals or
 exceeds the deadband. Set the update deadband value by using the Update
 Deadband:Enabled and Update Deadband:Source or Update Deadband:User SharedVariableIO
 properties.

For example, for a data point with a range of values of 0 to 100,
 set the update deadband to 1%. The existing value in the SVE is 12.3. If the SVE
 reports a new value of 13, the SVE does not update because the change in value did
 not equal or exceed the deadband. If the SVE reports a new value of 11, it updates
 because the difference is greater than the deadband.

#### Setting Logging
 Deadbands

When you set a logging deadband value, the SVE compares any new
 value acquired to the existing value. The SVE logs the new value only if the
 percentage difference between the new value and the previous value equals or exceeds
 the deadband. Set the logging deadband value in the Value Deadband field of the
 Logging page of the Shared Variable Properties dialog box.
 You also can set the logging deadband value using the Logging:Value Deadband
 SharedVariableIO property.

The default setting for the logging deadband is
 1%.

For example, for a data point with a range of values of 0 to 100, set the
 logging deadband value to 2%. The last value the SVE logged was 12.3. When the SVE
 updates to 11, it does not log the updated value because the change in value is less
 than the 2% deadband. The value in the SVE must be equal to or greater than 14.3 or
 equal to or less than 10.3 for the SVE to log the data point. If the value in the
 SVE is 14.5, the SVE logs this new value because the value exceeds the 2% deadband.
 The next value that the SVE logs then must be equal to or greater than 16.5 or equal
 to or less than 12.5.

#### Setting Alarm Deadbands

When you set an alarm deadband value, the LabVIEW Datalogging and Supervisory
 Control (DSC) Module compares any new value acquired to the existing value. The SVE
 clears an active alarm if the percentage difference between the new value and the
 previous value equals or exceeds the deadband. Set the alarm deadband using the
 Alarming:AlarmName:Deadband SharedVariableIO property, where AlarmName is HI_HI, HI,
 LO_LO, LO, RoC, U32 Bit Field, Bad Status, or Boolean, or when you configure alarms
 for a shared variable.

For example, for a data point with a range of values of
 0 to 100, set a LO condition alarm at a value of 12 with a deadband of 1.5%. The
 alarm condition does not trigger until the SVE value drops to 12 or below. The alarm
 stays active until the SVE value rises to 13.5 or greater.

Parent topic:

Shared Variable Properties

Related concepts:

- The Shared Variable Engine
- Creating OPC Client I/O Servers

Related tasks:

- Setting Shared Variable Deadbands

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=set-the-database-read-rate.html language=enus -->
## TOPIC 00100: Set the Database Read Rate

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `set-the-database-read-rate.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/set-the-database-read-rate.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Historical VIs to obtain or read historical information about shared variables and to manage Citadel databases.All VIs that read information from the Shared Variable Engine (SVE) can return information immediately or wait for the database to update with new information before returning infor

### Set the Database Read Rate

Use the Historical VIs to obtain or read historical information about
 shared variables and to manage Citadel databases.

All VIs that read information from the Shared Variable Engine (SVE) can return information
 immediately or wait for the database to update with new information before returning
 information. The timeout input controls this behavior. This timeout
 value tells the VI how long to wait, in seconds, for the shared variable information to update
 in the SVE.

The following table describes the behavior for each timeout value:

| VI Timeout Input | Behavior |
| --- | --- |
| 0 | VI immediately reads the database and returns the current shared variable information. |
| Less than 0 | VI continues to wait until the shared variable updates. |
| Greater than 0 | VI waits until the shared variable updates in the database or the time between updates exceeds the timeout period, whichever occurs first, then reads the database and returns the current shared variable information. |

If you leave the timeout input unwired, the default value is
 0. How you use the timeout input depends on whether
 you want to implement event-driven or polled programming techniques in the Human Machine
 Interface (HMI).

Parent topic:

Displaying and Controlling Data

Related concepts:

- Pass Data between LabVIEW and the Shared Variable Engine

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=setting-a-proxy-user-account.html language=enus -->
## TOPIC 00101: Setting a Proxy User Account

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `setting-a-proxy-user-account.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/setting-a-proxy-user-account.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to set proxy user access.Select Tools»Options to display the Options dialog box.Select Security from the Category list to display the Security Options page.In the Shared variable engine user section, specify the User name and Password to use for the Shared Variable Engin

### Setting a Proxy User Account

Complete the following steps to set proxy user access.

1. Select Tools»Options to display the Options dialog
 box.
2. Select Security from the Category list to display
 the Security Options page.
3. In the Shared variable engine user section, specify the User
 name and Password to use for the Shared
 Variable Engine (SVE) user. The default setting for the SVE user is the built-in
 nobody account, which has no password unless you add one.
4. Click the OK button to close the Security Options page.

Parent topic:

Configure Security

Related concepts:

- Pass Data between LabVIEW and the Shared Variable Engine

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=setting-shared-variable-deadbands.html language=enus -->
## TOPIC 00102: Setting Shared Variable Deadbands

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `setting-shared-variable-deadbands.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/setting-shared-variable-deadbands.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: The shared variable deadband settings that you can control directly are the update deadband, logging deadband, and alarm deadband.You can set update deadband and logging deadband for network-published shared variables with floating-point data types. You can set alarm deadband for floating-point and

### Setting Shared Variable Deadbands

Note

Complete the following steps to set shared variable deadband values:

1. Right-click a target or a LabVIEW project library in the Project
 Explorer window and select New»Variable
 from the shortcut menu to display the Shared Variable
 Properties dialog box. 
 You also can right-click an existing shared variable in the Project
 Explorer window and select Properties
 from the shortcut menu to display this dialog box.
2. Set the update deadband:
  1. Select Update Deadband to display the
 Update Deadband page.
  2. Place a checkmark in the Enable Update Deadband
 checkbox.
  3. Enter values in the User deadband (% of range)
 and Source deadband (% of range) numeric
 controls. You must bind this shared variable to a data source to use the
 source deadband.
3. Optional: 
 Set the logging deadband:
  1. Select Logging to display the
 Logging page.
  2. Place a checkmark in the Enable Logging
 checkbox.
  3. Verify that a checkmark is in the Log Data
 checkbox.
  4. Enter a value for the deadband in the Value
 Deadband numeric control.
4. Optional: 
 Set the alarm deadband. 
 Select Alarming to display the
 Alarming page.
 Place a checkmark in the Enable Alarming
 checkbox.
 Place checkmarks in the appropriate cells of the
 Enabled column to enable the alarms.
 Enter values in the appropriate cell of the
 Deadband/Time column for the alarms.
5. Click the OK button.

You also can use the SharedVariableIO properties to set alarm, logging, and update deadbands
 programmatically.

Parent topic:

Edit Shared Variable Properties

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=setting-time-synchronization-for-networked-co.html language=enus -->
## TOPIC 00103: Setting Time Synchronization for Networked Computers

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `setting-time-synchronization-for-networked-co.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/setting-time-synchronization-for-networked-co.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to set time synchronization. Select Tools»Options to display the Options dialog box. Select Shared Variable Engine from the Category list to display the Shared Variable Engine Options page.Notice the Time server search order list. Any computer that is running the time sy

### Setting Time Synchronization for Networked Computers

Complete the following steps to set time
 synchronization.

1. Select Tools»Options to display the
 Options dialog box.
2. Select Shared Variable Engine from the
 Category list to display the Shared
 Variable Engine Options page. Notice the Time server search order list. Any computer
 that is running the time synchronization service can serve as a time server or a
 time client. The primary time server is the first computer listed in the
 Time Server Search Order list. If no computer is set
 as a primary time server, the computer synchronizes to itself.
3. To add a computer to the Time server search order list,
 click the Add button to display the Select
 Computer dialog box.
4. If you know the name of the computer you want to add, you can type the name
 into the Host text box. If you do not know the exact name
 of the computer, you can browse for the computer using the network tree in the
 Machines list. To remove a computer from the Time server search order
 list, select the computer name and click the Remove
 button.
5. To change the order in which computers search for a time synchronization server, select the computer name and click the Up or Down button.
6. Use Sleep time (seconds) to set how long each computer
 waits between each synchronization. Set the primary time synchronization server
 sleep time to 60 seconds. If the primary server is off-line for some reason, a computer scheduled to
 synchronize automatically seeks out the second computer on the synchronization
 server list. At the time of the next synchronization, the computer first looks
 for the primary server before seeking a secondary synchronization server.
7. Click the OK button.
8. Repeat steps 4 through 8 for all computers on the network that you want to synchronize to make sure that the order of search for time servers is the same for all the computers, including the primary time synchronization server.

Parent topic:

Network and Deploy Applications

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=setting-up-networked-applications-dsc-module.html language=enus -->
## TOPIC 00104: Setting Up Networked Applications

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `setting-up-networked-applications-dsc-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/setting-up-networked-applications-dsc-module.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to use a LabVIEW Datalogging and Supervisory Control (DSC) Module application on a network. Register the computers and devices on the network that use Logos networking. Synchronize the clocks of all computers or devices.Verify network paths and names.Make sure all necess

### Setting Up Networked Applications

Complete the following steps to use a LabVIEW
 Datalogging and Supervisory Control (DSC) Module application on a
 network.

1. Register the computers and devices on the network that use
 Logos networking.
2. Synchronize the clocks of all computers or devices.
3. Verify network paths and names.
4. Make sure all necessary services are running.

Parent topic:

Network and Deploy Applications

Related concepts:

- Monitoring Services

Related tasks:

- Registering Remote Computers
- Setting Time Synchronization for Networked Computers

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=share-live-data-using-shared-variables.html language=enus -->
## TOPIC 00105: Share Live Data Using Shared Variables

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `share-live-data-using-shared-variables.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/share-live-data-using-shared-variables.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you have the LabVIEW Datalogging and Supervisory Control (DSC) Module and the LabVIEW Real-Time Module, you can configure shared variables to communicate with both modules.You can use shared variables to share live data with other VIs and other applications, such as the Shared Variable Engine (SV

### Share Live Data Using Shared Variables

If you have the LabVIEW Datalogging and Supervisory Control (DSC) Module and the LabVIEW
 Real-Time Module, you can configure shared variables to communicate with both
 modules.

You can use shared variables to share live data with other VIs and other applications, such as
 the Shared Variable Engine (SVE).

Parent topic:

Shared Variables

Related concepts:

- Pass Data between LabVIEW and the Shared Variable Engine

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=shared-variable-alarming-data-i.html language=enus -->
## TOPIC 00106: Shared Variable Alarming Data Items

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `shared-variable-alarming-data-i.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/shared-variable-alarming-data-i.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you enable alarming for a shared variable and deploy the shared variable, LabVIEW creates shared variable alarming data items in the Shared Variable Engine (SVE). The alarming data items reside in a folder named Alarms and is stored under the shared variable.You use alarming data items to read

### Shared Variable Alarming Data Items

When you enable alarming for a shared variable and deploy the shared variable, LabVIEW
 creates shared variable alarming data items in the Shared Variable Engine (SVE). The
 alarming data items reside in a folder named Alarms and is stored
 under the shared variable.

You use alarming data items to read from and write values to alarms. You can read and write
 alarming data items by using the NI Publish-Subscribe Protocol (NI-PSP) clients, such as
 the Shared Variable node, VI, and functions, the Distributed System Manager, and so on.
 To launch the System Manager from LabVIEW, select Tools»Distributed System
 Manager.

To read from or write a value to an alarming data item, you can specify the data item URL in the
 following format:
 \\computer\process\variable\Alarms\alarm\data_item. If you use
 the Shared Variable Node, VI, and Functions to read and write alarming data items,
 specify the data item URL in the following format:
 ni.var.psp://computer/process/variable/Alarms/alarm/data_item.
 In both URL formats, variable stands for the name of the shared
 variable under which the data item resides and alarm stands for the
 alarm name you specify.

The default values of alarming data items are the values that you specify for the alarming
 property when you configure a shared variable. However, the values that you write to
 alarming data items do not change the values that you specify for the alarming property.
 If you restart the SVE or the computer, LabVIEW initializes the values you specify for
 alarming data items. The values that LabVIEW initializes are the same as the values you
 specify for the alarming property.

The following table lists the shared variable alarming data items that the LabVIEW Datalogging
 and Supervisory Control (DSC) Module supports:

| Data Item | Data Type | Access Type | Description |
| --- | --- | --- | --- |
| Ack | Boolean value | Read | Specifies whether an alarm is acknowledged for a shared variable. |
| AckType | 32-bit unsigned integer | Read/Write | Specifies how an alarm is acknowledged. A value of 0 indicates that LabVIEW acknowledges the alarm when the shared variable value returns to a normal state. When you specify 0 for AckType, the acknowledgement type of the alarm is Auto.A value of 1 indicates that LabVIEW does not acknowledge an alarm until the user acknowledges the alarm regardless of the alarm state. LabVIEW does not generate any new alarm instance before you acknowledge the existing alarm instance. When you specify 1 for AckType, the acknowledgement type of the alarm is User.A value of 3 indicates that LabVIEW does not acknowledge an alarm until the user acknowledges the alarm. LabVIEW generates a new alarm instance whenever the alarm changes from a normal state to an abnormal state. When you specify 3 for AckType, the acknowledgement type of the alarm is Each Occurrence.Note If you specify 3 for AckType, LabVIEW may generate a large number of alarm instances before you acknowledge them. |
| AlarmState | Boolean value | Read/Write | Sets alarm conditions for Boolean shared variables. You use this data item to set the Boolean shared variable to be in alarm state when the value is either TRUE or FALSE. This data item exists when you enable a Boolean alarm. |
| deadband | 64-bit floating-point number | Read/Write | Specifies the alarm deadband for a shared variable as a percentage of the full scale range. This data item exists when you enable a HI_HI alarm, HI alarm, LO alarm, or LO_LO alarm. |
| Description | String | Read | Specifies the description of the alarm. |
| Enable | Boolean value | Read/Write | Specifies whether an alarm is enabled for a shared variable. |
| level | 64-bit floating-point number | Read/Write | Specifies the value, in engineering units, that evokes the alarm condition. This data item exists when you enable a HI_HI alarm, HI alarm, LO alarm, or LO_LO alarm. The level values of the numeric alarms conform to the following rule: HI_HI level>HI level>LO level>LO_LO level. |
| Log | Boolean value | Read/Write | Specifies whether alarm logging is enabled. |
| Priority | 32-bit unsigned integer | Read/Write | Specifies the priority of the alarm. Enter a value between 1 and 1000, where 1000 is the highest priority. |
| Set | Boolean value | Read | Specifies whether an alarm is set for a shared variable. |

Parent topic:

Shared Variable Properties

Related concepts:

- Shared Variables
- The Shared Variable Engine
- Configure Shared Variables

Related tasks:

- Deploying a Shared Variable

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=shared-variable-engine-error-handling.html language=enus -->
## TOPIC 00107: Shared Variable Engine Error Handling

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `shared-variable-engine-error-handling.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/shared-variable-engine-error-handling.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Shared Variable Engine (SVE) generates alarms and events when errors occur in LabVIEW Datalogging and Supervisory Control (DSC) Module applications.You can view these alarms and events by using the Distributed System Manager. You also can view errors for logged data in the Historical Data Viewer

### Shared Variable Engine Error Handling

The Shared Variable Engine (SVE) generates alarms and events when errors occur in LabVIEW
 Datalogging and Supervisory Control (DSC) Module applications.

You can view these alarms and events by using the Distributed System Manager. You also can view
 errors for logged data in the Historical Data Viewer, available in
 the Measurement & Automation Explorer. LabVIEW logs engine alarm errors to the
 database for the process that generates the alarm. If this database is not available,
 LabVIEW logs the errors to the default database under the System
 process.

The SVE also reports server status updates and critical errors, such as invalid process
 configurations or failed database connections. You can view these errors in the Windows
 Event Viewer. In the Windows Control Panel, select
 Administrative Tools»Event Viewer to display the Windows
 Event Viewer.

DSC Module VIs and functions report errors by using standard LabVIEW error in
 and error out indicators.

Parent topic:

The Shared Variable Engine

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=shared-variable-properties.html language=enus -->
## TOPIC 00108: Shared Variable Properties

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `shared-variable-properties.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/shared-variable-properties.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Shared variable properties determine how the Shared Variable Engine (SVE) handles a shared variable.You can use the shared variable properties to edit the following shared variable configurations:Initialize shared variable valuesSet alarm levels and priorities for the shared variable dataLog the sha

### Shared Variable Properties

Shared variable properties determine how the Shared Variable Engine (SVE) handles a
 shared variable.

You can use the shared variable properties to edit the following shared variable
 configurations:

- Initialize shared variable values
- Set alarm levels and priorities for the shared variable data
- Log the shared variable to a historical database
- Scale data
- Set deadbands to filter the shared variable data
- Update security settings for the shared variable

Note

The shared variable properties that you can edit depends on the data type of the shared variable
 and on your target and licensed product(s).

- [Initialize Shared Variable Values](initialize-shared-variable-values.html)
- [Set Alarms for Shared Variables](set-alarms-for-shared-variables.html)
- [Enable Data and Event Logging with Shared Variables](enable-data-and-event-logging-with-shared-v.html)
- [Configure Scaling for Shared Variables](configure-scaling-for-shared-variables.html)
- [Set Shared Variable Deadbands](set-shared-variable-deadbands.html)
- [Supported Shared Variable Properties Based on Target and Products](supported-shared-variable-properties-based-on.html)
- [Supported Shared Variable Properties Based on Data Type](supported-shared-variable-properties-based.html)
- [Supported Shared Variable Types](supported-shared-variable-types.html)
- [Edit Shared Variable Properties](edit-shared-variable-properties.html)
- [Configure Shared Variables](configure-shared-variables-dsc-module-or-re.html)
- [Shared Variable Alarming Data Items](shared-variable-alarming-data-i.html)

Parent topic:

Managing I/O with Shared Variables

Related concepts:

- Shared Variables
- Set Shared Variable Deadbands
- Configure Security

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=shared-variables-and-io-servers.html language=enus -->
## TOPIC 00109: Shared Variables and I/O Servers

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `shared-variables-and-io-servers.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/shared-variables-and-io-servers.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Shared variables form the basis for the I/O model in the DSC Module. Each shared variable represents one I/O point. You can bind a shared variable to a single I/O source. You can configure data logging, alarming, and security settings for shared variables. Use LabVIEW projects and LabVIEW project li

### Shared Variables and I/O Servers

Shared variables form the basis for the I/O model in the DSC Module. Each shared variable
 represents one I/O point. You can bind a shared variable to a single I/O source.

You can configure data logging, alarming, and security settings for shared variables. Use
 LabVIEW projects and LabVIEW project libraries to organize hierarchies of shared
 variables in a DSC Module application.

You can use shared variables with or without data binding. With data binding, a data
 source automatically updates the shared variable value. The DSC Module includes several
 I/O servers, including OPC Client and Modbus I/O servers, that you can use to acquire
 data from Programmable Logic Controllers (PLCs) or other similar devices.

Parent topic:

Components of a DSC Module Application

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=shared-variables.html language=enus -->
## TOPIC 00110: Shared Variables

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `shared-variables.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/shared-variables.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use shared variables to represent a real-world input/output point. Shared variables communicate between VIs, remote computers, and hardware through the Shared Variable Engine (SVE).With the LabVIEW Datalogging and Supervisory Control (DSC) Module, you can configure shared variables by editin

### Shared Variables

You can use shared variables to represent a real-world input/output point. Shared
 variables communicate between VIs, remote computers, and hardware through the Shared
 Variable Engine (SVE).

With the LabVIEW Datalogging and Supervisory Control (DSC) Module, you can configure shared
 variables by editing the following shared variable properties:

- Shared variable data type
- Initial values
- Update deadbands, logging deadbands, and alarm deadbands
- Units of measurement to data
- Alarm messages for a shared variable whose values enter the alarm ranges you set
- Data binding
- Security settings
- Scaling

Note

LabVIEW saves shared variable information in LabVIEW project library
 (.lvlib) files. You can include as many shared variables in a
 project library as you need. However, you might notice performance issues if you have
 insufficient system resources.

- [Bind Shared Variables to OPC Server Data Items](bind-shared-variables-to-opc-server-data-i.html)
- [Share Live Data Using Shared Variables](share-live-data-using-shared-variables.html)
- [Create Shared Variables](create-shared-variables.html)
- [Deploying, Committing, and Monitoring Shared Variables](deploying-committing-and-monitoring-shared-va.html)

Parent topic:

Managing I/O with Shared Variables

Related concepts:

- Shared Variable Properties

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=sql-examples.html language=enus -->
## TOPIC 00111: SQL Examples

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `sql-examples.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/sql-examples.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following examples are typical query statements. Queries might be more involved, depending on the system requirements. Aliases Table Example QueriesThe following example queries obtain Citadel data from the Aliases table: Retrieve all aliases: SELECT * FROM Aliases Retrieve all aliases of Proces

### SQL Examples

The following examples are typical query statements. Queries might be more involved,
 depending on the system requirements.

#### Aliases Table Example
 Queries

The following example queries obtain Citadel data
 from the Aliases table:

- Retrieve all aliases: SELECT * FROM Aliases
- Retrieve all aliases of Process_1 traces: SELECT * FROM
 Aliases WHERE FullName LIKE '%Process_1%'
- Retrieves all data set aliases: SELECT * FROM Aliases WHERE AliasName LIKE
 'DS_%'
- Retrieves all non data set traces: SELECT * FROM Aliases WHERE AliasName NOT
 LIKE 'DS_%'

#### IntData Table Example
 Queries

The following example queries obtain Citadel data
 from the IntData table:

- Select data over a specified time at one-minute intervals
  - SELECT * FROM IntData WHERE LocalTime BETWEEN '2001-11-29 17:00:00'
 AND '2001-11-29 18:00:00' AND IntInterval = '1:0'
- Select data over a specified time at one-minute intervals and orders rows based on
 values in column: computername/my_process/pot1@value
  - SELECT * FROM IntData WHERE LocalTime BETWEEN '2001-11-29 17:00:00'
 AND '2001-11-29 18:00:00' AND IntInterval = '1:0' ORDER BY
 "computername/my_process/pot1@value"
- Select data over a specified time at one-minute intervals and orders rows based on
 values in column computername/my_process/pot1@value in descending
 order
  - SELECT * FROM IntData WHERE LocalTime BETWEEN '2001-11-29 17:00:00'
 AND '2001-11-29 18:00:00' AND IntInterval = '1:0' ORDER BY
 "computername/my_process/pot1@value" DESC
- Select data over a specified time and value interval at one-minute intervals and
 orders rows based on values in column
 computername/my_process/pot1@value in descending order
  - SELECT * FROM IntData WHERE LocalTime BETWEEN '2001-11-29 17:00:00'
 AND '2001-11-29 18:00:00' AND IntInterval = '1:0' AND
 "computername/my_process/pot1@value" BETWEEN 1.5 AND 5.4 ORDER BY
 "computername/my_process/pot1@value" DESC
- Select data over a specified time at one-minute intervals and returns minimum,
 maximum, and average value of the computername/my_process/pot1@value 
 column
  - SELECT MIN("computername/my_process/pot1@value"),
 MAX("computername/my_process/pot1@value"),
 AVG("computername/my_process/pot1@value") FROM IntData WHERE UTCTime BETWEEN
 '2001-11-29 17:00:00' AND '2001-11-29 18:00:00' AND IntInterval =
 '1:0'

#### RawData Table Example
 Queries

The following example queries obtain Citadel data
 from the RawData table:

- Select the computername\my_process\pot1.value shared variable data
 over a specified time
  - SELECT LocalTime, UTCTime, "computername/my_process/pot1@value" FROM
 RawData WHERE LocalTime BETWEEN '2001-11-29 17:00:00' AND '2001-12-01
 17:00:00'
- Select the computername\my_process\pot1.value shared variable data
 with bad quality over a specified time
  - SELECT LocalTime, UTCTime, "computername/my_process/pot1@value" FROM
 RawData WHERE LocalTime BETWEEN '2001-11-29 17:00:00' AND '2001-12-01
 17:00:00' AND NOT Quality = 0
- Select the computername\my_process\pot1.value shared variable data
 over a specified time and order result rows in descending order
  - SELECT LocalTime, UTCTime, "computername/my_process/pot1@value" FROM
 RawData WHERE LocalTime BETWEEN '2001-11-29 17:00:00' AND '2001-12-01
 17:00:00' ORDER BY "computername/my_process/pot1@value" DESC
- Select the computername\my_process\pot1.value shared variable data
 over a specified time and search the minimum and maximum value
  - SELECT MIN("computername/my_process/pot1@value"),
 MAX("computername/my_process/pot1@value") FROM RawData WHERE LocalTime
 BETWEEN '2001-11-29 17:00:00' AND '2001-12-01 17:00:00'

#### Dataset Tables Example
 Queries

The following example queries obtain Citadel data
 from the Dataset tables:

- Select the computername\my_process\pot1.value shared variable data
 over a data set run MyRun_1
  - SELECT LocalTime, UTCTime,
 RunName,"computername/my_process/pot1@value" FROM DS_RawData_My_Dataset
 WHERE RunName = 'MyRun_1'
- Select the computername\my_process\pot1.value shared variable data
 over a data set runs MyRun_1 and MyRun_3
  - SELECT LocalTime, UTCTime, RunName,
 "computername/my_process/pot1@value" FROM DS_RawData_My_Dataset WHERE
 RunName IN ('MyRun_1', 'MyRun_3')
- Select the computername\my_process\pot1.value shared variable data
 over a data set whose names begin with string MyRun_
  - SELECT LocalTime, UTCTime, RunName,
 "computername/my_process/pot1@value" FROM DS_RawData_My_Dataset WHERE
 RunName LIKE 'MyRun_%'
- Query for start time, end time and number of points of the MyRun_3 
 data set run
  - SELECT Min(LocalTime), Max(LocalTime),
 COUNT("computername/my_process/pot1@value") FROM DS_RawData_My_Dataset WHERE
 RunName = 'MyRun_3'

#### Data Transform and Type Cast Command
 Example Queries

The following example queries obtain
 Citadel data using Data Transform and Type Cast commands:

- Select the computername\my_process\pot1.value shared variable data
 over a specified time at one-minute intervals and treats shared variable as
 discrete
  - SELECT LocalTime, TO_DISCRETE("computername/my_process/pot1@value")
 FROM IntData WHERE LocalTime BETWEEN '2001-11-29 17:00:00' AND '2001-11-29
 18:00:00' AND IntInterval = '1:0'
- Select the computername\my_process\pot1.value shared variable data
 over a specified time at one-day intervals and return minimum and maximum day
 values
  - SELECT LocalTime, MATH_MIN("computername/my_process/pot1@value"),
 MATH_MAX("computername/my_process/pot1@value") FROM IntData WHERE LocalTime
 BETWEEN '1999-03-06' AND '1999-03-13' AND IntInterval = '1.0'
- Select the computername\my_process\pot1.value shared variable data
 over a specified time at one-day intervals and return minimum day values and order
 results in descending order
  - SELECT LocalTime, MATH_MIN("computername/my_process/pot1@value") AS
 'min_value' FROM IntData WHERE LocalTime BETWEEN '1999-03-06' AND
 '1999-03-13' AND IntInterval = '1.0' ORDER BY min_value DESC
- Select the computername\my_process\pot1.value shared variable data
 over a specified time at week intervals and return minimum week values. Note that the
 computername\my_process\pot1.value shared variable is treated as
 a Boolean shared variable.
  - SELECT LocalTime,
 MATH_MIN(TO_DISCRETE("computername/my_process/pot1@value")) WHERE LocalTime
 BETWEEN '1999-03-06' AND '1999-03-13' AND IntInterval = 'WEEK'

Parent topic:

Access Citadel Data with SQL

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=stopping-and-starting-the-shared-variable-eng.html language=enus -->
## TOPIC 00112: Stopping and Starting the Shared Variable Engine

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `stopping-and-starting-the-shared-variable-eng.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/stopping-and-starting-the-shared-variable-eng.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: The Shared Variable Engine (SVE) starts automatically when you log into Windows. You also can stop and start the SVE manually.You can log data, alarms, and events for network-published shared variables only.Complete the following steps to stop and start the SVE manually: In the Windows Control Panel

### Stopping and Starting the Shared Variable Engine

Note

Complete the following
 steps to stop and start the SVE manually:

1. In the Windows Control Panel, navigate to the Administrative Tools folder.
2. Double-click the Services shortcut to display the Services utility.
3. Right-click NI Variable Engine in the Name list and select Stop or Start from the shortcut menu to stop or start the SVE, respectively.

Note

You also can stop and start the SVE by using the Distributed System Manager. Select
 Action»Stop Shared Variable Engine or
 Action»Start Shared Variable Engine
 to stop or start the SVE respectively.

Parent topic:

The Shared Variable Engine

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=supervisory-programs.html language=enus -->
## TOPIC 00113: Supervisory Programs

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `supervisory-programs.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/supervisory-programs.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Most DSC Module applications implement some form of supervisory control. One way to write a supervisory control application in the DSC Module is to write a VI that reads from a set of shared variables in a While Loop and performs some action on the data. For example, you can monitor alarms on shared

### Supervisory Programs

Most DSC Module applications implement some form of supervisory control. One way to write
 a supervisory control application in the DSC Module is to write a VI that reads from a
 set of shared variables in a While Loop and performs some action
 on the data.

For example, you can monitor alarms on shared variables and then perform a task when the
 alarm occurs. You also can monitor a set of input shared variables bound to an I/O
 server, reduce the data, and then write the output to another set of shared variables. A
 more complex example of supervisory control is PC-based control of a process or of
 multiple processes.

Maintaining the application can be difficult using this static data access method.
 Instead, you can use DSC Module tools, such as custom I/O servers, and programmatic data
 access methods to build flexible and maintainable supervisory control applications.

Parent topic:

Components of a DSC Module Application

Related concepts:

- Pass Data between LabVIEW and the Shared Variable Engine
- Using Custom VI-Based I/O Servers

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=supported-shared-variable-properties-based-on.html language=enus -->
## TOPIC 00114: Supported Shared Variable Properties Based on Target and Products

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `supported-shared-variable-properties-based-on.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/supported-shared-variable-properties-based-on.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configuring a shared variable depends on the data type of the shared variable and on your target and licensed products.Use the following flowchart to determine which shared variable properties you can edit:

### Supported Shared Variable Properties Based on
 Target and Products

Configuring a shared variable depends on the data type of the shared variable and on your
 target and licensed products.

Use the following flowchart to determine which shared variable properties you can edit:

[IMAGE alt='image' src='GUID-132CC9C2-21FB-452D-B06F-86B328F645C8-a5.gif']

Parent topic:

Shared Variable Properties

Related reference:

- Supported Shared Variable Properties Based on Data Type

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=supported-shared-variable-properties-based.html language=enus -->
## TOPIC 00115: Supported Shared Variable Properties Based on Data Type

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `supported-shared-variable-properties-based.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/supported-shared-variable-properties-based.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configuring a shared variable depends on the data type of the shared variable and on your target and licensed products. The following table describes the shared variable properties that a specific data type supports: Shared Variable PropertiesBooleanStringU32 Bit FieldFixed-Point NumbersVariantFloat

### Supported Shared Variable Properties Based on
 Data Type

Configuring a shared variable depends on the data type of the shared
 variable and on your target and licensed products.

The following table describes the shared variable properties that a
 specific data type supports:

| Shared Variable Properties | Boolean | String | U32 Bit Field | Fixed-Point Numbers | Variant | Floating-Point Numbers | Integer* | Others* |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Alarming:Hi Alarming:HiHi Alarming:Lo Alarming:LoLo |  |  |  |  |  | ✓ | ✓ |  |
| Alarming:Boolean | ✓ |  |  |  |  |  |  |  |
| Alarming:U32 Bit Field |  |  | ✓ |  |  |  |  |  |
| Alarming:Rate Of Change |  |  |  |  |  | ✓ | ✓ |  |
| Alarming:Bad Status Alarming:Event On Data Change Alarming:Event On User Input Only | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ |
| Update Deadband |  |  |  |  |  | ✓ |  |  |
| Initial Value | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ |
| Logging:Time Resolution Logging:Value Resolution Logging:Deadband |  |  |  |  |  | ✓ |  |  |
| Logging:String Format |  | ✓ |  |  | ✓ |  |  | ✓ |
| Logging:Log Data Logging:Log Events | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ |
| Scaling:Coerce Scaling:Raw Zero Scale Scaling:Engineering Full Scale Scaling:Engineering Zero Scale Scaling:Numeric Scaling Type Scaling:Units |  |  |  |  |  | ✓ | ✓ |  |
| Scaling:Invert | ✓ |  |  |  |  |  |  |  |
| Scaling:Invert Mask Scaling:Select Mask |  |  | ✓ |  |  | ✓ |  |  |
| Description | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Network | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Security | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Real-Time FIFO | ✓ | ✓ | ✓ |  |  | ✓ | ✓ | ✓ |

Note

- Integer includes the following data types: Int8,
 UInt8, Int16, UInt16, Int32, UInt32, Int64, and UInt64.
- Others includes the following data types: Array of
 Single, Array of Double, Array of Boolean, Array of Double Waveform, Array
 of Int8, Array of UInt8, Array of Int16, Array of Int16 Waveform, Array of
 UInt16, Array of Int32, Array of UInt32, Array of Int64, Array of UInt64,
 Double Waveform, Int16 Waveform, and Timestamp.

Parent topic:

Shared Variable Properties

Related concepts:

- Supported Shared Variable Types
- Supported Shared Variable Properties Based on Target and Products

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=supported-shared-variable-types.html language=enus -->
## TOPIC 00116: Supported Shared Variable Types

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `supported-shared-variable-types.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/supported-shared-variable-types.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure shared variables depending on the data type. Specify the data type of a shared variable on the Variable page of the Shared Variable Properties dialog box.The LabVIEW Datalogging and Supervisory Control (DSC) Module supports the following data types: Numeric A continuous value repre

### Supported Shared Variable Types

You can configure shared variables depending on the data type. Specify the data type of a
 shared variable on the Variable page of the Shared Variable
 Properties dialog box.

The LabVIEW Datalogging and Supervisory Control (DSC) Module supports the following data
 types:

Numeric

- Single-precision, floating-point numbers
- Double-precision, floating-point numbers
- 8-bit signed and unsigned integers
- 16-bit signed and unsigned integers
- 32-bit signed and unsigned integers
- 64-bit signed and unsigned integers

Boolean

1

TRUE

0

FALSE

U32 Bit Field

String

LabVIEW also includes many additional data types for shared variables, such as arrays, waveforms,
 timestamps, and variants. Some DSC Module features have limited support for the
 additional shared variable data types.

Parent topic:

Shared Variable Properties

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=the-shared-variable-engine.html language=enus -->
## TOPIC 00117: The Shared Variable Engine

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `the-shared-variable-engine.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/the-shared-variable-engine.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Shared Variable Engine (SVE) is a data processing engine that manages the use and connectivity of shared variables.The SVE runs independently from LabVIEW as a separate process. Whereas LabVIEW follows a dataflow model to run VIs, the SVE is event-driven.After you configure shared variables in a

### The Shared Variable Engine

The Shared Variable Engine (SVE) is a data processing engine that manages the use and
 connectivity of shared variables.

The SVE runs independently from LabVIEW as a separate process. Whereas LabVIEW follows a dataflow
 model to run VIs, the SVE is event-driven.

After you configure shared variables in a LabVIEW project, you deploy the shared variables to the
 SVE. When you use shared variables in a VI, you therefore must ensure that the SVE has
 enough CPU time to process shared variable updates and read requests. For example,
 running a VI that writes to or reads from shared variables continuously without a
 Wait (ms) function can cause instability and prevent the SVE from
 updating or returning the most recent value of a shared variable.

- [Pass Data between LabVIEW and the Shared Variable Engine](pass-data-between-labview-and-the-shared-v.html)
- [Shared Variable Engine Error Handling](shared-variable-engine-error-handling.html)
- [Stopping and Starting the Shared Variable Engine](stopping-and-starting-the-shared-variable-eng.html)

Parent topic:

Managing I/O with Shared Variables

Related concepts:

- Configure Shared Variables

Related tasks:

- Deploying a Shared Variable

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=troubleshooting-communication-problems.html language=enus -->
## TOPIC 00118: Troubleshooting Communication Problems

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `troubleshooting-communication-problems.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/troubleshooting-communication-problems.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you are having communication problems across the network, review these guidelines.Make sure each network computer can access the other computers across the network.Because the protocol used for network communication between network Shared Variable Engines is based on TCP/IP, make sure each comput

### Troubleshooting Communication Problems

If you are having communication problems across the network, review these guidelines.

- Make sure each network computer can access the other computers across the network.
- Because the protocol used for network communication between network Shared Variable Engines is
 based on TCP/IP, make sure each computer has TCP/IP configured correctly on it.
- Each computer must have a unique IP address and a host name assigned to it. You can use TCP/IP utilities such as ping (all operating systems) and nslookup (Windows XP only) to verify the address and the host name.

Note

ping /?

ping

nslookup

Enter

?

nslookup

- If the network contains a firewall that separates network computers, you must make some
 adjustments. Refer to the Developer Zone at ni.com/zone for more
 information about networking across firewalls.
- Use the Distributed System Manager to monitor communication and determine whether data is
 accessible through the NI Publish-Subscribe Protocol (NI-PSP) or
 Logos .

For more information, read the following:

- [Troubleshooting Modbus I/O Servers](troubleshooting-modbus-i-o-servers.html)
- [Troubleshooting OPC Client I/O Servers](troubleshooting-opc-client-i-o-servers.html)

Parent topic:

Network and Deploy Applications

Related concepts:

- Pass Data between LabVIEW and the Shared Variable Engine

Related tasks:

- Monitoring Shared Variable Values

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=troubleshooting-modbus-i-o-servers.html language=enus -->
## TOPIC 00119: Troubleshooting Modbus I/O Servers

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `troubleshooting-modbus-i-o-servers.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/troubleshooting-modbus-i-o-servers.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You might face the following issues while using Modbus I/O servers. Follow these guidelines to troubleshoot Modbus I/O servers.Modbus generates the following error after you deploy a Modbus Master I/O server. Modbus failure: LabVIEW DSC error code: -1967353900. The Modbus I/O server failed to alloca

### Troubleshooting Modbus I/O Servers

You might face the following issues while using Modbus I/O servers. Follow these
 guidelines to troubleshoot Modbus I/O servers.

- Modbus generates the following error after you deploy a Modbus Master I/O server. Modbus
 failure: LabVIEW DSC error code: -1967353900. The Modbus I/O server failed to
 allocate a serial port.
  - Check the serial port you configured for the I/O server. Ensure that no
 other program occupies the serial port.
  - The Shared Variable Engine (SVE) registers available serial ports only when
 the SVE is initializing. Ensure that no process or application occupies any
 serial ports when the SVE is initializing. The SVE does not register
 occupied serial ports. If you install new serial ports using the ENET232,
 USB, or Virtual Ports when the SVE is running, restart the computer or the
 SVE to register the new serial ports.
- Modbus generates the following error after you deploy a Modbus Slave I/O server. Modbus failure:
 LabVIEW DSC error code: -1967353912. The Modbus Slave I/O server failed to bind to
 port 502.
  - Check whether you deployed duplicate Modbus Slave (Ethernet) I/O servers.
 Modbus Slave (Ethernet) I/O servers listen on port 502 to communicate with
 Modbus Master I/O servers. Duplicate Modbus Slave (Ethernet) I/O servers
 cause errors when these I/O servers listen on port 502.
- Modbus cannot read/write array types.
  - Ensure that the length of the array does not exceed the maximum length of arrays that you
 specified. You can specify the maximum length of arrays in the
 Maximum Data Points Per Command section of the
 Advanced Attribute Settings dialog box.
- Modbus generates errors when the Modbus Master I/O server communicates with Modbus Slave I/O
 servers.
  - Assign a unique address to each Modbus Slave (Serial) I/O server. If
 multiple Modbus Slave (Serial) I/O servers have the same addresses, the
 Modbus Master I/O server communicates with only the first Modbus Slave I/O
 server that the SVE deploys.
- Modbus does not work at low baud rates.
  - Increase the Timeout delay value in the Configure Modbus I/O
 Server dialog box. For example, to use the modbus I/O server
 at baud rate 2400, set Timeout delay to 500
 ms or greater.

Parent topic:

Troubleshooting Communication Problems

Related concepts:

- Use Modbus I/O Servers
- Pass Data between LabVIEW and the Shared Variable Engine
- Modbus Communication in LabVIEW

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=troubleshooting-opc-client-i-o-servers.html language=enus -->
## TOPIC 00120: Troubleshooting OPC Client I/O Servers

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `troubleshooting-opc-client-i-o-servers.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/troubleshooting-opc-client-i-o-servers.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to troubleshoot OPC I/O servers. Configure the DCOM security settings on both the client and server. The OPC Client I/O servers connect to both local and remote OPC servers through DCOM. Refer to the Using OPC via DCOM with Microsoft Windows XP Service Pack 2 manual on t

### Troubleshooting OPC Client I/O Servers

Complete the following steps to troubleshoot OPC I/O
 servers.

1. Configure the DCOM security settings on both the client and server. The OPC
 Client I/O servers connect to both local and remote OPC servers through DCOM.
 Refer to the *Using OPC via DCOM with Microsoft Windows XP Service Pack
 2* manual on the OPC Foundation web site at www.opcfoundation.org for
 information about configuring DCOM security settings.
2. Configure the security settings on both the client and server.
  1. In the Windows Control Panel, navigate to the
 Administrative Tools folder.
  2. Double-click the Local Security Policy shortcut
 to launch the Local Security Settings utility.
  3. In the Security Settings tree, select
 Local Policies»Security Options. Ensure the
 value of Network access: Sharing and security model for local
 accounts policy is Classic - local users
 authenticate as themselves.
3. Configure the service username for the Shared Variable Engine (SVE). OPC Client
 I/O servers connect to OPC servers by using the SVE. The username of SVE is
 SYSTEM by default. Note If you use the
 default SVE username, you must configure local OPC servers to work with OPC
 Client I/O servers. Otherwise, you must ensure the username of SVE is an
 administrator.
  1. In the Windows Control Panel, navigate to the
 Administrative Tools folder.
  2. Double-click the Services shortcut to launch the
 Services utility.
  3. In the Services window, right-click the
 Variable Engine service and select
 Properties from the short menu. The
 Variable Engine Properties dialog box
 displays.
  4. Click the Log On tab to display the
 Log On page.
  5. Select the This account option.
  6. Enter an administrator username and password in the text boxes.
  7. Click the OK button to close this dialog
 box.
  8. Restart the SVE to apply the configurations.

Parent topic:

Troubleshooting Communication Problems

Related concepts:

- Use OPC Client I/O Servers
- Pass Data between LabVIEW and the Shared Variable Engine

Related tasks:

- Configuring Local OPC Servers to Work with OPC Client I/O Servers
- Stopping and Starting the Shared Variable Engine

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=use-alarms-and-events-in-dsc-module-applica.html language=enus -->
## TOPIC 00121: Use Alarms and Events in DSC Module Applications

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `use-alarms-and-events-in-dsc-module-applica.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/use-alarms-and-events-in-dsc-module-applica.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section describes how to configure, log, and respond to alarms and events with the LabVIEW Datalogging and Supervisory Control (DSC) Module applications.An event is an instantaneous occurrence that happens to an individual element of an application or to the DSC Module environment. Examples of

### Use Alarms and Events in DSC Module
 Applications

This section describes how to configure, log, and respond to alarms and events with the
 LabVIEW Datalogging and Supervisory Control (DSC) Module applications.

An event is an instantaneous occurrence that happens to an individual element of an application
 or to the DSC Module environment. Examples of events include changes in shared variable
 alarm states, changes in a front panel control, user log ins, and changes in historical
 logging. Events can be divided into two groups: shared variable events that occur to
 individual shared variables and system events that occur in the overall DSC Module
 application. An example of a shared variable event is a change of alarm state for a
 shared variable. Examples of system events include a user logging on to the system or a
 user enabling historical logging for the system.

An alarm represents a specific, abnormal condition associated with shared variable or with a
 user-defined state. You can set and configure alarms for shared variables. Examples of
 alarms include bad status or high/low values for a shared variable. Alarms have two
 types of status: TRUE or FALSE, and acknowledged or
 unacknowledged. Any time an alarm transitions from FALSE to
 TRUE is an alarm instance. Besides these two status values, every
 alarm instance contains data such as timestamps, user names, setpoint, shared variable
 value, priority, alarm area, description, and acknowledgement comments.

An alarm is a specific kind of event associated with a shared variable or with a user-defined
 state. An event can be virtually any instantaneous activity such as a mouse click. An
 alarm typically has the following characteristics:

- Denotes an abnormal condition
- Occurs under certain, specific conditions
- Must be acknowledged by the user or configured for automatic acknowledgment

Note

Refer to the DSC Alarms Demo.lvproj in the
 labview\examples\lvdsc\Data and Alarm Historical Logging\DSC Alarms
 Demo directory for an example of using alarms.

- [Configure Alarms and Events](configure-alarms-and-events.html)
- [View System Errors and Events](view-system-errors-and-events.html)
- [Archiving and Extracting Alarm and Event Data](archiving-and-extracting-alarm-and-event-data.html)
- [Print Alarm and Event Data](print-alarm-and-event-data.html)
- [Viewing and Retrieving Alarm and Event Data](viewing-and-retrieving-alarm-and-event-data.html)
- [Acknowledging Alarms](acknowledge-alarms.html)
- [Configuring Alarms](configuring-alarms_2.html)
- [Configuring Alarms for Boolean Shared Variables](configuring-alarms-for-boolean-shared-variabl.html)
- [Configuring Alarms for Numeric Shared Variables](configuring-alarms-for-numeric-shared-variabl.html)
- [Configuring Alarms for String Shared Variables](configuring-alarms-for-string-shared-variable.html)
- [Configuring Alarms for U32 Bit Field Shared Variables](configuring-alarms-for-u32-bit-field-shared-v.html)
- [Filtering Alarms and Events in the Alarm and Event Display Control](filtering-alarms-and-events-in-the-alarm-and.html)
- [Printing Alarms and Events](printing-alarms-and-events.html)
- [Viewing Alarms and Events Using the Alarm and Event Display Control](viewing-alarms-and-events-using-the-alarm-and.html)

Parent topic:

LabVIEW Datalogging and Supervisory Control Module Features

Related concepts:

- Set Alarms for Shared Variables
- Enable Data and Event Logging with Shared Variables

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=use-custom-vi-based-i-o-servers.html language=enus -->
## TOPIC 00122: Using Custom VI-Based I/O Servers

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `use-custom-vi-based-i-o-servers.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/use-custom-vi-based-i-o-servers.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use a custom I/O server to simulate hardware or connect the DSC Module to hardware for which no device server exists.When you have a uniquely configured or custom device that you want to use with the LabVIEW Datalogging and Supervisory Control (DSC) Module you create custom I/O servers with LabVIEW,

### Using Custom VI-Based I/O Servers

Use a custom I/O server to simulate hardware or connect the DSC Module to hardware for
 which no device server exists.

When you have a uniquely configured or custom device that you want to use with the LabVIEW
 Datalogging and Supervisory Control (DSC) Module you create custom I/O servers with
 LabVIEW, unlike OPC servers, which are typically written in Microsoft Visual Basic or
 C++. A custom I/O server publishes selected data items as Publish-Subscribe Protocol
 data items on the network. The custom I/O server shares ownership of the data with the
 Shared Variable Engine (SVE), which publishes the data.

For example, you might want to create a custom I/O server in the following situations:

- You do not have an OPC server to handle communication between hardware and LabVIEW. Custom VI-based I/O servers can interface directly with the hardware and expose data items through the SVE.
- You want to create a simulation server to emulate hardware connections.

You can create two types of custom I/O servers: on input change I/O servers and periodic I/O
 servers. Create an on input change I/O server if you want the custom I/O server to
 update based on an event, such as a change in the value of the input of the server data
 item. Create a periodic I/O server when you want to control the update rate of a data
 item and when you want a continuous update of the data item.

The DSC Module provides two wizards to help you create custom I/O servers:

Custom VI-based Server – On Input Change Wizard

Custom VI-based Server – Periodic Wizard

To create a custom I/O server, right-click My Computer or a LabVIEW
 project library in the Project Explorer window and select
 New»I/O Server from the shortcut menu. In the
 Create New I/O Server dialog box, you can select
 Custom VI - On Input Change or Custom VI -
 Periodic.

- [Use On Input Change I/O Servers](use-on-input-change-i-o-servers.html)
- [Use Periodic I/O Servers](use-periodic-i-o-servers.html)

Parent topic:

Interact with Data Using I/O Servers

Related concepts:

- Pass Data between LabVIEW and the Shared Variable Engine
- Creating On Input Change I/O Servers
- Creating Periodic I/O Servers

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=use-epics-server-i-o-servers-dsc-module-or.html language=enus -->
## TOPIC 00123: Use EPICS Server I/O Servers

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `use-epics-server-i-o-servers-dsc-module-or.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/use-epics-server-i-o-servers-dsc-module-or.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: With EPICS Server I/O servers, LabVIEW acts as a server that uses the Channel Access (CA) network protocol.Use EPICS Server I/O servers to publish shared variables by using the CA network protocol. An EPICS Server I/O server is a Channel Access Server (CAS). You can create an EPICS Server I/O server

### Use EPICS Server I/O Servers

With EPICS Server I/O servers, LabVIEW acts as a server that uses the Channel Access (CA)
 network protocol.

Note

- [Publish Shared Variables to an EPICS Network](publish-shared-variables-to-epics.html)
- [Access PVs](access-pv.html)
- [Distribute EPICS Server I/O Servers](distribute-epics-server-io-servers.html)

Parent topic:

Use EPICS I/O Servers

Related concepts:

- Create EPICS Server I/O Servers (DSC Module or Real-Time Module)

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=use-modbus-i-o-servers-dsc-module-or-real-t.html language=enus -->
## TOPIC 00124: Use Modbus I/O Servers

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `use-modbus-i-o-servers-dsc-module-or-real-t.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/use-modbus-i-o-servers-dsc-module-or-real-t.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Modbus is an application-level messaging protocol that provides client-server communication between devices connected on different types of buses or networks. You can create a Modbus or Modbus Slave I/O server to read data from or write data to Modbus devices.For example, you can create a Modbus Sla

### Use Modbus I/O Servers

Modbus is an application-level messaging protocol that provides client-server
 communication between devices connected on different types of buses or networks. You can
 create a Modbus or Modbus Slave I/O server to read data from or write data to Modbus
 devices.

For example, you can create a Modbus Slave I/O server on a real-time controller and use this
 controller as a Modbus slave device. You also can create a Modbus I/O server on a host
 computer and use this server as a Modbus master device to communicate with a Modbus
 slave device.

Note

Use the View I/O Items dialog box to view the data items to which the I/O server can read or
 write. You also can monitor these data items by using the Distributed System
 Manager. To launch the System Manager from LabVIEW, select
 Tools»Distributed System Manager.

Modbus I/O servers use six-digit addresses. You can convert a five-digit address to a six-digit
 address by adding a zero between the first and the second digits of the five-digit
 address. For example, you can convert address 45001 to
 405001.

Modbus and Modbus Slave I/O server data items use the following denotations:

A

D

F

L

Maximum Data Points Per
 Command

Advanced
 Attribute Settings

Maximum Data Points Per Command

S

SD

Example

Data Item

{I/O point
 address}

Note

| Data Item | Data Type | Modbus Read | Modbus Write | Modbus Slave Read | Modbus Slave Write | Description | Example |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 000001–065535 | Boolean value | Yes | Yes | Yes | Yes | Accesses single-bit coils. | 000001 = {000001} |
| 100001–165535 | Boolean value | Yes | No | Yes | Yes | Accesses single-bit discrete inputs. | 100002 = {100002} |
| 300001.1–365535.16 | Boolean value | Yes | No | Yes | Yes | Accesses individual bits of input registers and interprets them as logical TRUE or FALSE values. The least significant bit is 1. The most significant bit is 16. | 300001.1 = {the first bit of 300001} |
| 300001–365535 | 16-bit unsigned integer | Yes | No | Yes | Yes | Accesses 16-bit input registers as unsigned integers ranging from 0 to 65,535. | 300001 = {300001} |
| 400001.1–465535.16 | Boolean value | Yes | No | Yes | Yes | Accesses individual bits of holding registers and interprets them as logical TRUE or FALSE values. The least significant bit is 1. The most significant bit is 16. | 400002.16 = {the 16th bit of 400002} |
| 400001–465535 | 16-bit unsigned integer | Yes | Yes | Yes | Yes | Accesses 16-bit holding registers as unsigned integers ranging from 0 to 65,535. | 400002 = {400002} |
| A000001L1–A065535L1 | Array of Boolean values | Yes | Yes | Yes | Yes | Accesses arrays of single-bit coils. | A000001L2 = {000001, 000002} |
| A100001L1–A165535L1 | Array of Boolean values | Yes | No | Yes | Yes | Accesses arrays of single-bit discrete inputs. | A100005L3 = {100005–100007} |
| A300001L1–A365535L1 | Array of 16-bit unsigned integers | Yes | No | Yes | Yes | Accesses arrays of 16-bit input registers as arrays of unsigned integers. | A300001L2 = {300001, 300002} |
| A400001L1–A465535L1 | Array of 16-bit unsigned integers | Yes | Yes | Yes | Yes | Accesses arrays of 16-bit holding registers as arrays of unsigned integers. | A400005L3 = {400005–400007} |
| AD300001L1–AD365534L1 | Array of 32-bit unsigned integers | Yes | No | Yes | Yes | Accesses arrays of 32-bit unsigned integers. Each 32-bit unsigned integer in the array is composed of two adjacent 16-bit input registers. | AD300001L1 ={300001, 300002} |
| AD400001L1–AD465534L1 | Array of 32-bit unsigned integers | Yes | Yes | Yes | Yes | Accesses arrays of 32-bit unsigned integers. Each 32-bit unsigned integer in the array is composed of two adjacent 16-bit holding registers. | AD400002L3 = {400002–400007} |
| AF300001L1–AF365534L1 | Array of 32-bit floating-point numbers | Yes | No | Yes | Yes | Accesses arrays of 32-bit floating-point numbers. Each 32-bit floating-point number in the array is composed of two adjacent 16-bit input registers. | AF300001L2 = {300001–300004} |
| AF400001L1–AF465534L1 | Array of 32-bit floating-point numbers | Yes | Yes | Yes | Yes | Accesses arrays of 32-bit floating-point numbers. Each 32-bit floating-point number in the array is composed of two adjacent 16-bit holding registers. | AF400002L3 = {400002–400007} |
| AS300001L1–AS365535L1 | Array of 16-bit signed integers | Yes | No | Yes | Yes | Accesses arrays of 16-bit input registers as arrays of signed integers. | AS300001L1 = {300001} |
| AS400001L1–AS465535L1 | Array of 16-bit signed integers | Yes | Yes | Yes | Yes | Accesses arrays of 16-bit holding registers as arrays of signed integers. | AS400002L3 = {400002–400004} |
| ASD300001L1–ASD365534L1 | Array of 32-bit signed integers | Yes | No | Yes | Yes | Accesses arrays of 32-bit signed integers. Each 32-bit signed integer in the array is composed of two adjacent 16-bit input registers. | ASD300001L1 = {300001, 300002} |
| ASD400001L1–ASD465534L1 | Array of 32-bit signed integers | Yes | Yes | Yes | Yes | Accesses arrays of 32-bit signed integers. Each 32-bit signed integer in the array is composed of two adjacent 16-bit holding registers. | ASD400002L3 = {400002–400007} |
| CommFail | Boolean value | Yes | No | Yes | No | Represents a signal the Modbus I/O server generates. The signal is TRUE in the following cases: Errors occur when the Shared Variable Engine fails to communicate with a Modbus device. Errors occur on the serial ports or Ethernet interface of a Modbus Slave I/O server. | N/A |
| D300001–D365534 | 32-bit unsigned integer | Yes | No | Yes | Yes | Accesses two adjacent 16-bit input registers as one 32-bit unsigned integer ranging from 0 to 4,294,967,295. | D300001 = {300001, 300002} |
| D400001–D465534 | 32-bit unsigned integer | Yes | Yes | Yes | Yes | Accesses two adjacent 16-bit holding registers as one 32-bit unsigned integer ranging from 0 to 4,294,967,295. | D400002 = {400002, 400003} |
| ErrorStatus | 32-bit signed integer | N/A | N/A | Yes | No | Represents the error status of the Modbus Slave I/O server. If CommFail is FALSE, this data item is 0. If CommFail is TRUE, this data item returns an error code. | N/A |
| F300001–F365534 | 32-bit floating-point number | Yes | No | Yes | Yes | Accesses two adjacent 16-bit input registers as one 32-bit floating-point number. | F300001 = {300001, 300002} |
| F400001–F465534 | 32-bit floating-point number | Yes | Yes | Yes | Yes | Accesses two adjacent 16-bit holding registers as one 32-bit floating-point number. | F400002 = {400002, 400003} |
| OffHook | Boolean value | Yes | Yes | N/A | N/A | Specifies that a Modbus object retain exclusive use of a communication port when the value of OffHook is TRUE. If the value is FALSE, the Modbus object does not retain exclusive use of the communication port. Modbus Slave I/O servers do not support this data item. | N/A |
| S300001–S365535 | 16-bit signed integer | Yes | No | Yes | Yes | Accesses 16-bit input registers as signed integers ranging from –32,768 to 32,767. | S300001 = {300001} |
| S400001–S465535 | 16-bit signed integer | Yes | Yes | Yes | Yes | Accesses 16-bit holding registers as signed integers ranging from –32,768 to 32,767. | S400002 = {400002} |
| SD300001–SD365534 | 32-bit signed integer | Yes | No | Yes | Yes | Accesses two adjacent 16-bit input registers as one 32-bit signed integer ranging from –2,147,483,648 to 2,147,483,647. | SD300001 = {300001, 300002} |
| SD400001–SD465534 | 32-bit signed integer | Yes | Yes | Yes | Yes | Accesses two adjacent 16-bit holding registers as one 32-bit signed integer ranging from –2,147,483,648 to 2,147,483,647. | SD400002 = {400002, 400003} |
| UpdateNow | Boolean value | No | Yes | N/A | N/A | Specifies that the Modbus I/O server refresh the Modbus device once if the value of UpdateNow changes from FALSE to TRUE. Modbus Slave I/O servers do not support this data item. | N/A |
| UpdateRate | 64-bit floating-point number | Yes | Yes | N/A | N/A | Specifies how often the Modbus I/O server refreshes a Modbus device, in seconds. You can specify a non-integer value for this data item. If the value of this data item is zero, the Modbus I/O server does not refresh the device. Modbus Slave I/O servers do not support this data item. | N/A |
| Updating | Boolean value | Yes | No | Yes | No | Represents a signal the Modbus or Modbus Slave I/O server generates. The signal is TRUE while the Modbus I/O server polls a Modbus device or the Modbus Slave I/O server is being updated. | N/A |

Parent topic:

Interact with Data Using I/O Servers

Related concepts:

- Creating Modbus I/O Servers (DSC Module or Real-Time Module)
- Modbus Communication in LabVIEW

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=use-on-input-change-i-o-servers.html language=enus -->
## TOPIC 00125: Use On Input Change I/O Servers

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `use-on-input-change-i-o-servers.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/use-on-input-change-i-o-servers.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Custom VI-based Server – On Input Change Wizard converts a VI into a custom I/O server that performs calculations for an application and publishes the calculated results as NI Publish-Subscribe Protocol (NI-PSP) data items to the network.The Shared Variable Engine (SVE) launches the on input cha

### Use On Input Change I/O Servers

The Custom VI-based Server – On Input Change Wizard converts a VI
 into a custom I/O server that performs calculations for an application and publishes the
 calculated results as NI Publish-Subscribe Protocol (NI-PSP) data items to the
 network.

The Shared Variable Engine (SVE) launches the on input change I/O server when you load a LabVIEW
 process that includes an on input change I/O server. When any input changes or when a
 trigger condition occurs, the on input change I/O server recalculates published data
 items. This I/O server remains loaded until the process stops. On input change I/O
 servers do not have shutdown or timeout settings.

#### Creating an On Input Change I/O
 Server

To create an on input change I/O server, first create a
 Calculation VI that reads values, performs calculations, and
 returns a result. Then use the Custom VI-based Server – On Input Change
 Wizard to convert the VI to an on input change I/O server and
 configure the on input change I/O server in a process.

#### Guidelines for Creating a Calculation
 VI

Use the following guidelines when you create the
 Calculation VI:

- Make sure the VI is reentrant so that each instance of the server has its own
 data space. Otherwise, the server does not work.
- Make sure that the VI executes in the shortest time possible. The SVE waits
 until the VI finishes executing before updating the data items.
- Make sure all While Loops terminate without user
 intervention. While Loops must terminate so the SVE can stop
 the VI.
- Use double-precision, string, and Boolean data types when you create a VI to
 convert into a custom I/O server. These data types are the most efficient to use
 when publishing data items. LabVIEW converts other data types to variants, which
 can slow down the performance of the server.

The Custom VI-based Server – On Input Change Wizard
 checks these items, except for execution speed, when you attempt to convert a
 Calculation VI to an on input change I/O
 server.

#### Converting the Calculation
 VI

To convert the Calculation VI into an on input
 change I/O server, right-click My Computer or a LabVIEW
 project library in the Project Explorer window and select
 New»I/O Server from the shortcut menu. In the
 Create New I/O Server dialog box, select
 Custom VI - On Input Change and click the
 Continue button to create and configure the on input
 change I/O server. The Custom VI-based Server – On Input Change
 Wizard creates the following files:

- A registration VI saved as National Instruments\Shared\DSC\Custom VI
 Input Change Server\version
 number\vior_filename.vi
- VIs in the National Instruments\Shared\DSC\Custom VI Input Change
 Server\version numberfilename folder

#### Testing an On Input Change I/O
 Server

Use the Distributed System Manager to ensure that the on input
 change I/O server publishes values as expected.

Note

Parent topic:

Using Custom VI-Based I/O Servers

Related concepts:

- Pass Data between LabVIEW and the Shared Variable Engine
- Creating On Input Change I/O Servers

Related tasks:

- Monitoring Shared Variable Values
- Building a DSC Module Application
- Distributing a Built Application

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=use-opc-client-i-o-servers.html language=enus -->
## TOPIC 00126: Use OPC Client I/O Servers

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `use-opc-client-i-o-servers.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/use-opc-client-i-o-servers.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Datalogging and Supervisory Control (DSC) Module provides OPC Client I/O servers for communicating with any server implementing the OPC Foundation OPC server interface, which is a Microsoft COM-based standard.An OPC Client I/O server lists all OPC servers installed on the computer and re

### Use OPC Client I/O Servers

The LabVIEW Datalogging and Supervisory Control (DSC) Module provides OPC Client I/O
 servers for communicating with any server implementing the OPC Foundation OPC server
 interface, which is a Microsoft COM-based standard.

An OPC Client I/O server lists all OPC servers installed on the computer and reads any available
 information about the server capabilities and items directly from the server. You can
 create an OPC Client I/O server to access data items on a local or remote OPC server.
 You also can configure a local OPC server to work with an OPC Client I/O server.

x

x

Launcher

x

x

Note

OPC Servers Help

Help»Server Help

#### Configuring Local OPC Servers to Work
 with OPC Client I/O Servers

You must verify the DCOM configuration for a
 local OPC server before you connect an OPC Client I/O server to the OPC server. The
 manufacturer recommends that you configure the OPC server to run with an identity of
 The interactive user.

#### Accessing Remote OPC Servers through
 OPC Client I/O Servers

You can use an OPC Client I/O server to access OPC servers running on other computers
 on the network. An OPC Client I/O server enables you to access different instances
 of the same remote OPC server.

#### Logging OPC Diagnostic
 Information

Logging diagnostic information about OPC Client I/O servers
 can help you debug an OPC system. You can use the options on the
 Diagnostics page of the Configure OPC Client
 I/O Server dialog box to log diagnostic information about the OPC
 Client I/O servers you create.

OPC Client I/O servers communicate with both
 LabVIEW and the Shared Variable Engine (SVE) and log this communication to
 HTML log files. The HTML file you
 specify in the Log file option logs the communication between
 the SVE and the OPC Client I/O server you create. OPC Client I/O servers generate
 separate log files to log the communication between LabVIEW and the OPC Client I/O
 servers. For example, if you specify a log file named
 logfile.html, the OPC Client I/O server automatically
 generates a logfile_LV.html file to log the communication
 between LabVIEW and the OPC Client I/O server. The log files highlight communication
 activities in blue and communication errors in red. The log files also provide
 explanations of the communication errors. You can use the log files to debug an OPC
 system.

Parent topic:

Interact with Data Using I/O Servers

Related concepts:

- Creating OPC Client I/O Servers
- Bind Shared Variables to OPC Server Data Items

Related tasks:

- Configuring Local OPC Servers to Work with OPC Client I/O Servers

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=use-periodic-i-o-servers.html language=enus -->
## TOPIC 00127: Use Periodic I/O Servers

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `use-periodic-i-o-servers.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/use-periodic-i-o-servers.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Custom VI-based Server – Periodic Wizard to create a periodic I/O server.The Custom VI-based Server – Periodic Wizard converts a VI into a custom I/O server that runs as a service and publishes NI Publish-Subscribe Protocol (NI-PSP) data items to the network. LabVIEW automatically launches,

### Use Periodic I/O Servers

Use the Custom VI-based Server – Periodic Wizard to create a
 periodic I/O server.

The Custom VI-based Server – Periodic Wizard converts a VI into a custom
 I/O server that runs as a service and publishes NI Publish-Subscribe Protocol (NI-PSP)
 data items to the network. LabVIEW automatically launches, registers, initializes,
 performs error handling, and shuts down the periodic I/O server when necessary.

The Shared Variable Engine (SVE) launches the periodic I/O server when you load a LabVIEW process
 that includes a periodic I/O server. The periodic I/O server executes until the
 specified stop condition occurs. If the stop condition occurs and the periodic I/O
 server does not shut down by the specified timeout value, the VI aborts and generates an
 event of priority 500.

#### Creating a Periodic Custom I/O Server
 in LabVIEW

Before you create a periodic I/O server in LabVIEW, first
 create a data access VI that retrieves or emulates hardware data values in a loop
 structure. You then can use the Custom VI-based Server – Periodic
 Wizard to convert the VI to a periodic I/O server and configure the
 periodic I/O server in a process.

Use the following guidelines when you create the data access VI:

- Make sure the VI does not contain any Event Structures or user interface
 interaction.
- Make sure all While Loops terminate without user intervention. While
 Loops must terminate so the SVE can stop the VI.
- Make sure all loops are timed in the same way.
- Make sure controls and indicators that you want to publish from the top-level VI
 do not contain local variables, Property Nodes, or control references. The
 server synchronizes control and indicator values with NI-PSP data items only
 when a value is read or written at the control terminal. Modifying the value
 using a local variable, Property Node, or control reference can cause the data
 to be out of sync with NI-PSP data items.
- If you select a While Loop in the top-level VI as the way to stop the server,
 configure the While Loop as either Stop if True or
 Continue if True . Do not use Stop on
 Error or Continue while Error .
- Use double-precision, string, and Boolean data types when you create a VI to
 convert into a custom I/O server. These data types are the most efficient to use
 when publishing data items. LabVIEW converts other data types to variants, which
 can slow down the performance of the server.

Custom VI-based Server – Periodic Wizard checks these items when you
 attempt to convert a data access VI to a periodic I/O server.

#### Converting the Data Access
 VI

To convert the data access VI into a periodic I/O server, right-click
 My Computer or a LabVIEW project library in the
 Project Explorer window and select New»I/O
 Server from the shortcut menu. In the Create New I/O
 Server dialog box, select Custom VI -
 Periodic and click the Continue button to
 create and configure the periodic I/O server. The Custom VI-based Server
 – Periodic Wizard creates the following files:

- A VI template saved as National Instruments\Shared\DSC\Custom VI
 Periodic Server\version
 number\templates\vislt_filename.vit
- A registration VI saved as National Instruments\Shared\DSC\Custom VI
 Periodic Server\version
 number\registration\vislr_filename.vi
- DLLs and VIs in the National Instruments\Shared\DSC\Custom VI Periodic
 Server\version
 number\templates\filename 
 folder

#### Testing a Periodic I/O
 Server

Use the Distributed System Manager to ensure that the periodic I/O
 server publishes values as expected.

Note

Parent topic:

Using Custom VI-Based I/O Servers

Related concepts:

- Pass Data between LabVIEW and the Shared Variable Engine
- Creating Periodic I/O Servers

Related tasks:

- Monitoring Shared Variable Values
- Building a DSC Module Application
- Distributing a Built Application

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=user-manual-welcome.html language=enus -->
## TOPIC 00128: LabVIEW Datalogging and Supervisory Control Module User Manual

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/user-manual-welcome.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Datalogging and Supervisory Control Module User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, b

### LabVIEW Datalogging and Supervisory Control
 Module
 User Manual

The LabVIEW Datalogging and Supervisory Control
 Module User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Hardware and Software Operating System Compatibility
- License Setup and Activation

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=using-data-set-marking-i-o-servers.html language=enus -->
## TOPIC 00129: Use Data Set Marking I/O Servers

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `using-data-set-marking-i-o-servers.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/using-data-set-marking-i-o-servers.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can create data set I/O servers with the LabVIEW Datalogging and Supervisory Control (DSC) Module to read and write groups of shared variables logged together as a set during a specific period of time, or data sets.Right-click My Computer or a LabVIEW project library in the Project Explorer wind

### Use Data Set Marking I/O Servers

You can create data set I/O servers with the LabVIEW Datalogging and Supervisory Control
 (DSC) Module to read and write groups of shared variables logged together as a set
 during a specific period of time, or data sets.

My Computer

Project Explorer

New»I/O
 Server

Create New I/O
 Server

Data Set
 Marking

Continue

Configure Data Set Marking I/O Server

Configure Data Set Marking I/O Server

Note

You can use data set marking I/O servers to log statistical data, such as the batch process that
 is running, the current ID of the batch process, and so on.

The following table lists the data items that LabVIEW creates when you create and configure a
 data set marking I/O server. Use the View I/O Items dialog box to
 view the data items. You also can monitor these data items by using the Distributed
 System Manager. To launch the System Manager from LabVIEW, select
 Tools»Distributed System Manager.

| Data Item | Data Type | Read | Write | Description |
| --- | --- | --- | --- | --- |
| active | Boolean | Yes | No | Returns whether a start or end condition for a data set run is met. The value is TRUE after the start condition is met and until the end condition is met. |
| alarm_area | String | Yes | Yes | Specifies the alarm area of this data set instance. The server generates an alarm if the configuration is bad. |
| alarm_priority | Double | Yes | Yes | Specifies the alarm priority of this data set instance. The server generates an alarm with this priority if the configuration is bad. |
| configure_start_end_condition | Boolean | Yes | Yes | Specifies whether the start and end conditions are configured. If the value is TRUE, the data set waits for new configuration to be written before starting. |
| current_start_run_time | Double | Yes | No | Displays the current data set run start time if a run is active. The units are in UTC seconds. |
| currentid | String | Yes | No | Reports the ID tag value for the current data set run, while the data set run is active. |
| dataset_server_state | String | Yes | No | Displays the current state of the data set server. For example, if active=TRUE, dataset_server_state=Wait for stop. If active=FALSE, dataset_server_state=Wait for start. Possible states are Verify Configuration, Wait for start, Wait for stop, Post End of Run, and Wait for config transition. |
| desc | String | Yes | Yes | Specifies the description of the data set. If you write to this data item, the description updates at the start of the next data set run. |
| end_condition | Double | Yes | Yes | Specifies the type of end condition to use for the next data set run. Depending on the end condition, you may need to update other items. |
| end_limit_numeric | Double | Yes | Yes | If end_condition uses numeric comparisons, this data item compares with the value of end_tag to determine whether the end condition has been met. |
| end_tag | String | Yes | Yes | Specifies the tag to use for testing the end condition. The data type must be compatible with the data type of the end condition. |
| end_value_string | String | Yes | Yes | If end_condition is set to String SV=Value, this data item compares with the value of end_tag to determine whether the end condition has been met. The comparison is case sensitive. |
| equip | String | Yes | Yes | Lists the equipment for the current data run. You can write a tab-delimited spreadsheet-style string, rows by EOL (end-of-line) characters, or a flattened 2-dimensional array of LabVIEW strings to this data item. Changes take effect when the next run starts. |
| idtag | String | Yes | Yes | Specifies this tag as the ID tag when the next data set run starts. |
| internal_id | Binary string | Yes | No | Returns an internally generated, 8-byte binary identifier that is unique for each data set. This data item identifies each data set run. |
| name | String | Yes | No | Specifies the name of the data set configuration. |
| previous_run_duration | Double | Yes | No | Displays the last run duration. The units are in UTC seconds. |
| previous_run_end_time | Double | Yes | No | Displays the last run end time. The units are in UTC seconds. |
| previous_run_id | String | Yes | No | Reports the ID tag value for the previous data set run, while the data set run is active. |
| start_condition | Double | Yes | Yes | Specifies the type of start condition to use at the beginning of the next data set run. Depending on the start condition, you may need to update other items. |
| start_limit_numeric | Double | Yes | Yes | If start_condition uses numeric comparisons, this data item compares with the value of start_tag to determine whether the start condition has been met. |
| start_tag | String | Yes | Yes | Specifies the name of the tag for testing the start condition. The data type must be compatible with the data type of the start condition. |
| start_value_string | String | Yes | Yes | If the start_condition is set as String SV=Value, this data item compares with the value of start_tag to determine whether the start condition has been met. The comparison is case sensitive. |
| tags | String | Yes | Yes | Specifies the list of tags in the data set, delimited by EOL characters. If specified, the set of tags in a data set will be used when the next data set run starts. You can write either an EOL-delimited text string or a flattened LabVIEW array of strings to this tag. |

Parent topic:

Interact with Data Using I/O Servers

Related concepts:

- Log Data in Sets

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=using-epics-client-i-o-servers-dsc-module-or.html language=enus -->
## TOPIC 00130: Use EPICS Client I/O Servers

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `using-epics-client-i-o-servers-dsc-module-or.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/using-epics-client-i-o-servers-dsc-module-or.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the EPICS Client I/O servers to monitor and update Process Variables (PVs) that an input/output controller (IOC) or Channel Access Server (CAS) publishes using the CA network protocol or to create EPICS Client I/O server to monitor and update the value of a PV that exists on an IOC or CAS.With E

### Use EPICS Client I/O Servers

Use the EPICS Client I/O servers to monitor and update Process Variables (PVs) that an
 input/output controller (IOC) or Channel Access Server (CAS) publishes using the CA
 network protocol or to create EPICS Client I/O server to monitor and update the value of
 a PV that exists on an IOC or CAS.

With EPICS Client I/O servers, the LabVIEW Datalogging and Supervisory Control (DSC) Module and
 the LabVIEW Real-Time Module act as Channel Access (CA) clients.

You also can publish shared variables to an EPICS network by using EPICS Server I/O servers.

Parent topic:

Use EPICS I/O Servers

Related concepts:

- Create EPICS Client I/O Servers

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=using-epics-i-o-servers-dsc-module-or-real-ti.html language=enus -->
## TOPIC 00131: Use EPICS I/O Servers

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `using-epics-i-o-servers-dsc-module-or-real-ti.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/using-epics-i-o-servers-dsc-module-or-real-ti.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Experimental Physics and Industrial Control System (EPICS) is a set of open-source software tools you can use to develop large, distributed control systems.EPICS systems use the Channel Access (CA) network protocol to pass data between Channel Access clients (CACs) and Channel Access servers (CA

### Use EPICS I/O Servers

The Experimental Physics and Industrial Control System (EPICS) is a set of open-source
 software tools you can use to develop large, distributed control systems.

EPICS systems use the Channel Access (CA) network protocol to pass data between Channel Access
 clients (CACs) and Channel Access servers (CASs). The CA network protocol is a
 TCP/IP-based protocol.

Typically, a CAS contains multiple Process Variables (PVs). A PV represents a single value within
 a server and is the primary object of the CA network protocol. You can use CACs to read,
 write, or subscribe to PVs in an EPICS system.

In LabVIEW, you can create the following
 types of EPICS I/O servers:

EPICS Client I/O servers

EPICS Server I/O servers

Note

Argonne National Laboratory

Refer to the *Interactively Configuring EPICS I/O
 Servers* article on the manufacturer's web site for more information about
 how to interactively configure both EPICS Client I/O servers and EPICS Server I/O
 servers in LabVIEW.

- [Use EPICS Client I/O Servers](using-epics-client-i-o-servers-dsc-module-or.html)
- [Use EPICS Server I/O Servers](use-epics-server-i-o-servers-dsc-module-or.html)

Parent topic:

Interact with Data Using I/O Servers

Related information:

- Interactively Configuring LabVIEW EPICS I/O Clients and
 Servers
- EPICS at Argonne

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=using-query-commands.html language=enus -->
## TOPIC 00132: Using Query Commands

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `using-query-commands.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/using-query-commands.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use data transform and shared variable type case commands to query the Citadel data tables. Data TransformsYou can include special commands that perform data transforms to manipulate and analyze historical data. You cannot use data transform commands to query raw data tables.The following table illu

### Using Query Commands

Use data transform and shared variable type case commands to query the
 Citadel data tables.

#### Data Transforms

You can
 include special commands that perform data transforms to manipulate and analyze
 historical data. You cannot use data transform commands to query raw data
 tables.

The following table illustrates the query commands to transform
 Citadel data:

| Command | Transformation |
| --- | --- |
| MATH_MIN(shared variable \| TO_DISCRETE(shared variable) \| TO_CONTINUOUS(shared variable)) | Returns the minimum for a shared variable across the interval. |
| MATH_MAX(shared variable \| TO_DISCRETE(shared variable) \| TO_CONTINUOUS(shared variable)) | Returns the maximum for a shared variable across the interval. |
| MATH_AVG(shared variable \| TO_DISCRETE(shared variable) \| TO_CONTINUOUS(shared variable)) | Returns the average for a shared variable across the interval. |
| MATH_STDEV(shared variable \| TO_DISCRETE(shared variable) \| TO_CONTINUOUS(shared variable)) | Returns the standard deviation for a shared variable across the interval. |
| MATH_STARTS(shared variable \| TO_DISCRETE(shared variable) \| TO_CONTINUOUS(shared variable)) | Returns the number of starts (that is, the number of transitions from OFF to ON) for a shared variable across the interval. For numeric points, Citadel interprets 0.0 as OFF and treats all other numbers as ON. |
| MATH_STOPS(shared variable \| TO_DISCRETE(shared variable) \| TO_CONTINUOUS(shared variable)) | Returns the number of stops (that is, the number of transitions from ON to OFF) for a shared variable across the interval. For numeric points, Citadel interprets 0.0 as OFF and treats all other numbers as ON. |
| MATH_ETM(shared variable \| TO_DISCRETE(shared variable) \| TO_CONTINUOUS(shared variable)) | Returns the amount of time a shared variable was in the ON state across the interval. For numeric points, Citadel interprets all nonzero numbers as ON. |
| MATH_QUAL(shared variable \| TO_DISCRETE(shared variable) \| TO_CONTINUOUS(shared variable)) | Returns the ratio of time for which valid data exist for shared variables across the interval to the length of the interval itself. If valid data exist for only one-half of the interval, MATH_QUAL returns 0.5. You might encounter gaps in the historical data traces in Citadel because of computer shutdown, Shared Variable Engine shutdown, or similar occurrences. |
| RAW_VALUE() | Returns the last raw, or uninterpolated, value before each interval boundary. The Citadel historical database might return raw values for partial intervals. Partial intervals contain at least one data point but have no data at the interval boundary. Therefore, the Citadel historical database does not return an interpolation point. For some partial intervals, the Citadel historical database adds an additional row of data to the query results. This data contains a NULL interpolation result and the last raw datapoint in the trace. This transform can take any trace type as an input. |
| RAW_UTC_TIMESTAMP() | Returns the timestamp, in UTC time, associated with the RAW_VALUE() transform result. This transform is equivalent to the UTCTime column name in the Citadel data tables. This transform can take any trace type as an input. |
| RAW_LOCAL_TIMESTAMP() | Returns the timestamp, in local time, associated with the RAW_VALUE() transform result. This transform is equivalent to the LocalTime column name in the Citadel data tables. This transform can take any trace type as an input. |

You can use the RAW_VALUE(),
 RAW_UTC_TIMESTAMP(), and RAW_LOCAL_TIMESTAMP()
 commands in combination to append the last raw point from a trace to a set of
 interpolated results. You also can use these commands to query raw points from
 multiple traces. You can use the interpolation interval to control the number of
 results that the Citadel historical database returns, and you can
 display the results in a table.

Note that Citadel supports
 standard set functions (MIN, MAX, AVG, COUNT) and you can use
 them on any Citadel table. Distinguish between set functions MIN,
 MAX, AVG and Citadel transform functions MATH_MIN, MATH_MAX,
 MATH_AVG. Set functions perform calculations on query result. Transform functions
 perform calculations on interpolation intervals.

#### Shared Variable Type Cast
 Commands

You can use type cast commands to override current type of shared
 variable that you query. You must distinguish between discrete and continuous shared
 variables because different point interpolation is used for different shared
 variables. Discrete points are interpolated using step interpolation. Continuous
 points are interpolated using linear interpolation. You might want to override
 shared variable type to enforce step or linear interpolation.

The following
 table shows the shared variable type cast commands:

| Citadel 5 ODBC driver | Description |
| --- | --- |
| TO_DISCRETE(project variable) | Cast current shared variable type to discrete (that is, the shared variable is treated as discrete) |
| TO_CONTINUOUS(shared variable) | Cast current shared variable type to continuous (that is, the shared variable is treated as continuous) |

Use these data commands to calculate and retrieve complex information, such
 as averages and standard deviations, from the database. You do not need to extract
 the raw data and then manipulate them in another application.

Parent topic:

Access Citadel Data with SQL

Related concepts:

- Pass Data between LabVIEW and the Shared Variable Engine

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=view-system-errors-and-events.html language=enus -->
## TOPIC 00133: View System Errors and Events

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `view-system-errors-and-events.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/view-system-errors-and-events.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: System errors are conditions that result in problems with the LabVIEW Datalogging and Supervisory Control (DSC) Module functioning and occur on a system level, as opposed to the shared variable level. When a system error occurs, LabVIEW prompts you with an error dialog box.System events are changes

### View System Errors and Events

System errors are conditions that result in problems with the LabVIEW Datalogging and
 Supervisory Control (DSC) Module functioning and occur on a system level, as opposed to
 the shared variable level. When a system error occurs, LabVIEW prompts you with an error
 dialog box.

System events are changes in the system that cause a change in behavior that is not problematic,
 such as events that the Distributed System Manager reports.

Parent topic:

Use Alarms and Events in DSC Module Applications

Related concepts:

- Shared Variable Engine Error Handling

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=viewing-alarms-and-events-using-the-alarm-and.html language=enus -->
## TOPIC 00134: Viewing Alarms and Events Using the Alarm and Event Display Control

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `viewing-alarms-and-events-using-the-alarm-and.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/viewing-alarms-and-events-using-the-alarm-and.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: The Alarm and Event Display control subscribes to the processes for which you are monitoring shared variables. When this process generates alarms, the Alarm and Event Display control automatically displays these alarms.Complete the following steps to select a different source from which to monitor a

### Viewing Alarms and Events Using the Alarm and
 Event Display Control

The Alarm and Event Display control subscribes to the processes for which
 you are monitoring shared variables. When this process generates
 alarms, the Alarm and Event Display control automatically displays
 these alarms.

Complete the following steps to select a different source from which to monitor alarms in the
 Alarm and Event Display control. To complete these steps, you must have a VI with an
 Alarm and Event Display control.

1. Select Operate»Change to Run Mode to
 switch the VI to run mode.
2. Right-click the Alarm and Event Display control and select
 Select Processes from the
 shortcut menu to display the Select
 Processes dialog box.
3. In the Available Processes list, navigate to the process for which you want to view alarms.
4. Click the Add button. The process appears in the Selected Processes list.
5. Click the OK button.

You also can filter the viewing of alarms and events in the Alarm and Event Display control.

Parent topic:

Use Alarms and Events in DSC Module Applications

Related tasks:

- Filtering Alarms and Events in the Alarm and Event Display Control

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=viewing-and-retrieving-alarm-and-event-data.html language=enus -->
## TOPIC 00135: Viewing and Retrieving Alarm and Event Data

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `viewing-and-retrieving-alarm-and-event-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/viewing-and-retrieving-alarm-and-event-data.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: The LabVIEW Datalogging and Supervisory Control (DSC) Module provides multiple options for viewing and retrieving alarm and event data.You can view and retrieve alarm and event data in the following ways: Alarm and Event Display Control — You can use the Alarm and Event Display control to view alarm

### Viewing and Retrieving Alarm and Event Data

The LabVIEW Datalogging and Supervisory Control (DSC) Module provides multiple
 options for viewing and retrieving alarm and event data.

You can view and retrieve alarm and event data in the following ways:

- Alarm and Event Display Control — You can use the Alarm
 and Event Display control to view alarm and event data that you want to monitor
 from any LabVIEW processes running on the network. You also can acknowledge
 alarms in this control.
- Summary Data Control — You can use this control to view
 alarm data, such as the number of active alarms and unacknowledged alarms in the
 system.
- VIs — You can use the Read Tag Alarms
 VI, the Alarms & Events VIs, and the
 Historical VIs to retrieve alarm and event data for
 displaying or for interacting with other VIs.
- Distributed System Manager — You can use the
 Alarms and Events view in the Distributed System
 Manager to monitor alarms and events. To launch the System Manager from LabVIEW,
 select Tools»Distributed System Manager.
- Historical Data Viewer — You can use the
 Historical Data Viewer, available in the Measurement
 & Automation Explorer (MAX), to create views of alarm and event data. You
 also can use the Historical Data Viewer to archive and
 export alarm and event data that has been logged to a Citadel
 database.
- Alarm Printer I/O Server — You can use this I/O server
 to print alarm and event data to a line printer.

Parent topic:

Use Alarms and Events in DSC Module Applications

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=writing-a-data-break-into-a-citadel-trace.html language=enus -->
## TOPIC 00136: Writing a Data Break into a Citadel Trace

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `writing-a-data-break-into-a-citadel-trace.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/writing-a-data-break-into-a-citadel-trace.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Write Trace Break VI to insert a data break into a Citadel trace.When you display Citadel data in a graph, the LabVIEW Datalogging and Supervisory Control (DSC) Module does not draw a line between two points separated by a data break.Complete the following steps to insert a data break: Add t

### Writing a Data Break into a Citadel Trace

Use the Write Trace Break VI to insert a data break into a
 Citadel trace.

When you display Citadel data in a graph, the LabVIEW Datalogging and
 Supervisory Control (DSC) Module does not draw a line between two points separated
 by a data break.

Complete the following steps to insert a data break:

1. Add the Write Trace Break VI on the block diagram.
2. Wire the trace reference output of the Open
 Trace VI to the trace reference input of
 the Write Trace Break VI. 
 Note If you close
 and then reopen a trace, the DSC Module automatically inserts a data break
 into the data stream, as if you had used the Write Trace
 Break VI.

Parent topic:

Logging Historical Data to the Citadel Database

<!--NI_TOPIC bundle=labview-datalogging-and-supervisory-control-module path=writing-a-value-to-a-citadel-trace.html language=enus -->
## TOPIC 00137: Writing a Value to a Citadel Trace

- bundle_id: `labview-datalogging-and-supervisory-control-module`
- source_path: `writing-a-value-to-a-citadel-trace.html`
- source_url: https://docs-be.ni.com/bundle/labview-datalogging-and-supervisory-control-module/raw/resource/enus/writing-a-value-to-a-citadel-trace.html
- document_id: `labview-datalogging-and-supervisory-control-module`
- page_type: `leaf`
- content_type: `task`
- source_description: You can use the Write Trace VI to append a data point to a Citadel trace. You can use the Write Trace VI to append a data point to a Citadel trace. Complete the following steps to write a value: Add the Write Trace VI on the block diagram. Wire the trace reference output of the Open Trace VI to the

### Writing a Value to a Citadel Trace

You can use the Write Trace VI to append a data point to a Citadel
 trace.

You can use the Write Trace VI to append a data point to a
 Citadel trace. Complete the following steps to write a value:

1. Add the Write Trace VI on the block diagram.
2. Wire the trace reference output of the Open
 Trace VI to the trace reference input of the
 Write Trace VI.
3. Wire the value and timestamp inputs of
 the Write Trace VI. 
 Leave the timestamp input unwired to use the current time. The
 Write Trace VI fails if the timestamp input is earlier than the
 timestamp of the last point written to the trace. You can determine the timestamp of the
 last point in the trace using the Get Trace Info VI.

Parent topic:

Logging Historical Data to the Citadel Database
