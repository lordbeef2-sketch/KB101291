# NI DOCUMENT BUNDLE: ni-usrp-lvnxg-prop-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-usrp-lvnxg-prop-api-ref start=1 end=43 -->
<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=active-channel.html language=enus -->
## TOPIC 00001: Active Channel

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `active-channel.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/active-channel.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the channel name used to access all subsequent properties in this instance of the property node. If the property you want to use is channel-based, you must first select this property and then pass the name of the specific channel. If the property you specify is not channel-based, or you wa

Active Channel

Specifies the channel name used to access all subsequent properties in this instance of the property node. If the property you want to use is channel-based, you must first select this property and then pass the name of the specific channel. If the property you specify is not channel-based, or you want to set the property on all channels, pass an empty string or omit setting this property.

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

| Channel-based | No |
| --- | --- |
| Resettable | No |

#### Specifying Channels

Enter 
 0 for the first channel and 
 1 for the second channel. The order of the IP addresses sets the channel order.

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=ni-usrp.html language=enus -->
## TOPIC 00002: NI-USRP

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `ni-usrp.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/ni-usrp.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the properties in the NI-USRP class to access advanced configuration options for NI-USRP driver applications.

NI-USRP

Use the properties in the NI-USRP class to access advanced configuration options for NI-USRP driver applications.

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-active-antenna-00118c37.html language=enus -->
## TOPIC 00003: Active Antenna

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-active-antenna-00118c37.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-active-antenna-00118c37.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the antenna port to use for this channel. Hardware Support This property supports the following hardware: USRP-2900/2901 USRP-2920/2921/2922 USRP-2930/2932 USRP-2940/2942/2943/2944/2945 USRP-2950/2952/2953/2954/2955 Channel-based Yes Resettable Yes Antenna Names Antenna Names USRP Device C

Active Antenna

Specifies the antenna port to use for this channel.

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Channel-based | Yes |
| --- | --- |
| Resettable | Yes |

#### Antenna Names

| USRP Device | Connector Name | PCB (Internal) Name |
| --- | --- | --- |
| USRP-2900/2901/2920/2922/2930/2932 | TX1, RX1 | TX/RX |
| RX2 | RX2 |  |
| USRP-2921 | RX1, TX1 | J1 |
| RX2, TX2 | J2 |  |
| USRP-2940/2942/2943/2944/2950/2952/2953/2954/2974 | TX1, RX1 | TX/RX |
| RX2 | RX2 |  |
| USRP-2945/2955 | RX1 | RX |
| RX2 | RX2 |  |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-bandwidth-00118c35.html language=enus -->
## TOPIC 00004: Bandwidth

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-bandwidth-00118c35.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-bandwidth-00118c35.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth, in Hz, of the analog filter used in the RF front-end. This property sets an upper limit to the maximum bandwidth that the device can acquire or generate. Refer to your device specifications for more information about available bandwidth options. Hardware Support This propert

Bandwidth

Specifies the bandwidth, in Hz, of the analog filter used in the RF front-end.

This property sets an upper limit to the maximum bandwidth that the device can acquire or generate. Refer to your device specifications for more information about available bandwidth options.

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Channel-based | Yes |
| --- | --- |
| Resettable | Yes |

#### Range of Valid Values

The range of available values is hardware dependent. If you specify a value outside the range supported by your device, NI-USRP coerces the value to the nearest supported value. Writing to this property specifies the value you want to use. Reading from this property returns the actual value, which may have been coerced to the capabilities of the device. NI recommends that you read the value after you write to this property to determine the actual setting for the device.

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-carrier-frequency-00118c34.html language=enus -->
## TOPIC 00005: Carrier Frequency

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-carrier-frequency-00118c34.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-carrier-frequency-00118c34.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the carrier frequency, in Hz, of the RF signal. Hardware Support This property supports the following hardware: USRP-2900/2901 USRP-2920/2921/2922 USRP-2930/2932 USRP-2940/2942/2943/2944/2945 USRP-2950/2952/2953/2954/2955 Channel-based Yes Resettable Yes Carrier Frequency Behavior with Har

Carrier Frequency

Specifies the carrier frequency, in Hz, of the RF signal.

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Channel-based | Yes |
| --- | --- |
| Resettable | Yes |

#### Carrier Frequency Behavior with Hardware

The overall carrier frequency is realized in hardware as a combination of frequency translation in the local oscillator (LO) and additional frequency translation implemented in the digital signal processing on the FPGA. To set the LO to a specific frequency, set the 
 [LO Frequency](niusrp-lo-frequency-00118c3e.html) property.

The range of available values is hardware dependent. If you specify a value outside the range supported by your device, NI-USRP coerces the value to the nearest supported value. Writing to this property specifies the value you want to use. Reading from this property returns the actual value, which may have been coerced to the capabilities of the device. NI recommends that you read the value after you write to this property to determine the actual setting for the device.

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-coerced-lo-frequency-00118c45.html language=enus -->
## TOPIC 00006: Coerced LO Frequency

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-coerced-lo-frequency-00118c45.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-coerced-lo-frequency-00118c45.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads back the coerced local oscillator (LO) frequency, in Hz. Hardware Support This property supports the following hardware: USRP-2900/2901 USRP-2920/2921/2922 USRP-2930/2932 USRP-2940/2942/2943/2944/2945 USRP-2950/2952/2953/2954/2955 Default value: -1 Channel-based No Resettable Yes Consideration

Coerced LO
 Frequency

Reads back the coerced local oscillator (LO) frequency, in Hz.

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

Default value: -1

| Channel-based | No |
| --- | --- |
| Resettable | Yes |

#### Considerations for Specifying Carrier
 Frequency and LO Frequency

The overall carrier frequency is realized in hardware as a combination of frequency
 translation in the local oscillator (LO) and an additional frequency translation
 implemented in the digital signal processing on the FPGA. You can allow NI-USRP to
 automatically calculate the value for the LO frequency, or you can specify it with the
 [LO Frequency](niusrp-lo-frequency-00118c3e.html) property.

If you only specify a value for the [Carrier Frequency](niusrp-carrier-frequency-00118c34.html) property,
 NI-USRP sets the LO frequency as close to the carrier frequency as possible and implements
 the remainder of the frequency translation using digital signal processing. Any time the
 carrier frequency changes, NI-USRP adjusts the LO frequency. However, each time the LO
 frequency changes, NI-USRP must wait for the LO frequency to settle before it adjusts,
 which causes a delay.

When changing carrier frequencies within a narrow range, you can minimize retuning time
 by locking the LO frequency to one value using the LO Frequency property. In this case,
 changes to the carrier frequency do not affect the specified LO frequency, and NI-USRP
 only changes the digital signal processing frequency to account for the difference between
 the carrier frequency and LO frequency. To unlock the LO frequency and allow NI-USRP to
 automatically calculate it, set the LO Frequency property to -1. Specifying the LO
 frequency allows you to offset the LO from the carrier frequency, which avoids LO
 feedthrough that can distort your signal.

The range of available values is hardware dependent. If you specify a value outside the
 range supported by your device, NI-USRP coerces the value to the nearest supported value.
 Writing to this property specifies the value you want to use. Reading from this property
 returns the actual value, which may have been coerced to the capabilities of the device.
 NI recommends that you read the value after you write to this property to determine the
 actual setting for the device.

Note

*Carrier Frequency* = *LO Frequency* - *DSP Frequency*

For example, if you want to sweep through a 25 MHz band
 starting at 2.4375 GHz, set the LO Frequency property to a
 value halfway through the band using the following equation:

2.4375 GHz + (25 MHz / 2) =
 2.45 GHz

When you set the LO Frequency property to 2.45 GHz, as the
 carrier frequency changes, NI-USRP only changes the DSP frequency as it sweeps through the
 bandwidth. The following figure illustrates how NI-USRP sets the frequency values on the
 first step of the sweep.

[IMAGE alt='1378' src='GUID-CE85578F-30E9-4D9A-B503-AA63CB351C27-a5.gif']

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-coerced-lo-if1-frequency-00118c46.html language=enus -->
## TOPIC 00007: Coerced LO IF1 Frequency

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-coerced-lo-if1-frequency-00118c46.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-coerced-lo-if1-frequency-00118c46.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads back the frequency, in Hz, of the IF1 LO. Hardware Support This property supports the following hardware: USRP-2945 USRP-2955 Channel-based No Resettable Yes Obtaining Carrier Frequency in Hardware The overall carrier frequency is realized in hardware as a combination of frequency translation

Coerced LO IF1 Frequency

Reads back the frequency, in Hz, of the IF1 LO.

#### Hardware Support

This property supports the following hardware:

- USRP-2945
- USRP-2955

**Permissions:** Read

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Channel-based | No |
| --- | --- |
| Resettable | Yes |

#### Obtaining Carrier Frequency in Hardware

The overall carrier frequency is realized in hardware as a combination of frequency translation in the local oscillator (LO) and an additional frequency translation implemented in the digital signal processing on the FPGA. You can allow NI-USRP to automatically calculate the value for the LO frequency, or you can specify it with the 
 [LO Frequency](niusrp-lo-frequency-00118c3e.html) property.

For the USRP-2945/2955, you can manually configure the separate LO stage frequencies by specifying bothLO IF1 Frequency and LO IF2 Frequency to avoid the automatic tuning used in either 
 [Carrier Frequency](niusrp-carrier-frequency-00118c34.html) or 
 [LO Frequency](niusrp-lo-frequency-00118c3e.html) properties. When LO IF1 Frequency is configured, NI-USRP adjusts the DSP frequency translation to maintain the same overall carrier frequency if possible.

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-coerced-lo-if2-frequency-00118c47.html language=enus -->
## TOPIC 00008: Coerced LO IF2 Frequency

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-coerced-lo-if2-frequency-00118c47.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-coerced-lo-if2-frequency-00118c47.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads back the frequency, in Hz, of the IF2 LO. Hardware Support This property supports the following hardware: USRP-2945 USRP-2955 Channel-based No Resettable Yes Obtaining Carrier Frequency in Hardware The overall carrier frequency is realized in hardware as a combination of frequency translation

Coerced LO IF2 Frequency

Reads back the frequency, in Hz, of the IF2 LO.

#### Hardware Support

This property supports the following hardware:

- USRP-2945
- USRP-2955

**Permissions:** Read

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Channel-based | No |
| --- | --- |
| Resettable | Yes |

#### Obtaining Carrier Frequency in Hardware

The overall carrier frequency is realized in hardware as a combination of frequency translation in the local oscillator (LO) and an additional frequency translation implemented in the digital signal processing on the FPGA. You can allow NI-USRP to automatically calculate the value for the LO frequency, or you can specify it with the 
 [LO Frequency](niusrp-lo-frequency-00118c3e.html) property.

For the USRP-2945/2955, you can manually configure the separate LO stage frequencies by specifying bothLO IF1 Frequency and LO IF2 Frequency to avoid the automatic tuning used in either 
 [Carrier Frequency](niusrp-carrier-frequency-00118c34.html) or 
 [LO Frequency](niusrp-lo-frequency-00118c3e.html) properties. When LO IF1 Frequency is configured, NI-USRP adjusts the DSP frequency translation to maintain the same overall carrier frequency if possible.

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-current-driver-version-00118d30.html language=enus -->
## TOPIC 00009: Current Driver Version

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-current-driver-version-00118d30.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-current-driver-version-00118d30.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string that contains the current version information for the NI-USRP driver. For example, NI-USRP can return 1.3.0. Hardware Support This property supports the following hardware: USRP-2900/2901 USRP-2920/2921/2922 USRP-2930/2932 USRP-2940/2942/2943/2944/2945 USRP-2950/2952/2953/2954/2955

Current Driver Version

Returns a string that contains the current version information for the NI-USRP driver. For example, NI-USRP can return 
1.3.0.

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Channel-based | No |
| --- | --- |
| Resettable | No |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-current-firmware-version-00118d32.html language=enus -->
## TOPIC 00010: Current Firmware Version

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-current-firmware-version-00118d32.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-current-firmware-version-00118d32.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string containing the current version of the firmware for the device you are currently using. Hardware Support This property supports the following hardware: USRP-2900/2901 USRP-2920/2921/2922 USRP-2930/2932 USRP-2940/2942/2943/2944/2945 USRP-2950/2952/2953/2954/2955 Channel-based Yes Rese

Current Firmware Version

Returns a string containing the current version of the firmware for the device you are currently using.

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Channel-based | Yes |
| --- | --- |
| Resettable | No |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-current-fpga-version-00118d34.html language=enus -->
## TOPIC 00011: Current FPGA Version

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-current-fpga-version-00118d34.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-current-fpga-version-00118d34.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string containing the current version of the FPGA image for the device you are currently using. Hardware Support This property supports the following hardware: USRP-2900/2901 USRP-2920/2921/2922 USRP-2930/2932 USRP-2940/2942/2943/2944/2945 USRP-2950/2952/2953/2954/2955 Channel-based Yes Re

Current FPGA Version

Returns a string containing the current version of the FPGA image for the device you are currently using.

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Channel-based | Yes |
| --- | --- |
| Resettable | No |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-data-clock-rate-00118e38.html language=enus -->
## TOPIC 00012: Data Clock Rate

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-data-clock-rate-00118e38.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-data-clock-rate-00118e38.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the data rate of samples coming from the analog-to-digital converters (ADCs) to the DSP or going to the digital-to-analog converters (DACs) from the DSP. Only the USRP-2900/2901 supports changing the data clock rate. Hardware Support This property supports the following hardware: USRP-2900

Data Clock Rate

Specifies the data rate of samples coming from the analog-to-digital converters (ADCs) to the DSP or going to the digital-to-analog converters (DACs) from the DSP.

Only the USRP-2900/2901 supports changing the data clock rate.

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Channel-based | No |
| --- | --- |
| Resettable | Yes |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-enabled-channels-00118c40.html language=enus -->
## TOPIC 00013: Enabled Channels

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-enabled-channels-00118c40.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-enabled-channels-00118c40.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the list of channels enabled for acquisition/generation for this session. Valid Values: "0", "1", "0,1", etc. Hardware Support This property supports the following hardware: USRP-2900/2901 USRP-2920/2921/2922 USRP-2930/2932 USRP-2940/2942/2943/2944/2945 USRP-2950/2952/2953/2954/2955 Defaul

Enabled Channels

Specifies the list of channels enabled for acquisition/generation for this session.

Valid Values: "0", "1", "0,1", etc.

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

Default value: "" (empty string, which means all channels)

| Channel-based | No |
| --- | --- |
| Resettable | Yes |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-expected-peak-00118c3d.html language=enus -->
## TOPIC 00014: Expected Peak

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-expected-peak-00118c3d.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-expected-peak-00118c3d.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the expected peak signal, as a fraction of the full-scale signal to acquire or generate. 1.0 = 100%, 0.5 = 50%. NI-USRP uses this value to scale 8-bit data transferred over the bus. USRP devices support 16-bit values, which allow a full-scale binary data range from -32,768 to 32,767. When

Expected Peak

Specifies the expected peak signal, as a fraction of the full-scale signal to acquire or generate.

1.0 = 100%,0.5 = 50%. NI-USRP uses this value to scale 8-bit data transferred over the bus. USRP devices support 16-bit values, which allow a full-scale binary data range from -32,768 to 32,767. When using an 8-bit sample width, transfer the 8-bit samples that contain the significant values of your signal. Use this property to specify the fraction of the full-scale range you expect your signal to occupy so that you transfer the most significant bits.

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

Default value: 1.0

| Channel-based | No |
| --- | --- |
| Resettable | Yes |

#### Determining Expected Peak

Use the following equation to determine the value for the Expected Peak property:

*Expected Actual Signal Range*/*Full-Scale Range* = 
 *Expected Peak Property Value*

For example, if your input signal range is -128 to 127, the expected peak, as a fraction of full-scale, is 0.00390625. If you set the Expected Peak property to 0.00390625 and the 
 [Sample Width](niusrp-sample-width-00118c3c.html) property to 8-bit, NI-USRP transfers the lower 8-bits of data across the bus, which preserves the full dynamic range of the signal. If you set the Expected Peak property to the default value (1.0), only the upper 8-bits are transferred across the bus, which results in a signal loss.

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-exported-reference-frequency-output-terminal-00118c83.html language=enus -->
## TOPIC 00015: Exported Reference Frequency Output Terminal

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-exported-reference-frequency-output-terminal-00118c83.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-exported-reference-frequency-output-terminal-00118c83.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output terminal of the exported reference frequency signal. Hardware Support This property supports the following hardware: USRP-2940/2942/2943/2944/2945 USRP-2950/2952/2953/2954/2955 None "" Indicates the signal should not be exported. RefOut "RefOut" Exports the signal to the REF OUT

Exported Reference Frequency Output Terminal

Specifies the output terminal of the exported reference frequency signal.

#### Hardware Support

This property supports the following hardware:

- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| None | "" | Indicates the signal should not be exported. |
| --- | --- | --- |
| RefOut | "RefOut" | Exports the signal to the REF OUT front panel terminal. |

| Channel-based | No |
| --- | --- |
| Resettable | Yes |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-exported-timebase-clock-output-terminal-00118c84.html language=enus -->
## TOPIC 00016: Exported Timebase Clock Output Terminal

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-exported-timebase-clock-output-terminal-00118c84.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-exported-timebase-clock-output-terminal-00118c84.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output terminal of the exported timebase clock (PPS) signal. Hardware Support This property supports the following hardware: USRP-2940/2942/2943/2944/2945 USRP-2950/2952/2953/2954/2955 None "" Indicates the signal should not be exported. PpsTrigOut "PpsTrigOut" Exports the signal to th

Exported Timebase Clock Output Terminal

Specifies the output terminal of the exported timebase clock (PPS) signal.

#### Hardware Support

This property supports the following hardware:

- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| None | "" | Indicates the signal should not be exported. |
| --- | --- | --- |
| PpsTrigOut | "PpsTrigOut" | Exports the signal to the PPS TRIG OUT front panel terminal. |

| Channel-based | No |
| --- | --- |
| Resettable | Yes |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-gain-00118c36.html language=enus -->
## TOPIC 00017: Gain

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-gain-00118c36.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-gain-00118c36.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the gain, in dB, applied to the RF signal for receive (Rx) and transmit (Tx) signals. Gain represents the total aggregate gain applied to the signal throughout the signal path. Hardware Support This property supports the following hardware: USRP-2900/2901 USRP-2920/2921/2922 USRP-2930/2932

Gain

Specifies the gain, in dB, applied to the RF signal for receive (Rx) and transmit (Tx) signals.

Gain represents the total aggregate gain applied to the signal throughout the signal path.

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Channel-based | Yes |
| --- | --- |
| Resettable | Yes |

#### Considerations of Gain Values and Hardware

The USRP devices are not calibrated. The gain value does not represent an absolute gain and does not have linear behavior. Different devices exhibit different gain curves for different carrier frequencies. You may need to experiment to determine the correct gain setting for your application.

The range of available values is hardware dependent. If you specify a value outside the range supported by your device, NI-USRP coerces the value to the nearest supported value. Writing to this property specifies the value you want to use. Reading from this property returns the actual value, which may have been coerced to the capabilities of the device. NI recommends that you read the value after you write to this property to determine the actual setting for the device.

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-gps-lock-status-00118d61.html language=enus -->
## TOPIC 00018: GPS Lock Status

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-gps-lock-status-00118d61.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-gps-lock-status-00118d61.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns True if the GPS has a satellite fix. True The GPS has a satellite fix. False The GPS does not have a satellite fix. Hardware Support This property supports the following hardware: USRP-2930/2932 USRP-2950/2952/2953/2954/2955 Channel-based Yes Resettable No

GPS Lock Status

Returns True if the GPS has a satellite fix.

| True | The GPS has a satellite fix. |
| --- | --- |
| False | The GPS does not have a satellite fix. |

#### Hardware Support

This property supports the following hardware:

- USRP-2930/2932
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Channel-based | Yes |
| --- | --- |
| Resettable | No |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-gps-sentence-gga-00118d62.html language=enus -->
## TOPIC 00019: GPS Sentence GGA

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-gps-sentence-gga-00118d62.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-gps-sentence-gga-00118d62.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the GPS fix data. Hardware Support This property supports the following hardware: USRP-2930/2932 USRP-2950/2952/2953/2954/2955 Channel-based Yes Resettable No

GPS Sentence GGA

Returns the GPS fix data.

#### Hardware Support

This property supports the following hardware:

- USRP-2930/2932
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Channel-based | Yes |
| --- | --- |
| Resettable | No |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-gps-sentence-rmc-00118d63.html language=enus -->
## TOPIC 00020: GPS Sentence RMC

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-gps-sentence-rmc-00118d63.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-gps-sentence-rmc-00118d63.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the recommended minimum specific GPS and transit data. Hardware Support This property supports the following hardware: USRP-2930/2932 USRP-2950/2952/2953/2954/2955 Channel-based Yes Resettable No

GPS Sentence RMC

Returns the recommended minimum specific GPS and transit data.

#### Hardware Support

This property supports the following hardware:

- USRP-2930/2932
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Channel-based | Yes |
| --- | --- |
| Resettable | No |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-gps-time-seconds-00118d60.html language=enus -->
## TOPIC 00021: GPS Time (seconds)

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-gps-time-seconds-00118d60.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-gps-time-seconds-00118d60.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the time that the GPS reports. Time is measured in seconds since 00:00:00 January 1, 1970 (UTC). Hardware Support This property supports the following hardware: USRP-2930/2932 USRP-2950/2952/2953/2954/2955 Channel-based Yes Resettable No

GPS Time (seconds)

Returns the time that the GPS reports.

Time is measured in seconds since 00:00:00 January 1, 1970 (UTC).

#### Hardware Support

This property supports the following hardware:

- USRP-2930/2932
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Channel-based | Yes |
| --- | --- |
| Resettable | No |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-has-gps-disciplined-clock-00118d36.html language=enus -->
## TOPIC 00022: Has GPS Disciplined Clock?

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-has-gps-disciplined-clock-00118d36.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-has-gps-disciplined-clock-00118d36.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns True if the device has a GPS-disciplined clock. This property allows the device to use a GPS clock reference and GPS timestamps. True The device has a GPS-disciplined clock. False The device does not have a GPS-disciplined clock. Hardware Support This property supports the following hardware

Has GPS Disciplined Clock?

Returns True if the device has a GPS-disciplined clock.

This property allows the device to use a GPS clock reference and GPS timestamps.

| True | The device has a GPS-disciplined clock. |
| --- | --- |
| False | The device does not have a GPS-disciplined clock. |

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Channel-based | Yes |
| --- | --- |
| Resettable | No |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-host-data-type-00118c3f.html language=enus -->
## TOPIC 00023: Host Data Type

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-host-data-type-00118c3f.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-host-data-type-00118c3f.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the data type to fetch from or write to the driver. Hardware Support This property supports the following hardware: USRP-2900/2901 USRP-2920/2921/2922 USRP-2930/2932 USRP-2940/2942/2943/2944/2945 USRP-2950/2952/2953/2954/2955 CDB 0 Write or fetch data as complex, double-precision floating-

Host Data Type

Specifies the data type to fetch from or write to the driver.

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| CDB | 0 | Write or fetch data as complex, double-precision floating-point (CDB) samples. |
| --- | --- | --- |
| I16 | 1 | Write or fetch data as signed 16-bit integer (I16) samples. |

Default value: CDB

| Channel-based | No |
| --- | --- |
| Resettable | Yes |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-iq-rate-00118c33.html language=enus -->
## TOPIC 00024: IQ Rate

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-iq-rate-00118c33.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-iq-rate-00118c33.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sample rate of the baseband I/Q data for transmit (Tx) or receive (Rx) signals in samples per second (S/s). Hardware Support This property supports the following hardware: USRP-2900/2901 USRP-2920/2921/2922 USRP-2930/2932 USRP-2940/2942/2943/2944/2945 USRP-2950/2952/2953/2954/2955 Chan

IQ Rate

Specifies the sample rate of the baseband I/Q data for transmit (Tx) or receive (Rx) signals in samples per second (S/s).

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Channel-based | No |
| --- | --- |
| Resettable | Yes |

#### Range of Valid Values

The range of available values is hardware dependent. If you specify a value outside the range supported by your device, NI-USRP coerces the value to the nearest supported value. Writing to this property specifies the value you want to use. Reading from this property returns the actual value, which may have been coerced to the capabilities of the device. NI recommends that you read the value after you write to this property to determine the actual setting for the device.

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-lo-export-enabled-00118c42.html language=enus -->
## TOPIC 00025: LO Export Enabled

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-lo-export-enabled-00118c42.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-lo-export-enabled-00118c42.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether or not to export the LO of the selected channel. Hardware Support This property supports the following hardware: USRP-2945 USRP-2955 Default value: False Channel-based No Resettable Yes

LO Export Enabled

Specifies whether or not to export the LO of the selected channel.

#### Hardware Support

This property supports the following hardware:

- USRP-2945
- USRP-2955

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

Default value: False

| Channel-based | No |
| --- | --- |
| Resettable | Yes |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-lo-frequency-00118c3e.html language=enus -->
## TOPIC 00026: LO Frequency

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-lo-frequency-00118c3e.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-lo-frequency-00118c3e.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the local oscillator (LO) frequency, in Hz. Hardware Support This property supports the following hardware: USRP-2900/2901 USRP-2920/2921/2922 USRP-2930/2932 USRP-2940/2942/2943/2944/2945 USRP-2950/2952/2953/2954/2955 Default value: -1 Channel-based Yes Resettable Yes Considerations for Sp

LO Frequency

Specifies the local oscillator (LO) frequency, in Hz.

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

Default value: -1

| Channel-based | Yes |
| --- | --- |
| Resettable | Yes |

#### Considerations for Specifying Carrier
 Frequency and LO Frequency

The overall carrier frequency is realized in hardware as a combination of frequency
 translation in the local oscillator (LO) and an additional frequency translation
 implemented in the digital signal processing on the FPGA. You can allow NI-USRP to
 automatically calculate the value for the LO frequency, or you can specify it with the
 LO Frequency property.

If you only specify a value for the [Carrier Frequency](niusrp-carrier-frequency-00118c34.html) property,
 NI-USRP sets the LO frequency as close to the carrier frequency as possible and implements
 the remainder of the frequency translation using digital signal processing. Any time the
 carrier frequency changes, NI-USRP adjusts the LO frequency. However, each time the LO
 frequency changes, NI-USRP must wait for the LO frequency to settle before it adjusts,
 which causes a delay.

When changing carrier frequencies within a narrow range, you can minimize retuning time
 by locking the LO frequency to one value using the LO Frequency property. In this case,
 changes to the carrier frequency do not affect the specified LO frequency, and NI-USRP
 only changes the digital signal processing frequency to account for the difference between
 the carrier frequency and LO frequency. To unlock the LO frequency and allow NI-USRP to
 automatically calculate it, set the LO Frequency property to -1. Specifying the LO
 frequency allows you to offset the LO from the carrier frequency, which avoids LO
 feedthrough that can distort your signal.

The range of available values is hardware dependent. If you specify a value outside the
 range supported by your device, NI-USRP coerces the value to the nearest supported value.
 Writing to this property specifies the value you want to use. Reading from this property
 returns the actual value, which may have been coerced to the capabilities of the device.
 NI recommends that you read the value after you write to this property to determine the
 actual setting for the device.

Note

*Carrier Frequency* = *LO Frequency* - *DSP Frequency*

For example, if you want to sweep through a 25 MHz band
 starting at 2.4375 GHz, set the LO Frequency property to a
 value halfway through the band using the following equation:

2.4375 GHz + (25 MHz / 2) =
 2.45 GHz

When you set the LO Frequency property to 2.45 GHz, as the
 carrier frequency changes, NI-USRP only changes the DSP frequency as it sweeps through the
 bandwidth. The following figure illustrates how NI-USRP sets the frequency values on the
 first step of the sweep.

[IMAGE alt='1378' src='GUID-CE85578F-30E9-4D9A-B503-AA63CB351C27-a5.gif']

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-lo-if1-frequency-00118c43.html language=enus -->
## TOPIC 00027: LO IF1 Frequency

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-lo-if1-frequency-00118c43.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-lo-if1-frequency-00118c43.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency, in Hz, of the IF1 LO. Hardware Support This property supports the following hardware: USRP-2945 USRP-2955 Channel-based No Resettable Yes Obtaining Carrier Frequency in Hardware The overall carrier frequency is realized in hardware as a combination of frequency translation i

LO IF1 Frequency

Specifies the frequency, in Hz, of the IF1 LO.

#### Hardware Support

This property supports the following hardware:

- USRP-2945
- USRP-2955

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Channel-based | No |
| --- | --- |
| Resettable | Yes |

#### Obtaining Carrier Frequency in Hardware

The overall carrier frequency is realized in hardware as a combination of frequency translation in the local oscillator (LO) and an additional frequency translation implemented in the digital signal processing on the FPGA. You can allow NI-USRP to automatically calculate the value for the LO frequency, or you can specify it with the 
 [LO Frequency](niusrp-lo-frequency-00118c3e.html) property.

For the USRP-2945/2955, you can manually configure the separate LO stage frequencies by specifying bothLO IF1 Frequency and LO IF2 Frequency to avoid the automatic tuning used in either 
 [Carrier Frequency](niusrp-carrier-frequency-00118c34.html) or 
 [LO Frequency](niusrp-lo-frequency-00118c3e.html) properties. When LO IF1 Frequency is configured, NI-USRP adjusts the DSP frequency translation to maintain the same overall carrier frequency if possible.

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-lo-if2-frequency-00118c44.html language=enus -->
## TOPIC 00028: LO IF2 Frequency

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-lo-if2-frequency-00118c44.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-lo-if2-frequency-00118c44.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency, in Hz, of the IF2 LO. Hardware Support This property supports the following hardware: USRP-2945 USRP-2955 Channel-based No Resettable Yes Obtaining Carrier Frequency in Hardware The overall carrier frequency is realized in hardware as a combination of frequency translation i

LO IF2 Frequency

Specifies the frequency, in Hz, of the IF2 LO.

#### Hardware Support

This property supports the following hardware:

- USRP-2945
- USRP-2955

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Channel-based | No |
| --- | --- |
| Resettable | Yes |

#### Obtaining Carrier Frequency in Hardware

The overall carrier frequency is realized in hardware as a combination of frequency translation in the local oscillator (LO) and an additional frequency translation implemented in the digital signal processing on the FPGA. You can allow NI-USRP to automatically calculate the value for the LO frequency, or you can specify it with the 
 [LO Frequency](niusrp-lo-frequency-00118c3e.html) property.

For the USRP-2945/2955, you can manually configure the separate LO stage frequencies by specifying bothLO IF1 Frequency and LO IF2 Frequency to avoid the automatic tuning used in either 
 [Carrier Frequency](niusrp-carrier-frequency-00118c34.html) or 
 [LO Frequency](niusrp-lo-frequency-00118c3e.html) properties. When LO IF1 Frequency is configured, NI-USRP adjusts the DSP frequency translation to maintain the same overall carrier frequency if possible.

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-lo-source-00118c41.html language=enus -->
## TOPIC 00029: LO Source

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-lo-source-00118c41.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-lo-source-00118c41.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the LO source for the selected channel. Hardware Support This property supports the following hardware: USRP-2945 USRP-2955 Internal internal Uses internal channel LO source. Companion companion Uses internal LO source of the other channel on the shared daughterboard. External/LO IN extern

LO Source

Specifies the LO source for the selected channel.

#### Hardware Support

This property supports the following hardware:

- USRP-2945
- USRP-2955

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Internal | internal | Uses internal channel LO source. |
| --- | --- | --- |
| Companion | companion | Uses internal LO source of the other channel on the shared daughterboard. |
| External/LO IN | external | Uses external LO source. |
| Reimport | reimport | Uses an LO source that originates internally, is exported, and is then imported through the external LO terminal. |

Default value: Internal

| Channel-based | No |
| --- | --- |
| Resettable | Yes |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-model-00118d31.html language=enus -->
## TOPIC 00030: Model

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-model-00118d31.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-model-00118d31.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string that contains the model number or name of the device that you are currently using. Hardware Support This property supports the following hardware: USRP-2900/2901 USRP-2920/2921/2922 USRP-2930/2932 USRP-2940/2942/2943/2944/2945 USRP-2950/2952/2953/2954/2955 Channel-based Yes Resettab

Model

Returns a string that contains the model number or name of the device that you are currently using.

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Channel-based | Yes |
| --- | --- |
| Resettable | No |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-number-of-channels-in-session-00118d80.html language=enus -->
## TOPIC 00031: Number of Channels in Session

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-number-of-channels-in-session-00118d80.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-number-of-channels-in-session-00118d80.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of separate transmit (Tx) or receive (Rx) channels contained in the current driver session. Hardware Support This property supports the following hardware: USRP-2900/2901 USRP-2920/2921/2922 USRP-2930/2932 USRP-2940/2942/2943/2944/2945 USRP-2950/2952/2953/2954/2955 Channel-based N

Number of Channels in Session

Returns the number of separate transmit (Tx) or receive (Rx) channels contained in the current driver session.

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Channel-based | No |
| --- | --- |
| Resettable | No |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-number-of-samples-00118c32.html language=enus -->
## TOPIC 00032: Number of Samples

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-number-of-samples-00118c32.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-number-of-samples-00118c32.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the finite number of samples to acquire. This value is ignored if you set the Number of Samples Is Finite property to False. Hardware Support This property supports the following hardware: USRP-2900/2901 USRP-2920/2921/2922 USRP-2930/2932 USRP-2940/2942/2943/2944/2945 USRP-2950/2952/2953/2

Number of Samples

Specifies the finite number of samples to acquire.

This value is ignored if you set the [Number of Samples Is Finite](niusrp-number-of-samples-is-finite-00118c31.html) property to False.

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Channel-based | No |
| --- | --- |
| Resettable | Yes |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-number-of-samples-is-finite-00118c31.html language=enus -->
## TOPIC 00033: Number of Samples Is Finite

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-number-of-samples-is-finite-00118c31.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-number-of-samples-is-finite-00118c31.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the device acquires a finite number of samples or acquires samples continuously. True Acquires a finite number of samples. False Acquires samples continuously until you abort the acquisition. Hardware Support This property supports the following hardware: USRP-2900/2901 USRP-2920/2

Number of Samples Is Finite

Specifies whether the device acquires a finite number of samples or acquires samples continuously.

| True | Acquires a finite number of samples. |
| --- | --- |
| False | Acquires samples continuously until you abort the acquisition. |

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

Default value: False

| Channel-based | No |
| --- | --- |
| Resettable | Yes |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-oldest-compatible-firmware-version-00118d33.html language=enus -->
## TOPIC 00034: Oldest Compatible Firmware Version

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-oldest-compatible-firmware-version-00118d33.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-oldest-compatible-firmware-version-00118d33.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string containing the oldest compatible version of the firmware for the device you are currently using. Hardware Support This property supports the following hardware: USRP-2900/2901 USRP-2920/2921/2922 USRP-2930/2932 USRP-2940/2942/2943/2944/2945 USRP-2950/2952/2953/2954/2955 Channel-base

Oldest Compatible Firmware Version

Returns a string containing the oldest compatible version of the firmware for the device you are currently using.

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Channel-based | Yes |
| --- | --- |
| Resettable | No |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-oldest-compatible-fpga-version-00118d35.html language=enus -->
## TOPIC 00035: Oldest Compatible FPGA Version

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-oldest-compatible-fpga-version-00118d35.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-oldest-compatible-fpga-version-00118d35.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string containing the oldest compatible version of the FPGA image for the device you are currently using. Hardware Support This property supports the following hardware: USRP-2900/2901 USRP-2920/2921/2922 USRP-2930/2932 USRP-2940/2942/2943/2944/2945 USRP-2950/2952/2953/2954/2955 Channel-ba

Oldest Compatible FPGA Version

Returns a string containing the oldest compatible version of the FPGA image for the device you are currently using.

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Channel-based | Yes |
| --- | --- |
| Resettable | No |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-reference-frequency-source-00118c38.html language=enus -->
## TOPIC 00036: Reference Frequency Source

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-reference-frequency-source-00118c38.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-reference-frequency-source-00118c38.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source of the signal used as a frequency reference for the local oscillator (LO). Hardware Support This property supports the following hardware: USRP-2900/2901 USRP-2920/2921/2922 USRP-2930/2932 USRP-2940/2942/2943/2944/2945 USRP-2950/2952/2953/2954/2955 Internal "Internal" Specifies

Reference Frequency Source

Specifies the source of the signal used as a frequency reference for the local oscillator (LO).

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Internal | "Internal" | Specifies the onboard reference signal as the source for the frequency reference signal. |
| --- | --- | --- |
| RefIn | "RefIn" | Specifies the reference signal received from the REF IN connector on the device front panel as the source for the frequency reference signal. |
| Mimo | "Mimo" | Specifies the reference signal received from the MIMO EXPANSION connector on the device front panel as the source for the frequency reference signal. |
| GPS | "GPS" | Specifies the reference signal received from the GPS. |

Default value: Internal

| Channel-based | Yes |
| --- | --- |
| Resettable | Yes |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-sample-width-00118c3c.html language=enus -->
## TOPIC 00037: Sample Width

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-sample-width-00118c3c.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-sample-width-00118c3c.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the width, in bits, of the binary data sample transferred across the bus between the host and the device. Hardware Support This property supports the following hardware: USRP-2900/2901 USRP-2920/2921/2922 USRP-2930/2932 USRP-2940/2942/2943/2944/2945 USRP-2950/2952/2953/2954/2955 16-bit 16

Sample Width

Specifies the width, in bits, of the binary data sample transferred across the bus between the host and the device.

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| 16-bit | 16 | Each component of each complex sample uses 16 bits, for a total of 32 bits per sample. |
| --- | --- | --- |
| 8-bit | 8 | Each component of each complex sample uses 8 bits, for a total of 16 bits per sample. |

Default value: 
 16-bit

| Channel-based | No |
| --- | --- |
| Resettable | Yes |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-start-trigger-time-fractional-seconds-00118c82.html language=enus -->
## TOPIC 00038: Start Trigger Time (fractional seconds)

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-start-trigger-time-fractional-seconds-00118c82.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-start-trigger-time-fractional-seconds-00118c82.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the fractional seconds part of the trigger start time. Hardware Support This property supports the following hardware: USRP-2900/2901 USRP-2920/2921/2922 USRP-2930/2932 USRP-2940/2942/2943/2944/2945 USRP-2950/2952/2953/2954/2955 Channel-based No Resettable Yes

Start Trigger Time (fractional seconds)

Specifies the fractional seconds part of the trigger start time.

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Channel-based | No |
| --- | --- |
| Resettable | Yes |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-start-trigger-time-whole-seconds-00118c81.html language=enus -->
## TOPIC 00039: Start Trigger Time (whole seconds)

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-start-trigger-time-whole-seconds-00118c81.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-start-trigger-time-whole-seconds-00118c81.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the whole seconds part of the trigger start time. Hardware Support This property supports the following hardware: USRP-2900/2901 USRP-2920/2921/2922 USRP-2930/2932 USRP-2940/2942/2943/2944/2945 USRP-2950/2952/2953/2954/2955 Channel-based No Resettable Yes

Start Trigger Time (whole seconds)

Specifies the whole seconds part of the trigger start time.

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Channel-based | No |
| --- | --- |
| Resettable | Yes |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-start-trigger-type-00118c80.html language=enus -->
## TOPIC 00040: Start Trigger Type

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-start-trigger-type-00118c80.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-start-trigger-type-00118c80.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of Start Trigger, which controls how the device generates or acquires signals. Use this property to choose whether to generate or acquire data immediately or to synchronize generations and acquisitions to the timestamp specified by the Start Trigger Time properties. Hardware Suppo

Start Trigger Type

Specifies the type of Start Trigger, which controls how the device generates or acquires signals.

Use this property to choose whether to generate or acquire data immediately or to synchronize generations and acquisitions to the timestamp specified by the Start Trigger Time properties.

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| None | 0 | For Rx, acquires data immediately (as soon as the acquisition starts). For Tx, generates data as soon as it writes to the device. |
| --- | --- | --- |
| Time | 1 | Acquires or generates data synchronous to a timestamp. The Start Trigger occurs when the onboard device timer reaches the timestamp specified by the Start Trigger Time properties. |

Default value: None

| Channel-based | No |
| --- | --- |
| Resettable | Yes |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-timebase-clock-polarity-00118c3a.html language=enus -->
## TOPIC 00041: Timebase Clock Polarity

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-timebase-clock-polarity-00118c3a.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-timebase-clock-polarity-00118c3a.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of the signal used as the timebase clock if you set the Start Trigger Type property to Time. Hardware Support This property supports the following hardware: USRP-2900/2901 USRP-2920/2921/2922 USRP-2930/2932 USRP-2940/2942/2943/2944/2945 USRP-2950/2952/2953/2954/2955 Rising 0 D

Timebase Clock Polarity

Specifies the polarity of the signal used as the timebase clock if you set the [Start Trigger Type](niusrp-start-trigger-type-00118c80.html) property to Time.

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Rising | 0 | Data latches on the clock rising edge. |
| --- | --- | --- |
| Falling | 1 | Data latches on the clock falling edge. |

Default value: Rising

| Channel-based | Yes |
| --- | --- |
| Resettable | Yes |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-timebase-clock-source-00118c39.html language=enus -->
## TOPIC 00042: Timebase Clock Source

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-timebase-clock-source-00118c39.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-timebase-clock-source-00118c39.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source of the signal used as the timebase clock if you set the Start Trigger Type property to Time. Hardware Support This property supports the following hardware: USRP-2900/2901 USRP-2920/2921/2922 USRP-2930/2932 USRP-2940/2942/2943/2944/2945 USRP-2950/2952/2953/2954/2955 Internal "In

Timebase Clock Source

Specifies the source of the signal used as the timebase clock if you set the [Start Trigger Type](niusrp-start-trigger-type-00118c80.html) property to Time.

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Internal | "Internal" | Specifies the onboard device timer as the source for the timebase clock. |
| --- | --- | --- |
| PpsIn | "PpsIn" | Specifies the signal received from the PPS IN connector on the device front panel as the source for the timebase clock. |
| Mimo | "Mimo" | Specifies the signal received from the MIMO EXPANSION connector on the device front panel as the source for the timebase clock. |
| GPS | "GPS" | Specifies the reference signal received from the GPS. |

Default value: Internal

| Channel-based | Yes |
| --- | --- |
| Resettable | Yes |

Parent topic:

NI-USRP

<!--NI_TOPIC bundle=ni-usrp-lvnxg-prop-api-ref path=niusrp-warning-policy-00118e30.html language=enus -->
## TOPIC 00043: Warning Policy

- bundle_id: `ni-usrp-lvnxg-prop-api-ref`
- source_path: `niusrp-warning-policy-00118e30.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-prop-api-ref/raw/resource/enus/niusrp-warning-policy-00118e30.html
- document_id: `ni-usrp-lvnxg-prop-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether NI-USRP returns an error, returns a warning, or ignores overflow, underflow, or timeout conditions during data transfer. Hardware Support This property supports the following hardware: USRP-2900/2901 USRP-2920/2921/2922 USRP-2930/2932 USRP-2940/2942/2943/2944/2945 USRP-2950/2952/29

Warning Policy

Specifies whether NI-USRP returns an error, returns a warning, or ignores overflow, underflow, or timeout conditions during data transfer.

#### Hardware Support

This property supports the following hardware:

- USRP-2900/2901
- USRP-2920/2921/2922
- USRP-2930/2932
- USRP-2940/2942/2943/2944/2945
- USRP-2950/2952/2953/2954/2955

**Permissions:** Read/Write

**Data type:**[IMAGE alt='datatype_icon' src='/assets/img/.png']

| Return Warnings | 0 | Returns a warning when an overflow, underflow, or timeout condition occurs during a data transfer. |
| --- | --- | --- |
| Return Errors | 1 | Returns an error when an overflow, underflow, or timeout condition occurs during a data transfer. |
| Return Success | 2 | Ignores overflow, underflow, or timeout conditions during a data transfer. |

Default value: Return Errors

| Channel-based | No |
| --- | --- |
| Resettable | Yes |

Parent topic:

NI-USRP
