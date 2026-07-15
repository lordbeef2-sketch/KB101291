# NI DOCUMENT BUNDLE: rfmxgsm-dotnet-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxgsm-dotnet-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-abortmeasurements__string.html language=enus -->
## TOPIC 00001: AbortMeasurements(string)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-abortmeasurements__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-abortmeasurements__string.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops acquisition and measurements associated with the signal instance that you specify in the selectorString parameter. This acquisition and measurements were previously initiated by the Initiate(string, string) method. Calling this method is optional, unless you want to stop a measurement before i

### AbortMeasurements(string)

Stops acquisition and measurements associated with the signal instance that you specify in the *selectorString* parameter. This acquisition and measurements were previously initiated by the [Initiate(string, string)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-initiate__string-string.html) method. Calling this method is optional, unless you want to stop a measurement before it is complete. This method executes even if there is an incoming error.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int AbortMeasurements(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-analyzeiq1waveform__string-string-complexwaveform_complexsingle_-bool-long.html language=enus -->
## TOPIC 00002: AnalyzeIQ1Waveform(string, string, ComplexWaveform< ComplexSingle >, bool, long)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-analyzeiq1waveform__string-string-complexwaveform_complexsingle_-bool-long.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-analyzeiq1waveform__string-string-complexwaveform_complexsingle_-bool-long.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods. Use this method only if the RFmxInstrMX.GetRecommended

### AnalyzeIQ1Waveform(string, string, ComplexWaveform< ComplexSingle >, bool, long)

Performs the enabled measurements on the I/Q complex waveform that you specify in *IQ* parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods. Use this method only if the RFmxInstrMX.GetRecommendedAcquisitionType method value is *IQ*. 
 Query the RFmxInstrMX.GetRecommendedAcquisitionType method after calling the [Commit(string)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-commit__string.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int AnalyzeIQ1Waveform(string selectorString, string resultName, ComplexWaveform< ComplexSingle > iq, bool reset, long reserved)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the result name in this parameter, either the result name specified by the resultName parameter or the default result instance is used. Example: "" "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| resultName | string | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example: "" "result::r1" "r1" |
| iq | ComplexWaveform< ComplexSingle > | Specifies the data for a complex waveform including the start, delta, and actual values. |
| reset | bool | Resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| reserved | long | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-autolevel__string-double-out.html language=enus -->
## TOPIC 00003: AutoLevel(string, double, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-autolevel__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-autolevel__string-double-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Examines the input signal to calculate the peak power level and sets it as the value of the SetReferenceLevel(string, double) method. Use this method to help calculate an approximate setting for the reference level. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int AutoLevel(string selectorS

### AutoLevel(string, double, out double)

Examines the input signal to calculate the peak power level and sets it as the value of the [SetReferenceLevel(string, double)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setreferencelevel__string-double.html) method. Use this method to help calculate an approximate setting for the reference level.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int AutoLevel(string selectorString, double measurementInterval, out double referenceLevel)

#### Remarks

1. Resets the mixer level, mixer level offset, and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation, and preamplifier enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after completing execution.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| measurementInterval | double | Specifies the acquisition length. Use this value to compute the number of samples to acquire from the signal analyzer. This value is expressed in seconds. Auto Level VI does not use any trigger for acquisition. It ignores the user-configured trigger properties. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. |
| referenceLevel | out double | Upon return, contains the estimated peak power level of the input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-buildoffsetstring__string-int.html language=enus -->
## TOPIC 00004: BuildOffsetString(string, int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-buildoffsetstring__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-buildoffsetstring__string-int.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a offset string to use as the selector string with configuration or fetch methods and methods.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic static string BuildOffsetString(string selectorString, int offsetNumber)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector st

### BuildOffsetString(string, int)

Creates a offset string to use as the selector string with configuration or fetch methods and methods.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public static string BuildOffsetString(string selectorString, int offsetNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| offsetNumber | int | Specifies the offset number for building the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-buildresultstring__string.html language=enus -->
## TOPIC 00005: BuildResultString(string)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-buildresultstring__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-buildresultstring__string.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates selector string for use with configuration or fetch. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic static string BuildResultString(string resultName)ParametersNameTypeDescriptionresultNamestringSpecifies the result name for building the selector string. This input accepts the result

### BuildResultString(string)

Creates selector string for use with configuration or fetch.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public static string BuildResultString(string resultName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| resultName | string | Specifies the result name for building the selector string. This input accepts the result name with or without the "result::" prefix. Example: "", "result::r1", "r1". |

#### Returns

Upon return, contains the selector string created by this method.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-buildslotstring__string-int.html language=enus -->
## TOPIC 00006: BuildSlotString(string, int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-buildslotstring__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-buildslotstring__string-int.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a slot string to use as the selector string with configuration or fetch methods and methods.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic static string BuildSlotString(string selectorString, int slotNumber)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string c

### BuildSlotString(string, int)

Creates a slot string to use as the selector string with configuration or fetch methods and methods.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public static string BuildSlotString(string selectorString, int slotNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| slotNumber | int | Specifies the slot number for building the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-checkmeasurementstatus__string-out.html language=enus -->
## TOPIC 00007: CheckMeasurementStatus(string, out bool)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-checkmeasurementstatus__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-checkmeasurementstatus__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks the status of the measurement. Use this method to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int CheckMeasurementStatus(string selectorString, out bool d

### CheckMeasurementStatus(string, out bool)

Checks the status of the measurement. Use this method to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int CheckMeasurementStatus(string selectorString, out bool done)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| done | out bool | Indicates whether the measurement is complete. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-clearallnamedresults__string.html language=enus -->
## TOPIC 00008: ClearAllNamedResults(string)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-clearallnamedresults__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-clearallnamedresults__string.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all results for the current signal instance.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int ClearAllNamedResults(string selectorString)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when creating the signal configuration is used

### ClearAllNamedResults(string)

Clears all results for the current signal instance.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ClearAllNamedResults(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-clearnamedresult__string.html language=enus -->
## TOPIC 00009: ClearNamedResult(string)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-clearnamedresult__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-clearnamedresult__string.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears a result instance specified by the result name in the selectorString parameter.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int ClearNamedResult(string selectorString)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the result name. If you do

### ClearNamedResult(string)

Clears a result instance specified by the result name in the *selectorString* parameter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ClearNamedResult(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-clonesignalconfiguration__string-out.html language=enus -->
## TOPIC 00010: CloneSignalConfiguration(string, out RFmxGsmMX)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-clonesignalconfiguration__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-clonesignalconfiguration__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal by copying all the method values from an existing signal instance.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int CloneSignalConfiguration(string newSignalName, out RFmxGsmMX signalConfiguration)ParametersNameTypeDescriptionnewSignalNamestringSpecifies th

### CloneSignalConfiguration(string, out RFmxGsmMX)

Creates a new instance of a signal by copying all the method values from an existing signal instance.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int CloneSignalConfiguration(string newSignalName, out RFmxGsmMX signalConfiguration)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| newSignalName | string | Specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::NewSigName" "NewSigName" |
| signalConfiguration | out RFmxGsmMX | Upon return, contains a new GSM signal instance. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-commit__string.html language=enus -->
## TOPIC 00011: Commit(string)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-commit__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-commit__string.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits settings to the hardware. Calling this method is optional. RFmxGSM commits settings to the hardware when you call the Initiate(string, string) method. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int Commit(string selectorString)ParametersNameTypeDescriptionselectorStringstringPass

### Commit(string)

Commits settings to the hardware. Calling this method is optional. RFmxGSM commits settings to the hardware when you call the [Initiate(string, string)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-initiate__string-string.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int Commit(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configureautotscdetectionenabled__string-rfmxgsmmxautotscdetectionenabled.html language=enus -->
## TOPIC 00012: ConfigureAutoTscDetectionEnabled(string, RFmxGsmMXAutoTscDetectionEnabled)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configureautotscdetectionenabled__string-rfmxgsmmxautotscdetectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configureautotscdetectionenabled__string-rfmxgsmmxautotscdetectionenabled.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether to auto detect the training sequence code (TSC).SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int ConfigureAutoTscDetectionEnabled(string selectorString, RFmxGsmMXAutoTscDetectionEnabled autoTscDetectionEnabled)ParametersNameTypeDescriptionselectorStringstringPass an empty

### ConfigureAutoTscDetectionEnabled(string, RFmxGsmMXAutoTscDetectionEnabled)

Configures whether to auto detect the training sequence code (TSC).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigureAutoTscDetectionEnabled(string selectorString, RFmxGsmMXAutoTscDetectionEnabled autoTscDetectionEnabled)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| autoTscDetectionEnabled | RFmxGsmMXAutoTscDetectionEnabled | Specifies whether to auto detect the TSC. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configureband__string-rfmxgsmmxband.html language=enus -->
## TOPIC 00013: ConfigureBand(string, RFmxGsmMXBand)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configureband__string-rfmxgsmmxband.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configureband__string-rfmxgsmmxband.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the band of operation.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int ConfigureBand(string selectorString, RFmxGsmMXBand band)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when creating the signal configuration is used.band

### ConfigureBand(string, RFmxGsmMXBand)

Configures the band of operation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigureBand(string selectorString, RFmxGsmMXBand band)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| band | RFmxGsmMXBand | Specifies the band of operation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configureburstsynchronizationtype__string-rfmxgsmmxburstsynchronizationtype.html language=enus -->
## TOPIC 00014: ConfigureBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configureburstsynchronizationtype__string-rfmxgsmmxburstsynchronizationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configureburstsynchronizationtype__string-rfmxgsmmxburstsynchronizationtype.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the burst synchronization type.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int ConfigureBurstSynchronizationType(string selectorString, RFmxGsmMXBurstSynchronizationType burstSynchronizationType)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal na

### ConfigureBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType)

Configures the burst synchronization type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigureBurstSynchronizationType(string selectorString, RFmxGsmMXBurstSynchronizationType burstSynchronizationType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| burstSynchronizationType | RFmxGsmMXBurstSynchronizationType | Specifies the method used to synchronize the burst. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configuredigitaledgetrigger__string-string-rfmxgsmmxdigitaledgetriggeredge-double-bool.html language=enus -->
## TOPIC 00015: ConfigureDigitalEdgeTrigger(string, string, RFmxGsmMXDigitalEdgeTriggerEdge, double, bool)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configuredigitaledgetrigger__string-string-rfmxgsmmxdigitaledgetriggeredge-double-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configuredigitaledgetrigger__string-string-rfmxgsmmxdigitaledgetriggeredge-double-bool.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a digital edge trigger and then marks a reference point within the record. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int ConfigureDigitalEdgeTrigger(string selectorString, string digitalEdgeTriggerSource, RFmxGsmMXDigitalEdgeTriggerEdge digitalEdgeTrigge

### ConfigureDigitalEdgeTrigger(string, string, RFmxGsmMXDigitalEdgeTriggerEdge, double, bool)

Configures the device to wait for a digital edge trigger and then marks a reference point within the record.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigureDigitalEdgeTrigger(string selectorString, string digitalEdgeTriggerSource, RFmxGsmMXDigitalEdgeTriggerEdge digitalEdgeTriggerEdge, double triggerDelay, bool enableTrigger)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| digitalEdgeTriggerSource | string | Specifies the source terminal for the digital-edge trigger. Use the string constants from the RFmxGsmMXConstants class or any other valid string to configure this parameter. |
| digitalEdgeTriggerEdge | RFmxGsmMXDigitalEdgeTriggerEdge | Specifies the trigger edge to detect. |
| triggerDelay | double | Specifies the trigger delay time. This value is expressed in seconds. |
| enableTrigger | bool | Specifies whether to enable the trigger. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configureexternalattenuation__string-double.html language=enus -->
## TOPIC 00016: ConfigureExternalAttenuation(string, double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configureexternalattenuation__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configureexternalattenuation__string-double.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int ConfigureExternalAttenuation(string selectorString, double externalAttenuation)ParametersNameTypeDescriptionselectorStringstringPass an emp

### ConfigureExternalAttenuation(string, double)

Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigureExternalAttenuation(string selectorString, double externalAttenuation)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| externalAttenuation | double | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the External Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configurefrequency__string-double.html language=enus -->
## TOPIC 00017: ConfigureFrequency(string, double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configurefrequency__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configurefrequency__string-double.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the center frequency of the RF signal to acquire. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int ConfigureFrequency(string selectorString, double centerFrequency)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when creating

### ConfigureFrequency(string, double)

Configures the center frequency of the RF signal to acquire.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigureFrequency(string selectorString, double centerFrequency)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| centerFrequency | double | Specifies the expected center frequency of the RF signal to acquire. This value is expressed in Hz. The signal analyzer tunes to this frequency. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configurefrequencyarfcn__string-rfmxgsmmxlinkdirection-rfmxgsmmxband-int.html language=enus -->
## TOPIC 00018: ConfigureFrequencyArfcn(string, RFmxGsmMXLinkDirection, RFmxGsmMXBand, int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configurefrequencyarfcn__string-rfmxgsmmxlinkdirection-rfmxgsmmxband-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configurefrequencyarfcn__string-rfmxgsmmxlinkdirection-rfmxgsmmxband-int.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the center frequency from the absolute RF channel number (ARFCN), band, and the link direction.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int ConfigureFrequencyArfcn(string selectorString, RFmxGsmMXLinkDirection linkDirection, RFmxGsmMXBand band, int arfcn)ParametersNameTypeDes

### ConfigureFrequencyArfcn(string, RFmxGsmMXLinkDirection, RFmxGsmMXBand, int)

Configures the center frequency from the absolute RF channel number (ARFCN), band, and the link direction.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigureFrequencyArfcn(string selectorString, RFmxGsmMXLinkDirection linkDirection, RFmxGsmMXBand band, int arfcn)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| linkDirection | RFmxGsmMXLinkDirection | Specifies the source of the signal to be measured. |
| band | RFmxGsmMXBand | Specifies the band of operation. |
| arfcn | int | Specifies the ARFCN. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configureiqpoweredgetrigger__string-string-rfmxgsmmxiqpoweredgetriggerslope-double-double-rfmxgsmmxtriggerminimumquiettimemode-double-rfmxgsmmxi...d17e797.html language=enus -->
## TOPIC 00019: ConfigureIQPowerEdgeTrigger(string, string, RFmxGsmMXIQPowerEdgeTriggerSlope, double, double, RFmxGsmMXTriggerMinimumQuietTimeMode, double, RFmxGsmMXIQPowerEdgeTriggerLevelType, bool)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configureiqpoweredgetrigger__string-string-rfmxgsmmxiqpoweredgetriggerslope-double-double-rfmxgsmmxtriggerminimumquiettimemode-double-rfmxgsmmxi...d17e797.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configureiqpoweredgetrigger__string-string-rfmxgsmmxiqpoweredgetriggerslope-double-double-rfmxgsmmxtriggerminimumquiettimemode-double-rfmxgsmmxi...d17e797.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int ConfigureIQPowerEdgeTrigger(string selectorString, string iqPowerEdgeTriggerSource, RFmxGsmMXIQP

### ConfigureIQPowerEdgeTrigger(string, string, RFmxGsmMXIQPowerEdgeTriggerSlope, double, double, RFmxGsmMXTriggerMinimumQuietTimeMode, double, RFmxGsmMXIQPowerEdgeTriggerLevelType, bool)

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigureIQPowerEdgeTrigger(string selectorString, string iqPowerEdgeTriggerSource, RFmxGsmMXIQPowerEdgeTriggerSlope iqPowerEdgeTriggerSlope, double iqPowerEdgeTriggerLevel, double triggerDelay, RFmxGsmMXTriggerMinimumQuietTimeMode minimumQuietTimeMode, double minimumQuietTimeDuration, RFmxGsmMXIQPowerEdgeTriggerLevelType iqPowerEdgeTriggerLevelType, bool enableTrigger)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| iqPowerEdgeTriggerSource | string | Specifies the channel from which the device monitors the trigger. |
| iqPowerEdgeTriggerSlope | RFmxGsmMXIQPowerEdgeTriggerSlope | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. |
| iqPowerEdgeTriggerLevel | double | Specifies the power level at which the device triggers, depending on the value of the iqPowerEdgeTriggerSlope parameter. The value is expressed in dB when the iqPowerEdgeTriggerLevelType parameter is set to Relative, or in dBm when it is set to Absolute. |
| triggerDelay | double | Specifies the trigger delay time. This value is expressed in seconds. |
| minimumQuietTimeMode | RFmxGsmMXTriggerMinimumQuietTimeMode | Specifies whether the measurement computes the minimum quiet time used for triggering. |
| minimumQuietTimeDuration | double | Specifies the duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set SetIQPowerEdgeTriggerSlope(string, RFmxGsmMXIQPowerEdgeTriggerSlope) to Rising, the signal is quiet when it is below the trigger level. |
| iqPowerEdgeTriggerLevelType | RFmxGsmMXIQPowerEdgeTriggerLevelType | Specifies whether the IQPowerEdgeLevel is set to Relative or Absolute. The value is expressed in dB when this parameter is set to Relative. The value is expressed in dBm when this parameter is set to Absolute. |
| enableTrigger | bool | Specifies whether the trigger is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configurelinkdirection__string-rfmxgsmmxlinkdirection.html language=enus -->
## TOPIC 00020: ConfigureLinkDirection(string, RFmxGsmMXLinkDirection)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configurelinkdirection__string-rfmxgsmmxlinkdirection.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configurelinkdirection__string-rfmxgsmmxlinkdirection.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the source of the signal to be measured.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int ConfigureLinkDirection(string selectorString, RFmxGsmMXLinkDirection linkDirection)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when c

### ConfigureLinkDirection(string, RFmxGsmMXLinkDirection)

Configures the source of the signal to be measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigureLinkDirection(string selectorString, RFmxGsmMXLinkDirection linkDirection)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| linkDirection | RFmxGsmMXLinkDirection | Specifies the source of the signal to be measured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configurenumberoftimeslots__string-int.html language=enus -->
## TOPIC 00021: ConfigureNumberOfTimeslots(string, int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configurenumberoftimeslots__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configurenumberoftimeslots__string-int.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of timeslots to be measured.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int ConfigureNumberOfTimeslots(string selectorString, int numberOfTimeSlots)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when creating the

### ConfigureNumberOfTimeslots(string, int)

Configures the number of timeslots to be measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigureNumberOfTimeslots(string selectorString, int numberOfTimeSlots)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| numberOfTimeSlots | int | Specifies the number of time slots to be measured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configurepowercontrollevel__string-int.html language=enus -->
## TOPIC 00022: ConfigurePowerControlLevel(string, int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configurepowercontrollevel__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configurepowercontrollevel__string-int.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the power control level corresponding to the transmitted power. Use "slot(n)" as the selector string to configure this method.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int ConfigurePowerControlLevel(string selectorString, int powerControlLevel)ParametersNameTypeDescriptionsele

### ConfigurePowerControlLevel(string, int)

Configures the power control level corresponding to the transmitted power. 
 Use "slot(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigurePowerControlLevel(string selectorString, int powerControlLevel)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of slot number. Example: "slot0" "slot::all" You can use the BuildSlotString(string, int) method to build the selector string. |
| powerControlLevel | int | Specifies the power control level corresponding to the transmitted power, as defined in section 4.1 of the 3GPP TS 45.005 v8.0.0 specifications. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configurereferencelevel__string-double.html language=enus -->
## TOPIC 00023: ConfigureReferenceLevel(string, double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configurereferencelevel__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configurereferencelevel__string-double.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference level, which represents the maximum expected power of an RF input signal.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int ConfigureReferenceLevel(string selectorString, double referenceLevel)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The

### ConfigureReferenceLevel(string, double)

Configures the reference level, which represents the maximum expected power of an RF input signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigureReferenceLevel(string selectorString, double referenceLevel)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| referenceLevel | double | Specifies the reference level, which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configurerf__string-double-double-double.html language=enus -->
## TOPIC 00024: ConfigureRF(string, double, double, double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configurerf__string-double-double-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configurerf__string-double-double-double.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RF methods of the signal specified by the selector string.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int ConfigureRF(string selectorString, double centerFrequency, double referenceLevel, double externalAttenuation)ParametersNameTypeDescriptionselectorStringstringPass an emp

### ConfigureRF(string, double, double, double)

Configures the RF methods of the signal specified by the selector string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigureRF(string selectorString, double centerFrequency, double referenceLevel, double externalAttenuation)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| centerFrequency | double | Specifies the expected center frequency of the RF signal to acquire. This value is expressed in Hz. The signal analyzer tunes to this frequency. |
| referenceLevel | double | Specifies the reference level, which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
| externalAttenuation | double | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the External Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configuresignaltype__string-rfmxgsmmxmodulationtype-rfmxgsmmxbursttype-rfmxgsmmxhbfilterwidth.html language=enus -->
## TOPIC 00025: ConfigureSignalType(string, RFmxGsmMXModulationType, RFmxGsmMXBurstType, RFmxGsmMXHBFilterWidth)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configuresignaltype__string-rfmxgsmmxmodulationtype-rfmxgsmmxbursttype-rfmxgsmmxhbfilterwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configuresignaltype__string-rfmxgsmmxmodulationtype-rfmxgsmmxbursttype-rfmxgsmmxhbfilterwidth.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the signal type. Use "slot(n)" as the selector string to configure this method.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int ConfigureSignalType(string selectorString, RFmxGsmMXModulationType modulationType, RFmxGsmMXBurstType burstType, RFmxGsmMXHBFilterWidth hbFilterWidth)Pa

### ConfigureSignalType(string, RFmxGsmMXModulationType, RFmxGsmMXBurstType, RFmxGsmMXHBFilterWidth)

Configures the signal type. 
 Use "slot(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigureSignalType(string selectorString, RFmxGsmMXModulationType modulationType, RFmxGsmMXBurstType burstType, RFmxGsmMXHBFilterWidth hbFilterWidth)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of slot number. Example: "slot0" "slot::all" You can use the BuildSlotString(string, int) method to build the selector string. |
| modulationType | RFmxGsmMXModulationType | Specifies the modulation type of the signal. |
| burstType | RFmxGsmMXBurstType | Specifies the burst type. |
| hbFilterWidth | RFmxGsmMXHBFilterWidth | Specifies the filter width when you set the burstType parameter to HB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configuresoftwareedgetrigger__string-double-bool.html language=enus -->
## TOPIC 00026: ConfigureSoftwareEdgeTrigger(string, double, bool)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configuresoftwareedgetrigger__string-double-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configuresoftwareedgetrigger__string-double-bool.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a software trigger and then marks a reference point within the record.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int ConfigureSoftwareEdgeTrigger(string selectorString, double triggerDelay, bool enableTrigger)ParametersNameTypeDescriptionselectorStringstr

### ConfigureSoftwareEdgeTrigger(string, double, bool)

Configures the device to wait for a software trigger and then marks a reference point within the record.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigureSoftwareEdgeTrigger(string selectorString, double triggerDelay, bool enableTrigger)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| triggerDelay | double | Specifies the trigger delay time, in seconds. |
| enableTrigger | bool | Specifies whether to enable the trigger. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configuretsc__string-rfmxgsmmxtsc.html language=enus -->
## TOPIC 00027: ConfigureTsc(string, RFmxGsmMXTsc)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configuretsc__string-rfmxgsmmxtsc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-configuretsc__string-rfmxgsmmxtsc.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the training sequence code (TSC) in the burst. Use "slot(n)" as the selector string to configure this method.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int ConfigureTsc(string selectorString, RFmxGsmMXTsc tsc)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector

### ConfigureTsc(string, RFmxGsmMXTsc)

Configures the training sequence code (TSC) in the burst. 
 Use "slot(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigureTsc(string selectorString, RFmxGsmMXTsc tsc)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of slot number. Example: "slot0" "slot::all" You can use the BuildSlotString(string, int) method to build the selector string. |
| tsc | RFmxGsmMXTsc | Specifies the training sequence code in the burst. For access burst TSC0, TSC1, and TSC2 are applicable. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-deletesignalconfiguration.html language=enus -->
## TOPIC 00028: DeleteSignalConfiguration()

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-deletesignalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-deletesignalconfiguration.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes an instance of a signal.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int DeleteSignalConfiguration()ReturnsReturns the status code of this method. The status code either indicates success or describes a warning condition.

### DeleteSignalConfiguration()

Deletes an instance of a signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int DeleteSignalConfiguration()

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-disabletrigger__string.html language=enus -->
## TOPIC 00029: DisableTrigger(string)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-disabletrigger__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-disabletrigger__string.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to not wait for a trigger to mark a reference point within a record. This method defines the signal triggering as immediate.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int DisableTrigger(string selectorString)ParametersNameTypeDescriptionselectorStringstringPass an em

### DisableTrigger(string)

Configures the device to not wait for a trigger to mark a reference point within a record. This method defines the signal triggering as immediate.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int DisableTrigger(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-dispose.html language=enus -->
## TOPIC 00030: Dispose()

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-dispose.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-dispose.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes the signal configuration if it is not the default signal configuration and clears any trace of the current signal configuration, if any. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic void Dispose()RemarksYou can call this method safely more than once, even if the signal is already de

### Dispose()

Deletes the signal configuration if it is not the default signal configuration and clears any trace of the current signal configuration, if any.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public void Dispose()

#### Remarks

You can call this method safely more than once, even if the signal is already deleted.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getallnamedresultnames__string-out-out.html language=enus -->
## TOPIC 00031: GetAllNamedResultNames(string, out string[], out bool)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getallnamedresultnames__string-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getallnamedresultnames__string-out-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns all the named result names of the current signal instance. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetAllNamedResultNames(string selectorString, out string[] resultNames, out bool defaultResultExists)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The

### GetAllNamedResultNames(string, out string[], out bool)

Returns all the named result names of the current signal instance.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetAllNamedResultNames(string selectorString, out string[] resultNames, out bool defaultResultExists)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| resultNames | out string[] | Returns an array of result names. |
| defaultResultExists | out bool | Indicates whether the default result exists. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getattributebool__string-int-out.html language=enus -->
## TOPIC 00032: GetAttributeBool(string, int, out bool)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getattributebool__string-int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getattributebool__string-int-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of a Bool attribute. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetAttributeBool(string selectorString, int attributeIdentifier, out bool value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being read. Refer to the Usin

### GetAttributeBool(string, int, out bool)

Gets the value of a Bool attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetAttributeBool(string selectorString, int attributeIdentifier, out bool value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the RFmx GSM Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | out bool | Upon return, contains a value of the specified attribute ID. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getattributedouble__string-int-out.html language=enus -->
## TOPIC 00033: GetAttributeDouble(string, int, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getattributedouble__string-int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getattributedouble__string-int-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of a Double attribute. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetAttributeDouble(string selectorString, int attributeIdentifier, out double value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being read. Refer to th

### GetAttributeDouble(string, int, out double)

Gets the value of a Double attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetAttributeDouble(string selectorString, int attributeIdentifier, out double value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the RFmx GSM Help for more information about configuring the selector string. |
| attributeIdentifier | int | Passes the ID of an attribute. |
| value | out double | Upon return, contains a value of the specified attribute ID. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getattributeint__string-int-out.html language=enus -->
## TOPIC 00034: GetAttributeInt(string, int, out int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getattributeint__string-int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getattributeint__string-int-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of an RFmx 32-bit integer (int32) attribute. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetAttributeInt(string selectorString, int attributeIdentifier, out int value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being r

### GetAttributeInt(string, int, out int)

Gets the value of an RFmx 32-bit integer (int32) attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetAttributeInt(string selectorString, int attributeIdentifier, out int value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the RFmx GSM Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | out int | Upon return, contains a value of the specified attribute ID. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getattributestring__string-int-out.html language=enus -->
## TOPIC 00035: GetAttributeString(string, int, out string)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getattributestring__string-int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getattributestring__string-int-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of a of an RFmx string. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetAttributeString(string selectorString, int attributeIdentifier, out string value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being read. Refer to t

### GetAttributeString(string, int, out string)

Gets the value of a of an RFmx string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetAttributeString(string selectorString, int attributeIdentifier, out string value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the RFmx GSM Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | out string | Upon return, contains a value of the specified attribute ID. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getautolevelinitialreferencelevel__string-out.html language=enus -->
## TOPIC 00036: GetAutoLevelInitialReferenceLevel(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getautolevelinitialreferencelevel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getautolevelinitialreferencelevel__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the initial reference level the AutoLevel(string, double, out double) function uses to estimate the peak power of the input signal. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetAutoLevelInitialReferenceLevel(string selectorString, out double value

### GetAutoLevelInitialReferenceLevel(string, out double)

Gets the initial reference level the [AutoLevel(string, double, out double)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-autolevel__string-double-out.html) function uses to estimate the peak power of the input signal. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetAutoLevelInitialReferenceLevel(string selectorString, out double value)

#### Remarks

This method gets the value of [AutoLevelInitialReferenceLevel](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 30.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the initial reference level the AutoLevel(string, double, out double) function uses to estimate the peak power of the input signal. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getautotscdetectionenabled__string-out.html language=enus -->
## TOPIC 00037: GetAutoTscDetectionEnabled(string, out RFmxGsmMXAutoTscDetectionEnabled)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getautotscdetectionenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getautotscdetectionenabled__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement automatically detects the training sequence code (TSC). SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetAutoTscDetectionEnabled(string selectorString, out RFmxGsmMXAutoTscDetectionEnabled value)RemarksThis method gets the value of AutoTscDetectionEnabled att

### GetAutoTscDetectionEnabled(string, out RFmxGsmMXAutoTscDetectionEnabled)

Gets whether the measurement automatically detects the training sequence code (TSC).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetAutoTscDetectionEnabled(string selectorString, out RFmxGsmMXAutoTscDetectionEnabled value)

#### Remarks

This method gets the value of [AutoTscDetectionEnabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-gsmmx-rfmxgsmmxautotscdetectionenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxGsmMXAutoTscDetectionEnabled | Upon return, contains whether the measurement automatically detects the training sequence code (TSC). |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getband__string-out.html language=enus -->
## TOPIC 00038: GetBand(string, out RFmxGsmMXBand)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getband__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getband__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the operation band. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetBand(string selectorString, out RFmxGsmMXBand value)RemarksThis method gets the value of Band attribute.The default value is Pgsm.ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal na

### GetBand(string, out RFmxGsmMXBand)

Gets the operation band.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetBand(string selectorString, out RFmxGsmMXBand value)

#### Remarks

This method gets the value of [Band](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Pgsm](nationalinstruments-rfmx-gsmmx-rfmxgsmmxband.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxGsmMXBand | Upon return, contains the operation band. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getburstsynchronizationtype__string-out.html language=enus -->
## TOPIC 00039: GetBurstSynchronizationType(string, out RFmxGsmMXBurstSynchronizationType)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getburstsynchronizationtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getburstsynchronizationtype__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the method used to synchronize the burst. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetBurstSynchronizationType(string selectorString, out RFmxGsmMXBurstSynchronizationType value)RemarksThis method gets the value of BurstSynchronizationType attribute.The default value is Tsc.Par

### GetBurstSynchronizationType(string, out RFmxGsmMXBurstSynchronizationType)

Gets the method used to synchronize the burst.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetBurstSynchronizationType(string selectorString, out RFmxGsmMXBurstSynchronizationType value)

#### Remarks

This method gets the value of [BurstSynchronizationType](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Tsc](nationalinstruments-rfmx-gsmmx-rfmxgsmmxburstsynchronizationtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxGsmMXBurstSynchronizationType | Upon return, contains the method used to synchronize the burst. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getbursttype__string-out.html language=enus -->
## TOPIC 00040: GetBurstType(string, out RFmxGsmMXBurstType)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getbursttype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getbursttype__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the burst type. Use "slot(n)" as the selector string to configure or read this method. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetBurstType(string selectorString, out RFmxGsmMXBurstType value)RemarksThis method gets the value of BurstType attribute.The default value is NB.Para

### GetBurstType(string, out RFmxGsmMXBurstType)

Gets the burst type. Use "slot(n)" as the selector string to configure or read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetBurstType(string selectorString, out RFmxGsmMXBurstType value)

#### Remarks

This method gets the value of [BurstType](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [NB](nationalinstruments-rfmx-gsmmx-rfmxgsmmxbursttype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the slot number. Example: "slot0". You can use the BuildSlotString(string, int) method to build the selector string. |
| value | out RFmxGsmMXBurstType | Upon return, contains the burst type. Use "slot(n)" as the selector string to configure or read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getcenterfrequency__string-out.html language=enus -->
## TOPIC 00041: GetCenterFrequency(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getcenterfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getcenterfrequency__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetCenterFrequency(string selectorString, out double value)RemarksThis method gets the value of CenterF

### GetCenterFrequency(string, out double)

Gets the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetCenterFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [CenterFrequency](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 890.2 MHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getdigitaledgetriggeredge__string-out.html language=enus -->
## TOPIC 00042: GetDigitalEdgeTriggerEdge(string, out RFmxGsmMXDigitalEdgeTriggerEdge)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getdigitaledgetriggeredge__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getdigitaledgetriggeredge__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to DigitalEdge. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetDigitalEdgeTriggerEdge(string selectorString, out RFmxGsmMXDigitalEdgeTriggerEdge value)Rem

### GetDigitalEdgeTriggerEdge(string, out RFmxGsmMXDigitalEdgeTriggerEdge)

Gets the active edge for the trigger. This method is used only when you set the [SetTriggerType(string, RFmxGsmMXTriggerType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggertype__string-rfmxgsmmxtriggertype.html) method to [DigitalEdge](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetDigitalEdgeTriggerEdge(string selectorString, out RFmxGsmMXDigitalEdgeTriggerEdge value)

#### Remarks

This method gets the value of [DigitalEdgeTriggerEdge](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Rising](nationalinstruments-rfmx-gsmmx-rfmxgsmmxdigitaledgetriggeredge.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxGsmMXDigitalEdgeTriggerEdge | Upon return, contains the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to DigitalEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getdigitaledgetriggersource__string-out.html language=enus -->
## TOPIC 00043: GetDigitalEdgeTriggerSource(string, out string)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getdigitaledgetriggersource__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getdigitaledgetriggersource__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to DigitalEdge. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetDigitalEdgeTriggerSource(string selectorString, out string value)RemarksTh

### GetDigitalEdgeTriggerSource(string, out string)

Gets the source terminal for the digital edge trigger. This method is used only when you set the [SetTriggerType(string, RFmxGsmMXTriggerType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggertype__string-rfmxgsmmxtriggertype.html) method to [DigitalEdge](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetDigitalEdgeTriggerSource(string selectorString, out string value)

#### Remarks

This method gets the value of [DigitalEdgeTriggerSource](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is RFMXGSM_VAL_PFI0_STR.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out string | Upon return, contains the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to DigitalEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-geterror__out-out.html language=enus -->
## TOPIC 00044: GetError(out int, out string)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-geterror__out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-geterror__out-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the latest error code and description. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetError(out int errorCode, out string errorDescription)ParametersNameTypeDescriptionerrorCodeout intUpon return, contains the latest error code.errorDescriptionout stringUpon return, contains the l

### GetError(out int, out string)

Gets the latest error code and description.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetError(out int errorCode, out string errorDescription)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| errorCode | out int | Upon return, contains the latest error code. |
| errorDescription | out string | Upon return, contains the latest error description. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-geterrorstring__int-out.html language=enus -->
## TOPIC 00045: GetErrorString(int, out string)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-geterrorstring__int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-geterrorstring__int-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the status code returned by an RFmxGSM function into a string. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetErrorString(int errorCode, out string errorDescription)ParametersNameTypeDescriptionerrorCodeintSpecifies an error or warning code.errorDescriptionout stringUpon retur

### GetErrorString(int, out string)

Converts the status code returned by an RFmxGSM function into a string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetErrorString(int errorCode, out string errorDescription)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| errorCode | int | Specifies an error or warning code. |
| errorDescription | out string | Upon return, contains the error description. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getexternalattenuation__string-out.html language=enus -->
## TOPIC 00046: GetExternalAttenuation(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getexternalattenuation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getexternalattenuation__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. SyntaxNamespace: Na

### GetExternalAttenuation(string, out double)

Gets the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the *NI RF Vector Signal Analyzers Help*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetExternalAttenuation(string selectorString, out double value)

#### Remarks

This method gets the value of [ExternalAttenuation](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-gethbfilterwidth__string-out.html language=enus -->
## TOPIC 00047: GetHBFilterWidth(string, out RFmxGsmMXHBFilterWidth)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-gethbfilterwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-gethbfilterwidth__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the filter width when you set the SetBurstType(string, RFmxGsmMXBurstType) method to HB. Use "slot(n)" as the selector string to configure or read this method. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetHBFilterWidth(string selectorString, out RFmxGsmMXHBFilterWidth value)Rema

### GetHBFilterWidth(string, out RFmxGsmMXHBFilterWidth)

Gets the filter width when you set the [SetBurstType(string, RFmxGsmMXBurstType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setbursttype__string-rfmxgsmmxbursttype.html) method to [HB](nationalinstruments-rfmx-gsmmx-rfmxgsmmxbursttype.html). Use "slot(n)" as the selector string to configure or read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetHBFilterWidth(string selectorString, out RFmxGsmMXHBFilterWidth value)

#### Remarks

This method gets the value of [HBFilterWidth](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Narrow](nationalinstruments-rfmx-gsmmx-rfmxgsmmxhbfilterwidth.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the slot number. Example: "slot0". You can use the BuildSlotString(string, int) method to build the selector string. |
| value | out RFmxGsmMXHBFilterWidth | Upon return, contains the filter width when you set the SetBurstType(string, RFmxGsmMXBurstType) method to HB. Use "slot(n)" as the selector string to configure or read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getiqpoweredgetriggerlevel__string-out.html language=enus -->
## TOPIC 00048: GetIQPowerEdgeTriggerLevel(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getiqpoweredgetriggerlevel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getiqpoweredgetriggerlevel__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power level at which the device triggers. This value is expressed in dB when you set the SetIQPowerEdgeTriggerLevelType(string, RFmxGsmMXIQPowerEdgeTriggerLevelType) method to Relative and in dBm when you set the IQ Power Edge Level Type method to Absolute. The device asserts the trigger wh

### GetIQPowerEdgeTriggerLevel(string, out double)

Gets the power level at which the device triggers. This value is expressed in dB when you set the [SetIQPowerEdgeTriggerLevelType(string, RFmxGsmMXIQPowerEdgeTriggerLevelType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setiqpoweredgetriggerleveltype__string-rfmxgsmmxiqpoweredgetriggerleveltype.html) method to [Relative](nationalinstruments-rfmx-gsmmx-rfmxgsmmxiqpoweredgetriggerleveltype.html) and in dBm when you set the IQ Power Edge Level Type method to [Absolute](nationalinstruments-rfmx-gsmmx-rfmxgsmmxiqpoweredgetriggerleveltype.html). The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the [SetTriggerType(string, RFmxGsmMXTriggerType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggertype__string-rfmxgsmmxtriggertype.html) method to [IQPowerEdge](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetIQPowerEdgeTriggerLevel(string selectorString, out double value)

#### Remarks

This method gets the value of [IQPowerEdgeTriggerLevel](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is -20 dB.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the power level at which the device triggers. This value is expressed in dB when you set the SetIQPowerEdgeTriggerLevelType(string, RFmxGsmMXIQPowerEdgeTriggerLevelType) method to Relative and in dBm when you set the IQ Power Edge Level Type method to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getiqpoweredgetriggerleveltype__string-out.html language=enus -->
## TOPIC 00049: GetIQPowerEdgeTriggerLevelType(string, out RFmxGsmMXIQPowerEdgeTriggerLevelType)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getiqpoweredgetriggerleveltype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getiqpoweredgetriggerleveltype__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetIQPowerEdgeTriggerLevelType

### GetIQPowerEdgeTriggerLevelType(string, out RFmxGsmMXIQPowerEdgeTriggerLevelType)

Gets the reference for the [SetIQPowerEdgeTriggerLevel(string, double)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setiqpoweredgetriggerlevel__string-double.html) method. The IQ Power Edge Level Type method is used only when you set the [SetTriggerType(string, RFmxGsmMXTriggerType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggertype__string-rfmxgsmmxtriggertype.html) method to [IQPowerEdge](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetIQPowerEdgeTriggerLevelType(string selectorString, out RFmxGsmMXIQPowerEdgeTriggerLevelType value)

#### Remarks

This method gets the value of [IQPowerEdgeTriggerLevelType](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Relative](nationalinstruments-rfmx-gsmmx-rfmxgsmmxiqpoweredgetriggerleveltype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxGsmMXIQPowerEdgeTriggerLevelType | Upon return, contains the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getiqpoweredgetriggerslope__string-out.html language=enus -->
## TOPIC 00050: GetIQPowerEdgeTriggerSlope(string, out RFmxGsmMXIQPowerEdgeTriggerSlope)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getiqpoweredgetriggerslope__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getiqpoweredgetriggerslope__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the SetIQPowerEdgeTriggerLevel(string, double) method with the slope you specify. This method is used only whe

### GetIQPowerEdgeTriggerSlope(string, out RFmxGsmMXIQPowerEdgeTriggerSlope)

Gets whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the [SetIQPowerEdgeTriggerLevel(string, double)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setiqpoweredgetriggerlevel__string-double.html) method with the slope you specify. This method is used only when you set the [SetTriggerType(string, RFmxGsmMXTriggerType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggertype__string-rfmxgsmmxtriggertype.html) method to [IQPowerEdge](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetIQPowerEdgeTriggerSlope(string selectorString, out RFmxGsmMXIQPowerEdgeTriggerSlope value)

#### Remarks

This method gets the value of [IQPowerEdgeTriggerSlope](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Rising](nationalinstruments-rfmx-gsmmx-rfmxgsmmxiqpoweredgetriggerslope.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxGsmMXIQPowerEdgeTriggerSlope | Upon return, contains whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the SetIQPowerEdgeTriggerLevel(string, double) method with the slope you specify. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getiqpoweredgetriggersource__string-out.html language=enus -->
## TOPIC 00051: GetIQPowerEdgeTriggerSource(string, out string)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getiqpoweredgetriggersource__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getiqpoweredgetriggersource__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetIQPowerEdgeTriggerSource(string selectorString, out string value)Rem

### GetIQPowerEdgeTriggerSource(string, out string)

Gets the channel from which the device monitors the trigger. This method is used only when you set the [SetTriggerType(string, RFmxGsmMXTriggerType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggertype__string-rfmxgsmmxtriggertype.html) method to [IQPowerEdge](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetIQPowerEdgeTriggerSource(string selectorString, out string value)

#### Remarks

This method gets the value of [IQPowerEdgeTriggerSource](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out string | Upon return, contains the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getlimitedconfigurationchange__string-out.html language=enus -->
## TOPIC 00052: GetLimitedConfigurationChange(string, out RFmxGsmMXLimitedConfigurationChange)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getlimitedconfigurationchange__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getlimitedconfigurationchange__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the set of properties that are considered by RFmx in the locked signal configuration state. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetLimitedConfigurationChange(string selectorString, out RFmxGsmMXLimitedConfigurationChange value)RemarksIf your test system performs the same m

### GetLimitedConfigurationChange(string, out RFmxGsmMXLimitedConfigurationChange)

Gets the set of properties that are considered by RFmx in the locked signal configuration state.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetLimitedConfigurationChange(string selectorString, out RFmxGsmMXLimitedConfigurationChange value)

#### Remarks

If your test system performs the same measurement at multiple frequencies and/or power levels repeatedly, enabling this method can help achieve faster measurements. When you set this method to a value other than [Disabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxlimitedconfigurationchange.html), the RFmx driver will use an optimized code path and skip some checks. Because RFmx skips some checks when you use this property, you need to be aware of the limitations of this feature, which are listed in the Limitations of the Limited Configuration Change Property topic. You can also use this method to lock a specific instrument configuration for a signal so that every time that you initiate the signal, RFmx applies the RFmxInstr properties from a locked configuration. NI recommends you use this method in conjunction with named signal configurations. Create named signal configurations for each measurement configuration in your test program and set this method to a value other than [Disabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxlimitedconfigurationchange.html) for one or more of the named signal configurations. This allows RFmx to precompute the acquisition settings for your measurement configurations and re-use the precomputed settings each time you initiate the measurement. You do not need to use this method if you create named signals for all the measurement configurations in your test program during test sequence initialization and do not change any RFInstr or personality properties while testing each device under test. RFmx automatically optimizes that use case. Specify the named signal configuration you are setting this property in the selector string input. This method gets the value of [LimitedConfigurationChange](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Disabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxlimitedconfigurationchange.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxGsmMXLimitedConfigurationChange | Upon return, contains the set of properties that are considered by RFmx in the locked signal configuration state. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getlinkdirection__string-out.html language=enus -->
## TOPIC 00053: GetLinkDirection(string, out RFmxGsmMXLinkDirection)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getlinkdirection__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getlinkdirection__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source of the signal to be measured. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetLinkDirection(string selectorString, out RFmxGsmMXLinkDirection value)RemarksThis method gets the value of LinkDirection attribute.The default value is Uplink.ParametersNameTypeDescriptionselec

### GetLinkDirection(string, out RFmxGsmMXLinkDirection)

Gets the source of the signal to be measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetLinkDirection(string selectorString, out RFmxGsmMXLinkDirection value)

#### Remarks

This method gets the value of [LinkDirection](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Uplink](nationalinstruments-rfmx-gsmmx-rfmxgsmmxlinkdirection.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxGsmMXLinkDirection | Upon return, contains the source of the signal to be measured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getmodulationtype__string-out.html language=enus -->
## TOPIC 00054: GetModulationType(string, out RFmxGsmMXModulationType)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getmodulationtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getmodulationtype__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the modulation scheme used for the signal. Use "slot(n)" as the selector string to configure or read this method. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetModulationType(string selectorString, out RFmxGsmMXModulationType value)RemarksThis method gets the value of ModulationT

### GetModulationType(string, out RFmxGsmMXModulationType)

Gets the modulation scheme used for the signal. Use "slot(n)" as the selector string to configure or read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetModulationType(string selectorString, out RFmxGsmMXModulationType value)

#### Remarks

This method gets the value of [ModulationType](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [ModulationType8Psk](nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodulationtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the slot number. Example: "slot0". You can use the BuildSlotString(string, int) method to build the selector string. |
| value | out RFmxGsmMXModulationType | Upon return, contains the modulation scheme used for the signal. Use "slot(n)" as the selector string to configure or read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getnumberoftimeslots__string-out.html language=enus -->
## TOPIC 00055: GetNumberOfTimeslots(string, out int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getnumberoftimeslots__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getnumberoftimeslots__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of time slots to be measured. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetNumberOfTimeslots(string selectorString, out int value)RemarksThis method gets the value of NumberOfTimeslots attribute.The default value is 1.ParametersNameTypeDescriptionselectorStringstringP

### GetNumberOfTimeslots(string, out int)

Gets the number of time slots to be measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetNumberOfTimeslots(string selectorString, out int value)

#### Remarks

This method gets the value of [NumberOfTimeslots](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of time slots to be measured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getpowercontrollevel__string-out.html language=enus -->
## TOPIC 00056: GetPowerControlLevel(string, out int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getpowercontrollevel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getpowercontrollevel__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power control level corresponding to the transmitted power, as defined in section 4.1 of the 3GPP TS 45.005 v8.0.0 specifications. Use "slot(n)" as the selector string to configure or read this method. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetPowerControlLevel(string sel

### GetPowerControlLevel(string, out int)

Gets the power control level corresponding to the transmitted power, as defined in section 4.1 of the *3GPP TS 45.005 v8.0.0 specifications*. Use "slot(n)" as the selector string to configure or read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetPowerControlLevel(string selectorString, out int value)

#### Remarks

This method gets the value of [PowerControlLevel](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 0. Valid values are 0 to 40, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the slot number. Example: "slot0". You can use the BuildSlotString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the power control level corresponding to the transmitted power, as defined in section 4.1 of the 3GPP TS 45.005 v8.0.0 specifications. Use "slot(n)" as the selector string to configure or read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getreferencelevel__string-out.html language=enus -->
## TOPIC 00057: GetReferenceLevel(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getreferencelevel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getreferencelevel__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and V[pk-pk] for baseband devices. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetReferenceLevel(string selectorString, out double value)RemarksThis

### GetReferenceLevel(string, out double)

Gets the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and V<sub>pk-pk</sub> for baseband devices.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetReferenceLevel(string selectorString, out double value)

#### Remarks

This method gets the value of [ReferenceLevel](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getreferencelevelheadroom__string-out.html language=enus -->
## TOPIC 00058: GetReferenceLevelHeadroom(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getreferencelevelheadroom__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getreferencelevelheadroom__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the margin RFmx adds to the Reference Level method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input signal

### GetReferenceLevelHeadroom(string, out double)

Gets the margin RFmx adds to the Reference Level method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input signal remains within the reference level plus the reference level headroom. If you know the input power of the signal precisely or previously included the margin in the reference level, you could improve the signal-to-noise ratio by reducing the reference level headroom. **Default values** 
 PXIe-5668: 6 dB 
 PXIe-5830/5831/5832/5841/5842/5860: 1 dB 
 PXIe-5840: 0 dB **Supported devices:**PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetReferenceLevelHeadroom(string selectorString, out double value)

#### Remarks

This method gets the value of [ReferenceLevelHeadroom](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the margin RFmx adds to the Reference Level method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getresultfetchtimeout__string-out.html language=enus -->
## TOPIC 00059: GetResultFetchTimeout(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getresultfetchtimeout__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getresultfetchtimeout__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the time to wait before results are available. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx driver waits until the measurement is complete. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpub

### GetResultFetchTimeout(string, out double)

Gets the time to wait before results are available. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx driver waits until the measurement is complete.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetResultFetchTimeout(string selectorString, out double value)

#### Remarks

This method gets the value of [ResultFetchTimeout](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the time to wait before results are available. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx driver waits until the measurement is complete. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getselectedports__string-out.html language=enus -->
## TOPIC 00060: GetSelectedPorts(string, out string)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getselectedports__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getselectedports__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the instrument port to be configured to acquire a signal. Valid values PXIe-5820/5840: "" (empty string) PXIe-5830: if0, if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Default valu

### GetSelectedPorts(string, out string)

Gets the instrument port to be configured to acquire a signal. **Valid values** 
 PXIe-5820/5840: "" (empty string) 
 PXIe-5830: if0, if1 
 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel **Default values** 
 PXIe-5820/5840: "" (empty string) 
 PXIe-5830/5831/5832: if1 
 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel **Supported devices**: PXIe-5820/5830/5831/5832/5840 
</x></x>

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetSelectedPorts(string selectorString, out string value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out string | Specifies the instrument port to be used by the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getsignalstructure__string-out.html language=enus -->
## TOPIC 00061: GetSignalStructure(string, out RFmxGsmMXSignalStructure)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getsignalstructure__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getsignalstructure__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the signal is bursted or continuous. For bursted signal and continuous signals, set the SetTriggerType(string, RFmxGsmMXTriggerType) to IQPowerEdge and None, respectively. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetSignalStructure(string selectorString, out RFmxGsmMXSi

### GetSignalStructure(string, out RFmxGsmMXSignalStructure)

Gets whether the signal is bursted or continuous. For bursted signal and continuous signals, set the [SetTriggerType(string, RFmxGsmMXTriggerType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggertype__string-rfmxgsmmxtriggertype.html) to [IQPowerEdge](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggertype.html) and [None](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggertype.html), respectively.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetSignalStructure(string selectorString, out RFmxGsmMXSignalStructure value)

#### Remarks

This method gets the value of [SignalStructure](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Bursted](nationalinstruments-rfmx-gsmmx-rfmxgsmmxsignalstructure.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxGsmMXSignalStructure | Upon return, contains whether the signal is bursted or continuous. For bursted signal and continuous signals, set the SetTriggerType(string, RFmxGsmMXTriggerType) to IQPowerEdge and None, respectively. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-gettimingadvance__string-out.html language=enus -->
## TOPIC 00062: GetTimingAdvance(string, out int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-gettimingadvance__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-gettimingadvance__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the timing advance value as specified in the 3GPP TS 45.010 specification for GSM access burst. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetTimingAdvance(string selectorString, out int value)RemarksThis method gets the value of TimingAdvance attribute.The default value is

### GetTimingAdvance(string, out int)

Specifies the timing advance value as specified in the 3GPP TS 45.010 specification for GSM access burst.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetTimingAdvance(string selectorString, out int value)

#### Remarks

This method gets the value of [TimingAdvance](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the timing advance value as specified in the 3GPP TS 45.010 specification for GSM access burst. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-gettriggerdelay__string-out.html language=enus -->
## TOPIC 00063: GetTriggerDelay(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-gettriggerdelay__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-gettriggerdelay__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetTriggerDelay(string selectorSt

### GetTriggerDelay(string, out double)

Gets the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetTriggerDelay(string selectorString, out double value)

#### Remarks

This method gets the value of [TriggerDelay](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-gettriggerminimumquiettimeduration__string-out.html language=enus -->
## TOPIC 00064: GetTriggerMinimumQuietTimeDuration(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-gettriggerminimumquiettimeduration__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-gettriggerminimumquiettimeduration__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the SetIQPowerEdgeTriggerSlope(string, RFmxGsmMXIQPowerEdgeTriggerSlope) method to Rising, the signal is quiet below the trigger level.

### GetTriggerMinimumQuietTimeDuration(string, out double)

Gets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the [SetIQPowerEdgeTriggerSlope(string, RFmxGsmMXIQPowerEdgeTriggerSlope)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setiqpoweredgetriggerslope__string-rfmxgsmmxiqpoweredgetriggerslope.html) method to [Rising](nationalinstruments-rfmx-gsmmx-rfmxgsmmxiqpoweredgetriggerslope.html), the signal is quiet below the trigger level. If you set the IQ Power Edge Slope method to [Falling](nationalinstruments-rfmx-gsmmx-rfmxgsmmxiqpoweredgetriggerslope.html), the signal is quiet above the trigger level.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetTriggerMinimumQuietTimeDuration(string selectorString, out double value)

#### Remarks

This method gets the value of [TriggerMinimumQuietTimeDuration](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 582 microseconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the SetIQPowerEdgeTriggerSlope(string, RFmxGsmMXIQPowerEdgeTriggerSlope) method to Rising, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope method to Falling, the signal is quiet above the trigger level. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-gettriggerminimumquiettimemode__string-out.html language=enus -->
## TOPIC 00065: GetTriggerMinimumQuietTimeMode(string, out RFmxGsmMXTriggerMinimumQuietTimeMode)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-gettriggerminimumquiettimemode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-gettriggerminimumquiettimemode__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement computes the minimum quiet time used for triggering. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetTriggerMinimumQuietTimeMode(string selectorString, out RFmxGsmMXTriggerMinimumQuietTimeMode value)RemarksThis method gets the value of TriggerMinimumQuietTim

### GetTriggerMinimumQuietTimeMode(string, out RFmxGsmMXTriggerMinimumQuietTimeMode)

Gets whether the measurement computes the minimum quiet time used for triggering.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetTriggerMinimumQuietTimeMode(string selectorString, out RFmxGsmMXTriggerMinimumQuietTimeMode value)

#### Remarks

This method gets the value of [TriggerMinimumQuietTimeMode](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Auto](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggerminimumquiettimemode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxGsmMXTriggerMinimumQuietTimeMode | Upon return, contains whether the measurement computes the minimum quiet time used for triggering. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-gettriggertype__string-out.html language=enus -->
## TOPIC 00066: GetTriggerType(string, out RFmxGsmMXTriggerType)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-gettriggertype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-gettriggertype__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the trigger type. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetTriggerType(string selectorString, out RFmxGsmMXTriggerType value)RemarksThis method gets the value of TriggerType attribute.The default value is IQ Power Edge.ParametersNameTypeDescriptionselectorStringstringPass an

### GetTriggerType(string, out RFmxGsmMXTriggerType)

Gets the trigger type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetTriggerType(string selectorString, out RFmxGsmMXTriggerType value)

#### Remarks

This method gets the value of [TriggerType](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is IQ Power Edge.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxGsmMXTriggerType | Upon return, contains the trigger type. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-gettsc__string-out.html language=enus -->
## TOPIC 00067: GetTsc(string, out RFmxGsmMXTsc)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-gettsc__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-gettsc__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the training sequence code (TSC) to use. This method is applicable only when you set the SetBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType) method to Tsc and the SetAutoTscDetectionEnabled(string, RFmxGsmMXAutoTscDetectionEnabled) method to False. For access burst Tsc0, Tsc1

### GetTsc(string, out RFmxGsmMXTsc)

Gets the training sequence code (TSC) to use. This method is applicable only when you set the [SetBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setburstsynchronizationtype__string-rfmxgsmmxburstsynchronizationtype.html) method to [Tsc](nationalinstruments-rfmx-gsmmx-rfmxgsmmxburstsynchronizationtype.html) and the [SetAutoTscDetectionEnabled(string, RFmxGsmMXAutoTscDetectionEnabled)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setautotscdetectionenabled__string-rfmxgsmmxautotscdetectionenabled.html) method to [False](nationalinstruments-rfmx-gsmmx-rfmxgsmmxautotscdetectionenabled.html). For access burst [Tsc0](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtsc.html), [Tsc1](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtsc.html), and [Tsc2](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtsc.html) are applicable. Use "slot(n)" as the selector string to configure or read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetTsc(string selectorString, out RFmxGsmMXTsc value)

#### Remarks

This method gets the value of [Tsc](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Tsc0](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtsc.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the slot number. Example: "slot0". You can use the BuildSlotString(string, int) method to build the selector string. |
| value | out RFmxGsmMXTsc | Upon return, contains the training sequence code (TSC) to use. This method is applicable only when you set the SetBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType) method to Tsc and the SetAutoTscDetectionEnabled(string, RFmxGsmMXAutoTscDetectionEnabled) method to False. For access burst Tsc0, Tsc1, and Tsc2 are applicable. Use "slot(n)" as the selector string to configure or read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getwarning__out-out.html language=enus -->
## TOPIC 00068: GetWarning(out int, out string)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getwarning__out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-getwarning__out-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the latest warning code and description. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetWarning(out int warningCode, out string warningDescription)ParametersNameTypeDescriptionwarningCodeout intUpon return, contains the latest warning code.warningDescriptionout stringUpon return,

### GetWarning(out int, out string)

Gets the latest warning code and description.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetWarning(out int warningCode, out string warningDescription)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| warningCode | out int | Upon return, contains the latest warning code. |
| warningDescription | out string | Upon return, contains the latest warning description. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-initiate__string-string.html language=enus -->
## TOPIC 00069: Initiate(string, string)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-initiate__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-initiate__string-string.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates all enabled measurements. Call this method after configuring the signal and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch methods or result methods. To get the

### Initiate(string, string)

Initiates all enabled measurements. Call this method after configuring the signal and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch methods or result methods. To get the status of measurements, use the [WaitForMeasurementComplete(string, double)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-waitformeasurementcomplete__string-double.html) method or [CheckMeasurementStatus(string, out bool)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-checkmeasurementstatus__string-out.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int Initiate(string selectorString, string resultName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the result name in this parameter, either the result name specified by the resultName parameter or the default result instance is used. Example: "" "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| resultName | string | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example: "" "result::r1" "r1" |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-isdisposed.html language=enus -->
## TOPIC 00070: IsDisposed

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-isdisposed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-isdisposed.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates whether the signal has been disposed. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic bool IsDisposed { get; }Remarkstrue if the session is disposed; otherwise, false.

### IsDisposed

Gets a value that indicates whether the signal has been disposed.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public bool IsDisposed { get; }

#### Remarks

true if the session is disposed; otherwise, false.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-modacc.html language=enus -->
## TOPIC 00071: ModAcc

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-modacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-modacc.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxGsmMXModAcc instance that represents the ModAcc measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic RFmxGsmMXModAcc ModAcc { get; }

### ModAcc

Gets the [RFmxGsmMXModAcc](nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodacc.html) instance that represents the ModAcc measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public [RFmxGsmMXModAcc](nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodacc.html) ModAcc { get; }

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-orfs.html language=enus -->
## TOPIC 00072: Orfs

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-orfs.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-orfs.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxGsmMXOrfs instance that represents the ORFS measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic RFmxGsmMXOrfs Orfs { get; }

### Orfs

Gets the [RFmxGsmMXOrfs](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfs.html) instance that represents the ORFS measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public [RFmxGsmMXOrfs](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfs.html) Orfs { get; }

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-pvt.html language=enus -->
## TOPIC 00073: Pvt

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-pvt.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-pvt.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxGsmMXPvt instance that represents the PVT measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic RFmxGsmMXPvt Pvt { get; }

### Pvt

Gets the [RFmxGsmMXPvt](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvt.html) instance that represents the PVT measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public [RFmxGsmMXPvt](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvt.html) Pvt { get; }

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-resetattribute__string-rfmxgsmmxpropertyid.html language=enus -->
## TOPIC 00074: ResetAttribute(string, RFmxGsmMXPropertyId)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-resetattribute__string-rfmxgsmmxpropertyid.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-resetattribute__string-rfmxgsmmxpropertyid.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the attribute to its default value. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int ResetAttribute(string selectorString, RFmxGsmMXPropertyId attributeId)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the property being reset. Refer to the Using a

### ResetAttribute(string, RFmxGsmMXPropertyId)

Resets the attribute to its default value.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ResetAttribute(string selectorString, RFmxGsmMXPropertyId attributeId)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the property being reset. Refer to the Using a Selector String (.NET) topic in the RFmx CDMA2K Help for more information about configuring the selector string. |
| attributeId | RFmxGsmMXPropertyId | Specifies an attribute identifier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-resettodefault__string.html language=enus -->
## TOPIC 00075: ResetToDefault(string)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-resettodefault__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-resettodefault__string.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a signal to the default values. This method disables all the external attenuation tables in all calibration planes.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int ResetToDefault(string selectorString)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal n

### ResetToDefault(string)

Resets a signal to the default values. This method disables all the external attenuation tables in all calibration planes.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ResetToDefault(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-selectmeasurements__string-rfmxgsmmxmeasurementtypes-bool.html language=enus -->
## TOPIC 00076: SelectMeasurements(string, RFmxGsmMXMeasurementTypes, bool)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-selectmeasurements__string-rfmxgsmmxmeasurementtypes-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-selectmeasurements__string-rfmxgsmmxmeasurementtypes-bool.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurements that you want to enable. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SelectMeasurements(string selectorString, RFmxGsmMXMeasurementTypes measurement, bool enableAllTraces)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name t

### SelectMeasurements(string, RFmxGsmMXMeasurementTypes, bool)

Specifies the measurements that you want to enable.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SelectMeasurements(string selectorString, RFmxGsmMXMeasurementTypes measurement, bool enableAllTraces)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| measurement | RFmxGsmMXMeasurementTypes | Specifies the measurement to perform. |
| enableAllTraces | bool | True to enable all traces for the selected measurement; otherwise False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-sendsoftwareedgetrigger.html language=enus -->
## TOPIC 00077: SendSoftwareEdgeTrigger()

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-sendsoftwareedgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-sendsoftwareedgetrigger.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a trigger to the device when you use the RFmxGSM_CfgTrigger method to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this method to override a hardware trigger. This method returns an error in the following situations: You configur

### SendSoftwareEdgeTrigger()

Sends a trigger to the device when you use the RFmxGSM_CfgTrigger method to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this method to override a hardware trigger. 
 This method returns an error in the following situations: 
 You configure an invalid trigger. You have not previously called the RFmxGSM Initiate method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SendSoftwareEdgeTrigger()

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setattributebool__string-int-bool.html language=enus -->
## TOPIC 00078: SetAttributeBool(string, int, bool)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setattributebool__string-int-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setattributebool__string-int-bool.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a Bool attribute. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetAttributeBool(string selectorString, int attributeIdentifier, bool value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being set. Refer to the Using a S

### SetAttributeBool(string, int, bool)

Sets the value of a Bool attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetAttributeBool(string selectorString, int attributeIdentifier, bool value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx GSM Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | bool | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setattributedouble__string-int-double.html language=enus -->
## TOPIC 00079: SetAttributeDouble(string, int, double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setattributedouble__string-int-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setattributedouble__string-int-double.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a Double attribute. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetAttributeDouble(string selectorString, int attributeIdentifier, double value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being set. Refer to the Usi

### SetAttributeDouble(string, int, double)

Sets the value of a Double attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetAttributeDouble(string selectorString, int attributeIdentifier, double value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx GSM Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | double | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setattributeint__string-int-int.html language=enus -->
## TOPIC 00080: SetAttributeInt(string, int, int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setattributeint__string-int-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setattributeint__string-int-int.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a Int attribute. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetAttributeInt(string selectorString, int attributeIdentifier, int value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being set. Refer to the Using a Sele

### SetAttributeInt(string, int, int)

Sets the value of a Int attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetAttributeInt(string selectorString, int attributeIdentifier, int value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx GSM Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | int | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setattributestring__string-int-string.html language=enus -->
## TOPIC 00081: SetAttributeString(string, int, string)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setattributestring__string-int-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setattributestring__string-int-string.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a String attribute. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetAttributeString(string selectorString, int attributeIdentifier, string value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being set. Refer to the Usi

### SetAttributeString(string, int, string)

Sets the value of a String attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetAttributeString(string selectorString, int attributeIdentifier, string value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx GSM Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | string | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setautolevelinitialreferencelevel__string-double.html language=enus -->
## TOPIC 00082: SetAutoLevelInitialReferenceLevel(string, double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setautolevelinitialreferencelevel__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setautolevelinitialreferencelevel__string-double.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the initial reference level the AutoLevel(string, double, out double) function uses to estimate the peak power of the input signal. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetAutoLevelInitialReferenceLevel(string selectorString, double value)Rem

### SetAutoLevelInitialReferenceLevel(string, double)

Sets the initial reference level the [AutoLevel(string, double, out double)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-autolevel__string-double-out.html) function uses to estimate the peak power of the input signal. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetAutoLevelInitialReferenceLevel(string selectorString, double value)

#### Remarks

This method sets the value of [AutoLevelInitialReferenceLevel](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 30.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the initial reference level the AutoLevel(string, double, out double) function uses to estimate the peak power of the input signal. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setautotscdetectionenabled__string-rfmxgsmmxautotscdetectionenabled.html language=enus -->
## TOPIC 00083: SetAutoTscDetectionEnabled(string, RFmxGsmMXAutoTscDetectionEnabled)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setautotscdetectionenabled__string-rfmxgsmmxautotscdetectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setautotscdetectionenabled__string-rfmxgsmmxautotscdetectionenabled.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement automatically detects the training sequence code (TSC). SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetAutoTscDetectionEnabled(string selectorString, RFmxGsmMXAutoTscDetectionEnabled value)RemarksThis method sets the value of AutoTscDetectionEnabled attribu

### SetAutoTscDetectionEnabled(string, RFmxGsmMXAutoTscDetectionEnabled)

Sets whether the measurement automatically detects the training sequence code (TSC).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetAutoTscDetectionEnabled(string selectorString, RFmxGsmMXAutoTscDetectionEnabled value)

#### Remarks

This method sets the value of [AutoTscDetectionEnabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-gsmmx-rfmxgsmmxautotscdetectionenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxGsmMXAutoTscDetectionEnabled | Specifies whether the measurement automatically detects the training sequence code (TSC). |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setband__string-rfmxgsmmxband.html language=enus -->
## TOPIC 00084: SetBand(string, RFmxGsmMXBand)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setband__string-rfmxgsmmxband.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setband__string-rfmxgsmmxband.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the operation band. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetBand(string selectorString, RFmxGsmMXBand value)RemarksThis method sets the value of Band attribute.The default value is Pgsm.ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name t

### SetBand(string, RFmxGsmMXBand)

Sets the operation band.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetBand(string selectorString, RFmxGsmMXBand value)

#### Remarks

This method sets the value of [Band](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Pgsm](nationalinstruments-rfmx-gsmmx-rfmxgsmmxband.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxGsmMXBand | Specifies the operation band. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setburstsynchronizationtype__string-rfmxgsmmxburstsynchronizationtype.html language=enus -->
## TOPIC 00085: SetBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setburstsynchronizationtype__string-rfmxgsmmxburstsynchronizationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setburstsynchronizationtype__string-rfmxgsmmxburstsynchronizationtype.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the method used to synchronize the burst. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetBurstSynchronizationType(string selectorString, RFmxGsmMXBurstSynchronizationType value)RemarksThis method sets the value of BurstSynchronizationType attribute.The default value is Tsc.Paramet

### SetBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType)

Sets the method used to synchronize the burst.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetBurstSynchronizationType(string selectorString, RFmxGsmMXBurstSynchronizationType value)

#### Remarks

This method sets the value of [BurstSynchronizationType](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Tsc](nationalinstruments-rfmx-gsmmx-rfmxgsmmxburstsynchronizationtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxGsmMXBurstSynchronizationType | Specifies the method used to synchronize the burst. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setbursttype__string-rfmxgsmmxbursttype.html language=enus -->
## TOPIC 00086: SetBurstType(string, RFmxGsmMXBurstType)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setbursttype__string-rfmxgsmmxbursttype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setbursttype__string-rfmxgsmmxbursttype.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the burst type. Use "slot(n)" as the selector string to configure or read this method. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetBurstType(string selectorString, RFmxGsmMXBurstType value)RemarksThis method sets the value of BurstType attribute.The default value is NB.Paramete

### SetBurstType(string, RFmxGsmMXBurstType)

Sets the burst type. Use "slot(n)" as the selector string to configure or read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetBurstType(string selectorString, RFmxGsmMXBurstType value)

#### Remarks

This method sets the value of [BurstType](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [NB](nationalinstruments-rfmx-gsmmx-rfmxgsmmxbursttype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the slot number. Example: "slot0". You can use the BuildSlotString(string, int) method to build the selector string. |
| value | RFmxGsmMXBurstType | Specifies the burst type. Use "slot(n)" as the selector string to configure or read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setcenterfrequency__string-double.html language=enus -->
## TOPIC 00087: SetCenterFrequency(string, double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setcenterfrequency__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setcenterfrequency__string-double.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetCenterFrequency(string selectorString, double value)RemarksThis method sets the value of CenterFrequ

### SetCenterFrequency(string, double)

Sets the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetCenterFrequency(string selectorString, double value)

#### Remarks

This method sets the value of [CenterFrequency](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 890.2 MHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setdigitaledgetriggeredge__string-rfmxgsmmxdigitaledgetriggeredge.html language=enus -->
## TOPIC 00088: SetDigitalEdgeTriggerEdge(string, RFmxGsmMXDigitalEdgeTriggerEdge)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setdigitaledgetriggeredge__string-rfmxgsmmxdigitaledgetriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setdigitaledgetriggeredge__string-rfmxgsmmxdigitaledgetriggeredge.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to DigitalEdge. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetDigitalEdgeTriggerEdge(string selectorString, RFmxGsmMXDigitalEdgeTriggerEdge value)Remarks

### SetDigitalEdgeTriggerEdge(string, RFmxGsmMXDigitalEdgeTriggerEdge)

Sets the active edge for the trigger. This method is used only when you set the [SetTriggerType(string, RFmxGsmMXTriggerType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggertype__string-rfmxgsmmxtriggertype.html) method to [DigitalEdge](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetDigitalEdgeTriggerEdge(string selectorString, RFmxGsmMXDigitalEdgeTriggerEdge value)

#### Remarks

This method sets the value of [DigitalEdgeTriggerEdge](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Rising](nationalinstruments-rfmx-gsmmx-rfmxgsmmxdigitaledgetriggeredge.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxGsmMXDigitalEdgeTriggerEdge | Specifies the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to DigitalEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setdigitaledgetriggersource__string-string.html language=enus -->
## TOPIC 00089: SetDigitalEdgeTriggerSource(string, string)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setdigitaledgetriggersource__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setdigitaledgetriggersource__string-string.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the source terminal for the digital-edge trigger. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to DigitalEdge. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetDigitalEdgeTriggerSource(string selectorString, string value)RemarksThis m

### SetDigitalEdgeTriggerSource(string, string)

Sets the source terminal for the digital-edge trigger. This method is used only when you set the [SetTriggerType(string, RFmxGsmMXTriggerType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggertype__string-rfmxgsmmxtriggertype.html) method to [DigitalEdge](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetDigitalEdgeTriggerSource(string selectorString, string value)

#### Remarks

This method sets the value of [DigitalEdgeTriggerSource](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is PFI0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | string | Specifies the source terminal for the digital-edge trigger. Use the string constants from the RFmxGsmMXConstants class or any other valid string to configure this parameter. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to DigitalEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setexternalattenuation__string-double.html language=enus -->
## TOPIC 00090: SetExternalAttenuation(string, double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setexternalattenuation__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setexternalattenuation__string-double.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. SyntaxNamespace: Na

### SetExternalAttenuation(string, double)

Sets the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the *NI RF Vector Signal Analyzers Help*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetExternalAttenuation(string selectorString, double value)

#### Remarks

This method sets the value of [ExternalAttenuation](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-sethbfilterwidth__string-rfmxgsmmxhbfilterwidth.html language=enus -->
## TOPIC 00091: SetHBFilterWidth(string, RFmxGsmMXHBFilterWidth)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-sethbfilterwidth__string-rfmxgsmmxhbfilterwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-sethbfilterwidth__string-rfmxgsmmxhbfilterwidth.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the filter width when you set the SetBurstType(string, RFmxGsmMXBurstType) method to HB. Use "slot(n)" as the selector string to configure or read this method. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetHBFilterWidth(string selectorString, RFmxGsmMXHBFilterWidth value)RemarksT

### SetHBFilterWidth(string, RFmxGsmMXHBFilterWidth)

Sets the filter width when you set the [SetBurstType(string, RFmxGsmMXBurstType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setbursttype__string-rfmxgsmmxbursttype.html) method to [HB](nationalinstruments-rfmx-gsmmx-rfmxgsmmxbursttype.html). Use "slot(n)" as the selector string to configure or read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetHBFilterWidth(string selectorString, RFmxGsmMXHBFilterWidth value)

#### Remarks

This method sets the value of [HBFilterWidth](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Narrow](nationalinstruments-rfmx-gsmmx-rfmxgsmmxhbfilterwidth.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the slot number. Example: "slot0". You can use the BuildSlotString(string, int) method to build the selector string. |
| value | RFmxGsmMXHBFilterWidth | Specifies the filter width when you set the SetBurstType(string, RFmxGsmMXBurstType) method to HB. Use "slot(n)" as the selector string to configure or read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setiqpoweredgetriggerlevel__string-double.html language=enus -->
## TOPIC 00092: SetIQPowerEdgeTriggerLevel(string, double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setiqpoweredgetriggerlevel__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setiqpoweredgetriggerlevel__string-double.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the power level at which the device triggers. This value is expressed in dB when you set the SetIQPowerEdgeTriggerLevelType(string, RFmxGsmMXIQPowerEdgeTriggerLevelType) method to Relative and in dBm when you set the IQ Power Edge Level Type method to Absolute. The device asserts the trigger wh

### SetIQPowerEdgeTriggerLevel(string, double)

Sets the power level at which the device triggers. This value is expressed in dB when you set the [SetIQPowerEdgeTriggerLevelType(string, RFmxGsmMXIQPowerEdgeTriggerLevelType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setiqpoweredgetriggerleveltype__string-rfmxgsmmxiqpoweredgetriggerleveltype.html) method to [Relative](nationalinstruments-rfmx-gsmmx-rfmxgsmmxiqpoweredgetriggerleveltype.html) and in dBm when you set the IQ Power Edge Level Type method to [Absolute](nationalinstruments-rfmx-gsmmx-rfmxgsmmxiqpoweredgetriggerleveltype.html). The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the [SetTriggerType(string, RFmxGsmMXTriggerType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggertype__string-rfmxgsmmxtriggertype.html) method to [IQPowerEdge](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetIQPowerEdgeTriggerLevel(string selectorString, double value)

#### Remarks

This method sets the value of [IQPowerEdgeTriggerLevel](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is -20 dB.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the power level at which the device triggers. This value is expressed in dB when you set the SetIQPowerEdgeTriggerLevelType(string, RFmxGsmMXIQPowerEdgeTriggerLevelType) method to Relative and in dBm when you set the IQ Power Edge Level Type method to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setiqpoweredgetriggerleveltype__string-rfmxgsmmxiqpoweredgetriggerleveltype.html language=enus -->
## TOPIC 00093: SetIQPowerEdgeTriggerLevelType(string, RFmxGsmMXIQPowerEdgeTriggerLevelType)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setiqpoweredgetriggerleveltype__string-rfmxgsmmxiqpoweredgetriggerleveltype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setiqpoweredgetriggerleveltype__string-rfmxgsmmxiqpoweredgetriggerleveltype.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetIQPowerEdgeTriggerLevelType

### SetIQPowerEdgeTriggerLevelType(string, RFmxGsmMXIQPowerEdgeTriggerLevelType)

Sets the reference for the [SetIQPowerEdgeTriggerLevel(string, double)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setiqpoweredgetriggerlevel__string-double.html) method. The IQ Power Edge Level Type method is used only when you set the [SetTriggerType(string, RFmxGsmMXTriggerType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggertype__string-rfmxgsmmxtriggertype.html) method to [IQPowerEdge](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetIQPowerEdgeTriggerLevelType(string selectorString, RFmxGsmMXIQPowerEdgeTriggerLevelType value)

#### Remarks

This method sets the value of [IQPowerEdgeTriggerLevelType](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Relative](nationalinstruments-rfmx-gsmmx-rfmxgsmmxiqpoweredgetriggerleveltype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxGsmMXIQPowerEdgeTriggerLevelType | Specifies the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setiqpoweredgetriggerslope__string-rfmxgsmmxiqpoweredgetriggerslope.html language=enus -->
## TOPIC 00094: SetIQPowerEdgeTriggerSlope(string, RFmxGsmMXIQPowerEdgeTriggerSlope)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setiqpoweredgetriggerslope__string-rfmxgsmmxiqpoweredgetriggerslope.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setiqpoweredgetriggerslope__string-rfmxgsmmxiqpoweredgetriggerslope.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the SetIQPowerEdgeTriggerLevel(string, double) method with the slope you specify. This method is used only whe

### SetIQPowerEdgeTriggerSlope(string, RFmxGsmMXIQPowerEdgeTriggerSlope)

Sets whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the [SetIQPowerEdgeTriggerLevel(string, double)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setiqpoweredgetriggerlevel__string-double.html) method with the slope you specify. This method is used only when you set the [SetTriggerType(string, RFmxGsmMXTriggerType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggertype__string-rfmxgsmmxtriggertype.html) method to [IQPowerEdge](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetIQPowerEdgeTriggerSlope(string selectorString, RFmxGsmMXIQPowerEdgeTriggerSlope value)

#### Remarks

This method sets the value of [IQPowerEdgeTriggerSlope](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Rising](nationalinstruments-rfmx-gsmmx-rfmxgsmmxiqpoweredgetriggerslope.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxGsmMXIQPowerEdgeTriggerSlope | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the SetIQPowerEdgeTriggerLevel(string, double) method with the slope you specify. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setiqpoweredgetriggersource__string-string.html language=enus -->
## TOPIC 00095: SetIQPowerEdgeTriggerSource(string, string)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setiqpoweredgetriggersource__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setiqpoweredgetriggersource__string-string.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetIQPowerEdgeTriggerSource(string selectorString, string value)Remarks

### SetIQPowerEdgeTriggerSource(string, string)

Sets the channel from which the device monitors the trigger. This method is used only when you set the [SetTriggerType(string, RFmxGsmMXTriggerType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggertype__string-rfmxgsmmxtriggertype.html) method to [IQPowerEdge](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetIQPowerEdgeTriggerSource(string selectorString, string value)

#### Remarks

This method sets the value of [IQPowerEdgeTriggerSource](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | string | Specifies the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setlimitedconfigurationchange__string-rfmxgsmmxlimitedconfigurationchange.html language=enus -->
## TOPIC 00096: SetLimitedConfigurationChange(string, RFmxGsmMXLimitedConfigurationChange)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setlimitedconfigurationchange__string-rfmxgsmmxlimitedconfigurationchange.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setlimitedconfigurationchange__string-rfmxgsmmxlimitedconfigurationchange.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the set of properties that are considered by RFmx in the locked signal configuration state. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetLimitedConfigurationChange(string selectorString, RFmxGsmMXLimitedConfigurationChange value)Remarks>If your test system performs the same meas

### SetLimitedConfigurationChange(string, RFmxGsmMXLimitedConfigurationChange)

Sets the set of properties that are considered by RFmx in the locked signal configuration state.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetLimitedConfigurationChange(string selectorString, RFmxGsmMXLimitedConfigurationChange value)

#### Remarks

>If your test system performs the same measurement at multiple frequencies and/or power levels repeatedly, enabling this method can help achieve faster measurements. When you set this method to a value other than [Disabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxlimitedconfigurationchange.html), the RFmx driver will use an optimized code path and skip some checks. Because RFmx skips some checks when you use this property, you need to be aware of the limitations of this feature, which are listed in the Limitations of the Limited Configuration Change Property topic. You can also use this method to lock a specific instrument configuration for a signal so that every time that you initiate the signal, RFmx applies the RFmxInstr properties from a locked configuration. NI recommends you use this method in conjunction with named signal configurations. Create named signal configurations for each measurement configuration in your test program and set this method to a value other than [Disabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxlimitedconfigurationchange.html) for one or more of the named signal configurations. This allows RFmx to precompute the acquisition settings for your measurement configurations and re-use the precomputed settings each time you initiate the measurement. You do not need to use this method if you create named signals for all the measurement configurations in your test program during test sequence initialization and do not change any RFInstr or personality properties while testing each device under test. RFmx automatically optimizes that use case. Specify the named signal configuration you are setting this property in the selector string input. This method sets the value of [LimitedConfigurationChange](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Disabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxlimitedconfigurationchange.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxGsmMXLimitedConfigurationChange | Specifies the set of properties that are considered by RFmx in the locked signal configuration state. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setlinkdirection__string-rfmxgsmmxlinkdirection.html language=enus -->
## TOPIC 00097: SetLinkDirection(string, RFmxGsmMXLinkDirection)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setlinkdirection__string-rfmxgsmmxlinkdirection.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setlinkdirection__string-rfmxgsmmxlinkdirection.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the source of the signal to be measured. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetLinkDirection(string selectorString, RFmxGsmMXLinkDirection value)RemarksThis method sets the value of LinkDirection attribute.The default value is Uplink.ParametersNameTypeDescriptionselectorS

### SetLinkDirection(string, RFmxGsmMXLinkDirection)

Sets the source of the signal to be measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetLinkDirection(string selectorString, RFmxGsmMXLinkDirection value)

#### Remarks

This method sets the value of [LinkDirection](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Uplink](nationalinstruments-rfmx-gsmmx-rfmxgsmmxlinkdirection.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxGsmMXLinkDirection | Specifies the source of the signal to be measured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setmodulationtype__string-rfmxgsmmxmodulationtype.html language=enus -->
## TOPIC 00098: SetModulationType(string, RFmxGsmMXModulationType)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setmodulationtype__string-rfmxgsmmxmodulationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setmodulationtype__string-rfmxgsmmxmodulationtype.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the modulation scheme used for the signal. Use "slot(n)" as the selector string to configure or read this method. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetModulationType(string selectorString, RFmxGsmMXModulationType value)RemarksThis method sets the value of ModulationType

### SetModulationType(string, RFmxGsmMXModulationType)

Sets the modulation scheme used for the signal. Use "slot(n)" as the selector string to configure or read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetModulationType(string selectorString, RFmxGsmMXModulationType value)

#### Remarks

This method sets the value of [ModulationType](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [ModulationType8Psk](nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodulationtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the slot number. Example: "slot0". You can use the BuildSlotString(string, int) method to build the selector string. |
| value | RFmxGsmMXModulationType | Specifies the modulation scheme used for the signal. Use "slot(n)" as the selector string to configure or read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setnumberoftimeslots__string-int.html language=enus -->
## TOPIC 00099: SetNumberOfTimeslots(string, int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setnumberoftimeslots__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setnumberoftimeslots__string-int.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of time slots to be measured. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetNumberOfTimeslots(string selectorString, int value)RemarksThis method sets the value of NumberOfTimeslots attribute.The default value is 1.ParametersNameTypeDescriptionselectorStringstringPass

### SetNumberOfTimeslots(string, int)

Sets the number of time slots to be measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetNumberOfTimeslots(string selectorString, int value)

#### Remarks

This method sets the value of [NumberOfTimeslots](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of time slots to be measured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setpowercontrollevel__string-int.html language=enus -->
## TOPIC 00100: SetPowerControlLevel(string, int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setpowercontrollevel__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setpowercontrollevel__string-int.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the power control level corresponding to the transmitted power, as defined in section 4.1 of the 3GPP TS 45.005 v8.0.0 specifications. Use "slot(n)" as the selector string to configure or read this method. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetPowerControlLevel(string sel

### SetPowerControlLevel(string, int)

Sets the power control level corresponding to the transmitted power, as defined in section 4.1 of the *3GPP TS 45.005 v8.0.0 specifications*. Use "slot(n)" as the selector string to configure or read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetPowerControlLevel(string selectorString, int value)

#### Remarks

This method sets the value of [PowerControlLevel](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 0. Valid values are 0 to 40, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the slot number. Example: "slot0". You can use the BuildSlotString(string, int) method to build the selector string. |
| value | int | Specifies the power control level corresponding to the transmitted power, as defined in section 4.1 of the 3GPP TS 45.005 v8.0.0 specifications. Use "slot(n)" as the selector string to configure or read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setreferencelevel__string-double.html language=enus -->
## TOPIC 00101: SetReferenceLevel(string, double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setreferencelevel__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setreferencelevel__string-double.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and V[pk-pk] for baseband devices. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetReferenceLevel(string selectorString, double value)RemarksThis met

### SetReferenceLevel(string, double)

Sets the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and V<sub>pk-pk</sub> for baseband devices.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetReferenceLevel(string selectorString, double value)

#### Remarks

This method sets the value of [ReferenceLevel](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setreferencelevelheadroom__string-double.html language=enus -->
## TOPIC 00102: SetReferenceLevelHeadroom(string, double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setreferencelevelheadroom__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setreferencelevelheadroom__string-double.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the margin RFmx adds to the Reference Level method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input signal

### SetReferenceLevelHeadroom(string, double)

Sets the margin RFmx adds to the Reference Level method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input signal remains within the reference level plus the reference level headroom. If you know the input power of the signal precisely or previously included the margin in the reference level, you could improve the signal-to-noise ratio by reducing the reference level headroom. **Default values** 
 PXIe-5668: 6 dB 
 PXIe-5830/5831/5832/5841/5842/5860: 1 dB 
 PXIe-5840: 0 dB **Supported devices:**PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetReferenceLevelHeadroom(string selectorString, double value)

#### Remarks

This method sets the value of [ReferenceLevelHeadroom](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the margin RFmx adds to the Reference Level method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setresultfetchtimeout__string-double.html language=enus -->
## TOPIC 00103: SetResultFetchTimeout(string, double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setresultfetchtimeout__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setresultfetchtimeout__string-double.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the time to wait before results are available. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx driver waits until the measurement is complete. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpub

### SetResultFetchTimeout(string, double)

Sets the time to wait before results are available. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx driver waits until the measurement is complete.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetResultFetchTimeout(string selectorString, double value)

#### Remarks

This method sets the value of [ResultFetchTimeout](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the time to wait before results are available. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx driver waits until the measurement is complete. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setselectedports__string-string.html language=enus -->
## TOPIC 00104: SetSelectedPorts(string, string)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setselectedports__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setselectedports__string-string.html
- document_id: `rfmxgsm-dotnet-api-ref`
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

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetSelectedPorts(string selectorString, string value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | string | Specifies the instrument port to be used by the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setsignalstructure__string-rfmxgsmmxsignalstructure.html language=enus -->
## TOPIC 00105: SetSignalStructure(string, RFmxGsmMXSignalStructure)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setsignalstructure__string-rfmxgsmmxsignalstructure.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setsignalstructure__string-rfmxgsmmxsignalstructure.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the signal is bursted or continuous. For bursted signal and continuous signals, set the SetTriggerType(string, RFmxGsmMXTriggerType) to IQPowerEdge and None, respectively. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetSignalStructure(string selectorString, RFmxGsmMXSignal

### SetSignalStructure(string, RFmxGsmMXSignalStructure)

Sets whether the signal is bursted or continuous. For bursted signal and continuous signals, set the [SetTriggerType(string, RFmxGsmMXTriggerType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggertype__string-rfmxgsmmxtriggertype.html) to [IQPowerEdge](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggertype.html) and [None](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggertype.html), respectively.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetSignalStructure(string selectorString, RFmxGsmMXSignalStructure value)

#### Remarks

This method sets the value of [SignalStructure](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Bursted](nationalinstruments-rfmx-gsmmx-rfmxgsmmxsignalstructure.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxGsmMXSignalStructure | Specifies whether the signal is bursted or continuous. For bursted signal and continuous signals, set the SetTriggerType(string, RFmxGsmMXTriggerType) to IQPowerEdge and None, respectively. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settimingadvance__string-int.html language=enus -->
## TOPIC 00106: SetTimingAdvance(string, int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settimingadvance__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settimingadvance__string-int.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the timing advance value as specified in the 3GPP TS 45.010 specification for GSM access burst. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetTimingAdvance(string selectorString, int value)RemarksThis method gets the value of TimingAdvance attribute.The default value is 0.Pa

### SetTimingAdvance(string, int)

Specifies the timing advance value as specified in the 3GPP TS 45.010 specification for GSM access burst.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetTimingAdvance(string selectorString, int value)

#### Remarks

This method gets the value of [TimingAdvance](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the timing advance value as specified in the 3GPP TS 45.010 specification for GSM access burst. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggerdelay__string-double.html language=enus -->
## TOPIC 00107: SetTriggerDelay(string, double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggerdelay__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggerdelay__string-double.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetTriggerDelay(string selectorSt

### SetTriggerDelay(string, double)

Sets the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetTriggerDelay(string selectorString, double value)

#### Remarks

This method sets the value of [TriggerDelay](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggerminimumquiettimeduration__string-double.html language=enus -->
## TOPIC 00108: SetTriggerMinimumQuietTimeDuration(string, double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggerminimumquiettimeduration__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggerminimumquiettimeduration__string-double.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the SetIQPowerEdgeTriggerSlope(string, RFmxGsmMXIQPowerEdgeTriggerSlope) method to Rising, the signal is quiet below the trigger level.

### SetTriggerMinimumQuietTimeDuration(string, double)

Sets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the [SetIQPowerEdgeTriggerSlope(string, RFmxGsmMXIQPowerEdgeTriggerSlope)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setiqpoweredgetriggerslope__string-rfmxgsmmxiqpoweredgetriggerslope.html) method to [Rising](nationalinstruments-rfmx-gsmmx-rfmxgsmmxiqpoweredgetriggerslope.html), the signal is quiet below the trigger level. If you set the IQ Power Edge Slope method to [Falling](nationalinstruments-rfmx-gsmmx-rfmxgsmmxiqpoweredgetriggerslope.html), the signal is quiet above the trigger level.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetTriggerMinimumQuietTimeDuration(string selectorString, double value)

#### Remarks

This method sets the value of [TriggerMinimumQuietTimeDuration](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 582 microseconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the SetIQPowerEdgeTriggerSlope(string, RFmxGsmMXIQPowerEdgeTriggerSlope) method to Rising, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope method to Falling, the signal is quiet above the trigger level. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggerminimumquiettimemode__string-rfmxgsmmxtriggerminimumquiettimemode.html language=enus -->
## TOPIC 00109: SetTriggerMinimumQuietTimeMode(string, RFmxGsmMXTriggerMinimumQuietTimeMode)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggerminimumquiettimemode__string-rfmxgsmmxtriggerminimumquiettimemode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggerminimumquiettimemode__string-rfmxgsmmxtriggerminimumquiettimemode.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement computes the minimum quiet time used for triggering. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetTriggerMinimumQuietTimeMode(string selectorString, RFmxGsmMXTriggerMinimumQuietTimeMode value)RemarksThis method sets the value of TriggerMinimumQuietTimeMod

### SetTriggerMinimumQuietTimeMode(string, RFmxGsmMXTriggerMinimumQuietTimeMode)

Sets whether the measurement computes the minimum quiet time used for triggering.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetTriggerMinimumQuietTimeMode(string selectorString, RFmxGsmMXTriggerMinimumQuietTimeMode value)

#### Remarks

This method sets the value of [TriggerMinimumQuietTimeMode](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Auto](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggerminimumquiettimemode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxGsmMXTriggerMinimumQuietTimeMode | Specifies whether the measurement computes the minimum quiet time used for triggering. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggertype__string-rfmxgsmmxtriggertype.html language=enus -->
## TOPIC 00110: SetTriggerType(string, RFmxGsmMXTriggerType)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggertype__string-rfmxgsmmxtriggertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggertype__string-rfmxgsmmxtriggertype.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the trigger type. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetTriggerType(string selectorString, RFmxGsmMXTriggerType value)RemarksThis method sets the value of TriggerType attribute.The default value is IQ Power Edge.ParametersNameTypeDescriptionselectorStringstringPass an emp

### SetTriggerType(string, RFmxGsmMXTriggerType)

Sets the trigger type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetTriggerType(string selectorString, RFmxGsmMXTriggerType value)

#### Remarks

This method sets the value of [TriggerType](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is IQ Power Edge.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxGsmMXTriggerType | Specifies the trigger type. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settsc__string-rfmxgsmmxtsc.html language=enus -->
## TOPIC 00111: SetTsc(string, RFmxGsmMXTsc)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settsc__string-rfmxgsmmxtsc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settsc__string-rfmxgsmmxtsc.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the training sequence code (TSC) to use. This method is applicable only when you set the SetBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType) method to Tsc and the SetAutoTscDetectionEnabled(string, RFmxGsmMXAutoTscDetectionEnabled) method to False. For access burst Tsc0, Tsc1

### SetTsc(string, RFmxGsmMXTsc)

Sets the training sequence code (TSC) to use. This method is applicable only when you set the [SetBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setburstsynchronizationtype__string-rfmxgsmmxburstsynchronizationtype.html) method to [Tsc](nationalinstruments-rfmx-gsmmx-rfmxgsmmxburstsynchronizationtype.html) and the [SetAutoTscDetectionEnabled(string, RFmxGsmMXAutoTscDetectionEnabled)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setautotscdetectionenabled__string-rfmxgsmmxautotscdetectionenabled.html) method to [False](nationalinstruments-rfmx-gsmmx-rfmxgsmmxautotscdetectionenabled.html). For access burst [Tsc0](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtsc.html), [Tsc1](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtsc.html), and [Tsc2](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtsc.html) are applicable. Use "slot(n)" as the selector string to configure or read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetTsc(string selectorString, RFmxGsmMXTsc value)

#### Remarks

This method sets the value of [Tsc](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Tsc0](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtsc.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the slot number. Example: "slot0". You can use the BuildSlotString(string, int) method to build the selector string. |
| value | RFmxGsmMXTsc | Specifies the training sequence code (TSC) to use. This method is applicable only when you set the SetBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType) method to Tsc and the SetAutoTscDetectionEnabled(string, RFmxGsmMXAutoTscDetectionEnabled) method to False. For access burst Tsc0, Tsc1, and Tsc2 are applicable. Use "slot(n)" as the selector string to configure or read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-signalconfigurationname.html language=enus -->
## TOPIC 00112: SignalConfigurationName

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-signalconfigurationname.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-signalconfigurationname.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the signal configuration name. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic string SignalConfigurationName { get; }RemarksReturns a string representing the signal configuration name

### SignalConfigurationName

Gets the signal configuration name.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public string SignalConfigurationName { get; }

#### Remarks

Returns a string representing the signal configuration name

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-signalconfigurationtype.html language=enus -->
## TOPIC 00113: SignalConfigurationType

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-signalconfigurationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-signalconfigurationtype.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Type object for RFmxGsmMX. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic Type SignalConfigurationType { get; }RemarksReturns the type of signal configuration object.

### SignalConfigurationType

Gets the Type object for RFmxGsmMX.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public Type SignalConfigurationType { get; }

#### Remarks

Returns the type of signal configuration object.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx-waitformeasurementcomplete__string-double.html language=enus -->
## TOPIC 00114: WaitForMeasurementComplete(string, double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx-waitformeasurementcomplete__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx-waitformeasurementcomplete__string-double.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the specified number for seconds for all the measurements to complete.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int WaitForMeasurementComplete(string selectorString, double timeout)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the re

### WaitForMeasurementComplete(string, double)

Waits for the specified number for seconds for all the measurements to complete.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int WaitForMeasurementComplete(string selectorString, double timeout)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the time for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMX Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmx.html language=enus -->
## TOPIC 00115: RFmxGsmMX Class

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmx.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmx.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines a root class which is used to identify and control GSM signal configuration. Derives fromISignalConfigurationIDisposableSyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic class RFmxGsmMX : ISignalConfiguration, IDisposablePropertiesNameDescriptionIsDisposedGets a value that indicates whet

### RFmxGsmMX Class

Defines a root class which is used to identify and control GSM signal configuration.

#### Derives from

- ISignalConfiguration
- IDisposable

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public class RFmxGsmMX : ISignalConfiguration, IDisposable

#### Properties

| Name | Description |
| --- | --- |
| IsDisposed | Gets a value that indicates whether the signal has been disposed. |
| ModAcc | Gets the RFmxGsmMXModAcc instance that represents the ModAcc measurement. |
| Orfs | Gets the RFmxGsmMXOrfs instance that represents the ORFS measurement. |
| Pvt | Gets the RFmxGsmMXPvt instance that represents the PVT measurement. |
| SignalConfigurationName | Gets the signal configuration name. |
| SignalConfigurationType | Gets the Type object for RFmxGsmMX. |

#### Methods

| Name | Description |
| --- | --- |
| AbortMeasurements(string) | Stops acquisition and measurements associated with the signal instance that you specify in the selectorString parameter. This acquisition and measurements were previously initiated by the Initiate(string, string) method. Calling this method is optional, unless you want to stop a measurement before it is complete. This method executes even if there is an incoming error. |
| AnalyzeIQ1Waveform(string, string, ComplexWaveform< ComplexSingle >, bool, long) | Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods. Use this method only if the RFmxInstrMX.GetRecommendedAcquisitionType method value is IQ. Query the RFmxInstrMX.GetRecommendedAcquisitionType method after calling the Commit(string) method. |
| AutoLevel(string, double, out double) | Examines the input signal to calculate the peak power level and sets it as the value of the SetReferenceLevel(string, double) method. Use this method to help calculate an approximate setting for the reference level. |
| CheckMeasurementStatus(string, out bool) | Checks the status of the measurement. Use this method to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
| ClearAllNamedResults(string) | Clears all results for the current signal instance. |
| ClearNamedResult(string) | Clears a result instance specified by the result name in the selectorString parameter. |
| CloneSignalConfiguration(string, out RFmxGsmMX) | Creates a new instance of a signal by copying all the method values from an existing signal instance. |
| Commit(string) | Commits settings to the hardware. Calling this method is optional. RFmxGSM commits settings to the hardware when you call the Initiate(string, string) method. |
| ConfigureAutoTscDetectionEnabled(string, RFmxGsmMXAutoTscDetectionEnabled) | Configures whether to auto detect the training sequence code (TSC). |
| ConfigureBand(string, RFmxGsmMXBand) | Configures the band of operation. |
| ConfigureBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType) | Configures the burst synchronization type. |
| ConfigureDigitalEdgeTrigger(string, string, RFmxGsmMXDigitalEdgeTriggerEdge, double, bool) | Configures the device to wait for a digital edge trigger and then marks a reference point within the record. |
| ConfigureExternalAttenuation(string, double) | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. |
| ConfigureFrequency(string, double) | Configures the center frequency of the RF signal to acquire. |
| ConfigureFrequencyArfcn(string, RFmxGsmMXLinkDirection, RFmxGsmMXBand, int) | Configures the center frequency from the absolute RF channel number (ARFCN), band, and the link direction. |
| ConfigureIQPowerEdgeTrigger(string, string, RFmxGsmMXIQPowerEdgeTriggerSlope, double, double, RFmxGsmMXTriggerMinimumQuietTimeMode, double, RFmxGsmMXIQPowerEdgeTriggerLevelType, bool) | Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record. |
| ConfigureLinkDirection(string, RFmxGsmMXLinkDirection) | Configures the source of the signal to be measured. |
| ConfigureNumberOfTimeslots(string, int) | Configures the number of timeslots to be measured. |
| ConfigurePowerControlLevel(string, int) | Configures the power control level corresponding to the transmitted power. Use "slot(n)" as the selector string to configure this method. |
| ConfigureReferenceLevel(string, double) | Configures the reference level, which represents the maximum expected power of an RF input signal. |
| ConfigureRF(string, double, double, double) | Configures the RF methods of the signal specified by the selector string. |
| ConfigureSignalType(string, RFmxGsmMXModulationType, RFmxGsmMXBurstType, RFmxGsmMXHBFilterWidth) | Configures the signal type. Use "slot(n)" as the selector string to configure this method. |
| ConfigureSoftwareEdgeTrigger(string, double, bool) | Configures the device to wait for a software trigger and then marks a reference point within the record. |
| ConfigureTsc(string, RFmxGsmMXTsc) | Configures the training sequence code (TSC) in the burst. Use "slot(n)" as the selector string to configure this method. |
| DeleteSignalConfiguration() | Deletes an instance of a signal. |
| DisableTrigger(string) | Configures the device to not wait for a trigger to mark a reference point within a record. This method defines the signal triggering as immediate. |
| Dispose() | Deletes the signal configuration if it is not the default signal configuration and clears any trace of the current signal configuration, if any. |
| GetAllNamedResultNames(string, out string[], out bool) | Returns all the named result names of the current signal instance. |
| GetAttributeBool(string, int, out bool) | Gets the value of a Bool attribute. |
| GetAttributeDouble(string, int, out double) | Gets the value of a Double attribute. |
| GetAttributeInt(string, int, out int) | Gets the value of an RFmx 32-bit integer (int32) attribute. |
| GetAttributeString(string, int, out string) | Gets the value of a of an RFmx string. |
| GetAutoLevelInitialReferenceLevel(string, out double) | Gets the initial reference level the AutoLevel(string, double, out double) function uses to estimate the peak power of the input signal. This value is expressed in dBm. |
| GetAutoTscDetectionEnabled(string, out RFmxGsmMXAutoTscDetectionEnabled) | Gets whether the measurement automatically detects the training sequence code (TSC). |
| GetBand(string, out RFmxGsmMXBand) | Gets the operation band. |
| GetBurstSynchronizationType(string, out RFmxGsmMXBurstSynchronizationType) | Gets the method used to synchronize the burst. |
| GetBurstType(string, out RFmxGsmMXBurstType) | Gets the burst type. Use "slot(n)" as the selector string to configure or read this method. |
| GetCenterFrequency(string, out double) | Gets the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency. |
| GetDigitalEdgeTriggerEdge(string, out RFmxGsmMXDigitalEdgeTriggerEdge) | Gets the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to DigitalEdge. |
| GetDigitalEdgeTriggerSource(string, out string) | Gets the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to DigitalEdge. |
| GetError(out int, out string) | Gets the latest error code and description. |
| GetErrorString(int, out string) | Converts the status code returned by an RFmxGSM function into a string. |
| GetExternalAttenuation(string, out double) | Gets the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |
| GetHBFilterWidth(string, out RFmxGsmMXHBFilterWidth) | Gets the filter width when you set the SetBurstType(string, RFmxGsmMXBurstType) method to HB. Use "slot(n)" as the selector string to configure or read this method. |
| GetIQPowerEdgeTriggerLevel(string, out double) | Gets the power level at which the device triggers. This value is expressed in dB when you set the SetIQPowerEdgeTriggerLevelType(string, RFmxGsmMXIQPowerEdgeTriggerLevelType) method to Relative and in dBm when you set the IQ Power Edge Level Type method to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge. |
| GetIQPowerEdgeTriggerLevelType(string, out RFmxGsmMXIQPowerEdgeTriggerLevelType) | Gets the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge. |
| GetIQPowerEdgeTriggerSlope(string, out RFmxGsmMXIQPowerEdgeTriggerSlope) | Gets whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the SetIQPowerEdgeTriggerLevel(string, double) method with the slope you specify. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge. |
| GetIQPowerEdgeTriggerSource(string, out string) | Gets the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge. |
| GetLimitedConfigurationChange(string, out RFmxGsmMXLimitedConfigurationChange) | Gets the set of properties that are considered by RFmx in the locked signal configuration state. |
| GetLinkDirection(string, out RFmxGsmMXLinkDirection) | Gets the source of the signal to be measured. |
| GetModulationType(string, out RFmxGsmMXModulationType) | Gets the modulation scheme used for the signal. Use "slot(n)" as the selector string to configure or read this method. |
| GetNumberOfTimeslots(string, out int) | Gets the number of time slots to be measured. |
| GetPowerControlLevel(string, out int) | Gets the power control level corresponding to the transmitted power, as defined in section 4.1 of the 3GPP TS 45.005 v8.0.0 specifications. Use "slot(n)" as the selector string to configure or read this method. |
| GetReferenceLevel(string, out double) | Gets the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
| GetReferenceLevelHeadroom(string, out double) | Gets the margin RFmx adds to the Reference Level method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input signal remains within the reference level plus the reference level headroom. If you know the input power of the signal precisely or previously included the margin in the reference level, you could improve the signal-to-noise ratio by reducing the reference level headroom. Default values PXIe-5668: 6 dB PXIe-5830/5831/5832/5841/5842/5860: 1 dB PXIe-5840: 0 dB Supported devices: PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860. |
| GetResultFetchTimeout(string, out double) | Gets the time to wait before results are available. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx driver waits until the measurement is complete. |
| GetSelectedPorts(string, out string) | Gets the instrument port to be configured to acquire a signal. Valid values PXIe-5820/5840: "" (empty string) PXIe-5830: if0, if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Default values PXIe-5820/5840: "" (empty string) PXIe-5830/5831/5832: if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Supported devices: PXIe-5820/5830/5831/5832/5840 </x></x> |
| GetSignalStructure(string, out RFmxGsmMXSignalStructure) | Gets whether the signal is bursted or continuous. For bursted signal and continuous signals, set the SetTriggerType(string, RFmxGsmMXTriggerType) to IQPowerEdge and None, respectively. |
| GetTimingAdvance(string, out int) | Specifies the timing advance value as specified in the 3GPP TS 45.010 specification for GSM access burst. |
| GetTriggerDelay(string, out double) | Gets the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. |
| GetTriggerMinimumQuietTimeDuration(string, out double) | Gets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the SetIQPowerEdgeTriggerSlope(string, RFmxGsmMXIQPowerEdgeTriggerSlope) method to Rising, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope method to Falling, the signal is quiet above the trigger level. |
| GetTriggerMinimumQuietTimeMode(string, out RFmxGsmMXTriggerMinimumQuietTimeMode) | Gets whether the measurement computes the minimum quiet time used for triggering. |
| GetTriggerType(string, out RFmxGsmMXTriggerType) | Gets the trigger type. |
| GetTsc(string, out RFmxGsmMXTsc) | Gets the training sequence code (TSC) to use. This method is applicable only when you set the SetBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType) method to Tsc and the SetAutoTscDetectionEnabled(string, RFmxGsmMXAutoTscDetectionEnabled) method to False. For access burst Tsc0, Tsc1, and Tsc2 are applicable. Use "slot(n)" as the selector string to configure or read this method. |
| GetWarning(out int, out string) | Gets the latest warning code and description. |
| Initiate(string, string) | Initiates all enabled measurements. Call this method after configuring the signal and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch methods or result methods. To get the status of measurements, use the WaitForMeasurementComplete(string, double) method or CheckMeasurementStatus(string, out bool) method. |
| ResetAttribute(string, RFmxGsmMXPropertyId) | Resets the attribute to its default value. |
| ResetToDefault(string) | Resets a signal to the default values. This method disables all the external attenuation tables in all calibration planes. |
| SelectMeasurements(string, RFmxGsmMXMeasurementTypes, bool) | Specifies the measurements that you want to enable. |
| SendSoftwareEdgeTrigger() | Sends a trigger to the device when you use the RFmxGSM_CfgTrigger method to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this method to override a hardware trigger. This method returns an error in the following situations: You configure an invalid trigger. You have not previously called the RFmxGSM Initiate method. |
| SetAttributeBool(string, int, bool) | Sets the value of a Bool attribute. |
| SetAttributeDouble(string, int, double) | Sets the value of a Double attribute. |
| SetAttributeInt(string, int, int) | Sets the value of a Int attribute. |
| SetAttributeString(string, int, string) | Sets the value of a String attribute. |
| SetAutoLevelInitialReferenceLevel(string, double) | Sets the initial reference level the AutoLevel(string, double, out double) function uses to estimate the peak power of the input signal. This value is expressed in dBm. |
| SetAutoTscDetectionEnabled(string, RFmxGsmMXAutoTscDetectionEnabled) | Sets whether the measurement automatically detects the training sequence code (TSC). |
| SetBand(string, RFmxGsmMXBand) | Sets the operation band. |
| SetBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType) | Sets the method used to synchronize the burst. |
| SetBurstType(string, RFmxGsmMXBurstType) | Sets the burst type. Use "slot(n)" as the selector string to configure or read this method. |
| SetCenterFrequency(string, double) | Sets the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency. |
| SetDigitalEdgeTriggerEdge(string, RFmxGsmMXDigitalEdgeTriggerEdge) | Sets the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to DigitalEdge. |
| SetDigitalEdgeTriggerSource(string, string) | Sets the source terminal for the digital-edge trigger. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to DigitalEdge. |
| SetExternalAttenuation(string, double) | Sets the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |
| SetHBFilterWidth(string, RFmxGsmMXHBFilterWidth) | Sets the filter width when you set the SetBurstType(string, RFmxGsmMXBurstType) method to HB. Use "slot(n)" as the selector string to configure or read this method. |
| SetIQPowerEdgeTriggerLevel(string, double) | Sets the power level at which the device triggers. This value is expressed in dB when you set the SetIQPowerEdgeTriggerLevelType(string, RFmxGsmMXIQPowerEdgeTriggerLevelType) method to Relative and in dBm when you set the IQ Power Edge Level Type method to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge. |
| SetIQPowerEdgeTriggerLevelType(string, RFmxGsmMXIQPowerEdgeTriggerLevelType) | Sets the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge. |
| SetIQPowerEdgeTriggerSlope(string, RFmxGsmMXIQPowerEdgeTriggerSlope) | Sets whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the SetIQPowerEdgeTriggerLevel(string, double) method with the slope you specify. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge. |
| SetIQPowerEdgeTriggerSource(string, string) | Sets the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge. |
| SetLimitedConfigurationChange(string, RFmxGsmMXLimitedConfigurationChange) | Sets the set of properties that are considered by RFmx in the locked signal configuration state. |
| SetLinkDirection(string, RFmxGsmMXLinkDirection) | Sets the source of the signal to be measured. |
| SetModulationType(string, RFmxGsmMXModulationType) | Sets the modulation scheme used for the signal. Use "slot(n)" as the selector string to configure or read this method. |
| SetNumberOfTimeslots(string, int) | Sets the number of time slots to be measured. |
| SetPowerControlLevel(string, int) | Sets the power control level corresponding to the transmitted power, as defined in section 4.1 of the 3GPP TS 45.005 v8.0.0 specifications. Use "slot(n)" as the selector string to configure or read this method. |
| SetReferenceLevel(string, double) | Sets the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
| SetReferenceLevelHeadroom(string, double) | Sets the margin RFmx adds to the Reference Level method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input signal remains within the reference level plus the reference level headroom. If you know the input power of the signal precisely or previously included the margin in the reference level, you could improve the signal-to-noise ratio by reducing the reference level headroom. Default values PXIe-5668: 6 dB PXIe-5830/5831/5832/5841/5842/5860: 1 dB PXIe-5840: 0 dB Supported devices: PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860. |
| SetResultFetchTimeout(string, double) | Sets the time to wait before results are available. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx driver waits until the measurement is complete. |
| SetSelectedPorts(string, string) | Sets the instrument port to be configured to acquire a signal. Valid values PXIe-5820/5840: "" (empty string) PXIe-5830: if0, if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Default values PXIe-5820/5840: "" (empty string) PXIe-5830/5831/5832: if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel Supported devices: PXIe-5820/5830/5831/5832/5840 </x></x> |
| SetSignalStructure(string, RFmxGsmMXSignalStructure) | Sets whether the signal is bursted or continuous. For bursted signal and continuous signals, set the SetTriggerType(string, RFmxGsmMXTriggerType) to IQPowerEdge and None, respectively. |
| SetTimingAdvance(string, int) | Specifies the timing advance value as specified in the 3GPP TS 45.010 specification for GSM access burst. |
| SetTriggerDelay(string, double) | Sets the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. |
| SetTriggerMinimumQuietTimeDuration(string, double) | Sets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the SetIQPowerEdgeTriggerSlope(string, RFmxGsmMXIQPowerEdgeTriggerSlope) method to Rising, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope method to Falling, the signal is quiet above the trigger level. |
| SetTriggerMinimumQuietTimeMode(string, RFmxGsmMXTriggerMinimumQuietTimeMode) | Sets whether the measurement computes the minimum quiet time used for triggering. |
| SetTriggerType(string, RFmxGsmMXTriggerType) | Sets the trigger type. |
| SetTsc(string, RFmxGsmMXTsc) | Sets the training sequence code (TSC) to use. This method is applicable only when you set the SetBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType) method to Tsc and the SetAutoTscDetectionEnabled(string, RFmxGsmMXAutoTscDetectionEnabled) method to False. For access burst Tsc0, Tsc1, and Tsc2 are applicable. Use "slot(n)" as the selector string to configure or read this method. |
| WaitForMeasurementComplete(string, double) | Waits for the specified number for seconds for all the measurements to complete. |
| BuildOffsetString(string, int) | Creates a offset string to use as the selector string with configuration or fetch methods and methods. |
| BuildResultString(string) | Creates selector string for use with configuration or fetch. |
| BuildSlotString(string, int) | Creates a slot string to use as the selector string with configuration or fetch methods and methods. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxautotscdetectionenabled.html language=enus -->
## TOPIC 00116: RFmxGsmMXAutoTscDetectionEnabled Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxautotscdetectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxautotscdetectionenabled.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement automatically detects the training sequence code (TSC). SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXAutoTscDetectionEnabledMembersNameValueDescriptionFalse0The measurement uses the value that you configure using the SetTsc(string, RFmxGsmMXTs

### RFmxGsmMXAutoTscDetectionEnabled Enumeration

Specifies whether the measurement automatically detects the training sequence code (TSC).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXAutoTscDetectionEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement uses the value that you configure using the SetTsc(string, RFmxGsmMXTsc) method. |
| True | 1 | The measurement detects the TSC in the burst. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxband.html language=enus -->
## TOPIC 00117: RFmxGsmMXBand Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxband.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxband.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the operation band. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXBandMembersNameValueDescriptionPgsm0The operation band is Primary GSM in the 900 MHz band. Egsm1The operation band is Extended GSM in the 900 MHz band. Rgsm2The operation band is Railway GSM in the 900

### RFmxGsmMXBand Enumeration

Specifies the operation band.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXBand

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Pgsm | 0 | The operation band is Primary GSM in the 900 MHz band. |
| Egsm | 1 | The operation band is Extended GSM in the 900 MHz band. |
| Rgsm | 2 | The operation band is Railway GSM in the 900 MHz band. |
| Dcs1800 | 3 | The operation band is GSM in the 1800 MHz band. |
| Pcs1900 | 4 | The operation band is GSM in the 1900 MHz band. |
| Gsm450 | 5 | The operation band is GSM in the 450 MHz band. |
| Gsm480 | 6 | The operation band is GSM in the 480 MHz band. |
| Gsm850 | 7 | The operation band is GSM in the 850 MHz band. |
| Gsm750 | 8 | The operation band is GSM in the 750 MHz band. |
| Tgsm810 | 9 | The operation band is terrestrial GSM in the 810 MHz band. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxburstsynchronizationtype.html language=enus -->
## TOPIC 00118: RFmxGsmMXBurstSynchronizationType Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxburstsynchronizationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxburstsynchronizationtype.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method used to synchronize the burst. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXBurstSynchronizationTypeMembersNameValueDescriptionTsc0Synchronizes the measurement to the timing of the demodulated training sequence in the burst. The measurement requires a burs

### RFmxGsmMXBurstSynchronizationType Enumeration

Specifies the method used to synchronize the burst.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXBurstSynchronizationType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Tsc | 0 | Synchronizes the measurement to the timing of the demodulated training sequence in the burst. The measurement requires a burst with a valid training sequence code (TSC). The measurement determines the T0 point by demodulating the burst and identifying the TSC. |
| Amplitude | 1 | Synchronizes the measurement based on the RF envelope of the received signal. The measurement sets the T0 point as the center of the RF envelope. |
| None | 2 | Sets the T0 point to 273.23 microseconds after the trigger. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxbursttype.html language=enus -->
## TOPIC 00119: RFmxGsmMXBurstType Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxbursttype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxbursttype.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the burst type. Use "slot(n)" as the selector string to configure or read this method. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXBurstTypeMembersNameValueDescriptionNB0The burst type is Normal Burst. HB1The burst type is Higher Symbol Rate Burst. AB2The burst type

### RFmxGsmMXBurstType Enumeration

Specifies the burst type. Use "slot(n)" as the selector string to configure or read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXBurstType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| NB | 0 | The burst type is Normal Burst. |
| HB | 1 | The burst type is Higher Symbol Rate Burst. |
| AB | 2 | The burst type is Access Burst. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-diopfi0.html language=enus -->
## TOPIC 00120: DioPfi0

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-diopfi0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-diopfi0.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic const string DioPfi0

### DioPfi0

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public const string DioPfi0

Parent topic:

RFmxGsmMXConstants Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-diopfi1.html language=enus -->
## TOPIC 00121: DioPfi1

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-diopfi1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-diopfi1.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic const string DioPfi1

### DioPfi1

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public const string DioPfi1

Parent topic:

RFmxGsmMXConstants Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-diopfi2.html language=enus -->
## TOPIC 00122: DioPfi2

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-diopfi2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-diopfi2.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic const string DioPfi2

### DioPfi2

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public const string DioPfi2

Parent topic:

RFmxGsmMXConstants Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-diopfi3.html language=enus -->
## TOPIC 00123: DioPfi3

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-diopfi3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-diopfi3.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic const string DioPfi3

### DioPfi3

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public const string DioPfi3

Parent topic:

RFmxGsmMXConstants Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-diopfi4.html language=enus -->
## TOPIC 00124: DioPfi4

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-diopfi4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-diopfi4.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic const string DioPfi4

### DioPfi4

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public const string DioPfi4

Parent topic:

RFmxGsmMXConstants Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-diopfi5.html language=enus -->
## TOPIC 00125: DioPfi5

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-diopfi5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-diopfi5.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic const string DioPfi5

### DioPfi5

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public const string DioPfi5

Parent topic:

RFmxGsmMXConstants Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-diopfi6.html language=enus -->
## TOPIC 00126: DioPfi6

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-diopfi6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-diopfi6.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic const string DioPfi6

### DioPfi6

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public const string DioPfi6

Parent topic:

RFmxGsmMXConstants Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-diopfi7.html language=enus -->
## TOPIC 00127: DioPfi7

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-diopfi7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-diopfi7.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic const string DioPfi7

### DioPfi7

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public const string DioPfi7

Parent topic:

RFmxGsmMXConstants Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pfi0.html language=enus -->
## TOPIC 00128: Pfi0

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pfi0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pfi0.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PFI 1 connector on the NI 5142 and NI 5622. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic const string Pfi0

### Pfi0

The signal is exported to the PFI 1 connector on the NI 5142 and NI 5622.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public const string Pfi0

Parent topic:

RFmxGsmMXConstants Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pfi1.html language=enus -->
## TOPIC 00129: Pfi1

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pfi1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pfi1.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 0. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic const string Pfi1

### Pfi1

The signal is exported to the PXI trigger line 0.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public const string Pfi1

Parent topic:

RFmxGsmMXConstants Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pulsein.html language=enus -->
## TOPIC 00130: PulseIn

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pulsein.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pulsein.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic const string PulseIn

### PulseIn

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public const string PulseIn

Parent topic:

RFmxGsmMXConstants Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxiedstarbline.html language=enus -->
## TOPIC 00131: PxieDStarBLine

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxiedstarbline.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxiedstarbline.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The trigger is received on the DStar B trigger line. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic const string PxieDStarBLine

### PxieDStarBLine

The trigger is received on the DStar B trigger line.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public const string PxieDStarBLine

Parent topic:

RFmxGsmMXConstants Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxistarline.html language=enus -->
## TOPIC 00132: PxiStarLine

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxistarline.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxistarline.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI star trigger line. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic const string PxiStarLine

### PxiStarLine

The signal is exported to the PXI star trigger line.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public const string PxiStarLine

Parent topic:

RFmxGsmMXConstants Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxitriggerline0.html language=enus -->
## TOPIC 00133: PxiTriggerLine0

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxitriggerline0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxitriggerline0.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 0. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic const string PxiTriggerLine0

### PxiTriggerLine0

The signal is exported to the PXI trigger line 0.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public const string PxiTriggerLine0

Parent topic:

RFmxGsmMXConstants Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxitriggerline1.html language=enus -->
## TOPIC 00134: PxiTriggerLine1

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxitriggerline1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxitriggerline1.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 1. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic const string PxiTriggerLine1

### PxiTriggerLine1

The signal is exported to the PXI trigger line 1.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public const string PxiTriggerLine1

Parent topic:

RFmxGsmMXConstants Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxitriggerline2.html language=enus -->
## TOPIC 00135: PxiTriggerLine2

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxitriggerline2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxitriggerline2.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 2. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic const string PxiTriggerLine2

### PxiTriggerLine2

The signal is exported to the PXI trigger line 2.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public const string PxiTriggerLine2

Parent topic:

RFmxGsmMXConstants Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxitriggerline3.html language=enus -->
## TOPIC 00136: PxiTriggerLine3

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxitriggerline3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxitriggerline3.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 3. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic const string PxiTriggerLine3

### PxiTriggerLine3

The signal is exported to the PXI trigger line 3.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public const string PxiTriggerLine3

Parent topic:

RFmxGsmMXConstants Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxitriggerline4.html language=enus -->
## TOPIC 00137: PxiTriggerLine4

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxitriggerline4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxitriggerline4.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 4. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic const string PxiTriggerLine4

### PxiTriggerLine4

The signal is exported to the PXI trigger line 4.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public const string PxiTriggerLine4

Parent topic:

RFmxGsmMXConstants Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxitriggerline5.html language=enus -->
## TOPIC 00138: PxiTriggerLine5

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxitriggerline5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxitriggerline5.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 5. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic const string PxiTriggerLine5

### PxiTriggerLine5

The signal is exported to the PXI trigger line 5.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public const string PxiTriggerLine5

Parent topic:

RFmxGsmMXConstants Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxitriggerline6.html language=enus -->
## TOPIC 00139: PxiTriggerLine6

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxitriggerline6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxitriggerline6.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 6. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic const string PxiTriggerLine6

### PxiTriggerLine6

The signal is exported to the PXI trigger line 6.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public const string PxiTriggerLine6

Parent topic:

RFmxGsmMXConstants Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxitriggerline7.html language=enus -->
## TOPIC 00140: PxiTriggerLine7

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxitriggerline7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-pxitriggerline7.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 7. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic const string PxiTriggerLine7

### PxiTriggerLine7

The signal is exported to the PXI trigger line 7.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public const string PxiTriggerLine7

Parent topic:

RFmxGsmMXConstants Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-timerevent.html language=enus -->
## TOPIC 00141: TimerEvent

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-timerevent.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants-timerevent.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The trigger is received from the timer event. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic const string TimerEvent

### TimerEvent

The trigger is received from the timer event.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public const string TimerEvent

Parent topic:

RFmxGsmMXConstants Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants.html language=enus -->
## TOPIC 00142: RFmxGsmMXConstants Class

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxconstants.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies constants for I/O terminals. Derives fromNoneSyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic class RFmxGsmMXConstantsFieldsNameDescriptionDioPfi0DioPfi1DioPfi2DioPfi3DioPfi4DioPfi5DioPfi6DioPfi7Pfi0The signal is exported to the PFI 1 connector on the NI 5142 and NI 5622. Pfi1The sign

### RFmxGsmMXConstants Class

Specifies constants for I/O terminals.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public class RFmxGsmMXConstants

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
| Pfi0 | The signal is exported to the PFI 1 connector on the NI 5142 and NI 5622. |
| Pfi1 | The signal is exported to the PXI trigger line 0. |
| PulseIn |  |
| PxieDStarBLine | The trigger is received on the DStar B trigger line. |
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

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxdigitaledgetriggeredge.html language=enus -->
## TOPIC 00143: RFmxGsmMXDigitalEdgeTriggerEdge Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxdigitaledgetriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxdigitaledgetriggeredge.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to DigitalEdge. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXDigitalEdgeTriggerEdgeMembersNameValueDescriptionRising0The trigger asserts on

### RFmxGsmMXDigitalEdgeTriggerEdge Enumeration

Specifies the active edge for the trigger. This method is used only when you set the [SetTriggerType(string, RFmxGsmMXTriggerType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggertype__string-rfmxgsmmxtriggertype.html) method to [DigitalEdge](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXDigitalEdgeTriggerEdge

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 0 | The trigger asserts on the rising edge of the signal. |
| Falling | 1 | The trigger asserts on the falling edge of the signal. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxhbfilterwidth.html language=enus -->
## TOPIC 00144: RFmxGsmMXHBFilterWidth Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxhbfilterwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxhbfilterwidth.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the filter width when you set the SetBurstType(string, RFmxGsmMXBurstType) method to HB. Use "slot(n)" as the selector string to configure or read this method. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXHBFilterWidthMembersNameValueDescriptionNarrow0The measurement

### RFmxGsmMXHBFilterWidth Enumeration

Specifies the filter width when you set the [SetBurstType(string, RFmxGsmMXBurstType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setbursttype__string-rfmxgsmmxbursttype.html) method to [HB](nationalinstruments-rfmx-gsmmx-rfmxgsmmxbursttype.html). Use "slot(n)" as the selector string to configure or read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXHBFilterWidth

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Narrow | 0 | The measurement uses a narrow filter. |
| Wide | 1 | The measurement uses a wide filter. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxiqpoweredgetriggerleveltype.html language=enus -->
## TOPIC 00145: RFmxGsmMXIQPowerEdgeTriggerLevelType Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxiqpoweredgetriggerleveltype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxiqpoweredgetriggerleveltype.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXIQPowerEdgeTrig

### RFmxGsmMXIQPowerEdgeTriggerLevelType Enumeration

Specifies the reference for the [SetIQPowerEdgeTriggerLevel(string, double)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setiqpoweredgetriggerlevel__string-double.html) method. The IQ Power Edge Level Type method is used only when you set the [SetTriggerType(string, RFmxGsmMXTriggerType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggertype__string-rfmxgsmmxtriggertype.html) method to [IQPowerEdge](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXIQPowerEdgeTriggerLevelType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Relative | 0 | The value of the IQ Power Edge Level method is relative to the value of the SetReferenceLevel(string, double) method. |
| Absolute | 1 | The IQ Power Edge Level method specifies the absolute power. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxiqpoweredgetriggerslope.html language=enus -->
## TOPIC 00146: RFmxGsmMXIQPowerEdgeTriggerSlope Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxiqpoweredgetriggerslope.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxiqpoweredgetriggerslope.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the SetIQPowerEdgeTriggerLevel(string, double) method with the slope you specify. This method is used onl

### RFmxGsmMXIQPowerEdgeTriggerSlope Enumeration

Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the [SetIQPowerEdgeTriggerLevel(string, double)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setiqpoweredgetriggerlevel__string-double.html) method with the slope you specify. This method is used only when you set the [SetTriggerType(string, RFmxGsmMXTriggerType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggertype__string-rfmxgsmmxtriggertype.html) method to [IQPowerEdge](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXIQPowerEdgeTriggerSlope

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 0 | The trigger asserts when the signal power is rising. |
| Falling | 1 | The trigger asserts when the signal power is falling. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxlimitedconfigurationchange.html language=enus -->
## TOPIC 00147: RFmxGsmMXLimitedConfigurationChange Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxlimitedconfigurationchange.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxlimitedconfigurationchange.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the set of properties that are considered by RFmx in the locked signal configuration state. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXLimitedConfigurationChangeMembersNameValueDescriptionDisabled0This is the normal mode of RFmx operation. All configuration changes

### RFmxGsmMXLimitedConfigurationChange Enumeration

Specifies the set of properties that are considered by RFmx in the locked signal configuration state.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXLimitedConfigurationChange

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Disabled | 0 | This is the normal mode of RFmx operation. All configuration changes in RFmxInstr properties or in personality properties will be applied during RFmx Commit. |
| NoChange | 1 | Signal configuration is locked after the first Commit of the named signal configuration. Any configuration change thereafter either in RFmxInstr properties or personality properties will not be considered by subsequent RFmx Commits or Initiates of this signal. Use No Change if you have created named signal configurations for all measurement configurations but are setting some RFmxInstr properties. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| Frequency | 2 | Signal configuration, other than center frequency and external attenuation, is locked after first Commit of the named signal configuration. Thereafter, only the Center Frequency and SetExternalAttenuation(string, double) method value changes will be considered by subsequent driver Commits or Initiates of this signal. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| ReferenceLevel | 3 | Signal configuration, other than the reference level, is locked after first Commit of the named signal configuration. Thereafter only the SetReferenceLevel(string, double) method value change will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends that you set the SetIQPowerEdgeTriggerLevelType(string, RFmxGsmMXIQPowerEdgeTriggerLevelType) to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| FrequencyAndReferenceLevel | 4 | Signal configuration, other than center frequency, reference level, and external attenuation, is locked after first Commit of the named signal configuration. Thereafter only Center Frequency, Reference Level, and External Attenuation method value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| SelectedPortsFrequencyAndReferenceLevel | 5 | Signal configuration, other than selected ports, center frequency, reference level, external attenuation, and RFInstr configuration is locked after first Commit of the named signal configuration. Thereafter only SetSelectedPorts(string, string), Center Frequency, SetReferenceLevel(string, double), and SetExternalAttenuation(string, double) method value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the SetIQPowerEdgeTriggerLevelType(string, RFmxGsmMXIQPowerEdgeTriggerLevelType) to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxlinkdirection.html language=enus -->
## TOPIC 00148: RFmxGsmMXLinkDirection Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxlinkdirection.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxlinkdirection.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the direction for which the frequency is calculated. Only Uplink is supported. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXLinkDirectionMembersNameValueDescriptionDownlink0The source is a base transceiver station. Uplink1The frequency is calculated in the reverse li

### RFmxGsmMXLinkDirection Enumeration

Specifies the direction for which the frequency is calculated. Only Uplink is supported.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXLinkDirection

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Downlink | 0 | The source is a base transceiver station. |
| Uplink | 1 | The frequency is calculated in the reverse link direction, also know as the uplink direction. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmeasurementtypes.html language=enus -->
## TOPIC 00149: RFmxGsmMXMeasurementTypes Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmeasurementtypes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmeasurementtypes.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXMeasurementTypesMembersNameValueDescriptionModAcc0x1Selects ModAcc measurement. Orfs0x2Selects ORFS measurement. Pvt0x4Selects PVT measurement.

### RFmxGsmMXMeasurementTypes Enumeration

Specifies the type of measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXMeasurementTypes

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ModAcc | 0x1 | Selects ModAcc measurement. |
| Orfs | 0x2 | Selects ORFS measurement. |
| Pvt | 0x4 | Selects PVT measurement. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodacc-configuration.html language=enus -->
## TOPIC 00150: Configuration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodacc-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodacc-configuration.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxGsmMXModAccConfiguration instance that provides methods to configure the ModAcc measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic RFmxGsmMXModAccConfiguration Configuration { get; }

### Configuration

Gets the [RFmxGsmMXModAccConfiguration](nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration.html) instance that provides methods to configure the ModAcc measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public [RFmxGsmMXModAccConfiguration](nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration.html) Configuration { get; }

Parent topic:

RFmxGsmMXModAcc Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodacc-results.html language=enus -->
## TOPIC 00151: Results

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodacc-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodacc-results.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxGsmMXModAccResults instance that provides methods to fetch and read the ModAcc measurement results. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic RFmxGsmMXModAccResults Results { get; }

### Results

Gets the [RFmxGsmMXModAccResults](nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults.html) instance that provides methods to fetch and read the ModAcc measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public [RFmxGsmMXModAccResults](nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults.html) Results { get; }

Parent topic:

RFmxGsmMXModAcc Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodacc.html language=enus -->
## TOPIC 00152: RFmxGsmMXModAcc Class

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodacc.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the ModAcc measurement. Derives fromRFmxGsmMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic class RFmxGsmMXModAcc : RFmxGsmMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxGsmMXModAccConfiguration instance that provides methods to configure the ModAcc measurem

### RFmxGsmMXModAcc Class

Represents the ModAcc measurement.

#### Derives from

- RFmxGsmMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public class RFmxGsmMXModAcc : RFmxGsmMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxGsmMXModAccConfiguration instance that provides methods to configure the ModAcc measurement. |
| Results | Gets the RFmxGsmMXModAccResults instance that provides methods to fetch and read the ModAcc measurement results. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccaveragingenabled.html language=enus -->
## TOPIC 00153: RFmxGsmMXModAccAveragingEnabled Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccaveragingenabled.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the modulation accuracy (ModAcc) measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXModAccAveragingEnabledMembersNameValueDescriptionFalse0The measurement is performed on a single acquisition. True1The measurement is averaged ov

### RFmxGsmMXModAccAveragingEnabled Enumeration

Specifies whether to enable averaging for the modulation accuracy (ModAcc) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXModAccAveragingEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement is performed on a single acquisition. |
| True | 1 | The measurement is averaged over multiple acquisitions. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-configureaveraging__string-rfmxgsmmxmodaccaveragingenabled-int.html language=enus -->
## TOPIC 00154: ConfigureAveraging(string, RFmxGsmMXModAccAveragingEnabled, int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-configureaveraging__string-rfmxgsmmxmodaccaveragingenabled-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-configureaveraging__string-rfmxgsmmxmodaccaveragingenabled-int.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the modulation accuracy (ModAcc) measurement.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int ConfigureAveraging(string selectorString, RFmxGsmMXModAccAveragingEnabled averagingEnabled, int averagingCount)ParametersNameTypeDescriptionselectorStringstringPass an empt

### ConfigureAveraging(string, RFmxGsmMXModAccAveragingEnabled, int)

Configures averaging for the modulation accuracy (ModAcc) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigureAveraging(string selectorString, RFmxGsmMXModAccAveragingEnabled averagingEnabled, int averagingCount)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| averagingEnabled | RFmxGsmMXModAccAveragingEnabled | Specifies whether to enable averaging for the measurement. |
| averagingCount | int | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-configuredroopcompensationenabled__string-rfmxgsmmxmodaccdroopcompensationenabled.html language=enus -->
## TOPIC 00155: ConfigureDroopCompensationEnabled(string, RFmxGsmMXModAccDroopCompensationEnabled)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-configuredroopcompensationenabled__string-rfmxgsmmxmodaccdroopcompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-configuredroopcompensationenabled__string-rfmxgsmmxmodaccdroopcompensationenabled.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int ConfigureDroopCompensationEnabled(string selectorString, RFmxGsmMXModAccDroopCompensationEnabled droopCompensationEnabled)ParametersNameTypeDesc

### ConfigureDroopCompensationEnabled(string, RFmxGsmMXModAccDroopCompensationEnabled)

Configures whether to enable droop compensation for the modulation accuracy (ModAcc) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigureDroopCompensationEnabled(string selectorString, RFmxGsmMXModAccDroopCompensationEnabled droopCompensationEnabled)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| droopCompensationEnabled | RFmxGsmMXModAccDroopCompensationEnabled | Specifies whether to enable droop compensation for the ModAcc measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00156: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method gets the value of ModAccAllTracesEnabled

### GetAllTracesEnabled(string, out bool)

Gets whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [ModAccAllTracesEnabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-getaveragingcount__string-out.html language=enus -->
## TOPIC 00157: GetAveragingCount(string, out int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-getaveragingcount__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-getaveragingcount__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxGsmMXModAccAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetAveragingCount(string selectorString, out int value)RemarksThis method gets the value of ModAc

### GetAveragingCount(string, out int)

Gets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxGsmMXModAccAveragingEnabled)](nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setaveragingenabled__string-rfmxgsmmxmodaccaveragingenabled.html) method to [True](nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetAveragingCount(string selectorString, out int value)

#### Remarks

This method gets the value of [ModAccAveragingCount](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxGsmMXModAccAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-getaveragingenabled__string-out.html language=enus -->
## TOPIC 00158: GetAveragingEnabled(string, out RFmxGsmMXModAccAveragingEnabled)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-getaveragingenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-getaveragingenabled__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable averaging for the modulation accuracy (ModAcc) measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetAveragingEnabled(string selectorString, out RFmxGsmMXModAccAveragingEnabled value)RemarksThis method gets the value of ModAccAveragingEnabled attribute.The

### GetAveragingEnabled(string, out RFmxGsmMXModAccAveragingEnabled)

Gets whether to enable averaging for the modulation accuracy (ModAcc) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetAveragingEnabled(string selectorString, out RFmxGsmMXModAccAveragingEnabled value)

#### Remarks

This method gets the value of [ModAccAveragingEnabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxGsmMXModAccAveragingEnabled | Upon return, contains whether to enable averaging for the modulation accuracy (ModAcc) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-getdroopcompensationenabled__string-out.html language=enus -->
## TOPIC 00159: GetDroopCompensationEnabled(string, out RFmxGsmMXModAccDroopCompensationEnabled)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-getdroopcompensationenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-getdroopcompensationenabled__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetDroopCompensationEn

### GetDroopCompensationEnabled(string, out RFmxGsmMXModAccDroopCompensationEnabled)

Gets whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetDroopCompensationEnabled(string selectorString, out RFmxGsmMXModAccDroopCompensationEnabled value)

#### Remarks

This method gets the value of [ModAccDroopCompensationEnabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccdroopcompensationenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxGsmMXModAccDroopCompensationEnabled | Upon return, contains whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00160: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable modulation accuracy (ModAcc) measurements on the acquired signal. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method gets the value of ModAccMeasurementEnabled attribute.The default value is

### GetMeasurementEnabled(string, out bool)

Gets whether to enable modulation accuracy (ModAcc) measurements on the acquired signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [ModAccMeasurementEnabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable modulation accuracy (ModAcc) measurements on the acquired signal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-getmeasurementinterval__string-out.html language=enus -->
## TOPIC 00161: GetMeasurementInterval(string, out RFmxGsmMXModAccMeasurementInterval)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-getmeasurementinterval__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-getmeasurementinterval__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement is performed on a single specified timeslot or across multiple timeslots. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetMeasurementInterval(string selectorString, out RFmxGsmMXModAccMeasurementInterval value)RemarksThis method gets the value of ModAccMeasu

### GetMeasurementInterval(string, out RFmxGsmMXModAccMeasurementInterval)

Gets whether the measurement is performed on a single specified timeslot or across multiple timeslots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetMeasurementInterval(string selectorString, out RFmxGsmMXModAccMeasurementInterval value)

#### Remarks

This method gets the value of [ModAccMeasurementInterval](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default Value iss 'Number of Timeslots'.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxGsmMXModAccMeasurementInterval | Upon return, contains whether the measurement is performed on a single specified timeslot or across multiple timeslots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-getmeasurementoffset__string-out.html language=enus -->
## TOPIC 00162: GetMeasurementOffset(string, out int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-getmeasurementoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-getmeasurementoffset__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the offset, relative to the trigger of the timeslot to be measured. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetMeasurementOffset(string selectorString, out int value)RemarksThis method gets the value of ModAccMeasurementOffset attribute.The default value is 0. Valid values are

### GetMeasurementOffset(string, out int)

Gets the offset, relative to the trigger of the timeslot to be measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetMeasurementOffset(string selectorString, out int value)

#### Remarks

This method gets the value of [ModAccMeasurementOffset](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 0. Valid values are [0, (Num Timeslots -1)].

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the offset, relative to the trigger of the timeslot to be measured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-getnumberofanalysisthreads__string-out.html language=enus -->
## TOPIC 00163: GetNumberOfAnalysisThreads(string, out int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-getnumberofanalysisthreads__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-getnumberofanalysisthreads__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources,

### GetNumberOfAnalysisThreads(string, out int)

Gets the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetNumberOfAnalysisThreads(string selectorString, out int value)

#### Remarks

This method gets the value of [ModAccNumberOfAnalysisThreads](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setalltracesenabled__string-bool.html language=enus -->
## TOPIC 00164: SetAllTracesEnabled(string, bool)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setalltracesenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setalltracesenabled__string-bool.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetAllTracesEnabled(string selectorString, bool value)RemarksThis method sets the value of ModAccAllTracesEnabled attr

### SetAllTracesEnabled(string, bool)

Sets whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetAllTracesEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [ModAccAllTracesEnabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setaveragingcount__string-int.html language=enus -->
## TOPIC 00165: SetAveragingCount(string, int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setaveragingcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setaveragingcount__string-int.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxGsmMXModAccAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetAveragingCount(string selectorString, int value)RemarksThis method sets the value of ModAccAve

### SetAveragingCount(string, int)

Sets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxGsmMXModAccAveragingEnabled)](nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setaveragingenabled__string-rfmxgsmmxmodaccaveragingenabled.html) method to [True](nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetAveragingCount(string selectorString, int value)

#### Remarks

This method sets the value of [ModAccAveragingCount](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxGsmMXModAccAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setaveragingenabled__string-rfmxgsmmxmodaccaveragingenabled.html language=enus -->
## TOPIC 00166: SetAveragingEnabled(string, RFmxGsmMXModAccAveragingEnabled)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setaveragingenabled__string-rfmxgsmmxmodaccaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setaveragingenabled__string-rfmxgsmmxmodaccaveragingenabled.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable averaging for the modulation accuracy (ModAcc) measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetAveragingEnabled(string selectorString, RFmxGsmMXModAccAveragingEnabled value)RemarksThis method sets the value of ModAccAveragingEnabled attribute.The defa

### SetAveragingEnabled(string, RFmxGsmMXModAccAveragingEnabled)

Sets whether to enable averaging for the modulation accuracy (ModAcc) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetAveragingEnabled(string selectorString, RFmxGsmMXModAccAveragingEnabled value)

#### Remarks

This method sets the value of [ModAccAveragingEnabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxGsmMXModAccAveragingEnabled | Specifies whether to enable averaging for the modulation accuracy (ModAcc) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setdroopcompensationenabled__string-rfmxgsmmxmodaccdroopcompensationenabled.html language=enus -->
## TOPIC 00167: SetDroopCompensationEnabled(string, RFmxGsmMXModAccDroopCompensationEnabled)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setdroopcompensationenabled__string-rfmxgsmmxmodaccdroopcompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setdroopcompensationenabled__string-rfmxgsmmxmodaccdroopcompensationenabled.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetDroopCompensationEn

### SetDroopCompensationEnabled(string, RFmxGsmMXModAccDroopCompensationEnabled)

Sets whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetDroopCompensationEnabled(string selectorString, RFmxGsmMXModAccDroopCompensationEnabled value)

#### Remarks

This method sets the value of [ModAccDroopCompensationEnabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccdroopcompensationenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxGsmMXModAccDroopCompensationEnabled | Specifies whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00168: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable modulation accuracy (ModAcc) measurements on the acquired signal. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method sets the value of ModAccMeasurementEnabled attribute.The default value is FALS

### SetMeasurementEnabled(string, bool)

Sets whether to enable modulation accuracy (ModAcc) measurements on the acquired signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [ModAccMeasurementEnabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable modulation accuracy (ModAcc) measurements on the acquired signal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setmeasurementinterval__string-rfmxgsmmxmodaccmeasurementinterval.html language=enus -->
## TOPIC 00169: SetMeasurementInterval(string, RFmxGsmMXModAccMeasurementInterval)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setmeasurementinterval__string-rfmxgsmmxmodaccmeasurementinterval.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setmeasurementinterval__string-rfmxgsmmxmodaccmeasurementinterval.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement is performed on a single specified timeslot or across multiple timeslots. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetMeasurementInterval(string selectorString, RFmxGsmMXModAccMeasurementInterval value)RemarksThis method sets the value of ModAccMeasureme

### SetMeasurementInterval(string, RFmxGsmMXModAccMeasurementInterval)

Sets whether the measurement is performed on a single specified timeslot or across multiple timeslots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetMeasurementInterval(string selectorString, RFmxGsmMXModAccMeasurementInterval value)

#### Remarks

This method sets the value of [ModAccMeasurementInterval](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default Value iss 'Number of Timeslots'.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxGsmMXModAccMeasurementInterval | Specifies whether the measurement is performed on a single specified timeslot or across multiple timeslots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setmeasurementoffset__string-int.html language=enus -->
## TOPIC 00170: SetMeasurementOffset(string, int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setmeasurementoffset__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setmeasurementoffset__string-int.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the offset, relative to the trigger of the timeslot to be measured. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetMeasurementOffset(string selectorString, int value)RemarksThis method sets the value of ModAccMeasurementOffset attribute.The default value is 0. Valid values are [0,

### SetMeasurementOffset(string, int)

Sets the offset, relative to the trigger of the timeslot to be measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetMeasurementOffset(string selectorString, int value)

#### Remarks

This method sets the value of [ModAccMeasurementOffset](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 0. Valid values are [0, (Num Timeslots -1)].

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the offset, relative to the trigger of the timeslot to be measured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setnumberofanalysisthreads__string-int.html language=enus -->
## TOPIC 00171: SetNumberOfAnalysisThreads(string, int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setnumberofanalysisthreads__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setnumberofanalysisthreads__string-int.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources,

### SetNumberOfAnalysisThreads(string, int)

Sets the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetNumberOfAnalysisThreads(string selectorString, int value)

#### Remarks

This method sets the value of [ModAccNumberOfAnalysisThreads](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration.html language=enus -->
## TOPIC 00172: RFmxGsmMXModAccConfiguration Class

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the ModAcc measurement. Derives fromRFmxGsmMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic class RFmxGsmMXModAccConfiguration : RFmxGsmMXSubObjectMethodsNameDescriptionConfigureAveraging(string, RFmxGsmMXModAccAveragingEnabled, int)Configures averaging

### RFmxGsmMXModAccConfiguration Class

Provides methods to configure the ModAcc measurement.

#### Derives from

- RFmxGsmMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public class RFmxGsmMXModAccConfiguration : RFmxGsmMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| ConfigureAveraging(string, RFmxGsmMXModAccAveragingEnabled, int) | Configures averaging for the modulation accuracy (ModAcc) measurement. |
| ConfigureDroopCompensationEnabled(string, RFmxGsmMXModAccDroopCompensationEnabled) | Configures whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. |
| GetAllTracesEnabled(string, out bool) | Gets whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement. |
| GetAveragingCount(string, out int) | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxGsmMXModAccAveragingEnabled) method to True. |
| GetAveragingEnabled(string, out RFmxGsmMXModAccAveragingEnabled) | Gets whether to enable averaging for the modulation accuracy (ModAcc) measurement. |
| GetDroopCompensationEnabled(string, out RFmxGsmMXModAccDroopCompensationEnabled) | Gets whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results. |
| GetMeasurementEnabled(string, out bool) | Gets whether to enable modulation accuracy (ModAcc) measurements on the acquired signal. |
| GetMeasurementInterval(string, out RFmxGsmMXModAccMeasurementInterval) | Gets whether the measurement is performed on a single specified timeslot or across multiple timeslots. |
| GetMeasurementOffset(string, out int) | Gets the offset, relative to the trigger of the timeslot to be measured. |
| GetNumberOfAnalysisThreads(string, out int) | Gets the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| SetAllTracesEnabled(string, bool) | Sets whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement. |
| SetAveragingCount(string, int) | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxGsmMXModAccAveragingEnabled) method to True. |
| SetAveragingEnabled(string, RFmxGsmMXModAccAveragingEnabled) | Sets whether to enable averaging for the modulation accuracy (ModAcc) measurement. |
| SetDroopCompensationEnabled(string, RFmxGsmMXModAccDroopCompensationEnabled) | Sets whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable modulation accuracy (ModAcc) measurements on the acquired signal. |
| SetMeasurementInterval(string, RFmxGsmMXModAccMeasurementInterval) | Sets whether the measurement is performed on a single specified timeslot or across multiple timeslots. |
| SetMeasurementOffset(string, int) | Sets the offset, relative to the trigger of the timeslot to be measured. |
| SetNumberOfAnalysisThreads(string, int) | Sets the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccdetectedtsc.html language=enus -->
## TOPIC 00173: RFmxGsmMXModAccDetectedTsc Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccdetectedtsc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccdetectedtsc.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the detected training sequence code (TSC) if you set the SetBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType) method to Tsc. Use "slot(n)" as the selector string to read this result. When the SetMeasurementInterval(string, RFmxGsmMXModAccMeasurementInterval) method is set t

### RFmxGsmMXModAccDetectedTsc Enumeration

Returns the detected training sequence code (TSC) if you set the [SetBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setburstsynchronizationtype__string-rfmxgsmmxburstsynchronizationtype.html) method to [Tsc](nationalinstruments-rfmx-gsmmx-rfmxgsmmxburstsynchronizationtype.html). Use "slot(n)" as the selector string to read this result. When the [SetMeasurementInterval(string, RFmxGsmMXModAccMeasurementInterval)](nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setmeasurementinterval__string-rfmxgsmmxmodaccmeasurementinterval.html) method is set to [TimeslotAtOffset](nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccmeasurementinterval.html), Detected TSC array has one element and the Detected TSC is returned at index 0.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXModAccDetectedTsc

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Tsc0 | 0 | The detected TSC is TSC0. |
| Tsc1 | 1 | The detected TSC is TSC1. |
| Tsc2 | 2 | The detected TSC is TSC2. |
| Tsc3 | 3 | The detected TSC is TSC3. |
| Tsc4 | 4 | The detected TSC is TSC4. |
| Tsc5 | 5 | The detected TSC is TSC5. |
| Tsc6 | 6 | The detected TSC is TSC6. |
| Tsc7 | 7 | The detected TSC is TSC7. |
| Unknown | -1 | The synchronization is not found, and measurements correspond to best estimate of synchronization. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccdroopcompensationenabled.html language=enus -->
## TOPIC 00174: RFmxGsmMXModAccDroopCompensationEnabled Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccdroopcompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccdroopcompensationenabled.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXModAccD

### RFmxGsmMXModAccDroopCompensationEnabled Enumeration

Specifies whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXModAccDroopCompensationEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables power droop compensation in the EVM measurement. |
| True | 1 | Enables power droop compensation in the EVM measurement. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccmeasurementinterval.html language=enus -->
## TOPIC 00175: RFmxGsmMXModAccMeasurementInterval Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccmeasurementinterval.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccmeasurementinterval.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed on a single specified timeslot or across multiple timeslots. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXModAccMeasurementIntervalMembersNameValueDescriptionNumberOfTimeslots0The measurement includes all timeslots defined by the

### RFmxGsmMXModAccMeasurementInterval Enumeration

Specifies whether the measurement is performed on a single specified timeslot or across multiple timeslots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXModAccMeasurementInterval

#### Members

| Name | Value | Description |
| --- | --- | --- |
| NumberOfTimeslots | 0 | The measurement includes all timeslots defined by the SetNumberOfTimeslots(string, int) property. |
| TimeslotAtOffset | 1 | The measurement is performed only on the timeslot specified by the SetMeasurementOffset(string, int) method. This method is applicable only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge or DigitalEdge. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchconstellationtrace__string-double-ref.html language=enus -->
## TOPIC 00176: FetchConstellationTrace(string, double, ref ComplexSingle[])

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchconstellationtrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchconstellationtrace__string-double-ref.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the constellation trace concatenated over all the measured time slots for the last acquistion.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int FetchConstellationTrace(string selectorString, double timeout, ref ComplexSingle[] constellation)ParametersNameTypeDescriptionselectorString

### FetchConstellationTrace(string, double, ref ComplexSingle[])

Fetches the constellation trace concatenated over all the measured time slots for the last acquistion.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int FetchConstellationTrace(string selectorString, double timeout, ref ComplexSingle[] constellation)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| constellation | ref ComplexSingle[] | Upon return, contains the constellation trace concatenated over all the measured time slots for the last acquisition. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchdemodulatedbits__string-double-ref.html language=enus -->
## TOPIC 00177: FetchDemodulatedBits(string, double, ref sbyte[])

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchdemodulatedbits__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchdemodulatedbits__string-double-ref.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the array of demodulated bits concatenated over all the measured time slots for the last acquisition.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int FetchDemodulatedBits(string selectorString, double timeout, ref sbyte[] bits)ParametersNameTypeDescriptionselectorStringstringSpecifi

### FetchDemodulatedBits(string, double, ref sbyte[])

Fetches the array of demodulated bits concatenated over all the measured time slots for the last acquisition.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int FetchDemodulatedBits(string selectorString, double timeout, ref sbyte[] bits)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| bits | ref sbyte[] | Upon return, contains an array of demodulated bits concatenated over all the measured time slots for the last acquisition. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchdetectedtsc__string-double-out.html language=enus -->
## TOPIC 00178: FetchDetectedTsc(string, double, out RFmxGsmMXModAccDetectedTsc)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchdetectedtsc__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchdetectedtsc__string-double-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the detected training sequence code (TSC) of the last burst for GSM/EDGE/EGPRS. Use "slot(n)" as the selector string to read results from this method. When the SetMeasurementInterval(string, RFmxGsmMXModAccMeasurementInterval) method is set to TimeslotAtOffset, Detected TSC array has one ele

### FetchDetectedTsc(string, double, out RFmxGsmMXModAccDetectedTsc)

Fetches the detected training sequence code (TSC) of the last burst for GSM/EDGE/EGPRS. 
 Use "slot(n)" as the selector string to read results from this method. 
 When the [SetMeasurementInterval(string, RFmxGsmMXModAccMeasurementInterval)](nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setmeasurementinterval__string-rfmxgsmmxmodaccmeasurementinterval.html) method is set to [TimeslotAtOffset](nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccmeasurementinterval.html), Detected TSC array has one element and the Detected TSC is returned at index 0.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int FetchDetectedTsc(string selectorString, double timeout, out RFmxGsmMXModAccDetectedTsc detectedTsc)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and slot number. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "slot0" "result::r1/slot0" You can use the BuildSlotString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| detectedTsc | out RFmxGsmMXModAccDetectedTsc | Upon return, contains the detected TSC when you set the SetBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType) method to Tsc. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchdetectedtscarray__string-double-ref.html language=enus -->
## TOPIC 00179: FetchDetectedTscArray(string, double, ref RFmxGsmMXModAccDetectedTsc[])

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchdetectedtscarray__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchdetectedtscarray__string-double-ref.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the detected training sequence code (TSC) of the last acquisition for GSM/EDGE/EGPRS. When the SetMeasurementInterval(string, RFmxGsmMXModAccMeasurementInterval) method is set to TimeslotAtOffset, Detected TSC array has one element and the Detected TSC is returned at index 0.SyntaxNamespace:

### FetchDetectedTscArray(string, double, ref RFmxGsmMXModAccDetectedTsc[])

Fetches the detected training sequence code (TSC) of the last acquisition for GSM/EDGE/EGPRS. 
 When the [SetMeasurementInterval(string, RFmxGsmMXModAccMeasurementInterval)](nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setmeasurementinterval__string-rfmxgsmmxmodaccmeasurementinterval.html) method is set to [TimeslotAtOffset](nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccmeasurementinterval.html), Detected TSC array has one element and the Detected TSC is returned at index 0.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int FetchDetectedTscArray(string selectorString, double timeout, ref RFmxGsmMXModAccDetectedTsc[] detectedTsc)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| detectedTsc | ref RFmxGsmMXModAccDetectedTsc[] | Upon return, contains an array of the detected TSCs when you set the SetBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType) method to Tsc. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchevm__string-double-out-out-out-out-out-out-out.html language=enus -->
## TOPIC 00180: FetchEvm(string, double, out double, out double, out double, out double, out double, out double, out int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchevm__string-double-out-out-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchevm__string-double-out-out-out-out-out-out-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EVM measurement results for EDGE/EGPRS. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int FetchEvm(string selectorString, double timeout, out double meanRmsEvm, out double maximumRmsEvm, out double meanPeakEvm, out double maximumPeakEvm, out double ninetyFifthPercentileEvm, out d

### FetchEvm(string, double, out double, out double, out double, out double, out double, out double, out int)

Fetches the EVM measurement results for EDGE/EGPRS.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int FetchEvm(string selectorString, double timeout, out double meanRmsEvm, out double maximumRmsEvm, out double meanPeakEvm, out double maximumPeakEvm, out double ninetyFifthPercentileEvm, out double meanFrequencyError, out int peakEvmSymbol)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| meanRmsEvm | out double | Upon return, contains the mean of RMS EVM values over all the measured time slots. This value is expressed as a percentage. |
| maximumRmsEvm | out double | Upon return, contains the maximum of RMS EVM values over all the measured time slots. This value is expressed as a percentage. |
| meanPeakEvm | out double | Upon return, contains the mean of peak EVM values over all the measured time slots. This value is expressed as a percentage. |
| maximumPeakEvm | out double | Upon return, contains the maximum of peak EVM values over all the measured time slots. This value is expressed as a percentage. |
| ninetyFifthPercentileEvm | out double | Upon return, contains the EVM value, at which no more than 5 percent of the symbols have an EVM exceeding this value. This value is expressed as a percentage. |
| meanFrequencyError | out double | Upon return, contains the mean of frequency error values over all the measured time slots. This value is expressed in Hz. |
| peakEvmSymbol | out int | Upon return, contains the symbol number in the burst measurement interval corresponding to the EVM value returned by the maximumPeakEVM parameter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchevmamplitudedroop__string-double-out-out.html language=enus -->
## TOPIC 00181: FetchEvmAmplitudeDroop(string, double, out double, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchevmamplitudedroop__string-double-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchevmamplitudedroop__string-double-out-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the amplitude droop measurement results for EDGE/EGPRS.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int FetchEvmAmplitudeDroop(string selectorString, double timeout, out double meanAmplitudeDroop, out double maximumAmplitudeDroop)ParametersNameTypeDescriptionselectorStringstringSpec

### FetchEvmAmplitudeDroop(string, double, out double, out double)

Fetches the amplitude droop measurement results for EDGE/EGPRS.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int FetchEvmAmplitudeDroop(string selectorString, double timeout, out double meanAmplitudeDroop, out double maximumAmplitudeDroop)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| meanAmplitudeDroop | out double | Upon return, contains the mean of amplitude droop values over all the measured time slots. This value is expressed in dB/symbol. |
| maximumAmplitudeDroop | out double | Upon return, contains the maximum of amplitude droop values over all the measured time slots. This value is expressed in dB/symbol. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchevmmagnitudeerror__string-double-out-out.html language=enus -->
## TOPIC 00182: FetchEvmMagnitudeError(string, double, out double, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchevmmagnitudeerror__string-double-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchevmmagnitudeerror__string-double-out-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the RMS values of the magnitude error measurement results for EDGE/EGPRS.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int FetchEvmMagnitudeError(string selectorString, double timeout, out double meanMagnitudeError, out double maximumMagnitudeError)ParametersNameTypeDescriptionselect

### FetchEvmMagnitudeError(string, double, out double, out double)

Fetches the RMS values of the magnitude error measurement results for EDGE/EGPRS.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int FetchEvmMagnitudeError(string selectorString, double timeout, out double meanMagnitudeError, out double maximumMagnitudeError)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| meanMagnitudeError | out double | Upon return, contains the mean of magnitude error values over all the measured time slots. This value is expressed as a percentage. |
| maximumMagnitudeError | out double | Upon return, contains the maximum of magnitude error values over all the measured time slots. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchevmphaseerror__string-double-out-out.html language=enus -->
## TOPIC 00183: FetchEvmPhaseError(string, double, out double, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchevmphaseerror__string-double-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchevmphaseerror__string-double-out-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase error measurement results for EDGE/EGPRS.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int FetchEvmPhaseError(string selectorString, double timeout, out double meanPhaseError, out double maximumPhaseError)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector

### FetchEvmPhaseError(string, double, out double, out double)

Fetches the phase error measurement results for EDGE/EGPRS.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int FetchEvmPhaseError(string selectorString, double timeout, out double meanPhaseError, out double maximumPhaseError)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| meanPhaseError | out double | Upon return, contains the mean of phase error values over all the measured time slots. This value is expressed in degrees. |
| maximumPhaseError | out double | Upon return, contains the maximum of phase error values over all the measured time slots. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchevmtrace__string-double-ref.html language=enus -->
## TOPIC 00184: FetchEvmTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchevmtrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchevmtrace__string-double-ref.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EDGE/EGPRS RMS EVM trace concatenated over all the measured time slots for the last acquisition.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int FetchEvmTrace(string selectorString, double timeout, ref AnalogWaveform< float > evm)ParametersNameTypeDescriptionselectorStringstring

### FetchEvmTrace(string, double, ref AnalogWaveform< float >)

Fetches the EDGE/EGPRS RMS EVM trace concatenated over all the measured time slots for the last acquisition.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int FetchEvmTrace(string selectorString, double timeout, ref AnalogWaveform< float > evm)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| evm | ref AnalogWaveform< float > | Upon return, contains the EVM trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchiqimpairments__string-double-out-out-out-out.html language=enus -->
## TOPIC 00185: FetchIQImpairments(string, double, out double, out double, out double, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchiqimpairments__string-double-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchiqimpairments__string-double-out-out-out-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the origin offset and gain imbalance measurement results for GSM/EDGE/EGPRS.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int FetchIQImpairments(string selectorString, double timeout, out double meanIQGainImbalance, out double maximumIQGainImbalance, out double meanIQOriginOffset, ou

### FetchIQImpairments(string, double, out double, out double, out double, out double)

Fetches the origin offset and gain imbalance measurement results for GSM/EDGE/EGPRS.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int FetchIQImpairments(string selectorString, double timeout, out double meanIQGainImbalance, out double maximumIQGainImbalance, out double meanIQOriginOffset, out double maximumIQOriginOffset)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| meanIQGainImbalance | out double | Upon return, contains the mean of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. |
| maximumIQGainImbalance | out double | Upon return, contains the maximum of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. |
| meanIQOriginOffset | out double | Upon return, contains the mean of I/Q origin offset values over all the measured time slots. This value is expressed in dB. Presence of I/Q gain imbalance in the signal affects the I/Q origin offset measurement. The measurement returns this result for GSM/EDGE/EGPRS. |
| maximumIQOriginOffset | out double | Upon return, contains the maximum of I/Q origin offset values over all the measured time slots. This value is expressed in dB. Presence of I/Q gain imbalance in the signal affects the I/Q origin offset measurement. The measurement returns this result for GSM/EDGE/EGPRS. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchmagnitudeerrortrace__string-double-ref.html language=enus -->
## TOPIC 00186: FetchMagnitudeErrorTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchmagnitudeerrortrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchmagnitudeerrortrace__string-double-ref.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EDGE/EGPRS magnitude error trace concatenated over all the measured time slots for the last acquisition.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int FetchMagnitudeErrorTrace(string selectorString, double timeout, ref AnalogWaveform< float > magnitudeError)ParametersNameTypeD

### FetchMagnitudeErrorTrace(string, double, ref AnalogWaveform< float >)

Fetches the EDGE/EGPRS magnitude error trace concatenated over all the measured time slots for the last acquisition.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int FetchMagnitudeErrorTrace(string selectorString, double timeout, ref AnalogWaveform< float > magnitudeError)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| magnitudeError | ref AnalogWaveform< float > | Upon return, contains the magnitude error trace. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchpfer__string-double-out-out-out-out-out-out.html language=enus -->
## TOPIC 00187: FetchPfer(string, double, out double, out double, out double, out double, out double, out int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchpfer__string-double-out-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchpfer__string-double-out-out-out-out-out-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase and frequency error measurement results for GSM.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int FetchPfer(string selectorString, double timeout, out double meanRmsPhaseError, out double maximumRmsPhaseError, out double meanPeakPhaseError, out double maximumPeakPhaseError,

### FetchPfer(string, double, out double, out double, out double, out double, out double, out int)

Fetches the phase and frequency error measurement results for GSM.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int FetchPfer(string selectorString, double timeout, out double meanRmsPhaseError, out double maximumRmsPhaseError, out double meanPeakPhaseError, out double maximumPeakPhaseError, out double meanFrequencyError, out int peakSymbol)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| meanRmsPhaseError | out double | Upon return, contains the mean of RMS phase error values over all the measured time slots. This value is expressed in degrees. |
| maximumRmsPhaseError | out double | Upon return, contains the maximum of RMS phase error values over all the measured time slots. This value is expressed in degrees. |
| meanPeakPhaseError | out double | Upon return, contains the mean of peak phase error values over all the measured time slots. This value is expressed in degrees. |
| maximumPeakPhaseError | out double | Upon return, contains the maximum of peak phase error values over all the measured time slots. This value is expressed in degrees. |
| meanFrequencyError | out double | Upon return, contains the mean of frequency error values over all the measured time slots. This value is expressed in Hz. |
| peakSymbol | out int | Upon return, contains the symbol number in the useful portion of the burst corresponding to phase error value in the maximumPeakPhaseError parameter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchphaseerrortrace__string-double-ref.html language=enus -->
## TOPIC 00188: FetchPhaseErrorTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchphaseerrortrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-fetchphaseerrortrace__string-double-ref.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase error trace concatenated over all the measured time slots for the last acquisition.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int FetchPhaseErrorTrace(string selectorString, double timeout, ref AnalogWaveform< float > phaseError)ParametersNameTypeDescriptionselectorStrin

### FetchPhaseErrorTrace(string, double, ref AnalogWaveform< float >)

Fetches the phase error trace concatenated over all the measured time slots for the last acquisition.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int FetchPhaseErrorTrace(string selectorString, double timeout, ref AnalogWaveform< float > phaseError)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| phaseError | ref AnalogWaveform< float > | Upon return, contains the phase error trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getdetectedtsc__string-out.html language=enus -->
## TOPIC 00189: GetDetectedTsc(string, out RFmxGsmMXModAccDetectedTsc)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getdetectedtsc__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getdetectedtsc__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the detected training sequence code (TSC) if you set the SetBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType) method to Tsc. Use "slot(n)" as the selector string to read this result. When the SetMeasurementInterval(string, RFmxGsmMXModAccMeasurementInterval) method is set to T

### GetDetectedTsc(string, out RFmxGsmMXModAccDetectedTsc)

Gets the detected training sequence code (TSC) if you set the [SetBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setburstsynchronizationtype__string-rfmxgsmmxburstsynchronizationtype.html) method to [Tsc](nationalinstruments-rfmx-gsmmx-rfmxgsmmxburstsynchronizationtype.html). Use "slot(n)" as the selector string to read this result. When the [SetMeasurementInterval(string, RFmxGsmMXModAccMeasurementInterval)](nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccconfiguration-setmeasurementinterval__string-rfmxgsmmxmodaccmeasurementinterval.html) method is set to [TimeslotAtOffset](nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccmeasurementinterval.html), Detected TSC array has one element and the Detected TSC is returned at index 0.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetDetectedTsc(string selectorString, out RFmxGsmMXModAccDetectedTsc value)

#### Remarks

This method gets the value of [ModAccResultsDetectedTsc](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Slot number. Example: "Slot0", "result::r1/Slot0". You can use the BuildSlotString(string, int) method to build the selector string. |
| value | out RFmxGsmMXModAccDetectedTsc | Upon return, contains the detected training sequence code (TSC) if you set the SetBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType) method to Tsc. Use "slot(n)" as the selector string to read this result. When the SetMeasurementInterval(string, RFmxGsmMXModAccMeasurementInterval) method is set to TimeslotAtOffset, Detected TSC array has one element and the Detected TSC is returned at index 0. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevm95thpercentileevm__string-out.html language=enus -->
## TOPIC 00190: GetEvm95thPercentileEvm(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevm95thpercentileevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevm95thpercentileevm__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the EVM value at which no more than 5% of the symbols have an EVM exceeding this value. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetEvm95thPercentileEvm(string selectorString, o

### GetEvm95thPercentileEvm(string, out double)

Gets the EVM value at which no more than 5% of the symbols have an EVM exceeding this value. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetEvm95thPercentileEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsEvm95thPercentileEvm](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the EVM value at which no more than 5% of the symbols have an EVM exceeding this value. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevm95thpercentilemagnitudeerror__string-out.html language=enus -->
## TOPIC 00191: GetEvm95thPercentileMagnitudeError(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevm95thpercentilemagnitudeerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevm95thpercentilemagnitudeerror__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measured magnitude error value multiplied by 100, at which, no more than 5 percent of the symbols have magnitude error exceeding this value. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage. SyntaxNamespace: NationalInstrum

### GetEvm95thPercentileMagnitudeError(string, out double)

Returns the measured magnitude error value multiplied by 100, at which, no more than 5 percent of the symbols have magnitude error exceeding this value. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetEvm95thPercentileMagnitudeError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsEvm95thPercentileMagnitudeError](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevm95thpercentilephaseerror__string-out.html language=enus -->
## TOPIC 00192: GetEvm95thPercentilePhaseError(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevm95thpercentilephaseerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevm95thpercentilephaseerror__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the measured phase error value multiplied by 100, at which, no more than 5 percent of the symbols have phase error exceeding this value. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees. SyntaxNamespace: NationalInstruments.RFmx.GsmMXp

### GetEvm95thPercentilePhaseError(string, out double)

Gets the measured phase error value multiplied by 100, at which, no more than 5 percent of the symbols have phase error exceeding this value. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetEvm95thPercentilePhaseError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsEvm95thPercentilePhaseError](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmaximumamplitudedroop__string-out.html language=enus -->
## TOPIC 00193: GetEvmMaximumAmplitudeDroop(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmaximumamplitudedroop__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmaximumamplitudedroop__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum of the amplitude droop values over all the measured time slots. This value is expressed in dB/symbol. The method returns this result for EDGE/EGPRS measurements. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetEvmMaximumAmplitudeDroop(string selectorString, out double v

### GetEvmMaximumAmplitudeDroop(string, out double)

Gets the maximum of the amplitude droop values over all the measured time slots. This value is expressed in dB/symbol. The method returns this result for EDGE/EGPRS measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetEvmMaximumAmplitudeDroop(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsEvmMaximumAmplitudeDroop](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum of the amplitude droop values over all the measured time slots. This value is expressed in dB/symbol. The method returns this result for EDGE/EGPRS measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmaximumfrequencyerror__string-out.html language=enus -->
## TOPIC 00194: GetEvmMaximumFrequencyError(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmaximumfrequencyerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmaximumfrequencyerror__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum of the frequency error values over all the measured time slots. This value is expressed in Hz. The method returns this result for EDGE/EGPRS measurements. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetEvmMaximumFrequencyError(string selectorString, out double value)Re

### GetEvmMaximumFrequencyError(string, out double)

Gets the maximum of the frequency error values over all the measured time slots. This value is expressed in Hz. The method returns this result for EDGE/EGPRS measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetEvmMaximumFrequencyError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsEvmMaximumFrequencyError](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum of the frequency error values over all the measured time slots. This value is expressed in Hz. The method returns this result for EDGE/EGPRS measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmaximummagnitudeerror__string-out.html language=enus -->
## TOPIC 00195: GetEvmMaximumMagnitudeError(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmaximummagnitudeerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmaximummagnitudeerror__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum of the RMS values of magnitude error over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetEvmMaximumMagnitudeError(string selectorString, ou

### GetEvmMaximumMagnitudeError(string, out double)

Gets the maximum of the RMS values of magnitude error over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetEvmMaximumMagnitudeError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsEvmMaximumMagnitudeError](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum of the magnitude error values over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmaximumpeakevm__string-out.html language=enus -->
## TOPIC 00196: GetEvmMaximumPeakEvm(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmaximumpeakevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmaximumpeakevm__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum of the peak EVM values over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetEvmMaximumPeakEvm(string selectorString, out double value)Remark

### GetEvmMaximumPeakEvm(string, out double)

Gets the maximum of the peak EVM values over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetEvmMaximumPeakEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsEvmMaximumPeakEvm](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum of the peak EVM values over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmaximumpeakmagnitudeerror__string-out.html language=enus -->
## TOPIC 00197: GetEvmMaximumPeakMagnitudeError(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmaximumpeakmagnitudeerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmaximumpeakmagnitudeerror__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum of peak magnitude error over all the measured time slots. This method is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetEvmMaximumPeakMagnitudeError(string selectorStrin

### GetEvmMaximumPeakMagnitudeError(string, out double)

Gets the maximum of peak magnitude error over all the measured time slots. This method is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetEvmMaximumPeakMagnitudeError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsEvmMaximumPeakMagnitudeError](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmaximumpeakphaseerror__string-out.html language=enus -->
## TOPIC 00198: GetEvmMaximumPeakPhaseError(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmaximumpeakphaseerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmaximumpeakphaseerror__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum of peak phase error measured over all the measured time slots. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetEvmMaximumPeakPhaseError(string selectorString, o

### GetEvmMaximumPeakPhaseError(string, out double)

Gets the maximum of peak phase error measured over all the measured time slots. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetEvmMaximumPeakPhaseError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsEvmMaximumPeakPhaseError](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmaximumphaseerror__string-out.html language=enus -->
## TOPIC 00199: GetEvmMaximumPhaseError(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmaximumphaseerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmaximumphaseerror__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum of the RMS values of phase error values over all the measured time slots. This value is expressed in degrees. The method returns this result for EDGE/EGPRS measurements. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetEvmMaximumPhaseError(string selectorString, out doub

### GetEvmMaximumPhaseError(string, out double)

Gets the maximum of the RMS values of phase error values over all the measured time slots. This value is expressed in degrees. The method returns this result for EDGE/EGPRS measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetEvmMaximumPhaseError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsEvmMaximumPhaseError](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum of the phase error values over all the measured time slots. This value is expressed in degrees. The method returns this result for EDGE/EGPRS measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmaximumrmsevm__string-out.html language=enus -->
## TOPIC 00200: GetEvmMaximumRmsEvm(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmaximumrmsevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmaximumrmsevm__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum of the RMS EVM values over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetEvmMaximumRmsEvm(string selectorString, out double value)RemarksT

### GetEvmMaximumRmsEvm(string, out double)

Gets the maximum of the RMS EVM values over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetEvmMaximumRmsEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsEvmMaximumRmsEvm](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum of the RMS EVM values over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmeanamplitudedroop__string-out.html language=enus -->
## TOPIC 00201: GetEvmMeanAmplitudeDroop(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmeanamplitudedroop__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmeanamplitudedroop__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the amplitude droop values over all the measured time slots. This value is expressed in dB/symbol. The method returns this result for EDGE/EGPRS measurements. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetEvmMeanAmplitudeDroop(string selectorString, out double value)R

### GetEvmMeanAmplitudeDroop(string, out double)

Gets the mean of the amplitude droop values over all the measured time slots. This value is expressed in dB/symbol. The method returns this result for EDGE/EGPRS measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetEvmMeanAmplitudeDroop(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsEvmMeanAmplitudeDroop](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the amplitude droop values over all the measured time slots. This value is expressed in dB/symbol. The method returns this result for EDGE/EGPRS measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmeanfrequencyerror__string-out.html language=enus -->
## TOPIC 00202: GetEvmMeanFrequencyError(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmeanfrequencyerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmeanfrequencyerror__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the frequency error values over all the measured time slots. This value is expressed in Hz. The method returns this result for EDGE/EGPRS measurements. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetEvmMeanFrequencyError(string selectorString, out double value)RemarksT

### GetEvmMeanFrequencyError(string, out double)

Gets the mean of the frequency error values over all the measured time slots. This value is expressed in Hz. The method returns this result for EDGE/EGPRS measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetEvmMeanFrequencyError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsEvmMeanFrequencyError](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the frequency error values over all the measured time slots. This value is expressed in Hz. The method returns this result for EDGE/EGPRS measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmeanmagnitudeerror__string-out.html language=enus -->
## TOPIC 00203: GetEvmMeanMagnitudeError(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmeanmagnitudeerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmeanmagnitudeerror__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the RMS values of magnitude error over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetEvmMeanMagnitudeError(string selectorString, out doub

### GetEvmMeanMagnitudeError(string, out double)

Gets the mean of the RMS values of magnitude error over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetEvmMeanMagnitudeError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsEvmMeanMagnitudeError](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the magnitude error values over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmeanpeakevm__string-out.html language=enus -->
## TOPIC 00204: GetEvmMeanPeakEvm(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmeanpeakevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmeanpeakevm__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the peak EVM values over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetEvmMeanPeakEvm(string selectorString, out double value)RemarksThis

### GetEvmMeanPeakEvm(string, out double)

Gets the mean of the peak EVM values over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetEvmMeanPeakEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsEvmMeanPeakEvm](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the peak EVM values over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmeanpeakmagnitudeerror__string-out.html language=enus -->
## TOPIC 00205: GetEvmMeanPeakMagnitudeError(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmeanpeakmagnitudeerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmeanpeakmagnitudeerror__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of peak magnitude error over all the measured time slots. This method is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetEvmMeanPeakMagnitudeError(string selectorString,

### GetEvmMeanPeakMagnitudeError(string, out double)

Returns the mean of peak magnitude error over all the measured time slots. This method is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetEvmMeanPeakMagnitudeError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsEvmMeanPeakMagnitudeError](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmeanpeakphaseerror__string-out.html language=enus -->
## TOPIC 00206: GetEvmMeanPeakPhaseError(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmeanpeakphaseerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmeanpeakphaseerror__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of peak phase error over all the measured time slots. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetEvmMeanPeakPhaseError(string selectorString, out double value

### GetEvmMeanPeakPhaseError(string, out double)

Gets the mean of peak phase error over all the measured time slots. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetEvmMeanPeakPhaseError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsEvmMeanPeakPhaseError](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmeanphaseerror__string-out.html language=enus -->
## TOPIC 00207: GetEvmMeanPhaseError(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmeanphaseerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmeanphaseerror__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the RMS values of phase error values over all the measured time slots. This value is expressed in degrees. The method returns this result for EDGE/EGPRS measurements. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetEvmMeanPhaseError(string selectorString, out double val

### GetEvmMeanPhaseError(string, out double)

Gets the mean of the RMS values of phase error values over all the measured time slots. This value is expressed in degrees. The method returns this result for EDGE/EGPRS measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetEvmMeanPhaseError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsEvmMeanPhaseError](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the phase error values over all the measured time slots. This value is expressed in degrees. The method returns this result for EDGE/EGPRS measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmeanrmsevm__string-out.html language=enus -->
## TOPIC 00208: GetEvmMeanRmsEvm(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmeanrmsevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmeanrmsevm__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the RMS EVM values over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetEvmMeanRmsEvm(string selectorString, out double value)RemarksThis me

### GetEvmMeanRmsEvm(string, out double)

Gets the mean of the RMS EVM values over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetEvmMeanRmsEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsEvmMeanRmsEvm](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the RMS EVM values over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmpeakevmsymbol__string-out.html language=enus -->
## TOPIC 00209: GetEvmPeakEvmSymbol(string, out int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmpeakevmsymbol__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmpeakevmsymbol__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the symbol number in the burst measurement interval that corresponds to the EVM value returned by the GetEvmMaximumPeakEvm(string, out double) result. The method returns this result for EDGE/EGPRS measurements. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetEvmPeakEvmSymbol(string

### GetEvmPeakEvmSymbol(string, out int)

Gets the symbol number in the burst measurement interval that corresponds to the EVM value returned by the [GetEvmMaximumPeakEvm(string, out double)](nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getevmmaximumpeakevm__string-out.html) result. The method returns this result for EDGE/EGPRS measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetEvmPeakEvmSymbol(string selectorString, out int value)

#### Remarks

This method gets the value of [ModAccResultsEvmPeakEvmSymbol](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out int | Upon return, contains the symbol number in the burst measurement interval that corresponds to the EVM value returned by the GetEvmMaximumPeakEvm(string, out double) result. The method returns this result for EDGE/EGPRS measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getmaximumiqgainimbalance__string-out.html language=enus -->
## TOPIC 00210: GetMaximumIQGainImbalance(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getmaximumiqgainimbalance__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getmaximumiqgainimbalance__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetMaximumIQGainImbalance(string selec

### GetMaximumIQGainImbalance(string, out double)

Gets the maximum of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetMaximumIQGainImbalance(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsMaximumIQGainImbalance](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getmaximumiqoriginoffset__string-out.html language=enus -->
## TOPIC 00211: GetMaximumIQOriginOffset(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getmaximumiqoriginoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getmaximumiqoriginoffset__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum of the I/Q origin offset values over all the measured time slots. This value is expressed in dB. Presence of I/Q gain imbalance in the signal affects the I/Q origin offset measurement. The method returns this result for GSM/EDGE/EGPRS measurements. SyntaxNamespace: NationalInstrumen

### GetMaximumIQOriginOffset(string, out double)

Gets the maximum of the I/Q origin offset values over all the measured time slots. This value is expressed in dB. Presence of I/Q gain imbalance in the signal affects the I/Q origin offset measurement. The method returns this result for GSM/EDGE/EGPRS measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetMaximumIQOriginOffset(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsMaximumIQOriginOffset](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum of the I/Q origin offset values over all the measured time slots. This value is expressed in dB. Presence of I/Q gain imbalance in the signal affects the I/Q origin offset measurement. The method returns this result for GSM/EDGE/EGPRS measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getmeaniqgainimbalance__string-out.html language=enus -->
## TOPIC 00212: GetMeanIQGainImbalance(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getmeaniqgainimbalance__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getmeaniqgainimbalance__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetMeanIQGainImbalance(string selectorStr

### GetMeanIQGainImbalance(string, out double)

Gets the mean of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetMeanIQGainImbalance(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsMeanIQGainImbalance](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getmeaniqoriginoffset__string-out.html language=enus -->
## TOPIC 00213: GetMeanIQOriginOffset(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getmeaniqoriginoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getmeaniqoriginoffset__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the I/Q origin offset values over all the measured time slots. This value is expressed in dB. Presence of I/Q gain imbalance in the signal affects the I/Q origin offset measurement. The method returns this result for GSM/EDGE/EGPRS measurements. SyntaxNamespace: NationalInstruments.

### GetMeanIQOriginOffset(string, out double)

Gets the mean of the I/Q origin offset values over all the measured time slots. This value is expressed in dB. Presence of I/Q gain imbalance in the signal affects the I/Q origin offset measurement. The method returns this result for GSM/EDGE/EGPRS measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetMeanIQOriginOffset(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsMeanIQOriginOffset](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the I/Q origin offset values over all the measured time slots. This value is expressed in dB. Presence of I/Q gain imbalance in the signal affects the I/Q origin offset measurement. The method returns this result for GSM/EDGE/EGPRS measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getpfer95thpercentilephaseerror__string-out.html language=enus -->
## TOPIC 00214: GetPfer95thPercentilePhaseError(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getpfer95thpercentilephaseerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getpfer95thpercentilephaseerror__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the measured phase error value multiplied by 100, at which, no more than 5 percent of the symbols have phase error exceeding this value. This result is returned while performing ModAcc measurement on GSM. This value is measured in degrees. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic i

### GetPfer95thPercentilePhaseError(string, out double)

Gets the measured phase error value multiplied by 100, at which, no more than 5 percent of the symbols have phase error exceeding this value. This result is returned while performing ModAcc measurement on GSM. This value is measured in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetPfer95thPercentilePhaseError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsPfer95thPercentilePhaseError](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getpfermaximumfrequencyerror__string-out.html language=enus -->
## TOPIC 00215: GetPferMaximumFrequencyError(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getpfermaximumfrequencyerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getpfermaximumfrequencyerror__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum of the frequency error values over all the measured time slots. This value is expressed in Hz. The method returns this result for GSM ModAcc measurements. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetPferMaximumFrequencyError(string selectorString, out double value)R

### GetPferMaximumFrequencyError(string, out double)

Gets the maximum of the frequency error values over all the measured time slots. This value is expressed in Hz. The method returns this result for GSM ModAcc measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetPferMaximumFrequencyError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsPferMaximumFrequencyError](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum of the frequency error values over all the measured time slots. This value is expressed in Hz. The method returns this result for GSM ModAcc measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getpfermaximumpeakphaseerror__string-out.html language=enus -->
## TOPIC 00216: GetPferMaximumPeakPhaseError(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getpfermaximumpeakphaseerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getpfermaximumpeakphaseerror__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum of peak phase error values over all the measured time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetPferMaximumPeakPhaseError(string selectorString, out double value

### GetPferMaximumPeakPhaseError(string, out double)

Gets the maximum of peak phase error values over all the measured time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetPferMaximumPeakPhaseError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsPferMaximumPeakPhaseError](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum of the peak phase error values over all the measured time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getpfermaximumrmsphaseerror__string-out.html language=enus -->
## TOPIC 00217: GetPferMaximumRmsPhaseError(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getpfermaximumrmsphaseerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getpfermaximumrmsphaseerror__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum of the RMS phase error values over all the measured time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetPferMaximumRmsPhaseError(string selectorString, out double val

### GetPferMaximumRmsPhaseError(string, out double)

Gets the maximum of the RMS phase error values over all the measured time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetPferMaximumRmsPhaseError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsPferMaximumRmsPhaseError](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the maximum of the RMS phase error values over all the measured time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getpfermeanfrequencyerror__string-out.html language=enus -->
## TOPIC 00218: GetPferMeanFrequencyError(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getpfermeanfrequencyerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getpfermeanfrequencyerror__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the frequency error values over all the measured time slots. This value is expressed in Hz. The method returns this result for GSM ModAcc measurements. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetPferMeanFrequencyError(string selectorString, out double value)Remarks

### GetPferMeanFrequencyError(string, out double)

Gets the mean of the frequency error values over all the measured time slots. This value is expressed in Hz. The method returns this result for GSM ModAcc measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetPferMeanFrequencyError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsPferMeanFrequencyError](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the frequency error values over all the measured time slots. This value is expressed in Hz. The method returns this result for GSM ModAcc measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getpfermeanpeakphaseerror__string-out.html language=enus -->
## TOPIC 00219: GetPferMeanPeakPhaseError(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getpfermeanpeakphaseerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getpfermeanpeakphaseerror__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of peak phase error values over all the measured time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetPferMeanPeakPhaseError(string selectorString, out double value)Remar

### GetPferMeanPeakPhaseError(string, out double)

Gets the mean of peak phase error values over all the measured time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetPferMeanPeakPhaseError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsPferMeanPeakPhaseError](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the peak phase error values over all the measured time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getpfermeanrmsphaseerror__string-out.html language=enus -->
## TOPIC 00220: GetPferMeanRmsPhaseError(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getpfermeanrmsphaseerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getpfermeanrmsphaseerror__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean of the RMS phase error values over all the measured time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetPferMeanRmsPhaseError(string selectorString, out double value)Rem

### GetPferMeanRmsPhaseError(string, out double)

Gets the mean of the RMS phase error values over all the measured time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetPferMeanRmsPhaseError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsPferMeanRmsPhaseError](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the mean of the RMS phase error values over all the measured time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getpferpeakphaseerrorsymbol__string-out.html language=enus -->
## TOPIC 00221: GetPferPeakPhaseErrorSymbol(string, out int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getpferpeakphaseerrorsymbol__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getpferpeakphaseerrorsymbol__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the symbol number in the useful portion of the burst corresponding to the phase error value in the GetPferMaximumPeakPhaseError(string, out double) result. The method returns this result for GSM ModAcc measurements. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetPferPeakPhaseError

### GetPferPeakPhaseErrorSymbol(string, out int)

Gets the symbol number in the useful portion of the burst corresponding to the phase error value in the [GetPferMaximumPeakPhaseError(string, out double)](nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults-getpfermaximumpeakphaseerror__string-out.html) result. The method returns this result for GSM ModAcc measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetPferPeakPhaseErrorSymbol(string selectorString, out int value)

#### Remarks

This method gets the value of [ModAccResultsPferPeakPhaseErrorSymbol](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out int | Upon return, contains the symbol number in the useful portion of the burst corresponding to the phase error value in the GetPferMaximumPeakPhaseError(string, out double) result. The method returns this result for GSM ModAcc measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXModAccResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults.html language=enus -->
## TOPIC 00222: RFmxGsmMXModAccResults Class

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodaccresults.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the ModAcc measurement results. Derives fromRFmxGsmMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic class RFmxGsmMXModAccResults : RFmxGsmMXSubObjectMethodsNameDescriptionFetchConstellationTrace(string, double, ref ComplexSingle[])Fetches the conste

### RFmxGsmMXModAccResults Class

Provides methods to fetch and read the ModAcc measurement results.

#### Derives from

- RFmxGsmMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public class RFmxGsmMXModAccResults : RFmxGsmMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchConstellationTrace(string, double, ref ComplexSingle[]) | Fetches the constellation trace concatenated over all the measured time slots for the last acquistion. |
| FetchDemodulatedBits(string, double, ref sbyte[]) | Fetches the array of demodulated bits concatenated over all the measured time slots for the last acquisition. |
| FetchDetectedTsc(string, double, out RFmxGsmMXModAccDetectedTsc) | Fetches the detected training sequence code (TSC) of the last burst for GSM/EDGE/EGPRS. Use "slot(n)" as the selector string to read results from this method. When the SetMeasurementInterval(string, RFmxGsmMXModAccMeasurementInterval) method is set to TimeslotAtOffset, Detected TSC array has one element and the Detected TSC is returned at index 0. |
| FetchDetectedTscArray(string, double, ref RFmxGsmMXModAccDetectedTsc[]) | Fetches the detected training sequence code (TSC) of the last acquisition for GSM/EDGE/EGPRS. When the SetMeasurementInterval(string, RFmxGsmMXModAccMeasurementInterval) method is set to TimeslotAtOffset, Detected TSC array has one element and the Detected TSC is returned at index 0. |
| FetchEvm(string, double, out double, out double, out double, out double, out double, out double, out int) | Fetches the EVM measurement results for EDGE/EGPRS. |
| FetchEvmAmplitudeDroop(string, double, out double, out double) | Fetches the amplitude droop measurement results for EDGE/EGPRS. |
| FetchEvmMagnitudeError(string, double, out double, out double) | Fetches the RMS values of the magnitude error measurement results for EDGE/EGPRS. |
| FetchEvmPhaseError(string, double, out double, out double) | Fetches the phase error measurement results for EDGE/EGPRS. |
| FetchEvmTrace(string, double, ref AnalogWaveform< float >) | Fetches the EDGE/EGPRS RMS EVM trace concatenated over all the measured time slots for the last acquisition. |
| FetchIQImpairments(string, double, out double, out double, out double, out double) | Fetches the origin offset and gain imbalance measurement results for GSM/EDGE/EGPRS. |
| FetchMagnitudeErrorTrace(string, double, ref AnalogWaveform< float >) | Fetches the EDGE/EGPRS magnitude error trace concatenated over all the measured time slots for the last acquisition. |
| FetchPfer(string, double, out double, out double, out double, out double, out double, out int) | Fetches the phase and frequency error measurement results for GSM. |
| FetchPhaseErrorTrace(string, double, ref AnalogWaveform< float >) | Fetches the phase error trace concatenated over all the measured time slots for the last acquisition. |
| GetDetectedTsc(string, out RFmxGsmMXModAccDetectedTsc) | Gets the detected training sequence code (TSC) if you set the SetBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType) method to Tsc. Use "slot(n)" as the selector string to read this result. When the SetMeasurementInterval(string, RFmxGsmMXModAccMeasurementInterval) method is set to TimeslotAtOffset, Detected TSC array has one element and the Detected TSC is returned at index 0. |
| GetEvm95thPercentileEvm(string, out double) | Gets the EVM value at which no more than 5% of the symbols have an EVM exceeding this value. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
| GetEvm95thPercentileMagnitudeError(string, out double) | Returns the measured magnitude error value multiplied by 100, at which, no more than 5 percent of the symbols have magnitude error exceeding this value. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage. |
| GetEvm95thPercentilePhaseError(string, out double) | Gets the measured phase error value multiplied by 100, at which, no more than 5 percent of the symbols have phase error exceeding this value. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees. |
| GetEvmMaximumAmplitudeDroop(string, out double) | Gets the maximum of the amplitude droop values over all the measured time slots. This value is expressed in dB/symbol. The method returns this result for EDGE/EGPRS measurements. |
| GetEvmMaximumFrequencyError(string, out double) | Gets the maximum of the frequency error values over all the measured time slots. This value is expressed in Hz. The method returns this result for EDGE/EGPRS measurements. |
| GetEvmMaximumMagnitudeError(string, out double) | Gets the maximum of the RMS values of magnitude error over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
| GetEvmMaximumPeakEvm(string, out double) | Gets the maximum of the peak EVM values over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
| GetEvmMaximumPeakMagnitudeError(string, out double) | Gets the maximum of peak magnitude error over all the measured time slots. This method is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage. |
| GetEvmMaximumPeakPhaseError(string, out double) | Gets the maximum of peak phase error measured over all the measured time slots. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees. |
| GetEvmMaximumPhaseError(string, out double) | Gets the maximum of the RMS values of phase error values over all the measured time slots. This value is expressed in degrees. The method returns this result for EDGE/EGPRS measurements. |
| GetEvmMaximumRmsEvm(string, out double) | Gets the maximum of the RMS EVM values over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
| GetEvmMeanAmplitudeDroop(string, out double) | Gets the mean of the amplitude droop values over all the measured time slots. This value is expressed in dB/symbol. The method returns this result for EDGE/EGPRS measurements. |
| GetEvmMeanFrequencyError(string, out double) | Gets the mean of the frequency error values over all the measured time slots. This value is expressed in Hz. The method returns this result for EDGE/EGPRS measurements. |
| GetEvmMeanMagnitudeError(string, out double) | Gets the mean of the RMS values of magnitude error over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
| GetEvmMeanPeakEvm(string, out double) | Gets the mean of the peak EVM values over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
| GetEvmMeanPeakMagnitudeError(string, out double) | Returns the mean of peak magnitude error over all the measured time slots. This method is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage. |
| GetEvmMeanPeakPhaseError(string, out double) | Gets the mean of peak phase error over all the measured time slots. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees. |
| GetEvmMeanPhaseError(string, out double) | Gets the mean of the RMS values of phase error values over all the measured time slots. This value is expressed in degrees. The method returns this result for EDGE/EGPRS measurements. |
| GetEvmMeanRmsEvm(string, out double) | Gets the mean of the RMS EVM values over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
| GetEvmPeakEvmSymbol(string, out int) | Gets the symbol number in the burst measurement interval that corresponds to the EVM value returned by the GetEvmMaximumPeakEvm(string, out double) result. The method returns this result for EDGE/EGPRS measurements. |
| GetMaximumIQGainImbalance(string, out double) | Gets the maximum of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. |
| GetMaximumIQOriginOffset(string, out double) | Gets the maximum of the I/Q origin offset values over all the measured time slots. This value is expressed in dB. Presence of I/Q gain imbalance in the signal affects the I/Q origin offset measurement. The method returns this result for GSM/EDGE/EGPRS measurements. |
| GetMeanIQGainImbalance(string, out double) | Gets the mean of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. |
| GetMeanIQOriginOffset(string, out double) | Gets the mean of the I/Q origin offset values over all the measured time slots. This value is expressed in dB. Presence of I/Q gain imbalance in the signal affects the I/Q origin offset measurement. The method returns this result for GSM/EDGE/EGPRS measurements. |
| GetPfer95thPercentilePhaseError(string, out double) | Gets the measured phase error value multiplied by 100, at which, no more than 5 percent of the symbols have phase error exceeding this value. This result is returned while performing ModAcc measurement on GSM. This value is measured in degrees. |
| GetPferMaximumFrequencyError(string, out double) | Gets the maximum of the frequency error values over all the measured time slots. This value is expressed in Hz. The method returns this result for GSM ModAcc measurements. |
| GetPferMaximumPeakPhaseError(string, out double) | Gets the maximum of peak phase error values over all the measured time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements. |
| GetPferMaximumRmsPhaseError(string, out double) | Gets the maximum of the RMS phase error values over all the measured time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements. |
| GetPferMeanFrequencyError(string, out double) | Gets the mean of the frequency error values over all the measured time slots. This value is expressed in Hz. The method returns this result for GSM ModAcc measurements. |
| GetPferMeanPeakPhaseError(string, out double) | Gets the mean of peak phase error values over all the measured time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements. |
| GetPferMeanRmsPhaseError(string, out double) | Gets the mean of the RMS phase error values over all the measured time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements. |
| GetPferPeakPhaseErrorSymbol(string, out int) | Gets the symbol number in the useful portion of the burst corresponding to the phase error value in the GetPferMaximumPeakPhaseError(string, out double) result. The method returns this result for GSM ModAcc measurements. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodulationtype.html language=enus -->
## TOPIC 00223: RFmxGsmMXModulationType Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodulationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxmodulationtype.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the modulation scheme used for the signal. Use "slot(n)" as the selector string to configure or read this method. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXModulationTypeMembersNameValueDescriptionModulationTypeGmsk0The modulation type is Gaussian minimum shift ke

### RFmxGsmMXModulationType Enumeration

Specifies the modulation scheme used for the signal. Use "slot(n)" as the selector string to configure or read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXModulationType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ModulationTypeGmsk | 0 | The modulation type is Gaussian minimum shift keying. This value is valid only when you set the SetBurstType(string, RFmxGsmMXBurstType) method to NB. |
| ModulationType8Psk | 1 | The modulation type is 8-PSK. This value is valid only when you set the Burst Type method to NB. |
| ModulationTypeQpsk | 2 | The modulation type is QPSK. This value is valid only when you set the Burst Type method to HB. |
| ModulationType16Qam | 3 | The modulation type is 16-QAM. |
| ModulationType32Qam | 4 | The modulation type is 32-QAM. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfs-configuration.html language=enus -->
## TOPIC 00224: Configuration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfs-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfs-configuration.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxGsmMXOrfsConfiguration instance that provides methods to configure the ORFS measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic RFmxGsmMXOrfsConfiguration Configuration { get; }

### Configuration

Gets the [RFmxGsmMXOrfsConfiguration](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration.html) instance that provides methods to configure the ORFS measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public [RFmxGsmMXOrfsConfiguration](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration.html) Configuration { get; }

Parent topic:

RFmxGsmMXOrfs Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfs-results.html language=enus -->
## TOPIC 00225: Results

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfs-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfs-results.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxGsmMXOrfsResults instance that provides methods to fetch and read the ORFS measurement results. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic RFmxGsmMXOrfsResults Results { get; }

### Results

Gets the [RFmxGsmMXOrfsResults](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsresults.html) instance that provides methods to fetch and read the ORFS measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public [RFmxGsmMXOrfsResults](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsresults.html) Results { get; }

Parent topic:

RFmxGsmMXOrfs Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfs.html language=enus -->
## TOPIC 00226: RFmxGsmMXOrfs Class

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfs.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfs.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the ORFS measurement. Derives fromRFmxGsmMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic class RFmxGsmMXOrfs : RFmxGsmMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxGsmMXOrfsConfiguration instance that provides methods to configure the ORFS measurement. Res

### RFmxGsmMXOrfs Class

Represents the ORFS measurement.

#### Derives from

- RFmxGsmMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public class RFmxGsmMXOrfs : RFmxGsmMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxGsmMXOrfsConfiguration instance that provides methods to configure the ORFS measurement. |
| Results | Gets the RFmxGsmMXOrfsResults instance that provides methods to fetch and read the ORFS measurement results. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsaveragingenabled.html language=enus -->
## TOPIC 00227: RFmxGsmMXOrfsAveragingEnabled Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsaveragingenabled.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the output radio frequency spectrum (ORFS) measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXOrfsAveragingEnabledMembersNameValueDescriptionFalse0The measurement is performed on a single acquisition. True1The measurement is ave

### RFmxGsmMXOrfsAveragingEnabled Enumeration

Specifies whether to enable averaging for the output radio frequency spectrum (ORFS) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXOrfsAveragingEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement is performed on a single acquisition. |
| True | 1 | The measurement is averaged over multiple acquisitions. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsaveragingtype.html language=enus -->
## TOPIC 00228: RFmxGsmMXOrfsAveragingType Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsaveragingtype.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the output radio frequency spectrum (ORFS) measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXOrfsAveragingTypeMembersNameValueDescriptionRms0The measurement ave

### RFmxGsmMXOrfsAveragingType Enumeration

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the output radio frequency spectrum (ORFS) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXOrfsAveragingType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rms | 0 | The measurement averages the power spectrum linearly. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log | 1 | The measurement averages the power spectrum in a logarithmic scale. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configureaveraging__string-rfmxgsmmxorfsaveragingenabled-int-rfmxgsmmxorfsaveragingtype.html language=enus -->
## TOPIC 00229: ConfigureAveraging(string, RFmxGsmMXOrfsAveragingEnabled, int, RFmxGsmMXOrfsAveragingType)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configureaveraging__string-rfmxgsmmxorfsaveragingenabled-int-rfmxgsmmxorfsaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configureaveraging__string-rfmxgsmmxorfsaveragingenabled-int-rfmxgsmmxorfsaveragingtype.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the output radio frequency spectrum (ORFS) measurement.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int ConfigureAveraging(string selectorString, RFmxGsmMXOrfsAveragingEnabled averagingEnabled, int averagingCount, RFmxGsmMXOrfsAveragingType averagingType)ParametersN

### ConfigureAveraging(string, RFmxGsmMXOrfsAveragingEnabled, int, RFmxGsmMXOrfsAveragingType)

Configures averaging for the output radio frequency spectrum (ORFS) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigureAveraging(string selectorString, RFmxGsmMXOrfsAveragingEnabled averagingEnabled, int averagingCount, RFmxGsmMXOrfsAveragingType averagingType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| averagingEnabled | RFmxGsmMXOrfsAveragingEnabled | Specifies whether to enable averaging for the measurement. |
| averagingCount | int | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True. |
| averagingType | RFmxGsmMXOrfsAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configureevaluationsymbols__string-double-rfmxgsmmxorfsevaluationsymbolsincludetsc-double.html language=enus -->
## TOPIC 00230: ConfigureEvaluationSymbols(string, double, RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc, double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configureevaluationsymbols__string-double-rfmxgsmmxorfsevaluationsymbolsincludetsc-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configureevaluationsymbols__string-double-rfmxgsmmxorfsevaluationsymbolsincludetsc-double.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the evaluation symbols. The GSM standard specifies that 50% to 90% portion of the burst, excluding the midamble, be measured. However, RFmxGSM allows you to specify which portion of the burst to measure for ORFS due to Modulation. RFmx considers the measurement over evaluation symbols for

### ConfigureEvaluationSymbols(string, double, RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc, double)

Configures the evaluation symbols. The GSM standard specifies that 50% to 90% portion of the burst, excluding the midamble, be measured. However, RFmxGSM allows you to specify which portion of the burst to measure for ORFS due to Modulation. RFmx considers the measurement over evaluation symbols for a single burst as one average.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigureEvaluationSymbols(string selectorString, double evaluationSymbolsStart, RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc evaluationSymbolsIncludeTsc, double evaluationSymbolsStop)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| evaluationSymbolsStart | double | Specifies the start position of the burst over which you perform the ORFS measurement. This value is expressed as a percentage. |
| evaluationSymbolsIncludeTsc | RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc | Specifies whether to include the TSC portion of burst in the ORFS measurement. |
| evaluationSymbolsStop | double | Specifies the stop position of the burst over which you perform the ORFS measurement. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configuremeasurementtype__string-rfmxgsmmxorfsmeasurementtype.html language=enus -->
## TOPIC 00231: ConfigureMeasurementType(string, RFmxGsmMXOrfsMeasurementType)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configuremeasurementtype__string-rfmxgsmmxorfsmeasurementtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configuremeasurementtype__string-rfmxgsmmxorfsmeasurementtype.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the type of spectral distortion to be measured. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int ConfigureMeasurementType(string selectorString, RFmxGsmMXOrfsMeasurementType measurementType)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name tha

### ConfigureMeasurementType(string, RFmxGsmMXOrfsMeasurementType)

Configures the type of spectral distortion to be measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigureMeasurementType(string selectorString, RFmxGsmMXOrfsMeasurementType measurementType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| measurementType | RFmxGsmMXOrfsMeasurementType | Specifies the type of spectral distortion to be measured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configuremodulationcustomoffsetfrequencyarray__string-double_arr1.html language=enus -->
## TOPIC 00232: ConfigureModulationCustomOffsetFrequencyArray(string, double[])

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configuremodulationcustomoffsetfrequencyarray__string-double_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configuremodulationcustomoffsetfrequencyarray__string-double_arr1.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of modulation when you set the SetOffsetFrequencyMode(string, RFmxGsmMXOrfsOffsetFrequencyMode) method to Custom. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int Config

### ConfigureModulationCustomOffsetFrequencyArray(string, double[])

Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of modulation when you set the [SetOffsetFrequencyMode(string, RFmxGsmMXOrfsOffsetFrequencyMode)](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setoffsetfrequencymode__string-rfmxgsmmxorfsoffsetfrequencymode.html) method to [Custom](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsoffsetfrequencymode.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigureModulationCustomOffsetFrequencyArray(string selectorString, double[] modulationCustomOffsetFrequency)

#### Remarks

This method is obsoleted. Use ConfigureModulationCustomOffsetFrequencyArray(string selectorString, float[] modulationCustomOffsetFrequency) method to configure.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| modulationCustomOffsetFrequency | double[] | Specifies an array of positive offset frequencies relative to the frequency of the carrier for the spectrum measurement because of modulation when you set the SetOffsetFrequencyMode(string, RFmxGsmMXOrfsOffsetFrequencyMode) method to Custom. This value is expressed in Hz. The lower offset frequency or the negative offset value corresponding to each entry is automatically considered for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configuremodulationcustomoffsetfrequencyarray__string-float_arr1.html language=enus -->
## TOPIC 00233: ConfigureModulationCustomOffsetFrequencyArray(string, float[])

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configuremodulationcustomoffsetfrequencyarray__string-float_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configuremodulationcustomoffsetfrequencyarray__string-float_arr1.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of modulation when you set the SetOffsetFrequencyMode(string, RFmxGsmMXOrfsOffsetFrequencyMode) method to Custom. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int Config

### ConfigureModulationCustomOffsetFrequencyArray(string, float[])

Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of modulation when you set the [SetOffsetFrequencyMode(string, RFmxGsmMXOrfsOffsetFrequencyMode)](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setoffsetfrequencymode__string-rfmxgsmmxorfsoffsetfrequencymode.html) method to [Custom](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsoffsetfrequencymode.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigureModulationCustomOffsetFrequencyArray(string selectorString, float[] modulationCustomOffsetFrequency)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| modulationCustomOffsetFrequency | float[] | Specifies an array of positive offset frequencies relative to the frequency of the carrier for the spectrum measurement because of modulation when you set the SetOffsetFrequencyMode(string, RFmxGsmMXOrfsOffsetFrequencyMode) method to Custom. This value is expressed in Hz. The lower offset frequency or the negative offset value corresponding to each entry is automatically considered for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configurenoisecompensationenabled__string-rfmxgsmmxorfsnoisecompensationenabled.html language=enus -->
## TOPIC 00234: ConfigureNoiseCompensationEnabled(string, RFmxGsmMXOrfsNoiseCompensationEnabled)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configurenoisecompensationenabled__string-rfmxgsmmxorfsnoisecompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configurenoisecompensationenabled__string-rfmxgsmmxorfsnoisecompensationenabled.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. supportedDevices: NI 5663/5665, NI 5668RSyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int ConfigureNoiseCompensationEnabled(string selectorString, RFmxGsmMXOrfsNoiseCompensati

### ConfigureNoiseCompensationEnabled(string, RFmxGsmMXOrfsNoiseCompensationEnabled)

Configures whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. *supportedDevices:* NI 5663/5665, NI 5668R

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigureNoiseCompensationEnabled(string selectorString, RFmxGsmMXOrfsNoiseCompensationEnabled noiseCompensationEnabled)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| noiseCompensationEnabled | RFmxGsmMXOrfsNoiseCompensationEnabled | Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configureoffsetfrequencymode__string-rfmxgsmmxorfsoffsetfrequencymode.html language=enus -->
## TOPIC 00235: ConfigureOffsetFrequencyMode(string, RFmxGsmMXOrfsOffsetFrequencyMode)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configureoffsetfrequencymode__string-rfmxgsmmxorfsoffsetfrequencymode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configureoffsetfrequencymode__string-rfmxgsmmxorfsoffsetfrequencymode.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int ConfigureOffsetFrequencyMode(string selectorString, RFmxGsmMXOrfsOffsetFrequencyMode offsetFrequencyMode)ParametersName

### ConfigureOffsetFrequencyMode(string, RFmxGsmMXOrfsOffsetFrequencyMode)

Configures the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigureOffsetFrequencyMode(string selectorString, RFmxGsmMXOrfsOffsetFrequencyMode offsetFrequencyMode)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| offsetFrequencyMode | RFmxGsmMXOrfsOffsetFrequencyMode | Specifies the list of frequency offsets for which you can perform the ORFS measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configureswitchingcustomoffsetfrequencyarray__string-double_arr1.html language=enus -->
## TOPIC 00236: ConfigureSwitchingCustomOffsetFrequencyArray(string, double[])

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configureswitchingcustomoffsetfrequencyarray__string-double_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configureswitchingcustomoffsetfrequencyarray__string-double_arr1.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of switching when you set the SetOffsetFrequencyMode(string, RFmxGsmMXOrfsOffsetFrequencyMode) method to Custom. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int Configu

### ConfigureSwitchingCustomOffsetFrequencyArray(string, double[])

Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of switching when you set the [SetOffsetFrequencyMode(string, RFmxGsmMXOrfsOffsetFrequencyMode)](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setoffsetfrequencymode__string-rfmxgsmmxorfsoffsetfrequencymode.html) method to [Custom](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsoffsetfrequencymode.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigureSwitchingCustomOffsetFrequencyArray(string selectorString, double[] switchingCustomOffsetFrequency)

#### Remarks

This method is obsoleted. Use ConfigureSwitchingCustomOffsetFrequencyArray(string selectorString, float[] switchingCustomOffsetFrequency) method to configure.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| switchingCustomOffsetFrequency | double[] | Specifies an array of positive offset frequencies relative to the frequency of the carrier for the spectrum measurement because of switching when you set the SetOffsetFrequencyMode(string, RFmxGsmMXOrfsOffsetFrequencyMode) method to Custom. This value is expressed in Hz. The lower offset frequency or the negative offset value corresponding to each entry is automatically considered for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configureswitchingcustomoffsetfrequencyarray__string-float_arr1.html language=enus -->
## TOPIC 00237: ConfigureSwitchingCustomOffsetFrequencyArray(string, float[])

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configureswitchingcustomoffsetfrequencyarray__string-float_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configureswitchingcustomoffsetfrequencyarray__string-float_arr1.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of switching when you set the SetOffsetFrequencyMode(string, RFmxGsmMXOrfsOffsetFrequencyMode) method to Custom. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int Configu

### ConfigureSwitchingCustomOffsetFrequencyArray(string, float[])

Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of switching when you set the [SetOffsetFrequencyMode(string, RFmxGsmMXOrfsOffsetFrequencyMode)](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setoffsetfrequencymode__string-rfmxgsmmxorfsoffsetfrequencymode.html) method to [Custom](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsoffsetfrequencymode.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigureSwitchingCustomOffsetFrequencyArray(string selectorString, float[] switchingCustomOffsetFrequency)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| switchingCustomOffsetFrequency | float[] | Specifies an array of positive offset frequencies relative to the frequency of the carrier for the spectrum measurement because of switching when you set the SetOffsetFrequencyMode(string, RFmxGsmMXOrfsOffsetFrequencyMode) method to Custom. This value is expressed in Hz. The lower offset frequency or the negative offset value corresponding to each entry is automatically considered for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00238: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the traces to be stored and retrieved after performing the output radio frequency spectrum (ORFS) measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method gets the value of OrfsAllTraces

### GetAllTracesEnabled(string, out bool)

Gets whether to enable the traces to be stored and retrieved after performing the output radio frequency spectrum (ORFS) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [OrfsAllTracesEnabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the traces to be stored and retrieved after performing the output radio frequency spectrum (ORFS) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getaveragingcount__string-out.html language=enus -->
## TOPIC 00239: GetAveragingCount(string, out int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getaveragingcount__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getaveragingcount__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxGsmMXOrfsAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetAveragingCount(string selectorString, out int value)RemarksThis method gets the value of OrfsAve

### GetAveragingCount(string, out int)

Gets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxGsmMXOrfsAveragingEnabled)](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setaveragingenabled__string-rfmxgsmmxorfsaveragingenabled.html) method to [True](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetAveragingCount(string selectorString, out int value)

#### Remarks

This method gets the value of [OrfsAveragingCount](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxGsmMXOrfsAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getaveragingenabled__string-out.html language=enus -->
## TOPIC 00240: GetAveragingEnabled(string, out RFmxGsmMXOrfsAveragingEnabled)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getaveragingenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getaveragingenabled__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable averaging for the output radio frequency spectrum (ORFS) measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetAveragingEnabled(string selectorString, out RFmxGsmMXOrfsAveragingEnabled value)RemarksThis method gets the value of OrfsAveragingEnabled attribut

### GetAveragingEnabled(string, out RFmxGsmMXOrfsAveragingEnabled)

Gets whether to enable averaging for the output radio frequency spectrum (ORFS) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetAveragingEnabled(string selectorString, out RFmxGsmMXOrfsAveragingEnabled value)

#### Remarks

This method gets the value of [OrfsAveragingEnabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxGsmMXOrfsAveragingEnabled | Upon return, contains whether to enable averaging for the output radio frequency spectrum (ORFS) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getaveragingtype__string-out.html language=enus -->
## TOPIC 00241: GetAveragingType(string, out RFmxGsmMXOrfsAveragingType)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getaveragingtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getaveragingtype__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the output radio frequency spectrum (ORFS) measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetAveragingType(string selectorString, out RFmxGsmMXOrfsAveragingType value)Remar

### GetAveragingType(string, out RFmxGsmMXOrfsAveragingType)

Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the output radio frequency spectrum (ORFS) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetAveragingType(string selectorString, out RFmxGsmMXOrfsAveragingType value)

#### Remarks

This method gets the value of [OrfsAveragingType](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Log](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsaveragingtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxGsmMXOrfsAveragingType | Upon return, contains the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the output radio frequency spectrum (ORFS) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getevaluationsymbolsincludetsc__string-out.html language=enus -->
## TOPIC 00242: GetEvaluationSymbolsIncludeTsc(string, out RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getevaluationsymbolsincludetsc__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getevaluationsymbolsincludetsc__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to include the training sequence code (TSC) portion of the burst in the output radio frequency spectrum (ORFS) measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetEvaluationSymbolsIncludeTsc(string selectorString, out RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc value)

### GetEvaluationSymbolsIncludeTsc(string, out RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc)

Gets whether to include the training sequence code (TSC) portion of the burst in the output radio frequency spectrum (ORFS) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetEvaluationSymbolsIncludeTsc(string selectorString, out RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc value)

#### Remarks

This method gets the value of [OrfsEvaluationSymbolsIncludeTsc](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsevaluationsymbolsincludetsc.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc | Upon return, contains whether to include the training sequence code (TSC) portion of the burst in the output radio frequency spectrum (ORFS) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getevaluationsymbolsscope__string-out.html language=enus -->
## TOPIC 00243: GetEvaluationSymbolsScope(string, out RFmxGsmMXOrfsEvaluationSymbolsScope)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getevaluationsymbolsscope__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getevaluationsymbolsscope__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the modulation power measurements that will use the part of burst configured using the ConfigureEvaluationSymbols(string, double, RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc, double) method. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetEvaluationSymbolsScope(string selectorString,

### GetEvaluationSymbolsScope(string, out RFmxGsmMXOrfsEvaluationSymbolsScope)

Gets the modulation power measurements that will use the part of burst configured using the [ConfigureEvaluationSymbols(string, double, RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc, double)](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configureevaluationsymbols__string-double-rfmxgsmmxorfsevaluationsymbolsincludetsc-double.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetEvaluationSymbolsScope(string selectorString, out RFmxGsmMXOrfsEvaluationSymbolsScope value)

#### Remarks

This method gets the value of [OrfsEvaluationSymbolsScope](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [OffsetAndCarrier](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsevaluationsymbolsscope.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxGsmMXOrfsEvaluationSymbolsScope | Upon return, contains the modulation power measurements that will use the part of burst configured using the ConfigureEvaluationSymbols(string, double, RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc, double) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getevaluationsymbolsstart__string-out.html language=enus -->
## TOPIC 00244: GetEvaluationSymbolsStart(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getevaluationsymbolsstart__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getevaluationsymbolsstart__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the start position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetEvaluationSymbolsStart(string selectorString, out double value)RemarksThis method

### GetEvaluationSymbolsStart(string, out double)

Gets the start position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetEvaluationSymbolsStart(string selectorString, out double value)

#### Remarks

This method gets the value of [OrfsEvaluationSymbolsStart](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 50.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the start position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getevaluationsymbolsstop__string-out.html language=enus -->
## TOPIC 00245: GetEvaluationSymbolsStop(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getevaluationsymbolsstop__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getevaluationsymbolsstop__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the stop position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetEvaluationSymbolsStop(string selectorString, out double value)RemarksThis method ge

### GetEvaluationSymbolsStop(string, out double)

Gets the stop position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetEvaluationSymbolsStop(string selectorString, out double value)

#### Remarks

This method gets the value of [OrfsEvaluationSymbolsStop](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 90.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the stop position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00246: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the output radio frequency spectrum (ORFS) measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method gets the value of OrfsMeasurementEnabled attribute.The default value is FALSE.Parame

### GetMeasurementEnabled(string, out bool)

Gets whether to enable the output radio frequency spectrum (ORFS) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [OrfsMeasurementEnabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the output radio frequency spectrum (ORFS) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getmeasurementinterval__string-out.html language=enus -->
## TOPIC 00247: GetMeasurementInterval(string, out RFmxGsmMXOrfsMeasurementInterval)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getmeasurementinterval__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getmeasurementinterval__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement is performed on a single specified timeslot or across multiple timeslots. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetMeasurementInterval(string selectorString, out RFmxGsmMXOrfsMeasurementInterval value)RemarksThis method gets the value of OrfsMeasureme

### GetMeasurementInterval(string, out RFmxGsmMXOrfsMeasurementInterval)

Gets whether the measurement is performed on a single specified timeslot or across multiple timeslots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetMeasurementInterval(string selectorString, out RFmxGsmMXOrfsMeasurementInterval value)

#### Remarks

This method gets the value of [OrfsMeasurementInterval](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default Value iss 'Number of Timeslots'.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxGsmMXOrfsMeasurementInterval | Upon return, contains whether the measurement is performed on a single specified timeslot or across multiple timeslots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getmeasurementoffset__string-out.html language=enus -->
## TOPIC 00248: GetMeasurementOffset(string, out int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getmeasurementoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getmeasurementoffset__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the offset, relative to the trigger of the timeslot to be measured. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetMeasurementOffset(string selectorString, out int value)RemarksThis method gets the value of OrfsMeasurementOffset attribute.The default value is 0. Valid values are [

### GetMeasurementOffset(string, out int)

Gets the offset, relative to the trigger of the timeslot to be measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetMeasurementOffset(string selectorString, out int value)

#### Remarks

This method gets the value of [OrfsMeasurementOffset](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 0. Valid values are [0, (Num Timeslots -1)].

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the offset, relative to the trigger of the timeslot to be measured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getmeasurementtype__string-out.html language=enus -->
## TOPIC 00249: GetMeasurementType(string, out RFmxGsmMXOrfsMeasurementType)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getmeasurementtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getmeasurementtype__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the type of spectral distortion to be measured. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetMeasurementType(string selectorString, out RFmxGsmMXOrfsMeasurementType value)RemarksThis method gets the value of OrfsMeasurementType attribute.The default value is ModulationAndSwitchi

### GetMeasurementType(string, out RFmxGsmMXOrfsMeasurementType)

Gets the type of spectral distortion to be measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetMeasurementType(string selectorString, out RFmxGsmMXOrfsMeasurementType value)

#### Remarks

This method gets the value of [OrfsMeasurementType](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [ModulationAndSwitching](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsmeasurementtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxGsmMXOrfsMeasurementType | Upon return, contains the type of spectral distortion to be measured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getmodulationcarrierrbw__string-out.html language=enus -->
## TOPIC 00250: GetModulationCarrierRbw(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getmodulationcarrierrbw__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getmodulationcarrierrbw__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RBW used for measuring modulation carrier power in Hz. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetModulationCarrierRbw(string selectorString, out double value)RemarksThis method gets the value of OrfsModulationCarrierRbw attribute.The default value is 30kHz.ParametersNameT

### GetModulationCarrierRbw(string, out double)

Gets the RBW used for measuring modulation carrier power in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetModulationCarrierRbw(string selectorString, out double value)

#### Remarks

This method gets the value of [OrfsModulationCarrierRbw](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 30kHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the RBW used for measuring modulation carrier power in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class
