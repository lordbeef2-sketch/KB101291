# NI DOCUMENT BUNDLE: rfmxgsm-dotnet-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxgsm-dotnet-api-ref start=251 end=339 -->
<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getmodulationnumberofoffsets__string-out.html language=enus -->
## TOPIC 00251: GetModulationNumberOfOffsets(string, out int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getmodulationnumberofoffsets__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getmodulationnumberofoffsets__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to modulation. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetModulationNumberOfOffsets(string selectorString, out int value)RemarksThis method gets the value

### GetModulationNumberOfOffsets(string, out int)

Gets the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetModulationNumberOfOffsets(string selectorString, out int value)

#### Remarks

This method gets the value of [OrfsModulationNumberOfOffsets](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getmodulationoffsetfrequency__string-out.html language=enus -->
## TOPIC 00252: GetModulationOffsetFrequency(string, out float)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getmodulationoffsetfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getmodulationoffsetfrequency__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of positive frequency offset for which to measure the spectrum due to modulation measurement. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetModulationOffsetFrequency(string selectorString, out float value)RemarksThis method gets the value

### GetModulationOffsetFrequency(string, out float)

Gets the value of positive frequency offset for which to measure the spectrum due to modulation measurement. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetModulationOffsetFrequency(string selectorString, out float value)

#### Remarks

This method gets the value of [OrfsModulationOffsetFrequency](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the modoffset number. Example: "modoffset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out float | Upon return, contains the value of positive frequency offset for which to measure the spectrum due to modulation measurement. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getmodulationoffsetrbw__string-out.html language=enus -->
## TOPIC 00253: GetModulationOffsetRbw(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getmodulationoffsetrbw__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getmodulationoffsetrbw__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the resolution bandwidth used for ORFS due to modulation measurement. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetModulationOffsetRbw(string selectorString, out double value)RemarksThis method gets the value of OrfsModulationOffsetRbw attribute.Th

### GetModulationOffsetRbw(string, out double)

Gets the resolution bandwidth used for ORFS due to modulation measurement. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetModulationOffsetRbw(string selectorString, out double value)

#### Remarks

This method gets the value of [OrfsModulationOffsetRbw](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 30000.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the modoffset number. Example: "modoffset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the resolution bandwidth used for ORFS due to modulation measurement. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getnoisecompensationenabled__string-out.html language=enus -->
## TOPIC 00254: GetNoiseCompensationEnabled(string, out RFmxGsmMXOrfsNoiseCompensationEnabled)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getnoisecompensationenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getnoisecompensationenabled__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Noise compensation is applicable only on modulation offsets and not on switching offsets. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetNoiseCompensationEnabled(string select

### GetNoiseCompensationEnabled(string, out RFmxGsmMXOrfsNoiseCompensationEnabled)

Gets whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Noise compensation is applicable only on modulation offsets and not on switching offsets.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetNoiseCompensationEnabled(string selectorString, out RFmxGsmMXOrfsNoiseCompensationEnabled value)

#### Remarks

This method gets the value of [OrfsNoiseCompensationEnabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsnoisecompensationenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxGsmMXOrfsNoiseCompensationEnabled | Upon return, contains whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Noise compensation is applicable only on modulation offsets and not on switching offsets. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832 |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getnumberofanalysisthreads__string-out.html language=enus -->
## TOPIC 00255: GetNumberOfAnalysisThreads(string, out int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getnumberofanalysisthreads__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getnumberofanalysisthreads__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum number of threads used for parallelism for the output radio frequency spectrum (ORFS) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the

### GetNumberOfAnalysisThreads(string, out int)

Gets the maximum number of threads used for parallelism for the output radio frequency spectrum (ORFS) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetNumberOfAnalysisThreads(string selectorString, out int value)

#### Remarks

This method gets the value of [OrfsNumberOfAnalysisThreads](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the maximum number of threads used for parallelism for the output radio frequency spectrum (ORFS) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getoffsetfrequencymode__string-out.html language=enus -->
## TOPIC 00256: GetOffsetFrequencyMode(string, out RFmxGsmMXOrfsOffsetFrequencyMode)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getoffsetfrequencymode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getoffsetfrequencymode__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetOffsetFrequencyMode(string selectorString, out RFmxGsmMXOrfsOffsetFrequencyMode value)RemarksThis method gets the value o

### GetOffsetFrequencyMode(string, out RFmxGsmMXOrfsOffsetFrequencyMode)

Gets the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetOffsetFrequencyMode(string selectorString, out RFmxGsmMXOrfsOffsetFrequencyMode value)

#### Remarks

This method gets the value of [OrfsOffsetFrequencyMode](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Standard](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsoffsetfrequencymode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxGsmMXOrfsOffsetFrequencyMode | Upon return, contains the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getswitchingcarrierrbw__string-out.html language=enus -->
## TOPIC 00257: GetSwitchingCarrierRbw(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getswitchingcarrierrbw__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getswitchingcarrierrbw__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RBW used for measuring switching carrier power in Hz. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetSwitchingCarrierRbw(string selectorString, out double value)RemarksThis method gets the value of OrfsSwitchingCarrierRbw attribute.The default value is 300kHz.ParametersNameTyp

### GetSwitchingCarrierRbw(string, out double)

Gets the RBW used for measuring switching carrier power in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetSwitchingCarrierRbw(string selectorString, out double value)

#### Remarks

This method gets the value of [OrfsSwitchingCarrierRbw](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 300kHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the RBW used for measuring switching carrier power in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getswitchingnumberofoffsets__string-out.html language=enus -->
## TOPIC 00258: GetSwitchingNumberOfOffsets(string, out int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getswitchingnumberofoffsets__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getswitchingnumberofoffsets__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to switching. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetSwitchingNumberOfOffsets(string selectorString, out int value)RemarksThis method gets the value of

### GetSwitchingNumberOfOffsets(string, out int)

Gets the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to switching.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetSwitchingNumberOfOffsets(string selectorString, out int value)

#### Remarks

This method gets the value of [OrfsSwitchingNumberOfOffsets](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to switching. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getswitchingoffsetfrequency__string-out.html language=enus -->
## TOPIC 00259: GetSwitchingOffsetFrequency(string, out float)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getswitchingoffsetfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getswitchingoffsetfrequency__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of positive frequency offset for which to measure the spectrum due to switching measurement. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetSwitchingOffsetFrequency(string selectorString, out float value)RemarksThis method gets the value of

### GetSwitchingOffsetFrequency(string, out float)

Gets the value of positive frequency offset for which to measure the spectrum due to switching measurement. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetSwitchingOffsetFrequency(string selectorString, out float value)

#### Remarks

This method gets the value of [OrfsSwitchingOffsetFrequency](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out float | Upon return, contains the value of positive frequency offset for which to measure the spectrum due to switching measurement. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getswitchingoffsetrbw__string-out.html language=enus -->
## TOPIC 00260: GetSwitchingOffsetRbw(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getswitchingoffsetrbw__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-getswitchingoffsetrbw__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the resolution bandwidth used for ORFS due to switching measurement. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetSwitchingOffsetRbw(string selectorString, out double value)RemarksThis method gets the value of OrfsSwitchingOffsetRbw attribute.The d

### GetSwitchingOffsetRbw(string, out double)

Gets the resolution bandwidth used for ORFS due to switching measurement. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetSwitchingOffsetRbw(string selectorString, out double value)

#### Remarks

This method gets the value of [OrfsSwitchingOffsetRbw](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 30000.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the resolution bandwidth used for ORFS due to switching measurement. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setalltracesenabled__string-bool.html language=enus -->
## TOPIC 00261: SetAllTracesEnabled(string, bool)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setalltracesenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setalltracesenabled__string-bool.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the traces to be stored and retrieved after performing the output radio frequency spectrum (ORFS) measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetAllTracesEnabled(string selectorString, bool value)RemarksThis method sets the value of OrfsAllTracesEnab

### SetAllTracesEnabled(string, bool)

Sets whether to enable the traces to be stored and retrieved after performing the output radio frequency spectrum (ORFS) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetAllTracesEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [OrfsAllTracesEnabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the traces to be stored and retrieved after performing the output radio frequency spectrum (ORFS) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setaveragingcount__string-int.html language=enus -->
## TOPIC 00262: SetAveragingCount(string, int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setaveragingcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setaveragingcount__string-int.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxGsmMXOrfsAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetAveragingCount(string selectorString, int value)RemarksThis method sets the value of OrfsAveragi

### SetAveragingCount(string, int)

Sets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxGsmMXOrfsAveragingEnabled)](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setaveragingenabled__string-rfmxgsmmxorfsaveragingenabled.html) method to [True](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetAveragingCount(string selectorString, int value)

#### Remarks

This method sets the value of [OrfsAveragingCount](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxGsmMXOrfsAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setaveragingenabled__string-rfmxgsmmxorfsaveragingenabled.html language=enus -->
## TOPIC 00263: SetAveragingEnabled(string, RFmxGsmMXOrfsAveragingEnabled)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setaveragingenabled__string-rfmxgsmmxorfsaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setaveragingenabled__string-rfmxgsmmxorfsaveragingenabled.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable averaging for the output radio frequency spectrum (ORFS) measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetAveragingEnabled(string selectorString, RFmxGsmMXOrfsAveragingEnabled value)RemarksThis method sets the value of OrfsAveragingEnabled attribute.Th

### SetAveragingEnabled(string, RFmxGsmMXOrfsAveragingEnabled)

Sets whether to enable averaging for the output radio frequency spectrum (ORFS) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetAveragingEnabled(string selectorString, RFmxGsmMXOrfsAveragingEnabled value)

#### Remarks

This method sets the value of [OrfsAveragingEnabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxGsmMXOrfsAveragingEnabled | Specifies whether to enable averaging for the output radio frequency spectrum (ORFS) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setaveragingtype__string-rfmxgsmmxorfsaveragingtype.html language=enus -->
## TOPIC 00264: SetAveragingType(string, RFmxGsmMXOrfsAveragingType)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setaveragingtype__string-rfmxgsmmxorfsaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setaveragingtype__string-rfmxgsmmxorfsaveragingtype.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the output radio frequency spectrum (ORFS) measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetAveragingType(string selectorString, RFmxGsmMXOrfsAveragingType value)RemarksTh

### SetAveragingType(string, RFmxGsmMXOrfsAveragingType)

Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the output radio frequency spectrum (ORFS) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetAveragingType(string selectorString, RFmxGsmMXOrfsAveragingType value)

#### Remarks

This method sets the value of [OrfsAveragingType](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Log](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsaveragingtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxGsmMXOrfsAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the output radio frequency spectrum (ORFS) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setevaluationsymbolsincludetsc__string-rfmxgsmmxorfsevaluationsymbolsincludetsc.html language=enus -->
## TOPIC 00265: SetEvaluationSymbolsIncludeTsc(string, RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setevaluationsymbolsincludetsc__string-rfmxgsmmxorfsevaluationsymbolsincludetsc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setevaluationsymbolsincludetsc__string-rfmxgsmmxorfsevaluationsymbolsincludetsc.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to include the training sequence code (TSC) portion of the burst in the output radio frequency spectrum (ORFS) measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetEvaluationSymbolsIncludeTsc(string selectorString, RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc value)Rema

### SetEvaluationSymbolsIncludeTsc(string, RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc)

Sets whether to include the training sequence code (TSC) portion of the burst in the output radio frequency spectrum (ORFS) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetEvaluationSymbolsIncludeTsc(string selectorString, RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc value)

#### Remarks

This method sets the value of [OrfsEvaluationSymbolsIncludeTsc](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsevaluationsymbolsincludetsc.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc | Specifies whether to include the training sequence code (TSC) portion of the burst in the output radio frequency spectrum (ORFS) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setevaluationsymbolsscope__string-rfmxgsmmxorfsevaluationsymbolsscope.html language=enus -->
## TOPIC 00266: SetEvaluationSymbolsScope(string, RFmxGsmMXOrfsEvaluationSymbolsScope)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setevaluationsymbolsscope__string-rfmxgsmmxorfsevaluationsymbolsscope.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setevaluationsymbolsscope__string-rfmxgsmmxorfsevaluationsymbolsscope.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the modulation power measurements that will use the part of burst configured using the ConfigureEvaluationSymbols(string, double, RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc, double) method. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetEvaluationSymbolsScope(string selectorString,

### SetEvaluationSymbolsScope(string, RFmxGsmMXOrfsEvaluationSymbolsScope)

Sets the modulation power measurements that will use the part of burst configured using the [ConfigureEvaluationSymbols(string, double, RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc, double)](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configureevaluationsymbols__string-double-rfmxgsmmxorfsevaluationsymbolsincludetsc-double.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetEvaluationSymbolsScope(string selectorString, RFmxGsmMXOrfsEvaluationSymbolsScope value)

#### Remarks

This method sets the value of [OrfsEvaluationSymbolsScope](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [OffsetAndCarrier](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsevaluationsymbolsscope.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxGsmMXOrfsEvaluationSymbolsScope | Specifies the modulation power measurements that will use the part of burst configured using the ConfigureEvaluationSymbols(string, double, RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc, double) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setevaluationsymbolsstart__string-double.html language=enus -->
## TOPIC 00267: SetEvaluationSymbolsStart(string, double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setevaluationsymbolsstart__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setevaluationsymbolsstart__string-double.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the start position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetEvaluationSymbolsStart(string selectorString, double value)RemarksThis method sets

### SetEvaluationSymbolsStart(string, double)

Sets the start position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetEvaluationSymbolsStart(string selectorString, double value)

#### Remarks

This method sets the value of [OrfsEvaluationSymbolsStart](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 50.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the start position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setevaluationsymbolsstop__string-double.html language=enus -->
## TOPIC 00268: SetEvaluationSymbolsStop(string, double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setevaluationsymbolsstop__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setevaluationsymbolsstop__string-double.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the stop position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetEvaluationSymbolsStop(string selectorString, double value)RemarksThis method sets t

### SetEvaluationSymbolsStop(string, double)

Sets the stop position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetEvaluationSymbolsStop(string selectorString, double value)

#### Remarks

This method sets the value of [OrfsEvaluationSymbolsStop](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 90.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the stop position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00269: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the output radio frequency spectrum (ORFS) measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method sets the value of OrfsMeasurementEnabled attribute.The default value is FALSE.Parameters

### SetMeasurementEnabled(string, bool)

Sets whether to enable the output radio frequency spectrum (ORFS) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [OrfsMeasurementEnabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the output radio frequency spectrum (ORFS) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setmeasurementinterval__string-rfmxgsmmxorfsmeasurementinterval.html language=enus -->
## TOPIC 00270: SetMeasurementInterval(string, RFmxGsmMXOrfsMeasurementInterval)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setmeasurementinterval__string-rfmxgsmmxorfsmeasurementinterval.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setmeasurementinterval__string-rfmxgsmmxorfsmeasurementinterval.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement is performed on a single specified timeslot or across multiple timeslots. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetMeasurementInterval(string selectorString, RFmxGsmMXOrfsMeasurementInterval value)RemarksThis method sets the value of OrfsMeasurementIn

### SetMeasurementInterval(string, RFmxGsmMXOrfsMeasurementInterval)

Sets whether the measurement is performed on a single specified timeslot or across multiple timeslots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetMeasurementInterval(string selectorString, RFmxGsmMXOrfsMeasurementInterval value)

#### Remarks

This method sets the value of [OrfsMeasurementInterval](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default Value iss 'Number of Timeslots'.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxGsmMXOrfsMeasurementInterval | Specifies whether the measurement is performed on a single specified timeslot or across multiple timeslots. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setmeasurementoffset__string-int.html language=enus -->
## TOPIC 00271: SetMeasurementOffset(string, int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setmeasurementoffset__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setmeasurementoffset__string-int.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the offset, relative to the trigger of the timeslot to be measured. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetMeasurementOffset(string selectorString, int value)RemarksThis method sets the value of OrfsMeasurementOffset attribute.The default value is 0. Valid values are [0, (

### SetMeasurementOffset(string, int)

Sets the offset, relative to the trigger of the timeslot to be measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetMeasurementOffset(string selectorString, int value)

#### Remarks

This method sets the value of [OrfsMeasurementOffset](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 0. Valid values are [0, (Num Timeslots -1)].

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the offset, relative to the trigger of the timeslot to be measured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setmeasurementtype__string-rfmxgsmmxorfsmeasurementtype.html language=enus -->
## TOPIC 00272: SetMeasurementType(string, RFmxGsmMXOrfsMeasurementType)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setmeasurementtype__string-rfmxgsmmxorfsmeasurementtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setmeasurementtype__string-rfmxgsmmxorfsmeasurementtype.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the type of spectral distortion to be measured. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetMeasurementType(string selectorString, RFmxGsmMXOrfsMeasurementType value)RemarksThis method sets the value of OrfsMeasurementType attribute.The default value is ModulationAndSwitching.P

### SetMeasurementType(string, RFmxGsmMXOrfsMeasurementType)

Sets the type of spectral distortion to be measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetMeasurementType(string selectorString, RFmxGsmMXOrfsMeasurementType value)

#### Remarks

This method sets the value of [OrfsMeasurementType](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [ModulationAndSwitching](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsmeasurementtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxGsmMXOrfsMeasurementType | Specifies the type of spectral distortion to be measured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setmodulationcarrierrbw__string-double.html language=enus -->
## TOPIC 00273: SetModulationCarrierRbw(string, double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setmodulationcarrierrbw__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setmodulationcarrierrbw__string-double.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the RBW used for measuring modulation carrier power in Hz. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetModulationCarrierRbw(string selectorString, double value)RemarksThis method sets the value of OrfsModulationCarrierRbw attribute.The default value is 30kHz.ParametersNameTypeD

### SetModulationCarrierRbw(string, double)

Sets the RBW used for measuring modulation carrier power in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetModulationCarrierRbw(string selectorString, double value)

#### Remarks

This method sets the value of [OrfsModulationCarrierRbw](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 30kHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the RBW used for measuring modulation carrier power in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setmodulationnumberofoffsets__string-int.html language=enus -->
## TOPIC 00274: SetModulationNumberOfOffsets(string, int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setmodulationnumberofoffsets__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setmodulationnumberofoffsets__string-int.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to modulation. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetModulationNumberOfOffsets(string selectorString, int value)RemarksThis method sets the value of O

### SetModulationNumberOfOffsets(string, int)

Sets the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to modulation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetModulationNumberOfOffsets(string selectorString, int value)

#### Remarks

This method sets the value of [OrfsModulationNumberOfOffsets](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to modulation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setmodulationoffsetfrequency__string-float.html language=enus -->
## TOPIC 00275: SetModulationOffsetFrequency(string, float)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setmodulationoffsetfrequency__string-float.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setmodulationoffsetfrequency__string-float.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of positive frequency offset for which to measure the spectrum due to modulation measurement. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetModulationOffsetFrequency(string selectorString, float value)RemarksThis method sets the value of O

### SetModulationOffsetFrequency(string, float)

Sets the value of positive frequency offset for which to measure the spectrum due to modulation measurement. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetModulationOffsetFrequency(string selectorString, float value)

#### Remarks

This method sets the value of [OrfsModulationOffsetFrequency](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the modoffset number. Example: "modoffset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | float | Specifies the value of positive frequency offset for which to measure the spectrum due to modulation measurement. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setnoisecompensationenabled__string-rfmxgsmmxorfsnoisecompensationenabled.html language=enus -->
## TOPIC 00276: SetNoiseCompensationEnabled(string, RFmxGsmMXOrfsNoiseCompensationEnabled)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setnoisecompensationenabled__string-rfmxgsmmxorfsnoisecompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setnoisecompensationenabled__string-rfmxgsmmxorfsnoisecompensationenabled.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Noise compensation is applicable only on modulation offsets and not on switching offsets. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetNoiseCompensationEnabled(string select

### SetNoiseCompensationEnabled(string, RFmxGsmMXOrfsNoiseCompensationEnabled)

Sets whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Noise compensation is applicable only on modulation offsets and not on switching offsets.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetNoiseCompensationEnabled(string selectorString, RFmxGsmMXOrfsNoiseCompensationEnabled value)

#### Remarks

This method sets the value of [OrfsNoiseCompensationEnabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsnoisecompensationenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxGsmMXOrfsNoiseCompensationEnabled | Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Noise compensation is applicable only on modulation offsets and not on switching offsets. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832 |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setnumberofanalysisthreads__string-int.html language=enus -->
## TOPIC 00277: SetNumberOfAnalysisThreads(string, int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setnumberofanalysisthreads__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setnumberofanalysisthreads__string-int.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the maximum number of threads used for parallelism for the output radio frequency spectrum (ORFS) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the

### SetNumberOfAnalysisThreads(string, int)

Sets the maximum number of threads used for parallelism for the output radio frequency spectrum (ORFS) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetNumberOfAnalysisThreads(string selectorString, int value)

#### Remarks

This method sets the value of [OrfsNumberOfAnalysisThreads](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the maximum number of threads used for parallelism for the output radio frequency spectrum (ORFS) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setoffsetfrequencymode__string-rfmxgsmmxorfsoffsetfrequencymode.html language=enus -->
## TOPIC 00278: SetOffsetFrequencyMode(string, RFmxGsmMXOrfsOffsetFrequencyMode)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setoffsetfrequencymode__string-rfmxgsmmxorfsoffsetfrequencymode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setoffsetfrequencymode__string-rfmxgsmmxorfsoffsetfrequencymode.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetOffsetFrequencyMode(string selectorString, RFmxGsmMXOrfsOffsetFrequencyMode value)RemarksThis method sets the value of Or

### SetOffsetFrequencyMode(string, RFmxGsmMXOrfsOffsetFrequencyMode)

Sets the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetOffsetFrequencyMode(string selectorString, RFmxGsmMXOrfsOffsetFrequencyMode value)

#### Remarks

This method sets the value of [OrfsOffsetFrequencyMode](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Standard](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsoffsetfrequencymode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxGsmMXOrfsOffsetFrequencyMode | Specifies the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setswitchingcarrierrbw__string-double.html language=enus -->
## TOPIC 00279: SetSwitchingCarrierRbw(string, double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setswitchingcarrierrbw__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setswitchingcarrierrbw__string-double.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the RBW used for measuring switching carrier power in Hz. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetSwitchingCarrierRbw(string selectorString, double value)RemarksThis method sets the value of OrfsSwitchingCarrierRbw attribute.The default value is 300kHz.ParametersNameTypeDes

### SetSwitchingCarrierRbw(string, double)

Sets the RBW used for measuring switching carrier power in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetSwitchingCarrierRbw(string selectorString, double value)

#### Remarks

This method sets the value of [OrfsSwitchingCarrierRbw](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 300kHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the RBW used for measuring switching carrier power in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setswitchingnumberofoffsets__string-int.html language=enus -->
## TOPIC 00280: SetSwitchingNumberOfOffsets(string, int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setswitchingnumberofoffsets__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setswitchingnumberofoffsets__string-int.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to switching. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetSwitchingNumberOfOffsets(string selectorString, int value)RemarksThis method sets the value of Orf

### SetSwitchingNumberOfOffsets(string, int)

Sets the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to switching.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetSwitchingNumberOfOffsets(string selectorString, int value)

#### Remarks

This method sets the value of [OrfsSwitchingNumberOfOffsets](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to switching. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setswitchingoffsetfrequency__string-float.html language=enus -->
## TOPIC 00281: SetSwitchingOffsetFrequency(string, float)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setswitchingoffsetfrequency__string-float.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-setswitchingoffsetfrequency__string-float.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of positive frequency offset for which to measure the spectrum due to switching measurement. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetSwitchingOffsetFrequency(string selectorString, float value)RemarksThis method sets the value of Orf

### SetSwitchingOffsetFrequency(string, float)

Sets the value of positive frequency offset for which to measure the spectrum due to switching measurement. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetSwitchingOffsetFrequency(string selectorString, float value)

#### Remarks

This method sets the value of [OrfsSwitchingOffsetFrequency](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the offset number. Example: "offset0". You can use the BuildOffsetString(string, int) method to build the selector string. |
| value | float | Specifies the value of positive frequency offset for which to measure the spectrum due to switching measurement. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration.html language=enus -->
## TOPIC 00282: RFmxGsmMXOrfsConfiguration Class

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the ORFS measurement. Derives fromRFmxGsmMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic class RFmxGsmMXOrfsConfiguration : RFmxGsmMXSubObjectMethodsNameDescriptionConfigureAveraging(string, RFmxGsmMXOrfsAveragingEnabled, int, RFmxGsmMXOrfsAveragingType

### RFmxGsmMXOrfsConfiguration Class

Provides methods to configure the ORFS measurement.

#### Derives from

- RFmxGsmMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public class RFmxGsmMXOrfsConfiguration : RFmxGsmMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| ConfigureAveraging(string, RFmxGsmMXOrfsAveragingEnabled, int, RFmxGsmMXOrfsAveragingType) | Configures averaging for the output radio frequency spectrum (ORFS) measurement. |
| ConfigureEvaluationSymbols(string, double, RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc, double) | Configures the evaluation symbols. The GSM standard specifies that 50% to 90% portion of the burst, excluding the midamble, be measured. However, RFmxGSM allows you to specify which portion of the burst to measure for ORFS due to Modulation. RFmx considers the measurement over evaluation symbols for a single burst as one average. |
| ConfigureMeasurementType(string, RFmxGsmMXOrfsMeasurementType) | Configures the type of spectral distortion to be measured. |
| ConfigureModulationCustomOffsetFrequencyArray(string, float[]) | Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of modulation when you set the SetOffsetFrequencyMode(string, RFmxGsmMXOrfsOffsetFrequencyMode) method to Custom. |
| ConfigureModulationCustomOffsetFrequencyArray(string, double[]) | Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of modulation when you set the SetOffsetFrequencyMode(string, RFmxGsmMXOrfsOffsetFrequencyMode) method to Custom. |
| ConfigureNoiseCompensationEnabled(string, RFmxGsmMXOrfsNoiseCompensationEnabled) | Configures whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. supportedDevices: NI 5663/5665, NI 5668R |
| ConfigureOffsetFrequencyMode(string, RFmxGsmMXOrfsOffsetFrequencyMode) | Configures the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements. |
| ConfigureSwitchingCustomOffsetFrequencyArray(string, double[]) | Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of switching when you set the SetOffsetFrequencyMode(string, RFmxGsmMXOrfsOffsetFrequencyMode) method to Custom. |
| ConfigureSwitchingCustomOffsetFrequencyArray(string, float[]) | Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of switching when you set the SetOffsetFrequencyMode(string, RFmxGsmMXOrfsOffsetFrequencyMode) method to Custom. |
| GetAllTracesEnabled(string, out bool) | Gets whether to enable the traces to be stored and retrieved after performing the output radio frequency spectrum (ORFS) measurement. |
| GetAveragingCount(string, out int) | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxGsmMXOrfsAveragingEnabled) method to True. |
| GetAveragingEnabled(string, out RFmxGsmMXOrfsAveragingEnabled) | Gets whether to enable averaging for the output radio frequency spectrum (ORFS) measurement. |
| GetAveragingType(string, out RFmxGsmMXOrfsAveragingType) | Gets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the output radio frequency spectrum (ORFS) measurement. |
| GetEvaluationSymbolsIncludeTsc(string, out RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc) | Gets whether to include the training sequence code (TSC) portion of the burst in the output radio frequency spectrum (ORFS) measurement. |
| GetEvaluationSymbolsScope(string, out RFmxGsmMXOrfsEvaluationSymbolsScope) | Gets the modulation power measurements that will use the part of burst configured using the ConfigureEvaluationSymbols(string, double, RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc, double) method. |
| GetEvaluationSymbolsStart(string, out double) | Gets the start position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage. |
| GetEvaluationSymbolsStop(string, out double) | Gets the stop position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage. |
| GetMeasurementEnabled(string, out bool) | Gets whether to enable the output radio frequency spectrum (ORFS) measurement. |
| GetMeasurementInterval(string, out RFmxGsmMXOrfsMeasurementInterval) | Gets whether the measurement is performed on a single specified timeslot or across multiple timeslots. |
| GetMeasurementOffset(string, out int) | Gets the offset, relative to the trigger of the timeslot to be measured. |
| GetMeasurementType(string, out RFmxGsmMXOrfsMeasurementType) | Gets the type of spectral distortion to be measured. |
| GetModulationCarrierRbw(string, out double) | Gets the RBW used for measuring modulation carrier power in Hz. |
| GetModulationNumberOfOffsets(string, out int) | Gets the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to modulation. |
| GetModulationOffsetFrequency(string, out float) | Gets the value of positive frequency offset for which to measure the spectrum due to modulation measurement. This value is expressed in Hz. |
| GetModulationOffsetRbw(string, out double) | Gets the resolution bandwidth used for ORFS due to modulation measurement. This value is expressed in Hz. |
| GetNoiseCompensationEnabled(string, out RFmxGsmMXOrfsNoiseCompensationEnabled) | Gets whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Noise compensation is applicable only on modulation offsets and not on switching offsets. |
| GetNumberOfAnalysisThreads(string, out int) | Gets the maximum number of threads used for parallelism for the output radio frequency spectrum (ORFS) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| GetOffsetFrequencyMode(string, out RFmxGsmMXOrfsOffsetFrequencyMode) | Gets the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements. |
| GetSwitchingCarrierRbw(string, out double) | Gets the RBW used for measuring switching carrier power in Hz. |
| GetSwitchingNumberOfOffsets(string, out int) | Gets the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to switching. |
| GetSwitchingOffsetFrequency(string, out float) | Gets the value of positive frequency offset for which to measure the spectrum due to switching measurement. This value is expressed in Hz. |
| GetSwitchingOffsetRbw(string, out double) | Gets the resolution bandwidth used for ORFS due to switching measurement. This value is expressed in Hz. |
| SetAllTracesEnabled(string, bool) | Sets whether to enable the traces to be stored and retrieved after performing the output radio frequency spectrum (ORFS) measurement. |
| SetAveragingCount(string, int) | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxGsmMXOrfsAveragingEnabled) method to True. |
| SetAveragingEnabled(string, RFmxGsmMXOrfsAveragingEnabled) | Sets whether to enable averaging for the output radio frequency spectrum (ORFS) measurement. |
| SetAveragingType(string, RFmxGsmMXOrfsAveragingType) | Sets the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the output radio frequency spectrum (ORFS) measurement. |
| SetEvaluationSymbolsIncludeTsc(string, RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc) | Sets whether to include the training sequence code (TSC) portion of the burst in the output radio frequency spectrum (ORFS) measurement. |
| SetEvaluationSymbolsScope(string, RFmxGsmMXOrfsEvaluationSymbolsScope) | Sets the modulation power measurements that will use the part of burst configured using the ConfigureEvaluationSymbols(string, double, RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc, double) method. |
| SetEvaluationSymbolsStart(string, double) | Sets the start position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage. |
| SetEvaluationSymbolsStop(string, double) | Sets the stop position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable the output radio frequency spectrum (ORFS) measurement. |
| SetMeasurementInterval(string, RFmxGsmMXOrfsMeasurementInterval) | Sets whether the measurement is performed on a single specified timeslot or across multiple timeslots. |
| SetMeasurementOffset(string, int) | Sets the offset, relative to the trigger of the timeslot to be measured. |
| SetMeasurementType(string, RFmxGsmMXOrfsMeasurementType) | Sets the type of spectral distortion to be measured. |
| SetModulationCarrierRbw(string, double) | Sets the RBW used for measuring modulation carrier power in Hz. |
| SetModulationNumberOfOffsets(string, int) | Sets the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to modulation. |
| SetModulationOffsetFrequency(string, float) | Sets the value of positive frequency offset for which to measure the spectrum due to modulation measurement. This value is expressed in Hz. |
| SetNoiseCompensationEnabled(string, RFmxGsmMXOrfsNoiseCompensationEnabled) | Sets whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Noise compensation is applicable only on modulation offsets and not on switching offsets. |
| SetNumberOfAnalysisThreads(string, int) | Sets the maximum number of threads used for parallelism for the output radio frequency spectrum (ORFS) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| SetOffsetFrequencyMode(string, RFmxGsmMXOrfsOffsetFrequencyMode) | Sets the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements. |
| SetSwitchingCarrierRbw(string, double) | Sets the RBW used for measuring switching carrier power in Hz. |
| SetSwitchingNumberOfOffsets(string, int) | Sets the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to switching. |
| SetSwitchingOffsetFrequency(string, float) | Sets the value of positive frequency offset for which to measure the spectrum due to switching measurement. This value is expressed in Hz. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsevaluationsymbolsincludetsc.html language=enus -->
## TOPIC 00283: RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsevaluationsymbolsincludetsc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsevaluationsymbolsincludetsc.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to include the training sequence code (TSC) portion of the burst in the output radio frequency spectrum (ORFS) measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXOrfsEvaluationSymbolsIncludeTscMembersNameValueDescriptionFalse0The TSC portion of the bur

### RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc Enumeration

Specifies whether to include the training sequence code (TSC) portion of the burst in the output radio frequency spectrum (ORFS) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The TSC portion of the burst is excluded while completing the ORFS measurement. |
| True | 1 | The TSC portion of the burst is included while completing the ORFS measurement. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsevaluationsymbolsscope.html language=enus -->
## TOPIC 00284: RFmxGsmMXOrfsEvaluationSymbolsScope Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsevaluationsymbolsscope.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsevaluationsymbolsscope.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the modulation power measurements that will use the part of burst configured using the ConfigureEvaluationSymbols(string, double, RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc, double) method. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXOrfsEvaluationSymbolsScopeMembersN

### RFmxGsmMXOrfsEvaluationSymbolsScope Enumeration

Specifies the modulation power measurements that will use the part of burst configured using the [ConfigureEvaluationSymbols(string, double, RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc, double)](nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsconfiguration-configureevaluationsymbols__string-double-rfmxgsmmxorfsevaluationsymbolsincludetsc-double.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXOrfsEvaluationSymbolsScope

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Offset | 0 | Modulation Offset Power measurements will only use the part of burst configured using the RFmxGSM ORFS Configure Evaluation Symbols function. Modulation Carrier Power measurement will use all of the useful part of the burst. |
| OffsetAndCarrier | 1 | Modulation Offset and Carrier Power measurements will both use the part of burst configured using the RFmxGSM ORFS Configure Evaluation Symbols function. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsmeasurementinterval.html language=enus -->
## TOPIC 00285: RFmxGsmMXOrfsMeasurementInterval Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsmeasurementinterval.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsmeasurementinterval.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed on a single specified timeslot or across multiple timeslots. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXOrfsMeasurementIntervalMembersNameValueDescriptionNumberOfTimeslots0The measurement includes all timeslots defined by the Se

### RFmxGsmMXOrfsMeasurementInterval Enumeration

Specifies whether the measurement is performed on a single specified timeslot or across multiple timeslots.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXOrfsMeasurementInterval

#### Members

| Name | Value | Description |
| --- | --- | --- |
| NumberOfTimeslots | 0 | The measurement includes all timeslots defined by the SetNumberOfTimeslots(string, int) method. |
| TimeslotAtOffset | 1 | The measurement is performed only on the timeslot specified by theSetMeasurementOffset(string, int) method. This method is applicable only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge or DigitalEdge. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsmeasurementtype.html language=enus -->
## TOPIC 00286: RFmxGsmMXOrfsMeasurementType Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsmeasurementtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsmeasurementtype.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of spectral distortion to be measured. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXOrfsMeasurementTypeMembersNameValueDescriptionModulationAndSwitching0Measures the spectrum on the modulated part and the switching part of the waveform. Modulation1Measures t

### RFmxGsmMXOrfsMeasurementType Enumeration

Specifies the type of spectral distortion to be measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXOrfsMeasurementType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ModulationAndSwitching | 0 | Measures the spectrum on the modulated part and the switching part of the waveform. |
| Modulation | 1 | Measures the spectrum on the modulated part of the waveform. |
| Switching | 2 | Measures the spectrum on the switching part of the waveform. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsnoisecompensationenabled.html language=enus -->
## TOPIC 00287: RFmxGsmMXOrfsNoiseCompensationEnabled Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsnoisecompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsnoisecompensationenabled.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Noise compensation is applicable only on modulation offsets and not on switching offsets. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832. SyntaxNamespace: NationalInstrum

### RFmxGsmMXOrfsNoiseCompensationEnabled Enumeration

Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Noise compensation is applicable only on modulation offsets and not on switching offsets. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXOrfsNoiseCompensationEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables compensation of the channel powers for the signal analyzer noise floor. |
| True | 1 | Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the output radio frequency spectrum (ORFS) measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are measured again. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsoffsetfrequencymode.html language=enus -->
## TOPIC 00288: RFmxGsmMXOrfsOffsetFrequencyMode Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsoffsetfrequencymode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsoffsetfrequencymode.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXOrfsOffsetFrequencyModeMembersNameValueDescriptionStandard0Uses the list of lower and upper offset frequencie

### RFmxGsmMXOrfsOffsetFrequencyMode Enumeration

Specifies the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXOrfsOffsetFrequencyMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Standard | 0 | Uses the list of lower and upper offset frequencies of 100 kHz, 200 kHz, 250 kHz, 400 kHz, 600 kHz, 800 kHz, 1000 kHz, 1200 kHz, 1400 kHz, 1600 kHz, and 1800 kHz for the spectrum due to the modulation measurement, and the lower and upper offset frequencies of 400 kHz, 600 kHz, 1200 kHz, and 1800 kHz for the spectrum produced by the switching measurement. |
| Short | 1 | Uses the list of lower and upper offset frequencies of 200 kHz, 250 kHz, 400 kHz, 600 kHz, and 1200 kHz for the spectrum due to the modulation measurement, and the lower and upper offset frequencies of 400 kHz, 600 kHz, 1200 kHz, and 1800 kHz for the spectrum produced by the switching measurement. |
| Custom | 2 | Uses the list of frequencies that is configured using the RFmxGSM_ORFSCfgModulationCustomOffsetFrequencyArray and RFmxGSM_ORFSCfgSwitchingCustomOffsetFrequencyArray functions for measurement of spectrum produced by modulation and switching measurements. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsresults-fetchmodulationpowertrace__string-double-ref-ref-ref.html language=enus -->
## TOPIC 00289: FetchModulationPowerTrace(string, double, ref float[], ref float[], ref float[])

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsresults-fetchmodulationpowertrace__string-double-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsresults-fetchmodulationpowertrace__string-double-ref-ref-ref.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the modulation power trace and frequency offset.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int FetchModulationPowerTrace(string selectorString, double timeout, ref float[] offsetFrequency, ref float[] absolutePower, ref float[] relativePower)ParametersNameTypeDescriptionselectorSt

### FetchModulationPowerTrace(string, double, ref float[], ref float[], ref float[])

Fetches the modulation power trace and frequency offset.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int FetchModulationPowerTrace(string selectorString, double timeout, ref float[] offsetFrequency, ref float[] absolutePower, ref float[] relativePower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| offsetFrequency | ref float[] | Upon return, contains an array of modulation offset frequencies at which the measurement is performed in an ascending order. This value is expressed in Hz. |
| absolutePower | ref float[] | Upon return, contains an array of absolute powers corresponding to the modulation offset frequency list. This value is expressed in dBm. |
| relativePower | ref float[] | Upon return, contains an array of relative powers corresponding to modulation offset frequency list. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsresults-fetchmodulationresultsarray__string-double-out-ref-ref-ref-ref.html language=enus -->
## TOPIC 00290: FetchModulationResultsArray(string, double, out double, ref double[], ref double[], ref double[], ref double[])

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsresults-fetchmodulationresultsarray__string-double-out-ref-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsresults-fetchmodulationresultsarray__string-double-out-ref-ref-ref-ref.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the modulation carrier power, absolute powers, and relative powers measured at the modulation offset frequencies. The relative powers are measured relative to the integrated modulation power of the carrier.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int FetchModulationResultsArray(

### FetchModulationResultsArray(string, double, out double, ref double[], ref double[], ref double[], ref double[])

Returns the modulation carrier power, absolute powers, and relative powers measured at the modulation offset frequencies. The relative powers are measured relative to the integrated modulation power of the carrier.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int FetchModulationResultsArray(string selectorString, double timeout, out double modulationCarrierPower, ref double[] lowerRelativePower, ref double[] upperRelativePower, ref double[] lowerAbsolutePower, ref double[] upperAbsolutePower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| modulationCarrierPower | out double | Upon return, contains the modulation carrier power. This value is expressed in dBm. |
| lowerRelativePower | ref double[] | Upon return, contains an array of relative powers measured at the negative modulation offset frequencies. This value is expressed in dB. The relative powers are measured relative to the integrated modulation power of the carrier. |
| upperRelativePower | ref double[] | Upon return, contains an array of relative powers measured at the positive modulation offset frequencies. This value is expressed in dB. The relative powers are measured relative to the integrated modulation power of the carrier. |
| lowerAbsolutePower | ref double[] | Upon return, contains an array of absolute powers measured at the negative modulation offset frequencies. This value is expressed in dBm. |
| upperAbsolutePower | ref double[] | Upon return, contains an array of absolute powers measured at the positive modulation offset frequencies. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsresults-fetchswitchingpowertrace__string-double-ref-ref-ref.html language=enus -->
## TOPIC 00291: FetchSwitchingPowerTrace(string, double, ref float[], ref float[], ref float[])

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsresults-fetchswitchingpowertrace__string-double-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsresults-fetchswitchingpowertrace__string-double-ref-ref-ref.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the switching power trace and frequency offsets.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int FetchSwitchingPowerTrace(string selectorString, double timeout, ref float[] offsetFrequency, ref float[] absolutePower, ref float[] relativePower)ParametersNameTypeDescriptionselectorStr

### FetchSwitchingPowerTrace(string, double, ref float[], ref float[], ref float[])

Fetches the switching power trace and frequency offsets.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int FetchSwitchingPowerTrace(string selectorString, double timeout, ref float[] offsetFrequency, ref float[] absolutePower, ref float[] relativePower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| offsetFrequency | ref float[] | Upon return, contains an array of switching offset frequencies at which the measurement is performed in an ascending order. This value is expressed in Hz. |
| absolutePower | ref float[] | Upon return, contains an array of absolute powers corresponding to the switching offset frequency list. This value is expressed in dBm. |
| relativePower | ref float[] | Upon return, contains an array of relative powers corresponding to the switching offset frequencies. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsresults-fetchswitchingresultsarray__string-double-out-ref-ref-ref-ref.html language=enus -->
## TOPIC 00292: FetchSwitchingResultsArray(string, double, out double, ref double[], ref double[], ref double[], ref double[])

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsresults-fetchswitchingresultsarray__string-double-out-ref-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsresults-fetchswitchingresultsarray__string-double-out-ref-ref-ref-ref.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the switching carrier power, absolute powers, and relative powers measured at the switching offset frequencies. The relative powers are measured relative to the integrated switching power of the carrier.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int FetchSwitchingResultsArray(stri

### FetchSwitchingResultsArray(string, double, out double, ref double[], ref double[], ref double[], ref double[])

Fetches the switching carrier power, absolute powers, and relative powers measured at the switching offset frequencies. The relative powers are measured relative to the integrated switching power of the carrier.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int FetchSwitchingResultsArray(string selectorString, double timeout, out double switchingCarrierPower, ref double[] lowerRelativePower, ref double[] upperRelativePower, ref double[] lowerAbsolutePower, ref double[] upperAbsolutePower)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| switchingCarrierPower | out double | Upon return, contains the switching carrier power. This value is expressed in dBm. |
| lowerRelativePower | ref double[] | Upon return, contains an array of relative powers measured at the negative switching offset frequencies. This value is expressed in dB. The relative powers are measured relative to the integrated switching power of the carrier. |
| upperRelativePower | ref double[] | Upon return, contains an array of relative powers measured at the positive switching offset frequencies. This value is expressed in dB. The relative powers are measured relative to the integrated switching power of the carrier. |
| lowerAbsolutePower | ref double[] | Upon return, contains an array of absolute powers measured at the negative switching offset frequencies. This value is expressed in dBm. |
| upperAbsolutePower | ref double[] | Upon return, contains an array of absolute powers measured at the positive switching offset frequencies. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXOrfsResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsresults.html language=enus -->
## TOPIC 00293: RFmxGsmMXOrfsResults Class

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxorfsresults.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the ORFS measurement results. Derives fromRFmxGsmMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic class RFmxGsmMXOrfsResults : RFmxGsmMXSubObjectMethodsNameDescriptionFetchModulationPowerTrace(string, double, ref float[], ref float[], ref float[])Fe

### RFmxGsmMXOrfsResults Class

Provides methods to fetch and read the ORFS measurement results.

#### Derives from

- RFmxGsmMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public class RFmxGsmMXOrfsResults : RFmxGsmMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchModulationPowerTrace(string, double, ref float[], ref float[], ref float[]) | Fetches the modulation power trace and frequency offset. |
| FetchModulationResultsArray(string, double, out double, ref double[], ref double[], ref double[], ref double[]) | Returns the modulation carrier power, absolute powers, and relative powers measured at the modulation offset frequencies. The relative powers are measured relative to the integrated modulation power of the carrier. |
| FetchSwitchingPowerTrace(string, double, ref float[], ref float[], ref float[]) | Fetches the switching power trace and frequency offsets. |
| FetchSwitchingResultsArray(string, double, out double, ref double[], ref double[], ref double[], ref double[]) | Fetches the switching carrier power, absolute powers, and relative powers measured at the switching offset frequencies. The relative powers are measured relative to the integrated switching power of the carrier. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html language=enus -->
## TOPIC 00294: RFmxGsmMXPropertyId Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies all the attribute identifiers. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXPropertyIdMembersNameValueDescriptionAutoLevelInitialReferenceLevel4247552Specifies the initial reference level the AutoLevel(string, double, out double) function uses to estimate the peak po

### RFmxGsmMXPropertyId Enumeration

Specifies all the attribute identifiers.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXPropertyId

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AutoLevelInitialReferenceLevel | 4247552 | Specifies the initial reference level the AutoLevel(string, double, out double) function uses to estimate the peak power of the input signal. This value is expressed in dBm. |
| AutoTscDetectionEnabled | 4194323 | Specifies whether the measurement automatically detects the training sequence code (TSC). |
| Band | 4194318 | Specifies the operation band. |
| BurstSynchronizationType | 4194326 | Specifies the method used to synchronize the burst. |
| BurstType | 4194321 | Specifies the burst type. Use "slot(n)" as the selector string to configure or read this method. |
| CenterFrequency | 4194305 | Specifies the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency. |
| DigitalEdgeTriggerEdge | 4194310 | Specifies the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to DigitalEdge. |
| DigitalEdgeTriggerSource | 4194309 | Specifies the source terminal for the digital edge trigger. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to DigitalEdge. |
| ExternalAttenuation | 4194307 | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |
| HBFilterWidth | 4194322 | Specifies the filter width when you set the SetBurstType(string, RFmxGsmMXBurstType) method to HB. Use "slot(n)" as the selector string to configure or read this method. |
| IQPowerEdgeTriggerLevel | 4194312 | Specifies the power level at which the device triggers. This value is expressed in dB when you set the SetIQPowerEdgeTriggerLevelType(string, RFmxGsmMXIQPowerEdgeTriggerLevelType) method to Relative and in dBm when you set the IQ Power Edge Level Type method to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this method, taking into consideration the specified slope. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge. |
| IQPowerEdgeTriggerLevelType | 4198399 | Specifies the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge. |
| IQPowerEdgeTriggerSlope | 4194313 | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the SetIQPowerEdgeTriggerLevel(string, double) method with the slope you specify. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge. |
| IQPowerEdgeTriggerSource | 4194311 | Specifies the channel from which the device monitors the trigger. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge. |
| LinkDirection | 4194317 | Specifies the source of the signal to be measured. |
| ModAccAllTracesEnabled | 4198406 | Specifies whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement. |
| ModAccAveragingCount | 4198404 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxGsmMXModAccAveragingEnabled) method to True. |
| ModAccAveragingEnabled | 4198402 | Specifies whether to enable averaging for the modulation accuracy (ModAcc) measurement. |
| ModAccMeasurementInterval | 4198442 | Specifies whether the measurement is performed on a single specified timeslot or across multiple timeslots. |
| ModAccMeasurementOffset | 4198443 | Specifies the offset, relative to the trigger of the timeslot to be measured. |
| ModAccDroopCompensationEnabled | 4198405 | Specifies whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results. |
| ModAccMeasurementEnabled | 4198400 | Specifies whether to enable modulation accuracy (ModAcc) measurements on the acquired signal. |
| ModAccNumberOfAnalysisThreads | 4198407 | Specifies the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| ModAccResultsDetectedTsc | 4198433 | Returns the detected training sequence code (TSC) if you set the SetBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType) method to Tsc. Use "slot(n)" as the selector string to read this result. When the SetMeasurementInterval(string, RFmxGsmMXModAccMeasurementInterval) method is set to TimeslotAtOffset, Detected TSC array has one element and the Detected TSC is returned at index 0. |
| ModAccResultsEvm95thPercentileEvm | 4198412 | Returns the EVM value at which no more than 5% of the symbols have an EVM exceeding this value. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
| ModAccResultsEvmMaximumAmplitudeDroop | 4198421 | Returns the maximum of the amplitude droop values over all the measured time slots. This value is expressed in dB/symbol. The method returns this result for EDGE/EGPRS measurements. |
| ModAccResultsEvmMaximumFrequencyError | 4198419 | Returns the maximum of the frequency error values over all the measured time slots. This value is expressed in Hz. The method returns this result for EDGE/EGPRS measurements. |
| ModAccResultsEvmMaximumMagnitudeError | 4198415 | Returns the maximum of the RMS values of magnitude error over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
| ModAccResultsEvmMaximumPeakEvm | 4198411 | Returns the maximum of the peak EVM values over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
| ModAccResultsEvmMaximumPhaseError | 4198417 | Returns the maximum of the RMS values of phase error values over all the measured time slots. This value is expressed in degrees. The method returns this result for EDGE/EGPRS measurements. |
| ModAccResultsEvmMaximumRmsEvm | 4198409 | Returns the maximum of the RMS EVM values over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
| ModAccResultsEvmMeanAmplitudeDroop | 4198420 | Returns the mean of the amplitude droop values over all the measured time slots. This value is expressed in dB/symbol. The method returns this result for EDGE/EGPRS measurements. |
| ModAccResultsEvmMeanFrequencyError | 4198418 | Returns the mean of the frequency error values over all the measured time slots. This value is expressed in Hz. The method returns this result for EDGE/EGPRS measurements. |
| ModAccResultsEvmMeanMagnitudeError | 4198414 | Returns the mean of the RMS values of magnitude error over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
| ModAccResultsEvmMeanPeakEvm | 4198410 | Returns the mean of the peak EVM values over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
| ModAccResultsEvmMeanPhaseError | 4198416 | Returns the mean of the RMS values of phase error over all the measured time slots. This value is expressed in degrees. The method returns this result for EDGE/EGPRS measurements. |
| ModAccResultsEvmMeanRmsEvm | 4198408 | Returns the mean of the RMS EVM values over all the measured time slots. This value is expressed as a percentage. The method returns this result for EDGE/EGPRS measurements. |
| ModAccResultsEvmPeakEvmSymbol | 4198413 | Returns the symbol number in the useful portion of the burst corresponding to the EVM value returned by the GetEvmMaximumPeakEvm(string, out double) result. The method returns this result for EDGE/EGPRS measurements. |
| ModAccResultsMaximumIQGainImbalance | 4198430 | Returns the maximum of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. |
| ModAccResultsMaximumIQOriginOffset | 4198432 | Returns the maximum of the I/Q origin offset values over all the measured time slots. This value is expressed in dB. Presence of I/Q gain imbalance in the signal affects the I/Q origin offset measurement. The method returns this result for GSM/EDGE/EGPRS measurements. |
| ModAccResultsMeanIQGainImbalance | 4198429 | Returns the mean of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. |
| ModAccResultsMeanIQOriginOffset | 4198431 | Returns the mean of the I/Q origin offset values over all the measured time slots. This value is expressed in dB. Presence of I/Q gain imbalance in the signal affects the I/Q origin offset measurement. The method returns this result for GSM/EDGE/EGPRS measurements. |
| ModAccResultsPferMaximumFrequencyError | 4198428 | Returns the maximum of the frequency error values over all the measured time slots. This value is expressed in Hz. The method returns this result for GSM ModAcc measurements. |
| ModAccResultsPferMaximumPeakPhaseError | 4198425 | Returns the maximum of peak phase error over all the measured time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements. |
| ModAccResultsPferMaximumRmsPhaseError | 4198423 | Returns the maximum of the RMS phase error values over all the measured time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements. |
| ModAccResultsPferMeanFrequencyError | 4198427 | Returns the mean of the frequency error values over all the measured time slots. This value is expressed in Hz. The method returns this result for GSM ModAcc measurements. |
| ModAccResultsPferMeanPeakPhaseError | 4198424 | Returns the mean of peak phase error over all the measured time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements. |
| ModAccResultsPferMeanRmsPhaseError | 4198422 | Returns the mean of the RMS phase error values over all the measured time slots. This value is expressed in degrees. The method returns this result for GSM ModAcc measurements. |
| ModAccResultsPferPeakPhaseErrorSymbol | 4198426 | Returns the symbol number in the useful portion of the burst corresponding to the phase error value in the GetPferMaximumPeakPhaseError(string, out double) result. The method returns this result for GSM ModAcc measurements. |
| ModulationType | 4194320 | Specifies the modulation scheme used for the signal. Use "slot(n)" as the selector string to configure or read this method. |
| NumberOfTimeslots | 4194319 | Specifies the number of time slots to be measured. |
| OrfsAllTracesEnabled | 4202516 | Specifies whether to enable the traces to be stored and retrieved after performing the output radio frequency spectrum (ORFS) measurement. |
| OrfsAveragingCount | 4202500 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxGsmMXOrfsAveragingEnabled) method to True. |
| OrfsAveragingEnabled | 4202498 | Specifies whether to enable averaging for the output radio frequency spectrum (ORFS) measurement. |
| OrfsAveragingType | 4202499 | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the output radio frequency spectrum (ORFS) measurement. |
| OrfsMeasurementInterval | 4202533 | Specifies whether the measurement is performed on a single specified timeslot or across multiple timeslots. |
| OrfsMeasurementOffset | 4202534 | Specifies the offset, relative to the trigger of the timeslot to be measured. |
| OrfsEvaluationSymbolsIncludeTsc | 4202514 | Specifies whether to include the training sequence code (TSC) portion of the burst in the output radio frequency spectrum (ORFS) measurement. |
| OrfsEvaluationSymbolsStart | 4202513 | Specifies the start position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage. |
| OrfsEvaluationSymbolsStop | 4202515 | Specifies the stop position of the burst over which you perform the output radio frequency spectrum (ORFS) measurement. This value is expressed as a percentage. |
| OrfsMeasurementEnabled | 4202496 | Specifies whether to enable the output radio frequency spectrum (ORFS) measurement. |
| OrfsMeasurementType | 4202501 | Specifies the type of spectral distortion to be measured. |
| OrfsNoiseCompensationEnabled | 4202502 | Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Noise compensation is applicable only on modulation offsets and not on switching offsets. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832. |
| OrfsNumberOfAnalysisThreads | 4202517 | Specifies the maximum number of threads used for parallelism for the output radio frequency spectrum (ORFS) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| OrfsOffsetFrequencyMode | 4202503 | Specifies the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements. |
| PowerControlLevel | 4194325 | Specifies the power control level corresponding to the transmitted power, as defined in section 4.1 of the 3GPP TS 45.005 v8.0.0 specifications. Use "slot(n)" as the selector string to configure or read this method. |
| PvtAllTracesEnabled | 4206601 | Specifies whether to enable the traces to be stored and retrieved after performing the power versus time (PVT) measurement. |
| PvtAveragingCount | 4206597 | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxGsmMXPvtAveragingEnabled) method to True. |
| PvtRbwFilterBandwidth | 4206599 | Specifies the RBW Filter Bandwidth in Hz. RFMXGSM_VAL |
| PvtAveragingEnabled | 4206594 | Specifies whether to enable averaging for the power versus time (PVT) measurement. |
| PvtAveragingType | 4206596 | Specifies the averaging type for multiple acquisitions. |
| PvtMeasurementEnabled | 4206592 | Specifies whether to enable the power versus time (PVT) measurement. |
| PvtNumberOfAnalysisThreads | 4206602 | Specifies the maximum number of threads used for parallelism for the power versus time (PVT) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| PvtResultsMeasurementStatus | 4206603 | Indicates the overall measurement status based on standard-defined limits. |
| PvtResultsSlotAveragePower | 4206604 | Returns the mean power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. Use "slot(n)" as the selector string to read this method. |
| PvtResultsSlotBurstThreshold | 4206608 | Returns the threshold that the power versus time (PVT) measurement uses to determine the burst validity. This value is expressed in dBm. Use "slot(n)" as the selector string to read this method. |
| PvtResultsSlotBurstWidth | 4206605 | Returns the burst width for the slot where the -3 dB transition points occur. This value is expressed in seconds. Use "slot(n)" as the selector string to read this method. |
| PvtResultsSlotMaximumPower | 4206606 | Returns the maximum power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. Use "slot(n)" as the selector string to read this method. |
| PvtResultsSlotMinimumPower | 4206607 | Returns the minimum power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. Use "slot(n)" as the selector string to read this method. |
| PvtResultsSlotMeasurementStatus | 4206609 | Indicates the power versus time (PVT) measurement status for a particular slot. Use "slot(n)" as the selector string to read this method. |
| ReferenceLevel | 4194306 | Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
| ResultFetchTimeout | 4243456 | Specifies the time to wait before results are available. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx driver waits until the measurement is complete. |
| TriggerDelay | 4194314 | Specifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. |
| TriggerMinimumQuietTimeDuration | 4194316 | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the SetIQPowerEdgeTriggerSlope(string, RFmxGsmMXIQPowerEdgeTriggerSlope) method to Rising, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope method to Falling, the signal is quiet above the trigger level. |
| TriggerMinimumQuietTimeMode | 4194315 | Specifies whether the measurement computes the minimum quiet time used for triggering. |
| TriggerType | 4194308 | Specifies the trigger type. |
| Tsc | 4194324 | Specifies the training sequence code (TSC) to use. This method is applicable only when you set the SetBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType) method to Tsc and the SetAutoTscDetectionEnabled(string, RFmxGsmMXAutoTscDetectionEnabled) method to False. For access burst Tsc0, Tsc1, and Tsc2 are applicable. Use "slot(n)" as the selector string to configure or read this method. |
| SignalStructure | 4194327 | Specifies whether the signal is bursted or continuous. For bursted signal and continuous signals, set the SetTriggerType(string, RFmxGsmMXTriggerType) to IQPowerEdge and None, respectively. |
| OrfsModulationNumberOfOffsets | 4202525 | Specifies the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to modulation. |
| TimingAdvance | 4194328 | Specifies the timing advance value as specified in the 3GPP TS 45.010 specification for GSM access burst. |
| OrfsModulationOffsetFrequency | 4202526 | Specifies the value of positive frequency offset for which to measure the spectrum due to modulation measurement. This value is expressed in Hz. |
| OrfsModulationOffsetRbw | 4202527 | Specifies the resolution bandwidth used for ORFS due to modulation measurement. This value is expressed in Hz. |
| OrfsSwitchingNumberOfOffsets | 4202528 | Specifies the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to switching. |
| OrfsSwitchingOffsetFrequency | 4202529 | Specifies the value of positive frequency offset for which to measure the spectrum due to switching measurement. This value is expressed in Hz. |
| OrfsSwitchingOffsetRbw | 4202530 | Specifies the resolution bandwidth used for ORFS due to switching measurement. This value is expressed in Hz. |
| LimitedConfigurationChange | 4247555 | Specifies the set of properties that are considered by RFmx in the locked signal configuration state. |
| SelectedPorts | 4198397 | Specifies the instrument port to be configured to acquire a signal. Use RFmxInstrMX.GetAvailablePorts Method to get the valid port names. |
| ReferenceLevelHeadroom | 4198396 | Specifies the margin RFmx adds to the Reference Level method. |
| ModAccResultsEvmMeanPeakMagnitudeError | 4198435 | Returns the mean of peak magnitude error over all the measured time slots. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage. |
| ModAccResultsEvmMaximumPeakMagnitudeError | 4198436 | Returns the maximum of peak magnitude error over all the measured time slots. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage. |
| ModAccResultsEvm95thPercentileMagnitudeError | 4198437 | Returns the measured magnitude error value multiplied by 100, at which, no more than 5 percent of the symbols have magnitude error exceeding this value. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage. |
| ModAccResultsEvmMeanPeakPhaseError | 4198438 | Returns the mean of peak phase error over all the measured time slots. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees. |
| ModAccResultsEvmMaximumPeakPhaseError | 4198439 | Returns the maximum of peak phase error over all the measured time slots. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees. |
| ModAccResultsEvm95thPercentilePhaseError | 4198440 | Returns the measured phase error value multiplied by 100, at which, no more than 5 percent of the symbols have phase error exceeding this value. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees. |
| ModAccResultsPfer95thPercentilePhaseError | 4198441 | Returns the measured phase error value multiplied by 100, at which, no more than 5 percent of the symbols have phase error exceeding this value. This result is returned while performing ModAcc measurement on GSM. This value is measured in degrees. |
| OrfsModulationCarrierRbw | 4202507 |  |
| OrfsSwitchingCarrierRbw | 4202510 |  |
| OrfsEvaluationSymbolsScope | 4202532 |  |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvt-configuration.html language=enus -->
## TOPIC 00295: Configuration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvt-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvt-configuration.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxGsmMXPvtConfiguration instance that provides methods to configure the PVT measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic RFmxGsmMXPvtConfiguration Configuration { get; }

### Configuration

Gets the [RFmxGsmMXPvtConfiguration](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration.html) instance that provides methods to configure the PVT measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public [RFmxGsmMXPvtConfiguration](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration.html) Configuration { get; }

Parent topic:

RFmxGsmMXPvt Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvt-results.html language=enus -->
## TOPIC 00296: Results

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvt-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvt-results.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxGsmMXPvtResults instance that provides methods to fetch and read the PVT measurement results. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic RFmxGsmMXPvtResults Results { get; }

### Results

Gets the [RFmxGsmMXPvtResults](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults.html) instance that provides methods to fetch and read the PVT measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public [RFmxGsmMXPvtResults](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults.html) Results { get; }

Parent topic:

RFmxGsmMXPvt Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvt.html language=enus -->
## TOPIC 00297: RFmxGsmMXPvt Class

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvt.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvt.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the PVT measurement. Derives fromRFmxGsmMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic class RFmxGsmMXPvt : RFmxGsmMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxGsmMXPvtConfiguration instance that provides methods to configure the PVT measurement. Results

### RFmxGsmMXPvt Class

Represents the PVT measurement.

#### Derives from

- RFmxGsmMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public class RFmxGsmMXPvt : RFmxGsmMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxGsmMXPvtConfiguration instance that provides methods to configure the PVT measurement. |
| Results | Gets the RFmxGsmMXPvtResults instance that provides methods to fetch and read the PVT measurement results. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtaveragingenabled.html language=enus -->
## TOPIC 00298: RFmxGsmMXPvtAveragingEnabled Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtaveragingenabled.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the power versus time (PVT) measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXPvtAveragingEnabledMembersNameValueDescriptionFalse0The measurement is performed on a single acquisition. True1The measurement is averaged over multi

### RFmxGsmMXPvtAveragingEnabled Enumeration

Specifies whether to enable averaging for the power versus time (PVT) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXPvtAveragingEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement is performed on a single acquisition. |
| True | 1 | The measurement is averaged over multiple acquisitions. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtaveragingtype.html language=enus -->
## TOPIC 00299: RFmxGsmMXPvtAveragingType Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtaveragingtype.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for multiple acquisitions. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXPvtAveragingTypeMembersNameValueDescriptionRms0The power at each sample interval is linearly averaged from one acquisition to the next acquisition. Log1The power at each sample

### RFmxGsmMXPvtAveragingType Enumeration

Specifies the averaging type for multiple acquisitions.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXPvtAveragingType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rms | 0 | The power at each sample interval is linearly averaged from one acquisition to the next acquisition. |
| Log | 1 | The power at each sample interval is averaged on a logarithmic scale from one acquisition to the next acquisition. |
| Maximum | 3 | The peak power at each sample interval is retained from one acquisition to the next acquisition. |
| Minimum | 4 | The lowest power at each sample interval is retained from one acquisition to the next acquisition. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-configureaveraging__string-rfmxgsmmxpvtaveragingenabled-int-rfmxgsmmxpvtaveragingtype.html language=enus -->
## TOPIC 00300: ConfigureAveraging(string, RFmxGsmMXPvtAveragingEnabled, int, RFmxGsmMXPvtAveragingType)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-configureaveraging__string-rfmxgsmmxpvtaveragingenabled-int-rfmxgsmmxpvtaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-configureaveraging__string-rfmxgsmmxpvtaveragingenabled-int-rfmxgsmmxpvtaveragingtype.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the power versus time (PVT) measurement.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int ConfigureAveraging(string selectorString, RFmxGsmMXPvtAveragingEnabled averagingEnabled, int averagingCount, RFmxGsmMXPvtAveragingType averagingType)ParametersNameTypeDescriptio

### ConfigureAveraging(string, RFmxGsmMXPvtAveragingEnabled, int, RFmxGsmMXPvtAveragingType)

Configures averaging for the power versus time (PVT) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int ConfigureAveraging(string selectorString, RFmxGsmMXPvtAveragingEnabled averagingEnabled, int averagingCount, RFmxGsmMXPvtAveragingType averagingType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| averagingEnabled | RFmxGsmMXPvtAveragingEnabled | Specifies whether to enable averaging for the measurement. |
| averagingCount | int | Specifies the number of acquisitions used for averaging when you set the averagingEnabled parameter to True. |
| averagingType | RFmxGsmMXPvtAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXPvtConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-getalltracesenabled__string-out.html language=enus -->
## TOPIC 00301: GetAllTracesEnabled(string, out bool)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-getalltracesenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-getalltracesenabled__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the traces to be stored and retrieved after performing the power versus time (PVT) measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetAllTracesEnabled(string selectorString, out bool value)RemarksThis method gets the value of PvtAllTracesEnabled attribut

### GetAllTracesEnabled(string, out bool)

Gets whether to enable the traces to be stored and retrieved after performing the power versus time (PVT) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetAllTracesEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [PvtAllTracesEnabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is False.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the traces to be stored and retrieved after performing the power versus time (PVT) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXPvtConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-getaveragingcount__string-out.html language=enus -->
## TOPIC 00302: GetAveragingCount(string, out int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-getaveragingcount__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-getaveragingcount__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxGsmMXPvtAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetAveragingCount(string selectorString, out int value)RemarksThis method gets the value of PvtAvera

### GetAveragingCount(string, out int)

Gets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxGsmMXPvtAveragingEnabled)](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-setaveragingenabled__string-rfmxgsmmxpvtaveragingenabled.html) method to [True](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetAveragingCount(string selectorString, out int value)

#### Remarks

This method gets the value of [PvtAveragingCount](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxGsmMXPvtAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXPvtConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-getaveragingenabled__string-out.html language=enus -->
## TOPIC 00303: GetAveragingEnabled(string, out RFmxGsmMXPvtAveragingEnabled)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-getaveragingenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-getaveragingenabled__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable averaging for the power versus time (PVT) measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetAveragingEnabled(string selectorString, out RFmxGsmMXPvtAveragingEnabled value)RemarksThis method gets the value of PvtAveragingEnabled attribute.The default val

### GetAveragingEnabled(string, out RFmxGsmMXPvtAveragingEnabled)

Gets whether to enable averaging for the power versus time (PVT) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetAveragingEnabled(string selectorString, out RFmxGsmMXPvtAveragingEnabled value)

#### Remarks

This method gets the value of [PvtAveragingEnabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxGsmMXPvtAveragingEnabled | Upon return, contains whether to enable averaging for the power versus time (PVT) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXPvtConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-getaveragingtype__string-out.html language=enus -->
## TOPIC 00304: GetAveragingType(string, out RFmxGsmMXPvtAveragingType)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-getaveragingtype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-getaveragingtype__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the averaging type for multiple acquisitions. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetAveragingType(string selectorString, out RFmxGsmMXPvtAveragingType value)RemarksThis method gets the value of PvtAveragingType attribute.The default value is Rms.ParametersNameTypeDescript

### GetAveragingType(string, out RFmxGsmMXPvtAveragingType)

Gets the averaging type for multiple acquisitions.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetAveragingType(string selectorString, out RFmxGsmMXPvtAveragingType value)

#### Remarks

This method gets the value of [PvtAveragingType](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Rms](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtaveragingtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxGsmMXPvtAveragingType | Upon return, contains the averaging type for multiple acquisitions. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXPvtConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00305: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the power versus time (PVT) measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method gets the value of PvtMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDesc

### GetMeasurementEnabled(string, out bool)

Gets whether to enable the power versus time (PVT) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [PvtMeasurementEnabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the power versus time (PVT) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXPvtConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-getnumberofanalysisthreads__string-out.html language=enus -->
## TOPIC 00306: GetNumberOfAnalysisThreads(string, out int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-getnumberofanalysisthreads__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-getnumberofanalysisthreads__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum number of threads used for parallelism for the power versus time (PVT) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, s

### GetNumberOfAnalysisThreads(string, out int)

Gets the maximum number of threads used for parallelism for the power versus time (PVT) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetNumberOfAnalysisThreads(string selectorString, out int value)

#### Remarks

This method gets the value of [PvtNumberOfAnalysisThreads](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the maximum number of threads used for parallelism for the power versus time (PVT) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXPvtConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-getrbwfilterbandwidth__string-out.html language=enus -->
## TOPIC 00307: GetRbwFilterBandwidth(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-getrbwfilterbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-getrbwfilterbandwidth__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RBW Filter Bandwidth in Hz. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetRbwFilterBandwidth(string selectorString, out double value)RemarksRFMXGSM_VALThis method gets the value of PvtRbwFilterBandwidth attribute.The default value is 500 kHzParametersNameTypeDescriptionselect

### GetRbwFilterBandwidth(string, out double)

Gets the RBW Filter Bandwidth in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetRbwFilterBandwidth(string selectorString, out double value)

#### Remarks

RFMXGSM_VAL

This method gets the value of [PvtRbwFilterBandwidth](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 500 kHz

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the RBW Filter Bandwidth in Hz |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXPvtConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-setalltracesenabled__string-bool.html language=enus -->
## TOPIC 00308: SetAllTracesEnabled(string, bool)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-setalltracesenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-setalltracesenabled__string-bool.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the traces to be stored and retrieved after performing the power versus time (PVT) measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetAllTracesEnabled(string selectorString, bool value)RemarksThis method sets the value of PvtAllTracesEnabled attribute.Th

### SetAllTracesEnabled(string, bool)

Sets whether to enable the traces to be stored and retrieved after performing the power versus time (PVT) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetAllTracesEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [PvtAllTracesEnabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is False.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the traces to be stored and retrieved after performing the power versus time (PVT) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXPvtConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-setaveragingcount__string-int.html language=enus -->
## TOPIC 00309: SetAveragingCount(string, int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-setaveragingcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-setaveragingcount__string-int.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxGsmMXPvtAveragingEnabled) method to True. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetAveragingCount(string selectorString, int value)RemarksThis method sets the value of PvtAveraging

### SetAveragingCount(string, int)

Sets the number of acquisitions used for averaging when you set the [SetAveragingEnabled(string, RFmxGsmMXPvtAveragingEnabled)](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-setaveragingenabled__string-rfmxgsmmxpvtaveragingenabled.html) method to [True](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetAveragingCount(string selectorString, int value)

#### Remarks

This method sets the value of [PvtAveragingCount](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxGsmMXPvtAveragingEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXPvtConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-setaveragingenabled__string-rfmxgsmmxpvtaveragingenabled.html language=enus -->
## TOPIC 00310: SetAveragingEnabled(string, RFmxGsmMXPvtAveragingEnabled)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-setaveragingenabled__string-rfmxgsmmxpvtaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-setaveragingenabled__string-rfmxgsmmxpvtaveragingenabled.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable averaging for the power versus time (PVT) measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetAveragingEnabled(string selectorString, RFmxGsmMXPvtAveragingEnabled value)RemarksThis method sets the value of PvtAveragingEnabled attribute.The default value i

### SetAveragingEnabled(string, RFmxGsmMXPvtAveragingEnabled)

Sets whether to enable averaging for the power versus time (PVT) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetAveragingEnabled(string selectorString, RFmxGsmMXPvtAveragingEnabled value)

#### Remarks

This method sets the value of [PvtAveragingEnabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtaveragingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxGsmMXPvtAveragingEnabled | Specifies whether to enable averaging for the power versus time (PVT) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXPvtConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-setaveragingtype__string-rfmxgsmmxpvtaveragingtype.html language=enus -->
## TOPIC 00311: SetAveragingType(string, RFmxGsmMXPvtAveragingType)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-setaveragingtype__string-rfmxgsmmxpvtaveragingtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-setaveragingtype__string-rfmxgsmmxpvtaveragingtype.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the averaging type for multiple acquisitions. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetAveragingType(string selectorString, RFmxGsmMXPvtAveragingType value)RemarksThis method sets the value of PvtAveragingType attribute.The default value is Rms.ParametersNameTypeDescriptions

### SetAveragingType(string, RFmxGsmMXPvtAveragingType)

Sets the averaging type for multiple acquisitions.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetAveragingType(string selectorString, RFmxGsmMXPvtAveragingType value)

#### Remarks

This method sets the value of [PvtAveragingType](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is [Rms](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtaveragingtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxGsmMXPvtAveragingType | Specifies the averaging type for multiple acquisitions. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXPvtConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00312: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the power versus time (PVT) measurement. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method sets the value of PvtMeasurementEnabled attribute.The default value is FALSE.ParametersNameTypeDescript

### SetMeasurementEnabled(string, bool)

Sets whether to enable the power versus time (PVT) measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [PvtMeasurementEnabled](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is FALSE.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the power versus time (PVT) measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXPvtConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-setnumberofanalysisthreads__string-int.html language=enus -->
## TOPIC 00313: SetNumberOfAnalysisThreads(string, int)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-setnumberofanalysisthreads__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-setnumberofanalysisthreads__string-int.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the maximum number of threads used for parallelism for the power versus time (PVT) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, s

### SetNumberOfAnalysisThreads(string, int)

Sets the maximum number of threads used for parallelism for the power versus time (PVT) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetNumberOfAnalysisThreads(string selectorString, int value)

#### Remarks

This method sets the value of [PvtNumberOfAnalysisThreads](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the maximum number of threads used for parallelism for the power versus time (PVT) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXPvtConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-setrbwfilterbandwidth__string-double.html language=enus -->
## TOPIC 00314: SetRbwFilterBandwidth(string, double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-setrbwfilterbandwidth__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration-setrbwfilterbandwidth__string-double.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the RBW Filter Bandwidth in Hz. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int SetRbwFilterBandwidth(string selectorString, double value)RemarksRFMXGSM_VALThis method sets the value of PvtRbwFilterBandwidth attribute.The default value is 500 kHzParametersNameTypeDescriptionselectorSt

### SetRbwFilterBandwidth(string, double)

Sets the RBW Filter Bandwidth in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int SetRbwFilterBandwidth(string selectorString, double value)

#### Remarks

RFMXGSM_VAL

This method sets the value of [PvtRbwFilterBandwidth](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.The default value is 500 kHz

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the RBW Filter Bandwidth in Hz |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXPvtConfiguration Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration.html language=enus -->
## TOPIC 00315: RFmxGsmMXPvtConfiguration Class

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtconfiguration.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the PVT measurement. Derives fromRFmxGsmMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic class RFmxGsmMXPvtConfiguration : RFmxGsmMXSubObjectMethodsNameDescriptionConfigureAveraging(string, RFmxGsmMXPvtAveragingEnabled, int, RFmxGsmMXPvtAveragingType)Con

### RFmxGsmMXPvtConfiguration Class

Provides methods to configure the PVT measurement.

#### Derives from

- RFmxGsmMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public class RFmxGsmMXPvtConfiguration : RFmxGsmMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| ConfigureAveraging(string, RFmxGsmMXPvtAveragingEnabled, int, RFmxGsmMXPvtAveragingType) | Configures averaging for the power versus time (PVT) measurement. |
| GetAllTracesEnabled(string, out bool) | Gets whether to enable the traces to be stored and retrieved after performing the power versus time (PVT) measurement. |
| GetAveragingCount(string, out int) | Gets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxGsmMXPvtAveragingEnabled) method to True. |
| GetAveragingEnabled(string, out RFmxGsmMXPvtAveragingEnabled) | Gets whether to enable averaging for the power versus time (PVT) measurement. |
| GetAveragingType(string, out RFmxGsmMXPvtAveragingType) | Gets the averaging type for multiple acquisitions. |
| GetMeasurementEnabled(string, out bool) | Gets whether to enable the power versus time (PVT) measurement. |
| GetNumberOfAnalysisThreads(string, out int) | Gets the maximum number of threads used for parallelism for the power versus time (PVT) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| GetRbwFilterBandwidth(string, out double) | Gets the RBW Filter Bandwidth in Hz. |
| SetAllTracesEnabled(string, bool) | Sets whether to enable the traces to be stored and retrieved after performing the power versus time (PVT) measurement. |
| SetAveragingCount(string, int) | Sets the number of acquisitions used for averaging when you set the SetAveragingEnabled(string, RFmxGsmMXPvtAveragingEnabled) method to True. |
| SetAveragingEnabled(string, RFmxGsmMXPvtAveragingEnabled) | Sets whether to enable averaging for the power versus time (PVT) measurement. |
| SetAveragingType(string, RFmxGsmMXPvtAveragingType) | Sets the averaging type for multiple acquisitions. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable the power versus time (PVT) measurement. |
| SetNumberOfAnalysisThreads(string, int) | Sets the maximum number of threads used for parallelism for the power versus time (PVT) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. |
| SetRbwFilterBandwidth(string, double) | Sets the RBW Filter Bandwidth in Hz. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtmeasurementstatus.html language=enus -->
## TOPIC 00316: RFmxGsmMXPvtMeasurementStatus Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtmeasurementstatus.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtmeasurementstatus.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the overall measurement status based on standard-defined limits. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXPvtMeasurementStatusMembersNameValueDescriptionFail0The measurement failed because the average power of at least one slot is outside the standard-defined lim

### RFmxGsmMXPvtMeasurementStatus Enumeration

Indicates the overall measurement status based on standard-defined limits.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXPvtMeasurementStatus

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Fail | 0 | The measurement failed because the average power of at least one slot is outside the standard-defined limits. |
| Pass | 1 | The measurement passed because the average power of all slots is within the standard-defined limits. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-fetchmeasurementstatus__string-double-out.html language=enus -->
## TOPIC 00317: FetchMeasurementStatus(string, double, out RFmxGsmMXPvtMeasurementStatus)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-fetchmeasurementstatus__string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-fetchmeasurementstatus__string-double-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the overall PVT measurement status based on the standard defined measurement limits.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int FetchMeasurementStatus(string selectorString, double timeout, out RFmxGsmMXPvtMeasurementStatus measurementStatus)ParametersNameTypeDescriptionselecto

### FetchMeasurementStatus(string, double, out RFmxGsmMXPvtMeasurementStatus)

Fetches the overall PVT measurement status based on the standard defined measurement limits.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int FetchMeasurementStatus(string selectorString, double timeout, out RFmxGsmMXPvtMeasurementStatus measurementStatus)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| measurementStatus | out RFmxGsmMXPvtMeasurementStatus | Indicates the overall measurement status based on standard-defined limits. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXPvtResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-fetchpowertrace__string-double-ref-ref-ref.html language=enus -->
## TOPIC 00318: FetchPowerTrace(string, double, ref AnalogWaveform< float >, ref AnalogWaveform< float >, ref AnalogWaveform< float >)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-fetchpowertrace__string-double-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-fetchpowertrace__string-double-ref-ref-ref.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the upper mask, signal power, and lower mask trace.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int FetchPowerTrace(string selectorString, double timeout, ref AnalogWaveform< float > upperMask, ref AnalogWaveform< float > signalPower, ref AnalogWaveform< float > lowerMask)Parameters

### FetchPowerTrace(string, double, ref AnalogWaveform< float >, ref AnalogWaveform< float >, ref AnalogWaveform< float >)

Fetches the upper mask, signal power, and lower mask trace.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int FetchPowerTrace(string selectorString, double timeout, ref AnalogWaveform< float > upperMask, ref AnalogWaveform< float > signalPower, ref AnalogWaveform< float > lowerMask)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| upperMask | ref AnalogWaveform< float > | Upon return, contains the upper mask trace, in dB. |
| signalPower | ref AnalogWaveform< float > | Upon return, contains the signal power trace. This value is expressed in dBm. |
| lowerMask | ref AnalogWaveform< float > | Upon return, contains the lower mask trace. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXPvtResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-fetchslotmeasurement__string-double-out-out-out-out-out-out.html language=enus -->
## TOPIC 00319: FetchSlotMeasurement(string, double, out double, out double, out RFmxGsmMXPvtSlotMeasurementStatus, out double, out double, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-fetchslotmeasurement__string-double-out-out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-fetchslotmeasurement__string-double-out-out-out-out-out-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the measurement results for a single-slot PVT measurement. Use "slot(n)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int FetchSlotMeasurement(string selectorString, double timeout, out double slotAveragePower, out double slotB

### FetchSlotMeasurement(string, double, out double, out double, out RFmxGsmMXPvtSlotMeasurementStatus, out double, out double, out double)

Fetches the measurement results for a single-slot PVT measurement. 
 Use "slot(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int FetchSlotMeasurement(string selectorString, double timeout, out double slotAveragePower, out double slotBurstWidth, out RFmxGsmMXPvtSlotMeasurementStatus slotMeasurementStatus, out double slotMaximumPower, out double slotMinimumPower, out double slotBurstThreshold)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and slot number. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "slot0" "result::r1/slot0" You can use the BuildSlotString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| slotAveragePower | out double | Upon return, contains the mean power of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. |
| slotBurstWidth | out double | Upon return, contains the burst width of the slot where the -3 dB transition points occur. This value is expressed in seconds. |
| slotMeasurementStatus | out RFmxGsmMXPvtSlotMeasurementStatus | Indicates the PVT measurement status for a particular slot. |
| slotMaximumPower | out double | Upon return, contains the maximum power of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. |
| slotMinimumPower | out double | Upon return, contains the minimum power of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. |
| slotBurstThreshold | out double | Upon return, contains the threshold that the PVT measurement uses to determine the burst validity. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXPvtResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-fetchslotmeasurementarray__string-double-ref-ref-ref-ref-ref-ref.html language=enus -->
## TOPIC 00320: FetchSlotMeasurementArray(string, double, ref double[], ref double[], ref RFmxGsmMXPvtSlotMeasurementStatus[], ref double[], ref double[], ref double[])

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-fetchslotmeasurementarray__string-double-ref-ref-ref-ref-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-fetchslotmeasurementarray__string-double-ref-ref-ref-ref-ref-ref.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PVT measurement results for each slot.SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int FetchSlotMeasurementArray(string selectorString, double timeout, ref double[] slotAveragePower, ref double[] slotBurstWidth, ref RFmxGsmMXPvtSlotMeasurementStatus[] slotMeasurementStatus, ref

### FetchSlotMeasurementArray(string, double, ref double[], ref double[], ref RFmxGsmMXPvtSlotMeasurementStatus[], ref double[], ref double[], ref double[])

Fetches the PVT measurement results for each slot.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int FetchSlotMeasurementArray(string selectorString, double timeout, ref double[] slotAveragePower, ref double[] slotBurstWidth, ref RFmxGsmMXPvtSlotMeasurementStatus[] slotMeasurementStatus, ref double[] slotMaximumPower, ref double[] slotMinimumPower, ref double[] slotBurstThreshold)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "" "result::r1" You can use the BuildResultString(string) method to build the selector string. |
| timeout | double | Specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the method waits until the measurement is complete. |
| slotAveragePower | ref double[] | Upon return, contains an array of mean powers of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. |
| slotBurstWidth | ref double[] | Upon return, contains an array of burst widths for the slots where the -3 dB transition points occur. This value is expressed in seconds. |
| slotMeasurementStatus | ref RFmxGsmMXPvtSlotMeasurementStatus[] | Indicates an array of PVT measurement statuses for multiple slots. |
| slotMaximumPower | ref double[] | Upon return, contains an array of maximum powers of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. |
| slotMinimumPower | ref double[] | Upon return, contains an array of minimum powers of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. |
| slotBurstThreshold | ref double[] | Upon return, contains an array of thresholds that the PVT measurement uses to determine the burst validity. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXPvtResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-getmeasurementstatus__string-out.html language=enus -->
## TOPIC 00321: GetMeasurementStatus(string, out RFmxGsmMXPvtMeasurementStatus)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-getmeasurementstatus__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-getmeasurementstatus__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the overall measurement status based on standard-defined limits. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetMeasurementStatus(string selectorString, out RFmxGsmMXPvtMeasurementStatus value)RemarksThis method gets the value of PvtResultsMeasurementStatus attribute.Paramete

### GetMeasurementStatus(string, out RFmxGsmMXPvtMeasurementStatus)

Indicates the overall measurement status based on standard-defined limits.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetMeasurementStatus(string selectorString, out RFmxGsmMXPvtMeasurementStatus value)

#### Remarks

This method gets the value of [PvtResultsMeasurementStatus](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name.Example: "" "result::r1" You can use the BuildResultString(string) method to build the selectorString. |
| value | out RFmxGsmMXPvtMeasurementStatus | Indicates the overall measurement status based on standard-defined limits. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXPvtResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-getslotaveragepower__string-out.html language=enus -->
## TOPIC 00322: GetSlotAveragePower(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-getslotaveragepower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-getslotaveragepower__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mean power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. Use "slot(n)" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetSlotAveragePower(string selectorString, out double valu

### GetSlotAveragePower(string, out double)

Gets the mean power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. Use "slot(n)" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetSlotAveragePower(string selectorString, out double value)

#### Remarks

This method gets the value of [PvtResultsSlotAveragePower](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Slot number. Example: "Slot0", "result::r1/Slot0". You can use the BuildSlotString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the mean power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. Use "slot(n)" as the selector string to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXPvtResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-getslotburstthreshold__string-out.html language=enus -->
## TOPIC 00323: GetSlotBurstThreshold(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-getslotburstthreshold__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-getslotburstthreshold__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the threshold that the power versus time (PVT) measurement uses to determine the burst validity. This value is expressed in dBm. Use "slot(n)" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetSlotBurstThreshold(string selectorString, out d

### GetSlotBurstThreshold(string, out double)

Gets the threshold that the power versus time (PVT) measurement uses to determine the burst validity. This value is expressed in dBm. Use "slot(n)" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetSlotBurstThreshold(string selectorString, out double value)

#### Remarks

This method gets the value of [PvtResultsSlotBurstThreshold](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Slot number. Example: "Slot0", "result::r1/Slot0". You can use the BuildSlotString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the threshold that the power versus time (PVT) measurement uses to determine the burst validity. This value is expressed in dBm. Use "slot(n)" as the selector string to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXPvtResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-getslotburstwidth__string-out.html language=enus -->
## TOPIC 00324: GetSlotBurstWidth(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-getslotburstwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-getslotburstwidth__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the burst width for the slot where the -3 dB transition points occur. This value is expressed in seconds. Use "slot(n)" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetSlotBurstWidth(string selectorString, out double value)RemarksThis met

### GetSlotBurstWidth(string, out double)

Gets the burst width for the slot where the -3 dB transition points occur. This value is expressed in seconds. Use "slot(n)" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetSlotBurstWidth(string selectorString, out double value)

#### Remarks

This method gets the value of [PvtResultsSlotBurstWidth](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Slot number. Example: "Slot0", "result::r1/Slot0". You can use the BuildSlotString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the burst width for the slot where the -3 dB transition points occur. This value is expressed in seconds. Use "slot(n)" as the selector string to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXPvtResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-getslotmaximumpower__string-out.html language=enus -->
## TOPIC 00325: GetSlotMaximumPower(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-getslotmaximumpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-getslotmaximumpower__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. Use "slot(n)" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetSlotMaximumPower(string selectorString, out double v

### GetSlotMaximumPower(string, out double)

Gets the maximum power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. Use "slot(n)" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetSlotMaximumPower(string selectorString, out double value)

#### Remarks

This method gets the value of [PvtResultsSlotMaximumPower](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Slot number. Example: "Slot0", "result::r1/Slot0". You can use the BuildSlotString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the maximum power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. Use "slot(n)" as the selector string to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXPvtResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-getslotmeasurementstatus__string-out.html language=enus -->
## TOPIC 00326: GetSlotMeasurementStatus(string, out RFmxGsmMXPvtSlotMeasurementStatus)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-getslotmeasurementstatus__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-getslotmeasurementstatus__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the power versus time (PVT) measurement status for a particular slot. Use "slot(n)" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetSlotMeasurementStatus(string selectorString, out RFmxGsmMXPvtSlotMeasurementStatus value)RemarksThis

### GetSlotMeasurementStatus(string, out RFmxGsmMXPvtSlotMeasurementStatus)

Indicates the power versus time (PVT) measurement status for a particular slot. Use "slot(n)" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetSlotMeasurementStatus(string selectorString, out RFmxGsmMXPvtSlotMeasurementStatus value)

#### Remarks

This method gets the value of [PvtResultsSlotMeasurementStatus](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Slot number. Example: "Slot0", "result::r1/Slot0". You can use the BuildSlotString(string, int) method to build the selector string. |
| value | out RFmxGsmMXPvtSlotMeasurementStatus | Indicates the power versus time (PVT) measurement status for a particular slot. Use "slot(n)" as the selector string to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXPvtResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-getslotminimumpower__string-out.html language=enus -->
## TOPIC 00327: GetSlotMinimumPower(string, out double)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-getslotminimumpower__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults-getslotminimumpower__string-out.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minimum power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. Use "slot(n)" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic int GetSlotMinimumPower(string selectorString, out double v

### GetSlotMinimumPower(string, out double)

Gets the minimum power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. Use "slot(n)" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public int GetSlotMinimumPower(string selectorString, out double value)

#### Remarks

This method gets the value of [PvtResultsSlotMinimumPower](nationalinstruments-rfmx-gsmmx-rfmxgsmmxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the result name and Slot number. Example: "Slot0", "result::r1/Slot0". You can use the BuildSlotString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the minimum power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. Use "slot(n)" as the selector string to read this method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxGsmMXPvtResults Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults.html language=enus -->
## TOPIC 00328: RFmxGsmMXPvtResults Class

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtresults.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the PVT measurement results. Derives fromRFmxGsmMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic class RFmxGsmMXPvtResults : RFmxGsmMXSubObjectMethodsNameDescriptionFetchMeasurementStatus(string, double, out RFmxGsmMXPvtMeasurementStatus)Fetches the

### RFmxGsmMXPvtResults Class

Provides methods to fetch and read the PVT measurement results.

#### Derives from

- RFmxGsmMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public class RFmxGsmMXPvtResults : RFmxGsmMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchMeasurementStatus(string, double, out RFmxGsmMXPvtMeasurementStatus) | Fetches the overall PVT measurement status based on the standard defined measurement limits. |
| FetchPowerTrace(string, double, ref AnalogWaveform< float >, ref AnalogWaveform< float >, ref AnalogWaveform< float >) | Fetches the upper mask, signal power, and lower mask trace. |
| FetchSlotMeasurement(string, double, out double, out double, out RFmxGsmMXPvtSlotMeasurementStatus, out double, out double, out double) | Fetches the measurement results for a single-slot PVT measurement. Use "slot(n)" as the selector string to read results from this method. |
| FetchSlotMeasurementArray(string, double, ref double[], ref double[], ref RFmxGsmMXPvtSlotMeasurementStatus[], ref double[], ref double[], ref double[]) | Fetches the PVT measurement results for each slot. |
| GetMeasurementStatus(string, out RFmxGsmMXPvtMeasurementStatus) | Indicates the overall measurement status based on standard-defined limits. |
| GetSlotAveragePower(string, out double) | Gets the mean power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. Use "slot(n)" as the selector string to read this method. |
| GetSlotBurstThreshold(string, out double) | Gets the threshold that the power versus time (PVT) measurement uses to determine the burst validity. This value is expressed in dBm. Use "slot(n)" as the selector string to read this method. |
| GetSlotBurstWidth(string, out double) | Gets the burst width for the slot where the -3 dB transition points occur. This value is expressed in seconds. Use "slot(n)" as the selector string to read this method. |
| GetSlotMaximumPower(string, out double) | Gets the maximum power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. Use "slot(n)" as the selector string to read this method. |
| GetSlotMeasurementStatus(string, out RFmxGsmMXPvtSlotMeasurementStatus) | Indicates the power versus time (PVT) measurement status for a particular slot. Use "slot(n)" as the selector string to read this method. |
| GetSlotMinimumPower(string, out double) | Gets the minimum power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. Use "slot(n)" as the selector string to read this method. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtslotmeasurementstatus.html language=enus -->
## TOPIC 00329: RFmxGsmMXPvtSlotMeasurementStatus Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtslotmeasurementstatus.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxpvtslotmeasurementstatus.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the power versus time (PVT) measurement status for a particular slot. Use "slot(n)" as the selector string to read this method. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXPvtSlotMeasurementStatusMembersNameValueDescriptionFail0The average power for at least one slo

### RFmxGsmMXPvtSlotMeasurementStatus Enumeration

Indicates the power versus time (PVT) measurement status for a particular slot. Use "slot(n)" as the selector string to read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXPvtSlotMeasurementStatus

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Fail | 0 | The average power for at least one slot is outside the standard-defined limits. |
| Pass | 1 | The average power for each slot is within the standard-defined limits. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxsignalstructure.html language=enus -->
## TOPIC 00330: RFmxGsmMXSignalStructure Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxsignalstructure.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxsignalstructure.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the signal is bursted or continuous. For bursted signal and continuous signals, set the SetTriggerType(string, RFmxGsmMXTriggerType) to IQPowerEdge and None, respectively. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXSignalStructureMembersNameValueDescription

### RFmxGsmMXSignalStructure Enumeration

Specifies whether the signal is bursted or continuous. For bursted signal and continuous signals, set the [SetTriggerType(string, RFmxGsmMXTriggerType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-settriggertype__string-rfmxgsmmxtriggertype.html) to [IQPowerEdge](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggertype.html) and [None](nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggertype.html), respectively.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXSignalStructure

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Bursted | 0 | The signal is bursted. |
| Continuous | 1 | The signal is continuous. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxsubobject.html language=enus -->
## TOPIC 00331: RFmxGsmMXSubObject Class

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxsubobject.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxsubobject.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents members that are common to all sub-object of RFmxGsmMX classes. Derives fromNoneSyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic class RFmxGsmMXSubObjectThread SafetyAny public static members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

### RFmxGsmMXSubObject Class

Represents members that are common to all sub-object of RFmxGsmMX classes.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public class RFmxGsmMXSubObject

#### Thread Safety

Any public static members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggerminimumquiettimemode.html language=enus -->
## TOPIC 00332: RFmxGsmMXTriggerMinimumQuietTimeMode Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggerminimumquiettimemode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggerminimumquiettimemode.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the minimum quiet time used for triggering. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXTriggerMinimumQuietTimeModeMembersNameValueDescriptionManual0The minimum quiet time for triggering is the value of the SetTriggerMinimumQuietTime

### RFmxGsmMXTriggerMinimumQuietTimeMode Enumeration

Specifies whether the measurement computes the minimum quiet time used for triggering.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXTriggerMinimumQuietTimeMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Manual | 0 | The minimum quiet time for triggering is the value of the SetTriggerMinimumQuietTimeDuration(string, double) method. |
| Auto | 1 | The measurement computes the minimum quiet time used for triggering. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggertype.html language=enus -->
## TOPIC 00333: RFmxGsmMXTriggerType Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxtriggertype.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger type. SyntaxNamespace: NationalInstruments.RFmx.GsmMXpublic enum RFmxGsmMXTriggerTypeMembersNameValueDescriptionNone0No Reference Trigger is configured. DigitalEdge1The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specifi

### RFmxGsmMXTriggerType Enumeration

Specifies the trigger type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXTriggerType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0 | No Reference Trigger is configured. |
| DigitalEdge | 1 | The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the SetDigitalEdgeTriggerSource(string, string) method. |
| IQPowerEdge | 2 | The Reference Trigger is asserted when the signal changes past the level specified by the slope (rising or falling), which is configured using the SetIQPowerEdgeTriggerSlope(string, RFmxGsmMXIQPowerEdgeTriggerSlope) method. |
| Software | 3 | The Reference Trigger is not asserted until a software trigger occurs. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx-rfmxgsmmxtsc.html language=enus -->
## TOPIC 00334: RFmxGsmMXTsc Enumeration

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx-rfmxgsmmxtsc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx-rfmxgsmmxtsc.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the training sequence code (TSC) to use. This method is applicable only when you set the SetBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType) method to Tsc and the SetAutoTscDetectionEnabled(string, RFmxGsmMXAutoTscDetectionEnabled) method to False. For access burst Tsc0,

### RFmxGsmMXTsc Enumeration

Specifies the training sequence code (TSC) to use. This method is applicable only when you set the [SetBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setburstsynchronizationtype__string-rfmxgsmmxburstsynchronizationtype.html) method to [Tsc](nationalinstruments-rfmx-gsmmx-rfmxgsmmxburstsynchronizationtype.html) and the [SetAutoTscDetectionEnabled(string, RFmxGsmMXAutoTscDetectionEnabled)](nationalinstruments-rfmx-gsmmx-rfmxgsmmx-setautotscdetectionenabled__string-rfmxgsmmxautotscdetectionenabled.html) method to [False](nationalinstruments-rfmx-gsmmx-rfmxgsmmxautotscdetectionenabled.html). For access burst Tsc0, Tsc1, and Tsc2 are applicable. Use "slot(n)" as the selector string to configure or read this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.GsmMX](nationalinstruments-rfmx-gsmmx.html)

public enum RFmxGsmMXTsc

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Tsc0 | 0 | The measurement uses training sequence code 0. |
| Tsc1 | 1 | The measurement uses training sequence code 1. |
| Tsc2 | 2 | The measurement uses training sequence code 2. |
| Tsc3 | 3 | The measurement uses training sequence code 3. |
| Tsc4 | 4 | The measurement uses training sequence code 4. |
| Tsc5 | 5 | The measurement uses training sequence code 5. |
| Tsc6 | 6 | The measurement uses training sequence code 6. |
| Tsc7 | 7 | The measurement uses training sequence code 7. |

Parent topic:

NationalInstruments.RFmx.GsmMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-gsmmx.html language=enus -->
## TOPIC 00335: NationalInstruments.RFmx.GsmMX

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-gsmmx.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-gsmmx.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionRFmxGsmMXDefines a root class which is used to identify and control GSM signal configuration. RFmxGsmMXConstantsSpecifies constants for I/O terminals. RFmxGsmMXModAccRepresents the ModAcc measurement. RFmxGsmMXModAccConfigurationProvides methods to configure the ModAcc measurem

### NationalInstruments.RFmx.GsmMX

#### Classes

| Name | Description |
| --- | --- |
| RFmxGsmMX | Defines a root class which is used to identify and control GSM signal configuration. |
| RFmxGsmMXConstants | Specifies constants for I/O terminals. |
| RFmxGsmMXModAcc | Represents the ModAcc measurement. |
| RFmxGsmMXModAccConfiguration | Provides methods to configure the ModAcc measurement. |
| RFmxGsmMXModAccResults | Provides methods to fetch and read the ModAcc measurement results. |
| RFmxGsmMXOrfs | Represents the ORFS measurement. |
| RFmxGsmMXOrfsConfiguration | Provides methods to configure the ORFS measurement. |
| RFmxGsmMXOrfsResults | Provides methods to fetch and read the ORFS measurement results. |
| RFmxGsmMXPvt | Represents the PVT measurement. |
| RFmxGsmMXPvtConfiguration | Provides methods to configure the PVT measurement. |
| RFmxGsmMXPvtResults | Provides methods to fetch and read the PVT measurement results. |
| RFmxGsmMXSubObject | Represents members that are common to all sub-object of RFmxGsmMX classes. |

#### Interfaces

None

#### Structures

None

#### Enumerations

| Name | Description |
| --- | --- |
| RFmxGsmMXAutoTscDetectionEnabled | Specifies whether the measurement automatically detects the training sequence code (TSC). |
| RFmxGsmMXBand | Specifies the operation band. |
| RFmxGsmMXBurstSynchronizationType | Specifies the method used to synchronize the burst. |
| RFmxGsmMXBurstType | Specifies the burst type. Use "slot(n)" as the selector string to configure or read this method. |
| RFmxGsmMXDigitalEdgeTriggerEdge | Specifies the active edge for the trigger. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to DigitalEdge. |
| RFmxGsmMXHBFilterWidth | Specifies the filter width when you set the SetBurstType(string, RFmxGsmMXBurstType) method to HB. Use "slot(n)" as the selector string to configure or read this method. |
| RFmxGsmMXIQPowerEdgeTriggerLevelType | Specifies the reference for the SetIQPowerEdgeTriggerLevel(string, double) method. The IQ Power Edge Level Type method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge. |
| RFmxGsmMXIQPowerEdgeTriggerSlope | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the SetIQPowerEdgeTriggerLevel(string, double) method with the slope you specify. This method is used only when you set the SetTriggerType(string, RFmxGsmMXTriggerType) method to IQPowerEdge. |
| RFmxGsmMXLimitedConfigurationChange | Specifies the set of properties that are considered by RFmx in the locked signal configuration state. |
| RFmxGsmMXLinkDirection | Specifies the direction for which the frequency is calculated. Only Uplink is supported. |
| RFmxGsmMXMeasurementTypes | Specifies the type of measurement. |
| RFmxGsmMXModAccAveragingEnabled | Specifies whether to enable averaging for the modulation accuracy (ModAcc) measurement. |
| RFmxGsmMXModAccDetectedTsc | Returns the detected training sequence code (TSC) if you set the SetBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType) method to Tsc. Use "slot(n)" as the selector string to read this result. When the SetMeasurementInterval(string, RFmxGsmMXModAccMeasurementInterval) method is set to TimeslotAtOffset, Detected TSC array has one element and the Detected TSC is returned at index 0. |
| RFmxGsmMXModAccDroopCompensationEnabled | Specifies whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results. |
| RFmxGsmMXModAccMeasurementInterval | Specifies whether the measurement is performed on a single specified timeslot or across multiple timeslots. |
| RFmxGsmMXModulationType | Specifies the modulation scheme used for the signal. Use "slot(n)" as the selector string to configure or read this method. |
| RFmxGsmMXOrfsAveragingEnabled | Specifies whether to enable averaging for the output radio frequency spectrum (ORFS) measurement. |
| RFmxGsmMXOrfsAveragingType | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the output radio frequency spectrum (ORFS) measurement. |
| RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc | Specifies whether to include the training sequence code (TSC) portion of the burst in the output radio frequency spectrum (ORFS) measurement. |
| RFmxGsmMXOrfsEvaluationSymbolsScope | Specifies the modulation power measurements that will use the part of burst configured using the ConfigureEvaluationSymbols(string, double, RFmxGsmMXOrfsEvaluationSymbolsIncludeTsc, double) method. |
| RFmxGsmMXOrfsMeasurementInterval | Specifies whether the measurement is performed on a single specified timeslot or across multiple timeslots. |
| RFmxGsmMXOrfsMeasurementType | Specifies the type of spectral distortion to be measured. |
| RFmxGsmMXOrfsNoiseCompensationEnabled | Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Noise compensation is applicable only on modulation offsets and not on switching offsets. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832. |
| RFmxGsmMXOrfsOffsetFrequencyMode | Specifies the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements. |
| RFmxGsmMXPropertyId | Specifies all the attribute identifiers. |
| RFmxGsmMXPvtAveragingEnabled | Specifies whether to enable averaging for the power versus time (PVT) measurement. |
| RFmxGsmMXPvtAveragingType | Specifies the averaging type for multiple acquisitions. |
| RFmxGsmMXPvtMeasurementStatus | Indicates the overall measurement status based on standard-defined limits. |
| RFmxGsmMXPvtSlotMeasurementStatus | Indicates the power versus time (PVT) measurement status for a particular slot. Use "slot(n)" as the selector string to read this method. |
| RFmxGsmMXSignalStructure | Specifies whether the signal is bursted or continuous. For bursted signal and continuous signals, set the SetTriggerType(string, RFmxGsmMXTriggerType) to IQPowerEdge and None, respectively. |
| RFmxGsmMXTriggerMinimumQuietTimeMode | Specifies whether the measurement computes the minimum quiet time used for triggering. |
| RFmxGsmMXTriggerType | Specifies the trigger type. |
| RFmxGsmMXTsc | Specifies the training sequence code (TSC) to use. This method is applicable only when you set the SetBurstSynchronizationType(string, RFmxGsmMXBurstSynchronizationType) method to Tsc and the SetAutoTscDetectionEnabled(string, RFmxGsmMXAutoTscDetectionEnabled) method to False. For access burst Tsc0, Tsc1, and Tsc2 are applicable. Use "slot(n)" as the selector string to configure or read this method. |

#### Delegates

None

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxgsmmxextension-getgsmsignalconfiguration__this-string.html language=enus -->
## TOPIC 00336: GetGsmSignalConfiguration(this RFmxInstrMX, string)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxgsmmxextension-getgsmsignalconfiguration__this-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxgsmmxextension-getgsmsignalconfiguration__this-string.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a GSM signal configuration for specified signal name. Existing GSM signal configuration is returned if specified signal name exists. SyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic static RFmxGsmMX GetGsmSignalConfiguration(this RFmxInstrMX instrSession, string signalName)ParametersN

### GetGsmSignalConfiguration(this RFmxInstrMX, string)

Creates a GSM signal configuration for specified signal name. Existing GSM signal configuration is returned if specified signal name exists.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public static [RFmxGsmMX](nationalinstruments-rfmx-gsmmx-rfmxgsmmx.html) GetGsmSignalConfiguration(this RFmxInstrMX instrSession, string signalName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| instrSession | this RFmxInstrMX | Specifies an RFmxInstr session. |
| signalName | string | Specifies a signal name. |

#### Returns

Returns an object of type RFmxGsmMX.

Parent topic:

RFmxGsmMXExtension Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxgsmmxextension-getgsmsignalconfiguration__this.html language=enus -->
## TOPIC 00337: GetGsmSignalConfiguration(this RFmxInstrMX)

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxgsmmxextension-getgsmsignalconfiguration__this.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxgsmmxextension-getgsmsignalconfiguration__this.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new default GSM signal configuration if it doesn't exist; otherwise, it returns the existing default GSM signal configuration. SyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic static RFmxGsmMX GetGsmSignalConfiguration(this RFmxInstrMX instrSession)ParametersNameTypeDescriptioninstr

### GetGsmSignalConfiguration(this RFmxInstrMX)

Creates a new default GSM signal configuration if it doesn't exist; otherwise, it returns the existing default GSM signal configuration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public static [RFmxGsmMX](nationalinstruments-rfmx-gsmmx-rfmxgsmmx.html) GetGsmSignalConfiguration(this RFmxInstrMX instrSession)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| instrSession | this RFmxInstrMX | Specifies an instr session. |

#### Returns

Returns an object of type RFmxGsmMX.

Parent topic:

RFmxGsmMXExtension Class

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxgsmmxextension.html language=enus -->
## TOPIC 00338: RFmxGsmMXExtension Class

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxgsmmxextension.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxgsmmxextension.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides extension methods to create GSM signal configuration. These methods are added to RFmxInstrMX class. Derives fromNoneSyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic class RFmxGsmMXExtensionRemarksFor more information about RFmx Instruments, refer to the RFmx Instruments Help.Thread S

### RFmxGsmMXExtension Class

Provides extension methods to create GSM signal configuration. These methods are added to RFmxInstrMX class.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public class RFmxGsmMXExtension

#### Remarks

For more information about RFmx Instruments, refer to the RFmx Instruments Help.

#### Thread Safety

Any public static members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| GetGsmSignalConfiguration(this RFmxInstrMX, string) | Creates a GSM signal configuration for specified signal name. Existing GSM signal configuration is returned if specified signal name exists. |
| GetGsmSignalConfiguration(this RFmxInstrMX) | Creates a new default GSM signal configuration if it doesn't exist; otherwise, it returns the existing default GSM signal configuration. |

Parent topic:

NationalInstruments.RFmx.InstrMX

<!--NI_TOPIC bundle=rfmxgsm-dotnet-api-ref path=nationalinstruments-rfmx-instrmx.html language=enus -->
## TOPIC 00339: NationalInstruments.RFmx.InstrMX

- bundle_id: `rfmxgsm-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx.html
- document_id: `rfmxgsm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionRFmxGsmMXExtensionProvides extension methods to create GSM signal configuration. These methods are added to RFmxInstrMX class. InterfacesNoneStructuresNoneEnumerationsNoneDelegatesNone

### NationalInstruments.RFmx.InstrMX

#### Classes

| Name | Description |
| --- | --- |
| RFmxGsmMXExtension | Provides extension methods to create GSM signal configuration. These methods are added to RFmxInstrMX class. |

#### Interfaces

None

#### Structures

None

#### Enumerations

None

#### Delegates

None
