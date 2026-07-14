# NI DOCUMENT BUNDLE: veristand-net-api-reference

<!--NI_BUNDLE_CHUNK bundle=veristand-net-api-reference start=1 end=250 -->
<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_dataloggingsessionstopeventargs.htm language=enus -->
## TOPIC 00001: DataLoggingSessionStopEventArgs Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_dataloggingsessionstopeventargs.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_dataloggingsessionstopeventargs.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [DataLoggingSessionStopEventArgs](t_nationalinstruments_veristand_clientapi_logging_dataloggingsessionstopeventargs.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | LogFilePaths | Gets a value indicating the paths to all log files generated during the current data logging session. |
|  | SessionName | Gets a value indicating the unique name of the data logging session. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DataLoggingSessionStopEventArgs Class

NationalInstruments.VeriStand.ClientAPI.Logging Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_dataloggingspecification.htm language=enus -->
## TOPIC 00002: DataLoggingSpecification Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_dataloggingspecification.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_dataloggingspecification.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [DataLoggingSpecification](t_nationalinstruments_veristand_clientapi_logging_dataloggingspecification.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | DataLoggingSpecification | Overloaded. Initializes a new instance of the DataLoggingSpecification class with default settings. The log is set to start immediately and log indefinitely. Data is logged at the rate at which the targets are running. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | CustomRate | Gets or sets a value indicating the requested rate in Hertz at which data will be logged. The actual rates at which data is logged may be coerced to an even divisor of the rates at which the targets in the system definition produce data. This property is ignored unless LogDataAtTargetRate is false. |
|  | LogDataAgainstAbsoluteTimeBase | Gets or sets a value indicating whether to log data against an absolute time base from the system clock on the target. If this value is false, no timing informating will be added to the log file. |
|  | LogDataAtTargetRate | Gets or sets a value indicating whether data is logged at the rate at which the target is running. Set this property to true to log all data produced by a target. If this property is false, data is logged using the rate specified by CustomRate. |
|  | LogFile | Gets or sets a value indicating the log file specification for the data logging session. This includes information about the type of log files to create and the channels to log. |
|  | MinimumBufferSize | Gets or sets a value indicating the minimum size of data buffered while logging. Increasing the minimum buffer size can improve logging performance but requires additional memory resources. |
|  | PostTriggerDuration | Gets or sets a value indicating the duration in seconds of data that is logged after the stop trigger condition occurs. |
|  | PreTriggerDuration | Gets or sets a value indicating the duration in seconds of data that is logged before the start trigger condition occurs. |
|  | Retriggerable | Gets or sets a value indicating whether logging is retriggerable. If this is true, then data logging can be triggered by the start trigger condition after it has completed logging data from the previous start trigger instance. |
|  | SegmentFileOnTrigger | Gets or sets a value indicating whether to create a new file instance each time the start trigger condition occurs. Segmenting the log file for each start trigger instance ensures that all data logged to a file is contiguous in time. |
|  | SegmentingSpecification | Gets or sets a value indicating the condition that determines when to segment a log file. When the condition occurs, the current instance of the log file is closed, and data continues to be logged to a new log file instance. |
|  | SetLogFilesReadOnlyOnClose | Gets or sets a value indicating whether log files should be set as read-only after being closed. |
|  | StartTrigger | Gets or sets a value indicating the condition used to determine when to start logging. |
|  | StopLogOnDataLoss | Gets or sets a value indicating whether to stop logging data in the case of data loss. The default value is true. If this value is false and data loss occurs, an error will be generated, but data logging will continue. |
|  | StopTrigger | Gets or sets a value indicating the condition used to determine when to stop logging. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DataLoggingSpecification Class

NationalInstruments.VeriStand.ClientAPI.Logging Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_defaulttrigger.htm language=enus -->
## TOPIC 00003: DefaultTrigger Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_defaulttrigger.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_defaulttrigger.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [DefaultTrigger](t_nationalinstruments_veristand_clientapi_logging_defaulttrigger.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | DefaultTrigger | Initializes a new instance of the DefaultTrigger class. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | DefaultResult | Gets or sets a value indicating whether the trigger always evaluates to true or false. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DefaultTrigger Class

NationalInstruments.VeriStand.ClientAPI.Logging Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_digitaledgetrigger.htm language=enus -->
## TOPIC 00004: DigitalEdgeTrigger Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_digitaledgetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_digitaledgetrigger.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [DigitalEdgeTrigger](t_nationalinstruments_veristand_clientapi_logging_digitaledgetrigger.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | DigitalEdgeTrigger | Initializes a new instance of the DigitalEdgeTrigger class. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | ChannelPath | Gets or sets a value indicating the system definition path of the channel to monitor. (Inherited from SingleChannelTrigger.) |
|  | Slope | Gets or sets a value indicating whether the slope is rising or falling. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DigitalEdgeTrigger Class

NationalInstruments.VeriStand.ClientAPI.Logging Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_idatalogging.htm language=enus -->
## TOPIC 00005: IDataLogging Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_idatalogging.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_idatalogging.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [IDataLogging](t_nationalinstruments_veristand_clientapi_logging_idatalogging.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | GetAllCompleteLogFiles | Returns the file paths of all log files generated by the data logging session. |
|  | GetAllDataLoggingSessionsNames | Returns the session names of all data logging sessions. |
|  | GetCurrentLogFileInfo | Returns information about the current log file for the data logging session. |
|  | GetDataLoggingSessionSpecification | Returns the data logging specification for the data logging session. |
|  | GetDataLoggingSessionState | Returns the state of the data logging session. |
|  | GetLastError | Returns the last error generated by the data logging session. If no error has been generated, the Code property of the Error object is 0. |
|  | StartDataLoggingSession | Starts a new data logging session. |
|  | StopDataLoggingSession | Stops the data logging session. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | DataLoggingSessionError | Callback invoked when a data logging session produces an error. |
|  | DataLoggingSessionStart | Callback invoked when a new data logging session starts. |
|  | DataLoggingSessionStateChange | Callback invoked when a data logging session changes state. |
|  | DataLoggingSessionStop | Callback invoked when a data logging session stops. |
|  | LogFileClosed | Callback invoked when a data logging session on the host computer closes a log file. |
|  | LogFileOpened | Callback invoked when a data logging session on the host computer opens a log file. |
|  | NewLogFilesComplete | Callback invoked when a target generates a new log file. Features that perform logging on a target rather than the host, such as DAQ tasks and XNET raw frame data logging, generate this event. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IDataLogging Interface

NationalInstruments.VeriStand.ClientAPI.Logging Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_inrangetrigger.htm language=enus -->
## TOPIC 00006: InRangeTrigger Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_inrangetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_inrangetrigger.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [InRangeTrigger](t_nationalinstruments_veristand_clientapi_logging_inrangetrigger.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | InRangeTrigger | Initializes a new instance of the InRangeTrigger class. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | ChannelPath | Gets or sets a value indicating the system definition path of the channel to monitor. (Inherited from SingleChannelTrigger.) |
|  | HighLimit | Gets or sets a value indicating the high limit of the range. |
|  | Invert | Gets or sets a value indicating whether to invert the range check. If the range check is inverted, then the trigger condition occurs when the value falls outside the specified range. |
|  | LowLimit | Gets or sets a value indicating the low limit of the range. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

InRangeTrigger Class

NationalInstruments.VeriStand.ClientAPI.Logging Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_newlogfilescompleteeventargs.htm language=enus -->
## TOPIC 00007: NewLogFilesCompleteEventArgs Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_newlogfilescompleteeventargs.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_newlogfilescompleteeventargs.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [NewLogFilesCompleteEventArgs](t_nationalinstruments_veristand_clientapi_logging_newlogfilescompleteeventargs.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | LogFilePaths | Gets a value indicating the paths to all newly produced log files. |
|  | Source | Gets a value indicating the feature that generated the log files, such as a waveform DAQ task or the Embedded Data Logger custom device. |
|  | Target | Gets a value indicating the name of the target that contains the log files. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

NewLogFilesCompleteEventArgs Class

NationalInstruments.VeriStand.ClientAPI.Logging Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_tdmschannel.htm language=enus -->
## TOPIC 00008: TdmsChannel Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_tdmschannel.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_tdmschannel.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [TdmsChannel](t_nationalinstruments_veristand_clientapi_logging_tdmschannel.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | TdmsChannel | Initializes a new instance of the TdmsChannel class. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | AddProperty | Overloaded. Adds the specified TdmsProperty to the TdmsChannel. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetProperty | Returns the specified TDMS property associated with this TdmsChannel. |
|  | GetPropertyNames | Returns an array of property names for the TDMS channel. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | ChannelPath | Gets or sets a value indicating the system definition path of the channel to log. |
|  | Description | Gets or sets a value indicating the description of the TDMS channel. |
|  | Name | Gets or sets a value indicating the name of the TDMS channel. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

TdmsChannel Class

NationalInstruments.VeriStand.ClientAPI.Logging Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_tdmsproperty.htm language=enus -->
## TOPIC 00009: TdmsProperty Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_tdmsproperty.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_tdmsproperty.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [TdmsProperty](t_nationalinstruments_veristand_clientapi_logging_tdmsproperty.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | TdmsProperty | Initializes a new instance of the TdmsProperty class. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | DataType | Gets a value indicating the data type of the TdmsProperty |
|  | Name | Gets a value indicating the name of the TdmsProperty |
|  | Value | Gets or sets a value indicating the value of the TdmsProperty |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

TdmsProperty Class

NationalInstruments.VeriStand.ClientAPI.Logging Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_textlogchannel.htm language=enus -->
## TOPIC 00010: TextLogChannel Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_textlogchannel.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_textlogchannel.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [TextLogChannel](t_nationalinstruments_veristand_clientapi_logging_textlogchannel.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | TextLogChannel | Initializes a new instance of the TextLogChannel class. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | ChannelPath | Gets or sets a value indicating the system definition path of the channel to log. |
|  | IncludeChannelUnitsInName | Gets or sets a value indicating whether to include the units of the channel to log in the column header. |
|  | Name | Gets or sets a value indicating the name of the channel in the text file column header. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

TextLogChannel Class

NationalInstruments.VeriStand.ClientAPI.Logging Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_textlogfile.htm language=enus -->
## TOPIC 00011: TextLogFile Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_textlogfile.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_textlogfile.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [TextLogFile](t_nationalinstruments_veristand_clientapi_logging_textlogfile.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | TextLogFile | Initializes a new instance of the TextLogFile class. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | AddChannel | Overloaded. Adds the specified channel to the list of channels to log. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | BaseFilePath | Gets or sets a value indicating the base file path used to specify the log file path (Inherited from LogFile.) |
|  | Channels | Gets a value indicating the channels to log |
|  | DecimalPlaces | Gets or sets a value indicating the number of decimal places used when converting the numeric log data to string |
|  | Delimiter | Gets or sets a value indicating the delimiter between columns in the text file |
|  | FileConflictOperation | Gets or sets a value indicating the operation to take if a file already exists at the specified path (Inherited from LogFile.) |
|  | HeaderText | Gets or sets a value indicating the header text to insert at the beginning of the text log file. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

TextLogFile Class

NationalInstruments.VeriStand.ClientAPI.Logging Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_valuechangetrigger.htm language=enus -->
## TOPIC 00012: ValueChangeTrigger Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_valuechangetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_logging_valuechangetrigger.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [ValueChangeTrigger](t_nationalinstruments_veristand_clientapi_logging_valuechangetrigger.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | ValueChangeTrigger | Initializes a new instance of the ValueChangeTrigger class |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | ChannelPath | Gets or sets a value indicating the system definition path of the channel to monitor. (Inherited from SingleChannelTrigger.) |
|  | Deadband | Gets or sets a value indicating the deadband. The absolute difference of the change in the channel value must be greater than this amount for the trigger condition to occur. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ValueChangeTrigger Class

NationalInstruments.VeriStand.ClientAPI.Logging Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_loginfo.htm language=enus -->
## TOPIC 00013: LogInfo Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_loginfo.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_loginfo.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [LogInfo](t_nationalinstruments_veristand_clientapi_loginfo.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | LogInfo | Initializes a new instance of the LogInfo class. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Fields

|  | Name | Description |
| --- | --- | --- |
|  | channels | The list of channels to log in the log file. |
|  | description | The description for the data log file. |
|  | file_path | The file path for the data log file. The file must be a TDMS file. |
|  | high_limit | The high limit for trigger limit analysis. |
|  | low_limit | The low limit for trigger limit analysis. |
|  | rate | The requested rate in Hz at which data is logged to the log file. Data is logged at the closest possible rate to this value that does not exceed the rate at which a target produces data. The default value is Inf, which specifies that all samples are logged. |
|  | replace_file | A flag specifying whether to replace an existing log file or append data to the file. TRUE specifies to replace the log file. FALSE specifies to append data to the log file. |
|  | root_properties | A dictionary containing property name and property value strings. These properties are written as metadata to the root item in the log file. |
|  | trigger_channel | The path to the channel, as specified in the system definition file, on which to perform trigger limit analysis. The path matches the node hierarchy that appears in the System Explorer window configuration tree. |
|  | trigger_type | The type of LogInfo.trigger to use for the log file. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

LogInfo Class

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_nodeinfo.htm language=enus -->
## TOPIC 00014: NodeInfo Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_nodeinfo.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_nodeinfo.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [NodeInfo](t_nationalinstruments_veristand_clientapi_nodeinfo.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | NodeInfo | Initializes a new instance of the NodeInfo class. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Fields

|  | Name | Description |
| --- | --- | --- |
|  | ChannelColumnDimension | The number of columns in a channel node value. |
|  | ChannelRowDimension | The number of rows in a channel node value. |
|  | ChannelUnit | The unit associated with a channel node value. |
|  | FullPath | The full path to a node, as specified in the system definition file. The path matches the node hierarchy that appears in the System Explorer window configuration tree. |
|  | IsChannel | TRUE if a node is a channel. |
|  | IsFaultable | TRUE if a node can be faulted. |
|  | IsReadable | TRUE if you can read from a node. |
|  | IsScalable | TRUE if you can scale a node. |
|  | IsWaveform | TRUE if a node is a waveform. |
|  | IsWritable | TRUE if you can write to a node. |
|  | Name | The name of a node in the system definition file. |
|  | Type | The GUID of a node in the system definition file. |
|  | WaveformDataType | The data type of a waveform node. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

NodeInfo Class

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_parametervaluechangeeventargs.htm language=enus -->
## TOPIC 00015: ParameterValueChangeEventArgs Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_parametervaluechangeeventargs.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_parametervaluechangeeventargs.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [ParameterValueChangeEventArgs](t_nationalinstruments_veristand_clientapi_parametervaluechangeeventargs.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | ParameterValueChangeEventArgs | Initializes a new instance of the ParameterValueChangeEventArgs class. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | NewValue | Gets a value indicating the new value of the model parameter. |
|  | ParameterName | Gets a value indicating the name of the model parameter whose value changed. |
|  | Target | Gets a value indicating the name of the target to which the new model parameter value was applied. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ParameterValueChangeEventArgs Class

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_sequencecallinfo.htm language=enus -->
## TOPIC 00016: SequenceCallInfo Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_sequencecallinfo.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_sequencecallinfo.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SequenceCallInfo](t_nationalinstruments_veristand_clientapi_sequencecallinfo.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | SequenceCallInfo | Initializes a new instance of SequenceCallInfo. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Debug | Gets whether the sequence executes in debug mode. |
|  | ParameterAssignments | Gets the parameter assignments for the sequence. |
|  | SequencePath | Gets the file path of the sequence file to execute. |
|  | Target | Gets the name of the target on which to execute the sequence. |
|  | Timeout | Gets the timeout in milliseconds within which the sequence must complete a time step. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SequenceCallInfo Class

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_sequencecompleteeventargs.htm language=enus -->
## TOPIC 00017: SequenceCompleteEventArgs Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_sequencecompleteeventargs.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_sequencecompleteeventargs.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SequenceCompleteEventArgs](t_nationalinstruments_veristand_clientapi_sequencecompleteeventargs.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | SequenceCompleteEventArgs | Initializes a new instance of SequenceCompleteEventArgs with the specified ReturnValue. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Aborted | Gets whether the sequence execution was aborted. |
|  | Error | Gets the final error state of the sequence execution. |
|  | ReturnValue | Gets the return value for the completed sequence. Return values generally indicate some type of pass/fail information, and can be any data type. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SequenceCompleteEventArgs Class

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_sequencestatechangeeventargs.htm language=enus -->
## TOPIC 00018: SequenceStateChangeEventArgs Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_sequencestatechangeeventargs.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_clientapi_sequencestatechangeeventargs.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SequenceStateChangeEventArgs](t_nationalinstruments_veristand_clientapi_sequencestatechangeeventargs.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | SequenceStateChangeEventArgs | Initializes a new instance of SequenceStateChangeEventArgs. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | aborted | Gets whether sequence execution is aborted. |
|  | state | Gets the execution SequenceState of the sequence. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SequenceStateChangeEventArgs Class

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_data_booleanvaluearray.htm language=enus -->
## TOPIC 00019: BooleanValueArray Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_data_booleanvaluearray.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_data_booleanvaluearray.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [BooleanValueArray](t_nationalinstruments_veristand_data_booleanvaluearray.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | BooleanValueArray | Overloaded. Initializes a new instance of BooleanValueArray with an empty array of BooleanValue objects. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Clone | Creates a new object that is a copy of the current data resource. (Inherited from DataResource.) |
|  | Equals | Overloaded. Returns a value indicating whether this instance is equal to the specified object, which must be a DataValue object. This method uses Body and the CaseValue to determine equivalency. |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | FromString | Builds the current DataValueArray(T) from the specified string. (Inherited from DataValueArray(T).) |
|  | GetBytes | Returns DataValueArray(T) as an array of bytes. (Inherited from DataValueArray(T).) |
|  | GetHashCode | Serves as a hash function for a DataValue object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. (Inherited from DataValue.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | GetValues | Returns the values of DataValueArray(T). (Inherited from DataValueArray(T).) |
|  | IsEqualTo | Overloaded. Determines whether the specified DataValueArray is equal to the current DataValueArray. |
|  | IsGreaterThan | Overloaded. Determines whether the value of each element in the current DataValueArray is greater than the corresponding value in the specified DataValueArray. |
|  | IsGreaterThanOrEqualTo | Overloaded. Determines whether the value of each element in the current DataValueArray is greater than or equal to the corresponding value in the specified DataValueArray. |
|  | IsLessThan | Overloaded. Determines whether the value of each element in the current DataValueArray is less than the corresponding value in the specified DataValueArray. |
|  | IsLessThanOrEqualTo | Overloaded. Determines whether the value of each element in the current DataValueArray is less than or equal to the corresponding value in the specified DataValueArray. |
|  | IsNotEqualTo | Overloaded. Determines whether the value of each element in the current DataValueArray is not equal to the corresponding value in the specified DataValueArray. |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | SetBytes | Sets DataValueArray(T) based on Bytes. (Inherited from DataValueArray(T).) |
|  | ToString | Returns a string representation of DataValueArray(T) (Inherited from DataValueArray(T).) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | ChildType | Gets the data type of the elements in DataValueArray(T). (Inherited from DataValueArray(T).) |
|  | Item | Gets or sets the element at the specified index. (Inherited from DataValueArray(T).) |
|  | Length | Gets the total number of elements in DataValueArray(T). (Inherited from DataValueArray(T).) |
|  | Size | Gets the number of elements in each dimension of DataValueArray(T). (Inherited from DataValueArray(T).) |
|  | Type | Gets the data type of DataValueArray. (Inherited from DataValueArray.) |
|  | Units | Gets or sets the units of the data value. Units can be any string that makes sense for the data value. (Inherited from DataValue.) |
|  | Value | Gets or sets an array of values in DataValueArray(T). (Inherited from DataValueArray(T).) |
|  | ValueAsString | Gets or sets a string representation of the values in DataValueArray(T). (Inherited from DataValueArray(T).) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from DataResource.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

BooleanValueArray Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_data_i32value.htm language=enus -->
## TOPIC 00020: I32Value Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_data_i32value.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_data_i32value.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [I32Value](t_nationalinstruments_veristand_data_i32value.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | I32Value | Overloaded. Initializes a new instance of I32Value. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Clone | Creates a new object that is a copy of the current data resource. (Inherited from DataResource.) |
|  | CompareTo | Overloaded. Compares this instance to a specified object and returns an integer that indicates their relationship to each other. |
|  | Equals | Overloaded. Returns a value indicating whether this instance is equal to the specified object, which must be a DataValue object. This method uses Body and the CaseValue to determine equivalency. |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | FromString | Converts the specified string to its Int32 equivalent. (Overrides ScalarDataValue.FromString(String).) |
|  | GetBytes | Returns the 32-bit signed integer as an array of bytes. (Overrides DataValue.GetBytes().) |
|  | GetHashCode | Serves as a hash function for a DataValue object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. (Inherited from DataValue.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | SetBytes | Sets the value of I32Value based on Bytes. (Overrides DataValue.SetBytes(Byte[]).) |
|  | ToBoolean | Returns if this instance is a nonzero value. (Overrides ScalarDataValue.ToBoolean().) |
|  | ToDouble | Returns the value of this instance as a double-precision floating point number. (Overrides ScalarDataValue.ToDouble().) |
|  | ToInt32 | Returns the value of this instance as an equivalent 32-bit signed integer. (Overrides ScalarDataValue.ToInt32().) |
|  | ToInt64 | Returns the value of this instance as an equivalent 64-bit signed integer. (Overrides ScalarDataValue.ToInt64().) |
|  | ToString | Returns the value of this instance as an equivalent string. (Overrides Object.ToString().) |
|  | ToUInt32 | Returns the value of this instance as an equivalent 32-bit unsigned integer. (Overrides ScalarDataValue.ToUInt32().) |
|  | ToUInt64 | Returns the value of this instance as an equivalent 64-bit unsigned integer. (Overrides ScalarDataValue.ToUInt64().) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Size | Gets the size of the 32-bit signed integer. (Overrides DataValue.Size.) |
|  | Type | Gets the data type of the 32-bit signed integer. (Overrides DataValue.Type.) |
|  | Units | Gets or sets the units of the data value. Units can be any string that makes sense for the data value. (Inherited from DataValue.) |
|  | Value | Gets or sets the value of the 32-bit signed integer. |
|  | ValueAsString | Gets or sets the value as a string. (Inherited from ScalarDataValue.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from DataResource.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

I32Value Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_data_i64value.htm language=enus -->
## TOPIC 00021: I64Value Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_data_i64value.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_data_i64value.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [I64Value](t_nationalinstruments_veristand_data_i64value.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | I64Value | Overloaded. Initializes a new instance of I64Value. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Clone | Creates a new object that is a copy of the current data resource. (Inherited from DataResource.) |
|  | CompareTo | Overloaded. Compares this instance to a specified object and returns an integer that indicates their relationship to each other. |
|  | Equals | Overloaded. Returns a value indicating whether this instance is equal to the specified object, which must be a DataValue object. This method uses Body and the CaseValue to determine equivalency. |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | FromString | Converts the specified string to its Int64 equivalent. (Overrides ScalarDataValue.FromString(String).) |
|  | GetBytes | Returns the 64-bit signed integer as an array of bytes. (Overrides DataValue.GetBytes().) |
|  | GetHashCode | Serves as a hash function for a DataValue object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. (Inherited from DataValue.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | SetBytes | Sets the value of I64Value based on Bytes. (Overrides DataValue.SetBytes(Byte[]).) |
|  | ToBoolean | Returns if this instance is a nonzero value. (Overrides ScalarDataValue.ToBoolean().) |
|  | ToDouble | Returns the value of this instance as a double-precision floating point number. (Overrides ScalarDataValue.ToDouble().) |
|  | ToInt32 | Returns the value of this instance as an equivalent 32-bit signed integer. (Overrides ScalarDataValue.ToInt32().) |
|  | ToInt64 | Returns the value of this instance as an equivalent 64-bit signed integer. (Overrides ScalarDataValue.ToInt64().) |
|  | ToString | Returns the value of this instance as an equivalent string. (Overrides Object.ToString().) |
|  | ToUInt32 | Returns the value of this instance as an equivalent 32-bit unsigned integer. (Overrides ScalarDataValue.ToUInt32().) |
|  | ToUInt64 | Returns the value of this instance as an equivalent 64-bit unsigned integer. (Overrides ScalarDataValue.ToUInt64().) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Size | Gets the size of the 64-bit signed integer. (Overrides DataValue.Size.) |
|  | Type | Gets the data type of the 64-bit signed integer. (Overrides DataValue.Type.) |
|  | Units | Gets or sets the units of the data value. Units can be any string that makes sense for the data value. (Inherited from DataValue.) |
|  | Value | Gets or sets the value of the 64-bit signed integer. |
|  | ValueAsString | Gets or sets the value as a string. (Inherited from ScalarDataValue.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from DataResource.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

I64Value Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_data_voidvalue.htm language=enus -->
## TOPIC 00022: VoidValue Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_data_voidvalue.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_data_voidvalue.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [VoidValue](t_nationalinstruments_veristand_data_voidvalue.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | VoidValue | Overloaded. Initializes a new instance of VoidValue. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Clone | Creates a new object that is a copy of the current data resource. (Inherited from DataResource.) |
|  | CompareTo | Overloaded. Compares this instance to a specified object and returns an integer that indicates their relationship to each other. |
|  | Equals | Overloaded. Returns a value indicating whether this instance is equal to the specified object, which must be a DataValue object. This method uses Body and the CaseValue to determine equivalency. |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | FromString | Converts the specified string to an empty string. (Overrides ScalarDataValue.FromString(String).) |
|  | GetBytes | Returns the data value as an array of bytes. (Inherited from DataValue.) |
|  | GetHashCode | Serves as a hash function for a DataValue object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. (Inherited from DataValue.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | SetBytes | Sets the value of VoidValue based on Bytes. Using this method has no effect. (Overrides DataValue.SetBytes(Byte[]).) |
|  | ToBoolean | Returns false (False in Visual Basic). (Overrides ScalarDataValue.ToBoolean().) |
|  | ToDouble | Returns a a value that is not a number (NaN). (Overrides ScalarDataValue.ToDouble().) |
|  | ToInt32 | Returns zero as a 32-bit signed integer. (Overrides ScalarDataValue.ToInt32().) |
|  | ToInt64 | Returns zero as a 64-bit signed integer. (Overrides ScalarDataValue.ToInt64().) |
|  | ToString | Returns a string representation of zero. (Overrides Object.ToString().) |
|  | ToUInt32 | Returns zero as a 32-bit unsigned integer. (Overrides ScalarDataValue.ToUInt32().) |
|  | ToUInt64 | Returns zero as a 64-bit unsigned integer. (Overrides ScalarDataValue.ToUInt64().) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Size | Gets the size of the void value. (Overrides DataValue.Size.) |
|  | Type | Gets the data type of the void value. (Overrides DataValue.Type.) |
|  | Units | Gets or sets the units of the data value. Units can be any string that makes sense for the data value. (Inherited from DataValue.) |
|  | ValueAsString | Gets or sets the value as a string. (Inherited from ScalarDataValue.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from DataResource.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

VoidValue Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_realtimesequencedefinitionapi_abstractloop.htm language=enus -->
## TOPIC 00023: AbstractLoop Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_realtimesequencedefinitionapi_abstractloop.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_realtimesequencedefinitionapi_abstractloop.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [AbstractLoop](t_nationalinstruments_veristand_realtimesequencedefinitionapi_abstractloop.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | AbstractLoop | Overloaded. Initializes a new instance of AbstractLoop. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | AddStatement | Adds the specified statement to the end of the loop body. |
|  | ClearStatements | Clears all statements from the loop. |
|  | Clone | Creates a new object that is a copy of the current instance. (Inherited from BaseNode.) |
|  | Equals | Overloaded. Determines whether the specified other object is equal to the current instance of Statement. This is an abstract declaration only. Derived classes must implement the correct Equals comparison for that class. |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a Statement object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. This is an abstract declaration only. Derived classes must implement the correct GetHashCode comparison for that class. (Inherited from Statement.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | AutoYield | Gets or sets whether the loop automatically yields control of the CPU to the next task at the end of each iteration. |
|  | Body | Gets or sets the set of statements that execute in the loop. |
|  | Description | Gets or sets the description of the node that appears in the Property Browser when you select the node in the Stimulus Profile Editor. (Inherited from BaseNode.) |
|  | ResXKey | Gets or sets the ResX key for the node, which is a pointer to a .resx file that contains a context help description for the node. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

AbstractLoop Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_realtimesequencedefinitionapi_basenode.htm language=enus -->
## TOPIC 00024: BaseNode Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_realtimesequencedefinitionapi_basenode.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_realtimesequencedefinitionapi_basenode.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [BaseNode](t_nationalinstruments_veristand_realtimesequencedefinitionapi_basenode.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | BaseNode | Overloaded. Initializes a new instance of BaseNode. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Clone | Creates a new object that is a copy of the current instance. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Description | Gets or sets the description of the node that appears in the Property Browser when you select the node in the Stimulus Profile Editor. |
|  | ResXKey | Gets or sets the ResX key for the node, which is a pointer to a .resx file that contains a context help description for the node. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

BaseNode Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_realtimesequencedefinitionapi_block.htm language=enus -->
## TOPIC 00025: Block Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_realtimesequencedefinitionapi_block.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_realtimesequencedefinitionapi_block.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [Block](t_nationalinstruments_veristand_realtimesequencedefinitionapi_block.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | Block | Overloaded. Initializes a new instance of Block. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | AddStatement | Adds the specified functional statement to the end of the current block. |
|  | ClearStatements | Clears all the functional statements from the current block. |
|  | Clone | Creates a new object that is a copy of the current instance. (Inherited from BaseNode.) |
|  | Equals | Overloaded. Determines whether the specified other object is equal to the current instance of Block. Equivalency is determined using the Statements in the block. |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a Block object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. (Overrides Statement.GetHashCode().) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Description | Gets or sets the description of the node that appears in the Property Browser when you select the node in the Stimulus Profile Editor. (Inherited from BaseNode.) |
|  | Name | Gets or sets the name of the block. |
|  | ResXKey | Gets or sets the ResX key for the node, which is a pointer to a .resx file that contains a context help description for the node. (Inherited from BaseNode.) |
|  | Statements | Get or sets the set of functional statements that the block contains and that execute when the block executes. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Block Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_realtimesequencedefinitionapi_main.htm language=enus -->
## TOPIC 00026: Main Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_realtimesequencedefinitionapi_main.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_realtimesequencedefinitionapi_main.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [Main](t_nationalinstruments_veristand_realtimesequencedefinitionapi_main.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | Main | Overloaded. Initializes a new instance of Main. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | AddStatement | Adds the specified functional statement to the end of the current section of code. (Inherited from CodeSection.) |
|  | ClearStatements | Clears all the functional statements from the current section of code. (Inherited from CodeSection.) |
|  | Clone | Creates a new object that is a copy of the current instance. (Inherited from BaseNode.) |
|  | Equals | Overloaded. Determines whether the specified other object is equal to the current instance of CodeSection. Equivalency is determined using the Body code block. |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a CodeSection object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. (Inherited from CodeSection.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Body | Gets or sets the body of the code section, which contains all the blocks and statements in the section. (Inherited from CodeSection.) |
|  | Description | Gets or sets the description of the node that appears in the Property Browser when you select the node in the Stimulus Profile Editor. (Inherited from BaseNode.) |
|  | ResXKey | Gets or sets the ResX key for the node, which is a pointer to a .resx file that contains a context help description for the node. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Main Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_realtimesequencedefinitionapi_multilinestringattribute.htm language=enus -->
## TOPIC 00027: MultilineStringAttribute Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_realtimesequencedefinitionapi_multilinestringattribute.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_realtimesequencedefinitionapi_multilinestringattribute.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [MultilineStringAttribute](t_nationalinstruments_veristand_realtimesequencedefinitionapi_multilinestringattribute.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | MultilineStringAttribute | Initializes a new instance of the MultilineStringAttribute class. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Returns a value that indicates whether this instance is equal to a specified object. (Inherited from Attribute.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Returns the hash code for this instance. (Inherited from Attribute.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | IsDefaultAttribute | When overridden in a derived class, indicates whether the value of this instance is the default value for the derived class. (Inherited from Attribute.) |
|  | Match | When overridden in a derived class, returns a value that indicates whether this instance equals a specified object. (Inherited from Attribute.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | TypeId | When implemented in a derived class, gets a unique identifier for this Attribute. (Inherited from Attribute.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

MultilineStringAttribute Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_realtimesequencedefinitionapi_propertyuidisplayattribute.htm language=enus -->
## TOPIC 00028: PropertyUIDisplayAttribute Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_realtimesequencedefinitionapi_propertyuidisplayattribute.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_realtimesequencedefinitionapi_propertyuidisplayattribute.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [PropertyUIDisplayAttribute](t_nationalinstruments_veristand_realtimesequencedefinitionapi_propertyuidisplayattribute.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | PropertyUIDisplayAttribute | Initializes a new instance of the PropertyUIDisplayAttribute class with the specified identifier class. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Returns a value that indicates whether this instance is equal to a specified object. (Inherited from Attribute.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Returns the hash code for this instance. (Inherited from Attribute.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | IsDefaultAttribute | When overridden in a derived class, indicates whether the value of this instance is the default value for the derived class. (Inherited from Attribute.) |
|  | Match | When overridden in a derived class, returns a value that indicates whether this instance equals a specified object. (Inherited from Attribute.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | DottedProperty | Gets or sets the dotted property. A dotted property allows you to access properties of the object returned by a calling property. For example, if a property with the attribute (Foo) returns an object with a property Bar, specifying Bar as the dotted property specifies to access Foo.Bar in place of Foo. |
|  | Identifier | Gets the identifier, or name, for the property. |
|  | TypeId | When implemented in a derived class, gets a unique identifier for this Attribute. (Inherited from Attribute.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

PropertyUIDisplayAttribute Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_realtimesequencedefinitionapi_realtimesequence.htm language=enus -->
## TOPIC 00029: RealTimeSequence Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_realtimesequencedefinitionapi_realtimesequence.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_realtimesequencedefinitionapi_realtimesequence.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [RealTimeSequence](t_nationalinstruments_veristand_realtimesequencedefinitionapi_realtimesequence.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | RealTimeSequence | Overloaded. Initializes a new instance of the RealTimeSequence class. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Clone | Creates a new object that is a copy of the current instance. (Inherited from BaseNode.) |
|  | Equals | Overloaded. Determines whether the specified other real-time sequence is equal to the current RealTimeSequence. Equivalency is determined using the Code, References, and Variables that make up the sequence. |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | FindAllCalledSubsequencePaths | Finds all of the sub-sequences that the current real-time sequence calls and returns an array of file paths to the sub-sequences. |
|  | GetHashCode | Serves as a hash function for a RealTimeSequence. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. (Overrides Object.GetHashCode().) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | SaveSequence | Saves the real-time sequence to the specified file name and location. |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Code | Gets or sets the Code section of a sequence, which is the top-level container for all sequence code and contains the Setup, Main, and CleanUp sections. |
|  | Description | Gets or sets the description of the node that appears in the Property Browser when you select the node in the Stimulus Profile Editor. (Inherited from BaseNode.) |
|  | FileFormatVersion | Gets or sets the file format version of the real-time sequence definition file. (Inherited from RootNode.) |
|  | FileName | Gets the name of the real-time sequence definition file on disk. (Inherited from RootNode.) |
|  | FilePath | Gets the full path on disk to the real-time system definition file. Setting this property updates the value of FileName. (Inherited from RootNode.) |
|  | References | Gets or sets the References section of the real-time sequence, which is represented by the References pane in the Stimulus Profile Editor. You can use this section to add references to other real-time sequences, which allows you to call those sequences from expressions within the current sequence. |
|  | ResXKey | Gets or sets the ResX key for the node, which is a pointer to a .resx file that contains a context help description for the node. (Inherited from BaseNode.) |
|  | SequenceName | Gets the name of the real-time sequence. This name is derived from the name of the saved sequence file, and is the file name without the file extension. |
|  | Variables | Gets or sets the Variables section of the real-time sequence, which is represented by the Variables pane in the Stimulus Profile Editor. This section contains all the variables the sequence has access to at run time and can us in expressions. It includes Parameters, LocalVariables, and the ReturnDeclaration, or output value, of the sequence. |
|  | Version | Gets or sets the version of the real-time sequence definition file. (Inherited from RootNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

RealTimeSequence Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_realtimesequencedefinitionapi_references.htm language=enus -->
## TOPIC 00030: References Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_realtimesequencedefinitionapi_references.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_realtimesequencedefinitionapi_references.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [References](t_nationalinstruments_veristand_realtimesequencedefinitionapi_references.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | References | Overloaded. Initializes a new instance of References. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | AddReference | Adds the specified reference to the references list for the real-time sequence. |
|  | Clone | Creates a new object that is a copy of the current instance. (Inherited from BaseNode.) |
|  | Equals | Overloaded. Determines whether the specified other object is equal to the current References instance. Equivalency is determined using the ReferenceList. |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a References object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. (Overrides Object.GetHashCode().) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Description | Gets or sets the description of the node that appears in the Property Browser when you select the node in the Stimulus Profile Editor. (Inherited from BaseNode.) |
|  | ReferenceList | Gets or sets an array of all the defined references for the current real-time sequence. |
|  | ResXKey | Gets or sets the ResX key for the node, which is a pointer to a .resx file that contains a context help description for the node. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

References Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_realtimesequencedefinitionapi_yield.htm language=enus -->
## TOPIC 00031: Yield Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_realtimesequencedefinitionapi_yield.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_realtimesequencedefinitionapi_yield.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [Yield](t_nationalinstruments_veristand_realtimesequencedefinitionapi_yield.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | Yield | Overloaded. Initializes a new instance of Yield. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Clone | Creates a new object that is a copy of the current instance. (Inherited from BaseNode.) |
|  | Equals | Overloaded. Determines whether the specified obj, which must be a Statement object, is equal to the current instance of Statement. |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a Yield object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. (Overrides Statement.GetHashCode().) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Description | Gets or sets the description of the node that appears in the Property Browser when you select the node in the Stimulus Profile Editor. (Inherited from BaseNode.) |
|  | ResXKey | Gets or sets the ResX key for the node, which is a pointer to a .resx file that contains a context help description for the node. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Yield Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_actionstep.htm language=enus -->
## TOPIC 00032: ActionStep Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_actionstep.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_actionstep.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [ActionStep](t_nationalinstruments_veristand_stimulusprofiledefinitionapi_actionstep.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | ActionStep | Overloaded. Initializes a new instance of ActionStep. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | CheckForErrors | Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. |
|  | Clone | Creates a new object that is a copy of the current instance. (Inherited from BaseNode.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Description | Gets or sets the description of the node that appears in the Property Browser when you select the node in the Stimulus Profile Editor. (Inherited from BaseNode.) |
|  | Id | Gets the unique identifier for a step, which is the full path to the step in the stimulus profile hierarchy. |
|  | ResXKey | Gets or sets the ResX key for the node, which is a pointer to a .resx file that contains a context help description for the node. (Inherited from BaseNode.) |
|  | State | Gets the execution state of a step (Idle, Initializing, Running, and so on.) |
|  | StepName | Gets the name of a step. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ActionStep Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_alwayspassevaluation.htm language=enus -->
## TOPIC 00033: AlwaysPassEvaluation Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_alwayspassevaluation.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_alwayspassevaluation.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [AlwaysPassEvaluation](t_nationalinstruments_veristand_stimulusprofiledefinitionapi_alwayspassevaluation.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | AlwaysPassEvaluation | Overloaded. Initializes a new instance of AlwaysPassEvaluation. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Clone | Creates a clone object of the current instance. (Inherited from Evaluation.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Evaluate | Performs an AlwaysPass evaluation, which always returns true (True in Visual Basic). (Overrides Evaluation.Evaluate(DataValue).) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from Evaluation.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

AlwaysPassEvaluation Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_booleanevaluation.htm language=enus -->
## TOPIC 00034: BooleanEvaluation Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_booleanevaluation.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_booleanevaluation.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [BooleanEvaluation](t_nationalinstruments_veristand_stimulusprofiledefinitionapi_booleanevaluation.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | BooleanEvaluation | Overloaded. Initializes a new instance of BooleanEvaluation. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Clone | Creates a clone object of the current instance. (Inherited from Evaluation.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Evaluate | Performs a Boolean evaluation on the specified value. (Overrides Evaluation.Evaluate(DataValue).) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Invert | Gets or sets whether the Boolean evaluation is inverted. In an inverted evaluation, a false (False in Visual Basic) value indicates passing and a true (True in Visual Basic) value indicates failing. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from Evaluation.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

BooleanEvaluation Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_ftpdownload.htm language=enus -->
## TOPIC 00035: FTPDownload Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_ftpdownload.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_ftpdownload.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [FTPDownload](t_nationalinstruments_veristand_stimulusprofiledefinitionapi_ftpdownload.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | FTPDownload | Overloaded. Initializes a new instance of the FTPDownload class. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | CheckForErrors | Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. (Overrides FTPBase.CheckForErrors().) |
|  | Clone | Creates a new object that is a copy of the current instance. (Inherited from BaseNode.) |
|  | CreateUniqueFileName | Creates a unique filename by appending a number to proposedFileName. (Inherited from FTPBase.) |
|  | DoesFileExistOnFTPServer | Checks if the specified file already exists on the FTP server. (Inherited from FTPBase.) |
|  | DownloadFile | Downloads the specified file from the FTP server and copies it to the Destination directory. This method uses a buffer of a size specified by BufferLength. (Inherited from FTPBase.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetFileListFromDirectory | Returns the name of all files from a directory on the FTP server. This method uses the proxy server settings, including ProxyUserName and ProxyPassword. (Inherited from FTPBase.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |
|  | UploadFile | Overloaded. Uploads a file to the FTP server. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | BufferLength | Gets or sets the size of the buffer, in bytes, to use for streaming data. (Inherited from FTPBase.) |
|  | Description | Gets or sets the description of the node that appears in the Property Browser when you select the node in the Stimulus Profile Editor. (Inherited from BaseNode.) |
|  | Destination | Gets or sets the destination directory for downloaded files. |
|  | EnableProxy | Gets or sets a value indicating whether to transmit data through a proxy server. (Inherited from FTPBase.) |
|  | Filter | Gets or sets a regular expression to use to filter files by filename when ServerURL is a folder. (Overrides FTPBase.Filter.) |
|  | Id | Gets the unique identifier for a step, which is the full path to the step in the stimulus profile hierarchy. (Inherited from ActionStep.) |
|  | OverwriteExistingFileBehavior | Gets or sets the action to take if a file of the same name already exists in the destination directory. (Inherited from FTPBase.) |
|  | Password | Gets or sets the password for UserName to use to access the FTP server. (Inherited from FTPBase.) |
|  | ProxyPassword | Gets or sets the password for ProxyUserName to use to access the proxy server. (Inherited from FTPBase.) |
|  | ProxyPort | Gets or sets the port the FTP proxy uses. (Inherited from FTPBase.) |
|  | ProxyURL | Gets or sets the URL of the proxy server. (Inherited from FTPBase.) |
|  | ProxyUserName | Gets or sets the username for the proxy server. (Inherited from FTPBase.) |
|  | ResXKey | Gets or sets the ResX key for the node, which is a pointer to a .resx file that contains a context help description for the node. (Inherited from BaseNode.) |
|  | ServerURL | Gets or sets the address of a file or directory on the FTP server. (Inherited from FTPBase.) |
|  | ServerURLIsFolder | Gets or sets a value indicating whether the path to the source files is a file or a folder. |
|  | SSL | Gets or sets a value indicating whether data transmission is encrypted using an SSL protocol. (Inherited from FTPBase.) |
|  | State | Gets the execution state of a step (Idle, Initializing, Running, and so on.) (Inherited from ActionStep.) |
|  | StepName | Gets the name of a step. (Overrides ActionStep.StepName.) |
|  | Timeout | Gets or sets the time in seconds to wait for a response from the FTP server before returning a timeout error. (Inherited from FTPBase.) |
|  | UseBinary | Gets or sets a value indicating whether data is transmitted in binary form. (Inherited from FTPBase.) |
|  | UsePassive | Gets or sets a value indicating whether to use a passive or active connection on the FTP server. (Inherited from FTPBase.) |
|  | UserName | Gets or sets the username to use to access the FTP server. (Inherited from FTPBase.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

FTPDownload Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_ftpupload.htm language=enus -->
## TOPIC 00036: FTPUpload Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_ftpupload.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_ftpupload.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [FTPUpload](t_nationalinstruments_veristand_stimulusprofiledefinitionapi_ftpupload.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | FTPUpload | Overloaded. Initializes a new instance of the FTPUpload class. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | CheckForErrors | Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. (Overrides FTPBase.CheckForErrors().) |
|  | Clone | Creates a new object that is a copy of the current instance. (Inherited from BaseNode.) |
|  | CreateUniqueFileName | Creates a unique filename by appending a number to proposedFileName. (Inherited from FTPBase.) |
|  | DoesFileExistOnFTPServer | Checks if the specified file already exists on the FTP server. (Inherited from FTPBase.) |
|  | DownloadFile | Downloads the specified file from the FTP server and copies it to the Destination directory. This method uses a buffer of a size specified by BufferLength. (Inherited from FTPBase.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetFileListFromDirectory | Returns the name of all files from a directory on the FTP server. This method uses the proxy server settings, including ProxyUserName and ProxyPassword. (Inherited from FTPBase.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |
|  | UploadFile | Overloaded. Uploads a file to the FTP server. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | BufferLength | Gets or sets the size of the buffer, in bytes, to use for streaming data. (Inherited from FTPBase.) |
|  | Description | Gets or sets the description of the node that appears in the Property Browser when you select the node in the Stimulus Profile Editor. (Inherited from BaseNode.) |
|  | EnableProxy | Gets or sets a value indicating whether to transmit data through a proxy server. (Inherited from FTPBase.) |
|  | Filter | Gets or sets a regular expression to use to filter files by filename when ServerURL is a folder. (Overrides FTPBase.Filter.) |
|  | Id | Gets the unique identifier for a step, which is the full path to the step in the stimulus profile hierarchy. (Inherited from ActionStep.) |
|  | OverwriteExistingFileBehavior | Gets or sets the action to take if a file of the same name already exists in the destination directory. (Inherited from FTPBase.) |
|  | Password | Gets or sets the password for UserName to use to access the FTP server. (Inherited from FTPBase.) |
|  | ProxyPassword | Gets or sets the password for ProxyUserName to use to access the proxy server. (Inherited from FTPBase.) |
|  | ProxyPort | Gets or sets the port the FTP proxy uses. (Inherited from FTPBase.) |
|  | ProxyURL | Gets or sets the URL of the proxy server. (Inherited from FTPBase.) |
|  | ProxyUserName | Gets or sets the username for the proxy server. (Inherited from FTPBase.) |
|  | ResXKey | Gets or sets the ResX key for the node, which is a pointer to a .resx file that contains a context help description for the node. (Inherited from BaseNode.) |
|  | ServerURL | Gets or sets the address of a file or directory on the FTP server. (Inherited from FTPBase.) |
|  | Source | Gets or sets the path to the source file(s) to upload. |
|  | SourceIsFolder | Gets or sets a value indicating whether the Source is a folder. |
|  | SSL | Gets or sets a value indicating whether data transmission is encrypted using an SSL protocol. (Inherited from FTPBase.) |
|  | State | Gets the execution state of a step (Idle, Initializing, Running, and so on.) (Inherited from ActionStep.) |
|  | StepName | Gets the name of a step. (Overrides ActionStep.StepName.) |
|  | Timeout | Gets or sets the time in seconds to wait for a response from the FTP server before returning a timeout error. (Inherited from FTPBase.) |
|  | UseBinary | Gets or sets a value indicating whether data is transmitted in binary form. (Inherited from FTPBase.) |
|  | UsePassive | Gets or sets a value indicating whether to use a passive or active connection on the FTP server. (Inherited from FTPBase.) |
|  | UserName | Gets or sets the username to use to access the FTP server. (Inherited from FTPBase.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

FTPUpload Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_launchniveristand.htm language=enus -->
## TOPIC 00037: LaunchNIVeriStand Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_launchniveristand.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_launchniveristand.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [LaunchNIVeriStand](t_nationalinstruments_veristand_stimulusprofiledefinitionapi_launchniveristand.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | LaunchNIVeriStand | Overloaded. Initializes a new instance of the LaunchNIVeriStand class. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | CheckForErrors | Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. (Overrides ActionStep.CheckForErrors().) |
|  | Clone | Creates a new object that is a copy of the current instance. (Inherited from BaseNode.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Description | Gets or sets the description of the node that appears in the Property Browser when you select the node in the Stimulus Profile Editor. (Inherited from BaseNode.) |
|  | Id | Gets the unique identifier for a step, which is the full path to the step in the stimulus profile hierarchy. (Inherited from ActionStep.) |
|  | ResXKey | Gets or sets the ResX key for the node, which is a pointer to a .resx file that contains a context help description for the node. (Inherited from BaseNode.) |
|  | State | Gets the execution state of a step (Idle, Initializing, Running, and so on.) (Inherited from ActionStep.) |
|  | StepName | Gets the name of a step. (Overrides ActionStep.StepName.) |
|  | Timeout | Gets or sets the time in seconds to wait for NI VeriStand to launch before returning a timeout error. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

LaunchNIVeriStand Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_realtimesequencecallparameterassignment.htm language=enus -->
## TOPIC 00038: RealTimeSequenceCallParameterAssignment Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_realtimesequencecallparameterassignment.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_realtimesequencecallparameterassignment.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [RealTimeSequenceCallParameterAssignment](t_nationalinstruments_veristand_stimulusprofiledefinitionapi_realtimesequencecallparameterassignment.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | RealTimeSequenceCallParameterAssignment | Overloaded. Initializes a new instance of RealTimeSequenceCallParameterAssignment. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Clone | Creates a new object that is a copy of the current instance. (Inherited from BaseNode.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Description | Gets or sets the description of the node that appears in the Property Browser when you select the node in the Stimulus Profile Editor. (Inherited from BaseNode.) |
|  | ParameterName | Gets or sets the name of the sequence parameter. |
|  | ResXKey | Gets or sets the ResX key for the node, which is a pointer to a .resx file that contains a context help description for the node. (Inherited from BaseNode.) |
|  | Value | Gets or sets the value assigned to the real-time sequence parameter. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

RealTimeSequenceCallParameterAssignment Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_realtimesequencecallstep.htm language=enus -->
## TOPIC 00039: RealTimeSequenceCallStep Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_realtimesequencecallstep.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_realtimesequencecallstep.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [RealTimeSequenceCallStep](t_nationalinstruments_veristand_stimulusprofiledefinitionapi_realtimesequencecallstep.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | RealTimeSequenceCallStep | Overloaded. Initializes a new instance of RealTimeSequenceCallStep. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | AddReplaceParameterAssignment | Adds or changes a parameter assignment for the real-time sequence. A parameter assignment can be a channel in the system definition or a constant value. |
|  | CheckForErrors | Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. (Overrides ActionStep.CheckForErrors().) |
|  | Clone | Creates a new object that is a copy of the current instance. (Inherited from BaseNode.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | RefreshSequenceCall | Overloaded. Refreshes the ParameterAssignments and OutputEvaluation for the sequence call based on the current contents of the sequence. This ensures that parameter assignments exist for all parameters, and that the data types of all parameter assignments match the data type of the corresponding sequence. This method also deletes any parameter assignments that have no corresponding entry in the sequence. |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Description | Gets or sets the description of the node that appears in the Property Browser when you select the node in the Stimulus Profile Editor. (Inherited from BaseNode.) |
|  | Id | Gets the unique identifier for a step, which is the full path to the step in the stimulus profile hierarchy. (Inherited from ActionStep.) |
|  | OutputEvaluation | Gets or sets a reference to the pass/fail evaluation performed on the real-time sequence. |
|  | OutputEvaluationType | Gets or sets the type of pass/fail evaluation performed on the real-time sequence. |
|  | ParameterAssignments | Gets or sets the parameter assignments for the real-time sequence, which can be constant values or channels in the system definition file that the parameters map to. |
|  | ResXKey | Gets or sets the ResX key for the node, which is a pointer to a .resx file that contains a context help description for the node. (Inherited from BaseNode.) |
|  | SequencePath | Gets or sets the path to the real-time sequence (.nivsseq) file on disk. A properly formatted CSV (.csv) file also can function as a real-time sequence. |
|  | State | Gets the execution state of a step (Idle, Initializing, Running, and so on.) (Inherited from ActionStep.) |
|  | StepName | Gets the name of the step. (Overrides ActionStep.StepName.) |
|  | Target | The name of the target on which the sequence will execute. |
|  | Timeout | Gets or sets he timeout in milliseconds within which the real-time sequence must complete each time step. If the sequence exceeds this timeout, the VeriStand Engine aborts the sequence execution and returns an error. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

RealTimeSequenceCallStep Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_sendprojectcommandstep.htm language=enus -->
## TOPIC 00040: SendProjectCommandStep Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_sendprojectcommandstep.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_sendprojectcommandstep.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SendProjectCommandStep](t_nationalinstruments_veristand_stimulusprofiledefinitionapi_sendprojectcommandstep.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | SendProjectCommandStep | Overloaded. Initializes a new instance of SendProjectCommandStep. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | CheckForErrors | Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. (Inherited from ActionStep.) |
|  | Clone | Creates a new object that is a copy of the current instance. (Inherited from BaseNode.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Command | Gets or sets the command sent to the VeriStand project (Connect, Run, Deploy, and so on). |
|  | Description | Gets or sets the description of the node that appears in the Property Browser when you select the node in the Stimulus Profile Editor. (Inherited from BaseNode.) |
|  | Id | Gets the unique identifier for a step, which is the full path to the step in the stimulus profile hierarchy. (Inherited from ActionStep.) |
|  | ResXKey | Gets or sets the ResX key for the node, which is a pointer to a .resx file that contains a context help description for the node. (Inherited from BaseNode.) |
|  | State | Gets the execution state of a step (Idle, Initializing, Running, and so on.) (Inherited from ActionStep.) |
|  | StepName | Gets the name of the step. (Overrides ActionStep.StepName.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SendProjectCommandStep Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_sendworkspacetoolmessagestep.htm language=enus -->
## TOPIC 00041: SendWorkspaceToolMessageStep Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_sendworkspacetoolmessagestep.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_sendworkspacetoolmessagestep.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SendWorkspaceToolMessageStep](t_nationalinstruments_veristand_stimulusprofiledefinitionapi_sendworkspacetoolmessagestep.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | SendWorkspaceToolMessageStep | Overloaded. Initializes a new instance of SendWorkspaceToolMessageStep. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | CheckForErrors | Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. (Inherited from ActionStep.) |
|  | Clone | Creates a new object that is a copy of the current instance. (Inherited from BaseNode.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Command | Gets or sets the message or command sent to the tool. |
|  | Data | Gets or sets any data required by the case of the Workspace tool that handles the Command. |
|  | Description | Gets or sets the description of the node that appears in the Property Browser when you select the node in the Stimulus Profile Editor. (Inherited from BaseNode.) |
|  | Id | Gets the unique identifier for a step, which is the full path to the step in the stimulus profile hierarchy. (Inherited from ActionStep.) |
|  | ResXKey | Gets or sets the ResX key for the node, which is a pointer to a .resx file that contains a context help description for the node. (Inherited from BaseNode.) |
|  | State | Gets the execution state of a step (Idle, Initializing, Running, and so on.) (Inherited from ActionStep.) |
|  | StepName | Gets the name of the step. (Overrides ActionStep.StepName.) |
|  | Timeout | Gets or sets the amount of time in milliseconds to wait for a response from the Workspace tool before timing out. |
|  | WorkspaceToolPath | Gets or sets the path to the Workspace tool VI. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SendWorkspaceToolMessageStep Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_setupstepgroup.htm language=enus -->
## TOPIC 00042: SetupStepGroup Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_setupstepgroup.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_setupstepgroup.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SetupStepGroup](t_nationalinstruments_veristand_stimulusprofiledefinitionapi_setupstepgroup.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | SetupStepGroup | Overloaded. Initializes a new instance of SetupStepGroup. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | CheckForErrors | Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. (Inherited from StepGroup.) |
|  | Clone | Creates a new object that is a copy of the current instance. (Inherited from BaseNode.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Description | Gets or sets the description of the node that appears in the Property Browser when you select the node in the Stimulus Profile Editor. (Inherited from BaseNode.) |
|  | GroupName | Gets or sets the name of the step group. (Inherited from StepGroup.) |
|  | Id | Gets the unique identifier for a step, which is the full path to the step in the stimulus profile hierarchy. (Inherited from ActionStep.) |
|  | ResXKey | Gets or sets the ResX key for the node, which is a pointer to a .resx file that contains a context help description for the node. (Inherited from BaseNode.) |
|  | State | Gets the execution state of a step (Idle, Initializing, Running, and so on.) (Inherited from ActionStep.) |
|  | StepName | Gets the name of the step, which for step groups is also the GroupName. (Inherited from StepGroup.) |
|  | Steps | Gets or sets the steps that belong to the current step group. (Inherited from StepGroup.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SetupStepGroup Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_systemdefinitionapi_customdevice.htm language=enus -->
## TOPIC 00043: CustomDevice Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_systemdefinitionapi_customdevice.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_systemdefinitionapi_customdevice.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [CustomDevice](t_nationalinstruments_veristand_systemdefinitionapi_customdevice.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | CustomDevice | Initializes a new instance of the CustomDevice class. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | AddCustomDeviceChannelIfNotFound | Adds a custom device channel with the name and guid you specify to the current section, if the channel does not already exist under the section. If the channel you specify already exists, this method takes no action and returns a reference to the existing channel. (Inherited from CustomDeviceSection.) |
|  | AddCustomDeviceSectionIfNotFound | Adds a custom device subsection with the name and guid you specify to the current section, if the subsection does not already exist under the section. If the subsection does exist, this method does nothing. (Inherited from CustomDeviceSection.) |
|  | AddCustomDeviceWaveformIfNotFound | Adds a CustomDeviceWaveform with the name, dataType and guid you specify to the current section, if the CustomDeviceWaveform does not already exist under the section. If the CustomDeviceWaveform you specify already exists, this method takes no action and returns a reference to the existing CustomDeviceWaveform. (Inherited from CustomDeviceSection.) |
|  | AddDependencies | Adds dependencies to a custom device. Dependencies are any files, such as DLLs or VIs, that the custom device requires and that you want to deploy to the target along with the custom device. |
|  | AddErrorChannel | Adds an error channel to the custom device. An asynchronous custom device can send a fatal error status to the Primary Control Loop of the VeriStand Engine by writing a non-zero error code value to this channel. (Inherited from CustomDeviceSection.) |
|  | AddInputOverflowCountChannel | Adds an input overflow count channel to a section in an asynchronous custom device. Input overflow count channels track the number of times the system fails to write data to an asynchronous custom device because the FIFO is full. A custom device can have only one input overflow count channel. (Inherited from CustomDeviceSection.) |
|  | AddOutputUnderflowCountChannel | Adds an output underflow count channel to a section in an asynchronous custom device. Output underflow count channels track the number of times the system fails to read data from an asynchronous custom device because there is no data to read. A custom device can have only one output underflow count channel. (Inherited from CustomDeviceSection.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Class Destructor (Overrides CustomDeviceSection.Finalize().) |
|  | FindChildrenByGUID | Gets an array that contains the child BaseNode elements of the current node that match the specified TypeGUID. (Inherited from BaseNode.) |
|  | FindFirstChildWithName | Gets the first child node with the specified name. (Inherited from BaseNode.) |
|  | FindNodeByPath | Gets a node using the specified path. (Inherited from BaseNode.) |
|  | GetBinaryStringProperty | Gets the binary string value of the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | GetBooleanProperty | Gets the Boolean value of the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | GetChildren | Gets an array that contains the child BaseNode elements of the current node. (Inherited from BaseNode.) |
|  | GetCustomDeviceChannelList | Gets an array that contains the CustomDeviceChannel elements from the current CustomDevice. |
|  | GetCustomDeviceSectionList | Gets an array that contains the CustomDeviceSection elements from the current CustomDevice. Sections are not required in custom devices, but provide a way to organize custom device channels into a logical hierarchy. |
|  | GetCustomDeviceWaveformList | Gets an array that contains the CustomDeviceWaveform elements from the current CustomDevice. |
|  | GetDependencies | Gets an array that contains the DependentFile elements from the current CustomDevice. Dependent files are any files that the device requires and that deploy to the target along with the custom device. |
|  | GetDependentFileProperty | Gets the reference to the dependent file that is the value of the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | GetDependentNodeProperty | Overloaded. Gets the reference to the dependent node that is the value of the custom device item property specified by name. |
|  | GetDictionaryArrayProperty | Gets the reference to the Dictionary array that is the value of the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | GetDictionaryProperty | Gets the reference to the Dictionary that is the value of the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | GetDocumentPath | Gets the path to the system definition file that owns this node. (Inherited from BaseNode.) |
|  | GetDocumentRoot | Gets the Root node of the system definition file. (Inherited from BaseNode.) |
|  | GetDoubleArrayProperty | Gets the array of double-precision floating point numbers that is the value of the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | GetDoubleProperty | Gets the double-precision floating point value of the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | GetDriverVIForOwnerTargetType | Gets the RT Driver VI for the target indicated by the custom device. A single custom device can have multiple RT Driver VIs if the device supports multiple real-time operating systems or multiple execution modes. |
|  | GetDriverVIs | Gets all the RT Driver VIs associated with the custom device. A single custom device can have multiple RT Driver VIs if the device supports multiple real-time operating systems or multiple execution modes. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetI32ArrayProperty | Gets the array of 32-bit signed integers that is the value of the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | GetI32Property | Gets the 32-bit signed integer that is the value of the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | GetParent | Gets the parent node of this node. (Inherited from BaseNode.) |
|  | GetPropertyNames | Gets the names of all the properties associated with a custom device item. Custom device item properties store and communicate state information. (Inherited from CustomDeviceBase.) |
|  | GetPropertyType | Gets the data type of the custom device item property specified by propertyName. (Inherited from CustomDeviceBase.) |
|  | GetStringArrayProperty | Gets the array of strings that is the value of the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | GetStringProperty | Gets the string value of the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | GetTimingSourceInitVIs | Gets the Timing Source Initialization VIs associated with the custom device. If you configure the custom device as the master timing source for the target, these VIs create a timing source for the Primary Control Loop. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | GetU16Property | Gets the unsigned 16-bit integer value of the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | GetU32ArrayProperty | Gets the array of unsigned 32-bit integers that is the value of the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | GetU32Property | Gets the unsigned 32-bit integer value of the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | GetU64Property | Gets the unsigned 64-bit integer value of the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | GetVariantProperty | Gets the LabVIEW variant value of the custom device item property specified by name. The variant data type is a generic container for all other LabVIEW data types. (Inherited from CustomDeviceBase.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MoveNodeTo | Moves a custom device item to a new location within the custom device hierarchy. (Inherited from CustomDeviceBase.) |
|  | RemoveError | Removes an error that matches the specified ErrorID. (Inherited from CustomDeviceBase.) |
|  | RemoveNode | Removes this node from the hierarchy, if the node can be removed. (Inherited from BaseNode.) |
|  | RemoveProperty | Removes the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | RenameNode | Overloaded. Renames this node to the name you specify, if the node can be renamed and if the name you specify is not already in use by a sibling of this node. |
|  | ReportError | Configures whether to report an error that occurs during custom device execution. (Inherited from CustomDeviceBase.) |
|  | ResetDependencies | Removes all the dependencies from the custom device. Dependencies are any files, such as DLLs or VIs, that the custom device requires and that you want to deploy to the target along with the custom device. |
|  | SetBinaryStringProperty | Sets a binary string value for the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | SetBooleanProperty | Sets a Boolean value for the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | SetDependentFileProperty | Sets a reference to a dependent file as the value for the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | SetDependentNodeProperty | Overloaded. Sets a reference to a dependent node as the value of the custom device item property specified by name. |
|  | SetDictionaryArrayProperty | Sets a reference to a Dictionary as the value of the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | SetDictionaryProperty | Sets a reference to a Dictionary element as the value of the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | SetDoubleArrayProperty | Sets an array of double-precision floating point numbers as the value of the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | SetDoubleProperty | Sets a double-precision floating point value for the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | SetDriverVIs | Sets the RT Driver VIs to associate with the custom device. A custom device requires at least one RT Driver VI. A single custom device can have multiple RT Driver VIs if the device supports multiple real-time operating systems or multiple execution modes. |
|  | SetI32ArrayProperty | Sets an array of 32-bit signed integers as the value of the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | SetI32Property | Sets a 32-bit signed integer value for the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | SetStringArrayProperty | Sets an array of strings as the value of the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | SetStringProperty | Sets a string value for the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | SetTimingSourceInitVIs | Sets the Timing Source Initialization VIs to associate with the custom device. Timing Source Initialization VIs are required if you want to use a custom device that is not a timing and sync device as the master timing source for the Primary Control Loop. |
|  | SetU16Property | Sets an unsigned 16-bit integer value for the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | SetU32ArrayProperty | Sets an array of unsigned 32-bit integers as the value of the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | SetU32Property | Sets an unsigned 32-bit integer value for the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | SetU64Property | Sets an unsigned 64-bit integer value for the custom device item property specified by name. (Inherited from CustomDeviceBase.) |
|  | SetVariantProperty | Sets a LabVIEW variant value for the custom device item property specified by name. The variant data type is a generic container for all other LabVIEW data types. (Inherited from CustomDeviceBase.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | BaseNodeType | Gets a reference to the internal representation of this node. (Inherited from BaseNode.) |
|  | Decimation | Gets or sets the decimation factor for the custom device, which determines how many iterations of the Primary Control Loop (PCL) occur between calls to the custom device. |
|  | Description | Gets or sets the description of this node. (Inherited from BaseNode.) |
|  | DeviceEnabledState | Gets or sets the state (enabled or disabled) of the custom device. |
|  | DriverVIExecutionMode | Gets or sets the execution mode of the custom device, such as if it runs inline with the Primary Control Loop or asynchronously. |
|  | FIFOSinkDepth | Gets or sets the depth of the FIFO at the sink. This property defines the size of the buffer for outgoing data. This property only applies to asynchronous custom devices. |
|  | FIFOSourceDepth | Gets or sets the depth of the FIFO at the source. This property defines the size of the buffer for incoming data. This property only applies to asynchronous custom devices. |
|  | LoopType | Gets or sets the type of loop (TimedLoop or WhileLoop) in which the custom device runs. This property only applies to asynchronous custom devices. |
|  | Name | Gets the name of this node. To rename a node, use the RenameNode method. (Inherited from BaseNode.) |
|  | NodeID | Gets the ID of this node. (Inherited from BaseNode.) |
|  | NodePath | Gets the path to the node within the system definition file. (Inherited from BaseNode.) |
|  | TimedLoopPriority | Gets or sets the priority (High, Low, or Medium) of the Timed Loop in which an asynchronous custom device runs. This property only applies to asynchronous custom devices that run in Timed Loops. |
|  | TypeGUID | Gets or sets the GUID associated with an item in a custom device. You can use this property to get or set the GUID for any component of a custom device that lists a GUID in the Custom Device XML file, such as the configuration page for the item, menu items that appear at run-time, Action VIs associated with the item, and so on. (Inherited from CustomDeviceBase.) |
|  | UseDeviceClock | Gets or sets whether the Timed Loop in which an asynchronous custom device runs is synchronized with the Primary Control Loop (PCL) timing source. This property only applies to asynchronous custom devices that run in Timed Loops. |
|  | Version | Gets or sets information stored with a custom device, such as version information. You can read this string to determine whether to update device dependencies or, if you are migrating a custom device to a new version of NI VeriStand, to determine whether to run mutation code. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CustomDevice Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_systemdefinitionapi_daqanalogoutputs.htm language=enus -->
## TOPIC 00044: DAQAnalogOutputs Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_systemdefinitionapi_daqanalogoutputs.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_systemdefinitionapi_daqanalogoutputs.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [DAQAnalogOutputs](t_nationalinstruments_veristand_systemdefinitionapi_daqanalogoutputs.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | AddAnalogOutput | Adds the specified DAQAnalogOutput channel. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Class Destructor (Overrides Section.Finalize().) |
|  | FindChildrenByGUID | Gets an array that contains the child BaseNode elements of the current node that match the specified TypeGUID. (Inherited from BaseNode.) |
|  | FindFirstChildWithName | Gets the first child node with the specified name. (Inherited from BaseNode.) |
|  | FindNodeByPath | Gets a node using the specified path. (Inherited from BaseNode.) |
|  | GetAnalogOutputList | Gets an array that contains the DAQAnalogOutput elements from the current DAQAnalogOutputs section. |
|  | GetChildren | Gets an array that contains the child BaseNode elements of the current node. (Inherited from BaseNode.) |
|  | GetDocumentPath | Gets the path to the system definition file that owns this node. (Inherited from BaseNode.) |
|  | GetDocumentRoot | Gets the Root node of the system definition file. (Inherited from BaseNode.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetParent | Gets the parent node of this node. (Inherited from BaseNode.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | RemoveNode | Removes this node from the hierarchy, if the node can be removed. (Inherited from BaseNode.) |
|  | RenameNode | Renames this node to the name you specify, if the node can be renamed and if the name you specify is not already in use by a sibling of this node. (Inherited from BaseNode.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | BaseNodeType | Gets a reference to the internal representation of this node. (Inherited from BaseNode.) |
|  | Description | Gets or sets the description of this node. (Inherited from BaseNode.) |
|  | Name | Gets the name of this node. To rename a node, use the RenameNode method. (Inherited from BaseNode.) |
|  | NodeID | Gets the ID of this node. (Inherited from BaseNode.) |
|  | NodePath | Gets the path to the node within the system definition file. (Inherited from BaseNode.) |
|  | TypeGUID | Gets the GUID associated with the node. Attempts to set the GUID of a BaseNode will generate an exception. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQAnalogOutputs Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_systemdefinitionapi_maximum.htm language=enus -->
## TOPIC 00045: Maximum Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_systemdefinitionapi_maximum.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_systemdefinitionapi_maximum.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [Maximum](t_nationalinstruments_veristand_systemdefinitionapi_maximum.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | Maximum | Overloaded. Initializes a new instance of Maximum where the values of x and y are both channels. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Downcast | Casts CalculatedChannel to a more specific type. (Inherited from CalculatedChannel.) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Class Destructor (Overrides CalculatedChannel.Finalize().) |
|  | FindChildrenByGUID | Gets an array that contains the child BaseNode elements of the current node that match the specified TypeGUID. (Inherited from BaseNode.) |
|  | FindFirstChildWithName | Gets the first child node with the specified name. (Inherited from BaseNode.) |
|  | FindNodeByPath | Gets a node using the specified path. (Inherited from BaseNode.) |
|  | GetChildren | Gets an array that contains the child BaseNode elements of the current node. (Inherited from BaseNode.) |
|  | GetDocumentPath | Gets the path to the system definition file that owns this node. (Inherited from BaseNode.) |
|  | GetDocumentRoot | Gets the Root node of the system definition file. (Inherited from BaseNode.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetParent | Gets the parent node of this node. (Inherited from BaseNode.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | RemoveNode | Removes this node from the hierarchy, if the node can be removed. (Inherited from BaseNode.) |
|  | RenameNode | Renames this node to the name you specify, if the node can be renamed and if the name you specify is not already in use by a sibling of this node. (Inherited from BaseNode.) |
|  | SetXValue | Overloaded. Sets the value of x in the comparison of x and y to the value of the specified channel. |
|  | SetYValue | Overloaded. Sets the value of y in the comparison of x and y to the value of the specified channel. |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | BaseNodeType | Gets a reference to the internal representation of this node. (Inherited from BaseNode.) |
|  | BitFields | Gets a bitfield mask that is set on the channel. (Inherited from Channel.) |
|  | CalculatedChannelType | Gets the type of the calculated channel. (Inherited from CalculatedChannel.) |
|  | ColumnDimensions | Gets the number of columns in the channel value. (Inherited from Channel.) |
|  | DataSource | Gets or sets the source channel that maps to the current channel and provides it data. (Inherited from Channel.) |
|  | DefaultValue | Gets the default value of the channel. (Inherited from Channel.) |
|  | Description | Gets or sets the description of this node. (Inherited from BaseNode.) |
|  | Name | Gets the name of this node. To rename a node, use the RenameNode method. (Inherited from BaseNode.) |
|  | NodeID | Gets the ID of this node. (Inherited from BaseNode.) |
|  | NodePath | Gets the path to the node within the system definition file. (Inherited from BaseNode.) |
|  | RowDimensions | Gets the number of rows in the channel value. (Inherited from Channel.) |
|  | Scale | Gets or sets the value of the scale property on the channel. (Inherited from Channel.) |
|  | ScaleUnits | Gets the units of the scale associated with the channel. (Inherited from Channel.) |
|  | TypeGUID | Gets the GUID associated with the node. Attempts to set the GUID of a BaseNode will generate an exception. (Inherited from BaseNode.) |
|  | Units | Gets or sets the units associated with the channel. This can be any arbitrary string. (Inherited from Channel.) |
|  | XChannelValue | Gets the channel that specifies the value of x in the comparison of x and y. |
|  | XConstantValue | Gets the constant value of x in the comparison of x and y, regardless of whether x is a constant or a channel. |
|  | XIsConstant | Gets whether the value of x in the comparison of x and y is specified by a constant or a channel. |
|  | YChannelValue | Gets the channel that specifies the value of y in the comparison of x and y. |
|  | YConstantValue | Gets the constant value of y in the comparison of x and y. regardless of whether x is a constant or a channel. |
|  | YIsConstant | Gets whether the value of y in the comparison of x and y is specified by a constant or a channel. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Maximum Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_systemdefinitionapi_model.htm language=enus -->
## TOPIC 00046: Model Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_systemdefinitionapi_model.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_systemdefinitionapi_model.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [Model](t_nationalinstruments_veristand_systemdefinitionapi_model.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | Model | Overloaded. Initializes a new instance of Model and sets the network port that an .mdl file uses for communication via TCP. DLLs and .lvmodel files do not require a network port. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Class Destructor (Overrides Section.Finalize().) |
|  | FindChildrenByGUID | Gets an array that contains the child BaseNode elements of the current node that match the specified TypeGUID. (Inherited from BaseNode.) |
|  | FindFirstChildWithName | Gets the first child node with the specified name. (Inherited from BaseNode.) |
|  | FindNodeByPath | Gets a node using the specified path. (Inherited from BaseNode.) |
|  | GetChildren | Gets an array that contains the child BaseNode elements of the current node. (Inherited from BaseNode.) |
|  | GetDocumentPath | Gets the path to the system definition file that owns this node. (Inherited from BaseNode.) |
|  | GetDocumentRoot | Gets the Root node of the system definition file. (Inherited from BaseNode.) |
|  | GetExecutionSection | Gets the Execution section, which contains channels that track execution details of the model, such as its current status and the amount of time that has elapsed since it began executing. . |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetInportsSection | Gets the Inports section, which contains all the Inport and InportGroup objects under the model. |
|  | GetOutportsSection | Gets the Outports section, which contains all the Outport and OutportGroup objects under the model. |
|  | GetParametersSection | Gets the ModelParameters section, which contains all the ModelParameter and ModelParameterGroup objects under the model. |
|  | GetParent | Gets the parent node of this node. (Inherited from BaseNode.) |
|  | GetSignalsSection | Gets the ModelSignals section, which contains all the ModelSignal and ModelSignalGroup objects under the model. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | RefreshModelInformation | Overloaded. Reloads a previously imported model. |
|  | RemoveNode | Removes this node from the hierarchy, if the node can be removed. (Inherited from BaseNode.) |
|  | RenameNode | Renames this node to the name you specify, if the node can be renamed and if the name you specify is not already in use by a sibling of this node. (Overrides BaseNode.RenameNode(String).) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | BaseNodeType | Gets a reference to the internal representation of this node. (Inherited from BaseNode.) |
|  | BaseRate | Gets the base rate of the model in microseconds. |
|  | Decimation | Gets or sets the decimation applied to the Primary Control Loop rate to determine the BaseRate of the model. |
|  | Description | Gets or sets the description of this node. (Inherited from BaseNode.) |
|  | DLLPath | Gets a reference to the compiled version of the model (.dll file). |
|  | DLLSize | Gets the size, in bytes, of the compiled version of the model (.dll file). |
|  | DLLTimestamp | Gets the time at which the model DLL was compiled. |
|  | GlobalParameterScope | Gets or sets whether global parameters in the current model share their values with other models on the same target. |
|  | LoadSuccess | Gets whether NI VeriStand loaded the model successfully. |
|  | MD5 | Gets the MD5 message-digest for the model. |
|  | ModelPath | Gets a reference to the uncompiled model file. |
|  | ModelTimestamp | Gets the time at which the model was last saved. |
|  | Name | Gets the name of this node. To rename a node, use the RenameNode method. (Inherited from BaseNode.) |
|  | NIVeriStandServerPort | Gets or sets the network port that the model uses for communication via TCP. This property only applies to uncompiled models from The MathWorks, Inc. SimulinkÂ® software. DLLs and .lvmodel files do not require a network port. |
|  | NodeID | Gets the ID of this node. (Inherited from BaseNode.) |
|  | NodePath | Gets the path to the node within the system definition file. (Inherited from BaseNode.) |
|  | Processor | Gets or sets the processor on which the Model Execution Loop executes. -2 automatically assigns the processor to "any available". |
|  | SegmentVectors | Gets information about whether or not vector inputs, outputs, parameters, and signals were split up into scalar channels when the model was loaded. |
|  | ShowUnnamedSignals | Gets whether signals without names are visible. |
|  | TypeGUID | Gets the GUID associated with the node. Attempts to set the GUID of a BaseNode will generate an exception. (Inherited from BaseNode.) |
|  | UserRate | Obsolete. THIS PROPERTY IS OBSOLETE in NI VeriStand 2011 SP1 and later. Use BaseRate instead. Gets the user rate of the model. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Model Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_systemdefinitionapi_modelsignal.htm language=enus -->
## TOPIC 00047: ModelSignal Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_systemdefinitionapi_modelsignal.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_systemdefinitionapi_modelsignal.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [ModelSignal](t_nationalinstruments_veristand_systemdefinitionapi_modelsignal.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | ModelSignal | Initializes a new instance of ModelSignal with the specified signal. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Class Destructor (Overrides Channel.Finalize().) |
|  | FindChildrenByGUID | Gets an array that contains the child BaseNode elements of the current node that match the specified TypeGUID. (Inherited from BaseNode.) |
|  | FindFirstChildWithName | Gets the first child node with the specified name. (Inherited from BaseNode.) |
|  | FindNodeByPath | Gets a node using the specified path. (Inherited from BaseNode.) |
|  | GetChildren | Gets an array that contains the child BaseNode elements of the current node. (Inherited from BaseNode.) |
|  | GetDocumentPath | Gets the path to the system definition file that owns this node. (Inherited from BaseNode.) |
|  | GetDocumentRoot | Gets the Root node of the system definition file. (Inherited from BaseNode.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetParent | Gets the parent node of this node. (Inherited from BaseNode.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | RemoveNode | Removes this node from the hierarchy, if the node can be removed. (Inherited from BaseNode.) |
|  | RenameNode | Renames this node to the name you specify, if the node can be renamed and if the name you specify is not already in use by a sibling of this node. (Inherited from BaseNode.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | BaseNodeType | Gets a reference to the internal representation of this node. (Inherited from BaseNode.) |
|  | BitFields | Gets a bitfield mask that is set on the channel. (Inherited from Channel.) |
|  | ColumnDimensions | Gets the number of columns in the channel value. (Inherited from Channel.) |
|  | DataSource | Gets or sets the source channel that maps to the current channel and provides it data. (Inherited from Channel.) |
|  | DefaultValue | Gets the default value of the channel. (Inherited from Channel.) |
|  | Description | Gets or sets the description of this node. (Inherited from BaseNode.) |
|  | Index | Gets the index of the model signal. |
|  | ModelPath | Gets the symbolic path to the parameter within the model. |
|  | Name | Gets the name of this node. To rename a node, use the RenameNode method. (Inherited from BaseNode.) |
|  | NodeID | Gets the ID of this node. (Inherited from BaseNode.) |
|  | NodePath | Gets the path to the node within the system definition file. (Inherited from BaseNode.) |
|  | Path | Gets the path to the model that contains the signal. |
|  | RowDimensions | Gets the number of rows in the channel value. (Inherited from Channel.) |
|  | Scale | Gets or sets the value of the scale property on the channel. (Inherited from Channel.) |
|  | ScaleUnits | Gets the units of the scale associated with the channel. (Inherited from Channel.) |
|  | TypeGUID | Gets the GUID associated with the node. Attempts to set the GUID of a BaseNode will generate an exception. (Inherited from BaseNode.) |
|  | Units | Gets or sets the units associated with the channel. This can be any arbitrary string. (Inherited from Channel.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ModelSignal Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_systemdefinitionapi_modelsupport_modelloader.htm language=enus -->
## TOPIC 00048: ModelLoader Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_systemdefinitionapi_modelsupport_modelloader.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_systemdefinitionapi_modelsupport_modelloader.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [ModelLoader](t_nationalinstruments_veristand_systemdefinitionapi_modelsupport_modelloader.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | ModelLoader | Initializes a new instance of ModelLoader for the model at the specified filePath. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | FinalizeLibrary | Finalizes the model library (DLL). You must call this property after FinalizeModel. |
|  | FinalizeModel | Finalizes the model. You must call this property before FinalizeLibrary. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetInputOutputPorts | Gets the inports and outports of a model. |
|  | GetParameters | Overloaded. Gets the parameters of a model. |
|  | GetSignals | Overloaded. Gets the signals of a model. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeModel | Initializes a model. |
|  | InitializeModelDLL | Initializes a model DLL. |
|  | InitializeModelMDL | Initialize mdl client so we can get information |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Fields

|  | Name | Description |
| --- | --- | --- |
|  | ModelPath | The model path. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ModelLoader Class

NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_systemdefinitionapi_modelsupport_modelsignaltype.htm language=enus -->
## TOPIC 00049: ModelSignalType Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_systemdefinitionapi_modelsupport_modelsignaltype.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_systemdefinitionapi_modelsupport_modelsignaltype.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [ModelSignalType](t_nationalinstruments_veristand_systemdefinitionapi_modelsupport_modelsignaltype.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Constructors

|  | Name | Description |
| --- | --- | --- |
|  | ModelSignalType | RESERVED FOR INTERNAL USE. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an Object to attempt to free resources and perform other cleanup operations before the Object is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Fields

|  | Name | Description |
| --- | --- | --- |
|  | BlockName | RESERVED FOR INTERNAL USE. |
|  | DataType | RESERVED FOR INTERNAL USE. |
|  | ID | RESERVED FOR INTERNAL USE. |
|  | Idx | RESERVED FOR INTERNAL USE. |
|  | Name | RESERVED FOR INTERNAL USE. |
|  | PortNumber | RESERVED FOR INTERNAL USE. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Dims | RESERVED FOR INTERNAL USE. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ModelSignalType Class

NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_systemdefinitionapi_outports.htm language=enus -->
## TOPIC 00050: Outports Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_systemdefinitionapi_outports.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_systemdefinitionapi_outports.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [Outports](t_nationalinstruments_veristand_systemdefinitionapi_outports.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Class Destructor (Overrides Section.Finalize().) |
|  | FindChildrenByGUID | Gets an array that contains the child BaseNode elements of the current node that match the specified TypeGUID. (Inherited from BaseNode.) |
|  | FindFirstChildWithName | Gets the first child node with the specified name. (Inherited from BaseNode.) |
|  | FindNodeByPath | Gets a node using the specified path. (Inherited from BaseNode.) |
|  | GetChildren | Gets an array that contains the child BaseNode elements of the current node. (Inherited from BaseNode.) |
|  | GetDocumentPath | Gets the path to the system definition file that owns this node. (Inherited from BaseNode.) |
|  | GetDocumentRoot | Gets the Root node of the system definition file. (Inherited from BaseNode.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetOutportGroups | Gets an array that contains the of OutportGroup elements from the current Outports section. This method gets the defined organizational groups for model outports. |
|  | GetOutports | Gets an array that contains the Outport elements from the current Outports section. This method gets the individual outports or the model. |
|  | GetParent | Gets the parent node of this node. (Inherited from BaseNode.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | RemoveNode | Removes this node from the hierarchy, if the node can be removed. (Inherited from BaseNode.) |
|  | RenameNode | Renames this node to the name you specify, if the node can be renamed and if the name you specify is not already in use by a sibling of this node. (Inherited from BaseNode.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | BaseNodeType | Gets a reference to the internal representation of this node. (Inherited from BaseNode.) |
|  | Description | Gets or sets the description of this node. (Inherited from BaseNode.) |
|  | Name | Gets the name of this node. To rename a node, use the RenameNode method. (Inherited from BaseNode.) |
|  | NodeID | Gets the ID of this node. (Inherited from BaseNode.) |
|  | NodePath | Gets the path to the node within the system definition file. (Inherited from BaseNode.) |
|  | TypeGUID | Gets the GUID associated with the node. Attempts to set the GUID of a BaseNode will generate an exception. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Outports Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/allmembers_t_nationalinstruments_veristand_systemdefinitionapi_rawframedatalogging.htm language=enus -->
## TOPIC 00051: RawFrameDataLogging Members

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/allmembers_t_nationalinstruments_veristand_systemdefinitionapi_rawframedatalogging.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/allmembers_t_nationalinstruments_veristand_systemdefinitionapi_rawframedatalogging.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [RawFrameDataLogging](t_nationalinstruments_veristand_systemdefinitionapi_rawframedatalogging.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | AddDataLoggingFile | Adds the specified raw frame data logging file under the current NI-XNET port. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Class Destructor (Overrides Section.Finalize().) |
|  | FindChildrenByGUID | Gets an array that contains the child BaseNode elements of the current node that match the specified TypeGUID. (Inherited from BaseNode.) |
|  | FindFirstChildWithName | Gets the first child node with the specified name. (Inherited from BaseNode.) |
|  | FindNodeByPath | Gets a node using the specified path. (Inherited from BaseNode.) |
|  | GetChildren | Gets an array that contains the child BaseNode elements of the current node. (Inherited from BaseNode.) |
|  | GetDataLoggingFileList | Gets an array that contains the DataLoggingFile elements from the current RawFrameDataLogging section. This method gets the defined frame data logging files for the current NI-XNET port. |
|  | GetDocumentPath | Gets the path to the system definition file that owns this node. (Inherited from BaseNode.) |
|  | GetDocumentRoot | Gets the Root node of the system definition file. (Inherited from BaseNode.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetParent | Gets the parent node of this node. (Inherited from BaseNode.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | RemoveNode | Removes this node from the hierarchy, if the node can be removed. (Inherited from BaseNode.) |
|  | RenameNode | Renames this node to the name you specify, if the node can be renamed and if the name you specify is not already in use by a sibling of this node. (Inherited from BaseNode.) |
|  | ToString | Returns a String that represents the current Object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | BaseNodeType | Gets a reference to the internal representation of this node. (Inherited from BaseNode.) |
|  | Description | Gets or sets the description of this node. (Inherited from BaseNode.) |
|  | Name | Gets the name of this node. To rename a node, use the RenameNode method. (Inherited from BaseNode.) |
|  | NodeID | Gets the ID of this node. (Inherited from BaseNode.) |
|  | NodePath | Gets the path to the node within the system definition file. (Inherited from BaseNode.) |
|  | TypeGUID | Gets the GUID associated with the node. Attempts to set the GUID of a BaseNode will generate an exception. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

RawFrameDataLogging Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_defaultcase.htm language=enus -->
## TOPIC 00052: DefaultCase Events

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_defaultcase.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_defaultcase.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [DefaultCase](t_nationalinstruments_veristand_realtimesequencedefinitionapi_defaultcase.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DefaultCase Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_dowhileloop.htm language=enus -->
## TOPIC 00053: DoWhileLoop Events

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_dowhileloop.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_dowhileloop.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [DoWhileLoop](t_nationalinstruments_veristand_realtimesequencedefinitionapi_dowhileloop.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DoWhileLoop Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_expression.htm language=enus -->
## TOPIC 00054: Expression Events

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_expression.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_expression.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [Expression](t_nationalinstruments_veristand_realtimesequencedefinitionapi_expression.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Expression Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_foreachloop.htm language=enus -->
## TOPIC 00055: ForEachLoop Events

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_foreachloop.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_foreachloop.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [ForEachLoop](t_nationalinstruments_veristand_realtimesequencedefinitionapi_foreachloop.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ForEachLoop Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_forloop.htm language=enus -->
## TOPIC 00056: ForLoop Events

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_forloop.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_forloop.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [ForLoop](t_nationalinstruments_veristand_realtimesequencedefinitionapi_forloop.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ForLoop Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_ifelse.htm language=enus -->
## TOPIC 00057: IfElse Events

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_ifelse.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_ifelse.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [IfElse](t_nationalinstruments_veristand_realtimesequencedefinitionapi_ifelse.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IfElse Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_realtimesequence.htm language=enus -->
## TOPIC 00058: RealTimeSequence Events

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_realtimesequence.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_realtimesequence.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [RealTimeSequence](t_nationalinstruments_veristand_realtimesequencedefinitionapi_realtimesequence.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

RealTimeSequence Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_reference.htm language=enus -->
## TOPIC 00059: Reference Events

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_reference.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_reference.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [Reference](t_nationalinstruments_veristand_realtimesequencedefinitionapi_reference.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Reference Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_setup.htm language=enus -->
## TOPIC 00060: Setup Events

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_setup.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_setup.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [Setup](t_nationalinstruments_veristand_realtimesequencedefinitionapi_setup.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Setup Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_statement.htm language=enus -->
## TOPIC 00061: Statement Events

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_statement.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_statement.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [Statement](t_nationalinstruments_veristand_realtimesequencedefinitionapi_statement.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Statement Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_task.htm language=enus -->
## TOPIC 00062: Task Events

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_task.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/events_t_nationalinstruments_veristand_realtimesequencedefinitionapi_task.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [Task](t_nationalinstruments_veristand_realtimesequencedefinitionapi_task.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Task Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/events_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_evaluation.htm language=enus -->
## TOPIC 00063: Evaluation Events

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/events_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_evaluation.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/events_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_evaluation.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [Evaluation](t_nationalinstruments_veristand_stimulusprofiledefinitionapi_evaluation.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Evaluation Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/events_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_ftpbase.htm language=enus -->
## TOPIC 00064: FTPBase Events

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/events_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_ftpbase.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/events_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_ftpbase.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [FTPBase](t_nationalinstruments_veristand_stimulusprofiledefinitionapi_ftpbase.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

FTPBase Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/events_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_launchniveristand.htm language=enus -->
## TOPIC 00065: LaunchNIVeriStand Events

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/events_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_launchniveristand.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/events_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_launchniveristand.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [LaunchNIVeriStand](t_nationalinstruments_veristand_stimulusprofiledefinitionapi_launchniveristand.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

LaunchNIVeriStand Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/events_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_logchannelgroup.htm language=enus -->
## TOPIC 00066: LogChannelGroup Events

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/events_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_logchannelgroup.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/events_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_logchannelgroup.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [LogChannelGroup](t_nationalinstruments_veristand_stimulusprofiledefinitionapi_logchannelgroup.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

LogChannelGroup Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/events_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_macroplayerstep.htm language=enus -->
## TOPIC 00067: MacroPlayerStep Events

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/events_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_macroplayerstep.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/events_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_macroplayerstep.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [MacroPlayerStep](t_nationalinstruments_veristand_stimulusprofiledefinitionapi_macroplayerstep.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

MacroPlayerStep Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/events_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_openprojectstep.htm language=enus -->
## TOPIC 00068: OpenProjectStep Events

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/events_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_openprojectstep.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/events_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_openprojectstep.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [OpenProjectStep](t_nationalinstruments_veristand_stimulusprofiledefinitionapi_openprojectstep.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

OpenProjectStep Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/events_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_openworkspacestep.htm language=enus -->
## TOPIC 00069: OpenWorkspaceStep Events

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/events_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_openworkspacestep.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/events_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_openworkspacestep.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [OpenWorkspaceStep](t_nationalinstruments_veristand_stimulusprofiledefinitionapi_openworkspacestep.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

OpenWorkspaceStep Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/events_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_openworkspacetoolstep.htm language=enus -->
## TOPIC 00070: OpenWorkspaceToolStep Events

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/events_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_openworkspacetoolstep.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/events_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_openworkspacetoolstep.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [OpenWorkspaceToolStep](t_nationalinstruments_veristand_stimulusprofiledefinitionapi_openworkspacetoolstep.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

OpenWorkspaceToolStep Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/events_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_realtimesequencegroupstep.htm language=enus -->
## TOPIC 00071: RealTimeSequenceGroupStep Events

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/events_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_realtimesequencegroupstep.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/events_t_nationalinstruments_veristand_stimulusprofiledefinitionapi_realtimesequencegroupstep.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [RealTimeSequenceGroupStep](t_nationalinstruments_veristand_stimulusprofiledefinitionapi_realtimesequencegroupstep.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | PropertyChanged | Occurs when a property value changes. (Inherited from BaseNode.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

RealTimeSequenceGroupStep Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/fields_t_nationalinstruments_veristand_systemdefinitionapi_conditional.htm language=enus -->
## TOPIC 00072: Conditional Fields

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/fields_t_nationalinstruments_veristand_systemdefinitionapi_conditional.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/fields_t_nationalinstruments_veristand_systemdefinitionapi_conditional.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [Conditional](t_nationalinstruments_veristand_systemdefinitionapi_conditional.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Fields

|  | Name | Description |
| --- | --- | --- |
|  | AND | NI VeriStand converts the values of the double data type to the I32 data type and then performs the AND operation on the values bitwise. |
|  | Equal | Equal to operation. |
|  | Greater | Greater than operation. |
|  | GreaterOrEqual | Greater than or equal to operation. |
|  | Less | Less than operation. |
|  | LessOrEqual | Less than or equal to operation. |
|  | NotEqual | Not equal operation. |
|  | OR | NI VeriStand converts the values of the double data type to the I32 data type and then performs the OR operation on the values bitwise. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Conditional Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/fields_t_nationalinstruments_veristand_systemdefinitionapi_modelsupport_modelloader.htm language=enus -->
## TOPIC 00073: ModelLoader Fields

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/fields_t_nationalinstruments_veristand_systemdefinitionapi_modelsupport_modelloader.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/fields_t_nationalinstruments_veristand_systemdefinitionapi_modelsupport_modelloader.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [ModelLoader](t_nationalinstruments_veristand_systemdefinitionapi_modelsupport_modelloader.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Fields

|  | Name | Description |
| --- | --- | --- |
|  | ModelPath | The model path. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ModelLoader Class

NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_factory_getchannelmonitor_1.htm language=enus -->
## TOPIC 00074: Factory.GetChannelMonitor Method (String)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_factory_getchannelmonitor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_factory_getchannelmonitor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets the IChannelMonitor interface, which you can use to register and deregister for Channel Value Change Events.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetChannelMonitor ( _ gateway_ip_address As String _ ) As IChannelMonitor |

| C# |
| --- |
| public IChannelMonitor GetChannelMonitor( string gateway_ip_address ) |

| Visual C++ |
| --- |
| public: IChannelMonitor^ GetChannelMonitor( String^ gateway_ip_address ) |

###### Parameters

- **gateway_ip_address**
  - Type: System.StringSpecifies the IP address of the VeriStand Gateway.

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Factory Class

GetChannelMonitor Overload

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_factory_getialarmmanager.htm language=enus -->
## TOPIC 00075: Factory.GetIAlarmManager Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_factory_getialarmmanager.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_factory_getialarmmanager.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

GetIAlarmManager2

Gets the [IAlarmManager](t_nationalinstruments_veristand_clientapi_ialarmmanager.htm) interface, which you can use to get a list of alarms configured on the system and the status of those alarms.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetIAlarmManager As IAlarmManager |

| C# |
| --- |
| public IAlarmManager GetIAlarmManager() |

| Visual C++ |
| --- |
| public: IAlarmManager^ GetIAlarmManager() |

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Factory Class

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_factory_geticalibration.htm language=enus -->
## TOPIC 00076: Factory.GetICalibration Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_factory_geticalibration.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_factory_geticalibration.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

**NOTE: This method is obsolete.**

ICalibration

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| <ObsoleteAttribute("This method is obsolete in NI VeriStand 2012 and later. Use the GetICalibration2 method instead.")> _ Public Function GetICalibration ( _ gateway_ip_address As String _ ) As ICalibration |

| C# |
| --- |
| [ObsoleteAttribute("This method is obsolete in NI VeriStand 2012 and later. Use the GetICalibration2 method instead.")] public ICalibration GetICalibration( string gateway_ip_address ) |

| Visual C++ |
| --- |
| [ObsoleteAttribute(L"This method is obsolete in NI VeriStand 2012 and later. Use the GetICalibration2 method instead.")] public: ICalibration^ GetICalibration( String^ gateway_ip_address ) |

###### Parameters

- **gateway_ip_address**
  - Type: System.String Specifies the IP address of the VeriStand Gateway.

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Factory Class

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_factory_getimacrorecorder.htm language=enus -->
## TOPIC 00077: Factory.GetIMacroRecorder Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_factory_getimacrorecorder.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_factory_getimacrorecorder.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

IMacroRecorder

.nivsmacro

IMacroPlayer

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetIMacroRecorder As IMacroRecorder |

| C# |
| --- |
| public IMacroRecorder GetIMacroRecorder() |

| Visual C++ |
| --- |
| public: IMacroRecorder^ GetIMacroRecorder() |

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Factory Class

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_factory_getimodel_1.htm language=enus -->
## TOPIC 00078: Factory.GetIModel Method (String, String, String)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_factory_getimodel_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_factory_getimodel_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

IModel

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetIModel ( _ gateway_ip_address As String, _ target As String, _ modelName As String _ ) As IModel |

| C# |
| --- |
| public IModel GetIModel( string gateway_ip_address, string target, string modelName ) |

| Visual C++ |
| --- |
| public: IModel^ GetIModel( String^ gateway_ip_address, String^ target, String^ modelName ) |

###### Parameters

- **gateway_ip_address**
  - Type: System.String Specifies the IP address of the VeriStand Gateway.

- **target**
  - Type: System.String Specifies the name of the target, or execution host. on which the model is running.

- **modelName**
  - Type: System.String Specifies the name of the model you want to access.

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Factory Class

GetIModel Overload

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_factory_getistimulusprofilesession.htm language=enus -->
## TOPIC 00079: Factory.GetIStimulusProfileSession Method (String, String)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_factory_getistimulusprofilesession.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_factory_getistimulusprofilesession.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

IStimulusProfileSession

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetIStimulusProfileSession ( _ gateway_ip_address As String, _ session_id As String _ ) As IStimulusProfileSession |

| C# |
| --- |
| public IStimulusProfileSession GetIStimulusProfileSession( string gateway_ip_address, string session_id ) |

| Visual C++ |
| --- |
| public: IStimulusProfileSession^ GetIStimulusProfileSession( String^ gateway_ip_address, String^ session_id ) |

###### Parameters

- **gateway_ip_address**
  - Type: System.String Specifies the IP address of the VeriStand Gateway.

- **session_id**
  - Type: System.String Specifies the Session ID of the deployed Stimulus Profile Session.

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Factory Class

GetIStimulusProfileSession Overload

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_factory_getiwaveformstreaming.htm language=enus -->
## TOPIC 00080: Factory.GetIWaveformStreaming Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_factory_getiwaveformstreaming.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_factory_getiwaveformstreaming.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets the IWaveformStreaming interface, which you can use to stream waveform data from the VeriStand Gateway.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetIWaveformStreaming ( _ gatewayIPAddress As String _ ) As IWaveformStreaming |

| C# |
| --- |
| public IWaveformStreaming GetIWaveformStreaming( string gatewayIPAddress ) |

| Visual C++ |
| --- |
| public: IWaveformStreaming^ GetIWaveformStreaming( String^ gatewayIPAddress ) |

###### Parameters

- **gatewayIPAddress**
  - Type: System.StringSpecifies the IP address of the VeriStand Gateway.

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Factory Class

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_factory_getiworkspace.htm language=enus -->
## TOPIC 00081: Factory.GetIWorkspace Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_factory_getiworkspace.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_factory_getiworkspace.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

GetIWorkspace2

Gets the [IWorkspace](t_nationalinstruments_veristand_clientapi_iworkspace.htm) interface, which you can use to run or stop the Workspace, get channel and alias information, and set values for channels.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetIWorkspace As IWorkspace |

| C# |
| --- |
| public IWorkspace GetIWorkspace() |

| Visual C++ |
| --- |
| public: IWorkspace^ GetIWorkspace() |

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Factory Class

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_factory_getiworkspace2_1.htm language=enus -->
## TOPIC 00082: Factory.GetIWorkspace2 Method (String)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_factory_getiworkspace2_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_factory_getiworkspace2_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

IWorkspace2

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetIWorkspace2 ( _ gateway_ip_address As String _ ) As IWorkspace2 |

| C# |
| --- |
| public IWorkspace2 GetIWorkspace2( string gateway_ip_address ) |

| Visual C++ |
| --- |
| public: IWorkspace2^ GetIWorkspace2( String^ gateway_ip_address ) |

###### Parameters

- **gateway_ip_address**
  - Type: System.StringSpecifies the IP address of the VeriStand Gateway.

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Factory Class

GetIWorkspace2 Overload

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_imodelmanager2_unregisterforparametervaluechange.htm language=enus -->
## TOPIC 00083: IModelManager2.UnregisterForParameterValueChange Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_imodelmanager2_unregisterforparametervaluechange.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_imodelmanager2_unregisterforparametervaluechange.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Unregisters a delegate for a change in a particular model parameter.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Function UnregisterForParameterValueChange ( _ target As String, _ parameter As String, _ eventHandler As EventHandler(Of ParameterValueChangeEventArgs) _ ) As Error |

| C# |
| --- |
| Error UnregisterForParameterValueChange( string target, string parameter, EventHandler<ParameterValueChangeEventArgs> eventHandler ) |

| Visual C++ |
| --- |
| Error^ UnregisterForParameterValueChange( String^ target, String^ parameter, EventHandler<ParameterValueChangeEventArgs^>^ eventHandler ) |

###### Parameters

- **target**
  - Type: System.String Target the model parameter exists on

- **parameter**
  - Type: System.String Name of the model parameter

- **eventHandler**
  - Type: System.EventHandlerParameterValueChangeEventArgs Delegate function that was registered to the event

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IModelManager2 Interface

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_imodelmanager_getparametervectorvalues.htm language=enus -->
## TOPIC 00084: IModelManager.GetParameterVectorValues Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_imodelmanager_getparametervectorvalues.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_imodelmanager_getparametervectorvalues.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

GetParameterVectorValues

IModelManager2

Gets the vector values for a model parameter present on the *first* target. You must use the [GetParameterVectorValues](overload_nationalinstruments_veristand_clientapi_imodelmanager2_getparametervectorvalues.htm) method of the [IModelManager2](t_nationalinstruments_veristand_clientapi_imodelmanager2.htm) interface if you want to specify one of multiple targets.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Function GetParameterVectorValues ( _ parameter As String, _ <OutAttribute> ByRef rowDim As UInteger, _ <OutAttribute> ByRef colDim As UInteger, _ <OutAttribute> ByRef values As Double() _ ) As Error |

| C# |
| --- |
| Error GetParameterVectorValues( string parameter, out uint rowDim, out uint colDim, out double[] values ) |

| Visual C++ |
| --- |
| Error^ GetParameterVectorValues( String^ parameter, [OutAttribute] unsigned int% rowDim, [OutAttribute] unsigned int% colDim, [OutAttribute] array<double>^% values ) |

###### Parameters

- **parameter**
  - Type: System.String The parameter for which to get values. Use the GetParametersList method to get a list of model parameters from which you can select this input.

- **rowDim**
  - Type: System.UInt32 % The number of rows in the vector array.

- **colDim**
  - Type: System.UInt32 % The number of columns in the vector array.

- **values**
  - Type: System.Double % The vector values.

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IModelManager Interface

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_imodelmanager_getsingleparametervalue.htm language=enus -->
## TOPIC 00085: IModelManager.GetSingleParameterValue Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_imodelmanager_getsingleparametervalue.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_imodelmanager_getsingleparametervalue.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

GetSingleParameterValue

IModelManager2

Gets the value of a single model parameter present on the *first* target. You must use the [GetSingleParameterValue](overload_nationalinstruments_veristand_clientapi_imodelmanager2_getsingleparametervalue.htm) method of the [IModelManager2](t_nationalinstruments_veristand_clientapi_imodelmanager2.htm) interface if you want to specify one of multiple targets.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Function GetSingleParameterValue ( _ parameter As String, _ <OutAttribute> ByRef value As Double _ ) As Error |

| C# |
| --- |
| Error GetSingleParameterValue( string parameter, out double value ) |

| Visual C++ |
| --- |
| Error^ GetSingleParameterValue( String^ parameter, [OutAttribute] double% value ) |

###### Parameters

- **parameter**
  - Type: System.String The name of the parameter for which to get the value.

- **value**
  - Type: System.Double % The value of parameter.

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IModelManager Interface

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_imodelmanager_setsingleparametervalue.htm language=enus -->
## TOPIC 00086: IModelManager.SetSingleParameterValue Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_imodelmanager_setsingleparametervalue.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_imodelmanager_setsingleparametervalue.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

SetSingleParameterValue

IModelManager2

Sets the value of a single model parameter present on the *first* target. You must use the [SetSingleParameterValue](overload_nationalinstruments_veristand_clientapi_imodelmanager2_setsingleparametervalue.htm) method of the [IModelManager2](t_nationalinstruments_veristand_clientapi_imodelmanager2.htm) interface if you want to specify one of multiple targets.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Function SetSingleParameterValue ( _ parameter As String, _ newValue As Double _ ) As Error |

| C# |
| --- |
| Error SetSingleParameterValue( string parameter, double newValue ) |

| Visual C++ |
| --- |
| Error^ SetSingleParameterValue( String^ parameter, double newValue ) |

###### Parameters

- **parameter**
  - Type: System.String The name of the parameter for which to set the value.

- **newValue**
  - Type: System.Double The vector values to set on parameter.

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IModelManager Interface

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_iproject_deploy_1.htm language=enus -->
## TOPIC 00087: IProject.Deploy Method (Boolean)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_iproject_deploy_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_iproject_deploy_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Deploys the system definition file associated with an NI VeriStand project to the target. This method includes the option to display a deployment progress dialog.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Function Deploy ( _ show_progress As Boolean _ ) As Error |

| C# |
| --- |
| Error Deploy( bool show_progress ) |

| Visual C++ |
| --- |
| Error^ Deploy( bool show_progress ) |

###### Parameters

- **show_progress**
  - Type: System.Boolean Specifies whether to display a progress dialog while deploying.

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IProject Interface

Deploy Overload

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_iproject_openworkspace.htm language=enus -->
## TOPIC 00088: IProject.OpenWorkspace Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_iproject_openworkspace.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_iproject_openworkspace.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Workspace

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Function OpenWorkspace As Error |

| C# |
| --- |
| Error OpenWorkspace() |

| Visual C++ |
| --- |
| Error^ OpenWorkspace() |

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IProject Interface

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_iproject_quit.htm language=enus -->
## TOPIC 00089: IProject.Quit Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_iproject_quit.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_iproject_quit.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Workspace

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Function Quit As Error |

| C# |
| --- |
| Error Quit() |

| Visual C++ |
| --- |
| Error^ Quit() |

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IProject Interface

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_isequencecontrol_getreturnvalue.htm language=enus -->
## TOPIC 00090: ISequenceControl.GetReturnValue Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_isequencecontrol_getreturnvalue.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_isequencecontrol_getreturnvalue.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets the return value for the sequence. This function will fail if the sequence has not completed execution.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Function GetReturnValue As DataValue |

| C# |
| --- |
| DataValue GetReturnValue() |

| Visual C++ |
| --- |
| DataValue^ GetReturnValue() |

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ISequenceControl Interface

GetReturnValue Overload

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_isequencecontrol_getsequencetime.htm language=enus -->
## TOPIC 00091: ISequenceControl.GetSequenceTime Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_isequencecontrol_getsequencetime.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_isequencecontrol_getsequencetime.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets the relative time since the sequence started, as determined by the delta t at which the sequence executes and the number of executed iterations.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Function GetSequenceTime As Double |

| C# |
| --- |
| double GetSequenceTime() |

| Visual C++ |
| --- |
| double GetSequenceTime() |

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ISequenceControl Interface

GetSequenceTime Overload

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_isequencecontrol_getsequencetime_1.htm language=enus -->
## TOPIC 00092: ISequenceControl.GetSequenceTime Method ()

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_isequencecontrol_getsequencetime_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_isequencecontrol_getsequencetime_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets the relative time since the sequence started, as determined by the delta t at which the sequence executes and the number of executed iterations. If an error occurs, this instance outputs an error object.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Function GetSequenceTime ( _ <OutAttribute> ByRef error As Error _ ) As Double |

| C# |
| --- |
| double GetSequenceTime( out Error error ) |

| Visual C++ |
| --- |
| double GetSequenceTime( [OutAttribute] Error^% error ) |

###### Parameters

- **error**
  - Type: Error %The error object.

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ISequenceControl Interface

GetSequenceTime Overload

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_isequencecontrol_pause.htm language=enus -->
## TOPIC 00093: ISequenceControl.Pause Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_isequencecontrol_pause.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_isequencecontrol_pause.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Pauses the sequence.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Sub Pause |

| C# |
| --- |
| void Pause() |

| Visual C++ |
| --- |
| void Pause() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ISequenceControl Interface

Pause Overload

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_isequencecontrol_pause_1.htm language=enus -->
## TOPIC 00094: ISequenceControl.Pause Method ()

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_isequencecontrol_pause_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_isequencecontrol_pause_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Pauses the sequence. If an error occurs, this instance outputs an error object.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Sub Pause ( _ <OutAttribute> ByRef error As Error _ ) |

| C# |
| --- |
| void Pause( out Error error ) |

| Visual C++ |
| --- |
| void Pause( [OutAttribute] Error^% error ) |

###### Parameters

- **error**
  - Type: Error % The error object.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ISequenceControl Interface

Pause Overload

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_isequencecontrol_run.htm language=enus -->
## TOPIC 00095: ISequenceControl.Run Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_isequencecontrol_run.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_isequencecontrol_run.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Runs the sequence.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Sub Run |

| C# |
| --- |
| void Run() |

| Visual C++ |
| --- |
| void Run() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ISequenceControl Interface

Run Overload

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_isequencecontrol_run_1.htm language=enus -->
## TOPIC 00096: ISequenceControl.Run Method ()

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_isequencecontrol_run_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_isequencecontrol_run_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Runs the sequence. If an error occurs, this instance outputs an error object.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Sub Run ( _ <OutAttribute> ByRef error As Error _ ) |

| C# |
| --- |
| void Run( out Error error ) |

| Visual C++ |
| --- |
| void Run( [OutAttribute] Error^% error ) |

###### Parameters

- **error**
  - Type: Error %The error object.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ISequenceControl Interface

Run Overload

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_isequencecontrol_singlestep.htm language=enus -->
## TOPIC 00097: ISequenceControl.SingleStep Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_isequencecontrol_singlestep.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_isequencecontrol_singlestep.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Single-steps the sequence.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Sub SingleStep |

| C# |
| --- |
| void SingleStep() |

| Visual C++ |
| --- |
| void SingleStep() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ISequenceControl Interface

SingleStep Overload

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_isequencecontrol_singlestep_1.htm language=enus -->
## TOPIC 00098: ISequenceControl.SingleStep Method ()

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_isequencecontrol_singlestep_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_isequencecontrol_singlestep_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Single-steps the sequence. If an error occurs, this instance outputs an error object.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Sub SingleStep ( _ <OutAttribute> ByRef error As Error _ ) |

| C# |
| --- |
| void SingleStep( out Error error ) |

| Visual C++ |
| --- |
| void SingleStep( [OutAttribute] Error^% error ) |

###### Parameters

- **error**
  - Type: Error %The error object.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ISequenceControl Interface

SingleStep Overload

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulus_getstimulusprofilefile.htm language=enus -->
## TOPIC 00099: IStimulus.GetStimulusProfileFile Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulus_getstimulusprofilefile.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulus_getstimulusprofilefile.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets the stimulus profile file that is running on the target.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Function GetStimulusProfileFile ( _ <OutAttribute> ByRef file_path As String _ ) As Error |

| C# |
| --- |
| Error GetStimulusProfileFile( out string file_path ) |

| Visual C++ |
| --- |
| Error^ GetStimulusProfileFile( [OutAttribute] String^% file_path ) |

###### Parameters

- **file_path**
  - Type: System.String %Returns the path to the stimulus profile file.

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

The method is valid for the original version of the NI VeriStand Stimulus Profile Editor only. In NI VeriStand 2011 and later, this method is maintained for compatibility purposes only. Use the members of the Stimulus Profile Execution API to interact with stimulus profiles in NI VeriStand 2011 and later.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IStimulus Interface

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulus_getstimulusprofilemanagerstate.htm language=enus -->
## TOPIC 00100: IStimulus.GetStimulusProfileManagerState Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulus_getstimulusprofilemanagerstate.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulus_getstimulusprofilemanagerstate.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets the state of the stimulus profile manager.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Function GetStimulusProfileManagerState ( _ <OutAttribute> ByRef state As StimulusState _ ) As Error |

| C# |
| --- |
| Error GetStimulusProfileManagerState( out StimulusState state ) |

| Visual C++ |
| --- |
| Error^ GetStimulusProfileManagerState( [OutAttribute] StimulusState% state ) |

###### Parameters

- **state**
  - Type: NationalInstruments.VeriStand.ClientAPI.StimulusState %The StimulusState of the stimulus profile manager.

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

The method is valid for the original version of the NI VeriStand Stimulus Profile Editor only. In NI VeriStand 2011 and later, this method is maintained for compatibility purposes only. Use the members of the Stimulus Profile Execution API to interact with stimulus profiles in NI VeriStand 2011 and later.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IStimulus Interface

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulus_getstimulusprofileresult.htm language=enus -->
## TOPIC 00101: IStimulus.GetStimulusProfileResult Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulus_getstimulusprofileresult.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulus_getstimulusprofileresult.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets the results of the last stimulus profile that ran on the target, including whether it passed, failed, or received an error.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Function GetStimulusProfileResult ( _ <OutAttribute> ByRef result As StimulusResult, _ <OutAttribute> ByRef file_result As String _ ) As Error |

| C# |
| --- |
| Error GetStimulusProfileResult( out StimulusResult result, out string file_result ) |

| Visual C++ |
| --- |
| Error^ GetStimulusProfileResult( [OutAttribute] StimulusResult% result, [OutAttribute] String^% file_result ) |

###### Parameters

- **result**
  - Type: NationalInstruments.VeriStand.ClientAPI.StimulusResult %The StimulusResult of the stimulus profile.

- **file_result**
  - Type: System.String %The file name of a .csv file containing the results of the last stimulus profile file that ran on the target.

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

The method is valid for the original version of the NI VeriStand Stimulus Profile Editor only. In NI VeriStand 2011 and later, this method is maintained for compatibility purposes. Use the members of the Stimulus Profile Execution API to interact with stimulus profiles in NI VeriStand 2011 and later.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IStimulus Interface

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulus_unreservestimulusprofilemanager.htm language=enus -->
## TOPIC 00102: IStimulus.UnreserveStimulusProfileManager Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulus_unreservestimulusprofilemanager.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulus_unreservestimulusprofilemanager.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Unreserves the stimulus profile manager.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Function UnreserveStimulusProfileManager As Error |

| C# |
| --- |
| Error UnreserveStimulusProfileManager() |

| Visual C++ |
| --- |
| Error^ UnreserveStimulusProfileManager() |

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

The method is valid for the original version of the NI VeriStand Stimulus Profile Editor only. In NI VeriStand 2011 and later, this method is maintained for compatibility purposes only. Use the members of the Stimulus Profile Execution API to interact with stimulus profiles in NI VeriStand 2011 and later.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IStimulus Interface

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulusprofilesession_deploy.htm language=enus -->
## TOPIC 00103: IStimulusProfileSession.Deploy Method (Boolean, String)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulusprofilesession_deploy.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulusprofilesession_deploy.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Deploys the Stimulus Profile Session. If an error occurs, this instance throws an exception.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Sub Deploy ( _ auto_start As Boolean, _ <OutAttribute> ByRef session_id As String _ ) |

| C# |
| --- |
| void Deploy( bool auto_start, out string session_id ) |

| Visual C++ |
| --- |
| void Deploy( bool auto_start, [OutAttribute] String^% session_id ) |

###### Parameters

- **auto_start**
  - Type: System.Boolean If true (True in Visual Basic), starts sequences immediately upon deploy. If false (False in Visual Basic), waits for an external Run command.

- **session_id**
  - Type: System.String %The ID of the Stimulus profile session.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IStimulusProfileSession Interface

Deploy Overload

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulusprofilesession_deploy_1.htm language=enus -->
## TOPIC 00104: IStimulusProfileSession.Deploy Method (Boolean, String, )

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulusprofilesession_deploy_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulusprofilesession_deploy_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

error

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Sub Deploy ( _ auto_start As Boolean, _ <OutAttribute> ByRef session_id As String, _ <OutAttribute> ByRef error As Error _ ) |

| C# |
| --- |
| void Deploy( bool auto_start, out string session_id, out Error error ) |

| Visual C++ |
| --- |
| void Deploy( bool auto_start, [OutAttribute] String^% session_id, [OutAttribute] Error^% error ) |

###### Parameters

- **auto_start**
  - Type: System.Boolean If true (True in Visual Basic), starts sequences immediately upon deploy. If false (False in Visual Basic), waits for an external Run command.

- **session_id**
  - Type: System.String %The ID of the Stimulus Profile Session.

- **error**
  - Type: Error %The error object.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IStimulusProfileSession Interface

Deploy Overload

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulusprofilesession_run.htm language=enus -->
## TOPIC 00105: IStimulusProfileSession.Run Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulusprofilesession_run.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulusprofilesession_run.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Runs the Stimulus Profile Session. If an error occurs, this instance throws an exception.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Sub Run |

| C# |
| --- |
| void Run() |

| Visual C++ |
| --- |
| void Run() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IStimulusProfileSession Interface

Run Overload

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulusprofilesession_run_1.htm language=enus -->
## TOPIC 00106: IStimulusProfileSession.Run Method ()

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulusprofilesession_run_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulusprofilesession_run_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Runs the Stimulus Profile Session. If an error occurs, this instance outputs an error object.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Sub Run ( _ <OutAttribute> ByRef error As Error _ ) |

| C# |
| --- |
| void Run( out Error error ) |

| Visual C++ |
| --- |
| void Run( [OutAttribute] Error^% error ) |

###### Parameters

- **error**
  - Type: Error %The error object.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IStimulusProfileSession Interface

Run Overload

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulusprofilesession_stop_1.htm language=enus -->
## TOPIC 00107: IStimulusProfileSession.Stop Method ()

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulusprofilesession_stop_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulusprofilesession_stop_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Stops the Stimulus Profile Session. If an error occurs, this instance outputs an error object.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Sub Stop ( _ <OutAttribute> ByRef error As Error _ ) |

| C# |
| --- |
| void Stop( out Error error ) |

| Visual C++ |
| --- |
| void Stop( [OutAttribute] Error^% error ) |

###### Parameters

- **error**
  - Type: Error %The error object.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IStimulusProfileSession Interface

Stop Overload

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulusprofilesession_undeploy.htm language=enus -->
## TOPIC 00108: IStimulusProfileSession.Undeploy Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulusprofilesession_undeploy.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulusprofilesession_undeploy.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Undeploys the Stimulus Profile Session. If an error occurs, this instance throws an exception.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Sub Undeploy |

| C# |
| --- |
| void Undeploy() |

| Visual C++ |
| --- |
| void Undeploy() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IStimulusProfileSession Interface

Undeploy Overload

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulusprofilesession_undeploy_1.htm language=enus -->
## TOPIC 00109: IStimulusProfileSession.Undeploy Method ()

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulusprofilesession_undeploy_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_istimulusprofilesession_undeploy_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Undeploys the Stimulus Profile Session. If an error occurs, this instance outputs an error object.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Sub Undeploy ( _ <OutAttribute> ByRef error As Error _ ) |

| C# |
| --- |
| void Undeploy( out Error error ) |

| Visual C++ |
| --- |
| void Undeploy( [OutAttribute] Error^% error ) |

###### Parameters

- **error**
  - Type: Error %The error object.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IStimulusProfileSession Interface

Undeploy Overload

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_iudpchannelstreamsession_undeployudpchannelstreamsession.htm language=enus -->
## TOPIC 00110: IUDPChannelStreamSession.UndeployUDPChannelStreamSession Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_iudpchannelstreamsession_undeployudpchannelstreamsession.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_iudpchannelstreamsession_undeployudpchannelstreamsession.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

| Note: |
| --- |
| If a client has a request open for a channel, the VeriStand Gateway continues to publish data even after this method executes. |

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Function UndeployUDPChannelStreamSession As Error |

| C# |
| --- |
| Error UndeployUDPChannelStreamSession() |

| Visual C++ |
| --- |
| Error^ UndeployUDPChannelStreamSession() |

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IUDPChannelStreamSession Interface

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_iworkspace_getenginestate.htm language=enus -->
## TOPIC 00111: IWorkspace.GetEngineState Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_iworkspace_getenginestate.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_iworkspace_getenginestate.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

GetSystemState

Returns the current state of the VeriStand Engine.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Function GetEngineState ( _ <OutAttribute> ByRef state As SystemState, _ <OutAttribute> ByRef workspace_file As String, _ <OutAttribute> ByRef systemdefinition_file As String, _ <OutAttribute> ByRef ip_address As String _ ) As Error |

| C# |
| --- |
| Error GetEngineState( out SystemState state, out string workspace_file, out string systemdefinition_file, out string ip_address ) |

| Visual C++ |
| --- |
| Error^ GetEngineState( [OutAttribute] SystemState% state, [OutAttribute] String^% workspace_file, [OutAttribute] String^% systemdefinition_file, [OutAttribute] String^% ip_address ) |

###### Parameters

- **state**
  - Type: NationalInstruments.VeriStand.ClientAPI.SystemState % The current SystemState of the VeriStand Engine.

- **workspace_file**
  - Type: System.String % The current system definition file. The workspace file does not exist in NI VeriStand 2010 and later.

- **systemdefinition_file**
  - Type: System.String % The current system definition file.

- **ip_address**
  - Type: System.String % The IP address of the system.

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IWorkspace Interface

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_iworkspace_getsystemnodechannellist.htm language=enus -->
## TOPIC 00112: IWorkspace.GetSystemNodeChannelList Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_iworkspace_getsystemnodechannellist.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_iworkspace_getsystemnodechannellist.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

nodeName

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Function GetSystemNodeChannelList ( _ nodeName As String, _ <OutAttribute> ByRef channels As NodeInfo() _ ) As Error |

| C# |
| --- |
| Error GetSystemNodeChannelList( string nodeName, out NodeInfo[] channels ) |

| Visual C++ |
| --- |
| Error^ GetSystemNodeChannelList( String^ nodeName, [OutAttribute] array<NodeInfo^>^% channels ) |

###### Parameters

- **nodeName**
  - Type: System.String The name of the node for which you want to see all channels. If this parameter is empty, this method gets all the channels in the system.

- **channels**
  - Type: NationalInstruments.VeriStand.ClientAPI.NodeInfo % An array containing information about all the channels. You can index this array and use the members of the NodeInfo class to get specific information about each channel, such as its name, path, GUID, and whether it is readable, writable, scalable, faultable, and so on.

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IWorkspace Interface

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_iworkspace_getsystemnodechildren.htm language=enus -->
## TOPIC 00113: IWorkspace.GetSystemNodeChildren Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_iworkspace_getsystemnodechildren.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_iworkspace_getsystemnodechildren.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

nodeName

GetSystemNodeChannelList

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Function GetSystemNodeChildren ( _ nodeName As String, _ <OutAttribute> ByRef nodes As NodeInfo() _ ) As Error |

| C# |
| --- |
| Error GetSystemNodeChildren( string nodeName, out NodeInfo[] nodes ) |

| Visual C++ |
| --- |
| Error^ GetSystemNodeChildren( String^ nodeName, [OutAttribute] array<NodeInfo^>^% nodes ) |

###### Parameters

- **nodeName**
  - Type: System.String The name of the node for which you want to see all child nodes.

- **nodes**
  - Type: NationalInstruments.VeriStand.ClientAPI.NodeInfo % An array containing information about all the child nodes. You can index this array and use the members of the NodeInfo class to get specific information about each node, such as its name, path, GUID, and, if the node is a channel, information about the channel.

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IWorkspace Interface

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_iworkspace_lockworkspacefile.htm language=enus -->
## TOPIC 00114: IWorkspace.LockWorkspaceFile Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_iworkspace_lockworkspacefile.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_iworkspace_lockworkspacefile.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

LockConnection

Locks a running workspace configuration so that a user must provide a password to stop running the configuration. The configuration must be running when you call this method. If the configuration has an existing password, you must provide the password to the old_password parameter in order to set the new password.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Function LockWorkspaceFile ( _ old_password As String, _ new_password As String _ ) As Error |

| C# |
| --- |
| Error LockWorkspaceFile( string old_password, string new_password ) |

| Visual C++ |
| --- |
| Error^ LockWorkspaceFile( String^ old_password, String^ new_password ) |

###### Parameters

- **old_password**
  - Type: System.String The existing password for the configuration. If no password exists, this method ignores this parameter.

- **new_password**
  - Type: System.String The password to use to lock the configuration.

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IWorkspace Interface

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_iworkspace_runworkspacefile.htm language=enus -->
## TOPIC 00115: IWorkspace.RunWorkspaceFile Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_iworkspace_runworkspacefile.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_iworkspace_runworkspacefile.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

ConnectToSystem

Runs the workspace configuration you specify. If a configuration is already running when you call this method, the method returns an error.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Function RunWorkspaceFile ( _ file_path As String, _ launchworkspace As Boolean, _ deploysystemdefinition As Boolean, _ timeout As UInteger, _ user_name As String, _ password As String _ ) As Error |

| C# |
| --- |
| Error RunWorkspaceFile( string file_path, bool launchworkspace, bool deploysystemdefinition, uint timeout, string user_name, string password ) |

| Visual C++ |
| --- |
| Error^ RunWorkspaceFile( String^ file_path, bool launchworkspace, bool deploysystemdefinition, unsigned int timeout, String^ user_name, String^ password ) |

###### Parameters

- **file_path**
  - Type: System.String The path to the configuration.

- **launchworkspace**
  - Type: System.Boolean Specifies whether to launch the Workspace window. This input is ignored in NI VeriStand 2010 and later.

- **deploysystemdefinition**
  - Type: System.Boolean Specifies whether to deploy the system definition file before running the workspace.

- **timeout**
  - Type: System.UInt32 The time allowed for the VeriStand Gateway to successfully deploy the system definition to the target(s) and for the target(s) to achieve active running state. If timeout is exceeded, deployment is cancelled.

- **user_name**
  - Type: System.String The user name to use to access the NI VeriStand project. This parameter is ignored in NI VeriStand 2010 and later.

- **password**
  - Type: System.String The password associated with the user_name you enter. This input is ignored in NI VeriStand 2010 and later.

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IWorkspace Interface

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_logging_timesegmentingspecification__ctor.htm language=enus -->
## TOPIC 00116: TimeSegmentingSpecification Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_logging_timesegmentingspecification__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_logging_timesegmentingspecification__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Initializes a new instance of the TimeSegmentingSpecification class.

Namespace:

NationalInstruments.VeriStand.ClientAPI.Logging

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ maxInstances As Integer, _ timeLimit As Double _ ) |

| C# |
| --- |
| public TimeSegmentingSpecification( int maxInstances, double timeLimit ) |

| Visual C++ |
| --- |
| public: TimeSegmentingSpecification( int maxInstances, double timeLimit ) |

###### Parameters

- **maxInstances**
  - Type: System.Int32The maximum number of file instances that can be created. A value of -1 indicates that an unlimited number of file instances can be created.

- **timeLimit**
  - Type: System.DoubleThe time in seconds after which a log file will be segmented.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

TimeSegmentingSpecification Class

NationalInstruments.VeriStand.ClientAPI.Logging Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_loginfo__ctor.htm language=enus -->
## TOPIC 00117: LogInfo Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_loginfo__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_loginfo__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

LogInfo

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New |

| C# |
| --- |
| public LogInfo() |

| Visual C++ |
| --- |
| public: LogInfo() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

LogInfo Class

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_parametervaluechangeeventargs__ctor.htm language=enus -->
## TOPIC 00118: ParameterValueChangeEventArgs Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_parametervaluechangeeventargs__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_parametervaluechangeeventargs__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

ParameterValueChangeEventArgs

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ target As String, _ paramName As String, _ value As DataArray _ ) |

| C# |
| --- |
| public ParameterValueChangeEventArgs( string target, string paramName, DataArray value ) |

| Visual C++ |
| --- |
| public: ParameterValueChangeEventArgs( String^ target, String^ paramName, DataArray^ value ) |

###### Parameters

- **target**
  - Type: System.String The name of the target on which the model parameter exists.

- **paramName**
  - Type: System.String The name of the model parameter whose value changed.

- **value**
  - Type: DataArray An array containing the new value of the model parameter.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ParameterValueChangeEventArgs Class

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_parametervaluewatcher_finalize.htm language=enus -->
## TOPIC 00119: ParameterValueWatcher.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_parametervaluewatcher_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_parametervaluewatcher_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Finalizes an instance of the ParameterValueWatcher class.

Namespace:

NationalInstruments.VeriStand.ClientAPI

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ParameterValueWatcher Class

NationalInstruments.VeriStand.ClientAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_waveformstreaming_iwaveformstreaming_registerfordblwaveformdata.htm language=enus -->
## TOPIC 00120: IWaveformStreaming.RegisterForDBLWaveformData Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_waveformstreaming_iwaveformstreaming_registerfordblwaveformdata.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_waveformstreaming_iwaveformstreaming_registerfordblwaveformdata.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Registers a delegate to receive data defined by waveform stream specifications. Waveforms must be of double data type.

Namespace:

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Function RegisterForDBLWaveformData ( _ waveformStreamSpecifications As WaveformStreamSpecification(), _ eventHandler As EventHandler(Of WaveformDataDBLEventArgs) _ ) As Error |

| C# |
| --- |
| Error RegisterForDBLWaveformData( WaveformStreamSpecification[] waveformStreamSpecifications, EventHandler<WaveformDataDBLEventArgs> eventHandler ) |

| Visual C++ |
| --- |
| Error^ RegisterForDBLWaveformData( array<WaveformStreamSpecification^>^ waveformStreamSpecifications, EventHandler<WaveformDataDBLEventArgs^>^ eventHandler ) |

###### Parameters

- **waveformStreamSpecifications**
  - Type: NationalInstruments.VeriStand.ClientAPI.WaveformStreaming.WaveformStreamSpecification Waveform stream specifications associated with delegate. Must specify waveforms of double data type.

- **eventHandler**
  - Type: System.EventHandlerWaveformDataDBLEventArgs Delegate function to be called when the event is raised.

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IWaveformStreaming Interface

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_waveformstreaming_streamalldata__ctor.htm language=enus -->
## TOPIC 00121: StreamAllData Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_waveformstreaming_streamalldata__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_waveformstreaming_streamalldata__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Initializes a new instance of the StreamAllData class.

Namespace:

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New |

| C# |
| --- |
| public StreamAllData() |

| Visual C++ |
| --- |
| public: StreamAllData() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

StreamAllData Class

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_waveformstreaming_streamalldata_equals_1.htm language=enus -->
## TOPIC 00122: StreamAllData.Equals Method (WaveformStreamCondition)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_waveformstreaming_streamalldata_equals_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_waveformstreaming_streamalldata_equals_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

other

StreamAllData

Namespace:

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function Equals ( _ other As WaveformStreamCondition _ ) As Boolean |

| C# |
| --- |
| public override bool Equals( WaveformStreamCondition other ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( WaveformStreamCondition^ other ) override |

###### Parameters

- **other**
  - Type: NationalInstruments.VeriStand.ClientAPI.WaveformStreaming.WaveformStreamConditionThe WaveformStreamCondition object to compare with the current instance.

###### Return Value

true

True

other

StreamAllData

false

False

###### Implements

IEquatable(T).Equals(T)

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

StreamAllData

WaveformStreamCondition

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

StreamAllData Class

Equals Overload

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_waveformstreaming_streamfirstnseconds_equals.htm language=enus -->
## TOPIC 00123: StreamFirstNSeconds.Equals Method (StreamFirstNSeconds)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_waveformstreaming_streamfirstnseconds_equals.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_waveformstreaming_streamfirstnseconds_equals.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

other

StreamFirstNSeconds

StreamFirstNSeconds

Namespace:

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function Equals ( _ other As StreamFirstNSeconds _ ) As Boolean |

| C# |
| --- |
| public bool Equals( StreamFirstNSeconds other ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( StreamFirstNSeconds^ other ) sealed |

###### Parameters

- **other**
  - Type: NationalInstruments.VeriStand.ClientAPI.WaveformStreaming.StreamFirstNSecondsThe StreamFirstNSeconds object to compare with the current instance.

###### Return Value

true

True

other

false

False

###### Implements

IEquatable(T).Equals(T)

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

StreamFirstNSeconds Class

Equals Overload

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_waveformstreaming_waveformdatawatcherdbl__ctor.htm language=enus -->
## TOPIC 00124: WaveformDataWatcherDBL Constructor (IWaveformStreaming)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_waveformstreaming_waveformdatawatcherdbl__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_waveformstreaming_waveformdatawatcherdbl__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Initializes a new instance of the WaveformDataWatcherDBL class.

Namespace:

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ streamInterface As IWaveformStreaming _ ) |

| C# |
| --- |
| public WaveformDataWatcherDBL( IWaveformStreaming streamInterface ) |

| Visual C++ |
| --- |
| public: WaveformDataWatcherDBL( IWaveformStreaming^ streamInterface ) |

###### Parameters

- **streamInterface**
  - Type: NationalInstruments.VeriStand.ClientAPI.WaveformStreaming.IWaveformStreaming Instance of the interface with which to register the waveform data event

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

WaveformDataWatcherDBL Class

WaveformDataWatcherDBL Overload

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_waveformstreaming_waveformstreamspecification__ctor.htm language=enus -->
## TOPIC 00125: WaveformStreamSpecification Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_waveformstreaming_waveformstreamspecification__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_waveformstreaming_waveformstreamspecification__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Initializes a new instance of the WaveformStreamSpecification class.

Namespace:

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ waveformPath As String _ ) |

| C# |
| --- |
| public WaveformStreamSpecification( string waveformPath ) |

| Visual C++ |
| --- |
| public: WaveformStreamSpecification( String^ waveformPath ) |

###### Parameters

- **waveformPath**
  - Type: System.StringThe system definition path of the waveform to stream.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

WaveformStreamSpecification Class

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_clientapi_waveformstreaming_waveformstreamspecification_equals.htm language=enus -->
## TOPIC 00126: WaveformStreamSpecification.Equals Method (WaveformStreamSpecification)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_clientapi_waveformstreaming_waveformstreamspecification_equals.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_clientapi_waveformstreaming_waveformstreamspecification_equals.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Indicates whether the current WaveformStreamSpecification is equivalent to another WaveformStreamSpecification

Namespace:

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming

Assembly:

NationalInstruments.VeriStand.ClientAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function Equals ( _ other As WaveformStreamSpecification _ ) As Boolean |

| C# |
| --- |
| public bool Equals( WaveformStreamSpecification other ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( WaveformStreamSpecification^ other ) sealed |

###### Parameters

- **other**
  - Type: NationalInstruments.VeriStand.ClientAPI.WaveformStreaming.WaveformStreamSpecificationAn WaveformStreamSpecification to compare with this WaveformStreamSpecification.

###### Return Value

###### Implements

IEquatable(T).Equals(T)

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

WaveformStreamSpecification Class

Equals Overload

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_booleanvalue__ctor_1.htm language=enus -->
## TOPIC 00127: BooleanValue Constructor (BooleanValue)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_booleanvalue__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_booleanvalue__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

BooleanValue

BooleanValue

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ node As BooleanValue _ ) |

| C# |
| --- |
| public BooleanValue( BooleanValue node ) |

| Visual C++ |
| --- |
| public: BooleanValue( BooleanValue^ node ) |

###### Parameters

- **node**
  - Type: NationalInstruments.VeriStand.Data.BooleanValueThe instance of BooleanValue to copy.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

BooleanValue Class

BooleanValue Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_booleanvalue__ctor_2.htm language=enus -->
## TOPIC 00128: BooleanValue Constructor (Boolean)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_booleanvalue__ctor_2.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_booleanvalue__ctor_2.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

BooleanValue

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ value As Boolean _ ) |

| C# |
| --- |
| public BooleanValue( bool value ) |

| Visual C++ |
| --- |
| public: BooleanValue( bool value ) |

###### Parameters

- **value**
  - Type: System.BooleanThe value of the Boolean.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

BooleanValue Class

BooleanValue Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_booleanvalue_compareto.htm language=enus -->
## TOPIC 00129: BooleanValue.CompareTo Method (ScalarDataValue)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_booleanvalue_compareto.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_booleanvalue_compareto.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Compares this instance to a specified object and returns an integer that indicates their relationship to each other.

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function CompareTo ( _ other As ScalarDataValue _ ) As Integer |

| C# |
| --- |
| public override int CompareTo( ScalarDataValue other ) |

| Visual C++ |
| --- |
| public: virtual int CompareTo( ScalarDataValue^ other ) override |

###### Parameters

- **other**
  - Type: NationalInstruments.VeriStand.Data.ScalarDataValueThe object to compare to this instance.

###### Return Value

other

| Condition | Return Value |
| --- | --- |
| Less than zero | This instance is false (False in Visual Basic) and other is true (True in Visual Basic).) |
| Zero | This instance and other are equal (either both are true (True in Visual Basic) or false (False in Visual Basic).) |
| Greater than zero | This instance is true (True in Visual Basic) and other is false (False in Visual Basic), or other is a null reference (Nothing in Visual Basic). |

###### Implements

IComparable(T).CompareTo(T)

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

BooleanValue Class

CompareTo Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_booleanvalue_equals.htm language=enus -->
## TOPIC 00130: BooleanValue.Equals Method (DataResource)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_booleanvalue_equals.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_booleanvalue_equals.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DataResource

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function Equals ( _ other As DataResource _ ) As Boolean |

| C# |
| --- |
| public override bool Equals( DataResource other ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( DataResource^ other ) override |

###### Parameters

- **other**
  - Type: NationalInstruments.VeriStand.Data.DataResourceThe data resource to compare to this instance.

###### Return Value

true

True

other

BooleanValue

false

False

###### Implements

IEquatable(T).Equals(T)

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

BooleanValue Class

Equals Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_booleanvalue_touint32.htm language=enus -->
## TOPIC 00131: BooleanValue.ToUInt32 Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_booleanvalue_touint32.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_booleanvalue_touint32.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns the value of this instance as an equivalent 32-bit unsigned integer.

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function ToUInt32 As UInteger |

| C# |
| --- |
| public override uint ToUInt32() |

| Visual C++ |
| --- |
| public: virtual unsigned int ToUInt32() override |

###### Return Value

UInt32

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

BooleanValue Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_booleanvaluearray__ctor_4.htm language=enus -->
## TOPIC 00132: BooleanValueArray Constructor (IEnumerable)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_booleanvaluearray__ctor_4.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_booleanvaluearray__ctor_4.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

BooleanValueArray

Boolean

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Value As IEnumerable(Of Boolean) _ ) |

| C# |
| --- |
| public BooleanValueArray( IEnumerable<bool> Value ) |

| Visual C++ |
| --- |
| public: BooleanValueArray( IEnumerable<bool>^ Value ) |

###### Parameters

- **Value**
  - Type: System.Collections.Generic.IEnumerableBooleanA list of Boolean values.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

BooleanValueArray Class

BooleanValueArray Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_datavaluearray_1_equals.htm language=enus -->
## TOPIC 00133: DataValueArray.Equals Method (DataResource)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_datavaluearray_1_equals.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_datavaluearray_1_equals.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DataResource

Length

Value

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function Equals ( _ other As DataResource _ ) As Boolean |

| C# |
| --- |
| public override bool Equals( DataResource other ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( DataResource^ other ) override |

###### Parameters

- **other**
  - Type: NationalInstruments.VeriStand.Data.DataResourceThe data resource to compare to this instance.

###### Return Value

true

True

other

false

False

###### Implements

IEquatable(T).Equals(T)

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DataValueArray(T) Class

Equals Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_datavaluearray__ctor.htm language=enus -->
## TOPIC 00134: DataValueArray Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_datavaluearray__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_datavaluearray__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DataValueArray

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New |

| C# |
| --- |
| public DataValueArray() |

| Visual C++ |
| --- |
| public: DataValueArray() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DataValueArray Class

DataValueArray Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_datavaluearray_getdatavaluearrayoftype.htm language=enus -->
## TOPIC 00135: DataValueArray.GetDataValueArrayOfType Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_datavaluearray_getdatavaluearrayoftype.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_datavaluearray_getdatavaluearrayoftype.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns a data value array object of the specified data type.

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared Function GetDataValueArrayOfType ( _ ChildType As DataType _ ) As DataValueArray |

| C# |
| --- |
| public static DataValueArray GetDataValueArrayOfType( DataType ChildType ) |

| Visual C++ |
| --- |
| public: static DataValueArray^ GetDataValueArrayOfType( DataType ChildType ) |

###### Parameters

- **ChildType**
  - Type: NationalInstruments.VeriStand.Data.DataTypeThe data type of the object to return, as an enumeration of DataType.

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DataValueArray Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_datavaluearray_getvalues.htm language=enus -->
## TOPIC 00136: DataValueArray.GetValues Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_datavaluearray_getvalues.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_datavaluearray_getvalues.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DataValueArray

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public MustOverride Function GetValues As ScalarDataValue() |

| C# |
| --- |
| public abstract ScalarDataValue[] GetValues() |

| Visual C++ |
| --- |
| public: virtual array<ScalarDataValue^>^ GetValues() abstract |

###### Return Value

DataValueArray

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DataValueArray Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_datavaluearray_isequalto_1.htm language=enus -->
## TOPIC 00137: DataValueArray.IsEqualTo Method (ScalarDataValue)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_datavaluearray_isequalto_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_datavaluearray_isequalto_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DataValueArray

ScalarDataValue

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function IsEqualTo ( _ Value As ScalarDataValue _ ) As Boolean |

| C# |
| --- |
| public bool IsEqualTo( ScalarDataValue Value ) |

| Visual C++ |
| --- |
| public: bool IsEqualTo( ScalarDataValue^ Value ) |

###### Parameters

- **Value**
  - Type: NationalInstruments.VeriStand.Data.ScalarDataValueThe scalar value to compare to each value in the array.

###### Return Value

true

True

Value

false

False

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DataValueArray Class

IsEqualTo Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_datavaluearray_isgreaterthan.htm language=enus -->
## TOPIC 00138: DataValueArray.IsGreaterThan Method (DataValueArray)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_datavaluearray_isgreaterthan.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_datavaluearray_isgreaterthan.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DataValueArray

DataValueArray

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function IsGreaterThan ( _ Value As DataValueArray _ ) As Boolean |

| C# |
| --- |
| public bool IsGreaterThan( DataValueArray Value ) |

| Visual C++ |
| --- |
| public: bool IsGreaterThan( DataValueArray^ Value ) |

###### Parameters

- **Value**
  - Type: NationalInstruments.VeriStand.Data.DataValueArrayThe array to compare to the current DataValueArray.

###### Return Value

true

True

DataValueArray

Value

false

False

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DataValueArray Class

IsGreaterThan Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_doublevalue_toint64.htm language=enus -->
## TOPIC 00139: DoubleValue.ToInt64 Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_doublevalue_toint64.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_doublevalue_toint64.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns the value of this instance as an equivalent 64-bit signed integer.

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function ToInt64 As Long |

| C# |
| --- |
| public override long ToInt64() |

| Visual C++ |
| --- |
| public: virtual long long ToInt64() override |

###### Return Value

Int64

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DoubleValue Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_doublevalue_touint64.htm language=enus -->
## TOPIC 00140: DoubleValue.ToUInt64 Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_doublevalue_touint64.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_doublevalue_touint64.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns the value of this instance as an equivalent 64-bit unsigned integer.

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function ToUInt64 As ULong |

| C# |
| --- |
| public override ulong ToUInt64() |

| Visual C++ |
| --- |
| public: virtual unsigned long long ToUInt64() override |

###### Return Value

UInt64

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DoubleValue Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_i32value__ctor_2.htm language=enus -->
## TOPIC 00141: I32Value Constructor (Int32)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_i32value__ctor_2.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_i32value__ctor_2.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

I32Value

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Value As Integer _ ) |

| C# |
| --- |
| public I32Value( int Value ) |

| Visual C++ |
| --- |
| public: I32Value( int Value ) |

###### Parameters

- **Value**
  - Type: System.Int32 The value of the 32-bit signed integer.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

I32Value Class

I32Value Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_i32value_equals.htm language=enus -->
## TOPIC 00142: I32Value.Equals Method (DataResource)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_i32value_equals.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_i32value_equals.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DataResource

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function Equals ( _ other As DataResource _ ) As Boolean |

| C# |
| --- |
| public override bool Equals( DataResource other ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( DataResource^ other ) override |

###### Parameters

- **other**
  - Type: NationalInstruments.VeriStand.Data.DataResourceThe data resource to compare to this instance.

###### Return Value

true

True

other

I32Value

false

False

###### Implements

IEquatable(T).Equals(T)

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

I32Value Class

Equals Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_i32value_todouble.htm language=enus -->
## TOPIC 00143: I32Value.ToDouble Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_i32value_todouble.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_i32value_todouble.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns the value of this instance as a double-precision floating point number.

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function ToDouble As Double |

| C# |
| --- |
| public override double ToDouble() |

| Visual C++ |
| --- |
| public: virtual double ToDouble() override |

###### Return Value

Double

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

I32Value Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_i32value_toint32.htm language=enus -->
## TOPIC 00144: I32Value.ToInt32 Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_i32value_toint32.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_i32value_toint32.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns the value of this instance as an equivalent 32-bit signed integer.

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function ToInt32 As Integer |

| C# |
| --- |
| public override int ToInt32() |

| Visual C++ |
| --- |
| public: virtual int ToInt32() override |

###### Return Value

Int32

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

I32Value Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_i32valuearray__ctor_2.htm language=enus -->
## TOPIC 00145: I32ValueArray Constructor (I32ValueArray)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_i32valuearray__ctor_2.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_i32valuearray__ctor_2.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

I32ValueArray

I32ValueArray

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Node As I32ValueArray _ ) |

| C# |
| --- |
| public I32ValueArray( I32ValueArray Node ) |

| Visual C++ |
| --- |
| public: I32ValueArray( I32ValueArray^ Node ) |

###### Parameters

- **Node**
  - Type: NationalInstruments.VeriStand.Data.I32ValueArrayThe instance of I32ValueArray to copy.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

I32ValueArray Class

I32ValueArray Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_i32valuearray__ctor_3.htm language=enus -->
## TOPIC 00146: I32ValueArray Constructor (IEnumerable)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_i32valuearray__ctor_3.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_i32valuearray__ctor_3.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

I32ValueArray

Int32

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Value As IEnumerable(Of Integer) _ ) |

| C# |
| --- |
| public I32ValueArray( IEnumerable<int> Value ) |

| Visual C++ |
| --- |
| public: I32ValueArray( IEnumerable<int>^ Value ) |

###### Parameters

- **Value**
  - Type: System.Collections.Generic.IEnumerableInt32A list of 32-bit signed integers.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

I32ValueArray Class

I32ValueArray Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_i32valuearray__ctor_4.htm language=enus -->
## TOPIC 00147: I32ValueArray Constructor (Int32[])

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_i32valuearray__ctor_4.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_i32valuearray__ctor_4.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

I32ValueArray

Int32

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Value As Integer() _ ) |

| C# |
| --- |
| public I32ValueArray( int[] Value ) |

| Visual C++ |
| --- |
| public: I32ValueArray( array<int>^ Value ) |

###### Parameters

- **Value**
  - Type: System.Int32 An array of 32-bit signed integers.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

I32ValueArray Class

I32ValueArray Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_i64value_compareto.htm language=enus -->
## TOPIC 00148: I64Value.CompareTo Method (ScalarDataValue)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_i64value_compareto.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_i64value_compareto.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Compares this instance to a specified object and returns an integer that indicates their relationship to each other.

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function CompareTo ( _ other As ScalarDataValue _ ) As Integer |

| C# |
| --- |
| public override int CompareTo( ScalarDataValue other ) |

| Visual C++ |
| --- |
| public: virtual int CompareTo( ScalarDataValue^ other ) override |

###### Parameters

- **other**
  - Type: NationalInstruments.VeriStand.Data.ScalarDataValueThe object to compare to this instance.

###### Return Value

other

| Condition | Return Value |
| --- | --- |
| Less than zero | This instance is less than other. |
| Zero | This instance and other are equal. |
| Greater than zero | This instance is greater than other. |

###### Implements

IComparable(T).CompareTo(T)

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

I64Value Class

CompareTo Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_i64value_setbytes.htm language=enus -->
## TOPIC 00149: I64Value.SetBytes Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_i64value_setbytes.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_i64value_setbytes.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

I64Value

Bytes

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Sub SetBytes ( _ Bytes As Byte() _ ) |

| C# |
| --- |
| public override void SetBytes( byte[] Bytes ) |

| Visual C++ |
| --- |
| public: virtual void SetBytes( array<unsigned char>^ Bytes ) override |

###### Parameters

- **Bytes**
  - Type: System.Byte An array of bytes.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

I64Value

Bytes[0]

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

I64Value Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_i64value_todouble.htm language=enus -->
## TOPIC 00150: I64Value.ToDouble Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_i64value_todouble.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_i64value_todouble.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns the value of this instance as a double-precision floating point number.

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function ToDouble As Double |

| C# |
| --- |
| public override double ToDouble() |

| Visual C++ |
| --- |
| public: virtual double ToDouble() override |

###### Return Value

Double

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

I64Value Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_i64value_toint64.htm language=enus -->
## TOPIC 00151: I64Value.ToInt64 Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_i64value_toint64.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_i64value_toint64.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns the value of this instance as an equivalent 64-bit signed integer.

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function ToInt64 As Long |

| C# |
| --- |
| public override long ToInt64() |

| Visual C++ |
| --- |
| public: virtual long long ToInt64() override |

###### Return Value

Int64

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

I64Value Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_importeddoublevaluearray__ctor_1.htm language=enus -->
## TOPIC 00152: ImportedDoubleValueArray Constructor (ImportedDoubleValueArray)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_importeddoublevaluearray__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_importeddoublevaluearray__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

ImportedDoubleValueArray

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ other As ImportedDoubleValueArray _ ) |

| C# |
| --- |
| public ImportedDoubleValueArray( ImportedDoubleValueArray other ) |

| Visual C++ |
| --- |
| public: ImportedDoubleValueArray( ImportedDoubleValueArray^ other ) |

###### Parameters

- **other**
  - Type: NationalInstruments.VeriStand.Data.ImportedDoubleValueArrayThe instance of ImportedDoubleValueArray to copy.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ImportedDoubleValueArray Class

ImportedDoubleValueArray Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_importeddoublevaluearray__ctor_2.htm language=enus -->
## TOPIC 00153: ImportedDoubleValueArray Constructor (String, String, String, UInt64, UInt64)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_importeddoublevaluearray__ctor_2.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_importeddoublevaluearray__ctor_2.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

ImportedDoubleValueArray

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ filePath As String, _ channelGroup As String, _ channel As String, _ importLength As ULong, _ importOffset As ULong _ ) |

| C# |
| --- |
| public ImportedDoubleValueArray( string filePath, string channelGroup, string channel, ulong importLength, ulong importOffset ) |

| Visual C++ |
| --- |
| public: ImportedDoubleValueArray( String^ filePath, String^ channelGroup, String^ channel, unsigned long long importLength, unsigned long long importOffset ) |

###### Parameters

- **filePath**
  - Type: System.StringThe path of the file from which to import values.

- **channelGroup**
  - Type: System.StringThe name of the group in the import file that owns the channel.

- **channel**
  - Type: System.StringThe name of the channel in the import file that contains data you want to import.

- **importLength**
  - Type: System.UInt64The number of samples to import, starting at the importOffset of the first sample you want to import.

- **importOffset**
  - Type: System.UInt64The index of the first sample you want to import.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ImportedDoubleValueArray Class

ImportedDoubleValueArray Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_importeddoublevaluearray_tostring.htm language=enus -->
## TOPIC 00154: ImportedDoubleValueArray.ToString Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_importeddoublevaluearray_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_importeddoublevaluearray_tostring.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns a string representation of the channel name and channel group name.

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function ToString As String |

| C# |
| --- |
| public override string ToString() |

| Visual C++ |
| --- |
| public: virtual String^ ToString() override |

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ImportedDoubleValueArray Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_scalardatavalue_todouble.htm language=enus -->
## TOPIC 00155: ScalarDataValue.ToDouble Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_scalardatavalue_todouble.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_scalardatavalue_todouble.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns the value of this instance as a double-precision floating point number. This is an abstract declaration only. Derived classes must implement the correct ToDouble method for that class.

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public MustOverride Function ToDouble As Double |

| C# |
| --- |
| public abstract double ToDouble() |

| Visual C++ |
| --- |
| public: virtual double ToDouble() abstract |

###### Return Value

Double

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ScalarDataValue Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_systemdefinitionchannelresource__ctor.htm language=enus -->
## TOPIC 00156: SystemDefinitionChannelResource Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_systemdefinitionchannelresource__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_systemdefinitionchannelresource__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

SystemDefinitionChannelResource

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New |

| C# |
| --- |
| public SystemDefinitionChannelResource() |

| Visual C++ |
| --- |
| public: SystemDefinitionChannelResource() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SystemDefinitionChannelResource Class

SystemDefinitionChannelResource Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_systemdefinitionchannelresource_equals.htm language=enus -->
## TOPIC 00157: SystemDefinitionChannelResource.Equals Method (DataResource)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_systemdefinitionchannelresource_equals.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_systemdefinitionchannelresource_equals.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DataResource

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function Equals ( _ other As DataResource _ ) As Boolean |

| C# |
| --- |
| public override bool Equals( DataResource other ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( DataResource^ other ) override |

###### Parameters

- **other**
  - Type: NationalInstruments.VeriStand.Data.DataResourceThe data resource to compare to this instance.

###### Return Value

true

True

other

SystemDefinitionChannelResource

false

False

###### Implements

IEquatable(T).Equals(T)

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SystemDefinitionChannelResource Class

Equals Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_systemdefinitionchannelresource_gethashcode.htm language=enus -->
## TOPIC 00158: SystemDefinitionChannelResource.GetHashCode Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_systemdefinitionchannelresource_gethashcode.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_systemdefinitionchannelresource_gethashcode.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

SystemDefinitionChannelResource

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function GetHashCode As Integer |

| C# |
| --- |
| public override int GetHashCode() |

| Visual C++ |
| --- |
| public: virtual int GetHashCode() override |

###### Return Value

SystemDefinitionChannelResource

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

Object.GetHashCode

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SystemDefinitionChannelResource Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_systemdefinitionchannelresource_tostring.htm language=enus -->
## TOPIC 00159: SystemDefinitionChannelResource.ToString Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_systemdefinitionchannelresource_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_systemdefinitionchannelresource_tostring.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns a string representation of the channel.

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function ToString As String |

| C# |
| --- |
| public override string ToString() |

| Visual C++ |
| --- |
| public: virtual String^ ToString() override |

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SystemDefinitionChannelResource Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_u32value_getbytes.htm language=enus -->
## TOPIC 00160: U32Value.GetBytes Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_u32value_getbytes.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_u32value_getbytes.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns the 32-bit unsigned integer as an array of bytes.

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function GetBytes As Byte() |

| C# |
| --- |
| public override byte[] GetBytes() |

| Visual C++ |
| --- |
| public: virtual array<unsigned char>^ GetBytes() override |

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

U32Value Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_u32value_setbytes.htm language=enus -->
## TOPIC 00161: U32Value.SetBytes Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_u32value_setbytes.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_u32value_setbytes.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

U32Value

Bytes

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Sub SetBytes ( _ Bytes As Byte() _ ) |

| C# |
| --- |
| public override void SetBytes( byte[] Bytes ) |

| Visual C++ |
| --- |
| public: virtual void SetBytes( array<unsigned char>^ Bytes ) override |

###### Parameters

- **Bytes**
  - Type: System.Byte An array of bytes.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

U32Value

Bytes[0]

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

U32Value Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_u32value_todouble.htm language=enus -->
## TOPIC 00162: U32Value.ToDouble Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_u32value_todouble.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_u32value_todouble.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns the value of this instance as a double-precision floating point number.

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function ToDouble As Double |

| C# |
| --- |
| public override double ToDouble() |

| Visual C++ |
| --- |
| public: virtual double ToDouble() override |

###### Return Value

Double

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

U32Value Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_u32value_toint64.htm language=enus -->
## TOPIC 00163: U32Value.ToInt64 Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_u32value_toint64.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_u32value_toint64.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns the value of this instance as an equivalent 64-bit signed integer.

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function ToInt64 As Long |

| C# |
| --- |
| public override long ToInt64() |

| Visual C++ |
| --- |
| public: virtual long long ToInt64() override |

###### Return Value

Int64

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

U32Value Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_u32value_tostring.htm language=enus -->
## TOPIC 00164: U32Value.ToString Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_u32value_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_u32value_tostring.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns the value of this instance as an equivalent string.

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function ToString As String |

| C# |
| --- |
| public override string ToString() |

| Visual C++ |
| --- |
| public: virtual String^ ToString() override |

###### Return Value

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

U32Value Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_u32value_touint32.htm language=enus -->
## TOPIC 00165: U32Value.ToUInt32 Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_u32value_touint32.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_u32value_touint32.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns the value of this instance as an equivalent 32-bit unsigned integer.

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function ToUInt32 As UInteger |

| C# |
| --- |
| public override uint ToUInt32() |

| Visual C++ |
| --- |
| public: virtual unsigned int ToUInt32() override |

###### Return Value

UInt32

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

U32Value Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_u32valuearray__ctor.htm language=enus -->
## TOPIC 00166: U32ValueArray Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_u32valuearray__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_u32valuearray__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

U32ValueArray

U32Value

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New |

| C# |
| --- |
| public U32ValueArray() |

| Visual C++ |
| --- |
| public: U32ValueArray() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

U32ValueArray Class

U32ValueArray Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_u32valuearray__ctor_1.htm language=enus -->
## TOPIC 00167: U32ValueArray Constructor (U32Value[])

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_u32valuearray__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_u32valuearray__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

U32ValueArray

U32Value

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Value As U32Value() _ ) |

| C# |
| --- |
| public U32ValueArray( U32Value[] Value ) |

| Visual C++ |
| --- |
| public: U32ValueArray( array<U32Value^>^ Value ) |

###### Parameters

- **Value**
  - Type: NationalInstruments.VeriStand.Data.U32Value An array of U32Value objects.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

U32ValueArray Class

U32ValueArray Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_u32valuearray__ctor_2.htm language=enus -->
## TOPIC 00168: U32ValueArray Constructor (U32ValueArray)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_u32valuearray__ctor_2.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_u32valuearray__ctor_2.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

U32ValueArray

U32ValueArray

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Node As U32ValueArray _ ) |

| C# |
| --- |
| public U32ValueArray( U32ValueArray Node ) |

| Visual C++ |
| --- |
| public: U32ValueArray( U32ValueArray^ Node ) |

###### Parameters

- **Node**
  - Type: NationalInstruments.VeriStand.Data.U32ValueArrayThe instance of U32ValueArray to copy.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

U32ValueArray Class

U32ValueArray Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_u64value__ctor.htm language=enus -->
## TOPIC 00169: U64Value Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_u64value__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_u64value__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

U64Value

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New |

| C# |
| --- |
| public U64Value() |

| Visual C++ |
| --- |
| public: U64Value() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

U64Value Class

U64Value Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_u64value__ctor_2.htm language=enus -->
## TOPIC 00170: U64Value Constructor (UInt64)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_u64value__ctor_2.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_u64value__ctor_2.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

U64Value

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Value As ULong _ ) |

| C# |
| --- |
| public U64Value( ulong Value ) |

| Visual C++ |
| --- |
| public: U64Value( unsigned long long Value ) |

###### Parameters

- **Value**
  - Type: System.UInt64 The value of the 64-bit unsigned integer.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

U64Value Class

U64Value Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_u64value_equals.htm language=enus -->
## TOPIC 00171: U64Value.Equals Method (DataResource)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_u64value_equals.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_u64value_equals.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DataResource

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function Equals ( _ other As DataResource _ ) As Boolean |

| C# |
| --- |
| public override bool Equals( DataResource other ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( DataResource^ other ) override |

###### Parameters

- **other**
  - Type: NationalInstruments.VeriStand.Data.DataResourceThe data resource to compare to this instance.

###### Return Value

true

True

other

U64Value

false

False

###### Implements

IEquatable(T).Equals(T)

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

U64Value Class

Equals Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_u64value_getbytes.htm language=enus -->
## TOPIC 00172: U64Value.GetBytes Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_u64value_getbytes.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_u64value_getbytes.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns the 64-bit unsigned integer as an array of bytes.

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function GetBytes As Byte() |

| C# |
| --- |
| public override byte[] GetBytes() |

| Visual C++ |
| --- |
| public: virtual array<unsigned char>^ GetBytes() override |

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

U64Value Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_u64value_setbytes.htm language=enus -->
## TOPIC 00173: U64Value.SetBytes Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_u64value_setbytes.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_u64value_setbytes.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

U64Value

Bytes

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Sub SetBytes ( _ Bytes As Byte() _ ) |

| C# |
| --- |
| public override void SetBytes( byte[] Bytes ) |

| Visual C++ |
| --- |
| public: virtual void SetBytes( array<unsigned char>^ Bytes ) override |

###### Parameters

- **Bytes**
  - Type: System.Byte An array of bytes.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

U64Value

Bytes[0]

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

U64Value Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_u64value_toboolean.htm language=enus -->
## TOPIC 00174: U64Value.ToBoolean Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_u64value_toboolean.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_u64value_toboolean.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns if this instance is a nonzero value.

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function ToBoolean As Boolean |

| C# |
| --- |
| public override bool ToBoolean() |

| Visual C++ |
| --- |
| public: virtual bool ToBoolean() override |

###### Return Value

true

True

false

False

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

U64Value Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_u64value_touint64.htm language=enus -->
## TOPIC 00175: U64Value.ToUInt64 Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_u64value_touint64.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_u64value_touint64.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns the value of this instance as an equivalent 64-bit unsigned integer.

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function ToUInt64 As ULong |

| C# |
| --- |
| public override ulong ToUInt64() |

| Visual C++ |
| --- |
| public: virtual unsigned long long ToUInt64() override |

###### Return Value

UInt64

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

U64Value Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_u64valuearray__ctor.htm language=enus -->
## TOPIC 00176: U64ValueArray Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_u64valuearray__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_u64valuearray__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

U64ValueArray

U64Value

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New |

| C# |
| --- |
| public U64ValueArray() |

| Visual C++ |
| --- |
| public: U64ValueArray() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

U64ValueArray Class

U64ValueArray Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_u64valuearray__ctor_3.htm language=enus -->
## TOPIC 00177: U64ValueArray Constructor (IEnumerable)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_u64valuearray__ctor_3.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_u64valuearray__ctor_3.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

U64ValueArray

UInt64

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Value As IEnumerable(Of ULong) _ ) |

| C# |
| --- |
| public U64ValueArray( IEnumerable<ulong> Value ) |

| Visual C++ |
| --- |
| public: U64ValueArray( IEnumerable<unsigned long long>^ Value ) |

###### Parameters

- **Value**
  - Type: System.Collections.Generic.IEnumerableUInt64A list of 64-bit unsigned integers.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

U64ValueArray Class

U64ValueArray Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_u64valuearray__ctor_4.htm language=enus -->
## TOPIC 00178: U64ValueArray Constructor (UInt64[])

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_u64valuearray__ctor_4.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_u64valuearray__ctor_4.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

U64ValueArray

UInt64

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Value As ULong() _ ) |

| C# |
| --- |
| public U64ValueArray( ulong[] Value ) |

| Visual C++ |
| --- |
| public: U64ValueArray( array<unsigned long long>^ Value ) |

###### Parameters

- **Value**
  - Type: System.UInt64 An array of 64-bit unsigned integers.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

U64ValueArray Class

U64ValueArray Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_voidvalue__ctor_1.htm language=enus -->
## TOPIC 00179: VoidValue Constructor (VoidValue)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_voidvalue__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_voidvalue__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

VoidValue

VoidValue

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Node As VoidValue _ ) |

| C# |
| --- |
| public VoidValue( VoidValue Node ) |

| Visual C++ |
| --- |
| public: VoidValue( VoidValue^ Node ) |

###### Parameters

- **Node**
  - Type: NationalInstruments.VeriStand.Data.VoidValueThe instance of VoidValue to copy.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

VoidValue Class

VoidValue Overload

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_voidvalue_toboolean.htm language=enus -->
## TOPIC 00180: VoidValue.ToBoolean Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_voidvalue_toboolean.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_voidvalue_toboolean.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

false

False

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function ToBoolean As Boolean |

| C# |
| --- |
| public override bool ToBoolean() |

| Visual C++ |
| --- |
| public: virtual bool ToBoolean() override |

###### Return Value

false

False

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

VoidValue Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_voidvalue_todouble.htm language=enus -->
## TOPIC 00181: VoidValue.ToDouble Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_voidvalue_todouble.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_voidvalue_todouble.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns a a value that is not a number (NaN).

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function ToDouble As Double |

| C# |
| --- |
| public override double ToDouble() |

| Visual C++ |
| --- |
| public: virtual double ToDouble() override |

###### Return Value

Double.NaN

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

VoidValue Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_data_voidvalue_toint64.htm language=enus -->
## TOPIC 00182: VoidValue.ToInt64 Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_data_voidvalue_toint64.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_data_voidvalue_toint64.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns zero as a 64-bit signed integer.

Namespace:

NationalInstruments.VeriStand.Data

Assembly:

NationalInstruments.VeriStand.DataTypes

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function ToInt64 As Long |

| C# |
| --- |
| public override long ToInt64() |

| Visual C++ |
| --- |
| public: virtual long long ToInt64() override |

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

VoidValue Class

NationalInstruments.VeriStand.Data Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_abstractdeclaration_equals_1.htm language=enus -->
## TOPIC 00183: AbstractDeclaration.Equals Method (Object)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_abstractdeclaration_equals_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_abstractdeclaration_equals_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

obj

AbstractDeclaration

AbstractDeclaration

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function Equals ( _ obj As Object _ ) As Boolean |

| C# |
| --- |
| public override bool Equals( Object obj ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( Object^ obj ) override |

###### Parameters

- **obj**
  - Type: System.ObjectThe object to compare with the current AbstractDeclaration.

###### Return Value

true

True

obj

AbstractDeclaration

false

False

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

Object.Equals

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

AbstractDeclaration Class

Equals Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_block_gethashcode.htm language=enus -->
## TOPIC 00184: Block.GetHashCode Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_block_gethashcode.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_block_gethashcode.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Block

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function GetHashCode As Integer |

| C# |
| --- |
| public override int GetHashCode() |

| Visual C++ |
| --- |
| public: virtual int GetHashCode() override |

###### Return Value

Block

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

Object.GetHashCode

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Block Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_cases__ctor.htm language=enus -->
## TOPIC 00185: Cases Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_cases__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_cases__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Cases

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New |

| C# |
| --- |
| public Cases() |

| Visual C++ |
| --- |
| public: Cases() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Cases Class

Cases Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_cases_clearcases.htm language=enus -->
## TOPIC 00186: Cases.ClearCases Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_cases_clearcases.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_cases_clearcases.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Cases

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub ClearCases |

| C# |
| --- |
| public void ClearCases() |

| Visual C++ |
| --- |
| public: void ClearCases() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Cases Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_cases_equals_1.htm language=enus -->
## TOPIC 00187: Cases.Equals Method (Object)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_cases_equals_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_cases_equals_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

obj

Cases

Cases

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function Equals ( _ obj As Object _ ) As Boolean |

| C# |
| --- |
| public override bool Equals( Object obj ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( Object^ obj ) override |

###### Parameters

- **obj**
  - Type: System.ObjectThe object to compare with the current Cases.

###### Return Value

true

True

obj

Cases

false

False

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

Object.Equals

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Cases Class

Equals Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_casestatement__ctor.htm language=enus -->
## TOPIC 00188: CaseStatement Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_casestatement__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_casestatement__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

CaseStatement

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New |

| C# |
| --- |
| public CaseStatement() |

| Visual C++ |
| --- |
| public: CaseStatement() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| A CaseStatement can only exist under the Cases section of a Switch statement, and cannot stand alone. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CaseStatement Class

CaseStatement Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_casestatement__ctor_1.htm language=enus -->
## TOPIC 00189: CaseStatement Constructor (CaseStatement)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_casestatement__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_casestatement__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

CaseStatement

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ node As CaseStatement _ ) |

| C# |
| --- |
| public CaseStatement( CaseStatement node ) |

| Visual C++ |
| --- |
| public: CaseStatement( CaseStatement^ node ) |

###### Parameters

- **node**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.CaseStatementThe instance of CaseStatement to copy.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| A CaseStatement can only exist under the Cases section of a Switch statement, and cannot stand alone. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CaseStatement Class

CaseStatement Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_cleanup__ctor_1.htm language=enus -->
## TOPIC 00190: CleanUp Constructor (CleanUp)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_cleanup__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_cleanup__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

CleanUp

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ node As CleanUp _ ) |

| C# |
| --- |
| public CleanUp( CleanUp node ) |

| Visual C++ |
| --- |
| public: CleanUp( CleanUp^ node ) |

###### Parameters

- **node**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.CleanUpThe instance of CleanUp to copy.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CleanUp Class

CleanUp Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_code_gethashcode.htm language=enus -->
## TOPIC 00191: Code.GetHashCode Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_code_gethashcode.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_code_gethashcode.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Code

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function GetHashCode As Integer |

| C# |
| --- |
| public override int GetHashCode() |

| Visual C++ |
| --- |
| public: virtual int GetHashCode() override |

###### Return Value

Code

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

Object.GetHashCode

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Code Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_codesection__ctor.htm language=enus -->
## TOPIC 00192: CodeSection Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_codesection__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_codesection__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

CodeSection

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Sub New |

| C# |
| --- |
| protected CodeSection() |

| Visual C++ |
| --- |
| protected: CodeSection() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CodeSection Class

CodeSection Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_codesection_equals_1.htm language=enus -->
## TOPIC 00193: CodeSection.Equals Method (Object)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_codesection_equals_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_codesection_equals_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

obj

CodeSection

CodeSection

Body

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function Equals ( _ obj As Object _ ) As Boolean |

| C# |
| --- |
| public override bool Equals( Object obj ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( Object^ obj ) override |

###### Parameters

- **obj**
  - Type: System.ObjectThe object to compare with the current CodeSection object.

###### Return Value

true

True

obj

CodeSection

false

False

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

Object.Equals

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CodeSection Class

Equals Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_compiler_tostring.htm language=enus -->
## TOPIC 00194: Compiler.ToString Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_compiler_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_compiler_tostring.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns a string representation of the current object.

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function ToString As String |

| C# |
| --- |
| public override string ToString() |

| Visual C++ |
| --- |
| public: virtual String^ ToString() override |

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

Object.ToString

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Compiler Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_dowhileloop_equals.htm language=enus -->
## TOPIC 00195: DoWhileLoop.Equals Method (DoWhileLoop)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_dowhileloop_equals.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_dowhileloop_equals.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

other

DoWhileLoop

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function Equals ( _ other As DoWhileLoop _ ) As Boolean |

| C# |
| --- |
| public bool Equals( DoWhileLoop other ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( DoWhileLoop^ other ) sealed |

###### Parameters

- **other**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.DoWhileLoopThe DoWhileLoop object to compare with the current instance.

###### Return Value

true

True

other

false

False

###### Implements

IEquatable(T).Equals(T)

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DoWhileLoop Class

Equals Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_expression__ctor.htm language=enus -->
## TOPIC 00196: Expression Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_expression__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_expression__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Expression

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New |

| C# |
| --- |
| public Expression() |

| Visual C++ |
| --- |
| public: Expression() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

ExpressionString

String.Empty

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Expression Class

Expression Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_expression_equals.htm language=enus -->
## TOPIC 00197: Expression.Equals Method (Expression)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_expression_equals.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_expression_equals.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

other

Expression

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function Equals ( _ other As Expression _ ) As Boolean |

| C# |
| --- |
| public bool Equals( Expression other ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( Expression^ other ) sealed |

###### Parameters

- **other**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.ExpressionThe Expression object to compare with the current instance.

###### Return Value

true

True

other

false

False

###### Implements

IEquatable(T).Equals(T)

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Expression Class

Equals Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_expression_equals_1.htm language=enus -->
## TOPIC 00198: Expression.Equals Method (Statement)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_expression_equals_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_expression_equals_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

other

Expression

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function Equals ( _ other As Statement _ ) As Boolean |

| C# |
| --- |
| public override bool Equals( Statement other ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( Statement^ other ) override |

###### Parameters

- **other**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.StatementThe Expression object to compare with the current instance.

###### Return Value

true

True

other

Expression

false

False

###### Implements

IEquatable(T).Equals(T)

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

Expression

Statement

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Expression Class

Equals Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_foreachloop__ctor_1.htm language=enus -->
## TOPIC 00199: ForEachLoop Constructor (ForEachLoop)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_foreachloop__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_foreachloop__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

ForEachLoop

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ node As ForEachLoop _ ) |

| C# |
| --- |
| public ForEachLoop( ForEachLoop node ) |

| Visual C++ |
| --- |
| public: ForEachLoop( ForEachLoop^ node ) |

###### Parameters

- **node**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.ForEachLoopThe instance of ForEachLoop to copy.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ForEachLoop Class

ForEachLoop Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_foreachloop__ctor_3.htm language=enus -->
## TOPIC 00200: ForEachLoop Constructor (String, Expression, Boolean, Block)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_foreachloop__ctor_3.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_foreachloop__ctor_3.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

ForEachLoop

arrayExpression

body

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ loopVariable As String, _ arrayExpression As Expression, _ autoYield As Boolean, _ body As Block _ ) |

| C# |
| --- |
| public ForEachLoop( string loopVariable, Expression arrayExpression, bool autoYield, Block body ) |

| Visual C++ |
| --- |
| public: ForEachLoop( String^ loopVariable, Expression^ arrayExpression, bool autoYield, Block^ body ) |

###### Parameters

- **loopVariable**
  - Type: System.StringThe identifier for the variable that holds the current value of the array element. For example, i.

- **arrayExpression**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.ExpressionThe array of values that the loop iterates over.

- **autoYield**
  - Type: System.BooleanIf true (True in Visual Basic), specifies that the loop automatically yields control of the CPU to the next task at the end of each iteration.

- **body**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.BlockThe sequence code to execute on each iteration of the loop.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ForEachLoop Class

ForEachLoop Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_foreachloop_equals.htm language=enus -->
## TOPIC 00201: ForEachLoop.Equals Method (ForEachLoop)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_foreachloop_equals.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_foreachloop_equals.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

other

ForEachLoop

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function Equals ( _ other As ForEachLoop _ ) As Boolean |

| C# |
| --- |
| public bool Equals( ForEachLoop other ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( ForEachLoop^ other ) sealed |

###### Parameters

- **other**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.ForEachLoopThe ForEachLoop object to compare with the current instance.

###### Return Value

true

True

other

false

False

###### Implements

IEquatable(T).Equals(T)

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ForEachLoop Class

Equals Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_foreachloop_gethashcode.htm language=enus -->
## TOPIC 00202: ForEachLoop.GetHashCode Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_foreachloop_gethashcode.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_foreachloop_gethashcode.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

ForEachLoop

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function GetHashCode As Integer |

| C# |
| --- |
| public override int GetHashCode() |

| Visual C++ |
| --- |
| public: virtual int GetHashCode() override |

###### Return Value

ForEachLoop

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

Statement.GetHashCode

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ForEachLoop Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_ifelse__ctor.htm language=enus -->
## TOPIC 00203: IfElse Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_ifelse__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_ifelse__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

IfElse

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New |

| C# |
| --- |
| public IfElse() |

| Visual C++ |
| --- |
| public: IfElse() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

TestExpression

Expression

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IfElse Class

IfElse Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_ifelse_equals_1.htm language=enus -->
## TOPIC 00204: IfElse.Equals Method (Statement)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_ifelse_equals_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_ifelse_equals_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

other

IfElse

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function Equals ( _ other As Statement _ ) As Boolean |

| C# |
| --- |
| public override bool Equals( Statement other ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( Statement^ other ) override |

###### Parameters

- **other**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.StatementThe Statement object to compare with the current instance.

###### Return Value

true

True

other

IfElse

false

False

###### Implements

IEquatable(T).Equals(T)

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

IfElse

Statement

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

IfElse Class

Equals Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_localvariables_equals.htm language=enus -->
## TOPIC 00205: LocalVariables.Equals Method (LocalVariables)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_localvariables_equals.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_localvariables_equals.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

other

LocalVariables

Variables()

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function Equals ( _ other As LocalVariables _ ) As Boolean |

| C# |
| --- |
| public bool Equals( LocalVariables other ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( LocalVariables^ other ) sealed |

###### Parameters

- **other**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.LocalVariablesThe LocalVariables object to compare with the current instance.

###### Return Value

true

True

other

false

False

###### Implements

IEquatable(T).Equals(T)

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

LocalVariables Class

Equals Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_localvariables_equals_1.htm language=enus -->
## TOPIC 00206: LocalVariables.Equals Method (Object)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_localvariables_equals_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_localvariables_equals_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

obj

LocalVariables

LocalVariables

Variables()

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function Equals ( _ obj As Object _ ) As Boolean |

| C# |
| --- |
| public override bool Equals( Object obj ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( Object^ obj ) override |

###### Parameters

- **obj**
  - Type: System.ObjectThe object to compare with the current LocalVariables object.

###### Return Value

true

True

obj

LocalVariables

false

False

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

Object.Equals

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

LocalVariables Class

Equals Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_localvariables_gethashcode.htm language=enus -->
## TOPIC 00207: LocalVariables.GetHashCode Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_localvariables_gethashcode.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_localvariables_gethashcode.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

LocalVariables

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function GetHashCode As Integer |

| C# |
| --- |
| public override int GetHashCode() |

| Visual C++ |
| --- |
| public: virtual int GetHashCode() override |

###### Return Value

LocalVariables

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

Object.GetHashCode

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

LocalVariables Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_main__ctor.htm language=enus -->
## TOPIC 00208: Main Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_main__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_main__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Main

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New |

| C# |
| --- |
| public Main() |

| Visual C++ |
| --- |
| public: Main() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Main Class

Main Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_main__ctor_1.htm language=enus -->
## TOPIC 00209: Main Constructor (Main)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_main__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_main__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Main

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ node As Main _ ) |

| C# |
| --- |
| public Main( Main node ) |

| Visual C++ |
| --- |
| public: Main( Main^ node ) |

###### Parameters

- **node**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.MainThe instance of Main to copy.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Main Class

Main Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_multilinestringattribute__ctor.htm language=enus -->
## TOPIC 00210: MultilineStringAttribute Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_multilinestringattribute__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_multilinestringattribute__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

MultilineStringAttribute

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New |

| C# |
| --- |
| public MultilineStringAttribute() |

| Visual C++ |
| --- |
| public: MultilineStringAttribute() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

MultilineStringAttribute Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_multitask__ctor_2.htm language=enus -->
## TOPIC 00211: Multitask Constructor (Task[])

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_multitask__ctor_2.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_multitask__ctor_2.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Multitask

tasks

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ tasks As Task() _ ) |

| C# |
| --- |
| public Multitask( Task[] tasks ) |

| Visual C++ |
| --- |
| public: Multitask( array<Task^>^ tasks ) |

###### Parameters

- **tasks**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.Task The set of child tasks to iteratively execute in the same time step.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Multitask Class

Multitask Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_multitask_cleartasks.htm language=enus -->
## TOPIC 00212: Multitask.ClearTasks Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_multitask_cleartasks.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_multitask_cleartasks.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Multitask

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub ClearTasks |

| C# |
| --- |
| public void ClearTasks() |

| Visual C++ |
| --- |
| public: void ClearTasks() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Multitask Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_multitask_equals.htm language=enus -->
## TOPIC 00213: Multitask.Equals Method (Multitask)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_multitask_equals.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_multitask_equals.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

other

Multitask

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function Equals ( _ other As Multitask _ ) As Boolean |

| C# |
| --- |
| public bool Equals( Multitask other ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( Multitask^ other ) sealed |

###### Parameters

- **other**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.MultitaskThe Multitask object to compare with the current instance.

###### Return Value

true

True

other

false

False

###### Implements

IEquatable(T).Equals(T)

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Multitask Class

Equals Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_multitask_equals_1.htm language=enus -->
## TOPIC 00214: Multitask.Equals Method (Statement)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_multitask_equals_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_multitask_equals_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

other

Multitask

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function Equals ( _ other As Statement _ ) As Boolean |

| C# |
| --- |
| public override bool Equals( Statement other ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( Statement^ other ) override |

###### Parameters

- **other**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.StatementThe Multitask object to compare with the current instance.

###### Return Value

true

True

other

Multitask

false

False

###### Implements

IEquatable(T).Equals(T)

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

Multitask

Statement

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Multitask Class

Equals Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_multitask_gethashcode.htm language=enus -->
## TOPIC 00215: Multitask.GetHashCode Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_multitask_gethashcode.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_multitask_gethashcode.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Multitask

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function GetHashCode As Integer |

| C# |
| --- |
| public override int GetHashCode() |

| Visual C++ |
| --- |
| public: virtual int GetHashCode() override |

###### Return Value

Multitask

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

Statement.GetHashCode

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Multitask Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_parameterdeclaration__ctor_1.htm language=enus -->
## TOPIC 00216: ParameterDeclaration Constructor (ParameterDeclaration)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_parameterdeclaration__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_parameterdeclaration__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

ParameterDeclaration

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ node As ParameterDeclaration _ ) |

| C# |
| --- |
| public ParameterDeclaration( ParameterDeclaration node ) |

| Visual C++ |
| --- |
| public: ParameterDeclaration( ParameterDeclaration^ node ) |

###### Parameters

- **node**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.ParameterDeclarationThe instance of ParameterDeclaration to copy.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ParameterDeclaration Class

ParameterDeclaration Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_parameterdeclaration__ctor_2.htm language=enus -->
## TOPIC 00217: ParameterDeclaration Constructor (String, DataValue, EvaluationMethod)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_parameterdeclaration__ctor_2.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_parameterdeclaration__ctor_2.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

ParameterDeclaration

identifier

defaultValue

evaluationMethod

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ identifier As String, _ defaultValue As DataValue, _ evaluationMethod As EvaluationMethod _ ) |

| C# |
| --- |
| public ParameterDeclaration( string identifier, DataValue defaultValue, EvaluationMethod evaluationMethod ) |

| Visual C++ |
| --- |
| public: ParameterDeclaration( String^ identifier, DataValue^ defaultValue, EvaluationMethod evaluationMethod ) |

###### Parameters

- **identifier**
  - Type: System.StringThe name of the parameter.

- **defaultValue**
  - Type: NationalInstruments.VeriStand.Data.DataValueThe default value and data type of the parameter.

- **evaluationMethod**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.EvaluationMethodThe evaluation method for the parameter value. If the parameter value is passed in by reference, the sequence directly reads or writes the value of the calling sequence, rather than a copy of that value.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ParameterDeclaration Class

ParameterDeclaration Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_parameterdeclaration_equals.htm language=enus -->
## TOPIC 00218: ParameterDeclaration.Equals Method (ParameterDeclaration)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_parameterdeclaration_equals.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_parameterdeclaration_equals.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

other

ParameterDeclaration

EvaluationMethod

DefaultAssignment

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function Equals ( _ other As ParameterDeclaration _ ) As Boolean |

| C# |
| --- |
| public bool Equals( ParameterDeclaration other ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( ParameterDeclaration^ other ) sealed |

###### Parameters

- **other**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.ParameterDeclarationThe ParameterDeclaration object to compare with the current instance.

###### Return Value

true

True

other

false

False

###### Implements

IEquatable(T).Equals(T)

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ParameterDeclaration Class

Equals Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_parameterdeclaration_equals_1.htm language=enus -->
## TOPIC 00219: ParameterDeclaration.Equals Method (Object)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_parameterdeclaration_equals_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_parameterdeclaration_equals_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

obj

ParameterDeclaration

ParameterDeclaration

EvaluationMethod

DefaultAssignment

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function Equals ( _ obj As Object _ ) As Boolean |

| C# |
| --- |
| public override bool Equals( Object obj ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( Object^ obj ) override |

###### Parameters

- **obj**
  - Type: System.ObjectThe object to compare with the current ParameterDeclaration.

###### Return Value

true

True

obj

ParameterDeclaration

false

False

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

Object.Equals

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ParameterDeclaration Class

Equals Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_parameters_addparameter.htm language=enus -->
## TOPIC 00220: Parameters.AddParameter Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_parameters_addparameter.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_parameters_addparameter.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

parameter

Parameters

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub AddParameter ( _ parameter As ParameterDeclaration _ ) |

| C# |
| --- |
| public void AddParameter( ParameterDeclaration parameter ) |

| Visual C++ |
| --- |
| public: void AddParameter( ParameterDeclaration^ parameter ) |

###### Parameters

- **parameter**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.ParameterDeclarationThe parameter to add.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Parameters Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_reference_equals_1.htm language=enus -->
## TOPIC 00221: Reference.Equals Method (Object)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_reference_equals_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_reference_equals_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

obj

Reference

Reference

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function Equals ( _ obj As Object _ ) As Boolean |

| C# |
| --- |
| public override bool Equals( Object obj ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( Object^ obj ) override |

###### Parameters

- **obj**
  - Type: System.ObjectThe object to compare with the current reference.

###### Return Value

true

True

obj

Reference

false

False

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

Object.Equals

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Reference Class

Equals Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_references_equals_1.htm language=enus -->
## TOPIC 00222: References.Equals Method (Object)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_references_equals_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_references_equals_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

obj

References

References

Setup

Main

CleanUp

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function Equals ( _ obj As Object _ ) As Boolean |

| C# |
| --- |
| public override bool Equals( Object obj ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( Object^ obj ) override |

###### Parameters

- **obj**
  - Type: System.ObjectThe object to compare with the current References object.

###### Return Value

true

True

obj

References

false

False

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

Object.Equals

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

References Class

Equals Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_statement__ctor_1.htm language=enus -->
## TOPIC 00223: Statement Constructor (Statement)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_statement__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_statement__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Statement

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Sub New ( _ node As Statement _ ) |

| C# |
| --- |
| protected Statement( Statement node ) |

| Visual C++ |
| --- |
| protected: Statement( Statement^ node ) |

###### Parameters

- **node**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.StatementThe instance of Statement to copy.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

This constructor is protected.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Statement Class

Statement Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_stimulusprofilecompilationexception__ctor.htm language=enus -->
## TOPIC 00224: StimulusProfileCompilationException Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_stimulusprofilecompilationexception__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_stimulusprofilecompilationexception__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

StimulusProfileCompilationException

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New |

| C# |
| --- |
| public StimulusProfileCompilationException() |

| Visual C++ |
| --- |
| public: StimulusProfileCompilationException() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

StimulusProfileCompilationException Class

StimulusProfileCompilationException Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_stimulusprofilecompilationexception__ctor_1.htm language=enus -->
## TOPIC 00225: StimulusProfileCompilationException Constructor (CompilationEvent[])

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_stimulusprofilecompilationexception__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_stimulusprofilecompilationexception__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

StimulusProfileCompilationException

events

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ events As CompilationEvent() _ ) |

| C# |
| --- |
| public StimulusProfileCompilationException( CompilationEvent[] events ) |

| Visual C++ |
| --- |
| public: StimulusProfileCompilationException( array<CompilationEvent^>^ events ) |

###### Parameters

- **events**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.CompilationEvent The events to recognize as compilation errors.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

StimulusProfileCompilationException Class

StimulusProfileCompilationException Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_stoptask__ctor_1.htm language=enus -->
## TOPIC 00226: StopTask Constructor (StopTask)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_stoptask__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_stoptask__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

StopTask

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ node As StopTask _ ) |

| C# |
| --- |
| public StopTask( StopTask node ) |

| Visual C++ |
| --- |
| public: StopTask( StopTask^ node ) |

###### Parameters

- **node**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.StopTaskThe instance of StopTask to copy.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

StopTask Class

StopTask Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_variables_equals_1.htm language=enus -->
## TOPIC 00227: Variables.Equals Method (Object)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_variables_equals_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_variables_equals_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

obj

Variables

Variables

LocalVariables

Parameters

ReturnType

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function Equals ( _ obj As Object _ ) As Boolean |

| C# |
| --- |
| public override bool Equals( Object obj ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( Object^ obj ) override |

###### Parameters

- **obj**
  - Type: System.ObjectThe object to compare with the current Variables object.

###### Return Value

true

True

obj

Variables

false

False

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

Object.Equals

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Variables Class

Equals Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_whileloop__ctor.htm language=enus -->
## TOPIC 00228: WhileLoop Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_whileloop__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_whileloop__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

WhileLoop

LoopTest

false

False

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New |

| C# |
| --- |
| public WhileLoop() |

| Visual C++ |
| --- |
| public: WhileLoop() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

WhileLoop Class

WhileLoop Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_whileloop__ctor_1.htm language=enus -->
## TOPIC 00229: WhileLoop Constructor (Expression, Boolean)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_whileloop__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_whileloop__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

WhileLoop

loopTest

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ loopTest As Expression, _ autoYield As Boolean _ ) |

| C# |
| --- |
| public WhileLoop( Expression loopTest, bool autoYield ) |

| Visual C++ |
| --- |
| public: WhileLoop( Expression^ loopTest, bool autoYield ) |

###### Parameters

- **loopTest**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.ExpressionThe Boolean expression that is evaluated to determine whether to execute the loop. The loop executes as long as this expression evaluates to true (True in Visual Basic).

- **autoYield**
  - Type: System.BooleanIf true (True in Visual Basic), specifies that the loop automatically yields control of the CPU to the next task at the end of each iteration.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

WhileLoop Class

WhileLoop Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_whileloop__ctor_3.htm language=enus -->
## TOPIC 00230: WhileLoop Constructor (WhileLoop)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_whileloop__ctor_3.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_whileloop__ctor_3.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

WhileLoop

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ node As WhileLoop _ ) |

| C# |
| --- |
| public WhileLoop( WhileLoop node ) |

| Visual C++ |
| --- |
| public: WhileLoop( WhileLoop^ node ) |

###### Parameters

- **node**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.WhileLoopThe instance of WhileLoop to copy.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

WhileLoop Class

WhileLoop Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_whileloop_equals_1.htm language=enus -->
## TOPIC 00231: WhileLoop.Equals Method (WhileLoop)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_whileloop_equals_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_whileloop_equals_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

other

WhileLoop

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function Equals ( _ other As WhileLoop _ ) As Boolean |

| C# |
| --- |
| public bool Equals( WhileLoop other ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( WhileLoop^ other ) sealed |

###### Parameters

- **other**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.WhileLoopThe WhileLoop object to compare with the current instance.

###### Return Value

true

True

other

false

False

###### Implements

IEquatable(T).Equals(T)

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

WhileLoop Class

Equals Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_yield__ctor.htm language=enus -->
## TOPIC 00232: Yield Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_yield__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_yield__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Yield

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New |

| C# |
| --- |
| public Yield() |

| Visual C++ |
| --- |
| public: Yield() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Yield Class

Yield Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_yield__ctor_1.htm language=enus -->
## TOPIC 00233: Yield Constructor (Yield)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_yield__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_yield__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Yield

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ node As Yield _ ) |

| C# |
| --- |
| public Yield( Yield node ) |

| Visual C++ |
| --- |
| public: Yield( Yield^ node ) |

###### Parameters

- **node**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.YieldThe instance of Yield to copy.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Yield Class

Yield Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_yield_equals.htm language=enus -->
## TOPIC 00234: Yield.Equals Method (Statement)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_yield_equals.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_yield_equals.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

other

Yield

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function Equals ( _ other As Statement _ ) As Boolean |

| C# |
| --- |
| public override bool Equals( Statement other ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( Statement^ other ) override |

###### Parameters

- **other**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.StatementThe Statement object to compare with the current instance.

###### Return Value

true

True

other

Yield

false

False

###### Implements

IEquatable(T).Equals(T)

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

Yield

Statement

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Yield Class

Equals Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_yield_equals_1.htm language=enus -->
## TOPIC 00235: Yield.Equals Method (Yield)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_yield_equals_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_yield_equals_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

other

Yield

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function Equals ( _ other As Yield _ ) As Boolean |

| C# |
| --- |
| public bool Equals( Yield other ) |

| Visual C++ |
| --- |
| public: virtual bool Equals( Yield^ other ) sealed |

###### Parameters

- **other**
  - Type: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.YieldThe Yield object to compare with the current instance.

###### Return Value

true

True

other

false

False

###### Implements

IEquatable(T).Equals(T)

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Yield Class

Equals Overload

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_yield_gethashcode.htm language=enus -->
## TOPIC 00236: Yield.GetHashCode Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_yield_gethashcode.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_realtimesequencedefinitionapi_yield_gethashcode.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Yield

Namespace:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function GetHashCode As Integer |

| C# |
| --- |
| public override int GetHashCode() |

| Visual C++ |
| --- |
| public: virtual int GetHashCode() override |

###### Return Value

Yield

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

Statement.GetHashCode

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Yield Class

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_actionstep__ctor.htm language=enus -->
## TOPIC 00237: ActionStep Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_actionstep__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_actionstep__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

ActionStep

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Sub New |

| C# |
| --- |
| protected ActionStep() |

| Visual C++ |
| --- |
| protected: ActionStep() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

This constructor is protected.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ActionStep Class

ActionStep Overload

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_actionstep__ctor_1.htm language=enus -->
## TOPIC 00238: ActionStep Constructor (ActionStep)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_actionstep__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_actionstep__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

ActionStep

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Sub New ( _ node As ActionStep _ ) |

| C# |
| --- |
| protected ActionStep( ActionStep node ) |

| Visual C++ |
| --- |
| protected: ActionStep( ActionStep^ node ) |

###### Parameters

- **node**
  - Type: NationalInstruments.VeriStand.StimulusProfileDefinitionApi.ActionStepThe instance of ActionStep to copy.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

This constructor is protected.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ActionStep Class

ActionStep Overload

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_actionstep_checkforerrors.htm language=enus -->
## TOPIC 00239: ActionStep.CheckForErrors Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_actionstep_checkforerrors.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_actionstep_checkforerrors.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration.

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overridable Function CheckForErrors As CompilationEvent() |

| C# |
| --- |
| public virtual CompilationEvent[] CheckForErrors() |

| Visual C++ |
| --- |
| public: virtual array<CompilationEvent^>^ CheckForErrors() |

###### Return Value

CompilationEvent

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ActionStep Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_alwayspassevaluation__ctor_1.htm language=enus -->
## TOPIC 00240: AlwaysPassEvaluation Constructor (AlwaysPassEvaluation)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_alwayspassevaluation__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_alwayspassevaluation__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

AlwaysPassEvaluation

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ node As AlwaysPassEvaluation _ ) |

| C# |
| --- |
| public AlwaysPassEvaluation( AlwaysPassEvaluation node ) |

| Visual C++ |
| --- |
| public: AlwaysPassEvaluation( AlwaysPassEvaluation^ node ) |

###### Parameters

- **node**
  - Type: NationalInstruments.VeriStand.StimulusProfileDefinitionApi.AlwaysPassEvaluationThe instance of AlwaysPassEvaluation to copy.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

AlwaysPassEvaluation Class

AlwaysPassEvaluation Overload

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_cleanupstepgroup__ctor.htm language=enus -->
## TOPIC 00241: CleanupStepGroup Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_cleanupstepgroup__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_cleanupstepgroup__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

CleanupStepGroup

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New |

| C# |
| --- |
| public CleanupStepGroup() |

| Visual C++ |
| --- |
| public: CleanupStepGroup() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

GroupName

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CleanupStepGroup Class

CleanupStepGroup Overload

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_cleanupstepgroup__ctor_1.htm language=enus -->
## TOPIC 00242: CleanupStepGroup Constructor (CleanupStepGroup)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_cleanupstepgroup__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_cleanupstepgroup__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

CleanupStepGroup

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ node As CleanupStepGroup _ ) |

| C# |
| --- |
| public CleanupStepGroup( CleanupStepGroup node ) |

| Visual C++ |
| --- |
| public: CleanupStepGroup( CleanupStepGroup^ node ) |

###### Parameters

- **node**
  - Type: NationalInstruments.VeriStand.StimulusProfileDefinitionApi.CleanupStepGroupThe instance of CleanupStepGroup to copy.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CleanupStepGroup Class

CleanupStepGroup Overload

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_closeprojectstep__ctor.htm language=enus -->
## TOPIC 00243: CloseProjectStep Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_closeprojectstep__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_closeprojectstep__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

CloseProjectStep

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New |

| C# |
| --- |
| public CloseProjectStep() |

| Visual C++ |
| --- |
| public: CloseProjectStep() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CloseProjectStep Class

CloseProjectStep Overload

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_commandshell__ctor.htm language=enus -->
## TOPIC 00244: CommandShell Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_commandshell__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_commandshell__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

CommandShell

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New |

| C# |
| --- |
| public CommandShell() |

| Visual C++ |
| --- |
| public: CommandShell() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

FileName

String.Empty

Arguments

String.Empty

WaitToComplete

false

False

WaitToCompleteTimeout

HideCommandShellWindow

false

False

RedirectStandardOutput

false

False

RedirectStandardError

false

False

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CommandShell Class

CommandShell Overload

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_evaluation_evaluate.htm language=enus -->
## TOPIC 00245: Evaluation.Evaluate Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_evaluation_evaluate.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_evaluation_evaluate.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

value

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public MustOverride Function Evaluate ( _ value As DataValue _ ) As Boolean |

| C# |
| --- |
| public abstract bool Evaluate( DataValue value ) |

| Visual C++ |
| --- |
| public: virtual bool Evaluate( DataValue^ value ) abstract |

###### Parameters

- **value**
  - Type: NationalInstruments.VeriStand.Data.DataValueThe value to evaluate. This is typically the return value of a real-time sequence.

###### Return Value

true

True

value

EvaluationType

AlwaysPass

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Evaluation Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_ftpbase__ctor.htm language=enus -->
## TOPIC 00246: FTPBase Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_ftpbase__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_ftpbase__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

FTPBase

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New |

| C# |
| --- |
| public FTPBase() |

| Visual C++ |
| --- |
| public: FTPBase() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

Timeout

BufferLength

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

FTPBase Class

FTPBase Overload

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_ftpbase__ctor_1.htm language=enus -->
## TOPIC 00247: FTPBase Constructor (FTPBase)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_ftpbase__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_ftpbase__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

FTPBase

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ node As FTPBase _ ) |

| C# |
| --- |
| public FTPBase( FTPBase node ) |

| Visual C++ |
| --- |
| public: FTPBase( FTPBase^ node ) |

###### Parameters

- **node**
  - Type: NationalInstruments.VeriStand.StimulusProfileDefinitionApi.FTPBaseThe instance of FTPBase to copy.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

FTPBase Class

FTPBase Overload

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_ftpbase_checkforerrors.htm language=enus -->
## TOPIC 00248: FTPBase.CheckForErrors Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_ftpbase_checkforerrors.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_ftpbase_checkforerrors.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration.

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function CheckForErrors As CompilationEvent() |

| C# |
| --- |
| public override CompilationEvent[] CheckForErrors() |

| Visual C++ |
| --- |
| public: virtual array<CompilationEvent^>^ CheckForErrors() override |

###### Return Value

CompilationEvent

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

ActionStep.CheckForErrors

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

FTPBase Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_ftpbase_createuniquefilename.htm language=enus -->
## TOPIC 00249: FTPBase.CreateUniqueFileName Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_ftpbase_createuniquefilename.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_ftpbase_createuniquefilename.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

proposedFileName

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Function CreateUniqueFileName ( _ proposedFileName As String _ ) As String |

| C# |
| --- |
| protected string CreateUniqueFileName( string proposedFileName ) |

| Visual C++ |
| --- |
| protected: String^ CreateUniqueFileName( String^ proposedFileName ) |

###### Parameters

- **proposedFileName**
  - Type: System.StringThe filename to use to create a unique filename.

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

FTPBase Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_numericboundsevaluation_evaluate.htm language=enus -->
## TOPIC 00250: NumericBoundsEvaluation.Evaluate Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_numericboundsevaluation_evaluate.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_numericboundsevaluation_evaluate.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

NumericBounds

value

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function Evaluate ( _ value As DataValue _ ) As Boolean |

| C# |
| --- |
| public override bool Evaluate( DataValue value ) |

| Visual C++ |
| --- |
| public: virtual bool Evaluate( DataValue^ value ) override |

###### Parameters

- **value**
  - Type: NationalInstruments.VeriStand.Data.DataValueThe value to evaluate. This is typically the return value of a real-time sequence.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Use the CheckType property to specify whether a value must be within bounds or outside bounds to pass the evaluation. |

Evaluation.Evaluate

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

NumericBoundsEvaluation Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace
