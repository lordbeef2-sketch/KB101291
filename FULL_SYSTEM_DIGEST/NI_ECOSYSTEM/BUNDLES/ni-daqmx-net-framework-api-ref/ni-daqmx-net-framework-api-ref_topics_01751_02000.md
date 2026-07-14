# NI DOCUMENT BUNDLE: ni-daqmx-net-framework-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-daqmx-net-framework-api-ref start=1751 end=2000 -->
<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-diacquireon.html language=enus -->
## TOPIC 01751: DIAcquireOn Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-diacquireon.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-diacquireon.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of the sample clock to acquire samples. SyntaxNamespace: NationalInstruments.DAQmxpublic enum DIAcquireOnRemarksSpecifies on which edge of the sample clock to acquire samples. Use this enumeration to get or set the value of AcquireOn.MembersNameValueDescriptionActiveEdge14617

### DIAcquireOn Enumeration

Specifies on which edge of the sample clock to acquire samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum DIAcquireOn

#### Remarks

Specifies on which edge of the sample clock to acquire samples. Use this enumeration to get or set the value of [AcquireOn](nationalinstruments-daqmx-dichannel-acquireon.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ActiveEdge | 14617 | Active edges. |
| InactiveEdge | 14618 | Inactive edges. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dichannel-acquireon.html language=enus -->
## TOPIC 01752: AcquireOn

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dichannel-acquireon.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dichannel-acquireon.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of the sample clock to acquire samples. SyntaxNamespace: NationalInstruments.DAQmxpublic DIAcquireOn AcquireOn { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AcquireOn

Specifies on which edge of the sample clock to acquire samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DIAcquireOn](nationalinstruments-daqmx-diacquireon.html) AcquireOn { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dichannel-datatransfermechanism.html language=enus -->
## TOPIC 01753: DataTransferMechanism

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dichannel-datatransfermechanism.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dichannel-datatransfermechanism.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the data transfer mode for the device. SyntaxNamespace: NationalInstruments.DAQmxpublic DIDataTransferMechanism DataTransferMechanism { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DataTransferMechanism

Specifies the data transfer mode for the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DIDataTransferMechanism](nationalinstruments-daqmx-didatatransfermechanism.html) DataTransferMechanism { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dichannel-datatransferrequestcondition.html language=enus -->
## TOPIC 01754: DataTransferRequestCondition

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dichannel-datatransferrequestcondition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dichannel-datatransferrequestcondition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies under what condition to transfer data from the onboard memory of the device to the buffer. SyntaxNamespace: NationalInstruments.DAQmxpublic DIDataTransferRequestCondition DataTransferRequestCondition { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx d

### DataTransferRequestCondition

Specifies under what condition to transfer data from the onboard memory of the device to the buffer.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DIDataTransferRequestCondition](nationalinstruments-daqmx-didatatransferrequestcondition.html) DataTransferRequestCondition { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dichannel-digitalfilterenable.html language=enus -->
## TOPIC 01755: DigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dichannel-digitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dichannel-digitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the digital filter for the line(s) or port(s). You can enable the filter on a line-by-line basis. You do not have to enable the filter for all lines in a channel. SyntaxNamespace: NationalInstruments.DAQmxpublic bool DigitalFilterEnable { get; set; }ExceptionsTypeDescript

### DigitalFilterEnable

Specifies whether to enable the digital [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) for the line(s) or port(s). You can enable the filter on a line-by-line basis. You do not have to enable the filter for all lines in a channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dichannel-digitalfilterenablebusmode.html language=enus -->
## TOPIC 01756: DigitalFilterEnableBusMode

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dichannel-digitalfilterenablebusmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dichannel-digitalfilterenablebusmode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable bus mode for digital filtering. If you set this property to true, NI-DAQmx treats all lines that use common filtering settings as a bus. If any line in the bus has jitter, all lines in the bus hold state until the entire bus stabilizes, or until 2 times the minimum pulse

### DigitalFilterEnableBusMode

Specifies whether to enable bus mode for digital filtering. If you set this property to true, NI-DAQmx treats all lines that use common filtering settings as a bus. If any line in the bus has jitter, all lines in the bus hold state until the entire bus stabilizes, or until 2 times the minimum pulse width elapses. If you set this property to false, NI-DAQmx filters all lines individually. Jitter in one line does not affect other lines.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DigitalFilterEnableBusMode { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dichannel-digitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 01757: DigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dichannel-digitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dichannel-digitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes as a valid high or low state transition. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned

### DigitalFilterMinimumPulseWidth

Specifies in seconds the minimum pulse width the [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) recognizes as a valid high or low state transition.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dichannel-digitalfiltertimebaserate.html language=enus -->
## TOPIC 01758: DigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dichannel-digitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dichannel-digitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver r

### DigitalFilterTimebaseRate

Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dichannel-digitalfiltertimebasesource.html language=enus -->
## TOPIC 01759: DigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dichannel-digitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dichannel-digitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the timebase of the digital filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string DigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterTimebaseSource

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the timebase of the digital filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string DigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dichannel-digitalsynchronizationenable.html language=enus -->
## TOPIC 01760: DigitalSynchronizationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dichannel-digitalsynchronizationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dichannel-digitalsynchronizationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic bool DigitalSynchronizationEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returne

### DigitalSynchronizationEnable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DigitalSynchronizationEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dichannel-invertlines.html language=enus -->
## TOPIC 01761: InvertLines

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dichannel-invertlines.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dichannel-invertlines.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to invert the lines in the channel. If you set this property to true, the lines are at high logic when off and at low logic when on. SyntaxNamespace: NationalInstruments.DAQmxpublic bool InvertLines { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-

### InvertLines

Specifies whether to invert the lines in the channel. If you set this property to true, the lines are at high logic when off and at low logic when on.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool InvertLines { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dichannel-logicfamily.html language=enus -->
## TOPIC 01762: LogicFamily

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dichannel-logicfamily.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dichannel-logicfamily.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic family to use for acquisition. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families. SyntaxNamespace: NationalIns

### LogicFamily

Specifies the logic family to use for acquisition. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DILogicFamily](nationalinstruments-daqmx-dilogicfamily.html) LogicFamily { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dichannel-memorymappingenable.html language=enus -->
## TOPIC 01763: MemoryMappingEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dichannel-memorymappingenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dichannel-memorymappingenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space of the application increases performance. However, if the application ac

### MemoryMappingEnable

Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space of the application increases performance. However, if the application accesses the memory space mapped to the registers, it can adversely affect the operation of the device and possibly result in a system crash.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool MemoryMappingEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dichannel-numberoflines.html language=enus -->
## TOPIC 01764: NumberOfLines

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dichannel-numberoflines.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dichannel-numberoflines.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of digital lines in the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic long NumberOfLines { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### NumberOfLines

Indicates the number of digital lines in the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long NumberOfLines { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dichannel-tristate.html language=enus -->
## TOPIC 01765: Tristate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dichannel-tristate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dichannel-tristate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to tristate the lines in the channel. If you set this property to true, NI-DAQmx tristates the lines in the channel. If you set this property to false, NI-DAQmx does not modify the configuration of the lines even if the lines were previously tristated. Set this property to false to

### Tristate

Specifies whether to tristate the lines in the channel. If you set this property to true, NI-DAQmx tristates the lines in the channel. If you set this property to false, NI-DAQmx does not modify the configuration of the lines even if the lines were previously tristated. Set this property to false to read lines in other tasks or to read output-only lines.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool Tristate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dichannel-usbtransferrequestcount.html language=enus -->
## TOPIC 01766: UsbTransferRequestCount

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dichannel-usbtransferrequestcount.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dichannel-usbtransferrequestcount.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device. SyntaxNamespace: NationalInstruments.DAQmxpublic long UsbTransferRequestCount { get; set; }ExceptionsTypeDescriptionNat

### UsbTransferRequestCount

Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long UsbTransferRequestCount { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dichannel-usbtransferrequestsize.html language=enus -->
## TOPIC 01767: UsbTransferRequestSize

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dichannel-usbtransferrequestsize.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dichannel-usbtransferrequestsize.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device. SyntaxNamespace: NationalInstruments.DAQmxpublic long UsbTransferRequestSize { get; set; }ExceptionsTypeDescriptionNationalInstruments.D

### UsbTransferRequestSize

Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long UsbTransferRequestSize { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dichannel.html language=enus -->
## TOPIC 01768: DIChannel Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dichannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dichannel.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Encapsulates one or more digital input channels and the properties for a digital input channel. Derives fromChannelIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class DIChannel : Channel, IFilteredTypeDescriptorRemarksUse the DIChannels property to create or access a digita

### DIChannel Class

Encapsulates one or more digital input channels and the properties for a digital input channel.

#### Derives from

- Channel
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class DIChannel : Channel, IFilteredTypeDescriptor

#### Remarks

DIChannels

DIChannel

DIChannel

DIChannels

DIChannelCollection

DIChannel

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| AcquireOn | Specifies on which edge of the sample clock to acquire samples. |
| DataTransferMechanism | Specifies the data transfer mode for the device. |
| DataTransferRequestCondition | Specifies under what condition to transfer data from the onboard memory of the device to the buffer. |
| DigitalFilterEnable | Specifies whether to enable the digital filter for the line(s) or port(s). You can enable the filter on a line-by-line basis. You do not have to enable the filter for all lines in a channel. |
| DigitalFilterEnableBusMode | Specifies whether to enable bus mode for digital filtering. If you set this property to true, NI-DAQmx treats all lines that use common filtering settings as a bus. If any line in the bus has jitter, all lines in the bus hold state until the entire bus stabilizes, or until 2 times the minimum pulse width elapses. If you set this property to false, NI-DAQmx filters all lines individually. Jitter in one line does not affect other lines. |
| DigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes as a valid high or low state transition. |
| DigitalFilterTimebaseRate | Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
| DigitalFilterTimebaseSource | Specifies the terminal of the signal to use as the timebase of the digital filter. |
| DigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
| InvertLines | Specifies whether to invert the lines in the channel. If you set this property to true, the lines are at high logic when off and at low logic when on. |
| LogicFamily | Specifies the logic family to use for acquisition. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families. |
| MemoryMappingEnable | Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space of the application increases performance. However, if the application accesses the memory space mapped to the registers, it can adversely affect the operation of the device and possibly result in a system crash. |
| NumberOfLines | Indicates the number of digital lines in the channel. |
| Tristate | Specifies whether to tristate the lines in the channel. If you set this property to true, NI-DAQmx tristates the lines in the channel. If you set this property to false, NI-DAQmx does not modify the configuration of the lines even if the lines were previously tristated. Set this property to false to read lines in other tasks or to read output-only lines. |
| UsbTransferRequestCount | Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device. |
| UsbTransferRequestSize | Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device. |

#### See Also

- DIChannelCollection

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dichannelcollection-all.html language=enus -->
## TOPIC 01769: All

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dichannelcollection-all.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dichannelcollection-all.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DIChannel that operates on all of the channels in the task. SyntaxNamespace: NationalInstruments.DAQmxpublic DIChannel All { get; }RemarksA DIChannel that operates on all of the channels in a task.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an e

### All

Gets a [DIChannel](nationalinstruments-daqmx-dichannel.html) that operates on all of the channels in the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DIChannel](nationalinstruments-daqmx-dichannel.html) All { get; }

#### Remarks

A [DIChannel](nationalinstruments-daqmx-dichannel.html) that operates on all of the channels in a task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dichannelcollection-copyto__array-int.html language=enus -->
## TOPIC 01770: CopyTo(Array, int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dichannelcollection-copyto__array-int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dichannelcollection-copyto__array-int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Copies the collection to an array or a portion of an array. This operation is not supported for DIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic void CopyTo(Array array, int index)ParametersNameTypeDescriptionarrayArrayDestination array for the collection.indexintThe index in th

### CopyTo(Array, int)

Copies the collection to an array or a portion of an array. This operation is not supported for [DIChannelCollection](nationalinstruments-daqmx-dichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void CopyTo(Array array, int index)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| array | Array | Destination array for the collection. |
| index | int | The index in the target array at which you want to begin copying the collection to. |

#### Exceptions

| Type | Description |
| --- | --- |
| NotSupportedException | This method always throws a NotSupportedException. |

Parent topic:

DIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dichannelcollection-count.html language=enus -->
## TOPIC 01771: Count

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dichannelcollection-count.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dichannelcollection-count.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of elements in the collection. SyntaxNamespace: NationalInstruments.DAQmxpublic int Count { get; }RemarksThe number of elements contained in the collection.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Count

Gets the number of elements in the collection.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int Count { get; }

#### Remarks

The number of elements contained in the collection.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dichannelcollection-createchannel__string-string-channellinegrouping.html language=enus -->
## TOPIC 01772: CreateChannel(string, string, ChannelLineGrouping)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dichannelcollection-createchannel__string-string-channellinegrouping.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dichannelcollection-createchannel__string-string-channellinegrouping.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a DIChannel to measure digital signals. This method adds one or more channels to the DIChannelCollection. SyntaxNamespace: NationalInstruments.DAQmxpublic DIChannel CreateChannel(string lines, string nameToAssign, ChannelLineGrouping grouping)RemarksYou can group digital lines into one DICha

### CreateChannel(string, string, ChannelLineGrouping)

Creates a [DIChannel](nationalinstruments-daqmx-dichannel.html) to [measure digital signals](/csh?context=nidaqmx_daqhelp_diglevelmeasgen). This method adds one or more channels to the [DIChannelCollection](nationalinstruments-daqmx-dichannelcollection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DIChannel](nationalinstruments-daqmx-dichannel.html) CreateChannel(string lines, string nameToAssign, ChannelLineGrouping grouping)

#### Remarks

You can group digital lines into one [DIChannel](nationalinstruments-daqmx-dichannel.html) or separate them into multiple [DIChannel](nationalinstruments-daqmx-dichannel.html) objects. If you specify one or more entire ports with *lines*  by using port physical channel names, you cannot separate the ports into multiple channels. To separate ports into multiple channels, use this method multiple times with a different port each time.

If you do not specify a value for *nameToAssign* , NI-DAQmx uses the physical channel name for the virtual channel name. If you use *nameToAssign*  to create a name for the local virtual channel, you must use that name when you refer to this channel in other NI-DAQmx properties and methods.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. CreateChannel(string, string, ChannelLineGrouping) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| lines | string | The names of the digital lines or ports to use to create the virtual channel. |
| nameToAssign | string | The name of the virtual channel this method creates. |
| grouping | ChannelLineGrouping | The grouping of digital lines into one or more DIChannel objects. If you specify one or more entire ports with lines , you must set grouping to OneChannelForAllLines. |

#### Returns

The newly created [DIChannel](nationalinstruments-daqmx-dichannel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dichannelcollection-getenumerator.html language=enus -->
## TOPIC 01773: GetEnumerator()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dichannelcollection-getenumerator.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dichannelcollection-getenumerator.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an enumerator that you can use to iterate through the collection. SyntaxNamespace: NationalInstruments.DAQmxpublic IEnumerator GetEnumerator()RemarksFor a detailed explanation of this method, refer to GetEnumerator in the Microsoft .NET Framework documentation. ReturnsEnumerator for the coll

### GetEnumerator()

Returns an enumerator that you can use to iterate through the collection.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IEnumerator GetEnumerator()

#### Remarks

For a detailed explanation of this method, refer to GetEnumerator in the Microsoft .NET Framework documentation.

#### Returns

Enumerator for the collection.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dichannelcollection-this__long.html language=enus -->
## TOPIC 01774: this[long index]

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dichannelcollection-this__long.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dichannelcollection-this__long.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DIChannel at the specified index. In Visual C#, this property is the indexer. SyntaxNamespace: NationalInstruments.DAQmxpublic DIChannel this[long index] { get; }RemarksThe DIChannel at the specified index. ChannelsParametersNameTypeDescriptionindexlongThe zero-based index of the entry to l

### this[long index]

Gets the [DIChannel](nationalinstruments-daqmx-dichannel.html) at the specified index. In Visual C#, this property is the indexer.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DIChannel](nationalinstruments-daqmx-dichannel.html) this[long index] { get; }

#### Remarks

The [DIChannel](nationalinstruments-daqmx-dichannel.html) at the specified index.

Channels

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| index | long | The zero-based index of the entry to locate in the collection. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

#### See Also

- DIChannel

Parent topic:

DIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dichannelcollection-this__string.html language=enus -->
## TOPIC 01775: this[string virtualChannelName]

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dichannelcollection-this__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dichannelcollection-this__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DIChannel with the specified virtual channel name. In Visual C#, this property is the indexer. SyntaxNamespace: NationalInstruments.DAQmxpublic DIChannel this[string virtualChannelName] { get; }RemarksThe specified DIChannel. ChannelsBy using a comma or colon in virtualChannelName , you can

### this[string virtualChannelName]

Gets the [DIChannel](nationalinstruments-daqmx-dichannel.html) with the specified virtual channel name. In Visual C#, this property is the indexer.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DIChannel](nationalinstruments-daqmx-dichannel.html) this[string virtualChannelName] { get; }

#### Remarks

The specified [DIChannel](nationalinstruments-daqmx-dichannel.html).

Channels

By using a comma or colon in *virtualChannelName* , you can retrieve more than one channel at a time. For more information refer to [Channels](https://#).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| virtualChannelName | string | One or more virtual channel names that the retrieved DIChannel operates on. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

#### See Also

- DIChannel

Parent topic:

DIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dichannelcollection-tostring.html language=enus -->
## TOPIC 01776: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dichannelcollection-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dichannelcollection-tostring.html
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

DIChannelCollection Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-dichannelcollection.html language=enus -->
## TOPIC 01777: DIChannelCollection Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-dichannelcollection.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-dichannelcollection.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains the collection of digital input channels for a Task. Derives fromMarshalByRefObjectICollectionSyntaxNamespace: NationalInstruments.DAQmxpublic class DIChannelCollection : MarshalByRefObject, ICollectionRemarksExample applications are located in the <Public Documents>\National Instruments\NI

### DIChannelCollection Class

Contains the collection of digital input channels for a [Task](nationalinstruments-daqmx-task.html).

#### Derives from

- MarshalByRefObject
- ICollection

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class DIChannelCollection : MarshalByRefObject, ICollection

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| All | Gets a DIChannel that operates on all of the channels in the task. |
| Count | Gets the number of elements in the collection. |
| this[long index] | Gets the DIChannel at the specified index. In Visual C#, this property is the indexer. |
| this[string virtualChannelName] | Gets the DIChannel with the specified virtual channel name. In Visual C#, this property is the indexer. |

#### Methods

| Name | Description |
| --- | --- |
| CopyTo(Array, int) | Copies the collection to an array or a portion of an array. This operation is not supported for DIChannelCollection. |
| CreateChannel(string, string, ChannelLineGrouping) | Creates a DIChannel to measure digital signals. This method adds one or more channels to the DIChannelCollection. |
| GetEnumerator() | Returns an enumerator that you can use to iterate through the collection. |
| ToString() | Returns a string representation of the object. |

#### See Also

- Task
- DIChannels
- DIChannel

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-didatatransfermechanism.html language=enus -->
## TOPIC 01778: DIDataTransferMechanism Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-didatatransfermechanism.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-didatatransfermechanism.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the data transfer mode for the device. SyntaxNamespace: NationalInstruments.DAQmxpublic enum DIDataTransferMechanismRemarksSpecifies the data transfer mode for the device. Use this enumeration to get or set the value of DataTransferMechanism.MembersNameValueDescriptionDma10054Direct Memory

### DIDataTransferMechanism Enumeration

Specifies the data transfer mode for the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum DIDataTransferMechanism

#### Remarks

Specifies the data transfer mode for the device. Use this enumeration to get or set the value of [DataTransferMechanism](nationalinstruments-daqmx-dichannel-datatransfermechanism.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Dma | 10054 | Direct Memory Access. Data transfers take place independently from the application. |
| Interrupts | 10204 | Data transfers take place independently from the application. Using interrupts increases CPU usage because the CPU must service interrupt requests. Typically, you should use interrupts if the device is out of DMA channels. |
| ProgrammedIO | 10264 | Data transfers take place when you call reading from the task or writing to the task. |
| UsbBulk | 12590 | Data transfers take place independently from the application using a USB bulk pipe. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-didatatransferrequestcondition.html language=enus -->
## TOPIC 01779: DIDataTransferRequestCondition Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-didatatransferrequestcondition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-didatatransferrequestcondition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies under what condition to transfer data from the onboard memory of the device to the buffer. SyntaxNamespace: NationalInstruments.DAQmxpublic enum DIDataTransferRequestConditionRemarksSpecifies under what condition to transfer data from the onboard memory of the device to the buffer. Use thi

### DIDataTransferRequestCondition Enumeration

Specifies under what condition to transfer data from the onboard memory of the device to the buffer.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum DIDataTransferRequestCondition

#### Remarks

Specifies under what condition to transfer data from the onboard memory of the device to the buffer. Use this enumeration to get or set the value of [DataTransferRequestCondition](nationalinstruments-daqmx-dichannel-datatransferrequestcondition.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| OnBoardMemoryMoreThanHalfFull | 10237 | Transfer data from the device when more than half of the onboard memory of the device fills. |
| OnBoardMemoryNotEmpty | 10241 | Transfer data from the device when there is data in the onboard memory. |
| OnBoardMemoryCustomThreshold | 12577 | Transfer data from the device when the number of samples specified with DataTransferCustomThreshold are in the device FIFO. |
| WhenAcquisitionComplete | 12546 | Transfer data when the acquisition is complete. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalchangedetectioneventargs-digitalchangedetectioneventargs.html language=enus -->
## TOPIC 01780: DigitalChangeDetectionEventArgs()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalchangedetectioneventargs-digitalchangedetectioneventargs.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalchangedetectioneventargs-digitalchangedetectioneventargs.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DigitalChangeDetectionEventArgs class. SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalChangeDetectionEventArgs()

### DigitalChangeDetectionEventArgs()

Initializes a new instance of the [DigitalChangeDetectionEventArgs](nationalinstruments-daqmx-digitalchangedetectioneventargs.html) class.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public DigitalChangeDetectionEventArgs()

Parent topic:

DigitalChangeDetectionEventArgs Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalchangedetectioneventargs-getobjectdata__serializationinfo-streamingcontext.html language=enus -->
## TOPIC 01781: GetObjectData(SerializationInfo, StreamingContext)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalchangedetectioneventargs-getobjectdata__serializationinfo-streamingcontext.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalchangedetectioneventargs-getobjectdata__serializationinfo-streamingcontext.html
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

DigitalChangeDetectionEventArgs Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalchangedetectioneventargs.html language=enus -->
## TOPIC 01782: DigitalChangeDetectionEventArgs Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalchangedetectioneventargs.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalchangedetectioneventargs.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides data for the DigitalChangeDetection event. Derives fromEventArgsISerializableSyntaxNamespace: NationalInstruments.DAQmxpublic class DigitalChangeDetectionEventArgs : EventArgs, ISerializableRemarksExample applications are located in the <Public Documents>\National Instruments\NI-DAQ\Example

### DigitalChangeDetectionEventArgs Class

Provides data for the [DigitalChangeDetection](nationalinstruments-daqmx-task-digitalchangedetection.html) event.

#### Derives from

- EventArgs
- ISerializable

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class DigitalChangeDetectionEventArgs : EventArgs, ISerializable

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| DigitalChangeDetectionEventArgs() | Initializes a new instance of the DigitalChangeDetectionEventArgs class. |

#### Methods

| Name | Description |
| --- | --- |
| GetObjectData(SerializationInfo, StreamingContext) | Sets the SerializationInfo object with information about the exception. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalchangedetectioneventhandler__object-digitalchangedetectioneventargs.html language=enus -->
## TOPIC 01783: DigitalChangeDetectionEventHandler Delegate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalchangedetectioneventhandler__object-digitalchangedetectioneventargs.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalchangedetectioneventhandler__object-digitalchangedetectioneventargs.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the method that handles the DigitalChangeDetection event. SyntaxNamespace: NationalInstrumentspublic delegate void DigitalChangeDetectionEventHandler(object sender, DigitalChangeDetectionEventArgs e)ParametersNameTypeDescriptionsenderobjectThe Task that caused this event.eDigitalChangeDet

### DigitalChangeDetectionEventHandler Delegate

Represents the method that handles the [DigitalChangeDetection](nationalinstruments-daqmx-task-digitalchangedetection.html) event.

#### Syntax

**Namespace:**NationalInstruments

public delegate void DigitalChangeDetectionEventHandler(object sender, DigitalChangeDetectionEventArgs e)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sender | object | The Task that caused this event. |
| e | DigitalChangeDetectionEventArgs | A DigitalChangeDetectionEventArgs that contains the event data. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgeadvancetrigger-digitalfilterenable.html language=enus -->
## TOPIC 01784: DigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgeadvancetrigger-digitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgeadvancetrigger-digitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This property is obsolete. Will warn if used (Deprecated) Specifies whether to apply the pulse width filter to the signal. SyntaxNamespace: NationalInstruments.DAQmxpublic bool DigitalFilterEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driv

### DigitalFilterEnable

**Obsolete: This property is obsolete. Will warn if used** 
(Deprecated) Specifies whether to apply the pulse width filter to the signal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalEdgeAdvanceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgeadvancetrigger-edge.html language=enus -->
## TOPIC 01785: Edge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgeadvancetrigger-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgeadvancetrigger-edge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This property is obsolete. Will warn if used (Deprecated) Specifies on which edge of a digital signal to advance to the next entry in a scan list. SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalEdgeAdvanceTriggerEdge Edge { get; set; }ExceptionsTypeDescriptionNationalInstruments.D

### Edge

**Obsolete: This property is obsolete. Will warn if used** 
(Deprecated) Specifies on which edge of a digital signal to advance to the next entry in a scan list.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DigitalEdgeAdvanceTriggerEdge](nationalinstruments-daqmx-digitaledgeadvancetriggeredge.html) Edge { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalEdgeAdvanceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgeadvancetrigger-source.html language=enus -->
## TOPIC 01786: Source

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgeadvancetrigger-source.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgeadvancetrigger-source.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This property is obsolete. Will warn if used (Deprecated) Specifies the name of a terminal where there is a digital signal to use as the source of the Advance Trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic string Source { get; set; }ExceptionsTypeDescriptionNationalInstruments.D

### Source

**Obsolete: This property is obsolete. Will warn if used** 
(Deprecated) Specifies the name of a [terminal](/csh?context=nidaqmx_mxcncpts_terminal) where there is a digital signal to use as the source of the Advance Trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Source { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalEdgeAdvanceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgeadvancetrigger-tostring.html language=enus -->
## TOPIC 01787: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgeadvancetrigger-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgeadvancetrigger-tostring.html
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

DigitalEdgeAdvanceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgeadvancetrigger.html language=enus -->
## TOPIC 01788: DigitalEdgeAdvanceTrigger Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgeadvancetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgeadvancetrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties to configure digital edge advance triggers. For more information, refer to AdvanceTrigger. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class DigitalEdgeAdvanceTrigger : MarshalByRefObject, IFilteredTypeDescriptorRemarksExa

### DigitalEdgeAdvanceTrigger Class

Contains properties to configure [digital edge](/csh?context=nidaqmx_mxcncpts_digtrigger) [advance triggers](/csh?context=nidaqmx_mxcncpts_adtrig). For more information, refer to [AdvanceTrigger](nationalinstruments-daqmx-advancetrigger.html).

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class DigitalEdgeAdvanceTrigger : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| DigitalFilterEnable | Obsolete: This property is obsolete. Will warn if used(Deprecated) Specifies whether to apply the pulse width filter to the signal. |
| Edge | Obsolete: This property is obsolete. Will warn if used(Deprecated) Specifies on which edge of a digital signal to advance to the next entry in a scan list. |
| Source | Obsolete: This property is obsolete. Will warn if used(Deprecated) Specifies the name of a terminal where there is a digital signal to use as the source of the Advance Trigger. |

#### Methods

| Name | Description |
| --- | --- |
| ToString() | Returns a string representation of the object. |

#### See Also

- AdvanceTrigger
- DigitalEdge

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgeadvancetriggeredge.html language=enus -->
## TOPIC 01789: DigitalEdgeAdvanceTriggerEdge Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgeadvancetriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgeadvancetriggeredge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This enum is obsolete. Will warn if used (Deprecated) Specifies on which edge of a digital signal to advance to the next entry in a scan list. SyntaxNamespace: NationalInstruments.DAQmxpublic enum DigitalEdgeAdvanceTriggerEdgeRemarks(Deprecated) Specifies on which edge of a digital signal

### DigitalEdgeAdvanceTriggerEdge Enumeration

**Obsolete: This enum is obsolete. Will warn if used** 
(Deprecated) Specifies on which edge of a digital signal to advance to the next entry in a scan list.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum DigitalEdgeAdvanceTriggerEdge

#### Remarks

(Deprecated) Specifies on which edge of a digital signal to advance to the next entry in a scan list. Use this enumeration to get or set the value of [Edge](nationalinstruments-daqmx-digitaledgeadvancetrigger-edge.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 10280 | Rising edge(s). |
| Falling | 10171 | Falling edge(s). |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgearmstarttrigger-digitalfilterenable.html language=enus -->
## TOPIC 01790: DigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgearmstarttrigger-digitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgearmstarttrigger-digitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the pulse width filter to the signal. SyntaxNamespace: NationalInstruments.DAQmxpublic bool DigitalFilterEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterEnable

Specifies whether to apply the pulse width [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) to the signal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalEdgeArmStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgearmstarttrigger-digitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 01791: DigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgearmstarttrigger-digitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgearmstarttrigger-digitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterMinimumPulseWidth

Specifies in seconds the minimum pulse width the [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) recognizes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalEdgeArmStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgearmstarttrigger-digitalfiltertimebaserate.html language=enus -->
## TOPIC 01792: DigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgearmstarttrigger-digitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgearmstarttrigger-digitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driv

### DigitalFilterTimebaseRate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalEdgeArmStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgearmstarttrigger-digitalfiltertimebasesource.html language=enus -->
## TOPIC 01793: DigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgearmstarttrigger-digitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgearmstarttrigger-digitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string DigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterTimebaseSource

Specifies the input [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the timebase of the pulse width filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string DigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalEdgeArmStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgearmstarttrigger-digitalsynchronizationenable.html language=enus -->
## TOPIC 01794: DigitalSynchronizationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgearmstarttrigger-digitalsynchronizationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgearmstarttrigger-digitalsynchronizationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic bool DigitalSynchronizationEnable { get; set; }RemarksThis property does not affect the minimum pulse width recognized by the device, but

### DigitalSynchronizationEnable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DigitalSynchronizationEnable { get; set; }

#### Remarks

This property does not affect the minimum pulse width recognized by the device, but setting this property to true does limit the speed at which the device recognizes transitions to less than the frequency of the internal timebase.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalEdgeArmStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgearmstarttrigger-edge.html language=enus -->
## TOPIC 01795: Edge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgearmstarttrigger-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgearmstarttrigger-edge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of a digital signal to arm the task for a Start Trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalEdgeArmStartTriggerEdge Edge { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Edge

Specifies on which edge of a digital signal to arm the task for a Start Trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DigitalEdgeArmStartTriggerEdge](nationalinstruments-daqmx-digitaledgearmstarttriggeredge.html) Edge { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalEdgeArmStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgearmstarttrigger-source.html language=enus -->
## TOPIC 01796: Source

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgearmstarttrigger-source.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgearmstarttrigger-source.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of a terminal where there is a digital signal to use as the source of the Arm Start Trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic string Source { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Source

Specifies the name of a [terminal](/csh?context=nidaqmx_mxcncpts_terminal) where there is a digital signal to use as the source of the Arm Start Trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Source { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalEdgeArmStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgearmstarttrigger-tostring.html language=enus -->
## TOPIC 01797: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgearmstarttrigger-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgearmstarttrigger-tostring.html
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

DigitalEdgeArmStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgearmstarttrigger.html language=enus -->
## TOPIC 01798: DigitalEdgeArmStartTrigger Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgearmstarttrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgearmstarttrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties to configure digital edge arm start triggers. For more information, refer to ArmStartTrigger. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class DigitalEdgeArmStartTrigger : MarshalByRefObject, IFilteredTypeDescriptorRemark

### DigitalEdgeArmStartTrigger Class

Contains properties to configure [digital edge](/csh?context=nidaqmx_mxcncpts_digtrigger) [arm start triggers](/csh?context=nidaqmx_mxcncpts_armtrig). For more information, refer to [ArmStartTrigger](nationalinstruments-daqmx-armstarttrigger.html).

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class DigitalEdgeArmStartTrigger : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| DigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
| DigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
| DigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
| DigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
| DigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
| Edge | Specifies on which edge of a digital signal to arm the task for a Start Trigger. |
| Source | Specifies the name of a terminal where there is a digital signal to use as the source of the Arm Start Trigger. |

#### Methods

| Name | Description |
| --- | --- |
| ToString() | Returns a string representation of the object. |

#### See Also

- ArmStartTrigger
- DigitalEdge

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgearmstarttriggeredge.html language=enus -->
## TOPIC 01799: DigitalEdgeArmStartTriggerEdge Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgearmstarttriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgearmstarttriggeredge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of a digital signal to arm the task for a Start Trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic enum DigitalEdgeArmStartTriggerEdgeRemarksSpecifies on which edge of a digital signal to arm the task for a Start Trigger. Use this enumeration to get or set the value of

### DigitalEdgeArmStartTriggerEdge Enumeration

Specifies on which edge of a digital signal to arm the task for a Start Trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum DigitalEdgeArmStartTriggerEdge

#### Remarks

Specifies on which edge of a digital signal to arm the task for a Start Trigger. Use this enumeration to get or set the value of [Edge](nationalinstruments-daqmx-digitaledgearmstarttrigger-edge.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 10280 | Rising edge(s). |
| Falling | 10171 | Falling edge(s). |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgereferencetrigger-digitalfilterenable.html language=enus -->
## TOPIC 01800: DigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgereferencetrigger-digitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgereferencetrigger-digitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply a digital filter to the trigger signal. SyntaxNamespace: NationalInstruments.DAQmxpublic bool DigitalFilterEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterEnable

Specifies whether to apply a digital [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) to the trigger signal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalEdgeReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgereferencetrigger-digitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 01801: DigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgereferencetrigger-digitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgereferencetrigger-digitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterMinimumPulseWidth

Specifies in seconds the minimum pulse width the [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) recognizes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalEdgeReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgereferencetrigger-digitalfiltertimebaserate.html language=enus -->
## TOPIC 01802: DigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgereferencetrigger-digitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgereferencetrigger-digitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver r

### DigitalFilterTimebaseRate

Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalEdgeReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgereferencetrigger-digitalfiltertimebasesource.html language=enus -->
## TOPIC 01803: DigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgereferencetrigger-digitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgereferencetrigger-digitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the timebase of the digital filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string DigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterTimebaseSource

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the timebase of the digital filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string DigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalEdgeReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgereferencetrigger-digitalsynchronizationenable.html language=enus -->
## TOPIC 01804: DigitalSynchronizationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgereferencetrigger-digitalsynchronizationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgereferencetrigger-digitalsynchronizationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic bool DigitalSynchronizationEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returne

### DigitalSynchronizationEnable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DigitalSynchronizationEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalEdgeReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgereferencetrigger-edge.html language=enus -->
## TOPIC 01805: Edge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgereferencetrigger-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgereferencetrigger-edge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on what edge of a digital pulse the Reference Trigger occurs. SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalEdgeReferenceTriggerEdge Edge { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Edge

Specifies on what edge of a digital pulse the [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger) occurs.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DigitalEdgeReferenceTriggerEdge](nationalinstruments-daqmx-digitaledgereferencetriggeredge.html) Edge { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalEdgeReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgereferencetrigger-source.html language=enus -->
## TOPIC 01806: Source

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgereferencetrigger-source.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgereferencetrigger-source.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of a terminal where there is a digital signal to use as the source of the Reference Trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic string Source { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Source

Specifies the name of a [terminal](/csh?context=nidaqmx_mxcncpts_terminal) where there is a digital signal to use as the source of the [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Source { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalEdgeReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgereferencetrigger-tostring.html language=enus -->
## TOPIC 01807: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgereferencetrigger-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgereferencetrigger-tostring.html
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

DigitalEdgeReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgereferencetrigger.html language=enus -->
## TOPIC 01808: DigitalEdgeReferenceTrigger Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgereferencetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgereferencetrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties to configure digital edge reference triggers. For more information, refer to ReferenceTrigger. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class DigitalEdgeReferenceTrigger : MarshalByRefObject, IFilteredTypeDescriptorRema

### DigitalEdgeReferenceTrigger Class

Contains properties to configure [digital edge](/csh?context=nidaqmx_mxcncpts_digtrigger) [reference triggers](/csh?context=nidaqmx_mxcncpts_referencetrigger). For more information, refer to [ReferenceTrigger](nationalinstruments-daqmx-referencetrigger.html).

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class DigitalEdgeReferenceTrigger : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| DigitalFilterEnable | Specifies whether to apply a digital filter to the trigger signal. |
| DigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
| DigitalFilterTimebaseRate | Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
| DigitalFilterTimebaseSource | Specifies the terminal of the signal to use as the timebase of the digital filter. |
| DigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
| Edge | Specifies on what edge of a digital pulse the Reference Trigger occurs. |
| Source | Specifies the name of a terminal where there is a digital signal to use as the source of the Reference Trigger. |

#### Methods

| Name | Description |
| --- | --- |
| ToString() | Returns a string representation of the object. |

#### See Also

- ReferenceTrigger
- DigitalEdge

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgereferencetriggeredge.html language=enus -->
## TOPIC 01809: DigitalEdgeReferenceTriggerEdge Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgereferencetriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgereferencetriggeredge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on what edge of a digital pulse the Reference Trigger occurs. SyntaxNamespace: NationalInstruments.DAQmxpublic enum DigitalEdgeReferenceTriggerEdgeRemarksSpecifies on what edge of a digital pulse the Reference Trigger occurs. Use this enumeration to get or set the value of Edge.MembersName

### DigitalEdgeReferenceTriggerEdge Enumeration

Specifies on what edge of a digital pulse the [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger) occurs.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum DigitalEdgeReferenceTriggerEdge

#### Remarks

Specifies on what edge of a digital pulse the [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger) occurs. Use this enumeration to get or set the value of [Edge](nationalinstruments-daqmx-digitaledgereferencetrigger-edge.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 10280 | Rising edge(s). |
| Falling | 10171 | Falling edge(s). |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgestarttrigger-digitalfilterenable.html language=enus -->
## TOPIC 01810: DigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgestarttrigger-digitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgestarttrigger-digitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply a digital filter to the trigger signal. SyntaxNamespace: NationalInstruments.DAQmxpublic bool DigitalFilterEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterEnable

Specifies whether to apply a digital [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) to the trigger signal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgestarttrigger-digitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 01811: DigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgestarttrigger-digitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgestarttrigger-digitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterMinimumPulseWidth

Specifies in seconds the minimum pulse width the [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) recognizes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgestarttrigger-digitalfiltertimebaserate.html language=enus -->
## TOPIC 01812: DigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgestarttrigger-digitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgestarttrigger-digitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driv

### DigitalFilterTimebaseRate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgestarttrigger-digitalfiltertimebasesource.html language=enus -->
## TOPIC 01813: DigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgestarttrigger-digitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgestarttrigger-digitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string DigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterTimebaseSource

Specifies the input [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the timebase of the pulse width filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string DigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgestarttrigger-digitalsynchronizationenable.html language=enus -->
## TOPIC 01814: DigitalSynchronizationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgestarttrigger-digitalsynchronizationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgestarttrigger-digitalsynchronizationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. If you set this property to true, the device does not recognize and act upon the trigger until the next pulse of the internal timebase. SyntaxNamespace: NationalInstruments.DAQmxpublic b

### DigitalSynchronizationEnable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. If you set this property to true, the device does not recognize and act upon the trigger until the next pulse of the internal timebase.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DigitalSynchronizationEnable { get; set; }

#### Remarks

This property does not affect the minimum pulse width recognized by the device, but setting this property to true does limit the speed at which the device recognizes transitions to less than the frequency of the internal timebase.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgestarttrigger-edge.html language=enus -->
## TOPIC 01815: Edge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgestarttrigger-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgestarttrigger-edge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of a digital pulse to start acquiring or generating samples. SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalEdgeStartTriggerEdge Edge { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Edge

Specifies on which edge of a digital pulse to start acquiring or generating samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DigitalEdgeStartTriggerEdge](nationalinstruments-daqmx-digitaledgestarttriggeredge.html) Edge { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgestarttrigger-source.html language=enus -->
## TOPIC 01816: Source

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgestarttrigger-source.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgestarttrigger-source.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of a terminal where there is a digital signal to use as the source of the Start Trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic string Source { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Source

Specifies the name of a [terminal](/csh?context=nidaqmx_mxcncpts_terminal) where there is a digital signal to use as the source of the Start Trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Source { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgestarttrigger-tostring.html language=enus -->
## TOPIC 01817: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgestarttrigger-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgestarttrigger-tostring.html
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

DigitalEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgestarttrigger.html language=enus -->
## TOPIC 01818: DigitalEdgeStartTrigger Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgestarttrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgestarttrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties to configure digital edge start triggers. For more information, refer to StartTrigger. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class DigitalEdgeStartTrigger : MarshalByRefObject, IFilteredTypeDescriptorRemarksExample a

### DigitalEdgeStartTrigger Class

Contains properties to configure [digital edge](/csh?context=nidaqmx_mxcncpts_digtrigger) [start triggers](/csh?context=nidaqmx_mxcncpts_starttrig). For more information, refer to [StartTrigger](nationalinstruments-daqmx-starttrigger.html).

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class DigitalEdgeStartTrigger : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| DigitalFilterEnable | Specifies whether to apply a digital filter to the trigger signal. |
| DigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
| DigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
| DigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
| DigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. If you set this property to true, the device does not recognize and act upon the trigger until the next pulse of the internal timebase. |
| Edge | Specifies on which edge of a digital pulse to start acquiring or generating samples. |
| Source | Specifies the name of a terminal where there is a digital signal to use as the source of the Start Trigger. |

#### Methods

| Name | Description |
| --- | --- |
| ToString() | Returns a string representation of the object. |

#### See Also

- StartTrigger
- DigitalEdge

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgestarttriggeredge.html language=enus -->
## TOPIC 01819: DigitalEdgeStartTriggerEdge Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgestarttriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgestarttriggeredge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of a digital pulse to start acquiring or generating samples. SyntaxNamespace: NationalInstruments.DAQmxpublic enum DigitalEdgeStartTriggerEdgeRemarksSpecifies on which edge of a digital pulse to start acquiring or generating samples. Use this enumeration to get or set the val

### DigitalEdgeStartTriggerEdge Enumeration

Specifies on which edge of a digital pulse to start acquiring or generating samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum DigitalEdgeStartTriggerEdge

#### Remarks

Specifies on which edge of a digital pulse to start acquiring or generating samples. Use this enumeration to get or set the value of [Edge](nationalinstruments-daqmx-digitaledgestarttrigger-edge.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 10280 | Rising edge(s). |
| Falling | 10171 | Falling edge(s). |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgewatchdogexpirationtrigger-edge.html language=enus -->
## TOPIC 01820: Edge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgewatchdogexpirationtrigger-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgewatchdogexpirationtrigger-edge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of a digital signal to expire the watchdog task. SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalEdgeWatchdogExpirationTriggerEdge Edge { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Edge

Specifies on which edge of a digital signal to expire the watchdog task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DigitalEdgeWatchdogExpirationTriggerEdge](nationalinstruments-daqmx-digitaledgewatchdogexpirationtriggeredge.html) Edge { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalEdgeWatchdogExpirationTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgewatchdogexpirationtrigger-source.html language=enus -->
## TOPIC 01821: Source

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgewatchdogexpirationtrigger-source.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgewatchdogexpirationtrigger-source.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of a terminal where a digital signal exists to use as the source of the Expiration Trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic string Source { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Source

Specifies the name of a [terminal](/csh?context=nidaqmx_mxcncpts_terminal) where a digital signal exists to use as the source of the Expiration Trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Source { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalEdgeWatchdogExpirationTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgewatchdogexpirationtrigger-tostring.html language=enus -->
## TOPIC 01822: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgewatchdogexpirationtrigger-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgewatchdogexpirationtrigger-tostring.html
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

DigitalEdgeWatchdogExpirationTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgewatchdogexpirationtrigger.html language=enus -->
## TOPIC 01823: DigitalEdgeWatchdogExpirationTrigger Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgewatchdogexpirationtrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgewatchdogexpirationtrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties to configure digital edge watchdog expiration triggers. For more information, refer to WatchdogExpirationTrigger. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class DigitalEdgeWatchdogExpirationTrigger : MarshalByRefObject,

### DigitalEdgeWatchdogExpirationTrigger Class

Contains properties to configure [digital edge](/csh?context=nidaqmx_mxcncpts_digtrigger) [watchdog expiration triggers](/csh?context=nidaqmx_mxcncpts_expirationtrigger). For more information, refer to [WatchdogExpirationTrigger](nationalinstruments-daqmx-watchdogexpirationtrigger.html).

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class DigitalEdgeWatchdogExpirationTrigger : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Edge | Specifies on which edge of a digital signal to expire the watchdog task. |
| Source | Specifies the name of a terminal where a digital signal exists to use as the source of the Expiration Trigger. |

#### Methods

| Name | Description |
| --- | --- |
| ToString() | Returns a string representation of the object. |

#### See Also

- WatchdogExpirationTrigger
- DigitalEdge

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitaledgewatchdogexpirationtriggeredge.html language=enus -->
## TOPIC 01824: DigitalEdgeWatchdogExpirationTriggerEdge Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitaledgewatchdogexpirationtriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitaledgewatchdogexpirationtriggeredge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of a digital signal to expire the watchdog task. SyntaxNamespace: NationalInstruments.DAQmxpublic enum DigitalEdgeWatchdogExpirationTriggerEdgeRemarksSpecifies on which edge of a digital signal to expire the watchdog task. Use this enumeration to get or set the value of Edge.

### DigitalEdgeWatchdogExpirationTriggerEdge Enumeration

Specifies on which edge of a digital signal to expire the watchdog task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum DigitalEdgeWatchdogExpirationTriggerEdge

#### Remarks

Specifies on which edge of a digital signal to expire the watchdog task. Use this enumeration to get or set the value of [Edge](nationalinstruments-daqmx-digitaledgewatchdogexpirationtrigger-edge.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 10280 | Rising edge(s). |
| Falling | 10171 | Falling edge(s). |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitallevelpausetrigger-condition.html language=enus -->
## TOPIC 01825: Condition

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitallevelpausetrigger-condition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitallevelpausetrigger-condition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the task pauses while the signal is high or low. SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalLevelPauseTriggerCondition Condition { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Condition

Specifies whether the task pauses while the signal is high or low.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DigitalLevelPauseTriggerCondition](nationalinstruments-daqmx-digitallevelpausetriggercondition.html) Condition { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalLevelPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitallevelpausetrigger-digitalfilterenable.html language=enus -->
## TOPIC 01826: DigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitallevelpausetrigger-digitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitallevelpausetrigger-digitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply a digital filter to the trigger signal. SyntaxNamespace: NationalInstruments.DAQmxpublic bool DigitalFilterEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterEnable

Specifies whether to apply a digital [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) to the trigger signal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalLevelPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitallevelpausetrigger-digitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 01827: DigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitallevelpausetrigger-digitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitallevelpausetrigger-digitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterMinimumPulseWidth

Specifies in seconds the minimum pulse width the [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) recognizes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalLevelPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitallevelpausetrigger-digitalfiltertimebaserate.html language=enus -->
## TOPIC 01828: DigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitallevelpausetrigger-digitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitallevelpausetrigger-digitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driv

### DigitalFilterTimebaseRate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalLevelPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitallevelpausetrigger-digitalfiltertimebasesource.html language=enus -->
## TOPIC 01829: DigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitallevelpausetrigger-digitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitallevelpausetrigger-digitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string DigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterTimebaseSource

Specifies the input [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the timebase of the pulse width filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string DigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalLevelPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitallevelpausetrigger-digitalsynchronizationenable.html language=enus -->
## TOPIC 01830: DigitalSynchronizationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitallevelpausetrigger-digitalsynchronizationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitallevelpausetrigger-digitalsynchronizationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic bool DigitalSynchronizationEnable { get; set; }RemarksThis property does not affect the minimum pulse width recognized by the device, but

### DigitalSynchronizationEnable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DigitalSynchronizationEnable { get; set; }

#### Remarks

This property does not affect the minimum pulse width recognized by the device, but setting this property to true does limit the speed at which the device recognizes transitions to less than the frequency of the internal timebase.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalLevelPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitallevelpausetrigger-source.html language=enus -->
## TOPIC 01831: Source

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitallevelpausetrigger-source.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitallevelpausetrigger-source.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of a terminal where there is a digital signal to use as the source of the Pause Trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic string Source { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Source

Specifies the name of a [terminal](/csh?context=nidaqmx_mxcncpts_terminal) where there is a digital signal to use as the source of the Pause Trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Source { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalLevelPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitallevelpausetrigger-tostring.html language=enus -->
## TOPIC 01832: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitallevelpausetrigger-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitallevelpausetrigger-tostring.html
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

DigitalLevelPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitallevelpausetrigger.html language=enus -->
## TOPIC 01833: DigitalLevelPauseTrigger Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitallevelpausetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitallevelpausetrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties to configure digital level pause triggers. For more information, refer to PauseTrigger. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class DigitalLevelPauseTrigger : MarshalByRefObject, IFilteredTypeDescriptorRemarksExample

### DigitalLevelPauseTrigger Class

Contains properties to configure [digital level](/csh?context=nidaqmx_mxcncpts_digtrigger) [pause triggers](/csh?context=nidaqmx_mxcncpts_pausetrigger). For more information, refer to [PauseTrigger](nationalinstruments-daqmx-pausetrigger.html).

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class DigitalLevelPauseTrigger : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Condition | Specifies whether the task pauses while the signal is high or low. |
| DigitalFilterEnable | Specifies whether to apply a digital filter to the trigger signal. |
| DigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
| DigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
| DigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
| DigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
| Source | Specifies the name of a terminal where there is a digital signal to use as the source of the Pause Trigger. |

#### Methods

| Name | Description |
| --- | --- |
| ToString() | Returns a string representation of the object. |

#### See Also

- PauseTrigger
- DigitalLevel

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitallevelpausetriggercondition.html language=enus -->
## TOPIC 01834: DigitalLevelPauseTriggerCondition Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitallevelpausetriggercondition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitallevelpausetriggercondition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the task pauses while the signal is high or low. SyntaxNamespace: NationalInstruments.DAQmxpublic enum DigitalLevelPauseTriggerConditionRemarksSpecifies whether the task pauses while the signal is high or low. Use this enumeration to get or set the value of Condition.MembersNameVal

### DigitalLevelPauseTriggerCondition Enumeration

Specifies whether the task pauses while the signal is high or low.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum DigitalLevelPauseTriggerCondition

#### Remarks

Specifies whether the task pauses while the signal is high or low. Use this enumeration to get or set the value of [Condition](nationalinstruments-daqmx-digitallevelpausetrigger-condition.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| High | 10192 | High state. |
| Low | 10214 | Low state. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportbyte__int-asynccallback-object-byte_arr2-reallocationpolicy.html language=enus -->
## TOPIC 01835: BeginMemoryOptimizedReadMultiSamplePortByte(int, AsyncCallback, object, byte, ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportbyte__int-asynccallback-object-byte_arr2-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportbyte__int-asynccallback-object-byte_arr2-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more 8-bit unsigned integer samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSamplePortByte(int samplesPerChannel, AsyncCallback callback, object state, byte[,] data,

### BeginMemoryOptimizedReadMultiSamplePortByte(int, AsyncCallback, object, byte, ReallocationPolicy)

Begins an asynchronous read of one or more 8-bit unsigned integer samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSamplePortByte(int samplesPerChannel, AsyncCallback callback, object state, byte[,] data, ReallocationPolicy policy)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSamplePortByte(IAsyncResult, out int)](nationalinstruments-daqmx-digitalmultichannelreader-endmemoryoptimizedreadmultisampleportbyte__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | byte | An initialized 2D array of 8-bit unsigned integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportbyte__int-asynccallback-object-byte_arr2.html language=enus -->
## TOPIC 01836: BeginMemoryOptimizedReadMultiSamplePortByte(int, AsyncCallback, object, byte)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportbyte__int-asynccallback-object-byte_arr2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportbyte__int-asynccallback-object-byte_arr2.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more 8-bit unsigned integer samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSamplePortByte(int samplesPerChannel, AsyncCallback callback, object state, byte[,] data)

### BeginMemoryOptimizedReadMultiSamplePortByte(int, AsyncCallback, object, byte)

Begins an asynchronous read of one or more 8-bit unsigned integer samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSamplePortByte(int samplesPerChannel, AsyncCallback callback, object state, byte[,] data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSamplePortByte(IAsyncResult, out int)](nationalinstruments-daqmx-digitalmultichannelreader-endmemoryoptimizedreadmultisampleportbyte__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | byte | An initialized 2D array of 8-bit unsigned integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportint32__int-asynccallback-object-int_arr2-reallocationpolicy.html language=enus -->
## TOPIC 01837: BeginMemoryOptimizedReadMultiSamplePortInt32(int, AsyncCallback, object, int, ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportint32__int-asynccallback-object-int_arr2-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportint32__int-asynccallback-object-int_arr2-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more 32-bit integer samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSamplePortInt32(int samplesPerChannel, AsyncCallback callback, object state, int[,] data, Realloc

### BeginMemoryOptimizedReadMultiSamplePortInt32(int, AsyncCallback, object, int, ReallocationPolicy)

Begins an asynchronous read of one or more 32-bit integer samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSamplePortInt32(int samplesPerChannel, AsyncCallback callback, object state, int[,] data, ReallocationPolicy policy)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | int | An initialized 2D array of one or more 32-bit integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportint32__int-asynccallback-object-int_arr2.html language=enus -->
## TOPIC 01838: BeginMemoryOptimizedReadMultiSamplePortInt32(int, AsyncCallback, object, int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportint32__int-asynccallback-object-int_arr2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportint32__int-asynccallback-object-int_arr2.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more 32-bit integer samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSamplePortInt32(int samplesPerChannel, AsyncCallback callback, object state, int[,] data)Paramete

### BeginMemoryOptimizedReadMultiSamplePortInt32(int, AsyncCallback, object, int)

Begins an asynchronous read of one or more 32-bit integer samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSamplePortInt32(int samplesPerChannel, AsyncCallback callback, object state, int[,] data)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | int | An initialized 2D array of one or more 32-bit integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportuint16__int-asynccallback-object-ushort_arr2-reallocationpolicy.html language=enus -->
## TOPIC 01839: BeginMemoryOptimizedReadMultiSamplePortUInt16(int, AsyncCallback, object, ushort, ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportuint16__int-asynccallback-object-ushort_arr2-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportuint16__int-asynccallback-object-ushort_arr2-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more 16-bit unsigned integer samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSamplePortUInt16(int samplesPerChannel, AsyncCallback callback, object state, ushort[,]

### BeginMemoryOptimizedReadMultiSamplePortUInt16(int, AsyncCallback, object, ushort, ReallocationPolicy)

Begins an asynchronous read of one or more 16-bit unsigned integer samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSamplePortUInt16(int samplesPerChannel, AsyncCallback callback, object state, ushort[,] data, ReallocationPolicy policy)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSamplePortUInt16(IAsyncResult, out int)](nationalinstruments-daqmx-digitalmultichannelreader-endmemoryoptimizedreadmultisampleportuint16__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | ushort | An initialized 2D array of 16-bit unsigned integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportuint16__int-asynccallback-object-ushort_arr2.html language=enus -->
## TOPIC 01840: BeginMemoryOptimizedReadMultiSamplePortUInt16(int, AsyncCallback, object, ushort)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportuint16__int-asynccallback-object-ushort_arr2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportuint16__int-asynccallback-object-ushort_arr2.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more 16-bit unsigned integer samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSamplePortUInt16(int samplesPerChannel, AsyncCallback callback, object state, ushort[,]

### BeginMemoryOptimizedReadMultiSamplePortUInt16(int, AsyncCallback, object, ushort)

Begins an asynchronous read of one or more 16-bit unsigned integer samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSamplePortUInt16(int samplesPerChannel, AsyncCallback callback, object state, ushort[,] data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSamplePortUInt16(IAsyncResult, out int)](nationalinstruments-daqmx-digitalmultichannelreader-endmemoryoptimizedreadmultisampleportuint16__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | ushort | An initialized 2D array of 16-bit unsigned integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportuint32__int-asynccallback-object-uint_arr2-reallocationpolicy.html language=enus -->
## TOPIC 01841: BeginMemoryOptimizedReadMultiSamplePortUInt32(int, AsyncCallback, object, uint, ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportuint32__int-asynccallback-object-uint_arr2-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportuint32__int-asynccallback-object-uint_arr2-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more 32-bit unsigned integer samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSamplePortUInt32(int samplesPerChannel, AsyncCallback callback, object state, uint[,] da

### BeginMemoryOptimizedReadMultiSamplePortUInt32(int, AsyncCallback, object, uint, ReallocationPolicy)

Begins an asynchronous read of one or more 32-bit unsigned integer samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSamplePortUInt32(int samplesPerChannel, AsyncCallback callback, object state, uint[,] data, ReallocationPolicy policy)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSamplePortUInt32(IAsyncResult, out int)](nationalinstruments-daqmx-digitalmultichannelreader-endmemoryoptimizedreadmultisampleportuint32__iasyncresult-out.html)

with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | uint | An initialized 2D array of 32-bit unsigned integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportuint32__int-asynccallback-object-uint_arr2.html language=enus -->
## TOPIC 01842: BeginMemoryOptimizedReadMultiSamplePortUInt32(int, AsyncCallback, object, uint)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportuint32__int-asynccallback-object-uint_arr2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportuint32__int-asynccallback-object-uint_arr2.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more 32-bit unsigned integer samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSamplePortUInt32(int samplesPerChannel, AsyncCallback callback, object state, uint[,] da

### BeginMemoryOptimizedReadMultiSamplePortUInt32(int, AsyncCallback, object, uint)

Begins an asynchronous read of one or more 32-bit unsigned integer samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSamplePortUInt32(int samplesPerChannel, AsyncCallback callback, object state, uint[,] data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSamplePortUInt32(IAsyncResult, out int)](nationalinstruments-daqmx-digitalmultichannelreader-endmemoryoptimizedreadmultisampleportuint32__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | uint | An initialized 2D array of 32-bit unsigned integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadsinglesamplemultiline__asynccallback-object-bool_arr2.html language=enus -->
## TOPIC 01843: BeginMemoryOptimizedReadSingleSampleMultiLine(AsyncCallback, object, bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadsinglesamplemultiline__asynccallback-object-bool_arr2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadsinglesamplemultiline__asynccallback-object-bool_arr2.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a single sample containing Boolean values from one or more DIChannel objects in a task. Each channel can contain multiple digital lines. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadSingleSampleMultiLine(AsyncCallback callback,

### BeginMemoryOptimizedReadSingleSampleMultiLine(AsyncCallback, object, bool)

Begins an asynchronous read of a single sample containing Boolean values from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task. Each channel can contain multiple digital lines.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadSingleSampleMultiLine(AsyncCallback callback, object state, bool[,] data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadSingleSampleMultiLine(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelreader-endmemoryoptimizedreadsinglesamplemultiline__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | bool | An initialized 2D array of Boolean samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a line in that channel. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-beginreadmultisampleportbyte__int-asynccallback-object.html language=enus -->
## TOPIC 01844: BeginReadMultiSamplePortByte(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-beginreadmultisampleportbyte__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-beginreadmultisampleportbyte__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more 8-bit unsigned integer samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadMultiSamplePortByte(int samplesPerChannel, AsyncCallback callback, object state)RemarksTo get the read data o

### BeginReadMultiSamplePortByte(int, AsyncCallback, object)

Begins an asynchronous read of one or more 8-bit unsigned integer samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadMultiSamplePortByte(int samplesPerChannel, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadMultiSamplePortByte(int, AsyncCallback, object), call [EndReadMultiSamplePortByte(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelreader-endreadmultisampleportbyte__iasyncresult.html) with the returned IAsyncResult.

Use this method for devices with up to eight lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-beginreadmultisampleportint16__int-asynccallback-object.html language=enus -->
## TOPIC 01845: BeginReadMultiSamplePortInt16(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-beginreadmultisampleportint16__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-beginreadmultisampleportint16__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more 16-bit integer samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadMultiSamplePortInt16(int samplesPerChannel, AsyncCallback callback, object state)RemarksTo get the read data or any e

### BeginReadMultiSamplePortInt16(int, AsyncCallback, object)

Begins an asynchronous read of one or more 16-bit integer samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadMultiSamplePortInt16(int samplesPerChannel, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadMultiSamplePortInt16(int, AsyncCallback, object), call [EndReadMultiSamplePortInt16(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelreader-endreadmultisampleportint16__iasyncresult.html) with the returned IAsyncResult.

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-beginreadmultisampleportint32__int-asynccallback-object.html language=enus -->
## TOPIC 01846: BeginReadMultiSamplePortInt32(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-beginreadmultisampleportint32__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-beginreadmultisampleportint32__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more 32-bit integer samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadMultiSamplePortInt32(int samplesPerChannel, AsyncCallback callback, object state)RemarksTo get the read data or any e

### BeginReadMultiSamplePortInt32(int, AsyncCallback, object)

Begins an asynchronous read of one or more 32-bit integer samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadMultiSamplePortInt32(int samplesPerChannel, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadMultiSamplePortInt32(int, AsyncCallback, object), call [EndReadMultiSamplePortInt32(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelreader-endreadmultisampleportint32__iasyncresult.html) with the returned IAsyncResult.

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-beginreadmultisampleportuint16__int-asynccallback-object.html language=enus -->
## TOPIC 01847: BeginReadMultiSamplePortUInt16(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-beginreadmultisampleportuint16__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-beginreadmultisampleportuint16__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more 16-bit unsigned integer samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadMultiSamplePortUInt16(int samplesPerChannel, AsyncCallback callback, object state)RemarksTo get the read dat

### BeginReadMultiSamplePortUInt16(int, AsyncCallback, object)

Begins an asynchronous read of one or more 16-bit unsigned integer samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadMultiSamplePortUInt16(int samplesPerChannel, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadMultiSamplePortUInt16(int, AsyncCallback, object), call [EndReadMultiSamplePortUInt16(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelreader-endreadmultisampleportuint16__iasyncresult.html) with the returned IAsyncResult.

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-beginreadmultisampleportuint32__int-asynccallback-object.html language=enus -->
## TOPIC 01848: BeginReadMultiSamplePortUInt32(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-beginreadmultisampleportuint32__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-beginreadmultisampleportuint32__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more 32-bit unsigned integer samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadMultiSamplePortUInt32(int samplesPerChannel, AsyncCallback callback, object state)RemarksTo get the read dat

### BeginReadMultiSamplePortUInt32(int, AsyncCallback, object)

Begins an asynchronous read of one or more 32-bit unsigned integer samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadMultiSamplePortUInt32(int samplesPerChannel, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadMultiSamplePortUInt32(int, AsyncCallback, object), call [EndReadMultiSamplePortUInt32(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelreader-endreadmultisampleportuint32__iasyncresult.html) with the returned IAsyncResult.

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesamplemultiline__asynccallback-object.html language=enus -->
## TOPIC 01849: BeginReadSingleSampleMultiLine(AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesamplemultiline__asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesamplemultiline__asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a single sample containing Boolean values from one or more DIChannel objects in a task. Each channel can contain multiple digital lines. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadSingleSampleMultiLine(AsyncCallback callback, object state)Re

### BeginReadSingleSampleMultiLine(AsyncCallback, object)

Begins an asynchronous read of a single sample containing Boolean values from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task. Each channel can contain multiple digital lines.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadSingleSampleMultiLine(AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSampleMultiLine(AsyncCallback, object), call [EndReadSingleSampleMultiLine(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesamplemultiline__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesampleportbyte__asynccallback-object.html language=enus -->
## TOPIC 01850: BeginReadSingleSamplePortByte(AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesampleportbyte__asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesampleportbyte__asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a single 8-bit unsigned integer sample from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadSingleSamplePortByte(AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occu

### BeginReadSingleSamplePortByte(AsyncCallback, object)

Begins an asynchronous read of a single 8-bit unsigned integer sample from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadSingleSamplePortByte(AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSamplePortByte(AsyncCallback, object), call [EndReadSingleSamplePortByte(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesampleportbyte__iasyncresult.html) with the returned IAsyncResult.

Use this method for devices with up to eight lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesampleportint16__asynccallback-object.html language=enus -->
## TOPIC 01851: BeginReadSingleSamplePortInt16(AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesampleportint16__asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesampleportint16__asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a single 16-bit integer sample from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadSingleSamplePortInt16(AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occurred du

### BeginReadSingleSamplePortInt16(AsyncCallback, object)

Begins an asynchronous read of a single 16-bit integer sample from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadSingleSamplePortInt16(AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSamplePortInt16(AsyncCallback, object), call [EndReadSingleSamplePortInt16(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesampleportint16__iasyncresult.html) with the returned IAsyncResult.

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesampleportint32__asynccallback-object.html language=enus -->
## TOPIC 01852: BeginReadSingleSamplePortInt32(AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesampleportint32__asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesampleportint32__asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a single 32-bit integer sample from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadSingleSamplePortInt32(AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occurred du

### BeginReadSingleSamplePortInt32(AsyncCallback, object)

Begins an asynchronous read of a single 32-bit integer sample from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadSingleSamplePortInt32(AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSamplePortInt32(AsyncCallback, object), call [EndReadSingleSamplePortInt32(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesampleportint32__iasyncresult.html) with the returned IAsyncResult.

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesampleportuint16__asynccallback-object.html language=enus -->
## TOPIC 01853: BeginReadSingleSamplePortUInt16(AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesampleportuint16__asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesampleportuint16__asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a single 16-bit unsigned integer sample from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadSingleSamplePortUInt16(AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that o

### BeginReadSingleSamplePortUInt16(AsyncCallback, object)

Begins an asynchronous read of a single 16-bit unsigned integer sample from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadSingleSamplePortUInt16(AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSamplePortUInt16(AsyncCallback, object), call [EndReadSingleSamplePortUInt16(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesampleportuint16__iasyncresult.html) with the returned IAsyncResult.

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesampleportuint32__asynccallback-object.html language=enus -->
## TOPIC 01854: BeginReadSingleSamplePortUInt32(AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesampleportuint32__asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesampleportuint32__asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a single 32-bit unsigned integer sample from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadSingleSamplePortUInt32(AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that o

### BeginReadSingleSamplePortUInt32(AsyncCallback, object)

Begins an asynchronous read of a single 32-bit unsigned integer sample from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadSingleSamplePortUInt32(AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSamplePortUInt32(AsyncCallback, object), call [EndReadSingleSamplePortUInt32(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesampleportuint32__iasyncresult.html) with the returned IAsyncResult.

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesamplesingleline__asynccallback-object.html language=enus -->
## TOPIC 01855: BeginReadSingleSampleSingleLine(AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesamplesingleline__asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesamplesingleline__asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a single Boolean sample from one or more DIChannel objects in a task. Each channel can contain a single digital line. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadSingleSampleSingleLine(AsyncCallback callback, object state)RemarksTo get the re

### BeginReadSingleSampleSingleLine(AsyncCallback, object)

Begins an asynchronous read of a single Boolean sample from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task. Each channel can contain a single digital line.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadSingleSampleSingleLine(AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSampleSingleLine(AsyncCallback, object), call [EndReadSingleSampleSingleLine(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesamplesingleline__iasyncresult.html) with the returned IAsyncResult.

The data returned from digital waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) you are reading from.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-beginreadwaveform__int-asynccallback-object.html language=enus -->
## TOPIC 01856: BeginReadWaveform(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-beginreadwaveform__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-beginreadwaveform__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more digital waveform samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadWaveform(int samplesPerChannel, AsyncCallback callback, object state)RemarksTo get the read data or any exceptions

### BeginReadWaveform(int, AsyncCallback, object)

Begins an asynchronous read of one or more digital waveform samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadWaveform(int samplesPerChannel, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadWaveform(int, AsyncCallback, object), call [EndReadWaveform(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelreader-endreadwaveform__iasyncresult.html) with the returned IAsyncResult.

The data returned from digital waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) you are reading from.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-beginreadwaveform__timespan-asynccallback-object.html language=enus -->
## TOPIC 01857: BeginReadWaveform(TimeSpan, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-beginreadwaveform__timespan-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-beginreadwaveform__timespan-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more digital waveform samples from one or more DIChannel objects in a task for a specified duration . SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadWaveform(TimeSpan duration, AsyncCallback callback, object state)RemarksTo get the read d

### BeginReadWaveform(TimeSpan, AsyncCallback, object)

Begins an asynchronous read of one or more digital waveform samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task for a specified *duration* .

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadWaveform(TimeSpan duration, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadWaveform(TimeSpan, AsyncCallback, object), call [EndReadWaveform(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelreader-endreadwaveform__iasyncresult.html), passing the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units when creating channels using the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) being read.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the [Stream](nationalinstruments-daqmx-task-stream.html) object used for the reads or writes.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| duration | TimeSpan | The duration of time to read the waveform. The duration specified must be long enough to read at least one sample at the configured SampleClockRate. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-digitalmultichannelreader__daqstream.html language=enus -->
## TOPIC 01858: DigitalMultiChannelReader(DaqStream)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-digitalmultichannelreader__daqstream.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-digitalmultichannelreader__daqstream.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of the DigitalMultiChannelReader class to read from the specified DaqStream. SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalMultiChannelReader(DaqStream stream)RemarksEach Task object contains a Stream property that serves as the connection point for readers to access

### DigitalMultiChannelReader(DaqStream)

Creates a new instance of the [DigitalMultiChannelReader](nationalinstruments-daqmx-digitalmultichannelreader.html) class to read from the specified [DaqStream](nationalinstruments-daqmx-daqstream.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public DigitalMultiChannelReader(DaqStream stream)

#### Remarks

Each [Task](nationalinstruments-daqmx-task.html) object contains a [Stream](nationalinstruments-daqmx-task-stream.html) property that serves as the connection point for readers to access the samples generated by that task.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| stream | DaqStream | The DaqStream to read. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-endmemoryoptimizedreadmultisampleportbyte__iasyncresult-out.html language=enus -->
## TOPIC 01859: EndMemoryOptimizedReadMultiSamplePortByte(IAsyncResult, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-endmemoryoptimizedreadmultisampleportbyte__iasyncresult-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-endmemoryoptimizedreadmultisampleportbyte__iasyncresult-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePortByte(int, AsyncCallback, object, byte[, ]) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic byte[,] EndMemoryOptimizedReadMultiSamplePortByte(IAsyncResult asyncResult, out in

### EndMemoryOptimizedReadMultiSamplePortByte(IAsyncResult, out int)

Handles the end of an asynchronous read initiated with [BeginMemoryOptimizedReadMultiSamplePortByte(int, AsyncCallback, object, byte[, ])](nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportbyte__int-asynccallback-object-byte_arr2.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public byte[,] EndMemoryOptimizedReadMultiSamplePortByte(IAsyncResult asyncResult, out int actualNumberOfSamplesPerChannelRead)

#### Remarks

If you call this method before the asynchronous read IAsyncResult is complete, it waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSamplePortByte(int, AsyncCallback, object, byte[, ]). |
| actualNumberOfSamplesPerChannelRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A 2D array of 8-bit unsigned integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSamplePortByte(int, AsyncCallback, object, byte[, ]). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-endmemoryoptimizedreadmultisampleportint32__iasyncresult-out.html language=enus -->
## TOPIC 01860: EndMemoryOptimizedReadMultiSamplePortInt32(IAsyncResult, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-endmemoryoptimizedreadmultisampleportint32__iasyncresult-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-endmemoryoptimizedreadmultisampleportint32__iasyncresult-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePortInt32(int, AsyncCallback, object, int[, ]) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic int[,] EndMemoryOptimizedReadMultiSamplePortInt32(IAsyncResult asyncResult, out in

### EndMemoryOptimizedReadMultiSamplePortInt32(IAsyncResult, out int)

Handles the end of an asynchronous read initiated with [BeginMemoryOptimizedReadMultiSamplePortInt32(int, AsyncCallback, object, int[, ])](nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportint32__int-asynccallback-object-int_arr2.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int[,] EndMemoryOptimizedReadMultiSamplePortInt32(IAsyncResult asyncResult, out int actualNumberOfSamplesPerChannelRead)

#### Remarks

If you call this method before the asynchronous read IAsyncResult is complete, it waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSamplePortInt32(int, AsyncCallback, object, int[, ]). |
| actualNumberOfSamplesPerChannelRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A 2D array of 32-bit integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSamplePortInt32(int, AsyncCallback, object, int[, ]). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-endmemoryoptimizedreadmultisampleportuint16__iasyncresult-out.html language=enus -->
## TOPIC 01861: EndMemoryOptimizedReadMultiSamplePortUInt16(IAsyncResult, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-endmemoryoptimizedreadmultisampleportuint16__iasyncresult-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-endmemoryoptimizedreadmultisampleportuint16__iasyncresult-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePortUInt16(int, AsyncCallback, object, ushort[, ]) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic ushort[,] EndMemoryOptimizedReadMultiSamplePortUInt16(IAsyncResult asyncResult

### EndMemoryOptimizedReadMultiSamplePortUInt16(IAsyncResult, out int)

Handles the end of an asynchronous read initiated with [BeginMemoryOptimizedReadMultiSamplePortUInt16(int, AsyncCallback, object, ushort[, ])](nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportuint16__int-asynccallback-object-ushort_arr2.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public ushort[,] EndMemoryOptimizedReadMultiSamplePortUInt16(IAsyncResult asyncResult, out int actualNumberOfSamplesPerChannelRead)

#### Remarks

If you call this method before the asynchronous read IAsyncResult is complete, it waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSamplePortUInt16(int, AsyncCallback, object, ushort[, ]). |
| actualNumberOfSamplesPerChannelRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A 2D array of 16-bit unsigned integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSamplePortUInt16(int, AsyncCallback, object, ushort[, ]). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-endmemoryoptimizedreadmultisampleportuint32__iasyncresult-out.html language=enus -->
## TOPIC 01862: EndMemoryOptimizedReadMultiSamplePortUInt32(IAsyncResult, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-endmemoryoptimizedreadmultisampleportuint32__iasyncresult-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-endmemoryoptimizedreadmultisampleportuint32__iasyncresult-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePortUInt32(int, AsyncCallback, object, uint[, ]) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic uint[,] EndMemoryOptimizedReadMultiSamplePortUInt32(IAsyncResult asyncResult, ou

### EndMemoryOptimizedReadMultiSamplePortUInt32(IAsyncResult, out int)

Handles the end of an asynchronous read initiated with [BeginMemoryOptimizedReadMultiSamplePortUInt32(int, AsyncCallback, object, uint[, ])](nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportuint32__int-asynccallback-object-uint_arr2.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint[,] EndMemoryOptimizedReadMultiSamplePortUInt32(IAsyncResult asyncResult, out int actualNumberOfSamplesPerChannelRead)

#### Remarks

If you call this method before the asynchronous read IAsyncResult is complete, it waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSamplePortUInt32(int, AsyncCallback, object, uint[, ]). |
| actualNumberOfSamplesPerChannelRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A 2D array of 32-bit unsigned integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSamplePortUInt32(int, AsyncCallback, object, uint[, ]). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-endmemoryoptimizedreadsinglesamplemultiline__iasyncresult.html language=enus -->
## TOPIC 01863: EndMemoryOptimizedReadSingleSampleMultiLine(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-endmemoryoptimizedreadsinglesamplemultiline__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-endmemoryoptimizedreadsinglesamplemultiline__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadSingleSampleMultiLine(AsyncCallback, object, bool[, ]) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic bool[,] EndMemoryOptimizedReadSingleSampleMultiLine(IAsyncResult asyncResult)RemarksI

### EndMemoryOptimizedReadSingleSampleMultiLine(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginMemoryOptimizedReadSingleSampleMultiLine(AsyncCallback, object, bool[, ])](nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadsinglesamplemultiline__asynccallback-object-bool_arr2.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool[,] EndMemoryOptimizedReadSingleSampleMultiLine(IAsyncResult asyncResult)

#### Remarks

If you call this method before the asynchronous read is complete, it waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadSingleSampleMultiLine(AsyncCallback, object, bool[, ]). |

#### Returns

A 2D array of Boolean samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a line in that channel. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadSingleSampleMultiLine(AsyncCallback, object, bool[, ]). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-endreadmultisampleportbyte__iasyncresult.html language=enus -->
## TOPIC 01864: EndReadMultiSamplePortByte(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-endreadmultisampleportbyte__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-endreadmultisampleportbyte__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortByte(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic byte[,] EndReadMultiSamplePortByte(IAsyncResult asyncResult)RemarksIf you call EndReadMultiSamplePortByte(I

### EndReadMultiSamplePortByte(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadMultiSamplePortByte(int, AsyncCallback, object)](nationalinstruments-daqmx-digitalmultichannelreader-beginreadmultisampleportbyte__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public byte[,] EndReadMultiSamplePortByte(IAsyncResult asyncResult)

#### Remarks

If you call EndReadMultiSamplePortByte(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSamplePortByte(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSamplePortByte(int, AsyncCallback, object). |

#### Returns

A 2D array of 8-bit unsigned integer samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each channel. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadMultiSamplePortByte(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-endreadmultisampleportint16__iasyncresult.html language=enus -->
## TOPIC 01865: EndReadMultiSamplePortInt16(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-endreadmultisampleportint16__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-endreadmultisampleportint16__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortInt16(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic short[,] EndReadMultiSamplePortInt16(IAsyncResult asyncResult)RemarksIf you call EndReadMultiSamplePortInt

### EndReadMultiSamplePortInt16(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadMultiSamplePortInt16(int, AsyncCallback, object)](nationalinstruments-daqmx-digitalmultichannelreader-beginreadmultisampleportint16__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public short[,] EndReadMultiSamplePortInt16(IAsyncResult asyncResult)

#### Remarks

If you call EndReadMultiSamplePortInt16(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSamplePortInt16(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSamplePortInt16(int, AsyncCallback, object). |

#### Returns

A 2D array of 16-bit integer samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each channel. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadMultiSamplePortInt16(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-endreadmultisampleportint32__iasyncresult.html language=enus -->
## TOPIC 01866: EndReadMultiSamplePortInt32(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-endreadmultisampleportint32__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-endreadmultisampleportint32__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortInt32(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic int[,] EndReadMultiSamplePortInt32(IAsyncResult asyncResult)RemarksIf you call EndReadMultiSamplePortInt32

### EndReadMultiSamplePortInt32(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadMultiSamplePortInt32(int, AsyncCallback, object)](nationalinstruments-daqmx-digitalmultichannelreader-beginreadmultisampleportint32__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int[,] EndReadMultiSamplePortInt32(IAsyncResult asyncResult)

#### Remarks

If you call EndReadMultiSamplePortInt32(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSamplePortInt32(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSamplePortInt32(int, AsyncCallback, object). |

#### Returns

A 2D array of 32-bit integer samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each channel. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadMultiSamplePortInt32(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-endreadmultisampleportuint16__iasyncresult.html language=enus -->
## TOPIC 01867: EndReadMultiSamplePortUInt16(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-endreadmultisampleportuint16__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-endreadmultisampleportuint16__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortUInt16(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic ushort[,] EndReadMultiSamplePortUInt16(IAsyncResult asyncResult)RemarksIf you call EndReadMultiSamplePort

### EndReadMultiSamplePortUInt16(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadMultiSamplePortUInt16(int, AsyncCallback, object)](nationalinstruments-daqmx-digitalmultichannelreader-beginreadmultisampleportuint16__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public ushort[,] EndReadMultiSamplePortUInt16(IAsyncResult asyncResult)

#### Remarks

If you call EndReadMultiSamplePortUInt16(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSamplePortUInt16(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSamplePortUInt16(int, AsyncCallback, object). |

#### Returns

A 2D array of 16-bit unsigned integer samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each channel. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadMultiSamplePortUInt16(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-endreadmultisampleportuint32__iasyncresult.html language=enus -->
## TOPIC 01868: EndReadMultiSamplePortUInt32(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-endreadmultisampleportuint32__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-endreadmultisampleportuint32__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortUInt32(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic uint[,] EndReadMultiSamplePortUInt32(IAsyncResult asyncResult)RemarksIf you call EndReadMultiSamplePortUI

### EndReadMultiSamplePortUInt32(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadMultiSamplePortUInt32(int, AsyncCallback, object)](nationalinstruments-daqmx-digitalmultichannelreader-beginreadmultisampleportuint32__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint[,] EndReadMultiSamplePortUInt32(IAsyncResult asyncResult)

#### Remarks

If you call EndReadMultiSamplePortUInt32(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSamplePortUInt32(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSamplePortUInt32(int, AsyncCallback, object). |

#### Returns

A 2D array of 32-bit unsigned integer samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each channel. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadMultiSamplePortUInt32(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesamplemultiline__iasyncresult.html language=enus -->
## TOPIC 01869: EndReadSingleSampleMultiLine(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesamplemultiline__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesamplemultiline__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadSingleSampleMultiLine(AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic bool[,] EndReadSingleSampleMultiLine(IAsyncResult asyncResult)RemarksIf you call EndReadSingleSampleMultiLine(

### EndReadSingleSampleMultiLine(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadSingleSampleMultiLine(AsyncCallback, object)](nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesamplemultiline__asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool[,] EndReadSingleSampleMultiLine(IAsyncResult asyncResult)

#### Remarks

If you call EndReadSingleSampleMultiLine(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSampleMultiLine(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSampleMultiLine(AsyncCallback, object). |

#### Returns

A 2D array of Boolean samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a line in that channel. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadSingleSampleMultiLine(AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesampleportbyte__iasyncresult.html language=enus -->
## TOPIC 01870: EndReadSingleSamplePortByte(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesampleportbyte__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesampleportbyte__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortByte(AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic byte[] EndReadSingleSamplePortByte(IAsyncResult asyncResult)RemarksIf you call EndReadSingleSamplePortByte(IAsy

### EndReadSingleSamplePortByte(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadSingleSamplePortByte(AsyncCallback, object)](nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesampleportbyte__asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public byte[] EndReadSingleSamplePortByte(IAsyncResult asyncResult)

#### Remarks

If you call EndReadSingleSamplePortByte(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSamplePortByte(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSamplePortByte(AsyncCallback, object). |

#### Returns

A 1D array of 8-bit unsigned integer samples from the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadSingleSamplePortByte(AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesampleportint16__iasyncresult.html language=enus -->
## TOPIC 01871: EndReadSingleSamplePortInt16(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesampleportint16__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesampleportint16__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortInt16(AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic short[] EndReadSingleSamplePortInt16(IAsyncResult asyncResult)RemarksIf you call EndReadSingleSamplePortInt16(

### EndReadSingleSamplePortInt16(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadSingleSamplePortInt16(AsyncCallback, object)](nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesampleportint16__asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public short[] EndReadSingleSamplePortInt16(IAsyncResult asyncResult)

#### Remarks

If you call EndReadSingleSamplePortInt16(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSamplePortInt16(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSamplePortInt16(AsyncCallback, object). |

#### Returns

A 1D array of 16-bit integer samples from the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadSingleSamplePortInt16(AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesampleportint32__iasyncresult.html language=enus -->
## TOPIC 01872: EndReadSingleSamplePortInt32(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesampleportint32__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesampleportint32__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortInt32(AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic int[] EndReadSingleSamplePortInt32(IAsyncResult asyncResult)RemarksIf you call EndReadSingleSamplePortInt32(IA

### EndReadSingleSamplePortInt32(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadSingleSamplePortInt32(AsyncCallback, object)](nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesampleportint32__asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int[] EndReadSingleSamplePortInt32(IAsyncResult asyncResult)

#### Remarks

If you call EndReadSingleSamplePortInt32(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSamplePortInt32(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSamplePortInt32(AsyncCallback, object). |

#### Returns

A 1D array of 32-bit integer samples from the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadSingleSamplePortInt32(AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesampleportuint16__iasyncresult.html language=enus -->
## TOPIC 01873: EndReadSingleSamplePortUInt16(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesampleportuint16__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesampleportuint16__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortUInt16(AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic ushort[] EndReadSingleSamplePortUInt16(IAsyncResult asyncResult)RemarksIf you call EndReadSingleSamplePortUIn

### EndReadSingleSamplePortUInt16(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadSingleSamplePortUInt16(AsyncCallback, object)](nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesampleportuint16__asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public ushort[] EndReadSingleSamplePortUInt16(IAsyncResult asyncResult)

#### Remarks

If you call EndReadSingleSamplePortUInt16(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSamplePortUInt16(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSamplePortUInt16(AsyncCallback, object). |

#### Returns

A 1D array of 16-bit unsigned integer samples from the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadSingleSamplePortUInt16(AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesampleportuint32__iasyncresult.html language=enus -->
## TOPIC 01874: EndReadSingleSamplePortUInt32(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesampleportuint32__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesampleportuint32__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortUInt32(AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic uint[] EndReadSingleSamplePortUInt32(IAsyncResult asyncResult)RemarksIf you call EndReadSingleSamplePortUInt3

### EndReadSingleSamplePortUInt32(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadSingleSamplePortUInt32(AsyncCallback, object)](nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesampleportuint32__asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint[] EndReadSingleSamplePortUInt32(IAsyncResult asyncResult)

#### Remarks

If you call EndReadSingleSamplePortUInt32(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSamplePortUInt32(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSamplePortUInt32(AsyncCallback, object). |

#### Returns

A 1D array of 32-bit unsigned integer samples from the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadSingleSamplePortUInt32(AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesamplesingleline__iasyncresult.html language=enus -->
## TOPIC 01875: EndReadSingleSampleSingleLine(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesamplesingleline__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-endreadsinglesamplesingleline__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadSingleSampleSingleLine(AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic bool[] EndReadSingleSampleSingleLine(IAsyncResult asyncResult)RemarksIf you call EndReadSingleSampleSingleLin

### EndReadSingleSampleSingleLine(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadSingleSampleSingleLine(AsyncCallback, object)](nationalinstruments-daqmx-digitalmultichannelreader-beginreadsinglesamplesingleline__asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool[] EndReadSingleSampleSingleLine(IAsyncResult asyncResult)

#### Remarks

If you call EndReadSingleSampleSingleLine(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSampleSingleLine(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSampleSingleLine(AsyncCallback, object). |

#### Returns

A 1D array of Boolean samples from the task. Each element of the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadSingleSampleSingleLine(AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-endreadwaveform__iasyncresult.html language=enus -->
## TOPIC 01876: EndReadWaveform(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-endreadwaveform__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-endreadwaveform__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadWaveform(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalWaveform[] EndReadWaveform(IAsyncResult asyncResult)RemarksIf you call EndReadWaveform(IAsyncResult) before the

### EndReadWaveform(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadWaveform(int, AsyncCallback, object)](nationalinstruments-daqmx-digitalmultichannelreader-beginreadwaveform__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public DigitalWaveform[] EndReadWaveform(IAsyncResult asyncResult)

#### Remarks

If you call EndReadWaveform(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadWaveform(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadWaveform(int, AsyncCallback, object). |

#### Returns

A 1D array of DigitalWaveform objects containing samples from the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadWaveform(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-memoryoptimizedreadmultisampleportbyte__int-ref-out.html language=enus -->
## TOPIC 01877: MemoryOptimizedReadMultiSamplePortByte(int, ref byte, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-memoryoptimizedreadmultisampleportbyte__int-ref-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-memoryoptimizedreadmultisampleportbyte__int-ref-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 8-bit unsigned integer samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic byte[,] MemoryOptimizedReadMultiSamplePortByte(int samplesPerChannel, ref byte[,] data, out int actualNumberOfSamplesPerChannelRead)RemarksIf the data buffe

### MemoryOptimizedReadMultiSamplePortByte(int, ref byte, out int)

Reads one or more 8-bit unsigned integer samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public byte[,] MemoryOptimizedReadMultiSamplePortByte(int samplesPerChannel, ref byte[,] data, out int actualNumberOfSamplesPerChannelRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref byte | An initialized 2D array of 8-bit unsigned integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| actualNumberOfSamplesPerChannelRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; or If the first dimension of data does not match the number of channels. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-memoryoptimizedreadmultisampleportbyte__int-ref-reallocationpolicy-out.html language=enus -->
## TOPIC 01878: MemoryOptimizedReadMultiSamplePortByte(int, ref byte, ReallocationPolicy, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-memoryoptimizedreadmultisampleportbyte__int-ref-reallocationpolicy-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-memoryoptimizedreadmultisampleportbyte__int-ref-reallocationpolicy-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 8-bit unsigned integer samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic byte[,] MemoryOptimizedReadMultiSamplePortByte(int samplesPerChannel, ref byte[,] data, ReallocationPolicy policy, out int actualNumberOfSamplesPerChannelRe

### MemoryOptimizedReadMultiSamplePortByte(int, ref byte, ReallocationPolicy, out int)

Reads one or more 8-bit unsigned integer samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public byte[,] MemoryOptimizedReadMultiSamplePortByte(int samplesPerChannel, ref byte[,] data, ReallocationPolicy policy, out int actualNumberOfSamplesPerChannelRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref byte | An initialized 2D array of 8-bit unsigned integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |
| actualNumberOfSamplesPerChannelRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-memoryoptimizedreadmultisampleportint32__int-ref-out.html language=enus -->
## TOPIC 01879: MemoryOptimizedReadMultiSamplePortInt32(int, ref int, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-memoryoptimizedreadmultisampleportint32__int-ref-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-memoryoptimizedreadmultisampleportint32__int-ref-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 32-bit integer samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic int[,] MemoryOptimizedReadMultiSamplePortInt32(int samplesPerChannel, ref int[,] data, out int actualNumberOfSamplesPerChannelRead)RemarksIf the data buffer is larg

### MemoryOptimizedReadMultiSamplePortInt32(int, ref int, out int)

Reads one or more 32-bit integer samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int[,] MemoryOptimizedReadMultiSamplePortInt32(int samplesPerChannel, ref int[,] data, out int actualNumberOfSamplesPerChannelRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref int | An initialized 2D array of 32-bit integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| actualNumberOfSamplesPerChannelRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; or If the first dimension of data does not match the number of channels. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-memoryoptimizedreadmultisampleportint32__int-ref-reallocationpolicy-out.html language=enus -->
## TOPIC 01880: MemoryOptimizedReadMultiSamplePortInt32(int, ref int, ReallocationPolicy, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-memoryoptimizedreadmultisampleportint32__int-ref-reallocationpolicy-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-memoryoptimizedreadmultisampleportint32__int-ref-reallocationpolicy-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 32-bit integer samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic int[,] MemoryOptimizedReadMultiSamplePortInt32(int samplesPerChannel, ref int[,] data, ReallocationPolicy policy, out int actualNumberOfSamplesPerChannelRead)Remark

### MemoryOptimizedReadMultiSamplePortInt32(int, ref int, ReallocationPolicy, out int)

Reads one or more 32-bit integer samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int[,] MemoryOptimizedReadMultiSamplePortInt32(int samplesPerChannel, ref int[,] data, ReallocationPolicy policy, out int actualNumberOfSamplesPerChannelRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref int | An initialized 2D array of 32-bit integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |
| actualNumberOfSamplesPerChannelRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-memoryoptimizedreadmultisampleportuint16__int-ref-out.html language=enus -->
## TOPIC 01881: MemoryOptimizedReadMultiSamplePortUInt16(int, ref ushort, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-memoryoptimizedreadmultisampleportuint16__int-ref-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-memoryoptimizedreadmultisampleportuint16__int-ref-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 16-bit unsigned integer samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic ushort[,] MemoryOptimizedReadMultiSamplePortUInt16(int samplesPerChannel, ref ushort[,] data, out int actualNumberOfSamplesPerChannelRead)RemarksIf the dat

### MemoryOptimizedReadMultiSamplePortUInt16(int, ref ushort, out int)

Reads one or more 16-bit unsigned integer samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public ushort[,] MemoryOptimizedReadMultiSamplePortUInt16(int samplesPerChannel, ref ushort[,] data, out int actualNumberOfSamplesPerChannelRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref ushort | An initialized 2D array of 16-bit unsigned integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| actualNumberOfSamplesPerChannelRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; or If the first dimension of data does not match the number of channels. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-memoryoptimizedreadmultisampleportuint16__int-ref-reallocationpolicy-out.html language=enus -->
## TOPIC 01882: MemoryOptimizedReadMultiSamplePortUInt16(int, ref ushort, ReallocationPolicy, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-memoryoptimizedreadmultisampleportuint16__int-ref-reallocationpolicy-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-memoryoptimizedreadmultisampleportuint16__int-ref-reallocationpolicy-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 16-bit unsigned integer samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic ushort[,] MemoryOptimizedReadMultiSamplePortUInt16(int samplesPerChannel, ref ushort[,] data, ReallocationPolicy policy, out int actualNumberOfSamplesPerCh

### MemoryOptimizedReadMultiSamplePortUInt16(int, ref ushort, ReallocationPolicy, out int)

Reads one or more 16-bit unsigned integer samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public ushort[,] MemoryOptimizedReadMultiSamplePortUInt16(int samplesPerChannel, ref ushort[,] data, ReallocationPolicy policy, out int actualNumberOfSamplesPerChannelRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref ushort | An initialized 2D array of 16-bit unsigned integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |
| actualNumberOfSamplesPerChannelRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-memoryoptimizedreadmultisampleportuint32__int-ref-out.html language=enus -->
## TOPIC 01883: MemoryOptimizedReadMultiSamplePortUInt32(int, ref uint, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-memoryoptimizedreadmultisampleportuint32__int-ref-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-memoryoptimizedreadmultisampleportuint32__int-ref-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 32-bit unsigned integer samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic uint[,] MemoryOptimizedReadMultiSamplePortUInt32(int samplesPerChannel, ref uint[,] data, out int actualNumberOfSamplesPerChannelRead)RemarksIf the data bu

### MemoryOptimizedReadMultiSamplePortUInt32(int, ref uint, out int)

Reads one or more 32-bit unsigned integer samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint[,] MemoryOptimizedReadMultiSamplePortUInt32(int samplesPerChannel, ref uint[,] data, out int actualNumberOfSamplesPerChannelRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref uint | An initialized 2D array of 32-bit unsigned integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| actualNumberOfSamplesPerChannelRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; or If the first dimension of data does not match the number of channels. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-memoryoptimizedreadmultisampleportuint32__int-ref-reallocationpolicy-out.html language=enus -->
## TOPIC 01884: MemoryOptimizedReadMultiSamplePortUInt32(int, ref uint, ReallocationPolicy, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-memoryoptimizedreadmultisampleportuint32__int-ref-reallocationpolicy-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-memoryoptimizedreadmultisampleportuint32__int-ref-reallocationpolicy-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 32-bit unsigned integer samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic uint[,] MemoryOptimizedReadMultiSamplePortUInt32(int samplesPerChannel, ref uint[,] data, ReallocationPolicy policy, out int actualNumberOfSamplesPerChanne

### MemoryOptimizedReadMultiSamplePortUInt32(int, ref uint, ReallocationPolicy, out int)

Reads one or more 32-bit unsigned integer samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint[,] MemoryOptimizedReadMultiSamplePortUInt32(int samplesPerChannel, ref uint[,] data, ReallocationPolicy policy, out int actualNumberOfSamplesPerChannelRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref uint | An initialized 2D array of 32-bit unsigned integer samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |
| actualNumberOfSamplesPerChannelRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-memoryoptimizedreadsinglesamplemultiline__bool_arr2.html language=enus -->
## TOPIC 01885: MemoryOptimizedReadSingleSampleMultiLine(bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-memoryoptimizedreadsinglesamplemultiline__bool_arr2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-memoryoptimizedreadsinglesamplemultiline__bool_arr2.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single sample containing Boolean values from one or more DIChannel objects in a task. Each channel can contain multiple digital lines. SyntaxNamespace: NationalInstruments.DAQmxpublic bool[,] MemoryOptimizedReadSingleSampleMultiLine(bool[,] data)RemarksIf the data buffer is large enough to h

### MemoryOptimizedReadSingleSampleMultiLine(bool)

Reads a single sample containing Boolean values from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task. Each channel can contain multiple digital lines.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool[,] MemoryOptimizedReadSingleSampleMultiLine(bool[,] data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| data | bool | An initialized 2D array of boolean samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a line in that channel. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; or If the first dimension of data does not match the number of channels. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-readmultisampleportbyte__int.html language=enus -->
## TOPIC 01886: ReadMultiSamplePortByte(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-readmultisampleportbyte__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-readmultisampleportbyte__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 8-bit unsigned integer samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic byte[,] ReadMultiSamplePortByte(int samplesPerChannel)RemarksUse this method for devices with up to eight lines per port.NI-DAQmx read and write methods tim

### ReadMultiSamplePortByte(int)

Reads one or more 8-bit unsigned integer samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public byte[,] ReadMultiSamplePortByte(int samplesPerChannel)

#### Remarks

Use this method for devices with up to eight lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 2D array of 8-bit unsigned integer samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each channel. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-readmultisampleportint16__int.html language=enus -->
## TOPIC 01887: ReadMultiSamplePortInt16(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-readmultisampleportint16__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-readmultisampleportint16__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 16-bit integer samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic short[,] ReadMultiSamplePortInt16(int samplesPerChannel)RemarksUse this method for devices with up to 16 lines per port.NI-DAQmx read and write methods time out aft

### ReadMultiSamplePortInt16(int)

Reads one or more 16-bit integer samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public short[,] ReadMultiSamplePortInt16(int samplesPerChannel)

#### Remarks

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 2D array of 16-bit integer samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each channel. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-readmultisampleportint32__int.html language=enus -->
## TOPIC 01888: ReadMultiSamplePortInt32(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-readmultisampleportint32__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-readmultisampleportint32__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 32-bit integer samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic int[,] ReadMultiSamplePortInt32(int samplesPerChannel)RemarksUse this method for devices with up to 32 lines per port.NI-DAQmx read and write methods time out after

### ReadMultiSamplePortInt32(int)

Reads one or more 32-bit integer samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int[,] ReadMultiSamplePortInt32(int samplesPerChannel)

#### Remarks

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 2D array of 32-bit integer samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each channel. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-readmultisampleportuint16__int.html language=enus -->
## TOPIC 01889: ReadMultiSamplePortUInt16(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-readmultisampleportuint16__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-readmultisampleportuint16__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 16-bit unsigned integer samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic ushort[,] ReadMultiSamplePortUInt16(int samplesPerChannel)RemarksUse this method for devices with up to 16 lines per port.NI-DAQmx read and write methods t

### ReadMultiSamplePortUInt16(int)

Reads one or more 16-bit unsigned integer samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public ushort[,] ReadMultiSamplePortUInt16(int samplesPerChannel)

#### Remarks

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 2D array of 16-bit unsigned integer samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each channel. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-readmultisampleportuint32__int.html language=enus -->
## TOPIC 01890: ReadMultiSamplePortUInt32(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-readmultisampleportuint32__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-readmultisampleportuint32__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 32-bit unsigned integer samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic uint[,] ReadMultiSamplePortUInt32(int samplesPerChannel)RemarksUse this method for devices with up to 32 lines per port.NI-DAQmx read and write methods tim

### ReadMultiSamplePortUInt32(int)

Reads one or more 32-bit unsigned integer samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint[,] ReadMultiSamplePortUInt32(int samplesPerChannel)

#### Remarks

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 2D array of 32-bit unsigned integer samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each channel. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-readsinglesamplemultiline.html language=enus -->
## TOPIC 01891: ReadSingleSampleMultiLine()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-readsinglesamplemultiline.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-readsinglesamplemultiline.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single sample containing Boolean values from one or more DIChannel objects in a task. Each channel can contain multiple digital lines. SyntaxNamespace: NationalInstruments.DAQmxpublic bool[,] ReadSingleSampleMultiLine()RemarksNI-DAQmx read and write methods time out after the amount of time

### ReadSingleSampleMultiLine()

Reads a single sample containing Boolean values from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task. Each channel can contain multiple digital lines.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool[,] ReadSingleSampleMultiLine()

#### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Returns

A 2D array of Boolean samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a line in that channel. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-readsinglesampleportbyte.html language=enus -->
## TOPIC 01892: ReadSingleSamplePortByte()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-readsinglesampleportbyte.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-readsinglesampleportbyte.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single 8-bit unsigned integer sample from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic byte[] ReadSingleSamplePortByte()RemarksUse this method for devices with up to eight lines per port.NI-DAQmx read and write methods time out after the amount of

### ReadSingleSamplePortByte()

Reads a single 8-bit unsigned integer sample from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public byte[] ReadSingleSamplePortByte()

#### Remarks

Use this method for devices with up to eight lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Returns

A 1D array of 8-bit unsigned integer samples from the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-readsinglesampleportint16.html language=enus -->
## TOPIC 01893: ReadSingleSamplePortInt16()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-readsinglesampleportint16.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-readsinglesampleportint16.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single 16-bit integer sample from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic short[] ReadSingleSamplePortInt16()RemarksUse this method for devices with up to 16 lines per port. NI-DAQmx read and write methods time out after the amount of time sp

### ReadSingleSamplePortInt16()

Reads a single 16-bit integer sample from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public short[] ReadSingleSamplePortInt16()

#### Remarks

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Returns

A 1D array of 16-bit integer samples from the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-readsinglesampleportint32.html language=enus -->
## TOPIC 01894: ReadSingleSamplePortInt32()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-readsinglesampleportint32.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-readsinglesampleportint32.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single 32-bit integer sample from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic int[] ReadSingleSamplePortInt32()RemarksUse this method for devices with up to 32 lines per port. NI-DAQmx read and write methods time out after the amount of time spec

### ReadSingleSamplePortInt32()

Reads a single 32-bit integer sample from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int[] ReadSingleSamplePortInt32()

#### Remarks

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Returns

A 1D array of 32-bit integer samples from the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-readsinglesampleportuint16.html language=enus -->
## TOPIC 01895: ReadSingleSamplePortUInt16()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-readsinglesampleportuint16.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-readsinglesampleportuint16.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single 16-bit unsigned integer sample from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic ushort[] ReadSingleSamplePortUInt16()RemarksUse this method for devices with up to 16 lines per port.NI-DAQmx read and write methods time out after the amount

### ReadSingleSamplePortUInt16()

Reads a single 16-bit unsigned integer sample from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public ushort[] ReadSingleSamplePortUInt16()

#### Remarks

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Returns

A 1D array of 16-bit unsigned integer samples from the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-readsinglesampleportuint32.html language=enus -->
## TOPIC 01896: ReadSingleSamplePortUInt32()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-readsinglesampleportuint32.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-readsinglesampleportuint32.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single 32-bit unsigned integer sample from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic uint[] ReadSingleSamplePortUInt32()RemarksUse this method for devices with up to 32 lines per port. NI-DAQmx read and write methods time out after the amount o

### ReadSingleSamplePortUInt32()

Reads a single 32-bit unsigned integer sample from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint[] ReadSingleSamplePortUInt32()

#### Remarks

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Returns

A 1D array of 32-bit unsigned integer samples from the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-readsinglesamplesingleline.html language=enus -->
## TOPIC 01897: ReadSingleSampleSingleLine()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-readsinglesamplesingleline.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-readsinglesamplesingleline.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single Boolean sample from one or more DIChannel objects in a task. Each channel can contain a single digital line. SyntaxNamespace: NationalInstruments.DAQmxpublic bool[] ReadSingleSampleSingleLine()RemarksNI-DAQmx read and write methods time out after the amount of time specified by the Ti

### ReadSingleSampleSingleLine()

Reads a single Boolean sample from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task. Each channel can contain a single digital line.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool[] ReadSingleSampleSingleLine()

#### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Returns

A 1D array of Boolean samples from the task. Each element of the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-readwaveform__int.html language=enus -->
## TOPIC 01898: ReadWaveform(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-readwaveform__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-readwaveform__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more digital waveform samples from one or more DIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalWaveform[] ReadWaveform(int samplesPerChannel)RemarksThe data returned from digital waveform reads is affected by the WaveformAttributeMode property of the

### ReadWaveform(int)

Reads one or more digital waveform samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public DigitalWaveform[] ReadWaveform(int samplesPerChannel)

#### Remarks

The data returned from digital waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) you are reading from.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 1D array of DigitalWaveform objects containing samples from the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-readwaveform__timespan.html language=enus -->
## TOPIC 01899: ReadWaveform(TimeSpan)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-readwaveform__timespan.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-readwaveform__timespan.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more digital waveform samples from one or more DIChannel objects in a task for a specified duration . SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalWaveform[] ReadWaveform(TimeSpan duration)RemarksNI-DAQmx scales the read data to the units of the measurement, including any cus

### ReadWaveform(TimeSpan)

Reads one or more digital waveform samples from one or more [DIChannel](nationalinstruments-daqmx-dichannel.html) objects in a task for a specified *duration* .

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public DigitalWaveform[] ReadWaveform(TimeSpan duration)

#### Remarks

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units when creating channels using the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) being read.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the [Stream](nationalinstruments-daqmx-task-stream.html) object used for the reads or writes.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| duration | TimeSpan | The duration of time to read the waveform. The duration specified must be long enough to read at least one sample at the configured SampleClockRate. |

#### Returns

A 1D array of DigitalWaveform objects containing samples from the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If the duration provided was less than Zero. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-synchronizecallbacks.html language=enus -->
## TOPIC 01900: SynchronizeCallbacks

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-synchronizecallbacks.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-synchronizecallbacks.html
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

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-synchronizingobject.html language=enus -->
## TOPIC 01901: SynchronizingObject

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-synchronizingobject.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-synchronizingobject.html
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

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader-tostring.html language=enus -->
## TOPIC 01902: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader-tostring.html
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

DigitalMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelreader.html language=enus -->
## TOPIC 01903: DigitalMultiChannelReader Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelreader.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelreader.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains methods for reading samples from one or more digital input or output channels in a task. Derives fromMarshalByRefObjectISynchronizeCallbacksISupportSynchronizationContextSyntaxNamespace: NationalInstruments.DAQmxpublic class DigitalMultiChannelReader : MarshalByRefObject, ISynchronizeCallba

### DigitalMultiChannelReader Class

Contains methods for reading samples from one or more digital input or output channels in a task.

#### Derives from

- MarshalByRefObject
- ISynchronizeCallbacks
- ISupportSynchronizationContext

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class DigitalMultiChannelReader : MarshalByRefObject, ISynchronizeCallbacks, ISupportSynchronizationContext

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| DigitalMultiChannelReader(DaqStream) | Creates a new instance of the DigitalMultiChannelReader class to read from the specified DaqStream. |

#### Properties

| Name | Description |
| --- | --- |
| SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |
| SynchronizingObject | Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will warn if usedGets or sets the object that marshals event-handler and callback calls. |

#### Methods

| Name | Description |
| --- | --- |
| BeginMemoryOptimizedReadMultiSamplePortByte(int, AsyncCallback, object, byte, ReallocationPolicy) | Begins an asynchronous read of one or more 8-bit unsigned integer samples from one or more DIChannel objects in a task. |
| BeginMemoryOptimizedReadMultiSamplePortByte(int, AsyncCallback, object, byte) | Begins an asynchronous read of one or more 8-bit unsigned integer samples from one or more DIChannel objects in a task. |
| BeginMemoryOptimizedReadMultiSamplePortInt32(int, AsyncCallback, object, int) | Begins an asynchronous read of one or more 32-bit integer samples from one or more DIChannel objects in a task. |
| BeginMemoryOptimizedReadMultiSamplePortInt32(int, AsyncCallback, object, int, ReallocationPolicy) | Begins an asynchronous read of one or more 32-bit integer samples from one or more DIChannel objects in a task. |
| BeginMemoryOptimizedReadMultiSamplePortUInt16(int, AsyncCallback, object, ushort, ReallocationPolicy) | Begins an asynchronous read of one or more 16-bit unsigned integer samples from one or more DIChannel objects in a task. |
| BeginMemoryOptimizedReadMultiSamplePortUInt16(int, AsyncCallback, object, ushort) | Begins an asynchronous read of one or more 16-bit unsigned integer samples from one or more DIChannel objects in a task. |
| BeginMemoryOptimizedReadMultiSamplePortUInt32(int, AsyncCallback, object, uint) | Begins an asynchronous read of one or more 32-bit unsigned integer samples from one or more DIChannel objects in a task. |
| BeginMemoryOptimizedReadMultiSamplePortUInt32(int, AsyncCallback, object, uint, ReallocationPolicy) | Begins an asynchronous read of one or more 32-bit unsigned integer samples from one or more DIChannel objects in a task. |
| BeginMemoryOptimizedReadSingleSampleMultiLine(AsyncCallback, object, bool) | Begins an asynchronous read of a single sample containing Boolean values from one or more DIChannel objects in a task. Each channel can contain multiple digital lines. |
| BeginReadMultiSamplePortByte(int, AsyncCallback, object) | Begins an asynchronous read of one or more 8-bit unsigned integer samples from one or more DIChannel objects in a task. |
| BeginReadMultiSamplePortInt16(int, AsyncCallback, object) | Begins an asynchronous read of one or more 16-bit integer samples from one or more DIChannel objects in a task. |
| BeginReadMultiSamplePortInt32(int, AsyncCallback, object) | Begins an asynchronous read of one or more 32-bit integer samples from one or more DIChannel objects in a task. |
| BeginReadMultiSamplePortUInt16(int, AsyncCallback, object) | Begins an asynchronous read of one or more 16-bit unsigned integer samples from one or more DIChannel objects in a task. |
| BeginReadMultiSamplePortUInt32(int, AsyncCallback, object) | Begins an asynchronous read of one or more 32-bit unsigned integer samples from one or more DIChannel objects in a task. |
| BeginReadSingleSampleMultiLine(AsyncCallback, object) | Begins an asynchronous read of a single sample containing Boolean values from one or more DIChannel objects in a task. Each channel can contain multiple digital lines. |
| BeginReadSingleSamplePortByte(AsyncCallback, object) | Begins an asynchronous read of a single 8-bit unsigned integer sample from one or more DIChannel objects in a task. |
| BeginReadSingleSamplePortInt16(AsyncCallback, object) | Begins an asynchronous read of a single 16-bit integer sample from one or more DIChannel objects in a task. |
| BeginReadSingleSamplePortInt32(AsyncCallback, object) | Begins an asynchronous read of a single 32-bit integer sample from one or more DIChannel objects in a task. |
| BeginReadSingleSamplePortUInt16(AsyncCallback, object) | Begins an asynchronous read of a single 16-bit unsigned integer sample from one or more DIChannel objects in a task. |
| BeginReadSingleSamplePortUInt32(AsyncCallback, object) | Begins an asynchronous read of a single 32-bit unsigned integer sample from one or more DIChannel objects in a task. |
| BeginReadSingleSampleSingleLine(AsyncCallback, object) | Begins an asynchronous read of a single Boolean sample from one or more DIChannel objects in a task. Each channel can contain a single digital line. |
| BeginReadWaveform(int, AsyncCallback, object) | Begins an asynchronous read of one or more digital waveform samples from one or more DIChannel objects in a task. |
| BeginReadWaveform(TimeSpan, AsyncCallback, object) | Begins an asynchronous read of one or more digital waveform samples from one or more DIChannel objects in a task for a specified duration . |
| EndMemoryOptimizedReadMultiSamplePortByte(IAsyncResult, out int) | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePortByte(int, AsyncCallback, object, byte[, ]) and retrieves the read samples. |
| EndMemoryOptimizedReadMultiSamplePortInt32(IAsyncResult, out int) | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePortInt32(int, AsyncCallback, object, int[, ]) and retrieves the read samples. |
| EndMemoryOptimizedReadMultiSamplePortUInt16(IAsyncResult, out int) | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePortUInt16(int, AsyncCallback, object, ushort[, ]) and retrieves the read samples. |
| EndMemoryOptimizedReadMultiSamplePortUInt32(IAsyncResult, out int) | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePortUInt32(int, AsyncCallback, object, uint[, ]) and retrieves the read samples. |
| EndMemoryOptimizedReadSingleSampleMultiLine(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadSingleSampleMultiLine(AsyncCallback, object, bool[, ]) and retrieves the read samples. |
| EndReadMultiSamplePortByte(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortByte(int, AsyncCallback, object) and retrieves the read samples. |
| EndReadMultiSamplePortInt16(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortInt16(int, AsyncCallback, object) and retrieves the read samples. |
| EndReadMultiSamplePortInt32(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortInt32(int, AsyncCallback, object) and retrieves the read samples. |
| EndReadMultiSamplePortUInt16(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortUInt16(int, AsyncCallback, object) and retrieves the read samples. |
| EndReadMultiSamplePortUInt32(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortUInt32(int, AsyncCallback, object) and retrieves the read samples. |
| EndReadSingleSampleMultiLine(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadSingleSampleMultiLine(AsyncCallback, object) and retrieves the read samples. |
| EndReadSingleSamplePortByte(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortByte(AsyncCallback, object) and retrieves the read samples. |
| EndReadSingleSamplePortInt16(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortInt16(AsyncCallback, object) and retrieves the read samples. |
| EndReadSingleSamplePortInt32(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortInt32(AsyncCallback, object) and retrieves the read samples. |
| EndReadSingleSamplePortUInt16(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortUInt16(AsyncCallback, object) and retrieves the read samples. |
| EndReadSingleSamplePortUInt32(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortUInt32(AsyncCallback, object) and retrieves the read samples. |
| EndReadSingleSampleSingleLine(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadSingleSampleSingleLine(AsyncCallback, object) and retrieves the read samples. |
| EndReadWaveform(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadWaveform(int, AsyncCallback, object) and retrieves the read samples. |
| MemoryOptimizedReadMultiSamplePortByte(int, ref byte, out int) | Reads one or more 8-bit unsigned integer samples from one or more DIChannel objects in a task. |
| MemoryOptimizedReadMultiSamplePortByte(int, ref byte, ReallocationPolicy, out int) | Reads one or more 8-bit unsigned integer samples from one or more DIChannel objects in a task. |
| MemoryOptimizedReadMultiSamplePortInt32(int, ref int, out int) | Reads one or more 32-bit integer samples from one or more DIChannel objects in a task. |
| MemoryOptimizedReadMultiSamplePortInt32(int, ref int, ReallocationPolicy, out int) | Reads one or more 32-bit integer samples from one or more DIChannel objects in a task. |
| MemoryOptimizedReadMultiSamplePortUInt16(int, ref ushort, ReallocationPolicy, out int) | Reads one or more 16-bit unsigned integer samples from one or more DIChannel objects in a task. |
| MemoryOptimizedReadMultiSamplePortUInt16(int, ref ushort, out int) | Reads one or more 16-bit unsigned integer samples from one or more DIChannel objects in a task. |
| MemoryOptimizedReadMultiSamplePortUInt32(int, ref uint, ReallocationPolicy, out int) | Reads one or more 32-bit unsigned integer samples from one or more DIChannel objects in a task. |
| MemoryOptimizedReadMultiSamplePortUInt32(int, ref uint, out int) | Reads one or more 32-bit unsigned integer samples from one or more DIChannel objects in a task. |
| MemoryOptimizedReadSingleSampleMultiLine(bool) | Reads a single sample containing Boolean values from one or more DIChannel objects in a task. Each channel can contain multiple digital lines. |
| ReadMultiSamplePortByte(int) | Reads one or more 8-bit unsigned integer samples from one or more DIChannel objects in a task. |
| ReadMultiSamplePortInt16(int) | Reads one or more 16-bit integer samples from one or more DIChannel objects in a task. |
| ReadMultiSamplePortInt32(int) | Reads one or more 32-bit integer samples from one or more DIChannel objects in a task. |
| ReadMultiSamplePortUInt16(int) | Reads one or more 16-bit unsigned integer samples from one or more DIChannel objects in a task. |
| ReadMultiSamplePortUInt32(int) | Reads one or more 32-bit unsigned integer samples from one or more DIChannel objects in a task. |
| ReadSingleSampleMultiLine() | Reads a single sample containing Boolean values from one or more DIChannel objects in a task. Each channel can contain multiple digital lines. |
| ReadSingleSamplePortByte() | Reads a single 8-bit unsigned integer sample from one or more DIChannel objects in a task. |
| ReadSingleSamplePortInt16() | Reads a single 16-bit integer sample from one or more DIChannel objects in a task. |
| ReadSingleSamplePortInt32() | Reads a single 32-bit integer sample from one or more DIChannel objects in a task. |
| ReadSingleSamplePortUInt16() | Reads a single 16-bit unsigned integer sample from one or more DIChannel objects in a task. |
| ReadSingleSamplePortUInt32() | Reads a single 32-bit unsigned integer sample from one or more DIChannel objects in a task. |
| ReadSingleSampleSingleLine() | Reads a single Boolean sample from one or more DIChannel objects in a task. Each channel can contain a single digital line. |
| ReadWaveform(int) | Reads one or more digital waveform samples from one or more DIChannel objects in a task. |
| ReadWaveform(TimeSpan) | Reads one or more digital waveform samples from one or more DIChannel objects in a task for a specified duration . |
| ToString() | Returns a string representation of the object. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-beginwritemultisampleport__bool-byte_arr2-asynccallback-object.html language=enus -->
## TOPIC 01904: BeginWriteMultiSamplePort(bool, byte, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-beginwritemultisampleport__bool-byte_arr2-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-beginwritemultisampleport__bool-byte_arr2-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of one or more 8-bit unsigned integer samples to one or more DOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, byte[,] data, AsyncCallback callback, object st

### BeginWriteMultiSamplePort(bool, byte, AsyncCallback, object)

Begins an asynchronous write of one or more 8-bit unsigned integer samples to one or more [DOChannel](nationalinstruments-daqmx-dochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, byte[,] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Use this method for devices with up to 8 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | byte | A 2D array of 8-bit integer samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-beginwritemultisampleport__bool-int_arr2-asynccallback-object.html language=enus -->
## TOPIC 01905: BeginWriteMultiSamplePort(bool, int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-beginwritemultisampleport__bool-int_arr2-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-beginwritemultisampleport__bool-int_arr2-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of one or more 32-bit integer samples to one or more DOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, int[,] data, AsyncCallback callback, object state)Remar

### BeginWriteMultiSamplePort(bool, int, AsyncCallback, object)

Begins an asynchronous write of one or more 32-bit integer samples to one or more [DOChannel](nationalinstruments-daqmx-dochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, int[,] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | int | A 2D array of 32-bit integer samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-beginwritemultisampleport__bool-short_arr2-asynccallback-object.html language=enus -->
## TOPIC 01906: BeginWriteMultiSamplePort(bool, short, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-beginwritemultisampleport__bool-short_arr2-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-beginwritemultisampleport__bool-short_arr2-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of one or more 16-bit integer samples to one or more DOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, short[,] data, AsyncCallback callback, object state)Rem

### BeginWriteMultiSamplePort(bool, short, AsyncCallback, object)

Begins an asynchronous write of one or more 16-bit integer samples to one or more [DOChannel](nationalinstruments-daqmx-dochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, short[,] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | short | A 2D array of 16-bit integer samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-beginwritemultisampleport__bool-uint_arr2-asynccallback-object.html language=enus -->
## TOPIC 01907: BeginWriteMultiSamplePort(bool, uint, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-beginwritemultisampleport__bool-uint_arr2-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-beginwritemultisampleport__bool-uint_arr2-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of one or more 32-bit unsigned integer samples to one or more DOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, uint[,] data, AsyncCallback callback, object s

### BeginWriteMultiSamplePort(bool, uint, AsyncCallback, object)

Begins an asynchronous write of one or more 32-bit unsigned integer samples to one or more [DOChannel](nationalinstruments-daqmx-dochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, uint[,] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | uint | A 2D array of 32-bit unsigned integer samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-beginwritemultisampleport__bool-ushort_arr2-asynccallback-object.html language=enus -->
## TOPIC 01908: BeginWriteMultiSamplePort(bool, ushort, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-beginwritemultisampleport__bool-ushort_arr2-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-beginwritemultisampleport__bool-ushort_arr2-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of one or more 16-bit unsigned integer samples to one or more DOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, ushort[,] data, AsyncCallback callback, object

### BeginWriteMultiSamplePort(bool, ushort, AsyncCallback, object)

Begins an asynchronous write of one or more 16-bit unsigned integer samples to one or more [DOChannel](nationalinstruments-daqmx-dochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, ushort[,] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | ushort | A 2D array of 16-bit unsigned integer samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-beginwritesinglesamplemultiline__bool-bool_arr2-asynccallback-object.html language=enus -->
## TOPIC 01909: BeginWriteSingleSampleMultiLine(bool, bool, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-beginwritesinglesamplemultiline__bool-bool_arr2-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-beginwritesinglesamplemultiline__bool-bool_arr2-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of a Boolean sample to one or more DOChannel objects in a task. The channels can contain one or more digital lines. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteSingleSampleMultiLine([MarshalAs(UnmanagedType.U1)] bool autoStart, bool[,] data, A

### BeginWriteSingleSampleMultiLine(bool, bool, AsyncCallback, object)

Begins an asynchronous write of a Boolean sample to one or more [DOChannel](nationalinstruments-daqmx-dochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx). The channels can contain one or more digital lines.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteSingleSampleMultiLine([MarshalAs(UnmanagedType.U1)] bool autoStart, bool[,] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | bool | A 2D array of Boolean samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a line in that channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-beginwritesinglesampleport__bool-byte_arr1-asynccallback-object.html language=enus -->
## TOPIC 01910: BeginWriteSingleSamplePort(bool, byte[], AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-beginwritesinglesampleport__bool-byte_arr1-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-beginwritesinglesampleport__bool-byte_arr1-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of a single 8-bit unsigned integer sample to one or more DOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, byte[] data, AsyncCallback callback, object state)

### BeginWriteSingleSamplePort(bool, byte[], AsyncCallback, object)

Begins an asynchronous write of a single 8-bit unsigned integer sample to one or more [DOChannel](nationalinstruments-daqmx-dochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, byte[] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Use this method for devices with up to eight lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | byte[] | A 1D array of 8-bit unsigned integer samples to write to the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-beginwritesinglesampleport__bool-int_arr1-asynccallback-object.html language=enus -->
## TOPIC 01911: BeginWriteSingleSamplePort(bool, int[], AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-beginwritesinglesampleport__bool-int_arr1-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-beginwritesinglesampleport__bool-int_arr1-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of a single 32-bit integer sample to one or more DOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, int[] data, AsyncCallback callback, object state)RemarksPa

### BeginWriteSingleSamplePort(bool, int[], AsyncCallback, object)

Begins an asynchronous write of a single 32-bit integer sample to one or more [DOChannel](nationalinstruments-daqmx-dochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, int[] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | int[] | A 2D array of 32-bit integer samples to write to the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-beginwritesinglesampleport__bool-short_arr1-asynccallback-object.html language=enus -->
## TOPIC 01912: BeginWriteSingleSamplePort(bool, short[], AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-beginwritesinglesampleport__bool-short_arr1-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-beginwritesinglesampleport__bool-short_arr1-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of one or more 16-bit integer samples to one or more DOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, short[] data, AsyncCallback callback, object state)Rem

### BeginWriteSingleSamplePort(bool, short[], AsyncCallback, object)

Begins an asynchronous write of one or more 16-bit integer samples to one or more [DOChannel](nationalinstruments-daqmx-dochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, short[] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | short[] | A 2D array of 16-bit integer samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-beginwritesinglesampleport__bool-uint_arr1-asynccallback-object.html language=enus -->
## TOPIC 01913: BeginWriteSingleSamplePort(bool, uint[], AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-beginwritesinglesampleport__bool-uint_arr1-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-beginwritesinglesampleport__bool-uint_arr1-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of a single 32-bit unsigned integer sample to one or more DOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, uint[] data, AsyncCallback callback, object state

### BeginWriteSingleSamplePort(bool, uint[], AsyncCallback, object)

Begins an asynchronous write of a single 32-bit unsigned integer sample to one or more [DOChannel](nationalinstruments-daqmx-dochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, uint[] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | uint[] | A 2D array of 32-bit unsigned integer samples to write to the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-beginwritesinglesampleport__bool-ushort_arr1-asynccallback-object.html language=enus -->
## TOPIC 01914: BeginWriteSingleSamplePort(bool, ushort[], AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-beginwritesinglesampleport__bool-ushort_arr1-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-beginwritesinglesampleport__bool-ushort_arr1-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of a single 16-bit unsigned integer sample to one or more DOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, ushort[] data, AsyncCallback callback, object sta

### BeginWriteSingleSamplePort(bool, ushort[], AsyncCallback, object)

Begins an asynchronous write of a single 16-bit unsigned integer sample to one or more [DOChannel](nationalinstruments-daqmx-dochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, ushort[] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | ushort[] | A 2D array of 16-bit unsigned integer samples to write to the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-beginwritesinglesamplesingleline__bool-bool_arr1-asynccallback-object.html language=enus -->
## TOPIC 01915: BeginWriteSingleSampleSingleLine(bool, bool[], AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-beginwritesinglesamplesingleline__bool-bool_arr1-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-beginwritesinglesamplesingleline__bool-bool_arr1-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of a single Boolean sample to one or more DOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteSingleSampleSingleLine([MarshalAs(UnmanagedType.U1)] bool autoStart, bool[] data, AsyncCallback callback, object state)RemarksPa

### BeginWriteSingleSampleSingleLine(bool, bool[], AsyncCallback, object)

Begins an asynchronous write of a single Boolean sample to one or more [DOChannel](nationalinstruments-daqmx-dochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteSingleSampleSingleLine([MarshalAs(UnmanagedType.U1)] bool autoStart, bool[] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

This method fails if the channels in the task contain more than one digital line.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | bool[] | A 1D array of Boolean samples to write to the task. Each element of the array corresponds to a channel within the task. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-beginwritewaveform__bool-digitalwaveform_arr1-asynccallback-object.html language=enus -->
## TOPIC 01916: BeginWriteWaveform(bool, DigitalWaveform[], AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-beginwritewaveform__bool-digitalwaveform_arr1-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-beginwritewaveform__bool-digitalwaveform_arr1-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of one or more digital waveform samples to one or more DOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteWaveform([MarshalAs(UnmanagedType.U1)] bool autoStart, DigitalWaveform[] data, AsyncCallback callback, object state

### BeginWriteWaveform(bool, DigitalWaveform[], AsyncCallback, object)

Begins an asynchronous write of one or more digital waveform samples to one or more [DOChannel](nationalinstruments-daqmx-dochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteWaveform([MarshalAs(UnmanagedType.U1)] bool autoStart, DigitalWaveform[] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-digitalmultichannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

Digital waveform writes are not affected by the WaveformTiming.SampleInterval or WaveformTiming.StartTime properties on the DigitalWaveform. To configure timing for digital waveform writes, use the Overload:NationalInstruments.DAQmx.Timing.ConfigureSampleClock method.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | DigitalWaveform[] | A 1D array of DigitalWaveform objects to write to the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task. The order of the lines in the digital waveform corresponds to the order in which you add the lines to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-digitalmultichannelwriter__daqstream.html language=enus -->
## TOPIC 01917: DigitalMultiChannelWriter(DaqStream)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-digitalmultichannelwriter__daqstream.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-digitalmultichannelwriter__daqstream.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of the DigitalMultiChannelWriter class to write to the specified DaqStream. SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalMultiChannelWriter(DaqStream stream)RemarksEach Task object contains a Stream property that serves as the connection point for writers to provide

### DigitalMultiChannelWriter(DaqStream)

Creates a new instance of the [DigitalMultiChannelWriter](nationalinstruments-daqmx-digitalmultichannelwriter.html) class to write to the specified [DaqStream](nationalinstruments-daqmx-daqstream.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public DigitalMultiChannelWriter(DaqStream stream)

#### Remarks

Each [Task](nationalinstruments-daqmx-task.html) object contains a [Stream](nationalinstruments-daqmx-task-stream.html) property that serves as the connection point for writers to provide samples to be generated by that task.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| stream | DaqStream | The DaqStream to write to. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-endwrite__iasyncresult.html language=enus -->
## TOPIC 01918: EndWrite(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-endwrite__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-endwrite__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous write initiated with BeginWriteMultiSamplePort(bool, uint[, ], AsyncCallback, object), BeginWriteSingleSamplePort(bool, uint[], AsyncCallback, object), BeginWriteSingleSampleMultiLine(bool, bool[, ], AsyncCallback, object), BeginWriteSingleSampleSingleLine(bool, bo

### EndWrite(IAsyncResult)

Handles the end of an asynchronous write initiated with [BeginWriteMultiSamplePort(bool, uint[, ], AsyncCallback, object)](nationalinstruments-daqmx-digitalmultichannelwriter-beginwritemultisampleport__bool-uint_arr2-asynccallback-object.html), [BeginWriteSingleSamplePort(bool, uint[], AsyncCallback, object)](nationalinstruments-daqmx-digitalmultichannelwriter-beginwritesinglesampleport__bool-uint_arr1-asynccallback-object.html), [BeginWriteSingleSampleMultiLine(bool, bool[, ], AsyncCallback, object)](nationalinstruments-daqmx-digitalmultichannelwriter-beginwritesinglesamplemultiline__bool-bool_arr2-asynccallback-object.html), [BeginWriteSingleSampleSingleLine(bool, bool[], AsyncCallback, object)](nationalinstruments-daqmx-digitalmultichannelwriter-beginwritesinglesamplesingleline__bool-bool_arr1-asynccallback-object.html), or [BeginWriteWaveform(bool, DigitalWaveform[], AsyncCallback, object)](nationalinstruments-daqmx-digitalmultichannelwriter-beginwritewaveform__bool-digitalwaveform_arr1-asynccallback-object.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void EndWrite(IAsyncResult asyncResult)

#### Remarks

If you call EndWrite(IAsyncResult) before the asynchronous write represented by the provided IAsyncResult is complete, EndWrite(IAsyncResult) waits for the write to complete before returning. For a write to a buffered task, the write is considered complete when all of the written samples have been transferred to the task buffer. Use [IsDone](nationalinstruments-daqmx-task-isdone.html) or [WaitUntilDone(int)](nationalinstruments-daqmx-task-waituntildone__int.html) on the [Task](nationalinstruments-daqmx-task.html) object to determine if a task has generated all of the data it was configured to generate.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginWriteMultiSamplePort(bool, uint[, ], AsyncCallback, object), BeginWriteSingleSamplePort(bool, uint[], AsyncCallback, object), BeginWriteSingleSampleMultiLine(bool, bool[, ], AsyncCallback, object), BeginWriteSingleSampleSingleLine(bool, bool[], AsyncCallback, object), or BeginWriteWaveform(bool, DigitalWaveform[], AsyncCallback, object). |

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginWriteMultiSamplePort(bool, uint[, ], AsyncCallback, object), BeginWriteSingleSamplePort(bool, uint[], AsyncCallback, object), BeginWriteSingleSampleMultiLine(bool, bool[, ], AsyncCallback, object), BeginWriteSingleSampleSingleLine(bool, bool[], AsyncCallback, object), or BeginWriteWaveform(bool, DigitalWaveform[], AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| IndexOutOfRangeException | The data passed to BeginWriteMultiSamplePort(bool, uint[, ], AsyncCallback, object), BeginWriteSingleSamplePort(bool, uint[], AsyncCallback, object), BeginWriteSingleSampleMultiLine(bool, bool[, ], AsyncCallback, object), BeginWriteSingleSampleSingleLine(bool, bool[], AsyncCallback, object), or BeginWriteWaveform(bool, DigitalWaveform[], AsyncCallback, object) has a non-zero lower bound. |

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-synchronizecallbacks.html language=enus -->
## TOPIC 01919: SynchronizeCallbacks

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-synchronizecallbacks.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-synchronizecallbacks.html
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

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-synchronizingobject.html language=enus -->
## TOPIC 01920: SynchronizingObject

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-synchronizingobject.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-synchronizingobject.html
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

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-tostring.html language=enus -->
## TOPIC 01921: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-tostring.html
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

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-writemultisampleport__bool-byte_arr2.html language=enus -->
## TOPIC 01922: WriteMultiSamplePort(bool, byte)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-writemultisampleport__bool-byte_arr2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-writemultisampleport__bool-byte_arr2.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more 8-bit unsigned integer samples to one or more DOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, byte[,] data)RemarksUse this method for devices with up to eight lines per port. If t

### WriteMultiSamplePort(bool, byte)

Writes one or more 8-bit unsigned integer samples to one or more [DOChannel](nationalinstruments-daqmx-dochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, byte[,] data)

#### Remarks

Use this method for devices with up to eight lines per port. If the task uses on-demand timing, this method returns only after the device generates all samples. If the task uses any timing type other than on-demand, this method returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) method to block until the device has generated all samples.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | byte | A 2D array of 8-bit unsigned integer samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-writemultisampleport__bool-int_arr2.html language=enus -->
## TOPIC 01923: WriteMultiSamplePort(bool, int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-writemultisampleport__bool-int_arr2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-writemultisampleport__bool-int_arr2.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more 32-bit integer samples to one or more DOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, int[,] data)RemarksUse this method for devices with up to 32 lines per port. If the task uses

### WriteMultiSamplePort(bool, int)

Writes one or more 32-bit integer samples to one or more [DOChannel](nationalinstruments-daqmx-dochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, int[,] data)

#### Remarks

Use this method for devices with up to 32 lines per port. If the task uses on-demand timing, this method returns only after the device generates all samples. If the task uses any timing type other than on-demand, this method returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) method to block until the device has generated all samples.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | int | A 2D array of 32-bit unsigned integer samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-writemultisampleport__bool-short_arr2.html language=enus -->
## TOPIC 01924: WriteMultiSamplePort(bool, short)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-writemultisampleport__bool-short_arr2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-writemultisampleport__bool-short_arr2.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more 16-bit integer samples to one or more DOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, short[,] data)RemarksUse this format for devices with up to 16 lines per port. If the task us

### WriteMultiSamplePort(bool, short)

Writes one or more 16-bit integer samples to one or more [DOChannel](nationalinstruments-daqmx-dochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, short[,] data)

#### Remarks

Use this format for devices with up to 16 lines per port. If the task uses on-demand timing, this method returns only after the device generates all samples. If the task uses any timing type other than on-demand, this method returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) method to block until the device has generated all samples.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | short | A 2D array of 16-bit unsigned integer samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-writemultisampleport__bool-uint_arr2.html language=enus -->
## TOPIC 01925: WriteMultiSamplePort(bool, uint)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-writemultisampleport__bool-uint_arr2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-writemultisampleport__bool-uint_arr2.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more 32-bit unsigned integer samples to one or more DOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, uint[,] data)RemarksUse this method for devices with up to 32 lines per port. If the

### WriteMultiSamplePort(bool, uint)

Writes one or more 32-bit unsigned integer samples to one or more [DOChannel](nationalinstruments-daqmx-dochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, uint[,] data)

#### Remarks

Use this method for devices with up to 32 lines per port. If the task uses on-demand timing, this method returns only after the device generates all samples. If the task uses any timing type other than on-demand, this method returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) method to block until the device has generated all samples.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | uint | A 2D array of 32-bit unsigned integer samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-writemultisampleport__bool-ushort_arr2.html language=enus -->
## TOPIC 01926: WriteMultiSamplePort(bool, ushort)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-writemultisampleport__bool-ushort_arr2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-writemultisampleport__bool-ushort_arr2.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more 16-bit unsigned integer samples to one or more DOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, ushort[,] data)RemarksUse this method for devices with up to 16 lines per port. If t

### WriteMultiSamplePort(bool, ushort)

Writes one or more 16-bit unsigned integer samples to one or more [DOChannel](nationalinstruments-daqmx-dochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteMultiSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, ushort[,] data)

#### Remarks

Use this method for devices with up to 16 lines per port. If the task uses on-demand timing, this method returns only after the device generates all samples. If the task uses any timing type other than on-demand, this method returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) method to block until the device has generated all samples.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | ushort | A 2D array of 16-bit unsigned integer samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-writesinglesamplemultiline__bool-bool_arr2.html language=enus -->
## TOPIC 01927: WriteSingleSampleMultiLine(bool, bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-writesinglesamplemultiline__bool-bool_arr2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-writesinglesamplemultiline__bool-bool_arr2.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a Boolean sample to one or more DOChannel objects in a task. The channels can contain one or more digital lines. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteSingleSampleMultiLine([MarshalAs(UnmanagedType.U1)] bool autoStart, bool[,] data)RemarksNI-DAQmx read and write methods t

### WriteSingleSampleMultiLine(bool, bool)

Writes a Boolean sample to one or more [DOChannel](nationalinstruments-daqmx-dochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx). The channels can contain one or more digital lines.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteSingleSampleMultiLine([MarshalAs(UnmanagedType.U1)] bool autoStart, bool[,] data)

#### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | bool | A 2D array of Boolean samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a line in that channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-writesinglesampleport__bool-byte_arr1.html language=enus -->
## TOPIC 01928: WriteSingleSamplePort(bool, byte[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-writesinglesampleport__bool-byte_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-writesinglesampleport__bool-byte_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single 8-bit unsigned integer sample to one or more DOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, byte[] data)RemarksUse this method for devices with up to eight lines per port. NI-DAQmx

### WriteSingleSamplePort(bool, byte[])

Writes a single 8-bit unsigned integer sample to one or more [DOChannel](nationalinstruments-daqmx-dochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, byte[] data)

#### Remarks

Use this method for devices with up to eight lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | byte[] | A 1D array of 8-bit unsigned integer samples to write to the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-writesinglesampleport__bool-int_arr1.html language=enus -->
## TOPIC 01929: WriteSingleSamplePort(bool, int[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-writesinglesampleport__bool-int_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-writesinglesampleport__bool-int_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single 32-bit integer sample to one or more DOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, int[] data)RemarksUse this method for devices with up to 32 lines per port. NI-DAQmx read and wr

### WriteSingleSamplePort(bool, int[])

Writes a single 32-bit integer sample to one or more [DOChannel](nationalinstruments-daqmx-dochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, int[] data)

#### Remarks

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | int[] | A 2D array of 32-bit integer samples to write to the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-writesinglesampleport__bool-short_arr1.html language=enus -->
## TOPIC 01930: WriteSingleSamplePort(bool, short[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-writesinglesampleport__bool-short_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-writesinglesampleport__bool-short_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more 16-bit integer samples to one or more DOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, short[] data)RemarksUse this method for devices with up to 16 lines per port. If the task us

### WriteSingleSamplePort(bool, short[])

Writes one or more 16-bit integer samples to one or more [DOChannel](nationalinstruments-daqmx-dochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, short[] data)

#### Remarks

Use this method for devices with up to 16 lines per port. If the task uses on-demand timing, this method returns only after the device generates all samples. If the task uses any timing type other than on-demand, this method returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) method to block until the device has generated all samples.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | short[] | A 2D array of 16-bit integer samples to write to the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample to write to each channel. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-writesinglesampleport__bool-uint_arr1.html language=enus -->
## TOPIC 01931: WriteSingleSamplePort(bool, uint[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-writesinglesampleport__bool-uint_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-writesinglesampleport__bool-uint_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single 32-bit unsigned integer sample to one or more DOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, uint[] data)RemarksUse this method for devices with up to 32 lines per port. NI-DAQmx r

### WriteSingleSamplePort(bool, uint[])

Writes a single 32-bit unsigned integer sample to one or more [DOChannel](nationalinstruments-daqmx-dochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, uint[] data)

#### Remarks

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | uint[] | A 2D array of 32-bit unsigned integer samples to write to the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-writesinglesampleport__bool-ushort_arr1.html language=enus -->
## TOPIC 01932: WriteSingleSamplePort(bool, ushort[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-writesinglesampleport__bool-ushort_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-writesinglesampleport__bool-ushort_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single 16-bit unsigned integer sample to one or more DOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, ushort[] data)RemarksUse this method for devices with up to 16 lines per port. NI-DAQmx

### WriteSingleSamplePort(bool, ushort[])

Writes a single 16-bit unsigned integer sample to one or more [DOChannel](nationalinstruments-daqmx-dochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteSingleSamplePort([MarshalAs(UnmanagedType.U1)] bool autoStart, ushort[] data)

#### Remarks

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | ushort[] | A 2D array of 16-bit unsigned integer samples to write to the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-writesinglesamplesingleline__bool-bool_arr1.html language=enus -->
## TOPIC 01933: WriteSingleSampleSingleLine(bool, bool[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-writesinglesamplesingleline__bool-bool_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-writesinglesamplesingleline__bool-bool_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single Boolean sample to one or more DOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteSingleSampleSingleLine([MarshalAs(UnmanagedType.U1)] bool autoStart, bool[] data)RemarksThis method fails if the channels in the task contain more than one digital li

### WriteSingleSampleSingleLine(bool, bool[])

Writes a single Boolean sample to one or more [DOChannel](nationalinstruments-daqmx-dochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteSingleSampleSingleLine([MarshalAs(UnmanagedType.U1)] bool autoStart, bool[] data)

#### Remarks

This method fails if the channels in the task contain more than one digital line.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | bool[] | A 1D array of Boolean samples to write to the task. Each element of the array corresponds to a channel within the task. The order of the channels in the array correspond to the order in which you add the channels to the task. The order of the lines in the array corresponds to the order in which you add the lines to the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter-writewaveform__bool-digitalwaveform_arr1.html language=enus -->
## TOPIC 01934: WriteWaveform(bool, DigitalWaveform[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter-writewaveform__bool-digitalwaveform_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter-writewaveform__bool-digitalwaveform_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more digital waveform samples to one or more DOChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteWaveform([MarshalAs(UnmanagedType.U1)] bool autoStart, DigitalWaveform[] data)RemarksIf the task uses on-demand timing, this method returns only after th

### WriteWaveform(bool, DigitalWaveform[])

Writes one or more digital waveform samples to one or more [DOChannel](nationalinstruments-daqmx-dochannel.html) objects in a [task](/csh?context=nidaqmx_mxcncpts_tasksnidaqmx).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteWaveform([MarshalAs(UnmanagedType.U1)] bool autoStart, DigitalWaveform[] data)

#### Remarks

If the task uses on-demand timing, this method returns only after the device generates all samples. If the task uses any timing type other than on-demand, this method returns immediately and does not wait for the device to generate all samples. Your application must call the [WaitUntilDone](nationalinstruments-daqmx-task-waituntildone__int.html) method to block until the device has generated all samples.

Digital waveform writes are not affected by the WaveformTiming.SampleInterval or WaveformTiming.StartTime properties on the DigitalWaveform. To configure timing for digital waveform writes, use the Overload:NationalInstruments.DAQmx.Timing.ConfigureSampleClock method.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

This method returns immediately if the output buffer has sufficient space for the samples. Otherwise, the call is blocked until the application generates enough samples to fit the new data into the output buffer.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | DigitalWaveform[] | A 1D array of DigitalWaveform objects to write to the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task. The order of the lines in the digital waveform corresponds to the order in which you add the lines to the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

DigitalMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalmultichannelwriter.html language=enus -->
## TOPIC 01935: DigitalMultiChannelWriter Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalmultichannelwriter.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalmultichannelwriter.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains methods for writing samples to one or more digital output channels in a task. Derives fromMarshalByRefObjectISynchronizeCallbacksISupportSynchronizationContextSyntaxNamespace: NationalInstruments.DAQmxpublic class DigitalMultiChannelWriter : MarshalByRefObject, ISynchronizeCallbacks, ISuppo

### DigitalMultiChannelWriter Class

Contains methods for writing samples to one or more digital output channels in a task.

#### Derives from

- MarshalByRefObject
- ISynchronizeCallbacks
- ISupportSynchronizationContext

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class DigitalMultiChannelWriter : MarshalByRefObject, ISynchronizeCallbacks, ISupportSynchronizationContext

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| DigitalMultiChannelWriter(DaqStream) | Creates a new instance of the DigitalMultiChannelWriter class to write to the specified DaqStream. |

#### Properties

| Name | Description |
| --- | --- |
| SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |
| SynchronizingObject | Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will warn if usedGets or sets the object that marshals event-handler and callback calls. |

#### Methods

| Name | Description |
| --- | --- |
| BeginWriteMultiSamplePort(bool, int, AsyncCallback, object) | Begins an asynchronous write of one or more 32-bit integer samples to one or more DOChannel objects in a task. |
| BeginWriteMultiSamplePort(bool, ushort, AsyncCallback, object) | Begins an asynchronous write of one or more 16-bit unsigned integer samples to one or more DOChannel objects in a task. |
| BeginWriteMultiSamplePort(bool, short, AsyncCallback, object) | Begins an asynchronous write of one or more 16-bit integer samples to one or more DOChannel objects in a task. |
| BeginWriteMultiSamplePort(bool, byte, AsyncCallback, object) | Begins an asynchronous write of one or more 8-bit unsigned integer samples to one or more DOChannel objects in a task. |
| BeginWriteMultiSamplePort(bool, uint, AsyncCallback, object) | Begins an asynchronous write of one or more 32-bit unsigned integer samples to one or more DOChannel objects in a task. |
| BeginWriteSingleSampleMultiLine(bool, bool, AsyncCallback, object) | Begins an asynchronous write of a Boolean sample to one or more DOChannel objects in a task. The channels can contain one or more digital lines. |
| BeginWriteSingleSamplePort(bool, ushort[], AsyncCallback, object) | Begins an asynchronous write of a single 16-bit unsigned integer sample to one or more DOChannel objects in a task. |
| BeginWriteSingleSamplePort(bool, short[], AsyncCallback, object) | Begins an asynchronous write of one or more 16-bit integer samples to one or more DOChannel objects in a task. |
| BeginWriteSingleSamplePort(bool, int[], AsyncCallback, object) | Begins an asynchronous write of a single 32-bit integer sample to one or more DOChannel objects in a task. |
| BeginWriteSingleSamplePort(bool, byte[], AsyncCallback, object) | Begins an asynchronous write of a single 8-bit unsigned integer sample to one or more DOChannel objects in a task. |
| BeginWriteSingleSamplePort(bool, uint[], AsyncCallback, object) | Begins an asynchronous write of a single 32-bit unsigned integer sample to one or more DOChannel objects in a task. |
| BeginWriteSingleSampleSingleLine(bool, bool[], AsyncCallback, object) | Begins an asynchronous write of a single Boolean sample to one or more DOChannel objects in a task. |
| BeginWriteWaveform(bool, DigitalWaveform[], AsyncCallback, object) | Begins an asynchronous write of one or more digital waveform samples to one or more DOChannel objects in a task. |
| EndWrite(IAsyncResult) | Handles the end of an asynchronous write initiated with BeginWriteMultiSamplePort(bool, uint[, ], AsyncCallback, object), BeginWriteSingleSamplePort(bool, uint[], AsyncCallback, object), BeginWriteSingleSampleMultiLine(bool, bool[, ], AsyncCallback, object), BeginWriteSingleSampleSingleLine(bool, bool[], AsyncCallback, object), or BeginWriteWaveform(bool, DigitalWaveform[], AsyncCallback, object). |
| ToString() | Returns a string representation of the object. |
| WriteMultiSamplePort(bool, short) | Writes one or more 16-bit integer samples to one or more DOChannel objects in a task. |
| WriteMultiSamplePort(bool, byte) | Writes one or more 8-bit unsigned integer samples to one or more DOChannel objects in a task. |
| WriteMultiSamplePort(bool, uint) | Writes one or more 32-bit unsigned integer samples to one or more DOChannel objects in a task. |
| WriteMultiSamplePort(bool, int) | Writes one or more 32-bit integer samples to one or more DOChannel objects in a task. |
| WriteMultiSamplePort(bool, ushort) | Writes one or more 16-bit unsigned integer samples to one or more DOChannel objects in a task. |
| WriteSingleSampleMultiLine(bool, bool) | Writes a Boolean sample to one or more DOChannel objects in a task. The channels can contain one or more digital lines. |
| WriteSingleSamplePort(bool, byte[]) | Writes a single 8-bit unsigned integer sample to one or more DOChannel objects in a task. |
| WriteSingleSamplePort(bool, short[]) | Writes one or more 16-bit integer samples to one or more DOChannel objects in a task. |
| WriteSingleSamplePort(bool, uint[]) | Writes a single 32-bit unsigned integer sample to one or more DOChannel objects in a task. |
| WriteSingleSamplePort(bool, int[]) | Writes a single 32-bit integer sample to one or more DOChannel objects in a task. |
| WriteSingleSamplePort(bool, ushort[]) | Writes a single 16-bit unsigned integer sample to one or more DOChannel objects in a task. |
| WriteSingleSampleSingleLine(bool, bool[]) | Writes a single Boolean sample to one or more DOChannel objects in a task. |
| WriteWaveform(bool, DigitalWaveform[]) | Writes one or more digital waveform samples to one or more DOChannel objects in a task. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalpatternpausetrigger-condition.html language=enus -->
## TOPIC 01936: Condition

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalpatternpausetrigger-condition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalpatternpausetrigger-condition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if the Pause Trigger occurs when the physical channels specified with Source match or differ from the digital pattern specified with Pattern. SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalPatternPauseTriggerCondition Condition { get; set; }ExceptionsTypeDescriptionNationalInstrum

### Condition

Specifies if the Pause Trigger occurs when the physical channels specified with [Source](nationalinstruments-daqmx-digitalpatternpausetrigger-source.html) match or differ from the digital pattern specified with [Pattern](nationalinstruments-daqmx-digitalpatternpausetrigger-pattern.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DigitalPatternPauseTriggerCondition](nationalinstruments-daqmx-digitalpatternpausetriggercondition.html) Condition { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalPatternPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalpatternpausetrigger-pattern.html language=enus -->
## TOPIC 01937: Pattern

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalpatternpausetrigger-pattern.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalpatternpausetrigger-pattern.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the digital pattern that must be met for the Pause Trigger to occur. SyntaxNamespace: NationalInstruments.DAQmxpublic string Pattern { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Pattern

Specifies the [digital pattern](/csh?context=nidaqmx_mxcncpts_digpattern) that must be met for the Pause Trigger to occur.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Pattern { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalPatternPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalpatternpausetrigger-source.html language=enus -->
## TOPIC 01938: Source

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalpatternpausetrigger-source.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalpatternpausetrigger-source.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the physical channels to use for pattern matching. The order of the physical channels determines the order of the pattern. If a port is included, the lines within the port are in ascending order. SyntaxNamespace: NationalInstruments.DAQmxpublic string Source { get; set; }ExceptionsTypeDesc

### Source

Specifies the physical channels to use for pattern matching. The order of the physical channels determines the order of the pattern. If a port is included, the lines within the port are in ascending order.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Source { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalPatternPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalpatternpausetrigger-tostring.html language=enus -->
## TOPIC 01939: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalpatternpausetrigger-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalpatternpausetrigger-tostring.html
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

DigitalPatternPauseTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalpatternpausetrigger.html language=enus -->
## TOPIC 01940: DigitalPatternPauseTrigger Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalpatternpausetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalpatternpausetrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties that let a task pause the acquisition or generation when the device matches a digital pattern. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class DigitalPatternPauseTrigger : MarshalByRefObject, IFilteredTypeDescriptorRemar

### DigitalPatternPauseTrigger Class

Contains properties that let a task pause the acquisition or generation when the device matches a [digital pattern](/csh?context=nidaqmx_mxcncpts_digpattern).

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class DigitalPatternPauseTrigger : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Condition | Specifies if the Pause Trigger occurs when the physical channels specified with Source match or differ from the digital pattern specified with Pattern. |
| Pattern | Specifies the digital pattern that must be met for the Pause Trigger to occur. |
| Source | Specifies the physical channels to use for pattern matching. The order of the physical channels determines the order of the pattern. If a port is included, the lines within the port are in ascending order. |

#### Methods

| Name | Description |
| --- | --- |
| ToString() | Returns a string representation of the object. |

#### See Also

- ConfigureDigitalPatternTrigger(string, string, DigitalPatternPauseTriggerCondition)
- PauseTrigger
- DigitalPattern

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalpatternpausetriggercondition.html language=enus -->
## TOPIC 01941: DigitalPatternPauseTriggerCondition Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalpatternpausetriggercondition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalpatternpausetriggercondition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if the Pause Trigger occurs when the physical channels specified with Source match or differ from the digital pattern specified with Pattern. SyntaxNamespace: NationalInstruments.DAQmxpublic enum DigitalPatternPauseTriggerConditionRemarksSpecifies if the Pause Trigger occurs when the physi

### DigitalPatternPauseTriggerCondition Enumeration

Specifies if the Pause Trigger occurs when the physical channels specified with [Source](nationalinstruments-daqmx-digitalpatternpausetrigger-source.html) match or differ from the digital pattern specified with [Pattern](nationalinstruments-daqmx-digitalpatternpausetrigger-pattern.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum DigitalPatternPauseTriggerCondition

#### Remarks

Specifies if the Pause Trigger occurs when the physical channels specified with [Source](nationalinstruments-daqmx-digitalpatternpausetrigger-source.html) match or differ from the digital pattern specified with [Pattern](nationalinstruments-daqmx-digitalpatternpausetrigger-pattern.html). Use this enumeration to get or set the value of [Condition](nationalinstruments-daqmx-digitalpatternpausetrigger-condition.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| PatternMatches | 10254 | Trigger when the physical channels match the specified pattern. |
| PatternDoesNotMatch | 10253 | Trigger when the physical channels do not match the specified pattern. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalpatternreferencetrigger-condition.html language=enus -->
## TOPIC 01942: Condition

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalpatternreferencetrigger-condition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalpatternreferencetrigger-condition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the Reference Trigger occurs when the physical channels specified with Source match or differ from the digital pattern specified with Pattern. SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalPatternReferenceTriggerCondition Condition { get; set; }ExceptionsTypeDescriptionNa

### Condition

Specifies whether the [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger) occurs when the [physical channels](/csh?context=nidaqmx_mxcncpts_chans) specified with [Source](nationalinstruments-daqmx-digitalpatternreferencetrigger-source.html) match or differ from the [digital pattern](/csh?context=nidaqmx_mxcncpts_digpattern) specified with [Pattern](nationalinstruments-daqmx-digitalpatternreferencetrigger-pattern.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DigitalPatternReferenceTriggerCondition](nationalinstruments-daqmx-digitalpatternreferencetriggercondition.html) Condition { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalPatternReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalpatternreferencetrigger-pattern.html language=enus -->
## TOPIC 01943: Pattern

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalpatternreferencetrigger-pattern.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalpatternreferencetrigger-pattern.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the digital pattern that must be met for the Reference Trigger to occur. SyntaxNamespace: NationalInstruments.DAQmxpublic string Pattern { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Pattern

Specifies the [digital pattern](/csh?context=nidaqmx_mxcncpts_digpattern) that must be met for the [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger) to occur.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Pattern { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalPatternReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalpatternreferencetrigger-source.html language=enus -->
## TOPIC 01944: Source

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalpatternreferencetrigger-source.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalpatternreferencetrigger-source.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the physical channels to use for pattern matching. The order of the physical channels determines the order of the pattern. If a port is included, the order of the physical channels within the port is in ascending order. SyntaxNamespace: NationalInstruments.DAQmxpublic string Source { get;

### Source

Specifies the [physical channels](/csh?context=nidaqmx_mxcncpts_chans) to use for pattern matching. The order of the physical channels determines the order of the pattern. If a [port](/csh?context=nidaqmx_mxcncpts_linesports) is included, the order of the physical channels within the port is in ascending order.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Source { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalPatternReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalpatternreferencetrigger-tostring.html language=enus -->
## TOPIC 01945: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalpatternreferencetrigger-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalpatternreferencetrigger-tostring.html
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

DigitalPatternReferenceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalpatternreferencetrigger.html language=enus -->
## TOPIC 01946: DigitalPatternReferenceTrigger Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalpatternreferencetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalpatternreferencetrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties that let a task stop the acquisition when the device acquires all pretrigger samples, matches a digital pattern, and acquires all posttrigger samples. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class DigitalPatternReferen

### DigitalPatternReferenceTrigger Class

Contains properties that let a task stop the acquisition when the device acquires all pretrigger samples, matches a [digital pattern](/csh?context=nidaqmx_mxcncpts_digpattern), and acquires all posttrigger samples.

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class DigitalPatternReferenceTrigger : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Condition | Specifies whether the Reference Trigger occurs when the physical channels specified with Source match or differ from the digital pattern specified with Pattern. |
| Pattern | Specifies the digital pattern that must be met for the Reference Trigger to occur. |
| Source | Specifies the physical channels to use for pattern matching. The order of the physical channels determines the order of the pattern. If a port is included, the order of the physical channels within the port is in ascending order. |

#### Methods

| Name | Description |
| --- | --- |
| ToString() | Returns a string representation of the object. |

#### See Also

- ConfigureDigitalPatternTrigger(string, string, DigitalPatternReferenceTriggerCondition, long)
- ReferenceTrigger
- DigitalPattern

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalpatternreferencetriggercondition.html language=enus -->
## TOPIC 01947: DigitalPatternReferenceTriggerCondition Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalpatternreferencetriggercondition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalpatternreferencetriggercondition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the Reference Trigger occurs when the physical channels specified with Source match or differ from the digital pattern specified with Pattern. SyntaxNamespace: NationalInstruments.DAQmxpublic enum DigitalPatternReferenceTriggerConditionRemarksSpecifies whether the Reference Trigger

### DigitalPatternReferenceTriggerCondition Enumeration

Specifies whether the [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger) occurs when the [physical channels](/csh?context=nidaqmx_mxcncpts_chans) specified with [Source](nationalinstruments-daqmx-digitalpatternreferencetrigger-source.html) match or differ from the [digital pattern](/csh?context=nidaqmx_mxcncpts_digpattern) specified with [Pattern](nationalinstruments-daqmx-digitalpatternreferencetrigger-pattern.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum DigitalPatternReferenceTriggerCondition

#### Remarks

Specifies whether the [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger) occurs when the [physical channels](/csh?context=nidaqmx_mxcncpts_chans) specified with [Source](nationalinstruments-daqmx-digitalpatternreferencetrigger-source.html) match or differ from the [digital pattern](/csh?context=nidaqmx_mxcncpts_digpattern) specified with [Pattern](nationalinstruments-daqmx-digitalpatternreferencetrigger-pattern.html). Use this enumeration to get or set the value of [Condition](nationalinstruments-daqmx-digitalpatternreferencetrigger-condition.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| PatternMatches | 10254 | Trigger when the physical channels match the specified pattern. |
| PatternDoesNotMatch | 10253 | Trigger when the physical channels do not match the specified pattern. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalpatternstarttrigger-condition.html language=enus -->
## TOPIC 01948: Condition

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalpatternstarttrigger-condition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalpatternstarttrigger-condition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the Start Trigger occurs when the physical channels specified with Source match or differ from the digital pattern specified with Pattern. SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalPatternStartTriggerCondition Condition { get; set; }ExceptionsTypeDescriptionNationalIn

### Condition

Specifies whether the Start Trigger occurs when the [physical channels](/csh?context=nidaqmx_mxcncpts_chans) specified with [Source](nationalinstruments-daqmx-digitalpatternstarttrigger-source.html) match or differ from the [digital pattern](/csh?context=nidaqmx_mxcncpts_digpattern) specified with [Pattern](nationalinstruments-daqmx-digitalpatternstarttrigger-pattern.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DigitalPatternStartTriggerCondition](nationalinstruments-daqmx-digitalpatternstarttriggercondition.html) Condition { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalPatternStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalpatternstarttrigger-pattern.html language=enus -->
## TOPIC 01949: Pattern

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalpatternstarttrigger-pattern.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalpatternstarttrigger-pattern.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the digital pattern that must be met for the Start Trigger to occur. SyntaxNamespace: NationalInstruments.DAQmxpublic string Pattern { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Pattern

Specifies the [digital pattern](/csh?context=nidaqmx_mxcncpts_digpattern) that must be met for the Start Trigger to occur.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Pattern { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalPatternStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalpatternstarttrigger-source.html language=enus -->
## TOPIC 01950: Source

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalpatternstarttrigger-source.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalpatternstarttrigger-source.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the physical channels to use for pattern matching. The order of the physical channels determines the order of the pattern. If a port is included, the order of the physical channels within the port is in ascending order. SyntaxNamespace: NationalInstruments.DAQmxpublic string Source { get;

### Source

Specifies the [physical channels](/csh?context=nidaqmx_mxcncpts_chans) to use for pattern matching. The order of the physical channels determines the order of the pattern. If a [port](/csh?context=nidaqmx_mxcncpts_linesports) is included, the order of the physical channels within the port is in ascending order.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Source { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalPatternStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalpatternstarttrigger-tostring.html language=enus -->
## TOPIC 01951: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalpatternstarttrigger-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalpatternstarttrigger-tostring.html
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

DigitalPatternStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalpatternstarttrigger.html language=enus -->
## TOPIC 01952: DigitalPatternStartTrigger Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalpatternstarttrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalpatternstarttrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties that let a task start acquiring or generating samples when a digital pattern is matched. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class DigitalPatternStartTrigger : MarshalByRefObject, IFilteredTypeDescriptorRemarksExam

### DigitalPatternStartTrigger Class

Contains properties that let a task start acquiring or generating samples when a [digital pattern](/csh?context=nidaqmx_mxcncpts_digpattern) is matched.

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class DigitalPatternStartTrigger : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Condition | Specifies whether the Start Trigger occurs when the physical channels specified with Source match or differ from the digital pattern specified with Pattern. |
| Pattern | Specifies the digital pattern that must be met for the Start Trigger to occur. |
| Source | Specifies the physical channels to use for pattern matching. The order of the physical channels determines the order of the pattern. If a port is included, the order of the physical channels within the port is in ascending order. |

#### Methods

| Name | Description |
| --- | --- |
| ToString() | Returns a string representation of the object. |

#### See Also

- StartTrigger
- DigitalPattern

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalpatternstarttriggercondition.html language=enus -->
## TOPIC 01953: DigitalPatternStartTriggerCondition Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalpatternstarttriggercondition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalpatternstarttriggercondition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the Start Trigger occurs when the physical channels specified with Source match or differ from the digital pattern specified with Pattern. SyntaxNamespace: NationalInstruments.DAQmxpublic enum DigitalPatternStartTriggerConditionRemarksSpecifies whether the Start Trigger occurs when

### DigitalPatternStartTriggerCondition Enumeration

Specifies whether the Start Trigger occurs when the [physical channels](/csh?context=nidaqmx_mxcncpts_chans) specified with [Source](nationalinstruments-daqmx-digitalpatternstarttrigger-source.html) match or differ from the [digital pattern](/csh?context=nidaqmx_mxcncpts_digpattern) specified with [Pattern](nationalinstruments-daqmx-digitalpatternstarttrigger-pattern.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum DigitalPatternStartTriggerCondition

#### Remarks

Specifies whether the Start Trigger occurs when the [physical channels](/csh?context=nidaqmx_mxcncpts_chans) specified with [Source](nationalinstruments-daqmx-digitalpatternstarttrigger-source.html) match or differ from the [digital pattern](/csh?context=nidaqmx_mxcncpts_digpattern) specified with [Pattern](nationalinstruments-daqmx-digitalpatternstarttrigger-pattern.html). Use this enumeration to get or set the value of [Condition](nationalinstruments-daqmx-digitalpatternstarttrigger-condition.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| PatternMatches | 10254 | Trigger when the physical channels match the specified pattern. |
| PatternDoesNotMatch | 10253 | Trigger when the physical channels do not match the specified pattern. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalpowerupstate.html language=enus -->
## TOPIC 01954: DigitalPowerUpState Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalpowerupstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalpowerupstate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power up state to set for the physical channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum DigitalPowerUpStateMembersNameValueDescriptionHigh10192High logic. Low10214Low logic. Tristate10310High-impedance state. You can set this power up state only on devices with bidirectio

### DigitalPowerUpState Enumeration

Specifies the power up state to set for the physical channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum DigitalPowerUpState

#### Members

| Name | Value | Description |
| --- | --- | --- |
| High | 10192 | High logic. |
| Low | 10214 | Low logic. |
| Tristate | 10310 | High-impedance state. You can set this power up state only on devices with bidirectional ports, and you can set it only on entire ports. You cannot set this power up state on dedicated digital output lines. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalpulluppulldownresistorstate.html language=enus -->
## TOPIC 01955: DigitalPullUpPullDownResistorState Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalpulluppulldownresistorstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalpulluppulldownresistorstate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pull up pull down level for each physical channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum DigitalPullUpPullDownResistorStateMembersNameValueDescriptionPullUp15950Pull up state for pull up pull down resistors. PullDown15951Pull down state for pull up pull down resistors.

### DigitalPullUpPullDownResistorState Enumeration

Specifies the pull up pull down level for each physical channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum DigitalPullUpPullDownResistorState

#### Members

| Name | Value | Description |
| --- | --- | --- |
| PullUp | 15950 | Pull up state for pull up pull down resistors. |
| PullDown | 15951 | Pull down state for pull up pull down resistors. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadmultisampleportbyte__int-asynccallback-object-byte_arr1-reallocationpolicy.html language=enus -->
## TOPIC 01956: BeginMemoryOptimizedReadMultiSamplePortByte(int, AsyncCallback, object, byte[], ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadmultisampleportbyte__int-asynccallback-object-byte_arr1-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadmultisampleportbyte__int-asynccallback-object-byte_arr1-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more 8-bit unsigned integer samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSamplePortByte(int numberOfSamples, AsyncCallback callback, object state, byte[] data, ReallocationP

### BeginMemoryOptimizedReadMultiSamplePortByte(int, AsyncCallback, object, byte[], ReallocationPolicy)

Begins an asynchronous read of one or more 8-bit unsigned integer samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSamplePortByte(int numberOfSamples, AsyncCallback callback, object state, byte[] data, ReallocationPolicy policy)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSamplePortByte(IAsyncResult, out int)](nationalinstruments-daqmx-digitalsinglechannelreader-endmemoryoptimizedreadmultisampleportbyte__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | byte[] | An initialized 1D array of 8-bit unsigned integer samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadmultisampleportbyte__int-asynccallback-object-byte_arr1.html language=enus -->
## TOPIC 01957: BeginMemoryOptimizedReadMultiSamplePortByte(int, AsyncCallback, object, byte[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadmultisampleportbyte__int-asynccallback-object-byte_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadmultisampleportbyte__int-asynccallback-object-byte_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more 8-bit unsigned integer samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSamplePortByte(int numberOfSamples, AsyncCallback callback, object state, byte[] data)RemarksIf the

### BeginMemoryOptimizedReadMultiSamplePortByte(int, AsyncCallback, object, byte[])

Begins an asynchronous read of one or more 8-bit unsigned integer samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSamplePortByte(int numberOfSamples, AsyncCallback callback, object state, byte[] data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSamplePortByte(IAsyncResult, out int)](nationalinstruments-daqmx-digitalsinglechannelreader-endmemoryoptimizedreadmultisampleportbyte__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | byte[] | An initialized 1D array of 8-bit unsigned integer samples that contains the read data. Each element in the array corresponds to a sample from the channel. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadmultisampleportint32__int-asynccallback-object-int_arr1-reallocationpolicy.html language=enus -->
## TOPIC 01958: BeginMemoryOptimizedReadMultiSamplePortInt32(int, AsyncCallback, object, int[], ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadmultisampleportint32__int-asynccallback-object-int_arr1-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadmultisampleportint32__int-asynccallback-object-int_arr1-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more 32-bit integer samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSamplePortInt32(int numberOfSamples, AsyncCallback callback, object state, int[] data, ReallocationPolicy po

### BeginMemoryOptimizedReadMultiSamplePortInt32(int, AsyncCallback, object, int[], ReallocationPolicy)

Begins an asynchronous read of one or more 32-bit integer samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSamplePortInt32(int numberOfSamples, AsyncCallback callback, object state, int[] data, ReallocationPolicy policy)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSamplePortInt32(IAsyncResult, out int)](nationalinstruments-daqmx-digitalsinglechannelreader-endmemoryoptimizedreadmultisampleportint32__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | int[] | An initialized 1D array of 32-bit integer samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadmultisampleportint32__int-asynccallback-object-int_arr1.html language=enus -->
## TOPIC 01959: BeginMemoryOptimizedReadMultiSamplePortInt32(int, AsyncCallback, object, int[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadmultisampleportint32__int-asynccallback-object-int_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadmultisampleportint32__int-asynccallback-object-int_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more 32-bit integer samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSamplePortInt32(int numberOfSamples, AsyncCallback callback, object state, int[] data)RemarksIf the data buf

### BeginMemoryOptimizedReadMultiSamplePortInt32(int, AsyncCallback, object, int[])

Begins an asynchronous read of one or more 32-bit integer samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSamplePortInt32(int numberOfSamples, AsyncCallback callback, object state, int[] data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSamplePortInt32(IAsyncResult, out int)](nationalinstruments-daqmx-digitalsinglechannelreader-endmemoryoptimizedreadmultisampleportint32__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | int[] | An initialized 1D array of 32-bit integer samples that contains the read data. Each element in the array corresponds to a sample from the channel. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadmultisampleportuint16__int-asynccallback-object-ushort_arr1-reallocationpolicy.html language=enus -->
## TOPIC 01960: BeginMemoryOptimizedReadMultiSamplePortUInt16(int, AsyncCallback, object, ushort[], ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadmultisampleportuint16__int-asynccallback-object-ushort_arr1-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadmultisampleportuint16__int-asynccallback-object-ushort_arr1-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more 16-bit unsigned integer samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSamplePortUInt16(int numberOfSamples, AsyncCallback callback, object state, ushort[] data, Realloca

### BeginMemoryOptimizedReadMultiSamplePortUInt16(int, AsyncCallback, object, ushort[], ReallocationPolicy)

Begins an asynchronous read of one or more 16-bit unsigned integer samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSamplePortUInt16(int numberOfSamples, AsyncCallback callback, object state, ushort[] data, ReallocationPolicy policy)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSamplePortUInt16(IAsyncResult, out int)](nationalinstruments-daqmx-digitalsinglechannelreader-endmemoryoptimizedreadmultisampleportuint16__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | ushort[] | An initialized 1D array of 16-bit unsigned integer samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadmultisampleportuint16__int-asynccallback-object-ushort_arr1.html language=enus -->
## TOPIC 01961: BeginMemoryOptimizedReadMultiSamplePortUInt16(int, AsyncCallback, object, ushort[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadmultisampleportuint16__int-asynccallback-object-ushort_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadmultisampleportuint16__int-asynccallback-object-ushort_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more 16-bit unsigned integer samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSamplePortUInt16(int numberOfSamples, AsyncCallback callback, object state, ushort[] data)RemarksIf

### BeginMemoryOptimizedReadMultiSamplePortUInt16(int, AsyncCallback, object, ushort[])

Begins an asynchronous read of one or more 16-bit unsigned integer samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSamplePortUInt16(int numberOfSamples, AsyncCallback callback, object state, ushort[] data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSamplePortUInt16(IAsyncResult, out int)](nationalinstruments-daqmx-digitalsinglechannelreader-endmemoryoptimizedreadmultisampleportuint16__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | ushort[] | An initialized 1D array of 16-bit unsigned integer samples that contains the read data. Each element in the array corresponds to a sample from the channel. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadmultisampleportuint32__int-asynccallback-object-uint_arr1-reallocationpolicy.html language=enus -->
## TOPIC 01962: BeginMemoryOptimizedReadMultiSamplePortUInt32(int, AsyncCallback, object, uint[], ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadmultisampleportuint32__int-asynccallback-object-uint_arr1-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadmultisampleportuint32__int-asynccallback-object-uint_arr1-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more 32-bit unsigned integer samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSamplePortUInt32(int numberOfSamples, AsyncCallback callback, object state, uint[] data, Reallocati

### BeginMemoryOptimizedReadMultiSamplePortUInt32(int, AsyncCallback, object, uint[], ReallocationPolicy)

Begins an asynchronous read of one or more 32-bit unsigned integer samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSamplePortUInt32(int numberOfSamples, AsyncCallback callback, object state, uint[] data, ReallocationPolicy policy)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSamplePortUInt32(IAsyncResult, out int)](nationalinstruments-daqmx-digitalsinglechannelreader-endmemoryoptimizedreadmultisampleportuint32__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | uint[] | An initialized 1D array of 32-bit unsigned integer samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadmultisampleportuint32__int-asynccallback-object-uint_arr1.html language=enus -->
## TOPIC 01963: BeginMemoryOptimizedReadMultiSamplePortUInt32(int, AsyncCallback, object, uint[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadmultisampleportuint32__int-asynccallback-object-uint_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadmultisampleportuint32__int-asynccallback-object-uint_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more 32-bit unsigned integer samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSamplePortUInt32(int numberOfSamples, AsyncCallback callback, object state, uint[] data)RemarksIf t

### BeginMemoryOptimizedReadMultiSamplePortUInt32(int, AsyncCallback, object, uint[])

Begins an asynchronous read of one or more 32-bit unsigned integer samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSamplePortUInt32(int numberOfSamples, AsyncCallback callback, object state, uint[] data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSamplePortUInt32(IAsyncResult, out int)](nationalinstruments-daqmx-digitalsinglechannelreader-endmemoryoptimizedreadmultisampleportuint32__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | uint[] | An initialized 1D array of 32-bit unsigned integer samples that contains the read data. Each element in the array corresponds to a sample from the channel. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadsinglesamplemultiline__asynccallback-object-bool_arr1.html language=enus -->
## TOPIC 01964: BeginMemoryOptimizedReadSingleSampleMultiLine(AsyncCallback, object, bool[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadsinglesamplemultiline__asynccallback-object-bool_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadsinglesamplemultiline__asynccallback-object-bool_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a single Boolean sample from a single DIChannel in a task. The channel can contain multiple digital lines. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadSingleSampleMultiLine(AsyncCallback callback, object state, bool[] data)Rema

### BeginMemoryOptimizedReadSingleSampleMultiLine(AsyncCallback, object, bool[])

Begins an asynchronous read of a single Boolean sample from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task. The channel can contain multiple digital lines.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadSingleSampleMultiLine(AsyncCallback callback, object state, bool[] data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndReadSingleSampleMultiLine(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesamplemultiline__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | bool[] | An initialized 1D array of Boolean samples that contains the read data. Each element in the array corresponds to a digital line in the channel. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-beginreadmultisampleportbyte__int-asynccallback-object.html language=enus -->
## TOPIC 01965: BeginReadMultiSamplePortByte(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-beginreadmultisampleportbyte__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-beginreadmultisampleportbyte__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more 8-bit unsigned integer samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadMultiSamplePortByte(int numberOfSamples, AsyncCallback callback, object state)RemarksTo get the read data or any excepti

### BeginReadMultiSamplePortByte(int, AsyncCallback, object)

Begins an asynchronous read of one or more 8-bit unsigned integer samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadMultiSamplePortByte(int numberOfSamples, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadMultiSamplePortByte(int, AsyncCallback, object), call [EndReadMultiSamplePortByte(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelreader-endreadmultisampleportbyte__iasyncresult.html) with the returned IAsyncResult.

Use this method for devices with up to eight lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-beginreadmultisampleportint16__int-asynccallback-object.html language=enus -->
## TOPIC 01966: BeginReadMultiSamplePortInt16(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-beginreadmultisampleportint16__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-beginreadmultisampleportint16__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more 16-bit integer samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadMultiSamplePortInt16(int numberOfSamples, AsyncCallback callback, object state)RemarksTo get the read data or any exceptions tha

### BeginReadMultiSamplePortInt16(int, AsyncCallback, object)

Begins an asynchronous read of one or more 16-bit integer samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadMultiSamplePortInt16(int numberOfSamples, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadMultiSamplePortInt16(int, AsyncCallback, object), call [EndReadMultiSamplePortInt16(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelreader-endreadmultisampleportint16__iasyncresult.html) with the returned IAsyncResult.

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-beginreadmultisampleportint32__int-asynccallback-object.html language=enus -->
## TOPIC 01967: BeginReadMultiSamplePortInt32(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-beginreadmultisampleportint32__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-beginreadmultisampleportint32__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more 32-bit integer samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadMultiSamplePortInt32(int numberOfSamples, AsyncCallback callback, object state)RemarksTo get the read data or any exceptions tha

### BeginReadMultiSamplePortInt32(int, AsyncCallback, object)

Begins an asynchronous read of one or more 32-bit integer samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadMultiSamplePortInt32(int numberOfSamples, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadMultiSamplePortInt32(int, AsyncCallback, object), call [EndReadMultiSamplePortInt32(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelreader-endreadmultisampleportint32__iasyncresult.html) with the returned IAsyncResult.

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-beginreadmultisampleportuint16__int-asynccallback-object.html language=enus -->
## TOPIC 01968: BeginReadMultiSamplePortUInt16(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-beginreadmultisampleportuint16__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-beginreadmultisampleportuint16__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more 16-bit unsigned integer samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadMultiSamplePortUInt16(int numberOfSamples, AsyncCallback callback, object state)RemarksTo get the read data or any exce

### BeginReadMultiSamplePortUInt16(int, AsyncCallback, object)

Begins an asynchronous read of one or more 16-bit unsigned integer samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadMultiSamplePortUInt16(int numberOfSamples, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadMultiSamplePortUInt16(int, AsyncCallback, object), call [EndReadMultiSamplePortUInt16(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelreader-endreadmultisampleportuint16__iasyncresult.html) with the returned IAsyncResult.

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-beginreadmultisampleportuint32__int-asynccallback-object.html language=enus -->
## TOPIC 01969: BeginReadMultiSamplePortUInt32(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-beginreadmultisampleportuint32__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-beginreadmultisampleportuint32__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more 32-bit unsigned integer samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadMultiSamplePortUInt32(int numberOfSamples, AsyncCallback callback, object state)RemarksTo get the read data or any exce

### BeginReadMultiSamplePortUInt32(int, AsyncCallback, object)

Begins an asynchronous read of one or more 32-bit unsigned integer samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadMultiSamplePortUInt32(int numberOfSamples, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadMultiSamplePortUInt32(int, AsyncCallback, object), call [EndReadMultiSamplePortUInt32(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelreader-endreadmultisampleportuint32__iasyncresult.html) with the returned IAsyncResult.

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesamplemultiline__asynccallback-object.html language=enus -->
## TOPIC 01970: BeginReadSingleSampleMultiLine(AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesamplemultiline__asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesamplemultiline__asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a single Boolean sample from a single DIChannel in a task. The channel can contain multiple digital lines. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadSingleSampleMultiLine(AsyncCallback callback, object state)RemarksTo get the read data or a

### BeginReadSingleSampleMultiLine(AsyncCallback, object)

Begins an asynchronous read of a single Boolean sample from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task. The channel can contain multiple digital lines.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadSingleSampleMultiLine(AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSampleMultiLine(AsyncCallback, object), call [EndReadSingleSampleMultiLine(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesamplemultiline__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesampleportbyte__asynccallback-object.html language=enus -->
## TOPIC 01971: BeginReadSingleSamplePortByte(AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesampleportbyte__asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesampleportbyte__asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a single 8-bit unsigned integer sample from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadSingleSamplePortByte(AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occurred during

### BeginReadSingleSamplePortByte(AsyncCallback, object)

Begins an asynchronous read of a single 8-bit unsigned integer sample from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadSingleSamplePortByte(AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSamplePortByte(AsyncCallback, object), call [EndReadSingleSamplePortByte(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesampleportbyte__iasyncresult.html) with the returned IAsyncResult.

Use this method for devices with up to eight lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesampleportint16__asynccallback-object.html language=enus -->
## TOPIC 01972: BeginReadSingleSamplePortInt16(AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesampleportint16__asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesampleportint16__asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a single 16-bit integer sample from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadSingleSamplePortInt16(AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occurred during an asy

### BeginReadSingleSamplePortInt16(AsyncCallback, object)

Begins an asynchronous read of a single 16-bit integer sample from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadSingleSamplePortInt16(AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSamplePortInt16(AsyncCallback, object), call[EndReadSingleSamplePortInt16(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesampleportint16__iasyncresult.html) with the returned IAsyncResult.

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesampleportint32__asynccallback-object.html language=enus -->
## TOPIC 01973: BeginReadSingleSamplePortInt32(AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesampleportint32__asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesampleportint32__asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a single 32-bit integer sample from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadSingleSamplePortInt32(AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occurred during an asy

### BeginReadSingleSamplePortInt32(AsyncCallback, object)

Begins an asynchronous read of a single 32-bit integer sample from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadSingleSamplePortInt32(AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSamplePortInt32(AsyncCallback, object), call[EndReadSingleSamplePortInt32(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesampleportint32__iasyncresult.html) with the returned IAsyncResult.

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesampleportuint16__asynccallback-object.html language=enus -->
## TOPIC 01974: BeginReadSingleSamplePortUInt16(AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesampleportuint16__asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesampleportuint16__asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a single 16-bit unsigned integer sample from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadSingleSamplePortUInt16(AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occurred dur

### BeginReadSingleSamplePortUInt16(AsyncCallback, object)

Begins an asynchronous read of a single 16-bit unsigned integer sample from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadSingleSamplePortUInt16(AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSamplePortUInt16(AsyncCallback, object), call [EndReadSingleSamplePortUInt16(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesampleportuint16__iasyncresult.html) with the returned IAsyncResult.

Use this method for devices with up to 16 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesampleportuint32__asynccallback-object.html language=enus -->
## TOPIC 01975: BeginReadSingleSamplePortUInt32(AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesampleportuint32__asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesampleportuint32__asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a single 32-bit unsigned integer sample from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadSingleSamplePortUInt32(AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occurred dur

### BeginReadSingleSamplePortUInt32(AsyncCallback, object)

Begins an asynchronous read of a single 32-bit unsigned integer sample from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadSingleSamplePortUInt32(AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSamplePortUInt32(AsyncCallback, object), call [EndReadSingleSamplePortUInt32(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesampleportuint32__iasyncresult.html) with the returned IAsyncResult.

Use this method for devices with up to 32 lines per port.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesamplesingleline__asynccallback-object.html language=enus -->
## TOPIC 01976: BeginReadSingleSampleSingleLine(AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesamplesingleline__asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesamplesingleline__asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a single Boolean sample from a single DIChannel in a task. The task can contain only a single digital line. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadSingleSampleSingleLine(AsyncCallback callback, object state)RemarksTo get the read data or

### BeginReadSingleSampleSingleLine(AsyncCallback, object)

Begins an asynchronous read of a single Boolean sample from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task. The task can contain only a single digital line.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadSingleSampleSingleLine(AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSampleSingleLine(AsyncCallback, object), call [EndReadSingleSampleSingleLine(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesamplesingleline__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-beginreadwaveform__int-asynccallback-object.html language=enus -->
## TOPIC 01977: BeginReadWaveform(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-beginreadwaveform__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-beginreadwaveform__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more digital waveform samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadWaveform(int numberOfSamples, AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occurred

### BeginReadWaveform(int, AsyncCallback, object)

Begins an asynchronous read of one or more digital waveform samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadWaveform(int numberOfSamples, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadWaveform(int, AsyncCallback, object), call [EndReadWaveform(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelreader-endreadwaveform__iasyncresult.html) with the returned IAsyncResult.

The data returned from digital waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) you are reading from.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-beginreadwaveform__timespan-asynccallback-object.html language=enus -->
## TOPIC 01978: BeginReadWaveform(TimeSpan, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-beginreadwaveform__timespan-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-beginreadwaveform__timespan-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more digital waveform samples from a single DIChannel in a task for a specified duration . SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadWaveform(TimeSpan duration, AsyncCallback callback, object state)RemarksTo get the read data or any

### BeginReadWaveform(TimeSpan, AsyncCallback, object)

Begins an asynchronous read of one or more digital waveform samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task for a specified *duration* .

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadWaveform(TimeSpan duration, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadWaveform(TimeSpan, AsyncCallback, object), call [EndReadWaveform(IAsyncResult)](nationalinstruments-daqmx-digitalsinglechannelreader-endreadwaveform__iasyncresult.html), passing the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units when creating channels using the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

The data returned from analog waveform reads is affected by the [WaveformAttributeMode](nationalinstruments-daqmx-daqstream-waveformattributemode.html) property of the [DaqStream](nationalinstruments-daqmx-daqstream.html) being read.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the [Stream](nationalinstruments-daqmx-task-stream.html) object used for the reads or writes.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| duration | TimeSpan | The duration of time to read the waveform. The duration specified must be long enough to read at least one sample at the configured SampleClockRate. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-digitalsinglechannelreader__daqstream.html language=enus -->
## TOPIC 01979: DigitalSingleChannelReader(DaqStream)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-digitalsinglechannelreader__daqstream.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-digitalsinglechannelreader__daqstream.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of the DigitalSingleChannelReader class to read from the specified DaqStream. SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalSingleChannelReader(DaqStream stream)RemarksEach Task object contains a Stream property that serves as the connection point for readers to acce

### DigitalSingleChannelReader(DaqStream)

Creates a new instance of the [DigitalSingleChannelReader](nationalinstruments-daqmx-digitalsinglechannelreader.html) class to read from the specified [DaqStream](nationalinstruments-daqmx-daqstream.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public DigitalSingleChannelReader(DaqStream stream)

#### Remarks

Each [Task](nationalinstruments-daqmx-task.html) object contains a [Stream](nationalinstruments-daqmx-task-stream.html) property that serves as the connection point for readers to access the samples generated by that task.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| stream | DaqStream | The DaqStream to read. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-endmemoryoptimizedreadmultisampleportbyte__iasyncresult-out.html language=enus -->
## TOPIC 01980: EndMemoryOptimizedReadMultiSamplePortByte(IAsyncResult, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-endmemoryoptimizedreadmultisampleportbyte__iasyncresult-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-endmemoryoptimizedreadmultisampleportbyte__iasyncresult-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePortByte(int, AsyncCallback, object, byte[]) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic byte[] EndMemoryOptimizedReadMultiSamplePortByte(IAsyncResult asyncResult, out int a

### EndMemoryOptimizedReadMultiSamplePortByte(IAsyncResult, out int)

Handles the end of an asynchronous read initiated with [BeginMemoryOptimizedReadMultiSamplePortByte(int, AsyncCallback, object, byte[])](nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadmultisampleportbyte__int-asynccallback-object-byte_arr1.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public byte[] EndMemoryOptimizedReadMultiSamplePortByte(IAsyncResult asyncResult, out int actualNumberOfSamplesRead)

#### Remarks

If you call this method before the asynchronous read is complete, it waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSamplePortByte(int, AsyncCallback, object, byte[]). |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A 1D array of 8-bit unsigned integer samples that contains the read data. Each element in the array corresponds to a sample from the channel.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSamplePortByte(int, AsyncCallback, object, byte[]). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-endmemoryoptimizedreadmultisampleportint32__iasyncresult-out.html language=enus -->
## TOPIC 01981: EndMemoryOptimizedReadMultiSamplePortInt32(IAsyncResult, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-endmemoryoptimizedreadmultisampleportint32__iasyncresult-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-endmemoryoptimizedreadmultisampleportint32__iasyncresult-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePortInt32(int, AsyncCallback, object, int[, ]) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic int[] EndMemoryOptimizedReadMultiSamplePortInt32(IAsyncResult asyncResult, out int

### EndMemoryOptimizedReadMultiSamplePortInt32(IAsyncResult, out int)

Handles the end of an asynchronous read initiated with [BeginMemoryOptimizedReadMultiSamplePortInt32(int, AsyncCallback, object, int[, ])](nationalinstruments-daqmx-digitalmultichannelreader-beginmemoryoptimizedreadmultisampleportint32__int-asynccallback-object-int_arr2.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int[] EndMemoryOptimizedReadMultiSamplePortInt32(IAsyncResult asyncResult, out int actualNumberOfSamplesRead)

#### Remarks

If you call this method before the asynchronous read IAsyncResult is complete, it waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSamplePortInt32(int, AsyncCallback, object, int[, ]). |
| actualNumberOfSamplesRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A 1D array of 32-bit integer samples that contains the read data. Each element in the array corresponds to a sample from the channel.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSamplePortInt32(int, AsyncCallback, object, int[, ]). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-endmemoryoptimizedreadmultisampleportuint16__iasyncresult-out.html language=enus -->
## TOPIC 01982: EndMemoryOptimizedReadMultiSamplePortUInt16(IAsyncResult, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-endmemoryoptimizedreadmultisampleportuint16__iasyncresult-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-endmemoryoptimizedreadmultisampleportuint16__iasyncresult-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePortUInt16(int, AsyncCallback, object, ushort[]) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic ushort[] EndMemoryOptimizedReadMultiSamplePortUInt16(IAsyncResult asyncResult, o

### EndMemoryOptimizedReadMultiSamplePortUInt16(IAsyncResult, out int)

Handles the end of an asynchronous read initiated with [BeginMemoryOptimizedReadMultiSamplePortUInt16(int, AsyncCallback, object, ushort[])](nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadmultisampleportuint16__int-asynccallback-object-ushort_arr1.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public ushort[] EndMemoryOptimizedReadMultiSamplePortUInt16(IAsyncResult asyncResult, out int actualNumberOfSamplesRead)

#### Remarks

If you call this method before the asynchronous read is complete, it waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSamplePortUInt16(int, AsyncCallback, object, ushort[]). |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A 1D array of 16-bit unsigned integer samples that contains the read data. Each element in the array corresponds to a sample from the channel.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSamplePortUInt16(int, AsyncCallback, object, ushort[]). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-endmemoryoptimizedreadmultisampleportuint32__iasyncresult-out.html language=enus -->
## TOPIC 01983: EndMemoryOptimizedReadMultiSamplePortUInt32(IAsyncResult, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-endmemoryoptimizedreadmultisampleportuint32__iasyncresult-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-endmemoryoptimizedreadmultisampleportuint32__iasyncresult-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePortUInt32(int, AsyncCallback, object, uint[]) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic uint[] EndMemoryOptimizedReadMultiSamplePortUInt32(IAsyncResult asyncResult, out i

### EndMemoryOptimizedReadMultiSamplePortUInt32(IAsyncResult, out int)

Handles the end of an asynchronous read initiated with [BeginMemoryOptimizedReadMultiSamplePortUInt32(int, AsyncCallback, object, uint[])](nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadmultisampleportuint32__int-asynccallback-object-uint_arr1.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint[] EndMemoryOptimizedReadMultiSamplePortUInt32(IAsyncResult asyncResult, out int actualNumberOfSamplesRead)

#### Remarks

If you call this method before the asynchronous read is complete, it waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSamplePortUInt32(int, AsyncCallback, object, uint[]). |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A 1D array of 32-bit unsigned integer samples that contains the read data. Each element in the array corresponds to a sample from the channel.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSamplePortUInt32(int, AsyncCallback, object, uint[]). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-endmemoryoptimizedreadsinglesamplemultiline__iasyncresult.html language=enus -->
## TOPIC 01984: EndMemoryOptimizedReadSingleSampleMultiLine(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-endmemoryoptimizedreadsinglesamplemultiline__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-endmemoryoptimizedreadsinglesamplemultiline__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadSingleSampleMultiLine(AsyncCallback, object, bool[]) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic bool[] EndMemoryOptimizedReadSingleSampleMultiLine(IAsyncResult asyncResult)RemarksIf y

### EndMemoryOptimizedReadSingleSampleMultiLine(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginMemoryOptimizedReadSingleSampleMultiLine(AsyncCallback, object, bool[])](nationalinstruments-daqmx-digitalsinglechannelreader-beginmemoryoptimizedreadsinglesamplemultiline__asynccallback-object-bool_arr1.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool[] EndMemoryOptimizedReadSingleSampleMultiLine(IAsyncResult asyncResult)

#### Remarks

If you call this method before the asynchronous read is complete, it waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadSingleSampleMultiLine(AsyncCallback, object, bool[]). |

#### Returns

A 1D array of Boolean samples from the task. Each element of the array corresponds to a digital line in the channel.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadSingleSampleMultiLine(AsyncCallback, object, bool[]). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-endreadmultisampleportbyte__iasyncresult.html language=enus -->
## TOPIC 01985: EndReadMultiSamplePortByte(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-endreadmultisampleportbyte__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-endreadmultisampleportbyte__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortByte(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic byte[] EndReadMultiSamplePortByte(IAsyncResult asyncResult)RemarksIf you call EndReadMultiSamplePortByte(IA

### EndReadMultiSamplePortByte(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadMultiSamplePortByte(int, AsyncCallback, object)](nationalinstruments-daqmx-digitalsinglechannelreader-beginreadmultisampleportbyte__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public byte[] EndReadMultiSamplePortByte(IAsyncResult asyncResult)

#### Remarks

If you call EndReadMultiSamplePortByte(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSamplePortByte(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSamplePortByte(int, AsyncCallback, object). |

#### Returns

A 1D array of 8-bit unsigned integer samples from the task. Each element in the array corresponds to a sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadMultiSamplePortByte(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-endreadmultisampleportint16__iasyncresult.html language=enus -->
## TOPIC 01986: EndReadMultiSamplePortInt16(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-endreadmultisampleportint16__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-endreadmultisampleportint16__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortInt16(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic short[] EndReadMultiSamplePortInt16(IAsyncResult asyncResult)RemarksIf you call EndReadMultiSamplePortInt1

### EndReadMultiSamplePortInt16(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadMultiSamplePortInt16(int, AsyncCallback, object)](nationalinstruments-daqmx-digitalsinglechannelreader-beginreadmultisampleportint16__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public short[] EndReadMultiSamplePortInt16(IAsyncResult asyncResult)

#### Remarks

If you call EndReadMultiSamplePortInt16(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSamplePortInt16(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSamplePortInt16(int, AsyncCallback, object). |

#### Returns

A 1D array of 16-bit integer samples from the task. Each element in the array corresponds to a sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadMultiSamplePortInt16(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-endreadmultisampleportint32__iasyncresult.html language=enus -->
## TOPIC 01987: EndReadMultiSamplePortInt32(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-endreadmultisampleportint32__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-endreadmultisampleportint32__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortInt32(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic int[] EndReadMultiSamplePortInt32(IAsyncResult asyncResult)RemarksIf you call EndReadMultiSamplePortInt32(

### EndReadMultiSamplePortInt32(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadMultiSamplePortInt32(int, AsyncCallback, object)](nationalinstruments-daqmx-digitalsinglechannelreader-beginreadmultisampleportint32__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int[] EndReadMultiSamplePortInt32(IAsyncResult asyncResult)

#### Remarks

If you call EndReadMultiSamplePortInt32(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSamplePortInt32(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSamplePortInt32(int, AsyncCallback, object). |

#### Returns

A 1D array of 32-bit integer samples from the task. Each element in the array corresponds to a sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadMultiSamplePortInt32(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-endreadmultisampleportuint16__iasyncresult.html language=enus -->
## TOPIC 01988: EndReadMultiSamplePortUInt16(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-endreadmultisampleportuint16__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-endreadmultisampleportuint16__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortUInt16(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic ushort[] EndReadMultiSamplePortUInt16(IAsyncResult asyncResult)RemarksIf you call EndReadMultiSamplePortU

### EndReadMultiSamplePortUInt16(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadMultiSamplePortUInt16(int, AsyncCallback, object)](nationalinstruments-daqmx-digitalsinglechannelreader-beginreadmultisampleportuint16__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public ushort[] EndReadMultiSamplePortUInt16(IAsyncResult asyncResult)

#### Remarks

If you call EndReadMultiSamplePortUInt16(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSamplePortUInt16(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSamplePortUInt16(int, AsyncCallback, object). |

#### Returns

A 1D array of 16-bit unsigned integer samples from the task. Each element in the array corresponds to a sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadMultiSamplePortUInt16(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-endreadmultisampleportuint32__iasyncresult.html language=enus -->
## TOPIC 01989: EndReadMultiSamplePortUInt32(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-endreadmultisampleportuint32__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-endreadmultisampleportuint32__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortUInt32(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic uint[] EndReadMultiSamplePortUInt32(IAsyncResult asyncResult)RemarksIf you call EndReadMultiSamplePortUIn

### EndReadMultiSamplePortUInt32(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadMultiSamplePortUInt32(int, AsyncCallback, object)](nationalinstruments-daqmx-digitalsinglechannelreader-beginreadmultisampleportuint32__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint[] EndReadMultiSamplePortUInt32(IAsyncResult asyncResult)

#### Remarks

If you call EndReadMultiSamplePortUInt32(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSamplePortUInt32(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSamplePortUInt32(int, AsyncCallback, object). |

#### Returns

A 1D array of 32-bit unsigned integer samples from the task. Each element in the array corresponds to a sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadMultiSamplePortUInt32(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesamplemultiline__iasyncresult.html language=enus -->
## TOPIC 01990: EndReadSingleSampleMultiLine(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesamplemultiline__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesamplemultiline__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadSingleSampleMultiLine(AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic bool[] EndReadSingleSampleMultiLine(IAsyncResult asyncResult)RemarksIf you call EndReadSingleSampleMultiLine(I

### EndReadSingleSampleMultiLine(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadSingleSampleMultiLine(AsyncCallback, object)](nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesamplemultiline__asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool[] EndReadSingleSampleMultiLine(IAsyncResult asyncResult)

#### Remarks

If you call EndReadSingleSampleMultiLine(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSampleMultiLine(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSampleMultiLine(AsyncCallback, object). |

#### Returns

A 1D array of Boolean samples from the task. Each element of the array corresponds to a digital line in the channel.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadSingleSampleMultiLine(AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesampleportbyte__iasyncresult.html language=enus -->
## TOPIC 01991: EndReadSingleSamplePortByte(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesampleportbyte__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesampleportbyte__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortByte(AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic byte EndReadSingleSamplePortByte(IAsyncResult asyncResult)RemarksIf you call EndReadSingleSamplePortByte(IAsync

### EndReadSingleSamplePortByte(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadSingleSamplePortByte(AsyncCallback, object)](nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesampleportbyte__asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public byte EndReadSingleSamplePortByte(IAsyncResult asyncResult)

#### Remarks

If you call EndReadSingleSamplePortByte(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSamplePortByte(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSamplePortByte(AsyncCallback, object). |

#### Returns

An 8-bit unsigned integer sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadSingleSamplePortByte(AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesampleportint16__iasyncresult.html language=enus -->
## TOPIC 01992: EndReadSingleSamplePortInt16(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesampleportint16__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesampleportint16__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortInt16(AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic short EndReadSingleSamplePortInt16(IAsyncResult asyncResult)RemarksIf you call EndReadSingleSamplePortInt16(IA

### EndReadSingleSamplePortInt16(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadSingleSamplePortInt16(AsyncCallback, object)](nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesampleportint16__asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public short EndReadSingleSamplePortInt16(IAsyncResult asyncResult)

#### Remarks

If you call EndReadSingleSamplePortInt16(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSamplePortInt16(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSamplePortInt16(AsyncCallback, object). |

#### Returns

A 16-bit integer sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadSingleSamplePortInt16(AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesampleportint32__iasyncresult.html language=enus -->
## TOPIC 01993: EndReadSingleSamplePortInt32(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesampleportint32__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesampleportint32__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortInt32(AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic int EndReadSingleSamplePortInt32(IAsyncResult asyncResult)RemarksIf you call EndReadSingleSamplePortInt32(IAsy

### EndReadSingleSamplePortInt32(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadSingleSamplePortInt32(AsyncCallback, object)](nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesampleportint32__asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int EndReadSingleSamplePortInt32(IAsyncResult asyncResult)

#### Remarks

If you call EndReadSingleSamplePortInt32(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSamplePortInt32(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSamplePortInt32(AsyncCallback, object). |

#### Returns

A 32-bit integer sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadSingleSamplePortInt32(AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesampleportuint16__iasyncresult.html language=enus -->
## TOPIC 01994: EndReadSingleSamplePortUInt16(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesampleportuint16__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesampleportuint16__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortUInt16(AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic ushort EndReadSingleSamplePortUInt16(IAsyncResult asyncResult)RemarksIf you call EndReadSingleSamplePortUInt1

### EndReadSingleSamplePortUInt16(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadSingleSamplePortUInt16(AsyncCallback, object)](nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesampleportuint16__asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public ushort EndReadSingleSamplePortUInt16(IAsyncResult asyncResult)

#### Remarks

If you call EndReadSingleSamplePortUInt16(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSamplePortUInt16(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSamplePortUInt16(AsyncCallback, object). |

#### Returns

A 16-bit unsigned integer sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadSingleSamplePortUInt16(AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesampleportuint32__iasyncresult.html language=enus -->
## TOPIC 01995: EndReadSingleSamplePortUInt32(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesampleportuint32__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesampleportuint32__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortUInt32(AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic uint EndReadSingleSamplePortUInt32(IAsyncResult asyncResult)RemarksIf you call EndReadSingleSamplePortUInt32(

### EndReadSingleSamplePortUInt32(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadSingleSamplePortUInt32(AsyncCallback, object)](nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesampleportuint32__asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint EndReadSingleSamplePortUInt32(IAsyncResult asyncResult)

#### Remarks

If you call EndReadSingleSamplePortUInt32(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSamplePortUInt32(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSamplePortUInt32(AsyncCallback, object). |

#### Returns

A 32-bit unsigned integer sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadSingleSamplePortUInt32(AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesamplesingleline__iasyncresult.html language=enus -->
## TOPIC 01996: EndReadSingleSampleSingleLine(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesamplesingleline__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-endreadsinglesamplesingleline__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadSingleSampleSingleLine(AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic bool EndReadSingleSampleSingleLine(IAsyncResult asyncResult)RemarksIf you call EndReadSingleSampleSingleLine(

### EndReadSingleSampleSingleLine(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadSingleSampleSingleLine(AsyncCallback, object)](nationalinstruments-daqmx-digitalsinglechannelreader-beginreadsinglesamplesingleline__asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool EndReadSingleSampleSingleLine(IAsyncResult asyncResult)

#### Remarks

If you call EndReadSingleSampleSingleLine(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSampleSingleLine(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSampleSingleLine(AsyncCallback, object). |

#### Returns

A Boolean sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadSingleSampleSingleLine(AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-endreadwaveform__iasyncresult.html language=enus -->
## TOPIC 01997: EndReadWaveform(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-endreadwaveform__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-endreadwaveform__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadWaveform(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalWaveform EndReadWaveform(IAsyncResult asyncResult)RemarksIf you call EndReadWaveform(IAsyncResult) before the a

### EndReadWaveform(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadWaveform(int, AsyncCallback, object)](nationalinstruments-daqmx-digitalsinglechannelreader-beginreadwaveform__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public DigitalWaveform EndReadWaveform(IAsyncResult asyncResult)

#### Remarks

If you call EndReadWaveform(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadWaveform(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadWaveform(int, AsyncCallback, object). |

#### Returns

A DigitalWaveform containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadWaveform(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-memoryoptimizedreadmultisampleportbyte__int-ref-out.html language=enus -->
## TOPIC 01998: MemoryOptimizedReadMultiSamplePortByte(int, ref byte[], out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-memoryoptimizedreadmultisampleportbyte__int-ref-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-memoryoptimizedreadmultisampleportbyte__int-ref-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 8-bit unsigned integer samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic byte[] MemoryOptimizedReadMultiSamplePortByte(int numberOfSamples, ref byte[] data, out int actualNumberOfSamplesRead)RemarksIf the data buffer is large enough to hold

### MemoryOptimizedReadMultiSamplePortByte(int, ref byte[], out int)

Reads one or more 8-bit unsigned integer samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public byte[] MemoryOptimizedReadMultiSamplePortByte(int numberOfSamples, ref byte[] data, out int actualNumberOfSamplesRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref byte[] | An initialized 1D array of 8-bit unsigned integer samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-memoryoptimizedreadmultisampleportbyte__int-ref-reallocationpolicy-out.html language=enus -->
## TOPIC 01999: MemoryOptimizedReadMultiSamplePortByte(int, ref byte[], ReallocationPolicy, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-memoryoptimizedreadmultisampleportbyte__int-ref-reallocationpolicy-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-memoryoptimizedreadmultisampleportbyte__int-ref-reallocationpolicy-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 8-bit unsigned integer samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic byte[] MemoryOptimizedReadMultiSamplePortByte(int numberOfSamples, ref byte[] data, ReallocationPolicy policy, out int actualNumberOfSamplesRead)RemarksIf the data buf

### MemoryOptimizedReadMultiSamplePortByte(int, ref byte[], ReallocationPolicy, out int)

Reads one or more 8-bit unsigned integer samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public byte[] MemoryOptimizedReadMultiSamplePortByte(int numberOfSamples, ref byte[] data, ReallocationPolicy policy, out int actualNumberOfSamplesRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref byte[] | An initialized 1D array of 8-bit unsigned integer samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-digitalsinglechannelreader-memoryoptimizedreadmultisampleportint32__int-ref-out.html language=enus -->
## TOPIC 02000: MemoryOptimizedReadMultiSamplePortInt32(int, ref int[], out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-digitalsinglechannelreader-memoryoptimizedreadmultisampleportint32__int-ref-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-digitalsinglechannelreader-memoryoptimizedreadmultisampleportint32__int-ref-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more 32-bit integer samples from a single DIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic int[] MemoryOptimizedReadMultiSamplePortInt32(int numberOfSamples, ref int[] data, out int actualNumberOfSamplesRead)RemarksIf the data buffer is large enough to hold the numb

### MemoryOptimizedReadMultiSamplePortInt32(int, ref int[], out int)

Reads one or more 32-bit integer samples from a single [DIChannel](nationalinstruments-daqmx-dichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int[] MemoryOptimizedReadMultiSamplePortInt32(int numberOfSamples, ref int[] data, out int actualNumberOfSamplesRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous digital input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref int[] | An initialized 1D array of 32-bit integer samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DigitalSingleChannelReader Class
