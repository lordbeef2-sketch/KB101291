# NI DOCUMENT BUNDLE: ni-hsdio-properties

<!--NI_BUNDLE_CHUNK bundle=ni-hsdio-properties start=1 end=27 -->
<!--NI_TOPIC bundle=ni-hsdio-properties path=hsdiopropref/pnihsdio_ppmucapableioswitch.html language=enus -->
## TOPIC 00001: Advanced:Device:PPMU-Capable I/O Switch Property

- bundle_id: `ni-hsdio-properties`
- source_path: `hsdiopropref/pnihsdio_ppmucapableioswitch.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-properties/raw/resource/enus/hsdiopropref/pnihsdio_ppmucapableioswitch.html
- document_id: `ni-hsdio-properties`
- page_type: `leaf`
- content_type: ``

### Advanced:Device:PPMU-Capable I/O Switch Property

**Short Name:**PPMU-Capable I/O Switch

Property of [niHSDIO](cnihsdio.html)

Connects or disconnects, on the fly, all PPMU-capable channels on the DDC connector from the internal device pins. If you set this property to
 **Disconnect**, the PPMU-capable channels remain disconnected from the internal device pins until one of the following conditions occurs:

- This property is set to
 Connect 
 .
- The hardware reboots.
- The
 niHSDIO Reset 
 or the
 niHSDIO Reset Device 
 VIs are called.
- Self-calibration completes.

|  | Note This property cannot configure channels on a per pin basis. It always configures all PPMU-capable channels on your device. |
| --- | --- |

|  | Note Only NI 6555/6556 devices support this property. |
| --- | --- |

| Connect (98) | Connects the internal device pins to the DDC connector pins across all PPMU-capable channels. This is the default value. |
| --- | --- |
| Disconnect (99) | Disconnects the internal device pins from the DDC connector pins across all PPMU-capable channels. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-hsdio-properties path=hsdiopropref/pnihsdio_preferredpacketsize.html language=enus -->
## TOPIC 00002: Advanced:Preferred Packet Size Property

- bundle_id: `ni-hsdio-properties`
- source_path: `hsdiopropref/pnihsdio_preferredpacketsize.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-properties/raw/resource/enus/hsdiopropref/pnihsdio_preferredpacketsize.html
- document_id: `ni-hsdio-properties`
- page_type: `leaf`
- content_type: ``

### Advanced:Preferred Packet Size Property

**Short Name:**Preferred Packet Size

Property of [niHSDIO](cnihsdio.html)

Specifies the preferred size of the data field in the PCI Express packet. In general, the larger the packet size, the more efficiently the device uses the bus. However, some systems, because of their implementation, perform better with smaller packet sizes. The value of this property must be a power of two (2, 4, ..., 512).

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-hsdio-properties path=hsdiopropref/pnihsdio_rdyforadvanceevent.activelvl.html language=enus -->
## TOPIC 00003: Events:Ready For Advance:Active Level Property

- bundle_id: `ni-hsdio-properties`
- source_path: `hsdiopropref/pnihsdio_rdyforadvanceevent.activelvl.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-properties/raw/resource/enus/hsdiopropref/pnihsdio_rdyforadvanceevent.activelvl.html
- document_id: `ni-hsdio-properties`
- page_type: `leaf`
- content_type: ``

### Events:Ready For Advance:Active Level Property

**Short Name:**RdyForAdvanceEvent.ActiveLvl

Property of [niHSDIO](cnihsdio.html)

Specifies the output polarity of the Ready for Advance Event.

| Active high (10) | The exported signal is low level while the event is deasserted. A high pulse occurs when the event asserts. |
| --- | --- |
| Active low (11) | The exported signal is high level while the event is deasserted. A low pulse occurs when the event asserts. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-hsdio-properties path=hsdiopropref/pnihsdio_rdyforadvanceevent.outputterm.html language=enus -->
## TOPIC 00004: Events:Ready For Advance:Output Terminal Property

- bundle_id: `ni-hsdio-properties`
- source_path: `hsdiopropref/pnihsdio_rdyforadvanceevent.outputterm.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-properties/raw/resource/enus/hsdiopropref/pnihsdio_rdyforadvanceevent.outputterm.html
- document_id: `ni-hsdio-properties`
- page_type: `leaf`
- content_type: ``

### Events:Ready For Advance:Output Terminal Property

**Short Name:**RdyForAdvanceEvent.OutputTerm

Property of [niHSDIO](cnihsdio.html)

Specifies the destination terminal for the Ready for Advance Event. Event voltages and positions are relevant only if the destination of the event is a front panel connector.

| None | The signal is not exported. |
| --- | --- |
| PFI0 | PFI 0 on the front panel connector. |
| PFI1 | PFI 1 on the front panel DDC connector. |
| PFI2 | PFI 2 on the front panel DDC connector. |
| PFI3 | PFI 3 on the front panel DDC connector. |
| PFI24 | PFI 24 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| PFI25 | PFI 25 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| PFI26 | PFI 26 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| PFI27 | PFI 27 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| PFI28 | PFI 28 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| PFI29 | PFI 29 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| PFI30 | PFI 30 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| PFI31 | PFI 31 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| PXI_Trig0 | PXI trigger line 0. This selection is available only for PXI devices. |
| PXI_Trig1 | PXI trigger line 1. This selection is available only for PXI devices. |
| PXI_Trig2 | PXI trigger line 2. This selection is available only for PXI devices. |
| PXI_Trig3 | PXI trigger line 3. This selection is available only for PXI devices. |
| PXI_Trig4 | PXI trigger line 4. This selection is available only for PXI devices. |
| PXI_Trig5 | PXI trigger line 5. This selection is available only for PXI devices. |
| PXI_Trig6 | PXI trigger line 6. This selection is available only for PXI devices. |
| PXI_Trig7 | PXI trigger line 7. This selection is available only for PXI devices. |
| RTSI0 | RTSI trigger line 0. This selection is available only for PCI devices. |
| RTSI1 | RTSI trigger line 1. This selection is available only for PCI devices. |
| RTSI2 | RTSI trigger line 2. This selection is available only for PCI devices. |
| RTSI3 | RTSI trigger line 3. This selection is available only for PCI devices. |
| RTSI4 | RTSI trigger line 4. This selection is available only for PCI devices. |
| RTSI5 | RTSI trigger line 5. This selection is available only for PCI devices. |
| RTSI6 | RTSI trigger line 6. This selection is available only for PCI devices. |
| RTSI7 | RTSI trigger line 7. This selection is available only for PCI devices. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niHSDIO Export Signal |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-hsdio-properties path=hsdiopropref/pnihsdio_rdyforadvanceevent.termconfig.html language=enus -->
## TOPIC 00005: Events:Ready For Advance:Terminal Configuration Property

- bundle_id: `ni-hsdio-properties`
- source_path: `hsdiopropref/pnihsdio_rdyforadvanceevent.termconfig.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-properties/raw/resource/enus/hsdiopropref/pnihsdio_rdyforadvanceevent.termconfig.html
- document_id: `ni-hsdio-properties`
- page_type: `leaf`
- content_type: ``

### Events:Ready For Advance:Terminal Configuration Property

**Short Name:**RdyForAdvanceEvent.TermConfig

Property of [niHSDIO](cnihsdio.html)

Specifies whether the Ready for Advance event terminal is configured for single-ended or LVDS operation. Valid values for this property vary by device. Refer to your device documentation to determine if your hardware supports LVDS operation.

| LVDS (64) | The terminal is configured for LVDS operation. |
| --- | --- |
| Single-Ended (65) | The terminal is configured for single-ended operation. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-hsdio-properties path=hsdiopropref/pnihsdio_rdyforstartevent.activelvl.html language=enus -->
## TOPIC 00006: Events:Ready For Start:Active Level Property

- bundle_id: `ni-hsdio-properties`
- source_path: `hsdiopropref/pnihsdio_rdyforstartevent.activelvl.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-properties/raw/resource/enus/hsdiopropref/pnihsdio_rdyforstartevent.activelvl.html
- document_id: `ni-hsdio-properties`
- page_type: `leaf`
- content_type: ``

### Events:Ready For Start:Active Level Property

**Short Name:**RdyForStartEvent.ActiveLvl

Property of [niHSDIO](cnihsdio.html)

Specifies the output polarity of the Ready for Start Event.

| Active high (10) | The exported signal is low level while the event is deasserted. A high pulse occurs when the event asserts. |
| --- | --- |
| Active low (11) | The exported signal is high level while the event is deasserted. A low pulse occurs when the event asserts. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-hsdio-properties path=hsdiopropref/pnihsdio_rdyforstartevent.outputterm.html language=enus -->
## TOPIC 00007: Events:Ready For Start:Output Terminal Property

- bundle_id: `ni-hsdio-properties`
- source_path: `hsdiopropref/pnihsdio_rdyforstartevent.outputterm.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-properties/raw/resource/enus/hsdiopropref/pnihsdio_rdyforstartevent.outputterm.html
- document_id: `ni-hsdio-properties`
- page_type: `leaf`
- content_type: ``

### Events:Ready For Start:Output Terminal Property

**Short Name:**RdyForStartEvent.OutputTerm

Property of [niHSDIO](cnihsdio.html)

Specifies the destination terminal for the Ready for Start Event. Event voltages and positions are relevant only if the destination of the event is a front panel connector.

| None | The signal is not exported. |
| --- | --- |
| PFI0 | PFI 0 on the front panel connector. |
| PFI1 | PFI 1 on the front panel DDC connector. |
| PFI2 | PFI 2 on the front panel DDC connector. |
| PFI3 | PFI 3 on the front panel DDC connector. |
| PFI24 | PFI 24 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| PFI25 | PFI 25 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| PFI26 | PFI 26 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| PFI27 | PFI 27 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| PFI28 | PFI 28 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| PFI29 | PFI 29 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| PFI30 | PFI 30 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| PFI31 | PFI 31 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| PXI_Trig0 | PXI trigger line 0. This selection is available only for PXI devices. |
| PXI_Trig1 | PXI trigger line 1. This selection is available only for PXI devices. |
| PXI_Trig2 | PXI trigger line 2. This selection is available only for PXI devices. |
| PXI_Trig3 | PXI trigger line 3. This selection is available only for PXI devices. |
| PXI_Trig4 | PXI trigger line 4. This selection is available only for PXI devices. |
| PXI_Trig5 | PXI trigger line 5. This selection is available only for PXI devices. |
| PXI_Trig6 | PXI trigger line 6. This selection is available only for PXI devices. |
| PXI_Trig7 | PXI trigger line 7. This selection is available only for PXI devices. |
| RTSI0 | RTSI trigger line 0. This selection is available only for PCI devices. |
| RTSI1 | RTSI trigger line 1. This selection is available only for PCI devices. |
| RTSI2 | RTSI trigger line 2. This selection is available only for PCI devices. |
| RTSI3 | RTSI trigger line 3. This selection is available only for PCI devices. |
| RTSI4 | RTSI trigger line 4. This selection is available only for PCI devices. |
| RTSI5 | RTSI trigger line 5. This selection is available only for PCI devices. |
| RTSI6 | RTSI trigger line 6. This selection is available only for PCI devices. |
| RTSI7 | RTSI trigger line 7. This selection is available only for PCI devices. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-hsdio-properties path=hsdiopropref/pnihsdio_rdyforstartevent.termconfig.html language=enus -->
## TOPIC 00008: Events:Ready For Start:Terminal Configuration Property

- bundle_id: `ni-hsdio-properties`
- source_path: `hsdiopropref/pnihsdio_rdyforstartevent.termconfig.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-properties/raw/resource/enus/hsdiopropref/pnihsdio_rdyforstartevent.termconfig.html
- document_id: `ni-hsdio-properties`
- page_type: `leaf`
- content_type: ``

### Events:Ready For Start:Terminal Configuration Property

**Short Name:**RdyForStartEvent.TermConfig

Property of [niHSDIO](cnihsdio.html)

Specifies whether the Ready for Start event terminal is configured for single-ended or LVDS operation. Valid values for this property vary by device. Refer to your device documentation to determine if your hardware supports LVDS operation.

| LVDS (64) | The terminal is configured for LVDS operation. |
| --- | --- |
| Single-Ended (65) | The terminal is configured for single-ended operation. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-hsdio-properties path=hsdiopropref/pnihsdio_recordsdone.html language=enus -->
## TOPIC 00009: Dynamic Acquisition:Fetch:Records Done Property

- bundle_id: `ni-hsdio-properties`
- source_path: `hsdiopropref/pnihsdio_recordsdone.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-properties/raw/resource/enus/hsdiopropref/pnihsdio_recordsdone.html
- document_id: `ni-hsdio-properties`
- page_type: `leaf`
- content_type: ``

### Dynamic Acquisition:Fetch:Records Done Property

**Short Name:**RecordsDone

Property of [niHSDIO](cnihsdio.html)

Returns the number of records that have been acquired.

**Related Topics**

- Records
- Dynamic Acquisition Triggers and Events

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-hsdio-properties path=hsdiopropref/pnihsdio_refclk.rate.html language=enus -->
## TOPIC 00010: Timing:Ref Clock:Rate Property

- bundle_id: `ni-hsdio-properties`
- source_path: `hsdiopropref/pnihsdio_refclk.rate.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-properties/raw/resource/enus/hsdiopropref/pnihsdio_refclk.rate.html
- document_id: `ni-hsdio-properties`
- page_type: `leaf`
- content_type: ``

### Timing:Ref Clock:Rate Property

**Short Name:**RefClk.Rate

Property of [niHSDIO](cnihsdio.html)

Specifies the Reference clock rate, expressed in Hertz.
This property is ignored when the
 [Reference Clock Source](pnihsdio_refclk.source.html)
 property is set to
 None
 .

Valid values for NI 6544/6545/6547/6548/6555/6556 devices are from 5 MHz to 100 MHz in 1 MHz steps. All other high-speed digital devices support only 10 MHz as a valid value.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niHSDIO Configure Ref Clock |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-hsdio-properties path=hsdiopropref/pnihsdio_refclk.source.html language=enus -->
## TOPIC 00011: Timing:Ref Clock:Source Property

- bundle_id: `ni-hsdio-properties`
- source_path: `hsdiopropref/pnihsdio_refclk.source.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-properties/raw/resource/enus/hsdiopropref/pnihsdio_refclk.source.html
- document_id: `ni-hsdio-properties`
- page_type: `leaf`
- content_type: ``

### Timing:Ref Clock:Source Property

**Short Name:**RefClk.Source

Property of [niHSDIO](cnihsdio.html)

Specifies the Reference clock source.

| None | The device does not use a Reference clock. |
| --- | --- |
| ClkIn | The device uses the clock present at the front panel CLK IN connector. |
| PXI_CLK | The device chooses between the PXI_CLK10 and PXIe_CLK100 signals, which are present on the backplane. |
| RTSI7 | The device uses the signal present on RTSI trigger line 7. This selection is valid only for PCI devices. |
| PXIe_DStarA | The device uses the PXIe_DStarA signal present on the PXI Express backplane as the Sample clock source. This selection is valid only for NI 6555/6556 devices. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niHSDIO Configure Ref Clock |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-hsdio-properties path=hsdiopropref/pnihsdio_refclockimpedance.html language=enus -->
## TOPIC 00012: Timing:Ref Clock:Impedance Property

- bundle_id: `ni-hsdio-properties`
- source_path: `hsdiopropref/pnihsdio_refclockimpedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-properties/raw/resource/enus/hsdiopropref/pnihsdio_refclockimpedance.html
- document_id: `ni-hsdio-properties`
- page_type: `leaf`
- content_type: ``

### Timing:Ref Clock:Impedance Property

**Short Name:**RefClk.Impedance

Property of [niHSDIO](cnihsdio.html)

Specifies the input impedance of the Reference clock when it is supplied through the device front panel. This property is expressed in ohms.

Valid values are 50 or 1000.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-hsdio-properties path=hsdiopropref/pnihsdio_reftorefholdoff.html language=enus -->
## TOPIC 00013: Triggers:Ref:Advanced: Reference to Reference Trigger Holdoff Property

- bundle_id: `ni-hsdio-properties`
- source_path: `hsdiopropref/pnihsdio_reftorefholdoff.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-properties/raw/resource/enus/hsdiopropref/pnihsdio_reftorefholdoff.html
- document_id: `ni-hsdio-properties`
- page_type: `leaf`
- content_type: ``

### Triggers:Ref:Advanced: Reference to Reference Trigger Holdoff Property

**Short Name:**RefToRefHoldoff

Property of [niHSDIO](cnihsdio.html)

Specifies the amount of time, in seconds, until the next record's Reference trigger is recognized.

This property is especially useful when you want each device in a multidevice situation to recognize the Reference trigger at the same time, though the Reference trigger is shared among devices and each device has a different record size.

This property is valid only for acquisition sessions.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-hsdio-properties path=hsdiopropref/pnihsdio_reftrig.digedge.edge.html language=enus -->
## TOPIC 00014: Triggers:Ref:Digital Edge:Edge Property

- bundle_id: `ni-hsdio-properties`
- source_path: `hsdiopropref/pnihsdio_reftrig.digedge.edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-properties/raw/resource/enus/hsdiopropref/pnihsdio_reftrig.digedge.edge.html
- document_id: `ni-hsdio-properties`
- page_type: `leaf`
- content_type: ``

### Triggers:Ref:Digital Edge:Edge Property

**Short Name:**RefTrig.DigEdge.Edge

Property of [niHSDIO](cnihsdio.html)

Specifies the active edge for the Reference trigger. This property is used when the
 [Reference Trigger Type](pnihsdio_reftrig.type.html)
 property is set to
 **Digital edge**
 .

This property is valid only for acquisition sessions.

| Rising edge (12) | Rising-edge trigger. |
| --- | --- |
| Falling edge (13) | Falling-edge trigger. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-hsdio-properties path=hsdiopropref/pnihsdio_reftrig.digedge.impedance.html language=enus -->
## TOPIC 00015: Triggers:Ref:Digital Edge:Impedance Property

- bundle_id: `ni-hsdio-properties`
- source_path: `hsdiopropref/pnihsdio_reftrig.digedge.impedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-properties/raw/resource/enus/hsdiopropref/pnihsdio_reftrig.digedge.impedance.html
- document_id: `ni-hsdio-properties`
- page_type: `leaf`
- content_type: ``

### Triggers:Ref:Digital Edge:Impedance Property

**Short Name:**RefTrig.DigEdge.Impedance

Property of [niHSDIO](cnihsdio.html)

Specifies the impedance on the channel configured for the digital edge Reference trigger. Valid values for this property vary by device. Refer to your device documentation for more information about the valid impedance settings.

This property is set only if the trigger is configured to use a PFI channel, and it is ignored if the trigger is configured for any other channel.

This property is only valid for acquisition sessions.

| Device | Supported Value |
| --- | --- |
| NI 6541/6542 | 10000 |
| NI 6544/6545/6547/6548 | 50000 |
| NI 6551/6552 | All NI 6551/6552 devices support 50 as a valid impedance value. NI 6551/6552 devices also support either 10000 or 50000 as valid impedance values depending on the revision of your device. Refer to the NI PXI/PCI-6551/6552 Specifications for more information about supported values. |
| NI 6555/6556 | NI 6555/6556 devices do not support this property. |
| NI 656 x | 100 in LVDS terminal configuration or 10000 in single-ended terminal configuration |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-hsdio-properties path=hsdiopropref/pnihsdio_reftrig.digedge.position.html language=enus -->
## TOPIC 00016: Triggers:Ref:Digital Edge:Position Property

- bundle_id: `ni-hsdio-properties`
- source_path: `hsdiopropref/pnihsdio_reftrig.digedge.position.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-properties/raw/resource/enus/hsdiopropref/pnihsdio_reftrig.digedge.position.html
- document_id: `ni-hsdio-properties`
- page_type: `leaf`
- content_type: ``

### Triggers:Ref:Digital Edge:Position Property

**Short Name:**RefTrig.DigEdge.Position

Property of [niHSDIO](cnihsdio.html)

Specifies the position where the Reference trigger is latched, relative to the Sample clock. Trigger voltages and positions are only relevant if the trigger source is a front panel connector.

This property is only valid for acquisition sessions.

| Sample clock rising edge (18) | The device asserts the Reference trigger on the Sample clock rising edge. |
| --- | --- |
| Sample clock falling edge (19) | The device asserts the Reference trigger on the Sample clock falling edge. |
| Delay from sample clock rising edge (20) | The device asserts the Reference trigger with a delay from the Sample clock rising edge. Specify the delay using the Data Position Delay property. This choice has more jitter than the rising or falling edge values. Certain devices have Sample clock frequency limitations on when a custom delay can be used. Refer to the device documentation for more information about these limitations. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-hsdio-properties path=hsdiopropref/pnihsdio_reftrig.digedge.termconfig.html language=enus -->
## TOPIC 00017: Triggers:Ref:Digital Edge:Terminal Configuration Property

- bundle_id: `ni-hsdio-properties`
- source_path: `hsdiopropref/pnihsdio_reftrig.digedge.termconfig.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-properties/raw/resource/enus/hsdiopropref/pnihsdio_reftrig.digedge.termconfig.html
- document_id: `ni-hsdio-properties`
- page_type: `leaf`
- content_type: ``

### Triggers:Ref:Digital Edge:Terminal Configuration Property

**Short Name:**RefTrig.DigEdge.TermConfig

Property of [niHSDIO](cnihsdio.html)

Specifies whether the Reference trigger terminal is configured for single-ended or LVDS operation. Valid values for this property vary by device. Refer to your device documentation to determine if your hardware supports LVDS operation.

This property is only valid for acquisition sessions.

| LVDS (64) | The terminal is configured for LVDS operation. |
| --- | --- |
| Single-Ended (65) | The terminal is configured for single-ended operation. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-hsdio-properties path=hsdiopropref/pnihsdio_reftrig.patmatch.trigwhen.html language=enus -->
## TOPIC 00018: Triggers:Ref:Pattern Match:Trigger When Property

- bundle_id: `ni-hsdio-properties`
- source_path: `hsdiopropref/pnihsdio_reftrig.patmatch.trigwhen.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-properties/raw/resource/enus/hsdiopropref/pnihsdio_reftrig.patmatch.trigwhen.html
- document_id: `ni-hsdio-properties`
- page_type: `leaf`
- content_type: ``

### Triggers:Ref:Pattern Match:Trigger When Property

**Short Name:**RefTrig.PatMatch.TrigWhen

Property of [niHSDIO](cnihsdio.html)

Specifies whether a pattern match Reference trigger asserts when a particular pattern is matched or not matched.

This property is valid only for acquisition sessions.

| Pattern matches (36) | The trigger asserts when the pattern matches. |
| --- | --- |
| Pattern does not match (37) | The trigger asserts when the pattern does not match. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niHSDIO Configure Trigger |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-hsdio-properties path=hsdiopropref/pnihsdio_reftrig.pretrigsamples.html language=enus -->
## TOPIC 00019: Triggers:Ref:Pretrigger Samples Per Record Property

- bundle_id: `ni-hsdio-properties`
- source_path: `hsdiopropref/pnihsdio_reftrig.pretrigsamples.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-properties/raw/resource/enus/hsdiopropref/pnihsdio_reftrig.pretrigsamples.html
- document_id: `ni-hsdio-properties`
- page_type: `leaf`
- content_type: ``

### Triggers:Ref:Pretrigger Samples Per Record Property

**Short Name:**RefTrig.PretrigSamples

Property of [niHSDIO](cnihsdio.html)

Specifies the number of pretrigger samples, which are the samples acquired before the Reference trigger is received, to be acquired per record. The number of pretrigger samples cannot be greater than the value of the Samples Per Record property.

This property is valid only for acquisition sessions.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-hsdio-properties path=hsdiopropref/pnihsdio_reftrig.type.html language=enus -->
## TOPIC 00020: Triggers:Ref:Type Property

- bundle_id: `ni-hsdio-properties`
- source_path: `hsdiopropref/pnihsdio_reftrig.type.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-properties/raw/resource/enus/hsdiopropref/pnihsdio_reftrig.type.html
- document_id: `ni-hsdio-properties`
- page_type: `leaf`
- content_type: ``

### Triggers:Ref:Type Property

**Short Name:**RefTrig.Type

Property of [niHSDIO](cnihsdio.html)

Specifies the Reference trigger type. Depending on this property value, more properties may need to be set to fully configure the trigger.

This property is valid only for acquisition sessions.

| None (28) | The device does not use a Reference trigger. |
| --- | --- |
| Digital edge (29) | The trigger asserts on the digital edge of an input signal. The source of the digital edge is specified with the Reference Trigger Digital Edge Source property, and the active edge is specified with Reference Trigger Digital Edge Edge property. |
| Software (32) | The trigger does not assert until a software trigger occurs. You can assert the software trigger by calling the niHSDIO Send Software Edge Trigger VI and selecting Reference Trigger as the trigger parameter. |
| Pattern match (31) | The data operation does not take effect until a specific data pattern matching condition is met. Configure the condition by setting the Reference Trigger Pattern Match and Reference Trigger Pattern Match When properties. This value is valid only for acquisition sessions. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niHSDIO Configure Trigger |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-hsdio-properties path=hsdiopropref/pnihsdio_reftrigdigedge.source.html language=enus -->
## TOPIC 00021: Triggers:Ref:Digital Edge:Source Property

- bundle_id: `ni-hsdio-properties`
- source_path: `hsdiopropref/pnihsdio_reftrigdigedge.source.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-properties/raw/resource/enus/hsdiopropref/pnihsdio_reftrigdigedge.source.html
- document_id: `ni-hsdio-properties`
- page_type: `leaf`
- content_type: ``

### Triggers:Ref:Digital Edge:Source Property

**Short Name:**RefTrig:DigEdge.Source

Property of [niHSDIO](cnihsdio.html)

Specifies the source terminal for the Reference trigger. This property is used only when the
 [Reference Trigger Type](pnihsdio_reftrig.type.html)
 property is set to
 **Digital edge**
 .

This property is valid only for acquisition sessions.

| PFI0 | PFI 0 on the front panel connector. |
| --- | --- |
| PFI1 | PFI 1 on the front panel DDC connector. |
| PFI2 | PFI 2 on the front panel DDC connector. |
| PFI3 | PFI 3 on the front panel DDC connector. |
| PFI24 | PFI 24 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| PFI25 | PFI 25 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| PFI26 | PFI 26 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| PFI27 | PFI 27 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| PFI28 | PFI 28 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| PFI29 | PFI 29 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| PFI30 | PFI 30 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| PFI31 | PFI 31 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| PXI_Trig0 | PXI trigger line 0. This selection is available only for PXI devices. |
| PXI_Trig1 | PXI trigger line 1. This selection is available only for PXI devices. |
| PXI_Trig2 | PXI trigger line 2. This selection is available only for PXI devices. |
| PXI_Trig3 | PXI trigger line 3. This selection is available only for PXI devices. |
| PXI_Trig4 | PXI trigger line 4. This selection is available only for PXI devices. |
| PXI_Trig5 | PXI trigger line 5. This selection is available only for PXI devices. |
| PXI_Trig6 | PXI trigger line 6. This selection is available only for PXI devices. |
| PXI_Trig7 | PXI trigger line 7. This selection is available only for PXI devices. |
| RTSI0 | RTSI trigger line 0. This selection is available only for PCI devices. |
| RTSI1 | RTSI trigger line 1. This selection is available only for PCI devices. |
| RTSI2 | RTSI trigger line 2. This selection is available only for PCI devices. |
| RTSI3 | RTSI trigger line 3. This selection is available only for PCI devices. |
| RTSI4 | RTSI trigger line 4. This selection is available only for PCI devices. |
| RTSI5 | RTSI trigger line 5. This selection is available only for PCI devices. |
| RTSI6 | RTSI trigger line 6. This selection is available only for PCI devices. |
| RTSI7 | RTSI trigger line 7. This selection is available only for PCI devices. |
| PXI_STAR | The device uses the PXI_STAR signal, which is present on the PXI backplane. This selection is valid only for PXI devices in slots other than Slot 2. |
| PXIe_DStarB | The device uses the PXIe_DStarB signal, which is present on the PXI Express backplane. This selection is valid only for NI 6555/6556 devices. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-hsdio-properties path=hsdiopropref/pnihsdio_reftrigpatmatchpattern.html language=enus -->
## TOPIC 00022: Triggers:Ref:Pattern Match:Pattern Property

- bundle_id: `ni-hsdio-properties`
- source_path: `hsdiopropref/pnihsdio_reftrigpatmatchpattern.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-properties/raw/resource/enus/hsdiopropref/pnihsdio_reftrigpatmatchpattern.html
- document_id: `ni-hsdio-properties`
- page_type: `leaf`
- content_type: ``

### Triggers:Ref:Pattern Match:Pattern Property

**Short Name:**RefTrig:PatMatch:Pattern

Property of [niHSDIO](cnihsdio.html)

Sets the pattern match mask for the Reference trigger. This property is used when the
 [Reference Trigger Type](pnihsdio_reftrig.type.html)
 property is set to
 **Pattern match**
 .

The pattern is a string of characters representing the entire pattern to be matched on. Each character corresponds to a particular channel.

- 'X' or 'x': Match on any value
- '1': Match on a logic 1
- '0': Match on a logic 0
- 'R' or 'r': Match on a rising edge
- 'F' or 'f': Match on a falling edge
- 'E' or 'e': Match on either edge
- Spaces are ignored, and are useful for readability to segment long patterns

The rightmost character in the expression corresponds to the lowest numbered physical channel.
Ex. 'XXXX XXXX XXXX 1111 1100' specifies to match when channels 0 and 1 are '0' and channels 2-7 are '1'.
The values seen by pattern matching are affected by the
 [Data Interpretation](pnihsdio_datainterpretation.html)
 property.

This property is only valid for acquisition sessions.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niHSDIO Configure Trigger |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-hsdio-properties path=hsdiopropref/pnihsdio_repeatcount.html language=enus -->
## TOPIC 00023: Dynamic Generation:Repeat Count Property

- bundle_id: `ni-hsdio-properties`
- source_path: `hsdiopropref/pnihsdio_repeatcount.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-properties/raw/resource/enus/hsdiopropref/pnihsdio_repeatcount.html
- document_id: `ni-hsdio-properties`
- page_type: `leaf`
- content_type: ``

### Dynamic Generation:Repeat Count Property

**Short Name:**RepeatCount

Property of [niHSDIO](cnihsdio.html)

Specifies how many times to generate the waveform specified by the
 [Waveform To Generate](pnihsdio_waveformtogenerate.html)
 property. This property is valid only when the
 [Repeat Mode](pnihsdio_repeatmode.html)
 property is set to
 **Finite**
 ; it is not used when the
 [Repeat Mode](pnihsdio_repeatmode.html)
 property is set to
 **Continuous**
 . This property is valid only when the
 [Generation Mode](pnihsdio_generationmode.html)
 property is set to
 **Waveform**
 . It is ignored if you set the
 [Generation Mode](pnihsdio_generationmode.html)
 property to
 **Scripted**
 .

This property is valid only for generation sessions.

**Related Topics**

- Generating Data in Single-Waveform Mode

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niHSDIO Configure Generation Repeat |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-hsdio-properties path=hsdiopropref/pnihsdio_repeatmode.html language=enus -->
## TOPIC 00024: Dynamic Generation:Repeat Mode Property

- bundle_id: `ni-hsdio-properties`
- source_path: `hsdiopropref/pnihsdio_repeatmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-properties/raw/resource/enus/hsdiopropref/pnihsdio_repeatmode.html
- document_id: `ni-hsdio-properties`
- page_type: `leaf`
- content_type: ``

### Dynamic Generation:Repeat Mode Property

**Short Name:**RepeatMode

Property of [niHSDIO](cnihsdio.html)

Specifies whether to generate a single waveform a finite number of times or continuously. This property is valid only when the
 [Generation Mode](pnihsdio_generationmode.html)
 property is set to
 **Waveform**
 ; it is not used if you select
 **Scripted**
 .

If this property is set to
 **Finite**
 , use the
 [Repeat Count](pnihsdio_repeatcount.html)
 property to specify how many times the named waveform is generated.

This property is valid only for generation sessions.

**Related Topics**

- Generating Data in Single-Waveform Mode

| Finite (16) | Calling the niHSDIO Initiate VI generates the named waveform a finite number of times. The number to repeat is defined by the Repeat Count property. |
| --- | --- |
| Continuous (17) | Calling niHSDIO Init Generation Session VI generates the named waveform continuously (until the niHSDIO Abort VI is called). |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niHSDIO Configure Generation Repeat |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-hsdio-properties path=hsdiopropref/pnihsdio_samplesperrecordisfinite.html language=enus -->
## TOPIC 00025: Dynamic Acquisition:Samples Per Record Is Finite Property

- bundle_id: `ni-hsdio-properties`
- source_path: `hsdiopropref/pnihsdio_samplesperrecordisfinite.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-properties/raw/resource/enus/hsdiopropref/pnihsdio_samplesperrecordisfinite.html
- document_id: `ni-hsdio-properties`
- page_type: `leaf`
- content_type: ``

### Dynamic Acquisition:Samples Per Record Is Finite Property

**Short Name:**SamplesPerRecordIsFinite

Property of [niHSDIO](cnihsdio.html)

Specifies whether the configured samples per record is finite (TRUE) or infinite (FALSE).

This property is valid only for acquisition sessions.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-hsdio-properties path=hsdiopropref/pnihsdio_sampsperrecord.html language=enus -->
## TOPIC 00026: Dynamic Acquisition:Samples Per Record Property

- bundle_id: `ni-hsdio-properties`
- source_path: `hsdiopropref/pnihsdio_sampsperrecord.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-properties/raw/resource/enus/hsdiopropref/pnihsdio_sampsperrecord.html
- document_id: `ni-hsdio-properties`
- page_type: `leaf`
- content_type: ``

### Dynamic Acquisition:Samples Per Record Property

**Short Name:**SampsPerRecord

Property of [niHSDIO](cnihsdio.html)

Specifies the number of samples to be acquired per record. If you are using a Reference trigger, this number includes both pretrigger and posttrigger samples.

This property is only valid for acquisition sessions.

**Related Topics**

- Dynamic Acquisition

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niHSDIO Configure Acquisition Size |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-hsdio-properties path=hsdiopropref/pnihsdio_scripttogenerate.html language=enus -->
## TOPIC 00027: Dynamic Generation:Script To Generate Property

- bundle_id: `ni-hsdio-properties`
- source_path: `hsdiopropref/pnihsdio_scripttogenerate.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-properties/raw/resource/enus/hsdiopropref/pnihsdio_scripttogenerate.html
- document_id: `ni-hsdio-properties`
- page_type: `leaf`
- content_type: ``

### Dynamic Generation:Script To Generate Property

**Short Name:**ScriptToGenerate

Property of [niHSDIO](cnihsdio.html)

Specifies which script in onboard memory is generated upon calling the
 [niHSDIO Initiate](/csh?topicname=hsdioviref/hsdio_initiate.html)
 VI when the
 [Generation Mode](pnihsdio_generationmode.html)
 property is set to
 **Scripted**
 . If this property is not set to a valid script and more than one script is in onboard memory, you receive an error after calling the niHSDIO Initiate VI. If only one script is in onboard memory and this property is set to
 ""
 (empty string), then that script is generated upon calling the niHSDIO Initiate VI.

This property is ignored when the
 [Generation Mode](pnihsdio_generationmode.html)
 property is set to
 **Waveform**
 , since the
 [Waveform to Generate](pnihsdio_waveformtogenerate.html)
 property defines which waveform to generate.

This property is valid only for generation sessions.

**Related Topics**

- Writing Waveforms to Your Device

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niHSDIO Configure Script To Generate |
| Channel-based | No |
| Resettable | No |
