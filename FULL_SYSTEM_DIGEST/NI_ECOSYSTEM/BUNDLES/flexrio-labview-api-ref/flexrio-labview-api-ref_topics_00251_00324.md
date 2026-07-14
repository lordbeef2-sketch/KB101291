# NI DOCUMENT BUNDLE: flexrio-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=flexrio-labview-api-ref start=251 end=324 -->
<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-streamdataformat.html language=enus -->
## TOPIC 00251: Description:Stream Data Format

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-streamdataformat.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-streamdataformat.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Remarks The following table lists the characteristics of this property. Short Name Stream Data Format Data type ci32.png Permissions Read Only Interleaved 0 FIFO Per Channel 1

### Description:Stream Data Format

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Stream Data Format |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

| Interleaved | 0 |  |
| --- | --- | --- |
| FIFO Per Channel | 1 |  |

Parent topic:

FlexRIO Stream Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-streamfifoname.html language=enus -->
## TOPIC 00252: Description:FIFO Name

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-streamfifoname.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-streamfifoname.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a semicolon delimited list of the names of the FIFOs used on the stream. Remarks The following table lists the characteristics of this property. Short Name Stream FIFO Name Data type cstr.png Permissions Read Only

### Description:FIFO Name

Returns a semicolon delimited list of the names of the FIFOs used on the stream.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Stream FIFO Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Stream Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-streamfifosize.html language=enus -->
## TOPIC 00253: Stream FIFO Size

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-streamfifosize.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-streamfifosize.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of samples allocated in each stream FIFO. Set this value to 0 to allow the driver to allocate the buffer according to its own heuristics. Remarks The following table lists the characteristics of this property. Short Name Stream FIFO Size Data type cu64.png Permissions Read/Write

### Stream FIFO Size

Specifies the number of samples allocated in each stream FIFO. Set this value to 0 to allow the driver to allocate the buffer according to its own heuristics.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Stream FIFO Size |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Stream Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-streamfinite.html language=enus -->
## TOPIC 00254: Configuration:Finite

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-streamfinite.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-streamfinite.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the stream should be finite. Finite streams are bound by a number of samples specified in Stream Number of Samples. Remarks The following table lists the characteristics of this property. Short Name Stream Finite Data type cbool.png Permissions Read/Write

### Configuration:Finite

Specifies whether the stream should be finite. Finite streams are bound by a number of samples specified in Stream Number of Samples.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Stream Finite |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Stream Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-streamnumberofsamples.html language=enus -->
## TOPIC 00255: Stream Number Of Samples

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-streamnumberofsamples.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-streamnumberofsamples.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of samples to transfer in a finite stream. Remarks The following table lists the characteristics of this property. Short Name Stream Number Of Samples Data type cu64.png Permissions Read/Write

### Stream Number Of Samples

Specifies the number of samples to transfer in a finite stream.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Stream Number Of Samples |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Stream Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-tclkapicontrolenabled.html language=enus -->
## TOPIC 00256: Configuration:TClk API Control Enabled

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-tclkapicontrolenabled.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-tclkapicontrolenabled.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the TClk API will control this stream. When this attribute is true for a stream, TClk API calls such as niTClk Configure for Homogeneous Triggers, niTClk Initiate, and niTClk Wait Until Done will apply to this stream. Remarks The following table lists the characteristics of this pr

### Configuration:TClk API Control Enabled

Specifies whether the TClk API will control this stream. When this attribute is true for a stream, TClk API calls such as niTClk Configure for Homogeneous Triggers, niTClk Initiate, and niTClk Wait Until Done will apply to this stream.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TClk API Control Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Stream Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger-p.html language=enus -->
## TOPIC 00257: FlexRIO Trigger Properties

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger-p.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger-p.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`

### FlexRIO Trigger Properties

- [Active Trigger](../../../resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-activetrigger.html) Specifies the trigger instance used to access all subsequent properties in this instance of the property node. You must first select this property and then pass the name of the specific trigger.
- [Analog:Edge Trigger Channel](../../../resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-analogedgetriggerchannel.html) Specifies the channel to monitor for edge trigger conditions.
- [Analog:Edge Trigger Hysteresis](../../../resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-analogedgetriggerhysteresis.html) Specifies the trigger hysteresis in volts. Rising edge triggers arm when the signal drops below trigger level - hysteresis. Falling edge triggers arm when the signal rises above trigger level + hysteresis.
- [Analog:Edge Trigger Level](../../../resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-analogedgetriggerlevel.html) Specifies the trigger level in volts.
- [Analog:Edge Trigger Rising](../../../resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-analogedgetriggerrising.html) Specifies whether the analog edge trigger triggers on a rising edge. Set this value to FALSE to trigger on a falling edge.
- [DSP Reset:Sending Terminal](../../../resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-dspresetsendingterm.html) Indicates the terminal that will generate the TClk synchronized DSP Reset event if this device is the DSP Reset Master. The DSP Reset Master device is the first device in the array of devices passed to SynchronizedDspReset.
- [DSP Reset:Source](../../../resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-dspresetsource.html) Specifies the source of the TClk synchronized DSP Reset event.
- [External Analog:Edge Trigger Hysteresis](../../../resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-externalanalogedgetriggerhysteresis.html) Specifies the trigger hysteresis in volts. Rising edge triggers arm when the signal drops below trigger level - hysteresis. Falling edge triggers arm when the signal rises above trigger level + hysteresis.
- [External Analog:Edge Trigger Level](../../../resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-externalanalogedgetriggerlevel.html) Specifies the trigger level in volts.
- [External Analog:Edge Trigger Rising](../../../resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-externalanalogedgetriggerrising.html) Specifies whether the external analog edge trigger triggers on a rising edge. Set this value to FALSE to trigger on a falling edge.
- [Start:Linked](../../../resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-linkedstarttrigger.html) Configures whether this stream's trigger is overridden to be linked to another stream's start event. Ensure the target stream is *started* before the trigger arrives.
- [Start:Output Terminal](../../../resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-starttriggeroutputterminal.html) Specifies the export destination for the start trigger.
- [Start:TClk Conditioned Output Terminal](../../../resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-starttriggerfortclkoutputterminal.html) Specifies the export destination for the TClk conditioned start trigger.
- [Start:Terminals:Start Trigger For TClk Sending Terminal](../../../resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-tclkstarttriggerterm.html) Indicates the terminal that will export the TClk synchronized start trigger.
- [Start:Trigger Sensitivity](../../../resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-starttriggersensitivity.html) Specifies the trigger sensitivity.
- [Start:Trigger Synchronizer](../../../resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-starttriggersynchronizer.html) Specifies the trigger synchronizer configuration.
- [Start:Trigger Type](../../../resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-starttriggertype.html) Specifies the trigger type.
- [Trigger:Digital:Start:Source](../../../resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-digitalstarttriggersource.html) Specifies the source of the digital start trigger.

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-activetrigger.html language=enus -->
## TOPIC 00258: Active Trigger

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-activetrigger.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-activetrigger.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger instance used to access all subsequent properties in this instance of the property node. You must first select this property and then pass the name of the specific trigger. Remarks The following table lists the characteristics of this property. Short Name Active Trigger Data ty

### Active Trigger

Specifies the trigger instance used to access all subsequent properties in this instance of the property node. You must first select this property and then pass the name of the specific trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Active Trigger |
| --- | --- |
| Data type |  |
| Permissions | Write Only |

Parent topic:

FlexRIO Trigger Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-analogedgetriggerchannel.html language=enus -->
## TOPIC 00259: Analog:Edge Trigger Channel

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-analogedgetriggerchannel.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-analogedgetriggerchannel.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the channel to monitor for edge trigger conditions. Remarks The following table lists the characteristics of this property. Short Name Analog Edge Trigger Channel Data type ci32.png Permissions Read/Write

### Analog:Edge Trigger Channel

Specifies the channel to monitor for edge trigger conditions.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Analog Edge Trigger Channel |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Trigger Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-analogedgetriggerhysteresis.html language=enus -->
## TOPIC 00260: Analog:Edge Trigger Hysteresis

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-analogedgetriggerhysteresis.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-analogedgetriggerhysteresis.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger hysteresis in volts. Rising edge triggers arm when the signal drops below trigger level - hysteresis. Falling edge triggers arm when the signal rises above trigger level + hysteresis. Remarks The following table lists the characteristics of this property. Short Name Analog Edge

### Analog:Edge Trigger Hysteresis

Specifies the trigger hysteresis in volts. Rising edge triggers arm when the signal drops below trigger level - hysteresis. Falling edge triggers arm when the signal rises above trigger level + hysteresis.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Analog Edge Trigger Hysteresis |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Trigger Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-analogedgetriggerlevel.html language=enus -->
## TOPIC 00261: Analog:Edge Trigger Level

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-analogedgetriggerlevel.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-analogedgetriggerlevel.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger level in volts. Remarks The following table lists the characteristics of this property. Short Name Analog Edge Trigger Level Data type cdbl.png Permissions Read/Write

### Analog:Edge Trigger Level

Specifies the trigger level in volts.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Analog Edge Trigger Level |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Trigger Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-analogedgetriggerrising.html language=enus -->
## TOPIC 00262: Analog:Edge Trigger Rising

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-analogedgetriggerrising.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-analogedgetriggerrising.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the analog edge trigger triggers on a rising edge. Set this value to FALSE to trigger on a falling edge. Remarks The following table lists the characteristics of this property. Short Name Analog Edge Trigger Rising Data type cbool.png Permissions Read/Write

### Analog:Edge Trigger Rising

Specifies whether the analog edge trigger triggers on a rising edge. Set this value to FALSE to trigger on a falling edge.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Analog Edge Trigger Rising |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Trigger Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-digitalstarttriggersource.html language=enus -->
## TOPIC 00263: Trigger:Digital:Start:Source

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-digitalstarttriggersource.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-digitalstarttriggersource.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source of the digital start trigger. Remarks The following table lists the characteristics of this property. Short Name Digital Start Trigger Source Data type cstr.png Permissions Read/Write

### Trigger:Digital:Start:Source

Specifies the source of the digital start trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Digital Start Trigger Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Trigger Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-dspresetsendingterm.html language=enus -->
## TOPIC 00264: DSP Reset:Sending Terminal

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-dspresetsendingterm.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-dspresetsendingterm.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the terminal that will generate the TClk synchronized DSP Reset event if this device is the DSP Reset Master. The DSP Reset Master device is the first device in the array of devices passed to SynchronizedDspReset. Remarks The following table lists the characteristics of this property. Shor

### DSP Reset:Sending Terminal

Indicates the terminal that will generate the TClk synchronized DSP Reset event if this device is the DSP Reset Master. The DSP Reset Master device is the first device in the array of devices passed to SynchronizedDspReset.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DSP Reset Sending Term. |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Trigger Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-dspresetsource.html language=enus -->
## TOPIC 00265: DSP Reset:Source

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-dspresetsource.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-dspresetsource.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source of the TClk synchronized DSP Reset event. Remarks The following table lists the characteristics of this property. Short Name DSP Reset Source Data type cstr.png Permissions Read/Write

### DSP Reset:Source

Specifies the source of the TClk synchronized DSP Reset event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DSP Reset Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Trigger Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-externalanalogedgetriggerhysteresis.html language=enus -->
## TOPIC 00266: External Analog:Edge Trigger Hysteresis

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-externalanalogedgetriggerhysteresis.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-externalanalogedgetriggerhysteresis.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger hysteresis in volts. Rising edge triggers arm when the signal drops below trigger level - hysteresis. Falling edge triggers arm when the signal rises above trigger level + hysteresis. Remarks The following table lists the characteristics of this property. Short Name External An

### External Analog:Edge Trigger Hysteresis

Specifies the trigger hysteresis in volts. Rising edge triggers arm when the signal drops below trigger level - hysteresis. Falling edge triggers arm when the signal rises above trigger level + hysteresis.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | External Analog Edge Trigger Hysteresis |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Trigger Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-externalanalogedgetriggerlevel.html language=enus -->
## TOPIC 00267: External Analog:Edge Trigger Level

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-externalanalogedgetriggerlevel.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-externalanalogedgetriggerlevel.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger level in volts. Remarks The following table lists the characteristics of this property. Short Name External Analog Edge Trigger Level Data type cdbl.png Permissions Read/Write

### External Analog:Edge Trigger Level

Specifies the trigger level in volts.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | External Analog Edge Trigger Level |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Trigger Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-externalanalogedgetriggerrising.html language=enus -->
## TOPIC 00268: External Analog:Edge Trigger Rising

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-externalanalogedgetriggerrising.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-externalanalogedgetriggerrising.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the external analog edge trigger triggers on a rising edge. Set this value to FALSE to trigger on a falling edge. Remarks The following table lists the characteristics of this property. Short Name External Analog Edge Trigger Rising Data type cbool.png Permissions Read/Write

### External Analog:Edge Trigger Rising

Specifies whether the external analog edge trigger triggers on a rising edge. Set this value to FALSE to trigger on a falling edge.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | External Analog Edge Trigger Rising |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Trigger Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-linkedstarttrigger.html language=enus -->
## TOPIC 00269: Start:Linked

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-linkedstarttrigger.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-linkedstarttrigger.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether this stream's trigger is overridden to be linked to another stream's start event. Ensure the target stream is *started* before the trigger arrives. Remarks The following table lists the characteristics of this property. Short Name Linked Start Trigger Data type cbool.png Permissio

### Start:Linked

Configures whether this stream's trigger is overridden to be linked to another stream's start event. Ensure the target stream is *started* before the trigger arrives.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Linked Start Trigger |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Trigger Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-starttriggerfortclkoutputterminal.html language=enus -->
## TOPIC 00270: Start:TClk Conditioned Output Terminal

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-starttriggerfortclkoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-starttriggerfortclkoutputterminal.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the export destination for the TClk conditioned start trigger. Remarks The following table lists the characteristics of this property. Short Name Start Trigger for TClk Output Terminal Data type cstr.png Permissions Read/Write

### Start:TClk Conditioned Output Terminal

Specifies the export destination for the TClk conditioned start trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start Trigger for TClk Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Trigger Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-starttriggeroutputterminal.html language=enus -->
## TOPIC 00271: Start:Output Terminal

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-starttriggeroutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-starttriggeroutputterminal.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the export destination for the start trigger. Remarks The following table lists the characteristics of this property. Short Name Start Trigger Output Terminal Data type cstr.png Permissions Read/Write

### Start:Output Terminal

Specifies the export destination for the start trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start Trigger Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Trigger Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-starttriggersensitivity.html language=enus -->
## TOPIC 00272: Start:Trigger Sensitivity

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-starttriggersensitivity.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-starttriggersensitivity.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger sensitivity. Remarks The following table lists the characteristics of this property. Short Name Start Trigger Sensitivity Data type ci32.png Permissions Read/Write Rising Edge 2147483647 Falling Edge 2147483646 High Level 2147483645 Low Level 2147483644

### Start:Trigger Sensitivity

Specifies the trigger sensitivity.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start Trigger Sensitivity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| Rising Edge | 2147483647 |  |
| --- | --- | --- |
| Falling Edge | 2147483646 |  |
| High Level | 2147483645 |  |
| Low Level | 2147483644 |  |

Parent topic:

FlexRIO Trigger Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-starttriggersynchronizer.html language=enus -->
## TOPIC 00273: Start:Trigger Synchronizer

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-starttriggersynchronizer.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-starttriggersynchronizer.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger synchronizer configuration. Remarks The following table lists the characteristics of this property. Short Name Start Trigger Synchronizer Data type ci32.png Permissions Read/Write Disabled 0 Master 1 Slave 2

### Start:Trigger Synchronizer

Specifies the trigger synchronizer configuration.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start Trigger Synchronizer |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| Disabled | 0 |  |
| --- | --- | --- |
| Master | 1 |  |
| Slave | 2 |  |

Parent topic:

FlexRIO Trigger Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-starttriggertype.html language=enus -->
## TOPIC 00274: Start:Trigger Type

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-starttriggertype.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-starttriggertype.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger type. Remarks The following table lists the characteristics of this property. Short Name Start Trigger Type Data type ci32.png Permissions Read/Write Immediate 0 Digital 1 User 2 DIO 3 Analog 4 External Analog 5

### Start:Trigger Type

Specifies the trigger type.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start Trigger Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| Immediate | 0 |  |
| --- | --- | --- |
| Digital | 1 |  |
| User | 2 |  |
| DIO | 3 |  |
| Analog | 4 |  |
| External Analog | 5 |  |

Parent topic:

FlexRIO Trigger Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-tclkstarttriggerterm.html language=enus -->
## TOPIC 00275: Start:Terminals:Start Trigger For TClk Sending Terminal

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-tclkstarttriggerterm.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapitrigger-rc/flexrio-trigger/pniflexrio-tclkstarttriggerterm.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the terminal that will export the TClk synchronized start trigger. Remarks The following table lists the characteristics of this property. Short Name TClk Start Trigger Term. Data type cstr.png Permissions Read Only

### Start:Terminals:Start Trigger For TClk Sending Terminal

Indicates the terminal that will export the TClk synchronized start trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TClk Start Trigger Term. |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Trigger Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc.html language=enus -->
## TOPIC 00276: System Config

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`

### System Config

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapifilter-p.html language=enus -->
## TOPIC 00277: nisysapiFilter Properties

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapifilter-p.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapifilter-p.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`

### nisysapiFilter Properties

- [FlexRIO:Device Family](../../../resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-devicefamily.html) Specifies the resource's device type.
- [FlexRIO:Device Status](../../../resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-devicestatus.html) Specifies the operational status of the resource. This attribute is populated only on PXIe-797xR and NI-793xR targets. Values 0-2 apply to PXIe-797xR targets only. Values 0 and 3-7 apply to NI-793xR targets only.
- [FlexRIO:FPGA Family](../../../resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-fpgafamily.html) Specifies the resource's FPGA type.
- [FlexRIO:Fixed Logic Revision](../../../resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-fixedlogicrevision.html) Specifies the fixed logic version of the resource.
- [FlexRIO:FlexRIO with Integrated I/O:Test Verification:Last Temp (C)](../../../resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-lasttempc.html) Specifies the onboard device temperature, in degrees Celsius, the last time the device was externally adjusted.
- [FlexRIO:FlexRIO with Integrated I/O:Test Verification:Last Time](../../../resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-lasttime.html) Specifies the last time the device was externally calibrated.
- [FlexRIO:FlexRIO with Modular I/O:Adapter Module Present](../../../resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-adaptermodulepresent.html) Specifies whether an adapter module is detected by the resource.
- [FlexRIO:FlexRIO with Modular I/O:Adapter Module:Module ID](../../../resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-moduleid.html) Specifies the IO Module ID from the adapter module.
- [FlexRIO:FlexRIO with Modular I/O:Adapter Module:Powered On](../../../resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-poweredon.html) Specifies whether the adapter module is powered on. Returns TRUE if the adapter module is powered on, and returns FALSE if the adapter module is not powered on.
- [FlexRIO:FlexRIO with Modular I/O:Expected Adapter Module](../../../resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-expectedadaptermodule.html) Returns the name of the adapter module that the resource expected to be present.
- [FlexRIO:FlexRIO with Modular I/O:FPGA Module:Adapter Module Child Name](../../../resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-adaptermodulechildname.html) Returns the name of the adapter module attached to the FlexRIO FPGA Module or Controller for FlexRIO. For example, if the FPGA module or controller is named RIO0, the attached adapter module is named AdapterModule0. If the FPGA module or controller is named RIO1, the attached adapter module is named AdapterModule1, and so on.
- [FlexRIO:Is Adapter Module](../../../resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-isadaptermodule.html) Specifies whether this resource is an adapter module.
- [FlexRIO:Oldest Compatible Revision](../../../resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-oldestcompatiblerevision.html) Specifies the earliest fixed logic revision compatible with your resource.
- [FlexRIO:System Resources:Fan PWM](../../../resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-fanpwm.html) Specifies the PWM (pulse width modulation) duty cycle, in units of percentage, of the fans on the device.

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-adaptermodulechildname.html language=enus -->
## TOPIC 00278: FlexRIO:FlexRIO with Modular I/O:FPGA Module:Adapter Module Child Name

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-adaptermodulechildname.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-adaptermodulechildname.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the name of the adapter module attached to the FlexRIO FPGA Module or Controller for FlexRIO. For example, if the FPGA module or controller is named RIO0, the attached adapter module is named AdapterModule0. If the FPGA module or controller is named RIO1, the attached adapter module is named

### FlexRIO:FlexRIO with Modular I/O:FPGA Module:Adapter Module Child Name

Returns the name of the adapter module attached to the FlexRIO FPGA Module or Controller for FlexRIO. For example, if the FPGA module or controller is named RIO0, the attached adapter module is named AdapterModule0. If the FPGA module or controller is named RIO1, the attached adapter module is named AdapterModule1, and so on.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AdapterModuleChildName |
| --- | --- |
| Data type |  |
| Permissions | Write Only |

Parent topic:

nisysapiFilter Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-adaptermodulepresent.html language=enus -->
## TOPIC 00279: FlexRIO:FlexRIO with Modular I/O:Adapter Module Present

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-adaptermodulepresent.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-adaptermodulepresent.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether an adapter module is detected by the resource. Remarks The following table lists the characteristics of this property. Short Name AdapterModulePresent Data type cbool.png Permissions Write Only

### FlexRIO:FlexRIO with Modular I/O:Adapter Module Present

Specifies whether an adapter module is detected by the resource.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AdapterModulePresent |
| --- | --- |
| Data type |  |
| Permissions | Write Only |

Parent topic:

nisysapiFilter Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-devicefamily.html language=enus -->
## TOPIC 00280: FlexRIO:Device Family

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-devicefamily.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-devicefamily.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the resource's device type. Remarks The following table lists the characteristics of this property. Short Name DeviceFamily Data type cu32.png Permissions Write Only Unknown 0 PXIe-484X 1 PXI-795X 2 PXIe-796X 3 PXIe-797X 4 NI-793X 5 PXIe-798X 6

### FlexRIO:Device Family

Specifies the resource's device type.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DeviceFamily |
| --- | --- |
| Data type |  |
| Permissions | Write Only |

| Unknown | 0 |  |
| --- | --- | --- |
| PXIe-484X | 1 |  |
| PXI-795X | 2 |  |
| PXIe-796X | 3 |  |
| PXIe-797X | 4 |  |
| NI-793X | 5 |  |
| PXIe-798X | 6 |  |

Parent topic:

nisysapiFilter Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-devicestatus.html language=enus -->
## TOPIC 00281: FlexRIO:Device Status

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-devicestatus.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-devicestatus.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the operational status of the resource. This attribute is populated only on PXIe-797xR and NI-793xR targets. Values 0-2 apply to PXIe-797xR targets only. Values 0 and 3-7 apply to NI-793xR targets only. Remarks The following table lists the characteristics of this property. Short Name Devi

### FlexRIO:Device Status

Specifies the operational status of the resource. This attribute is populated only on PXIe-797xR and NI-793xR targets. Values 0-2 apply to PXIe-797xR targets only. Values 0 and 3-7 apply to NI-793xR targets only.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DeviceStatus |
| --- | --- |
| Data type |  |
| Permissions | Write Only |

| Normal | 0 |  |
| --- | --- | --- |
| Thermal Shutdown | 1 |  |
| Power Shutdown | 2 |  |
| Firmware Update Needed | 3 |  |
| Internal Error | 4 |  |
| Fan Slowed | 5 |  |
| Fan Stopped | 6 |  |
| PLL Loss of Lock | 7 |  |
| USB Over Current | 8 |  |

Parent topic:

nisysapiFilter Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-expectedadaptermodule.html language=enus -->
## TOPIC 00282: FlexRIO:FlexRIO with Modular I/O:Expected Adapter Module

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-expectedadaptermodule.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-expectedadaptermodule.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the name of the adapter module that the resource expected to be present. Remarks The following table lists the characteristics of this property. Short Name ExpectedAdapterModule Data type cstr.png Permissions Write Only

### FlexRIO:FlexRIO with Modular I/O:Expected Adapter Module

Returns the name of the adapter module that the resource expected to be present.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ExpectedAdapterModule |
| --- | --- |
| Data type |  |
| Permissions | Write Only |

Parent topic:

nisysapiFilter Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-fanpwm.html language=enus -->
## TOPIC 00283: FlexRIO:System Resources:Fan PWM

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-fanpwm.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-fanpwm.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the PWM (pulse width modulation) duty cycle, in units of percentage, of the fans on the device. Remarks The following table lists the characteristics of this property. Short Name FanPWM Data type c1du32.png Permissions Read Only

### FlexRIO:System Resources:Fan PWM

Specifies the PWM (pulse width modulation) duty cycle, in units of percentage, of the fans on the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FanPWM |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

nisysapiFilter Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-fixedlogicrevision.html language=enus -->
## TOPIC 00284: FlexRIO:Fixed Logic Revision

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-fixedlogicrevision.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-fixedlogicrevision.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the fixed logic version of the resource. Remarks The following table lists the characteristics of this property. Short Name FixedLogicRevision Data type cstr.png Permissions Write Only

### FlexRIO:Fixed Logic Revision

Specifies the fixed logic version of the resource.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FixedLogicRevision |
| --- | --- |
| Data type |  |
| Permissions | Write Only |

Parent topic:

nisysapiFilter Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-fpgafamily.html language=enus -->
## TOPIC 00285: FlexRIO:FPGA Family

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-fpgafamily.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-fpgafamily.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the resource's FPGA type. Remarks The following table lists the characteristics of this property. Short Name FPGAFamily Data type cu32.png Permissions Write Only Unknown 0 Virtex-5 1 Kintex-7 2 Kintex UltraScale 3 Kintex UltraScale+ 4 Virtex UltraScale+ 5 Versal 6

### FlexRIO:FPGA Family

Specifies the resource's FPGA type.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FPGAFamily |
| --- | --- |
| Data type |  |
| Permissions | Write Only |

| Unknown | 0 |  |
| --- | --- | --- |
| Virtex-5 | 1 |  |
| Kintex-7 | 2 |  |
| Kintex UltraScale | 3 |  |
| Kintex UltraScale+ | 4 |  |
| Virtex UltraScale+ | 5 |  |
| Versal | 6 |  |

Parent topic:

nisysapiFilter Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-isadaptermodule.html language=enus -->
## TOPIC 00286: FlexRIO:Is Adapter Module

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-isadaptermodule.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-isadaptermodule.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether this resource is an adapter module. Remarks The following table lists the characteristics of this property. Short Name IsAdapterModule Data type cbool.png Permissions Write Only

### FlexRIO:Is Adapter Module

Specifies whether this resource is an adapter module.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IsAdapterModule |
| --- | --- |
| Data type |  |
| Permissions | Write Only |

Parent topic:

nisysapiFilter Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-lasttempc.html language=enus -->
## TOPIC 00287: FlexRIO:FlexRIO with Integrated I/O:Test Verification:Last Temp (C)

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-lasttempc.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-lasttempc.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the onboard device temperature, in degrees Celsius, the last time the device was externally adjusted. Remarks The following table lists the characteristics of this property. Short Name TestVerificationLastTempC Data type cdbl.png Permissions Read Only

### FlexRIO:FlexRIO with Integrated I/O:Test Verification:Last Temp (C)

Specifies the onboard device temperature, in degrees Celsius, the last time the device was externally adjusted.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TestVerificationLastTempC |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

nisysapiFilter Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-lasttime.html language=enus -->
## TOPIC 00288: FlexRIO:FlexRIO with Integrated I/O:Test Verification:Last Time

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-lasttime.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-lasttime.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the last time the device was externally calibrated. Remarks The following table lists the characteristics of this property. Short Name TestVerificationLastTime Data type catrn.png Permissions Read Only

### FlexRIO:FlexRIO with Integrated I/O:Test Verification:Last Time

Specifies the last time the device was externally calibrated.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TestVerificationLastTime |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

nisysapiFilter Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-moduleid.html language=enus -->
## TOPIC 00289: FlexRIO:FlexRIO with Modular I/O:Adapter Module:Module ID

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-moduleid.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-moduleid.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the IO Module ID from the adapter module. Remarks The following table lists the characteristics of this property. Short Name ModuleID Data type cstr.png Permissions Write Only

### FlexRIO:FlexRIO with Modular I/O:Adapter Module:Module ID

Specifies the IO Module ID from the adapter module.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModuleID |
| --- | --- |
| Data type |  |
| Permissions | Write Only |

Parent topic:

nisysapiFilter Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-oldestcompatiblerevision.html language=enus -->
## TOPIC 00290: FlexRIO:Oldest Compatible Revision

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-oldestcompatiblerevision.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-oldestcompatiblerevision.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the earliest fixed logic revision compatible with your resource. Remarks The following table lists the characteristics of this property. Short Name OldestCompatibleRevision Data type cstr.png Permissions Write Only

### FlexRIO:Oldest Compatible Revision

Specifies the earliest fixed logic revision compatible with your resource.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OldestCompatibleRevision |
| --- | --- |
| Data type |  |
| Permissions | Write Only |

Parent topic:

nisysapiFilter Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-poweredon.html language=enus -->
## TOPIC 00291: FlexRIO:FlexRIO with Modular I/O:Adapter Module:Powered On

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-poweredon.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapifilter/pni-flexrio-poweredon.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the adapter module is powered on. Returns TRUE if the adapter module is powered on, and returns FALSE if the adapter module is not powered on. Remarks The following table lists the characteristics of this property. Short Name PoweredOn Data type cbool.png Permissions Write Only

### FlexRIO:FlexRIO with Modular I/O:Adapter Module:Powered On

Specifies whether the adapter module is powered on. Returns TRUE if the adapter module is powered on, and returns FALSE if the adapter module is not powered on.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PoweredOn |
| --- | --- |
| Data type |  |
| Permissions | Write Only |

Parent topic:

nisysapiFilter Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapihardware-p.html language=enus -->
## TOPIC 00292: nisysapiHardware Properties

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapihardware-p.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapihardware-p.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`

### nisysapiHardware Properties

- [FlexRIO:Device Family](../../../resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-devicestatus.html) Specifies the resource's device type.
- [FlexRIO:FPGA Family](../../../resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-fpgafamily.html) Specifies the resource's FPGA type.
- [FlexRIO:Fixed Logic Revision](../../../resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-fixedlogicrevision.html) Specifies the fixed logic version of the resource.
- [FlexRIO:FlexRIO with Integrated I/O:Test Verification:Last Temp (C)](../../../resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-lasttempc.html) Specifies the onboard device temperature, in degrees Celsius, the last time the device was externally adjusted.
- [FlexRIO:FlexRIO with Integrated I/O:Test Verification:Last Time](../../../resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-lasttime.html) Specifies the last time the device was externally calibrated.
- [FlexRIO:FlexRIO with Modular I/O:Adapter Module:Module ID](../../../resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-moduleid.html) Specifies the IO Module ID from the adapter module.
- [FlexRIO:FlexRIO with Modular I/O:Adapter Module:Powered On](../../../resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-poweredon.html) Specifies whether the adapter module is powered on. Returns TRUE if the adapter module is powered on, and returns FALSE if the adapter module is not powered on.
- [FlexRIO:FlexRIO with Modular I/O:FPGA Module:Adapter Module Child Name](../../../resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-adaptermodulechildname.html) Returns the name of the adapter module attached to the FlexRIO FPGA Module or Controller for FlexRIO. For example, if the FPGA module or controller is named RIO0, the attached adapter module is named AdapterModule0. If the FPGA module or controller is named RIO1, the attached adapter module is named AdapterModule1, and so on.
- [FlexRIO:FlexRIO with Modular I/O:FPGA Module:Adapter Module Present](../../../resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-adaptermodulepresent.html) Specifies whether an adapter module is detected by the resource.
- [FlexRIO:FlexRIO with Modular I/O:FPGA Module:Expected Adapter Module](../../../resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-expectedadaptermodule.html) Returns the name of the adapter module that the resource expected to be present.
- [FlexRIO:Is Adapter Module](../../../resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-isadaptermodule.html) Specifies whether this resource is an adapter module.
- [FlexRIO:Oldest Compatible Fixed Logic Revision](../../../resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-oldestcompatiblefixedlogicrevision.html) Specifies the earliest fixed logic revision compatible with your resource.
- [FlexRIO:System Resources:Fan PWM](../../../resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-fanpwm.html) Specifies the PWM (pulse width modulation) duty cycle, in units of percentage, of the fans on the device.

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-adaptermodulechildname.html language=enus -->
## TOPIC 00293: FlexRIO:FlexRIO with Modular I/O:FPGA Module:Adapter Module Child Name

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-adaptermodulechildname.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-adaptermodulechildname.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the name of the adapter module attached to the FlexRIO FPGA Module or Controller for FlexRIO. For example, if the FPGA module or controller is named RIO0, the attached adapter module is named AdapterModule0. If the FPGA module or controller is named RIO1, the attached adapter module is named

### FlexRIO:FlexRIO with Modular I/O:FPGA Module:Adapter Module Child Name

Returns the name of the adapter module attached to the FlexRIO FPGA Module or Controller for FlexRIO. For example, if the FPGA module or controller is named RIO0, the attached adapter module is named AdapterModule0. If the FPGA module or controller is named RIO1, the attached adapter module is named AdapterModule1, and so on.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AdapterModuleChildName |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

nisysapiHardware Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-adaptermodulepresent.html language=enus -->
## TOPIC 00294: FlexRIO:FlexRIO with Modular I/O:FPGA Module:Adapter Module Present

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-adaptermodulepresent.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-adaptermodulepresent.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether an adapter module is detected by the resource. Remarks The following table lists the characteristics of this property. Short Name AdapterModulePresent Data type cbool.png Permissions Read Only

### FlexRIO:FlexRIO with Modular I/O:FPGA Module:Adapter Module Present

Specifies whether an adapter module is detected by the resource.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AdapterModulePresent |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

nisysapiHardware Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-devicestatus.html language=enus -->
## TOPIC 00295: FlexRIO:Device Family

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-devicestatus.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-devicestatus.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the resource's device type. Remarks The following table lists the characteristics of this property. Short Name DeviceFamily Data type cu32.png Permissions Read Only Unknown 0 PXIe-484X 1 PXI-795X 2 PXIe-796X 3 PXIe-797X 4 NI-793X 5 PXIe-798X 6

### FlexRIO:Device Family

Specifies the resource's device type.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DeviceFamily |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

| Unknown | 0 |  |
| --- | --- | --- |
| PXIe-484X | 1 |  |
| PXI-795X | 2 |  |
| PXIe-796X | 3 |  |
| PXIe-797X | 4 |  |
| NI-793X | 5 |  |
| PXIe-798X | 6 |  |

Parent topic:

nisysapiHardware Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-expectedadaptermodule.html language=enus -->
## TOPIC 00296: FlexRIO:FlexRIO with Modular I/O:FPGA Module:Expected Adapter Module

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-expectedadaptermodule.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-expectedadaptermodule.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the name of the adapter module that the resource expected to be present. Remarks The following table lists the characteristics of this property. Short Name ExpectedAdapterModule Data type cstr.png Permissions Read Only

### FlexRIO:FlexRIO with Modular I/O:FPGA Module:Expected Adapter Module

Returns the name of the adapter module that the resource expected to be present.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ExpectedAdapterModule |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

nisysapiHardware Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-fanpwm.html language=enus -->
## TOPIC 00297: FlexRIO:System Resources:Fan PWM

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-fanpwm.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-fanpwm.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the PWM (pulse width modulation) duty cycle, in units of percentage, of the fans on the device. Remarks The following table lists the characteristics of this property. Short Name FanPWM Data type c1du32.png Permissions Read Only

### FlexRIO:System Resources:Fan PWM

Specifies the PWM (pulse width modulation) duty cycle, in units of percentage, of the fans on the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FanPWM |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

nisysapiHardware Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-fixedlogicrevision.html language=enus -->
## TOPIC 00298: FlexRIO:Fixed Logic Revision

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-fixedlogicrevision.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-fixedlogicrevision.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the fixed logic version of the resource. Remarks The following table lists the characteristics of this property. Short Name FixedLogicRevision Data type cstr.png Permissions Read Only

### FlexRIO:Fixed Logic Revision

Specifies the fixed logic version of the resource.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FixedLogicRevision |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

nisysapiHardware Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-fpgafamily.html language=enus -->
## TOPIC 00299: FlexRIO:FPGA Family

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-fpgafamily.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-fpgafamily.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the resource's FPGA type. Remarks The following table lists the characteristics of this property. Short Name FPGAFamily Data type cu32.png Permissions Read Only Unknown 0 Virtex-5 1 Kintex-7 2 Kintex UltraScale 3 Kintex UltraScale+ 4 Virtex UltraScale+ 5 Versal 6

### FlexRIO:FPGA Family

Specifies the resource's FPGA type.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FPGAFamily |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

| Unknown | 0 |  |
| --- | --- | --- |
| Virtex-5 | 1 |  |
| Kintex-7 | 2 |  |
| Kintex UltraScale | 3 |  |
| Kintex UltraScale+ | 4 |  |
| Virtex UltraScale+ | 5 |  |
| Versal | 6 |  |

Parent topic:

nisysapiHardware Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-isadaptermodule.html language=enus -->
## TOPIC 00300: FlexRIO:Is Adapter Module

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-isadaptermodule.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-isadaptermodule.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether this resource is an adapter module. Remarks The following table lists the characteristics of this property. Short Name IsAdapterModule Data type cbool.png Permissions Read Only

### FlexRIO:Is Adapter Module

Specifies whether this resource is an adapter module.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IsAdapterModule |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

nisysapiHardware Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-lasttempc.html language=enus -->
## TOPIC 00301: FlexRIO:FlexRIO with Integrated I/O:Test Verification:Last Temp (C)

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-lasttempc.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-lasttempc.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the onboard device temperature, in degrees Celsius, the last time the device was externally adjusted. Remarks The following table lists the characteristics of this property. Short Name TestVerificationLastTempC Data type cdbl.png Permissions Read Only

### FlexRIO:FlexRIO with Integrated I/O:Test Verification:Last Temp (C)

Specifies the onboard device temperature, in degrees Celsius, the last time the device was externally adjusted.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TestVerificationLastTempC |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

nisysapiHardware Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-lasttime.html language=enus -->
## TOPIC 00302: FlexRIO:FlexRIO with Integrated I/O:Test Verification:Last Time

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-lasttime.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-lasttime.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the last time the device was externally calibrated. Remarks The following table lists the characteristics of this property. Short Name TestVerificationLastTime Data type catrn.png Permissions Read Only

### FlexRIO:FlexRIO with Integrated I/O:Test Verification:Last Time

Specifies the last time the device was externally calibrated.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TestVerificationLastTime |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

nisysapiHardware Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-moduleid.html language=enus -->
## TOPIC 00303: FlexRIO:FlexRIO with Modular I/O:Adapter Module:Module ID

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-moduleid.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-moduleid.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the IO Module ID from the adapter module. Remarks The following table lists the characteristics of this property. Short Name ModuleID Data type cstr.png Permissions Read Only

### FlexRIO:FlexRIO with Modular I/O:Adapter Module:Module ID

Specifies the IO Module ID from the adapter module.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModuleID |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

nisysapiHardware Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-oldestcompatiblefixedlogicrevision.html language=enus -->
## TOPIC 00304: FlexRIO:Oldest Compatible Fixed Logic Revision

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-oldestcompatiblefixedlogicrevision.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-oldestcompatiblefixedlogicrevision.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the earliest fixed logic revision compatible with your resource. Remarks The following table lists the characteristics of this property. Short Name OldestCompatibleFixedLogicRevision Data type cstr.png Permissions Read Only

### FlexRIO:Oldest Compatible Fixed Logic Revision

Specifies the earliest fixed logic revision compatible with your resource.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OldestCompatibleFixedLogicRevision |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

nisysapiHardware Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-poweredon.html language=enus -->
## TOPIC 00305: FlexRIO:FlexRIO with Modular I/O:Adapter Module:Powered On

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-poweredon.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexriosae-rc/nisysapihardware/pni-flexrio-poweredon.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the adapter module is powered on. Returns TRUE if the adapter module is powered on, and returns FALSE if the adapter module is not powered on. Remarks The following table lists the characteristics of this property. Short Name PoweredOn Data type cbool.png Permissions Read Only

### FlexRIO:FlexRIO with Modular I/O:Adapter Module:Powered On

Specifies whether the adapter module is powered on. Returns TRUE if the adapter module is powered on, and returns FALSE if the adapter module is not powered on.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PoweredOn |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

nisysapiHardware Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-controliomodpower-vi.html language=enus -->
## TOPIC 00306: FlexRIO_Host_ControlIOModPower VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-controliomodpower-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-controliomodpower-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables or disables power to the attached FlexRIO adapter module. icon Inputs/Outputs cdaqmxscale.png RIO Device Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Exp

### FlexRIO_Host_ControlIOModPower VI

Enables or disables power to the attached FlexRIO adapter module.

[IMAGE alt='icon' src='flexrio-host-controliomodpower-vi.png']

#### Inputs/Outputs

| RIO Device — Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). Enabled — When TRUE, power to the adapter module is enabled if it is compatible with the bitstream currently downloaded to the FPGA. When FALSE, power to the adapter module is disabled. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. RIO Device out — Returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexRIO LabVIEW Host VIs

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-customattributeread-vi.html language=enus -->
## TOPIC 00307: FlexRIO_Host_CustomAttributeRead VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-customattributeread-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-customattributeread-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the current value of the specified attribute. icon Inputs/Outputs cdaqmxscale.png RIO Device Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX).

### FlexRIO_Host_CustomAttributeRead VI

Queries the current value of the specified attribute.

[IMAGE alt='icon' src='flexrio-host-customattributeread-vi.png']

#### Inputs/Outputs

| RIO Device — Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). — Specifies which custom attribute to query. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. RIO Device out — Returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. — Returns the value read from the specified custom attribute. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexRIO LabVIEW Host VIs

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-customattributewrite-vi.html language=enus -->
## TOPIC 00308: FlexRIO_Host_CustomAttributeWrite VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-customattributewrite-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-customattributewrite-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a value to the specified custom attribute. icon Inputs/Outputs cdaqmxscale.png RIO Device Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). cu3

### FlexRIO_Host_CustomAttributeWrite VI

Writes a value to the specified custom attribute.

[IMAGE alt='icon' src='flexrio-host-customattributewrite-vi.png']

#### Inputs/Outputs

| RIO Device — Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). — Specifies which custom attribute to write to. — Specifies the value to write to the specified attribute. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. RIO Device out — Returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexRIO LabVIEW Host VIs

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-eepromread32-vi.html language=enus -->
## TOPIC 00309: FlexRIO_Host_EEPROMRead32 VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-eepromread32-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-eepromread32-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads an unsigned 32-bit number from the adapter module EEPROM at the specified address. icon Inputs/Outputs cdaqmxscale.png RIO Device Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measu

### FlexRIO_Host_EEPROMRead32 VI

Reads an unsigned 32-bit number from the adapter module EEPROM at the specified address.

[IMAGE alt='icon' src='flexrio-host-eepromread32-vi.png']

#### Inputs/Outputs

| RIO Device — Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). Address — Specifies the EEPROM byte address to read from. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. RIO Device out — Returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. Data — Returns the data that was read from the EEPROM at the specified byte address. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexRIO LabVIEW Host VIs

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-eepromreadbytearray-vi.html language=enus -->
## TOPIC 00310: FlexRIO_Host_EEPROMReadByteArray VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-eepromreadbytearray-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-eepromreadbytearray-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads an array of bytes from the adapter module EEPROM, starting at the specified address. icon Inputs/Outputs cdaqmxscale.png RIO Device Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Mea

### FlexRIO_Host_EEPROMReadByteArray VI

Reads an array of bytes from the adapter module EEPROM, starting at the specified address.

[IMAGE alt='icon' src='flexrio-host-eepromreadbytearray-vi.png']

#### Inputs/Outputs

| RIO Device — Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). Address — Specifies the EEPROM byte address to start reading from. Size (bytes) — Specifies the number of bytes to read from the EEPROM. The maximum possible EEPROM address is 255. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. RIO Device out — Returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. Data — error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexRIO LabVIEW Host VIs

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-eepromwrite32-vi.html language=enus -->
## TOPIC 00311: FlexRIO_Host_EEPROMWrite32 VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-eepromwrite32-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-eepromwrite32-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an unsigned 32-bit number to the adapter module EEPROM at the specified address. icon Inputs/Outputs cbool.png Suppress Message Box? (No) cdaqmxscale.png RIO Device Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO

### FlexRIO_Host_EEPROMWrite32 VI

Writes an unsigned 32-bit number to the adapter module EEPROM at the specified address.

[IMAGE alt='icon' src='flexrio-host-eepromwrite32-vi.png']

#### Inputs/Outputs

| Suppress Message Box? (No) — RIO Device — Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). Address — Specifies the EEPROM byte address to write to. Data — Specifies the 32-bit data value to write to the EEPROM. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. RIO Device out — Returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexRIO LabVIEW Host VIs

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-eepromwritebytearray-vi.html language=enus -->
## TOPIC 00312: FlexRIO_Host_EEPROMWriteByteArray VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-eepromwritebytearray-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-eepromwritebytearray-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an array of bytes to the adapter module EEPROM, starting at the specified address. icon Inputs/Outputs cbool.png Suppress Message Box? (No) cdaqmxscale.png RIO Device Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRI

### FlexRIO_Host_EEPROMWriteByteArray VI

Writes an array of bytes to the adapter module EEPROM, starting at the specified address.

[IMAGE alt='icon' src='flexrio-host-eepromwritebytearray-vi.png']

#### Inputs/Outputs

| Suppress Message Box? (No) — RIO Device — Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). Address — Specifies the EEPROM byte address to start writing to. Data — error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. RIO Device out — Returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexRIO LabVIEW Host VIs

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-getdeviceshutdownlimit-vi.html language=enus -->
## TOPIC 00313: FlexRIO_Host_GetDeviceShutdownLimit VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-getdeviceshutdownlimit-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-getdeviceshutdownlimit-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This VI returns the device's thermal shutdown limit. icon Inputs/Outputs cdaqmxscale.png RIO Device Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX).

### FlexRIO_Host_GetDeviceShutdownLimit VI

This VI returns the device's thermal shutdown limit.

[IMAGE alt='icon' src='flexrio-host-getdeviceshutdownlimit-vi.png']

#### Inputs/Outputs

| RIO Device — Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). Shutdown Type — Description - specifies what type of shutdown to configure. Valid values: Thermal, Total Power, 3.3V Power, 12V Power error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. RIO Device out — Returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. Value in deg C or mW — Returns the device's thermal shutdown limit. If you specified Thermal in Shutdown Type, this value is returned in °C. If you specified Total Power, 3.3V Power or 12V Power in Shutdown Type, this value is returned in mW. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexRIO LabVIEW Host VIs

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-getdevicestatus-vi.html language=enus -->
## TOPIC 00314: FlexRIO_Host_GetDeviceStatus VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-getdevicestatus-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-getdevicestatus-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the current status of the specified hardware device. icon Inputs/Outputs cdaqmxscale.png RIO Device Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer

### FlexRIO_Host_GetDeviceStatus VI

Queries the current status of the specified hardware device.

[IMAGE alt='icon' src='flexrio-host-getdevicestatus-vi.png']

#### Inputs/Outputs

| RIO Device — Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. RIO Device out — Returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexRIO LabVIEW Host VIs

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-i2caccesscontrol-vi.html language=enus -->
## TOPIC 00315: FlexRIO_Host_I2CAccessControl VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-i2caccesscontrol-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-i2caccesscontrol-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this VI to acquire or release software access to the adapter module I2C bus. NI FlexRIO firmware has an arbiter that controls access to the I2C bus on the adapter module interface. Before issuing any I2C bus commands to the adapter module, software must first acquire access to the I2C bus. The F

### FlexRIO_Host_I2CAccessControl VI

Use this VI to acquire or release software access to the adapter module I2C bus. NI FlexRIO firmware has an arbiter that controls access to the I2C bus on the adapter module interface. Before issuing any I2C bus commands to the adapter module, software must first acquire access to the I2C bus. The FlexRIO host interface gives users the ability to perform raw I2C bus cycles by using the FlexRIO_Host_I2CIssueBusCycle VI. Because this VI makes no assumptions about I2C command composition, you must use the FlexRIO_Host_I2C_AccessControl VI to acquire and release access to the bus before and after issuing your I2C command.

Note that it is not necessary to use this VI with the FlexRIO EEPROM host interface VIs. The EEPROM host interface VIs will all automatically acquire and release access to the bus internally.

[IMAGE alt='icon' src='flexrio-host-i2caccesscontrol-vi.png']

#### Inputs/Outputs

| RIO Device — Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). Method — Specifies whether you want to acquire or release access to the I2C bus. Timeout in msec (1000) — Specifies the number of milliseconds the VI waits before timing out. -1 indicates that the timeout waits indefinitely. The default is 1000 ms. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. RIO Device out — Returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexRIO LabVIEW Host VIs

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-i2cissuebuscycle-vi.html language=enus -->
## TOPIC 00316: FlexRIO_Host_I2CIssueBusCycle VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-i2cissuebuscycle-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-i2cissuebuscycle-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this VI to issue a single cycle on the adapter module I2C bus. By chaining multiple instances of this VI together, you are able to issue custom I2C commands to the adapter module interface. This is useful for accessing custom I2C circuitry that may exist on custom adapter modules. Note that prio

### FlexRIO_Host_I2CIssueBusCycle VI

Use this VI to issue a single cycle on the adapter module I2C bus. By chaining multiple instances of this VI together, you are able to issue custom I2C commands to the adapter module interface. This is useful for accessing custom I2C circuitry that may exist on custom adapter modules.

Note that prior to using this VI, you must first acquire software access to the I2C bus by calling the FlexRIO_Host_I2CAccessControl VI.

[IMAGE alt='icon' src='flexrio-host-i2cissuebuscycle-vi.png']

#### Inputs/Outputs

| Start bit? — When TRUE, causes the I2C controller to issue a start bit with the I2C bus cycle. When FALSE, the I2C controller does not issue a start bit with the I2C bus cycle. RIO Device — Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). Command — Specifies whether the I2C bus cycle is performing a write or read operation. Write Data — The raw data that is written to the I2C bus when performing a write operation. Expect Ack? — When TRUE, causes the I2C controller to wait for an acknowledge bit before finishing the I2C bus cycle. When FALSE, the I2C controller does not wait for an acknowledge bit. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. Stop bit? — When TRUE, causes the I2C controller to issue a stop bit with the I2C bus cycle. When FALSE, the I2C controller does not issue a stop bit with the I2C bus cycle. RIO Device out — Returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. Read Data — The raw data that was read from the I2C bus when performing a read operation. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexRIO LabVIEW Host VIs

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-programiomodid-vi.html language=enus -->
## TOPIC 00317: FlexRIO_Host_ProgramIOModID VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-programiomodid-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-programiomodid-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Programs the IO Module ID to the EEPROM on the adapter module that is currently connected. Note: Use this VI to program the IO Module ID on custom adapter modules only. Do not use this VI to reprogram the IO Module ID on an adapter module that you did not manufacturer. icon Inputs/Outputs cbool.png

### FlexRIO_Host_ProgramIOModID VI

Programs the IO Module ID to the EEPROM on the adapter module that is currently connected.

Note: Use this VI to program the IO Module ID on custom adapter modules only. Do not use this VI to reprogram the IO Module ID on an adapter module that you did not manufacturer.

[IMAGE alt='icon' src='flexrio-host-programiomodid-vi.png']

#### Inputs/Outputs

| Suppress Message Box? (No) — RIO Device — Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). IO Module ID — Specifies the unique, 32-bit IO Module ID of your adapter module. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. RIO Device out — Returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexRIO LabVIEW Host VIs

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-queryattribute-bool-vi.html language=enus -->
## TOPIC 00318: FlexRIO_Host_QueryAttribute_Bool VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-queryattribute-bool-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-queryattribute-bool-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the current value of the selected attribute. icon Inputs/Outputs cdaqmxscale.png RIO Device Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX).

### FlexRIO_Host_QueryAttribute_Bool VI

Queries the current value of the selected attribute.

[IMAGE alt='icon' src='flexrio-host-queryattribute-bool-vi.png']

#### Inputs/Outputs

| RIO Device — Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). Attribute — Specifies which attribute to query. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. RIO Device out — Returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. Value — Returns the value of specified attribute. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexRIO LabVIEW Host VIs

Parent topic:

FlexRIO_Host_QueryAttribute VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-queryattribute-u32-vi.html language=enus -->
## TOPIC 00319: FlexRIO_Host_QueryAttribute_U32 VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-queryattribute-u32-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-queryattribute-u32-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the current value of the selected attribute. icon Inputs/Outputs cdaqmxscale.png RIO Device Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX).

### FlexRIO_Host_QueryAttribute_U32 VI

Queries the current value of the selected attribute.

[IMAGE alt='icon' src='flexrio-host-queryattribute-u32-vi.png']

#### Inputs/Outputs

| RIO Device — Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). Attribute — Specifies which attribute to query. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. RIO Device out — Returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. Value — Returns the value of specified attribute. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexRIO LabVIEW Host VIs

Parent topic:

FlexRIO_Host_QueryAttribute VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-queryattribute-vi.html language=enus -->
## TOPIC 00320: FlexRIO_Host_QueryAttribute VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-queryattribute-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-queryattribute-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this VI to query the current value of the selected attribute. icon

### FlexRIO_Host_QueryAttribute VI

Use this VI to query the current value of the selected attribute.

[IMAGE alt='icon' src='flexrio-host-queryattribute-vi.png']

- [FlexRIO_Host_QueryAttribute_Bool VI](../../../vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-queryattribute-bool-vi.html) Queries the current value of the selected attribute.
- [FlexRIO_Host_QueryAttribute_U32 VI](../../../vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-queryattribute-u32-vi.html) Queries the current value of the selected attribute.

Parent topic:

FlexRIO LabVIEW Host VIs

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-queryiomodid-vi.html language=enus -->
## TOPIC 00321: FlexRIO_Host_QueryIOModID VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-queryiomodid-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-queryiomodid-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the IO Module ID from the EEPROM of the adapter module that is currently connected. icon Inputs/Outputs cdaqmxscale.png RIO Device cerrcodeclst.png error in (no error) error in can accept error information wired from VIs previously called. Use this information to decide if any functionality sh

### FlexRIO_Host_QueryIOModID VI

Reads the IO Module ID from the EEPROM of the adapter module that is currently connected.

[IMAGE alt='icon' src='flexrio-host-queryiomodid-vi.png']

#### Inputs/Outputs

| RIO Device — error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. RIO Device out — IO Module ID — error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexRIO LabVIEW Host VIs

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-queryiomodmgrstate-vi.html language=enus -->
## TOPIC 00322: FlexRIO_Host_QueryIOModMgrState VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-queryiomodmgrstate-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-queryiomodmgrstate-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the current state of the adapter module manager. icon Inputs/Outputs cdaqmxscale.png RIO Device Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MA

### FlexRIO_Host_QueryIOModMgrState VI

Queries the current state of the adapter module manager.

[IMAGE alt='icon' src='flexrio-host-queryiomodmgrstate-vi.png']

#### Inputs/Outputs

| RIO Device — Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. RIO Device out — Returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. State — Returns the current state of the adapter module. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexRIO LabVIEW Host VIs

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-redetectiomod-vi.html language=enus -->
## TOPIC 00323: FlexRIO_Host_RedetectIOMod VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-redetectiomod-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-redetectiomod-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Redetects the adapter module that is currently connected to the selected FlexRIO device. icon Inputs/Outputs cdaqmxscale.png RIO Device Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measu

### FlexRIO_Host_RedetectIOMod VI

Redetects the adapter module that is currently connected to the selected FlexRIO device.

[IMAGE alt='icon' src='flexrio-host-redetectiomod-vi.png']

#### Inputs/Outputs

| RIO Device — Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. RIO Device out — Returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexRIO LabVIEW Host VIs

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-setdeviceshutdownlimit-vi.html language=enus -->
## TOPIC 00324: FlexRIO_Host_SetDeviceShutdownLimit VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-setdeviceshutdownlimit-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-setdeviceshutdownlimit-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this VI to set the device's thermal shutdown limit. icon Inputs/Outputs cdaqmxscale.png RIO Device Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX

### FlexRIO_Host_SetDeviceShutdownLimit VI

Use this VI to set the device's thermal shutdown limit.

[IMAGE alt='icon' src='flexrio-host-setdeviceshutdownlimit-vi.png']

#### Inputs/Outputs

| RIO Device — Specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). Shutdown Type — Description - specifies what type of shutdown to configure. Valid values: Thermal, Total Power, 3.3V Power, 12V Power Value in deg C or mW — Specifies the device's thermal shutdown limit. If you specified Thermal in Shutdown Type, this value is specified in °C. If you specified Total Power, 3.3V Power or 12V Power in Shutdown Type, this value is specified in mW. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. RIO Device out — Returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexRIO LabVIEW Host VIs
