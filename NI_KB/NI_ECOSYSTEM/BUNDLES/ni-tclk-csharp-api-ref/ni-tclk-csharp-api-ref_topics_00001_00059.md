# NI DOCUMENT BUNDLE: ni-tclk-csharp-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-tclk-csharp-api-ref start=1 end=59 -->
<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-device.html language=enus -->
## TOPIC 00001: Device

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-device.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-device.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the ITClockSynchronizable device that the DeviceToSynchronize object represents. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic ITClockSynchronizableDevice Device { get; set; }RemarksAn ITClockSynchronizable object that represents the Modular

### Device

Gets or sets the ITClockSynchronizable device that the [DeviceToSynchronize](nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize.html) object represents.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public ITClockSynchronizableDevice Device { get; set; }

#### Remarks

An ITClockSynchronizable object that represents the Modular Instruments device connected to the system.

#### Exceptions

| Type | Description |
| --- | --- |
| System.InvalidOperationException | Valid ITClockSynchronizable device has not been passed. |

Parent topic:

DeviceToSynchronize Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-devicetosynchronize.html language=enus -->
## TOPIC 00002: DeviceToSynchronize()

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-devicetosynchronize.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-devicetosynchronize.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DeviceToSynchronize class. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic DeviceToSynchronize()

### DeviceToSynchronize()

Initializes a new instance of the [DeviceToSynchronize](nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize.html) class.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public DeviceToSynchronize()

Parent topic:

DeviceToSynchronize Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-devicetosynchronize__itclocksynchronizabledevice.html language=enus -->
## TOPIC 00003: DeviceToSynchronize(ITClockSynchronizableDevice)

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-devicetosynchronize__itclocksynchronizabledevice.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-devicetosynchronize__itclocksynchronizabledevice.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DeviceToSynchronize class with the specified ITClockSynchronizable device. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic DeviceToSynchronize(ITClockSynchronizableDevice device)ParametersNameTypeDescriptiondeviceITClockSy

### DeviceToSynchronize(ITClockSynchronizableDevice)

Initializes a new instance of the [DeviceToSynchronize](nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize.html) class with the specified ITClockSynchronizable device.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public DeviceToSynchronize(ITClockSynchronizableDevice device)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| device | ITClockSynchronizableDevice | Specifies an ITClockSynchronizable device. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentNullException | Thrown when the device object is null. |

Parent topic:

DeviceToSynchronize Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-exportedsyncpulseoutputterminal.html language=enus -->
## TOPIC 00004: ExportedSyncPulseOutputTerminal

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-exportedsyncpulseoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-exportedsyncpulseoutputterminal.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the destination of the sync pulse. Typically used in a multi-chassis system. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic string ExportedSyncPulseOutputTerminal { get; set; }RemarksValid values are as follows: An empty string, indicating th

### ExportedSyncPulseOutputTerminal

Gets or sets the destination of the sync pulse. Typically used in a multi-chassis system.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public string ExportedSyncPulseOutputTerminal { get; set; }

#### Remarks

Valid values are as follows:

- An empty string, indicating that the signal is not exported.
- For PXI devices, "<tt>PXI_Trig0</tt>" through "<tt>PXI_Trig7</tt>" and device-specific settings.
- For PCI devices, "<tt>RTSI_0</tt>" through "<tt>RTSI_7</tt>" and device-specific settings.

The default value is an empty string.

Examples of device-specific settings:

- NI PXI-5122 supports "<tt>PFI0</tt>" and "<tt>PFI1</tt>".
- NI PXI-5421 supports "<tt>PFI0</tt>", "<tt>PFI1</tt>", "<tt>PFI4</tt>", and "<tt>PFI5</tt>".
- NI PXI-6551/6552 supports "<tt>PFI0</tt>", "<tt>PFI1</tt>", "<tt>PFI2</tt>", and "<tt>PFI3</tt>".

#### Exceptions

| Type | Description |
| --- | --- |
| System.InvalidOperationException | The DeviceToSynchronize object does not belong to a TClock object. |
| System.InvalidOperationException | Cannot access the property before the session is opened. |
| System.ObjectDisposedException | The ITClockSynchronizable object that is contained in the DeviceToSynchronize object has been disposed. |
| System.ArgumentNullException | The value being set on the property is null. |
| NationalInstruments.ModularInstruments.ModularInstrumentsException | The underlying driver returned an error. |

Parent topic:

DeviceToSynchronize Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-exportedtclkoutputterminal.html language=enus -->
## TOPIC 00005: ExportedTClkOutputTerminal

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-exportedtclkoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-exportedtclkoutputterminal.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the destination for the TClk signal of the device. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic string ExportedTClkOutputTerminal { get; set; }RemarksSpecifies a String representing the destination for the TClk signal of the device.

### ExportedTClkOutputTerminal

Gets or sets the destination for the TClk signal of the device.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public string ExportedTClkOutputTerminal { get; set; }

#### Remarks

Specifies a String representing the destination for the TClk signal of the device.

Parent topic:

DeviceToSynchronize Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-exportedtclockoutputterminal.html language=enus -->
## TOPIC 00006: ExportedTClockOutputTerminal

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-exportedtclockoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-exportedtclockoutputterminal.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the destination for the TClk signal of the device. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic string ExportedTClockOutputTerminal { get; set; }RemarksSpecifies a String representing the destination for the TClk signal of the device.

### ExportedTClockOutputTerminal

Gets or sets the destination for the TClk signal of the device.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public string ExportedTClockOutputTerminal { get; set; }

#### Remarks

Specifies a String representing the destination for the TClk signal of the device.

Parent topic:

DeviceToSynchronize Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-getscripttriggermaster__string.html language=enus -->
## TOPIC 00007: GetScriptTriggerMaster(string)

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-getscripttriggermaster__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-getscripttriggermaster__string.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the script trigger master session. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic ITClockSynchronizableDevice GetScriptTriggerMaster(string channelName)RemarksReturns an ITClockSynchronizable object that represents a modular instrument connected to t

### GetScriptTriggerMaster(string)

Gets the script trigger master session.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public ITClockSynchronizableDevice GetScriptTriggerMaster(string channelName)

#### Remarks

Returns an ITClockSynchronizable object that represents a modular instrument connected to the system.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelName | string | Valid values for the channelName are "<tt>scriptTrigger0</tt>", "<tt>scriptTrigger1</tt>", "<tt>scriptTrigger2</tt>", and "<tt>scriptTrigger3</tt>". An empty string is treated as "<tt>scriptTrigger0</tt>". |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentNullException | channelName cannot be null. |
| System.InvalidOperationException | The DeviceToSynchronize object does not belong to a TClock object. |
| System.ObjectDisposedException | The ITClockSynchronizable object that is contained in the DeviceToSynchronize object has been disposed. |
| System.InvalidOperationException | Cannot call this method before the session is opened. |
| NationalInstruments.ModularInstruments.ModularInstrumentsException | The underlying driver returned an error. |

Parent topic:

DeviceToSynchronize Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-gettclkactualperiod.html language=enus -->
## TOPIC 00008: GetTClkActualPeriod

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-gettclkactualperiod.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-gettclkactualperiod.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the computed TClk period. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic double GetTClkActualPeriod { get; }RemarksReturns a Double representing the computed TClk period.

### GetTClkActualPeriod

Gets the computed TClk period.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public double GetTClkActualPeriod { get; }

#### Remarks

Returns a Double representing the computed TClk period.

Parent topic:

DeviceToSynchronize Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-pausetriggermaster.html language=enus -->
## TOPIC 00009: PauseTriggerMaster

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-pausetriggermaster.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-pausetriggermaster.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the pause trigger master session. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic ITClockSynchronizableDevice PauseTriggerMaster { get; set; }RemarksAn ITClockSynchronizable object that represents a modular instrument connected to the system.

### PauseTriggerMaster

Gets or sets the pause trigger master session.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public ITClockSynchronizableDevice PauseTriggerMaster { get; set; }

#### Remarks

An ITClockSynchronizable object that represents a modular instrument connected to the system.

#### Exceptions

| Type | Description |
| --- | --- |
| System.InvalidOperationException | The DeviceToSynchronize object does not belong to a TClock object. |
| System.ObjectDisposedException | The ITClockSynchronizable object that is contained in the DeviceToSynchronize object has been disposed. |
| NationalInstruments.ModularInstruments.ModularInstrumentsException | The underlying driver returned an error. |
| System.ArgumentNullException | The value being set on the property is null. |
| System.InvalidOperationException | Cannot access the property before the session is opened. |

Parent topic:

DeviceToSynchronize Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-referencetriggermaster.html language=enus -->
## TOPIC 00010: ReferenceTriggerMaster

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-referencetriggermaster.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-referencetriggermaster.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the reference trigger master session. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic ITClockSynchronizableDevice ReferenceTriggerMaster { get; set; }RemarksAn ITClockSynchronizable object that represents a modular instrument connected to the

### ReferenceTriggerMaster

Gets or sets the reference trigger master session.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public ITClockSynchronizableDevice ReferenceTriggerMaster { get; set; }

#### Remarks

An ITClockSynchronizable object that represents a modular instrument connected to the system.

For external triggers, the master session is the session configured to receive an external trigger. If no trigger is configured or using software triggers, the master session is the session that generates the trigger.

#### Exceptions

| Type | Description |
| --- | --- |
| System.InvalidOperationException | The DeviceToSynchronize object does not belong to a TClock object. |
| System.ObjectDisposedException | The ITClockSynchronizable object that is contained in the DeviceToSynchronize object has been disposed. |
| NationalInstruments.ModularInstruments.ModularInstrumentsException | The underlying driver returned an error. |
| System.ArgumentNullException | The value being set on the property is null. |
| System.InvalidOperationException | Cannot access the property before the session is opened. |

Parent topic:

DeviceToSynchronize Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-sampleclockdelay.html language=enus -->
## TOPIC 00011: SampleClockDelay

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-sampleclockdelay.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-sampleclockdelay.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the delay, in seconds. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic double SampleClockDelay { get; set; }RemarksThis delay is applied to the session sample clock relative to the other synchronized sessions. During synchronization, the drive

### SampleClockDelay

Gets or sets the delay, in seconds.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public double SampleClockDelay { get; set; }

#### Remarks

This delay is applied to the session sample clock relative to the other synchronized sessions. During synchronization, the driver aligns the sample clocks on the synchronized devices. To delay the sample clocks, set this attribute before calling [Synchronize](nationalinstruments-modularinstruments-systemservices-timingservices-tclock-synchronize.html).

Between minus one and plus one period of the sample clock.

One sample clock period is equal to (1/*Sample Clock Rate*). For example, for a session with sample rate of 100 MS/s, you can specify sample clock delays between -10.0 ns and +10.0 ns.

The default value is 0.

#### Exceptions

| Type | Description |
| --- | --- |
| System.InvalidOperationException | The DeviceToSynchronize object does not belong to a TClock object. |
| System.ObjectDisposedException | The ITClockSynchronizable object that is contained in the DeviceToSynchronize object has been disposed. |
| System.InvalidOperationException | Cannot access the property before the session is opened. |
| NationalInstruments.ModularInstruments.ModularInstrumentsException | The underlying driver returned an error. |

Parent topic:

DeviceToSynchronize Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-sequencerflagmaster.html language=enus -->
## TOPIC 00012: SequencerFlagMaster

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-sequencerflagmaster.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-sequencerflagmaster.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the sequencer flag master session. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic ITClockSynchronizableDevice SequencerFlagMaster { get; set; }RemarksAn ITClockSynchronizable object that represents a modular instrument connected to the system

### SequencerFlagMaster

Gets or sets the sequencer flag master session.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public ITClockSynchronizableDevice SequencerFlagMaster { get; set; }

#### Remarks

An ITClockSynchronizable object that represents a modular instrument connected to the system.

#### Exceptions

| Type | Description |
| --- | --- |
| System.InvalidOperationException | The DeviceToSynchronize object does not belong to a TClock object. |
| System.ObjectDisposedException | The ITClockSynchronizable object that is contained in the DeviceToSynchronize object has been disposed. |
| NationalInstruments.ModularInstruments.ModularInstrumentsException | The underlying driver returned an error. |
| System.ArgumentNullException | The value being set on the property is null. |
| System.InvalidOperationException | Cannot access the property before the session is opened. |

Parent topic:

DeviceToSynchronize Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-setscripttriggermaster__string-itclocksynchronizabledevice.html language=enus -->
## TOPIC 00013: SetScriptTriggerMaster(string, ITClockSynchronizableDevice)

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-setscripttriggermaster__string-itclocksynchronizabledevice.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-setscripttriggermaster__string-itclocksynchronizabledevice.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the script trigger master session. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic void SetScriptTriggerMaster(string channelName, ITClockSynchronizableDevice scriptTriggerMaster)ParametersNameTypeDescriptionchannelNamestringValid values for the chann

### SetScriptTriggerMaster(string, ITClockSynchronizableDevice)

Sets the script trigger master session.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public void SetScriptTriggerMaster(string channelName, ITClockSynchronizableDevice scriptTriggerMaster)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelName | string | Valid values for the channelName are "<tt>scriptTrigger0</tt>", "<tt>scriptTrigger1</tt>", "<tt>scriptTrigger2</tt>", and "<tt>scriptTrigger3</tt>". An empty string is treated as "<tt>scriptTrigger0</tt>". |
| scriptTriggerMaster | ITClockSynchronizableDevice | An ITClockSynchronizable object that represents a modular instrument connected to the system. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.InvalidOperationException | The DeviceToSynchronize object does not belong to a TClock object. |
| System.ObjectDisposedException | The ITClockSynchronizable object that is contained in the DeviceToSynchronize object has been disposed. |
| NationalInstruments.ModularInstruments.ModularInstrumentsException | The underlying driver returned an error. |
| System.ArgumentNullException | The value being set on the property is null. |

Parent topic:

DeviceToSynchronize Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-starttriggermaster.html language=enus -->
## TOPIC 00014: StartTriggerMaster

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-starttriggermaster.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-starttriggermaster.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the start trigger master session. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic ITClockSynchronizableDevice StartTriggerMaster { get; set; }RemarksAn ITClockSynchronizable object that represents a modular instrument connected to the system.

### StartTriggerMaster

Gets or sets the start trigger master session.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public ITClockSynchronizableDevice StartTriggerMaster { get; set; }

#### Remarks

An ITClockSynchronizable object that represents a modular instrument connected to the system.

#### Exceptions

| Type | Description |
| --- | --- |
| System.InvalidOperationException | The DeviceToSynchronize object does not belong to a TClock object. |
| System.ObjectDisposedException | The ITClockSynchronizable object that is contained in the DeviceToSynchronize object has been disposed. |
| NationalInstruments.ModularInstruments.ModularInstrumentsException | The underlying driver returned an error. |
| System.ArgumentNullException | The value being set on the property is null. |
| System.InvalidOperationException | Cannot access the property before the session is opened. |

Parent topic:

DeviceToSynchronize Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-syncpulseclocksource.html language=enus -->
## TOPIC 00015: SyncPulseClockSource

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-syncpulseclocksource.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-syncpulseclocksource.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the sync pulse clock source. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic string SyncPulseClockSource { get; set; }RemarksThis attribute is typically used to synchronize PCI devices when you want to control RTSI 7 yourself. Make sure that a

### SyncPulseClockSource

Gets or sets the sync pulse clock source.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public string SyncPulseClockSource { get; set; }

#### Remarks

This attribute is typically used to synchronize PCI devices when you want to control RTSI 7 yourself. Make sure that a 10 MHz clock is driven onto RTSI 7.

Valid values are as follows:

- For PXI devices, "<tt>PXI_CLK10</tt>" and "<tt>None</tt>".
- For PCI devices, "<tt>RTSI_7</tt>" and "<tt>None</tt>".

"<tt>None</tt>" directs the [Synchronize](nationalinstruments-modularinstruments-systemservices-timingservices-tclock-synchronize.html) method to create the necessary routes. For PCI, one of the synchronized devices drives a 10 MHz clock on RTSI_7 unless that line is already being driven.

#### Exceptions

| Type | Description |
| --- | --- |
| System.InvalidOperationException | The DeviceToSynchronize object does not belong to a TClock object. |
| System.ObjectDisposedException | The ITClockSynchronizable object that is contained in the DeviceToSynchronize object has been disposed. |
| System.ArgumentNullException | The value being set on the property is null. |
| System.InvalidOperationException | Cannot access the property before the session is opened. |
| NationalInstruments.ModularInstruments.ModularInstrumentsException | The underlying driver returned an error. |

Parent topic:

DeviceToSynchronize Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-syncpulsesendersyncpulsesource.html language=enus -->
## TOPIC 00016: SyncPulseSenderSyncPulseSource

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-syncpulsesendersyncpulsesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-syncpulsesendersyncpulsesource.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the the external sync pulse source of the sync pulse sender. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic string SyncPulseSenderSyncPulseSource { get; set; }RemarksYou can use this source to synchronize the sync pulse sender with an externa

### SyncPulseSenderSyncPulseSource

Gets or sets the the external sync pulse source of the sync pulse sender.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public string SyncPulseSenderSyncPulseSource { get; set; }

#### Remarks

You can use this source to synchronize the sync pulse sender with an external non-TClk event.

Valid values are as follows:

- For PXI devices, "<tt>PXI_Trig0</tt>" through "<tt>PXI_Trig7</tt>" and device-specific settings.
- For PCI devices, "<tt>RTSI_0</tt>" through "<tt>RTSI_7</tt>" and device-specific settings.

The default value is an empty string. An empty string indicates that the signal is not exported.

Parent topic:

DeviceToSynchronize Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-syncpulsesource.html language=enus -->
## TOPIC 00017: SyncPulseSource

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-syncpulsesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-syncpulsesource.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the sync pulse source. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic string SyncPulseSource { get; set; }RemarksThis attribute is most often used when synchronizing a multi-chassis system. Valid values are as follows: An empty string. For PX

### SyncPulseSource

Gets or sets the sync pulse source.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public string SyncPulseSource { get; set; }

#### Remarks

This attribute is most often used when synchronizing a multi-chassis system.

Valid values are as follows:

1. An empty string.
2. For PXI devices, "<tt>PXI_Trig0</tt>" through "<tt>PXI_Trig7</tt>" and device-specific settings.
3. For PCI devices, "<tt>RTSI_0</tt>" through "<tt>RTSI_7</tt>" and device-specific settings.

The default value is an empty string. This default value directs the [Synchronize](nationalinstruments-modularinstruments-systemservices-timingservices-tclock-synchronize.html) method to set this attribute when all the synchronized devices are in one PXI chassis. To synchronize a multi-chassis system, you must set this attribute before calling [Synchronize](nationalinstruments-modularinstruments-systemservices-timingservices-tclock-synchronize.html).

**Examples of device-specific settings:**

- NI PXI-5122 supports "<tt>PFI0</tt>" and "<tt>PFI1</tt>"
- NI PXI-5421 supports "<tt>PFI0</tt>", "<tt>PFI1</tt>", "<tt>PFI2</tt>", and "<tt>PFI3</tt>"
- NI PXI-6551/6552 supports "<tt>PFI0</tt>", "<tt>PFI1</tt>", "<tt>PFI2</tt>", and "<tt>PFI3</tt>"

#### Exceptions

| Type | Description |
| --- | --- |
| System.InvalidOperationException | The DeviceToSynchronize object does not belong to a TClock object. |
| System.ObjectDisposedException | The ITClockSynchronizable object that is contained in the DeviceToSynchronize object has been disposed. |
| System.ArgumentNullException | The value being set on the property is null. |
| System.InvalidOperationException | Cannot access the property before the session is opened. |
| NationalInstruments.ModularInstruments.ModularInstrumentsException | The underlying driver returned an error. |

Parent topic:

DeviceToSynchronize Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-tclockactualperiod.html language=enus -->
## TOPIC 00018: TClockActualPeriod

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-tclockactualperiod.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-tclockactualperiod.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the computed TClk period. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic double TClockActualPeriod { get; }RemarksReturns a Double representing the computed TClk period.

### TClockActualPeriod

Gets the computed TClk period.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public double TClockActualPeriod { get; }

#### Remarks

Returns a Double representing the computed TClk period.

Parent topic:

DeviceToSynchronize Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize.html language=enus -->
## TOPIC 00019: DeviceToSynchronize Class

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a modular instruments device that can be synchronized. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic class DeviceToSynchronizeRemarksContains properties to synchronize modular instruments devices. Thread SafetyAll members of th

### DeviceToSynchronize Class

Represents a modular instruments device that can be synchronized.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public class DeviceToSynchronize

#### Remarks

Contains properties to synchronize modular instruments devices.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| DeviceToSynchronize(ITClockSynchronizableDevice) | Initializes a new instance of the DeviceToSynchronize class with the specified ITClockSynchronizable device. |
| DeviceToSynchronize() | Initializes a new instance of the DeviceToSynchronize class. |

#### Properties

| Name | Description |
| --- | --- |
| Device | Gets or sets the ITClockSynchronizable device that the DeviceToSynchronize object represents. |
| ExportedSyncPulseOutputTerminal | Gets or sets the destination of the sync pulse. Typically used in a multi-chassis system. |
| ExportedTClkOutputTerminal | Gets or sets the destination for the TClk signal of the device. |
| ExportedTClockOutputTerminal | Gets or sets the destination for the TClk signal of the device. |
| GetTClkActualPeriod | Gets the computed TClk period. |
| PauseTriggerMaster | Gets or sets the pause trigger master session. |
| ReferenceTriggerMaster | Gets or sets the reference trigger master session. |
| SampleClockDelay | Gets or sets the delay, in seconds. |
| SequencerFlagMaster | Gets or sets the sequencer flag master session. |
| StartTriggerMaster | Gets or sets the start trigger master session. |
| SyncPulseClockSource | Gets or sets the sync pulse clock source. |
| SyncPulseSenderSyncPulseSource | Gets or sets the the external sync pulse source of the sync pulse sender. |
| SyncPulseSource | Gets or sets the sync pulse source. |
| TClockActualPeriod | Gets the computed TClk period. |

#### Methods

| Name | Description |
| --- | --- |
| GetScriptTriggerMaster(string) | Gets the script trigger master session. |
| SetScriptTriggerMaster(string, ITClockSynchronizableDevice) | Sets the script trigger master session. |

Parent topic:

NationalInstruments.ModularInstruments.SystemServices.TimingServices

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclock-advanced.html language=enus -->
## TOPIC 00020: Advanced

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclock-advanced.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclock-advanced.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an instance of TClockAdvanced. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic TClockAdvanced Advanced { get; }RemarksAn instance of TClockAdvanced.

### Advanced

Gets an instance of [TClockAdvanced](nationalinstruments-modularinstruments-systemservices-timingservices-tclockadvanced.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public [TClockAdvanced](nationalinstruments-modularinstruments-systemservices-timingservices-tclockadvanced.html) Advanced { get; }

#### Remarks

An instance of [TClockAdvanced](nationalinstruments-modularinstruments-systemservices-timingservices-tclockadvanced.html).

Parent topic:

TClock Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclock-configureforhomogeneoustriggers.html language=enus -->
## TOPIC 00021: ConfigureForHomogeneousTriggers()

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclock-configureforhomogeneoustriggers.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclock-configureforhomogeneoustriggers.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the properties required for the synchronization of device sessions with homogeneous triggers in a single PXI chassis or a single PC. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic void ConfigureForHomogeneousTriggers()RemarksFor more informatio

### ConfigureForHomogeneousTriggers()

Configures the properties required for the synchronization of device sessions with homogeneous triggers in a single PXI chassis or a single PC.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public void ConfigureForHomogeneousTriggers()

#### Remarks

For more information about how this method affects clocks and triggers, refer to the *NI-TClk Synchronization Help*.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.ModularInstruments.ModularInstrumentsException | The underlying driver returned an error. |

Parent topic:

TClock Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclock-devicestosynchronize.html language=enus -->
## TOPIC 00022: DevicesToSynchronize

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclock-devicestosynchronize.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclock-devicestosynchronize.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the TClockSynchronizableDevicesCollection held by the TClock object. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic TClockSynchronizableDevicesCollection DevicesToSynchronize { get; }RemarksThe TClockSynchronizableDevicesCollection collection held by

### DevicesToSynchronize

Gets the [TClockSynchronizableDevicesCollection](nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection.html) held by the [TClock](nationalinstruments-modularinstruments-systemservices-timingservices-tclock.html) object.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public [TClockSynchronizableDevicesCollection](nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection.html) DevicesToSynchronize { get; }

#### Remarks

The [TClockSynchronizableDevicesCollection](nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection.html) collection held by the [TClock](nationalinstruments-modularinstruments-systemservices-timingservices-tclock.html) object.

Parent topic:

TClock Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclock-initiate.html language=enus -->
## TOPIC 00023: Initiate()

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclock-initiate.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclock-initiate.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates the specified acquisition or generation sessions. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic void Initiate()RemarksThis method also processes any special requirements for synchronization. For example, the session that exports the TClock-sync

### Initiate()

Initiates the specified acquisition or generation sessions.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public void Initiate()

#### Remarks

This method also processes any special requirements for synchronization. For example, the session that exports the [TClock](nationalinstruments-modularinstruments-systemservices-timingservices-tclock.html)-synchronized start trigger is not initiated until the Initiate method initiates all the sessions that import the [TClock](nationalinstruments-modularinstruments-systemservices-timingservices-tclock.html)-synchronized start trigger.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.ModularInstruments.ModularInstrumentsException | The underlying driver returned an error. |

Parent topic:

TClock Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclock-isdone.html language=enus -->
## TOPIC 00024: IsDone

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclock-isdone.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclock-isdone.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating whether the operations initiated by Initiate on the modular instrument(s) are complete. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic bool IsDone { get; }Remarkstrue if the operations initiated by Initiate on the modular instrumen

### IsDone

Gets a value indicating whether the operations initiated by [Initiate](nationalinstruments-modularinstruments-systemservices-timingservices-tclock-initiate.html) on the modular instrument(s) are complete.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public bool IsDone { get; }

#### Remarks

true if the operations initiated by [Initiate](nationalinstruments-modularinstruments-systemservices-timingservices-tclock-initiate.html) on the modular instrument(s) are complete; otherwise, false.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.ModularInstruments.ModularInstrumentsException | The underlying driver returned an error. |

Parent topic:

TClock Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclock-synchronize.html language=enus -->
## TOPIC 00025: Synchronize()

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclock-synchronize.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclock-synchronize.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Synchronizes the TClk signals on the given sessions. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic void Synchronize()RemarksAfter the Synchronize method executes, TClk signals from all sessions are synchronized. For more information, refer to the NI-TClk

### Synchronize()

Synchronizes the TClk signals on the given sessions.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public void Synchronize()

#### Remarks

After the Synchronize method executes, TClk signals from all sessions are synchronized. For more information, refer to the *NI-TClk Synchronization Help*.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.ModularInstruments.ModularInstrumentsException | The underlying driver returned an error. |

Parent topic:

TClock Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclock-synchronize__precisiontimespan.html language=enus -->
## TOPIC 00026: Synchronize(PrecisionTimeSpan)

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclock-synchronize__precisiontimespan.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclock-synchronize__precisiontimespan.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Synchronizes the TClk signals on the given sessions. After Synchronize executes, TClk signals from all sessions are synchronized. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic void Synchronize(PrecisionTimeSpan minTime)Remarks<Scopetag> For more informat

### Synchronize(PrecisionTimeSpan)

Synchronizes the TClk signals on the given sessions. After [Synchronize](nationalinstruments-modularinstruments-systemservices-timingservices-tclock-synchronize.html) executes, TClk signals from all sessions are synchronized.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public void Synchronize(PrecisionTimeSpan minTime)

#### Remarks

<Scopetag> For more information, refer to the *NI-TClk Synchronization Help*. </Scopetag>

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| minTime | PrecisionTimeSpan | Minimal period of TClk, expressed in seconds. Supported values are between 0.0 s and 0.050 s (50 ms). Minimal period for a single chassis/PC is 200 ns. If the specified value is less than 200 ns, the driver automatically coerces minTime to 200 ns. For multi-chassis synchronization, adjust this value to account for propagation delays through the various devices and cables. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.ModularInstruments.ModularInstrumentsException | The underlying driver returned an error. |

Parent topic:

TClock Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclock-tclock.html language=enus -->
## TOPIC 00027: TClock()

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclock-tclock.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclock-tclock.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the TClock class. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic TClock()

### TClock()

Initializes a new instance of the [TClock](nationalinstruments-modularinstruments-systemservices-timingservices-tclock.html) class.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public TClock()

Parent topic:

TClock Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclock-tclock__params.html language=enus -->
## TOPIC 00028: TClock(params ITClockSynchronizableDevice[])

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclock-tclock__params.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclock-tclock__params.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the TClock class. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic TClock(params ITClockSynchronizableDevice[] devices)RemarksInitializes a new instance of the TClock class with the specified ITClockSynchronizableDevice collect

### TClock(params ITClockSynchronizableDevice[])

Initializes a new instance of the [TClock](nationalinstruments-modularinstruments-systemservices-timingservices-tclock.html) class.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public TClock(params ITClockSynchronizableDevice[] devices)

#### Remarks

Initializes a new instance of the [TClock](nationalinstruments-modularinstruments-systemservices-timingservices-tclock.html) class with the specified ITClockSynchronizableDevice collection.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| devices | params ITClockSynchronizableDevice[] | An array of ITClockSynchronizableDevice objects. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentNullException | Thrown when the devices object is null. |

Parent topic:

TClock Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclock-waituntildone__precisiontimespan.html language=enus -->
## TOPIC 00029: WaitUntilDone(PrecisionTimeSpan)

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclock-waituntildone__precisiontimespan.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclock-waituntildone__precisiontimespan.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Delays the execution of your program until the acquisitions and generations corresponding to sessions are complete, or until the method returns a timeout error. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic void WaitUntilDone(PrecisionTimeSpan timeout)Re

### WaitUntilDone(PrecisionTimeSpan)

Delays the execution of your program until the acquisitions and generations corresponding to sessions are complete, or until the method returns a timeout error.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public void WaitUntilDone(PrecisionTimeSpan timeout)

#### Remarks

<Scopetag> For more information, refer to the *NI-TClk Synchronization Help*. </Scopetag>

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| timeout | PrecisionTimeSpan | Specifies the amount of time, in seconds, that the WaitUntilDone method waits for the sessions to complete. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.ModularInstruments.ModularInstrumentsException | The underlying driver returned an error. |

Parent topic:

TClock Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclock.html language=enus -->
## TOPIC 00030: TClock Class

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclock.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclock.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the component that is used to synchronize modular instruments. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic class TClockRemarksThe TClock object holds a TClockSynchronizableDevicesCollection. Each item in the collection is a D

### TClock Class

Represents the component that is used to synchronize modular instruments.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public class TClock

#### Remarks

The TClock object holds a [TClockSynchronizableDevicesCollection](nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection.html). Each item in the collection is a [DeviceToSynchronize](nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize.html) object. The [DeviceToSynchronize](nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize.html) object represents an ITClockSynchronizableDevice. This ITClockSynchronizableDevice is a Modular Instruments device that can be synchronized by TClk technology.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| TClock(params ITClockSynchronizableDevice[]) | Initializes a new instance of the TClock class. |
| TClock() | Initializes a new instance of the TClock class. |

#### Properties

| Name | Description |
| --- | --- |
| Advanced | Gets an instance of TClockAdvanced. |
| DevicesToSynchronize | Gets the TClockSynchronizableDevicesCollection held by the TClock object. |
| IsDone | Gets a value indicating whether the operations initiated by Initiate on the modular instrument(s) are complete. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureForHomogeneousTriggers() | Configures the properties required for the synchronization of device sessions with homogeneous triggers in a single PXI chassis or a single PC. |
| Initiate() | Initiates the specified acquisition or generation sessions. |
| Synchronize(PrecisionTimeSpan) | Synchronizes the TClk signals on the given sessions. After Synchronize executes, TClk signals from all sessions are synchronized. |
| Synchronize() | Synchronizes the TClk signals on the given sessions. |
| WaitUntilDone(PrecisionTimeSpan) | Delays the execution of your program until the acquisitions and generations corresponding to sessions are complete, or until the method returns a timeout error. |

Parent topic:

NationalInstruments.ModularInstruments.SystemServices.TimingServices

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclockadvanced-finishsyncpulsesendersynchronize__double.html language=enus -->
## TOPIC 00031: FinishSyncPulseSenderSynchronize(double)

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclockadvanced-finishsyncpulsesendersynchronize__double.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclockadvanced-finishsyncpulsesendersynchronize__double.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Finishes synchronizing the device responsible for sending sync pulses, as determined automatically by NI-TClk or manually when you set the SyncPulseSenderSyncPulseSource property for a specific device. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic void F

### FinishSyncPulseSenderSynchronize(double)

Finishes synchronizing the device responsible for sending sync pulses, as determined automatically by NI-TClk or manually when you set the [SyncPulseSenderSyncPulseSource](nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-syncpulsesendersyncpulsesource.html) property for a specific device.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public void FinishSyncPulseSenderSynchronize(double minTime)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| minTime | double | Specifies the minimal TClk period, in seconds, for the TClock object to perform synchronization. Supported values are between 0.0 and 0.050 s. |

Parent topic:

TClockAdvanced Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclockadvanced-finishsyncpulsesendersynchronize__precisiontimespan.html language=enus -->
## TOPIC 00032: FinishSyncPulseSenderSynchronize(PrecisionTimeSpan)

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclockadvanced-finishsyncpulsesendersynchronize__precisiontimespan.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclockadvanced-finishsyncpulsesendersynchronize__precisiontimespan.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Finishes synchronizing the device responsible for sending sync pulses, as determined automatically by NI-TClk or manually when you set the SyncPulseSenderSyncPulseSource property for a specific device. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic void F

### FinishSyncPulseSenderSynchronize(PrecisionTimeSpan)

Finishes synchronizing the device responsible for sending sync pulses, as determined automatically by NI-TClk or manually when you set the [SyncPulseSenderSyncPulseSource](nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-syncpulsesendersyncpulsesource.html) property for a specific device.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public void FinishSyncPulseSenderSynchronize(PrecisionTimeSpan minTime)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| minTime | PrecisionTimeSpan | Specifies the minimal TClk period, in seconds, for the TClock object to perform synchronization. Supported values are between 0.0 and 0.050 s. |

Parent topic:

TClockAdvanced Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclockadvanced-setupforsyncpulsesendersynchronize__double.html language=enus -->
## TOPIC 00033: SetupForSyncPulseSenderSynchronize(double)

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclockadvanced-setupforsyncpulsesendersynchronize__double.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclockadvanced-setupforsyncpulsesendersynchronize__double.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the TClks on all devices and prepares a device, chosen either automatically by NI-TClk or manually when you set the SyncPulseSenderSyncPulseSource property for a specific device, to send sync pulses to devices in the synchronization group. SyntaxNamespace: NationalInstruments.ModularInstr

### SetupForSyncPulseSenderSynchronize(double)

Configures the TClks on all devices and prepares a device, chosen either automatically by NI-TClk or manually when you set the [SyncPulseSenderSyncPulseSource](nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-syncpulsesendersyncpulsesource.html) property for a specific device, to send sync pulses to devices in the synchronization group.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public void SetupForSyncPulseSenderSynchronize(double minTime)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| minTime | double | Specifies the minimal TClk period, in seconds, for the TClock object to perform synchronization. Supported values are between 0.0 and 0.050 s. |

Parent topic:

TClockAdvanced Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclockadvanced-setupforsyncpulsesendersynchronize__precisiontimespan.html language=enus -->
## TOPIC 00034: SetupForSyncPulseSenderSynchronize(PrecisionTimeSpan)

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclockadvanced-setupforsyncpulsesendersynchronize__precisiontimespan.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclockadvanced-setupforsyncpulsesendersynchronize__precisiontimespan.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the TClks on all devices and prepares a device, chosen either automatically by NI-TClk or manually when you set the SyncPulseSenderSyncPulseSource property for a specific device, to send sync pulses to devices in the synchronization group. SyntaxNamespace: NationalInstruments.ModularInstr

### SetupForSyncPulseSenderSynchronize(PrecisionTimeSpan)

Configures the TClks on all devices and prepares a device, chosen either automatically by NI-TClk or manually when you set the [SyncPulseSenderSyncPulseSource](nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-syncpulsesendersyncpulsesource.html) property for a specific device, to send sync pulses to devices in the synchronization group.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public void SetupForSyncPulseSenderSynchronize(PrecisionTimeSpan minTime)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| minTime | PrecisionTimeSpan | Specifies the minimal TClk period, in seconds, for the TClock object to perform synchronization. Supported values are between 0.0 and 0.050 s. |

Parent topic:

TClockAdvanced Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclockadvanced-synchronizetosyncpulsesender__precisiontimespan.html language=enus -->
## TOPIC 00035: SynchronizeToSyncPulseSender(PrecisionTimeSpan)

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclockadvanced-synchronizetosyncpulsesender__precisiontimespan.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclockadvanced-synchronizetosyncpulsesender__precisiontimespan.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Synchronizes the other devices to the device responsible for sending sync pulses, as determined automatically by NI-TClk or manually when you set the SyncPulseSenderSyncPulseSource property for a specific device. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespu

### SynchronizeToSyncPulseSender(PrecisionTimeSpan)

Synchronizes the other devices to the device responsible for sending sync pulses, as determined automatically by NI-TClk or manually when you set the [SyncPulseSenderSyncPulseSource](nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize-syncpulsesendersyncpulsesource.html) property for a specific device.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public void SynchronizeToSyncPulseSender(PrecisionTimeSpan minTime)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| minTime | PrecisionTimeSpan | Specifies the minimal TClk period, in seconds, for the TClock object to perform synchronization. Supported values are between 0.0 and 0.050 s. |

Parent topic:

TClockAdvanced Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclockadvanced.html language=enus -->
## TOPIC 00036: TClockAdvanced Class

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclockadvanced.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclockadvanced.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides advanced functionality for NI-TClk. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic class TClockAdvancedRemarksThis object provides advanced functionality to initialize and synchronize modular instruments. Thread SafetyAny members

### TClockAdvanced Class

Provides advanced functionality for NI-TClk.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public class TClockAdvanced

#### Remarks

This object provides advanced functionality to initialize and synchronize modular instruments.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| FinishSyncPulseSenderSynchronize(PrecisionTimeSpan) | Finishes synchronizing the device responsible for sending sync pulses, as determined automatically by NI-TClk or manually when you set the SyncPulseSenderSyncPulseSource property for a specific device. |
| FinishSyncPulseSenderSynchronize(double) | Finishes synchronizing the device responsible for sending sync pulses, as determined automatically by NI-TClk or manually when you set the SyncPulseSenderSyncPulseSource property for a specific device. |
| SetupForSyncPulseSenderSynchronize(PrecisionTimeSpan) | Configures the TClks on all devices and prepares a device, chosen either automatically by NI-TClk or manually when you set the SyncPulseSenderSyncPulseSource property for a specific device, to send sync pulses to devices in the synchronization group. |
| SetupForSyncPulseSenderSynchronize(double) | Configures the TClks on all devices and prepares a device, chosen either automatically by NI-TClk or manually when you set the SyncPulseSenderSyncPulseSource property for a specific device, to send sync pulses to devices in the synchronization group. |
| SynchronizeToSyncPulseSender(PrecisionTimeSpan) | Synchronizes the other devices to the device responsible for sending sync pulses, as determined automatically by NI-TClk or manually when you set the SyncPulseSenderSyncPulseSource property for a specific device. |

#### See Also

- SyncPulseSenderSyncPulseSource
- SetupForSyncPulseSenderSynchronize
- FinishSyncPulseSenderSynchronize
- SynchronizeToSyncPulseSender

Parent topic:

NationalInstruments.ModularInstruments.SystemServices.TimingServices

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-add__devicetosynchronize.html language=enus -->
## TOPIC 00037: Add(DeviceToSynchronize)

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-add__devicetosynchronize.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-add__devicetosynchronize.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an item to the end of the collection. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic int Add(DeviceToSynchronize device)RemarksThe array index of the added item. ParametersNameTypeDescriptiondeviceDeviceToSynchronizeDeviceToSynchronize object to be a

### Add(DeviceToSynchronize)

Adds an item to the end of the collection.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public int Add(DeviceToSynchronize device)

#### Remarks

The array index of the added item.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| device | DeviceToSynchronize | DeviceToSynchronize object to be added to the collection. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentNullException | device value is null. |
| System.ArgumentException | device is already present in the collection. |

Parent topic:

TClockSynchronizableDevicesCollection Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-add__itclocksynchronizabledevice.html language=enus -->
## TOPIC 00038: Add(ITClockSynchronizableDevice)

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-add__itclocksynchronizabledevice.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-add__itclocksynchronizabledevice.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an item to the end of the collection. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic int Add(ITClockSynchronizableDevice device)RemarksThe array index of the added item. ParametersNameTypeDescriptiondeviceITClockSynchronizableDeviceITClockSynchroniza

### Add(ITClockSynchronizableDevice)

Adds an item to the end of the collection.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public int Add(ITClockSynchronizableDevice device)

#### Remarks

The array index of the added item.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| device | ITClockSynchronizableDevice | ITClockSynchronizableDevice object to be added to the collection. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentNullException | device value is null. |
| System.ArgumentException | device is already present in the collection. |

Parent topic:

TClockSynchronizableDevicesCollection Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-addrange__params.1.html language=enus -->
## TOPIC 00039: AddRange(params ITClockSynchronizableDevice[])

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-addrange__params.1.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-addrange__params.1.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an array of elements to the end of the collection. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic void AddRange(params ITClockSynchronizableDevice[] device)ParametersNameTypeDescriptiondeviceparams ITClockSynchronizableDevice[]Array of ITClockSynchro

### AddRange(params ITClockSynchronizableDevice[])

Adds an array of elements to the end of the collection.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public void AddRange(params ITClockSynchronizableDevice[] device)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| device | params ITClockSynchronizableDevice[] | Array of ITClockSynchronizableDevice objects to be added to the collection. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentNullException | device value is null. |
| System.ArgumentException | device is already present in the collection. |

Parent topic:

TClockSynchronizableDevicesCollection Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-addrange__params.html language=enus -->
## TOPIC 00040: AddRange(params DeviceToSynchronize[])

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-addrange__params.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-addrange__params.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an array of elements to the end of the collection. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic void AddRange(params DeviceToSynchronize[] device)ParametersNameTypeDescriptiondeviceparams DeviceToSynchronize[]Array of DeviceToSynchronize objects to

### AddRange(params DeviceToSynchronize[])

Adds an array of elements to the end of the collection.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public void AddRange(params DeviceToSynchronize[] device)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| device | params DeviceToSynchronize[] | Array of DeviceToSynchronize objects to be added to the collection. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentNullException | device value is null. |
| System.ArgumentException | device is already present in the collection. |

Parent topic:

TClockSynchronizableDevicesCollection Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-clear.html language=enus -->
## TOPIC 00041: Clear()

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-clear.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-clear.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes all items from the collection. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic void Clear()

### Clear()

Removes all items from the collection.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public void Clear()

Parent topic:

TClockSynchronizableDevicesCollection Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-collectionchanged.html language=enus -->
## TOPIC 00042: CollectionChanged

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-collectionchanged.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-collectionchanged.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Occurs when an item is added, removed, or updated. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic EventHandler CollectionChanged

### CollectionChanged

Occurs when an item is added, removed, or updated.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public EventHandler CollectionChanged

Parent topic:

TClockSynchronizableDevicesCollection Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-contains__devicetosynchronize.html language=enus -->
## TOPIC 00043: Contains(DeviceToSynchronize)

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-contains__devicetosynchronize.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-contains__devicetosynchronize.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether the specified element is in the collection. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic bool Contains(DeviceToSynchronize device)Remarkstrue if the collection contains device . ParametersNameTypeDescriptiondeviceDeviceToSynchronizeDevic

### Contains(DeviceToSynchronize)

Returns whether the specified element is in the collection.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public bool Contains(DeviceToSynchronize device)

#### Remarks

true if the collection contains *device* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| device | DeviceToSynchronize | DeviceToSynchronize object to be located in the collection. |

Parent topic:

TClockSynchronizableDevicesCollection Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-contains__itclocksynchronizabledevice.html language=enus -->
## TOPIC 00044: Contains(ITClockSynchronizableDevice)

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-contains__itclocksynchronizabledevice.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-contains__itclocksynchronizabledevice.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether the specified element is in the collection. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic bool Contains(ITClockSynchronizableDevice device)Remarkstrue if the collection contains device . ParametersNameTypeDescriptiondeviceITClockSynchroni

### Contains(ITClockSynchronizableDevice)

Returns whether the specified element is in the collection.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public bool Contains(ITClockSynchronizableDevice device)

#### Remarks

true if the collection contains *device* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| device | ITClockSynchronizableDevice | ITClockSynchronizableDevice object to be located in the collection. |

Parent topic:

TClockSynchronizableDevicesCollection Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-copyto__devicetosynchronize_arr1-int.html language=enus -->
## TOPIC 00045: CopyTo(DeviceToSynchronize[], int)

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-copyto__devicetosynchronize_arr1-int.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-copyto__devicetosynchronize_arr1-int.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Copies the collection to an array or a portion of an array. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic void CopyTo(DeviceToSynchronize[] destinationArray, int index)ParametersNameTypeDescriptiondestinationArrayDeviceToSynchronize[]Destination array fo

### CopyTo(DeviceToSynchronize[], int)

Copies the collection to an array or a portion of an array.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public void CopyTo(DeviceToSynchronize[] destinationArray, int index)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| destinationArray | DeviceToSynchronize[] | Destination array for the collection. |
| index | int | Index in the target array at which you want to begin copying the collection to. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentException | destinationArray is multidimensional. -or- index is greater than or equal to the array length. -or- The number of elements in the collection is greater than the available space between index and the end of destinationArray . |
| System.ArgumentNullException | destinationArray is null. |
| System.ArgumentOutOfRangeException | index is less than zero. |

Parent topic:

TClockSynchronizableDevicesCollection Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-count.html language=enus -->
## TOPIC 00046: Count

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-count.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-count.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of elements in the collection, which is equal to the number of NationalInstruments.ModularInstruments.ITClockSynchronizableDevice objects to be synchronized by TClk. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic int Count { get; }RemarksT

### Count

Gets the number of elements in the collection, which is equal to the number of NationalInstruments.ModularInstruments.ITClockSynchronizableDevice objects to be synchronized by TClk.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public int Count { get; }

#### Remarks

The number of elements contained in the collection, which is equal to the number of NationalInstruments.ModularInstruments.ITClockSynchronizableDevice objects to be synchronized by TClk.

Parent topic:

TClockSynchronizableDevicesCollection Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-equals__object.html language=enus -->
## TOPIC 00047: Equals(object)

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-equals__object.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns true if the specified object contains the same ITClockSynchronizableDevice devices as the current collection. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic override bool Equals(object obj)Remarkstrue if the collection contains the same ITClockSyn

### Equals(object)

Returns true if the specified object contains the same ITClockSynchronizableDevice devices as the current collection.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public override bool Equals(object obj)

#### Remarks

true if the collection contains the same ITClockSynchronizableDevice devices *obj*  parameter.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | Object to compare with the current collection. |

Parent topic:

TClockSynchronizableDevicesCollection Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-gethashcode.html language=enus -->
## TOPIC 00048: GetHashCode()

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-gethashcode.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a hash value that can be used to uniquely identify a particular TClockSynchronizableDevicesCollection object. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic override int GetHashCode()RemarksA hash value that uniquely identifies the TClockSynchro

### GetHashCode()

Generates a hash value that can be used to uniquely identify a particular [TClockSynchronizableDevicesCollection](nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection.html) object.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public override int GetHashCode()

#### Remarks

A hash value that uniquely identifies the [TClockSynchronizableDevicesCollection](nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection.html) object.

Parent topic:

TClockSynchronizableDevicesCollection Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-indexof__devicetosynchronize.html language=enus -->
## TOPIC 00049: IndexOf(DeviceToSynchronize)

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-indexof__devicetosynchronize.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-indexof__devicetosynchronize.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the zero-based index of the first occurrence of an item in the collection. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic int IndexOf(DeviceToSynchronize value)RemarksIndex of the item. If the item is not found, returns -1. ParametersNameTypeDescr

### IndexOf(DeviceToSynchronize)

Returns the zero-based index of the first occurrence of an item in the collection.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public int IndexOf(DeviceToSynchronize value)

#### Remarks

Index of the item. If the item is not found, returns -1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| value | DeviceToSynchronize | Item to search for. |

Parent topic:

TClockSynchronizableDevicesCollection Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-indexof__itclocksynchronizabledevice.html language=enus -->
## TOPIC 00050: IndexOf(ITClockSynchronizableDevice)

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-indexof__itclocksynchronizabledevice.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-indexof__itclocksynchronizabledevice.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the zero-based index of the first occurrence of an item in the collection. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic int IndexOf(ITClockSynchronizableDevice value)RemarksIndex of the item. If the item is not found, returns -1. ParametersNameT

### IndexOf(ITClockSynchronizableDevice)

Returns the zero-based index of the first occurrence of an item in the collection.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public int IndexOf(ITClockSynchronizableDevice value)

#### Remarks

Index of the item. If the item is not found, returns -1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| value | ITClockSynchronizableDevice | Item to search for. |

Parent topic:

TClockSynchronizableDevicesCollection Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-insert__int-devicetosynchronize.html language=enus -->
## TOPIC 00051: Insert(int, DeviceToSynchronize)

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-insert__int-devicetosynchronize.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-insert__int-devicetosynchronize.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inserts a DeviceToSynchronize object into the collection at the specified index. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic void Insert(int index, DeviceToSynchronize deviceToSynchronize)RemarksThe list elements after the inserted element shift down i

### Insert(int, DeviceToSynchronize)

Inserts a [DeviceToSynchronize](nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize.html) object into the collection at the specified index.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public void Insert(int index, DeviceToSynchronize deviceToSynchronize)

#### Remarks

The list elements after the inserted element shift down in the list. Because the list elements are indexed, the indexes of the shifted elements also are updated.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| index | int | Index at which to insert the item. |
| deviceToSynchronize | DeviceToSynchronize | DeviceToSynchronize object to insert into the collection. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentNullException | deviceToSynchronize is null. |
| System.ArgumentOutOfRangeException | index is not a valid index. |

Parent topic:

TClockSynchronizableDevicesCollection Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-insert__int-itclocksynchronizabledevice.html language=enus -->
## TOPIC 00052: Insert(int, ITClockSynchronizableDevice)

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-insert__int-itclocksynchronizabledevice.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-insert__int-itclocksynchronizabledevice.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inserts a NationalInstruments.ModularInstruments.ITClockSynchronizableDevice object into the collection at the specified index. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic void Insert(int index, ITClockSynchronizableDevice device)RemarksThe list elemen

### Insert(int, ITClockSynchronizableDevice)

Inserts a NationalInstruments.ModularInstruments.ITClockSynchronizableDevice object into the collection at the specified index.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public void Insert(int index, ITClockSynchronizableDevice device)

#### Remarks

The list elements after the inserted element shift down in the list. Because the list elements are indexed, the indexes of the shifted elements also are updated.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| index | int | Index to insert the item at. |
| device | ITClockSynchronizableDevice | NationalInstruments.ModularInstruments.ITClockSynchronizableDevice object to insert into the collection. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentNullException | device is null. |
| System.ArgumentOutOfRangeException | index is not a valid index. |

Parent topic:

TClockSynchronizableDevicesCollection Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-remove__devicetosynchronize.html language=enus -->
## TOPIC 00053: Remove(DeviceToSynchronize)

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-remove__devicetosynchronize.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-remove__devicetosynchronize.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes the first occurrence of the specified device. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic void Remove(DeviceToSynchronize device)RemarksThe list elements after the removed element shift up to occupy the vacated spot. Because the list elements a

### Remove(DeviceToSynchronize)

Removes the first occurrence of the specified device.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public void Remove(DeviceToSynchronize device)

#### Remarks

The list elements after the removed element shift up to occupy the vacated spot. Because the list elements are indexed, the indexes of the shifted elements are also updated.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| device | DeviceToSynchronize | Device to remove from the collection. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentNullException | device value is null. |
| System.ArgumentException | device is already present in the collection. |

Parent topic:

TClockSynchronizableDevicesCollection Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-remove__itclocksynchronizabledevice.html language=enus -->
## TOPIC 00054: Remove(ITClockSynchronizableDevice)

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-remove__itclocksynchronizabledevice.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-remove__itclocksynchronizabledevice.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes the first occurrence of the specified device. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic void Remove(ITClockSynchronizableDevice device)RemarksThe list elements after the removed element shift up to occupy the vacated spot. Because the list el

### Remove(ITClockSynchronizableDevice)

Removes the first occurrence of the specified device.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public void Remove(ITClockSynchronizableDevice device)

#### Remarks

The list elements after the removed element shift up to occupy the vacated spot. Because the list elements are indexed, the indexes of the shifted elements are also updated.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| device | ITClockSynchronizableDevice | Device to remove from the collection. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentNullException | device value is null. |
| System.ArgumentException | device is already present in the collection. |

Parent topic:

TClockSynchronizableDevicesCollection Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-tclocksynchronizabledevicescollection.html language=enus -->
## TOPIC 00055: TClockSynchronizableDevicesCollection()

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-tclocksynchronizabledevicescollection.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-tclocksynchronizabledevicescollection.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the TClockSynchronizableDevicesCollection class. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic TClockSynchronizableDevicesCollection()

### TClockSynchronizableDevicesCollection()

Initializes a new instance of the [TClockSynchronizableDevicesCollection](nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection.html) class.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public TClockSynchronizableDevicesCollection()

Parent topic:

TClockSynchronizableDevicesCollection Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-this__int.html language=enus -->
## TOPIC 00056: this[int device]

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-this__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-this__int.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DeviceToSynchronize object at the specified index. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic DeviceToSynchronize this[int device] { get; }RemarksThe DeviceToSynchronize object present at the specified index in the collection. Returns the Dev

### this[int device]

Gets the [DeviceToSynchronize](nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize.html) object at the specified index.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public [DeviceToSynchronize](nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize.html) this[int device] { get; }

#### Remarks

The [DeviceToSynchronize](nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize.html) object present at the specified index in the collection.

Returns the [DeviceToSynchronize](nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize.html) object corresponding to the index.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| device | int | Zero-based index of the entry to access in the collection. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentNullException | device value is null. |

Parent topic:

TClockSynchronizableDevicesCollection Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-this__itclocksynchronizabledevice.html language=enus -->
## TOPIC 00057: this[ITClockSynchronizableDevice device]

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-this__itclocksynchronizabledevice.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection-this__itclocksynchronizabledevice.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DeviceToSynchronize object at the specified index. SyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic DeviceToSynchronize this[ITClockSynchronizableDevice device] { get; }RemarksThe DeviceToSynchronize object corresponding to the ITClockSynchronizabl

### this[ITClockSynchronizableDevice device]

Gets the [DeviceToSynchronize](nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize.html) object at the specified index.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public [DeviceToSynchronize](nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize.html) this[ITClockSynchronizableDevice device] { get; }

#### Remarks

The [DeviceToSynchronize](nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize.html) object corresponding to the ITClockSynchronizableDevice.

Returns the [DeviceToSynchronize](nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize.html) object corresponding to the ITClockSynchronizableDevice.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| device | ITClockSynchronizableDevice | Zero-based index of the entry to access in the collection. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentOutOfRangeException | device is outside the valid range of indexes for the collection. |

Parent topic:

TClockSynchronizableDevicesCollection Class

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection.html language=enus -->
## TOPIC 00058: TClockSynchronizableDevicesCollection Class

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices-tclocksynchronizabledevicescollection.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a collection of DeviceToSynchronize objects. Derives fromICollectionIListSyntaxNamespace: NationalInstruments.ModularInstruments.SystemServices.TimingServicespublic class TClockSynchronizableDevicesCollection : ICollection, IListRemarksThe TClock object holds a TClockSynchronizableDevices

### TClockSynchronizableDevicesCollection Class

Represents a collection of [DeviceToSynchronize](nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize.html) objects.

#### Derives from

- ICollection
- IList

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.SystemServices.TimingServices](nationalinstruments-modularinstruments-systemservices-timingservices.html)

public class TClockSynchronizableDevicesCollection : ICollection, IList

#### Remarks

The [TClock](nationalinstruments-modularinstruments-systemservices-timingservices-tclock.html) object holds a TClockSynchronizableDevicesCollection. Each item in the collection is a [DeviceToSynchronize](nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize.html) object. The [DeviceToSynchronize](nationalinstruments-modularinstruments-systemservices-timingservices-devicetosynchronize.html) object represents an ITClockSynchronizableDevice. This ITClockSynchronizableDevice is a modular instrument that can be synchronized by TClk technology.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| TClockSynchronizableDevicesCollection() | Initializes a new instance of the TClockSynchronizableDevicesCollection class. |

#### Properties

| Name | Description |
| --- | --- |
| Count | Gets the number of elements in the collection, which is equal to the number of NationalInstruments.ModularInstruments.ITClockSynchronizableDevice objects to be synchronized by TClk. |
| this[int device] | Gets the DeviceToSynchronize object at the specified index. |
| this[ITClockSynchronizableDevice device] | Gets the DeviceToSynchronize object at the specified index. |

#### Methods

| Name | Description |
| --- | --- |
| Add(DeviceToSynchronize) | Adds an item to the end of the collection. |
| Add(ITClockSynchronizableDevice) | Adds an item to the end of the collection. |
| AddRange(params ITClockSynchronizableDevice[]) | Adds an array of elements to the end of the collection. |
| AddRange(params DeviceToSynchronize[]) | Adds an array of elements to the end of the collection. |
| Clear() | Removes all items from the collection. |
| Contains(DeviceToSynchronize) | Returns whether the specified element is in the collection. |
| Contains(ITClockSynchronizableDevice) | Returns whether the specified element is in the collection. |
| CopyTo(DeviceToSynchronize[], int) | Copies the collection to an array or a portion of an array. |
| Equals(object) | Returns true if the specified object contains the same ITClockSynchronizableDevice devices as the current collection. |
| GetHashCode() | Generates a hash value that can be used to uniquely identify a particular TClockSynchronizableDevicesCollection object. |
| IndexOf(ITClockSynchronizableDevice) | Returns the zero-based index of the first occurrence of an item in the collection. |
| IndexOf(DeviceToSynchronize) | Returns the zero-based index of the first occurrence of an item in the collection. |
| Insert(int, DeviceToSynchronize) | Inserts a DeviceToSynchronize object into the collection at the specified index. |
| Insert(int, ITClockSynchronizableDevice) | Inserts a NationalInstruments.ModularInstruments.ITClockSynchronizableDevice object into the collection at the specified index. |
| Remove(DeviceToSynchronize) | Removes the first occurrence of the specified device. |
| Remove(ITClockSynchronizableDevice) | Removes the first occurrence of the specified device. |

#### Events

| Name | Description |
| --- | --- |
| CollectionChanged | Occurs when an item is added, removed, or updated. |

Parent topic:

NationalInstruments.ModularInstruments.SystemServices.TimingServices

<!--NI_TOPIC bundle=ni-tclk-csharp-api-ref path=nationalinstruments-modularinstruments-systemservices-timingservices.html language=enus -->
## TOPIC 00059: NationalInstruments.ModularInstruments.SystemServices.TimingServices

- bundle_id: `ni-tclk-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-systemservices-timingservices.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-systemservices-timingservices.html
- document_id: `ni-tclk-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionDeviceToSynchronizeRepresents a modular instruments device that can be synchronized. TClockRepresents the component that is used to synchronize modular instruments. TClockAdvancedProvides advanced functionality for NI-TClk. TClockSynchronizableDevicesCollectionRepresents a coll

### NationalInstruments.ModularInstruments.SystemServices.TimingServices

#### Classes

| Name | Description |
| --- | --- |
| DeviceToSynchronize | Represents a modular instruments device that can be synchronized. |
| TClock | Represents the component that is used to synchronize modular instruments. |
| TClockAdvanced | Provides advanced functionality for NI-TClk. |
| TClockSynchronizableDevicesCollection | Represents a collection of DeviceToSynchronize objects. |

#### Interfaces

None

#### Structures

None

#### Enumerations

None

#### Delegates

None
