# NI DOCUMENT BUNDLE: rfmxlte-dotnet-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxlte-dotnet-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxltemxextension-getltesignalconfiguration__this-string.html language=enus -->
## TOPIC 00001: GetLteSignalConfiguration(this RFmxInstrMX, string)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxltemxextension-getltesignalconfiguration__this-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxltemxextension-getltesignalconfiguration__this-string.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a LTE signal configuration for specified signal name. Existing LTE signal configuration is returned if specified signal name exists. SyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic static RFmxLteMX GetLteSignalConfiguration(this RFmxInstrMX instrSession, string signalName)ParametersN

### GetLteSignalConfiguration(this RFmxInstrMX, string)

Creates a LTE signal configuration for specified signal name. Existing LTE signal configuration is returned if specified signal name exists.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public static [RFmxLteMX](nationalinstruments-rfmx-ltemx-rfmxltemx.html) GetLteSignalConfiguration(this RFmxInstrMX instrSession, string signalName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| instrSession | this RFmxInstrMX | Specifies an RFmxInstr session. |
| signalName | string | Specifies a signal name. |

#### Returns

Returns an object of type RFmxLteMX.

Parent topic:

RFmxLteMXExtension Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxltemxextension-getltesignalconfiguration__this.html language=enus -->
## TOPIC 00002: GetLteSignalConfiguration(this RFmxInstrMX)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxltemxextension-getltesignalconfiguration__this.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxltemxextension-getltesignalconfiguration__this.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new default LTE signal configuration if it doesn't exist; otherwise, it returns the existing default LTE signal configuration. SyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic static RFmxLteMX GetLteSignalConfiguration(this RFmxInstrMX instrSession)ParametersNameTypeDescriptioninstr

### GetLteSignalConfiguration(this RFmxInstrMX)

Creates a new default LTE signal configuration if it doesn't exist; otherwise, it returns the existing default LTE signal configuration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public static [RFmxLteMX](nationalinstruments-rfmx-ltemx-rfmxltemx.html) GetLteSignalConfiguration(this RFmxInstrMX instrSession)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| instrSession | this RFmxInstrMX | Specifies an instr session. |

#### Returns

Returns an object of type RFmxLteMX.

Parent topic:

RFmxLteMXExtension Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxltemxextension-lteclearnoisecalibrationdatabase__this-string.html language=enus -->
## TOPIC 00003: LteClearNoiseCalibrationDatabase(this RFmxInstrMX, string)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxltemxextension-lteclearnoisecalibrationdatabase__this-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxltemxextension-lteclearnoisecalibrationdatabase__this-string.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the noise calibration database used for noise compensation. SyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic static int LteClearNoiseCalibrationDatabase(this RFmxInstrMX instrSession, string selectorString)ParametersNameTypeDescriptioninstrSessionthis RFmxInstrMXSpecifies an RFmxInstr

### LteClearNoiseCalibrationDatabase(this RFmxInstrMX, string)

Clears the noise calibration database used for noise compensation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public static int LteClearNoiseCalibrationDatabase(this RFmxInstrMX instrSession, string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| instrSession | this RFmxInstrMX | Specifies an RFmxInstr session. |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXExtension Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxltemxextension.html language=enus -->
## TOPIC 00004: RFmxLteMXExtension Class

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxltemxextension.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxltemxextension.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides extension methods to create LTE signal configuration. These methods are added to RFmxInstrMX class. Derives fromNoneSyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic class RFmxLteMXExtensionRemarksFor more information about NI-RFmx Instruments, refer to the NI-RFmx Instruments Help.Th

### RFmxLteMXExtension Class

Provides extension methods to create LTE signal configuration. These methods are added to RFmxInstrMX class.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public class RFmxLteMXExtension

#### Remarks

For more information about NI-RFmx Instruments, refer to the NI-RFmx Instruments Help.

#### Thread Safety

Any public static members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| GetLteList(this RFmxInstrMX, string) | Creates a new Lte list if it doesn't exist; otherwise, it returns the existing Lte list. |
| GetLteSignalConfiguration(this RFmxInstrMX, string) | Creates a LTE signal configuration for specified signal name. Existing LTE signal configuration is returned if specified signal name exists. |
| GetLteSignalConfiguration(this RFmxInstrMX) | Creates a new default LTE signal configuration if it doesn't exist; otherwise, it returns the existing default LTE signal configuration. |
| LteClearNoiseCalibrationDatabase(this RFmxInstrMX, string) | Clears the noise calibration database used for noise compensation. |

Parent topic:

NationalInstruments.RFmx.InstrMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-instrmx.html language=enus -->
## TOPIC 00005: NationalInstruments.RFmx.InstrMX

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionRFmxLteMXExtensionProvides extension methods to create LTE signal configuration. These methods are added to RFmxInstrMX class. InterfacesNoneStructuresNoneEnumerationsNoneDelegatesNone

### NationalInstruments.RFmx.InstrMX

#### Classes

| Name | Description |
| --- | --- |
| RFmxLteMXExtension | Provides extension methods to create LTE signal configuration. These methods are added to RFmxInstrMX class. |

#### Interfaces

None

#### Structures

None

#### Enumerations

None

#### Delegates

None

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-abortmeasurements__string.html language=enus -->
## TOPIC 00006: AbortMeasurements(string)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-abortmeasurements__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-abortmeasurements__string.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops acquisition and measurements associated with signal instance that you specify in the selectorString parameter, which were previously initiated by the Initiate(string, string) method or measurement read methods. Calling this method is optional, unless you want to stop a measurement before it is

### AbortMeasurements(string)

Stops acquisition and measurements associated with signal instance that you specify in the *selectorString* parameter, which were previously initiated by the [Initiate(string, string)](nationalinstruments-rfmx-ltemx-rfmxltemx-initiate__string-string.html) method or measurement read methods. Calling this method is optional, unless you want to stop a measurement before it is complete. This method executes even if there is an incoming error.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int AbortMeasurements(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-acp.html language=enus -->
## TOPIC 00007: Acp

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-acp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-acp.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxLteMXAcp instance that represents the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic RFmxLteMXAcp Acp { get; }

### Acp

Gets the [RFmxLteMXAcp](nationalinstruments-rfmx-ltemx-rfmxltemxacp.html) instance that represents the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public [RFmxLteMXAcp](nationalinstruments-rfmx-ltemx-rfmxltemxacp.html) Acp { get; }

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-analyzeiq1waveform__string-string-complexwaveform_complexsingle_-bool-long.html language=enus -->
## TOPIC 00008: AnalyzeIQ1Waveform(string, string, ComplexWaveform< ComplexSingle >, bool, long)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-analyzeiq1waveform__string-string-complexwaveform_complexsingle_-bool-long.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-analyzeiq1waveform__string-string-complexwaveform_complexsingle_-bool-long.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods in the method node. Use this method only if the Recomme

### AnalyzeIQ1Waveform(string, string, ComplexWaveform< ComplexSingle >, bool, long)

Performs the enabled measurements on the I/Q complex waveform that you specify in *IQ* parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods in the method node. Use this method only if the Recommended Acquisition Type method value is either *IQ* or *IQorSpectral*. 
 When using the Analysis-Only mode in RFmxLTE, the RFmx driver ignores the RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM. 
 Query the Recommended Acquisition Type method from the RFmxInstr Property Node after calling the RFmx LTE Commit method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int AnalyzeIQ1Waveform(string selectorString, string resultName, ComplexWaveform< ComplexSingle > iq, bool reset, long reserved)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the result name in this input, either the result name specified by resultName parameter or the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| resultName | string | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"result::r1""r1" |
| iq | ComplexWaveform< ComplexSingle > | Specifies the data for a complex waveform including the start, delta, and actual values. |
| reset | bool | Resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| reserved | long | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-autolevel__string-double-out.html language=enus -->
## TOPIC 00009: AutoLevel(string, double, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-autolevel__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-autolevel__string-double-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Examines the input signal to calculate the peak power level and sets it as the value of the SetReferenceLevel(string, double) method. Use this method to calculate an approximate setting for the reference level. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int AutoLevel(string selectorString

### AutoLevel(string, double, out double)

Examines the input signal to calculate the peak power level and sets it as the value of the [SetReferenceLevel(string, double)](nationalinstruments-rfmx-ltemx-rfmxltemx-setreferencelevel__string-double.html) method. Use this method to calculate an approximate setting for the reference level.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int AutoLevel(string selectorString, double measurementInterval, out double referenceLevel)

#### Remarks

1. Resets the mixer level, mixer level offset, and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation, and preamplifier enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after the execution.

SetAutoLevelInitialReferenceLevel(string, double)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| measurementInterval | double | Specifies the acquisition length. This value is expressed in seconds. Use this value to compute the number of samples to acquire from the signal analyzer. Auto Level method does not use any trigger for acquisition. It ignores the user-configured trigger methods. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. |
| referenceLevel | out double | Upon return, contains the estimated peak power level of the input signal. This value is configured in dBm for RF devices and as Vpk-pk for baseband devices. The default value of this parameter is hardware dependent. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-buildcarrierstring__string-int.html language=enus -->
## TOPIC 00010: BuildCarrierString(string, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-buildcarrierstring__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-buildcarrierstring__string-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a carrier string to use as a selector string with the SEM and ACP carrier configurations or fetch methods and methods.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic static string BuildCarrierString(string selectorString, int carrierNumber)ParametersNameTypeDescriptionselectorStringstr

### BuildCarrierString(string, int)

Creates a carrier string to use as a selector string with the SEM and ACP carrier configurations or fetch methods and methods.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public static string BuildCarrierString(string selectorString, int carrierNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildResultString(string) method to build the selector string. |
| carrierNumber | int | Specifies the carrier number for building the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-buildclusterstring__string-int.html language=enus -->
## TOPIC 00011: BuildClusterString(string, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-buildclusterstring__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-buildclusterstring__string-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a cluster string to use as a selector string with the ModAcc cluster configuration or fetch methods and methods.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic static string BuildClusterString(string selectorString, int clusterNumber)ParametersNameTypeDescriptionselectorStringstringSpe

### BuildClusterString(string, int)

Creates a cluster string to use as a selector string with the ModAcc cluster configuration or fetch methods and methods.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public static string BuildClusterString(string selectorString, int clusterNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| clusterNumber | int | Specifies the cluster number for building the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-buildliststepstring__string-string-int.html language=enus -->
## TOPIC 00012: BuildListStepString(string, string, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-buildliststepstring__string-string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-buildliststepstring__string-string-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the list step string. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic static string BuildListStepString(string selectorString, string resultName, int listStepNumber)ParametersNameTypeDescriptionselectorStringstringSpecifies the list name. This input accepts the list name with or withou

### BuildListStepString(string, string, int)

Creates the list step string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public static string BuildListStepString(string selectorString, string resultName, int listStepNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the list name. This input accepts the list name with or without the "list::" prefix. Example: "list::samplelist1" "samplelist1" |
| resultName | string | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example: "result::r1" "r1" |
| listStepNumber | int | Specifies the list step number. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-buildliststring__string-string.html language=enus -->
## TOPIC 00013: BuildListString(string, string)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-buildliststring__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-buildliststring__string-string.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the list string. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic static string BuildListString(string listName, string resultName)ParametersNameTypeDescriptionlistNamestringSpecifies the list name for building the selector string. This input accepts the list name with or without the "l

### BuildListString(string, string)

Creates the list string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public static string BuildListString(string listName, string resultName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| listName | string | Specifies the list name for building the selector string. This input accepts the list name with or without the "list::" prefix. |
| resultName | string | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example: "result::r1" "r1" |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-buildoffsetstring__string-int.html language=enus -->
## TOPIC 00014: BuildOffsetString(string, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-buildoffsetstring__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-buildoffsetstring__string-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an offset string to use as a selector string with SEM and ACP offset configuration or fetch methods and methods.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic static string BuildOffsetString(string selectorString, int offsetNumber)ParametersNameTypeDescriptionselectorStringstringSpeci

### BuildOffsetString(string, int)

Creates an offset string to use as a selector string with SEM and ACP offset configuration or fetch methods and methods.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public static string BuildOffsetString(string selectorString, int offsetNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildResultString(string) method to build the selector string. |
| offsetNumber | int | Specifies the offset number for building the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-buildpdschstring__string-int.html language=enus -->
## TOPIC 00015: BuildPdschString(string, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-buildpdschstring__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-buildpdschstring__string-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a PDSCH string to use as a selector string with the configuration or fetch methods and methods.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic static string BuildPdschString(string selectorString, int pdschNumber)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector str

### BuildPdschString(string, int)

Creates a PDSCH string to use as a selector string with the configuration or fetch methods and methods.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public static string BuildPdschString(string selectorString, int pdschNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the signal name, subblock number, carrier number, and subframe number. Example:"subblock0/carrier0/subframe0""result::r1/subblock0/carrier0/subframe0" You can use the BuildSubframeString(string, int) method to build the selector string. |
| pdschNumber | int | Specifies the PDSCH channel number for building the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-buildresultstring__string.html language=enus -->
## TOPIC 00016: BuildResultString(string)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-buildresultstring__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-buildresultstring__string.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates selector string for use with configuration or fetch. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic static string BuildResultString(string resultName)ParametersNameTypeDescriptionresultNamestringSpecifies the result name for building the selector string. This input accepts the result

### BuildResultString(string)

Creates selector string for use with configuration or fetch.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public static string BuildResultString(string resultName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| resultName | string | Specifies the result name for building the selector string. This input accepts the result name with or without the "result::" prefix. Example: "", "result::r1", "r1". |

#### Returns

Upon return, contains the selector string created by this method.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-buildsubframestring__string-int.html language=enus -->
## TOPIC 00017: BuildSubframeString(string, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-buildsubframestring__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-buildsubframestring__string-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a subframe string to use as a selector string with the configuration or fetch methods and methods.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic static string BuildSubframeString(string selectorString, int subframeNumber)ParametersNameTypeDescriptionselectorStringstringSpecifies a sel

### BuildSubframeString(string, int)

Creates a subframe string to use as a selector string with the configuration or fetch methods and methods.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public static string BuildSubframeString(string selectorString, int subframeNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the signal name, subblock number, and carrier number. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| subframeNumber | int | Specifies the subframe number for building the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-clearnamedresult__string.html language=enus -->
## TOPIC 00018: ClearNamedResult(string)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-clearnamedresult__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-clearnamedresult__string.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears a result instance specified by the result name in the selectorString parameter.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ClearNamedResult(string selectorString)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the result name. If you do

### ClearNamedResult(string)

Clears a result instance specified by the result name in the *selectorString* parameter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ClearNamedResult(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-commit__string.html language=enus -->
## TOPIC 00019: Commit(string)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-commit__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-commit__string.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits settings to the hardware. Calling this method is optional. RFmxLTE commits settings to the hardware when you call the Initiate(string, string) method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int Commit(string selectorString)ParametersNameTypeDescriptionselectorStringstringPass

### Commit(string)

Commits settings to the hardware. Calling this method is optional. RFmxLTE commits settings to the hardware when you call the [Initiate(string, string)](nationalinstruments-rfmx-ltemx-rfmxltemx-initiate__string-string.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int Commit(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-componentcarrier.html language=enus -->
## TOPIC 00020: ComponentCarrier

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-componentcarrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-componentcarrier.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxLteMXComponentCarrier instance. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic RFmxLteMXComponentCarrier ComponentCarrier { get; }

### ComponentCarrier

Gets the [RFmxLteMXComponentCarrier](nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier.html) instance.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public [RFmxLteMXComponentCarrier](nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier.html) ComponentCarrier { get; }

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-configureautodmrsdetectionenabled__string-rfmxltemxautodmrsdetectionenabled.html language=enus -->
## TOPIC 00021: ConfigureAutoDmrsDetectionEnabled(string, RFmxLteMXAutoDmrsDetectionEnabled)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-configureautodmrsdetectionenabled__string-rfmxltemxautodmrsdetectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-configureautodmrsdetectionenabled__string-rfmxltemxautodmrsdetectionenabled.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether the demodulation reference signal (DMRS) parameters are configured by a user or automatically detected by a measurement.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ConfigureAutoDmrsDetectionEnabled(string selectorString, RFmxLteMXAutoDmrsDetectionEnabled autoDmrsDete

### ConfigureAutoDmrsDetectionEnabled(string, RFmxLteMXAutoDmrsDetectionEnabled)

Configures whether the demodulation reference signal (DMRS) parameters are configured by a user or automatically detected by a measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureAutoDmrsDetectionEnabled(string selectorString, RFmxLteMXAutoDmrsDetectionEnabled autoDmrsDetectionEnabled)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| autoDmrsDetectionEnabled | RFmxLteMXAutoDmrsDetectionEnabled | Specifies whether you need to configure the DMRS parameters, such as the values of the SetUplinkGroupHoppingEnabled(string, RFmxLteMXUplinkGroupHoppingEnabled), SetUplinkSequenceHoppingEnabled(string, RFmxLteMXUplinkSequenceHoppingEnabled), SetCellId(string, int), SetPuschNDmrs1(string, int), SetPuschNDmrs2(string, int), and SetPuschDeltaSequenceShift(string, int) methods, or if the measurement should automatically detect the values of these methods. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-configureband__string-int.html language=enus -->
## TOPIC 00022: ConfigureBand(string, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-configureband__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-configureband__string-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the evolved universal terrestrial radio access (E-UTRA) operating frequency band of a subblock. Use "subblock(n)" as the selector string to configure this method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ConfigureBand(string selectorString, int band)ParametersNameTypeDesc

### ConfigureBand(string, int)

Configures the evolved universal terrestrial radio access (E-UTRA) operating frequency band of a subblock. 
 Use "subblock(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureBand(string selectorString, int band)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the subblock number. Example:"subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| band | int | Specifies the E-UTRA operating frequency band of a subblock as defined in section 5.2 of the 3GPP TS 36.521 specification. Valid values are from 1 to 256, inclusive. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-configurefrequencyearfcn__string-rfmxltemxlinkdirection-int-int.html language=enus -->
## TOPIC 00023: ConfigureFrequencyEarfcn(string, RFmxLteMXLinkDirection, int, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-configurefrequencyearfcn__string-rfmxltemxlinkdirection-int-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-configurefrequencyearfcn__string-rfmxltemxlinkdirection-int-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to the E-UTRA absolute radio frequency channel number (EARFCN) frequency. Use "subblock(n)" as the selector string to configure this method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int Conf

### ConfigureFrequencyEarfcn(string, RFmxLteMXLinkDirection, int, int)

Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to the E-UTRA absolute radio frequency channel number (EARFCN) frequency. 
 Use "subblock(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureFrequencyEarfcn(string selectorString, RFmxLteMXLinkDirection linkDirection, int band, int earfcn)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the subblock number. Example:"subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| linkDirection | RFmxLteMXLinkDirection | Specifies the link direction of the received signal. |
| band | int | Specifies the E-UTRA operating frequency band of a subblock as defined in section 5.2 of the 3GPP TS 36.521 specification. Valid values are from 1 to 256, inclusive. |
| earfcn | int | Specifies the evolved universal terrestrial radio access (E-UTRA) absolute radio frequency channel number. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-configureiqpoweredgetrigger__string-string-rfmxltemxiqpoweredgetriggerslope-double-double-rfmxltemxtriggerminimumquiettimemode-double-rfmxltemxi...d23e1138.html language=enus -->
## TOPIC 00024: ConfigureIQPowerEdgeTrigger(string, string, RFmxLteMXIQPowerEdgeTriggerSlope, double, double, RFmxLteMXTriggerMinimumQuietTimeMode, double, RFmxLteMXIQPowerEdgeTriggerLevelType, bool)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-configureiqpoweredgetrigger__string-string-rfmxltemxiqpoweredgetriggerslope-double-double-rfmxltemxtriggerminimumquiettimemode-double-rfmxltemxi...d23e1138.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-configureiqpoweredgetrigger__string-string-rfmxltemxiqpoweredgetriggerslope-double-double-rfmxltemxtriggerminimumquiettimemode-double-rfmxltemxi...d23e1138.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ConfigureIQPowerEdgeTrigger(string selectorString, string iqPowerEdgeTriggerSource, RFmxLteMXIQP

### ConfigureIQPowerEdgeTrigger(string, string, RFmxLteMXIQPowerEdgeTriggerSlope, double, double, RFmxLteMXTriggerMinimumQuietTimeMode, double, RFmxLteMXIQPowerEdgeTriggerLevelType, bool)

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureIQPowerEdgeTrigger(string selectorString, string iqPowerEdgeTriggerSource, RFmxLteMXIQPowerEdgeTriggerSlope iqPowerEdgeTriggerSlope, double iqPowerEdgeTriggerLevel, double triggerDelay, RFmxLteMXTriggerMinimumQuietTimeMode triggerMinimumQuietTimeMode, double triggerMinimumQuietTimeDuration, RFmxLteMXIQPowerEdgeTriggerLevelType iqPowerEdgeTriggerLevelType, bool enableTrigger)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| iqPowerEdgeTriggerSource | string | Specifies the channel from which the device monitors the trigger. |
| iqPowerEdgeTriggerSlope | RFmxLteMXIQPowerEdgeTriggerSlope | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. |
| iqPowerEdgeTriggerLevel | double | Specifies the power level at which the device triggers, depending on the value of the iqPowerEdgeTriggerSlope parameter. The value is expressed in dB when the iqPowerEdgeTriggerLevelType parameter is set to Relative, or in dBm when it is set to Absolute. |
| triggerDelay | double | Specifies the trigger delay time. This value is expressed in seconds. |
| triggerMinimumQuietTimeMode | RFmxLteMXTriggerMinimumQuietTimeMode | Specifies whether the measurement computes the minimum quiet time used for triggering. |
| triggerMinimumQuietTimeDuration | double | Specifies the duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set SetIQPowerEdgeTriggerSlope(string, RFmxLteMXIQPowerEdgeTriggerSlope) to Rising, the signal is quiet when it is below the trigger level. |
| iqPowerEdgeTriggerLevelType | RFmxLteMXIQPowerEdgeTriggerLevelType | Specifies whether the IQPowerEdgeLevel is set to Relative or Absolute. The value is expressed in dB when this parameter is set to Relative. The value is expressed in dBm when this parameter is set to Absolute. |
| enableTrigger | bool | Specifies whether the trigger is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-configurelinkdirection__string-rfmxltemxlinkdirection.html language=enus -->
## TOPIC 00025: ConfigureLinkDirection(string, RFmxLteMXLinkDirection)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-configurelinkdirection__string-rfmxltemxlinkdirection.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-configurelinkdirection__string-rfmxltemxlinkdirection.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the link direction of the signal being measured. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ConfigureLinkDirection(string selectorString, RFmxLteMXLinkDirection linkDirection)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is pass

### ConfigureLinkDirection(string, RFmxLteMXLinkDirection)

Configures the link direction of the signal being measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureLinkDirection(string selectorString, RFmxLteMXLinkDirection linkDirection)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| linkDirection | RFmxLteMXLinkDirection | Specifies the link direction of the received signal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-configurenumberofcomponentcarriers__string-int.html language=enus -->
## TOPIC 00026: ConfigureNumberOfComponentCarriers(string, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-configurenumberofcomponentcarriers__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-configurenumberofcomponentcarriers__string-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of component carriers within a subblock. Use "subblock(n)" as the selector string to configure this method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ConfigureNumberOfComponentCarriers(string selectorString, int numberOfComponentCarriers)ParametersNameTypeDescri

### ConfigureNumberOfComponentCarriers(string, int)

Configures the number of component carriers within a subblock. 
 Use "subblock(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureNumberOfComponentCarriers(string selectorString, int numberOfComponentCarriers)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the subblock number. Example:"subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| numberOfComponentCarriers | int | Specifies the number of component carriers configured within a subblock. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-configurenumberofdutantennas__string-int.html language=enus -->
## TOPIC 00027: ConfigureNumberOfDutAntennas(string, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-configurenumberofdutantennas__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-configurenumberofdutantennas__string-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of physical antennas used for transmission by the DUT in a MIMO setup.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ConfigureNumberOfDutAntennas(string selectorString, int numberOfDutAntennas)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The

### ConfigureNumberOfDutAntennas(string, int)

Configures the number of physical antennas used for transmission by the DUT in a MIMO setup.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureNumberOfDutAntennas(string selectorString, int numberOfDutAntennas)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| numberOfDutAntennas | int | Specifies the number of physical antennas available at the DUT for transmission in a MIMO setup. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-configurenumberofsubblocks__string-int.html language=enus -->
## TOPIC 00028: ConfigureNumberOfSubblocks(string, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-configurenumberofsubblocks__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-configurenumberofsubblocks__string-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of subblocks.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ConfigureNumberOfSubblocks(string selectorString, int numberOfSubblocks)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when creating the signal configur

### ConfigureNumberOfSubblocks(string, int)

Configures the number of subblocks.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureNumberOfSubblocks(string selectorString, int numberOfSubblocks)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| numberOfSubblocks | int | Specifies the number of subblocks that are configured in the intra-band non-contiguous carrier aggregation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-configurereferencelevel__string-double.html language=enus -->
## TOPIC 00029: ConfigureReferenceLevel(string, double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-configurereferencelevel__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-configurereferencelevel__string-double.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference level, which represents the maximum expected power of an RF input signal.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ConfigureReferenceLevel(string selectorString, double referenceLevel)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The

### ConfigureReferenceLevel(string, double)

Configures the reference level, which represents the maximum expected power of an RF input signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureReferenceLevel(string selectorString, double referenceLevel)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| referenceLevel | double | Specifies the reference level which represents the maximum expected power of the RF input signal. This value is configured in dBm for RF devices and as Vpk-pk for baseband devices. The default value of this parameter is hardware dependent. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-getattributestring__string-int-out.html language=enus -->
## TOPIC 00030: GetAttributeString(string, int, out string)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-getattributestring__string-int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-getattributestring__string-int-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of a of an RFmx string. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetAttributeString(string selectorString, int attributeIdentifier, out string value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being read. Refer to t

### GetAttributeString(string, int, out string)

Gets the value of a of an RFmx string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetAttributeString(string selectorString, int attributeIdentifier, out string value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx LTE Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | out string | Upon return, contains a value of the specified attribute ID. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-getduplexscheme__string-out.html language=enus -->
## TOPIC 00031: GetDuplexScheme(string, out RFmxLteMXDuplexScheme)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-getduplexscheme__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-getduplexscheme__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the duplexing technique of the signal being measured. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetDuplexScheme(string selectorString, out RFmxLteMXDuplexScheme value)RemarksThis method gets the value of DuplexScheme attribute. The default value is Fdd.ParametersNameTypeDescript

### GetDuplexScheme(string, out RFmxLteMXDuplexScheme)

Gets the duplexing technique of the signal being measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetDuplexScheme(string selectorString, out RFmxLteMXDuplexScheme value)

#### Remarks

This method gets the value of [DuplexScheme](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [Fdd](nationalinstruments-rfmx-ltemx-rfmxltemxduplexscheme.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxLteMXDuplexScheme | Upon return, contains the duplexing technique of the signal being measured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-getlimitedconfigurationchange__string-out.html language=enus -->
## TOPIC 00032: GetLimitedConfigurationChange(string, out RFmxLteMXLimitedConfigurationChange)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-getlimitedconfigurationchange__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-getlimitedconfigurationchange__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the set of properties that are considered by RFmx driver in the locked signal configuration state. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetLimitedConfigurationChange(string selectorString, out RFmxLteMXLimitedConfigurationChange value)RemarksThis method gets the value of Li

### GetLimitedConfigurationChange(string, out RFmxLteMXLimitedConfigurationChange)

Gets the set of properties that are considered by RFmx driver in the locked signal configuration state.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetLimitedConfigurationChange(string selectorString, out RFmxLteMXLimitedConfigurationChange value)

#### Remarks

This method gets the value of [LimitedConfigurationChange](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [Disabled](nationalinstruments-rfmx-ltemx-rfmxltemxlimitedconfigurationchange.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxLteMXLimitedConfigurationChange | Upon return, contains the set of properties that are considered by RFmx driver in the locked signal configuration state. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-getlinkdirection__string-out.html language=enus -->
## TOPIC 00033: GetLinkDirection(string, out RFmxLteMXLinkDirection)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-getlinkdirection__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-getlinkdirection__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the link direction of the received signal. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetLinkDirection(string selectorString, out RFmxLteMXLinkDirection value)RemarksThis method gets the value of LinkDirection attribute. The default value is Uplink.ParametersNameTypeDescriptionse

### GetLinkDirection(string, out RFmxLteMXLinkDirection)

Gets the link direction of the received signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetLinkDirection(string selectorString, out RFmxLteMXLinkDirection value)

#### Remarks

This method gets the value of [LinkDirection](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [Uplink](nationalinstruments-rfmx-ltemx-rfmxltemxlinkdirection.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxLteMXLinkDirection | Upon return, contains the link direction of the received signal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-getresultfetchtimeout__string-out.html language=enus -->
## TOPIC 00034: GetResultFetchTimeout(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-getresultfetchtimeout__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-getresultfetchtimeout__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the time to wait before results are available in the RFmxLTE_PropertyNode. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx Property Node waits until the measurement is complete. SyntaxNamespace

### GetResultFetchTimeout(string, out double)

Gets the time to wait before results are available in the RFmxLTE_PropertyNode. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx Property Node waits until the measurement is complete.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetResultFetchTimeout(string selectorString, out double value)

#### Remarks

This method gets the value of [ResultFetchTimeout](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the time to wait before results are available in the RFmxLTE_PropertyNode. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx Property Node waits until the measurement is complete. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-getwarning__out-out.html language=enus -->
## TOPIC 00035: GetWarning(out int, out string)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-getwarning__out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-getwarning__out-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the latest warning code and description. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetWarning(out int warningCode, out string warningDescription)ParametersNameTypeDescriptionwarningCodeout intUpon return, contains the latest warning code.warningDescriptionout stringUpon return,

### GetWarning(out int, out string)

Gets the latest warning code and description.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetWarning(out int warningCode, out string warningDescription)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| warningCode | out int | Upon return, contains the latest warning code. |
| warningDescription | out string | Upon return, contains the latest warning description. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-isdisposed.html language=enus -->
## TOPIC 00036: IsDisposed

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-isdisposed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-isdisposed.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates whether the signal has been disposed. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic bool IsDisposed { get; }Remarkstrue if the session is disposed; otherwise, false.

### IsDisposed

Gets a value that indicates whether the signal has been disposed.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public bool IsDisposed { get; }

#### Remarks

true if the session is disposed; otherwise, false.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-modacc.html language=enus -->
## TOPIC 00037: ModAcc

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-modacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-modacc.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxLteMXModAcc instance that represents the ModAcc measurement. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic RFmxLteMXModAcc ModAcc { get; }

### ModAcc

Gets the [RFmxLteMXModAcc](nationalinstruments-rfmx-ltemx-rfmxltemxmodacc.html) instance that represents the ModAcc measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public [RFmxLteMXModAcc](nationalinstruments-rfmx-ltemx-rfmxltemxmodacc.html) ModAcc { get; }

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-sendsoftwareedgetrigger.html language=enus -->
## TOPIC 00038: SendSoftwareEdgeTrigger()

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-sendsoftwareedgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-sendsoftwareedgetrigger.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a trigger to the device when you use the RFmxLTE_CfgTrigger method to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this method to override a hardware trigger.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SendSoftwareE

### SendSoftwareEdgeTrigger()

Sends a trigger to the device when you use the RFmxLTE_CfgTrigger method to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this method to override a hardware trigger.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SendSoftwareEdgeTrigger()

#### Remarks

- You configure an invalid trigger.
- You have not previously called the [Initiate(string, string)](nationalinstruments-rfmx-ltemx-rfmxltemx-initiate__string-string.html) method.

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-setacquisitionbandwidthoptimizationenabled__string-rfmxltemxacquisitionbandwidthoptimizationenabled.html language=enus -->
## TOPIC 00039: SetAcquisitionBandwidthOptimizationEnabled(string, RFmxLteMXAcquisitionBandwidthOptimizationEnabled)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-setacquisitionbandwidthoptimizationenabled__string-rfmxltemxacquisitionbandwidthoptimizationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-setacquisitionbandwidthoptimizationenabled__string-rfmxltemxacquisitionbandwidthoptimizationenabled.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether RFmx driver optimizes the acquisition bandwidth. This may cause acquisition center frequency or local oscillator (LO) to be placed at different position than you configured. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetAcquisitionBandwidthOptimizationEnabled(string selec

### SetAcquisitionBandwidthOptimizationEnabled(string, RFmxLteMXAcquisitionBandwidthOptimizationEnabled)

Sets whether RFmx driver optimizes the acquisition bandwidth. This may cause acquisition center frequency or local oscillator (LO) to be placed at different position than you configured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetAcquisitionBandwidthOptimizationEnabled(string selectorString, RFmxLteMXAcquisitionBandwidthOptimizationEnabled value)

#### Remarks

This method sets the value of [AcquisitionBandwidthOptimizationEnabled](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [True](nationalinstruments-rfmx-ltemx-rfmxltemxacquisitionbandwidthoptimizationenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxLteMXAcquisitionBandwidthOptimizationEnabled | Specifies whether RFmx driver optimizes the acquisition bandwidth. This may cause acquisition center frequency or local oscillator (LO) to be placed at different position than you configured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-setattributeint__string-int-int.html language=enus -->
## TOPIC 00040: SetAttributeInt(string, int, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-setattributeint__string-int-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-setattributeint__string-int-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a Int attribute. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetAttributeInt(string selectorString, int attributeIdentifier, int value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being set. Refer to the Using a Sele

### SetAttributeInt(string, int, int)

Sets the value of a Int attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetAttributeInt(string selectorString, int attributeIdentifier, int value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx LTE Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | int | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-setattributestring__string-int-string.html language=enus -->
## TOPIC 00041: SetAttributeString(string, int, string)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-setattributestring__string-int-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-setattributestring__string-int-string.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a String attribute. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetAttributeString(string selectorString, int attributeIdentifier, string value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being set. Refer to the Usi

### SetAttributeString(string, int, string)

Sets the value of a String attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetAttributeString(string selectorString, int attributeIdentifier, string value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx LTE Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | string | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-setreferencelevelheadroom__string-double.html language=enus -->
## TOPIC 00042: SetReferenceLevelHeadroom(string, double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-setreferencelevelheadroom__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-setreferencelevelheadroom__string-double.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the margin RFmx driver adds to the SetReferenceLevel(string, double) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. Default values PXIe-5668: 6 dB PXIe-5830/5831/5832/5841/5842/5860: 1 dB PXIe-5840: 0 dB Supported devices: PX

### SetReferenceLevelHeadroom(string, double)

Sets the margin RFmx driver adds to the [SetReferenceLevel(string, double)](nationalinstruments-rfmx-ltemx-rfmxltemx-setreferencelevel__string-double.html) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. **Default values** 
 PXIe-5668: 6 dB 
 PXIe-5830/5831/5832/5841/5842/5860: 1 dB 
 PXIe-5840: 0 dB **Supported devices:**PXIe-5668, PXIe-5830/5831/5832/5840/5841/5842/5860.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetReferenceLevelHeadroom(string selectorString, double value)

#### Remarks

This method sets the value of [ReferenceLevelHeadroom](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the margin RFmx driver adds to the SetReferenceLevel(string, double) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-setselectedports__string-string.html language=enus -->
## TOPIC 00043: SetSelectedPorts(string, string)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-setselectedports__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-setselectedports__string-string.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. Valid values PXIe-5820/5840: "" (empty string) PXIe-5830: if0, if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connecti

### SetSelectedPorts(string, string)

Sets the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. **Valid values** 
 PXIe-5820/5840: "" (empty string) 
 PXIe-5830: if0, if1 
 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel **Default values** 
 PXIe-5820/5840: "" (empty string) 
 PXIe-5830/5831/5832: if1 
 PXIe-5831/5832: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel **Supported devices**: PXIe-5820/5830/5831/5832/5840 
</x></x>

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetSelectedPorts(string selectorString, string value)

#### Remarks

This method sets the value of [SelectedPorts](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. Default values PXIe-5830/5831/5832 if1. Other devices "" (empty string)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | string | Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-setspecialsubframeconfiguration__string-int.html language=enus -->
## TOPIC 00044: SetSpecialSubframeConfiguration(string, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-setspecialsubframeconfiguration__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-setspecialsubframeconfiguration__string-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the special subframe configuration index. It defines the length of DwPTS, GP, and UpPTS for TDD transmission as defined in the section 4.2 of 3GPP 36.211 specification. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetSpecialSubframeConfiguration(string selectorString, int value)Rem

### SetSpecialSubframeConfiguration(string, int)

Sets the special subframe configuration index. It defines the length of DwPTS, GP, and UpPTS for TDD transmission as defined in the section 4.2 of *3GPP 36.211* specification.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetSpecialSubframeConfiguration(string selectorString, int value)

#### Remarks

This method sets the value of [SpecialSubframeConfiguration](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 0. Valid values are 0 to 9, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the special subframe configuration index. It defines the length of DwPTS, GP, and UpPTS for TDD transmission as defined in the section 4.2 of 3GPP 36.211 specification. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-settransmitantennatoanalyze__string-int.html language=enus -->
## TOPIC 00045: SetTransmitAntennaToAnalyze(string, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-settransmitantennatoanalyze__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-settransmitantennatoanalyze__string-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the physical antenna connected to the analyzer. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetTransmitAntennaToAnalyze(string selectorString, int value)RemarksThis method sets the value of TransmitAntennaToAnalyze attribute. The default value is 0. Valid values are from 0 to N-1,

### SetTransmitAntennaToAnalyze(string, int)

Sets the physical antenna connected to the analyzer.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetTransmitAntennaToAnalyze(string selectorString, int value)

#### Remarks

This method sets the value of [TransmitAntennaToAnalyze](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 0. Valid values are from 0 to N-1, where N is the number of DUT antennas.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the physical antenna connected to the analyzer. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-setuplinkdownlinkconfiguration__string-rfmxltemxuplinkdownlinkconfiguration.html language=enus -->
## TOPIC 00046: SetUplinkDownlinkConfiguration(string, RFmxLteMXUplinkDownlinkConfiguration)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-setuplinkdownlinkconfiguration__string-rfmxltemxuplinkdownlinkconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-setuplinkdownlinkconfiguration__string-rfmxltemxuplinkdownlinkconfiguration.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the configuration of the LTE frame structure in the time division duplex (TDD) mode. Refer to table 4.2-2 of the 3GPP TS 36.211 specification to configure the LTE frame. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetUplinkDownlinkConfiguration(string selectorString, RFmxLteMXUpli

### SetUplinkDownlinkConfiguration(string, RFmxLteMXUplinkDownlinkConfiguration)

Sets the configuration of the LTE frame structure in the time division duplex (TDD) mode. Refer to table 4.2-2 of the *3GPP TS 36.211* specification to configure the LTE frame.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetUplinkDownlinkConfiguration(string selectorString, RFmxLteMXUplinkDownlinkConfiguration value)

#### Remarks

This method sets the value of [UplinkDownlinkConfiguration](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [Configuration0](nationalinstruments-rfmx-ltemx-rfmxltemxuplinkdownlinkconfiguration.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxLteMXUplinkDownlinkConfiguration | Specifies the configuration of the LTE frame structure in the time division duplex (TDD) mode. Refer to table 4.2-2 of the 3GPP TS 36.211 specification to configure the LTE frame. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-signalconfigurationtype.html language=enus -->
## TOPIC 00047: SignalConfigurationType

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-signalconfigurationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-signalconfigurationtype.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Type object for RFmxLteMX. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic Type SignalConfigurationType { get; }RemarksReturns the type of signal configuration object.

### SignalConfigurationType

Gets the Type object for RFmxLteMX.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public Type SignalConfigurationType { get; }

#### Remarks

Returns the type of signal configuration object.

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-slotphase.html language=enus -->
## TOPIC 00048: SlotPhase

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-slotphase.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-slotphase.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxLteMXSlotPhase instance that represents the SlotPhase measurement. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic RFmxLteMXSlotPhase SlotPhase { get; }

### SlotPhase

Gets the [RFmxLteMXSlotPhase](nationalinstruments-rfmx-ltemx-rfmxltemxslotphase.html) instance that represents the SlotPhase measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public [RFmxLteMXSlotPhase](nationalinstruments-rfmx-ltemx-rfmxltemxslotphase.html) SlotPhase { get; }

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemx-slotpower.html language=enus -->
## TOPIC 00049: SlotPower

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemx-slotpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemx-slotpower.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxLteMXSlotPower instance that represents the SlotPower measurement. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic RFmxLteMXSlotPower SlotPower { get; }

### SlotPower

Gets the [RFmxLteMXSlotPower](nationalinstruments-rfmx-ltemx-rfmxltemxslotpower.html) instance that represents the SlotPower measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public [RFmxLteMXSlotPower](nationalinstruments-rfmx-ltemx-rfmxltemxslotpower.html) SlotPower { get; }

Parent topic:

RFmxLteMX Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacpaveragingenabled.html language=enus -->
## TOPIC 00050: RFmxLteMXAcpAveragingEnabled Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacpaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacpaveragingenabled.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXAcpAveragingEnabledMembersNameValueDescriptionFalse0The measurement is performed on a single acquisition. True1The ACP measurement uses the value of the SetAveragingCoun

### RFmxLteMXAcpAveragingEnabled Enumeration

Specifies whether to enable averaging for the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXAcpAveragingEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement is performed on a single acquisition. |
| True | 1 | The ACP measurement uses the value of the SetAveragingCount(string, int) method as the number of acquisitions over which the ACP measurement is averaged. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-configurenoisecompensationenabled__string-rfmxltemxacpnoisecompensationenabled.html language=enus -->
## TOPIC 00051: ConfigureNoiseCompensationEnabled(string, RFmxLteMXAcpNoiseCompensationEnabled)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-configurenoisecompensationenabled__string-rfmxltemxacpnoisecompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-configurenoisecompensationenabled__string-rfmxltemxacpnoisecompensationenabled.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures compensation of the channel powers for the inherent noise floor of the signal analyzer.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ConfigureNoiseCompensationEnabled(string selectorString, RFmxLteMXAcpNoiseCompensationEnabled noiseCompensationEnabled)ParametersNameTypeDescrip

### ConfigureNoiseCompensationEnabled(string, RFmxLteMXAcpNoiseCompensationEnabled)

Configures compensation of the channel powers for the inherent noise floor of the signal analyzer.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureNoiseCompensationEnabled(string selectorString, RFmxLteMXAcpNoiseCompensationEnabled noiseCompensationEnabled)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| noiseCompensationEnabled | RFmxLteMXAcpNoiseCompensationEnabled | Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-configurenumberofeutraoffsets__string-int.html language=enus -->
## TOPIC 00052: ConfigureNumberOfEutraOffsets(string, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-configurenumberofeutraoffsets__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-configurenumberofeutraoffsets__string-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of evolved universal terrestrial radio access adjacent channels of the subblock, when you set the ACP Configurable Number of Offset Enabled method to true. Use "subblock(n)" as the selector string to configure this method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic i

### ConfigureNumberOfEutraOffsets(string, int)

Configures the number of evolved universal terrestrial radio access adjacent channels of the subblock, when you set the ACP Configurable Number of Offset Enabled method to *true*. 
 Use "subblock(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureNumberOfEutraOffsets(string selectorString, int numberOfEutraOffsets)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the subblock number. Example:"subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| numberOfEutraOffsets | int | Specifies the number of E-UTRA adjacent channel offsets to be configured at offset positions, when you set the ACP Configurable Number of Offset Enabled method to true. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-configurenumberofgsmoffsets__string-int.html language=enus -->
## TOPIC 00053: ConfigureNumberOfGsmOffsets(string, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-configurenumberofgsmoffsets__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-configurenumberofgsmoffsets__string-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of GSM adjacent channels of the subblock, when you set the ACP Configurable Number of Offset Enabled method to true. Use "subblock(n)" as the selector string to configure this method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ConfigureNumberOfGsmOffsets(string s

### ConfigureNumberOfGsmOffsets(string, int)

Configures the number of GSM adjacent channels of the subblock, when you set the ACP Configurable Number of Offset Enabled method to *true*. 
 Use "subblock(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureNumberOfGsmOffsets(string selectorString, int numberOfGsmOffsets)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the subblock number. Example:"subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| numberOfGsmOffsets | int | Specifies the number of GSM adjacent channel offsets to be configured when you set the SetBandwidth(string, double) to 200.0k and when you set the ACP Configurable Number of Offset Enabled method to true. The frequency offset from the center of NB-IOT carrier to the center of the first offset is 300 kHz as defined in the 3GPP specification. The center of every other offset is placed at 200 kHz from the previous offset's center. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-configurenumberofutraoffsets__string-int.html language=enus -->
## TOPIC 00054: ConfigureNumberOfUtraOffsets(string, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-configurenumberofutraoffsets__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-configurenumberofutraoffsets__string-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of universal terrestrial radio access (UTRA) adjacent channels of the subblock, when you set the ACP Configurable Number of Offset Enabled method to true. Use "subblock(n)" as the selector string to configure this method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic in

### ConfigureNumberOfUtraOffsets(string, int)

Configures the number of universal terrestrial radio access (UTRA) adjacent channels of the subblock, when you set the ACP Configurable Number of Offset Enabled method to *true*. 
 Use "subblock(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureNumberOfUtraOffsets(string selectorString, int numberOfUtraOffsets)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the subblock number. Example:"subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| numberOfUtraOffsets | int | Specifies the number of UTRA adjacent channel offsets to be configured at offset positions, when you set the ACP Configurable Number of Offset Enabled method to true. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-configurerbwfilter__string-rfmxltemxacprbwautobandwidth-double-rfmxltemxacprbwfiltertype.html language=enus -->
## TOPIC 00055: ConfigureRbwFilter(string, RFmxLteMXAcpRbwAutoBandwidth, double, RFmxLteMXAcpRbwFilterType)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-configurerbwfilter__string-rfmxltemxacprbwautobandwidth-double-rfmxltemxacprbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-configurerbwfilter__string-rfmxltemxacprbwautobandwidth-double-rfmxltemxacprbwfiltertype.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RBW filter.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ConfigureRbwFilter(string selectorString, RFmxLteMXAcpRbwAutoBandwidth rbwAuto, double rbw, RFmxLteMXAcpRbwFilterType rbwFilterType)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal na

### ConfigureRbwFilter(string, RFmxLteMXAcpRbwAutoBandwidth, double, RFmxLteMXAcpRbwFilterType)

Configures the RBW filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureRbwFilter(string selectorString, RFmxLteMXAcpRbwAutoBandwidth rbwAuto, double rbw, RFmxLteMXAcpRbwFilterType rbwFilterType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| rbwAuto | RFmxLteMXAcpRbwAutoBandwidth | Specifies whether the measurement computes the RBW. |
| rbw | double | Specifies the bandwidth of the RBW filter used to sweep the acquired signal, when you set the rbwAuto parameter to False. This value is expressed in Hz. |
| rbwFilterType | RFmxLteMXAcpRbwFilterType | Specifies the shape of the digital RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-configureutraandeutraoffsets__string-int-int.html language=enus -->
## TOPIC 00056: ConfigureUtraAndEutraOffsets(string, int, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-configureutraandeutraoffsets__string-int-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-configureutraandeutraoffsets__string-int-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of universal terrestrial radio access (UTRA) and evolved universal terrestrial radio access (E-UTRA) adjacent channels of the subblock. This method is valid only for uplink single carrier, and contiguous carrier aggregation. In case of uplink non-contiguous multi-carrier and do

### ConfigureUtraAndEutraOffsets(string, int, int)

Configures the number of universal terrestrial radio access (UTRA) and evolved universal terrestrial radio access (E-UTRA) adjacent channels of the subblock. This method is valid only for uplink single carrier, and contiguous carrier aggregation. In case of uplink non-contiguous multi-carrier and downlink, the number of UTRA/EUTRA offsets are determined from the 3GPP specification. 
 Use "subblock(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureUtraAndEutraOffsets(string selectorString, int numberOfUtraOffsets, int numberOfEutraOffsets)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the subblock number. Example:"subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| numberOfUtraOffsets | int | Specifies the number of UTRA adjacent channel offsets to be configured at offset positions as defined in the 3GPP specification. |
| numberOfEutraOffsets | int | Specifies the number of E-UTRA adjacent channel offsets to be configured at offset positions as defined in the 3GPP specification. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00057: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the traces to be stored and retrieved after performing the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method gets the value of AcpAllTracesEnabled attribute. The default value

### GetAllTracesEnabled(string, out bool)

Gets whether to enable the traces to be stored and retrieved after performing the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [AcpAllTracesEnabled](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the traces to be stored and retrieved after performing the ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-getamplitudecorrectiontype__string-out.html language=enus -->
## TOPIC 00058: GetAmplitudeCorrectionType(string, out RFmxLteMXAcpAmplitudeCorrectionType)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-getamplitudecorrectiontype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-getamplitudecorrectiontype__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. SyntaxNamespace: National

### GetAmplitudeCorrectionType(string, out RFmxLteMXAcpAmplitudeCorrectionType)

Gets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetAmplitudeCorrectionType(string selectorString, out RFmxLteMXAcpAmplitudeCorrectionType value)

#### Remarks

This method gets the value of [AcpAmplitudeCorrectionType](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [RFCenterFrequency](nationalinstruments-rfmx-ltemx-rfmxltemxacpamplitudecorrectiontype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxLteMXAcpAmplitudeCorrectionType | Upon return, contains whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-getconfigurablenumberofoffsetsenabled__string-out.html language=enus -->
## TOPIC 00059: GetConfigurableNumberOfOffsetsEnabled(string, out RFmxLteMXAcpConfigurableNumberOfOffsetsEnabled)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-getconfigurablenumberofoffsetsenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-getconfigurablenumberofoffsetsenabled__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the number of offsets is computed by measurement or configured by you. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetConfigurableNumberOfOffsetsEnabled(string selectorString, out RFmxLteMXAcpConfigurableNumberOfOffsetsEnabled value)RemarksThis method gets the value of Acp

### GetConfigurableNumberOfOffsetsEnabled(string, out RFmxLteMXAcpConfigurableNumberOfOffsetsEnabled)

Gets whether the number of offsets is computed by measurement or configured by you.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetConfigurableNumberOfOffsetsEnabled(string selectorString, out RFmxLteMXAcpConfigurableNumberOfOffsetsEnabled value)

#### Remarks

This method gets the value of [AcpConfigurableNumberOfOffsetsEnabled](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. When the carrier bandwidth is 200 kHz or the Link Direction is Downlink, the default value is False. The default value is True, otherwise. Incase of downlink, this property is applicable only for number of EUTRA offsets. For the number of UTRA offsets, only 3GPP specification defined values are supported.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxLteMXAcpConfigurableNumberOfOffsetsEnabled | Upon return, contains whether the number of offsets is computed by measurement or configured by you. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-getfarifoutputpoweroffset__string-out.html language=enus -->
## TOPIC 00060: GetFarIFOutputPowerOffset(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-getfarifoutputpoweroffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-getfarifoutputpoweroffset__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the offset that is needed to adjust the IF output power levels for the offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This method is applicable only when you set the SetIFOutputPowerOffsetAuto(string, RFmxLteMXAcpIFOutputPowerO

### GetFarIFOutputPowerOffset(string, out double)

Gets the offset that is needed to adjust the IF output power levels for the offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This method is applicable only when you set the [SetIFOutputPowerOffsetAuto(string, RFmxLteMXAcpIFOutputPowerOffsetAuto)](nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setifoutputpoweroffsetauto__string-rfmxltemxacpifoutputpoweroffsetauto.html) method to [False](nationalinstruments-rfmx-ltemx-rfmxltemxacpifoutputpoweroffsetauto.html) and [SetMeasurementMethod(string, RFmxLteMXAcpMeasurementMethod)](nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setmeasurementmethod__string-rfmxltemxacpmeasurementmethod.html) method to [DynamicRange](nationalinstruments-rfmx-ltemx-rfmxltemxacpmeasurementmethod.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetFarIFOutputPowerOffset(string selectorString, out double value)

#### Remarks

This method gets the value of [AcpFarIFOutputPowerOffset](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 20.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the offset that is needed to adjust the IF output power levels for the offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This method is applicable only when you set the SetIFOutputPowerOffsetAuto(string, RFmxLteMXAcpIFOutputPowerOffsetAuto) method to False and SetMeasurementMethod(string, RFmxLteMXAcpMeasurementMethod) method to DynamicRange. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-getfftoverlap__string-out.html language=enus -->
## TOPIC 00061: GetFftOverlap(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-getfftoverlap__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-getfftoverlap__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the samples to overlap between the consecutive chunks as a percentage of the ACP Sequential FFT Size property value when you set the SetMeasurementMethod(string, RFmxLteMXAcpMeasurementMethod) method to SequentialFft and the SetFftOverlapMode(string, RFmxLteMXAcpFftOverlapMode) method to UserDe

### GetFftOverlap(string, out double)

Gets the samples to overlap between the consecutive chunks as a percentage of the ACP Sequential FFT Size property value when you set the [SetMeasurementMethod(string, RFmxLteMXAcpMeasurementMethod)](nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setmeasurementmethod__string-rfmxltemxacpmeasurementmethod.html) method to [SequentialFft](nationalinstruments-rfmx-ltemx-rfmxltemxacpmeasurementmethod.html) and the [SetFftOverlapMode(string, RFmxLteMXAcpFftOverlapMode)](nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setfftoverlapmode__string-rfmxltemxacpfftoverlapmode.html) method to [UserDefined](nationalinstruments-rfmx-ltemx-rfmxltemxacpfftoverlapmode.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetFftOverlap(string selectorString, out double value)

#### Remarks

This method gets the value of [AcpFftOverlap](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, the samples to overlap between the consecutive chunks as a percentage of the AcpSequentialFftSize property value. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-getnoisecompensationtype__string-out.html language=enus -->
## TOPIC 00062: GetNoiseCompensationType(string, out RFmxLteMXAcpNoiseCompensationType)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-getnoisecompensationtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-getnoisecompensationtype__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetNoiseCompensationType(string selectorString, out RFmxLteMXAcpNoiseCompensationType value)RemarksT

### GetNoiseCompensationType(string, out RFmxLteMXAcpNoiseCompensationType)

Gets the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetNoiseCompensationType(string selectorString, out RFmxLteMXAcpNoiseCompensationType value)

#### Remarks

This method gets the value of [AcpNoiseCompensationType](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [AnalyzerAndTermination](nationalinstruments-rfmx-ltemx-rfmxltemxacpnoisecompensationtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxLteMXAcpNoiseCompensationType | Upon return, contains the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-getnumberofstandalonenbiotoffsets__string-out.html language=enus -->
## TOPIC 00063: GetNumberOfStandaloneNBIoTOffsets(string, out int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-getnumberofstandalonenbiotoffsets__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-getnumberofstandalonenbiotoffsets__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of Standalone NB-IoT adjacent channel offsets to be configured when you set the SetBandwidth(string, double) to 200.0 k, SetLinkDirection(string, RFmxLteMXLinkDirection) to Downlink and the ACP Configurable Number of Offset Enabled method to True. SyntaxNamespace: NationalInstruments

### GetNumberOfStandaloneNBIoTOffsets(string, out int)

Gets the number of Standalone NB-IoT adjacent channel offsets to be configured when you set the [SetBandwidth(string, double)](nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-setbandwidth__string-double.html) to 200.0 k, [SetLinkDirection(string, RFmxLteMXLinkDirection)](nationalinstruments-rfmx-ltemx-rfmxltemx-setlinkdirection__string-rfmxltemxlinkdirection.html) to Downlink and the ACP Configurable Number of Offset Enabled method to True.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetNumberOfStandaloneNBIoTOffsets(string selectorString, out int value)

#### Remarks

This method gets the value of [AcpNumberOfStandaloneNBIoTOffsets](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 2, when you set the CC Bandwidth property to is 200.0 k and LinkDirection to is Downlink. The default value is 0, otherwise.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the Standalone NB-IoT adjacent channel offsets to be configured when you set the SetBandwidth(string, double) to 200.0 k, SetLinkDirection(string, RFmxLteMXLinkDirection) to Downlink and the ACP Configurable Number of Offset Enabled method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setamplitudecorrectiontype__string-rfmxltemxacpamplitudecorrectiontype.html language=enus -->
## TOPIC 00064: SetAmplitudeCorrectionType(string, RFmxLteMXAcpAmplitudeCorrectionType)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setamplitudecorrectiontype__string-rfmxltemxacpamplitudecorrectiontype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setamplitudecorrectiontype__string-rfmxltemxacpamplitudecorrectiontype.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. SyntaxNamespace: National

### SetAmplitudeCorrectionType(string, RFmxLteMXAcpAmplitudeCorrectionType)

Sets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetAmplitudeCorrectionType(string selectorString, RFmxLteMXAcpAmplitudeCorrectionType value)

#### Remarks

This method sets the value of [AcpAmplitudeCorrectionType](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [RFCenterFrequency](nationalinstruments-rfmx-ltemx-rfmxltemxacpamplitudecorrectiontype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxLteMXAcpAmplitudeCorrectionType | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setaveragingcount__string-int.html language=enus -->
## TOPIC 00065: SetAveragingCount(string, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setaveragingcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setaveragingcount__string-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxLteMXAcpAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetAveragingCount(string selectorString, int value)RemarksThis method sets the value of AcpAveraging

### SetAveragingCount(string, int)

Sets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxLteMXAcpAveragingEnabled)](nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setaveragingenabled__string-rfmxltemxacpaveragingenabled.html) method to [True](nationalinstruments-rfmx-ltemx-rfmxltemxacpaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetAveragingCount(string selectorString, int value)

#### Remarks

This method sets the value of [AcpAveragingCount](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxLteMXAcpAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setifoutputpoweroffsetauto__string-rfmxltemxacpifoutputpoweroffsetauto.html language=enus -->
## TOPIC 00066: SetIFOutputPowerOffsetAuto(string, RFmxLteMXAcpIFOutputPowerOffsetAuto)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setifoutputpoweroffsetauto__string-rfmxltemxacpifoutputpoweroffsetauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setifoutputpoweroffsetauto__string-rfmxltemxacpifoutputpoweroffsetauto.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement computes an appropriate IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. This method is applicable only when you set the SetMeasurementMethod(string, RFmxLteMXAcpMeasurementMethod) method to DynamicRange. SyntaxNam

### SetIFOutputPowerOffsetAuto(string, RFmxLteMXAcpIFOutputPowerOffsetAuto)

Sets whether the measurement computes an appropriate IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. This method is applicable only when you set the [SetMeasurementMethod(string, RFmxLteMXAcpMeasurementMethod)](nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setmeasurementmethod__string-rfmxltemxacpmeasurementmethod.html) method to [DynamicRange](nationalinstruments-rfmx-ltemx-rfmxltemxacpmeasurementmethod.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetIFOutputPowerOffsetAuto(string selectorString, RFmxLteMXAcpIFOutputPowerOffsetAuto value)

#### Remarks

This method sets the value of [AcpIFOutputPowerOffsetAuto](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [True](nationalinstruments-rfmx-ltemx-rfmxltemxacpifoutputpoweroffsetauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxLteMXAcpIFOutputPowerOffsetAuto | Specifies whether the measurement computes an appropriate IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. This method is applicable only when you set the SetMeasurementMethod(string, RFmxLteMXAcpMeasurementMethod) method to DynamicRange. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setnumberofstandalonenbiotoffsets__string-int.html language=enus -->
## TOPIC 00067: SetNumberOfStandaloneNBIoTOffsets(string, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setnumberofstandalonenbiotoffsets__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setnumberofstandalonenbiotoffsets__string-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of Standalone NB-IoT adjacent channel offsets to be configured when you set the SetBandwidth(string, double) to 200.0 k, SetLinkDirection(string, RFmxLteMXLinkDirection) to Downlink and the ACP Configurable Number of Offset Enabled method to True. SyntaxNamespace: NationalInstruments

### SetNumberOfStandaloneNBIoTOffsets(string, int)

Sets the number of Standalone NB-IoT adjacent channel offsets to be configured when you set the [SetBandwidth(string, double)](nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-setbandwidth__string-double.html) to 200.0 k, [SetLinkDirection(string, RFmxLteMXLinkDirection)](nationalinstruments-rfmx-ltemx-rfmxltemx-setlinkdirection__string-rfmxltemxlinkdirection.html) to Downlink and the ACP Configurable Number of Offset Enabled method to True.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetNumberOfStandaloneNBIoTOffsets(string selectorString, int value)

#### Remarks

This method sets the value of [AcpNumberOfStandaloneNBIoTOffsets](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 2, when you set the CC Bandwidth property to is 200.0 k and LinkDirection to is Downlink. The default value is 0, otherwise.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(string, int) method to build the selector string. |
| value | int | Specifies the number of Standalone NB-IoT adjacent channel offsets to be configured when you set the SetBandwidth(string, double) to 200.0 k, SetLinkDirection(string, RFmxLteMXLinkDirection) to Downlink and the ACP Configurable Number of Offset Enabled method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setrbwfilterbandwidth__string-double.html language=enus -->
## TOPIC 00068: SetRbwFilterBandwidth(string, double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setrbwfilterbandwidth__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setrbwfilterbandwidth__string-double.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(string, RFmxLteMXAcpRbwAutoBandwidth) method to False. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetRbwFilterBandwidth(string selectorStr

### SetRbwFilterBandwidth(string, double)

Sets the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the [SetRbwFilterAutoBandwidth(string, RFmxLteMXAcpRbwAutoBandwidth)](nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setrbwfilterautobandwidth__string-rfmxltemxacprbwautobandwidth.html) method to [False](nationalinstruments-rfmx-ltemx-rfmxltemxacprbwautobandwidth.html). This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetRbwFilterBandwidth(string selectorString, double value)

#### Remarks

This method sets the value of [AcpRbwFilterBandwidth](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 30000.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(string, RFmxLteMXAcpRbwAutoBandwidth) method to False. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setrbwfiltertype__string-rfmxltemxacprbwfiltertype.html language=enus -->
## TOPIC 00069: SetRbwFilterType(string, RFmxLteMXAcpRbwFilterType)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setrbwfiltertype__string-rfmxltemxacprbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setrbwfiltertype__string-rfmxltemxacprbwfiltertype.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the shape of the RBW filter. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetRbwFilterType(string selectorString, RFmxLteMXAcpRbwFilterType value)RemarksThis method sets the value of AcpRbwFilterType attribute. The default value is FftBased.ParametersNameTypeDescriptionselectorStri

### SetRbwFilterType(string, RFmxLteMXAcpRbwFilterType)

Sets the shape of the RBW filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetRbwFilterType(string selectorString, RFmxLteMXAcpRbwFilterType value)

#### Remarks

This method sets the value of [AcpRbwFilterType](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [FftBased](nationalinstruments-rfmx-ltemx-rfmxltemxacprbwfiltertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxLteMXAcpRbwFilterType | Specifies the shape of the RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setsweeptimeauto__string-rfmxltemxacpsweeptimeauto.html language=enus -->
## TOPIC 00070: SetSweepTimeAuto(string, RFmxLteMXAcpSweepTimeAuto)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setsweeptimeauto__string-rfmxltemxacpsweeptimeauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration-setsweeptimeauto__string-rfmxltemxacpsweeptimeauto.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement computes the sweep time. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetSweepTimeAuto(string selectorString, RFmxLteMXAcpSweepTimeAuto value)RemarksThis method sets the value of AcpSweepTimeAuto attribute. The default value is True.ParametersNameTypeDescrip

### SetSweepTimeAuto(string, RFmxLteMXAcpSweepTimeAuto)

Sets whether the measurement computes the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetSweepTimeAuto(string selectorString, RFmxLteMXAcpSweepTimeAuto value)

#### Remarks

This method sets the value of [AcpSweepTimeAuto](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [True](nationalinstruments-rfmx-ltemx-rfmxltemxacpsweeptimeauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxLteMXAcpSweepTimeAuto | Specifies whether the measurement computes the sweep time. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration.html language=enus -->
## TOPIC 00071: RFmxLteMXAcpConfiguration Class

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacpconfiguration.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the ACP measurement. Derives fromRFmxLteMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.LteMXpublic class RFmxLteMXAcpConfiguration : RFmxLteMXSubObjectMethodsNameDescriptionConfigureAveraging(string, RFmxLteMXAcpAveragingEnabled, int, RFmxLteMXAcpAveragingType)Con

### RFmxLteMXAcpConfiguration Class

Provides methods to configure the ACP measurement.

#### Derives from

- RFmxLteMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public class RFmxLteMXAcpConfiguration : RFmxLteMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| ConfigureAveraging(string, RFmxLteMXAcpAveragingEnabled, int, RFmxLteMXAcpAveragingType) | Configures averaging for the ACP measurement. |
| ConfigureConfigurableNumberOfOffsetsEnabled(string, RFmxLteMXAcpConfigurableNumberOfOffsetsEnabled) | Configures whether the number of offsets will be computed by the measurement or configured by the user. |
| ConfigureMeasurementMethod(string, RFmxLteMXAcpMeasurementMethod) | Configures the method for performing the ACP measurement. |
| ConfigureNoiseCompensationEnabled(string, RFmxLteMXAcpNoiseCompensationEnabled) | Configures compensation of the channel powers for the inherent noise floor of the signal analyzer. |
| ConfigureNumberOfEutraOffsets(string, int) | Configures the number of evolved universal terrestrial radio access adjacent channels of the subblock, when you set the ACP Configurable Number of Offset Enabled method to true. Use "subblock(n)" as the selector string to configure this method. |
| ConfigureNumberOfGsmOffsets(string, int) | Configures the number of GSM adjacent channels of the subblock, when you set the ACP Configurable Number of Offset Enabled method to true. Use "subblock(n)" as the selector string to configure this method. |
| ConfigureNumberOfUtraOffsets(string, int) | Configures the number of universal terrestrial radio access (UTRA) adjacent channels of the subblock, when you set the ACP Configurable Number of Offset Enabled method to true. Use "subblock(n)" as the selector string to configure this method. |
| ConfigurePowerUnits(string, RFmxLteMXAcpPowerUnits) | Configures the units for the absolute power. |
| ConfigureRbwFilter(string, RFmxLteMXAcpRbwAutoBandwidth, double, RFmxLteMXAcpRbwFilterType) | Configures the RBW filter. |
| ConfigureSweepTime(string, RFmxLteMXAcpSweepTimeAuto, double) | Configures the sweep time. |
| ConfigureUtraAndEutraOffsets(string, int, int) | Configures the number of universal terrestrial radio access (UTRA) and evolved universal terrestrial radio access (E-UTRA) adjacent channels of the subblock. This method is valid only for uplink single carrier, and contiguous carrier aggregation. In case of uplink non-contiguous multi-carrier and downlink, the number of UTRA/EUTRA offsets are determined from the 3GPP specification. Use "subblock(n)" as the selector string to configure this method. |
| GetAllTracesEnabled(string, out bool) | Gets whether to enable the traces to be stored and retrieved after performing the ACP measurement. |
| GetAmplitudeCorrectionType(string, out RFmxLteMXAcpAmplitudeCorrectionType) | Gets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |
| GetAveragingCount(string, out int) | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxLteMXAcpAveragingEnabled) method to True. |
| GetAveragingEnabled(string, out RFmxLteMXAcpAveragingEnabled) | Gets whether to enable averaging for the ACP measurement. |
| GetAveragingType(string, out RFmxLteMXAcpAveragingType) | Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement. |
| GetComponentCarrierIntegrationBandwidth(string, out double) | Gets the integration bandwidth of the component carrier (CC). This value is expressed in Hz. |
| GetConfigurableNumberOfOffsetsEnabled(string, out RFmxLteMXAcpConfigurableNumberOfOffsetsEnabled) | Gets whether the number of offsets is computed by measurement or configured by you. |
| GetEutraOffsetDefinition(string, out RFmxLteMXAcpEutraOffsetDefinition) | Gets the evolved universal terrestrial radio access (E-UTRA) offset channel definition. |
| GetFarIFOutputPowerOffset(string, out double) | Gets the offset that is needed to adjust the IF output power levels for the offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This method is applicable only when you set the SetIFOutputPowerOffsetAuto(string, RFmxLteMXAcpIFOutputPowerOffsetAuto) method to False and SetMeasurementMethod(string, RFmxLteMXAcpMeasurementMethod) method to DynamicRange. |
| GetFftOverlap(string, out double) | Gets the samples to overlap between the consecutive chunks as a percentage of the ACP Sequential FFT Size property value when you set the SetMeasurementMethod(string, RFmxLteMXAcpMeasurementMethod) method to SequentialFft and the SetFftOverlapMode(string, RFmxLteMXAcpFftOverlapMode) method to UserDefined. |
| GetFftOverlapMode(string, out RFmxLteMXAcpFftOverlapMode) | Gets the overlap mode when you set the SetMeasurementMethod(string, RFmxLteMXAcpMeasurementMethod) method to SequentialFft. In Sequential FFT method, the measurement divides all the acquired samples into smaller FFT chunks of equal size. Then the FFT is computed for each chunk. The resultant FFTs are averaged to get the spectrum used to compute the ACP. |
| GetIFOutputPowerOffsetAuto(string, out RFmxLteMXAcpIFOutputPowerOffsetAuto) | Gets whether the measurement computes an appropriate IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. This method is applicable only when you set the SetMeasurementMethod(string, RFmxLteMXAcpMeasurementMethod) method to DynamicRange. |
| GetMeasurementEnabled(string, out bool) | Gets whether to enable the ACP measurement. |
| GetMeasurementMethod(string, out RFmxLteMXAcpMeasurementMethod) | Gets the method for performing the ACP measurement. |
| GetMeasurementMode(string, out RFmxLteMXAcpMeasurementMode) | Gets whether the measurement calibrates the noise floor of analyzer or performs the ACP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| GetNearIFOutputPowerOffset(string, out double) | Gets the offset that is needed to adjust the IF output power levels for the offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This method is applicable only when you set the SetIFOutputPowerOffsetAuto(string, RFmxLteMXAcpIFOutputPowerOffsetAuto) method to False and SetMeasurementMethod(string, RFmxLteMXAcpMeasurementMethod) method to DynamicRange. |
| GetNoiseCalibrationAveragingAuto(string, out RFmxLteMXAcpNoiseCalibrationAveragingAuto) | Gets whether the RFmx driver automatically computes the averaging count used for instrument noise calibration. |
| GetNoiseCalibrationAveragingCount(string, out int) | Gets the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(string, RFmxLteMXAcpNoiseCalibrationAveragingAuto) method to False. |
| GetNoiseCalibrationMode(string, out RFmxLteMXAcpNoiseCalibrationMode) | Gets whether the noise calibration and measurement is performed automatically by the measurement or by you. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| GetNoiseCompensationEnabled(string, out RFmxLteMXAcpNoiseCompensationEnabled) | Gets whether RFmx driver compensates for the instrument noise while performing the measurement when you set the SetNoiseCalibrationMode(string, RFmxLteMXAcpNoiseCalibrationMode) method to Auto, or when you set the ACP Noise Cal Mode method to Manual and the SetMeasurementMode(string, RFmxLteMXAcpMeasurementMode) method to Measure. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| GetNoiseCompensationType(string, out RFmxLteMXAcpNoiseCompensationType) | Gets the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| GetNumberOfAnalysisThreads(string, out int) | Gets the maximum number of threads used for parallelism for the ACP measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| GetNumberOfEutraOffsets(string, out int) | Gets the number of evolved universal terrestrial radio access (E-UTRA) adjacent channel offsets to be configured at offset positions, when you set the ACP Configurable Number of Offset Enabled method to True. |
| GetNumberOfGsmOffsets(string, out int) | Gets the number of GSM adjacent channel offsets to be configured when you set the SetBandwidth(string, double) to 200.0 k and the ACP Configurable Number of Offset Enabled method to True. |
| GetNumberOfStandaloneNBIoTOffsets(string, out int) | Gets the number of Standalone NB-IoT adjacent channel offsets to be configured when you set the SetBandwidth(string, double) to 200.0 k, SetLinkDirection(string, RFmxLteMXLinkDirection) to Downlink and the ACP Configurable Number of Offset Enabled method to True. |
| GetNumberOfUtraOffsets(string, out int) | Gets the number of universal terrestrial radio access (UTRA) adjacent channel offsets to be configured at offset positions, when you set the ACP Configurable Number of Offset Enabled method to True. |
| GetOffsetFrequency(string, out double) | Gets the offset frequency of an offset channel. This value is expressed in Hz. When you set the SetLinkDirection(string, RFmxLteMXLinkDirection) method to Uplink, the offset frequency is computed from the center of a reference component carrier/subblock to the center of the nearest RBW filter of the offset channel. When you set the Link Direction method to Downlink, the offset frequency is computed from the center of the closest component carrier to the center of the nearest RBW filter of the offset channel. |
| GetOffsetIntegrationBandwidth(string, out double) | Gets the integration bandwidth of an offset carrier. This value is expressed in Hz. |
| GetPowerUnits(string, out RFmxLteMXAcpPowerUnits) | Gets the units for the absolute power. |
| GetRbwFilterAutoBandwidth(string, out RFmxLteMXAcpRbwAutoBandwidth) | Gets whether the measurement computes the RBW. |
| GetRbwFilterBandwidth(string, out double) | Gets the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(string, RFmxLteMXAcpRbwAutoBandwidth) method to False. This value is expressed in Hz. |
| GetRbwFilterType(string, out RFmxLteMXAcpRbwFilterType) | Gets the shape of the RBW filter. |
| GetSequentialFftSize(string, out int) | Gets the FFT size, when you set the SetMeasurementMethod(string, RFmxLteMXAcpMeasurementMethod) method to SequentialFft. |
| GetSubblockIntegrationBandwidth(string, out double) | Gets the integration bandwidth of a subblock. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. |
| GetSweepTimeAuto(string, out RFmxLteMXAcpSweepTimeAuto) | Gets whether the measurement computes the sweep time. |
| GetSweepTimeInterval(string, out double) | Gets the sweep time when you set the SetSweepTimeAuto(string, RFmxLteMXAcpSweepTimeAuto) method to False. This value is expressed in seconds. |
| SetAllTracesEnabled(string, bool) | Sets whether to enable the traces to be stored and retrieved after performing the ACP measurement. |
| SetAmplitudeCorrectionType(string, RFmxLteMXAcpAmplitudeCorrectionType) | Sets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |
| SetAveragingCount(string, int) | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxLteMXAcpAveragingEnabled) method to True. |
| SetAveragingEnabled(string, RFmxLteMXAcpAveragingEnabled) | Sets whether to enable averaging for the ACP measurement. |
| SetAveragingType(string, RFmxLteMXAcpAveragingType) | Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement. |
| SetConfigurableNumberOfOffsetsEnabled(string, RFmxLteMXAcpConfigurableNumberOfOffsetsEnabled) | Sets whether the number of offsets is computed by measurement or configured by you. |
| SetEutraOffsetDefinition(string, RFmxLteMXAcpEutraOffsetDefinition) | Sets the evolved universal terrestrial radio access (E-UTRA) offset channel definition. |
| SetFarIFOutputPowerOffset(string, double) | Sets the offset that is needed to adjust the IF output power levels for the offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This method is applicable only when you set the SetIFOutputPowerOffsetAuto(string, RFmxLteMXAcpIFOutputPowerOffsetAuto) method to False and SetMeasurementMethod(string, RFmxLteMXAcpMeasurementMethod) method to DynamicRange. |
| SetFftOverlap(string, double) | Sets the samples to overlap between the consecutive chunks as a percentage of the ACP Sequential FFT Size property value when you set the SetMeasurementMethod(string, RFmxLteMXAcpMeasurementMethod) method to SequentialFft and the SetFftOverlapMode(string, RFmxLteMXAcpFftOverlapMode) method to UserDefined. |
| SetFftOverlapMode(string, RFmxLteMXAcpFftOverlapMode) | Sets the overlap mode when you set the SetMeasurementMethod(string, RFmxLteMXAcpMeasurementMethod) method to SequentialFft. In Sequential FFT method, the measurement divides all the acquired samples into smaller FFT chunks of equal size. Then the FFT is computed for each chunk. The resultant FFTs are averaged to get the spectrum used to compute the ACP. |
| SetIFOutputPowerOffsetAuto(string, RFmxLteMXAcpIFOutputPowerOffsetAuto) | Sets whether the measurement computes an appropriate IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. This method is applicable only when you set the SetMeasurementMethod(string, RFmxLteMXAcpMeasurementMethod) method to DynamicRange. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable the ACP measurement. |
| SetMeasurementMethod(string, RFmxLteMXAcpMeasurementMethod) | Sets the method for performing the ACP measurement. |
| SetMeasurementMode(string, RFmxLteMXAcpMeasurementMode) | Sets whether the measurement calibrates the noise floor of analyzer or performs the ACP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| SetNearIFOutputPowerOffset(string, double) | Sets the offset that is needed to adjust the IF output power levels for the offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This method is applicable only when you set the SetIFOutputPowerOffsetAuto(string, RFmxLteMXAcpIFOutputPowerOffsetAuto) method to False and SetMeasurementMethod(string, RFmxLteMXAcpMeasurementMethod) method to DynamicRange. |
| SetNoiseCalibrationAveragingAuto(string, RFmxLteMXAcpNoiseCalibrationAveragingAuto) | Sets whether the RFmx driver automatically computes the averaging count used for instrument noise calibration. |
| SetNoiseCalibrationAveragingCount(string, int) | Sets the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(string, RFmxLteMXAcpNoiseCalibrationAveragingAuto) method to False. |
| SetNoiseCalibrationMode(string, RFmxLteMXAcpNoiseCalibrationMode) | Sets whether the noise calibration and measurement is performed automatically by the measurement or by you. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| SetNoiseCompensationEnabled(string, RFmxLteMXAcpNoiseCompensationEnabled) | Sets whether RFmx driver compensates for the instrument noise while performing the measurement when you set the SetNoiseCalibrationMode(string, RFmxLteMXAcpNoiseCalibrationMode) method to Auto, or when you set the ACP Noise Cal Mode method to Manual and the SetMeasurementMode(string, RFmxLteMXAcpMeasurementMode) method to Measure. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| SetNoiseCompensationType(string, RFmxLteMXAcpNoiseCompensationType) | Sets the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| SetNumberOfAnalysisThreads(string, int) | Sets the maximum number of threads used for parallelism for the ACP measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| SetNumberOfEutraOffsets(string, int) | Sets the number of evolved universal terrestrial radio access (E-UTRA) adjacent channel offsets to be configured at offset positions, when you set the ACP Configurable Number of Offset Enabled method to True. |
| SetNumberOfGsmOffsets(string, int) | Sets the number of GSM adjacent channel offsets to be configured when you set the SetBandwidth(string, double) to 200.0 k and the ACP Configurable Number of Offset Enabled method to True. |
| SetNumberOfStandaloneNBIoTOffsets(string, int) | Sets the number of Standalone NB-IoT adjacent channel offsets to be configured when you set the SetBandwidth(string, double) to 200.0 k, SetLinkDirection(string, RFmxLteMXLinkDirection) to Downlink and the ACP Configurable Number of Offset Enabled method to True. |
| SetNumberOfUtraOffsets(string, int) | Sets the number of universal terrestrial radio access (UTRA) adjacent channel offsets to be configured at offset positions, when you set the ACP Configurable Number of Offset Enabled method to True. |
| SetPowerUnits(string, RFmxLteMXAcpPowerUnits) | Sets the units for the absolute power. |
| SetRbwFilterAutoBandwidth(string, RFmxLteMXAcpRbwAutoBandwidth) | Sets whether the measurement computes the RBW. |
| SetRbwFilterBandwidth(string, double) | Sets the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(string, RFmxLteMXAcpRbwAutoBandwidth) method to False. This value is expressed in Hz. |
| SetRbwFilterType(string, RFmxLteMXAcpRbwFilterType) | Sets the shape of the RBW filter. |
| SetSequentialFftSize(string, int) | Sets the FFT size, when you set the SetMeasurementMethod(string, RFmxLteMXAcpMeasurementMethod) method to SequentialFft. |
| SetSweepTimeAuto(string, RFmxLteMXAcpSweepTimeAuto) | Sets whether the measurement computes the sweep time. |
| SetSweepTimeInterval(string, double) | Sets the sweep time when you set the SetSweepTimeAuto(string, RFmxLteMXAcpSweepTimeAuto) method to False. This value is expressed in seconds. |
| ValidateNoiseCalibrationData(string, out RFmxLteMXAcpNoiseCalibrationDataValid) | Indicates whether calibration data is valid for the configuration specified by the signal name in the selectorString parameter. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacpmeasurementmode.html language=enus -->
## TOPIC 00072: RFmxLteMXAcpMeasurementMode Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacpmeasurementmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacpmeasurementmode.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement calibrates the noise floor of analyzer or performs the ACP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXAcpMeasurementMode

### RFmxLteMXAcpMeasurementMode Enumeration

Specifies whether the measurement calibrates the noise floor of analyzer or performs the ACP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXAcpMeasurementMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Measure | 0 | ACP measurement is performed on the acquired signal. |
| CalibrateNoiseFloor | 1 | Manual noise calibration of the signal analyzer is performed for the ACP measurement. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacpnoisecalibrationaveragingauto.html language=enus -->
## TOPIC 00073: RFmxLteMXAcpNoiseCalibrationAveragingAuto Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacpnoisecalibrationaveragingauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacpnoisecalibrationaveragingauto.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the RFmx driver automatically computes the averaging count used for instrument noise calibration. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXAcpNoiseCalibrationAveragingAutoMembersNameValueDescriptionFalse0The RFmx driver uses the averages that you set for

### RFmxLteMXAcpNoiseCalibrationAveragingAuto Enumeration

Specifies whether the RFmx driver automatically computes the averaging count used for instrument noise calibration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXAcpNoiseCalibrationAveragingAuto

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The RFmx driver uses the averages that you set for SetNoiseCalibrationAveragingCount(string, int) method. |
| True | 1 | The RFmx driver uses the following averaging counts: |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacpnoisecalibrationdatavalid.html language=enus -->
## TOPIC 00074: RFmxLteMXAcpNoiseCalibrationDataValid Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacpnoisecalibrationdatavalid.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacpnoisecalibrationdatavalid.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether the calibration data is valid. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXAcpNoiseCalibrationDataValidMembersNameValueDescriptionFalse0Returns false if the calibration data is not present for the specified configuration or if the difference between the curren

### RFmxLteMXAcpNoiseCalibrationDataValid Enumeration

Returns whether the calibration data is valid.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXAcpNoiseCalibrationDataValid

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Returns false if the calibration data is not present for the specified configuration or if the difference between the current device temperature and the calibration temperature exceeds the [-5°C, 5°C] range. |
| True | 1 | Returns true if the calibration data is present for the configuration specified by the signal name in the Selector string parameter. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacppowerunits.html language=enus -->
## TOPIC 00075: RFmxLteMXAcpPowerUnits Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacppowerunits.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacppowerunits.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units for absolute power. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXAcpPowerUnitsMembersNameValueDescriptiondBm0The absolute powers are reported in dBm. dBmByHz1The absolute powers are reported in dBm/Hz.

### RFmxLteMXAcpPowerUnits Enumeration

Specifies the units for absolute power.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXAcpPowerUnits

#### Members

| Name | Value | Description |
| --- | --- | --- |
| dBm | 0 | The absolute powers are reported in dBm. |
| dBmByHz | 1 | The absolute powers are reported in dBm/Hz. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacprbwautobandwidth.html language=enus -->
## TOPIC 00076: RFmxLteMXAcpRbwAutoBandwidth Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacprbwautobandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacprbwautobandwidth.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the RBW. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXAcpRbwAutoBandwidthMembersNameValueDescriptionFalse0The measurement uses the RBW that you specify in the SetRbwFilterBandwidth(string, double) method. True1The measurement computes

### RFmxLteMXAcpRbwAutoBandwidth Enumeration

Specifies whether the measurement computes the RBW.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXAcpRbwAutoBandwidth

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement uses the RBW that you specify in the SetRbwFilterBandwidth(string, double) method. |
| True | 1 | The measurement computes the RBW. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxacprbwfiltertype.html language=enus -->
## TOPIC 00077: RFmxLteMXAcpRbwFilterType Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxacprbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxacprbwfiltertype.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of the RBW filter. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXAcpRbwFilterTypeMembersNameValueDescriptionFftBased0No RBW filtering is performed. Gaussian1An RBW filter with a Gaussian response is applied. Flat2An RBW filter with a flat response is applied

### RFmxLteMXAcpRbwFilterType Enumeration

Specifies the shape of the RBW filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXAcpRbwFilterType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| FftBased | 0 | No RBW filtering is performed. |
| Gaussian | 1 | An RBW filter with a Gaussian response is applied. |
| Flat | 2 | An RBW filter with a flat response is applied. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxchpconfiguration-setnoisecalibrationaveragingauto__string-rfmxltemxchpnoisecalibrationaveragingauto.html language=enus -->
## TOPIC 00078: SetNoiseCalibrationAveragingAuto(string, RFmxLteMXChpNoiseCalibrationAveragingAuto)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxchpconfiguration-setnoisecalibrationaveragingauto__string-rfmxltemxchpnoisecalibrationaveragingauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxchpconfiguration-setnoisecalibrationaveragingauto__string-rfmxltemxchpnoisecalibrationaveragingauto.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the RFmx driver automatically computes the averaging count used for instrument noise calibration. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetNoiseCalibrationAveragingAuto(string selectorString, RFmxLteMXChpNoiseCalibrationAveragingAuto value)RemarksThis method sets the

### SetNoiseCalibrationAveragingAuto(string, RFmxLteMXChpNoiseCalibrationAveragingAuto)

Sets whether the RFmx driver automatically computes the averaging count used for instrument noise calibration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetNoiseCalibrationAveragingAuto(string selectorString, RFmxLteMXChpNoiseCalibrationAveragingAuto value)

#### Remarks

This method sets the value of [ChpNoiseCalibrationAveragingAuto](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [True](nationalinstruments-rfmx-ltemx-rfmxltemxchpnoisecalibrationaveragingauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxLteMXChpNoiseCalibrationAveragingAuto | Specifies whether the RFmx driver automatically computes the averaging count used for instrument noise calibration. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxchpconfiguration-setnoisecalibrationaveragingcount__string-int.html language=enus -->
## TOPIC 00079: SetNoiseCalibrationAveragingCount(string, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxchpconfiguration-setnoisecalibrationaveragingcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxchpconfiguration-setnoisecalibrationaveragingcount__string-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(string, RFmxLteMXChpNoiseCalibrationAveragingAuto) method to False. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetNoiseCalibrationAveragingCount(string selectorString, int value)Remar

### SetNoiseCalibrationAveragingCount(string, int)

Sets the averaging count used for noise calibration when you set the [SetNoiseCalibrationAveragingAuto(string, RFmxLteMXChpNoiseCalibrationAveragingAuto)](nationalinstruments-rfmx-ltemx-rfmxltemxchpconfiguration-setnoisecalibrationaveragingauto__string-rfmxltemxchpnoisecalibrationaveragingauto.html) method to [False](nationalinstruments-rfmx-ltemx-rfmxltemxchpnoisecalibrationaveragingauto.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetNoiseCalibrationAveragingCount(string selectorString, int value)

#### Remarks

This method sets the value of [ChpNoiseCalibrationAveragingCount](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 32.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(string, RFmxLteMXChpNoiseCalibrationAveragingAuto) method to False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxchpnoisecalibrationmode.html language=enus -->
## TOPIC 00080: RFmxLteMXChpNoiseCalibrationMode Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxchpnoisecalibrationmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxchpnoisecalibrationmode.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the noise calibration and measurement is performed automatically by the measurement or initiated by you. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXC

### RFmxLteMXChpNoiseCalibrationMode Enumeration

Specifies whether the noise calibration and measurement is performed automatically by the measurement or initiated by you. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXChpNoiseCalibrationMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Manual | 0 | When you set the SetMeasurementMode(string, RFmxLteMXChpMeasurementMode) method to Calibrate Noise Floor, you can initiate instrument noise calibration for CHP manually. When you set the CHP Meas Mode method to Measure, you can initiate the CHP measurement manually. |
| Auto | 1 | When you set the SetNoiseCompensationEnabled(string, RFmxLteMXChpNoiseCompensationEnabled) method to True, the RFmx driver sets the Input Isolation Enabled method to Enabled and calibrates the instrument noise in the current state of the instrument. The RFmx driver then resets the Input Isolation Enabled method and performs the CHP measurement, including compensation for the noise contribution of the instrument. The RFmx driver skips noise calibration in this mode if valid noise calibration data is already cached. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxchpnoisecompensationtype.html language=enus -->
## TOPIC 00081: RFmxLteMXChpNoiseCompensationType Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxchpnoisecompensationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxchpnoisecompensationtype.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXChpNoiseCompensationTypeMembersNameValueDescriptionAnalyzerAndTermination0Compensates

### RFmxLteMXChpNoiseCompensationType Enumeration

Specifies the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXChpNoiseCompensationType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AnalyzerAndTermination | 0 | Compensates for noise from the analyzer and the 50 ohm termination. The measured power values are in excess of the thermal noise floor. |
| AnalyzerOnly | 1 | Compensates only for analyzer noise. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxchpresults-getsubblockintegrationbandwidth__string-out.html language=enus -->
## TOPIC 00082: GetSubblockIntegrationBandwidth(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxchpresults-getsubblockintegrationbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxchpresults-getsubblockintegrationbandwidth__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the integration bandwidth used in calculating the power of the subblock. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. This value is expressed in Hz. Use "subblock(n)" as the selector string to read this

### GetSubblockIntegrationBandwidth(string, out double)

Gets the integration bandwidth used in calculating the power of the subblock. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. This value is expressed in Hz. Use "subblock(n)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetSubblockIntegrationBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [ChpResultsSubblockIntegrationBandwidth](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Subblock number. Example: "Subblock0", "result::r1/Subblock0". You can use the BuildSubblockString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the integration bandwidth used in calculating the power of the subblock. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. This value is expressed in Hz. Use "subblock(n)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXChpResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxchpresults-getsubblockpower__string-out.html language=enus -->
## TOPIC 00083: GetSubblockPower(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxchpresults-getsubblockpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxchpresults-getsubblockpower__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the sum of total power of all the frequency bins over the integration bandwidth of the subblock. This value includes the power in inter-carrier gaps within a subblock. This value is expressed in dBm. Use "subblock(n)" as the selector string to read this result. SyntaxNamespace: NationalInstrume

### GetSubblockPower(string, out double)

Gets the sum of total power of all the frequency bins over the integration bandwidth of the subblock. This value includes the power in inter-carrier gaps within a subblock. This value is expressed in dBm. Use "subblock(n)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetSubblockPower(string selectorString, out double value)

#### Remarks

This method gets the value of [ChpResultsSubblockPower](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Subblock number. Example: "Subblock0", "result::r1/Subblock0". You can use the BuildSubblockString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the sum of total power of all the frequency bins over the integration bandwidth of the subblock. This value includes the power in inter-carrier gaps within a subblock. This value is expressed in dBm. Use "subblock(n)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXChpResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxchpresults-gettotalaggregatedpower__string-out.html language=enus -->
## TOPIC 00084: GetTotalAggregatedPower(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxchpresults-gettotalaggregatedpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxchpresults-gettotalaggregatedpower__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the total power of all the subblocks. This value is expressed in dBm. The power in each subblock is the sum of powers of all the frequency bins over the integration bandwidth of the subblocks. This value includes the power in the inter-carrier gaps within a subblock, but it does not include the

### GetTotalAggregatedPower(string, out double)

Gets the total power of all the subblocks. This value is expressed in dBm. The power in each subblock is the sum of powers of all the frequency bins over the integration bandwidth of the subblocks. This value includes the power in the inter-carrier gaps within a subblock, but it does not include the power within the subblock gaps.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetTotalAggregatedPower(string selectorString, out double value)

#### Remarks

This method gets the value of [ChpResultsTotalAggregatedPower](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the total power of all the subblocks. This value is expressed in dBm. The power in each subblock is the sum of powers of all the frequency bins over the integration bandwidth of the subblocks. This value includes the power in the inter-carrier gaps within a subblock, but it does not include the power within the subblock gaps. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXChpResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxchpresults.html language=enus -->
## TOPIC 00085: RFmxLteMXChpResults Class

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxchpresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxchpresults.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the CHP measurement results. Derives fromRFmxLteMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.LteMXpublic class RFmxLteMXChpResults : RFmxLteMXSubObjectPropertiesNameDescriptionComponentCarrierGets the RFmxLteMXChpComponentCarrierResults instance that provid

### RFmxLteMXChpResults Class

Provides methods to fetch and read the CHP measurement results.

#### Derives from

- RFmxLteMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public class RFmxLteMXChpResults : RFmxLteMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| ComponentCarrier | Gets the RFmxLteMXChpComponentCarrierResults instance that provides methods to fetch and read the CHP Component Carrier results. |

#### Methods

| Name | Description |
| --- | --- |
| FetchSpectrum(string, double, ref Spectrum< float >) | Fetches the spectrum used for CHP measurements. |
| FetchSubblockMeasurement(string, double, out double, out double, out double) | Returns the power, integration bandwidth and center frequency of the subblock. Use "subblock(n)" as the selector string to read results from this method. |
| FetchTotalAggregatedPower(string, double, out double) | Fetches the sum of powers in all the subblocks. |
| GetSubblockFrequency(string, out double) | Gets the absolute center frequency of the subblock. This value is the center of the subblock integration bandwidth. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. This value is expressed in Hz. Use "subblock(n)" as the selector string to read this result. |
| GetSubblockIntegrationBandwidth(string, out double) | Gets the integration bandwidth used in calculating the power of the subblock. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. This value is expressed in Hz. Use "subblock(n)" as the selector string to read this result. |
| GetSubblockPower(string, out double) | Gets the sum of total power of all the frequency bins over the integration bandwidth of the subblock. This value includes the power in inter-carrier gaps within a subblock. This value is expressed in dBm. Use "subblock(n)" as the selector string to read this result. |
| GetTotalAggregatedPower(string, out double) | Gets the total power of all the subblocks. This value is expressed in dBm. The power in each subblock is the sum of powers of all the frequency bins over the integration bandwidth of the subblocks. This value includes the power in the inter-carrier gaps within a subblock, but it does not include the power within the subblock gaps. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxchpsweeptimeauto.html language=enus -->
## TOPIC 00086: RFmxLteMXChpSweepTimeAuto Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxchpsweeptimeauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxchpsweeptimeauto.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the sweep time. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXChpSweepTimeAutoMembersNameValueDescriptionFalse0The measurement uses the sweep time that you specify in the SetSweepTimeInterval(string, double) method. True1The measuremen

### RFmxLteMXChpSweepTimeAuto Enumeration

Specifies whether the measurement computes the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXChpSweepTimeAuto

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement uses the sweep time that you specify in the SetSweepTimeInterval(string, double) method. |
| True | 1 | The measurement uses a sweep time of 1 ms. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-configurecellspecificratio__string-rfmxltemxdownlinkuserdefinedratio.html language=enus -->
## TOPIC 00087: ConfigureCellSpecificRatio(string, RFmxLteMXDownlinkUserDefinedRatio)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-configurecellspecificratio__string-rfmxltemxdownlinkuserdefinedratio.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-configurecellspecificratio__string-rfmxltemxdownlinkuserdefinedratio.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the cellspecificratio parameter. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ConfigureCellSpecificRatio(string selectorString, RFmxLteMXDownlinkUserDefinedRatio cellSpecificRatio)Par

### ConfigureCellSpecificRatio(string, RFmxLteMXDownlinkUserDefinedRatio)

Configures the *cellspecificratio* parameter. 
 Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureCellSpecificRatio(string selectorString, RFmxLteMXDownlinkUserDefinedRatio cellSpecificRatio)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the signal name, subblock number and carrier number. Example:"subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| cellSpecificRatio | RFmxLteMXDownlinkUserDefinedRatio | Specifies the ratio ρb/ρa for the cell-specific ratio of one, two, or four cell-specific antenna ports as described in Table 5.2-1 in section 5.2 of the 3GPP TS 36.213 Specifications. This parameter determines the power of the channel resource element (RE) in the symbols that do not contain the reference symbols. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-configuredownlinktestmodel__string-rfmxltemxdownlinktestmodel.html language=enus -->
## TOPIC 00088: ConfigureDownlinkTestModel(string, RFmxLteMXDownlinkTestModel)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-configuredownlinktestmodel__string-rfmxltemxdownlinktestmodel.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-configuredownlinktestmodel__string-rfmxltemxdownlinktestmodel.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the E-UTRA Test Model type. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ConfigureDownlinkTestModel(string selectorString, RFmxLteMXDownlinkTestModel downlinkTestModel)ParametersNameT

### ConfigureDownlinkTestModel(string, RFmxLteMXDownlinkTestModel)

Configures the E-UTRA Test Model type. 
 Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureDownlinkTestModel(string selectorString, RFmxLteMXDownlinkTestModel downlinkTestModel)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the signal name, subblock number and carrier number. Example:"subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| downlinkTestModel | RFmxLteMXDownlinkTestModel | Specifies the E-UTRA Test Model type when you set the SetDownlinkChannelConfigurationMode(string, RFmxLteMXDownlinkChannelConfigurationMode) method to TestModel. Refer to section 6.1.1 of the 3GPP 36.141 specification for more information regarding test model configurations. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-configurenbiotcomponentcarrier__string-int-rfmxltemxnbiotuplinksubcarrierspacing.html language=enus -->
## TOPIC 00089: ConfigureNBIoTComponentCarrier(string, int, RFmxLteMXNBIoTUplinkSubcarrierSpacing)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-configurenbiotcomponentcarrier__string-int-rfmxltemxnbiotuplinksubcarrierspacing.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-configurenbiotcomponentcarrier__string-int-rfmxltemxnbiotuplinksubcarrierspacing.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Ncell ID and Uplink Subcarrier Spacing parameters for the NB-IoT signal. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ConfigureNBIoTComponentCarrier(string selectorString, int nCe

### ConfigureNBIoTComponentCarrier(string, int, RFmxLteMXNBIoTUplinkSubcarrierSpacing)

Configures the Ncell ID and Uplink Subcarrier Spacing parameters for the NB-IoT signal. 
 Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureNBIoTComponentCarrier(string selectorString, int nCellID, RFmxLteMXNBIoTUplinkSubcarrierSpacing uplinkSubcarrierSpacing)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the signal name, subblock number and carrier number. Example:"subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| nCellID | int | Specifies the narrowband physical layer cell identity. |
| uplinkSubcarrierSpacing | RFmxLteMXNBIoTUplinkSubcarrierSpacing | Specifies the subcarrier bandwidth of an NB-IoT signal. This parameter specifies the spacing between adjacent subcarriers. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-configurenpuschdmrs__string-rfmxltemxnpuschdmrsbasesequencemode-int-int-rfmxltemxnpuschdmrsgrouphoppingenabled-int.html language=enus -->
## TOPIC 00090: ConfigureNPuschDmrs(string, RFmxLteMXNPuschDmrsBaseSequenceMode, int, int, RFmxLteMXNPuschDmrsGroupHoppingEnabled, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-configurenpuschdmrs__string-rfmxltemxnpuschdmrsbasesequencemode-int-int-rfmxltemxnpuschdmrsgrouphoppingenabled-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-configurenpuschdmrs__string-rfmxltemxnpuschdmrsbasesequencemode-int-int-rfmxltemxnpuschdmrsgrouphoppingenabled-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the base sequence mode, base sequence index, cyclic shift, delta sequence shift of the narrowband physical uplink shared channel (NPUSCH) DMRS and specifies whether group hopping is enabled. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method.Synta

### ConfigureNPuschDmrs(string, RFmxLteMXNPuschDmrsBaseSequenceMode, int, int, RFmxLteMXNPuschDmrsGroupHoppingEnabled, int)

Configures the base sequence mode, base sequence index, cyclic shift, delta sequence shift of the narrowband physical uplink shared channel (NPUSCH) DMRS and specifies whether group hopping is enabled. 
 Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureNPuschDmrs(string selectorString, RFmxLteMXNPuschDmrsBaseSequenceMode nPuschDmrsBaseSequenceMode, int nPuschDmrsBaseSequenceIndex, int nPuschDmrsCyclicShift, RFmxLteMXNPuschDmrsGroupHoppingEnabled nPuschDmrsGroupHoppingEnabled, int nPuschDmrsDeltaSS)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the signal name, subblock number and carrier number. Example:"subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| nPuschDmrsBaseSequenceMode | RFmxLteMXNPuschDmrsBaseSequenceMode | Specifies whether the NPUSCHDMRSBaseSequenceindex is computed by the measurement or user-specified. This parameter is valid when you set the NPUSCHDMRSGroupHoppingEnabled parameter to False, the value of SetNPuschFormat(string, int) method to 1, and the value of NPUSCH Number of Tones method to 3, 6, or 12. |
| nPuschDmrsBaseSequenceIndex | int | Specifies the base sequence index of the NPUSCH DMRS as defined in section 10.1.4.1.2 of the 3GPP TS 36.211 specification. This parameter is valid when you set the NPUSCHDMRSGroupHoppingEnabled parameter to False, the NPUSCHDMRSBaseSequenceMode parameter to Manual, and the value of NPUSCH Number of Tones method to 3, 6, or 12. |
| nPuschDmrsCyclicShift | int | Specifies the cyclic shift of the NPUSCH DMRS as defined in table 10.1.4.1.2-3 of the 3GPP TS 36.211 specification. |
| nPuschDmrsGroupHoppingEnabled | RFmxLteMXNPuschDmrsGroupHoppingEnabled | Specifies whether group hopping is enabled for the NPUSCH DMRS. This parameter is valid when the value of SetNPuschFormat(string, int) is equal to 1. |
| nPuschDmrsDeltaSS | int | Specifies the delta sequence shift of the NPUSCH DMRS that is used to calculate the sequence shift pattern, which in turn is used to compute the sequence group number as defined in section 10.1.4.1.3 of the 3GPP TS 36.211 specification. This parameter is valid when you set the NPUSCHDMRSGroupHoppingEnabled parameter to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-configurenumberofpuschresourceblockclusters__string-int.html language=enus -->
## TOPIC 00091: ConfigureNumberOfPuschResourceBlockClusters(string, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-configurenumberofpuschresourceblockclusters__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-configurenumberofpuschresourceblockclusters__string-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of clusters of resource allocations. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ConfigureNumberOfPuschResourceBlockClusters(string selectorString, int numberOfResourceBlo

### ConfigureNumberOfPuschResourceBlockClusters(string, int)

Configures the number of clusters of resource allocations. 
 Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureNumberOfPuschResourceBlockClusters(string selectorString, int numberOfResourceBlockClusters)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the signal name, subblock number and carrier number. Example:"subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| numberOfResourceBlockClusters | int | Specifies the number resource allocation clusters, with each cluster including one or more consecutive resource blocks. For more information about the physical uplink shared channel (PUSCH) number of clusters, refer to 5.5.2.1.1 of the 3GPP TS 36.213 specification. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-configurepsschmodulationtype__string-rfmxltemxpsschmodulationtype.html language=enus -->
## TOPIC 00092: ConfigurePsschModulationType(string, RFmxLteMXPsschModulationType)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-configurepsschmodulationtype__string-rfmxltemxpsschmodulationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-configurepsschmodulationtype__string-rfmxltemxpsschmodulationtype.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the modulation scheme used in the physical sidelink shared channel (PSSCH) of the signal being measured. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ConfigurePsschModulationType(stri

### ConfigurePsschModulationType(string, RFmxLteMXPsschModulationType)

Configures the modulation scheme used in the physical sidelink shared channel (PSSCH) of the signal being measured. 
 Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigurePsschModulationType(string selectorString, RFmxLteMXPsschModulationType modulationType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the signal name, subblock number and carrier number. Example:"subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| modulationType | RFmxLteMXPsschModulationType | Specifies the modulation scheme used in the PSSCH channel of the signal being measured. The default value is QPSK. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getautoresourceblockdetectionenabled__string-out.html language=enus -->
## TOPIC 00093: GetAutoResourceBlockDetectionEnabled(string, out RFmxLteMXAutoResourceBlockDetectionEnabled)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getautoresourceblockdetectionenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getautoresourceblockdetectionenabled__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the values of the SetPuschModulationType(string, RFmxLteMXPuschModulationType), SetPuschNumberOfResourceBlockClusters(string, int), SetPuschResourceBlockOffset(string, int), and SetPuschNumberOfResourceBlocks(string, int) properties are auto-detected by the measurement or if you specify

### GetAutoResourceBlockDetectionEnabled(string, out RFmxLteMXAutoResourceBlockDetectionEnabled)

Gets whether the values of the [SetPuschModulationType(string, RFmxLteMXPuschModulationType)](nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-setpuschmodulationtype__string-rfmxltemxpuschmodulationtype.html), [SetPuschNumberOfResourceBlockClusters(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-setpuschnumberofresourceblockclusters__string-int.html), [SetPuschResourceBlockOffset(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-setpuschresourceblockoffset__string-int.html), and [SetPuschNumberOfResourceBlocks(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-setpuschnumberofresourceblocks__string-int.html) properties are auto-detected by the measurement or if you specify the values of these properties.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetAutoResourceBlockDetectionEnabled(string selectorString, out RFmxLteMXAutoResourceBlockDetectionEnabled value)

#### Remarks

This method gets the value of [AutoResourceBlockDetectionEnabled](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [True](nationalinstruments-rfmx-ltemx-rfmxltemxautoresourceblockdetectionenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxLteMXAutoResourceBlockDetectionEnabled | Upon return, contains whether the values of the SetPuschModulationType(string, RFmxLteMXPuschModulationType), SetPuschNumberOfResourceBlockClusters(string, int), SetPuschResourceBlockOffset(string, int), and SetPuschNumberOfResourceBlocks(string, int) properties are auto-detected by the measurement or if you specify the values of these properties. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getcyclicprefixmode__string-out.html language=enus -->
## TOPIC 00094: GetCyclicPrefixMode(string, out RFmxLteMXCyclicPrefixMode)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getcyclicprefixmode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getcyclicprefixmode__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the cyclic prefix (CP) duration and the number of symbols in a slot for the signal being measured. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetCyclicPrefixMode(string selectorString, out RFmxLteMXCyclicPrefixMode value)RemarksThis method gets the value of CyclicPrefixMode attri

### GetCyclicPrefixMode(string, out RFmxLteMXCyclicPrefixMode)

Gets the cyclic prefix (CP) duration and the number of symbols in a slot for the signal being measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetCyclicPrefixMode(string selectorString, out RFmxLteMXCyclicPrefixMode value)

#### Remarks

This method gets the value of [CyclicPrefixMode](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [Normal](nationalinstruments-rfmx-ltemx-rfmxltemxcyclicprefixmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxLteMXCyclicPrefixMode | Upon return, contains the cyclic prefix (CP) duration and the number of symbols in a slot for the signal being measured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getdownlinktestmodel__string-out.html language=enus -->
## TOPIC 00095: GetDownlinkTestModel(string, out RFmxLteMXDownlinkTestModel)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getdownlinktestmodel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getdownlinktestmodel__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the E-UTRA Test Model type when you set the SetDownlinkChannelConfigurationMode(string, RFmxLteMXDownlinkChannelConfigurationMode) method to TestModel. Refer to section 6.1.1 of the 3GPP 36.141 specification for more information regarding test model configurations. SyntaxNamespace: NationalInst

### GetDownlinkTestModel(string, out RFmxLteMXDownlinkTestModel)

Gets the E-UTRA Test Model type when you set the [SetDownlinkChannelConfigurationMode(string, RFmxLteMXDownlinkChannelConfigurationMode)](nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-setdownlinkchannelconfigurationmode__string-rfmxltemxdownlinkchannelconfigurationmode.html) method to [TestModel](nationalinstruments-rfmx-ltemx-rfmxltemxdownlinkchannelconfigurationmode.html). Refer to section 6.1.1 of the *3GPP 36.141* specification for more information regarding test model configurations.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetDownlinkTestModel(string selectorString, out RFmxLteMXDownlinkTestModel value)

#### Remarks

This method gets the value of [DownlinkTestModel](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is TM1.1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out RFmxLteMXDownlinkTestModel | Upon return, contains the E-UTRA Test Model type when you set the SetDownlinkChannelConfigurationMode(string, RFmxLteMXDownlinkChannelConfigurationMode) method to TestModel. Refer to section 6.1.1 of the 3GPP 36.141 specification for more information regarding test model configurations. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getnpuschnumberoftones__string-out.html language=enus -->
## TOPIC 00096: GetNPuschNumberOfTones(string, out int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getnpuschnumberoftones__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getnpuschnumberoftones__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of subcarriers (tones) within the 200 kHz bandwidth that is allocated to the narrowband physical uplink shared channel (NPUSCH). SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetNPuschNumberOfTones(string selectorString, out int value)RemarksThis method gets the value of

### GetNPuschNumberOfTones(string, out int)

Gets the number of subcarriers (tones) within the 200 kHz bandwidth that is allocated to the narrowband physical uplink shared channel (NPUSCH).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetNPuschNumberOfTones(string selectorString, out int value)

#### Remarks

This method gets the value of [NPuschNumberOfTones](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 1.For Format 1 and 15 kHz subcarrier spacing, the valid values are 1, 3, 6, and 12.For Format 1, 3.75 kHz subcarrier spacing, and Format 2, the valid value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the number of subcarriers (tones) within the 200 kHz bandwidth that is allocated to the narrowband physical uplink shared channel (NPUSCH). |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getnssspower__string-out.html language=enus -->
## TOPIC 00097: GetNsssPower(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getnssspower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getnssspower__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power of the NB-IoT secondary synchronization signal (NSSS) relative to the power of the NB-IoT downlink reference signal (NRS). This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetNsssPower(string selectorString, out double value)RemarksThis method g

### GetNsssPower(string, out double)

Gets the power of the NB-IoT secondary synchronization signal (NSSS) relative to the power of the NB-IoT downlink reference signal (NRS). This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetNsssPower(string selectorString, out double value)

#### Remarks

This method gets the value of [NsssPower](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power of the NB-IoT secondary synchronization signal (NSSS) relative to the power of the NB-IoT downlink reference signal (NRS). This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getpdschcw0modulationtype__string-out.html language=enus -->
## TOPIC 00098: GetPdschCW0ModulationType(string, out RFmxLteMXUserDefinedPdschCW0ModulationType)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getpdschcw0modulationtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getpdschcw0modulationtype__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the modulation type of codeword0 PDSCH allocation. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetPdschCW0ModulationType(string selectorString, out RFmxLteMXUserDefinedPdschCW0ModulationType value)RemarksThis method gets the value of PdschCW0ModulationType attribute.The default va

### GetPdschCW0ModulationType(string, out RFmxLteMXUserDefinedPdschCW0ModulationType)

Gets the modulation type of codeword0 PDSCH allocation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetPdschCW0ModulationType(string selectorString, out RFmxLteMXUserDefinedPdschCW0ModulationType value)

#### Remarks

This method gets the value of [PdschCW0ModulationType](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.The default value is [Qpsk](nationalinstruments-rfmx-ltemx-rfmxltemxuserdefinedpdschcw0modulationtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, subframe number and pdsch number. Example: "pdsch0" or "subframe0" or "carrier0" or "subblock0" or "subblock0/carrier0/subframe0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | out RFmxLteMXUserDefinedPdschCW0ModulationType | Upon return, contains the modulation type of codeword0 PDSCH allocation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getpsschmodulationtype__string-out.html language=enus -->
## TOPIC 00099: GetPsschModulationType(string, out RFmxLteMXPsschModulationType)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getpsschmodulationtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getpsschmodulationtype__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the modulation scheme used in physical sidelink shared channel (PSSCH) of the signal being measured. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetPsschModulationType(string selectorString, out RFmxLteMXPsschModulationType value)RemarksThis method gets the value of PsschModulatio

### GetPsschModulationType(string, out RFmxLteMXPsschModulationType)

Gets the modulation scheme used in physical sidelink shared channel (PSSCH) of the signal being measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetPsschModulationType(string selectorString, out RFmxLteMXPsschModulationType value)

#### Remarks

This method gets the value of [PsschModulationType](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [Qpsk](nationalinstruments-rfmx-ltemx-rfmxltemxpsschmodulationtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out RFmxLteMXPsschModulationType | Upon return, contains the modulation scheme used in physical sidelink shared channel (PSSCH) of the signal being measured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getpuschndmrs1__string-out.html language=enus -->
## TOPIC 00100: GetPuschNDmrs1(string, out int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getpuschndmrs1__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getpuschndmrs1__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the n_DMRS_1 value, which is used to calculate the cyclic shift of the demodulation reference signal (DMRS) in a frame. The valid values for this method are defined in table 5.5.2.1.1-2 of the 3GPP TS 36.211 specification. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetPuschNDmrs1

### GetPuschNDmrs1(string, out int)

Gets the n_DMRS_1 value, which is used to calculate the cyclic shift of the demodulation reference signal (DMRS) in a frame. The valid values for this method are defined in table 5.5.2.1.1-2 of the *3GPP TS 36.211* specification.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetPuschNDmrs1(string selectorString, out int value)

#### Remarks

This method gets the value of [PuschNDmrs1](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the n_DMRS_1 value, which is used to calculate the cyclic shift of the demodulation reference signal (DMRS) in a frame. The valid values for this method are defined in table 5.5.2.1.1-2 of the 3GPP TS 36.211 specification. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getpuschresourceblockoffset__string-out.html language=enus -->
## TOPIC 00101: GetPuschResourceBlockOffset(string, out int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getpuschresourceblockoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getpuschresourceblockoffset__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the starting resource block number of a physical uplink shared channel (PUSCH) cluster. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetPuschResourceBlockOffset(string selectorString, out int value)RemarksThis method gets the value of PuschResourceBlockOffset attribute.The default

### GetPuschResourceBlockOffset(string, out int)

Gets the starting resource block number of a physical uplink shared channel (PUSCH) cluster.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetPuschResourceBlockOffset(string selectorString, out int value)

#### Remarks

This method gets the value of [PuschResourceBlockOffset](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number, subblock number and cluster number. Example: "carrier0" or "subblock0" or "cluster0" or "subblock0/carrier0/cluster0". You can use the BuildClusterString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the starting resource block number of a physical uplink shared channel (PUSCH) cluster. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getsrsbhop__string-out.html language=enus -->
## TOPIC 00102: GetSrsbHop(string, out int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getsrsbhop__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-getsrsbhop__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the SRS hopping bandwidth bhop. Frequency hopping for SRS signal is enabled when the value of SRS b_hop method is less than the value of SetSrsBSrs(string, int) method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetSrsbHop(string selectorString, out int value)RemarksThis method g

### GetSrsbHop(string, out int)

Gets the SRS hopping bandwidth bhop. Frequency hopping for SRS signal is enabled when the value of SRS b_hop method is less than the value of [SetSrsBSrs(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-setsrsbsrs__string-int.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetSrsbHop(string selectorString, out int value)

#### Remarks

This method gets the value of [SrsbHop](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 3. Valid values are from 0 to 3, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the SRS hopping bandwidth bhop. Frequency hopping for SRS signal is enabled when the value of SRS b_hop method is less than the value of SetSrsBSrs(string, int) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-setcyclicprefixmode__string-rfmxltemxcyclicprefixmode.html language=enus -->
## TOPIC 00103: SetCyclicPrefixMode(string, RFmxLteMXCyclicPrefixMode)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-setcyclicprefixmode__string-rfmxltemxcyclicprefixmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-setcyclicprefixmode__string-rfmxltemxcyclicprefixmode.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the cyclic prefix (CP) duration and the number of symbols in a slot for the signal being measured. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetCyclicPrefixMode(string selectorString, RFmxLteMXCyclicPrefixMode value)RemarksThis method sets the value of CyclicPrefixMode attribute

### SetCyclicPrefixMode(string, RFmxLteMXCyclicPrefixMode)

Sets the cyclic prefix (CP) duration and the number of symbols in a slot for the signal being measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetCyclicPrefixMode(string selectorString, RFmxLteMXCyclicPrefixMode value)

#### Remarks

This method sets the value of [CyclicPrefixMode](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [Normal](nationalinstruments-rfmx-ltemx-rfmxltemxcyclicprefixmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxLteMXCyclicPrefixMode | Specifies the cyclic prefix (CP) duration and the number of symbols in a slot for the signal being measured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-setdmrsoccenabled__string-rfmxltemxdmrsoccenabled.html language=enus -->
## TOPIC 00104: SetDmrsOccEnabled(string, RFmxLteMXDmrsOccEnabled)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-setdmrsoccenabled__string-rfmxltemxdmrsoccenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-setdmrsoccenabled__string-rfmxltemxdmrsoccenabled.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether orthogonal cover codes (OCCs) need to be used on the demodulation reference signal (DMRS) signal. The measurement internally sets this method to TRUE for multi antenna cases. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetDmrsOccEnabled(string selectorString, RFmxLteMXDmrs

### SetDmrsOccEnabled(string, RFmxLteMXDmrsOccEnabled)

Sets whether orthogonal cover codes (OCCs) need to be used on the demodulation reference signal (DMRS) signal. The measurement internally sets this method to TRUE for multi antenna cases.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetDmrsOccEnabled(string selectorString, RFmxLteMXDmrsOccEnabled value)

#### Remarks

This method sets the value of [DmrsOccEnabled](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [False](nationalinstruments-rfmx-ltemx-rfmxltemxdmrsoccenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | RFmxLteMXDmrsOccEnabled | Specifies whether orthogonal cover codes (OCCs) need to be used on the demodulation reference signal (DMRS) signal. The measurement internally sets this method to TRUE for multi antenna cases. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-setdownlinknumberofsubframes__string-int.html language=enus -->
## TOPIC 00105: SetDownlinkNumberOfSubframes(string, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-setdownlinknumberofsubframes__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-setdownlinknumberofsubframes__string-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of unique subframes transmitted by the DUT. If you set the SetDownlinkChannelConfigurationMode(string, RFmxLteMXDownlinkChannelConfigurationMode) method to TestModel, this method will be set to 10 for FDD and 20 for TDD by default. SyntaxNamespace: NationalInstruments.RFmx.LteMXpubli

### SetDownlinkNumberOfSubframes(string, int)

Sets the number of unique subframes transmitted by the DUT. If you set the [SetDownlinkChannelConfigurationMode(string, RFmxLteMXDownlinkChannelConfigurationMode)](nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-setdownlinkchannelconfigurationmode__string-rfmxltemxdownlinkchannelconfigurationmode.html) method to [TestModel](nationalinstruments-rfmx-ltemx-rfmxltemxdownlinkchannelconfigurationmode.html), this method will be set to 10 for FDD and 20 for TDD by default.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetDownlinkNumberOfSubframes(string selectorString, int value)

#### Remarks

This method sets the value of [DownlinkNumberOfSubframes](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 10. Valid values are 10 and 20.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | int | Specifies the number of unique subframes transmitted by the DUT. If you set the SetDownlinkChannelConfigurationMode(string, RFmxLteMXDownlinkChannelConfigurationMode) method to TestModel, this method will be set to 10 for FDD and 20 for TDD by default. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-setemtcanalysisenabled__string-rfmxltemxemtcanalysisenabled.html language=enus -->
## TOPIC 00106: SetEmtcAnalysisEnabled(string, RFmxLteMXEmtcAnalysisEnabled)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-setemtcanalysisenabled__string-rfmxltemxemtcanalysisenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-setemtcanalysisenabled__string-rfmxltemxemtcanalysisenabled.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the component carrier contains enhanced machine type communications (Cat-M1 or Cat-M2) transmission. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetEmtcAnalysisEnabled(string selectorString, RFmxLteMXEmtcAnalysisEnabled value)RemarksThis method sets the value of EmtcAnalys

### SetEmtcAnalysisEnabled(string, RFmxLteMXEmtcAnalysisEnabled)

Sets whether the component carrier contains enhanced machine type communications (Cat-M1 or Cat-M2) transmission.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetEmtcAnalysisEnabled(string selectorString, RFmxLteMXEmtcAnalysisEnabled value)

#### Remarks

This method sets the value of [EmtcAnalysisEnabled](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [False](nationalinstruments-rfmx-ltemx-rfmxltemxemtcanalysisenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | RFmxLteMXEmtcAnalysisEnabled | Specifies whether the component carrier contains enhanced machine type communications (Cat-M1 or Cat-M2) transmission. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-setnpdschmodulationtype__string-rfmxltemxnpdschmodulationtype.html language=enus -->
## TOPIC 00107: SetNpdschModulationType(string, RFmxLteMXNpdschModulationType)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-setnpdschmodulationtype__string-rfmxltemxnpdschmodulationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-setnpdschmodulationtype__string-rfmxltemxnpdschmodulationtype.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the modulation scheme used in NB-IoT physical downlink shared channel (NPDSCH) of the signal being measured. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetNpdschModulationType(string selectorString, RFmxLteMXNpdschModulationType value)RemarksThis method sets the value of NpdschMo

### SetNpdschModulationType(string, RFmxLteMXNpdschModulationType)

Sets the modulation scheme used in NB-IoT physical downlink shared channel (NPDSCH) of the signal being measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetNpdschModulationType(string selectorString, RFmxLteMXNpdschModulationType value)

#### Remarks

This method sets the value of [NpdschModulationType](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.The default value is [Qpsk](nationalinstruments-rfmx-ltemx-rfmxltemxnpdschmodulationtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0/carrier0" or "subblock0/carrier0/subframe0". You can use the BuildSubframeString(string, int) method to build the selector string. |
| value | RFmxLteMXNpdschModulationType | Specifies the NPDSCH Modulation Type. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxconstants-diopfi5.html language=enus -->
## TOPIC 00108: DioPfi5

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxconstants-diopfi5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxconstants-diopfi5.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic const string DioPfi5

### DioPfi5

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public const string DioPfi5

Parent topic:

RFmxLteMXConstants Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxconstants-diopfi6.html language=enus -->
## TOPIC 00109: DioPfi6

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxconstants-diopfi6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxconstants-diopfi6.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic const string DioPfi6

### DioPfi6

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public const string DioPfi6

Parent topic:

RFmxLteMXConstants Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxconstants-diopfi7.html language=enus -->
## TOPIC 00110: DioPfi7

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxconstants-diopfi7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxconstants-diopfi7.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic const string DioPfi7

### DioPfi7

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public const string DioPfi7

Parent topic:

RFmxLteMXConstants Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxconstants-pulsein.html language=enus -->
## TOPIC 00111: PulseIn

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxconstants-pulsein.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxconstants-pulsein.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic const string PulseIn

### PulseIn

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public const string PulseIn

Parent topic:

RFmxLteMXConstants Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxlist-abortmeasurements__string.html language=enus -->
## TOPIC 00112: AbortMeasurements(string)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxlist-abortmeasurements__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxlist-abortmeasurements__string.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops acquisition and measurements associated with list instance that you specify in the selectorString parameter, which were previously initiated by the Initiate(string, string) method or measurement read methods. Calling this method is optional, unless you want to stop a measurement before it is c

### AbortMeasurements(string)

Stops acquisition and measurements associated with list instance that you specify in the *selectorString* parameter, which were previously initiated by the [Initiate(string, string)](nationalinstruments-rfmx-ltemx-rfmxltemxlist-initiate__string-string.html) method or measurement read methods. Calling this method is optional, unless you want to stop a measurement before it is complete. This method executes even if there is an incoming error.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int AbortMeasurements(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The list name that is passed when creating the list is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXList Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxlist-checkmeasurementstatus__string-out.html language=enus -->
## TOPIC 00113: CheckMeasurementStatus(string, out bool)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxlist-checkmeasurementstatus__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxlist-checkmeasurementstatus__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks the status of the measurement. Use this method to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int CheckMeasurementStatus(string selectorString, out bool i

### CheckMeasurementStatus(string, out bool)

Checks the status of the measurement. Use this method to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int CheckMeasurementStatus(string selectorString, out bool isDone)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| isDone | out bool | Indicates whether the measurement is complete. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXList Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxlist-getliststepall.html language=enus -->
## TOPIC 00114: GetListStepAll()

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxlist-getliststepall.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxlist-getliststepall.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns all list step instances in a list. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic RFmxLteMX GetListStepAll()ReturnsReturns the status code of this method. The status code either indicates success or describes an error or warning condition.

### GetListStepAll()

Returns all list step instances in a list.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public [RFmxLteMX](nationalinstruments-rfmx-ltemx-rfmxltemx.html) GetListStepAll()

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxLteMXList Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxlist-listtype.html language=enus -->
## TOPIC 00115: ListType

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxlist-listtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxlist-listtype.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Type object for RFmxLteMXList. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic Type ListType { get; }RemarksReturns the type of list object.

### ListType

Gets the Type object for RFmxLteMXList.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public Type ListType { get; }

#### Remarks

Returns the type of list object.

Parent topic:

RFmxLteMXList Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxlist-resettodefault__string.html language=enus -->
## TOPIC 00116: ResetToDefault(string)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxlist-resettodefault__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxlist-resettodefault__string.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a list to the default values.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ResetToDefault(string selectorString)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The list name that is passed when creating the list is used.ReturnsReturns the status code of this

### ResetToDefault(string)

Resets a list to the default values.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ResetToDefault(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The list name that is passed when creating the list is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXList Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxlist-waitformeasurementcomplete__string-double.html language=enus -->
## TOPIC 00117: WaitForMeasurementComplete(string, double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxlist-waitformeasurementcomplete__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxlist-waitformeasurementcomplete__string-double.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the specified number for seconds for all the measurements to complete.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int WaitForMeasurementComplete(string selectorString, double timeout)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the re

### WaitForMeasurementComplete(string, double)

Waits for the specified number for seconds for all the measurements to complete.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int WaitForMeasurementComplete(string selectorString, double timeout)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXList Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmeasurementtypes.html language=enus -->
## TOPIC 00118: RFmxLteMXMeasurementTypes Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmeasurementtypes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmeasurementtypes.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of measurement. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXMeasurementTypesMembersNameValueDescriptionAcp0x1Selects ACP measurement. Chp0x2Selects CHP measurement. ModAcc0x4Selects ModAcc measurement. Obw0x8Selects OBW measurement. Sem0x10Selects SEM measu

### RFmxLteMXMeasurementTypes Enumeration

Specifies the type of measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXMeasurementTypes

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Acp | 0x1 | Selects ACP measurement. |
| Chp | 0x2 | Selects CHP measurement. |
| ModAcc | 0x4 | Selects ModAcc measurement. |
| Obw | 0x8 | Selects OBW measurement. |
| Sem | 0x10 | Selects SEM measurement. |
| Pvt | 0x20 | Selects PVT measurement. |
| SlotPhase | 0x40 | Selects SlotPhase measurement. |
| SlotPower | 0x80 | Selects SlotPower measurement. |
| Txp | 0x100 | Selects TXP measurement. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchcompositemagnitudeandphaseerror__string-double-out-out-out-out.html language=enus -->
## TOPIC 00119: FetchCompositeMagnitudeAndPhaseError(string, double, out double, out double, out double, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchcompositemagnitudeandphaseerror__string-double-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchcompositemagnitudeandphaseerror__string-double-out-out-out-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean RMS composite magnitude error, phase error, the maximum peak composite magnitude error, and the phase error. The method result is valid only when you set the SetLinkDirection(string, RFmxLteMXLinkDirection) method to Uplink. Use "carrier(k)" or "subblock(n)/carrier(k)" as the select

### FetchCompositeMagnitudeAndPhaseError(string, double, out double, out double, out double, out double)

Returns the mean RMS composite magnitude error, phase error, the maximum peak composite magnitude error, and the phase error. 
 The method result is valid only when you set the [SetLinkDirection(string, RFmxLteMXLinkDirection)](nationalinstruments-rfmx-ltemx-rfmxltemx-setlinkdirection__string-rfmxltemxlinkdirection.html) method to [Uplink](nationalinstruments-rfmx-ltemx-rfmxltemxlinkdirection.html). 
 Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchCompositeMagnitudeAndPhaseError(string selectorString, double timeout, out double meanRmsCompositeMagnitudeError, out double maximumPeakCompositeMagnitudeError, out double meanRmsCompositePhaseError, out double maximumPeakCompositePhaseError)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| meanRmsCompositeMagnitudeError | out double | Upon return, contains the RMS mean value of the magnitude error calculated over the slots specified by the SetMeasurementLength(string, int) method on all the configured channels. |
| maximumPeakCompositeMagnitudeError | out double | Upon return, contains the peak value of magnitude error calculated over the slots specified by the ModAcc Meas Length method on all the configured channels. |
| meanRmsCompositePhaseError | out double | Upon return, contains the RMS mean value of the phase error calculated over the slots specified by the ModAcc Meas Length method on all the configured channels. This value is expressed in degrees. |
| maximumPeakCompositePhaseError | out double | Upon return, contains the peak value of phase error calculated over the slots specified by the ModAcc Meas Length method on all thee configured channels. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchcsrsevmarray__string-double-ref.html language=enus -->
## TOPIC 00120: FetchCsrsEvmArray(string, double, ref double[])

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchcsrsevmarray__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchcsrsevmarray__string-double-ref.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the array of CSRS EVMs for all the component carriers within the subblock. Use "subblock(n)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchCsrsEvmArray(string selectorString, double timeout, ref double[] meanRmsCsrsEvm)

### FetchCsrsEvmArray(string, double, ref double[])

Fetches the array of CSRS EVMs for all the component carriers within the subblock. 
 Use "subblock(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchCsrsEvmArray(string selectorString, double timeout, ref double[] meanRmsCsrsEvm)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| meanRmsCsrsEvm | ref double[] | Upon return, contains the array of mean values of RMS EVMs calculated on Reference Signal (RS) resource elements over the slots specified by the SetMeasurementLength(string, int) method. When you set the SetEvmUnit(string, RFmxLteMXModAccEvmUnit) method to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit method to dB, the measurement is returned in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchdownlinkdetectedcellid__string-double-out.html language=enus -->
## TOPIC 00121: FetchDownlinkDetectedCellID(string, double, out int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchdownlinkdetectedcellid__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchdownlinkdetectedcellid__string-double-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the detected cell ID. This method is valid only when the measured signal contains primary synchronization signal (PSS) and secondary synchronization signal (SSS). Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.SyntaxNamespace: NationalIns

### FetchDownlinkDetectedCellID(string, double, out int)

Fetches the detected cell ID. This method is valid only when the measured signal contains primary synchronization signal (PSS) and secondary synchronization signal (SSS). 
 Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchDownlinkDetectedCellID(string selectorString, double timeout, out int detectedCellID)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| detectedCellID | out int | Upon return, contains the detected cell ID value. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchdownlinktransmitpowerarray__string-double-ref-ref-ref-ref.html language=enus -->
## TOPIC 00122: FetchDownlinkTransmitPowerArray(string, double, ref double[], ref double[], ref double[], ref double[])

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchdownlinktransmitpowerarray__string-double-ref-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchdownlinktransmitpowerarray__string-double-ref-ref-ref-ref.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the array of reference signal powers and the OFDM symbol transmit powers for all the component carriers within the subblock. Use "subblock(n)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchDownlinkTransmitPowerArray(str

### FetchDownlinkTransmitPowerArray(string, double, ref double[], ref double[], ref double[], ref double[])

Fetches the array of reference signal powers and the OFDM symbol transmit powers for all the component carriers within the subblock. 
 Use "subblock(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchDownlinkTransmitPowerArray(string selectorString, double timeout, ref double[] RSTransmitPower, ref double[] ofdmSymbolTransmitPower, ref double[] reserved1, ref double[] reserved2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| RSTransmitPower | ref double[] | Upon return, contains the array of mean values of power calculated on cell-specific reference signal (CSRS) resource elements over the slots specified by the SetMeasurementLength(string, int) method. This value is expressed in dBm. |
| ofdmSymbolTransmitPower | ref double[] | Upon return, contains the array the mean value of power calculated in one OFDM symbol over the slots specified by the ModAcc Meas Length method. This value is expressed in dBm. |
| reserved1 | ref double[] | This result is not supported in this release and it is reserved for future enhancements. |
| reserved2 | ref double[] | This result is not supported in this release and it is reserved for future enhancements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchevmhighpersymboltrace__string-double-ref.html language=enus -->
## TOPIC 00123: FetchEvmHighPerSymbolTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchevmhighpersymboltrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchevmhighpersymboltrace__string-double-ref.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the EVM per symbol trace for all the configured slots. The EVM is obtained by using the FFT window position, Delta_C+W/2. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchEvmHig

### FetchEvmHighPerSymbolTrace(string, double, ref AnalogWaveform< float >)

Returns the EVM per symbol trace for all the configured slots. The EVM is obtained by using the FFT window position, Delta_C+W/2. 
 Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchEvmHighPerSymbolTrace(string selectorString, double timeout, ref AnalogWaveform< float > evmHighPerSymbol)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| evmHighPerSymbol | ref AnalogWaveform< float > | Upon return, contains the EVM per symbol trace for all the configured slots. The EVM is obtained by using FFT window position, Delta_C+W/2. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchevmpersymboltrace__string-double-ref.html language=enus -->
## TOPIC 00124: FetchEvmPerSymbolTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchevmpersymboltrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchevmpersymboltrace__string-double-ref.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the EVM on each symbol within the SetMeasurementLength(string, int) method averaged across all the allocated subcarriers. Use "carrier(k)" or "subblock(k)/carrier(k)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchEvmPer

### FetchEvmPerSymbolTrace(string, double, ref AnalogWaveform< float >)

Returns the EVM on each symbol within the [SetMeasurementLength(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxmodaccconfiguration-setmeasurementlength__string-int.html) method averaged across all the allocated subcarriers. 
 Use "carrier(k)" or "subblock(k)/carrier(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchEvmPerSymbolTrace(string selectorString, double timeout, ref AnalogWaveform< float > rmsEvmPerSymbol)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| rmsEvmPerSymbol | ref AnalogWaveform< float > | Upon return, contains the starting OFDM symbol position corresponding to Meas Slot Offset parameter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchnpdsch16qamconstellation__string-double-ref.html language=enus -->
## TOPIC 00125: FetchNpdsch16QamConstellation(string, double, ref ComplexSingle[])

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchnpdsch16qamconstellation__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchnpdsch16qamconstellation__string-double-ref.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the narrow-band physical downlink shared channel (NPDSCH) 16 QAM trace. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchNpdsch16QamConstellation(string selectorString, double t

### FetchNpdsch16QamConstellation(string, double, ref ComplexSingle[])

Fetches the narrow-band physical downlink shared channel (NPDSCH) 16 QAM trace. 
 Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchNpdsch16QamConstellation(string selectorString, double timeout, ref ComplexSingle[] qam16Constellation)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| qam16Constellation | ref ComplexSingle[] | Upon return, contains the 16 QAM constellation trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchpdsch1024qamconstellation__string-double-ref.html language=enus -->
## TOPIC 00126: FetchPdsch1024QamConstellation(string, double, ref ComplexSingle[])

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchpdsch1024qamconstellation__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchpdsch1024qamconstellation__string-double-ref.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the physical downlink shared channel (PDSCH) 1024 QAM trace. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchPdsch1024QamConstellation(string selectorString, double timeout, re

### FetchPdsch1024QamConstellation(string, double, ref ComplexSingle[])

Fetches the physical downlink shared channel (PDSCH) 1024 QAM trace. 
 Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchPdsch1024QamConstellation(string selectorString, double timeout, ref ComplexSingle[] qam1024Constellation)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| qam1024Constellation | ref ComplexSingle[] | Upon return, contains the 1024 QAM constellation trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchpdschevmarray__string-double-ref-ref-ref-ref-ref.html language=enus -->
## TOPIC 00127: FetchPdschEvmArray(string, double, ref double[], ref double[], ref double[], ref double[], ref double[])

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchpdschevmarray__string-double-ref-ref-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchpdschevmarray__string-double-ref-ref-ref-ref-ref.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the array of physical downlink shared channel (PDSCH) EVM for all the component carriers within the subblock. Use "subblock(n)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchPdschEvmArray(string selectorString, double t

### FetchPdschEvmArray(string, double, ref double[], ref double[], ref double[], ref double[], ref double[])

Fetches the array of physical downlink shared channel (PDSCH) EVM for all the component carriers within the subblock. 
 Use "subblock(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchPdschEvmArray(string selectorString, double timeout, ref double[] meanRmsEvm, ref double[] meanRmsQpskEvm, ref double[] meanRms16QamEvm, ref double[] meanRms64QamEvm, ref double[] meanRms256QamEvm)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| meanRmsEvm | ref double[] | Upon return, contains the array of mean values of RMS EVMs calculated on the PDSCH data symbols over the slots specified by the SetMeasurementLength(string, int) method. When you set the SetEvmUnit(string, RFmxLteMXModAccEvmUnit) method to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit method to dB, the measurement is returned in dB. |
| meanRmsQpskEvm | ref double[] | Upon return, contains the array of mean values of RMS EVMs calculated on all QPSK modulated PDSCH resource blocks over the slots specified by the ModAcc Meas Length method. When you set the ModAcc EVM Unit method to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit method to dB, the measurement is returned in dB. |
| meanRms16QamEvm | ref double[] | Upon return, contains the array of mean values of RMS EVMs calculated on all 16 QAM modulated PDSCH resource blocks over the slots specified by the ModAcc Meas Length method. When you set the ModAcc EVM Unit method to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit method to dB, the measurement is returned in dB. |
| meanRms64QamEvm | ref double[] | Upon return, contains the array of mean values of RMS EVMs calculated on all 64 QAM modulated PDSCH resource blocks over the slots specified by the ModAcc Meas Length method. When you set the ModAcc EVM Unit method to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit method to dB, the measurement is returned in dB. |
| meanRms256QamEvm | ref double[] | Upon return, contains the array of mean values of RMS EVMs calculated on all 256 QAM modulated PDSCH resource blocks over the slots specified by the ModAcc Meas Length method. When you set the ModAcc EVM Unit method to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit method to dB, the measurement is returned in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchpsschsymbolpowerarray__string-double-ref-ref.html language=enus -->
## TOPIC 00128: FetchPsschSymbolPowerArray(string, double, ref double[], ref double[])

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchpsschsymbolpowerarray__string-double-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchpsschsymbolpowerarray__string-double-ref-ref.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the array of the physical sidelink shared channel (PSSCH) data symbols power and DMRS symbols power. Use "subblock(n)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchPsschSymbolPowerArray(string selectorString, double ti

### FetchPsschSymbolPowerArray(string, double, ref double[], ref double[])

Fetches the array of the physical sidelink shared channel (PSSCH) data symbols power and DMRS symbols power. 
 Use "subblock(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchPsschSymbolPowerArray(string selectorString, double timeout, ref double[] psschMeanDataPower, ref double[] psschMeanDmrsPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| psschMeanDataPower | ref double[] | Upon return, contains the array of the mean value of the power calculated on the PSSCH data symbols over the slots specified by the SetMeasurementLength(string, int) method. This value is expressed in dBm. |
| psschMeanDmrsPower | ref double[] | Upon return, contains the array of the mean value of the power calculated on the PSSCH DMRS symbols over the slots specified by the ModAcc Meas Length method. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchpuschdataevm__string-double-out-out.html language=enus -->
## TOPIC 00129: FetchPuschDataEvm(string, double, out double, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchpuschdataevm__string-double-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchpuschdataevm__string-double-out-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the physical uplink shared channel (PUSCH) data EVM for ModAcc measurements. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchPuschDataEvm(string selectorString, double timeout,

### FetchPuschDataEvm(string, double, out double, out double)

Fetches the physical uplink shared channel (PUSCH) data EVM for ModAcc measurements. 
 Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchPuschDataEvm(string selectorString, double timeout, out double meanRmsDataEvm, out double maximumPeakDataEvm)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| meanRmsDataEvm | out double | Upon return, contains the mean value of the RMS EVMs calculated on PUSCH data symbols over the slots specified by the SetMeasurementLength(string, int) method. |
| maximumPeakDataEvm | out double | Upon return, contains the maximum value of the peak EVMs calculated on PUSCH data symbols over the slots specified by the ModAcc Meas Length method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchpuschsymbolpower__string-double-out-out.html language=enus -->
## TOPIC 00130: FetchPuschSymbolPower(string, double, out double, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchpuschsymbolpower__string-double-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchpuschsymbolpower__string-double-out-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the physical uplink shared channel (PUSCH) symbol power measurement. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchPuschSymbolPower(string selectorString, double timeout, out

### FetchPuschSymbolPower(string, double, out double, out double)

Fetches the physical uplink shared channel (PUSCH) symbol power measurement. 
 Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchPuschSymbolPower(string selectorString, double timeout, out double puschMeanDataPower, out double puschMeanDmrsPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| puschMeanDataPower | out double | Upon return, contains the mean value of the power calculated on PUSCH data symbols over the slots specified by the SetMeasurementLength(string, int) method. |
| puschMeanDmrsPower | out double | Upon return, contains the mean value of the power calculated on PUSCH DMRS over the slots specified by the ModAcc Meas Length method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchpuschsymbolpowerarray__string-double-ref-ref.html language=enus -->
## TOPIC 00131: FetchPuschSymbolPowerArray(string, double, ref double[], ref double[])

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchpuschsymbolpowerarray__string-double-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchpuschsymbolpowerarray__string-double-ref-ref.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of powers of the physical uplink shared channel (PUSCH) data symbols and DMRS of all the component carriers in the subblock. Use "subblock(n)" as the selector string to read results from this method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchPuschSymbolPowerArra

### FetchPuschSymbolPowerArray(string, double, ref double[], ref double[])

Returns an array of powers of the physical uplink shared channel (PUSCH) data symbols and DMRS of all the component carriers in the subblock. 
 Use "subblock(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchPuschSymbolPowerArray(string selectorString, double timeout, ref double[] puschMeanDataPower, ref double[] puschMeanDmrsPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| puschMeanDataPower | ref double[] | Upon return, contains the array of the mean value of the power calculated on PUSCH data symbols over the slots specified by the SetMeasurementLength(string, int) method. |
| puschMeanDmrsPower | ref double[] | Upon return, contains the array of the mean value of the power calculated on PUSCH DMRS over the slots specified by the ModAcc Meas Length method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchspectralflatness__string-double-out-out-out-out.html language=enus -->
## TOPIC 00132: FetchSpectralFlatness(string, double, out double, out double, out double, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchspectralflatness__string-double-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchspectralflatness__string-double-out-out-out-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the spectral flatness measurements of the component carrier. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchSpectralFlatness(string selectorString, double timeout, out double

### FetchSpectralFlatness(string, double, out double, out double, out double, out double)

Returns the spectral flatness measurements of the component carrier. 
 Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchSpectralFlatness(string selectorString, double timeout, out double range1MaximumToRange1Minimum, out double range2MaximumToRange2Minimum, out double range1MaximumToRange2Minimum, out double range2MaximumToRange1Minimum)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| range1MaximumToRange1Minimum | out double | Upon return, contains the peak-to-peak ripple of the EVM equalizer coefficients within the frequency Range1. The frequency Range1 is as defined in section 6.5.2.4.5 of the 3GPP TS 36.521 specification. |
| range2MaximumToRange2Minimum | out double | Upon return, contains the peak-to-peak ripple of the EVM equalizer coefficients within the frequency Range2. The frequency Range2 is defined in section 6.5.2.4.5 of the 3GPP TS 36.521 specification. |
| range1MaximumToRange2Minimum | out double | Upon return, contains the peak-to-peak ripple of the EVM equalizer coefficients from the frequency Range1 to the frequency Range2. The frequency Range1 and 2 are defined in the section 6.5.2.4.5 of the 3GPP TS 36.521 specification. |
| range2MaximumToRange1Minimum | out double | Upon return, contains the peak-to-peak ripple of the EVM equalizer coefficients from frequency Range2 to frequency Range1. The frequency Range1 and 2 are defined in section 6.5.2.4.5 of the 3GPP TS 36.521 specification. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchspectralflatnessarray__string-double-ref-ref-ref-ref.html language=enus -->
## TOPIC 00133: FetchSpectralFlatnessArray(string, double, ref double[], ref double[], ref double[], ref double[])

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchspectralflatnessarray__string-double-ref-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchspectralflatnessarray__string-double-ref-ref-ref-ref.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the arrays of spectral flatness measurements of all component carriers within the subblock. Use "subblock(n)" as the selector string to read results from this method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchSpectralFlatnessArray(string selectorString, double timeout, r

### FetchSpectralFlatnessArray(string, double, ref double[], ref double[], ref double[], ref double[])

Returns the arrays of spectral flatness measurements of all component carriers within the subblock. 
 Use "subblock(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchSpectralFlatnessArray(string selectorString, double timeout, ref double[] range1MaximumToRange1Minimum, ref double[] range2MaximumToRange2Minimum, ref double[] range1MaximumToRange2Minimum, ref double[] range2MaximumToRange1Minimum)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| range1MaximumToRange1Minimum | ref double[] | Upon return, contains the array of the peak-to-peak ripple of the EVM equalizer coefficients within the frequency Range1. The frequency Range1 is as defined in section 6.5.2.4.5 of the 3GPP TS 36.521 specification. |
| range2MaximumToRange2Minimum | ref double[] | Upon return, contains the array of the peak-to-peak ripple of the EVM equalizer coefficients within the frequency Range2. The frequency Range2 is defined in section 6.5.2.4.5 of the 3GPP TS 36.521 specification. |
| range1MaximumToRange2Minimum | ref double[] | Upon return, contains the array of the peak-to-peak ripple of the EVM equalizer coefficients from the frequency Range1 to the frequency Range2. The frequency Range1 and 2 are defined in the section 6.5.2.4.5 of the 3GPP TS 36.521 specification. |
| range2MaximumToRange1Minimum | ref double[] | Upon return, contains the array of the peak-to-peak ripple of the EVM equalizer coefficients from frequency Range2 to frequency Range1. The frequency Range1 and 2 are defined in section 6.5.2.4.5 of the 3GPP TS 36.521 specification. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchspectralflatnesstrace__string-double-ref-ref-ref.html language=enus -->
## TOPIC 00134: FetchSpectralFlatnessTrace(string, double, ref Spectrum< float >, ref Spectrum< float >, ref Spectrum< float >)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchspectralflatnesstrace__string-double-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchspectralflatnesstrace__string-double-ref-ref-ref.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the spectral flatness, upper mask, and lower mask traces. Spectral flatness is the magnitude of equalizer coefficients at each allocated subcarrier. Lower and upper masks are derived from section 6.5.2.4.5 of the 3GPP TS 36.521 specification. Use "carrier(k)" or "subblock(n)/carrier(k)" as t

### FetchSpectralFlatnessTrace(string, double, ref Spectrum< float >, ref Spectrum< float >, ref Spectrum< float >)

Returns the spectral flatness, upper mask, and lower mask traces. Spectral flatness is the magnitude of equalizer coefficients at each allocated subcarrier. Lower and upper masks are derived from section 6.5.2.4.5 of the *3GPP TS 36.521* specification. 
 Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchSpectralFlatnessTrace(string selectorString, double timeout, ref Spectrum< float > spectralFlatness, ref Spectrum< float > spectralFlatnessLowerMask, ref Spectrum< float > spectralFlatnessUpperMask)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| spectralFlatness | ref Spectrum< float > | Specifies the data for a real waveform including the start, delta, and actual values. |
| spectralFlatnessLowerMask | ref Spectrum< float > | Specifies the data for a real waveform including the start, delta, and actual values. |
| spectralFlatnessUpperMask | ref Spectrum< float > | Specifies the data for a real waveform including the start, delta, and actual values. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchsrsconstellation__string-double-ref.html language=enus -->
## TOPIC 00135: FetchSrsConstellation(string, double, ref ComplexSingle[])

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchsrsconstellation__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchsrsconstellation__string-double-ref.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the constellation trace for the SRS channel. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchSrsConstellation(string selectorString, double timeout, ref ComplexSingle[] srsCons

### FetchSrsConstellation(string, double, ref ComplexSingle[])

Fetches the constellation trace for the SRS channel. 
 Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchSrsConstellation(string selectorString, double timeout, ref ComplexSingle[] srsConstellation)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| srsConstellation | ref ComplexSingle[] | Upon return, contains the SRS constellation trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchsrsevm__string-double-out-out.html language=enus -->
## TOPIC 00136: FetchSrsEvm(string, double, out double, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchsrsevm__string-double-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchsrsevm__string-double-out-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean RMS EVM and the mean power for the SRS channel. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchSrsEvm(string selectorString, double timeout, out double meanRmsSrsEvm,

### FetchSrsEvm(string, double, out double, out double)

Fetches the mean RMS EVM and the mean power for the SRS channel. 
 Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchSrsEvm(string selectorString, double timeout, out double meanRmsSrsEvm, out double meanSrsPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| meanRmsSrsEvm | out double | Upon return, contains the mean value of RMS EVMs calculated on the SRS symbols over the slots specified by the SetMeasurementLength(string, int) method. When you set the SetEvmUnit(string, RFmxLteMXModAccEvmUnit) method to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit method to dB, the measurement is returned in dB. |
| meanSrsPower | out double | Upon return, contains the mean value of power calculated on SRS over the slots specified by the ModAcc Meas Length method. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchsrsevmarray__string-double-ref-ref.html language=enus -->
## TOPIC 00137: FetchSrsEvmArray(string, double, ref double[], ref double[])

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchsrsevmarray__string-double-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchsrsevmarray__string-double-ref-ref.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the array of SRS EVMs for all the component carriers within the subblock. This value is expressed in percentage or dB. Use "subblock(n)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchSrsEvmArray(string selectorString, d

### FetchSrsEvmArray(string, double, ref double[], ref double[])

Fetches the array of SRS EVMs for all the component carriers within the subblock. This value is expressed in percentage or dB. 
 Use "subblock(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchSrsEvmArray(string selectorString, double timeout, ref double[] meanRmsSrsEvm, ref double[] meanSrsPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| meanRmsSrsEvm | ref double[] | Upon return, contains the array of mean values of RMS EVMs calculated on the SRS symbols over the slots specified by the SetMeasurementLength(string, int) method. When you set the SetEvmUnit(string, RFmxLteMXModAccEvmUnit) method to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit method to dB, the measurement is returned in dB. |
| meanSrsPower | ref double[] | Upon return, contains the array of mean values of power calculated on SRS over the slots specified by the ModAcc Meas Length method. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchsubblockinbandemissionmargin__string-double-out.html language=enus -->
## TOPIC 00138: FetchSubblockInBandEmissionMargin(string, double, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchsubblockinbandemissionmargin__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchsubblockinbandemissionmargin__string-double-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the margin on non-allocated resource blocks (RBs) within the subblock aggregated bandwidth. This value is expressed in dB. The method result is valid only when you set the SetLinkDirection(string, RFmxLteMXLinkDirection) method to Uplink and the SetTransmitterArchitecture(string, RFmxLteMXTr

### FetchSubblockInBandEmissionMargin(string, double, out double)

Returns the margin on non-allocated resource blocks (RBs) within the subblock aggregated bandwidth. This value is expressed in dB. 
 The method result is valid only when you set the [SetLinkDirection(string, RFmxLteMXLinkDirection)](nationalinstruments-rfmx-ltemx-rfmxltemx-setlinkdirection__string-rfmxltemxlinkdirection.html) method to [Uplink](nationalinstruments-rfmx-ltemx-rfmxltemxlinkdirection.html) and the [SetTransmitterArchitecture(string, RFmxLteMXTransmitterArchitecture)](nationalinstruments-rfmx-ltemx-rfmxltemx-settransmitterarchitecture__string-rfmxltemxtransmitterarchitecture.html) method to [LOPerSubblock](nationalinstruments-rfmx-ltemx-rfmxltemxtransmitterarchitecture.html). 
 Refer to section 6.5.2A.3 of the *3GPP TS 36.521* specification for more information about in-band emission margin. 
 Use "subblock(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchSubblockInBandEmissionMargin(string selectorString, double timeout, out double subblockInBandEmissionMargin)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| subblockInBandEmissionMargin | out double | Upon return, contains the in-band emission margin of a subblock aggregated bandwidth. This value is expressed in dB. The margin is the lowest difference between the in-band emission measurement trace and the limit trace. The limit is defined in section 6.5.2A.3 of the 3GPP TS 36.521 specification. The in-band emissions are a measure of the interference in the non-allocated resources blocks. This result is valid only when you set the SetTransmitterArchitecture(string, RFmxLteMXTransmitterArchitecture) method to LOPerSubblock. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchsubblockinbandemissiontrace__string-double-ref-ref-ref.html language=enus -->
## TOPIC 00139: FetchSubblockInBandEmissionTrace(string, double, ref double[], ref double[], ref double[])

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchsubblockinbandemissiontrace__string-double-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchsubblockinbandemissiontrace__string-double-ref-ref-ref.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the in-band emission trace and the limit trace within the subblock aggregated bandwidth. The in-band emissions are a measure of the interference in the non-allocated resources blocks. The in-band emissions for various regions, such as general, carrier leakage, and I/Q image, are evaluated ac

### FetchSubblockInBandEmissionTrace(string, double, ref double[], ref double[], ref double[])

Returns the in-band emission trace and the limit trace within the subblock aggregated bandwidth. The in-band emissions are a measure of the interference in the non-allocated resources blocks. The in-band emissions for various regions, such as general, carrier leakage, and I/Q image, are evaluated according to the method defined in the *3GPP 36.521* specification, and concatenated to form a composite trace. Limit trace is derived from the limits defined in section 6.5.2A.3 of the *3GPP TS 36.521* specification. 
 The method result is valid only when you set the [SetLinkDirection(string, RFmxLteMXLinkDirection)](nationalinstruments-rfmx-ltemx-rfmxltemx-setlinkdirection__string-rfmxltemxlinkdirection.html) method to [Uplink](nationalinstruments-rfmx-ltemx-rfmxltemxlinkdirection.html) and the [SetTransmitterArchitecture(string, RFmxLteMXTransmitterArchitecture)](nationalinstruments-rfmx-ltemx-rfmxltemx-settransmitterarchitecture__string-rfmxltemxtransmitterarchitecture.html) method to [LOPerSubblock](nationalinstruments-rfmx-ltemx-rfmxltemxtransmitterarchitecture.html). 
 Use "subblock(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchSubblockInBandEmissionTrace(string selectorString, double timeout, ref double[] subblockInBandEmission, ref double[] subblockInBandEmissionMask, ref double[] subblockInBandEmissionRBIndices)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| subblockInBandEmission | ref double[] | Upon return, contains the array of the subblock in-band emission measurement trace. |
| subblockInBandEmissionMask | ref double[] | Upon return, contains the array of the subblock in-band emission mask trace. |
| subblockInBandEmissionRBIndices | ref double[] | Upon return, contains the array of the resource block indices for the subblock in-band emission trace. It can have non integer values depending upon the spacing between carriers. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchsubblockiqimpairments__string-double-out-out-out.html language=enus -->
## TOPIC 00140: FetchSubblockIQImpairments(string, double, out double, out double, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchsubblockiqimpairments__string-double-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchsubblockiqimpairments__string-double-out-out-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean I/Q origin offset, the mean I/Q gain imbalance, and the mean I/Q quadrature error of a subblock. This method is valid only when you set the SetLinkDirection(string, RFmxLteMXLinkDirection) method to Uplink and the SetTransmitterArchitecture(string, RFmxLteMXTransmitterArchitecture)

### FetchSubblockIQImpairments(string, double, out double, out double, out double)

Returns the mean I/Q origin offset, the mean I/Q gain imbalance, and the mean I/Q quadrature error of a subblock. 
 This method is valid only when you set the [SetLinkDirection(string, RFmxLteMXLinkDirection)](nationalinstruments-rfmx-ltemx-rfmxltemx-setlinkdirection__string-rfmxltemxlinkdirection.html) method to [Uplink](nationalinstruments-rfmx-ltemx-rfmxltemxlinkdirection.html) and the [SetTransmitterArchitecture(string, RFmxLteMXTransmitterArchitecture)](nationalinstruments-rfmx-ltemx-rfmxltemx-settransmitterarchitecture__string-rfmxltemxtransmitterarchitecture.html) method to [LOPerSubblock](nationalinstruments-rfmx-ltemx-rfmxltemxtransmitterarchitecture.html). Otherwise, the method returns NaN, as measurements of this result are currently not supported. 
 Use "subblock(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchSubblockIQImpairments(string selectorString, double timeout, out double subblockMeanIQOriginOffset, out double subblockMeanIQGainImbalance, out double subblockMeanIQQuadratureError)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| subblockMeanIQOriginOffset | out double | Upon return, contains the estimated I/Q origin offset averaged over the slots specified by the SetMeasurementLength(string, int) method in a subblock. This value is expressed in dBc. |
| subblockMeanIQGainImbalance | out double | Upon return, contains the estimated I/Q gain imbalance averaged over the slots specified by the ModAcc Meas Length method. This value is expressed in dB. The I/Q gain imbalance is the ratio of the amplitude of the I component to the Q component of the I/Q signal being measured in the subblock. |
| subblockMeanIQQuadratureError | out double | Upon return, contains the estimated quadrature error averaged over the slots specified by the ModAcc Meas Length method. This value is expressed in degrees. Quadrature error is a measure of the skewness of the I component with respect to the Q component of the I/Q signal being measured in the subblock. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchsynchronizationsignalconstellation__string-double-ref-ref.html language=enus -->
## TOPIC 00141: FetchSynchronizationSignalConstellation(string, double, ref ComplexSingle[], ref ComplexSingle[])

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchsynchronizationsignalconstellation__string-double-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchsynchronizationsignalconstellation__string-double-ref-ref.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the constellations traces for PSS and SSS. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchSynchronizationSignalConstellation(string selectorString, double timeout, ref Complex

### FetchSynchronizationSignalConstellation(string, double, ref ComplexSingle[], ref ComplexSingle[])

Fetches the constellations traces for PSS and SSS. 
 Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchSynchronizationSignalConstellation(string selectorString, double timeout, ref ComplexSingle[] sssConstellation, ref ComplexSingle[] pssConstellation)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| sssConstellation | ref ComplexSingle[] | Upon return, contains SSS constellation trace. |
| pssConstellation | ref ComplexSingle[] | Upon return, contains PSS constellation trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchsynchronizationsignalevm__string-double-out-out.html language=enus -->
## TOPIC 00142: FetchSynchronizationSignalEvm(string, double, out double, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchsynchronizationsignalevm__string-double-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchsynchronizationsignalevm__string-double-out-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the primary synchronization signal (PSS) EVM and secondary synchronization signal (SSS) EVM. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchSynchronizationSignalEvm(string sel

### FetchSynchronizationSignalEvm(string, double, out double, out double)

Fetches the primary synchronization signal (PSS) EVM and secondary synchronization signal (SSS) EVM. 
 Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchSynchronizationSignalEvm(string selectorString, double timeout, out double meanRmsPssEvm, out double meanRmsSssEvm)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| meanRmsPssEvm | out double | Upon return, contains the mean value of RMS EVMs calculated on PSS channel over the slots specified by the SetMeasurementLength(string, int) method. When you set the SetEvmUnit(string, RFmxLteMXModAccEvmUnit) method to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit method to dB, the measurement is returned in dB. |
| meanRmsSssEvm | out double | Upon return, contains the mean value of RMS EVMs calculated on SSS channel over the slots specified by the ModAcc Meas Length method. When you set the ModAcc EVM Unit method to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit method to dB, the measurement is returned in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchsynchronizationsignalevmarray__string-double-ref-ref.html language=enus -->
## TOPIC 00143: FetchSynchronizationSignalEvmArray(string, double, ref double[], ref double[])

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchsynchronizationsignalevmarray__string-double-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-fetchsynchronizationsignalevmarray__string-double-ref-ref.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the array of primary synchronization signal (PSS) EVMs and secondary synchronization signal (SSS) EVMS for all the component carriers within a subblock. Use "subblock(n)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchSy

### FetchSynchronizationSignalEvmArray(string, double, ref double[], ref double[])

Fetches the array of primary synchronization signal (PSS) EVMs and secondary synchronization signal (SSS) EVMS for all the component carriers within a subblock. 
 Use "subblock(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchSynchronizationSignalEvmArray(string selectorString, double timeout, ref double[] meanRmsPssEvm, ref double[] meanRmsSssEvm)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| meanRmsPssEvm | ref double[] | Upon return, contains the array of mean values of RMS EVMs calculated on PSS channel over the slots specified by the SetMeasurementLength(string, int) method. When you set the SetEvmUnit(string, RFmxLteMXModAccEvmUnit) method to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit method to dB, the measurement is returned in dB. |
| meanRmsSssEvm | ref double[] | Upon return, contains the array of mean values of RMS EVMs calculated on SSS channel over the slots specified by the ModAcc Meas Length method. When you set the ModAcc EVM Unit method to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit method to dB, the measurement is returned in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getdownlinkdetectedcellid__string-out.html language=enus -->
## TOPIC 00144: GetDownlinkDetectedCellID(string, out int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getdownlinkdetectedcellid__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getdownlinkdetectedcellid__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the detected cell ID value. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetDownlinkDetectedCellID(string selectorString, out int value)RemarksThis method gets the value of ModAccResultsDownlinkDetectedCellID attribute.ParametersNameTypeDescriptionselectorStringstringSpecifies the

### GetDownlinkDetectedCellID(string, out int)

Gets the detected cell ID value.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetDownlinkDetectedCellID(string selectorString, out int value)

#### Remarks

This method gets the value of [ModAccResultsDownlinkDetectedCellID](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the detected cell ID value. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getdownlinknrstransmitpower__string-out.html language=enus -->
## TOPIC 00145: GetDownlinkNrsTransmitPower(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getdownlinknrstransmitpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getdownlinknrstransmitpower__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean value of power calculated on NB-IoT downlink reference signal (NRS) resource elements over the slots specified by the ModAccMeasurementLength method. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetDownlinkNrsTransmitPower(string selectorStr

### GetDownlinkNrsTransmitPower(string, out double)

Gets the mean value of power calculated on NB-IoT downlink reference signal (NRS) resource elements over the slots specified by the [ModAccMeasurementLength](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) method. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetDownlinkNrsTransmitPower(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsDownlinkNrsTransmitPower](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the mean value of power calculated on NB-IoT downlink reference signal (NRS) resource elements over the slots specified by the ModAccMeasurementLength method. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getdownlinkofdmsymboltransmitpower__string-out.html language=enus -->
## TOPIC 00146: GetDownlinkOfdmSymbolTransmitPower(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getdownlinkofdmsymboltransmitpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getdownlinkofdmsymboltransmitpower__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean value of power calculated in one OFDM symbol over the slots specified by the SetMeasurementLength(string, int) method. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetDownlinkOfdmSymbolTransmitPower(string selectorString, out double value)Re

### GetDownlinkOfdmSymbolTransmitPower(string, out double)

Gets the mean value of power calculated in one OFDM symbol over the slots specified by the [SetMeasurementLength(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxmodaccconfiguration-setmeasurementlength__string-int.html) method. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetDownlinkOfdmSymbolTransmitPower(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsDownlinkOfdmSymbolTransmitPower](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the mean value of power calculated in one OFDM symbol over the slots specified by the SetMeasurementLength(string, int) method. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getdownlinkrstransmitpower__string-out.html language=enus -->
## TOPIC 00147: GetDownlinkRSTransmitPower(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getdownlinkrstransmitpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getdownlinkrstransmitpower__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean value of power calculated on cell-specific reference signal (CSRS) resource elements over the slots specified by the SetMeasurementLength(string, int) method. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetDownlinkRSTransmitPower(string sel

### GetDownlinkRSTransmitPower(string, out double)

Gets the mean value of power calculated on cell-specific reference signal (CSRS) resource elements over the slots specified by the [SetMeasurementLength(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxmodaccconfiguration-setmeasurementlength__string-int.html) method. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetDownlinkRSTransmitPower(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsDownlinkRSTransmitPower](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the mean value of power calculated on cell-specific reference signal (CSRS) resource elements over the slots specified by the SetMeasurementLength(string, int) method. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getinbandemissionmargin__string-out.html language=enus -->
## TOPIC 00148: GetInBandEmissionMargin(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getinbandemissionmargin__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getinbandemissionmargin__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the in-band emission margin. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetInBandEmissionMargin(string selectorString, out double value)RemarksThis method gets the value of ModAccResultsInBandEmissionMargin attribute.ParametersNameTypeDescriptionsel

### GetInBandEmissionMargin(string, out double)

Gets the in-band emission margin. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetInBandEmissionMargin(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsInBandEmissionMargin](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the in-band emission margin. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmaximumpeakcompositemagnitudeerror__string-out.html language=enus -->
## TOPIC 00149: GetMaximumPeakCompositeMagnitudeError(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmaximumpeakcompositemagnitudeerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmaximumpeakcompositemagnitudeerror__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak value of the composite magnitude error calculated over the slots specified by the SetMeasurementLength(string, int) method on all the configured channels. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetMaximumPeakCompositeMagnitudeError(string selectorString, out double v

### GetMaximumPeakCompositeMagnitudeError(string, out double)

Gets the peak value of the composite magnitude error calculated over the slots specified by the [SetMeasurementLength(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxmodaccconfiguration-setmeasurementlength__string-int.html) method on all the configured channels.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetMaximumPeakCompositeMagnitudeError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsMaximumPeakCompositeMagnitudeError](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak value of the composite magnitude error calculated over the slots specified by the SetMeasurementLength(string, int) method on all the configured channels. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmaximumpeakcompositephaseerror__string-out.html language=enus -->
## TOPIC 00150: GetMaximumPeakCompositePhaseError(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmaximumpeakcompositephaseerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmaximumpeakcompositephaseerror__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak value of phase error calculated over the slots specified by the SetMeasurementLength(string, int) method on all thee configured channels. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetMaximumPeakCompositePhaseError(string selectorStrin

### GetMaximumPeakCompositePhaseError(string, out double)

Gets the peak value of phase error calculated over the slots specified by the [SetMeasurementLength(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxmodaccconfiguration-setmeasurementlength__string-int.html) method on all thee configured channels. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetMaximumPeakCompositePhaseError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsMaximumPeakCompositePhaseError](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak value of phase error calculated over the slots specified by the SetMeasurementLength(string, int) method on all thee configured channels. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmaximumpeakfrequencyerror__string-out.html language=enus -->
## TOPIC 00151: GetMaximumPeakFrequencyError(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmaximumpeakfrequencyerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmaximumpeakfrequencyerror__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the estimated maximum carrier frequency offset per slot in case of Uplink and per subframe in case of Downlink over the slots specified by the SetMeasurementLength(string, int) method. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetMaximumPeakFrequen

### GetMaximumPeakFrequencyError(string, out double)

Gets the estimated maximum carrier frequency offset per slot in case of Uplink and per subframe in case of Downlink over the slots specified by the [SetMeasurementLength(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxmodaccconfiguration-setmeasurementlength__string-int.html) method. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetMaximumPeakFrequencyError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsMaximumPeakFrequencyError](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the estimated maximum carrier frequency offset per slot in case of Uplink and per subframe in case of Downlink over the slots specified by the SetMeasurementLength(string, int) method. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmaximumpeakiqoriginoffset__string-out.html language=enus -->
## TOPIC 00152: GetMaximumPeakIQOriginOffset(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmaximumpeakiqoriginoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmaximumpeakiqoriginoffset__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the estimated maximum IQ origin offset over the slots specified by the SetMeasurementLength(string, int) method. This value is expressed in dBc. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetMaximumPeakIQOriginOffset(string selectorString, out double value)RemarksThis method gets

### GetMaximumPeakIQOriginOffset(string, out double)

Gets the estimated maximum IQ origin offset over the slots specified by the [SetMeasurementLength(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxmodaccconfiguration-setmeasurementlength__string-int.html) method. This value is expressed in dBc.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetMaximumPeakIQOriginOffset(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsMaximumPeakIQOriginOffset](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the estimated maximum IQ origin offset over the slots specified by the SetMeasurementLength(string, int) method. This value is expressed in dBc. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmeanfrequencyerror__string-out.html language=enus -->
## TOPIC 00153: GetMeanFrequencyError(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmeanfrequencyerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmeanfrequencyerror__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the estimated carrier frequency offset averaged over the slots specified by the SetMeasurementLength(string, int) method. This value is expressed in Hz. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic

### GetMeanFrequencyError(string, out double)

Gets the estimated carrier frequency offset averaged over the slots specified by the [SetMeasurementLength(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxmodaccconfiguration-setmeasurementlength__string-int.html) method. This value is expressed in Hz. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetMeanFrequencyError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsMeanFrequencyError](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the estimated carrier frequency offset averaged over the slots specified by the SetMeasurementLength(string, int) method. This value is expressed in Hz. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmeaniqgainimbalance__string-out.html language=enus -->
## TOPIC 00154: GetMeanIQGainImbalance(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmeaniqgainimbalance__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmeaniqgainimbalance__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the estimated I/Q gain imbalance averaged over the measurement length. The I/Q gain imbalance is the ratio of the amplitude of the I component to the Q component of the I/Q signal being measured. This value is expressed in dB. When you set the CC Bandwidth Method to 200.0 k and the NPUSCH Num T

### GetMeanIQGainImbalance(string, out double)

Gets the estimated I/Q gain imbalance averaged over the measurement length. The I/Q gain imbalance is the ratio of the amplitude of the I component to the Q component of the I/Q signal being measured. This value is expressed in dB.

Note

When you set the CC Bandwidth Method to 200.0 k and the NPUSCH Num Tones Method to 12, this result is available. For other values of NPUSCH Num Tones, this result will be reported as NaN.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetMeanIQGainImbalance(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsMeanIQGainImbalance](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the estimated I/Q gain imbalance averaged over the measurement length. The I/Q gain imbalance is the ratio of the amplitude of the I component to the Q component of the I/Q signal being measured. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmeanquadratureerror__string-out.html language=enus -->
## TOPIC 00155: GetMeanQuadratureError(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmeanquadratureerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmeanquadratureerror__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the estimated quadrature error averaged over the slots specified by the SetMeasurementLength(string, int) method. This value is expressed in degrees. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetMeanQuadratureError(string selectorString, out double value)RemarksThis method gets

### GetMeanQuadratureError(string, out double)

Gets the estimated quadrature error averaged over the slots specified by the [SetMeasurementLength(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxmodaccconfiguration-setmeasurementlength__string-int.html) method. This value is expressed in degrees.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetMeanQuadratureError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsMeanQuadratureError](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the estimated quadrature error averaged over the slots specified by the SetMeasurementLength(string, int) method. This value is expressed in degrees. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmeanrmscompositeevm__string-out.html language=enus -->
## TOPIC 00156: GetMeanRmsCompositeEvm(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmeanrmscompositeevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmeanrmscompositeevm__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean value of the RMS EVMs calculated on all the configured channels, over the slots specified by the SetMeasurementLength(string, int) method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetMeanRmsCompositeEvm(string selectorString, out double value)RemarksThis method gets th

### GetMeanRmsCompositeEvm(string, out double)

Gets the mean value of the RMS EVMs calculated on all the configured channels, over the slots specified by the [SetMeasurementLength(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxmodaccconfiguration-setmeasurementlength__string-int.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetMeanRmsCompositeEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsMeanRmsCompositeEvm](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the mean value of the RMS EVMs calculated on all the configured channels, over the slots specified by the SetMeasurementLength(string, int) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmeanrmscompositemagnitudeerror__string-out.html language=enus -->
## TOPIC 00157: GetMeanRmsCompositeMagnitudeError(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmeanrmscompositemagnitudeerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmeanrmscompositemagnitudeerror__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RMS mean value of the composite magnitude error calculated over the slots specified by the SetMeasurementLength(string, int) method on all the configured channels. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetMeanRmsCompositeMagnitudeError(string selectorString, out double v

### GetMeanRmsCompositeMagnitudeError(string, out double)

Gets the RMS mean value of the composite magnitude error calculated over the slots specified by the [SetMeasurementLength(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxmodaccconfiguration-setmeasurementlength__string-int.html) method on all the configured channels.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetMeanRmsCompositeMagnitudeError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsMeanRmsCompositeMagnitudeError](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the RMS mean value of the composite magnitude error calculated over the slots specified by the SetMeasurementLength(string, int) method on all the configured channels. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmeanrmscsrsevm__string-out.html language=enus -->
## TOPIC 00158: GetMeanRmsCsrsEvm(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmeanrmscsrsevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmeanrmscsrsevm__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean value of RMS EVMs calculated on RS resource elements over the slots specified by the SetMeasurementLength(string, int) method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetMeanRmsCsrsEvm(string selectorString, out double value)RemarksThis method gets the value of ModAcc

### GetMeanRmsCsrsEvm(string, out double)

Gets the mean value of RMS EVMs calculated on RS resource elements over the slots specified by the [SetMeasurementLength(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxmodaccconfiguration-setmeasurementlength__string-int.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetMeanRmsCsrsEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsMeanRmsCsrsEvm](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the mean value of RMS EVMs calculated on RS resource elements over the slots specified by the SetMeasurementLength(string, int) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmeanrmspcfichevm__string-out.html language=enus -->
## TOPIC 00159: GetMeanRmsPcfichEvm(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmeanrmspcfichevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmeanrmspcfichevm__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean value of RMS EVMs calculated on PCFICH channel over the slots specified by the SetMeasurementLength(string, int) method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetMeanRmsPcfichEvm(string selectorString, out double value)RemarksThis method gets the value of ModAccResu

### GetMeanRmsPcfichEvm(string, out double)

Gets the mean value of RMS EVMs calculated on PCFICH channel over the slots specified by the [SetMeasurementLength(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxmodaccconfiguration-setmeasurementlength__string-int.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetMeanRmsPcfichEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsMeanRmsPcfichEvm](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the mean value of RMS EVMs calculated on PCFICH channel over the slots specified by the SetMeasurementLength(string, int) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getnpdschmeanrms16qamevm__string-out.html language=enus -->
## TOPIC 00160: GetNpdschMeanRms16QamEvm(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getnpdschmeanrms16qamevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getnpdschmeanrms16qamevm__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean value of RMS EVMs calculated on all 16QAM modulated NPDSCH subframes/slots specified by the ModAccMeasurementLength method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetNpdschMeanRms16QamEvm(string selectorString, out double value)RemarksThis method gets the value of Mo

### GetNpdschMeanRms16QamEvm(string, out double)

Gets the mean value of RMS EVMs calculated on all 16QAM modulated NPDSCH subframes/slots specified by the [ModAccMeasurementLength](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetNpdschMeanRms16QamEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsNpdschMeanRms16QamEvm](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the mean value of RMS EVMs calculated on all 16QAM modulated NPDSCH subframes/slots specified by the ModAccMeasurementLength method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getnpdschmeanrmsevm__string-out.html language=enus -->
## TOPIC 00161: GetNpdschMeanRmsEvm(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getnpdschmeanrmsevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getnpdschmeanrmsevm__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean value of RMS EVMs calculated on the NB-IoT downlink shared channel (NPDSCH) data symbols over the slots specified by the ModAccMeasurementLength method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetNpdschMeanRmsEvm(string selectorString, out double value)RemarksThis met

### GetNpdschMeanRmsEvm(string, out double)

Gets the mean value of RMS EVMs calculated on the NB-IoT downlink shared channel (NPDSCH) data symbols over the slots specified by the [ModAccMeasurementLength](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetNpdschMeanRmsEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsNpdschMeanRmsEvm](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the mean value of RMS EVMs calculated on the NB-IoT downlink shared channel (NPDSCH) data symbols over the slots specified by the ModAccMeasurementLength method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getnpdschmeanrmsqpskevm__string-out.html language=enus -->
## TOPIC 00162: GetNpdschMeanRmsQpskEvm(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getnpdschmeanrmsqpskevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getnpdschmeanrmsqpskevm__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean value of RMS EVMs calculated on all QPSK modulated NPDSCH subframes/slots specified by the ModAccMeasurementLength method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetNpdschMeanRmsQpskEvm(string selectorString, out double value)RemarksThis method gets the value of ModA

### GetNpdschMeanRmsQpskEvm(string, out double)

Gets the mean value of RMS EVMs calculated on all QPSK modulated NPDSCH subframes/slots specified by the [ModAccMeasurementLength](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetNpdschMeanRmsQpskEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsNpdschMeanRmsQpskEvm](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the mean value of RMS EVMs calculated on all QPSK modulated NPDSCH subframes/slots specified by the ModAccMeasurementLength method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getnpuschmaximumpeakdataevm__string-out.html language=enus -->
## TOPIC 00163: GetNPuschMaximumPeakDataEvm(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getnpuschmaximumpeakdataevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getnpuschmaximumpeakdataevm__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum value of peak EVMs calculated on the narrowband physical uplink shared channel (NPUSCH) data symbols over the slots specified by the SetMeasurementLength(string, int) method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetNPuschMaximumPeakDataEvm(string selectorString,

### GetNPuschMaximumPeakDataEvm(string, out double)

Gets the maximum value of peak EVMs calculated on the narrowband physical uplink shared channel (NPUSCH) data symbols over the slots specified by the [SetMeasurementLength(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxmodaccconfiguration-setmeasurementlength__string-int.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetNPuschMaximumPeakDataEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsNPuschMaximumPeakDataEvm](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the maximum value of peak EVMs calculated on the narrowband physical uplink shared channel (NPUSCH) data symbols over the slots specified by the SetMeasurementLength(string, int) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getnpuschmaximumpeakdmrsevm__string-out.html language=enus -->
## TOPIC 00164: GetNPuschMaximumPeakDmrsEvm(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getnpuschmaximumpeakdmrsevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getnpuschmaximumpeakdmrsevm__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum value of peak EVMs calculated on NPUSCH DMRS over the slots specified by the SetMeasurementLength(string, int) method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetNPuschMaximumPeakDmrsEvm(string selectorString, out double value)RemarksThis method gets the value of M

### GetNPuschMaximumPeakDmrsEvm(string, out double)

Gets the maximum value of peak EVMs calculated on NPUSCH DMRS over the slots specified by the [SetMeasurementLength(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxmodaccconfiguration-setmeasurementlength__string-int.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetNPuschMaximumPeakDmrsEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsNPuschMaximumPeakDmrsEvm](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the maximum value of peak EVMs calculated on NPUSCH DMRS over the slots specified by the SetMeasurementLength(string, int) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getnpuschmeanrmsdmrsevm__string-out.html language=enus -->
## TOPIC 00165: GetNPuschMeanRmsDmrsEvm(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getnpuschmeanrmsdmrsevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getnpuschmeanrmsdmrsevm__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean value of RMS EVMs calculated on the narrowband physical uplink shared channel (NPUSCH) DMRS over the slots specified by the SetMeasurementLength(string, int) method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetNPuschMeanRmsDmrsEvm(string selectorString, out double valu

### GetNPuschMeanRmsDmrsEvm(string, out double)

Gets the mean value of RMS EVMs calculated on the narrowband physical uplink shared channel (NPUSCH) DMRS over the slots specified by the [SetMeasurementLength(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxmodaccconfiguration-setmeasurementlength__string-int.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetNPuschMeanRmsDmrsEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsNPuschMeanRmsDmrsEvm](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the mean value of RMS EVMs calculated on the narrowband physical uplink shared channel (NPUSCH) DMRS over the slots specified by the SetMeasurementLength(string, int) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getpdschmeanrms1024qamevm__string-out.html language=enus -->
## TOPIC 00166: GetPdschMeanRms1024QamEvm(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getpdschmeanrms1024qamevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getpdschmeanrms1024qamevm__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean value of RMS EVMs calculated on all 1024 QAM modulated PDSCH resource blocks over the slots specified by the SetMeasurementLength(string, int) method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetPdschMeanRms1024QamEvm(string selectorString, out double value)RemarksThis

### GetPdschMeanRms1024QamEvm(string, out double)

Gets the mean value of RMS EVMs calculated on all 1024 QAM modulated PDSCH resource blocks over the slots specified by the [SetMeasurementLength(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxmodaccconfiguration-setmeasurementlength__string-int.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetPdschMeanRms1024QamEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsPdschMeanRms1024QamEvm](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the mean value of RMS EVMs calculated on all 1024 QAM modulated PDSCH resource blocks over the slots specified by the SetMeasurementLength(string, int) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getpdschmeanrms16qamevm__string-out.html language=enus -->
## TOPIC 00167: GetPdschMeanRms16QamEvm(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getpdschmeanrms16qamevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getpdschmeanrms16qamevm__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean value of RMS EVMs calculated on all 16QAM modulated PDSCH resource blocks over the slots specified by the SetMeasurementLength(string, int) method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetPdschMeanRms16QamEvm(string selectorString, out double value)RemarksThis meth

### GetPdschMeanRms16QamEvm(string, out double)

Gets the mean value of RMS EVMs calculated on all 16QAM modulated PDSCH resource blocks over the slots specified by the [SetMeasurementLength(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxmodaccconfiguration-setmeasurementlength__string-int.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetPdschMeanRms16QamEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsPdschMeanRms16QamEvm](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the mean value of RMS EVMs calculated on all 16QAM modulated PDSCH resource blocks over the slots specified by the SetMeasurementLength(string, int) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getpdschmeanrms256qamevm__string-out.html language=enus -->
## TOPIC 00168: GetPdschMeanRms256QamEvm(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getpdschmeanrms256qamevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getpdschmeanrms256qamevm__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean value of RMS EVMs calculated on all 256 QAM modulated PDSCH resource blocks over the slots specified by the SetMeasurementLength(string, int) method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetPdschMeanRms256QamEvm(string selectorString, out double value)RemarksThis m

### GetPdschMeanRms256QamEvm(string, out double)

Gets the mean value of RMS EVMs calculated on all 256 QAM modulated PDSCH resource blocks over the slots specified by the [SetMeasurementLength(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxmodaccconfiguration-setmeasurementlength__string-int.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetPdschMeanRms256QamEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsPdschMeanRms256QamEvm](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the mean value of RMS EVMs calculated on all 256 QAM modulated PDSCH resource blocks over the slots specified by the SetMeasurementLength(string, int) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getpeakcompositeevmsymbolindex__string-out.html language=enus -->
## TOPIC 00169: GetPeakCompositeEvmSymbolIndex(string, out int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getpeakcompositeevmsymbolindex__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getpeakcompositeevmsymbolindex__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the symbol index of the GetMaximumPeakCompositeEvm(string, out double) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetPeakCompositeEvmSymbolIndex(string selectorString, out int value)R

### GetPeakCompositeEvmSymbolIndex(string, out int)

Gets the symbol index of the [GetMaximumPeakCompositeEvm(string, out double)](nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getmaximumpeakcompositeevm__string-out.html) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetPeakCompositeEvmSymbolIndex(string selectorString, out int value)

#### Remarks

This method gets the value of [ModAccResultsPeakCompositeEvmSymbolIndex](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the symbol index of the GetMaximumPeakCompositeEvm(string, out double) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getpsschmaximumpeakdataevm__string-out.html language=enus -->
## TOPIC 00170: GetPsschMaximumPeakDataEvm(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getpsschmaximumpeakdataevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getpsschmaximumpeakdataevm__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum value of the peak EVMs calculated on the physical sidelink shared channel (PSSCH) data symbols over the slots specified by the SetMeasurementLength(string, int) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. SyntaxNamespace: National

### GetPsschMaximumPeakDataEvm(string, out double)

Gets the maximum value of the peak EVMs calculated on the physical sidelink shared channel (PSSCH) data symbols over the slots specified by the [SetMeasurementLength(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxmodaccconfiguration-setmeasurementlength__string-int.html) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetPsschMaximumPeakDataEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsPsschMaximumPeakDataEvm](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the maximum value of the peak EVMs calculated on the physical sidelink shared channel (PSSCH) data symbols over the slots specified by the SetMeasurementLength(string, int) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getpsschmaximumpeakdmrsevm__string-out.html language=enus -->
## TOPIC 00171: GetPsschMaximumPeakDmrsEvm(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getpsschmaximumpeakdmrsevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getpsschmaximumpeakdmrsevm__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum value of the peak EVMs calculated on PSSCH DMRS symbols over the slots specified by the SetMeasurementLength(string, int) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetPss

### GetPsschMaximumPeakDmrsEvm(string, out double)

Gets the maximum value of the peak EVMs calculated on PSSCH DMRS symbols over the slots specified by the [SetMeasurementLength(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxmodaccconfiguration-setmeasurementlength__string-int.html) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetPsschMaximumPeakDmrsEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsPsschMaximumPeakDmrsEvm](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the maximum value of the peak EVMs calculated on PSSCH DMRS symbols over the slots specified by the SetMeasurementLength(string, int) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getpsschmeandatapower__string-out.html language=enus -->
## TOPIC 00172: GetPsschMeanDataPower(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getpsschmeandatapower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getpsschmeandatapower__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean value of the power calculated on the physical sidelink shared channel (PSSCH) data symbols over the slots specified by the SetMeasurementLength(string, int) method. This value is expressed in dBm. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

### GetPsschMeanDataPower(string, out double)

Gets the mean value of the power calculated on the physical sidelink shared channel (PSSCH) data symbols over the slots specified by the [SetMeasurementLength(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxmodaccconfiguration-setmeasurementlength__string-int.html) method. This value is expressed in dBm. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetPsschMeanDataPower(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsPsschMeanDataPower](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the mean value of the power calculated on the physical sidelink shared channel (PSSCH) data symbols over the slots specified by the SetMeasurementLength(string, int) method. This value is expressed in dBm. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getpuschmaximumpeakdataevm__string-out.html language=enus -->
## TOPIC 00173: GetPuschMaximumPeakDataEvm(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getpuschmaximumpeakdataevm__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getpuschmaximumpeakdataevm__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum value of the peak EVMs calculated on the physical uplink shared channel (PUSCH) data symbols over the slots specified by the SetMeasurementLength(string, int) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. SyntaxNamespace: NationalIn

### GetPuschMaximumPeakDataEvm(string, out double)

Gets the maximum value of the peak EVMs calculated on the physical uplink shared channel (PUSCH) data symbols over the slots specified by the [SetMeasurementLength(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxmodaccconfiguration-setmeasurementlength__string-int.html) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetPuschMaximumPeakDataEvm(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsPuschMaximumPeakDataEvm](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the maximum value of the peak EVMs calculated on the physical uplink shared channel (PUSCH) data symbols over the slots specified by the SetMeasurementLength(string, int) method. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getspectralflatnessrange1maximumtorange1minimum__string-out.html language=enus -->
## TOPIC 00174: GetSpectralFlatnessRange1MaximumToRange1Minimum(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getspectralflatnessrange1maximumtorange1minimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getspectralflatnessrange1maximumtorange1minimum__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak-to-peak ripple of the EVM equalizer coefficients within the frequency Range1. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetSpectralFlatnessRange1MaximumToRange1Minimum(string selectorString, out double value)RemarksThis method gets the val

### GetSpectralFlatnessRange1MaximumToRange1Minimum(string, out double)

Gets the peak-to-peak ripple of the EVM equalizer coefficients within the frequency *Range1*. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetSpectralFlatnessRange1MaximumToRange1Minimum(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsSpectralFlatnessRange1MaximumToRange1Minimum](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak-to-peak ripple of the EVM equalizer coefficients within the frequency Range1. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getspectralflatnessrange1maximumtorange2minimum__string-out.html language=enus -->
## TOPIC 00175: GetSpectralFlatnessRange1MaximumToRange2Minimum(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getspectralflatnessrange1maximumtorange2minimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getspectralflatnessrange1maximumtorange2minimum__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak-to-peak ripple of the EVM equalizer coefficients from the frequency Range1 to the frequency Measurement Offset parameter. The frequency Range1 and frequency Measurement Offset parameter are defined in the section 6.5.2.4.5 of the 3GPP TS 36.521 specification. This value is expressed in

### GetSpectralFlatnessRange1MaximumToRange2Minimum(string, out double)

Gets the peak-to-peak ripple of the EVM equalizer coefficients from the frequency *Range1* to the frequency *Measurement Offset* parameter. The frequency *Range1* and frequency *Measurement Offset* parameter are defined in the section 6.5.2.4.5 of the *3GPP TS 36.521* specification. This value is expressed in dB. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetSpectralFlatnessRange1MaximumToRange2Minimum(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsSpectralFlatnessRange1MaximumToRange2Minimum](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak-to-peak ripple of the EVM equalizer coefficients from the frequency Range1 to the frequency Measurement Offset parameter. The frequency Range1 and frequency Measurement Offset parameter are defined in the section 6.5.2.4.5 of the 3GPP TS 36.521 specification. This value is expressed in dB. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getspectralflatnessrange2maximumtorange1minimum__string-out.html language=enus -->
## TOPIC 00176: GetSpectralFlatnessRange2MaximumToRange1Minimum(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getspectralflatnessrange2maximumtorange1minimum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getspectralflatnessrange2maximumtorange1minimum__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak-to-peak ripple of the EVM equalizer coefficients from frequency Measurement Offset parameter to frequency Range1. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetSpectralFlatnessRange2MaximumToRange1Minimum(string selectorString, out double v

### GetSpectralFlatnessRange2MaximumToRange1Minimum(string, out double)

Gets the peak-to-peak ripple of the EVM equalizer coefficients from frequency *Measurement Offset* parameter to frequency *Range1*. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetSpectralFlatnessRange2MaximumToRange1Minimum(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsSpectralFlatnessRange2MaximumToRange1Minimum](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak-to-peak ripple of the EVM equalizer coefficients from frequency Measurement Offset parameter to frequency Range1. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getsubblockmeaniqoriginoffset__string-out.html language=enus -->
## TOPIC 00177: GetSubblockMeanIQOriginOffset(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getsubblockmeaniqoriginoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getsubblockmeaniqoriginoffset__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the estimated I/Q origin offset averaged over the slots specified by the SetMeasurementLength(string, int) method in the subblock. This value is expressed in dBc. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetSubblockMeanIQOriginOffset(string selectorString, out double value)Rema

### GetSubblockMeanIQOriginOffset(string, out double)

Gets the estimated I/Q origin offset averaged over the slots specified by the [SetMeasurementLength(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxmodaccconfiguration-setmeasurementlength__string-int.html) method in the subblock. This value is expressed in dBc.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetSubblockMeanIQOriginOffset(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsSubblockMeanIQOriginOffset](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Subblock number. Example: "Subblock0", "result::r1/Subblock0". You can use the BuildSubblockString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the estimated I/Q origin offset averaged over the slots specified by the SetMeasurementLength(string, int) method in the subblock. This value is expressed in dBc. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getsubblockmeanquadratureerror__string-out.html language=enus -->
## TOPIC 00178: GetSubblockMeanQuadratureError(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getsubblockmeanquadratureerror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccresults-getsubblockmeanquadratureerror__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the estimated quadrature error averaged over the slots specified by the SetMeasurementLength(string, int) method. This value is expressed in degrees. Quadrature error is a measure of the skewness of the I component with respect to the Q component of the I/Q signal being measured in the subblock

### GetSubblockMeanQuadratureError(string, out double)

Gets the estimated quadrature error averaged over the slots specified by the [SetMeasurementLength(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxmodaccconfiguration-setmeasurementlength__string-int.html) method. This value is expressed in degrees. Quadrature error is a measure of the skewness of the I component with respect to the Q component of the I/Q signal being measured in the subblock.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetSubblockMeanQuadratureError(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsSubblockMeanQuadratureError](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Subblock number. Example: "Subblock0", "result::r1/Subblock0". You can use the BuildSubblockString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the estimated quadrature error averaged over the slots specified by the SetMeasurementLength(string, int) method. This value is expressed in degrees. Quadrature error is a measure of the skewness of the I component with respect to the Q component of the I/Q signal being measured in the subblock. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXModAccResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxmodaccsynchronizationmode.html language=enus -->
## TOPIC 00179: RFmxLteMXModAccSynchronizationMode Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxmodaccsynchronizationmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxmodaccsynchronizationmode.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed from the frame or the slot boundary. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXModAccSynchronizationModeMembersNameValueDescriptionFrame0The frame boundary is detected, and the measurement is performed over the SetMeasurementLe

### RFmxLteMXModAccSynchronizationMode Enumeration

Specifies whether the measurement is performed from the frame or the slot boundary.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXModAccSynchronizationMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Frame | 0 | The frame boundary is detected, and the measurement is performed over the SetMeasurementLength(string, int) method, starting at the SetMeasurementOffset(string, int) method from the frame boundary. When you set the SetTriggerType(string, RFmxLteMXTriggerType) method to DigitalEdge, the measurement expects a trigger at the frame boundary. |
| Slot | 1 | The slot boundary is detected, and the measurement is performed over the ModAcc Meas Length method starting at the ModAcc Meas Offset method from the slot boundary. When you set the Trigger Type method to DigitalEdge, the measurement expects a trigger at any slot boundary. |
| Marker | 2 | The measurement expects a marker (trigger) at the frame boundary from the user. The measurement takes advantage of triggered acquisitions to reduce processing resulting in faster measurement time. Measurement is performed over the ModAcc Meas Length method starting at ModAcc Meas Offset method from the frame boundary. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxnpuschdmrsgrouphoppingenabled.html language=enus -->
## TOPIC 00180: RFmxLteMXNPuschDmrsGroupHoppingEnabled Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxnpuschdmrsgrouphoppingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxnpuschdmrsgrouphoppingenabled.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the group hopping is enabled for narrowband physical uplink shared channel (NPUSCH) DMRS. This method is valid only when the SetNPuschFormat(string, int) is 1. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXNPuschDmrsGroupHoppingEnabledMembersNameValueDescripti

### RFmxLteMXNPuschDmrsGroupHoppingEnabled Enumeration

Specifies whether the group hopping is enabled for narrowband physical uplink shared channel (NPUSCH) DMRS. This method is valid only when the [SetNPuschFormat(string, int)](nationalinstruments-rfmx-ltemx-rfmxltemxcomponentcarrier-setnpuschformat__string-int.html) is 1.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXNPuschDmrsGroupHoppingEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Group hopping is disabled. |
| True | 1 | Group hopping is enabled. The sequence group number is calculated as defined in section 10.1.4.1.3 of the 3GPP TS 36.211 specification. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxnpuschmodulationtype.html language=enus -->
## TOPIC 00181: RFmxLteMXNPuschModulationType Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxnpuschmodulationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxnpuschmodulationtype.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the modulation type that is used by the narrowband physical uplink shared channel (NPUSCH). SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXNPuschModulationTypeMembersNameValueDescriptionBpsk0Specifies a BPSK modulation scheme. Qpsk1Specifies a QPSK modulation scheme.

### RFmxLteMXNPuschModulationType Enumeration

Specifies the modulation type that is used by the narrowband physical uplink shared channel (NPUSCH).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXNPuschModulationType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Bpsk | 0 | Specifies a BPSK modulation scheme. |
| Qpsk | 1 | Specifies a QPSK modulation scheme. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxobw-configuration.html language=enus -->
## TOPIC 00182: Configuration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxobw-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxobw-configuration.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxLteMXObwConfiguration instance that provides methods to configure the OBW measurement. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic RFmxLteMXObwConfiguration Configuration { get; }

### Configuration

Gets the [RFmxLteMXObwConfiguration](nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration.html) instance that provides methods to configure the OBW measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public [RFmxLteMXObwConfiguration](nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration.html) Configuration { get; }

Parent topic:

RFmxLteMXObw Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxobwaveragingtype.html language=enus -->
## TOPIC 00183: RFmxLteMXObwAveragingType Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxobwaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxobwaveragingtype.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXObwAveragingTypeMembersNameValueDescriptionRms0The power spectrum is linearly averaged. RMS averaging

### RFmxLteMXObwAveragingType Enumeration

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXObwAveragingType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rms | 0 | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log | 1 | The power spectrum is averaged in a logarithmic scale. |
| Scalar | 2 | The square root of the power spectrum is averaged. |
| Maximum | 3 | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Minimum | 4 | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-configurerbwfilter__string-rfmxltemxobwrbwautobandwidth-double-rfmxltemxobwrbwfiltertype.html language=enus -->
## TOPIC 00184: ConfigureRbwFilter(string, RFmxLteMXObwRbwAutoBandwidth, double, RFmxLteMXObwRbwFilterType)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-configurerbwfilter__string-rfmxltemxobwrbwautobandwidth-double-rfmxltemxobwrbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-configurerbwfilter__string-rfmxltemxobwrbwautobandwidth-double-rfmxltemxobwrbwfiltertype.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RBW filter.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ConfigureRbwFilter(string selectorString, RFmxLteMXObwRbwAutoBandwidth rbwAuto, double rbw, RFmxLteMXObwRbwFilterType rbwFilterType)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal na

### ConfigureRbwFilter(string, RFmxLteMXObwRbwAutoBandwidth, double, RFmxLteMXObwRbwFilterType)

Configures the RBW filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureRbwFilter(string selectorString, RFmxLteMXObwRbwAutoBandwidth rbwAuto, double rbw, RFmxLteMXObwRbwFilterType rbwFilterType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| rbwAuto | RFmxLteMXObwRbwAutoBandwidth | Specifies whether the measurement computes the RBW. |
| rbw | double | Specifies the bandwidth of the resolution bandwidth (RBW) filter, used to sweep the acquired signal, when you set the rbwAuto parameter to False. This value is expressed in Hz. |
| rbwFilterType | RFmxLteMXObwRbwFilterType | Specifies the shape of the digital RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-configuresweeptime__string-rfmxltemxobwsweeptimeauto-double.html language=enus -->
## TOPIC 00185: ConfigureSweepTime(string, RFmxLteMXObwSweepTimeAuto, double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-configuresweeptime__string-rfmxltemxobwsweeptimeauto-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-configuresweeptime__string-rfmxltemxobwsweeptimeauto-double.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ConfigureSweepTime(string selectorString, RFmxLteMXObwSweepTimeAuto sweepTimeAuto, double sweepTimeInterval)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when

### ConfigureSweepTime(string, RFmxLteMXObwSweepTimeAuto, double)

Configures the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureSweepTime(string selectorString, RFmxLteMXObwSweepTimeAuto sweepTimeAuto, double sweepTimeInterval)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| sweepTimeAuto | RFmxLteMXObwSweepTimeAuto | Specifies whether the measurement computes the sweep time. |
| sweepTimeInterval | double | Specifies the sweep time when you set the sweepTimeAuto parameter to False. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00186: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the traces to be stored and retrieved after performing the OBW measurement. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method gets the value of ObwAllTracesEnabled attribute. The default value

### GetAllTracesEnabled(string, out bool)

Gets whether to enable the traces to be stored and retrieved after performing the OBW measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [ObwAllTracesEnabled](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the traces to be stored and retrieved after performing the OBW measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-getaveragingtype__string-out.html language=enus -->
## TOPIC 00187: GetAveragingType(string, out RFmxLteMXObwAveragingType)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-getaveragingtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-getaveragingtype__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetAveragingType(string selectorString, out RFmxLteMXObwAveragingType value)RemarksThis method gets the value of ObwA

### GetAveragingType(string, out RFmxLteMXObwAveragingType)

Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetAveragingType(string selectorString, out RFmxLteMXObwAveragingType value)

#### Remarks

This method gets the value of [ObwAveragingType](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [Rms](nationalinstruments-rfmx-ltemx-rfmxltemxobwaveragingtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxLteMXObwAveragingType | Upon return, contains the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-getrbwfilterautobandwidth__string-out.html language=enus -->
## TOPIC 00188: GetRbwFilterAutoBandwidth(string, out RFmxLteMXObwRbwAutoBandwidth)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-getrbwfilterautobandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-getrbwfilterautobandwidth__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement computes the RBW. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetRbwFilterAutoBandwidth(string selectorString, out RFmxLteMXObwRbwAutoBandwidth value)RemarksThis method gets the value of ObwRbwFilterAutoBandwidth attribute. The default value is True.Paramet

### GetRbwFilterAutoBandwidth(string, out RFmxLteMXObwRbwAutoBandwidth)

Gets whether the measurement computes the RBW.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetRbwFilterAutoBandwidth(string selectorString, out RFmxLteMXObwRbwAutoBandwidth value)

#### Remarks

This method gets the value of [ObwRbwFilterAutoBandwidth](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [True](nationalinstruments-rfmx-ltemx-rfmxltemxobwrbwautobandwidth.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxLteMXObwRbwAutoBandwidth | Upon return, contains whether the measurement computes the RBW. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-getrbwfilterbandwidth__string-out.html language=enus -->
## TOPIC 00189: GetRbwFilterBandwidth(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-getrbwfilterbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-getrbwfilterbandwidth__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the bandwidth of the RBW filter used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(string, RFmxLteMXObwRbwAutoBandwidth) method to False. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetRbwFilterBandwidth(string selectorStri

### GetRbwFilterBandwidth(string, out double)

Gets the bandwidth of the RBW filter used to sweep the acquired signal, when you set the [SetRbwFilterAutoBandwidth(string, RFmxLteMXObwRbwAutoBandwidth)](nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-setrbwfilterautobandwidth__string-rfmxltemxobwrbwautobandwidth.html) method to [False](nationalinstruments-rfmx-ltemx-rfmxltemxobwrbwautobandwidth.html). This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetRbwFilterBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [ObwRbwFilterBandwidth](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 10000.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the bandwidth of the RBW filter used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(string, RFmxLteMXObwRbwAutoBandwidth) method to False. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-setaveragingcount__string-int.html language=enus -->
## TOPIC 00190: SetAveragingCount(string, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-setaveragingcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-setaveragingcount__string-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxLteMXObwAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetAveragingCount(string selectorString, int value)RemarksThis method sets the value of ObwAveraging

### SetAveragingCount(string, int)

Sets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxLteMXObwAveragingEnabled)](nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-setaveragingenabled__string-rfmxltemxobwaveragingenabled.html) method to [True](nationalinstruments-rfmx-ltemx-rfmxltemxobwaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetAveragingCount(string selectorString, int value)

#### Remarks

This method sets the value of [ObwAveragingCount](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxLteMXObwAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-setaveragingtype__string-rfmxltemxobwaveragingtype.html language=enus -->
## TOPIC 00191: SetAveragingType(string, RFmxLteMXObwAveragingType)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-setaveragingtype__string-rfmxltemxobwaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-setaveragingtype__string-rfmxltemxobwaveragingtype.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetAveragingType(string selectorString, RFmxLteMXObwAveragingType value)RemarksThis method sets the value of ObwAvera

### SetAveragingType(string, RFmxLteMXObwAveragingType)

Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetAveragingType(string selectorString, RFmxLteMXObwAveragingType value)

#### Remarks

This method sets the value of [ObwAveragingType](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [Rms](nationalinstruments-rfmx-ltemx-rfmxltemxobwaveragingtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxLteMXObwAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-setrbwfiltertype__string-rfmxltemxobwrbwfiltertype.html language=enus -->
## TOPIC 00192: SetRbwFilterType(string, RFmxLteMXObwRbwFilterType)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-setrbwfiltertype__string-rfmxltemxobwrbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxobwconfiguration-setrbwfiltertype__string-rfmxltemxobwrbwfiltertype.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the shape of the digital RBW filter. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetRbwFilterType(string selectorString, RFmxLteMXObwRbwFilterType value)RemarksThis method sets the value of ObwRbwFilterType attribute. The default value is Gaussian.ParametersNameTypeDescriptionsele

### SetRbwFilterType(string, RFmxLteMXObwRbwFilterType)

Sets the shape of the digital RBW filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetRbwFilterType(string selectorString, RFmxLteMXObwRbwFilterType value)

#### Remarks

This method sets the value of [ObwRbwFilterType](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [Gaussian](nationalinstruments-rfmx-ltemx-rfmxltemxobwrbwfiltertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxLteMXObwRbwFilterType | Specifies the shape of the digital RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxobwrbwautobandwidth.html language=enus -->
## TOPIC 00193: RFmxLteMXObwRbwAutoBandwidth Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxobwrbwautobandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxobwrbwautobandwidth.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the RBW. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXObwRbwAutoBandwidthMembersNameValueDescriptionFalse0The measurement uses the RBW that you specify in the SetRbwFilterBandwidth(string, double) method. True1The measurement computes

### RFmxLteMXObwRbwAutoBandwidth Enumeration

Specifies whether the measurement computes the RBW.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXObwRbwAutoBandwidth

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement uses the RBW that you specify in the SetRbwFilterBandwidth(string, double) method. |
| True | 1 | The measurement computes the RBW. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxobwrbwfiltertype.html language=enus -->
## TOPIC 00194: RFmxLteMXObwRbwFilterType Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxobwrbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxobwrbwfiltertype.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of the digital RBW filter. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXObwRbwFilterTypeMembersNameValueDescriptionFftBased0No RBW filtering is performed. Gaussian1An RBW filter with a Gaussian response is applied. Flat2An RBW filter with a flat response is

### RFmxLteMXObwRbwFilterType Enumeration

Specifies the shape of the digital RBW filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXObwRbwFilterType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| FftBased | 0 | No RBW filtering is performed. |
| Gaussian | 1 | An RBW filter with a Gaussian response is applied. |
| Flat | 2 | An RBW filter with a flat response is applied. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxobwresults-fetchmeasurement__string-double-out-out-out-out.html language=enus -->
## TOPIC 00195: FetchMeasurement(string, double, out double, out double, out double, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxobwresults-fetchmeasurement__string-double-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxobwresults-fetchmeasurement__string-double-out-out-out-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the occupied bandwidth, absolute power, start frequency, and stop frequency of a component carrier or subblock. Use "subblock(n)" as the selector string to read results from this method. Refer to the LTE Occupied Bandwidth topic for more information about OBW measurements.SyntaxNamespace: Na

### FetchMeasurement(string, double, out double, out double, out double, out double)

Returns the occupied bandwidth, absolute power, start frequency, and stop frequency of a component carrier or subblock. 
 Use "subblock(n)" as the selector string to read results from this method. 
 Refer to the [LTE Occupied Bandwidth](/csh?context=rfmxlte_rfmxlte_lte_occupied_bandwidth_obw) topic for more information about OBW measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchMeasurement(string selectorString, double timeout, out double occupiedBandwidth, out double absolutePower, out double startFrequency, out double stopFrequency)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| occupiedBandwidth | out double | Upon return, contains the bandwidth that occupies 99 percentage of the total power of the signal within a carrier/subblock. |
| absolutePower | out double | Upon return, contains the power measured over the integration bandwidth of the carrier/subblock. |
| startFrequency | out double | Upon return, contains the start frequency of the subblock. The occupied bandwidth of a carrier/subblock is calculated using the following equation: Stop frequency - Start frequency = Occupied bandwidth. |
| stopFrequency | out double | Upon return, contains the stop frequency of the subblock. The occupied bandwidth of a carrier/subblock is calculated using the following equation: Stop frequency - Start frequency = Occupied bandwidth. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXObwResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxobwresults-getabsolutepower__string-out.html language=enus -->
## TOPIC 00196: GetAbsolutePower(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxobwresults-getabsolutepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxobwresults-getabsolutepower__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the total power measured in the carrier/subblock. This value is expressed in dBm. Use "subblock(n)" as the selector string to read this result. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetAbsolutePower(string selectorString, out double value)RemarksThis method gets the value of

### GetAbsolutePower(string, out double)

Gets the total power measured in the carrier/subblock. This value is expressed in dBm. Use "subblock(n)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetAbsolutePower(string selectorString, out double value)

#### Remarks

This method gets the value of [ObwResultsAbsolutePower](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Subblock number. Example: "Subblock0", "result::r1/Subblock0". You can use the BuildSubblockString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the total power measured in the carrier/subblock. This value is expressed in dBm. Use "subblock(n)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXObwResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxobwresults-getoccupiedbandwidth__string-out.html language=enus -->
## TOPIC 00197: GetOccupiedBandwidth(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxobwresults-getoccupiedbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxobwresults-getoccupiedbandwidth__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the bandwidth that occupies 99 percentage of the total power of the signal within a carrier/subblock. This value is expressed in Hz. Use "subblock(n)" as the selector string to read this result. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetOccupiedBandwidth(string selectorString

### GetOccupiedBandwidth(string, out double)

Gets the bandwidth that occupies 99 percentage of the total power of the signal within a carrier/subblock. This value is expressed in Hz. Use "subblock(n)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetOccupiedBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [ObwResultsOccupiedBandwidth](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Subblock number. Example: "Subblock0", "result::r1/Subblock0". You can use the BuildSubblockString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the bandwidth that occupies 99 percentage of the total power of the signal within a carrier/subblock. This value is expressed in Hz. Use "subblock(n)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXObwResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxobwresults-getstartfrequency__string-out.html language=enus -->
## TOPIC 00198: GetStartFrequency(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxobwresults-getstartfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxobwresults-getstartfrequency__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the start frequency of the carrier/subblock. This value is expressed in Hz. The occupied bandwidth is calculated using the following equation:Stop frequency - Start frequency = Occupied bandwidthUse "subblock(n)" as the selector string to read this result. SyntaxNamespace: NationalInstruments.R

### GetStartFrequency(string, out double)

Gets the start frequency of the carrier/subblock. This value is expressed in Hz. The occupied bandwidth is calculated using the following equation:*Stop frequency* - *Start frequency* = *Occupied bandwidth*Use "subblock(n)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetStartFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [ObwResultsStartFrequency](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Subblock number. Example: "Subblock0", "result::r1/Subblock0". You can use the BuildSubblockString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the start frequency of the carrier/subblock. This value is expressed in Hz. The occupied bandwidth is calculated using the following equation:Stop frequency - Start frequency = Occupied bandwidthUse "subblock(n)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXObwResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxobwresults-getstopfrequency__string-out.html language=enus -->
## TOPIC 00199: GetStopFrequency(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxobwresults-getstopfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxobwresults-getstopfrequency__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the stop frequency of the carrier/subblock. This value is expressed in Hz. Occupied bandwidth is calculated using the following equation:Occupied bandwidth = Stop frequency - Start frequencyUse "subblock(n)" as the selector string to read this result. SyntaxNamespace: NationalInstruments.RFmx.L

### GetStopFrequency(string, out double)

Gets the stop frequency of the carrier/subblock. This value is expressed in Hz. Occupied bandwidth is calculated using the following equation:*Occupied bandwidth* = *Stop frequency* - *Start frequency*Use "subblock(n)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetStopFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [ObwResultsStopFrequency](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Subblock number. Example: "Subblock0", "result::r1/Subblock0". You can use the BuildSubblockString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the stop frequency of the carrier/subblock. This value is expressed in Hz. Occupied bandwidth is calculated using the following equation:Occupied bandwidth = Stop frequency - Start frequencyUse "subblock(n)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXObwResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxobwresults.html language=enus -->
## TOPIC 00200: RFmxLteMXObwResults Class

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxobwresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxobwresults.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the OBW measurement results. Derives fromRFmxLteMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.LteMXpublic class RFmxLteMXObwResults : RFmxLteMXSubObjectMethodsNameDescriptionFetchMeasurement(string, double, out double, out double, out double, out double)Retu

### RFmxLteMXObwResults Class

Provides methods to fetch and read the OBW measurement results.

#### Derives from

- RFmxLteMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public class RFmxLteMXObwResults : RFmxLteMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchMeasurement(string, double, out double, out double, out double, out double) | Returns the occupied bandwidth, absolute power, start frequency, and stop frequency of a component carrier or subblock. Use "subblock(n)" as the selector string to read results from this method. Refer to the LTE Occupied Bandwidth topic for more information about OBW measurements. |
| FetchSpectrum(string, double, ref Spectrum< float >) | Fetches the spectrum used for OBW measurements. |
| GetAbsolutePower(string, out double) | Gets the total power measured in the carrier/subblock. This value is expressed in dBm. Use "subblock(n)" as the selector string to read this result. |
| GetOccupiedBandwidth(string, out double) | Gets the bandwidth that occupies 99 percentage of the total power of the signal within a carrier/subblock. This value is expressed in Hz. Use "subblock(n)" as the selector string to read this result. |
| GetStartFrequency(string, out double) | Gets the start frequency of the carrier/subblock. This value is expressed in Hz. The occupied bandwidth is calculated using the following equation:Stop frequency - Start frequency = Occupied bandwidthUse "subblock(n)" as the selector string to read this result. |
| GetStopFrequency(string, out double) | Gets the stop frequency of the carrier/subblock. This value is expressed in Hz. Occupied bandwidth is calculated using the following equation:Occupied bandwidth = Stop frequency - Start frequencyUse "subblock(n)" as the selector string to read this result. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxobwsweeptimeauto.html language=enus -->
## TOPIC 00201: RFmxLteMXObwSweepTimeAuto Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxobwsweeptimeauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxobwsweeptimeauto.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the sweep time. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXObwSweepTimeAutoMembersNameValueDescriptionFalse0The measurement uses the sweep time that you specify in the SetSweepTimeInterval(string, double) method. True1The measuremen

### RFmxLteMXObwSweepTimeAuto Enumeration

Specifies whether the measurement computes the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXObwSweepTimeAuto

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement uses the sweep time that you specify in the SetSweepTimeInterval(string, double) method. |
| True | 1 | The measurement uses a sweep time of 1 ms. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxpuschmodulationtype.html language=enus -->
## TOPIC 00202: RFmxLteMXPuschModulationType Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxpuschmodulationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxpuschmodulationtype.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the modulation scheme used in the physical uplink shared channel (PUSCH) of the signal being measured. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure or read this method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXPuschModulationTy

### RFmxLteMXPuschModulationType Enumeration

Specifies the modulation scheme used in the physical uplink shared channel (PUSCH) of the signal being measured. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure or read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXPuschModulationType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ModulationTypeQpsk | 0 | Specifies a QPSK modulation scheme. |
| ModulationType16Qam | 1 | Specifies a 16-QAM modulation scheme. |
| ModulationType64Qam | 2 | Specifies a 64-QAM modulation scheme. |
| ModulationType256Qam | 3 | Specifies a 256-QAM modulation scheme. |
| ModulationType1024Qam | 4 | Specifies a 1024-QAM modulation scheme. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxpvtconfiguration-configuremeasurementmethod__string-rfmxltemxpvtmeasurementmethod.html language=enus -->
## TOPIC 00203: ConfigureMeasurementMethod(string, RFmxLteMXPvtMeasurementMethod)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxpvtconfiguration-configuremeasurementmethod__string-rfmxltemxpvtmeasurementmethod.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxpvtconfiguration-configuremeasurementmethod__string-rfmxltemxpvtmeasurementmethod.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the method for performing the power versus time (PVT) measurement. Refer to the LTE PVT (Power Vs Time) Measurement topic for more information about measurement method.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ConfigureMeasurementMethod(string selectorString, RFmxLteMXPvtM

### ConfigureMeasurementMethod(string, RFmxLteMXPvtMeasurementMethod)

Configures the method for performing the power versus time (PVT) measurement. 
 Refer to the LTE PVT (Power Vs Time) Measurement topic for more information about measurement method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureMeasurementMethod(string selectorString, RFmxLteMXPvtMeasurementMethod measurementMethod)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| measurementMethod | RFmxLteMXPvtMeasurementMethod | Specifies the method for performing the PVT measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXPvtConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxpvtconfiguration-getmeasurementmethod__string-out.html language=enus -->
## TOPIC 00204: GetMeasurementMethod(string, out RFmxLteMXPvtMeasurementMethod)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxpvtconfiguration-getmeasurementmethod__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxpvtconfiguration-getmeasurementmethod__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the method for performing the power versus time (PVT) measurement. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetMeasurementMethod(string selectorString, out RFmxLteMXPvtMeasurementMethod value)RemarksThis method gets the value of PvtMeasurementMethod attribute. The default value

### GetMeasurementMethod(string, out RFmxLteMXPvtMeasurementMethod)

Gets the method for performing the power versus time (PVT) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetMeasurementMethod(string selectorString, out RFmxLteMXPvtMeasurementMethod value)

#### Remarks

This method gets the value of [PvtMeasurementMethod](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [Normal](nationalinstruments-rfmx-ltemx-rfmxltemxpvtmeasurementmethod.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxLteMXPvtMeasurementMethod | Upon return, contains the method for performing the power versus time (PVT) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXPvtConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxpvtconfiguration-getoffpowerexclusionbefore__string-out.html language=enus -->
## TOPIC 00205: GetOffPowerExclusionBefore(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxpvtconfiguration-getoffpowerexclusionbefore__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxpvtconfiguration-getoffpowerexclusionbefore__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the time excluded from the Off region before the burst. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetOffPowerExclusionBefore(string selectorString, out double value)RemarksThis method gets the value of PvtOffPowerExclusionBefore attribute. The

### GetOffPowerExclusionBefore(string, out double)

Gets the time excluded from the Off region before the burst. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetOffPowerExclusionBefore(string selectorString, out double value)

#### Remarks

This method gets the value of [PvtOffPowerExclusionBefore](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the time excluded from the Off region before the burst. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXPvtConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxpvtconfiguration-setaveragingcount__string-int.html language=enus -->
## TOPIC 00206: SetAveragingCount(string, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxpvtconfiguration-setaveragingcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxpvtconfiguration-setaveragingcount__string-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxLteMXPvtAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetAveragingCount(string selectorString, int value)RemarksThis method sets the value of PvtAveraging

### SetAveragingCount(string, int)

Sets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxLteMXPvtAveragingEnabled)](nationalinstruments-rfmx-ltemx-rfmxltemxpvtconfiguration-setaveragingenabled__string-rfmxltemxpvtaveragingenabled.html) method to [True](nationalinstruments-rfmx-ltemx-rfmxltemxpvtaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetAveragingCount(string selectorString, int value)

#### Remarks

This method sets the value of [PvtAveragingCount](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxLteMXPvtAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXPvtConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxpvtconfiguration-setaveragingenabled__string-rfmxltemxpvtaveragingenabled.html language=enus -->
## TOPIC 00207: SetAveragingEnabled(string, RFmxLteMXPvtAveragingEnabled)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxpvtconfiguration-setaveragingenabled__string-rfmxltemxpvtaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxpvtconfiguration-setaveragingenabled__string-rfmxltemxpvtaveragingenabled.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable averaging for the power versus time (PVT) measurement. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetAveragingEnabled(string selectorString, RFmxLteMXPvtAveragingEnabled value)RemarksThis method sets the value of PvtAveragingEnabled attribute. The default value

### SetAveragingEnabled(string, RFmxLteMXPvtAveragingEnabled)

Sets whether to enable averaging for the power versus time (PVT) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetAveragingEnabled(string selectorString, RFmxLteMXPvtAveragingEnabled value)

#### Remarks

This method sets the value of [PvtAveragingEnabled](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [False](nationalinstruments-rfmx-ltemx-rfmxltemxpvtaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxLteMXPvtAveragingEnabled | Specifies whether to enable averaging for the power versus time (PVT) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXPvtConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxpvtconfiguration-setaveragingtype__string-rfmxltemxpvtaveragingtype.html language=enus -->
## TOPIC 00208: SetAveragingType(string, RFmxLteMXPvtAveragingType)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxpvtconfiguration-setaveragingtype__string-rfmxltemxpvtaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxpvtconfiguration-setaveragingtype__string-rfmxltemxpvtaveragingtype.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the power versus time (PVT) measurement. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetAveragingType(string selectorString, RFmxLteMXPvtAveragingType value)RemarksThis method sets t

### SetAveragingType(string, RFmxLteMXPvtAveragingType)

Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the power versus time (PVT) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetAveragingType(string selectorString, RFmxLteMXPvtAveragingType value)

#### Remarks

This method sets the value of [PvtAveragingType](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [Rms](nationalinstruments-rfmx-ltemx-rfmxltemxpvtaveragingtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxLteMXPvtAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the power versus time (PVT) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXPvtConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxpvtconfiguration-setmeasurementmethod__string-rfmxltemxpvtmeasurementmethod.html language=enus -->
## TOPIC 00209: SetMeasurementMethod(string, RFmxLteMXPvtMeasurementMethod)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxpvtconfiguration-setmeasurementmethod__string-rfmxltemxpvtmeasurementmethod.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxpvtconfiguration-setmeasurementmethod__string-rfmxltemxpvtmeasurementmethod.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the method for performing the power versus time (PVT) measurement. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetMeasurementMethod(string selectorString, RFmxLteMXPvtMeasurementMethod value)RemarksThis method sets the value of PvtMeasurementMethod attribute. The default value is

### SetMeasurementMethod(string, RFmxLteMXPvtMeasurementMethod)

Sets the method for performing the power versus time (PVT) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetMeasurementMethod(string selectorString, RFmxLteMXPvtMeasurementMethod value)

#### Remarks

This method sets the value of [PvtMeasurementMethod](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [Normal](nationalinstruments-rfmx-ltemx-rfmxltemxpvtmeasurementmethod.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxLteMXPvtMeasurementMethod | Specifies the method for performing the power versus time (PVT) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXPvtConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemcomponentcarrierconfiguration-configuremaximumoutputpower__string-double.html language=enus -->
## TOPIC 00210: ConfigureMaximumOutputPower(string, double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemcomponentcarrierconfiguration-configuremaximumoutputpower__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemcomponentcarrierconfiguration-configuremaximumoutputpower__string-double.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the maximum output power of the component carrier. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. This method is considered only when you set the Link Direction method to Downlink, eNodeB Category method to Medium Range Base Station, and SEM

### ConfigureMaximumOutputPower(string, double)

Configures the maximum output power of the component carrier. 
 Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to configure this method. 
 This method is considered only when you set the Link Direction method to Downlink, eNodeB Category method to Medium Range Base Station, and SEM DL Mask Type method to eNodeB Category Based.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureMaximumOutputPower(string selectorString, double componentCarrierMaximumOutputPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the signal name, subblock number and carrier number. Example:"subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| componentCarrierMaximumOutputPower | double | Specifies the maximum output power per carrier, which is used only to choose the limit table for Medium Range Base Station. This value is expressed in dBm. Refer to the section 6.6.3 of the 3GPP 36.141 specification for more details. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemComponentCarrierConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemcomponentcarrierconfiguration-getintegrationbandwidth__string-out.html language=enus -->
## TOPIC 00211: GetIntegrationBandwidth(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemcomponentcarrierconfiguration-getintegrationbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemcomponentcarrierconfiguration-getintegrationbandwidth__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the integration bandwidth of a component carrier. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetIntegrationBandwidth(string selectorString, out double value)RemarksThis method gets the value of GetIntegrationBandwidth(string, out double) attribute.

### GetIntegrationBandwidth(string, out double)

Gets the integration bandwidth of a component carrier. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetIntegrationBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of GetIntegrationBandwidth(string, out double) attribute. The default value is 9 MHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the integration bandwidth of a component carrier. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemComponentCarrierConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemcomponentcarrierconfiguration-getmaximumoutputpower__string-out.html language=enus -->
## TOPIC 00212: GetMaximumOutputPower(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemcomponentcarrierconfiguration-getmaximumoutputpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemcomponentcarrierconfiguration-getmaximumoutputpower__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum output power, Pmax,c, per carrier that is used only to choose the limit table for Medium Range Base Station. For more details please refer to the section 6.6.3 of 3GPP 36.141 specification. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetMaximumOutputPower(string select

### GetMaximumOutputPower(string, out double)

Gets the maximum output power, Pmax,c, per carrier that is used only to choose the limit table for Medium Range Base Station. For more details please refer to the section 6.6.3 of *3GPP 36.141* specification.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetMaximumOutputPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SetMaximumOutputPower(string, double)](nationalinstruments-rfmx-ltemx-rfmxltemxsemcomponentcarrierconfiguration-setmaximumoutputpower__string-double.html) attribute. The default value is 0. Valid values are within 38, inclusive. This property is considered only when you set the Link Direction property to Downlink, eNodeB Category property to Medium Range Base Station, and SEM DL Mask Type property to eNodeB Category Based.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the maximum output power, Pmax,c, per carrier that is used only to choose the limit table for Medium Range Base Station. For more details please refer to the section 6.6.3 of 3GPP 36.141 specification. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemComponentCarrierConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemcomponentcarrierresults-getabsolutepeakpower__string-out.html language=enus -->
## TOPIC 00213: GetAbsolutePeakPower(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemcomponentcarrierresults-getabsolutepeakpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemcomponentcarrierresults-getabsolutepeakpower__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power in the component carrier. This value is expressed in dBm. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetAbsolutePeakPower(string selectorString, out double value)RemarksThis me

### GetAbsolutePeakPower(string, out double)

Gets the peak power in the component carrier. This value is expressed in dBm. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetAbsolutePeakPower(string selectorString, out double value)

#### Remarks

This method gets the value of GetAbsolutePeakPower(string, out double) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak power in the component carrier. This value is expressed in dBm. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemComponentCarrierResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemcomponentcarrierresults-getpeakfrequency__string-out.html language=enus -->
## TOPIC 00214: GetPeakFrequency(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemcomponentcarrierresults-getpeakfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemcomponentcarrierresults-getpeakfrequency__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency at which the peak power occurs in the component carrier. This value is expressed in Hz. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetPeakFrequency(string selectorString, out do

### GetPeakFrequency(string, out double)

Gets the frequency at which the peak power occurs in the component carrier. This value is expressed in Hz. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetPeakFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of GetPeakFrequency(string, out double) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the frequency at which the peak power occurs in the component carrier. This value is expressed in Hz. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemComponentCarrierResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemcomponentcarrierresults-getrelativeintegratedpower__string-out.html language=enus -->
## TOPIC 00215: GetRelativeIntegratedPower(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemcomponentcarrierresults-getrelativeintegratedpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemcomponentcarrierresults-getrelativeintegratedpower__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the sum of powers of all the frequency bins over the integration bandwidth of the component carrier power relative to its subblock power. This value is expressed in dB. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. SyntaxNamespace: NationalInstruments.

### GetRelativeIntegratedPower(string, out double)

Gets the sum of powers of all the frequency bins over the integration bandwidth of the component carrier power relative to its subblock power. This value is expressed in dB. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetRelativeIntegratedPower(string selectorString, out double value)

#### Remarks

This method gets the value of GetRelativeIntegratedPower(string, out double) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the sum of powers of all the frequency bins over the integration bandwidth of the component carrier power relative to its subblock power. This value is expressed in dB. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemComponentCarrierResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-configuredownlinkmask__string-rfmxltemxsemdownlinkmasktype-double-double.html language=enus -->
## TOPIC 00216: ConfigureDownlinkMask(string, RFmxLteMXSemDownlinkMaskType, double, double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-configuredownlinkmask__string-rfmxltemxsemdownlinkmasktype-double-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-configuredownlinkmask__string-rfmxltemxsemdownlinkmasktype-double-double.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the downlinkMaskType, deltaF_max, and aggregatedMaximumOutputPower parameters for the SEM measurement in LTE downlink.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ConfigureDownlinkMask(string selectorString, RFmxLteMXSemDownlinkMaskType downlinkMaskType, double deltaFMaximum,

### ConfigureDownlinkMask(string, RFmxLteMXSemDownlinkMaskType, double, double)

Configures the *downlinkMaskType*, *deltaF_max*, and *aggregatedMaximumOutputPower* parameters for the SEM measurement in LTE downlink.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureDownlinkMask(string selectorString, RFmxLteMXSemDownlinkMaskType downlinkMaskType, double deltaFMaximum, double aggregatedMaximumPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| downlinkMaskType | RFmxLteMXSemDownlinkMaskType | Specifies the standard-defined spectrum emission mask used in the measurement for the downlink. You must set the mask type to CUSTOM to configure the custom offsets and the masks. Refer to section 6.6.3 of the 3GPP 36.141 specification for more information about standard-defined mask types. |
| deltaFMaximum | double | Specifies the stop frequency for the last offset segment to be used in the measurement. This value is expressed in Hz. |
| aggregatedMaximumPower | double | Specifies the aggregated maximum output power of all the transmit antenna connectors. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-configureoffsetlimitfailmaskarray__string-rfmxltemxsemoffsetlimitfailmask_arr1.html language=enus -->
## TOPIC 00217: ConfigureOffsetLimitFailMaskArray(string, RFmxLteMXSemOffsetLimitFailMask[])

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-configureoffsetlimitfailmaskarray__string-rfmxltemxsemoffsetlimitfailmask_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-configureoffsetlimitfailmaskarray__string-rfmxltemxsemoffsetlimitfailmask_arr1.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the array of limit fail mask of the offset segments that specifies the criteria to determine the measurement fail status. Use "subblock(n)" as the selector string to read results from this method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ConfigureOffsetLimitFailMaskArray(

### ConfigureOffsetLimitFailMaskArray(string, RFmxLteMXSemOffsetLimitFailMask[])

Configures the array of limit fail mask of the offset segments that specifies the criteria to determine the measurement fail status. 
 Use "subblock(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureOffsetLimitFailMaskArray(string selectorString, RFmxLteMXSemOffsetLimitFailMask[] limitFailMask)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| limitFailMask | RFmxLteMXSemOffsetLimitFailMask[] | Specifies the array of criterion to determine the measurement fail status. When you set the Link Direction method to Downlink, all the values of limit fail mask are supported but when you set the Link Direction method to Uplink, the measurement internally sets the value of limit fail mask to Absolute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-configureoffsetrbwfilterarray__string-double_arr1-rfmxltemxsemoffsetrbwfiltertype_arr1.html language=enus -->
## TOPIC 00218: ConfigureOffsetRbwFilterArray(string, double[], RFmxLteMXSemOffsetRbwFilterType[])

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-configureoffsetrbwfilterarray__string-double_arr1-rfmxltemxsemoffsetrbwfiltertype_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-configureoffsetrbwfilterarray__string-double_arr1-rfmxltemxsemoffsetrbwfiltertype_arr1.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the offset RBW and the offset RBW filter type arrays. Use "subblock(n)" as the selector string to configure from this method.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ConfigureOffsetRbwFilterArray(string selectorString, double[] offsetRbw, RFmxLteMXSemOffsetRbwFilterType[]

### ConfigureOffsetRbwFilterArray(string, double[], RFmxLteMXSemOffsetRbwFilterType[])

Configures the offset RBW and the offset RBW filter type arrays. 
 Use "subblock(n)" as the selector string to configure from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureOffsetRbwFilterArray(string selectorString, double[] offsetRbw, RFmxLteMXSemOffsetRbwFilterType[] offsetRbwFilterType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| offsetRbw | double[] | Specifies the array of the RBW filter bandwidth values used to sweep the acquired offset segment, when you set the SEM Offset RBW Auto method to False. This value is expressed in Hz. |
| offsetRbwFilterType | RFmxLteMXSemOffsetRbwFilterType[] | Specifies the array of the shape of a digital RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-configureoffsetrelativelimit__string-double-double.html language=enus -->
## TOPIC 00219: ConfigureOffsetRelativeLimit(string, double, double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-configureoffsetrelativelimit__string-double-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-configureoffsetrelativelimit__string-double-double.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the start and stop relative limit of the offset segment. Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to read results from this method. This method is considered only when you set the Link Direction method to Downlink and SEM DL Mask Type method to Custom. SyntaxNames

### ConfigureOffsetRelativeLimit(string, double, double)

Configures the start and stop relative limit of the offset segment. 
 Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to read results from this method. 
 This method is considered only when you set the Link Direction method to Downlink and SEM DL Mask Type method to Custom.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureOffsetRelativeLimit(string selectorString, double relativeLimitStart, double relativeLimitStop)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the signal name, subblock number, and offset number. Example:"subblock0/offset0" You can use the BuildOffsetString(string, int) method to build the selector string. |
| relativeLimitStart | double | Specifies the relative power limit corresponding to the beginning of the offset segment. This value is expressed in dB. |
| relativeLimitStop | double | Specifies the relative power limit corresponding to the end of the offset segment. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-configuresweeptime__string-rfmxltemxsemsweeptimeauto-double.html language=enus -->
## TOPIC 00220: ConfigureSweepTime(string, RFmxLteMXSemSweepTimeAuto, double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-configuresweeptime__string-rfmxltemxsemsweeptimeauto-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-configuresweeptime__string-rfmxltemxsemsweeptimeauto-double.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ConfigureSweepTime(string selectorString, RFmxLteMXSemSweepTimeAuto sweepTimeAuto, double sweepTimeInterval)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when

### ConfigureSweepTime(string, RFmxLteMXSemSweepTimeAuto, double)

Configures the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureSweepTime(string selectorString, RFmxLteMXSemSweepTimeAuto sweepTimeAuto, double sweepTimeInterval)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| sweepTimeAuto | RFmxLteMXSemSweepTimeAuto | Specifies whether the measurement computes the sweep time. |
| sweepTimeInterval | double | Specifies the sweep time when you set the sweepTimeAuto parameter to False. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-configureuplinkmasktype__string-rfmxltemxsemuplinkmasktype.html language=enus -->
## TOPIC 00221: ConfigureUplinkMaskType(string, RFmxLteMXSemUplinkMaskType)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-configureuplinkmasktype__string-rfmxltemxsemuplinkmasktype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-configureuplinkmasktype__string-rfmxltemxsemuplinkmasktype.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the standard defined mask type that has to be used in the measurement for uplink. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int ConfigureUplinkMaskType(string selectorString, RFmxLteMXSemUplinkMaskType uplinkMaskType)ParametersNameTypeDescriptionselectorStringstringPass an emp

### ConfigureUplinkMaskType(string, RFmxLteMXSemUplinkMaskType)

Configures the standard defined mask type that has to be used in the measurement for uplink.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int ConfigureUplinkMaskType(string selectorString, RFmxLteMXSemUplinkMaskType uplinkMaskType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| uplinkMaskType | RFmxLteMXSemUplinkMaskType | Specifies the standard-defined spectrum emission mask used in the measurement for uplink. The following mask types are supported: general, NS_03orNS_11orNS_20orNS_21, NS_04, NS_06orNS_07, CA_NS_04, custom, generalCAClassB, CA_NC_NS_01, NS_27, and NS_35. Each mask type refers to a different Network Signalled (NS) value. CA_NS_04 and CA_NC_NS_01 refers to carrier aggregation case. You must set the mask type to CUSTOM to configure the custom offset masks. Refer to section 6.6.2.1 of the 3GPP 36.521 specification for more information about standard-defined mask types. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-getaggregatedmaximumpower__string-out.html language=enus -->
## TOPIC 00222: GetAggregatedMaximumPower(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-getaggregatedmaximumpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-getaggregatedmaximumpower__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the aggregated maximum output power of all transmit antenna connectors. This value is expressed in dBm. Refer to the Section 6.6.3 of 3GPP 36.141 specification for more details. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetAggregatedMaximumPower(string selectorString, out double

### GetAggregatedMaximumPower(string, out double)

Gets the aggregated maximum output power of all transmit antenna connectors. This value is expressed in dBm. Refer to the Section 6.6.3 of *3GPP 36.141* specification for more details.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetAggregatedMaximumPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemAggregatedMaximumPower](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 0. Valid values are within 20, inclusive. This property is considered only when you set the Link Direction property to Downlink, eNodeB Category property to Home Base Station, and SEM DL Mask Type property to eNodeB Category Based.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the aggregated maximum output power of all transmit antenna connectors. This value is expressed in dBm. Refer to the Section 6.6.3 of 3GPP 36.141 specification for more details. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00223: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the traces to be stored and retrieved after performing the SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method gets the value of SemAllTracesEnabled attribute. The default value

### GetAllTracesEnabled(string, out bool)

Gets whether to enable the traces to be stored and retrieved after performing the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [SemAllTracesEnabled](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the traces to be stored and retrieved after performing the SEM measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-getdeltafmaximum__string-out.html language=enus -->
## TOPIC 00224: GetDeltaFMaximum(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-getdeltafmaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-getdeltafmaximum__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the stop frequency for the last offset segment to be used in the measurement. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetDeltaFMaximum(string selectorString, out double value)RemarksThis method gets the value of SemDeltaFMaximum attribute. The de

### GetDeltaFMaximum(string, out double)

Gets the stop frequency for the last offset segment to be used in the measurement. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetDeltaFMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [SemDeltaFMaximum](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 15 MHz. The minimum value is 9.5 MHz. This property is considered for downlink only when you set the SEM DL Mask Type property to either eNodeB Category Based or Band 46.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the stop frequency for the last offset segment to be used in the measurement. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-getdownlinkmasktype__string-out.html language=enus -->
## TOPIC 00225: GetDownlinkMaskType(string, out RFmxLteMXSemDownlinkMaskType)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-getdownlinkmasktype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-getdownlinkmasktype__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the limits to be used in the measurement for downlink. Refer to section 6.6.3 of the 3GPP 36.141 specification for more information about standard-defined mask types. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetDownlinkMaskType(string selectorString, out RFmxLteMXSemDownlinkMas

### GetDownlinkMaskType(string, out RFmxLteMXSemDownlinkMaskType)

Gets the limits to be used in the measurement for downlink. Refer to section 6.6.3 of the *3GPP 36.141* specification for more information about standard-defined mask types.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetDownlinkMaskType(string selectorString, out RFmxLteMXSemDownlinkMaskType value)

#### Remarks

This method gets the value of [SemDownlinkMaskType](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is [ENodeBCategoryBased](nationalinstruments-rfmx-ltemx-rfmxltemxsemdownlinkmasktype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxLteMXSemDownlinkMaskType | Upon return, contains the limits to be used in the measurement for downlink. Refer to section 6.6.3 of the 3GPP 36.141 specification for more information about standard-defined mask types. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-getnumberofoffsets__string-out.html language=enus -->
## TOPIC 00226: GetNumberOfOffsets(string, out int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-getnumberofoffsets__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-getnumberofoffsets__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of SEM offset segments. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetNumberOfOffsets(string selectorString, out int value)RemarksThis method gets the value of SemNumberOfOffsets attribute. The default value is 1.ParametersNameTypeDescriptionselectorStringstringSpecifi

### GetNumberOfOffsets(string, out int)

Gets the number of SEM offset segments.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetNumberOfOffsets(string selectorString, out int value)

#### Remarks

This method gets the value of [SemNumberOfOffsets](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the number of SEM offset segments. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-getoffsetabsolutelimitstart__string-out.html language=enus -->
## TOPIC 00227: GetOffsetAbsoluteLimitStart(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-getoffsetabsolutelimitstart__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-getoffsetabsolutelimitstart__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the absolute power limit corresponding to the beginning of an offset segment. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int GetOffsetAbsoluteLimitStart(string selectorString, out double value)RemarksThis method gets the value of SemOffsetAbsoluteLimit

### GetOffsetAbsoluteLimitStart(string, out double)

Gets the absolute power limit corresponding to the beginning of an offset segment. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetOffsetAbsoluteLimitStart(string selectorString, out double value)

#### Remarks

This method gets the value of [SemOffsetAbsoluteLimitStart](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is -16.5.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number and subblock number. Example: "subblock0" or "subblock0/offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the absolute power limit corresponding to the beginning of an offset segment. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-getsidelinkmasktype__string-out.html language=enus -->
## TOPIC 00228: GetSidelinkMaskType(string, out RFmxLteMXSemSidelinkMaskType)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-getsidelinkmasktype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-getsidelinkmasktype__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the spectrum emission mask used in the measurement for sidelink. Each mask type refers to a different Network Signalled (NS) value. You must set the mask type to Custom to configure the custom offset masks. Refer to section 6.6.2 of the 3GPP 36.521 specification for more information about stand

### GetSidelinkMaskType(string, out RFmxLteMXSemSidelinkMaskType)

Gets the spectrum emission mask used in the measurement for sidelink. Each mask type refers to a different Network Signalled (NS) value. You must set the mask type to [Custom](nationalinstruments-rfmx-ltemx-rfmxltemxsemsidelinkmasktype.html) to configure the custom offset masks. Refer to section 6.6.2 of the *3GPP 36.521* specification for more information about standard-defined mask types.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetSidelinkMaskType(string selectorString, out RFmxLteMXSemSidelinkMaskType value)

#### Remarks

This method gets the value of [SemSidelinkMaskType](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is General (NS_01).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxLteMXSemSidelinkMaskType | Upon return, contains the spectrum emission mask used in the measurement for sidelink. Each mask type refers to a different Network Signalled (NS) value. You must set the mask type to Custom to configure the custom offset masks. Refer to section 6.6.2 of the 3GPP 36.521 specification for more information about standard-defined mask types. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-setnumberofoffsets__string-int.html language=enus -->
## TOPIC 00229: SetNumberOfOffsets(string, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-setnumberofoffsets__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-setnumberofoffsets__string-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of SEM offset segments. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetNumberOfOffsets(string selectorString, int value)RemarksThis method sets the value of SemNumberOfOffsets attribute. The default value is 1.ParametersNameTypeDescriptionselectorStringstringSpecifies t

### SetNumberOfOffsets(string, int)

Sets the number of SEM offset segments.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetNumberOfOffsets(string selectorString, int value)

#### Remarks

This method sets the value of [SemNumberOfOffsets](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(string, int) method to build the selector string. |
| value | int | Specifies the number of SEM offset segments. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-setoffsetabsolutelimitstop__string-double.html language=enus -->
## TOPIC 00230: SetOffsetAbsoluteLimitStop(string, double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-setoffsetabsolutelimitstop__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-setoffsetabsolutelimitstop__string-double.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the absolute power limit corresponding to the end of an offset segment. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetOffsetAbsoluteLimitStop(string selectorString, double value)RemarksThis method sets the value of SemOffsetAbsoluteLimitStop attrib

### SetOffsetAbsoluteLimitStop(string, double)

Sets the absolute power limit corresponding to the end of an offset segment. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetOffsetAbsoluteLimitStop(string selectorString, double value)

#### Remarks

This method sets the value of [SemOffsetAbsoluteLimitStop](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is -16.5.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number and subblock number. Example: "subblock0" or "subblock0/offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | double | Specifies the absolute power limit corresponding to the end of an offset segment. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-setoffsetbandwidthintegral__string-int.html language=enus -->
## TOPIC 00231: SetOffsetBandwidthIntegral(string, int)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-setoffsetbandwidthintegral__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-setoffsetbandwidthintegral__string-int.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the resolution of a spectrum to compare with the spectral mask limits as an integer multiple of the RBW. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetOffsetBandwidthIntegral(string selectorString, int value)RemarksThis method sets the value of SemOffsetBandwidthIntegral attribut

### SetOffsetBandwidthIntegral(string, int)

Sets the resolution of a spectrum to compare with the spectral mask limits as an integer multiple of the RBW.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetOffsetBandwidthIntegral(string selectorString, int value)

#### Remarks

This method sets the value of [SemOffsetBandwidthIntegral](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number and subblock number. Example: "subblock0" or "subblock0/offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | int | Specifies the resolution of a spectrum to compare with the spectral mask limits as an integer multiple of the RBW. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-setoffsetrelativelimitstart__string-double.html language=enus -->
## TOPIC 00232: SetOffsetRelativeLimitStart(string, double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-setoffsetrelativelimitstart__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration-setoffsetrelativelimitstart__string-double.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the relative power limit corresponding to the beginning of the offset segment. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int SetOffsetRelativeLimitStart(string selectorString, double value)RemarksThis method sets the value of SemOffsetRelativeLimitStar

### SetOffsetRelativeLimitStart(string, double)

Sets the relative power limit corresponding to the beginning of the offset segment. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int SetOffsetRelativeLimitStart(string selectorString, double value)

#### Remarks

This method sets the value of [SemOffsetRelativeLimitStart](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute. The default value is -51.5.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number and subblock number. Example: "subblock0" or "subblock0/offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | double | Specifies the relative power limit corresponding to the beginning of the offset segment. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration.html language=enus -->
## TOPIC 00233: RFmxLteMXSemConfiguration Class

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemconfiguration.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the SEM measurement. Derives fromRFmxLteMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.LteMXpublic class RFmxLteMXSemConfiguration : RFmxLteMXSubObjectPropertiesNameDescriptionComponentCarrierGets the RFmxLteMXSemComponentCarrierConfiguration instance. MethodsName

### RFmxLteMXSemConfiguration Class

Provides methods to configure the SEM measurement.

#### Derives from

- RFmxLteMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public class RFmxLteMXSemConfiguration : RFmxLteMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| ComponentCarrier | Gets the RFmxLteMXSemComponentCarrierConfiguration instance. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureAveraging(string, RFmxLteMXSemAveragingEnabled, int, RFmxLteMXSemAveragingType) | Configures averaging for the SEM measurement. |
| ConfigureDownlinkMask(string, RFmxLteMXSemDownlinkMaskType, double, double) | Configures the downlinkMaskType, deltaF_max, and aggregatedMaximumOutputPower parameters for the SEM measurement in LTE downlink. |
| ConfigureNumberOfOffsets(string, int) | Configures the number of offset segments for the SEM measurement. |
| ConfigureOffsetAbsoluteLimit(string, double, double) | Configures the start and the stop limit of an offset segment. Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to configure this method. |
| ConfigureOffsetAbsoluteLimitArray(string, double[], double[]) | Configures the array of the start limit and the stop limit of the offset segments. Use "subblock(n)" as the selector string to configure this method. |
| ConfigureOffsetBandwidthIntegral(string, int) | Configures the bandwidth integral of the offset segments. Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to configure this method. |
| ConfigureOffsetBandwidthIntegralArray(string, int[]) | Configures the array of the bandwidth integral of the offset segments. Use "subblock(n)" as the selector string to configure this method. |
| ConfigureOffsetFrequency(string, double, double, RFmxLteMXSemOffsetSideband) | Configures the start and stop frequencies and the sideband of an offset segment. Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to configure from this method. |
| ConfigureOffsetFrequencyArray(string, double[], double[], RFmxLteMXSemOffsetSideband[]) | Configures the arrays of the start and stop frequencies and the sideband of an offset segment. Use "subblock(n)" as the selector string to configure this method. |
| ConfigureOffsetLimitFailMask(string, RFmxLteMXSemOffsetLimitFailMask) | Configures the limit fail mask of the offset segments that specify the criteria to determine the measurement fail status. Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to configure this method. |
| ConfigureOffsetLimitFailMaskArray(string, RFmxLteMXSemOffsetLimitFailMask[]) | Configures the array of limit fail mask of the offset segments that specifies the criteria to determine the measurement fail status. Use "subblock(n)" as the selector string to read results from this method. |
| ConfigureOffsetRbwFilter(string, double, RFmxLteMXSemOffsetRbwFilterType) | Configures the offset RBW and the offset RBW filter type. Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to configure this method. |
| ConfigureOffsetRbwFilterArray(string, double[], RFmxLteMXSemOffsetRbwFilterType[]) | Configures the offset RBW and the offset RBW filter type arrays. Use "subblock(n)" as the selector string to configure from this method. |
| ConfigureOffsetRelativeLimit(string, double, double) | Configures the start and stop relative limit of the offset segment. Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to read results from this method. This method is considered only when you set the Link Direction method to Downlink and SEM DL Mask Type method to Custom. |
| ConfigureOffsetRelativeLimitArray(string, double[], double[]) | Configures the array of start and stop relative limits of the offset segments. Use "subblock(n)" as the selector string to read results from this method. This method is considered only when you set the Link Direction method to Downlink and SEM DL Mask Type method to Custom. |
| ConfigureSweepTime(string, RFmxLteMXSemSweepTimeAuto, double) | Configures the sweep time. |
| ConfigureUplinkMaskType(string, RFmxLteMXSemUplinkMaskType) | Configures the standard defined mask type that has to be used in the measurement for uplink. |
| GetAggregatedMaximumPower(string, out double) | Gets the aggregated maximum output power of all transmit antenna connectors. This value is expressed in dBm. Refer to the Section 6.6.3 of 3GPP 36.141 specification for more details. |
| GetAllTracesEnabled(string, out bool) | Gets whether to enable the traces to be stored and retrieved after performing the SEM measurement. |
| GetAmplitudeCorrectionType(string, out RFmxLteMXSemAmplitudeCorrectionType) | Gets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |
| GetAveragingCount(string, out int) | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxLteMXSemAveragingEnabled) method to True. |
| GetAveragingEnabled(string, out RFmxLteMXSemAveragingEnabled) | Gets whether to enable averaging for the SEM measurement. |
| GetAveragingType(string, out RFmxLteMXSemAveragingType) | Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement. |
| GetDeltaFMaximum(string, out double) | Gets the stop frequency for the last offset segment to be used in the measurement. This value is expressed in Hz. |
| GetDownlinkMaskType(string, out RFmxLteMXSemDownlinkMaskType) | Gets the limits to be used in the measurement for downlink. Refer to section 6.6.3 of the 3GPP 36.141 specification for more information about standard-defined mask types. |
| GetMeasurementEnabled(string, out bool) | Gets whether to enable the SEM measurement. |
| GetNumberOfAnalysisThreads(string, out int) | Gets the maximum number of threads used for parallelism for the SEM measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| GetNumberOfOffsets(string, out int) | Gets the number of SEM offset segments. |
| GetOffsetAbsoluteLimitStart(string, out double) | Gets the absolute power limit corresponding to the beginning of an offset segment. This value is expressed in dBm. |
| GetOffsetAbsoluteLimitStop(string, out double) | Gets the absolute power limit corresponding to the end of an offset segment. This value is expressed in dBm. |
| GetOffsetBandwidthIntegral(string, out int) | Gets the resolution of a spectrum to compare with the spectral mask limits as an integer multiple of the RBW. |
| GetOffsetLimitFailMask(string, out RFmxLteMXSemOffsetLimitFailMask) | Gets the criteria to determine the measurement fail status. |
| GetOffsetRbwFilterBandwidth(string, out double) | Gets the bandwidth of an RBW filter used to sweep an acquired offset segment. This value is expressed in Hz. |
| GetOffsetRbwFilterType(string, out RFmxLteMXSemOffsetRbwFilterType) | Gets the shape of a digital RBW filter. |
| GetOffsetRelativeLimitStart(string, out double) | Gets the relative power limit corresponding to the beginning of the offset segment. This value is expressed in dB. |
| GetOffsetRelativeLimitStop(string, out double) | Gets the relative power limit corresponding to the end of the offset segment. This value is expressed in dB. |
| GetOffsetSideband(string, out RFmxLteMXSemOffsetSideband) | Gets whether the offset segment is present either on one side or on both sides of a carrier. |
| GetOffsetStartFrequency(string, out double) | Gets the start frequency of an offset segment relative to the SetBandwidth(string, double) edge (single carrier) or GetSubblockAggregatedChannelBandwidth(string, out double) edge (multi-carrier). This value is expressed in Hz. |
| GetOffsetStopFrequency(string, out double) | Gets the stop frequency of an offset segment relative to the SetBandwidth(string, double) edge (single carrier) or GetSubblockAggregatedChannelBandwidth(string, out double) edge (multi-carrier). This value is expressed in Hz. |
| GetSidelinkMaskType(string, out RFmxLteMXSemSidelinkMaskType) | Gets the spectrum emission mask used in the measurement for sidelink. Each mask type refers to a different Network Signalled (NS) value. You must set the mask type to Custom to configure the custom offset masks. Refer to section 6.6.2 of the 3GPP 36.521 specification for more information about standard-defined mask types. |
| GetSubblockAggregatedChannelBandwidth(string, out double) | Gets the aggregated channel bandwidth of a configured subblock. This value is expressed in Hz. The aggregated channel bandwidth is the sum of the subblock integration bandwidth and the guard bands on either side of the subblock integration bandwidth. |
| GetSubblockIntegrationBandwidth(string, out double) | Gets the integration bandwidth of a subblock. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. |
| GetSweepTimeAuto(string, out RFmxLteMXSemSweepTimeAuto) | Gets whether the measurement computes the sweep time. |
| GetSweepTimeInterval(string, out double) | Gets the sweep time when you set the SetSweepTimeAuto(string, RFmxLteMXSemSweepTimeAuto) method to False. This value is expressed in seconds. |
| GetUplinkMaskType(string, out RFmxLteMXSemUplinkMaskType) | Gets the spectrum emission mask used in the measurement for uplink. Each mask type refers to a different Network Signalled (NS) value. General_CAClassB, CANS04, and CANCNS01 refers to carrier aggregation case. You must set the mask type to Custom to configure the custom offset masks. Refer to section 6.6.2.1 of the 3GPP 36.521 specification for more information about standard-defined mask types. |
| SetAggregatedMaximumPower(string, double) | Sets the aggregated maximum output power of all transmit antenna connectors. This value is expressed in dBm. Refer to the Section 6.6.3 of 3GPP 36.141 specification for more details. |
| SetAllTracesEnabled(string, bool) | Sets whether to enable the traces to be stored and retrieved after performing the SEM measurement. |
| SetAmplitudeCorrectionType(string, RFmxLteMXSemAmplitudeCorrectionType) | Sets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |
| SetAveragingCount(string, int) | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxLteMXSemAveragingEnabled) method to True. |
| SetAveragingEnabled(string, RFmxLteMXSemAveragingEnabled) | Sets whether to enable averaging for the SEM measurement. |
| SetAveragingType(string, RFmxLteMXSemAveragingType) | Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement. |
| SetDeltaFMaximum(string, double) | Sets the stop frequency for the last offset segment to be used in the measurement. This value is expressed in Hz. |
| SetDownlinkMaskType(string, RFmxLteMXSemDownlinkMaskType) | Sets the limits to be used in the measurement for downlink. Refer to section 6.6.3 of the 3GPP 36.141 specification for more information about standard-defined mask types. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable the SEM measurement. |
| SetNumberOfAnalysisThreads(string, int) | Sets the maximum number of threads used for parallelism for the SEM measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| SetNumberOfOffsets(string, int) | Sets the number of SEM offset segments. |
| SetOffsetAbsoluteLimitStart(string, double) | Sets the absolute power limit corresponding to the beginning of an offset segment. This value is expressed in dBm. |
| SetOffsetAbsoluteLimitStop(string, double) | Sets the absolute power limit corresponding to the end of an offset segment. This value is expressed in dBm. |
| SetOffsetBandwidthIntegral(string, int) | Sets the resolution of a spectrum to compare with the spectral mask limits as an integer multiple of the RBW. |
| SetOffsetLimitFailMask(string, RFmxLteMXSemOffsetLimitFailMask) | Sets the criteria to determine the measurement fail status. |
| SetOffsetRbwFilterBandwidth(string, double) | Sets the bandwidth of an RBW filter used to sweep an acquired offset segment. This value is expressed in Hz. |
| SetOffsetRbwFilterType(string, RFmxLteMXSemOffsetRbwFilterType) | Sets the shape of a digital RBW filter. |
| SetOffsetRelativeLimitStart(string, double) | Sets the relative power limit corresponding to the beginning of the offset segment. This value is expressed in dB. |
| SetOffsetRelativeLimitStop(string, double) | Sets the relative power limit corresponding to the end of the offset segment. This value is expressed in dB. |
| SetOffsetSideband(string, RFmxLteMXSemOffsetSideband) | Sets whether the offset segment is present either on one side or on both sides of a carrier. |
| SetOffsetStartFrequency(string, double) | Sets the start frequency of an offset segment relative to the SetBandwidth(string, double) edge (single carrier) or GetSubblockAggregatedChannelBandwidth(string, out double) edge (multi-carrier). This value is expressed in Hz. |
| SetOffsetStopFrequency(string, double) | Sets the stop frequency of an offset segment relative to the SetBandwidth(string, double) edge (single carrier) or GetSubblockAggregatedChannelBandwidth(string, out double) edge (multi-carrier). This value is expressed in Hz. |
| SetSidelinkMaskType(string, RFmxLteMXSemSidelinkMaskType) | Sets the spectrum emission mask used in the measurement for sidelink. Each mask type refers to a different Network Signalled (NS) value. You must set the mask type to Custom to configure the custom offset masks. Refer to section 6.6.2 of the 3GPP 36.521 specification for more information about standard-defined mask types. |
| SetSweepTimeAuto(string, RFmxLteMXSemSweepTimeAuto) | Sets whether the measurement computes the sweep time. |
| SetSweepTimeInterval(string, double) | Sets the sweep time when you set the SetSweepTimeAuto(string, RFmxLteMXSemSweepTimeAuto) method to False. This value is expressed in seconds. |
| SetUplinkMaskType(string, RFmxLteMXSemUplinkMaskType) | Sets the spectrum emission mask used in the measurement for uplink. Each mask type refers to a different Network Signalled (NS) value. General_CAClassB, CANS04, and CANCNS01 refers to carrier aggregation case. You must set the mask type to Custom to configure the custom offset masks. Refer to section 6.6.2.1 of the 3GPP 36.521 specification for more information about standard-defined mask types. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemdownlinkmasktype.html language=enus -->
## TOPIC 00234: RFmxLteMXSemDownlinkMaskType Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemdownlinkmasktype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemdownlinkmasktype.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the limits to be used in the measurement for downlink. Refer to section 6.6.3 of the 3GPP 36.141 specification for more information about standard-defined mask types. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXSemDownlinkMaskTypeMembersNameValueDescriptionENodeBCat

### RFmxLteMXSemDownlinkMaskType Enumeration

Specifies the limits to be used in the measurement for downlink. Refer to section 6.6.3 of the *3GPP 36.141* specification for more information about standard-defined mask types.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXSemDownlinkMaskType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ENodeBCategoryBased | 0 | The limits are applied based on eNodeBCategory method. |
| Band46 | 1 | The limits are applied based on Band 46 test requirements. |
| Custom | 5 | You need to configure the SetNumberOfOffsets(string, int), SetOffsetStartFrequency(string, double), SetOffsetStopFrequency(string, double), SetOffsetAbsoluteLimitStart(string, double), SetOffsetAbsoluteLimitStop(string, double), SetOffsetRelativeLimitStart(string, double), SetOffsetRelativeLimitStop(string, double), SetOffsetSideband(string, RFmxLteMXSemOffsetSideband), SetOffsetRbwFilterBandwidth(string, double), SetOffsetRbwFilterType(string, RFmxLteMXSemOffsetRbwFilterType), and SetOffsetBandwidthIntegral(string, int) properties for each offset. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemoffsetrbwfiltertype.html language=enus -->
## TOPIC 00235: RFmxLteMXSemOffsetRbwFilterType Enumeration

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemoffsetrbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemoffsetrbwfiltertype.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of a digital RBW filter. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic enum RFmxLteMXSemOffsetRbwFilterTypeMembersNameValueDescriptionFftBased0No RBW filtering is performed. Gaussian1The RBW filter has a Gaussian response. Flat2The RBW filter has a flat response.

### RFmxLteMXSemOffsetRbwFilterType Enumeration

Specifies the shape of a digital RBW filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public enum RFmxLteMXSemOffsetRbwFilterType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| FftBased | 0 | No RBW filtering is performed. |
| Gaussian | 1 | The RBW filter has a Gaussian response. |
| Flat | 2 | The RBW filter has a flat response. |

Parent topic:

NationalInstruments.RFmx.LteMX

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchloweroffsetmarginarray__string-double-ref-ref-ref-ref-ref.html language=enus -->
## TOPIC 00236: FetchLowerOffsetMarginArray(string, double, ref RFmxLteMXSemLowerOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[])

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchloweroffsetmarginarray__string-double-ref-ref-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchloweroffsetmarginarray__string-double-ref-ref-ref-ref-ref.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of measurement statuses, margins, frequencies at margins, and absolute and relative powers at margins for lower offset segments. The relative power is relative to the total aggregated power. Use "subblock(n)" as the selector string to read results from this method. Refer to the LTE

### FetchLowerOffsetMarginArray(string, double, ref RFmxLteMXSemLowerOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[])

Returns an array of measurement statuses, margins, frequencies at margins, and absolute and relative powers at margins for lower offset segments. The relative power is relative to the total aggregated power. 
 Use "subblock(n)" as the selector string to read results from this method. 
 Refer to the [LTE Uplink Spectral Emission Mask](/csh?context=rfmxlte_rfmxlte_lte_spectral_emission_mask_sem) and LTE Downlink Spectral Emission Mask topics for more information.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchLowerOffsetMarginArray(string selectorString, double timeout, ref RFmxLteMXSemLowerOffsetMeasurementStatus[] measurementStatus, ref double[] margin, ref double[] marginFrequency, ref double[] marginAbsolutePower, ref double[] marginRelativePower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| measurementStatus | ref RFmxLteMXSemLowerOffsetMeasurementStatus[] | Upon return, contains the array of the measurement status indicating whether the power before and after the burst is within the standard defined limit. |
| margin | ref double[] | Upon return, contains the array of margins from the standard-defined absolute limit mask for the lower (negative) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the SEM results lower offset start frequency and SEM results lower offset stop frequency are updated, and the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| marginFrequency | ref double[] | Upon return, contains the array of frequency at which the margin occurs in the lower (negative) offset. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the SEM results lower offset start frequency and SEM results lower offset stop frequency are updated, and the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| marginAbsolutePower | ref double[] | Upon return, contains the array of power at which the margin occurs in the upper (positive) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the SEM results lower offset start frequency and SEM results lower offset stop frequency are updated, and the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| marginRelativePower | ref double[] | Upon return, contains the array of powers at which the margin occurs in the upper (positive) offset segment relative to the value returned by the GetTotalAggregatedPower(string, out double) method. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchloweroffsetpower__string-double-out-out-out-out-out.html language=enus -->
## TOPIC 00237: FetchLowerOffsetPower(string, double, out double, out double, out double, out double, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchloweroffsetpower__string-double-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchloweroffsetpower__string-double-out-out-out-out-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the total absolute and relative powers, peak, absolute, and relative powers, and the frequency at the peak absolute power of the lower offset segment. The relative power is relative to the total aggregated power. Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to read resul

### FetchLowerOffsetPower(string, double, out double, out double, out double, out double, out double)

Returns the total absolute and relative powers, peak, absolute, and relative powers, and the frequency at the peak absolute power of the lower offset segment. The relative power is relative to the total aggregated power. 
 Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to read results from this method. 
 Refer to the [LTE Uplink Spectral Emission Mask](/csh?context=rfmxlte_rfmxlte_lte_spectral_emission_mask_sem) and LTE Downlink Spectral Emission Mask topics for more information.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchLowerOffsetPower(string selectorString, double timeout, out double absoluteIntegratedPower, out double relativeIntegratedPower, out double absolutePeakPower, out double peakFrequency, out double relativePeakPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and offset number. If you do not specify the result name, the default result instance is used. Example:"subblock0/offset0""result::r1/subblock0/offset0" You can use the BuildOffsetString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| absoluteIntegratedPower | out double | Upon return, contains the lower (negative) offset segment power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| relativeIntegratedPower | out double | Upon return, contains the power in the lower (negative) offset segment relative to the value returned by the GetTotalAggregatedPower(string, out double) method. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| absolutePeakPower | out double | Upon return, contains the peak power in the lower (negative) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| peakFrequency | out double | Upon return, contains the frequency at which the peak power occurs in the upper (positive) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| relativePeakPower | out double | Upon return, contains the peak power in the upper (positive) offset segment relative to the value returned by the SEM Results Total Aggregated Pwr method. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchloweroffsetpowerarray__string-double-ref-ref-ref-ref-ref.html language=enus -->
## TOPIC 00238: FetchLowerOffsetPowerArray(string, double, ref double[], ref double[], ref double[], ref double[], ref double[])

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchloweroffsetpowerarray__string-double-ref-ref-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchloweroffsetpowerarray__string-double-ref-ref-ref-ref-ref.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of total absolute and relative powers, peak, absolute, and relative powers, and frequencies at peak absolute powers of lower offset segments. The relative power is relative to total aggregated power. Use "subblock(n)" as the selector string to read results from this method. Refer to

### FetchLowerOffsetPowerArray(string, double, ref double[], ref double[], ref double[], ref double[], ref double[])

Returns an array of total absolute and relative powers, peak, absolute, and relative powers, and frequencies at peak absolute powers of lower offset segments. The relative power is relative to total aggregated power. 
 Use "subblock(n)" as the selector string to read results from this method. 
 Refer to the [LTE Uplink Spectral Emission Mask](/csh?context=rfmxlte_rfmxlte_lte_spectral_emission_mask_sem) and LTE Downlink Spectral Emission Mask topics for more information.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchLowerOffsetPowerArray(string selectorString, double timeout, ref double[] absoluteIntegratedPower, ref double[] relativeIntegratedPower, ref double[] absolutePeakPower, ref double[] peakFrequency, ref double[] relativePeakPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| absoluteIntegratedPower | ref double[] | Upon return, contains the array of lower (negative) offset segment powers. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| relativeIntegratedPower | ref double[] | Upon return, contains the array of powers in the lower (negative) offset segment relative to the value returned by the GetTotalAggregatedPower(string, out double) method. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| absolutePeakPower | ref double[] | Upon return, contains the array of peak powers in the lower (negative) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| peakFrequency | ref double[] | Upon return, contains the array of frequency at which the peak power occurs in the upper (positive) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| relativePeakPower | ref double[] | Upon return, contains the array of peak power in the upper (positive) offset segment relative to the value returned by the SEM Results Total Aggregated Pwr method. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchmeasurementstatus__string-double-out.html language=enus -->
## TOPIC 00239: FetchMeasurementStatus(string, double, out RFmxLteMXSemMeasurementStatus)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchmeasurementstatus__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchmeasurementstatus__string-double-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the overall measurement status based on the standard mask type that you configure.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchMeasurementStatus(string selectorString, double timeout, out RFmxLteMXSemMeasurementStatus measurementStatus)ParametersNameTypeDescriptionselectorS

### FetchMeasurementStatus(string, double, out RFmxLteMXSemMeasurementStatus)

Returns the overall measurement status based on the standard mask type that you configure.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchMeasurementStatus(string selectorString, double timeout, out RFmxLteMXSemMeasurementStatus measurementStatus)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| measurementStatus | out RFmxLteMXSemMeasurementStatus | Upon return, contains the measurement status indicating whether the power before and after the burst is within the standard defined limit. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchspectrum__string-double-ref-ref.html language=enus -->
## TOPIC 00240: FetchSpectrum(string, double, ref Spectrum< float >, ref Spectrum< float >)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchspectrum__string-double-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchspectrum__string-double-ref-ref.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for the SEM measurement.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchSpectrum(string selectorString, double timeout, ref Spectrum< float > spectrum, ref Spectrum< float > compositeMask)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector s

### FetchSpectrum(string, double, ref Spectrum< float >, ref Spectrum< float >)

Fetches the spectrum used for the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchSpectrum(string selectorString, double timeout, ref Spectrum< float > spectrum, ref Spectrum< float > compositeMask)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| spectrum | ref Spectrum< float > | Upon return, contains the spectrum. |
| compositeMask | ref Spectrum< float > | Upon return, contains the composite mask trace used for the channel. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchsubblockmeasurement__string-double-out-out-out.html language=enus -->
## TOPIC 00241: FetchSubblockMeasurement(string, double, out double, out double, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchsubblockmeasurement__string-double-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchsubblockmeasurement__string-double-out-out-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power, integration bandwidth and center frequency of the subblock. Use "subblock(n)" as the selector string to read results from this method. SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchSubblockMeasurement(string selectorString, double timeout, out double subblockPower

### FetchSubblockMeasurement(string, double, out double, out double, out double)

Returns the power, integration bandwidth and center frequency of the subblock. 
 Use "subblock(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchSubblockMeasurement(string selectorString, double timeout, out double subblockPower, out double integrationBandwidth, out double frequency)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| subblockPower | out double | Upon return, contains the sum of powers of all the frequency bins over the integration bandwidth of the subblock. |
| integrationBandwidth | out double | Upon return, contains the integration bandwidth of the subblock. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within a subblock |
| frequency | out double | Upon return, contains the absolute center frequency of the subblock. This value is the center of the subblock integration bandwidth. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchtotalaggregatedpower__string-double-out.html language=enus -->
## TOPIC 00242: FetchTotalAggregatedPower(string, double, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchtotalaggregatedpower__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchtotalaggregatedpower__string-double-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the sum of powers of all subblocks.SyntaxNamespace: NationalInstruments.RFmx.LteMXpublic int FetchTotalAggregatedPower(string selectorString, double timeout, out double totalAggregatedPower)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the result

### FetchTotalAggregatedPower(string, double, out double)

Returns the sum of powers of all subblocks.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchTotalAggregatedPower(string selectorString, double timeout, out double totalAggregatedPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| totalAggregatedPower | out double | Upon return, contains the sum of powers of all the subblocks. This value includes the power in the inter-carrier gaps within a subblock, but it does not include the power in the subblock gaps. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchupperoffsetmargin__string-double-out-out-out-out-out.html language=enus -->
## TOPIC 00243: FetchUpperOffsetMargin(string, double, out RFmxLteMXSemUpperOffsetMeasurementStatus, out double, out double, out double, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchupperoffsetmargin__string-double-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchupperoffsetmargin__string-double-out-out-out-out-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status, margin, frequency at margin, and absolute and relative powers at margin for upper offset segments. The relative power is relative to total aggregated power. Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to read results from this method. Refer to th

### FetchUpperOffsetMargin(string, double, out RFmxLteMXSemUpperOffsetMeasurementStatus, out double, out double, out double, out double)

Returns the measurement status, margin, frequency at margin, and absolute and relative powers at margin for upper offset segments. The relative power is relative to total aggregated power. 
 Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to read results from this method. 
 Refer to the [LTE Uplink Spectral Emission Mask](/csh?context=rfmxlte_rfmxlte_lte_spectral_emission_mask_sem) and LTE Downlink Spectral Emission Mask topics for more information.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchUpperOffsetMargin(string selectorString, double timeout, out RFmxLteMXSemUpperOffsetMeasurementStatus measurementStatus, out double margin, out double marginFrequency, out double marginAbsolutePower, out double marginRelativePower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and offset number. If you do not specify the result name, the default result instance is used. Example:"subblock0/offset0""result::r1/subblock0/offset0" You can use the BuildOffsetString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| measurementStatus | out RFmxLteMXSemUpperOffsetMeasurementStatus | Upon return, contains the measurement status indicating whether the power before and after the burst is within the standard defined limit. |
| margin | out double | Upon return, contains the margin from the standard defined absolute limit mask for upper offset. Margin is defined as the minimum difference between the spectrum and the limit mask. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| marginFrequency | out double | Upon return, contains the frequency at which the margin occurs in the upper offset. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| marginAbsolutePower | out double | Upon return, contains the power at which the margin occurs in the upper (positive) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the SEM results lower offset start frequency and SEM results lower offset stop frequency are updated, and the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| marginRelativePower | out double | Upon return, contains the power at which the margin occurs in the upper (positive) offset segment relative to the value returned by the GetTotalAggregatedPower(string, out double) method. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchupperoffsetmarginarray__string-double-ref-ref-ref-ref-ref.html language=enus -->
## TOPIC 00244: FetchUpperOffsetMarginArray(string, double, ref RFmxLteMXSemUpperOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[])

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchupperoffsetmarginarray__string-double-ref-ref-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchupperoffsetmarginarray__string-double-ref-ref-ref-ref-ref.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of measurement statuses, margins, frequencies at margins, and absolute and relative powers at margins for upper offset segments. The relative power is relative to total aggregated power. Use "subblock(n)" as the selector string to read results from this method. Refer to the LTE Upli

### FetchUpperOffsetMarginArray(string, double, ref RFmxLteMXSemUpperOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[])

Returns an array of measurement statuses, margins, frequencies at margins, and absolute and relative powers at margins for upper offset segments. The relative power is relative to total aggregated power. 
 Use "subblock(n)" as the selector string to read results from this method. 
 Refer to the [LTE Uplink Spectral Emission Mask](/csh?context=rfmxlte_rfmxlte_lte_spectral_emission_mask_sem) and LTE Downlink Spectral Emission Mask topics for more information.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchUpperOffsetMarginArray(string selectorString, double timeout, ref RFmxLteMXSemUpperOffsetMeasurementStatus[] measurementStatus, ref double[] margin, ref double[] marginFrequency, ref double[] marginAbsolutePower, ref double[] marginRelativePower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| measurementStatus | ref RFmxLteMXSemUpperOffsetMeasurementStatus[] | Upon return, contains the array of the measurement status indicating whether the power before and after the burst is within the standard defined limit. |
| margin | ref double[] | Upon return, contains the array of margins from the standard defined absolute limit mask for upper offset. The margin is defined as the minimum difference between the spectrum and the limit mask. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| marginFrequency | ref double[] | Upon return, contains the array of frequency at which the margin occurs in the upper offset. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| marginAbsolutePower | ref double[] | Upon return, contains the array of power at which the margin occurs in the upper (positive) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the SEM results lower offset start frequency and SEM results lower offset stop frequency are updated, and the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| marginRelativePower | ref double[] | Upon return, contains the array of powers at which the margin occurs in the upper (positive) offset segment relative to the value returned by the GetTotalAggregatedPower(string, out double) method. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchupperoffsetpower__string-double-out-out-out-out-out.html language=enus -->
## TOPIC 00245: FetchUpperOffsetPower(string, double, out double, out double, out double, out double, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchupperoffsetpower__string-double-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-fetchupperoffsetpower__string-double-out-out-out-out-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the total absolute and relative powers, peak, absolute, and relative powers, and frequency at peak absolute power of upper offset segment. The relative power is relative to total aggregated power. Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to read results from this met

### FetchUpperOffsetPower(string, double, out double, out double, out double, out double, out double)

Returns the total absolute and relative powers, peak, absolute, and relative powers, and frequency at peak absolute power of upper offset segment. The relative power is relative to total aggregated power. 
 Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to read results from this method. 
 Refer to the [LTE Uplink Spectral Emission Mask](/csh?context=rfmxlte_rfmxlte_lte_spectral_emission_mask_sem) and LTE Downlink Spectral Emission Mask topics for more information.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int FetchUpperOffsetPower(string selectorString, double timeout, out double absoluteIntegratedPower, out double relativeIntegratedPower, out double absolutePeakPower, out double peakFrequency, out double relativePeakPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and offset number. If you do not specify the result name, the default result instance is used. Example:"subblock0/offset0""result::r1/subblock0/offset0" You can use the BuildOffsetString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| absoluteIntegratedPower | out double | Upon return, contains the upper offset segment power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| relativeIntegratedPower | out double | Upon return, contains the power in the upper offset segment relative to the value returned by the GetTotalAggregatedPower(string, out double) method. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| absolutePeakPower | out double | Upon return, contains the peak power in the upper offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| peakFrequency | out double | Upon return, contains the frequency at which the peak power occurs in the upper (positive) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| relativePeakPower | out double | Upon return, contains the peak power in the upper (positive) offset segment relative to the value returned by the SEM Results Total Aggregated Pwr method. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getloweroffsetabsoluteintegratedpower__string-out.html language=enus -->
## TOPIC 00246: GetLowerOffsetAbsoluteIntegratedPower(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getloweroffsetabsoluteintegratedpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getloweroffsetabsoluteintegratedpower__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the lower (negative) offset segment power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is pe

### GetLowerOffsetAbsoluteIntegratedPower(string, out double)

Gets the lower (negative) offset segment power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the *3GPP TS 36.521* specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetLowerOffsetAbsoluteIntegratedPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetAbsoluteIntegratedPower](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the lower (negative) offset segment power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getloweroffsetabsolutepeakpower__string-out.html language=enus -->
## TOPIC 00247: GetLowerOffsetAbsolutePeakPower(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getloweroffsetabsolutepeakpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getloweroffsetabsolutepeakpower__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power in the lower (negative) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measu

### GetLowerOffsetAbsolutePeakPower(string, out double)

Gets the peak power in the lower (negative) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the *3GPP TS 36.521* specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetLowerOffsetAbsolutePeakPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetAbsolutePeakPower](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak power in the lower (negative) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getloweroffsetmargin__string-out.html language=enus -->
## TOPIC 00248: GetLowerOffsetMargin(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getloweroffsetmargin__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getloweroffsetmargin__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the margin from the standard-defined absolute limit mask for the lower (negative) offset. Margin is defined as the minimum difference between the limit mask and the spectrum. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on

### GetLowerOffsetMargin(string, out double)

Gets the margin from the standard-defined absolute limit mask for the lower (negative) offset. Margin is defined as the minimum difference between the limit mask and the spectrum. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the *3GPP TS 36.521* specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetLowerOffsetMargin(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetMargin](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the margin from the standard-defined absolute limit mask for the lower (negative) offset. Margin is defined as the minimum difference between the limit mask and the spectrum. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getloweroffsetmarginrelativepower__string-out.html language=enus -->
## TOPIC 00249: GetLowerOffsetMarginRelativePower(string, out double)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getloweroffsetmarginrelativepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getloweroffsetmarginrelativepower__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power at which the margin occurs in the lower (negative) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521

### GetLowerOffsetMarginRelativePower(string, out double)

Gets the power at which the margin occurs in the lower (negative) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the *3GPP TS 36.521* specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetLowerOffsetMarginRelativePower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetMarginRelativePower](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power at which the margin occurs in the lower (negative) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemResults Class

<!--NI_TOPIC bundle=rfmxlte-dotnet-api-ref path=nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getloweroffsetmeasurementstatus__string-out.html language=enus -->
## TOPIC 00250: GetLowerOffsetMeasurementStatus(string, out RFmxLteMXSemLowerOffsetMeasurementStatus)

- bundle_id: `rfmxlte-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getloweroffsetmeasurementstatus__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-ltemx-rfmxltemxsemresults-getloweroffsetmeasurementstatus__string-out.html
- document_id: `rfmxlte-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the measurement status based on the spectrum emission limits defined by the standard mask type that you configure in the SEM Standard Mask Type method. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. SyntaxNamespace: NationalInstruments.RFmx.LteMXpubl

### GetLowerOffsetMeasurementStatus(string, out RFmxLteMXSemLowerOffsetMeasurementStatus)

Indicates the measurement status based on the spectrum emission limits defined by the standard mask type that you configure in the SEM Standard Mask Type method. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.LteMX](nationalinstruments-rfmx-ltemx.html)

public int GetLowerOffsetMeasurementStatus(string selectorString, out RFmxLteMXSemLowerOffsetMeasurementStatus value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetMeasurementStatus](nationalinstruments-rfmx-ltemx-rfmxltemxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out RFmxLteMXSemLowerOffsetMeasurementStatus | Indicates the measurement status based on the spectrum emission limits defined by the standard mask type that you configure in the SEM Standard Mask Type method. Use "offset(k)" or "subblock(n)/offset(k)" as the selector string to read this result. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxLteMXSemResults Class
