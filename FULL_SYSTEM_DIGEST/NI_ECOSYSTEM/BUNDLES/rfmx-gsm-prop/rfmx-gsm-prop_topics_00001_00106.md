# NI DOCUMENT BUNDLE: rfmx-gsm-prop

<!--NI_BUNDLE_CHUNK bundle=rfmx-gsm-prop start=1 end=106 -->
<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr0.html language=enus -->
## TOPIC 00001: rfmxgsmprop/attr0.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr0.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr0.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Selector String Property

Selector String Property

**Short Name:**Selector String

Property of [RFmxGSM](crfmxgsm.html)

Specifies the selector string used to access all subsequent selector string-based properties in this instance of the property node.

When there are multiple instances of a property, specify the property instance to configure or fetch by using the Selector String property in a property node.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Write Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr400001.html language=enus -->
## TOPIC 00002: rfmxgsmprop/attr400001.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr400001.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr400001.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Center Frequency (Hz) Property

Center Frequency (Hz) Property

**Short Name:**Center Freq (Hz)

Property of [RFmxGSM](crfmxgsm.html)

Specifies the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Frequency, RFmxGSM Configure RF |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr400002.html language=enus -->
## TOPIC 00003: rfmxgsmprop/attr400002.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr400002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr400002.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Reference Level Property

Reference Level Property

**Short Name:**Reference Level

Property of [RFmxGSM](crfmxgsm.html)

Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and V<sub>pk-pk</sub> for baseband devices.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Reference Level, RFmxGSM Configure RF |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr400003.html language=enus -->
## TOPIC 00004: rfmxgsmprop/attr400003.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr400003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr400003.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

External Attenuation (dB) Property

External Attenuation (dB) Property

**Short Name:**External Attenuation (dB)

Property of [RFmxGSM](crfmxgsm.html)

Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the *NI RF Vector Signal Analyzers Help*.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure External Attenuation, RFmxGSM Configure RF |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr400004.html language=enus -->
## TOPIC 00005: rfmxgsmprop/attr400004.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr400004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr400004.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Type Property

Trigger:Type Property

**Short Name:**Trigger Type

Property of [RFmxGSM](crfmxgsm.html)

Specifies the trigger type.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **IQ Power Edge**.

| None (0) | No Reference Trigger is configured. |
| --- | --- |
| Digital Edge (1) | The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the Digital Edge Source property. |
| IQ Power Edge (2) | The Reference Trigger is asserted when the signal changes past the level specified by the slope (rising or falling), which is configured using the IQ Power Edge Slope property. |
| Software (3) | The Reference Trigger is not asserted until a software trigger occurs. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr400005.html language=enus -->
## TOPIC 00006: rfmxgsmprop/attr400005.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr400005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr400005.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Digital Edge:Source Property

Trigger:Digital Edge:Source Property

**Short Name:**Digital Edge Source

Property of [RFmxGSM](crfmxgsm.html)

Specifies the source terminal for the digital edge trigger. This property is used only when you set the [Trigger Type](attr400004.html) property to **Digital Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default of this property is hardware dependent.

| PFI0 (PFI0) | The trigger is received on PFI 0. |
| --- | --- |
| PFI1 (PFI1) | The trigger is received on PFI 1. |
| PXI_Trig0 (PXI_Trig0) | The trigger is received on PXI trigger line 0. |
| PXI_Trig1 (PXI_Trig1) | The trigger is received on PXI trigger line 1. |
| PXI_Trig2 (PXI_Trig2) | The trigger is received on PXI trigger line 2. |
| PXI_Trig3 (PXI_Trig3) | The trigger is received on PXI trigger line 3. |
| PXI_Trig4 (PXI_Trig4) | The trigger is received on PXI trigger line 4. |
| PXI_Trig5 (PXI_Trig5) | The trigger is received on PXI trigger line 5. |
| PXI_Trig6 (PXI_Trig6) | The trigger is received on PXI trigger line 6. |
| PXI_Trig7 (PXI_Trig7) | The trigger is received on PXI trigger line 7. |
| PXI_STAR (PXI_STAR) | The trigger is received on the PXI star trigger line. |
| PXIe_DStarB (PXIe_DStarB) | The trigger is received on the PXIe DStar B trigger line. |
| TimerEvent (TimerEvent) | The trigger is received from the timer event. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr400006.html language=enus -->
## TOPIC 00007: rfmxgsmprop/attr400006.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr400006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr400006.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Digital Edge:Edge Property

Trigger:Digital Edge:Edge Property

**Short Name:**Digital Edge

Property of [RFmxGSM](crfmxgsm.html)

Specifies the active edge for the trigger. This property is used only when you set the [Trigger Type](attr400004.html) property to **Digital Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Rising Edge**.

| Rising Edge (0) | The trigger asserts on the rising edge of the signal. |
| --- | --- |
| Falling Edge (1) | The trigger asserts on the falling edge of the signal. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr400007.html language=enus -->
## TOPIC 00008: rfmxgsmprop/attr400007.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr400007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr400007.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Trigger:IQ Power Edge:Source Property

Trigger:IQ Power Edge:Source Property

**Short Name:**IQ Power Edge Source

Property of [RFmxGSM](crfmxgsm.html)

Specifies the channel from which the device monitors the trigger. This property is used only when you set the [Trigger Type](attr400004.html) property to **IQ Power Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr400008.html language=enus -->
## TOPIC 00009: rfmxgsmprop/attr400008.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr400008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr400008.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Trigger:IQ Power Edge:Level (dB or dBm) Property

Trigger:IQ Power Edge:Level (dB or dBm) Property

**Short Name:**IQ Power Edge Level

Property of [RFmxGSM](crfmxgsm.html)

Specifies the power level at which the device triggers. This value is expressed in dB when you set the [IQ Power Edge Level Type](attr400fff.html) property to **Relative** and in dBm when you set the IQ Power Edge Level Type property to **Absolute**. The device asserts the trigger when the signal exceeds the level specified by the value of this property, taking into consideration the specified slope. This property is used only when you set the [Trigger Type](attr400004.html) property to **IQ Power Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr400009.html language=enus -->
## TOPIC 00010: rfmxgsmprop/attr400009.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr400009.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr400009.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Trigger:IQ Power Edge:Slope Property

Trigger:IQ Power Edge:Slope Property

**Short Name:**IQ Power Edge Slope

Property of [RFmxGSM](crfmxgsm.html)

Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the [IQ Power Edge Level](attr400008.html) property with the slope you specify. This property is used only when you set the [Trigger Type](attr400004.html) property to **IQ Power Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Rising Slope**.

| Rising Slope (0) | The trigger asserts when the signal power is rising. |
| --- | --- |
| Falling Slope (1) | The trigger asserts when the signal power is falling. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40000a.html language=enus -->
## TOPIC 00011: rfmxgsmprop/attr40000a.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40000a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40000a.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Delay (s) Property

Trigger:Delay (s) Property

**Short Name:**Trigger Delay (s)

Property of [RFmxGSM](crfmxgsm.html)

Specifies the trigger delay time. This value is expressed in seconds.

If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40000b.html language=enus -->
## TOPIC 00012: rfmxgsmprop/attr40000b.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40000b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40000b.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Minimum Quiet Time:Mode Property

Trigger:Minimum Quiet Time:Mode Property

**Short Name:**Trigger Min Quiet Time Mode

Property of [RFmxGSM](crfmxgsm.html)

Specifies whether the measurement computes the minimum quiet time used for triggering.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Auto**.

| Manual (0) | The minimum quiet time for triggering is the value of the Trigger Min Quiet Time property. |
| --- | --- |
| Auto (1) | The measurement computes the minimum quiet time used for triggering. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40000c.html language=enus -->
## TOPIC 00013: rfmxgsmprop/attr40000c.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40000c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40000c.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Minimum Quiet Time:Duration (s) Property

Trigger:Minimum Quiet Time:Duration (s) Property

**Short Name:**Trigger Min Quiet Time (s)

Property of [RFmxGSM](crfmxgsm.html)

Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds.

If you set the [IQ Power Edge Slope](attr400009.html) property to **Rising Slope**, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope property to **Falling Slope**, the signal is quiet above the trigger level.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40000d.html language=enus -->
## TOPIC 00014: rfmxgsmprop/attr40000d.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40000d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40000d.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Link Direction Property

Link Direction Property

**Short Name:**Link Direction

Property of [RFmxGSM](crfmxgsm.html)

Specifies the source of the signal to be measured.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Uplink**.

| Downlink (0) | The source is a base transceiver station. |
| --- | --- |
| Uplink (1) | The source is a mobile station. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Link Direction |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40000e.html language=enus -->
## TOPIC 00015: rfmxgsmprop/attr40000e.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40000e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40000e.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Band Property

Band Property

**Short Name:**Band

Property of [RFmxGSM](crfmxgsm.html)

Specifies the operation band.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **PGSM**.

| PGSM (0) | The operation band is Primary GSM in the 900 MHz band. |
| --- | --- |
| EGSM (1) | The operation band is Extended GSM in the 900 MHz band. |
| RGSM (2) | The operation band is Railway GSM in the 900 MHz band. |
| DCS1800 (3) | The operation band is GSM in the 1800 MHz band. |
| PCS1900 (4) | The operation band is GSM in the 1900 MHz band. |
| GSM450 (5) | The operation band is GSM in the 450 MHz band. |
| GSM480 (6) | The operation band is GSM in the 480 MHz band. |
| GSM850 (7) | The operation band is GSM in the 850 MHz band. |
| GSM750 (8) | The operation band is GSM in the 750 MHz band. |
| TGSM810 (9) | The operation band is terrestrial GSM in the 810 MHz band. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Band |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40000f.html language=enus -->
## TOPIC 00016: rfmxgsmprop/attr40000f.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40000f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40000f.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Number of Timeslots Property

Number of Timeslots Property

**Short Name:**Num Timeslots

Property of [RFmxGSM](crfmxgsm.html)

Specifies the number of time slots to be measured.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Number of Timeslots |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr400010.html language=enus -->
## TOPIC 00017: rfmxgsmprop/attr400010.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr400010.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr400010.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Modulation Type Property

Modulation Type Property

**Short Name:**Modulation Type

Property of [RFmxGSM](crfmxgsm.html)

Specifies the modulation scheme used for the signal.

Use "slot<*n*>" as the selector string to configure or read this property.

The default value is **8PSK**.

| GMSK (0) | The modulation type is Gaussian minimum shift keying. This value is valid only when you set the Burst Type property to NB or AB. |
| --- | --- |
| 8PSK (1) | The modulation type is 8-PSK. This value is valid only when you set the Burst Type property to NB. |
| QPSK (2) | The modulation type is QPSK. This value is valid only when you set the Burst Type property to HB. |
| 16QAM (3) | The modulation type is 16-QAM. |
| 32QAM (4) | The modulation type is 32-QAM. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Signal Type |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr400011.html language=enus -->
## TOPIC 00018: rfmxgsmprop/attr400011.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr400011.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr400011.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Burst Type Property

Burst Type Property

**Short Name:**Burst Type

Property of [RFmxGSM](crfmxgsm.html)

Specifies the burst type.

Use "slot<*n*>" as the selector string to configure or read this property.

The default value is **NB**.

| NB (0) | The burst type is Normal Burst. |
| --- | --- |
| HB (1) | The burst type is Higher Symbol Rate Burst. |
| AB (2) | The burst type is Access Burst. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Signal Type |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr400012.html language=enus -->
## TOPIC 00019: rfmxgsmprop/attr400012.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr400012.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr400012.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

HB Filter Width Property

HB Filter Width Property

**Short Name:**HB Filter Width

Property of [RFmxGSM](crfmxgsm.html)

Specifies the filter width when you set the [Burst Type](attr400011.html) property to **HB**.

Use "slot<*n*>" as the selector string to configure or read this property.

The default value is **Narrow**.

| Narrow (0) | The measurement uses a narrow filter. |
| --- | --- |
| Wide (1) | The measurement uses a wide filter. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Signal Type |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr400013.html language=enus -->
## TOPIC 00020: rfmxgsmprop/attr400013.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr400013.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr400013.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Auto TSC Detection Enabled Property

Auto TSC Detection Enabled Property

**Short Name:**Auto TSC Detect Enabled

Property of [RFmxGSM](crfmxgsm.html)

Specifies whether the measurement automatically detects the training sequence code (TSC).

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | The measurement uses the value that you configure using the TSC property. |
| --- | --- |
| True (1) | The measurement detects the TSC in the burst. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Auto TSC Detection Enabled |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr400014.html language=enus -->
## TOPIC 00021: rfmxgsmprop/attr400014.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr400014.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr400014.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

TSC Property

TSC Property

**Short Name:**TSC

Property of [RFmxGSM](crfmxgsm.html)

Specifies the training sequence code (TSC) to use. This property is applicable only when you set the [Burst Sync Type](attr400016.html) property to **TSC** and the [Auto TSC Detect Enabled](attr400013.html) property to **False**. For access burst **TSC0**, **TSC1**, and **TSC2** are applicable.

Use "slot<*n*>" as the selector string to configure or read this property.

The default value is **TSC0**.

| TSC0 (0) | The measurement uses training sequence code 0. |
| --- | --- |
| TSC1 (1) | The measurement uses training sequence code 1. |
| TSC2 (2) | The measurement uses training sequence code 2. |
| TSC3 (3) | The measurement uses training sequence code 3. |
| TSC4 (4) | The measurement uses training sequence code 4. |
| TSC5 (5) | The measurement uses training sequence code 5. |
| TSC6 (6) | The measurement uses training sequence code 6. |
| TSC7 (7) | The measurement uses training sequence code 7. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure TSC |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr400015.html language=enus -->
## TOPIC 00022: rfmxgsmprop/attr400015.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr400015.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr400015.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Power Control Level Property

Power Control Level Property

**Short Name:**Pwr Control Level

Property of [RFmxGSM](crfmxgsm.html)

Specifies the power control level corresponding to the transmitted power, as defined in section 4.1 of the *3GPP TS 45.005 v8.0.0 specifications*.

Use "slot<*n*>" as the selector string to configure or read this property.

The default value is 0. Valid values are 0 to 31, inclusive.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Power Control Level |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr400016.html language=enus -->
## TOPIC 00023: rfmxgsmprop/attr400016.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr400016.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr400016.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Burst Synchronization Type Property

Burst Synchronization Type Property

**Short Name:**Burst Sync Type

Property of [RFmxGSM](crfmxgsm.html)

Specifies the method used to synchronize the burst.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **TSC**.

| TSC (0) | Synchronizes the measurement to the timing of the demodulated training sequence in the burst. The measurement requires a burst with a valid training sequence code (TSC). The measurement determines the T0 point by demodulating the burst and identifying the TSC. |
| --- | --- |
| Amplitude (1) | Synchronizes the measurement based on the RF envelope of the received signal. The measurement sets the T0 point as the center of the RF envelope. |
| None (2) | Sets the T0 point to 273.23 microseconds after the trigger. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Burst Synchronization Type |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr400017.html language=enus -->
## TOPIC 00024: rfmxgsmprop/attr400017.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr400017.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr400017.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Signal Structure Property

Signal Structure Property

**Short Name:**Signal Structure

Property of [RFmxGSM](crfmxgsm.html)

Specifies whether the signal is bursted or continuous. For bursted signal and continuous signals, set the [Trigger Type](attr400004.html) to **IQ Power Edge** and **None**, respectively.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Bursted**.

| Bursted (0) | The signal is bursted. |
| --- | --- |
| Continuous (1) | The signal is continuous. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr400018.html language=enus -->
## TOPIC 00025: rfmxgsmprop/attr400018.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr400018.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr400018.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Timing Advance Property

Timing Advance Property

**Short Name:**Timing Advance

Property of [RFmxGSM](crfmxgsm.html)

Specifies the timing advance value as specified in the 3GPP TS 45.010 specification for GSM access burst.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr400ffc.html language=enus -->
## TOPIC 00026: rfmxgsmprop/attr400ffc.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr400ffc.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr400ffc.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Reference Level Headroom Property

Reference Level Headroom Property

**Short Name:**Reference Level Headroom

Property of [RFmxGSM](crfmxgsm.html)

Specifies the margin RFmx adds to the [Reference Level](attr400002.html) property. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level.

RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input signal remains within the Reference Level plus the Reference Level Headroom. If you know the input power of the signal precisely or previously included the margin in the Reference Level, you could improve the signal-to-noise ratio by reducing the Reference Level Headroom.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

**Supported devices:**PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842.

**Default values**

| PXIe-5668 | 6 dB |
| --- | --- |
| PXIe-5830/5831/5832/5841/5842 | 1 dB |
| PXIe-5840 | 0 dB |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr400ffd.html language=enus -->
## TOPIC 00027: rfmxgsmprop/attr400ffd.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr400ffd.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr400ffd.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Selected Ports Property

Selected Ports Property

**Short Name:**Selected Ports

Property of [RFmxGSM](crfmxgsm.html)

Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr Get Available Ports VI to get the valid port names.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

**Valid values**

| PXIe-5830 | if0, if1 |
| --- | --- |
| PXIe-5831/5832 | if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel |
| Other devices | "" (empty string) |

**Default values**

| PXIe-5830/5831/5832 | if1 |
| --- | --- |
| Other devices | "" (empty string) |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr400fff.html language=enus -->
## TOPIC 00028: rfmxgsmprop/attr400fff.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr400fff.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr400fff.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Trigger:IQ Power Edge:Level Type Property

Trigger:IQ Power Edge:Level Type Property

**Short Name:**IQ Power Edge Level Type

Property of [RFmxGSM](crfmxgsm.html)

Specifies the reference for the [IQ Power Edge Level](attr400008.html) property. The IQ Power Edge Level Type property is used only when you set the [Trigger Type](attr400004.html) property to **IQ Power Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Relative**.

| Relative (0) | The value of the IQ Power Edge Level property is relative to the value of the Reference Level property. |
| --- | --- |
| Absolute (1) | The IQ Power Edge Level property specifies the absolute power. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr401000.html language=enus -->
## TOPIC 00029: rfmxgsmprop/attr401000.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr401000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr401000.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Measurement Enabled Property

ModAcc:Measurement Enabled Property

**Short Name:**ModAcc Enabled

Property of [RFmxGSM](crfmxgsm.html)

Specifies whether to enable modulation accuracy (ModAcc) measurements on the acquired signal.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr401002.html language=enus -->
## TOPIC 00030: rfmxgsmprop/attr401002.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr401002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr401002.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Averaging:Enabled Property

ModAcc:Averaging:Enabled Property

**Short Name:**ModAcc Averaging Enabled

Property of [RFmxGSM](crfmxgsm.html)

Specifies whether to enable averaging for the modulation accuracy (ModAcc) measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The measurement is performed on a single acquisition. |
| --- | --- |
| True (1) | The measurement is averaged over multiple acquisitions. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM ModAcc Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr401004.html language=enus -->
## TOPIC 00031: rfmxgsmprop/attr401004.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr401004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr401004.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Averaging:Count Property

ModAcc:Averaging:Count Property

**Short Name:**ModAcc Averaging Count

Property of [RFmxGSM](crfmxgsm.html)

Specifies the number of acquisitions used for averaging when you set the [ModAcc Averaging Enabled](attr401002.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM ModAcc Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr401005.html language=enus -->
## TOPIC 00032: rfmxgsmprop/attr401005.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr401005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr401005.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Droop Compensation Enabled Property

ModAcc:Droop Compensation Enabled Property

**Short Name:**ModAcc Droop Comp Enabled

Property of [RFmxGSM](crfmxgsm.html)

Specifies whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | Disables power droop compensation in the EVM measurement. |
| --- | --- |
| True (1) | Enables power droop compensation in the EVM measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM ModAcc Configure Droop Compensation Enabled |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr401006.html language=enus -->
## TOPIC 00033: rfmxgsmprop/attr401006.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr401006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr401006.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:All Traces Enabled Property

ModAcc:All Traces Enabled Property

**Short Name:**ModAcc All Traces Enabled

Property of [RFmxGSM](crfmxgsm.html)

Specifies whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr401007.html language=enus -->
## TOPIC 00034: rfmxgsmprop/attr401007.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr401007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr401007.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Number of Analysis Threads Property

ModAcc:Number of Analysis Threads Property

**Short Name:**ModAcc Num Analysis Threads

Property of [RFmxGSM](crfmxgsm.html)

Specifies the maximum number of threads used for parallelism for the ModAcc measurement.

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr401008.html language=enus -->
## TOPIC 00035: rfmxgsmprop/attr401008.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr401008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr401008.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:EVM:Mean RMS (%) Property

ModAcc:Results:EVM:Mean RMS (%) Property

**Short Name:**ModAcc Results EVM Mean RMS EVM (%)

Property of [RFmxGSM](crfmxgsm.html)

Returns the mean of RMS values of EVM measured over all acquisition time slots. This value is expressed as a percentage. The property returns this result for EDGE/EGPRS measurements.

You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr401009.html language=enus -->
## TOPIC 00036: rfmxgsmprop/attr401009.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr401009.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr401009.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:EVM:Maximum RMS (%) Property

ModAcc:Results:EVM:Maximum RMS (%) Property

**Short Name:**ModAcc Results EVM Max RMS EVM (%)

Property of [RFmxGSM](crfmxgsm.html)

Returns the maximum of RMS values of EVM measured over all acquisition time slots. This value is expressed as a percentage. The property returns this result for EDGE/EGPRS measurements.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40100a.html language=enus -->
## TOPIC 00037: rfmxgsmprop/attr40100a.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40100a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40100a.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:EVM:Mean Peak (%) Property

ModAcc:Results:EVM:Mean Peak (%) Property

**Short Name:**ModAcc Results EVM Mean Pk EVM (%)

Property of [RFmxGSM](crfmxgsm.html)

Returns the mean of the peak EVM values measured over all acquisition time slots. This value is expressed as a percentage. The property returns this result for EDGE/EGPRS measurements.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40100b.html language=enus -->
## TOPIC 00038: rfmxgsmprop/attr40100b.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40100b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40100b.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:EVM:Maximum Peak (%) Property

ModAcc:Results:EVM:Maximum Peak (%) Property

**Short Name:**ModAcc Results EVM Max Pk EVM (%)

Property of [RFmxGSM](crfmxgsm.html)

Returns the maximum of the peak EVM values measured over all acquisition time slots. This value is expressed as a percentage. The property returns this result for EDGE/EGPRS measurements.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40100c.html language=enus -->
## TOPIC 00039: rfmxgsmprop/attr40100c.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40100c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40100c.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:EVM:95th percentile (%) Property

ModAcc:Results:EVM:95th percentile (%) Property

**Short Name:**ModAcc Results EVM 95th percentile EVM (%)

Property of [RFmxGSM](crfmxgsm.html)

Returns the EVM value at which no more than 5% of the symbols have an EVM exceeding this value. This value is expressed as a percentage. The property returns this result for EDGE/EGPRS measurements.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40100d.html language=enus -->
## TOPIC 00040: rfmxgsmprop/attr40100d.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40100d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40100d.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:EVM:Peak EVM Symbol Property

ModAcc:Results:EVM:Peak EVM Symbol Property

**Short Name:**ModAcc Results EVM Pk EVM Symbol

Property of [RFmxGSM](crfmxgsm.html)

Returns the symbol number in the useful portion of the burst corresponding to [ModAcc Results EVM Max Pk EVM](attr40100b.html) result. The property returns this result for ModAcc EDGE/EGPRS measurements.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40100e.html language=enus -->
## TOPIC 00041: rfmxgsmprop/attr40100e.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40100e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40100e.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:EVM:Magnitude Error:Mean (%) Property

ModAcc:Results:EVM:Magnitude Error:Mean (%) Property

**Short Name:**ModAcc Results EVM Mean Magnitude Error (%)

Property of [RFmxGSM](crfmxgsm.html)

Returns the mean of RMS values of magnitude error measured over all acquisition time slots. This value is expressed as a percentage. The property returns this result for EDGE/EGPRS measurements.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40100f.html language=enus -->
## TOPIC 00042: rfmxgsmprop/attr40100f.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40100f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40100f.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:EVM:Magnitude Error:Maximum (%) Property

ModAcc:Results:EVM:Magnitude Error:Maximum (%) Property

**Short Name:**ModAcc Results EVM Max Magnitude Error (%)

Property of [RFmxGSM](crfmxgsm.html)

Returns the maximum of RMS values of magnitude error measured over all acquisition time slots. This value is expressed as a percentage. The property returns this result for EDGE/EGPRS measurements.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr401010.html language=enus -->
## TOPIC 00043: rfmxgsmprop/attr401010.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr401010.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr401010.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:EVM:Phase Error:Mean (deg) Property

ModAcc:Results:EVM:Phase Error:Mean (deg) Property

**Short Name:**ModAcc Results EVM Mean Phase Error (deg)

Property of [RFmxGSM](crfmxgsm.html)

Returns the mean of RMS values of phase error measured over all acquisition time slots. This value is expressed in degrees. The property returns this result for EDGE/EGPRS measurements.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr401011.html language=enus -->
## TOPIC 00044: rfmxgsmprop/attr401011.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr401011.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr401011.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:EVM:Phase Error:Maximum (deg) Property

ModAcc:Results:EVM:Phase Error:Maximum (deg) Property

**Short Name:**ModAcc Results EVM Max Phase Error (deg)

Property of [RFmxGSM](crfmxgsm.html)

Returns the maximum of the RMS values of phase error measured over all acquisition time slots. This value is expressed in degrees. The property returns this result for EDGE/EGPRS measurements.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr401012.html language=enus -->
## TOPIC 00045: rfmxgsmprop/attr401012.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr401012.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr401012.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:EVM:Frequency Error:Mean (Hz) Property

ModAcc:Results:EVM:Frequency Error:Mean (Hz) Property

**Short Name:**ModAcc Results EVM Mean Freq Error (Hz)

Property of [RFmxGSM](crfmxgsm.html)

Returns the mean of the frequency error values measured over all acquisition time slots. This value is expressed in Hz. The property returns this result for EDGE/EGPRS measurements.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr401013.html language=enus -->
## TOPIC 00046: rfmxgsmprop/attr401013.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr401013.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr401013.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:EVM:Frequency Error:Maximum (Hz) Property

ModAcc:Results:EVM:Frequency Error:Maximum (Hz) Property

**Short Name:**ModAcc Results EVM Max Freq Error (Hz)

Property of [RFmxGSM](crfmxgsm.html)

Returns the maximum of the frequency error values measured over all acquisition time slots. This value is expressed in Hz. The property returns this result for EDGE/EGPRS measurements.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr401014.html language=enus -->
## TOPIC 00047: rfmxgsmprop/attr401014.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr401014.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr401014.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:EVM:Amplitude Droop:Mean (dB/symbol) Property

ModAcc:Results:EVM:Amplitude Droop:Mean (dB/symbol) Property

**Short Name:**ModAcc Results EVM Mean Ampl Droop

Property of [RFmxGSM](crfmxgsm.html)

Returns the mean of the amplitude droop values measured over all acquisition time slots. This value is expressed in dB/symbol. The property returns this result for EDGE/EGPRS measurements.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr401015.html language=enus -->
## TOPIC 00048: rfmxgsmprop/attr401015.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr401015.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr401015.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:EVM:Amplitude Droop:Maximum (dB/symbol) Property

ModAcc:Results:EVM:Amplitude Droop:Maximum (dB/symbol) Property

**Short Name:**ModAcc Results EVM Max Ampl Droop

Property of [RFmxGSM](crfmxgsm.html)

Returns the maximum of the amplitude droop values measured over all acquisition time slots. This value is expressed in dB/symbol. The property returns this result for EDGE/EGPRS measurements.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr401016.html language=enus -->
## TOPIC 00049: rfmxgsmprop/attr401016.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr401016.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr401016.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:PFER:Phase Error:Mean RMS (deg) Property

ModAcc:Results:PFER:Phase Error:Mean RMS (deg) Property

**Short Name:**ModAcc Results PFER Mean RMS Phase Error

Property of [RFmxGSM](crfmxgsm.html)

Returns the mean of RMS values of phase error measured over all acquisition time slots. This value is expressed in degrees. The property returns this result for GSM ModAcc measurements.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr401017.html language=enus -->
## TOPIC 00050: rfmxgsmprop/attr401017.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr401017.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr401017.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:PFER:Phase Error:Maximum RMS (deg) Property

ModAcc:Results:PFER:Phase Error:Maximum RMS (deg) Property

**Short Name:**ModAcc Results PFER Max RMS Phase Error

Property of [RFmxGSM](crfmxgsm.html)

Returns the maximum of the RMS values of phase error measured over all acquisition time slots. This value is expressed in degrees. The property returns this result for GSM ModAcc measurements.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr401018.html language=enus -->
## TOPIC 00051: rfmxgsmprop/attr401018.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr401018.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr401018.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:PFER:Phase Error:Mean Peak (deg) Property

ModAcc:Results:PFER:Phase Error:Mean Peak (deg) Property

**Short Name:**ModAcc Results PFER Mean Pk Phase Error (deg)

Property of [RFmxGSM](crfmxgsm.html)

Returns the mean of peak phase error values measured over all acquisition time slots. This value is expressed in degrees. The property returns this result for GSM ModAcc measurements.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr401019.html language=enus -->
## TOPIC 00052: rfmxgsmprop/attr401019.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr401019.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr401019.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:PFER:Phase Error:Maximum Peak (deg) Property

ModAcc:Results:PFER:Phase Error:Maximum Peak (deg) Property

**Short Name:**ModAcc Results PFER Max Pk Phase Error (deg)

Property of [RFmxGSM](crfmxgsm.html)

Returns the maximum of peak phase error values measured over all acquisition time slots. This value is expressed in degrees. The property returns this result for GSM ModAcc measurements.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40101a.html language=enus -->
## TOPIC 00053: rfmxgsmprop/attr40101a.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40101a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40101a.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:PFER:Phase Error:Peak Symbol Property

ModAcc:Results:PFER:Phase Error:Peak Symbol Property

**Short Name:**ModAcc Results PFER Pk Phase Error Symbol

Property of [RFmxGSM](crfmxgsm.html)

Returns the symbol number in the useful portion of the burst corresponding to the phase error value in the [ModAcc Results PFER Max Pk Phase Error](attr401019.html) result. The property returns this result for GSM ModAcc measurements.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40101b.html language=enus -->
## TOPIC 00054: rfmxgsmprop/attr40101b.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40101b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40101b.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:PFER:Frequency Error:Mean (Hz) Property

ModAcc:Results:PFER:Frequency Error:Mean (Hz) Property

**Short Name:**ModAcc Results PFER Mean Freq Error (Hz)

Property of [RFmxGSM](crfmxgsm.html)

Returns the mean of the frequency error values measured over all acquisition time slots. This value is expressed in Hz. The property returns this result for GSM ModAcc measurements.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40101c.html language=enus -->
## TOPIC 00055: rfmxgsmprop/attr40101c.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40101c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40101c.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:PFER:Frequency Error:Maximum (Hz) Property

ModAcc:Results:PFER:Frequency Error:Maximum (Hz) Property

**Short Name:**ModAcc Results PFER Max Freq Error (Hz)

Property of [RFmxGSM](crfmxgsm.html)

Returns the maximum of the frequency error values measured over all acquisition time slots. This value is expressed in Hz. The property returns this result for GSM ModAcc measurements.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40101d.html language=enus -->
## TOPIC 00056: rfmxgsmprop/attr40101d.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40101d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40101d.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:IQ Gain Imbalance:Mean (dB) Property

ModAcc:Results:IQ Gain Imbalance:Mean (dB) Property

**Short Name:**ModAcc Results Mean IQ Gain Imbalance (dB)

Property of [RFmxGSM](crfmxgsm.html)

Returns the mean of I/Q gain imbalance values measured over all acquisition time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40101e.html language=enus -->
## TOPIC 00057: rfmxgsmprop/attr40101e.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40101e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40101e.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:IQ Gain Imbalance:Maximum (dB) Property

ModAcc:Results:IQ Gain Imbalance:Maximum (dB) Property

**Short Name:**ModAcc Results Max IQ Gain Imbalance (dB)

Property of [RFmxGSM](crfmxgsm.html)

Returns the maximum of I/Q gain imbalance values measured over all acquisition time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40101f.html language=enus -->
## TOPIC 00058: rfmxgsmprop/attr40101f.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40101f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40101f.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:IQ Origin Offset:Mean (dB) Property

ModAcc:Results:IQ Origin Offset:Mean (dB) Property

**Short Name:**ModAcc Results Mean IQ Origin Offset (dB)

Property of [RFmxGSM](crfmxgsm.html)

Returns the mean of the I/Q origin offset values measured over all acquisition time slots. This value is expressed in dB. Presence of I/Q gain imbalance and quadrature skew in the signal affects the I/Q origin offset measurement. The property returns this result for GSM/EDGE/EGPRS measurements.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr401020.html language=enus -->
## TOPIC 00059: rfmxgsmprop/attr401020.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr401020.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr401020.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:IQ Origin Offset:Maximum (dB) Property

ModAcc:Results:IQ Origin Offset:Maximum (dB) Property

**Short Name:**ModAcc Results Max IQ Origin Offset (dB)

Property of [RFmxGSM](crfmxgsm.html)

Returns the maximum of the I/Q origin offset values measured over all acquisition time slots. This value is expressed in dB. Presence of I/Q gain imbalance and quadrature skew in the signal affects the I/Q origin offset measurement. The property returns this result for GSM/EDGE/EGPRS measurements.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr401021.html language=enus -->
## TOPIC 00060: rfmxgsmprop/attr401021.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr401021.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr401021.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Detected TSC Property

ModAcc:Results:Detected TSC Property

**Short Name:**ModAcc Results Detected TSC

Property of [RFmxGSM](crfmxgsm.html)

Returns the detected training sequence code (TSC) if you set the [Burst Sync Type](attr400016.html) property to **TSC**.

Use "slot<*n*>" as the selector string to read this result.

| Unknown (-1) | The synchronization is not found, and measurements correspond to best estimate of synchronization. |
| --- | --- |
| TSC0 (0) | The detected TSC is TSC0. |
| TSC1 (1) | The detected TSC is TSC1. |
| TSC2 (2) | The detected TSC is TSC2. |
| TSC3 (3) | The detected TSC is TSC3. |
| TSC4 (4) | The detected TSC is TSC4. |
| TSC5 (5) | The detected TSC is TSC5. |
| TSC6 (6) | The detected TSC is TSC6. |
| TSC7 (7) | The detected TSC is TSC7. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr401023.html language=enus -->
## TOPIC 00061: rfmxgsmprop/attr401023.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr401023.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr401023.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:EVM:Magnitude Error:Mean Peak (%) Property

ModAcc:Results:EVM:Magnitude Error:Mean Peak (%) Property

**Short Name:**ModAcc Results EVM Mean Pk Magnitude Error (%)

Property of [RFmxGSM](crfmxgsm.html)

Returns the mean of peak magnitude error values measured over all timeslots of all acquisitions. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr401024.html language=enus -->
## TOPIC 00062: rfmxgsmprop/attr401024.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr401024.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr401024.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:EVM:Magnitude Error:Maximum Peak (%) Property

ModAcc:Results:EVM:Magnitude Error:Maximum Peak (%) Property

**Short Name:**ModAcc Results EVM Max Pk Magnitude Error (%)

Property of [RFmxGSM](crfmxgsm.html)

Returns the maximum of peak magnitude error values measured over all time slots of all acquisitions. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr401025.html language=enus -->
## TOPIC 00063: rfmxgsmprop/attr401025.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr401025.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr401025.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:EVM:Magnitude Error:95th percentile (%) Property

ModAcc:Results:EVM:Magnitude Error:95th percentile (%) Property

**Short Name:**ModAcc Results EVM 95th percentile Magnitude Error (%)

Property of [RFmxGSM](crfmxgsm.html)

Returns the measured magnitude error value multiplied by 100, at which, no more than 5 percent of the symbols have magnitude error exceeding this value. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr401026.html language=enus -->
## TOPIC 00064: rfmxgsmprop/attr401026.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr401026.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr401026.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:EVM:Phase Error:Mean Peak (deg) Property

ModAcc:Results:EVM:Phase Error:Mean Peak (deg) Property

**Short Name:**ModAcc Results EVM Mean Pk Phase Error (deg)

Property of [RFmxGSM](crfmxgsm.html)

Returns the mean of peak phase error values measured over all timeslots of all acquisitions. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr401027.html language=enus -->
## TOPIC 00065: rfmxgsmprop/attr401027.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr401027.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr401027.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:EVM:Phase Error:Maximum Peak (deg) Property

ModAcc:Results:EVM:Phase Error:Maximum Peak (deg) Property

**Short Name:**ModAcc Results EVM Max Pk Phase Error (deg)

Property of [RFmxGSM](crfmxgsm.html)

Returns the maximum of peak phase error values measured over all timeslots of all acquisitions. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr401028.html language=enus -->
## TOPIC 00066: rfmxgsmprop/attr401028.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr401028.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr401028.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:EVM:Phase Error:95th percentile (deg) Property

ModAcc:Results:EVM:Phase Error:95th percentile (deg) Property

**Short Name:**ModAcc Results EVM 95th percentile Phase Error (deg)

Property of [RFmxGSM](crfmxgsm.html)

Returns the measured phase error value multiplied by 100, at which, no more than 5 percent of the symbols have phase error exceeding this value. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr401029.html language=enus -->
## TOPIC 00067: rfmxgsmprop/attr401029.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr401029.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr401029.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:PFER:Phase Error:95th percentile (deg) Property

ModAcc:Results:PFER:Phase Error:95th percentile (deg) Property

**Short Name:**ModAcc Results PFER 95th percentile Phase Error (deg)

Property of [RFmxGSM](crfmxgsm.html)

Returns the measured phase error value multiplied by 100, at which, no more than 5 percent of the symbols have phase error exceeding this value. This result is returned while performing ModAcc measurement on GSM. This value is measured in degrees.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr402000.html language=enus -->
## TOPIC 00068: rfmxgsmprop/attr402000.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr402000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr402000.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ORFS:Measurement Enabled Property

ORFS:Measurement Enabled Property

**Short Name:**ORFS Enabled

Property of [RFmxGSM](crfmxgsm.html)

Specifies whether to enable the output radio frequency spectrum (ORFS) measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr402002.html language=enus -->
## TOPIC 00069: rfmxgsmprop/attr402002.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr402002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr402002.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ORFS:Averaging:Enabled Property

ORFS:Averaging:Enabled Property

**Short Name:**ORFS Averaging Enabled

Property of [RFmxGSM](crfmxgsm.html)

Specifies whether to enable averaging for the output radio frequency spectrum (ORFS) measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The measurement is performed on a single acquisition. |
| --- | --- |
| True (1) | The measurement is averaged over multiple acquisitions. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM ORFS Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr402003.html language=enus -->
## TOPIC 00070: rfmxgsmprop/attr402003.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr402003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr402003.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ORFS:Averaging:Type Property

ORFS:Averaging:Type Property

**Short Name:**ORFS Averaging Type

Property of [RFmxGSM](crfmxgsm.html)

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the output radio frequency spectrum (ORFS) measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Log**.

| RMS (0) | The measurement averages the power spectrum linearly. RMS averaging reduces signal fluctuations but not the noise floor. |
| --- | --- |
| Log (1) | The measurement averages the power spectrum in a logarithmic scale. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM ORFS Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr402004.html language=enus -->
## TOPIC 00071: rfmxgsmprop/attr402004.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr402004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr402004.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ORFS:Averaging:Count Property

ORFS:Averaging:Count Property

**Short Name:**ORFS Averaging Count

Property of [RFmxGSM](crfmxgsm.html)

Specifies the number of acquisitions used for averaging when you set the [ORFS Averaging Enabled](attr402002.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM ORFS Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr402005.html language=enus -->
## TOPIC 00072: rfmxgsmprop/attr402005.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr402005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr402005.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ORFS:Measurement Type Property

ORFS:Measurement Type Property

**Short Name:**ORFS Meas Type

Property of [RFmxGSM](crfmxgsm.html)

Specifies the type of spectral distortion to be measured.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Modulation and Switching**.

| Modulation and Switching (0) | Measures the spectrum on the modulated part and the switching part of the waveform. |
| --- | --- |
| Modulation (1) | Measures the spectrum on the modulated part of the waveform. |
| Switching (2) | Measures the spectrum on the switching part of the waveform. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM ORFS Configure Measurement Type |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr402006.html language=enus -->
## TOPIC 00073: rfmxgsmprop/attr402006.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr402006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr402006.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ORFS:Noise Compensation Enabled Property

ORFS:Noise Compensation Enabled Property

**Short Name:**ORFS Noise Comp Enabled

Property of [RFmxGSM](crfmxgsm.html)

Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Noise compensation is applicable only on modulation offsets and not on switching offsets.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **False**.

**Supported Devices**: PXIe-5663/5665/5668R, PXIe-5830/5831/5832

| False (0) | Disables compensation of the channel powers for the signal analyzer noise floor. |
| --- | --- |
| True (1) | Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the output radio frequency spectrum (ORFS) measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are measured again. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM ORFS Configure Noise Compensation Enabled |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr402007.html language=enus -->
## TOPIC 00074: rfmxgsmprop/attr402007.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr402007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr402007.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ORFS:Offset Frequency Mode Property

ORFS:Offset Frequency Mode Property

**Short Name:**ORFS Offset Freq Mode

Property of [RFmxGSM](crfmxgsm.html)

Specifies the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Standard**.

| Standard (0) | Uses the list of lower and upper offset frequencies of 100 kHz, 200 kHz, 250 kHz, 400 kHz, 600 kHz, 800 kHz, 1000 kHz, 1200 kHz, 1400 kHz, 1600 kHz, and 1800 kHz for the spectrum due to the modulation measurement, and the lower and upper offset frequencies of 400 kHz, 600 kHz, 1200 kHz, and 1800 kHz for the spectrum produced by the switching measurement. |
| --- | --- |
| Short (1) | Uses the list of lower and upper offset frequencies of 200 kHz, 250 kHz, 400 kHz, 600 kHz, and 1200 kHz for the spectrum due to the modulation measurement, and the lower and upper offset frequencies of 400 kHz, 600 kHz, 1200 kHz, and 1800 kHz for the spectrum produced by the switching measurement. |
| Custom (2) | Uses the list of frequencies that is configured using the RFmxGSM ORFS Configure Modulation Custom Offset Frequency (Array) and RFmxGSM ORFS Configure Switching Custom Offset Frequency (Array) VIs for measurement of spectrum produced by modulation and switching measurements. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM ORFS Configure Offset Frequency Mode |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40200b.html language=enus -->
## TOPIC 00075: rfmxgsmprop/attr40200b.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40200b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40200b.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ORFS:Modulation:Carrier RBW (Hz) Property

ORFS:Modulation:Carrier RBW (Hz) Property

**Short Name:**ORFS Mod Carrier RBW (Hz)

Property of [RFmxGSM](crfmxgsm.html)

Specifies the RBW used for measuring modulation carrier power in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 30kHz.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40200e.html language=enus -->
## TOPIC 00076: rfmxgsmprop/attr40200e.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40200e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40200e.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ORFS:Switching:Carrier RBW (Hz) Property

ORFS:Switching:Carrier RBW (Hz) Property

**Short Name:**ORFS Switching Carrier RBW (Hz)

Property of [RFmxGSM](crfmxgsm.html)

Specifies the RBW used for measuring switching carrier power in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 300kHz.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr402011.html language=enus -->
## TOPIC 00077: rfmxgsmprop/attr402011.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr402011.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr402011.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ORFS:Evaluation Symbols:Start (%) Property

ORFS:Evaluation Symbols:Start (%) Property

**Short Name:**ORFS Evaluation Symbols Start (%)

Property of [RFmxGSM](crfmxgsm.html)

Specifies the start position within the useful part of the burst, in percentage, for measuring ORFS due to modulation.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 50.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM ORFS Configure Evaluation Symbols |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr402012.html language=enus -->
## TOPIC 00078: rfmxgsmprop/attr402012.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr402012.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr402012.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ORFS:Evaluation Symbols:Include TSC Property

ORFS:Evaluation Symbols:Include TSC Property

**Short Name:**ORFS Evaluation Symbols Include TSC

Property of [RFmxGSM](crfmxgsm.html)

Specifies whether to include the training sequence code (TSC) portion of burst for measuring ORFS due to modulation.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The TSC portion of the burst will be excluded while performing the ORFS measurement. |
| --- | --- |
| True (1) | The TSC portion of the burst will be included while performing the ORFS measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM ORFS Configure Evaluation Symbols |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr402013.html language=enus -->
## TOPIC 00079: rfmxgsmprop/attr402013.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr402013.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr402013.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ORFS:Evaluation Symbols:Stop (%) Property

ORFS:Evaluation Symbols:Stop (%) Property

**Short Name:**ORFS Evaluation Symbols Stop (%)

Property of [RFmxGSM](crfmxgsm.html)

Specifies the stop position within the useful part of the burst, in percentage, for measuring ORFS due to modulation.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 90.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM ORFS Configure Evaluation Symbols |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr402014.html language=enus -->
## TOPIC 00080: rfmxgsmprop/attr402014.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr402014.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr402014.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ORFS:All Traces Enabled Property

ORFS:All Traces Enabled Property

**Short Name:**ORFS All Traces Enabled

Property of [RFmxGSM](crfmxgsm.html)

Specifies whether to enable the traces to be stored and retrieved after performing the output radio frequency spectrum (ORFS) measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr402015.html language=enus -->
## TOPIC 00081: rfmxgsmprop/attr402015.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr402015.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr402015.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ORFS:Number of Analysis Threads Property

ORFS:Number of Analysis Threads Property

**Short Name:**ORFS Num Analysis Threads

Property of [RFmxGSM](crfmxgsm.html)

Specifies the maximum number of threads used for parallelism for the output radio frequency spectrum (ORFS) measurement.

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40201d.html language=enus -->
## TOPIC 00082: rfmxgsmprop/attr40201d.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40201d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40201d.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ORFS:Modulation:Number of Offsets Property

ORFS:Modulation:Number of Offsets Property

**Short Name:**ORFS Mod Num Offsets

Property of [RFmxGSM](crfmxgsm.html)

Specifies the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to modulation.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40201e.html language=enus -->
## TOPIC 00083: rfmxgsmprop/attr40201e.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40201e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40201e.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ORFS:Modulation:Offset Frequency (Hz) Property

ORFS:Modulation:Offset Frequency (Hz) Property

**Short Name:**ORFS Mod Offset Freq (Hz)

Property of [RFmxGSM](crfmxgsm.html)

Specifies the value of positive frequency offset for which to measure the spectrum due to modulation measurement. This value is expressed in Hz.

Use "offset<*n*>" as the selector string to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Modulation Custom Offset Frequency (Array) |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40201f.html language=enus -->
## TOPIC 00084: rfmxgsmprop/attr40201f.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40201f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40201f.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ORFS:Modulation:Offset RBW (Hz) Property

ORFS:Modulation:Offset RBW (Hz) Property

**Short Name:**ORFS Mod Offset RBW (Hz)

Property of [RFmxGSM](crfmxgsm.html)

Specifies the resolution bandwidth used for ORFS due to modulation measurement. This value is expressed in Hz.

Use "offset<*n*>" as the selector string to configure or read this property.

The default value is 30000.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr402020.html language=enus -->
## TOPIC 00085: rfmxgsmprop/attr402020.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr402020.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr402020.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ORFS:Switching:Number of Offsets Property

ORFS:Switching:Number of Offsets Property

**Short Name:**ORFS Switching Num Offsets

Property of [RFmxGSM](crfmxgsm.html)

Specifies the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to switching.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr402021.html language=enus -->
## TOPIC 00086: rfmxgsmprop/attr402021.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr402021.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr402021.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ORFS:Switching:Offset Frequency (Hz) Property

ORFS:Switching:Offset Frequency (Hz) Property

**Short Name:**ORFS Switching Offset Freq (Hz)

Property of [RFmxGSM](crfmxgsm.html)

Specifies the value of positive frequency offset for which to measure the spectrum due to switching measurement. This value is expressed in Hz.

Use "offset<*n*>" as the selector string to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Switching Custom Offset Frequency (Array) |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr402022.html language=enus -->
## TOPIC 00087: rfmxgsmprop/attr402022.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr402022.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr402022.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ORFS:Switching:Offset RBW (Hz) Property

ORFS:Switching:Offset RBW (Hz) Property

**Short Name:**ORFS Switching Offset RBW (Hz)

Property of [RFmxGSM](crfmxgsm.html)

Specifies the resolution bandwidth used for ORFS due to switching measurement. This value is expressed in Hz.

Use "offset<*n*>" as the selector string to configure or read this property.

The default value is 30kHz.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr402024.html language=enus -->
## TOPIC 00088: rfmxgsmprop/attr402024.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr402024.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr402024.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

ORFS:Evaluation Symbols:Scope Property

ORFS:Evaluation Symbols:Scope Property

**Short Name:**ORFS Evaluation Symbols Scope

Property of [RFmxGSM](crfmxgsm.html)

Specifies the modulation power measurements that will use the part of burst configured using the RFmxGSM ORFS Configure Evaluation Symbols VI.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Offset**.

| Offset (0) | Modulation Offset Power measurements will only use the part of burst configured using the RFmxGSM ORFS Configure Evaluation Symbols VI. Modulation Carrier Power measurement will use all of the useful part of the burst. |
| --- | --- |
| Offset and Carrier (1) | Modulation Offset and Carrier Power measurements will both use the part of burst configured using the RFmxGSM ORFS Configure Evaluation Symbols VI. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr403000.html language=enus -->
## TOPIC 00089: rfmxgsmprop/attr403000.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr403000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr403000.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

PVT:Measurement Enabled Property

PVT:Measurement Enabled Property

**Short Name:**PVT Enabled

Property of [RFmxGSM](crfmxgsm.html)

Specifies whether to enable the power versus time (PVT) measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr403002.html language=enus -->
## TOPIC 00090: rfmxgsmprop/attr403002.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr403002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr403002.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

PVT:Averaging:Enabled Property

PVT:Averaging:Enabled Property

**Short Name:**PVT Averaging Enabled

Property of [RFmxGSM](crfmxgsm.html)

Specifies whether to enable averaging for the power versus time (PVT) measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The measurement is performed on a single acquisition. |
| --- | --- |
| True (1) | The measurement is averaged over multiple acquisitions. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM PVT Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr403004.html language=enus -->
## TOPIC 00091: rfmxgsmprop/attr403004.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr403004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr403004.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

PVT:Averaging:Type Property

PVT:Averaging:Type Property

**Short Name:**PVT Averaging Type

Property of [RFmxGSM](crfmxgsm.html)

Specifies the averaging type for multiple acquisitions.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **RMS**.

| RMS (0) | The power at each sample interval is linearly averaged from one acquisition to the next acquisition. |
| --- | --- |
| Log (1) | The power at each sample interval is averaged on a logarithmic scale from one acquisition to the next acquisition. |
| Max (3) | The peak power at each sample interval is retained from one acquisition to the next acquisition. |
| Min (4) | The lowest power at each sample interval is retained from one acquisition to the next acquisition. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM PVT Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr403005.html language=enus -->
## TOPIC 00092: rfmxgsmprop/attr403005.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr403005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr403005.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

PVT:Averaging:Count Property

PVT:Averaging:Count Property

**Short Name:**PVT Averaging Count

Property of [RFmxGSM](crfmxgsm.html)

Specifies the number of acquisitions used for averaging when you set the [PVT Averaging Enabled](attr403002.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr403007.html language=enus -->
## TOPIC 00093: rfmxgsmprop/attr403007.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr403007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr403007.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

PVT:RBW Filter:Bandwidth (Hz) Property

PVT:RBW Filter:Bandwidth (Hz) Property

**Short Name:**PVT RBW (Hz)

Property of [RFmxGSM](crfmxgsm.html)

Specifies the RBW Filter Bandwidth in Hz

The default value is 500 kHz

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr403009.html language=enus -->
## TOPIC 00094: rfmxgsmprop/attr403009.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr403009.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr403009.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

PVT:All Traces Enabled Property

PVT:All Traces Enabled Property

**Short Name:**PVT All Traces Enabled

Property of [RFmxGSM](crfmxgsm.html)

Specifies whether to enable the traces to be stored and retrieved after performing the power versus time (PVT) measurement.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40300a.html language=enus -->
## TOPIC 00095: rfmxgsmprop/attr40300a.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40300a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40300a.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

PVT:Number of Analysis Threads Property

PVT:Number of Analysis Threads Property

**Short Name:**PVT Num Analysis Threads

Property of [RFmxGSM](crfmxgsm.html)

Specifies the maximum number of threads used for parallelism for the power versus time (PVT) measurement.

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40300b.html language=enus -->
## TOPIC 00096: rfmxgsmprop/attr40300b.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40300b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40300b.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

PVT:Results:Measurement Status Property

PVT:Results:Measurement Status Property

**Short Name:**PVT Results Meas Status

Property of [RFmxGSM](crfmxgsm.html)

Indicates the overall measurement status based on standard-defined limits.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

| Fail (0) | The measurement failed because the average power of at least one slot is outside the standard-defined limits. |
| --- | --- |
| Pass (1) | The measurement passed because the average power of all slots is within the standard-defined limits. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM PVT Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40300c.html language=enus -->
## TOPIC 00097: rfmxgsmprop/attr40300c.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40300c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40300c.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

PVT:Results:Slot:Average Power (dBm) Property

PVT:Results:Slot:Average Power (dBm) Property

**Short Name:**PVT Results Slot Avg Pwr (dBm)

Property of [RFmxGSM](crfmxgsm.html)

Returns the mean power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm.

Use "slot<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM PVT Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40300d.html language=enus -->
## TOPIC 00098: rfmxgsmprop/attr40300d.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40300d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40300d.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

PVT:Results:Slot:Burst Width (s) Property

PVT:Results:Slot:Burst Width (s) Property

**Short Name:**PVT Results Slot Burst Width (s)

Property of [RFmxGSM](crfmxgsm.html)

Returns the burst width for the slot where the -3 dB transition points occur. This value is expressed in seconds.

Use "slot<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM PVT Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40300e.html language=enus -->
## TOPIC 00099: rfmxgsmprop/attr40300e.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40300e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40300e.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

PVT:Results:Slot:Maximum Power (dBm) Property

PVT:Results:Slot:Maximum Power (dBm) Property

**Short Name:**PVT Results Slot Max Pwr (dBm)

Property of [RFmxGSM](crfmxgsm.html)

Returns the maximum power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm.

Use "slot<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM PVT Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40300f.html language=enus -->
## TOPIC 00100: rfmxgsmprop/attr40300f.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40300f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40300f.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

PVT:Results:Slot:Minimum Power (dBm) Property

PVT:Results:Slot:Minimum Power (dBm) Property

**Short Name:**PVT Results Slot Min Pwr (dBm)

Property of [RFmxGSM](crfmxgsm.html)

Returns the minimum power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm.

Use "slot<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM PVT Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr403010.html language=enus -->
## TOPIC 00101: rfmxgsmprop/attr403010.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr403010.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr403010.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

PVT:Results:Slot:Burst Threshold (dBm) Property

PVT:Results:Slot:Burst Threshold (dBm) Property

**Short Name:**PVT Results Slot Burst Threshold (dBm)

Property of [RFmxGSM](crfmxgsm.html)

Returns the threshold that the power versus time (PVT) measurement uses to determine the burst validity. This value is expressed in dBm.

Use "slot<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM PVT Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr403011.html language=enus -->
## TOPIC 00102: rfmxgsmprop/attr403011.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr403011.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr403011.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

PVT:Results:Slot:Measurement Status Property

PVT:Results:Slot:Measurement Status Property

**Short Name:**PVT Results Slot Meas Status

Property of [RFmxGSM](crfmxgsm.html)

Indicates the power versus time (PVT) measurement status for a particular slot.

Use "slot<*n*>" as the selector string to read this property.

| Fail (0) | The average power for at least one slot is outside the standard-defined limits. |
| --- | --- |
| Pass (1) | The average power for each slot is within the standard-defined limits. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxGSM PVT Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40c000.html language=enus -->
## TOPIC 00103: rfmxgsmprop/attr40c000.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40c000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40c000.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Result Fetch Timeout (s) Property

Result Fetch Timeout (s) Property

**Short Name:**Result Fetch Timeout (s)

Property of [RFmxGSM](crfmxgsm.html)

Specifies the time to wait before results are available in the RFmxGSM Property Node. This value is expressed in seconds.

Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxGSM Property Node waits until the measurement is complete.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40d000.html language=enus -->
## TOPIC 00104: rfmxgsmprop/attr40d000.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40d000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40d000.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Auto Level Initial Reference Level (dBm) Property

Advanced:Auto Level Initial Reference Level (dBm) Property

**Short Name:**Auto Level Initial Ref Level (dBm)

Property of [RFmxGSM](crfmxgsm.html)

Specifies the initial reference level the RFmxGSM Auto Level VI uses to estimate the peak power of the input signal. This value is expressed in dBm.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 30.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/attr40d003.html language=enus -->
## TOPIC 00105: rfmxgsmprop/attr40d003.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/attr40d003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/attr40d003.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Limited Configuration Change Property

Advanced:Limited Configuration Change Property

**Short Name:**Limited Configuration Change

Property of [RFmxGSM](crfmxgsm.html)

Specifies the set of properties that are considered by RFmx in the locked signal configuration state.

If your test system performs the same measurement at different selected ports, multiple frequencies and/or power levels repeatedly, enabling this property can help achieve faster measurements. When you set this property to a value other than **Disabled**, the RFmx driver will use an optimized code path and skip some checks. Because RFmx skips some checks when you use this property, you need to be aware of the limitations of this feature, which are listed in the [Limitations of the Limited Configuration Change Property](limitations.html) topic.

You can also use this property to lock a specific instrument configuration for a signal so that every time that you initiate the signal, RFmx applies the RFmxInstr properties from a locked configuration.

NI recommends you use this property in conjunction with named signal configurations. Create named signal configurations for each measurement configuration in your test program and set this property to a value other than **Disabled** for one or more of the named signal configurations. This allows RFmx to precompute the acquisition settings for your measurement configurations and re-use the precomputed settings each time you initiate the measurement. You do not need to use this property if you create named signals for all the measurement configurations in your test program during test sequence initialization and do not change any RFInstr or personality properties while testing each device under test. RFmx automatically optimizes that use case.

Specify the named signal configuration you are setting this property in the selector string input. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Disabled**.

| Disabled (0) | This is the normal mode of RFmx operation. All configuration changes in RFmxInstr properties or in personality properties will be applied during RFmx Commit. |
| --- | --- |
| No Change (1) | Signal configuration is locked after the first Commit of the named signal configuration. Any configuration change thereafter either in RFmxInstr properties or personality properties will not be considered by subsequent RFmx Commits or Initiates of this signal. Use No Change if you have created named signal configurations for all measurement configurations but are setting some RFmxInstr properties. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| Frequency (2) | Signal configuration, other than center frequency and external attenuation, is locked after first Commit of the named signal configuration. Thereafter, only the Center Frequency and External Attenuation property value changes will be considered by subsequent driver Commits or Initiates of this signal. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| Reference Level (3) | Signal configuration, other than the reference level, is locked after first Commit of the named signal configuration. Thereafter only the Reference Level property value change will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends that you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| Freq and Ref Level (4) | Signal configuration, other than center frequency, reference level, and external attenuation, is locked after first Commit of the named signal configuration. Thereafter only Center Frequency, Reference Level, and External Attenuation property value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| Selected Ports, Freq and Ref Level (5) | Signal configuration, other than selected ports, center frequency, reference level, external attenuation, and RFInstr configuration, is locked after first Commit or Initiate of the named signal configuration. Thereafter only Selected Ports, Center Frequency, Reference Level, and External Attenuation property value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-gsm-prop path=rfmxgsmprop/crfmxgsm.html language=enus -->
## TOPIC 00106: rfmxgsmprop/crfmxgsm.html

- bundle_id: `rfmx-gsm-prop`
- source_path: `rfmxgsmprop/crfmxgsm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-prop/raw/resource/enus/rfmxgsmprop/crfmxgsm.html
- document_id: `rfmx-gsm-prop`
- page_type: `leaf`
- content_type: ``

RFmxGSM Properties

RFmxGSM Properties

Use the RFmxGSM properties to access options for configuring and fetching measurements.

| Property | Description |
| --- | --- |
| Selector String | Specifies the selector string used to access all subsequent selector string-based properties in this instance of the property node. Details |
| Selected Ports | Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr Get Available Ports VI to get the valid port names. Details |
| Center Frequency (Hz) | Specifies the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency. Details |
| Reference Level | Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. Details |
| External Attenuation (dB) | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. Details |
| Reference Level Headroom | Specifies the margin RFmx adds to the Reference Level property. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. Details |
| Trigger:Type | Specifies the trigger type. Details |
| Trigger:Digital Edge:Source | Specifies the source terminal for the digital edge trigger. This property is used only when you set the Trigger Type property to Digital Edge. Details |
| Trigger:Digital Edge:Edge | Specifies the active edge for the trigger. This property is used only when you set the Trigger Type property to Digital Edge. Details |
| Trigger:IQ Power Edge:Source | Specifies the channel from which the device monitors the trigger. This property is used only when you set the Trigger Type property to IQ Power Edge. Details |
| Trigger:IQ Power Edge:Level (dB or dBm) | Specifies the power level at which the device triggers. This value is expressed in dB when you set the IQ Power Edge Level Type property to Relative and in dBm when you set the IQ Power Edge Level Type property to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this property, taking into consideration the specified slope. This property is used only when you set the Trigger Type property to IQ Power Edge. Details |
| Trigger:IQ Power Edge:Level Type | Specifies the reference for the IQ Power Edge Level property. The IQ Power Edge Level Type property is used only when you set the Trigger Type property to IQ Power Edge. Details |
| Trigger:IQ Power Edge:Slope | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the IQ Power Edge Level property with the slope you specify. This property is used only when you set the Trigger Type property to IQ Power Edge. Details |
| Trigger:Delay (s) | Specifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. Details |
| Trigger:Minimum Quiet Time:Mode | Specifies whether the measurement computes the minimum quiet time used for triggering. Details |
| Trigger:Minimum Quiet Time:Duration (s) | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the IQ Power Edge Slope property to Rising Slope, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope property to Falling Slope, the signal is quiet above the trigger level. Details |
| Link Direction | Specifies the source of the signal to be measured. Details |
| Band | Specifies the operation band. Details |
| Signal Structure | Specifies whether the signal is bursted or continuous. For bursted signal and continuous signals, set the Trigger Type to IQ Power Edge and None, respectively. Details |
| Number of Timeslots | Specifies the number of time slots to be measured. Details |
| Modulation Type | Specifies the modulation scheme used for the signal. Use "slot<n>" as the selector string to configure or read this property. Details |
| Burst Type | Specifies the burst type. Use "slot<n>" as the selector string to configure or read this property. Details |
| HB Filter Width | Specifies the filter width when you set the Burst Type property to HB. Use "slot<n>" as the selector string to configure or read this property. Details |
| Auto TSC Detection Enabled | Specifies whether the measurement automatically detects the training sequence code (TSC). Details |
| TSC | Specifies the training sequence code (TSC) to use. This property is applicable only when you set the Burst Sync Type property to TSC and the Auto TSC Detect Enabled property to False. For access burst TSC0, TSC1, and TSC2 are applicable. Use "slot<n>" as the selector string to configure or read this property. Details |
| Power Control Level | Specifies the power control level corresponding to the transmitted power, as defined in section 4.1 of the 3GPP TS 45.005 v8.0.0 specifications. Use "slot<n>" as the selector string to configure or read this property. Details |
| Timing Advance | Specifies the timing advance value as specified in the 3GPP TS 45.010 specification for GSM access burst. Details |
| Burst Synchronization Type | Specifies the method used to synchronize the burst. Details |
| ModAcc:Measurement Enabled | Specifies whether to enable modulation accuracy (ModAcc) measurements on the acquired signal. Details |
| ModAcc:Averaging:Enabled | Specifies whether to enable averaging for the modulation accuracy (ModAcc) measurement. Details |
| ModAcc:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the ModAcc Averaging Enabled property to True. Details |
| ModAcc:Droop Compensation Enabled | Specifies whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results. Details |
| ModAcc:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement. Details |
| ModAcc:Number of Analysis Threads | Specifies the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. Details |
| ModAcc:Results:EVM:Mean RMS (%) | Returns the mean of RMS values of EVM measured over all acquisition time slots. This value is expressed as a percentage. The property returns this result for EDGE/EGPRS measurements. Details |
| ModAcc:Results:EVM:Maximum RMS (%) | Returns the maximum of RMS values of EVM measured over all acquisition time slots. This value is expressed as a percentage. The property returns this result for EDGE/EGPRS measurements. Details |
| ModAcc:Results:EVM:Mean Peak (%) | Returns the mean of the peak EVM values measured over all acquisition time slots. This value is expressed as a percentage. The property returns this result for EDGE/EGPRS measurements. Details |
| ModAcc:Results:EVM:Maximum Peak (%) | Returns the maximum of the peak EVM values measured over all acquisition time slots. This value is expressed as a percentage. The property returns this result for EDGE/EGPRS measurements. Details |
| ModAcc:Results:EVM:95th percentile (%) | Returns the EVM value at which no more than 5% of the symbols have an EVM exceeding this value. This value is expressed as a percentage. The property returns this result for EDGE/EGPRS measurements. Details |
| ModAcc:Results:EVM:Peak EVM Symbol | Returns the symbol number in the useful portion of the burst corresponding to ModAcc Results EVM Max Pk EVM result. The property returns this result for ModAcc EDGE/EGPRS measurements. Details |
| ModAcc:Results:EVM:Magnitude Error:Mean (%) | Returns the mean of RMS values of magnitude error measured over all acquisition time slots. This value is expressed as a percentage. The property returns this result for EDGE/EGPRS measurements. Details |
| ModAcc:Results:EVM:Magnitude Error:Maximum (%) | Returns the maximum of RMS values of magnitude error measured over all acquisition time slots. This value is expressed as a percentage. The property returns this result for EDGE/EGPRS measurements. Details |
| ModAcc:Results:EVM:Magnitude Error:Mean Peak (%) | Returns the mean of peak magnitude error values measured over all timeslots of all acquisitions. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage. Details |
| ModAcc:Results:EVM:Magnitude Error:Maximum Peak (%) | Returns the maximum of peak magnitude error values measured over all time slots of all acquisitions. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage. Details |
| ModAcc:Results:EVM:Magnitude Error:95th percentile (%) | Returns the measured magnitude error value multiplied by 100, at which, no more than 5 percent of the symbols have magnitude error exceeding this value. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage. Details |
| ModAcc:Results:EVM:Phase Error:Mean (deg) | Returns the mean of RMS values of phase error measured over all acquisition time slots. This value is expressed in degrees. The property returns this result for EDGE/EGPRS measurements. Details |
| ModAcc:Results:EVM:Phase Error:Maximum (deg) | Returns the maximum of the RMS values of phase error measured over all acquisition time slots. This value is expressed in degrees. The property returns this result for EDGE/EGPRS measurements. Details |
| ModAcc:Results:EVM:Phase Error:Mean Peak (deg) | Returns the mean of peak phase error values measured over all timeslots of all acquisitions. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees. Details |
| ModAcc:Results:EVM:Phase Error:Maximum Peak (deg) | Returns the maximum of peak phase error values measured over all timeslots of all acquisitions. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees. Details |
| ModAcc:Results:EVM:Phase Error:95th percentile (deg) | Returns the measured phase error value multiplied by 100, at which, no more than 5 percent of the symbols have phase error exceeding this value. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees. Details |
| ModAcc:Results:EVM:Frequency Error:Mean (Hz) | Returns the mean of the frequency error values measured over all acquisition time slots. This value is expressed in Hz. The property returns this result for EDGE/EGPRS measurements. Details |
| ModAcc:Results:EVM:Frequency Error:Maximum (Hz) | Returns the maximum of the frequency error values measured over all acquisition time slots. This value is expressed in Hz. The property returns this result for EDGE/EGPRS measurements. Details |
| ModAcc:Results:EVM:Amplitude Droop:Mean (dB/symbol) | Returns the mean of the amplitude droop values measured over all acquisition time slots. This value is expressed in dB/symbol. The property returns this result for EDGE/EGPRS measurements. Details |
| ModAcc:Results:EVM:Amplitude Droop:Maximum (dB/symbol) | Returns the maximum of the amplitude droop values measured over all acquisition time slots. This value is expressed in dB/symbol. The property returns this result for EDGE/EGPRS measurements. Details |
| ModAcc:Results:PFER:Phase Error:Mean RMS (deg) | Returns the mean of RMS values of phase error measured over all acquisition time slots. This value is expressed in degrees. The property returns this result for GSM ModAcc measurements. Details |
| ModAcc:Results:PFER:Phase Error:Maximum RMS (deg) | Returns the maximum of the RMS values of phase error measured over all acquisition time slots. This value is expressed in degrees. The property returns this result for GSM ModAcc measurements. Details |
| ModAcc:Results:PFER:Phase Error:Mean Peak (deg) | Returns the mean of peak phase error values measured over all acquisition time slots. This value is expressed in degrees. The property returns this result for GSM ModAcc measurements. Details |
| ModAcc:Results:PFER:Phase Error:Maximum Peak (deg) | Returns the maximum of peak phase error values measured over all acquisition time slots. This value is expressed in degrees. The property returns this result for GSM ModAcc measurements. Details |
| ModAcc:Results:PFER:Phase Error:Peak Symbol | Returns the symbol number in the useful portion of the burst corresponding to the phase error value in the ModAcc Results PFER Max Pk Phase Error result. The property returns this result for GSM ModAcc measurements. Details |
| ModAcc:Results:PFER:Phase Error:95th percentile (deg) | Returns the measured phase error value multiplied by 100, at which, no more than 5 percent of the symbols have phase error exceeding this value. This result is returned while performing ModAcc measurement on GSM. This value is measured in degrees. Details |
| ModAcc:Results:PFER:Frequency Error:Mean (Hz) | Returns the mean of the frequency error values measured over all acquisition time slots. This value is expressed in Hz. The property returns this result for GSM ModAcc measurements. Details |
| ModAcc:Results:PFER:Frequency Error:Maximum (Hz) | Returns the maximum of the frequency error values measured over all acquisition time slots. This value is expressed in Hz. The property returns this result for GSM ModAcc measurements. Details |
| ModAcc:Results:IQ Gain Imbalance:Mean (dB) | Returns the mean of I/Q gain imbalance values measured over all acquisition time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. Details |
| ModAcc:Results:IQ Gain Imbalance:Maximum (dB) | Returns the maximum of I/Q gain imbalance values measured over all acquisition time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. Details |
| ModAcc:Results:IQ Origin Offset:Mean (dB) | Returns the mean of the I/Q origin offset values measured over all acquisition time slots. This value is expressed in dB. Presence of I/Q gain imbalance and quadrature skew in the signal affects the I/Q origin offset measurement. The property returns this result for GSM/EDGE/EGPRS measurements. Details |
| ModAcc:Results:IQ Origin Offset:Maximum (dB) | Returns the maximum of the I/Q origin offset values measured over all acquisition time slots. This value is expressed in dB. Presence of I/Q gain imbalance and quadrature skew in the signal affects the I/Q origin offset measurement. The property returns this result for GSM/EDGE/EGPRS measurements. Details |
| ModAcc:Results:Detected TSC | Returns the detected training sequence code (TSC) if you set the Burst Sync Type property to TSC. Use "slot<n>" as the selector string to read this result. Details |
| ORFS:Measurement Enabled | Specifies whether to enable the output radio frequency spectrum (ORFS) measurement. Details |
| ORFS:Averaging:Enabled | Specifies whether to enable averaging for the output radio frequency spectrum (ORFS) measurement. Details |
| ORFS:Averaging:Type | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the output radio frequency spectrum (ORFS) measurement. Details |
| ORFS:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the ORFS Averaging Enabled property to True. Details |
| ORFS:Measurement Type | Specifies the type of spectral distortion to be measured. Details |
| ORFS:Offset Frequency Mode | Specifies the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements. Details |
| ORFS:Evaluation Symbols:Start (%) | Specifies the start position within the useful part of the burst, in percentage, for measuring ORFS due to modulation. Details |
| ORFS:Evaluation Symbols:Include TSC | Specifies whether to include the training sequence code (TSC) portion of burst for measuring ORFS due to modulation. Details |
| ORFS:Evaluation Symbols:Stop (%) | Specifies the stop position within the useful part of the burst, in percentage, for measuring ORFS due to modulation. Details |
| ORFS:Evaluation Symbols:Scope | Specifies the modulation power measurements that will use the part of burst configured using the RFmxGSM ORFS Configure Evaluation Symbols VI. Details |
| ORFS:Modulation:Carrier RBW (Hz) | Specifies the RBW used for measuring modulation carrier power in Hz. Details |
| ORFS:Modulation:Number of Offsets | Specifies the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to modulation. Details |
| ORFS:Modulation:Offset Frequency (Hz) | Specifies the value of positive frequency offset for which to measure the spectrum due to modulation measurement. This value is expressed in Hz. Details |
| ORFS:Modulation:Offset RBW (Hz) | Specifies the resolution bandwidth used for ORFS due to modulation measurement. This value is expressed in Hz. Details |
| ORFS:Switching:Carrier RBW (Hz) | Specifies the RBW used for measuring switching carrier power in Hz. Details |
| ORFS:Switching:Number of Offsets | Specifies the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to switching. Details |
| ORFS:Switching:Offset Frequency (Hz) | Specifies the value of positive frequency offset for which to measure the spectrum due to switching measurement. This value is expressed in Hz. Details |
| ORFS:Switching:Offset RBW (Hz) | Specifies the resolution bandwidth used for ORFS due to switching measurement. This value is expressed in Hz. Details |
| ORFS:Noise Compensation Enabled | Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Noise compensation is applicable only on modulation offsets and not on switching offsets. Details |
| ORFS:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the output radio frequency spectrum (ORFS) measurement. Details |
| ORFS:Number of Analysis Threads | Specifies the maximum number of threads used for parallelism for the output radio frequency spectrum (ORFS) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. Details |
| PVT:Measurement Enabled | Specifies whether to enable the power versus time (PVT) measurement. Details |
| PVT:Averaging:Enabled | Specifies whether to enable averaging for the power versus time (PVT) measurement. Details |
| PVT:Averaging:Type | Specifies the averaging type for multiple acquisitions. Details |
| PVT:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the PVT Averaging Enabled property to True. Details |
| PVT:RBW Filter:Bandwidth (Hz) | Specifies the RBW Filter Bandwidth in Hz Details |
| PVT:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the power versus time (PVT) measurement. Details |
| PVT:Number of Analysis Threads | Specifies the maximum number of threads used for parallelism for the power versus time (PVT) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. Details |
| PVT:Results:Measurement Status | Indicates the overall measurement status based on standard-defined limits. Details |
| PVT:Results:Slot:Average Power (dBm) | Returns the mean power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. Use "slot<n>" as the selector string to read this property. Details |
| PVT:Results:Slot:Burst Width (s) | Returns the burst width for the slot where the -3 dB transition points occur. This value is expressed in seconds. Use "slot<n>" as the selector string to read this property. Details |
| PVT:Results:Slot:Maximum Power (dBm) | Returns the maximum power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. Use "slot<n>" as the selector string to read this property. Details |
| PVT:Results:Slot:Minimum Power (dBm) | Returns the minimum power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. Use "slot<n>" as the selector string to read this property. Details |
| PVT:Results:Slot:Burst Threshold (dBm) | Returns the threshold that the power versus time (PVT) measurement uses to determine the burst validity. This value is expressed in dBm. Use "slot<n>" as the selector string to read this property. Details |
| PVT:Results:Slot:Measurement Status | Indicates the power versus time (PVT) measurement status for a particular slot. Use "slot<n>" as the selector string to read this property. Details |
| Advanced:Auto Level Initial Reference Level (dBm) | Specifies the initial reference level the RFmxGSM Auto Level VI uses to estimate the peak power of the input signal. This value is expressed in dBm. Details |
| Advanced:Limited Configuration Change | Specifies the set of properties that are considered by RFmx in the locked signal configuration state. Details |
| Result Fetch Timeout (s) | Specifies the time to wait before results are available in the RFmxGSM Property Node. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxGSM Property Node waits until the measurement is complete. Details |
