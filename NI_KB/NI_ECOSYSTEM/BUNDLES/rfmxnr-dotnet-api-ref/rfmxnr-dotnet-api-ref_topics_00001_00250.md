# NI DOCUMENT BUNDLE: rfmxnr-dotnet-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxnr-dotnet-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxnrmxextension-getnrlist__this-string.html language=enus -->
## TOPIC 00001: GetNRList(this RFmxInstrMX, string)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxnrmxextension-getnrlist__this-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxnrmxextension-getnrlist__this-string.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new NR list if it doesn't exist; otherwise, it returns the existing NR list. SyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic static RFmxNRMXList GetNRList(this RFmxInstrMX instrSession, string listName)ParametersNameTypeDescriptioninstrSessionthis RFmxInstrMXSpecifies an instr sess

### GetNRList(this RFmxInstrMX, string)

Creates a new NR list if it doesn't exist; otherwise, it returns the existing NR list.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public static [RFmxNRMXList](nationalinstruments-rfmx-nrmx-rfmxnrmxlist.html) GetNRList(this RFmxInstrMX instrSession, string listName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| instrSession | this RFmxInstrMX | Specifies an instr session. |
| listName | string | Specifies the name of the list. This parameter accepts the list name with or without the "list::" prefix. Example: "list::list1" "list1" |

#### Returns

Returns an object of type RFmxNRMXList.

Parent topic:

RFmxNRMXExtension Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-instrmx.html language=enus -->
## TOPIC 00002: NationalInstruments.RFmx.InstrMX

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionRFmxNRMXExtensionProvides extension methods to create NR signal configuration. These methods are added to RFmxInstrMX class. InterfacesNoneStructuresNoneEnumerationsNoneDelegatesNone

### NationalInstruments.RFmx.InstrMX

#### Classes

| Name | Description |
| --- | --- |
| RFmxNRMXExtension | Provides extension methods to create NR signal configuration. These methods are added to RFmxInstrMX class. |

#### Interfaces

None

#### Structures

None

#### Enumerations

None

#### Delegates

None

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-abortmeasurements__string.html language=enus -->
## TOPIC 00003: AbortMeasurements(string)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-abortmeasurements__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-abortmeasurements__string.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops acquisition and measurements associated with signal instance that you specify in the selectorString parameter, which were previously initiated by the Initiate(string, string) method or measurement read methods. Calling this method is optional, unless you want to stop a measurement before it is

### AbortMeasurements(string)

Stops acquisition and measurements associated with signal instance that you specify in the *selectorString* parameter, which were previously initiated by the [Initiate(string, string)](nationalinstruments-rfmx-nrmx-rfmxnrmx-initiate__string-string.html) method or measurement read methods. Calling this method is optional, unless you want to stop a measurement before it is complete. This method executes even if there is an incoming error.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int AbortMeasurements(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-acp.html language=enus -->
## TOPIC 00004: Acp

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-acp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-acp.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxNRMXAcp instance that represents the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic RFmxNRMXAcp Acp { get; }

### Acp

Gets the [RFmxNRMXAcp](nationalinstruments-rfmx-nrmx-rfmxnrmxacp.html) instance that represents the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public [RFmxNRMXAcp](nationalinstruments-rfmx-nrmx-rfmxnrmxacp.html) Acp { get; }

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-analyzeiq1waveform__string-string-complexwaveform_complexsingle_-bool-long.html language=enus -->
## TOPIC 00005: AnalyzeIQ1Waveform(string, string, ComplexWaveform< ComplexSingle >, bool, long)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-analyzeiq1waveform__string-string-complexwaveform_complexsingle_-bool-long.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-analyzeiq1waveform__string-string-complexwaveform_complexsingle_-bool-long.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods in the method node. Use this method only if the Recomme

### AnalyzeIQ1Waveform(string, string, ComplexWaveform< ComplexSingle >, bool, long)

Performs the enabled measurements on the I/Q complex waveform that you specify in *IQ* parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods in the method node. Use this method only if the Recommended Acquisition Type method value is either *IQ* or *IQorSpectral*. 
 When using the Analysis-Only mode in RFmxNR, the RFmx driver ignores the RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM. 
 Query the Recommended Acquisition Type method from the RFmxInstr Property Node after calling the RFmxNR Commit method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int AnalyzeIQ1Waveform(string selectorString, string resultName, ComplexWaveform< ComplexSingle > iq, bool reset, long reserved)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the result name in this parameter, either the result name specified by the resultName parameter or the default result instance is used. Example:"""""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| resultName | string | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"result::r1""r1" |
| iq | ComplexWaveform< ComplexSingle > | Specifies the data for a complex waveform including the start, delta, and actual values. |
| reset | bool | Resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| reserved | long | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-analyzenwaveformsspectrum__string-string-spectrum_float__arr1-bool.html language=enus -->
## TOPIC 00006: AnalyzeNWaveformsSpectrum(string, string, Spectrum< float >[], bool)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-analyzenwaveformsspectrum__string-string-spectrum_float__arr1-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-analyzenwaveformsspectrum__string-string-spectrum_float__arr1-bool.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the spectrum(s) that you specify in the spectrum parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods in the method node. Use this method only if the Recomm

### AnalyzeNWaveformsSpectrum(string, string, Spectrum< float >[], bool)

Performs the enabled measurements on the spectrum(s) that you specify in the *spectrum* parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods in the method node. Use this method only if the Recommended Acquisition Type property value is either *spectral* or *IQorSpectral*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int AnalyzeNWaveformsSpectrum(string selectorString, string resultName, Spectrum< float >[] spectrum, bool reset)

#### Remarks

Query the Recommended Acquisition Type property from the RFmxInstr Property Node after calling the RFmx NR Commit method.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the result name in this parameter, either the result name specified by the resultName parameter or the default result instance is used. Example:"""""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| resultName | string | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"result::r1""r1" |
| spectrum | Spectrum< float >[] | Specifies the waveform array where each element contains data for a spectrum waveform including start, delta, and actual values. |
| reset | bool | Resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-analyzespectrum1waveform__string-string-spectrum_float_-bool-long.html language=enus -->
## TOPIC 00007: AnalyzeSpectrum1Waveform(string, string, Spectrum< float >, bool, long)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-analyzespectrum1waveform__string-string-spectrum_float_-bool-long.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-analyzespectrum1waveform__string-string-spectrum_float_-bool-long.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the spectrum that you specify in the spectrum parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods in the method node. Use this method only if the Recommend

### AnalyzeSpectrum1Waveform(string, string, Spectrum< float >, bool, long)

Performs the enabled measurements on the spectrum that you specify in the *spectrum* parameter. Call this method after you configure the signal and measurement methods. You can fetch measurement results using the Fetch methods or result methods in the method node. Use this method only if the Recommended Acquisition Type method value is either *spectral* or *IQorSpectral*. 
 When using the Analysis-Only mode in RFmxNR, the RFmx driver ignores the RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM. 
 Query the Recommended Acquisition Type method from the RFmxInstr Property Node after calling the RFmxNR Commit method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int AnalyzeSpectrum1Waveform(string selectorString, string resultName, Spectrum< float > spectrum, bool reset, long reserved)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the result name in this parameter, either the result name specified by the resultName parameter or the default result instance is used. Example:"""""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| resultName | string | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"result::r1""r1" |
| spectrum | Spectrum< float > | Specifies the data for a spectrum waveform. |
| reset | bool | Resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| reserved | long | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-autolevel__string-double-out.html language=enus -->
## TOPIC 00008: AutoLevel(string, double, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-autolevel__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-autolevel__string-double-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Examines the input signal to calculate the peak power level and sets it as the value of the SetReferenceLevel(string, double) method. Use this method to calculate an approximate setting for the reference level. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int AutoLevel(string selectorString,

### AutoLevel(string, double, out double)

Examines the input signal to calculate the peak power level and sets it as the value of the [SetReferenceLevel(string, double)](nationalinstruments-rfmx-nrmx-rfmxnrmx-setreferencelevel__string-double.html) method. Use this method to calculate an approximate setting for the reference level.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int AutoLevel(string selectorString, double measurementInterval, out double referenceLevel)

#### Remarks

1. Resets the mixer level, mixer level offset, and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation, and preamplifier enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after the execution.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| measurementInterval | double | Specifies the acquisition length. This value is expressed in seconds. Use this value to compute the number of samples to acquire from the signal analyzer. Auto Level method does not use any trigger for acquisition. It ignores the user-configured trigger methods. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. |
| referenceLevel | out double | Upon return, contains the estimated peak power level of the input signal. This value is expressed in dBm. The default value of this parameter is hardware dependent. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-buildbandwidthpartstring__string-int.html language=enus -->
## TOPIC 00009: BuildBandwidthPartString(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-buildbandwidthpartstring__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-buildbandwidthpartstring__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the bandwidth part string.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic static string BuildBandwidthPartString(string selectorString, int bandwidthPartNumber)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the result name, subblock number, an

### BuildBandwidthPartString(string, int)

Creates the bandwidth part string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public static string BuildBandwidthPartString(string selectorString, int bandwidthPartNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| bandwidthPartNumber | int | Specifies the bandwidth part number for building the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-buildcarrierstring__string-int.html language=enus -->
## TOPIC 00010: BuildCarrierString(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-buildcarrierstring__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-buildcarrierstring__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the carrier string.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic static string BuildCarrierString(string selectorString, int carrierNumber)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the result name, and subblock number. If you do not spe

### BuildCarrierString(string, int)

Creates the carrier string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public static string BuildCarrierString(string selectorString, int carrierNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| carrierNumber | int | Specifies the carrier number for building the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-buildchainstring__string-int.html language=enus -->
## TOPIC 00011: BuildChainString(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-buildchainstring__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-buildchainstring__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a chain string.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic static string BuildChainString(string selectorString, int chainNumber)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the result name, subblock number, carrier number. If you do not

### BuildChainString(string, int)

Creates a chain string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public static string BuildChainString(string selectorString, int chainNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0/carrier0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| chainNumber | int | Specifies the chain number for building the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-buildcoresetclusterstring__string-int.html language=enus -->
## TOPIC 00012: BuildCoresetClusterString(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-buildcoresetclusterstring__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-buildcoresetclusterstring__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the coreset cluster string.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic static string BuildCoresetClusterString(string selectorString, int coresetClusterNumber)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the result name, subblock number,

### BuildCoresetClusterString(string, int)

Creates the coreset cluster string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public static string BuildCoresetClusterString(string selectorString, int coresetClusterNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, carrier number, bandwidth part number, and coreset number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0/bwp0/coreset0""result::r1/subblock0/carrier0/bwp0/coreset0" You can use the BuildCoresetString(string, int) method to build the selector string. |
| coresetClusterNumber | int | Specifies the CORESET cluster number for building the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-buildcoresetstring__string-int.html language=enus -->
## TOPIC 00013: BuildCoresetString(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-buildcoresetstring__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-buildcoresetstring__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the coreset string.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic static string BuildCoresetString(string selectorString, int coresetNumber)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the result name, subblock number, and bandwidth part nu

### BuildCoresetString(string, int)

Creates the coreset string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public static string BuildCoresetString(string selectorString, int coresetNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and bandwidth part number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0/bwp0""result::r1/subblock0/carrier0/bwp0" You can use the BuildBandwidthPartString(string, int) method to build the selector string. |
| coresetNumber | int | Specifies the CORESET number for building the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-buildliststepstring__string-string-int.html language=enus -->
## TOPIC 00014: BuildListStepString(string, string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-buildliststepstring__string-string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-buildliststepstring__string-string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the list step string. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic static string BuildListStepString(string selectorString, string resultName, int listStepNumber)ParametersNameTypeDescriptionselectorStringstringSpecifies the list name. This input accepts the list name with or without

### BuildListStepString(string, string, int)

Creates the list step string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

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

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-buildliststring__string-string.html language=enus -->
## TOPIC 00015: BuildListString(string, string)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-buildliststring__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-buildliststring__string-string.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the list string. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic static string BuildListString(string listName, string resultName)ParametersNameTypeDescriptionlistNamestringSpecifies the list name for building the selector string. This input accepts the list name with or without the "li

### BuildListString(string, string)

Creates the list string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public static string BuildListString(string listName, string resultName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| listName | string | Specifies the list name for building the selector string. This input accepts the list name with or without the "list::" prefix. |
| resultName | string | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example: "result::r1" "r1" |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-buildoffsetstring__string-int.html language=enus -->
## TOPIC 00016: BuildOffsetString(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-buildoffsetstring__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-buildoffsetstring__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the offset string.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic static string BuildOffsetString(string selectorString, int offsetNumber)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the result name, and subblock number. If you do not specif

### BuildOffsetString(string, int)

Creates the offset string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public static string BuildOffsetString(string selectorString, int offsetNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| offsetNumber | int | Specifies the offset number for building the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-buildpdcchstring__string-int.html language=enus -->
## TOPIC 00017: BuildPdcchString(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-buildpdcchstring__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-buildpdcchstring__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the PDCCH string.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic static string BuildPdcchString(string selectorString, int pdcchNumber)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the result name, subblock number, carrier number, bandwidth p

### BuildPdcchString(string, int)

Creates the PDCCH string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public static string BuildPdcchString(string selectorString, int pdcchNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, carrier number, bandwidth part number, and coreset number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0/bwp0/coreset0""result::r1/subblock0/carrier0/bwp0/coreset0" You can use the BuildCoresetString(string, int) method to build the selector string. |
| pdcchNumber | int | Specifies the PDCCH number for building the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-buildpdschstring__string-int.html language=enus -->
## TOPIC 00018: BuildPdschString(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-buildpdschstring__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-buildpdschstring__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the PDSCH string.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic static string BuildPdschString(string selectorString, int pdschNumber)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the result name, subblock number, bandwidth part number, and

### BuildPdschString(string, int)

Creates the PDSCH string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public static string BuildPdschString(string selectorString, int pdschNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, bandwidth part number, and user number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0/bwp0/user0""result::r1/subblock0/carrier0/bwp0/user0" You can use the BuildUserString(string, int) method to build the selector string. |
| pdschNumber | int | Specifies the PDSCH number for building the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-configureselectedportsmultiple__string-string_arr1.html language=enus -->
## TOPIC 00019: ConfigureSelectedPortsMultiple(string, string[])

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-configureselectedportsmultiple__string-string_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-configureselectedportsmultiple__string-string_arr1.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the selected ports to each chain based on the values you set in SetNumberOfReceiveChains(string, int) method. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int ConfigureSelectedPortsMultiple(string selectorString, string[] selectedPorts)ParametersNameTypeDescriptionselectorStringst

### ConfigureSelectedPortsMultiple(string, string[])

Configures the selected ports to each chain based on the values you set in [SetNumberOfReceiveChains(string, int)](nationalinstruments-rfmx-nrmx-rfmxnrmx-setnumberofreceivechains__string-int.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int ConfigureSelectedPortsMultiple(string selectorString, string[] selectedPorts)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| selectedPorts | string[] | Specifies the list of MIMO ports to be configured. Use "port::(deviceName)/(channelNumber)" as the format for the selected port. For PXIe-5830/5831/5832 devices on a MIMO session, the selected port includes the instrument port in the format "port::(deviceName)/(channelNumber)/(instrPort)". Example:port.myrfsa1/0/if1 You can use the RFmxInstr_BuildPortString attribute to build the selected port. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-getattributebool__string-int-out.html language=enus -->
## TOPIC 00020: GetAttributeBool(string, int, out bool)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-getattributebool__string-int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-getattributebool__string-int-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of a Bool attribute. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetAttributeBool(string selectorString, int attributeIdentifier, out bool value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being read. Refer to the Using

### GetAttributeBool(string, int, out bool)

Gets the value of a Bool attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetAttributeBool(string selectorString, int attributeIdentifier, out bool value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx NR Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | out bool | Upon return, contains a value of the specified attribute ID. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-getattributedouble__string-int-out.html language=enus -->
## TOPIC 00021: GetAttributeDouble(string, int, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-getattributedouble__string-int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-getattributedouble__string-int-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of a Double attribute. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetAttributeDouble(string selectorString, int attributeIdentifier, out double value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being read. Refer to the

### GetAttributeDouble(string, int, out double)

Gets the value of a Double attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetAttributeDouble(string selectorString, int attributeIdentifier, out double value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx NR Help for more information about configuring the selector string. |
| attributeIdentifier | int | Passes the ID of an attribute. |
| value | out double | Upon return, contains a value of the specified attribute ID. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-getattributeint__string-int-out.html language=enus -->
## TOPIC 00022: GetAttributeInt(string, int, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-getattributeint__string-int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-getattributeint__string-int-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of an RFmx 32-bit integer (int32) attribute. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetAttributeInt(string selectorString, int attributeIdentifier, out int value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being re

### GetAttributeInt(string, int, out int)

Gets the value of an RFmx 32-bit integer (int32) attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetAttributeInt(string selectorString, int attributeIdentifier, out int value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx NR Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | out int | Upon return, contains a value of the specified attribute ID. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-getattributesbyte__string-int-out.html language=enus -->
## TOPIC 00023: GetAttributeSbyte(string, int, out sbyte)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-getattributesbyte__string-int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-getattributesbyte__string-int-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of a Sbyte attribute. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetAttributeSbyte(string selectorString, int attributeIdentifier, out sbyte value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being read. Refer to the Us

### GetAttributeSbyte(string, int, out sbyte)

Gets the value of a Sbyte attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetAttributeSbyte(string selectorString, int attributeIdentifier, out sbyte value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the RFmx NR Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | out sbyte | Upon return, contains a value of the specified attribute ID. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-getcenterfrequency__string-out.html language=enus -->
## TOPIC 00024: GetCenterFrequency(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-getcenterfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-getcenterfrequency__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the center frequency of the acquired RF signal for a single carrier. This value is expressed in Hz. For intraband carrier aggregation, this method specifies the reference frequency of a subblock. Depending on the Subblock Frequency Definition method, the center frequency can either be absolute

### GetCenterFrequency(string, out double)

Gets the center frequency of the acquired RF signal for a single carrier. This value is expressed in Hz. For intraband carrier aggregation, this method specifies the reference frequency of a subblock. Depending on the Subblock Frequency Definition method, the center frequency can either be absolute or relative to first subblock's center frequency. All component carrier frequencies within the subblock are defined with respect to this frequency.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetCenterFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [CenterFrequency](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default of this property is hardware dependent.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the center frequency of the acquired RF signal for a single carrier. This value is expressed in Hz. For intraband carrier aggregation, this method specifies the reference frequency of a subblock. Depending on the Subblock Frequency Definition method, the center frequency can either be absolute or relative to first subblock's center frequency. All component carrier frequencies within the subblock are defined with respect to this frequency. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-getcomponentcarrierspacingtype__string-out.html language=enus -->
## TOPIC 00025: GetComponentCarrierSpacingType(string, out RFmxNRMXComponentCarrierSpacingType)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-getcomponentcarrierspacingtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-getcomponentcarrierspacingtype__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the spacing between adjacent component carriers (CCs) within a subblock. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetComponentCarrierSpacingType(string selectorString, out RFmxNRMXComponentCarrierSpacingType value)RemarksThis method gets the value of ComponentCarrierSpacingType

### GetComponentCarrierSpacingType(string, out RFmxNRMXComponentCarrierSpacingType)

Gets the spacing between adjacent component carriers (CCs) within a subblock.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetComponentCarrierSpacingType(string selectorString, out RFmxNRMXComponentCarrierSpacingType value)

#### Remarks

This method gets the value of [ComponentCarrierSpacingType](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Nominal](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrierspacingtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(string, int) method to build the selector string. |
| value | out RFmxNRMXComponentCarrierSpacingType | Upon return, contains the spacing between adjacent component carriers (CCs) within a subblock. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-getdownlinkchannelconfigurationmode__string-out.html language=enus -->
## TOPIC 00026: GetDownlinkChannelConfigurationMode(string, out RFmxNRMXDownlinkChannelConfigurationMode)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-getdownlinkchannelconfigurationmode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-getdownlinkchannelconfigurationmode__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the downlink channel configuration mode. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetDownlinkChannelConfigurationMode(string selectorString, out RFmxNRMXDownlinkChannelConfigurationMode value)RemarksThis method gets the value of DownlinkChannelConfigurationMode attribute.The def

### GetDownlinkChannelConfigurationMode(string, out RFmxNRMXDownlinkChannelConfigurationMode)

Gets the downlink channel configuration mode.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetDownlinkChannelConfigurationMode(string selectorString, out RFmxNRMXDownlinkChannelConfigurationMode value)

#### Remarks

This method gets the value of [DownlinkChannelConfigurationMode](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [TestModel](nationalinstruments-rfmx-nrmx-rfmxnrmxdownlinkchannelconfigurationmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxNRMXDownlinkChannelConfigurationMode | Upon return, contains the downlink channel configuration mode. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-geterror__out-out.html language=enus -->
## TOPIC 00027: GetError(out int, out string)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-geterror__out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-geterror__out-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the latest error code and description. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetError(out int errorCode, out string errorDescription)ParametersNameTypeDescriptionerrorCodeout intUpon return, contains the latest error code.errorDescriptionout stringUpon return, contains the la

### GetError(out int, out string)

Gets the latest error code and description.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetError(out int errorCode, out string errorDescription)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| errorCode | out int | Upon return, contains the latest error code. |
| errorDescription | out string | Upon return, contains the latest error description. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-geterrorstring__int-out.html language=enus -->
## TOPIC 00028: GetErrorString(int, out string)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-geterrorstring__int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-geterrorstring__int-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the status code returned by an RFmxNR function into a string. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetErrorString(int errorCode, out string errorDescription)ParametersNameTypeDescriptionerrorCodeintSpecifies an error or warning code.errorDescriptionout stringUpon return,

### GetErrorString(int, out string)

Converts the status code returned by an RFmxNR function into a string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetErrorString(int errorCode, out string errorDescription)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| errorCode | int | Specifies an error or warning code. |
| errorDescription | out string | Upon return, contains the error description. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-getexternalattenuation__string-out.html language=enus -->
## TOPIC 00029: GetExternalAttenuation(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-getexternalattenuation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-getexternalattenuation__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. On a MIMO session, u

### GetExternalAttenuation(string, out double)

Gets the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the *NI RF Vector Signal Analyzers Help*. On a MIMO session, use port::(deviceName)/(channelNumber) as a selector string to configure or read this property per port. If you do not specify port string, this method is configured for all ports. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetExternalAttenuation(string selectorString, out double value)

#### Remarks

This method gets the value of [ExternalAttenuation](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the instrport number. Example: "instrport0". You can use the NationalInstruments.RFmx.InstrMX.RFmxInstrMX.BuildPortString(string,string) method to build the selector string. |
| value | out double | Upon return, contains the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-getgnodebcategory__string-out.html language=enus -->
## TOPIC 00030: GetgNodeBCategory(string, out RFmxNRMXgNodeBCategory)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-getgnodebcategory__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-getgnodebcategory__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the downlink gNodeB (base station) category. Refer to the 3GPP 38.104 specification for more information about gNodeB category. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetgNodeBCategory(string selectorString, out RFmxNRMXgNodeBCategory value)RemarksThis method gets the value of

### GetgNodeBCategory(string, out RFmxNRMXgNodeBCategory)

Gets the downlink gNodeB (base station) category. Refer to the *3GPP 38.104* specification for more information about gNodeB category.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetgNodeBCategory(string selectorString, out RFmxNRMXgNodeBCategory value)

#### Remarks

This method gets the value of [gNodeBCategory](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is Wide Area Base Station - Category A.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxNRMXgNodeBCategory | Upon return, contains the downlink gNodeB (base station) category. Refer to the 3GPP 38.104 specification for more information about gNodeB category. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-getgridsizemode__string-out.html language=enus -->
## TOPIC 00031: GetGridSizeMode(string, out RFmxNRMXGridSizeMode)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-getgridsizemode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-getgridsizemode__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to set the grid size of all BWPs and SSB in a component carrier automatically or manually. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetGridSizeMode(string selectorString, out RFmxNRMXGridSizeMode value)RemarksThis method gets the value of GridSizeMode attribute.The defau

### GetGridSizeMode(string, out RFmxNRMXGridSizeMode)

Gets whether to set the grid size of all BWPs and SSB in a component carrier automatically or manually.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetGridSizeMode(string selectorString, out RFmxNRMXGridSizeMode value)

#### Remarks

This method gets the value of [GridSizeMode](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Auto](nationalinstruments-rfmx-nrmx-rfmxnrmxgridsizemode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxNRMXGridSizeMode | Upon return, contains whether to set the grid size of all BWPs and SSB in a component carrier automatically or manually. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-getiqpoweredgetriggerleveltype__string-out.html language=enus -->
## TOPIC 00032: GetIQPowerEdgeTriggerLevelType(string, out RFmxNRMXIQPowerEdgeTriggerLevelType)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-getiqpoweredgetriggerleveltype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-getiqpoweredgetriggerleveltype__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(string, RFmxNRMXTriggerType) method to IQPowerEdge. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetIQPowerEdgeTriggerLevelType(s

### GetIQPowerEdgeTriggerLevelType(string, out RFmxNRMXIQPowerEdgeTriggerLevelType)

Gets the reference for the [SetIQPowerEdgeTriggerLevel(string, double)](nationalinstruments-rfmx-nrmx-rfmxnrmx-setiqpoweredgetriggerlevel__string-double.html) method. The IQ Power Edge Level Type method is used only when you set the [SetTriggerType(string, RFmxNRMXTriggerType)](nationalinstruments-rfmx-nrmx-rfmxnrmx-settriggertype__string-rfmxnrmxtriggertype.html) method to [IQPowerEdge](nationalinstruments-rfmx-nrmx-rfmxnrmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetIQPowerEdgeTriggerLevelType(string selectorString, out RFmxNRMXIQPowerEdgeTriggerLevelType value)

#### Remarks

This method gets the value of [IQPowerEdgeTriggerLevelType](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Relative](nationalinstruments-rfmx-nrmx-rfmxnrmxiqpoweredgetriggerleveltype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxNRMXIQPowerEdgeTriggerLevelType | Upon return, contains the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(string, RFmxNRMXTriggerType) method to IQPowerEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-getiqpoweredgetriggersource__string-out.html language=enus -->
## TOPIC 00033: GetIQPowerEdgeTriggerSource(string, out string)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-getiqpoweredgetriggersource__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-getiqpoweredgetriggersource__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the channel from which the device monitors the trigger. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetIQPowerEdgeTriggerSource(string selectorString, out string value)RemarksThis method gets the value of IQPowerEdgeTriggerSource attribute.The default value of this property is hard

### GetIQPowerEdgeTriggerSource(string, out string)

Gets the channel from which the device monitors the trigger.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetIQPowerEdgeTriggerSource(string selectorString, out string value)

#### Remarks

This method gets the value of [IQPowerEdgeTriggerSource](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value of this property is hardware dependent.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out string | Upon return, contains the channel from which the device monitors the trigger. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-getlimitedconfigurationchange__string-out.html language=enus -->
## TOPIC 00034: GetLimitedConfigurationChange(string, out RFmxNRMXLimitedConfigurationChange)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-getlimitedconfigurationchange__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-getlimitedconfigurationchange__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the set of properties that are considered by RFmx in the locked signal configuration state. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetLimitedConfigurationChange(string selectorString, out RFmxNRMXLimitedConfigurationChange value)RemarksThis method gets the value of LimitedConf

### GetLimitedConfigurationChange(string, out RFmxNRMXLimitedConfigurationChange)

Gets the set of properties that are considered by RFmx in the locked signal configuration state.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetLimitedConfigurationChange(string selectorString, out RFmxNRMXLimitedConfigurationChange value)

#### Remarks

This method gets the value of [LimitedConfigurationChange](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Disabled](nationalinstruments-rfmx-nrmx-rfmxnrmxlimitedconfigurationchange.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxNRMXLimitedConfigurationChange | Upon return, contains the set of properties that are considered by RFmx in the locked signal configuration state. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-getlinkdirection__string-out.html language=enus -->
## TOPIC 00035: GetLinkDirection(string, out RFmxNRMXLinkDirection)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-getlinkdirection__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-getlinkdirection__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the link direction of the received signal. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetLinkDirection(string selectorString, out RFmxNRMXLinkDirection value)RemarksThis method gets the value of LinkDirection attribute.The default value is Uplink.ParametersNameTypeDescriptionselec

### GetLinkDirection(string, out RFmxNRMXLinkDirection)

Gets the link direction of the received signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetLinkDirection(string selectorString, out RFmxNRMXLinkDirection value)

#### Remarks

This method gets the value of [LinkDirection](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Uplink](nationalinstruments-rfmx-nrmx-rfmxnrmxlinkdirection.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxNRMXLinkDirection | Upon return, contains the link direction of the received signal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-getliststeptimerduration__string-out.html language=enus -->
## TOPIC 00036: GetListStepTimerDuration(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-getliststeptimerduration__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-getliststeptimerduration__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the duration of a given list step in units specified by SetListStepTimerUnit(string, RFmxNRMXListStepTimerUnit). SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetListStepTimerDuration(string selectorString, out double value)RemarksThis method gets the value of ListStepTimerDuration a

### GetListStepTimerDuration(string, out double)

Gets the duration of a given list step in units specified by [SetListStepTimerUnit(string, RFmxNRMXListStepTimerUnit)](nationalinstruments-rfmx-nrmx-rfmxnrmx-setliststeptimerunit__string-rfmxnrmxliststeptimerunit.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetListStepTimerDuration(string selectorString, out double value)

#### Remarks

This method gets the value of [ListStepTimerDuration](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the duration of a given list step in units specified by SetListStepTimerUnit(string, RFmxNRMXListStepTimerUnit). |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-getliststeptimeroffset__string-out.html language=enus -->
## TOPIC 00037: GetListStepTimerOffset(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-getliststeptimeroffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-getliststeptimeroffset__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the offset from the start of the step for which the measurements are computed. The unit for this method is specified by SetListStepTimerUnit(string, RFmxNRMXListStepTimerUnit). This method is valid only when you set the SetDigitalEdgeTriggerSource(string, string) method to TimerEventSyntaxNames

### GetListStepTimerOffset(string, out double)

Gets the offset from the start of the step for which the measurements are computed. The unit for this method is specified by [SetListStepTimerUnit(string, RFmxNRMXListStepTimerUnit)](nationalinstruments-rfmx-nrmx-rfmxnrmx-setliststeptimerunit__string-rfmxnrmxliststeptimerunit.html). This method is valid only when you set the [SetDigitalEdgeTriggerSource(string, string)](nationalinstruments-rfmx-nrmx-rfmxnrmx-setdigitaledgetriggersource__string-string.html) method to [TimerEvent](nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-timerevent.html)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetListStepTimerOffset(string selectorString, out double value)

#### Remarks

This method gets the value of [ListStepTimerOffset](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the offset from the start of the step for which the measurements are computed. The unit for this method is specified by SetListStepTimerUnit(string, RFmxNRMXListStepTimerUnit). This method is valid only when you set the SetDigitalEdgeTriggerSource(string, string) method to TimerEvent |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-getliststeptimerunit__string-out.html language=enus -->
## TOPIC 00038: GetListStepTimerUnit(string, out RFmxNRMXListStepTimerUnit)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-getliststeptimerunit__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-getliststeptimerunit__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the units in which SetListStepTimerDuration(string, double) and SetListStepTimerOffset(string, double) are specified. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetListStepTimerUnit(string selectorString, out RFmxNRMXListStepTimerUnit value)RemarksThis method gets the value of Lis

### GetListStepTimerUnit(string, out RFmxNRMXListStepTimerUnit)

Gets the units in which [SetListStepTimerDuration(string, double)](nationalinstruments-rfmx-nrmx-rfmxnrmx-setliststeptimerduration__string-double.html) and [SetListStepTimerOffset(string, double)](nationalinstruments-rfmx-nrmx-rfmxnrmx-setliststeptimeroffset__string-double.html) are specified.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetListStepTimerUnit(string selectorString, out RFmxNRMXListStepTimerUnit value)

#### Remarks

This method gets the value of [ListStepTimerUnit](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Slot](nationalinstruments-rfmx-nrmx-rfmxnrmxliststeptimerunit.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxNRMXListStepTimerUnit | Upon return, contains the units in which SetListStepTimerDuration(string, double) and SetListStepTimerOffset(string, double) are specified. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-getnumberofreceivechains__string-out.html language=enus -->
## TOPIC 00039: GetNumberOfReceiveChains(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-getnumberofreceivechains__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-getnumberofreceivechains__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetNumberOfReceiveChains(string selectorString, out int value)

### GetNumberOfReceiveChains(string, out int)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetNumberOfReceiveChains(string selectorString, out int value)

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-getnumberofsubblocks__string-out.html language=enus -->
## TOPIC 00040: GetNumberOfSubblocks(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-getnumberofsubblocks__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-getnumberofsubblocks__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of subblocks configured in intraband non-contiguous carrier aggregation scenarios. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetNumberOfSubblocks(string selectorString, out int value)RemarksThis method gets the value of NumberOfSubblocks attribute.The default value is

### GetNumberOfSubblocks(string, out int)

Gets the number of subblocks configured in intraband non-contiguous carrier aggregation scenarios.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetNumberOfSubblocks(string selectorString, out int value)

#### Remarks

This method gets the value of [NumberOfSubblocks](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 1. Set this property to 1 for single carrier and intra-band contiguous carrier aggregation.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of subblocks configured in intraband non-contiguous carrier aggregation scenarios. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-getphasecompensation__string-out.html language=enus -->
## TOPIC 00041: GetPhaseCompensation(string, out RFmxNRMXPhaseCompensation)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-getphasecompensation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-getphasecompensation__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether phase compensation is disabled, auto-set by the measurement or set by the you. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPhaseCompensation(string selectorString, out RFmxNRMXPhaseCompensation value)RemarksThis method gets the value of PhaseCompensation attribute.The de

### GetPhaseCompensation(string, out RFmxNRMXPhaseCompensation)

Gets whether phase compensation is disabled, auto-set by the measurement or set by the you.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPhaseCompensation(string selectorString, out RFmxNRMXPhaseCompensation value)

#### Remarks

This method gets the value of [PhaseCompensation](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Disabled](nationalinstruments-rfmx-nrmx-rfmxnrmxphasecompensation.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxNRMXPhaseCompensation | Upon return, contains whether phase compensation is disabled, auto-set by the measurement or set by the you. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-getphasecompensationfrequency__string-out.html language=enus -->
## TOPIC 00042: GetPhaseCompensationFrequency(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-getphasecompensationfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-getphasecompensationfrequency__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency used for phase compensation of the signal when you set the SetPhaseCompensation(string, RFmxNRMXPhaseCompensation) method to UserDefined. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPhaseCompensationFrequency(string selectorString, ou

### GetPhaseCompensationFrequency(string, out double)

Gets the frequency used for phase compensation of the signal when you set the [SetPhaseCompensation(string, RFmxNRMXPhaseCompensation)](nationalinstruments-rfmx-nrmx-rfmxnrmx-setphasecompensation__string-rfmxnrmxphasecompensation.html) method to [UserDefined](nationalinstruments-rfmx-nrmx-rfmxnrmxphasecompensation.html). This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPhaseCompensationFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [PhaseCompensationFrequency](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the frequency used for phase compensation of the signal when you set the SetPhaseCompensation(string, RFmxNRMXPhaseCompensation) method to UserDefined. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-getpiby2bpskpowerboostenabled__string-out.html language=enus -->
## TOPIC 00043: GetPiBy2BpskPowerBoostEnabled(string, out RFmxNRMXPiBy2BpskPowerBoostEnabled)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-getpiby2bpskpowerboostenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-getpiby2bpskpowerboostenabled__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power boost for PI/2 BPSK signal when you set the SetFrequencyRange(string, RFmxNRMXFrequencyRange) method to Range1. This method is valid only for uplink direction. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPiBy2BpskPowerBoostEnabled(string selectorString, out RFmxNRMXPiB

### GetPiBy2BpskPowerBoostEnabled(string, out RFmxNRMXPiBy2BpskPowerBoostEnabled)

Gets the power boost for PI/2 BPSK signal when you set the [SetFrequencyRange(string, RFmxNRMXFrequencyRange)](nationalinstruments-rfmx-nrmx-rfmxnrmx-setfrequencyrange__string-rfmxnrmxfrequencyrange.html) method to [Range1](nationalinstruments-rfmx-nrmx-rfmxnrmxfrequencyrange.html). This method is valid only for uplink direction.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPiBy2BpskPowerBoostEnabled(string selectorString, out RFmxNRMXPiBy2BpskPowerBoostEnabled value)

#### Remarks

This method gets the value of [PiBy2BpskPowerBoostEnabled](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-nrmx-rfmxnrmxpiby2bpskpowerboostenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxNRMXPiBy2BpskPowerBoostEnabled | Upon return, contains the power boost for PI/2 BPSK signal when you set the SetFrequencyRange(string, RFmxNRMXFrequencyRange) method to Range1. This method is valid only for uplink direction. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-getreferencegridalignmentmode__string-out.html language=enus -->
## TOPIC 00044: GetReferenceGridAlignmentMode(string, out RFmxNRMXReferenceGridAlignmentMode)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-getreferencegridalignmentmode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-getreferencegridalignmentmode__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to align the bandwidthparts and the SSB in a component carrier to a reference resource grid automatically or manually. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetReferenceGridAlignmentMode(string selectorString, out RFmxNRMXReferenceGridAlignmentMode value)RemarksThis m

### GetReferenceGridAlignmentMode(string, out RFmxNRMXReferenceGridAlignmentMode)

Gets whether to align the bandwidthparts and the SSB in a component carrier to a reference resource grid automatically or manually.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetReferenceGridAlignmentMode(string selectorString, out RFmxNRMXReferenceGridAlignmentMode value)

#### Remarks

This method gets the value of [ReferenceGridAlignmentMode](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Auto](nationalinstruments-rfmx-nrmx-rfmxnrmxreferencegridalignmentmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxNRMXReferenceGridAlignmentMode | Upon return, contains whether to align the bandwidthparts and the SSB in a component carrier to a reference resource grid automatically or manually. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-getreferencelevel__string-out.html language=enus -->
## TOPIC 00045: GetReferenceLevel(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-getreferencelevel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-getreferencelevel__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetReferenceLevel(string selectorString, out double value)RemarksThis m

### GetReferenceLevel(string, out double)

Gets the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetReferenceLevel(string selectorString, out double value)

#### Remarks

This method gets the value of [ReferenceLevel](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default of this property is hardware dependent.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the instrport number. Example: "instrport0". You can use the NationalInstruments.RFmx.InstrMX.RFmxInstrMX.BuildPortString(string,string) method to build the selector string. |
| value | out double | Upon return, contains the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-getreferencelevelheadroom__string-out.html language=enus -->
## TOPIC 00046: GetReferenceLevelHeadroom(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-getreferencelevelheadroom__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-getreferencelevelheadroom__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the margin RFmx adds to the SetReferenceLevel(string, double) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. Default values PXIe-5668: 6 dB PXIe-5830/5831/5832/5841/5842/5860: 1 dB PXIe-5840: 0 dB Supported devices: PXIe-5668

### GetReferenceLevelHeadroom(string, out double)

Gets the margin RFmx adds to the [SetReferenceLevel(string, double)](nationalinstruments-rfmx-nrmx-rfmxnrmx-setreferencelevel__string-double.html) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. **Default values** 
 PXIe-5668: 6 dB 
 PXIe-5830/5831/5832/5841/5842/5860: 1 dB 
 PXIe-5840: 0 dB **Supported devices:**PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842/5860.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetReferenceLevelHeadroom(string selectorString, out double value)

#### Remarks

This method gets the value of [ReferenceLevelHeadroom](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the margin RFmx adds to the SetReferenceLevel(string, double) method. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-getresultfetchtimeout__string-out.html language=enus -->
## TOPIC 00047: GetResultFetchTimeout(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-getresultfetchtimeout__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-getresultfetchtimeout__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the time to wait before results are available in the RFmxNR Property Node. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetResultFetchTimeout(string selectorString, out double value)RemarksThis method gets the value of ResultFetchTimeout attribute

### GetResultFetchTimeout(string, out double)

Gets the time to wait before results are available in the RFmxNR Property Node. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetResultFetchTimeout(string selectorString, out double value)

#### Remarks

This method gets the value of [ResultFetchTimeout](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the time to wait before results are available in the RFmxNR Property Node. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-setattributebool__string-int-bool.html language=enus -->
## TOPIC 00048: SetAttributeBool(string, int, bool)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-setattributebool__string-int-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-setattributebool__string-int-bool.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a Bool attribute. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetAttributeBool(string selectorString, int attributeIdentifier, bool value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being set. Refer to the Using a Se

### SetAttributeBool(string, int, bool)

Sets the value of a Bool attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetAttributeBool(string selectorString, int attributeIdentifier, bool value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx NR Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | bool | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-setautocelliddetectionenabled__string-rfmxnrmxautocelliddetectionenabled.html language=enus -->
## TOPIC 00049: SetAutoCellIDDetectionEnabled(string, RFmxNRMXAutoCellIDDetectionEnabled)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-setautocelliddetectionenabled__string-rfmxnrmxautocelliddetectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-setautocelliddetectionenabled__string-rfmxnrmxautocelliddetectionenabled.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the autodetection of the cell ID. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetAutoCellIDDetectionEnabled(string selectorString, RFmxNRMXAutoCellIDDetectionEnabled value)RemarksThis method sets the value of AutoCellIDDetectionEnabled attribute.The default value

### SetAutoCellIDDetectionEnabled(string, RFmxNRMXAutoCellIDDetectionEnabled)

Sets whether to enable the autodetection of the cell ID.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetAutoCellIDDetectionEnabled(string selectorString, RFmxNRMXAutoCellIDDetectionEnabled value)

#### Remarks

This method sets the value of [AutoCellIDDetectionEnabled](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-nrmx-rfmxnrmxautocelliddetectionenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXAutoCellIDDetectionEnabled | Specifies whether to enable the autodetection of the cell ID. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-setautoresourceblockdetectionenabled__string-rfmxnrmxautoresourceblockdetectionenabled.html language=enus -->
## TOPIC 00050: SetAutoResourceBlockDetectionEnabled(string, RFmxNRMXAutoResourceBlockDetectionEnabled)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-setautoresourceblockdetectionenabled__string-rfmxnrmxautoresourceblockdetectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-setautoresourceblockdetectionenabled__string-rfmxnrmxautoresourceblockdetectionenabled.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the values of modulation type, number of resource block clusters, resource block offsets, and number of resource blocks are auto-detected by the measurement or configured by you. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetAutoResourceBlockDetectionEnabled(string selecto

### SetAutoResourceBlockDetectionEnabled(string, RFmxNRMXAutoResourceBlockDetectionEnabled)

Sets whether the values of modulation type, number of resource block clusters, resource block offsets, and number of resource blocks are auto-detected by the measurement or configured by you.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetAutoResourceBlockDetectionEnabled(string selectorString, RFmxNRMXAutoResourceBlockDetectionEnabled value)

#### Remarks

This method sets the value of [AutoResourceBlockDetectionEnabled](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-nrmx-rfmxnrmxautoresourceblockdetectionenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXAutoResourceBlockDetectionEnabled | Specifies whether the values of modulation type, number of resource block clusters, resource block offsets, and number of resource blocks are auto-detected by the measurement or configured by you. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-setband__string-int.html language=enus -->
## TOPIC 00051: SetBand(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-setband__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-setband__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the evolved universal terrestrial radio access (E-UTRA) or NR operating frequency band of a subblock as specified in section 5.2 of the 3GPP 38.101-1/2/3 specification. Band determines the spectral flatness mask and spectral emission mask. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic in

### SetBand(string, int)

Sets the evolved universal terrestrial radio access (E-UTRA) or NR operating frequency band of a subblock as specified in section 5.2 of the *3GPP 38.101-1/2/3* specification. Band determines the spectral flatness mask and spectral emission mask.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetBand(string selectorString, int value)

#### Remarks

This method sets the value of [Band](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 78. Valid values for frequency range 1 are 1, 2, 3, 5, 7, 8, 12, 13, 14, 18, 20, 24, 25, 26, 28, 29, 30, 31, 34, 38, 39, 40, 41, 46, 47, 48, 50, 51, 53, 54, 65, 66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 104, 105, 106, 109, 110, 252, 254, 255 and 256. Valid values for frequency range 2-1 are 257, 258, 259, 260, 261, and 262. Valid values for frequency range 2-2 are 263.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(string, int) method to build the selector string. |
| value | int | Specifies the evolved universal terrestrial radio access (E-UTRA) or NR operating frequency band of a subblock as specified in section 5.2 of the 3GPP 38.101-1/2/3 specification. Band determines the spectral flatness mask and spectral emission mask. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-setcenterfrequency__string-double.html language=enus -->
## TOPIC 00052: SetCenterFrequency(string, double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-setcenterfrequency__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-setcenterfrequency__string-double.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the center frequency of the acquired RF signal for a single carrier. This value is expressed in Hz. For intraband carrier aggregation, this method specifies the reference frequency of a subblock. Depending on the Subblock Frequency Definition method, the center frequency can either be absolute

### SetCenterFrequency(string, double)

Sets the center frequency of the acquired RF signal for a single carrier. This value is expressed in Hz. For intraband carrier aggregation, this method specifies the reference frequency of a subblock. Depending on the Subblock Frequency Definition method, the center frequency can either be absolute or relative to first subblock's center frequency. All component carrier frequencies within the subblock are defined with respect to this frequency.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetCenterFrequency(string selectorString, double value)

#### Remarks

This method sets the value of [CenterFrequency](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default of this property is hardware dependent.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(string, int) method to build the selector string. |
| value | double | Specifies the center frequency of the acquired RF signal for a single carrier. This value is expressed in Hz. For intraband carrier aggregation, this method specifies the reference frequency of a subblock. Depending on the Subblock Frequency Definition method, the center frequency can either be absolute or relative to first subblock's center frequency. All component carrier frequencies within the subblock are defined with respect to this frequency. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-setchannelraster__string-double.html language=enus -->
## TOPIC 00053: SetChannelRaster(string, double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-setchannelraster__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-setchannelraster__string-double.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the subblock channel raster which is used for computing nominal spacing between aggregated carriers as specified in section 5.4A.1 of 3GPP 38.101-1/2 specification and section 5.4.1.2 of 3GPP TS 38.104 specification. The value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.NRMXpu

### SetChannelRaster(string, double)

Sets the subblock channel raster which is used for computing nominal spacing between aggregated carriers as specified in section 5.4A.1 of *3GPP 38.101-1/2* specification and section 5.4.1.2 of *3GPP TS 38.104* specification. The value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetChannelRaster(string selectorString, double value)

#### Remarks

This method sets the value of [ChannelRaster](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 15 kHz.Valid values for frequency range 1 are 15 kHz and 100kHz.Valid values for frequency range 2 is 60 kHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(string, int) method to build the selector string. |
| value | double | Specifies the subblock channel raster which is used for computing nominal spacing between aggregated carriers as specified in section 5.4A.1 of 3GPP 38.101-1/2 specification and section 5.4.1.2 of 3GPP TS 38.104 specification. The value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-setexternalattenuation__string-double.html language=enus -->
## TOPIC 00054: SetExternalAttenuation(string, double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-setexternalattenuation__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-setexternalattenuation__string-double.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. On a MIMO session, u

### SetExternalAttenuation(string, double)

Sets the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the *NI RF Vector Signal Analyzers Help*. On a MIMO session, use port::(deviceName)/(channelNumber) as a selector string to configure or read this property per port. If you do not specify port string, this method is configured for all ports. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetExternalAttenuation(string selectorString, double value)

#### Remarks

This method sets the value of [ExternalAttenuation](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the instrport number. Example: "instrport0". You can use the NationalInstruments.RFmx.InstrMX.RFmxInstrMX.BuildPortString(string,string) method to build the selector string. |
| value | double | Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-setfrequencyrange__string-rfmxnrmxfrequencyrange.html language=enus -->
## TOPIC 00055: SetFrequencyRange(string, RFmxNRMXFrequencyRange)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-setfrequencyrange__string-rfmxnrmxfrequencyrange.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-setfrequencyrange__string-rfmxnrmxfrequencyrange.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to use channel bandwidth and subcarrier spacing configuration supported in the frequency range 1 (sub 6 GHz) or the frequency range 2 (above 24 GHz). SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetFrequencyRange(string selectorString, RFmxNRMXFrequencyRange value)RemarksThi

### SetFrequencyRange(string, RFmxNRMXFrequencyRange)

Sets whether to use channel bandwidth and subcarrier spacing configuration supported in the frequency range 1 (sub 6 GHz) or the frequency range 2 (above 24 GHz).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetFrequencyRange(string selectorString, RFmxNRMXFrequencyRange value)

#### Remarks

This method sets the value of [FrequencyRange](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Range1](nationalinstruments-rfmx-nrmx-rfmxnrmxfrequencyrange.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(string, int) method to build the selector string. |
| value | RFmxNRMXFrequencyRange | Specifies whether to use channel bandwidth and subcarrier spacing configuration supported in the frequency range 1 (sub 6 GHz) or the frequency range 2 (above 24 GHz). |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-setgnodebcategory__string-rfmxnrmxgnodebcategory.html language=enus -->
## TOPIC 00056: SetgNodeBCategory(string, RFmxNRMXgNodeBCategory)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-setgnodebcategory__string-rfmxnrmxgnodebcategory.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-setgnodebcategory__string-rfmxnrmxgnodebcategory.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the downlink gNodeB (base station) category. Refer to the 3GPP 38.104 specification for more information about gNodeB category. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetgNodeBCategory(string selectorString, RFmxNRMXgNodeBCategory value)RemarksThis method sets the value of gNo

### SetgNodeBCategory(string, RFmxNRMXgNodeBCategory)

Sets the downlink gNodeB (base station) category. Refer to the *3GPP 38.104* specification for more information about gNodeB category.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetgNodeBCategory(string selectorString, RFmxNRMXgNodeBCategory value)

#### Remarks

This method sets the value of [gNodeBCategory](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is Wide Area Base Station - Category A.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXgNodeBCategory | Specifies the downlink gNodeB (base station) category. Refer to the 3GPP 38.104 specification for more information about gNodeB category. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-setgnodebtype__string-rfmxnrmxgnodebtype.html language=enus -->
## TOPIC 00057: SetgNodeBType(string, RFmxNRMXgNodeBType)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-setgnodebtype__string-rfmxnrmxgnodebtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-setgnodebtype__string-rfmxnrmxgnodebtype.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the downlink gNodeB (Base Station) type. Refer to the 3GPP 38.104 specification for more information about gNodeB Type. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetgNodeBType(string selectorString, RFmxNRMXgNodeBType value)RemarksThis method sets the value of gNodeBType attribut

### SetgNodeBType(string, RFmxNRMXgNodeBType)

Sets the downlink gNodeB (Base Station) type. Refer to the *3GPP 38.104* specification for more information about gNodeB Type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetgNodeBType(string selectorString, RFmxNRMXgNodeBType value)

#### Remarks

This method sets the value of [gNodeBType](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is Type 1-C.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXgNodeBType | Specifies the downlink gNodeB (Base Station) type. Refer to the 3GPP 38.104 specification for more information about gNodeB Type. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-setgridsizemode__string-rfmxnrmxgridsizemode.html language=enus -->
## TOPIC 00058: SetGridSizeMode(string, RFmxNRMXGridSizeMode)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-setgridsizemode__string-rfmxnrmxgridsizemode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-setgridsizemode__string-rfmxnrmxgridsizemode.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to set the grid size of all BWPs and SSB in a component carrier automatically or manually. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetGridSizeMode(string selectorString, RFmxNRMXGridSizeMode value)RemarksThis method sets the value of GridSizeMode attribute.The default v

### SetGridSizeMode(string, RFmxNRMXGridSizeMode)

Sets whether to set the grid size of all BWPs and SSB in a component carrier automatically or manually.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetGridSizeMode(string selectorString, RFmxNRMXGridSizeMode value)

#### Remarks

This method sets the value of [GridSizeMode](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Auto](nationalinstruments-rfmx-nrmx-rfmxnrmxgridsizemode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXGridSizeMode | Specifies whether to set the grid size of all BWPs and SSB in a component carrier automatically or manually. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-setiqpoweredgetriggerleveltype__string-rfmxnrmxiqpoweredgetriggerleveltype.html language=enus -->
## TOPIC 00059: SetIQPowerEdgeTriggerLevelType(string, RFmxNRMXIQPowerEdgeTriggerLevelType)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-setiqpoweredgetriggerleveltype__string-rfmxnrmxiqpoweredgetriggerleveltype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-setiqpoweredgetriggerleveltype__string-rfmxnrmxiqpoweredgetriggerleveltype.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(string, RFmxNRMXTriggerType) method to IQPowerEdge. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetIQPowerEdgeTriggerLevelType(s

### SetIQPowerEdgeTriggerLevelType(string, RFmxNRMXIQPowerEdgeTriggerLevelType)

Sets the reference for the [SetIQPowerEdgeTriggerLevel(string, double)](nationalinstruments-rfmx-nrmx-rfmxnrmx-setiqpoweredgetriggerlevel__string-double.html) method. The IQ Power Edge Level Type method is used only when you set the [SetTriggerType(string, RFmxNRMXTriggerType)](nationalinstruments-rfmx-nrmx-rfmxnrmx-settriggertype__string-rfmxnrmxtriggertype.html) method to [IQPowerEdge](nationalinstruments-rfmx-nrmx-rfmxnrmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetIQPowerEdgeTriggerLevelType(string selectorString, RFmxNRMXIQPowerEdgeTriggerLevelType value)

#### Remarks

This method sets the value of [IQPowerEdgeTriggerLevelType](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Relative](nationalinstruments-rfmx-nrmx-rfmxnrmxiqpoweredgetriggerleveltype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXIQPowerEdgeTriggerLevelType | Specifies the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(string, RFmxNRMXTriggerType) method to IQPowerEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-setiqpoweredgetriggerslope__string-rfmxnrmxiqpoweredgetriggerslope.html language=enus -->
## TOPIC 00060: SetIQPowerEdgeTriggerSlope(string, RFmxNRMXIQPowerEdgeTriggerSlope)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-setiqpoweredgetriggerslope__string-rfmxnrmxiqpoweredgetriggerslope.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-setiqpoweredgetriggerslope__string-rfmxnrmxiqpoweredgetriggerslope.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetIQPowerEdgeTriggerSlope(string s

### SetIQPowerEdgeTriggerSlope(string, RFmxNRMXIQPowerEdgeTriggerSlope)

Sets whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetIQPowerEdgeTriggerSlope(string selectorString, RFmxNRMXIQPowerEdgeTriggerSlope value)

#### Remarks

This method sets the value of [IQPowerEdgeTriggerSlope](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Rising](nationalinstruments-rfmx-nrmx-rfmxnrmxiqpoweredgetriggerslope.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXIQPowerEdgeTriggerSlope | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-setnumberofreceivechains__string-int.html language=enus -->
## TOPIC 00061: SetNumberOfReceiveChains(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-setnumberofreceivechains__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-setnumberofreceivechains__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetNumberOfReceiveChains(string selectorString, int value)

### SetNumberOfReceiveChains(string, int)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetNumberOfReceiveChains(string selectorString, int value)

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmx-signalconfigurationtype.html language=enus -->
## TOPIC 00062: SignalConfigurationType

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmx-signalconfigurationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmx-signalconfigurationtype.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Type object for RFmxNRMX. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic Type SignalConfigurationType { get; }RemarksReturns the type of signal configuration object.

### SignalConfigurationType

Gets the Type object for RFmxNRMX.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public Type SignalConfigurationType { get; }

#### Remarks

Returns the type of signal configuration object.

Parent topic:

RFmxNRMX Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpamplitudecorrectiontype.html language=enus -->
## TOPIC 00063: RFmxNRMXAcpAmplitudeCorrectionType Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpamplitudecorrectiontype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpamplitudecorrectiontype.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. SyntaxNamespace: Nat

### RFmxNRMXAcpAmplitudeCorrectionType Enumeration

Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXAcpAmplitudeCorrectionType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| RFCenterFrequency | 0 | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| SpectrumFrequencyBin | 1 | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpcomponentcarrierresults-fetchmeasurementarray__string-double-ref-ref.html language=enus -->
## TOPIC 00064: FetchMeasurementArray(string, double, ref double[], ref double[])

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpcomponentcarrierresults-fetchmeasurementarray__string-double-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpcomponentcarrierresults-fetchmeasurementarray__string-double-ref-ref.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of the absolute and relative powers measured in the component carriers. Use "subblock(n)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int FetchMeasurementArray(string selectorString, double timeout, ref double[] absolu

### FetchMeasurementArray(string, double, ref double[], ref double[])

Returns an array of the absolute and relative powers measured in the component carriers. 
 Use "subblock(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int FetchMeasurementArray(string selectorString, double timeout, ref double[] absolutePower, ref double[] relativePower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| absolutePower | ref double[] | Upon return, contains an array of the power measured over the integration bandwidth of the component carrier. This value is expressed in dBm. The carrier power is reported in dBm when you set the SetPowerUnits(string, RFmxNRMXAcpPowerUnits) method to dBm, and in dBm/Hz when you set the ACP Pwr Units method to dBmByHz. |
| relativePower | ref double[] | Upon return, contains an array of the component carrier power relative to its subblock power. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXAcpComponentCarrierResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpcomponentcarrierresults-getabsolutepower__string-out.html language=enus -->
## TOPIC 00065: GetAbsolutePower(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpcomponentcarrierresults-getabsolutepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpcomponentcarrierresults-getabsolutepower__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power measured over the integration bandwidth of the component carrier. The carrier power is reported in dBm when you set the SetPowerUnits(string, RFmxNRMXAcpPowerUnits) method to dBm, and in dBm/Hz when you set the ACP Pwr Units method to dBmByHz. SyntaxNamespace: NationalInstruments.RFmx

### GetAbsolutePower(string, out double)

Gets the power measured over the integration bandwidth of the component carrier. The carrier power is reported in dBm when you set the [SetPowerUnits(string, RFmxNRMXAcpPowerUnits)](nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setpowerunits__string-rfmxnrmxacppowerunits.html) method to [dBm](nationalinstruments-rfmx-nrmx-rfmxnrmxacppowerunits.html), and in dBm/Hz when you set the ACP Pwr Units method to [dBmByHz](nationalinstruments-rfmx-nrmx-rfmxnrmxacppowerunits.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetAbsolutePower(string selectorString, out double value)

#### Remarks

This method gets the value of [AcpResultsComponentCarrierAbsolutePower](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power measured over the integration bandwidth of the component carrier. The carrier power is reported in dBm when you set the SetPowerUnits(string, RFmxNRMXAcpPowerUnits) method to dBm, and in dBm/Hz when you set the ACP Pwr Units method to dBmByHz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXAcpComponentCarrierResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpcomponentcarrierresults-getrelativepower__string-out.html language=enus -->
## TOPIC 00066: GetRelativePower(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpcomponentcarrierresults-getrelativepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpcomponentcarrierresults-getrelativepower__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the component carrier power relative to its subblock power. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetRelativePower(string selectorString, out double value)RemarksThis method gets the value of AcpResultsComponentCarrierRelativePower attribute.Par

### GetRelativePower(string, out double)

Gets the component carrier power relative to its subblock power. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetRelativePower(string selectorString, out double value)

#### Remarks

This method gets the value of [AcpResultsComponentCarrierRelativePower](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the component carrier power relative to its subblock power. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXAcpComponentCarrierResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpcomponentcarrierresults.html language=enus -->
## TOPIC 00067: RFmxNRMXAcpComponentCarrierResults Class

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpcomponentcarrierresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpcomponentcarrierresults.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the ACP Component Carrier results. Derives fromRFmxNRMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.NRMXpublic class RFmxNRMXAcpComponentCarrierResults : RFmxNRMXSubObjectMethodsNameDescriptionFetchMeasurement(string, double, out double, out double)Returns th

### RFmxNRMXAcpComponentCarrierResults Class

Provides methods to fetch and read the ACP Component Carrier results.

#### Derives from

- RFmxNRMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public class RFmxNRMXAcpComponentCarrierResults : RFmxNRMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchMeasurement(string, double, out double, out double) | Returns the absolute and relative powers measured in the component carriers. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
| FetchMeasurementArray(string, double, ref double[], ref double[]) | Returns an array of the absolute and relative powers measured in the component carriers. Use "subblock(n)" as the selector string to read results from this method. |
| GetAbsolutePower(string, out double) | Gets the power measured over the integration bandwidth of the component carrier. The carrier power is reported in dBm when you set the SetPowerUnits(string, RFmxNRMXAcpPowerUnits) method to dBm, and in dBm/Hz when you set the ACP Pwr Units method to dBmByHz. |
| GetRelativePower(string, out double) | Gets the component carrier power relative to its subblock power. This value is expressed in dB. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-componentcarrier.html language=enus -->
## TOPIC 00068: ComponentCarrier

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-componentcarrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-componentcarrier.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxNRMXAcpComponentCarrierConfiguration instance. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic RFmxNRMXAcpComponentCarrierConfiguration ComponentCarrier { get; }

### ComponentCarrier

Gets the [RFmxNRMXAcpComponentCarrierConfiguration](nationalinstruments-rfmx-nrmx-rfmxnrmxacpcomponentcarrierconfiguration.html) instance.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public [RFmxNRMXAcpComponentCarrierConfiguration](nationalinstruments-rfmx-nrmx-rfmxnrmxacpcomponentcarrierconfiguration.html) ComponentCarrier { get; }

Parent topic:

RFmxNRMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-configureaveraging__string-rfmxnrmxacpaveragingenabled-int-rfmxnrmxacpaveragingtype.html language=enus -->
## TOPIC 00069: ConfigureAveraging(string, RFmxNRMXAcpAveragingEnabled, int, RFmxNRMXAcpAveragingType)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-configureaveraging__string-rfmxnrmxacpaveragingenabled-int-rfmxnrmxacpaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-configureaveraging__string-rfmxnrmxacpaveragingenabled-int-rfmxnrmxacpaveragingtype.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the ACP measurement.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int ConfigureAveraging(string selectorString, RFmxNRMXAcpAveragingEnabled averagingEnabled, int averagingCount, RFmxNRMXAcpAveragingType averagingType)ParametersNameTypeDescriptionselectorStringstringPa

### ConfigureAveraging(string, RFmxNRMXAcpAveragingEnabled, int, RFmxNRMXAcpAveragingType)

Configures averaging for the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int ConfigureAveraging(string selectorString, RFmxNRMXAcpAveragingEnabled averagingEnabled, int averagingCount, RFmxNRMXAcpAveragingType averagingType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| averagingEnabled | RFmxNRMXAcpAveragingEnabled | Specifies whether to enable averaging for the measurement. |
| averagingCount | int | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True. |
| averagingType | RFmxNRMXAcpAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-configurerbwfilter__string-rfmxnrmxacprbwautobandwidth-double-rfmxnrmxacprbwfiltertype.html language=enus -->
## TOPIC 00070: ConfigureRbwFilter(string, RFmxNRMXAcpRbwAutoBandwidth, double, RFmxNRMXAcpRbwFilterType)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-configurerbwfilter__string-rfmxnrmxacprbwautobandwidth-double-rfmxnrmxacprbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-configurerbwfilter__string-rfmxnrmxacprbwautobandwidth-double-rfmxnrmxacprbwfiltertype.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the resolution bandwidth (RBW) filter.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int ConfigureRbwFilter(string selectorString, RFmxNRMXAcpRbwAutoBandwidth rbwAuto, double rbw, RFmxNRMXAcpRbwFilterType rbwFilterType)ParametersNameTypeDescriptionselectorStringstringPass an empty s

### ConfigureRbwFilter(string, RFmxNRMXAcpRbwAutoBandwidth, double, RFmxNRMXAcpRbwFilterType)

Configures the resolution bandwidth (RBW) filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int ConfigureRbwFilter(string selectorString, RFmxNRMXAcpRbwAutoBandwidth rbwAuto, double rbw, RFmxNRMXAcpRbwFilterType rbwFilterType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| rbwAuto | RFmxNRMXAcpRbwAutoBandwidth | Specifies whether the measurement computes the RBW. |
| rbw | double | Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the rbwAuto parameter to False. This value is expressed in Hz. |
| rbwFilterType | RFmxNRMXAcpRbwFilterType | Specifies the shape of the RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00071: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the traces to be stored and retrieved after performing the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method gets the value of AcpAllTracesEnabled attribute.The default value i

### GetAllTracesEnabled(string, out bool)

Gets whether to enable the traces to be stored and retrieved after performing the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [AcpAllTracesEnabled](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the traces to be stored and retrieved after performing the ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getamplitudecorrectiontype__string-out.html language=enus -->
## TOPIC 00072: GetAmplitudeCorrectionType(string, out RFmxNRMXAcpAmplitudeCorrectionType)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getamplitudecorrectiontype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getamplitudecorrectiontype__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. SyntaxNamespace: National

### GetAmplitudeCorrectionType(string, out RFmxNRMXAcpAmplitudeCorrectionType)

Gets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetAmplitudeCorrectionType(string selectorString, out RFmxNRMXAcpAmplitudeCorrectionType value)

#### Remarks

This method gets the value of [AcpAmplitudeCorrectionType](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [RFCenterFrequency](nationalinstruments-rfmx-nrmx-rfmxnrmxacpamplitudecorrectiontype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxNRMXAcpAmplitudeCorrectionType | Upon return, contains whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getaveragingcount__string-out.html language=enus -->
## TOPIC 00073: GetAveragingCount(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getaveragingcount__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getaveragingcount__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxNRMXAcpAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetAveragingCount(string selectorString, out int value)RemarksThis method gets the value of AcpAveragi

### GetAveragingCount(string, out int)

Gets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxNRMXAcpAveragingEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setaveragingenabled__string-rfmxnrmxacpaveragingenabled.html) method to [True](nationalinstruments-rfmx-nrmx-rfmxnrmxacpaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetAveragingCount(string selectorString, out int value)

#### Remarks

This method gets the value of [AcpAveragingCount](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxNRMXAcpAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getfftwindow__string-out.html language=enus -->
## TOPIC 00074: GetFftWindow(string, out RFmxNRMXAcpFftWindow)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getfftwindow__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getfftwindow__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the FFT window type to be used to reduce spectral leakage. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetFftWindow(string selectorString, out RFmxNRMXAcpFftWindow value)RemarksThis method gets the value of AcpFftWindow attribute.The default value is FlatTop.ParametersNameTypeDescr

### GetFftWindow(string, out RFmxNRMXAcpFftWindow)

Gets the FFT window type to be used to reduce spectral leakage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetFftWindow(string selectorString, out RFmxNRMXAcpFftWindow value)

#### Remarks

This method gets the value of [AcpFftWindow](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [FlatTop](nationalinstruments-rfmx-nrmx-rfmxnrmxacpfftwindow.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxNRMXAcpFftWindow | Upon return, contains the FFT window type to be used to reduce spectral leakage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getnoisecalibrationaveragingauto__string-out.html language=enus -->
## TOPIC 00075: GetNoiseCalibrationAveragingAuto(string, out RFmxNRMXAcpNoiseCalibrationAveragingAuto)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getnoisecalibrationaveragingauto__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getnoisecalibrationaveragingauto__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether RFmx automatically computes the averaging count used for instrument noise calibration. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetNoiseCalibrationAveragingAuto(string selectorString, out RFmxNRMXAcpNoiseCalibrationAveragingAuto value)RemarksThis method gets the value of

### GetNoiseCalibrationAveragingAuto(string, out RFmxNRMXAcpNoiseCalibrationAveragingAuto)

Gets whether RFmx automatically computes the averaging count used for instrument noise calibration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetNoiseCalibrationAveragingAuto(string selectorString, out RFmxNRMXAcpNoiseCalibrationAveragingAuto value)

#### Remarks

This method gets the value of [AcpNoiseCalibrationAveragingAuto](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-nrmx-rfmxnrmxacpnoisecalibrationaveragingauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxNRMXAcpNoiseCalibrationAveragingAuto | Upon return, contains whether RFmx automatically computes the averaging count used for instrument noise calibration. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getnoisecalibrationaveragingcount__string-out.html language=enus -->
## TOPIC 00076: GetNoiseCalibrationAveragingCount(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getnoisecalibrationaveragingcount__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getnoisecalibrationaveragingcount__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(string, RFmxNRMXAcpNoiseCalibrationAveragingAuto) method to False. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetNoiseCalibrationAveragingCount(string selectorString, out int value)Rem

### GetNoiseCalibrationAveragingCount(string, out int)

Gets the averaging count used for noise calibration when you set the [SetNoiseCalibrationAveragingAuto(string, RFmxNRMXAcpNoiseCalibrationAveragingAuto)](nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setnoisecalibrationaveragingauto__string-rfmxnrmxacpnoisecalibrationaveragingauto.html) method to [False](nationalinstruments-rfmx-nrmx-rfmxnrmxacpnoisecalibrationaveragingauto.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetNoiseCalibrationAveragingCount(string selectorString, out int value)

#### Remarks

This method gets the value of [AcpNoiseCalibrationAveragingCount](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 32.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(string, RFmxNRMXAcpNoiseCalibrationAveragingAuto) method to False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getnoisecalibrationmode__string-out.html language=enus -->
## TOPIC 00077: GetNoiseCalibrationMode(string, out RFmxNRMXAcpNoiseCalibrationMode)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getnoisecalibrationmode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getnoisecalibrationmode__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetNoiseCalibrationMode(

### GetNoiseCalibrationMode(string, out RFmxNRMXAcpNoiseCalibrationMode)

Gets whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetNoiseCalibrationMode(string selectorString, out RFmxNRMXAcpNoiseCalibrationMode value)

#### Remarks

This method gets the value of [AcpNoiseCalibrationMode](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Auto](nationalinstruments-rfmx-nrmx-rfmxnrmxacpnoisecalibrationmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxNRMXAcpNoiseCalibrationMode | Upon return, contains whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getnoisecompensationenabled__string-out.html language=enus -->
## TOPIC 00078: GetNoiseCompensationEnabled(string, out RFmxNRMXAcpNoiseCompensationEnabled)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getnoisecompensationenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getnoisecompensationenabled__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether RFmx compensates for the instrument noise when performing the measurement when you set SetNoiseCalibrationMode(string, RFmxNRMXAcpNoiseCalibrationMode) method to Auto, or when you set ACP Noise Cal Mode to Manual and SetMeasurementMode(string, RFmxNRMXAcpMeasurementMode) method to Measu

### GetNoiseCompensationEnabled(string, out RFmxNRMXAcpNoiseCompensationEnabled)

Gets whether RFmx compensates for the instrument noise when performing the measurement when you set [SetNoiseCalibrationMode(string, RFmxNRMXAcpNoiseCalibrationMode)](nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setnoisecalibrationmode__string-rfmxnrmxacpnoisecalibrationmode.html) method to [Auto](nationalinstruments-rfmx-nrmx-rfmxnrmxacpnoisecalibrationmode.html), or when you set ACP Noise Cal Mode to [Manual](nationalinstruments-rfmx-nrmx-rfmxnrmxacpnoisecalibrationmode.html) and [SetMeasurementMode(string, RFmxNRMXAcpMeasurementMode)](nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setmeasurementmode__string-rfmxnrmxacpmeasurementmode.html) method to [Measure](nationalinstruments-rfmx-nrmx-rfmxnrmxacpmeasurementmode.html) Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetNoiseCompensationEnabled(string selectorString, out RFmxNRMXAcpNoiseCompensationEnabled value)

#### Remarks

This method gets the value of [AcpNoiseCompensationEnabled](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-nrmx-rfmxnrmxacpnoisecompensationenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxNRMXAcpNoiseCompensationEnabled | Upon return, contains whether RFmx compensates for the instrument noise when performing the measurement when you set SetNoiseCalibrationMode(string, RFmxNRMXAcpNoiseCalibrationMode) method to Auto, or when you set ACP Noise Cal Mode to Manual and SetMeasurementMode(string, RFmxNRMXAcpMeasurementMode) method to Measure Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getnumberofanalysisthreads__string-out.html language=enus -->
## TOPIC 00079: GetNumberOfAnalysisThreads(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getnumberofanalysisthreads__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getnumberofanalysisthreads__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum number of threads used for parallelism for the ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetNumberOfAnalysisThreads(string selectorString, out int value)RemarksThis method gets the value of AcpNumberOfAnalysisThreads attribute.The default value is 1.P

### GetNumberOfAnalysisThreads(string, out int)

Gets the maximum number of threads used for parallelism for the ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetNumberOfAnalysisThreads(string selectorString, out int value)

#### Remarks

This method gets the value of [AcpNumberOfAnalysisThreads](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the maximum number of threads used for parallelism for the ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getnumberofendcoffsets__string-out.html language=enus -->
## TOPIC 00080: GetNumberOfEndcOffsets(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getnumberofendcoffsets__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getnumberofendcoffsets__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of ENDC adjacent channel offsets to be configured at offset positions. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetNumberOfEndcOffsets(string selectorString, out int value)RemarksThis method gets the value of AcpNumberOfEndcOffsets attribute.The default value is depen

### GetNumberOfEndcOffsets(string, out int)

Gets the number of ENDC adjacent channel offsets to be configured at offset positions.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetNumberOfEndcOffsets(string selectorString, out int value)

#### Remarks

This method gets the value of [AcpNumberOfEndcOffsets](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is dependent on 3GPP specification.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the number of ENDC adjacent channel offsets to be configured at offset positions. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getrbwfilterbandwidth__string-out.html language=enus -->
## TOPIC 00081: GetRbwFilterBandwidth(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getrbwfilterbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getrbwfilterbandwidth__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(string, RFmxNRMXAcpRbwAutoBandwidth) method to False. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetRbwFilterBandwidth(string selectorStrin

### GetRbwFilterBandwidth(string, out double)

Gets the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the [SetRbwFilterAutoBandwidth(string, RFmxNRMXAcpRbwAutoBandwidth)](nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setrbwfilterautobandwidth__string-rfmxnrmxacprbwautobandwidth.html) method to [False](nationalinstruments-rfmx-nrmx-rfmxnrmxacprbwautobandwidth.html). This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetRbwFilterBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [AcpRbwFilterBandwidth](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 30 kHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(string, RFmxNRMXAcpRbwAutoBandwidth) method to False. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getsequentialfftsize__string-out.html language=enus -->
## TOPIC 00082: GetSequentialFftSize(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getsequentialfftsize__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getsequentialfftsize__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of bins to be used for FFT computation, when you set the SetMeasurementMethod(string, RFmxNRMXAcpMeasurementMethod) method to SequentialFft. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetSequentialFftSize(string selectorString, out int value)RemarksThis method gets the

### GetSequentialFftSize(string, out int)

Gets the number of bins to be used for FFT computation, when you set the [SetMeasurementMethod(string, RFmxNRMXAcpMeasurementMethod)](nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setmeasurementmethod__string-rfmxnrmxacpmeasurementmethod.html) method to [SequentialFft](nationalinstruments-rfmx-nrmx-rfmxnrmxacpmeasurementmethod.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetSequentialFftSize(string selectorString, out int value)

#### Remarks

This method gets the value of [AcpSequentialFftSize](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 512.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of bins to be used for FFT computation, when you set the SetMeasurementMethod(string, RFmxNRMXAcpMeasurementMethod) method to SequentialFft. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getsubblockintegrationbandwidth__string-out.html language=enus -->
## TOPIC 00083: GetSubblockIntegrationBandwidth(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getsubblockintegrationbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getsubblockintegrationbandwidth__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the integration bandwidth of a subblock. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetSubblockIntegrationBan

### GetSubblockIntegrationBandwidth(string, out double)

Gets the integration bandwidth of a subblock. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetSubblockIntegrationBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [AcpSubblockIntegrationBandwidth](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the integration bandwidth of a subblock. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getsweeptimeauto__string-out.html language=enus -->
## TOPIC 00084: GetSweepTimeAuto(string, out RFmxNRMXAcpSweepTimeAuto)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getsweeptimeauto__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-getsweeptimeauto__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement sets the sweep time. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetSweepTimeAuto(string selectorString, out RFmxNRMXAcpSweepTimeAuto value)RemarksThis method gets the value of AcpSweepTimeAuto attribute.The default value is True.ParametersNameTypeDescriptio

### GetSweepTimeAuto(string, out RFmxNRMXAcpSweepTimeAuto)

Gets whether the measurement sets the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetSweepTimeAuto(string selectorString, out RFmxNRMXAcpSweepTimeAuto value)

#### Remarks

This method gets the value of [AcpSweepTimeAuto](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-nrmx-rfmxnrmxacpsweeptimeauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxNRMXAcpSweepTimeAuto | Upon return, contains whether the measurement sets the sweep time. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setaveragingcount__string-int.html language=enus -->
## TOPIC 00085: SetAveragingCount(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setaveragingcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setaveragingcount__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxNRMXAcpAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetAveragingCount(string selectorString, int value)RemarksThis method sets the value of AcpAveragingCo

### SetAveragingCount(string, int)

Sets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxNRMXAcpAveragingEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setaveragingenabled__string-rfmxnrmxacpaveragingenabled.html) method to [True](nationalinstruments-rfmx-nrmx-rfmxnrmxacpaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetAveragingCount(string selectorString, int value)

#### Remarks

This method sets the value of [AcpAveragingCount](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxNRMXAcpAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setaveragingtype__string-rfmxnrmxacpaveragingtype.html language=enus -->
## TOPIC 00086: SetAveragingType(string, RFmxNRMXAcpAveragingType)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setaveragingtype__string-rfmxnrmxacpaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setaveragingtype__string-rfmxnrmxacpaveragingtype.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetAveragingType(string selectorString, RFmxNRMXAcpAveragingType value)RemarksThis method sets the value of AcpAveragingTy

### SetAveragingType(string, RFmxNRMXAcpAveragingType)

Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetAveragingType(string selectorString, RFmxNRMXAcpAveragingType value)

#### Remarks

This method sets the value of [AcpAveragingType](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.Default value is RMS[Rms](nationalinstruments-rfmx-nrmx-rfmxnrmxacpaveragingtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXAcpAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setfarifoutputpoweroffset__string-double.html language=enus -->
## TOPIC 00087: SetFarIFOutputPowerOffset(string, double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setfarifoutputpoweroffset__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setfarifoutputpoweroffset__string-double.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the offset that is needed to adjust the IF output power levels for the offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This method is applicable only when you set the SetIFOutputPowerOffsetAuto(string, RFmxNRMXAcpIFOutputPowerOf

### SetFarIFOutputPowerOffset(string, double)

Sets the offset that is needed to adjust the IF output power levels for the offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This method is applicable only when you set the [SetIFOutputPowerOffsetAuto(string, RFmxNRMXAcpIFOutputPowerOffsetAuto)](nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setifoutputpoweroffsetauto__string-rfmxnrmxacpifoutputpoweroffsetauto.html) method to [False](nationalinstruments-rfmx-nrmx-rfmxnrmxacpifoutputpoweroffsetauto.html) and [SetMeasurementMethod(string, RFmxNRMXAcpMeasurementMethod)](nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setmeasurementmethod__string-rfmxnrmxacpmeasurementmethod.html) method to [DynamicRange](nationalinstruments-rfmx-nrmx-rfmxnrmxacpmeasurementmethod.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetFarIFOutputPowerOffset(string selectorString, double value)

#### Remarks

This method sets the value of [AcpFarIFOutputPowerOffset](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 20.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the offset that is needed to adjust the IF output power levels for the offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This method is applicable only when you set the SetIFOutputPowerOffsetAuto(string, RFmxNRMXAcpIFOutputPowerOffsetAuto) method to False and SetMeasurementMethod(string, RFmxNRMXAcpMeasurementMethod) method to DynamicRange. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setfftoverlapmode__string-rfmxnrmxacpfftoverlapmode.html language=enus -->
## TOPIC 00088: SetFftOverlapMode(string, RFmxNRMXAcpFftOverlapMode)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setfftoverlapmode__string-rfmxnrmxacpfftoverlapmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setfftoverlapmode__string-rfmxnrmxacpfftoverlapmode.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the overlap mode when you set the SetMeasurementMethod(string, RFmxNRMXAcpMeasurementMethod) method to SequentialFft. In the Sequential FFT method, the measurement divides all the acquired samples into smaller FFT chunks of equal size. The FFT is then computed for each chunk. The resultant FFTs

### SetFftOverlapMode(string, RFmxNRMXAcpFftOverlapMode)

Sets the overlap mode when you set the [SetMeasurementMethod(string, RFmxNRMXAcpMeasurementMethod)](nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setmeasurementmethod__string-rfmxnrmxacpmeasurementmethod.html) method to [SequentialFft](nationalinstruments-rfmx-nrmx-rfmxnrmxacpmeasurementmethod.html). In the Sequential FFT method, the measurement divides all the acquired samples into smaller FFT chunks of equal size. The FFT is then computed for each chunk. The resultant FFTs are averaged to get the spectrum used to compute the ACP.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetFftOverlapMode(string selectorString, RFmxNRMXAcpFftOverlapMode value)

#### Remarks

This method sets the value of [AcpFftOverlapMode](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Disabled](nationalinstruments-rfmx-nrmx-rfmxnrmxacpfftoverlapmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXAcpFftOverlapMode | Specifies the overlap mode when you set the SetMeasurementMethod(string, RFmxNRMXAcpMeasurementMethod) method to SequentialFft. In the Sequential FFT method, the measurement divides all the acquired samples into smaller FFT chunks of equal size. The FFT is then computed for each chunk. The resultant FFTs are averaged to get the spectrum used to compute the ACP. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setrbwfilterbandwidth__string-double.html language=enus -->
## TOPIC 00089: SetRbwFilterBandwidth(string, double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setrbwfilterbandwidth__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setrbwfilterbandwidth__string-double.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(string, RFmxNRMXAcpRbwAutoBandwidth) method to False. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetRbwFilterBandwidth(string selectorStrin

### SetRbwFilterBandwidth(string, double)

Sets the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the [SetRbwFilterAutoBandwidth(string, RFmxNRMXAcpRbwAutoBandwidth)](nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setrbwfilterautobandwidth__string-rfmxnrmxacprbwautobandwidth.html) method to [False](nationalinstruments-rfmx-nrmx-rfmxnrmxacprbwautobandwidth.html). This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetRbwFilterBandwidth(string selectorString, double value)

#### Remarks

This method sets the value of [AcpRbwFilterBandwidth](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 30 kHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(string, RFmxNRMXAcpRbwAutoBandwidth) method to False. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setsubblockoffset__string-double.html language=enus -->
## TOPIC 00090: SetSubblockOffset(string, double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setsubblockoffset__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setsubblockoffset__string-double.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the offset of the subblock measurement relative to the subblock center. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetSubblockOffset(string selectorString, double value)RemarksThis method sets the value of AcpSubblockOffset attribute.The default valu

### SetSubblockOffset(string, double)

Sets the offset of the subblock measurement relative to the subblock center. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetSubblockOffset(string selectorString, double value)

#### Remarks

This method sets the value of [AcpSubblockOffset](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(string, int) method to build the selector string. |
| value | double | Specifies the offset of the subblock measurement relative to the subblock center. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setsweeptimeinterval__string-double.html language=enus -->
## TOPIC 00091: SetSweepTimeInterval(string, double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setsweeptimeinterval__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setsweeptimeinterval__string-double.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the sweep time when you set the SetSweepTimeAuto(string, RFmxNRMXAcpSweepTimeAuto) method to False. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetSweepTimeInterval(string selectorString, double value)RemarksThis method sets the value of AcpSweep

### SetSweepTimeInterval(string, double)

Sets the sweep time when you set the [SetSweepTimeAuto(string, RFmxNRMXAcpSweepTimeAuto)](nationalinstruments-rfmx-nrmx-rfmxnrmxacpconfiguration-setsweeptimeauto__string-rfmxnrmxacpsweeptimeauto.html) method to [False](nationalinstruments-rfmx-nrmx-rfmxnrmxacpsweeptimeauto.html). This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetSweepTimeInterval(string selectorString, double value)

#### Remarks

This method sets the value of [AcpSweepTimeInterval](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 1 ms.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the sweep time when you set the SetSweepTimeAuto(string, RFmxNRMXAcpSweepTimeAuto) method to False. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXAcpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacprbwfiltertype.html language=enus -->
## TOPIC 00092: RFmxNRMXAcpRbwFilterType Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacprbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacprbwfiltertype.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of the RBW filter. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXAcpRbwFilterTypeMembersNameValueDescriptionFftBased0No RBW filtering is performed. Gaussian1An RBW filter with a Gaussian response is applied. Flat2An RBW filter with a flat response is applied.

### RFmxNRMXAcpRbwFilterType Enumeration

Specifies the shape of the RBW filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXAcpRbwFilterType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| FftBased | 0 | No RBW filtering is performed. |
| Gaussian | 1 | An RBW filter with a Gaussian response is applied. |
| Flat | 2 | An RBW filter with a flat response is applied. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxacpresults-getupperoffsetrelativepower__string-out.html language=enus -->
## TOPIC 00093: GetUpperOffsetRelativePower(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxacpresults-getupperoffsetrelativepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxacpresults-getupperoffsetrelativepower__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power in the upper (positive) offset channel relative to the total aggregated power. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetUpperOffsetRelativePower(string selectorString, out double value)RemarksThis method gets the value of AcpResultsUpp

### GetUpperOffsetRelativePower(string, out double)

Gets the power in the upper (positive) offset channel relative to the total aggregated power. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetUpperOffsetRelativePower(string selectorString, out double value)

#### Remarks

This method gets the value of [AcpResultsUpperOffsetRelativePower](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power in the upper (positive) offset channel relative to the total aggregated power. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXAcpResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxchp-configuration.html language=enus -->
## TOPIC 00094: Configuration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxchp-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxchp-configuration.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxNRMXChpConfiguration instance that provides methods to configure the CHP measurement. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic RFmxNRMXChpConfiguration Configuration { get; }

### Configuration

Gets the [RFmxNRMXChpConfiguration](nationalinstruments-rfmx-nrmx-rfmxnrmxchpconfiguration.html) instance that provides methods to configure the CHP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public [RFmxNRMXChpConfiguration](nationalinstruments-rfmx-nrmx-rfmxnrmxchpconfiguration.html) Configuration { get; }

Parent topic:

RFmxNRMXChp Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxchpcomponentcarrierconfiguration-getintegrationbandwidth__string-out.html language=enus -->
## TOPIC 00095: GetIntegrationBandwidth(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxchpcomponentcarrierconfiguration-getintegrationbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxchpcomponentcarrierconfiguration-getintegrationbandwidth__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the integration bandwidth of a component carrier (CC). This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetIntegrationBandwidth(string selectorString, out double value)RemarksThis method gets the value of ChpComponentCarrierIntegrationBandwidth attribute.T

### GetIntegrationBandwidth(string, out double)

Gets the integration bandwidth of a component carrier (CC). This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetIntegrationBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [ChpComponentCarrierIntegrationBandwidth](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 9 MHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the integration bandwidth of a component carrier (CC). This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXChpComponentCarrierConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxchpcomponentcarrierconfiguration.html language=enus -->
## TOPIC 00096: RFmxNRMXChpComponentCarrierConfiguration Class

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxchpcomponentcarrierconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxchpcomponentcarrierconfiguration.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the CHP Component Carrier measurement. Derives fromRFmxNRMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.NRMXpublic class RFmxNRMXChpComponentCarrierConfiguration : RFmxNRMXSubObjectMethodsNameDescriptionGetIntegrationBandwidth(string, out double)Gets the integrati

### RFmxNRMXChpComponentCarrierConfiguration Class

Provides methods to configure the CHP Component Carrier measurement.

#### Derives from

- RFmxNRMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public class RFmxNRMXChpComponentCarrierConfiguration : RFmxNRMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| GetIntegrationBandwidth(string, out double) | Gets the integration bandwidth of a component carrier (CC). This value is expressed in Hz. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxchpcomponentcarrierresults-fetchmeasurementarray__string-double-ref-ref.html language=enus -->
## TOPIC 00097: FetchMeasurementArray(string, double, ref double[], ref double[])

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxchpcomponentcarrierresults-fetchmeasurementarray__string-double-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxchpcomponentcarrierresults-fetchmeasurementarray__string-double-ref-ref.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an arry of the absolute and relative powers measured in the component carriers. Use "subblock(n)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int FetchMeasurementArray(string selectorString, double timeout, ref double[] absolut

### FetchMeasurementArray(string, double, ref double[], ref double[])

Returns an arry of the absolute and relative powers measured in the component carriers. 
 Use "subblock(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int FetchMeasurementArray(string selectorString, double timeout, ref double[] absolutePower, ref double[] relativePower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| absolutePower | ref double[] | Upon return, contains an array of the power measured over the integration bandwidth of the component carrier. This value is expressed in dBm. |
| relativePower | ref double[] | Upon return, contains an array of the component carrier power relative to its subblock power. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXChpComponentCarrierResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxchpcomponentcarrierresults-getabsolutepower__string-out.html language=enus -->
## TOPIC 00098: GetAbsolutePower(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxchpcomponentcarrierresults-getabsolutepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxchpcomponentcarrierresults-getabsolutepower__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power measured over the integration bandwidth of the component carrier. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetAbsolutePower(string selectorString, out double value)RemarksThis method gets the value of ChpResultsComponentCarrierAbsolutePo

### GetAbsolutePower(string, out double)

Gets the power measured over the integration bandwidth of the component carrier. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetAbsolutePower(string selectorString, out double value)

#### Remarks

This method gets the value of [ChpResultsComponentCarrierAbsolutePower](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power measured over the integration bandwidth of the component carrier. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXChpComponentCarrierResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxchpconfiguration-getnoisecalibrationmode__string-out.html language=enus -->
## TOPIC 00099: GetNoiseCalibrationMode(string, out RFmxNRMXChpNoiseCalibrationMode)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxchpconfiguration-getnoisecalibrationmode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxchpconfiguration-getnoisecalibrationmode__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetNoiseCalibrationMode(

### GetNoiseCalibrationMode(string, out RFmxNRMXChpNoiseCalibrationMode)

Gets whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetNoiseCalibrationMode(string selectorString, out RFmxNRMXChpNoiseCalibrationMode value)

#### Remarks

This method gets the value of [ChpNoiseCalibrationMode](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Auto](nationalinstruments-rfmx-nrmx-rfmxnrmxchpnoisecalibrationmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxNRMXChpNoiseCalibrationMode | Upon return, contains whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxchpconfiguration-setamplitudecorrectiontype__string-rfmxnrmxchpamplitudecorrectiontype.html language=enus -->
## TOPIC 00100: SetAmplitudeCorrectionType(string, RFmxNRMXChpAmplitudeCorrectionType)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxchpconfiguration-setamplitudecorrectiontype__string-rfmxnrmxchpamplitudecorrectiontype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxchpconfiguration-setamplitudecorrectiontype__string-rfmxnrmxchpamplitudecorrectiontype.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the amplitude of frequency bins in the spectrum used by the measurement is corrected for external attenuation at RF center frequency or corrected for external attenuation at individual frequency bins Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenu

### SetAmplitudeCorrectionType(string, RFmxNRMXChpAmplitudeCorrectionType)

Sets whether the amplitude of frequency bins in the spectrum used by the measurement is corrected for external attenuation at RF center frequency or corrected for external attenuation at individual frequency bins Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetAmplitudeCorrectionType(string selectorString, RFmxNRMXChpAmplitudeCorrectionType value)

#### Remarks

This method sets the value of [ChpAmplitudeCorrectionType](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [RFCenterFrequency](nationalinstruments-rfmx-nrmx-rfmxnrmxchpamplitudecorrectiontype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXChpAmplitudeCorrectionType | Specifies whether the amplitude of frequency bins in the spectrum used by the measurement is corrected for external attenuation at RF center frequency or corrected for external attenuation at individual frequency bins Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxchpconfiguration-setnoisecompensationtype__string-rfmxnrmxchpnoisecompensationtype.html language=enus -->
## TOPIC 00101: SetNoiseCompensationType(string, RFmxNRMXChpNoiseCompensationType)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxchpconfiguration-setnoisecompensationtype__string-rfmxnrmxchpnoisecompensationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxchpconfiguration-setnoisecompensationtype__string-rfmxnrmxchpnoisecompensationtype.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetNoiseCompensationType(string selectorString, RFmxNRMXChpNoiseCompensationType value)RemarksThis me

### SetNoiseCompensationType(string, RFmxNRMXChpNoiseCompensationType)

Sets the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetNoiseCompensationType(string selectorString, RFmxNRMXChpNoiseCompensationType value)

#### Remarks

This method sets the value of [ChpNoiseCompensationType](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [AnalyzerAndTermination](nationalinstruments-rfmx-nrmx-rfmxnrmxchpnoisecompensationtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXChpNoiseCompensationType | Specifies the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxchpconfiguration-setnumberofanalysisthreads__string-int.html language=enus -->
## TOPIC 00102: SetNumberOfAnalysisThreads(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxchpconfiguration-setnumberofanalysisthreads__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxchpconfiguration-setnumberofanalysisthreads__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the maximum number of threads used for parallelism for the CHP measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, dat

### SetNumberOfAnalysisThreads(string, int)

Sets the maximum number of threads used for parallelism for the CHP measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetNumberOfAnalysisThreads(string selectorString, int value)

#### Remarks

This method sets the value of [ChpNumberOfAnalysisThreads](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the maximum number of threads used for parallelism for the CHP measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxchpconfiguration-setrbwfilterbandwidth__string-double.html language=enus -->
## TOPIC 00103: SetRbwFilterBandwidth(string, double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxchpconfiguration-setrbwfilterbandwidth__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxchpconfiguration-setrbwfilterbandwidth__string-double.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(string, RFmxNRMXChpRbwAutoBandwidth) method to False. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetRbwFilterBandwidth(string selectorStrin

### SetRbwFilterBandwidth(string, double)

Sets the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the [SetRbwFilterAutoBandwidth(string, RFmxNRMXChpRbwAutoBandwidth)](nationalinstruments-rfmx-nrmx-rfmxnrmxchpconfiguration-setrbwfilterautobandwidth__string-rfmxnrmxchprbwautobandwidth.html) method to [False](nationalinstruments-rfmx-nrmx-rfmxnrmxchprbwautobandwidth.html). This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetRbwFilterBandwidth(string selectorString, double value)

#### Remarks

This method sets the value of [ChpRbwFilterBandwidth](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 30 kHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(string, RFmxNRMXChpRbwAutoBandwidth) method to False. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXChpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxchpconfiguration.html language=enus -->
## TOPIC 00104: RFmxNRMXChpConfiguration Class

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxchpconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxchpconfiguration.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the CHP measurement. Derives fromRFmxNRMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.NRMXpublic class RFmxNRMXChpConfiguration : RFmxNRMXSubObjectPropertiesNameDescriptionComponentCarrierGets the RFmxNRMXChpComponentCarrierConfiguration instance. MethodsNameDescr

### RFmxNRMXChpConfiguration Class

Provides methods to configure the CHP measurement.

#### Derives from

- RFmxNRMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public class RFmxNRMXChpConfiguration : RFmxNRMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| ComponentCarrier | Gets the RFmxNRMXChpComponentCarrierConfiguration instance. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureAveraging(string, RFmxNRMXChpAveragingEnabled, int, RFmxNRMXChpAveragingType) | Configures averaging for the CHP measurement. |
| ConfigureRbwFilter(string, RFmxNRMXChpRbwAutoBandwidth, double, RFmxNRMXChpRbwFilterType) | Configures the resolution bandwidth (RBW) filter. |
| ConfigureSweepTime(string, RFmxNRMXChpSweepTimeAuto, double) | Configures the sweep time. |
| GetAllTracesEnabled(string, out bool) | Gets whether to enable the traces to be stored and retrieved after performing the CHP measurement. |
| GetAmplitudeCorrectionType(string, out RFmxNRMXChpAmplitudeCorrectionType) | Gets whether the amplitude of frequency bins in the spectrum used by the measurement is corrected for external attenuation at RF center frequency or corrected for external attenuation at individual frequency bins Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |
| GetAveragingCount(string, out int) | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxNRMXChpAveragingEnabled) method to True. |
| GetAveragingEnabled(string, out RFmxNRMXChpAveragingEnabled) | Gets whether to enable averaging for the CHP measurement. |
| GetAveragingType(string, out RFmxNRMXChpAveragingType) | Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for CHP measurement. |
| GetFftWindow(string, out RFmxNRMXChpFftWindow) | Gets the FFT window type to be used to reduce spectral leakage. |
| GetIntegrationBandwidthType(string, out RFmxNRMXChpIntegrationBandwidthType) | Gets the integration bandwidth (IBW) type used to measure the power of the acquired signal. Integration bandwidth is the frequency interval over which the power in each frequency bin is added to measure the total power in that interval. |
| GetMeasurementEnabled(string, out bool) | Gets whether to enable the channel power measurement. |
| GetMeasurementMode(string, out RFmxNRMXChpMeasurementMode) | Gets whether the measurement calibrates the noise floor of analyzer or performs the CHP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| GetNoiseCalibrationAveragingAuto(string, out RFmxNRMXChpNoiseCalibrationAveragingAuto) | Gets whether RFmx automatically computes the averaging count used for instrument noise calibration. |
| GetNoiseCalibrationAveragingCount(string, out int) | Gets the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(string, RFmxNRMXChpNoiseCalibrationAveragingAuto) method to False. |
| GetNoiseCalibrationMode(string, out RFmxNRMXChpNoiseCalibrationMode) | Gets whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| GetNoiseCompensationEnabled(string, out RFmxNRMXChpNoiseCompensationEnabled) | Gets whether RFmx compensates for the instrument noise when performing the measurement. To compensate for instrument noise when performing a CHP measurement, set the SetNoiseCalibrationMode(string, RFmxNRMXChpNoiseCalibrationMode) method to Auto, or set the CHP Noise Cal Mode method to Manual and the SetMeasurementMode(string, RFmxNRMXChpMeasurementMode) method to Measure. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| GetNoiseCompensationType(string, out RFmxNRMXChpNoiseCompensationType) | Gets the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| GetNumberOfAnalysisThreads(string, out int) | Gets the maximum number of threads used for parallelism for the CHP measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| GetRbwFilterAutoBandwidth(string, out RFmxNRMXChpRbwAutoBandwidth) | Gets whether the measurement computes the RBW. |
| GetRbwFilterBandwidth(string, out double) | Gets the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(string, RFmxNRMXChpRbwAutoBandwidth) method to False. This value is expressed in Hz. |
| GetRbwFilterType(string, out RFmxNRMXChpRbwFilterType) | Gets the shape of the digital RBW filter. |
| GetSubblockIntegrationBandwidth(string, out double) | Gets the integration bandwidth of the subblock. This value is expressed in Hz. It is the span from left edge of the integration bandwidth of the leftmost carrier to the right edge of the integration bandwidth of the rightmost carrier within a subblock. |
| GetSweepTimeAuto(string, out RFmxNRMXChpSweepTimeAuto) | Gets whether the measurement sets the sweep time. |
| GetSweepTimeInterval(string, out double) | Gets the sweep time when you set the SetSweepTimeAuto(string, RFmxNRMXChpSweepTimeAuto) method to False. This value is expressed in seconds. |
| SetAllTracesEnabled(string, bool) | Sets whether to enable the traces to be stored and retrieved after performing the CHP measurement. |
| SetAmplitudeCorrectionType(string, RFmxNRMXChpAmplitudeCorrectionType) | Sets whether the amplitude of frequency bins in the spectrum used by the measurement is corrected for external attenuation at RF center frequency or corrected for external attenuation at individual frequency bins Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |
| SetAveragingCount(string, int) | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxNRMXChpAveragingEnabled) method to True. |
| SetAveragingEnabled(string, RFmxNRMXChpAveragingEnabled) | Sets whether to enable averaging for the CHP measurement. |
| SetAveragingType(string, RFmxNRMXChpAveragingType) | Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for CHP measurement. |
| SetFftWindow(string, RFmxNRMXChpFftWindow) | Sets the FFT window type to be used to reduce spectral leakage. |
| SetIntegrationBandwidthType(string, RFmxNRMXChpIntegrationBandwidthType) | Sets the integration bandwidth (IBW) type used to measure the power of the acquired signal. Integration bandwidth is the frequency interval over which the power in each frequency bin is added to measure the total power in that interval. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable the channel power measurement. |
| SetMeasurementMode(string, RFmxNRMXChpMeasurementMode) | Sets whether the measurement calibrates the noise floor of analyzer or performs the CHP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| SetNoiseCalibrationAveragingAuto(string, RFmxNRMXChpNoiseCalibrationAveragingAuto) | Sets whether RFmx automatically computes the averaging count used for instrument noise calibration. |
| SetNoiseCalibrationAveragingCount(string, int) | Sets the averaging count used for noise calibration when you set the SetNoiseCalibrationAveragingAuto(string, RFmxNRMXChpNoiseCalibrationAveragingAuto) method to False. |
| SetNoiseCalibrationMode(string, RFmxNRMXChpNoiseCalibrationMode) | Sets whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| SetNoiseCompensationEnabled(string, RFmxNRMXChpNoiseCompensationEnabled) | Sets whether RFmx compensates for the instrument noise when performing the measurement. To compensate for instrument noise when performing a CHP measurement, set the SetNoiseCalibrationMode(string, RFmxNRMXChpNoiseCalibrationMode) method to Auto, or set the CHP Noise Cal Mode method to Manual and the SetMeasurementMode(string, RFmxNRMXChpMeasurementMode) method to Measure. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| SetNoiseCompensationType(string, RFmxNRMXChpNoiseCompensationType) | Sets the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| SetNumberOfAnalysisThreads(string, int) | Sets the maximum number of threads used for parallelism for the CHP measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| SetRbwFilterAutoBandwidth(string, RFmxNRMXChpRbwAutoBandwidth) | Sets whether the measurement computes the RBW. |
| SetRbwFilterBandwidth(string, double) | Sets the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(string, RFmxNRMXChpRbwAutoBandwidth) method to False. This value is expressed in Hz. |
| SetRbwFilterType(string, RFmxNRMXChpRbwFilterType) | Sets the shape of the digital RBW filter. |
| SetSweepTimeAuto(string, RFmxNRMXChpSweepTimeAuto) | Sets whether the measurement sets the sweep time. |
| SetSweepTimeInterval(string, double) | Sets the sweep time when you set the SetSweepTimeAuto(string, RFmxNRMXChpSweepTimeAuto) method to False. This value is expressed in seconds. |
| ValidateNoiseCalibrationData(string, out RFmxNRMXChpNoiseCalibrationDataValid) | Indicates whether the CHP noise calibration data is valid for the configuration specified by the signal name in the selectorString parameter. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxchpresults-fetchsubblockpower__string-double-out.html language=enus -->
## TOPIC 00105: FetchSubblockPower(string, double, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxchpresults-fetchsubblockpower__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxchpresults-fetchsubblockpower__string-double-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power of subblock. Use "subblock(n)" as the selector string to read results from this method. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int FetchSubblockPower(string selectorString, double timeout, out double subblockPower)ParametersNameTypeDescriptionselectorStringstringSpeci

### FetchSubblockPower(string, double, out double)

Returns the power of subblock. 
 Use "subblock(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int FetchSubblockPower(string selectorString, double timeout, out double subblockPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and subblock number. If you do not specify the result name, the default result instance is used. Example:"subblock0""result::r1/subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| subblockPower | out double | Upon return, contains the sum of powers of all the frequency bins over the integration bandwidth of the subblock. This includes the power in inter-carrier gaps within a subblock. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXChpResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getcoresetresourceblockoffset__string-out.html language=enus -->
## TOPIC 00106: GetCoresetResourceBlockOffset(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getcoresetresourceblockoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getcoresetresourceblockoffset__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the starting resource block of a CORESET cluster. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetCoresetResourceBlockOffset(string selectorString, out int value)RemarksThis method gets the value of CoresetResourceBlockOffset attribute.Valid values should be a multiple of 6. The def

### GetCoresetResourceBlockOffset(string, out int)

Gets the starting resource block of a CORESET cluster.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetCoresetResourceBlockOffset(string selectorString, out int value)

#### Remarks

This method gets the value of [CoresetResourceBlockOffset](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.Valid values should be a multiple of 6. The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, coreset number and coresetcluster number. Example: "coresetcluster0" or "coreset0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/coreset0/coresetcluster0". You can use the BuildCoresetClusterString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the starting resource block of a CORESET cluster. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getdownlinktestmodel__string-out.html language=enus -->
## TOPIC 00107: GetDownlinkTestModel(string, out RFmxNRMXDownlinkTestModel)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getdownlinktestmodel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getdownlinktestmodel__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the NR test model type when you set the Channel Configuration Mode method to Test Model. Refer to section 4.9.2 of the 3GPP 38.141 specification for more information regarding test model configurations. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetDownlinkTestModel(string selecto

### GetDownlinkTestModel(string, out RFmxNRMXDownlinkTestModel)

Gets the NR test model type when you set the Channel Configuration Mode method to Test Model. Refer to section 4.9.2 of the *3GPP 38.141* specification for more information regarding test model configurations.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetDownlinkTestModel(string selectorString, out RFmxNRMXDownlinkTestModel value)

#### Remarks

This method gets the value of [DownlinkTestModel](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is TM1.1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out RFmxNRMXDownlinkTestModel | Upon return, contains the NR test model type when you set the Channel Configuration Mode method to Test Model. Refer to section 4.9.2 of the 3GPP 38.141 specification for more information regarding test model configurations. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getdownlinktestmodelmodulationtype__string-out.html language=enus -->
## TOPIC 00108: GetDownlinkTestModelModulationType(string, out RFmxNRMXDownlinkTestModelModulationType)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getdownlinktestmodelmodulationtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getdownlinktestmodelmodulationtype__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the modulation type to be used with the selected test model. Selecting the modulation type is supported only for test models NR-FR2-TM3.1 and NR-FR2-TM2. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetDownlinkTestModelModulationType(string selectorString, out RFmxNRMXDownlinkTestMo

### GetDownlinkTestModelModulationType(string, out RFmxNRMXDownlinkTestModelModulationType)

Gets the modulation type to be used with the selected test model. Selecting the modulation type is supported only for test models *NR-FR2-TM3.1* and *NR-FR2-TM2*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetDownlinkTestModelModulationType(string selectorString, out RFmxNRMXDownlinkTestModelModulationType value)

#### Remarks

This method gets the value of [DownlinkTestModelModulationType](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Standard](nationalinstruments-rfmx-nrmx-rfmxnrmxdownlinktestmodelmodulationtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out RFmxNRMXDownlinkTestModelModulationType | Upon return, contains the modulation type to be used with the selected test model. Selecting the modulation type is supported only for test models NR-FR2-TM3.1 and NR-FR2-TM2. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getepreratioport__string-out.html language=enus -->
## TOPIC 00109: GetEpreRatioPort(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getepreratioport__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getepreratioport__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the EPRE Ratio Port used to determine the PDSCH PT-RS RE power scaling as defined in the Table 4.1-2 of 3GPP TS 38.214 specification when you set the PDSCH PTRS Power Mode method to Standard. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetEpreRatioPort(string selectorString, out in

### GetEpreRatioPort(string, out int)

Gets the EPRE Ratio Port used to determine the PDSCH PT-RS RE power scaling as defined in the Table 4.1-2 of *3GPP TS 38.214* specification when you set the PDSCH PTRS Power Mode method to Standard.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetEpreRatioPort(string selectorString, out int value)

#### Remarks

This method gets the value of [EpreRatioPort](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the EPRE Ratio Port used to determine the PDSCH PT-RS RE power scaling as defined in the Table 4.1-2 of 3GPP TS 38.214 specification when you set the PDSCH PTRS Power Mode method to Standard. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getgridsize__string-out.html language=enus -->
## TOPIC 00110: GetGridSize(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getgridsize__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getgridsize__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the reference resource grid size when you set the SetGridSizeMode(string, RFmxNRMXGridSizeMode) method to Manual. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetGridSize(string selectorString, out int value)RemarksThis method gets the value of GridSize attribute.ParametersNameTypeD

### GetGridSize(string, out int)

Gets the reference resource grid size when you set the [SetGridSizeMode(string, RFmxNRMXGridSizeMode)](nationalinstruments-rfmx-nrmx-rfmxnrmx-setgridsizemode__string-rfmxnrmxgridsizemode.html) method to [Manual](nationalinstruments-rfmx-nrmx-rfmxnrmxgridsizemode.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetGridSize(string selectorString, out int value)

#### Remarks

This method gets the value of [GridSize](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number, subblock number and bwp number. Example: "carrier0" or "subblock0" or "bwp0" or "subblock0/carrier0/bwp0". You can use the BuildBandwidthPartString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the reference resource grid size when you set the SetGridSizeMode(string, RFmxNRMXGridSizeMode) method to Manual. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getgridstart__string-out.html language=enus -->
## TOPIC 00111: GetGridStart(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getgridstart__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getgridstart__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the resource grid start relative to Reference Point A in terms of resource block offset when you set the Reference Grid Alignment Mode method to Manual. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetGridStart(string selectorString, out int value)RemarksThis method gets the value o

### GetGridStart(string, out int)

Gets the resource grid start relative to Reference Point A in terms of resource block offset when you set the Reference Grid Alignment Mode method to Manual.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetGridStart(string selectorString, out int value)

#### Remarks

This method gets the value of [GridStart](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number, subblock number and bwp number. Example: "carrier0" or "subblock0" or "bwp0" or "subblock0/carrier0/bwp0". You can use the BuildBandwidthPartString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the resource grid start relative to Reference Point A in terms of resource block offset when you set the Reference Grid Alignment Mode method to Manual. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getnumberofbandwidthparts__string-out.html language=enus -->
## TOPIC 00112: GetNumberOfBandwidthParts(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getnumberofbandwidthparts__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getnumberofbandwidthparts__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of bandwidth parts present in the component carrier. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetNumberOfBandwidthParts(string selectorString, out int value)RemarksThis method gets the value of NumberOfBandwidthParts attribute.The default value is 1.ParametersNameType

### GetNumberOfBandwidthParts(string, out int)

Gets the number of bandwidth parts present in the component carrier.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetNumberOfBandwidthParts(string selectorString, out int value)

#### Remarks

This method gets the value of [NumberOfBandwidthParts](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the number of bandwidth parts present in the component carrier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getnumberofcomponentcarriers__string-out.html language=enus -->
## TOPIC 00113: GetNumberOfComponentCarriers(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getnumberofcomponentcarriers__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getnumberofcomponentcarriers__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of component carriers configured within a subblock. Set this method to 1 for single carrier. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetNumberOfComponentCarriers(string selectorString, out int value)RemarksThis method gets the value of NumberOfComponentCarriers attri

### GetNumberOfComponentCarriers(string, out int)

Gets the number of component carriers configured within a subblock. Set this method to 1 for single carrier.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetNumberOfComponentCarriers(string selectorString, out int value)

#### Remarks

This method gets the value of [NumberOfComponentCarriers](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the number of component carriers configured within a subblock. Set this method to 1 for single carrier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getnumberofpdschconfigurations__string-out.html language=enus -->
## TOPIC 00114: GetNumberOfPdschConfigurations(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getnumberofpdschconfigurations__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getnumberofpdschconfigurations__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of PDSCH slot configurations. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetNumberOfPdschConfigurations(string selectorString, out int value)RemarksThis method gets the value of NumberOfPdschConfigurations attribute.The default value is 1.ParametersNameTypeDescriptionse

### GetNumberOfPdschConfigurations(string, out int)

Gets the number of PDSCH slot configurations.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetNumberOfPdschConfigurations(string selectorString, out int value)

#### Remarks

This method gets the value of [NumberOfPdschConfigurations](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number and user number. Example: "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0". You can use the BuildUserString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the number of PDSCH slot configurations. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdcchslotallocation__string-out.html language=enus -->
## TOPIC 00115: GetPdcchSlotAllocation(string, out string)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdcchslotallocation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdcchslotallocation__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the slot allocation in NR frame. This defines the indices of the allocated slots. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPdcchSlotAllocation(string selectorString, out string value)RemarksThis method gets the value of PdcchSlotAllocation attribute.The default value is 0-las

### GetPdcchSlotAllocation(string, out string)

Gets the slot allocation in NR frame. This defines the indices of the allocated slots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPdcchSlotAllocation(string selectorString, out string value)

#### Remarks

This method gets the value of [PdcchSlotAllocation](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0-last. Valid values are between 0 and (Maximum Slots in Frame - 1).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, coreset number and pdcch number. Example: "pdcch0" or "coreset0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/coreset0/pdcch0". You can use the BuildPdcchString(string, int) method to build the selector string. |
| value | out string | Upon return, contains the slot allocation in NR frame. This defines the indices of the allocated slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrsantennaports__string-out.html language=enus -->
## TOPIC 00116: GetPdschDmrsAntennaPorts(string, out string)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrsantennaports__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrsantennaports__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the antenna ports used for DMRS transmission. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPdschDmrsAntennaPorts(string selectorString, out string value)RemarksThis method gets the value of PdschDmrsAntennaPorts attribute.The default value is 1000.ParametersNameTypeDescriptionsel

### GetPdschDmrsAntennaPorts(string, out string)

Gets the antenna ports used for DMRS transmission.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPdschDmrsAntennaPorts(string selectorString, out string value)

#### Remarks

This method gets the value of [PdschDmrsAntennaPorts](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 1000.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | out string | Upon return, contains the antenna ports used for DMRS transmission. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrsconfigurationtype__string-out.html language=enus -->
## TOPIC 00117: GetPdschDmrsConfigurationType(string, out RFmxNRMXPdschDmrsConfigurationType)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrsconfigurationtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrsconfigurationtype__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the configuration type of DMRS. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPdschDmrsConfigurationType(string selectorString, out RFmxNRMXPdschDmrsConfigurationType value)RemarksThis method gets the value of PdschDmrsConfigurationType attribute.The default value is Type1.Paramet

### GetPdschDmrsConfigurationType(string, out RFmxNRMXPdschDmrsConfigurationType)

Gets the configuration type of DMRS.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPdschDmrsConfigurationType(string selectorString, out RFmxNRMXPdschDmrsConfigurationType value)

#### Remarks

This method gets the value of [PdschDmrsConfigurationType](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Type1](nationalinstruments-rfmx-nrmx-rfmxnrmxpdschdmrsconfigurationtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | out RFmxNRMXPdschDmrsConfigurationType | Upon return, contains the configuration type of DMRS. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrsduration__string-out.html language=enus -->
## TOPIC 00118: GetPdschDmrsDuration(string, out RFmxNRMXPdschDmrsDuration)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrsduration__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrsduration__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the DMRS is single-symbol or double-symbol. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPdschDmrsDuration(string selectorString, out RFmxNRMXPdschDmrsDuration value)RemarksThis method gets the value of PdschDmrsDuration attribute.The default value is Single-Symbol.Parame

### GetPdschDmrsDuration(string, out RFmxNRMXPdschDmrsDuration)

Gets whether the DMRS is single-symbol or double-symbol.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPdschDmrsDuration(string selectorString, out RFmxNRMXPdschDmrsDuration value)

#### Remarks

This method gets the value of [PdschDmrsDuration](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is Single-Symbol.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | out RFmxNRMXPdschDmrsDuration | Upon return, contains whether the DMRS is single-symbol or double-symbol. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrsnscid__string-out.html language=enus -->
## TOPIC 00119: GetPdschDmrsnScid(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrsnscid__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrsnscid__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of PDSCH DMRS nSCID used for reference signal generation. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPdschDmrsnScid(string selectorString, out int value)RemarksThis method gets the value of PdschDmrsnScid attribute.The default value is 0.ParametersNameTypeDescriptions

### GetPdschDmrsnScid(string, out int)

Gets the value of PDSCH DMRS nSCID used for reference signal generation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPdschDmrsnScid(string selectorString, out int value)

#### Remarks

This method gets the value of [PdschDmrsnScid](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the value of PDSCH DMRS nSCID used for reference signal generation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrsnumberofcdmgroups__string-out.html language=enus -->
## TOPIC 00120: GetPdschDmrsNumberOfCdmGroups(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrsnumberofcdmgroups__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrsnumberofcdmgroups__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of CDM groups. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPdschDmrsNumberOfCdmGroups(string selectorString, out int value)RemarksThis method gets the value of PdschDmrsNumberOfCdmGroups attribute.The default value is 1.ParametersNameTypeDescriptionselectorStringstrin

### GetPdschDmrsNumberOfCdmGroups(string, out int)

Gets the number of CDM groups.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPdschDmrsNumberOfCdmGroups(string selectorString, out int value)

#### Remarks

This method gets the value of [PdschDmrsNumberOfCdmGroups](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the number of CDM groups. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrspower__string-out.html language=enus -->
## TOPIC 00121: GetPdschDmrsPower(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrspower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrspower__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the factor by which the PDSCH DMRS REs are boosted. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPdschDmrsPower(string selectorString, out double value)RemarksThis method gets the value of PdschDmrsPower attribute.The default value is 0.ParametersNa

### GetPdschDmrsPower(string, out double)

Gets the factor by which the PDSCH DMRS REs are boosted. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPdschDmrsPower(string selectorString, out double value)

#### Remarks

This method gets the value of [PdschDmrsPower](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the factor by which the PDSCH DMRS REs are boosted. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrspowermode__string-out.html language=enus -->
## TOPIC 00122: GetPdschDmrsPowerMode(string, out RFmxNRMXPdschDmrsPowerMode)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrspowermode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrspowermode__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the configured SetPdschDmrsPower(string, double) is calculated based on the SetPdschDmrsNumberOfCdmGroups(string, int) or specified by you. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPdschDmrsPowerMode(string selectorString, out RFmxNRMXPdschDmrsPowerMode value)RemarksT

### GetPdschDmrsPowerMode(string, out RFmxNRMXPdschDmrsPowerMode)

Gets whether the configured [SetPdschDmrsPower(string, double)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdschdmrspower__string-double.html) is calculated based on the [SetPdschDmrsNumberOfCdmGroups(string, int)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdschdmrsnumberofcdmgroups__string-int.html) or specified by you.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPdschDmrsPowerMode(string selectorString, out RFmxNRMXPdschDmrsPowerMode value)

#### Remarks

This method gets the value of [PdschDmrsPowerMode](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [CdmGroups](nationalinstruments-rfmx-nrmx-rfmxnrmxpdschdmrspowermode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | out RFmxNRMXPdschDmrsPowerMode | Upon return, contains whether the configured SetPdschDmrsPower(string, double) is calculated based on the SetPdschDmrsNumberOfCdmGroups(string, int) or specified by you. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrsreleaseversion__string-out.html language=enus -->
## TOPIC 00123: GetPdschDmrsReleaseVersion(string, out RFmxNRMXPdschDmrsReleaseVersion)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrsreleaseversion__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrsreleaseversion__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the 3GGP release version for PDSCH DMRS. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPdschDmrsReleaseVersion(string selectorString, out RFmxNRMXPdschDmrsReleaseVersion value)RemarksThis method gets the value of PdschDmrsReleaseVersion attribute.The default value is 0.ParametersN

### GetPdschDmrsReleaseVersion(string, out RFmxNRMXPdschDmrsReleaseVersion)

Gets the 3GGP release version for PDSCH DMRS.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPdschDmrsReleaseVersion(string selectorString, out RFmxNRMXPdschDmrsReleaseVersion value)

#### Remarks

This method gets the value of [PdschDmrsReleaseVersion](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | out RFmxNRMXPdschDmrsReleaseVersion | Upon return, contains the 3GGP release version for PDSCH DMRS. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrsscramblingid__string-out.html language=enus -->
## TOPIC 00124: GetPdschDmrsScramblingID(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrsscramblingid__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrsscramblingid__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of scrambling ID used for reference signal generation. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPdschDmrsScramblingID(string selectorString, out int value)RemarksThis method gets the value of PdschDmrsScramblingID attribute.The default value is 0.ParametersNameTypeD

### GetPdschDmrsScramblingID(string, out int)

Gets the value of scrambling ID used for reference signal generation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPdschDmrsScramblingID(string selectorString, out int value)

#### Remarks

This method gets the value of [PdschDmrsScramblingID](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the value of scrambling ID used for reference signal generation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrsscramblingidmode__string-out.html language=enus -->
## TOPIC 00125: GetPdschDmrsScramblingIDMode(string, out RFmxNRMXPdschDmrsScramblingIDMode)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrsscramblingidmode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrsscramblingidmode__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the configured Scrambling ID is based on SetCellID(string, int) or specified by you. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPdschDmrsScramblingIDMode(string selectorString, out RFmxNRMXPdschDmrsScramblingIDMode value)RemarksThis method gets the value of PdschDmrsScr

### GetPdschDmrsScramblingIDMode(string, out RFmxNRMXPdschDmrsScramblingIDMode)

Gets whether the configured Scrambling ID is based on [SetCellID(string, int)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setcellid__string-int.html) or specified by you.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPdschDmrsScramblingIDMode(string selectorString, out RFmxNRMXPdschDmrsScramblingIDMode value)

#### Remarks

This method gets the value of [PdschDmrsScramblingIDMode](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [CellID](nationalinstruments-rfmx-nrmx-rfmxnrmxpdschdmrsscramblingidmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | out RFmxNRMXPdschDmrsScramblingIDMode | Upon return, contains whether the configured Scrambling ID is based on SetCellID(string, int) or specified by you. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrstypeaposition__string-out.html language=enus -->
## TOPIC 00126: GetPdschDmrsTypeAPosition(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrstypeaposition__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschdmrstypeaposition__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the position of first DMRS symbol in a slot for Type A configurations. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPdschDmrsTypeAPosition(string selectorString, out int value)RemarksThis method gets the value of PdschDmrsTypeAPosition attribute.The default value is 2.ParametersN

### GetPdschDmrsTypeAPosition(string, out int)

Gets the position of first DMRS symbol in a slot for Type A configurations.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPdschDmrsTypeAPosition(string selectorString, out int value)

#### Remarks

This method gets the value of [PdschDmrsTypeAPosition](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 2.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the position of first DMRS symbol in a slot for Type A configurations. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschmappingtype__string-out.html language=enus -->
## TOPIC 00127: GetPdschMappingType(string, out RFmxNRMXPdschMappingType)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschmappingtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschmappingtype__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mapping type of DMRS. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPdschMappingType(string selectorString, out RFmxNRMXPdschMappingType value)RemarksThis method gets the value of PdschMappingType attribute.The default value is TypeA.ParametersNameTypeDescriptionselectorString

### GetPdschMappingType(string, out RFmxNRMXPdschMappingType)

Gets the mapping type of DMRS.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPdschMappingType(string selectorString, out RFmxNRMXPdschMappingType value)

#### Remarks

This method gets the value of [PdschMappingType](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [TypeA](nationalinstruments-rfmx-nrmx-rfmxnrmxpdschmappingtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | out RFmxNRMXPdschMappingType | Upon return, contains the mapping type of DMRS. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschmodulationtype__string-out.html language=enus -->
## TOPIC 00128: GetPdschModulationType(string, out RFmxNRMXPdschModulationType)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschmodulationtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschmodulationtype__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the modulation scheme used in PDSCH channel of the signal being measured. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPdschModulationType(string selectorString, out RFmxNRMXPdschModulationType value)RemarksThis method gets the value of PdschModulationType attribute.The default v

### GetPdschModulationType(string, out RFmxNRMXPdschModulationType)

Gets the modulation scheme used in PDSCH channel of the signal being measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPdschModulationType(string selectorString, out RFmxNRMXPdschModulationType value)

#### Remarks

This method gets the value of [PdschModulationType](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Qpsk](nationalinstruments-rfmx-nrmx-rfmxnrmxpdschmodulationtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | out RFmxNRMXPdschModulationType | Upon return, contains the modulation scheme used in PDSCH channel of the signal being measured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschnumberofresourceblockclusters__string-out.html language=enus -->
## TOPIC 00129: GetPdschNumberOfResourceBlockClusters(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschnumberofresourceblockclusters__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschnumberofresourceblockclusters__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of clusters of resource allocations with each cluster including one or more consecutive resource blocks. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPdschNumberOfResourceBlockClusters(string selectorString, out int value)RemarksThis method gets the value of PdschNumbe

### GetPdschNumberOfResourceBlockClusters(string, out int)

Gets the number of clusters of resource allocations with each cluster including one or more consecutive resource blocks.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPdschNumberOfResourceBlockClusters(string selectorString, out int value)

#### Remarks

This method gets the value of [PdschNumberOfResourceBlockClusters](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the number of clusters of resource allocations with each cluster including one or more consecutive resource blocks. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschnumberofresourceblocks__string-out.html language=enus -->
## TOPIC 00130: GetPdschNumberOfResourceBlocks(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschnumberofresourceblocks__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschnumberofresourceblocks__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of consecutive resource blocks in a PDSCH cluster. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPdschNumberOfResourceBlocks(string selectorString, out int value)RemarksThis method gets the value of PdschNumberOfResourceBlocks attribute.The default value is -1. If you s

### GetPdschNumberOfResourceBlocks(string, out int)

Gets the number of consecutive resource blocks in a PDSCH cluster.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPdschNumberOfResourceBlocks(string selectorString, out int value)

#### Remarks

This method gets the value of [PdschNumberOfResourceBlocks](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is -1. If you set this property to -1, all available resource blocks within the bandwidth part are configured.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number, pdsch number and pdschcluster number. Example: "pdschcluster0" or "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0/pdschcluster0". You can use the BuildPdschClusterString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the number of consecutive resource blocks in a PDSCH cluster. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschptrsantennaports__string-out.html language=enus -->
## TOPIC 00131: GetPdschPtrsAntennaPorts(string, out string)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschptrsantennaports__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschptrsantennaports__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DMRS Antenna Ports associated with PTRS transmission. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPdschPtrsAntennaPorts(string selectorString, out string value)RemarksThis method gets the value of PdschPtrsAntennaPorts attribute.The default value is 0.ParametersNameTypeDescr

### GetPdschPtrsAntennaPorts(string, out string)

Gets the DMRS Antenna Ports associated with PTRS transmission.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPdschPtrsAntennaPorts(string selectorString, out string value)

#### Remarks

This method gets the value of [PdschPtrsAntennaPorts](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | out string | Upon return, contains the DMRS Antenna Ports associated with PTRS transmission. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschptrsenabled__string-out.html language=enus -->
## TOPIC 00132: GetPdschPtrsEnabled(string, out RFmxNRMXPdschPtrsEnabled)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschptrsenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschptrsenabled__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether PT-RS is present in the transmitted signal. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPdschPtrsEnabled(string selectorString, out RFmxNRMXPdschPtrsEnabled value)RemarksThis method gets the value of PdschPtrsEnabled attribute.The default value is False.ParametersNameTyp

### GetPdschPtrsEnabled(string, out RFmxNRMXPdschPtrsEnabled)

Gets whether PT-RS is present in the transmitted signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPdschPtrsEnabled(string selectorString, out RFmxNRMXPdschPtrsEnabled value)

#### Remarks

This method gets the value of [PdschPtrsEnabled](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-nrmx-rfmxnrmxpdschptrsenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | out RFmxNRMXPdschPtrsEnabled | Upon return, contains whether PT-RS is present in the transmitted signal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschptrsfrequencydensity__string-out.html language=enus -->
## TOPIC 00133: GetPdschPtrsFrequencyDensity(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschptrsfrequencydensity__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschptrsfrequencydensity__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the density of PTRS in frequency domain. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPdschPtrsFrequencyDensity(string selectorString, out int value)RemarksThis method gets the value of PdschPtrsFrequencyDensity attribute.The default value is 2.ParametersNameTypeDescriptionselect

### GetPdschPtrsFrequencyDensity(string, out int)

Gets the density of PTRS in frequency domain.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPdschPtrsFrequencyDensity(string selectorString, out int value)

#### Remarks

This method gets the value of [PdschPtrsFrequencyDensity](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 2.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the density of PTRS in frequency domain |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschptrspower__string-out.html language=enus -->
## TOPIC 00134: GetPdschPtrsPower(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschptrspower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschptrspower__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the factor by which the PDSCH PTRS REs are boosted, compared to PDSCH REs. This value is expressed in dB. The value of this method is taken as an input when you set the SetPdschPtrsPowerMode(string, RFmxNRMXPdschPtrsPowerMode) method to UserDefined. If you set the PDSCH PTRS Pwr Mode method to

### GetPdschPtrsPower(string, out double)

Gets the factor by which the PDSCH PTRS REs are boosted, compared to PDSCH REs. This value is expressed in dB. The value of this method is taken as an input when you set the [SetPdschPtrsPowerMode(string, RFmxNRMXPdschPtrsPowerMode)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdschptrspowermode__string-rfmxnrmxpdschptrspowermode.html) method to [UserDefined](nationalinstruments-rfmx-nrmx-rfmxnrmxpdschptrspowermode.html). If you set the PDSCH PTRS Pwr Mode method to [Standard](nationalinstruments-rfmx-nrmx-rfmxnrmxpdschptrspowermode.html), the value is computed from other parameters.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPdschPtrsPower(string selectorString, out double value)

#### Remarks

This method gets the value of [PdschPtrsPower](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the factor by which the PDSCH PTRS REs are boosted, compared to PDSCH REs. This value is expressed in dB. The value of this method is taken as an input when you set the SetPdschPtrsPowerMode(string, RFmxNRMXPdschPtrsPowerMode) method to UserDefined. If you set the PDSCH PTRS Pwr Mode method to Standard, the value is computed from other parameters. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschptrspowermode__string-out.html language=enus -->
## TOPIC 00135: GetPdschPtrsPowerMode(string, out RFmxNRMXPdschPtrsPowerMode)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschptrspowermode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschptrspowermode__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the configured SetPdschPtrsPower(string, double) is calculated as defined in 3GPP specification or configured by you. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPdschPtrsPowerMode(string selectorString, out RFmxNRMXPdschPtrsPowerMode value)RemarksThis method gets the va

### GetPdschPtrsPowerMode(string, out RFmxNRMXPdschPtrsPowerMode)

Gets whether the configured [SetPdschPtrsPower(string, double)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdschptrspower__string-double.html) is calculated as defined in 3GPP specification or configured by you.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPdschPtrsPowerMode(string selectorString, out RFmxNRMXPdschPtrsPowerMode value)

#### Remarks

This method gets the value of [PdschPtrsPowerMode](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Standard](nationalinstruments-rfmx-nrmx-rfmxnrmxpdschptrspowermode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | out RFmxNRMXPdschPtrsPowerMode | Upon return, contains whether the configured SetPdschPtrsPower(string, double) is calculated as defined in 3GPP specification or configured by you. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschptrsreoffset__string-out.html language=enus -->
## TOPIC 00136: GetPdschPtrsREOffset(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschptrsreoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschptrsreoffset__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RE Offset to be used for transmission of PTRS as defined in Table 7.4.1.2.2-1 of 3GPP 38.211 specification. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPdschPtrsREOffset(string selectorString, out int value)RemarksThis method gets the value of PdschPtrsREOffset attribute.The

### GetPdschPtrsREOffset(string, out int)

Gets the RE Offset to be used for transmission of PTRS as defined in Table 7.4.1.2.2-1 of *3GPP 38.211* specification.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPdschPtrsREOffset(string selectorString, out int value)

#### Remarks

This method gets the value of [PdschPtrsREOffset](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 00.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the RE Offset to be used for transmission of PTRS as defined in Table 7.4.1.2.2-1 of 3GPP 38.211 specification. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschptrstimedensity__string-out.html language=enus -->
## TOPIC 00137: GetPdschPtrsTimeDensity(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschptrstimedensity__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschptrstimedensity__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the density of PTRS in time domain. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPdschPtrsTimeDensity(string selectorString, out int value)RemarksThis method gets the value of PdschPtrsTimeDensity attribute.The default value is 1.ParametersNameTypeDescriptionselectorStringstringS

### GetPdschPtrsTimeDensity(string, out int)

Gets the density of PTRS in time domain.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPdschPtrsTimeDensity(string selectorString, out int value)

#### Remarks

This method gets the value of [PdschPtrsTimeDensity](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the density of PTRS in time domain |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschresourceblockoffset__string-out.html language=enus -->
## TOPIC 00138: GetPdschResourceBlockOffset(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschresourceblockoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschresourceblockoffset__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the starting resource block number of a PDSCH cluster. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPdschResourceBlockOffset(string selectorString, out int value)RemarksThis method gets the value of PdschResourceBlockOffset attribute.The default value is 0.ParametersNameTypeDescr

### GetPdschResourceBlockOffset(string, out int)

Gets the starting resource block number of a PDSCH cluster.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPdschResourceBlockOffset(string selectorString, out int value)

#### Remarks

This method gets the value of [PdschResourceBlockOffset](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number, pdsch number and pdschcluster number. Example: "pdschcluster0" or "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0/pdschcluster0". You can use the BuildPdschClusterString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the starting resource block number of a PDSCH cluster. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschslotallocation__string-out.html language=enus -->
## TOPIC 00139: GetPdschSlotAllocation(string, out string)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschslotallocation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschslotallocation__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the slot allocation in NR Frame. This defines the indices of the allocated slots. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPdschSlotAllocation(string selectorString, out string value)RemarksThis method gets the value of PdschSlotAllocation attribute.The default value is 0-Las

### GetPdschSlotAllocation(string, out string)

Gets the slot allocation in NR Frame. This defines the indices of the allocated slots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPdschSlotAllocation(string selectorString, out string value)

#### Remarks

This method gets the value of [PdschSlotAllocation](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0-Last. Valid values are from 0 to (Maximum number of slots in frame - 1), inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | out string | Upon return, contains the slot allocation in NR Frame. This defines the indices of the allocated slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschsymbolallocation__string-out.html language=enus -->
## TOPIC 00140: GetPdschSymbolAllocation(string, out string)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschsymbolallocation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpdschsymbolallocation__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the symbol allocation of each slot allocation. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPdschSymbolAllocation(string selectorString, out string value)RemarksThis method gets the value of PdschSymbolAllocation attribute.The default value is 0-Last. Valid values are from 0 to 1

### GetPdschSymbolAllocation(string, out string)

Gets the symbol allocation of each slot allocation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPdschSymbolAllocation(string selectorString, out string value)

#### Remarks

This method gets the value of [PdschSymbolAllocation](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0-Last. Valid values are from 0 to 13, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | out string | Upon return, contains the symbol allocation of each slot allocation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpsspower__string-out.html language=enus -->
## TOPIC 00141: GetPssPower(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpsspower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpsspower__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power scaling value for the primary synchronization symbol in the SS/PBCH block. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPssPower(string selectorString, out double value)RemarksThis method gets the value of PssPower attribute.The default va

### GetPssPower(string, out double)

Gets the power scaling value for the primary synchronization symbol in the SS/PBCH block. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPssPower(string selectorString, out double value)

#### Remarks

This method gets the value of [PssPower](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power scaling value for the primary synchronization symbol in the SS/PBCH block. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsadditionalpositions__string-out.html language=enus -->
## TOPIC 00142: GetPuschDmrsAdditionalPositions(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsadditionalpositions__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsadditionalpositions__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of additional sets of consecutive DMRS symbols in a slot. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPuschDmrsAdditionalPositions(string selectorString, out int value)RemarksThis method gets the value of PuschDmrsAdditionalPositions attribute.The default value is 0.P

### GetPuschDmrsAdditionalPositions(string, out int)

Gets the number of additional sets of consecutive DMRS symbols in a slot.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPuschDmrsAdditionalPositions(string selectorString, out int value)

#### Remarks

This method gets the value of [PuschDmrsAdditionalPositions](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the number of additional sets of consecutive DMRS symbols in a slot. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsantennaports__string-out.html language=enus -->
## TOPIC 00143: GetPuschDmrsAntennaPorts(string, out string)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsantennaports__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsantennaports__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the antenna ports used for DMRS transmission. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPuschDmrsAntennaPorts(string selectorString, out string value)RemarksThis method gets the value of PuschDmrsAntennaPorts attribute.The default value is 0. Valid values depend on PUSCH Mappi

### GetPuschDmrsAntennaPorts(string, out string)

Gets the antenna ports used for DMRS transmission.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPuschDmrsAntennaPorts(string selectorString, out string value)

#### Remarks

This method gets the value of [PuschDmrsAntennaPorts](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0. Valid values depend on PUSCH Mapping Type and PUSCH DMRS Num CDM Groups properties.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | out string | Upon return, contains the antenna ports used for DMRS transmission. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsconfigurationtype__string-out.html language=enus -->
## TOPIC 00144: GetPuschDmrsConfigurationType(string, out RFmxNRMXPuschDmrsConfigurationType)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsconfigurationtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsconfigurationtype__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the configuration type of DMRS. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPuschDmrsConfigurationType(string selectorString, out RFmxNRMXPuschDmrsConfigurationType value)RemarksThis method gets the value of PuschDmrsConfigurationType attribute.The default value is Type1.Paramet

### GetPuschDmrsConfigurationType(string, out RFmxNRMXPuschDmrsConfigurationType)

Gets the configuration type of DMRS.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPuschDmrsConfigurationType(string selectorString, out RFmxNRMXPuschDmrsConfigurationType value)

#### Remarks

This method gets the value of [PuschDmrsConfigurationType](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Type1](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschdmrsconfigurationtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | out RFmxNRMXPuschDmrsConfigurationType | Upon return, contains the configuration type of DMRS. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsduration__string-out.html language=enus -->
## TOPIC 00145: GetPuschDmrsDuration(string, out RFmxNRMXPuschDmrsDuration)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsduration__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsduration__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the DMRS is single-symbol or double-symbol. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPuschDmrsDuration(string selectorString, out RFmxNRMXPuschDmrsDuration value)RemarksThis method gets the value of PuschDmrsDuration attribute.The default value is Single-Symbol.Parame

### GetPuschDmrsDuration(string, out RFmxNRMXPuschDmrsDuration)

Gets whether the DMRS is single-symbol or double-symbol.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPuschDmrsDuration(string selectorString, out RFmxNRMXPuschDmrsDuration value)

#### Remarks

This method gets the value of [PuschDmrsDuration](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is Single-Symbol.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | out RFmxNRMXPuschDmrsDuration | Upon return, contains whether the DMRS is single-symbol or double-symbol. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsgrouphoppingenabled__string-out.html language=enus -->
## TOPIC 00146: GetPuschDmrsGroupHoppingEnabled(string, out RFmxNRMXPuschDmrsGroupHoppingEnabled)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsgrouphoppingenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsgrouphoppingenabled__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the group hopping is enabled. This method is valid only when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPuschDmrsGroupHoppingEnabled(string selectorString, out

### GetPuschDmrsGroupHoppingEnabled(string, out RFmxNRMXPuschDmrsGroupHoppingEnabled)

Gets whether the group hopping is enabled. This method is valid only when you set the [SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschtransformprecodingenabled__string-rfmxnrmxpuschtransformprecodingenabled.html) method to [True](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschdmrsgrouphoppingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPuschDmrsGroupHoppingEnabled(string selectorString, out RFmxNRMXPuschDmrsGroupHoppingEnabled value)

#### Remarks

This method gets the value of [PuschDmrsGroupHoppingEnabled](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschdmrsgrouphoppingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | out RFmxNRMXPuschDmrsGroupHoppingEnabled | Upon return, contains whether the group hopping is enabled. This method is valid only when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsnscid__string-out.html language=enus -->
## TOPIC 00147: GetPuschDmrsNscid(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsnscid__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsnscid__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of PUSCH DMRS nSCID used for reference signal generation. This method is valid only when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to False. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPuschDmrsNscid(string sel

### GetPuschDmrsNscid(string, out int)

Gets the value of PUSCH DMRS nSCID used for reference signal generation. This method is valid only when you set the [SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschtransformprecodingenabled__string-rfmxnrmxpuschtransformprecodingenabled.html) method to [False](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschtransformprecodingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPuschDmrsNscid(string selectorString, out int value)

#### Remarks

This method gets the value of [PuschDmrsNscid](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the value of PUSCH DMRS nSCID used for reference signal generation. This method is valid only when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsnumberofcdmgroups__string-out.html language=enus -->
## TOPIC 00148: GetPuschDmrsNumberOfCdmGroups(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsnumberofcdmgroups__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsnumberofcdmgroups__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of CDM groups, when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to False, otherwise it is coerced to 2. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPuschDmrsNumberOfCdmGroups(string selectorString, out int value

### GetPuschDmrsNumberOfCdmGroups(string, out int)

Gets the number of CDM groups, when you set the [SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschtransformprecodingenabled__string-rfmxnrmxpuschtransformprecodingenabled.html) method to [False](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschtransformprecodingenabled.html), otherwise it is coerced to 2.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPuschDmrsNumberOfCdmGroups(string selectorString, out int value)

#### Remarks

This method gets the value of [PuschDmrsNumberOfCdmGroups](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the number of CDM groups, when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to False, otherwise it is coerced to 2. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrspower__string-out.html language=enus -->
## TOPIC 00149: GetPuschDmrsPower(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrspower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrspower__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the factor which boosts the PUSCH DMRS REs. This value is expressed in dB. This method is ignored if you set the SetPuschDmrsPowerMode(string, RFmxNRMXPuschDmrsPowerMode) method to CdmGroups. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPuschDmrsPower(string selectorString, out d

### GetPuschDmrsPower(string, out double)

Gets the factor which boosts the PUSCH DMRS REs. This value is expressed in dB. This method is ignored if you set the [SetPuschDmrsPowerMode(string, RFmxNRMXPuschDmrsPowerMode)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschdmrspowermode__string-rfmxnrmxpuschdmrspowermode.html) method to [CdmGroups](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschdmrspowermode.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPuschDmrsPower(string selectorString, out double value)

#### Remarks

This method gets the value of [PuschDmrsPower](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the factor which boosts the PUSCH DMRS REs. This value is expressed in dB. This method is ignored if you set the SetPuschDmrsPowerMode(string, RFmxNRMXPuschDmrsPowerMode) method to CdmGroups. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrspowermode__string-out.html language=enus -->
## TOPIC 00150: GetPuschDmrsPowerMode(string, out RFmxNRMXPuschDmrsPowerMode)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrspowermode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrspowermode__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the value of SetPuschDmrsPower(string, double) method is calculated based on the SetPuschDmrsNumberOfCdmGroups(string, int) method or specified by you. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPuschDmrsPowerMode(string selectorString, out RFmxNRMXPuschDmrsPowerMode va

### GetPuschDmrsPowerMode(string, out RFmxNRMXPuschDmrsPowerMode)

Gets whether the value of [SetPuschDmrsPower(string, double)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschdmrspower__string-double.html) method is calculated based on the [SetPuschDmrsNumberOfCdmGroups(string, int)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschdmrsnumberofcdmgroups__string-int.html) method or specified by you.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPuschDmrsPowerMode(string selectorString, out RFmxNRMXPuschDmrsPowerMode value)

#### Remarks

This method gets the value of [PuschDmrsPowerMode](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [CdmGroups](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschdmrspowermode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | out RFmxNRMXPuschDmrsPowerMode | Upon return, contains whether the value of SetPuschDmrsPower(string, double) method is calculated based on the SetPuschDmrsNumberOfCdmGroups(string, int) method or specified by you. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrspuschid__string-out.html language=enus -->
## TOPIC 00151: GetPuschDmrsPuschID(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrspuschid__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrspuschid__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of PUSCH DMRS PUSCH ID used for reference signal generation. This method is valid only when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to True and SetPuschDmrsPuschIDMode(string, RFmxNRMXPuschDmrsPuschIDMode) method to UserDefi

### GetPuschDmrsPuschID(string, out int)

Gets the value of PUSCH DMRS PUSCH ID used for reference signal generation. This method is valid only when you set the [SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschtransformprecodingenabled__string-rfmxnrmxpuschtransformprecodingenabled.html) method to [True](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschtransformprecodingenabled.html) and [SetPuschDmrsPuschIDMode(string, RFmxNRMXPuschDmrsPuschIDMode)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschdmrspuschidmode__string-rfmxnrmxpuschdmrspuschidmode.html) method to [UserDefined](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschdmrspuschidmode.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPuschDmrsPuschID(string selectorString, out int value)

#### Remarks

This method gets the value of [PuschDmrsPuschID](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0. Valid values are from 0 to 1007, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the value of PUSCH DMRS PUSCH ID used for reference signal generation. This method is valid only when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to True and SetPuschDmrsPuschIDMode(string, RFmxNRMXPuschDmrsPuschIDMode) method to UserDefined. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrspuschidmode__string-out.html language=enus -->
## TOPIC 00152: GetPuschDmrsPuschIDMode(string, out RFmxNRMXPuschDmrsPuschIDMode)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrspuschidmode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrspuschidmode__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether PUSCH DMRS PUSCH ID is based on SetCellID(string, int) or specified by you. This method is valid only when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPuschDmrsP

### GetPuschDmrsPuschIDMode(string, out RFmxNRMXPuschDmrsPuschIDMode)

Gets whether PUSCH DMRS PUSCH ID is based on [SetCellID(string, int)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setcellid__string-int.html) or specified by you. This method is valid only when you set the [SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschtransformprecodingenabled__string-rfmxnrmxpuschtransformprecodingenabled.html) method to [True](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschtransformprecodingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPuschDmrsPuschIDMode(string selectorString, out RFmxNRMXPuschDmrsPuschIDMode value)

#### Remarks

This method gets the value of [PuschDmrsPuschIDMode](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [CellID](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschdmrspuschidmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | out RFmxNRMXPuschDmrsPuschIDMode | Upon return, contains whether PUSCH DMRS PUSCH ID is based on SetCellID(string, int) or specified by you. This method is valid only when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsreleaseversion__string-out.html language=enus -->
## TOPIC 00153: GetPuschDmrsReleaseVersion(string, out RFmxNRMXPuschDmrsReleaseVersion)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsreleaseversion__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsreleaseversion__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the 3GGP release version for PUSCH DMRS. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPuschDmrsReleaseVersion(string selectorString, out RFmxNRMXPuschDmrsReleaseVersion value)RemarksThis method gets the value of PuschDmrsReleaseVersion attribute.The default value is 0.ParametersN

### GetPuschDmrsReleaseVersion(string, out RFmxNRMXPuschDmrsReleaseVersion)

Gets the 3GGP release version for PUSCH DMRS.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPuschDmrsReleaseVersion(string selectorString, out RFmxNRMXPuschDmrsReleaseVersion value)

#### Remarks

This method gets the value of [PuschDmrsReleaseVersion](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | out RFmxNRMXPuschDmrsReleaseVersion | Upon return, contains the 3GGP release version for PUSCH DMRS. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsscramblingid__string-out.html language=enus -->
## TOPIC 00154: GetPuschDmrsScramblingID(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsscramblingid__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsscramblingid__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of scrambling ID. This method is valid only when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to False. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPuschDmrsScramblingID(string selectorString, out int value)Remark

### GetPuschDmrsScramblingID(string, out int)

Gets the value of scrambling ID. This method is valid only when you set the [SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschtransformprecodingenabled__string-rfmxnrmxpuschtransformprecodingenabled.html) method to [False](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschtransformprecodingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPuschDmrsScramblingID(string selectorString, out int value)

#### Remarks

This method gets the value of [PuschDmrsScramblingID](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0. Valid values are from 0 to 65535, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the value of scrambling ID. This method is valid only when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsscramblingidmode__string-out.html language=enus -->
## TOPIC 00155: GetPuschDmrsScramblingIDMode(string, out RFmxNRMXPuschDmrsScramblingIDMode)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsscramblingidmode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrsscramblingidmode__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the configured Scrambling ID is honored or the Cell ID is used for reference signal generation. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPuschDmrsScramblingIDMode(string selectorString, out RFmxNRMXPuschDmrsScramblingIDMode value)RemarksThis method gets the value of P

### GetPuschDmrsScramblingIDMode(string, out RFmxNRMXPuschDmrsScramblingIDMode)

Gets whether the configured Scrambling ID is honored or the Cell ID is used for reference signal generation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPuschDmrsScramblingIDMode(string selectorString, out RFmxNRMXPuschDmrsScramblingIDMode value)

#### Remarks

This method gets the value of [PuschDmrsScramblingIDMode](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [CellID](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschdmrsscramblingidmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | out RFmxNRMXPuschDmrsScramblingIDMode | Upon return, contains whether the configured Scrambling ID is honored or the Cell ID is used for reference signal generation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrssequencehoppingenabled__string-out.html language=enus -->
## TOPIC 00156: GetPuschDmrsSequenceHoppingEnabled(string, out RFmxNRMXPuschDmrsSequenceHoppingEnabled)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrssequencehoppingenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrssequencehoppingenabled__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the sequence hopping is enabled. This method is valid only when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPuschDmrsSequenceHoppingEnabled(string selectorString

### GetPuschDmrsSequenceHoppingEnabled(string, out RFmxNRMXPuschDmrsSequenceHoppingEnabled)

Gets whether the sequence hopping is enabled. This method is valid only when you set the [SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschtransformprecodingenabled__string-rfmxnrmxpuschtransformprecodingenabled.html) method to [True](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschdmrssequencehoppingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPuschDmrsSequenceHoppingEnabled(string selectorString, out RFmxNRMXPuschDmrsSequenceHoppingEnabled value)

#### Remarks

This method gets the value of [PuschDmrsSequenceHoppingEnabled](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschdmrssequencehoppingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | out RFmxNRMXPuschDmrsSequenceHoppingEnabled | Upon return, contains whether the sequence hopping is enabled. This method is valid only when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrstypeaposition__string-out.html language=enus -->
## TOPIC 00157: GetPuschDmrsTypeAPosition(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrstypeaposition__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschdmrstypeaposition__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the position of first DMRS symbol in a slot when you set the SetPuschMappingType(string, RFmxNRMXPuschMappingType) method to TypeA. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPuschDmrsTypeAPosition(string selectorString, out int value)RemarksThis method gets the value of PuschD

### GetPuschDmrsTypeAPosition(string, out int)

Gets the position of first DMRS symbol in a slot when you set the [SetPuschMappingType(string, RFmxNRMXPuschMappingType)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschmappingtype__string-rfmxnrmxpuschmappingtype.html) method to [TypeA](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschmappingtype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPuschDmrsTypeAPosition(string selectorString, out int value)

#### Remarks

This method gets the value of [PuschDmrsTypeAPosition](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 2.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the position of first DMRS symbol in a slot when you set the SetPuschMappingType(string, RFmxNRMXPuschMappingType) method to TypeA. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschmappingtype__string-out.html language=enus -->
## TOPIC 00158: GetPuschMappingType(string, out RFmxNRMXPuschMappingType)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschmappingtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschmappingtype__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mapping type of DMRS. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPuschMappingType(string selectorString, out RFmxNRMXPuschMappingType value)RemarksThis method gets the value of PuschMappingType attribute.The default value is TypeA.ParametersNameTypeDescriptionselectorString

### GetPuschMappingType(string, out RFmxNRMXPuschMappingType)

Gets the mapping type of DMRS.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPuschMappingType(string selectorString, out RFmxNRMXPuschMappingType value)

#### Remarks

This method gets the value of [PuschMappingType](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [TypeA](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschmappingtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | out RFmxNRMXPuschMappingType | Upon return, contains the mapping type of DMRS. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschmodulationtype__string-out.html language=enus -->
## TOPIC 00159: GetPuschModulationType(string, out RFmxNRMXPuschModulationType)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschmodulationtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschmodulationtype__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the modulation scheme used in the physical uplink shared channel (PUSCH) of the signal being measured. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPuschModulationType(string selectorString, out RFmxNRMXPuschModulationType value)RemarksThis method gets the value of PuschModulatio

### GetPuschModulationType(string, out RFmxNRMXPuschModulationType)

Gets the modulation scheme used in the physical uplink shared channel (PUSCH) of the signal being measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPuschModulationType(string selectorString, out RFmxNRMXPuschModulationType value)

#### Remarks

This method gets the value of [PuschModulationType](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Qpsk](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschmodulationtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | out RFmxNRMXPuschModulationType | Upon return, contains the modulation scheme used in the physical uplink shared channel (PUSCH) of the signal being measured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschnumberofresourceblockclusters__string-out.html language=enus -->
## TOPIC 00160: GetPuschNumberOfResourceBlockClusters(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschnumberofresourceblockclusters__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschnumberofresourceblockclusters__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of clusters of resource allocations with each cluster including one or more consecutive resource blocks. This method is ignored if you set the SetAutoResourceBlockDetectionEnabled(string, RFmxNRMXAutoResourceBlockDetectionEnabled) method to True. SyntaxNamespace: NationalInstruments.

### GetPuschNumberOfResourceBlockClusters(string, out int)

Gets the number of clusters of resource allocations with each cluster including one or more consecutive resource blocks. This method is ignored if you set the [SetAutoResourceBlockDetectionEnabled(string, RFmxNRMXAutoResourceBlockDetectionEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmx-setautoresourceblockdetectionenabled__string-rfmxnrmxautoresourceblockdetectionenabled.html) method to [True](nationalinstruments-rfmx-nrmx-rfmxnrmxautoresourceblockdetectionenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPuschNumberOfResourceBlockClusters(string selectorString, out int value)

#### Remarks

This method gets the value of [PuschNumberOfResourceBlockClusters](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the number of clusters of resource allocations with each cluster including one or more consecutive resource blocks. This method is ignored if you set the SetAutoResourceBlockDetectionEnabled(string, RFmxNRMXAutoResourceBlockDetectionEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschnumberofresourceblocks__string-out.html language=enus -->
## TOPIC 00161: GetPuschNumberOfResourceBlocks(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschnumberofresourceblocks__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschnumberofresourceblocks__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of consecutive resource blocks in a physical uplink shared channel (PUSCH) cluster. This method is ignored if you set the SetAutoResourceBlockDetectionEnabled(string, RFmxNRMXAutoResourceBlockDetectionEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int G

### GetPuschNumberOfResourceBlocks(string, out int)

Gets the number of consecutive resource blocks in a physical uplink shared channel (PUSCH) cluster. This method is ignored if you set the [SetAutoResourceBlockDetectionEnabled(string, RFmxNRMXAutoResourceBlockDetectionEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmx-setautoresourceblockdetectionenabled__string-rfmxnrmxautoresourceblockdetectionenabled.html) method to [True](nationalinstruments-rfmx-nrmx-rfmxnrmxautoresourceblockdetectionenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPuschNumberOfResourceBlocks(string selectorString, out int value)

#### Remarks

This method gets the value of [PuschNumberOfResourceBlocks](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is -1. If you set this property to -1, all available resource blocks for the specified bandwidth are configured.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number, pusch number and puschcluster number. Example: "puschcluster0" or "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0/puschcluster0". You can use the BuildPuschClusterString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the number of consecutive resource blocks in a physical uplink shared channel (PUSCH) cluster. This method is ignored if you set the SetAutoResourceBlockDetectionEnabled(string, RFmxNRMXAutoResourceBlockDetectionEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschptrsantennaports__string-out.html language=enus -->
## TOPIC 00162: GetPuschPtrsAntennaPorts(string, out string)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschptrsantennaports__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschptrsantennaports__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DMRS antenna ports associated with PTRS transmission. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPuschPtrsAntennaPorts(string selectorString, out string value)Rema

### GetPuschPtrsAntennaPorts(string, out string)

Gets the DMRS antenna ports associated with PTRS transmission. This method is valid only if you set the [SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschptrsenabled__string-rfmxnrmxpuschptrsenabled.html) method to [True](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschptrsenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPuschPtrsAntennaPorts(string selectorString, out string value)

#### Remarks

This method gets the value of [PuschPtrsAntennaPorts](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | out string | Upon return, contains the DMRS antenna ports associated with PTRS transmission. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschptrsenabled__string-out.html language=enus -->
## TOPIC 00163: GetPuschPtrsEnabled(string, out RFmxNRMXPuschPtrsEnabled)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschptrsenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschptrsenabled__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the PUSCH transmission contains PTRS signals. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPuschPtrsEnabled(string selectorString, out RFmxNRMXPuschPtrsEnabled value)RemarksThis method gets the value of PuschPtrsEnabled attribute.The default value is False.ParametersNameT

### GetPuschPtrsEnabled(string, out RFmxNRMXPuschPtrsEnabled)

Gets whether the PUSCH transmission contains PTRS signals.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPuschPtrsEnabled(string selectorString, out RFmxNRMXPuschPtrsEnabled value)

#### Remarks

This method gets the value of [PuschPtrsEnabled](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschptrsenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | out RFmxNRMXPuschPtrsEnabled | Upon return, contains whether the PUSCH transmission contains PTRS signals. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschptrsfrequencydensity__string-out.html language=enus -->
## TOPIC 00164: GetPuschPtrsFrequencyDensity(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschptrsfrequencydensity__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschptrsfrequencydensity__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the density of PTRS in frequency domain. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True and SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to False. SyntaxNamespace: NationalInstruments.RFmx

### GetPuschPtrsFrequencyDensity(string, out int)

Gets the density of PTRS in frequency domain. This method is valid only if you set the [SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschptrsenabled__string-rfmxnrmxpuschptrsenabled.html) method to [True](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschptrsenabled.html) and [SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschtransformprecodingenabled__string-rfmxnrmxpuschtransformprecodingenabled.html) method to [False](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschptrsenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPuschPtrsFrequencyDensity(string selectorString, out int value)

#### Remarks

This method gets the value of [PuschPtrsFrequencyDensity](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 2.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the density of PTRS in frequency domain. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True and SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschptrspower__string-out.html language=enus -->
## TOPIC 00165: GetPuschPtrsPower(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschptrspower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschptrspower__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the factor by which the PUSCH PTRS REs are boosted. This value is expressed in dB. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPuschPtrsPower(string selectorString, out

### GetPuschPtrsPower(string, out double)

Gets the factor by which the PUSCH PTRS REs are boosted. This value is expressed in dB. This method is valid only if you set the [SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschptrsenabled__string-rfmxnrmxpuschptrsenabled.html) method to [True](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschptrsenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPuschPtrsPower(string selectorString, out double value)

#### Remarks

This method gets the value of [PuschPtrsPower](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the factor by which the PUSCH PTRS REs are boosted. This value is expressed in dB. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschptrsreoffset__string-out.html language=enus -->
## TOPIC 00166: GetPuschPtrsREOffset(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschptrsreoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschptrsreoffset__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RE offset to be used for transmission of PTRS as defined in the Table 6.4.1.2.2.1-1 of 3GPP 38.211 specification. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True and SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransfor

### GetPuschPtrsREOffset(string, out int)

Gets the RE offset to be used for transmission of PTRS as defined in the Table 6.4.1.2.2.1-1 of *3GPP 38.211* specification. This method is valid only if you set the [SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschptrsenabled__string-rfmxnrmxpuschptrsenabled.html) method to [True](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschptrsenabled.html) and [SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschtransformprecodingenabled__string-rfmxnrmxpuschtransformprecodingenabled.html) method to [False](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschptrsenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPuschPtrsREOffset(string selectorString, out int value)

#### Remarks

This method gets the value of [PuschPtrsREOffset](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 00.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the RE offset to be used for transmission of PTRS as defined in the Table 6.4.1.2.2.1-1 of 3GPP 38.211 specification. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True and SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschresourceblockoffset__string-out.html language=enus -->
## TOPIC 00167: GetPuschResourceBlockOffset(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschresourceblockoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getpuschresourceblockoffset__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the starting resource block number of a PUSCH cluster. This method is ignored if you set the SetAutoResourceBlockDetectionEnabled(string, RFmxNRMXAutoResourceBlockDetectionEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPuschResourceBlockOffset(string select

### GetPuschResourceBlockOffset(string, out int)

Gets the starting resource block number of a PUSCH cluster. This method is ignored if you set the [SetAutoResourceBlockDetectionEnabled(string, RFmxNRMXAutoResourceBlockDetectionEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmx-setautoresourceblockdetectionenabled__string-rfmxnrmxautoresourceblockdetectionenabled.html) method to [True](nationalinstruments-rfmx-nrmx-rfmxnrmxautoresourceblockdetectionenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPuschResourceBlockOffset(string selectorString, out int value)

#### Remarks

This method gets the value of [PuschResourceBlockOffset](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number, pusch number and puschcluster number. Example: "puschcluster0" or "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0/puschcluster0". You can use the BuildPuschClusterString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the starting resource block number of a PUSCH cluster. This method is ignored if you set the SetAutoResourceBlockDetectionEnabled(string, RFmxNRMXAutoResourceBlockDetectionEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getreferencegridsize__string-out.html language=enus -->
## TOPIC 00168: GetReferenceGridSize(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getreferencegridsize__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getreferencegridsize__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the reference resource grid size when you set the SetGridSizeMode(string, RFmxNRMXGridSizeMode) method to Manual. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetReferenceGridSize(string selectorString, out int value)RemarksThis method gets the value of ReferenceGridSize attribute.P

### GetReferenceGridSize(string, out int)

Gets the reference resource grid size when you set the [SetGridSizeMode(string, RFmxNRMXGridSizeMode)](nationalinstruments-rfmx-nrmx-rfmxnrmx-setgridsizemode__string-rfmxnrmxgridsizemode.html) method to [Manual](nationalinstruments-rfmx-nrmx-rfmxnrmxgridsizemode.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetReferenceGridSize(string selectorString, out int value)

#### Remarks

This method gets the value of [ReferenceGridSize](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the reference resource grid size when you set the SetGridSizeMode(string, RFmxNRMXGridSizeMode) method to Manual. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getreferencegridsubcarrierspacing__string-out.html language=enus -->
## TOPIC 00169: GetReferenceGridSubcarrierSpacing(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getreferencegridsubcarrierspacing__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getreferencegridsubcarrierspacing__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the subcarrier spacing of the reference resource grid when you set the Reference Grid Alignment Mode method to Manual. This should be the largest subcarrier spacing used in the component carrier. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetReferenc

### GetReferenceGridSubcarrierSpacing(string, out double)

Gets the subcarrier spacing of the reference resource grid when you set the Reference Grid Alignment Mode method to Manual. This should be the largest subcarrier spacing used in the component carrier. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetReferenceGridSubcarrierSpacing(string selectorString, out double value)

#### Remarks

This method gets the value of [ReferenceGridSubcarrierSpacing](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 30kHz.Valid values for frequency range 1 are 15kHz, 30kHz, and 60kHz.Valid values for frequency range 2 are 60kHz and 120kHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the subcarrier spacing of the reference resource grid when you set the Reference Grid Alignment Mode method to Manual. This should be the largest subcarrier spacing used in the component carrier. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getrnti__string-out.html language=enus -->
## TOPIC 00170: GetRnti(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getrnti__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getrnti__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RNTI. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetRnti(string selectorString, out int value)RemarksThis method gets the value of Rnti attribute.The default value is 1.ParametersNameTypeDescriptionselectorStringstringSpecifies the subblock number, carrier number, bwp number a

### GetRnti(string, out int)

Gets the RNTI.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetRnti(string selectorString, out int value)

#### Remarks

This method gets the value of [Rnti](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number and user number. Example: "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0". You can use the BuildUserString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the RNTI. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getsamplesperptrsgroup__string-out.html language=enus -->
## TOPIC 00171: GetSamplesPerPtrsGroup(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getsamplesperptrsgroup__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getsamplesperptrsgroup__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of samples per each PTRS group. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True and SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFm

### GetSamplesPerPtrsGroup(string, out int)

Gets the number of samples per each PTRS group. This method is valid only if you set the [SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschptrsenabled__string-rfmxnrmxpuschptrsenabled.html) method to [True](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschptrsenabled.html) and [SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschtransformprecodingenabled__string-rfmxnrmxpuschtransformprecodingenabled.html) method to [True](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschptrsenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetSamplesPerPtrsGroup(string selectorString, out int value)

#### Remarks

This method gets the value of [SamplesPerPtrsGroup](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 2.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the number of samples per each PTRS group. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True and SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getssbactiveblocks__string-out.html language=enus -->
## TOPIC 00172: GetSsbActiveBlocks(string, out string)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getssbactiveblocks__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getssbactiveblocks__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the SSB burst(s) indices for the SSB pattern that needs to be transmitted. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetSsbActiveBlocks(string selectorString, out string value)RemarksThis method gets the value of SsbActiveBlocks attribute.The default value is 0 - Last.ParametersN

### GetSsbActiveBlocks(string, out string)

Gets the SSB burst(s) indices for the SSB pattern that needs to be transmitted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetSsbActiveBlocks(string selectorString, out string value)

#### Remarks

This method gets the value of [SsbActiveBlocks](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0 - Last.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out string | Upon return, contains the SSB burst(s) indices for the SSB pattern that needs to be transmitted. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getssbcrboffset__string-out.html language=enus -->
## TOPIC 00173: GetSsbCrbOffset(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getssbcrboffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getssbcrboffset__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the CRB offset for the SS/PBCH block relative to the reference Point A in units of 15 kHz or 60 kHz resource blocks for frequency range 1 and frequency range 2 respectively. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetSsbCrbOffset(string selectorString, out int value)RemarksThis

### GetSsbCrbOffset(string, out int)

Gets the CRB offset for the SS/PBCH block relative to the reference Point A in units of 15 kHz or 60 kHz resource blocks for frequency range 1 and frequency range 2 respectively.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetSsbCrbOffset(string selectorString, out int value)

#### Remarks

This method gets the value of [SsbCrbOffset](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the CRB offset for the SS/PBCH block relative to the reference Point A in units of 15 kHz or 60 kHz resource blocks for frequency range 1 and frequency range 2 respectively. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getssbenabled__string-out.html language=enus -->
## TOPIC 00174: GetSsbEnabled(string, out RFmxNRMXSsbEnabled)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getssbenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getssbenabled__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether synchronization signal block (SSB) is present in the transmitted signal. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetSsbEnabled(string selectorString, out RFmxNRMXSsbEnabled value)RemarksThis method gets the value of SsbEnabled attribute.The default value is False.Parame

### GetSsbEnabled(string, out RFmxNRMXSsbEnabled)

Gets whether synchronization signal block (SSB) is present in the transmitted signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetSsbEnabled(string selectorString, out RFmxNRMXSsbEnabled value)

#### Remarks

This method gets the value of [SsbEnabled](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-nrmx-rfmxnrmxssbenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out RFmxNRMXSsbEnabled | Upon return, contains whether synchronization signal block (SSB) is present in the transmitted signal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getssbgridstart__string-out.html language=enus -->
## TOPIC 00175: GetSsbGridStart(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getssbgridstart__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getssbgridstart__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the SSB resource grid start relative to Reference Point A in terms of resource block offset. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetSsbGridStart(string selectorString, out int value)RemarksThis method gets the value of SsbGridStart attribute.ParametersNameTypeDescriptionsel

### GetSsbGridStart(string, out int)

Gets the SSB resource grid start relative to Reference Point A in terms of resource block offset.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetSsbGridStart(string selectorString, out int value)

#### Remarks

This method gets the value of [SsbGridStart](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the SSB resource grid start relative to Reference Point A in terms of resource block offset. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getssbperiodicity__string-out.html language=enus -->
## TOPIC 00176: GetSsbPeriodicity(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getssbperiodicity__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getssbperiodicity__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the time difference with which the SS/PBCH block transmit pattern repeats. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetSsbPeriodicity(string selectorString, out double value)RemarksThis method gets the value of SsbPeriodicity attribute.The default value is 5 ms.ParametersNameTyp

### GetSsbPeriodicity(string, out double)

Gets the time difference with which the SS/PBCH block transmit pattern repeats.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetSsbPeriodicity(string selectorString, out double value)

#### Remarks

This method gets the value of [SsbPeriodicity](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 5 ms.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the repetition duration of the SS/PBCH block transmit pattern. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getssbsubcarrieroffset__string-out.html language=enus -->
## TOPIC 00177: GetSsbSubcarrierOffset(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getssbsubcarrieroffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getssbsubcarrieroffset__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an additional subcarrier offset for the SS/PBCH block in units of resource blocks of 15 kHz or subcarrier spacing given by SSB Subcarrier Common method for frequency range 1 and frequency range 2 respectively. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetSsbSubcarrierOffset(strin

### GetSsbSubcarrierOffset(string, out int)

Gets an additional subcarrier offset for the SS/PBCH block in units of resource blocks of 15 kHz or subcarrier spacing given by SSB Subcarrier Common method for frequency range 1 and frequency range 2 respectively.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetSsbSubcarrierOffset(string selectorString, out int value)

#### Remarks

This method gets the value of [SsbSubcarrierOffset](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out int | Upon return, contains an additional subcarrier offset for the SS/PBCH block in units of resource blocks of 15 kHz or subcarrier spacing given by SSB Subcarrier Common method for frequency range 1 and frequency range 2 respectively. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getssspower__string-out.html language=enus -->
## TOPIC 00178: GetSssPower(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getssspower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getssspower__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power scaling value for the secondary synchronization symbol in the SS/PBCH block. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetSssPower(string selectorString, out double value)RemarksThis method gets the value of SssPower attribute.The default

### GetSssPower(string, out double)

Gets the power scaling value for the secondary synchronization symbol in the SS/PBCH block. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetSssPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SssPower](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power scaling value for the secondary synchronization symbol in the SS/PBCH block. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getsubbandallocation__string-out.html language=enus -->
## TOPIC 00179: GetSubBandAllocation(string, out string)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getsubbandallocation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getsubbandallocation__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the sub-band allocation in the NR-U wideband channel. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetSubBandAllocation(string selectorString, out string value)RemarksThis method gets the value of SubBandAllocation attribute.The default value is 0-Last, whereLast = 0 for 20 MHz 1 fo

### GetSubBandAllocation(string, out string)

Gets the sub-band allocation in the NR-U wideband channel.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetSubBandAllocation(string selectorString, out string value)

#### Remarks

This method gets the value of [SubBandAllocation](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0-Last, whereLast = 0 for 20 MHz 1 for 40 MHz 2 for 60 MHz 3 for 80 MHz 4 for 100 MHz

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out string | Upon return, contains the sub-band allocation in the NR-U wideband channel. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getsubcarrierspacingcommon__string-out.html language=enus -->
## TOPIC 00180: GetSubcarrierSpacingCommon(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getsubcarrierspacingcommon__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-getsubcarrierspacingcommon__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the basic unit of SetSsbSubcarrierOffset(string, int) method for frequency range 2. The method refers to the MIB control element subCarrierSpacingCommon in 3GPP TS 38.331. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetSubcarrierSpacingCommon(string selectorString, out double value

### GetSubcarrierSpacingCommon(string, out double)

Gets the basic unit of [SetSsbSubcarrierOffset(string, int)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setssbsubcarrieroffset__string-int.html) method for frequency range 2. The method refers to the MIB control element subCarrierSpacingCommon in *3GPP TS 38.331*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetSubcarrierSpacingCommon(string selectorString, out double value)

#### Remarks

This method gets the value of [SubcarrierSpacingCommon](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 60kHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the basic unit of SetSsbSubcarrierOffset(string, int) method for frequency range 2. The method refers to the MIB control element subCarrierSpacingCommon in 3GPP TS 38.331. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setallocated__string-rfmxnrmxcomponentcarrierallocated.html language=enus -->
## TOPIC 00181: SetAllocated(string, RFmxNRMXComponentCarrierAllocated)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setallocated__string-rfmxnrmxcomponentcarrierallocated.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setallocated__string-rfmxnrmxcomponentcarrierallocated.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether a component carrier has one or more resource elements allocated. While performing IBE measurement on a subblock, you set this method to False for all secondary component carriers as specified in section 6.4A.2.3 of 3GPP 38.521-1 and 3GPP 38.521-2 specifications. SyntaxNamespace: Nationa

### SetAllocated(string, RFmxNRMXComponentCarrierAllocated)

Sets whether a component carrier has one or more resource elements allocated. While performing IBE measurement on a subblock, you set this method to [False](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrierallocated.html) for all secondary component carriers as specified in section 6.4A.2.3 of *3GPP 38.521-1* and *3GPP 38.521-2* specifications.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetAllocated(string selectorString, RFmxNRMXComponentCarrierAllocated value)

#### Remarks

This method sets the value of [ComponentCarrierAllocated](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrierallocated.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | RFmxNRMXComponentCarrierAllocated | Specifies whether a component carrier has one or more resource elements allocated. While performing IBE measurement on a subblock, you set this method to False for all secondary component carriers as specified in section 6.4A.2.3 of 3GPP 38.521-1 and 3GPP 38.521-2 specifications. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setbandwidth__string-double.html language=enus -->
## TOPIC 00182: SetBandwidth(string, double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setbandwidth__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setbandwidth__string-double.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the channel bandwidth of the signal being measured. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetBandwidth(string selectorString, double value)RemarksThis method sets the value of ComponentCarrierBandwidth attribute.The default value is 100M. Valid

### SetBandwidth(string, double)

Sets the channel bandwidth of the signal being measured. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetBandwidth(string selectorString, double value)

#### Remarks

This method sets the value of [ComponentCarrierBandwidth](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 100M. Valid values for frequency range 1 are from 3M to 100M. Valid values for frequency range 2 are 50M, 100M, 200M, and 400M.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | double | Specifies the channel bandwidth of the signal being measured. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setcoresetnumberofsymbols__string-int.html language=enus -->
## TOPIC 00183: SetCoresetNumberOfSymbols(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setcoresetnumberofsymbols__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setcoresetnumberofsymbols__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of symbols alloted to CORESET in each slot. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetCoresetNumberOfSymbols(string selectorString, int value)RemarksThis method sets the value of CoresetNumberOfSymbols attribute.The default value is 1.ParametersNameTypeDescriptionse

### SetCoresetNumberOfSymbols(string, int)

Sets the number of symbols alloted to CORESET in each slot.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetCoresetNumberOfSymbols(string selectorString, int value)

#### Remarks

This method sets the value of [CoresetNumberOfSymbols](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number and coreset number. Example: "coreset0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/coreset0". You can use the BuildCoresetString(string, int) method to build the selector string. |
| value | int | Specifies the number of symbols alloted to CORESET in each slot. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setdownlinktestmodelmodulationtype__string-rfmxnrmxdownlinktestmodelmodulationtype.html language=enus -->
## TOPIC 00184: SetDownlinkTestModelModulationType(string, RFmxNRMXDownlinkTestModelModulationType)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setdownlinktestmodelmodulationtype__string-rfmxnrmxdownlinktestmodelmodulationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setdownlinktestmodelmodulationtype__string-rfmxnrmxdownlinktestmodelmodulationtype.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the modulation type to be used with the selected test model. Selecting the modulation type is supported only for test models NR-FR2-TM3.1 and NR-FR2-TM2. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetDownlinkTestModelModulationType(string selectorString, RFmxNRMXDownlinkTestModelM

### SetDownlinkTestModelModulationType(string, RFmxNRMXDownlinkTestModelModulationType)

Sets the modulation type to be used with the selected test model. Selecting the modulation type is supported only for test models *NR-FR2-TM3.1* and *NR-FR2-TM2*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetDownlinkTestModelModulationType(string selectorString, RFmxNRMXDownlinkTestModelModulationType value)

#### Remarks

This method sets the value of [DownlinkTestModelModulationType](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Standard](nationalinstruments-rfmx-nrmx-rfmxnrmxdownlinktestmodelmodulationtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | RFmxNRMXDownlinkTestModelModulationType | Specifies the modulation type to be used with the selected test model. Selecting the modulation type is supported only for test models NR-FR2-TM3.1 and NR-FR2-TM2. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setgridstart__string-int.html language=enus -->
## TOPIC 00185: SetGridStart(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setgridstart__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setgridstart__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the resource grid start relative to Reference Point A in terms of resource block offset when you set the Reference Grid Alignment Mode method to Manual. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetGridStart(string selectorString, int value)RemarksThis method sets the value of Gr

### SetGridStart(string, int)

Sets the resource grid start relative to Reference Point A in terms of resource block offset when you set the Reference Grid Alignment Mode method to Manual.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetGridStart(string selectorString, int value)

#### Remarks

This method sets the value of [GridStart](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number, subblock number and bwp number. Example: "carrier0" or "subblock0" or "bwp0" or "subblock0/carrier0/bwp0". You can use the BuildBandwidthPartString(string, int) method to build the selector string. |
| value | int | Specifies the resource grid start relative to Reference Point A in terms of resource block offset when you set the Reference Grid Alignment Mode method to Manual. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setnumberofcomponentcarriers__string-int.html language=enus -->
## TOPIC 00186: SetNumberOfComponentCarriers(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setnumberofcomponentcarriers__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setnumberofcomponentcarriers__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of component carriers configured within a subblock. Set this method to 1 for single carrier. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetNumberOfComponentCarriers(string selectorString, int value)RemarksThis method sets the value of NumberOfComponentCarriers attribute

### SetNumberOfComponentCarriers(string, int)

Sets the number of component carriers configured within a subblock. Set this method to 1 for single carrier.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetNumberOfComponentCarriers(string selectorString, int value)

#### Remarks

This method sets the value of [NumberOfComponentCarriers](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(string, int) method to build the selector string. |
| value | int | Specifies the number of component carriers configured within a subblock. Set this method to 1 for single carrier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setnumberofpdcchconfigurations__string-int.html language=enus -->
## TOPIC 00187: SetNumberOfPdcchConfigurations(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setnumberofpdcchconfigurations__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setnumberofpdcchconfigurations__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of PDCCH Configurations for a CORESET. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetNumberOfPdcchConfigurations(string selectorString, int value)RemarksThis method sets the value of NumberOfPdcchConfigurations attribute.The default value is 0.ParametersNameTypeDescript

### SetNumberOfPdcchConfigurations(string, int)

Sets the number of PDCCH Configurations for a CORESET.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetNumberOfPdcchConfigurations(string selectorString, int value)

#### Remarks

This method sets the value of [NumberOfPdcchConfigurations](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number and coreset number. Example: "coreset0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/coreset0". You can use the BuildCoresetString(string, int) method to build the selector string. |
| value | int | Specifies the number of PDCCH Configurations for a CORESET. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setnumberofusers__string-int.html language=enus -->
## TOPIC 00188: SetNumberOfUsers(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setnumberofusers__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setnumberofusers__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of users present in the bandwidth part. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetNumberOfUsers(string selectorString, int value)RemarksThis method sets the value of NumberOfUsers attribute.The default value is 1.ParametersNameTypeDescriptionselectorStringstringSpec

### SetNumberOfUsers(string, int)

Sets the number of users present in the bandwidth part.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetNumberOfUsers(string selectorString, int value)

#### Remarks

This method sets the value of [NumberOfUsers](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number, subblock number and bwp number. Example: "carrier0" or "subblock0" or "bwp0" or "subblock0/carrier0/bwp0". You can use the BuildBandwidthPartString(string, int) method to build the selector string. |
| value | int | Specifies the number of users present in the bandwidth part. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdcchcceaggregationlevel__string-int.html language=enus -->
## TOPIC 00189: SetPdcchCceAggregationLevel(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdcchcceaggregationlevel__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdcchcceaggregationlevel__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the CCE aggregation level of PDCCH. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetPdcchCceAggregationLevel(string selectorString, int value)RemarksThis method sets the value of PdcchCceAggregationLevel attribute.The default value is 1.ParametersNameTypeDescriptionselectorStringstr

### SetPdcchCceAggregationLevel(string, int)

Sets the CCE aggregation level of PDCCH.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetPdcchCceAggregationLevel(string selectorString, int value)

#### Remarks

This method sets the value of [PdcchCceAggregationLevel](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, coreset number and pdcch number. Example: "pdcch0" or "coreset0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/coreset0/pdcch0". You can use the BuildPdcchString(string, int) method to build the selector string. |
| value | int | Specifies the CCE aggregation level of PDCCH. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdcchcceoffset__string-int.html language=enus -->
## TOPIC 00190: SetPdcchCceOffset(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdcchcceoffset__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdcchcceoffset__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the PDCCH CCE offset. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetPdcchCceOffset(string selectorString, int value)RemarksThis method sets the value of PdcchCceOffset attribute.It is used when the PDCCH Candidate Index is set to -1. The default value is 0.ParametersNameTypeDescri

### SetPdcchCceOffset(string, int)

Sets the PDCCH CCE offset.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetPdcchCceOffset(string selectorString, int value)

#### Remarks

This method sets the value of [PdcchCceOffset](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.It is used when the PDCCH Candidate Index is set to -1. The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, coreset number and pdcch number. Example: "pdcch0" or "coreset0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/coreset0/pdcch0". You can use the BuildPdcchString(string, int) method to build the selector string. |
| value | int | Specifies the PDCCH CCE offset. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdcchslotallocation__string-string.html language=enus -->
## TOPIC 00191: SetPdcchSlotAllocation(string, string)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdcchslotallocation__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdcchslotallocation__string-string.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the slot allocation in NR frame. This defines the indices of the allocated slots. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetPdcchSlotAllocation(string selectorString, string value)RemarksThis method sets the value of PdcchSlotAllocation attribute.The default value is 0-last. V

### SetPdcchSlotAllocation(string, string)

Sets the slot allocation in NR frame. This defines the indices of the allocated slots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetPdcchSlotAllocation(string selectorString, string value)

#### Remarks

This method sets the value of [PdcchSlotAllocation](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0-last. Valid values are between 0 and (Maximum Slots in Frame - 1).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, coreset number and pdcch number. Example: "pdcch0" or "coreset0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/coreset0/pdcch0". You can use the BuildPdcchString(string, int) method to build the selector string. |
| value | string | Specifies the slot allocation in NR frame. This defines the indices of the allocated slots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdschdmrsnscid__string-int.html language=enus -->
## TOPIC 00192: SetPdschDmrsnScid(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdschdmrsnscid__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdschdmrsnscid__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of PDSCH DMRS nSCID used for reference signal generation. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetPdschDmrsnScid(string selectorString, int value)RemarksThis method sets the value of PdschDmrsnScid attribute.The default value is 0.ParametersNameTypeDescriptionselec

### SetPdschDmrsnScid(string, int)

Sets the value of PDSCH DMRS nSCID used for reference signal generation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetPdschDmrsnScid(string selectorString, int value)

#### Remarks

This method sets the value of [PdschDmrsnScid](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | int | Specifies the value of PDSCH DMRS nSCID used for reference signal generation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdschdmrsreleaseversion__string-rfmxnrmxpdschdmrsreleaseversion.html language=enus -->
## TOPIC 00193: SetPdschDmrsReleaseVersion(string, RFmxNRMXPdschDmrsReleaseVersion)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdschdmrsreleaseversion__string-rfmxnrmxpdschdmrsreleaseversion.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdschdmrsreleaseversion__string-rfmxnrmxpdschdmrsreleaseversion.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the 3GGP release version for PDSCH DMRS. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetPdschDmrsReleaseVersion(string selectorString, RFmxNRMXPdschDmrsReleaseVersion value)RemarksThis method sets the value of PdschDmrsReleaseVersion attribute.The default value is 0.ParametersNameT

### SetPdschDmrsReleaseVersion(string, RFmxNRMXPdschDmrsReleaseVersion)

Sets the 3GGP release version for PDSCH DMRS.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetPdschDmrsReleaseVersion(string selectorString, RFmxNRMXPdschDmrsReleaseVersion value)

#### Remarks

This method sets the value of [PdschDmrsReleaseVersion](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | RFmxNRMXPdschDmrsReleaseVersion | Specifies the 3GGP release version for PDSCH DMRS. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdschdmrstypeaposition__string-int.html language=enus -->
## TOPIC 00194: SetPdschDmrsTypeAPosition(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdschdmrstypeaposition__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdschdmrstypeaposition__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the position of first DMRS symbol in a slot for Type A configurations. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetPdschDmrsTypeAPosition(string selectorString, int value)RemarksThis method sets the value of PdschDmrsTypeAPosition attribute.The default value is 2.ParametersNameT

### SetPdschDmrsTypeAPosition(string, int)

Sets the position of first DMRS symbol in a slot for Type A configurations.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetPdschDmrsTypeAPosition(string selectorString, int value)

#### Remarks

This method sets the value of [PdschDmrsTypeAPosition](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 2.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | int | Specifies the position of first DMRS symbol in a slot for Type A configurations. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdschptrspowermode__string-rfmxnrmxpdschptrspowermode.html language=enus -->
## TOPIC 00195: SetPdschPtrsPowerMode(string, RFmxNRMXPdschPtrsPowerMode)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdschptrspowermode__string-rfmxnrmxpdschptrspowermode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdschptrspowermode__string-rfmxnrmxpdschptrspowermode.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the configured SetPdschPtrsPower(string, double) is calculated as defined in 3GPP specification or configured by you. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetPdschPtrsPowerMode(string selectorString, RFmxNRMXPdschPtrsPowerMode value)RemarksThis method sets the value

### SetPdschPtrsPowerMode(string, RFmxNRMXPdschPtrsPowerMode)

Sets whether the configured [SetPdschPtrsPower(string, double)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdschptrspower__string-double.html) is calculated as defined in 3GPP specification or configured by you.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetPdschPtrsPowerMode(string selectorString, RFmxNRMXPdschPtrsPowerMode value)

#### Remarks

This method sets the value of [PdschPtrsPowerMode](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Standard](nationalinstruments-rfmx-nrmx-rfmxnrmxpdschptrspowermode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | RFmxNRMXPdschPtrsPowerMode | Specifies whether the configured SetPdschPtrsPower(string, double) is calculated as defined in 3GPP specification or configured by you. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdschsymbolallocation__string-string.html language=enus -->
## TOPIC 00196: SetPdschSymbolAllocation(string, string)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdschsymbolallocation__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpdschsymbolallocation__string-string.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the symbol allocation of each slot allocation. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetPdschSymbolAllocation(string selectorString, string value)RemarksThis method sets the value of PdschSymbolAllocation attribute.The default value is 0-Last. Valid values are from 0 to 13, i

### SetPdschSymbolAllocation(string, string)

Sets the symbol allocation of each slot allocation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetPdschSymbolAllocation(string selectorString, string value)

#### Remarks

This method sets the value of [PdschSymbolAllocation](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0-Last. Valid values are from 0 to 13, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pdsch number. Example: "pdsch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pdsch0". You can use the BuildPdschString(string, int) method to build the selector string. |
| value | string | Specifies the symbol allocation of each slot allocation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpsspower__string-double.html language=enus -->
## TOPIC 00197: SetPssPower(string, double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpsspower__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpsspower__string-double.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the power scaling value for the primary synchronization symbol in the SS/PBCH block. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetPssPower(string selectorString, double value)RemarksThis method sets the value of PssPower attribute.The default value

### SetPssPower(string, double)

Sets the power scaling value for the primary synchronization symbol in the SS/PBCH block. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetPssPower(string selectorString, double value)

#### Remarks

This method sets the value of [PssPower](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | double | Specifies the power scaling value for the primary synchronization symbol in the SS/PBCH block. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschnumberofresourceblockclusters__string-int.html language=enus -->
## TOPIC 00198: SetPuschNumberOfResourceBlockClusters(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschnumberofresourceblockclusters__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschnumberofresourceblockclusters__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of clusters of resource allocations with each cluster including one or more consecutive resource blocks. This method is ignored if you set the SetAutoResourceBlockDetectionEnabled(string, RFmxNRMXAutoResourceBlockDetectionEnabled) method to True. SyntaxNamespace: NationalInstruments.

### SetPuschNumberOfResourceBlockClusters(string, int)

Sets the number of clusters of resource allocations with each cluster including one or more consecutive resource blocks. This method is ignored if you set the [SetAutoResourceBlockDetectionEnabled(string, RFmxNRMXAutoResourceBlockDetectionEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmx-setautoresourceblockdetectionenabled__string-rfmxnrmxautoresourceblockdetectionenabled.html) method to [True](nationalinstruments-rfmx-nrmx-rfmxnrmxautoresourceblockdetectionenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetPuschNumberOfResourceBlockClusters(string selectorString, int value)

#### Remarks

This method sets the value of [PuschNumberOfResourceBlockClusters](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | int | Specifies the number of clusters of resource allocations with each cluster including one or more consecutive resource blocks. This method is ignored if you set the SetAutoResourceBlockDetectionEnabled(string, RFmxNRMXAutoResourceBlockDetectionEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschnumberofresourceblocks__string-int.html language=enus -->
## TOPIC 00199: SetPuschNumberOfResourceBlocks(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschnumberofresourceblocks__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschnumberofresourceblocks__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of consecutive resource blocks in a physical uplink shared channel (PUSCH) cluster. This method is ignored if you set the SetAutoResourceBlockDetectionEnabled(string, RFmxNRMXAutoResourceBlockDetectionEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int S

### SetPuschNumberOfResourceBlocks(string, int)

Sets the number of consecutive resource blocks in a physical uplink shared channel (PUSCH) cluster. This method is ignored if you set the [SetAutoResourceBlockDetectionEnabled(string, RFmxNRMXAutoResourceBlockDetectionEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmx-setautoresourceblockdetectionenabled__string-rfmxnrmxautoresourceblockdetectionenabled.html) method to [True](nationalinstruments-rfmx-nrmx-rfmxnrmxautoresourceblockdetectionenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetPuschNumberOfResourceBlocks(string selectorString, int value)

#### Remarks

This method sets the value of [PuschNumberOfResourceBlocks](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is -1. If you set this property to -1, all available resource blocks for the specified bandwidth are configured.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number, pusch number and puschcluster number. Example: "puschcluster0" or "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0/puschcluster0". You can use the BuildPuschClusterString(string, int) method to build the selector string. |
| value | int | Specifies the number of consecutive resource blocks in a physical uplink shared channel (PUSCH) cluster. This method is ignored if you set the SetAutoResourceBlockDetectionEnabled(string, RFmxNRMXAutoResourceBlockDetectionEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschptrsreoffset__string-int.html language=enus -->
## TOPIC 00200: SetPuschPtrsREOffset(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschptrsreoffset__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschptrsreoffset__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the RE offset to be used for transmission of PTRS as defined in the Table 6.4.1.2.2.1-1 of 3GPP 38.211 specification. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True and SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransfor

### SetPuschPtrsREOffset(string, int)

Sets the RE offset to be used for transmission of PTRS as defined in the Table 6.4.1.2.2.1-1 of *3GPP 38.211* specification. This method is valid only if you set the [SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschptrsenabled__string-rfmxnrmxpuschptrsenabled.html) method to [True](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschptrsenabled.html) and [SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschtransformprecodingenabled__string-rfmxnrmxpuschtransformprecodingenabled.html) method to [False](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschptrsenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetPuschPtrsREOffset(string selectorString, int value)

#### Remarks

This method sets the value of [PuschPtrsREOffset](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 00.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | int | Specifies the RE offset to be used for transmission of PTRS as defined in the Table 6.4.1.2.2.1-1 of 3GPP 38.211 specification. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True and SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschptrstimedensity__string-int.html language=enus -->
## TOPIC 00201: SetPuschPtrsTimeDensity(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschptrstimedensity__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschptrstimedensity__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the density of PTRS in time domain. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetPuschPtrsTimeDensity(string selectorString, int value)RemarksThis method sets the value

### SetPuschPtrsTimeDensity(string, int)

Sets the density of PTRS in time domain. This method is valid only if you set the [SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschptrsenabled__string-rfmxnrmxpuschptrsenabled.html) method to [True](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschptrsenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetPuschPtrsTimeDensity(string selectorString, int value)

#### Remarks

This method sets the value of [PuschPtrsTimeDensity](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | int | Specifies the density of PTRS in time domain. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschsymbolallocation__string-string.html language=enus -->
## TOPIC 00202: SetPuschSymbolAllocation(string, string)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschsymbolallocation__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschsymbolallocation__string-string.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the symbol allocation of each slot allocation. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetPuschSymbolAllocation(string selectorString, string value)RemarksThis method sets the value of PuschSymbolAllocation attribute.The default value is 0-Last. Valid values are from 0 to 13, i

### SetPuschSymbolAllocation(string, string)

Sets the symbol allocation of each slot allocation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetPuschSymbolAllocation(string selectorString, string value)

#### Remarks

This method sets the value of [PuschSymbolAllocation](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0-Last. Valid values are from 0 to 13, inclusive.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | string | Specifies the symbol allocation of each slot allocation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschtransformprecodingenabled__string-rfmxnrmxpuschtransformprecodingenabled.html language=enus -->
## TOPIC 00203: SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschtransformprecodingenabled__string-rfmxnrmxpuschtransformprecodingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschtransformprecodingenabled__string-rfmxnrmxpuschtransformprecodingenabled.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether transform precoding is enabled. Enable transform precoding when analyzing a DFT-s-OFDM waveform. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetPuschTransformPrecodingEnabled(string selectorString, RFmxNRMXPuschTransformPrecodingEnabled value)RemarksThis method sets the val

### SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled)

Sets whether transform precoding is enabled. Enable transform precoding when analyzing a DFT-s-OFDM waveform.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetPuschTransformPrecodingEnabled(string selectorString, RFmxNRMXPuschTransformPrecodingEnabled value)

#### Remarks

This method sets the value of [PuschTransformPrecodingEnabled](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschtransformprecodingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | RFmxNRMXPuschTransformPrecodingEnabled | Specifies whether transform precoding is enabled. Enable transform precoding when analyzing a DFT-s-OFDM waveform. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setradioaccesstype__string-rfmxnrmxcomponentcarrierradioaccesstype.html language=enus -->
## TOPIC 00204: SetRadioAccessType(string, RFmxNRMXComponentCarrierRadioAccessType)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setradioaccesstype__string-rfmxnrmxcomponentcarrierradioaccesstype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setradioaccesstype__string-rfmxnrmxcomponentcarrierradioaccesstype.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets if a carrier is a NR or an E-UTRA carrier while using dual connectivity (EN-DC) signal. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetRadioAccessType(string selectorString, RFmxNRMXComponentCarrierRadioAccessType value)RemarksThis method sets the value of ComponentCarrierRadioAcce

### SetRadioAccessType(string, RFmxNRMXComponentCarrierRadioAccessType)

Sets if a carrier is a NR or an E-UTRA carrier while using dual connectivity (EN-DC) signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetRadioAccessType(string selectorString, RFmxNRMXComponentCarrierRadioAccessType value)

#### Remarks

This method sets the value of [ComponentCarrierRadioAccessType](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [NR](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrierradioaccesstype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | RFmxNRMXComponentCarrierRadioAccessType | Specifies if a carrier is a NR or an E-UTRA carrier while using dual connectivity (EN-DC) signal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setratedeirp__string-double.html language=enus -->
## TOPIC 00205: SetRatedEirp(string, double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setratedeirp__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setratedeirp__string-double.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the rated carrier EIRP output power. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetRatedEirp(string selectorString, double value)RemarksThis method sets the value of RatedEirp attribute.The default value is 0.ParametersNameTypeDescriptionselectorStr

### SetRatedEirp(string, double)

Sets the rated carrier EIRP output power. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetRatedEirp(string selectorString, double value)

#### Remarks

This method sets the value of [RatedEirp](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | double | Specifies the rated carrier EIRP output power. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setratedtrp__string-double.html language=enus -->
## TOPIC 00206: SetRatedTrp(string, double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setratedtrp__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setratedtrp__string-double.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the rated carrier TRP output power. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetRatedTrp(string selectorString, double value)RemarksThis method sets the value of RatedTrp attribute.The default value is 0.ParametersNameTypeDescriptionselectorString

### SetRatedTrp(string, double)

Sets the rated carrier TRP output power. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetRatedTrp(string selectorString, double value)

#### Remarks

This method sets the value of [RatedTrp](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | double | Specifies the rated carrier TRP output power. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setreferencegridstart__string-int.html language=enus -->
## TOPIC 00207: SetReferenceGridStart(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setreferencegridstart__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setreferencegridstart__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the reference resource grid start relative to Reference Point A in terms of resource block offset when you set the Reference Grid Alignment Mode method to Manual. Center of subcarrier 0 in common resource block 0 is considered as Reference Point A. SyntaxNamespace: NationalInstruments.RFmx.NRMX

### SetReferenceGridStart(string, int)

Sets the reference resource grid start relative to Reference Point A in terms of resource block offset when you set the Reference Grid Alignment Mode method to Manual. Center of subcarrier 0 in common resource block 0 is considered as Reference Point A.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetReferenceGridStart(string selectorString, int value)

#### Remarks

This method sets the value of [ReferenceGridStart](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | int | Specifies the reference resource grid start relative to Reference Point A in terms of resource block offset when you set the Reference Grid Alignment Mode method to Manual. Center of subcarrier 0 in common resource block 0 is considered as Reference Point A. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setrnti__string-int.html language=enus -->
## TOPIC 00208: SetRnti(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setrnti__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setrnti__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the RNTI. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetRnti(string selectorString, int value)RemarksThis method sets the value of Rnti attribute.The default value is 1.ParametersNameTypeDescriptionselectorStringstringSpecifies the subblock number, carrier number, bwp number and u

### SetRnti(string, int)

Sets the RNTI.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetRnti(string selectorString, int value)

#### Remarks

This method sets the value of [Rnti](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number and user number. Example: "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0". You can use the BuildUserString(string, int) method to build the selector string. |
| value | int | Specifies the RNTI. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setsamplesperptrsgroup__string-int.html language=enus -->
## TOPIC 00209: SetSamplesPerPtrsGroup(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setsamplesperptrsgroup__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setsamplesperptrsgroup__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of samples per each PTRS group. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True and SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFm

### SetSamplesPerPtrsGroup(string, int)

Sets the number of samples per each PTRS group. This method is valid only if you set the [SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschptrsenabled__string-rfmxnrmxpuschptrsenabled.html) method to [True](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschptrsenabled.html) and [SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setpuschtransformprecodingenabled__string-rfmxnrmxpuschtransformprecodingenabled.html) method to [True](nationalinstruments-rfmx-nrmx-rfmxnrmxpuschptrsenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetSamplesPerPtrsGroup(string selectorString, int value)

#### Remarks

This method sets the value of [SamplesPerPtrsGroup](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 2.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number, carrier number, bwp number, user number and pusch number. Example: "pusch0" or "user0" or "bwp0" or "carrier0" or "subblock0" or "subblock0/carrier0/bwp0/user0/pusch0". You can use the BuildPuschString(string, int) method to build the selector string. |
| value | int | Specifies the number of samples per each PTRS group. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True and SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setssbactiveblocks__string-string.html language=enus -->
## TOPIC 00210: SetSsbActiveBlocks(string, string)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setssbactiveblocks__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setssbactiveblocks__string-string.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the SSB burst(s) indices for the SSB pattern that needs to be transmitted. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetSsbActiveBlocks(string selectorString, string value)RemarksThis method sets the value of SsbActiveBlocks attribute.The default value is 0 - Last.ParametersNameT

### SetSsbActiveBlocks(string, string)

Sets the SSB burst(s) indices for the SSB pattern that needs to be transmitted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetSsbActiveBlocks(string selectorString, string value)

#### Remarks

This method sets the value of [SsbActiveBlocks](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0 - Last.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | string | Specifies the SSB burst(s) indices for the SSB pattern that needs to be transmitted. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setssbenabled__string-rfmxnrmxssbenabled.html language=enus -->
## TOPIC 00211: SetSsbEnabled(string, RFmxNRMXSsbEnabled)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setssbenabled__string-rfmxnrmxssbenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setssbenabled__string-rfmxnrmxssbenabled.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether synchronization signal block (SSB) is present in the transmitted signal. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetSsbEnabled(string selectorString, RFmxNRMXSsbEnabled value)RemarksThis method sets the value of SsbEnabled attribute.The default value is False.Parameters

### SetSsbEnabled(string, RFmxNRMXSsbEnabled)

Sets whether synchronization signal block (SSB) is present in the transmitted signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetSsbEnabled(string selectorString, RFmxNRMXSsbEnabled value)

#### Remarks

This method sets the value of [SsbEnabled](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-nrmx-rfmxnrmxssbenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | RFmxNRMXSsbEnabled | Specifies whether synchronization signal block (SSB) is present in the transmitted signal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setssbpattern__string-rfmxnrmxssbpattern.html language=enus -->
## TOPIC 00212: SetSsbPattern(string, RFmxNRMXSsbPattern)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setssbpattern__string-rfmxnrmxssbpattern.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setssbpattern__string-rfmxnrmxssbpattern.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the candidate SS/PBCH blocks with different subcarrier spacing configurations as defined in the section 4.1 of 3GPP TS 38.213 specification. In order to configure Case C up to 1.88GHz unpaired spectrum, configure this method to CaseCUpTo3GHz. Similarly, to configure Case C 1.88GHz to 6GHz unpai

### SetSsbPattern(string, RFmxNRMXSsbPattern)

Sets the candidate SS/PBCH blocks with different subcarrier spacing configurations as defined in the section 4.1 of *3GPP TS 38.213* specification. In order to configure Case C up to 1.88GHz unpaired spectrum, configure this method to [CaseCUpTo3GHz](nationalinstruments-rfmx-nrmx-rfmxnrmxssbpattern.html). Similarly, to configure Case C 1.88GHz to 6GHz unpaired spectrum, configure this method to [CaseC3GHzTo6GHz](nationalinstruments-rfmx-nrmx-rfmxnrmxssbpattern.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetSsbPattern(string selectorString, RFmxNRMXSsbPattern value)

#### Remarks

This method sets the value of [SsbPattern](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [CaseB3GHzTo6GHz](nationalinstruments-rfmx-nrmx-rfmxnrmxssbpattern.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | RFmxNRMXSsbPattern | Specifies the candidate SS/PBCH blocks with different subcarrier spacing configurations as defined in the section 4.1 of 3GPP TS 38.213 specification. In order to configure Case C up to 1.88GHz unpaired spectrum, configure this method to CaseCUpTo3GHz. Similarly, to configure Case C 1.88GHz to 6GHz unpaired spectrum, configure this method to CaseC3GHzTo6GHz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setssbsubcarrieroffset__string-int.html language=enus -->
## TOPIC 00213: SetSsbSubcarrierOffset(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setssbsubcarrieroffset__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier-setssbsubcarrieroffset__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets an additional subcarrier offset for the SS/PBCH block in units of resource blocks of 15 kHz or subcarrier spacing given by SSB Subcarrier Common method for frequency range 1 and frequency range 2 respectively. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetSsbSubcarrierOffset(strin

### SetSsbSubcarrierOffset(string, int)

Sets an additional subcarrier offset for the SS/PBCH block in units of resource blocks of 15 kHz or subcarrier spacing given by SSB Subcarrier Common method for frequency range 1 and frequency range 2 respectively.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetSsbSubcarrierOffset(string selectorString, int value)

#### Remarks

This method sets the value of [SsbSubcarrierOffset](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | int | Specifies an additional subcarrier offset for the SS/PBCH block in units of resource blocks of 15 kHz or subcarrier spacing given by SSB Subcarrier Common method for frequency range 1 and frequency range 2 respectively. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXComponentCarrier Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier.html language=enus -->
## TOPIC 00214: RFmxNRMXComponentCarrier Class

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrier.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents Component Carrier. Derives fromRFmxNRMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.NRMXpublic class RFmxNRMXComponentCarrier : RFmxNRMXSubObjectMethodsNameDescriptionGetAllocated(string, out RFmxNRMXComponentCarrierAllocated)Gets whether a component carrier has one or more resource

### RFmxNRMXComponentCarrier Class

Represents Component Carrier.

#### Derives from

- RFmxNRMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public class RFmxNRMXComponentCarrier : RFmxNRMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| GetAllocated(string, out RFmxNRMXComponentCarrierAllocated) | Gets whether a component carrier has one or more resource elements allocated. While performing IBE measurement on a subblock, you set this method to False for all secondary component carriers as specified in section 6.4A.2.3 of 3GPP 38.521-1 and 3GPP 38.521-2 specifications. |
| GetBandwidth(string, out double) | Gets the channel bandwidth of the signal being measured. This value is expressed in Hz. |
| GetBandwidthPartCyclicPrefixMode(string, out RFmxNRMXBandwidthPartCyclicPrefixMode) | Gets the cyclic prefix (CP) duration and the number of symbols in a slot for the signal being measured. |
| GetBandwidthPartDCLocationKnown(string, out RFmxNRMXBandwidthPartDCLocationKnown) | Gets whether Uplink Tx Direct Current location within the carrier is determined. If set to False, DC location is undetermined within the carrier. In ModAcc measurement, IQ impairments are not estimated and compensated, and only General In-Band Emission limits are applied. If set to True, DC location is determined within the carrier. This property is not supported when Link Direction property is set to Downlink. Use "bwp(m)" or "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)/bwp(m)" as the Selector Strings to configure or read this property. |
| GetBandwidthPartNumberOfResourceBlocks(string, out int) | Sets the number of consecutive resource blocks in a bandwidth part. |
| GetBandwidthPartResourceBlockOffset(string, out int) | Gets the resource block offset of a bandwidth part relative to the resource SetGridStart(string, int) method. |
| GetBandwidthPartSubcarrierSpacing(string, out double) | Gets the subcarrier spacing of the bandwidth part used in the component carrier. |
| GetCellID(string, out int) | Gets a physical layer cell identity. |
| GetCoresetCceToRegMappingType(string, out RFmxNRMXCoresetCceToRegMappingType) | Gets the CCE-to-REG mapping type of CORESET. |
| GetCoresetInterleaverSize(string, out int) | Gets the interleaver size of CORESET for interleaved CCE to REG mapping. |
| GetCoresetNumberOfResourceBlockClusters(string, out int) | Gets the number of RB clusters present in the CORESET. |
| GetCoresetNumberOfResourceBlocks(string, out int) | Gets the number of consecutive resource blocks of CORESET cluster. |
| GetCoresetNumberOfSymbols(string, out int) | Gets the number of symbols alloted to CORESET in each slot. |
| GetCoresetPrecodingGranularity(string, out RFmxNRMXCoresetPrecodingGranularity) | Gets the precoding granularity of the CORESET. |
| GetCoresetRegBundleSize(string, out int) | Gets the RBG bundle size of CORESET for interleaved CCE to REG mapping. |
| GetCoresetResourceBlockOffset(string, out int) | Gets the starting resource block of a CORESET cluster. |
| GetCoresetShiftIndex(string, out int) | Gets the shift index of CORESET for interleaved CCE to REG mapping. |
| GetCoresetSymbolOffset(string, out int) | Gets the starting symbol number of the CORESET within a slot. |
| GetDownlinkTestModel(string, out RFmxNRMXDownlinkTestModel) | Gets the NR test model type when you set the Channel Configuration Mode method to Test Model. Refer to section 4.9.2 of the 3GPP 38.141 specification for more information regarding test model configurations. |
| GetDownlinkTestModelDuplexScheme(string, out RFmxNRMXDownlinkTestModelDuplexScheme) | Gets the duplexing technique of the signal being measured. Refer to section 4.9.2 of 3GPP 38.141 specification for more information regarding test model configurations based on duplex scheme. |
| GetDownlinkTestModelModulationType(string, out RFmxNRMXDownlinkTestModelModulationType) | Gets the modulation type to be used with the selected test model. Selecting the modulation type is supported only for test models NR-FR2-TM3.1 and NR-FR2-TM2. |
| GetEpreRatioPort(string, out int) | Gets the EPRE Ratio Port used to determine the PDSCH PT-RS RE power scaling as defined in the Table 4.1-2 of 3GPP TS 38.214 specification when you set the PDSCH PTRS Power Mode method to Standard. |
| GetFrequency(string, out double) | Gets the offset of the component carrier from the subblock center frequency that you configure in the Center Frequency method. This value is expressed in Hz. |
| GetGridSize(string, out int) | Gets the reference resource grid size when you set the SetGridSizeMode(string, RFmxNRMXGridSizeMode) method to Manual. |
| GetGridStart(string, out int) | Gets the resource grid start relative to Reference Point A in terms of resource block offset when you set the Reference Grid Alignment Mode method to Manual. |
| GetNumberOfBandwidthParts(string, out int) | Gets the number of bandwidth parts present in the component carrier. |
| GetNumberOfComponentCarriers(string, out int) | Gets the number of component carriers configured within a subblock. Set this method to 1 for single carrier. |
| GetNumberOfCoresets(string, out int) | Gets the number of CORSETs present in the bandwidth part. |
| GetNumberOfPdcchConfigurations(string, out int) | Gets the number of PDCCH Configurations for a CORESET. |
| GetNumberOfPdschConfigurations(string, out int) | Gets the number of PDSCH slot configurations. |
| GetNumberOfPtrsGroups(string, out int) | Gets the number of PTRS groups per OFDM symbol. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True and SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to True. |
| GetNumberOfPuschConfigurations(string, out int) | Gets the number of PUSCH slot configurations. |
| GetNumberOfUsers(string, out int) | Gets the number of users present in the bandwidth part. |
| GetPbchDmrsPower(string, out double) | Gets the power scaling value for the PBCH DMRS symbols in the SS/PBCH block. This value is expressed in dB. |
| GetPbchPower(string, out double) | Gets the power scaling value for the PBCH REs in the SS/PBCH block. This value is expressed in dB. |
| GetPdcchCceAggregationLevel(string, out int) | Gets the CCE aggregation level of PDCCH. |
| GetPdcchCceOffset(string, out int) | Gets the PDCCH CCE offset. |
| GetPdcchSlotAllocation(string, out string) | Gets the slot allocation in NR frame. This defines the indices of the allocated slots. |
| GetPdschDmrsAdditionalPositions(string, out int) | Gets the number of additional sets of consecutive DMRS symbols in a slot. |
| GetPdschDmrsAntennaPorts(string, out string) | Gets the antenna ports used for DMRS transmission. |
| GetPdschDmrsConfigurationType(string, out RFmxNRMXPdschDmrsConfigurationType) | Gets the configuration type of DMRS. |
| GetPdschDmrsDuration(string, out RFmxNRMXPdschDmrsDuration) | Gets whether the DMRS is single-symbol or double-symbol. |
| GetPdschDmrsnScid(string, out int) | Gets the value of PDSCH DMRS nSCID used for reference signal generation. |
| GetPdschDmrsNumberOfCdmGroups(string, out int) | Gets the number of CDM groups. |
| GetPdschDmrsPower(string, out double) | Gets the factor by which the PDSCH DMRS REs are boosted. This value is expressed in dB. |
| GetPdschDmrsPowerMode(string, out RFmxNRMXPdschDmrsPowerMode) | Gets whether the configured SetPdschDmrsPower(string, double) is calculated based on the SetPdschDmrsNumberOfCdmGroups(string, int) or specified by you. |
| GetPdschDmrsReleaseVersion(string, out RFmxNRMXPdschDmrsReleaseVersion) | Gets the 3GGP release version for PDSCH DMRS. |
| GetPdschDmrsScramblingID(string, out int) | Gets the value of scrambling ID used for reference signal generation. |
| GetPdschDmrsScramblingIDMode(string, out RFmxNRMXPdschDmrsScramblingIDMode) | Gets whether the configured Scrambling ID is based on SetCellID(string, int) or specified by you. |
| GetPdschDmrsTypeAPosition(string, out int) | Gets the position of first DMRS symbol in a slot for Type A configurations. |
| GetPdschMappingType(string, out RFmxNRMXPdschMappingType) | Gets the mapping type of DMRS. |
| GetPdschModulationType(string, out RFmxNRMXPdschModulationType) | Gets the modulation scheme used in PDSCH channel of the signal being measured. |
| GetPdschNumberOfResourceBlockClusters(string, out int) | Gets the number of clusters of resource allocations with each cluster including one or more consecutive resource blocks. |
| GetPdschNumberOfResourceBlocks(string, out int) | Gets the number of consecutive resource blocks in a PDSCH cluster. |
| GetPdschPtrsAntennaPorts(string, out string) | Gets the DMRS Antenna Ports associated with PTRS transmission. |
| GetPdschPtrsEnabled(string, out RFmxNRMXPdschPtrsEnabled) | Gets whether PT-RS is present in the transmitted signal. |
| GetPdschPtrsFrequencyDensity(string, out int) | Gets the density of PTRS in frequency domain. |
| GetPdschPtrsPower(string, out double) | Gets the factor by which the PDSCH PTRS REs are boosted, compared to PDSCH REs. This value is expressed in dB. The value of this method is taken as an input when you set the SetPdschPtrsPowerMode(string, RFmxNRMXPdschPtrsPowerMode) method to UserDefined. If you set the PDSCH PTRS Pwr Mode method to Standard, the value is computed from other parameters. |
| GetPdschPtrsPowerMode(string, out RFmxNRMXPdschPtrsPowerMode) | Gets whether the configured SetPdschPtrsPower(string, double) is calculated as defined in 3GPP specification or configured by you. |
| GetPdschPtrsREOffset(string, out int) | Gets the RE Offset to be used for transmission of PTRS as defined in Table 7.4.1.2.2-1 of 3GPP 38.211 specification. |
| GetPdschPtrsTimeDensity(string, out int) | Gets the density of PTRS in time domain. |
| GetPdschResourceBlockOffset(string, out int) | Gets the starting resource block number of a PDSCH cluster. |
| GetPdschSlotAllocation(string, out string) | Gets the slot allocation in NR Frame. This defines the indices of the allocated slots. |
| GetPdschSymbolAllocation(string, out string) | Gets the symbol allocation of each slot allocation. |
| GetPssPower(string, out double) | Gets the power scaling value for the primary synchronization symbol in the SS/PBCH block. This value is expressed in dB. |
| GetPuschDmrsAdditionalPositions(string, out int) | Gets the number of additional sets of consecutive DMRS symbols in a slot. |
| GetPuschDmrsAntennaPorts(string, out string) | Gets the antenna ports used for DMRS transmission. |
| GetPuschDmrsConfigurationType(string, out RFmxNRMXPuschDmrsConfigurationType) | Gets the configuration type of DMRS. |
| GetPuschDmrsDuration(string, out RFmxNRMXPuschDmrsDuration) | Gets whether the DMRS is single-symbol or double-symbol. |
| GetPuschDmrsGroupHoppingEnabled(string, out RFmxNRMXPuschDmrsGroupHoppingEnabled) | Gets whether the group hopping is enabled. This method is valid only when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to True. |
| GetPuschDmrsNscid(string, out int) | Gets the value of PUSCH DMRS nSCID used for reference signal generation. This method is valid only when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to False. |
| GetPuschDmrsNumberOfCdmGroups(string, out int) | Gets the number of CDM groups, when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to False, otherwise it is coerced to 2. |
| GetPuschDmrsPower(string, out double) | Gets the factor which boosts the PUSCH DMRS REs. This value is expressed in dB. This method is ignored if you set the SetPuschDmrsPowerMode(string, RFmxNRMXPuschDmrsPowerMode) method to CdmGroups. |
| GetPuschDmrsPowerMode(string, out RFmxNRMXPuschDmrsPowerMode) | Gets whether the value of SetPuschDmrsPower(string, double) method is calculated based on the SetPuschDmrsNumberOfCdmGroups(string, int) method or specified by you. |
| GetPuschDmrsPuschID(string, out int) | Gets the value of PUSCH DMRS PUSCH ID used for reference signal generation. This method is valid only when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to True and SetPuschDmrsPuschIDMode(string, RFmxNRMXPuschDmrsPuschIDMode) method to UserDefined. |
| GetPuschDmrsPuschIDMode(string, out RFmxNRMXPuschDmrsPuschIDMode) | Gets whether PUSCH DMRS PUSCH ID is based on SetCellID(string, int) or specified by you. This method is valid only when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to True. |
| GetPuschDmrsReleaseVersion(string, out RFmxNRMXPuschDmrsReleaseVersion) | Gets the 3GGP release version for PUSCH DMRS. |
| GetPuschDmrsScramblingID(string, out int) | Gets the value of scrambling ID. This method is valid only when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to False. |
| GetPuschDmrsScramblingIDMode(string, out RFmxNRMXPuschDmrsScramblingIDMode) | Gets whether the configured Scrambling ID is honored or the Cell ID is used for reference signal generation. |
| GetPuschDmrsSequenceHoppingEnabled(string, out RFmxNRMXPuschDmrsSequenceHoppingEnabled) | Gets whether the sequence hopping is enabled. This method is valid only when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to True. |
| GetPuschDmrsTypeAPosition(string, out int) | Gets the position of first DMRS symbol in a slot when you set the SetPuschMappingType(string, RFmxNRMXPuschMappingType) method to TypeA. |
| GetPuschMappingType(string, out RFmxNRMXPuschMappingType) | Gets the mapping type of DMRS. |
| GetPuschModulationType(string, out RFmxNRMXPuschModulationType) | Gets the modulation scheme used in the physical uplink shared channel (PUSCH) of the signal being measured. |
| GetPuschNumberOfResourceBlockClusters(string, out int) | Gets the number of clusters of resource allocations with each cluster including one or more consecutive resource blocks. This method is ignored if you set the SetAutoResourceBlockDetectionEnabled(string, RFmxNRMXAutoResourceBlockDetectionEnabled) method to True. |
| GetPuschNumberOfResourceBlocks(string, out int) | Gets the number of consecutive resource blocks in a physical uplink shared channel (PUSCH) cluster. This method is ignored if you set the SetAutoResourceBlockDetectionEnabled(string, RFmxNRMXAutoResourceBlockDetectionEnabled) method to True. |
| GetPuschPtrsAntennaPorts(string, out string) | Gets the DMRS antenna ports associated with PTRS transmission. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True. |
| GetPuschPtrsEnabled(string, out RFmxNRMXPuschPtrsEnabled) | Gets whether the PUSCH transmission contains PTRS signals. |
| GetPuschPtrsFrequencyDensity(string, out int) | Gets the density of PTRS in frequency domain. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True and SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to False. |
| GetPuschPtrsPower(string, out double) | Gets the factor by which the PUSCH PTRS REs are boosted. This value is expressed in dB. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True. |
| GetPuschPtrsPowerMode(string, out RFmxNRMXPuschPtrsPowerMode) | Gets whether the PUSCH PTRS power scaling is calculated as defined in 3GPP specification or specified by you. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True. |
| GetPuschPtrsREOffset(string, out int) | Gets the RE offset to be used for transmission of PTRS as defined in the Table 6.4.1.2.2.1-1 of 3GPP 38.211 specification. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True and SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to False. |
| GetPuschPtrsTimeDensity(string, out int) | Gets the density of PTRS in time domain. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True. |
| GetPuschResourceBlockOffset(string, out int) | Gets the starting resource block number of a PUSCH cluster. This method is ignored if you set the SetAutoResourceBlockDetectionEnabled(string, RFmxNRMXAutoResourceBlockDetectionEnabled) method to True. |
| GetPuschSlotAllocation(string, out string) | Gets the slot allocation in NR Frame. This defines the indices of the allocated slots. |
| GetPuschSymbolAllocation(string, out string) | Gets the symbol allocation of each slot allocation. |
| GetPuschTransformPrecodingEnabled(string, out RFmxNRMXPuschTransformPrecodingEnabled) | Gets whether transform precoding is enabled. Enable transform precoding when analyzing a DFT-s-OFDM waveform. |
| GetRadioAccessType(string, out RFmxNRMXComponentCarrierRadioAccessType) | Gets if a carrier is a NR or an E-UTRA carrier while using dual connectivity (EN-DC) signal. |
| GetRatedEirp(string, out double) | Gets the rated carrier EIRP output power. This value is expressed in dBm. |
| GetRatedTrp(string, out double) | Gets the rated carrier TRP output power. This value is expressed in dBm. |
| GetReferenceGridSize(string, out int) | Gets the reference resource grid size when you set the SetGridSizeMode(string, RFmxNRMXGridSizeMode) method to Manual. |
| GetReferenceGridStart(string, out int) | Gets the reference resource grid start relative to Reference Point A in terms of resource block offset when you set the Reference Grid Alignment Mode method to Manual. Center of subcarrier 0 in common resource block 0 is considered as Reference Point A. |
| GetReferenceGridSubcarrierSpacing(string, out double) | Gets the subcarrier spacing of the reference resource grid when you set the Reference Grid Alignment Mode method to Manual. This should be the largest subcarrier spacing used in the component carrier. This value is expressed in Hz. |
| GetRnti(string, out int) | Gets the RNTI. |
| GetSamplesPerPtrsGroup(string, out int) | Gets the number of samples per each PTRS group. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True and SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to True. |
| GetSsbActiveBlocks(string, out string) | Gets the SSB burst(s) indices for the SSB pattern that needs to be transmitted. |
| GetSsbCrbOffset(string, out int) | Gets the CRB offset for the SS/PBCH block relative to the reference Point A in units of 15 kHz or 60 kHz resource blocks for frequency range 1 and frequency range 2 respectively. |
| GetSsbEnabled(string, out RFmxNRMXSsbEnabled) | Gets whether synchronization signal block (SSB) is present in the transmitted signal. |
| GetSsbGridSize(string, out int) | Gets the SSB resource grid size when you set the SetGridSizeMode(string, RFmxNRMXGridSizeMode) method to Manual. |
| GetSsbGridStart(string, out int) | Gets the SSB resource grid start relative to Reference Point A in terms of resource block offset. |
| GetSsbHrfIndex(string, out int) | Gets the half radio frame in which the SS/PBCH block should be allocated. |
| GetSsbPattern(string, out RFmxNRMXSsbPattern) | Gets the candidate SS/PBCH blocks with different subcarrier spacing configurations as defined in the section 4.1 of 3GPP TS 38.213 specification. In order to configure Case C up to 1.88GHz unpaired spectrum, configure this method to CaseCUpTo3GHz. Similarly, to configure Case C 1.88GHz to 6GHz unpaired spectrum, configure this method to CaseC3GHzTo6GHz. |
| GetSsbPeriodicity(string, out double) | Gets the time difference with which the SS/PBCH block transmit pattern repeats. |
| GetSsbSubcarrierOffset(string, out int) | Gets an additional subcarrier offset for the SS/PBCH block in units of resource blocks of 15 kHz or subcarrier spacing given by SSB Subcarrier Common method for frequency range 1 and frequency range 2 respectively. |
| GetSssPower(string, out double) | Gets the power scaling value for the secondary synchronization symbol in the SS/PBCH block. This value is expressed in dB. |
| GetSubBandAllocation(string, out string) | Gets the sub-band allocation in the NR-U wideband channel. |
| GetSubcarrierSpacingCommon(string, out double) | Gets the basic unit of SetSsbSubcarrierOffset(string, int) method for frequency range 2. The method refers to the MIB control element subCarrierSpacingCommon in 3GPP TS 38.331. |
| SetAllocated(string, RFmxNRMXComponentCarrierAllocated) | Sets whether a component carrier has one or more resource elements allocated. While performing IBE measurement on a subblock, you set this method to False for all secondary component carriers as specified in section 6.4A.2.3 of 3GPP 38.521-1 and 3GPP 38.521-2 specifications. |
| SetBandwidth(string, double) | Sets the channel bandwidth of the signal being measured. This value is expressed in Hz. |
| SetBandwidthPartCyclicPrefixMode(string, RFmxNRMXBandwidthPartCyclicPrefixMode) | Sets the cyclic prefix (CP) duration and the number of symbols in a slot for the signal being measured. |
| SetBandwidthPartDCLocationKnown(string, RFmxNRMXBandwidthPartDCLocationKnown) | Sets whether Uplink Tx Direct Current location within the carrier is determined. If set to False, DC location is undetermined within the carrier. In ModAcc measurement, IQ impairments are not estimated and compensated, and only General In-Band Emission limits are applied. If set to True, DC location is determined within the carrier. This property is not supported when Link Direction property is set to Downlink. Use "bwp(m)" or "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)/bwp(m)" as the Selector Strings to configure or read this property. |
| SetBandwidthPartNumberOfResourceBlocks(string, int) | Sets the number of consecutive resource blocks in a bandwidth part. |
| SetBandwidthPartResourceBlockOffset(string, int) | Sets the resource block offset of a bandwidth part relative to the resource SetGridStart(string, int) method. |
| SetBandwidthPartSubcarrierSpacing(string, double) | Sets the subcarrier spacing of the bandwidth part used in the component carrier. |
| SetCellID(string, int) | Sets a physical layer cell identity. |
| SetCoresetCceToRegMappingType(string, RFmxNRMXCoresetCceToRegMappingType) | Sets the CCE-to-REG mapping type of CORESET. |
| SetCoresetInterleaverSize(string, int) | Sets the interleaver size of CORESET for interleaved CCE to REG mapping. |
| SetCoresetNumberOfResourceBlockClusters(string, int) | Sets the number of RB clusters present in the CORESET. |
| SetCoresetNumberOfResourceBlocks(string, int) | Sets the number of consecutive resource blocks of CORESET cluster. |
| SetCoresetNumberOfSymbols(string, int) | Sets the number of symbols alloted to CORESET in each slot. |
| SetCoresetPrecodingGranularity(string, RFmxNRMXCoresetPrecodingGranularity) | Sets the precoding granularity of the CORESET. |
| SetCoresetRegBundleSize(string, int) | Sets the RBG bundle size of CORESET for interleaved CCE to REG mapping. |
| SetCoresetResourceBlockOffset(string, int) | Sets the starting resource block of a CORESET cluster. |
| SetCoresetShiftIndex(string, int) | Sets the shift index of CORESET for interleaved CCE to REG mapping. |
| SetCoresetSymbolOffset(string, int) | Sets the starting symbol number of the CORESET within a slot. |
| SetDownlinkTestModel(string, RFmxNRMXDownlinkTestModel) | Sets the NR test model type when you set the Channel Configuration Mode method to Test Model. Refer to section 4.9.2 of the 3GPP 38.141 specification for more information regarding test model configurations. |
| SetDownlinkTestModelDuplexScheme(string, RFmxNRMXDownlinkTestModelDuplexScheme) | Sets the duplexing technique of the signal being measured. Refer to section 4.9.2 of 3GPP 38.141 specification for more information regarding test model configurations based on duplex scheme. |
| SetDownlinkTestModelModulationType(string, RFmxNRMXDownlinkTestModelModulationType) | Sets the modulation type to be used with the selected test model. Selecting the modulation type is supported only for test models NR-FR2-TM3.1 and NR-FR2-TM2. |
| SetEpreRatioPort(string, int) | Sets the EPRE Ratio Port used to determine the PDSCH PT-RS RE power scaling as defined in the Table 4.1-2 of 3GPP TS 38.214 specification when you set the PDSCH PTRS Power Mode method to Standard. |
| SetFrequency(string, double) | Sets the offset of the component carrier from the subblock center frequency that you configure in the Center Frequency method. This value is expressed in Hz. |
| SetGridSize(string, int) | Sets the reference resource grid size when you set the SetGridSizeMode(string, RFmxNRMXGridSizeMode) method to Manual. |
| SetGridStart(string, int) | Sets the resource grid start relative to Reference Point A in terms of resource block offset when you set the Reference Grid Alignment Mode method to Manual. |
| SetNumberOfBandwidthParts(string, int) | Sets the number of bandwidth parts present in the component carrier. |
| SetNumberOfComponentCarriers(string, int) | Sets the number of component carriers configured within a subblock. Set this method to 1 for single carrier. |
| SetNumberOfCoresets(string, int) | Sets the number of CORSETs present in the bandwidth part. |
| SetNumberOfPdcchConfigurations(string, int) | Sets the number of PDCCH Configurations for a CORESET. |
| SetNumberOfPdschConfigurations(string, int) | Sets the number of PDSCH slot configurations. |
| SetNumberOfPtrsGroups(string, int) | Sets the number of PTRS groups per OFDM symbol. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True and SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to True. |
| SetNumberOfPuschConfigurations(string, int) | Sets the number of PUSCH slot configurations. |
| SetNumberOfUsers(string, int) | Sets the number of users present in the bandwidth part. |
| SetPbchDmrsPower(string, double) | Sets the power scaling value for the PBCH DMRS symbols in the SS/PBCH block. This value is expressed in dB. |
| SetPbchPower(string, double) | Sets the power scaling value for the PBCH REs in the SS/PBCH block. This value is expressed in dB. |
| SetPdcchCceAggregationLevel(string, int) | Sets the CCE aggregation level of PDCCH. |
| SetPdcchCceOffset(string, int) | Sets the PDCCH CCE offset. |
| SetPdcchSlotAllocation(string, string) | Sets the slot allocation in NR frame. This defines the indices of the allocated slots. |
| SetPdschDmrsAdditionalPositions(string, int) | Sets the number of additional sets of consecutive DMRS symbols in a slot. |
| SetPdschDmrsAntennaPorts(string, string) | Sets the antenna ports used for DMRS transmission. |
| SetPdschDmrsConfigurationType(string, RFmxNRMXPdschDmrsConfigurationType) | Sets the configuration type of DMRS. |
| SetPdschDmrsDuration(string, RFmxNRMXPdschDmrsDuration) | Sets whether the DMRS is single-symbol or double-symbol. |
| SetPdschDmrsnScid(string, int) | Sets the value of PDSCH DMRS nSCID used for reference signal generation. |
| SetPdschDmrsNumberOfCdmGroups(string, int) | Sets the number of CDM groups. |
| SetPdschDmrsPower(string, double) | Sets the factor by which the PDSCH DMRS REs are boosted. This value is expressed in dB. |
| SetPdschDmrsPowerMode(string, RFmxNRMXPdschDmrsPowerMode) | Sets whether the configured SetPdschDmrsPower(string, double) is calculated based on the SetPdschDmrsNumberOfCdmGroups(string, int) or specified by you. |
| SetPdschDmrsReleaseVersion(string, RFmxNRMXPdschDmrsReleaseVersion) | Sets the 3GGP release version for PDSCH DMRS. |
| SetPdschDmrsScramblingID(string, int) | Sets the value of scrambling ID used for reference signal generation. |
| SetPdschDmrsScramblingIDMode(string, RFmxNRMXPdschDmrsScramblingIDMode) | Sets whether the configured Scrambling ID is based on SetCellID(string, int) or specified by you. |
| SetPdschDmrsTypeAPosition(string, int) | Sets the position of first DMRS symbol in a slot for Type A configurations. |
| SetPdschMappingType(string, RFmxNRMXPdschMappingType) | Sets the mapping type of DMRS. |
| SetPdschModulationType(string, RFmxNRMXPdschModulationType) | Sets the modulation scheme used in PDSCH channel of the signal being measured. |
| SetPdschNumberOfResourceBlockClusters(string, int) | Sets the number of clusters of resource allocations with each cluster including one or more consecutive resource blocks. |
| SetPdschNumberOfResourceBlocks(string, int) | Sets the number of consecutive resource blocks in a PDSCH cluster. |
| SetPdschPtrsAntennaPorts(string, string) | Sets the DMRS Antenna Ports associated with PTRS transmission. |
| SetPdschPtrsEnabled(string, RFmxNRMXPdschPtrsEnabled) | Sets whether PT-RS is present in the transmitted signal. |
| SetPdschPtrsFrequencyDensity(string, int) | Sets the density of PTRS in frequency domain. |
| SetPdschPtrsPower(string, double) | Sets the factor by which the PDSCH PTRS REs are boosted, compared to PDSCH REs. This value is expressed in dB. The value of this method is taken as an input when you set the SetPdschPtrsPowerMode(string, RFmxNRMXPdschPtrsPowerMode) method to UserDefined. If you set the PDSCH PTRS Pwr Mode method to Standard, the value is computed from other parameters. |
| SetPdschPtrsPowerMode(string, RFmxNRMXPdschPtrsPowerMode) | Sets whether the configured SetPdschPtrsPower(string, double) is calculated as defined in 3GPP specification or configured by you. |
| SetPdschPtrsREOffset(string, int) | Sets the RE Offset to be used for transmission of PTRS as defined in Table 7.4.1.2.2-1 of 3GPP 38.211 specification. |
| SetPdschPtrsTimeDensity(string, int) | Sets the density of PTRS in time domain. |
| SetPdschResourceBlockOffset(string, int) | Sets the starting resource block number of a PDSCH cluster. |
| SetPdschSlotAllocation(string, string) | Sets the slot allocation in NR Frame. This defines the indices of the allocated slots. |
| SetPdschSymbolAllocation(string, string) | Sets the symbol allocation of each slot allocation. |
| SetPssPower(string, double) | Sets the power scaling value for the primary synchronization symbol in the SS/PBCH block. This value is expressed in dB. |
| SetPuschDmrsAdditionalPositions(string, int) | Sets the number of additional sets of consecutive DMRS symbols in a slot. |
| SetPuschDmrsAntennaPorts(string, string) | Sets the antenna ports used for DMRS transmission. |
| SetPuschDmrsConfigurationType(string, RFmxNRMXPuschDmrsConfigurationType) | Sets the configuration type of DMRS. |
| SetPuschDmrsDuration(string, RFmxNRMXPuschDmrsDuration) | Sets whether the DMRS is single-symbol or double-symbol. |
| SetPuschDmrsGroupHoppingEnabled(string, RFmxNRMXPuschDmrsGroupHoppingEnabled) | Sets whether the group hopping is enabled. This method is valid only when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to True. |
| SetPuschDmrsNscid(string, int) | Sets the value of PUSCH DMRS nSCID used for reference signal generation. This method is valid only when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to False. |
| SetPuschDmrsNumberOfCdmGroups(string, int) | Sets the number of CDM groups, when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to False, otherwise it is coerced to 2. |
| SetPuschDmrsPower(string, double) | Sets the factor which boosts the PUSCH DMRS REs. This value is expressed in dB. This method is ignored if you set the SetPuschDmrsPowerMode(string, RFmxNRMXPuschDmrsPowerMode) method to CdmGroups. |
| SetPuschDmrsPowerMode(string, RFmxNRMXPuschDmrsPowerMode) | Sets whether the value of SetPuschDmrsPower(string, double) method is calculated based on the SetPuschDmrsNumberOfCdmGroups(string, int) method or specified by you. |
| SetPuschDmrsPuschID(string, int) | Sets the value of PUSCH DMRS PUSCH ID used for reference signal generation. This method is valid only when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to True and SetPuschDmrsPuschIDMode(string, RFmxNRMXPuschDmrsPuschIDMode) method to UserDefined. |
| SetPuschDmrsPuschIDMode(string, RFmxNRMXPuschDmrsPuschIDMode) | Sets whether PUSCH DMRS PUSCH ID is based on SetCellID(string, int) or specified by you. This method is valid only when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to True. |
| SetPuschDmrsReleaseVersion(string, RFmxNRMXPuschDmrsReleaseVersion) | Sets the 3GGP release version for PUSCH DMRS. |
| SetPuschDmrsScramblingID(string, int) | Sets the value of scrambling ID. This method is valid only when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to False. |
| SetPuschDmrsScramblingIDMode(string, RFmxNRMXPuschDmrsScramblingIDMode) | Sets whether the configured Scrambling ID is honored or the Cell ID is used for reference signal generation. |
| SetPuschDmrsSequenceHoppingEnabled(string, RFmxNRMXPuschDmrsSequenceHoppingEnabled) | Sets whether the sequence hopping is enabled. This method is valid only when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to True. |
| SetPuschDmrsTypeAPosition(string, int) | Sets the position of first DMRS symbol in a slot when you set the SetPuschMappingType(string, RFmxNRMXPuschMappingType) method to TypeA. |
| SetPuschMappingType(string, RFmxNRMXPuschMappingType) | Sets the mapping type of DMRS. |
| SetPuschModulationType(string, RFmxNRMXPuschModulationType) | Sets the modulation scheme used in the physical uplink shared channel (PUSCH) of the signal being measured. |
| SetPuschNumberOfResourceBlockClusters(string, int) | Sets the number of clusters of resource allocations with each cluster including one or more consecutive resource blocks. This method is ignored if you set the SetAutoResourceBlockDetectionEnabled(string, RFmxNRMXAutoResourceBlockDetectionEnabled) method to True. |
| SetPuschNumberOfResourceBlocks(string, int) | Sets the number of consecutive resource blocks in a physical uplink shared channel (PUSCH) cluster. This method is ignored if you set the SetAutoResourceBlockDetectionEnabled(string, RFmxNRMXAutoResourceBlockDetectionEnabled) method to True. |
| SetPuschPtrsAntennaPorts(string, string) | Sets the DMRS antenna ports associated with PTRS transmission. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True. |
| SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) | Sets whether the PUSCH transmission contains PTRS signals. |
| SetPuschPtrsFrequencyDensity(string, int) | Sets the density of PTRS in frequency domain. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True and SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to False. |
| SetPuschPtrsPower(string, double) | Sets the factor by which the PUSCH PTRS REs are boosted. This value is expressed in dB. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True. |
| SetPuschPtrsPowerMode(string, RFmxNRMXPuschPtrsPowerMode) | Sets whether the PUSCH PTRS power scaling is calculated as defined in 3GPP specification or specified by you. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True. |
| SetPuschPtrsREOffset(string, int) | Sets the RE offset to be used for transmission of PTRS as defined in the Table 6.4.1.2.2.1-1 of 3GPP 38.211 specification. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True and SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to False. |
| SetPuschPtrsTimeDensity(string, int) | Sets the density of PTRS in time domain. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True. |
| SetPuschResourceBlockOffset(string, int) | Sets the starting resource block number of a PUSCH cluster. This method is ignored if you set the SetAutoResourceBlockDetectionEnabled(string, RFmxNRMXAutoResourceBlockDetectionEnabled) method to True. |
| SetPuschSlotAllocation(string, string) | Sets the slot allocation in NR Frame. This defines the indices of the allocated slots. |
| SetPuschSymbolAllocation(string, string) | Sets the symbol allocation of each slot allocation. |
| SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) | Sets whether transform precoding is enabled. Enable transform precoding when analyzing a DFT-s-OFDM waveform. |
| SetRadioAccessType(string, RFmxNRMXComponentCarrierRadioAccessType) | Sets if a carrier is a NR or an E-UTRA carrier while using dual connectivity (EN-DC) signal. |
| SetRatedEirp(string, double) | Sets the rated carrier EIRP output power. This value is expressed in dBm. |
| SetRatedTrp(string, double) | Sets the rated carrier TRP output power. This value is expressed in dBm. |
| SetReferenceGridSize(string, int) | Sets the reference resource grid size when you set the SetGridSizeMode(string, RFmxNRMXGridSizeMode) method to Manual. |
| SetReferenceGridStart(string, int) | Sets the reference resource grid start relative to Reference Point A in terms of resource block offset when you set the Reference Grid Alignment Mode method to Manual. Center of subcarrier 0 in common resource block 0 is considered as Reference Point A. |
| SetReferenceGridSubcarrierSpacing(string, double) | Sets the subcarrier spacing of the reference resource grid when you set the Reference Grid Alignment Mode method to Manual. This should be the largest subcarrier spacing used in the component carrier. This value is expressed in Hz. |
| SetRnti(string, int) | Sets the RNTI. |
| SetSamplesPerPtrsGroup(string, int) | Sets the number of samples per each PTRS group. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True and SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to True. |
| SetSsbActiveBlocks(string, string) | Sets the SSB burst(s) indices for the SSB pattern that needs to be transmitted. |
| SetSsbCrbOffset(string, int) | Sets the CRB offset for the SS/PBCH block relative to the reference Point A in units of 15 kHz or 60 kHz resource blocks for frequency range 1 and frequency range 2 respectively. |
| SetSsbEnabled(string, RFmxNRMXSsbEnabled) | Sets whether synchronization signal block (SSB) is present in the transmitted signal. |
| SetSsbGridSize(string, int) | Sets the SSB resource grid size when you set the SetGridSizeMode(string, RFmxNRMXGridSizeMode) method to Manual. |
| SetSsbGridStart(string, int) | Sets the SSB resource grid start relative to Reference Point A in terms of resource block offset. |
| SetSsbHrfIndex(string, int) | Sets the half radio frame in which the SS/PBCH block should be allocated. |
| SetSsbPattern(string, RFmxNRMXSsbPattern) | Sets the candidate SS/PBCH blocks with different subcarrier spacing configurations as defined in the section 4.1 of 3GPP TS 38.213 specification. In order to configure Case C up to 1.88GHz unpaired spectrum, configure this method to CaseCUpTo3GHz. Similarly, to configure Case C 1.88GHz to 6GHz unpaired spectrum, configure this method to CaseC3GHzTo6GHz. |
| SetSsbPeriodicity(string, double) | Sets the time difference with which the SS/PBCH block transmit pattern repeats. |
| SetSsbSubcarrierOffset(string, int) | Sets an additional subcarrier offset for the SS/PBCH block in units of resource blocks of 15 kHz or subcarrier spacing given by SSB Subcarrier Common method for frequency range 1 and frequency range 2 respectively. |
| SetSssPower(string, double) | Sets the power scaling value for the secondary synchronization symbol in the SS/PBCH block. This value is expressed in dB. |
| SetSubBandAllocation(string, string) | Sets the sub-band allocation in the NR-U wideband channel. |
| SetSubcarrierSpacingCommon(string, double) | Sets the basic unit of SetSsbSubcarrierOffset(string, int) method for frequency range 2. The method refers to the MIB control element subCarrierSpacingCommon in 3GPP TS 38.331. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrierallocated.html language=enus -->
## TOPIC 00215: RFmxNRMXComponentCarrierAllocated Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrierallocated.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcomponentcarrierallocated.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether a component carrier has one or more resource elements allocated. While performing IBE measurement on a subblock, you set this method to False for all secondary component carriers as specified in section 6.4A.2.3 of 3GPP 38.521-1 and 3GPP 38.521-2 specifications. SyntaxNamespace: Na

### RFmxNRMXComponentCarrierAllocated Enumeration

Specifies whether a component carrier has one or more resource elements allocated. While performing IBE measurement on a subblock, you set this method to False for all secondary component carriers as specified in section 6.4A.2.3 of *3GPP 38.521-1* and *3GPP 38.521-2* specifications.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXComponentCarrierAllocated

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | No resource elements are allocated for the component carrier. Only subblock IBE is computed. |
| True | 1 | One or more resource elements are allocated for the component carrier. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-diopfi0.html language=enus -->
## TOPIC 00216: DioPfi0

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-diopfi0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-diopfi0.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic const string DioPfi0

### DioPfi0

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public const string DioPfi0

Parent topic:

RFmxNRMXConstants Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-diopfi2.html language=enus -->
## TOPIC 00217: DioPfi2

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-diopfi2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-diopfi2.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic const string DioPfi2

### DioPfi2

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public const string DioPfi2

Parent topic:

RFmxNRMXConstants Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-diopfi4.html language=enus -->
## TOPIC 00218: DioPfi4

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-diopfi4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-diopfi4.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic const string DioPfi4

### DioPfi4

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public const string DioPfi4

Parent topic:

RFmxNRMXConstants Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-diopfi5.html language=enus -->
## TOPIC 00219: DioPfi5

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-diopfi5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-diopfi5.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic const string DioPfi5

### DioPfi5

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public const string DioPfi5

Parent topic:

RFmxNRMXConstants Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-diopfi6.html language=enus -->
## TOPIC 00220: DioPfi6

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-diopfi6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-diopfi6.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic const string DioPfi6

### DioPfi6

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public const string DioPfi6

Parent topic:

RFmxNRMXConstants Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-diopfi7.html language=enus -->
## TOPIC 00221: DioPfi7

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-diopfi7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-diopfi7.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic const string DioPfi7

### DioPfi7

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public const string DioPfi7

Parent topic:

RFmxNRMXConstants Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-pfi0.html language=enus -->
## TOPIC 00222: Pfi0

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-pfi0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-pfi0.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PFI 0. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic const string Pfi0

### Pfi0

The signal is exported to the PFI 0.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public const string Pfi0

Parent topic:

RFmxNRMXConstants Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-pfi1.html language=enus -->
## TOPIC 00223: Pfi1

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-pfi1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-pfi1.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI 1. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic const string Pfi1

### Pfi1

The signal is exported to the PXI 1.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public const string Pfi1

Parent topic:

RFmxNRMXConstants Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-pxiedstarbline.html language=enus -->
## TOPIC 00224: PxieDStarBLine

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-pxiedstarbline.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-pxiedstarbline.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXIe DStar B trigger line. This value is valid only for PXIe-5820/5830/5831/5840/5841. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic const string PxieDStarBLine

### PxieDStarBLine

The signal is exported to the PXIe DStar B trigger line. This value is valid only for PXIe-5820/5830/5831/5840/5841.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public const string PxieDStarBLine

Parent topic:

RFmxNRMXConstants Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-pxitriggerline1.html language=enus -->
## TOPIC 00225: PxiTriggerLine1

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-pxitriggerline1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-pxitriggerline1.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 1. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic const string PxiTriggerLine1

### PxiTriggerLine1

The signal is exported to the PXI trigger line 1.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public const string PxiTriggerLine1

Parent topic:

RFmxNRMXConstants Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-pxitriggerline2.html language=enus -->
## TOPIC 00226: PxiTriggerLine2

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-pxitriggerline2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-pxitriggerline2.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 2. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic const string PxiTriggerLine2

### PxiTriggerLine2

The signal is exported to the PXI trigger line 2.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public const string PxiTriggerLine2

Parent topic:

RFmxNRMXConstants Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-pxitriggerline5.html language=enus -->
## TOPIC 00227: PxiTriggerLine5

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-pxitriggerline5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-pxitriggerline5.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 5. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic const string PxiTriggerLine5

### PxiTriggerLine5

The signal is exported to the PXI trigger line 5.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public const string PxiTriggerLine5

Parent topic:

RFmxNRMXConstants Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-pxitriggerline6.html language=enus -->
## TOPIC 00228: PxiTriggerLine6

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-pxitriggerline6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-pxitriggerline6.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 6. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic const string PxiTriggerLine6

### PxiTriggerLine6

The signal is exported to the PXI trigger line 6.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public const string PxiTriggerLine6

Parent topic:

RFmxNRMXConstants Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-pxitriggerline7.html language=enus -->
## TOPIC 00229: PxiTriggerLine7

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-pxitriggerline7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-pxitriggerline7.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 7. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic const string PxiTriggerLine7

### PxiTriggerLine7

The signal is exported to the PXI trigger line 7.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public const string PxiTriggerLine7

Parent topic:

RFmxNRMXConstants Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-timerevent.html language=enus -->
## TOPIC 00230: TimerEvent

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-timerevent.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxconstants-timerevent.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The trigger is received from the timer event. This value is valid only for PXIe-5820/5840/5841 and for digital edge advance triggers on PXIe-5663E/5665. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic const string TimerEvent

### TimerEvent

The trigger is received from the timer event. This value is valid only for PXIe-5820/5840/5841 and for digital edge advance triggers on PXIe-5663E/5665.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public const string TimerEvent

Parent topic:

RFmxNRMXConstants Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxconstants.html language=enus -->
## TOPIC 00231: RFmxNRMXConstants Class

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxconstants.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxconstants.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies constants for I/O terminals. Derives fromNoneSyntaxNamespace: NationalInstruments.RFmx.NRMXpublic class RFmxNRMXConstantsFieldsNameDescriptionDioPfi0DioPfi1DioPfi2DioPfi3DioPfi4DioPfi5DioPfi6DioPfi7Pfi0The signal is exported to the PFI 0. Pfi1The signal is exported to the PXI 1. PulseInPxi

### RFmxNRMXConstants Class

Specifies constants for I/O terminals.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public class RFmxNRMXConstants

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

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcoresetccetoregmappingtype.html language=enus -->
## TOPIC 00232: RFmxNRMXCoresetCceToRegMappingType Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcoresetccetoregmappingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcoresetccetoregmappingtype.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the CCE-to-REG mapping type of CORESET. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXCoresetCceToRegMappingTypeMembersNameValueDescriptionNonInterleaved0Mapping type is non-interleaved. Interleaved1Mapping type is interleaved.

### RFmxNRMXCoresetCceToRegMappingType Enumeration

Specifies the CCE-to-REG mapping type of CORESET.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXCoresetCceToRegMappingType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| NonInterleaved | 0 | Mapping type is non-interleaved. |
| Interleaved | 1 | Mapping type is interleaved. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxcoresetprecodinggranularity.html language=enus -->
## TOPIC 00233: RFmxNRMXCoresetPrecodingGranularity Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxcoresetprecodinggranularity.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxcoresetprecodinggranularity.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the precoding granularity of the CORESET. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXCoresetPrecodingGranularityMembersNameValueDescriptionSameAsRegBundle0Precoding granularity is set to Same As REG Bundle. AllContiguousResourceBlocks1Precoding granularity is set to

### RFmxNRMXCoresetPrecodingGranularity Enumeration

Specifies the precoding granularity of the CORESET.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXCoresetPrecodingGranularity

#### Members

| Name | Value | Description |
| --- | --- | --- |
| SameAsRegBundle | 0 | Precoding granularity is set to Same As REG Bundle. |
| AllContiguousResourceBlocks | 1 | Precoding granularity is set to All Contiguous Resource Blocks. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxdigitaledgetriggeredge.html language=enus -->
## TOPIC 00234: RFmxNRMXDigitalEdgeTriggerEdge Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxdigitaledgetriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxdigitaledgetriggeredge.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxNRMXTriggerType) method to DigitalEdge. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXDigitalEdgeTriggerEdgeMembersNameValueDescriptionRising0The trigger asserts on the

### RFmxNRMXDigitalEdgeTriggerEdge Enumeration

Specifies the active edge for the trigger. This method is used only when you set the [SetTriggerType(string, RFmxNRMXTriggerType)](nationalinstruments-rfmx-nrmx-rfmxnrmx-settriggertype__string-rfmxnrmxtriggertype.html) method to [DigitalEdge](nationalinstruments-rfmx-nrmx-rfmxnrmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXDigitalEdgeTriggerEdge

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 0 | The trigger asserts on the rising edge of the signal. |
| Falling | 1 | The trigger asserts on the falling edge of the signal. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxdownlinktestmodel.html language=enus -->
## TOPIC 00235: RFmxNRMXDownlinkTestModel Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxdownlinktestmodel.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxdownlinktestmodel.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the NR test model type when you set the Channel Configuration Mode method to Test Model. Refer to section 4.9.2 of the 3GPP 38.141 specification for more information regarding test model configurations. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXDownlinkTestModelMemb

### RFmxNRMXDownlinkTestModel Enumeration

Specifies the NR test model type when you set the Channel Configuration Mode method to Test Model. Refer to section 4.9.2 of the *3GPP 38.141* specification for more information regarding test model configurations.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXDownlinkTestModel

#### Members

| Name | Value | Description |
| --- | --- | --- |
| TM1_1 | 0 | Specifies a TM1.1 NR test model. |
| TM1_2 | 1 | Specifies a TM1.2 NR test model. |
| TM2 | 2 | Specifies a TM2 NR test model. |
| TM2a | 3 | Specifies a TM2a NR test model. |
| TM3_1 | 4 | Specifies a TM3.1 NR test model. |
| TM3_1a | 5 | Specifies a TM3.1a NR test model. |
| TM3_2 | 6 | Specifies a TM3.2 NR test model. |
| TM3_3 | 7 | Specifies a TM3.3 NR test model. |
| TM2b | 8 | Specifies a TM2b NR test model. |
| TM3_1b | 9 | Specifies a TM3.1b NR test model. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxiqpoweredgetriggerleveltype.html language=enus -->
## TOPIC 00236: RFmxNRMXIQPowerEdgeTriggerLevelType Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxiqpoweredgetriggerleveltype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxiqpoweredgetriggerleveltype.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(string, RFmxNRMXTriggerType) method to IQPowerEdge. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXIQPowerEdgeTrigger

### RFmxNRMXIQPowerEdgeTriggerLevelType Enumeration

Specifies the reference for the [SetIQPowerEdgeTriggerLevel(string, double)](nationalinstruments-rfmx-nrmx-rfmxnrmx-setiqpoweredgetriggerlevel__string-double.html) method. The IQ Power Edge Level Type method is used only when you set the [SetTriggerType(string, RFmxNRMXTriggerType)](nationalinstruments-rfmx-nrmx-rfmxnrmx-settriggertype__string-rfmxnrmxtriggertype.html) method to [IQPowerEdge](nationalinstruments-rfmx-nrmx-rfmxnrmxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXIQPowerEdgeTriggerLevelType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Relative | 0 | The IQ Power Edge Level method is relative to the value of the SetReferenceLevel(string, double) method. |
| Absolute | 1 | The IQ Power Edge Level method specifies the absolute power. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxlimitedconfigurationchange.html language=enus -->
## TOPIC 00237: RFmxNRMXLimitedConfigurationChange Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxlimitedconfigurationchange.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxlimitedconfigurationchange.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the set of properties that are considered by RFmx in the locked signal configuration state. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXLimitedConfigurationChangeMembersNameValueDescriptionDisabled0This is the normal mode of RFmx operation. All configuration changes i

### RFmxNRMXLimitedConfigurationChange Enumeration

Specifies the set of properties that are considered by RFmx in the locked signal configuration state.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXLimitedConfigurationChange

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Disabled | 0 | This is the normal mode of RFmx operation. All configuration changes in RFmxInstr properties or in personality properties will be applied during RFmx Commit. |
| NoChange | 1 | Signal configuration is locked after the first Commit of the named signal configuration. Any configuration change thereafter either in RFmxInstr properties or personality properties will not be considered by subsequent RFmx Commits or Initiates of this signal. Use No Change if you have created named signal configurations for all measurement configurations but are setting some RFmxInstr properties. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| Frequency | 2 | Signal configuration, other than center frequency and external attenuation, is locked after first Commit of the named signal configuration. Thereafter, only the Center Frequency and SetExternalAttenuation(string, double) method value changes will be considered by subsequent driver Commits or Initiates of this signal. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| ReferenceLevel | 3 | Signal configuration, other than the reference level, is locked after first Commit of the named signal configuration. Thereafter only the SetReferenceLevel(string, double) method value change will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends that you set the SetIQPowerEdgeTriggerLevelType(string, RFmxNRMXIQPowerEdgeTriggerLevelType) to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| FrequencyAndReferenceLevel | 4 | Signal configuration, other than center frequency, reference level, and external attenuation, is locked after first Commit of the named signal configuration. Thereafter only Center Frequency, SetReferenceLevel(string, double), and SetExternalAttenuation(string, double) method value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the SetIQPowerEdgeTriggerLevelType(string, RFmxNRMXIQPowerEdgeTriggerLevelType) to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| SelectedPortsFrequencyAndReferenceLevel | 5 | Signal configuration, other than selected ports, center frequency, reference level, external attenuation, and RFInstr configuration, is locked after first Commit or Initiate of the named signal configuration. Thereafter only Selected Ports, Center Frequency, Reference Level, and External Attenuation method value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxlist-getliststeprange__int-int.html language=enus -->
## TOPIC 00238: GetListStepRange(int, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxlist-getliststeprange__int-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxlist-getliststeprange__int-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a range of list step instances in a list. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic RFmxNRMX GetListStepRange(int stepStartIndex, int stepStopIndex)ParametersNameTypeDescriptionstepStartIndexintPass the starting index of the range of list step.stepStopIndexintPass the last index o

### GetListStepRange(int, int)

Returns a range of list step instances in a list.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public [RFmxNRMX](nationalinstruments-rfmx-nrmx-rfmxnrmx.html) GetListStepRange(int stepStartIndex, int stepStopIndex)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| stepStartIndex | int | Pass the starting index of the range of list step. |
| stepStopIndex | int | Pass the last index of the range of list step. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxNRMXList Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxlist-getnumberofsteps__string-out.html language=enus -->
## TOPIC 00239: GetNumberOfSteps(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxlist-getnumberofsteps__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxlist-getnumberofsteps__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns number of list step instances in a list.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetNumberOfSteps(string selectorString, out int value)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The list name that is passed when creating the list is used.valueout i

### GetNumberOfSteps(string, out int)

Returns number of list step instances in a list.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetNumberOfSteps(string selectorString, out int value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The list name that is passed when creating the list is used. |
| value | out int | Upon return, contains the number of list step instances in a list. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxNRMXList Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxlist-initiate__string-string.html language=enus -->
## TOPIC 00240: Initiate(string, string)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxlist-initiate__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxlist-initiate__string-string.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates all enabled measurements. Call this method after configuring the list and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch methods or result methods in the method

### Initiate(string, string)

Initiates all enabled measurements. Call this method after configuring the list and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch methods or result methods in the method node. To get the status of measurements, use the [WaitForMeasurementComplete(string, double)](nationalinstruments-rfmx-nrmx-rfmxnrmxlist-waitformeasurementcomplete__string-double.html) method or [CheckMeasurementStatus(string, out bool)](nationalinstruments-rfmx-nrmx-rfmxnrmxlist-checkmeasurementstatus__string-out.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int Initiate(string selectorString, string resultName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name. The result name can either be specified through this input or the resultName parameter. If you do not specify the result name in this parameter, either the result name specified by the resultName parameter or the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| resultName | string | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. Example:"result::r1""r1" |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXList Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxlist-listtype.html language=enus -->
## TOPIC 00241: ListType

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxlist-listtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxlist-listtype.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Type object for RFmxNRMXList. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic Type ListType { get; }RemarksReturns the type of list object.

### ListType

Gets the Type object for RFmxNRMXList.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public Type ListType { get; }

#### Remarks

Returns the type of list object.

Parent topic:

RFmxNRMXList Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxlist-resettodefault__string.html language=enus -->
## TOPIC 00242: ResetToDefault(string)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxlist-resettodefault__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxlist-resettodefault__string.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a list to the default values.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int ResetToDefault(string selectorString)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The list name that is passed when creating the list is used.ReturnsReturns the status code of this

### ResetToDefault(string)

Resets a list to the default values.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int ResetToDefault(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The list name that is passed when creating the list is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXList Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxlist-setnumberofsteps__string-int.html language=enus -->
## TOPIC 00243: SetNumberOfSteps(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxlist-setnumberofsteps__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxlist-setnumberofsteps__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets number of list step instances in a list.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetNumberOfSteps(string selectorString, int value)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The list name that is passed when creating the list is used.valueintUpon retu

### SetNumberOfSteps(string, int)

Sets number of list step instances in a list.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetNumberOfSteps(string selectorString, int value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The list name that is passed when creating the list is used. |
| value | int | Upon return, contains the number of list step instances in a list. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

RFmxNRMXList Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodacc-results.html language=enus -->
## TOPIC 00244: Results

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodacc-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodacc-results.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxNRMXModAccResults instance that provides methods to fetch and read the ModAcc measurement results. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic RFmxNRMXModAccResults Results { get; }

### Results

Gets the [RFmxNRMXModAccResults](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults.html) instance that provides methods to fetch and read the ModAcc measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public [RFmxNRMXModAccResults](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults.html) Results { get; }

Parent topic:

RFmxNRMXModAcc Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodacc.html language=enus -->
## TOPIC 00245: RFmxNRMXModAcc Class

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodacc.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the ModAcc measurement. Derives fromRFmxNRMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.NRMXpublic class RFmxNRMXModAcc : RFmxNRMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxNRMXModAccConfiguration instance that provides methods to configure the ModAcc measurement.

### RFmxNRMXModAcc Class

Represents the ModAcc measurement.

#### Derives from

- RFmxNRMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public class RFmxNRMXModAcc : RFmxNRMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxNRMXModAccConfiguration instance that provides methods to configure the ModAcc measurement. |
| Results | Gets the RFmxNRMXModAccResults instance that provides methods to fetch and read the ModAcc measurement results. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodacccalibrationdatavalid.html language=enus -->
## TOPIC 00246: RFmxNRMXModAccCalibrationDataValid Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodacccalibrationdatavalid.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodacccalibrationdatavalid.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether the calibration data is valid. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXModAccCalibrationDataValidMembersNameValueDescriptionFalse0Calibration data is not present for the specified configuration or the difference between the current device temperature and the

### RFmxNRMXModAccCalibrationDataValid Enumeration

Returns whether the calibration data is valid.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXModAccCalibrationDataValid

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Calibration data is not present for the specified configuration or the difference between the current device temperature and the calibration temperature exceeds the [-5 °C, 5 °C] range. |
| True | 1 | The calibration data is present for the configuration specified by the signal name in the Selector string method. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodacccompositeresultsincludedmrs.html language=enus -->
## TOPIC 00247: RFmxNRMXModAccCompositeResultsIncludeDmrs Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodacccompositeresultsincludedmrs.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodacccompositeresultsincludedmrs.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the DMRS resource elements are included for composite EVM and magnitude and phase error results and traces. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXModAccCompositeResultsIncludeDmrsMembersNameValueDescriptionFalse0The DMRS resource elements are not include

### RFmxNRMXModAccCompositeResultsIncludeDmrs Enumeration

Specifies whether the DMRS resource elements are included for composite EVM and magnitude and phase error results and traces.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXModAccCompositeResultsIncludeDmrs

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The DMRS resource elements are not included. |
| True | 1 | The DMRS resource elements are included. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-clearnoisecalibrationdatabase.html language=enus -->
## TOPIC 00248: ClearNoiseCalibrationDatabase()

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-clearnoisecalibrationdatabase.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-clearnoisecalibrationdatabase.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the noise calibration database used for EVM noise compensation.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int ClearNoiseCalibrationDatabase()ReturnsReturns the status code of this method. The status code either indicates success or describes a warning condition.

### ClearNoiseCalibrationDatabase()

Clears the noise calibration database used for EVM noise compensation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int ClearNoiseCalibrationDatabase()

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-configurereferencewaveform__string-complexwaveform_complexsingle..html language=enus -->
## TOPIC 00249: ConfigureReferenceWaveform(string, ComplexWaveform< ComplexSingle >)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-configurereferencewaveform__string-complexwaveform_complexsingle..html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-configurereferencewaveform__string-complexwaveform_complexsingle..html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference waveform for the creation of reference data symbols for EVM computation. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int ConfigureReferenceWaveform(string selectorString, ComplexWaveform< ComplexSingle > referenceWaveform)ParametersNameTypeDescriptionselectorStrings

### ConfigureReferenceWaveform(string, ComplexWaveform< ComplexSingle >)

Configures the reference waveform for the creation of reference data symbols for EVM computation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int ConfigureReferenceWaveform(string selectorString, ComplexWaveform< ComplexSingle > referenceWaveform)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| referenceWaveform | ComplexWaveform< ComplexSingle > | Specifies the array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00250: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the traces to be stored and retrieved after performing the ModAcc measurement. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method gets the value of ModAccAllTracesEnabled attribute.The default v

### GetAllTracesEnabled(string, out bool)

Gets whether to enable the traces to be stored and retrieved after performing the ModAcc measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [ModAccAllTracesEnabled](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the traces to be stored and retrieved after performing the ModAcc measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class
