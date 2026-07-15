# NI DOCUMENT BUNDLE: rfmxpulse-dotnet-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxpulse-dotnet-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxpulsemxextension-getpulsesignalconfiguration__this-string.html language=enus -->
## TOPIC 00001: GetPulseSignalConfiguration(this RFmxInstrMX, string)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxpulsemxextension-getpulsesignalconfiguration__this-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxpulsemxextension-getpulsesignalconfiguration__this-string.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a PULSE signal configuration for specified signal name. Existing PULSE signal configuration is returned if specified signal name exists. SyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic static RFmxPulseMX GetPulseSignalConfiguration(this RFmxInstrMX instrSession, string signalName)Par

### GetPulseSignalConfiguration(this RFmxInstrMX, string)

Creates a PULSE signal configuration for specified signal name. Existing PULSE signal configuration is returned if specified signal name exists.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public static [RFmxPulseMX](nationalinstruments-rfmx-pulsemx-rfmxpulsemx.html) GetPulseSignalConfiguration(this RFmxInstrMX instrSession, string signalName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| instrSession | this RFmxInstrMX | Specifies an RFmxInstr session. |
| signalName | string | Specifies a signal name. |

#### Returns

Returns an object of type RFmxPulseMX.

Parent topic:

RFmxPulseMXExtension Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxpulsemxextension-getpulsesignalconfiguration__this.html language=enus -->
## TOPIC 00002: GetPulseSignalConfiguration(this RFmxInstrMX)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxpulsemxextension-getpulsesignalconfiguration__this.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxpulsemxextension-getpulsesignalconfiguration__this.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new default PULSE signal configuration if it doesn't exist; otherwise, it returns the existing default PULSE signal configuration. SyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic static RFmxPulseMX GetPulseSignalConfiguration(this RFmxInstrMX instrSession)ParametersNameTypeDescript

### GetPulseSignalConfiguration(this RFmxInstrMX)

Creates a new default PULSE signal configuration if it doesn't exist; otherwise, it returns the existing default PULSE signal configuration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public static [RFmxPulseMX](nationalinstruments-rfmx-pulsemx-rfmxpulsemx.html) GetPulseSignalConfiguration(this RFmxInstrMX instrSession)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| instrSession | this RFmxInstrMX | Specifies an instr session. |

#### Returns

Returns an object of type RFmxPulseMX.

Parent topic:

RFmxPulseMXExtension Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxpulsemxextension.html language=enus -->
## TOPIC 00003: RFmxPulseMXExtension Class

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxpulsemxextension.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxpulsemxextension.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides extension methods to create PULSE signal configuration. These methods are added to RFmxInstrMX class. Derives fromNoneSyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic class RFmxPulseMXExtensionRemarksFor more information about NI-RFmx Instruments, refer to the NI-RFmx Instruments Hel

### RFmxPulseMXExtension Class

Provides extension methods to create PULSE signal configuration. These methods are added to RFmxInstrMX class.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public class RFmxPulseMXExtension

#### Remarks

For more information about NI-RFmx Instruments, refer to the NI-RFmx Instruments Help.

#### Thread Safety

Any public static members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| GetPulseSignalConfiguration(this RFmxInstrMX, string) | Creates a PULSE signal configuration for specified signal name. Existing PULSE signal configuration is returned if specified signal name exists. |
| GetPulseSignalConfiguration(this RFmxInstrMX) | Creates a new default PULSE signal configuration if it doesn't exist; otherwise, it returns the existing default PULSE signal configuration. |

Parent topic:

NationalInstruments.RFmx.InstrMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-instrmx.html language=enus -->
## TOPIC 00004: NationalInstruments.RFmx.InstrMX

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionRFmxPulseMXExtensionProvides extension methods to create PULSE signal configuration. These methods are added to RFmxInstrMX class. InterfacesNoneStructuresNoneEnumerationsNoneDelegatesNone

### NationalInstruments.RFmx.InstrMX

#### Classes

| Name | Description |
| --- | --- |
| RFmxPulseMXExtension | Provides extension methods to create PULSE signal configuration. These methods are added to RFmxInstrMX class. |

#### Interfaces

None

#### Structures

None

#### Enumerations

None

#### Delegates

None

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-abortmeasurements__string.html language=enus -->
## TOPIC 00005: AbortMeasurements(string)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-abortmeasurements__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-abortmeasurements__string.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops acquisition and measurements associated with signal instance that you specify in the selectorString parameter, which were previously initiated by the Initiate(string, string) method or measurement read methods. Calling this method is optional, unless you want to stop a measurement before it is

### AbortMeasurements(string)

Stops acquisition and measurements associated with signal instance that you specify in the *selectorString* parameter, which were previously initiated by the [Initiate(string, string)](nationalinstruments-rfmx-pulsemx-rfmxpulsemx-initiate__string-string.html) method or measurement read methods. Calling this method is optional, unless you want to stop a measurement before it is complete. This method executes even if there is an incoming error.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int AbortMeasurements(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the result name in this parameter, either the result name specified by the resultName parameter or the default result instance is used. Example:"""""result::r1" |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-analyzeiq1waveform__string-string-complexwaveform_complexsingle_-bool-long.html language=enus -->
## TOPIC 00006: AnalyzeIQ1Waveform(string, string, ComplexWaveform< ComplexSingle >, bool, long)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-analyzeiq1waveform__string-string-complexwaveform_complexsingle_-bool-long.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-analyzeiq1waveform__string-string-complexwaveform_complexsingle_-bool-long.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods in the method node. Use this method only if the RFmxIns

### AnalyzeIQ1Waveform(string, string, ComplexWaveform< ComplexSingle >, bool, long)

Performs the enabled measurements on the I/Q complex waveform that you specify in *IQ* parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods in the method node. Use this method only if the RFmxInstrMX.GetRecommendedAcquisitionType method value is either *IQ* or *IQorSpectral*. 
 Query the Recommended Acquisition Type method from the RFmxInstr Property Node after calling the RFmx Pulse Commit method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int AnalyzeIQ1Waveform(string selectorString, string resultName, ComplexWaveform< ComplexSingle > iq, bool reset, long reserved)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| resultName | string | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"result::r1""r1" |
| iq | ComplexWaveform< ComplexSingle > | Specifies the data for a complex waveform including the start, delta, and actual values. |
| reset | bool | Resets measurement averaging. If you enable averaging, set this parameter to TRUE for the first record and FALSE for the subsequent records. |
| reserved | long | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-autolevel__string-double-double-out.html language=enus -->
## TOPIC 00007: AutoLevel(string, double, double, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-autolevel__string-double-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-autolevel__string-double-double-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Examines the input signal to calculate the peak power level and sets it as the value of the ReferenceLevel method. Use this method to help calculate an approximate setting for the reference level. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int AutoLevel(string selectorString, double ban

### AutoLevel(string, double, double, out double)

Examines the input signal to calculate the peak power level and sets it as the value of the [ReferenceLevel](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method. Use this method to help calculate an approximate setting for the reference level.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int AutoLevel(string selectorString, double bandwidth, double measurementInterval, out double referenceLevel)

#### Remarks

1. Resets the mixer level, mixer level offset and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation and preamp enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after completing execution.

AutoLevelInitialReferenceLevel

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| bandwidth | double | Specifies the bandwidth, in Hz, of the signal to be analyzed. |
| measurementInterval | double | Specifies the acquisition length. Use this value to compute the number of samples to acquire from the signal analyzer. This value is expressed in seconds. Auto Level method does not use any trigger for acquisition. It ignores the user-configured trigger methods. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. |
| referenceLevel | out double | Upon return, contains the estimated peak power level of the input signal. This value is expressed in dBm for RF devices and as Vpk-pk for baseband devices. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-buildresultstring__string.html language=enus -->
## TOPIC 00008: BuildResultString(string)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-buildresultstring__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-buildresultstring__string.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates selector string for use with configuration or fetch. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic static string BuildResultString(string resultName)ParametersNameTypeDescriptionresultNamestringSpecifies the result name for building the selector string. This input accepts the resul

### BuildResultString(string)

Creates selector string for use with configuration or fetch.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public static string BuildResultString(string resultName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| resultName | string | Specifies the result name for building the selector string. This input accepts the result name with or without the "result::" prefix. Example: "", "result::r1", "r1". |

#### Returns

Upon return, contains the selector string created by this method.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-checkmeasurementstatus__string-out.html language=enus -->
## TOPIC 00009: CheckMeasurementStatus(string, out bool)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-checkmeasurementstatus__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-checkmeasurementstatus__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks the status of the measurement. Use this method to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int CheckMeasurementStatus(string selectorString, out bool

### CheckMeasurementStatus(string, out bool)

Checks the status of the measurement. Use this method to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int CheckMeasurementStatus(string selectorString, out bool isDone)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" |
| isDone | out bool | Indicates whether the measurement is complete. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-clearallnamedresults__string.html language=enus -->
## TOPIC 00010: ClearAllNamedResults(string)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-clearallnamedresults__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-clearallnamedresults__string.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all results for the current signal instance.SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int ClearAllNamedResults(string selectorString)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when creating the signal configuration is us

### ClearAllNamedResults(string)

Clears all results for the current signal instance.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int ClearAllNamedResults(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-clearnamedresult__string.html language=enus -->
## TOPIC 00011: ClearNamedResult(string)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-clearnamedresult__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-clearnamedresult__string.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears a result instance specified by the result name in the selectorString parameter.SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int ClearNamedResult(string selectorString)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the result name. If you

### ClearNamedResult(string)

Clears a result instance specified by the result name in the *selectorString* parameter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int ClearNamedResult(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-clonesignalconfiguration__string-out.html language=enus -->
## TOPIC 00012: CloneSignalConfiguration(string, out RFmxPulseMX)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-clonesignalconfiguration__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-clonesignalconfiguration__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal by copying all the method values from an existing signal instance.SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int CloneSignalConfiguration(string newSignalName, out RFmxPulseMX signalConfiguration)ParametersNameTypeDescriptionnewSignalNamestringSpecifie

### CloneSignalConfiguration(string, out RFmxPulseMX)

Creates a new instance of a signal by copying all the method values from an existing signal instance.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int CloneSignalConfiguration(string newSignalName, out RFmxPulseMX signalConfiguration)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| newSignalName | string | Specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix. Example:"signal::NewSigName""NewSigName" |
| signalConfiguration | out RFmxPulseMX | Upon return, contains a new Pulse signal instance. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-commit__string.html language=enus -->
## TOPIC 00013: Commit(string)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-commit__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-commit__string.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits settings to the hardware. Calling this method is optional. RFmxPulse commits settings to the hardware when you call the Initiate(string, string) method or any of the measurement Read methods.SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int Commit(string selectorString)ParametersNa

### Commit(string)

Commits settings to the hardware. Calling this method is optional. RFmxPulse commits settings to the hardware when you call the [Initiate(string, string)](nationalinstruments-rfmx-pulsemx-rfmxpulsemx-initiate__string-string.html) method or any of the measurement Read methods.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int Commit(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-configuredigitaledgetrigger__string-string-rfmxpulsemxdigitaledgetriggeredge-double-bool.html language=enus -->
## TOPIC 00014: ConfigureDigitalEdgeTrigger(string, string, RFmxPulseMXDigitalEdgeTriggerEdge, double, bool)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-configuredigitaledgetrigger__string-string-rfmxpulsemxdigitaledgetriggeredge-double-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-configuredigitaledgetrigger__string-string-rfmxpulsemxdigitaledgetriggeredge-double-bool.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a digital edge trigger and then marks a reference point within the record. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int ConfigureDigitalEdgeTrigger(string selectorString, string digitalEdgeTriggerSource, RFmxPulseMXDigitalEdgeTriggerEdge digitalEdgeTr

### ConfigureDigitalEdgeTrigger(string, string, RFmxPulseMXDigitalEdgeTriggerEdge, double, bool)

Configures the device to wait for a digital edge trigger and then marks a reference point within the record.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int ConfigureDigitalEdgeTrigger(string selectorString, string digitalEdgeTriggerSource, RFmxPulseMXDigitalEdgeTriggerEdge digitalEdgeTriggerEdge, double triggerDelay, bool enableTrigger)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| digitalEdgeTriggerSource | string | Specifies the source terminal for the RFmxPulseMXConstants. |
| digitalEdgeTriggerEdge | RFmxPulseMXDigitalEdgeTriggerEdge | Specifies the trigger edge to detect. |
| triggerDelay | double | Specifies the trigger delay time. This value is expressed in seconds. |
| enableTrigger | bool | Specifies whether to enable the trigger. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-configureexternalattenuation__string-double.html language=enus -->
## TOPIC 00015: ConfigureExternalAttenuation(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-configureexternalattenuation__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-configureexternalattenuation__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer.SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int ConfigureExternalAttenuation(string selectorString, double externalAttenuation)ParametersNameTypeDescriptionselectorStringstringPass an

### ConfigureExternalAttenuation(string, double)

Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int ConfigureExternalAttenuation(string selectorString, double externalAttenuation)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| externalAttenuation | double | Specifies the attenuation, in dB, of a switch (or cable) connected to the RF IN connector of the signal analyzer. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-configurefrequency__string-double.html language=enus -->
## TOPIC 00016: ConfigureFrequency(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-configurefrequency__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-configurefrequency__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int ConfigureFrequency(string selectorString, double centerFrequency)ParametersNameTypeDescriptionselectorStringstringPass an em

### ConfigureFrequency(string, double)

Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int ConfigureFrequency(string selectorString, double centerFrequency)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| centerFrequency | double | Specifies the expected carrier frequency, in Hz, of the RF signal to acquire. The signal analyzer tunes to this frequency. The default of this method is hardware dependent. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-configureiqpoweredgetrigger__string-string-rfmxpulsemxiqpoweredgetriggerslope-double-double-rfmxpulsemxtriggerminimumquiettimemode-double-rf...d21e589.html language=enus -->
## TOPIC 00017: ConfigureIQPowerEdgeTrigger(string, string, RFmxPulseMXIQPowerEdgeTriggerSlope, double, double, RFmxPulseMXTriggerMinimumQuietTimeMode, double, RFmxPulseMXIQPowerEdgeTriggerLevelType, bool)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-configureiqpoweredgetrigger__string-string-rfmxpulsemxiqpoweredgetriggerslope-double-double-rfmxpulsemxtriggerminimumquiettimemode-double-rf...d21e589.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-configureiqpoweredgetrigger__string-string-rfmxpulsemxiqpoweredgetriggerslope-double-double-rfmxpulsemxtriggerminimumquiettimemode-double-rf...d21e589.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int ConfigureIQPowerEdgeTrigger(string selectorString, string iqPowerEdgeTriggerSource, RFmxPulseM

### ConfigureIQPowerEdgeTrigger(string, string, RFmxPulseMXIQPowerEdgeTriggerSlope, double, double, RFmxPulseMXTriggerMinimumQuietTimeMode, double, RFmxPulseMXIQPowerEdgeTriggerLevelType, bool)

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int ConfigureIQPowerEdgeTrigger(string selectorString, string iqPowerEdgeTriggerSource, RFmxPulseMXIQPowerEdgeTriggerSlope iqPowerEdgeTriggerSlope, double iqPowerEdgeTriggerLevel, double triggerDelay, RFmxPulseMXTriggerMinimumQuietTimeMode triggerMinimumQuietTimeMode, double triggerMinimumQuietTimeDuration, RFmxPulseMXIQPowerEdgeTriggerLevelType iqPowerEdgeTriggerLevelType, bool enableTrigger)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| iqPowerEdgeTriggerSource | string | Specifies the channel from which the device monitors the trigger. |
| iqPowerEdgeTriggerSlope | RFmxPulseMXIQPowerEdgeTriggerSlope | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. |
| iqPowerEdgeTriggerLevel | double | Specifies the power level at which the device triggers, depending on the value of the iqPowerEdgeTriggerSlope parameter. The value is expressed in dB when the iqPowerEdgeTriggerLevelType parameter is set to Relative, or in dBm when it is set to Absolute. |
| triggerDelay | double | Specifies the trigger delay time. This value is expressed in seconds. |
| triggerMinimumQuietTimeMode | RFmxPulseMXTriggerMinimumQuietTimeMode | Specifies whether the measurement computes the minimum quiet time used for triggering. |
| triggerMinimumQuietTimeDuration | double | Specifies the duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set SetIQPowerEdgeTriggerSlope(string, RFmxPulseMXIQPowerEdgeTriggerSlope) to Rising, the signal is quiet when it is below the trigger level. |
| iqPowerEdgeTriggerLevelType | RFmxPulseMXIQPowerEdgeTriggerLevelType | Specifies whether the IQPowerEdgeLevel is set to Relative or Absolute. The value is expressed in dB when this parameter is set to Relative. The value is expressed in dBm when this parameter is set to Absolute. |
| enableTrigger | bool | Specifies whether the trigger is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-configurereferencelevel__string-double.html language=enus -->
## TOPIC 00018: ConfigureReferenceLevel(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-configurereferencelevel__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-configurereferencelevel__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference level, which represents the maximum expected power of an RF input signal.SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int ConfigureReferenceLevel(string selectorString, double referenceLevel)ParametersNameTypeDescriptionselectorStringstringPass an empty string. Th

### ConfigureReferenceLevel(string, double)

Configures the reference level, which represents the maximum expected power of an RF input signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int ConfigureReferenceLevel(string selectorString, double referenceLevel)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| referenceLevel | double | Specifies the reference level which represents the maximum expected power of an RF input signal. This value is configured in dBm for RF devices and as Vpk-pk for baseband devices. The default of this method is hardware dependent. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-configurerf__string-double-double-double.html language=enus -->
## TOPIC 00019: ConfigureRF(string, double, double, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-configurerf__string-double-double-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-configurerf__string-double-double-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RF methods of the signal specified by the selector string.SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int ConfigureRF(string selectorString, double centerFrequency, double referenceLevel, double externalAttenuation)ParametersNameTypeDescriptionselectorStringstringPass an e

### ConfigureRF(string, double, double, double)

Configures the RF methods of the signal specified by the selector string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int ConfigureRF(string selectorString, double centerFrequency, double referenceLevel, double externalAttenuation)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| centerFrequency | double | Specifies the expected carrier frequency, in Hz, of the RF signal to acquire. The signal analyzer tunes to this frequency. The default of this method is hardware dependent. |
| referenceLevel | double | Specifies the reference level which represents the maximum expected power of an RF input signal. This value is configured in dBm for RF devices and as Vpk-pk for baseband devices. The default of this method is hardware dependent. |
| externalAttenuation | double | Specifies the attenuation, in dB, of a switch (or cable) connected to the RF IN connector of the signal analyzer. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-configuresoftwareedgetrigger__string-double-bool.html language=enus -->
## TOPIC 00020: ConfigureSoftwareEdgeTrigger(string, double, bool)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-configuresoftwareedgetrigger__string-double-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-configuresoftwareedgetrigger__string-double-bool.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a software trigger and then marks a reference point within the record.SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int ConfigureSoftwareEdgeTrigger(string selectorString, double triggerDelay, bool enableTrigger)ParametersNameTypeDescriptionselectorStrings

### ConfigureSoftwareEdgeTrigger(string, double, bool)

Configures the device to wait for a software trigger and then marks a reference point within the record.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

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

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-deletesignalconfiguration.html language=enus -->
## TOPIC 00021: DeleteSignalConfiguration()

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-deletesignalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-deletesignalconfiguration.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes an instance of a signal.SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int DeleteSignalConfiguration()ReturnsReturns the status code of this method. The status code either indicates success or describes a warning condition.

### DeleteSignalConfiguration()

Deletes an instance of a signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int DeleteSignalConfiguration()

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-disabletrigger__string.html language=enus -->
## TOPIC 00022: DisableTrigger(string)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-disabletrigger__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-disabletrigger__string.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to not wait for a trigger to mark a reference point within a record. This method defines the signal triggering as immediate.SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int DisableTrigger(string selectorString)ParametersNameTypeDescriptionselectorStringstringPass an

### DisableTrigger(string)

Configures the device to not wait for a trigger to mark a reference point within a record. This method defines the signal triggering as immediate.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int DisableTrigger(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-dispose.html language=enus -->
## TOPIC 00023: Dispose()

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-dispose.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-dispose.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes the signal configuration if it is not the default signal configuration and clears any trace of the current signal configuration, if any. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic void Dispose()RemarksYou can call this method safely more than once, even if the signal is already

### Dispose()

Deletes the signal configuration if it is not the default signal configuration and clears any trace of the current signal configuration, if any.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public void Dispose()

#### Remarks

You can call this method safely more than once, even if the signal is already deleted.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getacquisitionlength__string-out.html language=enus -->
## TOPIC 00024: GetAcquisitionLength(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getacquisitionlength__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getacquisitionlength__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the acquisition length for the pulse measurement. This value is expressed in seconds.You configure this method when you set the SegmentedAcquisitionEnabled method to False. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAcquisitionLength(string selectorString, out double value)R

### GetAcquisitionLength(string, out double)

Gets the acquisition length for the pulse measurement. This value is expressed in seconds.You configure this method when you set the [SegmentedAcquisitionEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [False](nationalinstruments-rfmx-pulsemx-rfmxpulsemxsegmentedacquisitionenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAcquisitionLength(string selectorString, out double value)

#### Remarks

This method gets the value of [AcquisitionLength](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.001 seconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the acquisition length for the pulse measurement. This value is expressed in seconds.You configure this method when you set the SegmentedAcquisitionEnabled method to False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getallnamedresultnames__string-out-out.html language=enus -->
## TOPIC 00025: GetAllNamedResultNames(string, out string[], out bool)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getallnamedresultnames__string-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getallnamedresultnames__string-out-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the named result names of the signal that you specify in the selectorString parameter. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAllNamedResultNames(string selectorString, out string[] resultNames, out bool defaultResultExists)ParametersNameTypeDescriptionselectorStringstri

### GetAllNamedResultNames(string, out string[], out bool)

Gets the named result names of the signal that you specify in the *selectorString* parameter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAllNamedResultNames(string selectorString, out string[] resultNames, out bool defaultResultExists)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| resultNames | out string[] | Returns an array of result names. |
| defaultResultExists | out bool | Upon return, indicates whether the default result exists. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getattributebool__string-int-out.html language=enus -->
## TOPIC 00026: GetAttributeBool(string, int, out bool)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getattributebool__string-int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getattributebool__string-int-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of a Bool attribute. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAttributeBool(string selectorString, int attributeIdentifier, out bool value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being read. Refer to the Us

### GetAttributeBool(string, int, out bool)

Gets the value of a Bool attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAttributeBool(string selectorString, int attributeIdentifier, out bool value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx PULSE Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | out bool | Upon return, contains a value of the specified attribute ID. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getattributedouble__string-int-out.html language=enus -->
## TOPIC 00027: GetAttributeDouble(string, int, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getattributedouble__string-int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getattributedouble__string-int-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of a Double attribute. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAttributeDouble(string selectorString, int attributeIdentifier, out double value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being read. Refer to

### GetAttributeDouble(string, int, out double)

Gets the value of a Double attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAttributeDouble(string selectorString, int attributeIdentifier, out double value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx PULSE Help for more information about configuring the selector string. |
| attributeIdentifier | int | Passes the ID of an attribute. |
| value | out double | Upon return, contains a value of the specified attribute ID. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getattributedoublearray__string-int-ref.html language=enus -->
## TOPIC 00028: GetAttributeDoubleArray(string, int, ref double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getattributedoublearray__string-int-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getattributedoublearray__string-int-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of a double array attribute. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAttributeDoubleArray(string selectorString, int attributeIdentifier, ref double[] value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being re

### GetAttributeDoubleArray(string, int, ref double[])

Gets the value of a double array attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAttributeDoubleArray(string selectorString, int attributeIdentifier, ref double[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the RFmx Demod Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | ref double[] | Contains the value of the specified attribute ID. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getattributeint__string-int-out.html language=enus -->
## TOPIC 00029: GetAttributeInt(string, int, out int)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getattributeint__string-int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getattributeint__string-int-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of an RFmx 32-bit integer (int32) attribute. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAttributeInt(string selectorString, int attributeIdentifier, out int value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being

### GetAttributeInt(string, int, out int)

Gets the value of an RFmx 32-bit integer (int32) attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAttributeInt(string selectorString, int attributeIdentifier, out int value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx PULSE Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | out int | Upon return, contains a value of the specified attribute ID. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getattributeintarray__string-int-ref.html language=enus -->
## TOPIC 00030: GetAttributeIntArray(string, int, ref int[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getattributeintarray__string-int-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getattributeintarray__string-int-ref.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of a integer array attribute. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAttributeIntArray(string selectorString, int attributeIdentifier, ref int[] value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being read. R

### GetAttributeIntArray(string, int, ref int[])

Gets the value of a integer array attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAttributeIntArray(string selectorString, int attributeIdentifier, ref int[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the RFmx Demod Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | ref int[] | Contains the value of the specified attribute ID. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getattributestring__string-int-out.html language=enus -->
## TOPIC 00031: GetAttributeString(string, int, out string)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getattributestring__string-int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getattributestring__string-int-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of a of an RFmx string. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAttributeString(string selectorString, int attributeIdentifier, out string value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being read. Refer to

### GetAttributeString(string, int, out string)

Gets the value of a of an RFmx string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAttributeString(string selectorString, int attributeIdentifier, out string value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx PULSE Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | out string | Upon return, contains a value of the specified attribute ID. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getautolevelinitialreferencelevel__string-out.html language=enus -->
## TOPIC 00032: GetAutoLevelInitialReferenceLevel(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getautolevelinitialreferencelevel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getautolevelinitialreferencelevel__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the initial reference level, in dBm, which the AutoLevel(string, double, double, out double) function uses to estimate the peak power of the input signal. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAutoLevelInitialReferenceLevel(string selectorString, out double value)Remark

### GetAutoLevelInitialReferenceLevel(string, out double)

Gets the initial reference level, in dBm, which the [AutoLevel(string, double, double, out double)](nationalinstruments-rfmx-pulsemx-rfmxpulsemx-autolevel__string-double-double-out.html) function uses to estimate the peak power of the input signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAutoLevelInitialReferenceLevel(string selectorString, out double value)

#### Remarks

This method gets the value of [AutoLevelInitialReferenceLevel](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 30.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the initial reference level, in dBm, which the AutoLevel(string, double, double, out double) function uses to estimate the peak power of the input signal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getcenterfrequency__string-out.html language=enus -->
## TOPIC 00033: GetCenterFrequency(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getcenterfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getcenterfrequency__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetCenterFrequency(string selectorString, out double value)RemarksThis method gets the value of Cente

### GetCenterFrequency(string, out double)

Gets the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetCenterFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [CenterFrequency](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default of this property is hardware dependent.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getdigitaledgetriggeredge__string-out.html language=enus -->
## TOPIC 00034: GetDigitalEdgeTriggerEdge(string, out RFmxPulseMXDigitalEdgeTriggerEdge)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getdigitaledgetriggeredge__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getdigitaledgetriggeredge__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the active edge for the trigger. This method is used only when you set the TriggerType method to DigitalEdge. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetDigitalEdgeTriggerEdge(string selectorString, out RFmxPulseMXDigitalEdgeTriggerEdge value)RemarksThis method gets the valu

### GetDigitalEdgeTriggerEdge(string, out RFmxPulseMXDigitalEdgeTriggerEdge)

Gets the active edge for the trigger. This method is used only when you set the [TriggerType](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [DigitalEdge](nationalinstruments-rfmx-pulsemx-rfmxpulsemxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetDigitalEdgeTriggerEdge(string selectorString, out RFmxPulseMXDigitalEdgeTriggerEdge value)

#### Remarks

This method gets the value of [DigitalEdgeTriggerEdge](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [Rising](nationalinstruments-rfmx-pulsemx-rfmxpulsemxdigitaledgetriggeredge.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXDigitalEdgeTriggerEdge | Upon return, contains the active edge for the trigger. This method is used only when you set the TriggerType method to DigitalEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getdigitaledgetriggersource__string-out.html language=enus -->
## TOPIC 00035: GetDigitalEdgeTriggerSource(string, out string)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getdigitaledgetriggersource__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getdigitaledgetriggersource__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal for the digital edge trigger. This method is used only when you set the TriggerType method to DigitalEdge. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetDigitalEdgeTriggerSource(string selectorString, out string value)RemarksThis method gets the value of Dig

### GetDigitalEdgeTriggerSource(string, out string)

Gets the source terminal for the digital edge trigger. This method is used only when you set the [TriggerType](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [DigitalEdge](nationalinstruments-rfmx-pulsemx-rfmxpulsemxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetDigitalEdgeTriggerSource(string selectorString, out string value)

#### Remarks

This method gets the value of [DigitalEdgeTriggerSource](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default of this property is hardware dependent.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out string | Upon return, contains the source terminal for the digital edge trigger. This method is used only when you set the TriggerType method to DigitalEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-geterror__out-out.html language=enus -->
## TOPIC 00036: GetError(out int, out string)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-geterror__out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-geterror__out-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the latest error code and description. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetError(out int errorCode, out string errorDescription)ParametersNameTypeDescriptionerrorCodeout intUpon return, contains the latest error code.errorDescriptionout stringUpon return, contains the

### GetError(out int, out string)

Gets the latest error code and description.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetError(out int errorCode, out string errorDescription)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| errorCode | out int | Upon return, contains the latest error code. |
| errorDescription | out string | Upon return, contains the latest error description. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-geterrorstring__int-out.html language=enus -->
## TOPIC 00037: GetErrorString(int, out string)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-geterrorstring__int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-geterrorstring__int-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the status code returned by an RFmxPULSE function into a string. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetErrorString(int errorCode, out string errorDescription)ParametersNameTypeDescriptionerrorCodeintSpecifies an error or warning code.errorDescriptionout stringUpon r

### GetErrorString(int, out string)

Converts the status code returned by an RFmxPULSE function into a string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetErrorString(int errorCode, out string errorDescription)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| errorCode | int | Specifies an error or warning code. |
| errorDescription | out string | Upon return, contains the error description. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getexternalattenuation__string-out.html language=enus -->
## TOPIC 00038: GetExternalAttenuation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getexternalattenuation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getexternalattenuation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. SyntaxNamespace: Na

### GetExternalAttenuation(string, out double)

Gets the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the *NI RF Vector Signal Analyzers Help*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetExternalAttenuation(string selectorString, out double value)

#### Remarks

This method gets the value of [ExternalAttenuation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getiqpoweredgetriggerlevel__string-out.html language=enus -->
## TOPIC 00039: GetIQPowerEdgeTriggerLevel(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getiqpoweredgetriggerlevel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getiqpoweredgetriggerlevel__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power level at which the device triggers. This value is expressed in dB when you set the IQPowerEdgeTriggerLevelType method to Relative and in dBm when you set the IQ Power Edge Level Type method to Absolute. The device asserts the trigger when the signal exceeds the level specified by the

### GetIQPowerEdgeTriggerLevel(string, out double)

Gets the power level at which the device triggers. This value is expressed in dB when you set the [IQPowerEdgeTriggerLevelType](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [Relative](nationalinstruments-rfmx-pulsemx-rfmxpulsemxiqpoweredgetriggerleveltype.html) and in dBm when you set the IQ Power Edge Level Type method to [Absolute](nationalinstruments-rfmx-pulsemx-rfmxpulsemxiqpoweredgetriggerleveltype.html). The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the [TriggerType](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [IQPowerEdge](nationalinstruments-rfmx-pulsemx-rfmxpulsemxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetIQPowerEdgeTriggerLevel(string selectorString, out double value)

#### Remarks

This method gets the value of [IQPowerEdgeTriggerLevel](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default of this property is hardware dependent.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the power level at which the device triggers. This value is expressed in dB when you set the IQPowerEdgeTriggerLevelType method to Relative and in dBm when you set the IQ Power Edge Level Type method to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the TriggerType method to IQPowerEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getiqpoweredgetriggerleveltype__string-out.html language=enus -->
## TOPIC 00040: GetIQPowerEdgeTriggerLevelType(string, out RFmxPulseMXIQPowerEdgeTriggerLevelType)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getiqpoweredgetriggerleveltype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getiqpoweredgetriggerleveltype__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the reference for the IQPowerEdgeTriggerLevel method. The IQ Power Edge Level Type method is used only when you set the TriggerType method to IQPowerEdge. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetIQPowerEdgeTriggerLevelType(string selectorString, out RFmxPulseMXIQPowerEdge

### GetIQPowerEdgeTriggerLevelType(string, out RFmxPulseMXIQPowerEdgeTriggerLevelType)

Gets the reference for the [IQPowerEdgeTriggerLevel](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method. The IQ Power Edge Level Type method is used only when you set the [TriggerType](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [IQPowerEdge](nationalinstruments-rfmx-pulsemx-rfmxpulsemxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetIQPowerEdgeTriggerLevelType(string selectorString, out RFmxPulseMXIQPowerEdgeTriggerLevelType value)

#### Remarks

This method gets the value of [IQPowerEdgeTriggerLevelType](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [Absolute](nationalinstruments-rfmx-pulsemx-rfmxpulsemxiqpoweredgetriggerleveltype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXIQPowerEdgeTriggerLevelType | Upon return, contains the reference for the IQPowerEdgeTriggerLevel method. The IQ Power Edge Level Type method is used only when you set the TriggerType method to IQPowerEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getiqpoweredgetriggerslope__string-out.html language=enus -->
## TOPIC 00041: GetIQPowerEdgeTriggerSlope(string, out RFmxPulseMXIQPowerEdgeTriggerSlope)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getiqpoweredgetriggerslope__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getiqpoweredgetriggerslope__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the IQPowerEdgeTriggerLevel method with the slope you specify. This method is used only when you set the Trigg

### GetIQPowerEdgeTriggerSlope(string, out RFmxPulseMXIQPowerEdgeTriggerSlope)

Gets whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the [IQPowerEdgeTriggerLevel](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method with the slope you specify. This method is used only when you set the [TriggerType](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [IQPowerEdge](nationalinstruments-rfmx-pulsemx-rfmxpulsemxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetIQPowerEdgeTriggerSlope(string selectorString, out RFmxPulseMXIQPowerEdgeTriggerSlope value)

#### Remarks

This method gets the value of [IQPowerEdgeTriggerSlope](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [Rising](nationalinstruments-rfmx-pulsemx-rfmxpulsemxiqpoweredgetriggerslope.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXIQPowerEdgeTriggerSlope | Upon return, contains whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the IQPowerEdgeTriggerLevel method with the slope you specify. This method is used only when you set the TriggerType method to IQPowerEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getiqpoweredgetriggersource__string-out.html language=enus -->
## TOPIC 00042: GetIQPowerEdgeTriggerSource(string, out string)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getiqpoweredgetriggersource__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getiqpoweredgetriggersource__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the channel from which the device monitors the trigger. This method is used only when you set the TriggerType method to IQPowerEdge. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetIQPowerEdgeTriggerSource(string selectorString, out string value)RemarksThis method gets the value

### GetIQPowerEdgeTriggerSource(string, out string)

Gets the channel from which the device monitors the trigger. This method is used only when you set the [TriggerType](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [IQPowerEdge](nationalinstruments-rfmx-pulsemx-rfmxpulsemxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetIQPowerEdgeTriggerSource(string selectorString, out string value)

#### Remarks

This method gets the value of [IQPowerEdgeTriggerSource](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default of this property is hardware dependent.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out string | Upon return, contains the channel from which the device monitors the trigger. This method is used only when you set the TriggerType method to IQPowerEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getmaximumpulsecount__string-out.html language=enus -->
## TOPIC 00043: GetMaximumPulseCount(string, out int)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getmaximumpulsecount__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getmaximumpulsecount__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum number of pulses to be measured when you set the MaximumPulseCountEnabled method to True. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetMaximumPulseCount(string selectorString, out int value)RemarksThis method gets the value of MaximumPulseCount attribute.The defaul

### GetMaximumPulseCount(string, out int)

Gets the maximum number of pulses to be measured when you set the [MaximumPulseCountEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [True](nationalinstruments-rfmx-pulsemx-rfmxpulsemxmaximumpulsecountenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetMaximumPulseCount(string selectorString, out int value)

#### Remarks

This method gets the value of [MaximumPulseCount](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 100. Valid values are 1 to 10000, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the maximum number of pulses to be measured when you set the MaximumPulseCountEnabled method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getmaximumpulsecountenabled__string-out.html language=enus -->
## TOPIC 00044: GetMaximumPulseCountEnabled(string, out RFmxPulseMXMaximumPulseCountEnabled)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getmaximumpulsecountenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getmaximumpulsecountenabled__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the maximum pulse count for pulse measurements.You must configure this method when you set the SegmentedAcquisitionEnabled method to False. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetMaximumPulseCountEnabled(string selectorString, out RFmxPulseMXMaximumPuls

### GetMaximumPulseCountEnabled(string, out RFmxPulseMXMaximumPulseCountEnabled)

Gets whether to enable the maximum pulse count for pulse measurements.You must configure this method when you set the [SegmentedAcquisitionEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [False](nationalinstruments-rfmx-pulsemx-rfmxpulsemxmaximumpulsecountenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetMaximumPulseCountEnabled(string selectorString, out RFmxPulseMXMaximumPulseCountEnabled value)

#### Remarks

This method gets the value of [MaximumPulseCountEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-pulsemx-rfmxpulsemxmaximumpulsecountenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXMaximumPulseCountEnabled | Upon return, contains whether to enable the maximum pulse count for pulse measurements.You must configure this method when you set the SegmentedAcquisitionEnabled method to False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getmeasurementbandwidth__string-out.html language=enus -->
## TOPIC 00045: GetMeasurementBandwidth(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getmeasurementbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getmeasurementbandwidth__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the bandwidth of the filter used for the required sample rate. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetMeasurementBandwidth(string selectorString, out double value)RemarksThis method gets the value of MeasurementBandwidth attribute.The defau

### GetMeasurementBandwidth(string, out double)

Gets the bandwidth of the filter used for the required sample rate. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetMeasurementBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [MeasurementBandwidth](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 80 MHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the bandwidth of the filter used for the required sample rate. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getmeasurementfiltertype__string-out.html language=enus -->
## TOPIC 00046: GetMeasurementFilterType(string, out RFmxPulseMXMeasurementFilterType)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getmeasurementfiltertype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getmeasurementfiltertype__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the demodulation filter type to be used in the measurements. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetMeasurementFilterType(string selectorString, out RFmxPulseMXMeasurementFilterType value)RemarksThis method gets the value of MeasurementFilterType attribute.The default va

### GetMeasurementFilterType(string, out RFmxPulseMXMeasurementFilterType)

Gets the demodulation filter type to be used in the measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetMeasurementFilterType(string selectorString, out RFmxPulseMXMeasurementFilterType value)

#### Remarks

This method gets the value of [MeasurementFilterType](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [Gaussian](nationalinstruments-rfmx-pulsemx-rfmxpulsemxmeasurementfiltertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXMeasurementFilterType | Upon return, contains the demodulation filter type to be used in the measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getnumberofsegments__string-out.html language=enus -->
## TOPIC 00047: GetNumberOfSegments(string, out int)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getnumberofsegments__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getnumberofsegments__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of segments to acquire when you set the SegmentedAcquisitionEnabled method to True. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetNumberOfSegments(string selectorString, out int value)RemarksThis method gets the value of NumberOfSegments attribute.The default value i

### GetNumberOfSegments(string, out int)

Gets the number of segments to acquire when you set the [SegmentedAcquisitionEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [True](nationalinstruments-rfmx-pulsemx-rfmxpulsemxsegmentedacquisitionenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetNumberOfSegments(string selectorString, out int value)

#### Remarks

This method gets the value of [NumberOfSegments](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 1. Valid values are 1 to 10000, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of segments to acquire when you set the SegmentedAcquisitionEnabled method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getreferencelevel__string-out.html language=enus -->
## TOPIC 00048: GetReferenceLevel(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getreferencelevel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getreferencelevel__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetReferenceLevel(string selectorString, out double value)RemarksThis

### GetReferenceLevel(string, out double)

Gets the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetReferenceLevel(string selectorString, out double value)

#### Remarks

This method gets the value of [ReferenceLevel](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default of this property is hardware dependent.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getreferencelevelheadroom__string-out.html language=enus -->
## TOPIC 00049: GetReferenceLevelHeadroom(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getreferencelevelheadroom__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getreferencelevelheadroom__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the margin RFmx adds to the ReferenceLevel method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetReferenceLevelHeadroom(string selectorString, out double value)RemarksTh

### GetReferenceLevelHeadroom(string, out double)

Gets the margin RFmx adds to the [ReferenceLevel](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetReferenceLevelHeadroom(string selectorString, out double value)

#### Remarks

This method gets the value of [ReferenceLevelHeadroom](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.Default values PXIe-5668: 6 dB, PXIe-5830/5831/5832/5841/5842/5860: 1 dB, PXIe-5840: 0 dB

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the margin RFmx adds to the ReferenceLevel method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getresultfetchtimeout__string-out.html language=enus -->
## TOPIC 00050: GetResultFetchTimeout(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getresultfetchtimeout__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getresultfetchtimeout__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the wait time before results are available in the PropertyNode. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxPulse Property Node waits until the measurement is complete. SyntaxNamespace: Nati

### GetResultFetchTimeout(string, out double)

Gets the wait time before results are available in the PropertyNode. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxPulse Property Node waits until the measurement is complete.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetResultFetchTimeout(string selectorString, out double value)

#### Remarks

This method gets the value of [ResultFetchTimeout](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the wait time before results are available in the RFmx Property. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxPulse Property Node waits until the measurement is complete. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getsegmentacquisitionlength__string-out.html language=enus -->
## TOPIC 00051: GetSegmentAcquisitionLength(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getsegmentacquisitionlength__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getsegmentacquisitionlength__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the acquisition length for the pulse measurement when you set the SegmentedAcquisitionEnabled method to True. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetSegmentAcquisitionLength(string selectorString, out double value)RemarksThis method ge

### GetSegmentAcquisitionLength(string, out double)

Gets the acquisition length for the pulse measurement when you set the [SegmentedAcquisitionEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [True](nationalinstruments-rfmx-pulsemx-rfmxpulsemxsegmentedacquisitionenabled.html). This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetSegmentAcquisitionLength(string selectorString, out double value)

#### Remarks

This method gets the value of [SegmentAcquisitionLength](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.00001 seconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the acquisition length for the pulse measurement when you set the SegmentedAcquisitionEnabled method to True. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getsegmentedacquisitionenabled__string-out.html language=enus -->
## TOPIC 00052: GetSegmentedAcquisitionEnabled(string, out RFmxPulseMXSegmentedAcquisitionEnabled)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getsegmentedacquisitionenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getsegmentedacquisitionenabled__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable Segmented Acquisition. This mode is best applied when the pulses are sparsely spaced. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetSegmentedAcquisitionEnabled(string selectorString, out RFmxPulseMXSegmentedAcquisitionEnabled value)RemarksThis method gets the

### GetSegmentedAcquisitionEnabled(string, out RFmxPulseMXSegmentedAcquisitionEnabled)

Gets whether to enable Segmented Acquisition. This mode is best applied when the pulses are sparsely spaced.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetSegmentedAcquisitionEnabled(string selectorString, out RFmxPulseMXSegmentedAcquisitionEnabled value)

#### Remarks

This method gets the value of [SegmentedAcquisitionEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-pulsemx-rfmxpulsemxsegmentedacquisitionenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXSegmentedAcquisitionEnabled | Upon return, contains whether to enable Segmented Acquisition. This mode is best applied when the pulses are sparsely spaced. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getselectedports__string-out.html language=enus -->
## TOPIC 00053: GetSelectedPorts(string, out string)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getselectedports__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getselectedports__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetSelectedPorts(string selectorString, out string value)RemarksThis method gets the value of SelectedPorts

### GetSelectedPorts(string, out string)

Gets the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetSelectedPorts(string selectorString, out string value)

#### Remarks

This method gets the value of [SelectedPorts](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.Default valuesPXIe-5830/5831/5832if1Other devices"" (empty string)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out string | Upon return, contains the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-gettriggerdelay__string-out.html language=enus -->
## TOPIC 00054: GetTriggerDelay(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-gettriggerdelay__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-gettriggerdelay__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the trigger delay time. This value is expressed in seconds.If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTriggerDelay(string selectorS

### GetTriggerDelay(string, out double)

Gets the trigger delay time. This value is expressed in seconds.If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTriggerDelay(string selectorString, out double value)

#### Remarks

This method gets the value of [TriggerDelay](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the trigger delay time. This value is expressed in seconds.If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-gettriggerminimumquiettimeduration__string-out.html language=enus -->
## TOPIC 00055: GetTriggerMinimumQuietTimeDuration(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-gettriggerminimumquiettimeduration__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-gettriggerminimumquiettimeduration__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the IQPowerEdgeTriggerSlope method to Rising, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope method to

### GetTriggerMinimumQuietTimeDuration(string, out double)

Gets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the [IQPowerEdgeTriggerSlope](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [Rising](nationalinstruments-rfmx-pulsemx-rfmxpulsemxiqpoweredgetriggerslope.html), the signal is quiet below the trigger level. If you set the IQ Power Edge Slope method to [Falling](nationalinstruments-rfmx-pulsemx-rfmxpulsemxiqpoweredgetriggerslope.html), the signal is quiet above the trigger level.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTriggerMinimumQuietTimeDuration(string selectorString, out double value)

#### Remarks

This method gets the value of [TriggerMinimumQuietTimeDuration](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default of this property is hardware dependent.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the IQPowerEdgeTriggerSlope method to Rising, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope method to Falling, the signal is quiet above the trigger level. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-gettriggerminimumquiettimemode__string-out.html language=enus -->
## TOPIC 00056: GetTriggerMinimumQuietTimeMode(string, out RFmxPulseMXTriggerMinimumQuietTimeMode)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-gettriggerminimumquiettimemode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-gettriggerminimumquiettimemode__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement computes the minimum quiet time used for triggering. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTriggerMinimumQuietTimeMode(string selectorString, out RFmxPulseMXTriggerMinimumQuietTimeMode value)RemarksThis method gets the value of TriggerMinimumQuie

### GetTriggerMinimumQuietTimeMode(string, out RFmxPulseMXTriggerMinimumQuietTimeMode)

Gets whether the measurement computes the minimum quiet time used for triggering.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTriggerMinimumQuietTimeMode(string selectorString, out RFmxPulseMXTriggerMinimumQuietTimeMode value)

#### Remarks

This method gets the value of [TriggerMinimumQuietTimeMode](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [Manual](nationalinstruments-rfmx-pulsemx-rfmxpulsemxtriggerminimumquiettimemode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXTriggerMinimumQuietTimeMode | Upon return, contains whether the measurement computes the minimum quiet time used for triggering. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-gettriggertype__string-out.html language=enus -->
## TOPIC 00057: GetTriggerType(string, out RFmxPulseMXTriggerType)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-gettriggertype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-gettriggertype__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the trigger type. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTriggerType(string selectorString, out RFmxPulseMXTriggerType value)RemarksThis method gets the value of TriggerType attribute.The default value is None.ParametersNameTypeDescriptionselectorStringstringPass an empt

### GetTriggerType(string, out RFmxPulseMXTriggerType)

Gets the trigger type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTriggerType(string selectorString, out RFmxPulseMXTriggerType value)

#### Remarks

This method gets the value of [TriggerType](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [None](nationalinstruments-rfmx-pulsemx-rfmxpulsemxtriggertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXTriggerType | Upon return, contains the trigger type. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getwarning__out-out.html language=enus -->
## TOPIC 00058: GetWarning(out int, out string)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getwarning__out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-getwarning__out-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the latest warning code and description. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetWarning(out int warningCode, out string warningDescription)ParametersNameTypeDescriptionwarningCodeout intUpon return, contains the latest warning code.warningDescriptionout stringUpon return

### GetWarning(out int, out string)

Gets the latest warning code and description.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetWarning(out int warningCode, out string warningDescription)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| warningCode | out int | Upon return, contains the latest warning code. |
| warningDescription | out string | Upon return, contains the latest warning description. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-initiate__string-string.html language=enus -->
## TOPIC 00059: Initiate(string, string)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-initiate__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-initiate__string-string.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates all enabled measurements. Call this method after configuring the signal and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch methods or result methods in the meth

### Initiate(string, string)

Initiates all enabled measurements. Call this method after configuring the signal and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch methods or result methods in the method node. To get the status of measurements, use the RF [WaitForMeasurementComplete(string, double)](nationalinstruments-rfmx-pulsemx-rfmxpulsemx-waitformeasurementcomplete__string-double.html) method or [CheckMeasurementStatus(string, out bool)](nationalinstruments-rfmx-pulsemx-rfmxpulsemx-checkmeasurementstatus__string-out.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int Initiate(string selectorString, string resultName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the result name in this parameter, either the result name specified by the resultName parameter or the default result instance is used. Example:"""""result::r1" |
| resultName | string | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"""result::r1""r1" |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-isdisposed.html language=enus -->
## TOPIC 00060: IsDisposed

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-isdisposed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-isdisposed.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates whether the signal has been disposed. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic bool IsDisposed { get; }Remarkstrue if the session is disposed; otherwise, false.

### IsDisposed

Gets a value that indicates whether the signal has been disposed.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public bool IsDisposed { get; }

#### Remarks

true if the session is disposed; otherwise, false.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-pulse.html language=enus -->
## TOPIC 00061: Pulse

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-pulse.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-pulse.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxPulseMXPulse instance that represents the Pulse measurement. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic RFmxPulseMXPulse Pulse { get; }

### Pulse

Gets the [RFmxPulseMXPulse](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulse.html) instance that represents the Pulse measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public [RFmxPulseMXPulse](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulse.html) Pulse { get; }

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-resetattribute__string-rfmxpulsemxpropertyid.html language=enus -->
## TOPIC 00062: ResetAttribute(string, RFmxPulseMXPropertyId)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-resetattribute__string-rfmxpulsemxpropertyid.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-resetattribute__string-rfmxpulsemxpropertyid.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the attribute to its default value. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int ResetAttribute(string selectorString, RFmxPulseMXPropertyId attributeId)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the property being reset. Refer to the Usi

### ResetAttribute(string, RFmxPulseMXPropertyId)

Resets the attribute to its default value.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int ResetAttribute(string selectorString, RFmxPulseMXPropertyId attributeId)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the property being reset. Refer to the Using a Selector String (.NET) topic in the NI-RFmx PULSE Help for more information about configuring the selector string. |
| attributeId | RFmxPulseMXPropertyId | Specifies an attribute identifier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-resettodefault__string.html language=enus -->
## TOPIC 00063: ResetToDefault(string)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-resettodefault__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-resettodefault__string.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a signal to the default values.SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int ResetToDefault(string selectorString)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when creating the signal configuration is used.ReturnsReturns t

### ResetToDefault(string)

Resets a signal to the default values.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int ResetToDefault(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-selectmeasurements__string-rfmxpulsemxmeasurementtypes-bool.html language=enus -->
## TOPIC 00064: SelectMeasurements(string, RFmxPulseMXMeasurementTypes, bool)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-selectmeasurements__string-rfmxpulsemxmeasurementtypes-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-selectmeasurements__string-rfmxpulsemxmeasurementtypes-bool.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurements that you want to enable. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SelectMeasurements(string selectorString, RFmxPulseMXMeasurementTypes measurement, bool enableAllTraces)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal na

### SelectMeasurements(string, RFmxPulseMXMeasurementTypes, bool)

Specifies the measurements that you want to enable.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SelectMeasurements(string selectorString, RFmxPulseMXMeasurementTypes measurement, bool enableAllTraces)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| measurement | RFmxPulseMXMeasurementTypes | Specifies the measurement to perform. |
| enableAllTraces | bool | True to enable all traces for the selected measurement; otherwise False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-sendsoftwareedgetrigger.html language=enus -->
## TOPIC 00065: SendSoftwareEdgeTrigger()

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-sendsoftwareedgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-sendsoftwareedgetrigger.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a trigger to the device when you use the ConfigureSoftwareEdgeTrigger(string, double, bool) method to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this method to override a hardware trigger.SyntaxNamespace: NationalInstruments.RF

### SendSoftwareEdgeTrigger()

Sends a trigger to the device when you use the [ConfigureSoftwareEdgeTrigger(string, double, bool)](nationalinstruments-rfmx-pulsemx-rfmxpulsemx-configuresoftwareedgetrigger__string-double-bool.html) method to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this method to override a hardware trigger.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SendSoftwareEdgeTrigger()

#### Remarks

- You configure an invalid trigger.
- You have not previously called the [Initiate(string, string)](nationalinstruments-rfmx-pulsemx-rfmxpulsemx-initiate__string-string.html) method.

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setacquisitionlength__string-double.html language=enus -->
## TOPIC 00066: SetAcquisitionLength(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setacquisitionlength__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setacquisitionlength__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the acquisition length for the pulse measurement. This value is expressed in seconds.You configure this method when you set the SegmentedAcquisitionEnabled method to False. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetAcquisitionLength(string selectorString, double value)Remar

### SetAcquisitionLength(string, double)

Sets the acquisition length for the pulse measurement. This value is expressed in seconds.You configure this method when you set the [SegmentedAcquisitionEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [False](nationalinstruments-rfmx-pulsemx-rfmxpulsemxsegmentedacquisitionenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetAcquisitionLength(string selectorString, double value)

#### Remarks

This method sets the value of [AcquisitionLength](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.001 seconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the acquisition length for the pulse measurement. This value is expressed in seconds.You configure this method when you set the SegmentedAcquisitionEnabled method to False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setattributebool__string-int-bool.html language=enus -->
## TOPIC 00067: SetAttributeBool(string, int, bool)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setattributebool__string-int-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setattributebool__string-int-bool.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a Bool attribute. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetAttributeBool(string selectorString, int attributeIdentifier, bool value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being set. Refer to the Using a

### SetAttributeBool(string, int, bool)

Sets the value of a Bool attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetAttributeBool(string selectorString, int attributeIdentifier, bool value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx PULSE Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | bool | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setattributedouble__string-int-double.html language=enus -->
## TOPIC 00068: SetAttributeDouble(string, int, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setattributedouble__string-int-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setattributedouble__string-int-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a Double attribute. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetAttributeDouble(string selectorString, int attributeIdentifier, double value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being set. Refer to the U

### SetAttributeDouble(string, int, double)

Sets the value of a Double attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetAttributeDouble(string selectorString, int attributeIdentifier, double value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx PULSE Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | double | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setattributedoublearray__string-int-double_arr1.html language=enus -->
## TOPIC 00069: SetAttributeDoubleArray(string, int, double[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setattributedoublearray__string-int-double_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setattributedoublearray__string-int-double_arr1.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set the value of a double array attribute. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetAttributeDoubleArray(string selectorString, int attributeIdentifier, double[] value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being set. Re

### SetAttributeDoubleArray(string, int, double[])

Set the value of a double array attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetAttributeDoubleArray(string selectorString, int attributeIdentifier, double[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx Demod Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | double[] | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setattributeint__string-int-int.html language=enus -->
## TOPIC 00070: SetAttributeInt(string, int, int)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setattributeint__string-int-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setattributeint__string-int-int.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a Int attribute. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetAttributeInt(string selectorString, int attributeIdentifier, int value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being set. Refer to the Using a Se

### SetAttributeInt(string, int, int)

Sets the value of a Int attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetAttributeInt(string selectorString, int attributeIdentifier, int value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx PULSE Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | int | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setattributeintarray__string-int-int_arr1.html language=enus -->
## TOPIC 00071: SetAttributeIntArray(string, int, int[])

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setattributeintarray__string-int-int_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setattributeintarray__string-int-int_arr1.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set the value of a integer array attribute. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetAttributeIntArray(string selectorString, int attributeIdentifier, int[] value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being set. Refer t

### SetAttributeIntArray(string, int, int[])

Set the value of a integer array attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetAttributeIntArray(string selectorString, int attributeIdentifier, int[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the RFmx Demod Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | int[] | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setattributestring__string-int-string.html language=enus -->
## TOPIC 00072: SetAttributeString(string, int, string)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setattributestring__string-int-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setattributestring__string-int-string.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a String attribute. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetAttributeString(string selectorString, int attributeIdentifier, string value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being set. Refer to the U

### SetAttributeString(string, int, string)

Sets the value of a String attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetAttributeString(string selectorString, int attributeIdentifier, string value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx PULSE Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | string | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setautolevelinitialreferencelevel__string-double.html language=enus -->
## TOPIC 00073: SetAutoLevelInitialReferenceLevel(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setautolevelinitialreferencelevel__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setautolevelinitialreferencelevel__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the initial reference level, in dBm, which the AutoLevel(string, double, double, out double) function uses to estimate the peak power of the input signal. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetAutoLevelInitialReferenceLevel(string selectorString, double value)RemarksThi

### SetAutoLevelInitialReferenceLevel(string, double)

Sets the initial reference level, in dBm, which the [AutoLevel(string, double, double, out double)](nationalinstruments-rfmx-pulsemx-rfmxpulsemx-autolevel__string-double-double-out.html) function uses to estimate the peak power of the input signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetAutoLevelInitialReferenceLevel(string selectorString, double value)

#### Remarks

This method sets the value of [AutoLevelInitialReferenceLevel](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 30.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the initial reference level, in dBm, which the AutoLevel(string, double, double, out double) function uses to estimate the peak power of the input signal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setcenterfrequency__string-double.html language=enus -->
## TOPIC 00074: SetCenterFrequency(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setcenterfrequency__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setcenterfrequency__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetCenterFrequency(string selectorString, double value)RemarksThis method sets the value of CenterFre

### SetCenterFrequency(string, double)

Sets the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetCenterFrequency(string selectorString, double value)

#### Remarks

This method sets the value of [CenterFrequency](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default of this property is hardware dependent.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setdigitaledgetriggeredge__string-rfmxpulsemxdigitaledgetriggeredge.html language=enus -->
## TOPIC 00075: SetDigitalEdgeTriggerEdge(string, RFmxPulseMXDigitalEdgeTriggerEdge)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setdigitaledgetriggeredge__string-rfmxpulsemxdigitaledgetriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setdigitaledgetriggeredge__string-rfmxpulsemxdigitaledgetriggeredge.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the active edge for the trigger. This method is used only when you set the TriggerType method to DigitalEdge. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetDigitalEdgeTriggerEdge(string selectorString, RFmxPulseMXDigitalEdgeTriggerEdge value)RemarksThis method sets the value of

### SetDigitalEdgeTriggerEdge(string, RFmxPulseMXDigitalEdgeTriggerEdge)

Sets the active edge for the trigger. This method is used only when you set the [TriggerType](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [DigitalEdge](nationalinstruments-rfmx-pulsemx-rfmxpulsemxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetDigitalEdgeTriggerEdge(string selectorString, RFmxPulseMXDigitalEdgeTriggerEdge value)

#### Remarks

This method sets the value of [DigitalEdgeTriggerEdge](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [Rising](nationalinstruments-rfmx-pulsemx-rfmxpulsemxdigitaledgetriggeredge.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXDigitalEdgeTriggerEdge | Specifies the active edge for the trigger. This method is used only when you set the TriggerType method to DigitalEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setdigitaledgetriggersource__string-string.html language=enus -->
## TOPIC 00076: SetDigitalEdgeTriggerSource(string, string)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setdigitaledgetriggersource__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setdigitaledgetriggersource__string-string.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the source terminal for the digital edge trigger. This method is used only when you set the TriggerType method to DigitalEdge. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetDigitalEdgeTriggerSource(string selectorString, string value)RemarksThis method sets the value of Digital

### SetDigitalEdgeTriggerSource(string, string)

Sets the source terminal for the digital edge trigger. This method is used only when you set the [TriggerType](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [DigitalEdge](nationalinstruments-rfmx-pulsemx-rfmxpulsemxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetDigitalEdgeTriggerSource(string selectorString, string value)

#### Remarks

This method sets the value of [DigitalEdgeTriggerSource](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default of this property is hardware dependent.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | string | Specifies the source terminal for the digital edge trigger. This method is used only when you set the TriggerType method to DigitalEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setexternalattenuation__string-double.html language=enus -->
## TOPIC 00077: SetExternalAttenuation(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setexternalattenuation__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setexternalattenuation__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. SyntaxNamespace: Na

### SetExternalAttenuation(string, double)

Sets the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the *NI RF Vector Signal Analyzers Help*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetExternalAttenuation(string selectorString, double value)

#### Remarks

This method sets the value of [ExternalAttenuation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setiqpoweredgetriggerlevel__string-double.html language=enus -->
## TOPIC 00078: SetIQPowerEdgeTriggerLevel(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setiqpoweredgetriggerlevel__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setiqpoweredgetriggerlevel__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the power level at which the device triggers. This value is expressed in dB when you set the IQPowerEdgeTriggerLevelType method to Relative and in dBm when you set the IQ Power Edge Level Type method to Absolute. The device asserts the trigger when the signal exceeds the level specified by the

### SetIQPowerEdgeTriggerLevel(string, double)

Sets the power level at which the device triggers. This value is expressed in dB when you set the [IQPowerEdgeTriggerLevelType](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [Relative](nationalinstruments-rfmx-pulsemx-rfmxpulsemxiqpoweredgetriggerleveltype.html) and in dBm when you set the IQ Power Edge Level Type method to [Absolute](nationalinstruments-rfmx-pulsemx-rfmxpulsemxiqpoweredgetriggerleveltype.html). The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the [TriggerType](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [IQPowerEdge](nationalinstruments-rfmx-pulsemx-rfmxpulsemxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetIQPowerEdgeTriggerLevel(string selectorString, double value)

#### Remarks

This method sets the value of [IQPowerEdgeTriggerLevel](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default of this property is hardware dependent.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the power level at which the device triggers. This value is expressed in dB when you set the IQPowerEdgeTriggerLevelType method to Relative and in dBm when you set the IQ Power Edge Level Type method to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the TriggerType method to IQPowerEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setiqpoweredgetriggerleveltype__string-rfmxpulsemxiqpoweredgetriggerleveltype.html language=enus -->
## TOPIC 00079: SetIQPowerEdgeTriggerLevelType(string, RFmxPulseMXIQPowerEdgeTriggerLevelType)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setiqpoweredgetriggerleveltype__string-rfmxpulsemxiqpoweredgetriggerleveltype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setiqpoweredgetriggerleveltype__string-rfmxpulsemxiqpoweredgetriggerleveltype.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the reference for the IQPowerEdgeTriggerLevel method. The IQ Power Edge Level Type method is used only when you set the TriggerType method to IQPowerEdge. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetIQPowerEdgeTriggerLevelType(string selectorString, RFmxPulseMXIQPowerEdgeTrig

### SetIQPowerEdgeTriggerLevelType(string, RFmxPulseMXIQPowerEdgeTriggerLevelType)

Sets the reference for the [IQPowerEdgeTriggerLevel](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method. The IQ Power Edge Level Type method is used only when you set the [TriggerType](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [IQPowerEdge](nationalinstruments-rfmx-pulsemx-rfmxpulsemxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetIQPowerEdgeTriggerLevelType(string selectorString, RFmxPulseMXIQPowerEdgeTriggerLevelType value)

#### Remarks

This method sets the value of [IQPowerEdgeTriggerLevelType](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [Absolute](nationalinstruments-rfmx-pulsemx-rfmxpulsemxiqpoweredgetriggerleveltype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXIQPowerEdgeTriggerLevelType | Specifies the reference for the IQPowerEdgeTriggerLevel method. The IQ Power Edge Level Type method is used only when you set the TriggerType method to IQPowerEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setiqpoweredgetriggerslope__string-rfmxpulsemxiqpoweredgetriggerslope.html language=enus -->
## TOPIC 00080: SetIQPowerEdgeTriggerSlope(string, RFmxPulseMXIQPowerEdgeTriggerSlope)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setiqpoweredgetriggerslope__string-rfmxpulsemxiqpoweredgetriggerslope.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setiqpoweredgetriggerslope__string-rfmxpulsemxiqpoweredgetriggerslope.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the IQPowerEdgeTriggerLevel method with the slope you specify. This method is used only when you set the Trigg

### SetIQPowerEdgeTriggerSlope(string, RFmxPulseMXIQPowerEdgeTriggerSlope)

Sets whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the [IQPowerEdgeTriggerLevel](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method with the slope you specify. This method is used only when you set the [TriggerType](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [IQPowerEdge](nationalinstruments-rfmx-pulsemx-rfmxpulsemxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetIQPowerEdgeTriggerSlope(string selectorString, RFmxPulseMXIQPowerEdgeTriggerSlope value)

#### Remarks

This method sets the value of [IQPowerEdgeTriggerSlope](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [Rising](nationalinstruments-rfmx-pulsemx-rfmxpulsemxiqpoweredgetriggerslope.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXIQPowerEdgeTriggerSlope | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the IQPowerEdgeTriggerLevel method with the slope you specify. This method is used only when you set the TriggerType method to IQPowerEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setiqpoweredgetriggersource__string-string.html language=enus -->
## TOPIC 00081: SetIQPowerEdgeTriggerSource(string, string)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setiqpoweredgetriggersource__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setiqpoweredgetriggersource__string-string.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the channel from which the device monitors the trigger. This method is used only when you set the TriggerType method to IQPowerEdge. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetIQPowerEdgeTriggerSource(string selectorString, string value)RemarksThis method sets the value of I

### SetIQPowerEdgeTriggerSource(string, string)

Sets the channel from which the device monitors the trigger. This method is used only when you set the [TriggerType](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [IQPowerEdge](nationalinstruments-rfmx-pulsemx-rfmxpulsemxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetIQPowerEdgeTriggerSource(string selectorString, string value)

#### Remarks

This method sets the value of [IQPowerEdgeTriggerSource](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default of this property is hardware dependent.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | string | Specifies the channel from which the device monitors the trigger. This method is used only when you set the TriggerType method to IQPowerEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setmaximumpulsecount__string-int.html language=enus -->
## TOPIC 00082: SetMaximumPulseCount(string, int)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setmaximumpulsecount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setmaximumpulsecount__string-int.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the maximum number of pulses to be measured when you set the MaximumPulseCountEnabled method to True. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetMaximumPulseCount(string selectorString, int value)RemarksThis method sets the value of MaximumPulseCount attribute.The default va

### SetMaximumPulseCount(string, int)

Sets the maximum number of pulses to be measured when you set the [MaximumPulseCountEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [True](nationalinstruments-rfmx-pulsemx-rfmxpulsemxmaximumpulsecountenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetMaximumPulseCount(string selectorString, int value)

#### Remarks

This method sets the value of [MaximumPulseCount](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 100. Valid values are 1 to 10000, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the maximum number of pulses to be measured when you set the MaximumPulseCountEnabled method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setmaximumpulsecountenabled__string-rfmxpulsemxmaximumpulsecountenabled.html language=enus -->
## TOPIC 00083: SetMaximumPulseCountEnabled(string, RFmxPulseMXMaximumPulseCountEnabled)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setmaximumpulsecountenabled__string-rfmxpulsemxmaximumpulsecountenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setmaximumpulsecountenabled__string-rfmxpulsemxmaximumpulsecountenabled.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the maximum pulse count for pulse measurements.You must configure this method when you set the SegmentedAcquisitionEnabled method to False. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetMaximumPulseCountEnabled(string selectorString, RFmxPulseMXMaximumPulseCou

### SetMaximumPulseCountEnabled(string, RFmxPulseMXMaximumPulseCountEnabled)

Sets whether to enable the maximum pulse count for pulse measurements.You must configure this method when you set the [SegmentedAcquisitionEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [False](nationalinstruments-rfmx-pulsemx-rfmxpulsemxmaximumpulsecountenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetMaximumPulseCountEnabled(string selectorString, RFmxPulseMXMaximumPulseCountEnabled value)

#### Remarks

This method sets the value of [MaximumPulseCountEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-pulsemx-rfmxpulsemxmaximumpulsecountenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXMaximumPulseCountEnabled | Specifies whether to enable the maximum pulse count for pulse measurements.You must configure this method when you set the SegmentedAcquisitionEnabled method to False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setmeasurementbandwidth__string-double.html language=enus -->
## TOPIC 00084: SetMeasurementBandwidth(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setmeasurementbandwidth__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setmeasurementbandwidth__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the bandwidth of the filter used for the required sample rate. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetMeasurementBandwidth(string selectorString, double value)RemarksThis method sets the value of MeasurementBandwidth attribute.The default v

### SetMeasurementBandwidth(string, double)

Sets the bandwidth of the filter used for the required sample rate. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetMeasurementBandwidth(string selectorString, double value)

#### Remarks

This method sets the value of [MeasurementBandwidth](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 80 MHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the bandwidth of the filter used for the required sample rate. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setmeasurementfiltertype__string-rfmxpulsemxmeasurementfiltertype.html language=enus -->
## TOPIC 00085: SetMeasurementFilterType(string, RFmxPulseMXMeasurementFilterType)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setmeasurementfiltertype__string-rfmxpulsemxmeasurementfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setmeasurementfiltertype__string-rfmxpulsemxmeasurementfiltertype.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the demodulation filter type to be used in the measurements. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetMeasurementFilterType(string selectorString, RFmxPulseMXMeasurementFilterType value)RemarksThis method sets the value of MeasurementFilterType attribute.The default value

### SetMeasurementFilterType(string, RFmxPulseMXMeasurementFilterType)

Sets the demodulation filter type to be used in the measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetMeasurementFilterType(string selectorString, RFmxPulseMXMeasurementFilterType value)

#### Remarks

This method sets the value of [MeasurementFilterType](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [Gaussian](nationalinstruments-rfmx-pulsemx-rfmxpulsemxmeasurementfiltertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXMeasurementFilterType | Specifies the demodulation filter type to be used in the measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setnumberofsegments__string-int.html language=enus -->
## TOPIC 00086: SetNumberOfSegments(string, int)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setnumberofsegments__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setnumberofsegments__string-int.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of segments to acquire when you set the SegmentedAcquisitionEnabled method to True. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetNumberOfSegments(string selectorString, int value)RemarksThis method sets the value of NumberOfSegments attribute.The default value is 1.

### SetNumberOfSegments(string, int)

Sets the number of segments to acquire when you set the [SegmentedAcquisitionEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [True](nationalinstruments-rfmx-pulsemx-rfmxpulsemxsegmentedacquisitionenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetNumberOfSegments(string selectorString, int value)

#### Remarks

This method sets the value of [NumberOfSegments](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 1. Valid values are 1 to 10000, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of segments to acquire when you set the SegmentedAcquisitionEnabled method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setreferencelevel__string-double.html language=enus -->
## TOPIC 00087: SetReferenceLevel(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setreferencelevel__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setreferencelevel__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetReferenceLevel(string selectorString, double value)RemarksThis met

### SetReferenceLevel(string, double)

Sets the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetReferenceLevel(string selectorString, double value)

#### Remarks

This method sets the value of [ReferenceLevel](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default of this property is hardware dependent.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setreferencelevelheadroom__string-double.html language=enus -->
## TOPIC 00088: SetReferenceLevelHeadroom(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setreferencelevelheadroom__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setreferencelevelheadroom__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the margin RFmx adds to the ReferenceLevel method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetReferenceLevelHeadroom(string selectorString, double value)RemarksThis m

### SetReferenceLevelHeadroom(string, double)

Sets the margin RFmx adds to the [ReferenceLevel](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetReferenceLevelHeadroom(string selectorString, double value)

#### Remarks

This method sets the value of [ReferenceLevelHeadroom](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.Default values PXIe-5668: 6 dB, PXIe-5830/5831/5832/5841/5842/5860: 1 dB, PXIe-5840: 0 dB

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the margin RFmx adds to the ReferenceLevel method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setresultfetchtimeout__string-double.html language=enus -->
## TOPIC 00089: SetResultFetchTimeout(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setresultfetchtimeout__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setresultfetchtimeout__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the wait time before results are available in the RFmx Property. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxPulse Property Node waits until the measurement is complete. SyntaxNamespace: Nat

### SetResultFetchTimeout(string, double)

Sets the wait time before results are available in the RFmx Property. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxPulse Property Node waits until the measurement is complete.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetResultFetchTimeout(string selectorString, double value)

#### Remarks

This method sets the value of [ResultFetchTimeout](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the wait time before results are available in the RFmx Property. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxPulse Property Node waits until the measurement is complete. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setsegmentacquisitionlength__string-double.html language=enus -->
## TOPIC 00090: SetSegmentAcquisitionLength(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setsegmentacquisitionlength__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setsegmentacquisitionlength__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the acquisition length for the pulse measurement when you set the SegmentedAcquisitionEnabled method to True. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetSegmentAcquisitionLength(string selectorString, double value)RemarksThis method sets t

### SetSegmentAcquisitionLength(string, double)

Sets the acquisition length for the pulse measurement when you set the [SegmentedAcquisitionEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [True](nationalinstruments-rfmx-pulsemx-rfmxpulsemxsegmentedacquisitionenabled.html). This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetSegmentAcquisitionLength(string selectorString, double value)

#### Remarks

This method sets the value of [SegmentAcquisitionLength](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.00001 seconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the acquisition length for the pulse measurement when you set the SegmentedAcquisitionEnabled method to True. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setsegmentedacquisitionenabled__string-rfmxpulsemxsegmentedacquisitionenabled.html language=enus -->
## TOPIC 00091: SetSegmentedAcquisitionEnabled(string, RFmxPulseMXSegmentedAcquisitionEnabled)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setsegmentedacquisitionenabled__string-rfmxpulsemxsegmentedacquisitionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setsegmentedacquisitionenabled__string-rfmxpulsemxsegmentedacquisitionenabled.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable Segmented Acquisition. This mode is best applied when the pulses are sparsely spaced. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetSegmentedAcquisitionEnabled(string selectorString, RFmxPulseMXSegmentedAcquisitionEnabled value)RemarksThis method sets the valu

### SetSegmentedAcquisitionEnabled(string, RFmxPulseMXSegmentedAcquisitionEnabled)

Sets whether to enable Segmented Acquisition. This mode is best applied when the pulses are sparsely spaced.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetSegmentedAcquisitionEnabled(string selectorString, RFmxPulseMXSegmentedAcquisitionEnabled value)

#### Remarks

This method sets the value of [SegmentedAcquisitionEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-pulsemx-rfmxpulsemxsegmentedacquisitionenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXSegmentedAcquisitionEnabled | Specifies whether to enable Segmented Acquisition. This mode is best applied when the pulses are sparsely spaced. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setselectedports__string-string.html language=enus -->
## TOPIC 00092: SetSelectedPorts(string, string)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setselectedports__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-setselectedports__string-string.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetSelectedPorts(string selectorString, string value)RemarksThis method sets the value of SelectedPorts att

### SetSelectedPorts(string, string)

Sets the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetSelectedPorts(string selectorString, string value)

#### Remarks

This method sets the value of [SelectedPorts](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.Default valuesPXIe-5830/5831/5832if1Other devices"" (empty string)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | string | Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-settriggerdelay__string-double.html language=enus -->
## TOPIC 00093: SetTriggerDelay(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-settriggerdelay__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-settriggerdelay__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the trigger delay time. This value is expressed in seconds.If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetTriggerDelay(string selectorS

### SetTriggerDelay(string, double)

Sets the trigger delay time. This value is expressed in seconds.If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetTriggerDelay(string selectorString, double value)

#### Remarks

This method sets the value of [TriggerDelay](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the trigger delay time. This value is expressed in seconds.If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-settriggerminimumquiettimeduration__string-double.html language=enus -->
## TOPIC 00094: SetTriggerMinimumQuietTimeDuration(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-settriggerminimumquiettimeduration__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-settriggerminimumquiettimeduration__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the IQPowerEdgeTriggerSlope method to Rising, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope method to

### SetTriggerMinimumQuietTimeDuration(string, double)

Sets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the [IQPowerEdgeTriggerSlope](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [Rising](nationalinstruments-rfmx-pulsemx-rfmxpulsemxiqpoweredgetriggerslope.html), the signal is quiet below the trigger level. If you set the IQ Power Edge Slope method to [Falling](nationalinstruments-rfmx-pulsemx-rfmxpulsemxiqpoweredgetriggerslope.html), the signal is quiet above the trigger level.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetTriggerMinimumQuietTimeDuration(string selectorString, double value)

#### Remarks

This method sets the value of [TriggerMinimumQuietTimeDuration](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default of this property is hardware dependent.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the IQPowerEdgeTriggerSlope method to Rising, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope method to Falling, the signal is quiet above the trigger level. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-settriggerminimumquiettimemode__string-rfmxpulsemxtriggerminimumquiettimemode.html language=enus -->
## TOPIC 00095: SetTriggerMinimumQuietTimeMode(string, RFmxPulseMXTriggerMinimumQuietTimeMode)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-settriggerminimumquiettimemode__string-rfmxpulsemxtriggerminimumquiettimemode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-settriggerminimumquiettimemode__string-rfmxpulsemxtriggerminimumquiettimemode.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement computes the minimum quiet time used for triggering. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetTriggerMinimumQuietTimeMode(string selectorString, RFmxPulseMXTriggerMinimumQuietTimeMode value)RemarksThis method sets the value of TriggerMinimumQuietTim

### SetTriggerMinimumQuietTimeMode(string, RFmxPulseMXTriggerMinimumQuietTimeMode)

Sets whether the measurement computes the minimum quiet time used for triggering.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetTriggerMinimumQuietTimeMode(string selectorString, RFmxPulseMXTriggerMinimumQuietTimeMode value)

#### Remarks

This method sets the value of [TriggerMinimumQuietTimeMode](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [Manual](nationalinstruments-rfmx-pulsemx-rfmxpulsemxtriggerminimumquiettimemode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXTriggerMinimumQuietTimeMode | Specifies whether the measurement computes the minimum quiet time used for triggering. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-settriggertype__string-rfmxpulsemxtriggertype.html language=enus -->
## TOPIC 00096: SetTriggerType(string, RFmxPulseMXTriggerType)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-settriggertype__string-rfmxpulsemxtriggertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-settriggertype__string-rfmxpulsemxtriggertype.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the trigger type. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetTriggerType(string selectorString, RFmxPulseMXTriggerType value)RemarksThis method sets the value of TriggerType attribute.The default value is None.ParametersNameTypeDescriptionselectorStringstringPass an empty st

### SetTriggerType(string, RFmxPulseMXTriggerType)

Sets the trigger type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetTriggerType(string selectorString, RFmxPulseMXTriggerType value)

#### Remarks

This method sets the value of [TriggerType](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [None](nationalinstruments-rfmx-pulsemx-rfmxpulsemxtriggertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXTriggerType | Specifies the trigger type. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-signalconfigurationname.html language=enus -->
## TOPIC 00097: SignalConfigurationName

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-signalconfigurationname.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-signalconfigurationname.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the signal configuration name. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic string SignalConfigurationName { get; }RemarksReturns a string representing the signal configuration name

### SignalConfigurationName

Gets the signal configuration name.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public string SignalConfigurationName { get; }

#### Remarks

Returns a string representing the signal configuration name

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-signalconfigurationtype.html language=enus -->
## TOPIC 00098: SignalConfigurationType

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-signalconfigurationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-signalconfigurationtype.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Type object for RFmxPulseMX. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic Type SignalConfigurationType { get; }RemarksReturns the type of signal configuration object.

### SignalConfigurationType

Gets the Type object for RFmxPulseMX.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public Type SignalConfigurationType { get; }

#### Remarks

Returns the type of signal configuration object.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx-waitformeasurementcomplete__string-double.html language=enus -->
## TOPIC 00099: WaitForMeasurementComplete(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx-waitformeasurementcomplete__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx-waitformeasurementcomplete__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the specified number for seconds for all the measurements to complete.SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int WaitForMeasurementComplete(string selectorString, double timeout)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the

### WaitForMeasurementComplete(string, double)

Waits for the specified number for seconds for all the measurements to complete.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int WaitForMeasurementComplete(string selectorString, double timeout)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" |
| timeout | double | Specifies the time, in seconds, for which the method waits for the measurement to complete. A value of -1 specifies that the method waits until the measurement is complete. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMX Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemx.html language=enus -->
## TOPIC 00100: RFmxPulseMX Class

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemx.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemx.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines a root class which is used to identify and control PULSE signal configuration. Derives fromISignalConfigurationIDisposableSyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic class RFmxPulseMX : ISignalConfiguration, IDisposablePropertiesNameDescriptionIsDisposedGets a value that indicate

### RFmxPulseMX Class

Defines a root class which is used to identify and control PULSE signal configuration.

#### Derives from

- ISignalConfiguration
- IDisposable

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public class RFmxPulseMX : ISignalConfiguration, IDisposable

#### Properties

| Name | Description |
| --- | --- |
| IsDisposed | Gets a value that indicates whether the signal has been disposed. |
| Pulse | Gets the RFmxPulseMXPulse instance that represents the Pulse measurement. |
| SignalConfigurationName | Gets the signal configuration name. |
| SignalConfigurationType | Gets the Type object for RFmxPulseMX. |

#### Methods

| Name | Description |
| --- | --- |
| AbortMeasurements(string) | Stops acquisition and measurements associated with signal instance that you specify in the selectorString parameter, which were previously initiated by the Initiate(string, string) method or measurement read methods. Calling this method is optional, unless you want to stop a measurement before it is complete. This method executes even if there is an incoming error. |
| AnalyzeIQ1Waveform(string, string, ComplexWaveform< ComplexSingle >, bool, long) | Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods in the method node. Use this method only if the RFmxInstrMX.GetRecommendedAcquisitionType method value is either IQ or IQorSpectral. Query the Recommended Acquisition Type method from the RFmxInstr Property Node after calling the RFmx Pulse Commit method. |
| AutoLevel(string, double, double, out double) | Examines the input signal to calculate the peak power level and sets it as the value of the ReferenceLevel method. Use this method to help calculate an approximate setting for the reference level. |
| CheckMeasurementStatus(string, out bool) | Checks the status of the measurement. Use this method to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
| ClearAllNamedResults(string) | Clears all results for the current signal instance. |
| ClearNamedResult(string) | Clears a result instance specified by the result name in the selectorString parameter. |
| CloneSignalConfiguration(string, out RFmxPulseMX) | Creates a new instance of a signal by copying all the method values from an existing signal instance. |
| Commit(string) | Commits settings to the hardware. Calling this method is optional. RFmxPulse commits settings to the hardware when you call the Initiate(string, string) method or any of the measurement Read methods. |
| ConfigureDigitalEdgeTrigger(string, string, RFmxPulseMXDigitalEdgeTriggerEdge, double, bool) | Configures the device to wait for a digital edge trigger and then marks a reference point within the record. |
| ConfigureExternalAttenuation(string, double) | Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. |
| ConfigureFrequency(string, double) | Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. |
| ConfigureIQPowerEdgeTrigger(string, string, RFmxPulseMXIQPowerEdgeTriggerSlope, double, double, RFmxPulseMXTriggerMinimumQuietTimeMode, double, RFmxPulseMXIQPowerEdgeTriggerLevelType, bool) | Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record. |
| ConfigureReferenceLevel(string, double) | Configures the reference level, which represents the maximum expected power of an RF input signal. |
| ConfigureRF(string, double, double, double) | Configures the RF methods of the signal specified by the selector string. |
| ConfigureSoftwareEdgeTrigger(string, double, bool) | Configures the device to wait for a software trigger and then marks a reference point within the record. |
| DeleteSignalConfiguration() | Deletes an instance of a signal. |
| DisableTrigger(string) | Configures the device to not wait for a trigger to mark a reference point within a record. This method defines the signal triggering as immediate. |
| Dispose() | Deletes the signal configuration if it is not the default signal configuration and clears any trace of the current signal configuration, if any. |
| GetAcquisitionLength(string, out double) | Gets the acquisition length for the pulse measurement. This value is expressed in seconds.You configure this method when you set the SegmentedAcquisitionEnabled method to False. |
| GetAllNamedResultNames(string, out string[], out bool) | Gets the named result names of the signal that you specify in the selectorString parameter. |
| GetAttributeBool(string, int, out bool) | Gets the value of a Bool attribute. |
| GetAttributeDouble(string, int, out double) | Gets the value of a Double attribute. |
| GetAttributeDoubleArray(string, int, ref double[]) | Gets the value of a double array attribute. |
| GetAttributeInt(string, int, out int) | Gets the value of an RFmx 32-bit integer (int32) attribute. |
| GetAttributeIntArray(string, int, ref int[]) | Gets the value of a integer array attribute. |
| GetAttributeString(string, int, out string) | Gets the value of a of an RFmx string. |
| GetAutoLevelInitialReferenceLevel(string, out double) | Gets the initial reference level, in dBm, which the AutoLevel(string, double, double, out double) function uses to estimate the peak power of the input signal. |
| GetCenterFrequency(string, out double) | Gets the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency. |
| GetDigitalEdgeTriggerEdge(string, out RFmxPulseMXDigitalEdgeTriggerEdge) | Gets the active edge for the trigger. This method is used only when you set the TriggerType method to DigitalEdge. |
| GetDigitalEdgeTriggerSource(string, out string) | Gets the source terminal for the digital edge trigger. This method is used only when you set the TriggerType method to DigitalEdge. |
| GetError(out int, out string) | Gets the latest error code and description. |
| GetErrorString(int, out string) | Converts the status code returned by an RFmxPULSE function into a string. |
| GetExternalAttenuation(string, out double) | Gets the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |
| GetIQPowerEdgeTriggerLevel(string, out double) | Gets the power level at which the device triggers. This value is expressed in dB when you set the IQPowerEdgeTriggerLevelType method to Relative and in dBm when you set the IQ Power Edge Level Type method to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the TriggerType method to IQPowerEdge. |
| GetIQPowerEdgeTriggerLevelType(string, out RFmxPulseMXIQPowerEdgeTriggerLevelType) | Gets the reference for the IQPowerEdgeTriggerLevel method. The IQ Power Edge Level Type method is used only when you set the TriggerType method to IQPowerEdge. |
| GetIQPowerEdgeTriggerSlope(string, out RFmxPulseMXIQPowerEdgeTriggerSlope) | Gets whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the IQPowerEdgeTriggerLevel method with the slope you specify. This method is used only when you set the TriggerType method to IQPowerEdge. |
| GetIQPowerEdgeTriggerSource(string, out string) | Gets the channel from which the device monitors the trigger. This method is used only when you set the TriggerType method to IQPowerEdge. |
| GetMaximumPulseCount(string, out int) | Gets the maximum number of pulses to be measured when you set the MaximumPulseCountEnabled method to True. |
| GetMaximumPulseCountEnabled(string, out RFmxPulseMXMaximumPulseCountEnabled) | Gets whether to enable the maximum pulse count for pulse measurements.You must configure this method when you set the SegmentedAcquisitionEnabled method to False. |
| GetMeasurementBandwidth(string, out double) | Gets the bandwidth of the filter used for the required sample rate. This value is expressed in Hz. |
| GetMeasurementFilterType(string, out RFmxPulseMXMeasurementFilterType) | Gets the demodulation filter type to be used in the measurements. |
| GetNumberOfSegments(string, out int) | Gets the number of segments to acquire when you set the SegmentedAcquisitionEnabled method to True. |
| GetReferenceLevel(string, out double) | Gets the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
| GetReferenceLevelHeadroom(string, out double) | Gets the margin RFmx adds to the ReferenceLevel method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. |
| GetResultFetchTimeout(string, out double) | Gets the wait time before results are available in the PropertyNode. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxPulse Property Node waits until the measurement is complete. |
| GetSegmentAcquisitionLength(string, out double) | Gets the acquisition length for the pulse measurement when you set the SegmentedAcquisitionEnabled method to True. This value is expressed in seconds. |
| GetSegmentedAcquisitionEnabled(string, out RFmxPulseMXSegmentedAcquisitionEnabled) | Gets whether to enable Segmented Acquisition. This mode is best applied when the pulses are sparsely spaced. |
| GetSelectedPorts(string, out string) | Gets the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |
| GetTriggerDelay(string, out double) | Gets the trigger delay time. This value is expressed in seconds.If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. |
| GetTriggerMinimumQuietTimeDuration(string, out double) | Gets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the IQPowerEdgeTriggerSlope method to Rising, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope method to Falling, the signal is quiet above the trigger level. |
| GetTriggerMinimumQuietTimeMode(string, out RFmxPulseMXTriggerMinimumQuietTimeMode) | Gets whether the measurement computes the minimum quiet time used for triggering. |
| GetTriggerType(string, out RFmxPulseMXTriggerType) | Gets the trigger type. |
| GetWarning(out int, out string) | Gets the latest warning code and description. |
| Initiate(string, string) | Initiates all enabled measurements. Call this method after configuring the signal and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch methods or result methods in the method node. To get the status of measurements, use the RF WaitForMeasurementComplete(string, double) method or CheckMeasurementStatus(string, out bool) method. |
| ResetAttribute(string, RFmxPulseMXPropertyId) | Resets the attribute to its default value. |
| ResetToDefault(string) | Resets a signal to the default values. |
| SelectMeasurements(string, RFmxPulseMXMeasurementTypes, bool) | Specifies the measurements that you want to enable. |
| SendSoftwareEdgeTrigger() | Sends a trigger to the device when you use the ConfigureSoftwareEdgeTrigger(string, double, bool) method to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this method to override a hardware trigger. |
| SetAcquisitionLength(string, double) | Sets the acquisition length for the pulse measurement. This value is expressed in seconds.You configure this method when you set the SegmentedAcquisitionEnabled method to False. |
| SetAttributeBool(string, int, bool) | Sets the value of a Bool attribute. |
| SetAttributeDouble(string, int, double) | Sets the value of a Double attribute. |
| SetAttributeDoubleArray(string, int, double[]) | Set the value of a double array attribute. |
| SetAttributeInt(string, int, int) | Sets the value of a Int attribute. |
| SetAttributeIntArray(string, int, int[]) | Set the value of a integer array attribute. |
| SetAttributeString(string, int, string) | Sets the value of a String attribute. |
| SetAutoLevelInitialReferenceLevel(string, double) | Sets the initial reference level, in dBm, which the AutoLevel(string, double, double, out double) function uses to estimate the peak power of the input signal. |
| SetCenterFrequency(string, double) | Sets the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency. |
| SetDigitalEdgeTriggerEdge(string, RFmxPulseMXDigitalEdgeTriggerEdge) | Sets the active edge for the trigger. This method is used only when you set the TriggerType method to DigitalEdge. |
| SetDigitalEdgeTriggerSource(string, string) | Sets the source terminal for the digital edge trigger. This method is used only when you set the TriggerType method to DigitalEdge. |
| SetExternalAttenuation(string, double) | Sets the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |
| SetIQPowerEdgeTriggerLevel(string, double) | Sets the power level at which the device triggers. This value is expressed in dB when you set the IQPowerEdgeTriggerLevelType method to Relative and in dBm when you set the IQ Power Edge Level Type method to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the TriggerType method to IQPowerEdge. |
| SetIQPowerEdgeTriggerLevelType(string, RFmxPulseMXIQPowerEdgeTriggerLevelType) | Sets the reference for the IQPowerEdgeTriggerLevel method. The IQ Power Edge Level Type method is used only when you set the TriggerType method to IQPowerEdge. |
| SetIQPowerEdgeTriggerSlope(string, RFmxPulseMXIQPowerEdgeTriggerSlope) | Sets whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the IQPowerEdgeTriggerLevel method with the slope you specify. This method is used only when you set the TriggerType method to IQPowerEdge. |
| SetIQPowerEdgeTriggerSource(string, string) | Sets the channel from which the device monitors the trigger. This method is used only when you set the TriggerType method to IQPowerEdge. |
| SetMaximumPulseCount(string, int) | Sets the maximum number of pulses to be measured when you set the MaximumPulseCountEnabled method to True. |
| SetMaximumPulseCountEnabled(string, RFmxPulseMXMaximumPulseCountEnabled) | Sets whether to enable the maximum pulse count for pulse measurements.You must configure this method when you set the SegmentedAcquisitionEnabled method to False. |
| SetMeasurementBandwidth(string, double) | Sets the bandwidth of the filter used for the required sample rate. This value is expressed in Hz. |
| SetMeasurementFilterType(string, RFmxPulseMXMeasurementFilterType) | Sets the demodulation filter type to be used in the measurements. |
| SetNumberOfSegments(string, int) | Sets the number of segments to acquire when you set the SegmentedAcquisitionEnabled method to True. |
| SetReferenceLevel(string, double) | Sets the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
| SetReferenceLevelHeadroom(string, double) | Sets the margin RFmx adds to the ReferenceLevel method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. |
| SetResultFetchTimeout(string, double) | Sets the wait time before results are available in the RFmx Property. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxPulse Property Node waits until the measurement is complete. |
| SetSegmentAcquisitionLength(string, double) | Sets the acquisition length for the pulse measurement when you set the SegmentedAcquisitionEnabled method to True. This value is expressed in seconds. |
| SetSegmentedAcquisitionEnabled(string, RFmxPulseMXSegmentedAcquisitionEnabled) | Sets whether to enable Segmented Acquisition. This mode is best applied when the pulses are sparsely spaced. |
| SetSelectedPorts(string, string) | Sets the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |
| SetTriggerDelay(string, double) | Sets the trigger delay time. This value is expressed in seconds.If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. |
| SetTriggerMinimumQuietTimeDuration(string, double) | Sets the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the IQPowerEdgeTriggerSlope method to Rising, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope method to Falling, the signal is quiet above the trigger level. |
| SetTriggerMinimumQuietTimeMode(string, RFmxPulseMXTriggerMinimumQuietTimeMode) | Sets whether the measurement computes the minimum quiet time used for triggering. |
| SetTriggerType(string, RFmxPulseMXTriggerType) | Sets the trigger type. |
| WaitForMeasurementComplete(string, double) | Waits for the specified number for seconds for all the measurements to complete. |
| BuildResultString(string) | Creates selector string for use with configuration or fetch. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-diopfi0.html language=enus -->
## TOPIC 00101: DioPfi0

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-diopfi0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-diopfi0.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic const string DioPfi0

### DioPfi0

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public const string DioPfi0

Parent topic:

RFmxPulseMXConstants Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-diopfi1.html language=enus -->
## TOPIC 00102: DioPfi1

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-diopfi1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-diopfi1.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic const string DioPfi1

### DioPfi1

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public const string DioPfi1

Parent topic:

RFmxPulseMXConstants Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-diopfi2.html language=enus -->
## TOPIC 00103: DioPfi2

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-diopfi2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-diopfi2.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic const string DioPfi2

### DioPfi2

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public const string DioPfi2

Parent topic:

RFmxPulseMXConstants Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-diopfi3.html language=enus -->
## TOPIC 00104: DioPfi3

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-diopfi3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-diopfi3.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic const string DioPfi3

### DioPfi3

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public const string DioPfi3

Parent topic:

RFmxPulseMXConstants Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-diopfi4.html language=enus -->
## TOPIC 00105: DioPfi4

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-diopfi4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-diopfi4.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic const string DioPfi4

### DioPfi4

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public const string DioPfi4

Parent topic:

RFmxPulseMXConstants Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-diopfi5.html language=enus -->
## TOPIC 00106: DioPfi5

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-diopfi5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-diopfi5.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic const string DioPfi5

### DioPfi5

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public const string DioPfi5

Parent topic:

RFmxPulseMXConstants Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-diopfi6.html language=enus -->
## TOPIC 00107: DioPfi6

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-diopfi6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-diopfi6.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic const string DioPfi6

### DioPfi6

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public const string DioPfi6

Parent topic:

RFmxPulseMXConstants Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-diopfi7.html language=enus -->
## TOPIC 00108: DioPfi7

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-diopfi7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-diopfi7.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic const string DioPfi7

### DioPfi7

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public const string DioPfi7

Parent topic:

RFmxPulseMXConstants Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pfi0.html language=enus -->
## TOPIC 00109: Pfi0

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pfi0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pfi0.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PFI 0. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic const string Pfi0

### Pfi0

The signal is exported to the PFI 0.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public const string Pfi0

Parent topic:

RFmxPulseMXConstants Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pfi1.html language=enus -->
## TOPIC 00110: Pfi1

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pfi1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pfi1.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI 1. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic const string Pfi1

### Pfi1

The signal is exported to the PXI 1.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public const string Pfi1

Parent topic:

RFmxPulseMXConstants Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pulsein.html language=enus -->
## TOPIC 00111: PulseIn

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pulsein.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pulsein.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic const string PulseIn

### PulseIn

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public const string PulseIn

Parent topic:

RFmxPulseMXConstants Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxiedstarbline.html language=enus -->
## TOPIC 00112: PxieDStarBLine

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxiedstarbline.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxiedstarbline.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXIe DStar B trigger line. This value is valid only for PXIe-5820/5830/5831/5840/5841. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic const string PxieDStarBLine

### PxieDStarBLine

The signal is exported to the PXIe DStar B trigger line. This value is valid only for PXIe-5820/5830/5831/5840/5841.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public const string PxieDStarBLine

Parent topic:

RFmxPulseMXConstants Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxistarline.html language=enus -->
## TOPIC 00113: PxiStarLine

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxistarline.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxistarline.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI star trigger line. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic const string PxiStarLine

### PxiStarLine

The signal is exported to the PXI star trigger line.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public const string PxiStarLine

Parent topic:

RFmxPulseMXConstants Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxitriggerline0.html language=enus -->
## TOPIC 00114: PxiTriggerLine0

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxitriggerline0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxitriggerline0.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 0. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic const string PxiTriggerLine0

### PxiTriggerLine0

The signal is exported to the PXI trigger line 0.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public const string PxiTriggerLine0

Parent topic:

RFmxPulseMXConstants Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxitriggerline1.html language=enus -->
## TOPIC 00115: PxiTriggerLine1

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxitriggerline1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxitriggerline1.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 1. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic const string PxiTriggerLine1

### PxiTriggerLine1

The signal is exported to the PXI trigger line 1.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public const string PxiTriggerLine1

Parent topic:

RFmxPulseMXConstants Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxitriggerline2.html language=enus -->
## TOPIC 00116: PxiTriggerLine2

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxitriggerline2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxitriggerline2.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 2. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic const string PxiTriggerLine2

### PxiTriggerLine2

The signal is exported to the PXI trigger line 2.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public const string PxiTriggerLine2

Parent topic:

RFmxPulseMXConstants Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxitriggerline3.html language=enus -->
## TOPIC 00117: PxiTriggerLine3

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxitriggerline3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxitriggerline3.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 3. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic const string PxiTriggerLine3

### PxiTriggerLine3

The signal is exported to the PXI trigger line 3.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public const string PxiTriggerLine3

Parent topic:

RFmxPulseMXConstants Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxitriggerline4.html language=enus -->
## TOPIC 00118: PxiTriggerLine4

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxitriggerline4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxitriggerline4.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 4. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic const string PxiTriggerLine4

### PxiTriggerLine4

The signal is exported to the PXI trigger line 4.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public const string PxiTriggerLine4

Parent topic:

RFmxPulseMXConstants Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxitriggerline5.html language=enus -->
## TOPIC 00119: PxiTriggerLine5

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxitriggerline5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxitriggerline5.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 5. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic const string PxiTriggerLine5

### PxiTriggerLine5

The signal is exported to the PXI trigger line 5.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public const string PxiTriggerLine5

Parent topic:

RFmxPulseMXConstants Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxitriggerline6.html language=enus -->
## TOPIC 00120: PxiTriggerLine6

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxitriggerline6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxitriggerline6.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 6. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic const string PxiTriggerLine6

### PxiTriggerLine6

The signal is exported to the PXI trigger line 6.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public const string PxiTriggerLine6

Parent topic:

RFmxPulseMXConstants Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxitriggerline7.html language=enus -->
## TOPIC 00121: PxiTriggerLine7

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxitriggerline7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-pxitriggerline7.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 7. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic const string PxiTriggerLine7

### PxiTriggerLine7

The signal is exported to the PXI trigger line 7.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public const string PxiTriggerLine7

Parent topic:

RFmxPulseMXConstants Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-timerevent.html language=enus -->
## TOPIC 00122: TimerEvent

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-timerevent.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants-timerevent.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The trigger is received from the timer event. This value is valid only for PXIe-5820/5840/5841 and for digital edge advance triggers on PXIe-5663E/5665. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic const string TimerEvent

### TimerEvent

The trigger is received from the timer event. This value is valid only for PXIe-5820/5840/5841 and for digital edge advance triggers on PXIe-5663E/5665.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public const string TimerEvent

Parent topic:

RFmxPulseMXConstants Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants.html language=enus -->
## TOPIC 00123: RFmxPulseMXConstants Class

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxconstants.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies constants for I/O terminals. Derives fromNoneSyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic class RFmxPulseMXConstantsFieldsNameDescriptionDioPfi0DioPfi1DioPfi2DioPfi3DioPfi4DioPfi5DioPfi6DioPfi7Pfi0The signal is exported to the PFI 0. Pfi1The signal is exported to the PXI 1. Puls

### RFmxPulseMXConstants Class

Specifies constants for I/O terminals.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public class RFmxPulseMXConstants

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
| Pfi0 | The signal is exported to the PFI 0. |
| Pfi1 | The signal is exported to the PXI 1. |
| PulseIn |  |
| PxieDStarBLine | The signal is exported to the PXIe DStar B trigger line. This value is valid only for PXIe-5820/5830/5831/5840/5841. |
| PxiStarLine | The signal is exported to the PXI star trigger line. |
| PxiTriggerLine0 | The signal is exported to the PXI trigger line 0. |
| PxiTriggerLine1 | The signal is exported to the PXI trigger line 1. |
| PxiTriggerLine2 | The signal is exported to the PXI trigger line 2. |
| PxiTriggerLine3 | The signal is exported to the PXI trigger line 3. |
| PxiTriggerLine4 | The signal is exported to the PXI trigger line 4. |
| PxiTriggerLine5 | The signal is exported to the PXI trigger line 5. |
| PxiTriggerLine6 | The signal is exported to the PXI trigger line 6. |
| PxiTriggerLine7 | The signal is exported to the PXI trigger line 7. |
| TimerEvent | The trigger is received from the timer event. This value is valid only for PXIe-5820/5840/5841 and for digital edge advance triggers on PXIe-5663E/5665. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxdigitaledgetriggeredge.html language=enus -->
## TOPIC 00124: RFmxPulseMXDigitalEdgeTriggerEdge Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxdigitaledgetriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxdigitaledgetriggeredge.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the active edge for the trigger. This method is used only when you set the TriggerType method to DigitalEdge. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXDigitalEdgeTriggerEdgeMembersNameValueDescriptionRising0The trigger asserts on the rising edge of the signal

### RFmxPulseMXDigitalEdgeTriggerEdge Enumeration

Specifies the active edge for the trigger. This method is used only when you set the [TriggerType](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [DigitalEdge](nationalinstruments-rfmx-pulsemx-rfmxpulsemxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXDigitalEdgeTriggerEdge

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 0 | The trigger asserts on the rising edge of the signal. |
| Falling | 1 | The trigger asserts on the falling edge of the signal. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxiqpoweredgetriggerleveltype.html language=enus -->
## TOPIC 00125: RFmxPulseMXIQPowerEdgeTriggerLevelType Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxiqpoweredgetriggerleveltype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxiqpoweredgetriggerleveltype.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference for the IQPowerEdgeTriggerLevel method. The IQ Power Edge Level Type method is used only when you set the TriggerType method to IQPowerEdge. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXIQPowerEdgeTriggerLevelTypeMembersNameValueDescriptionRelative0

### RFmxPulseMXIQPowerEdgeTriggerLevelType Enumeration

Specifies the reference for the [IQPowerEdgeTriggerLevel](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method. The IQ Power Edge Level Type method is used only when you set the [TriggerType](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [IQPowerEdge](nationalinstruments-rfmx-pulsemx-rfmxpulsemxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXIQPowerEdgeTriggerLevelType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Relative | 0 | The value of the IQ Power Edge Level method is relative to the value of the ReferenceLevel method. |
| Absolute | 1 | The IQ Power Edge Level method specifies the absolute power. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxiqpoweredgetriggerslope.html language=enus -->
## TOPIC 00126: RFmxPulseMXIQPowerEdgeTriggerSlope Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxiqpoweredgetriggerslope.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxiqpoweredgetriggerslope.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the IQPowerEdgeTriggerLevel method with the slope you specify. This method is used only when you set the

### RFmxPulseMXIQPowerEdgeTriggerSlope Enumeration

Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the [IQPowerEdgeTriggerLevel](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method with the slope you specify. This method is used only when you set the [TriggerType](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [IQPowerEdge](nationalinstruments-rfmx-pulsemx-rfmxpulsemxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXIQPowerEdgeTriggerSlope

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 0 | The trigger asserts when the signal power is rising. |
| Falling | 1 | The trigger asserts when the signal power is falling. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxmaximumpulsecountenabled.html language=enus -->
## TOPIC 00127: RFmxPulseMXMaximumPulseCountEnabled Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxmaximumpulsecountenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxmaximumpulsecountenabled.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the maximum pulse count for pulse measurements.You must configure this method when you set the SegmentedAcquisitionEnabled method to False. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXMaximumPulseCountEnabledMembersNameValueDescriptionFalse0The

### RFmxPulseMXMaximumPulseCountEnabled Enumeration

Specifies whether to enable the maximum pulse count for pulse measurements.You must configure this method when you set the [SegmentedAcquisitionEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to False.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXMaximumPulseCountEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The maximum pulse count is disabled. |
| True | 1 | The maximum pulse count is enabled. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxmeasurementfiltertype.html language=enus -->
## TOPIC 00128: RFmxPulseMXMeasurementFilterType Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxmeasurementfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxmeasurementfiltertype.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the demodulation filter type to be used in the measurements. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXMeasurementFilterTypeMembersNameValueDescriptionRectangular0The Rectangular filter is applied. Gaussian1The Gaussian filter is applied.

### RFmxPulseMXMeasurementFilterType Enumeration

Specifies the demodulation filter type to be used in the measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXMeasurementFilterType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rectangular | 0 | The Rectangular filter is applied. |
| Gaussian | 1 | The Gaussian filter is applied. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxmeasurementtypes.html language=enus -->
## TOPIC 00129: RFmxPulseMXMeasurementTypes Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxmeasurementtypes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxmeasurementtypes.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of measurement. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXMeasurementTypesMembersNameValueDescriptionPulse0x1Selects Pulse measurement.

### RFmxPulseMXMeasurementTypes Enumeration

Specifies the type of measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXMeasurementTypes

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Pulse | 0x1 | Selects Pulse measurement. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxmultiburstenabled.html language=enus -->
## TOPIC 00130: RFmxPulseMXMultiburstEnabled Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxmultiburstenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxmultiburstenabled.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable pulse measurements on the multiple burst transmission. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXMultiburstEnabledMembersNameValueDescriptionFalse0Multiburst disabled, assumes all pulses detected in the current acquisition are analysed as sin

### RFmxPulseMXMultiburstEnabled Enumeration

Specifies whether to enable pulse measurements on the multiple burst transmission.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXMultiburstEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Multiburst disabled, assumes all pulses detected in the current acquisition are analysed as single burst. |
| True | 1 | Multiburst enabled, assumes every burst in the acquisition contains pulses specified by Pulse Burst Length (Pulses) method. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html language=enus -->
## TOPIC 00131: RFmxPulseMXPropertyId Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies all the attribute identifiers. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXPropertyIdMembersNameValueDescriptionSelectedPorts12587005Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid por

### RFmxPulseMXPropertyId Enumeration

Specifies all the attribute identifiers.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXPropertyId

#### Members

| Name | Value | Description |
| --- | --- | --- |
| SelectedPorts | 12587005 | Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |
| CenterFrequency | 12582913 | Specifies the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency. |
| ReferenceLevel | 12582914 | Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
| ExternalAttenuation | 12582915 | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |
| ReferenceLevelHeadroom | 12587004 | Specifies the margin RFmx adds to the ReferenceLevel method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. |
| TriggerType | 12582916 | Specifies the trigger type. |
| DigitalEdgeTriggerSource | 12582917 | Specifies the source terminal for the digital edge trigger. This method is used only when you set the TriggerType method to DigitalEdge. |
| DigitalEdgeTriggerEdge | 12582918 | Specifies the active edge for the trigger. This method is used only when you set the TriggerType method to DigitalEdge. |
| IQPowerEdgeTriggerSource | 12582919 | Specifies the channel from which the device monitors the trigger. This method is used only when you set the TriggerType method to IQPowerEdge. |
| IQPowerEdgeTriggerLevel | 12582920 | Specifies the power level at which the device triggers. This value is expressed in dB when you set the IQPowerEdgeTriggerLevelType method to Relative and in dBm when you set the IQ Power Edge Level Type method to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the TriggerType method to IQPowerEdge. |
| IQPowerEdgeTriggerLevelType | 12587007 | Specifies the reference for the IQPowerEdgeTriggerLevel method. The IQ Power Edge Level Type method is used only when you set the TriggerType method to IQPowerEdge. |
| IQPowerEdgeTriggerSlope | 12582921 | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the IQPowerEdgeTriggerLevel method with the slope you specify. This method is used only when you set the TriggerType method to IQPowerEdge. |
| TriggerDelay | 12582922 | Specifies the trigger delay time. This value is expressed in seconds.If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. |
| TriggerMinimumQuietTimeMode | 12582923 | Specifies whether the measurement computes the minimum quiet time used for triggering. |
| TriggerMinimumQuietTimeDuration | 12582924 | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the IQPowerEdgeTriggerSlope method to Rising, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope method to Falling, the signal is quiet above the trigger level. |
| MeasurementBandwidth | 12582935 | Specifies the bandwidth of the filter used for the required sample rate. This value is expressed in Hz. |
| MeasurementFilterType | 12582936 | Specifies the demodulation filter type to be used in the measurements. |
| AcquisitionLength | 12582929 | Specifies the acquisition length for the pulse measurement. This value is expressed in seconds.You configure this method when you set the SegmentedAcquisitionEnabled method to False. |
| MaximumPulseCountEnabled | 12582930 | Specifies whether to enable the maximum pulse count for pulse measurements.You must configure this method when you set the SegmentedAcquisitionEnabled method to False. |
| MaximumPulseCount | 12582931 | Specifies the maximum number of pulses to be measured when you set the MaximumPulseCountEnabled method to True. |
| SegmentedAcquisitionEnabled | 12582932 | Specifies whether to enable Segmented Acquisition. This mode is best applied when the pulses are sparsely spaced. |
| NumberOfSegments | 12582933 | Specifies the number of segments to acquire when you set the SegmentedAcquisitionEnabled method to True. |
| SegmentAcquisitionLength | 12582934 | Specifies the acquisition length for the pulse measurement when you set the SegmentedAcquisitionEnabled method to True. This value is expressed in seconds. |
| PulseMeasurementEnabled | 12587008 | Specifies whether pulse measurements are enabled.. |
| PulseMultiburstEnabled | 12587230 | Specifies whether to enable pulse measurements on the multiple burst transmission. |
| PulseMultiburstLength | 12587231 | Specifies the number of pulses assigned to a single burst. |
| PulseDetectionReference | 12587010 | Specifies the reference used for SetDetectionThreshold(string, double) method. |
| PulseDetectionThreshold | 12587011 | Specifies the threshold used for pulse detection. The unit dB or dBm is based on the value you set to the SetDetectionReference(string, RFmxPulseMXPulseDetectionReference) method. |
| PulseDetectionHysteresis | 12587012 | Specifies the hysteresis for pulse detection in dB for the defined threshold. |
| PulseDetectionMinimumOffDuration | 12587013 | Specifies the minimum pulse off duration to be ignored by the pulse detection. This value is expressed in seconds. |
| PulseDetectionMinimumWidth | 12587014 | Specifies the minimum pulse width time to be considered for pulse detection. Any detected pulse width time below the specified value will be ignored by the pulse detection. This value is expressed in seconds. |
| PulseDetectionMaximumWidth | 12587015 | Specifies the maximum pulse width time to be considered for pulse detection. Any detected pulse width time above the specified value will be ignored by the pulse detection. This value is expressed in seconds. |
| PulseMetricsEnabled | 12587162 | Specifies whether to enable pulse metrics results computation. |
| PulseMetricsAmplitudeDeviationUnit | 12587229 | Specifies the unit for amplitude deviation results. This method is applicable only for droop, ripple and overshoot results. |
| PulseLevelComputationMethod | 12587016 | Specifies the algorithm used to detect the pulse levels. The algorithm is based on the histogram method of level detection as defined in IEEE Std 181-2011. |
| PulseAmplitudeLevelDomain | 12587017 | Specifies whether voltage or power to be used as domain for pulse measurements. |
| PulseUpperThresholdLevel | 12587018 | Specifies the upper threshold level as a percentage of the pulse amplitude used to signify the end of a rising edge or beginning of a falling edge. |
| PulseWidthThresholdLevel | 12587019 | Specifies the middle threshold level as a percentage of the pulse amplitude used to signify the mid-transition level between pulse states used for pulse width computation. |
| PulseLowerThresholdLevel | 12587020 | Specifies the lower threshold level as a percentage of the pulse amplitude used to signify the start of a rising or end of a falling edge. |
| PulseDroopCompensationEnabled | 12587021 | Specifies whether to compensate the droop detected in pulse level when applying thresholds. |
| PulseMeasurementPointReference | 12587146 | Specifies the reference used for the measurement point calculation, in phase, frequency, and stability measurements. You can set measurement point based on a reference and offset. |
| PulseMeasurementPointOffset | 12587147 | Specifies the time offset of the measurement point within the pulse for phase, frequency, and stability measurements. |
| PulseMeasurementPointAveragingDuration | 12587148 | Specifies the length of the averaging window centered at the measurement point. A minimum of 1 sample is used internally. |
| PulseMultipleMeasurementPointsEnabled | 12587235 | Specifies whether to enable pulse stability measurements on multiple measurement points. This method is used to enable the multiple measurement points stability trace when you set the All Traces Enabled method to TRUE. |
| PulseMultipleMeasurementPointsWindowStart | 12587236 | Specifies the start of the measurement window used for multiple measurement points selection over pulse ON duration. |
| PulseMultipleMeasurementPointsWindowStop | 12587237 | Specifies the stop of the measurement window used for multiple measurement points selection over pulse ON duration. |
| PulseMultipleMeasurementPointsWindowStepSize | 12587238 | Specifies the step size of multiple measurement points selection within the measurement window over pulse ON duration. A minimum of 1 sample step size is used internally. |
| PulseFrequencyAndPhaseDeviationRangeReference | 12587149 | Specifies the reference used for the measurement range in phase/frequency deviation and error measurements. |
| PulseFrequencyAndPhaseDeviationRangeLength | 12587150 | Specifies the length of the pulse data used for the phase/frequency deviation and error measurements when you set the SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference) method to Center. |
| PulseFrequencyAndPhaseDeviationRangeEdgeStart | 12587151 | Specifies the start of the pulse data used for the phase/frequency deviation and error measurements when you set the SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference) method to Edge. |
| PulseFrequencyAndPhaseDeviationRangeEdgeStop | 12587152 | Specifies the stop of the pulse data used for the phase/frequency deviation and error measurements when you set the SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference) method to Edge. |
| PulseFrequencyAndPhaseModulationType | 12587163 | Specifies the pulse modulation type used for the phase and frequency error, and pulsed FM Measurement. |
| PulseFrequencyAndPhaseCWFrequencyOffsetAuto | 12587164 | Specifies whether the CW frequency offset computation of every detected pulse is automatic or manual. This method is valid only when you set the SetFrequencyAndPhaseModulationType(string, RFmxPulseMXPulseModulationType) method to CW. |
| PulseFrequencyAndPhaseCWFrequencyOffset | 12587165 | Specifies to manually enter the CW frequency offset. This method is valid only when you set the SetFrequencyAndPhaseModulationType(string, RFmxPulseMXPulseModulationType) method to CW. |
| PulseStabilityEnabled | 12587161 | Specifies whether to enable pulse stability results computation. |
| PulseStabilityMeasurementOffset | 12587154 | Specifies the offset in number of pulses to be used for pulse stability measurement. This method is applicable for average stability results and pulse-to-pulse stabilty trace. |
| PulseStabilityReferenceOffset | 12587155 | Specifies the offset in number of pulses used for pulse stability reference computation. |
| PulseStabilityPulseToPulseOffset | 12587156 | Specifies the offset in number of pulses used for pulse-to-pulse stability measurement trace. |
| PulseStabilityFrequencyErrorCompensation | 12587145 | Specifies whether to compute and correct the frequency offset for stability results computation. This is an optional setting and in negligible frequency error condition you must set this method to Off to avoid incorrect results. |
| PulseTimeSidelobeEnabled | 12587239 | Specifies whether to enable pulse time sidelobe results computation. |
| PulseTimeSidelobeReferenceWindowType | 12587240 | Specifies the window type to be applied to the reference pulse to obtain correlated output for the time sidelobe measurements. |
| PulseTimeSidelobeKeepOutTimeAuto | 12587241 | Specifies whether the keep out time computation for the time sidelobe measurements is automatic or manual. |
| PulseTimeSidelobeKeepOutTime | 12587242 | Specifies keep out time for the time sidelobe measurements. |
| PulseTimeSidelobeMinimumCorrelation | 12587243 | Specifies the minimum peak correlation value for the time sidelobe measurements. |
| PulseAllTracesEnabled | 12587022 | Specifies whether to enable storing and retrieving traces after performing the measurements. |
| PulseAcquisitionTraceSelect | 12587278 | Specifies the mode to select all pulses or the subset of acquired pulses available for display acquisition trace, limited to MaximumPulseCountEnabled method if set to True. |
| PulseAcquisitionTraceSubsetOffset | 12587279 | Specifies the offset in number of pulses to be used for display acquisition trace. You must configure this method when you set the PulseAcquisitionTraceSelect method to Subset. |
| PulseAcquisitionTraceSubsetLength | 12587280 | Specifies the total number of pulses starting from offset to be used for display acquisition trace. You must configure this method when you set the PulseAcquisitionTraceSelect method to Subset. Set length to 0 to disable the acquisition trace. |
| PulseTraceRangeAuto | 12587272 | Specifies whether the trace range computation of the selected pulse is automatic or manually configured by you. |
| PulseTraceRangeReference | 12587273 | Specifies the reference point for positioning of trace range. You can set reference point based on reference and Pulse Trace Range Offset (s) value. |
| PulseTraceRangeOffset | 12587274 | Specifies the time offset in seconds from the reference point to position the trace range. |
| PulseTraceRangeLength | 12587275 | Specifies the length in seconds of the trace range centered at the reference point. |
| PulseSelectedBurstTrace | 12587232 | Specifies the burst number selected for the display of traces. This method is applicable for IQ, amplitude and pulse stability traces. |
| PulseSelectedPulseTrace | 12587153 | Specifies the pulse number selected for displaying the traces. This method is valid only for IQ, amplitude and pulse stability traces. |
| PulseAmplitudeTraceUnit | 12587228 | Specifies the unit of the amplitude level. This method is applicable only for the amplitude and acquired amplitude trace. |
| PulseNumberOfAnalysisThreads | 12587144 | Specifies the maximum number of threads used for parallelism for the pulse measurement. |
| PulseResultsPulseCount | 12587023 | Returns the measured pulse count. |
| PulseResultsBurstIndex | 12587233 | Returns the burst indices of all the measured pulses. |
| PulseResultsPulsePositionIndex | 12587234 | Returns the position indices of all the measured pulses within a burst. |
| PulseResultsTopLevel | 12587024 | Returns the top levels for all measured pulses. The values are expressed in dBm. |
| PulseResultsTopLevelMean | 12587025 | Returns the mean of the top levels across the measured pulses. This value is expressed in dBm. |
| PulseResultsTopLevelMaximum | 12587026 | Returns the maximum top level across the measured pulses. This value is expressed in dBm. |
| PulseResultsTopLevelMinimum | 12587027 | Returns the minimum top level across the measured pulses. This value is expressed in dBm. |
| PulseResultsTopLevelStandardDeviation | 12587028 | Returns the standard deviation of the top levels across the measured pulses. This value is expressed in dBm. |
| PulseResultsBaseLevel | 12587029 | Returns the base levels for all measured pulses. The values are expressed in dBm. |
| PulseResultsBaseLevelMean | 12587030 | Returns the mean of the base levels across the measured pulses. This value is expressed in dBm. |
| PulseResultsBaseLevelMaximum | 12587031 | Returns the maximum base level across the measured pulses. This value is expressed in dBm. |
| PulseResultsBaseLevelMinimum | 12587032 | Returns the minimum base level across the measured pulses. This value is expressed in dBm. |
| PulseResultsBaseLevelStandardDeviation | 12587033 | Returns the standard deviation of the base levels across the measured pulses. This value is expressed in dBm. |
| PulseResultsAverageOnLevel | 12587034 | Returns the average power levels during the ON duration for all measured pulses. The values are expressed in dBm. |
| PulseResultsAverageOnLevelMean | 12587035 | Returns the mean of the average power levels during the ON duration across the measured pulses. This value is expressed in dBm. |
| PulseResultsAverageOnLevelMaximum | 12587036 | Returns the maximum average power level during the ON duration across the measured pulses. This value is expressed in dBm. |
| PulseResultsAverageOnLevelMinimum | 12587037 | Returns the minimum average power level during the ON duration across the measured pulses. This value is expressed in dBm. |
| PulseResultsAverageOnLevelStandardDeviation | 12587038 | Returns the standard deviation of the average power levels during the ON duration across the measured pulses. This value is expressed in dBm. |
| PulseResultsPeakLevel | 12587039 | Returns the peak power levels during the pulse period for all measured pulses. The values are expressed in dBm. |
| PulseResultsPeakLevelMean | 12587040 | Returns the mean of the peak power levels during the pulse period across the measured pulses. This value is expressed in dBm. |
| PulseResultsPeakLevelMaximum | 12587041 | Returns the maximum peak power level during the pulse period across the measured pulses. This value is expressed in dBm. |
| PulseResultsPeakLevelMinimum | 12587042 | Returns the minimum peak power level during the pulse period across the measured pulses. This value is expressed in dBm. |
| PulseResultsPeakLevelStandardDeviation | 12587043 | Returns the standard deviation of the peak power levels during the pulse period across the measured pulses. This value is expressed in dBm. |
| PulseResultsAverageLevel | 12587044 | Returns the average power levels during the pulse period for all measured pulses. The values are expressed in dBm. |
| PulseResultsAverageLevelMean | 12587045 | Returns the mean of the average power levels during the pulse period across the measured pulses. This value is expressed in dBm. |
| PulseResultsAverageLevelMaximum | 12587046 | Returns the maximum average power level during the pulse period across the measured pulses. This value is expressed in dBm. |
| PulseResultsAverageLevelMinimum | 12587047 | Returns the minimum average power level during the pulse period across the measured pulses. This value is expressed in dBm. |
| PulseResultsAverageLevelStandardDeviation | 12587048 | Returns the standard deviation of the average power levels during the pulse period across the measured pulses. This value is expressed in dBm. |
| PulseResultsOvershoot | 12587049 | Returns the overshoot values computed for all measured pulses. The overshoot value is defined as the ratio of height of the local peak after a rising edge to the pulse amplitude. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| PulseResultsOvershootMean | 12587050 | Returns the mean of the overshoot values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| PulseResultsOvershootMaximum | 12587051 | Returns the maximum of overshoot values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| PulseResultsOvershootMinimum | 12587052 | Returns the minimum of overshoot values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| PulseResultsOvershootStandardDeviation | 12587053 | Returns the standard deviation of the overshoot values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| PulseResultsDroop | 12587054 | Returns the droop values computed for all measured pulses. Droop values are defined as the rate at which the pulse top levels decays from the beginning to the end during On duration. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| PulseResultsDroopMean | 12587055 | Returns the mean of the droop values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| PulseResultsDroopMaximum | 12587056 | Returns the maximum of droop values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| PulseResultsDroopMinimum | 12587057 | Returns the minimum of droop values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| PulseResultsDroopStandardDeviation | 12587058 | Returns the standard deviation of the droop values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| PulseResultsRipple | 12587059 | Returns the ripple values computed for all measured pulses. Ripple values are the difference between the maximum and minimum deviation from the pulse top reference. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| PulseResultsRippleMean | 12587060 | Returns the mean of the ripple values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| PulseResultsRippleMaximum | 12587061 | Returns the maximum of ripple values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| PulseResultsRippleMinimum | 12587062 | Returns the minimum of ripple values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| PulseResultsRippleStandardDeviation | 12587063 | Returns the standard deviation of the ripple values computed for all measured pulses. This value is expressed in units specified by SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) method. |
| PulseResultsRiseTime | 12587064 | Returns the rise time for all measured pulses. Rise time is the difference between the time when the pulse exceeds the lower and upper thresholds. This value is expressed in seconds. |
| PulseResultsRiseTimeMean | 12587065 | Returns the mean of the rise time values across the measured pulses. This value is expressed in seconds. |
| PulseResultsRiseTimeMaximum | 12587066 | Returns the maximum rise time across the measured pulses. This value is expressed in seconds. |
| PulseResultsRiseTimeMinimum | 12587067 | Returns the minimum rise time across the measured pulses. This value is expressed in seconds. |
| PulseResultsRiseTimeStandardDeviation | 12587068 | Returns the standard deviation of the rise time values across the measured pulses. This value is expressed in seconds. |
| PulseResultsRiseEdge | 12587276 | Returns the rise edge for all measured pulses. Rise edge is the absolute time instant when the pulse exceeds the rising edge lower threshold. This value is expressed in seconds. |
| PulseResultsFallTime | 12587069 | Returns the fall time for all measured pulses. Fall time is the difference between the time when the pulse drops below the upper and lower thresholds. This value is expressed in seconds. |
| PulseResultsFallTimeMean | 12587070 | Returns the mean of the fall time values across the measured pulses. This value is expressed in seconds. |
| PulseResultsFallTimeMaximum | 12587071 | Returns the maximum fall time across the measured pulses. This value is expressed in seconds. |
| PulseResultsFallTimeMinimum | 12587072 | Returns the minimum fall time across the measured pulses. This value is expressed in seconds. |
| PulseResultsFallTimeStandardDeviation | 12587073 | Returns the standard deviation of the fall time values across the measured pulses. This value is expressed in seconds. |
| PulseResultsFallEdge | 12587277 | Returns the fall edge for all measured pulses. Fall edge is the absolute time instant when the pulse exceeds the falling edge width threshold. This value is expressed in seconds. |
| PulseResultsPulseWidth | 12587074 | Returns the ON duration for all measured pulses. ON duration value is the duration of the pulse for the first rising-edge and the subsequent falling-edge transition at width threshold. This value is expressed in seconds. |
| PulseResultsPulseWidthMean | 12587075 | Returns the mean of the ON duration values across the measured pulses. This value is expressed in seconds. |
| PulseResultsPulseWidthMaximum | 12587076 | Returns the maximum ON duration across the measured pulses. This value is expressed in seconds. |
| PulseResultsPulseWidthMinimum | 12587077 | Returns the minimum ON duration across the measured pulses. This value is expressed in seconds. |
| PulseResultsPulseWidthStandardDeviation | 12587078 | Returns the standard deviation of ON duration values across the measured pulses. This value is expressed in seconds. |
| PulseResultsPulseOffDuration | 12587079 | Returns the OFF duration values for all measured pulses. OFF duration value is the duration of the pulse for the first falling-edge and the subsequent rising-edge transition at width threshold. This value is expressed in seconds. |
| PulseResultsPulseOffDurationMean | 12587080 | Returns the mean of the OFF duration values across the measured pulses. This value is expressed in seconds. |
| PulseResultsPulseOffDurationMaximum | 12587081 | Returns the maximum OFF duration across the measured pulses. This value is expressed in seconds. |
| PulseResultsPulseOffDurationMinimum | 12587082 | Returns the minimum OFF duration across the measured pulses. This value is expressed in seconds. |
| PulseResultsPulseOffDurationStandardDeviation | 12587083 | Returns the standard deviation of OFF duration values across the measured pulses. This value is expressed in seconds. |
| PulseResultsDutyCycle | 12587084 | Returns the duty cycle values for all measured pulses. Duty cycle is the ratio of pulse ON duration to the pulse period. This value is expressed as a percentage. |
| PulseResultsDutyCycleMean | 12587085 | Returns the mean of duty cycle values across the measured pulses. This value is expressed as a percentage. |
| PulseResultsDutyCycleMaximum | 12587086 | Returns the maximum duty cycle across the measured pulses. This value is expressed as a percentage. |
| PulseResultsDutyCycleMinimum | 12587087 | Returns the minimum duty cycle across the measured pulses. This value is expressed as a percentage. |
| PulseResultsDutyCycleStandardDeviation | 12587088 | Returns the standard deviation of duty cycle values across the measured pulses. This value is expressed as a percentage. |
| PulseResultsPulseRepetitionInterval | 12587089 | Returns the pulse period values for all measured pulses. Period values are the time difference between two consecutive transitions of the same polarity, either positive or negative, where the transitions occur at crossings of the width threshold.This value is expressed in seconds. |
| PulseResultsPulseRepetitionIntervalMean | 12587090 | Returns the mean of pulse period values across the measured pulses. This value is expressed in seconds. |
| PulseResultsPulseRepetitionIntervalMaximum | 12587091 | Returns the maximum pulse period across the measured pulses. This value is expressed in seconds. |
| PulseResultsPulseRepetitionIntervalMinimum | 12587092 | Returns the minimum pulse period across the measured pulses. This value is expressed in seconds. |
| PulseResultsPulseRepetitionIntervalStandardDeviation | 12587093 | Returns the standard deviation of pulse period values across the measured pulses. This value is expressed in seconds. |
| PulseResultsAveragePhase | 12587099 | Returns the average phase for all measured pulses. This value is expressed in degrees. |
| PulseResultsAveragePhaseMean | 12587100 | Returns the mean of the average phase across the measured pulses. This value is expressed in degrees. |
| PulseResultsAveragePhaseMaximum | 12587101 | Returns the maximum average phase across the measured pulses. This value is expressed in degrees. |
| PulseResultsAveragePhaseMinimum | 12587102 | Returns the minimum average phase across the measured pulses. This value is expressed in degrees. |
| PulseResultsAveragePhaseStandardDeviation | 12587103 | Returns the standard deviation of the average phase across the measured pulses. This value is expressed in degrees. |
| PulseResultsPulseToPulsePhaseDifference | 12587160 | Returns the phase difference of the pulses with respect to the phase of the first pulse. This value is expressed in degrees. |
| PulseResultsPulseToPulsePhaseDifferenceMean | 12587105 | Returns the mean of the pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees. |
| PulseResultsPulseToPulsePhaseDifferenceMaximum | 12587106 | Returns the maximum pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees. |
| PulseResultsPulseToPulsePhaseDifferenceMinimum | 12587107 | Returns the minimum pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees. |
| PulseResultsPulseToPulsePhaseDifferenceStandardDeviation | 12587108 | Returns the standard deviation of the pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees. |
| PulseResultsPhaseDeviation | 12587109 | Returns the peak-to-peak phase deviation for all measured pulses. This value is expressed in degrees. |
| PulseResultsPhaseDeviationMean | 12587110 | Returns the mean of the peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees. |
| PulseResultsPhaseDeviationMaximum | 12587111 | Returns the maximum peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees. |
| PulseResultsPhaseDeviationMinimum | 12587112 | Returns the minimum peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees. |
| PulseResultsPhaseDeviationStandardDeviation | 12587113 | Returns the standard deviation of the peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees. |
| PulseResultsPhaseErrorRms | 12587166 | Returns the RMS phase error for all measured pulses. This value is expressed in degrees. |
| PulseResultsPhaseErrorRmsMean | 12587167 | Returns the mean of the RMS phase error across the measured pulses. This value is expressed in degrees. |
| PulseResultsPhaseErrorRmsMaximum | 12587168 | Returns the maximum RMS phase error across the measured pulses. This value is expressed in degrees. |
| PulseResultsPhaseErrorRmsMinimum | 12587169 | Returns the minimum RMS phase error across the measured pulses. This value is expressed in degrees. |
| PulseResultsPhaseErrorRmsStandardDeviation | 12587170 | Returns the standard deviation of the RMS phase errors across the measured pulses. This value is expressed in degrees. |
| PulseResultsPhaseErrorPeak | 12587171 | Returns the peak phase error for all measured pulses. This value is expressed in degrees. |
| PulseResultsPhaseErrorPeakMean | 12587172 | Returns the mean of the peak phase error across the measured pulses. This value is expressed in degrees. |
| PulseResultsPhaseErrorPeakMaximum | 12587173 | Returns the maximum peak phase error across the measured pulses. This value is expressed in degrees. |
| PulseResultsPhaseErrorPeakMinimum | 12587174 | Returns the minimum peak phase error across the measured pulses. This value is expressed in degrees. |
| PulseResultsPhaseErrorPeakStandardDeviation | 12587175 | Returns the standard deviation of the peak phase error across the measured pulses. This value is expressed in degrees. |
| PulseResultsPhaseErrorPeakLocation | 12587176 | Returns the time locations corresponding to the peak phase error for all measured pulses. This value is expressed in seconds. |
| PulseResultsAverageFrequency | 12587114 | Returns the average frequencie for all measured pulses. This value is expressed in Hz. |
| PulseResultsAverageFrequencyMean | 12587115 | Returns the mean of the average frequency across the measured pulses. This value is expressed in Hz. |
| PulseResultsAverageFrequencyMaximum | 12587116 | Returns the maximum average frequency across the measured pulses. This value is expressed in Hz. |
| PulseResultsAverageFrequencyMinimum | 12587117 | Returns the minimum average frequency across the measured pulses. This value is expressed in Hz. |
| PulseResultsAverageFrequencyStandardDeviation | 12587118 | Returns the standard deviation of the average frequency across the measured pulses. This value is expressed in Hz. |
| PulseResultsPulseToPulseFrequencyDifference | 12587119 | Returns the frequency difference of the pulses with respect to the frequency of the first pulse. This value is expressed in Hz. |
| PulseResultsPulseToPulseFrequencyDifferenceMean | 12587120 | Returns the mean of the pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz. |
| PulseResultsPulseToPulseFrequencyDifferenceMaximum | 12587121 | Returns the maximum pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz. |
| PulseResultsPulseToPulseFrequencyDifferenceMinimum | 12587122 | Returns the minimum pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz. |
| PulseResultsPulseToPulseFrequencyDifferenceStandardDeviation | 12587123 | Returns the standard deviation of the pulse-to-pulse frequency difference across the measured pulses. This value is expressed in Hz. |
| PulseResultsFrequencyDeviation | 12587124 | Returns the peak-to-peak frequency deviation for all measured pulses. This value is expressed in Hz. |
| PulseResultsFrequencyDeviationMean | 12587125 | Returns the mean of the peak-to-peak phase deviation across the measured pulses. This value is expressed in Hz. |
| PulseResultsFrequencyDeviationMaximum | 12587126 | Returns the maximum peak-to-peak phase deviation across the measured pulses. This value is expressed in Hz. |
| PulseResultsFrequencyDeviationMinimum | 12587127 | Returns the minimum peak-to-peak frequency deviation across the measured pulses. This value is expressed in Hz. |
| PulseResultsFrequencyDeviationStandardDeviation | 12587128 | Returns the standard deviation of the peak-to-peak frequency deviation across the measured pulses. This value is expressed in Hz. |
| PulseResultsFrequencyErrorRms | 12587177 | Returns the RMS frequency error for all measured pulses. This value is expressed in Hz. |
| PulseResultsFrequencyErrorRmsMean | 12587178 | Returns the mean of the RMS frequency error across the measured pulses. This value is expressed in Hz. |
| PulseResultsFrequencyErrorRmsMaximum | 12587179 | Returns the maximum RMS frequency error across the measured pulses. This value is expressed in Hz. |
| PulseResultsFrequencyErrorRmsMinimum | 12587180 | Returns the minimum RMS frequency error across the measured pulses. This value is expressed in Hz. |
| PulseResultsFrequencyErrorRmsStandardDeviation | 12587181 | Returns the standard deviation of the RMS frequency error across the measured pulses. This value is expressed in Hz. |
| PulseResultsFrequencyErrorPeak | 12587182 | Returns the peak frequency error for all measured pulses. This value is expressed in Hz. |
| PulseResultsFrequencyErrorPeakMean | 12587183 | Returns the mean of the peak frequency error across the measured pulses. This value is expressed in Hz. |
| PulseResultsFrequencyErrorPeakMaximum | 12587184 | Returns the maximum peak frequency error across the measured pulses. This value is expressed in Hz. |
| PulseResultsFrequencyErrorPeakMinimum | 12587185 | Returns the minimum peak frequency error across the measured pulses. This value is expressed in Hz. |
| PulseResultsFrequencyErrorPeakStandardDeviation | 12587186 | Returns the standard deviation of the peak frequency error across the measured pulses. This value is expressed in Hz. |
| PulseResultsFrequencyErrorPeakLocation | 12587187 | Returns the time locations corresponding to the peak frequency error of the measured pulses. This value is expressed in seconds. |
| PulseResultsFMChirpRate | 12587188 | Returns the frequency slope rate of a best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for each pulse. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation. |
| PulseResultsFMChirpRateMean | 12587189 | Returns the mean of the FM chirp rates across the measured pulses. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation. |
| PulseResultsFMChirpRateMaximum | 12587190 | Returns the maximum FM chirp rate across the measured pulses. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation. |
| PulseResultsFMChirpRateMinimum | 12587191 | Returns the minimum FM chirp rate across the measured pulses. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation. |
| PulseResultsFMChirpRateStandardDeviation | 12587192 | Returns the standard deviation of the FM chirp rates across the measured pulses. This value is expressed in Hz/us.This result is valid for linear FM and triangular FM modulation. |
| PulseResultsFMChirpStartFrequency | 12587193 | Returns the start frequencies of the best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |
| PulseResultsFMChirpStartFrequencyMean | 12587194 | Returns the mean of the FM chirp start frequency across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |
| PulseResultsFMChirpStartFrequencyMaximum | 12587195 | Returns the maximum FM chirp start frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |
| PulseResultsFMChirpStartFrequencyMinimum | 12587196 | Returns the minimum FM chirp start frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |
| PulseResultsFMChirpStartFrequencyStandardDeviation | 12587197 | Returns the FM chirp start frequency standard deviation across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |
| PulseResultsFMChirpStopFrequency | 12587198 | Returns the stop frequencies of the best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |
| PulseResultsFMChirpStopFrequencyMean | 12587199 | Returns the mean of the FM chirp stop frequency across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |
| PulseResultsFMChirpStopFrequencyMaximum | 12587200 | Returns the maximum FM chirp stop frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |
| PulseResultsFMChirpStopFrequencyMinimum | 12587201 | Returns the minimum FM chirp stop frequency among the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |
| PulseResultsFMChirpStopFrequencyStandardDeviation | 12587202 | Returns the FM chirp stop frequency standard deviation across the measured pulses. This value is expressed in Hz. This result is valid for linear FM and triangular FM modulation. |
| PulseResultsFMChirpRate2 | 12587213 | Returns the frequency slope rate of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for the measured pulses. This value is expressed in Hz/us.This result is valid only for triangular FM modulation. |
| PulseResultsFMChirpRate2Mean | 12587214 | Returns the mean of the FM chirp rate2 values across the measured pulses. This value is expressed in Hz/us.This result is valid only for triangular FM modulation. |
| PulseResultsFMChirpRate2Maximum | 12587215 | Returns the maximum FM chirp rate2 value across the measured pulses. This value is expressed in Hz/us.This result is valid only for triangular FM modulation. |
| PulseResultsFMChirpRate2Minimum | 12587216 | Returns the minimum FM chirp rate2 value across the measured pulses. This value is expressed in Hz/us.This result is valid only for triangular FM modulation. |
| PulseResultsFMChirpRate2StandardDeviation | 12587217 | Returns the standard deviation of the FM chirp rate2 values across the measured pulses. This value is expressed in Hz/us.This result is valid only for triangular FM modulation. |
| PulseResultsFMChirpStartFrequency2 | 12587218 | Returns the start frequency of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |
| PulseResultsFMChirpStartFrequency2Mean | 12587219 | Returns the mean of the FM chirp start frequency2 across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |
| PulseResultsFMChirpStartFrequency2Maximum | 12587220 | Returns the maximum FM chirp start frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |
| PulseResultsFMChirpStartFrequency2Minimum | 12587221 | Returns the minimum FM chirp start frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |
| PulseResultsFMChirpStartFrequency2StandardDeviation | 12587222 | Returns the FM chirp start frequency2 standard deviation across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |
| PulseResultsFMChirpStopFrequency2 | 12587223 | Returns the stop frequency of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by Pulse Freq Phase Dev Range Length (%) method for the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |
| PulseResultsFMChirpStopFrequency2Mean | 12587224 | Returns the mean of the FM chirp stop frequency2 across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |
| PulseResultsFMChirpStopFrequency2Maximum | 12587225 | Returns the maximum FM chirp stop frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |
| PulseResultsFMChirpStopFrequency2Minimum | 12587226 | Returns the minimum FM chirp stop frequency2 among the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |
| PulseResultsFMChirpStopFrequency2StandardDeviation | 12587227 | Returns the FM chirp stop frequency2 standard deviation across the measured pulses. This value is expressed in Hz. This result is valid only for triangular FM modulation. |
| PulseResultsAverageAmplitudeStability | 12587157 | Returns the average amplitude stability over the measured pulses. This value is expressed in dB.The stability is computed as the variance of the amplitude over the measured pulses. |
| PulseResultsAveragePhaseStability | 12587158 | Returns the average phase stability over the measured pulses. This value is expressed in dB.The stability is computed as the variance of the phase over the measured pulses. |
| PulseResultsAverageTotalStability | 12587159 | Returns the average total stability over measured pulses. This value is expressed in dB. |
| PulseResultsAmplitudeStability | 12587129 | Returns the amplitude stability of the measured pulses. This value is expressed in dB.This value is computed as the deviation of amplitude from the reference. |
| PulseResultsAmplitudeStabilityMean | 12587130 | Returns the mean of the amplitude stability values across the measured pulses. This value is expressed in dB. |
| PulseResultsAmplitudeStabilityMaximum | 12587131 | Returns the maximum amplitude stability across the measured pulses. This value is expressed in dB. |
| PulseResultsAmplitudeStabilityMinimum | 12587132 | Returns the minimum amplitude stability across the measured pulses. This value is expressed in dB. |
| PulseResultsAmplitudeStabilityStandardDeviation | 12587133 | Returns the amplitude stability standard deviation across the measured pulses. This value is expressed in dB. |
| PulseResultsPhaseStability | 12587134 | Returns the phase stability of the measured pulses. This value is expressed in dB.This value is computed as the deviation of phase from the reference. |
| PulseResultsPhaseStabilityMean | 12587135 | Returns the mean of the phase stability values across the measured pulses. This value is expressed in dB. |
| PulseResultsPhaseStabilityMaximum | 12587136 | Returns the maximum phase stability across the measured pulses. This value is expressed in dB. |
| PulseResultsPhaseStabilityMinimum | 12587137 | Returns the minimum phase stability across the measured pulses. This value is expressed in dB. |
| PulseResultsPhaseStabilityStandardDeviation | 12587138 | Returns the phase stability standard deviation across the measured pulses. This value is expressed in dB. |
| PulseResultsTotalStability | 12587139 | Returns the total stability of the measured pulses. This value is expressed in dB. |
| PulseResultsTotalStabilityMean | 12587140 | Returns the mean of the total stability values across the measured pulses. This value is expressed in dB. |
| PulseResultsTotalStabilityMaximum | 12587141 | Returns the maximum total stability across the measured pulses. This value is expressed in dB. |
| PulseResultsTotalStabilityMinimum | 12587142 | Returns the minimum total stability across the measured pulses. This value is expressed in dB. |
| PulseResultsTotalStabilityStandardDeviation | 12587143 | Returns the total stability standard deviation across the measured pulses. This value is expressed in dB. |
| PulseResultsTimeSidelobeMainlobeWidth | 12587244 | Returns the mainlobe width for all measured pulses. Mainlobe width is the width at 3dB below from its peak level. This value is expressed in seconds. |
| PulseResultsTimeSidelobeMainlobeWidthMean | 12587245 | Returns the mean of the mainlobe width values across the measured pulses. This value is expressed in seconds. |
| PulseResultsTimeSidelobeMainlobeWidthMaximum | 12587246 | Returns the maximum mainlobe width across the measured pulses. This value is expressed in seconds. |
| PulseResultsTimeSidelobeMainlobeWidthMinimum | 12587247 | Returns the minimum mainlobe width across the measured pulses. This value is expressed in seconds. |
| PulseResultsTimeSidelobeMainlobeWidthStandardDeviation | 12587248 | Returns the standard deviation of the mainlobe width values across the measured pulses. This value is expressed in seconds. |
| PulseResultsTimeSidelobeDelay | 12587249 | Returns the sidelobe delay for all measured pulses. Sidelobe delay is the time elapsed between the highest sidelobe peak and mainlobe peak level. This value is expressed in seconds. |
| PulseResultsTimeSidelobeDelayMean | 12587250 | Returns the mean of the sidelobe delay values across the measured pulses. This value is expressed in seconds. |
| PulseResultsTimeSidelobeDelayMaximum | 12587251 | Returns the maximum sidelobe delay across the measured pulses. This value is expressed in seconds. |
| PulseResultsTimeSidelobeDelayMinimum | 12587252 | Returns the minimum sidelobe delay across the measured pulses. This value is expressed in seconds. |
| PulseResultsTimeSidelobeDelayStandardDeviation | 12587253 | Returns the standard deviation of the sidelobe delay values across the measured pulses. This value is expressed in seconds. |
| PulseResultsTimeSidelobePeakSidelobeLevel | 12587254 | Returns the peak sidelobe level for all measured pulses. Peak sidelobe level is the ratio of the highest sidelobe peak to the mainlobe peak level. This value is expressed in dB. |
| PulseResultsTimeSidelobePeakSidelobeLevelMean | 12587255 | Returns the mean of the peak sidelobe level values across the measured pulses. This value is expressed in dB. |
| PulseResultsTimeSidelobePeakSidelobeLevelMaximum | 12587256 | Returns the maximum peak sidelobe level across the measured pulses. This value is expressed in seconds. |
| PulseResultsTimeSidelobePeakSidelobeLevelMinimum | 12587257 | Returns the minimum peak sidelobe level across the measured pulses. This value is expressed in dB. |
| PulseResultsTimeSidelobePeakSidelobeLevelStandardDeviation | 12587258 | Returns the standard deviation of the peak sidelobe level values across the measured pulses. This value is expressed in dB. |
| PulseResultsTimeSidelobeCompressionRatio | 12587259 | Returns the compression ratio for all measured pulses. Compression ratio is the ratio of the mainlobe width to the pulse width. This value is expressed as a percentage. |
| PulseResultsTimeSidelobeCompressionRatioMean | 12587260 | Returns the mean of the compression ratio values across the measured pulses. This value is expressed as a percentage. |
| PulseResultsTimeSidelobeCompressionRatioMaximum | 12587261 | Returns the maximum compression ratio across the measured pulses. This value is expressed as a percentage. |
| PulseResultsTimeSidelobeCompressionRatioMinimum | 12587262 | Returns the minimum compression ratio across the measured pulses. This value is expressed as a percentage. |
| PulseResultsTimeSidelobeCompressionRatioStandardDeviation | 12587263 | Returns the standard deviation of the compression ratio values across the measured pulses. This value is expressed as a percentage. |
| PulseResultsTimeSidelobePeakCorrelation | 12587264 | Returns the peak correlation for all measured pulses. Peak correlation is the normalized peak power of the correlated output by both measured and reference pulse powers. This values ranges in between 0 to 1. |
| PulseResultsTimeSidelobePeakCorrelationMean | 12587265 | Returns the mean of the peak correlation values across the measured pulses. |
| PulseResultsTimeSidelobePeakCorrelationMaximum | 12587266 | Returns the maximum peak correlation across the measured pulses. |
| PulseResultsTimeSidelobePeakCorrelationMinimum | 12587267 | Returns the minimum peak correlation across the measured pulses. |
| PulseResultsTimeSidelobePeakCorrelationStandardDeviation | 12587268 | Returns the standard deviation of the peak correlation values across the measured pulses. |
| AutoLevelInitialReferenceLevel | 12582925 | Specifies the initial reference level, in dBm, which the AutoLevel(string, double, double, out double) function uses to estimate the peak power of the input signal. |
| ResultFetchTimeout | 12632064 | Specifies the wait time before results are available in the RFmx Property. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxPulse Property Node waits until the measurement is complete. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulse-configuration.html language=enus -->
## TOPIC 00132: Configuration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulse-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulse-configuration.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxPulseMXPulseConfiguration instance that provides methods to configure the Pulse measurement. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic RFmxPulseMXPulseConfiguration Configuration { get; }

### Configuration

Gets the [RFmxPulseMXPulseConfiguration](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration.html) instance that provides methods to configure the Pulse measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public [RFmxPulseMXPulseConfiguration](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration.html) Configuration { get; }

Parent topic:

RFmxPulseMXPulse Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulse-results.html language=enus -->
## TOPIC 00133: Results

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulse-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulse-results.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxPulseMXPulseResults instance that provides methods to fetch and read the Pulse measurement results. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic RFmxPulseMXPulseResults Results { get; }

### Results

Gets the [RFmxPulseMXPulseResults](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults.html) instance that provides methods to fetch and read the Pulse measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public [RFmxPulseMXPulseResults](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseresults.html) Results { get; }

Parent topic:

RFmxPulseMXPulse Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulse.html language=enus -->
## TOPIC 00134: RFmxPulseMXPulse Class

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulse.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulse.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Pulse measurement. Derives fromRFmxPulseMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic class RFmxPulseMXPulse : RFmxPulseMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxPulseMXPulseConfiguration instance that provides methods to configure the Pulse me

### RFmxPulseMXPulse Class

Represents the Pulse measurement.

#### Derives from

- RFmxPulseMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public class RFmxPulseMXPulse : RFmxPulseMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxPulseMXPulseConfiguration instance that provides methods to configure the Pulse measurement. |
| Results | Gets the RFmxPulseMXPulseResults instance that provides methods to fetch and read the Pulse measurement results. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseacquisitiontraceselect.html language=enus -->
## TOPIC 00135: RFmxPulseMXPulseAcquisitionTraceSelect Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseacquisitiontraceselect.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseacquisitiontraceselect.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the mode to select all pulses or the subset of acquired pulses available for display acquisition trace, limited to MaximumPulseCountEnabled method if set to True. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXPulseAcquisitionTraceSelectMembersNameValueDescriptionA

### RFmxPulseMXPulseAcquisitionTraceSelect Enumeration

Specifies the mode to select all pulses or the subset of acquired pulses available for display acquisition trace, limited to [MaximumPulseCountEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method if set to [True](nationalinstruments-rfmx-pulsemx-rfmxpulsemxmaximumpulsecountenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXPulseAcquisitionTraceSelect

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AllPulses | 0 | Selects all the acquired pulses. |
| Subset | 1 | Selects subset of the acquired pulses. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseamplitudeleveldomain.html language=enus -->
## TOPIC 00136: RFmxPulseMXPulseAmplitudeLevelDomain Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseamplitudeleveldomain.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseamplitudeleveldomain.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether voltage or power to be used as domain for pulse measurements. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXPulseAmplitudeLevelDomainMembersNameValueDescriptionVolts0All threshold levels are calculated in the voltage domain. Watts1All threshold levels are

### RFmxPulseMXPulseAmplitudeLevelDomain Enumeration

Specifies whether voltage or power to be used as domain for pulse measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXPulseAmplitudeLevelDomain

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Volts | 0 | All threshold levels are calculated in the voltage domain. |
| Watts | 1 | All threshold levels are calculated in the power domain. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseamplitudetraceunit.html language=enus -->
## TOPIC 00137: RFmxPulseMXPulseAmplitudeTraceUnit Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseamplitudetraceunit.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseamplitudetraceunit.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the unit of the amplitude level. This method is applicable only for the amplitude and acquired amplitude trace. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXPulseAmplitudeTraceUnitMembersNameValueDescriptiondBm0Amplitude trace is expressed in dBm. Volts1Amplitude

### RFmxPulseMXPulseAmplitudeTraceUnit Enumeration

Specifies the unit of the amplitude level. This method is applicable only for the amplitude and acquired amplitude trace.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXPulseAmplitudeTraceUnit

#### Members

| Name | Value | Description |
| --- | --- | --- |
| dBm | 0 | Amplitude trace is expressed in dBm. |
| Volts | 1 | Amplitude trace is expressed in Volts. |
| Watts | 2 | Amplitude trace is expressed in Watts. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-configure1referencewaveform__string-complexwaveform_complexsingle..html language=enus -->
## TOPIC 00138: Configure1ReferenceWaveform(string, ComplexWaveform< ComplexSingle >)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-configure1referencewaveform__string-complexwaveform_complexsingle..html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-configure1referencewaveform__string-complexwaveform_complexsingle..html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference pulse waveform used for time sidelobe measurements. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int Configure1ReferenceWaveform(string selectorString, ComplexWaveform< ComplexSingle > referenceWaveform)ParametersNameTypeDescriptionselectorStringstringSpecifies a

### Configure1ReferenceWaveform(string, ComplexWaveform< ComplexSingle >)

Configures the reference pulse waveform used for time sidelobe measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int Configure1ReferenceWaveform(string selectorString, ComplexWaveform< ComplexSingle > referenceWaveform)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""""result::r1" |
| referenceWaveform | ComplexWaveform< ComplexSingle > | specifies the reference waveform used for correlation computation in time sidelobe Measurements. The default value is an empty waveform. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getacquisitiontraceselect__string-out.html language=enus -->
## TOPIC 00139: GetAcquisitionTraceSelect(string, out RFmxPulseMXPulseAcquisitionTraceSelect)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getacquisitiontraceselect__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getacquisitiontraceselect__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mode to select all pulses or the subset of acquired pulses available for display acquisition trace, limited to MaximumPulseCountEnabled method if set to True. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAcquisitionTraceSelect(string selectorString, out RFmxPulseMXPulseAcq

### GetAcquisitionTraceSelect(string, out RFmxPulseMXPulseAcquisitionTraceSelect)

Gets the mode to select all pulses or the subset of acquired pulses available for display acquisition trace, limited to [MaximumPulseCountEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method if set to [True](nationalinstruments-rfmx-pulsemx-rfmxpulsemxmaximumpulsecountenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAcquisitionTraceSelect(string selectorString, out RFmxPulseMXPulseAcquisitionTraceSelect value)

#### Remarks

This method gets the value of [PulseAcquisitionTraceSelect](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [Subset](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseacquisitiontraceselect.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXPulseAcquisitionTraceSelect | Upon return, contains the mode to select all pulses or the subset of acquired pulses available for display acquisition trace, limited to MaximumPulseCountEnabled method if set to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getacquisitiontracesubsetlength__string-out.html language=enus -->
## TOPIC 00140: GetAcquisitionTraceSubsetLength(string, out int)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getacquisitiontracesubsetlength__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getacquisitiontracesubsetlength__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the total number of pulses starting from offset to be used for display acquisition trace. You must configure this method when you set the PulseAcquisitionTraceSelect method to Subset. Set length to 0 to disable the acquisition trace. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int G

### GetAcquisitionTraceSubsetLength(string, out int)

Gets the total number of pulses starting from offset to be used for display acquisition trace. You must configure this method when you set the [PulseAcquisitionTraceSelect](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [Subset](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseacquisitiontraceselect.html). Set length to 0 to disable the acquisition trace.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAcquisitionTraceSubsetLength(string selectorString, out int value)

#### Remarks

This method gets the value of [PulseAcquisitionTraceSubsetLength](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 10. Valid values are 0 to 10000, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the total number of pulses starting from offset to be used for display acquisition trace. You must configure this method when you set the PulseAcquisitionTraceSelect method to Subset. Set length to 0 to disable the acquisition trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getacquisitiontracesubsetoffset__string-out.html language=enus -->
## TOPIC 00141: GetAcquisitionTraceSubsetOffset(string, out int)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getacquisitiontracesubsetoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getacquisitiontracesubsetoffset__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the offset in number of pulses to be used for display acquisition trace. You must configure this method when you set the PulseAcquisitionTraceSelect method to Subset. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAcquisitionTraceSubsetOffset(string selectorString, out int value

### GetAcquisitionTraceSubsetOffset(string, out int)

Gets the offset in number of pulses to be used for display acquisition trace. You must configure this method when you set the [PulseAcquisitionTraceSelect](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [Subset](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseacquisitiontraceselect.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAcquisitionTraceSubsetOffset(string selectorString, out int value)

#### Remarks

This method gets the value of [PulseAcquisitionTraceSubsetOffset](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0. Valid values are 0 to 9999, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the offset in number of pulses to be used for display acquisition trace. You must configure this method when you set the PulseAcquisitionTraceSelect method to Subset. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00142: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable storing and retrieving traces after performing the measurements. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method gets the value of PulseAllTracesEnabled attribute.The default value is FALS

### GetAllTracesEnabled(string, out bool)

Gets whether to enable storing and retrieving traces after performing the measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [PulseAllTracesEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable storing and retrieving traces after performing the measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getamplitudeleveldomain__string-out.html language=enus -->
## TOPIC 00143: GetAmplitudeLevelDomain(string, out RFmxPulseMXPulseAmplitudeLevelDomain)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getamplitudeleveldomain__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getamplitudeleveldomain__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether voltage or power to be used as domain for pulse measurements. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAmplitudeLevelDomain(string selectorString, out RFmxPulseMXPulseAmplitudeLevelDomain value)RemarksThis method gets the value of PulseAmplitudeLevelDomain attribut

### GetAmplitudeLevelDomain(string, out RFmxPulseMXPulseAmplitudeLevelDomain)

Gets whether voltage or power to be used as domain for pulse measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAmplitudeLevelDomain(string selectorString, out RFmxPulseMXPulseAmplitudeLevelDomain value)

#### Remarks

This method gets the value of [PulseAmplitudeLevelDomain](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [Volts](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseamplitudeleveldomain.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXPulseAmplitudeLevelDomain | Upon return, contains whether voltage or power to be used as domain for pulse measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getamplitudetraceunit__string-out.html language=enus -->
## TOPIC 00144: GetAmplitudeTraceUnit(string, out RFmxPulseMXPulseAmplitudeTraceUnit)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getamplitudetraceunit__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getamplitudetraceunit__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the unit of the amplitude level. This method is applicable only for the amplitude and acquired amplitude trace. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetAmplitudeTraceUnit(string selectorString, out RFmxPulseMXPulseAmplitudeTraceUnit value)RemarksThis method gets the value

### GetAmplitudeTraceUnit(string, out RFmxPulseMXPulseAmplitudeTraceUnit)

Gets the unit of the amplitude level. This method is applicable only for the amplitude and acquired amplitude trace.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetAmplitudeTraceUnit(string selectorString, out RFmxPulseMXPulseAmplitudeTraceUnit value)

#### Remarks

This method gets the value of [PulseAmplitudeTraceUnit](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [dBm](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseamplitudetraceunit.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXPulseAmplitudeTraceUnit | Upon return, contains the unit of the amplitude level. This method is applicable only for the amplitude trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getdetectionhysteresis__string-out.html language=enus -->
## TOPIC 00145: GetDetectionHysteresis(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getdetectionhysteresis__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getdetectionhysteresis__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the hysteresis for pulse detection in dB for the defined threshold. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetDetectionHysteresis(string selectorString, out double value)RemarksThis method gets the value of PulseDetectionHysteresis attribute.The default value is 1. Valid va

### GetDetectionHysteresis(string, out double)

Gets the hysteresis for pulse detection in dB for the defined threshold.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetDetectionHysteresis(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseDetectionHysteresis](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 1. Valid values are 0 to 50, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the hysteresis for pulse detection in dB for the defined threshold. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getdetectionmaximumwidth__string-out.html language=enus -->
## TOPIC 00146: GetDetectionMaximumWidth(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getdetectionmaximumwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getdetectionmaximumwidth__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum pulse width time to be considered for pulse detection. Any detected pulse width time above the specified value will be ignored by the pulse detection. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetDetectionMaximumWidth(string sele

### GetDetectionMaximumWidth(string, out double)

Gets the maximum pulse width time to be considered for pulse detection. Any detected pulse width time above the specified value will be ignored by the pulse detection. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetDetectionMaximumWidth(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseDetectionMaximumWidth](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.005 seconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the maximum pulse width time to be considered for pulse detection. Any detected pulse width time above the specified value will be ignored by the pulse detection. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getdetectionminimumoffduration__string-out.html language=enus -->
## TOPIC 00147: GetDetectionMinimumOffDuration(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getdetectionminimumoffduration__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getdetectionminimumoffduration__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum pulse off duration to be ignored by the pulse detection. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetDetectionMinimumOffDuration(string selectorString, out double value)RemarksThis method gets the value of PulseDetectionMinimumO

### GetDetectionMinimumOffDuration(string, out double)

Gets the minimum pulse off duration to be ignored by the pulse detection. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetDetectionMinimumOffDuration(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseDetectionMinimumOffDuration](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.00000005. Valid values are 0 to 0.001, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the minimum pulse off duration to be ignored by the pulse detection. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getdetectionminimumwidth__string-out.html language=enus -->
## TOPIC 00148: GetDetectionMinimumWidth(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getdetectionminimumwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getdetectionminimumwidth__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum pulse width time to be considered for pulse detection. Any detected pulse width time below the specified value will be ignored by the pulse detection. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetDetectionMinimumWidth(string sele

### GetDetectionMinimumWidth(string, out double)

Gets the minimum pulse width time to be considered for pulse detection. Any detected pulse width time below the specified value will be ignored by the pulse detection. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetDetectionMinimumWidth(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseDetectionMinimumWidth](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.00000005 seconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the minimum pulse width time to be considered for pulse detection. Any detected pulse width time below the specified value will be ignored by the pulse detection. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getdetectionreference__string-out.html language=enus -->
## TOPIC 00149: GetDetectionReference(string, out RFmxPulseMXPulseDetectionReference)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getdetectionreference__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getdetectionreference__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the reference used for SetDetectionThreshold(string, double) method. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetDetectionReference(string selectorString, out RFmxPulseMXPulseDetectionReference value)RemarksThis method gets the value of PulseDetectionReference attribute.The d

### GetDetectionReference(string, out RFmxPulseMXPulseDetectionReference)

Gets the reference used for [SetDetectionThreshold(string, double)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setdetectionthreshold__string-double.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetDetectionReference(string selectorString, out RFmxPulseMXPulseDetectionReference value)

#### Remarks

This method gets the value of [PulseDetectionReference](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is Ref Level.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXPulseDetectionReference | Upon return, contains the reference used for SetDetectionThreshold(string, double) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getdetectionthreshold__string-out.html language=enus -->
## TOPIC 00150: GetDetectionThreshold(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getdetectionthreshold__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getdetectionthreshold__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the threshold used for pulse detection. The unit dB or dBm is based on the value you set to the SetDetectionReference(string, RFmxPulseMXPulseDetectionReference) method. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetDetectionThreshold(string selectorString, out double value)Rem

### GetDetectionThreshold(string, out double)

Gets the threshold used for pulse detection. The unit dB or dBm is based on the value you set to the [SetDetectionReference(string, RFmxPulseMXPulseDetectionReference)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setdetectionreference__string-rfmxpulsemxpulsedetectionreference.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetDetectionThreshold(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseDetectionThreshold](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is -20. Valid values are -100 to 100, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the threshold used for pulse detection. The unit dB or dBm is based on the value you set to the SetDetectionReference(string, RFmxPulseMXPulseDetectionReference) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getdroopcompensationenabled__string-out.html language=enus -->
## TOPIC 00151: GetDroopCompensationEnabled(string, out RFmxPulseMXPulseDroopCompensationEnabled)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getdroopcompensationenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getdroopcompensationenabled__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to compensate the droop detected in pulse level when applying thresholds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetDroopCompensationEnabled(string selectorString, out RFmxPulseMXPulseDroopCompensationEnabled value)RemarksThis method gets the value of PulseDroopComp

### GetDroopCompensationEnabled(string, out RFmxPulseMXPulseDroopCompensationEnabled)

Gets whether to compensate the droop detected in pulse level when applying thresholds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetDroopCompensationEnabled(string selectorString, out RFmxPulseMXPulseDroopCompensationEnabled value)

#### Remarks

This method gets the value of [PulseDroopCompensationEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsedroopcompensationenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXPulseDroopCompensationEnabled | Upon return, contains whether to compensate the droop detected in pulse level when applying thresholds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getfrequencyandphasecwfrequencyoffset__string-out.html language=enus -->
## TOPIC 00152: GetFrequencyAndPhaseCWFrequencyOffset(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getfrequencyandphasecwfrequencyoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getfrequencyandphasecwfrequencyoffset__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets to manually enter the CW frequency offset. This method is valid only when you set the SetFrequencyAndPhaseModulationType(string, RFmxPulseMXPulseModulationType) method to CW. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFrequencyAndPhaseCWFrequencyOffset(string selectorString,

### GetFrequencyAndPhaseCWFrequencyOffset(string, out double)

Gets to manually enter the CW frequency offset. This method is valid only when you set the [SetFrequencyAndPhaseModulationType(string, RFmxPulseMXPulseModulationType)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasemodulationtype__string-rfmxpulsemxpulsemodulationtype.html) method to [CW](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemodulationtype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFrequencyAndPhaseCWFrequencyOffset(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseFrequencyAndPhaseCWFrequencyOffset](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains to manually enter the CW frequency offset. This method is valid only when you set the SetFrequencyAndPhaseModulationType(string, RFmxPulseMXPulseModulationType) method to CW. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getfrequencyandphasecwfrequencyoffsetauto__string-out.html language=enus -->
## TOPIC 00153: GetFrequencyAndPhaseCWFrequencyOffsetAuto(string, out RFmxPulseMXPulseCWFrequencyOffsetAuto)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getfrequencyandphasecwfrequencyoffsetauto__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getfrequencyandphasecwfrequencyoffsetauto__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the CW frequency offset computation of every detected pulse is automatic or manual. This method is valid only when you set the SetFrequencyAndPhaseModulationType(string, RFmxPulseMXPulseModulationType) method to CW. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFrequenc

### GetFrequencyAndPhaseCWFrequencyOffsetAuto(string, out RFmxPulseMXPulseCWFrequencyOffsetAuto)

Gets whether the CW frequency offset computation of every detected pulse is automatic or manual. This method is valid only when you set the [SetFrequencyAndPhaseModulationType(string, RFmxPulseMXPulseModulationType)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasemodulationtype__string-rfmxpulsemxpulsemodulationtype.html) method to [CW](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemodulationtype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFrequencyAndPhaseCWFrequencyOffsetAuto(string selectorString, out RFmxPulseMXPulseCWFrequencyOffsetAuto value)

#### Remarks

This method gets the value of [PulseFrequencyAndPhaseCWFrequencyOffsetAuto](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsecwfrequencyoffsetauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXPulseCWFrequencyOffsetAuto | Upon return, contains whether the CW frequency offset computation of every detected pulse is automatic or manual. This method is valid only when you set the SetFrequencyAndPhaseModulationType(string, RFmxPulseMXPulseModulationType) method to CW. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getfrequencyandphasedeviationrangeedgestart__string-out.html language=enus -->
## TOPIC 00154: GetFrequencyAndPhaseDeviationRangeEdgeStart(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getfrequencyandphasedeviationrangeedgestart__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getfrequencyandphasedeviationrangeedgestart__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the start of the pulse data used for the phase/frequency deviation and error measurements when you set the SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference) method to Edge. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int Ge

### GetFrequencyAndPhaseDeviationRangeEdgeStart(string, out double)

Gets the start of the pulse data used for the phase/frequency deviation and error measurements when you set the [SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasedeviationrangereference__string-rfmxpulsemxpulsefrequencyandphasedeviationrangereference.html) method to [Edge](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsefrequencyandphasedeviationrangereference.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFrequencyAndPhaseDeviationRangeEdgeStart(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseFrequencyAndPhaseDeviationRangeEdgeStart](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the start of the pulse data used for the phase/frequency deviation and error measurements when you set the SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference) method to Edge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getfrequencyandphasedeviationrangeedgestop__string-out.html language=enus -->
## TOPIC 00155: GetFrequencyAndPhaseDeviationRangeEdgeStop(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getfrequencyandphasedeviationrangeedgestop__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getfrequencyandphasedeviationrangeedgestop__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the stop of the pulse data used for the phase/frequency deviation and error measurements when you set the SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference) method to Edge. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int Get

### GetFrequencyAndPhaseDeviationRangeEdgeStop(string, out double)

Gets the stop of the pulse data used for the phase/frequency deviation and error measurements when you set the [SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasedeviationrangereference__string-rfmxpulsemxpulsefrequencyandphasedeviationrangereference.html) method to [Edge](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsefrequencyandphasedeviationrangereference.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFrequencyAndPhaseDeviationRangeEdgeStop(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseFrequencyAndPhaseDeviationRangeEdgeStop](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the stop of the pulse data used for the phase/frequency deviation and error measurements when you set the SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference) method to Edge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getfrequencyandphasedeviationrangelength__string-out.html language=enus -->
## TOPIC 00156: GetFrequencyAndPhaseDeviationRangeLength(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getfrequencyandphasedeviationrangelength__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getfrequencyandphasedeviationrangelength__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the length of the pulse data used for the phase/frequency deviation and error measurements when you set the SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference) method to Center. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int

### GetFrequencyAndPhaseDeviationRangeLength(string, out double)

Gets the length of the pulse data used for the phase/frequency deviation and error measurements when you set the [SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasedeviationrangereference__string-rfmxpulsemxpulsefrequencyandphasedeviationrangereference.html) method to [Center](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsefrequencyandphasedeviationrangereference.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFrequencyAndPhaseDeviationRangeLength(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseFrequencyAndPhaseDeviationRangeLength](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 75. Valid values are 0 to 100, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the length of the pulse data used for the phase/frequency deviation and error measurements when you set the SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference) method to Center. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getfrequencyandphasedeviationrangereference__string-out.html language=enus -->
## TOPIC 00157: GetFrequencyAndPhaseDeviationRangeReference(string, out RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getfrequencyandphasedeviationrangereference__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getfrequencyandphasedeviationrangereference__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the reference used for the measurement range in phase/frequency deviation and error measurements. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFrequencyAndPhaseDeviationRangeReference(string selectorString, out RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference value)Rem

### GetFrequencyAndPhaseDeviationRangeReference(string, out RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference)

Gets the reference used for the measurement range in phase/frequency deviation and error measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFrequencyAndPhaseDeviationRangeReference(string selectorString, out RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference value)

#### Remarks

This method gets the value of [PulseFrequencyAndPhaseDeviationRangeReference](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [Center](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsefrequencyandphasedeviationrangereference.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference | Upon return, contains the reference used for the measurement range in phase/frequency deviation and error measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getfrequencyandphasemodulationtype__string-out.html language=enus -->
## TOPIC 00158: GetFrequencyAndPhaseModulationType(string, out RFmxPulseMXPulseModulationType)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getfrequencyandphasemodulationtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getfrequencyandphasemodulationtype__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the pulse modulation type used for the phase and frequency error, and pulsed FM Measurement. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetFrequencyAndPhaseModulationType(string selectorString, out RFmxPulseMXPulseModulationType value)RemarksThis method gets the value of PulseF

### GetFrequencyAndPhaseModulationType(string, out RFmxPulseMXPulseModulationType)

Gets the pulse modulation type used for the phase and frequency error, and pulsed FM Measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetFrequencyAndPhaseModulationType(string selectorString, out RFmxPulseMXPulseModulationType value)

#### Remarks

This method gets the value of [PulseFrequencyAndPhaseModulationType](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [CW](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemodulationtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXPulseModulationType | Upon return, contains the pulse modulation type used for the phase and frequency error, and pulsed FM Measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getlevelcomputationmethod__string-out.html language=enus -->
## TOPIC 00159: GetLevelComputationMethod(string, out RFmxPulseMXPulseLevelComputationMethod)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getlevelcomputationmethod__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getlevelcomputationmethod__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the algorithm used to detect the pulse levels. The algorithm is based on the histogram method of level detection as defined in IEEE Std 181-2011. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetLevelComputationMethod(string selectorString, out RFmxPulseMXPulseLevelComputationMeth

### GetLevelComputationMethod(string, out RFmxPulseMXPulseLevelComputationMethod)

Gets the algorithm used to detect the pulse levels. The algorithm is based on the histogram method of level detection as defined in *IEEE Std 181-2011*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetLevelComputationMethod(string selectorString, out RFmxPulseMXPulseLevelComputationMethod value)

#### Remarks

This method gets the value of [PulseLevelComputationMethod](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [Median](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulselevelcomputationmethod.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXPulseLevelComputationMethod | Upon return, contains the algorithm used to detect the pulse levels. The algorithm is based on the histogram method of level detection as defined in IEEE Std 181-2011. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getlowerthresholdlevel__string-out.html language=enus -->
## TOPIC 00160: GetLowerThresholdLevel(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getlowerthresholdlevel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getlowerthresholdlevel__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the lower threshold level as a percentage of the pulse amplitude used to signify the start of a rising or end of a falling edge. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetLowerThresholdLevel(string selectorString, out double value)RemarksThis method gets the value of PulseL

### GetLowerThresholdLevel(string, out double)

Gets the lower threshold level as a percentage of the pulse amplitude used to signify the start of a rising or end of a falling edge.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetLowerThresholdLevel(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseLowerThresholdLevel](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 10. Valid values are 0 to 100, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the lower threshold level as a percentage of the pulse amplitude used to signify the start of a rising or end of a falling edge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00161: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether pulse measurements are enabled.. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method gets the value of PulseMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescriptionselecto

### GetMeasurementEnabled(string, out bool)

Gets whether pulse measurements are enabled..

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [PulseMeasurementEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether pulse measurements are enabled.. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmeasurementpointaveragingduration__string-out.html language=enus -->
## TOPIC 00162: GetMeasurementPointAveragingDuration(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmeasurementpointaveragingduration__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmeasurementpointaveragingduration__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the length of the averaging window centered at the measurement point. A minimum of 1 sample is used internally. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetMeasurementPointAveragingDuration(string selectorString, out double value)RemarksThis method gets the value of PulseMeas

### GetMeasurementPointAveragingDuration(string, out double)

Gets the length of the averaging window centered at the measurement point. A minimum of 1 sample is used internally.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetMeasurementPointAveragingDuration(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseMeasurementPointAveragingDuration](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the length of the averaging window centered at the measurement point. A minimum of 1 sample is used internally. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmeasurementpointoffset__string-out.html language=enus -->
## TOPIC 00163: GetMeasurementPointOffset(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmeasurementpointoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmeasurementpointoffset__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the time offset of the measurement point within the pulse for phase, frequency, and stability measurements. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetMeasurementPointOffset(string selectorString, out double value)RemarksThis method gets the value of PulseMeasurementPointOff

### GetMeasurementPointOffset(string, out double)

Gets the time offset of the measurement point within the pulse for phase, frequency, and stability measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetMeasurementPointOffset(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseMeasurementPointOffset](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the time offset of the measurement point within the pulse for phase, frequency, and stability measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmeasurementpointreference__string-out.html language=enus -->
## TOPIC 00164: GetMeasurementPointReference(string, out RFmxPulseMXPulseMeasurementPointReference)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmeasurementpointreference__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmeasurementpointreference__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the reference used for the measurement point calculation, in phase, frequency, and stability measurements. You can set measurement point based on a reference and offset. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetMeasurementPointReference(string selectorString, out RFmxPulse

### GetMeasurementPointReference(string, out RFmxPulseMXPulseMeasurementPointReference)

Gets the reference used for the measurement point calculation, in phase, frequency, and stability measurements. You can set measurement point based on a reference and offset.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetMeasurementPointReference(string selectorString, out RFmxPulseMXPulseMeasurementPointReference value)

#### Remarks

This method gets the value of [PulseMeasurementPointReference](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [Center](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemeasurementpointreference.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXPulseMeasurementPointReference | Upon return, contains the reference used for the measurement point calculation, in phase, frequency, and stability measurements. You can set measurement point based on a reference and offset. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmetricsamplitudedeviationunit__string-out.html language=enus -->
## TOPIC 00165: GetMetricsAmplitudeDeviationUnit(string, out RFmxPulseMXPulseMetricsAmplitudeDeviationUnit)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmetricsamplitudedeviationunit__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmetricsamplitudedeviationunit__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the unit for amplitude deviation results. This method is applicable only for droop, ripple and overshoot results. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetMetricsAmplitudeDeviationUnit(string selectorString, out RFmxPulseMXPulseMetricsAmplitudeDeviationUnit value)RemarksTh

### GetMetricsAmplitudeDeviationUnit(string, out RFmxPulseMXPulseMetricsAmplitudeDeviationUnit)

Gets the unit for amplitude deviation results. This method is applicable only for droop, ripple and overshoot results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetMetricsAmplitudeDeviationUnit(string selectorString, out RFmxPulseMXPulseMetricsAmplitudeDeviationUnit value)

#### Remarks

This method gets the value of [PulseMetricsAmplitudeDeviationUnit](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [Percentage](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemetricsamplitudedeviationunit.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXPulseMetricsAmplitudeDeviationUnit | Upon return, contains the unit for amplitude deviation results. This method is applicable only for droop, ripple and overshoot results. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmetricsenabled__string-out.html language=enus -->
## TOPIC 00166: GetMetricsEnabled(string, out RFmxPulseMXPulseMetricsEnabled)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmetricsenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmetricsenabled__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable pulse metrics results computation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetMetricsEnabled(string selectorString, out RFmxPulseMXPulseMetricsEnabled value)RemarksThis method gets the value of PulseMetricsEnabled attribute.The default value is True.Paramet

### GetMetricsEnabled(string, out RFmxPulseMXPulseMetricsEnabled)

Gets whether to enable pulse metrics results computation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetMetricsEnabled(string selectorString, out RFmxPulseMXPulseMetricsEnabled value)

#### Remarks

This method gets the value of [PulseMetricsEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemetricsenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXPulseMetricsEnabled | Upon return, contains whether to enable pulse metrics results computation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmultiburstenabled__string-out.html language=enus -->
## TOPIC 00167: GetMultiburstEnabled(string, out RFmxPulseMXMultiburstEnabled)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmultiburstenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmultiburstenabled__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable pulse measurements on the multiple burst transmission. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetMultiburstEnabled(string selectorString, out RFmxPulseMXMultiburstEnabled value)RemarksThis method gets the value of PulseMultiburstEnabled attribute.The defau

### GetMultiburstEnabled(string, out RFmxPulseMXMultiburstEnabled)

Gets whether to enable pulse measurements on the multiple burst transmission.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetMultiburstEnabled(string selectorString, out RFmxPulseMXMultiburstEnabled value)

#### Remarks

This method gets the value of [PulseMultiburstEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-pulsemx-rfmxpulsemxmultiburstenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXMultiburstEnabled | Upon return, contains whether to enable pulse measurements on the multiple burst transmission. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmultiburstlength__string-out.html language=enus -->
## TOPIC 00168: GetMultiburstLength(string, out int)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmultiburstlength__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmultiburstlength__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of pulses assigned to a single burst. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetMultiburstLength(string selectorString, out int value)RemarksThis method gets the value of PulseMultiburstLength attribute.The default value is 10.ParametersNameTypeDescriptionselecto

### GetMultiburstLength(string, out int)

Gets the number of pulses assigned to a single burst.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetMultiburstLength(string selectorString, out int value)

#### Remarks

This method gets the value of [PulseMultiburstLength](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of pulses assigned to a single burst. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmultiplemeasurementpointsenabled__string-out.html language=enus -->
## TOPIC 00169: GetMultipleMeasurementPointsEnabled(string, out RFmxPulseMXPulseMultipleMeasurementPointsEnabled)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmultiplemeasurementpointsenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmultiplemeasurementpointsenabled__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable pulse stability measurements on multiple measurement points. This method is used to enable the multiple measurement points stability trace when you set the All Traces Enabled method to TRUE. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetMultipleMeasurementPoin

### GetMultipleMeasurementPointsEnabled(string, out RFmxPulseMXPulseMultipleMeasurementPointsEnabled)

Gets whether to enable pulse stability measurements on multiple measurement points. This method is used to enable the multiple measurement points stability trace when you set the All Traces Enabled method to TRUE.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetMultipleMeasurementPointsEnabled(string selectorString, out RFmxPulseMXPulseMultipleMeasurementPointsEnabled value)

#### Remarks

This method gets the value of [PulseMultipleMeasurementPointsEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsetimesidelobeenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXPulseMultipleMeasurementPointsEnabled | Upon return, contains whether to enable pulse stability measurements on multiple measurement points. This method is used to enable the multiple measurement points stability trace when you set the All Traces Enabled method to TRUE. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmultiplemeasurementpointswindowstart__string-out.html language=enus -->
## TOPIC 00170: GetMultipleMeasurementPointsWindowStart(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmultiplemeasurementpointswindowstart__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmultiplemeasurementpointswindowstart__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the start of the measurement window used for multiple measurement points selection over pulse ON duration. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetMultipleMeasurementPointsWindowStart(string selectorString, out double value)RemarksThis method gets the value of PulseMultip

### GetMultipleMeasurementPointsWindowStart(string, out double)

Gets the start of the measurement window used for multiple measurement points selection over pulse ON duration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetMultipleMeasurementPointsWindowStart(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseMultipleMeasurementPointsWindowStart](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 20. Valid values are 0 to 100, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the start of the measurement window used for multiple measurement points selection over pulse ON duration. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmultiplemeasurementpointswindowstepsize__string-out.html language=enus -->
## TOPIC 00171: GetMultipleMeasurementPointsWindowStepSize(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmultiplemeasurementpointswindowstepsize__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmultiplemeasurementpointswindowstepsize__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the step size of multiple measurement points selection within the measurement window over pulse ON duration. A minimum of 1 sample step size is used internally. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetMultipleMeasurementPointsWindowStepSize(string selectorString, out doub

### GetMultipleMeasurementPointsWindowStepSize(string, out double)

Gets the step size of multiple measurement points selection within the measurement window over pulse ON duration. A minimum of 1 sample step size is used internally.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetMultipleMeasurementPointsWindowStepSize(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseMultipleMeasurementPointsWindowStepSize](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the step size of multiple measurement points selection within the measurement window over pulse ON duration. A minimum of 1 sample step size is used internally. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmultiplemeasurementpointswindowstop__string-out.html language=enus -->
## TOPIC 00172: GetMultipleMeasurementPointsWindowStop(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmultiplemeasurementpointswindowstop__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getmultiplemeasurementpointswindowstop__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the stop of the measurement window used for multiple measurement points selection over pulse ON duration. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetMultipleMeasurementPointsWindowStop(string selectorString, out double value)RemarksThis method gets the value of PulseMultiple

### GetMultipleMeasurementPointsWindowStop(string, out double)

Gets the stop of the measurement window used for multiple measurement points selection over pulse ON duration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetMultipleMeasurementPointsWindowStop(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseMultipleMeasurementPointsWindowStop](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 80. Valid values are 0 to 100, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the stop of the measurement window used for multiple measurement points selection over pulse ON duration. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getnumberofanalysisthreads__string-out.html language=enus -->
## TOPIC 00173: GetNumberOfAnalysisThreads(string, out int)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getnumberofanalysisthreads__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getnumberofanalysisthreads__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum number of threads used for parallelism for the pulse measurement. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetNumberOfAnalysisThreads(string selectorString, out int value)RemarksThis method gets the value of PulseNumberOfAnalysisThreads attribute.The default value

### GetNumberOfAnalysisThreads(string, out int)

Gets the maximum number of threads used for parallelism for the pulse measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetNumberOfAnalysisThreads(string selectorString, out int value)

#### Remarks

This method gets the value of [PulseNumberOfAnalysisThreads](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 1. Valid values are 1 to 10, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the maximum number of threads used for parallelism for the pulse measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getselectedbursttrace__string-out.html language=enus -->
## TOPIC 00174: GetSelectedBurstTrace(string, out int)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getselectedbursttrace__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getselectedbursttrace__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the burst number selected for the display of traces. This method is applicable for IQ, amplitude and pulse stability traces. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetSelectedBurstTrace(string selectorString, out int value)RemarksThis method gets the value of PulseSelectedB

### GetSelectedBurstTrace(string, out int)

Gets the burst number selected for the display of traces. This method is applicable for IQ, amplitude and pulse stability traces.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetSelectedBurstTrace(string selectorString, out int value)

#### Remarks

This method gets the value of [PulseSelectedBurstTrace](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the burst number selected for the display of traces. This method is applicable for IQ, amplitude and pulse stability traces. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getselectedpulsetrace__string-out.html language=enus -->
## TOPIC 00175: GetSelectedPulseTrace(string, out int)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getselectedpulsetrace__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getselectedpulsetrace__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the pulse number selected for displaying the traces. This method is valid only for IQ, amplitude and pulse stability traces. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetSelectedPulseTrace(string selectorString, out int value)RemarksThis method gets the value of PulseSelectedP

### GetSelectedPulseTrace(string, out int)

Gets the pulse number selected for displaying the traces. This method is valid only for IQ, amplitude and pulse stability traces.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetSelectedPulseTrace(string selectorString, out int value)

#### Remarks

This method gets the value of [PulseSelectedPulseTrace](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the pulse number selected for displaying the traces. This method is valid only for IQ, amplitude and pulse stability traces. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getstabilityenabled__string-out.html language=enus -->
## TOPIC 00176: GetStabilityEnabled(string, out RFmxPulseMXPulseStabilityEnabled)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getstabilityenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getstabilityenabled__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable pulse stability results computation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetStabilityEnabled(string selectorString, out RFmxPulseMXPulseStabilityEnabled value)RemarksThis method gets the value of PulseStabilityEnabled attribute.The default value is True

### GetStabilityEnabled(string, out RFmxPulseMXPulseStabilityEnabled)

Gets whether to enable pulse stability results computation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetStabilityEnabled(string selectorString, out RFmxPulseMXPulseStabilityEnabled value)

#### Remarks

This method gets the value of [PulseStabilityEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsestabilityenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXPulseStabilityEnabled | Upon return, contains whether to enable pulse stability results computation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getstabilityfrequencyerrorcompensation__string-out.html language=enus -->
## TOPIC 00177: GetStabilityFrequencyErrorCompensation(string, out RFmxPulseMXPulseStabilityFrequencyErrorCompensation)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getstabilityfrequencyerrorcompensation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getstabilityfrequencyerrorcompensation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to compute and correct the frequency offset for stability results computation. This is an optional setting and in negligible frequency error condition you must set this method to Off to avoid incorrect results. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetStabilityFreq

### GetStabilityFrequencyErrorCompensation(string, out RFmxPulseMXPulseStabilityFrequencyErrorCompensation)

Gets whether to compute and correct the frequency offset for stability results computation. This is an optional setting and in negligible frequency error condition you must set this method to Off to avoid incorrect results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetStabilityFrequencyErrorCompensation(string selectorString, out RFmxPulseMXPulseStabilityFrequencyErrorCompensation value)

#### Remarks

This method gets the value of [PulseStabilityFrequencyErrorCompensation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [Off](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsestabilityfrequencyerrorcompensation.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXPulseStabilityFrequencyErrorCompensation | Upon return, contains whether to compute and correct the frequency offset for stability results computation. This is an optional setting and in negligible frequency error condition you must set this method to Off to avoid incorrect results. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getstabilitymeasurementoffset__string-out.html language=enus -->
## TOPIC 00178: GetStabilityMeasurementOffset(string, out int)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getstabilitymeasurementoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getstabilitymeasurementoffset__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the offset in number of pulses to be used for pulse stability measurement. This method is applicable for average stability results and pulse-to-pulse stabilty trace. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetStabilityMeasurementOffset(string selectorString, out int value)Re

### GetStabilityMeasurementOffset(string, out int)

Gets the offset in number of pulses to be used for pulse stability measurement. This method is applicable for average stability results and pulse-to-pulse stabilty trace.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetStabilityMeasurementOffset(string selectorString, out int value)

#### Remarks

This method gets the value of [PulseStabilityMeasurementOffset](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the offset in number of pulses to be used for pulse stability measurement. This method is applicable for average stability results and pulse-to-pulse stabilty trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getstabilitypulsetopulseoffset__string-out.html language=enus -->
## TOPIC 00179: GetStabilityPulseToPulseOffset(string, out int)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getstabilitypulsetopulseoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getstabilitypulsetopulseoffset__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the offset in number of pulses used for pulse-to-pulse stability measurement trace. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetStabilityPulseToPulseOffset(string selectorString, out int value)RemarksThis method gets the value of PulseStabilityPulseToPulseOffset attribute.The

### GetStabilityPulseToPulseOffset(string, out int)

Gets the offset in number of pulses used for pulse-to-pulse stability measurement trace.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetStabilityPulseToPulseOffset(string selectorString, out int value)

#### Remarks

This method gets the value of [PulseStabilityPulseToPulseOffset](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the offset in number of pulses used for pulse-to-pulse stability measurement trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getstabilityreferenceoffset__string-out.html language=enus -->
## TOPIC 00180: GetStabilityReferenceOffset(string, out int)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getstabilityreferenceoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getstabilityreferenceoffset__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the offset in number of pulses used for pulse stability reference computation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetStabilityReferenceOffset(string selectorString, out int value)RemarksThis method gets the value of PulseStabilityReferenceOffset attribute.The default va

### GetStabilityReferenceOffset(string, out int)

Gets the offset in number of pulses used for pulse stability reference computation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetStabilityReferenceOffset(string selectorString, out int value)

#### Remarks

This method gets the value of [PulseStabilityReferenceOffset](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the offset in number of pulses used for pulse stability reference computation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-gettimesidelobeenabled__string-out.html language=enus -->
## TOPIC 00181: GetTimeSidelobeEnabled(string, out RFmxPulseMXPulseTimeSidelobeEnabled)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-gettimesidelobeenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-gettimesidelobeenabled__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable pulse time sidelobe results computation. You can use the NationalInstruments.RFmx.PulseMX.RFmxPulseMXPulseConfiguration.Configure1ReferenceWaveform(string,NationalInstruments.ComplexWaveform<NationalInstruments.ComplexSingle>) function to set the reference waveform for correla

### GetTimeSidelobeEnabled(string, out RFmxPulseMXPulseTimeSidelobeEnabled)

Gets whether to enable pulse time sidelobe results computation. You can use the NationalInstruments.RFmx.PulseMX.RFmxPulseMXPulseConfiguration.Configure1ReferenceWaveform(string,NationalInstruments.ComplexWaveform<NationalInstruments.ComplexSingle>) function to set the reference waveform for correlation computation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobeEnabled(string selectorString, out RFmxPulseMXPulseTimeSidelobeEnabled value)

#### Remarks

This method gets the value of [PulseTimeSidelobeEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsetimesidelobeenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXPulseTimeSidelobeEnabled | Upon return, contains whether to enable pulse time sidelobe results computation. You can use the NationalInstruments.RFmx.PulseMX.RFmxPulseMXPulseConfiguration.Configure1ReferenceWaveform(string,NationalInstruments.ComplexWaveform<NationalInstruments.ComplexSingle>) function to set the reference waveform for correlation computation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-gettimesidelobekeepouttime__string-out.html language=enus -->
## TOPIC 00182: GetTimeSidelobeKeepOutTime(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-gettimesidelobekeepouttime__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-gettimesidelobekeepouttime__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets keep out time for the time sidelobe measurements. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobeKeepOutTime(string selectorString, out double value)RemarksThis method gets the value of PulseTimeSidelobeKeepOutTime attribute.The default value is 0.000001 seconds.Para

### GetTimeSidelobeKeepOutTime(string, out double)

Gets keep out time for the time sidelobe measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobeKeepOutTime(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseTimeSidelobeKeepOutTime](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.000001 seconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains keep out time for the time sidelobe measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-gettimesidelobekeepouttimeauto__string-out.html language=enus -->
## TOPIC 00183: GetTimeSidelobeKeepOutTimeAuto(string, out RFmxPulseMXPulseTimeSidelobeKeepOutTimeAuto)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-gettimesidelobekeepouttimeauto__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-gettimesidelobekeepouttimeauto__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the keep out time computation for the time sidelobe measurements is automatic or manual. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobeKeepOutTimeAuto(string selectorString, out RFmxPulseMXPulseTimeSidelobeKeepOutTimeAuto value)RemarksThis method gets the va

### GetTimeSidelobeKeepOutTimeAuto(string, out RFmxPulseMXPulseTimeSidelobeKeepOutTimeAuto)

Gets whether the keep out time computation for the time sidelobe measurements is automatic or manual.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobeKeepOutTimeAuto(string selectorString, out RFmxPulseMXPulseTimeSidelobeKeepOutTimeAuto value)

#### Remarks

This method gets the value of [PulseTimeSidelobeKeepOutTimeAuto](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsetimesidelobekeepouttimeauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXPulseTimeSidelobeKeepOutTimeAuto | Upon return, contains whether the keep out time computation for the time sidelobe measurements is automatic or manual. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-gettimesidelobeminimumcorrelation__string-out.html language=enus -->
## TOPIC 00184: GetTimeSidelobeMinimumCorrelation(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-gettimesidelobeminimumcorrelation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-gettimesidelobeminimumcorrelation__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum peak correlation value for the time sidelobe measurements. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobeMinimumCorrelation(string selectorString, out double value)RemarksThis method gets the value of PulseTimeSidelobeMinimumCorrelation attribute.The def

### GetTimeSidelobeMinimumCorrelation(string, out double)

Gets the minimum peak correlation value for the time sidelobe measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobeMinimumCorrelation(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseTimeSidelobeMinimumCorrelation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.5.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the minimum peak correlation value for the time sidelobe measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-gettimesidelobereferencewindowtype__string-out.html language=enus -->
## TOPIC 00185: GetTimeSidelobeReferenceWindowType(string, out RFmxPulseMXPulseTimeSidelobeReferenceWindowType)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-gettimesidelobereferencewindowtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-gettimesidelobereferencewindowtype__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the window type to be applied to the reference pulse to obtain correlated output for the time sidelobe measurements. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTimeSidelobeReferenceWindowType(string selectorString, out RFmxPulseMXPulseTimeSidelobeReferenceWindowType value)Re

### GetTimeSidelobeReferenceWindowType(string, out RFmxPulseMXPulseTimeSidelobeReferenceWindowType)

Gets the window type to be applied to the reference pulse to obtain correlated output for the time sidelobe measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTimeSidelobeReferenceWindowType(string selectorString, out RFmxPulseMXPulseTimeSidelobeReferenceWindowType value)

#### Remarks

This method gets the value of [PulseTimeSidelobeReferenceWindowType](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [None](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsetimesidelobereferencewindowtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXPulseTimeSidelobeReferenceWindowType | Upon return, contains the window type to be applied to the reference pulse to obtain correlated output for the time sidelobe measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-gettracerangeauto__string-out.html language=enus -->
## TOPIC 00186: GetTraceRangeAuto(string, out RFmxPulseMXPulseTraceRangeAuto)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-gettracerangeauto__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-gettracerangeauto__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the trace range computation of the selected pulse is automatic or manually configured by you. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTraceRangeAuto(string selectorString, out RFmxPulseMXPulseTraceRangeAuto value)RemarksThis method gets the value of PulseTraceRang

### GetTraceRangeAuto(string, out RFmxPulseMXPulseTraceRangeAuto)

Gets whether the trace range computation of the selected pulse is automatic or manually configured by you.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTraceRangeAuto(string selectorString, out RFmxPulseMXPulseTraceRangeAuto value)

#### Remarks

This method gets the value of [PulseTraceRangeAuto](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is *RFmxPulseMXTraceRangeAuto.True*.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXPulseTraceRangeAuto | Upon return, contains whether the trace range computation of the selected pulse is automatic or manually configured by you. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-gettracerangelength__string-out.html language=enus -->
## TOPIC 00187: GetTraceRangeLength(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-gettracerangelength__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-gettracerangelength__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the length in seconds of the trace range centered at the reference point. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTraceRangeLength(string selectorString, out double value)RemarksThis method gets the value of PulseTraceRangeLength attribute.The default value is 0.000020 se

### GetTraceRangeLength(string, out double)

Gets the length in seconds of the trace range centered at the reference point.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTraceRangeLength(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseTraceRangeLength](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.000020 seconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the length in seconds of the trace range centered at the reference point. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-gettracerangeoffset__string-out.html language=enus -->
## TOPIC 00188: GetTraceRangeOffset(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-gettracerangeoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-gettracerangeoffset__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the time offset in seconds from the reference point to position the trace range. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTraceRangeOffset(string selectorString, out double value)RemarksThis method gets the value of PulseTraceRangeOffset attribute.The default value is 0.Pa

### GetTraceRangeOffset(string, out double)

Gets the time offset in seconds from the reference point to position the trace range.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTraceRangeOffset(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseTraceRangeOffset](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the time offset in seconds from the reference point to position the trace range. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-gettracerangereference__string-out.html language=enus -->
## TOPIC 00189: GetTraceRangeReference(string, out RFmxPulseMXPulseTraceRangeReference)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-gettracerangereference__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-gettracerangereference__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the reference point for positioning of trace range. You can set reference point based on reference and Pulse Trace Range Offset (s) value. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetTraceRangeReference(string selectorString, out RFmxPulseMXPulseTraceRangeReference value)Rema

### GetTraceRangeReference(string, out RFmxPulseMXPulseTraceRangeReference)

Gets the reference point for positioning of trace range. You can set reference point based on reference and Pulse Trace Range Offset (s) value.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetTraceRangeReference(string selectorString, out RFmxPulseMXPulseTraceRangeReference value)

#### Remarks

This method gets the value of [PulseTraceRangeReference](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is *RFmxPulseMXTraceRangeReference.Center*.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxPulseMXPulseTraceRangeReference | Upon return, contains the reference point for positioning of trace range. You can set reference point based on reference and Pulse Trace Range Offset (s) value. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getupperthresholdlevel__string-out.html language=enus -->
## TOPIC 00190: GetUpperThresholdLevel(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getupperthresholdlevel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getupperthresholdlevel__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the upper threshold level as a percentage of the pulse amplitude used to signify the end of a rising edge or beginning of a falling edge. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetUpperThresholdLevel(string selectorString, out double value)RemarksThis method gets the value

### GetUpperThresholdLevel(string, out double)

Gets the upper threshold level as a percentage of the pulse amplitude used to signify the end of a rising edge or beginning of a falling edge.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetUpperThresholdLevel(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseUpperThresholdLevel](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 90. Valid values are 0 to 100, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the upper threshold level as a percentage of the pulse amplitude used to signify the end of a rising edge or beginning of a falling edge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getwidththresholdlevel__string-out.html language=enus -->
## TOPIC 00191: GetWidthThresholdLevel(string, out double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getwidththresholdlevel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-getwidththresholdlevel__string-out.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the middle threshold level as a percentage of the pulse amplitude used to signify the mid-transition level between pulse states used for pulse width computation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int GetWidthThresholdLevel(string selectorString, out double value)RemarksThi

### GetWidthThresholdLevel(string, out double)

Gets the middle threshold level as a percentage of the pulse amplitude used to signify the mid-transition level between pulse states used for pulse width computation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int GetWidthThresholdLevel(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseWidthThresholdLevel](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 50. Valid values are 0 to 100, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the middle threshold level as a percentage of the pulse amplitude used to signify the mid-transition level between pulse states used for pulse width computation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setacquisitiontraceselect__string-rfmxpulsemxpulseacquisitiontraceselect.html language=enus -->
## TOPIC 00192: SetAcquisitionTraceSelect(string, RFmxPulseMXPulseAcquisitionTraceSelect)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setacquisitiontraceselect__string-rfmxpulsemxpulseacquisitiontraceselect.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setacquisitiontraceselect__string-rfmxpulsemxpulseacquisitiontraceselect.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the mode to select all pulses or the subset of acquired pulses available for display acquisition trace, limited to MaximumPulseCountEnabled method if set to True. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetAcquisitionTraceSelect(string selectorString, RFmxPulseMXPulseAcquisi

### SetAcquisitionTraceSelect(string, RFmxPulseMXPulseAcquisitionTraceSelect)

Sets the mode to select all pulses or the subset of acquired pulses available for display acquisition trace, limited to [MaximumPulseCountEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method if set to [True](nationalinstruments-rfmx-pulsemx-rfmxpulsemxmaximumpulsecountenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetAcquisitionTraceSelect(string selectorString, RFmxPulseMXPulseAcquisitionTraceSelect value)

#### Remarks

This method sets the value of [PulseAcquisitionTraceSelect](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [Subset](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseacquisitiontraceselect.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXPulseAcquisitionTraceSelect | Specifies the mode to select all pulses or the subset of acquired pulses available for display acquisition trace, limited to MaximumPulseCountEnabled method if set to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setacquisitiontracesubsetlength__string-int.html language=enus -->
## TOPIC 00193: SetAcquisitionTraceSubsetLength(string, int)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setacquisitiontracesubsetlength__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setacquisitiontracesubsetlength__string-int.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the total number of pulses starting from offset to be used for display acquisition trace. You must configure this method when you set the PulseAcquisitionTraceSelect method to Subset. Set length to 0 to disable the acquisition trace. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int S

### SetAcquisitionTraceSubsetLength(string, int)

Sets the total number of pulses starting from offset to be used for display acquisition trace. You must configure this method when you set the [PulseAcquisitionTraceSelect](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [Subset](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseacquisitiontraceselect.html). Set length to 0 to disable the acquisition trace.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetAcquisitionTraceSubsetLength(string selectorString, int value)

#### Remarks

This method sets the value of [PulseAcquisitionTraceSubsetLength](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 10. Valid values are 0 to 10000, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the total number of pulses starting from offset to be used for display acquisition trace. You must configure this method when you set the PulseAcquisitionTraceSelect method to Subset. Set length to 0 to disable the acquisition trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setacquisitiontracesubsetoffset__string-int.html language=enus -->
## TOPIC 00194: SetAcquisitionTraceSubsetOffset(string, int)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setacquisitiontracesubsetoffset__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setacquisitiontracesubsetoffset__string-int.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the offset in number of pulses to be used for display acquisition trace. You must configure this method when you set the PulseAcquisitionTraceSelect method to Subset. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetAcquisitionTraceSubsetOffset(string selectorString, int value)Rem

### SetAcquisitionTraceSubsetOffset(string, int)

Sets the offset in number of pulses to be used for display acquisition trace. You must configure this method when you set the [PulseAcquisitionTraceSelect](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) method to [Subset](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseacquisitiontraceselect.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetAcquisitionTraceSubsetOffset(string selectorString, int value)

#### Remarks

This method sets the value of [PulseAcquisitionTraceSubsetOffset](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0. Valid values are 0 to 9999, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the offset in number of pulses to be used for display acquisition trace. You must configure this method when you set the PulseAcquisitionTraceSelect method to Subset. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setalltracesenabled__string-bool.html language=enus -->
## TOPIC 00195: SetAllTracesEnabled(string, bool)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setalltracesenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setalltracesenabled__string-bool.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable storing and retrieving traces after performing the measurements. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetAllTracesEnabled(string selectorString, bool value)RemarksThis method sets the value of PulseAllTracesEnabled attribute.The default value is FALSE.Pa

### SetAllTracesEnabled(string, bool)

Sets whether to enable storing and retrieving traces after performing the measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetAllTracesEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [PulseAllTracesEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable storing and retrieving traces after performing the measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setamplitudeleveldomain__string-rfmxpulsemxpulseamplitudeleveldomain.html language=enus -->
## TOPIC 00196: SetAmplitudeLevelDomain(string, RFmxPulseMXPulseAmplitudeLevelDomain)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setamplitudeleveldomain__string-rfmxpulsemxpulseamplitudeleveldomain.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setamplitudeleveldomain__string-rfmxpulsemxpulseamplitudeleveldomain.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether voltage or power to be used as domain for pulse measurements. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetAmplitudeLevelDomain(string selectorString, RFmxPulseMXPulseAmplitudeLevelDomain value)RemarksThis method sets the value of PulseAmplitudeLevelDomain attribute.Th

### SetAmplitudeLevelDomain(string, RFmxPulseMXPulseAmplitudeLevelDomain)

Sets whether voltage or power to be used as domain for pulse measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetAmplitudeLevelDomain(string selectorString, RFmxPulseMXPulseAmplitudeLevelDomain value)

#### Remarks

This method sets the value of [PulseAmplitudeLevelDomain](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [Volts](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseamplitudeleveldomain.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXPulseAmplitudeLevelDomain | Specifies whether voltage or power to be used as domain for pulse measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setamplitudetraceunit__string-rfmxpulsemxpulseamplitudetraceunit.html language=enus -->
## TOPIC 00197: SetAmplitudeTraceUnit(string, RFmxPulseMXPulseAmplitudeTraceUnit)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setamplitudetraceunit__string-rfmxpulsemxpulseamplitudetraceunit.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setamplitudetraceunit__string-rfmxpulsemxpulseamplitudetraceunit.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the unit of the amplitude level. This method is applicable only for the amplitude trace. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetAmplitudeTraceUnit(string selectorString, RFmxPulseMXPulseAmplitudeTraceUnit value)RemarksThis method sets the value of PulseAmplitudeTraceUnit

### SetAmplitudeTraceUnit(string, RFmxPulseMXPulseAmplitudeTraceUnit)

Sets the unit of the amplitude level. This method is applicable only for the amplitude trace.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetAmplitudeTraceUnit(string selectorString, RFmxPulseMXPulseAmplitudeTraceUnit value)

#### Remarks

This method sets the value of [PulseAmplitudeTraceUnit](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [dBm](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseamplitudetraceunit.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXPulseAmplitudeTraceUnit | Specifies the unit of the amplitude level. This method is applicable only for the amplitude trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setdetectionhysteresis__string-double.html language=enus -->
## TOPIC 00198: SetDetectionHysteresis(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setdetectionhysteresis__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setdetectionhysteresis__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the hysteresis for pulse detection in dB for the defined threshold. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetDetectionHysteresis(string selectorString, double value)RemarksThis method sets the value of PulseDetectionHysteresis attribute.The default value is 1. Valid values

### SetDetectionHysteresis(string, double)

Sets the hysteresis for pulse detection in dB for the defined threshold.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetDetectionHysteresis(string selectorString, double value)

#### Remarks

This method sets the value of [PulseDetectionHysteresis](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 1. Valid values are 0 to 50, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the hysteresis for pulse detection in dB for the defined threshold. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setdetectionmaximumwidth__string-double.html language=enus -->
## TOPIC 00199: SetDetectionMaximumWidth(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setdetectionmaximumwidth__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setdetectionmaximumwidth__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the maximum pulse width time to be considered for pulse detection. Any detected pulse width time above the specified value will be ignored by the pulse detection. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetDetectionMaximumWidth(string sele

### SetDetectionMaximumWidth(string, double)

Sets the maximum pulse width time to be considered for pulse detection. Any detected pulse width time above the specified value will be ignored by the pulse detection. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetDetectionMaximumWidth(string selectorString, double value)

#### Remarks

This method sets the value of [PulseDetectionMaximumWidth](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.005 seconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the maximum pulse width time to be considered for pulse detection. Any detected pulse width time above the specified value will be ignored by the pulse detection. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setdetectionminimumoffduration__string-double.html language=enus -->
## TOPIC 00200: SetDetectionMinimumOffDuration(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setdetectionminimumoffduration__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setdetectionminimumoffduration__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the minimum pulse off duration to be ignored by the pulse detection. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetDetectionMinimumOffDuration(string selectorString, double value)RemarksThis method sets the value of PulseDetectionMinimumOffDu

### SetDetectionMinimumOffDuration(string, double)

Sets the minimum pulse off duration to be ignored by the pulse detection. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetDetectionMinimumOffDuration(string selectorString, double value)

#### Remarks

This method sets the value of [PulseDetectionMinimumOffDuration](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.00000005. Valid values are 0 to 0.001, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the minimum pulse off duration to be ignored by the pulse detection. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setdetectionminimumwidth__string-double.html language=enus -->
## TOPIC 00201: SetDetectionMinimumWidth(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setdetectionminimumwidth__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setdetectionminimumwidth__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the minimum pulse width time to be considered for pulse detection. Any detected pulse width time below the specified value will be ignored by the pulse detection. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetDetectionMinimumWidth(string sele

### SetDetectionMinimumWidth(string, double)

Sets the minimum pulse width time to be considered for pulse detection. Any detected pulse width time below the specified value will be ignored by the pulse detection. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetDetectionMinimumWidth(string selectorString, double value)

#### Remarks

This method sets the value of [PulseDetectionMinimumWidth](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.00000005 seconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the minimum pulse width time to be considered for pulse detection. Any detected pulse width time below the specified value will be ignored by the pulse detection. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setdetectionreference__string-rfmxpulsemxpulsedetectionreference.html language=enus -->
## TOPIC 00202: SetDetectionReference(string, RFmxPulseMXPulseDetectionReference)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setdetectionreference__string-rfmxpulsemxpulsedetectionreference.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setdetectionreference__string-rfmxpulsemxpulsedetectionreference.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the reference used for SetDetectionThreshold(string, double) method. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetDetectionReference(string selectorString, RFmxPulseMXPulseDetectionReference value)RemarksThis method sets the value of PulseDetectionReference attribute.The defau

### SetDetectionReference(string, RFmxPulseMXPulseDetectionReference)

Sets the reference used for [SetDetectionThreshold(string, double)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setdetectionthreshold__string-double.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetDetectionReference(string selectorString, RFmxPulseMXPulseDetectionReference value)

#### Remarks

This method sets the value of [PulseDetectionReference](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is Ref Level.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXPulseDetectionReference | Specifies the reference used for SetDetectionThreshold(string, double) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setdetectionthreshold__string-double.html language=enus -->
## TOPIC 00203: SetDetectionThreshold(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setdetectionthreshold__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setdetectionthreshold__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the threshold used for pulse detection. The unit dB or dBm is based on the value you set to the SetDetectionReference(string, RFmxPulseMXPulseDetectionReference) method. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetDetectionThreshold(string selectorString, double value)Remarks

### SetDetectionThreshold(string, double)

Sets the threshold used for pulse detection. The unit dB or dBm is based on the value you set to the [SetDetectionReference(string, RFmxPulseMXPulseDetectionReference)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setdetectionreference__string-rfmxpulsemxpulsedetectionreference.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetDetectionThreshold(string selectorString, double value)

#### Remarks

This method sets the value of [PulseDetectionThreshold](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is -20. Valid values are -100 to 100, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the threshold used for pulse detection. The unit dB or dBm is based on the value you set to the SetDetectionReference(string, RFmxPulseMXPulseDetectionReference) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setdroopcompensationenabled__string-rfmxpulsemxpulsedroopcompensationenabled.html language=enus -->
## TOPIC 00204: SetDroopCompensationEnabled(string, RFmxPulseMXPulseDroopCompensationEnabled)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setdroopcompensationenabled__string-rfmxpulsemxpulsedroopcompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setdroopcompensationenabled__string-rfmxpulsemxpulsedroopcompensationenabled.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to compensate the droop detected in pulse level when applying thresholds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetDroopCompensationEnabled(string selectorString, RFmxPulseMXPulseDroopCompensationEnabled value)RemarksThis method sets the value of PulseDroopCompensa

### SetDroopCompensationEnabled(string, RFmxPulseMXPulseDroopCompensationEnabled)

Sets whether to compensate the droop detected in pulse level when applying thresholds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetDroopCompensationEnabled(string selectorString, RFmxPulseMXPulseDroopCompensationEnabled value)

#### Remarks

This method sets the value of [PulseDroopCompensationEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsedroopcompensationenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXPulseDroopCompensationEnabled | Specifies whether to compensate the droop detected in pulse level when applying thresholds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasecwfrequencyoffset__string-double.html language=enus -->
## TOPIC 00205: SetFrequencyAndPhaseCWFrequencyOffset(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasecwfrequencyoffset__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasecwfrequencyoffset__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets to manually enter the CW frequency offset. This method is valid only when you set the SetFrequencyAndPhaseModulationType(string, RFmxPulseMXPulseModulationType) method to CW. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetFrequencyAndPhaseCWFrequencyOffset(string selectorString,

### SetFrequencyAndPhaseCWFrequencyOffset(string, double)

Sets to manually enter the CW frequency offset. This method is valid only when you set the [SetFrequencyAndPhaseModulationType(string, RFmxPulseMXPulseModulationType)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasemodulationtype__string-rfmxpulsemxpulsemodulationtype.html) method to [CW](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemodulationtype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetFrequencyAndPhaseCWFrequencyOffset(string selectorString, double value)

#### Remarks

This method sets the value of [PulseFrequencyAndPhaseCWFrequencyOffset](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies to manually enter the CW frequency offset. This method is valid only when you set the SetFrequencyAndPhaseModulationType(string, RFmxPulseMXPulseModulationType) method to CW. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasecwfrequencyoffsetauto__string-rfmxpulsemxpulsecwfrequencyoffsetauto.html language=enus -->
## TOPIC 00206: SetFrequencyAndPhaseCWFrequencyOffsetAuto(string, RFmxPulseMXPulseCWFrequencyOffsetAuto)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasecwfrequencyoffsetauto__string-rfmxpulsemxpulsecwfrequencyoffsetauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasecwfrequencyoffsetauto__string-rfmxpulsemxpulsecwfrequencyoffsetauto.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the CW frequency offset computation of every detected pulse is automatic or manual. This method is valid only when you set the SetFrequencyAndPhaseModulationType(string, RFmxPulseMXPulseModulationType) method to CW. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetFrequenc

### SetFrequencyAndPhaseCWFrequencyOffsetAuto(string, RFmxPulseMXPulseCWFrequencyOffsetAuto)

Sets whether the CW frequency offset computation of every detected pulse is automatic or manual. This method is valid only when you set the [SetFrequencyAndPhaseModulationType(string, RFmxPulseMXPulseModulationType)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasemodulationtype__string-rfmxpulsemxpulsemodulationtype.html) method to [CW](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemodulationtype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetFrequencyAndPhaseCWFrequencyOffsetAuto(string selectorString, RFmxPulseMXPulseCWFrequencyOffsetAuto value)

#### Remarks

This method sets the value of [PulseFrequencyAndPhaseCWFrequencyOffsetAuto](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsecwfrequencyoffsetauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXPulseCWFrequencyOffsetAuto | Specifies whether the CW frequency offset computation of every detected pulse is automatic or manual. This method is valid only when you set the SetFrequencyAndPhaseModulationType(string, RFmxPulseMXPulseModulationType) method to CW. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasedeviationrangeedgestart__string-double.html language=enus -->
## TOPIC 00207: SetFrequencyAndPhaseDeviationRangeEdgeStart(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasedeviationrangeedgestart__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasedeviationrangeedgestart__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the start of the pulse data used for the phase/frequency deviation and error measurements when you set the SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference) method to Edge. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int Se

### SetFrequencyAndPhaseDeviationRangeEdgeStart(string, double)

Sets the start of the pulse data used for the phase/frequency deviation and error measurements when you set the [SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasedeviationrangereference__string-rfmxpulsemxpulsefrequencyandphasedeviationrangereference.html) method to [Edge](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsefrequencyandphasedeviationrangereference.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetFrequencyAndPhaseDeviationRangeEdgeStart(string selectorString, double value)

#### Remarks

This method sets the value of [PulseFrequencyAndPhaseDeviationRangeEdgeStart](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the start of the pulse data used for the phase/frequency deviation and error measurements when you set the SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference) method to Edge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasedeviationrangeedgestop__string-double.html language=enus -->
## TOPIC 00208: SetFrequencyAndPhaseDeviationRangeEdgeStop(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasedeviationrangeedgestop__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasedeviationrangeedgestop__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the stop of the pulse data used for the phase/frequency deviation and error measurements when you set the SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference) method to Edge. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int Set

### SetFrequencyAndPhaseDeviationRangeEdgeStop(string, double)

Sets the stop of the pulse data used for the phase/frequency deviation and error measurements when you set the [SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasedeviationrangereference__string-rfmxpulsemxpulsefrequencyandphasedeviationrangereference.html) method to [Edge](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsefrequencyandphasedeviationrangereference.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetFrequencyAndPhaseDeviationRangeEdgeStop(string selectorString, double value)

#### Remarks

This method sets the value of [PulseFrequencyAndPhaseDeviationRangeEdgeStop](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the stop of the pulse data used for the phase/frequency deviation and error measurements when you set the SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference) method to Edge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasedeviationrangelength__string-double.html language=enus -->
## TOPIC 00209: SetFrequencyAndPhaseDeviationRangeLength(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasedeviationrangelength__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasedeviationrangelength__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the length of the pulse data used for the phase/frequency deviation and error measurements when you set the SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference) method to Center. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int

### SetFrequencyAndPhaseDeviationRangeLength(string, double)

Sets the length of the pulse data used for the phase/frequency deviation and error measurements when you set the [SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasedeviationrangereference__string-rfmxpulsemxpulsefrequencyandphasedeviationrangereference.html) method to [Center](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsefrequencyandphasedeviationrangereference.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetFrequencyAndPhaseDeviationRangeLength(string selectorString, double value)

#### Remarks

This method sets the value of [PulseFrequencyAndPhaseDeviationRangeLength](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 75. Valid values are 0 to 100, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the length of the pulse data used for the phase/frequency deviation and error measurements when you set the SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference) method to Center. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasedeviationrangereference__string-rfmxpulsemxpulsefrequencyandphasedeviationrangereference.html language=enus -->
## TOPIC 00210: SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasedeviationrangereference__string-rfmxpulsemxpulsefrequencyandphasedeviationrangereference.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasedeviationrangereference__string-rfmxpulsemxpulsefrequencyandphasedeviationrangereference.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the reference used for the measurement range in phase/frequency deviation and error measurements. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetFrequencyAndPhaseDeviationRangeReference(string selectorString, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference value)Remarks

### SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference)

Sets the reference used for the measurement range in phase/frequency deviation and error measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetFrequencyAndPhaseDeviationRangeReference(string selectorString, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference value)

#### Remarks

This method sets the value of [PulseFrequencyAndPhaseDeviationRangeReference](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [Center](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsefrequencyandphasedeviationrangereference.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference | Specifies the reference used for the measurement range in phase/frequency deviation and error measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasemodulationtype__string-rfmxpulsemxpulsemodulationtype.html language=enus -->
## TOPIC 00211: SetFrequencyAndPhaseModulationType(string, RFmxPulseMXPulseModulationType)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasemodulationtype__string-rfmxpulsemxpulsemodulationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasemodulationtype__string-rfmxpulsemxpulsemodulationtype.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the pulse modulation type used for the phase and frequency error, and pulsed FM Measurement. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetFrequencyAndPhaseModulationType(string selectorString, RFmxPulseMXPulseModulationType value)RemarksThis method sets the value of PulseFrequ

### SetFrequencyAndPhaseModulationType(string, RFmxPulseMXPulseModulationType)

Sets the pulse modulation type used for the phase and frequency error, and pulsed FM Measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetFrequencyAndPhaseModulationType(string selectorString, RFmxPulseMXPulseModulationType value)

#### Remarks

This method sets the value of [PulseFrequencyAndPhaseModulationType](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [CW](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemodulationtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXPulseModulationType | Specifies the pulse modulation type used for the phase and frequency error, and pulsed FM Measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setlevelcomputationmethod__string-rfmxpulsemxpulselevelcomputationmethod.html language=enus -->
## TOPIC 00212: SetLevelComputationMethod(string, RFmxPulseMXPulseLevelComputationMethod)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setlevelcomputationmethod__string-rfmxpulsemxpulselevelcomputationmethod.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setlevelcomputationmethod__string-rfmxpulsemxpulselevelcomputationmethod.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the algorithm used to detect the pulse levels. The algorithm is based on the histogram method of level detection as defined in IEEE Std 181-2011. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetLevelComputationMethod(string selectorString, RFmxPulseMXPulseLevelComputationMethod v

### SetLevelComputationMethod(string, RFmxPulseMXPulseLevelComputationMethod)

Sets the algorithm used to detect the pulse levels. The algorithm is based on the histogram method of level detection as defined in *IEEE Std 181-2011*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetLevelComputationMethod(string selectorString, RFmxPulseMXPulseLevelComputationMethod value)

#### Remarks

This method sets the value of [PulseLevelComputationMethod](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [Median](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulselevelcomputationmethod.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXPulseLevelComputationMethod | Specifies the algorithm used to detect the pulse levels. The algorithm is based on the histogram method of level detection as defined in IEEE Std 181-2011. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setlowerthresholdlevel__string-double.html language=enus -->
## TOPIC 00213: SetLowerThresholdLevel(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setlowerthresholdlevel__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setlowerthresholdlevel__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the lower threshold level as a percentage of the pulse amplitude used to signify the start of a rising or end of a falling edge. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetLowerThresholdLevel(string selectorString, double value)RemarksThis method sets the value of PulseLower

### SetLowerThresholdLevel(string, double)

Sets the lower threshold level as a percentage of the pulse amplitude used to signify the start of a rising or end of a falling edge.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetLowerThresholdLevel(string selectorString, double value)

#### Remarks

This method sets the value of [PulseLowerThresholdLevel](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 10. Valid values are 0 to 100, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the lower threshold level as a percentage of the pulse amplitude used to signify the start of a rising or end of a falling edge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00214: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether pulse measurements are enabled.. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method sets the value of PulseMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescriptionselectorStr

### SetMeasurementEnabled(string, bool)

Sets whether pulse measurements are enabled..

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [PulseMeasurementEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether pulse measurements are enabled.. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmeasurementpointaveragingduration__string-double.html language=enus -->
## TOPIC 00215: SetMeasurementPointAveragingDuration(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmeasurementpointaveragingduration__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmeasurementpointaveragingduration__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the length of the averaging window centered at the measurement point. A minimum of 1 sample is used internally. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetMeasurementPointAveragingDuration(string selectorString, double value)RemarksThis method sets the value of PulseMeasurem

### SetMeasurementPointAveragingDuration(string, double)

Sets the length of the averaging window centered at the measurement point. A minimum of 1 sample is used internally.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetMeasurementPointAveragingDuration(string selectorString, double value)

#### Remarks

This method sets the value of [PulseMeasurementPointAveragingDuration](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the length of the averaging window centered at the measurement point. A minimum of 1 sample is used internally. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmeasurementpointoffset__string-double.html language=enus -->
## TOPIC 00216: SetMeasurementPointOffset(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmeasurementpointoffset__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmeasurementpointoffset__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the time offset of the measurement point within the pulse for phase, frequency, and stability measurements. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetMeasurementPointOffset(string selectorString, double value)RemarksThis method sets the value of PulseMeasurementPointOffset

### SetMeasurementPointOffset(string, double)

Sets the time offset of the measurement point within the pulse for phase, frequency, and stability measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetMeasurementPointOffset(string selectorString, double value)

#### Remarks

This method sets the value of [PulseMeasurementPointOffset](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the time offset of the measurement point within the pulse for phase, frequency, and stability measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmeasurementpointreference__string-rfmxpulsemxpulsemeasurementpointreference.html language=enus -->
## TOPIC 00217: SetMeasurementPointReference(string, RFmxPulseMXPulseMeasurementPointReference)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmeasurementpointreference__string-rfmxpulsemxpulsemeasurementpointreference.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmeasurementpointreference__string-rfmxpulsemxpulsemeasurementpointreference.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the reference used for the measurement point calculation, in phase, frequency, and stability measurements. You can set measurement point based on a reference and offset. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetMeasurementPointReference(string selectorString, RFmxPulseMXPu

### SetMeasurementPointReference(string, RFmxPulseMXPulseMeasurementPointReference)

Sets the reference used for the measurement point calculation, in phase, frequency, and stability measurements. You can set measurement point based on a reference and offset.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetMeasurementPointReference(string selectorString, RFmxPulseMXPulseMeasurementPointReference value)

#### Remarks

This method sets the value of [PulseMeasurementPointReference](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [Center](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemeasurementpointreference.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXPulseMeasurementPointReference | Specifies the reference used for the measurement point calculation, in phase, frequency, and stability measurements. You can set measurement point based on a reference and offset. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmetricsamplitudedeviationunit__string-rfmxpulsemxpulsemetricsamplitudedeviationunit.html language=enus -->
## TOPIC 00218: SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmetricsamplitudedeviationunit__string-rfmxpulsemxpulsemetricsamplitudedeviationunit.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmetricsamplitudedeviationunit__string-rfmxpulsemxpulsemetricsamplitudedeviationunit.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the unit for amplitude deviation results. This method is applicable only for droop, ripple and overshoot results. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetMetricsAmplitudeDeviationUnit(string selectorString, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit value)RemarksThis m

### SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit)

Sets the unit for amplitude deviation results. This method is applicable only for droop, ripple and overshoot results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetMetricsAmplitudeDeviationUnit(string selectorString, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit value)

#### Remarks

This method sets the value of [PulseMetricsAmplitudeDeviationUnit](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [Percentage](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemetricsamplitudedeviationunit.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXPulseMetricsAmplitudeDeviationUnit | Specifies the unit for amplitude deviation results. This method is applicable only for droop, ripple and overshoot results. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmetricsenabled__string-rfmxpulsemxpulsemetricsenabled.html language=enus -->
## TOPIC 00219: SetMetricsEnabled(string, RFmxPulseMXPulseMetricsEnabled)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmetricsenabled__string-rfmxpulsemxpulsemetricsenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmetricsenabled__string-rfmxpulsemxpulsemetricsenabled.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable pulse metrics results computation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetMetricsEnabled(string selectorString, RFmxPulseMXPulseMetricsEnabled value)RemarksThis method sets the value of PulseMetricsEnabled attribute.The default value is True.ParametersN

### SetMetricsEnabled(string, RFmxPulseMXPulseMetricsEnabled)

Sets whether to enable pulse metrics results computation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetMetricsEnabled(string selectorString, RFmxPulseMXPulseMetricsEnabled value)

#### Remarks

This method sets the value of [PulseMetricsEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemetricsenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXPulseMetricsEnabled | Specifies whether to enable pulse metrics results computation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmultiburstenabled__string-rfmxpulsemxmultiburstenabled.html language=enus -->
## TOPIC 00220: SetMultiburstEnabled(string, RFmxPulseMXMultiburstEnabled)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmultiburstenabled__string-rfmxpulsemxmultiburstenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmultiburstenabled__string-rfmxpulsemxmultiburstenabled.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable pulse measurements on the multiple burst transmission. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetMultiburstEnabled(string selectorString, RFmxPulseMXMultiburstEnabled value)RemarksThis method sets the value of PulseMultiburstEnabled attribute.The default v

### SetMultiburstEnabled(string, RFmxPulseMXMultiburstEnabled)

Sets whether to enable pulse measurements on the multiple burst transmission.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetMultiburstEnabled(string selectorString, RFmxPulseMXMultiburstEnabled value)

#### Remarks

This method sets the value of [PulseMultiburstEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-pulsemx-rfmxpulsemxmultiburstenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXMultiburstEnabled | Specifies whether to enable pulse measurements on the multiple burst transmission. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmultiburstlength__string-int.html language=enus -->
## TOPIC 00221: SetMultiburstLength(string, int)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmultiburstlength__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmultiburstlength__string-int.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of pulses assigned to a single burst. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetMultiburstLength(string selectorString, int value)RemarksThis method sets the value of PulseMultiburstLength attribute.The default value is 10.ParametersNameTypeDescriptionselectorStr

### SetMultiburstLength(string, int)

Sets the number of pulses assigned to a single burst.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetMultiburstLength(string selectorString, int value)

#### Remarks

This method sets the value of [PulseMultiburstLength](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of pulses assigned to a single burst. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmultiplemeasurementpointsenabled__string-rfmxpulsemxpulsemultiplemeasurementpointsenabled.html language=enus -->
## TOPIC 00222: SetMultipleMeasurementPointsEnabled(string, RFmxPulseMXPulseMultipleMeasurementPointsEnabled)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmultiplemeasurementpointsenabled__string-rfmxpulsemxpulsemultiplemeasurementpointsenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmultiplemeasurementpointsenabled__string-rfmxpulsemxpulsemultiplemeasurementpointsenabled.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable pulse stability measurements on multiple measurement points. This method is used to enable the multiple measurement points stability trace when you set the All Traces Enabled method to TRUE. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetMultipleMeasurementPoin

### SetMultipleMeasurementPointsEnabled(string, RFmxPulseMXPulseMultipleMeasurementPointsEnabled)

Sets whether to enable pulse stability measurements on multiple measurement points. This method is used to enable the multiple measurement points stability trace when you set the All Traces Enabled method to TRUE.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetMultipleMeasurementPointsEnabled(string selectorString, RFmxPulseMXPulseMultipleMeasurementPointsEnabled value)

#### Remarks

This method sets the value of [PulseMultipleMeasurementPointsEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemultiplemeasurementpointsenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXPulseMultipleMeasurementPointsEnabled | Specifies whether to enable pulse stability measurements on multiple measurement points. This method is used to enable the multiple measurement points stability trace when you set the All Traces Enabled method to TRUE. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmultiplemeasurementpointswindowstart__string-double.html language=enus -->
## TOPIC 00223: SetMultipleMeasurementPointsWindowStart(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmultiplemeasurementpointswindowstart__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmultiplemeasurementpointswindowstart__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the start of the measurement window used for multiple measurement points selection over pulse ON duration. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetMultipleMeasurementPointsWindowStart(string selectorString, double value)RemarksThis method sets the value of PulseMultipleMe

### SetMultipleMeasurementPointsWindowStart(string, double)

Sets the start of the measurement window used for multiple measurement points selection over pulse ON duration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetMultipleMeasurementPointsWindowStart(string selectorString, double value)

#### Remarks

This method sets the value of [PulseMultipleMeasurementPointsWindowStart](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 20. Valid values are 0 to 100, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the start of the measurement window used for multiple measurement points selection over pulse ON duration. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmultiplemeasurementpointswindowstepsize__string-double.html language=enus -->
## TOPIC 00224: SetMultipleMeasurementPointsWindowStepSize(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmultiplemeasurementpointswindowstepsize__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmultiplemeasurementpointswindowstepsize__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the step size of multiple measurement points selection within the measurement window over pulse ON duration. A minimum of 1 sample step size is used internally. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetMultipleMeasurementPointsWindowStepSize(string selectorString, double v

### SetMultipleMeasurementPointsWindowStepSize(string, double)

Sets the step size of multiple measurement points selection within the measurement window over pulse ON duration. A minimum of 1 sample step size is used internally.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetMultipleMeasurementPointsWindowStepSize(string selectorString, double value)

#### Remarks

This method sets the value of [PulseMultipleMeasurementPointsWindowStepSize](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the step size of multiple measurement points selection within the measurement window over pulse ON duration. A minimum of 1 sample step size is used internally. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmultiplemeasurementpointswindowstop__string-double.html language=enus -->
## TOPIC 00225: SetMultipleMeasurementPointsWindowStop(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmultiplemeasurementpointswindowstop__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setmultiplemeasurementpointswindowstop__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the stop of the measurement window used for multiple measurement points selection over pulse ON duration. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetMultipleMeasurementPointsWindowStop(string selectorString, double value)RemarksThis method sets the value of PulseMultipleMeas

### SetMultipleMeasurementPointsWindowStop(string, double)

Sets the stop of the measurement window used for multiple measurement points selection over pulse ON duration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetMultipleMeasurementPointsWindowStop(string selectorString, double value)

#### Remarks

This method sets the value of [PulseMultipleMeasurementPointsWindowStop](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 80. Valid values are 0 to 100, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the stop of the measurement window used for multiple measurement points selection over pulse ON duration. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setnumberofanalysisthreads__string-int.html language=enus -->
## TOPIC 00226: SetNumberOfAnalysisThreads(string, int)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setnumberofanalysisthreads__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setnumberofanalysisthreads__string-int.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the maximum number of threads used for parallelism for the pulse measurement. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetNumberOfAnalysisThreads(string selectorString, int value)RemarksThis method sets the value of PulseNumberOfAnalysisThreads attribute.The default value is

### SetNumberOfAnalysisThreads(string, int)

Sets the maximum number of threads used for parallelism for the pulse measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetNumberOfAnalysisThreads(string selectorString, int value)

#### Remarks

This method sets the value of [PulseNumberOfAnalysisThreads](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 1. Valid values are 1 to 10, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the maximum number of threads used for parallelism for the pulse measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setselectedbursttrace__string-int.html language=enus -->
## TOPIC 00227: SetSelectedBurstTrace(string, int)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setselectedbursttrace__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setselectedbursttrace__string-int.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the burst number selected for the display of traces. This method is applicable for IQ, amplitude and pulse stability traces. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetSelectedBurstTrace(string selectorString, int value)RemarksThis method sets the value of PulseSelectedBurst

### SetSelectedBurstTrace(string, int)

Sets the burst number selected for the display of traces. This method is applicable for IQ, amplitude and pulse stability traces.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetSelectedBurstTrace(string selectorString, int value)

#### Remarks

This method sets the value of [PulseSelectedBurstTrace](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the burst number selected for the display of traces. This method is applicable for IQ, amplitude and pulse stability traces. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setselectedpulsetrace__string-int.html language=enus -->
## TOPIC 00228: SetSelectedPulseTrace(string, int)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setselectedpulsetrace__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setselectedpulsetrace__string-int.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the pulse number selected for displaying the traces. This method is valid only for IQ, amplitude and pulse stability traces. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetSelectedPulseTrace(string selectorString, int value)RemarksThis method sets the value of PulseSelectedPulse

### SetSelectedPulseTrace(string, int)

Sets the pulse number selected for displaying the traces. This method is valid only for IQ, amplitude and pulse stability traces.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetSelectedPulseTrace(string selectorString, int value)

#### Remarks

This method sets the value of [PulseSelectedPulseTrace](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the pulse number selected for displaying the traces. This method is valid only for IQ, amplitude and pulse stability traces. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setstabilityenabled__string-rfmxpulsemxpulsestabilityenabled.html language=enus -->
## TOPIC 00229: SetStabilityEnabled(string, RFmxPulseMXPulseStabilityEnabled)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setstabilityenabled__string-rfmxpulsemxpulsestabilityenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setstabilityenabled__string-rfmxpulsemxpulsestabilityenabled.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable pulse stability results computation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetStabilityEnabled(string selectorString, RFmxPulseMXPulseStabilityEnabled value)RemarksThis method sets the value of PulseStabilityEnabled attribute.The default value is True.Par

### SetStabilityEnabled(string, RFmxPulseMXPulseStabilityEnabled)

Sets whether to enable pulse stability results computation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetStabilityEnabled(string selectorString, RFmxPulseMXPulseStabilityEnabled value)

#### Remarks

This method sets the value of [PulseStabilityEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsestabilityenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXPulseStabilityEnabled | Specifies whether to enable pulse stability results computation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setstabilityfrequencyerrorcompensation__string-rfmxpulsemxpulsestabilityfrequencyerrorcompensation.html language=enus -->
## TOPIC 00230: SetStabilityFrequencyErrorCompensation(string, RFmxPulseMXPulseStabilityFrequencyErrorCompensation)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setstabilityfrequencyerrorcompensation__string-rfmxpulsemxpulsestabilityfrequencyerrorcompensation.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setstabilityfrequencyerrorcompensation__string-rfmxpulsemxpulsestabilityfrequencyerrorcompensation.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to compute and correct the frequency offset for stability results computation. This is an optional setting and in negligible frequency error condition you must set this method to Off to avoid incorrect results. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetStabilityFreq

### SetStabilityFrequencyErrorCompensation(string, RFmxPulseMXPulseStabilityFrequencyErrorCompensation)

Sets whether to compute and correct the frequency offset for stability results computation. This is an optional setting and in negligible frequency error condition you must set this method to Off to avoid incorrect results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetStabilityFrequencyErrorCompensation(string selectorString, RFmxPulseMXPulseStabilityFrequencyErrorCompensation value)

#### Remarks

This method sets the value of [PulseStabilityFrequencyErrorCompensation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [Off](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsestabilityfrequencyerrorcompensation.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXPulseStabilityFrequencyErrorCompensation | Specifies whether to compute and correct the frequency offset for stability results computation. This is an optional setting and in negligible frequency error condition you must set this method to Off to avoid incorrect results. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setstabilitymeasurementoffset__string-int.html language=enus -->
## TOPIC 00231: SetStabilityMeasurementOffset(string, int)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setstabilitymeasurementoffset__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setstabilitymeasurementoffset__string-int.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the offset in number of pulses to be used for pulse stability measurement. This method is applicable for average stability results and pulse-to-pulse stabilty trace. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetStabilityMeasurementOffset(string selectorString, int value)Remark

### SetStabilityMeasurementOffset(string, int)

Sets the offset in number of pulses to be used for pulse stability measurement. This method is applicable for average stability results and pulse-to-pulse stabilty trace.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetStabilityMeasurementOffset(string selectorString, int value)

#### Remarks

This method sets the value of [PulseStabilityMeasurementOffset](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the offset in number of pulses to be used for pulse stability measurement. This method is applicable for average stability results and pulse-to-pulse stabilty trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setstabilitypulsetopulseoffset__string-int.html language=enus -->
## TOPIC 00232: SetStabilityPulseToPulseOffset(string, int)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setstabilitypulsetopulseoffset__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setstabilitypulsetopulseoffset__string-int.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the offset in number of pulses used for pulse-to-pulse stability measurement trace. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetStabilityPulseToPulseOffset(string selectorString, int value)RemarksThis method sets the value of PulseStabilityPulseToPulseOffset attribute.The def

### SetStabilityPulseToPulseOffset(string, int)

Sets the offset in number of pulses used for pulse-to-pulse stability measurement trace.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetStabilityPulseToPulseOffset(string selectorString, int value)

#### Remarks

This method sets the value of [PulseStabilityPulseToPulseOffset](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the offset in number of pulses used for pulse-to-pulse stability measurement trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setstabilityreferenceoffset__string-int.html language=enus -->
## TOPIC 00233: SetStabilityReferenceOffset(string, int)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setstabilityreferenceoffset__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setstabilityreferenceoffset__string-int.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the offset in number of pulses used for pulse stability reference computation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetStabilityReferenceOffset(string selectorString, int value)RemarksThis method sets the value of PulseStabilityReferenceOffset attribute.The default value

### SetStabilityReferenceOffset(string, int)

Sets the offset in number of pulses used for pulse stability reference computation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetStabilityReferenceOffset(string selectorString, int value)

#### Remarks

This method sets the value of [PulseStabilityReferenceOffset](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the offset in number of pulses used for pulse stability reference computation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-settimesidelobeenabled__string-rfmxpulsemxpulsetimesidelobeenabled.html language=enus -->
## TOPIC 00234: SetTimeSidelobeEnabled(string, RFmxPulseMXPulseTimeSidelobeEnabled)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-settimesidelobeenabled__string-rfmxpulsemxpulsetimesidelobeenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-settimesidelobeenabled__string-rfmxpulsemxpulsetimesidelobeenabled.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable pulse time sidelobe results computation. You can use the NationalInstruments.RFmx.PulseMX.RFmxPulseMXPulseConfiguration.Configure1ReferenceWaveform(string,NationalInstruments.ComplexWaveform<NationalInstruments.ComplexSingle>) function to set the reference waveform for correla

### SetTimeSidelobeEnabled(string, RFmxPulseMXPulseTimeSidelobeEnabled)

Sets whether to enable pulse time sidelobe results computation. You can use the NationalInstruments.RFmx.PulseMX.RFmxPulseMXPulseConfiguration.Configure1ReferenceWaveform(string,NationalInstruments.ComplexWaveform<NationalInstruments.ComplexSingle>) function to set the reference waveform for correlation computation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetTimeSidelobeEnabled(string selectorString, RFmxPulseMXPulseTimeSidelobeEnabled value)

#### Remarks

This method sets the value of [PulseTimeSidelobeEnabled](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsetimesidelobeenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXPulseTimeSidelobeEnabled | Specifies whether to enable pulse time sidelobe results computation. You can use the NationalInstruments.RFmx.PulseMX.RFmxPulseMXPulseConfiguration.Configure1ReferenceWaveform(string,NationalInstruments.ComplexWaveform<NationalInstruments.ComplexSingle>) function to set the reference waveform for correlation computation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-settimesidelobekeepouttime__string-double.html language=enus -->
## TOPIC 00235: SetTimeSidelobeKeepOutTime(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-settimesidelobekeepouttime__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-settimesidelobekeepouttime__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets keep out time for the time sidelobe measurements. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetTimeSidelobeKeepOutTime(string selectorString, double value)RemarksThis method sets the value of PulseTimeSidelobeKeepOutTime attribute.The default value is 0.000001 seconds.Paramete

### SetTimeSidelobeKeepOutTime(string, double)

Sets keep out time for the time sidelobe measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetTimeSidelobeKeepOutTime(string selectorString, double value)

#### Remarks

This method sets the value of [PulseTimeSidelobeKeepOutTime](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.000001 seconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies keep out time for the time sidelobe measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-settimesidelobekeepouttimeauto__string-rfmxpulsemxpulsetimesidelobekeepouttimeauto.html language=enus -->
## TOPIC 00236: SetTimeSidelobeKeepOutTimeAuto(string, RFmxPulseMXPulseTimeSidelobeKeepOutTimeAuto)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-settimesidelobekeepouttimeauto__string-rfmxpulsemxpulsetimesidelobekeepouttimeauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-settimesidelobekeepouttimeauto__string-rfmxpulsemxpulsetimesidelobekeepouttimeauto.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the keep out time computation for the time sidelobe measurements is automatic or manual. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetTimeSidelobeKeepOutTimeAuto(string selectorString, RFmxPulseMXPulseTimeSidelobeKeepOutTimeAuto value)RemarksThis method sets the value

### SetTimeSidelobeKeepOutTimeAuto(string, RFmxPulseMXPulseTimeSidelobeKeepOutTimeAuto)

Sets whether the keep out time computation for the time sidelobe measurements is automatic or manual.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetTimeSidelobeKeepOutTimeAuto(string selectorString, RFmxPulseMXPulseTimeSidelobeKeepOutTimeAuto value)

#### Remarks

This method sets the value of [PulseTimeSidelobeKeepOutTimeAuto](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsetimesidelobekeepouttimeauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXPulseTimeSidelobeKeepOutTimeAuto | Specifies whether the keep out time computation for the time sidelobe measurements is automatic or manual. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-settimesidelobeminimumcorrelation__string-double.html language=enus -->
## TOPIC 00237: SetTimeSidelobeMinimumCorrelation(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-settimesidelobeminimumcorrelation__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-settimesidelobeminimumcorrelation__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the minimum peak correlation value for the time sidelobe measurements. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetTimeSidelobeMinimumCorrelation(string selectorString, double value)RemarksThis method sets the value of PulseTimeSidelobeMinimumCorrelation attribute.The default

### SetTimeSidelobeMinimumCorrelation(string, double)

Sets the minimum peak correlation value for the time sidelobe measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetTimeSidelobeMinimumCorrelation(string selectorString, double value)

#### Remarks

This method sets the value of [PulseTimeSidelobeMinimumCorrelation](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.5.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the minimum peak correlation value for the time sidelobe measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-settimesidelobereferencewindowtype__string-rfmxpulsemxpulsetimesidelobereferencewindowtype.html language=enus -->
## TOPIC 00238: SetTimeSidelobeReferenceWindowType(string, RFmxPulseMXPulseTimeSidelobeReferenceWindowType)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-settimesidelobereferencewindowtype__string-rfmxpulsemxpulsetimesidelobereferencewindowtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-settimesidelobereferencewindowtype__string-rfmxpulsemxpulsetimesidelobereferencewindowtype.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the window type to be applied to the reference pulse to obtain correlated output for the time sidelobe measurements. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetTimeSidelobeReferenceWindowType(string selectorString, RFmxPulseMXPulseTimeSidelobeReferenceWindowType value)Remark

### SetTimeSidelobeReferenceWindowType(string, RFmxPulseMXPulseTimeSidelobeReferenceWindowType)

Sets the window type to be applied to the reference pulse to obtain correlated output for the time sidelobe measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetTimeSidelobeReferenceWindowType(string selectorString, RFmxPulseMXPulseTimeSidelobeReferenceWindowType value)

#### Remarks

This method sets the value of [PulseTimeSidelobeReferenceWindowType](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is [None](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsetimesidelobereferencewindowtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXPulseTimeSidelobeReferenceWindowType | Specifies the window type to be applied to the reference pulse to obtain correlated output for the time sidelobe measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-settracerangeauto__string-rfmxpulsemxpulsetracerangeauto.html language=enus -->
## TOPIC 00239: SetTraceRangeAuto(string, RFmxPulseMXPulseTraceRangeAuto)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-settracerangeauto__string-rfmxpulsemxpulsetracerangeauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-settracerangeauto__string-rfmxpulsemxpulsetracerangeauto.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the trace range computation of the selected pulse is automatic or manually configured by you. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetTraceRangeAuto(string selectorString, RFmxPulseMXPulseTraceRangeAuto value)RemarksThis method sets the value of PulseTraceRangeAut

### SetTraceRangeAuto(string, RFmxPulseMXPulseTraceRangeAuto)

Sets whether the trace range computation of the selected pulse is automatic or manually configured by you.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetTraceRangeAuto(string selectorString, RFmxPulseMXPulseTraceRangeAuto value)

#### Remarks

This method sets the value of [PulseTraceRangeAuto](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is *RFmxPulseMXTraceRangeAuto.True*.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXPulseTraceRangeAuto | Specifies whether the trace range computation of the selected pulse is automatic or manually configured by you. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-settracerangelength__string-double.html language=enus -->
## TOPIC 00240: SetTraceRangeLength(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-settracerangelength__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-settracerangelength__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the length in seconds of the trace range centered at the reference point. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetTraceRangeLength(string selectorString, double value)RemarksThis method sets the value of PulseTraceRangeLength attribute.The default value is 0.000020 second

### SetTraceRangeLength(string, double)

Sets the length in seconds of the trace range centered at the reference point.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetTraceRangeLength(string selectorString, double value)

#### Remarks

This method sets the value of [PulseTraceRangeLength](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.000020 seconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the length in seconds of the trace range centered at the reference point. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-settracerangeoffset__string-double.html language=enus -->
## TOPIC 00241: SetTraceRangeOffset(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-settracerangeoffset__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-settracerangeoffset__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the time offset in seconds from the reference point to position the trace range. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetTraceRangeOffset(string selectorString, double value)RemarksThis method sets the value of PulseTraceRangeOffset attribute.The default value is 0.Parame

### SetTraceRangeOffset(string, double)

Sets the time offset in seconds from the reference point to position the trace range.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetTraceRangeOffset(string selectorString, double value)

#### Remarks

This method sets the value of [PulseTraceRangeOffset](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the time offset in seconds from the reference point to position the trace range. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-settracerangereference__string-rfmxpulsemxpulsetracerangereference.html language=enus -->
## TOPIC 00242: SetTraceRangeReference(string, RFmxPulseMXPulseTraceRangeReference)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-settracerangereference__string-rfmxpulsemxpulsetracerangereference.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-settracerangereference__string-rfmxpulsemxpulsetracerangereference.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the reference point for positioning of trace range. You can set reference point based on reference and Pulse Trace Range Offset (s) value. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetTraceRangeReference(string selectorString, RFmxPulseMXPulseTraceRangeReference value)RemarksT

### SetTraceRangeReference(string, RFmxPulseMXPulseTraceRangeReference)

Sets the reference point for positioning of trace range. You can set reference point based on reference and Pulse Trace Range Offset (s) value.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetTraceRangeReference(string selectorString, RFmxPulseMXPulseTraceRangeReference value)

#### Remarks

This method sets the value of [PulseTraceRangeReference](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is *RFmxPulseMXTraceRangeReference.Center*.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxPulseMXPulseTraceRangeReference | Specifies the reference point for positioning of trace range. You can set reference point based on reference and Pulse Trace Range Offset (s) value. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setupperthresholdlevel__string-double.html language=enus -->
## TOPIC 00243: SetUpperThresholdLevel(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setupperthresholdlevel__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setupperthresholdlevel__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the upper threshold level as a percentage of the pulse amplitude used to signify the end of a rising edge or beginning of a falling edge. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetUpperThresholdLevel(string selectorString, double value)RemarksThis method sets the value of P

### SetUpperThresholdLevel(string, double)

Sets the upper threshold level as a percentage of the pulse amplitude used to signify the end of a rising edge or beginning of a falling edge.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetUpperThresholdLevel(string selectorString, double value)

#### Remarks

This method sets the value of [PulseUpperThresholdLevel](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 90. Valid values are 0 to 100, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the upper threshold level as a percentage of the pulse amplitude used to signify the end of a rising edge or beginning of a falling edge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setwidththresholdlevel__string-double.html language=enus -->
## TOPIC 00244: SetWidthThresholdLevel(string, double)

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setwidththresholdlevel__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setwidththresholdlevel__string-double.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the middle threshold level as a percentage of the pulse amplitude used to signify the mid-transition level between pulse states used for pulse width computation. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic int SetWidthThresholdLevel(string selectorString, double value)RemarksThis me

### SetWidthThresholdLevel(string, double)

Sets the middle threshold level as a percentage of the pulse amplitude used to signify the mid-transition level between pulse states used for pulse width computation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public int SetWidthThresholdLevel(string selectorString, double value)

#### Remarks

This method sets the value of [PulseWidthThresholdLevel](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpropertyid.html) attribute.The default value is 50. Valid values are 0 to 100, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the middle threshold level as a percentage of the pulse amplitude used to signify the mid-transition level between pulse states used for pulse width computation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxPulseMXPulseConfiguration Class

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration.html language=enus -->
## TOPIC 00245: RFmxPulseMXPulseConfiguration Class

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the Pulse measurement. Derives fromRFmxPulseMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic class RFmxPulseMXPulseConfiguration : RFmxPulseMXSubObjectMethodsNameDescriptionConfigure1ReferenceWaveform(string, ComplexWaveform< ComplexSingle >)Configures

### RFmxPulseMXPulseConfiguration Class

Provides methods to configure the Pulse measurement.

#### Derives from

- RFmxPulseMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public class RFmxPulseMXPulseConfiguration : RFmxPulseMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| Configure1ReferenceWaveform(string, ComplexWaveform< ComplexSingle >) | Configures the reference pulse waveform used for time sidelobe measurements. |
| GetAcquisitionTraceSelect(string, out RFmxPulseMXPulseAcquisitionTraceSelect) | Gets the mode to select all pulses or the subset of acquired pulses available for display acquisition trace, limited to MaximumPulseCountEnabled method if set to True. |
| GetAcquisitionTraceSubsetLength(string, out int) | Gets the total number of pulses starting from offset to be used for display acquisition trace. You must configure this method when you set the PulseAcquisitionTraceSelect method to Subset. Set length to 0 to disable the acquisition trace. |
| GetAcquisitionTraceSubsetOffset(string, out int) | Gets the offset in number of pulses to be used for display acquisition trace. You must configure this method when you set the PulseAcquisitionTraceSelect method to Subset. |
| GetAllTracesEnabled(string, out bool) | Gets whether to enable storing and retrieving traces after performing the measurements. |
| GetAmplitudeLevelDomain(string, out RFmxPulseMXPulseAmplitudeLevelDomain) | Gets whether voltage or power to be used as domain for pulse measurements. |
| GetAmplitudeTraceUnit(string, out RFmxPulseMXPulseAmplitudeTraceUnit) | Gets the unit of the amplitude level. This method is applicable only for the amplitude and acquired amplitude trace. |
| GetDetectionHysteresis(string, out double) | Gets the hysteresis for pulse detection in dB for the defined threshold. |
| GetDetectionMaximumWidth(string, out double) | Gets the maximum pulse width time to be considered for pulse detection. Any detected pulse width time above the specified value will be ignored by the pulse detection. This value is expressed in seconds. |
| GetDetectionMinimumOffDuration(string, out double) | Gets the minimum pulse off duration to be ignored by the pulse detection. This value is expressed in seconds. |
| GetDetectionMinimumWidth(string, out double) | Gets the minimum pulse width time to be considered for pulse detection. Any detected pulse width time below the specified value will be ignored by the pulse detection. This value is expressed in seconds. |
| GetDetectionReference(string, out RFmxPulseMXPulseDetectionReference) | Gets the reference used for SetDetectionThreshold(string, double) method. |
| GetDetectionThreshold(string, out double) | Gets the threshold used for pulse detection. The unit dB or dBm is based on the value you set to the SetDetectionReference(string, RFmxPulseMXPulseDetectionReference) method. |
| GetDroopCompensationEnabled(string, out RFmxPulseMXPulseDroopCompensationEnabled) | Gets whether to compensate the droop detected in pulse level when applying thresholds. |
| GetFrequencyAndPhaseCWFrequencyOffset(string, out double) | Gets to manually enter the CW frequency offset. This method is valid only when you set the SetFrequencyAndPhaseModulationType(string, RFmxPulseMXPulseModulationType) method to CW. |
| GetFrequencyAndPhaseCWFrequencyOffsetAuto(string, out RFmxPulseMXPulseCWFrequencyOffsetAuto) | Gets whether the CW frequency offset computation of every detected pulse is automatic or manual. This method is valid only when you set the SetFrequencyAndPhaseModulationType(string, RFmxPulseMXPulseModulationType) method to CW. |
| GetFrequencyAndPhaseDeviationRangeEdgeStart(string, out double) | Gets the start of the pulse data used for the phase/frequency deviation and error measurements when you set the SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference) method to Edge. |
| GetFrequencyAndPhaseDeviationRangeEdgeStop(string, out double) | Gets the stop of the pulse data used for the phase/frequency deviation and error measurements when you set the SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference) method to Edge. |
| GetFrequencyAndPhaseDeviationRangeLength(string, out double) | Gets the length of the pulse data used for the phase/frequency deviation and error measurements when you set the SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference) method to Center. |
| GetFrequencyAndPhaseDeviationRangeReference(string, out RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference) | Gets the reference used for the measurement range in phase/frequency deviation and error measurements. |
| GetFrequencyAndPhaseModulationType(string, out RFmxPulseMXPulseModulationType) | Gets the pulse modulation type used for the phase and frequency error, and pulsed FM Measurement. |
| GetLevelComputationMethod(string, out RFmxPulseMXPulseLevelComputationMethod) | Gets the algorithm used to detect the pulse levels. The algorithm is based on the histogram method of level detection as defined in IEEE Std 181-2011. |
| GetLowerThresholdLevel(string, out double) | Gets the lower threshold level as a percentage of the pulse amplitude used to signify the start of a rising or end of a falling edge. |
| GetMeasurementEnabled(string, out bool) | Gets whether pulse measurements are enabled.. |
| GetMeasurementPointAveragingDuration(string, out double) | Gets the length of the averaging window centered at the measurement point. A minimum of 1 sample is used internally. |
| GetMeasurementPointOffset(string, out double) | Gets the time offset of the measurement point within the pulse for phase, frequency, and stability measurements. |
| GetMeasurementPointReference(string, out RFmxPulseMXPulseMeasurementPointReference) | Gets the reference used for the measurement point calculation, in phase, frequency, and stability measurements. You can set measurement point based on a reference and offset. |
| GetMetricsAmplitudeDeviationUnit(string, out RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) | Gets the unit for amplitude deviation results. This method is applicable only for droop, ripple and overshoot results. |
| GetMetricsEnabled(string, out RFmxPulseMXPulseMetricsEnabled) | Gets whether to enable pulse metrics results computation. |
| GetMultiburstEnabled(string, out RFmxPulseMXMultiburstEnabled) | Gets whether to enable pulse measurements on the multiple burst transmission. |
| GetMultiburstLength(string, out int) | Gets the number of pulses assigned to a single burst. |
| GetMultipleMeasurementPointsEnabled(string, out RFmxPulseMXPulseMultipleMeasurementPointsEnabled) | Gets whether to enable pulse stability measurements on multiple measurement points. This method is used to enable the multiple measurement points stability trace when you set the All Traces Enabled method to TRUE. |
| GetMultipleMeasurementPointsWindowStart(string, out double) | Gets the start of the measurement window used for multiple measurement points selection over pulse ON duration. |
| GetMultipleMeasurementPointsWindowStepSize(string, out double) | Gets the step size of multiple measurement points selection within the measurement window over pulse ON duration. A minimum of 1 sample step size is used internally. |
| GetMultipleMeasurementPointsWindowStop(string, out double) | Gets the stop of the measurement window used for multiple measurement points selection over pulse ON duration. |
| GetNumberOfAnalysisThreads(string, out int) | Gets the maximum number of threads used for parallelism for the pulse measurement. |
| GetSelectedBurstTrace(string, out int) | Gets the burst number selected for the display of traces. This method is applicable for IQ, amplitude and pulse stability traces. |
| GetSelectedPulseTrace(string, out int) | Gets the pulse number selected for displaying the traces. This method is valid only for IQ, amplitude and pulse stability traces. |
| GetStabilityEnabled(string, out RFmxPulseMXPulseStabilityEnabled) | Gets whether to enable pulse stability results computation. |
| GetStabilityFrequencyErrorCompensation(string, out RFmxPulseMXPulseStabilityFrequencyErrorCompensation) | Gets whether to compute and correct the frequency offset for stability results computation. This is an optional setting and in negligible frequency error condition you must set this method to Off to avoid incorrect results. |
| GetStabilityMeasurementOffset(string, out int) | Gets the offset in number of pulses to be used for pulse stability measurement. This method is applicable for average stability results and pulse-to-pulse stabilty trace. |
| GetStabilityPulseToPulseOffset(string, out int) | Gets the offset in number of pulses used for pulse-to-pulse stability measurement trace. |
| GetStabilityReferenceOffset(string, out int) | Gets the offset in number of pulses used for pulse stability reference computation. |
| GetTimeSidelobeEnabled(string, out RFmxPulseMXPulseTimeSidelobeEnabled) | Gets whether to enable pulse time sidelobe results computation. You can use the NationalInstruments.RFmx.PulseMX.RFmxPulseMXPulseConfiguration.Configure1ReferenceWaveform(string,NationalInstruments.ComplexWaveform<NationalInstruments.ComplexSingle>) function to set the reference waveform for correlation computation. |
| GetTimeSidelobeKeepOutTime(string, out double) | Gets keep out time for the time sidelobe measurements. |
| GetTimeSidelobeKeepOutTimeAuto(string, out RFmxPulseMXPulseTimeSidelobeKeepOutTimeAuto) | Gets whether the keep out time computation for the time sidelobe measurements is automatic or manual. |
| GetTimeSidelobeMinimumCorrelation(string, out double) | Gets the minimum peak correlation value for the time sidelobe measurements. |
| GetTimeSidelobeReferenceWindowType(string, out RFmxPulseMXPulseTimeSidelobeReferenceWindowType) | Gets the window type to be applied to the reference pulse to obtain correlated output for the time sidelobe measurements. |
| GetTraceRangeAuto(string, out RFmxPulseMXPulseTraceRangeAuto) | Gets whether the trace range computation of the selected pulse is automatic or manually configured by you. |
| GetTraceRangeLength(string, out double) | Gets the length in seconds of the trace range centered at the reference point. |
| GetTraceRangeOffset(string, out double) | Gets the time offset in seconds from the reference point to position the trace range. |
| GetTraceRangeReference(string, out RFmxPulseMXPulseTraceRangeReference) | Gets the reference point for positioning of trace range. You can set reference point based on reference and Pulse Trace Range Offset (s) value. |
| GetUpperThresholdLevel(string, out double) | Gets the upper threshold level as a percentage of the pulse amplitude used to signify the end of a rising edge or beginning of a falling edge. |
| GetWidthThresholdLevel(string, out double) | Gets the middle threshold level as a percentage of the pulse amplitude used to signify the mid-transition level between pulse states used for pulse width computation. |
| SetAcquisitionTraceSelect(string, RFmxPulseMXPulseAcquisitionTraceSelect) | Sets the mode to select all pulses or the subset of acquired pulses available for display acquisition trace, limited to MaximumPulseCountEnabled method if set to True. |
| SetAcquisitionTraceSubsetLength(string, int) | Sets the total number of pulses starting from offset to be used for display acquisition trace. You must configure this method when you set the PulseAcquisitionTraceSelect method to Subset. Set length to 0 to disable the acquisition trace. |
| SetAcquisitionTraceSubsetOffset(string, int) | Sets the offset in number of pulses to be used for display acquisition trace. You must configure this method when you set the PulseAcquisitionTraceSelect method to Subset. |
| SetAllTracesEnabled(string, bool) | Sets whether to enable storing and retrieving traces after performing the measurements. |
| SetAmplitudeLevelDomain(string, RFmxPulseMXPulseAmplitudeLevelDomain) | Sets whether voltage or power to be used as domain for pulse measurements. |
| SetAmplitudeTraceUnit(string, RFmxPulseMXPulseAmplitudeTraceUnit) | Sets the unit of the amplitude level. This method is applicable only for the amplitude trace. |
| SetDetectionHysteresis(string, double) | Sets the hysteresis for pulse detection in dB for the defined threshold. |
| SetDetectionMaximumWidth(string, double) | Sets the maximum pulse width time to be considered for pulse detection. Any detected pulse width time above the specified value will be ignored by the pulse detection. This value is expressed in seconds. |
| SetDetectionMinimumOffDuration(string, double) | Sets the minimum pulse off duration to be ignored by the pulse detection. This value is expressed in seconds. |
| SetDetectionMinimumWidth(string, double) | Sets the minimum pulse width time to be considered for pulse detection. Any detected pulse width time below the specified value will be ignored by the pulse detection. This value is expressed in seconds. |
| SetDetectionReference(string, RFmxPulseMXPulseDetectionReference) | Sets the reference used for SetDetectionThreshold(string, double) method. |
| SetDetectionThreshold(string, double) | Sets the threshold used for pulse detection. The unit dB or dBm is based on the value you set to the SetDetectionReference(string, RFmxPulseMXPulseDetectionReference) method. |
| SetDroopCompensationEnabled(string, RFmxPulseMXPulseDroopCompensationEnabled) | Sets whether to compensate the droop detected in pulse level when applying thresholds. |
| SetFrequencyAndPhaseCWFrequencyOffset(string, double) | Sets to manually enter the CW frequency offset. This method is valid only when you set the SetFrequencyAndPhaseModulationType(string, RFmxPulseMXPulseModulationType) method to CW. |
| SetFrequencyAndPhaseCWFrequencyOffsetAuto(string, RFmxPulseMXPulseCWFrequencyOffsetAuto) | Sets whether the CW frequency offset computation of every detected pulse is automatic or manual. This method is valid only when you set the SetFrequencyAndPhaseModulationType(string, RFmxPulseMXPulseModulationType) method to CW. |
| SetFrequencyAndPhaseDeviationRangeEdgeStart(string, double) | Sets the start of the pulse data used for the phase/frequency deviation and error measurements when you set the SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference) method to Edge. |
| SetFrequencyAndPhaseDeviationRangeEdgeStop(string, double) | Sets the stop of the pulse data used for the phase/frequency deviation and error measurements when you set the SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference) method to Edge. |
| SetFrequencyAndPhaseDeviationRangeLength(string, double) | Sets the length of the pulse data used for the phase/frequency deviation and error measurements when you set the SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference) method to Center. |
| SetFrequencyAndPhaseDeviationRangeReference(string, RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference) | Sets the reference used for the measurement range in phase/frequency deviation and error measurements. |
| SetFrequencyAndPhaseModulationType(string, RFmxPulseMXPulseModulationType) | Sets the pulse modulation type used for the phase and frequency error, and pulsed FM Measurement. |
| SetLevelComputationMethod(string, RFmxPulseMXPulseLevelComputationMethod) | Sets the algorithm used to detect the pulse levels. The algorithm is based on the histogram method of level detection as defined in IEEE Std 181-2011. |
| SetLowerThresholdLevel(string, double) | Sets the lower threshold level as a percentage of the pulse amplitude used to signify the start of a rising or end of a falling edge. |
| SetMeasurementEnabled(string, bool) | Sets whether pulse measurements are enabled.. |
| SetMeasurementPointAveragingDuration(string, double) | Sets the length of the averaging window centered at the measurement point. A minimum of 1 sample is used internally. |
| SetMeasurementPointOffset(string, double) | Sets the time offset of the measurement point within the pulse for phase, frequency, and stability measurements. |
| SetMeasurementPointReference(string, RFmxPulseMXPulseMeasurementPointReference) | Sets the reference used for the measurement point calculation, in phase, frequency, and stability measurements. You can set measurement point based on a reference and offset. |
| SetMetricsAmplitudeDeviationUnit(string, RFmxPulseMXPulseMetricsAmplitudeDeviationUnit) | Sets the unit for amplitude deviation results. This method is applicable only for droop, ripple and overshoot results. |
| SetMetricsEnabled(string, RFmxPulseMXPulseMetricsEnabled) | Sets whether to enable pulse metrics results computation. |
| SetMultiburstEnabled(string, RFmxPulseMXMultiburstEnabled) | Sets whether to enable pulse measurements on the multiple burst transmission. |
| SetMultiburstLength(string, int) | Sets the number of pulses assigned to a single burst. |
| SetMultipleMeasurementPointsEnabled(string, RFmxPulseMXPulseMultipleMeasurementPointsEnabled) | Sets whether to enable pulse stability measurements on multiple measurement points. This method is used to enable the multiple measurement points stability trace when you set the All Traces Enabled method to TRUE. |
| SetMultipleMeasurementPointsWindowStart(string, double) | Sets the start of the measurement window used for multiple measurement points selection over pulse ON duration. |
| SetMultipleMeasurementPointsWindowStepSize(string, double) | Sets the step size of multiple measurement points selection within the measurement window over pulse ON duration. A minimum of 1 sample step size is used internally. |
| SetMultipleMeasurementPointsWindowStop(string, double) | Sets the stop of the measurement window used for multiple measurement points selection over pulse ON duration. |
| SetNumberOfAnalysisThreads(string, int) | Sets the maximum number of threads used for parallelism for the pulse measurement. |
| SetSelectedBurstTrace(string, int) | Sets the burst number selected for the display of traces. This method is applicable for IQ, amplitude and pulse stability traces. |
| SetSelectedPulseTrace(string, int) | Sets the pulse number selected for displaying the traces. This method is valid only for IQ, amplitude and pulse stability traces. |
| SetStabilityEnabled(string, RFmxPulseMXPulseStabilityEnabled) | Sets whether to enable pulse stability results computation. |
| SetStabilityFrequencyErrorCompensation(string, RFmxPulseMXPulseStabilityFrequencyErrorCompensation) | Sets whether to compute and correct the frequency offset for stability results computation. This is an optional setting and in negligible frequency error condition you must set this method to Off to avoid incorrect results. |
| SetStabilityMeasurementOffset(string, int) | Sets the offset in number of pulses to be used for pulse stability measurement. This method is applicable for average stability results and pulse-to-pulse stabilty trace. |
| SetStabilityPulseToPulseOffset(string, int) | Sets the offset in number of pulses used for pulse-to-pulse stability measurement trace. |
| SetStabilityReferenceOffset(string, int) | Sets the offset in number of pulses used for pulse stability reference computation. |
| SetTimeSidelobeEnabled(string, RFmxPulseMXPulseTimeSidelobeEnabled) | Sets whether to enable pulse time sidelobe results computation. You can use the NationalInstruments.RFmx.PulseMX.RFmxPulseMXPulseConfiguration.Configure1ReferenceWaveform(string,NationalInstruments.ComplexWaveform<NationalInstruments.ComplexSingle>) function to set the reference waveform for correlation computation. |
| SetTimeSidelobeKeepOutTime(string, double) | Sets keep out time for the time sidelobe measurements. |
| SetTimeSidelobeKeepOutTimeAuto(string, RFmxPulseMXPulseTimeSidelobeKeepOutTimeAuto) | Sets whether the keep out time computation for the time sidelobe measurements is automatic or manual. |
| SetTimeSidelobeMinimumCorrelation(string, double) | Sets the minimum peak correlation value for the time sidelobe measurements. |
| SetTimeSidelobeReferenceWindowType(string, RFmxPulseMXPulseTimeSidelobeReferenceWindowType) | Sets the window type to be applied to the reference pulse to obtain correlated output for the time sidelobe measurements. |
| SetTraceRangeAuto(string, RFmxPulseMXPulseTraceRangeAuto) | Sets whether the trace range computation of the selected pulse is automatic or manually configured by you. |
| SetTraceRangeLength(string, double) | Sets the length in seconds of the trace range centered at the reference point. |
| SetTraceRangeOffset(string, double) | Sets the time offset in seconds from the reference point to position the trace range. |
| SetTraceRangeReference(string, RFmxPulseMXPulseTraceRangeReference) | Sets the reference point for positioning of trace range. You can set reference point based on reference and Pulse Trace Range Offset (s) value. |
| SetUpperThresholdLevel(string, double) | Sets the upper threshold level as a percentage of the pulse amplitude used to signify the end of a rising edge or beginning of a falling edge. |
| SetWidthThresholdLevel(string, double) | Sets the middle threshold level as a percentage of the pulse amplitude used to signify the mid-transition level between pulse states used for pulse width computation. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsecwfrequencyoffsetauto.html language=enus -->
## TOPIC 00246: RFmxPulseMXPulseCWFrequencyOffsetAuto Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsecwfrequencyoffsetauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsecwfrequencyoffsetauto.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the CW frequency offset computation of every detected pulse is automatic or manual. This method is valid only when you set the SetFrequencyAndPhaseModulationType(string, RFmxPulseMXPulseModulationType) method to CW. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxP

### RFmxPulseMXPulseCWFrequencyOffsetAuto Enumeration

Specifies whether the CW frequency offset computation of every detected pulse is automatic or manual. This method is valid only when you set the [SetFrequencyAndPhaseModulationType(string, RFmxPulseMXPulseModulationType)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setfrequencyandphasemodulationtype__string-rfmxpulsemxpulsemodulationtype.html) method to [CW](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsemodulationtype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXPulseCWFrequencyOffsetAuto

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | CW frequency offset computation is set to manual. |
| True | 1 | CW frequency offset computation is set to automatic. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsedetectionreference.html language=enus -->
## TOPIC 00247: RFmxPulseMXPulseDetectionReference Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsedetectionreference.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsedetectionreference.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference used for SetDetectionThreshold(string, double) method. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXPulseDetectionReferenceMembersNameValueDescriptionReferenceLevel0The threshold is relative to the reference level of the samples. Absolute1The thresh

### RFmxPulseMXPulseDetectionReference Enumeration

Specifies the reference used for [SetDetectionThreshold(string, double)](nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulseconfiguration-setdetectionthreshold__string-double.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXPulseDetectionReference

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ReferenceLevel | 0 | The threshold is relative to the reference level of the samples. |
| Absolute | 1 | The threshold is the absolute power, in dBm. |
| Peak | 2 | The threshold is relative to the peak level of the samples. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsedroopcompensationenabled.html language=enus -->
## TOPIC 00248: RFmxPulseMXPulseDroopCompensationEnabled Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsedroopcompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsedroopcompensationenabled.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to compensate the droop detected in pulse level when applying thresholds. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXPulseDroopCompensationEnabledMembersNameValueDescriptionFalse0Droop Compensation is disabled. True1Droop Compensation is enabled.

### RFmxPulseMXPulseDroopCompensationEnabled Enumeration

Specifies whether to compensate the droop detected in pulse level when applying thresholds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXPulseDroopCompensationEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Droop Compensation is disabled. |
| True | 1 | Droop Compensation is enabled. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsefrequencyandphasedeviationrangereference.html language=enus -->
## TOPIC 00249: RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsefrequencyandphasedeviationrangereference.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulsefrequencyandphasedeviationrangereference.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference used for the measurement range in phase/frequency deviation and error measurements. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReferenceMembersNameValueDescriptionEdge0Specifies the range with respect to the edg

### RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference Enumeration

Specifies the reference used for the measurement range in phase/frequency deviation and error measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXPulseFrequencyAndPhaseDeviationRangeReference

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Edge | 0 | Specifies the range with respect to the edges of the pulse. |
| Center | 1 | Specifies the range with respect to the center of the pulse. |

Parent topic:

NationalInstruments.RFmx.PulseMX

<!--NI_TOPIC bundle=rfmxpulse-dotnet-api-ref path=nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulselevelcomputationmethod.html language=enus -->
## TOPIC 00250: RFmxPulseMXPulseLevelComputationMethod Enumeration

- bundle_id: `rfmxpulse-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulselevelcomputationmethod.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-pulsemx-rfmxpulsemxpulselevelcomputationmethod.html
- document_id: `rfmxpulse-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the algorithm used to detect the pulse levels. The algorithm is based on the histogram method of level detection as defined in IEEE Std 181-2011. SyntaxNamespace: NationalInstruments.RFmx.PulseMXpublic enum RFmxPulseMXPulseLevelComputationMethodMembersNameValueDescriptionMean0The levels de

### RFmxPulseMXPulseLevelComputationMethod Enumeration

Specifies the algorithm used to detect the pulse levels. The algorithm is based on the histogram method of level detection as defined in *IEEE Std 181-2011*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.PulseMX](nationalinstruments-rfmx-pulsemx.html)

public enum RFmxPulseMXPulseLevelComputationMethod

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Mean | 0 | The levels derived as the pulse sub-histogram mean levels. |
| Median | 1 | The levels derived as the pulse sub-histogram median levels. |
| Mode | 2 | The levels derived as the pulse sub-histogram mode levels. |

Parent topic:

NationalInstruments.RFmx.PulseMX
