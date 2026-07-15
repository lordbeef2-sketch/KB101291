# NI DOCUMENT BUNDLE: systemlink-api

<!--NI_BUNDLE_CHUNK bundle=systemlink-api start=1 end=52 -->
<!--NI_TOPIC bundle=systemlink-api path=add-alarm-notes-description.html language=enus -->
## TOPIC 00001: Add Alarm Notes

- bundle_id: `systemlink-api`
- source_path: `add-alarm-notes-description.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/add-alarm-notes-description.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds one or more notes, or comments, to an alarm instance.

### Add Alarm
 Notes

Adds one or
 more notes, or comments, to an alarm instance.

Alarm Functions

Create alarms to implement rules and manage conditions affecting your systems, tests, or assets.

Multiple

Add a group of notes to an alarm instance to record information about it.

Single

Add a note to an alarm instance to record information about it.

API Reference

G, HTTP, Python, and .NET APIs allow you to programmatically access SystemLink data services outside of NI SystemLink Web Application.

SystemLink Nodes and Functions Reference for NXG and G Web Development Software

Use SystemLink nodes in NXG or G Web Development Software to communicate data between your test and measurement systems and your SystemLink Server account.

Alarm Functions

Create alarms to implement rules and manage conditions affecting your systems, tests, or assets.

Parent topic:

Alarm Functions

<!--NI_TOPIC bundle=systemlink-api path=advanced-file-transfer-functions.html language=enus -->
## TOPIC 00002: Advanced Functions

- bundle_id: `systemlink-api`
- source_path: `advanced-file-transfer-functions.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/advanced-file-transfer-functions.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Send files one data packet at a time, receive events when new files are available on the server, or receive file packets from the server asynchronously through events. Create Creates a file on the SystemLink file service using an AMQP configuration. Send Packet Uploads a packet containing file data

### Advanced Functions

Send files one data packet at a
 time, receive events when new files are available on the server, or receive
 file packets from the server asynchronously through events.

Create

Creates a file on the SystemLink
 file service using an AMQP configuration.

Send
 Packet

Uploads a packet containing file
 data to the SystemLink file service.

Send Last Packet

Uploads the last packet of the file's data, which causes the SystemLink file service to sequentially write the packets to disk.

Close

Terminates an open file reference.

Register for Available File Events

Subscribes to the SystemLink file service to receive events when new files are available.

Open

Opens a reference to an existing file on the SystemLink file service.

Unregister for Available File Events

Unsubscribes from the SystemLink file service to stop receiving available file events.

Register for Packet Events

Subscribes to the SystemLink file service to receive events when file data packets are available during a file download.

Download (Async)

Sends a request to the
 SystemLink file service to transfer a file or group of files.

Unregister for Packet Events

Unsubscribes from the SystemLink file service to stop receiving events when file data packets are available.

Parent topic:

File Transfer Functions

<!--NI_TOPIC bundle=systemlink-api path=advanced-nodes.html language=enus -->
## TOPIC 00003: Advanced Functions

- bundle_id: `systemlink-api`
- source_path: `advanced-nodes.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/advanced-nodes.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Read or write multiple times in a single call to improve performance.

### Advanced Functions

Read or write multiple times in a single call to improve performance.

Tag Functions

Use tags to read and write data values between systems and SystemLink Server.

Generate Tag Cluster

Creates or adds to an array of tag clusters, which specifies the tag data values for Multi Write to communicate.

Multi Read

Returns the value of an array of tags in a single operation.

Multi Write

Specifies values for multiple tags in a single operation.

API Reference

G, HTTP, Python, and .NET APIs allow you to programmatically access SystemLink data services outside of NI SystemLink Web Application.

SystemLink Nodes and Functions Reference for NXG and G Web Development Software

Use SystemLink nodes in NXG or G Web Development Software to communicate data between your test and measurement systems and your SystemLink Server account.

Tag Functions

Use tags to read and write data values between systems and SystemLink Server.

Parent topic:

Tag Functions

<!--NI_TOPIC bundle=systemlink-api path=alarm-functions.html language=enus -->
## TOPIC 00004: Alarm Functions

- bundle_id: `systemlink-api`
- source_path: `alarm-functions.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/alarm-functions.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create alarms to implement rules and manage conditions affecting your systems, tests, or assets. Acknowledge Alarm Acknowledges one or more active alarm instances on the server. Add Alarm Notes Adds one or more notes, or comments, to an alarm instance. Alarm Properties Reads and writes properties of

### Alarm Functions

Create alarms to implement
 rules and manage conditions affecting your systems, tests, or
 assets.

Acknowledge Alarm

Acknowledges one or more
 active alarm instances on the server.

Add Alarm Notes

Adds one or
 more notes, or comments, to an alarm instance.

Alarm Properties

Reads and
 writes properties of an alarm instance or a notification
 strategy.

Build Alarm ID

Creates an alarm id using the
 names of the system and application where the alarm
 originated.

Build Alarm Set Transition

Creates a set
 transition to apply when an alarm condition is
 met.

Clear
 Alarm

Clears a set alarm instance on the server if
 the VI does not detect a condition to trigger the alarm.

Create Alarm Query Filter

Creates a filter to query the server for
 specific alarms.

Delete
 Alarm

Removes the alarm instance identified by
 alarm from the server.

Get Notification Strategies

Queries
 the server for all alarm notification strategies.

Query
 Alarms

Searches the server
 for alarm instances that match the
 filter.

Set
 Alarm

Triggers an alarm instance to notify
 subscribers of an issue or a state requiring attention when an application
 detects a condition.

Parent topic:

SystemLink VIs and Functions Reference for LabVIEW

<!--NI_TOPIC bundle=systemlink-api path=alarm-nodes-description.html language=enus -->
## TOPIC 00005: Alarm Functions

- bundle_id: `systemlink-api`
- source_path: `alarm-nodes-description.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/alarm-nodes-description.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create alarms to implement rules and manage conditions affecting your systems, tests, or assets.

### Alarm
 Functions

Create alarms to implement
 rules and manage conditions affecting your systems, tests, or
 assets.

SystemLink Nodes and Functions Reference for NXG and G Web Development Software

Use SystemLink nodes in NXG or G Web Development Software to communicate data between your test and measurement systems and your SystemLink Server account.

Acknowledge Alarm

Acknowledges one or more active alarm instances on the server.

Add Alarm Notes

Adds one or more notes, or comments, to an alarm instance.

Build Alarm ID

Creates an alarm ID using the names of the system and application where the alarm originated.

Build Alarm Set Transition

set transition

Clear Alarm

Clears a set alarm instance on the server if the node does not detect a condition to trigger the alarm.

Delete Alarm

alarm

Create Alarm Query Filter

Returns a group of values you specify to query the server for matching alarm instances.

Get Alarm Information

Returns information, such as notes, severity levels, transition details, and more, about an alarm instance.

Get Notification Strategies

Queries the server for all alarm notification strategies.

Query Alarms

filter

Set Alarm

Triggers an alarm instance to notify subscribers of an issue or a state requiring attention when an application detects a condition.

API Reference

G, HTTP, Python, and .NET APIs allow you to programmatically access SystemLink data services outside of NI SystemLink Web Application.

SystemLink Nodes and Functions Reference for NXG and G Web Development Software

Use SystemLink nodes in NXG or G Web Development Software to communicate data between your test and measurement systems and your SystemLink Server account.

Parent topic:

SystemLink Nodes and Functions Reference for NXG and G Web Development Software

<!--NI_TOPIC bundle=systemlink-api path=asset-utilization-functions.html language=enus -->
## TOPIC 00006: Asset Utilization Functions

- bundle_id: `systemlink-api`
- source_path: `asset-utilization-functions.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/asset-utilization-functions.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Track how long and how often you use your assets in test systems. Start Utilization Collects usage data about an asset, group of assets, or all assets when a test or measurement task starts. End Utilization Stops collecting usage data about an asset or group of assets when a test or measurement task

### Asset Utilization Functions

Track how long and how
 often you use your assets in test systems.

Start Utilization

Collects usage data about an asset, group of assets, or all assets when a test
 or measurement task starts.

End
 Utilization

Stops
 collecting usage data about an asset or group of assets when a test or
 measurement task finishes.

Note

Parent topic:

Asset Functions

<!--NI_TOPIC bundle=systemlink-api path=asset-utilization-nodes.html language=enus -->
## TOPIC 00007: Asset Utilization Functions

- bundle_id: `systemlink-api`
- source_path: `asset-utilization-nodes.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/asset-utilization-nodes.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Track how long and how often you use your assets in test systems. G Web Development Software does not support this API.

### Asset Utilization
 Functions

Track how long and how
 often you use your assets in test systems.

Note

SystemLink Nodes and Functions Reference for NXG and G Web Development Software

Use SystemLink nodes in NXG or G Web Development Software to communicate data between your test and measurement systems and your SystemLink Server account.

End Utilization

Stops collecting usage data about an asset or group of assets when a test or measurement task finishes.

Start Utilization

Collects usage data about an asset, group of assets, or all assets when a test or measurement task starts.

API Reference

G, HTTP, Python, and .NET APIs allow you to programmatically access SystemLink data services outside of NI SystemLink Web Application.

SystemLink Nodes and Functions Reference for NXG and G Web Development Software

Use SystemLink nodes in NXG or G Web Development Software to communicate data between your test and measurement systems and your SystemLink Server account.

Parent topic:

SystemLink Nodes and Functions Reference for NXG and G Web Development Software

<!--NI_TOPIC bundle=systemlink-api path=build-alarm-id-description.html language=enus -->
## TOPIC 00008: Build Alarm ID

- bundle_id: `systemlink-api`
- source_path: `build-alarm-id-description.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/build-alarm-id-description.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an alarm ID using the names of the system and application where the alarm originated. alarm name Name of the alarm triggered. namespaceName to overwrite the default namespace.The namespace of the alarm ID defaults to the name of the top-level VI where the alarm triggered. If you want to over

### Build Alarm ID

Creates an alarm ID using the names of the system and application where the alarm
 originated.

[IMAGE alt='image' src='GUID-2974821B-BB47-4458-97EF-7F14FD209ADE-a5.png']

#### Inputs/Outputs

##### alarm name

Name of the alarm triggered.

##### namespace

Name to
 overwrite the default namespace.

The namespace of the alarm ID defaults to the name
 of the top-level VI where the alarm triggered. If you want to override the default
 namespace, wire a name to the namespace input.

##### alarm id

Unique identifier for a process or condition tracked by an alarm.

Parent topic:

Alarm Functions

<!--NI_TOPIC bundle=systemlink-api path=build-alarm-id.html language=enus -->
## TOPIC 00009: Build Alarm ID

- bundle_id: `systemlink-api`
- source_path: `build-alarm-id.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/build-alarm-id.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an alarm id using the names of the system and application where the alarm originated. alarm name Name of the alarm triggered. namespace Name to overwrite the default namespace. The namespace of the alarm id defaults to the name of the top-level VI where the alarm triggered. If you want to ov

### Build Alarm ID

Creates an alarm id using the
 names of the system and application where the alarm
 originated.

[IMAGE alt='image' src='GUID-A4D1C71A-5453-4066-80C6-A862A4C18B5D-a5.png']

#### alarm name

Name of the alarm triggered.

#### namespace

Name to overwrite the default namespace.

The namespace of the alarm id defaults to the name of the top-level VI where the alarm triggered. If you want to override the default namespace, wire a name to the namespace input.

#### alarm id

Unique identifier for a process or condition tracked by
 an alarm. The Build Alarm ID VI concatenates the names of
 the system and top-level VI where the rule triggered with the alarm
 name into a path.

For example, an
 alarm id may look like
 <system>.<namespace>.<alarm
 name>.

Parent topic:

Alarm Functions

<!--NI_TOPIC bundle=systemlink-api path=build-alarm-set-transition-multimode.html language=enus -->
## TOPIC 00010: Build Alarm Set Transition

- bundle_id: `systemlink-api`
- source_path: `build-alarm-set-transition-multimode.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/build-alarm-set-transition-multimode.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a set transition to apply when an alarm condition is met.

### Build Alarm Set
 Transition

Creates a set
 transition to apply when an alarm condition is
 met.

Alarm Functions

Create alarms to implement rules and manage conditions affecting your systems, tests, or assets.

Multiple Notifications

set transition

Single Notification

set transition

API Reference

G, HTTP, Python, and .NET APIs allow you to programmatically access SystemLink data services outside of NI SystemLink Web Application.

SystemLink Nodes and Functions Reference for NXG and G Web Development Software

Use SystemLink nodes in NXG or G Web Development Software to communicate data between your test and measurement systems and your SystemLink Server account.

Alarm Functions

Create alarms to implement rules and manage conditions affecting your systems, tests, or assets.

Parent topic:

Alarm Functions

<!--NI_TOPIC bundle=systemlink-api path=build-alarm-set-transition-multiple-description.html language=enus -->
## TOPIC 00011: Multiple Notifications

- bundle_id: `systemlink-api`
- source_path: `build-alarm-set-transition-multiple-description.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/build-alarm-set-transition-multiple-description.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a set transition to apply to multiple notification strategies when an alarm condition is met and the alarm changes in severity. Wire set transition to Set Alarm to create or update an alarm instance on the server. occurred at Timestamp of when a system or application triggered an alarm insta

### Multiple Notifications

Creates a set transition to apply to multiple
 notification strategies when an alarm condition is met and the alarm changes in
 severity.

Wire set transition to Set
 Alarm to create or update an alarm instance on the server.

[IMAGE alt='image' src='GUID-4D10FD55-DD02-460F-B98B-C63ACA043BEB-a5.png']

#### Inputs/Outputs

##### occurred at

Timestamp of when a system or application triggered an alarm instance.

##### value

Data value that caused the application to set the alarm.

##### condition

Description of what caused the transition.

For example, Greater than 90% CPU or Low disk
 space.

##### severity level

Number that indicates how severe an alarm instance is. In the user interface,
 severity levels range from 1 to 4, from lowest to highest.

##### notification strategy
 ids

IDs of the notification strategies that will trigger if the request creates an alarm
 instance or transitions to a new highest severity level.

##### keywords

Words or phrases associated with the transition.

##### properties

Key-value pairs associated with the transition.

##### set transition

State change and severity level that meet a specific condition to create or update an
 alarm instance.

Parent topic:

Build Alarm Set Transition

<!--NI_TOPIC bundle=systemlink-api path=build-alarm-set-transition-multiple.html language=enus -->
## TOPIC 00012: Build Alarm Set Transition (Multiple)

- bundle_id: `systemlink-api`
- source_path: `build-alarm-set-transition-multiple.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/build-alarm-set-transition-multiple.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a set transition to apply to multiple notification strategies when an alarm condition is met and the alarm changes in severity. Wire set transition to Set Alarm to create or update an alarm instance on the server. occurred at Timestamp of when a system or application triggered an alarm insta

### Build Alarm Set Transition (Multiple)

Creates a set
 transition to apply to multiple notification strategies when an
 alarm condition is met and the alarm changes in severity.

Wire set transition to
 Set Alarm to create or update an alarm instance on the
 server.

[IMAGE alt='image' src='GUID-AF9F3601-FEE4-4FAD-B19F-825529169934-a5.png']

#### occurred at

Timestamp of when a system or application triggered an
 alarm instance.

#### value

Data value that caused the
 application to set the alarm.

#### condition

Description of what caused the
 transition.

For example, Greater than 90% CPU or
 Low disk space.

#### severity level

Number that indicates how severe an alarm instance is.
 In the user interface, severity levels range from 1 to 4, from lowest to
 highest.

#### notification
 strategies

Plans established to notify the specified users with
 the correct information whenever an alarm triggers on a system or
 application.

#### keywords

Words or phrases associated with the transition.

Note

#### properties

Key-value pairs associated with the
 transition.

Note

#### set transition

State change and severity level
 that meet a specific condition to create or update an alarm instance.

Parent topic:

Build Alarm Set Transition

<!--NI_TOPIC bundle=systemlink-api path=build-alarm-set-transition-poly.html language=enus -->
## TOPIC 00013: Build Alarm Set Transition

- bundle_id: `systemlink-api`
- source_path: `build-alarm-set-transition-poly.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/build-alarm-set-transition-poly.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a set transition to apply when an alarm condition is met. Build Alarm Set Transition (Multiple) Creates a set transition to apply to multiple notification strategies when an alarm condition is met and the alarm changes in severity. Build Alarm Set Transition (Single) Creates a set transition

### Build Alarm Set Transition

Creates a set
 transition to apply when an alarm condition is
 met.

Build Alarm Set Transition (Multiple)

Creates a set
 transition to apply to multiple notification strategies when an
 alarm condition is met and the alarm changes in severity.

Build Alarm Set Transition (Single)

Creates
 a set transition to apply to a notification strategy
 when an alarm condition is met and the alarm changes in
 severity.

Parent topic:

Alarm Functions

<!--NI_TOPIC bundle=systemlink-api path=build-alarm-set-transition-single.html language=enus -->
## TOPIC 00014: Build Alarm Set Transition (Single)

- bundle_id: `systemlink-api`
- source_path: `build-alarm-set-transition-single.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/build-alarm-set-transition-single.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a set transition to apply to a notification strategy when an alarm condition is met and the alarm changes in severity. Wire set transition to Set Alarm to create or update an alarm instance on the server. occurred at Timestamp of when a system or application triggered an alarm instance. valu

### Build Alarm Set Transition (Single)

Creates
 a set transition to apply to a notification strategy
 when an alarm condition is met and the alarm changes in
 severity.

Wire set transition to
 Set Alarm to create or update an alarm instance on the
 server.

[IMAGE alt='image' src='GUID-DE23314D-7055-4E1B-A445-B8DED7932E0A-a5.png']

#### occurred at

Timestamp of when a system or application triggered an
 alarm instance.

#### value

Data value that caused the
 application to set the alarm.

#### condition

Description of what caused the
 transition.

For example, Greater than 90% CPU or
 Low disk space.

#### severity level

Number that indicates how severe an alarm instance is.
 In the user interface, severity levels range from 1 to 4, from lowest to
 highest.

#### notification
 strategy

Plan established to notify the specified users with
 the correct information whenever an alarm triggers on a system or
 application.

Wire Get Notification
 Strategies to this input.

#### keywords

Words or phrases associated with the transition.

Note

#### properties

Key-value pairs associated with the
 transition.

Note

#### set transition

State change and severity level
 that meet a specific condition to create or update an alarm instance.

Parent topic:

Build Alarm Set Transition

<!--NI_TOPIC bundle=systemlink-api path=configuration-functions.html language=enus -->
## TOPIC 00015: Configuration Functions

- bundle_id: `systemlink-api`
- source_path: `configuration-functions.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/configuration-functions.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Manage the connection between SystemLink data services and SystemLink. Open Configuration Initializes an HTTP or AMQP connection for SystemLink data services to communicate with SystemLink Server. Close Configuration Terminates connections associated with the configuration and invalidates open refer

### Configuration Functions

Manage the connection between SystemLink data services and SystemLink.

Open Configuration

Initializes an HTTP or AMQP connection for SystemLink data services
 to communicate with SystemLink Server.

Close
 Configuration

Terminates connections associated with the configuration and
 invalidates open references to SystemLink objects on SystemLink Server.

Use
 Workspace

Specifies the active workspace a VI that references this
 configuration uses to perform operations.

List
 Workspaces

Lists workspaces available on the SystemLink server.

Parent topic:

SystemLink VIs and Functions Reference for LabVIEW

<!--NI_TOPIC bundle=systemlink-api path=configure-retention-permanent-description.html language=enus -->
## TOPIC 00016: Permanent

- bundle_id: `systemlink-api`
- source_path: `configure-retention-permanent-description.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/configure-retention-permanent-description.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a retention policy to retain all historical tag values. Any tag that uses this retention policy may use a large amount of storage space on SystemLink Server. tag in Reference to a tag on the server. Use Open Tag or Query Tags to obtain this reference. error in Error conditions that occur bef

### Permanent

Creates a retention policy to retain all historical tag values.

Note

[IMAGE alt='image' src='GUID-75F9B177-6050-46C2-920B-FE2085EE1EC5-a5.png']

#### Inputs/Outputs

##### tag in

Reference to a tag on the server.

Use Open Tag or Query
 Tags to obtain this reference.

##### error in

Error conditions that occur before this node runs.

The node responds to this input
 according to standard error behavior.

Default value: No error

##### tag out

Reference to a specific tag on SystemLink Server.

##### error in

Error conditions that occur before this node runs.

The node responds to this input
 according to standard error behavior.

Default value: No error

Parent topic:

Configure Retention

Related information:

- Standard Error Behavior

<!--NI_TOPIC bundle=systemlink-api path=delete-alarm-description.html language=enus -->
## TOPIC 00017: Delete Alarm

- bundle_id: `systemlink-api`
- source_path: `delete-alarm-description.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/delete-alarm-description.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes the alarm instance identified by alarm from the server. Only delete an active alarm as a last resort. Instead, you should clear and acknowledge it or force clear and acknowledge it. alarm Alarm instance you want to delete on the server. error in Error conditions that occur before this node r

### Delete Alarm

Removes the alarm instance identified by alarm from
 the server.

Only delete an active alarm as a last resort. Instead, you should clear and acknowledge it or
 force clear and acknowledge it.

[IMAGE alt='image' src='GUID-6EFEEFAA-72AE-4FC8-BE7C-70B6F9FC28DF-a5.png']

#### Inputs/Outputs

##### alarm

Alarm instance you want to delete on the server.

##### error in

Error conditions that occur before this node runs.

The node responds to this input
 according to standard error behavior.

Default value: No error

##### error out

Error information.

The node produces this output according to standard error
 behavior.

Parent topic:

Alarm Functions

Related information:

- Standard Error Behavior

<!--NI_TOPIC bundle=systemlink-api path=get-system-name-description.html language=enus -->
## TOPIC 00018: Get System Name

- bundle_id: `systemlink-api`
- source_path: `get-system-name-description.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/get-system-name-description.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obtains the name of the system, if one is available. If a system name is not available, this VI returns an empty string. G Web Development Software does not support this function. system name Name of the system.

### Get System Name

Obtains the name of the system, if one is available.

If a system name is not available, this VI returns an empty string.

Note

[IMAGE alt='image' src='GUID-CDE3EBD7-A831-4EDD-A798-06221F9DBB61-a5.png']

#### Inputs/Outputs

##### system name

Name of the system.

Parent topic:

Utility Functions

<!--NI_TOPIC bundle=systemlink-api path=list-file-contents-multimode.html language=enus -->
## TOPIC 00019: List File Contents

- bundle_id: `systemlink-api`
- source_path: `list-file-contents-multimode.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/list-file-contents-multimode.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns channel group and channel names from a TDMS file.

### List File
 Contents

Returns channel group and channel names from a TDMS file.

TDM Reader Functions

Visualize and interact with waveform data in TDMS files.

GroupsAndChannels

Returns channel group and channel names from a TDMS file.

Channels

Returns channel names from channel group in a TDMS file.

API Reference

G, HTTP, Python, and .NET APIs allow you to programmatically access SystemLink data services outside of NI SystemLink Web Application.

SystemLink Nodes and Functions Reference for NXG and G Web Development Software

Use SystemLink nodes in NXG or G Web Development Software to communicate data between your test and measurement systems and your SystemLink Server account.

TDM Reader Functions

Visualize and interact with waveform data in TDMS files.

Parent topic:

TDM Reader Functions

<!--NI_TOPIC bundle=systemlink-api path=list-workspaces-description.html language=enus -->
## TOPIC 00020: List Workspaces

- bundle_id: `systemlink-api`
- source_path: `list-workspaces-description.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/list-workspaces-description.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Lists workspaces available on the SystemLink server. SystemLink uses workspaces to organize and control access to data on the server.This node returns only workspaces that the current Configuration can access. By default, this node does not return archived workspaces. configuration Connection to the

### List Workspaces

Lists workspaces available on the SystemLink server. SystemLink uses
 workspaces to organize and control access to data on the server.

This node returns only
 workspaces that the current Configuration can access. By default, this node does not return
 archived workspaces.

[IMAGE alt='image' src='GUID-840944D3-689E-468A-AD7F-8A8383E29392-a5.png']

#### Inputs/Outputs

##### configuration

Connection to the server.

If you leave this input unwired, this node uses the
 default connection. It automatically retrieves your SystemLink Server credentials when you
 execute the application on a managed system or server.

##### include
 archived?

Boolean that specifies whether or not to include archived workspaces in the list.

##### error in

Error conditions that occur before this node runs.

The node responds to this input
 according to standard error behavior.

Default value: No error

##### configuration
 out

Connection to the server.

##### workspaces

Workspaces this node can access using the current configuration. By default, this node
 does not return archived workspaces.

##### error out

Error information.

The node produces this output according to standard error
 behavior.

Parent topic:

Configuration Functions

Related information:

- Standard Error Behavior

<!--NI_TOPIC bundle=systemlink-api path=multi-read-history-description.html language=enus -->
## TOPIC 00021: Multi Read History

- bundle_id: `systemlink-api`
- source_path: `multi-read-history-description.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/multi-read-history-description.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the historical values from multiple tags in a single operation. tags in Reference to a specific tag or a group of tags on SystemLink Server.Use Open Tag or Query Tags to obtain this reference. window Time range you specify to read historical tag values. The default is set to read all values

### Multi Read History

Returns the historical values from multiple tags in a single operation.

[IMAGE alt='image' src='GUID-59B06082-F111-4DF6-A305-B5D6C40DD7C7-a5.png']

#### Inputs/Outputs

##### tags in

Reference to a specific tag or a group of tags on SystemLink Server.

Use Open Tag or Query Tags to
 obtain this reference.

##### window

Time range you specify to read historical tag values.

The default is set to read all values decimated to 1,000.

##### error in

Error conditions that occur before this node runs.

The node responds to this input
 according to standard error behavior.

Default value: No error

##### next window

Next page of historical tag data, if available.

##### tags out

Reference to a specific tag or a group of tags on SystemLink Server.

Use Open Tag or Query Tags to
 obtain this reference.

##### values

Data values of the tag history.

##### end of data?

Boolean that indicates whether the node read the last of the data for the tag.

##### error out

Error information.

The node produces this output according to standard error
 behavior.

Parent topic:

Historian Functions

<!--NI_TOPIC bundle=systemlink-api path=multi-write-description.html language=enus -->
## TOPIC 00022: Multi Write

- bundle_id: `systemlink-api`
- source_path: `multi-write-description.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/multi-write-description.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies values for multiple tags in a single operation. The tags may be of different data types. tag clusters Clusters of tags the web service references to communicate data. error in Error conditions that occur before this node runs. The node responds to this input according to standard error beh

### Multi Write

Specifies values for multiple tags in a single operation.

The tags may be of different data types.

[IMAGE alt='image' src='GUID-2C6C9ACB-F989-4EC6-8F9B-AF4E7F262E53-a5.png']

#### Inputs/Outputs

##### tag clusters

Clusters of tags the web service references to communicate data.

##### error in

Error conditions that occur before this node runs.

The node responds to this input
 according to standard error behavior.

Default value: No error

##### error out

Error information.

The node produces this output according to standard error
 behavior.

#### Programming Patterns

Wire this node to Generate Tag Cluster to build the tag clusters input.

Parent topic:

Advanced Functions

Related reference:

- Generate Tag Cluster
- Boolean
- DBL
- I32
- String
- Timestamp
- U64

Related information:

- Standard Error Behavior

<!--NI_TOPIC bundle=systemlink-api path=query-alarms-multimode.html language=enus -->
## TOPIC 00023: Query Alarms

- bundle_id: `systemlink-api`
- source_path: `query-alarms-multimode.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/query-alarms-multimode.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Searches the server for alarm instances that match the filter.

### Query
 Alarms

Searches the server
 for alarm instances that match the
 filter.

Alarm Functions

Create alarms to implement rules and manage conditions affecting your systems, tests, or assets.

No Transitions

filter

With Transitions

filter

API Reference

G, HTTP, Python, and .NET APIs allow you to programmatically access SystemLink data services outside of NI SystemLink Web Application.

SystemLink Nodes and Functions Reference for NXG and G Web Development Software

Use SystemLink nodes in NXG or G Web Development Software to communicate data between your test and measurement systems and your SystemLink Server account.

Alarm Functions

Create alarms to implement rules and manage conditions affecting your systems, tests, or assets.

Parent topic:

Alarm Functions

<!--NI_TOPIC bundle=systemlink-api path=query-files.html language=enus -->
## TOPIC 00024: Query Files

- bundle_id: `systemlink-api`
- source_path: `query-files.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/query-files.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Searches the SystemLink file service for files matching filter in using an HTTP configuration.If you do not provide a filter, this function opens references to every file on the service. The SystemLink file service limits the maximum number of results returned in a single query to 1,000 files.G Web

### Query Files

Searches the SystemLink file service for files matching filter in using an HTTP configuration.

If you do not provide a
 filter, this function opens references to every file on the service. The SystemLink file
 service limits the maximum number of results returned in a single query to 1,000
 files.

Note

[IMAGE alt='image' src='GUID-857D7E0F-8BC8-4946-AD12-B071758BD799-a5.png']

#### Inputs/Outputs

##### configuration

Connection to the server.

If you leave this input unwired, this node uses the
 default connection. It automatically retrieves your SystemLink Server credentials when you
 execute the application on a managed system or server.

##### filter in

Query or queries you want to use find matching files on the server.

Default value:
 new filter

##### limit to configured
 workspace?

Boolean that determines whether this node only queries for tags in the workspace you
 specify in configuration.

By default, the node
 queries for tags from all accessible workspaces.

##### error in

Error conditions that occur before this node runs.

The node responds to this input
 according to standard error behavior.

Default value: No error

##### files

Files returned from the server.

##### error out

Error information.

The node produces this output according to standard error
 behavior.

Parent topic:

File Transfer Functions

Related information:

- Standard Error Behavior

<!--NI_TOPIC bundle=systemlink-api path=query-tags-description.html language=enus -->
## TOPIC 00025: Query Tags

- bundle_id: `systemlink-api`
- source_path: `query-tags-description.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/query-tags-description.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Searches the server for tags matching the criteria you specify. If an input is empty, this node opens references to every tag on the server. configuration Connection to the server.If you leave this input unwired, this node uses the default connection. It automatically retrieves your SystemLink Serve

### Query Tags

Searches the server for tags matching the criteria you specify.

If an input is empty, this node opens references to every tag on the server.

[IMAGE alt='image' src='GUID-34CD554D-8E0B-4453-88BC-4E373C8ECFAF-a5.png']

#### Inputs/Outputs

##### configuration

Connection to the server.

If you leave this input unwired, this node uses the
 default connection. It automatically retrieves your SystemLink Server credentials when you
 execute the application on a managed system or server.

##### paths

Paths to tag references.

Note

##### keywords

Specific words provided to find tags.

##### properties

Key-value pairs that exist as metadata on a tag.

##### limit to configured
 workspace?

Boolean that determines whether this node only queries for tags in the workspace you
 specify in configuration.

By default, the node
 queries for tags from all accessible workspaces.

##### error in

Error conditions that occur before this node runs.

The node responds to this
 input according to standard error behavior.

Default value: No error

##### skip

Number of tags skipped to limit the amount returned from the server.

If the input
 is left empty, the query returns the first 1000 results by default.

##### take

Number of tags requested from the server.

If the input is left empty, the query
 returns the first 1000 results by default.

##### tags

Tags the server references to communicate measurement data.

##### total count

Total number of tags on the server.

##### error out

Error information.

The node produces this output according to standard error
 behavior.

Parent topic:

Tag Functions

Related information:

- Standard Error Behavior

<!--NI_TOPIC bundle=systemlink-api path=read-data-multimode.html language=enus -->
## TOPIC 00026: Read Data

- bundle_id: `systemlink-api`
- source_path: `read-data-multimode.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/read-data-multimode.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns data from a TDMS file.

### Read
 Data

Returns data from a TDMS file.

TDM Reader Functions

Visualize and interact with waveform data in TDMS files.

1Chan Boolean

channel name in

NChan Boolean

channel names in

1Chan Double

channel name in

NChan Double

channel names in

1Chan I16

channel name in

NChan I16

channel names in

1Chan I32

channel name in

NChan I32

channel names in

1Chan I8

channel name in

NChan I8

channel names in

1Chan Single

channel name in

NChan Single

channel names in

1Chan String

channel name in

NChan String

channel names in

1Chan Timestamp

channel name in

NChan Timestamp

channel names in

1Chan U16

channel name in

NChan U16

channel names in

1Chan U32

channel name in

NChan U32

channel names in

1Chan U8

channel name in

NChan U8

channel names in

1Chan Waveform

channel name in

NChan Waveform

channels name in

API Reference

G, HTTP, Python, and .NET APIs allow you to programmatically access SystemLink data services outside of NI SystemLink Web Application.

SystemLink Nodes and Functions Reference for NXG and G Web Development Software

Use SystemLink nodes in NXG or G Web Development Software to communicate data between your test and measurement systems and your SystemLink Server account.

TDM Reader Functions

Visualize and interact with waveform data in TDMS files.

Parent topic:

TDM Reader Functions

<!--NI_TOPIC bundle=systemlink-api path=read-description.html language=enus -->
## TOPIC 00027: Read

- bundle_id: `systemlink-api`
- source_path: `read-description.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/read-description.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a message from the queue. To read a message, you must subscribe to the topic the message is published to. If you do not subscribe to the topic, you cannot receive the message. Therefore, you cannot read it. If there are no queued messages, the call synchronously blocks up to the timeout spec

### Read

Returns a message from the queue.

To read a message, you must subscribe to the topic the message is published to. If you do not subscribe to the topic, you cannot receive the message. Therefore, you cannot read it.

If there are no queued messages, the call synchronously blocks up to the timeout specified or to the maximum timeout the web service defines, whichever is smaller. The SystemLink Server times out after 10 seconds.

[IMAGE alt='image' src='GUID-BF40D150-5C68-479D-B559-AC3F3E54C455-a5.png']

#### Inputs/Outputs

##### message session
 in

Synchronous message session established with the server.

##### timeout

Time, in milliseconds, that this node waits for an enqueued message before timing out.

Default value: 100

##### error in

Error conditions that occur before this node runs.

The node responds to this input
 according to standard error behavior.

Default value: No error

##### message session out

Synchronous message session established with the server.

##### topic

Channel to which endpoints publish or subscribe messages.

Ensure topic names are unique to avoid name collisions.

##### message

Text published for subscribers of a topic to read, if a message
 exists.

##### error out

Error information.

The node produces this output according to standard error
 behavior.

##### dequeue status

Information about the current state of the node.

If True, the node received an
 incoming message. If False, the node timed out.

Parent topic:

Message Functions

Related information:

- Standard Error Behavior
- Sending Messages Between Systems

<!--NI_TOPIC bundle=systemlink-api path=read-tag-boolean-description.html language=enus -->
## TOPIC 00028: Boolean

- bundle_id: `systemlink-api`
- source_path: `read-tag-boolean-description.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/read-tag-boolean-description.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of the tag. The data type of the tag must be a Boolean. tag in Tag the server references to communicate measurement data. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Default value: No error count

### Boolean

Returns the value of the tag.

The data type of the tag must be a Boolean.

[IMAGE alt='image' src='GUID-5A171EA8-D13A-45FA-AE63-0D96613087BB-a5.png']

#### Inputs/Outputs

##### tag in

Tag the server references to communicate measurement data.

##### error in

Error conditions that occur before this node runs.

The node responds to this input
 according to standard error behavior.

Default value: No error

##### count

Total number of times a system or group of systems writes to a tag.

##### tag out

Tag the server references to communicate measurement data.

##### value

Data value of the tag or tags.

##### time stamp

Date and time the server obtained the most recent data value.

##### error out

Error information.

The node produces this output according to standard error
 behavior.

Parent topic:

Read Tag

Related information:

- Standard Error Behavior
- Transferring Data Using Tags

<!--NI_TOPIC bundle=systemlink-api path=read-tag-dbl-description.html language=enus -->
## TOPIC 00029: DBL

- bundle_id: `systemlink-api`
- source_path: `read-tag-dbl-description.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/read-tag-dbl-description.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of the tag. The data type of the tag must be a double-precision, floating-point number. tag in Tag the server references to communicate measurement data. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior

### DBL

Returns the value of the tag.

The data type of the tag must be a double-precision, floating-point
 number.

[IMAGE alt='image' src='GUID-5A171EA8-D13A-45FA-AE63-0D96613087BB-a5.png']

#### Inputs/Outputs

##### tag in

Tag the server references to communicate measurement data.

##### error in

Error conditions that occur before this node runs.

The node responds to this input
 according to standard error behavior.

Default value: No error

##### aggregates

Values the tag collects since calling Reset Aggregates.

If a tag is set to collect aggregates, every write to the tag updates the aggregate
 of the tag.

##### tag out

Tag the server references to communicate measurement data.

##### value

Data value of the tag or tags.

##### time stamp

Date and time the server obtained the most recent data value.

##### error out

Error information.

The node produces this output according to standard error
 behavior.

Parent topic:

Read Tag

Related information:

- Standard Error Behavior
- Transferring Data Using Tags

<!--NI_TOPIC bundle=systemlink-api path=read-tag-history-multimode.html language=enus -->
## TOPIC 00030: Read Tag History

- bundle_id: `systemlink-api`
- source_path: `read-tag-history-multimode.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/read-tag-history-multimode.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the historical values from a single tag. The data type of the tag must match the polymorphic instance.

### Read Tag
 History

Returns the historical values from a single tag. The
 data type of the tag must match the polymorphic instance.

Historian Functions

Retain historical tag values to review, troubleshoot, or analyze data over time.

Boolean

Returns the historical tags of a single tag. The data type of the tag must be a Boolean.

DBL

Returns the historical values of a single tag. The data type of the tag must be a double-precision, floating-point number.

I32

Returns the historical values from a single tag. The data type of the tag must be a 32-bit integer.

String

Returns the historical values from a single tag. The data type of the tag must be a string.

Timestamp

Returns the historical values of a single tag. The data type of the tag must be a timestamp.

U64

Returns the historical values from a single tag. The data type of the tag must be an unsigned 64-bit integer.

API Reference

G, HTTP, Python, and .NET APIs allow you to programmatically access SystemLink data services outside of NI SystemLink Web Application.

SystemLink Nodes and Functions Reference for NXG and G Web Development Software

Use SystemLink nodes in NXG or G Web Development Software to communicate data between your test and measurement systems and your SystemLink Server account.

Tag Functions

Use tags to read and write data values between systems and SystemLink Server.

Historian Functions

Retain historical tag values to review, troubleshoot, or analyze data over time.

Parent topic:

Historian Functions

<!--NI_TOPIC bundle=systemlink-api path=send-file-multimode.html language=enus -->
## TOPIC 00031: Send

- bundle_id: `systemlink-api`
- source_path: `send-file-multimode.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/send-file-multimode.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a local file or data string to the server using the configuration you specify.G Web Development Software does not support this function.

### Send

Sends a local file or data string to the server using the configuration you
 specify.G Web Development Software does not support this function.

File Transfer Functions

Upload files to your SystemLink Server, where you can also update, delete, or download them.

Buffer

Uploads a buffer of data to create a new file on the SystemLink file service using the HTTP configuration.

Path

Sends a local file to the SystemLink file service using the HTTP configuration.

API Reference

G, HTTP, Python, and .NET APIs allow you to programmatically access SystemLink data services outside of NI SystemLink Web Application.

SystemLink Nodes and Functions Reference for NXG and G Web Development Software

Use SystemLink nodes in NXG or G Web Development Software to communicate data between your test and measurement systems and your SystemLink Server account.

File Transfer Functions

Upload files to your SystemLink Server, where you can also update, delete, or download them.

Parent topic:

File Transfer Functions

<!--NI_TOPIC bundle=systemlink-api path=set-alarm.html language=enus -->
## TOPIC 00032: Set Alarm

- bundle_id: `systemlink-api`
- source_path: `set-alarm.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/set-alarm.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Triggers an alarm instance to notify subscribers of an issue or a state requiring attention when an application detects a condition. Wire Clear Alarm after this VI to clear the alarms associated with the alarm instance. HTTP configuration HTTP connection to the server. If you leave this input unwire

### Set Alarm

Triggers an alarm instance to notify
 subscribers of an issue or a state requiring attention when an application
 detects a condition.

Wire Clear Alarm after this VI to clear the alarms associated with
 the alarm instance.

[IMAGE alt='image' src='GUID-2DF12DE9-0AB7-40D5-8B09-54EF3E2682CB-a5.png']

#### HTTP configuration

HTTP connection to the server.

If you leave this input unwired, this VI
 uses the default connection and automatically retrieves your SystemLink Server
 credentials when you execute the application on a managed system or on the
 server.

#### additional information

Variety of data about the new alarm instance, such as
 the application or user who created it and keywords and properties associated
 with it.

This VI ignores this input when
 updating an existing alarm instance.

#### alarm id

Unique identifier for a process or condition tracked by
 an alarm. The Build Alarm ID VI concatenates the names of
 the system and top-level VI where the rule triggered with the alarm
 name into a path.

For example, an
 alarm id may look like
 <system>.<namespace>.<alarm
 name>.

#### set transition

State change and severity level
 that meet a specific condition to create or update an alarm instance.

Wire Build Alarm Set Transition to
 this input.

#### display name

Title you want to give the alarm instance.

This VI ignores this input when updating an existing alarm
 instance.

#### channel

Resource associated with the alarm. For example, if an
 application sets an alarm because a wireless network went down, the
 channel could be the name of the network and the
 resource type classifies the alarm as the
 network.

This VI ignores this input when it
 updates an existing alarm instance.

#### error in

standard error behavior

#### resource type

Type of resource associated with the alarm. For example,
 if an application sets an alarm because a wireless network went down, the
 channel may be the name of the network where the
 alarm triggered and the resource type may classify the
 alarm as the network.

This VI ignores this
 input when it updates an existing alarm instance.

#### alarm

Alarm instance created or updated.

#### alarm instance created or
 updated?

Boolean that determines
 whether an alarm instance with the provided set
 transition already exists. If an alarm instance already exists
 or the current severity level already occurred, it returns False and
 alarm returns default data.

#### error out

standard error behavior

Parent topic:

Alarm Functions

<!--NI_TOPIC bundle=systemlink-api path=set-property-file.html language=enus -->
## TOPIC 00033: Set Property

- bundle_id: `systemlink-api`
- source_path: `set-property-file.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/set-property-file.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes the property value of the file that corresponds to the key and creates the property if it does not exist. You must wire this VI to Update Metadata Properties to reflect the updates on the SystemLink file service. file in File on the SystemLink file service. key Unique identifier for the prope

### Set Property

Writes the property value of
 the file that corresponds to the key and creates
 the property if it does not exist.

You must wire this VI to Update Metadata Properties to reflect the updates on the SystemLink file service.

[IMAGE alt='image' src='GUID-832AD26F-92E0-4BD8-95F2-EF7CE2D24A6D-a5.png']

#### file in

File on the SystemLink file service.

#### key

Unique identifier for the property you want to locate.

#### value

Metadata property to add.

#### error in

standard error behavior

#### file out

File on the SystemLink file service.

#### error out

standard error behavior

Parent topic:

File Transfer Functions

<!--NI_TOPIC bundle=systemlink-api path=subscribe.html language=enus -->
## TOPIC 00034: Subscribe

- bundle_id: `systemlink-api`
- source_path: `subscribe.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/subscribe.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Registers a session to receive messages published to a specific topic. Subscribers of a topic receive every message published to it. Wire several instances of this VI in a series to subscribe the multiple topics. Programming PatternsSending Messages Between Systems message session Message session es

### Subscribe

Registers a session to receive
 messages published to a specific topic.

Subscribers of a topic receive every message published to it. Wire several instances of this
 VI in a series to subscribe the multiple topics.

- Sending Messages Between
 Systems

[IMAGE alt='image' src='GUID-A9B2F4AA-3B4A-4529-9456-36F0B1763030-a5.png']

#### message session

Message session established with the server.

#### topic

Subject to which endpoints publish or subscribe messages.

#### error in

standard error behavior

#### message session out

Message session established with the server.

#### error out

standard error behavior

Parent topic:

Messages Functions

<!--NI_TOPIC bundle=systemlink-api path=systemlink-api-reference.html language=enus -->
## TOPIC 00035: API Reference

- bundle_id: `systemlink-api`
- source_path: `systemlink-api-reference.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/systemlink-api-reference.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `concept`
- source_description: G, HTTP, Python, and .NET APIs allow you to programmatically access SystemLink data services outside of NI SystemLink Web Application. Use the following table to choose which API meets your needs depending on your programming environment and the data services you want to access. API How to access Da

### API Reference

G, HTTP, Python, and .NET APIs allow you to programmatically access SystemLink data
 services outside of NI SystemLink Web Application.

| API | How to access | Data Services |
| --- | --- | --- |
| G (SystemLink nodes, or functions) | LabVIEW 2017 or later | Message TagTag HistorianServer Configuration File Transfer Test MonitorAlarmAsset UtilizationDataFinder |
| LabVIEW NXG 5.0 or later | Message TagTag HistorianServer Configuration File Transfer AlarmAsset UtilizationTDM ReaderUtilities |  |
| G Web Development Software 2021LabVIEW NXG Web Module 5.0 or later | Message TagTag HistorianServer ConfigurationAlarmsTDM Reader |  |
| Python | JupyterHubNI SystemLink API Clients for Python (Tag only) | File Ingestion TDM Reader TagTest Monitor Asset Management |
| HTTP | Any language-specific HTTP client | Auth ServiceUser ServiceAlarmAsset ManagementFileMessage OPC UA Tag Tag Historian TDM Reader Test Monitor Systems State ManagerSalt ServiceAnalysis Automation ConfigurationAnalysis Automation Package CreationData AnalysisData CartDataPlugin ServiceData Navigation UtilsData Navigation Data ServiceData Indexing ConfigurationData Preparation ConfigurationFederation Configuration |
| .NET | Any language-specific .NET client | CoreMessage Tag File Ingestion Test MonitorAsset Management |
| NI (Logos/Corba) | DIAdem | DataFinder |
| COM (DIAdem; Programming languages) | Object-oriented script interface | Analysis Automation Package CreationData Preparation Package CreationFile ServiceFile TransferTags |

Note

The Test Monitor API is only available in LabVIEW 2018 or later.

Related concepts:

- HTTP API Reference
- Python API Reference

<!--NI_TOPIC bundle=systemlink-api path=systemlink-nodes.html language=enus -->
## TOPIC 00036: SystemLink Nodes and Functions Reference for NXG and G Web Development Software

- bundle_id: `systemlink-api`
- source_path: `systemlink-nodes.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/systemlink-nodes.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use SystemLink nodes in NXG or G Web Development Software to communicate data between your test and measurement systems and your SystemLink Server account. G Web Development Software does not support the Asset Utilization, File Transfer, or Utilities APIs.

### SystemLink Nodes and
 Functions Reference for NXG and G Web Development Software

Use SystemLink nodes in NXG or G Web Development Software to communicate data between
 your test and measurement systems and your SystemLink Server
 account.

Note

API Reference

G, HTTP, Python, and .NET APIs allow you to programmatically access SystemLink data services outside of NI SystemLink Web Application.

Alarm Functions

Create alarms to implement rules and manage conditions affecting your systems, tests, or assets.

Asset Utilization Functions

Track how long and how often you use your assets in test systems.

Configuration Functions

Manage the HTTP or HTTPS connection with your server.

File Transfer Functions

Upload files to your SystemLink Server, where you can also update, delete, or download them.

Message Functions

Communicate as a network queue using the publish-subscribe model. Use messages to send commands, status updates, and data between your systems and server.

Tag Functions

Use tags to read and write data values between systems and SystemLink Server.

TDM Reader Functions

Visualize and interact with waveform data in TDMS files.

Utility Functions

Get information about systems connected to your server.

API Reference

G, HTTP, Python, and .NET APIs allow you to programmatically access SystemLink data services outside of NI SystemLink Web Application.

Parent topic:

API Reference

<!--NI_TOPIC bundle=systemlink-api path=systemlink-vi-function-reference.html language=enus -->
## TOPIC 00037: SystemLink VIs and Functions Reference for LabVIEW

- bundle_id: `systemlink-api`
- source_path: `systemlink-vi-function-reference.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/systemlink-vi-function-reference.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use SystemLink functions in LabVIEW to communicate data between your test and measurement systems and your SystemLink Server account. SystemLink data services allow you to efficiently manage and monitor your tests, assets, and systems data from anywhere in the world. Refer to the following list to s

### SystemLink VIs and Functions
 Reference for LabVIEW

Use SystemLink functions in LabVIEW to communicate data between your test and measurement systems and your SystemLink Server account.

SystemLink data services allow you to efficiently manage and monitor your tests, assets, and systems data from anywhere in the world. Refer to the following list to select which SystemLink API you want to learn more about.

Configuration Functions

Manage the HTTP or AMQP connection with your server.

File Transfer Functions

Upload files to your SystemLink Server, where you can also update, delete, or download them.

Tag Functions

Send pieces of data between distributed systems. Use tags to send and receive data from one system to other systems, or SystemLink Server.

Messages
 Functions

Communicate as
 a network queue using the publish-subscribe model. Use messages to send
 commands, status updates, and data between systems and applications.

Test Monitor Functions

Manage and communicate your test results and test steps between your test systems and SystemLink Server.

Utility Functions

Obtain system names and minion IDs to assign tag paths and properties to your data.

Alarm
 Functions

Create alarms to implement
 rules and manage conditions affecting your systems, tests, or
 assets.

Asset Utilization Functions

Track how long and how
 often you use your assets in test systems.

Parent topic:

API Reference

<!--NI_TOPIC bundle=systemlink-api path=tag-functions.html language=enus -->
## TOPIC 00038: Tag Functions

- bundle_id: `systemlink-api`
- source_path: `tag-functions.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/tag-functions.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use tags to read and write data values between systems and SystemLink Server. Build Path Identifies the system and top-level application that generates the tag as a tag path. Open Tag Opens a reference to a tag on the server. If the tag does not exist on the server, this VI creates it. Query Tags Se

### Tag Functions

Use tags to read and write data values between systems and SystemLink Server.

Build Path

Identifies the system and top-level
 application that generates the tag as a tag path.

Open Tag

Opens a reference to a tag on the server. If
 the tag does not exist on the server, this VI creates it.

Query Tags

Searches the server for tags matching the
 criteria you specify.

Close
 Tag

Closes a tag reference or an array of tag
 references.

Read Tag

Returns the value of the tag. The data type of the tag must match the polymorphic instance.

Write Tag

Specifies the value of the tag.

Reset
 Aggregates

Clears the aggregate
 information for a tag reference or group of tag references.

Delete Tag

Removes a tag or group of tags on the
 server.

Tag Properties

Returns information about an open
 tag reference so you can modify its configuration.

Retain historical tag values to review,
 troubleshoot, or analyze data over time.

Advanced Tag
 Functions

Read or write multiple times in a
 single call to improve performance.

Parent topic:

SystemLink VIs and Functions Reference for LabVIEW

<!--NI_TOPIC bundle=systemlink-api path=tag-properties.html language=enus -->
## TOPIC 00039: Tag Properties

- bundle_id: `systemlink-api`
- source_path: `tag-properties.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/tag-properties.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns information about an open tag reference so you can modify its configuration. reference Control reference associated with the object whose properties you want to configure. error inError conditions that occur before this VI runs. The VI responds to this input according to standard error behav

### Tag Properties

Returns information about an open
 tag reference so you can modify its configuration.

[IMAGE alt='image' src='GUID-934FB836-7F2F-4FC2-AF07-DB832B6DE5EA-a5.png']

#### reference

Control reference associated with the object whose properties you want to
 configure.

#### error in

standard error behavior

#### reference out

Control reference specified by
 reference. If you wrote values to this VI,
 the value of reference out may differ from
 reference in.

#### error out

standard error behavior

Parent topic:

Tag Functions

<!--NI_TOPIC bundle=systemlink-api path=tdm-reader-nodes.html language=enus -->
## TOPIC 00040: TDM Reader Functions

- bundle_id: `systemlink-api`
- source_path: `tdm-reader-nodes.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/tdm-reader-nodes.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Visualize and interact with waveform data in TDMS files.

### TDM Reader
 Functions

Visualize and interact with waveform data in TDMS files.

SystemLink Nodes and Functions Reference for NXG and G Web Development Software

Use SystemLink nodes in NXG or G Web Development Software to communicate data between your test and measurement systems and your SystemLink Server account.

Close File

Closes a reference to a TDMS file or group of TDMS files on the server.

Create Filter

Creates or adds to an existing filter to query TDMS files on the server.

Get TDM File Metadata

Returns metadata for a TDM file you specify.

List File Contents

Returns channel group and channel names from a TDMS file.

Open File

Opens a reference to a TDMS file on the server.

Query TDMS Files

filter in

Read Data

Returns data from a TDMS file.

API Reference

G, HTTP, Python, and .NET APIs allow you to programmatically access SystemLink data services outside of NI SystemLink Web Application.

SystemLink Nodes and Functions Reference for NXG and G Web Development Software

Use SystemLink nodes in NXG or G Web Development Software to communicate data between your test and measurement systems and your SystemLink Server account.

Parent topic:

SystemLink Nodes and Functions Reference for NXG and G Web Development Software

<!--NI_TOPIC bundle=systemlink-api path=test-monitor-functions.html language=enus -->
## TOPIC 00041: Test Monitor Functions

- bundle_id: `systemlink-api`
- source_path: `test-monitor-functions.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/test-monitor-functions.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Manage and communicate your test results and test steps between your test systems and SystemLink Server. Add Test Step Measurement Adds a measurement to a test step. Create Test Result Creates a test result or multiple test results on the server using the local reference from Initialize Test Result.

### Test Monitor Functions

Manage and communicate your test results and test steps between your test systems and SystemLink Server.

Add Test Step Measurement

Adds a measurement to a test
 step.

Create Test
 Result

Creates a test result or
 multiple test results on the server using the local reference from
 Initialize Test Result.

Create
 Test Step

Creates a test step or multiple test steps on the server
 using the local reference configured with Initialize Test
 Step.

Delete Test
 Result

Removes a test result or array of test results from
 the server.

Delete Test
 Step

Removes a test step or an array of test steps from the
 server.

Generate Named
 Value

Converts the name of the
 type definition and data provided into a named value
 object, which represents the inputs and outputs of a test step.

Initialize Child Step from Step

Configures a reference to a
 new test step for a test step reference on the
 server.

Initialize Test
 Result

Configures a local reference to a new test
 result on the server.

Initialize Test
 Step

Configures a local
 reference to a test step on the server.

Initialize Test Step from Result

Configures a reference to a child test step for a test
 result reference on the server.

Read Named Value
 Data

Returns the name and
 value data from the named
 value object, which represents the inputs and outputs of a test
 step.

Update Test
 Result

Modifies a test result or multiple test results on
 the server to match all the properties of the object supplied.

Update Test
 Step

Modifies a test step or multiple test steps on the
 server.

Parent topic:

SystemLink VIs and Functions Reference for LabVIEW

<!--NI_TOPIC bundle=systemlink-api path=unregister-for-available-file-events.html language=enus -->
## TOPIC 00042: Unregister for Available File Events

- bundle_id: `systemlink-api`
- source_path: `unregister-for-available-file-events.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/unregister-for-available-file-events.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unsubscribes from the SystemLink file service to stop receiving available file events. available file event An event stating new files are available to upload or download. error in Error conditions that occur before this VI runs. Unlike most VIs, this VI runs normally even if an error occurred befor

### Unregister for Available File Events

Unsubscribes from the SystemLink file service to stop receiving available file events.

[IMAGE alt='image' src='GUID-D9C82F24-F2A6-4F32-BF1C-C0BD7FA3F2DF-a5.png']

#### available file event

An event stating new files are available to upload or download.

#### error in

Error conditions that occur before this VI runs. Unlike most VIs, this VI runs normally
 even if an error occurred before this VI runs.

#### error out

standard error behavior

Parent topic:

Advanced Functions

<!--NI_TOPIC bundle=systemlink-api path=update-test-step.html language=enus -->
## TOPIC 00043: Update Test Step

- bundle_id: `systemlink-api`
- source_path: `update-test-step.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/update-test-step.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Modifies a test step or multiple test steps on the server. Programming PatternsAcquiring Test Results test step in Test step reference on the server. status type Execution state the test is in. When you leave this input unwired, this VI uses the status associated with test step in. The default is Ru

### Update Test Step

Modifies a test step or multiple test steps on the
 server.

- Acquiring Test Results

[IMAGE alt='image' src='GUID-E76F869A-9A0D-4A73-B304-F83E32BF123A-a5.png']

#### test step in

Test step reference on the server.

#### status type

Execution state the test is in.

When you leave this input unwired, this VI
 uses the status associated with test step in. The
 default is Running.

#### status name

Name of the test execution state.

The name is used only when
 status type is set to Custom.

#### error in

standard error behavior

#### update result total
 time

Boolean that determines whether to replace the automatically calculated time it
 takes to complete the test result.

If you want to define the total time,
 wire True to this input.

The default is False.

#### test step out

Test step reference on the server.

#### error out

standard error behavior

Parent topic:

Test Monitor Functions

<!--NI_TOPIC bundle=systemlink-api path=use-workspace-instance.html language=enus -->
## TOPIC 00044: Use Workspace (Instance)

- bundle_id: `systemlink-api`
- source_path: `use-workspace-instance.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/use-workspace-instance.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies, by workspace instance, the workspace that any VI referencing this configuration uses to perform operations.The active workspace determines what resources the VI can access on the SystemLink server and where new resources are created. HTTP configuration in Configuration to communicate with

### Use Workspace (Instance)

Specifies, by workspace instance, the workspace that any VI referencing this
 configuration uses to perform operations.The active workspace determines
 what resources the VI can access on the SystemLink server and where new resources are
 created.

[IMAGE alt='image' src='GUID-05AC30E2-C57F-4A36-844B-07332653D176-a5.png']

#### HTTP configuration
 in

#### workspace

#### error in

standard error behavior

#### HTTP configuration out

#### error out

standard error behavior

Parent topic:

Use Workspace

<!--NI_TOPIC bundle=systemlink-api path=use-workspace-multimode-function.html language=enus -->
## TOPIC 00045: Use Workspace

- bundle_id: `systemlink-api`
- source_path: `use-workspace-multimode-function.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/use-workspace-multimode-function.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the active workspace nodes that reference this configuration use to perform operations. The active workspace determines what resources the node can access on the SystemLink server and where new resources are created.

### Use
 Workspace

Specifies the active workspace nodes that reference this configuration use to
 perform operations. The active workspace determines what resources the node can access
 on the SystemLink server and where new resources are created.

Configuration Functions

Manage the HTTP or HTTPS connection with your server.

Name

Specifies, by workspace name, the active workspace a node that references this configuration uses to perform operations.

Instance

Specifies, by workspace instance, the workspace that any node referencing this configuration uses to perform operations.

API Reference

G, HTTP, Python, and .NET APIs allow you to programmatically access SystemLink data services outside of NI SystemLink Web Application.

SystemLink Nodes and Functions Reference for NXG and G Web Development Software

Use SystemLink nodes in NXG or G Web Development Software to communicate data between your test and measurement systems and your SystemLink Server account.

Configuration Functions

Manage the HTTP or HTTPS connection with your server.

Parent topic:

Configuration Functions

<!--NI_TOPIC bundle=systemlink-api path=utilities-functions.html language=enus -->
## TOPIC 00046: Utilities Functions

- bundle_id: `systemlink-api`
- source_path: `utilities-functions.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/utilities-functions.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obtain system names and minion IDs to assign tag paths and properties to your data. Get Minion ID Obtains the minion ID of the Salt system, if one is available. Get System Name Obtains the name of the system, if one is available.

### Utilities Functions

Obtain system names and minion IDs to assign tag paths and properties to your data.

Get Minion ID

Obtains the minion ID of the Salt system, if one is available.

Get System Name

Obtains the name of the system, if one is available.

Parent topic:

SystemLink VIs and Functions Reference for LabVIEW

<!--NI_TOPIC bundle=systemlink-api path=utility-nodes.html language=enus -->
## TOPIC 00047: Utility Functions

- bundle_id: `systemlink-api`
- source_path: `utility-nodes.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/utility-nodes.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get information about systems connected to your server. G Web Development Software does not support this API.

### Utility
 Functions

Get information about systems connected to your server.

Note

SystemLink Nodes and Functions Reference for NXG and G Web Development Software

Use SystemLink nodes in NXG or G Web Development Software to communicate data between your test and measurement systems and your SystemLink Server account.

Get Minion ID

Obtains the minion ID of the Salt system, if one is available.

Get System Name

Obtains the name of the system, if one is available.

API Reference

G, HTTP, Python, and .NET APIs allow you to programmatically access SystemLink data services outside of NI SystemLink Web Application.

SystemLink Nodes and Functions Reference for NXG and G Web Development Software

Use SystemLink nodes in NXG or G Web Development Software to communicate data between your test and measurement systems and your SystemLink Server account.

Parent topic:

SystemLink Nodes and Functions Reference for NXG and G Web Development Software

<!--NI_TOPIC bundle=systemlink-api path=write-tag-i32.html language=enus -->
## TOPIC 00048: I32

- bundle_id: `systemlink-api`
- source_path: `write-tag-i32.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/write-tag-i32.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value of the tag. The data type of the tag must be a 32-bit integer. tag in Tag the server references to communicate measurement data. value Data value of the tag or tags. time stamp Date and time the server obtained the most recent data value. Leave the time stamp input empty to have

### I32

Specifies the value of the tag.

The data type of the tag must be a 32-bit integer.

[IMAGE alt='image' src='GUID-EFF16F72-BCA1-4B91-8B0D-1BE1D5D80A94-a5.png']

#### Inputs/Outputs

##### tag in

Tag the server references to communicate measurement data.

##### value

Data value of the tag or tags.

##### time stamp

Date and time the server obtained the most recent data value.

Leave the time stamp input empty to have the
 server manage the timestamp.

##### error in

Error conditions that occur before this node runs.

The node responds to this input
 according to standard error behavior.

Default value: No error

##### tag out

Tag the server references to communicate measurement data.

##### error out

Error information.

The node produces this output according to standard error
 behavior.

Parent topic:

Write Tag

Related information:

- Standard Error Behavior
- Transferring Data Using Tags

<!--NI_TOPIC bundle=systemlink-api path=write-tag-settings.html language=enus -->
## TOPIC 00049: Write Tag Settings

- bundle_id: `systemlink-api`
- source_path: `write-tag-settings.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/write-tag-settings.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the settings of a tag. The node replaces existing tag settings on the server with the new settings. A tag setting is a type of permission for the tag, such as read, write, modify, delete, and create. Based on the settings, a tag can complete any of the permissions an administrator specifie

### Write Tag Settings

Specifies the settings of a tag. The node replaces existing tag settings on the server with the new settings.

A tag setting is a type of permission for the tag, such as read, write, modify, delete,
 and create. Based on the settings, a tag can complete any of the permissions an
 administrator specifies.

[IMAGE alt='image' src='GUID-6FE7DA70-5D9B-4B57-B159-64E7E8865D3C-a5.png']

#### Inputs/Outputs

##### retention type

Aging policy which the tag server uses.

##### tag in

Tag the server references to communicate measurement data.

##### properties

Key-value pairs that exist as metadata on a tag.

##### keywords

Specific words provided to find tags.

##### error in

Error conditions that occur before this node runs.

The node responds to this input
 according to standard error behavior.

Default value: No error

##### collect aggregates?

Boolean that determines if the node collects aggregate tag data.

##### tag out

Tag the server references to communicate measurement data.

##### error out

Error information.

The node produces this output according to standard error
 behavior.

Parent topic:

Tag Functions

Related information:

- Standard Error Behavior

<!--NI_TOPIC bundle=systemlink-api path=write-tag-string.html language=enus -->
## TOPIC 00050: String

- bundle_id: `systemlink-api`
- source_path: `write-tag-string.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/write-tag-string.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value of the tag. The data type of the tag must be a string. tag in Tag the server references to communicate measurement data. value Data value of the tag or tags. time stamp Date and time the server obtained the most recent data value. Leave the time stamp input empty to have the serv

### String

Specifies the value of the tag.

The data type of the tag must be a string.

[IMAGE alt='image' src='GUID-7DF5AF06-0DB1-46F9-88CB-DD972B236C28-a5.png']

#### Inputs/Outputs

##### tag in

Tag the server references to communicate measurement data.

##### value

Data value of the tag or tags.

##### time stamp

Date and time the server obtained the most recent data value.

Leave the time stamp input empty to have the
 server manage the timestamp.

##### error in

Error conditions that occur before this node runs.

The node responds to this input
 according to standard error behavior.

Default value: No error

##### tag out

Tag the server references to communicate measurement data.

##### error out

Error information.

The node produces this output according to standard error
 behavior.

Parent topic:

Write Tag

Related information:

- Standard Error Behavior
- Transferring Data Using Tags

<!--NI_TOPIC bundle=systemlink-api path=write-tag-timestamp.html language=enus -->
## TOPIC 00051: Timestamp

- bundle_id: `systemlink-api`
- source_path: `write-tag-timestamp.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/write-tag-timestamp.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value of the tag. The data type of the tag must be a timestamp. tag in Tag the server references to communicate measurement data. value Data value of the tag or tags. time stamp Date and time the server obtained the most recent data value. Leave the time stamp input empty to have the s

### Timestamp

Specifies the value of the tag.

The data type of the tag must be a timestamp.

[IMAGE alt='image' src='GUID-F5D45472-7362-4A43-8209-6F116A5FBF6B-a5.png']

#### Inputs/Outputs

##### tag in

Tag the server references to communicate measurement data.

##### value

Data value of the tag or tags.

##### time stamp

Date and time the server obtained the most recent data value.

Leave the time stamp input empty to have the
 server manage the timestamp.

##### error in

Error conditions that occur before this node runs.

The node responds to this input
 according to standard error behavior.

Default value: No error

##### tag out

Tag the server references to communicate measurement data.

##### error out

Error information.

The node produces this output according to standard error
 behavior.

Parent topic:

Write Tag

Related information:

- Standard Error Behavior
- Transferring Data Using Tags

<!--NI_TOPIC bundle=systemlink-api path=write-tag-u64.html language=enus -->
## TOPIC 00052: U64

- bundle_id: `systemlink-api`
- source_path: `write-tag-u64.html`
- source_url: https://docs-be.ni.com/bundle/systemlink-api/raw/resource/enus/write-tag-u64.html
- document_id: `systemlink-api`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value of the tag. The data type of the tag must be an unsigned 64-bit integer. tag in Tag the server references to communicate measurement data. value Data value of the tag or tags. time stamp Date and time the server obtained the most recent data value. Leave the time stamp input empt

### U64

Specifies the value of the tag.
 
 The data type of the tag must be an unsigned 64-bit integer.

[IMAGE alt='image' src='GUID-DCDF0EEE-FE45-43F1-B24A-1F145345F352-a5.png']

#### Inputs/Outputs

##### tag in

Tag the server references to communicate measurement data.

##### value

Data value of the tag or tags.

##### time stamp

Date and time the server obtained the most recent data value.

Leave the time stamp input empty to have the
 server manage the timestamp.

##### error in

Error conditions that occur before this node runs.

The node responds to this input
 according to standard error behavior. For more information, refer to *Standard Error
 Behavior*.

Default value: No error

##### error out

Error information.

The node produces this output according to standard error
 behavior. For more information, refer to *Standard Error Behavior*.

##### tag out

Tag the server references to communicate measurement data.

Parent topic:

Write Tag

Related information:

- Standard Error Behavior
- Transferring Data Using Tags
