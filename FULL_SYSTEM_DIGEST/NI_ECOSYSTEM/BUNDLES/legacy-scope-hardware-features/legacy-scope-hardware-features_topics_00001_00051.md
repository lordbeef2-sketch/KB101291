# NI DOCUMENT BUNDLE: legacy-scope-hardware-features

<!--NI_BUNDLE_CHUNK bundle=legacy-scope-hardware-features start=1 end=51 -->
<!--NI_TOPIC bundle=legacy-scope-hardware-features path=alias-protected-decimation.html language=enus -->
## TOPIC 00001: Alias-Protected Decimation

- bundle_id: `legacy-scope-hardware-features`
- source_path: `alias-protected-decimation.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/alias-protected-decimation.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: For alias-protected decimation applications, complete the following steps:Set the DDC Enabled property to True. Set the Data Processing Mode property to Real. Set the Min Sample Rate property to the desired decimated sample rate. Set the Frequency Translation Enabled property to False.

Alias-Protected Decimation

[IMAGE alt='1378' src='GUID-D3C5135C-9F2E-47A7-8AEC-EA4EBF5FFC5C-a5.svg']

For alias-protected decimation applications, complete the following steps:

1. Set the DDC Enabled property to True.
2. Set the Data Processing Mode property to Real.
3. Set the Min Sample Rate property to the desired decimated sample rate.
4. Set the Frequency Translation Enabled property to False.

Parent topic:

Common DDC Applications (NI 5142)

Parent topic:

Common DDC Applications (NI 5622)

Related information:

- NI-SCOPE LabVIEW VIs

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=baseband-decimation.html language=enus -->
## TOPIC 00002: Baseband Decimation

- bundle_id: `legacy-scope-hardware-features`
- source_path: `baseband-decimation.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/baseband-decimation.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: For baseband decimation applications, complete the following steps:Set the DDC Enabled property to True. Set the Data Processing Mode property to Complex. Set the Min Sample Rate property to the desired baseband sample rate. Set the Frequency Translation Enabled property to False. Set the Q Source p

Baseband Decimation

[IMAGE alt='1378' src='GUID-65B70056-F768-44F3-98A4-5ECC67A6A042-a5.svg']

For baseband decimation applications, complete the following steps:

1. Set the DDC Enabled property to True.
2. Set the Data Processing Mode property to Complex.
3. Set the Min Sample Rate property to the desired baseband sample rate.
4. Set the Frequency Translation Enabled property to False.
5. Set the Q Source property to "1" .

Parent topic:

Common DDC Applications (NI 5142)

Related information:

- NI-SCOPE LabVIEW VIs

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=center-frequency.html language=enus -->
## TOPIC 00003: Center Frequency

- bundle_id: `legacy-scope-hardware-features`
- source_path: `center-frequency.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/center-frequency.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Center Frequency property/attribute indicates the frequency by which the frequency translation stage of the DDC block frequency translates the input data; that is, the center frequency of the region of the spectrum that you want to downconvert to baseband. LabVIEW PropertyC/C++ Attribute Center

Center Frequency

The Center Frequency
property/attribute indicates the frequency by which the frequency translation stage of the DDC 
block frequency translates the input data; that is, the center frequency of the region of the spectrum that you want to downconvert to baseband.

| LabVIEW Property | C/C++ Attribute |
| --- | --- |
| Center Frequency | NISCOPE_ATTR_CENTER_FREQUENCY |

Parent topic:

OSP Basic Properties/Attributes

Related information:

- NI-SCOPE LabVIEW VIs
- NI-SCOPE C Function Reference

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ddc-enabled.html language=enus -->
## TOPIC 00004: DDC Enabled

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ddc-enabled.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ddc-enabled.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The DDC Enabled property/attribute activates the functionality of the DDC block. To use any of the features in the DDC block, you must set DDC Enabled to TRUE.LabVIEWC/C++DDC EnabledNISCOPE_ATTR_DDC_ENABLED To achieve maximum flatness in the filter response of the device in DDC mode, set the maxim

DDC Enabled

The DDC Enabled property/attribute activates the functionality of
 the DDC block. To use any of the features in the DDC block, you must set DDC Enabled to TRUE.

| LabVIEW | C/C++ |
| --- | --- |
| DDC Enabled | NISCOPE_ATTR_DDC_ENABLED |

Tip

–1

#### Hardware Calibration of Binary Data

In a normal acquisition, you cannot assume that the binary data maps perfectly to the vertical range. 
 For example, if you fetch 16-bit binary data, you might expect that the positive full scale binary value 
 corresponds to the maximum positive voltage of the vertical range, and that the negative full scale 
 binary value corresponds to the maximum negative voltage. This is not the case, however, 
 for a number of reasons. First, the full scale of the ADC is not mapped to the vertical range. 
 A few codes on the positive and negative ends are left as headroom, in case the input signal
 slightly exceeds the specified vertical range. Second, the binary values do not account for 
 the required corrections to gain and offset based on calibration data. 
 If you fetch binary data, you can convert to voltage values using the gain and offset values from the 
 wfmInfo struct. These values account for the ADC normalization 
 and calibration data.

Voltage = (Binary Value × wfmInfo.gain) + wfmInfo.offset

When the DDC is enabled, the onboard signal processing block accounts for both ADC normalization and 
calibration data. So the waveform samples are stored and can be fetched as calibrated, normalized 
binary data. This means that the range of binary values maps exactly to the vertical range you 
configure.

Voltage = Binary Value × Range/2<sup>(ADC resolution in bits)</sup>

The gain and offset values in the wfmInfo struct work
 just as well in this case (but they do not hold normalization and calibration information), so 
 the following conversion still works:

Voltage = (Binary Value × wfmInfo.gain) + wfmInfo.offset

In a normal acquisition, you must know the gain and offset values to correctly convert the binary 
data to voltage values. In DDC mode, you can assume the following:

- The maximum positive binary value
 maps to the maximum positive voltage of the vertical range.
- The maximum negative binary value maps to
 the maximum negative voltage of the vertical range.
- The vertical range is divided 
 evenly across 
 the possible binary values.

These assumptions may be useful for streaming or logging binary data, because
 
 you do not need to know the gain and offset value to recover the measured voltages.

Parent topic:

OSP Basic Properties/Attributes

Related information:

- NI-SCOPE LabVIEW VIs
- NI-SCOPE C Function Reference

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=digital-offset.html language=enus -->
## TOPIC 00005: Digital Offset

- bundle_id: `legacy-scope-hardware-features`
- source_path: `digital-offset.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/digital-offset.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The digital offset can be used to change the offset of each channel. You can program the digital offset of each channel independently using the Digital Offset attribute. The offset can range from –(Vertical Range × 0.4) to +(Vertical Range × 0.4) The digital offset circuit can overflow if the follow

Digital Offset

The digital offset can be used to change the offset of each channel. You can program the 
digital offset of each channel independently using the 
 
 Digital Offset attribute. The offset can range 
 from –(Vertical Range × 0.4) to +(Vertical Range × 0.4) The digital offset circuit 
 can overflow if the following condition is not met:

–(Vertical Range/2) ≤ Channel Data + Digital Offset ≤ +Vertical Range/2.

If an overflow occurs, the data is clipped and NI-SCOPE returns an error. To prevent data 
clipping, attenuate the waveform data or reduce the digital offset.

Tip

Parent topic:

NI 5142 Onboard Signal Processing Components

Parent topic:

NI 5622 Onboard Signal Processing Components

Related concepts:

- Digital Offset
- Overflow Error Reporting

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=equalization-fir-filter.html language=enus -->
## TOPIC 00006: Equalization FIR Filter

- bundle_id: `legacy-scope-hardware-features`
- source_path: `equalization-fir-filter.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/equalization-fir-filter.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: Equalization FIR Filter is a generic FIR filter. You can download coefficients to the filter using the niscope Configure Equalization Filter Coefficients VI or the niScope_ConfigureEqualizationFilterCoefficients function. The number of coefficients you can download to the filter is determined by the

Equalization FIR Filter

Equalization FIR Filter is a generic FIR filter. You can download coefficients to the filter using 
the niscope Configure Equalization Filter Coefficients VI or the 
niScope_ConfigureEqualizationFilterCoefficients function.

The number of coefficients you can download to the filter is determined by the Equalization Num Coefficients property or the 
NISCOPE_ATTR_EQUALIZATION_NUM_COEFFICIENTS attribute. 
After the coefficients are downloaded, you can use the Equalization Filter Enabled property 
 or the NISCOPE_ATTR_EQUALIZATION_FILTER_ENABLED attribute to enable 
the filter in the hardware. The Equalization FIR Filter can overflow if the data values exceed the vertical range.

Parent topic:

NI 5142 Onboard Signal Processing Components

Parent topic:

NI 5622 Onboard Signal Processing Components

Related information:

- NI-SCOPE LabVIEW VIs
- NI-SCOPE C Function Reference

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=features-supported-by-ni-scope-instruments.html language=enus -->
## TOPIC 00007: Features Supported by NI-SCOPE Instruments

- bundle_id: `legacy-scope-hardware-features`
- source_path: `features-supported-by-ni-scope-instruments.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/features-supported-by-ni-scope-instruments.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to this page for a comparison by feature category of the features supported by NI oscilloscopes. Instruments with multiple bus type variants (for example, PXIe and PXI) are shown separately only when the bus type affects the available features. These instruments are configurable in Measurem

Features Supported by NI-SCOPE Instruments

Refer to this page for a comparison by feature category of the features supported by NI
 oscilloscopes.

Note

- Instruments with multiple bus type variants (for example, PXIe and PXI) are shown
 separately only when the bus type affects the available features.
- These instruments are configurable in Measurement & Automation Explorer (MAX).
 Refer to the getting started guide for each instrument for configuration information.
- Refer to the specifications for each instrument for detailed information on the
 supported features.

Refer to the following categories to compare oscilloscope functionality:

| Instrument | Input Channels | Input Impedance | Maximum Input Range | DC Offset? | Input Coupling | 3 dB Bandwidth1 |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 50 Ω | 1 MΩ | Unfiltered | Analog Filter | Digital FIR Filter |  |  |  |  |  |
| PXIe/PXI/PCI-5105 | 8 | 50 Ω 1 MΩ | ±3 V | ±15 V | ✕ | AC2 DC | 60 MHz | 24 MHz | - |
| PXIe-5110 | 2 | 50 Ω 1 MΩ | ±5 V | ±20 V | ✔ | AC DC | 100 MHz | 20 MHz | - |
| PXIe-5111 | 350 MHz |  |  |  |  |  |  |  |  |
| PXIe-5113 | 500 MHz | 350 MHz 20 MHz |  |  |  |  |  |  |  |
| PXIe/PXI/PCI-5114 | 2 | 50 Ω 1 MΩ | ±5 V | ±20 V | ✔ | AC2 DC GND | 125 MHz | 20 MHz | - |
| PXIe/PXI/PCI-5122 | 2 | 50 Ω 1 MΩ | ±5 V | ±10 V | ✔ | AC2 DC GND | 100 MHz | 35 MHz 20 MHz | - |
| PXI/PCI-5124 | 2 | 50 Ω 1 MΩ | ±5 V | ±10 V | ✔ | AC2 DC GND | 150 MHz | 60 MHz 20 MHz | - |
| USB-5132 | 2 | 1 MΩ | - | ±20 V | ✔ | AC DC GND | 50 MHz | 20 MHz | - |
| USB-5133 |  |  |  |  |  |  |  |  |  |
| PXI/PCI-5142 | 2 | 50 Ω 1 MΩ | ±5 V | ±10 V | ✔ | AC2 DC GND | 100 MHz | 35 MHz 20 MHz | - |
| PXI/PCI-5152 | 2 | 50 Ω 1 MΩ | ±5 V | ±5 V | ✔ | AC DC GND | 300 MHz | 20 MHz | - |
| PXI/PCI-5153 | 50 Ω | ±2.5 V | - | ✕ | 500 MHz | 20 MHz | - |  |  |
| PXI/PCI-5154 | 1 GHz | 20 MHz | - |  |  |  |  |  |  |
| PXIe-5160 | 2 or 4 | 50 Ω 1 MΩ | ±2.5 V | ±25 V | ✔ | AC DC | 50 Ω: 500 MHz 1 MΩ: 300 MHz | 175 MHz 20 MHz | - |
| PXIe-5162 | 50 Ω: 1.5 GHz 1 MΩ: 300 MHz | 175 MHz 20 MHz | - |  |  |  |  |  |  |
| PXIe-5163 | 2 | 50 Ω 1 MΩ | ±2.5 V | ±50 V | ✕ | AC DC | 200 MHz | Low-pass: 150 MHz 30 MHz 20 MHz High-pass: 450 Hz 90 Hz | - |
| PXIe-5164 | 50 Ω: 400 MHz 1 MΩ: 300 MHz | - |  |  |  |  |  |  |  |
| PXIe-5170 | 4 or 8 | 50 Ω | ±2.5 V | - | ✕ | AC DC | 100 MHz | - | - |
| PXIe-5171 | 8 | 250 MHz | 100 MHz | - |  |  |  |  |  |
| PXIe-5172 | 4 or 8 | 50 Ω 1 MΩ | ±5 V | ±40 V | ✕ | 100 MHz | - | 80 MHz 40 MHz 20 MHz |  |
| PXIe-51853 | 2 | 50 Ω 1 MΩ | ±0.5 V | ±5 V | ✔ | AC2 DC | 50 Ω: 3 GHz 1 MΩ: 500 MHz | - | - |
| PXIe-51863 | 50 Ω: 5 GHz 1 MΩ: 500 MHz |  |  |  |  |  |  |  |  |
| PXIe-5622 | 1 | 50 Ω | ±1.4 V | - | ✕ | AC GND | Direct path: 3 MHz to 250 MHz Bandpass path: 162.5 MHz to 212.5 MHz | - | - |
| PXI/PCI-5922 | 2 | 50 Ω 1 MΩ | ±5 V | ±5 V | ✕ | AC DC GND | 0.4 × Sample Rate (6 MHz maximum) | - | - |

| Instrument | Maximum Sample Rate | Time Stamps |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Real-Time Sampling | Time-Interleaved Sampling (TIS) | Random Interleaved Sampling (RIS) | Absolute | Relative |  |
| PXIe/PXI/PCI-5105 | 60 MS/s | - | - | ✔ | ✔ |
| PXIe-5110 | 500 MS/s | 1 GS/s | - | ✔ | ✔ |
| PXIe-5111 | 1.5 GS/s | 3 GS/s |  |  |  |
| PXIe-5113 | 3 GS/s |  |  |  |  |
| PXIe/PXI/PCI-5114 | 250 MS/s | - | 5 GS/s | ✔ | ✔ |
| PXIe/PXI/PCI-5122 | 100 MS/s | - | 2 GS/s | ✔ | ✔ |
| PXI/PCI-5124 | 200 MS/s | - | 4 GS/s | ✔ | ✔ |
| USB-5132 | 50 MS/s | - | - | ✕ | ✔ |
| USB-5133 | 100 MS/s |  |  |  |  |
| PXI/PCI-5142 | 100 MS/s | - | 2 GS/s | ✔ | ✔ |
| PXI/PCI-5152 | 1 GS/s | 2 GS/s | 20 GS/s | ✔ | ✔ |
| PXI/PCI-5153 |  |  |  |  |  |
| PXI/PCI-5154 |  |  |  |  |  |
| PXIe-5160 | 1.25 GS/s | 2.5 GS/s | 50 GS/s | ✔ | ✔ |
| PXIe-5162 | 5 GS/s | 100 GS/s |  |  |  |
| PXIe-5163 | 1 GS/s | - | - | ✔ | ✔ |
| PXIe-5164 |  |  |  |  |  |
| PXIe-5170 | 250 MS/s | - | - | ✔ | ✔ |
| PXIe-5171 |  |  |  |  |  |
| PXIe-5172 |  |  |  |  |  |
| PXIe-5185 | 6.25 GS/s | 12.5 GS/s | 250 GS/s | ✔ | ✔ |
| PXIe-5186 |  |  |  |  |  |
| PXIe-5622 | 150 MS/s | - | - | ✔ | ✔ |
| PXI/PCI-5922 | 15 MS/s | - | - | ✔ | ✔ |

| Instrument | Reference Clock | External Sample Clock | Sample Clock Outputs |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Frequency | Input Sources | Outputs | Frequency | Sources |  |  |
| PXIe-5105 | 5 MHz to 20 MHz, 1 MHz increments | PFI 1 PXI_CLK10 | PFI 1 | 4 MHz to 65 MHz | PFI 1 PXI Star | PFI 14 |
| PXI-5105 | PFI 1 PXI_CLK10 | PFI 1 |  |  |  |  |
| PCI-5105 | PFI 1 RTSI clock (RTSI 7) | PFI 1 RTSI clock (RTSI 7) |  |  |  |  |
| PXIe-5110 | 100 MHz | PXI_CLK100 | - | - | - | - |
| PXIe-5111 |  |  |  |  |  |  |
| PXIe-5113 |  |  |  |  |  |  |
| PXIe-5114 | 5 MHz to 20 MHz, 1 MHz increments | CLK IN PXI_CLK10 | PFI <0..1> PXI_Trig <0..6> | 50 MHz to 250 MHz | CLK IN | - |
| PXI-5114 | CLK IN PXI_CLK10 | PFI <0..1> PXI_Trig <0..6> |  |  |  |  |
| PCI-5114 | CLK IN RTSI clock (RTSI 7) | PFI <0..1> RTSI clock (RTSI 7) |  |  |  |  |
| PXIe-5122 | 5 MHz to 20 MHz, 1 MHz increments | CLK IN PXI_CLK10 | CLK OUT PFI <0..1> PXI_Trig <0..6> | 30 MHz to 105 MHz | CLK IN PXI Star | CLK OUT PFI <0..1> RTSI <0..6> |
| PXI-5122 | CLK IN PXI_CLK10 | CLK OUT PFI <0..1> PXI_Trig <0..6> |  |  |  |  |
| PCI-5122 | CLK IN RTSI clock (RTSI 7) | CLK OUT PFI <0..1> RTSI clock (RTSI 7) |  |  |  |  |
| PXI-5124 | 5 MHz to 20 MHz, 1 MHz increments | CLK IN PXI_CLK10 | CLK OUT PFI <0..1> PXI_Trig <0..6> | 50 MHz to 210 MHz | CLK IN PXI Star | CLK OUT PFI <0..1> RTSI <0..6> |
| PCI-5124 | CLK IN RTSI clock (RTSI 7) | CLK OUT PFI <0..1> RTSI clock (RTSI 7) |  |  |  |  |
| USB-5132 | - | - | - | 1 MHz to 50 MHz | PFI 1 | - |
| USB-5133 | 1 MHz to 100 MHz |  |  |  |  |  |
| PXI-5142 | 5 MHz to 20 MHz, 1 MHz increments | CLK IN PXI_CLK10 | CLK OUT PFI <0..1> PXI_Trig <0..6> | 30 MHz to 105 MHz | CLK IN PXI Star | CLK OUT PFI <0..1> |
| PCI-5142 | CLK IN RTSI clock (RTSI 7) | CLK OUT PFI <0..1> RTSI clock (RTSI 7) |  |  |  |  |
| PXI-5152 | 1 MHz to 20 MHz, 1 MHz increments | PFI 0 PXI_CLK10 | PFI 1 PXI_Trig <0..6> | 350 MHz to 1 GHz | PFI 0 | - |
| PCI-5152 | PFI 0 RTSI clock (RTSI 7) | PFI 1 RTSI clock (RTSI 7) |  |  |  |  |
| PXI-5153 | PFI 0 PXI_CLK10 | PFI 1 PXI_Trig <0..6> |  |  |  |  |
| PCI-5153 | PFI 0 RTSI clock (RTSI 7) | PFI 1 RTSI clock (RTSI 7) |  |  |  |  |
| PXI-5154 | PFI 0 PXI_CLK10 | PFI 1 PXI_Trig <0..6> |  |  |  |  |
| PCI-5154 | PFI 0 RTSI clock (RTSI 7) | PFI 1 RTSI clock (RTSI 7) |  |  |  |  |
| PXIe-5160 | 10 MHz | CLK IN PXI_CLK10 | CLK OUT | 1.25 GHz to 2.5 GHz | CLK IN | - |
| PXIe-5162 |  |  |  |  |  |  |
| PXIe-5163 | 10 MHz | CLK IN AUX 0 CLK IN PXI_CLK10 | AUX 0 CLK OUT | 1.0 GHz | SMB CLK IN PXIe_DSTAR A | - |
| PXIe-5164 |  |  |  |  |  |  |
| PXIe-5170 | 10 MHz | AUX 0CLK IN PXI_CLK10 | AUX 0 CLK OUT | 150 MHz to 250 MHz | AUX 0CLK IN PXIe_DSTAR A | - |
| PXIe-5171 |  |  |  |  |  |  |
| PXIe-5172 |  |  |  |  |  |  |
| PXIe-5185 | 10 MHz 100 MHz | REF CLK PXI_CLK100 | - | 1.6 GHz to 3.125 GHz | CLK IN | - |
| PXIe-5186 |  |  |  |  |  |  |
| PXIe-5622 | 1 MHz to 100 MHz, 1 MHz increments | CLK IN PXI_CLK100 | CLK OUT | 20 MHz to 150 MHz | CLK IN | CLK OUT |
| PXI-5922 | 1 MHz to 20 MHz, 1 MHz increments | CLK IN PXI_CLK10 | CLK OUT PFI <0..1> PXI_Trig <0..6> | - | - | - |
| PCI-5922 | CLK IN RTSI clock (RTSI 7) | CLK OUT PFI <0..1> RTSI clock (RTSI 7) |  |  |  |  |

| Instrument | Reference Trigger Types | Trigger Holdoff? | Trigger Delay? |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Digital | Edge | Glitch | Hysteresis | Immediate | Runt | Software | Video | Width | Window |  |  |  |
| PXIe/PXI/PCI-5105 | ✔ | ✔ | ✕ | ✔ | ✔ | ✕ | ✔ | ✕ | ✕ | ✔ | ✔ | ✔ |
| PXIe-5110 | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✕ | ✔ | ✔ | ✔ | ✔ |
| PXIe-5111 |  |  |  |  |  |  |  |  |  |  |  |  |
| PXIe-5113 |  |  |  |  |  |  |  |  |  |  |  |  |
| PXIe/PXI/PCI-5114 | ✔ | ✔ | ✕ | ✔ | ✔ | ✕ | ✔ | ✔ | ✕ | ✔ | ✔ | ✔ |
| PXIe/PXI/PCI-5122 | ✔ | ✔ | ✕ | ✔ | ✔ | ✕ | ✔ | ✔ | ✕ | ✔ | ✔ | ✔ |
| PXI/PCI-5124 | ✔ | ✔ | ✕ | ✔ | ✔ | ✕ | ✔ | ✔ | ✕ | ✔ | ✔ | ✔ |
| USB-5132 | ✔ | ✔ | ✕ | ✔ | ✔ | ✕ | ✔ | ✕ | ✕ | ✔ | ✕ | ✔ |
| USB-5133 |  |  |  |  |  |  |  |  |  |  |  |  |
| PXI/PCI-5142 | ✔ | ✔ | ✕ | ✔ | ✔ | ✕ | ✔ | ✔ | ✕ | ✔ | ✔ | ✔ |
| PXI/PCI-5152 | ✔ | ✔ | ✕ | ✔ | ✔ | ✕ | ✔ | ✔ | ✕ | ✔ | ✔ | ✔ |
| PXI/PCI-5153 |  |  |  |  |  |  |  |  |  |  |  |  |
| PXI/PCI-5154 |  |  |  |  |  |  |  |  |  |  |  |  |
| PXIe-5160 | ✔ | ✔ | ✕ | ✔ | ✔ | ✕ | ✔ | ✕ | ✕ | ✕ | ✔ | ✔ |
| PXIe-5162 |  |  |  |  |  |  |  |  |  |  |  |  |
| PXIe-5163 | ✔ | ✔ | ✕ | ✔ | ✔ | ✕ | ✔ | ✕ | ✕ | ✔ | ✔ | ✔ |
| PXIe-5164 |  |  |  |  |  |  |  |  |  |  |  |  |
| PXIe-5170 | ✔ | ✔ | ✕ | ✔ | ✔ | ✕ | ✔ | ✕ | ✕ | ✔ | ✔ | ✔ |
| PXIe-5171 |  |  |  |  |  |  |  |  |  |  |  |  |
| PXIe-5172 |  |  |  |  |  |  |  |  |  |  |  |  |
| PXIe-5185 | ✔ | ✔ | ✕ | ✕ | ✔ | ✕ | ✔ | ✕ | ✕ | ✕ | ✔ | ✔ |
| PXIe-5186 |  |  |  |  |  |  |  |  |  |  |  |  |
| PXIe-5622 | ✔ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✔ | ✔ |
| PXI/PCI-5922 | ✔ | ✔ | ✕ | ✔ | ✔ | ✕ | ✔ | ✕ | ✕ | ✔ | ✔ | ✔ |

| Instrument | Reference Trigger Sources (Bus-Independent) | Trigger Coupling | External TRIG Input Impedance |  |
| --- | --- | --- | --- | --- |
| Analog Input Channel | External TRIG Input |  |  |  |
| PXIe/PXI/PCI-5105 | CH <0..7> PFI 1 | Same as input channel | - | - |
| PXIe-5110 | CH <0..1> PFI <0..3> | Same as input channel HF reject LF reject | - | - |
| PXIe-5111 |  |  |  |  |
| PXIe-5113 |  |  |  |  |
| PXIe/PXI/PCI-5114 | CH <0..1> PFI <0..1> TRIG | Same as input channel HF reject LF reject | AC DC LF reject HF reject AC + HF reject | 1 MΩ |
| PXIe/PXI/PCI-5122 | CH <0..1> PFI <0..1> TRIG | Same as input channel HF reject LF reject | AC DC LF reject HF reject AC + HF reject | 1 MΩ |
| PXI/PCI-5124 | CH <0..1> PFI <0..1> TRIG | Same as input channel HF reject LF reject | AC DC LF reject HF reject AC + HF reject | 1 MΩ |
| USB-5132 | CH <0..1> PFI 1 | Same as input channel | - | - |
| USB-5133 |  |  |  |  |
| PXI/PCI-5142 | CH <0..1> PFI <0..1> TRIG | Same as input channel HF reject LF reject | AC DC LF reject HF reject AC + HF reject | 1 MΩ |
| PXI/PCI-5152 | CH <0..1> PFI <0..1> TRIG | Same as input channel HF reject LF reject | AC DC LF reject HF reject AC + HF reject | 1 MΩ |
| PXI/PCI-5153 | CH <0..1> PFI <0..1> TRIG | DC LF reject HF reject | 2.25 kΩ |  |
| PXI/PCI-5154 | CH <0..1> PFI <0..1> TRIG |  |  |  |
| PXIe-5160 | CH <0..n> PFI <0..1> TRIG | Same as input channel HF reject LF reject | AC DC LF reject HF reject AC + HF reject | Software selectable: 50 Ω or 1 MΩ |
| PXIe-5162 |  |  |  |  |
| PXIe-5163 | CH <0..1> SMB PFI 0 AUX 0 PFI <0..7> | Same as input channel HF reject LF reject | - | - |
| PXIe-5164 |  |  |  |  |
| PXIe-5170 | CH <0..n> PFI <0..7> | Same as input channel | - | - |
| PXIe-5171 |  |  |  |  |
| PXIe-5172 |  |  |  |  |
| PXIe-5185 | CH <0..1> TRIG | Same as input channel | DC | 50 Ω |
| PXIe-5186 |  |  |  |  |
| PXIe-5622 | IF IN | - | - | - |
| PXI/PCI-5922 | CH <0..1> PFI <0..1> TRIG | Same as input channel | DC | 1 MΩ |

Note

The reference trigger sources available on NI oscilloscopes specific to bus type are
 as follows:

- PXIe
 oscilloscopes: PXI_Trig <0..7>
- PXI
 oscilloscopes: PXI_Trig <0..7>, PXI Star
- PCI
 oscilloscopes: RTSI <0..7>

The previous table excludes these bus-dependent reference trigger sources and lists
 only those sources that are unique to each instrument.

| Instrument | Synchronization Signal Sources | Synchronization Signal Outputs |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Arm Reference Trigger | Record Advance Trigger | Start Trigger | Reference Trigger | End of Record Event | End of Acquisition Event | Start Trigger |  |
| PXIe-5105 | PFI 1 PXI_Trig <0..7> | PFI 1 PXI Star RTSI <0..7> | PFI 1 RTSI <0..7> | PFI 1 RTSI <0..6> |  |  |  |
| PXI-5105 | PFI 1 PXI_Trig <0..7> PXI Star | PFI 1 PXI Star RTSI <0..7> |  |  |  |  |  |
| PCI-5105 | PFI 1 RTSI <0..7> | PFI 1 RTSI <0..7> |  |  |  |  |  |
| PXIe-5110 | PFI <0..3> PXI_Trig <0..7> | PFI <0..3> PXI_Trig <0..7> | PFI <0..3> PXI_Trig <0..7> | PFI <0..3> PXI_Trig <0..6> |  |  |  |
| PXIe-5111 |  |  |  |  |  |  |  |
| PXIe-5113 |  |  |  |  |  |  |  |
| PXIe-5114 | PFI <0..1> PXI_Trig <0..7> | PFI <0..1> PXI Star RTSI <0..7> | PFI <0..1> RTSI <0..7> | PFI <0..1> RTSI <0..6> |  |  |  |
| PXI-5114 | PFI <0..1> PXI_Trig <0..7> PXI Star | PFI <0..1> PXI Star RTSI <0..7> |  |  |  |  |  |
| PCI-5114 | PFI <0..1> PXI_Trig <0..7> RTSI <0..7> | PFI <0..1> RTSI <0..7> |  |  |  |  |  |
| PXIe-5122 | PFI <0..1> PXI_Trig <0..7> | PFI <0..1> PXI Star RTSI <0..7> | PFI <0..1> RTSI <0..7> | PFI <0..1> RTSI <0..6> |  |  |  |
| PXI-5122 | PFI <0..1> PXI_Trig <0..7> PXI Star | PFI <0..1> PXI Star RTSI <0..7> |  |  |  |  |  |
| PCI-5122 | PFI <0..1> PXI_Trig <0..7> RTSI <0..7> | PFI <0..1> RTSI <0..7> |  |  |  |  |  |
| PXI-5124 | PFI <0..1> PXI_Trig <0..7> PXI Star | PFI <0..1> PXI Star RTSI <0..7> | PFI <0..1> PXI Star RTSI <0..7> | PFI <0..1> RTSI <0..6> |  |  |  |
| PCI-5124 | PFI <0..1> PXI_Trig <0..7> RTSI <0..7> | PFI <0..1> RTSI <0..7> |  |  |  |  |  |
| USB-5132 | - | - | PFI 1 | PFI 1 | - | PFI 1 | PFI 1 |
| USB-5133 |  |  |  |  |  |  |  |
| PXI-5142 | PFI <0..1> PXI_Trig <0..7> PXI Star | PFI <0..1> PXI Star RTSI <0..7> | PFI <0..1> PXI Star RTSI <0..7> | PFI <0..1> RTSI <0..6> |  |  |  |
| PCI-5142 | PFI <0..1> PXI_Trig <0..7> RTSI <0..7> | PFI <0..1> RTSI <0..7> |  |  |  |  |  |
| PXI-5152 | PFI <0..1> PXI_Trig <0..7> PXI Star | PFI <0..1> PXI Star RTSI <0..7> | PFI <0..1> PXI Star RTSI <0..7> | PFI <0..1> RTSI <0..6> |  |  |  |
| PCI-5152 | PFI <0..1> PXI_Trig <0..7> RTSI <0..7> | PFI <0..1> RTSI <0..7> |  |  |  |  |  |
| PXI-5153 | PFI <0..1> PXI_Trig <0..7> PXI Star | PFI <0..1> PXI Star RTSI <0..7> |  |  |  |  |  |
| PCI-5153 | PFI <0..1> PXI_Trig <0..7> RTSI <0..7> | PFI <0..1> RTSI <0..7> |  |  |  |  |  |
| PXI-5154 | PFI <0..1> PXI_Trig <0..7> PXI Star | PFI <0..1> PXI Star RTSI <0..7> |  |  |  |  |  |
| PCI-5154 | PFI <0..1> PXI_Trig <0..7> RTSI <0..7> | PFI <0..1> RTSI <0..7> |  |  |  |  |  |
| PXIe-5160 | PFI <0..1> PXI_Trig <0..7> | PFI <0..1> PXI_Trig <0..7> | PFI <0..1> PXI_Trig <0..7> | PFI <0..1> PXI_Trig <0..6> |  |  |  |
| PXIe-5162 |  |  |  |  |  |  |  |
| PXIe-5163 | PFI <0..7> PXI_Trig <0..7> | PFI <0..7> PXI_Trig <0..7> | PFI <0..7> PXI_Trig <0..7> | PFI <0..7> PXI_Trig <0..6> |  |  |  |
| PXIe-5164 |  |  |  |  |  |  |  |
| PXIe-5170 | PFI <0..7> PXI_Trig <0..7> | PFI <0..7> PXI_Trig <0..7> | PFI <0..7> PXI_Trig <0..7> | PFI <0..7> PXI_Trig <0..6> |  |  |  |
| PXIe-5171 |  |  |  |  |  |  |  |
| PXIe-5172 |  |  |  |  |  |  |  |
| PXIe-51855 | - | PXI_Trig <0..6> | PXI_Trig <0..6> | PXI_Trig <0..6> |  |  |  |
| PXIe-51865 |  |  |  |  |  |  |  |
| PXIe-5622 | PFI 1 PXI_Trig <0..7> | PFI 1 PXI_Trig <0..7> | PFI 1 PXI_Trig <0..7> | PFI <0..1> PXI_Trig <0..6> |  |  |  |
| PXI-5922 | PFI <0..1> PXI_Trig <0..7> PXI Star | PFI <0..1> PXI Star RTSI <0..7> | PFI <0..1> PXI Star RTSI <0..7> | PFI <0..1> PXI_Trig <0..6> |  |  |  |
| PCI-5922 | PFI <0..1> RTSI <0..7> | PFI <0..1> RTSI <0..7> |  |  |  |  |  |

| Instrument | Resolution | Multiple Record Acquisitions? | Continuous Acquisition? | DDC Acquisition Mode? |
| --- | --- | --- | --- | --- |
| PXIe/PXI/PCI-5105 | 12 bits | ✔ | ✔ | ✕ |
| PXIe-5110 | 8 bits | ✔ | ✔ | ✕ |
| PXIe-5111 |  |  |  |  |
| PXIe-5113 |  |  |  |  |
| PXIe/PXI/PCI-5114 | 8 bits | ✔ | ✔ | ✕ |
| PXIe/PXI/PCI-5122 | 14 bits | ✔ | ✔ | ✕ |
| PXI/PCI-5124 | 12 bits | ✔ | ✔ | ✕ |
| USB-5132 | 8 bits | ✕ | ✔ | ✕ |
| USB-5133 |  |  |  |  |
| PXI/PCI-5142 | 14 bits | ✔ | ✔ | ✔ |
| PXI/PCI-5152 | 8 bits | ✔ | ✔ | ✕ |
| PXI/PCI-5153 |  |  |  |  |
| PXI/PCI-5154 |  |  |  |  |
| PXIe-5160 | 10 bits | ✔ | ✔ | ✕ |
| PXIe-5162 |  |  |  |  |
| PXIe-5163 | 14 bits | ✔ | ✔ | ✕ |
| PXIe-5164 |  |  |  |  |
| PXIe-5170 | 14 bits | ✔ | ✔ | ✕ |
| PXIe-5171 |  |  |  |  |
| PXIe-5172 |  |  |  |  |
| PXIe-5185 | 8 bits | ✔ | ✔ | ✕ |
| PXIe-5186 |  |  |  |  |
| PXIe-5622 | 16 bits | ✔ | ✔ | ✔ |
| PXI/PCI-5922 | Flexible resolution, up to 24 bits | ✔ | ✔ | ✕ |

| Instrument | Self-Calibration? | Probe Compensation Signal Output6 | LabVIEW Real-Time Support?7 | Onboard Signal Processing Support? | Reconfigurable FPGA? | CableSenseT Capable?8 | Onboard Memory Options9 | Supported Sample Widths |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PXIe/PXI/PCI-5105 | ✔ | PFI 1 | ✔ | ✕ | ✕ | ✕ | 16 MB 128 MB 512 MB | 16 bits |
| PXIe-5110 | ✔ | Probe compensation terminals | ✕ | ✕ | ✕ | ✔ | 64 MB 512 MB | 8 bits |
| PXIe-5111 |  |  |  |  |  |  |  |  |
| PXIe-5113 |  |  |  |  |  |  |  |  |
| PXIe/PXI/PCI-5114 | ✔ | PFI 1 | ✔ | ✕ | ✕ | ✕ | 8 MB 64 MB 256 MB | 8 bits |
| PXIe-5122 | ✔ | PFI 1 | ✔ | ✕ | ✕ | ✕ | 8 MB 64 MB 256 MB | 16 bits (default) 8 bits |
| PXI-5122 | 8 MB 32 MB 256 MB 512 MB |  |  |  |  |  |  |  |
| PCI-5122 | 8 MB 32 MB 256 MB |  |  |  |  |  |  |  |
| PXI/PCI-5124 | ✔ | PFI 1 | ✔ | ✕ | ✕ | ✕ | 8 MB 32 MB 256 MB 512 MB | 16 bits (default) 8 bits |
| USB-5132 | ✔10 | PFI 1 | ✕ | ✕ | ✕ | ✕ | 8 MB 64 MB | 8 bits |
| USB-5133 |  |  |  |  |  |  |  |  |
| PXI/PCI-5142 | ✔ | PFI 1 | ✔ | ✔ | ✕ | ✕ | 64 MB 256 MB | 16 bits (default) 8 bits |
| PXI/PCI-5152 | ✔ | PFI 1 | ✔ | ✕ | ✕ | ✕ | 16 MB 128 MB 512 MB | 8 bits |
| PXI/PCI-5153 |  |  |  |  |  |  |  |  |
| PXI/PCI-5154 |  |  |  |  |  |  |  |  |
| PXIe-5160 | ✔ | PFI 1 | ✔ | ✕ | ✕ | ✔ | 64 MB 2 GB | 16 bits (default) 8 bits |
| PXIe-5162 |  |  |  |  |  |  |  |  |
| PXIe-5163 | ✔ | SMB PFI 0 | ✕ | ✕ | ✕ | ✕ | 512 MB | 16 bits |
| PXIe-5164 | ✔ | 1.5 GB |  |  |  |  |  |  |
| PXIe-5170 | ✔ | - | ✕ | ✕ | ✔ | ✕ | 0.75 GB 1.5 GB | 16 bits |
| PXIe-5171 | 1.5 GB |  |  |  |  |  |  |  |
| PXIe-5172 | 0.75 GB 1.5 GB |  |  |  |  |  |  |  |
| PXIe-5185 | ✔11 | - | ✔ | ✕ | ✕ | ✕ | 32 MB 1 GB | 8 bits |
| PXIe-5186 |  |  |  |  |  |  |  |  |
| PXIe-5622 | ✔ | - | ✔ | ✔ | ✕ | ✕ | 64 MB 256 MB | 16 bits (default) 8 bits |
| PXI/PCI-5922 | ✔11 | - | ✔ | ✕ | ✕ | ✕ | 16 MB 64 MB 512 MB | 32 bits (default) 16 bits |

<sup>1</sup> All filters are
 low-pass unless otherwise noted.

<sup>2</sup> Available on 1 MΩ input impedance
 only.

<sup>3</sup> 1 MΩ available on modules with
 part numbers as follows:

- PXIe-5185: 152962 x -0 z L
- PXIe-5186: 152961 x -0 z L

where x is any letter and z is any number.

<sup>4</sup> Sample clock
 may be exported only at full rate.

<sup>5</sup> Can
 simultaneously export or import a maximum of four triggers or
 events.

<sup>6</sup> 1
 kHz square wave.

<sup>7</sup> Applies to instruments with PXIe
 and PXI bus types only.

<sup>8</sup> CableSense-capable instruments may not
 include the CableSense option. To use CableSense, you must
 purchase a CableSense-capable instrument that includes the
 CableSense option.

<sup>9</sup> Total module memory. The maximum
 memory available to each channel in a session is the module
 total divided by the number of channels enabled in the
 session.

<sup>10</sup> Self-calibration of DC offset
 only.

<sup>11</sup> Self-calibration not
 supported on Linux systems.

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=filtering-and-decimation.html language=enus -->
## TOPIC 00008: Filtering and Decimation

- bundle_id: `legacy-scope-hardware-features`
- source_path: `filtering-and-decimation.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/filtering-and-decimation.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The filtering and decimation stage of the OSP block reduces the effective sample rate of the digitizer while protecting the frequency spectrum of the decimated data from aliases. This protection occurs when the data passes through a lowpass filter before decimation. The normal decimation in digitize

Filtering and Decimation

The filtering and decimation stage of the OSP block reduces the effective sample rate of the 
digitizer while protecting the frequency spectrum of the decimated data from aliases. 
This protection occurs when the data passes through a lowpass filter before decimation. 
 The normal decimation in digitizers (when not using OSP) does not protect the frequency spectrum of the decimated data 
 from aliases.

[IMAGE alt='1378' src='GUID-839B0C58-B30B-4F52-B9ED-50FBA063CD3A-a5.svg']

Parent topic:

NI 5142 Onboard Signal Processing Components

Parent topic:

NI 5622 Onboard Signal Processing Components

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni--51225124514256225922-trigger-delay.html language=enus -->
## TOPIC 00009: NI 5122/5124/5142/5622/5922 Trigger Delay

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni--51225124514256225922-trigger-delay.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni--51225124514256225922-trigger-delay.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger delay, which is specified in seconds, is achieved by adding the appropriate number of posttrigger samples to the record while keeping the allocated onboard memory equal to the record size you request. NI-SCOPE then corrects the trigger time by the delay you specify. To determine the maximum

NI 5122/5124/5142/5622/5922 Trigger Delay

Trigger delay, which is specified in seconds, is achieved by adding the 
appropriate number of posttrigger samples to the record while keeping the allocated onboard
 memory equal to the record size you request. NI-SCOPE then corrects the trigger time by the 
 delay you specify. To determine the maximum delay for a particular actual sample rate, use the following formula:

Max trigger delay in seconds = [(2<sup>34</sup> – 1) – requested posttrigger samples] × (1/actual sample rate)

Note

The maximum trigger delay also changes based on the binary sample width. When binary 
 sample width is set to 8, the maximum trigger delay is doubled. When binary sample width 
 is set to 32, the maximum trigger delay is halved.

Parent topic:

NI 5114/5122/5124/5142 Analog Trigger Types

Parent topic:

NI 5622 Trigger Types

Related information:

- Trigger Delay

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-5114512251245142-acdcgnd-coupling.html language=enus -->
## TOPIC 00010: NI 5114/5122/5124/5142 AC/DC/GND Coupling

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-5114512251245142-acdcgnd-coupling.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-5114512251245142-acdcgnd-coupling.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can select AC, DC, or GND input coupling for the 1 MΩ input path, and DC or GND input coupling for the 50 Ω input path. Select AC-coupling if the input signal has a DC component that you want to reject, provided that you are not concerned about low-frequency flatness. A DC input offset adjustmen

NI 5114/5122/5124/5142 AC/DC/GND Coupling

You can select AC, DC, or GND input coupling for the 1 MΩ input path, and DC or GND input coupling for the 50 Ω input path. Select AC-coupling if the input signal has a DC component that you want to reject, 
provided that you are not concerned about low-frequency flatness. A DC 
input offset adjustment is available if the signal you want to measure is below this limit, or if you 
are using 
the 50 Ω path.

Ground coupling disconnects the input channel from the signal connected and internally connects the 
channel to ground to provide a ground reference.

Parent topic:

NI 5124 Input Signal Conditioning

Parent topic:

NI 5122/5142 Input Signal Conditioning

Related information:

- Input Coupling

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-5114512251245142-analog-trigger-paths.html language=enus -->
## TOPIC 00011: NI 5114/5122/5124/5142 Analog Trigger Paths

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-5114512251245142-analog-trigger-paths.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-5114512251245142-analog-trigger-paths.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: With high-speed digitizers, triggering capability is as important as input signal conditioning. The NI 5114/5122/5124/5142 provides flexible, high-precision, low-jitter triggering features.The NI 5114/5122/5124/5142 has three fundamental analog trigger paths:Channel 0 input (CH 0) Channel 1 input (C

NI 5114/5122/5124/5142 Analog Trigger Paths

With high-speed digitizers, triggering capability is as important as input 
signal conditioning. The NI 5114/5122/5124/5142 provides flexible, high-precision, low-jitter triggering 
features.

The NI 5114/5122/5124/5142 has three fundamental analog trigger paths:

- Channel 0 input (CH 0)
- Channel 1 input (CH 1)
- External trigger input (TRIG)

The following figure shows the analog trigger paths for the NI 5114/5122/5124/5142.

[IMAGE alt='1378' src='GUID-1BDC7AE0-1C2F-4149-8A2B-347094C048E4-a5.svg']

#### External Trigger Channel (TRIG)

Unlike the input channels (CH 0 and CH 1), the external trigger channel uses a fixed input range and impedance to give a higher bandwidth for triggering
 the digitizer. Signals that travel through the external trigger channel are not digitized.

Parent topic:

NI 5114/5122/5124/5142 Analog Trigger Types

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-5114512251245142-analog-trigger-types.html language=enus -->
## TOPIC 00012: NI 5114/5122/5124/5142 Analog Trigger Types

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-5114512251245142-analog-trigger-types.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-5114512251245142-analog-trigger-types.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5114/5122/5124/5142 supports the following analog trigger types: edge, hysteresis, window, and video triggers.

NI 5114/5122/5124/5142 Analog Trigger Types

The NI 5114/5122/5124/5142 supports the following analog trigger types: 
edge, 
hysteresis, 
window, and 
video triggers.

Parent topic:

NI 5124

Parent topic:

NI 5142

Related information:

- Edge Triggers
- Hysteresis Triggers
- Window Triggers
- Video Triggers

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-5114512251245142-vertical-offset.html language=enus -->
## TOPIC 00013: NI 5114/5122/5124/5142 Vertical Offset

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-5114512251245142-vertical-offset.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-5114512251245142-vertical-offset.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: On NI 5114/5122/5124/5142 devices, you can set a hardware-applied vertical offset up to one-half of the given range, which effectively creates a unipolar range. For example, if you set the vertical offset to –1 V for the 2 V range, you can measure input voltages between 0 and –2 V. Vertical offset

NI 5114/5122/5124/5142 Vertical Offset

On NI 5114/5122/5124/5142 devices, you can set a hardware-applied vertical offset up to one-half of the given range, which effectively creates 
a unipolar range. For example, if you set the vertical offset to –1 V for the 2 V range, you can measure input voltages between 0 and –2 V.

Note

Parent topic:

NI 5124 Input Signal Conditioning

Parent topic:

NI 5122/5142 Input Signal Conditioning

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-5114512251245142-video-triggering.html language=enus -->
## TOPIC 00014: NI 5114/5122/5124/5142 Video Triggering

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-5114512251245142-video-triggering.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-5114512251245142-video-triggering.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5114/5122/5124/5142 includes a mode for triggering on certain video signals. You can trigger on any line, a specific line number, or a specific field. For more information on video signals, refer to Video Fundamentals.The NI 5114/5122/5124/5142 supports negative polarity in video mode for cer

NI 5114/5122/5124/5142 Video Triggering

The NI 5114/5122/5124/5142 includes a mode for triggering on certain 
video signals. You can trigger on any line, a specific line number, or a 
specific field. For more information on video signals, refer to Video 
Fundamentals.

The NI 5114/5122/5124/5142 supports negative polarity in video mode for certain video signal formats.
 Negative trigger polarity means 
 that the synchronization pulses must go to a negative 
voltage with respect to the back porch level. 
 
The following tables show the video formats supported by each digitizer model, 
and whether negative trigger polarity is supported in video mode.

Note

#### NI 5114

| Video Signal Format | FormatSupported | Negative PolaritySupported |
| --- | --- | --- |
| Standard (SDTV) |  |  |
| M-NTSC | √ | √ |
| B/G-PAL | √ | √ |
| SECAM | √ | √ |
| M-PAL | √ | √ |
| Enhanced Definition (EDTV) |  |  |
| 480i/59.94 fps | √ | √ |
| 480i/60 fps | √ | √ |
| 480p/59.94 fps | √ | √ |
| 480p/60 Fps | √ | √ |
| 576i/50 fps | √ | √ |
| 576p/50 Fps | √ | √ |
| High Definition (HDTV) |  |  |
| 720p/50 Fps | √ | N/A |
| 720p/59.94 Fps | √ | N/A |
| 720p/60 Fps | √ | N/A |
| 1080i/50 fps | √ | N/A |
| 1080i/59.94 fps | √ | N/A |
| 1080i/60 fps | √ | N/A |
| 1080p/24 Fps | √ | N/A |

#### NI 5122/5124/5142

Note

| Video Signal Format | FormatSupported | Negative PolaritySupported |
| --- | --- | --- |
| Standard (SDTV) |  |  |
| M-NTSC | √ | √ |
| B/G-PAL | √ | √ |
| SECAM | √ | √ |
| M-PAL | √ | √ |

#### Video Signal DC Restoration

The NI 5114/5122/5124/5142 supports DC restoration, which adjusts the back porch level of the video signal to 
0 V. DC restore is performed on the digital data, rather than with an analog clamping circuit. When using DC restore, set the input voltage range to approximately twice the expected
signal amplitude to prevent signal clipping as the amplitude and offset of the video signal change. DC restore measures the voltage of
the back porch during the interval between the end of the colorburst and before the start of the active line, then subtracts this value from the signal for the remainder of the active video line.
 Excess
 noise on the back porch portion of the video signal may cause inconsistent level restoration
 between lines.

#### Signal Conditioning

To provide proper termination to the video signal, use a 75 Ω terminator on the input of the digitizer in 1 MΩ input mode.

#### Copy Protection System Implications

Many video signal sources, particularly DVD players, produce a copy protection signal. 
DVDs can be encoded to enable this function, which inhibits copying the signal by 
injecting pulses that violate video signal standards, and disrupts input circuitry on 
VCRs. These signals often include false synchronization pulses and signals that exceed 
the voltage range of a standard signal. Any false pulses may cause erroneous line 
triggering on the digitizer. To avoid this error in your application, 
try one of the following solutions:

- Deactivate or remove the copy protection signal from the signal source.
- Recover triggering information in software by taking an untriggered 
waveform with the NI 5114/5122/5124/5142 and searching for legal trigger points in the waveform.

Parent topic:

NI 5114/5122/5124/5142 Analog Trigger Paths

Related information:

- Video Fundamentals
- Avtive Image

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-5114512251245142515251535154--trigger-hold.html language=enus -->
## TOPIC 00015: NI 5114/5122/5124/5142/5152/5153/5154 Trigger Holdoff

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-5114512251245142515251535154--trigger-hold.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-5114512251245142515251535154--trigger-hold.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: For NI 5114/5122/5124/5142/5152/5153/5154 devices, the holdoff timer is started by the Reference Trigger. When the current record finishes and the minimum number of pretrigger samples for the next record have been acquired, the holdoff timer is evaluated. If the timer has expired, the digitizer arms

NI 5114/5122/5124/5142/5152/5153/5154 Trigger Holdoff

For NI 5114/5122/5124/5142/5152/5153/5154 devices, the holdoff timer is started by the Reference Trigger. 
 When the current record finishes and the minimum number of pretrigger samples for the next record 
 have been acquired, the holdoff timer is evaluated. 
 
 If the timer has expired, the digitizer arms its Reference Trigger circuit. If the timer has not expired,
 the digitizer continues pretrigger 
 sampling until the timer expires, and then arms its Reference Trigger circuit. Holdoff is 
 applied for each Reference Trigger during a multirecord acquisition.

#### TDC On

When the time-to-digital converter (TDC) is enabled on the digitizer, the 
minimum holdoff you can set is 10 µs (for the NI 5114/5122/5124/5142) or 8 µs (for the NI 5152/5153/5154). 
This minimum holdoff time between Reference Triggers is required for the TDC
to settle; any holdoff value below these values is coerced up.

#### TDC Off

When the TDC is disabled, 
the minimum holdoff value you can set is decreased to 2 µs (for the NI 5114/5122/5124/5142) or 1 µs (for the NI 5152/5153/5154) when using the internal sample clock. For 
minimum trigger holdoff when using an external sample clock, refer to 
the specifications document for your digitizer.

Parent topic:

NI 5114/5122/5124/5142 Analog Trigger Types

Parent topic:

NI 5152

Parent topic:

NI 5153/5154

Related information:

- Trigger Holdoff
- TDC

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-5114515251535154-trigger-delay.html language=enus -->
## TOPIC 00016: NI 5114/5152/5153/5154 Trigger Delay

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-5114515251535154-trigger-delay.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-5114515251535154-trigger-delay.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger delay, which is specified in seconds, is achieved on the NI 5114/5152/5153/5154 by adding the appropriate number of posttrigger samples to the record while keeping the allocated onboard memory equal to the record size you request. NI-SCOPE then corrects the trigger time by the delay you spec

NI 5114/5152/5153/5154 Trigger Delay

Trigger delay, which is specified in seconds, is achieved on the NI 5114/5152/5153/5154 by adding the 
appropriate number of posttrigger samples to the record while keeping the allocated onboard
 memory equal to the record size you request. NI-SCOPE then corrects the trigger time by the 
 delay you specify. To determine the maximum delay for a particular actual sample rate, use the following formula:

Max trigger delay in seconds = [(2<sup>35</sup> – 1) – requested posttrigger samples] × (1/actual sample rate)

Note

Parent topic:

NI 5152

Parent topic:

NI 5153/5154

Related information:

- Trigger Delay

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-512251245142--input-impedance.html language=enus -->
## TOPIC 00017: NI 5122/5124/5142 Input Impedance

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-512251245142--input-impedance.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-512251245142--input-impedance.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can set the NI 5122/5124/5142/5152 analog input impedance to either 50 Ω or 1 MΩ. The 50 Ω path provides slightly better noise and distortion performance because the high impedance buffer for the 1 MΩ path is bypassed. The 1 MΩ path is required in applications that require minimal loading or tha

NI 5122/5124/5142 Input Impedance

You can set the NI 5122/5124/5142/5152 analog input impedance to either 50 Ω or 1 MΩ. The 50 Ω path provides slightly better noise and
distortion performance because the 
high impedance buffer for the 1 MΩ path is bypassed. The 1 MΩ path is required in applications that require minimal loading or 
that require using a standard 10:1 oscilloscope probe.

#### Protection

The 50 Ω inputs of the NI 5122/5124/5142 are protected by a thermal 
disconnect circuit. If an overvoltage event is large and sudden enough, however, the protection circuits 
might not have enough time to react before permanent damage occurs. It is therefore important 
that you observe the specified maximum signal
input levels, especially when the inputs are set for 50 Ω.

Parent topic:

NI 5124 Input Signal Conditioning

Parent topic:

NI 5122/5142 Input Signal Conditioning

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-512251245142-calibration.html language=enus -->
## TOPIC 00018: NI 5122/5124/5142 Calibration

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-512251245142-calibration.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-512251245142-calibration.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: Every measurement instrument performs within its specifications over some finite temperature range and time period. If the temperature changes and time exceed those specified, and your application requires tight specifications, calibration is required. For example, if the accuracy of a digitizer is

NI 5122/5124/5142 Calibration

Every measurement instrument performs within its specifications over some finite temperature range and time period. 
 If the temperature changes and time exceed those specified, and your application requires tight specifications, 
 calibration
 is required.

For example, if the accuracy of a digitizer is specified as ±(1% of input + 10 mV), and you apply 5 V to the input, the error is:

1% of 5 V + 10 mV = 60 mV 
for temperature range 18-28 °C

This example demonstrates the traditional method of specifying accuracy. 
The problem with the traditional method is that in a system environment, temperature is 
not easily controlled. When a system is composed of multiple integrated instruments, the system is subject to temperature rise caused by inherent compromises in air circulation and 
other 
factors. Self-heating from surrounding equipment, uncontrolled manufacturing floor environment, and dirty 
fan filters are among these factors.

If the ambient temperature is outside of the 18-28 °C range, you may need to know exactly what the 
measurement accuracy is to compensate for this temperature variation. With the traditional method,
the only way to get the specified accuracy outside of the 18-28 °C range is to externally calibrate 
the 
system at the desired temperature. However, an external calibration is time-consuming and expensive and is 
infrequently done, so the specified accuracy is rarely obtained. You can learn more about external calibration at ni.com/calibration.
In the example, if the ambient temperature of the digitizer is 48 °C, assuming the Tempco 
(TC) error is specified as

TC = (0.1% of input +1 mV)/ °C (a typical number is 10% of accuracy/ °C)

The additional error is

20 °C x TC = ±(2% of input + 20 mV) or 120 mV

The total error is three times the specified error (180 mV in the example above, 
versus 60 mV if 
temperature effect is ignored) due to the 48 °C ambient temperature.

#### Self-Calibration

To eliminate errors caused by changing temperatures, NI-SCOPE provides a highly repeatable self-calibration
 
 function.

For the NI 5122/5124/5142, this self-calibration capability yields the following benefits:

- Corrects for DC gain and offset errors within the digitizer by comparison to a precision, 
high-stability internal voltage reference. This is done for all ranges, 
both input impedance paths (50 Ω and 1 MΩ), and all filter paths (enabled/disabled).
- Calibrates trigger level offset and gain.
- Calibrates trigger timing, as well as the time-to-digital conversion (TDC) circuitry to ensure 
accurate trigger timing and time-stamping.
- Compensates 1 MΩ input frequency flatness, then compensates input capacitance so that it 
is equal regardless of selected attenuator range.
- Takes approximately 2 minutes to complete.

Using the example as a comparison, the NI 5122/5124/5142, using self-calibration and a 5 V input, 
will have an error at 48 °C of

5 V(0.65% of input + 8 mV) = 40.5 mV error

This result compares favorably to the 180 mV 
error for a typical digitizer as described in the example without self-calibration.

#### When to Self-Calibrate

For optimum performance, use self-calibration when the digitizer is placed in a new system, 
any time the temperature changes more than 5 °C from 
the previous self-calibration, or 90 days after the previous self-calibration. The result is a 
product that yields full performance over its operating temperature range 
and two-year calibration cycle for DC accuracy, AC response, and trigger level/timing. When the two-year calibration interval expires, an external calibration
is required.

The NI 5122/5124/5142 has a temperature sensor that monitors temperature variations.
 The previous self-calibration time and date can also be read. Unless temperature variations are a 
 serious problem, self-calibration is not recommended more than once per day.

#### Input Connections During Self-Calibration

The NI 5122/5124/5142 internal circuitry is automatically isolated from the input during self-calibration. 
 
However, problems may occur if high-voltage, high-frequency signals (in excess of 500 V/µs slew rate) 
are present during self-calibration.

When in doubt, disconnect the inputs as directed. If you are absolutely certain that the maximum slew 
rate of the input signal is below 500 V/µs, then it is acceptable to leave the input signal connected during 
self-calibration.

#### Programming Flow

The following diagram shows the typical programming flow for self-calibration.

[IMAGE alt='1378' src='GUID-E9C48488-F5EB-4E81-A347-35C2CBB1C6D4-a5.svg']

NI-SCOPE provides the Calibrate example, which you can find by using the
 shortcut at Start»All Programs»National Instruments»NI-SCOPE»Examples.

#### Summary of Calibration Options

A summary of the calibration options available and when to use them is shown in the following table.

| Calibration | Impact | When | Notes |
| --- | --- | --- | --- |
| External calibration | Calibrate time drift of onboard reference | Every 2 years | Calibrates and verifies to full specifications |
| Self-calibration | Offset and gain Trigger level Trigger timing AC flatness Input capacitance | 90 days, or when temperature changes >5 °C | Ensures range to range matching Ensures trigger accuracy Optimizes performance with external 10:1 probes |
| No calibration | None, within 2 year calibration cycle or if temperature stays within ±5 C | High accuracy not required outside of 5 °C | If self-calibration is not used, derate the accuracy using the specified Tempco |

Parent topic:

NI 5124

Parent topic:

NI 5142

Related information:

- Calibration
- TDC

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-512251245142-input-ranges.html language=enus -->
## TOPIC 00019: NI 5122/5124/5142 Input Ranges

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-512251245142-input-ranges.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-512251245142-input-ranges.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: As shown in the following table, the 1 MΩ path allows up to 20 V[pk-pk] whereas the 50 Ω path is limited to 10 V[pk-pk]. 50 Ω Input Path 1 MΩ Input Path0.2 V[pk-pk] 0.2 V[pk-pk]0.4 V[pk-pk]0.4 V[pk-pk]1 V[pk-pk]1 V[pk-pk]2 V[pk-pk] 2 V[pk-pk]4 V[pk-pk]4 V[pk-pk]10 V[pk-pk] 10 V[pk-pk]—20 V[pk-pk]

NI 5122/5124/5142 Input Ranges

As shown in the following table, the 1 MΩ path 
allows up to 20 V<sub>pk-pk</sub> whereas the 50 Ω path is limited to 10 V<sub>pk-pk</sub>.

| 50 Ω Input Path | 1 MΩ Input Path |
| --- | --- |
| 0.2 Vpk-pk | 0.2 Vpk-pk |
| 0.4 Vpk-pk | 0.4 Vpk-pk |
| 1 Vpk-pk | 1 Vpk-pk |
| 2 Vpk-pk | 2 Vpk-pk |
| 4 Vpk-pk | 4 Vpk-pk |
| 10 Vpk-pk | 10 Vpk-pk |
| — | 20 Vpk-pk |

Note

Parent topic:

NI 5124 Input Signal Conditioning

Parent topic:

NI 5122/5142 Input Signal Conditioning

Related concepts:

- NI 5114/5122/5124/5142 Vertical Offset

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-5152-acdcgnd-coupling.html language=enus -->
## TOPIC 00020: NI 5152 AC/DC/GND Coupling

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-5152-acdcgnd-coupling.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-5152-acdcgnd-coupling.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can select AC, DC, or GND input coupling for the 1 MΩ input path or the 50 Ω input path. Select AC-coupling if the input signal has a DC component that you want to reject, provided that you are not concerned about low-frequency flatness. A DC input offset adjustment is available if the signal yo

NI 5152 AC/DC/GND Coupling

You can select AC, DC, or GND input coupling for the 1 MΩ input path or the 50 Ω input path. Select AC-coupling if the input signal has a DC component that you want to reject, 
provided that you are not concerned about low-frequency flatness. A DC 
input offset adjustment is available if the signal you want to measure is below this limit.

Ground coupling disconnects the input channel from the signal connected and internally connects the 
channel to ground to provide a ground reference.

Parent topic:

NI 5152 Input Signal Conditioning

Related information:

- Input Coupling

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-5152-input-impedance.html language=enus -->
## TOPIC 00021: NI 5152 Input Impedance

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-5152-input-impedance.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-5152-input-impedance.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can set the NI 5122/5124/5142/5152 analog input impedance to either 50 Ω or 1 MΩ. The 1 MΩ path is required in applications that require minimal loading or that require using a standard 10:1 oscilloscope probe.Protection The 50 Ω inputs of the NI 5152 are protected by a thermal disconnect circui

NI 5152 Input Impedance

You can set the NI 5122/5124/5142/5152 analog input impedance to either 50 Ω or 1 MΩ. The 1 MΩ path is required in applications that require minimal loading or 
that require using a standard 10:1 oscilloscope probe.

#### Protection

The 50 Ω inputs of the NI 5152 are protected by a thermal 
disconnect circuit. If an overvoltage event is large and sudden enough, however, the protection circuits 
might not have enough time to react before permanent damage occurs. It is therefore important 
that you observe the specified maximum signal
input levels, especially when the inputs are set for 50 Ω.

Parent topic:

NI 5152 Input Signal Conditioning

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-5152-input-ranges.html language=enus -->
## TOPIC 00022: NI 5152 Input Ranges

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-5152-input-ranges.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-5152-input-ranges.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5152 supports the following input ranges: 0.1, 0.2, 0.4, 1, 2, and 10 V[pk-pk]

NI 5152 Input Ranges

The NI 5152 supports the following input ranges: 0.1, 0.2, 0.4, 1, 2, and 10 V<sub>pk-pk</sub>

Parent topic:

NI 5152 Input Signal Conditioning

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-5152-input-signal-conditioning.html language=enus -->
## TOPIC 00023: NI 5152 Input Signal Conditioning

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-5152-input-signal-conditioning.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-5152-input-signal-conditioning.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5152 provides two independent digitizer input channel signal conditioning paths. Each path provides you with a choice of 50 Ω input impedance or 1 MΩ input impedance, as shown in the following diagram. The ground on the device inputs is connected to the chassis ground.

NI 5152 Input Signal Conditioning

The NI 5152 provides two independent digitizer input channel signal conditioning paths. Each path provides you
 with a choice of 50 Ω input impedance or 1 MΩ input impedance, as shown in the following diagram.

[IMAGE alt='1378' src='GUID-702323C3-9F0D-4697-9542-93B6979CCC7F-a5.svg']

Note

Parent topic:

NI 5152

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-5152-noise-filter.html language=enus -->
## TOPIC 00024: NI 5152 Noise Filter

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-5152-noise-filter.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-5152-noise-filter.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5152 provides a 20 MHz noise filter that limits the bandwidth of the signal path through both the 1 MΩ and 50 Ω signal paths. This filter is intended to reduce noise when the signal content is 20 MHz or less. Typical frequency responses of the NI 5152 are shown in the following figures.

NI 5152 Noise Filter

The NI 5152 provides a 20 MHz noise filter that limits the bandwidth 
of the signal path through both the 1 MΩ and 50 Ω signal paths.
 This filter is intended to reduce noise when the signal content is 20 MHz or less.

Typical frequency responses of the NI 5152 are shown in the following figures.

[IMAGE alt='1378' src='GUID-94CCABC0-F3E7-4412-B91F-0CD64E9478B1-a5.svg']

[IMAGE alt='1378' src='GUID-9E4E261A-2EAC-4BE5-B98B-BF98FEFBEB7D-a5.svg']

Parent topic:

NI 5152 Input Signal Conditioning

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-5152-vertical-offset.html language=enus -->
## TOPIC 00025: NI 5152 Vertical Offset

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-5152-vertical-offset.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-5152-vertical-offset.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table shows the valid vertical offset for each range on the NI 5152.Range50 Ω Vertical Offset1 MΩ Vertical Offset0.1 V[pk-pk]±1 V±1 V0.2 V[pk-pk]±1 V±1 V0.4 V[pk-pk]±1 V±1 V1 V[pk-pk]±1 V±1 V2 V[pk-pk]±6 V±10 V4 V[pk-pk]±5 V±10 V10 V[pk-pk]±2 V±10 V The maximum allowable DC voltage i

NI 5152 Vertical Offset

The following table shows the valid vertical offset for each range on the NI 5152.

| Range | 50 Ω Vertical Offset | 1 MΩ Vertical Offset |
| --- | --- | --- |
| 0.1 Vpk-pk | ±1 V | ±1 V |
| 0.2 Vpk-pk | ±1 V | ±1 V |
| 0.4 Vpk-pk | ±1 V | ±1 V |
| 1 Vpk-pk | ±1 V | ±1 V |
| 2 Vpk-pk | ±6 V | ±10 V |
| 4 Vpk-pk | ±5 V | ±10 V |
| 10 Vpk-pk | ±2 V | ±10 V |

Note

Parent topic:

NI 5152 Input Signal Conditioning

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-5152.html language=enus -->
## TOPIC 00026: NI 5152

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-5152.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-5152.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: Features The NI 5152 has the following features: 2 channels, simultaneously sampled 8-bit vertical resolution 1 GS/s real-time sampling rate, 2 GS/s time interleaved sampling rate 300 MHz bandwidth PXI or PCI versions 8 MB, 64 MB, or 256 MB of memory per channel NI-TClk synchronization

NI 5152

#### Features

The NI 5152 has the following features:

- 2 channels, simultaneously sampled
- 8-bit vertical resolution
- 1 GS/s real-time sampling rate, 2 GS/s time interleaved sampling rate
- 300 MHz bandwidth
- PXI or PCI versions
- 8 MB, 64 MB, or 256 MB of memory per channel
- NI-TClk synchronization

Related concepts:

- SMC-Based Device Synchronization
- Features Supported by NI-SCOPE Instruments

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-515251535154-calibration.html language=enus -->
## TOPIC 00027: NI 5152/5153/5154 Calibration

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-515251535154-calibration.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-515251535154-calibration.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: Every measurement instrument performs within its specifications over some finite temperature range and time period. If the temperature changes and time exceed those specified, and your application requires tight specifications, calibration is required. For example, if the accuracy of a digitizer is

NI 5152/5153/5154 Calibration

Every measurement instrument performs within its specifications over some finite temperature range and time period. 
 If the temperature changes and time exceed those specified, and your application requires tight specifications, 
 calibration
 is required.

For example, if the accuracy of a digitizer is specified as ±(1% of input + 10 mV), and you apply 5 V to the input, the error is:

1% of 5 V + 10 mV = 60 mV 
for temperature range 18-28 °C

This example demonstrates the traditional method of specifying accuracy. 
The problem with the traditional method is that in a system environment, temperature is 
not easily controlled. When a system is composed of multiple integrated instruments, the system is subject to temperature rise caused by inherent compromises in air circulation and 
other 
factors. Self-heating from surrounding equipment, uncontrolled manufacturing floor environment, and dirty 
fan filters are among these factors.

If the ambient temperature is outside of the 18-28 °C range, you may need to know exactly what the 
measurement accuracy is to compensate for this temperature variation. With the traditional method,
the only way to get the specified accuracy outside of the 18-28 °C range is to externally calibrate 
the 
system at the desired temperature. However, an external calibration is time-consuming and expensive and is 
infrequently done, so the specified accuracy is rarely obtained. You can learn more about external calibration at ni.com/calibration.
In the example, if the ambient temperature of the digitizer is 48 °C, assuming the Tempco 
(TC) error is specified as

TC = (0.1% of input +1 mV)/ °C (a typical number is 10% of accuracy/ °C)

The additional error is

20 °C x TC = ±(2% of input + 20 mV) or 120 mV

The total error is three times the specified error (180 mV in the example above, 
versus 60 mV if 
temperature effect is ignored) due to the 48 °C ambient temperature.

#### Self-Calibration

To eliminate errors caused by changing temperatures, NI-SCOPE provides a highly repeatable self-calibration
 
 function.

For the NI 5152/5153/5154, this self-calibration capability yields the following benefits:

- Corrects for DC gain and offset errors within the digitizer by comparison to a precision, 
high-stability internal voltage reference. This is done for all ranges 
 and all filter paths (enabled/disabled).
- (NI 5152) Calibrates trigger timing to ensure accurate trigger timing and time-stamping.
- Takes approximately 2-3 minutes (NI 5152) or 5 minutes (NI 5153/5154) to complete.

#### When to Self-Calibrate

For optimum performance, use self-calibration when the digitizer is placed in a new system, 
any time the temperature changes more than 5 °C from 
the previous self-calibration, or 90 days after the previous self-calibration. The result is a 
product that yields full performance over its operating temperature range 
and two-year calibration cycle for DC accuracy, AC response, and trigger level/timing. When the two-year calibration interval expires, an external calibration
is required.

The NI 5152/5153/5154 has a temperature sensor that monitors temperature variations.
 The previous self-calibration time and date can also be read. Unless temperature variations are a 
 serious problem, self-calibration is not recommended more than once per day.

#### Input Connections During Self-Calibration

The NI 5152/5153/5154 internal circuitry is automatically isolated from the input during self-calibration. 
 
However, problems may occur if high-voltage, high-frequency signals (in excess of 500 V/µs slew rate) 
are present during self-calibration.

When in doubt, disconnect the inputs as directed. If you are absolutely certain that the maximum slew 
rate of the input signal is below 500 V/µs, then it is acceptable to leave the input signal connected during 
self-calibration.

#### Programming Flow

The following diagram shows the typical programming flow for self-calibration.

[IMAGE alt='1378' src='GUID-E9C48488-F5EB-4E81-A347-35C2CBB1C6D4-a5.svg']

NI-SCOPE provides the Calibrate example, which you can find by using the
 shortcut at Start»All Programs»National Instruments»NI-SCOPE»Examples.

#### Summary of Calibration Options

A summary of the calibration options available and when to use them is shown in the following table.

| Calibration | Impact | When | Notes |
| --- | --- | --- | --- |
| External calibration | Calibrate time drift of onboard reference and TRIG channel | Every 2 years | Calibrates and verifies to full specifications |
| Self-calibration | Offset and gainTrigger timingTrigger level | 90 days, or when temperature changes >5 °C | Ensures range to range matchingEnsures trigger accuracy |
| No calibration | None, within 2 year calibration cycle or if temperature stays within ±5 C | High accuracy not required outside of 5 °C | If self-calibration is not used, derate the accuracy using the specified Tempco |

Parent topic:

NI 5152

Parent topic:

NI 5153/5154

Related information:

- Calibration

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-51535154-acdc-coupling.html language=enus -->
## TOPIC 00028: NI 5153/5154 AC/DC Coupling

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-51535154-acdc-coupling.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-51535154-acdc-coupling.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can select AC, DC, or GND input coupling for the 50 Ω input path. Select AC-coupling if the input signal has a DC component that you want to reject, provided that you are not concerned about low-frequency flatness. A DC input offset adjustment is available if the signal you want to measure is be

NI 5153/5154 AC/DC Coupling

You can select AC, DC, or GND input coupling for the 50 Ω input path. Select AC-coupling if the input signal has a DC component that you want to reject, 
provided that you are not concerned about low-frequency flatness. A DC input offset adjustment is available if the signal you want to measure is below this limit.

Ground coupling disconnects the input channel from the signal connected and internally connects the channel to ground to provide a ground reference.

Parent topic:

NI 5153/5154 Input Signal Conditioning

Related information:

- Input Coupling

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-51535154-input-impedance.html language=enus -->
## TOPIC 00029: NI 5153/5154 Input Impedance

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-51535154-input-impedance.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-51535154-input-impedance.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5153/5154 has 50 Ω analog input impedance. Protection The 50 Ω input of the NI 5153/5154 is protected by a voltage sense circuit. If an overvoltage event is large and sudden enough, however, the protection circuits might not have enough time to react before permanent damage occurs. It is ther

NI 5153/5154 Input Impedance

The NI 5153/5154 has 50 Ω analog input impedance.

#### Protection

The 50 Ω input of the NI 5153/5154 is protected by a voltage sense circuit. If an overvoltage event is large and sudden enough, however, the protection circuits 
might not have enough time to react before permanent damage occurs. It is therefore important 
that you observe the specified maximum signal
input levels.

Parent topic:

NI 5153/5154 Input Signal Conditioning

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-51535154-input-ranges.html language=enus -->
## TOPIC 00030: NI 5153/5154 Input Ranges

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-51535154-input-ranges.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-51535154-input-ranges.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5153-5154 supports the following input ranges: 0.1, 0.2, 0.5, 1, 2, and 5 V[pk-pk]

NI 5153/5154 Input Ranges

The NI 5153-5154 supports the following input ranges: 0.1, 0.2, 0.5, 1, 2, and 5 V<sub>pk-pk</sub>

Parent topic:

NI 5153/5154 Input Signal Conditioning

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-51535154.html language=enus -->
## TOPIC 00031: NI 5153/5154

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-51535154.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-51535154.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: Features The NI 5153/5154 has the following features: 2 channels, simultaneously sampled 8-bit vertical resolution 1 GS/s real-time sampling rate, 2 GS/s time interleaved sampling rate Bandwidth NI 5153: 500 MHz NI 5154: 1 GHz PXI or PCI versions 8 MB, 64 MB, or 256 MB of memory per channel NI-TClk

NI 5153/5154

#### Features

The NI 5153/5154 has the following features:

- 2 channels, simultaneously sampled
- 8-bit vertical resolution
- 1 GS/s real-time sampling rate, 2 GS/s time interleaved sampling rate
- Bandwidth
  - NI 5153: 500 MHz
  - NI 5154: 1 GHz
- PXI or PCI versions
- 8 MB, 64 MB, or 256 MB of memory per channel
- NI-TClk synchronization

Related concepts:

- Features Supported by NI-SCOPE Instruments
- SMC-Based Device Synchronization
- NI 5142 Onboard Signal Processing (OSP)

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-51855186-input-impedance.html language=enus -->
## TOPIC 00032: NI 5185/5186 Input Impedance

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-51855186-input-impedance.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-51855186-input-impedance.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5185/5186 has 50 Ω and 1 MΩ input impedances.Some previous NI 5185/5186 devices do not support 1 MΩ inputs. For more information, refer to NI 5185/5186 Front Panels.

NI 5185/5186 Input Impedance

The NI 5185/5186 has 50 Ω and 1 MΩ input impedances.

Some previous NI 5185/5186 devices do not support 1 MΩ inputs. For more information, refer to NI 5185/5186 Front Panels.

Parent topic:

NI 5185/5186

Related concepts:

- NI 5185/5186 Front Panels

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-51855186-input-ranges.html language=enus -->
## TOPIC 00033: NI 5185/5186 Input Ranges

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-51855186-input-ranges.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-51855186-input-ranges.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5185/5186 supports the following input ranges: 50 Ω path: 110 mV[pp] to 1 V[pp] 1 MΩ path: 110 mV[pp] to 10 V[pp] Some previous NI 5185/5186 devices do not support 1 MΩ inputs. For more information, refer to NI 5185/5186 Front Panels.

NI 5185/5186 Input Ranges

The NI 5185/5186 supports the following input ranges:

- 50 Ω path : 110 mV pp to 1 V pp
- 1 MΩ path : 110 mV pp to 10 V pp

Some previous NI 5185/5186 devices do not support 1 MΩ inputs. For more information, refer to NI 5185/5186 Front Panels.

Parent topic:

NI 5185/5186

Related concepts:

- NI 5185/5186 Front Panels

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-51855186-input-signal-conditioning.html language=enus -->
## TOPIC 00034: NI 5185/5186 Input Signal Conditioning

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-51855186-input-signal-conditioning.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-51855186-input-signal-conditioning.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5185/5186 provides the following input channel signal conditioning path.Some previous NI 5185/5186 devices do not support 1 MΩ inputs. For more information, refer to NI 5185/5186 Front Panels. The ground on the device inputs is connected to the chassis ground. For information regarding safe

NI 5185/5186 Input Signal Conditioning

The NI 5185/5186 provides the following input channel signal conditioning path.

[IMAGE alt='1378' src='GUID-C0EB9A66-ECFD-4504-B936-102691A53F46-a5.svg']

Some previous NI 5185/5186 devices do not support 1 MΩ inputs. For more information, refer to NI 5185/5186 Front Panels.

Note

Parent topic:

NI 5185/5186

Related concepts:

- NI 5185/5186 Front Panels

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-51855186-routing-matrix.html language=enus -->
## TOPIC 00035: NI 5185/5186 Routing Matrix

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-51855186-routing-matrix.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-51855186-routing-matrix.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table shows the signals available for export from the NI 5185/5186. SourceDestination PXI_Trig <0..6>(PXI Bus) TriggersAcquisition Arm (Start) Trigger√ Reference (Stop) Trigger√EventsEnd of Record Event√End of Acquisition Event√Ready for Start Event√Ready for Reference Event√Ready for

NI 5185/5186 Routing Matrix

The following table shows the signals available for export from the NI 5185/5186.

| Source | Destination |
| --- | --- |
|  | PXI_Trig <0..6>(PXI Bus) |
| Triggers |  |
| Acquisition Arm (Start) Trigger | √ |
| Reference (Stop) Trigger | √ |
| Events |  |
| End of Record Event | √ |
| End of Acquisition Event | √ |
| Ready for Start Event | √ |
| Ready for Reference Event | √ |
| Ready for Advance Event | √ |

Note

Parent topic:

NI 5185/5186

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-51855186-timing-diagram.html language=enus -->
## TOPIC 00036: NI 5185/5186 Timing Diagram

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-51855186-timing-diagram.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-51855186-timing-diagram.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5185/5186 supports multirecord acquisitions, which allow the capture of multiple triggered waveforms without software intervention. In this mode, the digitizer automatically begins storing a new record to onboard memory a short time after finishing the previous record. The number of records a

NI 5185/5186 Timing Diagram

The NI 5185/5186 supports multirecord acquisitions, which allow the capture of multiple triggered waveforms
 without software intervention. In this mode, the digitizer automatically begins storing a new record to onboard 
 memory a short time after finishing the previous record. The number of records and record size are both 
 configurable.

The following timing diagram illustrates how the NI 5185/5186 reacts to the user-configurable 
 input triggers during a multirecord acquisition.

[IMAGE alt='1378' src='GUID-B97DA5FF-B94F-4428-B135-9D24A0CE2987-a5.svg']

Each state prefixed by Wait for is a 
state in 
 which an input trigger can be configured. This trigger 
 tells the digitizer when to transition out of that particular state. If an input trigger is not explicitly configured, the device will default to transition immediately into 
 the next state. For more information, refer to the SMC-Based Digitizers 
 Acquisition Engine State Diagram. The digitizer is only able to detect a 
 particular trigger when in that trigger's appropriate Wait for state. For example, the 
 digitizer is not sensitive to a high level on the Advance Trigger until it enters the 
 Wait for the Advance 
 trigger state.
 Triggers in states that are not prefixed by Wait for are generated by the digitizer, and can
 be exported.

Note

The exportable events are also shown in the timing diagram. The End of Record Event is 
generated once per record when the digitizer has acquired all of its pre- and post-Reference Trigger samples. 
 This signal can be used for handshaking between devices in a system. The Done Event asserts when all of the 
 records have been completed, but it does not assert if the acquisition is aborted 
 or times out.

Parent topic:

NI 5185/5186

Related concepts:

- NI 5185/5186 Acquisition Engine State Diagram

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-51855186-trigger-delay.html language=enus -->
## TOPIC 00037: NI 5185/5186 Trigger Delay

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-51855186-trigger-delay.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-51855186-trigger-delay.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger delay, which is specified in seconds, is achieved by adding the appropriate number of posttrigger samples to the record while keeping the allocated onboard memory equal to the record size you request. The maximum trigger delay for the NI 5185/5186 is 1,300,000 seconds.

NI 5185/5186 Trigger Delay

Trigger delay, which is specified in seconds, is achieved by adding the 
appropriate number of posttrigger samples to the record while keeping the allocated onboard
 memory equal to the record size you request. The maximum trigger delay for the NI 5185/5186 is 1,300,000 seconds.

Parent topic:

NI 5185/5186 Trigger Types

Related information:

- Trigger Delay

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-51855186-trigger-holdoff.html language=enus -->
## TOPIC 00038: NI 5185/5186 Trigger Holdoff

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-51855186-trigger-holdoff.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-51855186-trigger-holdoff.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5185/5186 has a maximum trigger holdoff of 10.99 s.

NI 5185/5186 Trigger Holdoff

The NI 5185/5186 has a maximum trigger holdoff of 10.99 s.

Parent topic:

NI 5185/5186 Trigger Types

Related information:

- Trigger Holdoff

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-5622-onboard-signal-processing-osp.html language=enus -->
## TOPIC 00039: NI 5622 Onboard Signal Processing (OSP)

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-5622-onboard-signal-processing-osp.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-5622-onboard-signal-processing-osp.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5622 onboard signal processing (OSP) block is a general-purpose block of digital signal processing components. The following figure shows the main components found in the OSP block of the NI 5622. Click each area for more information about the main components of the OSP block.

NI 5622 Onboard Signal Processing (OSP)

The NI 5622 onboard signal processing (OSP) block is a 
general-purpose block of digital signal processing components.

The following figure shows the main components found in the OSP block of the NI 5622.

Click each area for more information about the main components of the OSP block.

[IMAGE alt='1378' src='GUID-68B721FA-2250-4485-9312-79C804ADE8D5-a5.svg']

Parent topic:

NI 5622

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-5622-signal-conditioning.html language=enus -->
## TOPIC 00040: NI 5622 Signal Conditioning

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-5622-signal-conditioning.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-5622-signal-conditioning.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5622 provides two input signal conditioning paths, one filtered and one unfiltered. The IF filtered path, shown in the upper signal conditioning path, has a bandwidth of 50 MHz centered at 187 MHz. This path can be used with NI 5663 vector signal analyzer applications, or other applications r

NI 5622 Signal Conditioning

The NI 5622 provides two input signal conditioning paths, one filtered and one unfiltered.

[IMAGE alt='1378' src='GUID-0C609B91-E0AC-486C-A6C5-5B46227C3974-a5.svg']

The IF filtered path, shown in the upper signal conditioning path, has a bandwidth of 50 MHz centered at 187 MHz. This 
path can be used with NI 5663 vector 
signal analyzer applications, or other applications requiring alias-protected sampling in 
the third Nyquist zone for the 150 MS/s ADC. The third Nyquist zone is 150 MHz to 225 MHz. To enable the IF filtered path, set the Bandpass Filter Enabled property to TRUE.

The direct path, shown in the lower signal conditioning path, has a frequency range of 3 to 250 MHz. This path can be used 
in digitizer-only applications. When the direct path (unfiltered) is selected, 
you should perform antialias filtering, external to the digitizer, depending on the spectral content of the signal being digitized.

Note

#### Related Information

Bandpass Filter Enabled Property

Parent topic:

NI 5622

Related information:

- NI-SCOPE LabVIEW VIs

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-5622-trigger-holdoff.html language=enus -->
## TOPIC 00041: NI 5622 Trigger Holdoff

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-5622-trigger-holdoff.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-5622-trigger-holdoff.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: For the NI 5622, the holdoff timer is started by the Reference Trigger. When the current record finishes and the minimum number of pretrigger samples for the next record have been acquired, the holdoff timer is evaluated. If the timer has expired, the digitizer arms its Reference Trigger circuit. If

NI 5622 Trigger Holdoff

For the NI 5622, the holdoff timer is started by the Reference Trigger. 
 When the current record finishes and the minimum number of pretrigger samples for the next record 
 have been acquired, the holdoff timer is evaluated. 
 
 If the timer has expired, the digitizer arms its Reference Trigger circuit. If the timer has not expired,
 the digitizer continues pretrigger 
 sampling until the timer expires, and then arms its Reference Trigger circuit. Holdoff is 
 applied for each Reference Trigger during a multirecord acquisition.

Parent topic:

NI 5622 Trigger Types

Related information:

- Trigger Holdoff

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-5622-trigger-types.html language=enus -->
## TOPIC 00042: NI 5622 Trigger Types

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-5622-trigger-types.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-5622-trigger-types.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 5622 supports only digital triggers.

NI 5622 Trigger Types

The NI 5622 supports only digital triggers.

Parent topic:

NI 5622

Related information:

- Digital Triggers

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-pci-511451225124--trigger-sources.html language=enus -->
## TOPIC 00043: NI PCI-5114/5122/5124 Trigger Sources

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-pci-511451225124--trigger-sources.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-pci-511451225124--trigger-sources.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the trigger sources for the NI PCI-5114/5122/5124.

NI PCI-5114/5122/5124 Trigger Sources

The following figure shows the trigger sources for the NI PCI-5114/5122/5124.

[IMAGE alt='1378' src='GUID-D99EF62A-7DE4-4025-84B9-F1C692552623-a5.svg']

Parent topic:

NI 5114/5122/5124/5142 Analog Trigger Types

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-pci-512251245142-routing-matrix.html language=enus -->
## TOPIC 00044: NI PCI-5122/5124/5142 Routing Matrix

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-pci-512251245142-routing-matrix.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-pci-512251245142-routing-matrix.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table shows the signals available for export from the NI PCI-5122/5124/5142, and the lines to which they can be routed. Source Destination RTSI <0..6>(RTSI Bus) CLK OUT(SMB) PFI <0..1>(AUX I/O) RTSI 7 Exported Clocks Reference Clock (External) — √ √ — Reference Clock (Internal) — √ √ √

NI PCI-5122/5124/5142 Routing Matrix

The following table shows the signals available for export from the NI PCI-5122/5124/5142, and the lines to which they can be routed.

| Source | Destination |  |  |  |
| --- | --- | --- | --- | --- |
|  | RTSI <0..6>(RTSI Bus) | CLK OUT(SMB) | PFI <0..1>(AUX I/O) | RTSI 7 |
| Exported Clocks |  |  |  |  |
| Reference Clock (External) | — | √ | √ | — |
| Reference Clock (Internal) | — | √ | √ | √ |
| Sample Clock (Full Rate) | — | √ | — | — |
| Sample Clock (Decimated Rate) | √ | √ | √ | — |
| Triggers |  |  |  |  |
| Acquisition Arm (Start) Trigger | √ | — | √ | — |
| Reference (Stop) Trigger | √ | — | √ | — |
| Events |  |  |  |  |
| End of Record Event | √ | — | √ | — |
| End of Acquisition Event | √ | — | √ | — |
| Ready for Start Event | √ | — | √ | — |
| Ready for Reference Event | √ | — | √ | — |
| Ready for Advance Event | √ | — | √ | — |

Parent topic:

NI 5124

Parent topic:

NI 5142

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-pci-51225142-clocking.html language=enus -->
## TOPIC 00045: NI PCI-5122/5142 Clocking

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-pci-51225142-clocking.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-pci-51225142-clocking.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The clock circuitry on the NI PCI-5122/5142 offers versatile clocking options with its ability to use either the internal 100 MHz sample clock or to accept an external sample clock that you provide. You can also use the phase-locked loop (PLL) circuit on the NI PCI-5122/5142 to phase lock the intern

NI PCI-5122/5142 Clocking

The clock circuitry on the NI PCI-5122/5142 offers versatile clocking options with its ability to use either 
the internal 100 MHz sample clock or to accept an external sample clock that you provide. You can also use the phase-locked loop (PLL)
 circuit 
on the NI PCI-5122/5142 to phase lock the internal 100 MHz sample clock with the internal 10 MHz reference, a reference 
clock from another module on RTSI 7 (RTSI Clock), or with an external reference clock that you provide. The following diagram 
shows the clocking options of the NI PCI-5122/5142.

[IMAGE alt='1378' src='GUID-8A87AA40-F5FA-41C1-AB5F-37E78FE30A8E-a5.svg']

#### Sample Clock

The sample clock is sent to the ADC of each channel and to the input timing engine. The NI PCI-5122/5142 can decimate its sample 
clock (internal or external) by an integer divisor. When using an external clock, you can use decimation to achieve rates below the 
external clock frequency.

#### Internal Sample Clock

The NI PCI-5122/5142 has an onboard voltage controlled crystal oscillator (VCXO) running at 100 MHz. When using the onboard 100 MHz 
oscillator, you can choose either free-run mode or PLL mode. In free-run mode, the sample clock is the calibrated 100 MHz 
frequency of the VCXO. In PLL mode, the NI PCI-5122/5142 phase locks its 100 MHz sample clock to the supplied reference clock. 
The PLL mode is useful when synchronizing the NI PCI-5122/5142 with other devices in a measurement system.

#### External Sample Clock

Some applications may require sampling at specific intervals that cannot be achieved by using the internal 100 MHz clock. 
In these cases the NI PCI-5122/5142 can accept an external sample clock. External clocking also provides a method to synchronize 
the NI PCI-5122/5142 to other devices in a measurement system by distributing a common clock to multiple devices. An external sample 
clock can be supplied to the NI PCI-5122/5142 from the front panel connector. Refer to the specifications document for your device 
 for external sample clock requirements.

Note

#### Reference Clock

The reference clock is used in the NI PCI-5122/5142 PLL circuit to synchronize the sample clock to the reference clock. The 
NI PCI-5122/5142 can accept a reference clock from its front panel (CLK IN) as well as from RTSI 7 (RTSI Clock) on the RTSI bus
or the internal 10 MHz reference clock. This reference clock can be any frequency from 5 MHz to 20 MHz if it is
provided to CLK IN or to RTSI 7. The internal reference clock is always a 10 MHz clock. The frequency stability of the sample clock matches 
that of the PLL reference clock when the two are phase locked. In turn, phase locking synchronizes clocks of multiple devices that 
are phase locked to the same reference clock. The default setting for the NI PCI-5122/5142 reference clock is None, or not to use a 
reference clock.

Note

#### Exporting Sample Clock

To achieve sampling rates other than 100 MS/s when using the internal sample clock, 
the NI PCI-5122/5142 decimates the sampled data. 
When you set a sampling rate of 50 MS/s, the NI PCI-5122/5142 only stores one out of every two samples it receives from the 
ADCs to onboard memory. The NI PCI-5122/5142 can sample at rates of 100/n MS/s,
 where n is an integer value 
between 1 and (2<sup>16</sup>). Because the NI PCI-5122/5142 does not change the
 frequency of the clock sent to the ADCs, it creates a 
sample clock for export based on the effective sampling rate that you have configured. 
When sampling at the maximum rate, a 
free-running version of the actual sample clock is exported to the front panel of the 
NI PCI-5122/5142. When the data is being 
decimated, a divided down version of the sample clock is exported. The divided down version 
of the sample clock only toggles while 
data is being acquired, and is driven low after the acquisition completes.

#### Exporting Reference Clock

If you are using the internal reference clock you can export that same reference clock to other NI PCI-5122/5142 devices for
synchronization purposes. For more information, refer to the section on synchronization.
If you are using a reference clock to phase lock the internal sample clock, you can export the reference clock for use with other 
instruments. For more information on exporting the reference clock, refer to the NI PCI-5122/5124/5142 Routing Matrix.

Parent topic:

NI 5142

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-pci-5124-block-diagram.html language=enus -->
## TOPIC 00046: NI PCI-5124 Block Diagram

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-pci-5124-block-diagram.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-pci-5124-block-diagram.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows a detailed block diagram of the NI PCI-5124.

NI PCI-5124 Block Diagram

The following figure shows a detailed block diagram of the NI PCI-5124.

[IMAGE alt='1378' src='GUID-AD9BA149-6E62-476F-8B29-BE885840C3F6-a5.svg']

Parent topic:

NI 5124

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-pci-5152-block-diagram.html language=enus -->
## TOPIC 00047: NI PCI-5152 Block Diagram

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-pci-5152-block-diagram.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-pci-5152-block-diagram.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows a detailed block diagram of the NI PCI-5152. The dual ADC architecture enables the Time Interleaved Sampling (TIS) feature of these digitizers.

NI PCI-5152 Block Diagram

The following figure shows a detailed block diagram of the NI PCI-5152. The dual ADC architecture 
 enables the Time Interleaved Sampling (TIS) feature of these digitizers.

[IMAGE alt='1378' src='GUID-141E1B54-8486-4B01-8ACF-13020D45D210-a5.svg']

Parent topic:

NI 5152

Related information:

- Time Interleaved Sampling

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-pci-515251535154-routing-matrix.html language=enus -->
## TOPIC 00048: NI PCI-5152/5153/5154 Routing Matrix

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-pci-515251535154-routing-matrix.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-pci-515251535154-routing-matrix.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table shows the signals available for export from the NI PCI-5152/5153/5154 and the lines to which they can be routed. Source Destination RTSI <0..6> (RTSI Bus) PFI 0 PFI 1 RTSI 7 Exported Clocks Reference Clock (External) √ — √ — Reference Clock (Internal) — √ √ √ Triggers Acquisition

NI PCI-5152/5153/5154 Routing Matrix

The following table shows the signals available for export from the NI PCI-5152/5153/5154 and the
 lines to which they can be routed.

| Source | Destination |  |  |  |
| --- | --- | --- | --- | --- |
|  | RTSI <0..6> (RTSI Bus) | PFI 0 | PFI 1 | RTSI 7 |
| Exported Clocks |  |  |  |  |
| Reference Clock (External) | √ | — | √ | — |
| Reference Clock (Internal) | — | √ | √ | √ |
| Triggers |  |  |  |  |
| Acquisition Arm (Start) Trigger | √ | √ | √ | — |
| Reference (Stop) Trigger | √ | √ | √ | — |
| Events |  |  |  |  |
| End of Record Event | √ | √ | √ | — |
| End of Acquisition Event | √ | √ | √ | — |
| Ready for Start Event | √ | √ | √ | — |
| Ready for Reference Event | √ | √ | √ | — |
| Ready for Advance Event | √ | √ | √ | — |

Parent topic:

NI 5152

Parent topic:

NI 5153/5154

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-pci-515251535154-trigger-sources.html language=enus -->
## TOPIC 00049: NI PCI-5152/5153/5154 Trigger Sources

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-pci-515251535154-trigger-sources.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-pci-515251535154-trigger-sources.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the trigger sources for the NI PCI-5152/5153/5154.

NI PCI-5152/5153/5154 Trigger Sources

The following figure shows the trigger sources for the NI PCI-5152/5153/5154.

[IMAGE alt='1378' src='GUID-E387C14B-5E01-41AC-9938-E6F0CD7DEC80-a5.svg']

Parent topic:

NI 5152

Parent topic:

NI 5153/5154

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=ni-pci-51535154-block-diagram.html language=enus -->
## TOPIC 00050: NI PCI-5153/5154 Block Diagram

- bundle_id: `legacy-scope-hardware-features`
- source_path: `ni-pci-51535154-block-diagram.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/ni-pci-51535154-block-diagram.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows a detailed block diagram of the NI PCI-5153/5154. The dual ADC architecture enables the Time Interleaved Sampling (TIS) feature of these digitizers.

NI PCI-5153/5154 Block Diagram

The following figure shows a detailed block diagram of the NI PCI-5153/5154. The dual ADC architecture 
 enables the Time Interleaved Sampling (TIS) feature of these digitizers.

[IMAGE alt='1378' src='GUID-6720FE47-5DB5-473A-B6B6-3941703D9456-a5.svg']

Parent topic:

NI 5153/5154

Related information:

- Time Interleaved Sampling

<!--NI_TOPIC bundle=legacy-scope-hardware-features path=smc-based-digitizers-acquisition-engine-state.html language=enus -->
## TOPIC 00051: SMC-Based Digitizers Acquisition Engine State Diagram

- bundle_id: `legacy-scope-hardware-features`
- source_path: `smc-based-digitizers-acquisition-engine-state.html`
- source_url: https://docs-be.ni.com/bundle/legacy-scope-hardware-features/raw/resource/enus/smc-based-digitizers-acquisition-engine-state.html
- document_id: `legacy-scope-hardware-features`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the acquisition engine state diagram for SMC-Based digitizers. The Reference (Stop) Trigger is the same as the trigger level input of any traditional benchtop oscilloscope. To configure a digitizer to behave as a traditional benchtop oscilloscope, configure only this tri

SMC-Based Digitizers Acquisition Engine State Diagram

The following figure shows the acquisition engine state diagram for SMC-Based digitizers.

[IMAGE alt='1378' src='GUID-FF763564-2E5B-4F13-AF9A-624254EF5681-a5.svg']

Note

Reference
 (Stop) Trigger

niScope Configure Trigger

| Arrow Color | Indication |
| --- | --- |
| Blue | State transitions always caused by software |
| Black | State transitions caused by the internal state machine of the device |
| Red | Output signals |
| Orange | User-configurable state transitions caused by software or hardware |

NI SMC-based digitizers can be in any of the following basic states during the course of
 operation.

Idle—The module is not sampling a waveform. All the session attributes can
 be programmed in this state. In this state, the attributes have not necessarily been applied to
 hardware yet, so the hardware configuration of the module may not match the session attribute
 values. Also, the module remains configured as it was the last time a session was committed. When
 initiate is called on the module, all the attributes are programmed to the hardware. If the
 computer has just been reset, or niScope_ResetDevice has just been called, the
 module is in the Idle state.

Wait for Start Trigger—On initiating an acquisition, the module
 transitions to this state. If the Start (Acquisition Arm) Trigger Source is configured to
 Immediate, the module immediately transitions out of this state and generates a Start Trigger
 Event. If the Start Trigger Source has been configured for software or hardware trigger from one
 of the available sources, the module remains in this state until the configured trigger occurs.
 When the module recognizes a trigger condition, it transitions out of this state on the next
 clock cycle and generates a Start Trigger Event. The default Start Trigger Source is
 Immediate.

Minimum Pre-Reference Trigger Sampling—The module can transition into
 this state two ways: receiving the Start (Acquisition Arm) Trigger from the Start (Acquisition
 Arm) Trigger Source or receiving the Advance Trigger from the Advance Trigger Source.
 Transitioning into this state depends on the previous state of the module. While in this state,
 the module samples according to the session attributes configured. The module remains in this
 state until three conditions are satisfied: the minimum Pre-Reference Trigger sampling completes,
 the TDC is ready, and the trigger-to-trigger holdoff count has expired. The minimum Pre-Reference
 Trigger sampling is at least the user-configured Minimum Record Length multiplied by the
 user-configured Reference Position. The first time through this state, the trigger-to-trigger
 holdoff does not have an effect. When the three conditions have been satisfied, the module
 transitions out of this state on the next clock cycle.

Wait for Arm Reference Trigger while Sampling—After the module finishes
 the Minimum Pre-Reference Trigger Sampling state, the module transitions into this state. While
 in this state, the module continues to acquire Pre-Reference Trigger samples according to the
 session attributes configured. If the Arm Reference Trigger Source is configured to Immediate,
 the module transitions out of this state on the next clock edge. If the Arm Reference Trigger
 Source has been configured for a software trigger or a hardware trigger from one of the available
 sources, the module remains in this state until the configured trigger occurs. When the module
 recognizes a trigger condition, the module transitions out of this state. The default Arm
 Reference Trigger Source is Immediate.

Wait for Reference Trigger while Sampling—After the module receives Arm
 Reference Trigger from the Arm Reference Trigger Source, the module transitions into this state.
 If the Reference Trigger Source has been configured for a software or hardware trigger from one
 of the available sources, the module remains in this state until the configured trigger occurs.
 When the module recognizes a trigger condition, the module transitions out of this state. The
 default Reference Trigger Source is Immediate.

Post-Reference Trigger Sampling—After the module receives the Reference
 (Stop) Trigger, the module transitions into this state. At the beginning of this state, the
 module starts a trigger-to-trigger holdoff counter. This holdoff counter corresponds to the
 user-configurable Trigger Holdoff attribute and is used in the Minimum
 Pre-Reference Trigger Sampling State. You can use the Trigger Holdoff
 attribute to delay the module from looking for a Reference Trigger between records. At the same
 time, the trigger-to-trigger holdoff counter is started, the module begins sampling
 Post-Reference Trigger samples according to the session attributes configured. When the
 Post-Reference Trigger sampling is completed, the module transitions out of this state.

Record Complete—After the module completes Post-Reference Trigger
 sampling, the module transitions into this state. The module leaves this state after the current
 record has been stored in the onboard memory. Upon leaving this state, the module outputs an End
 of Record Event.

Wait for Advance Trigger—After the module has completed a record and
 determines that there are still more records to complete, the module transitions into this state.
 If the Advance Trigger Source is configured to immediate, the module transitions out of this
 state on the next clock edge. If the Advance Trigger Source has been configured for software or
 hardware trigger from one of the available sources, the module remains in this state until the
 configured trigger occurs. Upon the module recognizing a trigger condition, the module
 transitions out of this state. The default Advance Trigger Source is Immediate.

Done—After the module completes a record and determines that all the
 records are done, it transitions into this state. Upon entering this state, the module outputs
 the End of Acquisition Event, which is a temporary state. The software transitions the module out
 of this state and back to the Idle state when you call either Fetch or Check Status.

Parent topic:

NI 5124

Parent topic:

NI 5142

Parent topic:

NI 5622

Related information:

- TDC
- Triggering
- Trigger Types
- NI-SCOPE LabVIEW VIs
