# NI DOCUMENT BUNDLE: ni-tclk-properties

<!--NI_BUNDLE_CHUNK bundle=ni-tclk-properties start=1 end=14 -->
<!--NI_TOPIC bundle=ni-tclk-properties path=tclkpropref/nitclk_properties.html language=enus -->
## TOPIC 00001: NI-TClk Properties

- bundle_id: `ni-tclk-properties`
- source_path: `tclkpropref/nitclk_properties.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-properties/raw/resource/enus/tclkpropref/nitclk_properties.html
- document_id: `ni-tclk-properties`
- page_type: `leaf`
- content_type: ``

### NI-TClk Properties

September 2016, 372533G-01

Gets (reads) and/or sets (writes) properties of a session reference.

© 2003–2016 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=ni-tclk-properties path=tclkpropref/pnitclk_activechannelsproperty.html language=enus -->
## TOPIC 00002: NI-TClk Active Channels Property

- bundle_id: `ni-tclk-properties`
- source_path: `tclkpropref/pnitclk_activechannelsproperty.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-properties/raw/resource/enus/tclkpropref/pnitclk_activechannelsproperty.html
- document_id: `ni-tclk-properties`
- page_type: `leaf`
- content_type: ``

### NI-TClk Active Channels Property

**Short Name:** ActiveChans

Use this property in conjunction with the [Script Trigger Master Session](pnitclk_scripttriggermastersession.html) property to specify which Script Trigger (scriptTrigger0, scriptTrigger1, scriptTrigger2, or
scriptTrigger3) the Script Trigger Master Session applies to.

To specify the Script Trigger Master Session for more than one Script Trigger, specify the 
Active Channel and the Script Trigger Master Session properties multiple times. The following example shows how to specify Script Trigger Master Session for scriptTrigger0 and scriptTrigger1.

[IMAGE alt='image' src='multi_script.gif']

The property is named Active Channels for consistency with similar properties in NI-SCOPE, NI-HSDIO, and NI-FGEN.

#### Remarks

The following table lists the characteristics of this property.

| Data Type |  |
| --- | --- |
| Permissions | Write Only |

<!--NI_TOPIC bundle=ni-tclk-properties path=tclkpropref/pnitclk_exportsyncpulseoutputterminal.html language=enus -->
## TOPIC 00003: NI-TClk Export Sync Pulse Output Terminal Property

- bundle_id: `ni-tclk-properties`
- source_path: `tclkpropref/pnitclk_exportsyncpulseoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-properties/raw/resource/enus/tclkpropref/pnitclk_exportsyncpulseoutputterminal.html
- document_id: `ni-tclk-properties`
- page_type: `leaf`
- content_type: ``

### NI-TClk Export Sync Pulse Output Terminal Property

| Short Name: | ExportSyncPulseOutputTerm |
| --- | --- |
| Description: | Specifies the destination of the Sync Pulse signal. This property is most often used when synchronizing a multichassis system. |
| Values |  |
| PXI Devices: | "PXI_Trig0" through "PXI_Trig7", "PXI_STAR" (Slots 3 through 15), and device-specific settings |
| PCI Devices: | "RTSI_0" through "RTSI_7", and device-specific settings |
| Examples of Device-specific Settings: | NI PXI-5122 supports "PFI0" and "PFI1" NI PXI-5421 supports "PFI0", "PFI1", "PFI4", and "PFI5" NI PXI-6551/6552 supports "PFI0", "PFI1", "PFI2", and "PFI3" |
| Default Value: | Empty string. An empty string indicates that the signal is not exported. |

#### Remarks

The following table lists the characteristics of this property.

| Data Type |  |
| --- | --- |
| Permissions | R/W |
| Corresponding Active Channels | N/A |

<!--NI_TOPIC bundle=ni-tclk-properties path=tclkpropref/pnitclk_externalpulsesource.html language=enus -->
## TOPIC 00004: NI-TClk SyncPulseSender:External Pulse Source

- bundle_id: `ni-tclk-properties`
- source_path: `tclkpropref/pnitclk_externalpulsesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-properties/raw/resource/enus/tclkpropref/pnitclk_externalpulsesource.html
- document_id: `ni-tclk-properties`
- page_type: `leaf`
- content_type: ``

### NI-TClk SyncPulseSender:External Pulse Source

**Short Name:**SyncPulseSender.ExternalPulseSrc

**Description:**Specifies the external sync pulse source of the Sync Pulse Sender. You can use this source to synchronize the Sync Pulse Sender with an external non-TClk event.

#### Remarks

The following table lists the characteristics of this property.

| Data Type |  |
| --- | --- |
| Permissions | R/W |
| Corresponding Active Channels | N/A |

<!--NI_TOPIC bundle=ni-tclk-properties path=tclkpropref/pnitclk_outputterminal.html language=enus -->
## TOPIC 00005: NI-TClk Actual TClk:Output Terminal

- bundle_id: `ni-tclk-properties`
- source_path: `tclkpropref/pnitclk_outputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-properties/raw/resource/enus/tclkpropref/pnitclk_outputterminal.html
- document_id: `ni-tclk-properties`
- page_type: `leaf`
- content_type: ``

### NI-TClk Actual TClk:Output Terminal

**Short Name:**TClk.OutputTerm

**Description:**Specifies the destination for the TClk signal of the device.

#### Remarks

The following table lists the characteristics of this property.

| Data Type |  |
| --- | --- |
| Permissions | R/W |
| Corresponding Active Channels | N/A |

<!--NI_TOPIC bundle=ni-tclk-properties path=tclkpropref/pnitclk_pausetriggermastersession.html language=enus -->
## TOPIC 00006: NI-TClk Pause Trigger Master Session Property

- bundle_id: `ni-tclk-properties`
- source_path: `tclkpropref/pnitclk_pausetriggermastersession.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-properties/raw/resource/enus/tclkpropref/pnitclk_pausetriggermastersession.html
- document_id: `ni-tclk-properties`
- page_type: `leaf`
- content_type: ``

### NI-TClk Pause Trigger Master Session Property

| Short Name: | PauseTrigMasterSession |
| --- | --- |
| Description: | Specifies the Pause Trigger master session. For external triggers, the NI-TClk Pause Trigger Master Session is the session that receives the external trigger and exports it to the other sessions. For "None", the Pause Trigger Master Session is the session that generates the trigger. |

#### Remarks

The following table lists the characteristics of this property.

| Data Type |  |
| --- | --- |
| Permissions | R/W |
| Corresponding Active Channels | N/A |

<!--NI_TOPIC bundle=ni-tclk-properties path=tclkpropref/pnitclk_period.html language=enus -->
## TOPIC 00007: NI-TClk Actual TClk:Period

- bundle_id: `ni-tclk-properties`
- source_path: `tclkpropref/pnitclk_period.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-properties/raw/resource/enus/tclkpropref/pnitclk_period.html
- document_id: `ni-tclk-properties`
- page_type: `leaf`
- content_type: ``

### NI-TClk Actual TClk:Period

**Short Name:**TClk.Period

**Description:**Returns the computed TClk period.

#### Remarks

The following table lists the characteristics of this property.

| Data Type |  |
| --- | --- |
| Permissions | RO |
| Corresponding Active Channels | N/A |

<!--NI_TOPIC bundle=ni-tclk-properties path=tclkpropref/pnitclk_referencetriggermastersession.html language=enus -->
## TOPIC 00008: NI-TClk Reference Trigger Master Session Property

- bundle_id: `ni-tclk-properties`
- source_path: `tclkpropref/pnitclk_referencetriggermastersession.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-properties/raw/resource/enus/tclkpropref/pnitclk_referencetriggermastersession.html
- document_id: `ni-tclk-properties`
- page_type: `leaf`
- content_type: ``

### NI-TClk Reference Trigger Master Session Property

| Short Name: | RefTrigMasterSession |
| --- | --- |
| Description: | Specifies the Reference Trigger master session. For external triggers, the NI-TClk Reference Trigger Master Session is the session that receives the external trigger and exports it to the other sessions. For "None", the Reference Trigger Master Session is the session that generates the trigger. |

#### Remarks

The following table lists the characteristics of this property.

| Data Type |  |
| --- | --- |
| Permissions | R/W |
| Corresponding Active Channels | N/A |

<!--NI_TOPIC bundle=ni-tclk-properties path=tclkpropref/pnitclk_sampleclockdelay.html language=enus -->
## TOPIC 00009: NI-TClk Sample Clock Delay Property

- bundle_id: `ni-tclk-properties`
- source_path: `tclkpropref/pnitclk_sampleclockdelay.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-properties/raw/resource/enus/tclkpropref/pnitclk_sampleclockdelay.html
- document_id: `ni-tclk-properties`
- page_type: `leaf`
- content_type: ``

### NI-TClk Sample Clock Delay Property

| Short Name: | SampleClkDelay |
| --- | --- |
| Description: | Specifies the delay, in seconds, to apply to the session Sample Clock, relative to the other synchronized sessions. During synchronization, NI-TClk aligns the Sample Clocks on the synchronized devices. To delay the Sample Clocks, set this property before calling the niTClk Synchronize VI. |
| Values |  |
| Default Value: | 0 |

#### Remarks

The following table lists the characteristics of this property.

| Data Type |  |
| --- | --- |
| Permissions | R/W |
| Corresponding Active Channels | N/A |

<!--NI_TOPIC bundle=ni-tclk-properties path=tclkpropref/pnitclk_scripttriggermastersession.html language=enus -->
## TOPIC 00010: NI-TClk Script Trigger Master Session Property

- bundle_id: `ni-tclk-properties`
- source_path: `tclkpropref/pnitclk_scripttriggermastersession.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-properties/raw/resource/enus/tclkpropref/pnitclk_scripttriggermastersession.html
- document_id: `ni-tclk-properties`
- page_type: `leaf`
- content_type: ``

### NI-TClk Script Trigger Master Session Property

| Short Name: | ScriptTrigMasterSession |
| --- | --- |
| Description: | Specifies the Script Trigger master session. For external triggers, the NI-TClk Script Trigger Master Session is the session that receives the external trigger and exports it to the other sessions. For "None", the Script Trigger Master Session is the session that generates the trigger. |

#### Remarks

The following table lists the characteristics of this property.

| Data Type |  |
| --- | --- |
| Permissions | R/W |
| Corresponding Active Channels | scriptTrigger0, scriptTrigger1, scriptTrigger2, and scriptTrigger3 |

If the Active Channels property is not specified or is set to an empty string, the Script Trigger Master Session property uses scriptTrigger0 for backward compatibility.

<!--NI_TOPIC bundle=ni-tclk-properties path=tclkpropref/pnitclk_sequencerflagmastersession.html language=enus -->
## TOPIC 00011: NI-TClk Sequencer Flag Master Session Property

- bundle_id: `ni-tclk-properties`
- source_path: `tclkpropref/pnitclk_sequencerflagmastersession.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-properties/raw/resource/enus/tclkpropref/pnitclk_sequencerflagmastersession.html
- document_id: `ni-tclk-properties`
- page_type: `leaf`
- content_type: ``

### NI-TClk Sequencer Flag Master Session Property

| Short Name: | SequencerFlagMasterSession |
| --- | --- |
| Description: | Specifies the Sequencer Flag master session. For external triggers, the NI-TClk Sequencer Flag Master Session is the session that receives the external trigger and exports it to the other sessions. For "None", the Sequencer Flag Master Session is the session that generates the trigger. |

#### Remarks

The following table lists the characteristics of this property.

| Data Type |  |
| --- | --- |
| Permissions | R/W |
| Corresponding Active Channels | N/A |

<!--NI_TOPIC bundle=ni-tclk-properties path=tclkpropref/pnitclk_starttriggermastersession.html language=enus -->
## TOPIC 00012: NI-TClk Start Trigger Master Session Property

- bundle_id: `ni-tclk-properties`
- source_path: `tclkpropref/pnitclk_starttriggermastersession.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-properties/raw/resource/enus/tclkpropref/pnitclk_starttriggermastersession.html
- document_id: `ni-tclk-properties`
- page_type: `leaf`
- content_type: ``

### NI-TClk Start Trigger Master Session Property

| Short Name: | StartTrigMasterSession |
| --- | --- |
| Description: | Specifies the Start Trigger master session. For external triggers, the NI-TClk Start Trigger Master Session is the session that receives the external trigger and exports it to the other sessions. For "None", the Start Trigger Master Session is the session that generates the trigger. |

#### Remarks

The following table lists the characteristics of this property.

| Data Type |  |
| --- | --- |
| Permissions | R/W |
| Corresponding Active Channels | N/A |

<!--NI_TOPIC bundle=ni-tclk-properties path=tclkpropref/pnitclk_syncpulseclocksource.html language=enus -->
## TOPIC 00013: NI-TClk Sync Pulse Clock Source Property

- bundle_id: `ni-tclk-properties`
- source_path: `tclkpropref/pnitclk_syncpulseclocksource.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-properties/raw/resource/enus/tclkpropref/pnitclk_syncpulseclocksource.html
- document_id: `ni-tclk-properties`
- page_type: `leaf`
- content_type: ``

### NI-TClk Sync Pulse Clock Source Property

| Short Name: | SyncPulseClkSrc |
| --- | --- |
| Description: | Specifies the source for the 10 MHz clock signal used as the Sync Pulse Clock. If you want to control this yourself when synchronizing PCI devices, then drive a 10 MHz clock onto RTSI 7 and set this property accordingly. |
| Values |  |
| PXI Devices: | "PXI_CLK10", "None" |
| PCI Devices: | "RTSI_7", "None" |
| Default Value: | "None". "None" directs the niTClk Synchronize VI to create the necessary routes. For PCI, one of the synchronized devices drives a 10 MHz clock on RTSI 7, unless RTSI 7 is already being driven. |

#### Remarks

The following table lists the characteristics of this property.

| Data Type |  |
| --- | --- |
| Permissions | R/W |
| Corresponding Active Channels | N/A |

<!--NI_TOPIC bundle=ni-tclk-properties path=tclkpropref/pnitclk_syncpulsesource.html language=enus -->
## TOPIC 00014: NI-TClk Sync Pulse Source Property

- bundle_id: `ni-tclk-properties`
- source_path: `tclkpropref/pnitclk_syncpulsesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-tclk-properties/raw/resource/enus/tclkpropref/pnitclk_syncpulsesource.html
- document_id: `ni-tclk-properties`
- page_type: `leaf`
- content_type: ``

### NI-TClk Sync Pulse Source Property

| Short Name: | SyncPulseClk |
| --- | --- |
| Description: | Specifies the Sync Pulse source. This property is most often used when synchronizing a multichassis system. |
| Values |  |
| PXI Devices: | "PXI_Trig0", "PXI_Trig7", and device-specific settings |
| PCI Devices: | "RTSI_0" through "RTSI_7", and device-specific settings |
| Examples of Device-specific Settings | NI PXI-5122 supports "PFI0" and "PFI1" NI PXI-5421 supports "PFI0", "PFI1", "PFI4", and "PFI5" NI PXI-6551/6552 supports "PFI0", "PFI1", "PFI2", and "PFI3" |
| Default Value: | Empty string. An empty string indicates that the signal is not exported. The default value (empty string) directs the niTClk Synchronize VI to set this property when all the synchronized devices are in one PXI chassis or in one PC. To synchronize a multichassis system, you must set this property before calling the niTClk Synchronize VI. |

#### Remarks

The following table lists the characteristics of this property.

| Data Type |  |
| --- | --- |
| Permissions | R/W |
| Corresponding Active Channels | N/A |
