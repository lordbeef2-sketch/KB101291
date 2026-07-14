# NI DOCUMENT BUNDLE: rfmxcdma2k-dotnet-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxcdma2k-dotnet-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-analyzeiq1waveform__string-string-complexwaveform_complexsingle_-bool-long.html language=enus -->
## TOPIC 00001: AnalyzeIQ1Waveform(string, string, ComplexWaveform< ComplexSingle >, bool, long)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-analyzeiq1waveform__string-string-complexwaveform_complexsingle_-bool-long.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-analyzeiq1waveform__string-string-complexwaveform_complexsingle_-bool-long.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods in the method node. Use this method only if the RFmxIns

### AnalyzeIQ1Waveform(string, string, ComplexWaveform< ComplexSingle >, bool, long)

Performs the enabled measurements on the I/Q complex waveform that you specify in *IQ* parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods in the method node. Use this method only if the RFmxInstrMX.GetRecommendedAcquisitionType method value is either *IQ* or *IQorSpectral*. 
 Query the Recommended Acquisition Type method after calling the [Commit(string)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-commit__string.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int AnalyzeIQ1Waveform(string selectorString, string resultName, ComplexWaveform< ComplexSingle > iq, bool reset, long reserved)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the result name in this input, either the result name specified by resultName parameter or the default result instance is used. The default is "" (empty string). Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| resultName | string | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"result::r1""r1" |
| iq | ComplexWaveform< ComplexSingle > | Specifies the data for a complex waveform including the start, delta, and actual values. |
| reset | bool | Resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| reserved | long | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-buildoffsetstring__string-int.html language=enus -->
## TOPIC 00002: BuildOffsetString(string, int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-buildoffsetstring__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-buildoffsetstring__string-int.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the offset string to use as the selector string with the SEM and ACP offset configuration for fetch methods and methods. Refer to the Selector String topic for information about the string syntax for named signals.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic static string BuildOf

### BuildOffsetString(string, int)

Creates the offset string to use as the selector string with the SEM and ACP offset configuration for fetch methods and methods. 
 Refer to the [Selector String](/csh?context=rfmxspecan_rfmxspecan_using_selector_string) topic for information about the string syntax for named signals.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public static string BuildOffsetString(string selectorString, int offsetNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| offsetNumber | int | Specifies the offset number used to build the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-buildresultstring__string.html language=enus -->
## TOPIC 00003: BuildResultString(string)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-buildresultstring__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-buildresultstring__string.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates selector string for use with configuration or fetch. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic static string BuildResultString(string resultName)ParametersNameTypeDescriptionresultNamestringSpecifies the result name for building the selector string. This input accepts the resu

### BuildResultString(string)

Creates selector string for use with configuration or fetch.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public static string BuildResultString(string resultName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| resultName | string | Specifies the result name for building the selector string. This input accepts the result name with or without the "result::" prefix. Example: "", "result::r1", "r1". |

#### Returns

Upon return, contains the selector string created by this method.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-cda.html language=enus -->
## TOPIC 00004: Cda

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-cda.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-cda.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxCdma2kMXCda instance that represents the CDA measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic RFmxCdma2kMXCda Cda { get; }

### Cda

Gets the [RFmxCdma2kMXCda](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcda.html) instance that represents the CDA measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public [RFmxCdma2kMXCda](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcda.html) Cda { get; }

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-clearallnamedresults__string.html language=enus -->
## TOPIC 00005: ClearAllNamedResults(string)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-clearallnamedresults__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-clearallnamedresults__string.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all results for the current signal instance.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int ClearAllNamedResults(string selectorString)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when creating the signal configuration is u

### ClearAllNamedResults(string)

Clears all results for the current signal instance.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int ClearAllNamedResults(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-configurefrequencychannelnumber__string-rfmxcdma2kmxlinkdirection-int-int.html language=enus -->
## TOPIC 00006: ConfigureFrequencyChannelNumber(string, RFmxCdma2kMXLinkDirection, int, int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-configurefrequencychannelnumber__string-rfmxcdma2kmxlinkdirection-int-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-configurefrequencychannelnumber__string-rfmxcdma2kmxlinkdirection-int-int.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the expected carrier frequency of the RF signal to acquire according to the given channel number. The signal analyzer tunes to this frequency.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int ConfigureFrequencyChannelNumber(string selectorString, RFmxCdma2kMXLinkDirection linkD

### ConfigureFrequencyChannelNumber(string, RFmxCdma2kMXLinkDirection, int, int)

Configures the expected carrier frequency of the RF signal to acquire according to the given channel number. The signal analyzer tunes to this frequency.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int ConfigureFrequencyChannelNumber(string selectorString, RFmxCdma2kMXLinkDirection linkDirection, int bandclass, int channelNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| linkDirection | RFmxCdma2kMXLinkDirection | Specifies the direction for which the frequency is calculated. Currently only uplink is supported. |
| bandclass | int | Specifies the band in which the channel is located as defined in Section: 1.5, Table 1.5-1: Band Class List, of the 3GPP2 C.S0057-F specification v1.0. |
| channelNumber | int | Specifies the channel number used to build the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-configureiqpoweredgetrigger__string-string-rfmxcdma2kmxiqpoweredgetriggerslope-double-double-rfmxcdma2kmxtriggerminimumquiettimemode-doubl...d17e997.html language=enus -->
## TOPIC 00007: ConfigureIQPowerEdgeTrigger(string, string, RFmxCdma2kMXIQPowerEdgeTriggerSlope, double, double, RFmxCdma2kMXTriggerMinimumQuietTimeMode, double, RFmxCdma2kMXIQPowerEdgeTriggerLevelType, bool)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-configureiqpoweredgetrigger__string-string-rfmxcdma2kmxiqpoweredgetriggerslope-double-double-rfmxcdma2kmxtriggerminimumquiettimemode-doubl...d17e997.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-configureiqpoweredgetrigger__string-string-rfmxcdma2kmxiqpoweredgetriggerslope-double-double-rfmxcdma2kmxtriggerminimumquiettimemode-doubl...d17e997.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int ConfigureIQPowerEdgeTrigger(string selectorString, string iqPowerEdgeTriggerSource, RFmxCdma2

### ConfigureIQPowerEdgeTrigger(string, string, RFmxCdma2kMXIQPowerEdgeTriggerSlope, double, double, RFmxCdma2kMXTriggerMinimumQuietTimeMode, double, RFmxCdma2kMXIQPowerEdgeTriggerLevelType, bool)

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int ConfigureIQPowerEdgeTrigger(string selectorString, string iqPowerEdgeTriggerSource, RFmxCdma2kMXIQPowerEdgeTriggerSlope iqPowerEdgeTriggerSlope, double iqPowerEdgeTriggerLevel, double triggerDelay, RFmxCdma2kMXTriggerMinimumQuietTimeMode triggerMinimumQuietTimeMode, double triggerMinimumQuietTimeDuration, RFmxCdma2kMXIQPowerEdgeTriggerLevelType iqPowerEdgeTriggerLevelType, bool enableTrigger)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| iqPowerEdgeTriggerSource | string | Specifies the channel from which the device monitors the trigger. |
| iqPowerEdgeTriggerSlope | RFmxCdma2kMXIQPowerEdgeTriggerSlope | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. |
| iqPowerEdgeTriggerLevel | double | Specifies the power level at which the device triggers, depending on the value of the iqPowerEdgeTriggerSlope parameter. The value is expressed in dB when the iqPowerEdgeTriggerLevelType parameter is set to Relative, or in dBm when it is set to Absolute. |
| triggerDelay | double | Specifies the trigger delay time. This value is expressed in seconds. |
| triggerMinimumQuietTimeMode | RFmxCdma2kMXTriggerMinimumQuietTimeMode | Specifies whether the measurement computes the minimum quiet time used for triggering. |
| triggerMinimumQuietTimeDuration | double | Specifies the duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set SetIQPowerEdgeTriggerSlope(string, RFmxCdma2kMXIQPowerEdgeTriggerSlope) to Rising, the signal is quiet when it is below the trigger level. |
| iqPowerEdgeTriggerLevelType | RFmxCdma2kMXIQPowerEdgeTriggerLevelType | Specifies whether the IQPowerEdgeLevel is set to Relative or Absolute. The value is expressed in dB when this parameter is set to Relative. The value is expressed in dBm when this parameter is set to Absolute. |
| enableTrigger | bool | Specifies whether the trigger is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-configureradioconfiguration__string-rfmxcdma2kmxradioconfiguration.html language=enus -->
## TOPIC 00008: ConfigureRadioConfiguration(string, RFmxCdma2kMXRadioConfiguration)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-configureradioconfiguration__string-rfmxcdma2kmxradioconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-configureradioconfiguration__string-rfmxcdma2kmxradioconfiguration.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the radio configuration of the CDMA2k signal.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int ConfigureRadioConfiguration(string selectorString, RFmxCdma2kMXRadioConfiguration radioConfiguration)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal

### ConfigureRadioConfiguration(string, RFmxCdma2kMXRadioConfiguration)

Configures the radio configuration of the CDMA2k signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int ConfigureRadioConfiguration(string selectorString, RFmxCdma2kMXRadioConfiguration radioConfiguration)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| radioConfiguration | RFmxCdma2kMXRadioConfiguration | Specifies the radio configuration of the CDMA2k signal to be analyzed. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-configureuserdefinedchannelarray__string-int_arr1-int_arr1-rfmxcdma2kmxbranch_arr1.html language=enus -->
## TOPIC 00009: ConfigureUserDefinedChannelArray(string, int[], int[], RFmxCdma2kMXBranch[])

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-configureuserdefinedchannelarray__string-int_arr1-int_arr1-rfmxcdma2kmxbranch_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-configureuserdefinedchannelarray__string-int_arr1-int_arr1-rfmxcdma2kmxbranch_arr1.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures all user-defined channels when you set the SetChannelConfigurationMode(string, RFmxCdma2kMXChannelConfigurationMode) method to UserDefined. Use equal-sized arrays for walshCodeLength, walshCodeNumber, and branch.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int ConfigureUserDef

### ConfigureUserDefinedChannelArray(string, int[], int[], RFmxCdma2kMXBranch[])

Configures all user-defined channels when you set the [SetChannelConfigurationMode(string, RFmxCdma2kMXChannelConfigurationMode)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setchannelconfigurationmode__string-rfmxcdma2kmxchannelconfigurationmode.html) method to [UserDefined](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchannelconfigurationmode.html). 
 Use equal-sized arrays for *walshCodeLength*, *walshCodeNumber*, and *branch*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int ConfigureUserDefinedChannelArray(string selectorString, int[] walshCodeLength, int[] walshCodeNumber, RFmxCdma2kMXBranch[] branch)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| walshCodeLength | int[] | Specifies the Walsh code length of the CDMA2k signal. |
| walshCodeNumber | int[] | Specifies the Walsh code number of the CDMA2k signal. |
| branch | RFmxCdma2kMXBranch[] | Specifies the branch on which a specific user-defined channel is mapped. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-deletesignalconfiguration.html language=enus -->
## TOPIC 00010: DeleteSignalConfiguration()

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-deletesignalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-deletesignalconfiguration.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes an instance of a signal.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int DeleteSignalConfiguration()ReturnsReturns the status code of this method. The status code either indicates success or describes a warning condition.

### DeleteSignalConfiguration()

Deletes an instance of a signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int DeleteSignalConfiguration()

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-getautolevelinitialreferencelevel__string-out.html language=enus -->
## TOPIC 00011: GetAutoLevelInitialReferenceLevel(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-getautolevelinitialreferencelevel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-getautolevelinitialreferencelevel__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the initial reference level that the AutoLevel(string, double, out double) function uses to estimate the peak power of the input signal. This value is expressed in dBm.The default value is 30 dBm. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetAutoLevelInitialReferenceLevel(str

### GetAutoLevelInitialReferenceLevel(string, out double)

Gets the initial reference level that the [AutoLevel(string, double, out double)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-autolevel__string-double-out.html) function uses to estimate the peak power of the input signal. This value is expressed in dBm.The default value is 30 dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetAutoLevelInitialReferenceLevel(string selectorString, out double value)

#### Remarks

This method gets the value of [AutoLevelInitialReferenceLevel](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the initial reference level that the AutoLevel(string, double, out double) function uses to estimate the peak power of the input signal. This value is expressed in dBm.The default value is 30 dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-getdownlinkspreadingpnoffset__string-out.html language=enus -->
## TOPIC 00012: GetDownlinkSpreadingPNOffset(string, out int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-getdownlinkspreadingpnoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-getdownlinkspreadingpnoffset__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specified the PN offset in increments of 64 chips for forward link. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetDownlinkSpreadingPNOffset(string selectorString, out int value)RemarksThis method gets the value of DownlinkSpreadingPNOffset attribute.The default value is 0.Specified

### GetDownlinkSpreadingPNOffset(string, out int)

Specified the PN offset in increments of 64 chips for forward link.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetDownlinkSpreadingPNOffset(string selectorString, out int value)

#### Remarks

This method gets the value of [DownlinkSpreadingPNOffset](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 0.

Specified the PN offset in increments of 64 chips for forward link.

This method gets the value of [DownlinkSpreadingPNOffset](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Specified the PN offset in increments of 64 chips for forward link. |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Specified the PN offset in increments of 64 chips for forward link. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-geterrorstring__int-out.html language=enus -->
## TOPIC 00013: GetErrorString(int, out string)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-geterrorstring__int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-geterrorstring__int-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the status code returned by an RFmxCDMA2k function into a string. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetErrorString(int errorCode, out string errorDescription)ParametersNameTypeDescriptionerrorCodeintSpecifies an error or warning code.errorDescriptionout stringUpon

### GetErrorString(int, out string)

Converts the status code returned by an RFmxCDMA2k function into a string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetErrorString(int errorCode, out string errorDescription)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| errorCode | int | Specifies an error or warning code. |
| errorDescription | out string | Upon return, contains the error description. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-getexternalattenuation__string-out.html language=enus -->
## TOPIC 00014: GetExternalAttenuation(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-getexternalattenuation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-getexternalattenuation__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. SyntaxNamespace: Na

### GetExternalAttenuation(string, out double)

Gets the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the *NI RF Vector Signal Analyzers Help*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetExternalAttenuation(string selectorString, out double value)

#### Remarks

This method gets the value of [ExternalAttenuation](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 0 dB.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-getuplinkspreadinglongcodemask__string-out.html language=enus -->
## TOPIC 00015: GetUplinkSpreadingLongCodeMask(string, out long)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-getuplinkspreadinglongcodemask__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-getuplinkspreadinglongcodemask__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the long code mask for reverse link spreading. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetUplinkSpreadingLongCodeMask(string selectorString, out long value)RemarksThis method gets the value of UplinkSpreadingLongCodeMask attribute.The default value is 0.ParametersNameTypeDe

### GetUplinkSpreadingLongCodeMask(string, out long)

Gets the long code mask for reverse link spreading.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetUplinkSpreadingLongCodeMask(string selectorString, out long value)

#### Remarks

This method gets the value of [UplinkSpreadingLongCodeMask](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out long | Upon return, contains the long code mask for reverse link spreading. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-obw.html language=enus -->
## TOPIC 00016: Obw

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-obw.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-obw.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxCdma2kMXObw instance that represents the OBW measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic RFmxCdma2kMXObw Obw { get; }

### Obw

Gets the [RFmxCdma2kMXObw](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxobw.html) instance that represents the OBW measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public [RFmxCdma2kMXObw](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxobw.html) Obw { get; }

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-resetattribute__string-rfmxcdma2kmxpropertyid.html language=enus -->
## TOPIC 00017: ResetAttribute(string, RFmxCdma2kMXPropertyId)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-resetattribute__string-rfmxcdma2kmxpropertyid.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-resetattribute__string-rfmxcdma2kmxpropertyid.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the attribute to its default value. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int ResetAttribute(string selectorString, RFmxCdma2kMXPropertyId attributeId)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the property being reset. Refer to the U

### ResetAttribute(string, RFmxCdma2kMXPropertyId)

Resets the attribute to its default value.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int ResetAttribute(string selectorString, RFmxCdma2kMXPropertyId attributeId)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the property being reset. Refer to the Using a Selector String (.NET) topic in the RFmx CDMA2K Help for more information about configuring the selector string. |
| attributeId | RFmxCdma2kMXPropertyId | Specifies an attribute identifier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-sendsoftwareedgetrigger.html language=enus -->
## TOPIC 00018: SendSoftwareEdgeTrigger()

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-sendsoftwareedgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-sendsoftwareedgetrigger.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a trigger to the device when you use the RFmxCDMA2k_CfgTrigger method to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this method to override a hardware trigger.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SendSof

### SendSoftwareEdgeTrigger()

Sends a trigger to the device when you use the RFmxCDMA2k_CfgTrigger method to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this method to override a hardware trigger.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SendSoftwareEdgeTrigger()

#### Remarks

1. You configure an invalid trigger.
2. You have not previously called the RFmxCdma2kMX.Initiate method.

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setattributebool__string-int-bool.html language=enus -->
## TOPIC 00019: SetAttributeBool(string, int, bool)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setattributebool__string-int-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setattributebool__string-int-bool.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a Bool attribute. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetAttributeBool(string selectorString, int attributeIdentifier, bool value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being set. Refer to the Using

### SetAttributeBool(string, int, bool)

Sets the value of a Bool attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetAttributeBool(string selectorString, int attributeIdentifier, bool value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx CDMA2k Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | bool | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setattributedouble__string-int-double.html language=enus -->
## TOPIC 00020: SetAttributeDouble(string, int, double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setattributedouble__string-int-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setattributedouble__string-int-double.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a Double attribute. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetAttributeDouble(string selectorString, int attributeIdentifier, double value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being set. Refer to the

### SetAttributeDouble(string, int, double)

Sets the value of a Double attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetAttributeDouble(string selectorString, int attributeIdentifier, double value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx CDMA2k Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | double | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setdigitaledgetriggeredge__string-rfmxcdma2kmxdigitaledgetriggeredge.html language=enus -->
## TOPIC 00021: SetDigitalEdgeTriggerEdge(string, RFmxCdma2kMXDigitalEdgeTriggerEdge)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setdigitaledgetriggeredge__string-rfmxcdma2kmxdigitaledgetriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setdigitaledgetriggeredge__string-rfmxcdma2kmxdigitaledgetriggeredge.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxCdma2kMXTriggerType) method to DigitalEdge. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetDigitalEdgeTriggerEdge(string selectorString, RFmxCdma2kMXDigitalEdgeTriggerEdge valu

### SetDigitalEdgeTriggerEdge(string, RFmxCdma2kMXDigitalEdgeTriggerEdge)

Sets the active edge for the trigger. This method is used only when you set the [SetTriggerType(string, RFmxCdma2kMXTriggerType)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-settriggertype__string-rfmxcdma2kmxtriggertype.html) method to [DigitalEdge](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetDigitalEdgeTriggerEdge(string selectorString, RFmxCdma2kMXDigitalEdgeTriggerEdge value)

#### Remarks

This method sets the value of [DigitalEdgeTriggerEdge](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [Rising](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxdigitaledgetriggeredge.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxCdma2kMXDigitalEdgeTriggerEdge | Specifies the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxCdma2kMXTriggerType) method to DigitalEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setiqpoweredgetriggerslope__string-rfmxcdma2kmxiqpoweredgetriggerslope.html language=enus -->
## TOPIC 00022: SetIQPowerEdgeTriggerSlope(string, RFmxCdma2kMXIQPowerEdgeTriggerSlope)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setiqpoweredgetriggerslope__string-rfmxcdma2kmxiqpoweredgetriggerslope.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setiqpoweredgetriggerslope__string-rfmxcdma2kmxiqpoweredgetriggerslope.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This method is used only when you set the SetTriggerType(string, RFmxCdma2kMXTriggerType) me

### SetIQPowerEdgeTriggerSlope(string, RFmxCdma2kMXIQPowerEdgeTriggerSlope)

Sets whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This method is used only when you set the [SetTriggerType(string, RFmxCdma2kMXTriggerType)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-settriggertype__string-rfmxcdma2kmxtriggertype.html) method to [IQPowerEdge](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetIQPowerEdgeTriggerSlope(string selectorString, RFmxCdma2kMXIQPowerEdgeTriggerSlope value)

#### Remarks

This method sets the value of [IQPowerEdgeTriggerSlope](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [Rising](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxiqpoweredgetriggerslope.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxCdma2kMXIQPowerEdgeTriggerSlope | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This method is used only when you set the SetTriggerType(string, RFmxCdma2kMXTriggerType) method to IQPowerEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setiqpoweredgetriggersource__string-string.html language=enus -->
## TOPIC 00023: SetIQPowerEdgeTriggerSource(string, string)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setiqpoweredgetriggersource__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setiqpoweredgetriggersource__string-string.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(string, RFmxCdma2kMXTriggerType) method to IQPowerEdge. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetIQPowerEdgeTriggerSource(string selectorString, string value)R

### SetIQPowerEdgeTriggerSource(string, string)

Sets the channel from which the device monitors the trigger. This method is used only when you set the [SetTriggerType(string, RFmxCdma2kMXTriggerType)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-settriggertype__string-rfmxcdma2kmxtriggertype.html) method to [IQPowerEdge](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetIQPowerEdgeTriggerSource(string selectorString, string value)

#### Remarks

This method sets the value of [IQPowerEdgeTriggerSource](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | string | Specifies the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(string, RFmxCdma2kMXTriggerType) method to IQPowerEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setlinkdirection__string-rfmxcdma2kmxlinkdirection.html language=enus -->
## TOPIC 00024: SetLinkDirection(string, RFmxCdma2kMXLinkDirection)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setlinkdirection__string-rfmxcdma2kmxlinkdirection.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setlinkdirection__string-rfmxcdma2kmxlinkdirection.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the link direction of the received signal. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetLinkDirection(string selectorString, RFmxCdma2kMXLinkDirection value)RemarksThis method sets the value of LinkDirection attribute.The default value is Uplink.ParametersNameTypeDescriptions

### SetLinkDirection(string, RFmxCdma2kMXLinkDirection)

Sets the link direction of the received signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetLinkDirection(string selectorString, RFmxCdma2kMXLinkDirection value)

#### Remarks

This method sets the value of [LinkDirection](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [Uplink](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxlinkdirection.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxCdma2kMXLinkDirection | Specifies the link direction of the received signal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setnumberofchannels__string-int.html language=enus -->
## TOPIC 00025: SetNumberOfChannels(string, int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setnumberofchannels__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setnumberofchannels__string-int.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of user-defined channels. This method is used only when you set the SetChannelConfigurationMode(string, RFmxCdma2kMXChannelConfigurationMode) method to UserDefined. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetNumberOfChannels(string selectorString, int value)Remar

### SetNumberOfChannels(string, int)

Sets the number of user-defined channels. This method is used only when you set the [SetChannelConfigurationMode(string, RFmxCdma2kMXChannelConfigurationMode)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setchannelconfigurationmode__string-rfmxcdma2kmxchannelconfigurationmode.html) method to [UserDefined](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchannelconfigurationmode.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetNumberOfChannels(string selectorString, int value)

#### Remarks

This method sets the value of [NumberOfChannels](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of user-defined channels. This method is used only when you set the SetChannelConfigurationMode(string, RFmxCdma2kMXChannelConfigurationMode) method to UserDefined. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setreferencelevel__string-double.html language=enus -->
## TOPIC 00026: SetReferenceLevel(string, double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setreferencelevel__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setreferencelevel__string-double.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the reference level, which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and V[pk-pk] for baseband devices. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetReferenceLevel(string selectorString, double value)RemarksThi

### SetReferenceLevel(string, double)

Sets the reference level, which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and V<sub>pk-pk</sub> for baseband devices.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetReferenceLevel(string selectorString, double value)

#### Remarks

This method sets the value of [ReferenceLevel](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 0 dBm.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the reference level, which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setresultfetchtimeout__string-double.html language=enus -->
## TOPIC 00027: SetResultFetchTimeout(string, double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setresultfetchtimeout__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setresultfetchtimeout__string-double.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the time to wait before results are available. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx driver waits until the measurement is complete. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMX

### SetResultFetchTimeout(string, double)

Sets the time to wait before results are available. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx driver waits until the measurement is complete.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetResultFetchTimeout(string selectorString, double value)

#### Remarks

This method sets the value of [ResultFetchTimeout](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 10 seconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the time to wait before results are available. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx driver waits until the measurement is complete before fetching the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setselectedports__string-string.html language=enus -->
## TOPIC 00028: SetSelectedPorts(string, string)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setselectedports__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setselectedports__string-string.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the instrument port to be configured to acquire a signal. Valid values PXIe-5820/5840: "" (empty string) PXIe-5830: if0, if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Default valu

### SetSelectedPorts(string, string)

Sets the instrument port to be configured to acquire a signal. **Valid values** 
 PXIe-5820/5840: "" (empty string) 
 PXIe-5830: if0, if1 
 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel **Default values** 
 PXIe-5820/5840: "" (empty string) 
 PXIe-5830/5831/5832: if1 
 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel **Supported devices**: PXIe-5820/5830/5831/5832/5840 
</x></x>

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetSelectedPorts(string selectorString, string value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | string | Specifies the instrument port to be used by the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-settriggerdelay__string-double.html language=enus -->
## TOPIC 00029: SetTriggerDelay(string, double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-settriggerdelay__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-settriggerdelay__string-double.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the trigger delay time. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetTriggerDelay(string selectorString, double value)RemarksThis method sets the value of TriggerDelay attribute.The default value is 0 seconds.ParametersNameTypeDescriptionse

### SetTriggerDelay(string, double)

Sets the trigger delay time. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetTriggerDelay(string selectorString, double value)

#### Remarks

This method sets the value of [TriggerDelay](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 0 seconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the trigger delay time. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-settriggerminimumquiettimeduration__string-double.html language=enus -->
## TOPIC 00030: SetTriggerMinimumQuietTimeDuration(string, double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-settriggerminimumquiettimeduration__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-settriggerminimumquiettimeduration__string-double.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the SetIQPowerEdgeTriggerSlope(string, RFmxCdma2kMXIQPowerEdgeTriggerSlope) method to Rising, the signal is quiet below the trigger lev

### SetTriggerMinimumQuietTimeDuration(string, double)

Sets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the [SetIQPowerEdgeTriggerSlope(string, RFmxCdma2kMXIQPowerEdgeTriggerSlope)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setiqpoweredgetriggerslope__string-rfmxcdma2kmxiqpoweredgetriggerslope.html) method to [Rising](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxiqpoweredgetriggerslope.html), the signal is quiet below the trigger level. If you set the IQ Power Edge Slope method to [Falling](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxiqpoweredgetriggerslope.html), the signal is quiet above the trigger level.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetTriggerMinimumQuietTimeDuration(string selectorString, double value)

#### Remarks

This method sets the value of [TriggerMinimumQuietTimeDuration](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 0 seconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the SetIQPowerEdgeTriggerSlope(string, RFmxCdma2kMXIQPowerEdgeTriggerSlope) method to Rising, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope method to Falling, the signal is quiet above the trigger level. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-settriggerminimumquiettimemode__string-rfmxcdma2kmxtriggerminimumquiettimemode.html language=enus -->
## TOPIC 00031: SetTriggerMinimumQuietTimeMode(string, RFmxCdma2kMXTriggerMinimumQuietTimeMode)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-settriggerminimumquiettimemode__string-rfmxcdma2kmxtriggerminimumquiettimemode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-settriggerminimumquiettimemode__string-rfmxcdma2kmxtriggerminimumquiettimemode.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement computes the minimum quiet time used for triggering. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetTriggerMinimumQuietTimeMode(string selectorString, RFmxCdma2kMXTriggerMinimumQuietTimeMode value)RemarksThis method sets the value of TriggerMinimumQuietT

### SetTriggerMinimumQuietTimeMode(string, RFmxCdma2kMXTriggerMinimumQuietTimeMode)

Sets whether the measurement computes the minimum quiet time used for triggering.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetTriggerMinimumQuietTimeMode(string selectorString, RFmxCdma2kMXTriggerMinimumQuietTimeMode value)

#### Remarks

This method sets the value of [TriggerMinimumQuietTimeMode](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [Auto](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxtriggerminimumquiettimemode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxCdma2kMXTriggerMinimumQuietTimeMode | Specifies whether the measurement computes the minimum quiet time used for triggering. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-settriggertype__string-rfmxcdma2kmxtriggertype.html language=enus -->
## TOPIC 00032: SetTriggerType(string, RFmxCdma2kMXTriggerType)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-settriggertype__string-rfmxcdma2kmxtriggertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-settriggertype__string-rfmxcdma2kmxtriggertype.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the trigger type. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetTriggerType(string selectorString, RFmxCdma2kMXTriggerType value)RemarksThis method sets the value of TriggerType attribute.The default value is None.ParametersNameTypeDescriptionselectorStringstringPass an empty

### SetTriggerType(string, RFmxCdma2kMXTriggerType)

Sets the trigger type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetTriggerType(string selectorString, RFmxCdma2kMXTriggerType value)

#### Remarks

This method sets the value of [TriggerType](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [None](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxtriggertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxCdma2kMXTriggerType | Specifies the trigger type. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setuplinkspreadinglongcodemask__string-long.html language=enus -->
## TOPIC 00033: SetUplinkSpreadingLongCodeMask(string, long)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setuplinkspreadinglongcodemask__string-long.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setuplinkspreadinglongcodemask__string-long.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the long code mask for reverse link spreading. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetUplinkSpreadingLongCodeMask(string selectorString, long value)RemarksThis method sets the value of UplinkSpreadingLongCodeMask attribute.The default value is 0.ParametersNameTypeDescri

### SetUplinkSpreadingLongCodeMask(string, long)

Sets the long code mask for reverse link spreading.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetUplinkSpreadingLongCodeMask(string selectorString, long value)

#### Remarks

This method sets the value of [UplinkSpreadingLongCodeMask](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | long | Specifies the long code mask for reverse link spreading. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setwalshcodelength__string-int.html language=enus -->
## TOPIC 00034: SetWalshCodeLength(string, int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setwalshcodelength__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setwalshcodelength__string-int.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Walsh code length of a specific user-defined channel. This value is expressed in chips. This method is used only when you set the SetChannelConfigurationMode(string, RFmxCdma2kMXChannelConfigurationMode) method to UserDefined.Use "channel(n)" as the Selector Strings to configure or read thi

### SetWalshCodeLength(string, int)

Sets the Walsh code length of a specific user-defined channel. This value is expressed in chips. This method is used only when you set the [SetChannelConfigurationMode(string, RFmxCdma2kMXChannelConfigurationMode)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setchannelconfigurationmode__string-rfmxcdma2kmxchannelconfigurationmode.html) method to [UserDefined](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchannelconfigurationmode.html).Use "channel(n)" as the Selector Strings to configure or read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetWalshCodeLength(string selectorString, int value)

#### Remarks

This method sets the value of [WalshCodeLength](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 64.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the channel number. Example: "channel0". You can use the BuildChannelString(string, int) method to build the selector string. |
| value | int | Specifies the Walsh code length of a specific user-defined channel. This value is expressed in chips. This method is used only when you set the SetChannelConfigurationMode(string, RFmxCdma2kMXChannelConfigurationMode) method to UserDefined.Use "channel(n)" as the Selector Strings to configure or read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-slotphase.html language=enus -->
## TOPIC 00035: SlotPhase

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-slotphase.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-slotphase.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxCdma2kMXSlotPhase instance that represents the SlotPhase measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic RFmxCdma2kMXSlotPhase SlotPhase { get; }

### SlotPhase

Gets the [RFmxCdma2kMXSlotPhase](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphase.html) instance that represents the SlotPhase measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public [RFmxCdma2kMXSlotPhase](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotphase.html) SlotPhase { get; }

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-slotpower.html language=enus -->
## TOPIC 00036: SlotPower

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-slotpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-slotpower.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxCdma2kMXSlotPower instance that represents the SlotPower measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic RFmxCdma2kMXSlotPower SlotPower { get; }

### SlotPower

Gets the [RFmxCdma2kMXSlotPower](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpower.html) instance that represents the SlotPower measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public [RFmxCdma2kMXSlotPower](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxslotpower.html) SlotPower { get; }

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-waitformeasurementcomplete__string-double.html language=enus -->
## TOPIC 00037: WaitForMeasurementComplete(string, double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-waitformeasurementcomplete__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-waitformeasurementcomplete__string-double.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the specified number of seconds for all the measurements to complete.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int WaitForMeasurementComplete(string selectorString, double timeout)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the

### WaitForMeasurementComplete(string, double)

Waits for the specified number of seconds for all the measurements to complete.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int WaitForMeasurementComplete(string selectorString, double timeout)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMX Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacp-configuration.html language=enus -->
## TOPIC 00038: Configuration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacp-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacp-configuration.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxCdma2kMXAcpConfiguration instance that provides methods to configure the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic RFmxCdma2kMXAcpConfiguration Configuration { get; }

### Configuration

Gets the [RFmxCdma2kMXAcpConfiguration](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration.html) instance that provides methods to configure the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public [RFmxCdma2kMXAcpConfiguration](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration.html) Configuration { get; }

Parent topic:

RFmxCdma2kMXAcp Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-configurenumberofoffsets__string-int.html language=enus -->
## TOPIC 00039: ConfigureNumberOfOffsets(string, int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-configurenumberofoffsets__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-configurenumberofoffsets__string-int.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of offsets for the ACP measurement.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int ConfigureNumberOfOffsets(string selectorString, int numberOfOffsets)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when creatin

### ConfigureNumberOfOffsets(string, int)

Configures the number of offsets for the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int ConfigureNumberOfOffsets(string selectorString, int numberOfOffsets)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| numberOfOffsets | int | Specifies the number of offset channels. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getaveragingenabled__string-out.html language=enus -->
## TOPIC 00040: GetAveragingEnabled(string, out RFmxCdma2kMXAcpAveragingEnabled)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getaveragingenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getaveragingenabled__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable averaging for the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetAveragingEnabled(string selectorString, out RFmxCdma2kMXAcpAveragingEnabled value)RemarksThis method gets the value of AcpAveragingEnabled attribute.The default value is False.Pa

### GetAveragingEnabled(string, out RFmxCdma2kMXAcpAveragingEnabled)

Gets whether to enable averaging for the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetAveragingEnabled(string selectorString, out RFmxCdma2kMXAcpAveragingEnabled value)

#### Remarks

This method gets the value of [AcpAveragingEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxCdma2kMXAcpAveragingEnabled | Upon return, contains whether to enable averaging for the ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getfftoverlapmode__string-out.html language=enus -->
## TOPIC 00041: GetFftOverlapMode(string, out RFmxCdma2kMXAcpFftOverlapMode)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getfftoverlapmode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getfftoverlapmode__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets how the FFT overlap is applied to the acquired samples. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetFftOverlapMode(string selectorString, out RFmxCdma2kMXAcpFftOverlapMode value)RemarksThis method gets the value of AcpFftOverlapMode attribute.The default value is Disabled.Pa

### GetFftOverlapMode(string, out RFmxCdma2kMXAcpFftOverlapMode)

Gets how the FFT overlap is applied to the acquired samples.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetFftOverlapMode(string selectorString, out RFmxCdma2kMXAcpFftOverlapMode value)

#### Remarks

This method gets the value of [AcpFftOverlapMode](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [Disabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpfftoverlapmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxCdma2kMXAcpFftOverlapMode | Upon return, contains how the FFT overlap is applied to the acquired samples. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getmeasurementmethod__string-out.html language=enus -->
## TOPIC 00042: GetMeasurementMethod(string, out RFmxCdma2kMXAcpMeasurementMethod)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getmeasurementmethod__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getmeasurementmethod__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the method for performing the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetMeasurementMethod(string selectorString, out RFmxCdma2kMXAcpMeasurementMethod value)RemarksThis method gets the value of AcpMeasurementMethod attribute.The default value is Normal.Para

### GetMeasurementMethod(string, out RFmxCdma2kMXAcpMeasurementMethod)

Gets the method for performing the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetMeasurementMethod(string selectorString, out RFmxCdma2kMXAcpMeasurementMethod value)

#### Remarks

This method gets the value of [AcpMeasurementMethod](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [Normal](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpmeasurementmethod.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxCdma2kMXAcpMeasurementMethod | Upon return, contains the method for performing the ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getnoisecompensationenabled__string-out.html language=enus -->
## TOPIC 00043: GetNoiseCompensationEnabled(string, out RFmxCdma2kMXAcpNoiseCompensationEnabled)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getnoisecompensationenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getnoisecompensationenabled__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetNoiseCompensationEnabled(string selectorString, out RFmxCdma2kMXAcpNoiseCompensationEnabled value)RemarksThis method gets the

### GetNoiseCompensationEnabled(string, out RFmxCdma2kMXAcpNoiseCompensationEnabled)

Gets whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetNoiseCompensationEnabled(string selectorString, out RFmxCdma2kMXAcpNoiseCompensationEnabled value)

#### Remarks

This method gets the value of [AcpNoiseCompensationEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpnoisecompensationenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxCdma2kMXAcpNoiseCompensationEnabled | Upon return, contains whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getnumberofanalysisthreads__string-out.html language=enus -->
## TOPIC 00044: GetNumberOfAnalysisThreads(string, out int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getnumberofanalysisthreads__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getnumberofanalysisthreads__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum number of threads used for parallelism for the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetNumberOfAnalysisThreads(string selectorString, out int value)RemarksThis method gets the value of AcpNumberOfAnalysisThreads attribute.The default value is

### GetNumberOfAnalysisThreads(string, out int)

Gets the maximum number of threads used for parallelism for the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetNumberOfAnalysisThreads(string selectorString, out int value)

#### Remarks

This method gets the value of [AcpNumberOfAnalysisThreads](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the maximum number of threads used for parallelism for the ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getnumberofoffsets__string-out.html language=enus -->
## TOPIC 00045: GetNumberOfOffsets(string, out int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getnumberofoffsets__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getnumberofoffsets__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of offset channels. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetNumberOfOffsets(string selectorString, out int value)RemarksThis method gets the value of AcpNumberOfOffsets attribute.The default value is 2.ParametersNameTypeDescriptionselectorStringstringPass an e

### GetNumberOfOffsets(string, out int)

Gets the number of offset channels.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetNumberOfOffsets(string selectorString, out int value)

#### Remarks

This method gets the value of [AcpNumberOfOffsets](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 2.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of offset channels. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getoffsetintegrationbandwidth__string-out.html language=enus -->
## TOPIC 00046: GetOffsetIntegrationBandwidth(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getoffsetintegrationbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getoffsetintegrationbandwidth__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the integration bandwidth of an ACP offset channel. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetOffsetIntegrationBandwidth(string selectorString, out double value)RemarksThis method gets the value of AcpOffsetIntegrationBandwidth attribute.Para

### GetOffsetIntegrationBandwidth(string, out double)

Gets the integration bandwidth of an ACP offset channel. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetOffsetIntegrationBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [AcpOffsetIntegrationBandwidth](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the integration bandwidth of an ACP offset channel. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getrbwfiltertype__string-out.html language=enus -->
## TOPIC 00047: GetRbwFilterType(string, out RFmxCdma2kMXAcpRbwFilterType)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getrbwfiltertype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getrbwfiltertype__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the shape of the digital RBW filter. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetRbwFilterType(string selectorString, out RFmxCdma2kMXAcpRbwFilterType value)RemarksThis method gets the value of AcpRbwFilterType attribute.The default value is Gaussian.ParametersNameTypeDescri

### GetRbwFilterType(string, out RFmxCdma2kMXAcpRbwFilterType)

Gets the shape of the digital RBW filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetRbwFilterType(string selectorString, out RFmxCdma2kMXAcpRbwFilterType value)

#### Remarks

This method gets the value of [AcpRbwFilterType](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [Gaussian](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacprbwfiltertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxCdma2kMXAcpRbwFilterType | Upon return, contains the shape of the digital RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getsequentialfftsize__string-out.html language=enus -->
## TOPIC 00048: GetSequentialFftSize(string, out int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getsequentialfftsize__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getsequentialfftsize__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the FFT size, when you set the SetMeasurementMethod(string, RFmxCdma2kMXAcpMeasurementMethod) method to SequentialFft. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetSequentialFftSize(string selectorString, out int value)RemarksThis method gets the value of AcpSequentialFftSize

### GetSequentialFftSize(string, out int)

Gets the FFT size, when you set the [SetMeasurementMethod(string, RFmxCdma2kMXAcpMeasurementMethod)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setmeasurementmethod__string-rfmxcdma2kmxacpmeasurementmethod.html) method to [SequentialFft](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpmeasurementmethod.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetSequentialFftSize(string selectorString, out int value)

#### Remarks

This method gets the value of [AcpSequentialFftSize](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 512.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the FFT size, when you set the SetMeasurementMethod(string, RFmxCdma2kMXAcpMeasurementMethod) method to SequentialFft. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getsweeptimeauto__string-out.html language=enus -->
## TOPIC 00049: GetSweepTimeAuto(string, out RFmxCdma2kMXAcpSweepTimeAuto)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getsweeptimeauto__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getsweeptimeauto__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement computes the sweep time. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetSweepTimeAuto(string selectorString, out RFmxCdma2kMXAcpSweepTimeAuto value)RemarksThis method gets the value of AcpSweepTimeAuto attribute.The default value is True.ParametersNameTy

### GetSweepTimeAuto(string, out RFmxCdma2kMXAcpSweepTimeAuto)

Gets whether the measurement computes the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetSweepTimeAuto(string selectorString, out RFmxCdma2kMXAcpSweepTimeAuto value)

#### Remarks

This method gets the value of [AcpSweepTimeAuto](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpsweeptimeauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxCdma2kMXAcpSweepTimeAuto | Upon return, contains whether the measurement computes the sweep time. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getsweeptimeinterval__string-out.html language=enus -->
## TOPIC 00050: GetSweepTimeInterval(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getsweeptimeinterval__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-getsweeptimeinterval__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the sweep time when you set the SetSweepTimeAuto(string, RFmxCdma2kMXAcpSweepTimeAuto) method to False. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetSweepTimeInterval(string selectorString, out double value)RemarksThis method gets the value

### GetSweepTimeInterval(string, out double)

Gets the sweep time when you set the [SetSweepTimeAuto(string, RFmxCdma2kMXAcpSweepTimeAuto)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setsweeptimeauto__string-rfmxcdma2kmxacpsweeptimeauto.html) method to [False](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpsweeptimeauto.html). This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetSweepTimeInterval(string selectorString, out double value)

#### Remarks

This method gets the value of [AcpSweepTimeInterval](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 0.0016667 seconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the sweep time when you set the SetSweepTimeAuto(string, RFmxCdma2kMXAcpSweepTimeAuto) method to False. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setalltracesenabled__string-bool.html language=enus -->
## TOPIC 00051: SetAllTracesEnabled(string, bool)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setalltracesenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setalltracesenabled__string-bool.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the traces to be stored and retrieved after performing the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetAllTracesEnabled(string selectorString, bool value)RemarksThis method sets the value of AcpAllTracesEnabled attribute.The default value i

### SetAllTracesEnabled(string, bool)

Sets whether to enable the traces to be stored and retrieved after performing the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetAllTracesEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [AcpAllTracesEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setaveragingcount__string-int.html language=enus -->
## TOPIC 00052: SetAveragingCount(string, int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setaveragingcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setaveragingcount__string-int.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxCdma2kMXAcpAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetAveragingCount(string selectorString, int value)RemarksThis method sets the value of AcpAve

### SetAveragingCount(string, int)

Sets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxCdma2kMXAcpAveragingEnabled)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setaveragingenabled__string-rfmxcdma2kmxacpaveragingenabled.html) method to [True](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetAveragingCount(string selectorString, int value)

#### Remarks

This method sets the value of [AcpAveragingCount](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxCdma2kMXAcpAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setaveragingenabled__string-rfmxcdma2kmxacpaveragingenabled.html language=enus -->
## TOPIC 00053: SetAveragingEnabled(string, RFmxCdma2kMXAcpAveragingEnabled)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setaveragingenabled__string-rfmxcdma2kmxacpaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setaveragingenabled__string-rfmxcdma2kmxacpaveragingenabled.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable averaging for the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetAveragingEnabled(string selectorString, RFmxCdma2kMXAcpAveragingEnabled value)RemarksThis method sets the value of AcpAveragingEnabled attribute.The default value is False.Parame

### SetAveragingEnabled(string, RFmxCdma2kMXAcpAveragingEnabled)

Sets whether to enable averaging for the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetAveragingEnabled(string selectorString, RFmxCdma2kMXAcpAveragingEnabled value)

#### Remarks

This method sets the value of [AcpAveragingEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxCdma2kMXAcpAveragingEnabled | Specifies whether to enable averaging for the ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setaveragingtype__string-rfmxcdma2kmxacpaveragingtype.html language=enus -->
## TOPIC 00054: SetAveragingType(string, RFmxCdma2kMXAcpAveragingType)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setaveragingtype__string-rfmxcdma2kmxacpaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setaveragingtype__string-rfmxcdma2kmxacpaveragingtype.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetAveragingType(string selectorString, RFmxCdma2kMXAcpAveragingType value)RemarksThis method sets the value of AcpAve

### SetAveragingType(string, RFmxCdma2kMXAcpAveragingType)

Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetAveragingType(string selectorString, RFmxCdma2kMXAcpAveragingType value)

#### Remarks

This method sets the value of [AcpAveragingType](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [Rms](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpaveragingtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxCdma2kMXAcpAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setmeasurementmethod__string-rfmxcdma2kmxacpmeasurementmethod.html language=enus -->
## TOPIC 00055: SetMeasurementMethod(string, RFmxCdma2kMXAcpMeasurementMethod)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setmeasurementmethod__string-rfmxcdma2kmxacpmeasurementmethod.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setmeasurementmethod__string-rfmxcdma2kmxacpmeasurementmethod.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the method for performing the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetMeasurementMethod(string selectorString, RFmxCdma2kMXAcpMeasurementMethod value)RemarksThis method sets the value of AcpMeasurementMethod attribute.The default value is Normal.Paramete

### SetMeasurementMethod(string, RFmxCdma2kMXAcpMeasurementMethod)

Sets the method for performing the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetMeasurementMethod(string selectorString, RFmxCdma2kMXAcpMeasurementMethod value)

#### Remarks

This method sets the value of [AcpMeasurementMethod](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [Normal](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpmeasurementmethod.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxCdma2kMXAcpMeasurementMethod | Specifies the method for performing the ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setnoisecompensationenabled__string-rfmxcdma2kmxacpnoisecompensationenabled.html language=enus -->
## TOPIC 00056: SetNoiseCompensationEnabled(string, RFmxCdma2kMXAcpNoiseCompensationEnabled)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setnoisecompensationenabled__string-rfmxcdma2kmxacpnoisecompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setnoisecompensationenabled__string-rfmxcdma2kmxacpnoisecompensationenabled.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetNoiseCompensationEnabled(string selectorString, RFmxCdma2kMXAcpNoiseCompensationEnabled value)RemarksThis method sets the val

### SetNoiseCompensationEnabled(string, RFmxCdma2kMXAcpNoiseCompensationEnabled)

Sets whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetNoiseCompensationEnabled(string selectorString, RFmxCdma2kMXAcpNoiseCompensationEnabled value)

#### Remarks

This method sets the value of [AcpNoiseCompensationEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpnoisecompensationenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxCdma2kMXAcpNoiseCompensationEnabled | Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setsweeptimeauto__string-rfmxcdma2kmxacpsweeptimeauto.html language=enus -->
## TOPIC 00057: SetSweepTimeAuto(string, RFmxCdma2kMXAcpSweepTimeAuto)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setsweeptimeauto__string-rfmxcdma2kmxacpsweeptimeauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setsweeptimeauto__string-rfmxcdma2kmxacpsweeptimeauto.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement computes the sweep time. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetSweepTimeAuto(string selectorString, RFmxCdma2kMXAcpSweepTimeAuto value)RemarksThis method sets the value of AcpSweepTimeAuto attribute.The default value is True.ParametersNameTypeDe

### SetSweepTimeAuto(string, RFmxCdma2kMXAcpSweepTimeAuto)

Sets whether the measurement computes the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetSweepTimeAuto(string selectorString, RFmxCdma2kMXAcpSweepTimeAuto value)

#### Remarks

This method sets the value of [AcpSweepTimeAuto](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpsweeptimeauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxCdma2kMXAcpSweepTimeAuto | Specifies whether the measurement computes the sweep time. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setsweeptimeinterval__string-double.html language=enus -->
## TOPIC 00058: SetSweepTimeInterval(string, double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setsweeptimeinterval__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setsweeptimeinterval__string-double.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the sweep time when you set the SetSweepTimeAuto(string, RFmxCdma2kMXAcpSweepTimeAuto) method to False. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetSweepTimeInterval(string selectorString, double value)RemarksThis method sets the value of

### SetSweepTimeInterval(string, double)

Sets the sweep time when you set the [SetSweepTimeAuto(string, RFmxCdma2kMXAcpSweepTimeAuto)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setsweeptimeauto__string-rfmxcdma2kmxacpsweeptimeauto.html) method to [False](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpsweeptimeauto.html). This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetSweepTimeInterval(string selectorString, double value)

#### Remarks

This method sets the value of [AcpSweepTimeInterval](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 0.0016667 seconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the sweep time when you set the SetSweepTimeAuto(string, RFmxCdma2kMXAcpSweepTimeAuto) method to False. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpifoutputpoweroffsetauto.html language=enus -->
## TOPIC 00059: RFmxCdma2kMXAcpIFOutputPowerOffsetAuto Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpifoutputpoweroffsetauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpifoutputpoweroffsetauto.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. This method is used only if you set the SetMeasurementMethod(string, RFmxCdma2kMXAcpMeasurementMethod) method to DynamicRange. SyntaxNamespace: Nati

### RFmxCdma2kMXAcpIFOutputPowerOffsetAuto Enumeration

Specifies whether the measurement computes an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. This method is used only if you set the [SetMeasurementMethod(string, RFmxCdma2kMXAcpMeasurementMethod)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpconfiguration-setmeasurementmethod__string-rfmxcdma2kmxacpmeasurementmethod.html) method to [DynamicRange](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpmeasurementmethod.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXAcpIFOutputPowerOffsetAuto

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement does not compute an IF output power level offset for the offset channels. |
| True | 1 | The measurement computes an IF output power level offset for the offset channels. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpmeasurementmethod.html language=enus -->
## TOPIC 00060: RFmxCdma2kMXAcpMeasurementMethod Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpmeasurementmethod.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpmeasurementmethod.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method for performing the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXAcpMeasurementMethodMembersNameValueDescriptionNormal0The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this m

### RFmxCdma2kMXAcpMeasurementMethod Enumeration

Specifies the method for performing the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXAcpMeasurementMethod

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Normal | 0 | The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. |
| DynamicRange | 1 | The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5665/5668R. |
| SequentialFft | 2 | The ACP measurement acquires I/Q samples specified by the SetSweepTimeInterval(string, double) method. These samples are divided into smaller chunks. The size of each chunk is defined by the SetSequentialFftSize(string, int) method, and FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute the ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of acquisition are not used for the measurement. Use this method to optimize the ACP measurement speed. The accuracy of the results may be reduced when using this measurement method. For accurate power measurements when the power characteristics of the signal vary over time, averaging is allowed. The following methods have limited support when you set the RFmxCdma2kMXAcpConfiguration.ConfigureMeasurementMethod method to SequentialFft.The RFmxCdma2kMXAcpConfiguration.SetRbwFilterAutoBandwidth method will only support True value. The RFmxCdma2kMXAcpConfiguration.SetRbwFilterType method will only support FftBased value. The RFmxCdma2kMXAcpConfiguration.SetAveragingCount method will only support a value greater than or equal to 1. The RFmxCdma2kMXAcpConfiguration.SetNumberOfAnalysisThreads method will only support a value greater than or equal to 1. Note For multi-span FFT, the averaging count should be 1. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpnoisecompensationenabled.html language=enus -->
## TOPIC 00061: RFmxCdma2kMXAcpNoiseCompensationEnabled Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpnoisecompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpnoisecompensationenabled.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXAcpNoiseCompensationEnabledMembersNameValueDescriptionFalse0Disables compensation of the channel powers for th

### RFmxCdma2kMXAcpNoiseCompensationEnabled Enumeration

Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXAcpNoiseCompensationEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables compensation of the channel powers for the noise floor of the signal analyzer. |
| True | 1 | Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are measured again. Supported Devices: PXIe-5663/5665/5668R. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacprbwfiltertype.html language=enus -->
## TOPIC 00062: RFmxCdma2kMXAcpRbwFilterType Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacprbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacprbwfiltertype.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of the digital RBW filter. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXAcpRbwFilterTypeMembersNameValueDescriptionFftBased0An RBW filter with an FFT-based response is applied. Gaussian1An RBW filter with a Gaussian response is applied. Flat2An RBW fi

### RFmxCdma2kMXAcpRbwFilterType Enumeration

Specifies the shape of the digital RBW filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXAcpRbwFilterType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| FftBased | 0 | An RBW filter with an FFT-based response is applied. |
| Gaussian | 1 | An RBW filter with a Gaussian response is applied. |
| Flat | 2 | An RBW filter with a flat response is applied. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpresults-fetchabsolutepowerstrace__string-double-int-ref.html language=enus -->
## TOPIC 00063: FetchAbsolutePowersTrace(string, double, int, ref Spectrum< float >)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpresults-fetchabsolutepowerstrace__string-double-int-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpresults-fetchabsolutepowerstrace__string-double-int-ref.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the absolute powers trace for the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int FetchAbsolutePowersTrace(string selectorString, double timeout, int traceIndex, ref Spectrum< float > absolutePowersTrace)ParametersNameTypeDescriptionselectorStringstringSpecifies

### FetchAbsolutePowersTrace(string, double, int, ref Spectrum< float >)

Fetches the absolute powers trace for the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int FetchAbsolutePowersTrace(string selectorString, double timeout, int traceIndex, ref Spectrum< float > absolutePowersTrace)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| traceIndex | int | Specifies the index of the trace to fetch. The traceIndex can range from 0 to (Number of carriers + 2*Number of offsets). |
| absolutePowersTrace | ref Spectrum< float > | Returns the trace of absolute integrated power measured in the offset channel specified by the traceIndex parameter. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXAcpResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpresults-fetchcarrierabsolutepower__string-double-out.html language=enus -->
## TOPIC 00064: FetchCarrierAbsolutePower(string, double, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpresults-fetchcarrierabsolutepower__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpresults-fetchcarrierabsolutepower__string-double-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute carrier power.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int FetchCarrierAbsolutePower(string selectorString, double timeout, out double carrierAbsolutePower)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the result name.

### FetchCarrierAbsolutePower(string, double, out double)

Returns the absolute carrier power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int FetchCarrierAbsolutePower(string selectorString, double timeout, out double carrierAbsolutePower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| carrierAbsolutePower | out double | Upon return, contains the averaged channel power measured in the specified integration bandwidth. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXAcpResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpresults-getloweroffsetabsolutepower__string-out.html language=enus -->
## TOPIC 00065: GetLowerOffsetAbsolutePower(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpresults-getloweroffsetabsolutepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxacpresults-getloweroffsetabsolutepower__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the absolute measured lower offset channel power. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetLowerOffsetAbsolutePower(string selectorString, out double value)RemarksThis method gets

### GetLowerOffsetAbsolutePower(string, out double)

Gets the absolute measured lower offset channel power. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetLowerOffsetAbsolutePower(string selectorString, out double value)

#### Remarks

This method gets the value of [AcpResultsLowerOffsetAbsolutePower](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the absolute measured lower offset channel power. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXAcpResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxbranch.html language=enus -->
## TOPIC 00066: RFmxCdma2kMXBranch Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxbranch.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxbranch.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the branch on which a specific user-defined channel is mapped. This method is used only when you set the SetChannelConfigurationMode(string, RFmxCdma2kMXChannelConfigurationMode) method to UserDefined.Use "channel(n)" as the Selector Strings to configure or read this method. SyntaxNamespac

### RFmxCdma2kMXBranch Enumeration

Specifies the branch on which a specific user-defined channel is mapped. This method is used only when you set the [SetChannelConfigurationMode(string, RFmxCdma2kMXChannelConfigurationMode)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setchannelconfigurationmode__string-rfmxcdma2kmxchannelconfigurationmode.html) method to [UserDefined](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchannelconfigurationmode.html).Use "channel(n)" as the Selector Strings to configure or read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXBranch

#### Members

| Name | Value | Description |
| --- | --- | --- |
| I | 0 | Specifies the in-phase branch. |
| Q | 1 | Specifies the quadrature branch. |
| IAndQ | 2 | Specifies the in-phase and quadrature branch. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-configuremeasurementchannel__string-int-int-rfmxcdma2kmxcdameasurementchannelbranch.html language=enus -->
## TOPIC 00067: ConfigureMeasurementChannel(string, int, int, RFmxCdma2kMXCdaMeasurementChannelBranch)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-configuremeasurementchannel__string-int-int-rfmxcdma2kmxcdameasurementchannelbranch.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-configuremeasurementchannel__string-int-int-rfmxcdma2kmxcdameasurementchannelbranch.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int ConfigureMeasurementChannel(string selectorString, int walshCodeLength, int walshCodeNumber, RFmxCdma2kMXCdaMeasurementChannelBranch

### ConfigureMeasurementChannel(string, int, int, RFmxCdma2kMXCdaMeasurementChannelBranch)

Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int ConfigureMeasurementChannel(string selectorString, int walshCodeLength, int walshCodeNumber, RFmxCdma2kMXCdaMeasurementChannelBranch branch)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| walshCodeLength | int | Specifies the Walsh code length of a channel subject to channel specific analysis. |
| walshCodeNumber | int | Specifies the Walsh code number of a channel subject to channel specific analysis. |
| branch | RFmxCdma2kMXCdaMeasurementChannelBranch | Specifies the branch of a channel subject to channel specific analysis. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXCdaConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-configurepowerunit__string-rfmxcdma2kmxcdapowerunit.html language=enus -->
## TOPIC 00068: ConfigurePowerUnit(string, RFmxCdma2kMXCdaPowerUnit)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-configurepowerunit__string-rfmxcdma2kmxcdapowerunit.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-configurepowerunit__string-rfmxcdma2kmxcdapowerunit.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the powerUnit parameter for the code domain power results, except for the totalPower parameter.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int ConfigurePowerUnit(string selectorString, RFmxCdma2kMXCdaPowerUnit powerUnit)ParametersNameTypeDescriptionselectorStringstringPass an

### ConfigurePowerUnit(string, RFmxCdma2kMXCdaPowerUnit)

Configures the *powerUnit* parameter for the code domain power results, except for the *totalPower* parameter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int ConfigurePowerUnit(string selectorString, RFmxCdma2kMXCdaPowerUnit powerUnit)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| powerUnit | RFmxCdma2kMXCdaPowerUnit | Specifies the measurement unit of the measured code domain power results. This value is expressed in dB/dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXCdaConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-configuresynchronizationmodeandinterval__string-rfmxcdma2kmxcdasynchronizationmode-int-int.html language=enus -->
## TOPIC 00069: ConfigureSynchronizationModeAndInterval(string, RFmxCdma2kMXCdaSynchronizationMode, int, int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-configuresynchronizationmodeandinterval__string-rfmxcdma2kmxcdasynchronizationmode-int-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-configuresynchronizationmodeandinterval__string-rfmxcdma2kmxcdasynchronizationmode-int-int.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the synchronizationMode, measurementOffset, and measurementLength parameters for the code domain analysis (CDA) measurement.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int ConfigureSynchronizationModeAndInterval(string selectorString, RFmxCdma2kMXCdaSynchronizationMode synchr

### ConfigureSynchronizationModeAndInterval(string, RFmxCdma2kMXCdaSynchronizationMode, int, int)

Configures the *synchronizationMode*, *measurementOffset*, and *measurementLength* parameters for the code domain analysis (CDA) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int ConfigureSynchronizationModeAndInterval(string selectorString, RFmxCdma2kMXCdaSynchronizationMode synchronizationMode, int measurementOffset, int measurementLength)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| synchronizationMode | RFmxCdma2kMXCdaSynchronizationMode | Specifies whether the measurement is performed from the frame, slot, or symbol boundary. |
| measurementOffset | int | Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the synchronizationMode parameter. This value is expressed in slots. |
| measurementLength | int | Specifies the duration of code domain measurement. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXCdaConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00070: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the traces to be stored and retrieved after performing the code domain analysis (CDA). SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method gets the value of CdaAllTracesEnabled attribute.The

### GetAllTracesEnabled(string, out bool)

Gets whether to enable the traces to be stored and retrieved after performing the code domain analysis (CDA).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [CdaAllTracesEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the traces to be stored and retrieved after performing the code domain analysis (CDA). |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXCdaConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-getbasespreadingfactor__string-out.html language=enus -->
## TOPIC 00071: GetBaseSpreadingFactor(string, out int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-getbasespreadingfactor__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-getbasespreadingfactor__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the base spreading factor used to calculate the code domain power traces. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetBaseSpreadingFactor(string selectorString, out int value)RemarksThis method gets the value of CdaBaseSpreadingFactor attribute.The default value is 64. The v

### GetBaseSpreadingFactor(string, out int)

Gets the base spreading factor used to calculate the code domain power traces.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetBaseSpreadingFactor(string selectorString, out int value)

#### Remarks

This method gets the value of [CdaBaseSpreadingFactor](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 64. The valid values are 2, 4, 8, 16, 32, and 64.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the base spreading factor used to calculate the code domain power traces. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXCdaConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-getmeasurementoffset__string-out.html language=enus -->
## TOPIC 00072: GetMeasurementOffset(string, out int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-getmeasurementoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-getmeasurementoffset__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxCdma2kMXCdaSynchronizationMode) method. This value is expressed in slots. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetMeasure

### GetMeasurementOffset(string, out int)

Gets the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the [SetSynchronizationMode(string, RFmxCdma2kMXCdaSynchronizationMode)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-setsynchronizationmode__string-rfmxcdma2kmxcdasynchronizationmode.html) method. This value is expressed in slots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetMeasurementOffset(string selectorString, out int value)

#### Remarks

This method gets the value of [CdaMeasurementOffset](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 0. The valid values are 1 to 15, inclusive. The sum of the CDA measurement offset and the CDA measurement length must be less than or equal to 16.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxCdma2kMXCdaSynchronizationMode) method. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXCdaConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-setiqgainimbalanceremovalenabled__string-rfmxcdma2kmxcdaiqgainimbalanceremovalenabled.html language=enus -->
## TOPIC 00073: SetIQGainImbalanceRemovalEnabled(string, RFmxCdma2kMXCdaIQGainImbalanceRemovalEnabled)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-setiqgainimbalanceremovalenabled__string-rfmxcdma2kmxcdaiqgainimbalanceremovalenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-setiqgainimbalanceremovalenabled__string-rfmxcdma2kmxcdaiqgainimbalanceremovalenabled.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to remove the I/Q gain imbalance before the code domain analysis (CDA) measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetIQGainImbalanceRemovalEnabled(string selectorString, RFmxCdma2kMXCdaIQGainImbalanceRemovalEnabled value)RemarksThis method sets the value o

### SetIQGainImbalanceRemovalEnabled(string, RFmxCdma2kMXCdaIQGainImbalanceRemovalEnabled)

Sets whether to remove the I/Q gain imbalance before the code domain analysis (CDA) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetIQGainImbalanceRemovalEnabled(string selectorString, RFmxCdma2kMXCdaIQGainImbalanceRemovalEnabled value)

#### Remarks

This method sets the value of [CdaIQGainImbalanceRemovalEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaiqgainimbalanceremovalenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxCdma2kMXCdaIQGainImbalanceRemovalEnabled | Specifies whether to remove the I/Q gain imbalance before the code domain analysis (CDA) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXCdaConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-setiqoffsetremovalenabled__string-rfmxcdma2kmxcdaiqoffsetremovalenabled.html language=enus -->
## TOPIC 00074: SetIQOffsetRemovalEnabled(string, RFmxCdma2kMXCdaIQOffsetRemovalEnabled)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-setiqoffsetremovalenabled__string-rfmxcdma2kmxcdaiqoffsetremovalenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-setiqoffsetremovalenabled__string-rfmxcdma2kmxcdaiqoffsetremovalenabled.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to remove I/Q offset before the code domain analysis (CDA) measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetIQOffsetRemovalEnabled(string selectorString, RFmxCdma2kMXCdaIQOffsetRemovalEnabled value)RemarksThis method sets the value of CdaIQOffsetRemovalEnable

### SetIQOffsetRemovalEnabled(string, RFmxCdma2kMXCdaIQOffsetRemovalEnabled)

Sets whether to remove I/Q offset before the code domain analysis (CDA) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetIQOffsetRemovalEnabled(string selectorString, RFmxCdma2kMXCdaIQOffsetRemovalEnabled value)

#### Remarks

This method sets the value of [CdaIQOffsetRemovalEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaiqoffsetremovalenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxCdma2kMXCdaIQOffsetRemovalEnabled | Specifies whether to remove I/Q offset before the code domain analysis (CDA) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXCdaConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-setiqquadratureerrorremovalenabled__string-rfmxcdma2kmxcdaiqquadratureerrorremovalenabled.html language=enus -->
## TOPIC 00075: SetIQQuadratureErrorRemovalEnabled(string, RFmxCdma2kMXCdaIQQuadratureErrorRemovalEnabled)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-setiqquadratureerrorremovalenabled__string-rfmxcdma2kmxcdaiqquadratureerrorremovalenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-setiqquadratureerrorremovalenabled__string-rfmxcdma2kmxcdaiqquadratureerrorremovalenabled.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to remove the I/Q quadrature error before the code domain analysis (CDA) measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetIQQuadratureErrorRemovalEnabled(string selectorString, RFmxCdma2kMXCdaIQQuadratureErrorRemovalEnabled value)RemarksThis method sets the v

### SetIQQuadratureErrorRemovalEnabled(string, RFmxCdma2kMXCdaIQQuadratureErrorRemovalEnabled)

Sets whether to remove the I/Q quadrature error before the code domain analysis (CDA) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetIQQuadratureErrorRemovalEnabled(string selectorString, RFmxCdma2kMXCdaIQQuadratureErrorRemovalEnabled value)

#### Remarks

This method sets the value of [CdaIQQuadratureErrorRemovalEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaiqquadratureerrorremovalenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxCdma2kMXCdaIQQuadratureErrorRemovalEnabled | Specifies whether to remove the I/Q quadrature error before the code domain analysis (CDA) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXCdaConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-setmeasurementchannelbranch__string-rfmxcdma2kmxcdameasurementchannelbranch.html language=enus -->
## TOPIC 00076: SetMeasurementChannelBranch(string, RFmxCdma2kMXCdaMeasurementChannelBranch)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-setmeasurementchannelbranch__string-rfmxcdma2kmxcdameasurementchannelbranch.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-setmeasurementchannelbranch__string-rfmxcdma2kmxcdameasurementchannelbranch.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Walsh branch of a channel subject to channel specific analysis. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetMeasurementChannelBranch(string selectorString, RFmxCdma2kMXCdaMeasurementChannelBranch value)RemarksThis method sets the value of CdaMeasurementChannelBranch attr

### SetMeasurementChannelBranch(string, RFmxCdma2kMXCdaMeasurementChannelBranch)

Sets the Walsh branch of a channel subject to channel specific analysis.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetMeasurementChannelBranch(string selectorString, RFmxCdma2kMXCdaMeasurementChannelBranch value)

#### Remarks

This method sets the value of [CdaMeasurementChannelBranch](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [I](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdameasurementchannelbranch.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxCdma2kMXCdaMeasurementChannelBranch | Specifies the branch of a channel subject to channel specific analysis. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXCdaConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration.html language=enus -->
## TOPIC 00077: RFmxCdma2kMXCdaConfiguration Class

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the CDA measurement. Derives fromRFmxCdma2kMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic class RFmxCdma2kMXCdaConfiguration : RFmxCdma2kMXSubObjectMethodsNameDescriptionConfigureMeasurementChannel(string, int, int, RFmxCdma2kMXCdaMeasurementChannel

### RFmxCdma2kMXCdaConfiguration Class

Provides methods to configure the CDA measurement.

#### Derives from

- RFmxCdma2kMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public class RFmxCdma2kMXCdaConfiguration : RFmxCdma2kMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| ConfigureMeasurementChannel(string, int, int, RFmxCdma2kMXCdaMeasurementChannelBranch) | Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured. |
| ConfigurePowerUnit(string, RFmxCdma2kMXCdaPowerUnit) | Configures the powerUnit parameter for the code domain power results, except for the totalPower parameter. |
| ConfigureSynchronizationModeAndInterval(string, RFmxCdma2kMXCdaSynchronizationMode, int, int) | Configures the synchronizationMode, measurementOffset, and measurementLength parameters for the code domain analysis (CDA) measurement. |
| GetAllTracesEnabled(string, out bool) | Gets whether to enable the traces to be stored and retrieved after performing the code domain analysis (CDA). |
| GetBaseSpreadingFactor(string, out int) | Gets the base spreading factor used to calculate the code domain power traces. |
| GetIQGainImbalanceRemovalEnabled(string, out RFmxCdma2kMXCdaIQGainImbalanceRemovalEnabled) | Gets whether to remove the I/Q gain imbalance before the code domain analysis (CDA) measurement. |
| GetIQOffsetRemovalEnabled(string, out RFmxCdma2kMXCdaIQOffsetRemovalEnabled) | Gets whether to remove I/Q offset before the code domain analysis (CDA) measurement. |
| GetIQQuadratureErrorRemovalEnabled(string, out RFmxCdma2kMXCdaIQQuadratureErrorRemovalEnabled) | Gets whether to remove the I/Q quadrature error before the code domain analysis (CDA) measurement. |
| GetMeasurementChannelBranch(string, out RFmxCdma2kMXCdaMeasurementChannelBranch) | Gets the Walsh branch of a channel subject to channel specific analysis. |
| GetMeasurementChannelWalshCodeLength(string, out int) | Gets the Walsh code length of a channel subject to channel specific analysis. |
| GetMeasurementChannelWalshCodeNumber(string, out int) | Gets the Walsh code number of a channel subject to channel specific analysis. |
| GetMeasurementEnabled(string, out bool) | Gets whether to enable the code domain analysis (CDA) measurement. |
| GetMeasurementLength(string, out int) | Gets the duration of code domain measurement. This value is expressed in slots. |
| GetMeasurementOffset(string, out int) | Gets the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxCdma2kMXCdaSynchronizationMode) method. This value is expressed in slots. |
| GetPowerUnit(string, out RFmxCdma2kMXCdaPowerUnit) | Gets the measurement unit of the measured code domain power results. |
| GetReceiveFilterEnabled(string, out RFmxCdma2kMXCdaReceiveFilterEnabled) | Gets whether to enable the received filter for the code domain analysis (CDA) measurement. Use this method to disable the filter, if the received signal is already filtered. |
| GetSpectrumInverted(string, out RFmxCdma2kMXCdaSpectrumInverted) | Gets whether the spectrum of the signal is inverted. |
| GetSynchronizationMode(string, out RFmxCdma2kMXCdaSynchronizationMode) | Gets whether the measurement is performed from the frame, slot, or symbol boundary. |
| SetAllTracesEnabled(string, bool) | Sets whether to enable the traces to be stored and retrieved after performing the code domain analysis (CDA). |
| SetBaseSpreadingFactor(string, int) | Sets the base spreading factor used to calculate the code domain power traces. |
| SetIQGainImbalanceRemovalEnabled(string, RFmxCdma2kMXCdaIQGainImbalanceRemovalEnabled) | Sets whether to remove the I/Q gain imbalance before the code domain analysis (CDA) measurement. |
| SetIQOffsetRemovalEnabled(string, RFmxCdma2kMXCdaIQOffsetRemovalEnabled) | Sets whether to remove I/Q offset before the code domain analysis (CDA) measurement. |
| SetIQQuadratureErrorRemovalEnabled(string, RFmxCdma2kMXCdaIQQuadratureErrorRemovalEnabled) | Sets whether to remove the I/Q quadrature error before the code domain analysis (CDA) measurement. |
| SetMeasurementChannelBranch(string, RFmxCdma2kMXCdaMeasurementChannelBranch) | Sets the Walsh branch of a channel subject to channel specific analysis. |
| SetMeasurementChannelWalshCodeLength(string, int) | Sets the Walsh code length of a channel subject to channel specific analysis. |
| SetMeasurementChannelWalshCodeNumber(string, int) | Sets the Walsh code number of a channel subject to channel specific analysis. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable the code domain analysis (CDA) measurement. |
| SetMeasurementLength(string, int) | Sets the duration of code domain measurement. This value is expressed in slots. |
| SetMeasurementOffset(string, int) | Sets the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxCdma2kMXCdaSynchronizationMode) method. This value is expressed in slots. |
| SetPowerUnit(string, RFmxCdma2kMXCdaPowerUnit) | Sets the measurement unit of the measured code domain power results. |
| SetReceiveFilterEnabled(string, RFmxCdma2kMXCdaReceiveFilterEnabled) | Sets whether to enable the received filter for the code domain analysis (CDA) measurement. Use this method to disable the filter, if the received signal is already filtered. |
| SetSpectrumInverted(string, RFmxCdma2kMXCdaSpectrumInverted) | Sets whether the spectrum of the signal is inverted. |
| SetSynchronizationMode(string, RFmxCdma2kMXCdaSynchronizationMode) | Sets whether the measurement is performed from the frame, slot, or symbol boundary. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdameasurementchannelbranch.html language=enus -->
## TOPIC 00078: RFmxCdma2kMXCdaMeasurementChannelBranch Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdameasurementchannelbranch.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdameasurementchannelbranch.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the branch of a channel subject to channel specific analysis. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXCdaMeasurementChannelBranchMembersNameValueDescriptionI0Specifies the in-phase branch. Q1Specifies the quadrature branch.

### RFmxCdma2kMXCdaMeasurementChannelBranch Enumeration

Specifies the branch of a channel subject to channel specific analysis.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXCdaMeasurementChannelBranch

#### Members

| Name | Value | Description |
| --- | --- | --- |
| I | 0 | Specifies the in-phase branch. |
| Q | 1 | Specifies the quadrature branch. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdapowerunit.html language=enus -->
## TOPIC 00079: RFmxCdma2kMXCdaPowerUnit Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdapowerunit.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdapowerunit.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement unit of the measured code domain power results. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXCdaPowerUnitMembersNameValueDescriptiondB0The CDA measurement results are reported in dB. dBm1The CDA measurement results are reported in dBm.

### RFmxCdma2kMXCdaPowerUnit Enumeration

Specifies the measurement unit of the measured code domain power results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXCdaPowerUnit

#### Members

| Name | Value | Description |
| --- | --- | --- |
| dB | 0 | The CDA measurement results are reported in dB. |
| dBm | 1 | The CDA measurement results are reported in dBm. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaresults-getmeaninactivepower__string-out.html language=enus -->
## TOPIC 00080: GetMeanInactivePower(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaresults-getmeaninactivepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaresults-getmeaninactivepower__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average code power, measured among the set of inactive channels, in the code domain of the base spreading factor. If you set the SetPowerUnit(string, RFmxCdma2kMXCdaPowerUnit) method to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value re

### GetMeanInactivePower(string, out double)

Gets the average code power, measured among the set of inactive channels, in the code domain of the base spreading factor. If you set the [SetPowerUnit(string, RFmxCdma2kMXCdaPowerUnit)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-setpowerunit__string-rfmxcdma2kmxcdapowerunit.html) method to [dBm](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdapowerunit.html), this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetMeanInactivePower(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsMeanInactivePower](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the average code power, measured among the set of inactive channels, in the code domain of the base spreading factor. If you set the SetPowerUnit(string, RFmxCdma2kMXCdaPowerUnit) method to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXCdaResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaresults-getmeanpilotpower__string-out.html language=enus -->
## TOPIC 00081: GetMeanPilotPower(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaresults-getmeanpilotpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaresults-getmeanpilotpower__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean power of the R-PICH.Gets the mean power value in dB, when you set the SetPowerUnit(string, RFmxCdma2kMXCdaPowerUnit) method to dB.Gets the mean power value in dBm, when you set the CDA Pwr Unit method to dBm. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetMeanPilotPowe

### GetMeanPilotPower(string, out double)

Gets the mean power of the R-PICH.Gets the mean power value in dB, when you set the [SetPowerUnit(string, RFmxCdma2kMXCdaPowerUnit)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-setpowerunit__string-rfmxcdma2kmxcdapowerunit.html) method to [dB](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdapowerunit.html).Gets the mean power value in dBm, when you set the CDA Pwr Unit method to [dBm](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdapowerunit.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetMeanPilotPower(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsMeanPilotPower](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean power of the R-PICH.Upon return, contains the mean power value in dB, when you set the SetPowerUnit(string, RFmxCdma2kMXCdaPowerUnit) method to dB.Upon return, contains the mean power value in dBm, when you set the CDA Pwr Unit method to dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXCdaResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaresults-getpeakactivepower__string-out.html language=enus -->
## TOPIC 00082: GetPeakActivePower(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaresults-getpeakactivepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaresults-getpeakactivepower__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum power among all active code channels. If you set the SetPowerUnit(string, RFmxCdma2kMXCdaPowerUnit) method to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power method. SyntaxNamespace: Nation

### GetPeakActivePower(string, out double)

Gets the maximum power among all active code channels. If you set the [SetPowerUnit(string, RFmxCdma2kMXCdaPowerUnit)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-setpowerunit__string-rfmxcdma2kmxcdapowerunit.html) method to [dBm](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdapowerunit.html), this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetPeakActivePower(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsPeakActivePower](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum power among all active code channels. If you set the SetPowerUnit(string, RFmxCdma2kMXCdaPowerUnit) method to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXCdaResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaresults-getqpeakinactivepower__string-out.html language=enus -->
## TOPIC 00083: GetQPeakInactivePower(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaresults-getqpeakinactivepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaresults-getqpeakinactivepower__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum measured code power among the set of inactive channels on the Q-branch and in the code domain of the base spreading factor. If you set the SetPowerUnit(string, RFmxCdma2kMXCdaPowerUnit) method to dBm, this measurement returns the absolute measured power; otherwise, this measurement

### GetQPeakInactivePower(string, out double)

Gets the maximum measured code power among the set of inactive channels on the Q-branch and in the code domain of the base spreading factor. If you set the [SetPowerUnit(string, RFmxCdma2kMXCdaPowerUnit)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdaconfiguration-setpowerunit__string-rfmxcdma2kmxcdapowerunit.html) method to [dBm](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxcdapowerunit.html), this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetQPeakInactivePower(string selectorString, out double value)

#### Remarks

This method gets the value of [CdaResultsQPeakInactivePower](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum measured code power among the set of inactive channels on the Q-branch and in the code domain of the base spreading factor. If you set the SetPowerUnit(string, RFmxCdma2kMXCdaPowerUnit) method to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXCdaResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration-getaveragingtype__string-out.html language=enus -->
## TOPIC 00084: GetAveragingType(string, out RFmxCdma2kMXChpAveragingType)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration-getaveragingtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration-getaveragingtype__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the CHP measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetAveragingType(string selectorString, out RFmxCdma2kMXChpAveragingType value)RemarksThis method gets the value o

### GetAveragingType(string, out RFmxCdma2kMXChpAveragingType)

Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the CHP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetAveragingType(string selectorString, out RFmxCdma2kMXChpAveragingType value)

#### Remarks

This method gets the value of [ChpAveragingType](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [Rms](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpaveragingtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxCdma2kMXChpAveragingType | Upon return, contains the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the CHP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration-getintegrationbandwidth__string-out.html language=enus -->
## TOPIC 00085: GetIntegrationBandwidth(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration-getintegrationbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration-getintegrationbandwidth__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the CHP carrier integration bandwidth. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetIntegrationBandwidth(string selectorString, out double value)RemarksThis method gets the value of ChpIntegrationBandwidth attribute.ParametersNameTypeDescription

### GetIntegrationBandwidth(string, out double)

Gets the CHP carrier integration bandwidth. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetIntegrationBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [ChpIntegrationBandwidth](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the CHP carrier integration bandwidth. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration-getsweeptimeauto__string-out.html language=enus -->
## TOPIC 00086: GetSweepTimeAuto(string, out RFmxCdma2kMXChpSweepTimeAuto)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration-getsweeptimeauto__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration-getsweeptimeauto__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement computes the sweep time. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetSweepTimeAuto(string selectorString, out RFmxCdma2kMXChpSweepTimeAuto value)RemarksThis method gets the value of ChpSweepTimeAuto attribute.The default value is True.ParametersNameTy

### GetSweepTimeAuto(string, out RFmxCdma2kMXChpSweepTimeAuto)

Gets whether the measurement computes the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetSweepTimeAuto(string selectorString, out RFmxCdma2kMXChpSweepTimeAuto value)

#### Remarks

This method gets the value of [ChpSweepTimeAuto](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpsweeptimeauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxCdma2kMXChpSweepTimeAuto | Upon return, contains whether the measurement computes the sweep time. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration-setaveragingcount__string-int.html language=enus -->
## TOPIC 00087: SetAveragingCount(string, int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration-setaveragingcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration-setaveragingcount__string-int.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxCdma2kMXChpAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetAveragingCount(string selectorString, int value)RemarksThis method sets the value of ChpAve

### SetAveragingCount(string, int)

Sets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxCdma2kMXChpAveragingEnabled)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration-setaveragingenabled__string-rfmxcdma2kmxchpaveragingenabled.html) method to [True](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetAveragingCount(string selectorString, int value)

#### Remarks

This method sets the value of [ChpAveragingCount](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxCdma2kMXChpAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration-setnumberofanalysisthreads__string-int.html language=enus -->
## TOPIC 00088: SetNumberOfAnalysisThreads(string, int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration-setnumberofanalysisthreads__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration-setnumberofanalysisthreads__string-int.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the maximum number of threads used for parallelism for the CHP measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetNumberOfAnalysisThreads(string selectorString, int value)RemarksThis method sets the value of ChpNumberOfAnalysisThreads attribute.The default value is 1.P

### SetNumberOfAnalysisThreads(string, int)

Sets the maximum number of threads used for parallelism for the CHP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetNumberOfAnalysisThreads(string selectorString, int value)

#### Remarks

This method sets the value of [ChpNumberOfAnalysisThreads](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the maximum number of threads used for parallelism for the CHP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration-setrbwfiltertype__string-rfmxcdma2kmxchprbwfiltertype.html language=enus -->
## TOPIC 00089: SetRbwFilterType(string, RFmxCdma2kMXChpRbwFilterType)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration-setrbwfiltertype__string-rfmxcdma2kmxchprbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration-setrbwfiltertype__string-rfmxcdma2kmxchprbwfiltertype.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the shape of the digital RBW filter. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetRbwFilterType(string selectorString, RFmxCdma2kMXChpRbwFilterType value)RemarksThis method sets the value of ChpRbwFilterType attribute.The default value is Gaussian.ParametersNameTypeDescriptio

### SetRbwFilterType(string, RFmxCdma2kMXChpRbwFilterType)

Sets the shape of the digital RBW filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetRbwFilterType(string selectorString, RFmxCdma2kMXChpRbwFilterType value)

#### Remarks

This method sets the value of [ChpRbwFilterType](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [Gaussian](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchprbwfiltertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxCdma2kMXChpRbwFilterType | Specifies the shape of the digital RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration-setsweeptimeauto__string-rfmxcdma2kmxchpsweeptimeauto.html language=enus -->
## TOPIC 00090: SetSweepTimeAuto(string, RFmxCdma2kMXChpSweepTimeAuto)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration-setsweeptimeauto__string-rfmxcdma2kmxchpsweeptimeauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration-setsweeptimeauto__string-rfmxcdma2kmxchpsweeptimeauto.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement computes the sweep time. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetSweepTimeAuto(string selectorString, RFmxCdma2kMXChpSweepTimeAuto value)RemarksThis method sets the value of ChpSweepTimeAuto attribute.The default value is True.ParametersNameTypeDe

### SetSweepTimeAuto(string, RFmxCdma2kMXChpSweepTimeAuto)

Sets whether the measurement computes the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetSweepTimeAuto(string selectorString, RFmxCdma2kMXChpSweepTimeAuto value)

#### Remarks

This method sets the value of [ChpSweepTimeAuto](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpsweeptimeauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxCdma2kMXChpSweepTimeAuto | Specifies whether the measurement computes the sweep time. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration-setsweeptimeinterval__string-double.html language=enus -->
## TOPIC 00091: SetSweepTimeInterval(string, double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration-setsweeptimeinterval__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration-setsweeptimeinterval__string-double.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the sweep time when you set the SetSweepTimeAuto(string, RFmxCdma2kMXChpSweepTimeAuto) method to False. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetSweepTimeInterval(string selectorString, double value)RemarksThis method sets the value of

### SetSweepTimeInterval(string, double)

Sets the sweep time when you set the [SetSweepTimeAuto(string, RFmxCdma2kMXChpSweepTimeAuto)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration-setsweeptimeauto__string-rfmxcdma2kmxchpsweeptimeauto.html) method to [False](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpsweeptimeauto.html). This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetSweepTimeInterval(string selectorString, double value)

#### Remarks

This method sets the value of [ChpSweepTimeInterval](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 0.001667 seconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the sweep time when you set the SetSweepTimeAuto(string, RFmxCdma2kMXChpSweepTimeAuto) method to False. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration.html language=enus -->
## TOPIC 00092: RFmxCdma2kMXChpConfiguration Class

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpconfiguration.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the CHP measurement. Derives fromRFmxCdma2kMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic class RFmxCdma2kMXChpConfiguration : RFmxCdma2kMXSubObjectMethodsNameDescriptionConfigureAveraging(string, RFmxCdma2kMXChpAveragingEnabled, int, RFmxCdma2kMXCh

### RFmxCdma2kMXChpConfiguration Class

Provides methods to configure the CHP measurement.

#### Derives from

- RFmxCdma2kMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public class RFmxCdma2kMXChpConfiguration : RFmxCdma2kMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| ConfigureAveraging(string, RFmxCdma2kMXChpAveragingEnabled, int, RFmxCdma2kMXChpAveragingType) | Configures averaging for the CHP measurement. |
| ConfigureRbwFilter(string, RFmxCdma2kMXChpRbwAutoBandwidth, double, RFmxCdma2kMXChpRbwFilterType) | Configures the RBW filter. |
| ConfigureSweepTime(string, RFmxCdma2kMXChpSweepTimeAuto, double) | Configures the sweep time. |
| GetAllTracesEnabled(string, out bool) | Gets whether to enable the traces to be stored and retrieved after performing the CHP measurement. |
| GetAveragingCount(string, out int) | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxCdma2kMXChpAveragingEnabled) method to True. |
| GetAveragingEnabled(string, out RFmxCdma2kMXChpAveragingEnabled) | Gets whether to enable averaging for the CHP measurement. |
| GetAveragingType(string, out RFmxCdma2kMXSemAveragingType) | Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the CHP measurement. |
| GetAveragingType(string, out RFmxCdma2kMXChpAveragingType) | Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the CHP measurement. |
| GetIntegrationBandwidth(string, out double) | Gets the CHP carrier integration bandwidth. This value is expressed in Hz. |
| GetMeasurementEnabled(string, out bool) | Gets whether to enable the CHP measurement. |
| GetNumberOfAnalysisThreads(string, out int) | Gets the maximum number of threads used for parallelism for the CHP measurement. |
| GetRbwFilterAutoBandwidth(string, out RFmxCdma2kMXChpRbwAutoBandwidth) | Gets whether the measurement computes the RBW. |
| GetRbwFilterBandwidth(string, out double) | Gets the bandwidth of the RBW filter used to sweep the acquired signal when you set the SetRbwFilterAutoBandwidth(string, RFmxCdma2kMXChpRbwAutoBandwidth) method to False. This value is expressed in Hz. |
| GetRbwFilterType(string, out RFmxCdma2kMXChpRbwFilterType) | Gets the shape of the digital RBW filter. |
| GetSweepTimeAuto(string, out RFmxCdma2kMXChpSweepTimeAuto) | Gets whether the measurement computes the sweep time. |
| GetSweepTimeInterval(string, out double) | Gets the sweep time when you set the SetSweepTimeAuto(string, RFmxCdma2kMXChpSweepTimeAuto) method to False. This value is expressed in seconds. |
| SetAllTracesEnabled(string, bool) | Sets whether to enable the traces to be stored and retrieved after performing the CHP measurement. |
| SetAveragingCount(string, int) | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxCdma2kMXChpAveragingEnabled) method to True. |
| SetAveragingEnabled(string, RFmxCdma2kMXChpAveragingEnabled) | Sets whether to enable averaging for the CHP measurement. |
| SetAveragingType(string, RFmxCdma2kMXSemAveragingType) | Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the CHP measurement. |
| SetAveragingType(string, RFmxCdma2kMXChpAveragingType) | Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the CHP measurement. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable the CHP measurement. |
| SetNumberOfAnalysisThreads(string, int) | Sets the maximum number of threads used for parallelism for the CHP measurement. |
| SetRbwFilterAutoBandwidth(string, RFmxCdma2kMXChpRbwAutoBandwidth) | Sets whether the measurement computes the RBW. |
| SetRbwFilterBandwidth(string, double) | Sets the bandwidth of the RBW filter used to sweep the acquired signal when you set the SetRbwFilterAutoBandwidth(string, RFmxCdma2kMXChpRbwAutoBandwidth) method to False. This value is expressed in Hz. |
| SetRbwFilterType(string, RFmxCdma2kMXChpRbwFilterType) | Sets the shape of the digital RBW filter. |
| SetSweepTimeAuto(string, RFmxCdma2kMXChpSweepTimeAuto) | Sets whether the measurement computes the sweep time. |
| SetSweepTimeInterval(string, double) | Sets the sweep time when you set the SetSweepTimeAuto(string, RFmxCdma2kMXChpSweepTimeAuto) method to False. This value is expressed in seconds. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchprbwautobandwidth.html language=enus -->
## TOPIC 00093: RFmxCdma2kMXChpRbwAutoBandwidth Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchprbwautobandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchprbwautobandwidth.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the RBW. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXChpRbwAutoBandwidthMembersNameValueDescriptionFalse0The measurement uses the RBW that you specify in the SetRbwFilterBandwidth(string, double) method. True1The measurement co

### RFmxCdma2kMXChpRbwAutoBandwidth Enumeration

Specifies whether the measurement computes the RBW.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXChpRbwAutoBandwidth

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement uses the RBW that you specify in the SetRbwFilterBandwidth(string, double) method. |
| True | 1 | The measurement computes the RBW. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchprbwfiltertype.html language=enus -->
## TOPIC 00094: RFmxCdma2kMXChpRbwFilterType Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchprbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchprbwfiltertype.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of the digital RBW filter. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXChpRbwFilterTypeMembersNameValueDescriptionFftBased0No RBW filtering is performed. Gaussian1An RBW filter with a Gaussian response is applied. Flat2An RBW filter with a flat respo

### RFmxCdma2kMXChpRbwFilterType Enumeration

Specifies the shape of the digital RBW filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXChpRbwFilterType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| FftBased | 0 | No RBW filtering is performed. |
| Gaussian | 1 | An RBW filter with a Gaussian response is applied. |
| Flat | 2 | An RBW filter with a flat response is applied. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpresults-fetchcarrierabsolutepower__string-double-out.html language=enus -->
## TOPIC 00095: FetchCarrierAbsolutePower(string, double, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpresults-fetchcarrierabsolutepower__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpresults-fetchcarrierabsolutepower__string-double-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute carrier power of the CHP measurement.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int FetchCarrierAbsolutePower(string selectorString, double timeout, out double carrierAbsolutePower)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string compris

### FetchCarrierAbsolutePower(string, double, out double)

Returns the absolute carrier power of the CHP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int FetchCarrierAbsolutePower(string selectorString, double timeout, out double carrierAbsolutePower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| carrierAbsolutePower | out double | Upon return, contains the averaged channel power measured in the specified integration bandwidth. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXChpResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpresults-fetchspectrum__string-double-ref.html language=enus -->
## TOPIC 00096: FetchSpectrum(string, double, ref Spectrum< float >)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpresults-fetchspectrum__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpresults-fetchspectrum__string-double-ref.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for the CHP measurement.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int FetchSpectrum(string selectorString, double timeout, ref Spectrum< float > spectrum)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the result nam

### FetchSpectrum(string, double, ref Spectrum< float >)

Fetches the spectrum used for the CHP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int FetchSpectrum(string selectorString, double timeout, ref Spectrum< float > spectrum)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| spectrum | ref Spectrum< float > | Upon return, contains the trace of power levels in the spectral domain. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXChpResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpresults-getcarrierabsolutepower__string-out.html language=enus -->
## TOPIC 00097: GetCarrierAbsolutePower(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpresults-getcarrierabsolutepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpresults-getcarrierabsolutepower__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the averaged CHP measured in the specified integration bandwidth. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetCarrierAbsolutePower(string selectorString, out double value)RemarksThis method gets the value of ChpResultsCarrierAbsolutePower attr

### GetCarrierAbsolutePower(string, out double)

Gets the averaged CHP measured in the specified integration bandwidth. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetCarrierAbsolutePower(string selectorString, out double value)

#### Remarks

This method gets the value of [ChpResultsCarrierAbsolutePower](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the averaged CHP measured in the specified integration bandwidth. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXChpResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpresults.html language=enus -->
## TOPIC 00098: RFmxCdma2kMXChpResults Class

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpresults.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the CHP measurement results. Derives fromRFmxCdma2kMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic class RFmxCdma2kMXChpResults : RFmxCdma2kMXSubObjectMethodsNameDescriptionFetchCarrierAbsolutePower(string, double, out double)Returns the absolut

### RFmxCdma2kMXChpResults Class

Provides methods to fetch and read the CHP measurement results.

#### Derives from

- RFmxCdma2kMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public class RFmxCdma2kMXChpResults : RFmxCdma2kMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchCarrierAbsolutePower(string, double, out double) | Returns the absolute carrier power of the CHP measurement. |
| FetchSpectrum(string, double, ref Spectrum< float >) | Fetches the spectrum used for the CHP measurement. |
| GetCarrierAbsolutePower(string, out double) | Gets the averaged CHP measured in the specified integration bandwidth. This value is expressed in dBm. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpsweeptimeauto.html language=enus -->
## TOPIC 00099: RFmxCdma2kMXChpSweepTimeAuto Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpsweeptimeauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchpsweeptimeauto.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the sweep time. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXChpSweepTimeAutoMembersNameValueDescriptionFalse0The measurement uses the sweep time that you specify in the SetSweepTimeInterval(string, double) method. True1The meas

### RFmxCdma2kMXChpSweepTimeAuto Enumeration

Specifies whether the measurement computes the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXChpSweepTimeAuto

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement uses the sweep time that you specify in the SetSweepTimeInterval(string, double) method. |
| True | 1 | The measurement uses the default sweep time of 0.001667 seconds. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-diopfi0.html language=enus -->
## TOPIC 00100: DioPfi0

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-diopfi0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-diopfi0.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic const string DioPfi0

### DioPfi0

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public const string DioPfi0

Parent topic:

RFmxCdma2kMXConstants Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-diopfi1.html language=enus -->
## TOPIC 00101: DioPfi1

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-diopfi1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-diopfi1.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic const string DioPfi1

### DioPfi1

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public const string DioPfi1

Parent topic:

RFmxCdma2kMXConstants Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-diopfi2.html language=enus -->
## TOPIC 00102: DioPfi2

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-diopfi2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-diopfi2.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic const string DioPfi2

### DioPfi2

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public const string DioPfi2

Parent topic:

RFmxCdma2kMXConstants Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-diopfi3.html language=enus -->
## TOPIC 00103: DioPfi3

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-diopfi3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-diopfi3.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic const string DioPfi3

### DioPfi3

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public const string DioPfi3

Parent topic:

RFmxCdma2kMXConstants Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-diopfi4.html language=enus -->
## TOPIC 00104: DioPfi4

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-diopfi4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-diopfi4.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic const string DioPfi4

### DioPfi4

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public const string DioPfi4

Parent topic:

RFmxCdma2kMXConstants Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-diopfi5.html language=enus -->
## TOPIC 00105: DioPfi5

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-diopfi5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-diopfi5.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic const string DioPfi5

### DioPfi5

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public const string DioPfi5

Parent topic:

RFmxCdma2kMXConstants Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-diopfi6.html language=enus -->
## TOPIC 00106: DioPfi6

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-diopfi6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-diopfi6.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic const string DioPfi6

### DioPfi6

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public const string DioPfi6

Parent topic:

RFmxCdma2kMXConstants Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-diopfi7.html language=enus -->
## TOPIC 00107: DioPfi7

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-diopfi7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-diopfi7.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic const string DioPfi7

### DioPfi7

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public const string DioPfi7

Parent topic:

RFmxCdma2kMXConstants Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pfi0.html language=enus -->
## TOPIC 00108: Pfi0

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pfi0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pfi0.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PFI 1 connector on the PXI-5142 and PXIe-5622. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic const string Pfi0

### Pfi0

The signal is exported to the PFI 1 connector on the PXI-5142 and PXIe-5622.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public const string Pfi0

Parent topic:

RFmxCdma2kMXConstants Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pfi1.html language=enus -->
## TOPIC 00109: Pfi1

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pfi1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pfi1.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 0. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic const string Pfi1

### Pfi1

The signal is exported to the PXI trigger line 0.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public const string Pfi1

Parent topic:

RFmxCdma2kMXConstants Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pulsein.html language=enus -->
## TOPIC 00110: PulseIn

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pulsein.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pulsein.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic const string PulseIn

### PulseIn

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public const string PulseIn

Parent topic:

RFmxCdma2kMXConstants Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxiedstarbline.html language=enus -->
## TOPIC 00111: PxieDStarBLine

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxiedstarbline.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxiedstarbline.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The trigger is received on the PXIe DStar B trigger line. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic const string PxieDStarBLine

### PxieDStarBLine

The trigger is received on the PXIe DStar B trigger line.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public const string PxieDStarBLine

Parent topic:

RFmxCdma2kMXConstants Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxistarline.html language=enus -->
## TOPIC 00112: PxiStarLine

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxistarline.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxistarline.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI star trigger line. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic const string PxiStarLine

### PxiStarLine

The signal is exported to the PXI star trigger line.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public const string PxiStarLine

Parent topic:

RFmxCdma2kMXConstants Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxitriggerline0.html language=enus -->
## TOPIC 00113: PxiTriggerLine0

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxitriggerline0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxitriggerline0.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 0. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic const string PxiTriggerLine0

### PxiTriggerLine0

The signal is exported to the PXI trigger line 0.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public const string PxiTriggerLine0

Parent topic:

RFmxCdma2kMXConstants Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxitriggerline1.html language=enus -->
## TOPIC 00114: PxiTriggerLine1

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxitriggerline1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxitriggerline1.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 1. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic const string PxiTriggerLine1

### PxiTriggerLine1

The signal is exported to the PXI trigger line 1.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public const string PxiTriggerLine1

Parent topic:

RFmxCdma2kMXConstants Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxitriggerline2.html language=enus -->
## TOPIC 00115: PxiTriggerLine2

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxitriggerline2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxitriggerline2.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 2. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic const string PxiTriggerLine2

### PxiTriggerLine2

The signal is exported to the PXI trigger line 2.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public const string PxiTriggerLine2

Parent topic:

RFmxCdma2kMXConstants Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxitriggerline3.html language=enus -->
## TOPIC 00116: PxiTriggerLine3

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxitriggerline3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxitriggerline3.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 3. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic const string PxiTriggerLine3

### PxiTriggerLine3

The signal is exported to the PXI trigger line 3.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public const string PxiTriggerLine3

Parent topic:

RFmxCdma2kMXConstants Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxitriggerline4.html language=enus -->
## TOPIC 00117: PxiTriggerLine4

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxitriggerline4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxitriggerline4.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 4. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic const string PxiTriggerLine4

### PxiTriggerLine4

The signal is exported to the PXI trigger line 4.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public const string PxiTriggerLine4

Parent topic:

RFmxCdma2kMXConstants Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxitriggerline5.html language=enus -->
## TOPIC 00118: PxiTriggerLine5

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxitriggerline5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxitriggerline5.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 5. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic const string PxiTriggerLine5

### PxiTriggerLine5

The signal is exported to the PXI trigger line 5.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public const string PxiTriggerLine5

Parent topic:

RFmxCdma2kMXConstants Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxitriggerline6.html language=enus -->
## TOPIC 00119: PxiTriggerLine6

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxitriggerline6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxitriggerline6.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 6. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic const string PxiTriggerLine6

### PxiTriggerLine6

The signal is exported to the PXI trigger line 6.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public const string PxiTriggerLine6

Parent topic:

RFmxCdma2kMXConstants Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxitriggerline7.html language=enus -->
## TOPIC 00120: PxiTriggerLine7

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxitriggerline7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-pxitriggerline7.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 7. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic const string PxiTriggerLine7

### PxiTriggerLine7

The signal is exported to the PXI trigger line 7.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public const string PxiTriggerLine7

Parent topic:

RFmxCdma2kMXConstants Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-timerevent.html language=enus -->
## TOPIC 00121: TimerEvent

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-timerevent.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants-timerevent.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The trigger is received from the timer event. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic const string TimerEvent

### TimerEvent

The trigger is received from the timer event.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public const string TimerEvent

Parent topic:

RFmxCdma2kMXConstants Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants.html language=enus -->
## TOPIC 00122: RFmxCdma2kMXConstants Class

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxconstants.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies constants for I/O terminals. Derives fromNoneSyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic class RFmxCdma2kMXConstantsFieldsNameDescriptionDioPfi0DioPfi1DioPfi2DioPfi3DioPfi4DioPfi5DioPfi6DioPfi7Pfi0The signal is exported to the PFI 1 connector on the PXI-5142 and PXIe-5622. Pfi

### RFmxCdma2kMXConstants Class

Specifies constants for I/O terminals.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public class RFmxCdma2kMXConstants

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
| PxieDStarBLine | The trigger is received on the PXIe DStar B trigger line. |
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

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxdigitaledgetriggeredge.html language=enus -->
## TOPIC 00123: RFmxCdma2kMXDigitalEdgeTriggerEdge Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxdigitaledgetriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxdigitaledgetriggeredge.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxCdma2kMXTriggerType) method to DigitalEdge. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXDigitalEdgeTriggerEdgeMembersNameValueDescriptionRising0The trigger as

### RFmxCdma2kMXDigitalEdgeTriggerEdge Enumeration

Specifies the active edge for the trigger. This method is used only when you set the [SetTriggerType(string, RFmxCdma2kMXTriggerType)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-settriggertype__string-rfmxcdma2kmxtriggertype.html) method to [DigitalEdge](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXDigitalEdgeTriggerEdge

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 0 | The trigger asserts on the rising edge of the signal. |
| Falling | 1 | The trigger asserts on the falling edge of the signal. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxiqpoweredgetriggerleveltype.html language=enus -->
## TOPIC 00124: RFmxCdma2kMXIQPowerEdgeTriggerLevelType Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxiqpoweredgetriggerleveltype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxiqpoweredgetriggerleveltype.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference for the IQ Power Edge Level Type method. This method is used only when you set the SetTriggerType(string, RFmxCdma2kMXTriggerType) method to IQPowerEdge. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXIQPowerEdgeTriggerLevelTypeMembersNameValueDescr

### RFmxCdma2kMXIQPowerEdgeTriggerLevelType Enumeration

Specifies the reference for the IQ Power Edge Level Type method. This method is used only when you set the [SetTriggerType(string, RFmxCdma2kMXTriggerType)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-settriggertype__string-rfmxcdma2kmxtriggertype.html) method to [IQPowerEdge](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXIQPowerEdgeTriggerLevelType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Relative | 0 | The IQ Power Edge Level method is relative to the value of the SetReferenceLevel(string, double) method. |
| Absolute | 1 | The IQ Power Edge Level method specifies the absolute power. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxiqpoweredgetriggerslope.html language=enus -->
## TOPIC 00125: RFmxCdma2kMXIQPowerEdgeTriggerSlope Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxiqpoweredgetriggerslope.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxiqpoweredgetriggerslope.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This method is used only when you set the SetTriggerType(string, RFmxCdma2kMXTriggerTyp

### RFmxCdma2kMXIQPowerEdgeTriggerSlope Enumeration

Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This method is used only when you set the [SetTriggerType(string, RFmxCdma2kMXTriggerType)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-settriggertype__string-rfmxcdma2kmxtriggertype.html) method to [IQPowerEdge](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXIQPowerEdgeTriggerSlope

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 0 | The trigger asserts when the signal power is rising. |
| Falling | 1 | The trigger asserts when the signal power is falling. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxlimitedconfigurationchange.html language=enus -->
## TOPIC 00126: RFmxCdma2kMXLimitedConfigurationChange Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxlimitedconfigurationchange.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxlimitedconfigurationchange.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the set of properties that are considered by RFmx in the locked signal configuration state. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXLimitedConfigurationChangeMembersNameValueDescriptionDisabled0This is the normal mode of RFmx operation. All configuration c

### RFmxCdma2kMXLimitedConfigurationChange Enumeration

Specifies the set of properties that are considered by RFmx in the locked signal configuration state.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXLimitedConfigurationChange

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Disabled | 0 | This is the normal mode of RFmx operation. All configuration changes in RFmxInstr properties or in personality properties will be applied during RFmx Commit. |
| NoChange | 1 | Signal configuration is locked after the first Commit of the named signal configuration. Any configuration change thereafter either in RFmxInstr properties or personality properties will not be considered by subsequent RFmx Commits or Initiates of this signal. Use No Change if you have created named signal configurations for all measurement configurations but are setting some RFmxInstr properties. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| Frequency | 2 | Signal configuration, other than center frequency and external attenuation, is locked after first Commit of the named signal configuration. Thereafter, only the Center Frequency and SetExternalAttenuation(string, double) method value changes will be considered by subsequent driver Commits or Initiates of this signal. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| ReferenceLevel | 3 | Signal configuration, other than the reference level, is locked after first Commit of the named signal configuration. Thereafter only the SetReferenceLevel(string, double) method value change will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends that you set the SetIQPowerEdgeTriggerLevelType(string, RFmxCdma2kMXIQPowerEdgeTriggerLevelType) to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| FrequencyAndReferenceLevel | 4 | Signal configuration, other than center frequency, reference level, and external attenuation, is locked after first Commit of the named signal configuration. Thereafter only Center Frequency, Reference Level, and External Attenuation method value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set SetIQPowerEdgeTriggerLevelType(string, RFmxCdma2kMXIQPowerEdgeTriggerLevelType) to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| SelectedPortsFrequencyAndReferenceLevel | 5 | Signal configuration, other than selected ports, center frequency, reference level, external attenuation, and RFInstr configuration is locked after first Commit of the named signal configuration. Thereafter only SetSelectedPorts(string, string), Center Frequency, SetReferenceLevel(string, double), and SetExternalAttenuation(string, double) method value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the SetIQPowerEdgeTriggerLevelType(string, RFmxCdma2kMXIQPowerEdgeTriggerLevelType) to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxlinkdirection.html language=enus -->
## TOPIC 00127: RFmxCdma2kMXLinkDirection Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxlinkdirection.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxlinkdirection.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the direction for which the frequency is calculated. Only Uplink is supported. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXLinkDirectionMembersNameValueDescriptionDownlink0CDMA2k measurement uses 3GPP CDMA2k forward link direction also known as downlink direct

### RFmxCdma2kMXLinkDirection Enumeration

Specifies the direction for which the frequency is calculated. Only Uplink is supported.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXLinkDirection

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Downlink | 0 | CDMA2k measurement uses 3GPP CDMA2k forward link direction also known as downlink direction to measure the received signal. |
| Uplink | 1 | CDMA2k measurement uses 3GPP CDMA2k reverse link direction also known as uplink direction to measure the received signal. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmeasurementtypes.html language=enus -->
## TOPIC 00128: RFmxCdma2kMXMeasurementTypes Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmeasurementtypes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmeasurementtypes.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXMeasurementTypesMembersNameValueDescriptionModAcc0x1Selects ModAcc measurement. Acp0x2Selects ACP measurement. Chp0x4Selects CHP measurement. Obw0x8Selects OBW measurement. Sem0x10Selects SEM

### RFmxCdma2kMXMeasurementTypes Enumeration

Specifies the type of measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXMeasurementTypes

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ModAcc | 0x1 | Selects ModAcc measurement. |
| Acp | 0x2 | Selects ACP measurement. |
| Chp | 0x4 | Selects CHP measurement. |
| Obw | 0x8 | Selects OBW measurement. |
| Sem | 0x10 | Selects SEM measurement. |
| Qevm | 0x20 | Selects QEVM measurement. |
| Cda | 0x40 | Selects CDA measurement. |
| SlotPhase | 0x80 | Selects SlotPhase measurement. |
| SlotPower | 0x100 | Selects SlotPower measurement. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodacc-configuration.html language=enus -->
## TOPIC 00129: Configuration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodacc-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodacc-configuration.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxCdma2kMXModAccConfiguration instance that provides methods to configure the ModAcc measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic RFmxCdma2kMXModAccConfiguration Configuration { get; }

### Configuration

Gets the [RFmxCdma2kMXModAccConfiguration](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccconfiguration.html) instance that provides methods to configure the ModAcc measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public [RFmxCdma2kMXModAccConfiguration](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccconfiguration.html) Configuration { get; }

Parent topic:

RFmxCdma2kMXModAcc Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodacc-results.html language=enus -->
## TOPIC 00130: Results

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodacc-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodacc-results.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxCdma2kMXModAccResults instance that provides methods to fetch and read the ModAcc measurement results. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic RFmxCdma2kMXModAccResults Results { get; }

### Results

Gets the [RFmxCdma2kMXModAccResults](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults.html) instance that provides methods to fetch and read the ModAcc measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public [RFmxCdma2kMXModAccResults](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults.html) Results { get; }

Parent topic:

RFmxCdma2kMXModAcc Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodacc.html language=enus -->
## TOPIC 00131: RFmxCdma2kMXModAcc Class

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodacc.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the ModAcc measurement. Derives fromRFmxCdma2kMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic class RFmxCdma2kMXModAcc : RFmxCdma2kMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxCdma2kMXModAccConfiguration instance that provides methods to configure the

### RFmxCdma2kMXModAcc Class

Represents the ModAcc measurement.

#### Derives from

- RFmxCdma2kMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public class RFmxCdma2kMXModAcc : RFmxCdma2kMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxCdma2kMXModAccConfiguration instance that provides methods to configure the ModAcc measurement. |
| Results | Gets the RFmxCdma2kMXModAccResults instance that provides methods to fetch and read the ModAcc measurement results. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccconfiguration-configuresynchronizationmodeandinterval__string-rfmxcdma2kmxmodaccsynchronizationmode-int-int.html language=enus -->
## TOPIC 00132: ConfigureSynchronizationModeAndInterval(string, RFmxCdma2kMXModAccSynchronizationMode, int, int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccconfiguration-configuresynchronizationmodeandinterval__string-rfmxcdma2kmxmodaccsynchronizationmode-int-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccconfiguration-configuresynchronizationmodeandinterval__string-rfmxcdma2kmxmodaccsynchronizationmode-int-int.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the synchronization mode, offset, and length for modulation accuracy (ModAcc) analysis.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int ConfigureSynchronizationModeAndInterval(string selectorString, RFmxCdma2kMXModAccSynchronizationMode synchronizationMode, int measurementOffs

### ConfigureSynchronizationModeAndInterval(string, RFmxCdma2kMXModAccSynchronizationMode, int, int)

Configures the synchronization mode, offset, and length for modulation accuracy (ModAcc) analysis.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int ConfigureSynchronizationModeAndInterval(string selectorString, RFmxCdma2kMXModAccSynchronizationMode synchronizationMode, int measurementOffset, int measurementLength)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| synchronizationMode | RFmxCdma2kMXModAccSynchronizationMode | Specifies whether the measurement is performed from the frame, slot, or symbol boundary. |
| measurementOffset | int | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. |
| measurementLength | int | Specifies the duration of the modulation accuracy measurement. This value is expressed in slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccconfiguration-getiqgainimbalanceremovalenabled__string-out.html language=enus -->
## TOPIC 00133: GetIQGainImbalanceRemovalEnabled(string, out RFmxCdma2kMXModAccIQGainImbalanceRemovalEnabled)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccconfiguration-getiqgainimbalanceremovalenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccconfiguration-getiqgainimbalanceremovalenabled__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to remove the I/Q gain imbalance before an EVM measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetIQGainImbalanceRemovalEnabled(string selectorString, out RFmxCdma2kMXModAccIQGainImbalanceRemovalEnabled value)RemarksThis method gets the value of ModAccIQGainImb

### GetIQGainImbalanceRemovalEnabled(string, out RFmxCdma2kMXModAccIQGainImbalanceRemovalEnabled)

Gets whether to remove the I/Q gain imbalance before an EVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetIQGainImbalanceRemovalEnabled(string selectorString, out RFmxCdma2kMXModAccIQGainImbalanceRemovalEnabled value)

#### Remarks

This method gets the value of [ModAccIQGainImbalanceRemovalEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodacciqgainimbalanceremovalenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxCdma2kMXModAccIQGainImbalanceRemovalEnabled | Upon return, contains whether to remove the I/Q gain imbalance before an EVM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodacciqgainimbalanceremovalenabled.html language=enus -->
## TOPIC 00134: RFmxCdma2kMXModAccIQGainImbalanceRemovalEnabled Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodacciqgainimbalanceremovalenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodacciqgainimbalanceremovalenabled.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove the I/Q gain imbalance before an EVM measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXModAccIQGainImbalanceRemovalEnabledMembersNameValueDescriptionFalse0I/Q gain imbalance is not removed before the EVM measurement. True1I/Q gain imba

### RFmxCdma2kMXModAccIQGainImbalanceRemovalEnabled Enumeration

Specifies whether to remove the I/Q gain imbalance before an EVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXModAccIQGainImbalanceRemovalEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | I/Q gain imbalance is not removed before the EVM measurement. |
| True | 1 | I/Q gain imbalance is removed before the EVM measurement. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodacciqoffsetremovalenabled.html language=enus -->
## TOPIC 00135: RFmxCdma2kMXModAccIQOffsetRemovalEnabled Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodacciqoffsetremovalenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodacciqoffsetremovalenabled.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove the I/Q offset before an EVM measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXModAccIQOffsetRemovalEnabledMembersNameValueDescriptionFalse0I/Q offset is not removed before the EVM measurement. True1I/Q offset is removed before the EVM

### RFmxCdma2kMXModAccIQOffsetRemovalEnabled Enumeration

Specifies whether to remove the I/Q offset before an EVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXModAccIQOffsetRemovalEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | I/Q offset is not removed before the EVM measurement. |
| True | 1 | I/Q offset is removed before the EVM measurement. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodacciqquadratureerrorremovalenabled.html language=enus -->
## TOPIC 00136: RFmxCdma2kMXModAccIQQuadratureErrorRemovalEnabled Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodacciqquadratureerrorremovalenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodacciqquadratureerrorremovalenabled.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove the I/Q quadrature error before an EVM measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXModAccIQQuadratureErrorRemovalEnabledMembersNameValueDescriptionFalse0I/Q quadrature error is not removed before the EVM measurement. True1I/Q qua

### RFmxCdma2kMXModAccIQQuadratureErrorRemovalEnabled Enumeration

Specifies whether to remove the I/Q quadrature error before an EVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXModAccIQQuadratureErrorRemovalEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | I/Q quadrature error is not removed before the EVM measurement. |
| True | 1 | I/Q quadrature error is removed before the EVM measurement. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccpeakcdebranch.html language=enus -->
## TOPIC 00137: RFmxCdma2kMXModAccPeakCdeBranch Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccpeakcdebranch.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccpeakcdebranch.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the branch corresponding to the value that the GetPeakCde(string, out double) method returns. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXModAccPeakCdeBranchMembersNameValueDescriptionI0The signal is modulated on the in-phase branch. Q1The signal is modulated on

### RFmxCdma2kMXModAccPeakCdeBranch Enumeration

Returns the branch corresponding to the value that the [GetPeakCde(string, out double)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getpeakcde__string-out.html) method returns.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXModAccPeakCdeBranch

#### Members

| Name | Value | Description |
| --- | --- | --- |
| I | 0 | The signal is modulated on the in-phase branch. |
| Q | 1 | The signal is modulated on the quadrature branch. |
| IAndQ | 2 | Complex modulated signal. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccreceivefilterenabled.html language=enus -->
## TOPIC 00138: RFmxCdma2kMXModAccReceiveFilterEnabled Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccreceivefilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccreceivefilterenabled.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the received filter for the ModAcc measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXModAccReceiveFilterEnabledMembersNameValueDescriptionFalse0Disables received filtering for the ModAcc measurement. True1Enables received filtering for

### RFmxCdma2kMXModAccReceiveFilterEnabled Enumeration

Specifies whether to enable the received filter for the ModAcc measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXModAccReceiveFilterEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables received filtering for the ModAcc measurement. |
| True | 1 | Enables received filtering for the ModAcc measurement. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-fetchdetectedchannelarray__string-double-ref-ref-ref.html language=enus -->
## TOPIC 00139: FetchDetectedChannelArray(string, double, ref int[], ref int[], ref RFmxCdma2kMXModAccDetectedBranch[])

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-fetchdetectedchannelarray__string-double-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-fetchdetectedchannelarray__string-double-ref-ref-ref.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the detected channels. If you set the SetChannelConfigurationMode(string, RFmxCdma2kMXChannelConfigurationMode) method to UserDefined, the measurement returns the configured channels.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int FetchDetectedChannelArray(string selectorString,

### FetchDetectedChannelArray(string, double, ref int[], ref int[], ref RFmxCdma2kMXModAccDetectedBranch[])

Returns the detected channels. If you set the [SetChannelConfigurationMode(string, RFmxCdma2kMXChannelConfigurationMode)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setchannelconfigurationmode__string-rfmxcdma2kmxchannelconfigurationmode.html) method to [UserDefined](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchannelconfigurationmode.html), the measurement returns the configured channels.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int FetchDetectedChannelArray(string selectorString, double timeout, ref int[] detectedWalshCodeLength, ref int[] detectedWalshCodeNumber, ref RFmxCdma2kMXModAccDetectedBranch[] detectedBranch)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| detectedWalshCodeLength | ref int[] | Upon return, contains the array of the detected Walsh code length. |
| detectedWalshCodeNumber | ref int[] | Upon return, contains the array of the detected Walsh code number. |
| detectedBranch | ref RFmxCdma2kMXModAccDetectedBranch[] | Upon return, contains the array of the detected branch. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXModAccResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-fetchevm__string-double-out-out-out-out-out-out-out.html language=enus -->
## TOPIC 00140: FetchEvm(string, double, out double, out double, out double, out double, out double, out double, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-fetchevm__string-double-out-out-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-fetchevm__string-double-out-out-out-out-out-out-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the EVM value and related measurement values of the modulation accuracy (ModAcc) of the CDMA2k signal.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int FetchEvm(string selectorString, double timeout, out double rmsEvm, out double peakEvm, out double rho, out double frequencyError,

### FetchEvm(string, double, out double, out double, out double, out double, out double, out double, out double)

Returns the EVM value and related measurement values of the modulation accuracy (ModAcc) of the CDMA2k signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int FetchEvm(string selectorString, double timeout, out double rmsEvm, out double peakEvm, out double rho, out double frequencyError, out double chipRateError, out double rmsMagnitudeError, out double rmsPhaseError)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| rmsEvm | out double | Upon return, contains the RMS EVM of the composite signal. This value is expressed as a percentage. |
| peakEvm | out double | Upon return, contains the peak value of the uplink EVM. This value is expressed as a percentage. |
| rho | out double | Upon return, contains the correlation of the received signal with the reference signal normalized by the signal power. |
| frequencyError | out double | Upon return, contains the frequency error. This value is expressed in Hz. |
| chipRateError | out double | Upon return, contains the chip rate error. This value is expressed in parts per million (ppm). |
| rmsMagnitudeError | out double | Upon return, contains the RMS magnitude error of the composite signal. This value is expressed as a percentage. |
| rmsPhaseError | out double | Upon return, contains the RMS phase error of the composite signal. This value is expressed in degrees (deg). |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXModAccResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-fetchphaseerrortrace__string-double-ref.html language=enus -->
## TOPIC 00141: FetchPhaseErrorTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-fetchphaseerrortrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-fetchphaseerrortrace__string-double-ref.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the phase error trace of the ModAcc measurement.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int FetchPhaseErrorTrace(string selectorString, double timeout, ref AnalogWaveform< float > phaseError)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string compris

### FetchPhaseErrorTrace(string, double, ref AnalogWaveform< float >)

Returns the phase error trace of the ModAcc measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int FetchPhaseErrorTrace(string selectorString, double timeout, ref AnalogWaveform< float > phaseError)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| phaseError | ref AnalogWaveform< float > | Upon return, contains the trace of phase errors of the corrected composite signal. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXModAccResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getdetectedwalshcodelength__string-out.html language=enus -->
## TOPIC 00142: GetDetectedWalshCodeLength(string, out int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getdetectedwalshcodelength__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getdetectedwalshcodelength__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Walsh code length of the detected channel. If you set the SetChannelConfigurationMode(string, RFmxCdma2kMXChannelConfigurationMode) method to UserDefined, the method returns the Walsh code length of the configured channel.Use "channel(n)" as the Selector Strings to read this method. SyntaxN

### GetDetectedWalshCodeLength(string, out int)

Gets the Walsh code length of the detected channel. If you set the [SetChannelConfigurationMode(string, RFmxCdma2kMXChannelConfigurationMode)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setchannelconfigurationmode__string-rfmxcdma2kmxchannelconfigurationmode.html) method to [UserDefined](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchannelconfigurationmode.html), the method returns the Walsh code length of the configured channel.Use "channel(n)" as the Selector Strings to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetDetectedWalshCodeLength(string selectorString, out int value)

#### Remarks

This method gets the value of [ModAccResultsDetectedWalshCodeLength](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Channel number. Example: "Channel0", "result::r1/Channel0". You can use the BuildChannelString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the Walsh code length of the detected channel. If you set the SetChannelConfigurationMode(string, RFmxCdma2kMXChannelConfigurationMode) method to UserDefined, the method returns the Walsh code length of the configured channel.Use "channel(n)" as the Selector Strings to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXModAccResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getdetectedwalshcodenumber__string-out.html language=enus -->
## TOPIC 00143: GetDetectedWalshCodeNumber(string, out int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getdetectedwalshcodenumber__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getdetectedwalshcodenumber__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Walsh code number of the detected channel. If you set the SetChannelConfigurationMode(string, RFmxCdma2kMXChannelConfigurationMode) method to UserDefined, the method returns the Walsh code number of the configured channel.Use "channel(n)" as the Selector Strings to read this method. SyntaxN

### GetDetectedWalshCodeNumber(string, out int)

Gets the Walsh code number of the detected channel. If you set the [SetChannelConfigurationMode(string, RFmxCdma2kMXChannelConfigurationMode)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setchannelconfigurationmode__string-rfmxcdma2kmxchannelconfigurationmode.html) method to [UserDefined](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchannelconfigurationmode.html), the method returns the Walsh code number of the configured channel.Use "channel(n)" as the Selector Strings to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetDetectedWalshCodeNumber(string selectorString, out int value)

#### Remarks

This method gets the value of [ModAccResultsDetectedWalshCodeNumber](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Channel number. Example: "Channel0", "result::r1/Channel0". You can use the BuildChannelString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the Walsh code number of the detected channel. If you set the SetChannelConfigurationMode(string, RFmxCdma2kMXChannelConfigurationMode) method to UserDefined, the method returns the Walsh code number of the configured channel.Use "channel(n)" as the Selector Strings to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXModAccResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getfrequencyerror__string-out.html language=enus -->
## TOPIC 00144: GetFrequencyError(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getfrequencyerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getfrequencyerror__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency error averaged over all measured slots. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetFrequencyError(string selectorString, out double value)RemarksThis method gets the value of ModAccResultsFrequencyError attribute.ParametersNameTy

### GetFrequencyError(string, out double)

Gets the frequency error averaged over all measured slots. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetFrequencyError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsFrequencyError](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the frequency error averaged over all measured slots. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXModAccResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getiqoriginoffset__string-out.html language=enus -->
## TOPIC 00145: GetIQOriginOffset(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getiqoriginoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getiqoriginoffset__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the I/Q origin offset of the composite signal averaged over all measured slots. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetIQOriginOffset(string selectorString, out double value)RemarksThis method gets the value of ModAccResultsIQOriginOffset

### GetIQOriginOffset(string, out double)

Gets the I/Q origin offset of the composite signal averaged over all measured slots. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetIQOriginOffset(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsIQOriginOffset](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the I/Q origin offset of the composite signal averaged over all measured slots. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXModAccResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getiqquadratureerror__string-out.html language=enus -->
## TOPIC 00146: GetIQQuadratureError(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getiqquadratureerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getiqquadratureerror__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the I/Q quadrature error of the composite signal, averaged over all measured slots. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetIQQuadratureError(string selectorString, out double value)RemarksThis method gets the value of ModAccResultsIQQ

### GetIQQuadratureError(string, out double)

Gets the I/Q quadrature error of the composite signal, averaged over all measured slots. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetIQQuadratureError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsIQQuadratureError](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the I/Q quadrature error of the composite signal, averaged over all measured slots. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXModAccResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getnumberofdetectedchannels__string-out.html language=enus -->
## TOPIC 00147: GetNumberOfDetectedChannels(string, out int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getnumberofdetectedchannels__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getnumberofdetectedchannels__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the total number of detected channels. If you set the SetChannelConfigurationMode(string, RFmxCdma2kMXChannelConfigurationMode) method to UserDefined, the method returns the number of configured channels. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetNumberOfDetectedChannels(s

### GetNumberOfDetectedChannels(string, out int)

Gets the total number of detected channels. If you set the [SetChannelConfigurationMode(string, RFmxCdma2kMXChannelConfigurationMode)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmx-setchannelconfigurationmode__string-rfmxcdma2kmxchannelconfigurationmode.html) method to [UserDefined](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxchannelconfigurationmode.html), the method returns the number of configured channels.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetNumberOfDetectedChannels(string selectorString, out int value)

#### Remarks

This method gets the value of [ModAccResultsNumberOfDetectedChannels](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out int | Upon return, contains the total number of detected channels. If you set the SetChannelConfigurationMode(string, RFmxCdma2kMXChannelConfigurationMode) method to UserDefined, the method returns the number of configured channels. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXModAccResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getpeakactivecdebranch__string-out.html language=enus -->
## TOPIC 00148: GetPeakActiveCdeBranch(string, out RFmxCdma2kMXModAccPeakActiveCdeBranch)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getpeakactivecdebranch__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getpeakactivecdebranch__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the branch of the channel corresponding to the value that the GetPeakActiveCde(string, out double) method returns. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetPeakActiveCdeBranch(string selectorString, out RFmxCdma2kMXModAccPeakActiveCdeBranch value)RemarksThis method gets t

### GetPeakActiveCdeBranch(string, out RFmxCdma2kMXModAccPeakActiveCdeBranch)

Gets the branch of the channel corresponding to the value that the [GetPeakActiveCde(string, out double)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getpeakactivecde__string-out.html) method returns.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetPeakActiveCdeBranch(string selectorString, out RFmxCdma2kMXModAccPeakActiveCdeBranch value)

#### Remarks

This method gets the value of [ModAccResultsPeakActiveCdeBranch](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out RFmxCdma2kMXModAccPeakActiveCdeBranch | Upon return, contains the branch of the channel corresponding to the value that the GetPeakActiveCde(string, out double) method returns. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXModAccResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getpeakactivecdewalshcodelength__string-out.html language=enus -->
## TOPIC 00149: GetPeakActiveCdeWalshCodeLength(string, out int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getpeakactivecdewalshcodelength__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getpeakactivecdewalshcodelength__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Walsh code length of the channel corresponding to the value that the GetPeakActiveCde(string, out double) method returns. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetPeakActiveCdeWalshCodeLength(string selectorString, out int value)RemarksThis method gets the value of Mo

### GetPeakActiveCdeWalshCodeLength(string, out int)

Gets the Walsh code length of the channel corresponding to the value that the [GetPeakActiveCde(string, out double)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getpeakactivecde__string-out.html) method returns.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetPeakActiveCdeWalshCodeLength(string selectorString, out int value)

#### Remarks

This method gets the value of [ModAccResultsPeakActiveCdeWalshCodeLength](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out int | Upon return, contains the Walsh code length of the channel corresponding to the value that the GetPeakActiveCde(string, out double) method returns. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXModAccResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getpeakcde__string-out.html language=enus -->
## TOPIC 00150: GetPeakCde(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getpeakcde__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxmodaccresults-getpeakcde__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum value among the code domain errors (CDEs). This value is expressed in dB. The CDEs are computed by projecting the descrambled error vector onto the code domain at a specific spreading factor. The CDE for every code with a specific spreading factor is defined as the ratio of the mean

### GetPeakCde(string, out double)

Gets the maximum value among the code domain errors (CDEs). This value is expressed in dB. The CDEs are computed by projecting the descrambled error vector onto the code domain at a specific spreading factor. The CDE for every code with a specific spreading factor is defined as the ratio of the mean power of the projection onto that code to the mean power of the composite reference waveform. A fixed spreading factor of 16 is used. The CDEs are computed separately for I and Q branches.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetPeakCde(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsPeakCde](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum value among the code domain errors (CDEs). This value is expressed in dB. The CDEs are computed by projecting the descrambled error vector onto the code domain at a specific spreading factor. The CDE for every code with a specific spreading factor is defined as the ratio of the mean power of the projection onto that code to the mean power of the composite reference waveform. A fixed spreading factor of 16 is used. The CDEs are computed separately for I and Q branches. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXModAccResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxobwaveragingtype.html language=enus -->
## TOPIC 00151: RFmxCdma2kMXObwAveragingType Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxobwaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxobwaveragingtype.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXObwAveragingTypeMembersNameValueDescriptionRms0The power spectrum is linearly averaged. RMS aver

### RFmxCdma2kMXObwAveragingType Enumeration

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXObwAveragingType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rms | 0 | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log | 1 | The power spectrum is averaged in a logarithmic scale. |
| Scalar | 2 | The square root of the power spectrum is averaged. |
| Maximum | 3 | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Minimum | 4 | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxobwconfiguration-configureaveraging__string-rfmxcdma2kmxobwaveragingenabled-int-rfmxcdma2kmxobwaveragingtype.html language=enus -->
## TOPIC 00152: ConfigureAveraging(string, RFmxCdma2kMXObwAveragingEnabled, int, RFmxCdma2kMXObwAveragingType)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxobwconfiguration-configureaveraging__string-rfmxcdma2kmxobwaveragingenabled-int-rfmxcdma2kmxobwaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxobwconfiguration-configureaveraging__string-rfmxcdma2kmxobwaveragingenabled-int-rfmxcdma2kmxobwaveragingtype.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the OBW measurement.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int ConfigureAveraging(string selectorString, RFmxCdma2kMXObwAveragingEnabled averagingEnabled, int averagingCount, RFmxCdma2kMXObwAveragingType averagingType)ParametersNameTypeDescriptionselectorSt

### ConfigureAveraging(string, RFmxCdma2kMXObwAveragingEnabled, int, RFmxCdma2kMXObwAveragingType)

Configures averaging for the OBW measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int ConfigureAveraging(string selectorString, RFmxCdma2kMXObwAveragingEnabled averagingEnabled, int averagingCount, RFmxCdma2kMXObwAveragingType averagingType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| averagingEnabled | RFmxCdma2kMXObwAveragingEnabled | Specifies whether to enable averaging for the measurement. |
| averagingCount | int | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True. |
| averagingType | RFmxCdma2kMXObwAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. RFmx uses the averaged spectrum for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxobwconfiguration-configuresweeptime__string-rfmxcdma2kmxobwsweeptimeauto-double.html language=enus -->
## TOPIC 00153: ConfigureSweepTime(string, RFmxCdma2kMXObwSweepTimeAuto, double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxobwconfiguration-configuresweeptime__string-rfmxcdma2kmxobwsweeptimeauto-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxobwconfiguration-configuresweeptime__string-rfmxcdma2kmxobwsweeptimeauto-double.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int ConfigureSweepTime(string selectorString, RFmxCdma2kMXObwSweepTimeAuto sweepTimeAuto, double sweepTimeInterval)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed

### ConfigureSweepTime(string, RFmxCdma2kMXObwSweepTimeAuto, double)

Configures the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int ConfigureSweepTime(string selectorString, RFmxCdma2kMXObwSweepTimeAuto sweepTimeAuto, double sweepTimeInterval)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| sweepTimeAuto | RFmxCdma2kMXObwSweepTimeAuto | Specifies whether the measurement computes the sweep time. |
| sweepTimeInterval | double | Specifies the sweep time when you set the sweepTimeAuto parameter to False. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxobwconfiguration-setsweeptimeinterval__string-double.html language=enus -->
## TOPIC 00154: SetSweepTimeInterval(string, double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxobwconfiguration-setsweeptimeinterval__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxobwconfiguration-setsweeptimeinterval__string-double.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the sweep time when you set the SetSweepTimeAuto(string, RFmxCdma2kMXObwSweepTimeAuto) method to False. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetSweepTimeInterval(string selectorString, double value)RemarksThis method sets the value of

### SetSweepTimeInterval(string, double)

Sets the sweep time when you set the [SetSweepTimeAuto(string, RFmxCdma2kMXObwSweepTimeAuto)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxobwconfiguration-setsweeptimeauto__string-rfmxcdma2kmxobwsweeptimeauto.html) method to [False](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxobwsweeptimeauto.html). This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetSweepTimeInterval(string selectorString, double value)

#### Remarks

This method sets the value of [ObwSweepTimeInterval](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 0.001667 seconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the sweep time when you set the SetSweepTimeAuto(string, RFmxCdma2kMXObwSweepTimeAuto) method to False. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxobwresults-getoccupiedbandwidth__string-out.html language=enus -->
## TOPIC 00155: GetOccupiedBandwidth(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxobwresults-getoccupiedbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxobwresults-getoccupiedbandwidth__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the bandwidth that occupies 99% of the total signal power. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetOccupiedBandwidth(string selectorString, out double value)RemarksThis method gets the value of ObwResultsOccupiedBandwidth attribute.Paramete

### GetOccupiedBandwidth(string, out double)

Gets the bandwidth that occupies 99% of the total signal power. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetOccupiedBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [ObwResultsOccupiedBandwidth](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the bandwidth that occupies 99% of the total signal power. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXObwResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxobwresults-getstartfrequency__string-out.html language=enus -->
## TOPIC 00156: GetStartFrequency(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxobwresults-getstartfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxobwresults-getstartfrequency__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the start frequency of the OBW. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetStartFrequency(string selectorString, out double value)RemarksThis method gets the value of ObwResultsStartFrequency attribute.ParametersNameTypeDescriptionselectorStri

### GetStartFrequency(string, out double)

Gets the start frequency of the OBW. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetStartFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [ObwResultsStartFrequency](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the start frequency of the OBW. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXObwResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxobwresults-getstopfrequency__string-out.html language=enus -->
## TOPIC 00157: GetStopFrequency(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxobwresults-getstopfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxobwresults-getstopfrequency__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the stop frequency of the OBW. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetStopFrequency(string selectorString, out double value)RemarksThis method gets the value of ObwResultsStopFrequency attribute.ParametersNameTypeDescriptionselectorStrings

### GetStopFrequency(string, out double)

Gets the stop frequency of the OBW. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetStopFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [ObwResultsStopFrequency](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the stop frequency of the OBW. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXObwResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevm-results.html language=enus -->
## TOPIC 00158: Results

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevm-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevm-results.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxCdma2kMXQevmResults instance that provides methods to fetch and read the QEVM measurement results. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic RFmxCdma2kMXQevmResults Results { get; }

### Results

Gets the [RFmxCdma2kMXQevmResults](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults.html) instance that provides methods to fetch and read the QEVM measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public [RFmxCdma2kMXQevmResults](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults.html) Results { get; }

Parent topic:

RFmxCdma2kMXQevm Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevm.html language=enus -->
## TOPIC 00159: RFmxCdma2kMXQevm Class

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevm.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevm.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the QEVM measurement. Derives fromRFmxCdma2kMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic class RFmxCdma2kMXQevm : RFmxCdma2kMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxCdma2kMXQevmConfiguration instance that provides methods to configure the QEVM m

### RFmxCdma2kMXQevm Class

Represents the QEVM measurement.

#### Derives from

- RFmxCdma2kMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public class RFmxCdma2kMXQevm : RFmxCdma2kMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxCdma2kMXQevmConfiguration instance that provides methods to configure the QEVM measurement. |
| Results | Gets the RFmxCdma2kMXQevmResults instance that provides methods to fetch and read the QEVM measurement results. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00160: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the traces to be stored and retrieved after performing the QEVM measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method gets the value of QevmAllTracesEnabled attribute.The default v

### GetAllTracesEnabled(string, out bool)

Gets whether to enable the traces to be stored and retrieved after performing the QEVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [QevmAllTracesEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the traces to be stored and retrieved after performing the QEVM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXQevmConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmconfiguration-getiqoffsetremovalenabled__string-out.html language=enus -->
## TOPIC 00161: GetIQOffsetRemovalEnabled(string, out RFmxCdma2kMXQevmIQOffsetRemovalEnabled)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmconfiguration-getiqoffsetremovalenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmconfiguration-getiqoffsetremovalenabled__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to remove I/Q offset before QEVM measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetIQOffsetRemovalEnabled(string selectorString, out RFmxCdma2kMXQevmIQOffsetRemovalEnabled value)RemarksThis method gets the value of QevmIQOffsetRemovalEnabled attribute.The defa

### GetIQOffsetRemovalEnabled(string, out RFmxCdma2kMXQevmIQOffsetRemovalEnabled)

Gets whether to remove I/Q offset before QEVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetIQOffsetRemovalEnabled(string selectorString, out RFmxCdma2kMXQevmIQOffsetRemovalEnabled value)

#### Remarks

This method gets the value of [QevmIQOffsetRemovalEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmiqoffsetremovalenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxCdma2kMXQevmIQOffsetRemovalEnabled | Upon return, contains whether to remove I/Q offset before QEVM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXQevmConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmconfiguration-getiqquadratureerrorremovalenabled__string-out.html language=enus -->
## TOPIC 00162: GetIQQuadratureErrorRemovalEnabled(string, out RFmxCdma2kMXQevmIQQuadratureErrorRemovalEnabled)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmconfiguration-getiqquadratureerrorremovalenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmconfiguration-getiqquadratureerrorremovalenabled__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to remove I/Q quadrature error before QEVM measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetIQQuadratureErrorRemovalEnabled(string selectorString, out RFmxCdma2kMXQevmIQQuadratureErrorRemovalEnabled value)RemarksThis method gets the value of QevmIQQuadratureE

### GetIQQuadratureErrorRemovalEnabled(string, out RFmxCdma2kMXQevmIQQuadratureErrorRemovalEnabled)

Gets whether to remove I/Q quadrature error before QEVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetIQQuadratureErrorRemovalEnabled(string selectorString, out RFmxCdma2kMXQevmIQQuadratureErrorRemovalEnabled value)

#### Remarks

This method gets the value of [QevmIQQuadratureErrorRemovalEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmiqquadratureerrorremovalenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxCdma2kMXQevmIQQuadratureErrorRemovalEnabled | Upon return, contains whether to remove I/Q quadrature error before QEVM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXQevmConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmconfiguration-getreceivefilterenabled__string-out.html language=enus -->
## TOPIC 00163: GetReceiveFilterEnabled(string, out RFmxCdma2kMXQevmReceiveFilterEnabled)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmconfiguration-getreceivefilterenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmconfiguration-getreceivefilterenabled__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the received filter for the QEVM measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetReceiveFilterEnabled(string selectorString, out RFmxCdma2kMXQevmReceiveFilterEnabled value)RemarksThis method gets the value of QevmReceiveFilterEnabled attribute.The

### GetReceiveFilterEnabled(string, out RFmxCdma2kMXQevmReceiveFilterEnabled)

Gets whether to enable the received filter for the QEVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetReceiveFilterEnabled(string selectorString, out RFmxCdma2kMXQevmReceiveFilterEnabled value)

#### Remarks

This method gets the value of [QevmReceiveFilterEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmreceivefilterenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxCdma2kMXQevmReceiveFilterEnabled | Upon return, contains whether to enable the received filter for the QEVM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXQevmConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmconfiguration-setalltracesenabled__string-bool.html language=enus -->
## TOPIC 00164: SetAllTracesEnabled(string, bool)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmconfiguration-setalltracesenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmconfiguration-setalltracesenabled__string-bool.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the traces to be stored and retrieved after performing the QEVM measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetAllTracesEnabled(string selectorString, bool value)RemarksThis method sets the value of QevmAllTracesEnabled attribute.The default value

### SetAllTracesEnabled(string, bool)

Sets whether to enable the traces to be stored and retrieved after performing the QEVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetAllTracesEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [QevmAllTracesEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the traces to be stored and retrieved after performing the QEVM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXQevmConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmconfiguration-setspectruminverted__string-rfmxcdma2kmxqevmspectruminverted.html language=enus -->
## TOPIC 00165: SetSpectrumInverted(string, RFmxCdma2kMXQevmSpectrumInverted)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmconfiguration-setspectruminverted__string-rfmxcdma2kmxqevmspectruminverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmconfiguration-setspectruminverted__string-rfmxcdma2kmxqevmspectruminverted.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the spectrum of the signal is inverted. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetSpectrumInverted(string selectorString, RFmxCdma2kMXQevmSpectrumInverted value)RemarksThis method sets the value of QevmSpectrumInverted attribute.The default value is False.Parameter

### SetSpectrumInverted(string, RFmxCdma2kMXQevmSpectrumInverted)

Sets whether the spectrum of the signal is inverted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetSpectrumInverted(string selectorString, RFmxCdma2kMXQevmSpectrumInverted value)

#### Remarks

This method sets the value of [QevmSpectrumInverted](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmspectruminverted.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxCdma2kMXQevmSpectrumInverted | Specifies whether the spectrum of the signal is inverted. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXQevmConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmconfiguration.html language=enus -->
## TOPIC 00166: RFmxCdma2kMXQevmConfiguration Class

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmconfiguration.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the QEVM measurement. Derives fromRFmxCdma2kMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic class RFmxCdma2kMXQevmConfiguration : RFmxCdma2kMXSubObjectMethodsNameDescriptionConfigureAveraging(string, RFmxCdma2kMXQevmAveragingEnabled, int)Configures a

### RFmxCdma2kMXQevmConfiguration Class

Provides methods to configure the QEVM measurement.

#### Derives from

- RFmxCdma2kMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public class RFmxCdma2kMXQevmConfiguration : RFmxCdma2kMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| ConfigureAveraging(string, RFmxCdma2kMXQevmAveragingEnabled, int) | Configures averaging for QEVM measurement. |
| ConfigureMeasurementLength(string, int) | Configures the number of chips used for a single QEVM measurement iteration. |
| GetAllTracesEnabled(string, out bool) | Gets whether to enable the traces to be stored and retrieved after performing the QEVM measurement. |
| GetAveragingCount(string, out int) | Gets the number of measurements used for averaging when you set the SetAveragingEnabled(string, RFmxCdma2kMXQevmAveragingEnabled) method to True. |
| GetAveragingEnabled(string, out RFmxCdma2kMXQevmAveragingEnabled) | Gets whether to enable averaging for the QEVM measurement. |
| GetIQGainImbalanceRemovalEnabled(string, out RFmxCdma2kMXQevmIQGainImbalanceRemovalEnabled) | Gets whether to remove I/Q gain imbalance before QEVM measurement. |
| GetIQOffsetRemovalEnabled(string, out RFmxCdma2kMXQevmIQOffsetRemovalEnabled) | Gets whether to remove I/Q offset before QEVM measurement. |
| GetIQQuadratureErrorRemovalEnabled(string, out RFmxCdma2kMXQevmIQQuadratureErrorRemovalEnabled) | Gets whether to remove I/Q quadrature error before QEVM measurement. |
| GetMeasurementEnabled(string, out bool) | Gets whether to enable the QEVM measurement. |
| GetMeasurementLength(string, out int) | Gets the number of chips used for a single measurement. |
| GetNumberOfAnalysisThreads(string, out int) | Gets the maximum number of threads used for parallelism for the QEVM measurement. |
| GetReceiveFilterEnabled(string, out RFmxCdma2kMXQevmReceiveFilterEnabled) | Gets whether to enable the received filter for the QEVM measurement. |
| GetSpectrumInverted(string, out RFmxCdma2kMXQevmSpectrumInverted) | Gets whether the spectrum of the signal is inverted. |
| SetAllTracesEnabled(string, bool) | Sets whether to enable the traces to be stored and retrieved after performing the QEVM measurement. |
| SetAveragingCount(string, int) | Sets the number of measurements used for averaging when you set the SetAveragingEnabled(string, RFmxCdma2kMXQevmAveragingEnabled) method to True. |
| SetAveragingEnabled(string, RFmxCdma2kMXQevmAveragingEnabled) | Sets whether to enable averaging for the QEVM measurement. |
| SetIQGainImbalanceRemovalEnabled(string, RFmxCdma2kMXQevmIQGainImbalanceRemovalEnabled) | Sets whether to remove I/Q gain imbalance before QEVM measurement. |
| SetIQOffsetRemovalEnabled(string, RFmxCdma2kMXQevmIQOffsetRemovalEnabled) | Sets whether to remove I/Q offset before QEVM measurement. |
| SetIQQuadratureErrorRemovalEnabled(string, RFmxCdma2kMXQevmIQQuadratureErrorRemovalEnabled) | Sets whether to remove I/Q quadrature error before QEVM measurement. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable the QEVM measurement. |
| SetMeasurementLength(string, int) | Sets the number of chips used for a single measurement. |
| SetNumberOfAnalysisThreads(string, int) | Sets the maximum number of threads used for parallelism for the QEVM measurement. |
| SetReceiveFilterEnabled(string, RFmxCdma2kMXQevmReceiveFilterEnabled) | Sets whether to enable the received filter for the QEVM measurement. |
| SetSpectrumInverted(string, RFmxCdma2kMXQevmSpectrumInverted) | Sets whether the spectrum of the signal is inverted. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmiqgainimbalanceremovalenabled.html language=enus -->
## TOPIC 00167: RFmxCdma2kMXQevmIQGainImbalanceRemovalEnabled Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmiqgainimbalanceremovalenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmiqgainimbalanceremovalenabled.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove I/Q gain imbalance before QEVM measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXQevmIQGainImbalanceRemovalEnabledMembersNameValueDescriptionFalse0I/Q gain imbalance is not removed before the QEVM measurement. True1I/Q gain imbalance i

### RFmxCdma2kMXQevmIQGainImbalanceRemovalEnabled Enumeration

Specifies whether to remove I/Q gain imbalance before QEVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXQevmIQGainImbalanceRemovalEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | I/Q gain imbalance is not removed before the QEVM measurement. |
| True | 1 | I/Q gain imbalance is removed before the QEVM measurement. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-fetchevmtrace__string-double-ref.html language=enus -->
## TOPIC 00168: FetchEvmTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-fetchevmtrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-fetchevmtrace__string-double-ref.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the EVM trace of the last averaging iteration.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int FetchEvmTrace(string selectorString, double timeout, ref AnalogWaveform< float > evm)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the resul

### FetchEvmTrace(string, double, ref AnalogWaveform< float >)

Returns the EVM trace of the last averaging iteration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int FetchEvmTrace(string selectorString, double timeout, ref AnalogWaveform< float > evm)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| evm | ref AnalogWaveform< float > | Upon return, contains the trace of EVM of the corrected received signal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXQevmResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmaximumfrequencyerror__string-out.html language=enus -->
## TOPIC 00169: GetMaximumFrequencyError(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmaximumfrequencyerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmaximumfrequencyerror__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum frequency error of the received signal. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetMaximumFrequencyError(string selectorString, out double value)RemarksThis method gets the value of QevmResultsMaximumFrequencyError attribute.Parame

### GetMaximumFrequencyError(string, out double)

Gets the maximum frequency error of the received signal. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetMaximumFrequencyError(string selectorString, out double value)

#### Remarks

This method gets the value of [QevmResultsMaximumFrequencyError](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum frequency error of the received signal. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXQevmResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmaximumiqquadratureerror__string-out.html language=enus -->
## TOPIC 00170: GetMaximumIQQuadratureError(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmaximumiqquadratureerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmaximumiqquadratureerror__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetMaximumIQQuadratureError(string selectorString, out double value)RemarksThis method gets the value of QevmResultsMaximum

### GetMaximumIQQuadratureError(string, out double)

Gets the maximum I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetMaximumIQQuadratureError(string selectorString, out double value)

#### Remarks

This method gets the value of [QevmResultsMaximumIQQuadratureError](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXQevmResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmaximumpeakevm__string-out.html language=enus -->
## TOPIC 00171: GetMaximumPeakEvm(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmaximumpeakevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmaximumpeakevm__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum peak EVM of the received signal. This value is expressed as a percentage. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetMaximumPeakEvm(string selectorString, out double value)RemarksThis method gets the value of QevmResultsMaximumPeakEvm attribute.ParametersNameTyp

### GetMaximumPeakEvm(string, out double)

Gets the maximum peak EVM of the received signal. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetMaximumPeakEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [QevmResultsMaximumPeakEvm](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum peak EVM of the received signal. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXQevmResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmaximumphaseerror__string-out.html language=enus -->
## TOPIC 00172: GetMaximumPhaseError(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmaximumphaseerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmaximumphaseerror__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum phase error of the received signal. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetMaximumPhaseError(string selectorString, out double value)RemarksThis method gets the value of QevmResultsMaximumPhaseError attribute.ParametersNam

### GetMaximumPhaseError(string, out double)

Gets the maximum phase error of the received signal. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetMaximumPhaseError(string selectorString, out double value)

#### Remarks

This method gets the value of [QevmResultsMaximumPhaseError](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum phase error of the received signal. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXQevmResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmaximumrmsevm__string-out.html language=enus -->
## TOPIC 00173: GetMaximumRmsEvm(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmaximumrmsevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmaximumrmsevm__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum RMS EVM of the received signal. This value is expressed as a percentage. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetMaximumRmsEvm(string selectorString, out double value)RemarksThis method gets the value of QevmResultsMaximumRmsEvm attribute.ParametersNameTypeDe

### GetMaximumRmsEvm(string, out double)

Gets the maximum RMS EVM of the received signal. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetMaximumRmsEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [QevmResultsMaximumRmsEvm](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum RMS EVM of the received signal. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXQevmResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmeanchiprateerror__string-out.html language=enus -->
## TOPIC 00174: GetMeanChipRateError(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmeanchiprateerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmeanchiprateerror__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean chip rate error. This value is expressed in parts per million (ppm). SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetMeanChipRateError(string selectorString, out double value)RemarksThis method gets the value of QevmResultsMeanChipRateError attribute.ParametersNameTypeD

### GetMeanChipRateError(string, out double)

Gets the mean chip rate error. This value is expressed in parts per million (ppm).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetMeanChipRateError(string selectorString, out double value)

#### Remarks

This method gets the value of [QevmResultsMeanChipRateError](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean chip rate error. This value is expressed in parts per million (ppm). |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXQevmResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmeanfrequencyerror__string-out.html language=enus -->
## TOPIC 00175: GetMeanFrequencyError(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmeanfrequencyerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmeanfrequencyerror__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean averaged frequency error of the received signal. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetMeanFrequencyError(string selectorString, out double value)RemarksThis method gets the value of QevmResultsMeanFrequencyError attribute.Parame

### GetMeanFrequencyError(string, out double)

Gets the mean averaged frequency error of the received signal. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetMeanFrequencyError(string selectorString, out double value)

#### Remarks

This method gets the value of [QevmResultsMeanFrequencyError](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean averaged frequency error of the received signal. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXQevmResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmeaniqgainimbalance__string-out.html language=enus -->
## TOPIC 00176: GetMeanIQGainImbalance(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmeaniqgainimbalance__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmeaniqgainimbalance__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean I/Q gain imbalance of the received signal. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetMeanIQGainImbalance(string selectorString, out double value)RemarksThis method gets the value of QevmResultsMeanIQGainImbalance attribute.Parameters

### GetMeanIQGainImbalance(string, out double)

Gets the mean I/Q gain imbalance of the received signal. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetMeanIQGainImbalance(string selectorString, out double value)

#### Remarks

This method gets the value of [QevmResultsMeanIQGainImbalance](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean I/Q gain imbalance of the received signal. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXQevmResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmeaniqquadratureerror__string-out.html language=enus -->
## TOPIC 00177: GetMeanIQQuadratureError(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmeaniqquadratureerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmeaniqquadratureerror__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetMeanIQQuadratureError(string selectorString, out double value)RemarksThis method gets the value of QevmResultsMeanIQQuadrat

### GetMeanIQQuadratureError(string, out double)

Gets the mean I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetMeanIQQuadratureError(string selectorString, out double value)

#### Remarks

This method gets the value of [QevmResultsMeanIQQuadratureError](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXQevmResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmeanmagnitudeerror__string-out.html language=enus -->
## TOPIC 00178: GetMeanMagnitudeError(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmeanmagnitudeerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmeanmagnitudeerror__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean averaged magnitude error of the received signal. This value is expressed as a percentage. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetMeanMagnitudeError(string selectorString, out double value)RemarksThis method gets the value of QevmResultsMeanMagnitudeError attrib

### GetMeanMagnitudeError(string, out double)

Gets the mean averaged magnitude error of the received signal. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetMeanMagnitudeError(string selectorString, out double value)

#### Remarks

This method gets the value of [QevmResultsMeanMagnitudeError](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean averaged magnitude error of the received signal. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXQevmResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmeanphaseerror__string-out.html language=enus -->
## TOPIC 00179: GetMeanPhaseError(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmeanphaseerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmeanphaseerror__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean averaged phase error of the received signal. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetMeanPhaseError(string selectorString, out double value)RemarksThis method gets the value of QevmResultsMeanPhaseError attribute.ParametersNam

### GetMeanPhaseError(string, out double)

Gets the mean averaged phase error of the received signal. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetMeanPhaseError(string selectorString, out double value)

#### Remarks

This method gets the value of [QevmResultsMeanPhaseError](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean averaged phase error of the received signal. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXQevmResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmeanrmsevm__string-out.html language=enus -->
## TOPIC 00180: GetMeanRmsEvm(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmeanrmsevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults-getmeanrmsevm__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean averaged RMS EVM of the received signal. This value is expressed as a percentage. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetMeanRmsEvm(string selectorString, out double value)RemarksThis method gets the value of QevmResultsMeanRmsEvm attribute.ParametersNameTypeDe

### GetMeanRmsEvm(string, out double)

Gets the mean averaged RMS EVM of the received signal. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetMeanRmsEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [QevmResultsMeanRmsEvm](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean averaged RMS EVM of the received signal. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXQevmResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults.html language=enus -->
## TOPIC 00181: RFmxCdma2kMXQevmResults Class

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmresults.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the QEVM measurement results. Derives fromRFmxCdma2kMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic class RFmxCdma2kMXQevmResults : RFmxCdma2kMXSubObjectMethodsNameDescriptionFetchConstellationTrace(string, double, ref ComplexSingle[])Returns th

### RFmxCdma2kMXQevmResults Class

Provides methods to fetch and read the QEVM measurement results.

#### Derives from

- RFmxCdma2kMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public class RFmxCdma2kMXQevmResults : RFmxCdma2kMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchConstellationTrace(string, double, ref ComplexSingle[]) | Returns the complex chips of the corrected received signal for the QEVM measurement. |
| FetchEvm(string, double, out double, out double, out double, out double, out double, out double) | Returns the EVM value and related measurement values of the QEVM measurement. |
| FetchEvmTrace(string, double, ref AnalogWaveform< float >) | Returns the EVM trace of the last averaging iteration. |
| FetchIQImpairments(string, double, out double, out double, out double, out double, out double, out double) | Returns the measured I/Q impairments. |
| FetchMagnitudeErrorTrace(string, double, ref AnalogWaveform< float >) | Returns the magnitude error trace of the last averaging iteration. |
| FetchPhaseErrorTrace(string, double, ref AnalogWaveform< float >) | Returns the phase error trace of the last averaging iteration. |
| GetMaximumChipRateError(string, out double) | Gets the maximum chip rate error. This value is expressed in parts per million (ppm). |
| GetMaximumFrequencyError(string, out double) | Gets the maximum frequency error of the received signal. This value is expressed in Hz. |
| GetMaximumIQGainImbalance(string, out double) | Gets the maximum I/Q gain imbalance of the received signal. This value is expressed in dB. |
| GetMaximumIQOriginOffset(string, out double) | Gets the maximum origin offset of the received signal. This value is expressed in dB. |
| GetMaximumIQQuadratureError(string, out double) | Gets the maximum I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees. |
| GetMaximumMagnitudeError(string, out double) | Gets the maximum magnitude error of the received signal. This value is expressed as a percentage. |
| GetMaximumPeakEvm(string, out double) | Gets the maximum peak EVM of the received signal. This value is expressed as a percentage. |
| GetMaximumPhaseError(string, out double) | Gets the maximum phase error of the received signal. This value is expressed in degrees. |
| GetMaximumRmsEvm(string, out double) | Gets the maximum RMS EVM of the received signal. This value is expressed as a percentage. |
| GetMeanChipRateError(string, out double) | Gets the mean chip rate error. This value is expressed in parts per million (ppm). |
| GetMeanFrequencyError(string, out double) | Gets the mean averaged frequency error of the received signal. This value is expressed in Hz. |
| GetMeanIQGainImbalance(string, out double) | Gets the mean I/Q gain imbalance of the received signal. This value is expressed in dB. |
| GetMeanIQOriginOffset(string, out double) | Gets the mean averaged origin offset of the received signal. This value is expressed in dB. |
| GetMeanIQQuadratureError(string, out double) | Gets the mean I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees. |
| GetMeanMagnitudeError(string, out double) | Gets the mean averaged magnitude error of the received signal. This value is expressed as a percentage. |
| GetMeanPeakEvm(string, out double) | Gets the mean averaged peak EVM of the received signal. This value is expressed as a percentage. |
| GetMeanPhaseError(string, out double) | Gets the mean averaged phase error of the received signal. This value is expressed in degrees. |
| GetMeanRmsEvm(string, out double) | Gets the mean averaged RMS EVM of the received signal. This value is expressed as a percentage. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmspectruminverted.html language=enus -->
## TOPIC 00182: RFmxCdma2kMXQevmSpectrumInverted Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmspectruminverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxqevmspectruminverted.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the spectrum of the signal is inverted. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXQevmSpectrumInvertedMembersNameValueDescriptionFalse0The measurement spectrum is normal. True1The measurement spectrum is inverted.

### RFmxCdma2kMXQevmSpectrumInverted Enumeration

Specifies whether the spectrum of the signal is inverted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXQevmSpectrumInverted

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement spectrum is normal. |
| True | 1 | The measurement spectrum is inverted. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxradioconfiguration.html language=enus -->
## TOPIC 00183: RFmxCdma2kMXRadioConfiguration Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxradioconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxradioconfiguration.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the radio configuration for the channel. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXRadioConfigurationMembersNameValueDescriptionRC10If SetLinkDirection(string, RFmxCdma2kMXLinkDirection) method is set to Uplink, Radio configuration 1 includes 64-ary orthogon

### RFmxCdma2kMXRadioConfiguration Enumeration

Specifies the radio configuration for the channel.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXRadioConfiguration

#### Members

| Name | Value | Description |
| --- | --- | --- |
| RC1 | 0 | If SetLinkDirection(string, RFmxCdma2kMXLinkDirection) method is set to Uplink, Radio configuration 1 includes 64-ary orthogonal modulation, reverse fundamental channel (R-FCH), and reverse supplemental code channels (R-SCCHs).If Link Direction method is set to Downlink, Radio Configuration 1 includes binary phase-shift keying (BPSK), forward fundamental channels (F-FCHs) and forward supplemental channels (F-SCHs). |
| RC2 | 1 | If Link Direction method is set to Uplink, Radio configuration 2 includes 64-ary orthogonal modulation, R-FCH, and R-SCCHs.If Link Direction method is set to Downlink, Radio Configuration 2 includes BPSKs, F-FCHs and F-SCHs. |
| RC3 | 2 | If Link Direction method is set to Uplink, Radio configuration 3 includes BPSK, R-FCH, and reverse supplemental channels (R-SCHs).If Link Direction method is set to Downlink, Radio Configuration 3 includes quadrature phase-shift keying (QPSK), F-FCHs and F-SCHs. |
| RC4 | 3 | If Link Direction method is set to Uplink, Radio configuration 4 includes BPSK, R-FCH, and R-SCHs.If Link Direction method is set to Downlink, Radio Configuration 4 includes QPSK, F-FCHs and F-SCHs. |
| RC5 | 4 | If Link Direction method is set to Uplink, Radio configuration 5 is not supported and gives invalid results.If Link Direction method is set to Downlink, Radio Configuration 5 includes QPSK, F-FCHs and F-SCHs. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsem-configuration.html language=enus -->
## TOPIC 00184: Configuration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsem-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsem-configuration.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxCdma2kMXSemConfiguration instance that provides methods to configure the SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic RFmxCdma2kMXSemConfiguration Configuration { get; }

### Configuration

Gets the [RFmxCdma2kMXSemConfiguration](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration.html) instance that provides methods to configure the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public [RFmxCdma2kMXSemConfiguration](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration.html) Configuration { get; }

Parent topic:

RFmxCdma2kMXSem Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsem-results.html language=enus -->
## TOPIC 00185: Results

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsem-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsem-results.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxCdma2kMXSemResults instance that provides methods to fetch and read the SEM measurement results. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic RFmxCdma2kMXSemResults Results { get; }

### Results

Gets the [RFmxCdma2kMXSemResults](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults.html) instance that provides methods to fetch and read the SEM measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public [RFmxCdma2kMXSemResults](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults.html) Results { get; }

Parent topic:

RFmxCdma2kMXSem Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsem.html language=enus -->
## TOPIC 00186: RFmxCdma2kMXSem Class

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsem.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsem.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the SEM measurement. Derives fromRFmxCdma2kMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic class RFmxCdma2kMXSem : RFmxCdma2kMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxCdma2kMXSemConfiguration instance that provides methods to configure the SEM measu

### RFmxCdma2kMXSem Class

Represents the SEM measurement.

#### Derives from

- RFmxCdma2kMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public class RFmxCdma2kMXSem : RFmxCdma2kMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxCdma2kMXSemConfiguration instance that provides methods to configure the SEM measurement. |
| Results | Gets the RFmxCdma2kMXSemResults instance that provides methods to fetch and read the SEM measurement results. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemaveragingenabled.html language=enus -->
## TOPIC 00187: RFmxCdma2kMXSemAveragingEnabled Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemaveragingenabled.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXSemAveragingEnabledMembersNameValueDescriptionFalse0The measurement is performed on a single acquisition. True1The SEM measurement uses the value of the SetAveragi

### RFmxCdma2kMXSemAveragingEnabled Enumeration

Specifies whether to enable averaging for the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXSemAveragingEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement is performed on a single acquisition. |
| True | 1 | The SEM measurement uses the value of the SetAveragingCount(string, int) method as the number of acquisitions over which the SEM measurement is averaged. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemaveragingtype.html language=enus -->
## TOPIC 00188: RFmxCdma2kMXSemAveragingType Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemaveragingtype.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXSemAveragingTypeMembersNameValueDescriptionRms0The power spectrum is linearly averaged. RMS aver

### RFmxCdma2kMXSemAveragingType Enumeration

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXSemAveragingType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rms | 0 | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log | 1 | The power spectrum is averaged in a logarithmic scale. |
| Scalar | 2 | The square root of the power spectrum is averaged. |
| Maximum | 3 | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Minimum | 4 | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-configureaveraging__string-rfmxcdma2kmxsemaveragingenabled-int-rfmxcdma2kmxsemaveragingtype.html language=enus -->
## TOPIC 00189: ConfigureAveraging(string, RFmxCdma2kMXSemAveragingEnabled, int, RFmxCdma2kMXSemAveragingType)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-configureaveraging__string-rfmxcdma2kmxsemaveragingenabled-int-rfmxcdma2kmxsemaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-configureaveraging__string-rfmxcdma2kmxsemaveragingenabled-int-rfmxcdma2kmxsemaveragingtype.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the SEM measurement.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int ConfigureAveraging(string selectorString, RFmxCdma2kMXSemAveragingEnabled averagingEnabled, int averagingCount, RFmxCdma2kMXSemAveragingType averagingType)ParametersNameTypeDescriptionselectorSt

### ConfigureAveraging(string, RFmxCdma2kMXSemAveragingEnabled, int, RFmxCdma2kMXSemAveragingType)

Configures averaging for the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int ConfigureAveraging(string selectorString, RFmxCdma2kMXSemAveragingEnabled averagingEnabled, int averagingCount, RFmxCdma2kMXSemAveragingType averagingType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| averagingEnabled | RFmxCdma2kMXSemAveragingEnabled | Specifies whether to enable averaging for the measurement. |
| averagingCount | int | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True. |
| averagingType | RFmxCdma2kMXSemAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. RFmx uses the averaged spectrum for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-configuresweeptime__string-rfmxcdma2kmxsemsweeptimeauto-double.html language=enus -->
## TOPIC 00190: ConfigureSweepTime(string, RFmxCdma2kMXSemSweepTimeAuto, double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-configuresweeptime__string-rfmxcdma2kmxsemsweeptimeauto-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-configuresweeptime__string-rfmxcdma2kmxsemsweeptimeauto-double.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int ConfigureSweepTime(string selectorString, RFmxCdma2kMXSemSweepTimeAuto sweepTimeAuto, double sweepTimeInterval)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed

### ConfigureSweepTime(string, RFmxCdma2kMXSemSweepTimeAuto, double)

Configures the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int ConfigureSweepTime(string selectorString, RFmxCdma2kMXSemSweepTimeAuto sweepTimeAuto, double sweepTimeInterval)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| sweepTimeAuto | RFmxCdma2kMXSemSweepTimeAuto | Specifies whether the measurement computes the sweep time. |
| sweepTimeInterval | double | Specifies the sweep time when you set the sweepTimeAuto parameter to False. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00191: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the traces to be stored and retrieved after performing the SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method gets the value of SemAllTracesEnabled attribute.The default val

### GetAllTracesEnabled(string, out bool)

Gets whether to enable the traces to be stored and retrieved after performing the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [SemAllTracesEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the traces to be stored and retrieved after performing the SEM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getaveragingcount__string-out.html language=enus -->
## TOPIC 00192: GetAveragingCount(string, out int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getaveragingcount__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getaveragingcount__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxCdma2kMXSemAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetAveragingCount(string selectorString, out int value)RemarksThis method gets the value of Se

### GetAveragingCount(string, out int)

Gets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxCdma2kMXSemAveragingEnabled)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setaveragingenabled__string-rfmxcdma2kmxsemaveragingenabled.html) method to [True](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetAveragingCount(string selectorString, out int value)

#### Remarks

This method gets the value of [SemAveragingCount](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxCdma2kMXSemAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getaveragingenabled__string-out.html language=enus -->
## TOPIC 00193: GetAveragingEnabled(string, out RFmxCdma2kMXSemAveragingEnabled)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getaveragingenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getaveragingenabled__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable averaging for the SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetAveragingEnabled(string selectorString, out RFmxCdma2kMXSemAveragingEnabled value)RemarksThis method gets the value of SemAveragingEnabled attribute.The default value is False.Pa

### GetAveragingEnabled(string, out RFmxCdma2kMXSemAveragingEnabled)

Gets whether to enable averaging for the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetAveragingEnabled(string selectorString, out RFmxCdma2kMXSemAveragingEnabled value)

#### Remarks

This method gets the value of [SemAveragingEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxCdma2kMXSemAveragingEnabled | Upon return, contains whether to enable averaging for the SEM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getaveragingtype__string-out.html language=enus -->
## TOPIC 00194: GetAveragingType(string, out RFmxCdma2kMXSemAveragingType)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getaveragingtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getaveragingtype__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetAveragingType(string selectorString, out RFmxCdma2kMXSemAveragingType value)RemarksThis method gets the value o

### GetAveragingType(string, out RFmxCdma2kMXSemAveragingType)

Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetAveragingType(string selectorString, out RFmxCdma2kMXSemAveragingType value)

#### Remarks

This method gets the value of [SemAveragingType](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [Rms](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemaveragingtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxCdma2kMXSemAveragingType | Upon return, contains the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the SEM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getcarrierintegrationbandwidth__string-out.html language=enus -->
## TOPIC 00195: GetCarrierIntegrationBandwidth(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getcarrierintegrationbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getcarrierintegrationbandwidth__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the SEM carrier integration bandwidth. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetCarrierIntegrationBandwidth(string selectorString, out double value)RemarksThis method gets the value of SemCarrierIntegrationBandwidth attribute.ParametersNameT

### GetCarrierIntegrationBandwidth(string, out double)

Gets the SEM carrier integration bandwidth. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetCarrierIntegrationBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [SemCarrierIntegrationBandwidth](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the SEM carrier integration bandwidth. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00196: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method gets the value of SemMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescriptionselectorSt

### GetMeasurementEnabled(string, out bool)

Gets whether to enable the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [SemMeasurementEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the SEM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getnumberofanalysisthreads__string-out.html language=enus -->
## TOPIC 00197: GetNumberOfAnalysisThreads(string, out int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getnumberofanalysisthreads__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getnumberofanalysisthreads__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum number of threads used for parallelism for the SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetNumberOfAnalysisThreads(string selectorString, out int value)RemarksThis method gets the value of SemNumberOfAnalysisThreads attribute.The default value is

### GetNumberOfAnalysisThreads(string, out int)

Gets the maximum number of threads used for parallelism for the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetNumberOfAnalysisThreads(string selectorString, out int value)

#### Remarks

This method gets the value of [SemNumberOfAnalysisThreads](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the maximum number of threads used for parallelism for the SEM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getnumberofoffsets__string-out.html language=enus -->
## TOPIC 00198: GetNumberOfOffsets(string, out int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getnumberofoffsets__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getnumberofoffsets__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of SEM offset segments. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetNumberOfOffsets(string selectorString, out int value)RemarksThis method gets the value of SemNumberOfOffsets attribute.ParametersNameTypeDescriptionselectorStringstringPass an empty string. The si

### GetNumberOfOffsets(string, out int)

Gets the number of SEM offset segments.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetNumberOfOffsets(string selectorString, out int value)

#### Remarks

This method gets the value of [SemNumberOfOffsets](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of SEM offset segments. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getoffsetbandwidthintegral__string-out.html language=enus -->
## TOPIC 00199: GetOffsetBandwidthIntegral(string, out int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getoffsetbandwidthintegral__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getoffsetbandwidthintegral__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the bandwidth integral for a specific offset segment. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetOffsetBandwidthIntegral(string selectorString, out int value)RemarksThis method gets the value of SemOffsetBandwidthIntegral attribute.Use "offset(n)" as the Selector Strings to

### GetOffsetBandwidthIntegral(string, out int)

Gets the bandwidth integral for a specific offset segment.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetOffsetBandwidthIntegral(string selectorString, out int value)

#### Remarks

This method gets the value of [SemOffsetBandwidthIntegral](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.Use "offset(n)" as the Selector Strings to read this result.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the bandwidth integral for a specific offset segment. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getoffsetrbwfilterbandwidth__string-out.html language=enus -->
## TOPIC 00200: GetOffsetRbwFilterBandwidth(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getoffsetrbwfilterbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getoffsetrbwfilterbandwidth__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the bandwidth of the RBW filter used to sweep the offset segment. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetOffsetRbwFilterBandwidth(string selectorString, out double value)RemarksThis method gets the value of SemOffsetRbwFilterBandwidth attr

### GetOffsetRbwFilterBandwidth(string, out double)

Gets the bandwidth of the RBW filter used to sweep the offset segment. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetOffsetRbwFilterBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [SemOffsetRbwFilterBandwidth](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the bandwidth of the RBW filter used to sweep the offset segment. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getoffsetrbwfiltertype__string-out.html language=enus -->
## TOPIC 00201: GetOffsetRbwFilterType(string, out RFmxCdma2kMXSemOffsetRbwFilterType)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getoffsetrbwfiltertype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getoffsetrbwfiltertype__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the type of RBW filter used to sweep the offset segment. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetOffsetRbwFilterType(string selectorString, out RFmxCdma2kMXSemOffsetRbwFilterType value)RemarksThis method gets the value of SemOffsetRbwFilterType attribute.The default valu

### GetOffsetRbwFilterType(string, out RFmxCdma2kMXSemOffsetRbwFilterType)

Gets the type of RBW filter used to sweep the offset segment.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetOffsetRbwFilterType(string selectorString, out RFmxCdma2kMXSemOffsetRbwFilterType value)

#### Remarks

This method gets the value of [SemOffsetRbwFilterType](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [Gaussian](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemoffsetrbwfiltertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out RFmxCdma2kMXSemOffsetRbwFilterType | Upon return, contains the type of RBW filter used to sweep the offset segment. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getoffsetstartfrequency__string-out.html language=enus -->
## TOPIC 00202: GetOffsetStartFrequency(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getoffsetstartfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getoffsetstartfrequency__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the start frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetOffsetStartFrequency(string selectorString, out double value)RemarksThis method gets the value of SemOffsetStartFrequenc

### GetOffsetStartFrequency(string, out double)

Gets the start frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetOffsetStartFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [SemOffsetStartFrequency](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the start frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getoffsetstopfrequency__string-out.html language=enus -->
## TOPIC 00203: GetOffsetStopFrequency(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getoffsetstopfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getoffsetstopfrequency__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the stop frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetOffsetStopFrequency(string selectorString, out double value)RemarksThis method gets the value of SemOffsetStopFrequency a

### GetOffsetStopFrequency(string, out double)

Gets the stop frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetOffsetStopFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [SemOffsetStopFrequency](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the stop frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getsweeptimeauto__string-out.html language=enus -->
## TOPIC 00204: GetSweepTimeAuto(string, out RFmxCdma2kMXSemSweepTimeAuto)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getsweeptimeauto__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getsweeptimeauto__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement computes the sweep time. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetSweepTimeAuto(string selectorString, out RFmxCdma2kMXSemSweepTimeAuto value)RemarksThis method gets the value of SemSweepTimeAuto attribute.The default value is True.ParametersNameTy

### GetSweepTimeAuto(string, out RFmxCdma2kMXSemSweepTimeAuto)

Gets whether the measurement computes the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetSweepTimeAuto(string selectorString, out RFmxCdma2kMXSemSweepTimeAuto value)

#### Remarks

This method gets the value of [SemSweepTimeAuto](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemsweeptimeauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxCdma2kMXSemSweepTimeAuto | Upon return, contains whether the measurement computes the sweep time. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getsweeptimeinterval__string-out.html language=enus -->
## TOPIC 00205: GetSweepTimeInterval(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getsweeptimeinterval__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-getsweeptimeinterval__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the sweep time when you set the SetSweepTimeAuto(string, RFmxCdma2kMXSemSweepTimeAuto) method to False. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetSweepTimeInterval(string selectorString, out double value)RemarksThis method gets the value

### GetSweepTimeInterval(string, out double)

Gets the sweep time when you set the [SetSweepTimeAuto(string, RFmxCdma2kMXSemSweepTimeAuto)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setsweeptimeauto__string-rfmxcdma2kmxsemsweeptimeauto.html) method to [False](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemsweeptimeauto.html). This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetSweepTimeInterval(string selectorString, out double value)

#### Remarks

This method gets the value of [SemSweepTimeInterval](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 0.001667 seconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the sweep time when you set the SetSweepTimeAuto(string, RFmxCdma2kMXSemSweepTimeAuto) method to False. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setalltracesenabled__string-bool.html language=enus -->
## TOPIC 00206: SetAllTracesEnabled(string, bool)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setalltracesenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setalltracesenabled__string-bool.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the traces to be stored and retrieved after performing the SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetAllTracesEnabled(string selectorString, bool value)RemarksThis method sets the value of SemAllTracesEnabled attribute.The default value i

### SetAllTracesEnabled(string, bool)

Sets whether to enable the traces to be stored and retrieved after performing the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetAllTracesEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [SemAllTracesEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the traces to be stored and retrieved after performing the SEM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setaveragingcount__string-int.html language=enus -->
## TOPIC 00207: SetAveragingCount(string, int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setaveragingcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setaveragingcount__string-int.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxCdma2kMXSemAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetAveragingCount(string selectorString, int value)RemarksThis method sets the value of SemAve

### SetAveragingCount(string, int)

Sets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxCdma2kMXSemAveragingEnabled)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setaveragingenabled__string-rfmxcdma2kmxsemaveragingenabled.html) method to [True](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetAveragingCount(string selectorString, int value)

#### Remarks

This method sets the value of [SemAveragingCount](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxCdma2kMXSemAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setaveragingenabled__string-rfmxcdma2kmxsemaveragingenabled.html language=enus -->
## TOPIC 00208: SetAveragingEnabled(string, RFmxCdma2kMXSemAveragingEnabled)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setaveragingenabled__string-rfmxcdma2kmxsemaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setaveragingenabled__string-rfmxcdma2kmxsemaveragingenabled.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable averaging for the SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetAveragingEnabled(string selectorString, RFmxCdma2kMXSemAveragingEnabled value)RemarksThis method sets the value of SemAveragingEnabled attribute.The default value is False.Parame

### SetAveragingEnabled(string, RFmxCdma2kMXSemAveragingEnabled)

Sets whether to enable averaging for the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetAveragingEnabled(string selectorString, RFmxCdma2kMXSemAveragingEnabled value)

#### Remarks

This method sets the value of [SemAveragingEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxCdma2kMXSemAveragingEnabled | Specifies whether to enable averaging for the SEM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setaveragingtype__string-rfmxcdma2kmxsemaveragingtype.html language=enus -->
## TOPIC 00209: SetAveragingType(string, RFmxCdma2kMXSemAveragingType)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setaveragingtype__string-rfmxcdma2kmxsemaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setaveragingtype__string-rfmxcdma2kmxsemaveragingtype.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetAveragingType(string selectorString, RFmxCdma2kMXSemAveragingType value)RemarksThis method sets the value of Se

### SetAveragingType(string, RFmxCdma2kMXSemAveragingType)

Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetAveragingType(string selectorString, RFmxCdma2kMXSemAveragingType value)

#### Remarks

This method sets the value of [SemAveragingType](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [Rms](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemaveragingtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxCdma2kMXSemAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the SEM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00210: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method sets the value of SemMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescriptionselectorString

### SetMeasurementEnabled(string, bool)

Sets whether to enable the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [SemMeasurementEnabled](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the SEM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setnumberofanalysisthreads__string-int.html language=enus -->
## TOPIC 00211: SetNumberOfAnalysisThreads(string, int)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setnumberofanalysisthreads__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setnumberofanalysisthreads__string-int.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the maximum number of threads used for parallelism for the SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetNumberOfAnalysisThreads(string selectorString, int value)RemarksThis method sets the value of SemNumberOfAnalysisThreads attribute.The default value is 1.P

### SetNumberOfAnalysisThreads(string, int)

Sets the maximum number of threads used for parallelism for the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetNumberOfAnalysisThreads(string selectorString, int value)

#### Remarks

This method sets the value of [SemNumberOfAnalysisThreads](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the maximum number of threads used for parallelism for the SEM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setsweeptimeauto__string-rfmxcdma2kmxsemsweeptimeauto.html language=enus -->
## TOPIC 00212: SetSweepTimeAuto(string, RFmxCdma2kMXSemSweepTimeAuto)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setsweeptimeauto__string-rfmxcdma2kmxsemsweeptimeauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setsweeptimeauto__string-rfmxcdma2kmxsemsweeptimeauto.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement computes the sweep time. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetSweepTimeAuto(string selectorString, RFmxCdma2kMXSemSweepTimeAuto value)RemarksThis method sets the value of SemSweepTimeAuto attribute.The default value is True.ParametersNameTypeDe

### SetSweepTimeAuto(string, RFmxCdma2kMXSemSweepTimeAuto)

Sets whether the measurement computes the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetSweepTimeAuto(string selectorString, RFmxCdma2kMXSemSweepTimeAuto value)

#### Remarks

This method sets the value of [SemSweepTimeAuto](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemsweeptimeauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxCdma2kMXSemSweepTimeAuto | Specifies whether the measurement computes the sweep time. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setsweeptimeinterval__string-double.html language=enus -->
## TOPIC 00213: SetSweepTimeInterval(string, double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setsweeptimeinterval__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setsweeptimeinterval__string-double.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the sweep time when you set the SetSweepTimeAuto(string, RFmxCdma2kMXSemSweepTimeAuto) method to False. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int SetSweepTimeInterval(string selectorString, double value)RemarksThis method sets the value of

### SetSweepTimeInterval(string, double)

Sets the sweep time when you set the [SetSweepTimeAuto(string, RFmxCdma2kMXSemSweepTimeAuto)](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration-setsweeptimeauto__string-rfmxcdma2kmxsemsweeptimeauto.html) method to [False](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemsweeptimeauto.html). This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int SetSweepTimeInterval(string selectorString, double value)

#### Remarks

This method sets the value of [SemSweepTimeInterval](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.The default value is 0.001667 seconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the sweep time when you set the SetSweepTimeAuto(string, RFmxCdma2kMXSemSweepTimeAuto) method to False. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration.html language=enus -->
## TOPIC 00214: RFmxCdma2kMXSemConfiguration Class

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemconfiguration.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the SEM measurement. Derives fromRFmxCdma2kMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic class RFmxCdma2kMXSemConfiguration : RFmxCdma2kMXSubObjectMethodsNameDescriptionConfigureAveraging(string, RFmxCdma2kMXSemAveragingEnabled, int, RFmxCdma2kMXSe

### RFmxCdma2kMXSemConfiguration Class

Provides methods to configure the SEM measurement.

#### Derives from

- RFmxCdma2kMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public class RFmxCdma2kMXSemConfiguration : RFmxCdma2kMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| ConfigureAveraging(string, RFmxCdma2kMXSemAveragingEnabled, int, RFmxCdma2kMXSemAveragingType) | Configures averaging for the SEM measurement. |
| ConfigureSweepTime(string, RFmxCdma2kMXSemSweepTimeAuto, double) | Configures the sweep time. |
| GetAllTracesEnabled(string, out bool) | Gets whether to enable the traces to be stored and retrieved after performing the SEM measurement. |
| GetAveragingCount(string, out int) | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxCdma2kMXSemAveragingEnabled) method to True. |
| GetAveragingEnabled(string, out RFmxCdma2kMXSemAveragingEnabled) | Gets whether to enable averaging for the SEM measurement. |
| GetAveragingType(string, out RFmxCdma2kMXSemAveragingType) | Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the SEM measurement. |
| GetCarrierIntegrationBandwidth(string, out double) | Gets the SEM carrier integration bandwidth. This value is expressed in Hz. |
| GetMeasurementEnabled(string, out bool) | Gets whether to enable the SEM measurement. |
| GetNumberOfAnalysisThreads(string, out int) | Gets the maximum number of threads used for parallelism for the SEM measurement. |
| GetNumberOfOffsets(string, out int) | Gets the number of SEM offset segments. |
| GetOffsetBandwidthIntegral(string, out int) | Gets the bandwidth integral for a specific offset segment. |
| GetOffsetRbwFilterBandwidth(string, out double) | Gets the bandwidth of the RBW filter used to sweep the offset segment. This value is expressed in Hz. |
| GetOffsetRbwFilterType(string, out RFmxCdma2kMXSemOffsetRbwFilterType) | Gets the type of RBW filter used to sweep the offset segment. |
| GetOffsetStartFrequency(string, out double) | Gets the start frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz. |
| GetOffsetStopFrequency(string, out double) | Gets the stop frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz. |
| GetSweepTimeAuto(string, out RFmxCdma2kMXSemSweepTimeAuto) | Gets whether the measurement computes the sweep time. |
| GetSweepTimeInterval(string, out double) | Gets the sweep time when you set the SetSweepTimeAuto(string, RFmxCdma2kMXSemSweepTimeAuto) method to False. This value is expressed in seconds. |
| SetAllTracesEnabled(string, bool) | Sets whether to enable the traces to be stored and retrieved after performing the SEM measurement. |
| SetAveragingCount(string, int) | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxCdma2kMXSemAveragingEnabled) method to True. |
| SetAveragingEnabled(string, RFmxCdma2kMXSemAveragingEnabled) | Sets whether to enable averaging for the SEM measurement. |
| SetAveragingType(string, RFmxCdma2kMXSemAveragingType) | Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the SEM measurement. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable the SEM measurement. |
| SetNumberOfAnalysisThreads(string, int) | Sets the maximum number of threads used for parallelism for the SEM measurement. |
| SetSweepTimeAuto(string, RFmxCdma2kMXSemSweepTimeAuto) | Sets whether the measurement computes the sweep time. |
| SetSweepTimeInterval(string, double) | Sets the sweep time when you set the SetSweepTimeAuto(string, RFmxCdma2kMXSemSweepTimeAuto) method to False. This value is expressed in seconds. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemloweroffsetmeasurementstatus.html language=enus -->
## TOPIC 00215: RFmxCdma2kMXSemLowerOffsetMeasurementStatus Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemloweroffsetmeasurementstatus.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemloweroffsetmeasurementstatus.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the lower offset segment measurement status based on measurement limits specified by the standard.Use "offset(n)" as the Selector Strings to read this result. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXSemLowerOffsetMeasurementStatusMembersNameValueDescriptio

### RFmxCdma2kMXSemLowerOffsetMeasurementStatus Enumeration

Indicates the lower offset segment measurement status based on measurement limits specified by the standard.Use "offset(n)" as the Selector Strings to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXSemLowerOffsetMeasurementStatus

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Fail | 0 | The lower offset segment measurement fails according to the measurement limits specified by the standard. |
| Pass | 1 | The lower offset segment measurement passes according to the measurement limits specified by the standard. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemmeasurementstatus.html language=enus -->
## TOPIC 00216: RFmxCdma2kMXSemMeasurementStatus Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemmeasurementstatus.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemmeasurementstatus.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the overall measurement status based on the measurement limits, which are specified by the standard for each offset segment. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXSemMeasurementStatusMembersNameValueDescriptionFail0The measurement fails according to the

### RFmxCdma2kMXSemMeasurementStatus Enumeration

Indicates the overall measurement status based on the measurement limits, which are specified by the standard for each offset segment.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXSemMeasurementStatus

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Fail | 0 | The measurement fails according to the measurement limits specified by this standard. |
| Pass | 1 | The measurement passes according to the measurement limits specified by this standard. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemoffsetrbwfiltertype.html language=enus -->
## TOPIC 00217: RFmxCdma2kMXSemOffsetRbwFilterType Enumeration

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemoffsetrbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemoffsetrbwfiltertype.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the type of RBW filter used to sweep the offset segment. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic enum RFmxCdma2kMXSemOffsetRbwFilterTypeMembersNameValueDescriptionFftBased0No RBW filtering is performed. Gaussian1The RBW filter has a Gaussian response. Flat2The RBW filter has

### RFmxCdma2kMXSemOffsetRbwFilterType Enumeration

Returns the type of RBW filter used to sweep the offset segment.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public enum RFmxCdma2kMXSemOffsetRbwFilterType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| FftBased | 0 | No RBW filtering is performed. |
| Gaussian | 1 | The RBW filter has a Gaussian response. |
| Flat | 2 | The RBW filter has a flat response. |
| SynchTuned4 | 3 | The RBW filter has a response of a 4-pole synchronously tuned filter. |
| SynchTuned5 | 4 | The RBW filter has a response of a 5-pole synchronously tuned filter. |

Parent topic:

NationalInstruments.RFmx.Cdma2kMX

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchcarrierabsoluteintegratedpower__string-double-out.html language=enus -->
## TOPIC 00218: FetchCarrierAbsoluteIntegratedPower(string, double, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchcarrierabsoluteintegratedpower__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchcarrierabsoluteintegratedpower__string-double-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute carrier integrated power of the SEM measurement.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int FetchCarrierAbsoluteIntegratedPower(string selectorString, double timeout, out double carrierAbsoluteIntegratedPower)ParametersNameTypeDescriptionselectorStringstringSpec

### FetchCarrierAbsoluteIntegratedPower(string, double, out double)

Returns the absolute carrier integrated power of the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int FetchCarrierAbsoluteIntegratedPower(string selectorString, double timeout, out double carrierAbsoluteIntegratedPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| carrierAbsoluteIntegratedPower | out double | Upon return, contains the averaged integrated channel power measured in the specified integration bandwidth. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchloweroffsetmargin__string-double-out-out-out-out-out.html language=enus -->
## TOPIC 00219: FetchLowerOffsetMargin(string, double, out RFmxCdma2kMXSemLowerOffsetMeasurementStatus, out double, out double, out double, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchloweroffsetmargin__string-double-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchloweroffsetmargin__string-double-out-out-out-out-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status and margin from the limit line measured in the lower offset segment. Use "offset(n)" as the selector string to read parameters from this method.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int FetchLowerOffsetMargin(string selectorString, double timeout, ou

### FetchLowerOffsetMargin(string, double, out RFmxCdma2kMXSemLowerOffsetMeasurementStatus, out double, out double, out double, out double)

Returns the measurement status and margin from the limit line measured in the lower offset segment. 
 Use "offset(n)" as the selector string to read parameters from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int FetchLowerOffsetMargin(string selectorString, double timeout, out RFmxCdma2kMXSemLowerOffsetMeasurementStatus measurementStatus, out double margin, out double marginFrequency, out double marginAbsolutePower, out double marginRelativePower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and offset number. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| measurementStatus | out RFmxCdma2kMXSemLowerOffsetMeasurementStatus | Upon return, contains the lower offset measurement status based on measurement limits and the failure criteria specified by the standard. |
| margin | out double | Upon return, contains the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum difference between the spectrum and the closest limit mask (absolute or relative). |
| marginFrequency | out double | Upon return, contains the frequency at which the margin occurred in the lower (negative) offset. This value is expressed in Hz. |
| marginAbsolutePower | out double | Upon return, contains the power at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm. |
| marginRelativePower | out double | Upon return, contains the power at which the margin occurred in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchloweroffsetmarginarray__string-double-ref-ref-ref-ref-ref.html language=enus -->
## TOPIC 00220: FetchLowerOffsetMarginArray(string, double, ref RFmxCdma2kMXSemLowerOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[])

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchloweroffsetmarginarray__string-double-ref-ref-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchloweroffsetmarginarray__string-double-ref-ref-ref-ref-ref.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the array of measurement status and margins from the limit line measured in the lower offset segments.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int FetchLowerOffsetMarginArray(string selectorString, double timeout, ref RFmxCdma2kMXSemLowerOffsetMeasurementStatus[] measurementS

### FetchLowerOffsetMarginArray(string, double, ref RFmxCdma2kMXSemLowerOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[])

Returns the array of measurement status and margins from the limit line measured in the lower offset segments.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int FetchLowerOffsetMarginArray(string selectorString, double timeout, ref RFmxCdma2kMXSemLowerOffsetMeasurementStatus[] measurementStatus, ref double[] margin, ref double[] marginFrequency, ref double[] marginAbsolutePower, ref double[] marginRelativePower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| measurementStatus | ref RFmxCdma2kMXSemLowerOffsetMeasurementStatus[] | Upon return, contains the array of lower offset measurement status based on measurement limits and the failure criteria specified by the standard. |
| margin | ref double[] | Upon return, contains the array of margins from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the maximum difference between the spectrum and the limit mask. |
| marginFrequency | ref double[] | Upon return, contains the array of frequencies at which the margin occurred in each lower (negative) offset segment. This value is expressed in Hz. |
| marginAbsolutePower | ref double[] | Upon return, contains the array of powers at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm. |
| marginRelativePower | ref double[] | Upon return, contains the array of powers at which the margin occurred in each lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchloweroffsetpower__string-double-out-out-out-out-out.html language=enus -->
## TOPIC 00221: FetchLowerOffsetPower(string, double, out double, out double, out double, out double, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchloweroffsetpower__string-double-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchloweroffsetpower__string-double-out-out-out-out-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the lower offset segment power measurements. Use "offset(n)" as the selector string to read parameters from this method.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int FetchLowerOffsetPower(string selectorString, double timeout, out double absoluteIntegratedPower, out double rel

### FetchLowerOffsetPower(string, double, out double, out double, out double, out double, out double)

Returns the lower offset segment power measurements. 
 Use "offset(n)" as the selector string to read parameters from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int FetchLowerOffsetPower(string selectorString, double timeout, out double absoluteIntegratedPower, out double relativeIntegratedPower, out double absolutePeakPower, out double peakFrequency, out double relativePeakPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and offset number. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| absoluteIntegratedPower | out double | Upon return, contains the lower (negative) offset segment power measured. |
| relativeIntegratedPower | out double | Upon return, contains the power in the lower (negative) offset segment relative to the carrier absolute integrated power. |
| absolutePeakPower | out double | Upon return, contains the peak power measured in the lower (negative) offset segment. The power is measured in dBm. |
| peakFrequency | out double | Upon return, contains the frequency at which the peak power occurred in the offset segment. This value is expressed in Hz. |
| relativePeakPower | out double | Upon return, contains the peak power in the lower (negative) offset segment relative to the carrier absolute integrated power. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchloweroffsetpowerarray__string-double-ref-ref-ref-ref-ref.html language=enus -->
## TOPIC 00222: FetchLowerOffsetPowerArray(string, double, ref double[], ref double[], ref double[], ref double[], ref double[])

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchloweroffsetpowerarray__string-double-ref-ref-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchloweroffsetpowerarray__string-double-ref-ref-ref-ref-ref.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the arrays of lower offset segment power measurements.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int FetchLowerOffsetPowerArray(string selectorString, double timeout, ref double[] absoluteIntegratedPower, ref double[] relativeIntegratedPower, ref double[] absolutePeakPower, ref

### FetchLowerOffsetPowerArray(string, double, ref double[], ref double[], ref double[], ref double[], ref double[])

Returns the arrays of lower offset segment power measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int FetchLowerOffsetPowerArray(string selectorString, double timeout, ref double[] absoluteIntegratedPower, ref double[] relativeIntegratedPower, ref double[] absolutePeakPower, ref double[] peakFrequency, ref double[] relativePeakPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| absoluteIntegratedPower | ref double[] | Upon return, contains the array of lower (negative) offset segment powers measured. |
| relativeIntegratedPower | ref double[] | Upon return, contains the array of powers in each lower (negative) offset segment relative to the carrier absolute integrated power. |
| absolutePeakPower | ref double[] | Upon return, contains the array of peak powers measured in each lower (negative) offset segment. The power is measured in dBm. |
| peakFrequency | ref double[] | Upon return, contains the array of frequencies at which the peak power occurred in each offset segment. This value is expressed in Hz. |
| relativePeakPower | ref double[] | Upon return, contains the array of peak powers in the lower (negative) offset segment relative to the carrier absolute integrated power. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchmeasurementstatus__string-double-out.html language=enus -->
## TOPIC 00223: FetchMeasurementStatus(string, double, out RFmxCdma2kMXSemMeasurementStatus)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchmeasurementstatus__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchmeasurementstatus__string-double-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the SEM measurement status.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int FetchMeasurementStatus(string selectorString, double timeout, out RFmxCdma2kMXSemMeasurementStatus measurementStatus)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising

### FetchMeasurementStatus(string, double, out RFmxCdma2kMXSemMeasurementStatus)

Returns the SEM measurement status.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int FetchMeasurementStatus(string selectorString, double timeout, out RFmxCdma2kMXSemMeasurementStatus measurementStatus)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| measurementStatus | out RFmxCdma2kMXSemMeasurementStatus | Upon return, contains the overall measurement status based on the measurement limits which are specified by the standard for each offset segment. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchspectrum__string-double-ref-ref-ref.html language=enus -->
## TOPIC 00224: FetchSpectrum(string, double, ref Spectrum< float >, ref Spectrum< float >, ref Spectrum< float >)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchspectrum__string-double-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchspectrum__string-double-ref-ref-ref.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the spectrum used for the SEM measurement.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int FetchSpectrum(string selectorString, double timeout, ref Spectrum< float > spectrum, ref Spectrum< float > absoluteMask, ref Spectrum< float > relativeMask)ParametersNameTypeDescriptionsele

### FetchSpectrum(string, double, ref Spectrum< float >, ref Spectrum< float >, ref Spectrum< float >)

Returns the spectrum used for the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int FetchSpectrum(string selectorString, double timeout, ref Spectrum< float > spectrum, ref Spectrum< float > absoluteMask, ref Spectrum< float > relativeMask)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| spectrum | ref Spectrum< float > | Upon return, contains the trace of power levels in the spectral domain. This value is expressed in dBm. |
| absoluteMask | ref Spectrum< float > | Upon return, contains the trace of power levels representing the absolute mask in the spectral domain. |
| relativeMask | ref Spectrum< float > | Upon return, contains the trace of power levels representing the relative mask in the spectral domain. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchupperoffsetmargin__string-double-out-out-out-out-out.html language=enus -->
## TOPIC 00225: FetchUpperOffsetMargin(string, double, out RFmxCdma2kMXSemUpperOffsetMeasurementStatus, out double, out double, out double, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchupperoffsetmargin__string-double-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchupperoffsetmargin__string-double-out-out-out-out-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status and margin from the limit line measured in the upper offset segment. Use "offset(n)" as the selector string to read parameters from this method.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int FetchUpperOffsetMargin(string selectorString, double timeout, ou

### FetchUpperOffsetMargin(string, double, out RFmxCdma2kMXSemUpperOffsetMeasurementStatus, out double, out double, out double, out double)

Returns the measurement status and margin from the limit line measured in the upper offset segment. 
 Use "offset(n)" as the selector string to read parameters from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int FetchUpperOffsetMargin(string selectorString, double timeout, out RFmxCdma2kMXSemUpperOffsetMeasurementStatus measurementStatus, out double margin, out double marginFrequency, out double marginAbsolutePower, out double marginRelativePower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and offset number. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| measurementStatus | out RFmxCdma2kMXSemUpperOffsetMeasurementStatus | Indicates the upper offset measurement status based on measurement limits and the failure criteria specified by the standard. |
| margin | out double | Upon return, contains the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum difference between the spectrum and the closest limit mask (absolute or relative). |
| marginFrequency | out double | Upon return, contains the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz. |
| marginAbsolutePower | out double | Upon return, contains the power at which the margin occurred in the upper (positive) offset segment. This value is expressed in dBm. |
| marginRelativePower | out double | Upon return, contains the power at which the margin occurred in the upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchupperoffsetmarginarray__string-double-ref-ref-ref-ref-ref.html language=enus -->
## TOPIC 00226: FetchUpperOffsetMarginArray(string, double, ref RFmxCdma2kMXSemUpperOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[])

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchupperoffsetmarginarray__string-double-ref-ref-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchupperoffsetmarginarray__string-double-ref-ref-ref-ref-ref.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status and margin from the limit line measured in the upper offset segments.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int FetchUpperOffsetMarginArray(string selectorString, double timeout, ref RFmxCdma2kMXSemUpperOffsetMeasurementStatus[] measurementStatus, ref

### FetchUpperOffsetMarginArray(string, double, ref RFmxCdma2kMXSemUpperOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[])

Returns the measurement status and margin from the limit line measured in the upper offset segments.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int FetchUpperOffsetMarginArray(string selectorString, double timeout, ref RFmxCdma2kMXSemUpperOffsetMeasurementStatus[] measurementStatus, ref double[] margin, ref double[] marginFrequency, ref double[] marginAbsolutePower, ref double[] marginRelativePower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| measurementStatus | ref RFmxCdma2kMXSemUpperOffsetMeasurementStatus[] | Upon return, contains the array of upper offset measurement statuses based on measurement limits and the failure criteria specified by the standard. |
| margin | ref double[] | Upon return, contains the array of margins from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum difference between the spectrum and the closest limit mask (absolute or relative). |
| marginFrequency | ref double[] | Upon return, contains the array of frequencies at which the margin occurred in each upper (positive) offset. This value is expressed in Hz. |
| marginAbsolutePower | ref double[] | Upon return, contains the array of powers at which the margin occurred in each upper (positive) offset segment. This value is expressed in dBm. |
| marginRelativePower | ref double[] | Upon return, contains the array of powers at which the margin occurred in each upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchupperoffsetpower__string-double-out-out-out-out-out.html language=enus -->
## TOPIC 00227: FetchUpperOffsetPower(string, double, out double, out double, out double, out double, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchupperoffsetpower__string-double-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchupperoffsetpower__string-double-out-out-out-out-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the upper offset segment power measurements. Use "offset(n)" as the selector string to read parameters from this method.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int FetchUpperOffsetPower(string selectorString, double timeout, out double absoluteIntegratedPower, out double rel

### FetchUpperOffsetPower(string, double, out double, out double, out double, out double, out double)

Returns the upper offset segment power measurements. 
 Use "offset(n)" as the selector string to read parameters from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int FetchUpperOffsetPower(string selectorString, double timeout, out double absoluteIntegratedPower, out double relativeIntegratedPower, out double absolutePeakPower, out double peakFrequency, out double relativePeakPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and offset number. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| absoluteIntegratedPower | out double | Upon return, contains the upper (positive) offset segment power measured. |
| relativeIntegratedPower | out double | Upon return, contains the power in the upper (positive) offset segment relative to the carrier absolute integrated power. |
| absolutePeakPower | out double | Upon return, contains the peak power measured in the upper (positive) offset segment. The power is measured in dBm. |
| peakFrequency | out double | Upon return, contains the frequency at which the peak power occurred in the offset segment. This value is expressed in Hz. |
| relativePeakPower | out double | Upon return, contains the peak power in the upper (positive) offset segment relative to the carrier absolute integrated power. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchupperoffsetpowerarray__string-double-ref-ref-ref-ref-ref.html language=enus -->
## TOPIC 00228: FetchUpperOffsetPowerArray(string, double, ref double[], ref double[], ref double[], ref double[], ref double[])

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchupperoffsetpowerarray__string-double-ref-ref-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-fetchupperoffsetpowerarray__string-double-ref-ref-ref-ref-ref.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the arrays of upper offset segment power measurements.SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int FetchUpperOffsetPowerArray(string selectorString, double timeout, ref double[] absoluteIntegratedPower, ref double[] relativeIntegratedPower, ref double[] absolutePeakPower, ref

### FetchUpperOffsetPowerArray(string, double, ref double[], ref double[], ref double[], ref double[], ref double[])

Returns the arrays of upper offset segment power measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int FetchUpperOffsetPowerArray(string selectorString, double timeout, ref double[] absoluteIntegratedPower, ref double[] relativeIntegratedPower, ref double[] absolutePeakPower, ref double[] peakFrequency, ref double[] relativePeakPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| absoluteIntegratedPower | ref double[] | Upon return, contains the array of upper (positive) offset segment powers measured. |
| relativeIntegratedPower | ref double[] | Upon return, contains the array of powers measured in each upper (positive) offset segment relative to the carrier absolute integrated power. |
| absolutePeakPower | ref double[] | Upon return, contains the array of peak powers measured in each upper (positive) offset segment. The power is measured in dBm. |
| peakFrequency | ref double[] | Upon return, contains the array of frequencies at which the peak power occurred in each offset segment. This value is expressed in Hz. |
| relativePeakPower | ref double[] | Upon return, contains the array of peak powers measured in each upper (positive) offset segment relative to the carrier absolute integrated power. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getcarrierabsoluteintegratedpower__string-out.html language=enus -->
## TOPIC 00229: GetCarrierAbsoluteIntegratedPower(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getcarrierabsoluteintegratedpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getcarrierabsoluteintegratedpower__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the carrier power. The carrier power is the power centered at the center frequency and integrated over the carrier bandwidth of 1.23 MHz. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetCarrierAbsoluteIntegratedPower(string selectorString, out dou

### GetCarrierAbsoluteIntegratedPower(string, out double)

Gets the carrier power. The carrier power is the power centered at the center frequency and integrated over the carrier bandwidth of 1.23 MHz. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetCarrierAbsoluteIntegratedPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsCarrierAbsoluteIntegratedPower](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the carrier power. The carrier power is the power centered at the center frequency and integrated over the carrier bandwidth of 1.23 MHz. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetabsoluteintegratedpower__string-out.html language=enus -->
## TOPIC 00230: GetLowerOffsetAbsoluteIntegratedPower(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetabsoluteintegratedpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetabsoluteintegratedpower__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the absolute power measured in the lower (negative) offset segment. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetLowerOffsetAbsoluteIntegratedPower(string selectorString, out double va

### GetLowerOffsetAbsoluteIntegratedPower(string, out double)

Gets the absolute power measured in the lower (negative) offset segment. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetLowerOffsetAbsoluteIntegratedPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetAbsoluteIntegratedPower](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the absolute power measured in the lower (negative) offset segment. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetabsolutepeakpower__string-out.html language=enus -->
## TOPIC 00231: GetLowerOffsetAbsolutePeakPower(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetabsolutepeakpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetabsolutepeakpower__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power measured in the lower (negative) offset segment. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetLowerOffsetAbsolutePeakPower(string selectorString, out double value)Remark

### GetLowerOffsetAbsolutePeakPower(string, out double)

Gets the peak power measured in the lower (negative) offset segment. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetLowerOffsetAbsolutePeakPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetAbsolutePeakPower](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak power measured in the lower (negative) offset segment. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetmargin__string-out.html language=enus -->
## TOPIC 00232: GetLowerOffsetMargin(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetmargin__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetmargin__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum difference between the spectrum and the closest limit mask, which can be absolute or relative.Use "offset(n)" as the Selector Strings to read this result. SyntaxNamesp

### GetLowerOffsetMargin(string, out double)

Gets the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum difference between the spectrum and the closest limit mask, which can be absolute or relative.Use "offset(n)" as the Selector Strings to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetLowerOffsetMargin(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetMargin](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum difference between the spectrum and the closest limit mask, which can be absolute or relative.Use "offset(n)" as the Selector Strings to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetmarginabsolutepower__string-out.html language=enus -->
## TOPIC 00233: GetLowerOffsetMarginAbsolutePower(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetmarginabsolutepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetmarginabsolutepower__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the absolute power at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetLowerOffsetMarginAbsolutePower(string selectorStrin

### GetLowerOffsetMarginAbsolutePower(string, out double)

Gets the absolute power at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetLowerOffsetMarginAbsolutePower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetMarginAbsolutePower](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the absolute power at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetmarginfrequency__string-out.html language=enus -->
## TOPIC 00234: GetLowerOffsetMarginFrequency(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetmarginfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetmarginfrequency__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency at which the margin occurred in the lower (negative) offset segment. This value is expressed in Hz.Use "offset(n)" as the Selector Strings to read this result. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetLowerOffsetMarginFrequency(string selectorString, out dou

### GetLowerOffsetMarginFrequency(string, out double)

Gets the frequency at which the margin occurred in the lower (negative) offset segment. This value is expressed in Hz.Use "offset(n)" as the Selector Strings to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetLowerOffsetMarginFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetMarginFrequency](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the frequency at which the margin occurred in the lower (negative) offset segment. This value is expressed in Hz.Use "offset(n)" as the Selector Strings to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetmarginrelativepower__string-out.html language=enus -->
## TOPIC 00235: GetLowerOffsetMarginRelativePower(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetmarginrelativepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetmarginrelativepower__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power at which the margin occurred in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetLowerOffset

### GetLowerOffsetMarginRelativePower(string, out double)

Gets the power at which the margin occurred in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetLowerOffsetMarginRelativePower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetMarginRelativePower](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power at which the margin occurred in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetmeasurementstatus__string-out.html language=enus -->
## TOPIC 00236: GetLowerOffsetMeasurementStatus(string, out RFmxCdma2kMXSemLowerOffsetMeasurementStatus)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetmeasurementstatus__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetmeasurementstatus__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the lower offset segment measurement status based on measurement limits specified by the standard.Use "offset(n)" as the Selector Strings to read this result. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetLowerOffsetMeasurementStatus(string selectorString, out RFmxCdma2kM

### GetLowerOffsetMeasurementStatus(string, out RFmxCdma2kMXSemLowerOffsetMeasurementStatus)

Indicates the lower offset segment measurement status based on measurement limits specified by the standard.Use "offset(n)" as the Selector Strings to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetLowerOffsetMeasurementStatus(string selectorString, out RFmxCdma2kMXSemLowerOffsetMeasurementStatus value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetMeasurementStatus](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out RFmxCdma2kMXSemLowerOffsetMeasurementStatus | Indicates the lower offset segment measurement status based on measurement limits specified by the standard.Use "offset(n)" as the Selector Strings to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetpeakfrequency__string-out.html language=enus -->
## TOPIC 00237: GetLowerOffsetPeakFrequency(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetpeakfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetpeakfrequency__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency at which the peak power occurred in the lower offset segment. This value is expressed in Hz. Use "offset(n)" as the Selector Strings to read this result. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetLowerOffsetPeakFrequency(string selectorString, out double valu

### GetLowerOffsetPeakFrequency(string, out double)

Gets the frequency at which the peak power occurred in the lower offset segment. This value is expressed in Hz. Use "offset(n)" as the Selector Strings to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetLowerOffsetPeakFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetPeakFrequency](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the frequency at which the peak power occurred in the lower offset segment. This value is expressed in Hz. Use "offset(n)" as the Selector Strings to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetrelativeintegratedpower__string-out.html language=enus -->
## TOPIC 00238: GetLowerOffsetRelativeIntegratedPower(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetrelativeintegratedpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetrelativeintegratedpower__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power measured in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetLowerOffsetRelativeIntegratedPo

### GetLowerOffsetRelativeIntegratedPower(string, out double)

Gets the power measured in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetLowerOffsetRelativeIntegratedPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetRelativeIntegratedPower](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power measured in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetrelativepeakpower__string-out.html language=enus -->
## TOPIC 00239: GetLowerOffsetRelativePeakPower(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetrelativepeakpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getloweroffsetrelativepeakpower__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power measured in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetLowerOffsetRelativePeakPow

### GetLowerOffsetRelativePeakPower(string, out double)

Gets the peak power measured in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetLowerOffsetRelativePeakPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetRelativePeakPower](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak power measured in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getmeasurementstatus__string-out.html language=enus -->
## TOPIC 00240: GetMeasurementStatus(string, out RFmxCdma2kMXSemMeasurementStatus)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getmeasurementstatus__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getmeasurementstatus__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the overall measurement status based on the measurement limits, which are specified by the standard for each offset segment. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetMeasurementStatus(string selectorString, out RFmxCdma2kMXSemMeasurementStatus value)RemarksThis metho

### GetMeasurementStatus(string, out RFmxCdma2kMXSemMeasurementStatus)

Indicates the overall measurement status based on the measurement limits, which are specified by the standard for each offset segment.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetMeasurementStatus(string selectorString, out RFmxCdma2kMXSemMeasurementStatus value)

#### Remarks

This method gets the value of [SemResultsMeasurementStatus](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out RFmxCdma2kMXSemMeasurementStatus | Indicates the overall measurement status based on the measurement limits, which are specified by the standard for each offset segment. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetabsoluteintegratedpower__string-out.html language=enus -->
## TOPIC 00241: GetUpperOffsetAbsoluteIntegratedPower(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetabsoluteintegratedpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetabsoluteintegratedpower__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power measured in the upper (positive) offset segment. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetUpperOffsetAbsoluteIntegratedPower(string selectorString, out double value)Remark

### GetUpperOffsetAbsoluteIntegratedPower(string, out double)

Gets the power measured in the upper (positive) offset segment. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetUpperOffsetAbsoluteIntegratedPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetAbsoluteIntegratedPower](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power measured in the upper (positive) offset segment. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetabsolutepeakpower__string-out.html language=enus -->
## TOPIC 00242: GetUpperOffsetAbsolutePeakPower(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetabsolutepeakpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetabsolutepeakpower__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power measured in the upper (positive) offset segment. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetUpperOffsetAbsolutePeakPower(string selectorString, out double value)Remark

### GetUpperOffsetAbsolutePeakPower(string, out double)

Gets the peak power measured in the upper (positive) offset segment. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetUpperOffsetAbsolutePeakPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetAbsolutePeakPower](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak power measured in the upper (positive) offset segment. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetmargin__string-out.html language=enus -->
## TOPIC 00243: GetUpperOffsetMargin(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetmargin__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetmargin__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum difference between the spectrum and the closest limit mask (absolute or relative).Use "offset(n)" as the Selector Strings to read this result. SyntaxNamespace: Nationa

### GetUpperOffsetMargin(string, out double)

Gets the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum difference between the spectrum and the closest limit mask (absolute or relative).Use "offset(n)" as the Selector Strings to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetUpperOffsetMargin(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetMargin](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum difference between the spectrum and the closest limit mask (absolute or relative).Use "offset(n)" as the Selector Strings to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetmarginabsolutepower__string-out.html language=enus -->
## TOPIC 00244: GetUpperOffsetMarginAbsolutePower(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetmarginabsolutepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetmarginabsolutepower__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power at which the margin occurred in the upper (positive) offset segment. This value is expressed in dBm. Use "offset(n)" as the Selector Strings to read this result. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetUpperOffsetMarginAbsolutePower(string selectorString, out d

### GetUpperOffsetMarginAbsolutePower(string, out double)

Gets the power at which the margin occurred in the upper (positive) offset segment. This value is expressed in dBm. Use "offset(n)" as the Selector Strings to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetUpperOffsetMarginAbsolutePower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetMarginAbsolutePower](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power at which the margin occurred in the upper (positive) offset segment. This value is expressed in dBm. Use "offset(n)" as the Selector Strings to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetmarginfrequency__string-out.html language=enus -->
## TOPIC 00245: GetUpperOffsetMarginFrequency(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetmarginfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetmarginfrequency__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz.Use "offset(n)" as the Selector Strings to read this result. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetUpperOffsetMarginFrequency(string selectorString, out double valu

### GetUpperOffsetMarginFrequency(string, out double)

Gets the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz.Use "offset(n)" as the Selector Strings to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetUpperOffsetMarginFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetMarginFrequency](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz.Use "offset(n)" as the Selector Strings to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetmarginrelativepower__string-out.html language=enus -->
## TOPIC 00246: GetUpperOffsetMarginRelativePower(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetmarginrelativepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetmarginrelativepower__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power at which the margin occurred in the upper (positive) offset segment. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetUpperOffsetMarginRelativePower(string selectorString, out do

### GetUpperOffsetMarginRelativePower(string, out double)

Gets the power at which the margin occurred in the upper (positive) offset segment. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetUpperOffsetMarginRelativePower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetMarginRelativePower](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power at which the margin occurred in the upper (positive) offset segment. This value is expressed in dBm.Use "offset(n)" as the Selector Strings to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetmeasurementstatus__string-out.html language=enus -->
## TOPIC 00247: GetUpperOffsetMeasurementStatus(string, out RFmxCdma2kMXSemUpperOffsetMeasurementStatus)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetmeasurementstatus__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetmeasurementstatus__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the upper offset measurement status based on measurement limits set by the standard.Use "offset(n)" as the Selector Strings to read this result. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetUpperOffsetMeasurementStatus(string selectorString, out RFmxCdma2kMXSemUpperOffse

### GetUpperOffsetMeasurementStatus(string, out RFmxCdma2kMXSemUpperOffsetMeasurementStatus)

Indicates the upper offset measurement status based on measurement limits set by the standard.Use "offset(n)" as the Selector Strings to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetUpperOffsetMeasurementStatus(string selectorString, out RFmxCdma2kMXSemUpperOffsetMeasurementStatus value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetMeasurementStatus](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out RFmxCdma2kMXSemUpperOffsetMeasurementStatus | Indicates the upper offset measurement status based on measurement limits set by the standard.Use "offset(n)" as the Selector Strings to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetpeakfrequency__string-out.html language=enus -->
## TOPIC 00248: GetUpperOffsetPeakFrequency(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetpeakfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetpeakfrequency__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency at which the peak power occurred in the upper offset segment. This value is expressed in Hz.Use "offset(n)" as the Selector Strings to read this result. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetUpperOffsetPeakFrequency(string selectorString, out double value

### GetUpperOffsetPeakFrequency(string, out double)

Gets the frequency at which the peak power occurred in the upper offset segment. This value is expressed in Hz.Use "offset(n)" as the Selector Strings to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetUpperOffsetPeakFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetPeakFrequency](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the frequency at which the peak power occurred in the upper offset segment. This value is expressed in Hz.Use "offset(n)" as the Selector Strings to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetrelativeintegratedpower__string-out.html language=enus -->
## TOPIC 00249: GetUpperOffsetRelativeIntegratedPower(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetrelativeintegratedpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetrelativeintegratedpower__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power measured in the upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetUpperOffsetRelativeIntegratedPo

### GetUpperOffsetRelativeIntegratedPower(string, out double)

Gets the power measured in the upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetUpperOffsetRelativeIntegratedPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetRelativeIntegratedPower](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power measured in the upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class

<!--NI_TOPIC bundle=rfmxcdma2k-dotnet-api-ref path=nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetrelativepeakpower__string-out.html language=enus -->
## TOPIC 00250: GetUpperOffsetRelativePeakPower(string, out double)

- bundle_id: `rfmxcdma2k-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetrelativepeakpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxsemresults-getupperoffsetrelativepeakpower__string-out.html
- document_id: `rfmxcdma2k-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power measured in the upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result. SyntaxNamespace: NationalInstruments.RFmx.Cdma2kMXpublic int GetUpperOffsetRelativePeakPow

### GetUpperOffsetRelativePeakPower(string, out double)

Gets the peak power measured in the upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.Cdma2kMX](nationalinstruments-rfmx-cdma2kmx.html)

public int GetUpperOffsetRelativePeakPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetRelativePeakPower](nationalinstruments-rfmx-cdma2kmx-rfmxcdma2kmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Offset number. Example: "Offset0", "result::r1/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak power measured in the upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.Use "offset(n)" as the Selector Strings to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxCdma2kMXSemResults Class
