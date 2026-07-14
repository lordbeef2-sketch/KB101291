# NI DOCUMENT BUNDLE: veristand-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=veristand-labview-api-ref start=251 end=445 -->
<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/get-data-logging-session-state-vi.html language=enus -->
## TOPIC 00251: Get Data Logging Session State VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/get-data-logging-session-state-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/get-data-logging-session-state-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the current state of the data logging specification specified by Session Name in. icon Inputs/Outputs cgnrn.png Data Logging Manager Ref in Data Logging Manager Ref in is the reference to the data logging service on the VeriStand Gateway. cstr.png Session Name in Session Name in specifies the n

### Get Data Logging Session State VI

Gets the current state of the data logging specification specified by **Session Name in**.

[IMAGE alt='icon' src='get-data-logging-session-state-vi.png']

#### Inputs/Outputs

| Data Logging Manager Ref in — Data Logging Manager Ref in is the reference to the data logging service on the VeriStand Gateway. Session Name in — Session Name in specifies the name of the current data logging session. You use this name to query and control logging operations during the logging session. To avoid overwriting data, use unique session names for each data logging session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Data Logging Manager Ref out — Data Logging Manager Ref out returns the reference to the data logging service. Session Name out — Session Name out returns the name of the current data logging session. Session State — Session State returns the current state of the data logging session. 0 Waiting on Trigger—The session is waiting on a start trigger. 1 Triggered—The start trigger has occurred and the session is logging data and waiting on the stop trigger. 2 Post-Trigger—The stop trigger has occurred and the session is logging post-trigger data. 3 Complete—Logging is complete. This session will not create any more log files. 4 Idle—The session is idle. 5 Error—The session encountered an error. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | Waiting on Trigger—The session is waiting on a start trigger. |
| 1 | Triggered—The start trigger has occurred and the session is logging data and waiting on the stop trigger. |
| 2 | Post-Trigger—The stop trigger has occurred and the session is logging post-trigger data. |
| 3 | Complete—Logging is complete. This session will not create any more log files. |
| 4 | Idle—The session is idle. |
| 5 | Error—The session encountered an error. |

Parent topic:

Status

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/get-last-error-vi.html language=unavailable -->
## TOPIC 00252: Get Last Error Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/get-last-error-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/get-last-error-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/new-data-logging-specification-tdms-vi.html language=enus -->
## TOPIC 00253: New Data Logging Specification (TDMS) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/new-data-logging-specification-tdms-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/new-data-logging-specification-tdms-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new data logging specification, which defines the channels to log and the type and base path for log files. You can log data to TDMS or text (.txt) files. You must manually select the polymorphic instance to use. icon Inputs/Outputs c1dcclst.png File Properties File Properties specifies th

### New Data Logging Specification (TDMS) VI

Creates a new data logging specification, which defines the channels to log and the type and base path for log files. You can log data to TDMS or text (.txt) files. You must manually select the polymorphic instance to use.

[IMAGE alt='icon' src='new-data-logging-specification-tdms-vi.png']

#### Inputs/Outputs

| File Properties — File Properties specifies the property names and values, or meta-data, of the TDMS file. Name — Name specifies the name of the TDMS property. Value — Value specifies the value of the TDMS property. This input accepts the following data types: •Signed or unsigned integer •Single, double, or extended precision numeric •Alphanumeric string that does not contain null characters •Timestamp •Boolean •Variant that contains any of the data types specified above File Description — File Description specifies a description for the TDMS file. Base Log File Path — Base Log File Path specifies the base path for the log file(s). File Conflict Operation — File Conflict Operation specifies the action to take if a file already exists at the Log File Path. 0 Create Unique—Creates a unique filename by appending an incrementing number to the end of the name until no conflicting name exists. 1 Append to Existing—Appends data to the existing file. NI VeriStand logs new data for existing channels under the existing channel and group names, and the file only shows the initial creation date in the file header. The TDMS file does not retain the timestamps of subsequent logging operations that append data to an existing file. 2 Overwrite—Overwrites the existing file. Channel Groups — Channel Groups specifies the groups and channels for which to log data. Group Name — Group Name specifies the name of the channel group. Group Description — Group Description specifies a description for the channel group. Group Properties — Group Properties specifies the properties of the channel group. Name — Name specifies the name of the TDMS property. Value — Value specifies the value of the TDMS property. This input accepts the following data types: •Signed or unsigned integer •Single, double, or extended precision numeric •Alphanumeric string that does not contain null characters •Timestamp •Boolean •Variant that contains any of the data types specified above Channels — Channels specifies the channels that belong to the channel group. Channel Name — Channel Name specifies a name for the channel. The default is the name of the channel at Channel Path, but you can specify a custom name. Channel Path — Channel Path specifies the path to the channel in the system definition file. For example: Targets/Controller/System Channels/Absolute Time Channel Description — Channel Description specifies a description for the channel. Channel Properties — Channel Properties specifies the properties of the channel. Name — Name specifies the name of the TDMS property. Value — Value specifies the value of the TDMS property. This input accepts the following data types: •Signed or unsigned integer •Single, double, or extended precision numeric •Alphanumeric string that does not contain null characters •Timestamp •Boolean •Variant that contains any of the data types specified above Time Channel Options — Time Channel Options specifies options for automatically including a time channel at the beginning of the channel group Time Channel Name — Time Channel Name gets or sets a value indicating the name of the time channel in the channel group. This property is ignored if TimeChannelOptions is set to NoTimeChannel. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Apply Root Properties to Groups — Data Logging Specification Ref out — Data Logging Specification Ref out returns the reference to the data logging specification. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Name — Name specifies the name of the TDMS property. Value — Value specifies the value of the TDMS property. This input accepts the following data types: •Signed or unsigned integer •Single, double, or extended precision numeric •Alphanumeric string that does not contain null characters •Timestamp •Boolean •Variant that contains any of the data types specified above |  |
| 0 | Create Unique—Creates a unique filename by appending an incrementing number to the end of the name until no conflicting name exists. |
| 1 | Append to Existing—Appends data to the existing file. NI VeriStand logs new data for existing channels under the existing channel and group names, and the file only shows the initial creation date in the file header. The TDMS file does not retain the timestamps of subsequent logging operations that append data to an existing file. |
| 2 | Overwrite—Overwrites the existing file. |
| Group Name — Group Name specifies the name of the channel group. Group Description — Group Description specifies a description for the channel group. Group Properties — Group Properties specifies the properties of the channel group. Name — Name specifies the name of the TDMS property. Value — Value specifies the value of the TDMS property. This input accepts the following data types: •Signed or unsigned integer •Single, double, or extended precision numeric •Alphanumeric string that does not contain null characters •Timestamp •Boolean •Variant that contains any of the data types specified above Channels — Channels specifies the channels that belong to the channel group. Channel Name — Channel Name specifies a name for the channel. The default is the name of the channel at Channel Path, but you can specify a custom name. Channel Path — Channel Path specifies the path to the channel in the system definition file. For example: Targets/Controller/System Channels/Absolute Time Channel Description — Channel Description specifies a description for the channel. Channel Properties — Channel Properties specifies the properties of the channel. Name — Name specifies the name of the TDMS property. Value — Value specifies the value of the TDMS property. This input accepts the following data types: •Signed or unsigned integer •Single, double, or extended precision numeric •Alphanumeric string that does not contain null characters •Timestamp •Boolean •Variant that contains any of the data types specified above Time Channel Options — Time Channel Options specifies options for automatically including a time channel at the beginning of the channel group Time Channel Name — Time Channel Name gets or sets a value indicating the name of the time channel in the channel group. This property is ignored if TimeChannelOptions is set to NoTimeChannel. |  |
| Name — Name specifies the name of the TDMS property. Value — Value specifies the value of the TDMS property. This input accepts the following data types: •Signed or unsigned integer •Single, double, or extended precision numeric •Alphanumeric string that does not contain null characters •Timestamp •Boolean •Variant that contains any of the data types specified above |  |
| Channel Name — Channel Name specifies a name for the channel. The default is the name of the channel at Channel Path, but you can specify a custom name. Channel Path — Channel Path specifies the path to the channel in the system definition file. For example: Targets/Controller/System Channels/Absolute Time Channel Description — Channel Description specifies a description for the channel. Channel Properties — Channel Properties specifies the properties of the channel. Name — Name specifies the name of the TDMS property. Value — Value specifies the value of the TDMS property. This input accepts the following data types: •Signed or unsigned integer •Single, double, or extended precision numeric •Alphanumeric string that does not contain null characters •Timestamp •Boolean •Variant that contains any of the data types specified above |  |
| Name — Name specifies the name of the TDMS property. Value — Value specifies the value of the TDMS property. This input accepts the following data types: •Signed or unsigned integer •Single, double, or extended precision numeric •Alphanumeric string that does not contain null characters •Timestamp •Boolean •Variant that contains any of the data types specified above |  |

Parent topic:

New Data Logging Specification VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/new-data-logging-specification-text-vi.html language=enus -->
## TOPIC 00254: New Data Logging Specification (Text) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/new-data-logging-specification-text-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/new-data-logging-specification-text-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new data logging specification, which defines the channels to log and the type and base path for log files. You can log data to TDMS or text (.txt) files. You must manually select the polymorphic instance to use. icon Inputs/Outputs cu32.png Decimal Places (3) Decimal Places specifies the

### New Data Logging Specification (Text) VI

Creates a new data logging specification, which defines the channels to log and the type and base path for log files. You can log data to TDMS or text (.txt) files. You must manually select the polymorphic instance to use.

[IMAGE alt='icon' src='new-data-logging-specification-text-vi.png']

#### Inputs/Outputs

| Decimal Places (3) — Decimal Places specifies the number of decimal places to use when converting numeric log data to a string. The default is 3. Delimiter (Tab) — Delimiter specifies the delimiter to use to separate columns in the text file. 0 Tab (default)―Separates columns with a tab. 1 Comma―Separates columns with a comma. Base Log File Path — Base Log File Path specifies the base path for the log file(s). File Conflict Operation — File Conflict Operation specifies the action to take if a file already exists at the Log File Path. 0 Create Unique—Creates a unique filename by appending an incrementing number to the end of the name until no conflicting name exists. 1 Append to Existing—Appends data to the existing file. NI VeriStand logs new data for existing channels under the existing channel and group names, and the file only shows the initial creation date in the file header. The TDMS file does not retain the timestamps of subsequent logging operations that append data to an existing file. 2 Overwrite—Overwrites the existing file. Channel Paths — Channel Paths specifies the channels for which to log data. Channel Name — Channel Name specifies a name for the channel. The default is the name of the channel at Channel Path, but you can specify a custom name. Channel Path — Channel Path specifies the path to the channel in the system definition file. For example: Targets/Controller/System Channels/Absolute Time. Include Channel Units in Name — Include Channel Units in Name specifies whether or not to add the units of the channel specified in Channel Path to Channel Name. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Header Text ("") — Header Text specifies text to display as the header of the text file. The default is an empty string, or no header. Data Logging Specification Ref out — Data Logging Specification Ref out returns the reference to the data logging specification. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | Tab (default)―Separates columns with a tab. |
| 1 | Comma―Separates columns with a comma. |
| 0 | Create Unique—Creates a unique filename by appending an incrementing number to the end of the name until no conflicting name exists. |
| 1 | Append to Existing—Appends data to the existing file. NI VeriStand logs new data for existing channels under the existing channel and group names, and the file only shows the initial creation date in the file header. The TDMS file does not retain the timestamps of subsequent logging operations that append data to an existing file. |
| 2 | Overwrite—Overwrites the existing file. |
| Channel Name — Channel Name specifies a name for the channel. The default is the name of the channel at Channel Path, but you can specify a custom name. Channel Path — Channel Path specifies the path to the channel in the system definition file. For example: Targets/Controller/System Channels/Absolute Time. Include Channel Units in Name — Include Channel Units in Name specifies whether or not to add the units of the channel specified in Channel Path to Channel Name. |  |

Parent topic:

New Data Logging Specification VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/new-data-logging-specification-vi.html language=enus -->
## TOPIC 00255: New Data Logging Specification VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/new-data-logging-specification-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/new-data-logging-specification-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new data logging specification, which defines the channels to log and the type and base path for log files. You can log data to TDMS or text (.txt) files. You must manually select the polymorphic instance to use. icon

### New Data Logging Specification VI

Creates a new data logging specification, which defines the channels to log and the type and base path for log files. You can log data to TDMS or text (.txt) files. You must manually select the polymorphic instance to use.

[IMAGE alt='icon' src='new-data-logging-specification-vi.png']

- [New Data Logging Specification (TDMS) VI](../../../../vi-lib/ni-veristand/execution/datalogging/new-data-logging-specification-tdms-vi.html) Creates a new data logging specification, which defines the channels to log and the type and base path for log files. You can log data to TDMS or text (.txt) files. You must manually select the polymorphic instance to use.
- [New Data Logging Specification (Text) VI](../../../../vi-lib/ni-veristand/execution/datalogging/new-data-logging-specification-text-vi.html) Creates a new data logging specification, which defines the channels to log and the type and base path for log files. You can log data to TDMS or text (.txt) files. You must manually select the polymorphic instance to use.

Parent topic:

Configuration

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/open-data-logging-manager-reference-vi.html language=unavailable -->
## TOPIC 00256: Open Data Logging Manager Reference Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/open-data-logging-manager-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/open-data-logging-manager-reference-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/register-data-logging-events-vi.html language=enus -->
## TOPIC 00257: Register Data Logging Events VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/register-data-logging-events-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/register-data-logging-events-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Registers for data logging events from the VeriStand Gateway. This VI returns a registered user event reference and information about the event. icon Inputs/Outputs cgnrn.png Data Logging Manager Ref in Data Logging Manager Ref in is the reference to the data logging service on the VeriStand Gateway

### Register Data Logging Events VI

Registers for data logging events from the VeriStand Gateway. This VI returns a registered user event reference and information about the event.

[IMAGE alt='icon' src='register-data-logging-events-vi.png']

#### Inputs/Outputs

| Data Logging Manager Ref in — Data Logging Manager Ref in is the reference to the data logging service on the VeriStand Gateway. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Registered Data Logging Event Refnum — Registered Data Logging Event Refnum contains information about the data logging event. Callback Refnum — Callback Refnum is a reference to the Register Event Callback. User Events — User Events is a reference to the Data Logging User Events. Error Event — Error Event is a reference to DataLoggingSessionError User Event, invoked when a data logging session produces an error. Start Event — Start Event is a reference to DataLoggingSession Start User Event, invoked when a new data logging session starts. State Change Event — State Change Event is a reference to DataLoggingSessionStateChange User Event, invoked when a data logging session changes state. Stop Event — Stop Event is a reference to the DataLoggingSessionStop User Event,invoked when a data logging session stops. File Closed Event — File Closed Event is a reference to the LogFileClosed User Event, invoked when a data logging session on the host computer closes a log file. File Opened Event — File Opened Event is a reference to the LogFileOpened User Event, invoked when a data logging session on the host computer opens a log file. New File Complete — New File Complete is a reference to NewLogFilesComplete User Event, invoked when a target generates a new log file. Features that perform logging on a target rather than the host, such as DAQ tasks and XNET raw frame data logging, generate this event. Event Refnum — Event Refnum is a reference to Waveform Data User Event Registration. Data Logging Manager Ref out — Data Logging Manager Ref out returns the reference to the data logging service. error out — error out contains error information. This output provides standard error out functionality. Log Event Registration Refnum — Log Event Registration Refnum returns the reference to a new or existing event registration. |
| --- |
| Callback Refnum — Callback Refnum is a reference to the Register Event Callback. User Events — User Events is a reference to the Data Logging User Events. Error Event — Error Event is a reference to DataLoggingSessionError User Event, invoked when a data logging session produces an error. Start Event — Start Event is a reference to DataLoggingSession Start User Event, invoked when a new data logging session starts. State Change Event — State Change Event is a reference to DataLoggingSessionStateChange User Event, invoked when a data logging session changes state. Stop Event — Stop Event is a reference to the DataLoggingSessionStop User Event,invoked when a data logging session stops. File Closed Event — File Closed Event is a reference to the LogFileClosed User Event, invoked when a data logging session on the host computer closes a log file. File Opened Event — File Opened Event is a reference to the LogFileOpened User Event, invoked when a data logging session on the host computer opens a log file. New File Complete — New File Complete is a reference to NewLogFilesComplete User Event, invoked when a target generates a new log file. Features that perform logging on a target rather than the host, such as DAQ tasks and XNET raw frame data logging, generate this event. Event Refnum — Event Refnum is a reference to Waveform Data User Event Registration. |
| Error Event — Error Event is a reference to DataLoggingSessionError User Event, invoked when a data logging session produces an error. Start Event — Start Event is a reference to DataLoggingSession Start User Event, invoked when a new data logging session starts. State Change Event — State Change Event is a reference to DataLoggingSessionStateChange User Event, invoked when a data logging session changes state. Stop Event — Stop Event is a reference to the DataLoggingSessionStop User Event,invoked when a data logging session stops. File Closed Event — File Closed Event is a reference to the LogFileClosed User Event, invoked when a data logging session on the host computer closes a log file. File Opened Event — File Opened Event is a reference to the LogFileOpened User Event, invoked when a data logging session on the host computer opens a log file. New File Complete — New File Complete is a reference to NewLogFilesComplete User Event, invoked when a target generates a new log file. Features that perform logging on a target rather than the host, such as DAQ tasks and XNET raw frame data logging, generate this event. |

Parent topic:

Events

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/set-completed-file-attributes-vi.html language=unavailable -->
## TOPIC 00258: Set Completed File Attributes Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/set-completed-file-attributes-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/set-completed-file-attributes-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/set-data-logging-rate-custom-rate-vi.html language=enus -->
## TOPIC 00259: Set Data Logging Rate (Custom Rate) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/set-data-logging-rate-custom-rate-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/set-data-logging-rate-custom-rate-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the rate at which to log data, in hertz. You can log at the rate at which the target produces data, or a custom rate. You must manually select the polymorphic instance to use. icon Inputs/Outputs cgnrn.png Data Logging Specification Ref in Data Logging Specification Ref in specifies the re

### Set Data Logging Rate (Custom Rate) VI

Specifies the rate at which to log data, in hertz. You can log at the rate at which the target produces data, or a custom rate. You must manually select the polymorphic instance to use.

[IMAGE alt='icon' src='set-data-logging-rate-custom-rate-vi.png']

#### Inputs/Outputs

| Data Logging Specification Ref in — Data Logging Specification Ref in specifies the reference to the data logging specification. You can use the New Data Logging Specification VI to create this reference. Custom Rate (Hz) — Custom Rate specifies the rate, in hertz, at which to log data. You cannot log data at a faster rate than the target produces data. The actual rate this VI uses might be coerced to an even divisor of the rates at which the target(s) produce data. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Data Logging Specification Ref out — Data Logging Specification Ref out returns the reference to the data logging specification. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Set Data Logging Rate VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/set-data-logging-rate-target-rate-vi.html language=unavailable -->
## TOPIC 00260: Set Data Logging Rate Target Rate Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/set-data-logging-rate-target-rate-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/set-data-logging-rate-target-rate-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/set-data-logging-rate-vi.html language=enus -->
## TOPIC 00261: Set Data Logging Rate VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/set-data-logging-rate-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/set-data-logging-rate-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the rate at which to log data, in hertz. You can log at the rate at which the target produces data, or a custom rate. You must manually select the polymorphic instance to use. icon

### Set Data Logging Rate VI

Specifies the rate at which to log data, in hertz. You can log at the rate at which the target produces data, or a custom rate. You must manually select the polymorphic instance to use.

[IMAGE alt='icon' src='set-data-logging-rate-vi.png']

- [Set Data Logging Rate (Target Rate) VI](../../../../vi-lib/ni-veristand/execution/datalogging/set-data-logging-rate-target-rate-vi.html) Specifies the rate at which to log data, in hertz. You can log at the rate at which the target produces data, or a custom rate. You must manually select the polymorphic instance to use.
- [Set Data Logging Rate (Custom Rate) VI](../../../../vi-lib/ni-veristand/execution/datalogging/set-data-logging-rate-custom-rate-vi.html) Specifies the rate at which to log data, in hertz. You can log at the rate at which the target produces data, or a custom rate. You must manually select the polymorphic instance to use.

Parent topic:

Configuration

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/set-minimum-buffer-size-vi.html language=enus -->
## TOPIC 00262: Set Minimum Buffer Size VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/set-minimum-buffer-size-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/set-minimum-buffer-size-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the minimum size of the buffer for logged data. Increasing the minimum buffer size can improve logging performance but requires additional memory resources. Decreasing the minimum buffer size can result in much larger TDMS and TDMS index files. Consider setting the minimum buffer size to at lea

### Set Minimum Buffer Size VI

Sets the minimum size of the buffer for logged data. Increasing the minimum buffer size can improve logging performance but requires additional memory resources. Decreasing the minimum buffer size can result in much larger TDMS and TDMS index files. Consider setting the minimum buffer size to at least 256 when logging data to TDMS files at high rates.

[IMAGE alt='icon' src='set-minimum-buffer-size-vi.png']

#### Inputs/Outputs

| Data Logging Specification Ref in — Data Logging Specification Ref in specifies the reference to the data logging specification. You can use the New Data Logging Specification VI to create this reference. Minimum Buffer Size — Minimum Buffer Size specifies the minimum size of the buffer, in bytes. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Data Logging Specification Ref out — Data Logging Specification Ref out returns the reference to the data logging specification. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/set-segmenting-specification-default-vi.html language=enus -->
## TOPIC 00263: Set Segmenting Specification (Default) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/set-segmenting-specification-default-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/set-segmenting-specification-default-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how to segment the log files created during the data logging session. You can segment log files according to time or size limits, or when a start trigger occurs. When the segmenting condition is met, this VI saves and closes the current log file and continues logging data in a new file. Se

### Set Segmenting Specification (Default) VI

Specifies how to segment the log files created during the data logging session. You can segment log files according to time or size limits, or when a start trigger occurs. When the segmenting condition is met, this VI saves and closes the current log file and continues logging data in a new file.

Select the Default instance of this VI if you do not want to segment log files based on time or size, but do want the option to segment on a start trigger.

You must manually select the polymorphic instance to use.

[IMAGE alt='icon' src='set-segmenting-specification-default-vi.png']

#### Inputs/Outputs

| Segment File on Trigger (T) — Segment File on Trigger specifies whether to create a new log file when a new start trigger occurs. If TRUE, a start trigger takes precedence over any configured footprint or time segmenting. This means that if a new start trigger occurs, the segment containing the data immediately preceding the start trigger might be smaller than other segments. The default is TRUE, segment on start trigger. Max Instances (-1: Infinite) — Max Instances specifies the maximum number of total log files to create through file segmenting. The default is -1, which specifies an infinite number of instances. Data Logging Specification Ref in — Data Logging Specification Ref in specifies the reference to the data logging specification. You can use the New Data Logging Specification VI to create this reference. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Data Logging Specification Ref out — Data Logging Specification Ref out returns the reference to the data logging specification. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Set Segmenting Specification VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/set-segmenting-specification-footprint-vi.html language=enus -->
## TOPIC 00264: Set Segmenting Specification (Footprint) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/set-segmenting-specification-footprint-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/set-segmenting-specification-footprint-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how to segment the log files created during the data logging session. You can segment log files according to time or size limits, or when a start trigger occurs. When the segmenting condition is met, this VI saves and closes the current log file and continues logging data in a new file. Se

### Set Segmenting Specification (Footprint) VI

Specifies how to segment the log files created during the data logging session. You can segment log files according to time or size limits, or when a start trigger occurs. When the segmenting condition is met, this VI saves and closes the current log file and continues logging data in a new file.

Select the Default instance of this VI if you do not want to segment log files based on time or size, but do want the option to segment on a start trigger.

You must manually select the polymorphic instance to use.

Note

[IMAGE alt='icon' src='set-segmenting-specification-footprint-vi.png']

#### Inputs/Outputs

| Segment File on Trigger (T) — Segment File on Trigger specifies whether to create a new log file when a new start trigger occurs. If TRUE, a start trigger takes precedence over any configured footprint or time segmenting. This means that if a new start trigger occurs, the segment containing the data immediately preceding the start trigger might be smaller than other segments. The default is TRUE, segment on start trigger. Max Instances (-1: Infinite) — Max Instances specifies the maximum number of total log files to create through file segmenting. The default is -1, which specifies an infinite number of instances. Data Logging Specification Ref in — Data Logging Specification Ref in specifies the reference to the data logging specification. You can use the New Data Logging Specification VI to create this reference. Size — Size specifies the size in bytes at which to segment a log file. The actual size of the segmented files might vary based on the Size Check Period you specify. Size Check Period (1000 ms) — Size Check Period specifies the period, in milliseconds, at which to periodically check if the log file has met the specified segmenting Size. The default is 1000 ms, or every second. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Data Logging Specification Ref out — Data Logging Specification Ref out returns the reference to the data logging specification. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Set Segmenting Specification VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/set-segmenting-specification-time-vi.html language=unavailable -->
## TOPIC 00265: Set Segmenting Specification Time Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/set-segmenting-specification-time-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/set-segmenting-specification-time-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/set-segmenting-specification-vi.html language=enus -->
## TOPIC 00266: Set Segmenting Specification VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/set-segmenting-specification-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/set-segmenting-specification-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how to segment the log files created during the data logging session. You can segment log files according to time or size limits, or when a start trigger occurs. When the segmenting condition is met, this VI saves and closes the current log file and continues logging data in a new file. Se

### Set Segmenting Specification VI

Specifies how to segment the log files created during the data logging session. You can segment log files according to time or size limits, or when a start trigger occurs. When the segmenting condition is met, this VI saves and closes the current log file and continues logging data in a new file.

Select the Default instance of this VI if you do not want to segment log files based on time or size, but do want the option to segment on a start trigger.

You must manually select the polymorphic instance to use.

[IMAGE alt='icon' src='set-segmenting-specification-vi.png']

- [Set Segmenting Specification (Default) VI](../../../../vi-lib/ni-veristand/execution/datalogging/set-segmenting-specification-default-vi.html) Specifies how to segment the log files created during the data logging session. You can segment log files according to time or size limits, or when a start trigger occurs. When the segmenting condition is met, this VI saves and closes the current log file and continues logging data in a new file. Select the Default instance of this VI if you do not want to segment log files based on time or size, but do want the option to segment on a start trigger. You must manually select the polymorphic instance to use.
- [Set Segmenting Specification (Footprint) VI](../../../../vi-lib/ni-veristand/execution/datalogging/set-segmenting-specification-footprint-vi.html) Specifies how to segment the log files created during the data logging session. You can segment log files according to time or size limits, or when a start trigger occurs. When the segmenting condition is met, this VI saves and closes the current log file and continues logging data in a new file. Select the Default instance of this VI if you do not want to segment log files based on time or size, but do want the option to segment on a start trigger. You must manually select the polymorphic instance to use.
- [Set Segmenting Specification (Time) VI](../../../../vi-lib/ni-veristand/execution/datalogging/set-segmenting-specification-time-vi.html) Specifies how to segment the log files created during the data logging session. You can segment log files according to time or size limits, or when a start trigger occurs. When the segmenting condition is met, this VI saves and closes the current log file and continues logging data in a new file. Select the Default instance of this VI if you do not want to segment log files based on time or size, but do want the option to segment on a start trigger. You must manually select the polymorphic instance to use.

Parent topic:

Configuration

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/set-start-trigger-analog-edge-vi.html language=enus -->
## TOPIC 00267: Set Start Trigger (Analog Edge) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/set-start-trigger-analog-edge-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/set-start-trigger-analog-edge-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a trigger condition on which to start logging data. You also can specify whether to log channel data immediately preceding the trigger condition and whether logging is retriggerable, meaning the data logging session watches for subsequent occurrences of the start trigger after the first lo

### Set Start Trigger (Analog Edge) VI

Specifies a trigger condition on which to start logging data. You also can specify whether to log channel data immediately preceding the trigger condition and whether logging is retriggerable, meaning the data logging session watches for subsequent occurrences of the start trigger after the first logging operation finishes. By default, logging stops after one operation.

You must manually select the polymorphic instance to use.

[IMAGE alt='icon' src='set-start-trigger-analog-edge-vi.png']

#### Inputs/Outputs

| Retriggerable (F) — Retriggerable specifies whether the current data logging session watches for subsequent start triggers, and logs additional data, after the data logging operation triggered by the first occurrence of the start trigger completes. The default is FALSE, logging is not retriggerable. Pre-Trigger Duration (0 s) — Pre-Trigger Duration specifies a number of seconds of data to retain in the buffer in case a start trigger occurs. When the start trigger occurs, any buffered data is included in the log file. Data Logging Specification Ref in — Data Logging Specification Ref in specifies the reference to the data logging specification. You can use the New Data Logging Specification VI to create this reference. Analog Edge Condition — Analog Edge Condition defines the analog edge condition that Trigger Channel must meet to generate a trigger. Threshold — Threshold specifies the value that Trigger Channel must cross to meet the condition. Slope — Slope specifies the slope or edge on which Trigger Channel must cross the Threshold value to meet the condition. 0 Rising (default)—The crossing must occur on a rising edge, or a positive slope. 1 Falling—The crossing must occur on a falling edge, or a negative slope. Strict Edge — Strict Edge specifies whether the value of Trigger Channel must strictly pass above or below the Threshold. If TRUE, the channel must pass beyond the Threshold in the direction of Slope. If FALSE, the channel value must only equal the threshold to meet the condition. Trigger Channel — Trigger Channel specifies the channel to watch for the trigger condition. Enter the path to the channel in the system definition file. For example: Targets/Controller/System Channels/Absolute Time error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Data Logging Specification Ref out — Data Logging Specification Ref out returns the reference to the data logging specification. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Threshold — Threshold specifies the value that Trigger Channel must cross to meet the condition. Slope — Slope specifies the slope or edge on which Trigger Channel must cross the Threshold value to meet the condition. 0 Rising (default)—The crossing must occur on a rising edge, or a positive slope. 1 Falling—The crossing must occur on a falling edge, or a negative slope. Strict Edge — Strict Edge specifies whether the value of Trigger Channel must strictly pass above or below the Threshold. If TRUE, the channel must pass beyond the Threshold in the direction of Slope. If FALSE, the channel value must only equal the threshold to meet the condition. |  |
| 0 | Rising (default)—The crossing must occur on a rising edge, or a positive slope. |
| 1 | Falling—The crossing must occur on a falling edge, or a negative slope. |

Parent topic:

Set Start Trigger VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/set-start-trigger-digital-edge-vi.html language=enus -->
## TOPIC 00268: Set Start Trigger (Digital Edge) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/set-start-trigger-digital-edge-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/set-start-trigger-digital-edge-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a trigger condition on which to start logging data. You also can specify whether to log channel data immediately preceding the trigger condition and whether logging is retriggerable, meaning the data logging session watches for subsequent occurrences of the start trigger after the first lo

### Set Start Trigger (Digital Edge) VI

Specifies a trigger condition on which to start logging data. You also can specify whether to log channel data immediately preceding the trigger condition and whether logging is retriggerable, meaning the data logging session watches for subsequent occurrences of the start trigger after the first logging operation finishes. By default, logging stops after one operation.

You must manually select the polymorphic instance to use.

Note

Trigger Channel

Slope

[IMAGE alt='icon' src='set-start-trigger-digital-edge-vi.png']

#### Inputs/Outputs

| Retriggerable (F) — Retriggerable specifies whether the current data logging session watches for subsequent start triggers, and logs additional data, after the data logging operation triggered by the first occurrence of the start trigger completes. The default is FALSE, logging is not retriggerable. Pre-Trigger Duration (0 s) — Pre-Trigger Duration specifies a number of seconds of data to retain in the buffer in case a start trigger occurs. When the start trigger occurs, any buffered data is included in the log file. Data Logging Specification Ref in — Data Logging Specification Ref in specifies the reference to the data logging specification. You can use the New Data Logging Specification VI to create this reference. Slope — Slope specifies whether Trigger Channel must start rising or falling to generate a trigger. 0 Rising (default)—Generates a trigger on a rising edge, or a positive slope. 1 Falling—Generates a trigger on a falling edge, or a negative slope. Trigger Channel — Trigger Channel specifies the channel to watch for the trigger condition. Enter the path to the channel in the system definition file. For example: Targets/Controller/System Channels/Absolute Time error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Data Logging Specification Ref out — Data Logging Specification Ref out returns the reference to the data logging specification. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | Rising (default)—Generates a trigger on a rising edge, or a positive slope. |
| 1 | Falling—Generates a trigger on a falling edge, or a negative slope. |

Parent topic:

Set Start Trigger VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/set-start-trigger-formula-vi.html language=unavailable -->
## TOPIC 00269: Set Start Trigger Formula Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/set-start-trigger-formula-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/set-start-trigger-formula-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/set-start-trigger-in-range-vi.html language=unavailable -->
## TOPIC 00270: Set Start Trigger In Range Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/set-start-trigger-in-range-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/set-start-trigger-in-range-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/set-start-trigger-start-immediately-vi.html language=unavailable -->
## TOPIC 00271: Set Start Trigger Start Immediately Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/set-start-trigger-start-immediately-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/set-start-trigger-start-immediately-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/set-start-trigger-value-change-vi.html language=unavailable -->
## TOPIC 00272: Set Start Trigger Value Change Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/set-start-trigger-value-change-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/set-start-trigger-value-change-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/set-start-trigger-vi.html language=enus -->
## TOPIC 00273: Set Start Trigger VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/set-start-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/set-start-trigger-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a trigger condition on which to start logging data. You also can specify whether to log channel data immediately preceding the trigger condition and whether logging is retriggerable, meaning the data logging session watches for subsequent occurrences of the start trigger after the first lo

### Set Start Trigger VI

Specifies a trigger condition on which to start logging data. You also can specify whether to log channel data immediately preceding the trigger condition and whether logging is retriggerable, meaning the data logging session watches for subsequent occurrences of the start trigger after the first logging operation finishes. By default, logging stops after one operation.

You must manually select the polymorphic instance to use.

[IMAGE alt='icon' src='set-start-trigger-vi.png']

- [Set Start Trigger (Analog Edge) VI](../../../../vi-lib/ni-veristand/execution/datalogging/set-start-trigger-analog-edge-vi.html) Specifies a trigger condition on which to start logging data. You also can specify whether to log channel data immediately preceding the trigger condition and whether logging is retriggerable, meaning the data logging session watches for subsequent occurrences of the start trigger after the first logging operation finishes. By default, logging stops after one operation. You must manually select the polymorphic instance to use.
- [Set Start Trigger (Digital Edge) VI](../../../../vi-lib/ni-veristand/execution/datalogging/set-start-trigger-digital-edge-vi.html) Specifies a trigger condition on which to start logging data. You also can specify whether to log channel data immediately preceding the trigger condition and whether logging is retriggerable, meaning the data logging session watches for subsequent occurrences of the start trigger after the first logging operation finishes. By default, logging stops after one operation. You must manually select the polymorphic instance to use.
- [Set Start Trigger (Formula) VI](../../../../vi-lib/ni-veristand/execution/datalogging/set-start-trigger-formula-vi.html) Specifies a trigger condition on which to stop logging data. You also can specify whether to continue logging channel data for a set period of time after the trigger condition occurs. You must manually select the polymorphic instance to use.
- [Set Start Trigger (In Range) VI](../../../../vi-lib/ni-veristand/execution/datalogging/set-start-trigger-in-range-vi.html) Specifies a trigger condition on which to start logging data. You also can specify whether to log channel data immediately preceding the trigger condition and whether logging is retriggerable, meaning the data logging session watches for subsequent occurrences of the start trigger after the first logging operation finishes. By default, logging stops after one operation. You must manually select the polymorphic instance to use.
- [Set Start Trigger (Start Immediately) VI](../../../../vi-lib/ni-veristand/execution/datalogging/set-start-trigger-start-immediately-vi.html) Specifies a trigger condition on which to start logging data. You also can specify whether to log channel data immediately preceding the trigger condition and whether logging is retriggerable, meaning the data logging session watches for subsequent occurrences of the start trigger after the first logging operation finishes. By default, logging stops after one operation. You must manually select the polymorphic instance to use.
- [Set Start Trigger (Value Change) VI](../../../../vi-lib/ni-veristand/execution/datalogging/set-start-trigger-value-change-vi.html) Specifies a trigger condition on which to start logging data. You also can specify whether to log channel data immediately preceding the trigger condition and whether logging is retriggerable, meaning the data logging session watches for subsequent occurrences of the start trigger after the first logging operation finishes. By default, logging stops after one operation. You must manually select the polymorphic instance to use.

Parent topic:

Configuration

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-analog-edge-vi.html language=unavailable -->
## TOPIC 00274: Set Stop Trigger Analog Edge Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-analog-edge-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-analog-edge-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-digital-edge-vi.html language=enus -->
## TOPIC 00275: Set Stop Trigger (Digital Edge) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-digital-edge-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-digital-edge-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a trigger condition on which to stop logging data. You also can specify whether to continue logging channel data for a set period of time after the trigger condition occurs. You must manually select the polymorphic instance to use. Generates a stop trigger when Trigger Channel starts risin

### Set Stop Trigger (Digital Edge) VI

Specifies a trigger condition on which to stop logging data. You also can specify whether to continue logging channel data for a set period of time after the trigger condition occurs.

You must manually select the polymorphic instance to use.

Note

Trigger Channel

Slope

[IMAGE alt='icon' src='set-stop-trigger-digital-edge-vi.png']

#### Inputs/Outputs

| Post-Trigger Duration (0 s) — Post-Trigger Duration specifies a duration in seconds to continue logging data after the stop trigger occurs. The default is 0. Data Logging Specification Ref in — Data Logging Specification Ref in specifies the reference to the data logging specification. You can use the New Data Logging Specification VI to create this reference. Slope — Slope specifies whether Trigger Channel must start rising or falling to generate a trigger. 0 Rising (default)—Generates a trigger on a rising edge, or a positive slope. 1 Falling—Generates a trigger on a falling edge, or a negative slope. Trigger Channel — Trigger Channel specifies the channel to watch for the trigger condition. Enter the path to the channel in the system definition file. For example: Targets/Controller/System Channels/Absolute Time error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Data Logging Specification Ref out — Data Logging Specification Ref out returns the reference to the data logging specification. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | Rising (default)—Generates a trigger on a rising edge, or a positive slope. |
| 1 | Falling—Generates a trigger on a falling edge, or a negative slope. |

Parent topic:

Set Stop Trigger VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-duration-vi.html language=enus -->
## TOPIC 00276: Set Stop Trigger (Duration) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-duration-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-duration-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a trigger condition on which to stop logging data. You also can specify whether to continue logging channel data for a set period of time after the trigger condition occurs. You must manually select the polymorphic instance to use. Generates a stop trigger when a specified amount of time e

### Set Stop Trigger (Duration) VI

Specifies a trigger condition on which to stop logging data. You also can specify whether to continue logging channel data for a set period of time after the trigger condition occurs.

You must manually select the polymorphic instance to use.

Note

[IMAGE alt='icon' src='set-stop-trigger-duration-vi.png']

#### Inputs/Outputs

| Data Logging Specification Ref in — Data Logging Specification Ref in specifies the reference to the data logging specification. You can use the New Data Logging Specification VI to create this reference. Duration — Duration specifies the time in seconds that must elapse to generate a stop trigger. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Data Logging Specification Ref out — Data Logging Specification Ref out returns the reference to the data logging specification. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Set Stop Trigger VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-formula-vi.html language=unavailable -->
## TOPIC 00277: Set Stop Trigger Formula Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-formula-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-formula-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-in-range-vi.html language=enus -->
## TOPIC 00278: Set Stop Trigger (In Range) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-in-range-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-in-range-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a trigger condition on which to stop logging data. You also can specify whether to continue logging channel data for a set period of time after the trigger condition occurs. You must manually select the polymorphic instance to use. Generates a stop trigger when the value of Trigger Channel

### Set Stop Trigger (In Range) VI

Specifies a trigger condition on which to stop logging data. You also can specify whether to continue logging channel data for a set period of time after the trigger condition occurs.

You must manually select the polymorphic instance to use.

Note

Trigger Channel

Range Options

[IMAGE alt='icon' src='set-stop-trigger-in-range-vi.png']

#### Inputs/Outputs

| Post-Trigger Duration (0 s) — Post-Trigger Duration specifies a duration in seconds to continue logging data after the stop trigger occurs. The default is 0. Data Logging Specification Ref in — Data Logging Specification Ref in specifies the reference to the data logging specification. You can use the New Data Logging Specification VI to create this reference. Range Options — Range Options specifies the high and low limit of the range to use for the trigger condition. If Invert is FALSE, the value of Trigger Channel must be within this range. If Invert is TRUE, the value must be outside this range. High Limit — High Limit specifies the high limit for trigger limit analysis. Low Limit — Low Limit specifies the low limit for trigger limit analysis. Invert — Invert specifies whether to invert the in-range evaluation to generate a trigger when the Trigger Channel value leaves the range specified by the limits. The default is FALSE, do not invert. Trigger Channel — Trigger Channel specifies the channel to watch for the trigger condition. Enter the path to the channel in the system definition file. For example: Targets/Controller/System Channels/Absolute Time error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Data Logging Specification Ref out — Data Logging Specification Ref out returns the reference to the data logging specification. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| High Limit — High Limit specifies the high limit for trigger limit analysis. Low Limit — Low Limit specifies the low limit for trigger limit analysis. Invert — Invert specifies whether to invert the in-range evaluation to generate a trigger when the Trigger Channel value leaves the range specified by the limits. The default is FALSE, do not invert. |

Parent topic:

Set Stop Trigger VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-log-indefinitely-vi.html language=unavailable -->
## TOPIC 00279: Set Stop Trigger Log Indefinitely Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-log-indefinitely-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-log-indefinitely-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-value-change-vi.html language=enus -->
## TOPIC 00280: Set Stop Trigger (Value Change) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-value-change-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-value-change-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a trigger condition on which to stop logging data. You also can specify whether to continue logging channel data for a set period of time after the trigger condition occurs. You must manually select the polymorphic instance to use. Generates a stop trigger when the value of Trigger Channel

### Set Stop Trigger (Value Change) VI

Specifies a trigger condition on which to stop logging data. You also can specify whether to continue logging channel data for a set period of time after the trigger condition occurs.

You must manually select the polymorphic instance to use.

Note

Trigger Channel

Deadband

[IMAGE alt='icon' src='set-stop-trigger-value-change-vi.png']

#### Inputs/Outputs

| Post-Trigger Duration (0 s) — Post-Trigger Duration specifies a duration in seconds to continue logging data after the stop trigger occurs. The default is 0. Data Logging Specification Ref in — Data Logging Specification Ref in specifies the reference to the data logging specification. You can use the New Data Logging Specification VI to create this reference. Deadband — Deadband specifies the amount by which the value of Trigger Channel must change to generate a trigger. Trigger Channel — Trigger Channel specifies the channel to watch for the trigger condition. Enter the path to the channel in the system definition file. For example: Targets/Controller/System Channels/Absolute Time error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Data Logging Specification Ref out — Data Logging Specification Ref out returns the reference to the data logging specification. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Set Stop Trigger VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-vi.html language=enus -->
## TOPIC 00281: Set Stop Trigger VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a trigger condition on which to stop logging data. You also can specify whether to continue logging channel data for a set period of time after the trigger condition occurs. You must manually select the polymorphic instance to use. icon

### Set Stop Trigger VI

Specifies a trigger condition on which to stop logging data. You also can specify whether to continue logging channel data for a set period of time after the trigger condition occurs.

You must manually select the polymorphic instance to use.

[IMAGE alt='icon' src='set-stop-trigger-vi.png']

- [Set Stop Trigger (Analog Edge) VI](../../../../vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-analog-edge-vi.html) Specifies a trigger condition on which to stop logging data. You also can specify whether to continue logging channel data for a set period of time after the trigger condition occurs. You must manually select the polymorphic instance to use.
- [Set Stop Trigger (Digital Edge) VI](../../../../vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-digital-edge-vi.html) Specifies a trigger condition on which to stop logging data. You also can specify whether to continue logging channel data for a set period of time after the trigger condition occurs. You must manually select the polymorphic instance to use.
- [Set Stop Trigger (Duration) VI](../../../../vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-duration-vi.html) Specifies a trigger condition on which to stop logging data. You also can specify whether to continue logging channel data for a set period of time after the trigger condition occurs. You must manually select the polymorphic instance to use.
- [Set Stop Trigger (Formula) VI](../../../../vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-formula-vi.html) Specifies a stop trigger condition that occurs when the formula specified in the Trigger Condition input evaluates to true. This formula must be a Boolean expression. The variables used in the expression must be valid identifiers. Use the Variable Mappings input to map the variables used in the expression to system definition channels, whose values will be used to evaluate the expression. Use the Post-Trigger Duration input to specify the post-trigger duration, which indicates the duration in seconds of data that is logged after the stop trigger condition occurs.
- [Set Stop Trigger (In Range) VI](../../../../vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-in-range-vi.html) Specifies a trigger condition on which to stop logging data. You also can specify whether to continue logging channel data for a set period of time after the trigger condition occurs. You must manually select the polymorphic instance to use.
- [Set Stop Trigger (Log Indefinitely) VI](../../../../vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-log-indefinitely-vi.html) Specifies a trigger condition on which to stop logging data. You also can specify whether to continue logging channel data for a set period of time after the trigger condition occurs. You must manually select the polymorphic instance to use.
- [Set Stop Trigger (Value Change) VI](../../../../vi-lib/ni-veristand/execution/datalogging/set-stop-trigger-value-change-vi.html) Specifies a trigger condition on which to stop logging data. You also can specify whether to continue logging channel data for a set period of time after the trigger condition occurs. You must manually select the polymorphic instance to use.

Parent topic:

Configuration

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/start-data-logging-session-vi.html language=enus -->
## TOPIC 00282: Start Data Logging Session VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/start-data-logging-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/start-data-logging-session-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Starts the data logging session specified by Data Logging Specification in. Use Session Name in to specify a unique name for the data logging session. You use this name to query and control logging operations during the logging session. icon Inputs/Outputs cbool.png Close Data Logging Specification

### Start Data Logging Session VI

Starts the data logging session specified by **Data Logging Specification in**. Use **Session Name in** to specify a unique name for the data logging session. You use this name to query and control logging operations during the logging session.

[IMAGE alt='icon' src='start-data-logging-session-vi.png']

#### Inputs/Outputs

| Close Data Logging Specification Ref (T) — Close Data Logging Specification Ref specifies whether to close the reference to the data logging specification after logging start. The default is TRUE, close the reference. Data Logging Specification Ref in — Data Logging Specification Ref in specifies the reference to the data logging specification. You can use the New Data Logging Specification VI to create this reference. Data Logging Manager Ref in — Data Logging Manager Ref in is the reference to the data logging service on the VeriStand Gateway. Session Name in — Session Name in specifies the name of the current data logging session. You use this name to query and control logging operations during the logging session. To avoid overwriting data, use unique session names for each data logging session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Data Logging Manager Ref out — Data Logging Manager Ref out returns the reference to the data logging service. Session Name out — Session Name out returns the name of the current data logging session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Data Logging

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/stop-data-logging-session-vi.html language=unavailable -->
## TOPIC 00283: Stop Data Logging Session Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/stop-data-logging-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/stop-data-logging-session-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/unregister-data-logging-events-vi.html language=enus -->
## TOPIC 00284: Unregister Data Logging Events VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/unregister-data-logging-events-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/unregister-data-logging-events-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unregisters for data logging events from the VeriStand Gateway. icon Inputs/Outputs ccclst.png Registered Data Logging Event Refnum Registered Data Logging Event Refnum contains information about the data logging event. ccallbackrefnum.png Callback Refnum Callback Refnum is a reference to the Regist

### Unregister Data Logging Events VI

Unregisters for data logging events from the VeriStand Gateway.

[IMAGE alt='icon' src='unregister-data-logging-events-vi.png']

#### Inputs/Outputs

| Registered Data Logging Event Refnum — Registered Data Logging Event Refnum contains information about the data logging event. Callback Refnum — Callback Refnum is a reference to the Register Event Callback. User Events — User Events is a reference to the Data Logging User Events. Error Event — Error Event is a reference to DataLoggingSessionError User Event, invoked when a data logging session produces an error. Start Event — Start Event is a reference to DataLoggingSession Start User Event, invoked when a new data logging session starts. State Change Event — State Change Event is a reference to DataLoggingSessionStateChange User Event, invoked when a data logging session changes state. Stop Event — Stop Event is a reference to the DataLoggingSessionStop User Event,invoked when a data logging session stops. File Closed Event — File Closed Event is a reference to the LogFileClosed User Event, invoked when a data logging session on the host computer closes a log file. File Opened Event — File Opened Event is a reference to the LogFileOpened User Event, invoked when a data logging session on the host computer opens a log file. New File Complete — New File Complete is a reference to NewLogFilesComplete User Event, invoked when a target generates a new log file. Features that perform logging on a target rather than the host, such as DAQ tasks and XNET raw frame data logging, generate this event. Event Refnum — Event Refnum is a reference to Waveform Data User Event Registration. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| Callback Refnum — Callback Refnum is a reference to the Register Event Callback. User Events — User Events is a reference to the Data Logging User Events. Error Event — Error Event is a reference to DataLoggingSessionError User Event, invoked when a data logging session produces an error. Start Event — Start Event is a reference to DataLoggingSession Start User Event, invoked when a new data logging session starts. State Change Event — State Change Event is a reference to DataLoggingSessionStateChange User Event, invoked when a data logging session changes state. Stop Event — Stop Event is a reference to the DataLoggingSessionStop User Event,invoked when a data logging session stops. File Closed Event — File Closed Event is a reference to the LogFileClosed User Event, invoked when a data logging session on the host computer closes a log file. File Opened Event — File Opened Event is a reference to the LogFileOpened User Event, invoked when a data logging session on the host computer opens a log file. New File Complete — New File Complete is a reference to NewLogFilesComplete User Event, invoked when a target generates a new log file. Features that perform logging on a target rather than the host, such as DAQ tasks and XNET raw frame data logging, generate this event. Event Refnum — Event Refnum is a reference to Waveform Data User Event Registration. |
| Error Event — Error Event is a reference to DataLoggingSessionError User Event, invoked when a data logging session produces an error. Start Event — Start Event is a reference to DataLoggingSession Start User Event, invoked when a new data logging session starts. State Change Event — State Change Event is a reference to DataLoggingSessionStateChange User Event, invoked when a data logging session changes state. Stop Event — Stop Event is a reference to the DataLoggingSessionStop User Event,invoked when a data logging session stops. File Closed Event — File Closed Event is a reference to the LogFileClosed User Event, invoked when a data logging session on the host computer closes a log file. File Opened Event — File Opened Event is a reference to the LogFileOpened User Event, invoked when a data logging session on the host computer opens a log file. New File Complete — New File Complete is a reference to NewLogFilesComplete User Event, invoked when a target generates a new log file. Features that perform logging on a target rather than the host, such as DAQ tasks and XNET raw frame data logging, generate this event. |

Parent topic:

Events

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/macroplayer/ni-veristand-close-command-line-notification-macro-player-vi.html language=enus -->
## TOPIC 00285: NI VeriStand - Close Command Line Notification (Macro Player) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/macroplayer/ni-veristand-close-command-line-notification-macro-player-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/macroplayer/ni-veristand-close-command-line-notification-macro-player-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an open reference to the command line of the Macro Player tool. Use the Open Command Line Notification (Macro Player) VI to open the reference this VI closes. icon Inputs/Outputs ccclst.png CommandLine Refs CommandLine Refs is the reference to the command line that you want to close. cusereve

### NI VeriStand - Close Command Line Notification (Macro Player) VI

Closes an open reference to the command line of the Macro Player tool. Use the Open Command Line Notification (Macro Player) VI to open the reference this VI closes.

[IMAGE alt='icon' src='ni-veristand-close-command-line-notification-macro-player-vi.png']

#### Inputs/Outputs

| CommandLine Refs — CommandLine Refs is the reference to the command line that you want to close. MacroPlayer CommandLine — MacroPlayer CommandLine is a reference to the Macro Command Line User Event, invoked just before a command to the Macro Player is logged. Event Callback Ref — Event Callback Ref is a reference to the Register Event Callback. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| MacroPlayer CommandLine — MacroPlayer CommandLine is a reference to the Macro Command Line User Event, invoked just before a command to the Macro Player is logged. Event Callback Ref — Event Callback Ref is a reference to the Register Event Callback. |

Parent topic:

Macro Player

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/macroplayer/ni-veristand-close-error-message-notification-vi.html language=enus -->
## TOPIC 00286: NI VeriStand - Close Error Message Notification VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/macroplayer/ni-veristand-close-error-message-notification-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/macroplayer/ni-veristand-close-error-message-notification-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an open reference to error messages the Macro Player sends. Use the Open Error Message Notification VI to open the reference this VI closes. icon Inputs/Outputs ccclst.png ErrorMessage Refs ErrorMessage Refs is the reference to the error messages that you want to close. cusereventrn.png Macro

### NI VeriStand - Close Error Message Notification VI

Closes an open reference to error messages the Macro Player sends. Use the Open Error Message Notification VI to open the reference this VI closes.

[IMAGE alt='icon' src='ni-veristand-close-error-message-notification-vi.png']

#### Inputs/Outputs

| ErrorMessage Refs — ErrorMessage Refs is the reference to the error messages that you want to close. MacroPlayer ErrorCluster — MacroPlayer ErrorCluster is a reference to the Macro Command Line User Event, invoked just before a command to the Macro Player is logged. Event Callback Ref — Event Callback Ref is a reference to the Register Event Callback. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| MacroPlayer ErrorCluster — MacroPlayer ErrorCluster is a reference to the Macro Command Line User Event, invoked just before a command to the Macro Player is logged. Event Callback Ref — Event Callback Ref is a reference to the Register Event Callback. |

Parent topic:

Macro Player

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/macroplayer/ni-veristand-close-macro-player-reference-vi.html language=enus -->
## TOPIC 00287: NI VeriStand - Close Macro Player Reference VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/macroplayer/ni-veristand-close-macro-player-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/macroplayer/ni-veristand-close-macro-player-reference-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an open reference to the Macro Player tool on the VeriStand Gateway. Use this VI to close each Macro Player reference that you open with the Open Macro Player Reference VI. icon Inputs/Outputs cgnrn.png MacroPlayer MacroPlayer is a reference to the Macro Player. You must open a reference to t

### NI VeriStand - Close Macro Player Reference VI

Closes an open reference to the Macro Player tool on the VeriStand Gateway. Use this VI to close each Macro Player reference that you open with the Open Macro Player Reference VI.

[IMAGE alt='icon' src='ni-veristand-close-macro-player-reference-vi.png']

#### Inputs/Outputs

| MacroPlayer — MacroPlayer is a reference to the Macro Player. You must open a reference to the macro player to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Macro Player

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/macroplayer/ni-veristand-close-percent-complete-notification-vi.html language=enus -->
## TOPIC 00288: NI VeriStand - Close Percent Complete Notification VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/macroplayer/ni-veristand-close-percent-complete-notification-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/macroplayer/ni-veristand-close-percent-complete-notification-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an open reference to messages the Macro Player sends that indicate the percentage of the macro file that has played back. Use the Open Percent Complete Notification VI to open the reference this VI closes. icon Inputs/Outputs ccclst.png PercentComplete Refs PercentComplete Refs is the referen

### NI VeriStand - Close Percent Complete Notification VI

Closes an open reference to messages the Macro Player sends that indicate the percentage of the macro file that has played back. Use the Open Percent Complete Notification VI to open the reference this VI closes.

[IMAGE alt='icon' src='ni-veristand-close-percent-complete-notification-vi.png']

#### Inputs/Outputs

| PercentComplete Refs — PercentComplete Refs is the reference to the percent complete messages that you want to close. MacroPlayer PercentComplete — MacroPlayer PercentComplete is a reference to the Macro Percent Complete Event, invoked after executing a Macro Player command. The percent is calculated using the length of time a command takes to execute relative to the total time required for all commands to execute. Event Callback Ref — Event Callback Ref is a reference to the Register Event Callback. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| MacroPlayer PercentComplete — MacroPlayer PercentComplete is a reference to the Macro Percent Complete Event, invoked after executing a Macro Player command. The percent is calculated using the length of time a command takes to execute relative to the total time required for all commands to execute. Event Callback Ref — Event Callback Ref is a reference to the Register Event Callback. |

Parent topic:

Macro Player

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/macroplayer/ni-veristand-get-macro-player-command-lines-vi.html language=enus -->
## TOPIC 00289: NI VeriStand - Get Macro Player Command Lines VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/macroplayer/ni-veristand-get-macro-player-command-lines-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/macroplayer/ni-veristand-get-macro-player-command-lines-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the commands the VeriStand Gateway sends to the RT target or desktop PC during recording. You must use the Open Command Line Notification (Macro Player) VI to open a reference to the command line of the Macro Player tool before you call this VI. icon Inputs/Outputs cgnrn.png MacroPlayer in M

### NI VeriStand - Get Macro Player Command Lines VI

Returns the commands the VeriStand Gateway sends to the RT target or desktop PC during recording. You must use the Open Command Line Notification (Macro Player) VI to open a reference to the command line of the Macro Player tool before you call this VI.

[IMAGE alt='icon' src='ni-veristand-get-macro-player-command-lines-vi.png']

#### Inputs/Outputs

| MacroPlayer in — MacroPlayer in is a reference to the Macro Player on the VeriStand Gateway. You must open a reference to the Macro Player to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. MacroPlayer out — MacroPlayer out returns a reference to the Macro Player. You can wire this output to other Macro Player VIs. Command Lines — Command Lines returns an array containing all the commands the VeriStand Gateway sends to the target and the time at which each command is sent. Seconds — Seconds returns the time at which the command shown in Command Text is sent in seconds elapsed from the beginning of the recording. Command Text — Command Text returns the name of the command. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| Seconds — Seconds returns the time at which the command shown in Command Text is sent in seconds elapsed from the beginning of the recording. Command Text — Command Text returns the name of the command. |

Parent topic:

Macro Player

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/macroplayer/ni-veristand-get-macro-player-state-vi.html language=unavailable -->
## TOPIC 00290: Ni Veristand Get Macro Player State Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/macroplayer/ni-veristand-get-macro-player-state-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/macroplayer/ni-veristand-get-macro-player-state-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/macroplayer/ni-veristand-load-macro-vi.html language=unavailable -->
## TOPIC 00291: Ni Veristand Load Macro Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/macroplayer/ni-veristand-load-macro-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/macroplayer/ni-veristand-load-macro-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/macroplayer/ni-veristand-open-command-line-notification-macro-player-vi.html language=enus -->
## TOPIC 00292: NI VeriStand - Open Command Line Notification (Macro Player) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/macroplayer/ni-veristand-open-command-line-notification-macro-player-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/macroplayer/ni-veristand-open-command-line-notification-macro-player-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a reference to the command line of the Macro Player tool. Opening this reference enables you to use the Get Macro Player Command Lines VI to read the commands the VeriStand Gateway sends to the RT target or desktop PC. This VI also returns a user event that you can register and wire to an Even

### NI VeriStand - Open Command Line Notification (Macro Player) VI

Opens a reference to the command line of the Macro Player tool. Opening this reference enables you to use the Get Macro Player Command Lines VI to read the commands the VeriStand Gateway sends to the RT target or desktop PC. This VI also returns a user event that you can register and wire to an Event structure.

[IMAGE alt='icon' src='ni-veristand-open-command-line-notification-macro-player-vi.png']

#### Inputs/Outputs

| MacroPlayer in — MacroPlayer in is a reference to the Macro Player on the VeriStand Gateway. You must open a reference to the Macro Player to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. MacroPlayer out — MacroPlayer out returns a reference to the Macro Player. You can wire this output to other Macro Player VIs. CommandLine Refs — CommandLine Refs returns the MacroPlayer CommandLine user event and an event callback reference. Use the Register For Events function to register the user event and use it with an Event structure. MacroPlayer CommandLine — MacroPlayer CommandLine is a reference to the Macro Command Line User Event, invoked just before a command to the Macro Player is logged. Event Callback Ref — Event Callback Ref is a reference to the Register Event Callback. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| MacroPlayer CommandLine — MacroPlayer CommandLine is a reference to the Macro Command Line User Event, invoked just before a command to the Macro Player is logged. Event Callback Ref — Event Callback Ref is a reference to the Register Event Callback. |

Parent topic:

Macro Player

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/macroplayer/ni-veristand-open-error-message-notification-vi.html language=unavailable -->
## TOPIC 00293: Ni Veristand Open Error Message Notification Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/macroplayer/ni-veristand-open-error-message-notification-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/macroplayer/ni-veristand-open-error-message-notification-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/macroplayer/ni-veristand-open-macro-player-reference-vi.html language=enus -->
## TOPIC 00294: NI VeriStand - Open Macro Player Reference VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/macroplayer/ni-veristand-open-macro-player-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/macroplayer/ni-veristand-open-macro-player-reference-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a reference to the Macro Player tool on the VeriStand Gateway. The Macro Player plays back macro files you record using the Macro Recorder VIs. You must open a reference to the Macro Player before using any other VIs on this palette. icon Inputs/Outputs cstr.png Gateway IP Address ("": localho

### NI VeriStand - Open Macro Player Reference VI

Opens a reference to the Macro Player tool on the VeriStand Gateway. The Macro Player plays back macro files you record using the Macro Recorder VIs. You must open a reference to the Macro Player before using any other VIs on this palette.

[IMAGE alt='icon' src='ni-veristand-open-macro-player-reference-vi.png']

#### Inputs/Outputs

| Gateway IP Address ("": localhost) — Gateway IP Address specifies the IP address of the VeriStand Gateway. This address can be in IP dot notation or it can be a hostname. If you do not specify an address, LabVIEW establishes a connection to the local computer. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. MacroPlayer — MacroPlayer is a reference to the Macro Player tool. You can wire this output to other Macro Player VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Macro Player

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/macroplayer/ni-veristand-open-percent-complete-notification-vi.html language=enus -->
## TOPIC 00295: NI VeriStand - Open Percent Complete Notification VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/macroplayer/ni-veristand-open-percent-complete-notification-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/macroplayer/ni-veristand-open-percent-complete-notification-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a reference to messages the Macro Player sends that indicate the percentage of the macro file that has played back. This VI returns a user event that you can register and wire to an Event structure. icon Inputs/Outputs cgnrn.png MacroPlayer in MacroPlayer in is a reference to the Macro Player

### NI VeriStand - Open Percent Complete Notification VI

Opens a reference to messages the Macro Player sends that indicate the percentage of the macro file that has played back. This VI returns a user event that you can register and wire to an Event structure.

[IMAGE alt='icon' src='ni-veristand-open-percent-complete-notification-vi.png']

#### Inputs/Outputs

| MacroPlayer in — MacroPlayer in is a reference to the Macro Player on the VeriStand Gateway. You must open a reference to the Macro Player to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. MacroPlayer out — MacroPlayer out returns a reference to the Macro Player. You can wire this output to other Macro Player VIs. PercentComplete Refs — PercentComplete Refs returns the MacroPlayer PercentComplete user event and an event callback reference. Use the Register For Events function to register the user event and use it with an Event structure. MacroPlayer PercentComplete — MacroPlayer PercentComplete is a reference to the Macro Percent Complete Event, invoked after executing a Macro Player command. The percent is calculated using the length of time a command takes to execute relative to the total time required for all commands to execute. Event Callback Ref — Event Callback Ref is a reference to the Register Event Callback. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| MacroPlayer PercentComplete — MacroPlayer PercentComplete is a reference to the Macro Percent Complete Event, invoked after executing a Macro Player command. The percent is calculated using the length of time a command takes to execute relative to the total time required for all commands to execute. Event Callback Ref — Event Callback Ref is a reference to the Register Event Callback. |

Parent topic:

Macro Player

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/macroplayer/ni-veristand-pause-macro-player-vi.html language=unavailable -->
## TOPIC 00296: Ni Veristand Pause Macro Player Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/macroplayer/ni-veristand-pause-macro-player-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/macroplayer/ni-veristand-pause-macro-player-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/macroplayer/ni-veristand-resume-macro-player-vi.html language=enus -->
## TOPIC 00297: NI VeriStand - Resume Macro Player VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/macroplayer/ni-veristand-resume-macro-player-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/macroplayer/ni-veristand-resume-macro-player-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resumes the playback of a macro file that was paused using the Pause Macro Player VI. This VI plays back the file from the point at which the Pause Macro Player VI paused playback. icon Inputs/Outputs cgnrn.png MacroPlayer in MacroPlayer in is a reference to the Macro Player on the VeriStand Gateway

### NI VeriStand - Resume Macro Player VI

Resumes the playback of a macro file that was paused using the Pause Macro Player VI. This VI plays back the file from the point at which the Pause Macro Player VI paused playback.

[IMAGE alt='icon' src='ni-veristand-resume-macro-player-vi.png']

#### Inputs/Outputs

| MacroPlayer in — MacroPlayer in is a reference to the Macro Player on the VeriStand Gateway. You must open a reference to the Macro Player to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. MacroPlayer out — MacroPlayer out returns a reference to the Macro Player. You can wire this output to other Macro Player VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Macro Player

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/macroplayer/ni-veristand-run-macro-player-vi.html language=unavailable -->
## TOPIC 00298: Ni Veristand Run Macro Player Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/macroplayer/ni-veristand-run-macro-player-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/macroplayer/ni-veristand-run-macro-player-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/macroplayer/ni-veristand-stop-macro-player-vi.html language=enus -->
## TOPIC 00299: NI VeriStand - Stop Macro Player VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/macroplayer/ni-veristand-stop-macro-player-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/macroplayer/ni-veristand-stop-macro-player-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops the Macro Player. This VI returns the Macro Player to the idle state and resets the macro you are playing back to the beginning of the recording. If you want to be able to resume playback from the place where you stop it, use the Pause Macro Player VI instead. icon Inputs/Outputs cgnrn.png Mac

### NI VeriStand - Stop Macro Player VI

Stops the Macro Player. This VI returns the Macro Player to the idle state and resets the macro you are playing back to the beginning of the recording. If you want to be able to resume playback from the place where you stop it, use the Pause Macro Player VI instead.

[IMAGE alt='icon' src='ni-veristand-stop-macro-player-vi.png']

#### Inputs/Outputs

| MacroPlayer in — MacroPlayer in is a reference to the Macro Player on the VeriStand Gateway. You must open a reference to the Macro Player to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. MacroPlayer out — MacroPlayer out returns a reference to the Macro Player. You can wire this output to other Macro Player VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Macro Player

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/macroplayer/ni-veristand-wait-for-macro-player-completion-vi.html language=enus -->
## TOPIC 00300: NI VeriStand - Wait For Macro Player Completion VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/macroplayer/ni-veristand-wait-for-macro-player-completion-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/macroplayer/ni-veristand-wait-for-macro-player-completion-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the Macro Player tool to finish playing back the current macro file before continuing execution and returning a reference to the Macro Player. icon Inputs/Outputs cgnrn.png MacroPlayer in MacroPlayer in is a reference to the Macro Player on the VeriStand Gateway. You must open a reference

### NI VeriStand - Wait For Macro Player Completion VI

Waits for the Macro Player tool to finish playing back the current macro file before continuing execution and returning a reference to the Macro Player.

[IMAGE alt='icon' src='ni-veristand-wait-for-macro-player-completion-vi.png']

#### Inputs/Outputs

| MacroPlayer in — MacroPlayer in is a reference to the Macro Player on the VeriStand Gateway. You must open a reference to the Macro Player to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. MacroPlayer out — MacroPlayer out returns a reference to the Macro Player. You can wire this output to other Macro Player VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Macro Player

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-close-command-line-notification-macro-recorder-vi.html language=enus -->
## TOPIC 00301: NI VeriStand - Close Command Line Notification (Macro Recorder) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-close-command-line-notification-macro-recorder-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-close-command-line-notification-macro-recorder-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an open reference to the command line of the Macro Recorder tool. Use the Open Command Line Notification (Macro Recorder) VI to open the reference this VI closes. icon Inputs/Outputs ccclst.png CommandLine Refs CommandLine Refs is the reference to the command line that you want to close. cuse

### NI VeriStand - Close Command Line Notification (Macro Recorder) VI

Closes an open reference to the command line of the Macro Recorder tool. Use the Open Command Line Notification (Macro Recorder) VI to open the reference this VI closes.

[IMAGE alt='icon' src='ni-veristand-close-command-line-notification-macro-recorder-vi.png']

#### Inputs/Outputs

| CommandLine Refs — CommandLine Refs is the reference to the command line that you want to close. MacroRecorder CommandLine — MacroRecorder CommandLine is a reference to the Macro Command Line User Event, invoked just before a command to the Macro Recorder is logged. Event Callback Ref — Event Callback Ref is a reference to the Register Event Callback. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| MacroRecorder CommandLine — MacroRecorder CommandLine is a reference to the Macro Command Line User Event, invoked just before a command to the Macro Recorder is logged. Event Callback Ref — Event Callback Ref is a reference to the Register Event Callback. |

Parent topic:

Macro Recorder

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-close-macro-recorder-reference-vi.html language=unavailable -->
## TOPIC 00302: Ni Veristand Close Macro Recorder Reference Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-close-macro-recorder-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-close-macro-recorder-reference-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-get-macro-recorder-command-lines-vi.html language=enus -->
## TOPIC 00303: NI VeriStand - Get Macro Recorder Command Lines VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-get-macro-recorder-command-lines-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-get-macro-recorder-command-lines-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the commands the VeriStand Gateway sends to the RT target or desktop PC. You must use the Open Command Line Notification (Macro Recorder) VI to open a reference to the command line of the Macro Recorder tool before you call this VI. icon Inputs/Outputs cgnrn.png MacroRecorder in MacroRecorde

### NI VeriStand - Get Macro Recorder Command Lines VI

Returns the commands the VeriStand Gateway sends to the RT target or desktop PC. You must use the Open Command Line Notification (Macro Recorder) VI to open a reference to the command line of the Macro Recorder tool before you call this VI.

[IMAGE alt='icon' src='ni-veristand-get-macro-recorder-command-lines-vi.png']

#### Inputs/Outputs

| MacroRecorder in — MacroRecorder in is a reference to the Macro Recorder on the VeriStand Gateway. You must open a reference to the macro recorder to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. MacroRecorder out — MacroRecorder out returns a reference to the Macro Recorder. You can wire this output to other Macro Recorder VIs. Command Lines — Command Lines returns an array containing all the commands the VeriStand Gateway sends to the target and the time at which each command is sent. Seconds — Seconds returns the time at which the command shown in Command Text is sent in seconds elapsed from the beginning of the recording. Command Text — Command Text returns the name of the command. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| Seconds — Seconds returns the time at which the command shown in Command Text is sent in seconds elapsed from the beginning of the recording. Command Text — Command Text returns the name of the command. |

Parent topic:

Macro Recorder

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-open-command-line-notification-macro-recorder-vi.html language=enus -->
## TOPIC 00304: NI VeriStand - Open Command Line Notification (Macro Recorder) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-open-command-line-notification-macro-recorder-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-open-command-line-notification-macro-recorder-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a reference to the command line of the Macro Recorder tool. Opening this reference enables you to use the Get Macro Recorder Command Lines VI to read the commands the VeriStand Gateway sends to the RT target or desktop PC. This VI also returns a user event that you can register and wire to an

### NI VeriStand - Open Command Line Notification (Macro Recorder) VI

Opens a reference to the command line of the Macro Recorder tool. Opening this reference enables you to use the Get Macro Recorder Command Lines VI to read the commands the VeriStand Gateway sends to the RT target or desktop PC. This VI also returns a user event that you can register and wire to an Event structure.

[IMAGE alt='icon' src='ni-veristand-open-command-line-notification-macro-recorder-vi.png']

#### Inputs/Outputs

| MacroRecorder in — MacroRecorder in is a reference to the Macro Recorder on the VeriStand Gateway. You must open a reference to the macro recorder to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. MacroRecorder out — MacroRecorder out returns a reference to the Macro Recorder. You can wire this output to other Macro Recorder VIs. CommandLine Refs — CommandLine Refs returns the MacroRecorder CommandLine user event and an event callback reference. Use the Register For Events function to register the user event and use it with an Event structure. MacroRecorder CommandLine — MacroRecorder CommandLine is a reference to the Macro Command Line User Event, invoked just before a command to the Macro Recorder is logged. Event Callback Ref — Event Callback Ref is a reference to the Register Event Callback. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| MacroRecorder CommandLine — MacroRecorder CommandLine is a reference to the Macro Command Line User Event, invoked just before a command to the Macro Recorder is logged. Event Callback Ref — Event Callback Ref is a reference to the Register Event Callback. |

Parent topic:

Macro Recorder

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-open-macro-recorder-reference-vi.html language=unavailable -->
## TOPIC 00305: Ni Veristand Open Macro Recorder Reference Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-open-macro-recorder-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-open-macro-recorder-reference-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-resume-macro-recording-vi.html language=unavailable -->
## TOPIC 00306: Ni Veristand Resume Macro Recording Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-resume-macro-recording-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-resume-macro-recording-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-save-macro-vi.html language=enus -->
## TOPIC 00307: NI VeriStand - Save Macro VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-save-macro-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-save-macro-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the current macro recording. You must use the Stop Macro Recording VI to stop recording before you call this VI. This VI creates a file of the type .nivsmacro. You can use the Macro Player VIs to load the file this VI creates and to play back the saved recording. icon Inputs/Outputs cgnrn.png

### NI VeriStand - Save Macro VI

Saves the current macro recording. You must use the Stop Macro Recording VI to stop recording before you call this VI. This VI creates a file of the type .nivsmacro. You can use the Macro Player VIs to load the file this VI creates and to play back the saved recording.

[IMAGE alt='icon' src='ni-veristand-save-macro-vi.png']

#### Inputs/Outputs

| MacroRecorder in — MacroRecorder in is a reference to the Macro Recorder on the VeriStand Gateway. You must open a reference to the macro recorder to use this parameter. File path — File path specifies the full path to the macro (.nivsmacro) file. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. MacroRecorder out — MacroRecorder out returns a reference to the Macro Recorder. You can wire this output to other Macro Recorder VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Macro Recorder

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-start-macro-recording-vi.html language=unavailable -->
## TOPIC 00308: Ni Veristand Start Macro Recording Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-start-macro-recording-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-start-macro-recording-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-stop-macro-recording-vi.html language=enus -->
## TOPIC 00309: NI VeriStand - Stop Macro Recording VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-stop-macro-recording-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-stop-macro-recording-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops the current macro recording. This VI does not save the recording or remove the recording from memory. Use the Save Macro VI to save the recording. If you call the Start Macro Recording VI after this VI without calling the Save Macro VI, LabVIEW removes the current macro recording from memory.

### NI VeriStand - Stop Macro Recording VI

Stops the current macro recording. This VI does not save the recording or remove the recording from memory. Use the Save Macro VI to save the recording.

Note

[IMAGE alt='icon' src='ni-veristand-stop-macro-recording-vi.png']

#### Inputs/Outputs

| MacroRecorder in — MacroRecorder in is a reference to the Macro Recorder on the VeriStand Gateway. You must open a reference to the macro recorder to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. MacroRecorder out — MacroRecorder out returns a reference to the Macro Recorder. You can wire this output to other Macro Recorder VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Macro Recorder

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/model/ni-veristand-close-model-vi.html language=enus -->
## TOPIC 00310: NI VeriStand - Close Model VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/model/ni-veristand-close-model-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/model/ni-veristand-close-model-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an open reference to a model. Use this VI to close each model reference that you open with the Open Model VI. icon Inputs/Outputs cgnrn.png Model Model is a reference to a model running on the target. You must open a reference to a model to use this parameter. cerrcodeclst.png error in (no er

### NI VeriStand - Close Model VI

Closes an open reference to a model. Use this VI to close each model reference that you open with the Open Model VI.

[IMAGE alt='icon' src='ni-veristand-close-model-vi.png']

#### Inputs/Outputs

| Model — Model is a reference to a model running on the target. You must open a reference to a model to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Model Execution

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/model/ni-veristand-get-model-execution-state-vi.html language=enus -->
## TOPIC 00311: NI VeriStand - Get Model Execution State VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/model/ni-veristand-get-model-execution-state-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/model/ni-veristand-get-model-execution-state-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the state and running time of the model you specify. icon Inputs/Outputs cgnrn.png Model in Model in is a reference to a model running on the target. You must open a reference to a model to use this parameter. cerrcodeclst.png error in (no error) error in describes error conditions that occu

### NI VeriStand - Get Model Execution State VI

Returns the state and running time of the model you specify.

[IMAGE alt='icon' src='ni-veristand-get-model-execution-state-vi.png']

#### Inputs/Outputs

| Model in — Model in is a reference to a model running on the target. You must open a reference to a model to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Model out — Model out returns a reference to a model running on the target. Model State — Model State indicates the current state of the model. 0 Running (default)—Indicates the model is running. 1 Paused—Indicates the model is paused. 2 Resetting—Indicates the model is resetting. 3 Idle—Indicates the model is idle. 4 Stopped—Indicates the model is stopped. Model Time — Model Time indicates the current running time of the model. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | Running (default)—Indicates the model is running. |
| 1 | Paused—Indicates the model is paused. |
| 2 | Resetting—Indicates the model is resetting. |
| 3 | Idle—Indicates the model is idle. |
| 4 | Stopped—Indicates the model is stopped. |

Parent topic:

Model Execution

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/model/ni-veristand-open-model-vi.html language=enus -->
## TOPIC 00312: NI VeriStand - Open Model VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/model/ni-veristand-open-model-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/model/ni-veristand-open-model-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a reference to a model. You must open a reference before using any other VIs on this palette. icon Inputs/Outputs cstr.png Target Target specifies the name of the target on which the models are running. This input expects the name of the target as specified in the System Explorer window. For e

### NI VeriStand - Open Model VI

Opens a reference to a model. You must open a reference before using any other VIs on this palette.

[IMAGE alt='icon' src='ni-veristand-open-model-vi.png']

#### Inputs/Outputs

| Target — Target specifies the name of the target on which the models are running. This input expects the name of the target as specified in the System Explorer window. For example: Controller. Model Name — Model Name specifies the name of the model to which you want to open a reference. Gateway IP Address ("": localhost) — Gateway IP Address specifies the IP address of the VeriStand Gateway. This address can be in IP dot notation or it can be a hostname. If you do not specify an address, LabVIEW establishes a connection to the local computer. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Model — Model is a reference to a model running on the target. You can wire this output to other Model Execution VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Model Execution

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/model/ni-veristand-restore-model-state-vi.html language=enus -->
## TOPIC 00313: NI VeriStand - Restore Model State VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/model/ni-veristand-restore-model-state-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/model/ni-veristand-restore-model-state-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Restores a model to the state defined by the file you specify. You only can use this VI on your models and your compiled models you have built using The MathWorks, Inc. Simulink(R) software. icon Inputs/Outputs cgnrn.png Model in Model in is a reference to a model running on the target. You must ope

### NI VeriStand - Restore Model State VI

Restores a model to the state defined by the file you specify. You only can use this VI on your models and your compiled models you have built using The MathWorks, Inc. Simulink(R) software.

[IMAGE alt='icon' src='ni-veristand-restore-model-state-vi.png']

#### Inputs/Outputs

| Model in — Model in is a reference to a model running on the target. You must open a reference to a model to use this parameter. FilePath — FilePath specifies the path to the file containing the saved execution state data you want to load to a model running on the target. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Model out — Model out is a reference to a model running on the target. You can wire this output to other Model Execution VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Model Execution

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/model/ni-veristand-save-model-state-vi.html language=enus -->
## TOPIC 00314: NI VeriStand - Save Model State VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/model/ni-veristand-save-model-state-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/model/ni-veristand-save-model-state-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves data about the current state of a model running on the target to a file you specify. You only can use this VI on your models and your compiled models you have built using The MathWorks, Inc. Simulink(R) software. icon Inputs/Outputs cgnrn.png Model in Model in is a reference to a model running

### NI VeriStand - Save Model State VI

Saves data about the current state of a model running on the target to a file you specify. You only can use this VI on your models and your compiled models you have built using The MathWorks, Inc. Simulink(R) software.

[IMAGE alt='icon' src='ni-veristand-save-model-state-vi.png']

#### Inputs/Outputs

| Model in — Model in is a reference to a model running on the target. You must open a reference to a model to use this parameter. FilePath — FilePath specifies the path to the file where you want to save data about the current state of the model. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Model out — Model out is a reference to a model running on the target. You can wire this output to other Model Execution VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Model Execution

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/model/ni-veristand-set-model-execution-state-vi.html language=unavailable -->
## TOPIC 00315: Ni Veristand Set Model Execution State Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/model/ni-veristand-set-model-execution-state-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/model/ni-veristand-set-model-execution-state-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/modelmanager/ni-veristand-close-model-manager-reference-vi.html language=enus -->
## TOPIC 00316: NI VeriStand - Close Model Manager Reference VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/modelmanager/ni-veristand-close-model-manager-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/modelmanager/ni-veristand-close-model-manager-reference-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an open reference to the model manager on the VeriStand Gateway. Use this VI to close each model manager reference that you open with the Open Model Manager Reference VI. icon Inputs/Outputs cgnrn.png ModelManager ModelManager is a reference to the model manager on the VeriStand Gateway. You

### NI VeriStand - Close Model Manager Reference VI

Closes an open reference to the model manager on the VeriStand Gateway. Use this VI to close each model manager reference that you open with the Open Model Manager Reference VI.

[IMAGE alt='icon' src='ni-veristand-close-model-manager-reference-vi.png']

#### Inputs/Outputs

| ModelManager — ModelManager is a reference to the model manager on the VeriStand Gateway. You must open a reference to the model manager to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Models

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/modelmanager/ni-veristand-get-model-list-vi.html language=enus -->
## TOPIC 00317: NI VeriStand - Get Model List VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/modelmanager/ni-veristand-get-model-list-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/modelmanager/ni-veristand-get-model-list-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of all the models running on the target. icon Inputs/Outputs cstr.png Target Target specifies the name of the target on which the models are running. This input expects the name of the target as specified in the System Explorer window. For example: Controller. cgnrn.png ModelManager i

### NI VeriStand - Get Model List VI

Returns a list of all the models running on the target.

[IMAGE alt='icon' src='ni-veristand-get-model-list-vi.png']

#### Inputs/Outputs

| Target — Target specifies the name of the target on which the models are running. This input expects the name of the target as specified in the System Explorer window. For example: Controller. ModelManager in — ModelManager in is a reference to the model manager on the VeriStand Gateway. You must open a reference to the model manager to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. ModelManager out — ModelManager out is a reference to the model manager on the VeriStand Gateway. You can wire this output to other Models VIs. Models — Models returns a list of all the models running on the target. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Models

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/modelmanager/ni-veristand-get-multiple-parameter-values-vi.html language=enus -->
## TOPIC 00318: NI VeriStand - Get Multiple Parameter Values VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/modelmanager/ni-veristand-get-multiple-parameter-values-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/modelmanager/ni-veristand-get-multiple-parameter-values-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns values of model parameters present on the target. You must manually select the polymorphic instance to use. Returns the values of multiple model parameters present on the target. icon Inputs/Outputs cstr.png Target Target specifies the name of the target on which the models are running. This

### NI VeriStand - Get Multiple Parameter Values VI

Returns values of model parameters present on the target. You must manually select the polymorphic instance to use.

Note

[IMAGE alt='icon' src='ni-veristand-get-multiple-parameter-values-vi.png']

#### Inputs/Outputs

| Target — Target specifies the name of the target on which the models are running. This input expects the name of the target as specified in the System Explorer window. For example: Controller. ModelManager in — ModelManager in is a reference to the model manager on the VeriStand Gateway. You must open a reference to the model manager to use this parameter. Parameters — Parameters specifies the parameters whose value this VI returns. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. ModelManager out — ModelManager out is a reference to the model manager on the VeriStand Gateway. You can wire this output to other Models VIs. Values — Values indicates a list of the values of the specified parameters. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI VeriStand - Get Parameter Value VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/modelmanager/ni-veristand-get-parameter-2d-array-values-vi.html language=unavailable -->
## TOPIC 00319: Ni Veristand Get Parameter 2D Array Values Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/modelmanager/ni-veristand-get-parameter-2d-array-values-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/modelmanager/ni-veristand-get-parameter-2d-array-values-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/modelmanager/ni-veristand-get-parameter-value-vi.html language=unavailable -->
## TOPIC 00320: Ni Veristand Get Parameter Value Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/modelmanager/ni-veristand-get-parameter-value-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/modelmanager/ni-veristand-get-parameter-value-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/modelmanager/ni-veristand-get-parameters-list-vi.html language=unavailable -->
## TOPIC 00321: Ni Veristand Get Parameters List Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/modelmanager/ni-veristand-get-parameters-list-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/modelmanager/ni-veristand-get-parameters-list-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/modelmanager/ni-veristand-get-single-parameter-value-vi.html language=enus -->
## TOPIC 00322: NI VeriStand - Get Single Parameter Value VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/modelmanager/ni-veristand-get-single-parameter-value-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/modelmanager/ni-veristand-get-single-parameter-value-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns values of model parameters present on the target. You must manually select the polymorphic instance to use. icon Inputs/Outputs cstr.png Target Target specifies the name of the target on which the models are running. This input expects the name of the target as specified in the System Explor

### NI VeriStand - Get Single Parameter Value VI

Returns values of model parameters present on the target. You must manually select the polymorphic instance to use.

[IMAGE alt='icon' src='ni-veristand-get-single-parameter-value-vi.png']

#### Inputs/Outputs

| Target — Target specifies the name of the target on which the models are running. This input expects the name of the target as specified in the System Explorer window. For example: Controller. ModelManager in — ModelManager in is a reference to the model manager on the VeriStand Gateway. You must open a reference to the model manager to use this parameter. Parameter — Parameter specifies the parameter whose value this VI returns. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. ModelManager out — ModelManager out is a reference to the model manager on the VeriStand Gateway. You can wire this output to other Models VIs. Value — Value indicates the value of the specified parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI VeriStand - Get Parameter Value VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/modelmanager/ni-veristand-open-model-manager-reference-vi.html language=enus -->
## TOPIC 00323: NI VeriStand - Open Model Manager Reference VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/modelmanager/ni-veristand-open-model-manager-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/modelmanager/ni-veristand-open-model-manager-reference-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a reference to the model manager on the VeriStand Gateway. You must open a reference before using any other VIs on this palette. icon Inputs/Outputs cstr.png Gateway IP Address ("": localhost) Gateway IP Address specifies the IP address of the VeriStand Gateway. This address can be in IP dot n

### NI VeriStand - Open Model Manager Reference VI

Opens a reference to the model manager on the VeriStand Gateway. You must open a reference before using any other VIs on this palette.

[IMAGE alt='icon' src='ni-veristand-open-model-manager-reference-vi.png']

#### Inputs/Outputs

| Gateway IP Address ("": localhost) — Gateway IP Address specifies the IP address of the VeriStand Gateway. This address can be in IP dot notation or it can be a hostname. If you do not specify an address, LabVIEW establishes a connection to the local computer. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. ModelManager — ModelManager is a reference to the model manager on the VeriStand Gateway. You can wire this output to other Models VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Models

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/modelmanager/ni-veristand-set-multiple-parameter-2d-array-values-vi.html language=unavailable -->
## TOPIC 00324: Ni Veristand Set Multiple Parameter 2D Array Values Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/modelmanager/ni-veristand-set-multiple-parameter-2d-array-values-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/modelmanager/ni-veristand-set-multiple-parameter-2d-array-values-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/modelmanager/ni-veristand-set-multiple-parameter-values-vi.html language=enus -->
## TOPIC 00325: NI VeriStand - Set Multiple Parameter Values VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/modelmanager/ni-veristand-set-multiple-parameter-values-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/modelmanager/ni-veristand-set-multiple-parameter-values-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets values of model parameters present on the target. You must manually select the polymorphic instance to use. Sets values of multiple model parameters present on the target. icon Inputs/Outputs cstr.png Target Target specifies the name of the target on which the models are running. This input exp

### NI VeriStand - Set Multiple Parameter Values VI

Sets values of model parameters present on the target. You must manually select the polymorphic instance to use.

Note

[IMAGE alt='icon' src='ni-veristand-set-multiple-parameter-values-vi.png']

#### Inputs/Outputs

| Target — Target specifies the name of the target on which the models are running. This input expects the name of the target as specified in the System Explorer window. For example: Controller. ModelManager in — ModelManager in is a reference to the model manager on the VeriStand Gateway. You must open a reference to the model manager to use this parameter. Parameters — Parameters specifies the parameters whose values you want to set. Values — Values specifies the values to set. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. ModelManager out — ModelManager out is a reference to the model manager on the VeriStand Gateway. You can wire this output to other Models VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI VeriStand - Set Parameter Value VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/modelmanager/ni-veristand-set-parameter-2d-array-values-vi.html language=enus -->
## TOPIC 00326: NI VeriStand - Set Parameter 2D Array Values VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/modelmanager/ni-veristand-set-parameter-2d-array-values-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/modelmanager/ni-veristand-set-parameter-2d-array-values-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets values of model parameters present on the target. You must manually select the polymorphic instance to use. Sets the vector values of a single model parameter present on the target. icon Inputs/Outputs cstr.png Target Target specifies the name of the target on which the models are running. This

### NI VeriStand - Set Parameter 2D Array Values VI

Sets values of model parameters present on the target. You must manually select the polymorphic instance to use.

Note

[IMAGE alt='icon' src='ni-veristand-set-parameter-2d-array-values-vi.png']

#### Inputs/Outputs

| Target — Target specifies the name of the target on which the models are running. This input expects the name of the target as specified in the System Explorer window. For example: Controller. ModelManager in — ModelManager in is a reference to the model manager on the VeriStand Gateway. You must open a reference to the model manager to use this parameter. Parameter — Parameter specifies the parameter whose value you want to set. Values — Values specifies the values to set. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. ModelManager out — ModelManager out is a reference to the model manager on the VeriStand Gateway. You can wire this output to other Models VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI VeriStand - Set Parameter Value VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/modelmanager/ni-veristand-set-parameter-value-vi.html language=enus -->
## TOPIC 00327: NI VeriStand - Set Parameter Value VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/modelmanager/ni-veristand-set-parameter-value-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/modelmanager/ni-veristand-set-parameter-value-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets values of model parameters present on the target. You must manually select the polymorphic instance to use. icon

### NI VeriStand - Set Parameter Value VI

Sets values of model parameters present on the target. You must manually select the polymorphic instance to use.

[IMAGE alt='icon' src='ni-veristand-set-parameter-value-vi.png']

- [NI VeriStand - Set Single Parameter Value VI](../../../../vi-lib/ni-veristand/execution/modelmanager/ni-veristand-set-single-parameter-value-vi.html) Sets values of model parameters present on the target. You must manually select the polymorphic instance to use.
- [NI VeriStand - Set Multiple Parameter Values VI](../../../../vi-lib/ni-veristand/execution/modelmanager/ni-veristand-set-multiple-parameter-values-vi.html) Sets values of model parameters present on the target. You must manually select the polymorphic instance to use.
- [NI VeriStand - Set Parameter 2D Array Values VI](../../../../vi-lib/ni-veristand/execution/modelmanager/ni-veristand-set-parameter-2d-array-values-vi.html) Sets values of model parameters present on the target. You must manually select the polymorphic instance to use.
- [NI VeriStand - Set Multiple Parameter 2D Array Values VI](../../../../vi-lib/ni-veristand/execution/modelmanager/ni-veristand-set-multiple-parameter-2d-array-values-vi.html) Sets values of model parameters present on the target. You must manually select the polymorphic instance to use.

Parent topic:

Models

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/modelmanager/ni-veristand-set-single-parameter-value-vi.html language=enus -->
## TOPIC 00328: NI VeriStand - Set Single Parameter Value VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/modelmanager/ni-veristand-set-single-parameter-value-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/modelmanager/ni-veristand-set-single-parameter-value-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets values of model parameters present on the target. You must manually select the polymorphic instance to use. icon Inputs/Outputs cstr.png Target Target specifies the name of the target on which the models are running. This input expects the name of the target as specified in the System Explorer

### NI VeriStand - Set Single Parameter Value VI

Sets values of model parameters present on the target. You must manually select the polymorphic instance to use.

[IMAGE alt='icon' src='ni-veristand-set-single-parameter-value-vi.png']

#### Inputs/Outputs

| Target — Target specifies the name of the target on which the models are running. This input expects the name of the target as specified in the System Explorer window. For example: Controller. ModelManager in — ModelManager in is a reference to the model manager on the VeriStand Gateway. You must open a reference to the model manager to use this parameter. Parameter — Parameter specifies the parameter whose value you want to set. Value — Value specifies the value to set. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. ModelManager out — ModelManager out is a reference to the model manager on the VeriStand Gateway. You can wire this output to other Models VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI VeriStand - Set Parameter Value VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/project/ni-veristand-close-project-reference-vi.html language=unavailable -->
## TOPIC 00329: Ni Veristand Close Project Reference Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/project/ni-veristand-close-project-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/project/ni-veristand-close-project-reference-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/project/ni-veristand-close-project-vi.html language=unavailable -->
## TOPIC 00330: Ni Veristand Close Project Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/project/ni-veristand-close-project-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/project/ni-veristand-close-project-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/project/ni-veristand-close-workspace-window-vi.html language=enus -->
## TOPIC 00331: NI VeriStand - Close Workspace Window VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/project/ni-veristand-close-workspace-window-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/project/ni-veristand-close-workspace-window-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the Workspace window for an NI VeriStand project. icon Inputs/Outputs cgnrn.png Project Ref in Project Ref in is the reference to the NI VeriStand project. Use the Open Project Reference VI to get this reference. cerrcodeclst.png error in (no error) error in describes error conditions that oc

### NI VeriStand - Close Workspace Window VI

Closes the **Workspace** window for an NI VeriStand project.

[IMAGE alt='icon' src='ni-veristand-close-workspace-window-vi.png']

#### Inputs/Outputs

| Project Ref in — Project Ref in is the reference to the NI VeriStand project. Use the Open Project Reference VI to get this reference. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Project Ref out — Project Ref out returns the reference to the NI VeriStand project. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Workspace Automation

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/project/ni-veristand-connect-project-vi.html language=enus -->
## TOPIC 00332: NI VeriStand - Connect Project VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/project/ni-veristand-connect-project-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/project/ni-veristand-connect-project-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connects an NI VeriStand project on the host computer to a target. This VI only establishes a connection to a target. It does not deploy the system definition file. Use the Deploy Project VI to deploy a system definition file to the target. icon Inputs/Outputs cgnrn.png Project Ref in Project Ref in

### NI VeriStand - Connect Project VI

Connects an NI VeriStand project on the host computer to a target. This VI only establishes a connection to a target. It does not deploy the system definition file. Use the Deploy Project VI to deploy a system definition file to the target.

[IMAGE alt='icon' src='ni-veristand-connect-project-vi.png']

#### Inputs/Outputs

| Project Ref in — Project Ref in is the reference to the NI VeriStand project. Use the Open Project Reference VI to get this reference. Show Progress (F) — Show Progress specifies whether to display a progress dialog. The default is FALSE, or no dialog. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Project Ref out — Project Ref out returns the reference to the NI VeriStand project. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Execution

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/project/ni-veristand-deploy-project-vi.html language=unavailable -->
## TOPIC 00333: Ni Veristand Deploy Project Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/project/ni-veristand-deploy-project-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/project/ni-veristand-deploy-project-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/project/ni-veristand-disconnect-project-vi.html language=enus -->
## TOPIC 00334: NI VeriStand - Disconnect Project VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/project/ni-veristand-disconnect-project-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/project/ni-veristand-disconnect-project-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disconnects an NI VeriStand project from the target. This VI does not stop execution of the system definition file on the target. If you want to stop execution, use the Undeploy Project VI. icon Inputs/Outputs cgnrn.png Project Ref in Project Ref in is the reference to the NI VeriStand project. Use

### NI VeriStand - Disconnect Project VI

Disconnects an NI VeriStand project from the target. This VI does not stop execution of the system definition file on the target. If you want to stop execution, use the Undeploy Project VI.

[IMAGE alt='icon' src='ni-veristand-disconnect-project-vi.png']

#### Inputs/Outputs

| Project Ref in — Project Ref in is the reference to the NI VeriStand project. Use the Open Project Reference VI to get this reference. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Project Ref out — Project Ref out returns the reference to the NI VeriStand project. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Execution

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/project/ni-veristand-open-project-reference-vi.html language=enus -->
## TOPIC 00335: NI VeriStand - Open Project Reference VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/project/ni-veristand-open-project-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/project/ni-veristand-open-project-reference-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a reference to an NI VeriStand project. icon Inputs/Outputs cpath.png Project File Path Project File Path specifies the path to the project (.nivsproj) file for the project. cstr.png Gateway IP Address ("": localhost) Gateway IP Address specifies the IP address of the VeriStand Gateway. This a

### NI VeriStand - Open Project Reference VI

Opens a reference to an NI VeriStand project.

[IMAGE alt='icon' src='ni-veristand-open-project-reference-vi.png']

#### Inputs/Outputs

| Project File Path — Project File Path specifies the path to the project (.nivsproj) file for the project. Gateway IP Address ("": localhost) — Gateway IP Address specifies the IP address of the VeriStand Gateway. This address can be in IP dot notation or it can be a hostname. If you do not specify an address, LabVIEW establishes a connection to the local computer. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Username — Username specifies the username to use to access the project. Password — Password specifies the password of the user account. Project Ref — Project Ref returns the reference to the NI VeriStand project. You can use this reference with the rest of the Project VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Project

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/project/ni-veristand-open-workspace-tool-vi.html language=enus -->
## TOPIC 00336: NI VeriStand - Open Workspace Tool VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/project/ni-veristand-open-workspace-tool-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/project/ni-veristand-open-workspace-tool-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a Workspace tool for an NI VeriStand project. icon Inputs/Outputs cpath.png Workspace Tool Path Workspace Tool Path specifies the path to the tool VI. cgnrn.png Project Ref in Project Ref in is the reference to the NI VeriStand project. Use the Open Project Reference VI to get this reference.

### NI VeriStand - Open Workspace Tool VI

Opens a Workspace tool for an NI VeriStand project.

[IMAGE alt='icon' src='ni-veristand-open-workspace-tool-vi.png']

#### Inputs/Outputs

| Workspace Tool Path — Workspace Tool Path specifies the path to the tool VI. Project Ref in — Project Ref in is the reference to the NI VeriStand project. Use the Open Project Reference VI to get this reference. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Project Ref out — Project Ref out returns the reference to the NI VeriStand project. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Workspace Automation

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/project/ni-veristand-open-workspace-window-vi.html language=enus -->
## TOPIC 00337: NI VeriStand - Open Workspace Window VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/project/ni-veristand-open-workspace-window-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/project/ni-veristand-open-workspace-window-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens the Workspace window for an NI VeriStand project. icon Inputs/Outputs cgnrn.png Project Ref in Project Ref in is the reference to the NI VeriStand project. Use the Open Project Reference VI to get this reference. cerrcodeclst.png error in (no error) error in describes error conditions that occ

### NI VeriStand - Open Workspace Window VI

Opens the **Workspace** window for an NI VeriStand project.

[IMAGE alt='icon' src='ni-veristand-open-workspace-window-vi.png']

#### Inputs/Outputs

| Project Ref in — Project Ref in is the reference to the NI VeriStand project. Use the Open Project Reference VI to get this reference. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Project Ref out — Project Ref out returns the reference to the NI VeriStand project. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Workspace Automation

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/project/ni-veristand-quit-application-vi.html language=unavailable -->
## TOPIC 00338: Ni Veristand Quit Application Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/project/ni-veristand-quit-application-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/project/ni-veristand-quit-application-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/project/ni-veristand-run-project-vi.html language=enus -->
## TOPIC 00339: NI VeriStand - Run Project VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/project/ni-veristand-run-project-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/project/ni-veristand-run-project-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Runs an NI VeriStand project. icon Inputs/Outputs cgnrn.png Project Ref in Project Ref in is the reference to the NI VeriStand project. Use the Open Project Reference VI to get this reference. cbool.png Show Progress (F) Show Progress specifies whether to display a progress dialog. The default is FA

### NI VeriStand - Run Project VI

Runs an NI VeriStand project.

[IMAGE alt='icon' src='ni-veristand-run-project-vi.png']

#### Inputs/Outputs

| Project Ref in — Project Ref in is the reference to the NI VeriStand project. Use the Open Project Reference VI to get this reference. Show Progress (F) — Show Progress specifies whether to display a progress dialog. The default is FALSE, or no dialog. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Project Ref out — Project Ref out returns the reference to the NI VeriStand project. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Execution

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/project/ni-veristand-send-workspace-tool-message-byte-array-vi.html language=unavailable -->
## TOPIC 00340: Ni Veristand Send Workspace Tool Message Byte Array Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/project/ni-veristand-send-workspace-tool-message-byte-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/project/ni-veristand-send-workspace-tool-message-byte-array-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/project/ni-veristand-send-workspace-tool-message-string-vi.html language=enus -->
## TOPIC 00341: NI VeriStand - Send Workspace Tool Message (String) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/project/ni-veristand-send-workspace-tool-message-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/project/ni-veristand-send-workspace-tool-message-string-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a message or command to a Workspace tool for an NI VeriStand project, as well as data required by the case that handles the command. You can use this method with any Workspace tool that registers to receive the command you specify. icon Inputs/Outputs cpath.png Workspace Tool Path Workspace To

### NI VeriStand - Send Workspace Tool Message (String) VI

Sends a message or command to a Workspace tool for an NI VeriStand project, as well as data required by the case that handles the command. You can use this method with any Workspace tool that registers to receive the command you specify.

[IMAGE alt='icon' src='ni-veristand-send-workspace-tool-message-string-vi.png']

#### Inputs/Outputs

| Workspace Tool Path — Workspace Tool Path specifies the path to the tool VI. Project Ref in — Project Ref in is the reference to the NI VeriStand project. Use the Open Project Reference VI to get this reference. Command — Command specifies the message or command to send. Data — Data specifies any data required by the case of the workspace tool that handles the Command. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Timeout ms (10000) — Timeout ms specifies the time in milliseconds that the VI waits for a response from the tool before returning an error. The default is 10,000. Project Ref out — Project Ref out returns the reference to the NI VeriStand project. response — response returns the response from the tool to the Command. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI VeriStand - Send Workspace Tool Message VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/project/ni-veristand-send-workspace-tool-message-vi.html language=enus -->
## TOPIC 00342: NI VeriStand - Send Workspace Tool Message VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/project/ni-veristand-send-workspace-tool-message-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/project/ni-veristand-send-workspace-tool-message-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a message or command to a Workspace tool for an NI VeriStand project, as well as data required by the case that handles the command. You can use this method with any Workspace tool that registers to receive the command you specify. icon

### NI VeriStand - Send Workspace Tool Message VI

Sends a message or command to a Workspace tool for an NI VeriStand project, as well as data required by the case that handles the command. You can use this method with any Workspace tool that registers to receive the command you specify.

[IMAGE alt='icon' src='ni-veristand-send-workspace-tool-message-vi.png']

- [NI VeriStand - Send Workspace Tool Message (String) VI](../../../../vi-lib/ni-veristand/execution/project/ni-veristand-send-workspace-tool-message-string-vi.html) Sends a message or command to a Workspace tool for an NI VeriStand project, as well as data required by the case that handles the command. You can use this method with any Workspace tool that registers to receive the command you specify.
- [NI VeriStand - Send Workspace Tool Message (Byte Array) VI](../../../../vi-lib/ni-veristand/execution/project/ni-veristand-send-workspace-tool-message-byte-array-vi.html) Sends a message or command to a Workspace tool for an NI VeriStand project, as well as data required by the case that handles the command. You can use this method with any Workspace tool that registers to receive the command you specify.

Parent topic:

Workspace Automation

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/project/ni-veristand-undeploy-project-vi.html language=enus -->
## TOPIC 00343: NI VeriStand - Undeploy Project VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/project/ni-veristand-undeploy-project-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/project/ni-veristand-undeploy-project-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Undeploys the system definition file associated with an NI VeriStand project from the target. Undeploying the system definition file stops execution on the target. icon Inputs/Outputs cgnrn.png Project Ref in Project Ref in is the reference to the NI VeriStand project. Use the Open Project Reference

### NI VeriStand - Undeploy Project VI

Undeploys the system definition file associated with an NI VeriStand project from the target. Undeploying the system definition file stops execution on the target.

[IMAGE alt='icon' src='ni-veristand-undeploy-project-vi.png']

#### Inputs/Outputs

| Project Ref in — Project Ref in is the reference to the NI VeriStand project. Use the Open Project Reference VI to get this reference. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Project Ref out — Project Ref out returns the reference to the NI VeriStand project. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Execution

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/abort-sequence-vi.html language=unavailable -->
## TOPIC 00344: Abort Sequence Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/abort-sequence-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/abort-sequence-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/abort-stimulus-profile-session-vi.html language=enus -->
## TOPIC 00345: Abort Stimulus Profile Session VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/abort-stimulus-profile-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/abort-stimulus-profile-session-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Aborts an NI VeriStand stimulus profile session and all the real-time sequences it contains. This VI immediately terminates sequence execution, without performing any clean-up tasks. To perform clean-up tasks, use the Stop Stimulus Profile Session VI instead. You can use the Abort Sequence VI to abo

### Abort Stimulus Profile Session VI

Aborts an NI VeriStand stimulus profile session and all the real-time sequences it contains. This VI immediately terminates sequence execution, without performing any clean-up tasks. To perform clean-up tasks, use the Stop Stimulus Profile Session VI instead.

Tip

[IMAGE alt='icon' src='abort-stimulus-profile-session-vi.png']

#### Inputs/Outputs

| Session Ref in — Session Ref in is a reference to the stimulus profile session. A session is a group of top-level sequences that are deployed and started together. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Session Ref out — Session Ref out returns a reference to the stimulus profile session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Session Control

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-call-vi.html language=unavailable -->
## TOPIC 00346: Create Sequence Call Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-call-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-call-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-boolean-array-vi.html language=enus -->
## TOPIC 00347: Create Sequence Parameter Assignment (Boolean Array) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-boolean-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-boolean-array-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. Wire data to the Channel input to determine the

### Create Sequence Parameter Assignment (Boolean Array) VI

Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. 

Wire data to the **Channel** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='create-sequence-parameter-assignment-boolean-array-vi.png']

#### Inputs/Outputs

| Parameter Name — Parameter Name specifies the name of the parameter to assign the value. Value — Value specifies the value to assign. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Sequence Parameter Assignment Ref — Sequence Parameter Assignment Ref returns a reference to the parameter assignment. You can use this reference with the Create Sequence Call VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Create Sequence Parameter Assignment VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-boolean-vi.html language=unavailable -->
## TOPIC 00348: Create Sequence Parameter Assignment Boolean Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-boolean-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-boolean-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-channel-vi.html language=enus -->
## TOPIC 00349: Create Sequence Parameter Assignment (Channel) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-channel-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-channel-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. Wire data to the Channel input to determine the

### Create Sequence Parameter Assignment (Channel) VI

Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. 

Wire data to the **Channel** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='create-sequence-parameter-assignment-channel-vi.png']

#### Inputs/Outputs

| Parameter Name — Parameter Name specifies the name of the parameter to assign the value. Channel — Channel specifies the channel to map to the parameter. You can enter a fully qualified channel path or a path to an alias. For example, Targets/Controller/Simulation Models/Models/delay_random/Inports/In1 or Aliases/In1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Sequence Parameter Assignment Ref — Sequence Parameter Assignment Ref returns a reference to the parameter assignment. You can use this reference with the Create Sequence Call VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Create Sequence Parameter Assignment VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-double-array-vi.html language=enus -->
## TOPIC 00350: Create Sequence Parameter Assignment (Double Array) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-double-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-double-array-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. Wire data to the Channel input to determine the

### Create Sequence Parameter Assignment (Double Array) VI

Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. 

Wire data to the **Channel** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='create-sequence-parameter-assignment-double-array-vi.png']

#### Inputs/Outputs

| Parameter Name — Parameter Name specifies the name of the parameter to assign the value. Value — Value specifies the value to assign. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Sequence Parameter Assignment Ref — Sequence Parameter Assignment Ref returns a reference to the parameter assignment. You can use this reference with the Create Sequence Call VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Create Sequence Parameter Assignment VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-double-vi.html language=enus -->
## TOPIC 00351: Create Sequence Parameter Assignment (Double) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-double-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-double-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. Wire data to the Channel input to determine the

### Create Sequence Parameter Assignment (Double) VI

Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. 

Wire data to the **Channel** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='create-sequence-parameter-assignment-double-vi.png']

#### Inputs/Outputs

| Parameter Name — Parameter Name specifies the name of the parameter to assign the value. Value — Value specifies the value to assign. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Sequence Parameter Assignment Ref — Sequence Parameter Assignment Ref returns a reference to the parameter assignment. You can use this reference with the Create Sequence Call VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Create Sequence Parameter Assignment VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-i32-array-vi.html language=unavailable -->
## TOPIC 00352: Create Sequence Parameter Assignment I32 Array Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-i32-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-i32-array-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-i32-vi.html language=unavailable -->
## TOPIC 00353: Create Sequence Parameter Assignment I32 Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-i32-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-i32-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-i64-array-vi.html language=enus -->
## TOPIC 00354: Create Sequence Parameter Assignment (I64 Array) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-i64-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-i64-array-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. Wire data to the Channel input to determine the

### Create Sequence Parameter Assignment (I64 Array) VI

Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. 

Wire data to the **Channel** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='create-sequence-parameter-assignment-i64-array-vi.png']

#### Inputs/Outputs

| Parameter Name — Parameter Name specifies the name of the parameter to assign the value. Value — Value specifies the value to assign. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Sequence Parameter Assignment Ref — Sequence Parameter Assignment Ref returns a reference to the parameter assignment. You can use this reference with the Create Sequence Call VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Create Sequence Parameter Assignment VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-i64-vi.html language=enus -->
## TOPIC 00355: Create Sequence Parameter Assignment (I64) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-i64-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-i64-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. Wire data to the Channel input to determine the

### Create Sequence Parameter Assignment (I64) VI

Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. 

Wire data to the **Channel** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='create-sequence-parameter-assignment-i64-vi.png']

#### Inputs/Outputs

| Parameter Name — Parameter Name specifies the name of the parameter to assign the value. Value — Value specifies the value to assign. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Sequence Parameter Assignment Ref — Sequence Parameter Assignment Ref returns a reference to the parameter assignment. You can use this reference with the Create Sequence Call VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Create Sequence Parameter Assignment VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-imported-double-array-vi.html language=enus -->
## TOPIC 00356: Create Sequence Parameter Assignment (Imported Double Array) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-imported-double-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-imported-double-array-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. Wire data to the Channel input to determine the

### Create Sequence Parameter Assignment (Imported Double Array) VI

Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. 

Wire data to the **Channel** input to determine the polymorphic instance to use or manually select the instance.

Note

ni.com/dataplugins

[IMAGE alt='icon' src='create-sequence-parameter-assignment-imported-double-array-vi.png']

#### Inputs/Outputs

| File Path — File Path--Specifies the path of the file from which to import values. Parameter Name — Parameter Name specifies the name of the parameter to assign the value. Channel Group — Channel Group specifies the name of the group in the import file that contains the Channel whose data you want to import. If the file type does not support groups or an equivalent container, refer to documentation for the DataPlugin or contact its creator to determine how to identify group names. Channel — Channel specifies the name of the channel in the import file that contains the data you want to imported. In some file types, column headers serve as channel names. For other file types, refer to documentation for the DataPlugin or contact its creator to determine how to identify channel names. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Import Offset (0) — Import Offset specifies the index of the first sample in the Channel you want to import. The default is 0. Import Length (0: import rest) — Import Length specifies the number of values to import from the file, starting at the Import Offset index. The default, 0, specifies to import all data in the file that exists after the Import Offset. Sequence Parameter Assignment Ref — Sequence Parameter Assignment Ref returns a reference to the parameter assignment. You can use this reference with the Create Sequence Call VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Create Sequence Parameter Assignment VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-u32-array-vi.html language=unavailable -->
## TOPIC 00357: Create Sequence Parameter Assignment U32 Array Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-u32-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-u32-array-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-u32-vi.html language=enus -->
## TOPIC 00358: Create Sequence Parameter Assignment (U32) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-u32-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-u32-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. Wire data to the Channel input to determine the

### Create Sequence Parameter Assignment (U32) VI

Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. 

Wire data to the **Channel** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='create-sequence-parameter-assignment-u32-vi.png']

#### Inputs/Outputs

| Parameter Name — Parameter Name specifies the name of the parameter to assign the value. Value — Value specifies the value to assign. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Sequence Parameter Assignment Ref — Sequence Parameter Assignment Ref returns a reference to the parameter assignment. You can use this reference with the Create Sequence Call VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Create Sequence Parameter Assignment VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-u64-array-vi.html language=unavailable -->
## TOPIC 00359: Create Sequence Parameter Assignment U64 Array Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-u64-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-u64-array-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-u64-vi.html language=unavailable -->
## TOPIC 00360: Create Sequence Parameter Assignment U64 Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-u64-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-u64-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-vi.html language=enus -->
## TOPIC 00361: Create Sequence Parameter Assignment VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. Wire data to the Channel input to determine the

### Create Sequence Parameter Assignment VI

Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. 

Wire data to the **Channel** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='create-sequence-parameter-assignment-vi.png']

- [Create Sequence Parameter Assignment (Channel) VI](../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-channel-vi.html) Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. Wire data to the Channel input to determine the polymorphic instance to use or manually select the instance.
- [Create Sequence Parameter Assignment (Boolean) VI](../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-boolean-vi.html) Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. Wire data to the Channel input to determine the polymorphic instance to use or manually select the instance.
- [Create Sequence Parameter Assignment (Boolean Array) VI](../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-boolean-array-vi.html) Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. Wire data to the Channel input to determine the polymorphic instance to use or manually select the instance.
- [Create Sequence Parameter Assignment (Double) VI](../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-double-vi.html) Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. Wire data to the Channel input to determine the polymorphic instance to use or manually select the instance.
- [Create Sequence Parameter Assignment (Double Array) VI](../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-double-array-vi.html) Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. Wire data to the Channel input to determine the polymorphic instance to use or manually select the instance.
- [Create Sequence Parameter Assignment (I32) VI](../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-i32-vi.html) Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. Wire data to the Channel input to determine the polymorphic instance to use or manually select the instance.
- [Create Sequence Parameter Assignment (I32 Array) VI](../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-i32-array-vi.html) Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. Wire data to the Channel input to determine the polymorphic instance to use or manually select the instance.
- [Create Sequence Parameter Assignment (I64) VI](../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-i64-vi.html) Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. Wire data to the Channel input to determine the polymorphic instance to use or manually select the instance.
- [Create Sequence Parameter Assignment (I64 Array) VI](../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-i64-array-vi.html) Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. Wire data to the Channel input to determine the polymorphic instance to use or manually select the instance.
- [Create Sequence Parameter Assignment (U32) VI](../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-u32-vi.html) Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. Wire data to the Channel input to determine the polymorphic instance to use or manually select the instance.
- [Create Sequence Parameter Assignment (U32 Array) VI](../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-u32-array-vi.html) Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. Wire data to the Channel input to determine the polymorphic instance to use or manually select the instance.
- [Create Sequence Parameter Assignment (U64) VI](../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-u64-vi.html) Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. Wire data to the Channel input to determine the polymorphic instance to use or manually select the instance.
- [Create Sequence Parameter Assignment (U64 Array) VI](../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-u64-array-vi.html) Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. Wire data to the Channel input to determine the polymorphic instance to use or manually select the instance.
- [Create Sequence Parameter Assignment (Imported Double Array) VI](../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-imported-double-array-vi.html) Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. Wire data to the Channel input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Stimulus Profile

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/data-value-ref-to-variant-vi.html language=enus -->
## TOPIC 00362: Data Value Ref to Variant VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/data-value-ref-to-variant-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/data-value-ref-to-variant-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Translates the data value reference returned by the Get Sequence Return Value VI or a sequence complete event into a LabVIEW variant data type that corresponds to the data type of the sequence return value. Return values are declared by real-time sequences, and generally indicate some type of pass/f

### Data Value Ref to Variant VI

Translates the data value reference returned by the Get Sequence Return Value VI or a sequence complete event into a LabVIEW variant data type that corresponds to the data type of the sequence return value.

Note

[IMAGE alt='icon' src='data-value-ref-to-variant-vi.png']

#### Inputs/Outputs

| Data Value Ref — Data Value Ref specifies a data value reference. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Data Value Ref out — Data Value Ref out returns the data value reference. Variant — Variant returns the data value reference as LabVIEW variant data. Type Descriptor — Type Descriptor describes the data type of a parameter or return value. Data Type — Data Type returns the data type of the parameter or return value. 0 Void—Indicates that the parameter or return value has a void or empty data type. Typically, this indicates that a sequence has no relevant data to return. 1 Boolean—Indicates the parameter or return value is a Boolean. 2 Int32—Indicates the parameter or return value is a 32-bit signed integer. 3 UInt32—Indicates the parameter or return value is a 32-bit unsigned integer. 4 Int64—Indicates the parameter or return value is a 64-bit signed integer. 5 UInt64—Indicates the parameter or return value is a 64-bit unsigned integer. 6 Double—Indicates the parameter or return value is a double-precision floating point number. 7 Array—Indicates the parameter or return value is an array. Child Type Indices — Child Type Indices--Returns the indices of any child elements of the parameter or return value. This array is empty unless Data Type is a type that is capable of containing child elements, such as Array. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Data Type — Data Type returns the data type of the parameter or return value. 0 Void—Indicates that the parameter or return value has a void or empty data type. Typically, this indicates that a sequence has no relevant data to return. 1 Boolean—Indicates the parameter or return value is a Boolean. 2 Int32—Indicates the parameter or return value is a 32-bit signed integer. 3 UInt32—Indicates the parameter or return value is a 32-bit unsigned integer. 4 Int64—Indicates the parameter or return value is a 64-bit signed integer. 5 UInt64—Indicates the parameter or return value is a 64-bit unsigned integer. 6 Double—Indicates the parameter or return value is a double-precision floating point number. 7 Array—Indicates the parameter or return value is an array. Child Type Indices — Child Type Indices--Returns the indices of any child elements of the parameter or return value. This array is empty unless Data Type is a type that is capable of containing child elements, such as Array. |  |
| 0 | Void—Indicates that the parameter or return value has a void or empty data type. Typically, this indicates that a sequence has no relevant data to return. |
| 1 | Boolean—Indicates the parameter or return value is a Boolean. |
| 2 | Int32—Indicates the parameter or return value is a 32-bit signed integer. |
| 3 | UInt32—Indicates the parameter or return value is a 32-bit unsigned integer. |
| 4 | Int64—Indicates the parameter or return value is a 64-bit signed integer. |
| 5 | UInt64—Indicates the parameter or return value is a 64-bit unsigned integer. |
| 6 | Double—Indicates the parameter or return value is a double-precision floating point number. |
| 7 | Array—Indicates the parameter or return value is an array. |

Parent topic:

Utilities

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/deploy-stimulus-profile-session-vi.html language=unavailable -->
## TOPIC 00363: Deploy Stimulus Profile Session Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/deploy-stimulus-profile-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/deploy-stimulus-profile-session-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-all-deployed-stimulus-profile-sessions-vi.html language=enus -->
## TOPIC 00364: Get All Deployed Stimulus Profile Sessions VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-all-deployed-stimulus-profile-sessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-all-deployed-stimulus-profile-sessions-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the VeriStand Gateway and returns a list of all currently deployed stimulus profile sessions. icon Inputs/Outputs cstr.png Gateway IP Address ("": localhost) Gateway IP Address specifies the IP address of the VeriStand Gateway. This address can be in IP dot notation or it can be a hostname.

### Get All Deployed Stimulus Profile Sessions VI

Queries the VeriStand Gateway and returns a list of all currently deployed stimulus profile sessions.

[IMAGE alt='icon' src='get-all-deployed-stimulus-profile-sessions-vi.png']

#### Inputs/Outputs

| Gateway IP Address ("": localhost) — Gateway IP Address specifies the IP address of the VeriStand Gateway. This address can be in IP dot notation or it can be a hostname. If you do not specify an address, LabVIEW establishes a connection to the local computer. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Deployed Session IDs — Deployed Session IDs returns a list of IDs and information about all currently deployed stimulus profile sessions. ID — ID returns the session ID. You can use this value with the Open Deployed Stimulus Profile Session VI to open the session. Name — Name returns the session name. Description — Description returns the session description. Sequences — Sequences returns all the sequences in the session. Name — Name returns the name of the sequence. Path — Path returns the path to the sequence file. Target — Target returns the target to which the sequence is deployed. State — State indicates the current state of the sequence. 0 Idle—Indicates the sequence is idle. 1 Running—Indicates the sequence is running. 2 SingleStepping—Indicates the sequence is single-stepping. 3 Paused—Indicates the sequence is paused. 4 Stopped—Indicates the sequence is stopped. Locked — Locked indicates whether the session is locked with a password. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| ID — ID returns the session ID. You can use this value with the Open Deployed Stimulus Profile Session VI to open the session. Name — Name returns the session name. Description — Description returns the session description. Sequences — Sequences returns all the sequences in the session. Name — Name returns the name of the sequence. Path — Path returns the path to the sequence file. Target — Target returns the target to which the sequence is deployed. State — State indicates the current state of the sequence. 0 Idle—Indicates the sequence is idle. 1 Running—Indicates the sequence is running. 2 SingleStepping—Indicates the sequence is single-stepping. 3 Paused—Indicates the sequence is paused. 4 Stopped—Indicates the sequence is stopped. Locked — Locked indicates whether the session is locked with a password. |  |
| Name — Name returns the name of the sequence. Path — Path returns the path to the sequence file. Target — Target returns the target to which the sequence is deployed. State — State indicates the current state of the sequence. 0 Idle—Indicates the sequence is idle. 1 Running—Indicates the sequence is running. 2 SingleStepping—Indicates the sequence is single-stepping. 3 Paused—Indicates the sequence is paused. 4 Stopped—Indicates the sequence is stopped. |  |
| 0 | Idle—Indicates the sequence is idle. |
| 1 | Running—Indicates the sequence is running. |
| 2 | SingleStepping—Indicates the sequence is single-stepping. |
| 3 | Paused—Indicates the sequence is paused. |
| 4 | Stopped—Indicates the sequence is stopped. |

Parent topic:

Stimulus Profile

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-all-sequence-names-vi.html language=enus -->
## TOPIC 00365: Get All Sequence Names VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-all-sequence-names-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-all-sequence-names-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of sequence names for all the real-time sequences in an NI VeriStand stimulus profile session. icon Inputs/Outputs cgnrn.png Session Ref in Session Ref in is a reference to the stimulus profile session. A session is a group of top-level sequences that are deployed and started together

### Get All Sequence Names VI

Returns a list of sequence names for all the real-time sequences in an NI VeriStand stimulus profile session.

[IMAGE alt='icon' src='get-all-sequence-names-vi.png']

#### Inputs/Outputs

| Session Ref in — Session Ref in is a reference to the stimulus profile session. A session is a group of top-level sequences that are deployed and started together. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Session Ref out — Session Ref out returns a reference to the stimulus profile session. Sequence Names out — Sequence Names out returns the names of the sequences. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Sequence Control

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-sequence-call-info-vi.html language=enus -->
## TOPIC 00366: Get Sequence Call Info VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-sequence-call-info-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-sequence-call-info-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a sequence call refnum for a real-time sequence in an NI VeriStand stimulus profile session. icon Inputs/Outputs cgnrn.png Session Ref in Session Ref in is a reference to the stimulus profile session. A session is a group of top-level sequences that are deployed and started together. cstr.pn

### Get Sequence Call Info VI

Returns a sequence call refnum for a real-time sequence in an NI VeriStand stimulus profile session.

[IMAGE alt='icon' src='get-sequence-call-info-vi.png']

#### Inputs/Outputs

| Session Ref in — Session Ref in is a reference to the stimulus profile session. A session is a group of top-level sequences that are deployed and started together. Sequence Name — Sequence Name specifies the name of the sequence. When operating on an individual sequence, the sequence must be specified by name. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Session Ref out — Session Ref out returns a reference to the stimulus profile session. Sequence Name out — Sequence Name out returns the name of the sequence. Sequence Call Ref — Sequence Call Ref returns a reference to the sequence call. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Sequence Control

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-sequence-info-vi.html language=enus -->
## TOPIC 00367: Get Sequence Info VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-sequence-info-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-sequence-info-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns information about a sequence in a stimulus profile session. icon Inputs/Outputs cpath.png Sequence File Path in Sequence File Path in specifies the path to the sequence. cerrcodeclst.png error in (no error) error in describes error conditions that occur before this node runs. This input prov

### Get Sequence Info VI

Returns information about a sequence in a stimulus profile session.

[IMAGE alt='icon' src='get-sequence-info-vi.png']

#### Inputs/Outputs

| Sequence File Path in — Sequence File Path in specifies the path to the sequence. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Description — Description returns the description of the parameter. Sequence File Path out — Sequence File Path out returns the path to the sequence. Parameters — Parameters returns an array of information about each input parameter in the sequence. Variable Info — Variable Info contains identification and type information for the parameter. Identifier — Identifier returns the ID of the input parameter. Default Value — Default Value indicates the default value of the parameter. Description — Description returns the description of the parameter. Units — Units returns the units associated with the parameter. Type Descriptor — Type Descriptor describes the data type of a parameter or return value. Data Type — Data Type returns the data type of the parameter or return value. 0 Void—Indicates that the parameter or return value has a void or empty data type. Typically, this indicates that a sequence has no relevant data to return. 1 Boolean—Indicates the parameter or return value is a Boolean. 2 Int32—Indicates the parameter or return value is a 32-bit signed integer. 3 UInt32—Indicates the parameter or return value is a 32-bit unsigned integer. 4 Int64—Indicates the parameter or return value is a 64-bit signed integer. 5 UInt64—Indicates the parameter or return value is a 64-bit unsigned integer. 6 Double—Indicates the parameter or return value is a double-precision floating point number. 7 Array—Indicates the parameter or return value is an array. Child Type Indices — Child Type Indices--Returns the indices of any child elements of the parameter or return value. This array is empty unless Data Type is a type that is capable of containing child elements, such as Array. By Reference — By Reference is TRUE if the parameter is called by reference. Default Assignment — Default Assignment returns the parameter's default assignment. Return Variable — Return Variable returns the return value of the sequence. Return values generally indicate some type of pass/fail information. They can be of any data type. Identifier — Identifier returns the ID of the return value. Default Value — Default Value indicates the default value for the return value. Description — Description returns the description of the return value. Units — Units returns the units associated with the return value. Type Descriptor — Type Descriptor describes the data type of a parameter or return value. Data Type — Data Type returns the data type of the parameter or return value. 0 Void—Indicates that the parameter or return value has a void or empty data type. Typically, this indicates that a sequence has no relevant data to return. 1 Boolean—Indicates the parameter or return value is a Boolean. 2 Int32—Indicates the parameter or return value is a 32-bit signed integer. 3 UInt32—Indicates the parameter or return value is a 32-bit unsigned integer. 4 Int64—Indicates the parameter or return value is a 64-bit signed integer. 5 UInt64—Indicates the parameter or return value is a 64-bit unsigned integer. 6 Double—Indicates the parameter or return value is a double-precision floating point number. 7 Array—Indicates the parameter or return value is an array. Child Type Indices — Child Type Indices--Returns the indices of any child elements of the parameter or return value. This array is empty unless Data Type is a type that is capable of containing child elements, such as Array. error out — error out contains error information. This output provides standard error out functionality. Version — Version returns version information for the real-time sequence. Major — Major indicates the major version. Minor — Minor indicates the minor version. Fix — Fix specifies the fix version number. This number may increment for smaller changes, such as bug fixes. Build — Build specifies the build number. This number may increment to reflect nightly builds. |  |
| --- | --- |
| Variable Info — Variable Info contains identification and type information for the parameter. Identifier — Identifier returns the ID of the input parameter. Default Value — Default Value indicates the default value of the parameter. Description — Description returns the description of the parameter. Units — Units returns the units associated with the parameter. Type Descriptor — Type Descriptor describes the data type of a parameter or return value. Data Type — Data Type returns the data type of the parameter or return value. 0 Void—Indicates that the parameter or return value has a void or empty data type. Typically, this indicates that a sequence has no relevant data to return. 1 Boolean—Indicates the parameter or return value is a Boolean. 2 Int32—Indicates the parameter or return value is a 32-bit signed integer. 3 UInt32—Indicates the parameter or return value is a 32-bit unsigned integer. 4 Int64—Indicates the parameter or return value is a 64-bit signed integer. 5 UInt64—Indicates the parameter or return value is a 64-bit unsigned integer. 6 Double—Indicates the parameter or return value is a double-precision floating point number. 7 Array—Indicates the parameter or return value is an array. Child Type Indices — Child Type Indices--Returns the indices of any child elements of the parameter or return value. This array is empty unless Data Type is a type that is capable of containing child elements, such as Array. By Reference — By Reference is TRUE if the parameter is called by reference. Default Assignment — Default Assignment returns the parameter's default assignment. |  |
| Identifier — Identifier returns the ID of the input parameter. Default Value — Default Value indicates the default value of the parameter. Description — Description returns the description of the parameter. Units — Units returns the units associated with the parameter. Type Descriptor — Type Descriptor describes the data type of a parameter or return value. Data Type — Data Type returns the data type of the parameter or return value. 0 Void—Indicates that the parameter or return value has a void or empty data type. Typically, this indicates that a sequence has no relevant data to return. 1 Boolean—Indicates the parameter or return value is a Boolean. 2 Int32—Indicates the parameter or return value is a 32-bit signed integer. 3 UInt32—Indicates the parameter or return value is a 32-bit unsigned integer. 4 Int64—Indicates the parameter or return value is a 64-bit signed integer. 5 UInt64—Indicates the parameter or return value is a 64-bit unsigned integer. 6 Double—Indicates the parameter or return value is a double-precision floating point number. 7 Array—Indicates the parameter or return value is an array. Child Type Indices — Child Type Indices--Returns the indices of any child elements of the parameter or return value. This array is empty unless Data Type is a type that is capable of containing child elements, such as Array. |  |
| Data Type — Data Type returns the data type of the parameter or return value. 0 Void—Indicates that the parameter or return value has a void or empty data type. Typically, this indicates that a sequence has no relevant data to return. 1 Boolean—Indicates the parameter or return value is a Boolean. 2 Int32—Indicates the parameter or return value is a 32-bit signed integer. 3 UInt32—Indicates the parameter or return value is a 32-bit unsigned integer. 4 Int64—Indicates the parameter or return value is a 64-bit signed integer. 5 UInt64—Indicates the parameter or return value is a 64-bit unsigned integer. 6 Double—Indicates the parameter or return value is a double-precision floating point number. 7 Array—Indicates the parameter or return value is an array. Child Type Indices — Child Type Indices--Returns the indices of any child elements of the parameter or return value. This array is empty unless Data Type is a type that is capable of containing child elements, such as Array. |  |
| 0 | Void—Indicates that the parameter or return value has a void or empty data type. Typically, this indicates that a sequence has no relevant data to return. |
| 1 | Boolean—Indicates the parameter or return value is a Boolean. |
| 2 | Int32—Indicates the parameter or return value is a 32-bit signed integer. |
| 3 | UInt32—Indicates the parameter or return value is a 32-bit unsigned integer. |
| 4 | Int64—Indicates the parameter or return value is a 64-bit signed integer. |
| 5 | UInt64—Indicates the parameter or return value is a 64-bit unsigned integer. |
| 6 | Double—Indicates the parameter or return value is a double-precision floating point number. |
| 7 | Array—Indicates the parameter or return value is an array. |
| Identifier — Identifier returns the ID of the return value. Default Value — Default Value indicates the default value for the return value. Description — Description returns the description of the return value. Units — Units returns the units associated with the return value. Type Descriptor — Type Descriptor describes the data type of a parameter or return value. Data Type — Data Type returns the data type of the parameter or return value. 0 Void—Indicates that the parameter or return value has a void or empty data type. Typically, this indicates that a sequence has no relevant data to return. 1 Boolean—Indicates the parameter or return value is a Boolean. 2 Int32—Indicates the parameter or return value is a 32-bit signed integer. 3 UInt32—Indicates the parameter or return value is a 32-bit unsigned integer. 4 Int64—Indicates the parameter or return value is a 64-bit signed integer. 5 UInt64—Indicates the parameter or return value is a 64-bit unsigned integer. 6 Double—Indicates the parameter or return value is a double-precision floating point number. 7 Array—Indicates the parameter or return value is an array. Child Type Indices — Child Type Indices--Returns the indices of any child elements of the parameter or return value. This array is empty unless Data Type is a type that is capable of containing child elements, such as Array. |  |
| Data Type — Data Type returns the data type of the parameter or return value. 0 Void—Indicates that the parameter or return value has a void or empty data type. Typically, this indicates that a sequence has no relevant data to return. 1 Boolean—Indicates the parameter or return value is a Boolean. 2 Int32—Indicates the parameter or return value is a 32-bit signed integer. 3 UInt32—Indicates the parameter or return value is a 32-bit unsigned integer. 4 Int64—Indicates the parameter or return value is a 64-bit signed integer. 5 UInt64—Indicates the parameter or return value is a 64-bit unsigned integer. 6 Double—Indicates the parameter or return value is a double-precision floating point number. 7 Array—Indicates the parameter or return value is an array. Child Type Indices — Child Type Indices--Returns the indices of any child elements of the parameter or return value. This array is empty unless Data Type is a type that is capable of containing child elements, such as Array. |  |
| 0 | Void—Indicates that the parameter or return value has a void or empty data type. Typically, this indicates that a sequence has no relevant data to return. |
| 1 | Boolean—Indicates the parameter or return value is a Boolean. |
| 2 | Int32—Indicates the parameter or return value is a 32-bit signed integer. |
| 3 | UInt32—Indicates the parameter or return value is a 32-bit unsigned integer. |
| 4 | Int64—Indicates the parameter or return value is a 64-bit signed integer. |
| 5 | UInt64—Indicates the parameter or return value is a 64-bit unsigned integer. |
| 6 | Double—Indicates the parameter or return value is a double-precision floating point number. |
| 7 | Array—Indicates the parameter or return value is an array. |
| Major — Major indicates the major version. Minor — Minor indicates the minor version. Fix — Fix specifies the fix version number. This number may increment for smaller changes, such as bug fixes. Build — Build specifies the build number. This number may increment to reflect nightly builds. |  |

Parent topic:

Utilities

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-sequence-return-value-vi.html language=unavailable -->
## TOPIC 00368: Get Sequence Return Value Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-sequence-return-value-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-sequence-return-value-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-sequence-state-vi.html language=enus -->
## TOPIC 00369: Get Sequence State VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-sequence-state-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-sequence-state-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the execution state of a real-time sequence (Idle, Running, SingleStepping, Paused, Complete). icon Inputs/Outputs cgnrn.png Session Ref in Session Ref in is a reference to the stimulus profile session. A session is a group of top-level sequences that are deployed and started together. cstr.

### Get Sequence State VI

Returns the execution state of a real-time sequence (Idle, Running, SingleStepping, Paused, Complete).

[IMAGE alt='icon' src='get-sequence-state-vi.png']

#### Inputs/Outputs

| Session Ref in — Session Ref in is a reference to the stimulus profile session. A session is a group of top-level sequences that are deployed and started together. Sequence Name — Sequence Name specifies the name of the sequence. When operating on an individual sequence, the sequence must be specified by name. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Session Ref out — Session Ref out returns a reference to the stimulus profile session. Sequence Name out — Sequence Name out returns the name of the sequence. State — State indicates the current state of the sequence. 0 Idle—Indicates the sequence is idle. 1 Running—Indicates the sequence is running. 2 SingleStepping—Indicates the sequence is single-stepping. 3 Paused—Indicates the sequence is paused. 4 Stopped—Indicates the sequence is stopped. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | Idle—Indicates the sequence is idle. |
| 1 | Running—Indicates the sequence is running. |
| 2 | SingleStepping—Indicates the sequence is single-stepping. |
| 3 | Paused—Indicates the sequence is paused. |
| 4 | Stopped—Indicates the sequence is stopped. |

Parent topic:

Sequence Control

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-sequence-time-vi.html language=unavailable -->
## TOPIC 00370: Get Sequence Time Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-sequence-time-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-sequence-time-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/lock-stimulus-profile-session-vi.html language=enus -->
## TOPIC 00371: Lock Stimulus Profile Session VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/lock-stimulus-profile-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/lock-stimulus-profile-session-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Locks an NI VeriStand stimulus profile session with a password you specify. If the session is already locked, this VI returns an error. You cannot control a session while the session is locked. For example, if you try to pause a sequence in a locked session, this VI returns an error. icon Inputs/Out

### Lock Stimulus Profile Session VI

Locks an NI VeriStand stimulus profile session with a password you specify. If the session is already locked, this VI returns an error.

Note

[IMAGE alt='icon' src='lock-stimulus-profile-session-vi.png']

#### Inputs/Outputs

| Session Ref in — Session Ref in is a reference to the stimulus profile session. A session is a group of top-level sequences that are deployed and started together. Password — Password specifies the password for the stimulus profile session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Session Ref out — Session Ref out returns a reference to the stimulus profile session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Session Control

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/open-deployed-stimulus-profile-session-vi.html language=enus -->
## TOPIC 00372: Open Deployed Stimulus Profile Session VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/open-deployed-stimulus-profile-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/open-deployed-stimulus-profile-session-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a reference to an existing stimulus profile session that has already been deployed. icon Inputs/Outputs cstr.png Deployed Session ID Deployed Session ID specifies the ID of the stimulus profile session with which to connect. cstr.png Gateway IP Address ("": localhost) Gateway IP Address specif

### Open Deployed Stimulus Profile Session VI

Opens a reference to an existing stimulus profile session that has already been deployed.

[IMAGE alt='icon' src='open-deployed-stimulus-profile-session-vi.png']

#### Inputs/Outputs

| Deployed Session ID — Deployed Session ID specifies the ID of the stimulus profile session with which to connect. Gateway IP Address ("": localhost) — Gateway IP Address specifies the IP address of the VeriStand Gateway. This address can be in IP dot notation or it can be a hostname. If you do not specify an address, LabVIEW establishes a connection to the local computer. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Session Ref — Session Ref returns a reference to the session this VI created. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Stimulus Profile

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/open-stimulus-profile-session-vi.html language=enus -->
## TOPIC 00373: Open Stimulus Profile Session VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/open-stimulus-profile-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/open-stimulus-profile-session-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connects to the VeriStand Gateway and creates a session with a name you specify. icon Inputs/Outputs cstr.png Description Description specifies a description for the session. c1dgnrn.png Sequence Calls Sequence Calls includes references to the sequences to execute. Use the Create Sequence Call VI to

### Open Stimulus Profile Session VI

Connects to the VeriStand Gateway and creates a session with a name you specify.

[IMAGE alt='icon' src='open-stimulus-profile-session-vi.png']

#### Inputs/Outputs

| Description — Description specifies a description for the session. Sequence Calls — Sequence Calls includes references to the sequences to execute. Use the Create Sequence Call VI to create this input. Session Name — Session Name specifies the name of the session. Gateway IP Address ("": localhost) — Gateway IP Address specifies the IP address of the VeriStand Gateway. This address can be in IP dot notation or it can be a hostname. If you do not specify an address, LabVIEW establishes a connection to the local computer. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Session Ref — Session Ref returns a reference to the session this VI created. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Stimulus Profile

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/pause-sequence-vi.html language=enus -->
## TOPIC 00374: Pause Sequence VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/pause-sequence-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/pause-sequence-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Pauses the execution of a real-time sequence in an NI VeriStand stimulus profile session. icon Inputs/Outputs cgnrn.png Session Ref in Session Ref in is a reference to the stimulus profile session. A session is a group of top-level sequences that are deployed and started together. cstr.png Sequence

### Pause Sequence VI

Pauses the execution of a real-time sequence in an NI VeriStand stimulus profile session.

[IMAGE alt='icon' src='pause-sequence-vi.png']

#### Inputs/Outputs

| Session Ref in — Session Ref in is a reference to the stimulus profile session. A session is a group of top-level sequences that are deployed and started together. Sequence Name — Sequence Name specifies the name of the sequence. When operating on an individual sequence, the sequence must be specified by name. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Session Ref out — Session Ref out returns a reference to the stimulus profile session. Sequence Name out — Sequence Name out returns the name of the sequence. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Sequence Control

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/pause-stimulus-profile-session-vi.html language=unavailable -->
## TOPIC 00375: Pause Stimulus Profile Session Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/pause-stimulus-profile-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/pause-stimulus-profile-session-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/register-for-sequence-complete-event-vi.html language=enus -->
## TOPIC 00376: Register for Sequence Complete Event VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/register-for-sequence-complete-event-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/register-for-sequence-complete-event-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Registers for a sequence complete event for the set of sequences you specify. A sequence complete event is triggered when a sequence completes execution. This VI returns a registered user event reference and information about the event. icon Inputs/Outputs cgnrn.png Session Ref in Session Ref in is

### Register for Sequence Complete Event VI

Registers for a sequence complete event for the set of sequences you specify. A sequence complete event is triggered when a sequence completes execution. This VI returns a registered user event reference and information about the event.

[IMAGE alt='icon' src='register-for-sequence-complete-event-vi.png']

#### Inputs/Outputs

| Session Ref in — Session Ref in is a reference to the stimulus profile session. A session is a group of top-level sequences that are deployed and started together. Sequence Names — Sequence Names specifies the names of all the sequences for which to register events. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Sequence Complete Event Ref — Sequence Complete Event Ref contains information about the sequence complete event. Event Callbacks — Event Callbacks returns an array of references to event callbacks. Sequence Complete Event Data — Sequence Complete Event Data returns data about the event, including the name of the sequence for which it triggered, the return value of the sequence, whether the sequence was prematurely aborted, and any error information. Note Return values are declared by real-time sequences, and generally indicate some type of pass/fail information. Return values can be any data type. Event Registration Refnum — Event Registration Refnum returns the reference to a new or existing event registration. Session Ref out — Session Ref out returns a reference to the stimulus profile session. Sequence Names out — Sequence Names out returns the names of the sequences. Event Registration Refnum — Event Registration Refnum returns the reference to a new or existing event registration. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| Event Callbacks — Event Callbacks returns an array of references to event callbacks. Sequence Complete Event Data — Sequence Complete Event Data returns data about the event, including the name of the sequence for which it triggered, the return value of the sequence, whether the sequence was prematurely aborted, and any error information. Note Return values are declared by real-time sequences, and generally indicate some type of pass/fail information. Return values can be any data type. Event Registration Refnum — Event Registration Refnum returns the reference to a new or existing event registration. |

Parent topic:

Events

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/register-for-sequence-state-change-event-vi.html language=unavailable -->
## TOPIC 00377: Register For Sequence State Change Event Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/register-for-sequence-state-change-event-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/register-for-sequence-state-change-event-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/register-for-stimulus-profile-session-complete-event-vi.html language=unavailable -->
## TOPIC 00378: Register For Stimulus Profile Session Complete Event Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/register-for-stimulus-profile-session-complete-event-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/register-for-stimulus-profile-session-complete-event-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/register-for-stimulus-profile-session-undeploy-event-vi.html language=enus -->
## TOPIC 00379: Register for Stimulus Profile Session Undeploy Event VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/register-for-stimulus-profile-session-undeploy-event-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/register-for-stimulus-profile-session-undeploy-event-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Registers for a session undeploy event for the session you specify. A session undeploy event is triggered when the session undeploys from a target. This VI returns a registered user event reference and information about the event. icon Inputs/Outputs cgnrn.png Session Ref in Session Ref in is a refe

### Register for Stimulus Profile Session Undeploy Event VI

Registers for a session undeploy event for the session you specify. A session undeploy event is triggered when the session undeploys from a target. This VI returns a registered user event reference and information about the event.

[IMAGE alt='icon' src='register-for-stimulus-profile-session-undeploy-event-vi.png']

#### Inputs/Outputs

| Session Ref in — Session Ref in is a reference to the stimulus profile session. A session is a group of top-level sequences that are deployed and started together. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Session Undeploy Event Ref — Sequence Undeploy Event Ref contains information about the session undeploy event. Event Callback — Event Callback returns an event callback reference. User Event Ref — User Event Ref returns the strictly typed user event refnum. Event Registration Refnum — Event Registration Refnum returns the reference to a new or existing event registration. Session Ref out — Session Ref out returns a reference to the stimulus profile session. Event Registration Refnum — Event Registration Refnum returns the reference to a new or existing event registration. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| Event Callback — Event Callback returns an event callback reference. User Event Ref — User Event Ref returns the strictly typed user event refnum. Event Registration Refnum — Event Registration Refnum returns the reference to a new or existing event registration. |

Parent topic:

Events

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/run-sequence-vi.html language=enus -->
## TOPIC 00380: Run Sequence VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/run-sequence-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/run-sequence-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Runs or resumes a real-time sequence in an NI VeriStand stimulus profile session. icon Inputs/Outputs cgnrn.png Session Ref in Session Ref in is a reference to the stimulus profile session. A session is a group of top-level sequences that are deployed and started together. cstr.png Sequence Name Seq

### Run Sequence VI

Runs or resumes a real-time sequence in an NI VeriStand stimulus profile session.

[IMAGE alt='icon' src='run-sequence-vi.png']

#### Inputs/Outputs

| Session Ref in — Session Ref in is a reference to the stimulus profile session. A session is a group of top-level sequences that are deployed and started together. Sequence Name — Sequence Name specifies the name of the sequence. When operating on an individual sequence, the sequence must be specified by name. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Session Ref out — Session Ref out returns a reference to the stimulus profile session. Sequence Name out — Sequence Name out returns the name of the sequence. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Sequence Control

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/run-stimulus-profile-session-vi.html language=enus -->
## TOPIC 00381: Run Stimulus Profile Session VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/run-stimulus-profile-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/run-stimulus-profile-session-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Runs all sequences in an NI VeriStand stimulus profile session. icon Inputs/Outputs cgnrn.png Session Ref in Session Ref in is a reference to the stimulus profile session. A session is a group of top-level sequences that are deployed and started together. cerrcodeclst.png error in (no error) error i

### Run Stimulus Profile Session VI

Runs all sequences in an NI VeriStand stimulus profile session.

[IMAGE alt='icon' src='run-stimulus-profile-session-vi.png']

#### Inputs/Outputs

| Session Ref in — Session Ref in is a reference to the stimulus profile session. A session is a group of top-level sequences that are deployed and started together. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Session Ref out — Session Ref out returns a reference to the stimulus profile session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Session Control

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/stop-sequence-vi.html language=enus -->
## TOPIC 00382: Stop Sequence VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/stop-sequence-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/stop-sequence-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops a real-time sequence in an NI VeriStand stimulus profile session, which causes the sequence to skip to the clean-up section. If you want to skip clean-up tasks, use the Abort Sequence VI. icon Inputs/Outputs cgnrn.png Session Ref in Session Ref in is a reference to the stimulus profile session

### Stop Sequence VI

Stops a real-time sequence in an NI VeriStand stimulus profile session, which causes the sequence to skip to the clean-up section. If you want to skip clean-up tasks, use the Abort Sequence VI.

[IMAGE alt='icon' src='stop-sequence-vi.png']

#### Inputs/Outputs

| Session Ref in — Session Ref in is a reference to the stimulus profile session. A session is a group of top-level sequences that are deployed and started together. Sequence Name — Sequence Name specifies the name of the sequence. When operating on an individual sequence, the sequence must be specified by name. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Session Ref out — Session Ref out returns a reference to the stimulus profile session. Sequence Name out — Sequence Name out returns the name of the sequence. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Sequence Control

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/stop-stimulus-profile-session-vi.html language=enus -->
## TOPIC 00383: Stop Stimulus Profile Session VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/stop-stimulus-profile-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/stop-stimulus-profile-session-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops all real-time sequences in an NI VeriStand stimulus profile session. This VI will cause all active sequences to skip to the clean-up section and perform clean-up tasks. To skip clean-up tasks, use the Abort Stimulus Profile Session VI instead. icon Inputs/Outputs cgnrn.png Session Ref in Sessi

### Stop Stimulus Profile Session VI

Stops all real-time sequences in an NI VeriStand stimulus profile session. This VI will cause all active sequences to skip to the clean-up section and perform clean-up tasks. To skip clean-up tasks, use the Abort Stimulus Profile Session VI instead.

[IMAGE alt='icon' src='stop-stimulus-profile-session-vi.png']

#### Inputs/Outputs

| Session Ref in — Session Ref in is a reference to the stimulus profile session. A session is a group of top-level sequences that are deployed and started together. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Session Ref out — Session Ref out returns a reference to the stimulus profile session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Session Control

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/undeploy-stimulus-profile-session-vi.html language=unavailable -->
## TOPIC 00384: Undeploy Stimulus Profile Session Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/undeploy-stimulus-profile-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/undeploy-stimulus-profile-session-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/unlock-stimulus-profile-session-vi.html language=unavailable -->
## TOPIC 00385: Unlock Stimulus Profile Session Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/unlock-stimulus-profile-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/unlock-stimulus-profile-session-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/unregister-for-sequence-complete-event-vi.html language=enus -->
## TOPIC 00386: Unregister for Sequence Complete Event VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/unregister-for-sequence-complete-event-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/unregister-for-sequence-complete-event-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unregisters sequence complete events. Use the Register for Sequence Complete Event VI to get the Sequence Complete Event Ref this VI expects. icon Inputs/Outputs ccclst.png Sequence Complete Event Ref Sequence Complete Event Ref contains information about the sequence complete event. c1dcallbackrefn

### Unregister for Sequence Complete Event VI

Unregisters sequence complete events. Use the Register for Sequence Complete Event VI to get the **Sequence Complete Event Ref** this VI expects.

[IMAGE alt='icon' src='unregister-for-sequence-complete-event-vi.png']

#### Inputs/Outputs

| Sequence Complete Event Ref — Sequence Complete Event Ref contains information about the sequence complete event. Event Callbacks — Event Callbacks is an array of references to event callbacks. Sequence Complete Event Data — Sequence Complete Event Data is data about the event, including the name of the sequence for which it triggered, the return value of the sequence, whether the sequence was prematurely aborted, and any error information. Event Registration Refnum — Event Registration Refnum is the reference to the event registration. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| Event Callbacks — Event Callbacks is an array of references to event callbacks. Sequence Complete Event Data — Sequence Complete Event Data is data about the event, including the name of the sequence for which it triggered, the return value of the sequence, whether the sequence was prematurely aborted, and any error information. Event Registration Refnum — Event Registration Refnum is the reference to the event registration. |

Parent topic:

Events

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/unregister-for-sequence-state-change-event-vi.html language=enus -->
## TOPIC 00387: Unregister for Sequence State Change Event VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/unregister-for-sequence-state-change-event-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/unregister-for-sequence-state-change-event-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unregisters a sequence state change event. Use the Register for Sequence State Change Event VI to get the Sequence State Change Event Ref this VI expects. icon Inputs/Outputs ccclst.png Sequence State Change Event Ref Sequence State Change Event Ref contains information about the sequence state chan

### Unregister for Sequence State Change Event VI

Unregisters a sequence state change event. Use the Register for Sequence State Change Event VI to get the **Sequence State Change Event Ref** this VI expects.

[IMAGE alt='icon' src='unregister-for-sequence-state-change-event-vi.png']

#### Inputs/Outputs

| Sequence State Change Event Ref — Sequence State Change Event Ref contains information about the sequence state change event. Event Callbacks — Event Callbacks is an array of references to event callbacks. Sequence State Change Event Data — Sequence State Change Event Data contains information about the event, including the name of the sequence for which it triggered, the state of the sequence, and whether the sequence was prematurely aborted. Event Registration Refnum — Event Registration Refnum is the reference to the event registration. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| Event Callbacks — Event Callbacks is an array of references to event callbacks. Sequence State Change Event Data — Sequence State Change Event Data contains information about the event, including the name of the sequence for which it triggered, the state of the sequence, and whether the sequence was prematurely aborted. Event Registration Refnum — Event Registration Refnum is the reference to the event registration. |

Parent topic:

Events

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/unregister-for-stimulus-profile-session-complete-event-vi.html language=enus -->
## TOPIC 00388: Unregister for Stimulus Profile Session Complete Event VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/unregister-for-stimulus-profile-session-complete-event-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/unregister-for-stimulus-profile-session-complete-event-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unregisters for a session complete event. Use the Register for Stimulus Profile Session Complete Event VI to get the Session Complete Event Ref this VI expects. icon Inputs/Outputs ccclst.png Session Complete Event Ref Session Complete Event Ref contains information about the session complete event.

### Unregister for Stimulus Profile Session Complete Event VI

Unregisters for a session complete event. Use the Register for Stimulus Profile Session Complete Event VI to get the **Session Complete Event Ref** this VI expects.

[IMAGE alt='icon' src='unregister-for-stimulus-profile-session-complete-event-vi.png']

#### Inputs/Outputs

| Session Complete Event Ref — Session Complete Event Ref contains information about the session complete event. Event Callback — Event Callback is the event callback reference. User Event Ref — User Event Ref is the strictly typed user event refnum. Event Registration Refnum — Event Registration Refnum is the reference to the event registration. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| Event Callback — Event Callback is the event callback reference. User Event Ref — User Event Ref is the strictly typed user event refnum. Event Registration Refnum — Event Registration Refnum is the reference to the event registration. |

Parent topic:

Events

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/sequenceexecutioninterface/unregister-for-stimulus-profile-session-undeploy-event-vi.html language=unavailable -->
## TOPIC 00389: Unregister For Stimulus Profile Session Undeploy Event Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/sequenceexecutioninterface/unregister-for-stimulus-profile-session-undeploy-event-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/sequenceexecutioninterface/unregister-for-stimulus-profile-session-undeploy-event-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/close-waveform-stream-specification-vi.html language=enus -->
## TOPIC 00390: Close Waveform Stream Specification VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/close-waveform-stream-specification-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/close-waveform-stream-specification-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a waveform stream specification you opened with the New Waveform Stream Specification VI. icon Inputs/Outputs cgnrn.png WaveformStreamSpecification WaveformStreamSpecification is a reference to a waveform stream specification. You must create a new streaming specification to use this paramete

### Close Waveform Stream Specification VI

Closes a waveform stream specification you opened with the New Waveform Stream Specification VI.

[IMAGE alt='icon' src='close-waveform-stream-specification-vi.png']

#### Inputs/Outputs

| WaveformStreamSpecification — WaveformStreamSpecification is a reference to a waveform stream specification. You must create a new streaming specification to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. This node runs normally even if an error occurred before this node runs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Waveform Streaming

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/close-waveform-streaming-manager-reference-vi.html language=enus -->
## TOPIC 00391: Close Waveform Streaming Manager Reference VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/close-waveform-streaming-manager-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/close-waveform-streaming-manager-reference-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an open reference to the waveform-stream manager on the VeriStand Gateway. Use this VI to close waveform-stream manager references you open with the Open Waveform Stream Manager Reference VI. icon Inputs/Outputs cgnrn.png WaveformStreaming WaveformStreaming is a reference to the waveform-stre

### Close Waveform Streaming Manager Reference VI

Closes an open reference to the waveform-stream manager on the VeriStand Gateway. Use this VI to close waveform-stream manager references you open with the Open Waveform Stream Manager Reference VI.

[IMAGE alt='icon' src='close-waveform-streaming-manager-reference-vi.png']

#### Inputs/Outputs

| WaveformStreaming — WaveformStreaming is a reference to the waveform-stream manager on the VeriStand Gateway. error in (no error) — error in describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. This node runs normally even if an error occurred before this node runs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Waveform Streaming

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/compare-waveform-stream-specifications-vi.html language=unavailable -->
## TOPIC 00392: Compare Waveform Stream Specifications Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/compare-waveform-stream-specifications-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/compare-waveform-stream-specifications-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/get-waveform-dt-values-vi.html language=enus -->
## TOPIC 00393: Get Waveform dt Values VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/get-waveform-dt-values-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/get-waveform-dt-values-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of the delta T values for the specified waveform(s). icon Inputs/Outputs cgnrn.png WaveformStreaming in WaveformStreaming in is a reference to the waveform-stream manager. You must open a reference to the manager to use this parameter. c1dstr.png waveform paths waveform paths is an

### Get Waveform dt Values VI

Returns an array of the delta T values for the specified waveform(s).

[IMAGE alt='icon' src='get-waveform-dt-values-vi.png']

#### Inputs/Outputs

| WaveformStreaming in — WaveformStreaming in is a reference to the waveform-stream manager. You must open a reference to the manager to use this parameter. waveform paths — waveform paths is an array of the paths of the waveforms you want to access. You must enter the full path to a waveform, for example, Targets/Controller/Hardware/Chassis/DAQ/Device1/Analog Input/AI0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. WaveformStreaming out — WaveformStreaming out is a reference to the waveform-stream manager on the VeriStand Gateway. You can wire this output to other Waveform Streaming VIs. dt values — dt values returns an array whose elements are the delta T values for each waveform in waveform paths. NaN means the waveform has not been initialized. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utilities

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/get-waveform-streams-for-data-event-cdb-vi.html language=enus -->
## TOPIC 00394: Get Waveform Streams for Data Event (CDB) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/get-waveform-streams-for-data-event-cdb-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/get-waveform-streams-for-data-event-cdb-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns references to all waveform stream specifications for which you previously registered for events. Wire data to the registered waveform data event (DBL) in input to determine the polymorphic instance to use or manually select the instance. icon Inputs/Outputs ccclst.png registered waveform dat

### Get Waveform Streams for Data Event (CDB) VI

Returns references to all waveform stream specifications for which you previously registered for events. Wire data to the **registered waveform data event (DBL) in** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='get-waveform-streams-for-data-event-cdb-vi.png']

#### Inputs/Outputs

| registered waveform data event (CDB) in — registered waveform data event (CDB) in is a cluster of data with references to the event registration. You must register for waveform data events to use this parameter. Callback Refnum — Callback Refnum is a reference to the Register Event Callback. Data Event — Data Event is a reference to Waveform Data User Event. Event Refnum — Event Refnum is a reference to Waveform Data User Event Registration. WaveformDataWatcherCDB — WaveformDataWatcherCDB is a reference to the WaveformDataWatcherCDB .NET class. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. registered waveform data event (CDB) out — registered waveform data event (CDB) out returns a cluster of data with references to the event registration. Wire this cluster to the Unregister for Waveform Data Events VI to stop LabVIEW from generating events when a waveform generates new samples. Callback Refnum — Callback Refnum is a reference to the Register Event Callback. Data Event — Data Event is a reference to Waveform Data User Event. Event Refnum — Event Refnum is a reference to Waveform Data User Event Registration. WaveformDataWatcherCDB — WaveformDataWatcherCDB is a reference to the WaveformDataWatcherCDB .NET class. WaveformStreamSpecifications — WaveformStreamSpecification is an array of references to waveform stream specifications. You can wire this output to other Waveform Streaming VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| Callback Refnum — Callback Refnum is a reference to the Register Event Callback. Data Event — Data Event is a reference to Waveform Data User Event. Event Refnum — Event Refnum is a reference to Waveform Data User Event Registration. WaveformDataWatcherCDB — WaveformDataWatcherCDB is a reference to the WaveformDataWatcherCDB .NET class. |
| Callback Refnum — Callback Refnum is a reference to the Register Event Callback. Data Event — Data Event is a reference to Waveform Data User Event. Event Refnum — Event Refnum is a reference to Waveform Data User Event Registration. WaveformDataWatcherCDB — WaveformDataWatcherCDB is a reference to the WaveformDataWatcherCDB .NET class. |

Parent topic:

Get Waveform Streams for Data Event VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/get-waveform-streams-for-data-event-dbl-vi.html language=unavailable -->
## TOPIC 00395: Get Waveform Streams For Data Event Dbl Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/get-waveform-streams-for-data-event-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/get-waveform-streams-for-data-event-dbl-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/get-waveform-streams-for-data-event-vi.html language=unavailable -->
## TOPIC 00396: Get Waveform Streams For Data Event Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/get-waveform-streams-for-data-event-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/get-waveform-streams-for-data-event-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/new-waveform-stream-specification-vi.html language=enus -->
## TOPIC 00397: New Waveform Stream Specification VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/new-waveform-stream-specification-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/new-waveform-stream-specification-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Identifies a waveform whose data you want to stream to a host computer. icon Inputs/Outputs cstr.png waveform path waveform path specifies the path of the waveform you want to access. You must enter the full path to the waveform, for example, Targets/Controller/Hardware/Chassis/DAQ/Device1/Analog In

### New Waveform Stream Specification VI

Identifies a waveform whose data you want to stream to a host computer.

[IMAGE alt='icon' src='new-waveform-stream-specification-vi.png']

#### Inputs/Outputs

| waveform path — waveform path specifies the path of the waveform you want to access. You must enter the full path to the waveform, for example, Targets/Controller/Hardware/Chassis/DAQ/Device1/Analog Input/AI0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. WaveformStreamSpecification — WaveformStreamSpecification is a reference to the waveform streaming specification for the specified waveform. You can wire this output to other Waveform Streaming VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Waveform Streaming

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/open-waveform-streaming-manager-reference-vi.html language=enus -->
## TOPIC 00398: Open Waveform Streaming Manager Reference VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/open-waveform-streaming-manager-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/open-waveform-streaming-manager-reference-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a reference to the waveform-stream manager on the VeriStand Gateway. You must open a reference before you register to receive waveform data and start streaming waveforms from the VeriStand Gateway. icon Inputs/Outputs cstr.png Gateway IP Address ("": localhost) Gateway IP Address specifies the

### Open Waveform Streaming Manager Reference VI

Opens a reference to the waveform-stream manager on the VeriStand Gateway. You must open a reference before you register to receive waveform data and start streaming waveforms from the VeriStand Gateway.

[IMAGE alt='icon' src='open-waveform-streaming-manager-reference-vi.png']

#### Inputs/Outputs

| Gateway IP Address ("": localhost) — Gateway IP Address specifies the IP address of the VeriStand Gateway. This address can be in IP dot notation or it can be a hostname. If you do not specify an address, LabVIEW establishes a connection to the local computer. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. WaveformStreaming — WaveformStreaming is a reference to the waveform-stream manager on the VeriStand Gateway. You can wire this output to other Waveform Streaming VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Waveform Streaming

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/register-for-waveform-data-events-cdb-vi.html language=enus -->
## TOPIC 00399: Register for Waveform Data Events (CDB) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/register-for-waveform-data-events-cdb-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/register-for-waveform-data-events-cdb-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Registers to receive waveform data from the specified WaveformStreamSpecifications. You can use this VI prior to starting waveform streams to generate an event registration refnum that allows an Event structure to stream data from waveforms. You must manually select the instance to use. icon Inputs/

### Register for Waveform Data Events (CDB) VI

Registers to receive waveform data from the specified **WaveformStreamSpecifications**. You can use this VI prior to starting waveform streams to generate an event registration refnum that allows an Event structure to stream data from waveforms. You must manually select the instance to use.

[IMAGE alt='icon' src='register-for-waveform-data-events-cdb-vi.png']

#### Inputs/Outputs

| WaveformStreaming in — WaveformStreaming in is a reference to the waveform-stream manager. You must open a reference to the manager to use this parameter. WaveformStreamSpecifications — WaveformStreamSpecifications is an array of references to waveform streaming specifications whose waveforms you want to stream. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. registered waveform data event (CDB) — registered waveform data event (CDB) returns a cluster of data with references to the event registration. Wire this cluster to the Unregister for Waveform Data Events VI to stop LabVIEW from generating events when a waveform generates new samples. Callback Refnum — Callback Refnum is a reference to the Register Event Callback. Data Event — Data Event is a reference to Waveform Data User Event. Event Refnum — Event Refnum is a reference to Waveform Data User Event Registration. WaveformDataWatcherCDB — WaveformDataWatcherCDB is a reference to the WaveformDataWatcherCDB .NET class. WaveformStreaming out — WaveformStreaming out is a reference to the waveform-stream manager on the VeriStand Gateway. You can wire this output to other Waveform Streaming VIs. error out — error out contains error information. This output provides standard error out functionality. waveform data event registration (CDB) — waveform data event registration (CDB) returns an event registration refnum you wire to an Event structure to serve as an event source that returns waveform data when a waveform produces new values. |
| --- |
| Callback Refnum — Callback Refnum is a reference to the Register Event Callback. Data Event — Data Event is a reference to Waveform Data User Event. Event Refnum — Event Refnum is a reference to Waveform Data User Event Registration. WaveformDataWatcherCDB — WaveformDataWatcherCDB is a reference to the WaveformDataWatcherCDB .NET class. |

Parent topic:

Register for Waveform Data Events VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/register-for-waveform-data-events-dbl-vi.html language=unavailable -->
## TOPIC 00400: Register For Waveform Data Events Dbl Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/register-for-waveform-data-events-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/register-for-waveform-data-events-dbl-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/register-for-waveform-data-events-vi.html language=enus -->
## TOPIC 00401: Register for Waveform Data Events VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/register-for-waveform-data-events-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/register-for-waveform-data-events-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Registers to receive waveform data from the specified WaveformStreamSpecifications. You can use this VI prior to starting waveform streams to generate an event registration refnum that allows an Event structure to stream data from waveforms. You must manually select the instance to use. icon

### Register for Waveform Data Events VI

Registers to receive waveform data from the specified **WaveformStreamSpecifications**. You can use this VI prior to starting waveform streams to generate an event registration refnum that allows an Event structure to stream data from waveforms. You must manually select the instance to use.

[IMAGE alt='icon' src='register-for-waveform-data-events-vi.png']

- [Register for Waveform Data Events (DBL) VI](../../../../vi-lib/ni-veristand/execution/waveformstreaming/register-for-waveform-data-events-dbl-vi.html) Registers to receive waveform data from the specified WaveformStreamSpecifications . You can use this VI prior to starting waveform streams to generate an event registration refnum that allows an Event structure to stream data from waveforms. You must manually select the instance to use.
- [Register for Waveform Data Events (CDB) VI](../../../../vi-lib/ni-veristand/execution/waveformstreaming/register-for-waveform-data-events-cdb-vi.html) Registers to receive waveform data from the specified WaveformStreamSpecifications . You can use this VI prior to starting waveform streams to generate an event registration refnum that allows an Event structure to stream data from waveforms. You must manually select the instance to use.

Parent topic:

Waveform Streaming

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/set-condition-for-waveform-stream-all-data-vi.html language=enus -->
## TOPIC 00402: Set Condition for Waveform Stream (All Data) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/set-condition-for-waveform-stream-all-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/set-condition-for-waveform-stream-all-data-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the condition under which NI VeriStand streams waveform data to a host computer. icon Inputs/Outputs cgnrn.png WaveformStreamSpecification in WaveformStreamSpecification in is a reference to a streaming specification. You must create a streaming specification to use this parameter. cerrcodec

### Set Condition for Waveform Stream (All Data) VI

Defines the condition under which NI VeriStand streams waveform data to a host computer.

[IMAGE alt='icon' src='set-condition-for-waveform-stream-all-data-vi.png']

#### Inputs/Outputs

| WaveformStreamSpecification in — WaveformStreamSpecification in is a reference to a streaming specification. You must create a streaming specification to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. WaveformStreamSpecification out — WaveformStreamSpecification out is a reference to a streaming specification. You can wire this output to other Waveform Streaming VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Set Condition for Waveform Stream VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/set-condition-for-waveform-stream-first-n-seconds-vi.html language=enus -->
## TOPIC 00403: Set Condition for Waveform Stream (First N Seconds) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/set-condition-for-waveform-stream-first-n-seconds-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/set-condition-for-waveform-stream-first-n-seconds-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the condition under which NI VeriStand streams waveform data to a host computer. icon Inputs/Outputs cgnrn.png WaveformStreamSpecification in WaveformStreamSpecification in is a reference to a streaming specification. You must create a streaming specification to use this parameter. cdbl.png

### Set Condition for Waveform Stream (First N Seconds) VI

Defines the condition under which NI VeriStand streams waveform data to a host computer.

[IMAGE alt='icon' src='set-condition-for-waveform-stream-first-n-seconds-vi.png']

#### Inputs/Outputs

| WaveformStreamSpecification in — WaveformStreamSpecification in is a reference to a streaming specification. You must create a streaming specification to use this parameter. n seconds — n seconds specifies the number of seconds to stream data. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. WaveformStreamSpecification out — WaveformStreamSpecification out is a reference to a streaming specification. You can wire this output to other Waveform Streaming VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Set Condition for Waveform Stream VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/set-condition-for-waveform-stream-in-range-dbl-vi.html language=enus -->
## TOPIC 00404: Set Condition for Waveform Stream (In Range DBL) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/set-condition-for-waveform-stream-in-range-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/set-condition-for-waveform-stream-in-range-dbl-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the condition under which NI VeriStand streams waveform data to a host computer. icon Inputs/Outputs cbool.png invert range check? (F) invert range check? if TRUE, specifies to stream data when values are outside the range between the high limit and low limit. The default is FALSE. cgnrn.png

### Set Condition for Waveform Stream (In Range DBL) VI

Defines the condition under which NI VeriStand streams waveform data to a host computer.

[IMAGE alt='icon' src='set-condition-for-waveform-stream-in-range-dbl-vi.png']

#### Inputs/Outputs

| invert range check? (F) — invert range check? if TRUE, specifies to stream data when values are outside the range between the high limit and low limit. The default is FALSE. WaveformStreamSpecification in — WaveformStreamSpecification in is a reference to a streaming specification. You must create a streaming specification to use this parameter. high limit — high limit specifies the maximum value of the range that determines whether to stream data. low limit — low limit specifies the minimum value of the range that determines whether to stream data. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. WaveformStreamSpecification out — WaveformStreamSpecification out is a reference to a streaming specification. You can wire this output to other Waveform Streaming VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Set Condition for Waveform Stream VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/set-condition-for-waveform-stream-n-of-m-seconds-vi.html language=enus -->
## TOPIC 00405: Set Condition for Waveform Stream (N of M Seconds) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/set-condition-for-waveform-stream-n-of-m-seconds-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/set-condition-for-waveform-stream-n-of-m-seconds-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the condition under which NI VeriStand streams waveform data to a host computer. icon Inputs/Outputs cgnrn.png WaveformStreamSpecification in WaveformStreamSpecification in is a reference to a streaming specification. You must create a streaming specification to use this parameter. cdbl.png

### Set Condition for Waveform Stream (N of M Seconds) VI

Defines the condition under which NI VeriStand streams waveform data to a host computer.

[IMAGE alt='icon' src='set-condition-for-waveform-stream-n-of-m-seconds-vi.png']

#### Inputs/Outputs

| WaveformStreamSpecification in — WaveformStreamSpecification in is a reference to a streaming specification. You must create a streaming specification to use this parameter. n seconds — n seconds specifies the number of seconds to stream data. m seconds — m seconds specifies the interval, in seconds, between the starts of streams. For example, if you specify to stream 2 out of every 10 seconds, NI VeriStand streams data for two seconds, waits for eight seconds, and then repeats the process. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. WaveformStreamSpecification out — WaveformStreamSpecification out is a reference to a streaming specification. You can wire this output to other Waveform Streaming VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Set Condition for Waveform Stream VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/set-condition-for-waveform-stream-vi.html language=enus -->
## TOPIC 00406: Set Condition for Waveform Stream VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/set-condition-for-waveform-stream-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/set-condition-for-waveform-stream-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the condition under which NI VeriStand streams waveform data to a host computer. If NI VeriStand acquires data at a faster rate than the streaming rate you set with the Set Rate for Waveform Stream VI, NI VeriStand decimates the acquired waveform data, so not all samples you requested are st

### Set Condition for Waveform Stream VI

Defines the condition under which NI VeriStand streams waveform data to a host computer.

Note

[IMAGE alt='icon' src='set-condition-for-waveform-stream-vi.png']

- [Set Condition for Waveform Stream (All Data) VI](../../../../vi-lib/ni-veristand/execution/waveformstreaming/set-condition-for-waveform-stream-all-data-vi.html) Defines the condition under which NI VeriStand streams waveform data to a host computer.
- [Set Condition for Waveform Stream (First N Seconds) VI](../../../../vi-lib/ni-veristand/execution/waveformstreaming/set-condition-for-waveform-stream-first-n-seconds-vi.html) Defines the condition under which NI VeriStand streams waveform data to a host computer.
- [Set Condition for Waveform Stream (N of M Seconds) VI](../../../../vi-lib/ni-veristand/execution/waveformstreaming/set-condition-for-waveform-stream-n-of-m-seconds-vi.html) Defines the condition under which NI VeriStand streams waveform data to a host computer.
- [Set Condition for Waveform Stream (In Range DBL) VI](../../../../vi-lib/ni-veristand/execution/waveformstreaming/set-condition-for-waveform-stream-in-range-dbl-vi.html) Defines the condition under which NI VeriStand streams waveform data to a host computer.

Parent topic:

Waveform Streaming

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/set-rate-for-waveform-stream-acquisition-rate-vi.html language=enus -->
## TOPIC 00407: Set Rate for Waveform Stream (Acquisition Rate) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/set-rate-for-waveform-stream-acquisition-rate-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/set-rate-for-waveform-stream-acquisition-rate-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to stream waveform values at the same rate the device acquires data or at a custom rate you specify. You must manually select the polymorphic instance to use. icon Inputs/Outputs cgnrn.png WaveformStreamSpecification in WaveformStreamSpecification in is a reference to a streaming specif

### Set Rate for Waveform Stream (Acquisition Rate) VI

Sets whether to stream waveform values at the same rate the device acquires data or at a custom rate you specify. You must manually select the polymorphic instance to use.

[IMAGE alt='icon' src='set-rate-for-waveform-stream-acquisition-rate-vi.png']

#### Inputs/Outputs

| WaveformStreamSpecification in — WaveformStreamSpecification in is a reference to a streaming specification. You must create a streaming specification to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. WaveformStreamSpecification out — WaveformStreamSpecification out is a reference to a streaming specification. You can wire this output to other Waveform Streaming VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Set Rate for Waveform Stream VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/set-rate-for-waveform-stream-custom-rate-vi.html language=unavailable -->
## TOPIC 00408: Set Rate For Waveform Stream Custom Rate Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/set-rate-for-waveform-stream-custom-rate-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/set-rate-for-waveform-stream-custom-rate-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/set-rate-for-waveform-stream-vi.html language=enus -->
## TOPIC 00409: Set Rate for Waveform Stream VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/set-rate-for-waveform-stream-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/set-rate-for-waveform-stream-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to stream waveform values at the same rate the device acquires data or at a custom rate you specify. You must manually select the polymorphic instance to use. icon

### Set Rate for Waveform Stream VI

Sets whether to stream waveform values at the same rate the device acquires data or at a custom rate you specify. You must manually select the polymorphic instance to use.

[IMAGE alt='icon' src='set-rate-for-waveform-stream-vi.png']

- [Set Rate for Waveform Stream (Acquisition Rate) VI](../../../../vi-lib/ni-veristand/execution/waveformstreaming/set-rate-for-waveform-stream-acquisition-rate-vi.html) Sets whether to stream waveform values at the same rate the device acquires data or at a custom rate you specify. You must manually select the polymorphic instance to use.
- [Set Rate for Waveform Stream (Custom Rate) VI](../../../../vi-lib/ni-veristand/execution/waveformstreaming/set-rate-for-waveform-stream-custom-rate-vi.html) Sets whether to stream waveform values at the same rate the device acquires data or at a custom rate you specify. You must manually select the polymorphic instance to use.

Parent topic:

Waveform Streaming

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/set-waveform-streams-for-data-event-cdb-vi.html language=enus -->
## TOPIC 00410: Set Waveform Streams for Data Event (CDB) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/set-waveform-streams-for-data-event-cdb-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/set-waveform-streams-for-data-event-cdb-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Updates the event registration to apply to the waveform stream specifications you specify. This VI is useful for changing the waveforms for which you want to receive data events without stopping the current event-handling routine and re-registering for waveform-data events. icon Inputs/Outputs cccls

### Set Waveform Streams for Data Event (CDB) VI

Updates the event registration to apply to the waveform stream specifications you specify. This VI is useful for changing the waveforms for which you want to receive data events without stopping the current event-handling routine and re-registering for waveform-data events.

[IMAGE alt='icon' src='set-waveform-streams-for-data-event-cdb-vi.png']

#### Inputs/Outputs

| registered waveform data event (CDB) in — registered waveform data event (CDB) in is a cluster of data with references to the event registration. You must register for waveform data events to use this parameter. Callback Refnum — Callback Refnum is a reference to the Register Event Callback. Data Event — Data Event is a reference to Waveform Data User Event. Event Refnum — Event Refnum is a reference to Waveform Data User Event Registration. WaveformDataWatcherCDB — WaveformDataWatcherCDB is a reference to the WaveformDataWatcherCDB .NET class. WaveformStreamSpecifications — WaveformStreamSpecifications is an array of references to waveform streaming specifications whose waveforms you want to stream. The data types of the waveform(s) must be complex double-precision, floating-point. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. registered waveform data event (CDB) out — registered waveform data event (CDB) out returns a cluster of data with references to the event registration. Wire this cluster to the Unregister for Waveform Data Events VI to stop LabVIEW from generating events when a waveform generates new samples. Callback Refnum — Callback Refnum is a reference to the Register Event Callback. Data Event — Data Event is a reference to Waveform Data User Event. Event Refnum — Event Refnum is a reference to Waveform Data User Event Registration. WaveformDataWatcherCDB — WaveformDataWatcherCDB is a reference to the WaveformDataWatcherCDB .NET class. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| Callback Refnum — Callback Refnum is a reference to the Register Event Callback. Data Event — Data Event is a reference to Waveform Data User Event. Event Refnum — Event Refnum is a reference to Waveform Data User Event Registration. WaveformDataWatcherCDB — WaveformDataWatcherCDB is a reference to the WaveformDataWatcherCDB .NET class. |
| Callback Refnum — Callback Refnum is a reference to the Register Event Callback. Data Event — Data Event is a reference to Waveform Data User Event. Event Refnum — Event Refnum is a reference to Waveform Data User Event Registration. WaveformDataWatcherCDB — WaveformDataWatcherCDB is a reference to the WaveformDataWatcherCDB .NET class. |

Parent topic:

Set Waveform Streams for Data Event VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/set-waveform-streams-for-data-event-dbl-vi.html language=unavailable -->
## TOPIC 00411: Set Waveform Streams For Data Event Dbl Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/set-waveform-streams-for-data-event-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/set-waveform-streams-for-data-event-dbl-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/set-waveform-streams-for-data-event-vi.html language=unavailable -->
## TOPIC 00412: Set Waveform Streams For Data Event Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/set-waveform-streams-for-data-event-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/set-waveform-streams-for-data-event-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/start-streaming-waveforms-vi.html language=enus -->
## TOPIC 00413: Start Streaming Waveforms VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/start-streaming-waveforms-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/start-streaming-waveforms-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Starts streaming waveform data to the VeriStand Gateway. Use this VI to allow an Event structure to start reading waveform values on the block diagram. icon Inputs/Outputs cgnrn.png WaveformStreaming in WaveformStreaming in is a reference to the waveform-stream manager. You must open a reference to

### Start Streaming Waveforms VI

Starts streaming waveform data to the VeriStand Gateway. Use this VI to allow an Event structure to start reading waveform values on the block diagram.

[IMAGE alt='icon' src='start-streaming-waveforms-vi.png']

#### Inputs/Outputs

| WaveformStreaming in — WaveformStreaming in is a reference to the waveform-stream manager. You must open a reference to the manager to use this parameter. WaveformStreamSpecifications — WaveformStreamSpecifications is an array of references to waveform streaming specifications whose waveforms you want to stream. The data types of the waveform(s) must be double-precision, floating-point. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. WaveformStreaming out — WaveformStreaming out is a reference to the waveform-stream manager on the VeriStand Gateway. You can wire this output to other Waveform Streaming VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Waveform Streaming

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/stop-streaming-waveforms-vi.html language=enus -->
## TOPIC 00414: Stop Streaming Waveforms VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/stop-streaming-waveforms-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/stop-streaming-waveforms-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops streaming the specified waveforms to the VeriStand Gateway. icon Inputs/Outputs cgnrn.png WaveformStreaming in WaveformStreaming in is a reference to the waveform-stream manager. You must open a reference to the manager to use this parameter. c1dgnrn.png WaveformStreamSpecifications WaveformSt

### Stop Streaming Waveforms VI

Stops streaming the specified waveforms to the VeriStand Gateway.

[IMAGE alt='icon' src='stop-streaming-waveforms-vi.png']

#### Inputs/Outputs

| WaveformStreaming in — WaveformStreaming in is a reference to the waveform-stream manager. You must open a reference to the manager to use this parameter. WaveformStreamSpecifications — WaveformStreamSpecifications is an array of references to waveform streaming specifications whose waveforms you want to stream. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. WaveformStreaming out — WaveformStreaming out is a reference to the waveform-stream manager on the VeriStand Gateway. You can wire this output to other Waveform Streaming VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Waveform Streaming

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/unregister-for-waveform-data-events-cdb-vi.html language=enus -->
## TOPIC 00415: Unregister for Waveform Data Events (CDB) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/unregister-for-waveform-data-events-cdb-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/unregister-for-waveform-data-events-cdb-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unregisters all waveform data events associated with the event registration refnum. Event structures that use this event registration refnum no longer receive any events. Wire data to the registered waveform data event (DBL) input to determine the polymorphic instance to use or manually select the i

### Unregister for Waveform Data Events (CDB) VI

Unregisters all waveform data events associated with the event registration refnum. Event structures that use this event registration refnum no longer receive any events. Wire data to the **registered waveform data event (DBL)** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='unregister-for-waveform-data-events-cdb-vi.png']

#### Inputs/Outputs

| registered waveform data event (CDB) — registered waveform data event (CDB) is a cluster of data with references to the event registration. You must register for waveform data events to use this parameter. Callback Refnum — Callback Refnum is a reference to the Register Event Callback. Data Event — Data Event is a reference to Waveform Data User Event. Event Refnum — Event Refnum is a reference to Waveform Data User Event Registration. WaveformDataWatcherCDB — WaveformDataWatcherCDB is a reference to the WaveformDataWatcherCDB .NET class. error in (no error) — error in describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. This node runs normally even if an error occurred before this node runs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| Callback Refnum — Callback Refnum is a reference to the Register Event Callback. Data Event — Data Event is a reference to Waveform Data User Event. Event Refnum — Event Refnum is a reference to Waveform Data User Event Registration. WaveformDataWatcherCDB — WaveformDataWatcherCDB is a reference to the WaveformDataWatcherCDB .NET class. |

Parent topic:

Unregister for Waveform Data Events VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/unregister-for-waveform-data-events-dbl-vi.html language=enus -->
## TOPIC 00416: Unregister for Waveform Data Events (DBL) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/unregister-for-waveform-data-events-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/unregister-for-waveform-data-events-dbl-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unregisters all waveform data events associated with the event registration refnum. Event structures that use this event registration refnum no longer receive any events. Wire data to the registered waveform data event (DBL) input to determine the polymorphic instance to use or manually select the i

### Unregister for Waveform Data Events (DBL) VI

Unregisters all waveform data events associated with the event registration refnum. Event structures that use this event registration refnum no longer receive any events. Wire data to the **registered waveform data event (DBL)** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='unregister-for-waveform-data-events-dbl-vi.png']

#### Inputs/Outputs

| registered waveform data event (DBL) — registered waveform data event (DBL) is a cluster of data with references to the event registration. You must register for waveform data events to use this parameter. Callback Refnum — Callback Refnum is a reference to the Register Event Callback. Data Event — Data Event is a reference to Waveform Data User Event. Event Refnum — Event Refnum is a reference to Waveform Data User Event Registration. WaveformDataWatcherDBL — WaveformDataWatcherDBL is a reference to the WaveformDataWatcherDBL .NET class. error in (no error) — error in describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. This node runs normally even if an error occurred before this node runs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| Callback Refnum — Callback Refnum is a reference to the Register Event Callback. Data Event — Data Event is a reference to Waveform Data User Event. Event Refnum — Event Refnum is a reference to Waveform Data User Event Registration. WaveformDataWatcherDBL — WaveformDataWatcherDBL is a reference to the WaveformDataWatcherDBL .NET class. |

Parent topic:

Unregister for Waveform Data Events VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/waveformstreaming/unregister-for-waveform-data-events-vi.html language=unavailable -->
## TOPIC 00417: Unregister For Waveform Data Events Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/waveformstreaming/unregister-for-waveform-data-events-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/waveformstreaming/unregister-for-waveform-data-events-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-close-engine-state-change-notification-vi.html language=enus -->
## TOPIC 00418: NI VeriStand - Close Engine State Change Notification VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-close-engine-state-change-notification-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-close-engine-state-change-notification-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Destroys the user event created by the Open Engine State Change Notification VI. icon Inputs/Outputs ccclst.png SystemStateRefs SystemStateRefs is a reference to the user event created by the Open Engine State Change Notification VI. cusereventrn.png CustDatRef CustDatRef is a reference to System St

### NI VeriStand - Close Engine State Change Notification VI

Destroys the user event created by the Open Engine State Change Notification VI.

[IMAGE alt='icon' src='ni-veristand-close-engine-state-change-notification-vi.png']

#### Inputs/Outputs

| SystemStateRefs — SystemStateRefs is a reference to the user event created by the Open Engine State Change Notification VI. CustDatRef — CustDatRef is a reference to System State Change User Event. EvtRef — EvtRef is a reference to Event Callback. Target State User Event — Target State User Event is a reference to Target State Change User Event. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| CustDatRef — CustDatRef is a reference to System State Change User Event. EvtRef — EvtRef is a reference to Event Callback. Target State User Event — Target State User Event is a reference to Target State Change User Event. |

Parent topic:

Workspace

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-close-udp-channel-streaming-session-vi.html language=enus -->
## TOPIC 00419: NI VeriStand - Close UDP Channel Streaming Session VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-close-udp-channel-streaming-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-close-udp-channel-streaming-session-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a UDP channel streaming session. icon Inputs/Outputs cgnrn.png UDPChannelStreamSession in UDPChannelStreamSession in is the reference to the channel streaming session. cerrcodeclst.png error in (no error) error in describes error conditions that occur before this node runs. This input provide

### NI VeriStand - Close UDP Channel Streaming Session VI

Closes a UDP channel streaming session.

[IMAGE alt='icon' src='ni-veristand-close-udp-channel-streaming-session-vi.png']

#### Inputs/Outputs

| UDPChannelStreamSession in — UDPChannelStreamSession in is the reference to the channel streaming session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

UDP Channel Streaming

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-close-workspace-manager-reference-vi.html language=unavailable -->
## TOPIC 00420: Ni Veristand Close Workspace Manager Reference Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-close-workspace-manager-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-close-workspace-manager-reference-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-connect-to-system-vi.html language=enus -->
## TOPIC 00421: NI VeriStand - Connect to System VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-connect-to-system-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-connect-to-system-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connects the VeriStand Gateway to the target(s) you define in the system definition file you specify. icon Inputs/Outputs cpath.png Calibration File Calibration File specifies the path to a .nivscf file that defines calibration coefficients for channels in the system definition file. When this VI ru

### NI VeriStand - Connect to System VI

Connects the VeriStand Gateway to the target(s) you define in the system definition file you specify.

[IMAGE alt='icon' src='ni-veristand-connect-to-system-vi.png']

#### Inputs/Outputs

| Calibration File — Calibration File specifies the path to a .nivscf file that defines calibration coefficients for channels in the system definition file. When this VI runs, VeriStand applies the calibration coefficients in the file. WorkspaceManager in — WorkspaceManager in specifies a reference to the Workspace Manager on the VeriStand Gateway. System Definition File (.nivssdf) — System Definition File specifies the path of the system definition file you want to run. Timeout (60000 ms) — Timeout specifies the maximum idle time, in milliseconds, before the connection to the VeriStand Gateway automatically times out. The default value is 60000 ms. If you specify zero or less as the value, the VI uses the default value. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Deploy System Definition (T) — Deploy System Definition specifies whether to deploy the system definition file to the target and then connect to the target, or to connect to a target that already is running without deploying the system definition file. Filtered Targets — Filtered Targets--Specifies the names of targets to skip connecting to. WorkspaceManager out — WorkspaceManager out is a reference to the workspace manager on the VeriStand Gateway. You can wire this output to other Workspace VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

System Connection

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-deploy-udp-channel-streaming-session-vi.html language=enus -->
## TOPIC 00422: NI VeriStand - Deploy UDP Channel Streaming Session VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-deploy-udp-channel-streaming-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-deploy-udp-channel-streaming-session-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deploys a UDP channel streaming session that you open with the Open UDP Channel Streaming Session VI. This VI returns data that you can use with the LabVIEW UDP VI and functions to read data from the channels. icon Inputs/Outputs cgnrn.png UDPChannelStreamSession in UDPChannelStreamSession in is the

### NI VeriStand - Deploy UDP Channel Streaming Session VI

Deploys a UDP channel streaming session that you open with the Open UDP Channel Streaming Session VI. This VI returns data that you can use with the LabVIEW UDP VI and functions to read data from the channels.

[IMAGE alt='icon' src='ni-veristand-deploy-udp-channel-streaming-session-vi.png']

#### Inputs/Outputs

| UDPChannelStreamSession in — UDPChannelStreamSession in is the reference to the channel streaming session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. UDP Multicast Address — UDP Multicast Address returns the IP address of the multicast group as a string. Port — Port returns the port number the VI used. UDPChannelStreamSession out — UDPChannelStreamSession out returns the reference to the channel streaming session. Channel IDs — Channel IDs returns the IDs of the channels you are streaming. Packet IDs — Packet IDs returns the IDs of the packets that contain the channel data. error out — error out contains error information. This output provides standard error out functionality. Max Packet Size — Max Packet Size returns the maximum possible size, in bytes, of a UDP packet that the VeriStand Gateway can publish. You can use this output to determine the maximum number of bytes to read from a packet. |
| --- |

Parent topic:

UDP Channel Streaming

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-disconnect-from-system-vi.html language=unavailable -->
## TOPIC 00423: Ni Veristand Disconnect From System Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-disconnect-from-system-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-disconnect-from-system-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-get-alias-list-vi.html language=enus -->
## TOPIC 00424: NI VeriStand - Get Alias List VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-get-alias-list-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-get-alias-list-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns lists of all the defined aliases and their corresponding channels. icon Inputs/Outputs cgnrn.png WorkspaceManager in WorkspaceManager in specifies a reference to the Workspace Manager on the VeriStand Gateway. cerrcodeclst.png error in (no error) error in describes error conditions that occu

### NI VeriStand - Get Alias List VI

Returns lists of all the defined aliases and their corresponding channels.

[IMAGE alt='icon' src='ni-veristand-get-alias-list-vi.png']

#### Inputs/Outputs

| WorkspaceManager in — WorkspaceManager in specifies a reference to the Workspace Manager on the VeriStand Gateway. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. WorkspaceManager out — WorkspaceManager out is a reference to the workspace manager on the VeriStand Gateway. You can wire this output to other Workspace VIs. Aliases — Aliases returns the list of defined aliases. Channels — Channels returns the names of the channels that correspond to the Aliases. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Workspace

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-get-channel-2d-array-values-vi.html language=enus -->
## TOPIC 00425: NI VeriStand - Get Channel 2D Array Values VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-get-channel-2d-array-values-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-get-channel-2d-array-values-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns values of channels on the target. You can get values for a single channel, multiple channels, or vector values for a single channel. You must manually select the polymorphic instance to use. Returns the vector values of a single channel. icon Inputs/Outputs cgnrn.png WorkspaceManager in Work

### NI VeriStand - Get Channel 2D Array Values VI

Returns values of channels on the target. You can get values for a single channel, multiple channels, or vector values for a single channel. You must manually select the polymorphic instance to use.

Note

[IMAGE alt='icon' src='ni-veristand-get-channel-2d-array-values-vi.png']

#### Inputs/Outputs

| WorkspaceManager in — WorkspaceManager in specifies a reference to the Workspace Manager on the VeriStand Gateway. Channel — Channel specifies the channel whose value you want to get. You must enter the full path to the channel, for example, Targets/Controller/Simulation Models/Models/delay_random/Inports/In1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. WorkspaceManager out — WorkspaceManager out is a reference to the workspace manager on the VeriStand Gateway. You can wire this output to other Workspace VIs. Values — Values returns the 2D array of vector values. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI VeriStand - Get Channel Value VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-get-channel-value-vi.html language=enus -->
## TOPIC 00426: NI VeriStand - Get Channel Value VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-get-channel-value-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-get-channel-value-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns values of channels on the target. You can get values for a single channel, multiple channels, or vector values for a single channel. You must manually select the polymorphic instance to use. icon

### NI VeriStand - Get Channel Value VI

Returns values of channels on the target. You can get values for a single channel, multiple channels, or vector values for a single channel. You must manually select the polymorphic instance to use.

[IMAGE alt='icon' src='ni-veristand-get-channel-value-vi.png']

- [NI VeriStand - Get Single Channel Value VI](../../../../vi-lib/ni-veristand/execution/workspace/ni-veristand-get-single-channel-value-vi.html) Returns values of channels on the target. You can get values for a single channel, multiple channels, or vector values for a single channel. You must manually select the polymorphic instance to use.
- [NI VeriStand - Get Multiple Channel Values VI](../../../../vi-lib/ni-veristand/execution/workspace/ni-veristand-get-multiple-channel-values-vi.html) Returns values of channels on the target. You can get values for a single channel, multiple channels, or vector values for a single channel. You must manually select the polymorphic instance to use.
- [NI VeriStand - Get Channel 2D Array Values VI](../../../../vi-lib/ni-veristand/execution/workspace/ni-veristand-get-channel-2d-array-values-vi.html) Returns values of channels on the target. You can get values for a single channel, multiple channels, or vector values for a single channel. You must manually select the polymorphic instance to use.

Parent topic:

Workspace

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-get-multiple-channel-values-vi.html language=enus -->
## TOPIC 00427: NI VeriStand - Get Multiple Channel Values VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-get-multiple-channel-values-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-get-multiple-channel-values-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns values of channels on the target. You can get values for a single channel, multiple channels, or vector values for a single channel. You must manually select the polymorphic instance to use. Returns the values of multiple channels. icon Inputs/Outputs cgnrn.png WorkspaceManager in WorkspaceM

### NI VeriStand - Get Multiple Channel Values VI

Returns values of channels on the target. You can get values for a single channel, multiple channels, or vector values for a single channel. You must manually select the polymorphic instance to use.

Note

[IMAGE alt='icon' src='ni-veristand-get-multiple-channel-values-vi.png']

#### Inputs/Outputs

| WorkspaceManager in — WorkspaceManager in specifies a reference to the Workspace Manager on the VeriStand Gateway. Channels — Channels specifies a list of channels whose values you want to get. You must enter the full path to the channels, for example Controller/Simulation Models/Models/delay_random/Inports/In1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. WorkspaceManager out — WorkspaceManager out is a reference to the workspace manager on the VeriStand Gateway. You can wire this output to other Workspace VIs. Values — Values returns a list of the values of the specified channels. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI VeriStand - Get Channel Value VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-get-multiple-system-nodes-data-vi.html language=unavailable -->
## TOPIC 00428: Ni Veristand Get Multiple System Nodes Data Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-get-multiple-system-nodes-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-get-multiple-system-nodes-data-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-get-single-channel-value-vi.html language=enus -->
## TOPIC 00429: NI VeriStand - Get Single Channel Value VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-get-single-channel-value-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-get-single-channel-value-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns values of channels on the target. You can get values for a single channel, multiple channels, or vector values for a single channel. You must manually select the polymorphic instance to use. icon Inputs/Outputs cgnrn.png WorkspaceManager in WorkspaceManager in specifies a reference to the Wo

### NI VeriStand - Get Single Channel Value VI

Returns values of channels on the target. You can get values for a single channel, multiple channels, or vector values for a single channel. You must manually select the polymorphic instance to use.

[IMAGE alt='icon' src='ni-veristand-get-single-channel-value-vi.png']

#### Inputs/Outputs

| WorkspaceManager in — WorkspaceManager in specifies a reference to the Workspace Manager on the VeriStand Gateway. Channel — Channel specifies the channel whose value you want to get. You must enter the full path to the channel, for example, Targets/Controller/Simulation Models/Models/delay_random/Inports/In1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. WorkspaceManager out — WorkspaceManager out is a reference to the workspace manager on the VeriStand Gateway. You can wire this output to other Workspace VIs. Value — Value returns the value of the specified channel. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI VeriStand - Get Channel Value VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-get-system-node-channel-list-vi.html language=enus -->
## TOPIC 00430: NI VeriStand - Get System Node Channel List VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-get-system-node-channel-list-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-get-system-node-channel-list-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns information about all the channels under the specified system node. icon Inputs/Outputs cgnrn.png WorkspaceManager in WorkspaceManager in specifies a reference to the Workspace Manager on the VeriStand Gateway. cstr.png StartNode ("") StartNode specifies the system node. This VI returns info

### NI VeriStand - Get System Node Channel List VI

Returns information about all the channels under the specified system node.

[IMAGE alt='icon' src='ni-veristand-get-system-node-channel-list-vi.png']

#### Inputs/Outputs

| WorkspaceManager in — WorkspaceManager in specifies a reference to the Workspace Manager on the VeriStand Gateway. StartNode ("") — StartNode specifies the system node. This VI returns information about all the channels under the specified system node. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. WorkspaceManager out — WorkspaceManager out is a reference to the workspace manager on the VeriStand Gateway. You can wire this output to other Workspace VIs. Channels — Channels returns a 1D array of information about the channels under the system node you specify in StartNode. Name — Name indicates the name of the node. FullPath — FullPath indicates the full path to the specified node. Type — Type indicates the GUID of the node. IsChannel — IsChannel indicates whether the specified node is a channel. A value of TRUE indicates the node is a channel. Channel — Channel indicates whether the channel is readable, writable, faultable, or scalable. Channel also indicates the Unit and the row and column dimensions of the node. Channel only indicates information about the node if IsChannel returns a value of TRUE. Unit — Unit indicates the unit of the channel. Unit only returns a value if IsChannel returns a value of TRUE. Readable — Readable indicates whether or not the node is readable. A value of TRUE indicates the node is readable. Writable — Writable indicates whether you can write to the node. A value of TRUE indicates the node is writable. Faultable — Faultable indicates whether the node can be faulted. A value of TRUE indicates the node is faultable. Scalable — Scalable indicates whether the specified node can be scaled. A value of TRUE indicates that a node is scalable. RowDim — RowDim indicates the row dimension of the specified node. ColumnDim — ColumnDim indicates the column dimension of the specified node. Value Table Names — Value Table Values — IsWaveform — Waveform — DataType — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| Name — Name indicates the name of the node. FullPath — FullPath indicates the full path to the specified node. Type — Type indicates the GUID of the node. IsChannel — IsChannel indicates whether the specified node is a channel. A value of TRUE indicates the node is a channel. Channel — Channel indicates whether the channel is readable, writable, faultable, or scalable. Channel also indicates the Unit and the row and column dimensions of the node. Channel only indicates information about the node if IsChannel returns a value of TRUE. Unit — Unit indicates the unit of the channel. Unit only returns a value if IsChannel returns a value of TRUE. Readable — Readable indicates whether or not the node is readable. A value of TRUE indicates the node is readable. Writable — Writable indicates whether you can write to the node. A value of TRUE indicates the node is writable. Faultable — Faultable indicates whether the node can be faulted. A value of TRUE indicates the node is faultable. Scalable — Scalable indicates whether the specified node can be scaled. A value of TRUE indicates that a node is scalable. RowDim — RowDim indicates the row dimension of the specified node. ColumnDim — ColumnDim indicates the column dimension of the specified node. Value Table Names — Value Table Values — IsWaveform — Waveform — DataType — |
| Unit — Unit indicates the unit of the channel. Unit only returns a value if IsChannel returns a value of TRUE. Readable — Readable indicates whether or not the node is readable. A value of TRUE indicates the node is readable. Writable — Writable indicates whether you can write to the node. A value of TRUE indicates the node is writable. Faultable — Faultable indicates whether the node can be faulted. A value of TRUE indicates the node is faultable. Scalable — Scalable indicates whether the specified node can be scaled. A value of TRUE indicates that a node is scalable. RowDim — RowDim indicates the row dimension of the specified node. ColumnDim — ColumnDim indicates the column dimension of the specified node. Value Table Names — Value Table Values — |
| DataType — |

Parent topic:

Workspace

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-get-system-node-children-vi.html language=enus -->
## TOPIC 00431: NI VeriStand - Get System Node Children VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-get-system-node-children-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-get-system-node-children-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns information about the nodes directly under the specified system node. icon Inputs/Outputs cgnrn.png WorkspaceManager in WorkspaceManager in specifies a reference to the Workspace Manager on the VeriStand Gateway. cstr.png Node Node specifies the system node. This VI returns information about

### NI VeriStand - Get System Node Children VI

Returns information about the nodes directly under the specified system node.

[IMAGE alt='icon' src='ni-veristand-get-system-node-children-vi.png']

#### Inputs/Outputs

| WorkspaceManager in — WorkspaceManager in specifies a reference to the Workspace Manager on the VeriStand Gateway. Node — Node specifies the system node. This VI returns information about the channels directly under the system node you specify. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. WorkspaceManager out — WorkspaceManager out is a reference to the workspace manager on the VeriStand Gateway. You can wire this output to other Workspace VIs. Nodes — Nodes returns a 1D array of information about the channels under the system node you specify in Node. Name — Name indicates the name of the node. FullPath — FullPath indicates the full path to the specified node. Type — Type indicates the GUID of the node. IsChannel — IsChannel indicates whether the specified node is a channel. A value of TRUE indicates the node is a channel. Channel — Channel indicates whether the channel is readable, writable, faultable, or scalable. Channel also indicates the Unit and the row and column dimensions of the node. Channel only indicates information about the node if IsChannel returns a value of TRUE. Unit — Unit indicates the unit of the channel. Unit only returns a value if IsChannel returns a value of TRUE. Readable — Readable indicates whether or not the node is readable. A value of TRUE indicates the node is readable. Writable — Writable indicates whether you can write to the node. A value of TRUE indicates the node is writable. Faultable — Faultable indicates whether the node can be faulted. A value of TRUE indicates the node is faultable. Scalable — Scalable indicates whether the specified node can be scaled. A value of TRUE indicates that a node is scalable. RowDim — RowDim indicates the row dimension of the specified node. ColumnDim — ColumnDim indicates the column dimension of the specified node. Value Table Names — Value Table Values — IsWaveform — Waveform — DataType — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| Name — Name indicates the name of the node. FullPath — FullPath indicates the full path to the specified node. Type — Type indicates the GUID of the node. IsChannel — IsChannel indicates whether the specified node is a channel. A value of TRUE indicates the node is a channel. Channel — Channel indicates whether the channel is readable, writable, faultable, or scalable. Channel also indicates the Unit and the row and column dimensions of the node. Channel only indicates information about the node if IsChannel returns a value of TRUE. Unit — Unit indicates the unit of the channel. Unit only returns a value if IsChannel returns a value of TRUE. Readable — Readable indicates whether or not the node is readable. A value of TRUE indicates the node is readable. Writable — Writable indicates whether you can write to the node. A value of TRUE indicates the node is writable. Faultable — Faultable indicates whether the node can be faulted. A value of TRUE indicates the node is faultable. Scalable — Scalable indicates whether the specified node can be scaled. A value of TRUE indicates that a node is scalable. RowDim — RowDim indicates the row dimension of the specified node. ColumnDim — ColumnDim indicates the column dimension of the specified node. Value Table Names — Value Table Values — IsWaveform — Waveform — DataType — |
| Unit — Unit indicates the unit of the channel. Unit only returns a value if IsChannel returns a value of TRUE. Readable — Readable indicates whether or not the node is readable. A value of TRUE indicates the node is readable. Writable — Writable indicates whether you can write to the node. A value of TRUE indicates the node is writable. Faultable — Faultable indicates whether the node can be faulted. A value of TRUE indicates the node is faultable. Scalable — Scalable indicates whether the specified node can be scaled. A value of TRUE indicates that a node is scalable. RowDim — RowDim indicates the row dimension of the specified node. ColumnDim — ColumnDim indicates the column dimension of the specified node. Value Table Names — Value Table Values — |
| DataType — |

Parent topic:

Workspace

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-get-system-state-vi.html language=unavailable -->
## TOPIC 00432: Ni Veristand Get System State Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-get-system-state-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-get-system-state-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-lock-connection-vi.html language=enus -->
## TOPIC 00433: NI VeriStand - Lock Connection VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-lock-connection-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-lock-connection-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Locks the current VeriStand Gateway connection. If the connection already is locked, you must provide the current password in order to set a new one. icon Inputs/Outputs cgnrn.png WorkspaceManager in WorkspaceManager in specifies a reference to the Workspace Manager on the VeriStand Gateway. cstr.pn

### NI VeriStand - Lock Connection VI

Locks the current VeriStand Gateway connection. If the connection already is locked, you must provide the current password in order to set a new one.

[IMAGE alt='icon' src='ni-veristand-lock-connection-vi.png']

#### Inputs/Outputs

| WorkspaceManager in — WorkspaceManager in specifies a reference to the Workspace Manager on the VeriStand Gateway. Old Password ("") — Old Password specifies the current password of the user account. New Password — New Password specifies the new password for the user account. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. WorkspaceManager out — WorkspaceManager out is a reference to the workspace manager on the VeriStand Gateway. You can wire this output to other Workspace VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

System Connection

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-open-engine-state-change-notification-vi.html language=unavailable -->
## TOPIC 00434: Ni Veristand Open Engine State Change Notification Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-open-engine-state-change-notification-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-open-engine-state-change-notification-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-open-udp-channel-streaming-session-vi.html language=enus -->
## TOPIC 00435: NI VeriStand - Open UDP Channel Streaming Session VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-open-udp-channel-streaming-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-open-udp-channel-streaming-session-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a UDP channel streaming session. Use the Deploy UDP Channel Streaming Session VI to deploy the session and begin streaming channel data. icon Inputs/Outputs cgnrn.png WorkspaceManager in WorkspaceManager in specifies a reference to the Workspace Manager on the VeriStand Gateway. c1dstr.png Cha

### NI VeriStand - Open UDP Channel Streaming Session VI

Opens a UDP channel streaming session. Use the Deploy UDP Channel Streaming Session VI to deploy the session and begin streaming channel data.

[IMAGE alt='icon' src='ni-veristand-open-udp-channel-streaming-session-vi.png']

#### Inputs/Outputs

| WorkspaceManager in — WorkspaceManager in specifies a reference to the Workspace Manager on the VeriStand Gateway. Channels — Channels specifies the channels you want to stream. You can enter an alias name or the full path to each channel, for example Targets/Controller/Simulation Models/Models/delay_random/Inports/In1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. WorkspaceManager out — WorkspaceManager out is a reference to the workspace manager on the VeriStand Gateway. You can wire this output to other Workspace VIs. UDPChannelStreamSession out — UDPChannelStreamSession out returns the reference to the channel streaming session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

UDP Channel Streaming

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-open-workspace-manager-reference-vi.html language=enus -->
## TOPIC 00436: NI VeriStand - Open Workspace Manager Reference VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-open-workspace-manager-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-open-workspace-manager-reference-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a reference to the workspace manager on the VeriStand Gateway. You must open a reference before using any other VIs on this palette. icon Inputs/Outputs cstr.png Gateway IP Address ("": localhost) Gateway IP Address specifies the IP address of the VeriStand Gateway. This address can be in IP d

### NI VeriStand - Open Workspace Manager Reference VI

Opens a reference to the workspace manager on the VeriStand Gateway. You must open a reference before using any other VIs on this palette.

[IMAGE alt='icon' src='ni-veristand-open-workspace-manager-reference-vi.png']

#### Inputs/Outputs

| Gateway IP Address ("": localhost) — Gateway IP Address specifies the IP address of the VeriStand Gateway. This address can be in IP dot notation or it can be a hostname. If you do not specify an address, LabVIEW establishes a connection to the local computer. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. WorkspaceManager — error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Workspace

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-reconnect-to-system-vi.html language=unavailable -->
## TOPIC 00437: Ni Veristand Reconnect To System Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-reconnect-to-system-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-reconnect-to-system-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-set-channel-2d-array-values-vi.html language=enus -->
## TOPIC 00438: NI VeriStand - Set Channel 2D Array Values VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-set-channel-2d-array-values-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-set-channel-2d-array-values-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets values of channels on the target. You must manually select the polymorphic instance to use. Sets the vector values of a single channel. icon Inputs/Outputs cgnrn.png WorkspaceManager in WorkspaceManager in specifies a reference to the Workspace Manager on the VeriStand Gateway. cstr.png Channel

### NI VeriStand - Set Channel 2D Array Values VI

Sets values of channels on the target. You must manually select the polymorphic instance to use.

Note

[IMAGE alt='icon' src='ni-veristand-set-channel-2d-array-values-vi.png']

#### Inputs/Outputs

| WorkspaceManager in — WorkspaceManager in specifies a reference to the Workspace Manager on the VeriStand Gateway. Channel — Channel specifies the channel whose value you want to set. You must enter the full path to the channel, for example Targets/Controller/Simulation Models/Models/delay_random/Inports/In1. Values — Values indicates the values of the specified parameter in your NI VeriStand model. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. WorkspaceManager out — WorkspaceManager out is a reference to the workspace manager on the VeriStand Gateway. You can wire this output to other Workspace VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI VeriStand - Set Channel Value VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-set-channel-value-vi.html language=enus -->
## TOPIC 00439: NI VeriStand - Set Channel Value VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-set-channel-value-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-set-channel-value-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets values of channels on the target. You must manually select the polymorphic instance to use. icon

### NI VeriStand - Set Channel Value VI

Sets values of channels on the target. You must manually select the polymorphic instance to use.

[IMAGE alt='icon' src='ni-veristand-set-channel-value-vi.png']

- [NI VeriStand - Set Single Channel Value VI](../../../../vi-lib/ni-veristand/execution/workspace/ni-veristand-set-single-channel-value-vi.html) Sets values of channels on the target. You must manually select the polymorphic instance to use.
- [NI VeriStand - Set Multiple Channel Values VI](../../../../vi-lib/ni-veristand/execution/workspace/ni-veristand-set-multiple-channel-values-vi.html) Sets values of channels on the target. You must manually select the polymorphic instance to use.
- [NI VeriStand - Set Channel 2D Array Values VI](../../../../vi-lib/ni-veristand/execution/workspace/ni-veristand-set-channel-2d-array-values-vi.html) Sets values of channels on the target. You must manually select the polymorphic instance to use.

Parent topic:

Workspace

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-set-multiple-channel-values-vi.html language=enus -->
## TOPIC 00440: NI VeriStand - Set Multiple Channel Values VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-set-multiple-channel-values-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-set-multiple-channel-values-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets values of channels on the target. You must manually select the polymorphic instance to use. Sets values of multiple channels. icon Inputs/Outputs cgnrn.png WorkspaceManager in WorkspaceManager in specifies a reference to the Workspace Manager on the VeriStand Gateway. c1dstr.png Channels Channe

### NI VeriStand - Set Multiple Channel Values VI

Sets values of channels on the target. You must manually select the polymorphic instance to use.

Note

[IMAGE alt='icon' src='ni-veristand-set-multiple-channel-values-vi.png']

#### Inputs/Outputs

| WorkspaceManager in — WorkspaceManager in specifies a reference to the Workspace Manager on the VeriStand Gateway. Channels — Channels specifies the channels whose values you want to set. You must enter the full path to each channel, for example Targets/Controller/Simulation Models/Models/delay_random/Inports/In1. Values — Values specifies the values to set for the channels you specify in Channels. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. WorkspaceManager out — WorkspaceManager out is a reference to the workspace manager on the VeriStand Gateway. You can wire this output to other Workspace VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI VeriStand - Set Channel Value VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-set-single-channel-value-vi.html language=unavailable -->
## TOPIC 00441: Ni Veristand Set Single Channel Value Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-set-single-channel-value-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-set-single-channel-value-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-start-data-logging-vi.html language=enus -->
## TOPIC 00442: NI VeriStand - Start Data Logging VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-start-data-logging-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-start-data-logging-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Starts logging data for the specified Data Log Configuration Name. icon Inputs/Outputs cgnrn.png WorkspaceManager in WorkspaceManager in specifies a reference to the Workspace Manager on the VeriStand Gateway. cstr.png Data Log Configuration Name Data Log Configuration Name specifies the name of the

### NI VeriStand - Start Data Logging VI

Starts logging data for the specified **Data Log Configuration Name**.

[IMAGE alt='icon' src='ni-veristand-start-data-logging-vi.png']

#### Inputs/Outputs

| WorkspaceManager in — WorkspaceManager in specifies a reference to the Workspace Manager on the VeriStand Gateway. Data Log Configuration Name — Data Log Configuration Name specifies the name of the configuration for which to start logging. Data Log File Configuration — Data Log File Configuration specifies data log file configuration settings. File Path — File Path specifies the file path for the data log file. The file must be a TDMS file. Description — Description specifies the description for the data log file. Trigger — Trigger specifies trigger settings. Type — Type specifies the type of trigger to use for the log file. 0 None—No trigger specified. 1 In Limits—Triggers when the watched channel is within specified limits. 2 Out of Limits—Triggers when the watched channel is outside specified limits. Channel Path — Channel Path specifies the path to the channel, as specified in the system definition file, on which to perform trigger limit analysis. The path matches the node hierarchy that appears in the System Explorer window configuration tree. High Limit — High Limit specifies the high limit for trigger limit analysis. Low Limit — Low Limit specifies the low limit for trigger limit analysis. Replace File — Replace File specifies whether to replace an existing log file or append data to the file. TRUE specifies to replace the log file. FALSE specifies to append data to the log file. Rate [Hz] — Rate [Hz] specifies the requested rate in Hz at which data is logged to the log file. Data is logged at the closest possible rate to this value that does not exceed the rate at which a target produces data. The default value is Inf, which specifies that all samples are logged. File Properties — File Properties specifies Name and Value property strings. These properties are written as metadata to the root item in the log file. Name — Name specifies the property name. Value — Value specifies the property value. Channels — Channels specifies the list of channels to log in the log file. Channel Path — Channel Path specifies the path to the channel, as specified in the system definition file, on which to perform trigger limit analysis. The path matches the node hierarchy that appears in the System Explorer window configuration tree. Custom Name — Custom Name specifies a custom name for the channel. Custom Group — Custom Group specifies a custom group for the channel. Properties — Properties specifies channel properties. Name — Name specifies the property name. Value — Value specifies the property value. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. WorkspaceManager out — WorkspaceManager out is a reference to the workspace manager on the VeriStand Gateway. You can wire this output to other Workspace VIs. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| File Path — File Path specifies the file path for the data log file. The file must be a TDMS file. Description — Description specifies the description for the data log file. Trigger — Trigger specifies trigger settings. Type — Type specifies the type of trigger to use for the log file. 0 None—No trigger specified. 1 In Limits—Triggers when the watched channel is within specified limits. 2 Out of Limits—Triggers when the watched channel is outside specified limits. Channel Path — Channel Path specifies the path to the channel, as specified in the system definition file, on which to perform trigger limit analysis. The path matches the node hierarchy that appears in the System Explorer window configuration tree. High Limit — High Limit specifies the high limit for trigger limit analysis. Low Limit — Low Limit specifies the low limit for trigger limit analysis. Replace File — Replace File specifies whether to replace an existing log file or append data to the file. TRUE specifies to replace the log file. FALSE specifies to append data to the log file. Rate [Hz] — Rate [Hz] specifies the requested rate in Hz at which data is logged to the log file. Data is logged at the closest possible rate to this value that does not exceed the rate at which a target produces data. The default value is Inf, which specifies that all samples are logged. File Properties — File Properties specifies Name and Value property strings. These properties are written as metadata to the root item in the log file. Name — Name specifies the property name. Value — Value specifies the property value. Channels — Channels specifies the list of channels to log in the log file. Channel Path — Channel Path specifies the path to the channel, as specified in the system definition file, on which to perform trigger limit analysis. The path matches the node hierarchy that appears in the System Explorer window configuration tree. Custom Name — Custom Name specifies a custom name for the channel. Custom Group — Custom Group specifies a custom group for the channel. Properties — Properties specifies channel properties. Name — Name specifies the property name. Value — Value specifies the property value. |  |
| Type — Type specifies the type of trigger to use for the log file. 0 None—No trigger specified. 1 In Limits—Triggers when the watched channel is within specified limits. 2 Out of Limits—Triggers when the watched channel is outside specified limits. Channel Path — Channel Path specifies the path to the channel, as specified in the system definition file, on which to perform trigger limit analysis. The path matches the node hierarchy that appears in the System Explorer window configuration tree. High Limit — High Limit specifies the high limit for trigger limit analysis. Low Limit — Low Limit specifies the low limit for trigger limit analysis. |  |
| 0 | None—No trigger specified. |
| 1 | In Limits—Triggers when the watched channel is within specified limits. |
| 2 | Out of Limits—Triggers when the watched channel is outside specified limits. |
| Name — Name specifies the property name. Value — Value specifies the property value. |  |
| Channel Path — Channel Path specifies the path to the channel, as specified in the system definition file, on which to perform trigger limit analysis. The path matches the node hierarchy that appears in the System Explorer window configuration tree. Custom Name — Custom Name specifies a custom name for the channel. Custom Group — Custom Group specifies a custom group for the channel. Properties — Properties specifies channel properties. Name — Name specifies the property name. Value — Value specifies the property value. |  |
| Name — Name specifies the property name. Value — Value specifies the property value. |  |

Parent topic:

Workspace

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-stop-data-logging-vi.html language=enus -->
## TOPIC 00443: NI VeriStand - Stop Data Logging VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-stop-data-logging-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-stop-data-logging-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops logging data for the specified Data Log Configuration Name. icon Inputs/Outputs cgnrn.png WorkspaceManager in WorkspaceManager in specifies a reference to the Workspace Manager on the VeriStand Gateway. cstr.png Data Log Configuration Name Data Log Configuration Name specifies the name of the

### NI VeriStand - Stop Data Logging VI

Stops logging data for the specified **Data Log Configuration Name**.

[IMAGE alt='icon' src='ni-veristand-stop-data-logging-vi.png']

#### Inputs/Outputs

| WorkspaceManager in — WorkspaceManager in specifies a reference to the Workspace Manager on the VeriStand Gateway. Data Log Configuration Name — Data Log Configuration Name specifies the name of the configuration for which to terminate logging. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. WorkspaceManager out — WorkspaceManager out is a reference to the workspace manager on the VeriStand Gateway. You can wire this output to other Workspace VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Workspace

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-undeploy-udp-channel-streaming-session-vi.html language=enus -->
## TOPIC 00444: NI VeriStand - Undeploy UDP Channel Streaming Session VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-undeploy-udp-channel-streaming-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-undeploy-udp-channel-streaming-session-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Undeploys a UDP channel streaming session and instructs the VeriStand Gateway to stop publishing UDP data. If a client has a request open for a channel, the VeriStand Gateway continues to publish data even after this VI executes. icon Inputs/Outputs cgnrn.png UDPChannelStreamSession in UDPChannelStr

### NI VeriStand - Undeploy UDP Channel Streaming Session VI

Undeploys a UDP channel streaming session and instructs the VeriStand Gateway to stop publishing UDP data.

Note

[IMAGE alt='icon' src='ni-veristand-undeploy-udp-channel-streaming-session-vi.png']

#### Inputs/Outputs

| UDPChannelStreamSession in — UDPChannelStreamSession in is the reference to the channel streaming session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. UDPChannelStreamSession out — UDPChannelStreamSession out returns the reference to the channel streaming session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

UDP Channel Streaming

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/workspace/ni-veristand-unlock-connection-vi.html language=unavailable -->
## TOPIC 00445: Ni Veristand Unlock Connection Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/workspace/ni-veristand-unlock-connection-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/workspace/ni-veristand-unlock-connection-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.
