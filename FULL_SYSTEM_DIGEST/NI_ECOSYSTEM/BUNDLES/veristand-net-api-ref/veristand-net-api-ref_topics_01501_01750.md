# NI DOCUMENT BUNDLE: veristand-net-api-ref

<!--NI_BUNDLE_CHUNK bundle=veristand-net-api-ref start=1501 end=1750 -->
<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload-ftpupload__string.html language=enus -->
## TOPIC 01501: FTPUpload(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload-ftpupload__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload-ftpupload__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the FTPUpload class with the specified destination directory on the FTP server. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic FTPUpload(string urlServer)ParametersNameTypeDescriptionurlServerstringDestination directory on the FTP serv

### FTPUpload(string)

Initializes a new instance of the [FTPUpload](nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload.html) class with the specified destination directory on the FTP server.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public FTPUpload(string urlServer)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| urlServer | string | Destination directory on the FTP server. |

Parent topic:

FTPUpload Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload-source.html language=enus -->
## TOPIC 01502: Source

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload-source.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload-source.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the path to the source file(s) to upload. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string Source { get; set; }ReturnsThe path to the source file(s) to upload. This value can be a file or a folder containing multiple files.

### Source

Gets or sets the path to the source file(s) to upload.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string Source { get; set; }

#### Returns

The path to the source file(s) to upload. This value can be a file or a folder containing multiple files.

Parent topic:

FTPUpload Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload-sourceisfolder.html language=enus -->
## TOPIC 01503: SourceIsFolder

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload-sourceisfolder.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload-sourceisfolder.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether the Source is a folder. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic bool SourceIsFolder { get; set; }Returnstrue if Source is a folder. If false, Source must be a specific file.

### SourceIsFolder

Gets or sets a value indicating whether the [Source](nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload-source.html) is a folder.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public bool SourceIsFolder { get; set; }

#### Returns

true if [Source](nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload-source.html) is a folder. If false, [Source](nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload-source.html) must be a specific file.

Parent topic:

FTPUpload Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload-stepname.html language=enus -->
## TOPIC 01504: StepName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload-stepname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload-stepname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override string StepName { get; }

### StepName

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override string StepName { get; }

Parent topic:

FTPUpload Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload.html language=enus -->
## TOPIC 01505: FTPUpload Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an FTP Upload step, which uploads files to an FTP server, such as an RT target. Derives fromFTPBaseSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic class FTPUpload : FTPBaseRemarksUse the members of this class to configure FTP settings and upload files to

### FTPUpload Class

Represents an FTP Upload step, which uploads files to an FTP server, such as an RT target.

#### Derives from

- FTPBase

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class FTPUpload : FTPBase

#### Remarks

Note

Some versions of Microsoft Windows block incoming FTP traffic by default. If prompted by the OS, allow NI VeriStand to use port 21 (FTP) to transfer data.

**Accessing this Class:**

- FTPUpload Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| FTPUpload(FTPUpload) | Initializes a new instance of the FTPUpload class by copying an existing instance. |
| FTPUpload(string) | Initializes a new instance of the FTPUpload class with the specified destination directory on the FTP server. |
| FTPUpload() | Initializes a new instance of the FTPUpload class. |

#### Properties

| Name | Description |
| --- | --- |
| Filter |  |
| Source | Gets or sets the path to the source file(s) to upload. |
| SourceIsFolder | Gets or sets a value indicating whether the Source is a folder. |
| StepName |  |

#### Methods

| Name | Description |
| --- | --- |
| CheckForErrors() | Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-launchniveristand-checkforerrors.html language=enus -->
## TOPIC 01506: CheckForErrors()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-launchniveristand-checkforerrors.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-launchniveristand-checkforerrors.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override CompilationEvent[] CheckForErrors()RemarksOverrides CheckForErrors. ReturnsAn arra

### CheckForErrors()

Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html)[] CheckForErrors()

#### Remarks

Overrides [CheckForErrors](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-checkforerrors.html).

#### Returns

An array of [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html) objects that represent the errors, warnings, and messages generated by the step.

Parent topic:

LaunchNIVeriStand Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-launchniveristand-launchniveristand.html language=enus -->
## TOPIC 01507: LaunchNIVeriStand()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-launchniveristand-launchniveristand.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-launchniveristand-launchniveristand.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the LaunchNIVeriStand class. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic LaunchNIVeriStand()RemarksThis constructor sets Timeout to 180 seconds.

### LaunchNIVeriStand()

Initializes a new instance of the [LaunchNIVeriStand](nationalinstruments-veristand-stimulusprofiledefinitionapi-launchniveristand.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public LaunchNIVeriStand()

#### Remarks

This constructor sets [Timeout](nationalinstruments-veristand-stimulusprofiledefinitionapi-launchniveristand-timeout.html) to 180 seconds.

Parent topic:

LaunchNIVeriStand Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-launchniveristand-launchniveristand__launchniveristand.html language=enus -->
## TOPIC 01508: LaunchNIVeriStand(LaunchNIVeriStand)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-launchniveristand-launchniveristand__launchniveristand.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-launchniveristand-launchniveristand__launchniveristand.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the LaunchNIVeriStand class by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic LaunchNIVeriStand(LaunchNIVeriStand node)ParametersNameTypeDescriptionnodeLaunchNIVeriStandThe instance of LaunchNIVeriStand to

### LaunchNIVeriStand(LaunchNIVeriStand)

Initializes a new instance of the [LaunchNIVeriStand](nationalinstruments-veristand-stimulusprofiledefinitionapi-launchniveristand.html) class by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public LaunchNIVeriStand(LaunchNIVeriStand node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | LaunchNIVeriStand | The instance of LaunchNIVeriStand to copy. |

Parent topic:

LaunchNIVeriStand Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-launchniveristand-stepname.html language=enus -->
## TOPIC 01509: StepName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-launchniveristand-stepname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-launchniveristand-stepname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override string StepName { get; }

### StepName

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override string StepName { get; }

Parent topic:

LaunchNIVeriStand Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-launchniveristand-timeout.html language=enus -->
## TOPIC 01510: Timeout

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-launchniveristand-timeout.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-launchniveristand-timeout.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the time in seconds to wait for NI VeriStand to launch before returning a timeout error. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic uint Timeout { get; set; }ReturnsThe time in seconds to wait for NI VeriStand to launch ExceptionsTypeDescriptionSys

### Timeout

Gets or sets the time in seconds to wait for NI VeriStand to launch before returning a timeout error.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public uint Timeout { get; set; }

#### Returns

The time in seconds to wait for NI VeriStand to launch

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentException | The specified value is less than 1. |

Parent topic:

LaunchNIVeriStand Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-launchniveristand.html language=enus -->
## TOPIC 01511: LaunchNIVeriStand Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-launchniveristand.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-launchniveristand.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Launch NI VeriStand step, which launches the NI VeriStand executable. Derives fromActionStepSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic class LaunchNIVeriStand : ActionStepRemarksThe Stimulus Profile Editor runs as a separate executable from the mai

### LaunchNIVeriStand Class

Represents a Launch NI VeriStand step, which launches the NI VeriStand executable.

#### Derives from

- ActionStep

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class LaunchNIVeriStand : ActionStep

#### Remarks

The Stimulus Profile Editor runs as a separate executable from the main NI VeriStand application. While you can edit stimulus profiles and real-time sequences without launching NI VeriStand, you cannot successfully execute tests unless NI VeriStand is running.

**Accessing this Class:**

- LaunchNIVeriStand Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| LaunchNIVeriStand(LaunchNIVeriStand) | Initializes a new instance of the LaunchNIVeriStand class by copying an existing instance. |
| LaunchNIVeriStand() | Initializes a new instance of the LaunchNIVeriStand class. |

#### Properties

| Name | Description |
| --- | --- |
| StepName |  |
| Timeout | Gets or sets the time in seconds to wait for NI VeriStand to launch before returning a timeout error. |

#### Methods

| Name | Description |
| --- | --- |
| CheckForErrors() | Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup-addchannel__systemdefinitionchannelresource.html language=enus -->
## TOPIC 01512: AddChannel(SystemDefinitionChannelResource)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup-addchannel__systemdefinitionchannelresource.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup-addchannel__systemdefinitionchannelresource.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified channel to the channel group. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic void AddChannel(SystemDefinitionChannelResource channel)ParametersNameTypeDescriptionchannelSystemDefinitionChannelResourceThe SystemDefinitionChannelResource reference

### AddChannel(SystemDefinitionChannelResource)

Adds the specified channel to the channel group.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public void AddChannel(SystemDefinitionChannelResource channel)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channel | SystemDefinitionChannelResource | The SystemDefinitionChannelResource reference to the channel. You can access this class from the Data assembly. |

Parent topic:

LogChannelGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup-channels.html language=enus -->
## TOPIC 01513: Channels

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup-channels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup-channels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the channels that belong to the channel group. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic SystemDefinitionChannelResource[] Channels { get; set; }ReturnsAn array of SystemDefinitionChannelResource objects (accessible from the NationalInstruments.Ve

### Channels

Gets or sets the channels that belong to the channel group.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public [SystemDefinitionChannelResource](nationalinstruments-veristand-data-systemdefinitionchannelresource.html)[] Channels { get; set; }

#### Returns

An array of SystemDefinitionChannelResource objects (accessible from the NationalInstruments.VeriStand.DataTypes assembly).

Parent topic:

LogChannelGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup-logchannelgroup.html language=enus -->
## TOPIC 01514: LogChannelGroup()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup-logchannelgroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup-logchannelgroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of LogChannelGroup. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic LogChannelGroup()RemarksThis constructor sets Name to "Group".

### LogChannelGroup()

Initializes a new instance of [LogChannelGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public LogChannelGroup()

#### Remarks

This constructor sets [Name](nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup-name.html) to "Group".

Parent topic:

LogChannelGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup-logchannelgroup__logchannelgroup.html language=enus -->
## TOPIC 01515: LogChannelGroup(LogChannelGroup)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup-logchannelgroup__logchannelgroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup-logchannelgroup__logchannelgroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of LogChannelGroup by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic LogChannelGroup(LogChannelGroup node)ParametersNameTypeDescriptionnodeLogChannelGroupThe instance of LogChannelGroup to copy.

### LogChannelGroup(LogChannelGroup)

Initializes a new instance of [LogChannelGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public LogChannelGroup(LogChannelGroup node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | LogChannelGroup | The instance of LogChannelGroup to copy. |

Parent topic:

LogChannelGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup-logchannelgroup__string.html language=enus -->
## TOPIC 01516: LogChannelGroup(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup-logchannelgroup__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup-logchannelgroup__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of LogChannelGroup and assigns the group the specified name . SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic LogChannelGroup(string name)ParametersNameTypeDescriptionnamestringThe name of the channel group.

### LogChannelGroup(string)

Initializes a new instance of [LogChannelGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup.html) and assigns the group the specified *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public LogChannelGroup(string name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the channel group. |

Parent topic:

LogChannelGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup-name.html language=enus -->
## TOPIC 01517: Name

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup-name.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup-name.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the channel group. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string Name { get; set; }ReturnsThe name of the group.

### Name

Gets or sets the name of the channel group.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string Name { get; set; }

#### Returns

The name of the group.

Parent topic:

LogChannelGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup-removechannel__systemdefinitionchannelresource.html language=enus -->
## TOPIC 01518: RemoveChannel(SystemDefinitionChannelResource)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup-removechannel__systemdefinitionchannelresource.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup-removechannel__systemdefinitionchannelresource.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes the specified channel from the channel group. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic void RemoveChannel(SystemDefinitionChannelResource channel)ParametersNameTypeDescriptionchannelSystemDefinitionChannelResourceThe SystemDefinitionChannelResource re

### RemoveChannel(SystemDefinitionChannelResource)

Removes the specified channel from the channel group.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public void RemoveChannel(SystemDefinitionChannelResource channel)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channel | SystemDefinitionChannelResource | The SystemDefinitionChannelResource reference to the channel. You can access this class from the NationalInstruments.VeriStand.DataTypes assembly. |

Parent topic:

LogChannelGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup.html language=enus -->
## TOPIC 01519: LogChannelGroup Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Channel Group, which contains channels in the system definition that you want to log from the stimulus profile. You can configure data logging by adding one or multiple channel groups to a StartLoggingStep. Derives fromBaseNodeSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfi

### LogChannelGroup Class

Represents a Channel Group, which contains channels in the system definition that you want to log from the stimulus profile. You can configure data logging by adding one or multiple channel groups to a [StartLoggingStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep.html).

#### Derives from

- BaseNode

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class LogChannelGroup : BaseNode

#### Remarks

Use the members of this class to configure the channel group and add and remove channels.

**Accessing this Class:**

- LogChannelGroup Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| LogChannelGroup() | Initializes a new instance of LogChannelGroup. |
| LogChannelGroup(string) | Initializes a new instance of LogChannelGroup and assigns the group the specified name . |
| LogChannelGroup(LogChannelGroup) | Initializes a new instance of LogChannelGroup by copying an existing instance. |

#### Properties

| Name | Description |
| --- | --- |
| Channels | Gets or sets the channels that belong to the channel group. |
| Name | Gets or sets the name of the channel group. |

#### Methods

| Name | Description |
| --- | --- |
| AddChannel(SystemDefinitionChannelResource) | Adds the specified channel to the channel group. |
| RemoveChannel(SystemDefinitionChannelResource) | Removes the specified channel from the channel group. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-logfilesegmentingoptions.html language=enus -->
## TOPIC 01520: LogFileSegmentingOptions Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-logfilesegmentingoptions.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-logfilesegmentingoptions.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how to segment the log files created during the data logging session. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic enum LogFileSegmentingOptionsRemarksYou can segment log files according to size limits or when a start trigger occurs. When the segmenting

### LogFileSegmentingOptions Enumeration

Specifies how to segment the log files created during the data logging session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public enum LogFileSegmentingOptions

#### Remarks

You can segment log files according to size limits or when a start trigger occurs. When the segmenting condition is met, NI VeriStand saves and closes the current log file and continues logging data in a new file.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| DoNotSegment |  | Specifies to not segment log files. |
| OnStartTrigger |  | Creates a new log file when a new start trigger occurs. |
| SizeLimit |  | Creates a new log file when the current log file reaches a certain size. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep-checkforerrors.html language=enus -->
## TOPIC 01521: CheckForErrors()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep-checkforerrors.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep-checkforerrors.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override CompilationEvent[] CheckForErrors()RemarksOverrides CheckForErrors. ReturnsAn arra

### CheckForErrors()

Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html)[] CheckForErrors()

#### Remarks

Overrides [CheckForErrors](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-checkforerrors.html).

#### Returns

An array of [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html) objects that represent the errors, warnings, and messages generated by the step.

Parent topic:

MacroPlayerStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep-filepath.html language=enus -->
## TOPIC 01522: FilePath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep-filepath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep-filepath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the path on disk to the macro (.nivsmacro) file to play back. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string FilePath { get; set; }ReturnsThe path to the macro file, as a string.

### FilePath

Gets or sets the path on disk to the macro (.nivsmacro) file to play back.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string FilePath { get; set; }

#### Returns

The path to the macro file, as a string.

Parent topic:

MacroPlayerStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep-macroplayerstep.html language=enus -->
## TOPIC 01523: MacroPlayerStep()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep-macroplayerstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep-macroplayerstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of MacroPlayerStep. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic MacroPlayerStep()RemarksThis constructor sets FilePath to string.Empty and Mode to IgnoreTiming.

### MacroPlayerStep()

Initializes a new instance of [MacroPlayerStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public MacroPlayerStep()

#### Remarks

This constructor sets [FilePath](nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep-filepath.html) to string.Empty and [Mode](nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep-mode.html) to IgnoreTiming.

Parent topic:

MacroPlayerStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep-macroplayerstep__macroplayerstep.html language=enus -->
## TOPIC 01524: MacroPlayerStep(MacroPlayerStep)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep-macroplayerstep__macroplayerstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep-macroplayerstep__macroplayerstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of MacroPlayerStep by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic MacroPlayerStep(MacroPlayerStep node)ParametersNameTypeDescriptionnodeMacroPlayerStepThe instance of MacroPlayerStep to copy.

### MacroPlayerStep(MacroPlayerStep)

Initializes a new instance of [MacroPlayerStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public MacroPlayerStep(MacroPlayerStep node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | MacroPlayerStep | The instance of MacroPlayerStep to copy. |

Parent topic:

MacroPlayerStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep-macroplayerstep__string-playmodeenum.html language=enus -->
## TOPIC 01525: MacroPlayerStep(string, PlayModeEnum)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep-macroplayerstep__string-playmodeenum.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep-macroplayerstep__string-playmodeenum.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of MacroPlayerStep for the macro file specified by filePath . SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic MacroPlayerStep(string filePath, PlayModeEnum mode)ParametersNameTypeDescriptionfilePathstringThe path on disk to the macro file.

### MacroPlayerStep(string, PlayModeEnum)

Initializes a new instance of [MacroPlayerStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep.html) for the macro file specified by *filePath* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public MacroPlayerStep(string filePath, PlayModeEnum mode)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | The path on disk to the macro file. |
| mode | PlayModeEnum | The playback mode to use for the file. 0 specifies to ignore the timing information embedded in the file and play back the macro as fast as possible. 1 specifies to use the timing information and play back the file at the speed it was recorded. |

Parent topic:

MacroPlayerStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep-mode.html language=enus -->
## TOPIC 01526: Mode

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep-mode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep-mode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the playback mode to use for the macro file. This mode specifies whether to use the timing information embedded in the macro file during playback, or to play back the file as fast as possible. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic PlayModeEnum

### Mode

Gets or sets the playback mode to use for the macro file. This mode specifies whether to use the timing information embedded in the macro file during playback, or to play back the file as fast as possible.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public [PlayModeEnum](nationalinstruments-veristand-clientapi-playmodeenum.html) Mode { get; set; }

#### Returns

An enumeration of [PlayModeEnum](nationalinstruments-veristand-clientapi-playmodeenum.html).

Parent topic:

MacroPlayerStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep-stepname.html language=enus -->
## TOPIC 01527: StepName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep-stepname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep-stepname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the step. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override string StepName { get; }RemarksOverrides StepName. ReturnsThe step name.

### StepName

Gets the name of the step.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override string StepName { get; }

#### Remarks

Overrides [StepName](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-stepname.html).

#### Returns

The step name.

Parent topic:

MacroPlayerStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep.html language=enus -->
## TOPIC 01528: MacroPlayerStep Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Macro Player step, which replays a previously recorded NI VeriStand macro (.nivsmacro) file. Derives fromActionStepSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic class MacroPlayerStep : ActionStepRemarksMacro files contain recordings of commands sent t

### MacroPlayerStep Class

Represents a Macro Player step, which replays a previously recorded NI VeriStand macro (.nivsmacro) file.

#### Derives from

- ActionStep

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class MacroPlayerStep : ActionStep

#### Remarks

Macro files contain recordings of commands sent to the target while an NI VeriStand project ran. You can use the Macro Recorder Workspace tool to create this file.

Use the members of this class to specify the file to play back and the timing setting to use for playback.

**Accessing this Class:**

- MacroPlayerStep Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| MacroPlayerStep(string, PlayModeEnum) | Initializes a new instance of MacroPlayerStep for the macro file specified by filePath . |
| MacroPlayerStep() | Initializes a new instance of MacroPlayerStep. |
| MacroPlayerStep(MacroPlayerStep) | Initializes a new instance of MacroPlayerStep by copying an existing instance. |

#### Properties

| Name | Description |
| --- | --- |
| FilePath | Gets or sets the path on disk to the macro (.nivsmacro) file to play back. |
| Mode | Gets or sets the playback mode to use for the macro file. This mode specifies whether to use the timing information embedded in the macro file during playback, or to play back the file as fast as possible. |
| StepName | Gets the name of the step. |

#### Methods

| Name | Description |
| --- | --- |
| CheckForErrors() | Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-mainstepgroup-mainstepgroup.html language=enus -->
## TOPIC 01529: MainStepGroup()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-mainstepgroup-mainstepgroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-mainstepgroup-mainstepgroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of MainStepGroup. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic MainStepGroup()RemarksThis constructor sets GroupName to "Group".

### MainStepGroup()

Initializes a new instance of [MainStepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-mainstepgroup.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public MainStepGroup()

#### Remarks

This constructor sets [GroupName](nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup-groupname.html) to "Group".

Parent topic:

MainStepGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-mainstepgroup-mainstepgroup__mainstepgroup.html language=enus -->
## TOPIC 01530: MainStepGroup(MainStepGroup)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-mainstepgroup-mainstepgroup__mainstepgroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-mainstepgroup-mainstepgroup__mainstepgroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of MainStepGroup by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic MainStepGroup(MainStepGroup node)ParametersNameTypeDescriptionnodeMainStepGroupThe instance of MainStepGroup to copy.

### MainStepGroup(MainStepGroup)

Initializes a new instance of [MainStepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-mainstepgroup.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public MainStepGroup(MainStepGroup node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | MainStepGroup | The instance of MainStepGroup to copy. |

Parent topic:

MainStepGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-mainstepgroup-mainstepgroup__string.html language=enus -->
## TOPIC 01531: MainStepGroup(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-mainstepgroup-mainstepgroup__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-mainstepgroup-mainstepgroup__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of MainStepGroup and assigns the group the specified groupName . SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic MainStepGroup(string groupName)ParametersNameTypeDescriptiongroupNamestringThe name of the step group.

### MainStepGroup(string)

Initializes a new instance of [MainStepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-mainstepgroup.html) and assigns the group the specified *groupName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public MainStepGroup(string groupName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| groupName | string | The name of the step group. |

Parent topic:

MainStepGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-mainstepgroup.html language=enus -->
## TOPIC 01532: MainStepGroup Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-mainstepgroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-mainstepgroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Main section of the stimulus profile code. This section is a StepGroup that contains the main execution code for the stimulus profile. Steps in this section execute after the SetupStepGroup and before the CleanupStepGroup. Derives fromStepGroupSyntaxNamespace: NationalInstruments.Veri

### MainStepGroup Class

Represents the **Main** section of the stimulus profile code. This section is a [StepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup.html) that contains the main execution code for the stimulus profile. Steps in this section execute after the [SetupStepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-setupstepgroup.html) and before the [CleanupStepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-cleanupstepgroup.html).

#### Derives from

- StepGroup

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class MainStepGroup : StepGroup

#### Remarks

Use the members of this class to get and set information about the step group.

**Accessing this Class:**

- MainStepGroup Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| MainStepGroup(string) | Initializes a new instance of MainStepGroup and assigns the group the specified groupName . |
| MainStepGroup(MainStepGroup) | Initializes a new instance of MainStepGroup by copying an existing instance. |
| MainStepGroup() | Initializes a new instance of MainStepGroup. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep-defaulttext.html language=enus -->
## TOPIC 01533: DefaultText

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep-defaulttext.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep-defaulttext.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the default text that appears in the pop-up dialog box in a text box beneath the Message. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string DefaultText { get; set; }ReturnsThe default text.

### DefaultText

Gets or sets the default text that appears in the pop-up dialog box in a text box beneath the [Message](nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep-message.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string DefaultText { get; set; }

#### Returns

The default text.

Parent topic:

MessageBoxStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep-message.html language=enus -->
## TOPIC 01534: Message

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep-message.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep-message.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the message that the pop-up dialog box displays. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string Message { get; set; }ReturnsThe message that the dialog box displays.

### Message

Gets or sets the message that the pop-up dialog box displays.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string Message { get; set; }

#### Returns

The message that the dialog box displays.

Parent topic:

MessageBoxStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep-messageboxstep.html language=enus -->
## TOPIC 01535: MessageBoxStep()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep-messageboxstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep-messageboxstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of MessageBoxStep. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic MessageBoxStep()RemarksThis constructor sets DefaultText, Message, and Title to string.Empty.

### MessageBoxStep()

Initializes a new instance of [MessageBoxStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public MessageBoxStep()

#### Remarks

This constructor sets [DefaultText](nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep-defaulttext.html), [Message](nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep-message.html), and [Title](nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep-title.html) to string.Empty.

Parent topic:

MessageBoxStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep-messageboxstep__messageboxstep.html language=enus -->
## TOPIC 01536: MessageBoxStep(MessageBoxStep)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep-messageboxstep__messageboxstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep-messageboxstep__messageboxstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of MessageBoxStep by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic MessageBoxStep(MessageBoxStep node)ParametersNameTypeDescriptionnodeMessageBoxStepThe instance of MessageBoxStep to copy.

### MessageBoxStep(MessageBoxStep)

Initializes a new instance of [MessageBoxStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public MessageBoxStep(MessageBoxStep node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | MessageBoxStep | The instance of MessageBoxStep to copy. |

Parent topic:

MessageBoxStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep-messageboxstep__string-string-string.html language=enus -->
## TOPIC 01537: MessageBoxStep(string, string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep-messageboxstep__string-string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep-messageboxstep__string-string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of MessageBoxStep and configures the pop-up dialog to display the specified message , title , and defaultText . SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic MessageBoxStep(string message, string title, string defaultText)ParametersNameT

### MessageBoxStep(string, string, string)

Initializes a new instance of [MessageBoxStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep.html) and configures the pop-up dialog to display the specified *message* , *title* , and *defaultText* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public MessageBoxStep(string message, string title, string defaultText)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| message | string | The message that the dialog box displays. |
| title | string | The title that appears in the title bar of the dialog box. |
| defaultText | string | The default text that appears in a text box beneath the message . |

Parent topic:

MessageBoxStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep-stepname.html language=enus -->
## TOPIC 01538: StepName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep-stepname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep-stepname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the step. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override string StepName { get; }RemarksOverrides StepName. ReturnsThe step name.

### StepName

Gets the name of the step.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override string StepName { get; }

#### Remarks

Overrides [StepName](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-stepname.html).

#### Returns

The step name.

Parent topic:

MessageBoxStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep-title.html language=enus -->
## TOPIC 01539: Title

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep-title.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep-title.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the title that appears in the title bar of the pop-up dialog box. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string Title { get; set; }ReturnsThe dialog box title.

### Title

Gets or sets the title that appears in the title bar of the pop-up dialog box.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string Title { get; set; }

#### Returns

The dialog box title.

Parent topic:

MessageBoxStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep.html language=enus -->
## TOPIC 01540: MessageBoxStep Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-messageboxstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Message Box step, which displays a pop-dialog box with a specified message. Derives fromActionStepSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic class MessageBoxStep : ActionStepRemarksUse the members of this class to configure the step, including the

### MessageBoxStep Class

Represents a Message Box step, which displays a pop-dialog box with a specified message.

#### Derives from

- ActionStep

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class MessageBoxStep : ActionStep

#### Remarks

Use the members of this class to configure the step, including the message that the box displays.

**Accessing this Class:**

- MessageBoxStep Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| MessageBoxStep(MessageBoxStep) | Initializes a new instance of MessageBoxStep by copying an existing instance. |
| MessageBoxStep() | Initializes a new instance of MessageBoxStep. |
| MessageBoxStep(string, string, string) | Initializes a new instance of MessageBoxStep and configures the pop-up dialog to display the specified message , title , and defaultText . |

#### Properties

| Name | Description |
| --- | --- |
| DefaultText | Gets or sets the default text that appears in the pop-up dialog box in a text box beneath the Message. |
| Message | Gets or sets the message that the pop-up dialog box displays. |
| StepName | Gets the name of the step. |
| Title | Gets or sets the title that appears in the title bar of the pop-up dialog box. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation-checktype.html language=enus -->
## TOPIC 01541: CheckType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation-checktype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation-checktype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the type of bounds check (within bounds or outside bounds) used for a NumericBounds evaluation. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic BoundsCheckType CheckType { get; set; }ReturnsAn enumeration of BoundsCheckType.

### CheckType

Gets or sets the type of bounds check (within bounds or outside bounds) used for a **NumericBounds** evaluation.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public [BoundsCheckType](nationalinstruments-veristand-stimulusprofiledefinitionapi-boundschecktype.html) CheckType { get; set; }

#### Returns

An enumeration of [BoundsCheckType](nationalinstruments-veristand-stimulusprofiledefinitionapi-boundschecktype.html).

Parent topic:

NumericBoundsEvaluation Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation-evaluate__datavalue.html language=enus -->
## TOPIC 01542: Evaluate(DataValue)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation-evaluate__datavalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation-evaluate__datavalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a NumericBounds evaluation on the specified value . SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override bool Evaluate(DataValue value)RemarksUse the CheckType property to specify whether a value must be within bounds or outside bounds to pass the evalu

### Evaluate(DataValue)

Performs a **NumericBounds** evaluation on the specified *value* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override bool Evaluate(DataValue value)

#### Remarks

Note

Use the [CheckType](nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation-checktype.html) property to specify whether a value must be within bounds or outside bounds to pass the evaluation.

Evaluate

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| value | DataValue | The value to evaluate. This is typically the return value of a real-time sequence. |

#### Returns

true if the value passes.

Parent topic:

NumericBoundsEvaluation Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation-highlimit.html language=enus -->
## TOPIC 01543: HighLimit

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation-highlimit.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation-highlimit.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the high limit of the bounds for a NumericBounds evaluation. A value is within bounds if it is less than or equal to this value and greater than or equal to the LowLimit. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic ScalarDataValue HighLimit { get; s

### HighLimit

Gets or sets the high limit of the bounds for a **NumericBounds** evaluation. A value is within bounds if it is less than or equal to this value and greater than or equal to the [LowLimit](nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation-lowlimit.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public [ScalarDataValue](nationalinstruments-veristand-data-scalardatavalue.html) HighLimit { get; set; }

#### Returns

The high limit of the numeric bounds.

Parent topic:

NumericBoundsEvaluation Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation-lowlimit.html language=enus -->
## TOPIC 01544: LowLimit

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation-lowlimit.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation-lowlimit.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the low limit of the bounds for a NumericBounds evaluation. A value is within bounds if it is greater than or equal to this value and less than or equal to the HighLimit. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic ScalarDataValue LowLimit { get; se

### LowLimit

Gets or sets the low limit of the bounds for a **NumericBounds** evaluation. A value is within bounds if it is greater than or equal to this value and less than or equal to the [HighLimit](nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation-highlimit.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public [ScalarDataValue](nationalinstruments-veristand-data-scalardatavalue.html) LowLimit { get; set; }

#### Returns

The low limit of the numeric bounds.

Parent topic:

NumericBoundsEvaluation Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation-numericboundsevaluation.html language=enus -->
## TOPIC 01545: NumericBoundsEvaluation()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation-numericboundsevaluation.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation-numericboundsevaluation.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of NumericBoundsEvaluation. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic NumericBoundsEvaluation()RemarksThis constructor sets HighLimit to 100, LowLimit to 0, and CheckType to Inbounds.

### NumericBoundsEvaluation()

Initializes a new instance of [NumericBoundsEvaluation](nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public NumericBoundsEvaluation()

#### Remarks

This constructor sets [HighLimit](nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation-highlimit.html) to 100, [LowLimit](nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation-lowlimit.html) to 0, and [CheckType](nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation-checktype.html) to [Inbounds](nationalinstruments-veristand-stimulusprofiledefinitionapi-boundschecktype.html).

Parent topic:

NumericBoundsEvaluation Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation-numericboundsevaluation__numericboundsevaluation.html language=enus -->
## TOPIC 01546: NumericBoundsEvaluation(NumericBoundsEvaluation)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation-numericboundsevaluation__numericboundsevaluation.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation-numericboundsevaluation__numericboundsevaluation.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of NumericBoundsEvaluation by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic NumericBoundsEvaluation(NumericBoundsEvaluation node)ParametersNameTypeDescriptionnodeNumericBoundsEvaluationThe instance of Numeri

### NumericBoundsEvaluation(NumericBoundsEvaluation)

Initializes a new instance of [NumericBoundsEvaluation](nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public NumericBoundsEvaluation(NumericBoundsEvaluation node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | NumericBoundsEvaluation | The instance of NumericBoundsEvaluation to copy. |

Parent topic:

NumericBoundsEvaluation Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation-numericboundsevaluation__scalardatavalue-scalardatavalue-boundschecktype.html language=enus -->
## TOPIC 01547: NumericBoundsEvaluation(ScalarDataValue, ScalarDataValue, BoundsCheckType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation-numericboundsevaluation__scalardatavalue-scalardatavalue-boundschecktype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation-numericboundsevaluation__scalardatavalue-scalardatavalue-boundschecktype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of NumericBoundsEvaluation with the specified bounds and check type, or condition for passing. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic NumericBoundsEvaluation(ScalarDataValue highLimit, ScalarDataValue lowLimit, BoundsCheckType che

### NumericBoundsEvaluation(ScalarDataValue, ScalarDataValue, BoundsCheckType)

Initializes a new instance of [NumericBoundsEvaluation](nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation.html) with the specified bounds and check type, or condition for passing.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public NumericBoundsEvaluation(ScalarDataValue highLimit, ScalarDataValue lowLimit, BoundsCheckType checkType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| highLimit | ScalarDataValue | The high limit of the bounds. A value is within bounds if it is less than or equal to this value and greater than or equal to the lowLimit . |
| lowLimit | ScalarDataValue | The low limit of the bounds. A value is within bounds if it is greater than or equal to this value and lower than or equal to the highLimit . |
| checkType | BoundsCheckType | The type of bounds check (within bounds or outside bounds) to use. This value specifies the passing condition for the evaluation. |

Parent topic:

NumericBoundsEvaluation Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation.html language=enus -->
## TOPIC 01548: NumericBoundsEvaluation Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a NumericBounds pass/fail evaluation, which checks if a specified value falls within the bounds of a specified high and low limit. You typically use evaluations on the return value of a real-time sequence to determine if the sequence passes or fails. Derives fromEvaluationSyntaxNamespace:

### NumericBoundsEvaluation Class

Represents a **NumericBounds** pass/fail evaluation, which checks if a specified value falls within the bounds of a specified high and low limit. You typically use evaluations on the return value of a real-time sequence to determine if the sequence passes or fails.

#### Derives from

- Evaluation

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class NumericBoundsEvaluation : Evaluation

#### Remarks

Use the members of this class to configure and perform a **NumericBounds** evaluation.

**Accessing this Class:**

- NumericBoundsEvaluation Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| NumericBoundsEvaluation(ScalarDataValue, ScalarDataValue, BoundsCheckType) | Initializes a new instance of NumericBoundsEvaluation with the specified bounds and check type, or condition for passing. |
| NumericBoundsEvaluation() | Initializes a new instance of NumericBoundsEvaluation. |
| NumericBoundsEvaluation(NumericBoundsEvaluation) | Initializes a new instance of NumericBoundsEvaluation by copying an existing instance. |

#### Properties

| Name | Description |
| --- | --- |
| CheckType | Gets or sets the type of bounds check (within bounds or outside bounds) used for a NumericBounds evaluation. |
| HighLimit | Gets or sets the high limit of the bounds for a NumericBounds evaluation. A value is within bounds if it is less than or equal to this value and greater than or equal to the LowLimit. |
| LowLimit | Gets or sets the low limit of the bounds for a NumericBounds evaluation. A value is within bounds if it is greater than or equal to this value and less than or equal to the HighLimit. |

#### Methods

| Name | Description |
| --- | --- |
| Evaluate(DataValue) | Performs a NumericBounds evaluation on the specified value . |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-checkforerrors.html language=enus -->
## TOPIC 01549: CheckForErrors()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-checkforerrors.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-checkforerrors.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override CompilationEvent[] CheckForErrors()RemarksOverrides CheckForErrors. ReturnsAn arra

### CheckForErrors()

Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html)[] CheckForErrors()

#### Remarks

Overrides [CheckForErrors](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-checkforerrors.html).

#### Returns

An array of [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html) objects that represent the errors, warnings, and messages generated by the step.

Parent topic:

OpenProjectStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-openprojectstep.html language=enus -->
## TOPIC 01550: OpenProjectStep()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-openprojectstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-openprojectstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of OpenProjectStep. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic OpenProjectStep()RemarksThis constructor sets Password, ProjectPath, and UserName to string.Empty and sets ShowProject to false.

### OpenProjectStep()

Initializes a new instance of [OpenProjectStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public OpenProjectStep()

#### Remarks

This constructor sets [Password](nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-password.html), [ProjectPath](nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-projectpath.html), and [UserName](nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-username.html) to string.Empty and sets [ShowProject](nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-showproject.html) to false.

Parent topic:

OpenProjectStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-openprojectstep__openprojectstep.html language=enus -->
## TOPIC 01551: OpenProjectStep(OpenProjectStep)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-openprojectstep__openprojectstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-openprojectstep__openprojectstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of OpenProjectStep by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic OpenProjectStep(OpenProjectStep node)ParametersNameTypeDescriptionnodeOpenProjectStepThe instance of OpenProjectStep to copy.

### OpenProjectStep(OpenProjectStep)

Initializes a new instance of [OpenProjectStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public OpenProjectStep(OpenProjectStep node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | OpenProjectStep | The instance of OpenProjectStep to copy. |

Parent topic:

OpenProjectStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-openprojectstep__string-string-string-bool.html language=enus -->
## TOPIC 01552: OpenProjectStep(string, string, string, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-openprojectstep__string-string-string-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-openprojectstep__string-string-string-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of OpenProjectStep for the project at the specified path , using the specified userName and password . SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic OpenProjectStep(string path, string userName, string password, bool showProject)Paramete

### OpenProjectStep(string, string, string, bool)

Initializes a new instance of [OpenProjectStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep.html) for the project at the specified *path* , using the specified *userName*  and *password* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public OpenProjectStep(string path, string userName, string password, bool showProject)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| path | string | The path to the NI VeriStand project (.nivsproj) file on disk. |
| userName | string | The user name to use to open the project. |
| password | string | The password for the specified userName . |
| showProject | bool | true to display the project in the NI VeriStand Project Explorer window. false to keep it hidden. |

Parent topic:

OpenProjectStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-password.html language=enus -->
## TOPIC 01553: Password

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-password.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-password.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the password used with the UserName to open the project. This property is ignored if the project is already open. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string Password { get; set; }ReturnsThe password for the UserName.

### Password

Gets or sets the password used with the [UserName](nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-username.html) to open the project. This property is ignored if the project is already open.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string Password { get; set; }

#### Returns

The password for the [UserName](nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-username.html).

Parent topic:

OpenProjectStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-projectpath.html language=enus -->
## TOPIC 01554: ProjectPath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-projectpath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-projectpath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the path to the NI VeriStand project (.nivsproj) file on disk. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string ProjectPath { get; set; }ReturnsThe path to the project file.

### ProjectPath

Gets or sets the path to the NI VeriStand project (.nivsproj) file on disk.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string ProjectPath { get; set; }

#### Returns

The path to the project file.

Parent topic:

OpenProjectStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-showproject.html language=enus -->
## TOPIC 01555: ShowProject

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-showproject.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-showproject.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to display the project in the NI VeriStand Project Explorer window when the project opens. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic bool ShowProject { get; set; }Returnstrue to display the project in the Project Explorer window. false to

### ShowProject

Gets or sets whether to display the project in the NI VeriStand **Project Explorer** window when the project opens.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public bool ShowProject { get; set; }

#### Returns

true to display the project in the **Project Explorer** window. false to keep it hidden.

Parent topic:

OpenProjectStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-stepname.html language=enus -->
## TOPIC 01556: StepName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-stepname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-stepname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the step. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override string StepName { get; }RemarksOverrides StepName. ReturnsThe step name.

### StepName

Gets the name of the step.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override string StepName { get; }

#### Remarks

Overrides [StepName](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-stepname.html).

#### Returns

The step name.

Parent topic:

OpenProjectStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-username.html language=enus -->
## TOPIC 01557: UserName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-username.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-username.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the user name used to open the NI VeriStand project. This property is ignored if the project is already open. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string UserName { get; set; }ReturnsThe user name for the project.

### UserName

Gets or sets the user name used to open the NI VeriStand project. This property is ignored if the project is already open.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string UserName { get; set; }

#### Returns

The user name for the project.

Parent topic:

OpenProjectStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep.html language=enus -->
## TOPIC 01558: OpenProjectStep Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an Open VeriStand Project step, which opens an NI VeriStand project (.nivsproj) file. Derives fromActionStepSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic class OpenProjectStep : ActionStepRemarksUse the members of this class to get and set information a

### OpenProjectStep Class

Represents an Open VeriStand Project step, which opens an NI VeriStand project (.nivsproj) file.

#### Derives from

- ActionStep

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class OpenProjectStep : ActionStep

#### Remarks

Use the members of this class to get and set information about the project, such as the path to the project on disk and the username and password for accessing the project.

**Accessing this Class:**

- OpenProjectStep Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| OpenProjectStep(string, string, string, bool) | Initializes a new instance of OpenProjectStep for the project at the specified path , using the specified userName and password . |
| OpenProjectStep(OpenProjectStep) | Initializes a new instance of OpenProjectStep by copying an existing instance. |
| OpenProjectStep() | Initializes a new instance of OpenProjectStep. |

#### Properties

| Name | Description |
| --- | --- |
| Password | Gets or sets the password used with the UserName to open the project. This property is ignored if the project is already open. |
| ProjectPath | Gets or sets the path to the NI VeriStand project (.nivsproj) file on disk. |
| ShowProject | Gets or sets whether to display the project in the NI VeriStand Project Explorer window when the project opens. |
| StepName | Gets the name of the step. |
| UserName | Gets or sets the user name used to open the NI VeriStand project. This property is ignored if the project is already open. |

#### Methods

| Name | Description |
| --- | --- |
| CheckForErrors() | Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacestep-openworkspacestep.html language=enus -->
## TOPIC 01559: OpenWorkspaceStep()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacestep-openworkspacestep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacestep-openworkspacestep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of OpenWorkspaceStep. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic OpenWorkspaceStep()

### OpenWorkspaceStep()

Initializes a new instance of [OpenWorkspaceStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacestep.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public OpenWorkspaceStep()

Parent topic:

OpenWorkspaceStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacestep-openworkspacestep__openworkspacestep.html language=enus -->
## TOPIC 01560: OpenWorkspaceStep(OpenWorkspaceStep)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacestep-openworkspacestep__openworkspacestep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacestep-openworkspacestep__openworkspacestep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of OpenWorkspaceStep by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic OpenWorkspaceStep(OpenWorkspaceStep node)ParametersNameTypeDescriptionnodeOpenWorkspaceStepThe instance of OpenWorkspaceStep to copy.

### OpenWorkspaceStep(OpenWorkspaceStep)

Initializes a new instance of [OpenWorkspaceStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacestep.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public OpenWorkspaceStep(OpenWorkspaceStep node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | OpenWorkspaceStep | The instance of OpenWorkspaceStep to copy. |

Parent topic:

OpenWorkspaceStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacestep-stepname.html language=enus -->
## TOPIC 01561: StepName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacestep-stepname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacestep-stepname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the step. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override string StepName { get; }RemarksOverrides StepName. ReturnsThe step name.

### StepName

Gets the name of the step.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override string StepName { get; }

#### Remarks

Overrides [StepName](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-stepname.html).

#### Returns

The step name.

Parent topic:

OpenWorkspaceStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacestep.html language=enus -->
## TOPIC 01562: OpenWorkspaceStep Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacestep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacestep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an Open VeriStand Workspace step, which opens the Workspace window with the screen file for the active NI VeriStand project. Derives fromActionStepSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic class OpenWorkspaceStep : ActionStepRemarksUse the members o

### OpenWorkspaceStep Class

Represents an Open VeriStand Workspace step, which opens the **Workspace** window with the screen file for the active NI VeriStand project.

#### Derives from

- ActionStep

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class OpenWorkspaceStep : ActionStep

#### Remarks

Use the members of this class to configure the step.

**Accessing this Class:**

- OpenWorkspaceStep Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| OpenWorkspaceStep(OpenWorkspaceStep) | Initializes a new instance of OpenWorkspaceStep by copying an existing instance. |
| OpenWorkspaceStep() | Initializes a new instance of OpenWorkspaceStep. |

#### Properties

| Name | Description |
| --- | --- |
| StepName | Gets the name of the step. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep-checkforerrors.html language=enus -->
## TOPIC 01563: CheckForErrors()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep-checkforerrors.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep-checkforerrors.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override CompilationEvent[] CheckForErrors()RemarksOverrides CheckForErrors. ReturnsAn arra

### CheckForErrors()

Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html)[] CheckForErrors()

#### Remarks

Overrides [CheckForErrors](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-checkforerrors.html).

#### Returns

An array of [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html) objects that represent the errors, warnings, and messages generated by the step.

Parent topic:

OpenWorkspaceToolStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep-initializationtime.html language=enus -->
## TOPIC 01564: InitializationTime

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep-initializationtime.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep-initializationtime.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the time in milliseconds allowed for the Workspace tool to initialize after it loads, but before proceeding to the next step. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic int InitializationTime { get; set; }ReturnsThe initialization time, in millisec

### InitializationTime

Gets or sets the time in milliseconds allowed for the Workspace tool to initialize after it loads, but before proceeding to the next step.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public int InitializationTime { get; set; }

#### Returns

The initialization time, in milliseconds.

Parent topic:

OpenWorkspaceToolStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep-openworkspacetoolstep.html language=enus -->
## TOPIC 01565: OpenWorkspaceToolStep()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep-openworkspacetoolstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep-openworkspacetoolstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of OpenWorkspaceToolStep. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic OpenWorkspaceToolStep()RemarksThis constructor sets WorkspaceToolPath to string.Empty.

### OpenWorkspaceToolStep()

Initializes a new instance of [OpenWorkspaceToolStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public OpenWorkspaceToolStep()

#### Remarks

This constructor sets [WorkspaceToolPath](nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep-workspacetoolpath.html) to string.Empty.

Parent topic:

OpenWorkspaceToolStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep-openworkspacetoolstep__openworkspacetoolstep.html language=enus -->
## TOPIC 01566: OpenWorkspaceToolStep(OpenWorkspaceToolStep)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep-openworkspacetoolstep__openworkspacetoolstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep-openworkspacetoolstep__openworkspacetoolstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of OpenWorkspaceToolStep by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic OpenWorkspaceToolStep(OpenWorkspaceToolStep node)ParametersNameTypeDescriptionnodeOpenWorkspaceToolStepThe instance of OpenWorkspaceT

### OpenWorkspaceToolStep(OpenWorkspaceToolStep)

Initializes a new instance of [OpenWorkspaceToolStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public OpenWorkspaceToolStep(OpenWorkspaceToolStep node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | OpenWorkspaceToolStep | The instance of OpenWorkspaceToolStep to copy. |

Parent topic:

OpenWorkspaceToolStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep-openworkspacetoolstep__string.html language=enus -->
## TOPIC 01567: OpenWorkspaceToolStep(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep-openworkspacetoolstep__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep-openworkspacetoolstep__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of OpenWorkspaceToolStep for the Workspace tool VI at the specified workspaceToolPath . SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic OpenWorkspaceToolStep(string workspaceToolPath)ParametersNameTypeDescriptionworkspaceToolPathstringThe

### OpenWorkspaceToolStep(string)

Initializes a new instance of [OpenWorkspaceToolStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep.html) for the Workspace tool VI at the specified *workspaceToolPath* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public OpenWorkspaceToolStep(string workspaceToolPath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| workspaceToolPath | string | The path to the Workspace tool VI. |

Parent topic:

OpenWorkspaceToolStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep-stepname.html language=enus -->
## TOPIC 01568: StepName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep-stepname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep-stepname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the step. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override string StepName { get; }RemarksOverrides StepName. ReturnsThe step name.

### StepName

Gets the name of the step.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override string StepName { get; }

#### Remarks

Overrides [StepName](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-stepname.html).

#### Returns

The step name.

Parent topic:

OpenWorkspaceToolStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep-workspacetoolpath.html language=enus -->
## TOPIC 01569: WorkspaceToolPath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep-workspacetoolpath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep-workspacetoolpath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the path to the Workspace tool VI. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string WorkspaceToolPath { get; set; }ReturnsThe path to the VI.

### WorkspaceToolPath

Gets or sets the path to the Workspace tool VI.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string WorkspaceToolPath { get; set; }

#### Returns

The path to the VI.

Parent topic:

OpenWorkspaceToolStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep.html language=enus -->
## TOPIC 01570: OpenWorkspaceToolStep Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an Open Workspace Tool step, which opens a Workspace tool for the active NI VeriStand project. Derives fromActionStepSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic class OpenWorkspaceToolStep : ActionStepRemarksUse the members of this class to configure

### OpenWorkspaceToolStep Class

Represents an Open Workspace Tool step, which opens a Workspace tool for the active NI VeriStand project.

#### Derives from

- ActionStep

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class OpenWorkspaceToolStep : ActionStep

#### Remarks

Use the members of this class to configure the step, including the path to the tool to open and the amount of time to allow the tool for initialization.

**Accessing this Class:**

- OpenWorkspaceToolStep Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| OpenWorkspaceToolStep(string) | Initializes a new instance of OpenWorkspaceToolStep for the Workspace tool VI at the specified workspaceToolPath . |
| OpenWorkspaceToolStep(OpenWorkspaceToolStep) | Initializes a new instance of OpenWorkspaceToolStep by copying an existing instance. |
| OpenWorkspaceToolStep() | Initializes a new instance of OpenWorkspaceToolStep. |

#### Properties

| Name | Description |
| --- | --- |
| InitializationTime | Gets or sets the time in milliseconds allowed for the Workspace tool to initialize after it loads, but before proceeding to the next step. |
| StepName | Gets the name of the step. |
| WorkspaceToolPath | Gets or sets the path to the Workspace tool VI. |

#### Methods

| Name | Description |
| --- | --- |
| CheckForErrors() | Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment-parametername.html language=enus -->
## TOPIC 01571: ParameterName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment-parametername.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment-parametername.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the sequence parameter. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string ParameterName { get; set; }ReturnsThe name of the parameter.

### ParameterName

Gets or sets the name of the sequence parameter.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string ParameterName { get; set; }

#### Returns

The name of the parameter.

Parent topic:

RealTimeSequenceCallParameterAssignment Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment-realtimesequencecallparameterassignment.html language=enus -->
## TOPIC 01572: RealTimeSequenceCallParameterAssignment()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment-realtimesequencecallparameterassignment.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment-realtimesequencecallparameterassignment.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of RealTimeSequenceCallParameterAssignment. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic RealTimeSequenceCallParameterAssignment()RemarksThis constructor sets ParameterName to string.Empty and Value to a VoidValue object.

### RealTimeSequenceCallParameterAssignment()

Initializes a new instance of [RealTimeSequenceCallParameterAssignment](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public RealTimeSequenceCallParameterAssignment()

#### Remarks

This constructor sets [ParameterName](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment-parametername.html) to string.Empty and [Value](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment-value.html) to a [VoidValue](nationalinstruments-veristand-data-voidvalue.html) object.

Parent topic:

RealTimeSequenceCallParameterAssignment Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment-realtimesequencecallparameterassignment__realtimesequencecallparameterassignment.html language=enus -->
## TOPIC 01573: RealTimeSequenceCallParameterAssignment(RealTimeSequenceCallParameterAssignment)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment-realtimesequencecallparameterassignment__realtimesequencecallparameterassignment.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment-realtimesequencecallparameterassignment__realtimesequencecallparameterassignment.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of RealTimeSequenceCallParameterAssignment by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic RealTimeSequenceCallParameterAssignment(RealTimeSequenceCallParameterAssignment node)ParametersNameTypeDescriptionn

### RealTimeSequenceCallParameterAssignment(RealTimeSequenceCallParameterAssignment)

Initializes a new instance of [RealTimeSequenceCallParameterAssignment](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public RealTimeSequenceCallParameterAssignment(RealTimeSequenceCallParameterAssignment node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | RealTimeSequenceCallParameterAssignment | The instance of RealTimeSequenceCallParameterAssignment to copy. |

Parent topic:

RealTimeSequenceCallParameterAssignment Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment-realtimesequencecallparameterassignment__string-dataresource.html language=enus -->
## TOPIC 01574: RealTimeSequenceCallParameterAssignment(string, DataResource)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment-realtimesequencecallparameterassignment__string-dataresource.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment-realtimesequencecallparameterassignment__string-dataresource.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of RealTimeSequenceCallParameterAssignment for the parameter with the specified parameterName and value , where value can be a constant or a channel in a system definition file. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic RealTimeSeque

### RealTimeSequenceCallParameterAssignment(string, DataResource)

Initializes a new instance of [RealTimeSequenceCallParameterAssignment](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment.html) for the parameter with the specified *parameterName*  and *value* , where *value*  can be a constant or a channel in a system definition file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public RealTimeSequenceCallParameterAssignment(string parameterName, DataResource value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| parameterName | string | The name of the sequence parameter. |
| value | DataResource | The value of the sequence parameter. You can access this object from the Data assembly. |

Parent topic:

RealTimeSequenceCallParameterAssignment Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment-realtimesequencecallparameterassignment__string-systemdefinitionchannelresource.html language=enus -->
## TOPIC 01575: RealTimeSequenceCallParameterAssignment(string, SystemDefinitionChannelResource)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment-realtimesequencecallparameterassignment__string-systemdefinitionchannelresource.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment-realtimesequencecallparameterassignment__string-systemdefinitionchannelresource.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of RealTimeSequenceCallParameterAssignment for the parameter with the specified parameterName and value , where value is a channel in a system definition file. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic RealTimeSequenceCallParameterAs

### RealTimeSequenceCallParameterAssignment(string, SystemDefinitionChannelResource)

Initializes a new instance of [RealTimeSequenceCallParameterAssignment](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment.html) for the parameter with the specified *parameterName*  and *value* , where *value*  is a channel in a system definition file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public RealTimeSequenceCallParameterAssignment(string parameterName, SystemDefinitionChannelResource value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| parameterName | string | The name of the sequence parameter. |
| value | SystemDefinitionChannelResource | The system definition channel that provides the value for parameterName . You can access this object from the Data assembly. |

Parent topic:

RealTimeSequenceCallParameterAssignment Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment-value.html language=enus -->
## TOPIC 01576: Value

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment-value.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment-value.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the value assigned to the real-time sequence parameter. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic DataResource Value { get; set; }ReturnsA DataResource object. This object can represent a constant or a channel in a system definition.

### Value

Gets or sets the value assigned to the real-time sequence parameter.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public [DataResource](nationalinstruments-veristand-data-dataresource.html) Value { get; set; }

#### Returns

A [DataResource](nationalinstruments-veristand-data-dataresource.html) object. This object can represent a constant or a channel in a system definition.

Parent topic:

RealTimeSequenceCallParameterAssignment Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment.html language=enus -->
## TOPIC 01577: RealTimeSequenceCallParameterAssignment Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the parameter assignments for a real-time sequence. A parameter can have a constant value or map to a channel in a system definition file. Derives fromBaseNodeSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic class RealTimeSequenceCallParameterAssignment :

### RealTimeSequenceCallParameterAssignment Class

Represents the parameter assignments for a real-time sequence. A parameter can have a constant value or map to a channel in a system definition file.

#### Derives from

- BaseNode

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class RealTimeSequenceCallParameterAssignment : BaseNode

#### Remarks

Use the members of this class to get or set the name and value of a real-time sequence parameter.

**Accessing this Class:**

- RealTimeSequenceCallParameterAssignment Constructor

AddReplaceParameterAssignment

ParameterAssignments

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| RealTimeSequenceCallParameterAssignment() | Initializes a new instance of RealTimeSequenceCallParameterAssignment. |
| RealTimeSequenceCallParameterAssignment(RealTimeSequenceCallParameterAssignment) | Initializes a new instance of RealTimeSequenceCallParameterAssignment by copying an existing instance. |
| RealTimeSequenceCallParameterAssignment(string, DataResource) | Initializes a new instance of RealTimeSequenceCallParameterAssignment for the parameter with the specified parameterName and value , where value can be a constant or a channel in a system definition file. |
| RealTimeSequenceCallParameterAssignment(string, SystemDefinitionChannelResource) | Initializes a new instance of RealTimeSequenceCallParameterAssignment for the parameter with the specified parameterName and value , where value is a channel in a system definition file. |

#### Properties

| Name | Description |
| --- | --- |
| ParameterName | Gets or sets the name of the sequence parameter. |
| Value | Gets or sets the value assigned to the real-time sequence parameter. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-addreplaceparameterassignment__realtimesequencecallparameterassignment.html language=enus -->
## TOPIC 01578: AddReplaceParameterAssignment(RealTimeSequenceCallParameterAssignment)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-addreplaceparameterassignment__realtimesequencecallparameterassignment.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-addreplaceparameterassignment__realtimesequencecallparameterassignment.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds or changes a parameter assignment for the real-time sequence. A parameter assignment can be a channel in the system definition or a constant value. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic void AddReplaceParameterAssignment(RealTimeSequenceCallParameterA

### AddReplaceParameterAssignment(RealTimeSequenceCallParameterAssignment)

Adds or changes a parameter assignment for the real-time sequence. A parameter assignment can be a channel in the system definition or a constant value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public void AddReplaceParameterAssignment(RealTimeSequenceCallParameterAssignment parameterAssignment)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| parameterAssignment | RealTimeSequenceCallParameterAssignment | The parameter assignment to add or change. |

Parent topic:

RealTimeSequenceCallStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-checkforerrors.html language=enus -->
## TOPIC 01579: CheckForErrors()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-checkforerrors.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-checkforerrors.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override CompilationEvent[] CheckForErrors()RemarksOverrides CheckForErrors. ReturnsAn arra

### CheckForErrors()

Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html)[] CheckForErrors()

#### Remarks

Overrides [CheckForErrors](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-checkforerrors.html).

#### Returns

An array of [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html) objects that represent the errors, warnings, and messages generated by the step.

Parent topic:

RealTimeSequenceCallStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-groupnumber.html language=enus -->
## TOPIC 01580: GroupNumber

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-groupnumber.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-groupnumber.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the Group Number for the real-time sequence. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic int GroupNumber { get; set; }

### GroupNumber

Gets or sets the Group Number for the real-time sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public int GroupNumber { get; set; }

Parent topic:

RealTimeSequenceCallStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-outputevaluation.html language=enus -->
## TOPIC 01581: OutputEvaluation

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-outputevaluation.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-outputevaluation.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a reference to the pass/fail evaluation performed on the real-time sequence. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic Evaluation OutputEvaluation { get; set; }ReturnsAn Evaluation object.

### OutputEvaluation

Gets or sets a reference to the pass/fail evaluation performed on the real-time sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public [Evaluation](nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluation.html) OutputEvaluation { get; set; }

#### Returns

An [Evaluation](nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluation.html) object.

Parent topic:

RealTimeSequenceCallStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-outputevaluationtype.html language=enus -->
## TOPIC 01582: OutputEvaluationType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-outputevaluationtype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-outputevaluationtype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the type of pass/fail evaluation performed on the real-time sequence. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic EvaluationType OutputEvaluationType { get; set; }ReturnsAn enumeration of EvaluationType.

### OutputEvaluationType

Gets or sets the type of pass/fail evaluation performed on the real-time sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public [EvaluationType](nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluationtype.html) OutputEvaluationType { get; set; }

#### Returns

An enumeration of [EvaluationType](nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluationtype.html).

Parent topic:

RealTimeSequenceCallStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-parameterassignments.html language=enus -->
## TOPIC 01583: ParameterAssignments

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-parameterassignments.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-parameterassignments.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the parameter assignments for the real-time sequence, which can be constant values or channels in the system definition file that the parameters map to. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic RealTimeSequenceCallParameterAssignment[] ParameterA

### ParameterAssignments

Gets or sets the parameter assignments for the real-time sequence, which can be constant values or channels in the system definition file that the parameters map to.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public [RealTimeSequenceCallParameterAssignment](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment.html)[] ParameterAssignments { get; set; }

#### Returns

An array of [RealTimeSequenceCallParameterAssignment](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallparameterassignment.html) objects.

Parent topic:

RealTimeSequenceCallStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-realtimesequencecallstep.html language=enus -->
## TOPIC 01584: RealTimeSequenceCallStep()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-realtimesequencecallstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-realtimesequencecallstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of RealTimeSequenceCallStep. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic RealTimeSequenceCallStep()RemarksThis constructor sets SequencePath to string.Empty.

### RealTimeSequenceCallStep()

Initializes a new instance of [RealTimeSequenceCallStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public RealTimeSequenceCallStep()

#### Remarks

This constructor sets [SequencePath](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-sequencepath.html) to string.Empty.

Parent topic:

RealTimeSequenceCallStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-realtimesequencecallstep__realtimesequencecallstep.html language=enus -->
## TOPIC 01585: RealTimeSequenceCallStep(RealTimeSequenceCallStep)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-realtimesequencecallstep__realtimesequencecallstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-realtimesequencecallstep__realtimesequencecallstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of RealTimeSequenceCallStep by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic RealTimeSequenceCallStep(RealTimeSequenceCallStep node)ParametersNameTypeDescriptionnodeRealTimeSequenceCallStepThe instance of Re

### RealTimeSequenceCallStep(RealTimeSequenceCallStep)

Initializes a new instance of [RealTimeSequenceCallStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public RealTimeSequenceCallStep(RealTimeSequenceCallStep node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | RealTimeSequenceCallStep | The instance of RealTimeSequenceCallStep to copy. |

Parent topic:

RealTimeSequenceCallStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-realtimesequencecallstep__string.html language=enus -->
## TOPIC 01586: RealTimeSequenceCallStep(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-realtimesequencecallstep__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-realtimesequencecallstep__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of RealTimeSequenceCallStep for the sequence at the specified sequencePath . SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic RealTimeSequenceCallStep(string sequencePath)ParametersNameTypeDescriptionsequencePathstringThe path to the real-t

### RealTimeSequenceCallStep(string)

Initializes a new instance of [RealTimeSequenceCallStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep.html) for the sequence at the specified *sequencePath* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public RealTimeSequenceCallStep(string sequencePath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sequencePath | string | The path to the real-time sequence file. This can be a .nivsseq file or a properly formatted .csv file. |

Parent topic:

RealTimeSequenceCallStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-refreshsequencecall.html language=enus -->
## TOPIC 01587: RefreshSequenceCall()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-refreshsequencecall.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-refreshsequencecall.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refreshes the ParameterAssignments and OutputEvaluation for the sequence call based on the current contents of the sequence. This ensures that parameter assignments exist for all parameters, and that the data types of all parameter assignments match the data type of the corresponding sequence. This

### RefreshSequenceCall()

Refreshes the [ParameterAssignments](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-parameterassignments.html) and [OutputEvaluation](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-outputevaluation.html) for the sequence call based on the current contents of the sequence. This ensures that parameter assignments exist for all parameters, and that the data types of all parameter assignments match the data type of the corresponding sequence. This method also deletes any parameter assignments that have no corresponding entry in the sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public void RefreshSequenceCall()

#### Remarks

Note

This method has no effect if [SequencePath](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-sequencepath.html) is not a valid file path.

Parent topic:

RealTimeSequenceCallStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-refreshsequencecall__realtimesequence.html language=enus -->
## TOPIC 01588: RefreshSequenceCall(RealTimeSequence)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-refreshsequencecall__realtimesequence.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-refreshsequencecall__realtimesequence.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refreshes the ParameterAssignments and OutputEvaluation for the sequence call based on the current contents of the specified sequence . This ensures that parameter assignments exist for all parameters, and that the data types of all parameter assignments match the data type of the corresponding sequ

### RefreshSequenceCall(RealTimeSequence)

Refreshes the [ParameterAssignments](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-parameterassignments.html) and [OutputEvaluation](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-outputevaluation.html) for the sequence call based on the current contents of the specified *sequence* . This ensures that parameter assignments exist for all parameters, and that the data types of all parameter assignments match the data type of the corresponding sequence. This method also deletes any parameter assignments that have no corresponding entry in the sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public void RefreshSequenceCall(RealTimeSequence sequence)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sequence | RealTimeSequence | The reference to the sequence to use to validate the sequence call data. |

Parent topic:

RealTimeSequenceCallStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-sequencepath.html language=enus -->
## TOPIC 01589: SequencePath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-sequencepath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-sequencepath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the path to the real-time sequence (.nivsseq) file on disk. A properly formatted CSV (.csv) file also can function as a real-time sequence. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string SequencePath { get; set; }ReturnsThe path to the sequence

### SequencePath

Gets or sets the path to the real-time sequence (.nivsseq) file on disk. A properly formatted CSV (.csv) file also can function as a real-time sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string SequencePath { get; set; }

#### Returns

The path to the sequence file.

Parent topic:

RealTimeSequenceCallStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-stepname.html language=enus -->
## TOPIC 01590: StepName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-stepname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-stepname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the step. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override string StepName { get; }RemarksOverrides StepName. ReturnsThe step name.

### StepName

Gets the name of the step.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override string StepName { get; }

#### Remarks

Overrides [StepName](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-stepname.html).

#### Returns

The step name.

Parent topic:

RealTimeSequenceCallStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-target.html language=enus -->
## TOPIC 01591: Target

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-target.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-target.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The name of the target on which the sequence will execute. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string Target { get; set; }ReturnsThe name of the target. If this is an empty string, NI VeriStand assigns a default target based on the ParameterAssignments.

### Target

The name of the target on which the sequence will execute.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string Target { get; set; }

#### Returns

The name of the target. If this is an empty string, NI VeriStand assigns a default target based on the [ParameterAssignments](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-parameterassignments.html).

Parent topic:

RealTimeSequenceCallStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-timeout.html language=enus -->
## TOPIC 01592: Timeout

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-timeout.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-timeout.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets he timeout in milliseconds within which the real-time sequence must complete each time step. If the sequence exceeds this timeout, the VeriStand Engine aborts the sequence execution and returns an error. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic d

### Timeout

Gets or sets he timeout in milliseconds within which the real-time sequence must complete each time step. If the sequence exceeds this timeout, the VeriStand Engine aborts the sequence execution and returns an error.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public double Timeout { get; set; }

#### Returns

The timeout, in milliseconds. The default is 10000. 0 or -1 indicates an infinite timeout.

Parent topic:

RealTimeSequenceCallStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep.html language=enus -->
## TOPIC 01593: RealTimeSequenceCallStep Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Call Real-Time Sequence Step, which calls a real-time sequence to execute. Derives fromActionStepSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic class RealTimeSequenceCallStep : ActionStepRemarksA real-time sequence is a program that can deploy to a tar

### RealTimeSequenceCallStep Class

Represents a Call Real-Time Sequence Step, which calls a real-time sequence to execute.

#### Derives from

- ActionStep

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class RealTimeSequenceCallStep : ActionStep

#### Remarks

A real-time sequence is a program that can deploy to a target with a system definition file and read/write channels defined in the system definition file. Use the members of this class to get or set the path to the sequence, assign parameters in the sequence constant values or map them to channels in the system definition, and get or set the evaluation method used to determine if the sequence passes or fails.

**Accessing this Class:**

- [Sequences](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep-sequences.html)
- RealTimeSequenceCallStep Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| RealTimeSequenceCallStep(string) | Initializes a new instance of RealTimeSequenceCallStep for the sequence at the specified sequencePath . |
| RealTimeSequenceCallStep() | Initializes a new instance of RealTimeSequenceCallStep. |
| RealTimeSequenceCallStep(RealTimeSequenceCallStep) | Initializes a new instance of RealTimeSequenceCallStep by copying an existing instance. |

#### Properties

| Name | Description |
| --- | --- |
| GroupNumber | Gets or sets the Group Number for the real-time sequence. |
| OutputEvaluation | Gets or sets a reference to the pass/fail evaluation performed on the real-time sequence. |
| OutputEvaluationType | Gets or sets the type of pass/fail evaluation performed on the real-time sequence. |
| ParameterAssignments | Gets or sets the parameter assignments for the real-time sequence, which can be constant values or channels in the system definition file that the parameters map to. |
| SequencePath | Gets or sets the path to the real-time sequence (.nivsseq) file on disk. A properly formatted CSV (.csv) file also can function as a real-time sequence. |
| StepName | Gets the name of the step. |
| Target | The name of the target on which the sequence will execute. |
| Timeout | Gets or sets he timeout in milliseconds within which the real-time sequence must complete each time step. If the sequence exceeds this timeout, the VeriStand Engine aborts the sequence execution and returns an error. |

#### Methods

| Name | Description |
| --- | --- |
| AddReplaceParameterAssignment(RealTimeSequenceCallParameterAssignment) | Adds or changes a parameter assignment for the real-time sequence. A parameter assignment can be a channel in the system definition or a constant value. |
| CheckForErrors() | Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. |
| RefreshSequenceCall() | Refreshes the ParameterAssignments and OutputEvaluation for the sequence call based on the current contents of the sequence. This ensures that parameter assignments exist for all parameters, and that the data types of all parameter assignments match the data type of the corresponding sequence. This method also deletes any parameter assignments that have no corresponding entry in the sequence. |
| RefreshSequenceCall(RealTimeSequence) | Refreshes the ParameterAssignments and OutputEvaluation for the sequence call based on the current contents of the specified sequence . This ensures that parameter assignments exist for all parameters, and that the data types of all parameter assignments match the data type of the corresponding sequence. This method also deletes any parameter assignments that have no corresponding entry in the sequence. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep-addsequence__realtimesequencecallstep.html language=enus -->
## TOPIC 01594: AddSequence(RealTimeSequenceCallStep)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep-addsequence__realtimesequencecallstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep-addsequence__realtimesequencecallstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified sequence to the real-time sequence group. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic void AddSequence(RealTimeSequenceCallStep sequence)ParametersNameTypeDescriptionsequenceRealTimeSequenceCallStepThe calling step for the sequence to add to t

### AddSequence(RealTimeSequenceCallStep)

Adds the specified *sequence*  to the real-time sequence group.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public void AddSequence(RealTimeSequenceCallStep sequence)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sequence | RealTimeSequenceCallStep | The calling step for the sequence to add to the group. |

Parent topic:

RealTimeSequenceGroupStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep-checkforerrors.html language=enus -->
## TOPIC 01595: CheckForErrors()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep-checkforerrors.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep-checkforerrors.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override CompilationEvent[] CheckForErrors()RemarksOverrides CheckForErrors. ReturnsAn arra

### CheckForErrors()

Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html)[] CheckForErrors()

#### Remarks

Overrides [CheckForErrors](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-checkforerrors.html).

#### Returns

An array of [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html) objects that represent the errors, warnings, and messages generated by the step.

Parent topic:

RealTimeSequenceGroupStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep-groupname.html language=enus -->
## TOPIC 01596: GroupName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep-groupname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep-groupname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the real-time sequence group. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string GroupName { get; set; }ReturnsThe name of the group.

### GroupName

Gets or sets the name of the real-time sequence group.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string GroupName { get; set; }

#### Returns

The name of the group.

Parent topic:

RealTimeSequenceGroupStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep-realtimesequencegroupstep.html language=enus -->
## TOPIC 01597: RealTimeSequenceGroupStep()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep-realtimesequencegroupstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep-realtimesequencegroupstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of RealTimeSequenceGroupStep. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic RealTimeSequenceGroupStep()RemarksThis constructor sets GroupName to "Real-Time Sequence Group".

### RealTimeSequenceGroupStep()

Initializes a new instance of [RealTimeSequenceGroupStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public RealTimeSequenceGroupStep()

#### Remarks

This constructor sets [GroupName](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep-groupname.html) to "Real-Time Sequence Group".

Parent topic:

RealTimeSequenceGroupStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep-realtimesequencegroupstep__realtimesequencegroupstep.html language=enus -->
## TOPIC 01598: RealTimeSequenceGroupStep(RealTimeSequenceGroupStep)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep-realtimesequencegroupstep__realtimesequencegroupstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep-realtimesequencegroupstep__realtimesequencegroupstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of RealTimeSequenceGroupStep by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic RealTimeSequenceGroupStep(RealTimeSequenceGroupStep node)ParametersNameTypeDescriptionnodeRealTimeSequenceGroupStepThe instance o

### RealTimeSequenceGroupStep(RealTimeSequenceGroupStep)

Initializes a new instance of [RealTimeSequenceGroupStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public RealTimeSequenceGroupStep(RealTimeSequenceGroupStep node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | RealTimeSequenceGroupStep | The instance of RealTimeSequenceGroupStep to copy. |

Parent topic:

RealTimeSequenceGroupStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep-realtimesequencegroupstep__string.html language=enus -->
## TOPIC 01599: RealTimeSequenceGroupStep(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep-realtimesequencegroupstep__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep-realtimesequencegroupstep__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of RealTimeSequenceGroupStep for the group with the specified groupName . SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic RealTimeSequenceGroupStep(string groupName)ParametersNameTypeDescriptiongroupNamestringThe name of the real-time sequ

### RealTimeSequenceGroupStep(string)

Initializes a new instance of [RealTimeSequenceGroupStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep.html) for the group with the specified *groupName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public RealTimeSequenceGroupStep(string groupName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| groupName | string | The name of the real-time sequence group. |

Parent topic:

RealTimeSequenceGroupStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep-sequences.html language=enus -->
## TOPIC 01600: Sequences

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep-sequences.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep-sequences.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the real-time sequences that belong to the real-time sequence group. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic RealTimeSequenceCallStep[] Sequences { get; set; }ReturnsAn array of RealTimeSequenceCallStep objects.

### Sequences

Gets or sets the real-time sequences that belong to the real-time sequence group.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public [RealTimeSequenceCallStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep.html)[] Sequences { get; set; }

#### Returns

An array of [RealTimeSequenceCallStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep.html) objects.

Parent topic:

RealTimeSequenceGroupStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep-stepname.html language=enus -->
## TOPIC 01601: StepName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep-stepname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep-stepname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the step. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override string StepName { get; }RemarksOverrides StepName. ReturnsThe step name.

### StepName

Gets the name of the step.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override string StepName { get; }

#### Remarks

Overrides [StepName](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-stepname.html).

#### Returns

The step name.

Parent topic:

RealTimeSequenceGroupStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep.html language=enus -->
## TOPIC 01602: RealTimeSequenceGroupStep Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Real-Time Sequence Group, which contains a group of RealTimeSequenceCallStep objects that execute in parallel. This step does not complete until each real-time sequence in the group executes. Derives fromActionStepSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionA

### RealTimeSequenceGroupStep Class

Represents a Real-Time Sequence Group, which contains a group of [RealTimeSequenceCallStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep.html) objects that execute in parallel. This step does not complete until each real-time sequence in the group executes.

#### Derives from

- ActionStep

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class RealTimeSequenceGroupStep : ActionStep

#### Remarks

Use the members of this class to create a group of sequences that execute in parallel.

**Accessing this Class:**

- RealTimeSequenceGroupStep Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| RealTimeSequenceGroupStep(string) | Initializes a new instance of RealTimeSequenceGroupStep for the group with the specified groupName . |
| RealTimeSequenceGroupStep() | Initializes a new instance of RealTimeSequenceGroupStep. |
| RealTimeSequenceGroupStep(RealTimeSequenceGroupStep) | Initializes a new instance of RealTimeSequenceGroupStep by copying an existing instance. |

#### Properties

| Name | Description |
| --- | --- |
| GroupName | Gets or sets the name of the real-time sequence group. |
| Sequences | Gets or sets the real-time sequences that belong to the real-time sequence group. |
| StepName | Gets the name of the step. |

#### Methods

| Name | Description |
| --- | --- |
| AddSequence(RealTimeSequenceCallStep) | Adds the specified sequence to the real-time sequence group. |
| CheckForErrors() | Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-sendprojectcommandstep-command.html language=enus -->
## TOPIC 01603: Command

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-sendprojectcommandstep-command.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-sendprojectcommandstep-command.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the command sent to the VeriStand project (Connect, Run, Deploy, and so on). SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic VeriStandProjectCommand Command { get; set; }ReturnsAn enumeration of VeriStandProjectCommand.

### Command

Gets or sets the command sent to the VeriStand project (Connect, Run, Deploy, and so on).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public [VeriStandProjectCommand](nationalinstruments-veristand-stimulusprofiledefinitionapi-veristandprojectcommand.html) Command { get; set; }

#### Returns

An enumeration of [VeriStandProjectCommand](nationalinstruments-veristand-stimulusprofiledefinitionapi-veristandprojectcommand.html).

Parent topic:

SendProjectCommandStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-sendprojectcommandstep-sendprojectcommandstep.html language=enus -->
## TOPIC 01604: SendProjectCommandStep()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-sendprojectcommandstep-sendprojectcommandstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-sendprojectcommandstep-sendprojectcommandstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SendProjectCommandStep. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic SendProjectCommandStep()RemarksThis constructor sets Command to Run.

### SendProjectCommandStep()

Initializes a new instance of [SendProjectCommandStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-sendprojectcommandstep.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public SendProjectCommandStep()

#### Remarks

This constructor sets [Command](nationalinstruments-veristand-stimulusprofiledefinitionapi-sendprojectcommandstep-command.html) to [Run](nationalinstruments-veristand-stimulusprofiledefinitionapi-veristandprojectcommand.html).

Parent topic:

SendProjectCommandStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-sendprojectcommandstep-sendprojectcommandstep__sendprojectcommandstep.html language=enus -->
## TOPIC 01605: SendProjectCommandStep(SendProjectCommandStep)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-sendprojectcommandstep-sendprojectcommandstep__sendprojectcommandstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-sendprojectcommandstep-sendprojectcommandstep__sendprojectcommandstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SendProjectCommandStep by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic SendProjectCommandStep(SendProjectCommandStep node)ParametersNameTypeDescriptionnodeSendProjectCommandStepThe instance of SendProjec

### SendProjectCommandStep(SendProjectCommandStep)

Initializes a new instance of [SendProjectCommandStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-sendprojectcommandstep.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public SendProjectCommandStep(SendProjectCommandStep node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | SendProjectCommandStep | The instance of SendProjectCommandStep to copy. |

Parent topic:

SendProjectCommandStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-sendprojectcommandstep-sendprojectcommandstep__veristandprojectcommand.html language=enus -->
## TOPIC 01606: SendProjectCommandStep(VeriStandProjectCommand)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-sendprojectcommandstep-sendprojectcommandstep__veristandprojectcommand.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-sendprojectcommandstep-sendprojectcommandstep__veristandprojectcommand.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SendProjectCommandStep for the specified command. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic SendProjectCommandStep(VeriStandProjectCommand command)ParametersNameTypeDescriptioncommandVeriStandProjectCommandThe command to send to t

### SendProjectCommandStep(VeriStandProjectCommand)

Initializes a new instance of [SendProjectCommandStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-sendprojectcommandstep.html) for the specified command.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public SendProjectCommandStep(VeriStandProjectCommand command)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| command | VeriStandProjectCommand | The command to send to the NI VeriStand project. |

Parent topic:

SendProjectCommandStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-sendprojectcommandstep-stepname.html language=enus -->
## TOPIC 01607: StepName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-sendprojectcommandstep-stepname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-sendprojectcommandstep-stepname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the step. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override string StepName { get; }RemarksOverrides StepName. ReturnsThe step name.

### StepName

Gets the name of the step.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override string StepName { get; }

#### Remarks

Overrides [StepName](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-stepname.html).

#### Returns

The step name.

Parent topic:

SendProjectCommandStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-sendprojectcommandstep.html language=enus -->
## TOPIC 01608: SendProjectCommandStep Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-sendprojectcommandstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-sendprojectcommandstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Control Active VeriStand Project step, which sends a command (Connect, Run, Deploy, and so on) to the NI VeriStand project the stimulus profile is associated with. Derives fromActionStepSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic class SendProjectCo

### SendProjectCommandStep Class

Represents a Control Active VeriStand Project step, which sends a command (Connect, Run, Deploy, and so on) to the NI VeriStand project the stimulus profile is associated with.

#### Derives from

- ActionStep

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class SendProjectCommandStep : ActionStep

#### Remarks

Use the members of this class to send commands to an NI VeriStand project.

**Accessing this Class:**

- SendProjectCommandStep Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SendProjectCommandStep(SendProjectCommandStep) | Initializes a new instance of SendProjectCommandStep by copying an existing instance. |
| SendProjectCommandStep() | Initializes a new instance of SendProjectCommandStep. |
| SendProjectCommandStep(VeriStandProjectCommand) | Initializes a new instance of SendProjectCommandStep for the specified command. |

#### Properties

| Name | Description |
| --- | --- |
| Command | Gets or sets the command sent to the VeriStand project (Connect, Run, Deploy, and so on). |
| StepName | Gets the name of the step. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-command.html language=enus -->
## TOPIC 01609: Command

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-command.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-command.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the message or command sent to the tool. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string Command { get; set; }ReturnsThe message, or command.

### Command

Gets or sets the message or command sent to the tool.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string Command { get; set; }

#### Returns

The message, or command.

Parent topic:

SendWorkspaceToolMessageStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-data.html language=enus -->
## TOPIC 01610: Data

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-data.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-data.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets any data required by the case of the Workspace tool that handles the Command. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string Data { get; set; }ReturnsThe required data, as a string.

### Data

Gets or sets any data required by the case of the Workspace tool that handles the [Command](nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-command.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string Data { get; set; }

#### Returns

The required data, as a string.

Parent topic:

SendWorkspaceToolMessageStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-sendworkspacetoolmessagestep.html language=enus -->
## TOPIC 01611: SendWorkspaceToolMessageStep()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-sendworkspacetoolmessagestep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-sendworkspacetoolmessagestep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SendWorkspaceToolMessageStep. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic SendWorkspaceToolMessageStep()RemarksThis constructor sets Timeout to 0 and sets Command, Data, and WorkspaceToolPath to string.Empty.

### SendWorkspaceToolMessageStep()

Initializes a new instance of [SendWorkspaceToolMessageStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public SendWorkspaceToolMessageStep()

#### Remarks

This constructor sets [Timeout](nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-timeout.html) to 0 and sets [Command](nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-command.html), [Data](nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-data.html), and [WorkspaceToolPath](nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-workspacetoolpath.html) to string.Empty.

Parent topic:

SendWorkspaceToolMessageStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-sendworkspacetoolmessagestep__sendworkspacetoolmessagestep.html language=enus -->
## TOPIC 01612: SendWorkspaceToolMessageStep(SendWorkspaceToolMessageStep)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-sendworkspacetoolmessagestep__sendworkspacetoolmessagestep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-sendworkspacetoolmessagestep__sendworkspacetoolmessagestep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SendWorkspaceToolMessageStep by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic SendWorkspaceToolMessageStep(SendWorkspaceToolMessageStep node)ParametersNameTypeDescriptionnodeSendWorkspaceToolMessageStepTh

### SendWorkspaceToolMessageStep(SendWorkspaceToolMessageStep)

Initializes a new instance of [SendWorkspaceToolMessageStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public SendWorkspaceToolMessageStep(SendWorkspaceToolMessageStep node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | SendWorkspaceToolMessageStep | The instance of SendWorkspaceToolMessageStep to copy. |

Parent topic:

SendWorkspaceToolMessageStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-sendworkspacetoolmessagestep__string-string-string-uint.html language=enus -->
## TOPIC 01613: SendWorkspaceToolMessageStep(string, string, string, uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-sendworkspacetoolmessagestep__string-string-string-uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-sendworkspacetoolmessagestep__string-string-string-uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SendWorkspaceToolMessageStep for the tool at workspaceToolPath with the specified command , data , and timeout . SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic SendWorkspaceToolMessageStep(string workspaceToolPath, string command, stri

### SendWorkspaceToolMessageStep(string, string, string, uint)

Initializes a new instance of [SendWorkspaceToolMessageStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep.html) for the tool at *workspaceToolPath*  with the specified *command* , *data* , and *timeout* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public SendWorkspaceToolMessageStep(string workspaceToolPath, string command, string data, uint timeout)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| workspaceToolPath | string | The path to the Workspace tool VI. |
| command | string | The message or command to send the Workspace tool. |
| data | string | Additional data required by the case of the Workspace tool that handles the command . |
| timeout | uint | The amount of time in milliseconds to wait for a response from the Workspace tool before timing out. |

Parent topic:

SendWorkspaceToolMessageStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-stepname.html language=enus -->
## TOPIC 01614: StepName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-stepname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-stepname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the step. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override string StepName { get; }RemarksOverrides StepName. ReturnsThe step name.

### StepName

Gets the name of the step.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override string StepName { get; }

#### Remarks

Overrides [StepName](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-stepname.html).

#### Returns

The step name.

Parent topic:

SendWorkspaceToolMessageStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-timeout.html language=enus -->
## TOPIC 01615: Timeout

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-timeout.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-timeout.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the amount of time in milliseconds to wait for a response from the Workspace tool before timing out. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic uint Timeout { get; set; }ReturnsThe timeout, in milliseconds.

### Timeout

Gets or sets the amount of time in milliseconds to wait for a response from the Workspace tool before timing out.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public uint Timeout { get; set; }

#### Returns

The timeout, in milliseconds.

Parent topic:

SendWorkspaceToolMessageStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-workspacetoolpath.html language=enus -->
## TOPIC 01616: WorkspaceToolPath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-workspacetoolpath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep-workspacetoolpath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the path to the Workspace tool VI. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string WorkspaceToolPath { get; set; }ReturnsThe path to the VI.

### WorkspaceToolPath

Gets or sets the path to the Workspace tool VI.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string WorkspaceToolPath { get; set; }

#### Returns

The path to the VI.

Parent topic:

SendWorkspaceToolMessageStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep.html language=enus -->
## TOPIC 01617: SendWorkspaceToolMessageStep Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-sendworkspacetoolmessagestep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Send Workspace Tool Message step. This step sends an open Workspace tool VI a specified message or command, as well as data required by the case in the tool that handles the command. Derives fromActionStepSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic

### SendWorkspaceToolMessageStep Class

Represents a **Send Workspace Tool Message** step. This step sends an open Workspace tool VI a specified message or command, as well as data required by the case in the tool that handles the command.

#### Derives from

- ActionStep

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class SendWorkspaceToolMessageStep : ActionStep

#### Remarks

Note

The Workspace tool must be capable of receiving commands. Typically, this means the tool VI must have a case that handles the command.

**Accessing this Class:**

- SendWorkspaceToolMessageStep Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SendWorkspaceToolMessageStep(SendWorkspaceToolMessageStep) | Initializes a new instance of SendWorkspaceToolMessageStep by copying an existing instance. |
| SendWorkspaceToolMessageStep() | Initializes a new instance of SendWorkspaceToolMessageStep. |
| SendWorkspaceToolMessageStep(string, string, string, uint) | Initializes a new instance of SendWorkspaceToolMessageStep for the tool at workspaceToolPath with the specified command , data , and timeout . |

#### Properties

| Name | Description |
| --- | --- |
| Command | Gets or sets the message or command sent to the tool. |
| Data | Gets or sets any data required by the case of the Workspace tool that handles the Command. |
| StepName | Gets the name of the step. |
| Timeout | Gets or sets the amount of time in milliseconds to wait for a response from the Workspace tool before timing out. |
| WorkspaceToolPath | Gets or sets the path to the Workspace tool VI. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-setupstepgroup-setupstepgroup.html language=enus -->
## TOPIC 01618: SetupStepGroup()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-setupstepgroup-setupstepgroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-setupstepgroup-setupstepgroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SetupStepGroup. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic SetupStepGroup()RemarksThis constructor sets GroupName to "Group".

### SetupStepGroup()

Initializes a new instance of [SetupStepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-setupstepgroup.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public SetupStepGroup()

#### Remarks

This constructor sets [GroupName](nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup-groupname.html) to "Group".

Parent topic:

SetupStepGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-setupstepgroup-setupstepgroup__setupstepgroup.html language=enus -->
## TOPIC 01619: SetupStepGroup(SetupStepGroup)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-setupstepgroup-setupstepgroup__setupstepgroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-setupstepgroup-setupstepgroup__setupstepgroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SetupStepGroup by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic SetupStepGroup(SetupStepGroup node)ParametersNameTypeDescriptionnodeSetupStepGroupThe instance of SetupStepGroup to copy.

### SetupStepGroup(SetupStepGroup)

Initializes a new instance of [SetupStepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-setupstepgroup.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public SetupStepGroup(SetupStepGroup node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | SetupStepGroup | The instance of SetupStepGroup to copy. |

Parent topic:

SetupStepGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-setupstepgroup-setupstepgroup__string.html language=enus -->
## TOPIC 01620: SetupStepGroup(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-setupstepgroup-setupstepgroup__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-setupstepgroup-setupstepgroup__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SetupStepGroup and assigns the group the specified groupName . SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic SetupStepGroup(string groupName)ParametersNameTypeDescriptiongroupNamestringThe name of the step group.

### SetupStepGroup(string)

Initializes a new instance of [SetupStepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-setupstepgroup.html) and assigns the group the specified *groupName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public SetupStepGroup(string groupName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| groupName | string | The name of the step group. |

Parent topic:

SetupStepGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-setupstepgroup.html language=enus -->
## TOPIC 01621: SetupStepGroup Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-setupstepgroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-setupstepgroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Setup, or initialization, section of the stimulus profile code. This section is a StepGroup that contains all the steps you want to execute before the MainStepGroup begins executing. Derives fromStepGroupSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic

### SetupStepGroup Class

Represents the **Setup**, or initialization, section of the stimulus profile code. This section is a [StepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup.html) that contains all the steps you want to execute before the [MainStepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-mainstepgroup.html) begins executing.

#### Derives from

- StepGroup

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class SetupStepGroup : StepGroup

#### Remarks

Use the members of this class to get and set information about the step group.

**Accessing this Class:**

- SetupStepGroup Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SetupStepGroup(string) | Initializes a new instance of SetupStepGroup and assigns the group the specified groupName . |
| SetupStepGroup(SetupStepGroup) | Initializes a new instance of SetupStepGroup by copying an existing instance. |
| SetupStepGroup() | Initializes a new instance of SetupStepGroup. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-addchannelgroup__logchannelgroup.html language=enus -->
## TOPIC 01622: AddChannelGroup(LogChannelGroup)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-addchannelgroup__logchannelgroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-addchannelgroup__logchannelgroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified channelGroup to the StartLoggingStep. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic void AddChannelGroup(LogChannelGroup channelGroup)ParametersNameTypeDescriptionchannelGroupLogChannelGroupThe channel group to add.

### AddChannelGroup(LogChannelGroup)

Adds the specified *channelGroup*  to the [StartLoggingStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public void AddChannelGroup(LogChannelGroup channelGroup)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelGroup | LogChannelGroup | The channel group to add. |

Parent topic:

StartLoggingStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-channelgroups.html language=enus -->
## TOPIC 01623: ChannelGroups

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-channelgroups.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-channelgroups.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the groups of channels to log data for when the StartLoggingStep executes or the TriggerCondition is met. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic LogChannelGroup[] ChannelGroups { get; set; }ReturnsAn array of LogChannelGroup objects.

### ChannelGroups

Gets or sets the groups of channels to log data for when the [StartLoggingStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep.html) executes or the [TriggerCondition](nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-triggercondition.html) is met.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public [LogChannelGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup.html)[] ChannelGroups { get; set; }

#### Returns

An array of [LogChannelGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-logchannelgroup.html) objects.

Parent topic:

StartLoggingStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-checkforerrors.html language=enus -->
## TOPIC 01624: CheckForErrors()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-checkforerrors.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-checkforerrors.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override CompilationEvent[] CheckForErrors()RemarksOverrides CheckForErrors. ReturnsAn arra

### CheckForErrors()

Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html)[] CheckForErrors()

#### Remarks

Overrides [CheckForErrors](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-checkforerrors.html).

#### Returns

An array of [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html) objects that represent the errors, warnings, and messages generated by the step.

Parent topic:

StartLoggingStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-configurationname.html language=enus -->
## TOPIC 01625: ConfigurationName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-configurationname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-configurationname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the logging configuration, which you can use to control data logging after it starts. For example, you can pass this value to a StopLoggingStep to stop logging. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string ConfigurationName { get;

### ConfigurationName

Gets or sets the name of the logging configuration, which you can use to control data logging after it starts. For example, you can pass this value to a [StopLoggingStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-stoploggingstep.html) to stop logging.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string ConfigurationName { get; set; }

#### Returns

The logging configuration name.

Parent topic:

StartLoggingStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-filepath.html language=enus -->
## TOPIC 01626: FilePath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-filepath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-filepath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the path to the log file to save data to. The Stimulus Profile Editor creates log files in the TDMS file format. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string FilePath { get; set; }ReturnsThe path to the log file (.tdms) on disk.

### FilePath

Gets or sets the path to the log file to save data to. The Stimulus Profile Editor creates log files in the TDMS file format.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string FilePath { get; set; }

#### Returns

The path to the log file (.tdms) on disk.

Parent topic:

StartLoggingStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-highlimit.html language=enus -->
## TOPIC 01627: HighLimit

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-highlimit.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-highlimit.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the high limit used when TriggerCondition is in_limits or out_of_limits. The value of TriggerChannel must be less than or equal to this value and greater than or equal to LowLimit to be considered within limits. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApi

### HighLimit

Gets or sets the high limit used when [TriggerCondition](nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-triggercondition.html) is in_limits or out_of_limits. The value of [TriggerChannel](nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-triggerchannel.html) must be less than or equal to this value and greater than or equal to [LowLimit](nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-lowlimit.html) to be considered within limits.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public double HighLimit { get; set; }

#### Returns

The high limit.

Parent topic:

StartLoggingStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-logfilesegmentingoptions.html language=enus -->
## TOPIC 01628: LogFileSegmentingOptions

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-logfilesegmentingoptions.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-logfilesegmentingoptions.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether and how to segment the log file. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic LogFileSegmentingOptions LogFileSegmentingOptions { get; set; }ReturnsAn enumeration of LogFileSegmentingOptions. The default value is DoNotSegme

### LogFileSegmentingOptions

Gets or sets a value indicating whether and how to segment the log file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public [LogFileSegmentingOptions](nationalinstruments-veristand-stimulusprofiledefinitionapi-logfilesegmentingoptions.html) LogFileSegmentingOptions { get; set; }

#### Returns

An enumeration of [LogFileSegmentingOptions](nationalinstruments-veristand-stimulusprofiledefinitionapi-logfilesegmentingoptions.html). The default value is [DoNotSegment](nationalinstruments-veristand-stimulusprofiledefinitionapi-logfilesegmentingoptions.html).

Parent topic:

StartLoggingStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-lowlimit.html language=enus -->
## TOPIC 01629: LowLimit

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-lowlimit.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-lowlimit.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the low limit used when TriggerCondition is in_limits or out_of_limits. The value of TriggerChannel must be greater than or equal to this value and less than or equal to HighLimit to be considered within limits. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApi

### LowLimit

Gets or sets the low limit used when [TriggerCondition](nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-triggercondition.html) is in_limits or out_of_limits. The value of [TriggerChannel](nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-triggerchannel.html) must be greater than or equal to this value and less than or equal to [HighLimit](nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-highlimit.html) to be considered within limits.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public double LowLimit { get; set; }

#### Returns

The low limit.

Parent topic:

StartLoggingStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-posttriggerduration.html language=enus -->
## TOPIC 01630: PostTriggerDuration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-posttriggerduration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-posttriggerduration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the duration in seconds to continue logging data after a stop trigger occurs. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic double PostTriggerDuration { get; set; }ReturnsThe duration in seconds to continue logging data after a stop

### PostTriggerDuration

Gets or sets a value indicating the duration in seconds to continue logging data after a stop trigger occurs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public double PostTriggerDuration { get; set; }

#### Returns

The duration in seconds to continue logging data after a stop trigger occurs. The default value is 0.

Parent topic:

StartLoggingStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-pretriggerduration.html language=enus -->
## TOPIC 01631: PreTriggerDuration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-pretriggerduration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-pretriggerduration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the number of seconds of data to retain in the buffer in case a start trigger occurs. When the start trigger occurs, any buffered data is included in the log. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic double PreTriggerDuration {

### PreTriggerDuration

Gets or sets a value indicating the number of seconds of data to retain in the buffer in case a start trigger occurs. When the start trigger occurs, any buffered data is included in the log.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public double PreTriggerDuration { get; set; }

#### Returns

The number of seconds of data to retain in the buffer in case a start trigger occurs. The default value is 0.

Parent topic:

StartLoggingStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-rate.html language=enus -->
## TOPIC 01632: Rate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-rate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-rate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the rate in hertz at which data is logged. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic double Rate { get; set; }ReturnsThe logging rate, in hertz.

### Rate

Gets or sets the rate in hertz at which data is logged.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public double Rate { get; set; }

#### Returns

The logging rate, in hertz.

Parent topic:

StartLoggingStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-removechannelgroup__string.html language=enus -->
## TOPIC 01633: RemoveChannelGroup(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-removechannelgroup__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-removechannelgroup__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes the specified channelGroupName from the StartLoggingStep. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic void RemoveChannelGroup(string channelGroupName)ParametersNameTypeDescriptionchannelGroupNamestringThe channel group to remove.

### RemoveChannelGroup(string)

Removes the specified *channelGroupName*  from the [StartLoggingStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public void RemoveChannelGroup(string channelGroupName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelGroupName | string | The channel group to remove. |

Parent topic:

StartLoggingStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-replacefile.html language=enus -->
## TOPIC 01634: ReplaceFile

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-replacefile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-replacefile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether NI VeriStand overwrites an existing log file if a new logging operation with the same FilePath starts. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic bool ReplaceFile { get; set; }Returnstrue to overwrite an existing log file. false to append d

### ReplaceFile

Gets or sets whether NI VeriStand overwrites an existing log file if a new logging operation with the same [FilePath](nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-filepath.html) starts.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public bool ReplaceFile { get; set; }

#### Returns

true to overwrite an existing log file. false to append data to the end of the existing log file.

Parent topic:

StartLoggingStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-size.html language=enus -->
## TOPIC 01635: Size

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-size.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-size.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the maximum size of a log file segment, in bytes. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic ulong Size { get; set; }ReturnsThe maximum size of a log file segment in bytes. The default value is 10 million bytes.

### Size

Gets or sets a value indicating the maximum size of a log file segment, in bytes.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public ulong Size { get; set; }

#### Returns

The maximum size of a log file segment in bytes. The default value is 10 million bytes.

Parent topic:

StartLoggingStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-startloggingstep.html language=enus -->
## TOPIC 01636: StartLoggingStep()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-startloggingstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-startloggingstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of StartLoggingStep. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic StartLoggingStep()RemarksThis constructor sets ConfigurationName to "Log Configuration", FilePath to "Log File.tdms", and Rate to 100 Hz.

### StartLoggingStep()

Initializes a new instance of [StartLoggingStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public StartLoggingStep()

#### Remarks

This constructor sets [ConfigurationName](nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-configurationname.html) to "Log Configuration", [FilePath](nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-filepath.html) to "Log File.tdms", and [Rate](nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-rate.html) to 100 Hz.

Parent topic:

StartLoggingStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-startloggingstep__startloggingstep.html language=enus -->
## TOPIC 01637: StartLoggingStep(StartLoggingStep)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-startloggingstep__startloggingstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-startloggingstep__startloggingstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of StartLoggingStep by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic StartLoggingStep(StartLoggingStep node)ParametersNameTypeDescriptionnodeStartLoggingStepThe instance of StartLoggingStep to copy.

### StartLoggingStep(StartLoggingStep)

Initializes a new instance of [StartLoggingStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public StartLoggingStep(StartLoggingStep node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | StartLoggingStep | The instance of StartLoggingStep to copy. |

Parent topic:

StartLoggingStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-startloggingstep__string-string-double.html language=enus -->
## TOPIC 01638: StartLoggingStep(string, string, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-startloggingstep__string-string-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-startloggingstep__string-string-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of StartLoggingStep that uses the specified configurationName to log data to the file at filePath at the specified rate . SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic StartLoggingStep(string configurationName, string filePath, double ra

### StartLoggingStep(string, string, double)

Initializes a new instance of [StartLoggingStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep.html) that uses the specified *configurationName*  to log data to the file at *filePath*  at the specified *rate* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public StartLoggingStep(string configurationName, string filePath, double rate)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| configurationName | string | The name of the logging configuration, which you can use to control data logging after it starts. |
| filePath | string | The path to the log file (.tdms) on disk. |
| rate | double | The rate in hertz at which to log data. |

Parent topic:

StartLoggingStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-stepname.html language=enus -->
## TOPIC 01639: StepName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-stepname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-stepname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the step. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override string StepName { get; }RemarksOverrides StepName. ReturnsThe step name.

### StepName

Gets the name of the step.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override string StepName { get; }

#### Remarks

Overrides [StepName](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-stepname.html).

#### Returns

The step name.

Parent topic:

StartLoggingStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-timestampfile.html language=enus -->
## TOPIC 01640: TimestampFile

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-timestampfile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-timestampfile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether a timestamp is appended to the log file name when logging begins. The timestamp contains the month, day, year, hour, minute and second at which logging begins. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic bool TimestampFile { get; set; }Retur

### TimestampFile

Gets or sets whether a timestamp is appended to the log file name when logging begins. The timestamp contains the month, day, year, hour, minute and second at which logging begins.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public bool TimestampFile { get; set; }

#### Returns

true to append a timestamp to the file name.

Parent topic:

StartLoggingStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-triggerchannel.html language=enus -->
## TOPIC 01641: TriggerChannel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-triggerchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-triggerchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the channel to watch for the TriggerCondition. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic SystemDefinitionChannelResource TriggerChannel { get; set; }ReturnsA SystemDefinitionChannelResource object.

### TriggerChannel

Gets or sets the channel to watch for the [TriggerCondition](nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-triggercondition.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public [SystemDefinitionChannelResource](nationalinstruments-veristand-data-systemdefinitionchannelresource.html) TriggerChannel { get; set; }

#### Returns

A [SystemDefinitionChannelResource](nationalinstruments-veristand-data-systemdefinitionchannelresource.html) object.

Parent topic:

StartLoggingStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-triggercondition.html language=enus -->
## TOPIC 01642: TriggerCondition

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-triggercondition.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-triggercondition.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a trigger condition to use to start data logging. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic trigger TriggerCondition { get; set; }ReturnsAn enumeration of trigger.

### TriggerCondition

Gets or sets a trigger condition to use to start data logging.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public [trigger](nationalinstruments-veristand-clientapi-loginfo-trigger.html) TriggerCondition { get; set; }

#### Returns

An enumeration of [trigger](nationalinstruments-veristand-clientapi-loginfo-trigger.html).

Parent topic:

StartLoggingStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep.html language=enus -->
## TOPIC 01643: StartLoggingStep Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Start Logging step, which starts logging data from a specified set of channels to a TDMS file. Derives fromActionStepSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic class StartLoggingStep : ActionStepRemarksUse the members of this class to configure the

### StartLoggingStep Class

Represents a Start Logging step, which starts logging data from a specified set of channels to a TDMS file.

#### Derives from

- ActionStep

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class StartLoggingStep : ActionStep

#### Remarks

Use the members of this class to configure the logging operation, including the channels to log and optionally a trigger condition to use to start logging.

**Accessing this Class:**

- StartLoggingStep Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| StartLoggingStep(string, string, double) | Initializes a new instance of StartLoggingStep that uses the specified configurationName to log data to the file at filePath at the specified rate . |
| StartLoggingStep(StartLoggingStep) | Initializes a new instance of StartLoggingStep by copying an existing instance. |
| StartLoggingStep() | Initializes a new instance of StartLoggingStep. |

#### Properties

| Name | Description |
| --- | --- |
| ChannelGroups | Gets or sets the groups of channels to log data for when the StartLoggingStep executes or the TriggerCondition is met. |
| ConfigurationName | Gets or sets the name of the logging configuration, which you can use to control data logging after it starts. For example, you can pass this value to a StopLoggingStep to stop logging. |
| FilePath | Gets or sets the path to the log file to save data to. The Stimulus Profile Editor creates log files in the TDMS file format. |
| HighLimit | Gets or sets the high limit used when TriggerCondition is in_limits or out_of_limits. The value of TriggerChannel must be less than or equal to this value and greater than or equal to LowLimit to be considered within limits. |
| LogFileSegmentingOptions | Gets or sets a value indicating whether and how to segment the log file. |
| LowLimit | Gets or sets the low limit used when TriggerCondition is in_limits or out_of_limits. The value of TriggerChannel must be greater than or equal to this value and less than or equal to HighLimit to be considered within limits. |
| PostTriggerDuration | Gets or sets a value indicating the duration in seconds to continue logging data after a stop trigger occurs. |
| PreTriggerDuration | Gets or sets a value indicating the number of seconds of data to retain in the buffer in case a start trigger occurs. When the start trigger occurs, any buffered data is included in the log. |
| Rate | Gets or sets the rate in hertz at which data is logged. |
| ReplaceFile | Gets or sets whether NI VeriStand overwrites an existing log file if a new logging operation with the same FilePath starts. |
| Size | Gets or sets a value indicating the maximum size of a log file segment, in bytes. |
| StepName | Gets the name of the step. |
| TimestampFile | Gets or sets whether a timestamp is appended to the log file name when logging begins. The timestamp contains the month, day, year, hour, minute and second at which logging begins. |
| TriggerChannel | Gets or sets the channel to watch for the TriggerCondition. |
| TriggerCondition | Gets or sets a trigger condition to use to start data logging. |

#### Methods

| Name | Description |
| --- | --- |
| AddChannelGroup(LogChannelGroup) | Adds the specified channelGroup to the StartLoggingStep. |
| CheckForErrors() | Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. |
| RemoveChannelGroup(string) | Removes the specified channelGroupName from the StartLoggingStep. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stepexecutionstate.html language=enus -->
## TOPIC 01644: StepExecutionState Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stepexecutionstate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stepexecutionstate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current execution state of a step in a stimulus profile. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic enum StepExecutionStateMembersNameValueDescriptionIdleThe step is idle. InitializingThe step is initializing. RunningThe step is running. PausedThe

### StepExecutionState Enumeration

Specifies the current execution state of a step in a stimulus profile.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public enum StepExecutionState

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Idle |  | The step is idle. |
| Initializing |  | The step is initializing. |
| Running |  | The step is running. |
| Paused |  | The step is paused. |
| Finalizing |  | The step is finalizing execution. |
| Complete |  | Step execution is complete. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup-checkforerrors.html language=enus -->
## TOPIC 01645: CheckForErrors()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup-checkforerrors.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup-checkforerrors.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override CompilationEvent[] CheckForErrors()RemarksOverrides CheckForErrors. ReturnsAn arra

### CheckForErrors()

Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html)[] CheckForErrors()

#### Remarks

Overrides [CheckForErrors](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-checkforerrors.html).

#### Returns

An array of [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html) objects that represent the errors, warnings, and messages generated by the step.

Parent topic:

StepGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup-groupname.html language=enus -->
## TOPIC 01646: GroupName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup-groupname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup-groupname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the step group. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string GroupName { get; set; }ReturnsThe name of the group.

### GroupName

Gets or sets the name of the step group.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string GroupName { get; set; }

#### Returns

The name of the group.

Parent topic:

StepGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup-stepgroup.html language=enus -->
## TOPIC 01647: StepGroup()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup-stepgroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup-stepgroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of StepGroup. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic StepGroup()RemarksThis constructor sets GroupName to "Group".

### StepGroup()

Initializes a new instance of [StepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public StepGroup()

#### Remarks

This constructor sets [GroupName](nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup-groupname.html) to "Group".

Parent topic:

StepGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup-stepgroup__stepgroup.html language=enus -->
## TOPIC 01648: StepGroup(StepGroup)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup-stepgroup__stepgroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup-stepgroup__stepgroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of StepGroup by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic StepGroup(StepGroup node)ParametersNameTypeDescriptionnodeStepGroupThe instance of StepGroup to copy.

### StepGroup(StepGroup)

Initializes a new instance of [StepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public StepGroup(StepGroup node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | StepGroup | The instance of StepGroup to copy. |

Parent topic:

StepGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup-stepgroup__string.html language=enus -->
## TOPIC 01649: StepGroup(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup-stepgroup__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup-stepgroup__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of StepGroup and assigns the group the specified groupName . SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic StepGroup(string groupName)ParametersNameTypeDescriptiongroupNamestringThe name of the step group.

### StepGroup(string)

Initializes a new instance of [StepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup.html) and assigns the group the specified *groupName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public StepGroup(string groupName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| groupName | string | The name of the step group. |

Parent topic:

StepGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup-stepname.html language=enus -->
## TOPIC 01650: StepName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup-stepname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup-stepname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the step, which for step groups is also the GroupName. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override string StepName { get; }RemarksOverrides StepName. ReturnsThe step name.

### StepName

Gets the name of the step, which for step groups is also the [GroupName](nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup-groupname.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override string StepName { get; }

#### Remarks

Overrides [StepName](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-stepname.html).

#### Returns

The step name.

Parent topic:

StepGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup-steps.html language=enus -->
## TOPIC 01651: Steps

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup-steps.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup-steps.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the steps that belong to the current step group. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic ActionStep[] Steps { get; set; }ReturnsAn array of ActionStep objects.

### Steps

Gets or sets the steps that belong to the current step group.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public [ActionStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep.html)[] Steps { get; set; }

#### Returns

An array of [ActionStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep.html) objects.

Parent topic:

StepGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup.html language=enus -->
## TOPIC 01652: StepGroup Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a group of steps in a stimulus profile. Derives fromActionStepSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic class StepGroup : ActionStepRemarksThis is a base class from which all step group types inherit. You can use step groups to organize steps in log

### StepGroup Class

Represents a group of steps in a stimulus profile.

#### Derives from

- ActionStep

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class StepGroup : ActionStep

#### Remarks

This is a base class from which all step group types inherit. You can use step groups to organize steps in logical chunks. Use the members of this class to get and set information about the group, including its name and the steps it contains.

**Accessing this Class:**

- StepGroup Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| StepGroup() | Initializes a new instance of StepGroup. |
| StepGroup(string) | Initializes a new instance of StepGroup and assigns the group the specified groupName . |
| StepGroup(StepGroup) | Initializes a new instance of StepGroup by copying an existing instance. |

#### Properties

| Name | Description |
| --- | --- |
| GroupName | Gets or sets the name of the step group. |
| StepName | Gets the name of the step, which for step groups is also the GroupName. |
| Steps | Gets or sets the steps that belong to the current step group. |

#### Methods

| Name | Description |
| --- | --- |
| CheckForErrors() | Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stepresult.html language=enus -->
## TOPIC 01653: StepResult Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stepresult.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stepresult.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the result of executing a stimulus profile step. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic enum StepResultMembersNameValueDescriptionNotExecuted0The step has not been executed. Aborted1The step was aborted. Failed2The step failed. Passed3The step pas

### StepResult Enumeration

Indicates the result of executing a stimulus profile step.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public enum StepResult

#### Members

| Name | Value | Description |
| --- | --- | --- |
| NotExecuted | 0 | The step has not been executed. |
| Aborted | 1 | The step was aborted. |
| Failed | 2 | The step failed. |
| Passed | 3 | The step passed. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-abort.html language=enus -->
## TOPIC 01654: Abort()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-abort.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-abort.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Immediately terminates the execution of the stimulus profile, without executing any clean up-tasks. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic void Abort()RemarksUse the Stop method to execute clean-up tasks before terminating stimulus profile execution.

### Abort()

Immediately terminates the execution of the stimulus profile, without executing any clean up-tasks.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public void Abort()

#### Remarks

Use the [Stop](nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-stop.html) method to execute clean-up tasks before terminating stimulus profile execution.

Parent topic:

StimulusProfile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-checkforerrors.html language=enus -->
## TOPIC 01655: CheckForErrors()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-checkforerrors.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-checkforerrors.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs checks on the stimulus profile and returns any errors, warnings, or messages that are relevant to the stimulus profile's current configuration. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic CompilationEvent[] CheckForErrors()ReturnsAn array of Compilation

### CheckForErrors()

Performs checks on the stimulus profile and returns any errors, warnings, or messages that are relevant to the stimulus profile's current configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html)[] CheckForErrors()

#### Returns

An array of [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html) objects that represent the errors, warnings, and messages generated by the stimulus profile.

Parent topic:

StimulusProfile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-cleanup.html language=enus -->
## TOPIC 01656: CleanUp

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-cleanup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-cleanup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the CleanupStepGroup for the stimulus profile, which contains the finalization section of stimulus profile code. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic CleanupStepGroup CleanUp { get; set; }ReturnsA CleanupStepGroup object.

### CleanUp

Gets or sets the [CleanupStepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-cleanupstepgroup.html) for the stimulus profile, which contains the finalization section of stimulus profile code.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public [CleanupStepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-cleanupstepgroup.html) CleanUp { get; set; }

#### Returns

A [CleanupStepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-cleanupstepgroup.html) object.

Parent topic:

StimulusProfile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-continue.html language=enus -->
## TOPIC 01657: Continue()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-continue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-continue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Continues the execution of the stimulus profile if it was previously paused. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic void Continue()

### Continue()

Continues the execution of the stimulus profile if it was previously paused.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public void Continue()

Parent topic:

StimulusProfile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-executeasync__string-string.html language=enus -->
## TOPIC 01658: ExecuteAsync(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-executeasync__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-executeasync__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Starts executing the stimulus profile asynchronously, or in a separate VeriStand Engine loop from the Primary Control Loop. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic void ExecuteAsync(string gatewayIP, string uutSerialNumber)ParametersNameTypeDescriptiongatewa

### ExecuteAsync(string, string)

Starts executing the stimulus profile asynchronously, or in a separate VeriStand Engine loop from the Primary Control Loop.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public void ExecuteAsync(string gatewayIP, string uutSerialNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| gatewayIP | string | The IP address of the VeriStand Gateway to connect to when executing the project. |
| uutSerialNumber | string | The serial number of the unit under test. If this string is empty, a default value appears in the results file. |

Parent topic:

StimulusProfile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-executecompleted.html language=enus -->
## TOPIC 01659: ExecuteCompleted

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-executecompleted.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-executecompleted.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Occurs when the stimulus profile completes execution. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic EventHandler< ExecuteCompletedEventArgs > ExecuteCompleted

### ExecuteCompleted

Occurs when the stimulus profile completes execution.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public EventHandler< [ExecuteCompletedEventArgs](nationalinstruments-veristand-stimulusprofiledefinitionapi-executecompletedeventargs.html) > ExecuteCompleted

Parent topic:

StimulusProfile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-main.html language=enus -->
## TOPIC 01660: Main

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-main.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-main.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the MainStepGroup for the stimulus profile, which contains the main execution code of the stimulus profile. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic MainStepGroup Main { get; set; }ReturnsA MainStepGroup object.

### Main

Gets or sets the [MainStepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-mainstepgroup.html) for the stimulus profile, which contains the main execution code of the stimulus profile.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public [MainStepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-mainstepgroup.html) Main { get; set; }

#### Returns

A [MainStepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-mainstepgroup.html) object.

Parent topic:

StimulusProfile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-pause.html language=enus -->
## TOPIC 01661: Pause()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-pause.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-pause.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Pauses the execution of the stimulus profile. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic void Pause()RemarksUse the Continue method to resume execution after a pause.

### Pause()

Pauses the execution of the stimulus profile.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public void Pause()

#### Remarks

Use the [Continue](nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-continue.html) method to resume execution after a pause.

Parent topic:

StimulusProfile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-progresschanged.html language=enus -->
## TOPIC 01662: ProgressChanged

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-progresschanged.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-progresschanged.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Occurs when the progress of the stimulus profile execution changes, such as when a new step begins executing. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic EventHandler< ExecuteProgressChangedEventArgs > ProgressChanged

### ProgressChanged

Occurs when the progress of the stimulus profile execution changes, such as when a new step begins executing.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public EventHandler< [ExecuteProgressChangedEventArgs](nationalinstruments-veristand-stimulusprofiledefinitionapi-executeprogresschangedeventargs.html) > ProgressChanged

Parent topic:

StimulusProfile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-resultsdirectory.html language=enus -->
## TOPIC 01663: ResultsDirectory

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-resultsdirectory.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-resultsdirectory.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the path to the folder on disk where test result data is stored. When a stimulus profile finishes executing, NI VeriStand generates an XML file with the results of the test and saves it in this folder. The file adheres to the Automatic Test Markup Language (ATML) standard. SyntaxNamespace: Nati

### ResultsDirectory

Gets the path to the folder on disk where test result data is stored. When a stimulus profile finishes executing, NI VeriStand generates an XML file with the results of the test and saves it in this folder. The file adheres to the Automatic Test Markup Language (ATML) standard.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string ResultsDirectory { get; set; }

#### Returns

The path to the results directory.

Parent topic:

StimulusProfile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-savestimulusprofile__string.html language=enus -->
## TOPIC 01664: SaveStimulusProfile(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-savestimulusprofile__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-savestimulusprofile__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the stimulus profile file with the name and to the location specified by file . SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic void SaveStimulusProfile(string file)ParametersNameTypeDescriptionfilestringThe name of the stimulus profile file. This can be a ful

### SaveStimulusProfile(string)

Saves the stimulus profile file with the name and to the location specified by *file* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public void SaveStimulusProfile(string file)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| file | string | The name of the stimulus profile file. This can be a fully qualified or relative path, including the file name. |

Parent topic:

StimulusProfile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-setup.html language=enus -->
## TOPIC 01665: Setup

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-setup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-setup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the SetupStepGroup for the stimulus profile, which contains the initialization section of stimulus profile code. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic SetupStepGroup Setup { get; set; }ReturnsA SetupStepGroup object.

### Setup

Gets or sets the [SetupStepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-setupstepgroup.html) for the stimulus profile, which contains the initialization section of stimulus profile code.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public [SetupStepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-setupstepgroup.html) Setup { get; set; }

#### Returns

A [SetupStepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-setupstepgroup.html) object.

Parent topic:

StimulusProfile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-state.html language=enus -->
## TOPIC 01666: State

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-state.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-state.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the execution state of a step (Idle, Initializing, Running, and so on.) SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic StepExecutionState State { get; }ReturnsAn enumeration of StepExecutionState.

### State

Gets the execution state of a step (Idle, Initializing, Running, and so on.)

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public [StepExecutionState](nationalinstruments-veristand-stimulusprofiledefinitionapi-stepexecutionstate.html) State { get; }

#### Returns

An enumeration of [StepExecutionState](nationalinstruments-veristand-stimulusprofiledefinitionapi-stepexecutionstate.html).

Parent topic:

StimulusProfile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-stimulusprofile.html language=enus -->
## TOPIC 01667: StimulusProfile()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-stimulusprofile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-stimulusprofile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of StimulusProfile. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic StimulusProfile()

### StimulusProfile()

Initializes a new instance of [StimulusProfile](nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public StimulusProfile()

Parent topic:

StimulusProfile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-stimulusprofile__stimulusprofile.html language=enus -->
## TOPIC 01668: StimulusProfile(StimulusProfile)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-stimulusprofile__stimulusprofile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-stimulusprofile__stimulusprofile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of StimulusProfile by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic StimulusProfile(StimulusProfile node)RemarksThis constructor also copies the FileFormatVersion and Version values of the stimulus profile s

### StimulusProfile(StimulusProfile)

Initializes a new instance of [StimulusProfile](nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public StimulusProfile(StimulusProfile node)

#### Remarks

This constructor also copies the [FileFormatVersion](nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode-fileformatversion.html) and [Version](nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode-version.html) values of the stimulus profile specified by *node* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | StimulusProfile | The instance of StimulusProfile to copy. |

Parent topic:

StimulusProfile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-stimulusprofile__string.html language=enus -->
## TOPIC 01669: StimulusProfile(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-stimulusprofile__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-stimulusprofile__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of StimulusProfile for the file at the specified file path. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic StimulusProfile(string file)ParametersNameTypeDescriptionfilestringThe location of the stimulus profile file on disk.ExceptionsType

### StimulusProfile(string)

Initializes a new instance of [StimulusProfile](nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile.html) for the file at the specified *file*  path.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public StimulusProfile(string file)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| file | string | The location of the stimulus profile file on disk. |

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentNullException | file is null. |
| ArgumentException | file is an empty string |
| FileNotFoundException | file does not exist |
| DirectoryNotFoundException | Any of the directories in the file path do not exist |
| InvalidOperationException | file does not match the defined schema for a stimulus profile file. |

Parent topic:

StimulusProfile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-stop.html language=enus -->
## TOPIC 01670: Stop()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-stop.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-stop.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops the execution of the stimulus profile. Stopping execution causes the stimulus profile to jump to and execute the tasks in the CleanupStepGroup before terminating execution. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic void Stop()RemarksIf you stop execution

### Stop()

Stops the execution of the stimulus profile. Stopping execution causes the stimulus profile to jump to and execute the tasks in the [CleanupStepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-cleanupstepgroup.html) before terminating execution.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public void Stop()

#### Remarks

Note

If you stop execution of a stimulus profile that contains nested real-time sequences, the tasks in the [CleanUp](nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup.html) section of each sequence also execute before the stimulus profile is stopped.

Abort

Parent topic:

StimulusProfile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-stopexecutiononfail.html language=enus -->
## TOPIC 01671: StopExecutionOnFail

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-stopexecutiononfail.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-stopexecutiononfail.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether execution of the stimulus profile stops if a step fails. Stopping execution causes the stimulus profile to jump to and execute the tasks in the CleanupStepGroup before terminating execution. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic bool S

### StopExecutionOnFail

Gets or sets whether execution of the stimulus profile stops if a step fails. Stopping execution causes the stimulus profile to jump to and execute the tasks in the [CleanupStepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-cleanupstepgroup.html) before terminating execution.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public bool StopExecutionOnFail { get; set; }

#### Remarks

Note

If you stop execution of a stimulus profile that contains nested real-time sequences, the tasks in the [CleanUp](nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup.html) section of each sequence also execute before the stimulus profile is stopped.

#### Returns

true if execution stops if a step fails.

Parent topic:

StimulusProfile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile.html language=enus -->
## TOPIC 01672: StimulusProfile Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a stimulus profile. Derives fromRootNodeSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic class StimulusProfile : RootNodeRemarksA stimulus profile is a test executive that can call real-time sequences, open and close NI VeriStand projects, and perform data

### StimulusProfile Class

Represents a stimulus profile.

#### Derives from

- RootNode

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class StimulusProfile : RootNode

#### Remarks

A stimulus profile is a test executive that can call real-time sequences, open and close NI VeriStand projects, and perform data-logging and pass/fail analysis. It also connects real-time sequences to system definition files to bind channel data within the system definition file to variables in the real-time sequence. Stimulus profiles execute on the host computer.

Use the members of this class to access the steps a stimulus profile contains, control the execution of the stimulus profile, and track events that occur during execution.

**Accessing this Class:**

- StimulusProfile Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| StimulusProfile(StimulusProfile) | Initializes a new instance of StimulusProfile by copying an existing instance. |
| StimulusProfile() | Initializes a new instance of StimulusProfile. |
| StimulusProfile(string) | Initializes a new instance of StimulusProfile for the file at the specified file path. |

#### Properties

| Name | Description |
| --- | --- |
| CleanUp | Gets or sets the CleanupStepGroup for the stimulus profile, which contains the finalization section of stimulus profile code. |
| Main | Gets or sets the MainStepGroup for the stimulus profile, which contains the main execution code of the stimulus profile. |
| ResultsDirectory | Gets the path to the folder on disk where test result data is stored. When a stimulus profile finishes executing, NI VeriStand generates an XML file with the results of the test and saves it in this folder. The file adheres to the Automatic Test Markup Language (ATML) standard. |
| Setup | Gets or sets the SetupStepGroup for the stimulus profile, which contains the initialization section of stimulus profile code. |
| State | Gets the execution state of a step (Idle, Initializing, Running, and so on.) |
| StopExecutionOnFail | Gets or sets whether execution of the stimulus profile stops if a step fails. Stopping execution causes the stimulus profile to jump to and execute the tasks in the CleanupStepGroup before terminating execution. |

#### Methods

| Name | Description |
| --- | --- |
| Abort() | Immediately terminates the execution of the stimulus profile, without executing any clean up-tasks. |
| CheckForErrors() | Performs checks on the stimulus profile and returns any errors, warnings, or messages that are relevant to the stimulus profile's current configuration. |
| Continue() | Continues the execution of the stimulus profile if it was previously paused. |
| ExecuteAsync(string, string) | Starts executing the stimulus profile asynchronously, or in a separate VeriStand Engine loop from the Primary Control Loop. |
| Pause() | Pauses the execution of the stimulus profile. |
| SaveStimulusProfile(string) | Saves the stimulus profile file with the name and to the location specified by file . |
| Stop() | Stops the execution of the stimulus profile. Stopping execution causes the stimulus profile to jump to and execute the tasks in the CleanupStepGroup before terminating execution. |

#### Events

| Name | Description |
| --- | --- |
| ExecuteCompleted | Occurs when the stimulus profile completes execution. |
| ProgressChanged | Occurs when the progress of the stimulus profile execution changes, such as when a new step begins executing. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stoploggingstep-checkforerrors.html language=enus -->
## TOPIC 01673: CheckForErrors()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stoploggingstep-checkforerrors.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stoploggingstep-checkforerrors.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override CompilationEvent[] CheckForErrors()RemarksOverrides CheckForErrors. ReturnsAn arra

### CheckForErrors()

Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html)[] CheckForErrors()

#### Remarks

Overrides [CheckForErrors](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-checkforerrors.html).

#### Returns

An array of [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html) objects that represent the errors, warnings, and messages generated by the step.

Parent topic:

StopLoggingStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stoploggingstep-configurationname.html language=enus -->
## TOPIC 01674: ConfigurationName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stoploggingstep-configurationname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stoploggingstep-configurationname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the logging configuration, which you can use to control an active data logging operation. Use this property to specify the logging operation to stop. This value should match the ConfigurationName value for the operation. SyntaxNamespace: NationalInstruments.VeriStand.Stimulu

### ConfigurationName

Gets or sets the name of the logging configuration, which you can use to control an active data logging operation. Use this property to specify the logging operation to stop. This value should match the [ConfigurationName](nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-configurationname.html) value for the operation.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string ConfigurationName { get; set; }

#### Returns

The logging configuration name.

Parent topic:

StopLoggingStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stoploggingstep-stepname.html language=enus -->
## TOPIC 01675: StepName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stoploggingstep-stepname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stoploggingstep-stepname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the step. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override string StepName { get; }RemarksOverrides StepName. ReturnsThe step name.

### StepName

Gets the name of the step.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override string StepName { get; }

#### Remarks

Overrides [StepName](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-stepname.html).

#### Returns

The step name.

Parent topic:

StopLoggingStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stoploggingstep-stoploggingstep.html language=enus -->
## TOPIC 01676: StopLoggingStep()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stoploggingstep-stoploggingstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stoploggingstep-stoploggingstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of StopLoggingStep. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic StopLoggingStep()RemarksThis constructor sets ConfigurationName to "Log Configuration".

### StopLoggingStep()

Initializes a new instance of [StopLoggingStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-stoploggingstep.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public StopLoggingStep()

#### Remarks

This constructor sets [ConfigurationName](nationalinstruments-veristand-stimulusprofiledefinitionapi-stoploggingstep-configurationname.html) to "Log Configuration".

Parent topic:

StopLoggingStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stoploggingstep-stoploggingstep__stoploggingstep.html language=enus -->
## TOPIC 01677: StopLoggingStep(StopLoggingStep)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stoploggingstep-stoploggingstep__stoploggingstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stoploggingstep-stoploggingstep__stoploggingstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of StopLoggingStep by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic StopLoggingStep(StopLoggingStep node)ParametersNameTypeDescriptionnodeStopLoggingStepThe instance of StopLoggingStep to copy.

### StopLoggingStep(StopLoggingStep)

Initializes a new instance of [StopLoggingStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-stoploggingstep.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public StopLoggingStep(StopLoggingStep node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | StopLoggingStep | The instance of StopLoggingStep to copy. |

Parent topic:

StopLoggingStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stoploggingstep-stoploggingstep__string.html language=enus -->
## TOPIC 01678: StopLoggingStep(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stoploggingstep-stoploggingstep__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stoploggingstep-stoploggingstep__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of StopLoggingStep for the logging configuration with the specified configurationName . SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic StopLoggingStep(string configurationName)ParametersNameTypeDescriptionconfigurationNamestringThe config

### StopLoggingStep(string)

Initializes a new instance of [StopLoggingStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-stoploggingstep.html) for the logging configuration with the specified *configurationName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public StopLoggingStep(string configurationName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| configurationName | string | The configuration name of the logging operation to stop. |

Parent topic:

StopLoggingStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-stoploggingstep.html language=enus -->
## TOPIC 01679: StopLoggingStep Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-stoploggingstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-stoploggingstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Stop Logging step, which finalizes and stops a logging operation started by a StartLoggingStep. Derives fromActionStepSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic class StopLoggingStep : ActionStepRemarksUse the members of this class to configure the

### StopLoggingStep Class

Represents a Stop Logging step, which finalizes and stops a logging operation started by a [StartLoggingStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep.html).

#### Derives from

- ActionStep

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class StopLoggingStep : ActionStep

#### Remarks

Use the members of this class to configure the step and set the name of the logging configuration to stop.

**Accessing this Class:**

- StopLoggingStep Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| StopLoggingStep(string) | Initializes a new instance of StopLoggingStep for the logging configuration with the specified configurationName . |
| StopLoggingStep(StopLoggingStep) | Initializes a new instance of StopLoggingStep by copying an existing instance. |
| StopLoggingStep() | Initializes a new instance of StopLoggingStep. |

#### Properties

| Name | Description |
| --- | --- |
| ConfigurationName | Gets or sets the name of the logging configuration, which you can use to control an active data logging operation. Use this property to specify the logging operation to stop. This value should match the ConfigurationName value for the operation. |
| StepName | Gets the name of the step. |

#### Methods

| Name | Description |
| --- | --- |
| CheckForErrors() | Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-aliasfile.html language=enus -->
## TOPIC 01680: AliasFile

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-aliasfile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-aliasfile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the path to an alias file, which defines mappings for aliased parameter names in the source file specified by FilePath. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string AliasFile { get; set; }RemarksAlias files allow you to easily reuse the same s

### AliasFile

Gets or sets the path to an alias file, which defines mappings for aliased parameter names in the source file specified by [FilePath](nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-filepath.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string AliasFile { get; set; }

#### Remarks

Alias files allow you to easily reuse the same source file for multiple models. For example, you can write a source file with parameter names a, b, and c, and then use an alias file to map a, b, and c to parameters in the current model.

#### Returns

The path to an alias file. Alias files must be .txt files that use the same [Delimiter](nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-delimiter.html) as the source file.

Parent topic:

UpdateModelParametersFromFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-allowtemporaryvariables.html language=enus -->
## TOPIC 01681: AllowTemporaryVariables

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-allowtemporaryvariables.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-allowtemporaryvariables.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether to allow temporary variables in the source file specified by FilePath. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic bool AllowTemporaryVariables { get; set; }RemarksFor example, the following snippet defines a temporary var

### AllowTemporaryVariables

Gets or sets a value indicating whether to allow temporary variables in the source file specified by [FilePath](nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-filepath.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public bool AllowTemporaryVariables { get; set; }

#### Remarks

For example, the following snippet defines a temporary variable, *tempX*, and then uses *tempX* in an expression that defines a model parameter value:

tempX 0.5

{parameter} 10 * tempX

Note

If you enable this property, this step assumes any keys in the source file specified by [FilePath](nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-filepath.html) that do not exactly match a model parameter name or an alias defined in the [AliasFile](nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-aliasfile.html) are temporary variables. If true, you will not receive error messages for variables that do not map to model parameters. Instead, the step simply discards the corresponding value when updating model parameters. If true, this property also makes model parameter names and alias names case-sensitive.

#### Returns

true to allow temporary variables in the source file. The default value is false.

Parent topic:

UpdateModelParametersFromFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-checkforerrors.html language=enus -->
## TOPIC 01682: CheckForErrors()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-checkforerrors.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-checkforerrors.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override CompilationEvent[] CheckForErrors()RemarksOverrides CheckForErrors. ReturnsAn arra

### CheckForErrors()

Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html)[] CheckForErrors()

#### Remarks

Overrides [CheckForErrors](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-checkforerrors.html).

#### Returns

An array of [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html) objects that represent the errors, warnings, and messages generated by the step.

Parent topic:

UpdateModelParametersFromFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-delimiter.html language=enus -->
## TOPIC 01683: Delimiter

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-delimiter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-delimiter.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the delimiter used to separate model parameter names and values in the source file specified by FilePath and, if used, parameter aliases and names in the AliasFile. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic Delimiters Delimiter

### Delimiter

Gets or sets a value indicating the delimiter used to separate model parameter names and values in the source file specified by [FilePath](nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-filepath.html) and, if used, parameter aliases and names in the [AliasFile](nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-aliasfile.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public [Delimiters](nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-delimiters.html) Delimiter { get; set; }

#### Returns

An enumeration of [Delimiters](nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-delimiters.html).

Parent topic:

UpdateModelParametersFromFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-filepath.html language=enus -->
## TOPIC 01684: FilePath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-filepath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-filepath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the path to the text file that contains the new model parameter values. The source file contains a set of key/value pairs that represent model parameter names and the corresponding values to assign each parameter. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionA

### FilePath

Gets or sets the path to the text file that contains the new model parameter values. The source file contains a set of key/value pairs that represent model parameter names and the corresponding values to assign each parameter.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string FilePath { get; set; }

#### Remarks

This step also provides limited support for .m files that follow the exact format generated by the Model Parameter Manager workspace tool.

#### Returns

The path to the text file that contains the new model parameter values. This file must be a .txt file and must follow the expected model parameter file format. Refer to *Formatting a Model Parameter File* in the *NI VeriStand Help* for more information about the model parameter file format.

Parent topic:

UpdateModelParametersFromFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-stepname.html language=enus -->
## TOPIC 01685: StepName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-stepname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-stepname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override string StepName { get; }

### StepName

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override string StepName { get; }

Parent topic:

UpdateModelParametersFromFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-target.html language=enus -->
## TOPIC 01686: Target

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-target.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-target.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the target, as it appears in the system definition file, on which the model executes. This step can only update model parameters on one target at a time. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string Target { get; set; }ReturnsThe n

### Target

Gets or sets the name of the target, as it appears in the system definition file, on which the model executes. This step can only update model parameters on one target at a time.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string Target { get; set; }

#### Returns

The name of the target.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentNullException | The value is null or an empty string. |

Parent topic:

UpdateModelParametersFromFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-updatemodelparametersfromfile.html language=enus -->
## TOPIC 01687: UpdateModelParametersFromFile()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-updatemodelparametersfromfile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-updatemodelparametersfromfile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the UpdateModelParametersFromFile class. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic UpdateModelParametersFromFile()RemarksThis constructor sets Target to Controller and Delimiter to Tab.

### UpdateModelParametersFromFile()

Initializes a new instance of the [UpdateModelParametersFromFile](nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public UpdateModelParametersFromFile()

#### Remarks

This constructor sets [Target](nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-target.html) to Controller and [Delimiter](nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-delimiter.html) to Tab.

Parent topic:

UpdateModelParametersFromFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-updatemodelparametersfromfile__updatemodelparametersfromfile.html language=enus -->
## TOPIC 01688: UpdateModelParametersFromFile(UpdateModelParametersFromFile)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-updatemodelparametersfromfile__updatemodelparametersfromfile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile-updatemodelparametersfromfile__updatemodelparametersfromfile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the UpdateModelParametersFromFile class by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic UpdateModelParametersFromFile(UpdateModelParametersFromFile node)ParametersNameTypeDescriptionnodeUpdateModelParame

### UpdateModelParametersFromFile(UpdateModelParametersFromFile)

Initializes a new instance of the [UpdateModelParametersFromFile](nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile.html) class by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public UpdateModelParametersFromFile(UpdateModelParametersFromFile node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | UpdateModelParametersFromFile | The instance of UpdateModelParametersFromFile to copy. |

Parent topic:

UpdateModelParametersFromFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile.html language=enus -->
## TOPIC 01689: UpdateModelParametersFromFile Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-updatemodelparametersfromfile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an Update Model Parameters from File step, which updates parameter values for a simulation model to values specified in a text (.txt) file. Derives fromActionStepSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic class UpdateModelParametersFromFile : ActionS

### UpdateModelParametersFromFile Class

Represents an Update Model Parameters from File step, which updates parameter values for a simulation model to values specified in a text (.txt) file.

#### Derives from

- ActionStep

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class UpdateModelParametersFromFile : ActionStep

#### Remarks

By using this step to automate model parameter value updates, you can synchronize the updates with the execution of real-time sequences. This step removes the need to stop execution of a stimulus profile to update model parameter values.

**Accessing this Class:**

- UpdateModelParametersFromFile Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| UpdateModelParametersFromFile(UpdateModelParametersFromFile) | Initializes a new instance of the UpdateModelParametersFromFile class by copying an existing instance. |
| UpdateModelParametersFromFile() | Initializes a new instance of the UpdateModelParametersFromFile class. |

#### Properties

| Name | Description |
| --- | --- |
| AliasFile | Gets or sets the path to an alias file, which defines mappings for aliased parameter names in the source file specified by FilePath. |
| AllowTemporaryVariables | Gets or sets a value indicating whether to allow temporary variables in the source file specified by FilePath. |
| Delimiter | Gets or sets a value indicating the delimiter used to separate model parameter names and values in the source file specified by FilePath and, if used, parameter aliases and names in the AliasFile. |
| FilePath | Gets or sets the path to the text file that contains the new model parameter values. The source file contains a set of key/value pairs that represent model parameter names and the corresponding values to assign each parameter. |
| StepName |  |
| Target | Gets or sets the name of the target, as it appears in the system definition file, on which the model executes. This step can only update model parameters on one target at a time. |

#### Methods

| Name | Description |
| --- | --- |
| CheckForErrors() | Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-veristandprojectcommand.html language=enus -->
## TOPIC 01690: VeriStandProjectCommand Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-veristandprojectcommand.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-veristandprojectcommand.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the command that a SendProjectCommandStep sends to the active NI VeriStand project. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic enum VeriStandProjectCommandMembersNameValueDescriptionRunRun the project. DeployDeploys the system definition file associat

### VeriStandProjectCommand Enumeration

Specifies the command that a [SendProjectCommandStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-sendprojectcommandstep.html) sends to the active NI VeriStand project.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public enum VeriStandProjectCommand

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Run |  | Run the project. |
| Deploy |  | Deploys the system definition file associated with the project to the target. |
| Connect |  | Connects the project on the host computer to a target. This option only establishes a connection to a target. It does not deploy the system definition file. |
| Disconnect |  | Disconnects the project from the target. This option does not stop execution of the system definition file on the target. |
| Undeploy |  | Undeploys the system definition file associated with the project from the target. Undeploying the system definition file stops execution on the target. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi.html language=enus -->
## TOPIC 01691: NationalInstruments.VeriStand.StimulusProfileDefinitionApi

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionActionStepRepresents a step that performs an action, such as opening or closing a project, opening or closing the Workspace, or calling a real-time sequence. AlwaysPassEvaluationRepresents a pass/fail evaluation that always passes, regardless of the value being evaluated. You t

### NationalInstruments.VeriStand.StimulusProfileDefinitionApi

#### Classes

| Name | Description |
| --- | --- |
| ActionStep | Represents a step that performs an action, such as opening or closing a project, opening or closing the Workspace, or calling a real-time sequence. |
| AlwaysPassEvaluation | Represents a pass/fail evaluation that always passes, regardless of the value being evaluated. You typically use evaluations on the return value of a real-time sequence to determine if the sequence passes or fails. |
| BooleanEvaluation | Represents a Boolean pass/fail evaluation, where one value (usually true) indicates a pass and the other a fail. You typically use evaluations on the return value of a real-time sequence to determine if the sequence passes or fails. |
| CleanupStepGroup | Represents the Clean Up, or finalization, section of stimulus profile code. This section is a StepGroup that contains all the steps you want to execute after the MainStepGroup finishes. |
| CloseProjectStep | Represents a Close VeriStand Project step, which closes an open NI VeriStand project. |
| CloseWorkspaceStep | Represents a Close Workspace step, which closes the Workspace for the active and open NI VeriStand project. |
| CommandShell | Represents a Command Shell step, which invokes the Windows Command Prompt and calls the specified application with the specified arguments. |
| Evaluation | Represents a pass/fail evaluation performed on a value. You typically use evaluations on the return value of a real-time sequence to determine if the sequence passes or fails. |
| ExecuteCompletedEventArgs | Provides data for the ExecuteCompleted event. |
| ExecuteProgressChangedEventArgs | Provides data for the ProgressChanged event. |
| FTPBase | Provides an abstract base class for interacting with files on an FTP server. |
| FTPDownload | Represents an FTP Download step, which downloads files from an FTP server, such as an RT target. |
| FTPUpload | Represents an FTP Upload step, which uploads files to an FTP server, such as an RT target. |
| LaunchNIVeriStand | Represents a Launch NI VeriStand step, which launches the NI VeriStand executable. |
| LogChannelGroup | Represents a Channel Group, which contains channels in the system definition that you want to log from the stimulus profile. You can configure data logging by adding one or multiple channel groups to a StartLoggingStep. |
| MacroPlayerStep | Represents a Macro Player step, which replays a previously recorded NI VeriStand macro (.nivsmacro) file. |
| MainStepGroup | Represents the Main section of the stimulus profile code. This section is a StepGroup that contains the main execution code for the stimulus profile. Steps in this section execute after the SetupStepGroup and before the CleanupStepGroup. |
| MessageBoxStep | Represents a Message Box step, which displays a pop-dialog box with a specified message. |
| NumericBoundsEvaluation | Represents a NumericBounds pass/fail evaluation, which checks if a specified value falls within the bounds of a specified high and low limit. You typically use evaluations on the return value of a real-time sequence to determine if the sequence passes or fails. |
| OpenProjectStep | Represents an Open VeriStand Project step, which opens an NI VeriStand project (.nivsproj) file. |
| OpenWorkspaceStep | Represents an Open VeriStand Workspace step, which opens the Workspace window with the screen file for the active NI VeriStand project. |
| OpenWorkspaceToolStep | Represents an Open Workspace Tool step, which opens a Workspace tool for the active NI VeriStand project. |
| RealTimeSequenceCallParameterAssignment | Represents the parameter assignments for a real-time sequence. A parameter can have a constant value or map to a channel in a system definition file. |
| RealTimeSequenceCallStep | Represents a Call Real-Time Sequence Step, which calls a real-time sequence to execute. |
| RealTimeSequenceGroupStep | Represents a Real-Time Sequence Group, which contains a group of RealTimeSequenceCallStep objects that execute in parallel. This step does not complete until each real-time sequence in the group executes. |
| SendProjectCommandStep | Represents a Control Active VeriStand Project step, which sends a command (Connect, Run, Deploy, and so on) to the NI VeriStand project the stimulus profile is associated with. |
| SendWorkspaceToolMessageStep | Represents a Send Workspace Tool Message step. This step sends an open Workspace tool VI a specified message or command, as well as data required by the case in the tool that handles the command. |
| SetupStepGroup | Represents the Setup, or initialization, section of the stimulus profile code. This section is a StepGroup that contains all the steps you want to execute before the MainStepGroup begins executing. |
| StartLoggingStep | Represents a Start Logging step, which starts logging data from a specified set of channels to a TDMS file. |
| StepGroup | Represents a group of steps in a stimulus profile. |
| StimulusProfile | Represents a stimulus profile. |
| StopLoggingStep | Represents a Stop Logging step, which finalizes and stops a logging operation started by a StartLoggingStep. |
| UpdateModelParametersFromFile | Represents an Update Model Parameters from File step, which updates parameter values for a simulation model to values specified in a text (.txt) file. |

#### Interfaces

None

#### Structures

None

#### Enumerations

| Name | Description |
| --- | --- |
| BoundsCheckType | Specifies the type of bounds check used for a NumericBoundsEvaluation. |
| EvaluationType | Specifies the type of pass/fail evaluation performed on a given value. This value is typically the return value of a real-time sequence called by a RealTimeSequenceCallStep. |
| LogFileSegmentingOptions | Specifies how to segment the log files created during the data logging session. |
| StepExecutionState | Specifies the current execution state of a step in a stimulus profile. |
| StepResult | Indicates the result of executing a stimulus profile step. |
| VeriStandProjectCommand | Specifies the command that a SendProjectCommandStep sends to the active NI VeriStand project. |

#### Delegates

None

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-acceleration-acceleration__string-string-string-basenode-basenode.html language=enus -->
## TOPIC 01692: Acceleration(string, string, string, BaseNode, BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-acceleration-acceleration__string-string-string-basenode-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-acceleration-acceleration__string-string-string-basenode-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Acceleration with the specified name, description, units, and channels. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Acceleration(string Name, string Description, string Units, BaseNode ChannelToAnalyze, BaseNode ChannelForVelocity)Parameters

### Acceleration(string, string, string, BaseNode, BaseNode)

Initializes a new instance of [Acceleration](nationalinstruments-veristand-systemdefinitionapi-acceleration.html) with the specified name, description, units, and channels.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Acceleration(string Name, string Description, string Units, BaseNode ChannelToAnalyze, BaseNode ChannelForVelocity)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Acceleration calculated channel. |
| Description | string | The description of the Acceleration calculated channel. |
| Units | string | The units to associate with the Acceleration calculated channel. |
| ChannelToAnalyze | BaseNode | The channel for which to calculate the acceleration. |
| ChannelForVelocity | BaseNode | The channel on which to store the velocity of the ChannelToAnalyze. |

Parent topic:

Acceleration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-acceleration-velocitychannel.html language=enus -->
## TOPIC 01693: VelocityChannel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-acceleration-velocitychannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-acceleration-velocitychannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the channel on which to store the velocity of XChannel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode VelocityChannel { get; set; }ReturnsA BaseNode reference to the velocity channel.

### VelocityChannel

Gets or sets the channel on which to store the velocity of [XChannel](nationalinstruments-veristand-systemdefinitionapi-acceleration-xchannel.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) VelocityChannel { get; set; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the velocity channel.

Parent topic:

Acceleration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-acceleration-xchannel.html language=enus -->
## TOPIC 01694: XChannel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-acceleration-xchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-acceleration-xchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the channel for which to calculate the acceleration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode XChannel { get; set; }ReturnsA BaseNode reference to the channel.

### XChannel

Gets or sets the channel for which to calculate the acceleration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) XChannel { get; set; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the channel.

Parent topic:

Acceleration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-acceleration.html language=enus -->
## TOPIC 01695: Acceleration Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-acceleration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-acceleration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a calculated channel with the acceleration function. Derives fromCalculatedChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Acceleration : CalculatedChannelRemarksUse the members of this class to specify the channels to use as variables in the accelera

### Acceleration Class

Represents a calculated channel with the acceleration function.

#### Derives from

- CalculatedChannel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Acceleration : CalculatedChannel

#### Remarks

Use the members of this class to specify the channels to use as variables in the acceleration calculation. The function calculates the acceleration and velocity of the [XChannel](nationalinstruments-veristand-systemdefinitionapi-acceleration-xchannel.html) you specify. The [VelocityChannel](nationalinstruments-veristand-systemdefinitionapi-acceleration-velocitychannel.html) stores the velocity. The calculated channel itself stores the acceleration value.

**Accessing this Class**

- Acceleration Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Acceleration(string, string, string, BaseNode, BaseNode) | Initializes a new instance of Acceleration with the specified name, description, units, and channels. |

#### Properties

| Name | Description |
| --- | --- |
| VelocityChannel | Gets or sets the channel on which to store the velocity of XChannel. |
| XChannel | Gets or sets the channel for which to calculate the acceleration. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-acquisitionmode.html language=enus -->
## TOPIC 01696: AcquisitionMode Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-acquisitionmode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-acquisitionmode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the acquisition mode of a DAQTask. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum AcquisitionModeMembersNameValueDescriptionFinite10178The task acquires a finite number of samples per channel or acquires for a finite number of seconds. Continuous10123Tha task a

### AcquisitionMode Enumeration

Defines the acquisition mode of a [DAQTask](nationalinstruments-veristand-systemdefinitionapi-daqtask.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum AcquisitionMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Finite | 10178 | The task acquires a finite number of samples per channel or acquires for a finite number of seconds. |
| Continuous | 10123 | Tha task acquires samples continuously until the task is stopped. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-acquisitionunits.html language=enus -->
## TOPIC 01697: AcquisitionUnits Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-acquisitionunits.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-acquisitionunits.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines whether the size of acquisitions is represented as samples per channel or time, in seconds. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum AcquisitionUnitsMembersNameValueDescriptionSamples0The size is defined in samples per channel. Seconds1The size is defined

### AcquisitionUnits Enumeration

Defines whether the size of acquisitions is represented as samples per channel or time, in seconds.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum AcquisitionUnits

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Samples | 0 | The size is defined in samples per channel. |
| Seconds | 1 | The size is defined in seconds. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-actiononnew.html language=enus -->
## TOPIC 01698: ActionOnNew Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-actiononnew.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-actiononnew.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the location to which to log data when a DAQTaskAI begins a new acquisition. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum ActionOnNewMembersNameValueDescriptionNewGroup0A new group within the TDMS file to which the system has been writing. If an acquisition h

### ActionOnNew Enumeration

Defines the location to which to log data when a [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html) begins a new acquisition.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum ActionOnNew

#### Members

| Name | Value | Description |
| --- | --- | --- |
| NewGroup | 0 | A new group within the TDMS file to which the system has been writing. If an acquisition has not yet occurred, create a new TDMS file. |
| NewFile | 1 | A new TDMS log file. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-addalarmstatuschannel.html language=enus -->
## TOPIC 01699: AddAlarmStatusChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-addalarmstatuschannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-addalarmstatuschannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an alarm status channel to this alarm. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddAlarmStatusChannel()ReturnsReturns true if a new alarm status channel was added.

### AddAlarmStatusChannel()

Adds an alarm status channel to this alarm.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddAlarmStatusChannel()

#### Returns

Returns true if a new alarm status channel was added.

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-alarm__string-string-channel-basenode-basenode-procedure-alarmmode-alarmstate-alarmpriority-double-string.html language=enus -->
## TOPIC 01700: Alarm(string, string, Channel, BaseNode, BaseNode, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-alarm__string-string-channel-basenode-basenode-procedure-alarmmode-alarmstate-alarmpriority-double-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-alarm__string-string-channel-basenode-basenode-procedure-alarmmode-alarmstate-alarmpriority-double-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Alarm with the specified name, description, and configuration. This constructor uses channels to specify the UpperLimit and LowerLimit values within which AlarmSource must stay to avoid triggering the alarm. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitio

### Alarm(string, string, Channel, BaseNode, BaseNode, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string)

Initializes a new instance of [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) with the specified name, description, and configuration. This constructor uses channels to specify the *UpperLimit*  and *LowerLimit*  values within which *AlarmSource*  must stay to avoid triggering the alarm.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Alarm(string Name, string Description, Channel AlarmSource, BaseNode UpperLimit, BaseNode LowerLimit, Procedure AlarmAction, AlarmMode Mode, AlarmState DefaultState, AlarmPriority Priority, double Delay, string TripMessage)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alarm. |
| Description | string | The description of the Alarm. |
| AlarmSource | Channel | The channel to monitor for alarm conditions. |
| UpperLimit | BaseNode | The channel that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. |
| LowerLimit | BaseNode | The channel that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. |
| AlarmAction | Procedure | The Procedure to initiate when the alarm occurs. |
| Mode | AlarmMode | The AlarmMode (Normal or IndicateOnly). |
| DefaultState | AlarmState | The default AlarmState (Enabled or Disabled). |
| Priority | AlarmPriority | The AlarmPriority level (Low, Medium, or High). |
| Delay | double | The amount of time to wait before triggering the alarm. |
| TripMessage | string | The message to display when the alarm is tripped. |

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-alarm__string-string-channel-basenode-double-procedure-alarmmode-alarmstate-alarmpriority-double-string.html language=enus -->
## TOPIC 01701: Alarm(string, string, Channel, BaseNode, double, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-alarm__string-string-channel-basenode-double-procedure-alarmmode-alarmstate-alarmpriority-double-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-alarm__string-string-channel-basenode-double-procedure-alarmmode-alarmstate-alarmpriority-double-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Alarm with the specified name, description, and configuration. This constructor uses a channel to specify the UpperLimit and a constant to specify the LowerLimit within which AlarmSource must stay to avoid triggering the alarm. SyntaxNamespace: NationalInstruments.VeriS

### Alarm(string, string, Channel, BaseNode, double, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string)

Initializes a new instance of [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) with the specified name, description, and configuration. This constructor uses a channel to specify the *UpperLimit*  and a constant to specify the *LowerLimit*  within which *AlarmSource*  must stay to avoid triggering the alarm.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Alarm(string Name, string Description, Channel AlarmSource, BaseNode UpperLimit, double LowerLimit, Procedure AlarmAction, AlarmMode Mode, AlarmState DefaultState, AlarmPriority Priority, double Delay, string TripMessage)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alarm. |
| Description | string | The description of the Alarm. |
| AlarmSource | Channel | The channel to monitor for alarm conditions. |
| UpperLimit | BaseNode | The channel that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. |
| LowerLimit | double | The constant that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. |
| AlarmAction | Procedure | The Procedure to initiate when the alarm occurs. |
| Mode | AlarmMode | The AlarmMode (Normal or IndicateOnly). |
| DefaultState | AlarmState | The default AlarmState (Enabled or Disabled). |
| Priority | AlarmPriority | The AlarmPriority level (Low, Medium, or High). |
| Delay | double | The amount of time to wait before triggering the alarm. |
| TripMessage | string | The message to display when the alarm is tripped. |

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-alarm__string-string-channel-double-basenode-procedure-alarmmode-alarmstate-alarmpriority-double-string.html language=enus -->
## TOPIC 01702: Alarm(string, string, Channel, double, BaseNode, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-alarm__string-string-channel-double-basenode-procedure-alarmmode-alarmstate-alarmpriority-double-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-alarm__string-string-channel-double-basenode-procedure-alarmmode-alarmstate-alarmpriority-double-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Alarm with the specified name, description, and configuration. This constructor uses a constant to specify the UpperLimit and a channel to specify the LowerLimit within which AlarmSource must stay to avoid triggering the alarm. SyntaxNamespace: NationalInstruments.VeriS

### Alarm(string, string, Channel, double, BaseNode, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string)

Initializes a new instance of [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) with the specified name, description, and configuration. This constructor uses a constant to specify the *UpperLimit*  and a channel to specify the *LowerLimit*  within which *AlarmSource*  must stay to avoid triggering the alarm.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Alarm(string Name, string Description, Channel AlarmSource, double UpperLimit, BaseNode LowerLimit, Procedure AlarmAction, AlarmMode Mode, AlarmState DefaultState, AlarmPriority Priority, double Delay, string TripMessage)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alarm. |
| Description | string | The description of the Alarm. |
| AlarmSource | Channel | The channel to monitor for alarm conditions. |
| UpperLimit | double | The constant that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. |
| LowerLimit | BaseNode | The channel that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. |
| AlarmAction | Procedure | The Procedure to initiate when the alarm occurs. |
| Mode | AlarmMode | The AlarmMode (Normal or IndicateOnly). |
| DefaultState | AlarmState | The default AlarmState (Enabled or Disabled). |
| Priority | AlarmPriority | The AlarmPriority level (Low, Medium, or High). |
| Delay | double | The amount of time to wait before triggering the alarm. |
| TripMessage | string | The message to display when the alarm is tripped. |

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-alarm__string-string-channel-double-double-procedure-alarmmode-alarmstate-alarmpriority-double-string.html language=enus -->
## TOPIC 01703: Alarm(string, string, Channel, double, double, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-alarm__string-string-channel-double-double-procedure-alarmmode-alarmstate-alarmpriority-double-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-alarm__string-string-channel-double-double-procedure-alarmmode-alarmstate-alarmpriority-double-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Alarm with the specified name, description, and configuration. This constructor uses constants to specify the UpperLimit and LowerLimit values within which AlarmSource must stay to avoid triggering the alarm. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefiniti

### Alarm(string, string, Channel, double, double, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string)

Initializes a new instance of [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) with the specified name, description, and configuration. This constructor uses constants to specify the *UpperLimit*  and *LowerLimit*  values within which *AlarmSource*  must stay to avoid triggering the alarm.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Alarm(string Name, string Description, Channel AlarmSource, double UpperLimit, double LowerLimit, Procedure AlarmAction, AlarmMode Mode, AlarmState DefaultState, AlarmPriority Priority, double Delay, string TripMessage)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alarm. |
| Description | string | The description of the Alarm. |
| AlarmSource | Channel | The channel to monitor for alarm conditions. |
| UpperLimit | double | The constant that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. |
| LowerLimit | double | The constant that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. |
| AlarmAction | Procedure | The Procedure to initiate when the alarm occurs. |
| Mode | AlarmMode | The AlarmMode (Normal or IndicateOnly). |
| DefaultState | AlarmState | The default AlarmState (Enabled or Disabled). |
| Priority | AlarmPriority | The AlarmPriority level (Low, Medium, or High). |
| Delay | double | The amount of time to wait before triggering the alarm. |
| TripMessage | string | The message to display when the alarm is tripped. |

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-alarm__string-string-channel-valuesource-valuesource-procedure-alarmmode-alarmstate-uint-uint-double-string-bool-bool.html language=enus -->
## TOPIC 01704: Alarm(string, string, Channel, ValueSource, ValueSource, Procedure, AlarmMode, AlarmState, uint, uint, double, string, bool, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-alarm__string-string-channel-valuesource-valuesource-procedure-alarmmode-alarmstate-uint-uint-double-string-bool-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-alarm__string-string-channel-valuesource-valuesource-procedure-alarmmode-alarmstate-uint-uint-double-string-bool-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Alarm with the specified name, description, and configuration, including whether the alarm resets automatically and whether the alarm must be manually acknowledged. This constructor uses channels OR constants to specify the UpperLimit and LowerLimit values within which

### Alarm(string, string, Channel, ValueSource, ValueSource, Procedure, AlarmMode, AlarmState, uint, uint, double, string, bool, bool)

Initializes a new instance of [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) with the specified name, description, and configuration, including whether the alarm resets automatically and whether the alarm must be manually acknowledged. This constructor uses channels OR constants to specify the *UpperLimit*  and *LowerLimit*  values within which *AlarmSource*  must stay to avoid triggering the alarm. This constructor also specifies the *GroupNumber*  to which the alarm belongs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Alarm(string Name, string Description, Channel AlarmSource, ValueSource UpperLimit, ValueSource LowerLimit, Procedure AlarmAction, AlarmMode Mode, AlarmState DefaultState, uint GroupNumber, uint PriorityNumber, double Delay, string TripMessage, bool AutoResetAlarm, bool RequireAlarmAcknowledgement)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alarm. |
| Description | string | The description of the Alarm. |
| AlarmSource | Channel | The channel to monitor for alarm conditions. |
| UpperLimit | ValueSource | The channel or constant that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. |
| LowerLimit | ValueSource | The channel or constant that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. |
| AlarmAction | Procedure | The Procedure to initiate when the alarm occurs. |
| Mode | AlarmMode | The AlarmMode (Normal or IndicateOnly). |
| DefaultState | AlarmState | The default AlarmState (Enabled or Disabled). |
| GroupNumber | uint | The number of the group to which the Alarm belongs. |
| PriorityNumber | uint | The priority of the alarm. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31. |
| Delay | double | The amount of time to wait before triggering the alarm. |
| TripMessage | string | The message to display when the alarm is tripped. |
| AutoResetAlarm | bool | If true, alarm automatically resets when channel is back in range, as opposed to being reset by a procedure. |
| RequireAlarmAcknowledgement | bool | If true, alarm must be manually acknowledged before it can reset. Otherwise, alarm is automatically acknowledged when the channel is back in range. |

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-alarm__string-string-channel-valuesource-valuesource-procedure-alarmmode-alarmstate-uint-uint-double-string.html language=enus -->
## TOPIC 01705: Alarm(string, string, Channel, ValueSource, ValueSource, Procedure, AlarmMode, AlarmState, uint, uint, double, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-alarm__string-string-channel-valuesource-valuesource-procedure-alarmmode-alarmstate-uint-uint-double-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-alarm__string-string-channel-valuesource-valuesource-procedure-alarmmode-alarmstate-uint-uint-double-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Alarm with the specified name, description, and configuration. This constructor uses channels OR constants to specify the UpperLimit and LowerLimit values within which AlarmSource must stay to avoid triggering the alarm. This constructor also specifies the GroupNumber t

### Alarm(string, string, Channel, ValueSource, ValueSource, Procedure, AlarmMode, AlarmState, uint, uint, double, string)

Initializes a new instance of [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) with the specified name, description, and configuration. This constructor uses channels OR constants to specify the *UpperLimit*  and *LowerLimit*  values within which *AlarmSource*  must stay to avoid triggering the alarm. This constructor also specifies the *GroupNumber*  to which the alarm belongs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Alarm(string Name, string Description, Channel AlarmSource, ValueSource UpperLimit, ValueSource LowerLimit, Procedure AlarmAction, AlarmMode Mode, AlarmState DefaultState, uint GroupNumber, uint PriorityNumber, double Delay, string TripMessage)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alarm. |
| Description | string | The description of the Alarm. |
| AlarmSource | Channel | The channel to monitor for alarm conditions. |
| UpperLimit | ValueSource | The channel or constant that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. |
| LowerLimit | ValueSource | The channel or constant that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. |
| AlarmAction | Procedure | The Procedure to initiate when the alarm occurs. |
| Mode | AlarmMode | The AlarmMode (Normal or IndicateOnly). |
| DefaultState | AlarmState | The default AlarmState (Enabled or Disabled). |
| GroupNumber | uint | The number of the group to which the Alarm belongs. |
| PriorityNumber | uint | The priority of the alarm. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31. |
| Delay | double | The amount of time to wait before triggering the alarm. |
| TripMessage | string | The message to display when the alarm is tripped. |

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-alarmaction.html language=enus -->
## TOPIC 01706: AlarmAction

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-alarmaction.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-alarmaction.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the procedure to initiate when the alarm conditions are met. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode AlarmAction { get; set; }ReturnsA BaseNode reference to the procedure.

### AlarmAction

Gets or sets the procedure to initiate when the alarm conditions are met.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) AlarmAction { get; set; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the procedure.

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-alarmsource.html language=enus -->
## TOPIC 01707: AlarmSource

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-alarmsource.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-alarmsource.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the channel to monitor for alarm conditions. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode AlarmSource { get; set; }ReturnsA BaseNode reference to the channel.

### AlarmSource

Gets or sets the channel to monitor for alarm conditions.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) AlarmSource { get; set; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the channel.

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-autoresetalarm.html language=enus -->
## TOPIC 01708: AutoResetAlarm

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-autoresetalarm.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-autoresetalarm.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the reset behavior of the alarm. This property defines whether the alarm automatically resets when the channel is back in range, as opposed to being reset by a procedure. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AutoResetAlarm { get; set; }

### AutoResetAlarm

Gets or sets the reset behavior of the alarm. This property defines whether the alarm automatically resets when the channel is back in range, as opposed to being reset by a procedure.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AutoResetAlarm { get; set; }

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-defaultstate.html language=enus -->
## TOPIC 01709: DefaultState

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-defaultstate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-defaultstate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the default state (Disabled or Enabled) of the alarm. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic AlarmState DefaultState { get; set; }ReturnsAn enumeration value of AlarmState.

### DefaultState

Gets or sets the default state (Disabled or Enabled) of the alarm.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [AlarmState](nationalinstruments-veristand-systemdefinitionapi-alarmstate.html) DefaultState { get; set; }

#### Returns

An enumeration value of [AlarmState](nationalinstruments-veristand-systemdefinitionapi-alarmstate.html).

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-delay.html language=enus -->
## TOPIC 01710: Delay

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-delay.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-delay.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the amount of time to wait before triggering the alarm. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double Delay { get; set; }ReturnsThe delay duration, in seconds.

### Delay

Gets or sets the amount of time to wait before triggering the alarm.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double Delay { get; set; }

#### Returns

The delay duration, in seconds.

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-getalarmstatuschannel.html language=enus -->
## TOPIC 01711: GetAlarmStatusChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-getalarmstatuschannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-getalarmstatuschannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns this alarm's status channel or null if it doesn't exist. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic AlarmStatus GetAlarmStatusChannel()

### GetAlarmStatusChannel()

Returns this alarm's status channel or null if it doesn't exist.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [AlarmStatus](nationalinstruments-veristand-systemdefinitionapi-alarmstatus.html) GetAlarmStatusChannel()

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-groupnumber.html language=enus -->
## TOPIC 01712: GroupNumber

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-groupnumber.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-groupnumber.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the number of the group to which an alarm belongs. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint GroupNumber { get; set; }ReturnsThe group number.

### GroupNumber

Gets or sets the number of the group to which an alarm belongs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint GroupNumber { get; set; }

#### Returns

The group number.

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-lowerlimitchannel.html language=enus -->
## TOPIC 01713: LowerLimitChannel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-lowerlimitchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-lowerlimitchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the channel that determines the lower limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode LowerLimitChannel { get; }ReturnsA BaseNode reference to the lower limit

### LowerLimitChannel

Gets the channel that determines the lower limit value of the alarm. If the value of [AlarmSource](nationalinstruments-veristand-systemdefinitionapi-alarm-alarmsource.html) falls below this limit, the alarm is triggered.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) LowerLimitChannel { get; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the lower limit channel.

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-lowerlimitconstant.html language=enus -->
## TOPIC 01714: LowerLimitConstant

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-lowerlimitconstant.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-lowerlimitconstant.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the constant value that determines the lower limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double LowerLimitConstant { get; }ReturnsThe constant lower limit value.

### LowerLimitConstant

Gets the constant value that determines the lower limit value of the alarm. If the value of [AlarmSource](nationalinstruments-veristand-systemdefinitionapi-alarm-alarmsource.html) falls below this limit, the alarm is triggered.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double LowerLimitConstant { get; }

#### Returns

The constant lower limit value.

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-lowerlimitisconstant.html language=enus -->
## TOPIC 01715: LowerLimitIsConstant

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-lowerlimitisconstant.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-lowerlimitisconstant.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the lower limit value of the alarm is specified by a constant or a channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint LowerLimitIsConstant { get; }Returnstrue if the lower limit is specified by a constant. false if the lower limit is specified by a ch

### LowerLimitIsConstant

Gets whether the lower limit value of the alarm is specified by a constant or a channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint LowerLimitIsConstant { get; }

#### Returns

true if the lower limit is specified by a constant. false if the lower limit is specified by a channel.

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-mode.html language=enus -->
## TOPIC 01716: Mode

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-mode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-mode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the mode of the alarm (Normal or IndicateOnly). SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic AlarmMode Mode { get; set; }ReturnsAn enumeration value of AlarmMode.

### Mode

Gets or sets the mode of the alarm (Normal or IndicateOnly).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [AlarmMode](nationalinstruments-veristand-systemdefinitionapi-alarmmode.html) Mode { get; set; }

#### Returns

An enumeration value of [AlarmMode](nationalinstruments-veristand-systemdefinitionapi-alarmmode.html).

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-priority.html language=enus -->
## TOPIC 01717: Priority

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-priority.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-priority.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property is deprecated in NI VeriStand 2011 and later. Use the PriorityNumber property instead. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic AlarmPriority Priority { get; set; }RemarksSetting this property to Low, Medium, or High automatically sets the PriorityNumber

### Priority

This property is deprecated in NI VeriStand 2011 and later. Use the [PriorityNumber](nationalinstruments-veristand-systemdefinitionapi-alarm-prioritynumber.html) property instead.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [AlarmPriority](nationalinstruments-veristand-systemdefinitionapi-alarmpriority.html) Priority { get; set; }

#### Remarks

Setting this property to Low, Medium, or High automatically sets the [PriorityNumber](nationalinstruments-veristand-systemdefinitionapi-alarm-prioritynumber.html) to 25, 15, or 5, respectively.

#### Returns

An enumeration value of [AlarmPriority](nationalinstruments-veristand-systemdefinitionapi-alarmpriority.html).

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-prioritynumber.html language=enus -->
## TOPIC 01718: PriorityNumber

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-prioritynumber.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-prioritynumber.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the priority of an alarm running on the target. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint PriorityNumber { get; set; }ReturnsThe alarm priority number.

### PriorityNumber

Gets or sets the priority of an alarm running on the target. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint PriorityNumber { get; set; }

#### Returns

The alarm priority number.

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-requirealarmacknowledgement.html language=enus -->
## TOPIC 01719: RequireAlarmAcknowledgement

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-requirealarmacknowledgement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-requirealarmacknowledgement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the acknowledgement behavior of the alarm. This property defines whether the alarm must be manually acknowledged before it can reset. Otherwise, alarm is automatically acknowledged when the channel is back in range. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpubli

### RequireAlarmAcknowledgement

Gets or sets the acknowledgement behavior of the alarm. This property defines whether the alarm must be manually acknowledged before it can reset. Otherwise, alarm is automatically acknowledged when the channel is back in range.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool RequireAlarmAcknowledgement { get; set; }

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-setlowerlimit__basenode.html language=enus -->
## TOPIC 01720: SetLowerLimit(BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-setlowerlimit__basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-setlowerlimit__basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the low limit to the specified channel value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetLowerLimit(BaseNode LowerLimit)ParametersNameTypeDescriptionLowerLimitBaseNodeThe channel that determines the low limit value of the alarm.

### SetLowerLimit(BaseNode)

Sets the low limit to the specified channel value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetLowerLimit(BaseNode LowerLimit)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| LowerLimit | BaseNode | The channel that determines the low limit value of the alarm. |

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-setlowerlimit__double.html language=enus -->
## TOPIC 01721: SetLowerLimit(double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-setlowerlimit__double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-setlowerlimit__double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the low limit to the specified constant value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetLowerLimit(double LowerLimit)ParametersNameTypeDescriptionLowerLimitdoubleThe constant that determines the low limit value of the alarm.

### SetLowerLimit(double)

Sets the low limit to the specified constant value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetLowerLimit(double LowerLimit)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| LowerLimit | double | The constant that determines the low limit value of the alarm. |

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-setlowerlimit__valuesource.html language=enus -->
## TOPIC 01722: SetLowerLimit(ValueSource)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-setlowerlimit__valuesource.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-setlowerlimit__valuesource.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the low limit to the specified channel or constant value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetLowerLimit(ValueSource Limit)ParametersNameTypeDescriptionLimitValueSourceThe channel or constant that determines the low limit value of the alarm.

### SetLowerLimit(ValueSource)

Sets the low limit to the specified channel or constant value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetLowerLimit(ValueSource Limit)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Limit | ValueSource | The channel or constant that determines the low limit value of the alarm. |

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-setupperlimit__basenode.html language=enus -->
## TOPIC 01723: SetUpperLimit(BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-setupperlimit__basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-setupperlimit__basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the high limit to the specified channel value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetUpperLimit(BaseNode UpperLimit)ParametersNameTypeDescriptionUpperLimitBaseNodeThe channel that determines the high limit value of the alarm.

### SetUpperLimit(BaseNode)

Sets the high limit to the specified channel value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetUpperLimit(BaseNode UpperLimit)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| UpperLimit | BaseNode | The channel that determines the high limit value of the alarm. |

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-setupperlimit__double.html language=enus -->
## TOPIC 01724: SetUpperLimit(double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-setupperlimit__double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-setupperlimit__double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the high limit to the specified constant value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetUpperLimit(double UpperLimit)ParametersNameTypeDescriptionUpperLimitdoubleThe constant that determines the high limit value of the alarm.

### SetUpperLimit(double)

Sets the high limit to the specified constant value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetUpperLimit(double UpperLimit)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| UpperLimit | double | The constant that determines the high limit value of the alarm. |

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-setupperlimit__valuesource.html language=enus -->
## TOPIC 01725: SetUpperLimit(ValueSource)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-setupperlimit__valuesource.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-setupperlimit__valuesource.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the high limit to the specified channel or constant value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetUpperLimit(ValueSource Limit)ParametersNameTypeDescriptionLimitValueSourceThe channel or constant that determines the high limit value of the alarm.

### SetUpperLimit(ValueSource)

Sets the high limit to the specified channel or constant value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetUpperLimit(ValueSource Limit)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Limit | ValueSource | The channel or constant that determines the high limit value of the alarm. |

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-tripmessage.html language=enus -->
## TOPIC 01726: TripMessage

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-tripmessage.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-tripmessage.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the message to display when the alarm is tripped. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string TripMessage { get; set; }ReturnsThe message to display.

### TripMessage

Gets or sets the message to display when the alarm is tripped.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string TripMessage { get; set; }

#### Returns

The message to display.

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-upperlimitchannel.html language=enus -->
## TOPIC 01727: UpperLimitChannel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-upperlimitchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-upperlimitchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the channel that determines the upper limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode UpperLimitChannel { get; }ReturnsA BaseNode reference to the upper limit chan

### UpperLimitChannel

Gets the channel that determines the upper limit value of the alarm. If the value of [AlarmSource](nationalinstruments-veristand-systemdefinitionapi-alarm-alarmsource.html) exceeds this limit, the alarm is triggered.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) UpperLimitChannel { get; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the upper limit channel.

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-upperlimitconstant.html language=enus -->
## TOPIC 01728: UpperLimitConstant

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-upperlimitconstant.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-upperlimitconstant.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the constant that determines the upper limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double UpperLimitConstant { get; }ReturnsThe constant upper limit value.

### UpperLimitConstant

Gets the constant that determines the upper limit value of the alarm. If the value of [AlarmSource](nationalinstruments-veristand-systemdefinitionapi-alarm-alarmsource.html) exceeds this limit, the alarm is triggered.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double UpperLimitConstant { get; }

#### Returns

The constant upper limit value.

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm-upperlimitisconstant.html language=enus -->
## TOPIC 01729: UpperLimitIsConstant

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm-upperlimitisconstant.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm-upperlimitisconstant.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the upper limit value of the alarm is specified by a constant or a channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint UpperLimitIsConstant { get; }Returnstrue if the upper limit is specified by a constant. false if the upper limit is specified by a ch

### UpperLimitIsConstant

Gets whether the upper limit value of the alarm is specified by a constant or a channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint UpperLimitIsConstant { get; }

#### Returns

true if the upper limit is specified by a constant. false if the upper limit is specified by a channel.

Parent topic:

Alarm Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarm.html language=enus -->
## TOPIC 01730: Alarm Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarm.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarm.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an alarm, which notifies the user that the value of a particular channel has gone outside a specified range of values. Alarms also can trigger the execution of a specified procedure. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Alarm :

### Alarm Class

Represents an alarm, which notifies the user that the value of a particular channel has gone outside a specified range of values. Alarms also can trigger the execution of a specified procedure.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Alarm : Section

#### Remarks

Use the members of this class to access and configure an alarm. For example, you can set the default state of the alarm, configure its upper and lower limits, and assign it to a group.

**Accessing this Class**

- [GetAlarmList(bool)](nationalinstruments-veristand-systemdefinitionapi-alarmfolder-getalarmlist__bool.html)
- [GetAlarmList(bool)](nationalinstruments-veristand-systemdefinitionapi-alarms-getalarmlist__bool.html)
- Alarm Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Alarm(string, string, Channel, BaseNode, BaseNode, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string) | Initializes a new instance of Alarm with the specified name, description, and configuration. This constructor uses channels to specify the UpperLimit and LowerLimit values within which AlarmSource must stay to avoid triggering the alarm. |
| Alarm(string, string, Channel, double, double, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string) | Initializes a new instance of Alarm with the specified name, description, and configuration. This constructor uses constants to specify the UpperLimit and LowerLimit values within which AlarmSource must stay to avoid triggering the alarm. |
| Alarm(string, string, Channel, BaseNode, double, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string) | Initializes a new instance of Alarm with the specified name, description, and configuration. This constructor uses a channel to specify the UpperLimit and a constant to specify the LowerLimit within which AlarmSource must stay to avoid triggering the alarm. |
| Alarm(string, string, Channel, double, BaseNode, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string) | Initializes a new instance of Alarm with the specified name, description, and configuration. This constructor uses a constant to specify the UpperLimit and a channel to specify the LowerLimit within which AlarmSource must stay to avoid triggering the alarm. |
| Alarm(string, string, Channel, ValueSource, ValueSource, Procedure, AlarmMode, AlarmState, uint, uint, double, string) | Initializes a new instance of Alarm with the specified name, description, and configuration. This constructor uses channels OR constants to specify the UpperLimit and LowerLimit values within which AlarmSource must stay to avoid triggering the alarm. This constructor also specifies the GroupNumber to which the alarm belongs. |
| Alarm(string, string, Channel, ValueSource, ValueSource, Procedure, AlarmMode, AlarmState, uint, uint, double, string, bool, bool) | Initializes a new instance of Alarm with the specified name, description, and configuration, including whether the alarm resets automatically and whether the alarm must be manually acknowledged. This constructor uses channels OR constants to specify the UpperLimit and LowerLimit values within which AlarmSource must stay to avoid triggering the alarm. This constructor also specifies the GroupNumber to which the alarm belongs. |

#### Properties

| Name | Description |
| --- | --- |
| AlarmAction | Gets or sets the procedure to initiate when the alarm conditions are met. |
| AlarmSource | Gets or sets the channel to monitor for alarm conditions. |
| AutoResetAlarm | Gets or sets the reset behavior of the alarm. This property defines whether the alarm automatically resets when the channel is back in range, as opposed to being reset by a procedure. |
| DefaultState | Gets or sets the default state (Disabled or Enabled) of the alarm. |
| Delay | Gets or sets the amount of time to wait before triggering the alarm. |
| GroupNumber | Gets or sets the number of the group to which an alarm belongs. |
| LowerLimitChannel | Gets the channel that determines the lower limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. |
| LowerLimitConstant | Gets the constant value that determines the lower limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. |
| LowerLimitIsConstant | Gets whether the lower limit value of the alarm is specified by a constant or a channel. |
| Mode | Gets or sets the mode of the alarm (Normal or IndicateOnly). |
| Priority | This property is deprecated in NI VeriStand 2011 and later. Use the PriorityNumber property instead. |
| PriorityNumber | Gets or sets the priority of an alarm running on the target. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31. |
| RequireAlarmAcknowledgement | Gets or sets the acknowledgement behavior of the alarm. This property defines whether the alarm must be manually acknowledged before it can reset. Otherwise, alarm is automatically acknowledged when the channel is back in range. |
| TripMessage | Gets or sets the message to display when the alarm is tripped. |
| UpperLimitChannel | Gets the channel that determines the upper limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. |
| UpperLimitConstant | Gets the constant that determines the upper limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. |
| UpperLimitIsConstant | Gets whether the upper limit value of the alarm is specified by a constant or a channel. |

#### Methods

| Name | Description |
| --- | --- |
| AddAlarmStatusChannel() | Adds an alarm status channel to this alarm. |
| GetAlarmStatusChannel() | Returns this alarm's status channel or null if it doesn't exist. |
| SetLowerLimit(BaseNode) | Sets the low limit to the specified channel value. |
| SetLowerLimit(double) | Sets the low limit to the specified constant value. |
| SetLowerLimit(ValueSource) | Sets the low limit to the specified channel or constant value. |
| SetUpperLimit(ValueSource) | Sets the high limit to the specified channel or constant value. |
| SetUpperLimit(double) | Sets the high limit to the specified constant value. |
| SetUpperLimit(BaseNode) | Sets the high limit to the specified channel value. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarmfolder-addalarm__alarm-out.html language=enus -->
## TOPIC 01731: AddAlarm(Alarm, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarmfolder-addalarm__alarm-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarmfolder-addalarm__alarm-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified Alarm to the AlarmFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddAlarm(Alarm alarm, out Error error)ParametersNameTypeDescriptionalarmAlarmThe Alarm to add.errorout ErrorReturns an NationalInstruments.VeriStand.Error object. If no error oc

### AddAlarm(Alarm, out Error)

Adds the specified [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) to the [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddAlarm(Alarm alarm, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| alarm | Alarm | The Alarm to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) was added successfully.

Parent topic:

AlarmFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarmfolder-addalarm__alarm.html language=enus -->
## TOPIC 01732: AddAlarm(Alarm)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarmfolder-addalarm__alarm.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarmfolder-addalarm__alarm.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified Alarm to the AlarmFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddAlarm(Alarm alarm)ParametersNameTypeDescriptionalarmAlarmThe Alarm to add.Returnstrue if the Alarm was added successfully.

### AddAlarm(Alarm)

Adds the specified [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) to the [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddAlarm(Alarm alarm)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| alarm | Alarm | The Alarm to add. |

#### Returns

true if the [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) was added successfully.

Parent topic:

AlarmFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarmfolder-addalarmfolder__alarmfolder-out.html language=enus -->
## TOPIC 01733: AddAlarmFolder(AlarmFolder, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarmfolder-addalarmfolder__alarmfolder-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarmfolder-addalarmfolder__alarmfolder-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified AlarmFolder to the AlarmFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddAlarmFolder(AlarmFolder folder, out Error error)ParametersNameTypeDescriptionfolderAlarmFolderThe AlarmFolder to add.errorout ErrorReturns an NationalInstruments.VeriSt

### AddAlarmFolder(AlarmFolder, out Error)

Adds the specified [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) to the [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddAlarmFolder(AlarmFolder folder, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| folder | AlarmFolder | The AlarmFolder to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) was added successfully.

Parent topic:

AlarmFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarmfolder-addalarmfolder__alarmfolder.html language=enus -->
## TOPIC 01734: AddAlarmFolder(AlarmFolder)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarmfolder-addalarmfolder__alarmfolder.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarmfolder-addalarmfolder__alarmfolder.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified AlarmFolder to the AlarmFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddAlarmFolder(AlarmFolder folder)ParametersNameTypeDescriptionfolderAlarmFolderThe AlarmFolder to add.Returnstrue if the AlarmFolder was added successfully.

### AddAlarmFolder(AlarmFolder)

Adds the specified [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) to the [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddAlarmFolder(AlarmFolder folder)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| folder | AlarmFolder | The AlarmFolder to add. |

#### Returns

true if the [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) was added successfully.

Parent topic:

AlarmFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarmfolder-addnewalarm__string-string-channel-valuesource-valuesource-procedure-alarmmode-alarmstate-uint-uint-double-string-out.html language=enus -->
## TOPIC 01735: AddNewAlarm(string, string, Channel, ValueSource, ValueSource, Procedure, AlarmMode, AlarmState, uint, uint, double, string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarmfolder-addnewalarm__string-string-channel-valuesource-valuesource-procedure-alarmmode-alarmstate-uint-uint-double-string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarmfolder-addnewalarm__string-string-channel-valuesource-valuesource-procedure-alarmmode-alarmstate-uint-uint-double-string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new Alarm with the specified name, description, and configuration to the AlarmFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Alarm AddNewAlarm(string Name, string Description, Channel AlarmSource, ValueSource UpperLimit, ValueSource LowerLimit, Procedure Alar

### AddNewAlarm(string, string, Channel, ValueSource, ValueSource, Procedure, AlarmMode, AlarmState, uint, uint, double, string, out Error)

Adds a new [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) with the specified name, description, and configuration to the [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) AddNewAlarm(string Name, string Description, Channel AlarmSource, ValueSource UpperLimit, ValueSource LowerLimit, Procedure AlarmAction, AlarmMode Mode, AlarmState DefaultState, uint GroupNumber, uint PriorityNumber, double Delay, string TripMessage, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alarm. |
| Description | string | The description of the Alarm. |
| AlarmSource | Channel | The channel to monitor for alarm conditions. |
| UpperLimit | ValueSource | The channel or constant that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. |
| LowerLimit | ValueSource | The channel or constant that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. |
| AlarmAction | Procedure | The Procedure to initiate when the alarm occurs. |
| Mode | AlarmMode | The AlarmMode. |
| DefaultState | AlarmState | The default AlarmState. |
| GroupNumber | uint | The number of the group to which the Alarm belongs. |
| PriorityNumber | uint | The priority of the alarm running on the target. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31. |
| Delay | double | The amount of time to wait before triggering the alarm. |
| TripMessage | string | The message to display when the alarm is tripped. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) was added successfully.

Parent topic:

AlarmFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarmfolder-addnewalarm__string-string-channel-valuesource-valuesource-procedure-alarmmode-alarmstate-uint-uint-double-string.html language=enus -->
## TOPIC 01736: AddNewAlarm(string, string, Channel, ValueSource, ValueSource, Procedure, AlarmMode, AlarmState, uint, uint, double, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarmfolder-addnewalarm__string-string-channel-valuesource-valuesource-procedure-alarmmode-alarmstate-uint-uint-double-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarmfolder-addnewalarm__string-string-channel-valuesource-valuesource-procedure-alarmmode-alarmstate-uint-uint-double-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new Alarm with the specified name, description, and configuration to the AlarmFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddNewAlarm(string Name, string Description, Channel AlarmSource, ValueSource UpperLimit, ValueSource LowerLimit, Procedure Alarm

### AddNewAlarm(string, string, Channel, ValueSource, ValueSource, Procedure, AlarmMode, AlarmState, uint, uint, double, string)

Adds a new [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) with the specified name, description, and configuration to the [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddNewAlarm(string Name, string Description, Channel AlarmSource, ValueSource UpperLimit, ValueSource LowerLimit, Procedure AlarmAction, AlarmMode Mode, AlarmState DefaultState, uint GroupNumber, uint PriorityNumber, double Delay, string TripMessage)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alarm. |
| Description | string | The description of the Alarm. |
| AlarmSource | Channel | The channel to monitor for alarm conditions. |
| UpperLimit | ValueSource | The channel or constant that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. |
| LowerLimit | ValueSource | The channel or constant that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. |
| AlarmAction | Procedure | The Procedure to initiate when the alarm occurs. |
| Mode | AlarmMode | The AlarmMode. |
| DefaultState | AlarmState | The default AlarmState. |
| GroupNumber | uint | The number of the group to which the Alarm belongs. |
| PriorityNumber | uint | The priority of the alarm running on the target. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31. |
| Delay | double | The amount of time to wait before triggering the alarm. |
| TripMessage | string | The message to display when the alarm is tripped. |

#### Returns

true if the [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) was added successfully.

Parent topic:

AlarmFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarmfolder-addnewalarmfolder__string-string-out.html language=enus -->
## TOPIC 01737: AddNewAlarmFolder(string, string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarmfolder-addnewalarmfolder__string-string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarmfolder-addnewalarmfolder__string-string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new AlarmFolder with the specified name and description to the AlarmFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic AlarmFolder AddNewAlarmFolder(string Name, string Description, out Error error)ParametersNameTypeDescriptionNamestringThe name of the AlarmFolde

### AddNewAlarmFolder(string, string, out Error)

Adds a new [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) with the specified name and description to the [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) AddNewAlarmFolder(string Name, string Description, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the AlarmFolder. |
| Description | string | The description of the AlarmFolder. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) was added successfully.

Parent topic:

AlarmFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarmfolder-addnewalarmfolder__string-string.html language=enus -->
## TOPIC 01738: AddNewAlarmFolder(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarmfolder-addnewalarmfolder__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarmfolder-addnewalarmfolder__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new AlarmFolder with the specified name and description to the AlarmFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddNewAlarmFolder(string Name, string Description)ParametersNameTypeDescriptionNamestringThe name of the AlarmFolder.DescriptionstringThe d

### AddNewAlarmFolder(string, string)

Adds a new [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) with the specified name and description to the [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddNewAlarmFolder(string Name, string Description)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the AlarmFolder. |
| Description | string | The description of the AlarmFolder. |

#### Returns

true if the [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) was added successfully.

Parent topic:

AlarmFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarmfolder-alarmfolder__string-string.html language=enus -->
## TOPIC 01739: AlarmFolder(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarmfolder-alarmfolder__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarmfolder-alarmfolder__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of AlarmFolder with the specified name and description. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic AlarmFolder(string Name, string Description)ParametersNameTypeDescriptionNamestringThe name of the AlarmFolder.DescriptionstringThe description

### AlarmFolder(string, string)

Initializes a new instance of [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) with the specified name and description.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public AlarmFolder(string Name, string Description)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the AlarmFolder. |
| Description | string | The description of the AlarmFolder. |

Parent topic:

AlarmFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarmfolder-getalarmfolderlist.html language=enus -->
## TOPIC 01740: GetAlarmFolderList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarmfolder-getalarmfolderlist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarmfolder-getalarmfolderlist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the current AlarmFolder elements from AlarmFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic AlarmFolder[] GetAlarmFolderList()RemarksThis method only returns folders that are direct descendants of the current AlarmFolder. Any modification t

### GetAlarmFolderList()

Gets an array that contains the current [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) elements from [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html)[] GetAlarmFolderList()

#### Remarks

AlarmFolder

Note

Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition.

#### Returns

Returns an array that contains the current [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) elements from [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html).

Parent topic:

AlarmFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarmfolder-getalarmfolderlist__bool.html language=enus -->
## TOPIC 01741: GetAlarmFolderList(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarmfolder-getalarmfolderlist__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarmfolder-getalarmfolderlist__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the current AlarmFolder elements from AlarmFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic AlarmFolder[] GetAlarmFolderList(bool deep)RemarksAny modification that you make to the contents of this array also apply to the system definition.

### GetAlarmFolderList(bool)

Gets an array that contains the current [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) elements from [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html)[] GetAlarmFolderList(bool deep)

#### Remarks

Note

Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deep | bool | Specifies whether the method traverses each child AlarmFolder element of the AlarmFolder instance. true if the method traverses each child AlarmFolder instance to search for other AlarmFolder instances to traverse or other AlarmFolder elements to add to the result list; otherwise false. |

#### Returns

Returns an array that contains the current [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) elements from [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html).

Parent topic:

AlarmFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarmfolder-getalarmlist.html language=enus -->
## TOPIC 01742: GetAlarmList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarmfolder-getalarmlist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarmfolder-getalarmlist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the current Alarm elements from AlarmFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Alarm[] GetAlarmList()RemarksThis method only returns alarms that are direct descendants of the current AlarmFolder. Any modification that you make to the

### GetAlarmList()

Gets an array that contains the current [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) elements from [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html)[] GetAlarmList()

#### Remarks

AlarmFolder

Note

Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition.

#### Returns

Returns an array that contains the current [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) elements from the [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html).

Parent topic:

AlarmFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarmfolder-getalarmlist__bool.html language=enus -->
## TOPIC 01743: GetAlarmList(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarmfolder-getalarmlist__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarmfolder-getalarmlist__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the current Alarm elements from the AlarmFolder class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Alarm[] GetAlarmList(bool deep)RemarksAny modification that you make to the contents of this array also apply to the system definition. However,

### GetAlarmList(bool)

Gets an array that contains the current [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) elements from the [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html)[] GetAlarmList(bool deep)

#### Remarks

Note

Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deep | bool | Specifies whether the method traverses each child AlarmFolder element of the AlarmFolder instance. true if the method traverses each child AlarmFolder instance to search for other AlarmFolder instances to traverse or other Alarm elements to add to the result list; otherwise false. |

#### Returns

Returns an array that contains the current [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) elements from [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html).

Parent topic:

AlarmFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html language=enus -->
## TOPIC 01744: AlarmFolder Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an alarm folder, which organizes alarms under the Alarms section. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class AlarmFolder : SectionRemarksUse the member of this class to add new alarms to a folder, access existing alarms, or create or

### AlarmFolder Class

Represents an alarm folder, which organizes alarms under the [Alarms](nationalinstruments-veristand-systemdefinitionapi-alarms.html) section.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class AlarmFolder : Section

#### Remarks

Use the member of this class to add new alarms to a folder, access existing alarms, or create or access subfolders of the alarm folder.

**Accessing this Class**

- [GetAlarmFolderList(bool)](nationalinstruments-veristand-systemdefinitionapi-alarms-getalarmfolderlist__bool.html)
- [GetAlarmFolderList(bool)](nationalinstruments-veristand-systemdefinitionapi-alarmfolder-getalarmfolderlist__bool.html)
- AlarmFolder Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| AlarmFolder(string, string) | Initializes a new instance of AlarmFolder with the specified name and description. |

#### Methods

| Name | Description |
| --- | --- |
| AddAlarm(Alarm) | Adds the specified Alarm to the AlarmFolder. |
| AddAlarm(Alarm, out Error) | Adds the specified Alarm to the AlarmFolder. |
| AddAlarmFolder(AlarmFolder, out Error) | Adds the specified AlarmFolder to the AlarmFolder. |
| AddAlarmFolder(AlarmFolder) | Adds the specified AlarmFolder to the AlarmFolder. |
| AddNewAlarm(string, string, Channel, ValueSource, ValueSource, Procedure, AlarmMode, AlarmState, uint, uint, double, string) | Adds a new Alarm with the specified name, description, and configuration to the AlarmFolder. |
| AddNewAlarm(string, string, Channel, ValueSource, ValueSource, Procedure, AlarmMode, AlarmState, uint, uint, double, string, out Error) | Adds a new Alarm with the specified name, description, and configuration to the AlarmFolder. |
| AddNewAlarmFolder(string, string) | Adds a new AlarmFolder with the specified name and description to the AlarmFolder. |
| AddNewAlarmFolder(string, string, out Error) | Adds a new AlarmFolder with the specified name and description to the AlarmFolder. |
| GetAlarmFolderList() | Gets an array that contains the current AlarmFolder elements from AlarmFolder. |
| GetAlarmFolderList(bool) | Gets an array that contains the current AlarmFolder elements from AlarmFolder. |
| GetAlarmList(bool) | Gets an array that contains the current Alarm elements from the AlarmFolder class. |
| GetAlarmList() | Gets an array that contains the current Alarm elements from AlarmFolder. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-alarm.html language=enus -->
## TOPIC 01745: Alarm

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-alarm.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-alarm.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the Alarm on which to perform the step Function. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode Alarm { get; set; }ReturnsA BaseNode reference to the alarm. If this is null, use the tripped alarm which triggered the procedure.

### Alarm

Gets or sets the [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) on which to perform the step [Function](nationalinstruments-veristand-systemdefinitionapi-alarming-function.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) Alarm { get; set; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the alarm. If this is null, use the tripped alarm which triggered the procedure.

Parent topic:

Alarming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-alarmchannel.html language=enus -->
## TOPIC 01746: AlarmChannel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-alarmchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-alarmchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the channel to monitor for alarm conditions. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode AlarmChannel { get; set; }ReturnsA BaseNode reference to the channel.

### AlarmChannel

Gets or sets the channel to monitor for alarm conditions.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) AlarmChannel { get; set; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the channel.

Parent topic:

Alarming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-alarming__string-string-alarmingstepfunction-basenode.html language=enus -->
## TOPIC 01747: Alarming(string, string, AlarmingStepFunction, BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-alarming__string-string-alarmingstepfunction-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-alarming__string-string-alarmingstepfunction-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Alarming with the specified Name , Description , and Function . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Alarming(string Name, string Description, AlarmingStepFunction Function, BaseNode Alarm)ParametersNameTypeDescriptionNamestringThe na

### Alarming(string, string, AlarmingStepFunction, BaseNode)

Initializes a new instance of [Alarming](nationalinstruments-veristand-systemdefinitionapi-alarming.html) with the specified *Name* , *Description* , and *Function* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Alarming(string Name, string Description, AlarmingStepFunction Function, BaseNode Alarm)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alarming step. |
| Description | string | The description of the Alarming step. |
| Function | AlarmingStepFunction | The AlarmingStepFunction. For example, an Alarming step can enable or disable an alarm or adjust the alarm settings. |
| Alarm | BaseNode | The Alarm to configure. If this is null, use the tripped alarm which triggered the procedure. |

Parent topic:

Alarming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-alarming__string-string-alarmpriority-alarmstate-basenode-double-basenode-basenode-basenode-basenode.html language=enus -->
## TOPIC 01748: Alarming(string, string, AlarmPriority, AlarmState, BaseNode, double, BaseNode, BaseNode, BaseNode, BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-alarming__string-string-alarmpriority-alarmstate-basenode-double-basenode-basenode-basenode-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-alarming__string-string-alarmpriority-alarmstate-basenode-double-basenode-basenode-basenode-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Alarming with the specified name, description, and configuration. This constructor uses channels to specify the UpperLimit and LowerLimit values within which AlarmChannel must stay to avoid triggering the alarm. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefin

### Alarming(string, string, AlarmPriority, AlarmState, BaseNode, double, BaseNode, BaseNode, BaseNode, BaseNode)

Initializes a new instance of [Alarming](nationalinstruments-veristand-systemdefinitionapi-alarming.html) with the specified name, description, and configuration. This constructor uses channels to specify the *UpperLimit*  and *LowerLimit*  values within which *AlarmChannel*  must stay to avoid triggering the alarm.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Alarming(string Name, string Description, AlarmPriority Priority, AlarmState DefaultState, BaseNode Alarm, double Delay, BaseNode Procedure, BaseNode AlarmChannel, BaseNode UpperLimit, BaseNode LowerLimit)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alarming step. |
| Description | string | The description of the Alarming step. |
| Priority | AlarmPriority | The AlarmPriority level (Low, Medium, or High). |
| DefaultState | AlarmState | The default AlarmState (Enabled or Disabled). |
| Alarm | BaseNode | The Alarm to configure. If this is null, use the tripped alarm which triggered the procedure. |
| Delay | double | The amount of time to wait before triggering the alarm. |
| Procedure | BaseNode | The Procedure to initiate when the alarm occurs. |
| AlarmChannel | BaseNode | The channel to monitor for alarm conditions. |
| UpperLimit | BaseNode | The channel that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. |
| LowerLimit | BaseNode | The channel that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. |

Parent topic:

Alarming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-alarming__string-string-alarmpriority-alarmstate-basenode-double-basenode-basenode-basenode-double.html language=enus -->
## TOPIC 01749: Alarming(string, string, AlarmPriority, AlarmState, BaseNode, double, BaseNode, BaseNode, BaseNode, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-alarming__string-string-alarmpriority-alarmstate-basenode-double-basenode-basenode-basenode-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-alarming__string-string-alarmpriority-alarmstate-basenode-double-basenode-basenode-basenode-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Alarming with the specified name, description, and configuration. This constructor uses a channel to specify the UpperLimit and a constant to specify the LowerLimit within which AlarmChannel must stay to avoid triggering the alarm. SyntaxNamespace: NationalInstruments.V

### Alarming(string, string, AlarmPriority, AlarmState, BaseNode, double, BaseNode, BaseNode, BaseNode, double)

Initializes a new instance of [Alarming](nationalinstruments-veristand-systemdefinitionapi-alarming.html) with the specified name, description, and configuration. This constructor uses a channel to specify the *UpperLimit*  and a constant to specify the *LowerLimit*  within which *AlarmChannel*  must stay to avoid triggering the alarm.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Alarming(string Name, string Description, AlarmPriority Priority, AlarmState DefaultState, BaseNode Alarm, double Delay, BaseNode Procedure, BaseNode AlarmChannel, BaseNode UpperLimit, double LowerLimit)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alarming step. |
| Description | string | The description of the Alarming step. |
| Priority | AlarmPriority | The AlarmPriority level (Low, Medium, or High). |
| DefaultState | AlarmState | The default AlarmState (Enabled or Disabled). |
| Alarm | BaseNode | The Alarm to configure. If this is null, use the tripped alarm which triggered the procedure. |
| Delay | double | The amount of time to wait before triggering the alarm. |
| Procedure | BaseNode | The Procedure to initiate when the alarm occurs. |
| AlarmChannel | BaseNode | The channel to monitor for alarm conditions. |
| UpperLimit | BaseNode | The channel that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. |
| LowerLimit | double | The constant that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. |

Parent topic:

Alarming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-alarming__string-string-alarmpriority-alarmstate-basenode-double-basenode-basenode-double-basenode.html language=enus -->
## TOPIC 01750: Alarming(string, string, AlarmPriority, AlarmState, BaseNode, double, BaseNode, BaseNode, double, BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-alarming__string-string-alarmpriority-alarmstate-basenode-double-basenode-basenode-double-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-alarming__string-string-alarmpriority-alarmstate-basenode-double-basenode-basenode-double-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Alarming with the specified name, description, and configuration. This constructor uses a constant to specify the UpperLimit and a channel to specify the LowerLimit within which AlarmChannel must stay to avoid triggering the alarm. SyntaxNamespace: NationalInstruments.V

### Alarming(string, string, AlarmPriority, AlarmState, BaseNode, double, BaseNode, BaseNode, double, BaseNode)

Initializes a new instance of [Alarming](nationalinstruments-veristand-systemdefinitionapi-alarming.html) with the specified name, description, and configuration. This constructor uses a constant to specify the *UpperLimit*  and a channel to specify the *LowerLimit*  within which *AlarmChannel*  must stay to avoid triggering the alarm.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Alarming(string Name, string Description, AlarmPriority Priority, AlarmState DefaultState, BaseNode Alarm, double Delay, BaseNode Procedure, BaseNode AlarmChannel, double UpperLimit, BaseNode LowerLimit)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alarming step. |
| Description | string | The description of the Alarming step. |
| Priority | AlarmPriority | The AlarmPriority level (Low, Medium, or High). |
| DefaultState | AlarmState | The default AlarmState (Enabled or Disabled). |
| Alarm | BaseNode | The Alarm to configure. If this is null, use the tripped alarm which triggered the procedure. |
| Delay | double | The amount of time to wait before triggering the alarm. |
| Procedure | BaseNode | The Procedure to initiate when the alarm occurs. |
| AlarmChannel | BaseNode | The channel to monitor for alarm conditions. |
| UpperLimit | double | The constant that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. |
| LowerLimit | BaseNode | The channel that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. |

Parent topic:

Alarming Class
