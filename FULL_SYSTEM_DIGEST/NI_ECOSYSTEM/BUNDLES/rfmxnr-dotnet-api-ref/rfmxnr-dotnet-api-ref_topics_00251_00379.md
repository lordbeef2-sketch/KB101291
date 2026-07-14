# NI DOCUMENT BUNDLE: rfmxnr-dotnet-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxnr-dotnet-api-ref start=251 end=379 -->
<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getautolevelallowoverflow__string-out.html language=enus -->
## TOPIC 00251: GetAutoLevelAllowOverflow(string, out RFmxNRMXModAccAutoLevelAllowOverflow)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getautolevelallowoverflow__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getautolevelallowoverflow__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the AutoLevel(string, double) function should search for the optimum reference levels while allowing ADC overflow. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetAutoLevelAllowOverflow(string selectorString, out RFmxNRMXModAccAutoLevelAllowOverflow value)RemarksThis method

### GetAutoLevelAllowOverflow(string, out RFmxNRMXModAccAutoLevelAllowOverflow)

Gets whether the [AutoLevel(string, double)](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-autolevel__string-double.html) function should search for the optimum reference levels while allowing ADC overflow.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetAutoLevelAllowOverflow(string selectorString, out RFmxNRMXModAccAutoLevelAllowOverflow value)

#### Remarks

This method gets the value of [ModAccAutoLevelAllowOverflow](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccautolevelallowoverflow.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxNRMXModAccAutoLevelAllowOverflow | Upon return, contains whether the AutoLevel(string, double) function should search for the optimum reference levels while allowing ADC overflow. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getevmreferencedatasymbolsmode__string-out.html language=enus -->
## TOPIC 00252: GetEvmReferenceDataSymbolsMode(string, out RFmxNRMXModAccEvmReferenceDataSymbolsMode)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getevmreferencedatasymbolsmode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getevmreferencedatasymbolsmode__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to either use a reference waveform or an acquired waveform to create reference data symbols for EVM computation. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetEvmReferenceDataSymbolsMode(string selectorString, out RFmxNRMXModAccEvmReferenceDataSymbolsMode value)RemarksThis

### GetEvmReferenceDataSymbolsMode(string, out RFmxNRMXModAccEvmReferenceDataSymbolsMode)

Gets whether to either use a reference waveform or an acquired waveform to create reference data symbols for EVM computation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetEvmReferenceDataSymbolsMode(string selectorString, out RFmxNRMXModAccEvmReferenceDataSymbolsMode value)

#### Remarks

This method gets the value of [ModAccEvmReferenceDataSymbolsMode](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [AcquiredWaveform](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccevmreferencedatasymbolsmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxNRMXModAccEvmReferenceDataSymbolsMode | Upon return, contains whether to either use a reference waveform or an acquired waveform to create reference data symbols for EVM computation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getevmunit__string-out.html language=enus -->
## TOPIC 00253: GetEvmUnit(string, out RFmxNRMXModAccEvmUnit)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getevmunit__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getevmunit__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the units of the EVM results. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetEvmUnit(string selectorString, out RFmxNRMXModAccEvmUnit value)RemarksThis method gets the value of ModAccEvmUnit attribute.The default value is Percentage.ParametersNameTypeDescriptionselectorStringstring

### GetEvmUnit(string, out RFmxNRMXModAccEvmUnit)

Gets the units of the EVM results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetEvmUnit(string selectorString, out RFmxNRMXModAccEvmUnit value)

#### Remarks

This method gets the value of [ModAccEvmUnit](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Percentage](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccevmunit.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxNRMXModAccEvmUnit | Upon return, contains the units of the EVM results. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getfftwindowlength__string-out.html language=enus -->
## TOPIC 00254: GetFftWindowLength(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getfftwindowlength__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getfftwindowlength__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the FFT window length (W). This value is expressed as a percentage of the cyclic prefix length. This method is used when you set the SetFftWindowType(string, RFmxNRMXModAccFftWindowType) method to Type3GPP, where it is needed to calculate the EVM using two different FFT window positions, Delta_

### GetFftWindowLength(string, out double)

Gets the FFT window length (W). This value is expressed as a percentage of the cyclic prefix length. This method is used when you set the [SetFftWindowType(string, RFmxNRMXModAccFftWindowType)](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setfftwindowtype__string-rfmxnrmxmodaccfftwindowtype.html) method to [Type3GPP](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccfftwindowtype.html), where it is needed to calculate the EVM using two different FFT window positions, Delta_C-W/2, and Delta_C+W/2.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetFftWindowLength(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccFftWindowLength](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is -1. Valid values range from -1 to 100, inclusive. When this property is set to -1, the measurement automatically sets the value of this property to the recommended value as specified in the Annexe F.5 of 3GPP TS 38.101-2 specification for uplink and Annexe B.5.2 and C.5.2 of 3GPP TS 38.104 specification for downlink.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the FFT window length (W). This value is expressed as a percentage of the cyclic prefix length. This method is used when you set the SetFftWindowType(string, RFmxNRMXModAccFftWindowType) method to Type3GPP, where it is needed to calculate the EVM using two different FFT window positions, Delta_C-W/2, and Delta_C+W/2. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getfftwindowtype__string-out.html language=enus -->
## TOPIC 00255: GetFftWindowType(string, out RFmxNRMXModAccFftWindowType)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getfftwindowtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getfftwindowtype__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the FFT window type used for EVM calculation. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetFftWindowType(string selectorString, out RFmxNRMXModAccFftWindowType value)RemarksThis method gets the value of ModAccFftWindowType attribute.The default value is TypeCustom.ParametersNameT

### GetFftWindowType(string, out RFmxNRMXModAccFftWindowType)

Gets the FFT window type used for EVM calculation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetFftWindowType(string selectorString, out RFmxNRMXModAccFftWindowType value)

#### Remarks

This method gets the value of [ModAccFftWindowType](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [TypeCustom](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccfftwindowtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxNRMXModAccFftWindowType | Upon return, contains the FFT window type used for EVM calculation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getiqimpairmentspersubcarrierenabled__string-out.html language=enus -->
## TOPIC 00256: GetIQImpairmentsPerSubcarrierEnabled(string, out RFmxNRMXModAccIQImpairmentsPerSubcarrierEnabled)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getiqimpairmentspersubcarrierenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getiqimpairmentspersubcarrierenabled__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to return I/Q impairments independently for each subcarrier. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetIQImpairmentsPerSubcarrierEnabled(string selectorString, out RFmxNRMXModAccIQImpairmentsPerSubcarrierEnabled value)RemarksThis method gets the value of ModAccIQImpair

### GetIQImpairmentsPerSubcarrierEnabled(string, out RFmxNRMXModAccIQImpairmentsPerSubcarrierEnabled)

Gets whether to return I/Q impairments independently for each subcarrier.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetIQImpairmentsPerSubcarrierEnabled(string selectorString, out RFmxNRMXModAccIQImpairmentsPerSubcarrierEnabled value)

#### Remarks

This method gets the value of [ModAccIQImpairmentsPerSubcarrierEnabled](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-nrmx-rfmxnrmxmodacciqimpairmentspersubcarrierenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxNRMXModAccIQImpairmentsPerSubcarrierEnabled | Upon return, contains whether to return I/Q impairments independently for each subcarrier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getmeasurementmode__string-out.html language=enus -->
## TOPIC 00257: GetMeasurementMode(string, out RFmxNRMXModAccMeasurementMode)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getmeasurementmode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getmeasurementmode__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement should calibrate the noise floor of the analyzer or perform the ModAcc measurement. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetMeasurementMode(string selectorString, out RFmxNRMXModAccMeasurementMode value)RemarksThis method gets the value of ModAccMeasu

### GetMeasurementMode(string, out RFmxNRMXModAccMeasurementMode)

Gets whether the measurement should calibrate the noise floor of the analyzer or perform the ModAcc measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetMeasurementMode(string selectorString, out RFmxNRMXModAccMeasurementMode value)

#### Remarks

This method gets the value of [ModAccMeasurementMode](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Measure](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccmeasurementmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxNRMXModAccMeasurementMode | Upon return, contains whether the measurement should calibrate the noise floor of the analyzer or perform the ModAcc measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getmeasurementoffset__string-out.html language=enus -->
## TOPIC 00258: GetMeasurementOffset(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getmeasurementoffset__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getmeasurementoffset__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxNRMXModAccSynchronizationMode) method. The unit for this is specified by ModAcc Measurement Length Unit. SyntaxNamespace: NationalInstruments.RFm

### GetMeasurementOffset(string, out double)

Gets the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the [SetSynchronizationMode(string, RFmxNRMXModAccSynchronizationMode)](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setsynchronizationmode__string-rfmxnrmxmodaccsynchronizationmode.html) method. The unit for this is specified by ModAcc Measurement Length Unit.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetMeasurementOffset(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccMeasurementOffset](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxNRMXModAccSynchronizationMode) method. The unit for this is specified by ModAcc Measurement Length Unit. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getmulticarrierfilterenabled__string-out.html language=enus -->
## TOPIC 00259: GetMulticarrierFilterEnabled(string, out RFmxNRMXModAccMulticarrierFilterEnabled)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getmulticarrierfilterenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getmulticarrierfilterenabled__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to use the filter in single carrier configurations to minimize leakage into the carrier. Measurement ignores this method, if number of carriers is set to more than 1 or if you set the SetAcquisitionBandwidthOptimizationEnabled(string, RFmxNRMXAcquisitionBandwidthOptimizationEnabled) met

### GetMulticarrierFilterEnabled(string, out RFmxNRMXModAccMulticarrierFilterEnabled)

Gets whether to use the filter in single carrier configurations to minimize leakage into the carrier. Measurement ignores this method, if number of carriers is set to more than 1 or if you set the [SetAcquisitionBandwidthOptimizationEnabled(string, RFmxNRMXAcquisitionBandwidthOptimizationEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmx-setacquisitionbandwidthoptimizationenabled__string-rfmxnrmxacquisitionbandwidthoptimizationenabled.html) method to [False](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccmulticarrierfilterenabled.html), where in the multi carrier filter will always be used.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetMulticarrierFilterEnabled(string selectorString, out RFmxNRMXModAccMulticarrierFilterEnabled value)

#### Remarks

This method gets the value of [ModAccMulticarrierFilterEnabled](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccmulticarrierfilterenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxNRMXModAccMulticarrierFilterEnabled | Upon return, contains whether to use the filter in single carrier configurations to minimize leakage into the carrier. Measurement ignores this method, if number of carriers is set to more than 1 or if you set the SetAcquisitionBandwidthOptimizationEnabled(string, RFmxNRMXAcquisitionBandwidthOptimizationEnabled) method to False, where in the multi carrier filter will always be used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getspectruminverted__string-out.html language=enus -->
## TOPIC 00260: GetSpectrumInverted(string, out RFmxNRMXModAccSpectrumInverted)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getspectruminverted__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-getspectruminverted__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the spectrum of the signal being measured is inverted. This happens when I and Q component of the baseband complex signal is swapped. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetSpectrumInverted(string selectorString, out RFmxNRMXModAccSpectrumInverted value)RemarksThis

### GetSpectrumInverted(string, out RFmxNRMXModAccSpectrumInverted)

Gets whether the spectrum of the signal being measured is inverted. This happens when I and Q component of the baseband complex signal is swapped.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetSpectrumInverted(string selectorString, out RFmxNRMXModAccSpectrumInverted value)

#### Remarks

This method gets the value of [ModAccSpectrumInverted](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccspectruminverted.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxNRMXModAccSpectrumInverted | Upon return, contains whether the spectrum of the signal being measured is inverted. This happens when I and Q component of the baseband complex signal is swapped. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-gettransientperiod__string-out.html language=enus -->
## TOPIC 00261: GetTransientPeriod(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-gettransientperiod__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-gettransientperiod__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: It configures the transient duration as specified in section 6.4.2.1a of 3GPP 38.101-1 specification. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetTransientPeriod(string selectorString, out double value)RemarksThis method gets the value of ModAccTransientPeriod attribute.The default v

### GetTransientPeriod(string, out double)

It configures the transient duration as specified in section 6.4.2.1a of *3GPP 38.101-1* specification.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetTransientPeriod(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccTransientPeriod](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 2us.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | It configures the transient duration as specified in section 6.4.2.1a of 3GPP 38.101-1 specification. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setalltracesenabled__string-bool.html language=enus -->
## TOPIC 00262: SetAllTracesEnabled(string, bool)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setalltracesenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setalltracesenabled__string-bool.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the traces to be stored and retrieved after performing the ModAcc measurement. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetAllTracesEnabled(string selectorString, bool value)RemarksThis method sets the value of ModAccAllTracesEnabled attribute.The default value

### SetAllTracesEnabled(string, bool)

Sets whether to enable the traces to be stored and retrieved after performing the ModAcc measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetAllTracesEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [ModAccAllTracesEnabled](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the traces to be stored and retrieved after performing the ModAcc measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setautolevelallowoverflow__string-rfmxnrmxmodaccautolevelallowoverflow.html language=enus -->
## TOPIC 00263: SetAutoLevelAllowOverflow(string, RFmxNRMXModAccAutoLevelAllowOverflow)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setautolevelallowoverflow__string-rfmxnrmxmodaccautolevelallowoverflow.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setautolevelallowoverflow__string-rfmxnrmxmodaccautolevelallowoverflow.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the AutoLevel(string, double) function should search for the optimum reference levels while allowing ADC overflow. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetAutoLevelAllowOverflow(string selectorString, RFmxNRMXModAccAutoLevelAllowOverflow value)RemarksThis method sets

### SetAutoLevelAllowOverflow(string, RFmxNRMXModAccAutoLevelAllowOverflow)

Sets whether the [AutoLevel(string, double)](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-autolevel__string-double.html) function should search for the optimum reference levels while allowing ADC overflow.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetAutoLevelAllowOverflow(string selectorString, RFmxNRMXModAccAutoLevelAllowOverflow value)

#### Remarks

This method sets the value of [ModAccAutoLevelAllowOverflow](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccautolevelallowoverflow.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXModAccAutoLevelAllowOverflow | Specifies whether the AutoLevel(string, double) function should search for the optimum reference levels while allowing ADC overflow. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setevmreferencedatasymbolsmode__string-rfmxnrmxmodaccevmreferencedatasymbolsmode.html language=enus -->
## TOPIC 00264: SetEvmReferenceDataSymbolsMode(string, RFmxNRMXModAccEvmReferenceDataSymbolsMode)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setevmreferencedatasymbolsmode__string-rfmxnrmxmodaccevmreferencedatasymbolsmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setevmreferencedatasymbolsmode__string-rfmxnrmxmodaccevmreferencedatasymbolsmode.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to either use a reference waveform or an acquired waveform to create reference data symbols for EVM computation. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetEvmReferenceDataSymbolsMode(string selectorString, RFmxNRMXModAccEvmReferenceDataSymbolsMode value)RemarksThis met

### SetEvmReferenceDataSymbolsMode(string, RFmxNRMXModAccEvmReferenceDataSymbolsMode)

Sets whether to either use a reference waveform or an acquired waveform to create reference data symbols for EVM computation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetEvmReferenceDataSymbolsMode(string selectorString, RFmxNRMXModAccEvmReferenceDataSymbolsMode value)

#### Remarks

This method sets the value of [ModAccEvmReferenceDataSymbolsMode](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [AcquiredWaveform](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccevmreferencedatasymbolsmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXModAccEvmReferenceDataSymbolsMode | Specifies whether to either use a reference waveform or an acquired waveform to create reference data symbols for EVM computation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setiqimpairmentsmodel__string-rfmxnrmxmodacciqimpairmentsmodel.html language=enus -->
## TOPIC 00265: SetIQImpairmentsModel(string, RFmxNRMXModAccIQImpairmentsModel)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setiqimpairmentsmodel__string-rfmxnrmxmodacciqimpairmentsmodel.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setiqimpairmentsmodel__string-rfmxnrmxmodacciqimpairmentsmodel.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the I/Q impairments model used by the measurement for estimating I/Q impairments. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetIQImpairmentsModel(string selectorString, RFmxNRMXModAccIQImpairmentsModel value)RemarksThis method sets the value of ModAccIQImpairmentsModel attribute.

### SetIQImpairmentsModel(string, RFmxNRMXModAccIQImpairmentsModel)

Sets the I/Q impairments model used by the measurement for estimating I/Q impairments.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetIQImpairmentsModel(string selectorString, RFmxNRMXModAccIQImpairmentsModel value)

#### Remarks

This method sets the value of [ModAccIQImpairmentsModel](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Tx](nationalinstruments-rfmx-nrmx-rfmxnrmxmodacciqimpairmentsmodel.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXModAccIQImpairmentsModel | Specifies the I/Q impairments model used by the measurement for estimating I/Q impairments. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setiqimpairmentspersubcarrierenabled__string-rfmxnrmxmodacciqimpairmentspersubcarrierenabled.html language=enus -->
## TOPIC 00266: SetIQImpairmentsPerSubcarrierEnabled(string, RFmxNRMXModAccIQImpairmentsPerSubcarrierEnabled)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setiqimpairmentspersubcarrierenabled__string-rfmxnrmxmodacciqimpairmentspersubcarrierenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setiqimpairmentspersubcarrierenabled__string-rfmxnrmxmodacciqimpairmentspersubcarrierenabled.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to return I/Q impairments independently for each subcarrier. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetIQImpairmentsPerSubcarrierEnabled(string selectorString, RFmxNRMXModAccIQImpairmentsPerSubcarrierEnabled value)RemarksThis method sets the value of ModAccIQImpairment

### SetIQImpairmentsPerSubcarrierEnabled(string, RFmxNRMXModAccIQImpairmentsPerSubcarrierEnabled)

Sets whether to return I/Q impairments independently for each subcarrier.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetIQImpairmentsPerSubcarrierEnabled(string selectorString, RFmxNRMXModAccIQImpairmentsPerSubcarrierEnabled value)

#### Remarks

This method sets the value of [ModAccIQImpairmentsPerSubcarrierEnabled](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-nrmx-rfmxnrmxmodacciqimpairmentspersubcarrierenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXModAccIQImpairmentsPerSubcarrierEnabled | Specifies whether to return I/Q impairments independently for each subcarrier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setiqtimingskewcorrectionenabled__string-rfmxnrmxmodacciqtimingskewcorrectionenabled.html language=enus -->
## TOPIC 00267: SetIQTimingSkewCorrectionEnabled(string, RFmxNRMXModAccIQTimingSkewCorrectionEnabled)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setiqtimingskewcorrectionenabled__string-rfmxnrmxmodacciqtimingskewcorrectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setiqtimingskewcorrectionenabled__string-rfmxnrmxmodacciqtimingskewcorrectionenabled.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable IQ timing skew correction. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetIQTimingSkewCorrectionEnabled(string selectorString, RFmxNRMXModAccIQTimingSkewCorrectionEnabled value)RemarksThis method sets the value of ModAccIQTimingSkewCorrectionEnabled attribute.The

### SetIQTimingSkewCorrectionEnabled(string, RFmxNRMXModAccIQTimingSkewCorrectionEnabled)

Sets whether to enable IQ timing skew correction.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetIQTimingSkewCorrectionEnabled(string selectorString, RFmxNRMXModAccIQTimingSkewCorrectionEnabled value)

#### Remarks

This method sets the value of [ModAccIQTimingSkewCorrectionEnabled](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-nrmx-rfmxnrmxmodacciqtimingskewcorrectionenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXModAccIQTimingSkewCorrectionEnabled | Specifies whether to enable IQ timing skew correction. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setmagnitudeandphaseerrorenabled__string-rfmxnrmxmodaccmagnitudeandphaseerrorenabled.html language=enus -->
## TOPIC 00268: SetMagnitudeAndPhaseErrorEnabled(string, RFmxNRMXModAccMagnitudeAndPhaseErrorEnabled)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setmagnitudeandphaseerrorenabled__string-rfmxnrmxmodaccmagnitudeandphaseerrorenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setmagnitudeandphaseerrorenabled__string-rfmxnrmxmodaccmagnitudeandphaseerrorenabled.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to measure the magnitude and the phase error. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetMagnitudeAndPhaseErrorEnabled(string selectorString, RFmxNRMXModAccMagnitudeAndPhaseErrorEnabled value)RemarksThis method sets the value of ModAccMagnitudeAndPhaseErrorEnabled attri

### SetMagnitudeAndPhaseErrorEnabled(string, RFmxNRMXModAccMagnitudeAndPhaseErrorEnabled)

Sets whether to measure the magnitude and the phase error.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetMagnitudeAndPhaseErrorEnabled(string selectorString, RFmxNRMXModAccMagnitudeAndPhaseErrorEnabled value)

#### Remarks

This method sets the value of [ModAccMagnitudeAndPhaseErrorEnabled](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccmagnitudeandphaseerrorenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXModAccMagnitudeAndPhaseErrorEnabled | Specifies whether to measure the magnitude and the phase error. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setmeasurementlengthunit__string-rfmxnrmxmodaccmeasurementlengthunit.html language=enus -->
## TOPIC 00269: SetMeasurementLengthUnit(string, RFmxNRMXModAccMeasurementLengthUnit)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setmeasurementlengthunit__string-rfmxnrmxmodaccmeasurementlengthunit.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setmeasurementlengthunit__string-rfmxnrmxmodaccmeasurementlengthunit.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the units in which measurement offset and measurement length are specified. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetMeasurementLengthUnit(string selectorString, RFmxNRMXModAccMeasurementLengthUnit value)RemarksThis method sets the value of ModAccMeasurementLengthUnit attribu

### SetMeasurementLengthUnit(string, RFmxNRMXModAccMeasurementLengthUnit)

Sets the units in which measurement offset and measurement length are specified.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetMeasurementLengthUnit(string selectorString, RFmxNRMXModAccMeasurementLengthUnit value)

#### Remarks

This method sets the value of [ModAccMeasurementLengthUnit](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Slot](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccmeasurementlengthunit.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXModAccMeasurementLengthUnit | Specifies the units in which measurement offset and measurement length are specified. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setmeasurementmode__string-rfmxnrmxmodaccmeasurementmode.html language=enus -->
## TOPIC 00270: SetMeasurementMode(string, RFmxNRMXModAccMeasurementMode)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setmeasurementmode__string-rfmxnrmxmodaccmeasurementmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setmeasurementmode__string-rfmxnrmxmodaccmeasurementmode.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement should calibrate the noise floor of the analyzer or perform the ModAcc measurement. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetMeasurementMode(string selectorString, RFmxNRMXModAccMeasurementMode value)RemarksThis method sets the value of ModAccMeasureme

### SetMeasurementMode(string, RFmxNRMXModAccMeasurementMode)

Sets whether the measurement should calibrate the noise floor of the analyzer or perform the ModAcc measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetMeasurementMode(string selectorString, RFmxNRMXModAccMeasurementMode value)

#### Remarks

This method sets the value of [ModAccMeasurementMode](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Measure](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccmeasurementmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXModAccMeasurementMode | Specifies whether the measurement should calibrate the noise floor of the analyzer or perform the ModAcc measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setmulticarrierfilterenabled__string-rfmxnrmxmodaccmulticarrierfilterenabled.html language=enus -->
## TOPIC 00271: SetMulticarrierFilterEnabled(string, RFmxNRMXModAccMulticarrierFilterEnabled)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setmulticarrierfilterenabled__string-rfmxnrmxmodaccmulticarrierfilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setmulticarrierfilterenabled__string-rfmxnrmxmodaccmulticarrierfilterenabled.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to use the filter in single carrier configurations to minimize leakage into the carrier. Measurement ignores this method, if number of carriers is set to more than 1 or if you set the SetAcquisitionBandwidthOptimizationEnabled(string, RFmxNRMXAcquisitionBandwidthOptimizationEnabled) met

### SetMulticarrierFilterEnabled(string, RFmxNRMXModAccMulticarrierFilterEnabled)

Sets whether to use the filter in single carrier configurations to minimize leakage into the carrier. Measurement ignores this method, if number of carriers is set to more than 1 or if you set the [SetAcquisitionBandwidthOptimizationEnabled(string, RFmxNRMXAcquisitionBandwidthOptimizationEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmx-setacquisitionbandwidthoptimizationenabled__string-rfmxnrmxacquisitionbandwidthoptimizationenabled.html) method to [False](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccmulticarrierfilterenabled.html), where in the multi carrier filter will always be used.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetMulticarrierFilterEnabled(string selectorString, RFmxNRMXModAccMulticarrierFilterEnabled value)

#### Remarks

This method sets the value of [ModAccMulticarrierFilterEnabled](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccmulticarrierfilterenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXModAccMulticarrierFilterEnabled | Specifies whether to use the filter in single carrier configurations to minimize leakage into the carrier. Measurement ignores this method, if number of carriers is set to more than 1 or if you set the SetAcquisitionBandwidthOptimizationEnabled(string, RFmxNRMXAcquisitionBandwidthOptimizationEnabled) method to False, where in the multi carrier filter will always be used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setnoisecompensationreferencelevelcoercionlimit__string-double.html language=enus -->
## TOPIC 00272: SetNoiseCompensationReferenceLevelCoercionLimit(string, double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setnoisecompensationreferencelevelcoercionlimit__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setnoisecompensationreferencelevelcoercionlimit__string-double.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the coercion limit for the reference level for noise compensation. When you set the SetMeasurementMode(string, RFmxNRMXModAccMeasurementMode) method to Measure and SetNoiseCompensationEnabled(string, RFmxNRMXModAccNoiseCompensationEnabled) method to True, the measurement attempts to read noise

### SetNoiseCompensationReferenceLevelCoercionLimit(string, double)

Sets the coercion limit for the reference level for noise compensation. When you set the [SetMeasurementMode(string, RFmxNRMXModAccMeasurementMode)](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setmeasurementmode__string-rfmxnrmxmodaccmeasurementmode.html) method to [Measure](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccmeasurementmode.html) and [SetNoiseCompensationEnabled(string, RFmxNRMXModAccNoiseCompensationEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setnoisecompensationenabled__string-rfmxnrmxmodaccnoisecompensationenabled.html) method to [True](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccnoisecompensationenabled.html), the measurement attempts to read noise floor calibration data corresponding to the configured reference level. If noise floor calibration data corresponding to the configured reference level is not found in the calibration database, the measurement attempts to read noise floor calibration data from the calibration database for any reference level in the range of the configured reference level plus or minus the coercion limit you set for this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetNoiseCompensationReferenceLevelCoercionLimit(string selectorString, double value)

#### Remarks

This method sets the value of [ModAccNoiseCompensationReferenceLevelCoercionLimit](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.For the configured reference level, if the noise calibration data is not present, the nearest value to the user-configured reference level that is available in the database within the coercion limit, is applied to the driver. The default value is 0.5.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the coercion limit for the reference level for noise compensation. When you set the SetMeasurementMode(string, RFmxNRMXModAccMeasurementMode) method to Measure and SetNoiseCompensationEnabled(string, RFmxNRMXModAccNoiseCompensationEnabled) method to True, the measurement attempts to read noise floor calibration data corresponding to the configured reference level. If noise floor calibration data corresponding to the configured reference level is not found in the calibration database, the measurement attempts to read noise floor calibration data from the calibration database for any reference level in the range of the configured reference level plus or minus the coercion limit you set for this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setnumberofanalysisthreads__string-int.html language=enus -->
## TOPIC 00273: SetNumberOfAnalysisThreads(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setnumberofanalysisthreads__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setnumberofanalysisthreads__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the maximum number of threads used for parallelism for the ModAcc measurement. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetNumberOfAnalysisThreads(string selectorString, int value)RemarksThis method sets the value of ModAccNumberOfAnalysisThreads attribute.The default value is 1

### SetNumberOfAnalysisThreads(string, int)

Sets the maximum number of threads used for parallelism for the ModAcc measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetNumberOfAnalysisThreads(string selectorString, int value)

#### Remarks

This method sets the value of [ModAccNumberOfAnalysisThreads](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the maximum number of threads used for parallelism for the ModAcc measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setphasetrackingmode__string-rfmxnrmxmodaccphasetrackingmode.html language=enus -->
## TOPIC 00274: SetPhaseTrackingMode(string, RFmxNRMXModAccPhaseTrackingMode)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setphasetrackingmode__string-rfmxnrmxmodaccphasetrackingmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setphasetrackingmode__string-rfmxnrmxmodaccphasetrackingmode.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the method used for phase tracking. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetPhaseTrackingMode(string selectorString, RFmxNRMXModAccPhaseTrackingMode value)RemarksThis method sets the value of ModAccPhaseTrackingMode attribute.The default value is Reference+Data.ParametersNam

### SetPhaseTrackingMode(string, RFmxNRMXModAccPhaseTrackingMode)

Sets the method used for phase tracking.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetPhaseTrackingMode(string selectorString, RFmxNRMXModAccPhaseTrackingMode value)

#### Remarks

This method sets the value of [ModAccPhaseTrackingMode](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is Reference+Data.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXModAccPhaseTrackingMode | Specifies the method used for phase tracking. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setpreffterrorestimationinterval__string-rfmxnrmxmodaccpreffterrorestimationinterval.html language=enus -->
## TOPIC 00275: SetPreFftErrorEstimationInterval(string, RFmxNRMXModAccPreFftErrorEstimationInterval)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setpreffterrorestimationinterval__string-rfmxnrmxmodaccpreffterrorestimationinterval.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setpreffterrorestimationinterval__string-rfmxnrmxmodaccpreffterrorestimationinterval.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the interval used for Pre-FFT error estimation. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetPreFftErrorEstimationInterval(string selectorString, RFmxNRMXModAccPreFftErrorEstimationInterval value)RemarksThis method sets the value of ModAccPreFftErrorEstimationInterval attribute.T

### SetPreFftErrorEstimationInterval(string, RFmxNRMXModAccPreFftErrorEstimationInterval)

Sets the interval used for Pre-FFT error estimation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetPreFftErrorEstimationInterval(string selectorString, RFmxNRMXModAccPreFftErrorEstimationInterval value)

#### Remarks

This method sets the value of [ModAccPreFftErrorEstimationInterval](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [MeasurementLength](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccpreffterrorestimationinterval.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXModAccPreFftErrorEstimationInterval | Specifies the interval used for Pre-FFT error estimation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setshortframeenabled__string-rfmxnrmxmodaccshortframeenabled.html language=enus -->
## TOPIC 00276: SetShortFrameEnabled(string, RFmxNRMXModAccShortFrameEnabled)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setshortframeenabled__string-rfmxnrmxmodaccshortframeenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setshortframeenabled__string-rfmxnrmxmodaccshortframeenabled.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the input signal has a periodicity shorter than the NR frame duration. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetShortFrameEnabled(string selectorString, RFmxNRMXModAccShortFrameEnabled value)RemarksThis method sets the value of ModAccShortFrameEnabled attribute.The de

### SetShortFrameEnabled(string, RFmxNRMXModAccShortFrameEnabled)

Sets whether the input signal has a periodicity shorter than the NR frame duration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetShortFrameEnabled(string selectorString, RFmxNRMXModAccShortFrameEnabled value)

#### Remarks

This method sets the value of [ModAccShortFrameEnabled](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccshortframeenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXModAccShortFrameEnabled | Specifies whether the input signal has a periodicity shorter than the NR frame duration. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setshortframelengthunit__string-rfmxnrmxmodaccshortframelengthunit.html language=enus -->
## TOPIC 00277: SetShortFrameLengthUnit(string, RFmxNRMXModAccShortFrameLengthUnit)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setshortframelengthunit__string-rfmxnrmxmodaccshortframelengthunit.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setshortframelengthunit__string-rfmxnrmxmodaccshortframelengthunit.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the units in which Short Frame Length is specified. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetShortFrameLengthUnit(string selectorString, RFmxNRMXModAccShortFrameLengthUnit value)RemarksThis method sets the value of ModAccShortFrameLengthUnit attribute.The default value is Tim

### SetShortFrameLengthUnit(string, RFmxNRMXModAccShortFrameLengthUnit)

Sets the units in which Short Frame Length is specified.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetShortFrameLengthUnit(string selectorString, RFmxNRMXModAccShortFrameLengthUnit value)

#### Remarks

This method sets the value of [ModAccShortFrameLengthUnit](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Time](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccshortframelengthunit.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXModAccShortFrameLengthUnit | Specifies the units in which Short Frame Length is specified. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setspectralflatnesscondition__string-rfmxnrmxmodaccspectralflatnesscondition.html language=enus -->
## TOPIC 00278: SetSpectralFlatnessCondition(string, RFmxNRMXModAccSpectralFlatnessCondition)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setspectralflatnesscondition__string-rfmxnrmxmodaccspectralflatnesscondition.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setspectralflatnesscondition__string-rfmxnrmxmodaccspectralflatnesscondition.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the test condition for Spectral Flatness measurement. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetSpectralFlatnessCondition(string selectorString, RFmxNRMXModAccSpectralFlatnessCondition value)RemarksThis method sets the value of ModAccSpectralFlatnessCondition attribute.The def

### SetSpectralFlatnessCondition(string, RFmxNRMXModAccSpectralFlatnessCondition)

Sets the test condition for Spectral Flatness measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetSpectralFlatnessCondition(string selectorString, RFmxNRMXModAccSpectralFlatnessCondition value)

#### Remarks

This method sets the value of [ModAccSpectralFlatnessCondition](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Normal](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccspectralflatnesscondition.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXModAccSpectralFlatnessCondition | Specifies the test condition for Spectral Flatness measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setspectruminverted__string-rfmxnrmxmodaccspectruminverted.html language=enus -->
## TOPIC 00279: SetSpectrumInverted(string, RFmxNRMXModAccSpectrumInverted)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setspectruminverted__string-rfmxnrmxmodaccspectruminverted.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setspectruminverted__string-rfmxnrmxmodaccspectruminverted.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the spectrum of the signal being measured is inverted. This happens when I and Q component of the baseband complex signal is swapped. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetSpectrumInverted(string selectorString, RFmxNRMXModAccSpectrumInverted value)RemarksThis meth

### SetSpectrumInverted(string, RFmxNRMXModAccSpectrumInverted)

Sets whether the spectrum of the signal being measured is inverted. This happens when I and Q component of the baseband complex signal is swapped.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetSpectrumInverted(string selectorString, RFmxNRMXModAccSpectrumInverted value)

#### Remarks

This method sets the value of [ModAccSpectrumInverted](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccspectruminverted.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXModAccSpectrumInverted | Specifies whether the spectrum of the signal being measured is inverted. This happens when I and Q component of the baseband complex signal is swapped. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setsymbolclockerrorestimationenabled__string-rfmxnrmxmodaccsymbolclockerrorestimationenabled.html language=enus -->
## TOPIC 00280: SetSymbolClockErrorEstimationEnabled(string, RFmxNRMXModAccSymbolClockErrorEstimationEnabled)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setsymbolclockerrorestimationenabled__string-rfmxnrmxmodaccsymbolclockerrorestimationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setsymbolclockerrorestimationenabled__string-rfmxnrmxmodaccsymbolclockerrorestimationenabled.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to estimate symbol clock error. This method is ignored when the Common Clock Source Enabled method is True and the Frequency Error Estimation method is Disabled, in which case, symbol clock error is not estimated. If symbol clock error is absent in the signal to be analyzed, you may dis

### SetSymbolClockErrorEstimationEnabled(string, RFmxNRMXModAccSymbolClockErrorEstimationEnabled)

Sets whether to estimate symbol clock error. This method is ignored when the Common Clock Source Enabled method is [True](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccsymbolclockerrorestimationenabled.html) and the Frequency Error Estimation method is Disabled, in which case, symbol clock error is not estimated. If symbol clock error is absent in the signal to be analyzed, you may disable symbol clock error estimation to reduce measurement time or to avoid measurement inaccuracy due to error in symbol clock error estimation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetSymbolClockErrorEstimationEnabled(string selectorString, RFmxNRMXModAccSymbolClockErrorEstimationEnabled value)

#### Remarks

This method sets the value of [ModAccSymbolClockErrorEstimationEnabled](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccsymbolclockerrorestimationenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXModAccSymbolClockErrorEstimationEnabled | Specifies whether to estimate symbol clock error. This method is ignored when the Common Clock Source Enabled method is True and the Frequency Error Estimation method is Disabled, in which case, symbol clock error is not estimated. If symbol clock error is absent in the signal to be analyzed, you may disable symbol clock error estimation to reduce measurement time or to avoid measurement inaccuracy due to error in symbol clock error estimation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-settransientperiod__string-double.html language=enus -->
## TOPIC 00281: SetTransientPeriod(string, double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-settransientperiod__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-settransientperiod__string-double.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: It configures the transient duration as specified in section 6.4.2.1a of 3GPP 38.101-1 specification. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetTransientPeriod(string selectorString, double value)RemarksThis method sets the value of ModAccTransientPeriod attribute.The default value

### SetTransientPeriod(string, double)

It configures the transient duration as specified in section 6.4.2.1a of *3GPP 38.101-1* specification.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetTransientPeriod(string selectorString, double value)

#### Remarks

This method sets the value of [ModAccTransientPeriod](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 2us.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | It configures the transient duration as specified in section 6.4.2.1a of 3GPP 38.101-1 specification. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-settransientperiodevmmode__string-rfmxnrmxmodacctransientperiodevmmode.html language=enus -->
## TOPIC 00282: SetTransientPeriodEvmMode(string, RFmxNRMXModAccTransientPeriodEvmMode)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-settransientperiodevmmode__string-rfmxnrmxmodacctransientperiodevmmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-settransientperiodevmmode__string-rfmxnrmxmodacctransientperiodevmmode.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the EVM measurement behavior for symbols affected by power transients. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetTransientPeriodEvmMode(string selectorString, RFmxNRMXModAccTransientPeriodEvmMode value)RemarksThis method sets the value of ModAccTransientPeriodEvmMode att

### SetTransientPeriodEvmMode(string, RFmxNRMXModAccTransientPeriodEvmMode)

Configures the EVM measurement behavior for symbols affected by power transients.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetTransientPeriodEvmMode(string selectorString, RFmxNRMXModAccTransientPeriodEvmMode value)

#### Remarks

This method sets the value of [ModAccTransientPeriodEvmMode](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Disabled](nationalinstruments-rfmx-nrmx-rfmxnrmxmodacctransientperiodevmmode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXModAccTransientPeriodEvmMode | Configures the EVM measurement behavior for symbols affected by power transients. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-settransientpowerchangethreshold__string-double.html language=enus -->
## TOPIC 00283: SetTransientPowerChangeThreshold(string, double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-settransientpowerchangethreshold__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-settransientpowerchangethreshold__string-double.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets transient period power change threshold level in dB. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetTransientPowerChangeThreshold(string selectorString, double value)RemarksThis method sets the value of ModAccTransientPowerChangeThreshold attribute.The default value is 1.Parameters

### SetTransientPowerChangeThreshold(string, double)

Sets transient period power change threshold level in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetTransientPowerChangeThreshold(string selectorString, double value)

#### Remarks

This method sets the value of [ModAccTransientPowerChangeThreshold](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies transient period power change threshold level in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-validatecalibrationdata__string-out.html language=enus -->
## TOPIC 00284: ValidateCalibrationData(string, out RFmxNRMXModAccCalibrationDataValid)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-validatecalibrationdata__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-validatecalibrationdata__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether calibration data is valid for the configuration specified by the signal name in the selectorString parameter.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int ValidateCalibrationData(string selectorString, out RFmxNRMXModAccCalibrationDataValid calibrationDataValid)Parameter

### ValidateCalibrationData(string, out RFmxNRMXModAccCalibrationDataValid)

Specifies whether calibration data is valid for the configuration specified by the signal name in the *selectorString* parameter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int ValidateCalibrationData(string selectorString, out RFmxNRMXModAccCalibrationDataValid calibrationDataValid)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| calibrationDataValid | out RFmxNRMXModAccCalibrationDataValid | Upon return, contains whether the calibration data is valid. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration.html language=enus -->
## TOPIC 00285: RFmxNRMXModAccConfiguration Class

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the ModAcc measurement. Derives fromRFmxNRMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.NRMXpublic class RFmxNRMXModAccConfiguration : RFmxNRMXSubObjectMethodsNameDescriptionAutoLevel(string, double)Performs the user-configured ModAcc measurement at multiple refe

### RFmxNRMXModAccConfiguration Class

Provides methods to configure the ModAcc measurement.

#### Derives from

- RFmxNRMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public class RFmxNRMXModAccConfiguration : RFmxNRMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| AutoLevel(string, double) | Performs the user-configured ModAcc measurement at multiple reference levels relative to the user-configured SetReferenceLevel(string, double) method and configures the reference level corresponding to the lowest GetCompositeRmsEvmMean(string, out double) result. This method only measures at the reference levels that do not result in an ADC or OSP overflow when you set the SetAutoLevelAllowOverflow(string, RFmxNRMXModAccAutoLevelAllowOverflow) method to False. If you set the ModAcc Auto Level Allow Overflow method to True, this method measures at a few reference levels beyond the overflow. |
| ClearNoiseCalibrationDatabase() | Clears the noise calibration database used for EVM noise compensation. |
| ConfigureMeasurementMode(string, RFmxNRMXModAccMeasurementMode) | Configures the measurement mode for the ModAcc measurement. |
| ConfigureNoiseCompensationEnabled(string, RFmxNRMXModAccNoiseCompensationEnabled) | Configures whether to enable EVM noise compensation for the ModAcc measurement.supporteddevices:PXIe-5830/5831/5832/5646/5840/5841/5842/5860. |
| ConfigureReferenceWaveform(string, ComplexWaveform< ComplexSingle >) | Configures the reference waveform for the creation of reference data symbols for EVM computation. |
| GetAllTracesEnabled(string, out bool) | Gets whether to enable the traces to be stored and retrieved after performing the ModAcc measurement. |
| GetAutoLevelAllowOverflow(string, out RFmxNRMXModAccAutoLevelAllowOverflow) | Gets whether the AutoLevel(string, double) function should search for the optimum reference levels while allowing ADC overflow. |
| GetAveragingCount(string, out int) | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxNRMXModAccAveragingEnabled) method to True. |
| GetAveragingEnabled(string, out RFmxNRMXModAccAveragingEnabled) | Enables averaging for the measurement. |
| GetChannelEstimationType(string, out RFmxNRMXModAccChannelEstimationType) | Gets the method used for channel estimation. |
| GetCommonClockSourceEnabled(string, out RFmxNRMXModAccCommonClockSourceEnabled) | Gets whether same reference clock is used for local oscillator and digital-to-analog converter. When same reference clock is used the Carrier Frequency Offset is proportional to Sample Clock Error. |
| GetCompositeResultsIncludeDmrs(string, out RFmxNRMXModAccCompositeResultsIncludeDmrs) | Gets whether the DMRS resource elements are included for composite EVM and magnitude and phase error results and traces. |
| GetCompositeResultsIncludePtrs(string, out RFmxNRMXModAccCompositeResultsIncludePtrs) | Gets whether the PTRS resource elements are included for composite EVM and magnitude and phase error results and traces. |
| GetDCSubcarrierRemovalEnabled(string, out RFmxNRMXModAccDCSubcarrierRemovalEnabled) | Gets whether the DC subcarrier is removed from the EVM results. |
| GetEvmReferenceDataSymbolsMode(string, out RFmxNRMXModAccEvmReferenceDataSymbolsMode) | Gets whether to either use a reference waveform or an acquired waveform to create reference data symbols for EVM computation. |
| GetEvmUnit(string, out RFmxNRMXModAccEvmUnit) | Gets the units of the EVM results. |
| GetFftWindowLength(string, out double) | Gets the FFT window length (W). This value is expressed as a percentage of the cyclic prefix length. This method is used when you set the SetFftWindowType(string, RFmxNRMXModAccFftWindowType) method to Type3GPP, where it is needed to calculate the EVM using two different FFT window positions, Delta_C-W/2, and Delta_C+W/2. |
| GetFftWindowOffset(string, out double) | Gets the position of the FFT window used to calculate the EVM when SetFftWindowType(string, RFmxNRMXModAccFftWindowType) method is set to TypeCustom. The offset is expressed as a percentage of the cyclic prefix length. If you set this method to 0, the EVM window starts at the end of cyclic prefix. If you set this method to 100, the EVM window starts at the beginning of cyclic prefix. |
| GetFftWindowType(string, out RFmxNRMXModAccFftWindowType) | Gets the FFT window type used for EVM calculation. |
| GetFrequencyErrorEstimation(string, out RFmxNRMXModAccFrequencyErrorEstimation) | Gets the operation mode of frequency error estimation. If frequency error is absent in the signal to be analyzed, you may disable frequency estimation to reduce measurement time or to avoid measurement inaccuracy due to error in frequency error estimation. |
| GetIQGainImbalanceCorrectionEnabled(string, out RFmxNRMXModAccIQGainImbalanceCorrectionEnabled) | Gets whether to enable IQ gain imbalance correction. |
| GetIQImpairmentsModel(string, out RFmxNRMXModAccIQImpairmentsModel) | Gets the I/Q impairments model used by the measurement for estimating I/Q impairments. |
| GetIQImpairmentsPerSubcarrierEnabled(string, out RFmxNRMXModAccIQImpairmentsPerSubcarrierEnabled) | Gets whether to return I/Q impairments independently for each subcarrier. |
| GetIQMismatchEstimationEnabled(string, out RFmxNRMXModAccIQMismatchEstimationEnabled) | Gets whether to estimate the IQ impairments such as IQ gain imbalance and quadrature skew. |
| GetIQOriginOffsetEstimationEnabled(string, out RFmxNRMXModAccIQOriginOffsetEstimationEnabled) | Gets whether to estimate the IQ origin offset. If IQ origin offset is absent in the signal to be analyzed, you may disable IQ origin offset estimation to reduce measurement time or to avoid measurement inaccuracy due to error in IQ origin offset estimation. |
| GetIQQuadratureErrorCorrectionEnabled(string, out RFmxNRMXModAccIQQuadratureErrorCorrectionEnabled) | Gets whether to enable IQ quadrature error correction. |
| GetIQTimingSkewCorrectionEnabled(string, out RFmxNRMXModAccIQTimingSkewCorrectionEnabled) | Gets whether to enable IQ timing skew correction. |
| GetMagnitudeAndPhaseErrorEnabled(string, out RFmxNRMXModAccMagnitudeAndPhaseErrorEnabled) | Gets whether to measure the magnitude and the phase error. |
| GetMeasurementEnabled(string, out bool) | Gets whether to enable the ModAcc measurement. |
| GetMeasurementLength(string, out double) | Gets the measurement length in units specified by Measurement Length Unit method. |
| GetMeasurementLengthUnit(string, out RFmxNRMXModAccMeasurementLengthUnit) | Gets the units in which measurement offset and measurement length are specified. |
| GetMeasurementMode(string, out RFmxNRMXModAccMeasurementMode) | Gets whether the measurement should calibrate the noise floor of the analyzer or perform the ModAcc measurement. |
| GetMeasurementOffset(string, out double) | Gets the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxNRMXModAccSynchronizationMode) method. The unit for this is specified by ModAcc Measurement Length Unit. |
| GetMulticarrierFilterEnabled(string, out RFmxNRMXModAccMulticarrierFilterEnabled) | Gets whether to use the filter in single carrier configurations to minimize leakage into the carrier. Measurement ignores this method, if number of carriers is set to more than 1 or if you set the SetAcquisitionBandwidthOptimizationEnabled(string, RFmxNRMXAcquisitionBandwidthOptimizationEnabled) method to False, where in the multi carrier filter will always be used. |
| GetNoiseCompensationEnabled(string, out RFmxNRMXModAccNoiseCompensationEnabled) | Gets whether the contribution of the instrument noise is compensated for EVM computation. You must measure the noise floor before applying the noise compensation. The instrument noise floor is measured for the RF path used by the ModAcc measurement and cached for future use. |
| GetNoiseCompensationInputPowerCheckEnabled(string, out RFmxNRMXModAccNoiseCompensationInputPowerCheckEnabled) | Gets whether the measurement checks if any high power signal is present at the RFIn port of the instrument while performing noise floor calibration. |
| GetNoiseCompensationReferenceLevelCoercionLimit(string, out double) | Gets the coercion limit for the reference level for noise compensation. When you set the SetMeasurementMode(string, RFmxNRMXModAccMeasurementMode) method to Measure and SetNoiseCompensationEnabled(string, RFmxNRMXModAccNoiseCompensationEnabled) method to True, the measurement attempts to read noise floor calibration data corresponding to the configured reference level. If noise floor calibration data corresponding to the configured reference level is not found in the calibration database, the measurement attempts to read noise floor calibration data from the calibration database for any reference level in the range of the configured reference level plus or minus the coercion limit you set for this method. |
| GetNumberOfAnalysisThreads(string, out int) | Gets the maximum number of threads used for parallelism for the ModAcc measurement. |
| GetPhaseTrackingMode(string, out RFmxNRMXModAccPhaseTrackingMode) | Gets the method used for phase tracking. |
| GetPreFftErrorEstimationInterval(string, out RFmxNRMXModAccPreFftErrorEstimationInterval) | Gets the interval used for Pre-FFT error estimation. |
| GetShortFrameEnabled(string, out RFmxNRMXModAccShortFrameEnabled) | Gets whether the input signal has a periodicity shorter than the NR frame duration. |
| GetShortFrameLength(string, out double) | Gets the short frame periodicity in unit specified by Short Frame Length Unit. |
| GetShortFrameLengthUnit(string, out RFmxNRMXModAccShortFrameLengthUnit) | Gets the units in which Short Frame Length is specified. |
| GetSpectralFlatnessCondition(string, out RFmxNRMXModAccSpectralFlatnessCondition) | Gets the test condition for Spectral Flatness measurement. |
| GetSpectrumInverted(string, out RFmxNRMXModAccSpectrumInverted) | Gets whether the spectrum of the signal being measured is inverted. This happens when I and Q component of the baseband complex signal is swapped. |
| GetSymbolClockErrorEstimationEnabled(string, out RFmxNRMXModAccSymbolClockErrorEstimationEnabled) | Gets whether to estimate symbol clock error. This method is ignored when the Common Clock Source Enabled method is True and the Frequency Error Estimation method is Disabled, in which case, symbol clock error is not estimated. If symbol clock error is absent in the signal to be analyzed, you may disable symbol clock error estimation to reduce measurement time or to avoid measurement inaccuracy due to error in symbol clock error estimation. |
| GetSynchronizationMode(string, out RFmxNRMXModAccSynchronizationMode) | Gets whether the measurement is performed from slot or frame boundary. |
| GetTimingTrackingMode(string, out RFmxNRMXModAccTimingTrackingMode) | Gets the method used for timing tracking. |
| GetTransientPeriod(string, out double) | It configures the transient duration as specified in section 6.4.2.1a of 3GPP 38.101-1 specification. |
| GetTransientPeriodEvmMode(string, out RFmxNRMXModAccTransientPeriodEvmMode) | Configures the EVM measurement behavior for symbols affected by power transients. |
| GetTransientPowerChangeThreshold(string, out double) | Gets transient period power change threshold level in dB. |
| SetAllTracesEnabled(string, bool) | Sets whether to enable the traces to be stored and retrieved after performing the ModAcc measurement. |
| SetAutoLevelAllowOverflow(string, RFmxNRMXModAccAutoLevelAllowOverflow) | Sets whether the AutoLevel(string, double) function should search for the optimum reference levels while allowing ADC overflow. |
| SetAveragingCount(string, int) | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxNRMXModAccAveragingEnabled) method to True. |
| SetAveragingEnabled(string, RFmxNRMXModAccAveragingEnabled) | Enables averaging for the measurement. |
| SetChannelEstimationType(string, RFmxNRMXModAccChannelEstimationType) | Sets the method used for channel estimation. |
| SetCommonClockSourceEnabled(string, RFmxNRMXModAccCommonClockSourceEnabled) | Sets whether same reference clock is used for local oscillator and digital-to-analog converter. When same reference clock is used the Carrier Frequency Offset is proportional to Sample Clock Error. |
| SetCompositeResultsIncludeDmrs(string, RFmxNRMXModAccCompositeResultsIncludeDmrs) | Sets whether the DMRS resource elements are included for composite EVM and magnitude and phase error results and traces. |
| SetCompositeResultsIncludePtrs(string, RFmxNRMXModAccCompositeResultsIncludePtrs) | Sets whether the PTRS resource elements are included for composite EVM and magnitude and phase error results and traces. |
| SetDCSubcarrierRemovalEnabled(string, RFmxNRMXModAccDCSubcarrierRemovalEnabled) | Sets whether the DC subcarrier is removed from the EVM results. |
| SetEvmReferenceDataSymbolsMode(string, RFmxNRMXModAccEvmReferenceDataSymbolsMode) | Sets whether to either use a reference waveform or an acquired waveform to create reference data symbols for EVM computation. |
| SetEvmUnit(string, RFmxNRMXModAccEvmUnit) | Sets the units of the EVM results. |
| SetFftWindowLength(string, double) | Sets the FFT window length (W). This value is expressed as a percentage of the cyclic prefix length. This method is used when you set the SetFftWindowType(string, RFmxNRMXModAccFftWindowType) method to Type3GPP, where it is needed to calculate the EVM using two different FFT window positions, Delta_C-W/2, and Delta_C+W/2. |
| SetFftWindowOffset(string, double) | Sets the position of the FFT window used to calculate the EVM when SetFftWindowType(string, RFmxNRMXModAccFftWindowType) method is set to TypeCustom. The offset is expressed as a percentage of the cyclic prefix length. If you set this method to 0, the EVM window starts at the end of cyclic prefix. If you set this method to 100, the EVM window starts at the beginning of cyclic prefix. |
| SetFftWindowType(string, RFmxNRMXModAccFftWindowType) | Sets the FFT window type used for EVM calculation. |
| SetFrequencyErrorEstimation(string, RFmxNRMXModAccFrequencyErrorEstimation) | Sets the operation mode of frequency error estimation. If frequency error is absent in the signal to be analyzed, you may disable frequency estimation to reduce measurement time or to avoid measurement inaccuracy due to error in frequency error estimation. |
| SetIQGainImbalanceCorrectionEnabled(string, RFmxNRMXModAccIQGainImbalanceCorrectionEnabled) | Sets whether to enable IQ gain imbalance correction. |
| SetIQImpairmentsModel(string, RFmxNRMXModAccIQImpairmentsModel) | Sets the I/Q impairments model used by the measurement for estimating I/Q impairments. |
| SetIQImpairmentsPerSubcarrierEnabled(string, RFmxNRMXModAccIQImpairmentsPerSubcarrierEnabled) | Sets whether to return I/Q impairments independently for each subcarrier. |
| SetIQMismatchEstimationEnabled(string, RFmxNRMXModAccIQMismatchEstimationEnabled) | Sets whether to estimate the IQ impairments such as IQ gain imbalance and quadrature skew. |
| SetIQOriginOffsetEstimationEnabled(string, RFmxNRMXModAccIQOriginOffsetEstimationEnabled) | Sets whether to estimate the IQ origin offset. If IQ origin offset is absent in the signal to be analyzed, you may disable IQ origin offset estimation to reduce measurement time or to avoid measurement inaccuracy due to error in IQ origin offset estimation. |
| SetIQQuadratureErrorCorrectionEnabled(string, RFmxNRMXModAccIQQuadratureErrorCorrectionEnabled) | Sets whether to enable IQ quadrature error correction. |
| SetIQTimingSkewCorrectionEnabled(string, RFmxNRMXModAccIQTimingSkewCorrectionEnabled) | Sets whether to enable IQ timing skew correction. |
| SetMagnitudeAndPhaseErrorEnabled(string, RFmxNRMXModAccMagnitudeAndPhaseErrorEnabled) | Sets whether to measure the magnitude and the phase error. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable the ModAcc measurement. |
| SetMeasurementLength(string, double) | Sets the measurement length in units specified by Measurement Length Unit method. |
| SetMeasurementLengthUnit(string, RFmxNRMXModAccMeasurementLengthUnit) | Sets the units in which measurement offset and measurement length are specified. |
| SetMeasurementMode(string, RFmxNRMXModAccMeasurementMode) | Sets whether the measurement should calibrate the noise floor of the analyzer or perform the ModAcc measurement. |
| SetMeasurementOffset(string, double) | Sets the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SetSynchronizationMode(string, RFmxNRMXModAccSynchronizationMode) method. The unit for this is specified by ModAcc Measurement Length Unit. |
| SetMulticarrierFilterEnabled(string, RFmxNRMXModAccMulticarrierFilterEnabled) | Sets whether to use the filter in single carrier configurations to minimize leakage into the carrier. Measurement ignores this method, if number of carriers is set to more than 1 or if you set the SetAcquisitionBandwidthOptimizationEnabled(string, RFmxNRMXAcquisitionBandwidthOptimizationEnabled) method to False, where in the multi carrier filter will always be used. |
| SetNoiseCompensationEnabled(string, RFmxNRMXModAccNoiseCompensationEnabled) | Sets whether the contribution of the instrument noise is compensated for EVM computation. You must measure the noise floor before applying the noise compensation. The instrument noise floor is measured for the RF path used by the ModAcc measurement and cached for future use. |
| SetNoiseCompensationInputPowerCheckEnabled(string, RFmxNRMXModAccNoiseCompensationInputPowerCheckEnabled) | Sets whether the measurement checks if any high power signal is present at the RFIn port of the instrument while performing noise floor calibration. |
| SetNoiseCompensationReferenceLevelCoercionLimit(string, double) | Sets the coercion limit for the reference level for noise compensation. When you set the SetMeasurementMode(string, RFmxNRMXModAccMeasurementMode) method to Measure and SetNoiseCompensationEnabled(string, RFmxNRMXModAccNoiseCompensationEnabled) method to True, the measurement attempts to read noise floor calibration data corresponding to the configured reference level. If noise floor calibration data corresponding to the configured reference level is not found in the calibration database, the measurement attempts to read noise floor calibration data from the calibration database for any reference level in the range of the configured reference level plus or minus the coercion limit you set for this method. |
| SetNumberOfAnalysisThreads(string, int) | Sets the maximum number of threads used for parallelism for the ModAcc measurement. |
| SetPhaseTrackingMode(string, RFmxNRMXModAccPhaseTrackingMode) | Sets the method used for phase tracking. |
| SetPreFftErrorEstimationInterval(string, RFmxNRMXModAccPreFftErrorEstimationInterval) | Sets the interval used for Pre-FFT error estimation. |
| SetShortFrameEnabled(string, RFmxNRMXModAccShortFrameEnabled) | Sets whether the input signal has a periodicity shorter than the NR frame duration. |
| SetShortFrameLength(string, double) | Sets the short frame periodicity in unit specified by Short Frame Length Unit. |
| SetShortFrameLengthUnit(string, RFmxNRMXModAccShortFrameLengthUnit) | Sets the units in which Short Frame Length is specified. |
| SetSpectralFlatnessCondition(string, RFmxNRMXModAccSpectralFlatnessCondition) | Sets the test condition for Spectral Flatness measurement. |
| SetSpectrumInverted(string, RFmxNRMXModAccSpectrumInverted) | Sets whether the spectrum of the signal being measured is inverted. This happens when I and Q component of the baseband complex signal is swapped. |
| SetSymbolClockErrorEstimationEnabled(string, RFmxNRMXModAccSymbolClockErrorEstimationEnabled) | Sets whether to estimate symbol clock error. This method is ignored when the Common Clock Source Enabled method is True and the Frequency Error Estimation method is Disabled, in which case, symbol clock error is not estimated. If symbol clock error is absent in the signal to be analyzed, you may disable symbol clock error estimation to reduce measurement time or to avoid measurement inaccuracy due to error in symbol clock error estimation. |
| SetSynchronizationMode(string, RFmxNRMXModAccSynchronizationMode) | Sets whether the measurement is performed from slot or frame boundary. |
| SetTimingTrackingMode(string, RFmxNRMXModAccTimingTrackingMode) | Sets the method used for timing tracking. |
| SetTransientPeriod(string, double) | It configures the transient duration as specified in section 6.4.2.1a of 3GPP 38.101-1 specification. |
| SetTransientPeriodEvmMode(string, RFmxNRMXModAccTransientPeriodEvmMode) | Configures the EVM measurement behavior for symbols affected by power transients. |
| SetTransientPowerChangeThreshold(string, double) | Sets transient period power change threshold level in dB. |
| ValidateCalibrationData(string, out RFmxNRMXModAccCalibrationDataValid) | Specifies whether calibration data is valid for the configuration specified by the signal name in the selectorString parameter. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccdcsubcarrierremovalenabled.html language=enus -->
## TOPIC 00286: RFmxNRMXModAccDCSubcarrierRemovalEnabled Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccdcsubcarrierremovalenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccdcsubcarrierremovalenabled.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the DC subcarrier is removed from the EVM results. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXModAccDCSubcarrierRemovalEnabledMembersNameValueDescriptionFalse0The DC subcarrier is present in the EVM results. True1The DC subcarrier is removed from the EVM resu

### RFmxNRMXModAccDCSubcarrierRemovalEnabled Enumeration

Specifies whether the DC subcarrier is removed from the EVM results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXModAccDCSubcarrierRemovalEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The DC subcarrier is present in the EVM results. |
| True | 1 | The DC subcarrier is removed from the EVM results. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccfftwindowtype.html language=enus -->
## TOPIC 00287: RFmxNRMXModAccFftWindowType Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccfftwindowtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccfftwindowtype.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the FFT window type used for EVM calculation. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXModAccFftWindowTypeMembersNameValueDescriptionType3GPP0The maximum EVM between the start window position and the end window position is returned according to the 3GPP specificati

### RFmxNRMXModAccFftWindowType Enumeration

Specifies the FFT window type used for EVM calculation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXModAccFftWindowType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Type3GPP | 0 | The maximum EVM between the start window position and the end window position is returned according to the 3GPP specification. The FFT window positions are specified by the method. |
| TypeCustom | 1 | Only one FFT window position is used for the EVM calculation. FFT window position is specified by SetFftWindowOffset(string, double) method. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccfrequencyerrorestimation.html language=enus -->
## TOPIC 00288: RFmxNRMXModAccFrequencyErrorEstimation Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccfrequencyerrorestimation.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccfrequencyerrorestimation.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the operation mode of frequency error estimation. If frequency error is absent in the signal to be analyzed, you may disable frequency estimation to reduce measurement time or to avoid measurement inaccuracy due to error in frequency error estimation. SyntaxNamespace: NationalInstruments.R

### RFmxNRMXModAccFrequencyErrorEstimation Enumeration

Specifies the operation mode of frequency error estimation. If frequency error is absent in the signal to be analyzed, you may disable frequency estimation to reduce measurement time or to avoid measurement inaccuracy due to error in frequency error estimation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXModAccFrequencyErrorEstimation

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Disabled | 0 | Frequency error estimation and correction is disabled. |
| Normal | 1 | Estimate and correct frequency error of range +/- half subcarrier spacing. |
| Wide | 2 | Estimate and correct frequency error of range +/- half resource block when SetAutoResourceBlockDetectionEnabled(string, RFmxNRMXAutoResourceBlockDetectionEnabled) is True, or range +/- number of guard subcarrier when SetAutoResourceBlockDetectionEnabled(string, RFmxNRMXAutoResourceBlockDetectionEnabled) is False. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodacciqgainimbalancecorrectionenabled.html language=enus -->
## TOPIC 00289: RFmxNRMXModAccIQGainImbalanceCorrectionEnabled Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodacciqgainimbalancecorrectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodacciqgainimbalancecorrectionenabled.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable IQ gain imbalance correction. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXModAccIQGainImbalanceCorrectionEnabledMembersNameValueDescriptionFalse0IQ gain imbalance correction is disabled. True1IQ gain imbalance correction is enabled.

### RFmxNRMXModAccIQGainImbalanceCorrectionEnabled Enumeration

Specifies whether to enable IQ gain imbalance correction.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXModAccIQGainImbalanceCorrectionEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | IQ gain imbalance correction is disabled. |
| True | 1 | IQ gain imbalance correction is enabled. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodacciqimpairmentsmodel.html language=enus -->
## TOPIC 00290: RFmxNRMXModAccIQImpairmentsModel Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodacciqimpairmentsmodel.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodacciqimpairmentsmodel.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the I/Q impairments model used by the measurement for estimating I/Q impairments. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXModAccIQImpairmentsModelMembersNameValueDescriptionTx0The measurement assumes that the I/Q impairments are introduced by a transmit DUT. Rx1Th

### RFmxNRMXModAccIQImpairmentsModel Enumeration

Specifies the I/Q impairments model used by the measurement for estimating I/Q impairments.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXModAccIQImpairmentsModel

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Tx | 0 | The measurement assumes that the I/Q impairments are introduced by a transmit DUT. |
| Rx | 1 | The measurement assumes that the I/Q impairments are introduced by a receive DUT. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodacciqquadratureerrorcorrectionenabled.html language=enus -->
## TOPIC 00291: RFmxNRMXModAccIQQuadratureErrorCorrectionEnabled Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodacciqquadratureerrorcorrectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodacciqquadratureerrorcorrectionenabled.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable IQ quadrature error correction. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXModAccIQQuadratureErrorCorrectionEnabledMembersNameValueDescriptionFalse0IQ quadrature error correction is disabled. True1IQ quadrature error correction is enabled.

### RFmxNRMXModAccIQQuadratureErrorCorrectionEnabled Enumeration

Specifies whether to enable IQ quadrature error correction.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXModAccIQQuadratureErrorCorrectionEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | IQ quadrature error correction is disabled. |
| True | 1 | IQ quadrature error correction is enabled. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodacciqtimingskewcorrectionenabled.html language=enus -->
## TOPIC 00292: RFmxNRMXModAccIQTimingSkewCorrectionEnabled Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodacciqtimingskewcorrectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodacciqtimingskewcorrectionenabled.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable IQ timing skew correction. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXModAccIQTimingSkewCorrectionEnabledMembersNameValueDescriptionFalse0IQ timing skew correction is disabled. True1IQ timing skew correction is enabled.

### RFmxNRMXModAccIQTimingSkewCorrectionEnabled Enumeration

Specifies whether to enable IQ timing skew correction.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXModAccIQTimingSkewCorrectionEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | IQ timing skew correction is disabled. |
| True | 1 | IQ timing skew correction is enabled. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccmagnitudeandphaseerrorenabled.html language=enus -->
## TOPIC 00293: RFmxNRMXModAccMagnitudeAndPhaseErrorEnabled Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccmagnitudeandphaseerrorenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccmagnitudeandphaseerrorenabled.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to measure the magnitude and the phase error. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXModAccMagnitudeAndPhaseErrorEnabledMembersNameValueDescriptionFalse0Indicates that magnitude error and phase error results computation is disabled. True1Indicates that ma

### RFmxNRMXModAccMagnitudeAndPhaseErrorEnabled Enumeration

Specifies whether to measure the magnitude and the phase error.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXModAccMagnitudeAndPhaseErrorEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Indicates that magnitude error and phase error results computation is disabled. |
| True | 1 | Indicates that magnitude error and phase error results computation is enabled. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccnoisecompensationapplied.html language=enus -->
## TOPIC 00294: RFmxNRMXModAccNoiseCompensationApplied Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccnoisecompensationapplied.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccnoisecompensationapplied.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the noise compensation is applied to the EVM measurement. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXModAccNoiseCompensationAppliedMembersNameValueDescriptionFalse0Noise compensation is not applied to the EVM measurement. True1Noise compensation is applied to

### RFmxNRMXModAccNoiseCompensationApplied Enumeration

Specifies whether the noise compensation is applied to the EVM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXModAccNoiseCompensationApplied

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Noise compensation is not applied to the EVM measurement. |
| True | 1 | Noise compensation is applied to the EVM measurement. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccpreffterrorestimationinterval.html language=enus -->
## TOPIC 00295: RFmxNRMXModAccPreFftErrorEstimationInterval Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccpreffterrorestimationinterval.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccpreffterrorestimationinterval.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the interval used for Pre-FFT error estimation. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXModAccPreFftErrorEstimationIntervalMembersNameValueDescriptionSlot0Frequency and timing error is estimated per slot in the pre-fft domain. MeasurementLength1Frequency and timin

### RFmxNRMXModAccPreFftErrorEstimationInterval Enumeration

Specifies the interval used for Pre-FFT error estimation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXModAccPreFftErrorEstimationInterval

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Slot | 0 | Frequency and timing error is estimated per slot in the pre-fft domain. |
| MeasurementLength | 1 | Frequency and timing error is estimated over the measurement interval in the pre-fft domain. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchiqgainimbalancepersubcarriermeantrace__string-double-ref.html language=enus -->
## TOPIC 00296: FetchIQGainImbalancePerSubcarrierMeanTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchiqgainimbalancepersubcarriermeantrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchiqgainimbalancepersubcarriermeantrace__string-double-ref.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches mean value of IQ Gain Imbalance. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int FetchIQGainImbalancePerSubcarrierMeanTrace(string selectorString, double timeout, re

### FetchIQGainImbalancePerSubcarrierMeanTrace(string, double, ref AnalogWaveform< float >)

Fetches mean value of IQ Gain Imbalance. 
 Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int FetchIQGainImbalancePerSubcarrierMeanTrace(string selectorString, double timeout, ref AnalogWaveform< float > IQGainImbalancePerSubcarrierMean)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| IQGainImbalancePerSubcarrierMean | ref AnalogWaveform< float > | Upon return, contains the mean value of IQ Gain Imbalance. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchpbchdmrsconstellationtrace__string-double-ref.html language=enus -->
## TOPIC 00297: FetchPbchDmrsConstellationTrace(string, double, ref ComplexSingle[])

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchpbchdmrsconstellationtrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchpbchdmrsconstellationtrace__string-double-ref.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PBCH DMRS trace. The constellation points of different slots in the measurement length is concatenated. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int FetchPbch

### FetchPbchDmrsConstellationTrace(string, double, ref ComplexSingle[])

Fetches the PBCH DMRS trace. The constellation points of different slots in the measurement length is concatenated. 
 Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int FetchPbchDmrsConstellationTrace(string selectorString, double timeout, ref ComplexSingle[] pbchDmrsConstellation)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| pbchDmrsConstellation | ref ComplexSingle[] | Upon return, contains the PBCH DMRS trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchpdsch1024qamconstellationtrace__string-double-ref.html language=enus -->
## TOPIC 00298: FetchPdsch1024QamConstellationTrace(string, double, ref ComplexSingle[])

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchpdsch1024qamconstellationtrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchpdsch1024qamconstellationtrace__string-double-ref.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PDSCH 1024 QAM constellation trace. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int FetchPdsch1024QamConstellationTrace(string selectorString, double timeout, re

### FetchPdsch1024QamConstellationTrace(string, double, ref ComplexSingle[])

Fetches the PDSCH 1024 QAM constellation trace. 
 Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int FetchPdsch1024QamConstellationTrace(string selectorString, double timeout, ref ComplexSingle[] qam1024Constellation)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| qam1024Constellation | ref ComplexSingle[] | Upon return, contains the 1024 QAM constellation trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchpdsch256qamconstellationtrace__string-double-ref.html language=enus -->
## TOPIC 00299: FetchPdsch256QamConstellationTrace(string, double, ref ComplexSingle[])

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchpdsch256qamconstellationtrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchpdsch256qamconstellationtrace__string-double-ref.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches PDSCH 256 QAM trace. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int FetchPdsch256QamConstellationTrace(string selectorString, double timeout, ref ComplexSingle[] qa

### FetchPdsch256QamConstellationTrace(string, double, ref ComplexSingle[])

Fetches PDSCH 256 QAM trace. 
 Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int FetchPdsch256QamConstellationTrace(string selectorString, double timeout, ref ComplexSingle[] qam256Constellation)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| qam256Constellation | ref ComplexSingle[] | Upon return, contains the 256 QAM constellation trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchpdsch8pskconstellationtrace__string-double-ref.html language=enus -->
## TOPIC 00300: FetchPdsch8PskConstellationTrace(string, double, ref ComplexSingle[])

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchpdsch8pskconstellationtrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchpdsch8pskconstellationtrace__string-double-ref.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches PDSCH 8 PSK constellation trace. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int FetchPdsch8PskConstellationTrace(string selectorString, double timeout, ref ComplexS

### FetchPdsch8PskConstellationTrace(string, double, ref ComplexSingle[])

Fetches PDSCH 8 PSK constellation trace. 
 Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int FetchPdsch8PskConstellationTrace(string selectorString, double timeout, ref ComplexSingle[] psk8Constellation)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| psk8Constellation | ref ComplexSingle[] | Upon return, contains the PDSCH 8 PSK constellation trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchpdschptrsconstellationtrace__string-double-ref.html language=enus -->
## TOPIC 00301: FetchPdschPtrsConstellationTrace(string, double, ref ComplexSingle[])

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchpdschptrsconstellationtrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchpdschptrsconstellationtrace__string-double-ref.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches PDSCH PTRS trace. Use "user(k)" or "carrier(l)" or "subblock(n)" or "subblock(n)/carrier(l)/user(k)" as the selector string to read this method.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int FetchPdschPtrsConstellationTrace(string selectorString, double timeout, ref ComplexSingle[]

### FetchPdschPtrsConstellationTrace(string, double, ref ComplexSingle[])

Fetches PDSCH PTRS trace. 
 Use "user(k)" or "carrier(l)" or "subblock(n)" or "subblock(n)/carrier(l)/user(k)" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int FetchPdschPtrsConstellationTrace(string selectorString, double timeout, ref ComplexSingle[] pdschPtrsConstellation)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and user number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0/user0""result::r1/subblock0/carrier0/user0" You can use the BuildUserString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| pdschPtrsConstellation | ref ComplexSingle[] | Upon return, contains the PDSCH PTRS constellation trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchpssconstellationtrace__string-double-ref.html language=enus -->
## TOPIC 00302: FetchPssConstellationTrace(string, double, ref ComplexSingle[])

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchpssconstellationtrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchpssconstellationtrace__string-double-ref.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PSS constellation trace. The constellation points of different slots in the measurement length is concatenated. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int F

### FetchPssConstellationTrace(string, double, ref ComplexSingle[])

Fetches the PSS constellation trace. The constellation points of different slots in the measurement length is concatenated. 
 Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int FetchPssConstellationTrace(string selectorString, double timeout, ref ComplexSingle[] pssConstellation)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| pssConstellation | ref ComplexSingle[] | Upon return, contains the PSS constellation trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchpssrmsevmpersubcarriermeantrace__string-double-ref.html language=enus -->
## TOPIC 00303: FetchPssRmsEvmPerSubcarrierMeanTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchpssrmsevmpersubcarriermeantrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchpssrmsevmpersubcarriermeantrace__string-double-ref.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean PSS RMS EVM of each subcarrier. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int FetchPssRmsEvmPerSubcarrierMeanTrace(string selectorString, double timeout,

### FetchPssRmsEvmPerSubcarrierMeanTrace(string, double, ref AnalogWaveform< float >)

Fetches the mean PSS RMS EVM of each subcarrier. 
 Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int FetchPssRmsEvmPerSubcarrierMeanTrace(string selectorString, double timeout, ref AnalogWaveform< float > pssRmsEvmPerSubcarrierMean)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| pssRmsEvmPerSubcarrierMean | ref AnalogWaveform< float > | Upon return, contains the RMS EVM of each subcarrier averaged across all the OFDM symbols allocated with PSS within the Meas Length. The unit of this EVM value is specified by the SetEvmUnit(string, RFmxNRMXModAccEvmUnit) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchpuschdmrsconstellationtrace__string-double-ref.html language=enus -->
## TOPIC 00304: FetchPuschDmrsConstellationTrace(string, double, ref ComplexSingle[])

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchpuschdmrsconstellationtrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchpuschdmrsconstellationtrace__string-double-ref.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches PUSCH DMRS trace. The constellation points of different slots in the measurement length is concatenated. Use "user(k)" or "carrier(l)" or "subblock(n)" or "subblock(n)/carrier(l)/user(k)" or "subblock(n)/carrier(k)/user(k)/layer(q)" as the selector string to read this method.SyntaxNamespace:

### FetchPuschDmrsConstellationTrace(string, double, ref ComplexSingle[])

Fetches PUSCH DMRS trace. The constellation points of different slots in the measurement length is concatenated. 
 Use "user(k)" or "carrier(l)" or "subblock(n)" or "subblock(n)/carrier(l)/user(k)" or "subblock(n)/carrier(k)/user(k)/layer(q)" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int FetchPuschDmrsConstellationTrace(string selectorString, double timeout, ref ComplexSingle[] puschDmrsConstellation)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, user number and layer number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0/user0/layer0""result::r1/subblock0/carrier0/user0/layer0" You can use the BuildUserString(string, int) and BuildLayerString(string, int) methods to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| puschDmrsConstellation | ref ComplexSingle[] | Upon return, contains the PDSCH DMRS constellation trace. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchrmsevmpersubcarriermeantrace__string-double-ref.html language=enus -->
## TOPIC 00305: FetchRmsEvmPerSubcarrierMeanTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchrmsevmpersubcarriermeantrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchrmsevmpersubcarriermeantrace__string-double-ref.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EVM of each allocated subcarrier averaged across all the symbols within the measurement length. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" or "subblock(n)/carrier(k)/layer(q)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.

### FetchRmsEvmPerSubcarrierMeanTrace(string, double, ref AnalogWaveform< float >)

Fetches the EVM of each allocated subcarrier averaged across all the symbols within the measurement length. 
 Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" or "subblock(n)/carrier(k)/layer(q)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int FetchRmsEvmPerSubcarrierMeanTrace(string selectorString, double timeout, ref AnalogWaveform< float > rmsEvmPerSubcarrierMean)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, carrier number and layer number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0/layer0""result::r1/subblock0/carrier0/layer0" You can use the BuildCarrierString(string, int) and BuildLayerString(string, int) methods to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| rmsEvmPerSubcarrierMean | ref AnalogWaveform< float > | Upon return, contains the EVM of each allocated subcarrier averaged across all the symbols within the measurement length. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchsssrmsevmpersymbolmeantrace__string-double-ref.html language=enus -->
## TOPIC 00306: FetchSssRmsEvmPerSymbolMeanTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchsssrmsevmpersymbolmeantrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-fetchsssrmsevmpersymbolmeantrace__string-double-ref.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean SSS RMS EVM of each symbol. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int FetchSssRmsEvmPerSymbolMeanTrace(string selectorString, double timeout, ref Anal

### FetchSssRmsEvmPerSymbolMeanTrace(string, double, ref AnalogWaveform< float >)

Fetches the mean SSS RMS EVM of each symbol. 
 Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int FetchSssRmsEvmPerSymbolMeanTrace(string selectorString, double timeout, ref AnalogWaveform< float > sssRmsEvmPerSymbolMean)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| sssRmsEvmPerSymbolMean | ref AnalogWaveform< float > | Upon return, contains the RMS EVM on each OFDM symbol averaged across all the defined subcarriers allocated with SSS within the Meas Length. The unit of this EVM value is specified by the SetEvmUnit(string, RFmxNRMXModAccEvmUnit) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-getcomponentcarriercrosspowermean__string-out.html language=enus -->
## TOPIC 00307: GetComponentCarrierCrossPowerMean(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-getcomponentcarriercrosspowermean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-getcomponentcarriercrosspowermean__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the cross power. The cross power for chain x is the power contribution from layers other than layer x in the chain. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetComponentCarrierCrossPowerMean(string selectorString, out double value)RemarksThis metho

### GetComponentCarrierCrossPowerMean(string, out double)

Gets the cross power. The cross power for chain x is the power contribution from layers other than layer x in the chain. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetComponentCarrierCrossPowerMean(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsComponentCarrierCrossPowerMean](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Chain number, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0/Chain0". You can use the BuildChainString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the cross power. The cross power for chain x is the power contribution from layers other than layer x in the chain. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-getcomponentcarrieriqtimingskewmean__string-out.html language=enus -->
## TOPIC 00308: GetComponentCarrierIQTimingSkewMean(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-getcomponentcarrieriqtimingskewmean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-getcomponentcarrieriqtimingskewmean__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the estimated IQ Timing Skew averaged over Meas Length. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetComponentCarrierIQTimingSkewMean(string selectorString, out double value)RemarksThis method gets the value of ModAccResultsComponentCarrierIQTimingSkewMean attribute.IQ Timing ske

### GetComponentCarrierIQTimingSkewMean(string, out double)

Gets the estimated IQ Timing Skew averaged over Meas Length.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetComponentCarrierIQTimingSkewMean(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsComponentCarrierIQTimingSkewMean](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.IQ Timing skew is the difference between the group delay of the in-phase (I) and quadrature (Q) components of the signal. This value is expressed in seconds.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the estimated IQ Timing Skew averaged over Meas Length. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-getpbchdmrspeakevmmaximum__string-out.html language=enus -->
## TOPIC 00309: GetPbchDmrsPeakEvmMaximum(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-getpbchdmrspeakevmmaximum__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-getpbchdmrspeakevmmaximum__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum value calculated over measurement length of peak EVMs calculated on PBCH DMRS symbols. When you set the SetEvmUnit(string, RFmxNRMXModAccEvmUnit) method to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit method to dB, the measurement

### GetPbchDmrsPeakEvmMaximum(string, out double)

Gets the maximum value calculated over measurement length of peak EVMs calculated on PBCH DMRS symbols. When you set the [SetEvmUnit(string, RFmxNRMXModAccEvmUnit)](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccconfiguration-setevmunit__string-rfmxnrmxmodaccevmunit.html) method to [Percentage](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccevmunit.html), the measurement returns this result as a percentage. When you set the ModAcc EVM Unit method to [dB](nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccevmunit.html), the measurement returns this result in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPbchDmrsPeakEvmMaximum(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsPbchDmrsPeakEvmMaximum](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the maximum value calculated over measurement length of peak EVMs calculated on PBCH DMRS symbols. When you set the SetEvmUnit(string, RFmxNRMXModAccEvmUnit) method to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit method to dB, the measurement returns this result in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-getpdsch4096qamrmsevmmean__string-out.html language=enus -->
## TOPIC 00310: GetPdsch4096QamRmsEvmMean(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-getpdsch4096qamrmsevmmean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-getpdsch4096qamrmsevmmean__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPdsch4096QamRmsEvmMean(string selectorString, out double value)

### GetPdsch4096QamRmsEvmMean(string, out double)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPdsch4096QamRmsEvmMean(string selectorString, out double value)

Parent topic:

RFmxNRMXModAccResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-getsubblockiqoriginoffsetmean__string-out.html language=enus -->
## TOPIC 00311: GetSubblockIQOriginOffsetMean(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-getsubblockiqoriginoffsetmean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-getsubblockiqoriginoffsetmean__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the estimated IQ origin offset averaged over measurement length in the subblock. This value is expressed in dBc. This result is valid only when you set the SetTransmitterArchitecture(string, RFmxNRMXTransmitterArchitecture) method to LOPerSubblock. SyntaxNamespace: NationalInstruments.RFmx.NRMX

### GetSubblockIQOriginOffsetMean(string, out double)

Gets the estimated IQ origin offset averaged over measurement length in the subblock. This value is expressed in dBc. This result is valid only when you set the [SetTransmitterArchitecture(string, RFmxNRMXTransmitterArchitecture)](nationalinstruments-rfmx-nrmx-rfmxnrmx-settransmitterarchitecture__string-rfmxnrmxtransmitterarchitecture.html) method to [LOPerSubblock](nationalinstruments-rfmx-nrmx-rfmxnrmxtransmitterarchitecture.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetSubblockIQOriginOffsetMean(string selectorString, out double value)

#### Remarks

This method gets the value of [ModAccResultsSubblockIQOriginOffsetMean](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Chain number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Chain0". You can use the BuildChainString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the estimated IQ origin offset averaged over measurement length in the subblock. This value is expressed in dBc. This result is valid only when you set the SetTransmitterArchitecture(string, RFmxNRMXTransmitterArchitecture) method to LOPerSubblock. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-getsubblocklocomponentcarrierindex__string-out.html language=enus -->
## TOPIC 00312: GetSubblockLOComponentCarrierIndex(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-getsubblocklocomponentcarrierindex__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-getsubblocklocomponentcarrierindex__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the index of the component carrier that includes the LO of the transmitter according to the SetSubblockFrequency(string, double) and SetSubblockTransmitLOFrequency(string, double) properties. If the LO of the transmitter doesn't fall into any component carrier of the subblock, the method return

### GetSubblockLOComponentCarrierIndex(string, out int)

Gets the index of the component carrier that includes the LO of the transmitter according to the [SetSubblockFrequency(string, double)](nationalinstruments-rfmx-nrmx-rfmxnrmx-setsubblockfrequency__string-double.html) and [SetSubblockTransmitLOFrequency(string, double)](nationalinstruments-rfmx-nrmx-rfmxnrmx-setsubblocktransmitlofrequency__string-double.html) properties. If the LO of the transmitter doesn't fall into any component carrier of the subblock, the method returns -1. This result is valid only when you set the [SetTransmitterArchitecture(string, RFmxNRMXTransmitterArchitecture)](nationalinstruments-rfmx-nrmx-rfmxnrmx-settransmitterarchitecture__string-rfmxnrmxtransmitterarchitecture.html) method to [LOPerSubblock](nationalinstruments-rfmx-nrmx-rfmxnrmxtransmitterarchitecture.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetSubblockLOComponentCarrierIndex(string selectorString, out int value)

#### Remarks

This method gets the value of [ModAccResultsSubblockLOComponentCarrierIndex](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Chain number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Chain0". You can use the BuildChainString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the index of the component carrier that includes the LO of the transmitter according to the SetSubblockFrequency(string, double) and SetSubblockTransmitLOFrequency(string, double) properties. If the LO of the transmitter doesn't fall into any component carrier of the subblock, the method returns -1. This result is valid only when you set the SetTransmitterArchitecture(string, RFmxNRMXTransmitterArchitecture) method to LOPerSubblock. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-getsubblocklosubcarrierindex__string-out.html language=enus -->
## TOPIC 00313: GetSubblockLOSubcarrierIndex(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-getsubblocklosubcarrierindex__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults-getsubblocklosubcarrierindex__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the subcarrier index within the respective component carrier where the transmitter LO is located. Due to its dependence on SetSubblockFrequency(string, double) and SetSubblockTransmitLOFrequency(string, double) properties, the value can be fractional, and the LO might reside in between subcarri

### GetSubblockLOSubcarrierIndex(string, out int)

Gets the subcarrier index within the respective component carrier where the transmitter LO is located. Due to its dependence on [SetSubblockFrequency(string, double)](nationalinstruments-rfmx-nrmx-rfmxnrmx-setsubblockfrequency__string-double.html) and [SetSubblockTransmitLOFrequency(string, double)](nationalinstruments-rfmx-nrmx-rfmxnrmx-setsubblocktransmitlofrequency__string-double.html) properties, the value can be fractional, and the LO might reside in between subcarriers of a component carrier. This result is valid only when you set the [SetTransmitterArchitecture(string, RFmxNRMXTransmitterArchitecture)](nationalinstruments-rfmx-nrmx-rfmxnrmx-settransmitterarchitecture__string-rfmxnrmxtransmitterarchitecture.html) method to [LOPerSubblock](nationalinstruments-rfmx-nrmx-rfmxnrmxtransmitterarchitecture.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetSubblockLOSubcarrierIndex(string selectorString, out int value)

#### Remarks

This method gets the value of [ModAccResultsSubblockLOSubcarrierIndex](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Chain number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Chain0". You can use the BuildChainString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the subcarrier index within the respective component carrier where the transmitter LO is located. Due to its dependence on SetSubblockFrequency(string, double) and SetSubblockTransmitLOFrequency(string, double) properties, the value can be fractional, and the LO might reside in between subcarriers of a component carrier. This result is valid only when you set the SetTransmitterArchitecture(string, RFmxNRMXTransmitterArchitecture) method to LOPerSubblock. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXModAccResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults.html language=enus -->
## TOPIC 00314: RFmxNRMXModAccResults Class

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccresults.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the ModAcc measurement results. Derives fromRFmxNRMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.NRMXpublic class RFmxNRMXModAccResults : RFmxNRMXSubObjectMethodsNameDescriptionFetchCompositeEvm(string, double, out double, out double)Fetches the composite EVM

### RFmxNRMXModAccResults Class

Provides methods to fetch and read the ModAcc measurement results.

#### Derives from

- RFmxNRMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public class RFmxNRMXModAccResults : RFmxNRMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchCompositeEvm(string, double, out double, out double) | Fetches the composite EVM for ModAcc measurements. Use "carrier(k)" or "subblock(n)/carrier(k)" or "subblock(n)/carrier(k)/layer(q)" as the selector string to read results from this method. |
| FetchFrequencyErrorMean(string, double, out double) | Fetches the estimated carrier frequency offset averaged over measurement length. This value is expressed in Hz. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" or "subblock(n)/carrier(k)/layer(q)" as the selector string to read this result. |
| FetchFrequencyErrorPerSlotMaximumTrace(string, double, ref AnalogWaveform< float >) | Fetches an array of the maximum value across averaging counts of the frequency error per slot for all slots within the measurement length. This value is expressed in Hz. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" or "subblock(n)/carrier(k)/layer(q)" as the selector string to read this result. |
| FetchInBandEmissionTrace(string, double, ref AnalogWaveform< float >, ref AnalogWaveform< float >) | Fetches the in-band emission trace and limits trace for the component carrier. In-band emission is measured as the ratio of the power in non-allocated resource blocks to the power in the allocated resource blocks averaged over the measurement interval. The IBE for various regions (general, carrier leakage, and I/Q Image) are obtained and concatenated to form a composite trace and the limits are defined in section 6.4.2.3 of 3GPP 38.101-1, and section 6.4.2.3 of 3GPP 38.101-2. The trace is not returned when there is full allocation of bandwidth, or there is clustered PUSCH or there is more than one active component carrier. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" or "subblock(n)/carrier(k)/chain(r)" as the selector string to read results from this method. |
| FetchIQGainImbalancePerSubcarrierMeanTrace(string, double, ref AnalogWaveform< float >) | Fetches mean value of IQ Gain Imbalance. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
| FetchIQQuadratureErrorPerSubcarrierMeanTrace(string, double, ref AnalogWaveform< float >) | Fetches the mean value of IQ Quadrature Error. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
| FetchPbchDataConstellationTrace(string, double, ref ComplexSingle[]) | Fetches the PBCH data trace. The constellation points of different slots in the measurement length is concatenated. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
| FetchPbchDataRmsEvmPerSubcarrierMeanTrace(string, double, ref AnalogWaveform< float >) | Fetches the mean PBCH data RMS EVM of each subcarrier. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
| FetchPbchDataRmsEvmPerSymbolMeanTrace(string, double, ref AnalogWaveform< float >) | Fetches the mean PBCH data RMS EVM for each symbol. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
| FetchPbchDmrsConstellationTrace(string, double, ref ComplexSingle[]) | Fetches the PBCH DMRS trace. The constellation points of different slots in the measurement length is concatenated. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
| FetchPbchDmrsRmsEvmPerSubcarrierMeanTrace(string, double, ref AnalogWaveform< float >) | Fetches the mean PBCH DMRS RMS EVM for each subcarrier. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
| FetchPbchDmrsRmsEvmPerSymbolMeanTrace(string, double, ref AnalogWaveform< float >) | Fetches the mean PBCH DMRS RMS EVM for each symbol. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
| FetchPdsch1024QamConstellationTrace(string, double, ref ComplexSingle[]) | Fetches the PDSCH 1024 QAM constellation trace. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
| FetchPdsch16QamConstellationTrace(string, double, ref ComplexSingle[]) | Fetches PDSCH 16 QAM trace. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
| FetchPdsch256QamConstellationTrace(string, double, ref ComplexSingle[]) | Fetches PDSCH 256 QAM trace. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
| FetchPdsch4096QamConstellationTrace(string, double, ref ComplexSingle[]) |  |
| FetchPdsch64QamConstellationTrace(string, double, ref ComplexSingle[]) | Fetches PDSCH 64 QAM trace. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
| FetchPdsch8PskConstellationTrace(string, double, ref ComplexSingle[]) | Fetches PDSCH 8 PSK constellation trace. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
| FetchPdschDataConstellationTrace(string, double, ref ComplexSingle[]) | Fetches the recovered PDSCH data constellation points. The constellation points of different slots in the measurement length is concatenated. Use "user(k)" or "carrier(l)" or "subblock(n)" or "subblock(n)/carrier(l)/user(k)" as the selector string to read this method. |
| FetchPdschDemodulatedBits(string, double, ref sbyte[]) | Fetches the recovered bits during EVM calculation. The bits of different slots in the measurement length are concatenated. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
| FetchPdschDmrsConstellationTrace(string, double, ref ComplexSingle[]) | Fetches PDSCH DMRS trace. The constellation points of different slots in the measurement length is concatenated. Use "user(k)" or "carrier(l)" or "subblock(n)" or "subblock(n)/carrier(l)/user(k)" as the selector string to read this method. |
| FetchPdschPtrsConstellationTrace(string, double, ref ComplexSingle[]) | Fetches PDSCH PTRS trace. Use "user(k)" or "carrier(l)" or "subblock(n)" or "subblock(n)/carrier(l)/user(k)" as the selector string to read this method. |
| FetchPdschQpskConstellationTrace(string, double, ref ComplexSingle[]) | Fetches PDSCH QPSK trace. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
| FetchPeakEvmHighPerSymbolMaximumTrace(string, double, ref AnalogWaveform< float >) | Fetches the peak EVM per symbol trace for all confgured slots. The EVM is obtained by using FFT window position Delta_C+W/2. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" or "subblock(n)/carrier(k)/layer(q)" as the selector string to read results from this method. |
| FetchPeakEvmLowPerSymbolMaximumTrace(string, double, ref AnalogWaveform< float >) | Fetches the peak EVM per symbol trace for all confgured slots. The EVM is obtained by using FFT window position Delta_C-W/2. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" or "subblock(n)/carrier(k)/layer(q)" as the selector string to read results from this method. |
| FetchPeakEvmPerSlotMaximumTrace(string, double, ref AnalogWaveform< float >) | Fetches the peak value of EVM for each slot computed across all the symbols and all the allocated subcarriers. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)"or "subblock(n)/carrier(k)/layer(q)" as the selector string to read results from this method. |
| FetchPeakEvmPerSubcarrierMaximumTrace(string, double, ref AnalogWaveform< float >) | Fetches the peak value of EVM for each allocated subcarrier computed across all the symbols within the measurement length. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" or "subblock(n)/carrier(k)/layer(q)" as the selector string to read results from this method. |
| FetchPeakEvmPerSymbolMaximumTrace(string, double, ref AnalogWaveform< float >) | Fetches the peak value of EVM for each symbol computed across all the allocated subcarriers. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" or "subblock(n)/carrier(k)/layer(q)" as the selector string to read results from this method. |
| FetchPssConstellationTrace(string, double, ref ComplexSingle[]) | Fetches the PSS constellation trace. The constellation points of different slots in the measurement length is concatenated. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
| FetchPssRmsEvmPerSubcarrierMeanTrace(string, double, ref AnalogWaveform< float >) | Fetches the mean PSS RMS EVM of each subcarrier. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
| FetchPssRmsEvmPerSymbolMeanTrace(string, double, ref AnalogWaveform< float >) | Fetches the mean PSS RMS EVM of each symbol. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
| FetchPuschDataConstellationTrace(string, double, ref ComplexSingle[]) | Fetches PUSCH Data Constellation trace. The constellation points of different slots in the measurement length is concatenated. Use "user(k)" or "carrier(l)" or "subblock(n)" or "subblock(n)/carrier(l)/user(k)" or "subblock(n)/carrier(k)/user(k)/layer(q)" as the selector string to read this method. |
| FetchPuschDemodulatedBits(string, double, ref sbyte[]) | Fetches the recovered bits during EVM calculation. The bits of different slots in the measurement length are concatenated. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" or "subblock(n)/carrier(k)/layer(q)" as the selector string to read results from this method. |
| FetchPuschDmrsConstellationTrace(string, double, ref ComplexSingle[]) | Fetches PUSCH DMRS trace. The constellation points of different slots in the measurement length is concatenated. Use "user(k)" or "carrier(l)" or "subblock(n)" or "subblock(n)/carrier(l)/user(k)" or "subblock(n)/carrier(k)/user(k)/layer(q)" as the selector string to read this method. |
| FetchPuschPhaseOffsetTrace(string, double, ref AnalogWaveform< float >) | Returns the phase offset for the slots with respect to the reference slot. Use "user(k)" or "carrier(l)" or "subblock(n)" or "subblock(n)/carrier(l)/user(k)" or "subblock(n)/carrier(k)/user(k)/layer(q)" as the selector string to read this method. |
| FetchPuschPtrsConstellationTrace(string, double, ref ComplexSingle[]) | Fetches PUSCH PTRS trace. The constellation points of different slots in the measurement length is concatenated. Use "user(k)" or "carrier(l)" or "subblock(n)" or "subblock(n)/carrier(l)/user(k)" or "subblock(n)/carrier(k)/user(k)/layer(q)" as the selector string to read this method. |
| FetchRmsEvmHighPerSymbolMeanTrace(string, double, ref AnalogWaveform< float >) | Fetches the EVM per symbol trace for all confgured slots. The EVM is obtained by using FFT window position Delta_C+W/2. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" or "subblock(n)/carrier(k)/layer(q)" as the selector string to read results from this method. |
| FetchRmsEvmLowPerSymbolMeanTrace(string, double, ref AnalogWaveform< float >) | Fetches the EVM per symbol trace for all confgured slots. The EVM is obtained by using FFT window position Delta_C-W/2. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" or "subblock(n)/carrier(k)/layer(q)" as the selector string to read results from this method. |
| FetchRmsEvmPerSlotMeanTrace(string, double, ref AnalogWaveform< float >) | Fetches the EVM of each slot averaged across all the symbols and all the allocated subcarriers within each slot. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" or "subblock(n)/carrier(k)/layer(q)" as the selector string to read results from this method. |
| FetchRmsEvmPerSubcarrierMeanTrace(string, double, ref AnalogWaveform< float >) | Fetches the EVM of each allocated subcarrier averaged across all the symbols within the measurement length. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" or "subblock(n)/carrier(k)/layer(q)" as the selector string to read results from this method. |
| FetchRmsEvmPerSymbolMeanTrace(string, double, ref AnalogWaveform< float >) | Fetches the EVM on each symbol within the measurement length averaged across all the allocated subcarriers. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" or "subblock(n)/carrier(k)/layer(q)" as the selector string to read results from this method. |
| FetchSpectralFlatnessTrace(string, double, ref Spectrum< float >, ref Spectrum< float >, ref Spectrum< float >) | Returns the spectral flatness, upper mask, and lower mask traces. Spectral flatness is the magnitude of equalizer coefficients at each allocated subcarrier. Lower and upper masks are derived from section 6.5.2.4.5 of 3GPP TS 38.521-1 specification. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" or "subblock(n)/carrier(k)/layer(q)" as the selector string to read results from this method. |
| FetchSssConstellationTrace(string, double, ref ComplexSingle[]) | Fetches the SSS constellation trace. The constellation points of different slots in the measurement length is concatenated. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
| FetchSssRmsEvmPerSubcarrierMeanTrace(string, double, ref AnalogWaveform< float >) | Fetches the mean SSS RMS EVM of each subcarrier. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
| FetchSssRmsEvmPerSymbolMeanTrace(string, double, ref AnalogWaveform< float >) | Fetches the mean SSS RMS EVM of each symbol. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. |
| FetchSubblockInBandEmissionTrace(string, double, ref double[], ref double[], ref double[]) | Returns the in-band emission trace and limit trace for the the subblocks aggregated bandwidth. In-band emission is measured as the ratio of the power in non-allocated resource blocks to the power in the allocated resource blocks averaged over the measurement interval. The IBE for various regions (general, carrier leakage, and I/Q Image) are obtained and concatenated to form a composite trace and the limits are defined in section 6.4A.2.2.2 of 3GPP 38.101-1, and section 6.4A.2.3 of 3GPP 38.101-2. The trace is not returned when there is clustered PUSCH allocation, or when there is more than one active carrier, or when there is full allocation of resource blocks, or when carriers with different sub-carrier spacing are aggregated, or when the number of carriers is greater than 2. Use "subblock(n)" or "subblock(n)/chain(r)" as the selector string to read results from this method. |
| FetchTransientPeriodLocationsTrace(string, double, ref AnalogWaveform< float >) | Returns the symbol indices that were identified to have a transient period. Use "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)" as the selector string to read results from this method. The length of the trace is equal to the number of symbols within the measurement length. The trace returns a 1 for the symbol index that was identified to have a transient period; otherwise returns a 0. The trace is intended to be used as additional context information for the following traces: RMS EVM per Symbol Mean Trace RMS EVM-High per Symbol Mean Trace RMS EVM-Low per Symbol Mean Trace |
| GetComponentCarrierCrossPowerMean(string, out double) | Gets the cross power. The cross power for chain x is the power contribution from layers other than layer x in the chain. This value is expressed in dB. |
| GetComponentCarrierFrequencyErrorMean(string, out double) | Gets the estimated carrier frequency offset averaged over measurement length. This value is expressed in Hz. |
| GetComponentCarrierIQGainImbalanceMean(string, out double) | Gets the estimated IQ gain imbalance averaged over measurement length. This value is expressed in dB. IQ gain imbalance is the ratio of the amplitude of the I component to the Q component of the IQ signal being measured. |
| GetComponentCarrierIQOriginOffsetMean(string, out double) | Gets the estimated IQ origin offset averaged over measurement length. This value is expressed in dBc. |
| GetComponentCarrierIQTimingSkewMean(string, out double) | Gets the estimated IQ Timing Skew averaged over Meas Length. |
| GetComponentCarrierQuadratureErrorMean(string, out double) | Gets the estimated quadrature error averaged over measurement length. This value is expressed in degrees. Quadrature error is the measure of skewness in degree of the I component with respect to the Q component of the IQ signal being measured. |
| GetComponentCarrierSlotFrequencyErrorMaximum(string, out double) | Gets the estimated maximum per slot carrier frequency offset over the Measurement Length. |
| GetComponentCarrierSlotIQOriginOffsetMaximum(string, out double) | Gets the estimated maximum per slot carrier IQ origin offset over the Measurement Length. |
| GetComponentCarrierSymbolClockErrorMean(string, out double) | Gets the estimated sample clock error averaged over measurement length. This value is expressed in ppm. |
| GetComponentCarrierTimeAlignmentErrorMean(string, out double) |  |
| GetComponentCarrierTimeOffsetMean(string, out double) | Gets the time difference between the detected slot or frame boundary depending on the sync mode and reference trigger location. This value is expressed in seconds. |
| GetCompositePeakEvmBwpIndex(string, out int) | Gets the bandwidth part index where ModAcc Results Max Pk Composite EVM occurs. |
| GetCompositePeakEvmMaximum(string, out double) | Gets the maximum value of peak EVMs calculated over measurement length. If ModAcc Composite Results Include DMRS method and ModAcc Composite Results Include PTRS method are set to False, EVM is computed only for the shared channel. |
| GetCompositePeakEvmSlotIndex(string, out int) | Gets the slot index where ModAcc Results Max Pk Composite EVM occurs. |
| GetCompositePeakEvmSubcarrierIndex(string, out int) | Gets the subcarrier index where ModAcc Results Max Pk Composite EVM occurs. |
| GetCompositePeakEvmSymbolIndex(string, out int) | Gets the symbol index where ModAcc Results Max Pk Composite EVM occurs. |
| GetCompositePeakMagnitudeErrorMaximum(string, out double) | Gets the peak value of magnitude error calculated over measurement length on all configured channels. |
| GetCompositePeakPhaseErrorMaximum(string, out double) | Gets the peak value of Phase error calculated over measurement length on all configured channels. This value is expressed in degrees. |
| GetCompositeRmsEvmMean(string, out double) | Gets the mean value of RMS EVMs calculated over measurement length. If ModAcc Composite Results Include DMRS method and ModAcc Composite Results Include PTRS method are set to False, EVM is computed only for the shared channel. |
| GetCompositeRmsMagnitudeErrorMean(string, out double) | Gets the RMS mean value of magnitude error calculated over measurement length on all configured channels. |
| GetCompositeRmsPhaseErrorMean(string, out double) | Gets the RMS mean value of Phase error calculated over measurement length on all configured channels. This value is expressed in degrees. |
| GetDetectedCellID(string, out int) | Gets the detected Cell ID, if the SetAutoCellIDDetectionEnabled(string, RFmxNRMXAutoCellIDDetectionEnabled) method is set to True. A value of -1 is returned, if the measurement fails to auto detect the Cell ID.Gets the user configured Cell ID, if the Auto Cell ID Detection Enabled method is set to False. |
| GetInBandEmissionMargin(string, out double) | Gets In-Band Emission Margin of the component carrier. This value is expressed in dB. |
| GetNoiseCompensationApplied(string, out RFmxNRMXModAccNoiseCompensationApplied) | Gets whether the noise compensation is applied to the EVM measurement. |
| GetPbchDataPeakEvmMaximum(string, out double) | Gets the maximum value calculated over measurement length of peak EVMs calculated on PBCH data symbols. When you set the SetEvmUnit(string, RFmxNRMXModAccEvmUnit) method to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit method to dB, the measurement returns this result in dB. |
| GetPbchDataRmsEvmMean(string, out double) | Gets the mean value calculated over measurement length of RMS EVMs calculated on PBCH data symbols. When you set the SetEvmUnit(string, RFmxNRMXModAccEvmUnit) method to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit method to dB, the measurement returns this result in dB. |
| GetPbchDmrsPeakEvmMaximum(string, out double) | Gets the maximum value calculated over measurement length of peak EVMs calculated on PBCH DMRS symbols. When you set the SetEvmUnit(string, RFmxNRMXModAccEvmUnit) method to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit method to dB, the measurement returns this result in dB. |
| GetPbchDmrsRmsEvmMean(string, out double) | Gets the mean value calculated over measurement length of RMS EVMs calculated on PBCH DMRS symbols. When you set the SetEvmUnit(string, RFmxNRMXModAccEvmUnit) method to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit method to dB, the measurement returns this result in dB. |
| GetPdsch1024QamRmsEvmMean(string, out double) | Gets the mean value of RMS EVMs calculated over measurement length on all 1024 QAM modulated PDSCH data symbols. |
| GetPdsch16QamRmsEvmMean(string, out double) | Gets the mean value of RMS EVMs calculated over measurement length on all 16 QAM modulated PDSCH data symbols. |
| GetPdsch256QamRmsEvmMean(string, out double) | Gets the mean value of RMS EVMs calculated over measurement length on all 256 QAM modulated PDSCH data symbols. |
| GetPdsch4096QamRmsEvmMean(string, out double) |  |
| GetPdsch64QamRmsEvmMean(string, out double) | Gets the mean value of RMS EVMs calculated over measurement length on all 64 QAM modulated PDSCH data symbols. |
| GetPdsch8PskRmsEvmMean(string, out double) | Gets the mean value of RMS EVMs calculated over measurement length on all 8 PSK modulated PDSCH data symbols. |
| GetPdschDataPeakEvmMaximum(string, out double) | Gets the maximum value of peak EVMs calculated over measurement length on PDSCH data symbols. |
| GetPdschDataREPowerMean(string, out double) | Gets the mean value (over Meas Length) of power calculated on PDSCH data REs. |
| GetPdschDataRmsEvmMean(string, out double) | Gets the mean value of RMS EVMs calculated over measurement length on PDSCH data symbols. |
| GetPdschDmrsPeakEvmMaximum(string, out double) | Gets the maximum value of peak EVMs calculated over measurement length on PDSCH DMRS. |
| GetPdschDmrsREPowerMean(string, out double) | Gets the mean value (over Meas Length) of power calculated on PDSCH DMRS REs. |
| GetPdschDmrsRmsEvmMean(string, out double) | Gets the mean value of RMS EVMs calculated over measurement length on PDSCH DMRS. |
| GetPdschPtrsPeakEvmMaximum(string, out double) | Gets the maximum value of peak EVMs calculated over measurement length on PDSCH PTRS. |
| GetPdschPtrsREPowerMean(string, out double) | Gets the mean value (over Meas Length) of power calculated on PDSCH PTRS REs. |
| GetPdschPtrsRmsEvmMean(string, out double) | Gets the mean value of RMS EVMs calculated over measurement length on PDSCH PTRS. |
| GetPdschQpskRmsEvmMean(string, out double) | Gets the mean value of RMS EVMs calculated over measurement length on all QPSK modulated PDSCH data symbols. |
| GetPssPeakEvmMaximum(string, out double) | Gets the maximum value of peak EVMs calculated over measurement length on PSS symbols. When you set the SetEvmUnit(string, RFmxNRMXModAccEvmUnit) method to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit method to dB, the measurement returns this result in dB. |
| GetPssRmsEvmMean(string, out double) | Gets the mean value of RMS EVMs computed over measurement length on PSS symbols. When you set the SetEvmUnit(string, RFmxNRMXModAccEvmUnit) method to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit method to dB, the measurement returns this result in dB. |
| GetPuschDataPeakEvmMaximum(string, out double) | Gets the maximum value of peak EVMs calculated over measurement length on PUSCH data symbols. |
| GetPuschDataREPowerMean(string, out double) | Gets the mean value (over Meas Length) of power calculated on PUSCH data REs. |
| GetPuschDataRmsEvmMean(string, out double) | Gets the mean value of RMS EVMs calculated over measurement length on PUSCH data symbols. |
| GetPuschDataTransientRmsEvmMean(string, out double) | Gets the mean value of RMS EVMs calulated over measurement interval for the PUSCH symbols where the transient occurs. |
| GetPuschDmrsPeakEvmMaximum(string, out double) | Gets the maximum value of peak EVMs calculated over measurement length on PUSCH DMRS. |
| GetPuschDmrsREPowerMean(string, out double) | Gets the mean value (over Meas Length) of power calculated on PUSCH DMRS REs. |
| GetPuschDmrsRmsEvmMean(string, out double) | Gets the mean value of RMS EVMs calculated over measurement length on PUSCH DMRS. |
| GetPuschPeakPhaseOffsetMaximum(string, out double) | Gets the maximum value over Meas Length of peak phase offsets between the reference and measurement slots. |
| GetPuschPeakPhaseOffsetSlotIndex(string, out int) | Gets the slot index where ModAcc Results PUSCH Pk Phase Offset Max occurs. |
| GetPuschPtrsPeakEvmMaximum(string, out double) | Gets the maximum value of peak EVMs calculated over measurement length on PUSCH PTRS. |
| GetPuschPtrsREPowerMean(string, out double) | Gets the mean value (over Meas Length) of power calculated on PUSCH PTRS REs. |
| GetPuschPtrsRmsEvmMean(string, out double) | Gets the mean value of RMS EVMs calculated over measurement length on PUSCH PTRS. |
| GetSchDetectedModulationType(string, out RFmxNRMXSchDetectedModulationType) | Gets the modulation of the shared channel user data if you set the SetAutoResourceBlockDetectionEnabled(string, RFmxNRMXAutoResourceBlockDetectionEnabled) method to True; otherwise, returns the configured modulation of the shared user data. In case of downlink test model, the modulation type specified by the 3GPP standard is returned. |
| GetSchSymbolPowerMean(string, out double) | Gets the mean value (over SetMeasurementLength(string, double)) of power calculated on OFDM symbols allocated only with the shared channel. |
| GetSpectralFlatnessMarginSlotIndex(string, out int) | Gets the slot index with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2. |
| GetSpectralFlatnessRange1Maximum(string, out double) | Gets the maximum magnitude of the EVM equalizer coefficients within Range1 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. The value is expressed in dB. |
| GetSpectralFlatnessRange1MaximumSubcarrierIndex(string, out int) | Gets the maximum subcarrier index magnitude of EVM equalizer coefficients within Range1 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. |
| GetSpectralFlatnessRange1MaximumToRange1Minimum(string, out double) | Gets the peak-to-peak ripple of the magnitude of EVM equalizer coefficients within Range1 for the measurement unit, that has the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. This value is expressed in dB. |
| GetSpectralFlatnessRange1MaximumToRange2Minimum(string, out double) | Gets the peak-to-peak ripple of the EVM equalizer coefficients from maximum in Range1 to minimum in Range2 for the Measurement unit that has the worst ripple margin among all four ripple results defined in 3section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. This value is expressed in dB. |
| GetSpectralFlatnessRange1Minimum(string, out double) | Gets the minimum magnitude of EVM equalizer coefficients within Range1 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. The value is expressed in dB. |
| GetSpectralFlatnessRange1MinimumSubcarrierIndex(string, out int) | Gets the minimum subcarrier index magnitude of EVM equalizer coefficients within Range1 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. |
| GetSpectralFlatnessRange2Maximum(string, out double) | Gets the maximum magnitude of EVM equalizer coefficients within Range2 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. The value is expressed in dB. |
| GetSpectralFlatnessRange2MaximumSubcarrierIndex(string, out int) | Gets the maximum subcarrier index magnitude of EVM equalizer coefficients within Range2 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. |
| GetSpectralFlatnessRange2MaximumToRange1Minimum(string, out double) | Gets the peak-to-peak ripple of the EVM equalizer coefficients from maximum in Range2 to minimum in Range1 for the Measurement unit that has the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. This value is expressed in dB. |
| GetSpectralFlatnessRange2MaximumToRange2Minimum(string, out double) | Gets the peak-to-peak ripple of the magnitude of EVM equalizer coefficients within Range2 for the Measurement unit, that has the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. This value is expressed in dB. |
| GetSpectralFlatnessRange2Minimum(string, out double) | Gets the minimum magnitude of EVM equalizer coefficients within Range2 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. The value is expressed in dB. |
| GetSpectralFlatnessRange2MinimumSubcarrierIndex(string, out int) | Gets the minimum subcarrier index magnitude of EVM equalizer coefficients within Range2 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. |
| GetSssPeakEvmMaximum(string, out double) | Gets the maximum value of peak EVMs calculated over measurement length on SSS symbols. When you set the SetEvmUnit(string, RFmxNRMXModAccEvmUnit) method to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit method to dB, the measurement returns this result in dB. |
| GetSssRmsEvmMean(string, out double) | Gets the mean value of RMS EVMs computed over measurement length on SSS symbols. When you set the SetEvmUnit(string, RFmxNRMXModAccEvmUnit) method to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit method to dB, the measurement returns this result in dB. |
| GetSubblockInBandEmissionMargin(string, out double) | Gets In-Band Emission Margin of the subblock's aggregated bandwidth. This value is expressed in dB. |
| GetSubblockIQOriginOffsetMean(string, out double) | Gets the estimated IQ origin offset averaged over measurement length in the subblock. This value is expressed in dBc. This result is valid only when you set the SetTransmitterArchitecture(string, RFmxNRMXTransmitterArchitecture) method to LOPerSubblock. |
| GetSubblockLOComponentCarrierIndex(string, out int) | Gets the index of the component carrier that includes the LO of the transmitter according to the SetSubblockFrequency(string, double) and SetSubblockTransmitLOFrequency(string, double) properties. If the LO of the transmitter doesn't fall into any component carrier of the subblock, the method returns -1. This result is valid only when you set the SetTransmitterArchitecture(string, RFmxNRMXTransmitterArchitecture) method to LOPerSubblock. |
| GetSubblockLOSubcarrierIndex(string, out int) | Gets the subcarrier index within the respective component carrier where the transmitter LO is located. Due to its dependence on SetSubblockFrequency(string, double) and SetSubblockTransmitLOFrequency(string, double) properties, the value can be fractional, and the LO might reside in between subcarriers of a component carrier. This result is valid only when you set the SetTransmitterArchitecture(string, RFmxNRMXTransmitterArchitecture) method to LOPerSubblock. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccshortframeenabled.html language=enus -->
## TOPIC 00315: RFmxNRMXModAccShortFrameEnabled Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccshortframeenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccshortframeenabled.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the input signal has a periodicity shorter than the NR frame duration. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXModAccShortFrameEnabledMembersNameValueDescriptionFalse0When you set the method to False or the SetTriggerType(string, RFmxNRMXTriggerType) metho

### RFmxNRMXModAccShortFrameEnabled Enumeration

Specifies whether the input signal has a periodicity shorter than the NR frame duration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXModAccShortFrameEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | When you set the method to False or the SetTriggerType(string, RFmxNRMXTriggerType) method is set to a value other than None, a signal periodicity equal to the maximum of 1 frame duration and the configured SSB periodicity, if SSB is active, is assumed. |
| True | 1 | When you set the method to False or the Trigger Type method is set to None, the measurement uses SetShortFrameLength(string, double) as signal periodicity. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccshortframelengthunit.html language=enus -->
## TOPIC 00316: RFmxNRMXModAccShortFrameLengthUnit Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccshortframelengthunit.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccshortframelengthunit.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units in which Short Frame Length is specified. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXModAccShortFrameLengthUnitMembersNameValueDescriptionSlot1Short frame length is specified in units of slots. Subframe3Short frame length is specified in units of subframes.

### RFmxNRMXModAccShortFrameLengthUnit Enumeration

Specifies the units in which Short Frame Length is specified.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXModAccShortFrameLengthUnit

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Slot | 1 | Short frame length is specified in units of slots. |
| Subframe | 3 | Short frame length is specified in units of subframes. |
| Time | 6 | Short frame length is specified in units of time. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccsynchronizationmode.html language=enus -->
## TOPIC 00317: RFmxNRMXModAccSynchronizationMode Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccsynchronizationmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxmodaccsynchronizationmode.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed from slot or frame boundary. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXModAccSynchronizationModeMembersNameValueDescriptionSlot1The measurement is performed over the SetMeasurementLength(string, double) starting at the SetMeasure

### RFmxNRMXModAccSynchronizationMode Enumeration

Specifies whether the measurement is performed from slot or frame boundary.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXModAccSynchronizationMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Slot | 1 | The measurement is performed over the SetMeasurementLength(string, double) starting at the SetMeasurementOffset(string, double) from the slot boundary. If you set the SetTriggerType(string, RFmxNRMXTriggerType) method to DigitalEdge, the measurement expects the digital trigger at the slot boundary. |
| Frame | 5 | The measurement is performed over the SetMeasurementLength(string, double) starting at SetMeasurementOffset(string, double) from the frame boundary. If you set the SetTriggerType(string, RFmxNRMXTriggerType) to DigitalEdge, the measurement expects the digital trigger from the frame boundary. |
| SsbStartFrame | 7 | The measurement is performed over the SetMeasurementLength(string, double) starting at SetMeasurementOffset(string, double) from the frame boundary. If you set the SetTriggerType(string, RFmxNRMXTriggerType) to DigitalEdge, the measurement expects the digital trigger from the boundary of the frame having SSB. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxobw.html language=enus -->
## TOPIC 00318: RFmxNRMXObw Class

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxobw.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxobw.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the OBW measurement. Derives fromRFmxNRMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.NRMXpublic class RFmxNRMXObw : RFmxNRMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxNRMXObwConfiguration instance that provides methods to configure the OBW measurement. ResultsGets

### RFmxNRMXObw Class

Represents the OBW measurement.

#### Derives from

- RFmxNRMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public class RFmxNRMXObw : RFmxNRMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxNRMXObwConfiguration instance that provides methods to configure the OBW measurement. |
| Results | Gets the RFmxNRMXObwResults instance that provides methods to fetch and read the OBW measurement results. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxobwamplitudecorrectiontype.html language=enus -->
## TOPIC 00319: RFmxNRMXObwAmplitudeCorrectionType Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxobwamplitudecorrectiontype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxobwamplitudecorrectiontype.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the amplitude of frequency bins in the spectrum used by the measurement is corrected for external attenuation at RF center frequency or corrected for external attenuation at individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external

### RFmxNRMXObwAmplitudeCorrectionType Enumeration

Specifies whether the amplitude of frequency bins in the spectrum used by the measurement is corrected for external attenuation at RF center frequency or corrected for external attenuation at individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXObwAmplitudeCorrectionType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| RFCenterFrequency | 0 | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| SpectrumFrequencyBin | 1 | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration-configurerbwfilter__string-rfmxnrmxobwrbwautobandwidth-double-rfmxnrmxobwrbwfiltertype.html language=enus -->
## TOPIC 00320: ConfigureRbwFilter(string, RFmxNRMXObwRbwAutoBandwidth, double, RFmxNRMXObwRbwFilterType)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration-configurerbwfilter__string-rfmxnrmxobwrbwautobandwidth-double-rfmxnrmxobwrbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration-configurerbwfilter__string-rfmxnrmxobwrbwautobandwidth-double-rfmxnrmxobwrbwfiltertype.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the resolution bandwidth (RBW) filter.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int ConfigureRbwFilter(string selectorString, RFmxNRMXObwRbwAutoBandwidth rbwAuto, double rbw, RFmxNRMXObwRbwFilterType rbwFilterType)ParametersNameTypeDescriptionselectorStringstringPass an empty s

### ConfigureRbwFilter(string, RFmxNRMXObwRbwAutoBandwidth, double, RFmxNRMXObwRbwFilterType)

Configures the resolution bandwidth (RBW) filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int ConfigureRbwFilter(string selectorString, RFmxNRMXObwRbwAutoBandwidth rbwAuto, double rbw, RFmxNRMXObwRbwFilterType rbwFilterType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| rbwAuto | RFmxNRMXObwRbwAutoBandwidth | Specifies whether the measurement computes the RBW. |
| rbw | double | Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the rbwAuto parameter to False. This value is expressed in Hz. |
| rbwFilterType | RFmxNRMXObwRbwFilterType | Specifies the shape of the RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration-getrbwfiltertype__string-out.html language=enus -->
## TOPIC 00321: GetRbwFilterType(string, out RFmxNRMXObwRbwFilterType)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration-getrbwfiltertype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration-getrbwfiltertype__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the shape of the digital RBW filter. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetRbwFilterType(string selectorString, out RFmxNRMXObwRbwFilterType value)RemarksThis method gets the value of ObwRbwFilterType attribute.The default value is Gaussian.ParametersNameTypeDescriptionsel

### GetRbwFilterType(string, out RFmxNRMXObwRbwFilterType)

Gets the shape of the digital RBW filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetRbwFilterType(string selectorString, out RFmxNRMXObwRbwFilterType value)

#### Remarks

This method gets the value of [ObwRbwFilterType](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Gaussian](nationalinstruments-rfmx-nrmx-rfmxnrmxobwrbwfiltertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxNRMXObwRbwFilterType | Upon return, contains the shape of the digital RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration-setamplitudecorrectiontype__string-rfmxnrmxobwamplitudecorrectiontype.html language=enus -->
## TOPIC 00322: SetAmplitudeCorrectionType(string, RFmxNRMXObwAmplitudeCorrectionType)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration-setamplitudecorrectiontype__string-rfmxnrmxobwamplitudecorrectiontype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration-setamplitudecorrectiontype__string-rfmxnrmxobwamplitudecorrectiontype.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the amplitude of frequency bins in the spectrum used by the measurement is corrected for external attenuation at RF center frequency or corrected for external attenuation at individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external atten

### SetAmplitudeCorrectionType(string, RFmxNRMXObwAmplitudeCorrectionType)

Sets whether the amplitude of frequency bins in the spectrum used by the measurement is corrected for external attenuation at RF center frequency or corrected for external attenuation at individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetAmplitudeCorrectionType(string selectorString, RFmxNRMXObwAmplitudeCorrectionType value)

#### Remarks

This method sets the value of [ObwAmplitudeCorrectionType](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [RFCenterFrequency](nationalinstruments-rfmx-nrmx-rfmxnrmxobwamplitudecorrectiontype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXObwAmplitudeCorrectionType | Specifies whether the amplitude of frequency bins in the spectrum used by the measurement is corrected for external attenuation at RF center frequency or corrected for external attenuation at individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration-setaveragingcount__string-int.html language=enus -->
## TOPIC 00323: SetAveragingCount(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration-setaveragingcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration-setaveragingcount__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxNRMXObwAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetAveragingCount(string selectorString, int value)RemarksThis method sets the value of ObwAveragingCo

### SetAveragingCount(string, int)

Sets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxNRMXObwAveragingEnabled)](nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration-setaveragingenabled__string-rfmxnrmxobwaveragingenabled.html) method to [True](nationalinstruments-rfmx-nrmx-rfmxnrmxobwaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetAveragingCount(string selectorString, int value)

#### Remarks

This method sets the value of [ObwAveragingCount](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxNRMXObwAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration-setaveragingtype__string-rfmxnrmxobwaveragingtype.html language=enus -->
## TOPIC 00324: SetAveragingType(string, RFmxNRMXObwAveragingType)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration-setaveragingtype__string-rfmxnrmxobwaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration-setaveragingtype__string-rfmxnrmxobwaveragingtype.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetAveragingType(string selectorString, RFmxNRMXObwAveragingType value)RemarksThis method sets the value of ObwAveragi

### SetAveragingType(string, RFmxNRMXObwAveragingType)

Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetAveragingType(string selectorString, RFmxNRMXObwAveragingType value)

#### Remarks

This method sets the value of [ObwAveragingType](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Rms](nationalinstruments-rfmx-nrmx-rfmxnrmxobwaveragingtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXObwAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration-setfftwindow__string-rfmxnrmxobwfftwindow.html language=enus -->
## TOPIC 00325: SetFftWindow(string, RFmxNRMXObwFftWindow)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration-setfftwindow__string-rfmxnrmxobwfftwindow.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration-setfftwindow__string-rfmxnrmxobwfftwindow.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the FFT window type to be used to reduce spectral leakage. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetFftWindow(string selectorString, RFmxNRMXObwFftWindow value)RemarksThis method sets the value of ObwFftWindow attribute.The default value is FlatTop.ParametersNameTypeDescripti

### SetFftWindow(string, RFmxNRMXObwFftWindow)

Sets the FFT window type to be used to reduce spectral leakage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetFftWindow(string selectorString, RFmxNRMXObwFftWindow value)

#### Remarks

This method sets the value of [ObwFftWindow](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [FlatTop](nationalinstruments-rfmx-nrmx-rfmxnrmxobwfftwindow.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXObwFftWindow | Specifies the FFT window type to be used to reduce spectral leakage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration-setrbwfilterbandwidth__string-double.html language=enus -->
## TOPIC 00326: SetRbwFilterBandwidth(string, double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration-setrbwfilterbandwidth__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration-setrbwfilterbandwidth__string-double.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the bandwidth of the RBW filter used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(string, RFmxNRMXObwRbwAutoBandwidth) method to False. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetRbwFilterBandwidth(string selectorString

### SetRbwFilterBandwidth(string, double)

Sets the bandwidth of the RBW filter used to sweep the acquired signal, when you set the [SetRbwFilterAutoBandwidth(string, RFmxNRMXObwRbwAutoBandwidth)](nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration-setrbwfilterautobandwidth__string-rfmxnrmxobwrbwautobandwidth.html) method to [False](nationalinstruments-rfmx-nrmx-rfmxnrmxobwrbwautobandwidth.html). This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetRbwFilterBandwidth(string selectorString, double value)

#### Remarks

This method sets the value of [ObwRbwFilterBandwidth](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 10 kHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the bandwidth of the RBW filter used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(string, RFmxNRMXObwRbwAutoBandwidth) method to False. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration-setspan__string-double.html language=enus -->
## TOPIC 00327: SetSpan(string, double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration-setspan__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration-setspan__string-double.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the frequency range around the subblock center frequency, which is used to find the Subblock Occupied Bandwidth. When SetSpanAuto(string, RFmxNRMXObwSpanAuto) is set to False, the configured span value is used by the measurement. This value is expressed in Hz. SyntaxNamespace: NationalInstrumen

### SetSpan(string, double)

Sets the frequency range around the subblock center frequency, which is used to find the Subblock Occupied Bandwidth. When [SetSpanAuto(string, RFmxNRMXObwSpanAuto)](nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration-setspanauto__string-rfmxnrmxobwspanauto.html) is set to [False](nationalinstruments-rfmx-nrmx-rfmxnrmxobwspanauto.html), the configured span value is used by the measurement. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetSpan(string selectorString, double value)

#### Remarks

This method sets the value of [ObwSpan](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 20 MHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the subblock number. Example: "subblock0". You can use the BuildSubblockString(string, int) method to build the selector string. |
| value | double | Specifies the frequency range around the subblock center frequency, which is used to find the Subblock Occupied Bandwidth. When SetSpanAuto(string, RFmxNRMXObwSpanAuto) is set to False, the configured span value is used by the measurement. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXObwConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration.html language=enus -->
## TOPIC 00328: RFmxNRMXObwConfiguration Class

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxobwconfiguration.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the OBW measurement. Derives fromRFmxNRMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.NRMXpublic class RFmxNRMXObwConfiguration : RFmxNRMXSubObjectMethodsNameDescriptionConfigureAveraging(string, RFmxNRMXObwAveragingEnabled, int, RFmxNRMXObwAveragingType)Configure

### RFmxNRMXObwConfiguration Class

Provides methods to configure the OBW measurement.

#### Derives from

- RFmxNRMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public class RFmxNRMXObwConfiguration : RFmxNRMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| ConfigureAveraging(string, RFmxNRMXObwAveragingEnabled, int, RFmxNRMXObwAveragingType) | Configures averaging for the OBW measurement. |
| ConfigureRbwFilter(string, RFmxNRMXObwRbwAutoBandwidth, double, RFmxNRMXObwRbwFilterType) | Configures the resolution bandwidth (RBW) filter. |
| ConfigureSweepTime(string, RFmxNRMXObwSweepTimeAuto, double) | Configures the sweep time. |
| GetAllTracesEnabled(string, out bool) | Gets whether to enable the traces to be stored and retrieved after performing the OBW measurement. |
| GetAmplitudeCorrectionType(string, out RFmxNRMXObwAmplitudeCorrectionType) | Gets whether the amplitude of frequency bins in the spectrum used by the measurement is corrected for external attenuation at RF center frequency or corrected for external attenuation at individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |
| GetAveragingCount(string, out int) | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxNRMXObwAveragingEnabled) method to True. |
| GetAveragingEnabled(string, out RFmxNRMXObwAveragingEnabled) | Gets whether to enable averaging for the OBW measurement. |
| GetAveragingType(string, out RFmxNRMXObwAveragingType) | Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. |
| GetFftWindow(string, out RFmxNRMXObwFftWindow) | Gets the FFT window type to be used to reduce spectral leakage. |
| GetMeasurementEnabled(string, out bool) | Gets whether to enable the OBW measurement. |
| GetNumberOfAnalysisThreads(string, out int) | Gets the maximum number of threads used for parallelism for the OBW measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| GetPowerIntegrationMethod(string, out RFmxNRMXObwPowerIntegrationMethod) | Gets if the OBW measurement window is centered around the signal or the RF Center frequency. |
| GetRbwFilterAutoBandwidth(string, out RFmxNRMXObwRbwAutoBandwidth) | Gets whether the measurement computes the RBW. |
| GetRbwFilterBandwidth(string, out double) | Gets the bandwidth of the RBW filter used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(string, RFmxNRMXObwRbwAutoBandwidth) method to False. This value is expressed in Hz. |
| GetRbwFilterType(string, out RFmxNRMXObwRbwFilterType) | Gets the shape of the digital RBW filter. |
| GetSpan(string, out double) | Gets the frequency range around the subblock center frequency, which is used to find the Subblock Occupied Bandwidth. When SetSpanAuto(string, RFmxNRMXObwSpanAuto) is set to False, the configured span value is used by the measurement. This value is expressed in Hz. |
| GetSpanAuto(string, out RFmxNRMXObwSpanAuto) | Gets whether the frequency range of the spectrum used for the OBW measurement is auto computed or configured by the user. |
| GetSweepTimeAuto(string, out RFmxNRMXObwSweepTimeAuto) | Gets whether the measurement sets the sweep time. |
| GetSweepTimeInterval(string, out double) | Gets the sweep time when you set the SetSweepTimeAuto(string, RFmxNRMXObwSweepTimeAuto) method to False. This value is expressed in seconds. |
| SetAllTracesEnabled(string, bool) | Sets whether to enable the traces to be stored and retrieved after performing the OBW measurement. |
| SetAmplitudeCorrectionType(string, RFmxNRMXObwAmplitudeCorrectionType) | Sets whether the amplitude of frequency bins in the spectrum used by the measurement is corrected for external attenuation at RF center frequency or corrected for external attenuation at individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |
| SetAveragingCount(string, int) | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxNRMXObwAveragingEnabled) method to True. |
| SetAveragingEnabled(string, RFmxNRMXObwAveragingEnabled) | Sets whether to enable averaging for the OBW measurement. |
| SetAveragingType(string, RFmxNRMXObwAveragingType) | Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. |
| SetFftWindow(string, RFmxNRMXObwFftWindow) | Sets the FFT window type to be used to reduce spectral leakage. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable the OBW measurement. |
| SetNumberOfAnalysisThreads(string, int) | Sets the maximum number of threads used for parallelism for the OBW measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| SetPowerIntegrationMethod(string, RFmxNRMXObwPowerIntegrationMethod) | Sets if the OBW measurement window is centered around the signal or the RF Center frequency. |
| SetRbwFilterAutoBandwidth(string, RFmxNRMXObwRbwAutoBandwidth) | Sets whether the measurement computes the RBW. |
| SetRbwFilterBandwidth(string, double) | Sets the bandwidth of the RBW filter used to sweep the acquired signal, when you set the SetRbwFilterAutoBandwidth(string, RFmxNRMXObwRbwAutoBandwidth) method to False. This value is expressed in Hz. |
| SetRbwFilterType(string, RFmxNRMXObwRbwFilterType) | Sets the shape of the digital RBW filter. |
| SetSpan(string, double) | Sets the frequency range around the subblock center frequency, which is used to find the Subblock Occupied Bandwidth. When SetSpanAuto(string, RFmxNRMXObwSpanAuto) is set to False, the configured span value is used by the measurement. This value is expressed in Hz. |
| SetSpanAuto(string, RFmxNRMXObwSpanAuto) | Sets whether the frequency range of the spectrum used for the OBW measurement is auto computed or configured by the user. |
| SetSweepTimeAuto(string, RFmxNRMXObwSweepTimeAuto) | Sets whether the measurement sets the sweep time. |
| SetSweepTimeInterval(string, double) | Sets the sweep time when you set the SetSweepTimeAuto(string, RFmxNRMXObwSweepTimeAuto) method to False. This value is expressed in seconds. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxobwrbwautobandwidth.html language=enus -->
## TOPIC 00329: RFmxNRMXObwRbwAutoBandwidth Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxobwrbwautobandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxobwrbwautobandwidth.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the RBW. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXObwRbwAutoBandwidthMembersNameValueDescriptionFalse0The measurement uses the RBW that you specify in the SetRbwFilterBandwidth(string, double) method. True1The measurement computes t

### RFmxNRMXObwRbwAutoBandwidth Enumeration

Specifies whether the measurement computes the RBW.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXObwRbwAutoBandwidth

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement uses the RBW that you specify in the SetRbwFilterBandwidth(string, double) method. |
| True | 1 | The measurement computes the RBW. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxobwresults-getabsolutepower__string-out.html language=enus -->
## TOPIC 00330: GetAbsolutePower(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxobwresults-getabsolutepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxobwresults-getabsolutepower__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the total power measured in the spectrum acquired by the measurement. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetAbsolutePower(string selectorString, out double value)RemarksThis method gets the value of ObwResultsAbsolutePower attribute.Paramete

### GetAbsolutePower(string, out double)

Gets the total power measured in the spectrum acquired by the measurement. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetAbsolutePower(string selectorString, out double value)

#### Remarks

This method gets the value of [ObwResultsAbsolutePower](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Subblock number. Example: "Subblock0", "result::r1/Subblock0". You can use the BuildSubblockString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the total power measured in the spectrum acquired by the measurement. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXObwResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxpvtmeasurementmethod.html language=enus -->
## TOPIC 00331: RFmxNRMXPvtMeasurementMethod Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxpvtmeasurementmethod.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxpvtmeasurementmethod.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the PVT measurement method. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXPvtMeasurementMethodMembersNameValueDescriptionNormal0The measurement is performed using a single acquisition. Use this method when a high dynamic range is not required. DynamicRange1The measureme

### RFmxNRMXPvtMeasurementMethod Enumeration

Specifies the PVT measurement method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXPvtMeasurementMethod

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Normal | 0 | The measurement is performed using a single acquisition. Use this method when a high dynamic range is not required. |
| DynamicRange | 1 | The measurement is performed using two acquisitions. Use this method when a higher dynamic range is desirable over the measurement speed. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxpvtresults-fetchmeasurement__string-double-out-out-out-out-out.html language=enus -->
## TOPIC 00332: FetchMeasurement(string, double, out RFmxNRMXPvtMeasurementStatus, out double, out double, out double, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxpvtresults-fetchmeasurement__string-double-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxpvtresults-fetchmeasurement__string-double-out-out-out-out-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches PVT ON and OFF powers along with measurement status and burst width. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read from this method.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int FetchMeasurement(string selectorString, double timeout, out RFmxNRMXPvtMe

### FetchMeasurement(string, double, out RFmxNRMXPvtMeasurementStatus, out double, out double, out double, out double)

Fetches PVT ON and OFF powers along with measurement status and burst width. 
 Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int FetchMeasurement(string selectorString, double timeout, out RFmxNRMXPvtMeasurementStatus measurementStatus, out double absoluteOffPowerBefore, out double absoluteOffPowerAfter, out double absoluteONPower, out double burstWidth)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |
| measurementStatus | out RFmxNRMXPvtMeasurementStatus | Upon return, contains the measurement status indicating whether the off power before and after is within the standard defined limit. |
| absoluteOffPowerBefore | out double | Upon return, contains the OFF power in the segment before the captured burst. The segment is defined as one slot prior to a short transient segment and the burst. This value is expressed in dBm. |
| absoluteOffPowerAfter | out double | Upon return, contains the OFF power in the segment after the captured burst. The segment is defined as one slot after the burst and a short transient segment. This value is expressed in dBm. |
| absoluteONPower | out double | Upon return, contains the power of the subframes within the captured burst. This value is expressed in dBm. |
| burstWidth | out double | Upon return, contains the width of the captured burst. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXPvtResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxpvtresults-fetchsignalpowertrace__string-double-ref-ref.html language=enus -->
## TOPIC 00333: FetchSignalPowerTrace(string, double, ref AnalogWaveform< float >, ref AnalogWaveform< float >)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxpvtresults-fetchsignalpowertrace__string-double-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxpvtresults-fetchsignalpowertrace__string-double-ref-ref.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an instantanous signal power trace along with the absolute limit for each segment in the trace. For uplink, the power unit of the returned traces is dBm, while for downlink, the power unit of the returned traces is dBm/MHz. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string

### FetchSignalPowerTrace(string, double, ref AnalogWaveform< float >, ref AnalogWaveform< float >)

Fetches an instantanous signal power trace along with the absolute limit for each segment in the trace. For uplink, the power unit of the returned traces is dBm, while for downlink, the power unit of the returned traces is dBm/MHz. 
 Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int FetchSignalPowerTrace(string selectorString, double timeout, ref AnalogWaveform< float > signalPower, ref AnalogWaveform< float > absoluteLimit)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |
| signalPower | ref AnalogWaveform< float > | Upon return, contains an instantanous signal power trace along with the absolute limit for each segment in the trace. For uplink, the power unit of the returned traces is dBm, while for downlink, the power unit of the returned traces is dBm/MHz. |
| absoluteLimit | ref AnalogWaveform< float > | Upon return, contains absolute limit for each segment in the trace as specified in section 6.5.2.4.5 of the 3GPP 36.521 specification. This value is expressed in dBm or dBm/MHz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXPvtResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxpvtresults-fetchwindowedsignalpowertrace__string-double-ref.html language=enus -->
## TOPIC 00334: FetchWindowedSignalPowerTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxpvtresults-fetchwindowedsignalpowertrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxpvtresults-fetchwindowedsignalpowertrace__string-double-ref.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the 70/N us windowed power trace in dBm/MHz for Downlink, while an empty trace is returned for Uplink. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int FetchWindowedSignalPowerTrace(string selecto

### FetchWindowedSignalPowerTrace(string, double, ref AnalogWaveform< float >)

Fetches the 70/N us windowed power trace in dBm/MHz for Downlink, while an empty trace is returned for Uplink. 
 Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int FetchWindowedSignalPowerTrace(string selectorString, double timeout, ref AnalogWaveform< float > windowedSignalPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, and carrier number. If you do not specify the result name, the default result instance is used. Example:"subblock0/carrier0""result::r1/subblock0/carrier0" You can use the BuildCarrierString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |
| windowedSignalPower | ref AnalogWaveform< float > | Upon return, contains the 70/N us windowed power trace in dBm/MHz for Downlink, while an empty trace is returned for Uplink. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXPvtResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxpvtresults-getabsoluteoffpowerbefore__string-out.html language=enus -->
## TOPIC 00335: GetAbsoluteOffPowerBefore(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxpvtresults-getabsoluteoffpowerbefore__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxpvtresults-getabsoluteoffpowerbefore__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the OFF power in the segment before the captured burst for the uplink direction, while it returns NaN in the segment after the captured burst for the downlink direction. The segment is defined as one slot prior to a short transient segment and the burst. This value is expressed in dBm. SyntaxNa

### GetAbsoluteOffPowerBefore(string, out double)

Gets the OFF power in the segment before the captured burst for the uplink direction, while it returns NaN in the segment after the captured burst for the downlink direction. The segment is defined as one slot prior to a short transient segment and the burst. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetAbsoluteOffPowerBefore(string selectorString, out double value)

#### Remarks

This method gets the value of [PvtResultsAbsoluteOffPowerBefore](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the OFF power in the segment before the captured burst. The segment is defined as one slot prior to a short transient segment and the burst. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXPvtResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxpvtresults-getpeakwindowedoffpowermargin__string-out.html language=enus -->
## TOPIC 00336: GetPeakWindowedOffPowerMargin(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxpvtresults-getpeakwindowedoffpowermargin__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxpvtresults-getpeakwindowedoffpowermargin__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the NaN for the uplink direction, while it returns the GetPeakWindowedOffPower(string, out double) to the 3GPP limit. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPeakWindowedOffPowerMargin(string selectorString, out double value)RemarksThis method

### GetPeakWindowedOffPowerMargin(string, out double)

Gets the NaN for the uplink direction, while it returns the [GetPeakWindowedOffPower(string, out double)](nationalinstruments-rfmx-nrmx-rfmxnrmxpvtresults-getpeakwindowedoffpower__string-out.html) to the 3GPP limit. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPeakWindowedOffPowerMargin(string selectorString, out double value)

#### Remarks

This method gets the value of [PvtResultsPeakWindowedOffPowerMargin](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the NaN for the uplink direction, while it returns the GetPeakWindowedOffPower(string, out double) to the 3GPP limit. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXPvtResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsem-configuration.html language=enus -->
## TOPIC 00337: Configuration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsem-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsem-configuration.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxNRMXSemConfiguration instance that provides methods to configure the SEM measurement. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic RFmxNRMXSemConfiguration Configuration { get; }

### Configuration

Gets the [RFmxNRMXSemConfiguration](nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration.html) instance that provides methods to configure the SEM measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public [RFmxNRMXSemConfiguration](nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration.html) Configuration { get; }

Parent topic:

RFmxNRMXSem Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemcomponentcarrierconfiguration-getintegrationbandwidth__string-out.html language=enus -->
## TOPIC 00338: GetIntegrationBandwidth(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemcomponentcarrierconfiguration-getintegrationbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemcomponentcarrierconfiguration-getintegrationbandwidth__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the integration bandwidth of a component carrier. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetIntegrationBandwidth(string selectorString, out double value)RemarksThis method gets the value of SemComponentCarrierIntegrationBandwidth attribute.The de

### GetIntegrationBandwidth(string, out double)

Gets the integration bandwidth of a component carrier. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetIntegrationBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [SemComponentCarrierIntegrationBandwidth](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 9 MHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the carrier number and subblock number. Example: "subblock0" or "subblock0/carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the integration bandwidth of a component carrier. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXSemComponentCarrierConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemcomponentcarrierresults-getpeakfrequency__string-out.html language=enus -->
## TOPIC 00339: GetPeakFrequency(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemcomponentcarrierresults-getpeakfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemcomponentcarrierresults-getpeakfrequency__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency at which peak power occurs in the component carrier. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetPeakFrequency(string selectorString, out double value)RemarksThis method gets the value of SemResultsComponentCarrierPeakFrequency attrib

### GetPeakFrequency(string, out double)

Gets the frequency at which peak power occurs in the component carrier. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetPeakFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsComponentCarrierPeakFrequency](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Carrier number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Carrier0". You can use the BuildCarrierString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the frequency at which peak power occurs in the component carrier. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXSemComponentCarrierResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-configureoffsetbandwidthintegral__string-int.html language=enus -->
## TOPIC 00340: ConfigureOffsetBandwidthIntegral(string, int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-configureoffsetbandwidthintegral__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-configureoffsetbandwidthintegral__string-int.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the bandwidth integral of the offset segments. Use "offset(k)" or "subblock(n)" or "subblock(n)/offset(k)" as the selector string to configure or read this method.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int ConfigureOffsetBandwidthIntegral(string selectorString, int bandwidth

### ConfigureOffsetBandwidthIntegral(string, int)

Configures the bandwidth integral of the offset segments. 
 Use "offset(k)" or "subblock(n)" or "subblock(n)/offset(k)" as the selector string to configure or read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int ConfigureOffsetBandwidthIntegral(string selectorString, int bandwidthIntegral)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, carrier number, and offset number. If you do not specify the result name, the default result instance is used. Example:"subblock0/offset0""result::r1/subblock0/offset0" You can use the BuildOffsetString(string, int) method to build the selector string. |
| bandwidthIntegral | int | Specifies the resolution of a spectrum to compare with the spectral mask limits as an integer multiple of the RBW. When you set this parameter to a value greater than 1, the measurement acquires the spectrum with a narrow resolution and then processes it digitally to get a wider resolution that is equal to the product of a bandwidth integral and a RBW. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-configureoffsetbandwidthintegralarray__string-int_arr1.html language=enus -->
## TOPIC 00341: ConfigureOffsetBandwidthIntegralArray(string, int[])

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-configureoffsetbandwidthintegralarray__string-int_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-configureoffsetbandwidthintegralarray__string-int_arr1.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an array of the bandwidth integral of the offset segments. Use "subblock(n)" as the selector string to configure or read this method.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int ConfigureOffsetBandwidthIntegralArray(string selectorString, int[] bandwidthIntegral)ParametersName

### ConfigureOffsetBandwidthIntegralArray(string, int[])

Configures an array of the bandwidth integral of the offset segments. 
 Use "subblock(n)" as the selector string to configure or read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int ConfigureOffsetBandwidthIntegralArray(string selectorString, int[] bandwidthIntegral)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the subblock number. Example:"subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| bandwidthIntegral | int[] | Specifies an array of the resolution of a spectrum to compare with the spectral mask limits as an integer multiple of the RBW. When you set this parameter to a value greater than 1, the measurement acquires the spectrum with a narrow resolution and then processes it digitally to get a wider resolution that is equal to the product of a bandwidth integral and a RBW. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-configureoffsetfrequency__string-double-double-rfmxnrmxsemoffsetsideband.html language=enus -->
## TOPIC 00342: ConfigureOffsetFrequency(string, double, double, RFmxNRMXSemOffsetSideband)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-configureoffsetfrequency__string-double-double-rfmxnrmxsemoffsetsideband.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-configureoffsetfrequency__string-double-double-rfmxnrmxsemoffsetsideband.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the start and stop frequencies and the sideband of an offset segment. Use "offset(k)" or "subblock(n)" or "subblock(n)/offset(k)" as the selector string to configure or read this method. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int ConfigureOffsetFrequency(string selectorStrin

### ConfigureOffsetFrequency(string, double, double, RFmxNRMXSemOffsetSideband)

Configures the start and stop frequencies and the sideband of an offset segment. 
 Use "offset(k)" or "subblock(n)" or "subblock(n)/offset(k)" as the selector string to configure or read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int ConfigureOffsetFrequency(string selectorString, double offsetStartFrequency, double offsetStopFrequency, RFmxNRMXSemOffsetSideband offsetSideband)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the signal name, subblock number, and offset number. Example:"subblock0/offset0" You can use the BuildOffsetString(string, int) method to build the selector string. |
| offsetStartFrequency | double | Specifies the start frequency of an offset segment relative to the component carrier bandwidth edge (single carrier) or subblock aggregated channel bandwidth edge (multi-carrier). This value is expressed in Hz. |
| offsetStopFrequency | double | Specifies the stop frequency of an offset segment relative to the component carrier bandwidth edge (single carrier) or subblock aggregated channel bandwidth edge (multi-carrier). This value is expressed in Hz. |
| offsetSideband | RFmxNRMXSemOffsetSideband | Specifies whether the offset segment is present either on one side or on both sides of a carrier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-configureoffsetfrequencyarray__string-double_arr1-double_arr1-rfmxnrmxsemoffsetsideband_arr1.html language=enus -->
## TOPIC 00343: ConfigureOffsetFrequencyArray(string, double[], double[], RFmxNRMXSemOffsetSideband[])

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-configureoffsetfrequencyarray__string-double_arr1-double_arr1-rfmxnrmxsemoffsetsideband_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-configureoffsetfrequencyarray__string-double_arr1-double_arr1-rfmxnrmxsemoffsetsideband_arr1.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an array of the start and stop frequencies and the sideband of an offset segment. Use "subblock(n)" as the selector string to configure or read this method. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int ConfigureOffsetFrequencyArray(string selectorString, double[] offsetStartFr

### ConfigureOffsetFrequencyArray(string, double[], double[], RFmxNRMXSemOffsetSideband[])

Configures an array of the start and stop frequencies and the sideband of an offset segment. 
 Use "subblock(n)" as the selector string to configure or read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int ConfigureOffsetFrequencyArray(string selectorString, double[] offsetStartFrequency, double[] offsetStopFrequency, RFmxNRMXSemOffsetSideband[] offsetSideband)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the subblock number. Example:"subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| offsetStartFrequency | double[] | Specifies an array of the start frequencies of an offset segment relative to the component carrier bandwidth edge (single carrier) or subblock aggregated channel bandwidth edge (multi-carrier). This value is expressed in Hz. |
| offsetStopFrequency | double[] | Specifies an array of the stop frequencies of an offset segment relative to the component carrier bandwidth edge (single carrier) or subblock aggregated channel bandwidth edge (multi-carrier). This value is expressed in Hz. |
| offsetSideband | RFmxNRMXSemOffsetSideband[] | Specifies an array of whether the offset segment is present either on one side or on both sides of a carrier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-configureoffsetlimitfailmask__string-rfmxnrmxsemoffsetlimitfailmask.html language=enus -->
## TOPIC 00344: ConfigureOffsetLimitFailMask(string, RFmxNRMXSemOffsetLimitFailMask)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-configureoffsetlimitfailmask__string-rfmxnrmxsemoffsetlimitfailmask.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-configureoffsetlimitfailmask__string-rfmxnrmxsemoffsetlimitfailmask.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the limit fail mask of the offset segments that specify the criteria to determine the measurement fail status. Use "offset(n)" or "subblock(n)/"offset(n)" as the selector string to configure or read this method.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int ConfigureOffsetLimitF

### ConfigureOffsetLimitFailMask(string, RFmxNRMXSemOffsetLimitFailMask)

Configures the limit fail mask of the offset segments that specify the criteria to determine the measurement fail status. 
 Use "offset(n)" or "subblock(n)/"offset(n)" as the selector string to configure or read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int ConfigureOffsetLimitFailMask(string selectorString, RFmxNRMXSemOffsetLimitFailMask limitFailMask)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the signal name, subblock number, and offset number. Example:"subblock0/offset0" You can use the BuildOffsetString(string, int) method to build the selector string. |
| limitFailMask | RFmxNRMXSemOffsetLimitFailMask | Specifies the criteria to determine the measurement fail status. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-configureoffsetrbwfilterarray__string-double_arr1-rfmxnrmxsemoffsetrbwfiltertype_arr1.html language=enus -->
## TOPIC 00345: ConfigureOffsetRbwFilterArray(string, double[], RFmxNRMXSemOffsetRbwFilterType[])

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-configureoffsetrbwfilterarray__string-double_arr1-rfmxnrmxsemoffsetrbwfiltertype_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-configureoffsetrbwfilterarray__string-double_arr1-rfmxnrmxsemoffsetrbwfiltertype_arr1.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the offset RBW and the offset RBW filter type array. Use "subblock(n)" as the selector string to configure this method. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int ConfigureOffsetRbwFilterArray(string selectorString, double[] offsetRbw, RFmxNRMXSemOffsetRbwFilterType[] offset

### ConfigureOffsetRbwFilterArray(string, double[], RFmxNRMXSemOffsetRbwFilterType[])

Configures the offset RBW and the offset RBW filter type array. 
 Use "subblock(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int ConfigureOffsetRbwFilterArray(string selectorString, double[] offsetRbw, RFmxNRMXSemOffsetRbwFilterType[] offsetRbwFilterType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the subblock number. Example:"subblock0" You can use the BuildSubblockString(string, int) method to build the selector string. |
| offsetRbw | double[] | Specifies an array of the bandwidth of an RBW filter used to sweep an acquired offset segment. This value is expressed in Hz. |
| offsetRbwFilterType | RFmxNRMXSemOffsetRbwFilterType[] | Specifies an array of the shape of the digital RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-setoffsetrbwfiltertype__string-rfmxnrmxsemoffsetrbwfiltertype.html language=enus -->
## TOPIC 00346: SetOffsetRbwFilterType(string, RFmxNRMXSemOffsetRbwFilterType)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-setoffsetrbwfiltertype__string-rfmxnrmxsemoffsetrbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-setoffsetrbwfiltertype__string-rfmxnrmxsemoffsetrbwfiltertype.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the shape of a digital RBW filter. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetOffsetRbwFilterType(string selectorString, RFmxNRMXSemOffsetRbwFilterType value)RemarksThis method sets the value of SemOffsetRbwFilterType attribute.The default value is Gaussian.ParametersNameTypeDe

### SetOffsetRbwFilterType(string, RFmxNRMXSemOffsetRbwFilterType)

Sets the shape of a digital RBW filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetOffsetRbwFilterType(string selectorString, RFmxNRMXSemOffsetRbwFilterType value)

#### Remarks

This method sets the value of [SemOffsetRbwFilterType](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [Gaussian](nationalinstruments-rfmx-nrmx-rfmxnrmxsemoffsetrbwfiltertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number and subblock number. Example: "subblock0" or "subblock0/offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | RFmxNRMXSemOffsetRbwFilterType | Specifies the shape of a digital RBW filter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-setsweeptimeinterval__string-double.html language=enus -->
## TOPIC 00347: SetSweepTimeInterval(string, double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-setsweeptimeinterval__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-setsweeptimeinterval__string-double.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the sweep time when you set the SetSweepTimeAuto(string, RFmxNRMXSemSweepTimeAuto) method to False. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetSweepTimeInterval(string selectorString, double value)RemarksThis method sets the value of SemSweep

### SetSweepTimeInterval(string, double)

Sets the sweep time when you set the [SetSweepTimeAuto(string, RFmxNRMXSemSweepTimeAuto)](nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-setsweeptimeauto__string-rfmxnrmxsemsweeptimeauto.html) method to [False](nationalinstruments-rfmx-nrmx-rfmxnrmxsemsweeptimeauto.html). This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetSweepTimeInterval(string selectorString, double value)

#### Remarks

This method sets the value of [SemSweepTimeInterval](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 1 ms.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the sweep time when you set the SetSweepTimeAuto(string, RFmxNRMXSemSweepTimeAuto) method to False. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-setuplinkmasktype__string-rfmxnrmxsemuplinkmasktype.html language=enus -->
## TOPIC 00348: SetUplinkMaskType(string, RFmxNRMXSemUplinkMaskType)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-setuplinkmasktype__string-rfmxnrmxsemuplinkmasktype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-setuplinkmasktype__string-rfmxnrmxsemuplinkmasktype.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the spectrum emission mask used in the measurement for uplink. You must set the mask type to Custom to configure the custom offset masks. Refer to section 6.5.2 of the 3GPP 38.101 specification for more information about standard-defined mask types. SyntaxNamespace: NationalInstruments.RFmx.NRM

### SetUplinkMaskType(string, RFmxNRMXSemUplinkMaskType)

Sets the spectrum emission mask used in the measurement for uplink. You must set the mask type to [Custom](nationalinstruments-rfmx-nrmx-rfmxnrmxsemuplinkmasktype.html) to configure the custom offset masks. Refer to section 6.5.2 of the *3GPP 38.101* specification for more information about standard-defined mask types.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetUplinkMaskType(string selectorString, RFmxNRMXSemUplinkMaskType value)

#### Remarks

This method sets the value of [SemUplinkMaskType](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is [General](nationalinstruments-rfmx-nrmx-rfmxnrmxsemuplinkmasktype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxNRMXSemUplinkMaskType | Specifies the spectrum emission mask used in the measurement for uplink. You must set the mask type to Custom to configure the custom offset masks. Refer to section 6.5.2 of the 3GPP 38.101 specification for more information about standard-defined mask types. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXSemConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration.html language=enus -->
## TOPIC 00349: RFmxNRMXSemConfiguration Class

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the SEM measurement. Derives fromRFmxNRMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.NRMXpublic class RFmxNRMXSemConfiguration : RFmxNRMXSubObjectPropertiesNameDescriptionComponentCarrierGets the RFmxNRMXSemComponentCarrierConfiguration instance. MethodsNameDescr

### RFmxNRMXSemConfiguration Class

Provides methods to configure the SEM measurement.

#### Derives from

- RFmxNRMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public class RFmxNRMXSemConfiguration : RFmxNRMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| ComponentCarrier | Gets the RFmxNRMXSemComponentCarrierConfiguration instance. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureAveraging(string, RFmxNRMXSemAveragingEnabled, int, RFmxNRMXSemAveragingType) | Configures averaging for the SEM measurement. |
| ConfigureNumberOfOffsets(string, int) | Configures the number of offset segments for the SEM measurement. Use "subblock(n)" as the selector string to read results from this method. |
| ConfigureOffsetAbsoluteLimit(string, double, double) | Configures the start and the stop limit of an offset segment. Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to configure this method. |
| ConfigureOffsetAbsoluteLimitArray(string, double[], double[]) | Configures an array of the start limit and the stop limit of the offset segments. Use "subblock(n)" as the selector string to configure this method. |
| ConfigureOffsetBandwidthIntegral(string, int) | Configures the bandwidth integral of the offset segments. Use "offset(k)" or "subblock(n)" or "subblock(n)/offset(k)" as the selector string to configure or read this method. |
| ConfigureOffsetBandwidthIntegralArray(string, int[]) | Configures an array of the bandwidth integral of the offset segments. Use "subblock(n)" as the selector string to configure or read this method. |
| ConfigureOffsetFrequency(string, double, double, RFmxNRMXSemOffsetSideband) | Configures the start and stop frequencies and the sideband of an offset segment. Use "offset(k)" or "subblock(n)" or "subblock(n)/offset(k)" as the selector string to configure or read this method. |
| ConfigureOffsetFrequencyArray(string, double[], double[], RFmxNRMXSemOffsetSideband[]) | Configures an array of the start and stop frequencies and the sideband of an offset segment. Use "subblock(n)" as the selector string to configure or read this method. |
| ConfigureOffsetLimitFailMask(string, RFmxNRMXSemOffsetLimitFailMask) | Configures the limit fail mask of the offset segments that specify the criteria to determine the measurement fail status. Use "offset(n)" or "subblock(n)/"offset(n)" as the selector string to configure or read this method. |
| ConfigureOffsetLimitFailMaskArray(string, RFmxNRMXSemOffsetLimitFailMask[]) | Configures an array of the limit fail mask of the offset segments that specifies the criteria to determine the measurement fail status. Use "subblock(n)" as the selector string to configure or read this method. |
| ConfigureOffsetRbwFilter(string, double, RFmxNRMXSemOffsetRbwFilterType) | Configures the offset RBW and the offset RBW filter type. Use "offset(n)" or "subblock(n)" or "subblock(n)/offset(n)" as the selector string to configure this method. |
| ConfigureOffsetRbwFilterArray(string, double[], RFmxNRMXSemOffsetRbwFilterType[]) | Configures the offset RBW and the offset RBW filter type array. Use "subblock(n)" as the selector string to configure this method. |
| ConfigureOffsetRelativeLimit(string, double, double) | Configures the start and stop relative limit of the offset segment. Use "offset(n)" or "subblock(n)" or "subblock(n)/offset(n)" as the selector string to configure this method. |
| ConfigureOffsetRelativeLimitArray(string, double[], double[]) | Configures an array of the start and stop relative limit of the offset segment. Use "subblock(n)" as the selector string to configure this method. |
| ConfigureSweepTime(string, RFmxNRMXSemSweepTimeAuto, double) | Configures the sweep time. |
| ConfigureUplinkMaskType(string, RFmxNRMXSemUplinkMaskType) | Configures the standard defined mask type that has to be used in the measurement for uplink. |
| GetAllTracesEnabled(string, out bool) | Gets whether to enable the traces to be stored and retrieved after performing the SEM measurement. |
| GetAmplitudeCorrectionType(string, out RFmxNRMXSemAmplitudeCorrectionType) | Gets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |
| GetAveragingCount(string, out int) | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxNRMXSemAveragingEnabled) method to True. |
| GetAveragingEnabled(string, out RFmxNRMXSemAveragingEnabled) | Gets whether to enable averaging for the SEM measurement. |
| GetAveragingType(string, out RFmxNRMXSemAveragingType) | Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement. |
| GetDeltaFMaximum(string, out double) | Gets the stop frequency for 3rd offset segment to be used in the measurement. This method is valid only for downlink and when you set the SetDownlinkMaskType(string, RFmxNRMXSemDownlinkMaskType) method to Standard. |
| GetDownlinkMaskType(string, out RFmxNRMXSemDownlinkMaskType) | Gets the limits to be used in the measurement for Downlink. |
| GetFftWindow(string, out RFmxNRMXSemFftWindow) | Gets the FFT window type to be used to reduce spectral leakage. |
| GetMeasurementEnabled(string, out bool) | Gets whether to enable the SEM measurement. |
| GetNumberOfAnalysisThreads(string, out int) | Gets the maximum number of threads used for parallelism for the SEM measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| GetNumberOfOffsets(string, out int) | Gets the number of SEM offset segments. |
| GetOffsetAbsoluteLimitStart(string, out double) | Gets the absolute power limit corresponding to the beginning of an offset segment. This value is expressed in dBm. |
| GetOffsetAbsoluteLimitStop(string, out double) | Gets the absolute power limit corresponding to the end of an offset segment. This value is expressed in dBm. |
| GetOffsetBandwidthIntegral(string, out int) | Gets the resolution of a spectrum to compare with the spectral mask limits as an integer multiple of the RBW. |
| GetOffsetFrequencyDefinition(string, out RFmxNRMXSemOffsetFrequencyDefinition) | Gets the definition of the the start frequency and stop frequency of the offset segments. |
| GetOffsetLimitFailMask(string, out RFmxNRMXSemOffsetLimitFailMask) | Gets the criteria to determine the measurement fail status. |
| GetOffsetRbwFilterBandwidth(string, out double) | Gets the bandwidth of the resolution bandwidth (RBW) filter used to sweep the acquired offset segment, when you set the SEM Offset RBW Auto method to False. This value is expressed in Hz. |
| GetOffsetRbwFilterType(string, out RFmxNRMXSemOffsetRbwFilterType) | Gets the shape of a digital RBW filter. |
| GetOffsetRelativeLimitStart(string, out double) | Gets the relative power limit corresponding to the beginning of the offset segment. This value is expressed in dB. |
| GetOffsetRelativeLimitStop(string, out double) | Gets the relative power limit corresponding to the end of the offset segment. This value is expressed in dB. |
| GetOffsetSideband(string, out RFmxNRMXSemOffsetSideband) | Gets whether the offset segment is present either on one side or on both sides of a carrier. |
| GetOffsetStartFrequency(string, out double) | Gets the start frequency of an offset segment relative to the ComponentCarrierBandwidth edge (single carrier) or GetSubblockAggregatedChannelBandwidth(string, out double) edge (multi-carrier). This value is expressed in Hz. |
| GetOffsetStopFrequency(string, out double) | Gets the stop frequency of an offset segment relative to the ComponentCarrierBandwidth edge (single carrier) or GetSubblockAggregatedChannelBandwidth(string, out double) edge (multi-carrier). This value is expressed in Hz. |
| GetSubblockAggregatedChannelBandwidth(string, out double) | Gets the aggregated channel bandwidth of a configured subblock. This value is expressed in Hz. The aggregated channel bandwidth is the sum of the subblock integration bandwidth and the guard bands on either side of the subblock integration bandwidth. |
| GetSubblockIntegrationBandwidth(string, out double) | Gets the integration bandwidth of a subblock. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. |
| GetSweepTimeAuto(string, out RFmxNRMXSemSweepTimeAuto) | Gets whether the measurement sets the sweep time. |
| GetSweepTimeInterval(string, out double) | Gets the sweep time when you set the SetSweepTimeAuto(string, RFmxNRMXSemSweepTimeAuto) method to False. This value is expressed in seconds. |
| GetUplinkMaskType(string, out RFmxNRMXSemUplinkMaskType) | Gets the spectrum emission mask used in the measurement for uplink. You must set the mask type to Custom to configure the custom offset masks. Refer to section 6.5.2 of the 3GPP 38.101 specification for more information about standard-defined mask types. |
| SetAllTracesEnabled(string, bool) | Sets whether to enable the traces to be stored and retrieved after performing the SEM measurement. |
| SetAmplitudeCorrectionType(string, RFmxNRMXSemAmplitudeCorrectionType) | Sets whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |
| SetAveragingCount(string, int) | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxNRMXSemAveragingEnabled) method to True. |
| SetAveragingEnabled(string, RFmxNRMXSemAveragingEnabled) | Sets whether to enable averaging for the SEM measurement. |
| SetAveragingType(string, RFmxNRMXSemAveragingType) | Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement. |
| SetDeltaFMaximum(string, double) | Sets the stop frequency for 3rd offset segment to be used in the measurement. This method is valid only for downlink and when you set the SetDownlinkMaskType(string, RFmxNRMXSemDownlinkMaskType) method to Standard. |
| SetDownlinkMaskType(string, RFmxNRMXSemDownlinkMaskType) | Sets the limits to be used in the measurement for Downlink. |
| SetFftWindow(string, RFmxNRMXSemFftWindow) | Sets the FFT window type to be used to reduce spectral leakage. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable the SEM measurement. |
| SetNumberOfAnalysisThreads(string, int) | Sets the maximum number of threads used for parallelism for the SEM measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| SetNumberOfOffsets(string, int) | Sets the number of SEM offset segments. |
| SetOffsetAbsoluteLimitStart(string, double) | Sets the absolute power limit corresponding to the beginning of an offset segment. This value is expressed in dBm. |
| SetOffsetAbsoluteLimitStop(string, double) | Sets the absolute power limit corresponding to the end of an offset segment. This value is expressed in dBm. |
| SetOffsetBandwidthIntegral(string, int) | Sets the resolution of a spectrum to compare with the spectral mask limits as an integer multiple of the RBW. |
| SetOffsetFrequencyDefinition(string, RFmxNRMXSemOffsetFrequencyDefinition) | Sets the definition of the the start frequency and stop frequency of the offset segments. |
| SetOffsetLimitFailMask(string, RFmxNRMXSemOffsetLimitFailMask) | Sets the criteria to determine the measurement fail status. |
| SetOffsetRbwFilterBandwidth(string, double) | Sets the bandwidth of the resolution bandwidth (RBW) filter used to sweep the acquired offset segment, when you set the SEM Offset RBW Auto method to False. This value is expressed in Hz. |
| SetOffsetRbwFilterType(string, RFmxNRMXSemOffsetRbwFilterType) | Sets the shape of a digital RBW filter. |
| SetOffsetRelativeLimitStart(string, double) | Sets the relative power limit corresponding to the beginning of the offset segment. This value is expressed in dB. |
| SetOffsetRelativeLimitStop(string, double) | Sets the relative power limit corresponding to the end of the offset segment. This value is expressed in dB. |
| SetOffsetSideband(string, RFmxNRMXSemOffsetSideband) | Sets whether the offset segment is present either on one side or on both sides of a carrier. |
| SetOffsetStartFrequency(string, double) | Sets the start frequency of an offset segment relative to the ComponentCarrierBandwidth edge (single carrier) or GetSubblockAggregatedChannelBandwidth(string, out double) edge (multi-carrier). This value is expressed in Hz. |
| SetOffsetStopFrequency(string, double) | Sets the stop frequency of an offset segment relative to the ComponentCarrierBandwidth edge (single carrier) or GetSubblockAggregatedChannelBandwidth(string, out double) edge (multi-carrier). This value is expressed in Hz. |
| SetSweepTimeAuto(string, RFmxNRMXSemSweepTimeAuto) | Sets whether the measurement sets the sweep time. |
| SetSweepTimeInterval(string, double) | Sets the sweep time when you set the SetSweepTimeAuto(string, RFmxNRMXSemSweepTimeAuto) method to False. This value is expressed in seconds. |
| SetUplinkMaskType(string, RFmxNRMXSemUplinkMaskType) | Sets the spectrum emission mask used in the measurement for uplink. You must set the mask type to Custom to configure the custom offset masks. Refer to section 6.5.2 of the 3GPP 38.101 specification for more information about standard-defined mask types. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemfftwindow.html language=enus -->
## TOPIC 00350: RFmxNRMXSemFftWindow Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemfftwindow.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemfftwindow.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the FFT window type to be used to reduce spectral leakage. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXSemFftWindowMembersNameValueDescriptionNone0No spectral leakage. FlatTop1Spectral leakage is reduced using flat top window type. Hanning2Spectral leakage is reduced

### RFmxNRMXSemFftWindow Enumeration

Specifies the FFT window type to be used to reduce spectral leakage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXSemFftWindow

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0 | No spectral leakage. |
| FlatTop | 1 | Spectral leakage is reduced using flat top window type. |
| Hanning | 2 | Spectral leakage is reduced using Hanning window type. |
| Hamming | 3 | Spectral leakage is reduced using Hamming window type. |
| Gaussian | 4 | Spectral leakage is reduced using Gaussian window type. |
| Blackman | 5 | Spectral leakage is reduced using Blackman window type. |
| BlackmanHarris | 6 | Spectral leakage is reduced using Blackman-Harris window type. |
| KaiserBessel | 7 | Spectral leakage is reduced using Kaiser-Bessel window type. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemloweroffsetmeasurementstatus.html language=enus -->
## TOPIC 00351: RFmxNRMXSemLowerOffsetMeasurementStatus Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemloweroffsetmeasurementstatus.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemloweroffsetmeasurementstatus.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status based on the spectrum emission limits defined by the standard mask type that you configure in the SetUplinkMaskType(string, RFmxNRMXSemUplinkMaskType) method. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXSemLowerOffsetMeasurementStatusMembersNameVa

### RFmxNRMXSemLowerOffsetMeasurementStatus Enumeration

Returns the measurement status based on the spectrum emission limits defined by the standard mask type that you configure in the [SetUplinkMaskType(string, RFmxNRMXSemUplinkMaskType)](nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-setuplinkmasktype__string-rfmxnrmxsemuplinkmasktype.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXSemLowerOffsetMeasurementStatus

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Fail | 0 | Indicates that the measurement has failed. |
| Pass | 1 | Indicates that the measurement has passed. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemoffsetrbwfiltertype.html language=enus -->
## TOPIC 00352: RFmxNRMXSemOffsetRbwFilterType Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemoffsetrbwfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemoffsetrbwfiltertype.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of a digital RBW filter. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXSemOffsetRbwFilterTypeMembersNameValueDescriptionFftBased0No RBW filtering is performed. Gaussian1The RBW filter has a Gaussian response. Flat2The RBW filter has a flat response.

### RFmxNRMXSemOffsetRbwFilterType Enumeration

Specifies the shape of a digital RBW filter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXSemOffsetRbwFilterType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| FftBased | 0 | No RBW filtering is performed. |
| Gaussian | 1 | The RBW filter has a Gaussian response. |
| Flat | 2 | The RBW filter has a flat response. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-componentcarrier.html language=enus -->
## TOPIC 00353: ComponentCarrier

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-componentcarrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-componentcarrier.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxNRMXSemComponentCarrierResults instance that provides methods to fetch and read the SEM Component Carrier results. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic RFmxNRMXSemComponentCarrierResults ComponentCarrier { get; }

### ComponentCarrier

Gets the [RFmxNRMXSemComponentCarrierResults](nationalinstruments-rfmx-nrmx-rfmxnrmxsemcomponentcarrierresults.html) instance that provides methods to fetch and read the SEM Component Carrier results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public [RFmxNRMXSemComponentCarrierResults](nationalinstruments-rfmx-nrmx-rfmxnrmxsemcomponentcarrierresults.html) ComponentCarrier { get; }

Parent topic:

RFmxNRMXSemResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-fetchtotalaggregatedpower__string-double-out.html language=enus -->
## TOPIC 00354: FetchTotalAggregatedPower(string, double, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-fetchtotalaggregatedpower__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-fetchtotalaggregatedpower__string-double-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the sum of powers in all the subblocks.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int FetchTotalAggregatedPower(string selectorString, double timeout, out double totalAggregatedPower)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the resu

### FetchTotalAggregatedPower(string, double, out double)

Returns the sum of powers in all the subblocks.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int FetchTotalAggregatedPower(string selectorString, double timeout, out double totalAggregatedPower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| totalAggregatedPower | out double | Upon return, contains the total power of all the subblocks. The power in each subblock is the sum of powers of all the frequency bins over the integration bandwidth of the subblocks. This value includes the power in the inter-carrier gaps within a subblock, but it does not include the power within the subblock gaps. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXSemResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-fetchupperoffsetmargin__string-double-out-out-out-out-out.html language=enus -->
## TOPIC 00355: FetchUpperOffsetMargin(string, double, out RFmxNRMXSemUpperOffsetMeasurementStatus, out double, out double, out double, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-fetchupperoffsetmargin__string-double-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-fetchupperoffsetmargin__string-double-out-out-out-out-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status, margin, frequency at margin, absolute, and relative powers at the margin for upper offset segments. The relative power is relative to the total aggregated power. Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to read results from this method. Syntax

### FetchUpperOffsetMargin(string, double, out RFmxNRMXSemUpperOffsetMeasurementStatus, out double, out double, out double, out double)

Returns the measurement status, margin, frequency at margin, absolute, and relative powers at the margin for upper offset segments. The relative power is relative to the total aggregated power. 
 Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int FetchUpperOffsetMargin(string selectorString, double timeout, out RFmxNRMXSemUpperOffsetMeasurementStatus measurementStatus, out double margin, out double marginFrequency, out double marginAbsolutePower, out double marginRelativePower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, subblock number, carrier number, and offset number. If you do not specify the result name, the default result instance is used. Example:"subblock0/offset0""result::r1/subblock0/offset0" You can use the BuildOffsetString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| measurementStatus | out RFmxNRMXSemUpperOffsetMeasurementStatus | Upon return, contains the measurement status indicating whether the power before and after the burst is within the standard defined limit. |
| margin | out double | Upon return, contains the margin from the absolute limit mask for upper (positive) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. This value is expressed in dB. |
| marginFrequency | out double | Upon return, contains the frequency at which the margin occurs in the upper offset. This value is expressed in Hz. |
| marginAbsolutePower | out double | Upon return, contains the power at which the margin occurs in the upper offset segment. This value is expressed in dBm. |
| marginRelativePower | out double | Upon return, contains the power at which the margin occurs in the upper offset segment. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXSemResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-getloweroffsetrelativeintegratedpower__string-out.html language=enus -->
## TOPIC 00356: GetLowerOffsetRelativeIntegratedPower(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-getloweroffsetrelativeintegratedpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-getloweroffsetrelativeintegratedpower__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power in the lower (negative) offset segment relative to GetTotalAggregatedPower(string, out double) method. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetLowerOffsetRelativeIntegratedPower(string selectorString, out double value)RemarksThis meth

### GetLowerOffsetRelativeIntegratedPower(string, out double)

Gets the power in the lower (negative) offset segment relative to [GetTotalAggregatedPower(string, out double)](nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-gettotalaggregatedpower__string-out.html) method. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetLowerOffsetRelativeIntegratedPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetRelativeIntegratedPower](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power in the lower (negative) offset segment relative to GetTotalAggregatedPower(string, out double) method. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXSemResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-getloweroffsetrelativepeakpower__string-out.html language=enus -->
## TOPIC 00357: GetLowerOffsetRelativePeakPower(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-getloweroffsetrelativepeakpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-getloweroffsetrelativepeakpower__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power in the lower (negative) offset segment relative to GetTotalAggregatedPower(string, out double) method. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetLowerOffsetRelativePeakPower(string selectorString, out double value)RemarksThis metho

### GetLowerOffsetRelativePeakPower(string, out double)

Gets the peak power in the lower (negative) offset segment relative to [GetTotalAggregatedPower(string, out double)](nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-gettotalaggregatedpower__string-out.html) method. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetLowerOffsetRelativePeakPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsLowerOffsetRelativePeakPower](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak power in the lower (negative) offset segment relative to GetTotalAggregatedPower(string, out double) method. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXSemResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-getsubblockpower__string-out.html language=enus -->
## TOPIC 00358: GetSubblockPower(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-getsubblockpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-getsubblockpower__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power measured over the SemComponentCarrierIntegrationBandwidth method. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetSubblockPower(string selectorString, out double value)RemarksThis method gets the value of SemResultsSubblockPower attribute.Pa

### GetSubblockPower(string, out double)

Gets the power measured over the [SemComponentCarrierIntegrationBandwidth](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) method. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetSubblockPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsSubblockPower](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Subblock number. Example: "Subblock0", "result::r1/Subblock0". You can use the BuildSubblockString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power measured over the SemComponentCarrierIntegrationBandwidth method. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXSemResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-getupperoffsetpeakfrequency__string-out.html language=enus -->
## TOPIC 00359: GetUpperOffsetPeakFrequency(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-getupperoffsetpeakfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-getupperoffsetpeakfrequency__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency at which the peak power occurs in the upper (positive)offset segment. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetUpperOffsetPeakFrequency(string selectorString, out double value)RemarksThis method gets the value of SemResultsUpperOff

### GetUpperOffsetPeakFrequency(string, out double)

Gets the frequency at which the peak power occurs in the upper (positive)offset segment. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetUpperOffsetPeakFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetPeakFrequency](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the frequency at which the peak power occurs in the upper (positive)offset segment. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXSemResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-getupperoffsetrelativeintegratedpower__string-out.html language=enus -->
## TOPIC 00360: GetUpperOffsetRelativeIntegratedPower(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-getupperoffsetrelativeintegratedpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-getupperoffsetrelativeintegratedpower__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the power in the upper (positive) offset segment relative to GetTotalAggregatedPower(string, out double) method. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetUpperOffsetRelativeIntegratedPower(string selectorString, out double value)RemarksThis meth

### GetUpperOffsetRelativeIntegratedPower(string, out double)

Gets the power in the upper (positive) offset segment relative to [GetTotalAggregatedPower(string, out double)](nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-gettotalaggregatedpower__string-out.html) method. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetUpperOffsetRelativeIntegratedPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetRelativeIntegratedPower](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the power in the upper (positive) offset segment relative to GetTotalAggregatedPower(string, out double) method. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXSemResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-getupperoffsetrelativepeakpower__string-out.html language=enus -->
## TOPIC 00361: GetUpperOffsetRelativePeakPower(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-getupperoffsetrelativepeakpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-getupperoffsetrelativepeakpower__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the peak power in the upper (positive) offset segment relative to GetTotalAggregatedPower(string, out double) method. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetUpperOffsetRelativePeakPower(string selectorString, out double value)RemarksThis metho

### GetUpperOffsetRelativePeakPower(string, out double)

Gets the peak power in the upper (positive) offset segment relative to [GetTotalAggregatedPower(string, out double)](nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults-gettotalaggregatedpower__string-out.html) method. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetUpperOffsetRelativePeakPower(string selectorString, out double value)

#### Remarks

This method gets the value of [SemResultsUpperOffsetRelativePeakPower](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name, Offset number and Subblock number. Example: "Subblock0", "result::r1/Subblock0" or "result::r1/Subblock0/Offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the peak power in the upper (positive) offset segment relative to GetTotalAggregatedPower(string, out double) method. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXSemResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults.html language=enus -->
## TOPIC 00362: RFmxNRMXSemResults Class

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemresults.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the SEM measurement results. Derives fromRFmxNRMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.NRMXpublic class RFmxNRMXSemResults : RFmxNRMXSubObjectPropertiesNameDescriptionComponentCarrierGets the RFmxNRMXSemComponentCarrierResults instance that provides me

### RFmxNRMXSemResults Class

Provides methods to fetch and read the SEM measurement results.

#### Derives from

- RFmxNRMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public class RFmxNRMXSemResults : RFmxNRMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| ComponentCarrier | Gets the RFmxNRMXSemComponentCarrierResults instance that provides methods to fetch and read the SEM Component Carrier results. |

#### Methods

| Name | Description |
| --- | --- |
| FetchLowerOffsetMargin(string, double, out RFmxNRMXSemLowerOffsetMeasurementStatus, out double, out double, out double, out double) | Returns the measurement status, margin, frequency at margin, absolute, and relative powers at the margin for lower offset segments. The relative power is relative to the total aggregated power. Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to read results from this method. |
| FetchLowerOffsetMarginArray(string, double, ref RFmxNRMXSemLowerOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[]) | Returns an array of measurement status, margin, frequency at margin, absolute, and relative power at margin for lower offset segments. The relative power is relative to the total aggregated power. Use "subblock(n)" as the selector string to read results from this method. |
| FetchLowerOffsetPower(string, double, out double, out double, out double, out double, out double) | Returns the total absolute and relative powers, peak, absolute, and relative powers, and the frequency at the peak absolute power of the lower offset segment. The relative power is relative to the total aggregated power. Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to read results from this method. |
| FetchLowerOffsetPowerArray(string, double, ref double[], ref double[], ref double[], ref double[], ref double[]) | Returns an array of total absolute and relative powers, peak, absolute, and relative powers, and frequencies at peak absolute powers of lower offset segments. The relative power is relative to total aggregated power. Use "subblock(n)" as the selector string to read results from this method. |
| FetchMeasurementStatus(string, double, out RFmxNRMXSemMeasurementStatus) | Returns the overall measurement status based on the standard mask type that you configure. |
| FetchSpectrum(string, double, ref Spectrum< float >, ref Spectrum< float >) | Fetches the spectrum used for SEM measurements. |
| FetchSubblockMeasurement(string, double, out double, out double, out double) | Fetches the power, integration bandwidth, and center frequency of the subblock. |
| FetchTotalAggregatedPower(string, double, out double) | Returns the sum of powers in all the subblocks. |
| FetchUpperOffsetMargin(string, double, out RFmxNRMXSemUpperOffsetMeasurementStatus, out double, out double, out double, out double) | Returns the measurement status, margin, frequency at margin, absolute, and relative powers at the margin for upper offset segments. The relative power is relative to the total aggregated power. Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to read results from this method. |
| FetchUpperOffsetMarginArray(string, double, ref RFmxNRMXSemUpperOffsetMeasurementStatus[], ref double[], ref double[], ref double[], ref double[]) | Returns an array of measurement status, margin, frequency at margin, absolute, and relative power at margin for upper offset segments. The relative power is relative to the total aggregated power. Use "subblock(n)" as the selector string to read results from this method. |
| FetchUpperOffsetPower(string, double, out double, out double, out double, out double, out double) | Returns the total absolute and relative powers, peak, absolute, and relative powers, and the frequency at the peak absolute power of the upper offset segment. The relative power is relative to the total aggregated power. Use "offset(n)" or "subblock(n)/offset(n)" as the selector string to read results from this method. |
| FetchUpperOffsetPowerArray(string, double, ref double[], ref double[], ref double[], ref double[], ref double[]) | Returns an array of total absolute and relative powers, peak, absolute, and relative powers, and frequencies at peak absolute powers of upper offset segments. The relative power is relative to total aggregated power. Use "subblock(n)" as the selector string to read results from this method. |
| GetLowerOffsetAbsoluteIntegratedPower(string, out double) | Gets the lower (negative) offset segment power. This value is expressed in dBm. |
| GetLowerOffsetAbsolutePeakPower(string, out double) | Gets the peak power in the lower (negative) offset segment. This value is expressed in dBm. |
| GetLowerOffsetMargin(string, out double) | Gets the margin from the absolute limit mask for lower (negative) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. This value is expressed in dB. |
| GetLowerOffsetMarginAbsolutePower(string, out double) | Gets the power at which the Margin occurs in the lower (negative) offset segment. This value is expressed in dBm. |
| GetLowerOffsetMarginFrequency(string, out double) | Gets the frequency at which the Margin occurs in the lower (negative) offset. This value is expressed in Hz. |
| GetLowerOffsetMarginRelativePower(string, out double) | Gets the power at which the Margin occurs in the lower (negative) offset segment relative to GetTotalAggregatedPower(string, out double) method. This value is expressed in dB. |
| GetLowerOffsetMeasurementStatus(string, out RFmxNRMXSemLowerOffsetMeasurementStatus) | Gets the measurement status based on the spectrum emission limits defined by the standard mask type that you configure in the SetUplinkMaskType(string, RFmxNRMXSemUplinkMaskType) method. |
| GetLowerOffsetPeakFrequency(string, out double) | Gets the frequency at which the peak power occurs in the lower (negative) offset segment. This value is expressed in Hz. |
| GetLowerOffsetRelativeIntegratedPower(string, out double) | Gets the power in the lower (negative) offset segment relative to GetTotalAggregatedPower(string, out double) method. This value is expressed in dB. |
| GetLowerOffsetRelativePeakPower(string, out double) | Gets the peak power in the lower (negative) offset segment relative to GetTotalAggregatedPower(string, out double) method. This value is expressed in dB. |
| GetMeasurementStatus(string, out RFmxNRMXSemMeasurementStatus) | Gets the overall measurement status based on the standard mask type that you configure in the SetUplinkMaskType(string, RFmxNRMXSemUplinkMaskType) method. |
| GetSubblockPower(string, out double) | Gets the power measured over the SemComponentCarrierIntegrationBandwidth method. This value is expressed in dBm. |
| GetTotalAggregatedPower(string, out double) | Gets the sum of powers of all the subblocks. This value includes the power in the inter-carrier gap within a subblock, but it excludes power in the inter-subblock gaps. This value is expressed in dBm. |
| GetUpperOffsetAbsoluteIntegratedPower(string, out double) | Gets the upper (positive) offset segment power. This value is expressed in dBm. |
| GetUpperOffsetAbsolutePeakPower(string, out double) | Gets the peak power in the upper (positive) offset segment. This value is expressed in dBm. |
| GetUpperOffsetMargin(string, out double) | Gets the margin from the absolute limit mask for upper (positive) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. This value is expressed in dB. |
| GetUpperOffsetMarginAbsolutePower(string, out double) | Gets the power at which the Margin occurs in the upper (positive) offset segment. This value is expressed in dBm. |
| GetUpperOffsetMarginFrequency(string, out double) | Gets the frequency at which the Margin occurs in the upper (positive) offset. This value is expressed in Hz. |
| GetUpperOffsetMarginRelativePower(string, out double) | Gets the power at which the Margin occurs in the upper (positive) offset segment relative to GetTotalAggregatedPower(string, out double) method. This value is expressed in dB. |
| GetUpperOffsetMeasurementStatus(string, out RFmxNRMXSemUpperOffsetMeasurementStatus) | Gets the measurement status based on the user-configured standard measurement limits. Spectrum emission limits can be defined by setting SetUplinkMaskType(string, RFmxNRMXSemUplinkMaskType) method. |
| GetUpperOffsetPeakFrequency(string, out double) | Gets the frequency at which the peak power occurs in the upper (positive)offset segment. This value is expressed in Hz. |
| GetUpperOffsetRelativeIntegratedPower(string, out double) | Gets the power in the upper (positive) offset segment relative to GetTotalAggregatedPower(string, out double) method. This value is expressed in dB. |
| GetUpperOffsetRelativePeakPower(string, out double) | Gets the peak power in the upper (positive) offset segment relative to GetTotalAggregatedPower(string, out double) method. This value is expressed in dB. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemsweeptimeauto.html language=enus -->
## TOPIC 00363: RFmxNRMXSemSweepTimeAuto Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemsweeptimeauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemsweeptimeauto.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement sets the sweep time. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXSemSweepTimeAutoMembersNameValueDescriptionFalse0The measurement uses the sweep time that you specify in the SetSweepTimeInterval(string, double) method. True1The measurement uses

### RFmxNRMXSemSweepTimeAuto Enumeration

Specifies whether the measurement sets the sweep time.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXSemSweepTimeAuto

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement uses the sweep time that you specify in the SetSweepTimeInterval(string, double) method. |
| True | 1 | The measurement uses a sweep time of 1 ms. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemuplinkmasktype.html language=enus -->
## TOPIC 00364: RFmxNRMXSemUplinkMaskType Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemuplinkmasktype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemuplinkmasktype.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the spectrum emission mask used in the measurement for uplink. You must set the mask type to Custom to configure the custom offset masks. Refer to section 6.5.2 of the 3GPP 38.101 specification for more information about standard-defined mask types. SyntaxNamespace: NationalInstruments.RFm

### RFmxNRMXSemUplinkMaskType Enumeration

Specifies the spectrum emission mask used in the measurement for uplink. You must set the mask type to Custom to configure the custom offset masks. Refer to section 6.5.2 of the *3GPP 38.101* specification for more information about standard-defined mask types.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXSemUplinkMaskType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| General | 0 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.2-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification, Table 6.5.2.1-1 and 6.5A.2.1-1 in section 6.5.2 of the 3GPP TS 38.101-2 specification and Table 6.5B.2.1.1-1 in section 6.5B of the 3GPP TS 38.101-3 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.1.5-1, 6.6.2.1.5-2, 6.6.2.1A.1.5-1, and 6.6.2.1A.1.5-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification.If the band value is set to 46 or 96 or 102, the measurement selects the offset frequencies and limits for SEM as defined in Table 6.5F.2.2-1 in section 6.5F.2 of the 3GPP TS 38.101-1 Specification.If the band value is set to NTN bands 252, 254, 255 or 256, the measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.2.1 in section 6.5.2 of the 3GPP 38.101-5 specification. |
| NS35 | 1 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.1-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification and Table 6.5B.2.1.2.1-1 in section 6.5B of the 3GPP TS 38.101-3 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.5-1 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| Custom | 2 | You need to configure the SetNumberOfOffsets(string, int), SetOffsetStartFrequency(string, double), SetOffsetStopFrequency(string, double), SetOffsetAbsoluteLimitStart(string, double), SetOffsetAbsoluteLimitStop(string, double), SetOffsetSideband(string, RFmxNRMXSemOffsetSideband), SetOffsetRbwFilterBandwidth(string, double), SetOffsetRbwFilterType(string, RFmxNRMXSemOffsetRbwFilterType), and SetOffsetBandwidthIntegral(string, int) properties for each offset. |
| NS03 | 3 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.3-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.1-1 and 6.6.2.2.5.1-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| NS04 | 4 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.2-3 in section 6.5.2 of the 3GPP TS 38.101-1 specification. Subcarrier spacing can be configured through SetBandwidthPartSubcarrierSpacing(string, double) method. Subcarrier spacing corresponding to first bandwidth part is used for computing mask. Transform precoding can be configured through SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method. Transform precoding corresponding to first bandwidth part is used for computing mask. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.3.2-3 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| NS06 | 5 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.4-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.3-1 and 6.6.2.2.5.3-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| NS21 | 6 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.3-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.1-1 and 6.6.2.2.5.1-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| NS27 | 7 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.8-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of intra-band contiguous CA consisting of at least one subblock with all NR carriers, for the NR subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.2A.2.3.2.1-1 in section 6.5A.2.3 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.3.4-1 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| NS07 | 8 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.4-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.3-1 and Table 6.6.2.2.5.3-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| NS03U | 9 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.3-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. |
| NS21Rel17Onwards | 10 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.9-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. |
| NS04N | 11 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.1-1 in section 6.5.2.3 of the 3GPP TS 38.101-5 specification. |
| NS05N | 12 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.2-1 in section 6.5.2.3 of the 3GPP TS 38.101-5 specification. |
| NS09N | 13 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.3-1 in section 6.5.2.3 of the 3GPP TS 38.101-5 specification. |
| NS10N | 14 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.3-1 in section 6.5.2.3 of the 3GPP TS 38.101-5 specification. |
| NS11N | 0xF | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.1-1 in section 6.5.2.3 of the 3GPP TS 38.101-5 specification. |
| NS12N | 0x10 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.2-1 in section 6.5.2.3 of the 3GPP TS 38.101-5 specification. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxsemupperoffsetmeasurementstatus.html language=enus -->
## TOPIC 00365: RFmxNRMXSemUpperOffsetMeasurementStatus Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxsemupperoffsetmeasurementstatus.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxsemupperoffsetmeasurementstatus.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status based on the user-configured standard measurement limits. Spectrum emission limits can be defined by setting SetUplinkMaskType(string, RFmxNRMXSemUplinkMaskType) method. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXSemUpperOffsetMeasurementStatusMe

### RFmxNRMXSemUpperOffsetMeasurementStatus Enumeration

Returns the measurement status based on the user-configured standard measurement limits. Spectrum emission limits can be defined by setting [SetUplinkMaskType(string, RFmxNRMXSemUplinkMaskType)](nationalinstruments-rfmx-nrmx-rfmxnrmxsemconfiguration-setuplinkmasktype__string-rfmxnrmxsemuplinkmasktype.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXSemUpperOffsetMeasurementStatus

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Fail | 0 | Indicates that the measurement has failed. |
| Pass | 1 | Indicates that the measurement has passed. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxssbenabled.html language=enus -->
## TOPIC 00366: RFmxNRMXSsbEnabled Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxssbenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxssbenabled.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether synchronization signal block (SSB) is present in the transmitted signal. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXSsbEnabledMembersNameValueDescriptionFalse0Detection of SSB in the transmitted signal is disabled. True1Detection of SSB in the transmitted sig

### RFmxNRMXSsbEnabled Enumeration

Specifies whether synchronization signal block (SSB) is present in the transmitted signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXSsbEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Detection of SSB in the transmitted signal is disabled. |
| True | 1 | Detection of SSB in the transmitted signal is enabled. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxssbpattern.html language=enus -->
## TOPIC 00367: RFmxNRMXSsbPattern Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxssbpattern.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxssbpattern.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the candidate SS/PBCH blocks with different subcarrier spacing configurations as defined in the section 4.1 of 3GPP TS 38.213 specification. In order to configure Case C up to 1.88GHz unpaired spectrum, configure this method to CaseCUpTo3GHz. Similarly, to configure Case C 1.88GHz to 6GHz

### RFmxNRMXSsbPattern Enumeration

Specifies the candidate SS/PBCH blocks with different subcarrier spacing configurations as defined in the section 4.1 of *3GPP TS 38.213* specification. In order to configure Case C up to 1.88GHz unpaired spectrum, configure this method to CaseCUpTo3GHz. Similarly, to configure Case C 1.88GHz to 6GHz unpaired spectrum, configure this method to CaseC3GHzTo6GHz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXSsbPattern

#### Members

| Name | Value | Description |
| --- | --- | --- |
| CaseAUpTo3GHz | 0 | Use with 15 kHz subcarrier spacing. The first symbols of the candidate SS/PBCH blocks have indexes of {2, 8} + 14 * n, where n is 0 or 1. |
| CaseA3GHzTo6GHz | 1 | Use with 15 kHz subcarrier spacing. The first symbols of the candidate SS/PBCH blocks have indexes of {2, 8} + 14 * n, where n is 0, 1, 2, or 3. |
| CaseBUpTo3GHz | 2 | Use with 30 kHz subcarrier spacing. The first symbols of the candidate SS/PBCH blocks have indexes of {4, 8, 16, 20} + 28 * n, where n is 0. |
| CaseB3GHzTo6GHz | 3 | Use with 30 kHz subcarrier spacing. The first symbols of the candidate SS/PBCH blocks have indexes of {4, 8, 16, 20} + 28 * n, where n is 0, 1, 2, or 3. |
| CaseCUpTo3GHz | 4 | Use with 30 kHz subcarrier spacing. The first symbols of the candidate SS/PBCH blocks have indexes of {2, 8} + 14 * n, where n is 0 or 1. |
| CaseC3GHzTo6GHz | 5 | Use with 30 kHz subcarrier spacing. The first symbols of the candidate SS/PBCH blocks have indexes of {2, 8} + 14 * n, where n is 0, 1, 2, or 3. |
| CaseD | 6 | Use with 120 kHz subcarrier spacing. The first symbols of the candidate SS/PBCH blocks have indexes {4, 8, 16, 20} + 28 * n. For carrier frequencies higher than 6 GHz, n is 0, 1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, or 18. |
| CaseE | 7 | Use with 240 kHz subcarrier spacing. The first symbols of the candidate SS/PBCH blocks have indexes {8, 12, 16, 20, 32, 36, 40, 44} + 56 * n. For carrier frequencies higher than 6 GHz, n is 0, 1, 2, 3, 5, 6, 7, or 8. |
| CaseF | 8 |  |
| CaseG | 9 |  |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxtriggerminimumquiettimemode.html language=enus -->
## TOPIC 00368: RFmxNRMXTriggerMinimumQuietTimeMode Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxtriggerminimumquiettimemode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxtriggerminimumquiettimemode.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the minimum quiet time used for triggering. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXTriggerMinimumQuietTimeModeMembersNameValueDescriptionManual0The minimum quiet time for triggering is the value of the SetTriggerMinimumQuietTimeDu

### RFmxNRMXTriggerMinimumQuietTimeMode Enumeration

Specifies whether the measurement computes the minimum quiet time used for triggering.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXTriggerMinimumQuietTimeMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Manual | 0 | The minimum quiet time for triggering is the value of the SetTriggerMinimumQuietTimeDuration(string, double) method. |
| Auto | 1 | The measurement computes the minimum quiet time used for triggering. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxtriggertype.html language=enus -->
## TOPIC 00369: RFmxNRMXTriggerType Enumeration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxtriggertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxtriggertype.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of trigger to be used for signal acquisition. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic enum RFmxNRMXTriggerTypeMembersNameValueDescriptionNone0No Reference Trigger is configured. DigitalEdge1The Reference Trigger is not asserted until a digital edge is detected. The so

### RFmxNRMXTriggerType Enumeration

Specifies the type of trigger to be used for signal acquisition.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public enum RFmxNRMXTriggerType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0 | No Reference Trigger is configured. |
| DigitalEdge | 1 | The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the SetDigitalEdgeTriggerSource(string, string) method. |
| IQPowerEdge | 2 | The Reference Trigger is asserted when the signal changes past the level specified by the slope (rising or falling), which is configured using the SetIQPowerEdgeTriggerSlope(string, RFmxNRMXIQPowerEdgeTriggerSlope) method. |
| Software | 3 | The Reference Trigger is not asserted until a software trigger occurs. |

Parent topic:

NationalInstruments.RFmx.NRMX

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxtxp-configuration.html language=enus -->
## TOPIC 00370: Configuration

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxtxp-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxtxp-configuration.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxNRMXTxpConfiguration instance that provides methods to configure the TXP measurement. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic RFmxNRMXTxpConfiguration Configuration { get; }

### Configuration

Gets the [RFmxNRMXTxpConfiguration](nationalinstruments-rfmx-nrmx-rfmxnrmxtxpconfiguration.html) instance that provides methods to configure the TXP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public [RFmxNRMXTxpConfiguration](nationalinstruments-rfmx-nrmx-rfmxnrmxtxpconfiguration.html) Configuration { get; }

Parent topic:

RFmxNRMXTxp Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxtxp-results.html language=enus -->
## TOPIC 00371: Results

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxtxp-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxtxp-results.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxNRMXTxpResults instance that provides methods to fetch and read the TXP measurement results. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic RFmxNRMXTxpResults Results { get; }

### Results

Gets the [RFmxNRMXTxpResults](nationalinstruments-rfmx-nrmx-rfmxnrmxtxpresults.html) instance that provides methods to fetch and read the TXP measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public [RFmxNRMXTxpResults](nationalinstruments-rfmx-nrmx-rfmxnrmxtxpresults.html) Results { get; }

Parent topic:

RFmxNRMXTxp Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxtxpconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00372: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxtxpconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxtxpconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the traces to be stored and retrieved after the TXP measurement is performed. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method gets the value of TxpAllTracesEnabled attribute.The default value is False.Param

### GetAllTracesEnabled(string, out bool)

Enables the traces to be stored and retrieved after the TXP measurement is performed.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [TxpAllTracesEnabled](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is False.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Enables the traces to be stored and retrieved after the TXP measurement is performed. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXTxpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxtxpconfiguration-getaveragingcount__string-out.html language=enus -->
## TOPIC 00373: GetAveragingCount(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxtxpconfiguration-getaveragingcount__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxtxpconfiguration-getaveragingcount__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of acquisitions used for averaging when Averaging Enabled is True. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetAveragingCount(string selectorString, out int value)RemarksThis method gets the value of TxpAveragingCount attribute.The default value is 10.ParametersNameTy

### GetAveragingCount(string, out int)

Gets the number of acquisitions used for averaging when Averaging Enabled is True.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetAveragingCount(string selectorString, out int value)

#### Remarks

This method gets the value of [TxpAveragingCount](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of acquisitions used for averaging when Averaging Enabled is True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXTxpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxtxpconfiguration-getnumberofanalysisthreads__string-out.html language=enus -->
## TOPIC 00374: GetNumberOfAnalysisThreads(string, out int)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxtxpconfiguration-getnumberofanalysisthreads__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxtxpconfiguration-getnumberofanalysisthreads__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum number of threads used for parallelism inside TXP measurement. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetNumberOfAnalysisThreads(string selectorString, out int value)RemarksThis method gets the value of TxpNumberOfAnalysisThreads attribute.The number of threads mus

### GetNumberOfAnalysisThreads(string, out int)

Gets the maximum number of threads used for parallelism inside TXP measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetNumberOfAnalysisThreads(string selectorString, out int value)

#### Remarks

This method gets the value of [TxpNumberOfAnalysisThreads](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The number of threads must range from 1 to the number of physical cores. The default value is 1. The number of threads set used in calculations is not guaranteed. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the maximum number of threads used for parallelism inside TXP measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXTxpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxtxpconfiguration-setalltracesenabled__string-bool.html language=enus -->
## TOPIC 00375: SetAllTracesEnabled(string, bool)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxtxpconfiguration-setalltracesenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxtxpconfiguration-setalltracesenabled__string-bool.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the traces to be stored and retrieved after the TXP measurement is performed. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int SetAllTracesEnabled(string selectorString, bool value)RemarksThis method sets the value of TxpAllTracesEnabled attribute.The default value is False.Parameter

### SetAllTracesEnabled(string, bool)

Enables the traces to be stored and retrieved after the TXP measurement is performed.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int SetAllTracesEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [TxpAllTracesEnabled](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is False.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Enables the traces to be stored and retrieved after the TXP measurement is performed. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXTxpConfiguration Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxtxpresults-fetchmeasurement__string-double-out-out.html language=enus -->
## TOPIC 00376: FetchMeasurement(string, double, out double, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxtxpresults-fetchmeasurement__string-double-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxtxpresults-fetchmeasurement__string-double-out-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the average power and peak power of the the signal over which power measurments are performed. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int FetchMeasurement(string selectorString, double timeo

### FetchMeasurement(string, double, out double, out double)

Fetches the average power and peak power of the the signal over which power measurments are performed. 
 Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int FetchMeasurement(string selectorString, double timeout, out double averagePowerMean, out double peakPowerMaximum)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |
| averagePowerMean | out double | Returns the average power of the the signal over which power measurments are performed. This value is expressed in dBm. |
| peakPowerMaximum | out double | Returns the peak power of the the signal over which power measurments are performed This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXTxpResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxtxpresults-fetchpowertrace__string-double-ref.html language=enus -->
## TOPIC 00377: FetchPowerTrace(string, double, ref AnalogWaveform< float >)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxtxpresults-fetchpowertrace__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxtxpresults-fetchpowertrace__string-double-ref.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches power versus time trace. Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int FetchPowerTrace(string selectorString, double timeout, ref AnalogWaveform< float > power)ParametersNameTypeDescriptionsele

### FetchPowerTrace(string, double, ref AnalogWaveform< float >)

Fetches power versus time trace. 
 Use "carrier(k)" or "subblock(n)/carrier(k)" as the selector string to read this result.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int FetchPowerTrace(string selectorString, double timeout, ref AnalogWaveform< float > power)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example:"""result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for which the method waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the method waits until the measurement is complete. |
| power | ref AnalogWaveform< float > | Returns power versus time trace. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXTxpResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx-rfmxnrmxtxpresults-getaveragepowermean__string-out.html language=enus -->
## TOPIC 00378: GetAveragePowerMean(string, out double)

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx-rfmxnrmxtxpresults-getaveragepowermean__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx-rfmxnrmxtxpresults-getaveragepowermean__string-out.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the average power of the acquired signal. SyntaxNamespace: NationalInstruments.RFmx.NRMXpublic int GetAveragePowerMean(string selectorString, out double value)RemarksThis method gets the value of TxpResultsAveragePowerMean attribute.The default value is dBm.ParametersNameTypeDescriptionselector

### GetAveragePowerMean(string, out double)

Gets the average power of the acquired signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.NRMX](nationalinstruments-rfmx-nrmx.html)

public int GetAveragePowerMean(string selectorString, out double value)

#### Remarks

This method gets the value of [TxpResultsAveragePowerMean](nationalinstruments-rfmx-nrmx-rfmxnrmxpropertyid.html) attribute.The default value is dBm.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: """result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out double | Upon return, contains the average power of the acquired signal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxNRMXTxpResults Class

<!--NI_TOPIC bundle=rfmxnr-dotnet-api-ref path=nationalinstruments-rfmx-nrmx.html language=enus -->
## TOPIC 00379: NationalInstruments.RFmx.NRMX

- bundle_id: `rfmxnr-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-nrmx.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-nrmx.html
- document_id: `rfmxnr-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionRFmxNRMXDefines a root class which is used to identify and control NR signal configuration. RFmxNRMXAcpRepresents the ACP measurement. RFmxNRMXAcpComponentCarrierConfigurationProvides methods to configure the ACP Component Carrier measurement. RFmxNRMXAcpComponentCarrierResults

### NationalInstruments.RFmx.NRMX

#### Classes

| Name | Description |
| --- | --- |
| RFmxNRMX | Defines a root class which is used to identify and control NR signal configuration. |
| RFmxNRMXAcp | Represents the ACP measurement. |
| RFmxNRMXAcpComponentCarrierConfiguration | Provides methods to configure the ACP Component Carrier measurement. |
| RFmxNRMXAcpComponentCarrierResults | Provides methods to fetch and read the ACP Component Carrier results. |
| RFmxNRMXAcpConfiguration | Provides methods to configure the ACP measurement. |
| RFmxNRMXAcpResults | Provides methods to fetch and read the ACP measurement results. |
| RFmxNRMXChp | Represents the CHP measurement. |
| RFmxNRMXChpComponentCarrierConfiguration | Provides methods to configure the CHP Component Carrier measurement. |
| RFmxNRMXChpComponentCarrierResults | Provides methods to fetch and read the CHP Component Carrier results. |
| RFmxNRMXChpConfiguration | Provides methods to configure the CHP measurement. |
| RFmxNRMXChpResults | Provides methods to fetch and read the CHP measurement results. |
| RFmxNRMXComponentCarrier | Represents Component Carrier. |
| RFmxNRMXConstants | Specifies constants for I/O terminals. |
| RFmxNRMXList | Defines a root class which is used to identify and control NR list. |
| RFmxNRMXModAcc | Represents the ModAcc measurement. |
| RFmxNRMXModAccConfiguration | Provides methods to configure the ModAcc measurement. |
| RFmxNRMXModAccResults | Provides methods to fetch and read the ModAcc measurement results. |
| RFmxNRMXObw | Represents the OBW measurement. |
| RFmxNRMXObwConfiguration | Provides methods to configure the OBW measurement. |
| RFmxNRMXObwResults | Provides methods to fetch and read the OBW measurement results. |
| RFmxNRMXPvt | Represents the PVT measurement. |
| RFmxNRMXPvtConfiguration | Provides methods to configure the PVT measurement. |
| RFmxNRMXPvtResults | Provides methods to fetch and read the PVT measurement results. |
| RFmxNRMXSem | Represents the SEM measurement. |
| RFmxNRMXSemComponentCarrierConfiguration | Provides methods to configure the SEM Component Carrier measurement. |
| RFmxNRMXSemComponentCarrierResults | Provides methods to fetch and read the SEM Component Carrier results. |
| RFmxNRMXSemConfiguration | Provides methods to configure the SEM measurement. |
| RFmxNRMXSemResults | Provides methods to fetch and read the SEM measurement results. |
| RFmxNRMXSubObject | Represents members that are common to all sub-object of RFmxNRMX classes. |
| RFmxNRMXTxp | Represents the TXP measurement. |
| RFmxNRMXTxpConfiguration | Provides methods to configure the TXP measurement. |
| RFmxNRMXTxpResults | Provides methods to fetch and read the TXP measurement results. |

#### Interfaces

None

#### Structures

None

#### Enumerations

| Name | Description |
| --- | --- |
| RFmxNRMXAcpAmplitudeCorrectionType | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |
| RFmxNRMXAcpAveragingEnabled | Specifies whether to enable averaging for the ACP measurement. |
| RFmxNRMXAcpAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement. |
| RFmxNRMXAcpChannelConfigurationType | Specifies the method to configure the carrier and the offset channel settings. |
| RFmxNRMXAcpFftOverlapMode | Specifies the overlap mode when you set the SetMeasurementMethod(string, RFmxNRMXAcpMeasurementMethod) method to SequentialFft. In the Sequential FFT method, the measurement divides all the acquired samples into smaller FFT chunks of equal size. The FFT is then computed for each chunk. The resultant FFTs are averaged to get the spectrum used to compute the ACP. |
| RFmxNRMXAcpFftWindow | Specifies the FFT window type to be used to reduce spectral leakage. |
| RFmxNRMXAcpIFOutputPowerOffsetAuto | Specifies whether the measurement computes an appropriate IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. This method is applicable only when you set the SetMeasurementMethod(string, RFmxNRMXAcpMeasurementMethod) method to DynamicRange. |
| RFmxNRMXAcpMeasurementMethod | Specifies the method for performing the ACP measurement. |
| RFmxNRMXAcpMeasurementMode | Specifies whether the measurement calibrates the noise floor of analyzer or performs the ACP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| RFmxNRMXAcpNoiseCalibrationAveragingAuto | Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration. |
| RFmxNRMXAcpNoiseCalibrationDataValid | Indicates whether calibration data is valid for the configuration specified by the signal name in the selectorstring parameter. |
| RFmxNRMXAcpNoiseCalibrationMode | Specifies whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| RFmxNRMXAcpNoiseCompensationEnabled | Specifies whether RFmx compensates for the instrument noise when performing the measurement when you set SetNoiseCalibrationMode(string, RFmxNRMXAcpNoiseCalibrationMode) method to Auto, or when you set ACP Noise Cal Mode to Manual and SetMeasurementMode(string, RFmxNRMXAcpMeasurementMode) method to Measure Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| RFmxNRMXAcpNoiseCompensationType | Specifies the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| RFmxNRMXAcpOffsetSideband | Specifies the sideband measured for the offset channel. |
| RFmxNRMXAcpPowerUnits | Specifies the unit for absolute power. |
| RFmxNRMXAcpRbwAutoBandwidth | Specifies whether the measurement computes the RBW. |
| RFmxNRMXAcpRbwFilterType | Specifies the shape of the RBW filter. |
| RFmxNRMXAcpSweepTimeAuto | Specifies whether the measurement sets the sweep time. |
| RFmxNRMXAcquisitionBandwidthOptimizationEnabled | Specifies whether RFmx optimizes the acquisition bandwidth. This may cause acquisition center frequency or local oscillator (LO) to be placed at different position than you configured. |
| RFmxNRMXAutoCellIDDetectionEnabled | Specifies whether to enable the autodetection of the cell ID. |
| RFmxNRMXAutoIncrementCellIDEnabled | Specifies whether the cell ID of component carrier is auto calculated and configured by the measurement or configured by the user. |
| RFmxNRMXAutoResourceBlockDetectionEnabled | Specifies whether the values of modulation type, number of resource block clusters, resource block offsets, and number of resource blocks are auto-detected by the measurement or configured by you. |
| RFmxNRMXBandwidthPartCyclicPrefixMode | Specifies the cyclic prefix (CP) duration and the number of symbols in a slot for the signal being measured. |
| RFmxNRMXBandwidthPartDCLocationKnown | Specifies whether Uplink Tx Direct Current location within the carrier is determined. If set to False, DC location is undetermined within the carrier. In ModAcc measurement, IQ impairments are not estimated and compensated, and only General In-Band Emission limits are applied. If set to True, DC location is determined within the carrier. This property is not supported when Link Direction property is set to Downlink. Use "bwp(m)" or "carrier(k)" or "subblock(n)" or "subblock(n)/carrier(k)/bwp(m)" as the Selector Strings to configure or read this property. |
| RFmxNRMXChpAmplitudeCorrectionType | Specifies whether the amplitude of frequency bins in the spectrum used by the measurement is corrected for external attenuation at RF center frequency or corrected for external attenuation at individual frequency bins Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |
| RFmxNRMXChpAveragingEnabled | Specifies whether to enable averaging for the CHP measurement. |
| RFmxNRMXChpAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for CHP measurement. |
| RFmxNRMXChpFftWindow | Specifies the FFT window type to be used to reduce spectral leakage. |
| RFmxNRMXChpIntegrationBandwidthType | Specifies the integration bandwidth (IBW) type used to measure the power of the acquired signal. Integration bandwidth is the frequency interval over which the power in each frequency bin is added to measure the total power in that interval. |
| RFmxNRMXChpMeasurementMode | Specifies whether the measurement calibrates the noise floor of analyzer or performs the CHP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| RFmxNRMXChpNoiseCalibrationAveragingAuto | Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration. |
| RFmxNRMXChpNoiseCalibrationDataValid | Indicates whether calibration data is valid for the configuration specified by the signal name in the selectorstring parameter. |
| RFmxNRMXChpNoiseCalibrationMode | Specifies whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| RFmxNRMXChpNoiseCompensationEnabled | Specifies whether RFmx compensates for the instrument noise when performing the measurement. To compensate for instrument noise when performing a CHP measurement, set the SetNoiseCalibrationMode(string, RFmxNRMXChpNoiseCalibrationMode) method to Auto, or set the CHP Noise Cal Mode method to Manual and the SetMeasurementMode(string, RFmxNRMXChpMeasurementMode) method to Measure. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| RFmxNRMXChpNoiseCompensationType | Specifies the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| RFmxNRMXChpRbwAutoBandwidth | Specifies whether the measurement computes the RBW. |
| RFmxNRMXChpRbwFilterType | Specifies the shape of the digital RBW filter. |
| RFmxNRMXChpSweepTimeAuto | Specifies whether the measurement sets the sweep time. |
| RFmxNRMXComponentCarrierAllocated | Specifies whether a component carrier has one or more resource elements allocated. While performing IBE measurement on a subblock, you set this method to False for all secondary component carriers as specified in section 6.4A.2.3 of 3GPP 38.521-1 and 3GPP 38.521-2 specifications. |
| RFmxNRMXComponentCarrierRadioAccessType | Specifies if a carrier is a NR or an E-UTRA carrier while using dual connectivity (EN-DC) signal. |
| RFmxNRMXComponentCarrierSpacingType | Specifies the spacing between adjacent component carriers (CCs) within a subblock. |
| RFmxNRMXCoresetCceToRegMappingType | Specifies the CCE-to-REG mapping type of CORESET. |
| RFmxNRMXCoresetPrecodingGranularity | Specifies the precoding granularity of the CORESET. |
| RFmxNRMXDigitalEdgeTriggerEdge | Specifies the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxNRMXTriggerType) method to DigitalEdge. |
| RFmxNRMXDownlinkChannelConfigurationMode | Specifies the downlink channel configuration mode. |
| RFmxNRMXDownlinkTestModel | Specifies the NR test model type when you set the Channel Configuration Mode method to Test Model. Refer to section 4.9.2 of the 3GPP 38.141 specification for more information regarding test model configurations. |
| RFmxNRMXDownlinkTestModelCellIDMode | Specifies whether the cell ID of downlink test model component carriers is auto calculated and configured by the measurement or configured by the user. |
| RFmxNRMXDownlinkTestModelDuplexScheme | Specifies the duplexing technique of the signal being measured. Refer to section 4.9.2 of 3GPP 38.141 specification for more information regarding test model configurations based on duplex scheme. |
| RFmxNRMXDownlinkTestModelModulationType | Specifies the modulation type to be used with the selected test model. Selecting the modulation type is supported only for test models NR-FR2-TM3.1 and NR-FR2-TM2. |
| RFmxNRMXFrequencyRange | Specifies whether to use channel bandwidth and subcarrier spacing configuration supported in the frequency range 1 (sub 6 GHz) or the frequency range 2 (above 24 GHz). |
| RFmxNRMXGridSizeMode | Specifies whether to set the grid size of all BWPs and SSB in a component carrier automatically or manually. |
| RFmxNRMXIQPowerEdgeTriggerLevelType | Specifies the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(string, RFmxNRMXTriggerType) method to IQPowerEdge. |
| RFmxNRMXIQPowerEdgeTriggerSlope | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. |
| RFmxNRMXLimitedConfigurationChange | Specifies the set of properties that are considered by RFmx in the locked signal configuration state. |
| RFmxNRMXLinkDirection | Specifies the direction for which the frequency is calculated. Only Uplink is supported. |
| RFmxNRMXListStepTimerUnit | Specifies the units in which SetListStepTimerDuration(string, double) and SetListStepTimerOffset(string, double) are specified. |
| RFmxNRMXMeasurementTypes | Specifies the type of measurement. |
| RFmxNRMXModAccAutoLevelAllowOverflow | Specifies whether the AutoLevel(string, double) function should search for the optimum reference levels while allowing ADC overflow. |
| RFmxNRMXModAccAveragingEnabled | Enables averaging for the measurement. |
| RFmxNRMXModAccCalibrationDataValid | Returns whether the calibration data is valid. |
| RFmxNRMXModAccChannelEstimationType | Specifies the method used for channel estimation. |
| RFmxNRMXModAccCommonClockSourceEnabled | Specifies whether same reference clock is used for local oscillator and digital-to-analog converter. When same reference clock is used the Carrier Frequency Offset is proportional to Sample Clock Error. |
| RFmxNRMXModAccCompositeResultsIncludeDmrs | Specifies whether the DMRS resource elements are included for composite EVM and magnitude and phase error results and traces. |
| RFmxNRMXModAccCompositeResultsIncludePtrs | Specifies whether the PTRS resource elements are included for composite EVM and magnitude and phase error results and traces. |
| RFmxNRMXModAccDCSubcarrierRemovalEnabled | Specifies whether the DC subcarrier is removed from the EVM results. |
| RFmxNRMXModAccEvmReferenceDataSymbolsMode | Specifies whether to either use a reference waveform or an acquired waveform to create reference data symbols for EVM computation. |
| RFmxNRMXModAccEvmUnit | Specifies the units of the EVM results. |
| RFmxNRMXModAccFftWindowType | Specifies the FFT window type used for EVM calculation. |
| RFmxNRMXModAccFrequencyErrorEstimation | Specifies the operation mode of frequency error estimation. If frequency error is absent in the signal to be analyzed, you may disable frequency estimation to reduce measurement time or to avoid measurement inaccuracy due to error in frequency error estimation. |
| RFmxNRMXModAccIQGainImbalanceCorrectionEnabled | Specifies whether to enable IQ gain imbalance correction. |
| RFmxNRMXModAccIQImpairmentsModel | Specifies the I/Q impairments model used by the measurement for estimating I/Q impairments. |
| RFmxNRMXModAccIQImpairmentsPerSubcarrierEnabled | Specifies whether to return I/Q impairments independently for each subcarrier. |
| RFmxNRMXModAccIQMismatchEstimationEnabled | Specifies whether to estimate the IQ impairments such as IQ gain imbalance and quadrature skew. |
| RFmxNRMXModAccIQOriginOffsetEstimationEnabled | Specifies whether to estimate the IQ origin offset. If IQ origin offset is absent in the signal to be analyzed, you may disable IQ origin offset estimation to reduce measurement time or to avoid measurement inaccuracy due to error in IQ origin offset estimation. |
| RFmxNRMXModAccIQQuadratureErrorCorrectionEnabled | Specifies whether to enable IQ quadrature error correction. |
| RFmxNRMXModAccIQTimingSkewCorrectionEnabled | Specifies whether to enable IQ timing skew correction. |
| RFmxNRMXModAccMagnitudeAndPhaseErrorEnabled | Specifies whether to measure the magnitude and the phase error. |
| RFmxNRMXModAccMeasurementLengthUnit | Specifies the units in which measurement offset and measurement length are specified. |
| RFmxNRMXModAccMeasurementMode | Specifies whether the measurement should calibrate the noise floor of the analyzer or perform the ModAcc measurement. |
| RFmxNRMXModAccMulticarrierFilterEnabled | Specifies whether to use the filter in single carrier configurations to minimize leakage into the carrier. Measurement ignores this method, if number of carriers is set to more than 1 or if you set the SetAcquisitionBandwidthOptimizationEnabled(string, RFmxNRMXAcquisitionBandwidthOptimizationEnabled) method to False, where in the multi carrier filter will always be used. |
| RFmxNRMXModAccNoiseCompensationApplied | Specifies whether the noise compensation is applied to the EVM measurement. |
| RFmxNRMXModAccNoiseCompensationEnabled | Specifies whether the contribution of the instrument noise is compensated for EVM computation. You must measure the noise floor before applying the noise compensation. The instrument noise floor is measured for the RF path used by the ModAcc measurement and cached for future use. Supported devices are NI 5831 and NI 5840/41. |
| RFmxNRMXModAccNoiseCompensationInputPowerCheckEnabled | Specifies whether the measurement checks if any high power signal is present at the RFIn port of the instrument while performing noise floor calibration. |
| RFmxNRMXModAccPhaseTrackingMode | Specifies the method used for phase tracking. |
| RFmxNRMXModAccPreFftErrorEstimationInterval | Specifies the interval used for Pre-FFT error estimation. |
| RFmxNRMXModAccShortFrameEnabled | Specifies whether the input signal has a periodicity shorter than the NR frame duration. |
| RFmxNRMXModAccShortFrameLengthUnit | Specifies the units in which Short Frame Length is specified. |
| RFmxNRMXModAccSpectralFlatnessCondition | Specifies the test condition for Spectral Flatness measurement. |
| RFmxNRMXModAccSpectrumInverted | Specifies whether the spectrum of the signal being measured is inverted. This happens when I and Q component of the baseband complex signal is swapped. |
| RFmxNRMXModAccSymbolClockErrorEstimationEnabled | Specifies whether to estimate symbol clock error. This method is ignored when the Common Clock Source Enabled method is True and the Frequency Error Estimation method is Disabled, in which case, symbol clock error is not estimated. If symbol clock error is absent in the signal to be analyzed, you may disable symbol clock error estimation to reduce measurement time or to avoid measurement inaccuracy due to error in symbol clock error estimation. |
| RFmxNRMXModAccSynchronizationMode | Specifies whether the measurement is performed from slot or frame boundary. |
| RFmxNRMXModAccTimingTrackingMode | Specifies the method used for timing tracking. |
| RFmxNRMXModAccTransientPeriodEvmMode | Configures the EVM measurement behavior for symbols affected by power transients. |
| RFmxNRMXObwAmplitudeCorrectionType | Specifies whether the amplitude of frequency bins in the spectrum used by the measurement is corrected for external attenuation at RF center frequency or corrected for external attenuation at individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |
| RFmxNRMXObwAveragingEnabled | Specifies whether to enable averaging for the OBW measurement. |
| RFmxNRMXObwAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. |
| RFmxNRMXObwFftWindow | Specifies the FFT window type to be used to reduce spectral leakage. |
| RFmxNRMXObwPowerIntegrationMethod | Specifies if the OBW measurement window is centered around the signal or the RF Center frequency. |
| RFmxNRMXObwRbwAutoBandwidth | Specifies whether the measurement computes the RBW. |
| RFmxNRMXObwRbwFilterType | Specifies the shape of the digital RBW filter. |
| RFmxNRMXObwSpanAuto | Specifies whether the frequency range of the spectrum used for the OBW measurement is auto computed or configured by the user. |
| RFmxNRMXObwSweepTimeAuto | Specifies whether the measurement sets the sweep time. |
| RFmxNRMXPdschDmrsConfigurationType | Specifies the configuration type of DMRS. |
| RFmxNRMXPdschDmrsDuration | Specifies whether the DMRS is single-symbol or double-symbol. |
| RFmxNRMXPdschDmrsPowerMode | Specifies whether the configured SetPdschDmrsPower(string, double) is calculated based on the SetPdschDmrsNumberOfCdmGroups(string, int) or specified by you. |
| RFmxNRMXPdschDmrsReleaseVersion | Specifies the 3GGP release version for PDSCH DMRS. |
| RFmxNRMXPdschDmrsScramblingIDMode | Specifies whether the configured Scrambling ID is based on SetCellID(string, int) or specified by you. |
| RFmxNRMXPdschMappingType | Specifies the mapping type of DMRS. |
| RFmxNRMXPdschModulationType | Specifies the modulation scheme used in PDSCH channel of the signal being measured. |
| RFmxNRMXPdschPtrsEnabled | Specifies whether PT-RS is present in the transmitted signal. |
| RFmxNRMXPdschPtrsPowerMode | Specifies whether the configured SetPdschPtrsPower(string, double) is calculated as defined in 3GPP specification or configured by you. |
| RFmxNRMXPhaseCompensation | Specifies whether phase compensation is disabled, auto-set by the measurement or set by the you. |
| RFmxNRMXPiBy2BpskPowerBoostEnabled | Specifies the power boost for PI/2 BPSK signal when you set the SetFrequencyRange(string, RFmxNRMXFrequencyRange) method to Range1. This method is valid only for uplink direction. |
| RFmxNRMXPropertyId | Specifies all the attribute identifiers. |
| RFmxNRMXPuschDmrsConfigurationType | Specifies the configuration type of DMRS. |
| RFmxNRMXPuschDmrsDuration | Specifies whether the DMRS is single-symbol or double-symbol. |
| RFmxNRMXPuschDmrsGroupHoppingEnabled | Specifies whether the group hopping is enabled. This method is valid only when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to True. |
| RFmxNRMXPuschDmrsPowerMode | Specifies whether the value of SetPuschDmrsPower(string, double) method is calculated based on the SetPuschDmrsNumberOfCdmGroups(string, int) method or specified by you. |
| RFmxNRMXPuschDmrsPuschIDMode | Specifies whether PUSCH DMRS PUSCH ID is based on SetCellID(string, int) or specified by you. This method is valid only when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to True. |
| RFmxNRMXPuschDmrsReleaseVersion | Specifies the 3GGP release version for PUSCH DMRS. |
| RFmxNRMXPuschDmrsScramblingIDMode | Specifies whether the configured Scrambling ID is honored or the Cell ID is used for reference signal generation. |
| RFmxNRMXPuschDmrsSequenceHoppingEnabled | Specifies whether the sequence hopping is enabled. This method is valid only when you set the SetPuschTransformPrecodingEnabled(string, RFmxNRMXPuschTransformPrecodingEnabled) method to True. |
| RFmxNRMXPuschMappingType | Specifies the mapping type of DMRS. |
| RFmxNRMXPuschModulationType | Specifies the modulation scheme used in the physical uplink shared channel (PUSCH) of the signal being measured. |
| RFmxNRMXPuschPtrsEnabled | Specifies whether the PUSCH transmission contains PTRS signals. |
| RFmxNRMXPuschPtrsPowerMode | Specifies whether the PUSCH PTRS power scaling is calculated as defined in 3GPP specification or specified by you. This method is valid only if you set the SetPuschPtrsEnabled(string, RFmxNRMXPuschPtrsEnabled) method to True. |
| RFmxNRMXPuschTransformPrecodingEnabled | Specifies whether transform precoding is enabled. Enable transform precoding when analyzing a DFT-s-OFDM waveform. |
| RFmxNRMXPvtAveragingEnabled | Specifies whether to enable averaging for the power versus time (PVT) measurement. |
| RFmxNRMXPvtAveragingType | Specifies the measurement averaging type. |
| RFmxNRMXPvtMeasurementIntervalAuto | Specifies whether the measurement interval is computed by the measurement or configured by the user through Measurement Interval method. Setting this method to False is supported for downlink only. |
| RFmxNRMXPvtMeasurementMethod | Specifies the PVT measurement method. |
| RFmxNRMXPvtMeasurementStatus | Returns the measurement status indicating whether the off power before and after is within the standard defined limit. |
| RFmxNRMXReferenceGridAlignmentMode | Specifies whether to align the bandwidthparts and the SSB in a component carrier to a reference resource grid automatically or manually. |
| RFmxNRMXSatelliteAccessNodeClass | Specifies the downlink SAN (Satellite Access Node) class representing the satellite constellation as specified in section 6.6.4 of (3GPP 38.108) specification. |
| RFmxNRMXSchDetectedModulationType | Returns the modulation of the shared channel user data if you set the SetAutoResourceBlockDetectionEnabled(string, RFmxNRMXAutoResourceBlockDetectionEnabled) method to True; otherwise, returns the configured modulation of the shared user data. In case of downlink test model, the modulation type specified by the 3GPP standard is returned. |
| RFmxNRMXSemAmplitudeCorrectionType | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr_CfgExternalAttenuationTable function to configure the external attenuation table. |
| RFmxNRMXSemAveragingEnabled | Specifies whether to enable averaging for the SEM measurement. |
| RFmxNRMXSemAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement. |
| RFmxNRMXSemDownlinkMaskType | Specifies the limits to be used in the measurement for Downlink. |
| RFmxNRMXSemFftWindow | Specifies the FFT window type to be used to reduce spectral leakage. |
| RFmxNRMXSemLowerOffsetMeasurementStatus | Returns the measurement status based on the spectrum emission limits defined by the standard mask type that you configure in the SetUplinkMaskType(string, RFmxNRMXSemUplinkMaskType) method. |
| RFmxNRMXSemMeasurementStatus | Returns the overall measurement status based on the standard mask type that you configure in the SetUplinkMaskType(string, RFmxNRMXSemUplinkMaskType) method. |
| RFmxNRMXSemOffsetFrequencyDefinition | Specifies the definition of the the start frequency and stop frequency of the offset segments. |
| RFmxNRMXSemOffsetLimitFailMask | Specifies the criteria to determine the measurement fail status. |
| RFmxNRMXSemOffsetRbwFilterType | Specifies the shape of a digital RBW filter. |
| RFmxNRMXSemOffsetSideband | Specifies whether the offset segment is present either on one side or on both sides of a carrier. |
| RFmxNRMXSemSweepTimeAuto | Specifies whether the measurement sets the sweep time. |
| RFmxNRMXSemUplinkMaskType | Specifies the spectrum emission mask used in the measurement for uplink. You must set the mask type to Custom to configure the custom offset masks. Refer to section 6.5.2 of the 3GPP 38.101 specification for more information about standard-defined mask types. |
| RFmxNRMXSemUpperOffsetMeasurementStatus | Returns the measurement status based on the user-configured standard measurement limits. Spectrum emission limits can be defined by setting SetUplinkMaskType(string, RFmxNRMXSemUplinkMaskType) method. |
| RFmxNRMXSsbEnabled | Specifies whether synchronization signal block (SSB) is present in the transmitted signal. |
| RFmxNRMXSsbPattern | Specifies the candidate SS/PBCH blocks with different subcarrier spacing configurations as defined in the section 4.1 of 3GPP TS 38.213 specification. In order to configure Case C up to 1.88GHz unpaired spectrum, configure this method to CaseCUpTo3GHz. Similarly, to configure Case C 1.88GHz to 6GHz unpaired spectrum, configure this method to CaseC3GHzTo6GHz. |
| RFmxNRMXTransmitterArchitecture | Specifies the RF architecture at the transmitter, whether each component carriers have a separate LO or one common LO for the entire subblock. |
| RFmxNRMXTriggerMinimumQuietTimeMode | Specifies whether the measurement computes the minimum quiet time used for triggering. |
| RFmxNRMXTriggerType | Specifies the type of trigger to be used for signal acquisition. |
| RFmxNRMXTxpAveragingEnabled | Specifies whether to enable averaging for TXP measurement. |
| RFmxNRMXgNodeBCategory | Specifies the downlink gNodeB (base station) category. Refer to the 3GPP 38.104 specification for more information about gNodeB category. |
| RFmxNRMXgNodeBType | Specifies the downlink gNodeB (Base Station) type. Refer to the 3GPP 38.104 specification for more information about gNodeB Type. |

#### Delegates

None
