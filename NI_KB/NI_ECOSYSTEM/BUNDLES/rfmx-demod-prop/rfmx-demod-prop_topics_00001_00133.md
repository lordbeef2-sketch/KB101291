# NI DOCUMENT BUNDLE: rfmx-demod-prop

<!--NI_BUNDLE_CHUNK bundle=rfmx-demod-prop start=1 end=133 -->
<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr0.html language=enus -->
## TOPIC 00001: rfmxdemodprop/attr0.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr0.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr0.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Selector String Property

Selector String Property

**Short Name:**Selector String

Property of [RFmxDemod](crfmxdemod.html)

Specifies the selector string used to access all subsequent selector string-based properties in this instance of the property node.

If the property you want to use is selector string-based, you must first set the Selector String property and then set the selector string-based property in the same property node. If a property is not selector string-based, and you set the Selector String property in this property node, RFmxDemod returns an error.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Write Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200002.html language=enus -->
## TOPIC 00002: rfmxdemodprop/attr200002.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200002.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:AM Carrier Suppressed Property

Analog Demod:AM Carrier Suppressed Property

**Short Name:**ADemod AM Carrier Suppressed

Property of [RFmxDemod](crfmxdemod.html)

Specifies whether the carrier of the AM (amplitude modulated) signal is absent.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The carrier of the AM signal is present. |
| --- | --- |
| True (1) | The carrier of the AM signal is absent. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod ADemod Configure AM Carrier Suppressed |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200003.html language=enus -->
## TOPIC 00003: rfmxdemodprop/attr200003.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200003.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Audio Filter:Type Property

Analog Demod:Audio Filter:Type Property

**Short Name:**ADemod Audio Filter Type

Property of [RFmxDemod](crfmxdemod.html)

Specifies the audio filter to be applied on the analog demodulated signal.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **None**.

| None (0) | Does not use any audio filter. |
| --- | --- |
| Custom (1) | Uses the filter specified by the Ademod Audio Filter Lower Cutoff property and the Ademod Audio Filter Upper Cutoff property. |
| A - Weight (2) | Uses an A-weighted filter. |
| B - Weight (3) | Uses a B-weighted filter. |
| C - Weight (4) | Uses a C-weighted filter. |
| CCITT (5) | Uses the filter specified by CCITT. |
| ITU-R 468-4 (6) | Uses the filter specified by ITU-R 468-4. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod ADemod Configure Audio Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200004.html language=enus -->
## TOPIC 00004: rfmxdemodprop/attr200004.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200004.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Audio Filter:Lower Cutoff Frequency (Hz) Property

Analog Demod:Audio Filter:Lower Cutoff Frequency (Hz) Property

**Short Name:**ADemod Audio Filter Lower Cutoff (Hz)

Property of [RFmxDemod](crfmxdemod.html)

Specifies the lower cutoff frequency of the custom audio filter. This property is applicable only when you set the [ADemod Audio Filter Type](attr200003.html) property to **Custom**. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 100.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod ADemod Configure Audio Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200005.html language=enus -->
## TOPIC 00005: rfmxdemodprop/attr200005.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200005.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Audio Filter:Upper Cutoff Frequency (Hz) Property

Analog Demod:Audio Filter:Upper Cutoff Frequency (Hz) Property

**Short Name:**ADemod Audio Filter Upper Cutoff (Hz)

Property of [RFmxDemod](crfmxdemod.html)

Specifies the upper cutoff frequency of the custom audio filter. This property is applicable only when you set the [ADemod Audio Filter Type](attr200003.html) property to **Custom**. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 10,000.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod ADemod Configure Audio Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200006.html language=enus -->
## TOPIC 00006: rfmxdemodprop/attr200006.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200006.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Averaging:Enabled Property

Analog Demod:Averaging:Enabled Property

**Short Name:**ADemod Averaging Enabled

Property of [RFmxDemod](crfmxdemod.html)

Specifies whether to enable averaging for the analog demodulation measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The measurement is performed on a single acquisition. |
| --- | --- |
| True (1) | The analog demodulation measurement uses the ADemod Averaging Count property to calculate the number of acquisitions over which the measurement is averaged. Traces are not averaged. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200007.html language=enus -->
## TOPIC 00007: rfmxdemodprop/attr200007.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200007.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Averaging:Count Property

Analog Demod:Averaging:Count Property

**Short Name:**ADemod Averaging Count

Property of [RFmxDemod](crfmxdemod.html)

Specifies the number of acquisitions used for averaging when you set the [ADemod Averaging Enabled](attr200006.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200009.html language=enus -->
## TOPIC 00008: rfmxdemodprop/attr200009.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200009.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200009.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Averaging:Type Property

Analog Demod:Averaging:Type Property

**Short Name:**ADemod Averaging Type

Property of [RFmxDemod](crfmxdemod.html)

Specifies the averaging type for the measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Linear**.

| Linear (0) | The averaged result is the mean value measured across multiple acquisitions. |
| --- | --- |
| Max (1) | The averaged result is the maximum value measured across multiple acquisitions. |
| Min (2) | The averaged result is the minimum value measured across multiple acquisitions. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20000a.html language=enus -->
## TOPIC 00009: rfmxdemodprop/attr20000a.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20000a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20000a.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Carrier Correction:Frequency Enabled Property

Analog Demod:Carrier Correction:Frequency Enabled Property

**Short Name:**ADemod Carrier Frequency Correction Enabled

Property of [RFmxDemod](crfmxdemod.html)

Specifies whether to correct the frequency error in the carrier when demodulating frequency-modulated (FM) or phase-modulated (PM) signals.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | Does not correct the carrier frequency error. |
| --- | --- |
| True (1) | Corrects the carrier frequency error. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod ADemod Configure Carrier Correction |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20000b.html language=enus -->
## TOPIC 00010: rfmxdemodprop/attr20000b.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20000b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20000b.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Carrier Correction:Phase Enabled Property

Analog Demod:Carrier Correction:Phase Enabled Property

**Short Name:**ADemod Carrier Phase Correction Enabled

Property of [RFmxDemod](crfmxdemod.html)

Specifies whether to correct the carrier phase error when demodulating phase-modulated signals.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | Does not correct the carrier phase error. |
| --- | --- |
| True (1) | Corrects the carrier phase error. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod ADemod Configure Carrier Correction |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20000c.html language=enus -->
## TOPIC 00011: rfmxdemodprop/attr20000c.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20000c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20000c.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:FM DeEmphasis (s) Property

Analog Demod:FM DeEmphasis (s) Property

**Short Name:**ADemod FM DeEmphasis (s)

Property of [RFmxDemod](crfmxdemod.html)

Specifies the time constant of de-emphasis filter, which compensates for the pre-emphasis filter in the FM transmitter. This value is expressed in seconds.

The lowpass characteristic transfer function of the de-emphasis filter is as shown in the following equation:

*H*(*f*) = 1/(1+*j*(2*pi**f**τ)

where τ is the de-emphasis filter time constant. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0 seconds. No filter is applied on the demodulated signal when de-emphasis is set to 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod ADemod Configure FM DeEmphasis |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20000d.html language=enus -->
## TOPIC 00012: rfmxdemodprop/attr20000d.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20000d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20000d.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Measurement Interval (s) Property

Analog Demod:Measurement Interval (s) Property

**Short Name:**ADemod Meas Interval (s)

Property of [RFmxDemod](crfmxdemod.html)

Specifies the signal acquisition time for the analog demodulation measurement. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 10 ms.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod ADemod Configure Measurement Interval |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20000e.html language=enus -->
## TOPIC 00013: rfmxdemodprop/attr20000e.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20000e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20000e.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Modulation Type Property

Analog Demod:Modulation Type Property

**Short Name:**ADemod Modulation Type

Property of [RFmxDemod](crfmxdemod.html)

Specifies the analog modulation type of the signal that needs to be analyzed.

The default value is **AM**.

| AM (0) | The signal to be analyzed is amplitude modulated. |
| --- | --- |
| FM (1) | The signal to be analyzed is frequency modulated. |
| PM (2) | The signal to be analyzed is phase modulated. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod ADemod Configure Modulation Type |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200010.html language=enus -->
## TOPIC 00014: rfmxdemodprop/attr200010.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200010.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200010.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:RBW Filter:Type Property

Analog Demod:RBW Filter:Type Property

**Short Name:**ADemod RBW Filter Type

Property of [RFmxDemod](crfmxdemod.html)

Specifies the shape of the digital RBW filter.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Flat**.

| None (0) | RBW filter is not applied on the acquired signal. |
| --- | --- |
| Gaussian (1) | RBW filter has a Gaussian response. |
| Flat (2) | RBW filter has a Flat response. |
| Synch Tuned - 4 (3) | RBW filter has a response of a 4-pole synchronously-tuned filter. |
| Synch Tuned - 5 (4) | RBW filter has a response of a 5-pole synchronously-tuned filter. |
| RRC (5) | RRC filter with roll-off specified by the ADemod RBW RRC Alpha property is used as the RBW filter. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod ADemod Configure RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200011.html language=enus -->
## TOPIC 00015: rfmxdemodprop/attr200011.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200011.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200011.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:RBW Filter:Bandwidth (Hz) Property

Analog Demod:RBW Filter:Bandwidth (Hz) Property

**Short Name:**ADemod RBW (Hz)

Property of [RFmxDemod](crfmxdemod.html)

Specifies the bandwidth of the resolution bandwidth (RBW) filter to be applied to the acquired signal. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 100 kHz.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod ADemod Configure RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200012.html language=enus -->
## TOPIC 00016: rfmxdemodprop/attr200012.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200012.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200012.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:RBW Filter:Alpha Property

Analog Demod:RBW Filter:Alpha Property

**Short Name:**ADemod RBW RRC Alpha

Property of [RFmxDemod](crfmxdemod.html)

Specifies the roll-off factor of the root-raised cosine (RRC) filter.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0.1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod ADemod Configure RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200013.html language=enus -->
## TOPIC 00017: rfmxdemodprop/attr200013.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200013.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200013.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:All Traces Enabled Property

Analog Demod:All Traces Enabled Property

**Short Name:**ADemod All Traces Enabled

Property of [RFmxDemod](crfmxdemod.html)

Specifies whether to enable the traces to be stored and retrieved after performing the analog demodulation measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod Select Measurement |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200014.html language=enus -->
## TOPIC 00018: rfmxdemodprop/attr200014.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200014.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200014.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:Mean Carrier Frequency Error (Hz) Property

Analog Demod:Results:Mean Carrier Frequency Error (Hz) Property

**Short Name:**ADemod Results Mean Carrier Freq Error (Hz)

Property of [RFmxDemod](crfmxdemod.html)

Returns the mean of the measured carrier frequency offset. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200015.html language=enus -->
## TOPIC 00019: rfmxdemodprop/attr200015.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200015.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200015.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:Mean Carrier Power (dBm) Property

Analog Demod:Results:Mean Carrier Power (dBm) Property

**Short Name:**ADemod Results Mean Carrier Power (dBm)

Property of [RFmxDemod](crfmxdemod.html)

Returns the mean of the measured carrier power. This value is expressed in dBm.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200016.html language=enus -->
## TOPIC 00020: rfmxdemodprop/attr200016.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200016.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200016.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:Mean Modulation Frequency (Hz) Property

Analog Demod:Results:Mean Modulation Frequency (Hz) Property

**Short Name:**ADemod Results Mean Modulation Freq (Hz)

Property of [RFmxDemod](crfmxdemod.html)

Returns the mean of the demodulated signal frequency. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200017.html language=enus -->
## TOPIC 00021: rfmxdemodprop/attr200017.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200017.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200017.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:Average SINAD (dB) Property

Analog Demod:Results:Average SINAD (dB) Property

**Short Name:**ADemod Results Average SINAD (dB)

Property of [RFmxDemod](crfmxdemod.html)

Returns the averaged signal-to-noise and distortion ratio of the demodulated signal. This value is expressed in dB.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200018.html language=enus -->
## TOPIC 00022: rfmxdemodprop/attr200018.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200018.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200018.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:Average THD with Noise (%) Property

Analog Demod:Results:Average THD with Noise (%) Property

**Short Name:**ADemod Results Average THD with Noise (%)

Property of [RFmxDemod](crfmxdemod.html)

Returns the averaged total harmonic distortion with noise of the demodulated signal, as a percentage.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200019.html language=enus -->
## TOPIC 00023: rfmxdemodprop/attr200019.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200019.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200019.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:Average THD (%) Property

Analog Demod:Results:Average THD (%) Property

**Short Name:**ADemod Results Average THD (%)

Property of [RFmxDemod](crfmxdemod.html)

Returns the averaged total harmonic distortion of the demodulated signal, as a percentage.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20001a.html language=enus -->
## TOPIC 00024: rfmxdemodprop/attr20001a.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20001a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20001a.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:Average SNR (dB) Property

Analog Demod:Results:Average SNR (dB) Property

**Short Name:**ADemod Results Average SNR (dB)

Property of [RFmxDemod](crfmxdemod.html)

Returns the averaged signal-to-noise ratio of the demodulated signal. This value is expressed in dB.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20001b.html language=enus -->
## TOPIC 00025: rfmxdemodprop/attr20001b.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20001b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20001b.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:AM Modulation Depth:Mean Standard Deviation (%) Property

Analog Demod:Results:AM Modulation Depth:Mean Standard Deviation (%) Property

**Short Name:**ADemod Results AM Mod Depth Mean Std Dev(%)

Property of [RFmxDemod](crfmxdemod.html)

Returns the mean amplitude variation around the unmodulated carrier amplitude, as a percentage. If the carrier is suppressed, the amplitude variation of the modulating signal is returned.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20001c.html language=enus -->
## TOPIC 00026: rfmxdemodprop/attr20001c.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20001c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20001c.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:AM Modulation Depth:Mean Peak to Peak /2 (%) Property

Analog Demod:Results:AM Modulation Depth:Mean Peak to Peak /2 (%) Property

**Short Name:**ADemod Results AM Mean Mod Depth Pk to Pk/2 (%)

Property of [RFmxDemod](crfmxdemod.html)

Returns the mean (peak-to-peak)/2 amplitude of the modulating signal, as a percentage.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20001d.html language=enus -->
## TOPIC 00027: rfmxdemodprop/attr20001d.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20001d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20001d.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:AM Modulation Depth:Mean Positive Peak (%) Property

Analog Demod:Results:AM Modulation Depth:Mean Positive Peak (%) Property

**Short Name:**ADemod Results AM Mean Mod Depth Pos Pk (%)

Property of [RFmxDemod](crfmxdemod.html)

Returns the mean positive peak amplitude of the modulating signal, as a percentage.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20001e.html language=enus -->
## TOPIC 00028: rfmxdemodprop/attr20001e.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20001e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20001e.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:AM Modulation Depth:Mean Negative Peak (%) Property

Analog Demod:Results:AM Modulation Depth:Mean Negative Peak (%) Property

**Short Name:**ADemod Results AM Mean Mod Depth Neg Pk (%)

Property of [RFmxDemod](crfmxdemod.html)

Returns the mean negative peak amplitude of the modulating signal, as a percentage.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20001f.html language=enus -->
## TOPIC 00029: rfmxdemodprop/attr20001f.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20001f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20001f.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:AM Modulation Depth:Mean RMS (%) Property

Analog Demod:Results:AM Modulation Depth:Mean RMS (%) Property

**Short Name:**ADemod Results AM Mean Mod Depth RMS (%)

Property of [RFmxDemod](crfmxdemod.html)

Returns the mean RMS amplitude of the modulating signal, as a percentage.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200020.html language=enus -->
## TOPIC 00030: rfmxdemodprop/attr200020.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200020.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200020.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:AM Modulation Depth:Maximum Standard Deviation (%) Property

Analog Demod:Results:AM Modulation Depth:Maximum Standard Deviation (%) Property

**Short Name:**ADemod Results AM Mod Depth Std Dev (%)

Property of [RFmxDemod](crfmxdemod.html)

Returns the maximum modulation depth measured across multiple acquisitions, as a percentage.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200021.html language=enus -->
## TOPIC 00031: rfmxdemodprop/attr200021.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200021.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200021.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:AM Modulation Depth:Maximum Peak to Peak /2 (%) Property

Analog Demod:Results:AM Modulation Depth:Maximum Peak to Peak /2 (%) Property

**Short Name:**ADemod Results AM Max Mod Depth Pk to Pk /2 (%)

Property of [RFmxDemod](crfmxdemod.html)

Returns the maximum (peak-to-peak)/2 amplitude of the modulating signal measured across multiple acquisitions, as a percentage.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200022.html language=enus -->
## TOPIC 00032: rfmxdemodprop/attr200022.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200022.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200022.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:AM Modulation Depth:Maximum Positive Peak (%) Property

Analog Demod:Results:AM Modulation Depth:Maximum Positive Peak (%) Property

**Short Name:**ADemod Results AM Max Mod Depth Pos Pk (%)

Property of [RFmxDemod](crfmxdemod.html)

Returns the maximum positive peak amplitude of the modulating signal measured across multiple acquisitions, as a percentage.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200023.html language=enus -->
## TOPIC 00033: rfmxdemodprop/attr200023.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200023.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200023.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:AM Modulation Depth:Maximum Negative Peak (%) Property

Analog Demod:Results:AM Modulation Depth:Maximum Negative Peak (%) Property

**Short Name:**ADemod Results AM Max Mod Depth Neg Pk (%)

Property of [RFmxDemod](crfmxdemod.html)

Returns the maximum negative peak amplitude of the modulating signal measured across multiple acquisitions, as a percentage.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200024.html language=enus -->
## TOPIC 00034: rfmxdemodprop/attr200024.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200024.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200024.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:AM Modulation Depth:Maximum RMS (%) Property

Analog Demod:Results:AM Modulation Depth:Maximum RMS (%) Property

**Short Name:**ADemod Results AM Max Mod Depth RMS (%)

Property of [RFmxDemod](crfmxdemod.html)

Returns the maximum RMS amplitude of the modulating signal measured across multiple acquisitions, as a percentage.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200025.html language=enus -->
## TOPIC 00035: rfmxdemodprop/attr200025.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200025.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200025.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:FM Deviation:Mean Standard Deviation (Hz) Property

Analog Demod:Results:FM Deviation:Mean Standard Deviation (Hz) Property

**Short Name:**ADemod Results FM Mean Std Dev (Hz)

Property of [RFmxDemod](crfmxdemod.html)

Returns the mean frequency deviation around the nominal frequency of the FM carrier. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200026.html language=enus -->
## TOPIC 00036: rfmxdemodprop/attr200026.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200026.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200026.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:FM Deviation:Mean Peak to Peak /2 (Hz) Property

Analog Demod:Results:FM Deviation:Mean Peak to Peak /2 (Hz) Property

**Short Name:**ADemod Results FM Mean Deviation Pk to Pk/2 (Hz)

Property of [RFmxDemod](crfmxdemod.html)

Returns the mean (peak-to-peak)/2 frequency variation around the nominal frequency of the FM carrier. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200027.html language=enus -->
## TOPIC 00037: rfmxdemodprop/attr200027.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200027.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200027.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:FM Deviation:Mean Positive Peak (Hz) Property

Analog Demod:Results:FM Deviation:Mean Positive Peak (Hz) Property

**Short Name:**ADemod Results FM Mean Deviation Pos Pk (Hz)

Property of [RFmxDemod](crfmxdemod.html)

Returns the mean positive peak frequency deviation of the frequency-modulated signal. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200028.html language=enus -->
## TOPIC 00038: rfmxdemodprop/attr200028.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200028.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200028.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:FM Deviation:Mean Negative Peak (Hz) Property

Analog Demod:Results:FM Deviation:Mean Negative Peak (Hz) Property

**Short Name:**ADemod Results FM Mean Deviation Neg Pk (Hz)

Property of [RFmxDemod](crfmxdemod.html)

Returns the mean negative peak frequency deviation of the frequency-modulated signal. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200029.html language=enus -->
## TOPIC 00039: rfmxdemodprop/attr200029.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200029.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200029.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:FM Deviation:Mean RMS (Hz) Property

Analog Demod:Results:FM Deviation:Mean RMS (Hz) Property

**Short Name:**ADemod Results FM Mean Deviation RMS (Hz)

Property of [RFmxDemod](crfmxdemod.html)

Returns the mean RMS frequency deviation of the frequency-modulated signal. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20002a.html language=enus -->
## TOPIC 00040: rfmxdemodprop/attr20002a.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20002a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20002a.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:FM Deviation:Maximum Standard Deviation (Hz) Property

Analog Demod:Results:FM Deviation:Maximum Standard Deviation (Hz) Property

**Short Name:**ADemod Results FM Max Std Dev (Hz)

Property of [RFmxDemod](crfmxdemod.html)

Returns the maximum frequency deviation of the frequency-modulated signal measured across multiple acquisitions. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20002b.html language=enus -->
## TOPIC 00041: rfmxdemodprop/attr20002b.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20002b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20002b.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:FM Deviation:Maximum Peak to Peak /2 (Hz) Property

Analog Demod:Results:FM Deviation:Maximum Peak to Peak /2 (Hz) Property

**Short Name:**ADemod Results FM Max Deviation Pk to Pk /2 (Hz)

Property of [RFmxDemod](crfmxdemod.html)

Returns the maximum (peak-to-peak)/2 frequency variation around the nominal frequency of the FM carrier measured across multiple acquisitions. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20002c.html language=enus -->
## TOPIC 00042: rfmxdemodprop/attr20002c.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20002c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20002c.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:FM Deviation:Maximum Positive Peak (Hz) Property

Analog Demod:Results:FM Deviation:Maximum Positive Peak (Hz) Property

**Short Name:**ADemod Results FM Max Deviation Pos Pk (Hz)

Property of [RFmxDemod](crfmxdemod.html)

Returns the maximum positive peak frequency deviation of the frequency-modulated signal measured across multiple acquisitions. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20002d.html language=enus -->
## TOPIC 00043: rfmxdemodprop/attr20002d.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20002d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20002d.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:FM Deviation:Maximum Negative Peak (Hz) Property

Analog Demod:Results:FM Deviation:Maximum Negative Peak (Hz) Property

**Short Name:**ADemod Results FM Max Deviation Neg Pk (Hz)

Property of [RFmxDemod](crfmxdemod.html)

Returns the maximum negative peak frequency deviation of the frequency-modulated signal measured across multiple acquisitions. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20002e.html language=enus -->
## TOPIC 00044: rfmxdemodprop/attr20002e.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20002e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20002e.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:FM Deviation:Maximum RMS (Hz) Property

Analog Demod:Results:FM Deviation:Maximum RMS (Hz) Property

**Short Name:**ADemod Results FM Max Deviation RMS (Hz)

Property of [RFmxDemod](crfmxdemod.html)

Returns the maximum RMS frequency deviation of the frequency-modulated signal measured across multiple acquisitions. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20002f.html language=enus -->
## TOPIC 00045: rfmxdemodprop/attr20002f.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20002f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20002f.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:PM Deviation:Mean Standard Deviation (deg) Property

Analog Demod:Results:PM Deviation:Mean Standard Deviation (deg) Property

**Short Name:**ADemod Results PM Mean Std Dev (deg)

Property of [RFmxDemod](crfmxdemod.html)

Returns the mean phase deviation around the unmodulated carrier phase. This value is expressed in degrees.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200030.html language=enus -->
## TOPIC 00046: rfmxdemodprop/attr200030.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200030.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200030.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:PM Deviation:Mean Peak to Peak /2 (deg) Property

Analog Demod:Results:PM Deviation:Mean Peak to Peak /2 (deg) Property

**Short Name:**ADemod Results PM Mean Deviation Pk to Pk /2 (deg)

Property of [RFmxDemod](crfmxdemod.html)

Returns the mean (peak-to-peak)/2 phase deviation around the unmodulated carrier phase. This value is expressed in degrees.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200031.html language=enus -->
## TOPIC 00047: rfmxdemodprop/attr200031.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200031.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200031.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:PM Deviation:Mean Positive Peak (deg) Property

Analog Demod:Results:PM Deviation:Mean Positive Peak (deg) Property

**Short Name:**ADemod Results PM Mean Deviation Pos Pk (deg)

Property of [RFmxDemod](crfmxdemod.html)

Returns the mean positive peak phase deviation around the unmodulated carrier phase. This value is expressed in degrees.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200032.html language=enus -->
## TOPIC 00048: rfmxdemodprop/attr200032.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200032.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200032.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:PM Deviation:Mean Negative Peak (deg) Property

Analog Demod:Results:PM Deviation:Mean Negative Peak (deg) Property

**Short Name:**ADemod Results PM Mean Deviation Neg Pk (deg)

Property of [RFmxDemod](crfmxdemod.html)

Returns the mean negative peak phase deviation around the unmodulated carrier phase. This value is expressed in degrees.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200033.html language=enus -->
## TOPIC 00049: rfmxdemodprop/attr200033.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200033.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200033.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:PM Deviation:Mean RMS (deg) Property

Analog Demod:Results:PM Deviation:Mean RMS (deg) Property

**Short Name:**ADemod Results PM Mean Deviation RMS (deg)

Property of [RFmxDemod](crfmxdemod.html)

Returns the mean RMS phase deviation of the phase-modulated signal. This value is expressed in degrees.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200034.html language=enus -->
## TOPIC 00050: rfmxdemodprop/attr200034.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200034.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200034.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:PM Deviation:Maximum Standard Deviation (deg) Property

Analog Demod:Results:PM Deviation:Maximum Standard Deviation (deg) Property

**Short Name:**ADemod Results PM Max Std Dev (deg)

Property of [RFmxDemod](crfmxdemod.html)

Returns the maximum phase deviation around the unmodulated carrier phase, measured across multiple acquisitions. This value is expressed in degrees.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200035.html language=enus -->
## TOPIC 00051: rfmxdemodprop/attr200035.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200035.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200035.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:PM Deviation:Maximum Peak to Peak /2 (deg) Property

Analog Demod:Results:PM Deviation:Maximum Peak to Peak /2 (deg) Property

**Short Name:**ADemod Results PM Max Deviation Pk to Pk /2 (deg)

Property of [RFmxDemod](crfmxdemod.html)

Returns the maximum (peak-to-peak)/2 phase deviation around the unmodulated carrier phase, measured across multiple acquisitions. This value is expressed in degrees.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200036.html language=enus -->
## TOPIC 00052: rfmxdemodprop/attr200036.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200036.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200036.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:PM Deviation:Maximum Positive Peak (deg) Property

Analog Demod:Results:PM Deviation:Maximum Positive Peak (deg) Property

**Short Name:**ADemod Results PM Max Deviation Pos Pk (deg)

Property of [RFmxDemod](crfmxdemod.html)

Returns the maximum positive peak phase deviation around the unmodulated carrier phase, measured across multiple acquisitions. This value is expressed in degrees.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200037.html language=enus -->
## TOPIC 00053: rfmxdemodprop/attr200037.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200037.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200037.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:PM Deviation:Maximum Negative Peak (deg) Property

Analog Demod:Results:PM Deviation:Maximum Negative Peak (deg) Property

**Short Name:**ADemod Results PM Max Deviation Neg Pk (deg)

Property of [RFmxDemod](crfmxdemod.html)

Returns the maximum negative peak phase deviation around the unmodulated carrier phase, measured across multiple acquisitions. This value is expressed in degrees.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200038.html language=enus -->
## TOPIC 00054: rfmxdemodprop/attr200038.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200038.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200038.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Results:PM Deviation:Maximum RMS (deg) Property

Analog Demod:Results:PM Deviation:Maximum RMS (deg) Property

**Short Name:**ADemod Results PM Max Deviation RMS (deg)

Property of [RFmxDemod](crfmxdemod.html)

Returns the maximum RMS phase deviation of the phase-modulated signal measured across multiple acquisitions. This value is expressed in degrees.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod ADemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200039.html language=enus -->
## TOPIC 00055: rfmxdemodprop/attr200039.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200039.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200039.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Measurement Enabled Property

Analog Demod:Measurement Enabled Property

**Short Name:**ADemod Enabled

Property of [RFmxDemod](crfmxdemod.html)

Specifies whether to enable analog demodulation measurements.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod Select Measurement |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr200040.html language=enus -->
## TOPIC 00056: rfmxdemodprop/attr200040.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr200040.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr200040.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Analog Demod:Audio Measurement Enabled Property

Analog Demod:Audio Measurement Enabled Property

**Short Name:**ADemod Audio Measurement Enabled

Property of [RFmxDemod](crfmxdemod.html)

Specifies whether to enable the audio signal measurements, such as SINAD, SNR, THD and THD+Noise.

The default value is **True**.

| False (0) | Disables the audio measurements. |
| --- | --- |
| True (1) | Enables the audio measurements. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201000.html language=enus -->
## TOPIC 00057: rfmxdemodprop/attr201000.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201000.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Measurement Enabled Property

Digital Demod:Measurement Enabled Property

**Short Name:**DDemod Enabled

Property of [RFmxDemod](crfmxdemod.html)

Enables digital demodulation measurements.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod Select Measurement |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201002.html language=enus -->
## TOPIC 00058: rfmxdemodprop/attr201002.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201002.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Averaging:Enabled Property

Digital Demod:Averaging:Enabled Property

**Short Name:**DDemod Averaging Enabled

Property of [RFmxDemod](crfmxdemod.html)

Enables averaging for digital demodulation measurements.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The measurement is performed on a single acquisition. |
| --- | --- |
| True (1) | The measurement uses the value of the DDemod Averaging Count property for the number of acquisitions over which the measurement is averaged. The traces are not averaged. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201003.html language=enus -->
## TOPIC 00059: rfmxdemodprop/attr201003.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201003.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Averaging:Count Property

Digital Demod:Averaging:Count Property

**Short Name:**DDemod Averaging Count

Property of [RFmxDemod](crfmxdemod.html)

Specifies the number of acquisitions used for averaging when you set the [DDemod Averaging Enabled](attr201002.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201005.html language=enus -->
## TOPIC 00060: rfmxdemodprop/attr201005.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201005.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Differential Enabled Property

Digital Demod:Differential Enabled Property

**Short Name:**DDemod Differential Enabled

Property of [RFmxDemod](crfmxdemod.html)

Specifies whether the symbols are differentially encoded. This property is applicable only to PSK and MSK modulation types.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The symbols are directly mapped onto the symbol map. |
| --- | --- |
| True (1) | In case of PSK modulation, the transition between two consecutive symbols is mapped onto the symbol map. In case of MSK modulation, the consecutive bits are XORed. Other modulation types do not have any impact. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Modulation Type |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201006.html language=enus -->
## TOPIC 00061: rfmxdemodprop/attr201006.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201006.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Equalizer:Mode Property

Digital Demod:Equalizer:Mode Property

**Short Name:**DDemod Equalizer Mode

Property of [RFmxDemod](crfmxdemod.html)

Specifies whether the measurement needs to perform equalization.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Off**.

| Off (0) | Equalization is not performed. |
| --- | --- |
| Train (1) | The adaptive feedforward equalizer is turned ON to compensate for the effect of the channel. You can set the initial coefficients to be used by the equalizer. If you do not specify the initial coefficients, an impulse is used. |
| Hold (2) | The filter that you specify using the RFmxDemod DDemod Configure Equalizer Initial Coefficients VI is used as the channel filter, and it is applied before demodulating the acquired signal. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Equalizer |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201007.html language=enus -->
## TOPIC 00062: rfmxdemodprop/attr201007.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201007.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Equalizer:Convergence Factor Property

Digital Demod:Equalizer:Convergence Factor Property

**Short Name:**DDemod Equalizer Convergence Factor

Property of [RFmxDemod](crfmxdemod.html)

Specifies the incremental step used by the equalizer to adapt to the channel during the training stage.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0.0001

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Equalizer |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201008.html language=enus -->
## TOPIC 00063: rfmxdemodprop/attr201008.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201008.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:FSK:Deviation (Hz) Property

Digital Demod:FSK:Deviation (Hz) Property

**Short Name:**DDemod FSK Deviation (Hz)

Property of [RFmxDemod](crfmxdemod.html)

Specifies the expected FSK frequency deviation At baseband frequencies, deviations for individual symbols are evenly spaced in the interval [-*fd*, *fd*], where *fd* represents the frequency deviation. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 15 kHz.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure FSK Deviation |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201009.html language=enus -->
## TOPIC 00064: rfmxdemodprop/attr201009.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201009.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201009.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:M Property

Digital Demod:M Property

**Short Name:**DDemod M

Property of [RFmxDemod](crfmxdemod.html)

Specifies the M-ary number, which is the number of distinct states that represent symbols in the complex baseband modulated waveform.

The M-ary number is calculated using the following formula:

M = 2<sup>^</sup>(bits per symbol)

Recommended values of M for the modulation types are as follows:

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **4**.

| 2 (2) | The M-ary number is 2. |
| --- | --- |
| 4 (4) | The M-ary number is 4. |
| 8 (8) | The M-ary number is 8. |
| 16 (16) | The M-ary number is 16. |
| 32 (32) | The M-ary number is 32. |
| 64 (64) | The M-ary number is 64. |
| 128 (128) | The M-ary number is 128. |
| 256 (256) | The M-ary number is 256. |
| 512 (512) | The M-ary number is 512. |
| 1024 (1024) | The M-ary number is 1,024. |
| 2048 (2048) | The M-ary number is 2,048. |
| 4096 (4096) | The M-ary number is 4,096. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure M, RFmxDemod DDemod Configure Modulation Type |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20100a.html language=enus -->
## TOPIC 00065: rfmxdemodprop/attr20100a.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20100a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20100a.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Measurement Filter:Type Property

Digital Demod:Measurement Filter:Type Property

**Short Name:**DDemod Meas Filter Type

Property of [RFmxDemod](crfmxdemod.html)

Specifies whether the measurement needs to compute the measurement filter based on the pulse-shaping filter type or uses the custom measurement filter coefficients.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Auto**.

| Auto (0) | The signal analyzer computes the measurement filter coefficients based on the pulse-shaping filter information that you specify in the DDemod Pulse Shaping Filter Type property. If the DDemod Pulse Shaping Filter Type property is set to Custom, the signal analyzer enables equalization. |
| --- | --- |
| Custom (1) | The signal analyzer uses the coefficients specified by RFmxDemod DDemod Configure Measurement Filter Custom Coefficients VI. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Measurement Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20100b.html language=enus -->
## TOPIC 00066: rfmxdemodprop/attr20100b.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20100b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20100b.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Modulation Type Property

Digital Demod:Modulation Type Property

**Short Name:**DDemod Modulation Type

Property of [RFmxDemod](crfmxdemod.html)

Specifies the digital modulation type of the signal that needs to be analyzed.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **PSK**.

| ASK (0) | The modulation type is amplitude-shift keying (ASK). |
| --- | --- |
| FSK (1) | The modulation type is frequency-shift keying (FSK). |
| PSK (2) | The modulation type is phase-shift keying (PSK). |
| QAM (3) | The modulation type is quadrature-amplitude modulation (QAM). |
| MSK (4) | The modulation type is minimum shift keying (MSK). |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Modulation Type |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20100d.html language=enus -->
## TOPIC 00067: rfmxdemodprop/attr20100d.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20100d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20100d.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Number of Symbols Property

Digital Demod:Number of Symbols Property

**Short Name:**DDemod Num Symbols

Property of [RFmxDemod](crfmxdemod.html)

Specifies the number of symbols to be analyzed. The measurement acquires additional symbols to account for filter delays.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 1,000.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Number of Symbols |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20100e.html language=enus -->
## TOPIC 00068: rfmxdemodprop/attr20100e.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20100e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20100e.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:PSK:Format Property

Digital Demod:PSK:Format Property

**Short Name:**DDemod PSK Format

Property of [RFmxDemod](crfmxdemod.html)

Specifies the PSK format.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Normal**.

| Normal (0) | Sets the modulation type to PSK. |
| --- | --- |
| Offset QPSK (1) | Sets the modulation type to offset quadrature PSK (OQPSK). The ideal symbol timing of Q is offset by half of a symbol period from the ideal symbol timing of I. |
| PI/4 - QPSK (2) | Sets the modulation type to pi/4 QPSK. In this modulation, each QPSK symbol is rotated by pi/4. |
| PI/8 - 8PSK (3) | Sets the modulation type to pi/8-8 PSK. In this modulation, each 8 PSK symbol is rotated by pi/8. |
| 3*PI/8 - 8PSK (4) | Sets the modulation type to 3*pi/8-8 PSK. In this modulation, each 8 PSK symbol is rotated by 3*pi/8. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure PSK Format |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20100f.html language=enus -->
## TOPIC 00069: rfmxdemodprop/attr20100f.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20100f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20100f.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Pulse Shaping Filter:Type Property

Digital Demod:Pulse Shaping Filter:Type Property

**Short Name:**DDemod Pulse Shaping Filter Type

Property of [RFmxDemod](crfmxdemod.html)

Specifies the pulse-shaping filter used to transmit the signal. This property determines the measurement filter to be used for analysis when you set the [DDemod Meas Filter Type](attr20100a.html) property to **Auto**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Root Raised Cosine**.

| Rectangular (0) | The transmitted waveform is filtered using a rectangular filter. |
| --- | --- |
| Raised Cosine (1) | The transmitted waveform is filtered using a raised cosine filter. Specify the filter Alpha in the DDemod Pulse Shaping Filter Parameter property. |
| Root Raised Cosine (2) | The transmitted waveform is filtered using a root raised cosine filter. Specify the filter Alpha in the DDemod Pulse Shaping Filter Parameter property. |
| Gaussian (3) | The transmitted waveform is filtered using a Gaussian filter. Specify the filter bandwidth * sample duration in the DDemod Pulse Shaping Filter Parameter property. This filter is applicable only to FSK and MSK modulation types. |
| Custom (4) | The transmitted waveform is filtered using the coefficients that you specify in the RFmxDemod DDemod Configure Pulse Shaping Filter Custom Coefficients VI. |
| Half Sine (5) | The transmitted waveform is filtered using a half sine filter. |
| Linearized GMSK - EDGE (6) | The transmitted waveform is filtered using an EDGE-specific linearized GMSK filter. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Pulse Shaping Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201010.html language=enus -->
## TOPIC 00070: rfmxdemodprop/attr201010.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201010.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201010.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Pulse Shaping Filter:Parameter Property

Digital Demod:Pulse Shaping Filter:Parameter Property

**Short Name:**DDemod Pulse Shaping Filter Parameter

Property of [RFmxDemod](crfmxdemod.html)

Specifies the rolloff factor for raised cosine and root-raised cosine filter that is used as pulse-shaping filter and measurement filter respectively.

For Gaussian filter, this property specifies bandwidth * sample duration.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0.5.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Pulse Shaping Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201011.html language=enus -->
## TOPIC 00071: rfmxdemodprop/attr201011.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201011.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201011.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Samples Per Symbol Property

Digital Demod:Samples Per Symbol Property

**Short Name:**DDemod Samples Per Symbol

Property of [RFmxDemod](crfmxdemod.html)

Specifies the samples per symbol used to acquire the signal for the measurement.

*Sample rate* = *Symbol rate* * *Samples per symbol*.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Auto**.

| Auto (-1) | The measurement uses appropriate samples per symbol(SPS) based on modulation type and pulse shaping filter. SPS=8, for FSK. SPS=4, for ASK,PSK, QAM, MSK when pulse shape filter is not rectangular. SPS=8, for ASK, PSK, QAM, MSK when pulse shape filter is rectangular. |
| --- | --- |
| 4 (4) | The samples per symbol value is 4. |
| 8 (8) | The samples per symbol value is 8. |
| 16 (16) | The samples per symbol value is 16. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Samples Per Symbol |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201012.html language=enus -->
## TOPIC 00072: rfmxdemodprop/attr201012.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201012.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201012.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Spectrum Inverted Property

Digital Demod:Spectrum Inverted Property

**Short Name:**DDemod Spectrum Inverted

Property of [RFmxDemod](crfmxdemod.html)

Specifies whether to swap the acquired I and Q samples for demodulation.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The acquired I and Q samples are used for demodulation as is. |
| --- | --- |
| True (1) | The acquired I and Q samples are swapped before using the signal for demodulation. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Spectrum Inverted |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201013.html language=enus -->
## TOPIC 00073: rfmxdemodprop/attr201013.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201013.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201013.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Symbol Rate (Hz) Property

Digital Demod:Symbol Rate (Hz) Property

**Short Name:**DDemod Symbol Rate (Hz)

Property of [RFmxDemod](crfmxdemod.html)

Specifies the number of symbols transmitted in one second. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 100 kHz.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Symbol Rate |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201014.html language=enus -->
## TOPIC 00074: rfmxdemodprop/attr201014.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201014.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201014.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Synchronization:Enabled Property

Digital Demod:Synchronization:Enabled Property

**Short Name:**DDemod Sync Enabled

Property of [RFmxDemod](crfmxdemod.html)

Specifies whether the demodulator needs to search and synchronize the signal to a known reference sequence. The reference sequence is the symbol representation of a defined set of bits known to be present in the transmitted signal. If the synchronization is found in the demodulated signal, the measurement is performed from this point onward. If the synchronization is not found, the entire signal is used for the measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | Does not search and synchronize the signal. |
| --- | --- |
| True (1) | Searches and synchronizes the signal. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Synchronization |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201015.html language=enus -->
## TOPIC 00075: rfmxdemodprop/attr201015.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201015.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201015.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:All Traces Enabled Property

Digital Demod:All Traces Enabled Property

**Short Name:**DDemod All Traces Enabled

Property of [RFmxDemod](crfmxdemod.html)

Specifies whether to enable the traces to be stored and retrieved after performing the digital demodulation.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod Select Measurement |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20101f.html language=enus -->
## TOPIC 00076: rfmxdemodprop/attr20101f.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20101f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20101f.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Synchronization:Bits Property

Digital Demod:Synchronization:Bits Property

**Short Name:**DDemod Sync Bits

Property of [RFmxDemod](crfmxdemod.html)

Specifies the synchronization bits used to create the reference sequence that must be located in the demodulated signal. The synchronization bits are modulated based on the modulation type to create the reference sequence.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Synchronization |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201021.html language=enus -->
## TOPIC 00077: rfmxdemodprop/attr201021.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201021.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201021.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Results:Carrier:Mean Frequency Offset (Hz) Property

Digital Demod:Results:Carrier:Mean Frequency Offset (Hz) Property

**Short Name:**DDemod Results Carrier Mean Freq Offset (Hz)

Property of [RFmxDemod](crfmxdemod.html)

Returns the measured frequency offset from the transmitted carrier frequency. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201022.html language=enus -->
## TOPIC 00078: rfmxdemodprop/attr201022.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201022.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201022.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Results:Carrier:Mean Frequency Drift (Hz) Property

Digital Demod:Results:Carrier:Mean Frequency Drift (Hz) Property

**Short Name:**DDemod Results Carrier Mean Freq Drift (Hz)

Property of [RFmxDemod](crfmxdemod.html)

Returns the measured carrier frequency drift. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201023.html language=enus -->
## TOPIC 00079: rfmxdemodprop/attr201023.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201023.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201023.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Results:Carrier:Mean Phase Error (deg) Property

Digital Demod:Results:Carrier:Mean Phase Error (deg) Property

**Short Name:**DDemod Results Carrier Mean Phase Error (deg)

Property of [RFmxDemod](crfmxdemod.html)

Returns the measured phase offset from the transmitted carrier phase. This value is expressed in degrees.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201024.html language=enus -->
## TOPIC 00080: rfmxdemodprop/attr201024.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201024.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201024.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Results:EVM:Mean RMS (%) Property

Digital Demod:Results:EVM:Mean RMS (%) Property

**Short Name:**DDemod Results Mean RMS EVM (%)

Property of [RFmxDemod](crfmxdemod.html)

Returns the mean of the RMS EVM measured per acquisition, as a percentage.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201025.html language=enus -->
## TOPIC 00081: rfmxdemodprop/attr201025.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201025.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201025.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Results:EVM:Maximum RMS (%) Property

Digital Demod:Results:EVM:Maximum RMS (%) Property

**Short Name:**DDemod Results Max RMS EVM (%)

Property of [RFmxDemod](crfmxdemod.html)

Returns the maximum of the RMS EVM measured per acquisition, as a percentage.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201026.html language=enus -->
## TOPIC 00082: rfmxdemodprop/attr201026.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201026.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201026.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Results:EVM:Mean Peak (%) Property

Digital Demod:Results:EVM:Mean Peak (%) Property

**Short Name:**DDemod Results Mean Peak EVM (%)

Property of [RFmxDemod](crfmxdemod.html)

Returns the mean of the peak EVM measured per acquisition, as a percentage.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201027.html language=enus -->
## TOPIC 00083: rfmxdemodprop/attr201027.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201027.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201027.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Results:EVM:Maximum Peak (%) Property

Digital Demod:Results:EVM:Maximum Peak (%) Property

**Short Name:**DDemod Results Max Peak EVM (%)

Property of [RFmxDemod](crfmxdemod.html)

Returns the maximum of the peak EVM measured per acquisition, as a percentage.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201028.html language=enus -->
## TOPIC 00084: rfmxdemodprop/attr201028.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201028.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201028.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Results:EVM:Mean Modulation Error Ratio (dB) Property

Digital Demod:Results:EVM:Mean Modulation Error Ratio (dB) Property

**Short Name:**DDemod Results Mean MER (dB)

Property of [RFmxDemod](crfmxdemod.html)

Returns the modulation error ratio. This value is expressed in dB.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201029.html language=enus -->
## TOPIC 00085: rfmxdemodprop/attr201029.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201029.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201029.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Results:Magnitude Error:Mean (%) Property

Digital Demod:Results:Magnitude Error:Mean (%) Property

**Short Name:**DDemod Results Mean Magnitude Error (%)

Property of [RFmxDemod](crfmxdemod.html)

Returns the mean of the magnitude error measured per acquisition, as a percentage.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20102a.html language=enus -->
## TOPIC 00086: rfmxdemodprop/attr20102a.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20102a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20102a.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Results:Magnitude Error:Maximum (%) Property

Digital Demod:Results:Magnitude Error:Maximum (%) Property

**Short Name:**DDemod Results Max Magnitude Error (%)

Property of [RFmxDemod](crfmxdemod.html)

Returns the maximum of the magnitude error measured per acquisition, as a percentage.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20102b.html language=enus -->
## TOPIC 00087: rfmxdemodprop/attr20102b.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20102b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20102b.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Results:Phase Error:Mean (deg) Property

Digital Demod:Results:Phase Error:Mean (deg) Property

**Short Name:**DDemod Results Mean Phase Error (deg)

Property of [RFmxDemod](crfmxdemod.html)

Returns the mean of the phase error measured per acquisition. This value is expressed in degrees.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20102c.html language=enus -->
## TOPIC 00088: rfmxdemodprop/attr20102c.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20102c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20102c.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Results:Phase Error:Maximum (deg) Property

Digital Demod:Results:Phase Error:Maximum (deg) Property

**Short Name:**DDemod Results Max Phase Error (deg)

Property of [RFmxDemod](crfmxdemod.html)

Returns the maximum of the phase error measured per acquisition. This value is expressed in degrees.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20102d.html language=enus -->
## TOPIC 00089: rfmxdemodprop/attr20102d.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20102d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20102d.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Results:FSK:Mean Deviation (Hz) Property

Digital Demod:Results:FSK:Mean Deviation (Hz) Property

**Short Name:**DDemod Results Mean FSK Deviation (Hz)

Property of [RFmxDemod](crfmxdemod.html)

Returns the reference FSK deviation used to measure the FSK error. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20102e.html language=enus -->
## TOPIC 00090: rfmxdemodprop/attr20102e.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20102e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20102e.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Results:FSK:Mean RMS FSK Error (Hz) Property

Digital Demod:Results:FSK:Mean RMS FSK Error (Hz) Property

**Short Name:**DDemod Results Mean RMS FSK Error (Hz)

Property of [RFmxDemod](crfmxdemod.html)

Returns the mean of the RMS frequency error of the FSK symbols measured per acquisition. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20102f.html language=enus -->
## TOPIC 00091: rfmxdemodprop/attr20102f.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20102f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20102f.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Results:FSK:Max Peak FSK Error (Hz) Property

Digital Demod:Results:FSK:Max Peak FSK Error (Hz) Property

**Short Name:**DDemod Results Max Peak FSK Error (Hz)

Property of [RFmxDemod](crfmxdemod.html)

Returns the maximum of peak frequency error of the FSK symbols measured per acquisition. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201030.html language=enus -->
## TOPIC 00092: rfmxdemodprop/attr201030.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201030.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201030.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Results:IQ Impairments:Mean IQ Gain Imbalance (dB) Property

Digital Demod:Results:IQ Impairments:Mean IQ Gain Imbalance (dB) Property

**Short Name:**DDemod Results Mean IQ Gain Imbalance (dB)

Property of [RFmxDemod](crfmxdemod.html)

Returns the measured ratio of I gain to Q gain. This value is expressed in dB.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201031.html language=enus -->
## TOPIC 00093: rfmxdemodprop/attr201031.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201031.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201031.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Results:IQ Impairments:Mean Quadrature Skew (deg) Property

Digital Demod:Results:IQ Impairments:Mean Quadrature Skew (deg) Property

**Short Name:**DDemod Results Mean Quadrature Skew (deg)

Property of [RFmxDemod](crfmxdemod.html)

Returns a measure of I and Q components in the signal that are not perfectly orthogonal. Quadrature error can be either positive or negative, with the sign indicating the orientation of the error.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201032.html language=enus -->
## TOPIC 00094: rfmxdemodprop/attr201032.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201032.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201032.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Results:IQ Impairments:Mean IQ Origin Offset (dB) Property

Digital Demod:Results:IQ Impairments:Mean IQ Origin Offset (dB) Property

**Short Name:**DDemod Results Mean IQ Origin Offset (dB)

Property of [RFmxDemod](crfmxdemod.html)

Returns the offset from the ideal location of the constellation origin. This value is expressed in dB.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201034.html language=enus -->
## TOPIC 00095: rfmxdemodprop/attr201034.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201034.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201034.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Synchronization:Measurement Offset Property

Digital Demod:Synchronization:Measurement Offset Property

**Short Name:**DDemod Meas Offset

Property of [RFmxDemod](crfmxdemod.html)

Specifies the offset, which is the location from which the signal is considered for further measurements. The offset is specified in symbols of the reference sequence. This offset is not applicable when the synchronization bits are not found.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Synchronization |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201035.html language=enus -->
## TOPIC 00096: rfmxdemodprop/attr201035.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201035.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201035.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Results:Sync Found? Property

Digital Demod:Results:Sync Found? Property

**Short Name:**DDemod Sync Found?

Property of [RFmxDemod](crfmxdemod.html)

Indicates whether the synchronization bits were found in the demodulated signal.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201036.html language=enus -->
## TOPIC 00097: rfmxdemodprop/attr201036.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201036.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201036.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Equalizer:Filter Length (Symbols) Property

Digital Demod:Equalizer:Filter Length (Symbols) Property

**Short Name:**DDemod Equalizer Filter Length (Symbols)

Property of [RFmxDemod](crfmxdemod.html)

Specifies the length of the equalization filter to be computed. The length is specified in terms of symbols.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 20.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Equalizer |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201037.html language=enus -->
## TOPIC 00098: rfmxdemodprop/attr201037.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201037.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201037.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Equalizer:Training Count Property

Digital Demod:Equalizer:Training Count Property

**Short Name:**DDemod Equalizer Training Count

Property of [RFmxDemod](crfmxdemod.html)

Specifies the number of iterations during which the equalizer adapts its coefficients in the training stage. After the training stage, the measurement is performed over the specified number of averages.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Equalizer |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201038.html language=enus -->
## TOPIC 00099: rfmxdemodprop/attr201038.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201038.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201038.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:FSK:Reference Compensation Enabled Property

Digital Demod:FSK:Reference Compensation Enabled Property

**Short Name:**DDemod FSK Ref Comp Enabled

Property of [RFmxDemod](crfmxdemod.html)

Specifies whether the FSK deviation that you specify is used to compensate for gain errors and compute FSK error.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | Does not compensate for gain errors. |
| --- | --- |
| True (1) | Compensates for gain errors. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure FSK Deviation |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201039.html language=enus -->
## TOPIC 00100: rfmxdemodprop/attr201039.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201039.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201039.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:EVM Normalization Reference Property

Digital Demod:EVM Normalization Reference Property

**Short Name:**DDemod EVM Norm Ref

Property of [RFmxDemod](crfmxdemod.html)

Specifies the reference used to normalize the error vector magnitude (EVM).

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Peak**.

| Peak (0) | The EVM is normalized to the peak magnitude of the reference symbols. |
| --- | --- |
| RMS (1) | The EVM is normalized to the RMS magnitude of the reference symbols. This value is applicable only to modulation types, such as quadrature-amplitude modulation (QAM). This value is expressed in which the symbols in the map do not have a constant amplitude. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure EVM Normalization Reference |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20103a.html language=enus -->
## TOPIC 00101: rfmxdemodprop/attr20103a.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20103a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20103a.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Results:Offset EVM:Mean RMS (%) Property

Digital Demod:Results:Offset EVM:Mean RMS (%) Property

**Short Name:**DDemod Results Mean RMS Offset EVM (%)

Property of [RFmxDemod](crfmxdemod.html)

Returns the mean of the RMS EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20103b.html language=enus -->
## TOPIC 00102: rfmxdemodprop/attr20103b.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20103b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20103b.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Results:Offset EVM:Mean Peak (%) Property

Digital Demod:Results:Offset EVM:Mean Peak (%) Property

**Short Name:**DDemod Results Mean Peak Offset EVM (%)

Property of [RFmxDemod](crfmxdemod.html)

Returns the mean of the peak EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20103c.html language=enus -->
## TOPIC 00103: rfmxdemodprop/attr20103c.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20103c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20103c.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Results:Offset EVM:Maximum RMS (%) Property

Digital Demod:Results:Offset EVM:Maximum RMS (%) Property

**Short Name:**DDemod Results Max RMS Offset EVM (%)

Property of [RFmxDemod](crfmxdemod.html)

Returns the maximum of the RMS EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20103d.html language=enus -->
## TOPIC 00104: rfmxdemodprop/attr20103d.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20103d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20103d.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Results:Offset EVM:Maximum Peak (%) Property

Digital Demod:Results:Offset EVM:Maximum Peak (%) Property

**Short Name:**DDemod Results Max Peak Offset EVM (%)

Property of [RFmxDemod](crfmxdemod.html)

Returns the maximum of the peak EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20103e.html language=enus -->
## TOPIC 00105: rfmxdemodprop/attr20103e.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20103e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20103e.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Results:Mean Rho Factor Property

Digital Demod:Results:Mean Rho Factor Property

**Short Name:**DDemod Results Mean Rho Factor

Property of [RFmxDemod](crfmxdemod.html)

Returns the correlation of the measurement waveform and the reference waveform.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20103f.html language=enus -->
## TOPIC 00106: rfmxdemodprop/attr20103f.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20103f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20103f.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Results:Mean Amplitude Droop (dB/Symbol) Property

Digital Demod:Results:Mean Amplitude Droop (dB/Symbol) Property

**Short Name:**DDemod Results Mean Amplitude Droop

Property of [RFmxDemod](crfmxdemod.html)

Returns the mean amplitude droop per symbol.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxDemod DDemod Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201040.html language=enus -->
## TOPIC 00107: rfmxdemodprop/attr201040.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201040.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201040.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Symbol Map Type Property

Digital Demod:Symbol Map Type Property

**Short Name:**DDemod Symbol Map Type

Property of [RFmxDemod](crfmxdemod.html)

Specifies whether the measurement uses the default symbol map or the map that you configure using the RFmxDemod DDemod Configure Symbol Map VI.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Auto**.

| Auto (0) | Uses a default symbol map. |
| --- | --- |
| Custom (1) | Uses the map that you specify using the RFmxDemod DDemod Configure Symbol Map VI . |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod DDemod Configure Symbol Map |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201041.html language=enus -->
## TOPIC 00108: rfmxdemodprop/attr201041.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201041.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201041.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Signal Structure Property

Digital Demod:Signal Structure Property

**Short Name:**DDemod Signal Structure

Property of [RFmxDemod](crfmxdemod.html)

Specifies whether the signal is either a bursty signal or a continuous signal.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Continuous**.

| Bursted (0) | The signal is a bursty signal. |
| --- | --- |
| Continuous (1) | The signal is a continuous signal. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201042.html language=enus -->
## TOPIC 00109: rfmxdemodprop/attr201042.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201042.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201042.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Burst Start Exclusion Symbols Property

Digital Demod:Burst Start Exclusion Symbols Property

**Short Name:**DDemod Burst Start Exclusion Symbols

Property of [RFmxDemod](crfmxdemod.html)

Specifies the number of symbols from the start of the burst trigger that is excluded from the measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201043.html language=enus -->
## TOPIC 00110: rfmxdemodprop/attr201043.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201043.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201043.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Burst End Exclusion Symbols Property

Digital Demod:Burst End Exclusion Symbols Property

**Short Name:**DDemod Burst End Exclusion Symbols

Property of [RFmxDemod](crfmxdemod.html)

Specifies the number of symbols that is excluded from the measurement before the falling edge of the burst.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201044.html language=enus -->
## TOPIC 00111: rfmxdemodprop/attr201044.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201044.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201044.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Compensation:IQ Offset Removal Enabled Property

Digital Demod:Compensation:IQ Offset Removal Enabled Property

**Short Name:**DDemod IQ Offset Removal Enabled

Property of [RFmxDemod](crfmxdemod.html)

Specifies whether to remove the I/Q offset before the EVM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | The IQ offset is not removed before the EVM measurement. |
| --- | --- |
| True (1) | The IQ offset is removed before the EVM measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201045.html language=enus -->
## TOPIC 00112: rfmxdemodprop/attr201045.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201045.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201045.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Compensation:CFO Estimation Mode Property

Digital Demod:Compensation:CFO Estimation Mode Property

**Short Name:**DDemod CFO Estimation Mode

Property of [RFmxDemod](crfmxdemod.html)

Specifies the carrier frequency offset estimation capability of the demodulator. If you select **Narrow**, coarse carrier frequency offset estimation is disabled and only fine carrier frequency offset estimation is performed. This is useful when analysing low SNR signals.

| Narrow (0) | The measurement disables coarse carrier frequency offset estimation. |
| --- | --- |
| Wide (1) | The measurement enables coarse and fine carrier frequency offset estimation. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201047.html language=enus -->
## TOPIC 00113: rfmxdemodprop/attr201047.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201047.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201047.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Search:Search Length Auto Property

Digital Demod:Search:Search Length Auto Property

**Short Name:**DDemod Search Length Auto

Property of [RFmxDemod](crfmxdemod.html)

Specifies whether the measurement should search for synchronization bit pattern in the waveform of length determined by the measurement or search for length duration.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | Synchronization bit pattern is searched in a waveform within the search Length duration. |
| --- | --- |
| True (1) | Synchronization bit pattern is searched in a waveform of length determined by the measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr201048.html language=enus -->
## TOPIC 00114: rfmxdemodprop/attr201048.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr201048.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr201048.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Digital Demod:Search:Search Length (s) Property

Digital Demod:Search:Search Length (s) Property

**Short Name:**DDemod Search Length (s)

Property of [RFmxDemod](crfmxdemod.html)

Specifies the length of the waveform within which the synchronization bit pattern needs to be searched when you set the [DDemod Search Length Auto](attr201047.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0.001 seconds.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr202001.html language=enus -->
## TOPIC 00115: rfmxdemodprop/attr202001.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr202001.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr202001.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Center Frequency (Hz) Property

Center Frequency (Hz) Property

**Short Name:**Center Freq (Hz)

Property of [RFmxDemod](crfmxdemod.html)

Specifies the carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod Configure Frequency |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr202002.html language=enus -->
## TOPIC 00116: rfmxdemodprop/attr202002.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr202002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr202002.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

External Attenuation (dB) Property

External Attenuation (dB) Property

**Short Name:**External Attenuation (dB)

Property of [RFmxDemod](crfmxdemod.html)

Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. For more information about attenuation, refer to the *Attenuation and Signal Levels* topic for your device in the *NI RF Vector Signal Analyzers Help*. This value is expressed in dB.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod Configure External Attenuation |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr202003.html language=enus -->
## TOPIC 00117: rfmxdemodprop/attr202003.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr202003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr202003.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Reference Level Property

Reference Level Property

**Short Name:**Reference Level

Property of [RFmxDemod](crfmxdemod.html)

Specifies the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and V<sub>pk-pk</sub> for baseband devices.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod Configure Reference Level |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr202004.html language=enus -->
## TOPIC 00118: rfmxdemodprop/attr202004.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr202004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr202004.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Type Property

Trigger:Type Property

**Short Name:**Trigger Type

Property of [RFmxDemod](crfmxdemod.html)

Specifies the type of Reference Trigger to use for signal acquisition.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **None**.

| None (0) | No reference trigger is used for signal acquisition. |
| --- | --- |
| Digital Edge (1) | A digital-edge trigger is used for signal acquisition. The source of the digital edge is specified using the Digital Edge Source property. |
| IQ Power Edge (2) | An I/Q power-edge trigger is used for signal acquisition, which is configured using the IQ Power Edge Slope property. |
| Software (3) | A software trigger is used for signal acquisition. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr202005.html language=enus -->
## TOPIC 00119: rfmxdemodprop/attr202005.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr202005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr202005.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Digital Edge:Source Property

Trigger:Digital Edge:Source Property

**Short Name:**Digital Edge Source

Property of [RFmxDemod](crfmxdemod.html)

Specifies the source terminal for the digital-edge trigger. This property is applicable only when you set the [Trigger Type](attr202004.html) property to **Digital Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

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
| TimerEvent (TimerEvent) | The trigger is received from the Timer Event. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr202006.html language=enus -->
## TOPIC 00120: rfmxdemodprop/attr202006.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr202006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr202006.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Digital Edge:Edge Property

Trigger:Digital Edge:Edge Property

**Short Name:**Digital Edge

Property of [RFmxDemod](crfmxdemod.html)

Specifies whether the signal analyzer detects a rising or falling edge on the digital-edge trigger signal. This property is applicable only when you set the [Trigger Type](attr202004.html) property to **Digital Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Rising Edge**.

| Rising Edge (0) | The trigger asserts on the rising edge of the signal. |
| --- | --- |
| Falling Edge (1) | The trigger asserts on the falling edge of the signal. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr202007.html language=enus -->
## TOPIC 00121: rfmxdemodprop/attr202007.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr202007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr202007.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Trigger:IQ Power Edge:Source Property

Trigger:IQ Power Edge:Source Property

**Short Name:**IQ Power Edge Source

Property of [RFmxDemod](crfmxdemod.html)

Specifies the channel from which the device monitors the trigger. This property is applicable only when you set the [Trigger Type](attr202004.html) property to **IQ Power Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr202008.html language=enus -->
## TOPIC 00122: rfmxdemodprop/attr202008.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr202008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr202008.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Trigger:IQ Power Edge:Level (dB or dBm) Property

Trigger:IQ Power Edge:Level (dB or dBm) Property

**Short Name:**IQ Power Edge Level

Property of [RFmxDemod](crfmxdemod.html)

Specifies the power level at which the device triggers. This value is expressed in dB when you set the [IQ Power Edge Level Type](attr202fff.html) property to **Relative** and in dBm when you set the IQ Power Edge Level Type property to **Absolute**. The device asserts the trigger when the signal exceeds the level specified by the value of this property, taking into consideration the specified slope. This property is used only when you set the [Trigger Type](attr202004.html) property to **IQ Power Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr202009.html language=enus -->
## TOPIC 00123: rfmxdemodprop/attr202009.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr202009.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr202009.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Trigger:IQ Power Edge:Slope Property

Trigger:IQ Power Edge:Slope Property

**Short Name:**IQ Power Edge Slope

Property of [RFmxDemod](crfmxdemod.html)

Specifies whether the device asserts the trigger when the signal power is rising or falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This property is used only when you set the [Trigger Type](attr202004.html) property to **IQ Power Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Rising Slope**.

| Rising Slope (0) | The trigger asserts when the signal power is rising. |
| --- | --- |
| Falling Slope (1) | The trigger asserts when the signal power is falling. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20200a.html language=enus -->
## TOPIC 00124: rfmxdemodprop/attr20200a.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20200a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20200a.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Delay (s) Property

Trigger:Delay (s) Property

**Short Name:**Trigger Delay (s)

Property of [RFmxDemod](crfmxdemod.html)

Specifies the trigger delay time. This value is expressed in seconds.

If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0 seconds.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20200b.html language=enus -->
## TOPIC 00125: rfmxdemodprop/attr20200b.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20200b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20200b.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Minimum Quiet Time:Mode Property

Trigger:Minimum Quiet Time:Mode Property

**Short Name:**Trigger Min Quiet Time Mode

Property of [RFmxDemod](crfmxdemod.html)

Specifies whether the measurement computes the minimum quiet time used for triggering.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Manual**.

| Manual (0) | The minimum quiet time for triggering is the value of the Trigger Min Quiet Time property. |
| --- | --- |
| Auto (1) | The measurement computes the minimum quiet time used for triggering. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20200c.html language=enus -->
## TOPIC 00126: rfmxdemodprop/attr20200c.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20200c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20200c.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Minimum Quiet Time:Duration (s) Property

Trigger:Minimum Quiet Time:Duration (s) Property

**Short Name:**Trigger Min Quiet Time (s)

Property of [RFmxDemod](crfmxdemod.html)

Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. If you set the [IQ Power Edge Slope](attr202004.html) property to **Rising Slope**, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope property to **Falling Slope**, the signal is quiet above the trigger level. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxDemod Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20200d.html language=enus -->
## TOPIC 00127: rfmxdemodprop/attr20200d.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20200d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20200d.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Auto Level Initial Reference Level (dBm) Property

Advanced:Auto Level Initial Reference Level (dBm) Property

**Short Name:**Auto Level Initial Ref Level (dBm)

Property of [RFmxDemod](crfmxdemod.html)

Specifies the initial reference level which the RFmxDemod Auto Level VI uses to estimate the peak power of the input signal. This value is expressed in dBm.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 30.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr20200e.html language=enus -->
## TOPIC 00128: rfmxdemodprop/attr20200e.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr20200e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr20200e.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Limited Configuration Change Property

Advanced:Limited Configuration Change Property

**Short Name:**Limited Configuration Change

Property of [RFmxDemod](crfmxdemod.html)

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
| Freq and Ref Level (4) | Signal configuration, other than center frequency, reference level, and external attenuation, is locked after first Commit of the named signal configuration. Thereafter only Center Frequency, Reference Level, and External Attenuation property value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type property to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| Selected Ports, Freq and Ref Level (5) | Signal configuration, other than Selected Ports, Center frequency, Reference level, External attenuation, and RFInstr configuration, is locked after first Commit or Initiate of the named signal configuration. Thereafter only Selected Ports, Center Frequency, Reference Level, and External Attenuation property value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type property to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr202ffc.html language=enus -->
## TOPIC 00129: rfmxdemodprop/attr202ffc.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr202ffc.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr202ffc.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Reference Level Headroom Property

Reference Level Headroom Property

**Short Name:**Reference Level Headroom

Property of [RFmxDemod](crfmxdemod.html)

Specifies the margin RFmx adds to the [Reference Level](attr202003.html) property. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level.

RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input signal remains within the Reference Level plus the Reference Level Headroom. If you know the input power of the signal precisely or previously included the margin in the Reference Level, you could improve the signal-to-noise ratio by reducing the Reference Level Headroom.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

**Supported devices:**PXIe-5668, PXIe-5830/5831/5832/5840/5841/5842.

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

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr202ffd.html language=enus -->
## TOPIC 00130: rfmxdemodprop/attr202ffd.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr202ffd.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr202ffd.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Selected Ports Property

Selected Ports Property

**Short Name:**Selected Ports

Property of [RFmxDemod](crfmxdemod.html)

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

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr202fff.html language=enus -->
## TOPIC 00131: rfmxdemodprop/attr202fff.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr202fff.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr202fff.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Trigger:IQ Power Edge:Level Type Property

Trigger:IQ Power Edge:Level Type Property

**Short Name:**IQ Power Edge Level Type

Property of [RFmxDemod](crfmxdemod.html)

Specifies the reference for the [IQ Power Edge Level](attr202008.html) property. This property is used only when you set the [Trigger Type](attr202004.html) property to **IQ Power Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Absolute**.

| Relative (0) | The value of the IQ Power Edge Level property is relative to the value of the Reference Level property. |
| --- | --- |
| Absolute (1) | The IQ Power Edge Level property specifies the absolute power. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/attr203000.html language=enus -->
## TOPIC 00132: rfmxdemodprop/attr203000.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/attr203000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/attr203000.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

Result Fetch Timeout (s) Property

Result Fetch Timeout (s) Property

**Short Name:**Result Fetch Timeout (s)

Property of [RFmxDemod](crfmxdemod.html)

Specifies the time to wait before results are available in the RFmxDemod Property Node. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxDemod Property Node waits until the measurement is complete.

 This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-demod-prop path=rfmxdemodprop/crfmxdemod.html language=enus -->
## TOPIC 00133: rfmxdemodprop/crfmxdemod.html

- bundle_id: `rfmx-demod-prop`
- source_path: `rfmxdemodprop/crfmxdemod.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-demod-prop/raw/resource/enus/rfmxdemodprop/crfmxdemod.html
- document_id: `rfmx-demod-prop`
- page_type: `leaf`
- content_type: ``

RFmxDemod Properties

RFmxDemod Properties

Use the RFmxDemod properties to access options for configuring and fetching measurements.

| Property | Description |
| --- | --- |
| Selector String | Specifies the selector string used to access all subsequent selector string-based properties in this instance of the property node. Details |
| Selected Ports | Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr Get Available Ports VI to get the valid port names. Details |
| Center Frequency (Hz) | Specifies the carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency. Details |
| Reference Level | Specifies the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. Details |
| External Attenuation (dB) | Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. This value is expressed in dB. Details |
| Reference Level Headroom | Specifies the margin RFmx adds to the Reference Level property. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. Details |
| Trigger:Type | Specifies the type of Reference Trigger to use for signal acquisition. Details |
| Trigger:Digital Edge:Source | Specifies the source terminal for the digital-edge trigger. This property is applicable only when you set the Trigger Type property to Digital Edge. Details |
| Trigger:Digital Edge:Edge | Specifies whether the signal analyzer detects a rising or falling edge on the digital-edge trigger signal. This property is applicable only when you set the Trigger Type property to Digital Edge. Details |
| Trigger:IQ Power Edge:Source | Specifies the channel from which the device monitors the trigger. This property is applicable only when you set the Trigger Type property to IQ Power Edge. Details |
| Trigger:IQ Power Edge:Level (dB or dBm) | Specifies the power level at which the device triggers. This value is expressed in dB when you set the IQ Power Edge Level Type property to Relative and in dBm when you set the IQ Power Edge Level Type property to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this property, taking into consideration the specified slope. This property is used only when you set the Trigger Type property to IQ Power Edge. Details |
| Trigger:IQ Power Edge:Level Type | Specifies the reference for the IQ Power Edge Level property. This property is used only when you set the Trigger Type property to IQ Power Edge. Details |
| Trigger:IQ Power Edge:Slope | Specifies whether the device asserts the trigger when the signal power is rising or falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This property is used only when you set the Trigger Type property to IQ Power Edge. Details |
| Trigger:Delay (s) | Specifies the trigger delay time. This value is expressed in seconds. Details |
| Trigger:Minimum Quiet Time:Mode | Specifies whether the measurement computes the minimum quiet time used for triggering. Details |
| Trigger:Minimum Quiet Time:Duration (s) | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. If you set the IQ Power Edge Slope property to Rising Slope, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope property to Falling Slope, the signal is quiet above the trigger level. This value is expressed in seconds. Details |
| Analog Demod:Measurement Enabled | Specifies whether to enable analog demodulation measurements. Details |
| Analog Demod:Audio Measurement Enabled | Specifies whether to enable the audio signal measurements, such as SINAD, SNR, THD and THD+Noise. Details |
| Analog Demod:Modulation Type | Specifies the analog modulation type of the signal that needs to be analyzed. Details |
| Analog Demod:AM Carrier Suppressed | Specifies whether the carrier of the AM (amplitude modulated) signal is absent. Details |
| Analog Demod:RBW Filter:Type | Specifies the shape of the digital RBW filter. Details |
| Analog Demod:RBW Filter:Bandwidth (Hz) | Specifies the bandwidth of the resolution bandwidth (RBW) filter to be applied to the acquired signal. This value is expressed in Hz. Details |
| Analog Demod:RBW Filter:Alpha | Specifies the roll-off factor of the root-raised cosine (RRC) filter. Details |
| Analog Demod:Measurement Interval (s) | Specifies the signal acquisition time for the analog demodulation measurement. This value is expressed in seconds. Details |
| Analog Demod:Carrier Correction:Frequency Enabled | Specifies whether to correct the frequency error in the carrier when demodulating frequency-modulated (FM) or phase-modulated (PM) signals. Details |
| Analog Demod:Carrier Correction:Phase Enabled | Specifies whether to correct the carrier phase error when demodulating phase-modulated signals. Details |
| Analog Demod:FM DeEmphasis (s) | Specifies the time constant of de-emphasis filter, which compensates for the pre-emphasis filter in the FM transmitter. This value is expressed in seconds. Details |
| Analog Demod:Audio Filter:Type | Specifies the audio filter to be applied on the analog demodulated signal. Details |
| Analog Demod:Audio Filter:Lower Cutoff Frequency (Hz) | Specifies the lower cutoff frequency of the custom audio filter. This property is applicable only when you set the ADemod Audio Filter Type property to Custom. This value is expressed in Hz. Details |
| Analog Demod:Audio Filter:Upper Cutoff Frequency (Hz) | Specifies the upper cutoff frequency of the custom audio filter. This property is applicable only when you set the ADemod Audio Filter Type property to Custom. This value is expressed in Hz. Details |
| Analog Demod:Averaging:Enabled | Specifies whether to enable averaging for the analog demodulation measurement. Details |
| Analog Demod:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the ADemod Averaging Enabled property to True. Details |
| Analog Demod:Averaging:Type | Specifies the averaging type for the measurement. Details |
| Analog Demod:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the analog demodulation measurement. Details |
| Analog Demod:Results:Mean Carrier Frequency Error (Hz) | Returns the mean of the measured carrier frequency offset. This value is expressed in Hz. Details |
| Analog Demod:Results:Mean Carrier Power (dBm) | Returns the mean of the measured carrier power. This value is expressed in dBm. Details |
| Analog Demod:Results:Mean Modulation Frequency (Hz) | Returns the mean of the demodulated signal frequency. This value is expressed in Hz. Details |
| Analog Demod:Results:Average SINAD (dB) | Returns the averaged signal-to-noise and distortion ratio of the demodulated signal. This value is expressed in dB. Details |
| Analog Demod:Results:Average THD with Noise (%) | Returns the averaged total harmonic distortion with noise of the demodulated signal, as a percentage. Details |
| Analog Demod:Results:Average THD (%) | Returns the averaged total harmonic distortion of the demodulated signal, as a percentage. Details |
| Analog Demod:Results:Average SNR (dB) | Returns the averaged signal-to-noise ratio of the demodulated signal. This value is expressed in dB. Details |
| Analog Demod:Results:AM Modulation Depth:Mean Standard Deviation (%) | Returns the mean amplitude variation around the unmodulated carrier amplitude, as a percentage. If the carrier is suppressed, the amplitude variation of the modulating signal is returned. Details |
| Analog Demod:Results:AM Modulation Depth:Mean Peak to Peak /2 (%) | Returns the mean (peak-to-peak)/2 amplitude of the modulating signal, as a percentage. Details |
| Analog Demod:Results:AM Modulation Depth:Mean Positive Peak (%) | Returns the mean positive peak amplitude of the modulating signal, as a percentage. Details |
| Analog Demod:Results:AM Modulation Depth:Mean Negative Peak (%) | Returns the mean negative peak amplitude of the modulating signal, as a percentage. Details |
| Analog Demod:Results:AM Modulation Depth:Mean RMS (%) | Returns the mean RMS amplitude of the modulating signal, as a percentage. Details |
| Analog Demod:Results:AM Modulation Depth:Maximum Standard Deviation (%) | Returns the maximum modulation depth measured across multiple acquisitions, as a percentage. Details |
| Analog Demod:Results:AM Modulation Depth:Maximum Peak to Peak /2 (%) | Returns the maximum (peak-to-peak)/2 amplitude of the modulating signal measured across multiple acquisitions, as a percentage. Details |
| Analog Demod:Results:AM Modulation Depth:Maximum Positive Peak (%) | Returns the maximum positive peak amplitude of the modulating signal measured across multiple acquisitions, as a percentage. Details |
| Analog Demod:Results:AM Modulation Depth:Maximum Negative Peak (%) | Returns the maximum negative peak amplitude of the modulating signal measured across multiple acquisitions, as a percentage. Details |
| Analog Demod:Results:AM Modulation Depth:Maximum RMS (%) | Returns the maximum RMS amplitude of the modulating signal measured across multiple acquisitions, as a percentage. Details |
| Analog Demod:Results:FM Deviation:Mean Standard Deviation (Hz) | Returns the mean frequency deviation around the nominal frequency of the FM carrier. This value is expressed in Hz. Details |
| Analog Demod:Results:FM Deviation:Mean Peak to Peak /2 (Hz) | Returns the mean (peak-to-peak)/2 frequency variation around the nominal frequency of the FM carrier. This value is expressed in Hz. Details |
| Analog Demod:Results:FM Deviation:Mean Positive Peak (Hz) | Returns the mean positive peak frequency deviation of the frequency-modulated signal. This value is expressed in Hz. Details |
| Analog Demod:Results:FM Deviation:Mean Negative Peak (Hz) | Returns the mean negative peak frequency deviation of the frequency-modulated signal. This value is expressed in Hz. Details |
| Analog Demod:Results:FM Deviation:Mean RMS (Hz) | Returns the mean RMS frequency deviation of the frequency-modulated signal. This value is expressed in Hz. Details |
| Analog Demod:Results:FM Deviation:Maximum Standard Deviation (Hz) | Returns the maximum frequency deviation of the frequency-modulated signal measured across multiple acquisitions. This value is expressed in Hz. Details |
| Analog Demod:Results:FM Deviation:Maximum Peak to Peak /2 (Hz) | Returns the maximum (peak-to-peak)/2 frequency variation around the nominal frequency of the FM carrier measured across multiple acquisitions. This value is expressed in Hz. Details |
| Analog Demod:Results:FM Deviation:Maximum Positive Peak (Hz) | Returns the maximum positive peak frequency deviation of the frequency-modulated signal measured across multiple acquisitions. This value is expressed in Hz. Details |
| Analog Demod:Results:FM Deviation:Maximum Negative Peak (Hz) | Returns the maximum negative peak frequency deviation of the frequency-modulated signal measured across multiple acquisitions. This value is expressed in Hz. Details |
| Analog Demod:Results:FM Deviation:Maximum RMS (Hz) | Returns the maximum RMS frequency deviation of the frequency-modulated signal measured across multiple acquisitions. This value is expressed in Hz. Details |
| Analog Demod:Results:PM Deviation:Mean Standard Deviation (deg) | Returns the mean phase deviation around the unmodulated carrier phase. This value is expressed in degrees. Details |
| Analog Demod:Results:PM Deviation:Mean Peak to Peak /2 (deg) | Returns the mean (peak-to-peak)/2 phase deviation around the unmodulated carrier phase. This value is expressed in degrees. Details |
| Analog Demod:Results:PM Deviation:Mean Positive Peak (deg) | Returns the mean positive peak phase deviation around the unmodulated carrier phase. This value is expressed in degrees. Details |
| Analog Demod:Results:PM Deviation:Mean Negative Peak (deg) | Returns the mean negative peak phase deviation around the unmodulated carrier phase. This value is expressed in degrees. Details |
| Analog Demod:Results:PM Deviation:Mean RMS (deg) | Returns the mean RMS phase deviation of the phase-modulated signal. This value is expressed in degrees. Details |
| Analog Demod:Results:PM Deviation:Maximum Standard Deviation (deg) | Returns the maximum phase deviation around the unmodulated carrier phase, measured across multiple acquisitions. This value is expressed in degrees. Details |
| Analog Demod:Results:PM Deviation:Maximum Peak to Peak /2 (deg) | Returns the maximum (peak-to-peak)/2 phase deviation around the unmodulated carrier phase, measured across multiple acquisitions. This value is expressed in degrees. Details |
| Analog Demod:Results:PM Deviation:Maximum Positive Peak (deg) | Returns the maximum positive peak phase deviation around the unmodulated carrier phase, measured across multiple acquisitions. This value is expressed in degrees. Details |
| Analog Demod:Results:PM Deviation:Maximum Negative Peak (deg) | Returns the maximum negative peak phase deviation around the unmodulated carrier phase, measured across multiple acquisitions. This value is expressed in degrees. Details |
| Analog Demod:Results:PM Deviation:Maximum RMS (deg) | Returns the maximum RMS phase deviation of the phase-modulated signal measured across multiple acquisitions. This value is expressed in degrees. Details |
| Digital Demod:Measurement Enabled | Enables digital demodulation measurements. Details |
| Digital Demod:Modulation Type | Specifies the digital modulation type of the signal that needs to be analyzed. Details |
| Digital Demod:M | Specifies the M-ary number, which is the number of distinct states that represent symbols in the complex baseband modulated waveform. Details |
| Digital Demod:Spectrum Inverted | Specifies whether to swap the acquired I and Q samples for demodulation. Details |
| Digital Demod:PSK:Format | Specifies the PSK format. Details |
| Digital Demod:Differential Enabled | Specifies whether the symbols are differentially encoded. This property is applicable only to PSK and MSK modulation types. Details |
| Digital Demod:Symbol Rate (Hz) | Specifies the number of symbols transmitted in one second. This value is expressed in Hz. Details |
| Digital Demod:Number of Symbols | Specifies the number of symbols to be analyzed. The measurement acquires additional symbols to account for filter delays. Details |
| Digital Demod:Samples Per Symbol | Specifies the samples per symbol used to acquire the signal for the measurement. Sample rate = Symbol rate * Samples per symbol. Details |
| Digital Demod:EVM Normalization Reference | Specifies the reference used to normalize the error vector magnitude (EVM). Details |
| Digital Demod:FSK:Deviation (Hz) | Specifies the expected FSK frequency deviation At baseband frequencies, deviations for individual symbols are evenly spaced in the interval [-fd, fd], where fd represents the frequency deviation. This value is expressed in Hz. Details |
| Digital Demod:FSK:Reference Compensation Enabled | Specifies whether the FSK deviation that you specify is used to compensate for gain errors and compute FSK error. Details |
| Digital Demod:Symbol Map Type | Specifies whether the measurement uses the default symbol map or the map that you configure using the RFmxDemod DDemod Configure Symbol Map VI. Details |
| Digital Demod:Pulse Shaping Filter:Type | Specifies the pulse-shaping filter used to transmit the signal. This property determines the measurement filter to be used for analysis when you set the DDemod Meas Filter Type property to Auto. Details |
| Digital Demod:Pulse Shaping Filter:Parameter | Specifies the rolloff factor for raised cosine and root-raised cosine filter that is used as pulse-shaping filter and measurement filter respectively. For Gaussian filter, this property specifies bandwidth * sample duration. Details |
| Digital Demod:Measurement Filter:Type | Specifies whether the measurement needs to compute the measurement filter based on the pulse-shaping filter type or uses the custom measurement filter coefficients. Details |
| Digital Demod:Equalizer:Mode | Specifies whether the measurement needs to perform equalization. Details |
| Digital Demod:Equalizer:Filter Length (Symbols) | Specifies the length of the equalization filter to be computed. The length is specified in terms of symbols. Details |
| Digital Demod:Equalizer:Training Count | Specifies the number of iterations during which the equalizer adapts its coefficients in the training stage. After the training stage, the measurement is performed over the specified number of averages. Details |
| Digital Demod:Equalizer:Convergence Factor | Specifies the incremental step used by the equalizer to adapt to the channel during the training stage. Details |
| Digital Demod:Synchronization:Enabled | Specifies whether the demodulator needs to search and synchronize the signal to a known reference sequence. The reference sequence is the symbol representation of a defined set of bits known to be present in the transmitted signal. If the synchronization is found in the demodulated signal, the measurement is performed from this point onward. If the synchronization is not found, the entire signal is used for the measurement. Details |
| Digital Demod:Synchronization:Bits | Specifies the synchronization bits used to create the reference sequence that must be located in the demodulated signal. The synchronization bits are modulated based on the modulation type to create the reference sequence. Details |
| Digital Demod:Synchronization:Measurement Offset | Specifies the offset, which is the location from which the signal is considered for further measurements. The offset is specified in symbols of the reference sequence. This offset is not applicable when the synchronization bits are not found. Details |
| Digital Demod:Averaging:Enabled | Enables averaging for digital demodulation measurements. Details |
| Digital Demod:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the DDemod Averaging Enabled property to True. Details |
| Digital Demod:Signal Structure | Specifies whether the signal is either a bursty signal or a continuous signal. Details |
| Digital Demod:Burst Start Exclusion Symbols | Specifies the number of symbols from the start of the burst trigger that is excluded from the measurement. Details |
| Digital Demod:Burst End Exclusion Symbols | Specifies the number of symbols that is excluded from the measurement before the falling edge of the burst. Details |
| Digital Demod:Compensation:IQ Offset Removal Enabled | Specifies whether to remove the I/Q offset before the EVM measurement. Details |
| Digital Demod:Compensation:CFO Estimation Mode | Specifies the carrier frequency offset estimation capability of the demodulator. If you select Narrow, coarse carrier frequency offset estimation is disabled and only fine carrier frequency offset estimation is performed. This is useful when analysing low SNR signals. Details |
| Digital Demod:Search:Search Length Auto | Specifies whether the measurement should search for synchronization bit pattern in the waveform of length determined by the measurement or search for length duration. Details |
| Digital Demod:Search:Search Length (s) | Specifies the length of the waveform within which the synchronization bit pattern needs to be searched when you set the DDemod Search Length Auto property to True. Details |
| Digital Demod:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the digital demodulation. Details |
| Digital Demod:Results:Carrier:Mean Frequency Offset (Hz) | Returns the measured frequency offset from the transmitted carrier frequency. This value is expressed in Hz. Details |
| Digital Demod:Results:Carrier:Mean Frequency Drift (Hz) | Returns the measured carrier frequency drift. This value is expressed in Hz. Details |
| Digital Demod:Results:Carrier:Mean Phase Error (deg) | Returns the measured phase offset from the transmitted carrier phase. This value is expressed in degrees. Details |
| Digital Demod:Results:EVM:Mean RMS (%) | Returns the mean of the RMS EVM measured per acquisition, as a percentage. Details |
| Digital Demod:Results:EVM:Maximum RMS (%) | Returns the maximum of the RMS EVM measured per acquisition, as a percentage. Details |
| Digital Demod:Results:EVM:Mean Peak (%) | Returns the mean of the peak EVM measured per acquisition, as a percentage. Details |
| Digital Demod:Results:EVM:Maximum Peak (%) | Returns the maximum of the peak EVM measured per acquisition, as a percentage. Details |
| Digital Demod:Results:EVM:Mean Modulation Error Ratio (dB) | Returns the modulation error ratio. This value is expressed in dB. Details |
| Digital Demod:Results:Offset EVM:Mean RMS (%) | Returns the mean of the RMS EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. Details |
| Digital Demod:Results:Offset EVM:Mean Peak (%) | Returns the mean of the peak EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. Details |
| Digital Demod:Results:Offset EVM:Maximum RMS (%) | Returns the maximum of the RMS EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. Details |
| Digital Demod:Results:Offset EVM:Maximum Peak (%) | Returns the maximum of the peak EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. Details |
| Digital Demod:Results:Magnitude Error:Mean (%) | Returns the mean of the magnitude error measured per acquisition, as a percentage. Details |
| Digital Demod:Results:Magnitude Error:Maximum (%) | Returns the maximum of the magnitude error measured per acquisition, as a percentage. Details |
| Digital Demod:Results:Phase Error:Mean (deg) | Returns the mean of the phase error measured per acquisition. This value is expressed in degrees. Details |
| Digital Demod:Results:Phase Error:Maximum (deg) | Returns the maximum of the phase error measured per acquisition. This value is expressed in degrees. Details |
| Digital Demod:Results:FSK:Mean Deviation (Hz) | Returns the reference FSK deviation used to measure the FSK error. This value is expressed in Hz. Details |
| Digital Demod:Results:FSK:Mean RMS FSK Error (Hz) | Returns the mean of the RMS frequency error of the FSK symbols measured per acquisition. This value is expressed in Hz. Details |
| Digital Demod:Results:FSK:Max Peak FSK Error (Hz) | Returns the maximum of peak frequency error of the FSK symbols measured per acquisition. This value is expressed in Hz. Details |
| Digital Demod:Results:IQ Impairments:Mean IQ Origin Offset (dB) | Returns the offset from the ideal location of the constellation origin. This value is expressed in dB. Details |
| Digital Demod:Results:IQ Impairments:Mean IQ Gain Imbalance (dB) | Returns the measured ratio of I gain to Q gain. This value is expressed in dB. Details |
| Digital Demod:Results:IQ Impairments:Mean Quadrature Skew (deg) | Returns a measure of I and Q components in the signal that are not perfectly orthogonal. Quadrature error can be either positive or negative, with the sign indicating the orientation of the error. Details |
| Digital Demod:Results:Mean Rho Factor | Returns the correlation of the measurement waveform and the reference waveform. Details |
| Digital Demod:Results:Mean Amplitude Droop (dB/Symbol) | Returns the mean amplitude droop per symbol. Details |
| Digital Demod:Results:Sync Found? | Indicates whether the synchronization bits were found in the demodulated signal. Details |
| Advanced:Auto Level Initial Reference Level (dBm) | Specifies the initial reference level which the RFmxDemod Auto Level VI uses to estimate the peak power of the input signal. This value is expressed in dBm. Details |
| Advanced:Limited Configuration Change | Specifies the set of properties that are considered by RFmx in the locked signal configuration state. Details |
| Result Fetch Timeout (s) | Specifies the time to wait before results are available in the RFmxDemod Property Node. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxDemod Property Node waits until the measurement is complete. This value is expressed in seconds. Details |
