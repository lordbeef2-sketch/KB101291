# NI DOCUMENT BUNDLE: veristand-net-api-ref

<!--NI_BUNDLE_CHUNK bundle=veristand-net-api-ref start=2501 end=2750 -->
<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtaskai-acquisitionsamples.html language=enus -->
## TOPIC 02501: AcquisitionSamples

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtaskai-acquisitionsamples.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtaskai-acquisitionsamples.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the total number of samples per channel to acquire. This property is valid for instances of DAQTaskAI that perform finite acquisitions. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint AcquisitionSamples { get; set; }ReturnsThe total number of samples per ch

### AcquisitionSamples

Gets or sets the total number of samples per channel to acquire. This property is valid for instances of [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html) that perform finite acquisitions.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint AcquisitionSamples { get; set; }

#### Returns

The total number of samples per channel to acquire. The default value is the task ([Rate](nationalinstruments-veristand-systemdefinitionapi-daqtaskai-rate.html) / 10).

#### See Also

- NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.AcquisitionMode
- NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.AcquisitionUnits

Parent topic:

DAQTaskAI Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtaskai-acquisitiontime.html language=enus -->
## TOPIC 02502: AcquisitionTime

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtaskai-acquisitiontime.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtaskai-acquisitiontime.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the total number of seconds to acquire data. This property is valid for instances of DAQTaskAI that perform finite acquisitions. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double AcquisitionTime { get; set; }ReturnsThe total number of seconds to acquire dat

### AcquisitionTime

Gets or sets the total number of seconds to acquire data. This property is valid for instances of [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html) that perform finite acquisitions.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double AcquisitionTime { get; set; }

#### Returns

The total number of seconds to acquire data. The default value is 0.1 seconds.

#### See Also

- NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.AcquisitionMode
- NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.AcquisitionUnits

Parent topic:

DAQTaskAI Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtaskai-acquisitionunits.html language=enus -->
## TOPIC 02503: AcquisitionUnits

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtaskai-acquisitionunits.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtaskai-acquisitionunits.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the task uses time in seconds or number of samples as the size of the acquisitions it performs. This property is valid for instances of DAQTaskAI that perform finite acquisitions. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic AcquisitionUnits Acquisiti

### AcquisitionUnits

Gets or sets whether the task uses time in seconds or number of samples as the size of the acquisitions it performs. This property is valid for instances of [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html) that perform finite acquisitions.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [AcquisitionUnits](nationalinstruments-veristand-systemdefinitionapi-acquisitionunits.html) AcquisitionUnits { get; set; }

#### Returns

An enumeration of [AcquisitionUnits](nationalinstruments-veristand-systemdefinitionapi-acquisitionunits.html). The default value is [Seconds](nationalinstruments-veristand-systemdefinitionapi-acquisitionunits.html).

#### See Also

- NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.AcquisitionSamples
- NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.AcquisitionTime
- NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.AcquisitionMode

Parent topic:

DAQTaskAI Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtaskai-activeedge.html language=enus -->
## TOPIC 02504: ActiveEdge

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtaskai-activeedge.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtaskai-activeedge.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the type of edge in the pulses of the sample clock that cause the task to acquire samples: rising or falling. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic EdgeType ActiveEdge { get; set; }ReturnsAn enumeration of EdgeType. The default value is Rising.

### ActiveEdge

Gets or sets the type of edge in the pulses of the sample clock that cause the task to acquire samples: rising or falling.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [EdgeType](nationalinstruments-veristand-systemdefinitionapi-edgetype.html) ActiveEdge { get; set; }

#### Returns

An enumeration of [EdgeType](nationalinstruments-veristand-systemdefinitionapi-edgetype.html). The default value is [Rising](nationalinstruments-veristand-systemdefinitionapi-edgetype.html).

Parent topic:

DAQTaskAI Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtaskai-automaticreadsize.html language=enus -->
## TOPIC 02505: AutomaticReadSize

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtaskai-automaticreadsize.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtaskai-automaticreadsize.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether to automatically determine the size of read operations that make up an acquisition. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AutomaticReadSize { get; set; }RemarksIf you enable logging, NI VeriStand adjusts the read size to

### AutomaticReadSize

Gets or sets a value indicating whether to automatically determine the size of read operations that make up an acquisition.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AutomaticReadSize { get; set; }

#### Remarks

If you enable logging, NI VeriStand adjusts the read size to be divisible by the sector size of the disk.

#### Returns

true to automatically use a read size of 0.1 seconds. false to use the read size from either the [ReadSamples](nationalinstruments-veristand-systemdefinitionapi-daqtaskai-readsamples.html) or [ReadTime](nationalinstruments-veristand-systemdefinitionapi-daqtaskai-readtime.html) properties. The property value used depends on the value of the [ReadUnits](nationalinstruments-veristand-systemdefinitionapi-daqtaskai-readunits.html) property.

Parent topic:

DAQTaskAI Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtaskai-channelnames.html language=enus -->
## TOPIC 02506: ChannelNames

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtaskai-channelnames.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtaskai-channelnames.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value that indicates how the names of AI channels appear in log files that this task creates. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ChannelNames ChannelNames { get; set; }ReturnsAn enumeration of ChannelNames. The default value is PhysicalChannel.

### ChannelNames

Gets or sets a value that indicates how the names of AI channels appear in log files that this task creates.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ChannelNames](nationalinstruments-veristand-systemdefinitionapi-channelnames.html) ChannelNames { get; set; }

#### Returns

An enumeration of [ChannelNames](nationalinstruments-veristand-systemdefinitionapi-channelnames.html). The default value is [PhysicalChannel](nationalinstruments-veristand-systemdefinitionapi-channelnames.html).

Parent topic:

DAQTaskAI Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtaskai-clocksource.html language=enus -->
## TOPIC 02507: ClockSource

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtaskai-clocksource.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtaskai-clocksource.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the source terminal of the sample clock that you want to control acquisition timing. An empty string corresponds to the default onboard clock of the device. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string ClockSource { get; set; }RemarksRefer to the NI-DA

### ClockSource

Gets or sets the source terminal of the sample clock that you want to control acquisition timing. An empty string corresponds to the default onboard clock of the device.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string ClockSource { get; set; }

#### Remarks

Refer to the *NI-DAQmx Device Terminals Help* to find the signal names for devices supported in NI-DAQmx.

#### Returns

The name of the terminal of the sample clock. The default value is an empty string.

Parent topic:

DAQTaskAI Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtaskai-daqtaskai__string-double-acquisitionmode.html language=enus -->
## TOPIC 02508: DAQTaskAI(string, double, AcquisitionMode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtaskai-daqtaskai__string-double-acquisitionmode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtaskai-daqtaskai__string-double-acquisitionmode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQTaskAI class with the specified name, rate, and acquisition mode. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQTaskAI(string name, double rate, AcquisitionMode mode)ParametersNameTypeDescriptionnamestringThe name of the task.ratedou

### DAQTaskAI(string, double, AcquisitionMode)

Initializes a new instance of the [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html) class with the specified name, rate, and acquisition mode.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQTaskAI(string name, double rate, AcquisitionMode mode)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the task. |
| rate | double | The sampling rate, in Hz, at which to acquire data from each channel. |
| mode | AcquisitionMode | The acquisition mode (finite or continuous). |

Parent topic:

DAQTaskAI Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtaskai-getdevices.html language=enus -->
## TOPIC 02509: GetDevices()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtaskai-getdevices.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtaskai-getdevices.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets all of the DAQ devices associated with the DAQTaskAI. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQDevice[] GetDevices()ReturnsAn array of DAQDevice objects associated with the DAQTaskAI.

### GetDevices()

Gets all of the DAQ devices associated with the [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html)[] GetDevices()

#### Returns

An array of [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html) objects associated with the [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html).

Parent topic:

DAQTaskAI Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtaskai-getlogging.html language=enus -->
## TOPIC 02510: GetLogging()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtaskai-getlogging.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtaskai-getlogging.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Logging section under the current DAQTaskAI. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQLogging GetLogging()ReturnsThe DAQLogging section.

### GetLogging()

Gets the **Logging** section under the current [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQLogging](nationalinstruments-veristand-systemdefinitionapi-daqlogging.html) GetLogging()

#### Returns

The [DAQLogging](nationalinstruments-veristand-systemdefinitionapi-daqlogging.html) section.

Parent topic:

DAQTaskAI Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtaskai-gettaskenabledchannel.html language=enus -->
## TOPIC 02511: GetTaskEnabledChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtaskai-gettaskenabledchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtaskai-gettaskenabledchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Task Enabled channel under the current DAQTaskAI. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQTaskCommand GetTaskEnabledChannel()ReturnsA DAQTaskCommand reference to the Task Enabled channel.

### GetTaskEnabledChannel()

Gets the Task Enabled channel under the current [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQTaskCommand](nationalinstruments-veristand-systemdefinitionapi-daqtaskcommand.html) GetTaskEnabledChannel()

#### Returns

A [DAQTaskCommand](nationalinstruments-veristand-systemdefinitionapi-daqtaskcommand.html) reference to the Task Enabled channel.

Parent topic:

DAQTaskAI Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtaskai-gettriggers.html language=enus -->
## TOPIC 02512: GetTriggers()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtaskai-gettriggers.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtaskai-gettriggers.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Triggers section under the current DAQTaskAI. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQTriggers GetTriggers()ReturnsThe DAQTriggers section.

### GetTriggers()

Gets the **Triggers** section under the current [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQTriggers](nationalinstruments-veristand-systemdefinitionapi-daqtriggers.html) GetTriggers()

#### Returns

The [DAQTriggers](nationalinstruments-veristand-systemdefinitionapi-daqtriggers.html) section.

Parent topic:

DAQTaskAI Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtaskai-rate.html language=enus -->
## TOPIC 02513: Rate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtaskai-rate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtaskai-rate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the sampling rate, in samples per channel per second, or Hz. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double Rate { get; set; }ReturnsThe sample rate.

### Rate

Gets or sets the sampling rate, in samples per channel per second, or Hz.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double Rate { get; set; }

#### Returns

The sample rate.

Parent topic:

DAQTaskAI Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtaskai-readsamples.html language=enus -->
## TOPIC 02514: ReadSamples

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtaskai-readsamples.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtaskai-readsamples.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the requested number of samples per channel to read at a time. This property is valid if AutomaticReadSize is false. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint ReadSamples { get; set; }RemarksThe interval, in seconds, at which the task performs reads i

### ReadSamples

Gets or sets the requested number of samples per channel to read at a time. This property is valid if [AutomaticReadSize](nationalinstruments-veristand-systemdefinitionapi-daqtaskai-automaticreadsize.html) is false.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint ReadSamples { get; set; }

#### Remarks

ReadSamples

Rate

Note

Reading small amounts of data makes the data available to the system sooner, but those operations consume system resources.

#### Returns

The number of samples per channel to read at a time. The default value is ([Rate](nationalinstruments-veristand-systemdefinitionapi-daqtaskai-rate.html) / 10).

Parent topic:

DAQTaskAI Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtaskai-readtime.html language=enus -->
## TOPIC 02515: ReadTime

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtaskai-readtime.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtaskai-readtime.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the number of seconds to read at a time. This property is valid if AutomaticReadSize is false. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double ReadTime { get; set; }RemarksThe samples per channel the task reads is equal to ReadTime / Rate. Reading small a

### ReadTime

Gets or sets the number of seconds to read at a time. This property is valid if [AutomaticReadSize](nationalinstruments-veristand-systemdefinitionapi-daqtaskai-automaticreadsize.html) is false.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double ReadTime { get; set; }

#### Remarks

ReadTime

Rate

Note

Reading small amounts of data makes the data available to the system sooner, but those operations consume system resources.

#### Returns

The number of seconds to read.

Parent topic:

DAQTaskAI Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtaskai-readunits.html language=enus -->
## TOPIC 02516: ReadUnits

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtaskai-readunits.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtaskai-readunits.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the task uses ReadTime or ReadSamples as the read size. This property is valid for instances of DAQTaskAI that do not automatically determine the read size. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic AcquisitionUnits ReadUnits { get; set; }ReturnsAn

### ReadUnits

Gets or sets whether the task uses [ReadTime](nationalinstruments-veristand-systemdefinitionapi-daqtaskai-readtime.html) or [ReadSamples](nationalinstruments-veristand-systemdefinitionapi-daqtaskai-readsamples.html) as the read size. This property is valid for instances of [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html) that do not automatically determine the read size.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [AcquisitionUnits](nationalinstruments-veristand-systemdefinitionapi-acquisitionunits.html) ReadUnits { get; set; }

#### Returns

An enumeration of [AcquisitionUnits](nationalinstruments-veristand-systemdefinitionapi-acquisitionunits.html). The default value is [Seconds](nationalinstruments-veristand-systemdefinitionapi-acquisitionunits.html).

#### See Also

- NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.ReadSamples
- NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.ReadTime
- NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.AutomaticReadSize

Parent topic:

DAQTaskAI Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html language=enus -->
## TOPIC 02517: DAQTaskAI Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a DAQmx task you can assign to one or more DAQ analog input channels to configure timing properties, triggers, and logging. Derives fromDAQTaskSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQTaskAI : DAQTaskRemarksUse WaveformAnalogInputTask to assign a D

### DAQTaskAI Class

Represents a DAQmx task you can assign to one or more DAQ analog input channels to configure timing properties, triggers, and logging.

#### Derives from

- DAQTask

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQTaskAI : DAQTask

#### Remarks

Use [WaveformAnalogInputTask](nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-waveformanaloginputtask.html) to assign a DAQTaskAI instance to the analog input channels of a [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html).

**Accessing this Class**

- [GetTaskList()](nationalinstruments-veristand-systemdefinitionapi-daqtasks-gettasklist.html)
- DAQTaskAI Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| DAQTaskAI(string, double, AcquisitionMode) | Initializes a new instance of the DAQTaskAI class with the specified name, rate, and acquisition mode. |

#### Properties

| Name | Description |
| --- | --- |
| AcquisitionMode | Gets or sets the type of acquisition the task performs. |
| AcquisitionSamples | Gets or sets the total number of samples per channel to acquire. This property is valid for instances of DAQTaskAI that perform finite acquisitions. |
| AcquisitionTime | Gets or sets the total number of seconds to acquire data. This property is valid for instances of DAQTaskAI that perform finite acquisitions. |
| AcquisitionUnits | Gets or sets whether the task uses time in seconds or number of samples as the size of the acquisitions it performs. This property is valid for instances of DAQTaskAI that perform finite acquisitions. |
| ActiveEdge | Gets or sets the type of edge in the pulses of the sample clock that cause the task to acquire samples: rising or falling. |
| AutomaticReadSize | Gets or sets a value indicating whether to automatically determine the size of read operations that make up an acquisition. |
| ChannelNames | Gets or sets a value that indicates how the names of AI channels appear in log files that this task creates. |
| ClockSource | Gets or sets the source terminal of the sample clock that you want to control acquisition timing. An empty string corresponds to the default onboard clock of the device. |
| Rate | Gets or sets the sampling rate, in samples per channel per second, or Hz. |
| ReadSamples | Gets or sets the requested number of samples per channel to read at a time. This property is valid if AutomaticReadSize is false. |
| ReadTime | Gets or sets the number of seconds to read at a time. This property is valid if AutomaticReadSize is false. |
| ReadUnits | Gets or sets whether the task uses ReadTime or ReadSamples as the read size. This property is valid for instances of DAQTaskAI that do not automatically determine the read size. |

#### Methods

| Name | Description |
| --- | --- |
| GetDevices() | Gets all of the DAQ devices associated with the DAQTaskAI. |
| GetLogging() | Gets the Logging section under the current DAQTaskAI. |
| GetTaskEnabledChannel() | Gets the Task Enabled channel under the current DAQTaskAI. |
| GetTriggers() | Gets the Triggers section under the current DAQTaskAI. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtaskcommand-initialvalue.html language=enus -->
## TOPIC 02518: InitialValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtaskcommand-initialvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtaskcommand-initialvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether the channel is initially enabled or disabled. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool InitialValue { get; set; }Returnstrue to enable the channel; false to disable.

### InitialValue

Gets or sets a value indicating whether the channel is initially enabled or disabled.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool InitialValue { get; set; }

#### Returns

true to enable the channel; false to disable.

Parent topic:

DAQTaskCommand Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtaskcommand.html language=enus -->
## TOPIC 02519: DAQTaskCommand Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtaskcommand.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtaskcommand.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents one of the channels under the DAQTaskAI, DAQTriggers, or DAQLogging sections. Task command channels control the execution of the DAQTaskAI. Derives fromChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQTaskCommand : ChannelRemarksAccessing this Class

### DAQTaskCommand Class

Represents one of the channels under the [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html), [DAQTriggers](nationalinstruments-veristand-systemdefinitionapi-daqtriggers.html), or [DAQLogging](nationalinstruments-veristand-systemdefinitionapi-daqlogging.html) sections. Task command channels control the execution of the [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html).

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQTaskCommand : Channel

#### Remarks

Accessing this Class

- [GetTaskEnabledChannel](nationalinstruments-veristand-systemdefinitionapi-daqtaskai-gettaskenabledchannel.html)
- [GetLoggingEnabledChannel](nationalinstruments-veristand-systemdefinitionapi-daqlogging-getloggingenabledchannel.html)
- [GetStartNewFileChannel](nationalinstruments-veristand-systemdefinitionapi-daqlogging-getstartnewfilechannel.html)
- [GetRetriggerableChannel](nationalinstruments-veristand-systemdefinitionapi-daqtriggers-getretriggerablechannel.html)
- [GetStartTriggerChannel](nationalinstruments-veristand-systemdefinitionapi-daqtriggers-getstarttriggerchannel.html)

Refer to *Waveform Task Channels* in the *NI VeriStand Help* for information about each type of DAQTaskCommand channel.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| InitialValue | Gets or sets a value indicating whether the channel is initially enabled or disabled. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtasks-addtask__daqtask-out.html language=enus -->
## TOPIC 02520: AddTask(DAQTask, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtasks-addtask__daqtask-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtasks-addtask__daqtask-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified DAQTask to the DAQTasks section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddTask(DAQTask task, out Error error)ParametersNameTypeDescriptiontaskDAQTaskThe instance of DAQTask to add.errorout ErrorReturns an NationalInstruments.VeriStand.Error

### AddTask(DAQTask, out Error)

Adds the specified [DAQTask](nationalinstruments-veristand-systemdefinitionapi-daqtask.html) to the [DAQTasks](nationalinstruments-veristand-systemdefinitionapi-daqtasks.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddTask(DAQTask task, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| task | DAQTask | The instance of DAQTask to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [DAQTask](nationalinstruments-veristand-systemdefinitionapi-daqtask.html) was added successfully.

Parent topic:

DAQTasks Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtasks-addtask__daqtask.html language=enus -->
## TOPIC 02521: AddTask(DAQTask)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtasks-addtask__daqtask.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtasks-addtask__daqtask.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified DAQTask to the DAQTasks section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddTask(DAQTask task)ParametersNameTypeDescriptiontaskDAQTaskThe instance of DAQTask to add.Returnstrue if the DAQTask was added successfully.

### AddTask(DAQTask)

Adds the specified [DAQTask](nationalinstruments-veristand-systemdefinitionapi-daqtask.html) to the [DAQTasks](nationalinstruments-veristand-systemdefinitionapi-daqtasks.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddTask(DAQTask task)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| task | DAQTask | The instance of DAQTask to add. |

#### Returns

true if the [DAQTask](nationalinstruments-veristand-systemdefinitionapi-daqtask.html) was added successfully.

Parent topic:

DAQTasks Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtasks-gettasklist.html language=enus -->
## TOPIC 02522: GetTaskList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtasks-gettasklist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtasks-gettasklist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the DAQTask elements from the current DAQTasks section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQTask[] GetTaskList()ReturnsAn array that contains the DAQTask elements from the current DAQTasks section.

### GetTaskList()

Gets an array that contains the [DAQTask](nationalinstruments-veristand-systemdefinitionapi-daqtask.html) elements from the current [DAQTasks](nationalinstruments-veristand-systemdefinitionapi-daqtasks.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQTask](nationalinstruments-veristand-systemdefinitionapi-daqtask.html)[] GetTaskList()

#### Returns

An array that contains the [DAQTask](nationalinstruments-veristand-systemdefinitionapi-daqtask.html) elements from the current [DAQTasks](nationalinstruments-veristand-systemdefinitionapi-daqtasks.html) section.

Parent topic:

DAQTasks Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtasks-reordertasklist__daqtask_arr1-out.html language=enus -->
## TOPIC 02523: ReorderTaskList(DAQTask[], out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtasks-reordertasklist__daqtask_arr1-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtasks-reordertasklist__daqtask_arr1-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes the order in which the VeriStand Engine starts DAQTask objects. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool ReorderTaskList(DAQTask[] tasks, out Error error)RemarksSetting the execution order for tasks is useful if you want to synchronize the start of multip

### ReorderTaskList(DAQTask[], out Error)

Changes the order in which the VeriStand Engine starts [DAQTask](nationalinstruments-veristand-systemdefinitionapi-daqtask.html) objects.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool ReorderTaskList(DAQTask[] tasks, out Error error)

#### Remarks

Setting the execution order for tasks is useful if you want to synchronize the start of multiple tasks that are triggered off of each other.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| tasks | DAQTask[] | An array of DAQTask objects in the order you want the VeriStand Engine to start them. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [DAQTask](nationalinstruments-veristand-systemdefinitionapi-daqtask.html) objects were reordered successfully.

Parent topic:

DAQTasks Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtasks-reordertasklist__daqtask_arr1.html language=enus -->
## TOPIC 02524: ReorderTaskList(DAQTask[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtasks-reordertasklist__daqtask_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtasks-reordertasklist__daqtask_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes the order in which the VeriStand Engine starts DAQTask objects. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool ReorderTaskList(DAQTask[] tasks)RemarksSetting the execution order for tasks is useful if you want to synchronize the start of multiple tasks that are

### ReorderTaskList(DAQTask[])

Changes the order in which the VeriStand Engine starts [DAQTask](nationalinstruments-veristand-systemdefinitionapi-daqtask.html) objects.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool ReorderTaskList(DAQTask[] tasks)

#### Remarks

Setting the execution order for tasks is useful if you want to synchronize the start of multiple tasks that are triggered off of each other.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| tasks | DAQTask[] | An array of DAQTask objects in the order you want the VeriStand Engine to start them. |

#### Returns

true if the [DAQTask](nationalinstruments-veristand-systemdefinitionapi-daqtask.html) objects were reordered successfully.

Parent topic:

DAQTasks Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtasks.html language=enus -->
## TOPIC 02525: DAQTasks Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtasks.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtasks.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Waveform Tasks section in a system definition. This section contains DAQTask objects. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQTasks : SectionRemarksUse the members of this class to add a new DAQTask or access an existing tas

### DAQTasks Class

Represents the **Waveform Tasks** section in a system definition. This section contains [DAQTask](nationalinstruments-veristand-systemdefinitionapi-daqtask.html) objects.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQTasks : Section

#### Remarks

Use the members of this class to add a new [DAQTask](nationalinstruments-veristand-systemdefinitionapi-daqtask.html) or access an existing task.

**Accessing this Class**

- [GetTasks](nationalinstruments-veristand-systemdefinitionapi-daq-gettasks.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddTask(DAQTask) | Adds the specified DAQTask to the DAQTasks section. |
| AddTask(DAQTask, out Error) | Adds the specified DAQTask to the DAQTasks section. |
| GetTaskList() | Gets an array that contains the DAQTask elements from the current DAQTasks section. |
| ReorderTaskList(DAQTask[], out Error) | Changes the order in which the VeriStand Engine starts DAQTask objects. |
| ReorderTaskList(DAQTask[]) | Changes the order in which the VeriStand Engine starts DAQTask objects. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtrigger-triggertype.html language=enus -->
## TOPIC 02526: TriggerType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtrigger-triggertype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtrigger-triggertype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the type of the DAQTrigger. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic TriggerType TriggerType { get; set; }ReturnsAn enumeration of TriggerType.

### TriggerType

Gets the type of the [DAQTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [TriggerType](nationalinstruments-veristand-systemdefinitionapi-triggertype.html) TriggerType { get; set; }

#### Returns

An enumeration of [TriggerType](nationalinstruments-veristand-systemdefinitionapi-triggertype.html).

Parent topic:

DAQTrigger Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtrigger.html language=enus -->
## TOPIC 02527: DAQTrigger Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtrigger.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtrigger.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides an abstract base class for different types of triggers you can use to configure a DAQTaskAI to start acquiring under certain conditions. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQTriggerThread SafetyAny members of this type are not gua

### DAQTrigger Class

Provides an abstract base class for different types of triggers you can use to configure a [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html) to start acquiring under certain conditions.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQTrigger

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| TriggerType | Gets the type of the DAQTrigger. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogedge-daqtriggeranalogedge__string-directiontype-double.html language=enus -->
## TOPIC 02528: DAQTriggerAnalogEdge(string, DirectionType, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogedge-daqtriggeranalogedge__string-directiontype-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogedge-daqtriggeranalogedge__string-directiontype-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQTriggerAnalogEdge class with the specified source, slope, and threshold level. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQTriggerAnalogEdge(string source, DirectionType slope, double level)ParametersNameTypeDescriptionsourcestring

### DAQTriggerAnalogEdge(string, DirectionType, double)

Initializes a new instance of the [DAQTriggerAnalogEdge](nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogedge.html) class with the specified source, slope, and threshold level.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQTriggerAnalogEdge(string source, DirectionType slope, double level)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | The name of a virtual channel or terminal that is the source of the analog signal used as the trigger. For E Series DAQ devices, if you specify a channel name as source, the channel must be the first channel in the task. Also, the only terminal you can use for E Series devices is PFI0. |
| slope | DirectionType | A DirectionType value that specifies the direction of a signal slope that causes a trigger when the signal crosses the threshold level . |
| level | double | The threshold value, in the units of the measurement, at which to start acquiring samples. Set the slope to specify on which type of slope the level causes the task to start acquiring data. |

Parent topic:

DAQTriggerAnalogEdge Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogedge-level.html language=enus -->
## TOPIC 02529: Level

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogedge-level.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogedge-level.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the threshold value, in the units of the measurement, at which to start acquiring samples. Set the Slope to specify on which type of slope this level causes the task to start acquiring data. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double Level { get; set

### Level

Gets or sets the threshold value, in the units of the measurement, at which to start acquiring samples. Set the [Slope](nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogedge-slope.html) to specify on which type of slope this level causes the task to start acquiring data.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double Level { get; set; }

#### Returns

The numeric value of the threshold level.

Parent topic:

DAQTriggerAnalogEdge Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogedge-slope.html language=enus -->
## TOPIC 02530: Slope

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogedge-slope.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogedge-slope.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the direction of a signal slope that causes a trigger when the signal crosses the threshold Level. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DirectionType Slope { get; set; }ReturnsAn enumeration of DirectionType.

### Slope

Gets or sets the direction of a signal slope that causes a trigger when the signal crosses the threshold [Level](nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogedge-level.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DirectionType](nationalinstruments-veristand-systemdefinitionapi-directiontype.html) Slope { get; set; }

#### Returns

An enumeration of [DirectionType](nationalinstruments-veristand-systemdefinitionapi-directiontype.html).

Parent topic:

DAQTriggerAnalogEdge Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogedge-source.html language=enus -->
## TOPIC 02531: Source

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogedge-source.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogedge-source.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of a virtual channel or terminal that is the source of the analog signal used as the trigger. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Source { get; set; }RemarksFor E Series DAQ devices, if you specify a channel name as source, the channe

### Source

Gets or sets the name of a virtual channel or terminal that is the source of the analog signal used as the trigger.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Source { get; set; }

#### Remarks

For E Series DAQ devices, if you specify a channel name as source, the channel must be the first channel in the task. Also, the only terminal you can use for E Series devices is PFI0.

Refer to the *NI-DAQmx Device Terminals Help* to find terminal names for devices supported in NI-DAQmx.

Parent topic:

DAQTriggerAnalogEdge Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogedge.html language=enus -->
## TOPIC 02532: DAQTriggerAnalogEdge Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogedge.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogedge.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an analog edge trigger that can configure a DAQTaskAI to start acquiring under certain conditions. Derives fromDAQTriggerSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQTriggerAnalogEdge : DAQTriggerRemarksUse the members of this class to create and confi

### DAQTriggerAnalogEdge Class

Represents an analog edge trigger that can configure a [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html) to start acquiring under certain conditions.

#### Derives from

- DAQTrigger

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQTriggerAnalogEdge : DAQTrigger

#### Remarks

Use the members of this class to create and configure an analog edge trigger you can set as the [StartTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtriggers-starttrigger.html) or [ReferenceTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtriggers-referencetrigger.html) for the [DAQTriggers](nationalinstruments-veristand-systemdefinitionapi-daqtriggers.html) section of a [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html).

An analog edge trigger starts acquisitions when an analog signal crosses a threshold [Level](nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogedge-level.html) on a particular type of [Slope](nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogedge-slope.html).

**Accessing this Class**

- DAQTriggerAnalogEdge Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| DAQTriggerAnalogEdge(string, DirectionType, double) | Initializes a new instance of the DAQTriggerAnalogEdge class with the specified source, slope, and threshold level. |

#### Properties

| Name | Description |
| --- | --- |
| Level | Gets or sets the threshold value, in the units of the measurement, at which to start acquiring samples. Set the Slope to specify on which type of slope this level causes the task to start acquiring data. |
| Slope | Gets or sets the direction of a signal slope that causes a trigger when the signal crosses the threshold Level. |
| Source | Gets or sets the name of a virtual channel or terminal that is the source of the analog signal used as the trigger. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogwindow-daqtriggeranalogwindow__string-double-double-windowconditiontype.html language=enus -->
## TOPIC 02533: DAQTriggerAnalogWindow(string, double, double, WindowConditionType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogwindow-daqtriggeranalogwindow__string-double-double-windowconditiontype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogwindow-daqtriggeranalogwindow__string-double-double-windowconditiontype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQTriggerAnalogWindow class with the specified source, window top, window bottom, and window condition. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQTriggerAnalogWindow(string source, double windowTop, double windowBottom, WindowCondi

### DAQTriggerAnalogWindow(string, double, double, WindowConditionType)

Initializes a new instance of the [DAQTriggerAnalogWindow](nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogwindow.html) class with the specified source, window top, window bottom, and window condition.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQTriggerAnalogWindow(string source, double windowTop, double windowBottom, WindowConditionType windowCondition)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | The name of a virtual channel or terminal that is the source of the analog signal used as the trigger. For E Series DAQ devices, if you specify a channel name as source, the channel must be the first channel in the task. Also, the only terminal you can use for E Series devices is PFI0. |
| windowTop | double | The upper limit of the window, in the units of the measurement. |
| windowBottom | double | The lower limit of the window, in the units of the measurement. |
| windowCondition | WindowConditionType | A WindowConditionType value that specifies whether the task starts acquiring samples when the signal enters the window between windowBottom and windowTop or when it leaves the window. |

Parent topic:

DAQTriggerAnalogWindow Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogwindow-source.html language=enus -->
## TOPIC 02534: Source

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogwindow-source.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogwindow-source.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of a virtual channel or terminal that is the source of the analog signal used as the trigger. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Source { get; set; }RemarksFor E Series DAQ devices, if you specify a channel name as source, the channe

### Source

Gets or sets the name of a virtual channel or terminal that is the source of the analog signal used as the trigger.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Source { get; set; }

#### Remarks

For E Series DAQ devices, if you specify a channel name as source, the channel must be the first channel in the task. Also, the only terminal you can use for E Series devices is PFI0.

Parent topic:

DAQTriggerAnalogWindow Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogwindow-windowbottom.html language=enus -->
## TOPIC 02535: WindowBottom

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogwindow-windowbottom.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogwindow-windowbottom.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the lower limit of the window, in the units of the measurement. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double WindowBottom { get; set; }ReturnsThe numeric value of the lower limit.

### WindowBottom

Gets or sets the lower limit of the window, in the units of the measurement.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double WindowBottom { get; set; }

#### Returns

The numeric value of the lower limit.

Parent topic:

DAQTriggerAnalogWindow Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogwindow-windowcondition.html language=enus -->
## TOPIC 02536: WindowCondition

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogwindow-windowcondition.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogwindow-windowcondition.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the task starts acquiring samples when the signal enters the window between WindowBottom and WindowTop or when it leaves the window. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic WindowConditionType WindowCondition { get; set; }ReturnsAn enumeration of

### WindowCondition

Gets or sets whether the task starts acquiring samples when the signal enters the window between [WindowBottom](nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogwindow-windowbottom.html) and [WindowTop](nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogwindow-windowtop.html) or when it leaves the window.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [WindowConditionType](nationalinstruments-veristand-systemdefinitionapi-windowconditiontype.html) WindowCondition { get; set; }

#### Returns

An enumeration of [WindowConditionType](nationalinstruments-veristand-systemdefinitionapi-windowconditiontype.html).

Parent topic:

DAQTriggerAnalogWindow Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogwindow-windowtop.html language=enus -->
## TOPIC 02537: WindowTop

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogwindow-windowtop.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogwindow-windowtop.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the upper limit of the window, in the units of the measurement. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double WindowTop { get; set; }ReturnsThe numeric value of the upper limit.

### WindowTop

Gets or sets the upper limit of the window, in the units of the measurement.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double WindowTop { get; set; }

#### Returns

The numeric value of the upper limit.

Parent topic:

DAQTriggerAnalogWindow Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogwindow.html language=enus -->
## TOPIC 02538: DAQTriggerAnalogWindow Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogwindow.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogwindow.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an analog window trigger that can configure a DAQTaskAI to start acquiring under certain conditions. Derives fromDAQTriggerSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQTriggerAnalogWindow : DAQTriggerRemarksUse the members of this class to create and c

### DAQTriggerAnalogWindow Class

Represents an analog window trigger that can configure a [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html) to start acquiring under certain conditions.

#### Derives from

- DAQTrigger

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQTriggerAnalogWindow : DAQTrigger

#### Remarks

Use the members of this class to create and configure an analog window trigger you can set as the [StartTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtriggers-starttrigger.html) or [ReferenceTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtriggers-referencetrigger.html) for the [DAQTriggers](nationalinstruments-veristand-systemdefinitionapi-daqtriggers.html) section of a [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html).

An analog window trigger starts acquisitions when an analog signal either passes into (enters) or passes out of (leaves) a window defined by two voltage levels, [WindowBottom](nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogwindow-windowbottom.html) and [WindowTop](nationalinstruments-veristand-systemdefinitionapi-daqtriggeranalogwindow-windowtop.html).

**Accessing this Class**

- DAQTriggerAnalogWindow Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| DAQTriggerAnalogWindow(string, double, double, WindowConditionType) | Initializes a new instance of the DAQTriggerAnalogWindow class with the specified source, window top, window bottom, and window condition. |

#### Properties

| Name | Description |
| --- | --- |
| Source | Gets or sets the name of a virtual channel or terminal that is the source of the analog signal used as the trigger. |
| WindowBottom | Gets or sets the lower limit of the window, in the units of the measurement. |
| WindowCondition | Gets or sets whether the task starts acquiring samples when the signal enters the window between WindowBottom and WindowTop or when it leaves the window. |
| WindowTop | Gets or sets the upper limit of the window, in the units of the measurement. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggerdigitaledge-daqtriggerdigitaledge__string-directiontype.html language=enus -->
## TOPIC 02539: DAQTriggerDigitalEdge(string, DirectionType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggerdigitaledge-daqtriggerdigitaledge__string-directiontype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggerdigitaledge-daqtriggerdigitaledge__string-directiontype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQTriggerDigitalEdge class with the specified source and edge. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQTriggerDigitalEdge(string source, DirectionType edge)ParametersNameTypeDescriptionsourcestringThe name of a terminal that is t

### DAQTriggerDigitalEdge(string, DirectionType)

Initializes a new instance of the [DAQTriggerDigitalEdge](nationalinstruments-veristand-systemdefinitionapi-daqtriggerdigitaledge.html) class with the specified source and edge.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQTriggerDigitalEdge(string source, DirectionType edge)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | The name of a terminal that is the source of the digital signal used as the trigger. |
| edge | DirectionType | A DirectionType value that specifies on which edge of the digital signal to start acquiring samples. |

Parent topic:

DAQTriggerDigitalEdge Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggerdigitaledge-edge.html language=enus -->
## TOPIC 02540: Edge

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggerdigitaledge-edge.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggerdigitaledge-edge.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets on which type of edge of the digital signal to start acquiring samples. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DirectionType Edge { get; set; }ReturnsAn enumeration of DirectionType.

### Edge

Gets or sets on which type of edge of the digital signal to start acquiring samples.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DirectionType](nationalinstruments-veristand-systemdefinitionapi-directiontype.html) Edge { get; set; }

#### Returns

An enumeration of [DirectionType](nationalinstruments-veristand-systemdefinitionapi-directiontype.html).

Parent topic:

DAQTriggerDigitalEdge Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggerdigitaledge-source.html language=enus -->
## TOPIC 02541: Source

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggerdigitaledge-source.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggerdigitaledge-source.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of a terminal that is the source of the digital signal used as the trigger. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Source { get; set; }RemarksRefer to the NI-DAQmx Device Terminals Help to find terminal names for devices supported in NI-

### Source

Gets or sets the name of a terminal that is the source of the digital signal used as the trigger.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Source { get; set; }

#### Remarks

Refer to the *NI-DAQmx Device Terminals Help* to find terminal names for devices supported in NI-DAQmx.

#### Returns

The name of a terminal.

Parent topic:

DAQTriggerDigitalEdge Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggerdigitaledge.html language=enus -->
## TOPIC 02542: DAQTriggerDigitalEdge Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggerdigitaledge.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggerdigitaledge.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a digital edge trigger that can configure a DAQTaskAI to start acquiring under certain conditions. Derives fromDAQTriggerSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQTriggerDigitalEdge : DAQTriggerRemarksUse the members of this class to create and conf

### DAQTriggerDigitalEdge Class

Represents a digital edge trigger that can configure a [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html) to start acquiring under certain conditions.

#### Derives from

- DAQTrigger

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQTriggerDigitalEdge : DAQTrigger

#### Remarks

Use the members of this class to create and configure a digital edge trigger you can set as the [StartTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtriggers-starttrigger.html) or [ReferenceTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtriggers-referencetrigger.html) for the [DAQTriggers](nationalinstruments-veristand-systemdefinitionapi-daqtriggers.html) section of a [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html).

A digital edge trigger starts acquisitions when the signal moves from high to low (falling) or from low to high (rising).

**Accessing this Class**

- DAQTriggerDigitalEdge Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| DAQTriggerDigitalEdge(string, DirectionType) | Initializes a new instance of the DAQTriggerDigitalEdge class with the specified source and edge. |

#### Properties

| Name | Description |
| --- | --- |
| Edge | Gets or sets on which type of edge of the digital signal to start acquiring samples. |
| Source | Gets or sets the name of a terminal that is the source of the digital signal used as the trigger. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggernone-daqtriggernone.html language=enus -->
## TOPIC 02543: DAQTriggerNone()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggernone-daqtriggernone.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggernone-daqtriggernone.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQTriggerNone class. You can set StartTrigger or ReferenceTrigger as a DAQTriggerNone object to disable those triggers for a DAQTaskAI. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQTriggerNone()

### DAQTriggerNone()

Initializes a new instance of the [DAQTriggerNone](nationalinstruments-veristand-systemdefinitionapi-daqtriggernone.html) class. You can set [StartTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtriggers-starttrigger.html) or [ReferenceTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtriggers-referencetrigger.html) as a [DAQTriggerNone](nationalinstruments-veristand-systemdefinitionapi-daqtriggernone.html) object to disable those triggers for a [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQTriggerNone()

Parent topic:

DAQTriggerNone Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggernone.html language=enus -->
## TOPIC 02544: DAQTriggerNone Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggernone.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggernone.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a disabled DAQTrigger. Derives fromDAQTriggerSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQTriggerNone : DAQTriggerRemarksUse the DAQTriggerNoneconstructor to create a DAQTrigger object you can set as StartTrigger or ReferenceTrigger to disable those tr

### DAQTriggerNone Class

Represents a disabled [DAQTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtrigger.html).

#### Derives from

- DAQTrigger

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQTriggerNone : DAQTrigger

#### Remarks

Use the DAQTriggerNone

constructor to create a [DAQTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtrigger.html) object you can set as [StartTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtriggers-starttrigger.html) or [ReferenceTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtriggers-referencetrigger.html) to disable those triggers for a [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html).

**Accessing this Class**

- DAQTriggerNone Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| DAQTriggerNone() | Initializes a new instance of the DAQTriggerNone class. You can set StartTrigger or ReferenceTrigger as a DAQTriggerNone object to disable those triggers for a DAQTaskAI. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggers-daqtriggers__string.html language=enus -->
## TOPIC 02545: DAQTriggers(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggers-daqtriggers__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggers-daqtriggers__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQTriggers class with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQTriggers(string name)RemarksAccessing this ClassDAQTriggers Constructor ParametersNameTypeDescriptionnamestringThe name of the DAQTriggers section.

### DAQTriggers(string)

Initializes a new instance of the [DAQTriggers](nationalinstruments-veristand-systemdefinitionapi-daqtriggers.html) class with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQTriggers(string name)

#### Remarks

**Accessing this Class**

- DAQTriggers Constructor

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the DAQTriggers section. |

Parent topic:

DAQTriggers Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggers-getretriggerablechannel.html language=enus -->
## TOPIC 02546: GetRetriggerableChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggers-getretriggerablechannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggers-getretriggerablechannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Retriggerable channel under the current DAQTriggers section. This reference is valid only if the section contains a StartTrigger or ReferenceTrigger whose TriggerType is a value other than None. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQTaskCommand GetRetri

### GetRetriggerableChannel()

Gets the Retriggerable channel under the current [DAQTriggers](nationalinstruments-veristand-systemdefinitionapi-daqtriggers.html) section. This reference is valid only if the section contains a [StartTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtriggers-starttrigger.html) or [ReferenceTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtriggers-referencetrigger.html) whose [TriggerType](nationalinstruments-veristand-systemdefinitionapi-triggertype.html) is a value other than [None](nationalinstruments-veristand-systemdefinitionapi-triggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQTaskCommand](nationalinstruments-veristand-systemdefinitionapi-daqtaskcommand.html) GetRetriggerableChannel()

#### Remarks

The value of the Retriggerable channel specifies whether NI VeriStand re-enables the task after an acquisition. For tasks that perform finite acquisitions and have a start and/or reference trigger, you can allow the task to re-arm itself after the acquisition finishes. This feature is useful when you define a trigger to be some signal value, and you want NI VeriStand to automatically acquire every occurrence of that value.

#### Returns

A [DAQTaskCommand](nationalinstruments-veristand-systemdefinitionapi-daqtaskcommand.html) reference to the Retriggerable channel.

Parent topic:

DAQTriggers Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggers-getstarttriggerchannel.html language=enus -->
## TOPIC 02547: GetStartTriggerChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggers-getstarttriggerchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggers-getstarttriggerchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Start Trigger channel under the current DAQTriggers section. This reference is valid only if the section contains a StartTrigger whose TriggerType is Software. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQTaskCommand GetStartTriggerChannel()RemarksThe value of

### GetStartTriggerChannel()

Gets the Start Trigger channel under the current [DAQTriggers](nationalinstruments-veristand-systemdefinitionapi-daqtriggers.html) section. This reference is valid only if the section contains a [StartTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtriggers-starttrigger.html) whose [TriggerType](nationalinstruments-veristand-systemdefinitionapi-triggertype.html) is [Software](nationalinstruments-veristand-systemdefinitionapi-triggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQTaskCommand](nationalinstruments-veristand-systemdefinitionapi-daqtaskcommand.html) GetStartTriggerChannel()

#### Remarks

The value of the Start Trigger channel determines whether a [DAQTriggerSoftware](nationalinstruments-veristand-systemdefinitionapi-daqtriggersoftware.html) trigger starts an acquisition.

#### Returns

A [DAQTaskCommand](nationalinstruments-veristand-systemdefinitionapi-daqtaskcommand.html) reference to the Start Trigger channel.

#### See Also

- NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerSoftware

Parent topic:

DAQTriggers Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggers-pretriggersamples.html language=enus -->
## TOPIC 02548: PretriggerSamples

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggers-pretriggersamples.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggers-pretriggersamples.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the number of samples per channel prior to the ReferenceTrigger to include in the acquisition that begins when the trigger occurs. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint PretriggerSamples { get; set; }RemarksThe number of post-trigger samples per c

### PretriggerSamples

Gets or sets the number of samples per channel prior to the [ReferenceTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtriggers-referencetrigger.html) to include in the acquisition that begins when the trigger occurs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint PretriggerSamples { get; set; }

#### Remarks

The number of *post-trigger* samples per channel in the acquisition is equal to total number of samples per channel, specified by the [AcquisitionSamples](nationalinstruments-veristand-systemdefinitionapi-daqtaskai-acquisitionsamples.html) property of the [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html), minus the PretriggerSamples.

#### Returns

The number of samples per channel prior to the [ReferenceTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtriggers-referencetrigger.html) to include in the acquisition. The default value is 500.

Parent topic:

DAQTriggers Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggers-pretriggertime.html language=enus -->
## TOPIC 02549: PretriggerTime

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggers-pretriggertime.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggers-pretriggertime.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the length of time, in seconds, prior to the ReferenceTrigger to include in the acquisition that begins when the trigger occurs. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double PretriggerTime { get; set; }ReturnsThe number of seconds to acquire data prior

### PretriggerTime

Gets or sets the length of time, in seconds, prior to the [ReferenceTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtriggers-referencetrigger.html) to include in the acquisition that begins when the trigger occurs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double PretriggerTime { get; set; }

#### Returns

The number of seconds to acquire data prior to the trigger. The default value is 0.05 seconds.

Parent topic:

DAQTriggers Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggers-pretriggerunits.html language=enus -->
## TOPIC 02550: PretriggerUnits

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggers-pretriggerunits.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggers-pretriggerunits.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the task uses samples or seconds of time as the size of the pre-trigger acquisition it performs. This property is valid for instances of DAQTrigger that serve as the ReferenceTrigger for the task. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Acquisiti

### PretriggerUnits

Gets or sets whether the task uses samples or seconds of time as the size of the pre-trigger acquisition it performs. This property is valid for instances of [DAQTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtrigger.html) that serve as the [ReferenceTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtriggers-referencetrigger.html) for the task.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [AcquisitionUnits](nationalinstruments-veristand-systemdefinitionapi-acquisitionunits.html) PretriggerUnits { get; set; }

#### Returns

An enumeration of [AcquisitionUnits](nationalinstruments-veristand-systemdefinitionapi-acquisitionunits.html). The default value is [Seconds](nationalinstruments-veristand-systemdefinitionapi-acquisitionunits.html).

Parent topic:

DAQTriggers Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggers-referencetrigger.html language=enus -->
## TOPIC 02551: ReferenceTrigger

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggers-referencetrigger.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggers-referencetrigger.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the DAQTrigger that serves as the reference trigger for current instance of DAQTaskAI. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQTrigger ReferenceTrigger { get; set; }RemarksA reference trigger establishes a reference point in a finite signal around whi

### ReferenceTrigger

Gets or sets the [DAQTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtrigger.html) that serves as the reference trigger for current instance of [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtrigger.html) ReferenceTrigger { get; set; }

#### Remarks

A reference trigger establishes a reference point in a finite signal around which the acquisition occurs. You can include samples that occur prior to a reference trigger in the acquisition. This is useful if you want to ensure that the acquisition includes the signal values that caused the reference trigger.

#### Returns

A reference to a [DAQTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtrigger.html). The default value is no trigger.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentException | The TriggerType of the DAQTrigger is Software. |

Parent topic:

DAQTriggers Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggers-starttrigger.html language=enus -->
## TOPIC 02552: StartTrigger

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggers-starttrigger.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggers-starttrigger.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the DAQTrigger that serves as the start trigger for current instance of DAQTaskAI. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQTrigger StartTrigger { get; set; }RemarksA start trigger begins an acquisition. ReturnsA reference to a DAQTrigger. The default

### StartTrigger

Gets or sets the [DAQTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtrigger.html) that serves as the start trigger for current instance of [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtrigger.html) StartTrigger { get; set; }

#### Remarks

A start trigger begins an acquisition.

#### Returns

A reference to a [DAQTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtrigger.html). The default value is no trigger.

Parent topic:

DAQTriggers Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggers.html language=enus -->
## TOPIC 02553: DAQTriggers Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggers.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggers.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Triggers section of a DAQTaskAI. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQTriggers : SectionRemarksUse the members of this class to create triggers that configure the DAQTaskAI to start acquiring under certain conditions. Acc

### DAQTriggers Class

Represents the **Triggers** section of a [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html).

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQTriggers : Section

#### Remarks

Use the members of this class to create triggers that configure the [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html) to start acquiring under certain conditions.

**Accessing this Class**

- [GetTriggers](nationalinstruments-veristand-systemdefinitionapi-daqtaskai-gettriggers.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| DAQTriggers(string) | Initializes a new instance of the DAQTriggers class with the specified name. |

#### Properties

| Name | Description |
| --- | --- |
| PretriggerSamples | Gets or sets the number of samples per channel prior to the ReferenceTrigger to include in the acquisition that begins when the trigger occurs. |
| PretriggerTime | Gets or sets the length of time, in seconds, prior to the ReferenceTrigger to include in the acquisition that begins when the trigger occurs. |
| PretriggerUnits | Gets or sets whether the task uses samples or seconds of time as the size of the pre-trigger acquisition it performs. This property is valid for instances of DAQTrigger that serve as the ReferenceTrigger for the task. |
| ReferenceTrigger | Gets or sets the DAQTrigger that serves as the reference trigger for current instance of DAQTaskAI. |
| StartTrigger | Gets or sets the DAQTrigger that serves as the start trigger for current instance of DAQTaskAI. |

#### Methods

| Name | Description |
| --- | --- |
| GetRetriggerableChannel() | Gets the Retriggerable channel under the current DAQTriggers section. This reference is valid only if the section contains a StartTrigger or ReferenceTrigger whose TriggerType is a value other than None. |
| GetStartTriggerChannel() | Gets the Start Trigger channel under the current DAQTriggers section. This reference is valid only if the section contains a StartTrigger whose TriggerType is Software. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggersoftware-daqtriggersoftware.html language=enus -->
## TOPIC 02554: DAQTriggerSoftware()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggersoftware-daqtriggersoftware.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggersoftware-daqtriggersoftware.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQTriggerSoftware class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQTriggerSoftware()

### DAQTriggerSoftware()

Initializes a new instance of the [DAQTriggerSoftware](nationalinstruments-veristand-systemdefinitionapi-daqtriggersoftware.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQTriggerSoftware()

Parent topic:

DAQTriggerSoftware Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtriggersoftware.html language=enus -->
## TOPIC 02555: DAQTriggerSoftware Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtriggersoftware.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtriggersoftware.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a software trigger that can configure a DAQTaskAI to start acquiring under certain conditions. Derives fromDAQTriggerSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQTriggerSoftware : DAQTriggerRemarksUse the members of this class to create and configure a

### DAQTriggerSoftware Class

Represents a software trigger that can configure a [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html) to start acquiring under certain conditions.

#### Derives from

- DAQTrigger

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQTriggerSoftware : DAQTrigger

#### Remarks

Use the members of this class to create and configure a software trigger you can set as the [StartTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtriggers-starttrigger.html) for the [DAQTriggers](nationalinstruments-veristand-systemdefinitionapi-daqtriggers.html) section of a [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html).

A software trigger starts acquisitions when the Start Trigger [DAQTaskCommand](nationalinstruments-veristand-systemdefinitionapi-daqtaskcommand.html) channel is true. Access the Start Trigger channel with the [GetStartTriggerChannel](nationalinstruments-veristand-systemdefinitionapi-daqtriggers-getstarttriggerchannel.html) method.

**Accessing this Class**

- DAQTriggerSoftware Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| DAQTriggerSoftware() | Initializes a new instance of the DAQTriggerSoftware class. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveform-getbooleanproperty__string-out.html language=enus -->
## TOPIC 02556: GetBooleanProperty(string, out bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveform-getbooleanproperty__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveform-getbooleanproperty__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get value of a property of type Boolean specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetBooleanProperty(string propertyName, out bool value)ParametersNameTypeDescri

### GetBooleanProperty(string, out bool)

Get value of a property of type Boolean specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetBooleanProperty(string propertyName, out bool value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | out bool | Value of property |

Parent topic:

DAQWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveform-getdoubleproperty__string-out.html language=enus -->
## TOPIC 02557: GetDoubleProperty(string, out double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveform-getdoubleproperty__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveform-getdoubleproperty__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get value of a property of type double specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetDoubleProperty(string propertyName, out double value)ParametersNameTypeDescri

### GetDoubleProperty(string, out double)

Get value of a property of type double specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetDoubleProperty(string propertyName, out double value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | out double | Value of property |

Parent topic:

DAQWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveform-getenumproperty__string-out-out.html language=enus -->
## TOPIC 02558: GetEnumProperty(string, out string, out int)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveform-getenumproperty__string-out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveform-getenumproperty__string-out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get value of a property of type enum specified by propertyName. This gets the enum value as a string as well as the underlying integer value. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetE

### GetEnumProperty(string, out string, out int)

Get value of a property of type enum specified by propertyName. This gets the enum value as a string as well as the underlying integer value. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetEnumProperty(string propertyName, out string enumString, out int enumValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| enumString | out string | String value of the enum |
| enumValue | out int | Integer value of the enum |

Parent topic:

DAQWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveform-geti16property__string-out.html language=enus -->
## TOPIC 02559: GetI16Property(string, out short)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveform-geti16property__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveform-geti16property__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get value of a property of type I16 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetI16Property(string propertyName, out short value)ParametersNameTypeDescriptionpr

### GetI16Property(string, out short)

Get value of a property of type I16 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetI16Property(string propertyName, out short value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | out short | Value of property |

Parent topic:

DAQWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveform-geti32property__string-out.html language=enus -->
## TOPIC 02560: GetI32Property(string, out int)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveform-geti32property__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveform-geti32property__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get value of a property of type I32 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetI32Property(string propertyName, out int value)ParametersNameTypeDescriptionprop

### GetI32Property(string, out int)

Get value of a property of type I32 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetI32Property(string propertyName, out int value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | out int | Value of property |

Parent topic:

DAQWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveform-geti64property__string-out.html language=enus -->
## TOPIC 02561: GetI64Property(string, out long)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveform-geti64property__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveform-geti64property__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get value of a property of type I64 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetI64Property(string propertyName, out long value)ParametersNameTypeDescriptionpro

### GetI64Property(string, out long)

Get value of a property of type I64 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetI64Property(string propertyName, out long value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | out long | Value of property |

Parent topic:

DAQWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveform-getproperties__out-out.html language=enus -->
## TOPIC 02562: GetProperties(out string[], out ValueDataType[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveform-getproperties__out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveform-getproperties__out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of all properties specified by the DAQ plugin for the channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetProperties(out string[] propertyNames, out ValueDataType[] propertyTypes)ParametersNameTypeDescriptionpropertyNamesout string[]The names of t

### GetProperties(out string[], out ValueDataType[])

Returns a list of all properties specified by the DAQ plugin for the channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetProperties(out string[] propertyNames, out ValueDataType[] propertyTypes)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyNames | out string[] | The names of the properties. |
| propertyTypes | out ValueDataType[] | An enum defining the data type of the property. |

Parent topic:

DAQWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveform-getstringproperty__string-out.html language=enus -->
## TOPIC 02563: GetStringProperty(string, out string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveform-getstringproperty__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveform-getstringproperty__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get value of a property of type string specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetStringProperty(string propertyName, out string value)ParametersNameTypeDescri

### GetStringProperty(string, out string)

Get value of a property of type string specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetStringProperty(string propertyName, out string value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | out string | Value of property |

Parent topic:

DAQWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveform-getu16property__string-out.html language=enus -->
## TOPIC 02564: GetU16Property(string, out ushort)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveform-getu16property__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveform-getu16property__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get value of a property of type U16 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetU16Property(string propertyName, out ushort value)ParametersNameTypeDescriptionp

### GetU16Property(string, out ushort)

Get value of a property of type U16 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetU16Property(string propertyName, out ushort value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | out ushort | Value of property |

Parent topic:

DAQWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveform-getu32property__string-out.html language=enus -->
## TOPIC 02565: GetU32Property(string, out uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveform-getu32property__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveform-getu32property__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get value of a property of type U32 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetU32Property(string propertyName, out uint value)ParametersNameTypeDescriptionpro

### GetU32Property(string, out uint)

Get value of a property of type U32 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetU32Property(string propertyName, out uint value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | out uint | Value of property |

Parent topic:

DAQWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveform-getu64property__string-out.html language=enus -->
## TOPIC 02566: GetU64Property(string, out ulong)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveform-getu64property__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveform-getu64property__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get value of a property of type U64 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetU64Property(string propertyName, out ulong value)ParametersNameTypeDescriptionpr

### GetU64Property(string, out ulong)

Get value of a property of type U64 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetU64Property(string propertyName, out ulong value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | out ulong | Value of property |

Parent topic:

DAQWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveform-measurementtype.html language=enus -->
## TOPIC 02567: MeasurementType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveform-measurementtype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveform-measurementtype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the enum specifying DAQ Measurement Type. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQMeasurementType MeasurementType { get; }

### MeasurementType

Gets the enum specifying DAQ Measurement Type.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQMeasurementType](nationalinstruments-veristand-systemdefinitionapi-daqmeasurementtype.html) MeasurementType { get; }

Parent topic:

DAQWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveform-pluginguid.html language=enus -->
## TOPIC 02568: PluginGUID

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveform-pluginguid.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveform-pluginguid.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the GUID specifying DAQPlugin XML/Measurement Type. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string PluginGUID { get; set; }

### PluginGUID

Gets the GUID specifying DAQPlugin XML/Measurement Type.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string PluginGUID { get; set; }

Parent topic:

DAQWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveform-resetpropertyvalues.html language=enus -->
## TOPIC 02569: ResetPropertyValues()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveform-resetpropertyvalues.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveform-resetpropertyvalues.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reset all properties specified in the DAQ Plugin XML to their defaults. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void ResetPropertyValues()

### ResetPropertyValues()

Reset all properties specified in the DAQ Plugin XML to their defaults.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void ResetPropertyValues()

Parent topic:

DAQWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveform-setbooleanproperty__string-bool.html language=enus -->
## TOPIC 02570: SetBooleanProperty(string, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveform-setbooleanproperty__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveform-setbooleanproperty__string-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set value of a property of type Boolean specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetBooleanProperty(string propertyName, bool value)ParametersNameTypeDescriptio

### SetBooleanProperty(string, bool)

Set value of a property of type Boolean specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetBooleanProperty(string propertyName, bool value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | bool | Value of property |

Parent topic:

DAQWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveform-setdoubleproperty__string-double.html language=enus -->
## TOPIC 02571: SetDoubleProperty(string, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveform-setdoubleproperty__string-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveform-setdoubleproperty__string-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set value of a property of type double specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetDoubleProperty(string propertyName, double value)ParametersNameTypeDescriptio

### SetDoubleProperty(string, double)

Set value of a property of type double specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetDoubleProperty(string propertyName, double value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | double | Value of property |

Parent topic:

DAQWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveform-setenumproperty__string-int.html language=enus -->
## TOPIC 02572: SetEnumProperty(string, int)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveform-setenumproperty__string-int.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveform-setenumproperty__string-int.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set value of a property of type enum specified by propertyName. Enum is specified by integer value. Throws exception if property of this type does not exist in the Plugin XML, or if value is an invalid enumeration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetEnum

### SetEnumProperty(string, int)

Set value of a property of type enum specified by propertyName. Enum is specified by integer value. Throws exception if property of this type does not exist in the Plugin XML, or if value is an invalid enumeration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetEnumProperty(string propertyName, int value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | int | Integer value of enum |

Parent topic:

DAQWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveform-setenumproperty__string-string.html language=enus -->
## TOPIC 02573: SetEnumProperty(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveform-setenumproperty__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveform-setenumproperty__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set value of a property of type enum specified by propertyName. Enum is specified by a string. Throws exception if property of this type does not exist in the Plugin XML, or if enumString is an invalid enumeration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetEnum

### SetEnumProperty(string, string)

Set value of a property of type enum specified by propertyName. Enum is specified by a string. Throws exception if property of this type does not exist in the Plugin XML, or if enumString is an invalid enumeration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetEnumProperty(string propertyName, string enumString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| enumString | string | Value of enum as a string |

Parent topic:

DAQWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveform-seti16property__string-short.html language=enus -->
## TOPIC 02574: SetI16Property(string, short)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveform-seti16property__string-short.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveform-seti16property__string-short.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set value of a property of type I16 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetI16Property(string propertyName, short value)ParametersNameTypeDescriptionproper

### SetI16Property(string, short)

Set value of a property of type I16 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetI16Property(string propertyName, short value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | short | Value of property |

Parent topic:

DAQWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveform-seti32property__string-int.html language=enus -->
## TOPIC 02575: SetI32Property(string, int)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveform-seti32property__string-int.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveform-seti32property__string-int.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set value of a property of type I32 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetI32Property(string propertyName, int value)ParametersNameTypeDescriptionproperty

### SetI32Property(string, int)

Set value of a property of type I32 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetI32Property(string propertyName, int value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | int | Value of property |

Parent topic:

DAQWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveform-seti64property__string-long.html language=enus -->
## TOPIC 02576: SetI64Property(string, long)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveform-seti64property__string-long.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveform-seti64property__string-long.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set value of a property of type I64 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetI64Property(string propertyName, long value)ParametersNameTypeDescriptionpropert

### SetI64Property(string, long)

Set value of a property of type I64 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetI64Property(string propertyName, long value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | long | Value of property |

Parent topic:

DAQWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveform-setstringproperty__string-string.html language=enus -->
## TOPIC 02577: SetStringProperty(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveform-setstringproperty__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveform-setstringproperty__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set value of a property of type string specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetStringProperty(string propertyName, string value)ParametersNameTypeDescriptio

### SetStringProperty(string, string)

Set value of a property of type string specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetStringProperty(string propertyName, string value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | string | Value of property |

Parent topic:

DAQWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveform-setu16property__string-ushort.html language=enus -->
## TOPIC 02578: SetU16Property(string, ushort)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveform-setu16property__string-ushort.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveform-setu16property__string-ushort.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set value of a property of type U16 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetU16Property(string propertyName, ushort value)ParametersNameTypeDescriptionprope

### SetU16Property(string, ushort)

Set value of a property of type U16 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetU16Property(string propertyName, ushort value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | ushort | Value of property |

Parent topic:

DAQWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveform-setu32property__string-uint.html language=enus -->
## TOPIC 02579: SetU32Property(string, uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveform-setu32property__string-uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveform-setu32property__string-uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set value of a property of type U32 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetU32Property(string propertyName, uint value)ParametersNameTypeDescriptionpropert

### SetU32Property(string, uint)

Set value of a property of type U32 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetU32Property(string propertyName, uint value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | uint | Value of property |

Parent topic:

DAQWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveform-setu64property__string-ulong.html language=enus -->
## TOPIC 02580: SetU64Property(string, ulong)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveform-setu64property__string-ulong.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveform-setu64property__string-ulong.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set value of a property of type U64 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetU64Property(string propertyName, ulong value)ParametersNameTypeDescriptionproper

### SetU64Property(string, ulong)

Set value of a property of type U64 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetU64Property(string propertyName, ulong value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | ulong | Value of property |

Parent topic:

DAQWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveform.html language=enus -->
## TOPIC 02581: DAQWaveform Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveform.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveform.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a generic DAQ waveform. Derives fromWaveformSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQWaveform : WaveformRemarksAbstract class implementing constructors and methods for creating /modifying DAQ channels based on DAQ Plugin XMLs PropertiesNameDescript

### DAQWaveform Class

Represents a generic DAQ waveform.

#### Derives from

- Waveform

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQWaveform : Waveform

#### Remarks

Abstract class implementing constructors and methods for creating /modifying DAQ channels based on DAQ Plugin XMLs

#### Properties

| Name | Description |
| --- | --- |
| MeasurementType | Gets the enum specifying DAQ Measurement Type. |
| PluginGUID | Gets the GUID specifying DAQPlugin XML/Measurement Type. |

#### Methods

| Name | Description |
| --- | --- |
| GetBooleanProperty(string, out bool) | Get value of a property of type Boolean specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| GetDoubleProperty(string, out double) | Get value of a property of type double specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| GetEnumProperty(string, out string, out int) | Get value of a property of type enum specified by propertyName. This gets the enum value as a string as well as the underlying integer value. Throws exception if property of this type does not exist in the Plugin XML. |
| GetI16Property(string, out short) | Get value of a property of type I16 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| GetI32Property(string, out int) | Get value of a property of type I32 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| GetI64Property(string, out long) | Get value of a property of type I64 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| GetProperties(out string[], out ValueDataType[]) | Returns a list of all properties specified by the DAQ plugin for the channel. |
| GetStringProperty(string, out string) | Get value of a property of type string specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| GetU16Property(string, out ushort) | Get value of a property of type U16 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| GetU32Property(string, out uint) | Get value of a property of type U32 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| GetU64Property(string, out ulong) | Get value of a property of type U64 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| ResetPropertyValues() | Reset all properties specified in the DAQ Plugin XML to their defaults. |
| SetBooleanProperty(string, bool) | Set value of a property of type Boolean specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| SetDoubleProperty(string, double) | Set value of a property of type double specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| SetEnumProperty(string, int) | Set value of a property of type enum specified by propertyName. Enum is specified by integer value. Throws exception if property of this type does not exist in the Plugin XML, or if value is an invalid enumeration. |
| SetEnumProperty(string, string) | Set value of a property of type enum specified by propertyName. Enum is specified by a string. Throws exception if property of this type does not exist in the Plugin XML, or if enumString is an invalid enumeration. |
| SetI16Property(string, short) | Set value of a property of type I16 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| SetI32Property(string, int) | Set value of a property of type I32 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| SetI64Property(string, long) | Set value of a property of type I64 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| SetStringProperty(string, string) | Set value of a property of type string specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| SetU16Property(string, ushort) | Set value of a property of type U16 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| SetU32Property(string, uint) | Set value of a property of type U32 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| SetU64Property(string, ulong) | Set value of a property of type U64 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveformanaloginput-channel.html language=enus -->
## TOPIC 02582: Channel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveformanaloginput-channel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveformanaloginput-channel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the channel number. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint Channel { get; set; }

### Channel

Gets or sets the channel number.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint Channel { get; set; }

Parent topic:

DAQWaveformAnalogInput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveformanaloginput-daqwaveformanaloginput__string-uint-daqmeasurementtype.html language=enus -->
## TOPIC 02583: DAQWaveformAnalogInput(string, uint, DAQMeasurementType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveformanaloginput-daqwaveformanaloginput__string-uint-daqmeasurementtype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveformanaloginput-daqwaveformanaloginput__string-uint-daqmeasurementtype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQWaveformAnalogInput class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQWaveformAnalogInput(string name, uint channel, DAQMeasurementType measurementType)ParametersNameTypeDescriptionnamestringName of AI ChannelchanneluintChannel Nu

### DAQWaveformAnalogInput(string, uint, DAQMeasurementType)

Initializes a new instance of the DAQWaveformAnalogInput class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQWaveformAnalogInput(string name, uint channel, DAQMeasurementType measurementType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | Name of AI Channel |
| channel | uint | Channel Number of Analog Input |
| measurementType | DAQMeasurementType | DAQ Measurement Type |

Parent topic:

DAQWaveformAnalogInput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveformanaloginput-daqwaveformanaloginput__string-uint-string.html language=enus -->
## TOPIC 02584: DAQWaveformAnalogInput(string, uint, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveformanaloginput-daqwaveformanaloginput__string-uint-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveformanaloginput-daqwaveformanaloginput__string-uint-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQWaveformAnalogInput class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQWaveformAnalogInput(string name, uint channel, string pluginGUID)ParametersNameTypeDescriptionnamestringName of AI ChannelchanneluintChannel Number of Analog In

### DAQWaveformAnalogInput(string, uint, string)

Initializes a new instance of the DAQWaveformAnalogInput class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQWaveformAnalogInput(string name, uint channel, string pluginGUID)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | Name of AI Channel |
| channel | uint | Channel Number of Analog Input |
| pluginGUID | string | GUID specifying DAQ Measurement Type Plugin |

Parent topic:

DAQWaveformAnalogInput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveformanaloginput-highlevel.html language=enus -->
## TOPIC 02585: HighLevel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveformanaloginput-highlevel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveformanaloginput-highlevel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the maximum value of the channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double HighLevel { get; set; }

### HighLevel

Gets or sets the maximum value of the channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double HighLevel { get; set; }

Parent topic:

DAQWaveformAnalogInput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveformanaloginput-lowlevel.html language=enus -->
## TOPIC 02586: LowLevel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveformanaloginput-lowlevel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveformanaloginput-lowlevel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the minimum value of the channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double LowLevel { get; set; }

### LowLevel

Gets or sets the minimum value of the channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double LowLevel { get; set; }

Parent topic:

DAQWaveformAnalogInput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqwaveformanaloginput.html language=enus -->
## TOPIC 02587: DAQWaveformAnalogInput Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqwaveformanaloginput.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqwaveformanaloginput.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a DAQ analog input waveform used in a buffered acquisition. Derives fromDAQWaveformSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQWaveformAnalogInput : DAQWaveformConstructorsNameDescriptionDAQWaveformAnalogInput(string, uint, DAQMeasurementType)Initiali

### DAQWaveformAnalogInput Class

Represents a DAQ analog input waveform used in a buffered acquisition.

#### Derives from

- DAQWaveform

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQWaveformAnalogInput : DAQWaveform

#### Constructors

| Name | Description |
| --- | --- |
| DAQWaveformAnalogInput(string, uint, DAQMeasurementType) | Initializes a new instance of the DAQWaveformAnalogInput class. |
| DAQWaveformAnalogInput(string, uint, string) | Initializes a new instance of the DAQWaveformAnalogInput class. |

#### Properties

| Name | Description |
| --- | --- |
| Channel | Gets or sets the channel number. |
| HighLevel | Gets or sets the maximum value of the channel. |
| LowLevel | Gets or sets the minimum value of the channel. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-database-database__string-string.html language=enus -->
## TOPIC 02588: Database(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-database-database__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-database-database__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the Database class for the XNET database specified by Name and MD5 . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Database(string Name, string MD5)ParametersNameTypeDescriptionNamestringThe name, or alias, of the XNET database to access.MD5st

### Database(string, string)

Initializes a new instance of the Database class for the XNET database specified by *Name*  and *MD5* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Database(string Name, string MD5)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name, or alias, of the XNET database to access. |
| MD5 | string | The MD5 message-digest of the XNET database. You can obtain this value from the MD5Checksum File VI. |

Parent topic:

Database Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-database-database__string.html language=enus -->
## TOPIC 02589: Database(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-database-database__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-database-database__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the Database class for the XNET database specified by Name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Database(string Name)ParametersNameTypeDescriptionNamestringThe name, or alias, of the XNET database to access.

### Database(string)

Initializes a new instance of the Database class for the XNET database specified by *Name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Database(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name, or alias, of the XNET database to access. |

Parent topic:

Database Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-database-md5.html language=enus -->
## TOPIC 02590: MD5

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-database-md5.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-database-md5.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the MD5 message-digest for the database as a byte array. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic byte[] MD5 { get; }ReturnsA byte array containing the message-digest.

### MD5

Gets the MD5 message-digest for the database as a byte array.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public byte[] MD5 { get; }

#### Returns

A byte array containing the message-digest.

Parent topic:

Database Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-database.html language=enus -->
## TOPIC 02591: Database Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-database.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-database.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an XNET database. XNET databases can be CANdb (.dbc), NI-CAN (.ncd), LDF (.ldf), or FIBEX (.xml) files. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Database : SectionRemarksUse the members or this class to access an XNET database and r

### Database Class

Represents an XNET database. XNET databases can be CANdb (.dbc), NI-CAN (.ncd), LDF (.ldf), or FIBEX (.xml) files.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Database : Section

#### Remarks

Use the members or this class to access an XNET database and read the MDF message-digest for the database.

**Accessing this Class**

- [GetDatabaseList](nationalinstruments-veristand-systemdefinitionapi-xnetdatabases-getdatabaselist.html)
- Database Constructor

For example code and more information about this class, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a System Definition File

C# Walkthrough: Modifying a System Definition File

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Database(string) | Initializes a new instance of the Database class for the XNET database specified by Name . |
| Database(string, string) | Initializes a new instance of the Database class for the XNET database specified by Name and MD5 . |

#### Properties

| Name | Description |
| --- | --- |
| MD5 | Gets the MD5 message-digest for the database as a byte array. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datafileerror.html language=enus -->
## TOPIC 02592: DataFileError Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datafileerror.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datafileerror.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Error channel associated with a raw frame data logging file or data replay file under an NI-XNET port. Derives fromChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DataFileError : ChannelRemarksUse the members of this class to get and set informati

### DataFileError Class

Represents the **Error** channel associated with a raw frame data logging file or data replay file under an NI-XNET port.

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DataFileError : Channel

#### Remarks

Use the members of this class to get and set information about the channel.

**Accessing this Class**

- [GetDataFileError](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-getdatafileerror.html)
- [GetDataFileError](nationalinstruments-veristand-systemdefinitionapi-datafilereplay-getdatafileerror.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datafilereplay-behavior.html language=enus -->
## TOPIC 02593: Behavior

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datafilereplay-behavior.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datafilereplay-behavior.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether and how frames in the data replay file are filtered. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ReplayBehavior Behavior { get; set; }ReturnsAn enumeration value of ReplayBehavior.

### Behavior

Gets or sets whether and how frames in the data replay file are filtered.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ReplayBehavior](nationalinstruments-veristand-systemdefinitionapi-replaybehavior.html) Behavior { get; set; }

#### Returns

An enumeration value of [ReplayBehavior](nationalinstruments-veristand-systemdefinitionapi-replaybehavior.html).

Parent topic:

DataFileReplay Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datafilereplay-datafilereplay__string-string-string-string.html language=enus -->
## TOPIC 02594: DataFileReplay(string, string, string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datafilereplay-datafilereplay__string-string-string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datafilereplay-datafilereplay__string-string-string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DataFileReplay class for a TDMS file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DataFileReplay(string Name, string Path, string TDMSGroupName, string TDMSChannelName)ParametersNameTypeDescriptionNamestringThe name of the data replay fi

### DataFileReplay(string, string, string, string)

Initializes a new instance of the [DataFileReplay](nationalinstruments-veristand-systemdefinitionapi-datafilereplay.html) class for a TDMS file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DataFileReplay(string Name, string Path, string TDMSGroupName, string TDMSChannelName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the data replay file to access. |
| Path | string | The path to the data replay file on disk. |
| TDMSChannelName | string | The name of the channel in the TDMS file that contains the logged data. |
| TDMSGroupName | string | The name of the group in the TDMS file that contains the logged data. |

Parent topic:

DataFileReplay Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datafilereplay-datafilereplay__string-string.html language=enus -->
## TOPIC 02595: DataFileReplay(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datafilereplay-datafilereplay__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datafilereplay-datafilereplay__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DataFileReplay class for an XNET data log (.ncl) files. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DataFileReplay(string Name, string Path)ParametersNameTypeDescriptionNamestringThe name of the data replay file to access.PathstringThe p

### DataFileReplay(string, string)

Initializes a new instance of the [DataFileReplay](nationalinstruments-veristand-systemdefinitionapi-datafilereplay.html) class for an XNET data log (.ncl) files.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DataFileReplay(string Name, string Path)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the data replay file to access. |
| Path | string | The path to the data replay file on disk. |

Parent topic:

DataFileReplay Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datafilereplay-framecachesize.html language=enus -->
## TOPIC 02596: FrameCacheSize

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datafilereplay-framecachesize.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datafilereplay-framecachesize.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the number of frames cached during replay. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint FrameCacheSize { get; set; }ReturnsThe number of cached frames, as an unsigned 32-bit integer.

### FrameCacheSize

Gets or sets the number of frames cached during replay.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint FrameCacheSize { get; set; }

#### Returns

The number of cached frames, as an unsigned 32-bit integer.

Parent topic:

DataFileReplay Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datafilereplay-frameids.html language=enus -->
## TOPIC 02597: FrameIDs

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datafilereplay-frameids.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datafilereplay-frameids.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the IDs of the frames in the log file that are included or excluded from the file replay when Behavior is ExcludeFrameIDs or IncludeFrameIDs. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string[] FrameIDs { get; set; }ReturnsThe frame IDs, as an array of stri

### FrameIDs

Gets or sets the IDs of the frames in the log file that are included or excluded from the file replay when [Behavior](nationalinstruments-veristand-systemdefinitionapi-datafilereplay-behavior.html) is [ExcludeFrameIDs](nationalinstruments-veristand-systemdefinitionapi-replaybehavior.html) or [IncludeFrameIDs](nationalinstruments-veristand-systemdefinitionapi-replaybehavior.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string[] FrameIDs { get; set; }

#### Returns

The frame IDs, as an array of strings.

Parent topic:

DataFileReplay Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datafilereplay-getdatafileerror.html language=enus -->
## TOPIC 02598: GetDataFileError()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datafilereplay-getdatafileerror.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datafilereplay-getdatafileerror.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DataFileError channel associated with the data replay file. The error channel stores the most recent error that occurred during replay. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DataFileError GetDataFileError()ReturnsA reference to the DataFileError channel.

### GetDataFileError()

Gets the [DataFileError](nationalinstruments-veristand-systemdefinitionapi-datafileerror.html) channel associated with the data replay file. The error channel stores the most recent error that occurred during replay.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DataFileError](nationalinstruments-veristand-systemdefinitionapi-datafileerror.html) GetDataFileError()

#### Returns

A reference to the [DataFileError](nationalinstruments-veristand-systemdefinitionapi-datafileerror.html) channel.

Parent topic:

DataFileReplay Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datafilereplay-getdatafilestatus.html language=enus -->
## TOPIC 02599: GetDataFileStatus()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datafilereplay-getdatafilestatus.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datafilereplay-getdatafilestatus.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DataFileStatus channel associated with the data replay file. The status channel stores the current status of the data replay process. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DataFileStatus GetDataFileStatus()ReturnsA reference to the DataFileStatus channel.

### GetDataFileStatus()

Gets the [DataFileStatus](nationalinstruments-veristand-systemdefinitionapi-datafilestatus.html) channel associated with the data replay file. The status channel stores the current status of the data replay process.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DataFileStatus](nationalinstruments-veristand-systemdefinitionapi-datafilestatus.html) GetDataFileStatus()

#### Returns

A reference to the [DataFileStatus](nationalinstruments-veristand-systemdefinitionapi-datafilestatus.html) channel.

Parent topic:

DataFileReplay Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datafilereplay-looprate.html language=enus -->
## TOPIC 02600: LoopRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datafilereplay-looprate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datafilereplay-looprate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the rate in hertz at which the frames to send in the outgoing queue are updated. This property does not affect the actual update rate of frames on the CAN bus. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int LoopRate { get; set; }ReturnsA signed 32-bit integ

### LoopRate

Gets or sets the rate in hertz at which the frames to send in the outgoing queue are updated. This property does not affect the actual update rate of frames on the CAN bus.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int LoopRate { get; set; }

#### Returns

A signed 32-bit integer representing the loop rate in hertz.

Parent topic:

DataFileReplay Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datafilereplay-path.html language=enus -->
## TOPIC 02601: Path

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datafilereplay-path.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datafilereplay-path.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the path to the replay file on disk. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DependentFile Path { get; set; }ReturnsA DependentFile reference to the replay file.

### Path

Gets or sets the path to the replay file on disk.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html) Path { get; set; }

#### Returns

A [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html) reference to the replay file.

Parent topic:

DataFileReplay Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datafilereplay-tdmschannelname.html language=enus -->
## TOPIC 02602: TDMSChannelName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datafilereplay-tdmschannelname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datafilereplay-tdmschannelname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the channel in a TDMS file that contains the logged data for replay. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string TDMSChannelName { get; set; }ReturnsThe name of the channel.

### TDMSChannelName

Gets or sets the name of the channel in a TDMS file that contains the logged data for replay.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string TDMSChannelName { get; set; }

#### Returns

The name of the channel.

Parent topic:

DataFileReplay Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datafilereplay-tdmsgroupname.html language=enus -->
## TOPIC 02603: TDMSGroupName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datafilereplay-tdmsgroupname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datafilereplay-tdmsgroupname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the group in a TDMS file that contains the logged data for replay. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string TDMSGroupName { get; set; }ReturnsThe name of the group.

### TDMSGroupName

Gets or sets the name of the group in a TDMS file that contains the logged data for replay.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string TDMSGroupName { get; set; }

#### Returns

The name of the group.

Parent topic:

DataFileReplay Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datafilereplay-triggerchannel.html language=enus -->
## TOPIC 02604: TriggerChannel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datafilereplay-triggerchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datafilereplay-triggerchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the channel used to trigger replay. Replay begins as soon as the value of this channel becomes non-zero. If desired, you can select or configure a channel that triggers multiple replays of the file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode Trigge

### TriggerChannel

Gets or sets the channel used to trigger replay. Replay begins as soon as the value of this channel becomes non-zero. If desired, you can select or configure a channel that triggers multiple replays of the file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) TriggerChannel { get; set; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the trigger channel.

Parent topic:

DataFileReplay Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datafilereplay.html language=enus -->
## TOPIC 02605: DataFileReplay Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datafilereplay.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datafilereplay.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a data replay file, which is a raw frame data logging (TDMS or NCL) file that you replay onto a CAN bus. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DataFileReplay : SectionRemarksUse the members of this class to configure how NI VeriS

### DataFileReplay Class

Represents a data replay file, which is a raw frame data logging (TDMS or NCL) file that you replay onto a CAN bus.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DataFileReplay : Section

#### Remarks

Use the members of this class to configure how NI VeriStand transmits data from a TDMS (.tdms) or XNET data log (.ncl) file onto a CAN bus. You can configure triggers for file replay, set the size of the frame cache, and set the loop rate for updating the frames in the outgoing queue.

Note

You can only add data replay files to NI-XNET CAN interfaces. LIN and FlexRay do not support data replay.

Note

NI VeriStand only can replay TDMS files that contain specific header information. To ensure your files contain the correct information, use NI VeriStand to create any TDMS files you want to replay in NI VeriStand.

**Accessing this Class**

- [GetDataFileReplayList](nationalinstruments-veristand-systemdefinitionapi-datareplay-getdatafilereplaylist.html)
- DataFileReplay Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| DataFileReplay(string, string) | Initializes a new instance of the DataFileReplay class for an XNET data log (.ncl) files. |
| DataFileReplay(string, string, string, string) | Initializes a new instance of the DataFileReplay class for a TDMS file. |

#### Properties

| Name | Description |
| --- | --- |
| Behavior | Gets or sets whether and how frames in the data replay file are filtered. |
| FrameCacheSize | Gets or sets the number of frames cached during replay. |
| FrameIDs | Gets or sets the IDs of the frames in the log file that are included or excluded from the file replay when Behavior is ExcludeFrameIDs or IncludeFrameIDs. |
| LoopRate | Gets or sets the rate in hertz at which the frames to send in the outgoing queue are updated. This property does not affect the actual update rate of frames on the CAN bus. |
| Path | Gets or sets the path to the replay file on disk. |
| TDMSChannelName | Gets or sets the name of the channel in a TDMS file that contains the logged data for replay. |
| TDMSGroupName | Gets or sets the name of the group in a TDMS file that contains the logged data for replay. |
| TriggerChannel | Gets or sets the channel used to trigger replay. Replay begins as soon as the value of this channel becomes non-zero. If desired, you can select or configure a channel that triggers multiple replays of the file. |

#### Methods

| Name | Description |
| --- | --- |
| GetDataFileError() | Gets the DataFileError channel associated with the data replay file. The error channel stores the most recent error that occurred during replay. |
| GetDataFileStatus() | Gets the DataFileStatus channel associated with the data replay file. The status channel stores the current status of the data replay process. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datafilestatus.html language=enus -->
## TOPIC 02606: DataFileStatus Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datafilestatus.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datafilestatus.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Status channel associated with a raw frame data logging file or data replay file under an NI-XNET port. Derives fromChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DataFileStatus : ChannelRemarksUse the members of this class to get and set informa

### DataFileStatus Class

Represents the **Status** channel associated with a raw frame data logging file or data replay file under an NI-XNET port.

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DataFileStatus : Channel

#### Remarks

Use the members of this class to get and set information about the channel.

**Accessing this Class**

- [GetDataFileStatus](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-getdatafilestatus.html)
- [GetDataFileStatus](nationalinstruments-veristand-systemdefinitionapi-datafilereplay-getdatafilestatus.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-buffertime.html language=enus -->
## TOPIC 02607: BufferTime

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-buffertime.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-buffertime.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the buffer time of the log file in seconds. Frames read will be added to the buffer until the specified amount of time has elapsed, at which point all buffered data will be written to the file. If the buffer is partially full when a file is finished, the remaining data in the buffer wil

### BufferTime

Gets or sets the buffer time of the log file in seconds. Frames read will be added to the buffer until the specified amount of time has elapsed, at which point all buffered data will be written to the file. If the buffer is partially full when a file is finished, the remaining data in the buffer will be written to the file. If the buffer time is set to 0, data will be immediately written to the file when read.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double BufferTime { get; set; }

#### Returns

A double representing the buffer time in seconds.

Parent topic:

DataLoggingFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-dataloggingfile__string-string-string.html language=enus -->
## TOPIC 02608: DataLoggingFile(string, string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-dataloggingfile__string-string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-dataloggingfile__string-string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DataLoggingFile class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DataLoggingFile(string Name, string Filename, string Destination)ParametersNameTypeDescriptionNamestringThe name of the data logging file, as it appears in the system def

### DataLoggingFile(string, string, string)

Initializes a new instance of the [DataLoggingFile](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DataLoggingFile(string Name, string Filename, string Destination)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the data logging file, as it appears in the system definition. |
| Filename | string | The filename of the data logging file. |
| Destination | string | The destination for the data logging file on disk. |

Parent topic:

DataLoggingFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-dataloggingfiletype.html language=enus -->
## TOPIC 02609: DataLoggingFileType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-dataloggingfiletype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-dataloggingfiletype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the file type of an NI-XNET DataLoggingFile. Log files can be TDMS or NCL files. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic FileType DataLoggingFileType { get; set; }ReturnsAn enumeration value of FileType.

### DataLoggingFileType

Gets or sets the file type of an NI-XNET [DataLoggingFile](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile.html). Log files can be TDMS or NCL files.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [FileType](nationalinstruments-veristand-systemdefinitionapi-filetype.html) DataLoggingFileType { get; set; }

#### Returns

An enumeration value of [FileType](nationalinstruments-veristand-systemdefinitionapi-filetype.html).

Parent topic:

DataLoggingFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-destination.html language=enus -->
## TOPIC 02610: Destination

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-destination.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-destination.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the destination for a DataLoggingFile on disk. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Destination { get; set; }ReturnsThe path to the destination.

### Destination

Gets or sets the destination for a [DataLoggingFile](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile.html) on disk.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Destination { get; set; }

#### Returns

The path to the destination.

Parent topic:

DataLoggingFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-filename.html language=enus -->
## TOPIC 02611: Filename

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-filename.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-filename.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the filename of a DataLoggingFile. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Filename { get; set; }ReturnsThe filename.

### Filename

Gets or sets the filename of a [DataLoggingFile](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Filename { get; set; }

#### Returns

The filename.

Parent topic:

DataLoggingFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-filter.html language=enus -->
## TOPIC 02612: Filter

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-filter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-filter.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether and how to filter the logged frames. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DataLoggingFilterType Filter { get; set; }ReturnsAn enumeration value of DataLoggingFilterType.

### Filter

Gets or sets whether and how to filter the logged frames.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DataLoggingFilterType](nationalinstruments-veristand-systemdefinitionapi-dataloggingfiltertype.html) Filter { get; set; }

#### Returns

An enumeration value of [DataLoggingFilterType](nationalinstruments-veristand-systemdefinitionapi-dataloggingfiltertype.html).

Parent topic:

DataLoggingFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-frameids.html language=enus -->
## TOPIC 02613: FrameIDs

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-frameids.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-frameids.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the frame IDs in the XNET database cluster to either include in or exclude from data logging. Use this property when you configure a Filter for the data logging file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string[] FrameIDs { get; set; }ReturnsThe array

### FrameIDs

Gets or sets the frame IDs in the XNET database cluster to either include in or exclude from data logging. Use this property when you configure a [Filter](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-filter.html) for the data logging file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string[] FrameIDs { get; set; }

#### Returns

The array of frame IDs, as strings.

Parent topic:

DataLoggingFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-getdatafileerror.html language=enus -->
## TOPIC 02614: GetDataFileError()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-getdatafileerror.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-getdatafileerror.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DataFileError channel associated with the data logging file. The error channel stores the most recent error that occurred during logging. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DataFileError GetDataFileError()ReturnsA reference to the DataFileError channel.

### GetDataFileError()

Gets the [DataFileError](nationalinstruments-veristand-systemdefinitionapi-datafileerror.html) channel associated with the data logging file. The error channel stores the most recent error that occurred during logging.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DataFileError](nationalinstruments-veristand-systemdefinitionapi-datafileerror.html) GetDataFileError()

#### Returns

A reference to the [DataFileError](nationalinstruments-veristand-systemdefinitionapi-datafileerror.html) channel.

Parent topic:

DataLoggingFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-getdatafilestatus.html language=enus -->
## TOPIC 02615: GetDataFileStatus()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-getdatafilestatus.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-getdatafilestatus.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DataFileStatus channel associated with the data logging file. The status channel stores the current status of the data logging process. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DataFileStatus GetDataFileStatus()ReturnsA reference to the DataFileStatus channel

### GetDataFileStatus()

Gets the [DataFileStatus](nationalinstruments-veristand-systemdefinitionapi-datafilestatus.html) channel associated with the data logging file. The status channel stores the current status of the data logging process.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DataFileStatus](nationalinstruments-veristand-systemdefinitionapi-datafilestatus.html) GetDataFileStatus()

#### Returns

A reference to the [DataFileStatus](nationalinstruments-veristand-systemdefinitionapi-datafilestatus.html) channel.

Parent topic:

DataLoggingFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-limittype.html language=enus -->
## TOPIC 02616: LimitType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-limittype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-limittype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the criteria to use to stop logging data to the current file. When the limit you specify occurs, NI VeriStand either stops logging completely or continues logging in a new file, depending on the specified Operation. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpubli

### LimitType

Gets or sets the criteria to use to stop logging data to the current file. When the limit you specify occurs, NI VeriStand either stops logging completely or continues logging in a new file, depending on the specified [Operation](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-operation.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [FileLimitationType](nationalinstruments-veristand-systemdefinitionapi-filelimitationtype.html) LimitType { get; set; }

#### Returns

An enumeration value of [FileLimitationType](nationalinstruments-veristand-systemdefinitionapi-filelimitationtype.html).

Parent topic:

DataLoggingFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-limitvalue.html language=enus -->
## TOPIC 02617: LimitValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-limitvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-limitvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the value used to determine when to stop logging data to the current log file. This property can represent a size in kilobytes or a time in seconds, depending on the file's LimitType. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint LimitValue { get; set; }R

### LimitValue

Gets or sets the value used to determine when to stop logging data to the current log file. This property can represent a size in kilobytes or a time in seconds, depending on the file's [LimitType](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-limittype.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint LimitValue { get; set; }

#### Remarks

When the limit value is reached, NI VeriStand either stops logging completely or continues logging in a new file, depending on the specified [Operation](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-operation.html).

#### Returns

A 32-bit signed integer representing the current file's limit value.

Parent topic:

DataLoggingFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-numberofbytestoread.html language=enus -->
## TOPIC 02618: NumberOfBytesToRead

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-numberofbytestoread.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-numberofbytestoread.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the maximum number of raw bytes to read. This number does not represent the number of frames to read. CAN and LIN frames are always 24 bytes long. FlexRay frames vary in length. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint NumberOfBytesToRead { get; set;

### NumberOfBytesToRead

Gets or sets the maximum number of raw bytes to read. This number does not represent the number of frames to read. CAN and LIN frames are always 24 bytes long. FlexRay frames vary in length.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint NumberOfBytesToRead { get; set; }

#### Remarks

DataFileError

Note

The larger the number you specify, the more memory data logging requires. To avoid additional dynamic memory allocation, try to determine the bus load for your session before starting a data logging operation.

#### Returns

An unsigned 32-bit integer representing the number of bytes to read.

Parent topic:

DataLoggingFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-operation.html language=enus -->
## TOPIC 02619: Operation

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-operation.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-operation.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the action to take when a trigger condition is met. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DataLoggingOperationType Operation { get; set; }RemarksIf TriggerType is StartLoggingOnNonZero or StartLoggingOnZero, this property specifies the action to take w

### Operation

Gets or sets the action to take when a trigger condition is met.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DataLoggingOperationType](nationalinstruments-veristand-systemdefinitionapi-dataloggingoperationtype.html) Operation { get; set; }

#### Remarks

If [TriggerType](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-triggertype.html) is [StartLoggingOnNonZero](nationalinstruments-veristand-systemdefinitionapi-dataloggingtriggertype.html) or [StartLoggingOnZero](nationalinstruments-veristand-systemdefinitionapi-dataloggingtriggertype.html), this property specifies the action to take when the [LimitType](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-limittype.html) condition is met.

If [TriggerType](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-triggertype.html) is [EnableLoggingWhenTriggerIsNonZero](nationalinstruments-veristand-systemdefinitionapi-dataloggingtriggertype.html) or [EnableLoggingWhenTriggerIsZero](nationalinstruments-veristand-systemdefinitionapi-dataloggingtriggertype.html), this property specifies the action to take when the value of the [TriggerChannel](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-triggerchannel.html) stops meeting the specified [TriggerType](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-triggertype.html) condition.

#### Returns

An enumeration value of [DataLoggingOperationType](nationalinstruments-veristand-systemdefinitionapi-dataloggingoperationtype.html).

Parent topic:

DataLoggingFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-retriggerable.html language=enus -->
## TOPIC 02620: Retriggerable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-retriggerable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-retriggerable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether logging can be retriggered after a stop. If true, logging begins again when the value of TriggerChannel reaches the specified TriggerType. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool Retriggerable { get; set; }RemarksYou must set Operation to St

### Retriggerable

Gets or sets whether logging can be retriggered after a stop. If true, logging begins again when the value of [TriggerChannel](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-triggerchannel.html) reaches the specified [TriggerType](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-triggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool Retriggerable { get; set; }

#### Remarks

You must set [Operation](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-operation.html) to [StopLogging](nationalinstruments-veristand-systemdefinitionapi-dataloggingoperationtype.html) to enable this property.

#### Returns

true if logging is retriggerable.

Parent topic:

DataLoggingFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-tdmschannelname.html language=enus -->
## TOPIC 02621: TDMSChannelName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-tdmschannelname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-tdmschannelname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the channel in the TDMS file to log data to. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string TDMSChannelName { get; set; }ReturnsThe name of the channel.

### TDMSChannelName

Gets or sets the name of the channel in the TDMS file to log data to.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string TDMSChannelName { get; set; }

#### Returns

The name of the channel.

Parent topic:

DataLoggingFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-tdmsgroupname.html language=enus -->
## TOPIC 02622: TDMSGroupName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-tdmsgroupname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-tdmsgroupname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the group in the TDMS file to log data to. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string TDMSGroupName { get; set; }ReturnsThe name of the group.

### TDMSGroupName

Gets or sets the name of the group in the TDMS file to log data to.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string TDMSGroupName { get; set; }

#### Returns

The name of the group.

Parent topic:

DataLoggingFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-triggerchannel.html language=enus -->
## TOPIC 02623: TriggerChannel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-triggerchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-triggerchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The channel to watch for the specified TriggerType. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode TriggerChannel { get; set; }ReturnsThe BaseNode reference to the trigger channel.

### TriggerChannel

The channel to watch for the specified [TriggerType](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-triggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) TriggerChannel { get; set; }

#### Returns

The [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the trigger channel.

Parent topic:

DataLoggingFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-triggertype.html language=enus -->
## TOPIC 02624: TriggerType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-triggertype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-triggertype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the type of trigger to use to start or stop data logging. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DataLoggingTriggerType TriggerType { get; set; }ReturnsAn enumeration value of DataLoggingTriggerType.

### TriggerType

Gets or sets the type of trigger to use to start or stop data logging.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DataLoggingTriggerType](nationalinstruments-veristand-systemdefinitionapi-dataloggingtriggertype.html) TriggerType { get; set; }

#### Returns

An enumeration value of [DataLoggingTriggerType](nationalinstruments-veristand-systemdefinitionapi-dataloggingtriggertype.html).

Parent topic:

DataLoggingFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dataloggingfile.html language=enus -->
## TOPIC 02625: DataLoggingFile Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dataloggingfile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dataloggingfile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a raw frame data logging (TDMS or NCL) file under an NI-XNET port. You can use raw frame data logging files to record incoming frame data during an NI-XNET session. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DataLoggingFile : SectionR

### DataLoggingFile Class

Represents a raw frame data logging (TDMS or NCL) file under an NI-XNET port. You can use raw frame data logging files to record incoming frame data during an NI-XNET session.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DataLoggingFile : Section

#### Remarks

Use the members of this class to get and set properties of a log file, such as its filename, location on disk, and triggers to start and stop logging.

**Accessing this Class**

- [GetDataLoggingFileList](nationalinstruments-veristand-systemdefinitionapi-rawframedatalogging-getdataloggingfilelist.html)
- DataLoggingFile Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| DataLoggingFile(string, string, string) | Initializes a new instance of the DataLoggingFile class. |

#### Properties

| Name | Description |
| --- | --- |
| BufferTime | Gets or sets the buffer time of the log file in seconds. Frames read will be added to the buffer until the specified amount of time has elapsed, at which point all buffered data will be written to the file. If the buffer is partially full when a file is finished, the remaining data in the buffer will be written to the file. If the buffer time is set to 0, data will be immediately written to the file when read. |
| DataLoggingFileType | Gets or sets the file type of an NI-XNET DataLoggingFile. Log files can be TDMS or NCL files. |
| Destination | Gets or sets the destination for a DataLoggingFile on disk. |
| Filename | Gets or sets the filename of a DataLoggingFile. |
| Filter | Gets or sets whether and how to filter the logged frames. |
| FrameIDs | Gets or sets the frame IDs in the XNET database cluster to either include in or exclude from data logging. Use this property when you configure a Filter for the data logging file. |
| LimitType | Gets or sets the criteria to use to stop logging data to the current file. When the limit you specify occurs, NI VeriStand either stops logging completely or continues logging in a new file, depending on the specified Operation. |
| LimitValue | Gets or sets the value used to determine when to stop logging data to the current log file. This property can represent a size in kilobytes or a time in seconds, depending on the file's LimitType. |
| NumberOfBytesToRead | Gets or sets the maximum number of raw bytes to read. This number does not represent the number of frames to read. CAN and LIN frames are always 24 bytes long. FlexRay frames vary in length. |
| Operation | Gets or sets the action to take when a trigger condition is met. |
| Retriggerable | Gets or sets whether logging can be retriggered after a stop. If true, logging begins again when the value of TriggerChannel reaches the specified TriggerType. |
| TDMSChannelName | Gets or sets the name of the channel in the TDMS file to log data to. |
| TDMSGroupName | Gets or sets the name of the group in the TDMS file to log data to. |
| TriggerChannel | The channel to watch for the specified TriggerType. |
| TriggerType | Gets or sets the type of trigger to use to start or stop data logging. |

#### Methods

| Name | Description |
| --- | --- |
| GetDataFileError() | Gets the DataFileError channel associated with the data logging file. The error channel stores the most recent error that occurred during logging. |
| GetDataFileStatus() | Gets the DataFileStatus channel associated with the data logging file. The status channel stores the current status of the data logging process. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dataloggingfiltertype.html language=enus -->
## TOPIC 02626: DataLoggingFilterType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dataloggingfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dataloggingfiltertype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of filtering applied to a DataLoggingFile under an NI-XNET port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum DataLoggingFilterTypeRemarksSpecifying to exclude or include frames for logging does not affect the actual data in the XNET database file.

### DataLoggingFilterType Enumeration

Specifies the type of filtering applied to a [DataLoggingFile](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile.html) under an NI-XNET port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum DataLoggingFilterType

#### Remarks

Note

Specifying to exclude or include frames for logging does not affect the actual data in the XNET database file.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| LogEntireBusTraffic | 0 | Logs all the frames on the bus. This value indicates that no filter is applied. |
| ExcludeFrameIDs | 1 | Logs all frames except for those specified by FrameIDs. |
| IncludeFrameIDs | 2 | Logs only the frames specified by FrameIDs. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dataloggingoperationtype.html language=enus -->
## TOPIC 02627: DataLoggingOperationType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dataloggingoperationtype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dataloggingoperationtype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the action taken when a trigger condition is met. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum DataLoggingOperationTypeRemarksIf TriggerType is StartLoggingOnNonZero or StartLoggingOnZero, this is the action taken when the LimitType condition is met. If Tri

### DataLoggingOperationType Enumeration

Specifies the action taken when a trigger condition is met.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum DataLoggingOperationType

#### Remarks

If [TriggerType](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-triggertype.html) is [StartLoggingOnNonZero](nationalinstruments-veristand-systemdefinitionapi-dataloggingtriggertype.html) or [StartLoggingOnZero](nationalinstruments-veristand-systemdefinitionapi-dataloggingtriggertype.html), this is the action taken when the [LimitType](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-limittype.html) condition is met.

If [TriggerType](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-triggertype.html) is [EnableLoggingWhenTriggerIsNonZero](nationalinstruments-veristand-systemdefinitionapi-dataloggingtriggertype.html) or [EnableLoggingWhenTriggerIsZero](nationalinstruments-veristand-systemdefinitionapi-dataloggingtriggertype.html), this is the action taken when the value of the [TriggerChannel](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-triggerchannel.html) stops meeting the specified [TriggerType](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile-triggertype.html) condition.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ContinueLoggingInNewFile | 0 | Continues logging data in a new file. NI VeriStand adds an incrementing number to the file name of each new log file it creates. |
| StopLogging | 1 | Stops logging data. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dataloggingtriggertype.html language=enus -->
## TOPIC 02628: DataLoggingTriggerType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dataloggingtriggertype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dataloggingtriggertype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of trigger used to start or stop logging data to a DataLoggingFile. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum DataLoggingTriggerTypeMembersNameValueDescriptionStartLoggingOnNonZero0Starts logging when the value of TriggerChannel becomes non-zero

### DataLoggingTriggerType Enumeration

Specifies the type of trigger used to start or stop logging data to a [DataLoggingFile](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum DataLoggingTriggerType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| StartLoggingOnNonZero | 0 | Starts logging when the value of TriggerChannel becomes non-zero and continues logging until the LimitType condition is met. |
| StartLoggingOnZero | 1 | Starts logging when the value of TriggerChannel becomes zero and continues logging until the LimitType condition is met. |
| EnableLoggingWhenTriggerIsZero | 2 | Logs data whenever the value of TriggerChannel is zero. When the value of TriggerChannel becomes non-zero, logging either stops or continues in a new log file, depending on the value of Operation. |
| EnableLoggingWhenTriggerIsNonZero | 3 | Logs data whenever the value of the TriggerChannel is not zero. When the value of TriggerChannel becomes zero, logging either stops or continues in a new log file, depending on the value of Operation. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datareplay-adddatafilereplay__datafilereplay-out.html language=enus -->
## TOPIC 02629: AddDataFileReplay(DataFileReplay, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datareplay-adddatafilereplay__datafilereplay-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datareplay-adddatafilereplay__datafilereplay-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified data replay file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddDataFileReplay(DataFileReplay dataFileReplay, out Error error)ParametersNameTypeDescriptiondataFileReplayDataFileReplaySpecifies the data replay file to add.errorout ErrorReturns an

### AddDataFileReplay(DataFileReplay, out Error)

Adds the specified data replay file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddDataFileReplay(DataFileReplay dataFileReplay, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| dataFileReplay | DataFileReplay | Specifies the data replay file to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the file was added successfully.

Parent topic:

DataReplay Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datareplay-adddatafilereplay__datafilereplay.html language=enus -->
## TOPIC 02630: AddDataFileReplay(DataFileReplay)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datareplay-adddatafilereplay__datafilereplay.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datareplay-adddatafilereplay__datafilereplay.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified data replay file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddDataFileReplay(DataFileReplay dataFileReplay)ParametersNameTypeDescriptiondataFileReplayDataFileReplaySpecifies the data replay file to add.Returnstrue if the file was added successf

### AddDataFileReplay(DataFileReplay)

Adds the specified data replay file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddDataFileReplay(DataFileReplay dataFileReplay)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| dataFileReplay | DataFileReplay | Specifies the data replay file to add. |

#### Returns

true if the file was added successfully.

Parent topic:

DataReplay Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datareplay-getdatafilereplaylist.html language=enus -->
## TOPIC 02631: GetDataFileReplayList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datareplay-getdatafilereplaylist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datareplay-getdatafilereplaylist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the DataFileReplay elements, or the data replay files, from the current DataReplay section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DataFileReplay[] GetDataFileReplayList()RemarksModifications you make to the contents of this list apply to

### GetDataFileReplayList()

Gets an array that contains the [DataFileReplay](nationalinstruments-veristand-systemdefinitionapi-datafilereplay.html) elements, or the data replay files, from the current [DataReplay](nationalinstruments-veristand-systemdefinitionapi-datareplay.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DataFileReplay](nationalinstruments-veristand-systemdefinitionapi-datafilereplay.html)[] GetDataFileReplayList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [DataFileReplay](nationalinstruments-veristand-systemdefinitionapi-datafilereplay.html) elements from the current [DataReplay](nationalinstruments-veristand-systemdefinitionapi-datareplay.html) section.

Parent topic:

DataReplay Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datareplay.html language=enus -->
## TOPIC 02632: DataReplay Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datareplay.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datareplay.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Data Replay section under an NI-XNET CAN port, which contains any DataFileReplay files you want to replay onto the CAN bus. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DataReplay : SectionRemarksUse the members of this class to add

### DataReplay Class

Represents the **Data Replay** section under an NI-XNET CAN port, which contains any [DataFileReplay](nationalinstruments-veristand-systemdefinitionapi-datafilereplay.html) files you want to replay onto the CAN bus.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DataReplay : Section

#### Remarks

Note

NI VeriStand only can replay TDMS files that contain specific header information. To ensure your files contain the correct information, use NI VeriStand to create any TDMS files you want to replay in NI VeriStand.

**Accessing this Class**

- [GetDataReplay](nationalinstruments-veristand-systemdefinitionapi-outgoing-getdatareplay.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddDataFileReplay(DataFileReplay, out Error) | Adds the specified data replay file. |
| AddDataFileReplay(DataFileReplay) | Adds the specified data replay file. |
| GetDataFileReplayList() | Gets an array that contains the DataFileReplay elements, or the data replay files, from the current DataReplay section. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datasharing-addreflectivememory__string-out.html language=enus -->
## TOPIC 02633: AddReflectiveMemory(string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datasharing-addreflectivememory__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datasharing-addreflectivememory__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified reflective memory device. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddReflectiveMemory(string Name, out Error error)ParametersNameTypeDescriptionNamestringThe name of the reflective memory device.errorout ErrorReturns an NationalInstruments.Ver

### AddReflectiveMemory(string, out Error)

Adds the specified reflective memory device.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddReflectiveMemory(string Name, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the reflective memory device. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the reflective memory device was added successfully.

Parent topic:

DataSharing Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datasharing-addreflectivememory__string.html language=enus -->
## TOPIC 02634: AddReflectiveMemory(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datasharing-addreflectivememory__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datasharing-addreflectivememory__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified reflective memory device. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddReflectiveMemory(string Name)ParametersNameTypeDescriptionNamestringThe name of the reflective memory device.Returnstrue if the reflective memory device was added successfull

### AddReflectiveMemory(string)

Adds the specified reflective memory device.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddReflectiveMemory(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the reflective memory device. |

#### Returns

true if the reflective memory device was added successfully.

Parent topic:

DataSharing Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datasharing-getreflectivememory.html language=enus -->
## TOPIC 02635: GetReflectiveMemory()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datasharing-getreflectivememory.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datasharing-getreflectivememory.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the first reflective memory device. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ReflectiveMemory GetReflectiveMemory()ReturnsThe first ReflectiveMemory object.

### GetReflectiveMemory()

Gets the first reflective memory device.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ReflectiveMemory](nationalinstruments-veristand-systemdefinitionapi-reflectivememory.html) GetReflectiveMemory()

#### Returns

The first [ReflectiveMemory](nationalinstruments-veristand-systemdefinitionapi-reflectivememory.html) object.

Parent topic:

DataSharing Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datasharing.html language=enus -->
## TOPIC 02636: DataSharing Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datasharing.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datasharing.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Data Sharing section under a Chassis. This section contains any reflective memory devices you add to the system definition. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DataSharing : SectionRemarksUse the members of this class to to

### DataSharing Class

Represents the **Data Sharing** section under a [Chassis](nationalinstruments-veristand-systemdefinitionapi-chassis.html). This section contains any reflective memory devices you add to the system definition.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DataSharing : Section

#### Remarks

Use the members of this class to to add a reflective memory device or get the first reflective memory device in the system definition file.

**Accessing this Class**

- [GetDataSharing](nationalinstruments-veristand-systemdefinitionapi-chassis-getdatasharing.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddReflectiveMemory(string, out Error) | Adds the specified reflective memory device. |
| AddReflectiveMemory(string) | Adds the specified reflective memory device. |
| GetReflectiveMemory() | Gets the first reflective memory device. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datasharingnetwork-addreflectivememorynetwork__string-out.html language=enus -->
## TOPIC 02637: AddReflectiveMemoryNetwork(string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datasharingnetwork-addreflectivememorynetwork__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datasharingnetwork-addreflectivememorynetwork__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new reflective memory network to the system definition. You can only configure one reflective memory network per system definition. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddReflectiveMemoryNetwork(string Name, out Error error)ParametersNameTypeDescripti

### AddReflectiveMemoryNetwork(string, out Error)

Adds a new reflective memory network to the system definition. You can only configure one reflective memory network per system definition.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddReflectiveMemoryNetwork(string Name, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the reflective memory network. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the reflective memory network is added successfully.

Parent topic:

DataSharingNetwork Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datasharingnetwork-addreflectivememorynetwork__string.html language=enus -->
## TOPIC 02638: AddReflectiveMemoryNetwork(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datasharingnetwork-addreflectivememorynetwork__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datasharingnetwork-addreflectivememorynetwork__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new reflective memory network to the system definition. You can only configure one reflective memory network per system definition. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddReflectiveMemoryNetwork(string Name)ParametersNameTypeDescriptionNamestringThe n

### AddReflectiveMemoryNetwork(string)

Adds a new reflective memory network to the system definition. You can only configure one reflective memory network per system definition.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddReflectiveMemoryNetwork(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the reflective memory network. |

#### Returns

true if the reflective memory network is added successfully.

Parent topic:

DataSharingNetwork Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datasharingnetwork-dynamicdatasize.html language=enus -->
## TOPIC 02639: DynamicDataSize

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datasharingnetwork-dynamicdatasize.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datasharingnetwork-dynamicdatasize.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the number of channels in reflective memory to reserve for dynamically mapping channel data at run-time. For example, in a distributed system, if target A needs to access data provided by a channel on target B at run-time, the targets require a channel in reflective memory that target B

### DynamicDataSize

Gets or sets the number of channels in reflective memory to reserve for dynamically mapping channel data at run-time. For example, in a distributed system, if target A needs to access data provided by a channel on target B at run-time, the targets require a channel in reflective memory that target B can copy data to and target A can read data from.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int DynamicDataSize { get; set; }

#### Returns

The number of channels in reflective memory to reserve for dynamically mapping channel data at run-time. The default value is 30.

Parent topic:

DataSharingNetwork Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datasharingnetwork-getreflectivememorynetwork.html language=enus -->
## TOPIC 02640: GetReflectiveMemoryNetwork()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datasharingnetwork-getreflectivememorynetwork.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datasharingnetwork-getreflectivememorynetwork.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a reference to a reflective memory network that already exists under DataSharingNetwork. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ReflectiveMemoryNetwork GetReflectiveMemoryNetwork()ReturnsA reference to the ReflectiveMemoryNetwork.

### GetReflectiveMemoryNetwork()

Gets a reference to a reflective memory network that already exists under [DataSharingNetwork](nationalinstruments-veristand-systemdefinitionapi-datasharingnetwork.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ReflectiveMemoryNetwork](nationalinstruments-veristand-systemdefinitionapi-reflectivememorynetwork.html) GetReflectiveMemoryNetwork()

#### Returns

A reference to the [ReflectiveMemoryNetwork](nationalinstruments-veristand-systemdefinitionapi-reflectivememorynetwork.html).

Parent topic:

DataSharingNetwork Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-datasharingnetwork.html language=enus -->
## TOPIC 02641: DataSharingNetwork Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-datasharingnetwork.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-datasharingnetwork.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Data Sharing Network section of the system definition, under which you can add and configure a reflective memory network. You can only configure one reflective memory network per system definition. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpu

### DataSharingNetwork Class

Represents the **Data Sharing Network** section of the system definition, under which you can add and configure a reflective memory network. You can only configure one reflective memory network per system definition.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DataSharingNetwork : Section

#### Remarks

Use the members of this class to add or access a reflective memory network.

**Accessing this Class**

- [GetDataSharingNetwork](nationalinstruments-veristand-systemdefinitionapi-root-getdatasharingnetwork.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| DynamicDataSize | Gets or sets the number of channels in reflective memory to reserve for dynamically mapping channel data at run-time. For example, in a distributed system, if target A needs to access data provided by a channel on target B at run-time, the targets require a channel in reflective memory that target B can copy data to and target A can read data from. |

#### Methods

| Name | Description |
| --- | --- |
| AddReflectiveMemoryNetwork(string, out Error) | Adds a new reflective memory network to the system definition. You can only configure one reflective memory network per system definition. |
| AddReflectiveMemoryNetwork(string) | Adds a new reflective memory network to the system definition. You can only configure one reflective memory network per system definition. |
| GetReflectiveMemoryNetwork() | Gets a reference to a reflective memory network that already exists under DataSharingNetwork. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-delimiter.html language=enus -->
## TOPIC 02642: Delimiter Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-delimiter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-delimiter.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the delimiter of the ParameterFile. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum DelimiterMembersNameValueDescriptionTab0Delimiter is tab. EqualsDelimiter is equals (=). CommaDelimiter is comma (,). See AlsoNationalInstruments.VeriStand.SystemDefinitionAPI.Si

### Delimiter Enumeration

Defines the delimiter of the [ParameterFile](nationalinstruments-veristand-systemdefinitionapi-simulationmodels-parameterfile.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum Delimiter

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Tab | 0 | Delimiter is tab. |
| Equals |  | Delimiter is equals (=). |
| Comma |  | Delimiter is comma (,). |

#### See Also

- NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels.ParameterFileDelimiter

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dependentfile-dependentfile__string-dependentfiletype-string-bool-string-string-string.html language=enus -->
## TOPIC 02643: DependentFile(string, DependentFileType, string, bool, string, string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dependentfile-dependentfile__string-dependentfiletype-string-bool-string-string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dependentfile-dependentfile__string-dependentfiletype-string-bool-string-string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DependentFile class for the specified file. This instance allows you to specify the type of FilePath used to specify the location of the file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DependentFile(string FilePath, DependentFileType T

### DependentFile(string, DependentFileType, string, bool, string, string, string)

Initializes a new instance of the [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html) class for the specified file. This instance allows you to specify the type of *FilePath*  used to specify the location of the file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DependentFile(string FilePath, DependentFileType Type, string Version, bool ForceDownload, string RTDestination, string SupportedTarget, string MD5)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| FilePath | string | The path to the file on the host. |
| Type | DependentFileType | The DependentFileType used for the FilePath . |
| Version | string | An arbitrary string to store with the file. You can use this parameter to store version information with the file. |
| ForceDownload | bool | If true, specifies to force-download the file to the target when you deploy the system definition. |
| RTDestination | string | The destination path, including the filename, for the file on the target. This must be an absolute path. |
| SupportedTarget | string | the target operating system(s) to which the file is deployed. Standard values include All, PharLap, VxWorks, Windows, PharLap & Windows, PharLap & VxWorks, and VxWorks & Windows. |
| MD5 | string | The MD5 message-digest for the file. |

Parent topic:

DependentFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dependentfile-dependentfile__string-string-bool-string-string-string.html language=enus -->
## TOPIC 02644: DependentFile(string, string, bool, string, string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dependentfile-dependentfile__string-string-bool-string-string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dependentfile-dependentfile__string-string-bool-string-string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DependentFile class for the specified file. This instance requires an absolute FilePath to specify the location of the file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DependentFile(string FilePath, string Version, bool ForceDownload, s

### DependentFile(string, string, bool, string, string, string)

Initializes a new instance of the [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html) class for the specified file. This instance requires an absolute *FilePath*  to specify the location of the file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DependentFile(string FilePath, string Version, bool ForceDownload, string RTDestination, string SupportedTarget, string MD5)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| FilePath | string | The path to the file on the host. This must be an absolute path. |
| Version | string | An arbitrary string to store with the file. You can use this parameter to store version information with the file. |
| ForceDownload | bool | If true, specifies to force-download the file to the target when you deploy the system definition. |
| RTDestination | string | The destination path, including the filename, for the file on the target. This must be an absolute path. |
| SupportedTarget | string | the target operating system(s) to which the file is deployed. Standard values include All, PharLap, VxWorks, Windows, PharLap & Windows, PharLap & VxWorks, and VxWorks & Windows. |
| MD5 | string | The MD5 message-digest for the file. |

Parent topic:

DependentFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dependentfile-forcedownload.html language=enus -->
## TOPIC 02645: ForceDownload

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dependentfile-forcedownload.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dependentfile-forcedownload.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the file is set to force-download to the target. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool ForceDownload { get; set; }Returnstrue if the file is set to force-download.

### ForceDownload

Gets or sets whether the file is set to force-download to the target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool ForceDownload { get; set; }

#### Returns

true if the file is set to force-download.

Parent topic:

DependentFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dependentfile-getabsolutepath__string.html language=enus -->
## TOPIC 02646: GetAbsolutePath(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dependentfile-getabsolutepath__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dependentfile-getabsolutepath__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the absolute path to a file by prepending the specified baseAbsolutePath to a relative path to the file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string GetAbsolutePath(string baseAbsolutePath)ParametersNameTypeDescriptionbaseAbsolutePathstringThe base path to ap

### GetAbsolutePath(string)

Gets the absolute path to a file by prepending the specified *baseAbsolutePath*  to a relative path to the file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string GetAbsolutePath(string baseAbsolutePath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| baseAbsolutePath | string | The base path to append to the path to the file to form the absolute bath. |

#### Returns

The absolute path to the file.

Parent topic:

DependentFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dependentfile-md5.html language=enus -->
## TOPIC 02647: MD5

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dependentfile-md5.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dependentfile-md5.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the MD5 message-digest for the file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string MD5 { get; set; }ReturnsA string containing the message-digest.

### MD5

Gets or sets the MD5 message-digest for the file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string MD5 { get; set; }

#### Returns

A string containing the message-digest.

Parent topic:

DependentFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dependentfile-path.html language=enus -->
## TOPIC 02648: Path

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dependentfile-path.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dependentfile-path.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the path to the file on the host computer. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Path { get; }ReturnsThe path to the file.

### Path

Gets the path to the file on the host computer.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Path { get; }

#### Returns

The path to the file.

Parent topic:

DependentFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dependentfile-rtdestination.html language=enus -->
## TOPIC 02649: RTDestination

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dependentfile-rtdestination.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dependentfile-rtdestination.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the destination path, including the filename, for the file on the target. This property must be an absolute path. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string RTDestination { get; set; }ReturnsThe absolute path to the destination.

### RTDestination

Gets or sets the destination path, including the filename, for the file on the target. This property must be an absolute path.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string RTDestination { get; set; }

#### Returns

The absolute path to the destination.

Parent topic:

DependentFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dependentfile-setpath__string-string.html language=enus -->
## TOPIC 02650: SetPath(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dependentfile-setpath__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dependentfile-setpath__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the paths to a DependentFile and the system definition file with which it is associated. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetPath(string FilePath, string SDFPath)ParametersNameTypeDescriptionFilePathstringThe path to the DependentFile.SDFPathstringTh

### SetPath(string, string)

Sets the paths to a [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html) and the system definition file with which it is associated.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetPath(string FilePath, string SDFPath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| FilePath | string | The path to the DependentFile. |
| SDFPath | string | The path to the system definition file that requires the DependentFile. |

Parent topic:

DependentFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dependentfile-supportedtarget.html language=enus -->
## TOPIC 02651: SupportedTarget

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dependentfile-supportedtarget.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dependentfile-supportedtarget.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the target operating system(s) to which the file is deployed. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string SupportedTarget { get; set; }ReturnsStandard values include All, PharLap, VxWorks, Windows, PharLap & Windows, PharLap & VxWorks, and VxWorks & W

### SupportedTarget

Gets or sets the target operating system(s) to which the file is deployed.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string SupportedTarget { get; set; }

#### Returns

Standard values include All, PharLap, VxWorks, Windows, PharLap & Windows, PharLap & VxWorks, and VxWorks & Windows.

Parent topic:

DependentFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dependentfile-type.html language=enus -->
## TOPIC 02652: Type

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dependentfile-type.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dependentfile-type.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the Path to the dependent file is absolute or relative to another directory. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DependentFileType Type { get; }ReturnsAn enumeration value of DependentFileType.

### Type

Gets whether the [Path](nationalinstruments-veristand-systemdefinitionapi-dependentfile-path.html) to the dependent file is absolute or relative to another directory.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DependentFileType](nationalinstruments-veristand-systemdefinitionapi-dependentfiletype.html) Type { get; }

#### Returns

An enumeration value of [DependentFileType](nationalinstruments-veristand-systemdefinitionapi-dependentfiletype.html).

Parent topic:

DependentFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dependentfile-version.html language=enus -->
## TOPIC 02653: Version

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dependentfile-version.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dependentfile-version.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets version information for the dependent file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Version { get; set; }ReturnsThis property can contain any string you want to store with the DependentFile.

### Version

Gets or sets version information for the dependent file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Version { get; set; }

#### Returns

This property can contain any string you want to store with the [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html).

Parent topic:

DependentFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dependentfile.html language=enus -->
## TOPIC 02654: DependentFile Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dependentfile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dependentfile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a dependent file, which can be any file that another node requires. For example, model files, bitfiles, and VIs that make up custom devices can all be dependent files. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DependentFileRemarksUse th

### DependentFile Class

Represents a dependent file, which can be any file that another node requires. For example, model files, bitfiles, and VIs that make up custom devices can all be dependent files.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DependentFile

#### Remarks

Use the members of this class to configure basic properties of a dependent file, such as the path to its location on the host, the destination path for the file on an RT target, and version information about the file.

**Accessing this Class**

- DependentFile Constructor

AFPBinaryFile

AddDependencies(DependentFile[])

SetDriverVIs

SetTimingSourceInitVIs

GetDependentFileProperty

Path

FPGABitfile

FPGAConfigFile

DLLPath

ModelPath

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| DependentFile(string, DependentFileType, string, bool, string, string, string) | Initializes a new instance of the DependentFile class for the specified file. This instance allows you to specify the type of FilePath used to specify the location of the file. |
| DependentFile(string, string, bool, string, string, string) | Initializes a new instance of the DependentFile class for the specified file. This instance requires an absolute FilePath to specify the location of the file. |

#### Properties

| Name | Description |
| --- | --- |
| ForceDownload | Gets or sets whether the file is set to force-download to the target. |
| MD5 | Gets or sets the MD5 message-digest for the file. |
| Path | Gets the path to the file on the host computer. |
| RTDestination | Gets or sets the destination path, including the filename, for the file on the target. This property must be an absolute path. |
| SupportedTarget | Gets or sets the target operating system(s) to which the file is deployed. |
| Type | Gets whether the Path to the dependent file is absolute or relative to another directory. |
| Version | Gets or sets version information for the dependent file. |

#### Methods

| Name | Description |
| --- | --- |
| GetAbsolutePath(string) | Gets the absolute path to a file by prepending the specified baseAbsolutePath to a relative path to the file. |
| SetPath(string, string) | Sets the paths to a DependentFile and the system definition file with which it is associated. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dependentfiletype.html language=enus -->
## TOPIC 02655: DependentFileType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dependentfiletype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dependentfiletype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of path used for the location of a DependentFile. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum DependentFileTypeRemarksThe paths to the NI VeriStand base directory, the application data directory, and the common data directory can vary depending on

### DependentFileType Enumeration

Specifies the type of path used for the location of a [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum DependentFileType

#### Remarks

The paths to the NI VeriStand base directory, the application data directory, and the common data directory can vary depending on your operating system and where you install NI VeriStand. Refer to the *NI VeriStand Directories and Aliases* topic in the *NI VeriStand Help* for the default locations of these directories.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Absolute |  | The path is an absolute path. |
| Relative |  | The path is relative to the base NI VeriStand directory. |
| ToCommonDocDir |  | The path is relative to the common data directory. |
| ToAppDataDir |  | The path is relative to the application data directory. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dependentnode-dependentnode__string.html language=enus -->
## TOPIC 02656: DependentNode(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dependentnode-dependentnode__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dependentnode-dependentnode__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DependentNode with the specified path. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DependentNode(string dependentNodePath)ParametersNameTypeDescriptiondependentNodePathstringThe path to the dependent node.

### DependentNode(string)

Initializes a new instance of the [DependentNode](nationalinstruments-veristand-systemdefinitionapi-dependentnode.html) with the specified path.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DependentNode(string dependentNodePath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| dependentNodePath | string | The path to the dependent node. |

Parent topic:

DependentNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dependentnode-path.html language=enus -->
## TOPIC 02657: Path

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dependentnode-path.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dependentnode-path.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The path to the dependent node. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Path { get; set; }

### Path

The path to the dependent node.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Path { get; set; }

Parent topic:

DependentNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dependentnode.html language=enus -->
## TOPIC 02658: DependentNode Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dependentnode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dependentnode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a dependent node that encapsulates the path to another node in the system definition. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DependentNodeConstructorsNameDescriptionDependentNode(string)Initializes a new instance of the DependentNode

### DependentNode Class

Represents a dependent node that encapsulates the path to another node in the system definition.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DependentNode

#### Constructors

| Name | Description |
| --- | --- |
| DependentNode(string) | Initializes a new instance of the DependentNode with the specified path. |

#### Properties

| Name | Description |
| --- | --- |
| Path | The path to the dependent node. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-addboolean__string-bool.html language=enus -->
## TOPIC 02659: AddBoolean(string, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-addboolean__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-addboolean__string-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a Boolean element to the dictionary. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddBoolean(string name, bool value)ParametersNameTypeDescriptionnamestringThe name, or key, for the element.valueboolThe initial value of the element.Returnstrue if the element was

### AddBoolean(string, bool)

Adds a Boolean element to the dictionary.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddBoolean(string name, bool value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name, or key, for the element. |
| value | bool | The initial value of the element. |

#### Returns

true if the element was added successfully.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-addbooleanarray__string-bool_arr1.html language=enus -->
## TOPIC 02660: AddBooleanArray(string, bool[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-addbooleanarray__string-bool_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-addbooleanarray__string-bool_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an Boolean array element to the dictionary. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddBooleanArray(string name, bool[] value)ParametersNameTypeDescriptionnamestringThe name, or key, for the element.valuebool[]The initial value of the element.Returnstrue if

### AddBooleanArray(string, bool[])

Adds an Boolean array element to the dictionary.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddBooleanArray(string name, bool[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name, or key, for the element. |
| value | bool[] | The initial value of the element. |

#### Returns

true if the element was added successfully.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-adddouble__string-double.html language=enus -->
## TOPIC 02661: AddDouble(string, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-adddouble__string-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-adddouble__string-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a double-precision floating-point numeric element to the dictionary. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddDouble(string name, double value)ParametersNameTypeDescriptionnamestringThe name, or key, for the element.valuedoubleThe initial value of the ele

### AddDouble(string, double)

Adds a double-precision floating-point numeric element to the dictionary.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddDouble(string name, double value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name, or key, for the element. |
| value | double | The initial value of the element. |

#### Returns

true if the element was added successfully.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-adddoublearray__string-double_arr1.html language=enus -->
## TOPIC 02662: AddDoubleArray(string, double[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-adddoublearray__string-double_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-adddoublearray__string-double_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a double-precision floating-point numeric array element to the dictionary. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddDoubleArray(string name, double[] value)ParametersNameTypeDescriptionnamestringThe name, or key, for the element.valuedouble[]The initial v

### AddDoubleArray(string, double[])

Adds a double-precision floating-point numeric array element to the dictionary.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddDoubleArray(string name, double[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name, or key, for the element. |
| value | double[] | The initial value of the element. |

#### Returns

true if the element was added successfully.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-addi16__string-short.html language=enus -->
## TOPIC 02663: AddI16(string, short)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-addi16__string-short.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-addi16__string-short.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a signed 16-bit integer element to the dictionary. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddI16(string name, short value)ParametersNameTypeDescriptionnamestringThe name, or key, for the element.valueshortThe initial value of the element.Returnstrue if the

### AddI16(string, short)

Adds a signed 16-bit integer element to the dictionary.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddI16(string name, short value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name, or key, for the element. |
| value | short | The initial value of the element. |

#### Returns

true if the element was added successfully.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-addi16array__string-short_arr1.html language=enus -->
## TOPIC 02664: AddI16Array(string, short[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-addi16array__string-short_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-addi16array__string-short_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a signed 16-bit integer array element to the dictionary. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddI16Array(string name, short[] value)ParametersNameTypeDescriptionnamestringThe name, or key, for the element.valueshort[]The initial value of the element.Ret

### AddI16Array(string, short[])

Adds a signed 16-bit integer array element to the dictionary.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddI16Array(string name, short[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name, or key, for the element. |
| value | short[] | The initial value of the element. |

#### Returns

true if the element was added successfully.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-addi32__string-int.html language=enus -->
## TOPIC 02665: AddI32(string, int)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-addi32__string-int.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-addi32__string-int.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a signed 32-bit integer element to the dictionary. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddI32(string name, int value)ParametersNameTypeDescriptionnamestringThe name, or key, for the element.valueintThe initial value of the element.Returnstrue if the ele

### AddI32(string, int)

Adds a signed 32-bit integer element to the dictionary.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddI32(string name, int value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name, or key, for the element. |
| value | int | The initial value of the element. |

#### Returns

true if the element was added successfully.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-addi32array__string-int_arr1.html language=enus -->
## TOPIC 02666: AddI32Array(string, int[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-addi32array__string-int_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-addi32array__string-int_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a signed 32-bit integer array element to the dictionary. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddI32Array(string name, int[] value)ParametersNameTypeDescriptionnamestringThe name, or key, for the element.valueint[]The initial value of the element.Returns

### AddI32Array(string, int[])

Adds a signed 32-bit integer array element to the dictionary.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddI32Array(string name, int[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name, or key, for the element. |
| value | int[] | The initial value of the element. |

#### Returns

true if the element was added successfully.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-addi64__string-long.html language=enus -->
## TOPIC 02667: AddI64(string, long)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-addi64__string-long.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-addi64__string-long.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a signed 64-bit integer element to the dictionary. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddI64(string name, long value)ParametersNameTypeDescriptionnamestringThe name, or key, for the element.valuelongThe initial value of the element.Returnstrue if the e

### AddI64(string, long)

Adds a signed 64-bit integer element to the dictionary.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddI64(string name, long value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name, or key, for the element. |
| value | long | The initial value of the element. |

#### Returns

true if the element was added successfully.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-addi64array__string-long_arr1.html language=enus -->
## TOPIC 02668: AddI64Array(string, long[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-addi64array__string-long_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-addi64array__string-long_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a signed 64-bit integer array element to the dictionary. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddI64Array(string name, long[] value)ParametersNameTypeDescriptionnamestringThe name, or key, for the element.valuelong[]The initial value of the element.Retur

### AddI64Array(string, long[])

Adds a signed 64-bit integer array element to the dictionary.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddI64Array(string name, long[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name, or key, for the element. |
| value | long[] | The initial value of the element. |

#### Returns

true if the element was added successfully.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-addstring__string-string.html language=enus -->
## TOPIC 02669: AddString(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-addstring__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-addstring__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a string element to the dictionary. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddString(string name, string value)ParametersNameTypeDescriptionnamestringThe name, or key, for the element.valuestringThe initial value of the element.Returnstrue if the element w

### AddString(string, string)

Adds a string element to the dictionary.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddString(string name, string value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name, or key, for the element. |
| value | string | The initial value of the element. |

#### Returns

true if the element was added successfully.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-addstringarray__string-string_arr1.html language=enus -->
## TOPIC 02670: AddStringArray(string, string[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-addstringarray__string-string_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-addstringarray__string-string_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a string array element to the dictionary. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddStringArray(string name, string[] value)ParametersNameTypeDescriptionnamestringThe name, or key, for the element.valuestring[]The initial value of the element.Returnstrue i

### AddStringArray(string, string[])

Adds a string array element to the dictionary.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddStringArray(string name, string[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name, or key, for the element. |
| value | string[] | The initial value of the element. |

#### Returns

true if the element was added successfully.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-addu16__string-ushort.html language=enus -->
## TOPIC 02671: AddU16(string, ushort)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-addu16__string-ushort.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-addu16__string-ushort.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an unsigned 16-bit integer element to the dictionary. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddU16(string name, ushort value)ParametersNameTypeDescriptionnamestringThe name, or key, for the element.valueushortThe initial value of the element.Returnstrue i

### AddU16(string, ushort)

Adds an unsigned 16-bit integer element to the dictionary.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddU16(string name, ushort value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name, or key, for the element. |
| value | ushort | The initial value of the element. |

#### Returns

true if the element was added successfully.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-addu16array__string-ushort_arr1.html language=enus -->
## TOPIC 02672: AddU16Array(string, ushort[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-addu16array__string-ushort_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-addu16array__string-ushort_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an unsigned 16-bit integer array element to the dictionary. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddU16Array(string name, ushort[] value)ParametersNameTypeDescriptionnamestringThe name, or key, for the element.valueushort[]The initial value of the elemen

### AddU16Array(string, ushort[])

Adds an unsigned 16-bit integer array element to the dictionary.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddU16Array(string name, ushort[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name, or key, for the element. |
| value | ushort[] | The initial value of the element. |

#### Returns

true if the element was added successfully.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-addu32__string-uint.html language=enus -->
## TOPIC 02673: AddU32(string, uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-addu32__string-uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-addu32__string-uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an unsigned 32-bit integer element to the dictionary. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddU32(string name, uint value)ParametersNameTypeDescriptionnamestringThe name, or key, for the element.valueuintThe initial value of the element.Returnstrue if th

### AddU32(string, uint)

Adds an unsigned 32-bit integer element to the dictionary.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddU32(string name, uint value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name, or key, for the element. |
| value | uint | The initial value of the element. |

#### Returns

true if the element was added successfully.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-addu32array__string-uint_arr1.html language=enus -->
## TOPIC 02674: AddU32Array(string, uint[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-addu32array__string-uint_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-addu32array__string-uint_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an unsigned 32-bit integer array element to the dictionary. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddU32Array(string name, uint[] value)ParametersNameTypeDescriptionnamestringThe name, or key, for the element.valueuint[]The initial value of the element.Re

### AddU32Array(string, uint[])

Adds an unsigned 32-bit integer array element to the dictionary.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddU32Array(string name, uint[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name, or key, for the element. |
| value | uint[] | The initial value of the element. |

#### Returns

true if the element was added successfully.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-addu64__string-ulong.html language=enus -->
## TOPIC 02675: AddU64(string, ulong)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-addu64__string-ulong.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-addu64__string-ulong.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an unsigned 64-bit integer element to the dictionary. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddU64(string name, ulong value)ParametersNameTypeDescriptionnamestringThe name, or key, for the element.valueulongThe initial value of the element.Returnstrue if

### AddU64(string, ulong)

Adds an unsigned 64-bit integer element to the dictionary.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddU64(string name, ulong value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name, or key, for the element. |
| value | ulong | The initial value of the element. |

#### Returns

true if the element was added successfully.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-addu64array__string-ulong_arr1.html language=enus -->
## TOPIC 02676: AddU64Array(string, ulong[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-addu64array__string-ulong_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-addu64array__string-ulong_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an unsigned 64-bit integer array element to the dictionary. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddU64Array(string name, ulong[] value)ParametersNameTypeDescriptionnamestringThe name, or key, for the element.valueulong[]The initial value of the element.

### AddU64Array(string, ulong[])

Adds an unsigned 64-bit integer array element to the dictionary.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddU64Array(string name, ulong[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name, or key, for the element. |
| value | ulong[] | The initial value of the element. |

#### Returns

true if the element was added successfully.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-clear.html language=enus -->
## TOPIC 02677: Clear()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-clear.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-clear.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the dictionary of all elements. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void Clear()

### Clear()

Clears the dictionary of all elements.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void Clear()

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-count.html language=enus -->
## TOPIC 02678: Count

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-count.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-count.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the total number of key/value pairs in a Dictionary. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int Count { get; }ReturnsThe number of key/value pairs in the dictionary.

### Count

Gets the total number of key/value pairs in a [Dictionary](nationalinstruments-veristand-systemdefinitionapi-dictionary.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int Count { get; }

#### Returns

The number of key/value pairs in the dictionary.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-dictionary.html language=enus -->
## TOPIC 02679: Dictionary()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-dictionary.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-dictionary.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the Dictionary class and creates a new dictionary. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Dictionary()

### Dictionary()

Initializes a new instance of the [Dictionary](nationalinstruments-veristand-systemdefinitionapi-dictionary.html) class and creates a new dictionary.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Dictionary()

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-dictionary__dictionary.html language=enus -->
## TOPIC 02680: Dictionary(Dictionary)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-dictionary__dictionary.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-dictionary__dictionary.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the Dictionary class and creates a new dictionary that contains the same elements as the dictionary specified by toCopy . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Dictionary(Dictionary toCopy)ParametersNameTypeDescriptiontoCopyDictionaryT

### Dictionary(Dictionary)

Initializes a new instance of the [Dictionary](nationalinstruments-veristand-systemdefinitionapi-dictionary.html) class and creates a new dictionary that contains the same elements as the dictionary specified by *toCopy* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Dictionary(Dictionary toCopy)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| toCopy | Dictionary | The Dictionary whose elements you want to copy into the new dictionary. |

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-elem.html language=enus -->
## TOPIC 02681: Elem

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-elem.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-elem.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets all the elements in the Dictionary. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DictionaryElement[] Elem { get; }ReturnsThe elements, as an array of DictionaryElement objects.

### Elem

Gets all the elements in the [Dictionary](nationalinstruments-veristand-systemdefinitionapi-dictionary.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DictionaryElement](nationalinstruments-veristand-systemdefinitionapi-dictionaryelement.html)[] Elem { get; }

#### Returns

The elements, as an array of [DictionaryElement](nationalinstruments-veristand-systemdefinitionapi-dictionaryelement.html) objects.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-getboolean__string-out.html language=enus -->
## TOPIC 02682: GetBoolean(string, out bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-getboolean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-getboolean__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Boolean element specified by name . This method also returns the current value of the element. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetBoolean(string name, out bool value)ParametersNameTypeDescriptionnamestringThe name of the element.valueout boolThe

### GetBoolean(string, out bool)

Gets the Boolean element specified by *name* . This method also returns the current *value*  of the element.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetBoolean(string name, out bool value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the element. |
| value | out bool | The current value of the element. |

#### Returns

true if the element was found in the current dictionary.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-getbooleanarray__string-out.html language=enus -->
## TOPIC 02683: GetBooleanArray(string, out bool[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-getbooleanarray__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-getbooleanarray__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Boolean array element specified by name . This method also returns the current value of the element. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetBooleanArray(string name, out bool[] value)ParametersNameTypeDescriptionnamestringThe name of the element.val

### GetBooleanArray(string, out bool[])

Gets the Boolean array element specified by *name* . This method also returns the current *value*  of the element.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetBooleanArray(string name, out bool[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the element. |
| value | out bool[] | The current value of the element. |

#### Returns

true if the element was found in the current dictionary.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-getdouble__string-out.html language=enus -->
## TOPIC 02684: GetDouble(string, out double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-getdouble__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-getdouble__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the double-precision floating-point numeric element specified by name . This method also returns the current value of the element. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetDouble(string name, out double value)ParametersNameTypeDescriptionnamestringThe nam

### GetDouble(string, out double)

Gets the double-precision floating-point numeric element specified by *name* . This method also returns the current *value*  of the element.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetDouble(string name, out double value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the element. |
| value | out double | The current value of the element. |

#### Returns

true if the element was found in the current dictionary.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-getdoublearray__string-out.html language=enus -->
## TOPIC 02685: GetDoubleArray(string, out double[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-getdoublearray__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-getdoublearray__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the double-precision floating-point numeric array element specified by name . This method also returns the current value of the element. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetDoubleArray(string name, out double[] value)ParametersNameTypeDescriptionname

### GetDoubleArray(string, out double[])

Gets the double-precision floating-point numeric array element specified by *name* . This method also returns the current *value*  of the element.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetDoubleArray(string name, out double[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the element. |
| value | out double[] | The current value of the element. |

#### Returns

true if the element was found in the current dictionary.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-geti16__string-out.html language=enus -->
## TOPIC 02686: GetI16(string, out short)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-geti16__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-geti16__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the 16-bit signed integer element specified by name . This method also returns the current value of the element. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetI16(string name, out short value)ParametersNameTypeDescriptionnamestringThe name of the element.value

### GetI16(string, out short)

Gets the 16-bit signed integer element specified by *name* . This method also returns the current *value*  of the element.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetI16(string name, out short value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the element. |
| value | out short | The current value of the element. |

#### Returns

true if the element was found in the current dictionary.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-geti16array__string-out.html language=enus -->
## TOPIC 02687: GetI16Array(string, out short[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-geti16array__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-geti16array__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the 16-bit signed integer array element specified by name . This method also returns the current value of the element. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetI16Array(string name, out short[] value)ParametersNameTypeDescriptionnamestringThe name of the

### GetI16Array(string, out short[])

Gets the 16-bit signed integer array element specified by *name* . This method also returns the current *value*  of the element.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetI16Array(string name, out short[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the element. |
| value | out short[] | The current value of the element. |

#### Returns

true if the element was found in the current dictionary.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-geti32__string-out.html language=enus -->
## TOPIC 02688: GetI32(string, out int)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-geti32__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-geti32__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the 32-bit signed integer element specified by name . This method also returns the current value of the element. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetI32(string name, out int value)ParametersNameTypeDescriptionnamestringThe name of the element.valueou

### GetI32(string, out int)

Gets the 32-bit signed integer element specified by *name* . This method also returns the current *value*  of the element.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetI32(string name, out int value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the element. |
| value | out int | The current value of the element. |

#### Returns

true if the element was found in the current dictionary.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-geti32array__string-out.html language=enus -->
## TOPIC 02689: GetI32Array(string, out int[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-geti32array__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-geti32array__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the 32-bit signed integer array element specified by name . This method also returns the current value of the element. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetI32Array(string name, out int[] value)ParametersNameTypeDescriptionnamestringThe name of the el

### GetI32Array(string, out int[])

Gets the 32-bit signed integer array element specified by *name* . This method also returns the current *value*  of the element.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetI32Array(string name, out int[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the element. |
| value | out int[] | The current value of the element. |

#### Returns

true if the element was found in the current dictionary.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-geti64__string-out.html language=enus -->
## TOPIC 02690: GetI64(string, out long)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-geti64__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-geti64__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the 64-bit signed integer element specified by name . This method also returns the current value of the element. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetI64(string name, out long value)ParametersNameTypeDescriptionnamestringThe name of the element.valueo

### GetI64(string, out long)

Gets the 64-bit signed integer element specified by *name* . This method also returns the current *value*  of the element.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetI64(string name, out long value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the element. |
| value | out long | The current value of the element. |

#### Returns

true if the element was found in the current dictionary.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-geti64array__string-out.html language=enus -->
## TOPIC 02691: GetI64Array(string, out long[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-geti64array__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-geti64array__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the 64-bit signed integer array element specified by name . This method also returns the current value of the element. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetI64Array(string name, out long[] value)ParametersNameTypeDescriptionnamestringThe name of the e

### GetI64Array(string, out long[])

Gets the 64-bit signed integer array element specified by *name* . This method also returns the current *value*  of the element.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetI64Array(string name, out long[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the element. |
| value | out long[] | The current value of the element. |

#### Returns

true if the element was found in the current dictionary.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-getstring__string-out.html language=enus -->
## TOPIC 02692: GetString(string, out string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-getstring__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-getstring__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the string element specified by name . This method also returns the current value of the element. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetString(string name, out string value)ParametersNameTypeDescriptionnamestringThe name of the element.valueout stringT

### GetString(string, out string)

Gets the string element specified by *name* . This method also returns the current *value*  of the element.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetString(string name, out string value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the element. |
| value | out string | The current value of the element. |

#### Returns

true if the element was found in the current dictionary.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-getstringarray__string-out.html language=enus -->
## TOPIC 02693: GetStringArray(string, out string[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-getstringarray__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-getstringarray__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the string array element specified by name . This method also returns the current value of the element. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetStringArray(string name, out string[] value)ParametersNameTypeDescriptionnamestringThe name of the element.val

### GetStringArray(string, out string[])

Gets the string array element specified by *name* . This method also returns the current *value*  of the element.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetStringArray(string name, out string[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the element. |
| value | out string[] | The current value of the element. |

#### Returns

true if the element was found in the current dictionary.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-getu16__string-out.html language=enus -->
## TOPIC 02694: GetU16(string, out ushort)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-getu16__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-getu16__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the unsigned 16-bit integer element specified by name . This method also returns the current value of the element. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetU16(string name, out ushort value)ParametersNameTypeDescriptionnamestringThe name of the element.va

### GetU16(string, out ushort)

Gets the unsigned 16-bit integer element specified by *name* . This method also returns the current *value*  of the element.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetU16(string name, out ushort value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the element. |
| value | out ushort | The current value of the element. |

#### Returns

true if the element was found in the current dictionary.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-getu16array__string-out.html language=enus -->
## TOPIC 02695: GetU16Array(string, out ushort[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-getu16array__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-getu16array__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the unsigned 16-bit integer array element specified by name . This method also returns the current value of the element. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetU16Array(string name, out ushort[] value)ParametersNameTypeDescriptionnamestringThe name of t

### GetU16Array(string, out ushort[])

Gets the unsigned 16-bit integer array element specified by *name* . This method also returns the current *value*  of the element.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetU16Array(string name, out ushort[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the element. |
| value | out ushort[] | The current value of the element. |

#### Returns

true if the element was found in the current dictionary.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-getu32__string-out.html language=enus -->
## TOPIC 02696: GetU32(string, out uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-getu32__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-getu32__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the unsigned 32-bit integer element specified by name . This method also returns the current value of the element. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetU32(string name, out uint value)ParametersNameTypeDescriptionnamestringThe name of the element.valu

### GetU32(string, out uint)

Gets the unsigned 32-bit integer element specified by *name* . This method also returns the current *value*  of the element.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetU32(string name, out uint value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the element. |
| value | out uint | The current value of the element. |

#### Returns

true if the element was found in the current dictionary.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-getu32array__string-out.html language=enus -->
## TOPIC 02697: GetU32Array(string, out uint[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-getu32array__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-getu32array__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the unsigned 32-bit integer array element specified by name . This method also returns the current value of the element. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetU32Array(string name, out uint[] value)ParametersNameTypeDescriptionnamestringThe name of the

### GetU32Array(string, out uint[])

Gets the unsigned 32-bit integer array element specified by *name* . This method also returns the current *value*  of the element.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetU32Array(string name, out uint[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the element. |
| value | out uint[] | The current value of the element. |

#### Returns

true if the element was found in the current dictionary.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-getu64__string-out.html language=enus -->
## TOPIC 02698: GetU64(string, out ulong)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-getu64__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-getu64__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the unsigned 64-bit integer element specified by name . This method also returns the current value of the element. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetU64(string name, out ulong value)ParametersNameTypeDescriptionnamestringThe name of the element.val

### GetU64(string, out ulong)

Gets the unsigned 64-bit integer element specified by *name* . This method also returns the current *value*  of the element.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetU64(string name, out ulong value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the element. |
| value | out ulong | The current value of the element. |

#### Returns

true if the element was found in the current dictionary.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-getu64array__string-out.html language=enus -->
## TOPIC 02699: GetU64Array(string, out ulong[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-getu64array__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-getu64array__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the unsigned 64-bit integer array element specified by name . This method also returns the current value of the element. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetU64Array(string name, out ulong[] value)ParametersNameTypeDescriptionnamestringThe name of th

### GetU64Array(string, out ulong[])

Gets the unsigned 64-bit integer array element specified by *name* . This method also returns the current *value*  of the element.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetU64Array(string name, out ulong[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the element. |
| value | out ulong[] | The current value of the element. |

#### Returns

true if the element was found in the current dictionary.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary-removeelement__string.html language=enus -->
## TOPIC 02700: RemoveElement(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary-removeelement__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary-removeelement__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes the element specified by key , which is the name of the element. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool RemoveElement(string key)ParametersNameTypeDescriptionkeystringThe name of the element to remove from the dictionary.Returnstrue if the element was r

### RemoveElement(string)

Removes the element specified by *key* , which is the name of the element.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool RemoveElement(string key)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| key | string | The name of the element to remove from the dictionary. |

#### Returns

true if the element was removed successfully. This method returns false if no element matching *key*  is found.

Parent topic:

Dictionary Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionary.html language=enus -->
## TOPIC 02701: Dictionary Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionary.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionary.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a dictionary, which is an associative array. You can set dictionaries as values for CustomDevice and TimingAndSyncDevice items. Derives fromICloneableSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Dictionary : ICloneableRemarksUse the members of this class

### Dictionary Class

Represents a dictionary, which is an associative array. You can set dictionaries as values for [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html) and [TimingAndSyncDevice](nationalinstruments-veristand-systemdefinitionapi-timingandsyncdevice.html) items.

#### Derives from

- ICloneable

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Dictionary : ICloneable

#### Remarks

Use the members of this class to create dictionaries and add and remove elements from them.

**Accessing this Class**

- Dictionary Constructor

GetDictionaryArrayProperty

GetDictionaryProperty

SetDictionaryArrayProperty

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Dictionary() | Initializes a new instance of the Dictionary class and creates a new dictionary. |
| Dictionary(Dictionary) | Initializes a new instance of the Dictionary class and creates a new dictionary that contains the same elements as the dictionary specified by toCopy . |

#### Properties

| Name | Description |
| --- | --- |
| Count | Gets the total number of key/value pairs in a Dictionary. |
| Elem | Gets all the elements in the Dictionary. |

#### Methods

| Name | Description |
| --- | --- |
| AddBoolean(string, bool) | Adds a Boolean element to the dictionary. |
| AddBooleanArray(string, bool[]) | Adds an Boolean array element to the dictionary. |
| AddDouble(string, double) | Adds a double-precision floating-point numeric element to the dictionary. |
| AddDoubleArray(string, double[]) | Adds a double-precision floating-point numeric array element to the dictionary. |
| AddI16(string, short) | Adds a signed 16-bit integer element to the dictionary. |
| AddI16Array(string, short[]) | Adds a signed 16-bit integer array element to the dictionary. |
| AddI32(string, int) | Adds a signed 32-bit integer element to the dictionary. |
| AddI32Array(string, int[]) | Adds a signed 32-bit integer array element to the dictionary. |
| AddI64(string, long) | Adds a signed 64-bit integer element to the dictionary. |
| AddI64Array(string, long[]) | Adds a signed 64-bit integer array element to the dictionary. |
| AddString(string, string) | Adds a string element to the dictionary. |
| AddStringArray(string, string[]) | Adds a string array element to the dictionary. |
| AddU16(string, ushort) | Adds an unsigned 16-bit integer element to the dictionary. |
| AddU16Array(string, ushort[]) | Adds an unsigned 16-bit integer array element to the dictionary. |
| AddU32(string, uint) | Adds an unsigned 32-bit integer element to the dictionary. |
| AddU32Array(string, uint[]) | Adds an unsigned 32-bit integer array element to the dictionary. |
| AddU64(string, ulong) | Adds an unsigned 64-bit integer element to the dictionary. |
| AddU64Array(string, ulong[]) | Adds an unsigned 64-bit integer array element to the dictionary. |
| Clear() | Clears the dictionary of all elements. |
| GetBoolean(string, out bool) | Gets the Boolean element specified by name . This method also returns the current value of the element. |
| GetBooleanArray(string, out bool[]) | Gets the Boolean array element specified by name . This method also returns the current value of the element. |
| GetDouble(string, out double) | Gets the double-precision floating-point numeric element specified by name . This method also returns the current value of the element. |
| GetDoubleArray(string, out double[]) | Gets the double-precision floating-point numeric array element specified by name . This method also returns the current value of the element. |
| GetI16(string, out short) | Gets the 16-bit signed integer element specified by name . This method also returns the current value of the element. |
| GetI16Array(string, out short[]) | Gets the 16-bit signed integer array element specified by name . This method also returns the current value of the element. |
| GetI32(string, out int) | Gets the 32-bit signed integer element specified by name . This method also returns the current value of the element. |
| GetI32Array(string, out int[]) | Gets the 32-bit signed integer array element specified by name . This method also returns the current value of the element. |
| GetI64(string, out long) | Gets the 64-bit signed integer element specified by name . This method also returns the current value of the element. |
| GetI64Array(string, out long[]) | Gets the 64-bit signed integer array element specified by name . This method also returns the current value of the element. |
| GetString(string, out string) | Gets the string element specified by name . This method also returns the current value of the element. |
| GetStringArray(string, out string[]) | Gets the string array element specified by name . This method also returns the current value of the element. |
| GetU16(string, out ushort) | Gets the unsigned 16-bit integer element specified by name . This method also returns the current value of the element. |
| GetU16Array(string, out ushort[]) | Gets the unsigned 16-bit integer array element specified by name . This method also returns the current value of the element. |
| GetU32(string, out uint) | Gets the unsigned 32-bit integer element specified by name . This method also returns the current value of the element. |
| GetU32Array(string, out uint[]) | Gets the unsigned 32-bit integer array element specified by name . This method also returns the current value of the element. |
| GetU64(string, out ulong) | Gets the unsigned 64-bit integer element specified by name . This method also returns the current value of the element. |
| GetU64Array(string, out ulong[]) | Gets the unsigned 64-bit integer array element specified by name . This method also returns the current value of the element. |
| RemoveElement(string) | Removes the element specified by key , which is the name of the element. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionaryelement-dictionaryelement__dictionaryelement.html language=enus -->
## TOPIC 02702: DictionaryElement(DictionaryElement)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionaryelement-dictionaryelement__dictionaryelement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionaryelement-dictionaryelement__dictionaryelement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DictionaryElement class and creates a new dictionary element by copying an existing element. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DictionaryElement(DictionaryElement toCopy)ParametersNameTypeDescriptiontoCopyDictionaryElementThe r

### DictionaryElement(DictionaryElement)

Initializes a new instance of the [DictionaryElement](nationalinstruments-veristand-systemdefinitionapi-dictionaryelement.html) class and creates a new dictionary element by copying an existing element.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DictionaryElement(DictionaryElement toCopy)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| toCopy | DictionaryElement | The reference to the dictionary element to copy. |

Parent topic:

DictionaryElement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionaryelement-item.html language=enus -->
## TOPIC 02703: Item

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionaryelement-item.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionaryelement-item.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a reference to a value of a dictionary element. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic object Item { get; set; }ReturnsA reference to the value, as a .

### Item

Gets or sets a reference to a value of a dictionary element.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public object Item { get; set; }

#### Returns

A reference to the value, as a .

Parent topic:

DictionaryElement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionaryelement-key.html language=enus -->
## TOPIC 02704: Key

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionaryelement-key.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionaryelement-key.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the key, or name, of a dictionary element. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Key { get; set; }ReturnsThe name of the element.

### Key

Gets or sets the key, or name, of a dictionary element.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Key { get; set; }

#### Returns

The name of the element.

Parent topic:

DictionaryElement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dictionaryelement.html language=enus -->
## TOPIC 02705: DictionaryElement Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dictionaryelement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dictionaryelement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an element, or a key/value pair, in a Dictionary. Derives fromICloneableSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DictionaryElement : ICloneableRemarksUse the members of this class to get and set keys and items (or values), and to create new elements b

### DictionaryElement Class

Represents an element, or a key/value pair, in a [Dictionary](nationalinstruments-veristand-systemdefinitionapi-dictionary.html).

#### Derives from

- ICloneable

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DictionaryElement : ICloneable

#### Remarks

Use the members of this class to get and set keys and items (or values), and to create new elements by copying existing ones.

**Accessing this Class**

- DictionaryElement Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| DictionaryElement(DictionaryElement) | Initializes a new instance of the DictionaryElement class and creates a new dictionary element by copying an existing element. |

#### Properties

| Name | Description |
| --- | --- |
| Item | Gets or sets a reference to a value of a dictionary element. |
| Key | Gets or sets the key, or name, of a dictionary element. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-directiontype.html language=enus -->
## TOPIC 02706: DirectionType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-directiontype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-directiontype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the direction of a signal slope or edge that causes a trigger. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum DirectionTypeMembersNameValueDescriptionRising10280A rising signal. Falling10171A falling signal.

### DirectionType Enumeration

Defines the direction of a signal slope or edge that causes a trigger.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum DirectionType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 10280 | A rising signal. |
| Falling | 10171 | A falling signal. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dwell-dwell__string-string-basenode.html language=enus -->
## TOPIC 02707: Dwell(string, string, BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dwell-dwell__string-string-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dwell-dwell__string-string-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of a Dwell step with a channel specifying the dwell time. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Dwell(string Name, string Description, BaseNode DwellTime)ParametersNameTypeDescriptionNamestringThe name of the step.DescriptionstringThe des

### Dwell(string, string, BaseNode)

Initializes a new instance of a [Dwell](nationalinstruments-veristand-systemdefinitionapi-dwell.html) step with a channel specifying the dwell time.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Dwell(string Name, string Description, BaseNode DwellTime)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the step. |
| Description | string | The description of the step. |
| DwellTime | BaseNode | The channel whose value specifies the amount of time to suspend the procedure. |

Parent topic:

Dwell Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dwell-dwell__string-string-double.html language=enus -->
## TOPIC 02708: Dwell(string, string, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dwell-dwell__string-string-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dwell-dwell__string-string-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of a Dwell step with a constant specifying the dwell time. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Dwell(string Name, string Description, double DwellTime)ParametersNameTypeDescriptionNamestringThe name of the step.DescriptionstringThe desc

### Dwell(string, string, double)

Initializes a new instance of a [Dwell](nationalinstruments-veristand-systemdefinitionapi-dwell.html) step with a constant specifying the dwell time.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Dwell(string Name, string Description, double DwellTime)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the step. |
| Description | string | The description of the step. |
| DwellTime | double | The constant value that specifies the amount of time to suspend the procedure. |

Parent topic:

Dwell Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dwell-dwelltimechannel.html language=enus -->
## TOPIC 02709: DwellTimeChannel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dwell-dwelltimechannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dwell-dwelltimechannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the channel whose value determines the amount of time to suspend the procedure. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode DwellTimeChannel { get; }ReturnsA BaseNode reference to the channel.

### DwellTimeChannel

Gets the channel whose value determines the amount of time to suspend the procedure.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) DwellTimeChannel { get; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the channel.

Parent topic:

Dwell Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dwell-dwelltimeconstant.html language=enus -->
## TOPIC 02710: DwellTimeConstant

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dwell-dwelltimeconstant.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dwell-dwelltimeconstant.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the constant value that determines the amount of time to suspend the procedure. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double DwellTimeConstant { get; }ReturnsThe constant dwell time value.

### DwellTimeConstant

Gets the constant value that determines the amount of time to suspend the procedure.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double DwellTimeConstant { get; }

#### Returns

The constant dwell time value.

Parent topic:

Dwell Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dwell-dwelltimeisconstant.html language=enus -->
## TOPIC 02711: DwellTimeIsConstant

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dwell-dwelltimeisconstant.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dwell-dwelltimeisconstant.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the amount of time to suspend the procedure is determined by a constant value or by a channel value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint DwellTimeIsConstant { get; }Returnstrue if the dwell time is specified by a constant. false if it is specifi

### DwellTimeIsConstant

Gets whether the amount of time to suspend the procedure is determined by a constant value or by a channel value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint DwellTimeIsConstant { get; }

#### Returns

true if the dwell time is specified by a constant. false if it is specified by a channel.

Parent topic:

Dwell Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dwell-setdwelltime__basenode.html language=enus -->
## TOPIC 02712: SetDwellTime(BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dwell-setdwelltime__basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dwell-setdwelltime__basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the amount of time to suspend the procedure using the value of a channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetDwellTime(BaseNode DwellTime)ParametersNameTypeDescriptionDwellTimeBaseNodeThe channel whose value determines the amount of time to suspend

### SetDwellTime(BaseNode)

Sets the amount of time to suspend the procedure using the value of a channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetDwellTime(BaseNode DwellTime)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| DwellTime | BaseNode | The channel whose value determines the amount of time to suspend the procedure. |

Parent topic:

Dwell Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dwell-setdwelltime__double.html language=enus -->
## TOPIC 02713: SetDwellTime(double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dwell-setdwelltime__double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dwell-setdwelltime__double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the amount of time to suspend the procedure using a constant value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetDwellTime(double DwellTime)ParametersNameTypeDescriptionDwellTimedoubleThe constant value that determines the amount of time to suspend the proced

### SetDwellTime(double)

Sets the amount of time to suspend the procedure using a constant value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetDwellTime(double DwellTime)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| DwellTime | double | The constant value that determines the amount of time to suspend the procedure. |

Parent topic:

Dwell Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dwell.html language=enus -->
## TOPIC 02714: Dwell Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dwell.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dwell.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Dwell step that you add to a procedure. The Dwell step suspends the procedure by the amount of time you specify. Derives fromCommandSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Dwell : CommandRemarksUse the members of this class to configure the dwell t

### Dwell Class

Represents a **Dwell** step that you add to a procedure. The **Dwell** step suspends the procedure by the amount of time you specify.

#### Derives from

- Command

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Dwell : Command

#### Remarks

Use the members of this class to configure the dwell time for the step.

**Accessing this Class**

- Dwell Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Dwell(string, string, double) | Initializes a new instance of a Dwell step with a constant specifying the dwell time. |
| Dwell(string, string, BaseNode) | Initializes a new instance of a Dwell step with a channel specifying the dwell time. |

#### Properties

| Name | Description |
| --- | --- |
| DwellTimeChannel | Gets the channel whose value determines the amount of time to suspend the procedure. |
| DwellTimeConstant | Gets the constant value that determines the amount of time to suspend the procedure. |
| DwellTimeIsConstant | Gets whether the amount of time to suspend the procedure is determined by a constant value or by a channel value. |

#### Methods

| Name | Description |
| --- | --- |
| SetDwellTime(double) | Sets the amount of time to suspend the procedure using a constant value. |
| SetDwellTime(BaseNode) | Sets the amount of time to suspend the procedure using the value of a channel. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dynamicsignal-md5.html language=enus -->
## TOPIC 02715: MD5

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dynamicsignal-md5.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dynamicsignal-md5.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the MD5 message-digest for the signal. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic byte[] MD5 { get; }ReturnsThe message-digest, as a byte array.

### MD5

Gets the MD5 message-digest for the signal.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public byte[] MD5 { get; }

#### Returns

The message-digest, as a byte array.

Parent topic:

DynamicSignal Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-dynamicsignal.html language=enus -->
## TOPIC 02716: DynamicSignal Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-dynamicsignal.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-dynamicsignal.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a dynamic signal contained in a multiplexed frame. NI VeriStand organizes dynamic signals under Mode nodes. Derives fromChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DynamicSignal : ChannelRemarksUse the members of this class to access a dynamic sig

### DynamicSignal Class

Represents a dynamic signal contained in a multiplexed frame. NI VeriStand organizes dynamic signals under [Mode](nationalinstruments-veristand-systemdefinitionapi-mode.html) nodes.

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DynamicSignal : Channel

#### Remarks

Note

Only an NI-XNET CAN port can contain multiplexed frames.

**Accessing this Class**

- M:NationalInstruments.VeriStand.SystemDefinitionAPI.Mode.GetDynamicSignal

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| MD5 | Gets the MD5 message-digest for the signal. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-addvirtualecu__string.html language=enus -->
## TOPIC 02717: AddVirtualECU(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-addvirtualecu__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-addvirtualecu__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new virtual ECU to the virtual ECU list. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void AddVirtualECU(string virtualECUName)ParametersNameTypeDescriptionvirtualECUNamestringThe name of the Virtual ECU to be added.

### AddVirtualECU(string)

Adds a new virtual ECU to the virtual ECU list.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void AddVirtualECU(string virtualECUName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| virtualECUName | string | The name of the Virtual ECU to be added. |

Parent topic:

ECUNetworkCluster Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-canconfiguration.html language=enus -->
## TOPIC 02718: CANConfiguration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-canconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-canconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the protocol specific configuration when Protocol is set to CAN. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ICANConfiguration CANConfiguration { get; private set; }

### CANConfiguration

Represents the protocol specific configuration when [Protocol](nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-protocol.html) is set to CAN.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ICANConfiguration](nationalinstruments-veristand-systemdefinitionapi-icanconfiguration.html) CANConfiguration { get; private set; }

Parent topic:

ECUNetworkCluster Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-clustername.html language=enus -->
## TOPIC 02719: ClusterName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-clustername.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-clustername.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the ECU Network Cluster. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string ClusterName { get; set; }RemarksSet the name of the silver virtual bus as cluster name when using virtual ECUs built using Synopsys Silver®.

### ClusterName

Gets or sets the name of the ECU Network Cluster.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string ClusterName { get; set; }

#### Remarks

Set the name of the silver virtual bus as cluster name when using virtual ECUs built using Synopsys Silver®.

Parent topic:

ECUNetworkCluster Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-ecunetworkcluster__string-string-string-int-int-ushort.html language=enus -->
## TOPIC 02720: ECUNetworkCluster(string, string, string, int, int, ushort)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-ecunetworkcluster__string-string-string-int-int-ushort.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-ecunetworkcluster__string-string-string-int-int-ushort.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the ECUNetworkCluster. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ECUNetworkCluster(string name, string description, string ecuNetworkClusterPath, int processor, int decimation, ushort initialState)ParametersNameTypeDescriptionnamestringThe

### ECUNetworkCluster(string, string, string, int, int, ushort)

Initializes a new instance of the [ECUNetworkCluster](nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public ECUNetworkCluster(string name, string description, string ecuNetworkClusterPath, int processor, int decimation, ushort initialState)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the ECU network cluster. |
| description | string | The description of the ECU network cluster. |
| ecuNetworkClusterPath | string | The path to the ECU network cluster. |
| processor | int | The processor on which the ECU network cluster runs. |
| decimation | int | The decimation applied to the Primary Control Loop rate to determine the base rate for executing the ECU network cluster. |
| initialState | ushort | The initial execution state of the ECU network cluster. 0: Running. 1: Paused. |

Parent topic:

ECUNetworkCluster Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-ethernetconfiguration.html language=enus -->
## TOPIC 02721: EthernetConfiguration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-ethernetconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-ethernetconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the protocol specific configuration when Protocol is set to Ethernet. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic IEthernetConfiguration EthernetConfiguration { get; private set; }

### EthernetConfiguration

Represents the protocol specific configuration when [Protocol](nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-protocol.html) is set to Ethernet.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [IEthernetConfiguration](nationalinstruments-veristand-systemdefinitionapi-iethernetconfiguration.html) EthernetConfiguration { get; private set; }

Parent topic:

ECUNetworkCluster Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-getvirtualecus.html language=enus -->
## TOPIC 02722: GetVirtualECUs()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-getvirtualecus.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-getvirtualecus.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the names of virtual ECUs that have been added to the cluster as an array. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string[] GetVirtualECUs()ReturnsAn array of virtual ECU names as strings.

### GetVirtualECUs()

Returns the names of virtual ECUs that have been added to the cluster as an array.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string[] GetVirtualECUs()

#### Returns

An array of virtual ECU names as strings.

Parent topic:

ECUNetworkCluster Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-linconfiguration.html language=enus -->
## TOPIC 02723: LINConfiguration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-linconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-linconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the protocol specific configuration when Protocol is set to LIN. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ILINConfiguration LINConfiguration { get; private set; }

### LINConfiguration

Represents the protocol specific configuration when [Protocol](nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-protocol.html) is set to LIN.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ILINConfiguration](nationalinstruments-veristand-systemdefinitionapi-ilinconfiguration.html) LINConfiguration { get; private set; }

Parent topic:

ECUNetworkCluster Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-protocol.html language=enus -->
## TOPIC 02724: Protocol

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-protocol.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-protocol.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the CommunicationProtocol used by the ECU network cluster. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CommunicationProtocol Protocol { get; set; }

### Protocol

Gets or sets the [CommunicationProtocol](nationalinstruments-veristand-systemdefinitionapi-communicationprotocol.html) used by the ECU network cluster.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CommunicationProtocol](nationalinstruments-veristand-systemdefinitionapi-communicationprotocol.html) Protocol { get; set; }

Parent topic:

ECUNetworkCluster Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-reloadmodelfrompath__string-out.html language=enus -->
## TOPIC 02725: ReloadModelFromPath(string, out string[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-reloadmodelfrompath__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-reloadmodelfrompath__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reloads the model from the given path. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic override void ReloadModelFromPath(string newPath, out string[] invalidNames)ParametersNameTypeDescriptionnewPathstringNew path from which to reload the modelinvalidNamesout string[]Names o

### ReloadModelFromPath(string, out string[])

Reloads the model from the given path.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public override void ReloadModelFromPath(string newPath, out string[] invalidNames)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| newPath | string | New path from which to reload the model |
| invalidNames | out string[] | Names of the removed nodes |

Parent topic:

ECUNetworkCluster Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-removevirtualecu__string.html language=enus -->
## TOPIC 02726: RemoveVirtualECU(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-removevirtualecu__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-removevirtualecu__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes a virtual ECU from the virtual ECU list. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void RemoveVirtualECU(string virtualECUName)ParametersNameTypeDescriptionvirtualECUNamestringThe name of the Virtual ECU to be removed.

### RemoveVirtualECU(string)

Removes a virtual ECU from the virtual ECU list.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void RemoveVirtualECU(string virtualECUName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| virtualECUName | string | The name of the Virtual ECU to be removed. |

Parent topic:

ECUNetworkCluster Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-timestep.html language=enus -->
## TOPIC 02727: TimeStep

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-timestep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-timestep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the time interval between two successive network steps where frames are exchanged between real and virtual ECUs. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double TimeStep { get; set; }RemarksWhen using virtual ECUs built using Synopsys Silver, set the SVB

### TimeStep

Gets or sets the time interval between two successive network steps where frames are exchanged between real and virtual ECUs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double TimeStep { get; set; }

#### Remarks

When using virtual ECUs built using Synopsys Silver, set the SVB Step Size to this property.

Parent topic:

ECUNetworkCluster Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-virtualecutoolchain.html language=enus -->
## TOPIC 02728: VirtualECUToolchain

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-virtualecutoolchain.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-virtualecutoolchain.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the VirtualECUToolchain that was used to build virtual ECUs. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic VirtualECUToolchain VirtualECUToolchain { get; set; }

### VirtualECUToolchain

Gets or sets the name of the [VirtualECUToolchain](nationalinstruments-veristand-systemdefinitionapi-virtualecutoolchain.html) that was used to build virtual ECUs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [VirtualECUToolchain](nationalinstruments-veristand-systemdefinitionapi-virtualecutoolchain.html) VirtualECUToolchain { get; set; }

Parent topic:

ECUNetworkCluster Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster.html language=enus -->
## TOPIC 02729: ECUNetworkCluster Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an ECU network cluster as a specialized type of Model. Use the ECU network cluster to configure the communication between VirtualECU and an XNET device. Derives fromModelIECUNetworkClusterConfigurationSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class ECUNetwor

### ECUNetworkCluster Class

Represents an ECU network cluster as a specialized type of [Model](nationalinstruments-veristand-systemdefinitionapi-model.html). Use the ECU network cluster to configure the communication between [VirtualECU](nationalinstruments-veristand-systemdefinitionapi-virtualecu.html) and an XNET device.

#### Derives from

- Model
- IECUNetworkClusterConfiguration

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class ECUNetworkCluster : Model, IECUNetworkClusterConfiguration

#### Remarks

Use the members of this class to retrieve information about, set the decimation for, or reload a ECU network cluster.

#### Constructors

| Name | Description |
| --- | --- |
| ECUNetworkCluster(string, string, string, int, int, ushort) | Initializes a new instance of the ECUNetworkCluster. |

#### Properties

| Name | Description |
| --- | --- |
| CANConfiguration | Represents the protocol specific configuration when Protocol is set to CAN. |
| ClusterName | Gets or sets the name of the ECU Network Cluster. |
| EthernetConfiguration | Represents the protocol specific configuration when Protocol is set to Ethernet. |
| LINConfiguration | Represents the protocol specific configuration when Protocol is set to LIN. |
| Protocol | Gets or sets the CommunicationProtocol used by the ECU network cluster. |
| TimeStep | Gets or sets the time interval between two successive network steps where frames are exchanged between real and virtual ECUs. |
| VirtualECUToolchain | Gets or sets the name of the VirtualECUToolchain that was used to build virtual ECUs. |

#### Methods

| Name | Description |
| --- | --- |
| AddVirtualECU(string) | Adds a new virtual ECU to the virtual ECU list. |
| GetVirtualECUs() | Returns the names of virtual ECUs that have been added to the cluster as an array. |
| ReloadModelFromPath(string, out string[]) | Reloads the model from the given path. |
| RemoveVirtualECU(string) | Removes a virtual ECU from the virtual ECU list. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-edgetype.html language=enus -->
## TOPIC 02730: EdgeType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-edgetype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-edgetype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the edge type of the sample clock. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum EdgeTypeMembersNameValueDescriptionRising10280The rising edge of the sample clock. Falling10171The falling edge of the sample clock.

### EdgeType Enumeration

Defines the edge type of the sample clock.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum EdgeType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 10280 | The rising edge of the sample clock. |
| Falling | 10171 | The falling edge of the sample clock. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-end-end__string-string.html language=enus -->
## TOPIC 02731: End(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-end-end__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-end-end__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of End with the specified name and description. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic End(string Name, string Description)ParametersNameTypeDescriptionNamestringThe name of the step.DescriptionstringThe description of the step.

### End(string, string)

Initializes a new instance of [End](nationalinstruments-veristand-systemdefinitionapi-end.html) with the specified name and description.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public End(string Name, string Description)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the step. |
| Description | string | The description of the step. |

Parent topic:

End Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-end.html language=enus -->
## TOPIC 02732: End Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-end.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-end.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an End step that you can add to a procedure. The End step stops the procedure. Derives fromCommandSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class End : CommandRemarksUse the members of this class to access the End step. Accessing this ClassEnd Constructor Th

### End Class

Represents an **End** step that you can add to a procedure. The **End** step stops the procedure.

#### Derives from

- Command

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class End : Command

#### Remarks

Use the members of this class to access the **End** step.

**Accessing this Class**

- End Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| End(string, string) | Initializes a new instance of End with the specified name and description. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-eventtriggered-addrawdatabasedframe__rawdatabasedframe-out.html language=enus -->
## TOPIC 02733: AddRawDataBasedFrame(RawDataBasedFrame, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-eventtriggered-addrawdatabasedframe__rawdatabasedframe-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-eventtriggered-addrawdatabasedframe__rawdatabasedframe-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified raw signal format frame to the Event Triggered section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddRawDataBasedFrame(RawDataBasedFrame rawDataBasedFrame, out Error error)ParametersNameTypeDescriptionrawDataBasedFrameRawDataBasedFrameSpecifies

### AddRawDataBasedFrame(RawDataBasedFrame, out Error)

Adds the specified raw signal format frame to the **Event Triggered** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddRawDataBasedFrame(RawDataBasedFrame rawDataBasedFrame, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rawDataBasedFrame | RawDataBasedFrame | Specifies the raw signal format frame to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the frame was added successfully.

Parent topic:

EventTriggered Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-eventtriggered-addrawdatabasedframe__rawdatabasedframe.html language=enus -->
## TOPIC 02734: AddRawDataBasedFrame(RawDataBasedFrame)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-eventtriggered-addrawdatabasedframe__rawdatabasedframe.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-eventtriggered-addrawdatabasedframe__rawdatabasedframe.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified raw signal format frame to the Event Triggered section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddRawDataBasedFrame(RawDataBasedFrame rawDataBasedFrame)ParametersNameTypeDescriptionrawDataBasedFrameRawDataBasedFrameSpecifies the raw signal fo

### AddRawDataBasedFrame(RawDataBasedFrame)

Adds the specified raw signal format frame to the **Event Triggered** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddRawDataBasedFrame(RawDataBasedFrame rawDataBasedFrame)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rawDataBasedFrame | RawDataBasedFrame | Specifies the raw signal format frame to add. |

#### Returns

true if the frame was added successfully.

Parent topic:

EventTriggered Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-eventtriggered-addsignalbasedframe__signalbasedframe-out.html language=enus -->
## TOPIC 02735: AddSignalBasedFrame(SignalBasedFrame, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-eventtriggered-addsignalbasedframe__signalbasedframe-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-eventtriggered-addsignalbasedframe__signalbasedframe-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified signal format frame to the Event Triggered section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddSignalBasedFrame(SignalBasedFrame signalBasedFrame, out Error error)ParametersNameTypeDescriptionsignalBasedFrameSignalBasedFrameSpecifies the signa

### AddSignalBasedFrame(SignalBasedFrame, out Error)

Adds the specified signal format frame to the **Event Triggered** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddSignalBasedFrame(SignalBasedFrame signalBasedFrame, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signalBasedFrame | SignalBasedFrame | Specifies the signal format frame to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the frame was added successfully.

Parent topic:

EventTriggered Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-eventtriggered-addsignalbasedframe__signalbasedframe.html language=enus -->
## TOPIC 02736: AddSignalBasedFrame(SignalBasedFrame)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-eventtriggered-addsignalbasedframe__signalbasedframe.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-eventtriggered-addsignalbasedframe__signalbasedframe.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified signal format frame to the Event Triggered section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddSignalBasedFrame(SignalBasedFrame signalBasedFrame)ParametersNameTypeDescriptionsignalBasedFrameSignalBasedFrameSpecifies the signal format frame to

### AddSignalBasedFrame(SignalBasedFrame)

Adds the specified signal format frame to the **Event Triggered** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddSignalBasedFrame(SignalBasedFrame signalBasedFrame)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signalBasedFrame | SignalBasedFrame | Specifies the signal format frame to add. |

#### Returns

true if the frame was added successfully.

Parent topic:

EventTriggered Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-eventtriggered-getrawdatabasedframelist.html language=enus -->
## TOPIC 02737: GetRawDataBasedFrameList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-eventtriggered-getrawdatabasedframelist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-eventtriggered-getrawdatabasedframelist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the RawDataBasedFrame elements from the current EventTriggered section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic RawDataBasedFrame[] GetRawDataBasedFrameList()RemarksModifications you make to the contents of this list apply to the system de

### GetRawDataBasedFrameList()

Gets an array that contains the [RawDataBasedFrame](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe.html) elements from the current [EventTriggered](nationalinstruments-veristand-systemdefinitionapi-eventtriggered.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [RawDataBasedFrame](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe.html)[] GetRawDataBasedFrameList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [RawDataBasedFrame](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe.html) elements from the current [EventTriggered](nationalinstruments-veristand-systemdefinitionapi-eventtriggered.html) section.

Parent topic:

EventTriggered Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-eventtriggered-getsignalbasedframelist.html language=enus -->
## TOPIC 02738: GetSignalBasedFrameList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-eventtriggered-getsignalbasedframelist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-eventtriggered-getsignalbasedframelist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the SignalBasedFrame elements from the current EventTriggered section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SignalBasedFrame[] GetSignalBasedFrameList()RemarksModifications you make to the contents of this list apply to the system defin

### GetSignalBasedFrameList()

Gets an array that contains the [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html) elements from the current [EventTriggered](nationalinstruments-veristand-systemdefinitionapi-eventtriggered.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html)[] GetSignalBasedFrameList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html) elements from the current [EventTriggered](nationalinstruments-veristand-systemdefinitionapi-eventtriggered.html) section.

Parent topic:

EventTriggered Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-eventtriggered.html language=enus -->
## TOPIC 02739: EventTriggered Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-eventtriggered.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-eventtriggered.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Event Triggered section under an Outgoing section of an NI-XNET CAN or FlexRay port. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class EventTriggered : SectionRemarksUse the members of this class to add new or get a list of existing even

### EventTriggered Class

Represents the **Event Triggered** section under an [Outgoing](nationalinstruments-veristand-systemdefinitionapi-outgoing.html) section of an NI-XNET CAN or FlexRay port.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class EventTriggered : Section

#### Remarks

Note

LIN does not support event triggered frames.

**Accessing this Class**

- M:NationalInstruments.VeriStand.SystemDefinitionAPI.Outgoing.GetEventTriggered

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddRawDataBasedFrame(RawDataBasedFrame) | Adds the specified raw signal format frame to the Event Triggered section. |
| AddRawDataBasedFrame(RawDataBasedFrame, out Error) | Adds the specified raw signal format frame to the Event Triggered section. |
| AddSignalBasedFrame(SignalBasedFrame, out Error) | Adds the specified signal format frame to the Event Triggered section. |
| AddSignalBasedFrame(SignalBasedFrame) | Adds the specified signal format frame to the Event Triggered section. |
| GetRawDataBasedFrameList() | Gets an array that contains the RawDataBasedFrame elements from the current EventTriggered section. |
| GetSignalBasedFrameList() | Gets an array that contains the SignalBasedFrame elements from the current EventTriggered section. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-execution-getmodelcommand.html language=enus -->
## TOPIC 02740: GetModelCommand()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-execution-getmodelcommand.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-execution-getmodelcommand.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the ModelCommand channel, which sends commands to the model at run-time. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModelCommand GetModelCommand()ReturnsA ModelCommand object.

### GetModelCommand()

Gets the [ModelCommand](nationalinstruments-veristand-systemdefinitionapi-modelcommand.html) channel, which sends commands to the model at run-time.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ModelCommand](nationalinstruments-veristand-systemdefinitionapi-modelcommand.html) GetModelCommand()

#### Returns

A [ModelCommand](nationalinstruments-veristand-systemdefinitionapi-modelcommand.html) object.

Parent topic:

Execution Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-execution-getmodelstatus.html language=enus -->
## TOPIC 02741: GetModelStatus()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-execution-getmodelstatus.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-execution-getmodelstatus.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the ModelStatus channel, which tracks the current state of the model (running, paused, and so on). SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModelStatus GetModelStatus()ReturnsA ModelStatus object.

### GetModelStatus()

Gets the [ModelStatus](nationalinstruments-veristand-systemdefinitionapi-modelstatus.html) channel, which tracks the current state of the model (running, paused, and so on).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ModelStatus](nationalinstruments-veristand-systemdefinitionapi-modelstatus.html) GetModelStatus()

#### Returns

A [ModelStatus](nationalinstruments-veristand-systemdefinitionapi-modelstatus.html) object.

Parent topic:

Execution Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-execution-getmodeltime.html language=enus -->
## TOPIC 02742: GetModelTime()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-execution-getmodeltime.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-execution-getmodeltime.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the ModelTime channel, which tracks the amount of time that has elapsed since the model began execution. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModelTime GetModelTime()ReturnsA ModelTime object.

### GetModelTime()

Gets the [ModelTime](nationalinstruments-veristand-systemdefinitionapi-modeltime.html) channel, which tracks the amount of time that has elapsed since the model began execution.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ModelTime](nationalinstruments-veristand-systemdefinitionapi-modeltime.html) GetModelTime()

#### Returns

A [ModelTime](nationalinstruments-veristand-systemdefinitionapi-modeltime.html) object.

Parent topic:

Execution Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-execution.html language=enus -->
## TOPIC 02743: Execution Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-execution.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-execution.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Execution section under a Model. This section contains channels that get and set execution details of the model, such as its current status and the amount of time that has elapsed since it began executing. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinit

### Execution Class

Represents the **Execution** section under a [Model](nationalinstruments-veristand-systemdefinitionapi-model.html). This section contains channels that get and set execution details of the model, such as its current status and the amount of time that has elapsed since it began executing.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Execution : Section

#### Remarks

Use the members of this class to get the [ModelCommand](nationalinstruments-veristand-systemdefinitionapi-modelcommand.html), [ModelStatus](nationalinstruments-veristand-systemdefinitionapi-modelstatus.html), or [ModelTime](nationalinstruments-veristand-systemdefinitionapi-modeltime.html) channels.

**Accessing this Class**

- M:NationalInstruments.VeriStand.SystemDefinitionAPI.Model.GetExecutionSection

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| GetModelCommand() | Gets the ModelCommand channel, which sends commands to the model at run-time. |
| GetModelStatus() | Gets the ModelStatus channel, which tracks the current state of the model (running, paused, and so on). |
| GetModelTime() | Gets the ModelTime channel, which tracks the amount of time that has elapsed since the model began execution. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-executionorder.html language=enus -->
## TOPIC 02744: ExecutionOrder Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-executionorder.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-executionorder.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Execution Order section under SimulationModels, which contains information about the order that your models execute relative to each other in the VeriStand Engine. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class ExecutionOrder : Sectio

### ExecutionOrder Class

Represents the **Execution Order** section under [SimulationModels](nationalinstruments-veristand-systemdefinitionapi-simulationmodels.html), which contains information about the order that your models execute relative to each other in the VeriStand Engine.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class ExecutionOrder : Section

#### Remarks

Use the members of this class to access the **Execution Order** section.

**Accessing this Class**

- M:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels.GetExecutionOrder

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-exitsubroutine-exitsubroutine__string-string.html language=enus -->
## TOPIC 02745: ExitSubroutine(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-exitsubroutine-exitsubroutine__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-exitsubroutine-exitsubroutine__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of ExitSubroutine with the specified name and description. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ExitSubroutine(string Name, string Description)ParametersNameTypeDescriptionNamestringThe name of the ExitSubroutine step.DescriptionstringTh

### ExitSubroutine(string, string)

Initializes a new instance of [ExitSubroutine](nationalinstruments-veristand-systemdefinitionapi-exitsubroutine.html) with the specified name and description.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public ExitSubroutine(string Name, string Description)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the ExitSubroutine step. |
| Description | string | The description of the ExitSubroutine step. |

Parent topic:

ExitSubroutine Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-exitsubroutine.html language=enus -->
## TOPIC 02746: ExitSubroutine Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-exitsubroutine.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-exitsubroutine.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an Exit Subroutine step that you can add to a procedure. The Exit Subroutine step is typically used in procedures that are called from other procedures by a CallProcedure step. The Exit Subroutine step stops the current procedure and returns to the calling procedure. Derives fromCommandSy

### ExitSubroutine Class

Represents an **Exit Subroutine** step that you can add to a procedure. The **Exit Subroutine** step is typically used in procedures that are called from other procedures by a [CallProcedure](nationalinstruments-veristand-systemdefinitionapi-callprocedure.html) step. The **Exit Subroutine** step stops the current procedure and returns to the calling procedure.

#### Derives from

- Command

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class ExitSubroutine : Command

#### Remarks

Use the members of this class to access the **Exit Subroutine** step.

**Accessing this Class**

- ExitSubroutine Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| ExitSubroutine(string, string) | Initializes a new instance of ExitSubroutine with the specified name and description. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fdisomode.html language=enus -->
## TOPIC 02747: FDISOMode Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fdisomode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fdisomode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the interface is working in the ISO CAN FD standard (ISO standard 11898-1:2015) or non-ISO CAN FD standard (Bosch CAN FD 1.0 specification). Two ports using different standards (ISO CAN FD vs. non-ISO CAN FD) cannot communicate with each other. SyntaxNamespace: NationalInstruments.

### FDISOMode Enumeration

Specifies whether the interface is working in the ISO CAN FD standard (ISO standard 11898-1:2015) or non-ISO CAN FD standard (Bosch CAN FD 1.0 specification). Two ports using different standards (ISO CAN FD vs. non-ISO CAN FD) cannot communicate with each other.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum FDISOMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ISO | 0 | ISO CAN FD standard (ISO standard 11898-1:2015) In ISO CAN FD mode, for every transmitted frame, you can specify in the database or frame header whether a frame must be sent in CAN 2.0, CAN FD, or CAN FD+BRS mode. In the frame type field of the frame header, received frames indicate whether they have been sent with CAN 2.0, CAN FD, or CAN FD+BRS. You cannot use the Interface:CAN:Transmit I/O Mode property in ISO CAN FD mode, as the frame defines the transmit mode. |
| NonISO | 1 | The interface is working in the non-ISO CAN FD standard (Bosch CAN FD 1.0 specification). In Non-ISO CAN FD mode, CAN data frames are received at CAN data typed frames, which is either CAN 2.0, CAN FD, or CAN FD+BRS, but you cannot distinguish the standard in which the frame has been transmitted. |
| ISOLegacy | 2 | Use this mode only for compatibility with existing applications. In this mode, the behavior is the same as in Non-ISO CAN FD mode (Interface:CAN:Transmit I/O Mode is working, and received frames have the CAN data type). But the interface is working in ISO CAN FD mode, so you can communicate with other ISO CAN FD devices. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-filelimitationtype.html language=enus -->
## TOPIC 02748: FileLimitationType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-filelimitationtype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-filelimitationtype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of limit used to stop logging incoming frame data to an NI-XNET DataLoggingFile. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum FileLimitationTypeMembersNameValueDescriptionFootprint0Stops logging data to the current file when the file's LimitValue r

### FileLimitationType Enumeration

Specifies the type of limit used to stop logging incoming frame data to an NI-XNET [DataLoggingFile](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum FileLimitationType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Footprint | 0 | Stops logging data to the current file when the file's LimitValue reaches the size in kilobytes (kB) you specify. |
| Time | 1 | Stops logging data to the current file when the file's LimitValue reaches the time in seconds you specify. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-filetype.html language=enus -->
## TOPIC 02749: FileType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-filetype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-filetype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the file type of an NI-XNET DataLoggingFile. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum FileTypeMembersNameValueDescriptionTDMS0A .tdms file. NCL1A .ncl file, which is a binary file format used by NI-XNET, NI-CAN, and CompactRIO applications.

### FileType Enumeration

Specifies the file type of an NI-XNET [DataLoggingFile](nationalinstruments-veristand-systemdefinitionapi-dataloggingfile.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum FileType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| TDMS | 0 | A .tdms file. |
| NCL | 1 | A .ncl file, which is a binary file format used by NI-XNET, NI-CAN, and CompactRIO applications. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-finishedfiles.html language=enus -->
## TOPIC 02750: FinishedFiles Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-finishedfiles.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-finishedfiles.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Finished Files channel associated with an NI-XNET RawFrameDataLogging file. This channel stores the number of completed log files for the current session of the VeriStand Engine. You can use this channel to determine when a file is ready for use by other processes. Derives fromChannelSy

### FinishedFiles Class

Represents a **Finished Files** channel associated with an NI-XNET [RawFrameDataLogging](nationalinstruments-veristand-systemdefinitionapi-rawframedatalogging.html) file. This channel stores the number of completed log files for the current session of the VeriStand Engine. You can use this channel to determine when a file is ready for use by other processes.

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class FinishedFiles : Channel

#### Remarks

The logging process creates this channel. You cannot directly call this class.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI
