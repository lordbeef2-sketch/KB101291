# NI DOCUMENT BUNDLE: ni-daqmx-net-framework-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-daqmx-net-framework-api-ref start=1501 end=1750 -->
<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readreversevoltageerrorchannels.html language=enus -->
## TOPIC 01501: ReadReverseVoltageErrorChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readreversevoltageerrorchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readreversevoltageerrorchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of all virtual channels in the task for which reverse voltage error condition has been detected. You must read the Reverse Voltage Error Channels Exist property before you read this property. Otherwise, you will receive an error. SyntaxNamespace: NationalInstruments.DAQmxpu

### ReadReverseVoltageErrorChannels

Indicates a list of names of all virtual channels in the task for which reverse voltage error condition has been detected. You must read the Reverse Voltage Error Channels Exist property before you read this property. Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] ReadReverseVoltageErrorChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readreversevoltageerrorchannelsexist.html language=enus -->
## TOPIC 01502: ReadReverseVoltageErrorChannelsExist

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readreversevoltageerrorchannelsexist.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readreversevoltageerrorchannelsexist.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected reverse voltage error for any of the channels in the task. Reverse voltage error occurs if the local voltage is equal to the negative saturated voltage. Reading this property clears the error condition status for all channels in the task. You must read this proper

### ReadReverseVoltageErrorChannelsExist

Indicates if the device(s) detected reverse voltage error for any of the channels in the task. Reverse voltage error occurs if the local voltage is equal to the negative saturated voltage. Reading this property clears the error condition status for all channels in the task. You must read this property before you read the Reverse Voltage Error Channels property. Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool ReadReverseVoltageErrorChannelsExist { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readsleeptime.html language=enus -->
## TOPIC 01503: ReadSleepTime

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readsleeptime.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readsleeptime.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the amount of time to sleep after checking for available samples if ReadWaitMode is Sleep. SyntaxNamespace: NationalInstruments.DAQmxpublic double ReadSleepTime { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ReadSleepTime

Specifies in seconds the amount of time to sleep after checking for available samples if [ReadWaitMode](nationalinstruments-daqmx-daqstream-readwaitmode.html) is [Sleep](nationalinstruments-daqmx-readwaitmode.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double ReadSleepTime { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readsynchronizationunlockedchannels.html language=enus -->
## TOPIC 01504: ReadSynchronizationUnlockedChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readsynchronizationunlockedchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readsynchronizationunlockedchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the channels from devices in an unlocked target. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] ReadSynchronizationUnlockedChannels { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each i

### ReadSynchronizationUnlockedChannels

Indicates the channels from devices in an unlocked target.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] ReadSynchronizationUnlockedChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readsynchronizationunlockedchannelsexist.html language=enus -->
## TOPIC 01505: ReadSynchronizationUnlockedChannelsExist

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readsynchronizationunlockedchannelsexist.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readsynchronizationunlockedchannelsexist.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the target is currently locked to the grand master. Devices may report PLL Unlock either during acquisition or after acquisition. SyntaxNamespace: NationalInstruments.DAQmxpublic bool ReadSynchronizationUnlockedChannelsExist { get; }ExceptionsTypeDescriptionNationalInstruments.DAQm

### ReadSynchronizationUnlockedChannelsExist

Indicates whether the target is currently locked to the grand master. Devices may report PLL Unlock either during acquisition or after acquisition.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool ReadSynchronizationUnlockedChannelsExist { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readwaitmode.html language=enus -->
## TOPIC 01506: ReadWaitMode

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readwaitmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readwaitmode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how reading from the task waits for samples to become available. SyntaxNamespace: NationalInstruments.DAQmxpublic ReadWaitMode ReadWaitMode { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ReadWaitMode

Specifies how reading from the task waits for samples to become available.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [ReadWaitMode](nationalinstruments-daqmx-readwaitmode.html) ReadWaitMode { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-tdmslogginggroupname.html language=enus -->
## TOPIC 01507: TdmsLoggingGroupName

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-tdmslogginggroupname.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-tdmslogginggroupname.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of the group to create within the TDMS file for data from this task. If you append data to an existing file and the specified group already exists, NI-DAQmx appends a number symbol and a number to the group name, incrementing that number until finding a group name that does not ex

### TdmsLoggingGroupName

Specifies the name of the group to create within the [TDMS](/csh?context=nidaqmx_mxcncpts_datalogging) file for data from this task. If you append data to an existing file and the specified group already exists, NI-DAQmx appends a number symbol and a number to the group name, incrementing that number until finding a group name that does not exist. For example, if you specify a group name of Voltage [Task](nationalinstruments-daqmx-task.html), and that group already exists, NI-DAQmx assigns the group name Voltage [Task](nationalinstruments-daqmx-task.html) #1, then Voltage [Task](nationalinstruments-daqmx-task.html) #2.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string TdmsLoggingGroupName { get; set; }

#### Remarks

For digital input tasks, NI-DAQmx creates a group for each virtual channel in the task. For each created group, NI-DAQmx appends a hyphen and the virtual channel name to the group name.

If you query this property, NI-DAQmx returns the original value specified without any suffixes appended by NI-DAQmx for digital input tasks or for existing groups.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-tdmsloggingoperation.html language=enus -->
## TOPIC 01508: TdmsLoggingOperation

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-tdmsloggingoperation.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-tdmsloggingoperation.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how to open the TDMS file. SyntaxNamespace: NationalInstruments.DAQmxpublic TdmsLoggingOperation TdmsLoggingOperation { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### TdmsLoggingOperation

Specifies how to open the [TDMS](/csh?context=nidaqmx_mxcncpts_datalogging) file.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [TdmsLoggingOperation](nationalinstruments-daqmx-tdmsloggingoperation.html) TdmsLoggingOperation { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-timeout.html language=enus -->
## TOPIC 01509: Timeout

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-timeout.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-timeout.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the amount of time in milliseconds to wait for reads or writes to complete. SyntaxNamespace: NationalInstruments.DAQmxpublic int Timeout { get; set; }RemarksThe time in milliseconds.If you set this property to -1 (or Infinite), read or write operations never time out.This property appli

### Timeout

Gets or sets the amount of time in milliseconds to wait for reads or writes to complete.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int Timeout { get; set; }

#### Remarks

The time in milliseconds.

If you set this property to -1 (or Infinite), read or write operations never time out.

This property applies to synchronous and asynchronous reads and writes. A write is considered complete when all of the written samples have been transferred to the task buffer. Writes do not wait until the written samples have been generated by the device.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-tostring.html language=enus -->
## TOPIC 01510: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString. ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

#### Remarks

Overrides ToString.

#### Returns

A string representation of the object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-totalsamplesacquiredperchannel.html language=enus -->
## TOPIC 01511: TotalSamplesAcquiredPerChannel

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-totalsamplesacquiredperchannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-totalsamplesacquiredperchannel.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the total number of samples acquired by each channel. NI-DAQmx returns a single value because this value is the same for all channels. For retriggered acquisitions, this value is the cumulative number of samples across all retriggered acquisitions. SyntaxNamespace: NationalInstruments.DAQm

### TotalSamplesAcquiredPerChannel

Indicates the total number of samples acquired by each channel. NI-DAQmx returns a single value because this value is the same for all channels. For retriggered acquisitions, this value is the cumulative number of samples across all retriggered acquisitions.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long TotalSamplesAcquiredPerChannel { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-totalsamplesgeneratedperchannel.html language=enus -->
## TOPIC 01512: TotalSamplesGeneratedPerChannel

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-totalsamplesgeneratedperchannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-totalsamplesgeneratedperchannel.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the total number of samples generated by each channel in the task. This value is identical for all channels in the task. SyntaxNamespace: NationalInstruments.DAQmxpublic long TotalSamplesGeneratedPerChannel { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx

### TotalSamplesGeneratedPerChannel

Indicates the total number of samples generated by each channel in the task. This value is identical for all channels in the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long TotalSamplesGeneratedPerChannel { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-waveformattributemode.html language=enus -->
## TOPIC 01513: WaveformAttributeMode

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-waveformattributemode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-waveformattributemode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the type of information returned from a waveform read. SyntaxNamespace: NationalInstruments.DAQmxpublic WaveformAttributeModes WaveformAttributeMode { get; set; }RemarksThe waveform attribute mode. The default value is a bitwise combination of Timing and ExtendedProperties.This property

### WaveformAttributeMode

Gets or sets the type of information returned from a waveform read.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [WaveformAttributeModes](nationalinstruments-daqmx-waveformattributemodes.html) WaveformAttributeMode { get; set; }

#### Remarks

The waveform attribute mode. The default value is a bitwise combination of [Timing](nationalinstruments-daqmx-waveformattributemodes.html) and [ExtendedProperties](nationalinstruments-daqmx-waveformattributemodes.html).

This property applies to synchronous and asynchronous waveform reads.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-writeexternalovervoltagechannels.html language=enus -->
## TOPIC 01514: WriteExternalOvervoltageChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-writeexternalovervoltagechannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-writeexternalovervoltagechannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any virtual channels in the task for which an External Overvoltage condition has been detected. You must read External OvervoltageChansExist before you read this property. Otherwise, you will receive an error. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] Wri

### WriteExternalOvervoltageChannels

Indicates a list of names of any virtual channels in the task for which an External Overvoltage condition has been detected. You must read External OvervoltageChansExist before you read this property. Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] WriteExternalOvervoltageChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-writeexternalovervoltagechannelsexist.html language=enus -->
## TOPIC 01515: WriteExternalOvervoltageChannelsExist

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-writeexternalovervoltagechannelsexist.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-writeexternalovervoltagechannelsexist.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected an External Overvoltage condition for any channel in the task. Reading this property clears the External Overvoltage status for all channels in the task. You must read this property before you read External OvervoltageChans. Otherwise, you will receive an error. S

### WriteExternalOvervoltageChannelsExist

Indicates if the device(s) detected an External Overvoltage condition for any channel in the task. Reading this property clears the External Overvoltage status for all channels in the task. You must read this property before you read External OvervoltageChans. Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool WriteExternalOvervoltageChannelsExist { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-writeoffset.html language=enus -->
## TOPIC 01516: WriteOffset

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-writeoffset.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-writeoffset.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in samples per channel an offset at which a write operation begins. This offset is relative to the location you specify with WriteRelativeTo. SyntaxNamespace: NationalInstruments.DAQmxpublic int WriteOffset { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-

### WriteOffset

Specifies in samples per channel an offset at which a write operation begins. This offset is relative to the location you specify with [WriteRelativeTo](nationalinstruments-daqmx-daqstream-writerelativeto.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int WriteOffset { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-writeopencurrentloopchannels.html language=enus -->
## TOPIC 01517: WriteOpenCurrentLoopChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-writeopencurrentloopchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-writeopencurrentloopchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any virtual channels in the task for which the device(s) detected an open current loop. You must read WriteOpenCurrentLoopChannelsExist before you read this property. Otherwise, you will receive an error. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] WriteOpe

### WriteOpenCurrentLoopChannels

Indicates a [list of names](/csh?context=nidaqmx_mxcncpts_physchannames) of any virtual channels in the task for which the device(s) detected an [open current loop](/csh?context=nidaqmx_mxdevconsid_opencurrent). You must read [WriteOpenCurrentLoopChannelsExist](nationalinstruments-daqmx-daqstream-writeopencurrentloopchannelsexist.html) before you read this property. Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] WriteOpenCurrentLoopChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-writeopencurrentloopchannelsexist.html language=enus -->
## TOPIC 01518: WriteOpenCurrentLoopChannelsExist

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-writeopencurrentloopchannelsexist.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-writeopencurrentloopchannelsexist.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected an open current loop for any channel in the task. Reading this property clears the open current loop status for all channels in the task. You must read this property before you read WriteOpenCurrentLoopChannels. Otherwise, you will receive an error. SyntaxNamespac

### WriteOpenCurrentLoopChannelsExist

Indicates if the device(s) detected an [open current loop](/csh?context=nidaqmx_mxdevconsid_opencurrent) for any channel in the task. Reading this property clears the open current loop status for all channels in the task. You must read this property before you read [WriteOpenCurrentLoopChannels](nationalinstruments-daqmx-daqstream-writeopencurrentloopchannels.html). Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool WriteOpenCurrentLoopChannelsExist { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-writeovercurrentchannels.html language=enus -->
## TOPIC 01519: WriteOvercurrentChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-writeovercurrentchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-writeovercurrentchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any virtual channels in the task for which an overcurrent condition has been detected. You must read WriteOvercurrentChannelsExist before you read this property. Otherwise, you will receive an error. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] WriteOvercurr

### WriteOvercurrentChannels

Indicates a [list of names](/csh?context=nidaqmx_mxcncpts_physchannames) of any virtual channels in the task for which an [overcurrent condition](/csh?context=nidaqmx_mxdevconsid_overcurrentdet) has been detected. You must read [WriteOvercurrentChannelsExist](nationalinstruments-daqmx-daqstream-writeovercurrentchannelsexist.html) before you read this property. Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] WriteOvercurrentChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-writeovercurrentchannelsexist.html language=enus -->
## TOPIC 01520: WriteOvercurrentChannelsExist

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-writeovercurrentchannelsexist.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-writeovercurrentchannelsexist.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected an overcurrent condition for any channel in the task. Reading this property clears the overcurrent status for all channels in the task. You must read this property before you read WriteOvercurrentChannels. Otherwise, you will receive an error. SyntaxNamespace: Nat

### WriteOvercurrentChannelsExist

Indicates if the device(s) detected an [overcurrent condition](/csh?context=nidaqmx_mxdevconsid_overcurrentdet) for any channel in the task. Reading this property clears the overcurrent status for all channels in the task. You must read this property before you read [WriteOvercurrentChannels](nationalinstruments-daqmx-daqstream-writeovercurrentchannels.html). Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool WriteOvercurrentChannelsExist { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-writeoverloadedchannels.html language=enus -->
## TOPIC 01521: WriteOverloadedChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-writeoverloadedchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-writeoverloadedchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any overloaded virtual channels in the task. You must read WriteOverloadedChannelsExist before you read this property. Otherwise, you will receive an error. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] WriteOverloadedChannels { get; }RemarksThis property ret

### WriteOverloadedChannels

Indicates a list of names of any overloaded virtual channels in the task. You must read [WriteOverloadedChannelsExist](nationalinstruments-daqmx-daqstream-writeoverloadedchannelsexist.html) before you read this property. Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] WriteOverloadedChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-writeoverloadedchannelsexist.html language=enus -->
## TOPIC 01522: WriteOverloadedChannelsExist

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-writeoverloadedchannelsexist.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-writeoverloadedchannelsexist.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected an overload in any virtual channel in the task. Reading this property clears the overload status for all channels in the task. You must read this property before you read WriteOverloadedChannels. Otherwise, you will receive an error. SyntaxNamespace: NationalInstr

### WriteOverloadedChannelsExist

Indicates if the device(s) detected an overload in any virtual channel in the task. Reading this property clears the overload status for all channels in the task. You must read this property before you read [WriteOverloadedChannels](nationalinstruments-daqmx-daqstream-writeoverloadedchannels.html). Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool WriteOverloadedChannelsExist { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-writeovertemperaturechannels.html language=enus -->
## TOPIC 01523: WriteOvertemperatureChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-writeovertemperaturechannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-writeovertemperaturechannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any overtemperature virtual channels. You must read WriteOvertemperatureChannelsExist before you read this property. Otherwise, you will receive an error. The list of names may be empty if the device cannot determine the source of the overtemperature. SyntaxNamespace: Na

### WriteOvertemperatureChannels

Indicates a list of names of any overtemperature virtual channels. You must read [WriteOvertemperatureChannelsExist](nationalinstruments-daqmx-daqstream-writeovertemperaturechannelsexist.html) before you read this property. Otherwise, you will receive an error. The list of names may be empty if the device cannot determine the source of the overtemperature.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] WriteOvertemperatureChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-writeovertemperaturechannelsexist.html language=enus -->
## TOPIC 01524: WriteOvertemperatureChannelsExist

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-writeovertemperaturechannelsexist.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-writeovertemperaturechannelsexist.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected an overtemperature condition in any virtual channel in the task. Reading this property clears the overtemperature status for all channels in the task. You must read this property before you read WriteOvertemperatureChannels. Otherwise, you will receive an error. S

### WriteOvertemperatureChannelsExist

Indicates if the device(s) detected an overtemperature condition in any virtual channel in the task. Reading this property clears the overtemperature status for all channels in the task. You must read this property before you read [WriteOvertemperatureChannels](nationalinstruments-daqmx-daqstream-writeovertemperaturechannels.html). Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool WriteOvertemperatureChannelsExist { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-writepowersupplyfaultchannels.html language=enus -->
## TOPIC 01525: WritePowerSupplyFaultChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-writepowersupplyfaultchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-writepowersupplyfaultchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any virtual channels in the task that have a power supply fault. You must read WritePowerSupplyFaultChannelsExist before you read this property. Otherwise, you will receive an error. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] WritePowerSupplyFaultChannels

### WritePowerSupplyFaultChannels

Indicates a [list of names](/csh?context=nidaqmx_mxcncpts_physchannames) of any virtual channels in the task that have a [power supply fault](/csh?context=nidaqmx_mxdevconsid_pwrsupfault). You must read [WritePowerSupplyFaultChannelsExist](nationalinstruments-daqmx-daqstream-writepowersupplyfaultchannelsexist.html) before you read this property. Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] WritePowerSupplyFaultChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-writepowersupplyfaultchannelsexist.html language=enus -->
## TOPIC 01526: WritePowerSupplyFaultChannelsExist

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-writepowersupplyfaultchannelsexist.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-writepowersupplyfaultchannelsexist.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected a power supply fault for any channel in the task. Reading this property clears the power supply fault status for all channels in the task. You must read this property before you read WritePowerSupplyFaultChannels. Otherwise, you will receive an error. SyntaxNamesp

### WritePowerSupplyFaultChannelsExist

Indicates if the device(s) detected a [power supply fault](/csh?context=nidaqmx_mxdevconsid_pwrsupfault) for any channel in the task. Reading this property clears the power supply fault status for all channels in the task. You must read this property before you read [WritePowerSupplyFaultChannels](nationalinstruments-daqmx-daqstream-writepowersupplyfaultchannels.html). Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool WritePowerSupplyFaultChannelsExist { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-writeraw__bool-byte_arr1.html language=enus -->
## TOPIC 01527: WriteRaw(bool, byte[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-writeraw__bool-byte_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-writeraw__bool-byte_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes raw, unprocessed samples to the channels in the task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteRaw([MarshalAs(UnmanagedType.U1)] bool autoStart, byte[] data)RemarksThe format of the raw samples depends on the device to which you are writing. Consult your device documentation

### WriteRaw(bool, byte[])

Writes [raw](/csh?context=nidaqmx_mxcncpts_rawdata), unprocessed samples to the channels in the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteRaw([MarshalAs(UnmanagedType.U1)] bool autoStart, byte[] data)

#### Remarks

The format of the raw samples depends on the device to which you are writing. Consult your device documentation for more information.

You can use the MemoryStream class to create a byte array from other types.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true, this method automatically calls Start if you do not explicitly call it. |
| data | byte[] | A byte array of raw data to write to the task. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-writerawdatawidth.html language=enus -->
## TOPIC 01528: WriteRawDataWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-writerawdatawidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-writerawdatawidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in bytes the required size of a raw sample to write to the task. SyntaxNamespace: NationalInstruments.DAQmxpublic long WriteRawDataWidth { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### WriteRawDataWidth

Indicates in bytes the required size of a raw sample to write to the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long WriteRawDataWidth { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-writeregenerationmode.html language=enus -->
## TOPIC 01529: WriteRegenerationMode

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-writeregenerationmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-writeregenerationmode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to allow NI-DAQmx to generate the same data multiple times. SyntaxNamespace: NationalInstruments.DAQmxpublic WriteRegenerationMode WriteRegenerationMode { get; set; }RemarksIf you enable regeneration and write new data to the buffer, NI-DAQmx can generate a combination of old and n

### WriteRegenerationMode

Specifies whether to allow NI-DAQmx to generate the same data multiple times.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [WriteRegenerationMode](nationalinstruments-daqmx-writeregenerationmode.html) WriteRegenerationMode { get; set; }

#### Remarks

If you enable regeneration and write new data to the buffer, NI-DAQmx can generate a combination of old and new data, a phenomenon called [glitching](/csh?context=nidaqmx_mxcncpts_glitching).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-writerelativeto.html language=enus -->
## TOPIC 01530: WriteRelativeTo

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-writerelativeto.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-writerelativeto.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the point in the buffer at which to write data. If you also specify an offset with WriteOffset, the write operation begins at that offset relative to this point you select with this property. SyntaxNamespace: NationalInstruments.DAQmxpublic WriteRelativeTo WriteRelativeTo { get; set; }Exce

### WriteRelativeTo

Specifies the point in the buffer at which to write data. If you also specify an offset with [WriteOffset](nationalinstruments-daqmx-daqstream-writeoffset.html), the write operation begins at that offset relative to this point you select with this property.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [WriteRelativeTo](nationalinstruments-daqmx-writerelativeto.html) WriteRelativeTo { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-writesleeptime.html language=enus -->
## TOPIC 01531: WriteSleepTime

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-writesleeptime.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-writesleeptime.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the amount of time to sleep after checking for available buffer space if WriteWaitMode is Sleep. SyntaxNamespace: NationalInstruments.DAQmxpublic double WriteSleepTime { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an err

### WriteSleepTime

Specifies in seconds the amount of time to sleep after checking for available buffer space if [WriteWaitMode](nationalinstruments-daqmx-daqstream-writewaitmode.html) is [Sleep](nationalinstruments-daqmx-writewaitmode.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double WriteSleepTime { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-writesynchronizationunlockedchannels.html language=enus -->
## TOPIC 01532: WriteSynchronizationUnlockedChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-writesynchronizationunlockedchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-writesynchronizationunlockedchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the channels from devices in an unlocked target. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] WriteSynchronizationUnlockedChannels { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each

### WriteSynchronizationUnlockedChannels

Indicates the channels from devices in an unlocked target.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] WriteSynchronizationUnlockedChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-writesynchronizationunlockedchannelsexist.html language=enus -->
## TOPIC 01533: WriteSynchronizationUnlockedChannelsExist

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-writesynchronizationunlockedchannelsexist.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-writesynchronizationunlockedchannelsexist.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the target is currently locked to the grand master. Devices may report PLL Unlock either during acquisition or after acquisition. SyntaxNamespace: NationalInstruments.DAQmxpublic bool WriteSynchronizationUnlockedChannelsExist { get; }ExceptionsTypeDescriptionNationalInstruments.DAQ

### WriteSynchronizationUnlockedChannelsExist

Indicates whether the target is currently locked to the grand master. Devices may report PLL Unlock either during acquisition or after acquisition.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool WriteSynchronizationUnlockedChannelsExist { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-writewaitmode.html language=enus -->
## TOPIC 01534: WriteWaitMode

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-writewaitmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-writewaitmode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how writing to the task waits for space to become available in the buffer. SyntaxNamespace: NationalInstruments.DAQmxpublic WriteWaitMode WriteWaitMode { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### WriteWaitMode

Specifies how writing to the task waits for space to become available in the buffer.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [WriteWaitMode](nationalinstruments-daqmx-writewaitmode.html) WriteWaitMode { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream.html language=enus -->
## TOPIC 01535: DaqStream Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exposes a data stream on a Task that can be used to control reading and writing behavior and can be used in conjunction with reader and writer classes to read or write samples to or from an NI-DAQmx task. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmx

### DaqStream Class

Exposes a data stream on a [Task](nationalinstruments-daqmx-task.html) that can be used to control reading and writing behavior and can be used in conjunction with reader and writer classes to read or write samples to or from an NI-DAQmx task.

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class DaqStream : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| AccessoryInsertionOrRemovalDetected | Indicates if any device(s) in the task detected the insertion or removal of an accessory since the task started. Reading this property clears the accessory change status for all channels in the task. You must read this property before you read DevicesWithInsertedOrRemovedAccessories. Otherwise, you will receive an error. |
| AvailableSamplesPerChannel | Indicates the number of samples available to read per channel. This value is the same for all channels in the task. |
| Buffer | Gets the buffer for the task. |
| ChannelsToRead | Sets a subset of channels in the task from which to read. |
| CommonModeRangeErrorChannels | Indicates a list of names of any virtual channels in the task for which the device(s) detected a common mode range violation. You must read CommonModeRangeErrorChannelsExist before you read this property. Otherwise, you will receive an error. |
| CommonModeRangeErrorChannelsExist | Indicates if the device(s) detected a common mode range violation for any virtual channel in the task. Common mode range violation occurs when the voltage of either the positive terminal or negative terminal to ground are out of range. Reading this property clears the common mode range violation status for all channels in the task. You must read this property before you read CommonModeRangeErrorChannels. Otherwise, you will receive an error. |
| CurrentReadPosition | Indicates in samples per channel the current position in the buffer. |
| CurrentWritePosition | Indicates the position in the buffer of the next sample to generate. This value is identical for all channels in the task. |
| DevicesWithInsertedOrRemovedAccessories | Indicates the names of any devices that detected the insertion or removal of an accessory since the task started. You must read AccessoryInsertionOrRemovalDetected before you read this property. Otherwise, you will receive an error. |
| DigitalLinesPerInputChannel | Indicates the number of lines per channel that NI-DAQmx returns in a sample for line-based reads. If a channel has fewer lines than this number, the extra lines are false. |
| DigitalLinesPerOutputChannel | Indicates the number of Boolean values expected per channel in a sample for line-based writes. This property is determined by the channel in the task with the most digital lines. If a channel has fewer lines than this number, NI-DAQmx ignores the extra Boolean values. |
| LoggingFilePath | Specifies the path to the TDMS file to which you want to log data. If the file path is changed while the task is running, this takes effect on the next sample interval (if Logging.SampsPerFile has been set) or when DAQmx Start New File is called. New file paths can be specified by ending with "\\" or "/". Files created after specifying a new file path retain the same name and numbering sequence. |
| LoggingFilePreallocationSize | Specifies a size in samples to be used to pre-allocate space on disk. Pre-allocation can improve file I/O performance, especially in situations where multiple files are being written to disk. For finite tasks, the default behavior is to pre-allocate the file based on the number of samples you configure the task to acquire. |
| LoggingFileWriteSize | Specifies the size, in samples, in which data will be written to disk. The size must be evenly divisible by the volume sector size, in bytes. |
| LoggingMode | Specifies whether to enable logging and whether to allow reading data while logging. Log mode allows for the best performance. However, you cannot read data while logging if you specify this mode. If you want to read data while logging, specify Log and Read mode. |
| LoggingPause | Specifies whether logging is paused while a task is executing. If LoggingMode is set to Log and Read mode, this value is taken into consideration on the next call to DAQmx Read, where data is written to disk. If LoggingMode is set to Log Only mode, this value is taken into consideration the next time that data is written to disk. A new TDMS group is written when logging is resumed from a paused state. |
| LoggingSamplesPerFile | Specifies how many samples to write to each file. When the file reaches the number of samples specified, a new file is created with the naming convention of <filename>_####.tdms, where #### starts at 0001 and increments automatically with each new file. For example, if the file specified is C:\\data.tdms, the next file name used is C:\\data_0001.tdms. To disable file spanning behavior, set this attribute to 0. If LoggingFilePath is changed while this attribute is set, the new file path takes effect on the next file created. |
| NumberOfInputChannels | Indicates the number of channels that reading from the task reads from the task. This value is the number of channels in the task or the number of channels you specify with ChannelsToRead. |
| NumberOfOutputChannels | Indicates the number of channels that writing to the task writes to the task. This value is the number of channels in the task. |
| OpenThermocoupleChannels | Indicates a list of names of any virtual channels in the task for which the device(s) detected an open thermcouple. You must read OpenThermocoupleChannelsExist before you read this property. Otherwise, you will receive an error. |
| OpenThermocoupleChannelsExist | Indicates if the device(s) detected an open thermocouple connected to any virtual channel in the task. Reading this property clears the open thermocouple status for all channels in the task. You must read this property before you read OpenThermocoupleChannels. Otherwise, you will receive an error. |
| OutputBufferSpaceAvailable | Indicates in samples per channel the amount of available space in the buffer. |
| OverloadedInputChannels | Indicates a list of names of any overloaded virtual channels in the task. You must read OverloadedInputChannelsExist before you read this property. Otherwise, you will receive an error. |
| OverloadedInputChannelsExist | Indicates if the device(s) detected an overload in any virtual channel in the task. Reading this property clears the overload status for all channels in the task. You must read this property before you read OverloadedInputChannels. Otherwise, you will receive an error. |
| PhaseLockedLoopUnlockedChannels | Indicates the channels that had their PLLs unlock. |
| PhaseLockedLoopUnlockedChannelsExist | Indicates whether the PLL is currently locked, or whether it became unlocked during the previous acquisition. Devices may report PLL Unlock either during acquisition or after acquisition. |
| ReadAllAvailableSamples | Specifies whether subsequent read operations read all samples currently available in the buffer or wait for the buffer to become full before reading. NI-DAQmx uses this setting for finite acquisitions and only when the number of samples to read is -1. For continuous acquisitions when the number of samples to read is -1, a read operation always reads all samples currently available in the buffer. |
| ReadAutoStart | Specifies if reading from the task automatically starts the task if you did not start the task explicitly by using starting the task. The default value is true. When reading from the task starts a finite acquisition task, it also stops the task after reading the last sample. |
| ReadAuxPowerErrorChannels | Indicates a list of names of any virtual channels in the task for which an auxiliary power supply error condition has been detected. You must read the Aux Power Error Channels Exist property before you read this property. Otherwise, you will receive an error. |
| ReadAuxPowerErrorChannelsExist | Indicates if the device(s) detected an auxiliary power supply error condition for any channel in the task. Reading this property clears the error condition status for all channels in the task. You must read this property before you read the Aux Power Error Channels property. Otherwise, you will receive an error. |
| ReadExcitationFaultChannels | Indicates a list of names of any virtual channels in the task for which the device(s) detected an excitation fault condition. You must read ReadExcitationFaultChannelsExist before you read this property. Otherwise, you will receive an error. |
| ReadExcitationFaultChannelsExist | Indicates if the device(s) detected an excitation fault condition for any virtual channel in the task. Reading this property clears the excitation fault status for all channels in the task. You must read this property before you read ReadExcitationFaultChannels. Otherwise, you will receive an error. |
| ReadInputLimitsFaultChannels | Indicates the virtual channels that have detected samples outside the upper or lower limits configured for each channel in the task. You must read ReadInputLimitsFaultChannelsExist before you read this property. Otherwise, you will receive an error. |
| ReadInputLimitsFaultChannelsExist | Indicates if the device or devices detected a sample that was outside the upper or lower limits configured for each channel in the task. Reading this property clears the input limits fault channel status for all channels in the task. You must read this property before you read ReadInputLimitsFaultChannels. Otherwise, you will receive an error. Note: Fault detection applies to both positive and negative inputs. For instance, if you specify a lower limit of 2 mA and an upper limit of 12 mA, NI-DAQmx detects a fault at 15 mA and -15 mA, but not at -6 mA because it is in the range of -12 mA to -2 mA. |
| ReadOffset | Specifies an offset in samples per channel at which to begin a read operation. This offset is relative to the location you specify with ReadRelativeTo. |
| ReadOpenCurrentLoopChannels | Indicates a list of names of any virtual channels in the task for which the device(s) detected an open current loop. You must read ReadOpenCurrentLoopChannelsExist before you read this property. Otherwise, you will receive an error. |
| ReadOpenCurrentLoopChannelsExist | Indicates if the device(s) detected an open current loop for any virtual channel in the task. Reading this property clears the open current loop status for all channels in the task. You must read this property before you read ReadOpenCurrentLoopChannels. Otherwise, you will receive an error. |
| ReadOvercurrentChannels | Indicates a list of names of any virtual channels in the task for which the device(s) detected an overcurrent condition. You must read ReadOvercurrentChannelsExist before you read this property. Otherwise, you will receive an error. On some devices, you must restart the task for all overcurrent channels to recover. |
| ReadOvercurrentChannelsExist | Indicates if the device(s) detected an overcurrent condition for any virtual channel in the task. Reading this property clears the overcurrent status for all channels in the task. You must read this property before you read ReadOvercurrentChannels. Otherwise, you will receive an error. |
| ReadOvertemperatureChannels | Indicates a list of names of any overtemperature virtual channels. You must read ReadOvertemperatureChannelsExist before you read this property. Otherwise, you will receive an error. |
| ReadOvertemperatureChannelsExist | Indicates if the device(s) detected an overtemperature condition in any virtual channel in the task. Reading this property clears the overtemperature status for all channels in the task. You must read this property before you read ReadOvertemperatureChannels. Otherwise, you will receive an error. |
| ReadOverwriteMode | Specifies whether to overwrite samples in the buffer that you have not yet read. |
| ReadPowerSupplyFaultChannels | Indicates the virtual channels that have detected a power supply fault. You must read WritePowerSupplyFaultChannelsExist before you read this property. Otherwise, you will receive an error. |
| ReadPowerSupplyFaultChannelsExist | Indicates if the device or devices detected a power supply fault condition in any virtual channel in the task. Reading this property clears the power supply fault status for all channels in this task. You must read this property before you read ReadPowerSupplyFaultChannels. Otherwise, you will receive an error. |
| ReadRawDataWidth | Indicates in bytes the size of a raw sample from the task. |
| ReadRelativeTo | Specifies the point in the buffer at which to begin a read operation. If you also specify an offset with ReadOffset, the read operation begins at that offset relative to the point you select with this property. The default value is CurrentReadPosition unless you configure a Reference Trigger for the task. If you configure a Reference Trigger, the default value is FirstPretriggerSample. |
| ReadRemoteSenseErrorChannels | Indicates a list of names of any virtual channels in the task for which a remote sense connection error condition has been detected. You must read Remote Sense Error Channels Exist before you read this property. Otherwise, you will receive an error. |
| ReadRemoteSenseErrorChannelsExist | Indicates if the device(s) detected an error condition of the remote sense connection for any channel in the task. You must disable the output and resolve the hardware connection issue to clear the error condition. You must read this property before you read the Remote Sense Error Channels property. Otherwise, you will receive an error. |
| ReadReverseVoltageErrorChannels | Indicates a list of names of all virtual channels in the task for which reverse voltage error condition has been detected. You must read the Reverse Voltage Error Channels Exist property before you read this property. Otherwise, you will receive an error. |
| ReadReverseVoltageErrorChannelsExist | Indicates if the device(s) detected reverse voltage error for any of the channels in the task. Reverse voltage error occurs if the local voltage is equal to the negative saturated voltage. Reading this property clears the error condition status for all channels in the task. You must read this property before you read the Reverse Voltage Error Channels property. Otherwise, you will receive an error. |
| ReadSleepTime | Specifies in seconds the amount of time to sleep after checking for available samples if ReadWaitMode is Sleep. |
| ReadSynchronizationUnlockedChannels | Indicates the channels from devices in an unlocked target. |
| ReadSynchronizationUnlockedChannelsExist | Indicates whether the target is currently locked to the grand master. Devices may report PLL Unlock either during acquisition or after acquisition. |
| ReadWaitMode | Specifies how reading from the task waits for samples to become available. |
| TdmsLoggingGroupName | Specifies the name of the group to create within the TDMS file for data from this task. If you append data to an existing file and the specified group already exists, NI-DAQmx appends a number symbol and a number to the group name, incrementing that number until finding a group name that does not exist. For example, if you specify a group name of Voltage Task, and that group already exists, NI-DAQmx assigns the group name Voltage Task #1, then Voltage Task #2. |
| TdmsLoggingOperation | Specifies how to open the TDMS file. |
| Timeout | Gets or sets the amount of time in milliseconds to wait for reads or writes to complete. |
| TotalSamplesAcquiredPerChannel | Indicates the total number of samples acquired by each channel. NI-DAQmx returns a single value because this value is the same for all channels. For retriggered acquisitions, this value is the cumulative number of samples across all retriggered acquisitions. |
| TotalSamplesGeneratedPerChannel | Indicates the total number of samples generated by each channel in the task. This value is identical for all channels in the task. |
| WaveformAttributeMode | Gets or sets the type of information returned from a waveform read. |
| WriteExternalOvervoltageChannels | Indicates a list of names of any virtual channels in the task for which an External Overvoltage condition has been detected. You must read External OvervoltageChansExist before you read this property. Otherwise, you will receive an error. |
| WriteExternalOvervoltageChannelsExist | Indicates if the device(s) detected an External Overvoltage condition for any channel in the task. Reading this property clears the External Overvoltage status for all channels in the task. You must read this property before you read External OvervoltageChans. Otherwise, you will receive an error. |
| WriteOffset | Specifies in samples per channel an offset at which a write operation begins. This offset is relative to the location you specify with WriteRelativeTo. |
| WriteOpenCurrentLoopChannels | Indicates a list of names of any virtual channels in the task for which the device(s) detected an open current loop. You must read WriteOpenCurrentLoopChannelsExist before you read this property. Otherwise, you will receive an error. |
| WriteOpenCurrentLoopChannelsExist | Indicates if the device(s) detected an open current loop for any channel in the task. Reading this property clears the open current loop status for all channels in the task. You must read this property before you read WriteOpenCurrentLoopChannels. Otherwise, you will receive an error. |
| WriteOvercurrentChannels | Indicates a list of names of any virtual channels in the task for which an overcurrent condition has been detected. You must read WriteOvercurrentChannelsExist before you read this property. Otherwise, you will receive an error. |
| WriteOvercurrentChannelsExist | Indicates if the device(s) detected an overcurrent condition for any channel in the task. Reading this property clears the overcurrent status for all channels in the task. You must read this property before you read WriteOvercurrentChannels. Otherwise, you will receive an error. |
| WriteOverloadedChannels | Indicates a list of names of any overloaded virtual channels in the task. You must read WriteOverloadedChannelsExist before you read this property. Otherwise, you will receive an error. |
| WriteOverloadedChannelsExist | Indicates if the device(s) detected an overload in any virtual channel in the task. Reading this property clears the overload status for all channels in the task. You must read this property before you read WriteOverloadedChannels. Otherwise, you will receive an error. |
| WriteOvertemperatureChannels | Indicates a list of names of any overtemperature virtual channels. You must read WriteOvertemperatureChannelsExist before you read this property. Otherwise, you will receive an error. The list of names may be empty if the device cannot determine the source of the overtemperature. |
| WriteOvertemperatureChannelsExist | Indicates if the device(s) detected an overtemperature condition in any virtual channel in the task. Reading this property clears the overtemperature status for all channels in the task. You must read this property before you read WriteOvertemperatureChannels. Otherwise, you will receive an error. |
| WritePowerSupplyFaultChannels | Indicates a list of names of any virtual channels in the task that have a power supply fault. You must read WritePowerSupplyFaultChannelsExist before you read this property. Otherwise, you will receive an error. |
| WritePowerSupplyFaultChannelsExist | Indicates if the device(s) detected a power supply fault for any channel in the task. Reading this property clears the power supply fault status for all channels in the task. You must read this property before you read WritePowerSupplyFaultChannels. Otherwise, you will receive an error. |
| WriteRawDataWidth | Indicates in bytes the required size of a raw sample to write to the task. |
| WriteRegenerationMode | Specifies whether to allow NI-DAQmx to generate the same data multiple times. |
| WriteRelativeTo | Specifies the point in the buffer at which to write data. If you also specify an offset with WriteOffset, the write operation begins at that offset relative to this point you select with this property. |
| WriteSleepTime | Specifies in seconds the amount of time to sleep after checking for available buffer space if WriteWaitMode is Sleep. |
| WriteSynchronizationUnlockedChannels | Indicates the channels from devices in an unlocked target. |
| WriteSynchronizationUnlockedChannelsExist | Indicates whether the target is currently locked to the grand master. Devices may report PLL Unlock either during acquisition or after acquisition. |
| WriteWaitMode | Specifies how writing to the task waits for space to become available in the buffer. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureInputBuffer(long) | Overrides the automatic input buffer allocation that NI-DAQmx performs. |
| ConfigureOutputBuffer(long) | Overrides the automatic output buffer allocation that NI-DAQmx performs. |
| ReadRaw(int) | Reads raw, unprocessed samples from the channels in the task. |
| ToString() | Returns a string representation of the object. |
| WriteRaw(bool, byte[]) | Writes raw, unprocessed samples to the channels in the task. |

#### See Also

- Task
- Stream
- AnalogSingleChannelReader
- AnalogMultiChannelReader
- AnalogUnscaledReader
- CounterSingleChannelReader
- CounterMultiChannelReader
- DigitalSingleChannelReader
- DigitalMultiChannelReader
- AnalogSingleChannelWriter
- AnalogMultiChannelWriter
- AnalogUnscaledWriter
- DigitalSingleChannelWriter
- DigitalMultiChannelWriter

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-addcdaqsynchronizationconnection__string.html language=enus -->
## TOPIC 01536: AddCDaqSynchronizationConnection(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-addcdaqsynchronizationconnection__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-addcdaqsynchronizationconnection__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a cDAQ Sync connection between devices. The connection is not verified. SyntaxNamespace: NationalInstruments.DAQmxpublic void AddCDaqSynchronizationConnection(string portList)ParametersNameTypeDescriptionportListstringSpecifies the cDAQ Sync ports to connect.ExceptionsTypeDescriptionNationalIns

### AddCDaqSynchronizationConnection(string)

Adds a cDAQ Sync connection between devices. The connection is not verified.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void AddCDaqSynchronizationConnection(string portList)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| portList | string | Specifies the cDAQ Sync ports to connect. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-addnetworkdevice__string-string-bool-double.html language=enus -->
## TOPIC 01537: AddNetworkDevice(string, string, bool, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-addnetworkdevice__string-string-bool-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-addnetworkdevice__string-string-bool-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a Network cDAQ device to the system and, if specified, attempts to reserve it. SyntaxNamespace: NationalInstruments.DAQmxpublic Device AddNetworkDevice(string ipAddress, string deviceName, [MarshalAs(UnmanagedType.U1)] bool attemptReservation, double timeout)RemarksMAX automatically attempts to

### AddNetworkDevice(string, string, bool, double)

Adds a Network cDAQ device to the system and, if specified, attempts to reserve it.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [Device](nationalinstruments-daqmx-device.html) AddNetworkDevice(string ipAddress, string deviceName, [MarshalAs(UnmanagedType.U1)] bool attemptReservation, double timeout)

#### Remarks

MAX automatically attempts to reserve a device when the device is added, but this method does not, unless *attemptReservation*  is set to true.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| ipAddress | string | Specifies the string containing the IP address (in dotted decimal notation) of the device to add to the system. |
| deviceName | string | The name to assign to the device. If unspecified, NI-DAQmx chooses the device name. |
| attemptReservation | bool | Specifies whether a reservation should be attempted after the device is successfully added. |
| timeout | double | Specifies the time in seconds to wait for the device to respond before timing out. |

#### Returns

The device object the operation applied to.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-addnetworkdevice__string-string-double.html language=enus -->
## TOPIC 01538: AddNetworkDevice(string, string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-addnetworkdevice__string-string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-addnetworkdevice__string-string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a Network cDAQ device to the system. This method does not attempt to reserve the device after the device is successfully added. SyntaxNamespace: NationalInstruments.DAQmxpublic Device AddNetworkDevice(string ipAddress, string deviceName, double timeout)RemarksMAX automatically attempts to reser

### AddNetworkDevice(string, string, double)

Adds a Network cDAQ device to the system. This method does not attempt to reserve the device after the device is successfully added.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [Device](nationalinstruments-daqmx-device.html) AddNetworkDevice(string ipAddress, string deviceName, double timeout)

#### Remarks

MAX automatically attempts to reserve a device when the device is added, but this method does not.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| ipAddress | string | Specifies the string containing the IP address (in dotted decimal notation) of the device to add to the system. |
| deviceName | string | The name to assign to the device. If unspecified, NI-DAQmx chooses the device name. |
| timeout | double | Specifies the time in seconds to wait for the device to respond before timing out. |

#### Returns

The device object the operation applied to.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-autoconfigurecdaqsynchronizationconnections__string-double.html language=enus -->
## TOPIC 01539: AutoConfigureCDaqSynchronizationConnections(string, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-autoconfigurecdaqsynchronizationconnections__string-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-autoconfigurecdaqsynchronizationconnections__string-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Detects and configures cDAQ Sync connections between devices. SyntaxNamespace: NationalInstruments.DAQmxpublic string AutoConfigureCDaqSynchronizationConnections(string deviceRequested, double timeout)RemarksStop all NI-DAQmx tasks running on the devices prior to calling this method because any runn

### AutoConfigureCDaqSynchronizationConnections(string, double)

Detects and configures cDAQ Sync connections between devices.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string AutoConfigureCDaqSynchronizationConnections(string deviceRequested, double timeout)

#### Remarks

Note

Auto-configure toggles lines on ports during configuration. Upon completion, all previous configurations are deleted.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deviceRequested | string | The names of the CompactDAQ chassis, C Series modules, or cDAQ Sync ports in comma separated form to search. If no names are specified, all cDAQ Sync ports on connected, non-simulated devices are scanned. |
| timeout | double | The time in seconds to wait for the device to respond before timing out. If a timeout occurs, no configuration is changed. |

#### Returns

The configured port-to-port connections.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-clearlastdaqwarning.html language=enus -->
## TOPIC 01540: ClearLastDaqWarning()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-clearlastdaqwarning.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-clearlastdaqwarning.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the value of the LastDaqWarning property, by setting the error code to zero and the error string to a blank string. SyntaxNamespace: NationalInstruments.DAQmxpublic void ClearLastDaqWarning()RemarksThis method clears information only about warnings that occur in the thread from which the meth

### ClearLastDaqWarning()

Clears the value of the [LastDaqWarning](nationalinstruments-daqmx-daqsystem-lastdaqwarning.html) property, by setting the error code to zero and the error string to a blank string.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ClearLastDaqWarning()

#### Remarks

This method clears information only about warnings that occur in the thread from which the method is called. This behavior distinguishes warnings that are caused by actions in one thread from warnings that are caused by independent actions that occur at the same time in another thread.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-closeswitchrelays__string-bool.html language=enus -->
## TOPIC 01541: CloseSwitchRelays(string, bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-closeswitchrelays__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-closeswitchrelays__string-bool.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This method is obsolete. Will warn if used Closes the specified relays. SyntaxNamespace: NationalInstruments.DAQmxpublic void CloseSwitchRelays(string relays, [MarshalAs(UnmanagedType.U1)] bool waitForSettling)RemarksWhen you operate relays directly, you circumvent the protection that chan

### CloseSwitchRelays(string, bool)

**Obsolete: This method is obsolete. Will warn if used** 
Closes the specified relays.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void CloseSwitchRelays(string relays, [MarshalAs(UnmanagedType.U1)] bool waitForSettling)

#### Remarks

When you operate relays directly, you circumvent the protection that channel usage types offer. Avoid using this method when you use the [ConnectSwitchChannels(string, bool)](nationalinstruments-daqmx-daqsystem-connectswitchchannels__string-bool.html) or [DisconnectSwitchChannels(string, bool)](nationalinstruments-daqmx-daqsystem-disconnectswitchchannels__string-bool.html) methods because this method does not pass the changes that you make to those methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| relays | string | A set of relays to close. You can specify a string that contains a comma-delimited list of relays. |
| waitForSettling | bool | If true, this method waits for the switches to settle before returning. If false, the method returns immediately after the operation. This settling time is controlled through the SettlingTime property. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-connectswitchchannels__string-bool.html language=enus -->
## TOPIC 01542: ConnectSwitchChannels(string, bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-connectswitchchannels__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-connectswitchchannels__string-bool.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This method is obsolete. Will warn if used Makes one or more connections between switch channels as specified by the connection list. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConnectSwitchChannels(string connectionList, [MarshalAs(UnmanagedType.U1)] bool waitForSettling)Remark

### ConnectSwitchChannels(string, bool)

**Obsolete: This method is obsolete. Will warn if used** 
Makes one or more connections between switch channels as specified by the connection list.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConnectSwitchChannels(string connectionList, [MarshalAs(UnmanagedType.U1)] bool waitForSettling)

#### Remarks

You can specify only the two endpoints, or you can specify the explicit path between two endpoints. This method can make connections on multiple devices, but each individual connection must reside on a single device. In the event of an error, connecting stops at the point in the list where the error occurred.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| connectionList | string | A list of connections to make between switch channels. This list uses a special syntax. |
| waitForSettling | bool | If true, this method waits for the switches to settle before returning. If false, the method returns immediately after the operation. This settling time is controlled through the SettlingTime property. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-connectswitchchannels__string-string-bool.html language=enus -->
## TOPIC 01543: ConnectSwitchChannels(string, string, bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-connectswitchchannels__string-string-bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-connectswitchchannels__string-string-bool.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This method is obsolete. Will warn if used Makes a connection between two switch channels. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConnectSwitchChannels(string switchChannel1, string switchChannel2, [MarshalAs(UnmanagedType.U1)] bool waitForSettling)ParametersNameTypeDescript

### ConnectSwitchChannels(string, string, bool)

**Obsolete: This method is obsolete. Will warn if used** 
Makes a connection between two switch channels.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConnectSwitchChannels(string switchChannel1, string switchChannel2, [MarshalAs(UnmanagedType.U1)] bool waitForSettling)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| switchChannel1 | string | The first channel to connect. |
| switchChannel2 | string | The second channel to connect. |
| waitForSettling | bool | If true, this method waits for the switches to settle before returning. If false, the method returns immediately after the operation. This settling time is controlled through the SettlingTime property. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-connectterminals__string-string-signalroutingmodifiers.html language=enus -->
## TOPIC 01544: ConnectTerminals(string, string, SignalRoutingModifiers)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-connectterminals__string-string-signalroutingmodifiers.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-connectterminals__string-string-signalroutingmodifiers.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a route between a source and destination terminal with the specified signal modification. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConnectTerminals(string sourceTerminal, string destinationTerminal, SignalRoutingModifiers signalModifiers)RemarksThe route can carry a variety of d

### ConnectTerminals(string, string, SignalRoutingModifiers)

Creates a route between a source and destination [terminal](/csh?context=nidaqmx_mxcncpts_terminal) with the specified signal modification.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConnectTerminals(string sourceTerminal, string destinationTerminal, SignalRoutingModifiers signalModifiers)

#### Remarks

The route can carry a variety of digital signals such as triggers, clocks, and hardware events. These source and destination terminals can be on different devices, as long as a connecting public bus, such as RTSI or the PXI backplane, is available. This method does not modify a task. When the method is called, the route is immediately reserved and committed to hardware. This type of routing is called [immediate routing](/csh?context=nidaqmx_mxcncpts_immediaterouting).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sourceTerminal | string | The originating terminal of the route. |
| destinationTerminal | string | The receiving terminal of the route. |
| signalModifiers | SignalRoutingModifiers | Specifies if the signal routed from the source terminal to the destination terminal is inverted. If the device is not capable of signal inversion or if a previous route reserved the inversion circuitry in an incompatible configuration, attempting to invert the signal causes an error. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-connectterminals__string-string.html language=enus -->
## TOPIC 01545: ConnectTerminals(string, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-connectterminals__string-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-connectterminals__string-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a route between a source and destination terminal. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConnectTerminals(string sourceTerminal, string destinationTerminal)RemarksThe route can carry a variety of digital signals such as triggers, clocks, and hardware events. These source and

### ConnectTerminals(string, string)

Creates a route between a source and destination [terminal](/csh?context=nidaqmx_mxcncpts_terminal).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConnectTerminals(string sourceTerminal, string destinationTerminal)

#### Remarks

The route can carry a variety of digital signals such as triggers, clocks, and hardware events. These source and destination terminals can be on different devices, as long as a connecting public bus, such as RTSI or the PXI backplane, is available. This method does not modify a task. When the method is called, the route is immediately reserved and committed to hardware. This type of routing is called [immediate routing](/csh?context=nidaqmx_mxcncpts_immediaterouting).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sourceTerminal | string | The originating terminal of the route. |
| destinationTerminal | string | The receiving terminal of the route. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-createswitchscantask__string-string.html language=enus -->
## TOPIC 01546: CreateSwitchScanTask(string, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-createswitchscantask__string-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-createswitchscantask__string-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This method is obsolete. Will warn if used Creates a new switch scanning task with the sequence specified in the scan list. SyntaxNamespace: NationalInstruments.DAQmxpublic unsafe Task CreateSwitchScanTask(string taskName, string scanList)RemarksThe NI-DAQmx driver does not determine if th

### CreateSwitchScanTask(string, string)

**Obsolete: This method is obsolete. Will warn if used** 
Creates a new switch scanning task with the sequence specified in the scan list.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public unsafe [Task](nationalinstruments-daqmx-task.html) CreateSwitchScanTask(string taskName, string scanList)

#### Remarks

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateSwitchScanTask(string, string) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| taskName | string | The name of the task to create. If you specify Empty or null, the NI-DAQmx driver assigns a unique name to the new task. |
| scanList | string | The sequence of connections and disconnections for the task. This sequence is specified using a special syntax. |

#### Returns

The [Task](nationalinstruments-daqmx-task.html) that this method creates.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-createwatchdogtimertask__string-string-double-string_arr1-watchdogdoexpirationstate_arr1.html language=enus -->
## TOPIC 01547: CreateWatchdogTimerTask(string, string, double, string[], WatchdogDOExpirationState[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-createwatchdogtimertask__string-string-double-string_arr1-watchdogdoexpirationstate_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-createwatchdogtimertask__string-string-double-string_arr1-watchdogdoexpirationstate_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a task to configure and control the watchdog timer of a static DIO device. The timer activates when you start the task. SyntaxNamespace: NationalInstruments.DAQmxpublic unsafe Task CreateWatchdogTimerTask(string taskName, string device, double timeout, string[] physicalChannels, WatchdogDOEx

### CreateWatchdogTimerTask(string, string, double, string[], WatchdogDOExpirationState[])

Creates a task to configure and control the [watchdog timer](/csh?context=nidaqmx_mxdevconsid_watchdogtimers) of a static DIO device. The timer activates when you start the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public unsafe [Task](nationalinstruments-daqmx-task.html) CreateWatchdogTimerTask(string taskName, string device, double timeout, string[] physicalChannels, WatchdogDOExpirationState[] expirationStates)

#### Remarks

Use the properties and methods on [Task](nationalinstruments-daqmx-task.html) and [Watchdog](nationalinstruments-daqmx-task-watchdog.html) to configure and control the watchdog timer task.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| taskName | string | The name of the task to create. If you specify Empty or null, the NI-DAQmx driver assigns a unique name to the new task. |
| device | string | The name of the device for which to create a watchdog timer task. |
| timeout | double | The amount of time in seconds until the watchdog timer expires. A value of -1 means the internal timer never expires. Set timeout to -1 if you use an Expiration Trigger to expire the watchdog task. |
| physicalChannels | string[] | The physical channel names for which to define watchdog expiration states. Each value in this vector specifies a physical channel string that is assigned the expiration state at the corresponding position in the expirationStates parameter. You cannot modify the expiration state of dedicated digital input physical channels. |
| expirationStates | WatchdogDOExpirationState[] | The state to which to set the digital physical channel when the watchdog timer expires. |

#### Returns

The [Task](nationalinstruments-daqmx-task.html) that this method creates.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-daqwarning.html language=enus -->
## TOPIC 01548: DaqWarning

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-daqwarning.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-daqwarning.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Occurs when the NI-DAQmx driver issues a warning. SyntaxNamespace: NationalInstruments.DAQmxpublic DaqWarningEventHandler DaqWarning

### DaqWarning

Occurs when the NI-DAQmx driver issues a warning.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DaqWarningEventHandler](nationalinstruments-daqmx-daqwarningeventhandler__object-daqwarningeventargs.html) DaqWarning

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-deleteglobalchannel__string.html language=enus -->
## TOPIC 01549: DeleteGlobalChannel(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-deleteglobalchannel__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-deleteglobalchannel__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes the specified global channel that is stored in Measurement & Automation Explorer (MAX). SyntaxNamespace: NationalInstruments.DAQmxpublic void DeleteGlobalChannel(string persistedName)RemarksThis method does not remove the global channel from tasks that use it. ParametersNameTypeDescriptionpe

### DeleteGlobalChannel(string)

Deletes the specified [global channel](/csh?context=nidaqmx_mxcncpts_chans)that is stored in Measurement & Automation Explorer (MAX).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void DeleteGlobalChannel(string persistedName)

#### Remarks

This method does not remove the global channel from [tasks](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that use it.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| persistedName | string | The name of the global channel to delete. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-deletescale__string.html language=enus -->
## TOPIC 01550: DeleteScale(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-deletescale__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-deletescale__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes the specified custom scale that is stored in Measurement & Automation Explorer (MAX). SyntaxNamespace: NationalInstruments.DAQmxpublic void DeleteScale(string persistedName)RemarksThis method does not remove the custom scale from virtual channels that use it. ParametersNameTypeDescriptionper

### DeleteScale(string)

Deletes the specified [custom scale](/csh?context=nidaqmx_mxcncpts_customscales) that is stored in Measurement & Automation Explorer (MAX).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void DeleteScale(string persistedName)

#### Remarks

This method does not remove the custom scale from [virtual channels](/csh?context=nidaqmx_mxcncpts_chans) that use it.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| persistedName | string | The name of the scale to delete. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-deletetask__string.html language=enus -->
## TOPIC 01551: DeleteTask(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-deletetask__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-deletetask__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes the specified task that is stored in Measurement & Automation Explorer (MAX). SyntaxNamespace: NationalInstruments.DAQmxpublic void DeleteTask(string persistedName)RemarksThis method does not clear the copy of the task stored in memory. ParametersNameTypeDescriptionpersistedNamestringThe nam

### DeleteTask(string)

Deletes the specified [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) that is stored in Measurement & Automation Explorer (MAX).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void DeleteTask(string persistedName)

#### Remarks

This method does not clear the copy of the task stored in memory.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| persistedName | string | The name of the task to delete. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-devices.html language=enus -->
## TOPIC 01552: Devices

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-devices.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-devices.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the names of all devices installed in the system. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] Devices { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid

### Devices

Indicates the names of all devices installed in the system.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] Devices { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-disconnectall__string-bool.html language=enus -->
## TOPIC 01553: DisconnectAll(string, bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-disconnectall__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-disconnectall__string-bool.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This method is obsolete. Will warn if used Terminates all active connections on the device, which places the relays into the topology reset state. SyntaxNamespace: NationalInstruments.DAQmxpublic void DisconnectAll(string switchDevice, [MarshalAs(UnmanagedType.U1)] bool waitForSettling)Rem

### DisconnectAll(string, bool)

**Obsolete: This method is obsolete. Will warn if used** 
Terminates all active connections on the device, which places the relays into the topology reset state.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void DisconnectAll(string switchDevice, [MarshalAs(UnmanagedType.U1)] bool waitForSettling)

#### Remarks

You can use this method to terminate connections made by [ConnectSwitchChannels(string, bool)](nationalinstruments-daqmx-daqsystem-connectswitchchannels__string-bool.html), [OpenSwitchRelays(string, bool)](nationalinstruments-daqmx-daqsystem-openswitchrelays__string-bool.html), or [CloseSwitchRelays(string, bool)](nationalinstruments-daqmx-daqsystem-closeswitchrelays__string-bool.html). This method does not alter the settling time or channel usage settings. To reset those settings, use [Reset](nationalinstruments-daqmx-device-reset.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| switchDevice | string | The switch device on which connections are to be terminated. |
| waitForSettling | bool | If true, this method waits for the switches to settle before returning. If false, the method returns immediately after the operation. This settling time is controlled through the SettlingTime property. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-disconnectswitchchannels__string-bool.html language=enus -->
## TOPIC 01554: DisconnectSwitchChannels(string, bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-disconnectswitchchannels__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-disconnectswitchchannels__string-bool.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This method is obsolete. Will warn if used Terminates one or more connections between switch channels as specified by the disconnection list. SyntaxNamespace: NationalInstruments.DAQmxpublic void DisconnectSwitchChannels(string disconnectionList, [MarshalAs(UnmanagedType.U1)] bool waitForS

### DisconnectSwitchChannels(string, bool)

**Obsolete: This method is obsolete. Will warn if used** 
Terminates one or more connections between switch channels as specified by the disconnection list.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void DisconnectSwitchChannels(string disconnectionList, [MarshalAs(UnmanagedType.U1)] bool waitForSettling)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| disconnectionList | string | A list of switch connections to terminate. This list uses a special syntax. |
| waitForSettling | bool | If true, this method waits for the switches to settle before returning. If false, the method returns immediately after the operation. This settling time is controlled through the SettlingTime property. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-disconnectswitchchannels__string-string-bool.html language=enus -->
## TOPIC 01555: DisconnectSwitchChannels(string, string, bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-disconnectswitchchannels__string-string-bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-disconnectswitchchannels__string-string-bool.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This method is obsolete. Will warn if used Terminates a connection between two channels. SyntaxNamespace: NationalInstruments.DAQmxpublic void DisconnectSwitchChannels(string switchChannel1, string switchChannel2, [MarshalAs(UnmanagedType.U1)] bool waitForSettling)ParametersNameTypeDescrip

### DisconnectSwitchChannels(string, string, bool)

**Obsolete: This method is obsolete. Will warn if used** 
Terminates a connection between two channels.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void DisconnectSwitchChannels(string switchChannel1, string switchChannel2, [MarshalAs(UnmanagedType.U1)] bool waitForSettling)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| switchChannel1 | string | The first channel in the connection. |
| switchChannel2 | string | The second channel in the connection. |
| waitForSettling | bool | If true, this method waits for the switches to settle before returning. If false, the method returns immediately after the operation. This settling time is controlled through the SettlingTime property. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-disconnectterminals__string-string.html language=enus -->
## TOPIC 01556: DisconnectTerminals(string, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-disconnectterminals__string-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-disconnectterminals__string-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes signal routes you created by using ConnectTerminals(string, string, SignalRoutingModifiers). SyntaxNamespace: NationalInstruments.DAQmxpublic void DisconnectTerminals(string sourceTerminal, string destinationTerminal)RemarksThis method cannot remove task-based routes, such as those you creat

### DisconnectTerminals(string, string)

Removes signal routes you created by using [ConnectTerminals(string, string, SignalRoutingModifiers)](nationalinstruments-daqmx-daqsystem-connectterminals__string-string-signalroutingmodifiers.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void DisconnectTerminals(string sourceTerminal, string destinationTerminal)

#### Remarks

This method cannot remove task-based routes, such as those you create through timing and triggering configuration. When this method is called, it immediately unreserves the route. This type of routing is called [immediate routing](/csh?context=nidaqmx_mxcncpts_immediaterouting).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sourceTerminal | string | The originating terminal of the route. |
| destinationTerminal | string | The receiving terminal of the route. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-drivermajorversion.html language=enus -->
## TOPIC 01557: DriverMajorVersion

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-drivermajorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-drivermajorversion.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the major portion of the installed version of NI-DAQmx, such as 7 for version 7.0. SyntaxNamespace: NationalInstruments.DAQmxpublic long DriverMajorVersion { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DriverMajorVersion

Indicates the major portion of the installed version of NI-DAQmx, such as 7 for version 7.0.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long DriverMajorVersion { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-driverminorversion.html language=enus -->
## TOPIC 01558: DriverMinorVersion

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-driverminorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-driverminorversion.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the minor portion of the installed version of NI-DAQmx, such as 0 for version 7.0. SyntaxNamespace: NationalInstruments.DAQmxpublic long DriverMinorVersion { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DriverMinorVersion

Indicates the minor portion of the installed version of NI-DAQmx, such as 0 for version 7.0.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long DriverMinorVersion { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-driverupdateversion.html language=enus -->
## TOPIC 01559: DriverUpdateVersion

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-driverupdateversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-driverupdateversion.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the update portion of the installed version of NI-DAQmx, such as 1 for version 9.0.1. SyntaxNamespace: NationalInstruments.DAQmxpublic long DriverUpdateVersion { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DriverUpdateVersion

Indicates the update portion of the installed version of NI-DAQmx, such as 1 for version 9.0.1.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long DriverUpdateVersion { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-getanalogpowerupstateswithoutputtype__string-out-out.html language=enus -->
## TOPIC 01560: GetAnalogPowerUpStatesWithOutputType(string, out double[], out AOPowerUpOutputBehavior[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-getanalogpowerupstateswithoutputtype__string-out-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-getanalogpowerupstateswithoutputtype__string-out-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the states that analog physical channels on a device are set to when the device powers up or when the device is reset. SyntaxNamespace: NationalInstruments.DAQmxpublic void GetAnalogPowerUpStatesWithOutputType(string channels, out double[] states, out AOPowerUpOutputBehavior[] modes)RemarksPowe

### GetAnalogPowerUpStatesWithOutputType(string, out double[], out AOPowerUpOutputBehavior[])

Gets the states that analog physical channels on a device are set to when the device powers up or when the device is reset.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void GetAnalogPowerUpStatesWithOutputType(string channels, out double[] states, out AOPowerUpOutputBehavior[] modes)

#### Remarks

Power-up states are stored in EEPROMs that you can write to only a limited number of times. Therefore, you should use this method as infrequently as possible. This method writes to the EEPROM only if a setting you request is different from the one currently stored on the EEPROM. This method writes power-up states in sequential order. Therefore, if a physical channel has multiple entries, the last entry is used.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channels | string | The physical channels that were modified. |
| states | out double[] | The 1D array listing the power-up states for each corresponding physical channel. If the channel type for the physical channel is high-impedance, this value is 0. |
| modes | out AOPowerUpOutputBehavior[] | The value set for the physical channel when the device powers up or when the device is reset. You specify this value with AOPowerUpOutputBehavior. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-getdevicepowerupstate__string-out-out-out-out.html language=enus -->
## TOPIC 01561: GetDevicePowerUpState(string, out string[], out double[], out string[], out double[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-getdevicepowerupstate__string-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-getdevicepowerupstate__string-out-out-out-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power up states for analog physical channels. SyntaxNamespace: NationalInstruments.DAQmxpublic void GetDevicePowerUpState(string deviceName, out string[] voltageChannels, out double[] voltageValues, out string[] currentChannels, out double[] currentValues)ParametersNameTypeDescriptiondevice

### GetDevicePowerUpState(string, out string[], out double[], out string[], out double[])

Gets the power up states for analog physical channels.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void GetDevicePowerUpState(string deviceName, out string[] voltageChannels, out double[] voltageValues, out string[] currentChannels, out double[] currentValues)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deviceName | string | The name, as configured in Measurement & Automation Explorer (MAX), of the device to which this operation applies. |
| voltageChannels | out string[] | The physical channels that were modified. |
| voltageValues | out double[] | The power up state set for the physical channel specified with the voltageChannels output. |
| currentChannels | out string[] | The physical channels that were modified. |
| currentValues | out double[] | The power up state set for the physical channel specified with the currentChannels output. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-getdevicepowerupstate__string-out-out.1.html language=enus -->
## TOPIC 01562: GetDevicePowerUpState(string, out string[], out DigitalPowerUpState[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-getdevicepowerupstate__string-out-out.1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-getdevicepowerupstate__string-out-out.1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power up states for digital physical lines. SyntaxNamespace: NationalInstruments.DAQmxpublic void GetDevicePowerUpState(string deviceName, out string[] channels, out DigitalPowerUpState[] states)ParametersNameTypeDescriptiondeviceNamestringThe name, as configured in Measurement & Automation

### GetDevicePowerUpState(string, out string[], out DigitalPowerUpState[])

Gets the power up states for digital physical lines.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void GetDevicePowerUpState(string deviceName, out string[] channels, out DigitalPowerUpState[] states)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deviceName | string | The name, as configured in Measurement & Automation Explorer (MAX), of the device to which this operation applies. |
| channels | out string[] | The physical channels that were modified. |
| states | out DigitalPowerUpState[] | The power up state set for the physical channels specified in channels . |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-getdevicepowerupstate__string-out-out.html language=enus -->
## TOPIC 01563: GetDevicePowerUpState(string, out string[], out DigitalPullUpPullDownResistorState[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-getdevicepowerupstate__string-out-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-getdevicepowerupstate__string-out-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the resistor level for lines when they are in tristate logic. SyntaxNamespace: NationalInstruments.DAQmxpublic void GetDevicePowerUpState(string deviceName, out string[] channels, out DigitalPullUpPullDownResistorState[] states)ParametersNameTypeDescriptiondeviceNamestringThe name, as configure

### GetDevicePowerUpState(string, out string[], out DigitalPullUpPullDownResistorState[])

Gets the resistor level for lines when they are in tristate logic.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void GetDevicePowerUpState(string deviceName, out string[] channels, out DigitalPullUpPullDownResistorState[] states)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deviceName | string | The name, as configured in Measurement & Automation Explorer (MAX), of the device to which this operation applies. |
| channels | out string[] | The physical channels that were modified. |
| states | out DigitalPullUpPullDownResistorState[] | The pull up pull down level set for the physical channel specified with DigitalPullUpPullDownResistorState. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-getdisconnectedcdaqsynchronizationports__string-double-out.html language=enus -->
## TOPIC 01564: GetDisconnectedCDaqSynchronizationPorts(string, double, out bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-getdisconnectedcdaqsynchronizationports__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-getdisconnectedcdaqsynchronizationports__string-double-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Verifies configured cDAQ Sync connections between devices. SyntaxNamespace: NationalInstruments.DAQmxpublic string GetDisconnectedCDaqSynchronizationPorts(string deviceRequested, double timeout, out bool disconnectedPortsFound)RemarksFailures generally indicate a wiring issue or that a device has be

### GetDisconnectedCDaqSynchronizationPorts(string, double, out bool)

Verifies configured cDAQ Sync connections between devices.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string GetDisconnectedCDaqSynchronizationPorts(string deviceRequested, double timeout, out bool disconnectedPortsFound)

#### Remarks

Failures generally indicate a wiring issue or that a device has been powered off or removed. Stop all NI-DAQmx tasks running on the devices prior to running this method because any running tasks cause the verification process to fail.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deviceRequested | string | The names of the CompactDAQ chassis, C Series modules, or cDAQ Sync ports in comma separated form to search. If no names are specified, all cDAQ Sync ports on connected, non-simulated devices are scanned. |
| timeout | double | The time in seconds to wait for the device to respond before timing out. If a timeout occurs, no configuration is changed. |
| disconnectedPortsFound | out bool | Indicates if any port connections are unverified. |

#### Returns

The port-to-port connections that failed verification.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-getlogicfamilypowerupstate__string.html language=enus -->
## TOPIC 01565: GetLogicFamilyPowerUpState(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-getlogicfamilypowerupstate__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-getlogicfamilypowerupstate__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the digital logic family for a device. SyntaxNamespace: NationalInstruments.DAQmxpublic LogicFamily GetLogicFamilyPowerUpState(string deviceName)ParametersNameTypeDescriptiondeviceNamestringThe name, as configured in Measurement & Automation Explorer (MAX), of the device to which this operation

### GetLogicFamilyPowerUpState(string)

Gets the digital logic family for a device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [LogicFamily](nationalinstruments-daqmx-logicfamily.html) GetLogicFamilyPowerUpState(string deviceName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deviceName | string | The name, as configured in Measurement & Automation Explorer (MAX), of the device to which this operation applies. |

#### Returns

Returns the [DILogicFamily](nationalinstruments-daqmx-dilogicfamily.html) that the device is set to when the device powers up.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-getphysicalchannels__physicalchanneltypes-physicalchannelaccess.html language=enus -->
## TOPIC 01566: GetPhysicalChannels(PhysicalChannelTypes, PhysicalChannelAccess)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-getphysicalchannels__physicalchanneltypes-physicalchannelaccess.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-getphysicalchannels__physicalchanneltypes-physicalchannelaccess.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the physical channel names of devices installed in the system. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] GetPhysicalChannels(PhysicalChannelTypes physicalChannelTypes, PhysicalChannelAccess physicalChannelAccess)ParametersNameTypeDescriptionphysicalChannel

### GetPhysicalChannels(PhysicalChannelTypes, PhysicalChannelAccess)

Gets an array that contains the [physical channel names](/csh?context=nidaqmx_mxcncpts_chans) of devices installed in the system.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] GetPhysicalChannels(PhysicalChannelTypes physicalChannelTypes, PhysicalChannelAccess physicalChannelAccess)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelTypes | PhysicalChannelTypes | The types of physical channels to include. |
| physicalChannelAccess | PhysicalChannelAccess | The access types of physical channels to include. |

#### Returns

An array that contains the names of the requested physical channels in the system.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-getsavedchannelinfo__string.html language=enus -->
## TOPIC 01567: GetSavedChannelInfo(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-getsavedchannelinfo__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-getsavedchannelinfo__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a SavedChannelInfo object that you can use to retrieve information about the specified global channel stored in Measurement & Automation Explorer (MAX). SyntaxNamespace: NationalInstruments.DAQmxpublic SavedChannelInfo GetSavedChannelInfo(string persistedName)ParametersNameTypeDescriptionper

### GetSavedChannelInfo(string)

Creates a [SavedChannelInfo](nationalinstruments-daqmx-savedchannelinfo.html) object that you can use to retrieve information about the specified global channel stored in Measurement & Automation Explorer (MAX).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SavedChannelInfo](nationalinstruments-daqmx-savedchannelinfo.html) GetSavedChannelInfo(string persistedName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| persistedName | string | The name of the global channel stored in MAX. |

#### Returns

A [SavedChannelInfo](nationalinstruments-daqmx-savedchannelinfo.html) object that represents the global channel stored in MAX.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-getsavedscaleinfo__string.html language=enus -->
## TOPIC 01568: GetSavedScaleInfo(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-getsavedscaleinfo__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-getsavedscaleinfo__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a SavedScaleInfo object that you can use to retrieve information about the specified custom scale stored in Measurement & Automation Explorer (MAX). SyntaxNamespace: NationalInstruments.DAQmxpublic SavedScaleInfo GetSavedScaleInfo(string persistedName)ParametersNameTypeDescriptionpersistedNa

### GetSavedScaleInfo(string)

Creates a [SavedScaleInfo](nationalinstruments-daqmx-savedscaleinfo.html) object that you can use to retrieve information about the specified [custom scale](/csh?context=nidaqmx_mxcncpts_customscales) stored in Measurement & Automation Explorer (MAX).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SavedScaleInfo](nationalinstruments-daqmx-savedscaleinfo.html) GetSavedScaleInfo(string persistedName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| persistedName | string | The name of the custom scale stored in MAX. |

#### Returns

A [SavedScaleInfo](nationalinstruments-daqmx-savedscaleinfo.html) object that represents the custom scale stored in MAX.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-getsavedtaskinfo__string.html language=enus -->
## TOPIC 01569: GetSavedTaskInfo(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-getsavedtaskinfo__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-getsavedtaskinfo__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a SavedTaskInfo object that you can use to retrieve information about the specified task stored in Measurement & Automation Explorer (MAX). SyntaxNamespace: NationalInstruments.DAQmxpublic SavedTaskInfo GetSavedTaskInfo(string persistedName)ParametersNameTypeDescriptionpersistedNamestringThe

### GetSavedTaskInfo(string)

Creates a [SavedTaskInfo](nationalinstruments-daqmx-savedtaskinfo.html) object that you can use to retrieve information about the specified [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) stored in Measurement & Automation Explorer (MAX).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SavedTaskInfo](nationalinstruments-daqmx-savedtaskinfo.html) GetSavedTaskInfo(string persistedName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| persistedName | string | The name of the task stored in MAX. |

#### Returns

A [SavedTaskInfo](nationalinstruments-daqmx-savedtaskinfo.html) object that represents the task stored in MAX.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-getswitchrelaycount__string.html language=enus -->
## TOPIC 01570: GetSwitchRelayCount(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-getswitchrelaycount__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-getswitchrelaycount__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This method is obsolete. Will warn if used Returns the number of times a relay has actuated on switches that support querying the relay count. SyntaxNamespace: NationalInstruments.DAQmxpublic long GetSwitchRelayCount(string relay)RemarksYou must wait for the switch to settle before this me

### GetSwitchRelayCount(string)

**Obsolete: This method is obsolete. Will warn if used** 
Returns the number of times a relay has actuated on switches that support querying the relay count.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long GetSwitchRelayCount(string relay)

#### Remarks

You must wait for the switch to settle before this method can determine an accurate relay count. Use this method to track relay lifetime and usage.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| relay | string | The relay you want to query. |

#### Returns

The number of times the relay has been activated.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-getswitchrelaycounts__string.html language=enus -->
## TOPIC 01571: GetSwitchRelayCounts(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-getswitchrelaycounts__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-getswitchrelaycounts__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This method is obsolete. Will warn if used Returns the number of times a set of relays have actuated. SyntaxNamespace: NationalInstruments.DAQmxpublic long[] GetSwitchRelayCounts(string relays)RemarksYou must wait for the switch to settle before this method can determine an accurate relay

### GetSwitchRelayCounts(string)

**Obsolete: This method is obsolete. Will warn if used** 
Returns the number of times a set of relays have actuated.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long[] GetSwitchRelayCounts(string relays)

#### Remarks

You must wait for the switch to settle before this method can determine an accurate relay count. Use this method to track relay lifetime and usage.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| relays | string | The set of relays you want to query. You can use a string that contains a comma-delimited list of relays. |

#### Returns

The number of times each specified relay has been activated. The order of this array corresponds to the order of *relays* .

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-getswitchrelayposition__string.html language=enus -->
## TOPIC 01572: GetSwitchRelayPosition(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-getswitchrelayposition__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-getswitchrelayposition__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This method is obsolete. Will warn if used Returns the current position of a single relay. SyntaxNamespace: NationalInstruments.DAQmxpublic SwitchRelayPosition GetSwitchRelayPosition(string relay)ParametersNameTypeDescriptionrelaystringThe relay you want to query.ReturnsThe position of the

### GetSwitchRelayPosition(string)

**Obsolete: This method is obsolete. Will warn if used** 
Returns the current position of a single relay.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SwitchRelayPosition](nationalinstruments-daqmx-switchrelayposition.html) GetSwitchRelayPosition(string relay)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| relay | string | The relay you want to query. |

#### Returns

The position of the relay.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-getswitchrelaypositions__string.html language=enus -->
## TOPIC 01573: GetSwitchRelayPositions(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-getswitchrelaypositions__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-getswitchrelaypositions__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This method is obsolete. Will warn if used Returns the current position of a set of relays. SyntaxNamespace: NationalInstruments.DAQmxpublic SwitchRelayPosition[] GetSwitchRelayPositions(string relays)ParametersNameTypeDescriptionrelaysstringThe set of relays you want to query. You can use

### GetSwitchRelayPositions(string)

**Obsolete: This method is obsolete. Will warn if used** 
Returns the current position of a set of relays.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SwitchRelayPosition](nationalinstruments-daqmx-switchrelayposition.html)[] GetSwitchRelayPositions(string relays)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| relays | string | The set of relays you want to query. You can use a string that contains a comma-delimited list of relays. |

#### Returns

The position of each specified relay. The order of this array corresponds to the order of *relays* .

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-getterminals__terminaltypes.html language=enus -->
## TOPIC 01574: GetTerminals(TerminalTypes)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-getterminals__terminaltypes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-getterminals__terminaltypes.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the terminal names of devices installed in the system. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] GetTerminals(TerminalTypes terminalTypes)ParametersNameTypeDescriptionterminalTypesTerminalTypesThe types of terminals to include.ReturnsAn array that contains

### GetTerminals(TerminalTypes)

Gets an array that contains the [terminal names](/csh?context=nidaqmx_mxcncpts_terminal) of devices installed in the system.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] GetTerminals(TerminalTypes terminalTypes)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| terminalTypes | TerminalTypes | The types of terminals to include. |

#### Returns

An array that contains the names of the requested terminals in the system.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-globalchannels.html language=enus -->
## TOPIC 01575: GlobalChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-globalchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-globalchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates an array that contains the names of all global channels saved on the system. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] GlobalChannels { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for

### GlobalChannels

Indicates an array that contains the names of all global channels saved on the system.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] GlobalChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-isreadorwritelate.html language=enus -->
## TOPIC 01576: IsReadOrWriteLate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-isreadorwritelate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-isreadorwritelate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: The IsReadOrWriteLate property is deprecated. Please use the Timing.SinglePoint.WaitForNextSampleClock method instead. Will warn if used Determines if a hardware-timed single-point read or write operation is overdue on the current thread. The IsReadOrWriteLate property has been deprecated

### IsReadOrWriteLate

**Obsolete: The IsReadOrWriteLate property is deprecated. Please use the Timing.SinglePoint.WaitForNextSampleClock method instead. Will warn if used** 
Determines if a hardware-timed single-point read or write operation is overdue on the current thread. The IsReadOrWriteLate property has been deprecated in favor of the [WaitForNextSampleClock(double)](nationalinstruments-daqmx-singlepoint-waitfornextsampleclock__double.html) method.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool IsReadOrWriteLate { get; }

#### Remarks

The value of this property is not meaningful unless reading or writing a task that has [SampleQuantityMode](nationalinstruments-daqmx-timing-samplequantitymode.html) set to [HardwareTimedSinglePoint](nationalinstruments-daqmx-samplequantitymode.html).

This property returns information only about warnings that occur in the thread from which the property is accessed. This behavior distinguishes warnings that are caused by actions in one thread from warnings that are caused by independent actions that occur at the same time in another thread.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

#### See Also

- SinglePoint

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-lastdaqwarning.html language=enus -->
## TOPIC 01577: LastDaqWarning

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-lastdaqwarning.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-lastdaqwarning.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DaqWarningEventArgs for the last DaqWarning event that occurred. SyntaxNamespace: NationalInstruments.DAQmxpublic DaqWarningEventArgs LastDaqWarning { get; }RemarksThe DaqWarningEventArgs for the DaqWarning event.This property returns information only about warnings that occur in the thread

### LastDaqWarning

Gets the [DaqWarningEventArgs](nationalinstruments-daqmx-daqwarningeventargs.html) for the last [DaqWarning](nationalinstruments-daqmx-daqsystem-daqwarning.html) event that occurred.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DaqWarningEventArgs](nationalinstruments-daqmx-daqwarningeventargs.html) LastDaqWarning { get; }

#### Remarks

The [DaqWarningEventArgs](nationalinstruments-daqmx-daqwarningeventargs.html) for the [DaqWarning](nationalinstruments-daqmx-daqsystem-daqwarning.html) event.

This property returns information only about warnings that occur in the thread from which the property is accessed. This behavior distinguishes warnings that are caused by actions in one thread from warnings that are caused by independent actions that occur at the same time in another thread.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-loaddevice__string.html language=enus -->
## TOPIC 01578: LoadDevice(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-loaddevice__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-loaddevice__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a Device that you can use to control the specified device or get information about that device. SyntaxNamespace: NationalInstruments.DAQmxpublic Device LoadDevice(string deviceName)RemarksYou can use the Devices property to get a list of devices installed on the system. ParametersNameTypeDes

### LoadDevice(string)

Creates a [Device](nationalinstruments-daqmx-device.html) that you can use to control the specified device or get information about that device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [Device](nationalinstruments-daqmx-device.html) LoadDevice(string deviceName)

#### Remarks

You can use the [Devices](nationalinstruments-daqmx-daqsystem-devices.html) property to get a list of devices installed on the system.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deviceName | string | The name of the device. |

#### Returns

A [Device](nationalinstruments-daqmx-device.html) that represents the device.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-loadphysicalchannel__string.html language=enus -->
## TOPIC 01579: LoadPhysicalChannel(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-loadphysicalchannel__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-loadphysicalchannel__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a PhysicalChannel that you can use to configure and retrieve TEDS information for the specified physical channel. SyntaxNamespace: NationalInstruments.DAQmxpublic PhysicalChannel LoadPhysicalChannel(string physicalChannelName)ParametersNameTypeDescriptionphysicalChannelNamestringThe name of

### LoadPhysicalChannel(string)

Creates a [PhysicalChannel](nationalinstruments-daqmx-physicalchannel.html) that you can use to configure and retrieve TEDS information for the specified physical channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [PhysicalChannel](nationalinstruments-daqmx-physicalchannel.html) LoadPhysicalChannel(string physicalChannelName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelName | string | The name of the physical channel. |

#### Returns

A [PhysicalChannel](nationalinstruments-daqmx-physicalchannel.html) that represents the physical channel.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-loadscale__string.html language=enus -->
## TOPIC 01580: LoadScale(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-loadscale__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-loadscale__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads a scale that is stored in Measurement & Automation Explorer (MAX). SyntaxNamespace: NationalInstruments.DAQmxpublic Scale LoadScale(string persistedName)RemarksYou can use the Scales property to get a list of custom scales on the system. ParametersNameTypeDescriptionpersistedNamestringThe name

### LoadScale(string)

Loads a scale that is stored in Measurement & Automation Explorer (MAX).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [Scale](nationalinstruments-daqmx-scale.html) LoadScale(string persistedName)

#### Remarks

You can use the [Scales](nationalinstruments-daqmx-daqsystem-scales.html) property to get a list of custom scales on the system.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| persistedName | string | The name of the scale to load. |

#### Returns

A [Scale](nationalinstruments-daqmx-scale.html) that represents the scale that is stored in MAX.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-loadswitchchannel__string.html language=enus -->
## TOPIC 01581: LoadSwitchChannel(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-loadswitchchannel__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-loadswitchchannel__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This method is obsolete. Will warn if used Creates a SwitchChannel that you can use to get the switch channel capabilities and set the usage type for the switch channel. SyntaxNamespace: NationalInstruments.DAQmxpublic SwitchChannel LoadSwitchChannel(string switchChannelName)ParametersName

### LoadSwitchChannel(string)

**Obsolete: This method is obsolete. Will warn if used** 
Creates a [SwitchChannel](nationalinstruments-daqmx-switchchannel.html) that you can use to get the switch channel capabilities and set the usage type for the switch channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SwitchChannel](nationalinstruments-daqmx-switchchannel.html) LoadSwitchChannel(string switchChannelName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| switchChannelName | string | The name of the switch channel. |

#### Returns

A [SwitchChannel](nationalinstruments-daqmx-switchchannel.html) that represents the switch channel.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-loadtask__string.html language=enus -->
## TOPIC 01582: LoadTask(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-loadtask__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-loadtask__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads a task that is stored in Measurement & Automation Explorer (MAX). SyntaxNamespace: NationalInstruments.DAQmxpublic unsafe Task LoadTask(string persistedName)RemarksYou can use the Tasks property to get a list of tasks on the system. ParametersNameTypeDescriptionpersistedNamestringThe name of t

### LoadTask(string)

Loads a task that is stored in Measurement & Automation Explorer (MAX).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public unsafe [Task](nationalinstruments-daqmx-task.html) LoadTask(string persistedName)

#### Remarks

You can use the [Tasks](nationalinstruments-daqmx-daqsystem-tasks.html) property to get a list of tasks on the system.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| persistedName | string | The name of the task to load. |

#### Returns

A [Task](nationalinstruments-daqmx-task.html) that represents the task that is stored in MAX.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-local.html language=enus -->
## TOPIC 01583: Local

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-local.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-local.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an instance of the DaqSystem class that represents the local DAQ system. SyntaxNamespace: NationalInstruments.DAQmxpublic static DaqSystem Local { get; }RemarksAn instance of the DaqSystem class.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error

### Local

Gets an instance of the [DaqSystem](nationalinstruments-daqmx-daqsystem.html) class that represents the local DAQ system.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public static [DaqSystem](nationalinstruments-daqmx-daqsystem.html) Local { get; }

#### Remarks

An instance of the [DaqSystem](nationalinstruments-daqmx-daqsystem.html) class.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-openswitchrelays__string-bool.html language=enus -->
## TOPIC 01584: OpenSwitchRelays(string, bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-openswitchrelays__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-openswitchrelays__string-bool.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This method is obsolete. Will warn if used Opens the specified relays. SyntaxNamespace: NationalInstruments.DAQmxpublic void OpenSwitchRelays(string relays, [MarshalAs(UnmanagedType.U1)] bool waitForSettling)RemarksWhen you operate relays directly, you circumvent the protection that channe

### OpenSwitchRelays(string, bool)

**Obsolete: This method is obsolete. Will warn if used** 
Opens the specified relays.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void OpenSwitchRelays(string relays, [MarshalAs(UnmanagedType.U1)] bool waitForSettling)

#### Remarks

When you operate relays directly, you circumvent the protection that channel usage types offer. Avoid using this method when you use the [ConnectSwitchChannels(string, bool)](nationalinstruments-daqmx-daqsystem-connectswitchchannels__string-bool.html) or [DisconnectSwitchChannels(string, bool)](nationalinstruments-daqmx-daqsystem-disconnectswitchchannels__string-bool.html) methods because this method does not pass the changes that you make to those methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| relays | string | A set of relays to open. You can specify a string that contains a comma-delimited list of relays. |
| waitForSettling | bool | If true, this method waits for the switches to settle before returning. If false, the method returns immediately after the operation. This settling time is controlled through the SettlingTime property. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-readidpinmemory__string-string-out-out.html language=enus -->
## TOPIC 01585: ReadIDPinMemory(string, string, out byte[], out uint)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-readidpinmemory__string-string-out-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-readidpinmemory__string-string-out-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads bitstream and format code from the memory connected to selected ID Pin. SyntaxNamespace: NationalInstruments.DAQmxpublic void ReadIDPinMemory(string deviceName, string idPinName, out byte[] data, out uint formatCode)ParametersNameTypeDescriptiondeviceNamestringThe name, as configured in Measur

### ReadIDPinMemory(string, string, out byte[], out uint)

Reads bitstream and format code from the memory connected to selected ID Pin.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ReadIDPinMemory(string deviceName, string idPinName, out byte[] data, out uint formatCode)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deviceName | string | The name, as configured in Measurement & Automation Explorer (MAX), of the device to which this operation applies. |
| idPinName | string | The name, as obtained from Identification.ID Pin.Pin Names in DAQmxDevice Attributes, of the ID Pin to which this operation applies. |
| data | out byte[] | An initialized 1D array of bytes that contains the read data. |
| formatCode | out uint | A byte indicating the format of the data read from the memory. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-removecdaqsynchronizationconnection__string.html language=enus -->
## TOPIC 01586: RemoveCDaqSynchronizationConnection(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-removecdaqsynchronizationconnection__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-removecdaqsynchronizationconnection__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes a cDAQ Sync connection between devices. The connection is not verified. SyntaxNamespace: NationalInstruments.DAQmxpublic void RemoveCDaqSynchronizationConnection(string portList)ParametersNameTypeDescriptionportListstringSpecifies the cDAQ Sync ports to disconnect.ExceptionsTypeDescriptionNa

### RemoveCDaqSynchronizationConnection(string)

Removes a cDAQ Sync connection between devices. The connection is not verified.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void RemoveCDaqSynchronizationConnection(string portList)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| portList | string | Specifies the cDAQ Sync ports to disconnect. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-saveglobalchannel__channel-string-saveoptions.html language=enus -->
## TOPIC 01587: SaveGlobalChannel(Channel, string, SaveOptions)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-saveglobalchannel__channel-string-saveoptions.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-saveglobalchannel__channel-string-saveoptions.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the specified local or global channel to Measurement & Automation Explorer (MAX) as a global channel, under the virtual name it was given when it was created and with specified author and options values. SyntaxNamespace: NationalInstruments.DAQmxpublic void SaveGlobalChannel(Channel channel, s

### SaveGlobalChannel(Channel, string, SaveOptions)

Saves the specified [local or global channel](/csh?context=nidaqmx_mxcncpts_chans) to Measurement & Automation Explorer (MAX) as a global channel, under the virtual name it was given when it was created and with specified author and options values.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void SaveGlobalChannel(Channel channel, string author, SaveOptions options)

#### Remarks

You may save a channel under a different name by calling [SaveGlobalChannelAs(Channel, string)](nationalinstruments-daqmx-daqsystem-saveglobalchannelas__channel-string.html).

You cannot view programmatically saved global channels in the DAQ Assistant for versions of NI-DAQ earlier than 7.4. To view a programmatically saved global channel in an earlier version of NI-DAQ, first use the DAQ Assistant in NI-DAQ 7.4 or later to save the global channel.

Visit the [DAQmx Professional Developer Tools](https://#) Web site for more information and examples of programmatically saving global channels.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channel | Channel | The channel instance to save. |
| author | string | A user-specified string that represents the name to store with the channel. For example, channels created with the DAQ Assistant have the string "DAQ Assistant" as their author. You may pass Empty. |
| options | SaveOptions | One or more flags indicating various save options. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-saveglobalchannel__channel.html language=enus -->
## TOPIC 01588: SaveGlobalChannel(Channel)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-saveglobalchannel__channel.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-saveglobalchannel__channel.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the specified local or global channel to Measurement & Automation Explorer (MAX) as a global channel, under the virtual name it was given when it was created. SyntaxNamespace: NationalInstruments.DAQmxpublic void SaveGlobalChannel(Channel channel)RemarksYou may save a channel under a different

### SaveGlobalChannel(Channel)

Saves the specified [local or global channel](/csh?context=nidaqmx_mxcncpts_chans) to Measurement & Automation Explorer (MAX) as a global channel, under the virtual name it was given when it was created.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void SaveGlobalChannel(Channel channel)

#### Remarks

You may save a channel under a different name by calling [SaveGlobalChannelAs(Channel, string)](nationalinstruments-daqmx-daqsystem-saveglobalchannelas__channel-string.html).

This method sets the [Default](nationalinstruments-daqmx-saveoptions.html) option for the saved channel and uses an empty string for the channel [Author](nationalinstruments-daqmx-savedtaskinfo-author.html). You can specify your own options and author value by using the [SaveGlobalChannel(Channel, string, SaveOptions)](nationalinstruments-daqmx-daqsystem-saveglobalchannel__channel-string-saveoptions.html) overload.

You cannot view programmatically saved global channels in the DAQ Assistant for versions of NI-DAQ earlier than 7.4. To view a programmatically saved global channel in an earlier version of NI-DAQ, first use the DAQ Assistant in NI-DAQ 7.4 or later to save the global channel.

Visit the [DAQmx Professional Developer Tools](https://#) Web site for more information and examples of programmatically saving global channels.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channel | Channel | The channel instance to save. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-saveglobalchannelas__channel-string-string-saveoptions.html language=enus -->
## TOPIC 01589: SaveGlobalChannelAs(Channel, string, string, SaveOptions)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-saveglobalchannelas__channel-string-string-saveoptions.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-saveglobalchannelas__channel-string-string-saveoptions.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the local or global channel to Measurement & Automation Explorer (MAX) as a global channel, under the specified name and specified author and options values. SyntaxNamespace: NationalInstruments.DAQmxpublic void SaveGlobalChannelAs(Channel channel, string persistedName, string author, SaveOpti

### SaveGlobalChannelAs(Channel, string, string, SaveOptions)

Saves the [local or global channel](/csh?context=nidaqmx_mxcncpts_chans) to Measurement & Automation Explorer (MAX) as a global channel, under the specified name and specified author and options values.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void SaveGlobalChannelAs(Channel channel, string persistedName, string author, SaveOptions options)

#### Remarks

If you do not assign a value to the saved channel, NI-DAQmx uses the name currently assigned to the channel.

You cannot view programmatically saved global channels in the DAQ Assistant for versions of NI-DAQ earlier than 7.4. To view a programmatically saved global channel in an earlier version of NI-DAQ, first use the DAQ Assistant in NI-DAQ 7.4 or later to save the global channel.

Visit the [DAQmx Professional Developer Tools](https://#) Web site for more information and examples of programmatically saving global channels.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channel | Channel | The channel instance to save. |
| persistedName | string | The name to use for the saved channel. |
| author | string | A user-specified string that represents the name to store with the channel. For example, channels created with the DAQ Assistant have the string "DAQ Assistant" as their author. You may pass Empty. |
| options | SaveOptions | One or more flags indicating various save options. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-saveglobalchannelas__channel-string.html language=enus -->
## TOPIC 01590: SaveGlobalChannelAs(Channel, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-saveglobalchannelas__channel-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-saveglobalchannelas__channel-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the local or global channel to Measurement & Automation Explorer (MAX) as a global channel, under the specified name. SyntaxNamespace: NationalInstruments.DAQmxpublic void SaveGlobalChannelAs(Channel channel, string persistedName)RemarksThis method sets the Default option for the saved channel

### SaveGlobalChannelAs(Channel, string)

Saves the [local or global channel](/csh?context=nidaqmx_mxcncpts_chans) to Measurement & Automation Explorer (MAX) as a global channel, under the specified name.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void SaveGlobalChannelAs(Channel channel, string persistedName)

#### Remarks

This method sets the [Default](nationalinstruments-daqmx-saveoptions.html) option for the saved channel and uses an empty string for the channel [Author](nationalinstruments-daqmx-savedchannelinfo-author.html). You can specify your own options and author value by using the [SaveGlobalChannelAs(Channel, string, string, SaveOptions)](nationalinstruments-daqmx-daqsystem-saveglobalchannelas__channel-string-string-saveoptions.html) overload.

If you do not assign a value to the saved channel, NI-DAQmx uses the name currently assigned to the channel.

You cannot view programmatically saved global channels in the DAQ Assistant for versions of NI-DAQ earlier than 7.4. To view a programmatically saved global channel in an earlier version of NI-DAQ, first use the DAQ Assistant in NI-DAQ 7.4 or later to save the global channel.

Visit the [DAQmx Professional Developer Tools](https://#) Web site for more information and examples of programmatically saving global channels.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channel | Channel | The channel instance to save. |
| persistedName | string | The name to use for the saved channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-savescale__scale-string-saveoptions.html language=enus -->
## TOPIC 01591: SaveScale(Scale, string, SaveOptions)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-savescale__scale-string-saveoptions.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-savescale__scale-string-saveoptions.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the specified custom scale to Measurement & Automation Explorer (MAX) under the name it was given when it was created and with specified author and options values. SyntaxNamespace: NationalInstruments.DAQmxpublic void SaveScale(Scale scale, string author, SaveOptions options)RemarksYou may sav

### SaveScale(Scale, string, SaveOptions)

Saves the specified [custom scale](/csh?context=nidaqmx_mxcncpts_customscales) to Measurement & Automation Explorer (MAX) under the name it was given when it was created and with specified author and options values.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void SaveScale(Scale scale, string author, SaveOptions options)

#### Remarks

You may save a scale under a different name by calling [SaveScaleAs(Scale, string)](nationalinstruments-daqmx-daqsystem-savescaleas__scale-string.html).

Visit the [DAQmx Professional Developer Tools](https://#) Web site for more information and examples of programmatically saving custom scales.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| scale | Scale | The scale instance to save. |
| author | string | A user-specified string that represents the name to store with the scale. For example, scales created with the DAQ Assistant have the string "DAQ Assistant" as their author. You may pass Empty. |
| options | SaveOptions | One or more flags indicating various save options. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-savescale__scale.html language=enus -->
## TOPIC 01592: SaveScale(Scale)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-savescale__scale.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-savescale__scale.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the specified custom scale to Measurement & Automation Explorer (MAX) under the name it was given when it was created. SyntaxNamespace: NationalInstruments.DAQmxpublic void SaveScale(Scale scale)RemarksYou may save a scale under a different name by calling SaveScaleAs(Scale, string). This meth

### SaveScale(Scale)

Saves the specified [custom scale](/csh?context=nidaqmx_mxcncpts_customscales) to Measurement & Automation Explorer (MAX) under the name it was given when it was created.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void SaveScale(Scale scale)

#### Remarks

You may save a scale under a different name by calling [SaveScaleAs(Scale, string)](nationalinstruments-daqmx-daqsystem-savescaleas__scale-string.html).

This method sets the [Default](nationalinstruments-daqmx-saveoptions.html) option for the saved scale and uses an empty string for the scale [Author](nationalinstruments-daqmx-savedscaleinfo-author.html). You can specify your own options and author value by using the [SaveScale(Scale, string, SaveOptions)](nationalinstruments-daqmx-daqsystem-savescale__scale-string-saveoptions.html) overload.

Visit the [DAQmx Professional Developer Tools](https://#) Web site for more information and examples of programmatically saving custom scales.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| scale | Scale | The scale instance to save. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-savescaleas__scale-string-string-saveoptions.html language=enus -->
## TOPIC 01593: SaveScaleAs(Scale, string, string, SaveOptions)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-savescaleas__scale-string-string-saveoptions.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-savescaleas__scale-string-string-saveoptions.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the specified custom scale to Measurement & Automation Explorer (MAX) under the specified name and with specified author and options values. SyntaxNamespace: NationalInstruments.DAQmxpublic void SaveScaleAs(Scale scale, string persistedName, string author, SaveOptions options)RemarksIf you do

### SaveScaleAs(Scale, string, string, SaveOptions)

Saves the specified [custom scale](/csh?context=nidaqmx_mxcncpts_customscales) to Measurement & Automation Explorer (MAX) under the specified name and with specified author and options values.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void SaveScaleAs(Scale scale, string persistedName, string author, SaveOptions options)

#### Remarks

If you do not assign a value to the saved scale, NI-DAQmx uses the name currently assigned to the scale.

Visit the [DAQmx Professional Developer Tools](https://#) Web site for more information and examples of programmatically saving custom scales.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| scale | Scale | The scale instance to save. |
| persistedName | string | The name to use for the saved scale. |
| author | string | A user-specified string that represents the name to store with the scale. For example, scales created with the DAQ Assistant have the string "DAQ Assistant" as their author. You may pass Empty. |
| options | SaveOptions | One or more flags indicating various save options. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-savescaleas__scale-string.html language=enus -->
## TOPIC 01594: SaveScaleAs(Scale, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-savescaleas__scale-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-savescaleas__scale-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the specified custom scale to Measurement & Automation Explorer (MAX) under the specified name. SyntaxNamespace: NationalInstruments.DAQmxpublic void SaveScaleAs(Scale scale, string persistedName)RemarksThis method sets the Default option for the saved scale and uses an empty string for the sc

### SaveScaleAs(Scale, string)

Saves the specified [custom scale](/csh?context=nidaqmx_mxcncpts_customscales) to Measurement & Automation Explorer (MAX) under the specified name.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void SaveScaleAs(Scale scale, string persistedName)

#### Remarks

This method sets the [Default](nationalinstruments-daqmx-saveoptions.html) option for the saved scale and uses an empty string for the scale [Author](nationalinstruments-daqmx-savedscaleinfo-author.html). You can specify your own options and author value by using the [SaveScaleAs(Scale, string, string, SaveOptions)](nationalinstruments-daqmx-daqsystem-savescaleas__scale-string-string-saveoptions.html) overload.

If you do not assign a value to the saved scale, NI-DAQmx uses the name currently assigned to the scale.

Visit the [DAQmx Professional Developer Tools](https://#) Web site for more information and examples of programmatically saving custom scales.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| scale | Scale | The scale instance to save. |
| persistedName | string | The name to use for the saved scale. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-savetask__task-string-saveoptions.html language=enus -->
## TOPIC 01595: SaveTask(Task, string, SaveOptions)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-savetask__task-string-saveoptions.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-savetask__task-string-saveoptions.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the specified task and any local channels it contains to Measurement & Automation Explorer (MAX) under the name it was given when it was created, with specifed author and options values. SyntaxNamespace: NationalInstruments.DAQmxpublic void SaveTask(Task task, string author, SaveOptions option

### SaveTask(Task, string, SaveOptions)

Saves the specified [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx)and any [local channels](/csh?context=nidaqmx_mxcncpts_chans) it contains to Measurement & Automation Explorer (MAX) under the name it was given when it was created, with specifed author and options values.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void SaveTask(Task task, string author, SaveOptions options)

#### Remarks

You may save a task under a different name by calling [SaveTaskAs(Task, string)](nationalinstruments-daqmx-daqsystem-savetaskas__task-string.html).

You cannot view programmatically saved tasks in the DAQ Assistant for versions of NI-DAQ earlier than 7.4. To view a programmatically saved task in an earlier version of NI-DAQ, first use the DAQ Assistant in NI-DAQ 7.4 or later to save the task.

Visit the [DAQmx Professional Developer Tools](https://#) Web site for more information and examples of programmatically saving tasks.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| task | Task | The task instance to save. |
| author | string | A user-specified string that represents the name to store with the task. For example, tasks created with the DAQ Assistant have the string "DAQ Assistant" as their author. You may pass Empty. |
| options | SaveOptions | One or more flags indicating various save options. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-savetask__task.html language=enus -->
## TOPIC 01596: SaveTask(Task)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-savetask__task.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-savetask__task.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the specified task and any local channels it contains to Measurement & Automation Explorer (MAX) under the name it was given when it was created. SyntaxNamespace: NationalInstruments.DAQmxpublic void SaveTask(Task task)RemarksYou may save a task under a different name by calling SaveTaskAs(Tas

### SaveTask(Task)

Saves the specified [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx)and any [local channels](/csh?context=nidaqmx_mxcncpts_chans) it contains to Measurement & Automation Explorer (MAX) under the name it was given when it was created.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void SaveTask(Task task)

#### Remarks

You may save a task under a different name by calling [SaveTaskAs(Task, string)](nationalinstruments-daqmx-daqsystem-savetaskas__task-string.html).

This method sets the [Default](nationalinstruments-daqmx-saveoptions.html) option for the saved task and uses an empty string for the task [Author](nationalinstruments-daqmx-savedtaskinfo-author.html). You can specify your own options and author value by using the [SaveTask(Task, string, SaveOptions)](nationalinstruments-daqmx-daqsystem-savetask__task-string-saveoptions.html) overload.

You cannot view programmatically saved tasks in the DAQ Assistant for versions of NI-DAQ earlier than 7.4. To view a programmatically saved task in an earlier version of NI-DAQ, first use the DAQ Assistant in NI-DAQ 7.4 or later to save the task.

Visit the [DAQmx Professional Developer Tools](https://#) Web site for more information and examples of programmatically saving tasks.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| task | Task | The task instance to save. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-savetaskas__task-string-string-saveoptions.html language=enus -->
## TOPIC 01597: SaveTaskAs(Task, string, string, SaveOptions)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-savetaskas__task-string-string-saveoptions.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-savetaskas__task-string-string-saveoptions.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the task and any local channels it contains to Measurement & Automation Explorer (MAX) under the specified name and with specified author and options values. SyntaxNamespace: NationalInstruments.DAQmxpublic void SaveTaskAs(Task task, string persistedName, string author, SaveOptions options)Rem

### SaveTaskAs(Task, string, string, SaveOptions)

Saves the [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) and any [local channels](/csh?context=nidaqmx_mxcncpts_chans) it contains to Measurement & Automation Explorer (MAX) under the specified name and with specified author and options values.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void SaveTaskAs(Task task, string persistedName, string author, SaveOptions options)

#### Remarks

If you do not assign a value to the saved task, NI-DAQmx uses the name currently assigned to the task.

You cannot view programmatically saved tasks in the DAQ Assistant for versions of NI-DAQ earlier than 7.4. To view a programmatically saved task in an earlier version of NI-DAQ, first use the DAQ Assistant in NI-DAQ 7.4 or later to save the task.

Visit the [DAQmx Professional Developer Tools](https://#) Web site for more information and examples of programmatically saving tasks.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| task | Task | The task instance to save. |
| persistedName | string | The name to use for the saved task. |
| author | string | A user-specified string that represents the name to store with the task. For example, tasks created with the DAQ Assistant have the string "DAQ Assistant" as their author. You may pass Empty. |
| options | SaveOptions | One or more flags indicating various save options. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-savetaskas__task-string.html language=enus -->
## TOPIC 01598: SaveTaskAs(Task, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-savetaskas__task-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-savetaskas__task-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the task and any local channels it contains to Measurement & Automation Explorer (MAX) under the specified name. SyntaxNamespace: NationalInstruments.DAQmxpublic void SaveTaskAs(Task task, string persistedName)RemarksThis method sets the Default option for the saved task and uses an empty stri

### SaveTaskAs(Task, string)

Saves the [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx) and any [local channels](/csh?context=nidaqmx_mxcncpts_chans) it contains to Measurement & Automation Explorer (MAX) under the specified name.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void SaveTaskAs(Task task, string persistedName)

#### Remarks

This method sets the [Default](nationalinstruments-daqmx-saveoptions.html) option for the saved task and uses an empty string for the task [Author](nationalinstruments-daqmx-savedtaskinfo-author.html). You can specify your own options and author value by using the [SaveTaskAs(Task, string, string, SaveOptions)](nationalinstruments-daqmx-daqsystem-savetaskas__task-string-string-saveoptions.html) overload.

You cannot view programmatically saved tasks in the DAQ Assistant for versions of NI-DAQ earlier than 7.4. To view a programmatically saved task in an earlier version of NI-DAQ, first use the DAQ Assistant in NI-DAQ 7.4 or later to save the task.

Visit the [DAQmx Professional Developer Tools](https://#) Web site for more information and examples of programmatically saving tasks.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| task | Task | The task instance to save. |
| persistedName | string | The name to use for the saved task. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-scales.html language=enus -->
## TOPIC 01599: Scales

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-scales.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-scales.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates an array that contains the names of all custom scales saved on the system. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] Scales { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iter

### Scales

Indicates an array that contains the names of all custom scales saved on the system.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] Scales { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-setanalogpowerupstateswithoutputtype__string-double_arr1-aopowerupoutputbehavior_arr1.html language=enus -->
## TOPIC 01600: SetAnalogPowerUpStatesWithOutputType(string, double[], AOPowerUpOutputBehavior[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-setanalogpowerupstateswithoutputtype__string-double_arr1-aopowerupoutputbehavior_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-setanalogpowerupstateswithoutputtype__string-double_arr1-aopowerupoutputbehavior_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the states that analog physical channels on a device are set to when the device powers up or when the device is reset. SyntaxNamespace: NationalInstruments.DAQmxpublic void SetAnalogPowerUpStatesWithOutputType(string channels, double[] states, AOPowerUpOutputBehavior[] modes)RemarksPower-up sta

### SetAnalogPowerUpStatesWithOutputType(string, double[], AOPowerUpOutputBehavior[])

Sets the states that analog physical channels on a device are set to when the device powers up or when the device is reset.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void SetAnalogPowerUpStatesWithOutputType(string channels, double[] states, AOPowerUpOutputBehavior[] modes)

#### Remarks

Power-up states are stored in EEPROMs that you can write to only a limited number of times. Therefore, you should use this method as infrequently as possible. This method writes to the EEPROM only if a setting you request is different from the one currently stored on the EEPROM. This method writes power-up states in sequential order. Therefore, if a physical channel has multiple entries, the last entry is used.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channels | string | The physical channels that were modified. |
| states | double[] | The 1D array listing the power-up states for each corresponding physical channel. If the channel type for the physical channel is high-impedance, this value is 0. |
| modes | AOPowerUpOutputBehavior[] | The value set for the physical channel when the device powers up or when the device is reset. You specify this value with AOPowerUpOutputBehavior. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-setdevicepowerupstate__string-string_arr1-digitalpowerupstate_arr1.html language=enus -->
## TOPIC 01601: SetDevicePowerUpState(string, string[], DigitalPowerUpState[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-setdevicepowerupstate__string-string_arr1-digitalpowerupstate_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-setdevicepowerupstate__string-string_arr1-digitalpowerupstate_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Updates the power up states to which to set digital physical channels on a device when the device powers up or when you reset the device. SyntaxNamespace: NationalInstruments.DAQmxpublic void SetDevicePowerUpState(string deviceName, string[] virtualChannels, DigitalPowerUpState[] powerUpStates)Remar

### SetDevicePowerUpState(string, string[], DigitalPowerUpState[])

Updates the [power up states](/csh?context=nidaqmx_mxdevconsid_initstates) to which to set digital physical channels on a device when the device powers up or when you reset the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void SetDevicePowerUpState(string deviceName, string[] virtualChannels, DigitalPowerUpState[] powerUpStates)

#### Remarks

Power up states are stored in EEPROMs that you can write to only a limited number of times. Therefore, you should use this method as infrequently as possible. This method writes to the EEPROM only if a setting you request is different from the one currently stored on the EEPROM. This method writes power up states in the sequential order of the power up states array. Therefore, any physical channels with multiple entries in that array use the highest array index.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deviceName | string | The name, as configured in Measurement & Automation Explorer (MAX), of the device to which this operation applies. |
| virtualChannels | string[] | The digital lines or ports for which to set new power up states. Each value in this array specifies a virtual channel string that is assigned the power up state at the corresponding position in the powerUpStates parameter. You cannot set power up states for dedicated digital input lines. You can specify a string that contains a list or range of digital lines or ports. |
| powerUpStates | DigitalPowerUpState[] | The physical channels and power up states to set. Each value in this array applies to the virtual channel name at the corresponding position of the virtualChannels parameter. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-setdevicepowerupstate__string-string_arr1-digitalpulluppulldownresistorstate_arr1.html language=enus -->
## TOPIC 01602: SetDevicePowerUpState(string, string[], DigitalPullUpPullDownResistorState[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-setdevicepowerupstate__string-string_arr1-digitalpulluppulldownresistorstate_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-setdevicepowerupstate__string-string_arr1-digitalpulluppulldownresistorstate_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the resistor level for lines when they are in tristate logic. SyntaxNamespace: NationalInstruments.DAQmxpublic void SetDevicePowerUpState(string deviceName, string[] channels, DigitalPullUpPullDownResistorState[] states)ParametersNameTypeDescriptiondeviceNamestringThe name, as configured in Mea

### SetDevicePowerUpState(string, string[], DigitalPullUpPullDownResistorState[])

Sets the resistor level for lines when they are in tristate logic.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void SetDevicePowerUpState(string deviceName, string[] channels, DigitalPullUpPullDownResistorState[] states)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deviceName | string | The name, as configured in Measurement & Automation Explorer (MAX), of the device to which this operation applies. |
| channels | string[] | The digital line or port to modify. You cannot modify dedicated digital input lines. |
| states | DigitalPullUpPullDownResistorState[] | The pull up pull down level set for the physical channel specified with DigitalPullUpPullDownResistorState. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-setdevicepowerupstate__string-string_arr1-double_arr1-string_arr1-double_arr1.html language=enus -->
## TOPIC 01603: SetDevicePowerUpState(string, string[], double[], string[], double[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-setdevicepowerupstate__string-string_arr1-double_arr1-string_arr1-double_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-setdevicepowerupstate__string-string_arr1-double_arr1-string_arr1-double_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Updates the power up states to which to set analog physical channels on a device when the device powers up or when you reset the device. SyntaxNamespace: NationalInstruments.DAQmxpublic void SetDevicePowerUpState(string deviceName, string[] voltageChannels, double[] voltageValues, string[] currentCh

### SetDevicePowerUpState(string, string[], double[], string[], double[])

Updates the [power up states](/csh?context=nidaqmx_mxdevconsid_initstates) to which to set analog physical channels on a device when the device powers up or when you reset the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void SetDevicePowerUpState(string deviceName, string[] voltageChannels, double[] voltageValues, string[] currentChannels, double[] currentValues)

#### Remarks

Power up states are stored in EEPROMs that you can write to only a limited number of times. Therefore, you should use this method as infrequently as possible. This method writes to the EEPROM only if a setting you request is different from the one currently stored on the EEPROM. This method writes power up states in the sequential order of the power up states array. Therefore, any physical channels with multiple entries in that array use the highest array index.

When you call this method, you can choose to not set either voltages or currents by passing in null for the voltage or current parameters, but not both.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deviceName | string | The name, as configured in Measurement & Automation Explorer (MAX), of the device to which this operation applies. |
| voltageChannels | string[] | The voltage channels for which to set new power up values. Each value in this array specifies a virtual channel string that is assigned the voltage at the corresponding position in the voltageValues parameter. You can set voltage power up states only for physical channels that support voltage output. |
| voltageValues | double[] | The voltages to set. Each value in this array applies to the virtual channel name at the corresponding position of the voltageChannels parameter. You can set voltage power up states only for physical channels that support voltage output. |
| currentChannels | string[] | The current channels for which to set new power up values. Each value in this array specifies a virtual channel string that is assigned the current at the corresponding position in the currentValues parameter. You can set current power up states only for physical channels that support current output. |
| currentValues | double[] | The currents to set. Each value in this array applies to the virtual channel name at the corresponding position of the currentChannels parameter. You can set current power up states only for physical channels that support current output. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-setlogicfamilypowerupstate__string-logicfamily.html language=enus -->
## TOPIC 01604: SetLogicFamilyPowerUpState(string, LogicFamily)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-setlogicfamilypowerupstate__string-logicfamily.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-setlogicfamilypowerupstate__string-logicfamily.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the digital logic family to use when the device powers up. SyntaxNamespace: NationalInstruments.DAQmxpublic void SetLogicFamilyPowerUpState(string deviceName, LogicFamily logicFamily)RemarksPower-up states are stored in non-volatile memory that you can write to only a limited number of times. T

### SetLogicFamilyPowerUpState(string, LogicFamily)

Sets the digital logic family to use when the device powers up.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void SetLogicFamilyPowerUpState(string deviceName, LogicFamily logicFamily)

#### Remarks

Power-up states are stored in non-volatile memory that you can write to only a limited number of times. Therefore, you should use this function as infrequently as possible. This function writes to the non-volatile memory only if a setting you request is different from the one currently stored on the non-volatile memory.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deviceName | string | The name, as configured in Measurement & Automation Explorer (MAX), of the device to which this operation applies. |
| logicFamily | LogicFamily | The logic family to set the device to when it powers up. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to device documentation for information on the logic high and logic low voltages for these logic families. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-switchchannels.html language=enus -->
## TOPIC 01605: SwitchChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-switchchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-switchchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This property is obsolete. Will warn if used Gets an array that contains the switch channel names of devices installed in the system. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] SwitchChannels { get; }RemarksAn array of String that contains the switch channel names of devices

### SwitchChannels

**Obsolete: This property is obsolete. Will warn if used** 
Gets an array that contains the [switch channel names](/csh?context=nidaqmx_mxcncpts_switchchanstrings) of devices installed in the system.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] SwitchChannels { get; }

#### Remarks

An array of String that contains the switch channel names of devices installed in the system.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-switchfindpath__string-string.html language=enus -->
## TOPIC 01606: SwitchFindPath(string, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-switchfindpath__string-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-switchfindpath__string-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This method is obsolete. Will warn if used Returns information about the path between two switch channels. SyntaxNamespace: NationalInstruments.DAQmxpublic string SwitchFindPath(string switchChannel1, string switchChannel2)ParametersNameTypeDescriptionswitchChannel1stringThe first channel

### SwitchFindPath(string, string)

**Obsolete: This method is obsolete. Will warn if used** 
Returns information about the path between two switch channels.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string SwitchFindPath(string switchChannel1, string switchChannel2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| switchChannel1 | string | The first channel in the connection. |
| switchChannel2 | string | The second channel in the connection. |

#### Returns

If the channels are connected, this method returns the path by which they are connected. If the channels are not connected, the method returns a path by which they can be connected, if one is available.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-switchrelays.html language=enus -->
## TOPIC 01607: SwitchRelays

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-switchrelays.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-switchrelays.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This property is obsolete. Will warn if used Gets an array that contains the switch relay names of devices installed in the system. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] SwitchRelays { get; }RemarksAn array of String that contains the switch relay names of devices insta

### SwitchRelays

**Obsolete: This property is obsolete. Will warn if used** 
Gets an array that contains the [switch relay names](/csh?context=nidaqmx_mxcncpts_switchchanstrings) of devices installed in the system.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] SwitchRelays { get; }

#### Remarks

An array of String that contains the switch relay names of devices installed in the system.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-switchtopologies.html language=enus -->
## TOPIC 01608: SwitchTopologies

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-switchtopologies.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-switchtopologies.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This property is obsolete. Will warn if used Gets an array containing the names of all switch topologies. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] SwitchTopologies { get; }RemarksAn array of String that contains the names of all switch topologies.ExceptionsTypeDescriptionN

### SwitchTopologies

**Obsolete: This property is obsolete. Will warn if used** 
Gets an array containing the names of all [switch topologies](/csh?context=nidaqmx_mxcncpts_topology).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] SwitchTopologies { get; }

#### Remarks

An array of String that contains the names of all switch topologies.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-synchronizecallbacks.html language=enus -->
## TOPIC 01609: SynchronizeCallbacks

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-synchronizecallbacks.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-synchronizecallbacks.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how events and callback delegates are invoked. SyntaxNamespace: NationalInstruments.DAQmxpublic bool SynchronizeCallbacks { get; set; }RemarksIn some cases, callbacks and event handlers are executed in a different thread than the rest of the program. Therefore, you must take special care w

### SynchronizeCallbacks

Specifies how events and callback delegates are invoked.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool SynchronizeCallbacks { get; set; }

#### Remarks

In some cases, callbacks and event handlers are executed in a different thread than the rest of the program. Therefore, you must take special care when accessing objects that have thread affinity, such as UI controls, from these callbacks and event handlers. For more information, refer to Events, Callbacks, and Thread Safety in Measurement Studio .NET Class Libraries.

Reading and Writing with NI-DAQmx Streams

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-synchronizingobject.html language=enus -->
## TOPIC 01610: SynchronizingObject

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-synchronizingobject.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-synchronizingobject.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will warn if used Gets or sets the object that marshals event-handler and callback calls. SyntaxNamespace: NationalInstruments.DAQmxpublic ISynchronizeInvoke SynchronizingObject { get; set;

### SynchronizingObject

**Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will warn if used** 
Gets or sets the object that marshals event-handler and callback calls.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public ISynchronizeInvoke SynchronizingObject { get; set; }

#### Remarks

The ISynchronizeInvoke representing the object that marshals the event-handler and callback calls. The default value is null.

null

Note

For more information, refer to Events, Callbacks, and Thread Safety in Measurement Studio .NET Class Libraries.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-tasks.html language=enus -->
## TOPIC 01611: Tasks

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-tasks.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-tasks.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates an array that contains the names of all tasks saved on the system. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] Tasks { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of

### Tasks

Indicates an array that contains the names of all tasks saved on the system.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] Tasks { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-tristateoutputterminal__string.html language=enus -->
## TOPIC 01612: TristateOutputTerminal(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-tristateoutputterminal__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-tristateoutputterminal__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a terminal to high-impedance state. SyntaxNamespace: NationalInstruments.DAQmxpublic void TristateOutputTerminal(string outputTerminal)RemarksIf you connect an external signal to a terminal on the I/O connector, the terminal must be in high-impedance state. Otherwise, the device could double-dr

### TristateOutputTerminal(string)

Sets a terminal to [high-impedance state](/csh?context=nidaqmx_mxcncpts_tristating).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void TristateOutputTerminal(string outputTerminal)

#### Remarks

If you connect an external signal to a terminal on the I/O connector, the terminal must be in high-impedance state. Otherwise, the device could double-drive the terminal and damage the hardware. If you call this method on a terminal in an active route, the method fails and reports no error back to the user.

[Reset](nationalinstruments-daqmx-device-reset.html) sets all terminals on the I/O connector to high-impedance state, but also clears any active tasks associated with the device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | string | The terminal on the I/O connector to set to high-impedance state. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem-writeidpinmemory__string-string-byte_arr1-uint.html language=enus -->
## TOPIC 01613: WriteIDPinMemory(string, string, byte[], uint)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem-writeidpinmemory__string-string-byte_arr1-uint.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem-writeidpinmemory__string-string-byte_arr1-uint.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes provided bitstream and format code to the memory connected to selected ID Pin. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteIDPinMemory(string deviceName, string idPinName, byte[] data, uint formatCode)ParametersNameTypeDescriptiondeviceNamestringThe name, as configured in Measu

### WriteIDPinMemory(string, string, byte[], uint)

Writes provided bitstream and format code to the memory connected to selected ID Pin.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteIDPinMemory(string deviceName, string idPinName, byte[] data, uint formatCode)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deviceName | string | The name, as configured in Measurement & Automation Explorer (MAX), of the device to which this operation applies. |
| idPinName | string | The name, as obtained from Identification.ID Pin.Pin Names in DAQmxDevice Attributes, of the ID Pin to which this operation applies. |
| data | byte[] | A byte array of raw data to write to the memory. |
| formatCode | uint | A byte indicating the format of the data to write to the memory. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqSystem Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqsystem.html language=enus -->
## TOPIC 01614: DaqSystem Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqsystem.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqsystem.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains methods that access tasks, scales, and global channels stored in Measurement & Automation Explorer (MAX), performs immediate operations on DAQ hardware, and creates classes from which you can get information about the hardware. Derives fromMarshalByRefObjectISynchronizeCallbacksISupportSync

### DaqSystem Class

Contains methods that access tasks, scales, and global channels stored in Measurement & Automation Explorer (MAX), performs immediate operations on DAQ hardware, and creates classes from which you can get information about the hardware.

#### Derives from

- MarshalByRefObject
- ISynchronizeCallbacks
- ISupportSynchronizationContext

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class DaqSystem : MarshalByRefObject, ISynchronizeCallbacks, ISupportSynchronizationContext

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

DaqSystem

DaqSystem

Local

DaqSystem

DaqSystem

```text
'Print the name of each task saved in MAX to the consoleFor Each taskName As string In DaqSystem.Local.TasksConsole.WriteLine(taskName)Next
```

```text
//Print the name of each task saved in MAX to the consoleforeach (string taskName in DaqSystem.Local.Tasks){Console.WriteLine(taskName);}
```

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Devices | Indicates the names of all devices installed in the system. |
| DriverMajorVersion | Indicates the major portion of the installed version of NI-DAQmx, such as 7 for version 7.0. |
| DriverMinorVersion | Indicates the minor portion of the installed version of NI-DAQmx, such as 0 for version 7.0. |
| DriverUpdateVersion | Indicates the update portion of the installed version of NI-DAQmx, such as 1 for version 9.0.1. |
| GlobalChannels | Indicates an array that contains the names of all global channels saved on the system. |
| IsReadOrWriteLate | Obsolete: The IsReadOrWriteLate property is deprecated. Please use the Timing.SinglePoint.WaitForNextSampleClock method instead. Will warn if usedDetermines if a hardware-timed single-point read or write operation is overdue on the current thread. The IsReadOrWriteLate property has been deprecated in favor of the WaitForNextSampleClock(double) method. |
| LastDaqWarning | Gets the DaqWarningEventArgs for the last DaqWarning event that occurred. |
| Local | Gets an instance of the DaqSystem class that represents the local DAQ system. |
| Scales | Indicates an array that contains the names of all custom scales saved on the system. |
| SwitchChannels | Obsolete: This property is obsolete. Will warn if usedGets an array that contains the switch channel names of devices installed in the system. |
| SwitchRelays | Obsolete: This property is obsolete. Will warn if usedGets an array that contains the switch relay names of devices installed in the system. |
| SwitchTopologies | Obsolete: This property is obsolete. Will warn if usedGets an array containing the names of all switch topologies. |
| SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |
| SynchronizingObject | Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will warn if usedGets or sets the object that marshals event-handler and callback calls. |
| Tasks | Indicates an array that contains the names of all tasks saved on the system. |

#### Methods

| Name | Description |
| --- | --- |
| AddCDaqSynchronizationConnection(string) | Adds a cDAQ Sync connection between devices. The connection is not verified. |
| AddNetworkDevice(string, string, bool, double) | Adds a Network cDAQ device to the system and, if specified, attempts to reserve it. |
| AddNetworkDevice(string, string, double) | Adds a Network cDAQ device to the system. This method does not attempt to reserve the device after the device is successfully added. |
| AutoConfigureCDaqSynchronizationConnections(string, double) | Detects and configures cDAQ Sync connections between devices. |
| ClearLastDaqWarning() | Clears the value of the LastDaqWarning property, by setting the error code to zero and the error string to a blank string. |
| CloseSwitchRelays(string, bool) | Obsolete: This method is obsolete. Will warn if usedCloses the specified relays. |
| ConnectSwitchChannels(string, string, bool) | Obsolete: This method is obsolete. Will warn if usedMakes a connection between two switch channels. |
| ConnectSwitchChannels(string, bool) | Obsolete: This method is obsolete. Will warn if usedMakes one or more connections between switch channels as specified by the connection list. |
| ConnectTerminals(string, string) | Creates a route between a source and destination terminal. |
| ConnectTerminals(string, string, SignalRoutingModifiers) | Creates a route between a source and destination terminal with the specified signal modification. |
| CreateSwitchScanTask(string, string) | Obsolete: This method is obsolete. Will warn if usedCreates a new switch scanning task with the sequence specified in the scan list. |
| CreateWatchdogTimerTask(string, string, double, string[], WatchdogDOExpirationState[]) | Creates a task to configure and control the watchdog timer of a static DIO device. The timer activates when you start the task. |
| DeleteGlobalChannel(string) | Deletes the specified global channel that is stored in Measurement & Automation Explorer (MAX). |
| DeleteScale(string) | Deletes the specified custom scale that is stored in Measurement & Automation Explorer (MAX). |
| DeleteTask(string) | Deletes the specified task that is stored in Measurement & Automation Explorer (MAX). |
| DisconnectAll(string, bool) | Obsolete: This method is obsolete. Will warn if usedTerminates all active connections on the device, which places the relays into the topology reset state. |
| DisconnectSwitchChannels(string, string, bool) | Obsolete: This method is obsolete. Will warn if usedTerminates a connection between two channels. |
| DisconnectSwitchChannels(string, bool) | Obsolete: This method is obsolete. Will warn if usedTerminates one or more connections between switch channels as specified by the disconnection list. |
| DisconnectTerminals(string, string) | Removes signal routes you created by using ConnectTerminals(string, string, SignalRoutingModifiers). |
| GetAnalogPowerUpStatesWithOutputType(string, out double[], out AOPowerUpOutputBehavior[]) | Gets the states that analog physical channels on a device are set to when the device powers up or when the device is reset. |
| GetDevicePowerUpState(string, out string[], out double[], out string[], out double[]) | Gets the power up states for analog physical channels. |
| GetDevicePowerUpState(string, out string[], out DigitalPullUpPullDownResistorState[]) | Gets the resistor level for lines when they are in tristate logic. |
| GetDevicePowerUpState(string, out string[], out DigitalPowerUpState[]) | Gets the power up states for digital physical lines. |
| GetDisconnectedCDaqSynchronizationPorts(string, double, out bool) | Verifies configured cDAQ Sync connections between devices. |
| GetLogicFamilyPowerUpState(string) | Gets the digital logic family for a device. |
| GetPhysicalChannels(PhysicalChannelTypes, PhysicalChannelAccess) | Gets an array that contains the physical channel names of devices installed in the system. |
| GetSavedChannelInfo(string) | Creates a SavedChannelInfo object that you can use to retrieve information about the specified global channel stored in Measurement & Automation Explorer (MAX). |
| GetSavedScaleInfo(string) | Creates a SavedScaleInfo object that you can use to retrieve information about the specified custom scale stored in Measurement & Automation Explorer (MAX). |
| GetSavedTaskInfo(string) | Creates a SavedTaskInfo object that you can use to retrieve information about the specified task stored in Measurement & Automation Explorer (MAX). |
| GetSwitchRelayCount(string) | Obsolete: This method is obsolete. Will warn if usedReturns the number of times a relay has actuated on switches that support querying the relay count. |
| GetSwitchRelayCounts(string) | Obsolete: This method is obsolete. Will warn if usedReturns the number of times a set of relays have actuated. |
| GetSwitchRelayPosition(string) | Obsolete: This method is obsolete. Will warn if usedReturns the current position of a single relay. |
| GetSwitchRelayPositions(string) | Obsolete: This method is obsolete. Will warn if usedReturns the current position of a set of relays. |
| GetTerminals(TerminalTypes) | Gets an array that contains the terminal names of devices installed in the system. |
| LoadDevice(string) | Creates a Device that you can use to control the specified device or get information about that device. |
| LoadPhysicalChannel(string) | Creates a PhysicalChannel that you can use to configure and retrieve TEDS information for the specified physical channel. |
| LoadScale(string) | Loads a scale that is stored in Measurement & Automation Explorer (MAX). |
| LoadSwitchChannel(string) | Obsolete: This method is obsolete. Will warn if usedCreates a SwitchChannel that you can use to get the switch channel capabilities and set the usage type for the switch channel. |
| LoadTask(string) | Loads a task that is stored in Measurement & Automation Explorer (MAX). |
| OpenSwitchRelays(string, bool) | Obsolete: This method is obsolete. Will warn if usedOpens the specified relays. |
| ReadIDPinMemory(string, string, out byte[], out uint) | Reads bitstream and format code from the memory connected to selected ID Pin. |
| RemoveCDaqSynchronizationConnection(string) | Removes a cDAQ Sync connection between devices. The connection is not verified. |
| SaveGlobalChannel(Channel, string, SaveOptions) | Saves the specified local or global channel to Measurement & Automation Explorer (MAX) as a global channel, under the virtual name it was given when it was created and with specified author and options values. |
| SaveGlobalChannel(Channel) | Saves the specified local or global channel to Measurement & Automation Explorer (MAX) as a global channel, under the virtual name it was given when it was created. |
| SaveGlobalChannelAs(Channel, string, string, SaveOptions) | Saves the local or global channel to Measurement & Automation Explorer (MAX) as a global channel, under the specified name and specified author and options values. |
| SaveGlobalChannelAs(Channel, string) | Saves the local or global channel to Measurement & Automation Explorer (MAX) as a global channel, under the specified name. |
| SaveScale(Scale) | Saves the specified custom scale to Measurement & Automation Explorer (MAX) under the name it was given when it was created. |
| SaveScale(Scale, string, SaveOptions) | Saves the specified custom scale to Measurement & Automation Explorer (MAX) under the name it was given when it was created and with specified author and options values. |
| SaveScaleAs(Scale, string, string, SaveOptions) | Saves the specified custom scale to Measurement & Automation Explorer (MAX) under the specified name and with specified author and options values. |
| SaveScaleAs(Scale, string) | Saves the specified custom scale to Measurement & Automation Explorer (MAX) under the specified name. |
| SaveTask(Task, string, SaveOptions) | Saves the specified task and any local channels it contains to Measurement & Automation Explorer (MAX) under the name it was given when it was created, with specifed author and options values. |
| SaveTask(Task) | Saves the specified task and any local channels it contains to Measurement & Automation Explorer (MAX) under the name it was given when it was created. |
| SaveTaskAs(Task, string) | Saves the task and any local channels it contains to Measurement & Automation Explorer (MAX) under the specified name. |
| SaveTaskAs(Task, string, string, SaveOptions) | Saves the task and any local channels it contains to Measurement & Automation Explorer (MAX) under the specified name and with specified author and options values. |
| SetAnalogPowerUpStatesWithOutputType(string, double[], AOPowerUpOutputBehavior[]) | Sets the states that analog physical channels on a device are set to when the device powers up or when the device is reset. |
| SetDevicePowerUpState(string, string[], double[], string[], double[]) | Updates the power up states to which to set analog physical channels on a device when the device powers up or when you reset the device. |
| SetDevicePowerUpState(string, string[], DigitalPullUpPullDownResistorState[]) | Sets the resistor level for lines when they are in tristate logic. |
| SetDevicePowerUpState(string, string[], DigitalPowerUpState[]) | Updates the power up states to which to set digital physical channels on a device when the device powers up or when you reset the device. |
| SetLogicFamilyPowerUpState(string, LogicFamily) | Sets the digital logic family to use when the device powers up. |
| SwitchFindPath(string, string) | Obsolete: This method is obsolete. Will warn if usedReturns information about the path between two switch channels. |
| TristateOutputTerminal(string) | Sets a terminal to high-impedance state. |
| WriteIDPinMemory(string, string, byte[], uint) | Writes provided bitstream and format code to the memory connected to selected ID Pin. |

#### Events

| Name | Description |
| --- | --- |
| DaqWarning | Occurs when the NI-DAQmx driver issues a warning. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqwarningeventargs-error.html language=enus -->
## TOPIC 01615: Error

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqwarningeventargs-error.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqwarningeventargs-error.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the NI-DAQmx driver code for the warning that occurred. Zero means no warning occurred. SyntaxNamespace: NationalInstruments.DAQmxpublic int Error { get; }RemarksThe NI-DAQmx driver code for the warning that occurred.Refer to NI-DAQmx Driver Error Codes for a list of possible values. NI-DAQmx D

### Error

Gets the NI-DAQmx driver code for the warning that occurred. Zero means no warning occurred.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int Error { get; }

#### Remarks

The NI-DAQmx driver code for the warning that occurred.

Refer to [NI-DAQmx Driver Error Codes](https://#) for a list of possible values.

NI-DAQmx Driver Error Codes

Parent topic:

DaqWarningEventArgs Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqwarningeventargs-getobjectdata__serializationinfo-streamingcontext.html language=enus -->
## TOPIC 01616: GetObjectData(SerializationInfo, StreamingContext)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqwarningeventargs-getobjectdata__serializationinfo-streamingcontext.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqwarningeventargs-getobjectdata__serializationinfo-streamingcontext.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the SerializationInfo object with information about the exception. SyntaxNamespace: NationalInstruments.DAQmxprotected void GetObjectData(SerializationInfo info, StreamingContext context)ParametersNameTypeDescriptioninfoSerializationInfoObject that holds the serialized object data.contextStream

### GetObjectData(SerializationInfo, StreamingContext)

Sets the SerializationInfo object with information about the exception.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

protected void GetObjectData(SerializationInfo info, StreamingContext context)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| info | SerializationInfo | Object that holds the serialized object data. |
| context | StreamingContext | Contextual information about the source or destination. |

Parent topic:

DaqWarningEventArgs Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqwarningeventargs-message.html language=enus -->
## TOPIC 01617: Message

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqwarningeventargs-message.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqwarningeventargs-message.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a message that describes the warning. SyntaxNamespace: NationalInstruments.DAQmxpublic string Message { get; }RemarksA message that describes the warning.

### Message

Gets a message that describes the warning.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Message { get; }

#### Remarks

A message that describes the warning.

Parent topic:

DaqWarningEventArgs Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqwarningeventargs-tostring.html language=enus -->
## TOPIC 01618: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqwarningeventargs-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqwarningeventargs-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString. ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

#### Remarks

Overrides ToString.

#### Returns

A string representation of the object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqWarningEventArgs Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqwarningeventargs.html language=enus -->
## TOPIC 01619: DaqWarningEventArgs Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqwarningeventargs.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqwarningeventargs.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides data for the DaqWarning event. Derives fromEventArgsISerializableSyntaxNamespace: NationalInstruments.DAQmxpublic class DaqWarningEventArgs : EventArgs, ISerializableRemarksExample applications are located in the <Public Documents>\National Instruments\NI-DAQ\Examples\DotNET4.x directory or

### DaqWarningEventArgs Class

Provides data for the [DaqWarning](nationalinstruments-daqmx-daqsystem-daqwarning.html) event.

#### Derives from

- EventArgs
- ISerializable

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class DaqWarningEventArgs : EventArgs, ISerializable

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Error | Gets the NI-DAQmx driver code for the warning that occurred. Zero means no warning occurred. |
| Message | Gets a message that describes the warning. |

#### Methods

| Name | Description |
| --- | --- |
| ToString() | Returns a string representation of the object. |
| GetObjectData(SerializationInfo, StreamingContext) | Sets the SerializationInfo object with information about the exception. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqwarningeventhandler__object-daqwarningeventargs.html language=enus -->
## TOPIC 01620: DaqWarningEventHandler Delegate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqwarningeventhandler__object-daqwarningeventargs.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqwarningeventhandler__object-daqwarningeventargs.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the method that handles the DaqWarning event. SyntaxNamespace: NationalInstrumentspublic delegate void DaqWarningEventHandler(object sender, DaqWarningEventArgs e)ParametersNameTypeDescriptionsenderobjectThe source of the event.eDaqWarningEventArgsA DaqWarningEventArgs object that contain

### DaqWarningEventHandler Delegate

Represents the method that handles the [DaqWarning](nationalinstruments-daqmx-daqsystem-daqwarning.html) event.

#### Syntax

**Namespace:**NationalInstruments

public delegate void DaqWarningEventHandler(object sender, DaqWarningEventArgs e)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sender | object | The source of the event. |
| e | DaqWarningEventArgs | A DaqWarningEventArgs object that contains the event data. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dataactiveeventlevelactivelevel.html language=enus -->
## TOPIC 01621: DataActiveEventLevelActiveLevel Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dataactiveeventlevelactivelevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dataactiveeventlevelactivelevel.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of the exported Data Active Event. SyntaxNamespace: NationalInstruments.DAQmxpublic enum DataActiveEventLevelActiveLevelRemarksSpecifies the polarity of the exported Data Active Event. Use this enumeration to get or set the value of DataActiveEventLevelActiveLevel.MembersNameV

### DataActiveEventLevelActiveLevel Enumeration

Specifies the polarity of the exported Data Active Event.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum DataActiveEventLevelActiveLevel

#### Remarks

Specifies the polarity of the exported Data Active Event. Use this enumeration to get or set the value of [DataActiveEventLevelActiveLevel](nationalinstruments-daqmx-exportsignals-dataactiveeventlevelactivelevel.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ActiveHigh | 10095 | High state is the active state. |
| ActiveLow | 10096 | Low state is the active state. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-delayfromsampleclockunits.html language=enus -->
## TOPIC 01622: DelayFromSampleClockUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-delayfromsampleclockunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-delayfromsampleclockunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of DelayFromSampleClock. SyntaxNamespace: NationalInstruments.DAQmxpublic enum DelayFromSampleClockUnitsRemarksSpecifies the units of DelayFromSampleClock. Use this enumeration to get or set the value of DelayFromSampleClockUnits.MembersNameValueDescriptionSeconds10364Seconds. Ti

### DelayFromSampleClockUnits Enumeration

Specifies the units of [DelayFromSampleClock](nationalinstruments-daqmx-timing-delayfromsampleclock.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum DelayFromSampleClockUnits

#### Remarks

Specifies the units of [DelayFromSampleClock](nationalinstruments-daqmx-timing-delayfromsampleclock.html). Use this enumeration to get or set the value of [DelayFromSampleClockUnits](nationalinstruments-daqmx-timing-delayfromsampleclockunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Seconds | 10364 | Seconds. |
| Ticks | 10304 | Timebase ticks. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-accessoryconnectioncount.html language=enus -->
## TOPIC 01623: AccessoryConnectionCount

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-accessoryconnectioncount.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-accessoryconnectioncount.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of times a particular connection that results in tangible wear and tear of onboard components has been made on the accessory. This connection count is useful for tracking accessory life and usage. SyntaxNamespace: NationalInstruments.DAQmxpublic long AccessoryConnectionCount { g

### AccessoryConnectionCount

Specifies the number of times a particular connection that results in tangible wear and tear of onboard components has been made on the accessory. This connection count is useful for tracking accessory life and usage.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long AccessoryConnectionCount { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-accessoryproductnumbers.html language=enus -->
## TOPIC 01624: AccessoryProductNumbers

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-accessoryproductnumbers.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-accessoryproductnumbers.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the unique hardware identification number for accessories connected to the device. Each array element corresponds to a connector. For example, index 0 corresponds to connector 0. The array contains 0 for each connector with no accessory connected. SyntaxNamespace: NationalInstruments.DAQmx

### AccessoryProductNumbers

Indicates the unique hardware identification number for accessories connected to the device. Each array element corresponds to a connector. For example, index 0 corresponds to connector 0. The array contains 0 for each connector with no accessory connected.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long[] AccessoryProductNumbers { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-accessoryproducttypes.html language=enus -->
## TOPIC 01625: AccessoryProductTypes

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-accessoryproducttypes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-accessoryproducttypes.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the model names of accessories connected to the device. Each array element corresponds to a connector. For example, index 0 corresponds to connector 0. The array contains an empty string for each connector with no accessory connected. SyntaxNamespace: NationalInstruments.DAQmxpublic string

### AccessoryProductTypes

Indicates the model names of accessories connected to the device. Each array element corresponds to a connector. For example, index 0 corresponds to connector 0. The array contains an empty string for each connector with no accessory connected.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] AccessoryProductTypes { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-accessoryserialnumbers.html language=enus -->
## TOPIC 01626: AccessorySerialNumbers

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-accessoryserialnumbers.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-accessoryserialnumbers.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the serial number for accessories connected to the device. Each array element corresponds to a connector. For example, index 0 corresponds to connector 0. The array contains 0 for each connector with no accessory connected. SyntaxNamespace: NationalInstruments.DAQmxpublic long[] AccessoryS

### AccessorySerialNumbers

Indicates the serial number for accessories connected to the device. Each array element corresponds to a connector. For example, index 0 corresponds to connector 0. The array contains 0 for each connector with no accessory connected.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long[] AccessorySerialNumbers { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aibridgeranges.html language=enus -->
## TOPIC 01627: AIBridgeRanges

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aibridgeranges.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aibridgeranges.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates pairs of input voltage ratio ranges, in volts per volt, supported by devices that acquire using ratiometric measurements. Each pair consists of the low value followed by the high value. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] AIBridgeRanges { get; }RemarksThis property re

### AIBridgeRanges

Indicates pairs of input voltage ratio ranges, in volts per volt, supported by devices that acquire using ratiometric measurements. Each pair consists of the low value followed by the high value.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] AIBridgeRanges { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aichargeranges.html language=enus -->
## TOPIC 01628: AIChargeRanges

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aichargeranges.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aichargeranges.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in coulombs pairs of input charge ranges for the device. Each pair consists of the low value followed by the high value. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] AIChargeRanges { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property wit

### AIChargeRanges

Indicates in coulombs pairs of input charge ranges for the device. Each pair consists of the low value followed by the high value.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] AIChargeRanges { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aicouplings.html language=enus -->
## TOPIC 01629: AICouplings

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aicouplings.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aicouplings.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the coupling types supported by this device. SyntaxNamespace: NationalInstruments.DAQmxpublic CouplingTypes AICouplings { get; }RemarksA CouplingTypes that indicates the coupling types supported by this device. The value is a bitwise combination of AC, DC, Ground, and None.ExceptionsTypeDe

### AICouplings

Indicates the coupling types supported by this device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CouplingTypes](nationalinstruments-daqmx-couplingtypes.html) AICouplings { get; }

#### Remarks

A [CouplingTypes](nationalinstruments-daqmx-couplingtypes.html) that indicates the coupling types supported by this device. The value is a bitwise combination of [AC](nationalinstruments-daqmx-couplingtypes.html), [DC](nationalinstruments-daqmx-couplingtypes.html), [Ground](nationalinstruments-daqmx-couplingtypes.html), and [None](nationalinstruments-daqmx-couplingtypes.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aicurrentinternalexcitationdiscretevalues.html language=enus -->
## TOPIC 01630: AICurrentInternalExcitationDiscreteValues

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aicurrentinternalexcitationdiscretevalues.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aicurrentinternalexcitationdiscretevalues.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the set of discrete internal current excitation values supported by this device. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] AICurrentInternalExcitationDiscreteValues { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loo

### AICurrentInternalExcitationDiscreteValues

Indicates the set of discrete internal current excitation values supported by this device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] AICurrentInternalExcitationDiscreteValues { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aicurrentranges.html language=enus -->
## TOPIC 01631: AICurrentRanges

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aicurrentranges.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aicurrentranges.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the pairs of current input ranges supported by this device. Each pair consists of the low value, followed by the high value. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] AICurrentRanges { get; }RemarksThis property returns a copy of the actual array. Avoid calling this propert

### AICurrentRanges

Indicates the pairs of current input ranges supported by this device. Each pair consists of the low value, followed by the high value.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] AICurrentRanges { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aifrequencyranges.html language=enus -->
## TOPIC 01632: AIFrequencyRanges

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aifrequencyranges.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aifrequencyranges.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the pairs of frequency input ranges supported by this device. Each pair consists of the low value, followed by the high value. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] AIFrequencyRanges { get; }RemarksThis property returns a copy of the actual array. Avoid calling this pro

### AIFrequencyRanges

Indicates the pairs of frequency input ranges supported by this device. Each pair consists of the low value, followed by the high value.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] AIFrequencyRanges { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aigains.html language=enus -->
## TOPIC 01633: AIGains

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aigains.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aigains.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the input gain settings supported by this device. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] AIGains { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid

### AIGains

Indicates the input gain settings supported by this device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] AIGains { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aimaximummultichannelrate.html language=enus -->
## TOPIC 01634: AIMaximumMultiChannelRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aimaximummultichannelrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aimaximummultichannelrate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the maximum sampling rate for an analog input task from this device. To find the maximum rate for the task, take the minimum of AIMaximumSingleChannelRate or the indicated sampling rate of this device divided by the number of channels to acquire data from (including cold-junction compensat

### AIMaximumMultiChannelRate

Indicates the maximum sampling rate for an analog input task from this device. To find the maximum rate for the task, take the minimum of [AIMaximumSingleChannelRate](nationalinstruments-daqmx-device-aimaximumsinglechannelrate.html) or the indicated sampling rate of this device divided by the number of channels to acquire data from (including cold-junction compensation and autozero channels).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double AIMaximumMultiChannelRate { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aimaximumsinglechannelrate.html language=enus -->
## TOPIC 01635: AIMaximumSingleChannelRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aimaximumsinglechannelrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aimaximumsinglechannelrate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the maximum rate for an analog input task if the task contains only a single channel from this device. SyntaxNamespace: NationalInstruments.DAQmxpublic double AIMaximumSingleChannelRate { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an e

### AIMaximumSingleChannelRate

Indicates the maximum rate for an analog input task if the task contains only a single channel from this device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double AIMaximumSingleChannelRate { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aiminimumrate.html language=enus -->
## TOPIC 01636: AIMinimumRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aiminimumrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aiminimumrate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the minimum rate for an analog input task on this device. NI-DAQmx returns a warning or error if you attempt to sample at a slower rate. SyntaxNamespace: NationalInstruments.DAQmxpublic double AIMinimumRate { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx

### AIMinimumRate

Indicates the minimum rate for an analog input task on this device. NI-DAQmx returns a warning or error if you attempt to sample at a slower rate.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double AIMinimumRate { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-ainumberofsampletimingengines.html language=enus -->
## TOPIC 01637: AINumberOfSampleTimingEngines

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-ainumberofsampletimingengines.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-ainumberofsampletimingengines.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of Analog Input sample timing engines supported by the device. SyntaxNamespace: NationalInstruments.DAQmxpublic long AINumberOfSampleTimingEngines { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AINumberOfSampleTimingEngines

Indicates the number of Analog Input sample timing engines supported by the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long AINumberOfSampleTimingEngines { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-ainumberofsynchronizationpulsesources.html language=enus -->
## TOPIC 01638: AINumberOfSynchronizationPulseSources

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-ainumberofsynchronizationpulsesources.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-ainumberofsynchronizationpulsesources.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of Analog Input synchronization pulse sources supported by the device. SyntaxNamespace: NationalInstruments.DAQmxpublic long AINumberOfSynchronizationPulseSources { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AINumberOfSynchronizationPulseSources

Indicates the number of Analog Input synchronization pulse sources supported by the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long AINumberOfSynchronizationPulseSources { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aiphysicalchannels.html language=enus -->
## TOPIC 01639: AIPhysicalChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aiphysicalchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aiphysicalchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates an array containing the names of the analog input physical channels available on the device. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] AIPhysicalChannels { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because i

### AIPhysicalChannels

Indicates an array containing the names of the analog input physical channels available on the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] AIPhysicalChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aisamplemodes.html language=enus -->
## TOPIC 01640: AISampleModes

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aisamplemodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aisamplemodes.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the sample modes from devices that support sample clocked analog input. SyntaxNamespace: NationalInstruments.DAQmxpublic SampleQuantityMode[] AISampleModes { get; }RemarksThe values of the supported SampleQuantityMode of the device. Reading and Writing with NI-DAQmx Streams

### AISampleModes

Gets the sample modes from devices that support sample clocked analog input.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SampleQuantityMode](nationalinstruments-daqmx-samplequantitymode.html)[] AISampleModes { get; }

#### Remarks

The values of the supported [SampleQuantityMode](nationalinstruments-daqmx-samplequantitymode.html) of the device.

Reading and Writing with NI-DAQmx Streams

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aisimultaneoussamplingsupported.html language=enus -->
## TOPIC 01641: AISimultaneousSamplingSupported

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aisimultaneoussamplingsupported.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aisimultaneoussamplingsupported.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device supports simultaneous sampling. SyntaxNamespace: NationalInstruments.DAQmxpublic bool AISimultaneousSamplingSupported { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AISimultaneousSamplingSupported

Indicates if the device supports simultaneous sampling.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool AISimultaneousSamplingSupported { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aisupportedmeasurementtypes.html language=enus -->
## TOPIC 01642: AISupportedMeasurementTypes

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aisupportedmeasurementtypes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aisupportedmeasurementtypes.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the measurement types supported by the physical channels of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic AIMeasurementType[] AISupportedMeasurementTypes { get; }RemarksThe values of the supported AIMeasurementType of the device.

### AISupportedMeasurementTypes

Gets the measurement types supported by the physical channels of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIMeasurementType](nationalinstruments-daqmx-aimeasurementtype.html)[] AISupportedMeasurementTypes { get; }

#### Remarks

The values of the supported [AIMeasurementType](nationalinstruments-daqmx-aimeasurementtype.html) of the device.

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aitriggerusage.html language=enus -->
## TOPIC 01643: AITriggerUsage

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aitriggerusage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aitriggerusage.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the analog input trigger types supported by this device. SyntaxNamespace: NationalInstruments.DAQmxpublic TriggerUsageTypes AITriggerUsage { get; }RemarksA TriggerUsageTypes that indicates the analog input trigger types supported by this device. The value is a bitwise combination of Advanc

### AITriggerUsage

Indicates the analog input trigger types supported by this device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [TriggerUsageTypes](nationalinstruments-daqmx-triggerusagetypes.html) AITriggerUsage { get; }

#### Remarks

A [TriggerUsageTypes](nationalinstruments-daqmx-triggerusagetypes.html) that indicates the analog input trigger types supported by this device. The value is a bitwise combination of [Advance](nationalinstruments-daqmx-triggerusagetypes.html), [ArmStart](nationalinstruments-daqmx-triggerusagetypes.html), [Handshake](nationalinstruments-daqmx-triggerusagetypes.html), [None](nationalinstruments-daqmx-triggerusagetypes.html), [Pause](nationalinstruments-daqmx-triggerusagetypes.html), [Reference](nationalinstruments-daqmx-triggerusagetypes.html), and [Start](nationalinstruments-daqmx-triggerusagetypes.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aivoltageinternalexcitationdiscretevalues.html language=enus -->
## TOPIC 01644: AIVoltageInternalExcitationDiscreteValues

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aivoltageinternalexcitationdiscretevalues.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aivoltageinternalexcitationdiscretevalues.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the set of discrete internal voltage excitation values supported by this device. If the device supports ranges of internal excitation values, use AIVoltageInternalExcitationRangeValues to determine supported excitation values. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] AIVol

### AIVoltageInternalExcitationDiscreteValues

Indicates the set of discrete internal voltage excitation values supported by this device. If the device supports ranges of internal excitation values, use [AIVoltageInternalExcitationRangeValues](nationalinstruments-daqmx-device-aivoltageinternalexcitationrangevalues.html) to determine supported excitation values.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] AIVoltageInternalExcitationDiscreteValues { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aivoltageinternalexcitationrangevalues.html language=enus -->
## TOPIC 01645: AIVoltageInternalExcitationRangeValues

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aivoltageinternalexcitationrangevalues.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aivoltageinternalexcitationrangevalues.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates pairs of internal voltage excitation ranges supported by this device. Each pair consists of the low value, followed by the high value. If the device supports a set of discrete internal excitation values, use AIVoltageInternalExcitationDiscreteValues to determine the supported excitation va

### AIVoltageInternalExcitationRangeValues

Indicates pairs of internal voltage excitation ranges supported by this device. Each pair consists of the low value, followed by the high value. If the device supports a set of discrete internal excitation values, use [AIVoltageInternalExcitationDiscreteValues](nationalinstruments-daqmx-device-aivoltageinternalexcitationdiscretevalues.html) to determine the supported excitation values.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] AIVoltageInternalExcitationRangeValues { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aivoltageranges.html language=enus -->
## TOPIC 01646: AIVoltageRanges

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aivoltageranges.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aivoltageranges.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates pairs of input voltage ranges supported by this device. Each pair consists of the low value, followed by the high value. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] AIVoltageRanges { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property wi

### AIVoltageRanges

Indicates pairs of input voltage ranges supported by this device. Each pair consists of the low value, followed by the high value.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] AIVoltageRanges { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-analogtriggersupported.html language=enus -->
## TOPIC 01647: AnalogTriggerSupported

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-analogtriggersupported.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-analogtriggersupported.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device supports analog triggering. SyntaxNamespace: NationalInstruments.DAQmxpublic bool AnalogTriggerSupported { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AnalogTriggerSupported

Indicates if the device supports analog triggering.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool AnalogTriggerSupported { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aocurrentranges.html language=enus -->
## TOPIC 01648: AOCurrentRanges

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aocurrentranges.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aocurrentranges.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates pairs of output current ranges supported by this device. Each pair consists of the low value, followed by the high value. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] AOCurrentRanges { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property w

### AOCurrentRanges

Indicates pairs of output current ranges supported by this device. Each pair consists of the low value, followed by the high value.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] AOCurrentRanges { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aogains.html language=enus -->
## TOPIC 01649: AOGains

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aogains.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aogains.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the output gain settings supported by this device. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] AOGains { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoi

### AOGains

Indicates the output gain settings supported by this device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] AOGains { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aomaximumrate.html language=enus -->
## TOPIC 01650: AOMaximumRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aomaximumrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aomaximumrate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the maximum analog output rate of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic double AOMaximumRate { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AOMaximumRate

Indicates the maximum analog output rate of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double AOMaximumRate { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aominimumrate.html language=enus -->
## TOPIC 01651: AOMinimumRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aominimumrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aominimumrate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the minimum analog output rate of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic double AOMinimumRate { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AOMinimumRate

Indicates the minimum analog output rate of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double AOMinimumRate { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aonumberofsampletimingengines.html language=enus -->
## TOPIC 01652: AONumberOfSampleTimingEngines

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aonumberofsampletimingengines.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aonumberofsampletimingengines.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of Analog Output sample timing engines supported by the device. SyntaxNamespace: NationalInstruments.DAQmxpublic long AONumberOfSampleTimingEngines { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AONumberOfSampleTimingEngines

Indicates the number of Analog Output sample timing engines supported by the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long AONumberOfSampleTimingEngines { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aonumberofsynchronizationpulsesources.html language=enus -->
## TOPIC 01653: AONumberOfSynchronizationPulseSources

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aonumberofsynchronizationpulsesources.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aonumberofsynchronizationpulsesources.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of Analog Output synchronization pulse sources supported by the device. SyntaxNamespace: NationalInstruments.DAQmxpublic long AONumberOfSynchronizationPulseSources { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AONumberOfSynchronizationPulseSources

Indicates the number of Analog Output synchronization pulse sources supported by the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long AONumberOfSynchronizationPulseSources { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aophysicalchannels.html language=enus -->
## TOPIC 01654: AOPhysicalChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aophysicalchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aophysicalchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates an array containing the names of the analog output physical channels available on the device. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] AOPhysicalChannels { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because

### AOPhysicalChannels

Indicates an array containing the names of the analog output physical channels available on the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] AOPhysicalChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aosampleclocksupported.html language=enus -->
## TOPIC 01655: AOSampleClockSupported

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aosampleclocksupported.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aosampleclocksupported.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device supports the sample clock timing type for analog output tasks. SyntaxNamespace: NationalInstruments.DAQmxpublic bool AOSampleClockSupported { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AOSampleClockSupported

Indicates if the device supports the sample clock timing type for analog output tasks.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool AOSampleClockSupported { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aosamplemodes.html language=enus -->
## TOPIC 01656: AOSampleModes

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aosamplemodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aosamplemodes.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets sample modes supported by devices that support sample clocked analog output. SyntaxNamespace: NationalInstruments.DAQmxpublic SampleQuantityMode[] AOSampleModes { get; }RemarksThe values of the supported SampleQuantityMode of the device.

### AOSampleModes

Gets sample modes supported by devices that support sample clocked analog output.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SampleQuantityMode](nationalinstruments-daqmx-samplequantitymode.html)[] AOSampleModes { get; }

#### Remarks

The values of the supported [SampleQuantityMode](nationalinstruments-daqmx-samplequantitymode.html) of the device.

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aosupportedoutputtypes.html language=enus -->
## TOPIC 01657: AOSupportedOutputTypes

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aosupportedoutputtypes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aosupportedoutputtypes.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets generation types supported by the physical channels of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic AOOutputType[] AOSupportedOutputTypes { get; }RemarksThe values of the supported AOOutputType of the device.

### AOSupportedOutputTypes

Gets generation types supported by the physical channels of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AOOutputType](nationalinstruments-daqmx-aooutputtype.html)[] AOSupportedOutputTypes { get; }

#### Remarks

The values of the supported [AOOutputType](nationalinstruments-daqmx-aooutputtype.html) of the device.

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aotriggerusage.html language=enus -->
## TOPIC 01658: AOTriggerUsage

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aotriggerusage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aotriggerusage.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the analog output trigger types supported by this device. SyntaxNamespace: NationalInstruments.DAQmxpublic TriggerUsageTypes AOTriggerUsage { get; }RemarksA TriggerUsageTypes that indicates the analog output trigger types supported by this device. The value is a bitwise combination of Adva

### AOTriggerUsage

Indicates the analog output trigger types supported by this device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [TriggerUsageTypes](nationalinstruments-daqmx-triggerusagetypes.html) AOTriggerUsage { get; }

#### Remarks

A [TriggerUsageTypes](nationalinstruments-daqmx-triggerusagetypes.html) that indicates the analog output trigger types supported by this device. The value is a bitwise combination of [Advance](nationalinstruments-daqmx-triggerusagetypes.html), [ArmStart](nationalinstruments-daqmx-triggerusagetypes.html), [Handshake](nationalinstruments-daqmx-triggerusagetypes.html), [None](nationalinstruments-daqmx-triggerusagetypes.html), [Pause](nationalinstruments-daqmx-triggerusagetypes.html), [Reference](nationalinstruments-daqmx-triggerusagetypes.html), and [Start](nationalinstruments-daqmx-triggerusagetypes.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-aovoltageranges.html language=enus -->
## TOPIC 01659: AOVoltageRanges

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-aovoltageranges.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-aovoltageranges.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates pairs of output voltage ranges supported by this device. Each pair consists of the low value, followed by the high value. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] AOVoltageRanges { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property w

### AOVoltageRanges

Indicates pairs of output voltage ranges supported by this device. Each pair consists of the low value, followed by the high value.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] AOVoltageRanges { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-bustype.html language=enus -->
## TOPIC 01660: BusType

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-bustype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-bustype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the bus type of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic DeviceBusType BusType { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### BusType

Indicates the bus type of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DeviceBusType](nationalinstruments-daqmx-devicebustype.html) BusType { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-carrierserialnumber.html language=enus -->
## TOPIC 01661: CarrierSerialNumber

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-carrierserialnumber.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-carrierserialnumber.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the serial number of the device carrier. This value is zero if the carrier does not have a serial number. SyntaxNamespace: NationalInstruments.DAQmxpublic long CarrierSerialNumber { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CarrierSerialNumber

Indicates the serial number of the device carrier. This value is zero if the carrier does not have a serial number.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long CarrierSerialNumber { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-changeexternalcalibrationpassword__string-string.html language=enus -->
## TOPIC 01662: ChangeExternalCalibrationPassword(string, string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-changeexternalcalibrationpassword__string-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-changeexternalcalibrationpassword__string-string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes the external calibration password of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic void ChangeExternalCalibrationPassword(string currentPassword, string newPassword)ParametersNameTypeDescriptioncurrentPasswordstringThe current calibration password for the device. The default p

### ChangeExternalCalibrationPassword(string, string)

Changes the external calibration password of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ChangeExternalCalibrationPassword(string currentPassword, string newPassword)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| currentPassword | string | The current calibration password for the device. The default password for all NI products is NI. |
| newPassword | string | The new password for the device. This password can be no longer than four characters. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-chassismoduledevicenames.html language=enus -->
## TOPIC 01663: ChassisModuleDeviceNames

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-chassismoduledevicenames.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-chassismoduledevicenames.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates an array containing the names of the modules in the chassis. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] ChassisModuleDeviceNames { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each

### ChassisModuleDeviceNames

Indicates an array containing the names of the modules in the chassis.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] ChassisModuleDeviceNames { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-cimaximumtimebase.html language=enus -->
## TOPIC 01664: CIMaximumTimebase

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-cimaximumtimebase.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-cimaximumtimebase.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in hertz the maximum counter timebase frequency. SyntaxNamespace: NationalInstruments.DAQmxpublic double CIMaximumTimebase { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CIMaximumTimebase

Indicates in hertz the maximum counter timebase frequency.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double CIMaximumTimebase { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-cimaxsize.html language=enus -->
## TOPIC 01665: CIMaxSize

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-cimaxsize.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-cimaxsize.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in bits the size of the counters on the device. SyntaxNamespace: NationalInstruments.DAQmxpublic long CIMaxSize { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CIMaxSize

Indicates in bits the size of the counters on the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long CIMaxSize { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-ciphysicalchannels.html language=enus -->
## TOPIC 01666: CIPhysicalChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-ciphysicalchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-ciphysicalchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates an array containing the names of the counter input physical channels available on the device. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] CIPhysicalChannels { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because

### CIPhysicalChannels

Indicates an array containing the names of the counter input physical channels available on the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] CIPhysicalChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-cisampleclocksupported.html language=enus -->
## TOPIC 01667: CISampleClockSupported

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-cisampleclocksupported.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-cisampleclocksupported.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device supports the sample clock timing type for counter input tasks. SyntaxNamespace: NationalInstruments.DAQmxpublic bool CISampleClockSupported { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CISampleClockSupported

Indicates if the device supports the sample clock timing type for counter input tasks.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool CISampleClockSupported { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-cisamplemodes.html language=enus -->
## TOPIC 01668: CISampleModes

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-cisamplemodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-cisamplemodes.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets sample modes supported by devices that support sample clocked counter input. SyntaxNamespace: NationalInstruments.DAQmxpublic SampleQuantityMode[] CISampleModes { get; }RemarksThe values of the supported SampleQuantityMode of the device.

### CISampleModes

Gets sample modes supported by devices that support sample clocked counter input.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SampleQuantityMode](nationalinstruments-daqmx-samplequantitymode.html)[] CISampleModes { get; }

#### Remarks

The values of the supported [SampleQuantityMode](nationalinstruments-daqmx-samplequantitymode.html) of the device.

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-cisupportedmeasurementtypes.html language=enus -->
## TOPIC 01669: CISupportedMeasurementTypes

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-cisupportedmeasurementtypes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-cisupportedmeasurementtypes.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the measurement types supported by the physical channels of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic CIMeasurementType[] CISupportedMeasurementTypes { get; }RemarksThe values of the supported CIMeasurementType of the device.

### CISupportedMeasurementTypes

Gets the measurement types supported by the physical channels of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIMeasurementType](nationalinstruments-daqmx-cimeasurementtype.html)[] CISupportedMeasurementTypes { get; }

#### Remarks

The values of the supported [CIMeasurementType](nationalinstruments-daqmx-cimeasurementtype.html) of the device.

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-citriggerusage.html language=enus -->
## TOPIC 01670: CITriggerUsage

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-citriggerusage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-citriggerusage.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the counter input trigger types supported by this device. SyntaxNamespace: NationalInstruments.DAQmxpublic TriggerUsageTypes CITriggerUsage { get; }RemarksA TriggerUsageTypes that indicates the counter input trigger types supported by this device. The value is a bitwise combination of Adva

### CITriggerUsage

Indicates the counter input trigger types supported by this device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [TriggerUsageTypes](nationalinstruments-daqmx-triggerusagetypes.html) CITriggerUsage { get; }

#### Remarks

A [TriggerUsageTypes](nationalinstruments-daqmx-triggerusagetypes.html) that indicates the counter input trigger types supported by this device. The value is a bitwise combination of [Advance](nationalinstruments-daqmx-triggerusagetypes.html), [ArmStart](nationalinstruments-daqmx-triggerusagetypes.html), [Handshake](nationalinstruments-daqmx-triggerusagetypes.html), [None](nationalinstruments-daqmx-triggerusagetypes.html), [Pause](nationalinstruments-daqmx-triggerusagetypes.html), [Reference](nationalinstruments-daqmx-triggerusagetypes.html), and [Start](nationalinstruments-daqmx-triggerusagetypes.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-comaximumtimebase.html language=enus -->
## TOPIC 01671: COMaximumTimebase

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-comaximumtimebase.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-comaximumtimebase.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in hertz the maximum counter timebase frequency. SyntaxNamespace: NationalInstruments.DAQmxpublic double COMaximumTimebase { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### COMaximumTimebase

Indicates in hertz the maximum counter timebase frequency.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double COMaximumTimebase { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-comaxsize.html language=enus -->
## TOPIC 01672: COMaxSize

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-comaxsize.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-comaxsize.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in bits the size of the counters on the device. SyntaxNamespace: NationalInstruments.DAQmxpublic long COMaxSize { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### COMaxSize

Indicates in bits the size of the counters on the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long COMaxSize { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-compactdaqchassisdevicename.html language=enus -->
## TOPIC 01673: CompactDaqChassisDeviceName

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-compactdaqchassisdevicename.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-compactdaqchassisdevicename.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the name of the CompactDAQ chassis that contains this module. SyntaxNamespace: NationalInstruments.DAQmxpublic string CompactDaqChassisDeviceName { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CompactDaqChassisDeviceName

Indicates the name of the CompactDAQ chassis that contains this module.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string CompactDaqChassisDeviceName { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-compactdaqchassisslotnumber.html language=enus -->
## TOPIC 01674: CompactDaqChassisSlotNumber

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-compactdaqchassisslotnumber.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-compactdaqchassisslotnumber.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the slot number in which this module is located in the CompactDAQ chassis. SyntaxNamespace: NationalInstruments.DAQmxpublic long CompactDaqChassisSlotNumber { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CompactDaqChassisSlotNumber

Indicates the slot number in which this module is located in the CompactDAQ chassis.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long CompactDaqChassisSlotNumber { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-compactriochassisdevicename.html language=enus -->
## TOPIC 01675: CompactRioChassisDeviceName

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-compactriochassisdevicename.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-compactriochassisdevicename.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the name of the CompactRIO chassis that contains this module. SyntaxNamespace: NationalInstruments.DAQmxpublic string CompactRioChassisDeviceName { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CompactRioChassisDeviceName

Indicates the name of the CompactRIO chassis that contains this module.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string CompactRioChassisDeviceName { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-compactrioslotnumber.html language=enus -->
## TOPIC 01676: CompactRioSlotNumber

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-compactrioslotnumber.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-compactrioslotnumber.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the slot number of the CompactRIO chassis where this module is located. SyntaxNamespace: NationalInstruments.DAQmxpublic long CompactRioSlotNumber { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CompactRioSlotNumber

Indicates the slot number of the CompactRIO chassis where this module is located.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long CompactRioSlotNumber { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-cophysicalchannels.html language=enus -->
## TOPIC 01677: COPhysicalChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-cophysicalchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-cophysicalchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates an array containing the names of the counter output physical channels available on the device. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] COPhysicalChannels { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because

### COPhysicalChannels

Indicates an array containing the names of the counter output physical channels available on the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] COPhysicalChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-cosampleclocksupported.html language=enus -->
## TOPIC 01678: COSampleClockSupported

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-cosampleclocksupported.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-cosampleclocksupported.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device supports Sample Clock timing for counter output tasks. SyntaxNamespace: NationalInstruments.DAQmxpublic bool COSampleClockSupported { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### COSampleClockSupported

Indicates if the device supports Sample Clock timing for counter output tasks.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool COSampleClockSupported { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-cosamplemodes.html language=enus -->
## TOPIC 01679: COSampleModes

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-cosamplemodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-cosamplemodes.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets sample modes supported by devices that support sample clocked counter output. SyntaxNamespace: NationalInstruments.DAQmxpublic SampleQuantityMode[] COSampleModes { get; }RemarksThe values of the supported SampleQuantityMode of the device.

### COSampleModes

Gets sample modes supported by devices that support sample clocked counter output.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [SampleQuantityMode](nationalinstruments-daqmx-samplequantitymode.html)[] COSampleModes { get; }

#### Remarks

The values of the supported [SampleQuantityMode](nationalinstruments-daqmx-samplequantitymode.html) of the device.

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-cosupportedoutputtypes.html language=enus -->
## TOPIC 01680: COSupportedOutputTypes

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-cosupportedoutputtypes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-cosupportedoutputtypes.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the generation types supported by the physical channels of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic COOutputType[] COSupportedOutputTypes { get; }RemarksThe values of the supported COOutputType of the device.

### COSupportedOutputTypes

Gets the generation types supported by the physical channels of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [COOutputType](nationalinstruments-daqmx-cooutputtype.html)[] COSupportedOutputTypes { get; }

#### Remarks

The values of the supported [COOutputType](nationalinstruments-daqmx-cooutputtype.html) of the device.

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-cotriggerusage.html language=enus -->
## TOPIC 01681: COTriggerUsage

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-cotriggerusage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-cotriggerusage.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the counter output trigger types supported by this device. SyntaxNamespace: NationalInstruments.DAQmxpublic TriggerUsageTypes COTriggerUsage { get; }RemarksA TriggerUsageTypes that indicates the counter output trigger types supported by this device. The value is a bitwise combination of Ad

### COTriggerUsage

Indicates the counter output trigger types supported by this device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [TriggerUsageTypes](nationalinstruments-daqmx-triggerusagetypes.html) COTriggerUsage { get; }

#### Remarks

A [TriggerUsageTypes](nationalinstruments-daqmx-triggerusagetypes.html) that indicates the counter output trigger types supported by this device. The value is a bitwise combination of [Advance](nationalinstruments-daqmx-triggerusagetypes.html), [ArmStart](nationalinstruments-daqmx-triggerusagetypes.html), [Handshake](nationalinstruments-daqmx-triggerusagetypes.html), [None](nationalinstruments-daqmx-triggerusagetypes.html), [Pause](nationalinstruments-daqmx-triggerusagetypes.html), [Reference](nationalinstruments-daqmx-triggerusagetypes.html), and [Start](nationalinstruments-daqmx-triggerusagetypes.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-deletenetworkdevice.html language=enus -->
## TOPIC 01682: DeleteNetworkDevice()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-deletenetworkdevice.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-deletenetworkdevice.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes a Network DAQ device previously added to the host. SyntaxNamespace: NationalInstruments.DAQmxpublic void DeleteNetworkDevice()RemarksIf the device is reserved, the device is unreserved before it is removed. ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver re

### DeleteNetworkDevice()

Deletes a Network DAQ device previously added to the host.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void DeleteNetworkDevice()

#### Remarks

If the device is reserved, the device is unreserved before it is removed.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-deviceid.html language=enus -->
## TOPIC 01683: DeviceID

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-deviceid.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-deviceid.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the device, as configured in Measurement & Automation Explorer (MAX), to which this operation applies. SyntaxNamespace: NationalInstruments.DAQmxpublic string DeviceID { get; }RemarksThe name of the device in MAX.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-

### DeviceID

Gets the name of the device, as configured in Measurement & Automation Explorer (MAX), to which this operation applies.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string DeviceID { get; }

#### Remarks

The name of the device in MAX.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-digitalfilterlowpasscutofffrequencydiscretevalues.html language=enus -->
## TOPIC 01684: DigitalFilterLowpassCutoffFrequencyDiscreteValues

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-digitalfilterlowpasscutofffrequencydiscretevalues.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-digitalfilterlowpasscutofffrequencydiscretevalues.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the set of discrete lowpass cutoff frequencies supported by this device. If the device supports ranges of lowpass cutoff frequencies, use AI.DigFltr.Lowpass.CutoffFreq.RangeVals to determine supported frequencies. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] DigitalFilterLowpa

### DigitalFilterLowpassCutoffFrequencyDiscreteValues

Indicates the set of discrete lowpass cutoff frequencies supported by this device. If the device supports ranges of lowpass cutoff frequencies, use AI.DigFltr.Lowpass.CutoffFreq.RangeVals to determine supported frequencies.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] DigitalFilterLowpassCutoffFrequencyDiscreteValues { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-digitalfilterlowpasscutofffrequencyrangevalues.html language=enus -->
## TOPIC 01685: DigitalFilterLowpassCutoffFrequencyRangeValues

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-digitalfilterlowpasscutofffrequencyrangevalues.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-digitalfilterlowpasscutofffrequencyrangevalues.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates pairs of lowpass cutoff frequency ranges supported by this device. Each pair consists of the low value, followed by the high value. If the device supports a set of discrete lowpass cutoff frequencies, use AI.DigFltr.Lowpass.CutoffFreq.DiscreteVals to determine the supported frequencies. Sy

### DigitalFilterLowpassCutoffFrequencyRangeValues

Indicates pairs of lowpass cutoff frequency ranges supported by this device. Each pair consists of the low value, followed by the high value. If the device supports a set of discrete lowpass cutoff frequencies, use AI.DigFltr.Lowpass.CutoffFreq.DiscreteVals to determine the supported frequencies.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] DigitalFilterLowpassCutoffFrequencyRangeValues { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-digitalfiltertypes.html language=enus -->
## TOPIC 01686: DigitalFilterTypes

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-digitalfiltertypes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-digitalfiltertypes.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the AI digital filter types supported by the device. SyntaxNamespace: NationalInstruments.DAQmxpublic AIDigitalFilterType[] DigitalFilterTypes { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each i

### DigitalFilterTypes

Indicates the AI digital filter types supported by the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIDigitalFilterType](nationalinstruments-daqmx-aidigitalfiltertype.html)[] DigitalFilterTypes { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-digitaltriggersupported.html language=enus -->
## TOPIC 01687: DigitalTriggerSupported

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-digitaltriggersupported.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-digitaltriggersupported.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device supports digital triggering. SyntaxNamespace: NationalInstruments.DAQmxpublic bool DigitalTriggerSupported { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalTriggerSupported

Indicates if the device supports digital triggering.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DigitalTriggerSupported { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-dilines.html language=enus -->
## TOPIC 01688: DILines

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-dilines.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-dilines.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates an array containing the names of the digital input lines available on the device. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] DILines { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for e

### DILines

Indicates an array containing the names of the digital input lines available on the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] DILines { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-dimaximumrate.html language=enus -->
## TOPIC 01689: DIMaximumRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-dimaximumrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-dimaximumrate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the maximum digital input rate of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic double DIMaximumRate { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DIMaximumRate

Indicates the maximum digital input rate of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DIMaximumRate { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-dinumberofsampletimingengines.html language=enus -->
## TOPIC 01690: DINumberOfSampleTimingEngines

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-dinumberofsampletimingengines.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-dinumberofsampletimingengines.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of Digital Input sample timing engines supported by the device. SyntaxNamespace: NationalInstruments.DAQmxpublic long DINumberOfSampleTimingEngines { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DINumberOfSampleTimingEngines

Indicates the number of Digital Input sample timing engines supported by the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long DINumberOfSampleTimingEngines { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-diports.html language=enus -->
## TOPIC 01691: DIPorts

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-diports.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-diports.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates an array containing the names of the digital input ports available on the device. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] DIPorts { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for e

### DIPorts

Indicates an array containing the names of the digital input ports available on the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] DIPorts { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-dispose.html language=enus -->
## TOPIC 01692: Dispose()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-dispose.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-dispose.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Releases all resources used by Device. SyntaxNamespace: NationalInstruments.DAQmxpublic override void Dispose()RemarksUse this method only if the application you create runs on a low memory system.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Dispose()

Releases all resources used by [Device](nationalinstruments-daqmx-device.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override void Dispose()

#### Remarks

Use this method only if the application you create runs on a low memory system.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-dispose__bool.html language=enus -->
## TOPIC 01693: Dispose(bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-dispose__bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-dispose__bool.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Releases the managed and unmanaged resources used by Device or optionally releases only the unmanaged resources. SyntaxNamespace: NationalInstruments.DAQmxprotected void Dispose([MarshalAs(UnmanagedType.U1)] bool A_0)RemarksRefer to Cleaning Up Unmanaged Resources for more information on implementin

### Dispose(bool)

Releases the managed and unmanaged resources used by [Device](nationalinstruments-daqmx-device.html) or optionally releases only the unmanaged resources.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

protected void Dispose([MarshalAs(UnmanagedType.U1)] bool A_0)

#### Remarks

Refer to [Cleaning Up Unmanaged Resources](https://#) for more information on implementing a Dispose method and using objects that implement IDisposable.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| A_0 | bool | true to release both managed and unmanaged resources used by Device; false to release only unmanaged resources used by Device. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-ditriggerusage.html language=enus -->
## TOPIC 01694: DITriggerUsage

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-ditriggerusage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-ditriggerusage.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the digital input trigger types supported by this device. SyntaxNamespace: NationalInstruments.DAQmxpublic TriggerUsageTypes DITriggerUsage { get; }RemarksA TriggerUsageTypes that indicates the digital input trigger types supported by this device. The default value is a bitwise combination

### DITriggerUsage

Indicates the digital input trigger types supported by this device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [TriggerUsageTypes](nationalinstruments-daqmx-triggerusagetypes.html) DITriggerUsage { get; }

#### Remarks

A [TriggerUsageTypes](nationalinstruments-daqmx-triggerusagetypes.html) that indicates the digital input trigger types supported by this device. The default value is a bitwise combination of [Advance](nationalinstruments-daqmx-triggerusagetypes.html), [ArmStart](nationalinstruments-daqmx-triggerusagetypes.html), [Handshake](nationalinstruments-daqmx-triggerusagetypes.html), [None](nationalinstruments-daqmx-triggerusagetypes.html), [Pause](nationalinstruments-daqmx-triggerusagetypes.html), [Reference](nationalinstruments-daqmx-triggerusagetypes.html), and [Start](nationalinstruments-daqmx-triggerusagetypes.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-dolines.html language=enus -->
## TOPIC 01695: DOLines

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-dolines.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-dolines.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates an array containing the names of the digital output lines available on the device. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] DOLines { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for

### DOLines

Indicates an array containing the names of the digital output lines available on the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] DOLines { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-domaximumrate.html language=enus -->
## TOPIC 01696: DOMaximumRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-domaximumrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-domaximumrate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the maximum digital output rate of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic double DOMaximumRate { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DOMaximumRate

Indicates the maximum digital output rate of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DOMaximumRate { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-donumberofsampletimingengines.html language=enus -->
## TOPIC 01697: DONumberOfSampleTimingEngines

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-donumberofsampletimingengines.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-donumberofsampletimingengines.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of Digital Output synchronization pulse sources supported by the device. SyntaxNamespace: NationalInstruments.DAQmxpublic long DONumberOfSampleTimingEngines { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DONumberOfSampleTimingEngines

Indicates the number of Digital Output synchronization pulse sources supported by the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long DONumberOfSampleTimingEngines { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-doports.html language=enus -->
## TOPIC 01698: DOPorts

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-doports.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-doports.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates an array containing the names of the digital output ports available on the device. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] DOPorts { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for

### DOPorts

Indicates an array containing the names of the digital output ports available on the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] DOPorts { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-dotriggerusage.html language=enus -->
## TOPIC 01699: DOTriggerUsage

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-dotriggerusage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-dotriggerusage.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the digital output trigger types supported by this device. SyntaxNamespace: NationalInstruments.DAQmxpublic TriggerUsageTypes DOTriggerUsage { get; }RemarksA TriggerUsageTypes that indicates the digital output trigger types supported by this device. The default value is a bitwise combinati

### DOTriggerUsage

Indicates the digital output trigger types supported by this device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [TriggerUsageTypes](nationalinstruments-daqmx-triggerusagetypes.html) DOTriggerUsage { get; }

#### Remarks

A [TriggerUsageTypes](nationalinstruments-daqmx-triggerusagetypes.html) that indicates the digital output trigger types supported by this device. The default value is a bitwise combination of [Advance](nationalinstruments-daqmx-triggerusagetypes.html), [ArmStart](nationalinstruments-daqmx-triggerusagetypes.html), [Handshake](nationalinstruments-daqmx-triggerusagetypes.html), [None](nationalinstruments-daqmx-triggerusagetypes.html), [Pause](nationalinstruments-daqmx-triggerusagetypes.html), [Reference](nationalinstruments-daqmx-triggerusagetypes.html), and [Start](nationalinstruments-daqmx-triggerusagetypes.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-externalcalibrationdate.html language=enus -->
## TOPIC 01700: ExternalCalibrationDate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-externalcalibrationdate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-externalcalibrationdate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the last date and time that the device underwent an external calibration. SyntaxNamespace: NationalInstruments.DAQmxpublic DateTime ExternalCalibrationDate { get; }RemarksThe date and time of the external calibration.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx dr

### ExternalCalibrationDate

Gets the last date and time that the device underwent an external calibration.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public DateTime ExternalCalibrationDate { get; }

#### Remarks

The date and time of the external calibration.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-externalcalibrationrecommendedinterval.html language=enus -->
## TOPIC 01701: ExternalCalibrationRecommendedInterval

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-externalcalibrationrecommendedinterval.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-externalcalibrationrecommendedinterval.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in months the National Instruments recommended interval between each external calibration of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic long ExternalCalibrationRecommendedInterval { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver r

### ExternalCalibrationRecommendedInterval

Indicates in months the National Instruments recommended interval between each external calibration of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long ExternalCalibrationRecommendedInterval { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-externalcalibrationtemperature.html language=enus -->
## TOPIC 01702: ExternalCalibrationTemperature

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-externalcalibrationtemperature.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-externalcalibrationtemperature.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in degrees Celsius the temperature of the device at the time of the last external calibration. Compare this temperature to the current onboard temperature to determine if you should perform another calibration. SyntaxNamespace: NationalInstruments.DAQmxpublic double ExternalCalibrationTemp

### ExternalCalibrationTemperature

Indicates in degrees Celsius the temperature of the device at the time of the last external calibration. Compare this temperature to the current onboard temperature to determine if you should perform another calibration.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double ExternalCalibrationTemperature { get; }

#### Remarks

The temperature returned by this property is the calibration temperature as measured by an onboard temperature sensor and may differ from the temperature displayed on a printed calibration certificate. Calibration certificates usually display the ambient temperature rather than the onboard temperature.

Using Traditional NI-DAQ (Legacy) to perform calibration does not update this property. This property is updated only when you use NI-DAQmx to perform calibration.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-fielddaqbankdevicenames.html language=enus -->
## TOPIC 01703: FieldDaqBankDeviceNames

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-fielddaqbankdevicenames.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-fielddaqbankdevicenames.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates an array containing the names of the banks in the FieldDAQ. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] FieldDaqBankDeviceNames { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each it

### FieldDaqBankDeviceNames

Indicates an array containing the names of the banks in the FieldDAQ.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] FieldDaqBankDeviceNames { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-fielddaqdevicename.html language=enus -->
## TOPIC 01704: FieldDaqDeviceName

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-fielddaqdevicename.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-fielddaqdevicename.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the parent device which this bank is located in. SyntaxNamespace: NationalInstruments.DAQmxpublic string FieldDaqDeviceName { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FieldDaqDeviceName

Indicates the parent device which this bank is located in.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string FieldDaqDeviceName { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-getphysicalchannels__physicalchanneltypes-physicalchannelaccess.html language=enus -->
## TOPIC 01705: GetPhysicalChannels(PhysicalChannelTypes, PhysicalChannelAccess)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-getphysicalchannels__physicalchanneltypes-physicalchannelaccess.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-getphysicalchannels__physicalchanneltypes-physicalchannelaccess.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the names of the physical channels on this device. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] GetPhysicalChannels(PhysicalChannelTypes physicalChannelTypes, PhysicalChannelAccess physicalChannelAccess)ParametersNameTypeDescriptionphysicalChannelTypesPhysica

### GetPhysicalChannels(PhysicalChannelTypes, PhysicalChannelAccess)

Gets an array that contains the names of the [physical channels](/csh?context=nidaqmx_mxcncpts_chans) on this device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] GetPhysicalChannels(PhysicalChannelTypes physicalChannelTypes, PhysicalChannelAccess physicalChannelAccess)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannelTypes | PhysicalChannelTypes | The types of physical channels to include. |
| physicalChannelAccess | PhysicalChannelAccess | The access types of physical channels to include. |

#### Returns

An array that contains the names of the requested physical channels on this device.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-getpossiblescexpresscalibrationaccessoryconnections__string.html language=enus -->
## TOPIC 01706: GetPossibleSCExpressCalibrationAccessoryConnections(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-getpossiblescexpresscalibrationaccessoryconnections__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-getpossiblescexpresscalibrationaccessoryconnections__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the available connections on an SC Express accessory for the specified physical channel(s). SyntaxNamespace: NationalInstruments.DAQmxpublic string[] GetPossibleSCExpressCalibrationAccessoryConnections(string physicalChannels)RemarksConnections specify how channels on the SC Express accessory s

### GetPossibleSCExpressCalibrationAccessoryConnections(string)

Gets the available connections on an SC Express accessory for the specified physical channel(s).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] GetPossibleSCExpressCalibrationAccessoryConnections(string physicalChannels)

#### Remarks

Connections specify how channels on the SC Express accessory should be configured. The resulting configuration connects channels to a particular external signal or an onboard terminal.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| physicalChannels | string | The physical channel(s) to use. |

#### Returns

An array of strings representing the available connections on an SC Express accessory for the specified physical channel(s).

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-getterminals__terminaltypes.html language=enus -->
## TOPIC 01707: GetTerminals(TerminalTypes)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-getterminals__terminaltypes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-getterminals__terminaltypes.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the names of the terminals on this device. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] GetTerminals(TerminalTypes terminalTypes)ParametersNameTypeDescriptionterminalTypesTerminalTypesThe types of terminals to include.ReturnsAn array that contains the names o

### GetTerminals(TerminalTypes)

Gets an array that contains the names of the [terminals](/csh?context=nidaqmx_mxcncpts_terminal) on this device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] GetTerminals(TerminalTypes terminalTypes)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| terminalTypes | TerminalTypes | The types of terminals to include. |

#### Returns

An array that contains the names of the requested terminals on this device.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-idpinmemfamilycodes.html language=enus -->
## TOPIC 01708: IDPinMemFamilyCodes

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-idpinmemfamilycodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-idpinmemfamilycodes.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the family code of the memory connected to each ID Pin. Each array element corresponds to an ID Pin. The array contains 0 for each ID Pin with no memory connected. SyntaxNamespace: NationalInstruments.DAQmxpublic long[] IDPinMemFamilyCodes { get; }RemarksThis property returns a copy of the

### IDPinMemFamilyCodes

Indicates the family code of the memory connected to each ID Pin. Each array element corresponds to an ID Pin. The array contains 0 for each ID Pin with no memory connected.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long[] IDPinMemFamilyCodes { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-idpinmemserialnums.html language=enus -->
## TOPIC 01709: IDPinMemSerialNums

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-idpinmemserialnums.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-idpinmemserialnums.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the serial number of the memory connected to each ID Pin. Each array element corresponds to an ID Pin. The array contains an empty string for each ID Pin with no memory connected. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] IDPinMemSerialNums { get; }RemarksThis property retu

### IDPinMemSerialNums

Indicates the serial number of the memory connected to each ID Pin. Each array element corresponds to an ID Pin. The array contains an empty string for each ID Pin with no memory connected.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] IDPinMemSerialNums { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-idpinmemsizes.html language=enus -->
## TOPIC 01710: IDPinMemSizes

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-idpinmemsizes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-idpinmemsizes.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the size in bytes of the memory connected to each ID Pin. Each array element corresponds to an ID Pin. The array contains 0 for each ID Pin with no memory connected. SyntaxNamespace: NationalInstruments.DAQmxpublic long[] IDPinMemSizes { get; }RemarksThis property returns a copy of the act

### IDPinMemSizes

Indicates the size in bytes of the memory connected to each ID Pin. Each array element corresponds to an ID Pin. The array contains 0 for each ID Pin with no memory connected.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long[] IDPinMemSizes { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-idpinpinnames.html language=enus -->
## TOPIC 01711: IDPinPinNames

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-idpinpinnames.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-idpinpinnames.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the names of all the ID Pins on this device. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] IDPinPinNames { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoi

### IDPinPinNames

Indicates the names of all the ID Pins on this device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] IDPinPinNames { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-idpinpinstatuses.html language=enus -->
## TOPIC 01712: IDPinPinStatuses

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-idpinpinstatuses.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-idpinpinstatuses.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates status of each ID Pin. SyntaxNamespace: NationalInstruments.DAQmxpublic IDPinStatus[] IDPinPinStatuses { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an ind

### IDPinPinStatuses

Indicates status of each ID Pin.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [IDPinStatus](nationalinstruments-daqmx-idpinstatus.html)[] IDPinPinStatuses { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-isselfcalibrationsupported.html language=enus -->
## TOPIC 01713: IsSelfCalibrationSupported

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-isselfcalibrationsupported.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-isselfcalibrationsupported.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the device supports self-calibration. SyntaxNamespace: NationalInstruments.DAQmxpublic bool IsSelfCalibrationSupported { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### IsSelfCalibrationSupported

Indicates whether the device supports self-calibration.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool IsSelfCalibrationSupported { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-issimulated.html language=enus -->
## TOPIC 01714: IsSimulated

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-issimulated.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-issimulated.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device is a simulated device. SyntaxNamespace: NationalInstruments.DAQmxpublic bool IsSimulated { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### IsSimulated

Indicates if the device is a simulated device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool IsSimulated { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-lowpasscutofffrequenciesdiscretevalues.html language=enus -->
## TOPIC 01715: LowpassCutoffFrequenciesDiscreteValues

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-lowpasscutofffrequenciesdiscretevalues.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-lowpasscutofffrequenciesdiscretevalues.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the set of discrete lowpass cutoff frequencies supported by this device. If the device supports ranges of lowpass cutoff frequencies, use LowpassCutoffFrequenciesRangeValues to determine supported frequencies. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] LowpassCutoffFrequenci

### LowpassCutoffFrequenciesDiscreteValues

Indicates the set of discrete lowpass cutoff frequencies supported by this device. If the device supports ranges of lowpass cutoff frequencies, use [LowpassCutoffFrequenciesRangeValues](nationalinstruments-daqmx-device-lowpasscutofffrequenciesrangevalues.html) to determine supported frequencies.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] LowpassCutoffFrequenciesDiscreteValues { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-lowpasscutofffrequenciesrangevalues.html language=enus -->
## TOPIC 01716: LowpassCutoffFrequenciesRangeValues

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-lowpasscutofffrequenciesrangevalues.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-lowpasscutofffrequenciesrangevalues.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates pairs of lowpass cutoff frequency ranges supported by this device. Each pair consists of the low value, followed by the high value. If the device supports a set of discrete lowpass cutoff frequencies, use LowpassCutoffFrequenciesDiscreteValues to determine the supported frequencies. Syntax

### LowpassCutoffFrequenciesRangeValues

Indicates pairs of lowpass cutoff frequency ranges supported by this device. Each pair consists of the low value, followed by the high value. If the device supports a set of discrete lowpass cutoff frequencies, use [LowpassCutoffFrequenciesDiscreteValues](nationalinstruments-daqmx-device-lowpasscutofffrequenciesdiscretevalues.html) to determine the supported frequencies.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] LowpassCutoffFrequenciesRangeValues { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-maxuserdefinedcalibrationinfosize.html language=enus -->
## TOPIC 01717: MaxUserDefinedCalibrationInfoSize

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-maxuserdefinedcalibrationinfosize.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-maxuserdefinedcalibrationinfosize.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the maximum length in characters of UserDefinedCalibrationInfo. SyntaxNamespace: NationalInstruments.DAQmxpublic long MaxUserDefinedCalibrationInfoSize { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### MaxUserDefinedCalibrationInfoSize

Indicates the maximum length in characters of [UserDefinedCalibrationInfo](nationalinstruments-daqmx-device-userdefinedcalibrationinfo.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long MaxUserDefinedCalibrationInfoSize { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-numberofdmachannels.html language=enus -->
## TOPIC 01718: NumberOfDmaChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-numberofdmachannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-numberofdmachannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of DMA channels on the device. SyntaxNamespace: NationalInstruments.DAQmxpublic long NumberOfDmaChannels { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### NumberOfDmaChannels

Indicates the number of DMA channels on the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long NumberOfDmaChannels { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-pcibusnumber.html language=enus -->
## TOPIC 01719: PciBusNumber

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-pcibusnumber.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-pcibusnumber.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the PCI bus number of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic long PciBusNumber { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PciBusNumber

Indicates the PCI bus number of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long PciBusNumber { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-pcidevicenumber.html language=enus -->
## TOPIC 01720: PciDeviceNumber

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-pcidevicenumber.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-pcidevicenumber.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the PCI slot number of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic long PciDeviceNumber { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PciDeviceNumber

Indicates the PCI slot number of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long PciDeviceNumber { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-productcategory.html language=enus -->
## TOPIC 01721: ProductCategory

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-productcategory.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-productcategory.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the product category of the device. This category corresponds to the category displayed in MAX when creating NI-DAQmx simulated devices. SyntaxNamespace: NationalInstruments.DAQmxpublic ProductCategory ProductCategory { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionT

### ProductCategory

Indicates the product category of the device. This category corresponds to the category displayed in MAX when creating NI-DAQmx simulated devices.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [ProductCategory](nationalinstruments-daqmx-productcategory.html) ProductCategory { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-productnumber.html language=enus -->
## TOPIC 01722: ProductNumber

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-productnumber.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-productnumber.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the unique hardware identification number for the device. SyntaxNamespace: NationalInstruments.DAQmxpublic long ProductNumber { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ProductNumber

Indicates the unique [hardware identification number](/csh?context=nidaqmx_mxdevconsid_hardwareids) for the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long ProductNumber { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-producttype.html language=enus -->
## TOPIC 01723: ProductType

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-producttype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-producttype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the product name of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic string ProductType { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ProductType

Indicates the product name of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string ProductType { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-pxichassisnumber.html language=enus -->
## TOPIC 01724: PxiChassisNumber

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-pxichassisnumber.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-pxichassisnumber.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the PXI chassis number of the device, as identified in MAX. SyntaxNamespace: NationalInstruments.DAQmxpublic long PxiChassisNumber { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PxiChassisNumber

Indicates the PXI chassis number of the device, as identified in MAX.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long PxiChassisNumber { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-pxislotnumber.html language=enus -->
## TOPIC 01725: PxiSlotNumber

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-pxislotnumber.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-pxislotnumber.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the PXI slot number of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic long PxiSlotNumber { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PxiSlotNumber

Indicates the PXI slot number of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long PxiSlotNumber { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-recommendedaccessoryconnectioncountlimit.html language=enus -->
## TOPIC 01726: RecommendedAccessoryConnectionCountLimit

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-recommendedaccessoryconnectioncountlimit.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-recommendedaccessoryconnectioncountlimit.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the recommended connection count limit for an accessory. If the accessory connection count exceeds this limit, the accessory could require maintenance. SyntaxNamespace: NationalInstruments.DAQmxpublic long RecommendedAccessoryConnectionCountLimit { get; }ExceptionsTypeDescriptionNationalIn

### RecommendedAccessoryConnectionCountLimit

Indicates the recommended connection count limit for an accessory. If the accessory connection count exceeds this limit, the accessory could require maintenance.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long RecommendedAccessoryConnectionCountLimit { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-reservenetworkdevice.html language=enus -->
## TOPIC 01727: ReserveNetworkDevice()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-reservenetworkdevice.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-reservenetworkdevice.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reserves the Network DAQ device for the current host. Reservation is required to run NI-DAQmx tasks, and the device must be added in MAX before it can be reserved. This method does not override any existing reservations on the device. SyntaxNamespace: NationalInstruments.DAQmxpublic void ReserveNetw

### ReserveNetworkDevice()

Reserves the Network DAQ device for the current host. Reservation is required to run NI-DAQmx tasks, and the device must be added in MAX before it can be reserved. This method does not override any existing reservations on the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ReserveNetworkDevice()

#### Remarks

Note

This functionality is performed implicitly for the NI 9163, so this method is not supported on the NI 9163 carrier.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-reservenetworkdevice__bool.html language=enus -->
## TOPIC 01728: ReserveNetworkDevice(bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-reservenetworkdevice__bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-reservenetworkdevice__bool.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reserves the Network DAQ device for the current host. Reservation is required to run NI-DAQmx tasks, and the device must be added in MAX before it can be reserved. Use this method to specify whether to override an existing reservation. SyntaxNamespace: NationalInstruments.DAQmxpublic void ReserveNet

### ReserveNetworkDevice(bool)

Reserves the Network DAQ device for the current host. Reservation is required to run NI-DAQmx tasks, and the device must be added in MAX before it can be reserved. Use this method to specify whether to override an existing reservation.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ReserveNetworkDevice([MarshalAs(UnmanagedType.U1)] bool overrideReservation)

#### Remarks

Note

This functionality is performed implicitly for the NI 9163, so this method is not supported on the NI 9163 carrier.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| overrideReservation | bool | Specifies whether an existing reservation on the device should be overridden by this reservation. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-reset.html language=enus -->
## TOPIC 01729: Reset()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-reset.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-reset.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Immediately aborts all active tasks associated with a device and returns the device to an initialized state. SyntaxNamespace: NationalInstruments.DAQmxpublic void Reset()RemarksAborting a task stops the task and releases any resources the task reserved.ExceptionsTypeDescriptionNationalInstruments.DA

### Reset()

Immediately aborts all active tasks associated with a device and returns the device to an [initialized](/csh?context=nidaqmx_mxdevconsid_initstates) state.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void Reset()

#### Remarks

Aborting a task stops the task and releases any resources the task reserved.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-restorelastexternalcalibration.html language=enus -->
## TOPIC 01730: RestoreLastExternalCalibration()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-restorelastexternalcalibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-restorelastexternalcalibration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the self-calibration constants of the device to the current external calibration constants. SyntaxNamespace: NationalInstruments.DAQmxpublic void RestoreLastExternalCalibration()RemarksNational Instruments sets the external calibration constants at the factory, and those constants remain in eff

### RestoreLastExternalCalibration()

Sets the self-calibration constants of the device to the current external calibration constants.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void RestoreLastExternalCalibration()

#### Remarks

National Instruments sets the external calibration constants at the factory, and those constants remain in effect until you perform a new external calibration on the device.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-selfcalibrate.html language=enus -->
## TOPIC 01731: SelfCalibrate()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-selfcalibrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-selfcalibrate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Measures the onboard reference voltage of the device and adjusts the self-calibration constants to account for any error caused by short-term fluctuation in the operating environment. SyntaxNamespace: NationalInstruments.DAQmxpublic void SelfCalibrate()ExceptionsTypeDescriptionNationalInstruments.DA

### SelfCalibrate()

Measures the onboard reference voltage of the device and adjusts the self-calibration constants to account for any error caused by short-term fluctuation in the operating environment.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void SelfCalibrate()

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

#### See Also

- IsSelfCalibrationSupported

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-selfcalibrationdatetime.html language=enus -->
## TOPIC 01732: SelfCalibrationDateTime

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-selfcalibrationdatetime.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-selfcalibrationdatetime.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the last date and time that the device underwent a self-calibration. SyntaxNamespace: NationalInstruments.DAQmxpublic DateTime SelfCalibrationDateTime { get; }RemarksThe date and time of the self-calibration.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver retu

### SelfCalibrationDateTime

Gets the last date and time that the device underwent a self-calibration.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public DateTime SelfCalibrationDateTime { get; }

#### Remarks

The date and time of the self-calibration.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-selfcalibrationtemperature.html language=enus -->
## TOPIC 01733: SelfCalibrationTemperature

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-selfcalibrationtemperature.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-selfcalibrationtemperature.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in degrees Celsius the temperature of the device at the time of the last self-calibration. Compare this temperature to the current onboard temperature to determine if you should perform another calibration. SyntaxNamespace: NationalInstruments.DAQmxpublic double SelfCalibrationTemperature

### SelfCalibrationTemperature

Indicates in degrees Celsius the temperature of the device at the time of the last self-calibration. Compare this temperature to the current onboard temperature to determine if you should perform another calibration.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double SelfCalibrationTemperature { get; }

#### Remarks

The temperature returned by this property is the calibration temperature as measured by an onboard temperature sensor and may differ from the temperature displayed on a printed calibration certificate. Calibration certificates usually display the ambient temperature rather than the onboard temperature.

Using Traditional NI-DAQ (Legacy) to perform calibration does not update this property. This property is updated only when you use NI-DAQmx to perform calibration.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-selftest.html language=enus -->
## TOPIC 01734: SelfTest()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-selftest.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-selftest.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a brief test of the device resources. If a failure occurs, refer to your device documentation for more information. SyntaxNamespace: NationalInstruments.DAQmxpublic void SelfTest()ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### SelfTest()

Performs a brief test of the device resources. If a failure occurs, refer to your device documentation for more information.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void SelfTest()

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-serialnumber.html language=enus -->
## TOPIC 01735: SerialNumber

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-serialnumber.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-serialnumber.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the serial number of the device. This value is zero if the device does not have a serial number. SyntaxNamespace: NationalInstruments.DAQmxpublic long SerialNumber { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### SerialNumber

Indicates the serial number of the device. This value is zero if the device does not have a serial number.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long SerialNumber { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-startexternalcalibration__string.html language=enus -->
## TOPIC 01736: StartExternalCalibration(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-startexternalcalibration__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-startexternalcalibration__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Starts an external calibration session on a device. SyntaxNamespace: NationalInstruments.DAQmxpublic ExternalCalibrationSession StartExternalCalibration(string password)ParametersNameTypeDescriptionpasswordstringThe current calibration password for the device. The default password for all NI product

### StartExternalCalibration(string)

Starts an external calibration session on a device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [ExternalCalibrationSession](nationalinstruments-daqmx-externalcalibrationsession.html) StartExternalCalibration(string password)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| password | string | The current calibration password for the device. The default password for all NI products is NI. |

#### Returns

A reference to the [ExternalCalibrationSession](nationalinstruments-daqmx-externalcalibrationsession.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-switch.html language=enus -->
## TOPIC 01737: Switch

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-switch.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-switch.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a Switch class for this device that contains properties and methods specific to switch devices. SyntaxNamespace: NationalInstruments.DAQmxpublic Switch Switch { get; }RemarksA Switch class for this device that contains properties and methods specific to switch devices.

### Switch

Gets a [Switch](nationalinstruments-daqmx-switch.html) class for this device that contains properties and methods specific to [switch devices](/csh?context=nidaqmx_mxcncpts_switches).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [Switch](nationalinstruments-daqmx-switch.html) Switch { get; }

#### Remarks

A [Switch](nationalinstruments-daqmx-switch.html) class for this device that contains properties and methods specific to switch devices.

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-tcpipethernetip.html language=enus -->
## TOPIC 01738: TcpipEthernetIP

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-tcpipethernetip.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-tcpipethernetip.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the IPv4 address of the Ethernet interface in dotted decimal format. This property returns 0.0.0.0 if the Ethernet interface cannot acquire an address. SyntaxNamespace: NationalInstruments.DAQmxpublic string TcpipEthernetIP { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExce

### TcpipEthernetIP

Indicates the IPv4 address of the Ethernet interface in dotted decimal format. This property returns 0.0.0.0 if the Ethernet interface cannot acquire an address.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string TcpipEthernetIP { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-tcpiphostname.html language=enus -->
## TOPIC 01739: TcpipHostname

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-tcpiphostname.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-tcpiphostname.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the IPv4 hostname of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic string TcpipHostname { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### TcpipHostname

Indicates the IPv4 hostname of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string TcpipHostname { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-tcpipwirelessip.html language=enus -->
## TOPIC 01740: TcpipWirelessIP

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-tcpipwirelessip.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-tcpipwirelessip.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the IPv4 address of the 802.11 wireless interface in dotted decimal format. This property returns 0.0.0.0 if the wireless interface cannot acquire an address. SyntaxNamespace: NationalInstruments.DAQmxpublic string TcpipWirelessIP { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.

### TcpipWirelessIP

Indicates the IPv4 address of the 802.11 wireless interface in dotted decimal format. This property returns 0.0.0.0 if the wireless interface cannot acquire an address.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string TcpipWirelessIP { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-tedshardwaretedssupported.html language=enus -->
## TOPIC 01741: TedsHardwareTedsSupported

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-tedshardwaretedssupported.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-tedshardwaretedssupported.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the device supports hardware TEDS. SyntaxNamespace: NationalInstruments.DAQmxpublic bool TedsHardwareTedsSupported { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### TedsHardwareTedsSupported

Indicates whether the device supports hardware TEDS.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool TedsHardwareTedsSupported { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-temperature.html language=enus -->
## TOPIC 01742: Temperature

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-temperature.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-temperature.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in degrees Celsius the current temperature of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic double Temperature { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Temperature

Indicates in degrees Celsius the current temperature of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double Temperature { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-timestampenginecount.html language=enus -->
## TOPIC 01743: TimestampEngineCount

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-timestampenginecount.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-timestampenginecount.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of timestamp engines available on the device. SyntaxNamespace: NationalInstruments.DAQmxpublic long TimestampEngineCount { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### TimestampEngineCount

Indicates the number of timestamp engines available on the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long TimestampEngineCount { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-timetriggercount.html language=enus -->
## TOPIC 01744: TimeTriggerCount

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-timetriggercount.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-timetriggercount.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of time triggers available on the device. SyntaxNamespace: NationalInstruments.DAQmxpublic long TimeTriggerCount { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### TimeTriggerCount

Indicates the number of time triggers available on the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long TimeTriggerCount { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-timetriggersupported.html language=enus -->
## TOPIC 01745: TimeTriggerSupported

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-timetriggersupported.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-timetriggersupported.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the device supports time triggering. SyntaxNamespace: NationalInstruments.DAQmxpublic bool TimeTriggerSupported { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### TimeTriggerSupported

Indicates whether the device supports time triggering.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool TimeTriggerSupported { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-tostring.html language=enus -->
## TOPIC 01746: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString. ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

#### Remarks

Overrides ToString.

#### Returns

A string representation of the object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-unreservenetworkdevice.html language=enus -->
## TOPIC 01747: UnreserveNetworkDevice()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-unreservenetworkdevice.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-unreservenetworkdevice.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unreserves or releases a Network DAQ device previously reserved by the host. SyntaxNamespace: NationalInstruments.DAQmxpublic void UnreserveNetworkDevice()ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### UnreserveNetworkDevice()

Unreserves or releases a Network DAQ device previously reserved by the host.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void UnreserveNetworkDevice()

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device-userdefinedcalibrationinfo.html language=enus -->
## TOPIC 01748: UserDefinedCalibrationInfo

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device-userdefinedcalibrationinfo.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device-userdefinedcalibrationinfo.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a string that contains arbitrary, user-defined information. This number of characters in this string can be no more than MaxUserDefinedCalibrationInfoSize. SyntaxNamespace: NationalInstruments.DAQmxpublic string UserDefinedCalibrationInfo { get; set; }ExceptionsTypeDescriptionNationalInstr

### UserDefinedCalibrationInfo

Specifies a string that contains arbitrary, user-defined information. This number of characters in this string can be no more than [MaxUserDefinedCalibrationInfoSize](nationalinstruments-daqmx-device-maxuserdefinedcalibrationinfosize.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string UserDefinedCalibrationInfo { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Device Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-device.html language=enus -->
## TOPIC 01749: Device Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-device.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-device.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Encapsulates a DAQ device and contains methods and properties that operate on devices outside the context of a task. Derives fromMarshalByRefObjectIDisposableSyntaxNamespace: NationalInstruments.DAQmxpublic class Device : MarshalByRefObject, IDisposableRemarks Dim dev as Device dev = DaqSystem.Local

### Device Class

Encapsulates a DAQ device and contains methods and properties that operate on devices outside the context of a task.

#### Derives from

- MarshalByRefObject
- IDisposable

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class Device : MarshalByRefObject, IDisposable

#### Remarks

```text
Dim dev as Devicedev = DaqSystem.Local.LoadDevice("dev1")dev.SelfCalibrate()
```

```text
Device dev = DaqSystem.Local.LoadDevice("dev1");dev.SelfCalibrate();
```

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

Device

Device

LoadDevice(string)

Device

Device

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| AccessoryConnectionCount | Specifies the number of times a particular connection that results in tangible wear and tear of onboard components has been made on the accessory. This connection count is useful for tracking accessory life and usage. |
| AccessoryProductNumbers | Indicates the unique hardware identification number for accessories connected to the device. Each array element corresponds to a connector. For example, index 0 corresponds to connector 0. The array contains 0 for each connector with no accessory connected. |
| AccessoryProductTypes | Indicates the model names of accessories connected to the device. Each array element corresponds to a connector. For example, index 0 corresponds to connector 0. The array contains an empty string for each connector with no accessory connected. |
| AccessorySerialNumbers | Indicates the serial number for accessories connected to the device. Each array element corresponds to a connector. For example, index 0 corresponds to connector 0. The array contains 0 for each connector with no accessory connected. |
| AIBridgeRanges | Indicates pairs of input voltage ratio ranges, in volts per volt, supported by devices that acquire using ratiometric measurements. Each pair consists of the low value followed by the high value. |
| AIChargeRanges | Indicates in coulombs pairs of input charge ranges for the device. Each pair consists of the low value followed by the high value. |
| AICouplings | Indicates the coupling types supported by this device. |
| AICurrentInternalExcitationDiscreteValues | Indicates the set of discrete internal current excitation values supported by this device. |
| AICurrentRanges | Indicates the pairs of current input ranges supported by this device. Each pair consists of the low value, followed by the high value. |
| AIFrequencyRanges | Indicates the pairs of frequency input ranges supported by this device. Each pair consists of the low value, followed by the high value. |
| AIGains | Indicates the input gain settings supported by this device. |
| AIMaximumMultiChannelRate | Indicates the maximum sampling rate for an analog input task from this device. To find the maximum rate for the task, take the minimum of AIMaximumSingleChannelRate or the indicated sampling rate of this device divided by the number of channels to acquire data from (including cold-junction compensation and autozero channels). |
| AIMaximumSingleChannelRate | Indicates the maximum rate for an analog input task if the task contains only a single channel from this device. |
| AIMinimumRate | Indicates the minimum rate for an analog input task on this device. NI-DAQmx returns a warning or error if you attempt to sample at a slower rate. |
| AINumberOfSampleTimingEngines | Indicates the number of Analog Input sample timing engines supported by the device. |
| AINumberOfSynchronizationPulseSources | Indicates the number of Analog Input synchronization pulse sources supported by the device. |
| AIPhysicalChannels | Indicates an array containing the names of the analog input physical channels available on the device. |
| AISampleModes | Gets the sample modes from devices that support sample clocked analog input. |
| AISimultaneousSamplingSupported | Indicates if the device supports simultaneous sampling. |
| AISupportedMeasurementTypes | Gets the measurement types supported by the physical channels of the device. |
| AITriggerUsage | Indicates the analog input trigger types supported by this device. |
| AIVoltageInternalExcitationDiscreteValues | Indicates the set of discrete internal voltage excitation values supported by this device. If the device supports ranges of internal excitation values, use AIVoltageInternalExcitationRangeValues to determine supported excitation values. |
| AIVoltageInternalExcitationRangeValues | Indicates pairs of internal voltage excitation ranges supported by this device. Each pair consists of the low value, followed by the high value. If the device supports a set of discrete internal excitation values, use AIVoltageInternalExcitationDiscreteValues to determine the supported excitation values. |
| AIVoltageRanges | Indicates pairs of input voltage ranges supported by this device. Each pair consists of the low value, followed by the high value. |
| AnalogTriggerSupported | Indicates if the device supports analog triggering. |
| AOCurrentRanges | Indicates pairs of output current ranges supported by this device. Each pair consists of the low value, followed by the high value. |
| AOGains | Indicates the output gain settings supported by this device. |
| AOMaximumRate | Indicates the maximum analog output rate of the device. |
| AOMinimumRate | Indicates the minimum analog output rate of the device. |
| AONumberOfSampleTimingEngines | Indicates the number of Analog Output sample timing engines supported by the device. |
| AONumberOfSynchronizationPulseSources | Indicates the number of Analog Output synchronization pulse sources supported by the device. |
| AOPhysicalChannels | Indicates an array containing the names of the analog output physical channels available on the device. |
| AOSampleClockSupported | Indicates if the device supports the sample clock timing type for analog output tasks. |
| AOSampleModes | Gets sample modes supported by devices that support sample clocked analog output. |
| AOSupportedOutputTypes | Gets generation types supported by the physical channels of the device. |
| AOTriggerUsage | Indicates the analog output trigger types supported by this device. |
| AOVoltageRanges | Indicates pairs of output voltage ranges supported by this device. Each pair consists of the low value, followed by the high value. |
| BusType | Indicates the bus type of the device. |
| CarrierSerialNumber | Indicates the serial number of the device carrier. This value is zero if the carrier does not have a serial number. |
| ChassisModuleDeviceNames | Indicates an array containing the names of the modules in the chassis. |
| CIMaximumTimebase | Indicates in hertz the maximum counter timebase frequency. |
| CIMaxSize | Indicates in bits the size of the counters on the device. |
| CIPhysicalChannels | Indicates an array containing the names of the counter input physical channels available on the device. |
| CISampleClockSupported | Indicates if the device supports the sample clock timing type for counter input tasks. |
| CISampleModes | Gets sample modes supported by devices that support sample clocked counter input. |
| CISupportedMeasurementTypes | Gets the measurement types supported by the physical channels of the device. |
| CITriggerUsage | Indicates the counter input trigger types supported by this device. |
| COMaximumTimebase | Indicates in hertz the maximum counter timebase frequency. |
| COMaxSize | Indicates in bits the size of the counters on the device. |
| CompactDaqChassisDeviceName | Indicates the name of the CompactDAQ chassis that contains this module. |
| CompactDaqChassisSlotNumber | Indicates the slot number in which this module is located in the CompactDAQ chassis. |
| CompactRioChassisDeviceName | Indicates the name of the CompactRIO chassis that contains this module. |
| CompactRioSlotNumber | Indicates the slot number of the CompactRIO chassis where this module is located. |
| COPhysicalChannels | Indicates an array containing the names of the counter output physical channels available on the device. |
| COSampleClockSupported | Indicates if the device supports Sample Clock timing for counter output tasks. |
| COSampleModes | Gets sample modes supported by devices that support sample clocked counter output. |
| COSupportedOutputTypes | Gets the generation types supported by the physical channels of the device. |
| COTriggerUsage | Indicates the counter output trigger types supported by this device. |
| DeviceID | Gets the name of the device, as configured in Measurement & Automation Explorer (MAX), to which this operation applies. |
| DigitalFilterLowpassCutoffFrequencyDiscreteValues | Indicates the set of discrete lowpass cutoff frequencies supported by this device. If the device supports ranges of lowpass cutoff frequencies, use AI.DigFltr.Lowpass.CutoffFreq.RangeVals to determine supported frequencies. |
| DigitalFilterLowpassCutoffFrequencyRangeValues | Indicates pairs of lowpass cutoff frequency ranges supported by this device. Each pair consists of the low value, followed by the high value. If the device supports a set of discrete lowpass cutoff frequencies, use AI.DigFltr.Lowpass.CutoffFreq.DiscreteVals to determine the supported frequencies. |
| DigitalFilterTypes | Indicates the AI digital filter types supported by the device. |
| DigitalTriggerSupported | Indicates if the device supports digital triggering. |
| DILines | Indicates an array containing the names of the digital input lines available on the device. |
| DIMaximumRate | Indicates the maximum digital input rate of the device. |
| DINumberOfSampleTimingEngines | Indicates the number of Digital Input sample timing engines supported by the device. |
| DIPorts | Indicates an array containing the names of the digital input ports available on the device. |
| DITriggerUsage | Indicates the digital input trigger types supported by this device. |
| DOLines | Indicates an array containing the names of the digital output lines available on the device. |
| DOMaximumRate | Indicates the maximum digital output rate of the device. |
| DONumberOfSampleTimingEngines | Indicates the number of Digital Output synchronization pulse sources supported by the device. |
| DOPorts | Indicates an array containing the names of the digital output ports available on the device. |
| DOTriggerUsage | Indicates the digital output trigger types supported by this device. |
| ExternalCalibrationDate | Gets the last date and time that the device underwent an external calibration. |
| ExternalCalibrationRecommendedInterval | Indicates in months the National Instruments recommended interval between each external calibration of the device. |
| ExternalCalibrationTemperature | Indicates in degrees Celsius the temperature of the device at the time of the last external calibration. Compare this temperature to the current onboard temperature to determine if you should perform another calibration. |
| FieldDaqBankDeviceNames | Indicates an array containing the names of the banks in the FieldDAQ. |
| FieldDaqDeviceName | Indicates the parent device which this bank is located in. |
| IDPinMemFamilyCodes | Indicates the family code of the memory connected to each ID Pin. Each array element corresponds to an ID Pin. The array contains 0 for each ID Pin with no memory connected. |
| IDPinMemSerialNums | Indicates the serial number of the memory connected to each ID Pin. Each array element corresponds to an ID Pin. The array contains an empty string for each ID Pin with no memory connected. |
| IDPinMemSizes | Indicates the size in bytes of the memory connected to each ID Pin. Each array element corresponds to an ID Pin. The array contains 0 for each ID Pin with no memory connected. |
| IDPinPinNames | Indicates the names of all the ID Pins on this device. |
| IDPinPinStatuses | Indicates status of each ID Pin. |
| IsSelfCalibrationSupported | Indicates whether the device supports self-calibration. |
| IsSimulated | Indicates if the device is a simulated device. |
| LowpassCutoffFrequenciesDiscreteValues | Indicates the set of discrete lowpass cutoff frequencies supported by this device. If the device supports ranges of lowpass cutoff frequencies, use LowpassCutoffFrequenciesRangeValues to determine supported frequencies. |
| LowpassCutoffFrequenciesRangeValues | Indicates pairs of lowpass cutoff frequency ranges supported by this device. Each pair consists of the low value, followed by the high value. If the device supports a set of discrete lowpass cutoff frequencies, use LowpassCutoffFrequenciesDiscreteValues to determine the supported frequencies. |
| MaxUserDefinedCalibrationInfoSize | Indicates the maximum length in characters of UserDefinedCalibrationInfo. |
| NumberOfDmaChannels | Indicates the number of DMA channels on the device. |
| PciBusNumber | Indicates the PCI bus number of the device. |
| PciDeviceNumber | Indicates the PCI slot number of the device. |
| ProductCategory | Indicates the product category of the device. This category corresponds to the category displayed in MAX when creating NI-DAQmx simulated devices. |
| ProductNumber | Indicates the unique hardware identification number for the device. |
| ProductType | Indicates the product name of the device. |
| PxiChassisNumber | Indicates the PXI chassis number of the device, as identified in MAX. |
| PxiSlotNumber | Indicates the PXI slot number of the device. |
| RecommendedAccessoryConnectionCountLimit | Indicates the recommended connection count limit for an accessory. If the accessory connection count exceeds this limit, the accessory could require maintenance. |
| SelfCalibrationDateTime | Gets the last date and time that the device underwent a self-calibration. |
| SelfCalibrationTemperature | Indicates in degrees Celsius the temperature of the device at the time of the last self-calibration. Compare this temperature to the current onboard temperature to determine if you should perform another calibration. |
| SerialNumber | Indicates the serial number of the device. This value is zero if the device does not have a serial number. |
| Switch | Gets a Switch class for this device that contains properties and methods specific to switch devices. |
| TcpipEthernetIP | Indicates the IPv4 address of the Ethernet interface in dotted decimal format. This property returns 0.0.0.0 if the Ethernet interface cannot acquire an address. |
| TcpipHostname | Indicates the IPv4 hostname of the device. |
| TcpipWirelessIP | Indicates the IPv4 address of the 802.11 wireless interface in dotted decimal format. This property returns 0.0.0.0 if the wireless interface cannot acquire an address. |
| TedsHardwareTedsSupported | Indicates whether the device supports hardware TEDS. |
| Temperature | Indicates in degrees Celsius the current temperature of the device. |
| TimestampEngineCount | Indicates the number of timestamp engines available on the device. |
| TimeTriggerCount | Indicates the number of time triggers available on the device. |
| TimeTriggerSupported | Indicates whether the device supports time triggering. |
| UserDefinedCalibrationInfo | Specifies a string that contains arbitrary, user-defined information. This number of characters in this string can be no more than MaxUserDefinedCalibrationInfoSize. |

#### Methods

| Name | Description |
| --- | --- |
| ChangeExternalCalibrationPassword(string, string) | Changes the external calibration password of the device. |
| DeleteNetworkDevice() | Deletes a Network DAQ device previously added to the host. |
| Dispose() | Releases all resources used by Device. |
| GetPhysicalChannels(PhysicalChannelTypes, PhysicalChannelAccess) | Gets an array that contains the names of the physical channels on this device. |
| GetPossibleSCExpressCalibrationAccessoryConnections(string) | Gets the available connections on an SC Express accessory for the specified physical channel(s). |
| GetTerminals(TerminalTypes) | Gets an array that contains the names of the terminals on this device. |
| ReserveNetworkDevice(bool) | Reserves the Network DAQ device for the current host. Reservation is required to run NI-DAQmx tasks, and the device must be added in MAX before it can be reserved. Use this method to specify whether to override an existing reservation. |
| ReserveNetworkDevice() | Reserves the Network DAQ device for the current host. Reservation is required to run NI-DAQmx tasks, and the device must be added in MAX before it can be reserved. This method does not override any existing reservations on the device. |
| Reset() | Immediately aborts all active tasks associated with a device and returns the device to an initialized state. |
| RestoreLastExternalCalibration() | Sets the self-calibration constants of the device to the current external calibration constants. |
| SelfCalibrate() | Measures the onboard reference voltage of the device and adjusts the self-calibration constants to account for any error caused by short-term fluctuation in the operating environment. |
| SelfTest() | Performs a brief test of the device resources. If a failure occurs, refer to your device documentation for more information. |
| StartExternalCalibration(string) | Starts an external calibration session on a device. |
| ToString() | Returns a string representation of the object. |
| UnreserveNetworkDevice() | Unreserves or releases a Network DAQ device previously reserved by the host. |
| Dispose(bool) | Releases the managed and unmanaged resources used by Device or optionally releases only the unmanaged resources. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-devicebustype.html language=enus -->
## TOPIC 01750: DeviceBusType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-devicebustype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-devicebustype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the bus type of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic enum DeviceBusTypeRemarksIndicates the bus type of the device. Use this enumeration to get or set the value of BusType.MembersNameValueDescriptionPci12582PCI. Pcie13612PCI Express. Pxi12583PXI. Pxie14706PXI Expres

### DeviceBusType Enumeration

Indicates the bus type of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum DeviceBusType

#### Remarks

Indicates the bus type of the device. Use this enumeration to get or set the value of [BusType](nationalinstruments-daqmx-device-bustype.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Pci | 12582 | PCI. |
| Pcie | 13612 | PCI Express. |
| Pxi | 12583 | PXI. |
| Pxie | 14706 | PXI Express. |
| Scxi | 12584 | SCXI. |
| Scc | 14707 | SCC. |
| PCCard | 12585 | PC Card/PCMCIA. |
| Usb | 12586 | USB. |
| CompactDaq | 14637 | CompactDAQ. |
| CompactRio | 16143 | CompactRIO. |
| Tcpip | 14828 | TCP/IP. |
| Unknown | 12588 | Unknown bus type. |
| SwitchBlock | 15870 | SwitchBlock. |

Parent topic:

NationalInstruments.DAQmx
