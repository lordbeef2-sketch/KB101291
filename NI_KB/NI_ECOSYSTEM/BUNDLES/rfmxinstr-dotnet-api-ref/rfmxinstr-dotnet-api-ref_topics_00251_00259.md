# NI DOCUMENT BUNDLE: rfmxinstr-dotnet-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxinstr-dotnet-api-ref start=251 end=259 -->
<!--NI_TOPIC bundle=rfmxinstr-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxinstrmxmechanicalattenuationauto.html language=enus -->
## TOPIC 00251: RFmxInstrMXMechanicalAttenuationAuto Enumeration

- bundle_id: `rfmxinstr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxinstrmxmechanicalattenuationauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxinstrmxmechanicalattenuationauto.html
- document_id: `rfmxinstr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether RFmx chooses an attenuation setting based on the hardware settings. SyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic enum RFmxInstrMXMechanicalAttenuationAutoMembersNameValueDescriptionFalse0Specifies that RFmx uses the value configured in the Mechanical Attenuation Value me

### RFmxInstrMXMechanicalAttenuationAuto Enumeration

Specifies whether RFmx chooses an attenuation setting based on the hardware settings.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public enum RFmxInstrMXMechanicalAttenuationAuto

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Specifies that RFmx uses the value configured in the Mechanical Attenuation Value method. |
| True | 1 | Specifies that the measurement computes the mechanical attenuation. |

Parent topic:

NationalInstruments.RFmx.InstrMX

<!--NI_TOPIC bundle=rfmxinstr-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxinstrmxoptimizepathforsignalbandwidth.html language=enus -->
## TOPIC 00252: RFmxInstrMXOptimizePathForSignalBandwidth Enumeration

- bundle_id: `rfmxinstr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxinstrmxoptimizepathforsignalbandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxinstrmxoptimizepathforsignalbandwidth.html
- document_id: `rfmxinstr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Optimizes RF path for the signal bandwidth that is centered on the IQ carrier frequency. SyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic enum RFmxInstrMXOptimizePathForSignalBandwidthMembersNameValueDescriptionDisabled0Disables the optimized path for signal bandwidth. Enabled1Enables the opt

### RFmxInstrMXOptimizePathForSignalBandwidth Enumeration

Optimizes RF path for the signal bandwidth that is centered on the IQ carrier frequency.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public enum RFmxInstrMXOptimizePathForSignalBandwidth

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Disabled | 0 | Disables the optimized path for signal bandwidth. |
| Enabled | 1 | Enables the optimized path for signal bandwidth. |
| Automatic | 2 | Automatically enables the optimized path based on other configurations. |

Parent topic:

NationalInstruments.RFmx.InstrMX

<!--NI_TOPIC bundle=rfmxinstr-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxinstrmxospdelayenabled.html language=enus -->
## TOPIC 00253: RFmxInstrMXOspDelayEnabled Enumeration

- bundle_id: `rfmxinstr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxinstrmxospdelayenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxinstrmxospdelayenabled.html
- document_id: `rfmxinstr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the digitizer OSP block to delay Reference Triggers, along with the data samples, moving through the OSP block. SyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic enum RFmxInstrMXOspDelayEnabledMembersNameValueDescriptionDisabled0Disables the method. Enabled1Enables

### RFmxInstrMXOspDelayEnabled Enumeration

Specifies whether to enable the digitizer OSP block to delay Reference Triggers, along with the data samples, moving through the OSP block.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public enum RFmxInstrMXOspDelayEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Disabled | 0 | Disables the method. |
| Enabled | 1 | Enables the method. |

Parent topic:

NationalInstruments.RFmx.InstrMX

<!--NI_TOPIC bundle=rfmxinstr-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxinstrmxoverflowerrorreporting.html language=enus -->
## TOPIC 00254: RFmxInstrMXOverflowErrorReporting Enumeration

- bundle_id: `rfmxinstr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxinstrmxoverflowerrorreporting.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxinstrmxoverflowerrorreporting.html
- document_id: `rfmxinstr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures error reporting for ADC and overflows occurred during onboard signal processing. Overflows lead to clipping of the waveform. SyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic enum RFmxInstrMXOverflowErrorReportingMembersNameValueDescriptionWarning0RFmx returns a warning when an ADC

### RFmxInstrMXOverflowErrorReporting Enumeration

Configures error reporting for ADC and overflows occurred during onboard signal processing. Overflows lead to clipping of the waveform.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public enum RFmxInstrMXOverflowErrorReporting

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Warning | 0 | RFmx returns a warning when an ADC or an onboard signal processing (OSP) overflow occurs. |
| Disabled | 1 | RFmx does not return an error or a warning when an ADC or OSP overflow occurs. |

Parent topic:

NationalInstruments.RFmx.InstrMX

<!--NI_TOPIC bundle=rfmxinstr-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxinstrmxpersonalities.html language=enus -->
## TOPIC 00255: RFmxInstrMXPersonalities Enumeration

- bundle_id: `rfmxinstr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxinstrmxpersonalities.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxinstrmxpersonalities.html
- document_id: `rfmxinstr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the personality of the signal if the signal exists. SyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic enum RFmxInstrMXPersonalitiesMembersNameValueDescriptionNone0x0Specifies that a signal does not exist. SpecAn0x1Specifies the SpecAn personality. Demod0x2Specifies the Demod personal

### RFmxInstrMXPersonalities Enumeration

Specifies the personality of the signal if the signal exists.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public enum RFmxInstrMXPersonalities

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0x0 | Specifies that a signal does not exist. |
| SpecAn | 0x1 | Specifies the SpecAn personality. |
| Demod | 0x2 | Specifies the Demod personality. |
| Lte | 0x4 | Specifies the LTE personality. |
| Gsm | 0x8 | Specifies the GSM personality. |
| Wcdma | 0x10 | Specifies the WCDMA personality. |
| Cdma2k | 0x20 | Specifies the CDMA2k personality. |
| Tdscdma | 0x40 | Specifies the TD-SCDMA personality. |
| Evdo | 0x80 | Specifies the EV-DO personality. |
| NR | 0x100 | Specifies the NR personality. |
| Wlan | 0x200 | Specifies the WLAN personality. |
| BT | 0x400 | Specifies the BT personality. |
| Vna | 0x1000 | Specifies the VNA personality. |
| Pulse | 0x800 | Specifies the Pulse personality. |
| Uwb | 0x2000 | Specifies the UWB personality. |
| All | int.MaxValue | Specifies all the personalities. |

Parent topic:

NationalInstruments.RFmx.InstrMX

<!--NI_TOPIC bundle=rfmxinstr-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxinstrmxpreampenabled.html language=enus -->
## TOPIC 00256: RFmxInstrMXPreampEnabled Enumeration

- bundle_id: `rfmxinstr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxinstrmxpreampenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxinstrmxpreampenabled.html
- document_id: `rfmxinstr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the RF preamplifier is enabled in the system. SyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic enum RFmxInstrMXPreampEnabledMembersNameValueDescriptionDisabled0Disables the RF preamplifier. Supported Devices: PXIe-5663/5663E/5665/5668. Enabled1Enables the RF preamplifier whe

### RFmxInstrMXPreampEnabled Enumeration

Specifies whether the RF preamplifier is enabled in the system.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public enum RFmxInstrMXPreampEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Disabled | 0 | Disables the RF preamplifier. Supported Devices: PXIe-5663/5663E/5665/5668. |
| Enabled | 1 | Enables the RF preamplifier when it is in the signal path and disables it when it is not in the signal path. Only devices with an RF preamplifier on the downconverter and an RF preselector support this option. Use the GetRFPreampPresent(string, out bool) method to determine whether the downconverter has a preamplifier. Supported Devices: PXIe-5663/5663E/5665/5668. |
| Automatic | 3 | Automatically enables the RF preamplifier based on the value of the reference level. Supported Devices: PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860. |

Parent topic:

NationalInstruments.RFmx.InstrMX

<!--NI_TOPIC bundle=rfmxinstr-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxinstrmxpropertyid.html language=enus -->
## TOPIC 00257: RFmxInstrMXPropertyId Enumeration

- bundle_id: `rfmxinstr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxinstrmxpropertyid.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxinstrmxpropertyid.html
- document_id: `rfmxinstr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies all the attribute identifiers. SyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic enum RFmxInstrMXPropertyIdMembersNameValueDescriptionFrequencyReferenceSource2Specifies the frequency reference source. FrequencyReferenceFrequency3Specifies the Reference Clock rate, when the Frequency

### RFmxInstrMXPropertyId Enumeration

Specifies all the attribute identifiers.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public enum RFmxInstrMXPropertyId

#### Members

| Name | Value | Description |
| --- | --- | --- |
| FrequencyReferenceSource | 2 | Specifies the frequency reference source. |
| FrequencyReferenceFrequency | 3 | Specifies the Reference Clock rate, when the Frequency Reference Source method is set to ClkIn or RefIn. This value is expressed in Hz. |
| RFAttenuationAuto | 4 | Specifies whether RFmx computes the RF attenuation. |
| RFAttenuationValue | 5 | Specifies the nominal attenuation setting for all attenuators before the first mixer in the RF signal chain. This value is expressed in dB. |
| MechanicalAttenuationAuto | 6 | Specifies whether RFmx chooses an attenuation setting based on the hardware settings. |
| MechanicalAttenuationValue | 7 | Specifies the level of mechanical attenuation for the RF path. This value is expressed in dB. |
| LO2ExportEnabled | 58 | Specifies whether to enable the LO2 OUT terminals in the installed devices. |
| TuningSpeed | 8 | Makes tradeoffs between tuning speed and phase noise. |
| FrequencySettlingUnits | 9 | Specifies the delay duration units and interpretation for LO settling. |
| FrequencySettling | 10 | Specifies the value used for LO frequency settling. |
| ChannelCoupling | 11 | Specifies whether the RF IN connector is AC- or DC-coupled on the downconverter. |
| DownconverterPreselectorEnabled | 12 | Specifies whether the tunable preselector is enabled on the downconverter. |
| DownconverterCenterFrequency | 13 | Enables in-band retuning and specifies the current frequency of the RF downconverter. This value is expressed in Hz. |
| PreampEnabled | 14 | Specifies whether the RF preamplifier is enabled in the system. |
| MixerLevelOffset | 0xF | Specifies the number of dB by which to adjust the device mixer level. |
| MixerLevel | 0x10 | Specifies the mixer level. This value is expressed in dBm. |
| IFOutputPowerLevelOffset | 17 | Specifies the power offset by which to adjust the default IF output power level. This value is expressed in dB. |
| LOFrequency | 60 | Specifies the LO signal frequency for the configured center frequency. This value is expressed in Hz. |
| LOSource | 59 | Specifies the local oscillator (LO) signal source used to downconvert the RF input signal. |
| LOInjectionSide | 18 | Enables in-band retuning and specifies the current frequency of the RF downconverter. This value is expressed in Hz. |
| PhaseOffset | 19 | Specifies the offset to apply to the initial I and Q phases. |
| DigitizerDitherEnabled | 21 | Specifies whether dithering is enabled on the digitizer. |
| FftWidth | 22 | Specifies the FFT width of the device. The FFT width is the effective bandwidth of the signal path during each signal acquisition. |
| OspDelayEnabled | 23 | Specifies whether to enable the digitizer OSP block to delay Reference Triggers, along with the data samples, moving through the OSP block. |
| DeviceTemperature | 24 | Returns the current temperature of the module. This value is expressed in degrees Celsius. |
| DigitizerTemperature | 25 | Returns the current temperature of the digitizer module. This value is expressed in degrees Celsius. |
| LOTemperature | 26 | Returns the current temperature of the LO module associated with the device. This value is expressed in degrees Celsius. |
| InstrumentFirmwareRevision | 27 | Returns a string containing the firmware revision information of the RF downconverter for the composite device you are currently using. |
| InstrumentModel | 28 | Returns a string that contains the model number or name of the RF device that you are currently using. |
| ModuleRevision | 29 | Returns the revision of the RF downconverter module. |
| SerialNumber | 30 | Returns the serial number of the RF downconverter module. |
| PreselectorPresent | 0x1F | Indicates whether a preselector is available on the RF downconverter module. |
| RFPreampPresent | 0x20 | Indicates whether an RF preamplifier is available on the RF downconverter module. |
| LOExportEnabled | 33 | Specifies whether to enable the LO OUT terminals on the installed devices. |
| FrequencyReferenceExportedTerminal | 34 | Specifies a comma-separated list of the terminals at which to export the frequency reference. |
| TriggerExportOutputTerminal | 35 | Specifies the destination terminal for the exported Reference Trigger. You can also choose not to export any signal. |
| TriggerTerminalName | 36 | Returns the fully qualified signal name as a string. |
| CleanerSpectrum | 37 | Specifies how to obtain the lowest noise floor or faster measurement speed. |
| RecommendedCenterFrequency | 57 | Returns the recommended center frequency of the RF signal. This value is expressed in Hz. This method is supported when 1. RFmxInstrMX(string, string) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(string[], string) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this property. |
| RecommendedAcquisitionType | 39 | Returns the recommended acquisition type for the last committed measurement configuration. This method is supported when 1. RFmxInstrMX(string, string) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(string[], string) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this property. |
| RecommendedNumberOfRecords | 40 | Returns the recommended number of records to acquire to complete measurement averaging. This method is supported when 1. RFmxInstrMX(string, string) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(string[], string) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this property. |
| RecommendedTriggerMinimumQuietTime | 41 | Returns the recommended minimum quiet time during which the signal level must be below the trigger value for triggering to occur. This value is expressed in seconds. This method is supported when 1. RFmxInstrMX(string, string) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(string[], string) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this property. |
| RecommendedIQAcquisitionTime | 42 | Returns the recommended acquisition time for I/Q acquisition. This value is expressed in seconds. This method is supported when 1. RFmxInstrMX(string, string) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(string[], string) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this property. |
| RecommendedIQMinimumSampleRate | 43 | Returns the recommended minimum sample rate for I/Q acquisition. This value is expressed in Hz. This method is supported when 1. RFmxInstrMX(string, string) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(string[], string) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this property. |
| RecommendedIQPreTriggerTime | 44 | Returns the recommended pretrigger time for I/Q acquisition. This value is expressed in seconds. This method is supported when 1. RFmxInstrMX(string, string) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(string[], string) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this property. |
| RecommendedSpectralAcquisitionSpan | 45 | Returns the recommended acquisition span for spectral acquisition. This value is expressed in Hz. This method is supported when 1. RFmxInstrMX(string, string) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(string[], string) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this property. |
| RecommendedSpectralFftWindow | 46 | Returns the recommended FFT window type for spectral acquisition. This method is supported when 1. RFmxInstrMX(string, string) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(string[], string) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this property. |
| RecommendedSpectralResolutionBandwidth | 47 | Returns the recommended FFT bin width for spectral acquisition. This value is expressed in Hz. This method is supported when 1. RFmxInstrMX(string, string) is called with option string "AnalysisOnly=1". 2. RFmxInstrMX(string[], string) is called with option string 'AnalysisOnly=1;MaxNumWfms:n'. Use 'instr(n)' as the selector string to read this property. |
| IFFilterBandwidth | 48 | Specifies the IF filter path bandwidth for your device configuration. |
| SubSpanOverlap | 50 | Specifies the maximum corner frequency of the high pass filter in the RF signal path. The device uses the highest frequency high-pass filter option below or equal to the value you specify and returns a coerced value. Specifying a value of 0 disables high pass filtering silly.For multispan acquisitions, the device uses the appropriate filter for each subspan during acquisition, depending on the details of your application and the value you specify. In multispan acquisition spectrum applications, this method returns the value you specified rather than a coerced value if multiple high-pass filters are used during the acquisition. |
| DownconverterGain | 52 | Returns the net signal gain for the device at the current RFmx settings and temperature. RFmx scales the acquired I/Q and spectrum data from the digitizer using the value of this method. |
| RecommendedIQMeasurementBandwidth | 51 | This enum value has been deprecated. |
| DownconverterFrequencyOffset | 53 | Specifies an offset from the center frequency value for the downconverter. Use this method to offset the measurement away from the LO leakage or DC Offset of analyzers that use a direct conversion architecture. You must set this method to half the bandwidth or span of the measurement + guardband. The guardband is needed to ensure that the LO leakage is not inside the analog or digital filter rolloffs. This value is expressed in Hz. |
| RFAttenuationStepSize | 54 | Specifies the step size for the RF attenuation level. This value is expressed in dB. The actual RF attenuation is coerced up to the next highest multiple of the specified step size. If the mechanical attenuators are not available to implement the coerced RF attenuation, the solid state attenuators are used. |
| LOLeakageAvoidanceEnabled | 55 | Specifies whether to reduce the effects of the instrument leakage by placing the LO outside the band of acquisition. |
| AmplitudeSettling | 56 | Specifies the amplitude settling accuracy value. This value is expressed in decibels. RFmx waits until the RF power attains the specified accuracy level after calling the RFmx Initiate function. |
| CommonModeLevel | 70 | Specifies the common-mode level presented at each differential input terminal. The common-mode level shifts both positive and negative terminals in the same direction. This must match the common-mode level of the device under test (DUT). This value is expressed in Volts. |
| SmuResourceName | 71 | Specifies the resource name assigned by Measurement and Automation Explorer (MAX) for NI Source Measure Units (SMU) which is used as the noise source power supply for Noise Figure (NF) measurement, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. SMU Resource Name can also be a logical IVI name. |
| SmuChannel | 72 | Specifies the output channel to be used for noise figure (NF) measurement in RFmx. |
| AutomaticSGSASharedLO | 74 | This enum value has been deprecated. |
| OverflowErrorReporting | 77 | Configures error reporting for ADC and overflows occurred during onboard signal processing. Overflows lead to clipping of the waveform. |
| LOInPower | 78 | Specifies the power level expected at the LO IN terminal when the SetLOSource(string, string) method is set to RFMXINSTR_VAL_LO_SOURCE_LO_IN. This value is expressed in dBm. |
| LOOutPower | 79 | Specifies the power level of the signal at the LO OUT terminal when the SetLOExportEnabled(string, bool) method is set to TRUE. This value is expressed in dBm. |
| LOPllFractionalMode | 90 | Specifies whether to use fractional mode for the LO phase-locked loop (PLL). |
| OptimizePathForSignalBandwidth | 91 | Optimizes RF path for the signal bandwidth that is centered on the IQ carrier frequency. |
| InputIsolationEnabled | 92 | Specifies whether input isolation is enabled. |
| LOVcoFrequencyStepSize | 80 | Specifies the step size for tuning the internal voltage-controlled oscillator (VCO) used to generate the LO signal. The valid values for LO1 include 1 Hz to 50 MHz and for LO2 include 1 Hz to 100 MHz. |
| ThermalCorrectionHeadroomRange | 94 | Specifies the expected thermal operating range of the instrument from the self-calibration temperature returned from the GetDeviceTemperature(string, out double) method. This value is expressed in degree Celsius. |
| LOFrequencyStepSize | 95 | Specifies the step size for tuning the LO phase-locked loop (PLL). |
| RFHighpassFilterFrequency | 49 | Specifies the maximum corner frequency of the high pass filter in the RF signal path. The device uses the highest frequency high-pass filter option below or equal to the value you specify and returns a coerced value. Specifying a value of 0 disables high pass filtering silly.For multispan acquisitions, the device uses the appropriate filter for each subspan during acquisition, depending on the details of your application and the value you specify. In multispan acquisition spectrum applications, this method returns the value you specified rather than a coerced value if multiple high-pass filters are used during the acquisition. |
| SelfCalibrationValidityCheck | 117 | Specifies whether RFmx validates the self-calibration data. |
| SelfCalibrationValidityCheckTimeInterval | 118 | Specifies the minimum time between two self calibration validity checks. This value is expressed in seconds. |
| StartTriggerType | 98 | Specifies whether the start trigger is a digital edge or a software trigger. |
| StartTriggerDigitalEdgeSource | 99 | Specifies the source terminal for the start trigger. This method is used only when you set the SetStartTriggerType(string, RFmxInstrMXStartTriggerType) method to DigitalEdge. |
| StartTriggerDigitalEdge | 100 | Specifies the active edge for the start trigger. This method is used only when you set the SetStartTriggerType(string, RFmxInstrMXStartTriggerType) method to DigitalEdge. |
| StartTriggerExportOutputTerminal | 101 | Specifies the destination terminal for the exported start trigger. |
| StartTriggerTerminalName | 102 | Returns the fully qualified signal name as a string. |
| AdvanceTriggerType | 103 | Specifies whether the advance trigger is a digital edge or a software trigger. |
| AdvanceTriggerDigitalEdgeSource | 104 | Specifies the source terminal for the advance trigger. |
| AdvanceTriggerExportOutputTerminal | 105 | Specifies the destination terminal for the exported advance trigger. |
| AdvanceTriggerTerminalName | 106 | Returns the fully qualified signal name as a string. |
| ReadyForStartEventOutputTerminal | 107 | Specifies the destination terminal for the Ready for Start event. |
| ReadyForStartEventTerminalName | 108 | Returns the fully qualified signal name as a string. |
| ReadyForAdvanceEventOutputTerminal | 109 | Specifies the destination terminal for the Ready for Advance event. |
| ReadyForAdvanceEventTerminalName | 110 | Returns the fully qualified signal name as a string. |
| ReadyForReferenceEventOutputTerminal | 111 | Specifies the destination terminal for the Ready for Reference event. |
| ReadyForReferenceEventTerminalName | 112 | Returns the fully qualified signal name as a string. |
| EndOfRecordEventOutputTerminal | 113 | Specifies the destination terminal for the End of Record event. |
| EndOfRecordEventTerminalName | 114 | Returns the fully qualified signal name as a string. |
| DoneEventOutputTerminal | 115 | Specifies the destination terminal for the Done event. |
| DoneEventTerminalName | 116 | Returns the fully qualified signal name as a string. |
| TemperatureReadInterval | 119 | Specifies the minimum time difference between temperature sensor readings. This value is expressed in seconds. |
| ThermalCorrectionTemperatureResolution | 120 | Specifies the temperature change required before RFmx recalculates the thermal correction settings when entering the running state. This value is expressed in degree Celsius. |
| NumberOfRawIQRecords | 0x80 | Gets the number of raw IQ records to acquire to complete measurement averaging. |
| DigitalGain | 84 | Specifies the scaling factor applied to the time-domain voltage data in the digitizer. This value is expressed in dB. |
| LOSharingMode | 68 | Specifies the RFmx session with the respective LO sharing mode. |
| NumberOfLOSharingGroups | 97 | Specifies the RFmx session with the number of LO sharing groups. |
| LOSplitterLossFrequency | 184 | Specifies the frequencies corresponding to the insertion loss inherent to the RF Splitter, as specified by the SetLOSplitterLoss(string, double[]) method. This value is expressed in Hz. |
| LOSplitterLoss | 185 | Specifies an array of the insertion losses inherent to the RF Splitter. This value is expressed in dB. |
| LoadOptions | 163 | Specifies the configurations to skip while loading from a file using the LoadConfigurations(string) method |

Parent topic:

NationalInstruments.RFmx.InstrMX

<!--NI_TOPIC bundle=rfmxinstr-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxinstrmxselfcalibratesteps.html language=enus -->
## TOPIC 00258: RFmxInstrMXSelfCalibrateSteps Enumeration

- bundle_id: `rfmxinstr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxinstrmxselfcalibratesteps.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxinstrmxselfcalibratesteps.html
- document_id: `rfmxinstr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the self-calibration step. SyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic enum RFmxInstrMXSelfCalibrateStepsMembersNameValueDescriptionNone0x0A value of None specifies that all calibration steps are performed. PreselectorAlignment0x1Selects/Omits the Preselector Alignment self-cal

### RFmxInstrMXSelfCalibrateSteps Enumeration

Specifies the self-calibration step.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public enum RFmxInstrMXSelfCalibrateSteps

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0x0 | A value of None specifies that all calibration steps are performed. |
| PreselectorAlignment | 0x1 | Selects/Omits the Preselector Alignment self-calibration step. |
| GainReference | 0x2 | Selects/Omits the Gain Reference self-calibration step. |
| IFFlatness | 0x4 | Selects/Omits the IF Flatness self-calibration step. |
| DigitizerSelfcal | 0x8 | Selects/Omits the Digitizer Self Cal self-calibration step. |
| LOSelfCal | 0x10 | Selects/Omits the LO Self Cal self-calibration step. |
| AmplitudeAccuracy | 0x20 | Selects/Omits the Amplitude Accuracy self-calibration step. |
| ResidualLOPower | 0x40 | Selects/Omits the Residual LO Power self-calibration step. |
| ImageSuppression | 0x80 | Selects/Omits the Image Suppression self-calibration step. |
| SynthesizerAlignment | 0x100 | Selects/Omits the Synthesizer Alignment self-calibration step. |
| DCOffset | 0x200 | Selects/Omits the DC Offset self-calibration step. |

Parent topic:

NationalInstruments.RFmx.InstrMX

<!--NI_TOPIC bundle=rfmxinstr-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxinstrmxstarttriggertype.html language=enus -->
## TOPIC 00259: RFmxInstrMXStartTriggerType Enumeration

- bundle_id: `rfmxinstr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxinstrmxstarttriggertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxinstrmxstarttriggertype.html
- document_id: `rfmxinstr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the start trigger is a digital edge or a software trigger. SyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic enum RFmxInstrMXStartTriggerTypeMembersNameValueDescriptionNone0No start trigger is configured. DigitalEdge1The start trigger is not asserted until a digital edge is d

### RFmxInstrMXStartTriggerType Enumeration

Specifies whether the start trigger is a digital edge or a software trigger.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public enum RFmxInstrMXStartTriggerType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0 | No start trigger is configured. |
| DigitalEdge | 1 | The start trigger is not asserted until a digital edge is detected. The source of the digital edge is specified by the SetStartTriggerDigitalEdgeSource(string, string) method. |
| Software | 3 | The start trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling the RFmxInstr_SendSoftwareEdgeTrigger function. |

Parent topic:

NationalInstruments.RFmx.InstrMX
