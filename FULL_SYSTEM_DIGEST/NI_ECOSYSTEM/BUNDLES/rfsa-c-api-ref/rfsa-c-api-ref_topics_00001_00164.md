# NI DOCUMENT BUNDLE: rfsa-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfsa-c-api-ref start=1 end=164 -->
<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__acquisition.html language=enus -->
## TOPIC 00001: Acquisition

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__acquisition.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__acquisition.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdvancedFetchIQSpectrumGroup membersNameDescriptionNIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTHSpecifies the instantaneous bandwidth of the device in hertz (Hz). AttachmentsNone

### Acquisition

#### Groups

- Advanced
- Fetch
- IQ
- Spectrum

#### Group members

| Name | Description |
| --- | --- |
| NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH | Specifies the instantaneous bandwidth of the device in hertz (Hz). |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__acquisition__advanced_1ga1f5ada0204044d908b4a6c293275cbb3.html language=enus -->
## TOPIC 00002: NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET_MODE

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__acquisition__advanced_1ga1f5ada0204044d908b4a6c293275cbb3.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__acquisition__advanced_1ga1f5ada0204044d908b4a6c293275cbb3.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to allow NI-RFSA to select the downconveter frequency offset. SyntaxNIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET_MODENumeric ValueData TypeAccessApplies To1150305ViInt32Read/WriteN/ARemarks You can either set an offset yourself or let NI-RFSA select one for you.Placing the downconver

### NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET_MODE

Specifies whether to allow NI-RFSA to select the downconveter frequency offset.

#### Syntax

NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150305 | ViInt32 | Read/Write | N/A |

#### Remarks

You can either set an offset yourself or let NI-RFSA select one for you.

Placing the downconverter center frequency outside the bandwidth of your input signal can help avoid issues such as LO leakage.

To set an offset yourself, set this attribute to **NIRFSA_VAL_AUTOMATIC** or **NIRFSA_VAL_USER_DEFINED**, and set either the [NIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCY](group____root__ni_r_f_s_a__attributes__acquisition__advanced_1ga2c531ee7ba9d98d6425e02725ac1dd51.html) or the [NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET](group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__acquisition__advanced_1gafc88efe7a66107e16fb0a9356cc21262.html) attributes.

To allow NI-RFSA to automatically select the downconverter frequency offset, set this attribute to **NIRFSA_VAL_AUTOMATIC** or **NIRFSA_VAL_ENABLED** and configure the [NIRFSA_ATTR_SIGNAL_BANDWIDTH](group____root__ni_r_f_s_a__attributes__acquisition__iq_1ga06a017af89cee8ecaa0d740f3074e7a1.html) attribute to describe your expected input signal. The signal bandwidth must be no greater than half the specified value of the [NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH](group____root__ni_r_f_s_a__attributes__acquisition_1ga6dc8cd7ae513eea80c2f0f7206bfe0c0.html) attribute, minus a device-specific guard band. Do not set the [NIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCY](group____root__ni_r_f_s_a__attributes__acquisition__advanced_1ga2c531ee7ba9d98d6425e02725ac1dd51.html) or [NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET](group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__acquisition__advanced_1gafc88efe7a66107e16fb0a9356cc21262.html) attributes. If all conditions are met, NI-RFSA places the downconverter center frequency outside the signal bandwidth. Set this attribute to **NIRFSA_VAL_ENABLED** if you want to receive an error any time NI-RFSA is unable to apply automatic offset.

When you set an offset yourself or do not use an offset, the reference frequency for gain is near the downconverter center frequency, and [NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET_MODE](group____root__ni_r_f_s_a__attributes__acquisition__advanced_1ga1f5ada0204044d908b4a6c293275cbb3.html) returns **NIRFSA_VAL_USER_DEFINED**. When NI-RFSA automatically sets an offset, the reference frequency for gain is the [NIRFSA_ATTR_IQ_CARRIER_FREQUENCY](group____root__ni_r_f_s_a__attributes__acquisition__iq_1ga12f2828abb7b5df5ee998deba3135019.html), and [NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET_MODE](group____root__ni_r_f_s_a__attributes__acquisition__advanced_1ga1f5ada0204044d908b4a6c293275cbb3.html) returns **NIRFSA_VAL_ENABLED**. Refer to the specifications document for your device for more information about gain, flatness, and reference frequencies.

Note

Below 120 MHz, the PXIe-5841 does not use an LO and **NIRFSA_VAL_ENABLED** is unavailable. Refer to the *PXIe-5841 Automatic Frequency Offset* topic for more information about using an automatic offset with an external LO.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIRFSA_VAL_AUTOMATIC | 1903 (0x76f) | NI-RFSA places the downconverter center frequency outside of the signal bandwidth if the NIRFSA_ATTR_SIGNAL_BANDWIDTH attribute has been set and can be avoided. |
| NIRFSA_VAL_ENABLED | 1901 (0x76d) | NI-RFSA places the downconverter center frequency outside of the signal bandwidth if the NIRFSA_ATTR_SIGNAL_BANDWIDTH attribute has been set and can be avoided. NI-RFSA returns an error if the NIRFSA_ATTR_SIGNAL_BANDWIDTH attribute has not been set, or if the signal bandwidth is too large. |
| NIRFSA_VAL_USER_DEFINED | 1904 (0x770) | NI-RFSA uses the offset that you specified with the NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET or NIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCY attributes. |

**Default Value:****NIRFSA_VAL_AUTOMATIC**

**Supported Devices**: PXIe-5830/5831/5832/5841/5842

**Related Topics**

[PXIe-5830 Automatic Frequency Offset](https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/automatic-frequency-offset.html)

[PXIe-5831/5832 Automatic Frequency Offset](https://www.ni.com/docs/en-US/bundle/pxie-5831/page/automatic-frequency-offset.html)

[PXIe-5841 Automatic Frequency Offset](https://www.ni.com/docs/en-US/bundle/pxie-5841/page/automatic-frequency-offset.html)

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__acquisition__advanced_1ga2c531ee7ba9d98d6425e02725ac1dd51.html language=enus -->
## TOPIC 00003: NIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCY

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__acquisition__advanced_1ga2c531ee7ba9d98d6425e02725ac1dd51.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__acquisition__advanced_1ga2c531ee7ba9d98d6425e02725ac1dd51.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables in-band retuning and specifies the current frequency, in hertz (Hz), of the RF downconverter. SyntaxNIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCYNumeric ValueData TypeAccessApplies To1150082ViReal64Read/WriteN/ARemarks If you set this attribute, any measurements outside the instantaneous bandwi

### NIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCY

Enables in-band retuning and specifies the current frequency, in hertz (Hz), of the RF downconverter.

#### Syntax

NIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150082 | ViReal64 | Read/Write | N/A |

#### Remarks

If you set this attribute, any measurements outside the instantaneous bandwidth of the device are invalid. To disable in-band retuning, reset the attribute or call the [niRFSA_ResetDevice](group____root__ni_r_f_s_a__functions__utility_1ga3fb4b35bed5a9e5560d062673a4846df.html) function.

After you set this attribute, the downconverter is locked to that frequency until the value is changed or the attribute is reset. Locking the downconverter to a fixed value allows frequencies within the instantaneous bandwidth of the downconverter to be measured with minimal overhead, decreasing tuning time.

**Valid Values**: Any supported tuning frequency of the device

**PXIe-5820**: The only valid value for this attribute is 0 Hz.

**Default Value**:

**PXIe-5694**: The default value for the PXIe-5694 is 193.6 MHz unless you set the [NIRFSA_ATTR_SIGNAL_CONDITIONING_ENABLED](group____root__ni_r_f_s_a__attributes__signal__path__advanced__ni__5694_1ga911d8d431b9d0d8d9737e434ec6c4944.html) attribute to **NIRFSA_VAL_SIGNAL_CONDITIONING_BYPASSED**, in which case the default value is 187.5 MHz.

**All other devices**: The carrier frequency or spectrum center frequency. NI-RFSA sets this attribute to the default value based on the value of the [NIRFSA_ATTR_ACQUISITION_TYPE](group____root__ni_r_f_s_a__attributes_1ga9a481e05f8dbacfbfc47cd622d990181.html) attribute.

**Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__acquisition__iq_1gaf10a45675d549e7f9118945b2b2d3887.html language=enus -->
## TOPIC 00004: NIRFSA_ATTR_NUMBER_OF_SAMPLES_IS_FINITE

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__acquisition__iq_1gaf10a45675d549e7f9118945b2b2d3887.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__acquisition__iq_1gaf10a45675d549e7f9118945b2b2d3887.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the device acquires a finite number of samples or acquires continuously. SyntaxNIRFSA_ATTR_NUMBER_OF_SAMPLES_IS_FINITENumeric ValueData TypeAccessApplies To1150008ViBooleanRead/WriteN/ARemarksDefined Values:ValueDescriptionVI_TRUEAcquire a finite number of samples.VI_FALSEAcquire c

### NIRFSA_ATTR_NUMBER_OF_SAMPLES_IS_FINITE

Specifies whether the device acquires a finite number of samples or acquires continuously.

#### Syntax

NIRFSA_ATTR_NUMBER_OF_SAMPLES_IS_FINITE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150008 | ViBoolean | Read/Write | N/A |

#### Remarks

**Defined Values:**

| Value | Description |
| --- | --- |
| VI_TRUE | Acquire a finite number of samples. |
| VI_FALSE | Acquire continuously until you abort the acquisition. |

**Default Value**: VI_TRUE

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[I/Q Modulation](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html)

**High-Level Functions**:

- [niRFSA_ConfigureNumberOfSamples](group____root__ni_r_f_s_a__functions__configuration__iq_1ga357d6779ea861fb4fdbf1fb620f4284d.html)

Parent topic:

IQ

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__acquisition__iq_1gafe66841e4a2a0fcd0460b0b32cb63696.html language=enus -->
## TOPIC 00005: NIRFSA_ATTR_PHASE_OFFSET

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__acquisition__iq_1gafe66841e4a2a0fcd0460b0b32cb63696.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__acquisition__iq_1gafe66841e4a2a0fcd0460b0b32cb63696.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the offset to apply to the initial I and Q phases. SyntaxNIRFSA_ATTR_PHASE_OFFSETNumeric ValueData TypeAccessApplies To1150106ViReal64Read/WriteN/ARemarksValid Values: 0 to 180Default Value: 0Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5

### NIRFSA_ATTR_PHASE_OFFSET

Specifies the offset to apply to the initial I and Q phases.

#### Syntax

NIRFSA_ATTR_PHASE_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150106 | ViReal64 | Read/Write | N/A |

#### Remarks

**Valid Values**: 0 to 180

**Default Value**: 0

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

Parent topic:

IQ

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1ga3bc5f3c94f98b6bb7dde3dc8a0de4256.html language=enus -->
## TOPIC 00006: NIRFSA_ATTR_FFT_WINDOW_SHAPE_FACTOR

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1ga3bc5f3c94f98b6bb7dde3dc8a0de4256.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1ga3bc5f3c94f98b6bb7dde3dc8a0de4256.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the shape factor of the window used in the fast Fourier transform (FFT). SyntaxNIRFSA_ATTR_FFT_WINDOW_SHAPE_FACTORNumeric ValueData TypeAccessApplies To1150206ViReal64Read-OnlyN/ARemarks The window shape factor is defined as the ratio of the 60 dB to 6 dB bandwidths.The following table shows

### NIRFSA_ATTR_FFT_WINDOW_SHAPE_FACTOR

Returns the shape factor of the window used in the fast Fourier transform (FFT).

#### Syntax

NIRFSA_ATTR_FFT_WINDOW_SHAPE_FACTOR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150206 | ViReal64 | Read-Only | N/A |

#### Remarks

The window shape factor is defined as the ratio of the 60 dB to 6 dB bandwidths.

The following table shows the shape factor for each NI-RFSA FFT window type.

| Window Type | Shape Factor |
| --- | --- |
| Uniform | 1.57:1 |
| Hanning | 1.94:1 |
| Hamming | 2.13:1 |
| Exact Blackman | 2.52:1 |
| Flat Top | 2.0:1 |
| 4-term Blackman-Harris | 2.5:1 |
| 7-term Blackman-Harris | 4.1:1 |
| Low Side Lobe | 2.78:1 |
| Gaussian | 2.3:1 |
| Kaiser Bessel | 2.55:1 |

**Default Value**: N/A

**Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842/5860

Parent topic:

Spectrum

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1ga43a9f81683c6ee4d3adb2cf3d8f7fb39.html language=enus -->
## TOPIC 00007: NIRFSA_ATTR_SPECTRUM_OSP_SAMPLING_RATIO

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1ga43a9f81683c6ee4d3adb2cf3d8f7fb39.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1ga43a9f81683c6ee4d3adb2cf3d8f7fb39.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the oversampling ratio used by the digitizer onboard signal processing (OSP) when you are in spectrum acquisition mode. This attribute allows you to acquire a larger bandwidth in hardware and reduce that bandwidth in software, decreasing the possibility of hardware data path overflows. Syn

### NIRFSA_ATTR_SPECTRUM_OSP_SAMPLING_RATIO

Specifies the oversampling ratio used by the digitizer onboard signal processing (OSP) when you are in spectrum acquisition mode. This attribute allows you to acquire a larger bandwidth in hardware and reduce that bandwidth in software, decreasing the possibility of hardware data path overflows.

#### Syntax

NIRFSA_ATTR_SPECTRUM_OSP_SAMPLING_RATIO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150144 | ViReal64 | Read/Write | N/A |

#### Remarks

**PXIe-5644/5645/5646**: The only valid value for this attribute is 1.

**Default Value**: 1.0

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

Parent topic:

Spectrum

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1ga58e77596055e0e180f4cef90ad4dc169.html language=enus -->
## TOPIC 00008: NIRFSA_ATTR_NUMBER_OF_SPECTRAL_LINES

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1ga58e77596055e0e180f4cef90ad4dc169.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1ga58e77596055e0e180f4cef90ad4dc169.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of spectral lines expected with the current power spectrum configuration. SyntaxNIRFSA_ATTR_NUMBER_OF_SPECTRAL_LINESNumeric ValueData TypeAccessApplies To1150018ViInt32Read/WriteN/ARemarks If you do not configure this attribute, NI-RFSA selects an appropriate value based on the

### NIRFSA_ATTR_NUMBER_OF_SPECTRAL_LINES

Specifies the number of spectral lines expected with the current power spectrum configuration.

#### Syntax

NIRFSA_ATTR_NUMBER_OF_SPECTRAL_LINES

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150018 | ViInt32 | Read/Write | N/A |

#### Remarks

If you do not configure this attribute, NI-RFSA selects an appropriate value based on the [NIRFSA_ATTR_RESOLUTION_BANDWIDTH](group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1gac0609addac41edaa3680e84ed716b62e.html) attribute. If you configure this attribute, NI-RFSA coerces the [NIRFSA_ATTR_RESOLUTION_BANDWIDTH](group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1gac0609addac41edaa3680e84ed716b62e.html) value based on the number of spectral lines requested and the value of the [NIRFSA_ATTR_SPECTRUM_SPAN](group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1ga438b38abd1378c3ccf5f6035f6c9bc2b.html) attribute.

**Default Value**: N/A

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

Parent topic:

Spectrum

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1ga6e5776559e896d8b28691bacc81ad5db.html language=enus -->
## TOPIC 00009: NIRFSA_ATTR_FFT_WINDOW_SIZE

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1ga6e5776559e896d8b28691bacc81ad5db.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1ga6e5776559e896d8b28691bacc81ad5db.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the size of the window used in the fast Fourier transform (FFT), in terms of the number of samples in the window. SyntaxNIRFSA_ATTR_FFT_WINDOW_SIZENumeric ValueData TypeAccessApplies To1150049ViInt32Read-OnlyN/ARemarksDefault Value: N/ASupported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5

### NIRFSA_ATTR_FFT_WINDOW_SIZE

Returns the size of the window used in the fast Fourier transform (FFT), in terms of the number of samples in the window.

#### Syntax

NIRFSA_ATTR_FFT_WINDOW_SIZE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150049 | ViInt32 | Read-Only | N/A |

#### Remarks

**Default Value**: N/A

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

Parent topic:

Spectrum

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1ga75ba9d15ce73a68016dd1585c944e651.html language=enus -->
## TOPIC 00010: NIRFSA_ATTR_SPECTRUM_NUMBER_OF_AVERAGES

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1ga75ba9d15ce73a68016dd1585c944e651.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1ga75ba9d15ce73a68016dd1585c944e651.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions to average. SyntaxNIRFSA_ATTR_SPECTRUM_NUMBER_OF_AVERAGESNumeric ValueData TypeAccessApplies To1150015ViInt32Read/WriteN/ARemarks The averaging process returns the final result after the number of averages is complete.Default Value: 10Supported Devices: PXIe-5644

### NIRFSA_ATTR_SPECTRUM_NUMBER_OF_AVERAGES

Specifies the number of acquisitions to average.

#### Syntax

NIRFSA_ATTR_SPECTRUM_NUMBER_OF_AVERAGES

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150015 | ViInt32 | Read/Write | N/A |

#### Remarks

The averaging process returns the final result after the number of averages is complete.

**Default Value**: 10

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

Parent topic:

Spectrum

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1gac0609addac41edaa3680e84ed716b62e.html language=enus -->
## TOPIC 00011: NIRFSA_ATTR_RESOLUTION_BANDWIDTH

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1gac0609addac41edaa3680e84ed716b62e.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1gac0609addac41edaa3680e84ed716b62e.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the resolution along the x-axis of the spectrum. SyntaxNIRFSA_ATTR_RESOLUTION_BANDWIDTHNumeric ValueData TypeAccessApplies To1150013ViReal64Read/WriteN/ARemarks NI-RFSA uses the resolution bandwidth value to determine the acquisition size. If specified, the NIRFSA_ATTR_NUMBER_OF_SPECTRAL_L

### NIRFSA_ATTR_RESOLUTION_BANDWIDTH

Specifies the resolution along the x-axis of the spectrum.

#### Syntax

NIRFSA_ATTR_RESOLUTION_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150013 | ViReal64 | Read/Write | N/A |

#### Remarks

NI-RFSA uses the resolution bandwidth value to determine the acquisition size. If specified, the [NIRFSA_ATTR_NUMBER_OF_SPECTRAL_LINES](group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1ga58e77596055e0e180f4cef90ad4dc169.html) attribute value overrides this value.

**Units**: hertz (Hz)

**Default Value**: 100 kHz

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**High-Level Functions**:

- [niRFSA_ConfigureResolutionBandwidth](group____root__ni_r_f_s_a__functions__configuration__spectrum_1gaad0f0bcd3df485882b0fe07d3b02407f.html)

Parent topic:

Spectrum

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1gaca824bc5f70525661bfb8d75b73c4edf.html language=enus -->
## TOPIC 00012: NIRFSA_ATTR_FFT_WINDOW_TYPE

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1gaca824bc5f70525661bfb8d75b73c4edf.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1gaca824bc5f70525661bfb8d75b73c4edf.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time-domain window type. SyntaxNIRFSA_ATTR_FFT_WINDOW_TYPENumeric ValueData TypeAccessApplies To1150017ViInt32Read/WriteN/ARemarksDefined Values:NameValueDescriptionNIRFSA_VAL_4_TERM_BLACKMAN_HARRIS507 (0x1fb)A 4-term Blackman-Harris window is a general purpose window; it has side-lobe

### NIRFSA_ATTR_FFT_WINDOW_TYPE

Specifies the time-domain window type.

#### Syntax

NIRFSA_ATTR_FFT_WINDOW_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150017 | ViInt32 | Read/Write | N/A |

#### Remarks

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIRFSA_VAL_4_TERM_BLACKMAN_HARRIS | 507 (0x1fb) | A 4-term Blackman-Harris window is a general purpose window; it has side-lobe rejection in the upper 90 dB, with moderately wide side lobe. A 4-term Blackman Harris window is applied to the waveform using the following equation: y[i] = x[i] * (a0 - a1*cos(w) + a2*cos(2w) - a3*cos(3w)) |
| NIRFSA_VAL_7_TERM_BLACKMAN_HARRIS | 508 (0x1fc) | A 7-term Blackman-Harris window has the highest dynamic range; it is ideal for signal-to-noise ratio applications. A 7-term Blackman Harris window is applied to the waveform using the following equation: y[i] = x[i] * (a0 - a1*cos(w) + a2*cos(2w) - a3*cos(3w) + a4*cos(4w) - a5*cos(5w) + a6*cos(6w)) |
| NIRFSA_VAL_BLACKMAN | 505 (0x1f9) | A Blackman window is useful for analyzing transient signals, and provides similar windowing to Hanning and Hamming windows but adds one additional cosine term to reduce ripple. A Blackman window is applied to the waveform using the following equation: y[i] = x[i] * (0.42 - 0.50*cos(w) + 0.08*cos(2w)) |
| NIRFSA_VAL_BLACKMAN_HARRIS | 503 (0x1f7) | A Blackman-Harris window is applied to the waveform using the following equation: y[i] = x[i] * (0.42323 - 0.49755*cos(w) + 0.07922*cos(2w)) |
| NIRFSA_VAL_EXACT_BLACKMAN | 504 (0x1f8) | An Exact Blackman window is applied to the waveform using the following equation: y[i] = x[i] * (a0 - a1*cos(w) + a2*cos(2w)) |
| NIRFSA_VAL_FLAT_TOP | 506 (0x1fa) | The fifth-order Flat Top window has the best amplitude accuracy of all the window functions. The increased amplitude accuracy (0.02 dB for signals exactly between integral cycles) is at the expense of frequency selectivity. The Flat Top window is most useful in accurately measuring the amplitude of single frequency components with little nearby spectral energy in the signal. A fifth-order Flat Top window is applied to the waveform using the following equation: y[i] = x[i] * (a0 - a1*cos(w) + a2*cos(2w) - a3*cos(3w) + a4*cos(4w)) |
| NIRFSA_VAL_GAUSSIAN | 510 (0x1fe) | A Gaussian window is applied to the waveform using the following equation: y[i] = x[i] * exp(-0.5*(i - (N-1)/2)^2 / ((N-1)/2)^2) where N is the length of the window |
| NIRFSA_VAL_HAMMING | 502 (0x1f6) | A Hamming window is applied to the waveform using the following equation: y[i] = x[i] * (0.54 - 0.46cos(w)) where w = (2)i/n and n = the waveform size. Note: Hanning and Hamming windows are somewhat similar. However, in the time domain, the Hamming window does not get as close to zero near the edges as does the Hanning window. |
| NIRFSA_VAL_HANNING | 501 (0x1f5) | The Hanning window is useful for analyzing transients longer than the time duration of the window, and also for general-purpose applications. |
| NIRFSA_VAL_KAISER_BESSEL | 511 (0x1ff) | A Kaiser-Bessel window is applied to the waveform using the following equation: y[i] = x[i] * I0(β*sqrt(1 - (2i/(N-1) - 1)^2))/I0(β) where i is between 0 and N-1, N is the length of the window, β determines the shape of the window, and I0 is the zeroth order Modified Bessel function of the first kind |
| NIRFSA_VAL_LOW_SIDE_LOBE | 509 (0x1fd) | The Low Side Lobe window further reduces the size of the main lobe. The following equation defines the Low Side Lobe window. where N is the length of window |
| NIRFSA_VAL_UNIFORM | 500 (0x1f4) | No window is applied. |

**Default Values**:

**PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860**: **NIRFSA_VAL_7_TERM_BLACKMAN_HARRIS**

**PXIe-5667**: **NIRFSA_VAL_4_TERM_BLACKMAN_HARRIS**

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Resolution Bandwidth](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/resolution-bandwidth.html)

Parent topic:

Spectrum

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__configuration__list.html language=enus -->
## TOPIC 00013: Configuration List

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__configuration__list.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__configuration__list.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdvancedGroup membersNameDescriptionNIRFSA_ATTR_ACTIVE_CONFIGURATION_LISTSpecifies the configuration list for RF list mode to make active for configuration or initiation. NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST_STEPSpecifies the step in the configuration list for RF list mode to make active for

### Configuration List

#### Groups

- Advanced

#### Group members

| Name | Description |
| --- | --- |
| NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST | Specifies the configuration list for RF list mode to make active for configuration or initiation. |
| NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST_STEP | Specifies the step in the configuration list for RF list mode to make active for configuration or initiation. |
| NIRFSA_ATTR_CONFIGURATION_LIST_STEP_IN_PROGRESS | Returns the configuration list step that is currently programmed to the hardware. |
| NIRFSA_ATTR_TIMER_EVENT_INTERVAL | Specifies the time, in seconds, that the timer counts before generating a Timer Event. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__configuration__list_1ga3a484b0bbdceacf87a54aab83b19948f.html language=enus -->
## TOPIC 00014: NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST_STEP

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__configuration__list_1ga3a484b0bbdceacf87a54aab83b19948f.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__configuration__list_1ga3a484b0bbdceacf87a54aab83b19948f.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the step in the configuration list for RF list mode to make active for configuration or initiation. SyntaxNIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST_STEPNumeric ValueData TypeAccessApplies To1150093ViInt64Read/WriteN/ARemarks Activating a list makes all attributes in the list reflect the value

### NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST_STEP

Specifies the step in the configuration list for [RF list mode](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html) to make active for configuration or initiation.

#### Syntax

NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST_STEP

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150093 | ViInt64 | Read/Write | N/A |

#### Remarks

Activating a list makes all attributes in the list reflect the value of the attributes that correspond to the set specified by the [NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST](group____root__ni_r_f_s_a__attributes__configuration__list_1gacc35d7d7792b502b870e9cd7258427d2.html) and the [NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST_STEP](group____root__ni_r_f_s_a__attributes__configuration__list_1ga3a484b0bbdceacf87a54aab83b19948f.html) attributes.

**Default Value**: 0 for devices that support RF list mode. For all other devices, the default value is N/A.

**Supported Devices:** PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842, PXIe-5842 with S-parameters

**Related Topics**

[RF List Mode](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html)

**High-Level Functions**:

- [niRFSA_CreateConfigurationListStep](group____root__ni_r_f_s_a__functions__configuration__configuration__list_1ga6b2721268b980d7e1bd1c0ce01640eab.html)

Parent topic:

Configuration List

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__configuration__list__advanced_1ga2ff88b2708790930de749847a2c7b4da.html language=enus -->
## TOPIC 00015: NIRFSA_ATTR_MINIMUM_RECONFIG_TIME

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__configuration__list__advanced_1ga2ff88b2708790930de749847a2c7b4da.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__configuration__list__advanced_1ga2ff88b2708790930de749847a2c7b4da.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This attribute is not for customer use. SyntaxNIRFSA_ATTR_MINIMUM_RECONFIG_TIMENumeric ValueData TypeAccessApplies To1150165ViReal64Read/WriteN/A

### NIRFSA_ATTR_MINIMUM_RECONFIG_TIME

This attribute is not for customer use.

#### Syntax

NIRFSA_ATTR_MINIMUM_RECONFIG_TIME

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150165 | ViReal64 | Read/Write | N/A |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__configuration__list__advanced_1ga7d3e33a6045ad5700d8d1f96627cd3b4.html language=enus -->
## TOPIC 00016: NIRFSA_ATTR_TIMER_START_SOURCE

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__configuration__list__advanced_1ga7d3e33a6045ad5700d8d1f96627cd3b4.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__configuration__list__advanced_1ga7d3e33a6045ad5700d8d1f96627cd3b4.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This attribute is not for customer use. SyntaxNIRFSA_ATTR_TIMER_START_SOURCENumeric ValueData TypeAccessApplies To1150173ViStringRead/WriteN/A

### NIRFSA_ATTR_TIMER_START_SOURCE

This attribute is not for customer use.

#### Syntax

NIRFSA_ATTR_TIMER_START_SOURCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150173 | ViString | Read/Write | N/A |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__signal__path_1ga408ce92f2b6a3d869232ca5b7693dc71.html language=enus -->
## TOPIC 00017: NIRFSA_ATTR_DECIMATION_DELAY

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__signal__path_1ga408ce92f2b6a3d869232ca5b7693dc71.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__signal__path_1ga408ce92f2b6a3d869232ca5b7693dc71.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sub-sample delay, in seconds, to apply to the acquired signal. SyntaxNIRFSA_ATTR_DECIMATION_DELAYNumeric ValueData TypeAccessApplies To1150191ViReal64Read/WriteN/ARemarks To set this attribute, the NI-RFSA device must be in the Configuration state.Valid Values: -4.16 ns to +4.16 nsDefa

### NIRFSA_ATTR_DECIMATION_DELAY

Specifies the sub-sample delay, in seconds, to apply to the acquired signal.

#### Syntax

NIRFSA_ATTR_DECIMATION_DELAY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150191 | ViReal64 | Read/Write | N/A |

#### Remarks

To set this attribute, the NI-RFSA device must be in the Configuration state.

**Valid Values:** -4.16 ns to +4.16 ns

**Default Value**: 0

**Supported Devices:** PXIe-5644/5645/5646

Parent topic:

Signal Path

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__signal__path_1ga843cadb2e10b1700d079773427a97269.html language=enus -->
## TOPIC 00018: NIRFSA_ATTR_LO_VCO_FREQUENCY_STEP_SIZE

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__signal__path_1ga843cadb2e10b1700d079773427a97269.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__signal__path_1ga843cadb2e10b1700d079773427a97269.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the step size for tuning the internal voltage-controlled oscillator (VCO) used to generate the LO signal. SyntaxNIRFSA_ATTR_LO_VCO_FREQUENCY_STEP_SIZENumeric ValueData TypeAccessApplies To1150312ViReal64Read/WriteN/ARemarksDo not set this attribute with the NIRFSA_ATTR_LO_FREQUENCY_STEP_SI

### NIRFSA_ATTR_LO_VCO_FREQUENCY_STEP_SIZE

Specifies the step size for tuning the internal voltage-controlled oscillator (VCO) used to generate the LO signal.

#### Syntax

NIRFSA_ATTR_LO_VCO_FREQUENCY_STEP_SIZE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150312 | ViReal64 | Read/Write | N/A |

#### Remarks

Note

Do not set this attribute with the [NIRFSA_ATTR_LO_FREQUENCY_STEP_SIZE](group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__signal__path_1gacb5201a4412b3650fd836cadbee2eebe.html) attribute.

**Valid Values**:

LO1: 1 Hz to 50 MHz

LO2: 1 Hz to 100 MHz

**Default Values**: 1 MHz

**Supported Devices**: PXIe-5830/5831/5832

Parent topic:

Signal Path

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__signal__path_1gac32416f0220f50ce05c673d9acc4a67f.html language=enus -->
## TOPIC 00019: NIRFSA_ATTR_INPUT_PORT

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__signal__path_1gac32416f0220f50ce05c673d9acc4a67f.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__signal__path_1gac32416f0220f50ce05c673d9acc4a67f.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the connector(s) to use to acquire the signal. SyntaxNIRFSA_ATTR_INPUT_PORTNumeric ValueData TypeAccessApplies To1150180ViInt32Read/WriteN/ARemarks To set this attribute, the NI-RFSA device must be in the Configuration state.Defined Values:NameValueDescriptionNIRFSA_VAL_CAL_IN2002 (0x7d2)E

### NIRFSA_ATTR_INPUT_PORT

Specifies the connector(s) to use to acquire the signal.

#### Syntax

NIRFSA_ATTR_INPUT_PORT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150180 | ViInt32 | Read/Write | N/A |

#### Remarks

To set this attribute, the NI-RFSA device must be in the Configuration state.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIRFSA_VAL_CAL_IN | 2002 (0x7d2) | Enables the CAL IN port. |
| NIRFSA_VAL_I_ONLY | 2003 (0x7d3) | Enables the I terminals of the I/Q IN port. It is supported only for PXIe-5645. |
| NIRFSA_VAL_IQ_IN | 2001 (0x7d1) | Enables the I/Q IN port. |
| NIRFSA_VAL_RF_IN | 2000 (0x7d0) | Enables the RF IN port. |

**Default Values**:

**PXIe-5820**: **NIRFSA_VAL_IQ_IN**

**All other devices**: **NIRFSA_VAL_RF_IN**

**Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

Parent topic:

Signal Path

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__signal__path_1gacb5201a4412b3650fd836cadbee2eebe.html language=enus -->
## TOPIC 00020: NIRFSA_ATTR_LO_FREQUENCY_STEP_SIZE

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__signal__path_1gacb5201a4412b3650fd836cadbee2eebe.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__signal__path_1gacb5201a4412b3650fd836cadbee2eebe.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the step size for tuning the local oscillator (LO) phase-locked loop (PLL). SyntaxNIRFSA_ATTR_LO_FREQUENCY_STEP_SIZENumeric ValueData TypeAccessApplies To1150188ViReal64Read/WriteN/ARemarks You can only tune the LO frequency by multiples of the NIRFSA_ATTR_LO_FREQUENCY_STEP_SIZE attribute.

### NIRFSA_ATTR_LO_FREQUENCY_STEP_SIZE

Specifies the step size for tuning the local oscillator (LO) phase-locked loop (PLL).

#### Syntax

NIRFSA_ATTR_LO_FREQUENCY_STEP_SIZE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150188 | ViReal64 | Read/Write | N/A |

#### Remarks

You can only tune the LO frequency by multiples of the [NIRFSA_ATTR_LO_FREQUENCY_STEP_SIZE](group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__signal__path_1gacb5201a4412b3650fd836cadbee2eebe.html) attribute. For the PXIe-5644/5645/5646 and PXIe-5840/5841, the LO frequency can therefore be offset from the requested center frequency by as much as half of the [NIRFSA_ATTR_LO_FREQUENCY_STEP_SIZE](group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__signal__path_1gacb5201a4412b3650fd836cadbee2eebe.html) attribute. This offset is corrected by digitally frequency shifting the [NIRFSA_ATTR_LO_FREQUENCY](group____root__ni_r_f_s_a__attributes__signal__path_1ga004deaa1159d0e024f93afcf409e87f4.html) attribute to the value requested in either the [NIRFSA_ATTR_IQ_CARRIER_FREQUENCY](group____root__ni_r_f_s_a__attributes__acquisition__iq_1ga12f2828abb7b5df5ee998deba3135019.html) attribute or the [NIRFSA_ATTR_CENTER_FREQUENCY](group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1gacec46d3076968f9fec0aa31c7a3ddc8f.html) attribute.

Note

For the PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653, this attribute is ignored if the PXIe-5653 is used as the LO source.

The valid values for this attribute depend on the [NIRFSA_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED](group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__signal__path_1ga10fc4c608fd6c79211215ecdcd203467.html) attribute.

**PXIe-5644/5645/5646**: If the [NIRFSA_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED](group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__signal__path_1ga10fc4c608fd6c79211215ecdcd203467.html) attribute is set to **NIRFSA_VAL_DISABLED**, the specified value is coerced to the closest valid value.

**PXIe-5840/5841/5842**: If the [NIRFSA_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED](group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__signal__path_1ga10fc4c608fd6c79211215ecdcd203467.html) attribute is set to **NIRFSA_VAL_DISABLED**, the specified value is coerced to the nearest valid value that is less than or equal to the desired step size.

| NIRFSA_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED | PXIe-5644/5645 | PXIe-5646 | PXIe-5840/5841 | PXIe-5830/5831/5832 | PXIe-5841 w/PXIe-5655 |
| --- | --- | --- | --- | --- | --- |
| NIRFSA_VAL_ENABLED | 50 kHz to 24 MHz | 50 kHz to 25 MHz | 50 kHz to 100 MHz | LO1: 8 Hz to 400 MHzLO2: 4 kHz to 400 MHz | 1 nHz to 50 MHz |
| NIRFSA_VAL_DISABLED | 4 MHz, 5 MHz, 6 MHz, 12 MHz, 24 MHz | 2 MHz, 5 MHz, 10 MHz, 25 MHz | 1 MHz, 5 MHz, 10 MHz, 25 MHz, 50 MHz, 100 MHz | LO1: –LO2:– | 1 nHz to 50 MHz |

- Values up to 100 MHz are coerced to 50 MHz.

Note

The default value for the PXIe-5831 depends on the frequency range of the selected port for your instrument configuration. Refer to the [Instrument Configurations](https://www.ni.com/docs/en-US/bundle/pxie-5831/page/instrument-configurations.html) topic for more information about available ports for your hardware configuration.

**Default Values:**

**PXIe-5644/5645/5646:** 200 kHz

**PXIe-5830:** 2 MHz

**PXIe-5831/5832 (RF port):** 8 MHz

**PXIe-5831/5832 (IF port):** 2 MHz, 4 MHz

**PXIe-5840/5841:**

- Fractional mode: 500 kHz
- Integer mode: 10 MHz for frequencies less than or equal to 4 GHz. 20 MHz for frequencies greater than 4 GHz.

**PXIe-5841 with PXIe-5655:** 500 kHz

**PXIe-5842:** 1 Hz

**Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

Parent topic:

Signal Path

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__triggers__ref__iq__analog__edge_1ga45896422b4c7ad3d55a2ae8f566af9ea.html language=enus -->
## TOPIC 00021: NIRFSA_ATTR_IQ_ANALOG_EDGE_REF_TRIGGER_SOURCE

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__triggers__ref__iq__analog__edge_1ga45896422b4c7ad3d55a2ae8f566af9ea.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__triggers__ref__iq__analog__edge_1ga45896422b4c7ad3d55a2ae8f566af9ea.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the channel from which the device monitors the trigger. SyntaxNIRFSA_ATTR_IQ_ANALOG_EDGE_REF_TRIGGER_SOURCENumeric ValueData TypeAccessApplies To1150192ViStringRead/WriteN/ARemarks Use a value of "I" to monitor the I channel. Use a value of "Q" to monitor the Q channel. Use a value of "I,Q

### NIRFSA_ATTR_IQ_ANALOG_EDGE_REF_TRIGGER_SOURCE

Specifies the channel from which the device monitors the trigger.

#### Syntax

NIRFSA_ATTR_IQ_ANALOG_EDGE_REF_TRIGGER_SOURCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150192 | ViString | Read/Write | N/A |

#### Remarks

Use a value of "I" to monitor the I channel. Use a value of "Q" to monitor the Q channel. Use a value of "I,Q" to monitor both I and Q channels. This attribute affects the device operation only when the [NIRFSA_ATTR_REF_TRIGGER_TYPE](group____root__ni_r_f_s_a__attributes__triggers__ref_1gaedc1117583c01c4d93a4a3a0f504b5de.html) attribute is set to **NIRFSA_VAL_IQ_ANALOG_EDGE**.

**Valid Values:** "I", "Q", "I,Q", "Q,I"

**Default Value:** "I"

**Supported Devices:** PXIe-5644/5645

Parent topic:

IQ Analog Edge

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__triggers__synchronization_1ga534acb8e7f8e525eb77a3886f5336c89.html language=enus -->
## TOPIC 00022: NIRFSA_ATTR_SYNC_REF_TRIGGER_DIST_LINE

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__triggers__synchronization_1ga534acb8e7f8e525eb77a3886f5336c89.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__triggers__synchronization_1ga534acb8e7f8e525eb77a3886f5336c89.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which external trigger line distributes the synchronized Reference Trigger signal. SyntaxNIRFSA_ATTR_SYNC_REF_TRIGGER_DIST_LINENumeric ValueData TypeAccessApplies To1150179ViStringRead/WriteN/ARemarks When synchronizing the Reference Trigger, configure all devices to use the same Reference

### NIRFSA_ATTR_SYNC_REF_TRIGGER_DIST_LINE

Specifies which external trigger line distributes the synchronized Reference Trigger signal.

#### Syntax

NIRFSA_ATTR_SYNC_REF_TRIGGER_DIST_LINE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150179 | ViString | Read/Write | N/A |

#### Remarks

When synchronizing the Reference Trigger, configure all devices to use the same Reference Trigger distribution line.

Refer to the *Synchronization Using NI-RFSA and NI-RFSG* topic appropriate to your device in the *NI RF Vector Signal Analyzers Help* for more information about device synchronization for vector signal transceivers.

**Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0

**Default Value**: "" (empty string)

**Supported Devices:** PXIe-5644/5645/5646

Parent topic:

Synchronization

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__triggers__synchronization_1gab31302613de833d9ba4a9dc4d2d6b958.html language=enus -->
## TOPIC 00023: NIRFSA_ATTR_SYNC_SAMPLE_CLOCK_DIST_LINE

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__triggers__synchronization_1gab31302613de833d9ba4a9dc4d2d6b958.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__triggers__synchronization_1gab31302613de833d9ba4a9dc4d2d6b958.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which external trigger line distributes the Sample Clock sync signal. SyntaxNIRFSA_ATTR_SYNC_SAMPLE_CLOCK_DIST_LINENumeric ValueData TypeAccessApplies To1150218ViStringRead/WriteN/ARemarks When synchronizing the Sample Clock, configure all devices to use the same Sample Clock distribution

### NIRFSA_ATTR_SYNC_SAMPLE_CLOCK_DIST_LINE

Specifies which external trigger line distributes the Sample Clock sync signal.

#### Syntax

NIRFSA_ATTR_SYNC_SAMPLE_CLOCK_DIST_LINE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150218 | ViString | Read/Write | N/A |

#### Remarks

When synchronizing the Sample Clock, configure all devices to use the same Sample Clock distribution line.

Refer to [Synchronization Using NI-RFSA and NI-RFSG](https://www.ni.com/docs/en-US/bundle/pxie-5644-feature/page/synchronization-rfsa-g.html) for more information about PXIe-5646 device synchronization.

**Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0

**Default Value:** "" (empty string)

**Supported Devices:** PXIe-5646

Parent topic:

Synchronization

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__triggers__synchronization_1gac8da2d1cbfbf2befba409fe51f0f3c48.html language=enus -->
## TOPIC 00024: NIRFSA_ATTR_SYNC_START_TRIGGER_DIST_LINE

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__triggers__synchronization_1gac8da2d1cbfbf2befba409fe51f0f3c48.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__triggers__synchronization_1gac8da2d1cbfbf2befba409fe51f0f3c48.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which external trigger line distributes the synchronized Start Trigger signal. SyntaxNIRFSA_ATTR_SYNC_START_TRIGGER_DIST_LINENumeric ValueData TypeAccessApplies To1150177ViStringRead/WriteN/ARemarks When synchronizing the Start Trigger, configure all devices to use the same Start Trigger d

### NIRFSA_ATTR_SYNC_START_TRIGGER_DIST_LINE

Specifies which external trigger line distributes the synchronized Start Trigger signal.

#### Syntax

NIRFSA_ATTR_SYNC_START_TRIGGER_DIST_LINE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150177 | ViString | Read/Write | N/A |

#### Remarks

When synchronizing the Start Trigger, configure all devices to use the same Start Trigger distribution line.

Refer to the *Synchronization Using NI-RFSA and NI-RFSG* topic appropriate to your device in the *NI RF Vector Signal Analyzers Help* for more information about device synchronization for vector signal transceivers.

**Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0

**Default Value**: "" (empty string)

**Supported Devices**: PXIe-5644/5645/5646

Parent topic:

Synchronization

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__triggers__synchronization_1gae47f1b7c95c16427d115dca934a46125.html language=enus -->
## TOPIC 00025: NIRFSA_ATTR_SYNC_REF_TRIGGER_MASTER

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__triggers__synchronization_1gae47f1b7c95c16427d115dca934a46125.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__device__specific__vector__signal__transceiver__triggers__synchronization_1gae47f1b7c95c16427d115dca934a46125.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the device is the master for synchronizing the shared Reference Trigger between multiple devices. SyntaxNIRFSA_ATTR_SYNC_REF_TRIGGER_MASTERNumeric ValueData TypeAccessApplies To1150178ViBooleanRead/WriteN/ARemarks The master device distributes the synchronized Reference Trigger to

### NIRFSA_ATTR_SYNC_REF_TRIGGER_MASTER

Specifies whether the device is the master for synchronizing the shared Reference Trigger between multiple devices.

#### Syntax

NIRFSA_ATTR_SYNC_REF_TRIGGER_MASTER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150178 | ViBoolean | Read/Write | N/A |

#### Remarks

The master device distributes the synchronized Reference Trigger to all devices in the system through the Reference Trigger distribution line.

When synchronizing the Reference Trigger, one device must always be designated as the master. When the device is configured as a master, it actively drives the Reference Trigger distribution line. When the device is configured as a slave, set the [NIRFSA_ATTR_REF_TRIGGER_TYPE](group____root__ni_r_f_s_a__attributes__triggers__ref_1gaedc1117583c01c4d93a4a3a0f504b5de.html) attribute to **NIRFSA_VAL_DIGITAL_EDGE**, and the [NIRFSA_ATTR_DIGITAL_EDGE_REF_TRIGGER_SOURCE](group____root__ni_r_f_s_a__attributes__triggers__ref__digital__edge_1gae2ac734aaa4700fc4c03ee0de9955fa9.html) attribute to NIRFSA VAL SYNC REF TRIGGER STR.

Refer to the *Synchronization Using NI-RFSA and NI-RFSG* topic appropriate to your device in the *NI RF Vector Signal Analyzers Help* for more information about device synchronization for vector signal transceivers.

**Defined Values:**

| Value | Description |
| --- | --- |
| VI_TRUE | The device is the master device for synchronizing the Ref Trigger. |
| VI_FALSE | The device is not the master device for synchronizing the Ref Trigger. |

**Default Value**: VI_FALSE

**Supported Devices:** PXIe-5644/5645/5646

Parent topic:

Synchronization

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__events__done_1gac358db8a77f659e181c2e8c71ae4f9ab.html language=enus -->
## TOPIC 00026: NIRFSA_ATTR_EXPORTED_DONE_EVENT_OUTPUT_TERMINAL

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__events__done_1gac358db8a77f659e181c2e8c71ae4f9ab.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__events__done_1gac358db8a77f659e181c2e8c71ae4f9ab.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for the Done Event. SyntaxNIRFSA_ATTR_EXPORTED_DONE_EVENT_OUTPUT_TERMINALNumeric ValueData TypeAccessApplies To1150054ViStringRead/WriteN/ARemarksDefined Values:NameValueDescriptionNIRFSA_VAL_CLK_OUT_STRClkOutExport the clock on the CLK OUT terminal on the IF digit

### NIRFSA_ATTR_EXPORTED_DONE_EVENT_OUTPUT_TERMINAL

Specifies the destination terminal for the Done Event.

#### Syntax

NIRFSA_ATTR_EXPORTED_DONE_EVENT_OUTPUT_TERMINAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150054 | ViString | Read/Write | N/A |

#### Remarks

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIRFSA_VAL_CLK_OUT_STR | ClkOut | Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841. |
| NIRFSA_VAL_DO_NOT_EXPORT_STR |  | The signal is not exported. |
| NIRFSA_VAL_PFI0_STR | PFI0 | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0. |
| NIRFSA_VAL_PFI1_STR | PFI1 | The trigger is received on PFI 1. |
| NIRFSA_VAL_PXI_STAR_STR | PXI_STAR | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646. |
| NIRFSA_VAL_PXI_TRIG0_STR | PXI_Trig0 | The trigger is received on PXI trigger line 0. |
| NIRFSA_VAL_PXI_TRIG1_STR | PXI_Trig1 | The trigger is received on PXI trigger line 1. |
| NIRFSA_VAL_PXI_TRIG2_STR | PXI_Trig2 | The trigger is received on PXI trigger line 2. |
| NIRFSA_VAL_PXI_TRIG3_STR | PXI_Trig3 | The trigger is received on PXI trigger line 3. |
| NIRFSA_VAL_PXI_TRIG4_STR | PXI_Trig4 | The trigger is received on PXI trigger line 4. |
| NIRFSA_VAL_PXI_TRIG5_STR | PXI_Trig5 | The trigger is received on PXI trigger line 5. |
| NIRFSA_VAL_PXI_TRIG6_STR | PXI_Trig6 | The trigger is received on PXI trigger line 6. |
| NIRFSA_VAL_PXI_TRIG7_STR | PXI_Trig7 | The trigger is received on PXI trigger line 7. |
| NIRFSA_VAL_PXIE_DSTARC_STR | PXIe_DStarC | The trigger is received on the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841. |
| NIRFSA_VAL_REF_OUT_STR | RefOut | Export the clock on the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, PXIe-5694, or PXIe-5820/5830/5831/5832/5840/5841. |
| NIRFSA_VAL_REF_OUT2_STR | RefOut2 | Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E. |
| NIRFSA_VAL_DIO_PFI0_STR | DIO/PFI0 | The trigger is received on PFI0 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI1_STR | DIO/PFI1 | The trigger is received on PFI1 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI2_STR | DIO/PFI2 | The trigger is received on PFI2 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI3_STR | DIO/PFI3 | The trigger is received on PFI3 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI4_STR | DIO/PFI4 | The trigger is received on PFI4 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI5_STR | DIO/PFI5 | The trigger is received on PFI5 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI6_STR | DIO/PFI6 | The trigger is received on PFI6 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI7_STR | DIO/PFI7 | The trigger is received on PFI7 from the front panel DIO terminal. |

**Default Value**: "" (empty string)

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**High-Level Functions**:

- [niRFSA_ExportSignal](group____root__ni_r_f_s_a__functions__configuration__clock_1gaa0e7acfa202c06fb09bdf610d8a613eb.html)

Parent topic:

Done

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__events__end__of__record_1ga5b19c9f115943bcb15f8a40ccefd46ff.html language=enus -->
## TOPIC 00027: NIRFSA_ATTR_END_OF_RECORD_EVENT_TERMINAL_NAME

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__events__end__of__record_1ga5b19c9f115943bcb15f8a40ccefd46ff.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__events__end__of__record_1ga5b19c9f115943bcb15f8a40ccefd46ff.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the fully qualified signal name as a string. SyntaxNIRFSA_ATTR_END_OF_RECORD_EVENT_TERMINAL_NAMENumeric ValueData TypeAccessApplies To1150120ViStringRead-OnlyN/ARemarksDefault Values:PXIe-5830/5831/5832: /BasebandModule/ai/0/EndOfRecordEvent, where BasebandModule is the name of the baseband

### NIRFSA_ATTR_END_OF_RECORD_EVENT_TERMINAL_NAME

Returns the fully qualified signal name as a string.

#### Syntax

NIRFSA_ATTR_END_OF_RECORD_EVENT_TERMINAL_NAME

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150120 | ViString | Read-Only | N/A |

#### Remarks

**Default Values**:

**PXIe-5830/5831/5832**: /*BasebandModule*/*ai*/0/*EndOfRecordEvent*, where *BasebandModule* is the name of the baseband module of your device in MAX.

**PXIe-5820/5840/5841/5842**: /*ModuleName*/*ai*/0/*EndOfRecordEvent*, where *ModuleName* is the name of your device in MAX.

**PXIe-5860**: /*ModuleName*/*ai*/*ChannelNumber*/*EndOfRecordEvent*, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

**All other devices**: /*DigitizerName*/*EndOfRecordEvent*, where *DigitizerName* is the name associated with your digitizer module in MAX.

**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Events](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html)

**High-Level Functions**:

- [niRFSA_GetTerminalName](group____root__ni_r_f_s_a__functions__configuration_1ga3e68e092f0621f1855ca7e753df47526.html)

Parent topic:

End Of Record

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__events__end__of__record_1gac10d77342bf81891451e078d3cf56f1a.html language=enus -->
## TOPIC 00028: NIRFSA_ATTR_EXPORTED_END_OF_RECORD_EVENT_OUTPUT_TERMINAL

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__events__end__of__record_1gac10d77342bf81891451e078d3cf56f1a.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__events__end__of__record_1gac10d77342bf81891451e078d3cf56f1a.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for the End of Record Event. SyntaxNIRFSA_ATTR_EXPORTED_END_OF_RECORD_EVENT_OUTPUT_TERMINALNumeric ValueData TypeAccessApplies To1150044ViStringRead/WriteN/ARemarksDefined Values:NameValueDescriptionNIRFSA_VAL_CLK_OUT_STRClkOutExport the clock on the CLK OUT termin

### NIRFSA_ATTR_EXPORTED_END_OF_RECORD_EVENT_OUTPUT_TERMINAL

Specifies the destination terminal for the End of Record Event.

#### Syntax

NIRFSA_ATTR_EXPORTED_END_OF_RECORD_EVENT_OUTPUT_TERMINAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150044 | ViString | Read/Write | N/A |

#### Remarks

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIRFSA_VAL_CLK_OUT_STR | ClkOut | Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841. |
| NIRFSA_VAL_DO_NOT_EXPORT_STR |  | The signal is not exported. |
| NIRFSA_VAL_PFI0_STR | PFI0 | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0. |
| NIRFSA_VAL_PFI1_STR | PFI1 | The trigger is received on PFI 1. |
| NIRFSA_VAL_PXI_STAR_STR | PXI_STAR | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646. |
| NIRFSA_VAL_PXI_TRIG0_STR | PXI_Trig0 | The trigger is received on PXI trigger line 0. |
| NIRFSA_VAL_PXI_TRIG1_STR | PXI_Trig1 | The trigger is received on PXI trigger line 1. |
| NIRFSA_VAL_PXI_TRIG2_STR | PXI_Trig2 | The trigger is received on PXI trigger line 2. |
| NIRFSA_VAL_PXI_TRIG3_STR | PXI_Trig3 | The trigger is received on PXI trigger line 3. |
| NIRFSA_VAL_PXI_TRIG4_STR | PXI_Trig4 | The trigger is received on PXI trigger line 4. |
| NIRFSA_VAL_PXI_TRIG5_STR | PXI_Trig5 | The trigger is received on PXI trigger line 5. |
| NIRFSA_VAL_PXI_TRIG6_STR | PXI_Trig6 | The trigger is received on PXI trigger line 6. |
| NIRFSA_VAL_PXI_TRIG7_STR | PXI_Trig7 | The trigger is received on PXI trigger line 7. |
| NIRFSA_VAL_PXIE_DSTARC_STR | PXIe_DStarC | The trigger is received on the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841. |
| NIRFSA_VAL_REF_OUT_STR | RefOut | Export the clock on the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, PXIe-5694, or PXIe-5820/5830/5831/5832/5840/5841. |
| NIRFSA_VAL_REF_OUT2_STR | RefOut2 | Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E. |
| NIRFSA_VAL_DIO_PFI0_STR | DIO/PFI0 | The trigger is received on PFI0 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI1_STR | DIO/PFI1 | The trigger is received on PFI1 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI2_STR | DIO/PFI2 | The trigger is received on PFI2 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI3_STR | DIO/PFI3 | The trigger is received on PFI3 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI4_STR | DIO/PFI4 | The trigger is received on PFI4 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI5_STR | DIO/PFI5 | The trigger is received on PFI5 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI6_STR | DIO/PFI6 | The trigger is received on PFI6 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI7_STR | DIO/PFI7 | The trigger is received on PFI7 from the front panel DIO terminal. |

**Default Value**: "" (empty string)

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Triggers](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html)

[Events](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html)

[Signal Routing](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/signal-routing.html)

**High-Level Functions**:

- [niRFSA_ExportSignal](group____root__ni_r_f_s_a__functions__configuration__clock_1gaa0e7acfa202c06fb09bdf610d8a613eb.html)

Parent topic:

End Of Record

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__events__ready__for__advance.html language=enus -->
## TOPIC 00029: Ready For Advance

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__events__ready__for__advance.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__events__ready__for__advance.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIRFSA_ATTR_EXPORTED_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINALSpecifies the destination terminal for the Ready for Advance Event. NIRFSA_ATTR_READY_FOR_ADVANCE_EVENT_TERMINAL_NAMEReturns the fully qualified signal name as a string. AttachmentsNone

### Ready For Advance

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIRFSA_ATTR_EXPORTED_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL | Specifies the destination terminal for the Ready for Advance Event. |
| NIRFSA_ATTR_READY_FOR_ADVANCE_EVENT_TERMINAL_NAME | Returns the fully qualified signal name as a string. |

#### Attachments

None

Parent topic:

Events

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__events__ready__for__ref.html language=enus -->
## TOPIC 00030: Ready For Ref

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__events__ready__for__ref.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__events__ready__for__ref.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIRFSA_ATTR_EXPORTED_READY_FOR_REF_EVENT_OUTPUT_TERMINALSpecifies the destination terminal for the Ready for Reference Event. NIRFSA_ATTR_READY_FOR_REF_EVENT_TERMINAL_NAMEReturns the fully qualified signal name as a string. AttachmentsNone

### Ready For Ref

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIRFSA_ATTR_EXPORTED_READY_FOR_REF_EVENT_OUTPUT_TERMINAL | Specifies the destination terminal for the Ready for Reference Event. |
| NIRFSA_ATTR_READY_FOR_REF_EVENT_TERMINAL_NAME | Returns the fully qualified signal name as a string. |

#### Attachments

None

Parent topic:

Events

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__events__ready__for__ref_1ga4c60bed8cf97082627b8ab53c4b797e4.html language=enus -->
## TOPIC 00031: NIRFSA_ATTR_EXPORTED_READY_FOR_REF_EVENT_OUTPUT_TERMINAL

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__events__ready__for__ref_1ga4c60bed8cf97082627b8ab53c4b797e4.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__events__ready__for__ref_1ga4c60bed8cf97082627b8ab53c4b797e4.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for the Ready for Reference Event. SyntaxNIRFSA_ATTR_EXPORTED_READY_FOR_REF_EVENT_OUTPUT_TERMINALNumeric ValueData TypeAccessApplies To1150043ViStringRead/WriteN/ARemarksValueDescriptionNIRFSA_VAL_DO_NOT_EXPORT_STR ("")The signal is not exported.NIRFSA_VAL_CLK_OUT_

### NIRFSA_ATTR_EXPORTED_READY_FOR_REF_EVENT_OUTPUT_TERMINAL

Specifies the destination terminal for the Ready for Reference Event.

#### Syntax

NIRFSA_ATTR_EXPORTED_READY_FOR_REF_EVENT_OUTPUT_TERMINAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150043 | ViString | Read/Write | N/A |

#### Remarks

| Value | Description |
| --- | --- |
| NIRFSA_VAL_DO_NOT_EXPORT_STR ("") | The signal is not exported. |
| NIRFSA_VAL_CLK_OUT_STR ("ClkOut") | The signal is exported to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| NIRFSA_VAL_REF_OUT_STR ("RefOut") | The signal is exported to the REF IN/OUT terminal on the PXI/PXIe-5652 and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841. |
| NIRFSA_VAL_REF_OUT2_STR ("RefOut2") | The signal is exported to the REF OUT2 terminal on the LO. This connector exists on only the PXIe-5652. |
| NIRFSA_VAL_PFI0_STR ("PFI0") | The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0. |
| NIRFSA_VAL_PFI1_STR ("PFI1") | The signal is exported to the PFI 1 connector on the PXI-5142 and PXIe-5622. |
| NIRFSA_VAL_PXI_TRIG0_STR ("PXI_Trig0") | The signal is exported to the PXI trigger line 0. |
| NIRFSA_VAL_PXI_TRIG1_STR ("PXI_Trig1") | The signal is exported to the PXI trigger line 1. |
| NIRFSA_VAL_PXI_TRIG2_STR ("PXI_Trig2") | The signal is exported to the PXI trigger line 2. |
| NIRFSA_VAL_PXI_TRIG3_STR ("PXI_Trig3") | The signal is exported to the PXI trigger line 3. |
| NIRFSA_VAL_PXI_TRIG4_STR ("PXI_Trig4") | The signal is exported to the PXI trigger line 4. |
| NIRFSA_VAL_PXI_TRIG5_STR ("PXI_Trig5") | The signal is exported to the PXI trigger line 5. |
| NIRFSA_VAL_PXI_TRIG6_STR ("PXI_Trig6") | The signal is exported to the PXI trigger line 6. |
| NIRFSA_VAL_PXI_TRIG7_STR ("PXI_Trig7") | The signal is exported to the PXI trigger line 7. |
| NIRFSA_VAL_PXI_STAR_STR ("PXI_Star") | The signal is exported to the PXI star trigger line. |
| NIRFSA_VAL_PXIE_DSTARC_STR ("PXIe_DStarC") | The trigger is received on the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841. |
| NIRFSA_VAL_DIO_PFI0_STR ("DIO/PFI0") | The trigger is received on PFI0 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI1_STR("DIO/PFI1") | The trigger is received on PFI1 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI2_STR ("DIO/PFI2") | The trigger is received on PFI2 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI3_STR ("DIO/PFI3") | The trigger is received on PFI3 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI4_STR ("DIO/PFI4") | The trigger is received on PFI4 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI5_STR ("DIO/PFI5") | The trigger is received on PFI5 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI6_STR ("DIO/PFI6") | The trigger is received on PFI6 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI7_STR ("DIO/PFI7") | The trigger is received on PFI7 from the front panel DIO terminal. |

**Default Value**: "" (empty string)

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**High-Level Functions**:

- [niRFSA_ExportSignal](group____root__ni_r_f_s_a__functions__configuration__clock_1gaa0e7acfa202c06fb09bdf610d8a613eb.html)

Parent topic:

Ready For Ref

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__events__user__source_1ga6ce141410f57b60f0ae0eab5240dd4a1.html language=enus -->
## TOPIC 00032: NIRFSA_ATTR_USER_SOURCE_PULSE_WIDTH_UNITS

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__events__user__source_1ga6ce141410f57b60f0ae0eab5240dd4a1.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__events__user__source_1ga6ce141410f57b60f0ae0eab5240dd4a1.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse width units for the User Source. SyntaxNIRFSA_ATTR_USER_SOURCE_PULSE_WIDTH_UNITSNumeric ValueData TypeAccessApplies To1150321ViInt32Read/WriteN/ARemarks When the value is NIRFSA_VAL_PULSE_WIDTH_UNITS_SECONDS, it is assumed that the clock rate of the signal is the data clock. Use

### NIRFSA_ATTR_USER_SOURCE_PULSE_WIDTH_UNITS

Specifies the pulse width units for the User Source.

#### Syntax

NIRFSA_ATTR_USER_SOURCE_PULSE_WIDTH_UNITS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150321 | ViInt32 | Read/Write | N/A |

#### Remarks

When the value is **NIRFSA_VAL_PULSE_WIDTH_UNITS_SECONDS**, it is assumed that the clock rate of the signal is the data clock. Use **NIRFSA_VAL_PULSE_WIDTH_UNITS_CLOCK_PERIODS** if the user source clock rate is anything else.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIRFSA_VAL_PULSE_WIDTH_UNITS_CLOCK_PERIODS | 6201 (0x1839) | Units are clock periods. |
| NIRFSA_VAL_PULSE_WIDTH_UNITS_SECONDS | 6200 (0x1838) | Units are seconds. |

**Default Value**: **NIRFSA_VAL_PULSE_WIDTH_UNITS_SECONDS**

**Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

Parent topic:

User Source

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__external__alignment.html language=enus -->
## TOPIC 00033: External Alignment

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__external__alignment.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__external__alignment.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNI 5665/5668RGroup membersNoneAttachmentsNone

### External Alignment

#### Groups

- NI 5665/5668R

#### Group members

None

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__external__alignment__ni__56655668r.html language=enus -->
## TOPIC 00034: NI 5665/5668R

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__external__alignment__ni__56655668r.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__external__alignment__ni__56655668r.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIRFSA_ATTR_5665_PRESELECTOR_TUNING_DAC_VALUESpecifies the preselector tuning DAC value during the preselector external alignment step. AttachmentsNone

### NI 5665/5668R

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIRFSA_ATTR_5665_PRESELECTOR_TUNING_DAC_VALUE | Specifies the preselector tuning DAC value during the preselector external alignment step. |

#### Attachments

None

Parent topic:

External Alignment

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__factory__calibration__ni__56655668r_1ga06950dde98379db38c288e6f8503944c.html language=enus -->
## TOPIC 00035: NIRFSA_ATTR_CAL_IF_ATTENUATION_INDEX

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__factory__calibration__ni__56655668r_1ga06950dde98379db38c288e6f8503944c.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__factory__calibration__ni__56655668r_1ga06950dde98379db38c288e6f8503944c.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the IF attenuation index from a table of valid settings. SyntaxNIRFSA_ATTR_CAL_IF_ATTENUATION_INDEXNumeric ValueData TypeAccessApplies To1150109ViInt32Read/WriteN/ARemarks To select a correct attenuation table, set this attribute in conjunction with the NIRFSA_ATTR_CAL_IF_FILTER_SELECTION

### NIRFSA_ATTR_CAL_IF_ATTENUATION_INDEX

Specifies the IF attenuation index from a table of valid settings.

#### Syntax

NIRFSA_ATTR_CAL_IF_ATTENUATION_INDEX

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150109 | ViInt32 | Read/Write | N/A |

#### Remarks

To select a correct attenuation table, set this attribute in conjunction with the [NIRFSA_ATTR_CAL_IF_FILTER_SELECTION](group____root__ni_r_f_s_a__attributes__factory__calibration__ni__56655668r_1ga9f934dde97c8f010e28927630820ca01.html) attribute. This attribute is valid only during a calibration session.

**Valid Values**: 0 to 25

**Default Value**: 0

**Supported Devices:** PXIe-5694

Parent topic:

NI 5665/5668R

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__factory__calibration__ni__56655668r_1ga53bdbb2f58ddeda05b3dba09ac834d44.html language=enus -->
## TOPIC 00036: NIRFSA_ATTR_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_SELECTION

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__factory__calibration__ni__56655668r_1ga53bdbb2f58ddeda05b3dba09ac834d44.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__factory__calibration__ni__56655668r_1ga53bdbb2f58ddeda05b3dba09ac834d44.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the RF lowband signal conditioning path. SyntaxNIRFSA_ATTR_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_SELECTIONNumeric ValueData TypeAccessApplies To1150215ViInt32Read/WriteN/ARemarksValid Values:NIRFSA_VAL_EXT_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_1NIRFSA_VAL_EXT_CAL_RF_LOWBAND_SIGNAL_COND

### NIRFSA_ATTR_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_SELECTION

Specifies the RF lowband signal conditioning path.

#### Syntax

NIRFSA_ATTR_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_SELECTION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150215 | ViInt32 | Read/Write | N/A |

#### Remarks

**Valid Values**:

**NIRFSA_VAL_EXT_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_1**

**NIRFSA_VAL_EXT_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_2**

**Default Value**: **NIRFSA_VAL_EXT_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_1**

**Supported Devices**: PXIe-5606

Parent topic:

NI 5665/5668R

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__factory__calibration__ni__56655668r_1ga9f934dde97c8f010e28927630820ca01.html language=enus -->
## TOPIC 00037: NIRFSA_ATTR_CAL_IF_FILTER_SELECTION

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__factory__calibration__ni__56655668r_1ga9f934dde97c8f010e28927630820ca01.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__factory__calibration__ni__56655668r_1ga9f934dde97c8f010e28927630820ca01.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the IF filter path during calibration. SyntaxNIRFSA_ATTR_CAL_IF_FILTER_SELECTIONNumeric ValueData TypeAccessApplies To1150112ViInt32Read/WriteN/ARemarks The attribute is valid only during a calibration session.Defined Values:NameValueDescriptionNIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_12100 (0x83

### NIRFSA_ATTR_CAL_IF_FILTER_SELECTION

Specifies the IF filter path during calibration.

#### Syntax

NIRFSA_ATTR_CAL_IF_FILTER_SELECTION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150112 | ViInt32 | Read/Write | N/A |

#### Remarks

The attribute is valid only during a calibration session.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_1 | 2100 (0x834) | Specifies that the 5 MHz filter path is used during calibration. |
| NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_2 | 2101 (0x835) | Specifies that the 300 kHz filter path is used during calibration. Not supported for the PXIe-5694. |
| NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_3 | 2102 (0x836) | None of the IF filter paths are used during calibration. |
| NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_4 | 2103 (0x837) | Specifies that the 20 MHz filter path is used during calibration. |
| NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_5 | 2104 (0x838) | Specifies that the 1.4 MHz filter path is used during calibration. |
| NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_6 | 2105 (0x839) | Specifies that the 400 kHz filter path is used during calibration. |
| NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_7 | 2106 (0x83a) | Specifies that the 110 kHz filter path is used during calibration. |
| NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_8 | 2107 (0x83b) | Specifies that the 30 kHz filter path is used during calibration. |

**Default Value**: **NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_4**

**Supported Devices**: PXIe-5694

Parent topic:

NI 5665/5668R

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__factory__calibration__ni__56655668r_1gaedee054aa121fc62fffb6d73f667a264.html language=enus -->
## TOPIC 00038: NIRFSA_ATTR_CAL_LO3_ATTENUATION

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__factory__calibration__ni__56655668r_1gaedee054aa121fc62fffb6d73f667a264.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__factory__calibration__ni__56655668r_1gaedee054aa121fc62fffb6d73f667a264.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the LO3 attenuation, in dB, during a calibration session. This attribute is valid only during a calibration session. SyntaxNIRFSA_ATTR_CAL_LO3_ATTENUATIONNumeric ValueData TypeAccessApplies To1150116ViReal64Read/WriteN/ARemarksValid Values and Default Values:DeviceValid ValuesDefault Value

### NIRFSA_ATTR_CAL_LO3_ATTENUATION

Specifies the LO3 attenuation, in dB, during a calibration session. This attribute is valid only during a calibration session.

#### Syntax

NIRFSA_ATTR_CAL_LO3_ATTENUATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150116 | ViReal64 | Read/Write | N/A |

#### Remarks

**Valid Values and Default Values**:

| Device | Valid Values | Default Value |
| --- | --- | --- |
| PXIe-5603/5605 | 0 to 15.5 | 15.5 |
| PXIe-5606 | 0 to 31 | 31 |

**Supported Devices**: PXIe-5603/5605/5606

Parent topic:

NI 5665/5668R

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__inherent__ivi__attributes.html language=enus -->
## TOPIC 00039: Inherent IVI Attributes

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__inherent__ivi__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__inherent__ivi__attributes.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdvanced Session InformationDriver CapabilitiesDriver IdentificationInstrument IdentificationUser OptionsGroup membersNoneAttachmentsNone

### Inherent IVI Attributes

#### Groups

- Advanced Session Information
- Driver Capabilities
- Driver Identification
- Instrument Identification
- User Options

#### Group members

None

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__inherent__ivi__attributes__advanced__session__information.html language=enus -->
## TOPIC 00040: Advanced Session Information

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__inherent__ivi__attributes__advanced__session__information.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__inherent__ivi__attributes__advanced__session__information.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIRFSA_ATTR_IO_RESOURCE_DESCRIPTORIndicates the resource name NI-RFSA uses to identify the physical device. NIRFSA_ATTR_LOGICAL_NAMEContains the logical name you specified when opening the current IVI session. AttachmentsNone

### Advanced Session Information

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIRFSA_ATTR_IO_RESOURCE_DESCRIPTOR | Indicates the resource name NI-RFSA uses to identify the physical device. |
| NIRFSA_ATTR_LOGICAL_NAME | Contains the logical name you specified when opening the current IVI session. |

#### Attachments

None

Parent topic:

Inherent IVI Attributes

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__inherent__ivi__attributes__driver__capabilities.html language=enus -->
## TOPIC 00041: Driver Capabilities

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__inherent__ivi__attributes__driver__capabilities.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__inherent__ivi__attributes__driver__capabilities.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIRFSA_ATTR_SUPPORTED_INSTRUMENT_MODELSReturns a comma-separated list of supported devices. AttachmentsNone

### Driver Capabilities

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIRFSA_ATTR_SUPPORTED_INSTRUMENT_MODELS | Returns a comma-separated list of supported devices. |

#### Attachments

None

Parent topic:

Inherent IVI Attributes

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__inherent__ivi__attributes__driver__identification_1gaec092d0b2e8f8e6a14392e4afb33cb6d.html language=enus -->
## TOPIC 00042: NIRFSA_ATTR_SPECIFIC_DRIVER_VENDOR

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__inherent__ivi__attributes__driver__identification_1gaec092d0b2e8f8e6a14392e4afb33cb6d.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__inherent__ivi__attributes__driver__identification_1gaec092d0b2e8f8e6a14392e4afb33cb6d.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string that contains the name of the vendor that supplies NI-RFSA. SyntaxNIRFSA_ATTR_SPECIFIC_DRIVER_VENDORNumeric ValueData TypeAccessApplies To1050513ViStringRead-OnlyN/ARemarks This attribute returnsNational Instruments.Default Value: N/ASupported Devices: PXI-5600, PXIe-5601/5603/5605/

### NIRFSA_ATTR_SPECIFIC_DRIVER_VENDOR

Returns a string that contains the name of the vendor that supplies NI-RFSA.

#### Syntax

NIRFSA_ATTR_SPECIFIC_DRIVER_VENDOR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050513 | ViString | Read-Only | N/A |

#### Remarks

This attribute returns

National Instruments.

**Default Value**: N/A

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

Parent topic:

Driver Identification

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__inherent__ivi__attributes__instrument__identification_1ga8d47b4a2696a0538835daabb2d5407fc.html language=enus -->
## TOPIC 00043: NIRFSA_ATTR_INSTRUMENT_FIRMWARE_REVISION

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__inherent__ivi__attributes__instrument__identification_1ga8d47b4a2696a0538835daabb2d5407fc.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__inherent__ivi__attributes__instrument__identification_1ga8d47b4a2696a0538835daabb2d5407fc.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string that contains the firmware revision information for the NI-RFSA downconverter for the composite device you are currently using. SyntaxNIRFSA_ATTR_INSTRUMENT_FIRMWARE_REVISIONNumeric ValueData TypeAccessApplies To1050510ViStringRead-OnlyN/ARemarksDefault Value: N/ASupported Devices:

### NIRFSA_ATTR_INSTRUMENT_FIRMWARE_REVISION

Returns a string that contains the firmware revision information for the NI-RFSA downconverter for the composite device you are currently using.

#### Syntax

NIRFSA_ATTR_INSTRUMENT_FIRMWARE_REVISION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050510 | ViString | Read-Only | N/A |

#### Remarks

**Default Value**: N/A

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

Note

PXIe-5820/5830/5831/5832/5840/5841/5842/5860 devices will return "No revision information available." To retrieve the firmware revision, use MAX, Hardware Configuration Utility, or NI System Configuration API.

Parent topic:

Instrument Identification

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__inherent__ivi__attributes__user__options_1ga6251fd83d016c4d8079eaa44a7236baa.html language=enus -->
## TOPIC 00044: NIRFSA_ATTR_CACHE

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__inherent__ivi__attributes__user__options_1ga6251fd83d016c4d8079eaa44a7236baa.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__inherent__ivi__attributes__user__options_1ga6251fd83d016c4d8079eaa44a7236baa.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to cache the value of attributes. SyntaxNIRFSA_ATTR_CACHENumeric ValueData TypeAccessApplies To1050004ViBooleanRead/WriteN/ARemarks If you set this attribute to VI_TRUE, NI-RFSA tracks the current NI-RFSA device settings and avoids sending redundant commands to the device.NI-RFSA c

### NIRFSA_ATTR_CACHE

Specifies whether to cache the value of attributes.

#### Syntax

NIRFSA_ATTR_CACHE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050004 | ViBoolean | Read/Write | N/A |

#### Remarks

If you set this attribute to VI_TRUE, NI-RFSA tracks the current NI-RFSA device settings and avoids sending redundant commands to the device.

NI-RFSA can always cache or never cache particular attributes, regardless of the setting of this attribute.

Use the [niRFSA_InitWithOptions](group____root__ni_r_f_s_a__functions_1ga790a63d6ecd99ed7842f52d1044e53cc.html) function to override the default value.

**Defined Values:**

| Value | Description |
| --- | --- |
| VI_TRUE | Caching is enabled. |
| VI_FALSE | Caching is disabled. |

**Default Value**: VI_TRUE

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

Parent topic:

User Options

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__inherent__ivi__attributes__user__options_1gabd4a86661347ffa3ecc81a39b8d260bb.html language=enus -->
## TOPIC 00045: NIRFSA_ATTR_RANGE_CHECK

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__inherent__ivi__attributes__user__options_1gabd4a86661347ffa3ecc81a39b8d260bb.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__inherent__ivi__attributes__user__options_1gabd4a86661347ffa3ecc81a39b8d260bb.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to validate attribute values and function parameters. SyntaxNIRFSA_ATTR_RANGE_CHECKNumeric ValueData TypeAccessApplies To1050002ViBooleanRead/WriteN/ARemarks If enabled, NI-RFSA validates the parameter values that you pass to NI-RFSA functions. Range checking parameters is very use

### NIRFSA_ATTR_RANGE_CHECK

Specifies whether to validate attribute values and function parameters.

#### Syntax

NIRFSA_ATTR_RANGE_CHECK

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050002 | ViBoolean | Read/Write | N/A |

#### Remarks

If enabled, NI-RFSA validates the parameter values that you pass to NI-RFSA functions. Range checking parameters is very useful for debugging. After you validate your program, you can set this attribute to VI_FALSE to disable range checking and maximize performance.

Note

Use the [niRFSA_InitWithOptions](group____root__ni_r_f_s_a__functions_1ga790a63d6ecd99ed7842f52d1044e53cc.html) function to override this value.

**Defined Values:**

| Value | Description |
| --- | --- |
| VI_TRUE | NI-RFSA validates attribute values and function parameters. |
| VI_FALSE | NI-RFSA does not validate attribute values and function parameters. |

**Default Value**: VI_TRUE

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

Parent topic:

User Options

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__inherent__ivi__attributes__user__options_1gafc25b04f1901b7178ded063bf480d74e.html language=enus -->
## TOPIC 00046: NIRFSA_ATTR_INTERCHANGE_CHECK

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__inherent__ivi__attributes__user__options_1gafc25b04f1901b7178ded063bf480d74e.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__inherent__ivi__attributes__user__options_1gafc25b04f1901b7178ded063bf480d74e.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to perform interchangeability checking and retrieve interchangeability warnings. SyntaxNIRFSA_ATTR_INTERCHANGE_CHECKNumeric ValueData TypeAccessApplies To1050021ViBooleanRead/WriteN/ARemarksInterchangeability check is unsupported.Defined Values:ValueDescriptionVI_TRUENI-RFSA perfor

### NIRFSA_ATTR_INTERCHANGE_CHECK

Specifies whether to perform interchangeability checking and retrieve interchangeability warnings.

#### Syntax

NIRFSA_ATTR_INTERCHANGE_CHECK

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050021 | ViBoolean | Read/Write | N/A |

#### Remarks

Note

Interchangeability check is unsupported.

**Defined Values:**

| Value | Description |
| --- | --- |
| VI_TRUE | NI-RFSA performs interchangeability-checking and retrieves warnings. |
| VI_FALSE | NI-RFSA does not perform interchangeability-checking or retrieve warnings. |

**Default Value**: VI_FALSE

**Supported Devices**: None

Parent topic:

User Options

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__load__configurations_1ga10ae80eef44d648fbbd6ff39c42c3756.html language=enus -->
## TOPIC 00047: NIRFSA_ATTR_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__load__configurations_1ga10ae80eef44d648fbbd6ff39c42c3756.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__load__configurations_1ga10ae80eef44d648fbbd6ff39c42c3756.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the configurations to skip to reset while loading configurations from a file. SyntaxNIRFSA_ATTR_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONSNumeric ValueData TypeAccessApplies To1150337ViInt32Read/WriteN/ARemarksDefined Values:NameValueDescriptionNIRFSA_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RES

### NIRFSA_ATTR_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS

Specifies the configurations to skip to reset while loading configurations from a file.

#### Syntax

NIRFSA_ATTR_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150337 | ViInt32 | Read/Write | N/A |

#### Remarks

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIRFSA_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_DEEMBEDDING_TABLES | 2 (0x2) | NI-RFSA skips resetting the de-embedding tables. |
| NIRFSA_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_NONE | 0 (0x0) | NI-RFSA resets all configurations. |

**Default Value:****NIRFSA_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_NONE****Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

Parent topic:

Load Configurations

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__peertopeer.html language=enus -->
## TOPIC 00048: Peer-to-Peer

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__peertopeer.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__peertopeer.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIRFSA_ATTR_P2P_ENABLEDSpecifies whether peer-to-peer streaming is enabled for the active stream endpoint. NIRFSA_ATTR_P2P_ENDPOINT_OVERFLOWIndicates whether the endpoint has overflowed. NIRFSA_ATTR_P2P_ENDPOINT_SIZEReturns the size, in samples, of the peer-to-p

### Peer-to-Peer

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIRFSA_ATTR_P2P_ENABLED | Specifies whether peer-to-peer streaming is enabled for the active stream endpoint. |
| NIRFSA_ATTR_P2P_ENDPOINT_OVERFLOW | Indicates whether the endpoint has overflowed. |
| NIRFSA_ATTR_P2P_ENDPOINT_SIZE | Returns the size, in samples, of the peer-to-peer endpoint. |
| NIRFSA_ATTR_P2P_FIFO_ENDPOINT_COUNT | Returns the number of peer-to-peer streams supported by the device. |
| NIRFSA_ATTR_P2P_MOST_SAMPLES_AVAILABLE_IN_ENDPOINT | Returns the largest number of complex samples available in the peer-to-peer endpoint since this attribute was last read. |
| NIRFSA_ATTR_P2P_ONBOARD_MEMORY_ENABLED | Specifies whether a limit is placed on the number of records and the size of the records by the size of the device onboard memory. |
| NIRFSA_ATTR_P2P_SAMPLES_AVAILABLE_IN_ENDPOINT | Returns the current number of complex samples available in the peer-to-peer endpoint. |
| NIRFSA_ATTR_P2P_SAMPLES_TRANSFERRED | Returns the number of complex samples transferred through the peer-to-peer stream endpoint since the endpoint was last reset. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__peertopeer_1gaeeaa32331f99ec292e9173c176c9fad8.html language=enus -->
## TOPIC 00049: NIRFSA_ATTR_P2P_ONBOARD_MEMORY_ENABLED

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__peertopeer_1gaeeaa32331f99ec292e9173c176c9fad8.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__peertopeer_1gaeeaa32331f99ec292e9173c176c9fad8.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether a limit is placed on the number of records and the size of the records by the size of the device onboard memory. SyntaxNIRFSA_ATTR_P2P_ONBOARD_MEMORY_ENABLEDNumeric ValueData TypeAccessApplies To1150107ViBooleanRead/WriteN/ARemarks When a peer-to-peer stream is enabled and onboard

### NIRFSA_ATTR_P2P_ONBOARD_MEMORY_ENABLED

Specifies whether a limit is placed on the number of records and the size of the records by the size of the device onboard memory.

#### Syntax

NIRFSA_ATTR_P2P_ONBOARD_MEMORY_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150107 | ViBoolean | Read/Write | N/A |

#### Remarks

When a peer-to-peer stream is enabled and onboard memory is disabled, any fetch calls result in an error.

**Default Value**: VI_FALSE

**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

Parent topic:

Peer-to-Peer

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__self__calibration_1ga6f75a321276ea6e6790614dd4e745236.html language=enus -->
## TOPIC 00050: NIRFSA_ATTR_RF_CONDITIONING_CAL_TONE_MODE

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__self__calibration_1ga6f75a321276ea6e6790614dd4e745236.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__self__calibration_1ga6f75a321276ea6e6790614dd4e745236.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the location in a signal path where an RF conditioning calibration tone is injected or whether the tone is disabled. SyntaxNIRFSA_ATTR_RF_CONDITIONING_CAL_TONE_MODENumeric ValueData TypeAccessApplies To1150208ViInt32Read/WriteN/ARemarksDefined Values:NameValueDescriptionNIRFSA_VAL_DISABLED

### NIRFSA_ATTR_RF_CONDITIONING_CAL_TONE_MODE

Specifies the location in a signal path where an RF conditioning calibration tone is injected or whether the tone is disabled.

#### Syntax

NIRFSA_ATTR_RF_CONDITIONING_CAL_TONE_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150208 | ViInt32 | Read/Write | N/A |

#### Remarks

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIRFSA_VAL_DISABLED | 1900 (0x76c) | Disables the calibration tone for the associated signal path. |
| NIRFSA_VAL_CAL_TONE_HIGHBAND_RF | 2702 (0xa8e) | Injects the calibration tone into the high band RF signal path. |
| NIRFSA_VAL_CAL_TONE_LOWBAND_RF | 2701 (0xa8d) | Injects the calibration tone into the low band RF signal path. |

**Default Value**: **NIRFSA_VAL_DISABLED**

**Supported Devices**: PXIe-5667, PXIe-5693/5698

Parent topic:

Self Calibration

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__self__calibration_1gab77b80fee67ab68e6b59dd1dd998b5a0.html language=enus -->
## TOPIC 00051: NIRFSA_ATTR_CAL_DIGITIZER_ID

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__self__calibration_1gab77b80fee67ab68e6b59dd1dd998b5a0.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__self__calibration_1gab77b80fee67ab68e6b59dd1dd998b5a0.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the currently associated digitizer ID. SyntaxNIRFSA_ATTR_CAL_DIGITIZER_IDNumeric ValueData TypeAccessApplies To1150226ViStringRead/WriteN/ARemarks Allows the use of self calibration data when configured in external digitizer mode.Default Value: "" (empty string) in external digitizer modeSup

### NIRFSA_ATTR_CAL_DIGITIZER_ID

Returns the currently associated digitizer ID.

#### Syntax

NIRFSA_ATTR_CAL_DIGITIZER_ID

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150226 | ViString | Read/Write | N/A |

#### Remarks

Allows the use of self calibration data when configured in external digitizer mode.

**Default Value**: "" (empty string) in external digitizer mode

**Supported Devices**: PXIe-5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668

Parent topic:

Self Calibration

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__self__calibration__ni__56655668r_1ga3cce432be8cbe79f53a1d8ece4e84726.html language=enus -->
## TOPIC 00052: NIRFSA_ATTR_CALIBRATION_CORRECTION_765_MHZ_FILTER

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__self__calibration__ni__56655668r_1ga3cce432be8cbe79f53a1d8ece4e84726.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__self__calibration__ni__56655668r_1ga3cce432be8cbe79f53a1d8ece4e84726.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the internal gain self-calibration correction for the 765 MHz IF filter path. SyntaxNIRFSA_ATTR_CALIBRATION_CORRECTION_765_MHZ_FILTERNumeric ValueData TypeAccessApplies To1150225ViReal64Read/WriteN/ARemarks The value you specify using this attribute overrides any previously-set value.Units

### NIRFSA_ATTR_CALIBRATION_CORRECTION_765_MHZ_FILTER

Specifies the internal gain self-calibration correction for the 765 MHz IF filter path.

#### Syntax

NIRFSA_ATTR_CALIBRATION_CORRECTION_765_MHZ_FILTER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150225 | ViReal64 | Read/Write | N/A |

#### Remarks

The value you specify using this attribute overrides any previously-set value.

**Units**: dB

**Default Value**: 0

**Supported Devices**: PXIe-5606

Parent topic:

NI 5665/5668R

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__self__calibration__ni__56655668r_1ga693f2e643081096e5b16cf73d18de8c3.html language=enus -->
## TOPIC 00053: NIRFSA_ATTR_CALIBRATION_CORRECTION_300_KHZ_FILTER

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__self__calibration__ni__56655668r_1ga693f2e643081096e5b16cf73d18de8c3.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__self__calibration__ni__56655668r_1ga693f2e643081096e5b16cf73d18de8c3.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the internal gain self-calibration correction for the 300 kHz IF filter path. SyntaxNIRFSA_ATTR_CALIBRATION_CORRECTION_300_KHZ_FILTERNumeric ValueData TypeAccessApplies To1150147ViReal64Read/WriteN/ARemarks The value you specify using this attribute overrides any previously-set value.Units

### NIRFSA_ATTR_CALIBRATION_CORRECTION_300_KHZ_FILTER

Specifies the internal gain self-calibration correction for the 300 kHz IF filter path.

#### Syntax

NIRFSA_ATTR_CALIBRATION_CORRECTION_300_KHZ_FILTER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150147 | ViReal64 | Read/Write | N/A |

#### Remarks

The value you specify using this attribute overrides any previously-set value.

**Units**: dB

**Default Value**: 0

**Supported Devices**: PXIe-5603/5605/5606

Parent topic:

NI 5665/5668R

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__self__calibration__ni__56655668r_1ga7104900c06134aa9533660752c185f93.html language=enus -->
## TOPIC 00054: NIRFSA_ATTR_CALIBRATION_CORRECTION_320_MHZ_FILTER

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__self__calibration__ni__56655668r_1ga7104900c06134aa9533660752c185f93.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__self__calibration__ni__56655668r_1ga7104900c06134aa9533660752c185f93.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the internal gain self-calibration correction for the 320 MHz IF filter path. SyntaxNIRFSA_ATTR_CALIBRATION_CORRECTION_320_MHZ_FILTERNumeric ValueData TypeAccessApplies To1150224ViReal64Read/WriteN/ARemarks The value you specify using this attribute overrides any previously-set value.Units

### NIRFSA_ATTR_CALIBRATION_CORRECTION_320_MHZ_FILTER

Specifies the internal gain self-calibration correction for the 320 MHz IF filter path.

#### Syntax

NIRFSA_ATTR_CALIBRATION_CORRECTION_320_MHZ_FILTER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150224 | ViReal64 | Read/Write | N/A |

#### Remarks

The value you specify using this attribute overrides any previously-set value.

**Units**: dB

**Default Value**: 0

**Supported Devices**: PXIe-5606

Parent topic:

NI 5665/5668R

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__signal__path_1ga1b587d1e14fec0249a96027b46fc3114.html language=enus -->
## TOPIC 00055: NIRFSA_ATTR_LO_SOURCE

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__signal__path_1ga1b587d1e14fec0249a96027b46fc3114.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__signal__path_1ga1b587d1e14fec0249a96027b46fc3114.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the LO signal source used to downconvert the RF input signal. SyntaxNIRFSA_ATTR_LO_SOURCENumeric ValueData TypeAccessApplies To1150162ViStringRead/WriteN/ARemarks If no signal downconversion is required, this attribute is ignored. If this attribute is set to "" (empty string), NI-RFSA uses

### NIRFSA_ATTR_LO_SOURCE

Specifies the LO signal source used to downconvert the RF input signal.

#### Syntax

NIRFSA_ATTR_LO_SOURCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150162 | ViString | Read/Write | N/A |

#### Remarks

If no signal downconversion is required, this attribute is ignored. If this attribute is set to "" (empty string), NI-RFSA uses the internal LO source.

To use this attribute for the PXIe-5830/5831/5832, you must use the channelName parameter of the [niRFSA_SetAttributeViString](group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__set__attribute_1ga36a5db3f92931d869655a49e3ba7d387.html) function to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

Note

For the PXIe-5841 with PXIe-5655, RF list mode is not supported when this attribute is set to **NIRFSA_VAL_LO_SOURCE_SG_SA_SHARED_STR**.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIRFSA_VAL_LO_IN_STR | LO_In | Specifies that the LO source used to downconvert the RF input signal is connected to the LO IN connector on the front panel. |
| NIRFSA_VAL_NONE_STR | None | Specifies that no LO source is required to downconvert the RF input signal. |
| NIRFSA_VAL_ONBOARD_STR | Onboard | Specifies that the onboard synthesizer is used to generate the LO signal that downconverts the RF input signal.**PXIe-5831/5832** This configuration uses the onboard LO of the PXIe-3622, using the LO2 stage.**PXIe-5831/5832 with PXIe-5653** This configuration uses the onboard LO of the PXIe-5653 when associated with the PXIe-3622.**PXIe-5841 with PXIe-5655** This configuration uses the onboard LO of the PXIe-5655. |
| NIRFSA_VAL_LO_SOURCE_SECONDARY_STR | Secondary | Uses the PXIe-5831/5840 internal LO as the LO source. This value is valid on only the PXIe-5831 with PXIe-5653 (LO1 stage only) or PXIe-5832 with PCIe-5653 (LO1 stage only). |
| NIRFSA_VAL_LO_SOURCE_SG_SA_SHARED_STR | SG_SA_Shared | Uses the same internal LO during NI-RFSA and NI-RFSG sessions. NI-RFSA selects an internal synthesizer and the synthesizer signal is switched to both the RF Out and RF In mixers. This value is valid on only the PXIe-5830/5831/5832/5841 with PXIe-5655. |

**Default Value**: **NIRFSA_VAL_ONBOARD_STR** ("Onboard")

**Supported Devices**: PXIe-5644/5645/5646, PXIe-5694, PXIe-5830/5831/5832/5840/5841/5842

**Related Topics**

[PXIe-5830 LO Sharing Using NI-RFSA and NI-RFSG](https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/lo-sharing-using-rfsa-rfsg.html)

[PXIe-5831/5832 LO Sharing Using NI-RFSA and NI-RFSG](https://www.ni.com/docs/en-US/bundle/pxie-5831/page/lo-sharing-using-rfsa-rfsg.html)

Parent topic:

Signal Path

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__signal__path_1ga2306097ec420b8a9c949b9b7f0ba7b79.html language=enus -->
## TOPIC 00056: NIRFSA_ATTR_LO_OUT_EXPORT_CONFIGURE_FROM_RFSG

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__signal__path_1ga2306097ec420b8a9c949b9b7f0ba7b79.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__signal__path_1ga2306097ec420b8a9c949b9b7f0ba7b79.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to allow NI-RFSG to control the NI-RFSA LO out export. SyntaxNIRFSA_ATTR_LO_OUT_EXPORT_CONFIGURE_FROM_RFSGNumeric ValueData TypeAccessApplies To1150299ViInt32Read/WriteN/ARemarks Set this attribute to NIRFSA_VAL_ENABLED to allow NI-RFSG to control the LO out export. Use the NIRFSG

### NIRFSA_ATTR_LO_OUT_EXPORT_CONFIGURE_FROM_RFSG

Specifies whether to allow NI-RFSG to control the NI-RFSA LO out export.

#### Syntax

NIRFSA_ATTR_LO_OUT_EXPORT_CONFIGURE_FROM_RFSG

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150299 | ViInt32 | Read/Write | N/A |

#### Remarks

Set this attribute to **NIRFSA_VAL_ENABLED** to allow NI-RFSG to control the LO out export. Use the NIRFSG ATTR RF IN LO EXPORT ENABLED attribute to control the NI-RFSA LO out export from NI-RFSG.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIRFSA_VAL_DISABLED | 1900 (0x76c) | The attribute is disabled. |
| NIRFSA_VAL_ENABLED | 1901 (0x76d) | The attribute is enabled. |

**Default Value:****NIRFSA_VAL_DISABLED**

**Supported Devices**: PXIe-5840/5841/5842

Parent topic:

Signal Path

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__signal__path_1ga39f159663f168568e320cb97d110b777.html language=enus -->
## TOPIC 00057: NIRFSA_ATTR_LO2_EXPORT_ENABLED

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__signal__path_1ga39f159663f168568e320cb97d110b777.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__signal__path_1ga39f159663f168568e320cb97d110b777.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the LO2 OUT terminal on the installed devices. SyntaxNIRFSA_ATTR_LO2_EXPORT_ENABLEDNumeric ValueData TypeAccessApplies To1150235ViInt32Read/WriteN/ARemarks Set this attribute to TRUE to export the 4 GHz LO signal from the device LO2 IN terminal to the LO2 OUT terminal.You

### NIRFSA_ATTR_LO2_EXPORT_ENABLED

Specifies whether to enable the LO2 OUT terminal on the installed devices.

#### Syntax

NIRFSA_ATTR_LO2_EXPORT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150235 | ViInt32 | Read/Write | N/A |

#### Remarks

Set this attribute to TRUE to export the 4 GHz LO signal from the device LO2 IN terminal to the LO2 OUT terminal.

You can also export the LO2 signal by setting the [NIRFSA_ATTR_LO_EXPORT_ENABLED](group____root__ni_r_f_s_a__attributes__signal__path_1ga26e4d0a7b305f7fe7d03ec72b70032f9.html) attribute and the [NIRFSA_ATTR_DIGITIZER_SAMPLE_CLOCK_TIMEBASE_SOURCE](group____root__ni_r_f_s_a__attributes__clocking_1ga7a95c6ae58d24bca6dddecff7182ff77.html) attribute.

**Defined Values:**

|  |  |
| --- | --- |
| VI_TRUE | Enables the LO2 OUT terminal. |
| VI_FALSE | Disables the LO2 OUT terminal. |

**Default Value:** VI_FALSE

**Supported Devices:** PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5668

Parent topic:

Signal Path

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__signal__path_1ga7065372afe424ff665f553e15886d4ad.html language=enus -->
## TOPIC 00058: NIRFSA_ATTR_DIGITIZER_DITHER_ENABLED

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__signal__path_1ga7065372afe424ff665f553e15886d4ad.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__signal__path_1ga7065372afe424ff665f553e15886d4ad.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether dithering is enabled on the digitizer. SyntaxNIRFSA_ATTR_DIGITIZER_DITHER_ENABLEDNumeric ValueData TypeAccessApplies To1150080ViInt32Read/WriteN/ARemarks Dithering adds band-limited noise in the analog signal path to help reduce the quantization effects of the A/D converter and imp

### NIRFSA_ATTR_DIGITIZER_DITHER_ENABLED

Specifies whether dithering is enabled on the digitizer.

#### Syntax

NIRFSA_ATTR_DIGITIZER_DITHER_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150080 | ViInt32 | Read/Write | N/A |

#### Remarks

Dithering adds band-limited noise in the analog signal path to help reduce the quantization effects of the A/D converter and improve spectral performance. On the PXIe-5622, this out-of-band noise is added at low frequencies up to approximately 12 MHz. On the PXIe-5624, this out-of-band noise is added at low frequencies up to approximately 50 MHz.

**PXIe-5663/5663E/5665/5667**: When you enable dithering, the maximum signal level is reduced by up to 3 dB. This signal level reduction is accounted for in the nominal input ranges of the PXIe-5622. Therefore, you can overrange the input by up to 3 dB with dither disabled. For example, the +4 dBm input range can handle signal levels up to +7 dBm with dither disabled. For wider bandwidth acquisitions, such as 40 MHz, disable dithering to eliminate residual leakage of the dither signal into the lower frequencies of the IF passband, which starts at 12.5 MHz and ends at 62.5 MHz. This leakage can slightly raise the noise floor in the lower frequencies, thus degrading the performance in high-sensitivity applications. When taking spectral measurements, this leakage can also appear as a wide, low-amplitude signal near 12.5 MHz and 62.5 MHz. The width and amplitude of the signal depends on your resolution bandwidth and the type of time-domain window you apply to your FFT.

**PXIe-5668**: When you enable dithering, the maximum signal level is reduced by up to 2 dB. For the PXIe-5624, the maximum input power with dither off is 8 dBm and the maximum input power with dither on is 6 dBm. When acquiring an 800 MHz bandwidth signal, the I/Q data contains the dither even if the dither signal is not in the displayed spectrum. The dither can affect actions like power level triggering.

Note

For the PXIe-5668, disabling dithering can negatively affect absolute amplitude accuracy.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIRFSA_VAL_DISABLED | 1900 (0x76c) | The attribute is disabled. |
| NIRFSA_VAL_ENABLED | 1901 (0x76d) | The attribute is enabled. |

Note

For the PXIe-5820/5830/5831/5832/5840/5841/5842, only **NIRFSA_VAL_ENABLED** is supported.

**Default Value**: **NIRFSA_VAL_ENABLED**

**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

Parent topic:

Signal Path

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__signal__path_1ga7dfc2547ed635c3d21f2e38b907996f4.html language=enus -->
## TOPIC 00059: NIRFSA_ATTR_IF_FILTER_BANDWIDTH

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__signal__path_1ga7dfc2547ed635c3d21f2e38b907996f4.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__signal__path_1ga7dfc2547ed635c3d21f2e38b907996f4.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the IF filter path bandwidth for your device configuration. SyntaxNIRFSA_ATTR_IF_FILTER_BANDWIDTHNumeric ValueData TypeAccessApplies To1150205ViReal64Read/WriteN/ARemarksFor composite devices, such as the PXIe-5665/5667/5668, the IF filter path bandwidth includes all IF filters across the

### NIRFSA_ATTR_IF_FILTER_BANDWIDTH

Specifies the IF filter path bandwidth for your device configuration.

#### Syntax

NIRFSA_ATTR_IF_FILTER_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150205 | ViReal64 | Read/Write | N/A |

#### Remarks

Note

For composite devices, such as the PXIe-5665/5667/5668, the IF filter path bandwidth includes all IF filters across the component modules of a composite device.

NI-RFSA uses this attribute in conjunction with the [NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH](group____root__ni_r_f_s_a__attributes__acquisition_1ga6dc8cd7ae513eea80c2f0f7206bfe0c0.html) attribute and the [NIRFSA_ATTR_DIGITAL_IF_EQUALIZATION_ENABLED](group____root__ni_r_f_s_a__attributes__signal__path_1gaba91585cbb83e83370d012c3a7732776.html) attribute to determine the settings for your measurement. NI-RFSA selects the next highest available filter based on the value you specify. The following table lists the IF filters available for NI devices. You may specify a higher value than your device instantaneous bandwidth if your measurement requires it, but specifying a lower value returns an error.

| Device | IF Filter Bandwidth Range | IF Filter |
| --- | --- | --- |
| PXIe-5603/5665 (3.6 GHz) | 2264300 kHz | 300 kHz IF filter |
| PXIe-5603/5665 (3.6 GHz) | >300 kHz and 22645 MHz | Through IF filter |
| PXIe-5603/5665 (3.6 GHz) | >5 MHz | Through IF filter |
| PXIe-5605/5665 (14 GHz) | 2264300 kHz | 300 kHz IF filter |
| PXIe-5603/5665 (14 GHz) | >300 kHz and 22645 MHz | 5 MHz IF filter |
| PXIe-5603/5665 (14 GHz) | >5 MHz | Through IF filter |
| PXIe-5668 | 2264300 kHz | 300 kHz IF filter |
| PXIe-5668 | >300 kHz and 22645 MHz | 5 MHz IF filter |
| PXIe-5668 | >5 MHz and 2264100 MHz | 100 MHz IF filter |
| PXIe-5668 | >100 MHz and 2264320 MHz | 320 MHz IF filter |
| PXIe-5668 | >320 MHz | 765 MHz IF filter |

**Valid Values**:

**PXIe-5603/5605**: 0 to 80 MHz

**PXIe-5665/5667**: 0 to 50 MHz

**PXIe-5668**: 0 to 765 MHz

**PXIe-5694**: 0 to 50 MHz

Note

To set this attribute to values greater than 20 MHz, you must set the [NIRFSA_ATTR_SIGNAL_CONDITIONING_ENABLED](group____root__ni_r_f_s_a__attributes__signal__path__advanced__ni__5694_1ga911d8d431b9d0d8d9737e434ec6c4944.html) attribute to **NIRFSA_VAL_SIGNAL_CONDITIONING_BYPASSED**

**Default Values:** For spectrum acquisition types the default is greater than or equal to the [NIRFSA_ATTR_SPECTRUM_SPAN](group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1ga438b38abd1378c3ccf5f6035f6c9bc2b.html) attribute. NI-RFSA chooses the default value of the [NIRFSA_ATTR_IF_FILTER_BANDWIDTH](group____root__ni_r_f_s_a__attributes__signal__path_1ga7dfc2547ed635c3d21f2e38b907996f4.html) attribute to correspond to the appropriate IF filter. For I/Q acquisition types NI-RFSA chooses the default value corresponding to the widest IF filter possible for your equipment setup.

**Supported Devices**: PXIe-5603/5605/5606, PXIe-5665/5667/5668, PXIe-5694

Parent topic:

Signal Path

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__signal__path__advanced_1ga28dab6947521ace79f996ff8915eb857.html language=enus -->
## TOPIC 00060: NIRFSA_ATTR_INPUT_ISOLATION_ENABLED

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__signal__path__advanced_1ga28dab6947521ace79f996ff8915eb857.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__signal__path__advanced_1ga28dab6947521ace79f996ff8915eb857.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether input isolation is enabled. SyntaxNIRFSA_ATTR_INPUT_ISOLATION_ENABLEDNumeric ValueData TypeAccessApplies To1150170ViInt32Read/WriteN/ARemarks Enabling this attribute isolates the input signal at the RF IN connector on the RF downconverter from the rest of the RF downconverter signa

### NIRFSA_ATTR_INPUT_ISOLATION_ENABLED

Specifies whether input isolation is enabled.

#### Syntax

NIRFSA_ATTR_INPUT_ISOLATION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150170 | ViInt32 | Read/Write | N/A |

#### Remarks

Enabling this attribute isolates the input signal at the RF IN connector on the RF downconverter from the rest of the RF downconverter signal path. Disabling this attribute reintegrates the input signal into the RF downconverter signal path.

Note

If you enable input isolation for your device, the device impedance is changed from the characteristic 50 impedance. A change in the device impedance may also cause a VSWR value higher than the device specifications.

For the PXIe-5830/5831/5832, input isolation is supported for all available ports for your hardware configuration.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIRFSA_VAL_DISABLED | 1900 (0x76c) | The attribute is disabled. |
| NIRFSA_VAL_ENABLED | 1901 (0x76d) | The attribute is enabled. |

**Default Value**: **NIRFSA_VAL_DISABLED**, if the device configuration is supported.

**Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5693, PXIe-5820/5830/5831/5832/5840/5841

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__signal__path__advanced_1ga68f118b3a29116b5d396612ee49e3a65.html language=enus -->
## TOPIC 00061: NIRFSA_ATTR_SELECTED_PORTS

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__signal__path__advanced_1ga68f118b3a29116b5d396612ee49e3a65.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__signal__path__advanced_1ga68f118b3a29116b5d396612ee49e3a65.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the port to configure. SyntaxNIRFSA_ATTR_SELECTED_PORTSNumeric ValueData TypeAccessApplies To1150297ViStringRead/WriteN/ARemarksWhen using RF list mode, ports cannot be shared with NI-RFSA.Valid Values:PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860: "" (empty string)PXIe-5830: if0, if1

### NIRFSA_ATTR_SELECTED_PORTS

Specifies the port to configure.

#### Syntax

NIRFSA_ATTR_SELECTED_PORTS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150297 | ViString | Read/Write | N/A |

#### Remarks

Note

When using RF list mode, ports cannot be shared with NI-RFSA.

**Valid Values**:

**PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860**: "" (empty string)

**PXIe-5830**: if0, if1

**PXIe-5831/5832**: if0, if1, rf <0-1> port <x>, where

*0-1* indicates one (*0*) or two (*1*) mmRH-5582 connections and

*x* is the port number on the mmRH-5582 front panel.

**Default Value:**

**PXIe-5830/5831/5832:**: if1

**PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860**: "" (empty string)

**Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[NIRFSA_ATTR_AVAILABLE_PORTS](group____root__ni_r_f_s_a__attributes__signal__path__advanced_1ga02c6b3352444e672a502891063f4724b.html)

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__signal__path__advanced_1ga725f827015b0a44d7ada587ae46d446b.html language=enus -->
## TOPIC 00062: NIRFSA_ATTR_FIXED_GROUP_DELAY_ACROSS_PORTS

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__signal__path__advanced_1ga725f827015b0a44d7ada587ae46d446b.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__signal__path__advanced_1ga725f827015b0a44d7ada587ae46d446b.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a comma-separated list of ports for which to fix the group delay. SyntaxNIRFSA_ATTR_FIXED_GROUP_DELAY_ACROSS_PORTSNumeric ValueData TypeAccessApplies To1150324ViStringRead/WriteN/ARemarksValid Values:PXIe-5831/5832: rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connecti

### NIRFSA_ATTR_FIXED_GROUP_DELAY_ACROSS_PORTS

Specifies a comma-separated list of ports for which to fix the group delay.

#### Syntax

NIRFSA_ATTR_FIXED_GROUP_DELAY_ACROSS_PORTS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150324 | ViString | Read/Write | N/A |

#### Remarks

**Valid Values**:

PXIe-5831/5832: rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel.

**Default Value**:

PXIe-5831/5832: "" (empty string), which specifies that the group delay will not be fixed for any port.

**Supported Devices**: PXIe-5831/5832

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__signal__path__advanced_1ga83313b28e901d44ab02266c9b6965747.html language=enus -->
## TOPIC 00063: NIRFSA_ATTR_DOWNCONVERTER_PRESELECTOR_ENABLED

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__signal__path__advanced_1ga83313b28e901d44ab02266c9b6965747.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__signal__path__advanced_1ga83313b28e901d44ab02266c9b6965747.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the tunable preselector is enabled on the downconverter. SyntaxNIRFSA_ATTR_DOWNCONVERTER_PRESELECTOR_ENABLEDNumeric ValueData TypeAccessApplies To1150132ViInt32Read/WriteN/ARemarksAll devices support setting this attribute to NIRFSA_VAL_PRESELECTOR_DISABLED or NIRFSA_VAL_PRESELECTO

### NIRFSA_ATTR_DOWNCONVERTER_PRESELECTOR_ENABLED

Specifies whether the tunable preselector is enabled on the downconverter.

#### Syntax

NIRFSA_ATTR_DOWNCONVERTER_PRESELECTOR_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150132 | ViInt32 | Read/Write | N/A |

#### Remarks

Note

All devices support setting this attribute to **NIRFSA_VAL_PRESELECTOR_DISABLED** or **NIRFSA_VAL_PRESELECTOR_ENABLED_WHEN_IN_SIGNAL_PATH**. Only devices with a preselector support setting this attribute to **NIRFSA_VAL_PRESELECTOR_ENABLED**.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIRFSA_VAL_PRESELECTOR_DISABLED | 2600 (0xa28) | Disables the preselector. |
| NIRFSA_VAL_PRESELECTOR_ENABLED | 2602 (0xa2a) | Enables the preselector. If the preselector is not in the signal path or if the preselector is not supported on the device, NI-RFSA returns an error. Select the NIRFSA_VAL_PRESELECTOR_ENABLED_WHEN_IN_SIGNAL_PATH whenever possible avoid an error. |
| NIRFSA_VAL_PRESELECTOR_ENABLED_WHEN_IN_SIGNAL_PATH | 2601 (0xa29) | The preselector is automatically enabled when it is in the signal path and is automatically disabled when it is not in the signal path. Use the NIRFSA_ATTR_PRESELECTOR_PRESENT attribute to determine if the downconverter has an preselector. |

**Default Value**: **NIRFSA_VAL_PRESELECTOR_DISABLED** if the device has no preselector. **NIRFSA_VAL_PRESELECTOR_ENABLED_WHEN_IN_SIGNAL_PATH** if the device has a preselector.

**Supported Devices:** PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842/5860

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__signal__path__advanced__ni__5663_1gae7b87e11ac3aec3dfd43efd43a5a5313.html language=enus -->
## TOPIC 00064: NIRFSA_ATTR_IF2_ATTEN_VALUE

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__signal__path__advanced__ni__5663_1gae7b87e11ac3aec3dfd43efd43a5a5313.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__signal__path__advanced__ni__5663_1gae7b87e11ac3aec3dfd43efd43a5a5313.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the IF2 attenuation, in dB. The device IF2 attenuator is set to this nominal value. SyntaxNIRFSA_ATTR_IF2_ATTEN_VALUENumeric ValueData TypeAccessApplies To1150079ViReal64Read/WriteN/ARemarks Use this attribute, along with the NIRFSA_ATTR_IF1_ATTEN_VALUE attribute, when you set the NIRFSA_A

### NIRFSA_ATTR_IF2_ATTEN_VALUE

Specifies the IF2 attenuation, in dB. The device IF2 attenuator is set to this nominal value.

#### Syntax

NIRFSA_ATTR_IF2_ATTEN_VALUE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150079 | ViReal64 | Read/Write | N/A |

#### Remarks

Use this attribute, along with the [NIRFSA_ATTR_IF1_ATTEN_VALUE](group____root__ni_r_f_s_a__attributes__signal__path__advanced__ni__5663_1ga3d3668fa615297bf3696f1c32c57b7dc.html) attribute, when you set the [NIRFSA_ATTR_IF_FILTER](group____root__ni_r_f_s_a__attributes__signal__path__advanced__ni__5663_1ga3f434071e2307d45b7eed37fd6e84ed9.html) attribute to **NIRFSA_VAL_BYPASS**.

**Valid Values**: 0 to 15

**Units**: dB

**Default Value**: N/A

**Supported Devices**: PXIe-5601 (external digitizer mode), PXIe-5663/5663E

Parent topic:

NI 5663

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__signal__path__advanced__ni__5694_1ga911d8d431b9d0d8d9737e434ec6c4944.html language=enus -->
## TOPIC 00065: NIRFSA_ATTR_SIGNAL_CONDITIONING_ENABLED

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__signal__path__advanced__ni__5694_1ga911d8d431b9d0d8d9737e434ec6c4944.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__signal__path__advanced__ni__5694_1ga911d8d431b9d0d8d9737e434ec6c4944.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether all signal conditioning is enabled on the PXIe-5694. SyntaxNIRFSA_ATTR_SIGNAL_CONDITIONING_ENABLEDNumeric ValueData TypeAccessApplies To1150160ViInt32Read/WriteN/ARemarksIf you set this attribute to NIRFSA_VAL_SIGNAL_CONDITIONING_BYPASSED, NI-RFSA bypasses all signal conditioning,

### NIRFSA_ATTR_SIGNAL_CONDITIONING_ENABLED

Specifies whether all signal conditioning is enabled on the PXIe-5694.

#### Syntax

NIRFSA_ATTR_SIGNAL_CONDITIONING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150160 | ViInt32 | Read/Write | N/A |

#### Remarks

Note

If you set this attribute to **NIRFSA_VAL_SIGNAL_CONDITIONING_BYPASSED**, NI-RFSA bypasses all signal conditioning, prevents any signal downconversion, and fixes the values for [NIRFSA_ATTR_DOWNCONVERTER_GAIN](group____root__ni_r_f_s_a__attributes__vertical_1ga0d25e4671022de4c2e6d09df3797acef.html) attribute, the [NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH](group____root__ni_r_f_s_a__attributes__acquisition_1ga6dc8cd7ae513eea80c2f0f7206bfe0c0.html) attribute, and the [NIRFSA_ATTR_IF_FILTER_BANDWIDTH](group____root__ni_r_f_s_a__attributes__signal__path_1ga7dfc2547ed635c3d21f2e38b907996f4.html) attribute.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIRFSA_VAL_SIGNAL_CONDITIONING_BYPASSED | 3601 (0xe11) | Bypasses all signal conditioning. |
| NIRFSA_VAL_SIGNAL_CONDITIONING_ENABLED | 3600 (0xe10) | Enables signal conditioning. |

**Default Value**: **NIRFSA_VAL_SIGNAL_CONDITIONING_ENABLED**

**Supported Devices**: PXIe-5694

Parent topic:

NI 5694

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__triggers__advance__export_1ga705aa88449d02b1d0ff100731cede001.html language=enus -->
## TOPIC 00066: NIRFSA_ATTR_EXPORTED_ADVANCE_TRIGGER_OUTPUT_TERMINAL

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__triggers__advance__export_1ga705aa88449d02b1d0ff100731cede001.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__triggers__advance__export_1ga705aa88449d02b1d0ff100731cede001.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for the exported Advance Trigger. SyntaxNIRFSA_ATTR_EXPORTED_ADVANCE_TRIGGER_OUTPUT_TERMINALNumeric ValueData TypeAccessApplies To1150038ViStringRead/WriteN/ARemarksDefined Values:NameValueDescriptionNIRFSA_VAL_CLK_OUT_STRClkOutExport the clock on the CLK OUT termi

### NIRFSA_ATTR_EXPORTED_ADVANCE_TRIGGER_OUTPUT_TERMINAL

Specifies the destination terminal for the exported Advance Trigger.

#### Syntax

NIRFSA_ATTR_EXPORTED_ADVANCE_TRIGGER_OUTPUT_TERMINAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150038 | ViString | Read/Write | N/A |

#### Remarks

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIRFSA_VAL_CLK_OUT_STR | ClkOut | Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841. |
| NIRFSA_VAL_DO_NOT_EXPORT_STR |  | The signal is not exported. |
| NIRFSA_VAL_PFI0_STR | PFI0 | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0. |
| NIRFSA_VAL_PFI1_STR | PFI1 | The trigger is received on PFI 1. |
| NIRFSA_VAL_PXI_STAR_STR | PXI_STAR | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646. |
| NIRFSA_VAL_PXI_TRIG0_STR | PXI_Trig0 | The trigger is received on PXI trigger line 0. |
| NIRFSA_VAL_PXI_TRIG1_STR | PXI_Trig1 | The trigger is received on PXI trigger line 1. |
| NIRFSA_VAL_PXI_TRIG2_STR | PXI_Trig2 | The trigger is received on PXI trigger line 2. |
| NIRFSA_VAL_PXI_TRIG3_STR | PXI_Trig3 | The trigger is received on PXI trigger line 3. |
| NIRFSA_VAL_PXI_TRIG4_STR | PXI_Trig4 | The trigger is received on PXI trigger line 4. |
| NIRFSA_VAL_PXI_TRIG5_STR | PXI_Trig5 | The trigger is received on PXI trigger line 5. |
| NIRFSA_VAL_PXI_TRIG6_STR | PXI_Trig6 | The trigger is received on PXI trigger line 6. |
| NIRFSA_VAL_PXI_TRIG7_STR | PXI_Trig7 | The trigger is received on PXI trigger line 7. |
| NIRFSA_VAL_PXIE_DSTARC_STR | PXIe_DStarC | The trigger is received on the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841. |
| NIRFSA_VAL_REF_OUT_STR | RefOut | Export the clock on the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, PXIe-5694, or PXIe-5820/5830/5831/5832/5840/5841. |
| NIRFSA_VAL_REF_OUT2_STR | RefOut2 | Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E. |
| NIRFSA_VAL_DIO_PFI0_STR | DIO/PFI0 | The trigger is received on PFI0 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI1_STR | DIO/PFI1 | The trigger is received on PFI1 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI2_STR | DIO/PFI2 | The trigger is received on PFI2 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI3_STR | DIO/PFI3 | The trigger is received on PFI3 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI4_STR | DIO/PFI4 | The trigger is received on PFI4 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI5_STR | DIO/PFI5 | The trigger is received on PFI5 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI6_STR | DIO/PFI6 | The trigger is received on PFI6 from the front panel DIO terminal. |
| NIRFSA_VAL_DIO_PFI7_STR | DIO/PFI7 | The trigger is received on PFI7 from the front panel DIO terminal. |

**Default Value**: "" (empty string)

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**High-Level Functions**:

- [niRFSA_ExportSignal](group____root__ni_r_f_s_a__functions__configuration__clock_1gaa0e7acfa202c06fb09bdf610d8a613eb.html)

Parent topic:

Export

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__triggers__advanced_1ga33fd3a0a542707c14a30901c286f1773.html language=enus -->
## TOPIC 00067: NIRFSA_ATTR_DDC_REF_TRIGGER_OVERRIDE

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__triggers__advanced_1ga33fd3a0a542707c14a30901c286f1773.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__triggers__advanced_1ga33fd3a0a542707c14a30901c286f1773.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This attribute is not for customer use. SyntaxNIRFSA_ATTR_DDC_REF_TRIGGER_OVERRIDENumeric ValueData TypeAccessApplies To1150164ViBooleanRead/WriteN/A

### NIRFSA_ATTR_DDC_REF_TRIGGER_OVERRIDE

This attribute is not for customer use.

#### Syntax

NIRFSA_ATTR_DDC_REF_TRIGGER_OVERRIDE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150164 | ViBoolean | Read/Write | N/A |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__triggers__advanced_1ga6733ed843de0c835a74eda59b7de4aff.html language=enus -->
## TOPIC 00068: NIRFSA_ATTR_START_TRIGGER_DELAY

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__triggers__advanced_1ga6733ed843de0c835a74eda59b7de4aff.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__triggers__advanced_1ga6733ed843de0c835a74eda59b7de4aff.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This attribute is not for customer use. SyntaxNIRFSA_ATTR_START_TRIGGER_DELAYNumeric ValueData TypeAccessApplies To1150175ViReal64Read/WriteN/A

### NIRFSA_ATTR_START_TRIGGER_DELAY

This attribute is not for customer use.

#### Syntax

NIRFSA_ATTR_START_TRIGGER_DELAY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150175 | ViReal64 | Read/Write | N/A |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__triggers__arm__ref__digital__edge.html language=enus -->
## TOPIC 00069: Digital Edge

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__triggers__arm__ref__digital__edge.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__triggers__arm__ref__digital__edge.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIRFSA_ATTR_DIGITAL_EDGE_ARM_REF_TRIGGER_SOURCESpecifies the source terminal for the digital edge Arm Reference Trigger. AttachmentsNone

### Digital Edge

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIRFSA_ATTR_DIGITAL_EDGE_ARM_REF_TRIGGER_SOURCE | Specifies the source terminal for the digital edge Arm Reference Trigger. |

#### Attachments

None

Parent topic:

Arm Ref

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__triggers__configuration__list__step.html language=enus -->
## TOPIC 00070: Configuration List Step

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__triggers__configuration__list__step.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__triggers__configuration__list__step.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDigital EdgeGroup membersNoneAttachmentsNone

### Configuration List Step

#### Groups

- Digital Edge

#### Group members

None

#### Attachments

None

Parent topic:

Triggers

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__triggers__configuration__list__step__digital__edge.html language=enus -->
## TOPIC 00071: Digital Edge

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__triggers__configuration__list__step__digital__edge.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__triggers__configuration__list__step__digital__edge.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIRFSA_ATTR_DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCEConfigures the list trigger source. AttachmentsNone

### Digital Edge

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIRFSA_ATTR_DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE | Configures the list trigger source. |

#### Attachments

None

Parent topic:

Configuration List Step

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__triggers__ref.html language=enus -->
## TOPIC 00072: Ref

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__triggers__ref.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__triggers__ref.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdvancedDigital EdgeExportIQ Power EdgeGroup membersNameDescriptionNIRFSA_ATTR_REF_TRIGGER_MINIMUM_QUIET_TIMESpecifies a time duration, in seconds, for which the signal must be quiet before the device arms the trigger. NIRFSA_ATTR_REF_TRIGGER_PRETRIGGER_SAMPLESSpecifies the number of pretrigge

### Ref

#### Groups

- Advanced
- Digital Edge
- Export
- IQ Power Edge

#### Group members

| Name | Description |
| --- | --- |
| NIRFSA_ATTR_REF_TRIGGER_MINIMUM_QUIET_TIME | Specifies a time duration, in seconds, for which the signal must be quiet before the device arms the trigger. |
| NIRFSA_ATTR_REF_TRIGGER_PRETRIGGER_SAMPLES | Specifies the number of pretrigger samples the samples acquired before the Reference Trigger is received to be acquired per record. |
| NIRFSA_ATTR_REF_TRIGGER_TERMINAL_NAME | Returns the fully qualified signal name as a string. |
| NIRFSA_ATTR_REF_TRIGGER_TYPE | Specifies whether you want the Reference Trigger to be a digital edge, I/Q power edge, or software trigger. |

#### Attachments

None

Parent topic:

Triggers

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__triggers__ref__export.html language=enus -->
## TOPIC 00073: Export

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__triggers__ref__export.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__triggers__ref__export.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIRFSA_ATTR_EXPORTED_REF_TRIGGER_OUTPUT_TERMINALSpecifies the destination terminal for the exported Reference Trigger. AttachmentsNone

### Export

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIRFSA_ATTR_EXPORTED_REF_TRIGGER_OUTPUT_TERMINAL | Specifies the destination terminal for the exported Reference Trigger. |

#### Attachments

None

Parent topic:

Ref

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__triggers__start__digital__edge_1ga6b2251271b365494a4d045a0008d5196.html language=enus -->
## TOPIC 00074: NIRFSA_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__triggers__start__digital__edge_1ga6b2251271b365494a4d045a0008d5196.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__triggers__start__digital__edge_1ga6b2251271b365494a4d045a0008d5196.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the active edge for the Start Trigger. SyntaxNIRFSA_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGENumeric ValueData TypeAccessApplies To1150026ViInt32Read/WriteN/ARemarks This attribute is used only when the NIRFSA_ATTR_START_TRIGGER_TYPE attribute is set to NIRFSA_VAL_DIGITAL_EDGE.Defined and Valid

### NIRFSA_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE

Specifies the active edge for the Start Trigger.

#### Syntax

NIRFSA_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150026 | ViInt32 | Read/Write | N/A |

#### Remarks

This attribute is used only when the [NIRFSA_ATTR_START_TRIGGER_TYPE](group____root__ni_r_f_s_a__attributes__triggers__start_1ga29d0d0b99120bee02c1ef7c7b7adff4a.html) attribute is set to **NIRFSA_VAL_DIGITAL_EDGE**.

**Defined and Valid Values:**

| Value | Description | Valid For |
| --- | --- | --- |
| NIRFSA_VAL_RISING_EDGE (900) | The trigger asserts on the rising edge of the signal. | PXI-5661, PXIe-5663/5663E/5665/5668 |
| NIRFSA_VAL_FALLING_EDGE (901) | The trigger asserts on the falling edge of the signal | PXIe-5668 |

**Default Value**: **NIRFSA_VAL_RISING_EDGE**

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Triggers](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html)

**High-Level Functions**:

- [niRFSA_ConfigureDigitalEdgeStartTrigger](group____root__ni_r_f_s_a__functions__configuration__trigger__start__trigger_1ga8457b8ed5f88516fcdb37d14ee3a3614.html)

Parent topic:

Digital Edge

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__vertical_1ga06e722aba7b1830c417d92ec5b964914.html language=enus -->
## TOPIC 00075: NIRFSA_ATTR_MIXER_LEVEL_OFFSET

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__vertical_1ga06e722aba7b1830c417d92ec5b964914.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__vertical_1ga06e722aba7b1830c417d92ec5b964914.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of dB by which to adjust the device mixer level. SyntaxNIRFSA_ATTR_MIXER_LEVEL_OFFSETNumeric ValueData TypeAccessApplies To1150127ViReal64Read/WriteN/ARemarks The default value is 0, which specifies device settings that are the best compromise between distortion and noise. Speci

### NIRFSA_ATTR_MIXER_LEVEL_OFFSET

Specifies the number of dB by which to adjust the device mixer level.

#### Syntax

NIRFSA_ATTR_MIXER_LEVEL_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150127 | ViReal64 | Read/Write | N/A |

#### Remarks

The default value is 0, which specifies device settings that are the best compromise between distortion and noise. Specifying a positive value for this attribute configures the device for moderate distortion and low noise, and specifying a negative value results in low distortion and higher noise.

You cannot set the [NIRFSA_ATTR_MIXER_LEVEL](group____root__ni_r_f_s_a__attributes__vertical_1gaa66439045cac15424b52feb9a942b27b.html) and [NIRFSA_ATTR_MIXER_LEVEL_OFFSET](group____root__ni_r_f_s_a__attributes__vertical_1ga06e722aba7b1830c417d92ec5b964914.html) attributes at the same time.

**PXIe-5667**: This attribute is read-only when the [NIRFSA_ATTR_LOW_FREQUENCY_BYPASS_ENABLED](group____root__ni_r_f_s_a__attributes__signal__path__advanced_1ga40129ae79e29b003e879f3db409f900f.html) attribute is set to **NIRFSA_VAL_DISABLED**.

**Units**: dB

**Default Value**: 0

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668

Parent topic:

Vertical

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__vertical_1ga47d505c5314d5aef4dd882004c9b13e7.html language=enus -->
## TOPIC 00076: NIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL_OFFSET

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__vertical_1ga47d505c5314d5aef4dd882004c9b13e7.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__vertical_1ga47d505c5314d5aef4dd882004c9b13e7.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of dB by which to adjust the default IF output power level. SyntaxNIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL_OFFSETNumeric ValueData TypeAccessApplies To1150131ViReal64Read/WriteN/ARemarks This attribute does not depend on absolute IF output power levels, so you can use it to adjust the

### NIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL_OFFSET

Specifies the number of dB by which to adjust the default IF output power level.

#### Syntax

NIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150131 | ViReal64 | Read/Write | N/A |

#### Remarks

This attribute does not depend on absolute IF output power levels, so you can use it to adjust the IF output power level on all NI-RFSA devices without knowing the exact default value. Use this attribute to increase or decrease the nominal output level to achieve better measurement results. The default value for the offset is 0 dB.

If you set the [NIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL](group____root__ni_r_f_s_a__attributes__vertical_1ga94a555c25f426b548697645c731e8dc9.html) and [NIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL_OFFSET](group____root__ni_r_f_s_a__attributes__vertical_1ga47d505c5314d5aef4dd882004c9b13e7.html) attributes at the same time, NI-RFSA returns an error.

**Units**: dB

**Default Value**: 0

**Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668

Parent topic:

Vertical

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__vertical__advanced_1ga0a02838fa0df48c1ab923c17c3f60d5a.html language=enus -->
## TOPIC 00077: NIRFSA_ATTR_MECHANICAL_ATTENUATION

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__vertical__advanced_1ga0a02838fa0df48c1ab923c17c3f60d5a.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__vertical__advanced_1ga0a02838fa0df48c1ab923c17c3f60d5a.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the level of mechanical attenuation for the RF path, in dB. SyntaxNIRFSA_ATTR_MECHANICAL_ATTENUATIONNumeric ValueData TypeAccessApplies To1150128ViReal64Read/WriteN/ARemarksPXIe-5667: This attribute is read-only when the NIRFSA_ATTR_LOW_FREQUENCY_BYPASS_ENABLED attribute is set to NIRFSA_V

### NIRFSA_ATTR_MECHANICAL_ATTENUATION

Specifies the level of mechanical attenuation for the RF path, in dB.

#### Syntax

NIRFSA_ATTR_MECHANICAL_ATTENUATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150128 | ViReal64 | Read/Write | N/A |

#### Remarks

**PXIe-5667**: This attribute is read-only when the [NIRFSA_ATTR_LOW_FREQUENCY_BYPASS_ENABLED](group____root__ni_r_f_s_a__attributes__signal__path__advanced_1ga40129ae79e29b003e879f3db409f900f.html) attribute is set to **NIRFSA_VAL_DISABLED**.

**PXIe-5668with PXIe-5698**: This attribute is read-only when the [NIRFSA_ATTR_RF_PREAMP_ENABLED](group____root__ni_r_f_s_a__attributes__vertical__advanced_1ga7005338da3a102e6e4648c7c66b315c8.html) attribute is set to **NIRFSA_VAL_RF_PREAMP_ENABLED**.

**Units**: dB

**Valid Values:**

**PXIe-5601/5663/5663E**: 0, 16

**PXIe-5603/5665 (3.6 GHz)**: 0, 10, 20, 30

**PXIe-5605/5665 (14 GHz), PXIe-5606/5668**: 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75

**PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector low frequency bypass path**: 0, 10, 20, 30

**PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector filter path**: 0

**PXIe-5667 (7 GHz) using the PXIe-5693 RF preselector low frequency bypass path**: 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75

**PXIe-5667 (7 GHz) using the PXIe-5693 RF preselector filter path**: 0

**PXIe-5668 with PXIe-5698 with the**[NIRFSA_ATTR_RF_PREAMP_ENABLED](group____root__ni_r_f_s_a__attributes__vertical__advanced_1ga7005338da3a102e6e4648c7c66b315c8.html) attribute set to **NIRFSA_VAL_RF_PREAMP_ENABLED**: 5

**Default Value**: N/A

**Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__vertical__advanced_1ga0ab282e9e4ab0fa1dc44e540a71999a3.html language=enus -->
## TOPIC 00078: NIRFSA_ATTR_THERMAL_CORRECTION_TEMPERATURE_RESOLUTION

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__vertical__advanced_1ga0ab282e9e4ab0fa1dc44e540a71999a3.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__vertical__advanced_1ga0ab282e9e4ab0fa1dc44e540a71999a3.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the temperature change required before NI-RFSA recalculates the thermal correction settings when entering the Running state. SyntaxNIRFSA_ATTR_THERMAL_CORRECTION_TEMPERATURE_RESOLUTIONNumeric ValueData TypeAccessApplies To1150300ViReal64Read/WriteN/ARemarksUnits: degrees Celsius (C)Support

### NIRFSA_ATTR_THERMAL_CORRECTION_TEMPERATURE_RESOLUTION

Specifies the temperature change required before NI-RFSA recalculates the thermal correction settings when entering the Running state.

#### Syntax

NIRFSA_ATTR_THERMAL_CORRECTION_TEMPERATURE_RESOLUTION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150300 | ViReal64 | Read/Write | N/A |

#### Remarks

**Units:** degrees Celsius (C)

**Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Default Values**:

**PXIe-5830/5831/5832/5842/5860**: 0.2

**PXIe-5840/5841**: 1.0

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__vertical__advanced__ni__566556675668r_1ga056af7c6175d0df4601fce8c1bf93803.html language=enus -->
## TOPIC 00079: NIRFSA_ATTR_CHANNEL_COUPLING

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__vertical__advanced__ni__566556675668r_1ga056af7c6175d0df4601fce8c1bf93803.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__vertical__advanced__ni__566556675668r_1ga056af7c6175d0df4601fce8c1bf93803.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the RF IN connector is AC- or DC-coupled on the downconverter. SyntaxNIRFSA_ATTR_CHANNEL_COUPLINGNumeric ValueData TypeAccessApplies To1150149ViInt32Read/WriteN/ARemarksFor the PXIe-5605/5606/5665/5667/5668, this attribute must be set to NIRFSA_VAL_AC when the DC block is present a

### NIRFSA_ATTR_CHANNEL_COUPLING

Specifies whether the RF IN connector is AC- or DC-coupled on the downconverter.

#### Syntax

NIRFSA_ATTR_CHANNEL_COUPLING

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150149 | ViInt32 | Read/Write | N/A |

#### Remarks

Note

For the PXIe-5605/5606/5665/5667/5668, this attribute must be set to **NIRFSA_VAL_AC** when the DC block is present and set to **NIRFSA_VAL_DC** when the DC block is not present to ensure device specifications are met and proper calibration data is used. For more information about removing or attaching the DC block, refer to the [PXIe-5665 Block Diagram](https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/block-diagram.2.html), the [PXIe-5605 Front Panel and LEDs](https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/pinout.4.html), the [PXIe-5667 Block Diagram](https://www.ni.com/docs/en-US/bundle/pxie-5667-feature/page/block-diagram.html), or the [PXIe-5668 Block Diagram](https://www.ni.com/docs/en-US/bundle/pxie-5668-feature/page/block-diagram.html) topics in this help file.

**Valid Values**:

**PXIe-5603/5665 (3.6 GHz)**: **NIRFSA_VAL_AC**, **NIRFSA_VAL_DC**

**PXIe-5605/5665 (14 GHz)**: **NIRFSA_VAL_AC**, **NIRFSA_VAL_DC**

**PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector low-frequency bypass path**: **NIRFSA_VAL_AC**, **NIRFSA_VAL_DC**

**PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector filter path**: **NIRFSA_VAL_AC**

**PXIe-5667 (7 GHz)**: **NIRFSA_VAL_AC**

**PXIe-5606/5668**: **NIRFSA_VAL_AC**, **NIRFSA_VAL_DC**

**Defined Values**:

| Name | Value | Description |
| --- | --- | --- |
| NIRFSA_VAL_AC | 3001 (0xbb9) | Specifies that the RF input channel is AC-coupled. For low frequencies (<10 MHz), accuracy decreases because NI-RFSA does not calibrate the configuration. |
| NIRFSA_VAL_DC | 3002 (0xbba) | Specifies that the RF input channel is DC-coupled. NI-RFSA enforces a minimum RF attenuation for device protection. |

**Default Value**: **NIRFSA_VAL_AC**

**Supported Devices**: PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5667/5668

Parent topic:

NI 5665/5667/5668R

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__vertical__advanced__ni__5693.html language=enus -->
## TOPIC 00080: NI 5693

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__vertical__advanced__ni__5693.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__vertical__advanced__ni__5693.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIRFSA_ATTR_CAL_TONE_POWER_REFERRED_TO_RF_INReturns the power of a virtual signal connected to the RF IN connector on the PXIe-5693 front panel when the calibration tone is enabled. AttachmentsNone

### NI 5693

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIRFSA_ATTR_CAL_TONE_POWER_REFERRED_TO_RF_IN | Returns the power of a virtual signal connected to the RF IN connector on the PXIe-5693 front panel when the calibration tone is enabled. |

#### Attachments

None

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__vertical__advanced__ni__5693_1ga97e32256875183748744f29ad2e4967a.html language=enus -->
## TOPIC 00081: NIRFSA_ATTR_CAL_TONE_POWER_REFERRED_TO_RF_IN

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__vertical__advanced__ni__5693_1ga97e32256875183748744f29ad2e4967a.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__vertical__advanced__ni__5693_1ga97e32256875183748744f29ad2e4967a.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power of a virtual signal connected to the RF IN connector on the PXIe-5693 front panel when the calibration tone is enabled. SyntaxNIRFSA_ATTR_CAL_TONE_POWER_REFERRED_TO_RF_INNumeric ValueData TypeAccessApplies To1150174ViReal64Read-OnlyN/ARemarks You can enable a calibration tone for t

### NIRFSA_ATTR_CAL_TONE_POWER_REFERRED_TO_RF_IN

Returns the power of a virtual signal connected to the RF IN connector on the PXIe-5693 front panel when the calibration tone is enabled.

#### Syntax

NIRFSA_ATTR_CAL_TONE_POWER_REFERRED_TO_RF_IN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150174 | ViReal64 | Read-Only | N/A |

#### Remarks

You can enable a calibration tone for the PXIe-5693 by setting the [NIRFSA_ATTR_RF_CONDITIONING_CAL_TONE_MODE](group____root__ni_r_f_s_a__attributes__self__calibration_1ga6f75a321276ea6e6790614dd4e745236.html) attribute to **NIRFSA_VAL_CAL_TONE_LOWBAND_RF** or **NIRFSA_VAL_CAL_TONE_HIGHBAND_RF**.

**Units**: dBm

**Default Value**: N/A

**Supported Devices**: PXIe-5693

Parent topic:

NI 5693

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__attributes__vertical__advanced__ni__5694.html language=enus -->
## TOPIC 00082: NI 5694

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__attributes__vertical__advanced__ni__5694.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__attributes__vertical__advanced__ni__5694.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIRFSA_ATTR_STEP_GAIN_ENABLEDSpecifies whether to enable the step gain amplifier. AttachmentsNone

### NI 5694

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIRFSA_ATTR_STEP_GAIN_ENABLED | Specifies whether to enable the step gain amplifier. |

#### Attachments

None

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions.html language=enus -->
## TOPIC 00083: Functions

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAcquisitionCalibrationConfigurationUtilityGroup membersNameDescriptionniRFSA_CloseCloses the session to the device. niRFSA_GetFrequencyResponseReturns the requested response type, based on current NI-RFSA settings. The PXI-5661 and PXIe-5663/5663E/5665/5667/5668 automatically corrects the IF a

### Functions

#### Groups

- Acquisition
- Calibration
- Configuration
- Utility

#### Group members

| Name | Description |
| --- | --- |
| niRFSA_Close | Closes the session to the device. |
| niRFSA_GetFrequencyResponse | Returns the requested response type, based on current NI-RFSA settings. The PXI-5661 and PXIe-5663/5663E/5665/5667/5668 automatically corrects the IF and RF response when you set the Digital IF Equalization Enabled property to TRUE. If you are using external digitizer mode, you can use information returned from this VI to correct your measurement. |
| niRFSA_Init | Creates a new session for the device. This function sends initialization commands to reset all hardware modules to a known state necessary for NI-RFSA operation. |
| niRFSA_InitWithOptions | Creates a new session for the device. |

#### Attachments

None

Parent topic:

niRFSA.h

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions_1ga790a63d6ecd99ed7842f52d1044e53cc.html language=enus -->
## TOPIC 00084: niRFSA_InitWithOptions

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions_1ga790a63d6ecd99ed7842f52d1044e53cc.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions_1ga790a63d6ecd99ed7842f52d1044e53cc.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new session for the device. SyntaxViStatus _VI_FUNC niRFSA_InitWithOptions(ViRsrc resourceName, ViBoolean idQuery, ViBoolean reset, ViConstString optionString, ViSession *vi)RemarksThis function sets the initial value of certain attributes and sends initialization commands to reset all har

### niRFSA_InitWithOptions

Creates a new session for the device.

#### Syntax

ViStatus _VI_FUNC niRFSA_InitWithOptions(ViRsrc resourceName, ViBoolean idQuery, ViBoolean reset, ViConstString optionString, ViSession *vi)

#### Remarks

This function sets the initial value of certain attributes and sends initialization commands to reset all hardware modules to a known state necessary for NI-RFSA operation.

To create a new session, pass the downconverter resource name for the RF vector signal analyzer to the **resource name** parameter.

You can access the device session this VI creates using the NI-RFSA Soft Front Panel (SFP). Accessing the device session with the SFP can help you debug your code. Refer to [Debugging Your Application Using SFP Session Access](https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/using_session_access_sfp_top.html) for more information about accessing your session with the SFP.

Note

Before initializing your device, you must first associate the modules that comprise your device in MAX. After associating the modules, pass the resource name of the device to this function to initialize all the modules. Refer to [Associating NI-RFSA Modules](https://www.ni.com/docs/en-US/bundle/ni-rfsa-max/page/maxrfsa/mi_rf_associating.html) for information about MAX association.

Note

For multichannel devices such as the PXIe-5860, the resource name must include the channel number to use. The channel number is specified by appending *ChannelNumber* to the device name, where *ChannelNumber* is the channel number (0, 1, etc.). For example, if the device name is PXI1Slot2 and you want to use channel 0, use the resource name PXI1Slot2/0.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Driver Setup Options](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/driver-setup-options.html)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| resourceName | [in] | ViRsrc | Specifies the resource name of the device to initialize.For NI-RFSA devices, the syntax is the device name specified in MAX. The typical default name for your device in MAX is PXI1Slot2. You can rename your device by right-clicking the name in MAX, selecting Rename from the drop-down menu, and entering a new name. You can also pass in the name of an IVI logical name configured with the IVI Configuration utility. For additional information, refer to the Installed Devices IVI topic of the Measurement & Automation Explorer Help.Device names are not case-sensitive. However, IVI logical names are case-sensitive. If you use an IVI logical name, verify the name is identical to the name shown in the IVI Configuration Utility. |
| idQuery | [in] | ViBoolean | Specifies whether NI-RFSA performs an ID query. When you perform an ID query, NI-RFSA verifies the device you initialize is supported.ValueDescriptionVI_TRUE (Yes)Perform an ID query. This value is the default.VI_FALSE (No)Do not perform an ID query. |
| Value | Description |  |  |
| VI_TRUE (Yes) | Perform an ID query. This value is the default. |  |  |
| VI_FALSE (No) | Do not perform an ID query. |  |  |
| reset | [in] | ViBoolean | Specifies whether the NI-RFSA device is reset during the initialization procedure.ValueDescriptionVI_TRUE (Yes)The device is reset.VI_FALSE (No)The device is not reset. This value is the default. |
| Value | Description |  |  |
| VI_TRUE (Yes) | The device is reset. |  |  |
| VI_FALSE (No) | The device is not reset. This value is the default. |  |  |
| optionString | [in] | ViConstString | Sets the initial value of certain attributes for the session. The attributes shown in the following table are used in this parameter.NameAttributeRangeCheckNIRFSA_ATTR_RANGE_CHECKQueryInstrStatusNIRFSA_ATTR_QUERY_INSTRUMENT_STATUSCacheNIRFSA_ATTR_CACHERecordCoercionsNIRFSA_ATTR_RECORD_COERCIONSDriverSetupNIRFSA_ATTR_DRIVER_SETUPSimulateNIRFSA_ATTR_SIMULATEThe format of this string is *"AttributeName=Value"*, where AttributeName is the name of the attribute and Value is the value to which the attribute will be set. For example, you can simulate the PXIe-5663 using the following strings:*"Simulate=1, DriverSetup=Model:5663E"*.*"Simulate=1, DriverSetup=Model:5601*; *Digitizer:5622; LO:5652; LOBoardType:PXIe"*.To set multiple attributes, separate their assignments with a comma.Refer to Driver Setup Options for more information about the driver setup string.Note: To simulate a device using the PXIe-5622 25 MHz digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1. You can set the Digitizer field to 5622_25MHz_DDC only when using the PXIe-5665. |
| Name | Attribute |  |  |
| RangeCheck | NIRFSA_ATTR_RANGE_CHECK |  |  |
| QueryInstrStatus | NIRFSA_ATTR_QUERY_INSTRUMENT_STATUS |  |  |
| Cache | NIRFSA_ATTR_CACHE |  |  |
| RecordCoercions | NIRFSA_ATTR_RECORD_COERCIONS |  |  |
| DriverSetup | NIRFSA_ATTR_DRIVER_SETUP |  |  |
| Simulate | NIRFSA_ATTR_SIMULATE |  |  |
| vi | [out] | ViSession * | Identifies your instrument session. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions_1gaf8504d85ab0c381b1dd8061f667f34c5.html language=enus -->
## TOPIC 00085: niRFSA_Close

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions_1gaf8504d85ab0c381b1dd8061f667f34c5.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions_1gaf8504d85ab0c381b1dd8061f667f34c5.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the session to the device. SyntaxViStatus _VI_FUNC niRFSA_Close(ViSession vi)RemarksIf you close a session that has Soft Front Panel (SFP) session access enabled, any application connected to the shared device session is no longer usable. Refer to Debugging Your Application Using SFP Session

### niRFSA_Close

Closes the session to the device.

#### Syntax

ViStatus _VI_FUNC niRFSA_Close(ViSession vi)

#### Remarks

If you close a session that has Soft Front Panel (SFP) session access enabled, any application connected to the shared device session is no longer usable. Refer to [Debugging Your Application Using SFP Session Access](https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/using_session_access_sfp_top.html) for more information about using SFP session access.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__acquisition.html language=enus -->
## TOPIC 00086: Acquisition

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__acquisition.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__acquisition.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsIQ AcquisitionSpectrum AcquisitionGroup membersNoneAttachmentsNone

### Acquisition

#### Groups

- IQ Acquisition
- Spectrum Acquisition

#### Group members

None

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__acquisition__iq__acquisition__multirecord__acquisition_1ga493a6578f05e27eaacc3c6136dbfc6fd.html language=enus -->
## TOPIC 00087: niRFSA_FetchIqMultiRecordComplexF32

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__acquisition__iq__acquisition__multirecord__acquisition_1ga493a6578f05e27eaacc3c6136dbfc6fd.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__acquisition__iq__acquisition__multirecord__acquisition_1ga493a6578f05e27eaacc3c6136dbfc6fd.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches I/Q data from multiple records in an acquisition. SyntaxViStatus _VI_FUNC niRFSA_FetchIqMultiRecordComplexF32(ViSession vi, ViConstString channelList, ViInt64 startingRecord, ViInt64 numberOfRecords, ViInt64 numberOfSamples, ViReal64 timeout, ni complex number f32 *data, niRFSA_wfmInfo *wfmI

### niRFSA_FetchIqMultiRecordComplexF32

Fetches I/Q data from multiple records in an acquisition.

#### Syntax

ViStatus _VI_FUNC niRFSA_FetchIqMultiRecordComplexF32(ViSession vi, ViConstString channelList, ViInt64 startingRecord, ViInt64 numberOfRecords, ViInt64 numberOfSamples, ViReal64 timeout, ni complex number f32 *data, niRFSA_wfmInfo *wfmInfo)

#### Remarks

A fetch transfers acquired waveform data from device memory to computer memory. The data was acquired to onboard memory previously by the hardware after the acquisition was initiated.

This function is not necessary if you use the [niRFSA_ReadIqSingleRecordComplexF64](group____root__ni_r_f_s_a__functions__acquisition__iq__acquisition__single__record__acquisition_1gab75a8b7514cc0e168bb75fd170013b8d.html) function because the [niRFSA_ReadIqSingleRecordComplexF64](group____root__ni_r_f_s_a__functions__acquisition__iq__acquisition__single__record__acquisition_1gab75a8b7514cc0e168bb75fd170013b8d.html) function performs the fetch as part of the function.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[None (Trigger Type)](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| channelList | [in] | ViConstString | Identifies which channels to apply settings. Specify an empty string as the value of this parameter. |
| startingRecord | [in] | ViInt64 | Specifies the first record to retrieve. Record numbers are zero-based. The default value is 0. |
| numberOfRecords | [in] | ViInt64 | Specifies the number of records to fetch. |
| numberOfSamples | [in] | ViInt64 | Specifies the number of samples per record. |
| timeout | [in] | ViReal64 | PXI-5661, PXIe-5663/5665/5667 Specifies the time, in seconds, allotted for the function to complete before returning a timeout error.PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Specifies the time, in seconds, allotted to receive the reference trigger.For all supported devices, a value of specifies the function waits until all data is available. A value of 0 specifies the function immediately returns available data. |
| data | [out] | ni complex number f32 * | Returns the acquired waveform for each record fetched. The waveforms are written sequentially in the array. Allocate an array at least as large as numberOfSamples times numberOfRecords for this parameter. |
| wfmInfo | [out] | niRFSA_wfmInfo * | Contains the absolute and relative timestamps for the operation, the time interval (dt), and the actual number of samples read. Each element of this array corresponds to a record.The following list provides more information about each of these properties:absolute timestamp Returns the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions.The value of the absolute timestamp returned is always 0 for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5840/5841/5842/5860.relative timestamp Returns a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred.The value of the relative timestamp returned is always 0 for the PXIe-5644/5645/5646.dt Returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value.actual samples read Returns an integer representing the number of samples in the waveform.The actual number of samples for each record can vary if the NIRFSA ATTR NUMBER OF SAMPLES attribute changes per step during RF list mode.offset Returns the offset to scale data, (b), in mx + b form.gain Returns the gain to scale data, (m), in mx + b form. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Multirecord Acquisition

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__acquisition__iq__acquisition__multirecord__acquisition_1ga68c00823ac4846338f1ee60269b82e06.html language=enus -->
## TOPIC 00088: niRFSA_FetchIqMultiRecordComplexI16

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__acquisition__iq__acquisition__multirecord__acquisition_1ga68c00823ac4846338f1ee60269b82e06.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__acquisition__iq__acquisition__multirecord__acquisition_1ga68c00823ac4846338f1ee60269b82e06.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches binary I/Q data from multiple records in an acquisition. SyntaxViStatus _VI_FUNC niRFSA_FetchIqMultiRecordComplexI16(ViSession vi, ViConstString channelList, ViInt64 startingRecord, ViInt64 numberOfRecords, ViInt64 numberOfSamples, ViReal64 timeout, ni complex number i16 *data, niRFSA_wfmInf

### niRFSA_FetchIqMultiRecordComplexI16

Fetches binary I/Q data from multiple records in an acquisition.

#### Syntax

ViStatus _VI_FUNC niRFSA_FetchIqMultiRecordComplexI16(ViSession vi, ViConstString channelList, ViInt64 startingRecord, ViInt64 numberOfRecords, ViInt64 numberOfSamples, ViReal64 timeout, ni complex number i16 *data, niRFSA_wfmInfo *wfmInfo)

#### Remarks

Fetching transfers acquired waveform data from device memory to computer memory. The data was acquired to onboard memory previously by the hardware after the acquisition was initiated.

This function is not necessary if you use the [niRFSA_ReadIqSingleRecordComplexF64](group____root__ni_r_f_s_a__functions__acquisition__iq__acquisition__single__record__acquisition_1gab75a8b7514cc0e168bb75fd170013b8d.html) function because the [niRFSA_ReadIqSingleRecordComplexF64](group____root__ni_r_f_s_a__functions__acquisition__iq__acquisition__single__record__acquisition_1gab75a8b7514cc0e168bb75fd170013b8d.html) function performs the fetch as part of the function.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[None (Trigger Type)](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| channelList | [in] | ViConstString | Identifies which channels to apply settings. Specify an empty string as the value of this parameter. |
| startingRecord | [in] | ViInt64 | Specifies the first record to retrieve. Record numbers are zero-based. The default value is 0. |
| numberOfRecords | [in] | ViInt64 | Specifies the number of records to fetch. |
| numberOfSamples | [in] | ViInt64 | Specifies the number of samples per record. |
| timeout | [in] | ViReal64 | PXI-5661, PXIe-5663/5665/5667 Specifies the time, in seconds, allotted for the function to complete before returning a timeout error.PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Specifies the time, in seconds, allotted to receive the reference trigger.For all supported devices, a value of specifies the function waits until all data is available. A value of 0 specifies the function immediately returns available data. |
| data | [out] | ni complex number i16 * | Returns the acquired waveform for each record fetched. The waveforms are written sequentially in the array. Allocate an array at least as large as numberOfSamples times numberOfRecords for this parameter. |
| wfmInfo | [out] | niRFSA_wfmInfo * | Contains the absolute and relative timestamps for the operation, the time interval (dt), and the actual number of samples read. Each element of this array corresponds to a record.The following list provides more information about each of these properties:absolute timestamp Returns the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions.The value of the absolute timestamp returned is always 0 for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860.relative timestamp Returns a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred.The value of the relative timestamp returned is always 0 for the PXIe-5644/5645/5646.dt Returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value.actual samples read Returns an integer representing the number of samples in the waveform.The actual number of samples for each record can vary if the NIRFSA ATTR NUMBER OF SAMPLES attribute changes per step during RF list mode.offset Returns the offset to scale data, (b), in mx + b form.gain Returns the gain to scale data, (m), in mx + b form. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Multirecord Acquisition

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__calibration.html language=enus -->
## TOPIC 00089: Calibration

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__calibration.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__calibration.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsCalibration ControlCalibration UtilityGroup membersNameDescriptionniRFSA_CloseExtCalCloses an NI-RFSA external calibration session and, if specified, stores the new calibration constants and calibration data, such as time and temperature, in the onboard EEPROM. niRFSA_CloseExternalAlignmentClo

### Calibration

#### Groups

- Calibration Control
- Calibration Utility

#### Group members

| Name | Description |
| --- | --- |
| niRFSA_CloseExtCal | Closes an NI-RFSA external calibration session and, if specified, stores the new calibration constants and calibration data, such as time and temperature, in the onboard EEPROM. |
| niRFSA_CloseExternalAlignment | Closes an NI-RFSA external alignment session and, if specified, stores the new calibration constants and calibration data, such as time and temperature, in the onboard EEPROM. |
| niRFSA_InitExtCal | Creates and initializes a special NI-RFSA external calibration session. |
| niRFSA_InitializeExternalAlignment | Creates and initializes a special NI-RFSA external alignment session. |
| niRFSA_IsSelfCalValid | Indicates which calibration steps contain valid calibration data. |
| niRFSA_SelfCalibrate | Self-calibrates the NI-RFSA device and associated modules that support self-calibration. |
| niRFSA_SelfCalibrateRange | Self-calibrates all configurations within the specified frequency and reference level limits. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__calibration_1ga87aaecb3b84e5aa3bcb534b7417dacbc.html language=enus -->
## TOPIC 00090: niRFSA_IsSelfCalValid

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__calibration_1ga87aaecb3b84e5aa3bcb534b7417dacbc.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__calibration_1ga87aaecb3b84e5aa3bcb534b7417dacbc.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates which calibration steps contain valid calibration data. SyntaxViStatus _VI_FUNC niRFSA_IsSelfCalValid(ViSession vi, ViBoolean *selfCalValid, ViInt64 *validSteps)RemarksTo omit steps with valid calibration data from self-calibration, you can pass the validSteps parameter to the stepsToOmit

### niRFSA_IsSelfCalValid

Indicates which calibration steps contain valid calibration data.

#### Syntax

ViStatus _VI_FUNC niRFSA_IsSelfCalValid(ViSession vi, ViBoolean *selfCalValid, ViInt64 *validSteps)

#### Remarks

To omit steps with valid calibration data from self-calibration, you can pass the **validSteps** parameter to the **stepsToOmit** parameter of the [niRFSA_SelfCalibrate](group____root__ni_r_f_s_a__functions__calibration_1ga003afd50781c22b5e3e187aca253a3b2.html) function.

**Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| selfCalValid | [out] | ViBoolean * | Returns VI_TRUE if all the calibration data is valid and VI_FALSE if any of the calibration data is invalid. |
| validSteps | [out] | ViInt64 * | Returns valid steps. If two or more calibration steps are valid, this parameter returns a bitwise-OR combination of the calibration steps. For example, if both NIRFSA_VAL_SELF_CAL_IF_FLATNESS and NIRFSA_VAL_SELF_CAL_LO_SELF_CAL steps are valid, NI-RFSA returns the following string:NIRFSA_VAL_SELF_CAL_IF_FLATNESS \|NIRFSA_VAL_SELF_CAL_LO_SELF_CALNameValueDescriptionNIRFSA_VAL_SELF_CAL_PRESELECTOR_ALIGNMENT1 (0x1)Calls for preselector alignment.NIRFSA_VAL_SELF_CAL_GAIN_REFERENCE2 (0x2)Measures the changes in gain since the last external calibration was run.NIRFSA_VAL_SELF_CAL_IF_FLATNESS4 (0x4)Measures the IF response of the entire system for each of the supported IF filtersNIRFSA_VAL_SELF_CAL_DIGITIZER_SELF_CAL8 (0x8)Calls for digitizer self-calibration, if the digitizer is associated with the RF downconverter.NIRFSA_VAL_SELF_CAL_LO_SELF_CAL16 (0x10)Calls for LO self-calibration, if the LO source module is associated with the RF downconverter.NIRFSA_VAL_SELF_CAL_AMPLITUDE_ACCURACY32 (0x20)Selects the Amplitude Accuracy self-calibration step.NIRFSA_VAL_SELF_CAL_RESIDUAL_LO_POWER64 (0x40)Selects the Residual LO Power self-calibration step.NIRFSA_VAL_SELF_CAL_IMAGE_SUPPRESSION128 (0x80)Selects the Image Suppression self-calibration step.NIRFSA_VAL_SELF_CAL_SYNTHESIZER_ALIGNMENT256 (0x100)Selects the Synthesizer Alignment self-calibration step.NIRFSA_VAL_SELF_CAL_DC_OFFSET512 (0x200)Selects the DC Offset self-calibration step. |
| Name | Value | Description |  |
| NIRFSA_VAL_SELF_CAL_PRESELECTOR_ALIGNMENT | 1 (0x1) | Calls for preselector alignment. |  |
| NIRFSA_VAL_SELF_CAL_GAIN_REFERENCE | 2 (0x2) | Measures the changes in gain since the last external calibration was run. |  |
| NIRFSA_VAL_SELF_CAL_IF_FLATNESS | 4 (0x4) | Measures the IF response of the entire system for each of the supported IF filters |  |
| NIRFSA_VAL_SELF_CAL_DIGITIZER_SELF_CAL | 8 (0x8) | Calls for digitizer self-calibration, if the digitizer is associated with the RF downconverter. |  |
| NIRFSA_VAL_SELF_CAL_LO_SELF_CAL | 16 (0x10) | Calls for LO self-calibration, if the LO source module is associated with the RF downconverter. |  |
| NIRFSA_VAL_SELF_CAL_AMPLITUDE_ACCURACY | 32 (0x20) | Selects the Amplitude Accuracy self-calibration step. |  |
| NIRFSA_VAL_SELF_CAL_RESIDUAL_LO_POWER | 64 (0x40) | Selects the Residual LO Power self-calibration step. |  |
| NIRFSA_VAL_SELF_CAL_IMAGE_SUPPRESSION | 128 (0x80) | Selects the Image Suppression self-calibration step. |  |
| NIRFSA_VAL_SELF_CAL_SYNTHESIZER_ALIGNMENT | 256 (0x100) | Selects the Synthesizer Alignment self-calibration step. |  |
| NIRFSA_VAL_SELF_CAL_DC_OFFSET | 512 (0x200) | Selects the DC Offset self-calibration step. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calibration

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__calibration_1gaff27a3a3c4be5e3ecc54a42791b70d3d.html language=enus -->
## TOPIC 00091: niRFSA_CloseExternalAlignment

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__calibration_1gaff27a3a3c4be5e3ecc54a42791b70d3d.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__calibration_1gaff27a3a3c4be5e3ecc54a42791b70d3d.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an NI-RFSA external alignment session and, if specified, stores the new calibration constants and calibration data, such as time and temperature, in the onboard EEPROM. SyntaxViStatus _VI_FUNC niRFSA_CloseExternalAlignment(ViSession vi, ViInt32 action)RemarksSupported Devices: PXIe-5605 (PXIe

### niRFSA_CloseExternalAlignment

Closes an NI-RFSA external alignment session and, if specified, stores the new calibration constants and calibration data, such as time and temperature, in the onboard EEPROM.

#### Syntax

ViStatus _VI_FUNC niRFSA_CloseExternalAlignment(ViSession vi, ViInt32 action)

#### Remarks

**Supported Devices**: PXIe-5605 (PXIe-5665 only), PXIe-5606 (PXIe-5668 only)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_InitializeExternalAlignment function and identifies a particular instrument session. |
| action | [in] | ViInt32 | Specifies how to use the alignment values from this session as the session is closed.ValueDescriptionNIRFSA_VAL_EXT_CAL_ABORTThe old alignment constants are kept, and the new ones are discarded.NIRFSA_VAL_EXT_CAL_COMMITThe new alignment constants are stored in the EEPROM. |
| Value | Description |  |  |
| NIRFSA_VAL_EXT_CAL_ABORT | The old alignment constants are kept, and the new ones are discarded. |  |  |
| NIRFSA_VAL_EXT_CAL_COMMIT | The new alignment constants are stored in the EEPROM. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calibration

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__calibration__calibration__control.html language=enus -->
## TOPIC 00092: Calibration Control

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__calibration__calibration__control.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__calibration__calibration__control.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNI 5601NI 5665NI 5693NI 5698Group membersNameDescriptionniRFSA_CloseCalibrationStepCloses the current calibration step. niRFSA_CloseExternalAlignmentStepCloses an EEPROM-specific external alignment step. niRFSA_InitializeCalibrationStepInitializes an EEPROM-specific calibration step. niRFSA_In

### Calibration Control

#### Groups

- NI 5601
- NI 5665
- NI 5693
- NI 5698

#### Group members

| Name | Description |
| --- | --- |
| niRFSA_CloseCalibrationStep | Closes the current calibration step. |
| niRFSA_CloseExternalAlignmentStep | Closes an EEPROM-specific external alignment step. |
| niRFSA_InitializeCalibrationStep | Initializes an EEPROM-specific calibration step. |
| niRFSA_InitializeExternalAlignmentStep | Initializes an EEPROM-specific external alignment step. |

#### Attachments

None

Parent topic:

Calibration

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__calibration__calibration__control_1gaad6fd698ea76e1e66917bd72d3769b42.html language=enus -->
## TOPIC 00093: niRFSA_InitializeExternalAlignmentStep

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__calibration__calibration__control_1gaad6fd698ea76e1e66917bd72d3769b42.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__calibration__calibration__control_1gaad6fd698ea76e1e66917bd72d3769b42.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes an EEPROM-specific external alignment step. SyntaxViStatus _VI_FUNC niRFSA_InitializeExternalAlignmentStep(ViSession vi, ViInt64 externalAlignmentStep)RemarksSupported Devices: PXIe-5605 (PXIe-5665 only), PXIe-5606 (PXIe-5668 only)ParametersNameDirectionTypeDescriptionvi[in]ViSessionIden

### niRFSA_InitializeExternalAlignmentStep

Initializes an EEPROM-specific external alignment step.

#### Syntax

ViStatus _VI_FUNC niRFSA_InitializeExternalAlignmentStep(ViSession vi, ViInt64 externalAlignmentStep)

#### Remarks

**Supported Devices**: PXIe-5605 (PXIe-5665 only), PXIe-5606 (PXIe-5668 only)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_InitializeExternalAlignment function and identifies a particular instrument session. |
| externalAlignmentStep | [in] | ViInt64 | Specifies which external alignment step you want to initialize.ValueDescriptionEXT ALIGNMENT PRESELECTORInitiates preselector alignment. This step generates coefficients to align the preselector across the frequency range of 3.6 GHz to 14 GHz. |
| Value | Description |  |  |
| EXT ALIGNMENT PRESELECTOR | Initiates preselector alignment. This step generates coefficients to align the preselector across the frequency range of 3.6 GHz to 14 GHz. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calibration Control

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__calibration__calibration__control_1gaba2a0882d4f67c74e3ed6ac268bae7ef.html language=enus -->
## TOPIC 00094: niRFSA_CloseExternalAlignmentStep

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__calibration__calibration__control_1gaba2a0882d4f67c74e3ed6ac268bae7ef.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__calibration__calibration__control_1gaba2a0882d4f67c74e3ed6ac268bae7ef.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an EEPROM-specific external alignment step. SyntaxViStatus _VI_FUNC niRFSA_CloseExternalAlignmentStep(ViSession vi)RemarksSupported Devices: PXIe-5605 (PXIe-5665 only), PXIe-5606 (PXIe-5668 only)ParametersNameDirectionTypeDescriptionvi[in]ViSessionIdentifies your instrument session. vi is obt

### niRFSA_CloseExternalAlignmentStep

Closes an EEPROM-specific external alignment step.

#### Syntax

ViStatus _VI_FUNC niRFSA_CloseExternalAlignmentStep(ViSession vi)

#### Remarks

**Supported Devices**: PXIe-5605 (PXIe-5665 only), PXIe-5606 (PXIe-5668 only)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_InitializeExternalAlignment function and identifies a particular instrument session. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calibration Control

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__calibration__calibration__control__ni__5601.html language=enus -->
## TOPIC 00095: NI 5601

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__calibration__calibration__control__ni__5601.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__calibration__calibration__control__ni__5601.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniRFSA_CalAdjustIfAttenuationCalibrationSpecifies the IF attenuation settings. niRFSA_CalAdjustIfResponseCalibrationSpecifies the IF response settings. niRFSA_CalAdjustRefLevelCalibrationWrites the reference level calibration data settings to the driver. niRFSA_

### NI 5601

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niRFSA_CalAdjustIfAttenuationCalibration | Specifies the IF attenuation settings. |
| niRFSA_CalAdjustIfResponseCalibration | Specifies the IF response settings. |
| niRFSA_CalAdjustRefLevelCalibration | Writes the reference level calibration data settings to the driver. |
| niRFSA_CalSetTemperature | Writes the calibration temperature to the driver. |

#### Attachments

None

Parent topic:

Calibration Control

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__calibration__calibration__control__ni__5601_1ga110763199cfb5195c921cb410d32e166.html language=enus -->
## TOPIC 00096: niRFSA_CalSetTemperature

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__calibration__calibration__control__ni__5601_1ga110763199cfb5195c921cb410d32e166.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__calibration__calibration__control__ni__5601_1ga110763199cfb5195c921cb410d32e166.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes the calibration temperature to the driver. SyntaxViStatus _VI_FUNC niRFSA_CalSetTemperature(ViSession vi, ViConstString channelList, ViReal64 temperature)RemarksSupported Devices: PXIe-5601ParametersNameDirectionTypeDescriptionvi[in]ViSessionIdentifies your instrument session. vi is obtained

### niRFSA_CalSetTemperature

Writes the calibration temperature to the driver.

#### Syntax

ViStatus _VI_FUNC niRFSA_CalSetTemperature(ViSession vi, ViConstString channelList, ViReal64 temperature)

#### Remarks

**Supported Devices**: PXIe-5601

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_InitExtCal function and identifies a particular instrument session. |
| channelList | [in] | ViConstString | Identifies which channels to apply settings. Specify an empty string as the value of this parameter. |
| temperature | [in] | ViReal64 | Specifies the calibration temperature, in degrees Celsius. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

NI 5601

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__calibration__calibration__control__ni__5601_1ga163e28f3492eda27595588ae04d9ece6.html language=enus -->
## TOPIC 00097: niRFSA_CalAdjustIfResponseCalibration

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__calibration__calibration__control__ni__5601_1ga163e28f3492eda27595588ae04d9ece6.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__calibration__calibration__control__ni__5601_1ga163e28f3492eda27595588ae04d9ece6.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the IF response settings. SyntaxViStatus _VI_FUNC niRFSA_CalAdjustIfResponseCalibration(ViSession vi, ViConstString channelList, ViInt32 ifFilter, ViReal64 rfFrequency, ViReal64 bandWidth, ViInt32 numberOfMeasurements, ViReal64 *measurements)RemarksSupported Devices: PXIe-5601, PXIe-5694Pa

### niRFSA_CalAdjustIfResponseCalibration

Specifies the IF response settings.

#### Syntax

ViStatus _VI_FUNC niRFSA_CalAdjustIfResponseCalibration(ViSession vi, ViConstString channelList, ViInt32 ifFilter, ViReal64 rfFrequency, ViReal64 bandWidth, ViInt32 numberOfMeasurements, ViReal64 *measurements)

#### Remarks

**Supported Devices**: PXIe-5601, PXIe-5694

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_InitExtCal function and identifies a particular instrument session. |
| channelList | [in] | ViConstString | Identifies which channels to apply settings. Specify an empty string as the value of this parameter. |
| ifFilter | [in] | ViInt32 | Specifies the IF filter used by the downconverter.ValueDescriptionNIRFSA_VAL_187_5_MHZ_NARROW (1400)Uses the 187.5 MHz wide bandwidth path.NIRFSA_VAL_187_5_MHZ_NARROW (1401)Uses the 187.5 MHz narrow bandwidth path.NIRFSA_VAL_53_MHZ (1402)Uses the 53 MHz path.NIRFSA_VAL_BYPASS (1403)Bypasses the IF path. |
| Value | Description |  |  |
| NIRFSA_VAL_187_5_MHZ_NARROW (1400) | Uses the 187.5 MHz wide bandwidth path. |  |  |
| NIRFSA_VAL_187_5_MHZ_NARROW (1401) | Uses the 187.5 MHz narrow bandwidth path. |  |  |
| NIRFSA_VAL_53_MHZ (1402) | Uses the 53 MHz path. |  |  |
| NIRFSA_VAL_BYPASS (1403) | Bypasses the IF path. |  |  |
| rfFrequency | [in] | ViReal64 | Specifies the RF frequency, in Hz, used during the IF response adjustment. |
| bandWidth | [in] | ViReal64 | Specifies the bandwidth, in Hz, to use for the IF response adjustment. |
| numberOfMeasurements | [in] | ViInt32 | Specifies the number of measurements to make. |
| measurements | [out] | ViReal64 * | Specifies the relevant measurements taken for each IF filter configuration, in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

NI 5601

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__calibration__calibration__control__ni__5601_1ga1ff155735a0306248871da6689b09a3d.html language=enus -->
## TOPIC 00098: niRFSA_CalAdjustIfAttenuationCalibration

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__calibration__calibration__control__ni__5601_1ga1ff155735a0306248871da6689b09a3d.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__calibration__calibration__control__ni__5601_1ga1ff155735a0306248871da6689b09a3d.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the IF attenuation settings. SyntaxViStatus _VI_FUNC niRFSA_CalAdjustIfAttenuationCalibration(ViSession vi, ViConstString channelList, ViInt32 ifFilter, ViInt32 numberOfAttenuators, ViReal64 *attenuatorSettings, ViReal64 measurement)RemarksSupported Devices: PXIe-5601, PXIe-5694ParametersN

### niRFSA_CalAdjustIfAttenuationCalibration

Specifies the IF attenuation settings.

#### Syntax

ViStatus _VI_FUNC niRFSA_CalAdjustIfAttenuationCalibration(ViSession vi, ViConstString channelList, ViInt32 ifFilter, ViInt32 numberOfAttenuators, ViReal64 *attenuatorSettings, ViReal64 measurement)

#### Remarks

**Supported Devices**: PXIe-5601, PXIe-5694

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_InitExtCal function and identifies a particular instrument session. |
| channelList | [in] | ViConstString | Identifies which channels to apply settings. Specify an empty string as the value of this parameter. |
| ifFilter | [in] | ViInt32 | Specifies the IF filter used by the downconverter.ValueDescriptionNIRFSA_VAL_187_5_MHZ_NARROW (1400)Uses the 187.5 MHz wide bandwidth filter.NIRFSA_VAL_187_5_MHZ_NARROW (1401)Uses the 187.5 MHz narrow bandwidth filter.NIRFSA_VAL_53_MHZ (1402)Uses the 53 MHz filter.NIRFSA_VAL_BYPASS (1403)Bypasses the IF filter. |
| Value | Description |  |  |
| NIRFSA_VAL_187_5_MHZ_NARROW (1400) | Uses the 187.5 MHz wide bandwidth filter. |  |  |
| NIRFSA_VAL_187_5_MHZ_NARROW (1401) | Uses the 187.5 MHz narrow bandwidth filter. |  |  |
| NIRFSA_VAL_53_MHZ (1402) | Uses the 53 MHz filter. |  |  |
| NIRFSA_VAL_BYPASS (1403) | Bypasses the IF filter. |  |  |
| numberOfAttenuators | [in] | ViInt32 | Specifies the number of attenuators to use during the IF attenuation adjustment. |
| attenuatorSettings | [out] | ViReal64 * | Specifies the IF attenuator settings for the measurement. The first element in the array corresponds with IF1, the next element corresponds to IF2, and so on. |
| measurement | [in] | ViReal64 | Specifies the relevant measurement taken for the current configuration. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

NI 5601

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__calibration__calibration__utility_1ga08f78f6025eff00a19cf369961758bc6.html language=enus -->
## TOPIC 00099: niRFSA_GetExtCalLastTemp

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__calibration__calibration__utility_1ga08f78f6025eff00a19cf369961758bc6.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__calibration__calibration__utility_1ga08f78f6025eff00a19cf369961758bc6.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the temperature of the last successful external calibration. SyntaxViStatus _VI_FUNC niRFSA_GetExtCalLastTemp(ViSession vi, ViReal64 *temperature)RemarksThe temperature is returned in degrees Celsius.Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5

### niRFSA_GetExtCalLastTemp

Returns the temperature of the last successful external calibration.

#### Syntax

ViStatus _VI_FUNC niRFSA_GetExtCalLastTemp(ViSession vi, ViReal64 *temperature)

#### Remarks

The temperature is returned in degrees Celsius.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init, niRFSA_InitWithOptions, or niRFSA_InitExtCal function and identifies a particular instrument session. |
| temperature | [out] | ViReal64 * | Returns the temperature, in degrees Celsius, of the last external calibration. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calibration Utility

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__calibration__calibration__utility_1ga5a2f55af6e8e23406442a416870998e0.html language=enus -->
## TOPIC 00100: niRFSA_ChangeExtCalPassword

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__calibration__calibration__utility_1ga5a2f55af6e8e23406442a416870998e0.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__calibration__calibration__utility_1ga5a2f55af6e8e23406442a416870998e0.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes the password that is required to initialize an external calibration session. SyntaxViStatus _VI_FUNC niRFSA_ChangeExtCalPassword(ViSession vi, ViConstString oldPassword, ViConstString newPassword)RemarksSupported Devices: PXIe-5601/5603/5605/5606, PXIe-5693/5694/5698, PXIe-5820/5830/5831/583

### niRFSA_ChangeExtCalPassword

Changes the password that is required to initialize an external calibration session.

#### Syntax

ViStatus _VI_FUNC niRFSA_ChangeExtCalPassword(ViSession vi, ViConstString oldPassword, ViConstString newPassword)

#### Remarks

**Supported Devices**: PXIe-5601/5603/5605/5606, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function and identifies a particular instrument session. |
| oldPassword | [in] | ViConstString | Specifies the old (current) external calibration password.The maximum length of the password varies by device. |
| newPassword | [in] | ViConstString | Specifies the new (desired) external calibration password.The maximum length of the password varies by device. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calibration Utility

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__calibration__calibration__utility_1ga6744a944f42e8a569e09383dae9a9ba8.html language=enus -->
## TOPIC 00101: niRFSA_GetExtCalLastDateAndTime

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__calibration__calibration__utility_1ga6744a944f42e8a569e09383dae9a9ba8.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__calibration__calibration__utility_1ga6744a944f42e8a569e09383dae9a9ba8.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the date and time of the last successful external calibration. SyntaxViStatus _VI_FUNC niRFSA_GetExtCalLastDateAndTime(ViSession vi, ViInt32 *year, ViInt32 *month, ViInt32 *day, ViInt32 *hour, ViInt32 *minute)RemarksThe time returned is 24-hour local time, and the date is returned as integer

### niRFSA_GetExtCalLastDateAndTime

Returns the date and time of the last successful external calibration.

#### Syntax

ViStatus _VI_FUNC niRFSA_GetExtCalLastDateAndTime(ViSession vi, ViInt32 *year, ViInt32 *month, ViInt32 *day, ViInt32 *hour, ViInt32 *minute)

#### Remarks

The time returned is 24-hour local time, and the date is returned as integer values. For example, if the device was calibrated at 2:30 PM on December 31, 2010, this function returns 14 for the **hour** parameter, 30 for the **minute** parameter, 12 for the **month** parameter, 31 for the **day** parameter, and 2010 for the **year** parameter.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init, niRFSA_InitWithOptions, or niRFSA_InitExtCal function and identifies a particular instrument session. |
| year | [out] | ViInt32 * | Returns the year of the last external calibration. |
| month | [out] | ViInt32 * | Returns the month of the last external calibration. |
| day | [out] | ViInt32 * | Returns the day of the last external calibration. |
| hour | [out] | ViInt32 * | Returns the hour of the last external calibration. |
| minute | [out] | ViInt32 * | Returns the minute of the last external calibration. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calibration Utility

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__calibration__calibration__utility_1gae7c88a4013de06652070ae97c4c14f56.html language=enus -->
## TOPIC 00102: niRFSA_GetCalUserDefinedInfoMaxSize

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__calibration__calibration__utility_1gae7c88a4013de06652070ae97c4c14f56.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__calibration__calibration__utility_1gae7c88a4013de06652070ae97c4c14f56.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of characters of user-defined information that can be stored in the device onboard EEPROM. SyntaxViStatus _VI_FUNC niRFSA_GetCalUserDefinedInfoMaxSize(ViSession vi, ViInt32 *infoSize)RemarksSupported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661,

### niRFSA_GetCalUserDefinedInfoMaxSize

Returns the number of characters of user-defined information that can be stored in the device onboard EEPROM.

#### Syntax

ViStatus _VI_FUNC niRFSA_GetCalUserDefinedInfoMaxSize(ViSession vi, ViInt32 *infoSize)

#### Remarks

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init, niRFSA_InitWithOptions, or niRFSA_InitExtCal function and identifies a particular instrument session. |
| infoSize | [out] | ViInt32 * | Returns the number of characters of user-defined information that can be stored in the device onboard EEPROM. The maximum size of the user-defined information array is 21 characters. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calibration Utility

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration.html language=enus -->
## TOPIC 00103: Configuration

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsClockConfiguration ListDe-embeddingIQSet/Get/Reset AttributeSpectrumTriggerGroup membersNameDescriptionniRFSA_ConfigureAcquisitionTypeConfigures whether the session acquires I/Q data or computes a power spectrum over the specified frequency range. niRFSA_ConfigureReferenceLevelConfigures the r

### Configuration

#### Groups

- Clock
- Configuration List
- De-embedding
- IQ
- Set/Get/Reset Attribute
- Spectrum
- Trigger

#### Group members

| Name | Description |
| --- | --- |
| niRFSA_ConfigureAcquisitionType | Configures whether the session acquires I/Q data or computes a power spectrum over the specified frequency range. |
| niRFSA_ConfigureReferenceLevel | Configures the reference level. |
| niRFSA_GetTerminalName | Returns the fully qualified name of the signal being queried. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration_1ga07d88370e580e38171f9ba88ca0c9a45.html language=enus -->
## TOPIC 00104: niRFSA_ConfigureReferenceLevel

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration_1ga07d88370e580e38171f9ba88ca0c9a45.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration_1ga07d88370e580e38171f9ba88ca0c9a45.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference level. SyntaxViStatus _VI_FUNC niRFSA_ConfigureReferenceLevel(ViSession vi, ViConstString channelList, ViReal64 referenceLevel)RemarksThe reference level represents the maximum expected power of an input RF signal.Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (extern

### niRFSA_ConfigureReferenceLevel

Configures the reference level.

#### Syntax

ViStatus _VI_FUNC niRFSA_ConfigureReferenceLevel(ViSession vi, ViConstString channelList, ViReal64 referenceLevel)

#### Remarks

The reference level represents the maximum expected power of an input RF signal.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Improving Your Measurements](https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/measurement_guidelines.html)

[Programming Attenuation-Related Properties and Attributes Using NI-RFSA](https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/programming-attenuation.html)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| channelList | [in] | ViConstString | Identifies which channels to apply settings. Specify an empty string as the value of this parameter. |
| referenceLevel | [in] | ViReal64 | Specifies the expected total power, in dBm, of the RF input signal. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration_1ga3e68e092f0621f1855ca7e753df47526.html language=enus -->
## TOPIC 00105: niRFSA_GetTerminalName

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration_1ga3e68e092f0621f1855ca7e753df47526.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration_1ga3e68e092f0621f1855ca7e753df47526.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the fully qualified name of the signal being queried. SyntaxViStatus _VI_FUNC niRFSA_GetTerminalName(ViSession vi, ViInt32 signal, ViConstString signalIdentifier, ViInt32 bufferSize, ViChar terminalName[])RemarksSignals can be triggers, clocks, or events.You can pass the terminalName paramet

### niRFSA_GetTerminalName

Returns the fully qualified name of the signal being queried.

#### Syntax

ViStatus _VI_FUNC niRFSA_GetTerminalName(ViSession vi, ViInt32 signal, ViConstString signalIdentifier, ViInt32 bufferSize, ViChar terminalName[])

#### Remarks

Signals can be triggers, clocks, or events.

You can pass the **terminalName** parameter that is returned to the **source** parameter of a configure trigger function.

**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Events](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| signal | [in] | ViInt32 | Specifies the signal for which you want to query the terminal.NameValueDescriptionNIRFSA_VAL_START_TRIGGER1100 (0x44c)NI-RFSA routes a Start Trigger.NIRFSA_VAL_REF_TRIGGER702 (0x2be)NI-RFSA routes a ReferenceNIRFSA_VAL_ADVANCE_TRIGGER1102 (0x44e)NI-RFSA routes an AdvanceNIRFSA_VAL_READY_FOR_START_EVENT1200 (0x4b0)NI-RFSA routes a Ready for Start Event.NIRFSA_VAL_READY_FOR_REF_EVENT1201 (0x4b1)NI-RFSA routes a Ready for Reference Event..NIRFSA_VAL_END_OF_RECORD_EVENT1203 (0x4b3)NI-RFSA routes a End of Record Event.NIRFSA_VAL_DONE_EVENT1204 (0x4b4)NI-RFSA routes a Done Event.NIRFSA_VAL_REF_CLOCK1205 (0x4b5)NI-RFSA routes a Reference Clock.NIRFSA_VAL_USER1206 (0x4b6)NI-RFSA routes a User Defined Signal. |
| Name | Value | Description |  |
| NIRFSA_VAL_START_TRIGGER | 1100 (0x44c) | NI-RFSA routes a Start Trigger. |  |
| NIRFSA_VAL_REF_TRIGGER | 702 (0x2be) | NI-RFSA routes a Reference |  |
| NIRFSA_VAL_ADVANCE_TRIGGER | 1102 (0x44e) | NI-RFSA routes an Advance |  |
| NIRFSA_VAL_READY_FOR_START_EVENT | 1200 (0x4b0) | NI-RFSA routes a Ready for Start Event. |  |
| NIRFSA_VAL_READY_FOR_REF_EVENT | 1201 (0x4b1) | NI-RFSA routes a Ready for Reference Event.. |  |
| NIRFSA_VAL_END_OF_RECORD_EVENT | 1203 (0x4b3) | NI-RFSA routes a End of Record Event. |  |
| NIRFSA_VAL_DONE_EVENT | 1204 (0x4b4) | NI-RFSA routes a Done Event. |  |
| NIRFSA_VAL_REF_CLOCK | 1205 (0x4b5) | NI-RFSA routes a Reference Clock. |  |
| NIRFSA_VAL_USER | 1206 (0x4b6) | NI-RFSA routes a User Defined Signal. |  |
| signalIdentifier | [in] | ViConstString | Specifies a particular instance of a trigger. NI-RFSA does not support this parameter. |
| bufferSize | [in] | ViInt32 | Passes the number of bytes in the ViChar buffer that you allocate for the terminalName parameter. |
| terminalName | [in] | ViChar[] | Returns the fully qualified name of the signal being queried. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__clock.html language=enus -->
## TOPIC 00106: Clock

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__clock.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__clock.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniRFSA_ConfigurePxiChassisClk10Specifies the signal to drive the 10 MHz Reference Clock on the PXI backplane. niRFSA_ConfigureRefClockConfigures the NI-RFSA device Reference Clock. niRFSA_ExportSignalRoutes signals (triggers, clocks, and events) to the specified

### Clock

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niRFSA_ConfigurePxiChassisClk10 | Specifies the signal to drive the 10 MHz Reference Clock on the PXI backplane. |
| niRFSA_ConfigureRefClock | Configures the NI-RFSA device Reference Clock. |
| niRFSA_ExportSignal | Routes signals (triggers, clocks, and events) to the specified output terminal. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__clock_1ga3b348a37451b85a66a8584bcd7c02ff8.html language=enus -->
## TOPIC 00107: niRFSA_ConfigureRefClock

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__clock_1ga3b348a37451b85a66a8584bcd7c02ff8.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__clock_1ga3b348a37451b85a66a8584bcd7c02ff8.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the NI-RFSA device Reference Clock. SyntaxViStatus _VI_FUNC niRFSA_ConfigureRefClock(ViSession vi, ViConstString clockSource, ViReal64 refClockRate)RemarksSupported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5

### niRFSA_ConfigureRefClock

Configures the NI-RFSA device Reference Clock.

#### Syntax

ViStatus _VI_FUNC niRFSA_ConfigureRefClock(ViSession vi, ViConstString clockSource, ViReal64 refClockRate)

#### Remarks

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[PXI-5661 Reference Clock](https://www.ni.com/docs/en-US/bundle/pxi-5661-feature/page/reference-clock.html)

[PXIe-5663 Timing Configurations](https://www.ni.com/docs/en-US/bundle/pxie-5663-5663e-feature/page/timing-configurations.html)

[PXIe-5665 Timing Configurations](https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/timing-configurations.html)

[PXIe-5667 Timing Configurations](https://www.ni.com/docs/en-US/bundle/pxie-5667-feature/page/timing-configurations.html)

[PXIe-5668 Timing Configurations](https://www.ni.com/docs/en-US/bundle/pxie-5668-feature/page/timing-configurations.html)

[PXIe-5830 Timing Configurations](https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/timing-configurations.html)

[PXIe-5831 Timing Configurations](https://www.ni.com/docs/en-US/bundle/pxie-5831/page/timing-configurations.html)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function |
| clockSource | [in] | ViConstString | specifies the source of the Reference Clock signal. Clock SourceDescriptionOnboard Clock (default)Uses the onboard Reference Clock as the clock source. PXIe-5830/5831/5832-- PXIe-5830: Connect PXIe-5820 REF IN to PXIe-3621 REF OUT. - PXIe-5831: Connect PXIe-5820 REF IN to PXIe-3622 REF OUT. - PXIe-5832: Connect PXIe-5820 REF IN to PXIe-3623 REF OUT. PXIe-5831 with PXIe-5653-- Connect PXIe-5820 REF IN to PXIe-3622 REF OUT. - Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3622 REF IN. PXIe-5832 with PXIe-5653-- Connect PXIe-5820 REF IN to PXIe-3623 REF OUT. - Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3623 REF IN. PXIe-5841 with PXIe-5655-- Lock to PXIe-5655 onboard clock. Connect REF OUT on PXIe-5655 to PXIe-5841 REF IN. PXIe-5842-- Lock to PXIe-5655 onboard clock. Use cables as shown in the Getting Started Guide.RefInUses the signal at the front panel REF IN connector. PXIe-5830/5831/5832-- PXIe-5830: Connect PXIe-5820 REF IN to PXIe-3621 REF OUT; lock external signal to PXIe-3621 REF IN. - PXIe-5831: Connect PXIe-5820 REF IN to PXIe-3622 REF OUT; lock external signal to PXIe-3622 REF IN. - PXIe-5832: Connect PXIe-5820 REF IN to PXIe-3623 REF OUT; lock external signal to PXIe-3623 REF IN. PXIe-5831 with PXIe-5653-- Connect PXIe-5820 REF IN to PXIe-3622 REF OUT. - Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3622 REF IN. - Lock external signal to PXIe-5653 REF IN. PXIe-5832 with PXIe-5653-- Connect PXIe-5820 REF IN to PXIe-3623 REF OUT. - Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3623 REF IN. - Lock external signal to PXIe-5653 REF IN. PXIe-5841 with PXIe-5655-- Lock to signal at REF IN on PXIe-5655. Connect REF OUT on PXIe-5655 to PXIe-5841 REF IN. PXIe-5842-- Lock to signal at REF IN on PXIe-5655. Use cables as shown in the Getting Started Guide.PXI ClockUses the PXI_CLK signal present on the PXI backplane.PXI_ClkMasterValid only for PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653. PXIe-5831 with PXIe-5653-- NI-RFSG configures PXIe-5653 to export Reference Clock. - Configures PXIe-5820 and PXIe-3622 to use PXI_Clk. - Connect PXIe-5653 REF OUT (10 MHz) to PXI chassis REF IN. PXIe-5832 with PXIe-5653-- NI-RFSG configures PXIe-5653 to export Reference Clock. - Configures PXIe-5820 and PXIe-3623 to use PXI_Clk. - Connect PXIe-5653 REF OUT (10 MHz) to PXI chassis REF IN. |
| Clock Source | Description |  |  |
| Onboard Clock (default) | Uses the onboard Reference Clock as the clock source. PXIe-5830/5831/5832-- PXIe-5830: Connect PXIe-5820 REF IN to PXIe-3621 REF OUT. - PXIe-5831: Connect PXIe-5820 REF IN to PXIe-3622 REF OUT. - PXIe-5832: Connect PXIe-5820 REF IN to PXIe-3623 REF OUT. PXIe-5831 with PXIe-5653-- Connect PXIe-5820 REF IN to PXIe-3622 REF OUT. - Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3622 REF IN. PXIe-5832 with PXIe-5653-- Connect PXIe-5820 REF IN to PXIe-3623 REF OUT. - Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3623 REF IN. PXIe-5841 with PXIe-5655-- Lock to PXIe-5655 onboard clock. Connect REF OUT on PXIe-5655 to PXIe-5841 REF IN. PXIe-5842-- Lock to PXIe-5655 onboard clock. Use cables as shown in the Getting Started Guide. |  |  |
| RefIn | Uses the signal at the front panel REF IN connector. PXIe-5830/5831/5832-- PXIe-5830: Connect PXIe-5820 REF IN to PXIe-3621 REF OUT; lock external signal to PXIe-3621 REF IN. - PXIe-5831: Connect PXIe-5820 REF IN to PXIe-3622 REF OUT; lock external signal to PXIe-3622 REF IN. - PXIe-5832: Connect PXIe-5820 REF IN to PXIe-3623 REF OUT; lock external signal to PXIe-3623 REF IN. PXIe-5831 with PXIe-5653-- Connect PXIe-5820 REF IN to PXIe-3622 REF OUT. - Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3622 REF IN. - Lock external signal to PXIe-5653 REF IN. PXIe-5832 with PXIe-5653-- Connect PXIe-5820 REF IN to PXIe-3623 REF OUT. - Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3623 REF IN. - Lock external signal to PXIe-5653 REF IN. PXIe-5841 with PXIe-5655-- Lock to signal at REF IN on PXIe-5655. Connect REF OUT on PXIe-5655 to PXIe-5841 REF IN. PXIe-5842-- Lock to signal at REF IN on PXIe-5655. Use cables as shown in the Getting Started Guide. |  |  |
| PXI Clock | Uses the PXI_CLK signal present on the PXI backplane. |  |  |
| PXI_ClkMaster | Valid only for PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653. PXIe-5831 with PXIe-5653-- NI-RFSG configures PXIe-5653 to export Reference Clock. - Configures PXIe-5820 and PXIe-3622 to use PXI_Clk. - Connect PXIe-5653 REF OUT (10 MHz) to PXI chassis REF IN. PXIe-5832 with PXIe-5653-- NI-RFSG configures PXIe-5653 to export Reference Clock. - Configures PXIe-5820 and PXIe-3623 to use PXI_Clk. - Connect PXIe-5653 REF OUT (10 MHz) to PXI chassis REF IN. |  |  |
| refClockRate | [in] | ViReal64 | specifies the Reference Clock rate, in hertz (Hz), of the signal present at the REF IN or CLK IN connector. This parameter is only valid when the ref clock source parameter is set to RefIn. The default value is Auto (-1.0), which allows NI-RFSG to use the default Reference Clock rate for the device or automatically detect the Reference Clock rate, if supported. Refer to the Reference Clock Rate property for possible values. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Clock

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__clock_1ga9e3180446cd71d563bbca7d8d1506cef.html language=enus -->
## TOPIC 00108: niRFSA_ConfigurePxiChassisClk10

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__clock_1ga9e3180446cd71d563bbca7d8d1506cef.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__clock_1ga9e3180446cd71d563bbca7d8d1506cef.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the signal to drive the 10 MHz Reference Clock on the PXI backplane. SyntaxViStatus _VI_FUNC niRFSA_ConfigurePxiChassisClk10(ViSession vi, ViConstString pxiClk10Source)RemarksThis option can be configured only when the PXI-5600 is installed in the Star Trigger Controller Slot, also known a

### niRFSA_ConfigurePxiChassisClk10

Specifies the signal to drive the 10 MHz Reference Clock on the PXI backplane.

#### Syntax

ViStatus _VI_FUNC niRFSA_ConfigurePxiChassisClk10(ViSession vi, ViConstString pxiClk10Source)

#### Remarks

This option can be configured only when the PXI-5600 is installed in the Star Trigger Controller Slot, also known as the System Timing Slot, of the PXI chassis.

**Supported Devices**: PXI-5600 (external digitizer mode), PXI-5661

**Related Topics**

[System Reference Clock](https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/system-reference-clock.html)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| pxiClk10Source | [in] | ViConstString | Specifies the signal to drive the 10 MHz Reference Clock on the PXI backplane. This option can only be configured when the PXI-5600 is in Slot 2 of the PXI chassis.ValueDescriptionNIRFSA_VAL_NONE_STR ("None")The device does not drive the PXI 10 MHz backplane Reference Clock.NIRFSA_VAL_ONBOARD_CLOCK_STR ("OnboardClock")The device drives the PXI 10 MHz backplane Reference Clock with the PXI-5600 onboard clock. You must connect the 10 MHz OUT connector to the PXI 10 MHz I/O connector on the PXI-5600 front panel to use this option.NIRFSA_VAL_REF_IN_STR ("RefIn")The device drives the PXI 10 MHz backplane Reference Clock with the reference source attached to the PXI-5600 REF IN connector. You must connect the 10 MHz OUT connector to the PXI 10 MHz I/O on the PXI-5600 front panel to use this option. |
| Value | Description |  |  |
| NIRFSA_VAL_NONE_STR ("None") | The device does not drive the PXI 10 MHz backplane Reference Clock. |  |  |
| NIRFSA_VAL_ONBOARD_CLOCK_STR ("OnboardClock") | The device drives the PXI 10 MHz backplane Reference Clock with the PXI-5600 onboard clock. You must connect the 10 MHz OUT connector to the PXI 10 MHz I/O connector on the PXI-5600 front panel to use this option. |  |  |
| NIRFSA_VAL_REF_IN_STR ("RefIn") | The device drives the PXI 10 MHz backplane Reference Clock with the reference source attached to the PXI-5600 REF IN connector. You must connect the 10 MHz OUT connector to the PXI 10 MHz I/O on the PXI-5600 front panel to use this option. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Clock

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__clock_1gaa0e7acfa202c06fb09bdf610d8a613eb.html language=enus -->
## TOPIC 00109: niRFSA_ExportSignal

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__clock_1gaa0e7acfa202c06fb09bdf610d8a613eb.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__clock_1gaa0e7acfa202c06fb09bdf610d8a613eb.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Routes signals (triggers, clocks, and events) to the specified output terminal. SyntaxViStatus _VI_FUNC niRFSA_ExportSignal(ViSession vi, ViInt32 signal, ViConstString signalIdentifier, ViConstString outputTerminal)RemarksIf you export a signal with this function and commit the session, the signal i

### niRFSA_ExportSignal

Routes signals (triggers, clocks, and events) to the specified output terminal.

#### Syntax

ViStatus _VI_FUNC niRFSA_ExportSignal(ViSession vi, ViInt32 signal, ViConstString signalIdentifier, ViConstString outputTerminal)

#### Remarks

If you export a signal with this function and [commit](https://rfsacref.chm/cviniRFSA_Commit.html) the session, the signal is routed to the output terminal you specify. If you then reconfigure the signal to have a different output terminal, the previous output terminal is tri-stated when the session is next committed. If you set the **outputTerminal** parameter to **NIRFSA_VAL_DO_NOT_EXPORT_STR** and commit, the previous output terminal is tristated.

Any signals, except for those exported over PXI trigger lines, that are exported within a session persist after the session closes to prevent signal glitches between sessions. PXI trigger lines are always set to tristate when a session is closed. If you wish to have the output terminal tristated when the session closes, change the **outputTerminal** for the exported signal to **NIRFSA_VAL_DO_NOT_EXPORT_STR**, and commit the session again before closing it.

You can also tristate all PFI lines by setting the **resetDevice** parameter in the [niRFSA_Init](group____root__ni_r_f_s_a__functions_1ga188b3c494896b1959fb1a2f43bf005dd.html) function to VI_TRUE or by using the [niRFSA_Reset](group____root__ni_r_f_s_a__functions__utility_1gacc51bf29e024ce7620a7003cb1c9a52f.html) function.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| signal | [in] | ViInt32 | Specifies the type of signal to route.NameValueDescriptionNIRFSA_VAL_START_TRIGGER1100 (0x44c)NI-RFSA routes a Start Trigger.NIRFSA_VAL_REF_TRIGGER702 (0x2be)NI-RFSA routes a ReferenceNIRFSA_VAL_ADVANCE_TRIGGER1102 (0x44e)NI-RFSA routes an AdvanceNIRFSA_VAL_READY_FOR_START_EVENT1200 (0x4b0)NI-RFSA routes a Ready for Start Event.NIRFSA_VAL_READY_FOR_REF_EVENT1201 (0x4b1)NI-RFSA routes a Ready for Reference Event..NIRFSA_VAL_END_OF_RECORD_EVENT1203 (0x4b3)NI-RFSA routes a End of Record Event.NIRFSA_VAL_DONE_EVENT1204 (0x4b4)NI-RFSA routes a Done Event.NIRFSA_VAL_REF_CLOCK1205 (0x4b5)NI-RFSA routes a Reference Clock.NIRFSA_VAL_USER1206 (0x4b6)NI-RFSA routes a User Defined Signal. |
| Name | Value | Description |  |
| NIRFSA_VAL_START_TRIGGER | 1100 (0x44c) | NI-RFSA routes a Start Trigger. |  |
| NIRFSA_VAL_REF_TRIGGER | 702 (0x2be) | NI-RFSA routes a Reference |  |
| NIRFSA_VAL_ADVANCE_TRIGGER | 1102 (0x44e) | NI-RFSA routes an Advance |  |
| NIRFSA_VAL_READY_FOR_START_EVENT | 1200 (0x4b0) | NI-RFSA routes a Ready for Start Event. |  |
| NIRFSA_VAL_READY_FOR_REF_EVENT | 1201 (0x4b1) | NI-RFSA routes a Ready for Reference Event.. |  |
| NIRFSA_VAL_END_OF_RECORD_EVENT | 1203 (0x4b3) | NI-RFSA routes a End of Record Event. |  |
| NIRFSA_VAL_DONE_EVENT | 1204 (0x4b4) | NI-RFSA routes a Done Event. |  |
| NIRFSA_VAL_REF_CLOCK | 1205 (0x4b5) | NI-RFSA routes a Reference Clock. |  |
| NIRFSA_VAL_USER | 1206 (0x4b6) | NI-RFSA routes a User Defined Signal. |  |
| signalIdentifier | [in] | ViConstString | Specifies the user-defined signal to route. Specify the signal you have implemented using FPGA extensions. |
| outputTerminal | [in] | ViConstString | Specifies the terminal where the signal will be exported. You can also choose not to export any signal. For the PXIe-5841 with PXIe-5655, the signal is exported to the terminal on the PXIe-5841.ValueDescriptionNIRFSA_VAL_DO_NOT_EXPORT_STRThe signal is not exported.NIRFSA_VAL_CLK_OUT_STRThe signal is exported to the CLK OUT connector on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841/5842/5860.NIRFSA_VAL_REF_OUT_STRThe signal is exported to the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5694, PXIe-5644/5645/5646, or PXIe-5820/5830/5831/5832/5840/5841/5842/5860.NIRFSA_VAL_REF_OUT2_STRThe signal is exported to the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E.NIRFSA_VAL_PFI0_STRThe signal is exported to the PFI 0 connector.NIRFSA_VAL_PFI1_STRThe signal is exported to the PFI 1 connector on the PXI-5142 and PXIe-5622.NIRFSA_VAL_PXI_TRIG0_STRThe signal is exported to the PXI trigger line 0.NIRFSA_VAL_PXI_TRIG1_STRThe signal is exported to the PXI trigger line 1.NIRFSA_VAL_PXI_TRIG2_STRThe signal is exported to the PXI trigger line 2.NIRFSA_VAL_PXI_TRIG3_STRThe signal is exported to the PXI trigger line 3.NIRFSA_VAL_PXI_TRIG4_STRThe signal is exported to the PXI trigger line 4.NIRFSA_VAL_PXI_TRIG5_STRThe signal is exported to the PXI trigger line 5.NIRFSA_VAL_PXI_TRIG6_STRThe signal is exported to the PXI trigger line 6.NIRFSA_VAL_PXI_TRIG7_STRThe signal is exported to the PXI trigger line 7.NIRFSA_VAL_PXI_STAR_STRThe signal is exported to the PXI star trigger line.NIRFSA_VAL_PXIE_DSTARC_STRThe signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.NIRFSA_VAL_DIO_PFI0_STR ("PFI0")The trigger is received on PFI 0 of the DIO Terminal.NIRFSA_VAL_DIO_PFI1_STR ("PFI1")The trigger is received on PFI 1 of the DIO Terminal.NIRFSA_VAL_DIO_PFI2_STR ("PFI2")The trigger is received on PFI 2 of the DIO Terminal.NIRFSA_VAL_DIO_PFI3_STR ("PFI3")The trigger is received on PFI 3 of the DIO Terminal.NIRFSA_VAL_DIO_PFI4_STR ("PFI4")The trigger is received on PFI 4 of the DIO Terminal.NIRFSA_VAL_DIO_PFI5_STR ("PFI5")The trigger is received on PFI 5 of the DIO Terminal.NIRFSA_VAL_DIO_PFI6_STR ("PFI6")The trigger is received on PFI 6 of the DIO Terminal.NIRFSA_VAL_DIO_PFI7_STR ("PFI7")The trigger is received on PFI 7 of the DIO Terminal. |
| Value | Description |  |  |
| NIRFSA_VAL_DO_NOT_EXPORT_STR | The signal is not exported. |  |  |
| NIRFSA_VAL_CLK_OUT_STR | The signal is exported to the CLK OUT connector on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |  |  |
| NIRFSA_VAL_REF_OUT_STR | The signal is exported to the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5694, PXIe-5644/5645/5646, or PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |  |  |
| NIRFSA_VAL_REF_OUT2_STR | The signal is exported to the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E. |  |  |
| NIRFSA_VAL_PFI0_STR | The signal is exported to the PFI 0 connector. |  |  |
| NIRFSA_VAL_PFI1_STR | The signal is exported to the PFI 1 connector on the PXI-5142 and PXIe-5622. |  |  |
| NIRFSA_VAL_PXI_TRIG0_STR | The signal is exported to the PXI trigger line 0. |  |  |
| NIRFSA_VAL_PXI_TRIG1_STR | The signal is exported to the PXI trigger line 1. |  |  |
| NIRFSA_VAL_PXI_TRIG2_STR | The signal is exported to the PXI trigger line 2. |  |  |
| NIRFSA_VAL_PXI_TRIG3_STR | The signal is exported to the PXI trigger line 3. |  |  |
| NIRFSA_VAL_PXI_TRIG4_STR | The signal is exported to the PXI trigger line 4. |  |  |
| NIRFSA_VAL_PXI_TRIG5_STR | The signal is exported to the PXI trigger line 5. |  |  |
| NIRFSA_VAL_PXI_TRIG6_STR | The signal is exported to the PXI trigger line 6. |  |  |
| NIRFSA_VAL_PXI_TRIG7_STR | The signal is exported to the PXI trigger line 7. |  |  |
| NIRFSA_VAL_PXI_STAR_STR | The signal is exported to the PXI star trigger line. |  |  |
| NIRFSA_VAL_PXIE_DSTARC_STR | The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |  |  |
| NIRFSA_VAL_DIO_PFI0_STR ("PFI0") | The trigger is received on PFI 0 of the DIO Terminal. |  |  |
| NIRFSA_VAL_DIO_PFI1_STR ("PFI1") | The trigger is received on PFI 1 of the DIO Terminal. |  |  |
| NIRFSA_VAL_DIO_PFI2_STR ("PFI2") | The trigger is received on PFI 2 of the DIO Terminal. |  |  |
| NIRFSA_VAL_DIO_PFI3_STR ("PFI3") | The trigger is received on PFI 3 of the DIO Terminal. |  |  |
| NIRFSA_VAL_DIO_PFI4_STR ("PFI4") | The trigger is received on PFI 4 of the DIO Terminal. |  |  |
| NIRFSA_VAL_DIO_PFI5_STR ("PFI5") | The trigger is received on PFI 5 of the DIO Terminal. |  |  |
| NIRFSA_VAL_DIO_PFI6_STR ("PFI6") | The trigger is received on PFI 6 of the DIO Terminal. |  |  |
| NIRFSA_VAL_DIO_PFI7_STR ("PFI7") | The trigger is received on PFI 7 of the DIO Terminal. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Clock

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__configuration__list.html language=enus -->
## TOPIC 00110: Configuration List

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__configuration__list.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__configuration__list.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniRFSA_CreateConfigurationListCreates an empty configuration list for RF list mode. niRFSA_CreateConfigurationListStepCreates a new configuration list step in the configuration list for RF list mode specified by the NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST attribut

### Configuration List

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niRFSA_CreateConfigurationList | Creates an empty configuration list for RF list mode. |
| niRFSA_CreateConfigurationListStep | Creates a new configuration list step in the configuration list for RF list mode specified by the NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST attribute. |
| niRFSA_DeleteConfigurationList | Deletes a previously created configuration list and all the configuration list steps in the RF list mode configuration list. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__configuration__list_1ga390222b856bcaece18789b2ba692d42c.html language=enus -->
## TOPIC 00111: niRFSA_CreateConfigurationList

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__configuration__list_1ga390222b856bcaece18789b2ba692d42c.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__configuration__list_1ga390222b856bcaece18789b2ba692d42c.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an empty configuration list for RF list mode. SyntaxViStatus _VI_FUNC niRFSA_CreateConfigurationList(ViSession vi, ViConstString listName, ViInt32 numberOfListAttributes, const ViAttr *listAttributeIDs, ViBoolean setAsActiveList)RemarksAfter a configuration list is created, enable the list u

### niRFSA_CreateConfigurationList

Creates an empty configuration list for [RF list mode](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html).

#### Syntax

ViStatus _VI_FUNC niRFSA_CreateConfigurationList(ViSession vi, ViConstString listName, ViInt32 numberOfListAttributes, const ViAttr *listAttributeIDs, ViBoolean setAsActiveList)

#### Remarks

After a configuration list is created, enable the list using the **setAsActiveList** parameter. Call the [niRFSA_CreateConfigurationListStep](group____root__ni_r_f_s_a__functions__configuration__configuration__list_1ga6b2721268b980d7e1bd1c0ce01640eab.html) function to add steps to the active configuration list.

**Supported Devices**: PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842/5860, PXIe-5842 with S-parameters, PXIe-5842 with 54GHz Frequency Extension, PXIe-5860 with S-parameters

**Related Topics**

[RF List Mode](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html)

#### Parameters

| Name | Direction | Type | Description |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |  |  |  |  |  |  |  |  |
| listName | [in] | ViConstString | Specifies the name of the configuration list. This string may not contain spaces, special characters, or punctuation marks. |  |  |  |  |  |  |  |  |
| numberOfListAttributes | [in] | ViInt32 | Specifies the number of configuration list attributes to set. |  |  |  |  |  |  |  |  |
| listAttributeIDs | [out] | const ViAttr * | Specifies the attributes that you intend to change between configuration list steps. Calling the niRFSA_CreateConfigurationList function allocates space for each of the configuration list attributes. When you use an NI-RFSG Set attribute function to set one of the attributes in the configuration list, that attribute is set for one of the configuration list steps. Use the NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST_STEP attribute to specify which configuration list step to configure.You can include the following attributes in your configuration list based on your device:AttributePXIe-5663EPXIe-5665PXIe-5667PXIe-5644/5646PXIe-5645PXIe-5820PXIe-5830/5831/5832PXIe-5840/5841PXIe-5841 with PXIe-5655PXIe-5842PXIe-5860NIRFSA_ATTR_CHANNEL_COUPLINGSupportedNIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTHSupportedSupportedSupportedSupportedSupportedSupportedSupportedNIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCYSupportedSupportedSupportedSupportedSupportedNIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSETSupportedNIRFSA_ATTR_DOWNCONVERTER_PRESELECTOR_ENABLEDSupportedSupportedSupportedSupportedSupportedNIRFSA_ATTR_EXTERNAL_GAINSupportedSupportedSupportedSupportedNIRFSA_ATTR_FREQUENCY_SETTLINGSupportedSupportedSupportedSupportedSupportedSupportedSupportedSupportedSupportedNIRFSA_ATTR_IF_FILTER_BANDWIDTHSupportedSupportedSupportedSupportedSupportedSupportedNIRFSA_ATTR_IF_OUTPUT_POWER_LEVELSupportedSupportedNIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL_OFFSETSupportedSupportedNIRFSA_ATTR_IQ_CARRIER_FREQUENCYSupportedSupportedSupportedNIRFSA_ATTR_IQ_IN_PORT_CARRIER_FREQUENCYSupportedSupportedNIRFSA_ATTR_IQ_IN_PORT_VERTICAL_RANGESupportedSupportedNIRFSA_ATTR_IQ_POWER_EDGE_REF_TRIGGER_LEVELSupportedSupportedSupportedNIRFSA_ATTR_LO_SOURCESupportedSupportedSupportedSupportedSupportedSupportedSupportedSupportedNIRFSA_ATTR_IF_OUTPUT_POWER_LEVELSupportedSupportedSupportedSupportedSupportedSupportedSupportedSupportedNIRFSA_ATTR_LOW_FREQUENCY_BYPASS_ENABLEDSupportedSupportedSupportedSupportedNIRFSA_ATTR_MECHANICAL_ATTENUATIONSupportedSupportedSupportedNIRFSA_ATTR_MECHANICAL_ATTENUATOR_ENABLEDSupportedNIRFSA_ATTR_MINIMUM_ACPRSupportedNIRFSA_ATTR_NOTCH_FILTER_ENABLEDSupportedSupportedNIRFSA_ATTR_NUMBER_OF_SAMPLESSupportedSupportedSupportedSupportedSupportedSupportedSupportedSupportedSupportedSupportedNIRFSA_ATTR_OSP_DATA_SCALING_FACTORSupportedSupportedSupportedSupportedSupportedNIRFSA_ATTR_REFERENCE_LEVELSupportedSupportedNIRFSA_ATTR_ATTENUATIONSupportedNIRFSA_ATTR_RF_OUT_LO_EXPORT_ENABLEDSupportedSupportedNIRFSA_ATTR_RF_PREAMP_ENABLEDSupportedSupportedNIRFSA_ATTR_RF_PRESELECTOR_FILTERSupportedSupportedNIRFSA_ATTR_SELECTED_PORTSSupportedSupportedNIRFSA_ATTR_TIMER_EVENT_INTERVALSupportedSupportedSupported |  |  |  |  |  |  |  |  |
| Attribute | PXIe-5663E | PXIe-5665 | PXIe-5667 | PXIe-5644/5646 | PXIe-5645 | PXIe-5820 | PXIe-5830/5831/5832 | PXIe-5840/5841 | PXIe-5841 with PXIe-5655 | PXIe-5842 | PXIe-5860 |
| NIRFSA_ATTR_CHANNEL_COUPLING |  |  | Supported |  |  |  |  |  |  |  |  |
| NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH | Supported | Supported | Supported |  |  | Supported |  | Supported |  | Supported | Supported |
| NIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCY |  |  |  |  | Supported | Supported |  | Supported | Supported | Supported |  |
| NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET |  |  |  |  |  | Supported |  |  |  |  |  |
| NIRFSA_ATTR_DOWNCONVERTER_PRESELECTOR_ENABLED | Supported | Supported |  |  |  |  |  | Supported | Supported | Supported |  |
| NIRFSA_ATTR_EXTERNAL_GAIN |  |  |  |  |  |  |  | Supported | Supported | Supported | Supported |
| NIRFSA_ATTR_FREQUENCY_SETTLING | Supported | Supported | Supported | Supported | Supported | Supported | Supported | Supported |  |  | Supported |
| NIRFSA_ATTR_IF_FILTER_BANDWIDTH |  |  | Supported | Supported | Supported | Supported | Supported |  |  | Supported |  |
| NIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL |  | Supported |  |  |  |  |  | Supported |  |  |  |
| NIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL_OFFSET |  | Supported |  |  |  |  |  | Supported |  |  |  |
| NIRFSA_ATTR_IQ_CARRIER_FREQUENCY |  | Supported |  |  |  |  |  | Supported |  |  | Supported |
| NIRFSA_ATTR_IQ_IN_PORT_CARRIER_FREQUENCY |  | Supported |  |  |  |  |  | Supported |  |  |  |
| NIRFSA_ATTR_IQ_IN_PORT_VERTICAL_RANGE |  |  |  |  |  |  |  |  | Supported | Supported |  |
| NIRFSA_ATTR_IQ_POWER_EDGE_REF_TRIGGER_LEVEL |  |  |  |  | Supported | Supported |  |  |  |  | Supported |
| NIRFSA_ATTR_LO_SOURCE | Supported | Supported | Supported | Supported |  |  | Supported | Supported | Supported | Supported |  |
| NIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL | Supported | Supported | Supported |  | Supported | Supported | Supported |  | Supported | Supported |  |
| NIRFSA_ATTR_LOW_FREQUENCY_BYPASS_ENABLED |  |  |  |  |  |  | Supported | Supported | Supported | Supported |  |
| NIRFSA_ATTR_MECHANICAL_ATTENUATION |  |  |  |  | Supported | Supported | Supported |  |  |  |  |
| NIRFSA_ATTR_MECHANICAL_ATTENUATOR_ENABLED |  |  |  |  |  |  |  |  | Supported |  |  |
| NIRFSA_ATTR_MINIMUM_ACPR |  |  |  |  |  |  |  |  | Supported |  |  |
| NIRFSA_ATTR_NOTCH_FILTER_ENABLED |  |  |  |  |  |  |  | Supported |  | Supported |  |
| NIRFSA_ATTR_NUMBER_OF_SAMPLES | Supported | Supported | Supported |  | Supported | Supported | Supported | Supported | Supported | Supported | Supported |
| NIRFSA_ATTR_OSP_DATA_SCALING_FACTOR | Supported | Supported |  |  |  |  | Supported |  |  | Supported | Supported |
| NIRFSA_ATTR_REFERENCE_LEVEL |  |  |  |  |  |  |  |  |  | Supported | Supported |
| NIRFSA_ATTR_ATTENUATION |  |  |  |  |  |  |  |  |  | Supported |  |
| NIRFSA_ATTR_RF_OUT_LO_EXPORT_ENABLED |  |  |  |  |  |  |  |  | Supported | Supported |  |
| NIRFSA_ATTR_RF_PREAMP_ENABLED |  |  |  |  |  |  |  |  | Supported | Supported |  |
| NIRFSA_ATTR_RF_PRESELECTOR_FILTER |  |  |  |  |  |  |  |  | Supported | Supported |  |
| NIRFSA_ATTR_SELECTED_PORTS |  |  |  |  |  |  |  |  | Supported | Supported |  |
| NIRFSA_ATTR_TIMER_EVENT_INTERVAL |  |  |  |  |  |  |  |  | Supported | Supported | Supported |
| setAsActiveList | [in] | ViBoolean | Sets this list as the active configuration list when this parameter is set to VI_TRUE. |  |  |  |  |  |  |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration List

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__configuration__list_1ga6b2721268b980d7e1bd1c0ce01640eab.html language=enus -->
## TOPIC 00112: niRFSA_CreateConfigurationListStep

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__configuration__list_1ga6b2721268b980d7e1bd1c0ce01640eab.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__configuration__list_1ga6b2721268b980d7e1bd1c0ce01640eab.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new configuration list step in the configuration list for RF list mode specified by the NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST attribute. SyntaxViStatus _VI_FUNC niRFSA_CreateConfigurationListStep(ViSession vi, ViBoolean setAsActiveStep)RemarksWhen you create a configuration list step, a ne

### niRFSA_CreateConfigurationListStep

Creates a new configuration list step in the configuration list for [RF list mode](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html) specified by the [NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST](group____root__ni_r_f_s_a__attributes__configuration__list_1gacc35d7d7792b502b870e9cd7258427d2.html) attribute.

#### Syntax

ViStatus _VI_FUNC niRFSA_CreateConfigurationListStep(ViSession vi, ViBoolean setAsActiveStep)

#### Remarks

When you create a configuration list step, a new instance of each attribute specified by the configuration list attributes is created. Configuration list attributes are specified when a configuration list is created.

**Supported Devices**: PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842/5860, PXIe-5842 with S-parameters, PXIe-5842 with 54GHz Frequency Extension, PXIe-5860 with S-parameters

**Related Topics**

[RF List Mode](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| setAsActiveStep | [in] | ViBoolean | Sets this step as the active step for the active configuration list. The default value for this parameter is VI_TRUE.If you set this parameter to VI_FALSE, you can select the active configuration list step using the NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST_STEP attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration List

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__configuration__list_1ga9ce0f39233a43d225b449bc4f1a71957.html language=enus -->
## TOPIC 00113: niRFSA_DeleteConfigurationList

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__configuration__list_1ga9ce0f39233a43d225b449bc4f1a71957.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__configuration__list_1ga9ce0f39233a43d225b449bc4f1a71957.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes a previously created configuration list and all the configuration list steps in the RF list mode configuration list. SyntaxViStatus _VI_FUNC niRFSA_DeleteConfigurationList(ViSession vi, ViConstString listName)RemarksWhen a configuration list step is deleted, all the instances of the attribut

### niRFSA_DeleteConfigurationList

Deletes a previously created configuration list and all the configuration list steps in the [RF list mode](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html) configuration list.

#### Syntax

ViStatus _VI_FUNC niRFSA_DeleteConfigurationList(ViSession vi, ViConstString listName)

#### Remarks

When a configuration list step is deleted, all the instances of the attributes associated with the configuration list step are also removed. When you delete the active configuration list, NI-RFSA automatically resets the [NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST](group____root__ni_r_f_s_a__attributes__configuration__list_1gacc35d7d7792b502b870e9cd7258427d2.html) attribute to "" (empty string), which indicates no list is active, and the [NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST_STEP](group____root__ni_r_f_s_a__attributes__configuration__list_1ga3a484b0bbdceacf87a54aab83b19948f.html) attribute to 0.

**Supported Devices**: PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842/5860, PXIe-5842 with S-parameters, PXIe-5842 with 54GHz Frequency Extension, PXIe-5860 with S-parameters

**Related Topics**

[RF List Mode](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| listName | [in] | ViConstString | Specifies the name of the configuration list. This string may not contain spaces, special characters, or punctuation marks. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration List

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__deembedding.html language=enus -->
## TOPIC 00114: De-embedding

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__deembedding.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__deembedding.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniRFSA_ConfigureDeembeddingTableInterpolationLinearSelects the linear interpolation method. niRFSA_ConfigureDeembeddingTableInterpolationNearestSelects the nearest interpolation method. niRFSA_ConfigureDeembeddingTableInterpolationSplineSelects the spline interp

### De-embedding

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niRFSA_ConfigureDeembeddingTableInterpolationLinear | Selects the linear interpolation method. |
| niRFSA_ConfigureDeembeddingTableInterpolationNearest | Selects the nearest interpolation method. |
| niRFSA_ConfigureDeembeddingTableInterpolationSpline | Selects the spline interpolation method. |
| niRFSA_CreateDeembeddingSparameterTableArray | Creates an s-parameter de-embedding table for the port from the input data. |
| niRFSA_CreateDeembeddingSparameterTableS2PFile | Creates an S-parameter de-embedding table for the port based on the specified S2P file. |
| niRFSA_DeleteAllDeembeddingTables | Deletes all configured de-embedding tables for the session. |
| niRFSA_DeleteDeembeddingTable | Deletes the selected de-embedding table for a given port. |
| niRFSA_GetDeembeddingSparameters | Returns the S-parameters used for de-embedding a measurement on the selected port. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__deembedding_1ga1b58cac2accd8a9b3e4fdcf90cb87de8.html language=enus -->
## TOPIC 00115: niRFSA_GetDeembeddingSparameters

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__deembedding_1ga1b58cac2accd8a9b3e4fdcf90cb87de8.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__deembedding_1ga1b58cac2accd8a9b3e4fdcf90cb87de8.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the S-parameters used for de-embedding a measurement on the selected port. SyntaxViStatus _VI_FUNC niRFSA_GetDeembeddingSparameters(ViSession vi, ni complex number f64 *sparameters, ViInt32 sparametersArraySize, ViInt32 *numberOfSparameters, ViInt32 *numberOfPorts)RemarksThis includes interp

### niRFSA_GetDeembeddingSparameters

Returns the S-parameters used for de-embedding a measurement on the selected port.

#### Syntax

ViStatus _VI_FUNC niRFSA_GetDeembeddingSparameters(ViSession vi, ni complex number f64 *sparameters, ViInt32 sparametersArraySize, ViInt32 *numberOfSparameters, ViInt32 *numberOfPorts)

#### Remarks

This includes interpolation of the parameters based on the configured carrier frequency. This function returns an empty array if no de-embedding is done.

If you want to call this function just to get the required buffer size, you can pass 0 for **S-parameter Size** and VI_NULL for the **S-parameters** buffer.

The port orientation for the returned S-parameters is normalized to **NIRFSA_VAL_PORT2_TOWARDS_DUT**.

**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| sparameters | [out] | ni complex number f64 * | Returns an array of S-parameters. The S-parameters are returned in the following order: s11, s12, s21, s22. |
| sparametersArraySize | [in] | ViInt32 | Specifies the size of the array that is returned by the sparameters output. |
| numberOfSparameters | [out] | ViInt32 * | Returns the number of S-parameters. |
| numberOfPorts | [out] | ViInt32 * | Returns the number of S-parameter ports. The sparameter array is always n x n, where span n is the number of ports. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

De-embedding

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__deembedding_1ga7367fa9428355a038e7fd70ab7d213cf.html language=enus -->
## TOPIC 00116: niRFSA_ConfigureDeembeddingTableInterpolationNearest

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__deembedding_1ga7367fa9428355a038e7fd70ab7d213cf.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__deembedding_1ga7367fa9428355a038e7fd70ab7d213cf.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects the nearest interpolation method. SyntaxViStatus _VI_FUNC niRFSA_ConfigureDeembeddingTableInterpolationNearest(ViSession vi, ViConstString port, ViConstString tableName)RemarksNI-RFSA uses the parameters of the table nearest to the carrier frequency for de-embedding.Supported Devices: PXIe-5

### niRFSA_ConfigureDeembeddingTableInterpolationNearest

Selects the nearest interpolation method.

#### Syntax

ViStatus _VI_FUNC niRFSA_ConfigureDeembeddingTableInterpolationNearest(ViSession vi, ViConstString port, ViConstString tableName)

#### Remarks

NI-RFSA uses the parameters of the table nearest to the carrier frequency for de-embedding.

**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| port | [in] | ViConstString | Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string). |
| tableName | [in] | ViConstString | Specifies the name of the table. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

De-embedding

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__deembedding_1ga7fff925480912acce5e3405be811a2df.html language=enus -->
## TOPIC 00117: niRFSA_DeleteDeembeddingTable

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__deembedding_1ga7fff925480912acce5e3405be811a2df.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__deembedding_1ga7fff925480912acce5e3405be811a2df.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes the selected de-embedding table for a given port. SyntaxViStatus _VI_FUNC niRFSA_DeleteDeembeddingTable(ViSession vi, ViConstString port, ViConstString tableName)RemarksSupported Devices: PXIe-5830/5831/5832/5840/5841/5842/5860ParametersNameDirectionTypeDescriptionvi[in]ViSessionIdentifies y

### niRFSA_DeleteDeembeddingTable

Deletes the selected de-embedding table for a given port.

#### Syntax

ViStatus _VI_FUNC niRFSA_DeleteDeembeddingTable(ViSession vi, ViConstString port, ViConstString tableName)

#### Remarks

**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| port | [in] | ViConstString | Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string). |
| tableName | [in] | ViConstString | Specifies the name of the table. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

De-embedding

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__deembedding_1ga87bbc493e47e8bfaa80165e6f3e18c09.html language=enus -->
## TOPIC 00118: niRFSA_CreateDeembeddingSparameterTableS2PFile

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__deembedding_1ga87bbc493e47e8bfaa80165e6f3e18c09.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__deembedding_1ga87bbc493e47e8bfaa80165e6f3e18c09.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an S-parameter de-embedding table for the port based on the specified S2P file. SyntaxViStatus _VI_FUNC niRFSA_CreateDeembeddingSparameterTableS2PFile(ViSession vi, ViConstString port, ViConstString tableName, ViConstString s2pFilePath, ViInt32 sparameterOrientation)RemarksIf you only create

### niRFSA_CreateDeembeddingSparameterTableS2PFile

Creates an S-parameter de-embedding table for the port based on the specified S2P file.

#### Syntax

ViStatus _VI_FUNC niRFSA_CreateDeembeddingSparameterTableS2PFile(ViSession vi, ViConstString port, ViConstString tableName, ViConstString s2pFilePath, ViInt32 sparameterOrientation)

#### Remarks

If you only create one table for a port, NI-RFSA automatically selects that table to de-embed the measurement.

**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[De-embedding Overview](https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html)

[S-parameters](https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html#GUID-0AD828DE-398A-45C6-ABBA-4208DEB7DE1B__GUID-67A69775-E4DB-4FA2-84FE-C05977ED4184)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| port | [in] | ViConstString | Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string). |
| tableName | [in] | ViConstString | Specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced. |
| s2pFilePath | [in] | ViConstString | Specifies the path to the S2P file that contains de-embedding information for the specified port. |
| sparameterOrientation | [in] | ViInt32 | Specifies the orientation of the data in the S2P file relative to the port on the DUT port.NameValueDescriptionNIRFSA_VAL_PORT1_TOWARDS_DUT3800 (0xed8)Port 1 of the S2P is oriented towards the DUT port.NIRFSA_VAL_PORT2_TOWARDS_DUT3801 (0xed9)Port 2 of the S2P is oriented towards the DUT port. |
| Name | Value | Description |  |
| NIRFSA_VAL_PORT1_TOWARDS_DUT | 3800 (0xed8) | Port 1 of the S2P is oriented towards the DUT port. |  |
| NIRFSA_VAL_PORT2_TOWARDS_DUT | 3801 (0xed9) | Port 2 of the S2P is oriented towards the DUT port. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

De-embedding

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__deembedding_1ga8fbbb3bcd0e5d0dcf19582bc200ed77c.html language=enus -->
## TOPIC 00119: niRFSA_ConfigureDeembeddingTableInterpolationSpline

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__deembedding_1ga8fbbb3bcd0e5d0dcf19582bc200ed77c.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__deembedding_1ga8fbbb3bcd0e5d0dcf19582bc200ed77c.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects the spline interpolation method. SyntaxViStatus _VI_FUNC niRFSA_ConfigureDeembeddingTableInterpolationSpline(ViSession vi, ViConstString port, ViConstString tableName)RemarksIf the carrier frequency does not match a row in the de-embedding table, NI-RFSA performs a spline interpolation based

### niRFSA_ConfigureDeembeddingTableInterpolationSpline

Selects the spline interpolation method.

#### Syntax

ViStatus _VI_FUNC niRFSA_ConfigureDeembeddingTableInterpolationSpline(ViSession vi, ViConstString port, ViConstString tableName)

#### Remarks

If the carrier frequency does not match a row in the de-embedding table, NI-RFSA performs a spline interpolation based on the entries in the de-embedding table to determine the parameters to use for de-embedding.

**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| port | [in] | ViConstString | Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string). |
| tableName | [in] | ViConstString | Specifies the name of the table. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

De-embedding

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__deembedding_1gaa3bea2c17c79302ba811aa97186337f5.html language=enus -->
## TOPIC 00120: niRFSA_DeleteAllDeembeddingTables

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__deembedding_1gaa3bea2c17c79302ba811aa97186337f5.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__deembedding_1gaa3bea2c17c79302ba811aa97186337f5.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes all configured de-embedding tables for the session. SyntaxViStatus _VI_FUNC niRFSA_DeleteAllDeembeddingTables(ViSession vi)RemarksSupported Devices: PXIe-5830/5831/5832/5840/5841/5842/5860ParametersNameDirectionTypeDescriptionvi[in]ViSessionIdentifies your instrument session. vi is obtained

### niRFSA_DeleteAllDeembeddingTables

Deletes all configured de-embedding tables for the session.

#### Syntax

ViStatus _VI_FUNC niRFSA_DeleteAllDeembeddingTables(ViSession vi)

#### Remarks

**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

De-embedding

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__deembedding_1gab7c8c62278e973038b46b109aa661ca0.html language=enus -->
## TOPIC 00121: niRFSA_CreateDeembeddingSparameterTableArray

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__deembedding_1gab7c8c62278e973038b46b109aa661ca0.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__deembedding_1gab7c8c62278e973038b46b109aa661ca0.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an s-parameter de-embedding table for the port from the input data. SyntaxViStatus _VI_FUNC niRFSA_CreateDeembeddingSparameterTableArray(ViSession vi, ViConstString port, ViConstString tableName, const ViReal64 frequencies[], ViInt32 frequenciesSize, const ni complex number f64 sparameterTab

### niRFSA_CreateDeembeddingSparameterTableArray

Creates an s-parameter de-embedding table for the port from the input data.

#### Syntax

ViStatus _VI_FUNC niRFSA_CreateDeembeddingSparameterTableArray(ViSession vi, ViConstString port, ViConstString tableName, const ViReal64 frequencies[], ViInt32 frequenciesSize, const ni complex number f64 sparameterTable[], ViInt32 sparameterTableSize, ViInt32 numberOfPorts, ViInt32 sparameterOrientation)

#### Remarks

If you only create one table for a port, NI-RFSA automatically selects that table to de-embed the measurement.

**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[De-embedding Overview](https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html)

[S-parameters](https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html#GUID-0AD828DE-398A-45C6-ABBA-4208DEB7DE1B__GUID-67A69775-E4DB-4FA2-84FE-C05977ED4184)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| port | [in] | ViConstString | Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string). |
| tableName | [in] | ViConstString | Specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced. |
| frequencies | [in] | const ViReal64[] | Specifies the frequencies for the sparameterTable rows. Frequencies must be unique and in ascending order. |
| frequenciesSize | [in] | ViInt32 | Specifies the size of the frequency. |
| sparameterTable | [in] | const ni complex number f64[] | Specifies the S-parameters for each frequency. S-parameters for each frequency are placed in the array in the following order: s11, s12, s21, s22. |
| sparameterTableSize | [in] | ViInt32 | Specifies the size of the S-parameter table. |
| numberOfPorts | [in] | ViInt32 | Specifies the number of DUT ports. |
| sparameterOrientation | [in] | ViInt32 | Specifies the orientation of the data in the S2P file relative to the port on the DUT port.NameValueDescriptionNIRFSA_VAL_PORT1_TOWARDS_DUT3800 (0xed8)Port 1 of the S2P is oriented towards the DUT port.NIRFSA_VAL_PORT2_TOWARDS_DUT3801 (0xed9)Port 2 of the S2P is oriented towards the DUT port. |
| Name | Value | Description |  |
| NIRFSA_VAL_PORT1_TOWARDS_DUT | 3800 (0xed8) | Port 1 of the S2P is oriented towards the DUT port. |  |
| NIRFSA_VAL_PORT2_TOWARDS_DUT | 3801 (0xed9) | Port 2 of the S2P is oriented towards the DUT port. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

De-embedding

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__deembedding_1gac5a918ee851f84603a70c217fd3dfb93.html language=enus -->
## TOPIC 00122: niRFSA_ConfigureDeembeddingTableInterpolationLinear

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__deembedding_1gac5a918ee851f84603a70c217fd3dfb93.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__deembedding_1gac5a918ee851f84603a70c217fd3dfb93.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects the linear interpolation method. SyntaxViStatus _VI_FUNC niRFSA_ConfigureDeembeddingTableInterpolationLinear(ViSession vi, ViConstString port, ViConstString tableName, ViInt32 format)RemarksIf the carrier frequency does not match a row in the de-embedding table, NI-RFSA performs a linear int

### niRFSA_ConfigureDeembeddingTableInterpolationLinear

Selects the linear interpolation method.

#### Syntax

ViStatus _VI_FUNC niRFSA_ConfigureDeembeddingTableInterpolationLinear(ViSession vi, ViConstString port, ViConstString tableName, ViInt32 format)

#### Remarks

If the carrier frequency does not match a row in the de-embedding table, NI-RFSA performs a linear interpolation based on the entries in the de-embedding table to determine the parameters to use for de-embedding.

**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| port | [in] | ViConstString | Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string). |
| tableName | [in] | ViConstString | Specifies the name of the table. |
| format | [in] | ViInt32 | Specifies the format of parameters to interpolate.NameValueDescriptionNIRFSA_VAL_LINEAR_INTERPOLATION_FORMAT_REAL_AND_IMAGINARY4000 (0xfa0)Results in a linear interpolation of the magnitude, in decibels, and a separate linear interpolation of the phase.NIRFSA_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_AND_PHASE4001 (0xfa1)Results in a linear interpolation of the real portion of the complex number and a separate linear interpolation of the complex portion.NIRFSA_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_DB_AND_PHASE4002 (0xfa2)Results in a linear interpolation of the magnitude and a separate linear interpolation of the phase. |
| Name | Value | Description |  |
| NIRFSA_VAL_LINEAR_INTERPOLATION_FORMAT_REAL_AND_IMAGINARY | 4000 (0xfa0) | Results in a linear interpolation of the magnitude, in decibels, and a separate linear interpolation of the phase. |  |
| NIRFSA_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_AND_PHASE | 4001 (0xfa1) | Results in a linear interpolation of the real portion of the complex number and a separate linear interpolation of the complex portion. |  |
| NIRFSA_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_DB_AND_PHASE | 4002 (0xfa2) | Results in a linear interpolation of the magnitude and a separate linear interpolation of the phase. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

De-embedding

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__iq.html language=enus -->
## TOPIC 00123: IQ

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__iq.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__iq.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniRFSA_ConfigureIqCarrierFrequencyConfigures the carrier frequency of the RF vector signal analyzer hardware for an I/Q acquisition. niRFSA_ConfigureIqRateSpecifies the I/Q rate for the acquisition. niRFSA_ConfigureNumberOfRecordsConfigures the number of records

### IQ

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niRFSA_ConfigureIqCarrierFrequency | Configures the carrier frequency of the RF vector signal analyzer hardware for an I/Q acquisition. |
| niRFSA_ConfigureIqRate | Specifies the I/Q rate for the acquisition. |
| niRFSA_ConfigureNumberOfRecords | Configures the number of records in a finite acquisition or configures the device to continuously acquire records. |
| niRFSA_ConfigureNumberOfSamples | Configures the number of samples in a finite acquisition or configures the device to continuously acquire samples. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__iq_1ga357d6779ea861fb4fdbf1fb620f4284d.html language=enus -->
## TOPIC 00124: niRFSA_ConfigureNumberOfSamples

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__iq_1ga357d6779ea861fb4fdbf1fb620f4284d.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__iq_1ga357d6779ea861fb4fdbf1fb620f4284d.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of samples in a finite acquisition or configures the device to continuously acquire samples. SyntaxViStatus _VI_FUNC niRFSA_ConfigureNumberOfSamples(ViSession vi, ViConstString channelList, ViBoolean numberOfSamplesIsFinite, ViInt64 samplesPerRecord)RemarksIf you configure the

### niRFSA_ConfigureNumberOfSamples

Configures the number of samples in a finite acquisition or configures the device to continuously acquire samples.

#### Syntax

ViStatus _VI_FUNC niRFSA_ConfigureNumberOfSamples(ViSession vi, ViConstString channelList, ViBoolean numberOfSamplesIsFinite, ViInt64 samplesPerRecord)

#### Remarks

If you configure the device for finite acquisition, it acquires the specified number of samples and then stops the acquisition. You can configure the device to acquire multiple records using the [niRFSA_ConfigureNumberOfRecords](group____root__ni_r_f_s_a__functions__configuration__iq_1gaf9073bff85bfbacfc1c6c0a99204f4cc.html) function. Each record contains the number of samples specified in this function.

If you configure the device to continuously acquire samples, it continues acquiring data until you call the [niRFSA_Abort](group____root__ni_r_f_s_a__functions__acquisition__iq__acquisition_1gac0c68f58ffb15698074be6f5cc2ed751.html) function to abort the acquisition. The device stores data in onboard memory in a circular fashion. After the device fills the memory, it starts overwriting previously acquired data from the beginning of the memory buffer. Retrieve the samples as they are being acquired, using one of the niRFSA fetch I/Q functions, to avoid overwriting data before you retrieve it.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[I/Q Modulation](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| channelList | [in] | ViConstString | Identifies which channels to apply settings. Specify an empty string as the value of this parameter. |
| numberOfSamplesIsFinite | [in] | ViBoolean | Specifies whether to configure the device to acquire a finite number of samples or to acquire samples continuously. The default is VI_TRUE.ValueDescriptionVI_TRUEThe device acquires a finite number of samples.VI_FALSEThe device acquires samples continuously until you call the niRFSA_Abort function to abort the acquisition. |
| Value | Description |  |  |
| VI_TRUE | The device acquires a finite number of samples. |  |  |
| VI_FALSE | The device acquires samples continuously until you call the niRFSA_Abort function to abort the acquisition. |  |  |
| samplesPerRecord | [in] | ViInt64 | Specifies the number of samples per record if numberOfSamplesIsFinite is set to VI_TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

IQ

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__iq_1gabe52587ac0806c784050c2e74bdf89af.html language=enus -->
## TOPIC 00125: niRFSA_ConfigureIqRate

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__iq_1gabe52587ac0806c784050c2e74bdf89af.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__iq_1gabe52587ac0806c784050c2e74bdf89af.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the I/Q rate for the acquisition. SyntaxViStatus _VI_FUNC niRFSA_ConfigureIqRate(ViSession vi, ViConstString channelList, ViReal64 iqRate)RemarksThe value is expressed in samples per second (S/s).For the PXIe-5663/5663E/5665/5667/5668, when you set the NIRFSA_ATTR_DIGITIZER_SAMPLE_CLOCK_TI

### niRFSA_ConfigureIqRate

Specifies the I/Q rate for the acquisition.

#### Syntax

ViStatus _VI_FUNC niRFSA_ConfigureIqRate(ViSession vi, ViConstString channelList, ViReal64 iqRate)

#### Remarks

The value is expressed in samples per second (S/s).

For the PXIe-5663/5663E/5665/5667/5668, when you set the [NIRFSA_ATTR_DIGITIZER_SAMPLE_CLOCK_TIMEBASE_SOURCE](group____root__ni_r_f_s_a__attributes__clocking_1ga7a95c6ae58d24bca6dddecff7182ff77.html) attribute to **NIRFSA_VAL_ONBOARD_CLOCK_STR**, the digitizer bandwidth is greater than or equal to the coerced **iqRate** times 0.8. Actual signal bandwidth is limited for all supported devices by the anti-aliasing filter. Further device-specific limitations are as follows.

Note

For the PXIe-5663/5663E/5665/5667/5668, NI-RFSA enables dithering by default. The dither noise can appear in your passband and affect your measurements. Refer to the [NIRFSA_ATTR_DIGITIZER_DITHER_ENABLED](group____root__ni_r_f_s_a__attributes__signal__path_1ga7065372afe424ff665f553e15886d4ad.html) attribute for more information about dithering.

- **PXI-5661** You should not need to configure an **iqRate** higher than 25 megasamples per second (MS/s) because the PXI-5600 RF downconverter bandwidth is 20 MHz. If you configure a higher I/Q rate, you may see aliasing effects at negative frequencies because the IF frequency of the PXI-5600 RF downconverter is 15 MHz.
- **PXIe-5663/5663E** Maximum allowed instantaneous bandwidth depends on the I/Q carrier frequency you use. Refer to the [PXIe-5601 RF downconverter overview](https://www.ni.com/docs/en-US/bundle/pxie-5663-5663e-feature/page/overview.3.html) for more information about instantaneous bandwidth.
- **PXIe-5665** Actual signal bandwidth is limited by the preselector and the combination of the chosen IF filter and anti-aliasing filter. Maximum allowed instantaneous bandwidth is independent of the downconverter center frequency for frequencies less than 3.6 GHz. At frequencies greater than 3.6 GHz, if your device supports the preselector (YIG-tuned filter) and you have enabled it for your application, the maximum allowed instantaneous bandwidth is limited to the instantaneous bandwidth of the preselector. Refer to the *NI PXIe-5665 Specifications* for more information about instantaneous bandwidth limits.
- **PXIe-5667** Actual signal bandwidth is limited by the preselector and the combination of the chosen IF filter and anti-aliasing filter. Maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use. Refer to the *NI PXIe-5667 Specifications* for more information about instantaneous bandwidth limits.
- **PXIe-5668** Actual signal bandwidth is limited by the FPGA image that is downloaded upon opening the session to the PXIe-5624 digitizer. Maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use. Refer to the *PXIe-5668 Specifications* for more information about instantaneous bandwidth limits.
- **PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842** Maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use. Refer to the specifications document for your device for more information about instantaneous bandwidth limits.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[I/Q Modulation](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| channelList | [in] | ViConstString | Identifies which channels to apply settings. Specify an empty string as the value of this parameter. |
| iqRate | [in] | ViReal64 | Specifies the I/Q rate for the acquisition. The value is expressed in samples per second (S/s). |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

IQ

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__iq_1gac9a524df75b7128131ae50959465edf7.html language=enus -->
## TOPIC 00126: niRFSA_ConfigureIqCarrierFrequency

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__iq_1gac9a524df75b7128131ae50959465edf7.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__iq_1gac9a524df75b7128131ae50959465edf7.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the carrier frequency of the RF vector signal analyzer hardware for an I/Q acquisition. SyntaxViStatus _VI_FUNC niRFSA_ConfigureIqCarrierFrequency(ViSession vi, ViConstString channelList, ViReal64 carrierFrequency)RemarksThe carrier frequency is the center frequency of the I/Q acquisition

### niRFSA_ConfigureIqCarrierFrequency

Configures the [carrier frequency](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/fund-carrierwave.html) of the RF vector signal analyzer hardware for an I/Q acquisition.

#### Syntax

ViStatus _VI_FUNC niRFSA_ConfigureIqCarrierFrequency(ViSession vi, ViConstString channelList, ViReal64 carrierFrequency)

#### Remarks

The carrier frequency is the center frequency of the I/Q acquisition.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Carrier Wave](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/fund-carrierwave.html)

[I/Q Modulation](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| channelList | [in] | ViConstString | Identifies which channels to apply settings. Specify an empty string as the value of this parameter. |
| carrierFrequency | [in] | ViReal64 | Specifies the carrier frequency, in hertz (Hz), of the RF signal to acquire.The RF vector signal analyzer tunes to this frequency. NI-RFSA may coerce this value based on hardware settings and downconversion settings.NI-RFSA sets the NIRFSA_ATTR_IQ_CARRIER_FREQUENCY attribute to this value. Refer to the specifications document that shipped with your device for allowable frequency settings. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

IQ

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__iq_1gaf9073bff85bfbacfc1c6c0a99204f4cc.html language=enus -->
## TOPIC 00127: niRFSA_ConfigureNumberOfRecords

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__iq_1gaf9073bff85bfbacfc1c6c0a99204f4cc.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__iq_1gaf9073bff85bfbacfc1c6c0a99204f4cc.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of records in a finite acquisition or configures the device to continuously acquire records. SyntaxViStatus _VI_FUNC niRFSA_ConfigureNumberOfRecords(ViSession vi, ViConstString channelList, ViBoolean numberOfRecordsIsFinite, ViInt64 numberOfRecords)RemarksYou can only configure

### niRFSA_ConfigureNumberOfRecords

Configures the number of records in a finite acquisition or configures the device to continuously acquire records.

#### Syntax

ViStatus _VI_FUNC niRFSA_ConfigureNumberOfRecords(ViSession vi, ViConstString channelList, ViBoolean numberOfRecordsIsFinite, ViInt64 numberOfRecords)

#### Remarks

You can only configure the device to acquire multiple records if you set the **numberOfRecordsIsFinite** parameter to VI_TRUE.

If you configure the device to continuously acquire samples, it continues acquiring data until you call the [niRFSA_Abort](group____root__ni_r_f_s_a__functions__acquisition__iq__acquisition_1gac0c68f58ffb15698074be6f5cc2ed751.html) function to abort the acquisition. The device stores data in onboard memory in a circular fashion. After the device fills the memory, it starts overwriting previously acquired data from the beginning of the memory buffer. Retrieve the samples as they are being acquired, using one of the niRFSA fetch I/Q functions, to avoid overwriting data before you retrieve it.

To acquire more records than will fit into the device memory without continuously acquiring records, set the **numberOfRecordsIsFinite** parameter in this function to VI_TRUE and the [NIRFSA_ATTR_ALLOW_MORE_RECORDS_THAN_MEMORY](group____root__ni_r_f_s_a__attributes__acquisition__iq_1ga63f1620e7abecc8a0b1c0eb9adeb7347.html) attribute to VI_TRUE.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[I/Q Modulation](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| channelList | [in] | ViConstString | Identifies which channels to apply settings. Specify an empty string as the value of this parameter. |
| numberOfRecordsIsFinite | [in] | ViBoolean | Specifies whether to configure the device to acquire a finite number of records or to acquire records continuously. The default is VI_TRUE.ValueDescriptionVI_TRUEThe device acquires a finite number of records.VI_FALSEThe NI-RFSA device acquires records continuously until you call the niRFSA_Abort function to abort the acquisition. |
| Value | Description |  |  |
| VI_TRUE | The device acquires a finite number of records. |  |  |
| VI_FALSE | The NI-RFSA device acquires records continuously until you call the niRFSA_Abort function to abort the acquisition. |  |  |
| numberOfRecords | [in] | ViInt64 | Specifies the number of records to acquire if numberOfRecordsIsFinite is set to VI_TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

IQ

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute.html language=enus -->
## TOPIC 00128: Set/Get/Reset Attribute

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsGet AttributeSet AttributeGroup membersNameDescriptionniRFSA_ResetAttributeResets the attribute to its default value. AttachmentsNone

### Set/Get/Reset Attribute

#### Groups

- Get Attribute
- Set Attribute

#### Group members

| Name | Description |
| --- | --- |
| niRFSA_ResetAttribute | Resets the attribute to its default value. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute_1ga38b2830fef34e0e908125fdb4ae691cf.html language=enus -->
## TOPIC 00129: niRFSA_ResetAttribute

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute_1ga38b2830fef34e0e908125fdb4ae691cf.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute_1ga38b2830fef34e0e908125fdb4ae691cf.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the attribute to its default value. SyntaxViStatus _VI_FUNC niRFSA_ResetAttribute(ViSession vi, ViConstString channelName, ViAttr attributeId)RemarksSupported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668,

### niRFSA_ResetAttribute

Resets the attribute to its default value.

#### Syntax

ViStatus _VI_FUNC niRFSA_ResetAttribute(ViSession vi, ViConstString channelName, ViAttr attributeId)

#### Remarks

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| channelName | [in] | ViConstString | Specifies the name of the channel on which to reset the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL. |
| attributeId | [in] | ViAttr | Pass the ID of an attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set/Get/Reset Attribute

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__get__attribute.html language=enus -->
## TOPIC 00130: Get Attribute

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__get__attribute.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__get__attribute.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniRFSA_GetAttributeViBooleanQueries the value of a ViBoolean attribute. niRFSA_GetAttributeViInt32Queries the value of a ViInt32 attribute. niRFSA_GetAttributeViInt64Queries the value of a ViInt64 attribute. niRFSA_GetAttributeViReal64Queries the value of a ViRe

### Get Attribute

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niRFSA_GetAttributeViBoolean | Queries the value of a ViBoolean attribute. |
| niRFSA_GetAttributeViInt32 | Queries the value of a ViInt32 attribute. |
| niRFSA_GetAttributeViInt64 | Queries the value of a ViInt64 attribute. |
| niRFSA_GetAttributeViReal64 | Queries the value of a ViReal64 attribute. |
| niRFSA_GetAttributeViSession | Queries the value of a ViSession attribute. |
| niRFSA_GetAttributeViString | Queries the value of a ViString attribute. |

#### Attachments

None

Parent topic:

Set/Get/Reset Attribute

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__get__attribute_1ga022e71baa54182bca9cd93590ed9f56c.html language=enus -->
## TOPIC 00131: niRFSA_GetAttributeViString

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__get__attribute_1ga022e71baa54182bca9cd93590ed9f56c.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__get__attribute_1ga022e71baa54182bca9cd93590ed9f56c.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of a ViString attribute. SyntaxViStatus _VI_FUNC niRFSA_GetAttributeViString(ViSession vi, ViConstString channelName, ViAttr attributeId, ViInt32 bufSize, ViConstString value[])RemarksYou can use this low-level function to get the values of inherent IVI attributes and instrument-sp

### niRFSA_GetAttributeViString

Queries the value of a ViString attribute.

#### Syntax

ViStatus _VI_FUNC niRFSA_GetAttributeViString(ViSession vi, ViConstString channelName, ViAttr attributeId, ViInt32 bufSize, ViConstString value[])

#### Remarks

You can use this low-level function to get the values of inherent IVI attributes and instrument-specific attributes.

You must provide a ViChar array to serve as a buffer for the value. You pass the number of bytes in the buffer as the **bufSize** parameter. If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **bufSize** parameter, the function copies buffer size 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

If you want to call this function just to get the required buffer size, you can pass 0 for **bufSize** and VI_NULL for the **attributeValue** buffer.

**Supported Devices:** PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| channelName | [in] | ViConstString | Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL. |
| attributeId | [in] | ViAttr | Pass the ID of an attribute. |
| bufSize | [in] | ViInt32 | Pass the number of bytes in the ViChar buffer you specify for the attribute value parameter.If you pass 0, you can pass VI_NULL for the attribute value buffer parameter. |
| value | [in] | ViConstString[] | The buffer in which the function returns the current value of the attribute. The buffer must be of type ViChar and have at least as many bytes as indicated in bufSize.If you specify 0 for the bufSize parameter, you can pass VI_NULL for this parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. You examine the status code from each call to an instrument driver function to determine if an error occurred. To obtain a text description of the status code, call the [niRFSA_ErrorMessage](group____root__ni_r_f_s_a__functions__utility__error__info_1gaffa80b8edb502a32d6a44cb31926eacf.html) function. To obtain additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from the driver, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attribute

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__get__attribute_1ga1b416a559059ce46fabc03b43f1ea025.html language=enus -->
## TOPIC 00132: niRFSA_GetAttributeViReal64

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__get__attribute_1ga1b416a559059ce46fabc03b43f1ea025.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__get__attribute_1ga1b416a559059ce46fabc03b43f1ea025.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of a ViReal64 attribute. SyntaxViStatus _VI_FUNC niRFSA_GetAttributeViReal64(ViSession vi, ViConstString channelName, ViAttr attributeId, ViReal64 *value)RemarksYou can use this low-level function to get the values of inherent IVI attributes and instrument-specific attributes.Suppo

### niRFSA_GetAttributeViReal64

Queries the value of a ViReal64 attribute.

#### Syntax

ViStatus _VI_FUNC niRFSA_GetAttributeViReal64(ViSession vi, ViConstString channelName, ViAttr attributeId, ViReal64 *value)

#### Remarks

You can use this low-level function to get the values of inherent IVI attributes and instrument-specific attributes.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| channelName | [in] | ViConstString | Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL. |
| attributeId | [in] | ViAttr | Pass the ID of an attribute. |
| value | [out] | ViReal64 * | Returns the current value of the attribute. Pass the address of a ViReal64 variable. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attribute

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__get__attribute_1ga35231e4a85509f65ca9db132019bf944.html language=enus -->
## TOPIC 00133: niRFSA_GetAttributeViInt64

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__get__attribute_1ga35231e4a85509f65ca9db132019bf944.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__get__attribute_1ga35231e4a85509f65ca9db132019bf944.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of a ViInt64 attribute. SyntaxViStatus _VI_FUNC niRFSA_GetAttributeViInt64(ViSession vi, ViConstString channelName, ViAttr attributeId, ViInt64 *value)RemarksYou can use this low-level function to get the values of inherent IVI attributes and instrument-specific attributes.Supporte

### niRFSA_GetAttributeViInt64

Queries the value of a ViInt64 attribute.

#### Syntax

ViStatus _VI_FUNC niRFSA_GetAttributeViInt64(ViSession vi, ViConstString channelName, ViAttr attributeId, ViInt64 *value)

#### Remarks

You can use this low-level function to get the values of inherent IVI attributes and instrument-specific attributes.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| channelName | [in] | ViConstString | Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL. |
| attributeId | [in] | ViAttr | Pass the ID of an attribute. |
| value | [out] | ViInt64 * | Returns the current value of the attribute. Pass the address of a ViInt64 variable. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attribute

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__get__attribute_1ga3d0a53dc62baea62acf06d90718169b9.html language=enus -->
## TOPIC 00134: niRFSA_GetAttributeViBoolean

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__get__attribute_1ga3d0a53dc62baea62acf06d90718169b9.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__get__attribute_1ga3d0a53dc62baea62acf06d90718169b9.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of a ViBoolean attribute. SyntaxViStatus _VI_FUNC niRFSA_GetAttributeViBoolean(ViSession vi, ViConstString channelName, ViAttr attributeId, ViBoolean *value)RemarksYou can use this low-level function to get the values of inherent IVI attributes and instrument-specific attributes.Su

### niRFSA_GetAttributeViBoolean

Queries the value of a ViBoolean attribute.

#### Syntax

ViStatus _VI_FUNC niRFSA_GetAttributeViBoolean(ViSession vi, ViConstString channelName, ViAttr attributeId, ViBoolean *value)

#### Remarks

You can use this low-level function to get the values of inherent IVI attributes and instrument-specific attributes.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| channelName | [in] | ViConstString | Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL. |
| attributeId | [in] | ViAttr | Pass the ID of an attribute. |
| value | [out] | ViBoolean * | Returns the current value of the attribute. Pass the address of a ViBoolean variable. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attribute

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__get__attribute_1ga6e5801fba7db2aca84140667bc687e89.html language=enus -->
## TOPIC 00135: niRFSA_GetAttributeViInt32

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__get__attribute_1ga6e5801fba7db2aca84140667bc687e89.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__get__attribute_1ga6e5801fba7db2aca84140667bc687e89.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of a ViInt32 attribute. SyntaxViStatus _VI_FUNC niRFSA_GetAttributeViInt32(ViSession vi, ViConstString channelName, ViAttr attributeId, ViInt32 *value)RemarksYou can use this low-level function to get the values of inherent IVI attributes and instrument-specific attributes.Supporte

### niRFSA_GetAttributeViInt32

Queries the value of a ViInt32 attribute.

#### Syntax

ViStatus _VI_FUNC niRFSA_GetAttributeViInt32(ViSession vi, ViConstString channelName, ViAttr attributeId, ViInt32 *value)

#### Remarks

You can use this low-level function to get the values of inherent IVI attributes and instrument-specific attributes.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| channelName | [in] | ViConstString | Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL. |
| attributeId | [in] | ViAttr | Pass the ID of an attribute. |
| value | [out] | ViInt32 * | Returns the current value of the attribute. Pass the address of a ViInt32 variable. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attribute

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__get__attribute_1gadb2df4d7306b475a2a4a90603be0cd7d.html language=enus -->
## TOPIC 00136: niRFSA_GetAttributeViSession

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__get__attribute_1gadb2df4d7306b475a2a4a90603be0cd7d.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__get__attribute_1gadb2df4d7306b475a2a4a90603be0cd7d.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of a ViSession attribute. SyntaxViStatus _VI_FUNC niRFSA_GetAttributeViSession(ViSession vi, ViConstString channelName, ViAttr attributeId, ViSession *value)RemarksYou can use this low-level function to get the values of inherent IVI attributes and instrument-specific attributes.Su

### niRFSA_GetAttributeViSession

Queries the value of a ViSession attribute.

#### Syntax

ViStatus _VI_FUNC niRFSA_GetAttributeViSession(ViSession vi, ViConstString channelName, ViAttr attributeId, ViSession *value)

#### Remarks

You can use this low-level function to get the values of inherent IVI attributes and instrument-specific attributes.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| channelName | [in] | ViConstString | Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL. |
| attributeId | [in] | ViAttr | Pass the ID of an attribute. |
| value | [out] | ViSession * | Returns the current value of the attribute. Pass the address of a ViSession variable. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attribute

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__set__attribute.html language=enus -->
## TOPIC 00137: Set Attribute

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__set__attribute.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__set__attribute.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniRFSA_SetAttributeViBooleanSets the value of a ViBoolean attribute. niRFSA_SetAttributeViInt32Sets the value of a ViInt32 attribute. niRFSA_SetAttributeViInt64Sets the value of a ViInt64 attribute. niRFSA_SetAttributeViReal64Sets the value of a ViReal64 attribu

### Set Attribute

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niRFSA_SetAttributeViBoolean | Sets the value of a ViBoolean attribute. |
| niRFSA_SetAttributeViInt32 | Sets the value of a ViInt32 attribute. |
| niRFSA_SetAttributeViInt64 | Sets the value of a ViInt64 attribute. |
| niRFSA_SetAttributeViReal64 | Sets the value of a ViReal64 attribute. |
| niRFSA_SetAttributeViSession | Sets the value of a ViSession attribute. |
| niRFSA_SetAttributeViString | Sets the value of a ViString attribute. |

#### Attachments

None

Parent topic:

Set/Get/Reset Attribute

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__set__attribute_1ga2d96bd6d84e77346d224cf59e824c591.html language=enus -->
## TOPIC 00138: niRFSA_SetAttributeViInt64

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__set__attribute_1ga2d96bd6d84e77346d224cf59e824c591.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__set__attribute_1ga2d96bd6d84e77346d224cf59e824c591.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a ViInt64 attribute. SyntaxViStatus _VI_FUNC niRFSA_SetAttributeViInt64(ViSession vi, ViConstString channelName, ViAttr attributeId, ViInt64 value)RemarksUse this low-level function to set the values of inherent IVI attributes and instrument-specific attributes.NI-RFSA contains hig

### niRFSA_SetAttributeViInt64

Sets the value of a ViInt64 attribute.

#### Syntax

ViStatus _VI_FUNC niRFSA_SetAttributeViInt64(ViSession vi, ViConstString channelName, ViAttr attributeId, ViInt64 value)

#### Remarks

Use this low-level function to set the values of inherent IVI attributes and instrument-specific attributes.

NI-RFSA contains high-level functions that set most of the instrument attributes. NI recommends you use the high-level functions as much as possible. High-level functions handle order dependencies and multithread locking for you.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| channelName | [in] | ViConstString | Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL. |
| attributeId | [in] | ViAttr | Pass the ID of an attribute. |
| value | [in] | ViInt64 | Pass the value to which you want to set the attribute.Some of the values might not be valid depending on the current state of the instrument session. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attribute

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__set__attribute_1ga36a5db3f92931d869655a49e3ba7d387.html language=enus -->
## TOPIC 00139: niRFSA_SetAttributeViString

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__set__attribute_1ga36a5db3f92931d869655a49e3ba7d387.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__set__attribute_1ga36a5db3f92931d869655a49e3ba7d387.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a ViString attribute. SyntaxViStatus _VI_FUNC niRFSA_SetAttributeViString(ViSession vi, ViConstString channelName, ViAttr attributeId, ViConstString value)RemarksUse this low-level function to set the values of inherent IVI attributes and instrument-specific attributes.NI-RFSA cont

### niRFSA_SetAttributeViString

Sets the value of a ViString attribute.

#### Syntax

ViStatus _VI_FUNC niRFSA_SetAttributeViString(ViSession vi, ViConstString channelName, ViAttr attributeId, ViConstString value)

#### Remarks

Use this low-level function to set the values of inherent IVI attributes and instrument-specific attributes.

NI-RFSA contains high-level functions that set most of the instrument attributes. NI recommends you use the high-level functions as much as possible. High-level functions handle order dependencies and multithread locking for you.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| channelName | [in] | ViConstString | Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL. |
| attributeId | [in] | ViAttr | Pass the ID of an attribute. |
| value | [in] | ViConstString | Pass the value to which you want to set the attribute.Some of the values might not be valid depending on the current state of the instrument session. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attribute

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__set__attribute_1ga83604225ff1726873f8c8b65946abb93.html language=enus -->
## TOPIC 00140: niRFSA_SetAttributeViReal64

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__set__attribute_1ga83604225ff1726873f8c8b65946abb93.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__set__attribute_1ga83604225ff1726873f8c8b65946abb93.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a ViReal64 attribute. SyntaxViStatus _VI_FUNC niRFSA_SetAttributeViReal64(ViSession vi, ViConstString channelName, ViAttr attributeId, ViReal64 value)RemarksUse this low-level function to set the values of inherent IVI attributes, and instrument-specific attributes.NI-RFSA contains

### niRFSA_SetAttributeViReal64

Sets the value of a ViReal64 attribute.

#### Syntax

ViStatus _VI_FUNC niRFSA_SetAttributeViReal64(ViSession vi, ViConstString channelName, ViAttr attributeId, ViReal64 value)

#### Remarks

Use this low-level function to set the values of inherent IVI attributes, and instrument-specific attributes.

NI-RFSA contains high-level functions that set most of the instrument attributes. NI recommends you use the high-level functions as much as possible. High-level functions handle order dependencies and multithread-locking for you.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| channelName | [in] | ViConstString | Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL. |
| attributeId | [in] | ViAttr | Pass the ID of an attribute. |
| value | [in] | ViReal64 | Pass the value to which you want to set the attribute.Some of the values might not be valid depending on the current state of the instrument session. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attribute

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__set__attribute_1gaaaa9a115b86c0170bb0ce4c7cc1b1f98.html language=enus -->
## TOPIC 00141: niRFSA_SetAttributeViBoolean

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__set__attribute_1gaaaa9a115b86c0170bb0ce4c7cc1b1f98.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__set__attribute_1gaaaa9a115b86c0170bb0ce4c7cc1b1f98.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a ViBoolean attribute. SyntaxViStatus _VI_FUNC niRFSA_SetAttributeViBoolean(ViSession vi, ViConstString channelName, ViAttr attributeId, ViBoolean value)RemarksUse this low-level function to set the values of inherent IVI attributes and instrument-specific attributes.NI-RFSA contai

### niRFSA_SetAttributeViBoolean

Sets the value of a ViBoolean attribute.

#### Syntax

ViStatus _VI_FUNC niRFSA_SetAttributeViBoolean(ViSession vi, ViConstString channelName, ViAttr attributeId, ViBoolean value)

#### Remarks

Use this low-level function to set the values of inherent IVI attributes and instrument-specific attributes.

NI-RFSA contains high-level functions that set most of the instrument attributes. NI recommends you use the high-level functions as much as possible. High-level functions handle order dependencies and multithread locking for you.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| channelName | [in] | ViConstString | Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL. |
| attributeId | [in] | ViAttr | Pass the ID of an attribute. |
| value | [in] | ViBoolean | Pass the value to which you want to set the attribute.Some of the values might not be valid depending on the current state of the instrument session. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attribute

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__set__attribute_1gad1a832c95846f77352291eb84e6d8aed.html language=enus -->
## TOPIC 00142: niRFSA_SetAttributeViSession

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__set__attribute_1gad1a832c95846f77352291eb84e6d8aed.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__set__attribute_1gad1a832c95846f77352291eb84e6d8aed.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a ViSession attribute. SyntaxViStatus _VI_FUNC niRFSA_SetAttributeViSession(ViSession vi, ViConstString channelName, ViAttr attributeId, ViSession value)RemarksUse this low-level function to set the values of inherent IVI attributes and instrument-specific attributes.NI-RFSA contai

### niRFSA_SetAttributeViSession

Sets the value of a ViSession attribute.

#### Syntax

ViStatus _VI_FUNC niRFSA_SetAttributeViSession(ViSession vi, ViConstString channelName, ViAttr attributeId, ViSession value)

#### Remarks

Use this low-level function to set the values of inherent IVI attributes and instrument-specific attributes.

NI-RFSA contains high-level functions that set most of the instrument attributes. NI recommends you use the high-level functions as much as possible. High-level functions handle order dependencies and multithread locking for you.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| channelName | [in] | ViConstString | Specifies the name of the channel on which to check the attribute value if the attribute is channel based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL. |
| attributeId | [in] | ViAttr | Pass the ID of an attribute. |
| value | [in] | ViSession | Pass the value to which you want to set the attribute.Some of the values might not be valid depending on the current state of the instrument session. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attribute

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__set__attribute_1gadad886cf26a3eba02ecd60a38e4eefcd.html language=enus -->
## TOPIC 00143: niRFSA_SetAttributeViInt32

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__set__attribute_1gadad886cf26a3eba02ecd60a38e4eefcd.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__setgetreset__attribute__set__attribute_1gadad886cf26a3eba02ecd60a38e4eefcd.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a ViInt32 attribute. SyntaxViStatus _VI_FUNC niRFSA_SetAttributeViInt32(ViSession vi, ViConstString channelName, ViAttr attributeId, ViInt32 value)RemarksUse this low-level function to set the values of inherent IVI attributes and instrument-specific attributes.NI-RFSA contains hig

### niRFSA_SetAttributeViInt32

Sets the value of a ViInt32 attribute.

#### Syntax

ViStatus _VI_FUNC niRFSA_SetAttributeViInt32(ViSession vi, ViConstString channelName, ViAttr attributeId, ViInt32 value)

#### Remarks

Use this low-level function to set the values of inherent IVI attributes and instrument-specific attributes.

NI-RFSA contains high-level functions that set most of the instrument attributes. NI recommends you use the high-level functions as much as possible. High-level functions handle order dependencies and multithread locking for you.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| channelName | [in] | ViConstString | Specifies the name of the channel on which to check the attribute value if the attribute is channel-based. If the attribute is not channel based, set this parameter to "" (empty string) or VI_NULL. |
| attributeId | [in] | ViAttr | Pass the ID of an attribute. |
| value | [in] | ViInt32 | Pass the value to which you want to set the attribute.Some of the values might not be valid depending on the current state of the instrument session. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attribute

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__spectrum.html language=enus -->
## TOPIC 00144: Spectrum

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__spectrum.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__spectrum.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniRFSA_ConfigureResolutionBandwidthConfigures the resolution bandwidth of a spectrum acquisition. niRFSA_ConfigureSpectrumFrequencyCenterSpanConfigures the span and center frequency of the spectrum read by NI-RFSA. niRFSA_ConfigureSpectrumFrequencyStartStopConfi

### Spectrum

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niRFSA_ConfigureResolutionBandwidth | Configures the resolution bandwidth of a spectrum acquisition. |
| niRFSA_ConfigureSpectrumFrequencyCenterSpan | Configures the span and center frequency of the spectrum read by NI-RFSA. |
| niRFSA_ConfigureSpectrumFrequencyStartStop | Configures the start and stop frequencies of a spectrum read by NI-RFSA. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__spectrum_1ga0f8b7b4cb4ebbc138e76fb244e137b04.html language=enus -->
## TOPIC 00145: niRFSA_ConfigureSpectrumFrequencyStartStop

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__spectrum_1ga0f8b7b4cb4ebbc138e76fb244e137b04.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__spectrum_1ga0f8b7b4cb4ebbc138e76fb244e137b04.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the start and stop frequencies of a spectrum read by NI-RFSA. SyntaxViStatus _VI_FUNC niRFSA_ConfigureSpectrumFrequencyStartStop(ViSession vi, ViConstString channelList, ViReal64 startFrequency, ViReal64 stopFrequency)RemarksIf you configure the spectrum span (stopFrequencystartFrequency)

### niRFSA_ConfigureSpectrumFrequencyStartStop

Configures the start and stop frequencies of a spectrum read by NI-RFSA.

#### Syntax

ViStatus _VI_FUNC niRFSA_ConfigureSpectrumFrequencyStartStop(ViSession vi, ViConstString channelList, ViReal64 startFrequency, ViReal64 stopFrequency)

#### Remarks

Note

If you configure the spectrum span (**stopFrequency****startFrequency**) to a value larger than the instantaneous bandwidth of the device, NI-RFSA performs multiple acquisitions and combines them into a spectrum of the size you request.

Note

For the PXIe-5663/5663E, NI-RFSA does not support multispan acquisitions from frequency ranges that correspond with different instantaneous bandwidths. For example, you cannot configure a multispan acquisition that acquires one span from 110 MHz to 120 MHz and a second from 120 MHz to 130 MHz because the bandwidths that correspond to each span are different (10 MHz and 20 MHz, respectively).

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| channelList | [in] | ViConstString | Identifies which channels to apply settings. Specify an empty string as the value of this parameter. |
| startFrequency | [in] | ViReal64 | Specifies the lower limit of a span of frequencies. This value is expressed in hertz (Hz). |
| stopFrequency | [in] | ViReal64 | Specifies the upper limit of a span of frequencies. This value is expressed in hertz (Hz). |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Spectrum

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__spectrum_1gaad0f0bcd3df485882b0fe07d3b02407f.html language=enus -->
## TOPIC 00146: niRFSA_ConfigureResolutionBandwidth

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__spectrum_1gaad0f0bcd3df485882b0fe07d3b02407f.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__spectrum_1gaad0f0bcd3df485882b0fe07d3b02407f.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the resolution bandwidth of a spectrum acquisition. SyntaxViStatus _VI_FUNC niRFSA_ConfigureResolutionBandwidth(ViSession vi, ViConstString channelList, ViReal64 resolutionBandwidth)RemarksThe resolution bandwidth controls the width of the frequency bins in the power spectrum computed by

### niRFSA_ConfigureResolutionBandwidth

Configures the resolution bandwidth of a spectrum acquisition.

#### Syntax

ViStatus _VI_FUNC niRFSA_ConfigureResolutionBandwidth(ViSession vi, ViConstString channelList, ViReal64 resolutionBandwidth)

#### Remarks

The resolution bandwidth controls the width of the frequency bins in the power spectrum computed by NI-RFSA. A larger value for resolution bandwidth means the frequency bins are wider, so you get fewer bins, or spectral lines.

By default, the resolution bandwidth value corresponds to the 3 decibels (dB) bandwidth of the window type NI-RFSA uses to compute the spectrum. To directly specify the frequency bin width, set the [NIRFSA_ATTR_RESOLUTION_BANDWIDTH_TYPE](group____root__ni_r_f_s_a__attributes__acquisition__spectrum_1ga084136d8179ce80d878cae2422258033.html) attribute to **NIRFSA_VAL_RBW_BIN_WIDTH**

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Resolution Bandwidth](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/resolution-bandwidth.html)

[Improving Your Measurements](https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/measurement_guidelines.html)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| channelList | [in] | ViConstString | Identifies which channels to apply settings. Specify an empty string as the value of this parameter. |
| resolutionBandwidth | [in] | ViReal64 | Specifies the resolution bandwidth of a spectrum acquisition. The value is expressed in hertz (Hz). Configure the type of resolution bandwidth with the NIRFSA_ATTR_RESOLUTION_BANDWIDTH_TYPE attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Spectrum

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__spectrum_1gabf3f570f0ab8b226445d04cfe69d1fdb.html language=enus -->
## TOPIC 00147: niRFSA_ConfigureSpectrumFrequencyCenterSpan

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__spectrum_1gabf3f570f0ab8b226445d04cfe69d1fdb.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__spectrum_1gabf3f570f0ab8b226445d04cfe69d1fdb.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the span and center frequency of the spectrum read by NI-RFSA. SyntaxViStatus _VI_FUNC niRFSA_ConfigureSpectrumFrequencyCenterSpan(ViSession vi, ViConstString channelList, ViReal64 centerFrequency, ViReal64 span)RemarksA spectrum acquisition consists of data surrounding the center frequen

### niRFSA_ConfigureSpectrumFrequencyCenterSpan

Configures the span and center frequency of the spectrum read by NI-RFSA.

#### Syntax

ViStatus _VI_FUNC niRFSA_ConfigureSpectrumFrequencyCenterSpan(ViSession vi, ViConstString channelList, ViReal64 centerFrequency, ViReal64 span)

#### Remarks

A spectrum acquisition consists of data surrounding the center frequency.

Note

If you configure the spectrum span to a value larger than the instantaneous bandwidth of the device, NI-RFSA performs multiple acquisitions and combines them into a spectrum of the size you requested.

Note

For the PXIe-5663/5663E, NI-RFSA does not support multispan acquisitions from frequency ranges that correspond with different instantaneous bandwidths. For example, you cannot configure a multispan acquisition that acquires one span from 110 MHz to 120 MHz and a second from 120 MHz to 130 MHz because the bandwidths that correspond to each span are different (10 MHz and 20 MHz, respectively).

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| channelList | [in] | ViConstString | Identifies which channels to apply settings. Specify an empty string as the value of this parameter. |
| centerFrequency | [in] | ViReal64 | Specifies the center frequency in a spectrum acquisition. The value is expressed in hertz (Hz). The NI-RFSA device you use determines the valid range. Refer to your device specifications document for more information about frequency range. |
| span | [in] | ViReal64 | Specifies the span of a spectrum acquisition. The value is expressed in hertz (Hz).Note For the PXIe-5663/5663E/5665/5667/5668, NI-RFSA enables dithering by default. The dither noise can appear in your passband and affect your measurements. Refer to the NIRFSA_ATTR_DIGITIZER_DITHER_ENABLED attribute for more information about dithering. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Spectrum

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__trigger.html language=enus -->
## TOPIC 00148: Trigger

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__trigger.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdvance TriggerRef TriggerStart TriggerGroup membersNameDescriptionniRFSA_SendSoftwareEdgeTriggerSends a trigger to the device when you use a software version of a supported trigger and the device is waiting for the trigger to be sent. AttachmentsNone

### Trigger

#### Groups

- Advance Trigger
- Ref Trigger
- Start Trigger

#### Group members

| Name | Description |
| --- | --- |
| niRFSA_SendSoftwareEdgeTrigger | Sends a trigger to the device when you use a software version of a supported trigger and the device is waiting for the trigger to be sent. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__trigger_1ga6e08170f0dffd1662d785df9dbbaeb4f.html language=enus -->
## TOPIC 00149: niRFSA_SendSoftwareEdgeTrigger

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__trigger_1ga6e08170f0dffd1662d785df9dbbaeb4f.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__trigger_1ga6e08170f0dffd1662d785df9dbbaeb4f.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a trigger to the device when you use a software version of a supported trigger and the device is waiting for the trigger to be sent. SyntaxViStatus _VI_FUNC niRFSA_SendSoftwareEdgeTrigger(ViSession vi, ViInt32 trigger, ViConstString triggerIdentifier)RemarksYou can also use this function to ov

### niRFSA_SendSoftwareEdgeTrigger

Sends a trigger to the device when you use a software version of a supported trigger and the device is waiting for the trigger to be sent.

#### Syntax

ViStatus _VI_FUNC niRFSA_SendSoftwareEdgeTrigger(ViSession vi, ViInt32 trigger, ViConstString triggerIdentifier)

#### Remarks

You can also use this function to override a hardware trigger.

This function returns an error in the following situations:

- You configure an invalid trigger.
- You set the **acquisitionType** to **NIRFSA_VAL_SPECTRUM** using the [niRFSA_ConfigureAcquisitionType](group____root__ni_r_f_s_a__functions__configuration_1ga31c461339b5833b6d710be153bdfb7f6.html) function.
- You have not previously called the [niRFSA_Initiate](group____root__ni_r_f_s_a__functions__acquisition__iq__acquisition_1ga9b458066c2b0d05e171c585fccf8d5dd.html) function.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Software Trigger](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/software-edge-trigger.html)

[Triggers](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| trigger | [in] | ViInt32 | Specifies the software signal to send.NameValueDescriptionNIRFSA_VAL_START_TRIGGER1100 (0x44c)NI-RFSA sends a Start software trigger.NIRFSA_VAL_REF_TRIGGER702 (0x2be)NI-RFSA sends a Reference software trigger.NIRFSA_VAL_ADVANCE_TRIGGER1102 (0x44e)NI-RFSA sends an Advance software trigger.NIRFSA_VAL_ARM_REF_TRIGGER1103 (0x44f)NI-RFSA sends an Arm Reference software trigger. This trigger is not valid for the PXIe-5668. |
| Name | Value | Description |  |
| NIRFSA_VAL_START_TRIGGER | 1100 (0x44c) | NI-RFSA sends a Start software trigger. |  |
| NIRFSA_VAL_REF_TRIGGER | 702 (0x2be) | NI-RFSA sends a Reference software trigger. |  |
| NIRFSA_VAL_ADVANCE_TRIGGER | 1102 (0x44e) | NI-RFSA sends an Advance software trigger. |  |
| NIRFSA_VAL_ARM_REF_TRIGGER | 1103 (0x44f) | NI-RFSA sends an Arm Reference software trigger. This trigger is not valid for the PXIe-5668. |  |
| triggerIdentifier | [in] | ViConstString | Specifies a particular instance of a trigger. NI-RFSA does not currently support this parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__trigger__advance__trigger.html language=enus -->
## TOPIC 00150: Advance Trigger

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__trigger__advance__trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__trigger__advance__trigger.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniRFSA_ConfigureDigitalEdgeAdvanceTriggerConfigures the device to wait for a digital edge Advance Trigger. niRFSA_ConfigureSoftwareEdgeAdvanceTriggerConfigures the device to wait for a software Advance Trigger. niRFSA_DisableAdvanceTriggerConfigures the device t

### Advance Trigger

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niRFSA_ConfigureDigitalEdgeAdvanceTrigger | Configures the device to wait for a digital edge Advance Trigger. |
| niRFSA_ConfigureSoftwareEdgeAdvanceTrigger | Configures the device to wait for a software Advance Trigger. |
| niRFSA_DisableAdvanceTrigger | Configures the device to not use an Advance Trigger. |

#### Attachments

None

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__trigger__advance__trigger_1ga7859af11e1ae0be89c1f67265e7e38b0.html language=enus -->
## TOPIC 00151: niRFSA_DisableAdvanceTrigger

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__trigger__advance__trigger_1ga7859af11e1ae0be89c1f67265e7e38b0.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__trigger__advance__trigger_1ga7859af11e1ae0be89c1f67265e7e38b0.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to not use an Advance Trigger. SyntaxViStatus _VI_FUNC niRFSA_DisableAdvanceTrigger(ViSession vi)RemarksThis function is necessary only if you configured an Advance Trigger in the past and now want to disable it.Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/

### niRFSA_DisableAdvanceTrigger

Configures the device to not use an Advance Trigger.

#### Syntax

ViStatus _VI_FUNC niRFSA_DisableAdvanceTrigger(ViSession vi)

#### Remarks

This function is necessary only if you configured an Advance Trigger in the past and now want to disable it.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Triggers](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advance Trigger

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__trigger__advance__trigger_1ga789d8e59cdb800915b1f198094947990.html language=enus -->
## TOPIC 00152: niRFSA_ConfigureDigitalEdgeAdvanceTrigger

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__trigger__advance__trigger_1ga789d8e59cdb800915b1f198094947990.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__trigger__advance__trigger_1ga789d8e59cdb800915b1f198094947990.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a digital edge Advance Trigger. SyntaxViStatus _VI_FUNC niRFSA_ConfigureDigitalEdgeAdvanceTrigger(ViSession vi, ViConstString source, ViInt32 edge)RemarksThe Advance Trigger indicates where a new record begins.This function is not supported if you set the acquisitio

### niRFSA_ConfigureDigitalEdgeAdvanceTrigger

Configures the device to wait for a digital edge Advance Trigger.

#### Syntax

ViStatus _VI_FUNC niRFSA_ConfigureDigitalEdgeAdvanceTrigger(ViSession vi, ViConstString source, ViInt32 edge)

#### Remarks

The Advance Trigger indicates where a new record begins.

Note

This function is not supported if you set the **acquisitionType** parameter to **NIRFSA_VAL_SPECTRUM** using the [niRFSA_ConfigureAcquisitionType](group____root__ni_r_f_s_a__functions__configuration_1ga31c461339b5833b6d710be153bdfb7f6.html) function or if you set the [NIRFSA_ATTR_ACQUISITION_TYPE](group____root__ni_r_f_s_a__attributes_1ga9a481e05f8dbacfbfc47cd622d990181.html) attribute to **NIRFSA_VAL_SPECTRUM**.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Triggers](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| source | [in] | ViConstString | Specifies the source of the digital edge for the Advance Trigger.ValueDescriptionNIRFSA_VAL_PFI0_STR ("PFI0")The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.NIRFSA_VAL_PFI1_STR ("PFI1")The trigger is received on PFI 1.NIRFSA_VAL_PXI_TRIG0_STR ("PXI_Trig0")The trigger is received on PXI trigger line 0.NIRFSA_VAL_PXI_TRIG1_STR ("PXI_Trig1")The trigger is received on PXI trigger line 1.NIRFSA_VAL_PXI_TRIG2_STR ("PXI_Trig2")The trigger is received on PXI trigger line 2.NIRFSA_VAL_PXI_TRIG3_STR ("PXI_Trig3")The trigger is received on PXI trigger line 3.NIRFSA_VAL_PXI_TRIG4_STR ("PXI_Trig4")The trigger is received on PXI trigger line 4.NIRFSA_VAL_PXI_TRIG5_STR ("PXI_Trig5")The trigger is received on PXI trigger line 5.NIRFSA_VAL_PXI_TRIG6_STR ("PXI_Trig6")The trigger is received on PXI trigger line 6.NIRFSA_VAL_PXI_TRIG7_STR ("PXI_Trig7")The trigger is received on PXI trigger line 7.NIRFSA_VAL_PXI_STAR_STR ("PXI_STAR")The trigger is received on the PXI star trigger line. This value is not supported for PXIe-5644/5645/5646 devices.NIRFSA_VAL_PXIE_DSTARB_STR ("PXIE_DSTARB")The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.NIRFSA_VAL_TIMER_EVENT_STR ("TimerEvent")The trigger is received from Timer Event on the digitizer. This value is valid on only the PXIe-5820/5840/5841/5842/5860 and for digital edge Advance Triggers on the PXIe-5644/5645/5646 and PXIe-5663E/5665.NIRFSA_VAL_DIO_PFI0_STR ("PFI0")The trigger is received on PFI 0 of the DIO Terminal.NIRFSA_VAL_DIO_PFI1_STR("PFI1")The trigger is received on PFI 1 of the DIO Terminal.NIRFSA_VAL_DIO_PFI2_STR ("PFI2")The trigger is received on PFI 2 of the DIO Terminal.NIRFSA_VAL_DIO_PFI3_STR ("PFI3")The trigger is received on PFI 3 of the DIO Terminal.NIRFSA_VAL_DIO_PFI4_STR ("PFI4")The trigger is received on PFI 4 of the DIO Terminal.NIRFSA_VAL_DIO_PFI5_STR ("PFI5")The trigger is received on PFI 5 of the DIO Terminal.NIRFSA_VAL_DIO_PFI6_STR ("PFI6")The trigger is received on PFI 6 of the DIO Terminal.NIRFSA_VAL_DIO_PFI7_STR ("PFI7")The trigger is received on PFI 7 of the DIO Terminal. |
| Value | Description |  |  |
| NIRFSA_VAL_PFI0_STR ("PFI0") | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0. |  |  |
| NIRFSA_VAL_PFI1_STR ("PFI1") | The trigger is received on PFI 1. |  |  |
| NIRFSA_VAL_PXI_TRIG0_STR ("PXI_Trig0") | The trigger is received on PXI trigger line 0. |  |  |
| NIRFSA_VAL_PXI_TRIG1_STR ("PXI_Trig1") | The trigger is received on PXI trigger line 1. |  |  |
| NIRFSA_VAL_PXI_TRIG2_STR ("PXI_Trig2") | The trigger is received on PXI trigger line 2. |  |  |
| NIRFSA_VAL_PXI_TRIG3_STR ("PXI_Trig3") | The trigger is received on PXI trigger line 3. |  |  |
| NIRFSA_VAL_PXI_TRIG4_STR ("PXI_Trig4") | The trigger is received on PXI trigger line 4. |  |  |
| NIRFSA_VAL_PXI_TRIG5_STR ("PXI_Trig5") | The trigger is received on PXI trigger line 5. |  |  |
| NIRFSA_VAL_PXI_TRIG6_STR ("PXI_Trig6") | The trigger is received on PXI trigger line 6. |  |  |
| NIRFSA_VAL_PXI_TRIG7_STR ("PXI_Trig7") | The trigger is received on PXI trigger line 7. |  |  |
| NIRFSA_VAL_PXI_STAR_STR ("PXI_STAR") | The trigger is received on the PXI star trigger line. This value is not supported for PXIe-5644/5645/5646 devices. |  |  |
| NIRFSA_VAL_PXIE_DSTARB_STR ("PXIE_DSTARB") | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |  |  |
| NIRFSA_VAL_TIMER_EVENT_STR ("TimerEvent") | The trigger is received from Timer Event on the digitizer. This value is valid on only the PXIe-5820/5840/5841/5842/5860 and for digital edge Advance Triggers on the PXIe-5644/5645/5646 and PXIe-5663E/5665. |  |  |
| NIRFSA_VAL_DIO_PFI0_STR ("PFI0") | The trigger is received on PFI 0 of the DIO Terminal. |  |  |
| NIRFSA_VAL_DIO_PFI1_STR("PFI1") | The trigger is received on PFI 1 of the DIO Terminal. |  |  |
| NIRFSA_VAL_DIO_PFI2_STR ("PFI2") | The trigger is received on PFI 2 of the DIO Terminal. |  |  |
| NIRFSA_VAL_DIO_PFI3_STR ("PFI3") | The trigger is received on PFI 3 of the DIO Terminal. |  |  |
| NIRFSA_VAL_DIO_PFI4_STR ("PFI4") | The trigger is received on PFI 4 of the DIO Terminal. |  |  |
| NIRFSA_VAL_DIO_PFI5_STR ("PFI5") | The trigger is received on PFI 5 of the DIO Terminal. |  |  |
| NIRFSA_VAL_DIO_PFI6_STR ("PFI6") | The trigger is received on PFI 6 of the DIO Terminal. |  |  |
| NIRFSA_VAL_DIO_PFI7_STR ("PFI7") | The trigger is received on PFI 7 of the DIO Terminal. |  |  |
| edge | [in] | ViInt32 | Specifies the trigger edge to detect. The default value is NIRFSA_VAL_RISING_EDGE.ValueDescriptionNIRFSA_VAL_RISING_EDGE (900)NI-RFSA detects a rising edge.NIRFSA_VAL_FALLING_EDGE (901)NI-RFSA detects a falling edge. |
| Value | Description |  |  |
| NIRFSA_VAL_RISING_EDGE (900) | NI-RFSA detects a rising edge. |  |  |
| NIRFSA_VAL_FALLING_EDGE (901) | NI-RFSA detects a falling edge. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advance Trigger

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__trigger__advance__trigger_1gae8d13484acf29601057939d701b009ec.html language=enus -->
## TOPIC 00153: niRFSA_ConfigureSoftwareEdgeAdvanceTrigger

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__trigger__advance__trigger_1gae8d13484acf29601057939d701b009ec.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__trigger__advance__trigger_1gae8d13484acf29601057939d701b009ec.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a software Advance Trigger. SyntaxViStatus _VI_FUNC niRFSA_ConfigureSoftwareEdgeAdvanceTrigger(ViSession vi)RemarksThe Advance Trigger indicates where a new record begins. The device waits until you call the niRFSA_SendSoftwareEdgeTrigger function to assert the trig

### niRFSA_ConfigureSoftwareEdgeAdvanceTrigger

Configures the device to wait for a software Advance Trigger.

#### Syntax

ViStatus _VI_FUNC niRFSA_ConfigureSoftwareEdgeAdvanceTrigger(ViSession vi)

#### Remarks

The Advance Trigger indicates where a new record begins. The device waits until you call the [niRFSA_SendSoftwareEdgeTrigger](group____root__ni_r_f_s_a__functions__configuration__trigger_1ga6e08170f0dffd1662d785df9dbbaeb4f.html) function to assert the trigger.

Note

This function is not supported if you set the **acquisitionType** parameter to **NIRFSA_VAL_SPECTRUM** using the [niRFSA_ConfigureAcquisitionType](group____root__ni_r_f_s_a__functions__configuration_1ga31c461339b5833b6d710be153bdfb7f6.html) function or if you set the [NIRFSA_ATTR_ACQUISITION_TYPE](group____root__ni_r_f_s_a__attributes_1ga9a481e05f8dbacfbfc47cd622d990181.html) attribute to **NIRFSA_VAL_SPECTRUM**.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Triggers](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advance Trigger

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__trigger__ref__trigger_1ga029a84cdcb097baa89d1040d1cca0c0b.html language=enus -->
## TOPIC 00154: niRFSA_ConfigureSoftwareEdgeRefTrigger

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__trigger__ref__trigger_1ga029a84cdcb097baa89d1040d1cca0c0b.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__trigger__ref__trigger_1ga029a84cdcb097baa89d1040d1cca0c0b.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a software Reference Trigger to mark a reference point within the record. SyntaxViStatus _VI_FUNC niRFSA_ConfigureSoftwareEdgeRefTrigger(ViSession vi, ViInt64 pretriggerSamples)RemarksThe device waits until you call the niRFSA_SendSoftwareEdgeTrigger function to ass

### niRFSA_ConfigureSoftwareEdgeRefTrigger

Configures the device to wait for a software Reference Trigger to mark a reference point within the record.

#### Syntax

ViStatus _VI_FUNC niRFSA_ConfigureSoftwareEdgeRefTrigger(ViSession vi, ViInt64 pretriggerSamples)

#### Remarks

The device waits until you call the [niRFSA_SendSoftwareEdgeTrigger](group____root__ni_r_f_s_a__functions__configuration__trigger_1ga6e08170f0dffd1662d785df9dbbaeb4f.html) function to assert the trigger.

You can use this trigger with the [NI-TClk API](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/user-manual-welcome.html).

Note

The PXIe-5644/5645/5646 does not support the NI-TClk API.

Note

This function is not supported if you set the **acquisitionType** parameter to **NIRFSA_VAL_SPECTRUM** using the [niRFSA_ConfigureAcquisitionType](group____root__ni_r_f_s_a__functions__configuration_1ga31c461339b5833b6d710be153bdfb7f6.html) function or if you set the [NIRFSA_ATTR_ACQUISITION_TYPE](group____root__ni_r_f_s_a__attributes_1ga9a481e05f8dbacfbfc47cd622d990181.html) attribute to **NIRFSA_VAL_SPECTRUM**.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Triggers](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| pretriggerSamples | [in] | ViInt64 | Specifies the number of samples to store for each record that was acquired in the time period immediately before the trigger occurred. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Ref Trigger

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__configuration__trigger__start__trigger_1ga8457b8ed5f88516fcdb37d14ee3a3614.html language=enus -->
## TOPIC 00155: niRFSA_ConfigureDigitalEdgeStartTrigger

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__configuration__trigger__start__trigger_1ga8457b8ed5f88516fcdb37d14ee3a3614.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__configuration__trigger__start__trigger_1ga8457b8ed5f88516fcdb37d14ee3a3614.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a digital edge Start Trigger at the beginning of the acquisition. SyntaxViStatus _VI_FUNC niRFSA_ConfigureDigitalEdgeStartTrigger(ViSession vi, ViConstString source, ViInt32 edge)RemarksYou can use this trigger with the NI-TClk API.The PXIe-5644/5645/5646 does not s

### niRFSA_ConfigureDigitalEdgeStartTrigger

Configures the device to wait for a digital edge Start Trigger at the beginning of the acquisition.

#### Syntax

ViStatus _VI_FUNC niRFSA_ConfigureDigitalEdgeStartTrigger(ViSession vi, ViConstString source, ViInt32 edge)

#### Remarks

You can use this trigger with the [NI-TClk API](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/user-manual-welcome.html).

Note

The PXIe-5644/5645/5646 does not support the NI-TClk API.

Note

This function is not supported if you set the **acquisitionType** parameter to **NIRFSA_VAL_SPECTRUM** using the [niRFSA_ConfigureAcquisitionType](group____root__ni_r_f_s_a__functions__configuration_1ga31c461339b5833b6d710be153bdfb7f6.html) function or if you set the [NIRFSA_ATTR_ACQUISITION_TYPE](group____root__ni_r_f_s_a__attributes_1ga9a481e05f8dbacfbfc47cd622d990181.html) attribute to **NIRFSA_VAL_SPECTRUM**.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Triggers](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| source | [in] | ViConstString | Specifies the source of the digital edge for the Start Trigger.ValueDescriptionNIRFSA_VAL_PFI0_STR ("PFI0")The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.NIRFSA_VAL_PFI1_STR ("PFI1")The trigger is received on PFI 1.NIRFSA_VAL_PXI_TRIG0_STR ("PXI_Trig0")The trigger is received on PXI trigger line 0.NIRFSA_VAL_PXI_TRIG1_STR ("PXI_Trig1")The trigger is received on PXI trigger line 1.NIRFSA_VAL_PXI_TRIG2_STR ("PXI_Trig2")The trigger is received on PXI trigger line 2.NIRFSA_VAL_PXI_TRIG3_STR ("PXI_Trig3")The trigger is received on PXI trigger line 3.NIRFSA_VAL_PXI_TRIG4_STR ("PXI_Trig4")The trigger is received on PXI trigger line 4.NIRFSA_VAL_PXI_TRIG5_STR ("PXI_Trig5")The trigger is received on PXI trigger line 5.NIRFSA_VAL_PXI_TRIG6_STR ("PXI_Trig6")The trigger is received on PXI trigger line 6.NIRFSA_VAL_PXI_TRIG7_STR ("PXI_Trig7")The trigger is received on PXI trigger line 7.NIRFSA_VAL_PXI_STAR_STR ("PXI_STAR")The trigger is received on the PXI star trigger line. This value is not supported for PXIe-5644/5645/5646 devices.NIRFSA_VAL_PXIE_DSTARB_STR ("PXIE_DSTARB")The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.NIRFSA_VAL_TIMER_EVENT_STR ("TimerEvent")The trigger is received from Timer Event on the digitizer. This value is valid on only the PXIe-5820/5840/5841/5842/5860 and for digital edge Advance Triggers on the PXIe-5644/5645/5646 and PXIe-5663E/5665.NIRFSA_VAL_DIO_PFI0_STR ("PFI1")The trigger is received on PFI 0 of the DIO Terminal.NIRFSA_VAL_DIO_PFI1_STR("PFI2")The trigger is received on PFI 1 of the DIO Terminal.NIRFSA_VAL_DIO_PFI2_STR ("PFI3")The trigger is received on PFI 2 of the DIO Terminal.NIRFSA_VAL_DIO_PFI3_STR ("PFI4")The trigger is received on PFI 3 of the DIO Terminal.NIRFSA_VAL_DIO_PFI4_STR ("PFI5")The trigger is received on PFI 4 of the DIO Terminal.NIRFSA_VAL_DIO_PFI5_STR ("PFI6")The trigger is received on PFI 5 of the DIO Terminal.NIRFSA_VAL_DIO_PFI6_STR ("PFI7")The trigger is received on PFI 6 of the DIO Terminal.NIRFSA_VAL_DIO_PFI7_STR ("PFI8")The trigger is received on PFI 7 of the DIO Terminal. |
| Value | Description |  |  |
| NIRFSA_VAL_PFI0_STR ("PFI0") | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0. |  |  |
| NIRFSA_VAL_PFI1_STR ("PFI1") | The trigger is received on PFI 1. |  |  |
| NIRFSA_VAL_PXI_TRIG0_STR ("PXI_Trig0") | The trigger is received on PXI trigger line 0. |  |  |
| NIRFSA_VAL_PXI_TRIG1_STR ("PXI_Trig1") | The trigger is received on PXI trigger line 1. |  |  |
| NIRFSA_VAL_PXI_TRIG2_STR ("PXI_Trig2") | The trigger is received on PXI trigger line 2. |  |  |
| NIRFSA_VAL_PXI_TRIG3_STR ("PXI_Trig3") | The trigger is received on PXI trigger line 3. |  |  |
| NIRFSA_VAL_PXI_TRIG4_STR ("PXI_Trig4") | The trigger is received on PXI trigger line 4. |  |  |
| NIRFSA_VAL_PXI_TRIG5_STR ("PXI_Trig5") | The trigger is received on PXI trigger line 5. |  |  |
| NIRFSA_VAL_PXI_TRIG6_STR ("PXI_Trig6") | The trigger is received on PXI trigger line 6. |  |  |
| NIRFSA_VAL_PXI_TRIG7_STR ("PXI_Trig7") | The trigger is received on PXI trigger line 7. |  |  |
| NIRFSA_VAL_PXI_STAR_STR ("PXI_STAR") | The trigger is received on the PXI star trigger line. This value is not supported for PXIe-5644/5645/5646 devices. |  |  |
| NIRFSA_VAL_PXIE_DSTARB_STR ("PXIE_DSTARB") | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |  |  |
| NIRFSA_VAL_TIMER_EVENT_STR ("TimerEvent") | The trigger is received from Timer Event on the digitizer. This value is valid on only the PXIe-5820/5840/5841/5842/5860 and for digital edge Advance Triggers on the PXIe-5644/5645/5646 and PXIe-5663E/5665. |  |  |
| NIRFSA_VAL_DIO_PFI0_STR ("PFI1") | The trigger is received on PFI 0 of the DIO Terminal. |  |  |
| NIRFSA_VAL_DIO_PFI1_STR("PFI2") | The trigger is received on PFI 1 of the DIO Terminal. |  |  |
| NIRFSA_VAL_DIO_PFI2_STR ("PFI3") | The trigger is received on PFI 2 of the DIO Terminal. |  |  |
| NIRFSA_VAL_DIO_PFI3_STR ("PFI4") | The trigger is received on PFI 3 of the DIO Terminal. |  |  |
| NIRFSA_VAL_DIO_PFI4_STR ("PFI5") | The trigger is received on PFI 4 of the DIO Terminal. |  |  |
| NIRFSA_VAL_DIO_PFI5_STR ("PFI6") | The trigger is received on PFI 5 of the DIO Terminal. |  |  |
| NIRFSA_VAL_DIO_PFI6_STR ("PFI7") | The trigger is received on PFI 6 of the DIO Terminal. |  |  |
| NIRFSA_VAL_DIO_PFI7_STR ("PFI8") | The trigger is received on PFI 7 of the DIO Terminal. |  |  |
| edge | [in] | ViInt32 | Specifies the trigger edge to detect. The default value is NIRFSA_VAL_RISING_EDGE.ValueDescriptionNIRFSA_VAL_RISING_EDGE (900)NI-RFSA detects a rising edge.NIRFSA_VAL_FALLING_EDGE (901)NI-RFSA detects a falling edge. |
| Value | Description |  |  |
| NIRFSA_VAL_RISING_EDGE (900) | NI-RFSA detects a rising edge. |  |  |
| NIRFSA_VAL_FALLING_EDGE (901) | NI-RFSA detects a falling edge. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Start Trigger

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__utility_1ga35bf63eb29316389a01e36999e1222c0.html language=enus -->
## TOPIC 00156: niRFSA_GetSpectralInfoForSmt

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__utility_1ga35bf63eb29316389a01e36999e1222c0.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__utility_1ga35bf63eb29316389a01e36999e1222c0.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns information about the power spectrum NI-RFSA computes. SyntaxViStatus _VI_FUNC niRFSA_GetSpectralInfoForSmt(ViSession vi, SmtSpectrumInfo *spectrumInfo)RemarksThe NI Spectral Measurements Toolkit (SMT) requires this information.Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663

### niRFSA_GetSpectralInfoForSmt

Returns information about the power spectrum NI-RFSA computes.

#### Syntax

ViStatus _VI_FUNC niRFSA_GetSpectralInfoForSmt(ViSession vi, SmtSpectrumInfo *spectrumInfo)

#### Remarks

Note

The NI Spectral Measurements Toolkit (SMT) requires this information.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| spectrumInfo | [out] | SmtSpectrumInfo * | Returns returns properties of the computed spectrum such as spectrum type, spectrum scale (linear or logarithmic), the window type the function used to compute the spectrum, window size, and FFT size. Pass this parameter to subsequent functions that contain the spectrumInfo parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__utility_1ga3e8a1067ec16b791d1a65f589a1ac330.html language=enus -->
## TOPIC 00157: niRFSA_GetScalingCoefficients

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__utility_1ga3e8a1067ec16b791d1a65f589a1ac330.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__utility_1ga3e8a1067ec16b791d1a65f589a1ac330.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns coefficients you can use to convert unscaled data to scaled I/Q data. SyntaxViStatus _VI_FUNC niRFSA_GetScalingCoefficients(ViSession vi, ViConstString channelList, ViInt32 arraySize, niRFSA_coefficientInfo coefficientInfo[], ViInt32 *numberOfCoefficientSets)RemarksAcquired data may be unsca

### niRFSA_GetScalingCoefficients

Returns coefficients you can use to convert unscaled data to scaled I/Q data.

#### Syntax

ViStatus _VI_FUNC niRFSA_GetScalingCoefficients(ViSession vi, ViConstString channelList, ViInt32 arraySize, niRFSA_coefficientInfo coefficientInfo[], ViInt32 *numberOfCoefficientSets)

#### Remarks

Acquired data may be unscaled when sent by a peer-to-peer stream or fetched as unscaled data. Use this function to obtain [niRFSA_GetScalingCoefficients](group____root__ni_r_f_s_a__functions__utility_1ga3e8a1067ec16b791d1a65f589a1ac330.html) structures in the **coefficientInfo** array that provide gain and offset values you can use to scale this data into the actual I/Q values. The **coefficientInfo** array returns one element for each channel specified in the **channelList** parameter. The element order matches the order specified by the **channelList** parameter. To get the actual I/Q values, scale the unscaled data from an acquisition by multiplying it by the gain value of the appropriate **coefficientInfo** element then adding the offset from the same element.

Note

The coefficients are calculated by NI-RFSA for the current configuration of the device, so they are only valid for acquisitions obtained with the same device configuration.

To get the required size of the array, call this function with **arraySize** set to 0 and NULL for the **coefficientInfo** array. This function returns the required size in the **numberOfCoefficientSets** parameter.

**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| channelList | [in] | ViConstString | Identifies which channels to apply settings. Specify an empty string as the value of this parameter. |
| arraySize | [in] | ViInt32 | Specifies the size of the array you specify for the coefficientInfo parameter. |
| coefficientInfo | [out] | niRFSA_coefficientInfo[] | Specifies the array for storing the coefficient info.offset is the number that should be added to the data from a peer-to-peer stream after the gain has been applied if you want to scale unscaled data.gain returns the multiplier that you should use to scale data obtained from a peer-to-peer stream. |
| numberOfCoefficientSets | [out] | ViInt32 * | Returns the number of valid coefficient sets. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__utility_1ga454ac405360dcc30df4867139f7f5fd4.html language=enus -->
## TOPIC 00158: niRFSA_EnableSessionAccess

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__utility_1ga454ac405360dcc30df4867139f7f5fd4.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__utility_1ga454ac405360dcc30df4867139f7f5fd4.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables or disables SFP session access for the specified instrument. SyntaxViStatus _VI_FUNC niRFSA_EnableSessionAccess(ViSession vi, ViBoolean enable)RemarksSFP session access allows the NI-RFSA Soft Front Panel (SFP) to access a device with an existing open session and can help you debug your code

### niRFSA_EnableSessionAccess

Enables or disables SFP session access for the specified instrument.

#### Syntax

ViStatus _VI_FUNC niRFSA_EnableSessionAccess(ViSession vi, ViBoolean enable)

#### Remarks

SFP session access allows the NI-RFSA Soft Front Panel (SFP) to access a device with an existing open session and can help you debug your code. To enable session access, pass VI_TRUE to the **enabled** parameter. To disable session access, pass VI_FALSE to the **enabled** parameter.

Refer to [Configuring SFP Session Access using LabWindows/CVI or C](https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/configuring_session_access_labwindows.html) for more information about SFP session access.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5830/5831/5832/5840/5841/5842/5860

Note

NI-RFSA does not support NI-TClk when driver session debugging is enabled.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| enable | [in] | ViBoolean | Enables or disables SFP session access for the specified device.ValueDescriptionVI_TRUEEnables session access.VI_FALSEDisables session access. |
| Value | Description |  |  |
| VI_TRUE | Enables session access. |  |  |
| VI_FALSE | Disables session access. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__utility_1ga52dfa0aa02764e1803a9b7558c8b1dc7.html language=enus -->
## TOPIC 00159: niRFSA_GetRelayOperationsCount

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__utility_1ga52dfa0aa02764e1803a9b7558c8b1dc7.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__utility_1ga52dfa0aa02764e1803a9b7558c8b1dc7.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array consisting of all the relay counts for your device. SyntaxViStatus _VI_FUNC niRFSA_GetRelayOperationsCount(ViSession vi, ViConstString channelList, ViInt32 operationsCount[], ViInt32 *bufferSize)RemarksWhen you call this function and pass a VI_NULL pointer to the operationsCount par

### niRFSA_GetRelayOperationsCount

Returns an array consisting of all the relay counts for your device.

#### Syntax

ViStatus _VI_FUNC niRFSA_GetRelayOperationsCount(ViSession vi, ViConstString channelList, ViInt32 operationsCount[], ViInt32 *bufferSize)

#### Remarks

When you call this function and pass a VI_NULL pointer to the **operationsCount** parameter, **bufferSize** is populated with the number of relays on the device. When you call this function and specify a value for **bufferSize** that is greater than or equal to the number of relays, the **operationsCount** parameter returns the appropriate value.

**Supported Devices**: PXIe-5603/5605/5606, PXIe-5698

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| channelList | [in] | ViConstString | Identifies which channels to apply settings. Specify an empty string as the value of this parameter. |
| operationsCount | [out] | ViInt32[] | Specifies the operations count array, when used as an input. You can select VI_NULL or a pointer to a ViInt32 array. VI_NULL is the default. When bufferSize is greater than or equal to the number of relays, operationsCount returns the number of relay operations. |
| bufferSize | [out] | ViInt32 * | Functions as an input or an output. bufferSize receives or returns the number of relays that are on the device. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__utility_1ga58cf7ed80a735450b51eca20b6769c85.html language=enus -->
## TOPIC 00160: niRFSA_GetRelayName

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__utility_1ga58cf7ed80a735450b51eca20b6769c85.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__utility_1ga58cf7ed80a735450b51eca20b6769c85.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the name of a relay for your device. SyntaxViStatus _VI_FUNC niRFSA_GetRelayName(ViSession vi, ViConstString channelList, ViInt32 index, ViChar name[], ViInt32 *bufferSize)RemarksWhen you call this function and pass a VI_NULL pointer to the name parameter, bufferSize is populated with the si

### niRFSA_GetRelayName

Returns the name of a relay for your device.

#### Syntax

ViStatus _VI_FUNC niRFSA_GetRelayName(ViSession vi, ViConstString channelList, ViInt32 index, ViChar name[], ViInt32 *bufferSize)

#### Remarks

When you call this function and pass a VI_NULL pointer to the **name** parameter, **bufferSize** is populated with the size of name including the terminating NULL byte. When you call this function and specify a value for **bufferSize** that is greater than or equal to the name of relay, the **name** parameter returns the appropriate value.

**Supported Devices**: PXIe-5603/5605/5606.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| channelList | [in] | ViConstString | Identifies which channels to apply settings. Specify an empty string as the value of this parameter. |
| index | [in] | ViInt32 | Specifies the index of the relay. |
| name | [out] | ViChar[] | Specifies the relay name, when used as an input. You can select VI_NULL or a pointer to a ViInt32 array. VI_NULL is the default. When bufferSize is greater than or equal to the number of relays, name returns the relay name. |
| bufferSize | [out] | ViInt32 * | When a VI_NULL pointer is passed in for the name, bufferSize is populated with the size of the name. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__utility_1ga7d5fa0aca1d9586530e731e58c9aa497.html language=enus -->
## TOPIC 00161: niRFSA_ResetWithOptions

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__utility_1ga7d5fa0aca1d9586530e731e58c9aa497.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__utility_1ga7d5fa0aca1d9586530e731e58c9aa497.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets all properties to default values and specifies steps to omit during the reset process, such as signal routes. SyntaxViStatus _VI_FUNC niRFSA_ResetWithOptions(ViSession vi, ViUInt64 stepsToOmit)RemarksFor the PXI-5600, this function does not reset the PXI Clock signal that is driven by devices

### niRFSA_ResetWithOptions

Resets all properties to default values and specifies steps to omit during the reset process, such as signal routes.

#### Syntax

ViStatus _VI_FUNC niRFSA_ResetWithOptions(ViSession vi, ViUInt64 stepsToOmit)

#### Remarks

For the PXI-5600, this function does not reset the PXI Clock signal that is driven by devices installed in the Star Trigger Controller Slot, also known as the System Timing Slot.

By default, this function resets all properties to their default values, deletes all de-embedding tables, aborts generation, clears all routes, and resets session properties to initial values. You can specify steps to omit using the steps to omit parameter. For example, if you specify **NIRFSA_VAL_RESET_WITH_OPTIONS_ROUTES** for the **stepsToOmit** parameter, this function does not release signal routes during the reset process.

When routes of signals between two devices are released, they are released regardless of which device created the route.

To avoid resetting routes on PXIe-5820/5830/5831/5832/5840/5841/5842/5860 that are in use by NI-RFSG sessions, NI recommends using this function instead of [niRFSA_Reset](group____root__ni_r_f_s_a__functions__utility_1gacc51bf29e024ce7620a7003cb1c9a52f.html), with **stepsToOmit** set to **NIRFSA_VAL_RESET_WITH_OPTIONS_ROUTES**.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Triggers](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html)

[Events](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |
| stepsToOmit | [in] | ViUInt64 | Specifies a list of steps to skip during the reset process. The default value is NIRFSA_VAL_RESET_WITH_OPTIONS_NONE, which specifies that no step is omitted during reset.NameValueDescriptionNIRFSA_VAL_RESET_WITH_OPTIONS_DEEMBEDDING_TABLES2 (0x2)Omits deleting de-embedding tables. This step is valid only for the PXIe-5830/5831/5832/5840.NIRFSA_VAL_RESET_WITH_OPTIONS_NONE0 (0x0)No step is omitted during reset.NIRFSA_VAL_RESET_WITH_OPTIONS_ROUTES1 (0x1)Omits the routing reset step. Routing is preserved after a reset. However, routing related properties are reset to default, and routing is released if the default properties are committed after a reset.Note:NIRFSA_VAL_RESET_WITH_OPTIONS_ROUTES is not supported in external calibration or alignment sessions.Note:NIRFSA_VAL_RESET_WITH_OPTIONS_ROUTES is not supported for the PXI-5600/5661. |
| Name | Value | Description |  |
| NIRFSA_VAL_RESET_WITH_OPTIONS_DEEMBEDDING_TABLES | 2 (0x2) | Omits deleting de-embedding tables. This step is valid only for the PXIe-5830/5831/5832/5840. |  |
| NIRFSA_VAL_RESET_WITH_OPTIONS_NONE | 0 (0x0) | No step is omitted during reset. |  |
| NIRFSA_VAL_RESET_WITH_OPTIONS_ROUTES | 1 (0x1) | Omits the routing reset step. Routing is preserved after a reset. However, routing related properties are reset to default, and routing is released if the default properties are committed after a reset. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__utility_1ga93c92e8977c5e45f0867e6a5c4f3a964.html language=enus -->
## TOPIC 00162: niRFSA_Commit

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__utility_1ga93c92e8977c5e45f0867e6a5c4f3a964.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__utility_1ga93c92e8977c5e45f0867e6a5c4f3a964.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits settings to hardware. SyntaxViStatus _VI_FUNC niRFSA_Commit(ViSession vi)RemarksCalling this function is optional. Settings are automatically committed to hardware when you call the niRFSA_Initiate function, the niRFSA_ReadIqSingleRecordComplexF64 function, or the niRFSA_ReadPowerSpectrumF64

### niRFSA_Commit

Commits settings to hardware.

#### Syntax

ViStatus _VI_FUNC niRFSA_Commit(ViSession vi)

#### Remarks

Calling this function is optional. Settings are automatically committed to hardware when you call the [niRFSA_Initiate](group____root__ni_r_f_s_a__functions__acquisition__iq__acquisition_1ga9b458066c2b0d05e171c585fccf8d5dd.html) function, the [niRFSA_ReadIqSingleRecordComplexF64](group____root__ni_r_f_s_a__functions__acquisition__iq__acquisition__single__record__acquisition_1gab75a8b7514cc0e168bb75fd170013b8d.html) function, or the [niRFSA_ReadPowerSpectrumF64](group____root__ni_r_f_s_a__functions__acquisition__spectrum__acquisition_1gaa03dfd475bf1ec4c6dff790ad5f4837b.html) function.

Note

This function does not wait for settling time, unlike the [niRFSA_Initiate](group____root__ni_r_f_s_a__functions__acquisition__iq__acquisition_1ga9b458066c2b0d05e171c585fccf8d5dd.html) function.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[NI RF Vector Signal Analyzer State Diagram](https://www.ni.com/docs/en-US/bundle/pxie-5667-feature/page/hardware-state-diagram.html)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__utility_1gaa14f3b024923be8707b9566266394f78.html language=enus -->
## TOPIC 00163: niRFSA_PerformThermalCorrection

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__utility_1gaa14f3b024923be8707b9566266394f78.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__utility_1gaa14f3b024923be8707b9566266394f78.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Corrects for temperature variations while acquiring the same signal for an extended period of time in a continuous acquisition. SyntaxViStatus _VI_FUNC niRFSA_PerformThermalCorrection(ViSession vi)RemarksNI-RFSA internally acquires the temperature every time you initiate an acquisition. If you are p

### niRFSA_PerformThermalCorrection

Corrects for temperature variations while acquiring the same signal for an extended period of time in a continuous acquisition.

#### Syntax

ViStatus _VI_FUNC niRFSA_PerformThermalCorrection(ViSession vi)

#### Remarks

NI-RFSA internally acquires the temperature every time you initiate an acquisition. If you are performing a continuous acquisition, National Instruments recommends calling this function once every 10 minutes in a stable temperature environment to periodically update temperature calibration. If the ambient temperature varies, call this function more frequently.

Note

You cannot call this function if your device is operating in [RF list mode](https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html).

Refer to the *Thermal Management* section for your device for more information about typical operating temperatures.

**Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5830/5831/5832/5840/5841/5842

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies your instrument session. vi is obtained from the niRFSA_Init or niRFSA_InitWithOptions function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsa-c-api-ref path=group____root__ni_r_f_s_a__functions__utility__error__info_1gaffa80b8edb502a32d6a44cb31926eacf.html language=enus -->
## TOPIC 00164: niRFSA_ErrorMessage

- bundle_id: `rfsa-c-api-ref`
- source_path: `group____root__ni_r_f_s_a__functions__utility__error__info_1gaffa80b8edb502a32d6a44cb31926eacf.html`
- source_url: https://docs-be.ni.com/bundle/rfsa-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_a__functions__utility__error__info_1gaffa80b8edb502a32d6a44cb31926eacf.html
- document_id: `rfsa-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a status code returned by an NI-RFSA function into a user-readable string. SyntaxViStatus _VI_FUNC niRFSA_ErrorMessage(ViSession vi, ViStatus statusCode, ViConstString errorMessage[])RemarksSupported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646,

### niRFSA_ErrorMessage

Converts a status code returned by an NI-RFSA function into a user-readable string.

#### Syntax

ViStatus _VI_FUNC niRFSA_ErrorMessage(ViSession vi, ViStatus statusCode, ViConstString errorMessage[])

#### Remarks

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5840

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The ViSession handle that you obtain from niRFSA_Init or niRFSA_InitWithOptions. The handle identifies a particular instrument session.You can pass VI_NULL for this parameter. Passing VI_NULL is useful when niRFSA_Init or niRFSA_InitWithOptions fails. |
| statusCode | [in] | ViStatus | Passes the status parameter that is returned from any NI-RFSA function. |
| errorMessage | [in] | ViConstString[] | Returns the user-readable message string that corresponds to the status code you specify.You must pass a ViChar array with 1024 bytes or more to this parameter. Only the first 1024 bytes of the array are used. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFSA function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSA_GetError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga56f3dda5b675deb2e8354757928aaf49.html) function. To clear the error information from NI-RFSA, call the [niRFSA_ClearError](group____root__ni_r_f_s_a__functions__utility__error__info_1ga734bd7fd9363b1eca615c0da98837060.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Error Info
