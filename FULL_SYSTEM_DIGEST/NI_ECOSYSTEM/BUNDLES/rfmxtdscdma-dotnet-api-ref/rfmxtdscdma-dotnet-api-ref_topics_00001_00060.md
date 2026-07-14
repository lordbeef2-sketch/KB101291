# NI DOCUMENT BUNDLE: rfmxtdscdma-dotnet-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxtdscdma-dotnet-api-ref start=1 end=60 -->
<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamx-clearallnamedresults__string.html language=enus -->
## TOPIC 00001: ClearAllNamedResults(string)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamx-clearallnamedresults__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamx-clearallnamedresults__string.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all results for the current signal instance.SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int ClearAllNamedResults(string selectorString)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when creating the signal configuration is

### ClearAllNamedResults(string)

Clears all results for the current signal instance.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int ClearAllNamedResults(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMX Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamx-configureexternalattenuation__string-double.html language=enus -->
## TOPIC 00002: ConfigureExternalAttenuation(string, double)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamx-configureexternalattenuation__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamx-configureexternalattenuation__string-double.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies external attenuation to be considered by RFmx TD-SCDMA measurements, such as the attenuation of a switch or cable connected to the signal analyzer RF IN connector.SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int ConfigureExternalAttenuation(string selectorString, double extern

### ConfigureExternalAttenuation(string, double)

Specifies external attenuation to be considered by RFmx TD-SCDMA measurements, such as the attenuation of a switch or cable connected to the signal analyzer RF IN connector.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int ConfigureExternalAttenuation(string selectorString, double externalAttenuation)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| externalAttenuation | double | Specifies the level of external attenuation that is considered by the selected measurement. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMX Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamx-configurefrequency__string-double.html language=enus -->
## TOPIC 00003: ConfigureFrequency(string, double)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamx-configurefrequency__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamx-configurefrequency__string-double.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency.SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int ConfigureFrequency(string selectorString, double centerFrequency)ParametersNameTypeDescriptionselectorStringstringPass an e

### ConfigureFrequency(string, double)

Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int ConfigureFrequency(string selectorString, double centerFrequency)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| centerFrequency | double | Specifies the carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMX Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamx-configurenumberofchannels__string-int.html language=enus -->
## TOPIC 00004: ConfigureNumberOfChannels(string, int)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamx-configurenumberofchannels__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamx-configurenumberofchannels__string-int.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of channels for the user-defined channel configuration when the channel configuration mode is set to userDefined.SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int ConfigureNumberOfChannels(string selectorString, int numberOfChannels)ParametersNameTypeDescriptionsele

### ConfigureNumberOfChannels(string, int)

Configures the number of channels for the user-defined channel configuration when the channel configuration mode is set to *userDefined*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int ConfigureNumberOfChannels(string selectorString, int numberOfChannels)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| numberOfChannels | int | Specifies the number of user-defined channels. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMX Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamx-configurepilot__string-int.html language=enus -->
## TOPIC 00005: ConfigurePilot(string, int)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamx-configurepilot__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamx-configurepilot__string-int.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the pilot code of the TD-SCDMA signal.SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int ConfigurePilot(string selectorString, int pilotCode)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when creating the signal configurat

### ConfigurePilot(string, int)

Configures the pilot code of the TD-SCDMA signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int ConfigurePilot(string selectorString, int pilotCode)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| pilotCode | int | Specifies the SYNC-UL code used by the uplink pilot time slot (UpPTS). This code is used when the SetSynchronizationMode(string, RFmxTdscdmaMXModAccSynchronizationMode) method is set to Subframe, or the SetSlotType(string, RFmxTdscdmaMXModAccSlotType) method is set to Pilot. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMX Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamx-configurereferencelevel__string-double.html language=enus -->
## TOPIC 00006: ConfigureReferenceLevel(string, double)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamx-configurereferencelevel__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamx-configurereferencelevel__string-double.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference level. The reference level represents the maximum expected power of an input RF signal.SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int ConfigureReferenceLevel(string selectorString, double referenceLevel)ParametersNameTypeDescriptionselectorStringstringPass an

### ConfigureReferenceLevel(string, double)

Configures the reference level. The reference level represents the maximum expected power of an input RF signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int ConfigureReferenceLevel(string selectorString, double referenceLevel)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| referenceLevel | double | Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMX Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamx.html language=enus -->
## TOPIC 00007: RFmxTdscdmaMX Class

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamx.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamx.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines a root class which is used to identify and control TDSCDMA signal configuration. Derives fromISignalConfigurationIDisposableSyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic class RFmxTdscdmaMX : ISignalConfiguration, IDisposablePropertiesNameDescriptionAcpGets the RFmxTdscdmaMXAcp i

### RFmxTdscdmaMX Class

Defines a root class which is used to identify and control TDSCDMA signal configuration.

#### Derives from

- ISignalConfiguration
- IDisposable

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public class RFmxTdscdmaMX : ISignalConfiguration, IDisposable

#### Properties

| Name | Description |
| --- | --- |
| Acp | Gets the RFmxTdscdmaMXAcp instance that represents the ACP measurement. |
| Cda | Gets the RFmxTdscdmaMXCda instance that represents the CDA measurement. |
| Chp | Gets the RFmxTdscdmaMXChp instance that represents the CHP measurement. |
| IsDisposed | Gets a value that indicates whether the signal has been disposed. |
| ModAcc | Gets the RFmxTdscdmaMXModAcc instance that represents the ModAcc measurement. |
| Obw | Gets the RFmxTdscdmaMXObw instance that represents the OBW measurement. |
| Pvt | Gets the RFmxTdscdmaMXPvt instance that represents the PVT measurement. |
| Sem | Gets the RFmxTdscdmaMXSem instance that represents the SEM measurement. |
| SignalConfigurationName | Gets the signal configuration name. |
| SignalConfigurationType | Gets the Type object for RFmxTdscdmaMX. |
| SlotPower | Gets the RFmxTdscdmaMXSlotPower instance that represents the SlotPower measurement. |

#### Methods

| Name | Description |
| --- | --- |
| AbortMeasurements(string) | Stops the acquisition and measurements associated with the signal instance that you specify in the selectorString parameter. The acquisition and measurements were previously initiated by the Initiate(string, string) method or measurement read methods. Calling this method is optional, unless you want to stop a measurement before it is complete. This method executes even if there is an incoming error. |
| AnalyzeIQ1Waveform(string, string, ComplexWaveform< ComplexSingle >, bool, long) | Performs the enabled measurements on the I/Q complex waveform that you specify in the IQ parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods. Use this method only if the RFmxInstrMX.GetRecommendedAcquisitionTypeMethod method value is either IQ or IQorSpectral. Query the Recommended Acquisition Type method from the RFmx driver after calling the RFmxTDSCDMA Commit method. |
| AnalyzeSpectrum1Waveform(string, string, Spectrum< float >, bool, long) | Performs the enabled measurements on the Spectrum waveform that you specify in the spectrum parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods. Use this method only if the RFmxInstrMX.GetRecommendedAcquisitionTypeMethod method value is either spectral or IQorSpectral. Query the Recommended Acquisition Type method from the RFmx driver after calling the RFmxTDSCDMA Commit method. |
| AutoLevel(string, double, out double) | Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level method. Use this method to calculate an approximate setting for the reference level. |
| CheckMeasurementStatus(string, out bool) | Checks the status of the measurement. Use this method to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
| ClearAllNamedResults(string) | Clears all results for the current signal instance. |
| ClearNamedResult(string) | Clears a result instance specified by the result name in the selectorString parameter. |
| CloneSignalConfiguration(string, out RFmxTdscdmaMX) | Creates a new instance of a signal by copying all the method values from an existing signal instance. |
| Commit(string) | Commits settings to the hardware. Calling this method is optional. RFmxTDSCDMA commits settings to the hardware when you call the Initiate(string, string) method. |
| ConfigureChannelConfigurationMode(string, RFmxTdscdmaMXChannelConfigurationMode) | Configures RFmx TD-SCDMA to detect the channels automatically or to use a specified channel configuration. |
| ConfigureDigitalEdgeTrigger(string, string, RFmxTdscdmaMXDigitalEdgeTriggerEdge, double, bool) | Configures the device to wait for a digital edge trigger and then marks a reference point within the record. |
| ConfigureExternalAttenuation(string, double) | Specifies external attenuation to be considered by RFmx TD-SCDMA measurements, such as the attenuation of a switch or cable connected to the signal analyzer RF IN connector. |
| ConfigureFrequency(string, double) | Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. |
| ConfigureFrequencyChannelNumber(string, int) | Configures the carrier frequency of the RF signal to acquire according to the given channel number. The signal analyzer tunes to this frequency. |
| ConfigureIQPowerEdgeTrigger(string, string, RFmxTdscdmaMXIQPowerEdgeTriggerSlope, double, double, RFmxTdscdmaMXTriggerMinimumQuietTimeMode, double, RFmxTdscdmaMXIQPowerEdgeTriggerLevelType, bool) | Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record. |
| ConfigureMidamble(string, RFmxTdscdmaMXMidambleAutoDetectionMode, int, int) | This method is now deprecated, please use the RFmxTDSCDMA Configure Midamble Shift method in the place of this method. |
| ConfigureMidambleShift(string, RFmxTdscdmaMXMidambleAutoDetectionMode, int, int) | Configures the midambleAutoDetectionMode, maximumNumberOfUsers, and MidambleShift parameters. |
| ConfigureNumberOfChannels(string, int) | Configures the number of channels for the user-defined channel configuration when the channel configuration mode is set to userDefined. |
| ConfigurePilot(string, int) | Configures the pilot code of the TD-SCDMA signal. |
| ConfigureReferenceLevel(string, double) | Configures the reference level. The reference level represents the maximum expected power of an input RF signal. |
| ConfigureRF(string, double, double, double) | Configures the RF methods of the signal specified by the selectorString parameter. |
| ConfigureSoftwareEdgeTrigger(string, double, bool) | Configures the device to wait for a software trigger to mark a reference point within the record. |
| ConfigureUplinkScramblingCode(string, int) | Configures the scrambling code used for the uplink transmission. |
| ConfigureUserDefinedChannel(string, int, RFmxTdscdmaMXChannelType, int, RFmxTdscdmaMXModulationType, int) | Configures an individual user-defined channel when the channel configuration mode is set to userDefined. Use "<span class="monospace">channel</span><span class="monospace">(n)</span>" as the selector string to configure this method. A channel configuration is defined by the slot index it refers to, the channel type, and the modulation type. |
| ConfigureUserDefinedChannelArray(string, int[], RFmxTdscdmaMXChannelType[], int[], RFmxTdscdmaMXModulationType[], int[]) | Configures all user-defined channels when the channel configuration mode is set to userDefined. Use equal-sized arrays for slotIndex, channelType, and modulationType. You can configure up to two channels for the same index for multi-code transmission. |
| DeleteSignalConfiguration() | Deletes an instance of a signal. |
| DisableTrigger(string) | Configures the device to not wait for a trigger to mark a reference point within a record. This method defines the signal triggering as immediate. |
| Dispose() | Deletes the signal configuration if it is not the default signal configuration and clears any trace of the current signal configuration, if any. |
| GetAllNamedResultNames(string, out string[], out bool) | Returns all the named result names of the current signal instance. |
| GetAttributeBool(string, int, out bool) | Gets the value of a Bool attribute. |
| GetAttributeDouble(string, int, out double) | Gets the value of a Double attribute. |
| GetAttributeInt(string, int, out int) | Gets the value of an RFmx 32-bit integer (int32) attribute. |
| GetAttributeString(string, int, out string) | Gets the value of a of an RFmx string. |
| GetAutoLevelInitialReferenceLevel(string, out double) | Gets the initial reference level that the AutoLevel(string, double, out double) function uses to estimate the peak power of the input signal. This value is expressed in dBm. |
| GetCenterFrequency(string, out double) | Gets the carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. This value is expressed in Hz. |
| GetChannelConfigurationMode(string, out RFmxTdscdmaMXChannelConfigurationMode) | Gets whether to detect the channels automatically or to use a specified channel configuration. |
| GetChannelizationCode(string, out int) | Gets the channelization code of the user-defined channel. This method is used only when you set the SetChannelConfigurationMode(string, RFmxTdscdmaMXChannelConfigurationMode) method to UserDefined. Use "channel(n)" as the selector string to configure or read this method. |
| GetChannelType(string, out RFmxTdscdmaMXChannelType) | Gets the channel type of the user-defined channel. This method is used only when you set the SetChannelConfigurationMode(string, RFmxTdscdmaMXChannelConfigurationMode) method to UserDefined. Use "channel(n)" as the selector string to configure or read this method. |
| GetDigitalEdgeTriggerEdge(string, out RFmxTdscdmaMXDigitalEdgeTriggerEdge) | Gets the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxTdscdmaMXTriggerType) method to DigitalEdge. |
| GetDigitalEdgeTriggerSource(string, out string) | Gets the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(string, RFmxTdscdmaMXTriggerType) method to DigitalEdge. |
| GetError(out int, out string) | Gets the latest error code and description. |
| GetErrorString(int, out string) | Converts the status code returned by an RFmxTDSCDMA function into a string. |
| GetExternalAttenuation(string, out double) | Gets the level of external attenuation that is considered by the selected measurement. This value is expressed in dB. |
| GetIQPowerEdgeTriggerLevel(string, out double) | Gets the threshold above or below which the signal analyzer triggers, depending on the value of the SetIQPowerEdgeTriggerSlope(string, RFmxTdscdmaMXIQPowerEdgeTriggerSlope) method. This value is expressed in dB when the SetIQPowerEdgeTriggerLevelType(string, RFmxTdscdmaMXIQPowerEdgeTriggerLevelType) method is set to Relative or in dBm when the IQ Power Edge Level Type method is set to Absolute. |
| GetIQPowerEdgeTriggerLevelType(string, out RFmxTdscdmaMXIQPowerEdgeTriggerLevelType) | Gets the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. This method is used only when you set the SetTriggerType(string, RFmxTdscdmaMXTriggerType) method to IQPowerEdge. |
| GetIQPowerEdgeTriggerSlope(string, out RFmxTdscdmaMXIQPowerEdgeTriggerSlope) | Gets whether the device asserts the trigger when the signal power is rising or when the signal power is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This method is used only when you set the SetTriggerType(string, RFmxTdscdmaMXTriggerType) method to IQPowerEdge. |
| GetIQPowerEdgeTriggerSource(string, out string) | Gets the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(string, RFmxTdscdmaMXTriggerType) method to IQPowerEdge. |
| GetLimitedConfigurationChange(string, out RFmxTdscdmaMXLimitedConfigurationChange) | Gets the set of properties that are considered by RFmx in the locked signal configuration state. |
| GetMaximumNumberOfUsers(string, out int) | Configures the maximum number of users. |
| GetMidambleAutoDetectionMode(string, out RFmxTdscdmaMXMidambleAutoDetectionMode) | Gets the midamble auto detection mode. |
| GetMidambleCode(string, out int) | Gets the midamble code. |
| GetMidambleShift(string, out int) | Gets the midamble shift used when you set the SetMidambleAutoDetectionMode(string, RFmxTdscdmaMXMidambleAutoDetectionMode) method to Off. This value is expressed in chips. |
| GetModulationType(string, out RFmxTdscdmaMXModulationType) | Gets the modulation type of the user-defined channel. This method is used only when you set the SetChannelConfigurationMode(string, RFmxTdscdmaMXChannelConfigurationMode) method to UserDefined. Use "channel(n)" as the selector string to configure or read this method. |
| GetNumberOfChannels(string, out int) | Gets the number of user-defined channels. This method is used only when you set the SetChannelConfigurationMode(string, RFmxTdscdmaMXChannelConfigurationMode) method to UserDefined. |
| GetPilotCode(string, out int) | Gets the SYNC-UL code used by the uplink pilot time slot (UpPTS). This method is used when the SetSynchronizationMode(string, RFmxTdscdmaMXModAccSynchronizationMode) method is set to Subframe, or the SetSlotType(string, RFmxTdscdmaMXModAccSlotType) method is set to Pilot. |
| GetReferenceLevel(string, out double) | Gets the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
| GetReferenceLevelHeadroom(string, out double) | Gets the margin RFmx adds to the Reference Level method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input signal remains within the reference level plus the reference level headroom. If you know the input power of the signal precisely or previously included the margin in the reference level, you could improve the signal-to-noise ratio by reducing the reference level headroom. Default values PXIe-5668: 6 dB PXIe-5830/5831/5832/5841/5842/5860: 1 dB PXIe-5840: 0 dB Supported devices: PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860. |
| GetResultFetchTimeout(string, out double) | Gets the time to wait before results are available in the RFmx driver. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx driver waits until the measurement is complete. |
| GetSelectedPorts(string, out string) | Gets the instrument port to be used by the measurement. Valid values PXIe-5820/5840: "" (empty string) PXIe-5830: if0, if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Default values PXIe-5820/5840: "" (empty string) PXIe-5830/5831/5832: if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Supported devices: PXIe-5820/5830/5831/5832/5840 </x></x> |
| GetSlotFormat(string, out int) | Gets the spreading factor, the number of TFCI code words, the number of transmit power control bits, and the number of synchronization shift bits. This method is used only when you set the SetChannelConfigurationMode(string, RFmxTdscdmaMXChannelConfigurationMode) method to UserDefined. Use "channel(n)" as the selector string to configure or read this method. |
| GetSlotIndex(string, out int) | Gets the slot index of the user-defined channel. This method is used only when you set the SetChannelConfigurationMode(string, RFmxTdscdmaMXChannelConfigurationMode) method to UserDefined. Use "channel(n)" as the selector string to configure or read this method. |
| GetTriggerDelay(string, out double) | Gets the trigger delay time. This value is expressed in seconds. |
| GetTriggerMinimumQuietTimeDuration(string, out double) | Gets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the SetIQPowerEdgeTriggerSlope(string, RFmxTdscdmaMXIQPowerEdgeTriggerSlope) method to Rising, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope method to Falling, the signal is quiet above the trigger level. |
| GetTriggerMinimumQuietTimeMode(string, out RFmxTdscdmaMXTriggerMinimumQuietTimeMode) | Gets whether the measurement calculates the minimum quiet time used for triggering. |
| GetTriggerType(string, out RFmxTdscdmaMXTriggerType) | Gets the trigger type. |
| GetUplinkScramblingCode(string, out int) | Gets the scrambling code and the basic midamble code for uplink transmission. |
| GetWarning(out int, out string) | Gets the latest warning code and description. |
| Initiate(string, string) | Initiates all enabled measurements. Call this method after configuring the signal and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the fetch methods or result methods. To get the status of measurements, use the WaitForMeasurementComplete(string, double) method or the CheckMeasurementStatus(string, out bool) method. |
| ResetAttribute(string, RFmxTdscdmaMXPropertyId) | Resets the attribute to its default value. |
| ResetToDefault(string) | Resets a signal to the default values. This method disables all the external attenuation tables in all calibration planes. |
| SelectMeasurements(string, RFmxTdscdmaMXMeasurementTypes, bool) | Specifies the measurements that you want to enable. |
| SendSoftwareEdgeTrigger() | Sends a trigger to the device when you use the RFmxTDSCDMA_CfgTrigger method to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this method to override a hardware trigger. |
| SetAttributeBool(string, int, bool) | Sets the value of a Bool attribute. |
| SetAttributeDouble(string, int, double) | Sets the value of a Double attribute. |
| SetAttributeInt(string, int, int) | Sets the value of a Int attribute. |
| SetAttributeString(string, int, string) | Sets the value of a String attribute. |
| SetAutoLevelInitialReferenceLevel(string, double) | Sets the initial reference level that the AutoLevel(string, double, out double) function uses to estimate the peak power of the input signal. This value is expressed in dBm. |
| SetCenterFrequency(string, double) | Sets the carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. This value is expressed in Hz. |
| SetChannelConfigurationMode(string, RFmxTdscdmaMXChannelConfigurationMode) | Sets whether to detect the channels automatically or to use a specified channel configuration. |
| SetChannelizationCode(string, int) | Sets the channelization code of the user-defined channel. This method is used only when you set the SetChannelConfigurationMode(string, RFmxTdscdmaMXChannelConfigurationMode) method to UserDefined. Use "channel(n)" as the selector string to configure or read this method. |
| SetChannelType(string, RFmxTdscdmaMXChannelType) | Sets the channel type of the user-defined channel. This method is used only when you set the SetChannelConfigurationMode(string, RFmxTdscdmaMXChannelConfigurationMode) method to UserDefined. Use "channel(n)" as the selector string to configure or read this method. |
| SetDigitalEdgeTriggerEdge(string, RFmxTdscdmaMXDigitalEdgeTriggerEdge) | Sets the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxTdscdmaMXTriggerType) method to DigitalEdge. |
| SetDigitalEdgeTriggerSource(string, string) | Sets the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(string, RFmxTdscdmaMXTriggerType) method to DigitalEdge. |
| SetExternalAttenuation(string, double) | Sets the level of external attenuation that is considered by the selected measurement. This value is expressed in dB. |
| SetIQPowerEdgeTriggerLevel(string, double) | Sets the threshold above or below which the signal analyzer triggers, depending on the value of the SetIQPowerEdgeTriggerSlope(string, RFmxTdscdmaMXIQPowerEdgeTriggerSlope) method. This value is expressed in dB when the SetIQPowerEdgeTriggerLevelType(string, RFmxTdscdmaMXIQPowerEdgeTriggerLevelType) method is set to Relative or in dBm when the IQ Power Edge Level Type method is set to Absolute. |
| SetIQPowerEdgeTriggerLevelType(string, RFmxTdscdmaMXIQPowerEdgeTriggerLevelType) | Sets the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. This method is used only when you set the SetTriggerType(string, RFmxTdscdmaMXTriggerType) method to IQPowerEdge. |
| SetIQPowerEdgeTriggerSlope(string, RFmxTdscdmaMXIQPowerEdgeTriggerSlope) | Sets whether the device asserts the trigger when the signal power is rising or when the signal power is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This method is used only when you set the SetTriggerType(string, RFmxTdscdmaMXTriggerType) method to IQPowerEdge. |
| SetIQPowerEdgeTriggerSource(string, string) | Sets the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(string, RFmxTdscdmaMXTriggerType) method to IQPowerEdge. |
| SetLimitedConfigurationChange(string, RFmxTdscdmaMXLimitedConfigurationChange) | Sets the set of properties that are considered by RFmx in the locked signal configuration state. |
| SetMaximumNumberOfUsers(string, int) | Configures the maximum number of users. |
| SetMidambleAutoDetectionMode(string, RFmxTdscdmaMXMidambleAutoDetectionMode) | Sets the midamble auto detection mode. |
| SetMidambleCode(string, int) | Sets the midamble code. |
| SetMidambleShift(string, int) | Sets the midamble shift used when you set the SetMidambleAutoDetectionMode(string, RFmxTdscdmaMXMidambleAutoDetectionMode) method to Off. This value is expressed in chips. |
| SetModulationType(string, RFmxTdscdmaMXModulationType) | Sets the modulation type of the user-defined channel. This method is used only when you set the SetChannelConfigurationMode(string, RFmxTdscdmaMXChannelConfigurationMode) method to UserDefined. Use "channel(n)" as the selector string to configure or read this method. |
| SetNumberOfChannels(string, int) | Sets the number of user-defined channels. This method is used only when you set the SetChannelConfigurationMode(string, RFmxTdscdmaMXChannelConfigurationMode) method to UserDefined. |
| SetPilotCode(string, int) | Sets the SYNC-UL code used by the uplink pilot time slot (UpPTS). This method is used when the SetSynchronizationMode(string, RFmxTdscdmaMXModAccSynchronizationMode) method is set to Subframe, or the SetSlotType(string, RFmxTdscdmaMXModAccSlotType) method is set to Pilot. |
| SetReferenceLevel(string, double) | Sets the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
| SetReferenceLevelHeadroom(string, double) | Sets the margin RFmx adds to the Reference Level method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input signal remains within the reference level plus the reference level headroom. If you know the input power of the signal precisely or previously included the margin in the reference level, you could improve the signal-to-noise ratio by reducing the reference level headroom. Default values PXIe-5668: 6 dB PXIe-5830/5831/5832/5841/5842/5860: 1 dB PXIe-5840: 0 dB Supported devices: PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860. |
| SetResultFetchTimeout(string, double) | Sets the time to wait before results are available in the RFmx driver. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx driver waits until the measurement is complete. |
| SetSelectedPorts(string, string) | Sets the instrument port to be used by the measurement. Valid values PXIe-5820/5840: "" (empty string) PXIe-5830: if0, if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Default values PXIe-5820/5840: "" (empty string) PXIe-5830/5831/5832: if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Supported devices: PXIe-5820/5830/5831/5832/5840 </x></x> |
| SetSlotFormat(string, int) | Sets the spreading factor, the number of TFCI code words, the number of transmit power control bits, and the number of synchronization shift bits. This method is used only when you set the SetChannelConfigurationMode(string, RFmxTdscdmaMXChannelConfigurationMode) method to UserDefined. Use "channel(n)" as the selector string to configure or read this method. |
| SetSlotIndex(string, int) | Sets the slot index of the user-defined channel. This method is used only when you set the SetChannelConfigurationMode(string, RFmxTdscdmaMXChannelConfigurationMode) method to UserDefined. Use "channel(n)" as the selector string to configure or read this method. |
| SetTriggerDelay(string, double) | Sets the trigger delay time. This value is expressed in seconds. |
| SetTriggerMinimumQuietTimeDuration(string, double) | Sets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the SetIQPowerEdgeTriggerSlope(string, RFmxTdscdmaMXIQPowerEdgeTriggerSlope) method to Rising, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope method to Falling, the signal is quiet above the trigger level. |
| SetTriggerMinimumQuietTimeMode(string, RFmxTdscdmaMXTriggerMinimumQuietTimeMode) | Sets whether the measurement calculates the minimum quiet time used for triggering. |
| SetTriggerType(string, RFmxTdscdmaMXTriggerType) | Sets the trigger type. |
| SetUplinkScramblingCode(string, int) | Sets the scrambling code and the basic midamble code for uplink transmission. |
| WaitForMeasurementComplete(string, double) | Waits for the specified number of seconds for all the measurements to complete. |
| BuildChannelString(string, int) | Creates a selector string to use with channel-specific configuration or fetch methods and methods. Refer to the Selector String topic for information about the string syntax for named signals. |
| BuildOffsetString(string, int) | Creates the offset string to use as the selector string with spectral emissions mask (SEM) and adjacent channel power (ACP) offset configuration or fetch methods and methods. Refer to the Selector String topic for information about the string syntax for named signals. |
| BuildResultString(string) | Creates selector string for use with configuration or fetch. |
| BuildSegmentString(string, int) | Creates the segment string to use as the selector string with the power versus time (PVT) segment configuration or fetch methods and methods. Refer to the Selector String topic for information about the string syntax for named signals. |

Parent topic:

NationalInstruments.RFmx.TdscdmaMX

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacp-configuration.html language=enus -->
## TOPIC 00008: Configuration

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacp-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacp-configuration.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxTdscdmaMXAcpConfiguration instance that provides methods to configure the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic RFmxTdscdmaMXAcpConfiguration Configuration { get; }

### Configuration

Gets the [RFmxTdscdmaMXAcpConfiguration](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration.html) instance that provides methods to configure the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public [RFmxTdscdmaMXAcpConfiguration](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration.html) Configuration { get; }

Parent topic:

RFmxTdscdmaMXAcp Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacp.html language=enus -->
## TOPIC 00009: RFmxTdscdmaMXAcp Class

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacp.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the ACP measurement. Derives fromRFmxTdscdmaMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic class RFmxTdscdmaMXAcp : RFmxTdscdmaMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxTdscdmaMXAcpConfiguration instance that provides methods to configure the ACP

### RFmxTdscdmaMXAcp Class

Represents the ACP measurement.

#### Derives from

- RFmxTdscdmaMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public class RFmxTdscdmaMXAcp : RFmxTdscdmaMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxTdscdmaMXAcpConfiguration instance that provides methods to configure the ACP measurement. |
| Results | Gets the RFmxTdscdmaMXAcpResults instance that provides methods to fetch and read the ACP measurement results. |

Parent topic:

NationalInstruments.RFmx.TdscdmaMX

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-configurerbwfilter__string-rfmxtdscdmamxacprbwautobandwidth-double-rfmxtdscdmamxacprbwfiltertype.html language=enus -->
## TOPIC 00010: ConfigureRbwFilter(string, RFmxTdscdmaMXAcpRbwAutoBandwidth, double, RFmxTdscdmaMXAcpRbwFilterType)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-configurerbwfilter__string-rfmxtdscdmamxacprbwautobandwidth-double-rfmxtdscdmamxacprbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-configurerbwfilter__string-rfmxtdscdmamxacprbwautobandwidth-double-rfmxtdscdmamxacprbwfiltertype.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RBW filter.SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int ConfigureRbwFilter(string selectorString, RFmxTdscdmaMXAcpRbwAutoBandwidth rbwAuto, double rbw, RFmxTdscdmaMXAcpRbwFilterType rbwFilterType)ParametersNameTypeDescriptionselectorStringstringPass an empty string. T

### ConfigureRbwFilter(string, RFmxTdscdmaMXAcpRbwAutoBandwidth, double, RFmxTdscdmaMXAcpRbwFilterType)

Configures the RBW filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int ConfigureRbwFilter(string selectorString, RFmxTdscdmaMXAcpRbwAutoBandwidth rbwAuto, double rbw, RFmxTdscdmaMXAcpRbwFilterType rbwFilterType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| rbwAuto | RFmxTdscdmaMXAcpRbwAutoBandwidth | Specifies whether the measurement computes the RBW. |
| rbw | double | Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the rbwAuto parameter to False. This value is expressed in Hz. |
| rbwFilterType | RFmxTdscdmaMXAcpRbwFilterType | Specifies the shape of the digital RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-configuresweeptime__string-rfmxtdscdmamxacpsweeptimeauto-double.html language=enus -->
## TOPIC 00011: ConfigureSweepTime(string, RFmxTdscdmaMXAcpSweepTimeAuto, double)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-configuresweeptime__string-rfmxtdscdmamxacpsweeptimeauto-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-configuresweeptime__string-rfmxtdscdmamxacpsweeptimeauto-double.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time.SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int ConfigureSweepTime(string selectorString, RFmxTdscdmaMXAcpSweepTimeAuto sweepTimeAuto, double sweepTimeInterval)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passe

### ConfigureSweepTime(string, RFmxTdscdmaMXAcpSweepTimeAuto, double)

Configures the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int ConfigureSweepTime(string selectorString, RFmxTdscdmaMXAcpSweepTimeAuto sweepTimeAuto, double sweepTimeInterval)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| sweepTimeAuto | RFmxTdscdmaMXAcpSweepTimeAuto | Specifies whether the measurement computes the sweep time. |
| sweepTimeInterval | double | Specifies the sweep time when you set the sweepTimeAuto parameter to False. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00012: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the traces to be stored and retrieved after performing the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method gets the value of AcpAllTracesEnabled attribute.The default va

### GetAllTracesEnabled(string, out bool)

Gets whether to enable the traces to be stored and retrieved after performing the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [AcpAllTracesEnabled](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the traces to be stored and retrieved after performing the ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-getaveragingtype__string-out.html language=enus -->
## TOPIC 00013: GetAveragingType(string, out RFmxTdscdmaMXAcpAveragingType)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-getaveragingtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-getaveragingtype__string-out.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int GetAveragingType(string selectorString, out RFmxTdscdmaMXAcpAveragingType value)RemarksThis method gets the value of

### GetAveragingType(string, out RFmxTdscdmaMXAcpAveragingType)

Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int GetAveragingType(string selectorString, out RFmxTdscdmaMXAcpAveragingType value)

#### Remarks

This method gets the value of [AcpAveragingType](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is [Rms](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpaveragingtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxTdscdmaMXAcpAveragingType | Upon return, contains the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-getmeasurementmethod__string-out.html language=enus -->
## TOPIC 00014: GetMeasurementMethod(string, out RFmxTdscdmaMXAcpMeasurementMethod)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-getmeasurementmethod__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-getmeasurementmethod__string-out.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the method for performing the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int GetMeasurementMethod(string selectorString, out RFmxTdscdmaMXAcpMeasurementMethod value)RemarksThis method gets the value of AcpMeasurementMethod attribute.The default value is Normal.Pa

### GetMeasurementMethod(string, out RFmxTdscdmaMXAcpMeasurementMethod)

Gets the method for performing the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int GetMeasurementMethod(string selectorString, out RFmxTdscdmaMXAcpMeasurementMethod value)

#### Remarks

This method gets the value of [AcpMeasurementMethod](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is [Normal](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpmeasurementmethod.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxTdscdmaMXAcpMeasurementMethod | Upon return, contains the method for performing the ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-getoffsetfrequency__string-out.html language=enus -->
## TOPIC 00015: GetOffsetFrequency(string, out double)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-getoffsetfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-getoffsetfrequency__string-out.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency of an ACP offset channel, relative to the carrier frequency. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int GetOffsetFrequency(string selectorString, out double value)RemarksThis method gets the value of AcpOffsetFrequency attribute.Th

### GetOffsetFrequency(string, out double)

Gets the frequency of an ACP offset channel, relative to the carrier frequency. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int GetOffsetFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [AcpOffsetFrequency](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is 1.6 MHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the frequency of an ACP offset channel, relative to the carrier frequency. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-getoffsetintegrationbandwidth__string-out.html language=enus -->
## TOPIC 00016: GetOffsetIntegrationBandwidth(string, out double)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-getoffsetintegrationbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-getoffsetintegrationbandwidth__string-out.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the integration bandwith of an ACP offset channel. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int GetOffsetIntegrationBandwidth(string selectorString, out double value)RemarksThis method gets the value of AcpOffsetIntegrationBandwidth attribute.The

### GetOffsetIntegrationBandwidth(string, out double)

Gets the integration bandwith of an ACP offset channel. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int GetOffsetIntegrationBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [AcpOffsetIntegrationBandwidth](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is 1.28 MHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the integration bandwith of an ACP offset channel. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-getsequentialfftsize__string-out.html language=enus -->
## TOPIC 00017: GetSequentialFftSize(string, out int)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-getsequentialfftsize__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-getsequentialfftsize__string-out.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the FFT size when you set the SetMeasurementMethod(string, RFmxTdscdmaMXAcpMeasurementMethod) method to SequentialFft. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int GetSequentialFftSize(string selectorString, out int value)RemarksThis method gets the value of AcpSequentialFftSiz

### GetSequentialFftSize(string, out int)

Gets the FFT size when you set the [SetMeasurementMethod(string, RFmxTdscdmaMXAcpMeasurementMethod)](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setmeasurementmethod__string-rfmxtdscdmamxacpmeasurementmethod.html) method to [SequentialFft](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpmeasurementmethod.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int GetSequentialFftSize(string selectorString, out int value)

#### Remarks

This method gets the value of [AcpSequentialFftSize](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is 512.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the FFT size when you set the SetMeasurementMethod(string, RFmxTdscdmaMXAcpMeasurementMethod) method to SequentialFft. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-getsweeptimeauto__string-out.html language=enus -->
## TOPIC 00018: GetSweepTimeAuto(string, out RFmxTdscdmaMXAcpSweepTimeAuto)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-getsweeptimeauto__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-getsweeptimeauto__string-out.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement calculates the sweep time. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int GetSweepTimeAuto(string selectorString, out RFmxTdscdmaMXAcpSweepTimeAuto value)RemarksThis method gets the value of AcpSweepTimeAuto attribute.The default value is True.ParametersNa

### GetSweepTimeAuto(string, out RFmxTdscdmaMXAcpSweepTimeAuto)

Gets whether the measurement calculates the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int GetSweepTimeAuto(string selectorString, out RFmxTdscdmaMXAcpSweepTimeAuto value)

#### Remarks

This method gets the value of [AcpSweepTimeAuto](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpsweeptimeauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxTdscdmaMXAcpSweepTimeAuto | Upon return, contains whether the measurement calculates the sweep time. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-getsweeptimeinterval__string-out.html language=enus -->
## TOPIC 00019: GetSweepTimeInterval(string, out double)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-getsweeptimeinterval__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-getsweeptimeinterval__string-out.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the sweep time when you set the SetSweepTimeAuto(string, RFmxTdscdmaMXAcpSweepTimeAuto) method to False. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int GetSweepTimeInterval(string selectorString, out double value)RemarksThis method gets the val

### GetSweepTimeInterval(string, out double)

Gets the sweep time when you set the [SetSweepTimeAuto(string, RFmxTdscdmaMXAcpSweepTimeAuto)](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setsweeptimeauto__string-rfmxtdscdmamxacpsweeptimeauto.html) method to [False](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpsweeptimeauto.html). This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int GetSweepTimeInterval(string selectorString, out double value)

#### Remarks

This method gets the value of [AcpSweepTimeInterval](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is 0.00066 s.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the sweep time when you set the SetSweepTimeAuto(string, RFmxTdscdmaMXAcpSweepTimeAuto) method to False. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setalltracesenabled__string-bool.html language=enus -->
## TOPIC 00020: SetAllTracesEnabled(string, bool)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setalltracesenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setalltracesenabled__string-bool.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the traces to be stored and retrieved after performing the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int SetAllTracesEnabled(string selectorString, bool value)RemarksThis method sets the value of AcpAllTracesEnabled attribute.The default value

### SetAllTracesEnabled(string, bool)

Sets whether to enable the traces to be stored and retrieved after performing the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int SetAllTracesEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [AcpAllTracesEnabled](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setfarifoutputpoweroffset__string-double.html language=enus -->
## TOPIC 00021: SetFarIFOutputPowerOffset(string, double)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setfarifoutputpoweroffset__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setfarifoutputpoweroffset__string-double.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the offset by which to adjust the IF output power level for offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This method is used only if you set the SetMeasurementMethod(string, RFmxTdscdmaMXAcpMeasurementMethod) method to Dynami

### SetFarIFOutputPowerOffset(string, double)

Sets the offset by which to adjust the IF output power level for offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This method is used only if you set the [SetMeasurementMethod(string, RFmxTdscdmaMXAcpMeasurementMethod)](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setmeasurementmethod__string-rfmxtdscdmamxacpmeasurementmethod.html) method to [DynamicRange](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpmeasurementmethod.html) and set the [SetIFOutputPowerOffsetAuto(string, RFmxTdscdmaMXAcpIFOutputPowerOffsetAuto)](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setifoutputpoweroffsetauto__string-rfmxtdscdmamxacpifoutputpoweroffsetauto.html) method to [False](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpifoutputpoweroffsetauto.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int SetFarIFOutputPowerOffset(string selectorString, double value)

#### Remarks

This method sets the value of [AcpFarIFOutputPowerOffset](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is 20 dB.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the offset by which to adjust the IF output power level for offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This method is used only if you set the SetMeasurementMethod(string, RFmxTdscdmaMXAcpMeasurementMethod) method to DynamicRange and set the SetIFOutputPowerOffsetAuto(string, RFmxTdscdmaMXAcpIFOutputPowerOffsetAuto) method to False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setfftoverlapmode__string-rfmxtdscdmamxacpfftoverlapmode.html language=enus -->
## TOPIC 00022: SetFftOverlapMode(string, RFmxTdscdmaMXAcpFftOverlapMode)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setfftoverlapmode__string-rfmxtdscdmamxacpfftoverlapmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setfftoverlapmode__string-rfmxtdscdmamxacpfftoverlapmode.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets how overlapping is applied when computing the FFT of the acquired samples. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int SetFftOverlapMode(string selectorString, RFmxTdscdmaMXAcpFftOverlapMode value)RemarksThis method sets the value of AcpFftOverlapMode attribute.The default val

### SetFftOverlapMode(string, RFmxTdscdmaMXAcpFftOverlapMode)

Sets how overlapping is applied when computing the FFT of the acquired samples.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int SetFftOverlapMode(string selectorString, RFmxTdscdmaMXAcpFftOverlapMode value)

#### Remarks

This method sets the value of [AcpFftOverlapMode](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is [Disabled](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpfftoverlapmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxTdscdmaMXAcpFftOverlapMode | Specifies how overlapping is applied when computing the FFT of the acquired samples. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00023: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method sets the value of AcpMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescriptionselectorStrin

### SetMeasurementEnabled(string, bool)

Sets whether to enable the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [AcpMeasurementEnabled](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setnearifoutputpoweroffset__string-double.html language=enus -->
## TOPIC 00024: SetNearIFOutputPowerOffset(string, double)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setnearifoutputpoweroffset__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setnearifoutputpoweroffset__string-double.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the offset by which to adjust the IF output power level for offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This method is used only if you set the SetMeasurementMethod(string, RFmxTdscdmaMXAcpMeasurementMethod) method to DynamicRan

### SetNearIFOutputPowerOffset(string, double)

Sets the offset by which to adjust the IF output power level for offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This method is used only if you set the [SetMeasurementMethod(string, RFmxTdscdmaMXAcpMeasurementMethod)](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setmeasurementmethod__string-rfmxtdscdmamxacpmeasurementmethod.html) method to [DynamicRange](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpmeasurementmethod.html) and set the [SetIFOutputPowerOffsetAuto(string, RFmxTdscdmaMXAcpIFOutputPowerOffsetAuto)](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setifoutputpoweroffsetauto__string-rfmxtdscdmamxacpifoutputpoweroffsetauto.html) method to [False](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpifoutputpoweroffsetauto.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int SetNearIFOutputPowerOffset(string selectorString, double value)

#### Remarks

This method sets the value of [AcpNearIFOutputPowerOffset](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is 10 dB.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the offset by which to adjust the IF output power level for offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This method is used only if you set the SetMeasurementMethod(string, RFmxTdscdmaMXAcpMeasurementMethod) method to DynamicRange and set the SetIFOutputPowerOffsetAuto(string, RFmxTdscdmaMXAcpIFOutputPowerOffsetAuto) method to False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setnumberofoffsets__string-int.html language=enus -->
## TOPIC 00025: SetNumberOfOffsets(string, int)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setnumberofoffsets__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setnumberofoffsets__string-int.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of offsets for the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int SetNumberOfOffsets(string selectorString, int value)RemarksThis method sets the value of AcpNumberOfOffsets attribute.The default value is 2.ParametersNameTypeDescriptionselectorStringst

### SetNumberOfOffsets(string, int)

Sets the number of offsets for the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int SetNumberOfOffsets(string selectorString, int value)

#### Remarks

This method sets the value of [AcpNumberOfOffsets](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is 2.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of offsets for the ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setsequentialfftsize__string-int.html language=enus -->
## TOPIC 00026: SetSequentialFftSize(string, int)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setsequentialfftsize__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setsequentialfftsize__string-int.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the FFT size when you set the SetMeasurementMethod(string, RFmxTdscdmaMXAcpMeasurementMethod) method to SequentialFft. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int SetSequentialFftSize(string selectorString, int value)RemarksThis method sets the value of AcpSequentialFftSize at

### SetSequentialFftSize(string, int)

Sets the FFT size when you set the [SetMeasurementMethod(string, RFmxTdscdmaMXAcpMeasurementMethod)](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setmeasurementmethod__string-rfmxtdscdmamxacpmeasurementmethod.html) method to [SequentialFft](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpmeasurementmethod.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int SetSequentialFftSize(string selectorString, int value)

#### Remarks

This method sets the value of [AcpSequentialFftSize](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is 512.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the FFT size when you set the SetMeasurementMethod(string, RFmxTdscdmaMXAcpMeasurementMethod) method to SequentialFft. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setsweeptimeauto__string-rfmxtdscdmamxacpsweeptimeauto.html language=enus -->
## TOPIC 00027: SetSweepTimeAuto(string, RFmxTdscdmaMXAcpSweepTimeAuto)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setsweeptimeauto__string-rfmxtdscdmamxacpsweeptimeauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpconfiguration-setsweeptimeauto__string-rfmxtdscdmamxacpsweeptimeauto.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement calculates the sweep time. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int SetSweepTimeAuto(string selectorString, RFmxTdscdmaMXAcpSweepTimeAuto value)RemarksThis method sets the value of AcpSweepTimeAuto attribute.The default value is True.ParametersNameTy

### SetSweepTimeAuto(string, RFmxTdscdmaMXAcpSweepTimeAuto)

Sets whether the measurement calculates the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int SetSweepTimeAuto(string selectorString, RFmxTdscdmaMXAcpSweepTimeAuto value)

#### Remarks

This method sets the value of [AcpSweepTimeAuto](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxacpsweeptimeauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxTdscdmaMXAcpSweepTimeAuto | Specifies whether the measurement calculates the sweep time. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxcdaconfiguration-setiqgainimbalanceremovalenabled__string-rfmxtdscdmamxcdaiqgainimbalanceremovalenabled.html language=enus -->
## TOPIC 00028: SetIQGainImbalanceRemovalEnabled(string, RFmxTdscdmaMXCdaIQGainImbalanceRemovalEnabled)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxcdaconfiguration-setiqgainimbalanceremovalenabled__string-rfmxtdscdmamxcdaiqgainimbalanceremovalenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxcdaconfiguration-setiqgainimbalanceremovalenabled__string-rfmxtdscdmamxcdaiqgainimbalanceremovalenabled.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to remove the I/Q gain imbalance before the code domain analysis (CDA) measurement. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int SetIQGainImbalanceRemovalEnabled(string selectorString, RFmxTdscdmaMXCdaIQGainImbalanceRemovalEnabled value)RemarksThis method sets the value

### SetIQGainImbalanceRemovalEnabled(string, RFmxTdscdmaMXCdaIQGainImbalanceRemovalEnabled)

Sets whether to remove the I/Q gain imbalance before the code domain analysis (CDA) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int SetIQGainImbalanceRemovalEnabled(string selectorString, RFmxTdscdmaMXCdaIQGainImbalanceRemovalEnabled value)

#### Remarks

This method sets the value of [CdaIQGainImbalanceRemovalEnabled](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxcdaiqgainimbalanceremovalenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxTdscdmaMXCdaIQGainImbalanceRemovalEnabled | Specifies whether to remove the I/Q gain imbalance before the code domain analysis (CDA) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXCdaConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxcdaresults-getmeansymbolpower__string-out.html language=enus -->
## TOPIC 00029: GetMeanSymbolPower(string, out double)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxcdaresults-getmeansymbolpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxcdaresults-getmeansymbolpower__string-out.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean symbol power for the selected time slot and channel. This value is expressed in dB if you set the SetPowerUnit(string, RFmxTdscdmaMXCdaPowerUnit) method to dB, or in dBm if you set the CDA Pwr Unit method to dBm. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int GetMeanSymb

### GetMeanSymbolPower(string, out double)

Gets the mean symbol power for the selected time slot and channel. This value is expressed in dB if you set the [SetPowerUnit(string, RFmxTdscdmaMXCdaPowerUnit)](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxcdaconfiguration-setpowerunit__string-rfmxtdscdmamxcdapowerunit.html) method to [dB](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxcdapowerunit.html), or in dBm if you set the CDA Pwr Unit method to [dBm](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxcdapowerunit.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int GetMeanSymbolPower(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsMeanSymbolPower](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean symbol power for the selected time slot and channel. This value is expressed in dB if you set the SetPowerUnit(string, RFmxTdscdmaMXCdaPowerUnit) method to dB, or in dBm if you set the CDA Pwr Unit method to dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXCdaResults Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxcdaresults-getmeantotalpower__string-out.html language=enus -->
## TOPIC 00030: GetMeanTotalPower(string, out double)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxcdaresults-getmeantotalpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxcdaresults-getmeantotalpower__string-out.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the total power measured in the code domain of the base spreading factor, averaged over all averaging iterations. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int GetMeanTotalPower(string selectorString, out double value)RemarksThis method gets the v

### GetMeanTotalPower(string, out double)

Gets the total power measured in the code domain of the base spreading factor, averaged over all averaging iterations. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int GetMeanTotalPower(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsMeanTotalPower](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the total power measured in the code domain of the base spreading factor, averaged over all averaging iterations. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXCdaResults Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxcdaspectruminverted.html language=enus -->
## TOPIC 00031: RFmxTdscdmaMXCdaSpectrumInverted Enumeration

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxcdaspectruminverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxcdaspectruminverted.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the spectrum of the signal is inverted. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic enum RFmxTdscdmaMXCdaSpectrumInvertedMembersNameValueDescriptionFalse0The spectrum is not inverted. True1The spectrum is inverted.

### RFmxTdscdmaMXCdaSpectrumInverted Enumeration

Specifies whether the spectrum of the signal is inverted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public enum RFmxTdscdmaMXCdaSpectrumInverted

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The spectrum is not inverted. |
| True | 1 | The spectrum is inverted. |

Parent topic:

NationalInstruments.RFmx.TdscdmaMX

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxcdasynchronizationmode.html language=enus -->
## TOPIC 00032: RFmxTdscdmaMXCdaSynchronizationMode Enumeration

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxcdasynchronizationmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxcdasynchronizationmode.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the synchronization mode for the code domain analysis (CDA) measurement. Currently, only the Slot mode is supported. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic enum RFmxTdscdmaMXCdaSynchronizationModeMembersNameValueDescriptionSlot0The measurement uses slot synchronization m

### RFmxTdscdmaMXCdaSynchronizationMode Enumeration

Specifies the synchronization mode for the code domain analysis (CDA) measurement. Currently, only the Slot mode is supported.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public enum RFmxTdscdmaMXCdaSynchronizationMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Slot | 0 | The measurement uses slot synchronization mode. The slot boundary in the acquired signal is detected, and the measurement is performed over one slot, starting from the boundary specified by the SetMeasurementOffset(string, int) method. |

Parent topic:

NationalInstruments.RFmx.TdscdmaMX

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-configureaveraging__string-rfmxtdscdmamxchpaveragingenabled-int-rfmxtdscdmamxchpaveragingtype.html language=enus -->
## TOPIC 00033: ConfigureAveraging(string, RFmxTdscdmaMXChpAveragingEnabled, int, RFmxTdscdmaMXChpAveragingType)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-configureaveraging__string-rfmxtdscdmamxchpaveragingenabled-int-rfmxtdscdmamxchpaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-configureaveraging__string-rfmxtdscdmamxchpaveragingenabled-int-rfmxtdscdmamxchpaveragingtype.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the CHP measurement.SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int ConfigureAveraging(string selectorString, RFmxTdscdmaMXChpAveragingEnabled averagingEnabled, int averagingCount, RFmxTdscdmaMXChpAveragingType averagingType)ParametersNameTypeDescriptionselecto

### ConfigureAveraging(string, RFmxTdscdmaMXChpAveragingEnabled, int, RFmxTdscdmaMXChpAveragingType)

Configures averaging for the CHP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int ConfigureAveraging(string selectorString, RFmxTdscdmaMXChpAveragingEnabled averagingEnabled, int averagingCount, RFmxTdscdmaMXChpAveragingType averagingType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| averagingEnabled | RFmxTdscdmaMXChpAveragingEnabled | Enables averaging for spectrum measurements. |
| averagingCount | int | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True. |
| averagingType | RFmxTdscdmaMXChpAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. RFmx uses the averaged spectrum for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-getintegrationbandwidth__string-out.html language=enus -->
## TOPIC 00034: GetIntegrationBandwidth(string, out double)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-getintegrationbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-getintegrationbandwidth__string-out.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the CHP carrier integration bandwidth. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int GetIntegrationBandwidth(string selectorString, out double value)RemarksThis method gets the value of ChpIntegrationBandwidth attribute.ParametersNameTypeDescriptio

### GetIntegrationBandwidth(string, out double)

Gets the CHP carrier integration bandwidth. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int GetIntegrationBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [ChpIntegrationBandwidth](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the CHP carrier integration bandwidth. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00035: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the CHP measurement. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method gets the value of ChpMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescriptionselectorS

### GetMeasurementEnabled(string, out bool)

Gets whether to enable the CHP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [ChpMeasurementEnabled](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the CHP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-getrbwfiltertype__string-out.html language=enus -->
## TOPIC 00036: GetRbwFilterType(string, out RFmxTdscdmaMXChpRbwFilterType)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-getrbwfiltertype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-getrbwfiltertype__string-out.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the shape of the digital RBW filter. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int GetRbwFilterType(string selectorString, out RFmxTdscdmaMXChpRbwFilterType value)RemarksThis method gets the value of ChpRbwFilterType attribute.The default value is FftBased.ParametersNameTypeDesc

### GetRbwFilterType(string, out RFmxTdscdmaMXChpRbwFilterType)

Gets the shape of the digital RBW filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int GetRbwFilterType(string selectorString, out RFmxTdscdmaMXChpRbwFilterType value)

#### Remarks

This method gets the value of [ChpRbwFilterType](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is [FftBased](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchprbwfiltertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxTdscdmaMXChpRbwFilterType | Upon return, contains the shape of the digital RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00037: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the CHP measurement. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method sets the value of ChpMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescriptionselectorStrin

### SetMeasurementEnabled(string, bool)

Sets whether to enable the CHP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [ChpMeasurementEnabled](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the CHP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-setnumberofanalysisthreads__string-int.html language=enus -->
## TOPIC 00038: SetNumberOfAnalysisThreads(string, int)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-setnumberofanalysisthreads__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-setnumberofanalysisthreads__string-int.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the maximum number of threads used for parallelism for the CHP measurement. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int SetNumberOfAnalysisThreads(string selectorString, int value)RemarksThis method sets the value of ChpNumberOfAnalysisThreads attribute.The default value is 1.

### SetNumberOfAnalysisThreads(string, int)

Sets the maximum number of threads used for parallelism for the CHP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int SetNumberOfAnalysisThreads(string selectorString, int value)

#### Remarks

This method sets the value of [ChpNumberOfAnalysisThreads](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the maximum number of threads used for parallelism for the CHP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-setrbwfilterbandwidth__string-double.html language=enus -->
## TOPIC 00039: SetRbwFilterBandwidth(string, double)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-setrbwfilterbandwidth__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-setrbwfilterbandwidth__string-double.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the bandwidth of the RBW filter used to sweep the acquired signal when you set the SetRbwFilterAutoBandwidth(string, RFmxTdscdmaMXChpRbwAutoBandwidth) method to False. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int SetRbwFilterBandwidth(string selec

### SetRbwFilterBandwidth(string, double)

Sets the bandwidth of the RBW filter used to sweep the acquired signal when you set the [SetRbwFilterAutoBandwidth(string, RFmxTdscdmaMXChpRbwAutoBandwidth)](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-setrbwfilterautobandwidth__string-rfmxtdscdmamxchprbwautobandwidth.html) method to [False](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchprbwautobandwidth.html). This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int SetRbwFilterBandwidth(string selectorString, double value)

#### Remarks

This method sets the value of [ChpRbwFilterBandwidth](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is 5.636 kHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the SetRbwFilterAutoBandwidth(string, RFmxTdscdmaMXChpRbwAutoBandwidth) method to False. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-setrbwfiltertype__string-rfmxtdscdmamxchprbwfiltertype.html language=enus -->
## TOPIC 00040: SetRbwFilterType(string, RFmxTdscdmaMXChpRbwFilterType)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-setrbwfiltertype__string-rfmxtdscdmamxchprbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-setrbwfiltertype__string-rfmxtdscdmamxchprbwfiltertype.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the shape of the digital RBW filter. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int SetRbwFilterType(string selectorString, RFmxTdscdmaMXChpRbwFilterType value)RemarksThis method sets the value of ChpRbwFilterType attribute.The default value is FftBased.ParametersNameTypeDescript

### SetRbwFilterType(string, RFmxTdscdmaMXChpRbwFilterType)

Sets the shape of the digital RBW filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int SetRbwFilterType(string selectorString, RFmxTdscdmaMXChpRbwFilterType value)

#### Remarks

This method sets the value of [ChpRbwFilterType](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is [FftBased](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchprbwfiltertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxTdscdmaMXChpRbwFilterType | Specifies the shape of the digital RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-setsweeptimeauto__string-rfmxtdscdmamxchpsweeptimeauto.html language=enus -->
## TOPIC 00041: SetSweepTimeAuto(string, RFmxTdscdmaMXChpSweepTimeAuto)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-setsweeptimeauto__string-rfmxtdscdmamxchpsweeptimeauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpconfiguration-setsweeptimeauto__string-rfmxtdscdmamxchpsweeptimeauto.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement calculates the sweep time. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int SetSweepTimeAuto(string selectorString, RFmxTdscdmaMXChpSweepTimeAuto value)RemarksThis method sets the value of ChpSweepTimeAuto attribute.The default value is True.ParametersNameTy

### SetSweepTimeAuto(string, RFmxTdscdmaMXChpSweepTimeAuto)

Sets whether the measurement calculates the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int SetSweepTimeAuto(string selectorString, RFmxTdscdmaMXChpSweepTimeAuto value)

#### Remarks

This method sets the value of [ChpSweepTimeAuto](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxchpsweeptimeauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxTdscdmaMXChpSweepTimeAuto | Specifies whether the measurement calculates the sweep time. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxconstants-pxitriggerline5.html language=enus -->
## TOPIC 00042: PxiTriggerLine5

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxconstants-pxitriggerline5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxconstants-pxitriggerline5.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 5. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic const string PxiTriggerLine5

### PxiTriggerLine5

The signal is exported to the PXI trigger line 5.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public const string PxiTriggerLine5

Parent topic:

RFmxTdscdmaMXConstants Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxconstants-pxitriggerline7.html language=enus -->
## TOPIC 00043: PxiTriggerLine7

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxconstants-pxitriggerline7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxconstants-pxitriggerline7.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 7. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic const string PxiTriggerLine7

### PxiTriggerLine7

The signal is exported to the PXI trigger line 7.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public const string PxiTriggerLine7

Parent topic:

RFmxTdscdmaMXConstants Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxconstants-timerevent.html language=enus -->
## TOPIC 00044: TimerEvent

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxconstants-timerevent.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxconstants-timerevent.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The trigger is received from the timer event. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic const string TimerEvent

### TimerEvent

The trigger is received from the timer event.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public const string TimerEvent

Parent topic:

RFmxTdscdmaMXConstants Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxconstants.html language=enus -->
## TOPIC 00045: RFmxTdscdmaMXConstants Class

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxconstants.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxconstants.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies constants for I/O terminals. Derives fromNoneSyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic class RFmxTdscdmaMXConstantsFieldsNameDescriptionDioPfi0DioPfi1DioPfi2DioPfi3DioPfi4DioPfi5DioPfi6DioPfi7Pfi0The signal is exported to the PFI 1 connector on the PXI-5142 and PXIe-5622. P

### RFmxTdscdmaMXConstants Class

Specifies constants for I/O terminals.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public class RFmxTdscdmaMXConstants

#### Fields

| Name | Description |
| --- | --- |
| DioPfi0 |  |
| DioPfi1 |  |
| DioPfi2 |  |
| DioPfi3 |  |
| DioPfi4 |  |
| DioPfi5 |  |
| DioPfi6 |  |
| DioPfi7 |  |
| Pfi0 | The signal is exported to the PFI 1 connector on the PXI-5142 and PXIe-5622. |
| Pfi1 | The signal is exported to the PXI trigger line 0. |
| PulseIn |  |
| PxieDStarBLine | The signal is exported to the PXIe DStar B trigger line. |
| PxiStarLine | The signal is exported to the PXI star trigger line. |
| PxiTriggerLine0 | The signal is exported to the PXI trigger line 0. |
| PxiTriggerLine1 | The signal is exported to the PXI trigger line 1. |
| PxiTriggerLine2 | The signal is exported to the PXI trigger line 2. |
| PxiTriggerLine3 | The signal is exported to the PXI trigger line 3. |
| PxiTriggerLine4 | The signal is exported to the PXI trigger line 4. |
| PxiTriggerLine5 | The signal is exported to the PXI trigger line 5. |
| PxiTriggerLine6 | The signal is exported to the PXI trigger line 6. |
| PxiTriggerLine7 | The signal is exported to the PXI trigger line 7. |
| TimerEvent | The trigger is received from the timer event. |

Parent topic:

NationalInstruments.RFmx.TdscdmaMX

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxdigitaledgetriggeredge.html language=enus -->
## TOPIC 00046: RFmxTdscdmaMXDigitalEdgeTriggerEdge Enumeration

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxdigitaledgetriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxdigitaledgetriggeredge.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxTdscdmaMXTriggerType) method to DigitalEdge. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic enum RFmxTdscdmaMXDigitalEdgeTriggerEdgeMembersNameValueDescriptionRising0The trigger

### RFmxTdscdmaMXDigitalEdgeTriggerEdge Enumeration

Specifies the active edge for the trigger. This method is used only when you set the [SetTriggerType(string, RFmxTdscdmaMXTriggerType)](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamx-settriggertype__string-rfmxtdscdmamxtriggertype.html) method to [DigitalEdge](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public enum RFmxTdscdmaMXDigitalEdgeTriggerEdge

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 0 | The trigger asserts on the rising edge of the signal. |
| Falling | 1 | The trigger asserts on the falling edge of the signal. |

Parent topic:

NationalInstruments.RFmx.TdscdmaMX

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxiqpoweredgetriggerleveltype.html language=enus -->
## TOPIC 00047: RFmxTdscdmaMXIQPowerEdgeTriggerLevelType Enumeration

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxiqpoweredgetriggerleveltype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxiqpoweredgetriggerleveltype.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. This method is used only when you set the SetTriggerType(string, RFmxTdscdmaMXTriggerType) method to IQPowerEdge. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic enum RFmxTdscdmaMXIQPowerEdgeTriggerLevelType

### RFmxTdscdmaMXIQPowerEdgeTriggerLevelType Enumeration

Specifies the reference for the [SetIQPowerEdgeTriggerLevel(string, double)](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamx-setiqpoweredgetriggerlevel__string-double.html) method. This method is used only when you set the [SetTriggerType(string, RFmxTdscdmaMXTriggerType)](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamx-settriggertype__string-rfmxtdscdmamxtriggertype.html) method to [IQPowerEdge](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public enum RFmxTdscdmaMXIQPowerEdgeTriggerLevelType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Relative | 0 | The IQ Power Edge Level method is relative to the value of the SetReferenceLevel(string, double) method. |
| Absolute | 1 | The IQ Power Edge Level method specifies the absolute power. |

Parent topic:

NationalInstruments.RFmx.TdscdmaMX

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodacc-configuration.html language=enus -->
## TOPIC 00048: Configuration

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodacc-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodacc-configuration.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxTdscdmaMXModAccConfiguration instance that provides methods to configure the ModAcc measurement. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic RFmxTdscdmaMXModAccConfiguration Configuration { get; }

### Configuration

Gets the [RFmxTdscdmaMXModAccConfiguration](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccconfiguration.html) instance that provides methods to configure the ModAcc measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public [RFmxTdscdmaMXModAccConfiguration](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccconfiguration.html) Configuration { get; }

Parent topic:

RFmxTdscdmaMXModAcc Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodacc.html language=enus -->
## TOPIC 00049: RFmxTdscdmaMXModAcc Class

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodacc.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the ModAcc measurement. Derives fromRFmxTdscdmaMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic class RFmxTdscdmaMXModAcc : RFmxTdscdmaMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxTdscdmaMXModAccConfiguration instance that provides methods to configure

### RFmxTdscdmaMXModAcc Class

Represents the ModAcc measurement.

#### Derives from

- RFmxTdscdmaMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public class RFmxTdscdmaMXModAcc : RFmxTdscdmaMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxTdscdmaMXModAccConfiguration instance that provides methods to configure the ModAcc measurement. |
| Results | Gets the RFmxTdscdmaMXModAccResults instance that provides methods to fetch and read the ModAcc measurement results. |

Parent topic:

NationalInstruments.RFmx.TdscdmaMX

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccconfiguration-configureslottype__string-rfmxtdscdmamxmodaccslottype.html language=enus -->
## TOPIC 00050: ConfigureSlotType(string, RFmxTdscdmaMXModAccSlotType)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccconfiguration-configureslottype__string-rfmxtdscdmamxmodaccslottype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccconfiguration-configureslottype__string-rfmxtdscdmamxmodaccslottype.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the type of the Time Slot for ModAcc analysis.SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int ConfigureSlotType(string selectorString, RFmxTdscdmaMXModAccSlotType slotType)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed w

### ConfigureSlotType(string, RFmxTdscdmaMXModAccSlotType)

Configures the type of the Time Slot for ModAcc analysis.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int ConfigureSlotType(string selectorString, RFmxTdscdmaMXModAccSlotType slotType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| slotType | RFmxTdscdmaMXModAccSlotType | Specifies the type of the Time Slot for ModAcc analysis. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccconfiguration-getaveragingenabled__string-out.html language=enus -->
## TOPIC 00051: GetAveragingEnabled(string, out RFmxTdscdmaMXModAccAveragingEnabled)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccconfiguration-getaveragingenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccconfiguration-getaveragingenabled__string-out.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable averaging for the ModAcc measurement. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int GetAveragingEnabled(string selectorString, out RFmxTdscdmaMXModAccAveragingEnabled value)RemarksThis method gets the value of ModAccAveragingEnabled attribute.The default value

### GetAveragingEnabled(string, out RFmxTdscdmaMXModAccAveragingEnabled)

Gets whether to enable averaging for the ModAcc measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int GetAveragingEnabled(string selectorString, out RFmxTdscdmaMXModAccAveragingEnabled value)

#### Remarks

This method gets the value of [ModAccAveragingEnabled](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxTdscdmaMXModAccAveragingEnabled | Upon return, contains whether to enable averaging for the ModAcc measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccconfiguration-getslottype__string-out.html language=enus -->
## TOPIC 00052: GetSlotType(string, out RFmxTdscdmaMXModAccSlotType)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccconfiguration-getslottype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccconfiguration-getslottype__string-out.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the type of the time slot for the ModAcc measurement. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int GetSlotType(string selectorString, out RFmxTdscdmaMXModAccSlotType value)RemarksThis method gets the value of ModAccSlotType attribute.The default value is Traffic.ParametersNameT

### GetSlotType(string, out RFmxTdscdmaMXModAccSlotType)

Gets the type of the time slot for the ModAcc measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int GetSlotType(string selectorString, out RFmxTdscdmaMXModAccSlotType value)

#### Remarks

This method gets the value of [ModAccSlotType](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is [Traffic](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccslottype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxTdscdmaMXModAccSlotType | Upon return, contains the type of the time slot for the ModAcc measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccconfiguration-setmeasurementoffset__string-int.html language=enus -->
## TOPIC 00053: SetMeasurementOffset(string, int)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccconfiguration-setmeasurementoffset__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccconfiguration-setmeasurementoffset__string-int.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the measurement offset that is skipped by the ModAcc measurement from the synchronization boundary. This value is expressed in traffic slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxTdscdmaMXModAccSynchronizationMode) method. SyntaxNamespace: National

### SetMeasurementOffset(string, int)

Sets the measurement offset that is skipped by the ModAcc measurement from the synchronization boundary. This value is expressed in traffic slots. The synchronization boundary is specified by the [SetSynchronizationMode(string, RFmxTdscdmaMXModAccSynchronizationMode)](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccconfiguration-setsynchronizationmode__string-rfmxtdscdmamxmodaccsynchronizationmode.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int SetMeasurementOffset(string selectorString, int value)

#### Remarks

This method sets the value of [ModAccMeasurementOffset](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the measurement offset that is skipped by the ModAcc measurement from the synchronization boundary. This value is expressed in traffic slots. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxTdscdmaMXModAccSynchronizationMode) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccconfiguration-setslottype__string-rfmxtdscdmamxmodaccslottype.html language=enus -->
## TOPIC 00054: SetSlotType(string, RFmxTdscdmaMXModAccSlotType)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccconfiguration-setslottype__string-rfmxtdscdmamxmodaccslottype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccconfiguration-setslottype__string-rfmxtdscdmamxmodaccslottype.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the type of the time slot for the ModAcc measurement. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int SetSlotType(string selectorString, RFmxTdscdmaMXModAccSlotType value)RemarksThis method sets the value of ModAccSlotType attribute.The default value is Traffic.ParametersNameTypeD

### SetSlotType(string, RFmxTdscdmaMXModAccSlotType)

Sets the type of the time slot for the ModAcc measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int SetSlotType(string selectorString, RFmxTdscdmaMXModAccSlotType value)

#### Remarks

This method sets the value of [ModAccSlotType](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is [Traffic](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccslottype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxTdscdmaMXModAccSlotType | Specifies the type of the time slot for the ModAcc measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccconfiguration-setspectruminverted__string-rfmxtdscdmamxmodaccspectruminverted.html language=enus -->
## TOPIC 00055: SetSpectrumInverted(string, RFmxTdscdmaMXModAccSpectrumInverted)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccconfiguration-setspectruminverted__string-rfmxtdscdmamxmodaccspectruminverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccconfiguration-setspectruminverted__string-rfmxtdscdmamxmodaccspectruminverted.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the spectrum of the signal is inverted. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int SetSpectrumInverted(string selectorString, RFmxTdscdmaMXModAccSpectrumInverted value)RemarksThis method sets the value of ModAccSpectrumInverted attribute.The default value is False.Par

### SetSpectrumInverted(string, RFmxTdscdmaMXModAccSpectrumInverted)

Sets whether the spectrum of the signal is inverted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int SetSpectrumInverted(string selectorString, RFmxTdscdmaMXModAccSpectrumInverted value)

#### Remarks

This method sets the value of [ModAccSpectrumInverted](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccspectruminverted.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxTdscdmaMXModAccSpectrumInverted | Specifies whether the spectrum of the signal is inverted. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccresults-getfrequencyerror__string-out.html language=enus -->
## TOPIC 00056: GetFrequencyError(string, out double)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccresults-getfrequencyerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccresults-getfrequencyerror__string-out.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency error averaged over all measured slots. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int GetFrequencyError(string selectorString, out double value)RemarksThis method gets the value of ModAccResultsFrequencyError attribute.ParametersNameT

### GetFrequencyError(string, out double)

Gets the frequency error averaged over all measured slots. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int GetFrequencyError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsFrequencyError](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the frequency error averaged over all measured slots. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXModAccResults Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccresults-getiqgainimbalance__string-out.html language=enus -->
## TOPIC 00057: GetIQGainImbalance(string, out double)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccresults-getiqgainimbalance__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccresults-getiqgainimbalance__string-out.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the I/Q gain imbalance of the composite signal, averaged over all measured slots. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int GetIQGainImbalance(string selectorString, out double value)RemarksThis method gets the value of ModAccResultsIQGainImbal

### GetIQGainImbalance(string, out double)

Gets the I/Q gain imbalance of the composite signal, averaged over all measured slots. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int GetIQGainImbalance(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsIQGainImbalance](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the I/Q gain imbalance of the composite signal, averaged over all measured slots. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXModAccResults Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccresults-getiqoriginoffset__string-out.html language=enus -->
## TOPIC 00058: GetIQOriginOffset(string, out double)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccresults-getiqoriginoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccresults-getiqoriginoffset__string-out.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the I/Q origin offset of the composite signal, averaged over all measured slots. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int GetIQOriginOffset(string selectorString, out double value)RemarksThis method gets the value of ModAccResultsIQOriginOffse

### GetIQOriginOffset(string, out double)

Gets the I/Q origin offset of the composite signal, averaged over all measured slots. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int GetIQOriginOffset(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsIQOriginOffset](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the I/Q origin offset of the composite signal, averaged over all measured slots. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXModAccResults Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccresults-getpeakmidambleevm__string-out.html language=enus -->
## TOPIC 00059: GetPeakMidambleEvm(string, out double)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccresults-getpeakmidambleevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccresults-getpeakmidambleevm__string-out.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak midamble EVM among all active time slots and averaging iterations. This value is expressed as a percentage. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int GetPeakMidambleEvm(string selectorString, out double value)RemarksThis method gets the value of ModAccResultsPeakMid

### GetPeakMidambleEvm(string, out double)

Gets the peak midamble EVM among all active time slots and averaging iterations. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int GetPeakMidambleEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsPeakMidambleEvm](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the value of the slot based peak midamble EVM among all active time slots. This value is expressed as a percentage. The value is averaged over all averaging iterations. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXModAccResults Class

<!--NI_TOPIC bundle=rfmxtdscdma-dotnet-api-ref path=nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccresults-getrmsdatamagnitudeerror__string-out.html language=enus -->
## TOPIC 00060: GetRmsDataMagnitudeError(string, out double)

- bundle_id: `rfmxtdscdma-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccresults-getrmsdatamagnitudeerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxmodaccresults-getrmsdatamagnitudeerror__string-out.html
- document_id: `rfmxtdscdma-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RMS of the data magnitude error, averaged over all active time slots and all averaging iterations. This value is expressed as a percentage. SyntaxNamespace: NationalInstruments.RFmx.TdscdmaMXpublic int GetRmsDataMagnitudeError(string selectorString, out double value)RemarksThis method gets

### GetRmsDataMagnitudeError(string, out double)

Gets the RMS of the data magnitude error, averaged over all active time slots and all averaging iterations. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.TdscdmaMX](nationalinstruments-rfmx-tdscdmamx.html)

public int GetRmsDataMagnitudeError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsRmsDataMagnitudeError](nationalinstruments-rfmx-tdscdmamx-rfmxtdscdmamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the RMS of the data magnitude error, averaged over all active time slots and all averaging iterations. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxTdscdmaMXModAccResults Class
